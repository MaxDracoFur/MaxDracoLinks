#!/usr/bin/env python3
"""Cover-image gate for maxdraco.com posts (rule Max 2026-11-12: "we need at least 1 image for the
CD album like cover that we pull from my nas of images/phone/ or create").

    python3 tools/cover_check.py check   # publish mode: exit 1 if a post dated on/after the rule
                                         # publishes without a cover, or its cover file is missing
    python3 tools/cover_check.py plan    # drafts too: list what each still needs; never fails

A cover is `cover_image: "/res/..."` in front matter (with `cover_alt`), a square, CD-album-style
image under assets/ (watermarked on build) or static/. Max's own photos come out of the stage app
(approved for one maxdraco destination, rebuilt from pixels, EXIF/GPS gone) or the cover is a
created graphic. Never stock or scraped. Posts older than the rule are warned about, not refused.
"""
from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from concepts import _split, _when  # noqa: E402

RULE_FROM = datetime(2026, 11, 12)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def problems(root: str, now: datetime, drafts: bool):
    """-> (refuse [(file, why)], warn [(file, why)])"""
    blog = os.path.join(root, "content", "blog")
    refuse, warn = [], []
    for name in sorted(os.listdir(blog)):
        if not name.endswith(".md") or name.startswith("_"):
            continue
        fm, _ = _split(open(os.path.join(blog, name)).read())
        when, draft = _when(fm.get("date")), bool(fm.get("draft", False))
        publishes = not draft and (when is None or when <= now)
        if not publishes and not drafts:
            continue
        cover = str(fm.get("cover_image") or "").strip()
        if not cover:
            why = "no cover_image (square, CD-album-style; see docs/hacker-inc-format.md)"
        else:
            rel = cover.lstrip("/")
            if any(os.path.isfile(os.path.join(root, d, rel)) for d in ("assets", "static")):
                continue
            why = f"cover_image {cover} is not under assets/ or static/"
        old = when is None or when < RULE_FROM          # undated = written before the rule
        (warn if (old or not publishes) else refuse).append((name, why))
    return refuse, warn


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("check", "plan"))
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--now", help="YYYY-MM-DD (tests)")
    a = ap.parse_args(argv)
    now = datetime.fromisoformat(a.now) if a.now else datetime.now(timezone.utc).replace(tzinfo=None)
    refuse, warn = problems(a.root, now, drafts=a.mode == "plan")
    for f, why in warn:
        print(f"covers: {'todo' if a.mode == 'plan' else 'warn'}: {f}: {why}", file=sys.stderr)
    for f, why in refuse:
        print(f"covers: refusing: {f}: {why}", file=sys.stderr)
    if refuse and a.mode == "check":
        return 1
    print(f"covers: {len(refuse) + len(warn)} post(s) need a cover" if refuse or warn else
          "covers: every post has a cover", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
