#!/usr/bin/env python3
"""The Max dictionary rule for maxdraco.com posts (Max, 2026-11-11).

"Like Wikipedia": when a post names an outside tool, technology, place or thing,
its FIRST mention links to that term's page at /dictionary/<term>/. Each page
lives at content/dictionary/<term>.md and declares, in its front matter:

    title: "OPNsense"
    term_kind: tool               # tool | technology | place | thing
    summary: "one-line definition"
    match: ['\\bOPNsense\\b']     # regexes (case-insensitive) that mean a post names it
    sources:                      # primary/official source FIRST, with primary: true
      - {title: ..., url: https://..., publisher: ..., primary: true}

A post links a term with the shortcode  {{< term "opnsense" >}}  (link text =
the page title) or  {{< term "grafana-loki" "Loki" >}}  (own text), or a plain
markdown link to /dictionary/<term>/.

Over the posts a build will publish, `check` refuses when a post
  1. names a known term without linking it, or its first mention isn't the link;
  2. links a term that has no page, or whose page is still a draft (Max approves
     every page's copy before a published post may lean on it);
and, for every page, when its front matter is incomplete (no summary, no
primary source first, a non-https source, a regex Hugo's RE2 can't run).

    python3 tools/dictionary.py check     # publish mode: exit 1 on a break (preview.sh, deploy)
    python3 tools/dictionary.py plan      # drafts too: list what each draft still
                                          # needs; exit 1 only on broken pages/links
    python3 tools/dictionary.py sync      # hand source URLs to the homelab checker and pull
                                          # its health into data/source_health.json (never fails)

Our OWN systems (badgescope, party...) are not dictionary terms: they are
sequenced by concepts.yaml / tools/concepts.py.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from concepts import _split, _when, load_posts, published  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KINDS = ("tool", "technology", "place", "thing")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# RE2 (Hugo's findRE) has no lookaround or backreferences.
NOT_RE2 = re.compile(r"\(\?[=!<]|\\[1-9]")

SHORTCODE = re.compile(r'\{\{[<%]\s*term\s+"?([A-Za-z0-9-]+)"?(?:\s+"[^"]*")?\s*[>%]\}\}')
MD_LINK = re.compile(r'\[[^\]]*\]\((?:https://maxdraco\.com)?/dictionary/([A-Za-z0-9-]+)/?\)')
MASKS = [
    re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.M | re.S),   # fenced code
    re.compile(r"`[^`\n]+`"),                               # inline code
    re.compile(r"<!--.*?-->", re.S),                        # comments
    re.compile(r"\{\{[<%].*?[>%]\}\}", re.S),               # any other shortcode
    re.compile(r"\]\([^)]*\)"),                             # link targets
    re.compile(r"https?://\S+"),                            # bare URLs
    re.compile(r"^#{1,6} .*$", re.M),                       # headings: link in the body instead
]

SSH_KUBECTL = ["ssh", "-o", "ConnectTimeout=8", "-o", "BatchMode=yes", "fat",
               "sudo -n kubectl -n homelab"]
CONFIGMAP = "dictionary-sources"


def load_terms(dict_dir: str) -> dict:
    terms = {}
    if not os.path.isdir(dict_dir):
        return terms
    for name in sorted(os.listdir(dict_dir)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        with open(os.path.join(dict_dir, name)) as fh:
            fm, body = _split(fh.read())
        slug = str(fm.get("slug") or name[:-3])
        terms[slug] = {
            "file": name, "slug": slug, "fm": fm, "body": body,
            "title": fm.get("title") or slug,
            "draft": bool(fm.get("draft", False)),
            "match": [str(p) for p in (fm.get("match") or [])],
            "sources": list(fm.get("sources") or []),
        }
    return terms


def section_draft(dict_dir: str) -> bool:
    path = os.path.join(dict_dir, "_index.md")
    if not os.path.exists(path):
        return True
    with open(path) as fh:
        fm, _ = _split(fh.read())
    return bool(fm.get("draft", False))


def page_problems(t: dict) -> list[str]:
    out = []
    fm = t["fm"]
    if not SLUG.match(t["slug"]):
        out.append(f"slug '{t['slug']}' must be lowercase words joined by '-'")
    for key in ("title", "summary"):
        if not str(fm.get(key) or "").strip():
            out.append(f"no `{key}`")
    if fm.get("term_kind") not in KINDS:
        out.append(f"`term_kind` must be one of {', '.join(KINDS)}")
    if not t["match"]:
        out.append("no `match` regexes: the check can't see a post naming it")
    for p in t["match"]:
        try:
            re.compile(p)
        except re.error as e:
            out.append(f"match {p!r} is not a regex: {e}")
            continue
        if NOT_RE2.search(p):
            out.append(f"match {p!r} uses lookaround/backreferences, which Hugo's RE2 can't run")
    if not t["sources"]:
        out.append("no `sources`")
    for i, s in enumerate(t["sources"]):
        if not isinstance(s, dict) or not s.get("url") or not s.get("title"):
            out.append(f"source {i + 1} needs `title` and `url`")
            continue
        if not str(s["url"]).startswith("https://"):
            out.append(f"source {s['url']} is not https")
    if t["sources"] and isinstance(t["sources"][0], dict) and not t["sources"][0].get("primary"):
        out.append("the first source must be the primary/official one (`primary: true`)")
    if not t["body"].strip():
        out.append("no definition in the body")
    return out


def _mask(body: str) -> str:
    for rx in MASKS:
        body = rx.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), body)
    return body


def _line(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def scan(body: str):
    """-> (links {slug: [pos]}, masked body). Positions index into `body`."""
    links: dict[str, list[int]] = {}
    for rx in (SHORTCODE, MD_LINK):
        for m in rx.finditer(body):
            links.setdefault(m.group(1).lower(), []).append(m.start())
    masked = body
    for rx in (SHORTCODE, MD_LINK):
        masked = rx.sub(lambda m: " " * len(m.group(0)), masked)
    return links, _mask(masked)


def post_problems(post: dict, terms: dict, publish: bool) -> list[str]:
    body = post["body"]
    links, masked = scan(body)
    off = post.get("line_offset", 0)

    def _line(text, pos):  # file line numbers, front matter included
        return text.count("\n", 0, pos) + 1 + off
    out = []
    for slug, where in sorted(links.items()):
        if slug not in terms:
            out.append(f"line {_line(body, where[0])}: links dictionary term '{slug}', which has no "
                       f"page (write content/dictionary/{slug}.md)")
        elif publish and terms[slug]["draft"]:
            out.append(f"links '{slug}', but dictionary/{slug} is still a draft "
                       f"(Max approves the page, then draft: false)")
    for slug, t in terms.items():
        mentions = [m.start() for p in t["match"] for m in re.finditer(p, masked, re.I)]
        if not mentions:
            continue
        first = min(mentions)
        if slug not in links:
            out.append(f"line {_line(body, first)}: names {t['title']} without linking it; "
                       f'first mention -> {{{{< term "{slug}" >}}}}')
        elif first < min(links[slug]):
            out.append(f"line {_line(body, first)}: first mention of {t['title']} is not the "
                       f"linked one (link is on line {_line(body, min(links[slug]))})")
    return out


def check(posts: list[dict], terms: dict, now: datetime, publish: bool,
          index_draft: bool = False) -> tuple[dict, dict]:
    """-> ({page file: [problem]}, {post file: [problem]}) for what the build ships."""
    pages = {}
    for t in terms.values():
        if publish and t["draft"]:
            continue
        out = page_problems(t)
        if out:
            pages[t["file"]] = out
    if publish and index_draft and any(not t["draft"] for t in terms.values()):
        pages["_index.md"] = ["a term page is published but the /dictionary/ index is still a draft"]
    built = [p for p in posts if published(p, now, drafts=not publish)]
    return pages, {p["file"]: o for p in built if (o := post_problems(p, terms, publish))}


def sources_doc(terms: dict) -> dict:
    out = []
    for t in terms.values():
        for i, s in enumerate(t["sources"]):
            if isinstance(s, dict) and s.get("url"):
                out.append({"url": s["url"], "term": t["slug"], "title": s.get("title", ""),
                            "primary": i == 0})
    return {"generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "sources": out}


def sync(root: str, terms: dict) -> int:
    """Best effort: a build must never fail because the homelab is unreachable."""
    data_file = os.path.join(root, "data", "source_health.json")
    patch = json.dumps({"data": {"sources.json": json.dumps(sources_doc(terms), indent=1)}})
    try:
        subprocess.run(SSH_KUBECTL[:-1] + [SSH_KUBECTL[-1] + f" patch configmap {CONFIGMAP} "
                                           "--type merge --patch-file /dev/stdin"],
                       input=patch.encode(), check=True, capture_output=True, timeout=40)
        r = subprocess.run(SSH_KUBECTL[:-1] + [SSH_KUBECTL[-1] + f" get configmap {CONFIGMAP} -o json"],
                           check=True, capture_output=True, timeout=40)
        health = json.loads(json.loads(r.stdout)["data"].get("health.json") or "{}")
    except (subprocess.SubprocessError, OSError, ValueError, KeyError) as e:
        err = getattr(e, "stderr", b"") or b""
        print(f"dictionary: sync skipped ({type(e).__name__} {err.decode(errors='replace').strip()[:160]}); "
              f"pages show the last pulled health" + ("" if os.path.exists(data_file) else " (none yet)"),
              file=sys.stderr)
        return 0
    os.makedirs(os.path.dirname(data_file), exist_ok=True)
    with open(data_file, "w") as fh:
        json.dump(health, fh, indent=1, sort_keys=True)
    n = len(health.get("sources", {}))
    dead = sum(1 for r in health.get("sources", {}).values() if r.get("status") == "dead")
    print(f"dictionary: health for {n} sources ({dead} dead) from {health.get('generated_at', 'never')}",
          file=sys.stderr)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("check", "plan", "sync"))
    ap.add_argument("--root", default=ROOT)
    a = ap.parse_args(argv)
    dict_dir = os.path.join(a.root, "content", "dictionary")
    terms = load_terms(dict_dir)
    if a.mode == "sync":
        return sync(a.root, terms)
    blog = os.path.join(a.root, "content", "blog")
    posts = load_posts(blog)
    for p in posts:
        with open(os.path.join(blog, p["file"])) as fh:
            full = fh.read()
        p["line_offset"] = full[:len(full) - len(p["body"])].count("\n")
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    publish = a.mode == "check"
    pages, postp = check(posts, terms, now, publish, index_draft=section_draft(dict_dir))
    for f, out in pages.items():
        for line in out:
            print(f"dictionary: refusing: dictionary/{f}: {line}", file=sys.stderr)
    label = "refusing" if publish else "todo"
    hard = bool(pages)
    for f, out in postp.items():
        for line in out:
            # In plan mode an unlinked mention is a to-do for a draft; a link to a missing
            # page breaks the Hugo build itself, so it stays an error.
            broken = "has no page" in line
            hard = hard or publish or broken
            print(f"dictionary: {'refusing' if broken else label}: {f}: {line}", file=sys.stderr)
    if hard:
        print("dictionary: link each term's first mention to its page; Max approves new pages "
              "(rule: tools/dictionary.py)", file=sys.stderr)
        return 1
    print(f"dictionary: {len(terms)} terms, every named term linked" if publish else
          f"dictionary: {len(terms)} terms; {len(postp)} draft(s) with terms to link", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
