#!/usr/bin/env python3
"""Concept sequencing for maxdraco.com posts (rule: Max, 2026-11-05).

A post may only lean on a concept a reader has already been given. Concepts are
listed in concepts.yaml. Each post declares, in its front matter:

    introduces: [badgescope]        # this post is where readers meet it
    uses: [badgescope]              # this post assumes readers already have

and the check enforces, over the posts a build will publish:

  1. every concept a post's body talks about (concepts.yaml `match`) is
     declared in `introduces` or `uses` -- no silent jargon;
  2. every `uses` concept is introduced by another post in the same build
     with a strictly EARLIER date -- the build-up comes first;
  3. every declared concept exists in concepts.yaml.

    python3 tools/concepts.py check            # publish mode: exit 1 on a break
    python3 tools/concepts.py plan             # include drafts; show what each
                                               # post is waiting on (exit 0)
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tomllib
from datetime import date, datetime, timezone

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_concepts(path: str) -> dict:
    with open(path) as fh:
        raw = yaml.safe_load(fh) or {}
    return {k: {"what": v.get("what", ""),
                "match": [re.compile(p, re.I) for p in v.get("match", [])]}
            for k, v in raw.items()}


def _split(text: str):
    for fence, parse in (("---", yaml.safe_load), ("+++", tomllib.loads)):
        if text.startswith(fence + "\n"):
            end = text.find("\n" + fence, len(fence))
            if end != -1:
                return parse(text[len(fence) + 1:end]) or {}, text[end + len(fence) + 1:]
    return {}, text


def _when(v):
    if v is None or v == "":
        return None
    if isinstance(v, str):
        v = datetime.fromisoformat(v.replace("Z", "+00:00"))
    if isinstance(v, datetime):
        return v.astimezone(timezone.utc).replace(tzinfo=None) if v.tzinfo else v
    if isinstance(v, date):
        return datetime(v.year, v.month, v.day)
    raise ValueError(f"unreadable date {v!r}")


def load_posts(blog_dir: str) -> list[dict]:
    posts = []
    for name in sorted(os.listdir(blog_dir)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        with open(os.path.join(blog_dir, name)) as fh:
            fm, body = _split(fh.read())
        posts.append({
            "file": name,
            "slug": str(fm.get("slug") or name[:-3]),
            "title": fm.get("title") or name,
            "draft": bool(fm.get("draft", False)),
            "date": _when(fm.get("date")),
            "introduces": list(fm.get("introduces") or []),
            "uses": list(fm.get("uses") or []),
            "body": body,
        })
    return posts


def published(post: dict, now: datetime, drafts: bool) -> bool:
    """What `hugo` (or `hugo --buildDrafts --buildFuture`) would build."""
    if drafts:
        return True
    return not post["draft"] and (post["date"] is None or post["date"] <= now)


def check(posts: list[dict], concepts: dict, now: datetime, drafts: bool = False):
    """Return {file: [problem, ...]} for posts in the build."""
    built = [p for p in posts if published(p, now, drafts)]
    oldest = datetime.min
    problems: dict[str, list[str]] = {}
    for p in built:
        out = []
        declared = set(p["introduces"]) | set(p["uses"])
        for c in sorted(declared - concepts.keys()):
            out.append(f"'{c}' is not in concepts.yaml")
        for c, spec in concepts.items():
            if c not in declared and any(rx.search(p["body"]) for rx in spec["match"]):
                out.append(f"talks about '{c}' without declaring it "
                           f"(add to `introduces` or `uses`)")
        for c in p["uses"]:
            if c not in concepts:
                continue
            when = p["date"] or oldest
            intro = [q for q in built if q is not p and c in q["introduces"]
                     and (q["date"] or oldest) < when]
            if not intro:
                out.append(f"uses '{c}' ({concepts[c]['what']}) but no earlier "
                           f"published post introduces it")
        if out:
            problems[p["file"]] = out
    return problems


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("check", "plan"))
    ap.add_argument("--root", default=ROOT)
    a = ap.parse_args(argv)
    concepts = load_concepts(os.path.join(a.root, "concepts.yaml"))
    posts = load_posts(os.path.join(a.root, "content", "blog"))
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    drafts = a.mode == "plan"
    problems = check(posts, concepts, now, drafts=drafts)
    label = "sequencing" if drafts else "refusing"
    for f, out in problems.items():
        for line in out:
            print(f"concepts: {label}: {f}: {line}", file=sys.stderr)
    if a.mode == "check":
        if problems:
            print("concepts: publish the introducing posts first (rule in concepts.yaml)",
                  file=sys.stderr)
            return 1
        print("concepts: every concept used is introduced earlier", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
