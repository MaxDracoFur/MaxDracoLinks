#!/usr/bin/env python3
"""No-jargon gate for maxdraco.com posts (Max, 2026-11-15: "can we have a no jargon rule").

Written after the venue-licence post was pulled: it said "(my account)" at readers who had never
been told what the label meant, called one sentence of ordinance "the trap", and sold itself as
"the two-minute check".

    python3 tools/jargon_check.py check   # published posts; warns, never blocks
    python3 tools/jargon_check.py plan    # drafts too

Three things a machine can see:

1. **Evidence labels** -- "(measured 11-05)", "(inferred)", "(my account)" -- belong to the hacker
   INC posts, where the format introduces them. Anywhere else they are our shorthand at a stranger.
2. **Our own process words** -- lane test, INC format, front matter, cover_source, copy review,
   the rotation -- are how the site is made, never what it says. Flagged in every post.
3. **Headings that sell** -- "The trap in ...", "The two-minute check", "What nobody tells you",
   "The secret to ..." -- a heading says what the section shows, or it tells the reader what to do.

The fourth test is the real one and no regex can run it: **would someone outside the field follow
this?** If a term is unavoidable (Public Place of Amusement licence, disc ID), it is explained in
plain words the first time or linked to its dictionary page. That stays a person's job.

Warnings only. The wording is always Max's.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from concepts import _split, _when  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EVIDENCE = re.compile(
    r"\(\s*(measured\b|inferred\b|my account\b|my recollection\b|my opinion\b|from my notes\b|quoted from\b)",
    re.I)

# Words from the machinery of making the site. None of them mean anything to a reader.
PROCESS = re.compile(
    r"\blane test\b|\bINC format\b|\bfront matter\b|\bcover_source\b|\bcover_image\b|\bsearch_phrase\b|"
    r"\bcopy review\b|\bthe rotation\b|\brotation slot\b|\bpublish gate\b|\bthe stage app\b|\bdraft gate\b",
    re.I)

HYPE_HEADING = re.compile(
    r"^#{1,6}\s+(?:the\s+)?(?:"
    r"trap\b|"
    r"(?:\d+|one|two|three|four|five|six|ten|fifteen|thirty|sixty)[- ](?:second|minute|hour)\b|"
    r"secret\b|"
    r"what nobody\b|"
    r"what no one\b|"
    r"the one (?:thing|trick)\b"
    r")", re.I | re.M)

# Masks: a shortcode, a link target, code and comments are not prose.
MASKS = [re.compile(r"^(```|~~~).*?^\1[^\n]*$", re.M | re.S), re.compile(r"`[^`\n]+`"),
         re.compile(r"<!--.*?-->", re.S), re.compile(r"\{\{[<%].*?[>%]\}\}", re.S),
         re.compile(r"\]\([^)]*\)")]


def prose(body: str) -> str:
    for m in MASKS:
        body = m.sub(" ", body)
    return body


def problems(root: str, now: datetime, drafts: bool):
    """-> [(file, [(kind, line_no, excerpt)])]"""
    blog = os.path.join(root, "content", "blog")
    out = []
    for name in sorted(os.listdir(blog)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        fm, body = _split(open(os.path.join(blog, name)).read())
        when, draft = _when(fm.get("date")), bool(fm.get("draft", False))
        publishes = not draft and (when is None or when <= now)
        if not publishes and not drafts:
            continue
        hacker = str(fm.get("series") or "").strip().strip('"') == "hacker"
        found = []
        for n, line in enumerate(prose(body).splitlines(), 1):
            if not hacker and EVIDENCE.search(line):
                found.append(("evidence label outside a hacker post", n, line.strip()[:90]))
            if PROCESS.search(line):
                found.append(("our own word for how the site is made", n, line.strip()[:90]))
            if HYPE_HEADING.search(line):
                found.append(("heading sells instead of saying or instructing", n, line.strip()[:90]))
        if found:
            out.append((name, found))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("check", "plan"))
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--now", help="YYYY-MM-DD (tests)")
    a = ap.parse_args(argv)
    now = datetime.fromisoformat(a.now) if a.now else datetime.now(timezone.utc).replace(tzinfo=None)
    found = problems(a.root, now, drafts=a.mode == "plan")
    n = 0
    for f, items in found:
        for kind, line, excerpt in items:
            n += 1
            print(f"jargon: {f}: line {line}: {kind}: {excerpt}")
    print(f"jargon: {n} thing(s) to say plainly" if n else "jargon: every post is in plain words")
    return 0   # always: the wording is Max's


if __name__ == "__main__":
    sys.exit(main())
