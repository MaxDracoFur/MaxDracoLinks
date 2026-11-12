#!/usr/bin/env python3
"""The Max dictionary rule for maxdraco.com posts (Max, 2026-11-11).

"Like Wikipedia": when a post names an outside tool, technology, place or thing,
its FIRST mention links to that term's page at /dictionary/<term>/. Each page
lives at content/dictionary/<term>.md and declares, in its front matter:

    title: "OPNsense"
    term_kind: tool               # what it is: see KINDS
    topics: [networking]          # what area it belongs to; first = primary (breadcrumb)
    see_also: [syslog]            # optional: other terms worth reading next
    summary: "one-line definition"
    match: ['\\bOPNsense\\b']     # regexes (case-insensitive) that mean a post names it
    sources:                      # primary/official source FIRST, with primary: true
      - {title: ..., url: https://..., publisher: ..., primary: true}
    classification:               # optional: where security catalogues file it
      - {standard: attack, clause: T1557, topic: Adversary-in-the-Middle,
         url: https://attack.mitre.org/techniques/T1557/}

`classification` uses the Guild's citation shape (docker-guild/backend/catalog.py cites
(standard, clause, topic) and keys its standards the same way: attack/cwe/capec/cpe/
sp800-53/atlas/csf), so the Guild can read these as crosswalk rows. Each entry's url must be
the catalogue's own canonical address for that id (CLASSIFY below), and goes through the
same daily source-health check as `sources`.

A post links a term with the shortcode  {{< term "opnsense" >}}  (link text =
the page title) or  {{< term "grafana-loki" "Loki" >}}  (own text), or a plain
markdown link to /dictionary/<term>/.

Over the posts a build will publish, and over every dictionary page it ships (pages link
each other the same way, so a reader can walk from term to term), `check` refuses when a post
  1. names a known term without linking it, or its first mention isn't the link;
  2. links a term that has no page, or whose page is still a draft (Max approves
     every page's copy before a published post may lean on it);
and, for every page, when its front matter is incomplete (no summary, no
primary source first, a non-https source, a regex Hugo's RE2 can't run).

    python3 tools/dictionary.py check     # publish mode: exit 1 on a break (preview.sh, deploy)
    python3 tools/dictionary.py plan      # drafts too: list what each draft still
                                          # needs; exit 1 only on broken pages/links
    python3 tools/dictionary.py link      # link every unlinked first mention in place (then git diff)
    python3 tools/dictionary.py candidates  # report names the site uses that have no page yet
    python3 tools/dictionary.py sync      # hand source URLs to the homelab checker and pull
                                          # its health into data/source_health.json (never fails)

Wiki pattern (Max 2026-11-11, "start taxonomizing the dictionary"): every topic is a page
at content/dictionary/topics/<slug>.md (title + a paragraph saying what the area covers).
A term's `topics` must name those pages and `see_also` must name other terms; a published
term may not point at a draft topic or term. /dictionary/ browses by topic and A-Z.

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
KINDS = ("tool", "protocol", "standard", "format", "concept", "organisation", "place", "thing")
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
    re.compile(r"(?<![\w}])/[\w.\-{}]+(?:/[\w.\-{}]*)*"),        # URL paths: /api/v1/status
    re.compile(r"^#{1,6} .*$", re.M),                       # headings: link in the body instead
]

def _cprt(fw: str, el: str) -> str:
    return f"https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/{fw}/home?element={el}"


def _sp80053_el(cid: str) -> str:  # SC-8 -> SC-08, AU-6(3) -> AU-06(03): CPRT's element ids
    m = re.match(r"^([A-Z]{2})-(\d+)(?:\((\d+)\))?$", cid)
    return f"{m.group(1)}-{int(m.group(2)):02d}" + (f"({int(m.group(3)):02d})" if m.group(3) else "")


def _attack_url(cid: str) -> str:
    kind = {"T": "techniques", "M": "mitigations", "S": "software", "G": "groups"}[cid[0]]
    return f"https://attack.mitre.org/{kind}/{cid.replace('.', '/')}/"


# standard key -> (label, id pattern, canonical url for an id). Keys match the Guild's
# STANDARDS keys (catalog.py) and depth's source kinds (sourcing.py).
CLASSIFY = {
    "attack": ("MITRE ATT&CK", re.compile(r"^[TMSG]\d{4}(?:\.\d{3})?$"), _attack_url),
    "atlas": ("MITRE ATLAS", re.compile(r"^AML\.[TM]\d{4}(?:\.\d{3})?$"),
              lambda c: f"https://atlas.mitre.org/{'techniques' if c[4] == 'T' else 'mitigations'}/{c}"),
    "cwe": ("CWE", re.compile(r"^CWE-\d+$"),
            lambda c: f"https://cwe.mitre.org/data/definitions/{c[4:]}.html"),
    "capec": ("CAPEC", re.compile(r"^CAPEC-\d+$"),
              lambda c: f"https://capec.mitre.org/data/definitions/{c[6:]}.html"),
    "cpe": ("NVD CPE", re.compile(r"^cpe:2\.3:[aho]:[a-z0-9_.\-]+:[a-z0-9_.\-]+$"),
            lambda c: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword="
                      + c.replace(":", "%3A")),
    "sp800-53": ("NIST SP 800-53", re.compile(r"^[A-Z]{2}-\d+(?:\(\d+\))?$"),
                 lambda c: _cprt("SP_800_53_5_2_0", _sp80053_el(c))),
    "csf": ("NIST CSF 2.0", re.compile(r"^[A-Z]{2}\.[A-Z]{2}(?:-\d{2})?$"),
            lambda c: _cprt("CSF_2_0_0", c)),
}

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
            full = fh.read()
        fm, body = _split(full)
        slug = str(fm.get("slug") or name[:-3])
        terms[slug] = {
            "file": name, "slug": slug, "fm": fm, "body": body,
            "line_offset": full[:len(full) - len(body)].count("\n"),
            "title": fm.get("title") or slug,
            "draft": bool(fm.get("draft", False)),
            "match": [str(p) for p in (fm.get("match") or [])],
            "sources": list(fm.get("sources") or []),
            "classification": list(fm.get("classification") or []),
            "topics": [str(x) for x in (fm.get("topics") or [])],
            "see_also": [str(x) for x in (fm.get("see_also") or [])],
        }
    return terms


def load_topics(dict_dir: str) -> dict:
    topics = {}
    tdir = os.path.join(dict_dir, "topics")
    if not os.path.isdir(tdir):
        return topics
    for name in sorted(os.listdir(tdir)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        with open(os.path.join(tdir, name)) as fh:
            fm, body = _split(fh.read())
        slug = name[:-3]
        topics[slug] = {"file": f"topics/{name}", "slug": slug, "title": fm.get("title") or "",
                        "draft": bool(fm.get("draft", False)), "body": body}
    return topics


def topic_problems(t: dict) -> list[str]:
    out = []
    if not SLUG.match(t["slug"]):
        out.append(f"slug '{t['slug']}' must be lowercase words joined by '-'")
    if not str(t["title"]).strip():
        out.append("no `title`")
    if not t["body"].strip():
        out.append("no description: say in a paragraph what this area covers")
    return out


def section_draft(dict_dir: str) -> bool:
    path = os.path.join(dict_dir, "_index.md")
    if not os.path.exists(path):
        return True
    with open(path) as fh:
        fm, _ = _split(fh.read())
    return bool(fm.get("draft", False))


def page_problems(t: dict, topics: dict | None = None, terms: dict | None = None,
                  publish: bool = False) -> list[str]:
    """topics/terms given: also check that topics and see_also point at real pages (and, when
    publishing a published term, at published ones)."""
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
    for c in t.get("classification", []):
        if not isinstance(c, dict) or not all(c.get(k) for k in ("standard", "clause", "topic", "url")):
            out.append(f"classification {c!r} needs `standard`, `clause`, `topic` and `url`")
            continue
        std, cid = str(c["standard"]), str(c["clause"])
        if std not in CLASSIFY:
            out.append(f"classification standard '{std}' is not one of {', '.join(CLASSIFY)}")
            continue
        _, rx, url = CLASSIFY[std]
        if not rx.match(cid):
            out.append(f"classification {std} '{cid}' is not a valid {CLASSIFY[std][0]} id")
        elif c["url"] != url(cid):
            out.append(f"classification {std} {cid}: url should be {url(cid)}")
    if not t.get("topics"):
        out.append("no `topics`: name at least one area it belongs to (content/dictionary/topics/)")
    live = publish and not t.get("draft")
    if topics is not None:
        for slug in t.get("topics", []):
            if slug not in topics:
                out.append(f"topic '{slug}' has no page (write content/dictionary/topics/{slug}.md)")
            elif live and topics[slug]["draft"]:
                out.append(f"topic '{slug}' is still a draft")
    if terms is not None:
        for slug in t.get("see_also", []):
            if slug == t["slug"]:
                out.append("see_also lists the term itself")
            elif slug not in terms:
                out.append(f"see_also '{slug}' has no page")
            elif live and terms[slug]["draft"]:
                out.append(f"see_also '{slug}' is still a draft")
    if not t["body"].strip():
        out.append("no definition in the body")
    if re.search(r"^#{1,6} Why it.s on this site", t["body"], re.M | re.I):
        out.append("pages are written for readers: no 'Why it's on this site' section (Max 2026-11-11)")
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
          index_draft: bool = False, topics: dict | None = None) -> tuple[dict, dict]:
    """-> ({page file: [problem]}, {post file: [problem]}) for what the build ships."""
    pages = {}
    topics = {} if topics is None else topics
    for t in terms.values():
        if publish and t["draft"]:
            continue
        out = page_problems(t, topics, terms, publish)
        # Pages link each other the way posts link pages (Max 2026-11-11: "you should be able
        # to traverse the terms"). A page naming itself needs no link.
        others = {k: v for k, v in terms.items() if k != t["slug"]}
        out += post_problems(t, others, publish)
        if out:
            pages[t["file"]] = out
    for tp in topics.values():
        if publish and tp["draft"]:
            continue
        if out := topic_problems(tp):
            pages[tp["file"]] = out
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
        for c in t.get("classification", []):
            if isinstance(c, dict) and c.get("url"):
                out.append({"url": c["url"], "term": t["slug"], "primary": False,
                            "title": f"{c.get('standard')} {c.get('clause')} {c.get('topic', '')}".strip(),
                            "standard": c.get("standard"), "clause": c.get("clause")})
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


# ---- candidates: names the site uses that nothing covers yet (Max 2026-11-11: "scan my site for
# terms that should be linked"). A heuristic, so it reports and never gates. Each name it lists
# either gets a dictionary page or goes into NOT_TERMS_FILE after review, so the list can reach zero.
NOT_TERMS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dictionary_not_terms.txt")
CAND = re.compile(r"\b(?:[A-Z][a-z]+-[A-Z][a-z]+"            # Wi-Fi
                  r"|[A-Za-z]*[a-z][A-Z][A-Za-z0-9]*"          # WireGuard, macOS, iPhone
                  r"|[A-Z][A-Za-z0-9]*[A-Z0-9][A-Za-z0-9]*"   # VLAN, VLANs, WPA3, RP2040
                  r"|[A-Z][a-z0-9]+(?: [A-Z][a-z0-9]+)*)\b")   # Prometheus, Flipper Zero
FUNCTION_WORDS = set("""I A An The This That These Those It Its My Our Your Their His Her We You They He She
Me Us Them In On At Of For And But Or Nor If When What Why How Who Whom Where Then So Not No Yes To By As
Be Is Are Was Were Do Does Did Here There With Without From Into Onto Over Under After Before Since Until
While Each Every Some All Any Both Most More Less Also Just Only Even Still Now Today Tonight Yesterday
Tomorrow One Two Three Four Five Six Seven Eight Nine Ten Monday Tuesday Wednesday Thursday Friday Saturday
Sunday January February March April May June July August September October November December Jan Feb Mar
Apr Jun Jul Aug Sep Sept Oct Nov Dec OK Max Draco MaxDraco""".split())
SENTENCE_START = re.compile(r"(?:^|[.!?:|>*(\-]|\d\.)\s*$")


def _english() -> set:
    try:
        with open("/usr/share/dict/words") as fh:
            return {w.strip() for w in fh if w[:1].islower()}
    except OSError:
        return set()


def load_not_terms(path: str = NOT_TERMS_FILE) -> set:
    """The committed list plus its git-excluded .local twin (names that would hint at unpublished posts)."""
    out = set()
    for p in (path, path.replace(".txt", ".local.txt")):
        try:
            with open(p) as fh:
                out |= {ln.split("#")[0].strip() for ln in fh if ln.split("#")[0].strip()}
        except OSError:
            pass
    return out


def candidates(docs: dict, terms: dict, own: list, not_terms: set) -> list:
    """docs {file: markdown body} -> [(name, mentions, [files])], most widely used first."""
    masked = {f: scan(b)[1] for f, b in docs.items()}
    lower = {w for m in masked.values() for w in re.findall(r"\b[a-z][a-z]+\b", m)}
    english = _english()
    covered = [re.compile(p, re.I) for t in terms.values() for p in t["match"]]
    covered += [re.compile(p, re.I) for p in own]
    hits: dict = {}
    for f, m in masked.items():
        for tok in CAND.finditer(m):
            words = tok.group(0).split(" ")
            start = m.rfind("\n", 0, tok.start()) + 1
            initial = bool(SENTENCE_START.search(m[start:tok.start()]))
            while words:  # drop leading ordinary words: "In October", "The Kea"
                w = words[0]
                ordinary = (w in FUNCTION_WORDS or
                            (re.fullmatch(r"[A-Z][a-z]+", w) and
                             (w.lower() in lower or (initial and w.lower() in english))))
                if not ordinary:
                    break
                words, initial = words[1:], False
            name = " ".join(words)
            if not name or name in not_terms or (name.endswith("s") and name[:-1] in not_terms):
                continue
            if any(rx.search(name) for rx in covered):
                continue
            n, files = hits.setdefault(name, [0, set()])
            hits[name][0] += 1
            files.add(f)
    for name in [n for n in hits if n.endswith("s") and n[:-1] in hits]:  # VLANs -> VLAN
        n, files = hits.pop(name)
        hits[name[:-1]][0] += n
        hits[name[:-1]][1] |= files
    return sorted(((w, n, sorted(fs)) for w, (n, fs) in hits.items()),
                  key=lambda r: (-len(r[2]), -r[1], r[0]))


def autolink(body: str, terms: dict, self_slug: str | None = None) -> tuple[str, list]:
    """Wrap each term's first unlinked mention in {{< term >}}. -> (new body, [skipped notes]).
    A mention inside markdown link text is skipped (a link can't nest), and reported."""
    links, masked = scan(body)
    edits, skipped = [], []
    for slug, t in terms.items():
        if slug == self_slug or slug in links:
            continue
        found = [m for p in t["match"] for m in re.finditer(p, masked, re.I)]
        if not found:
            continue
        m = min(found, key=lambda x: x.start())
        line_start = body.rfind("\n", 0, m.start()) + 1
        before = body[line_start:m.start()]
        if before.count("[") > before.count("]"):
            skipped.append(f"{slug}: first mention is inside link text; link it by hand")
            continue
        text = body[m.start():m.end()]
        code = f'{{{{< term "{slug}" >}}}}' if text == t["title"] else f'{{{{< term "{slug}" "{text}" >}}}}'
        edits.append((m.start(), m.end(), code))
    # Two terms can match the same text ('Google' inside 'Google Analytics'). Keep the longest
    # match at each start and drop any edit overlapping one already kept, or the splices corrupt
    # each other.
    kept, end = [], -1
    for a, b, code in sorted(edits, key=lambda e: (e[0], -(e[1] - e[0]))):
        if a >= end:
            kept.append((a, b, code))
            end = b
    for a, b, code in reversed(kept):
        body = body[:a] + code + body[b:]
    return body, skipped


def report_candidates(root: str, terms: dict, posts: list) -> int:
    docs = {"blog/" + p["file"]: p["body"] for p in posts}
    for extra in ("_index.md", "about/index.md"):
        path = os.path.join(root, "content", extra)
        if os.path.exists(path):
            with open(path) as fh:
                docs[extra] = _split(fh.read())[1]
    own = []
    cpath = os.path.join(root, "concepts.yaml")
    if os.path.exists(cpath):
        from concepts import load_concepts
        own = [getattr(p, "pattern", p) for c in load_concepts(cpath).values() for p in c["match"]]
    rows = candidates(docs, terms, own, load_not_terms())
    for name, n, files in rows:
        print(f"{len(files):3d} pages {n:4d}x  {name:32s} {', '.join(files)}")
    print(f"dictionary: {len(rows)} candidate names; each gets a page or a line in "
          f"tools/dictionary_not_terms.txt", file=sys.stderr)
    return 0


def link_all(root: str, terms: dict, posts: list) -> int:
    """Rewrite posts and pages in place, linking each term's first mention. Review with git diff."""
    targets = [(os.path.join(root, "content", "blog", p["file"]), p["body"], None) for p in posts]
    targets += [(os.path.join(root, "content", "dictionary", t["file"]), t["body"], s)
                for s, t in terms.items()]
    changed = 0
    for path, body, own in targets:
        new, skipped = autolink(body, terms, own)
        for note in skipped:
            print(f"dictionary: link: {os.path.relpath(path, root)}: {note}", file=sys.stderr)
        if new != body:
            with open(path) as fh:
                full = fh.read()
            with open(path, "w") as fh:
                fh.write(full[:len(full) - len(body)] + new)
            changed += 1
    print(f"dictionary: linked first mentions in {changed} file(s)", file=sys.stderr)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("check", "plan", "sync", "candidates", "link"))
    ap.add_argument("--root", default=ROOT)
    a = ap.parse_args(argv)
    dict_dir = os.path.join(a.root, "content", "dictionary")
    terms = load_terms(dict_dir)
    if a.mode == "sync":
        return sync(a.root, terms)
    blog = os.path.join(a.root, "content", "blog")
    posts = load_posts(blog)
    if a.mode == "candidates":
        return report_candidates(a.root, terms, posts)
    if a.mode == "link":
        return link_all(a.root, terms, posts)
    for p in posts:
        with open(os.path.join(blog, p["file"])) as fh:
            full = fh.read()
        p["line_offset"] = full[:len(full) - len(p["body"])].count("\n")
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    publish = a.mode == "check"
    pages, postp = check(posts, terms, now, publish, index_draft=section_draft(dict_dir),
                         topics=load_topics(dict_dir))
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
