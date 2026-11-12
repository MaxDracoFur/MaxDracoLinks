#!/usr/bin/env python3
"""Title gate for maxdraco.com posts: the title carries a phrase people actually search for.

Why (Max 2026-11-12): "A Furby fan site, a Mayan ruins guide, and one ad account" says exactly what
the post shows and drew readers from Telegram and direct links, but in its first week none came from
a search engine (measured 11-12: 17 human pageviews, 0 search referrers). Nobody searches "Furby fan
site Mayan ruins"; they search "AdSense publisher ID". The worked example is in
docs/hacker-inc-format.md (Title) and https://maxdraco.com/blog/furbytoyshop-adsense-trail/.

    python3 tools/title_check.py check   # publish mode: exit 1 on a post dated on/after the rule
    python3 tools/title_check.py plan    # drafts too: list what each still needs; never fails

A post sets `search_phrase:` in front matter: the 2 to 6 words a stranger would type to find it.
The title must contain it (case, punctuation and spacing ignored), and must not open like a listicle
("10 ... Tricks"): the brand rule is plain titles, no BuzzFeed hooks.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from concepts import _split, _when  # noqa: E402

RULE_FROM = datetime(2026, 11, 13)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NUMBERS = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty)"
LISTICLE = re.compile(
    rf"^\s*(?:the\s+)?(?:top\s+)?{NUMBERS}\s+(?:\S+\s+){{0,6}}?"
    r"(?:tricks?|tips?|ways?|reasons?|things?|hacks?|secrets?|mistakes?|lookups?|tools?|steps?|facts?)\b",
    re.I)


def _norm(s: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s.lower()).split())


def why_not(title: str, phrase: str) -> list[str]:
    why = []
    if LISTICLE.search(title):
        why.append(f"title opens like a listicle ({title!r}): say plainly what the post shows")
    if not phrase:
        why.append("no search_phrase: set the 2-6 words a stranger would type to find this post")
    else:
        n = len(_norm(phrase).split())
        if not 2 <= n <= 6:
            why.append(f"search_phrase {phrase!r} is {n} word(s): use 2 to 6")
        elif f" {_norm(phrase)} " not in f" {_norm(title)} ":
            why.append(f"title doesn't contain its search_phrase {phrase!r}")
    return why


def problems(root: str, now: datetime, drafts: bool):
    """-> [(file, [why])] for posts in scope."""
    blog = os.path.join(root, "content", "blog")
    out = []
    for name in sorted(os.listdir(blog)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        fm, _ = _split(open(os.path.join(blog, name)).read())
        when, draft = _when(fm.get("date")), bool(fm.get("draft", False))
        publishes = not draft and (when is None or when <= now)
        if when is None or when < RULE_FROM:  # undated = written before the rule (as cover_check)
            continue
        if not publishes and not drafts:
            continue
        why = why_not(str(fm.get("title") or ""), str(fm.get("search_phrase") or "").strip())
        if why:
            out.append((name, why))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("check", "plan"))
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--now", help="YYYY-MM-DD (tests)")
    a = ap.parse_args(argv)
    now = datetime.fromisoformat(a.now) if a.now else datetime.now(timezone.utc).replace(tzinfo=None)
    found = problems(a.root, now, drafts=a.mode == "plan")
    label = "todo" if a.mode == "plan" else "refusing"
    for f, why in found:
        for w in why:
            print(f"titles: {label}: {f}: {w}")
    if found and a.mode == "check":
        return 1
    print(f"titles: {len(found)} post(s) need a searchable title" if found else
          "titles: every post's title carries its search phrase")
    return 0


if __name__ == "__main__":
    sys.exit(main())
