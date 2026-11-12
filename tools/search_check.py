#!/usr/bin/env python3
"""Site search must never leak a page the public site doesn't ship (card maxdraco-dictionary).

    python3 tools/search_check.py <built dir> [--root <site root>]

Reads <built dir>/search-index.json and `hugo list all` for the site root, then fails (exit 1)
when the index lists a draft, future-dated or expired page, or a URL with no built file.
Run it against a --drafts build: that is the build where drafts exist to leak.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from urllib.parse import urlsplit


def _when(s: str):
    if not s or s.startswith("0001-01-01"):
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def hidden_paths(listing_csv: str, now: datetime) -> dict:
    """{url path: why} for every page a publish build would not ship."""
    out = {}
    for row in csv.DictReader(io.StringIO(listing_csv)):
        why = None
        if row.get("draft", "").lower() == "true":
            why = "draft"
        elif (d := _when(row.get("publishDate") or row.get("date"))) and d > now:
            why = "future-dated"
        elif (e := _when(row.get("expiryDate"))) and e <= now:
            why = "expired"
        if why and row.get("permalink"):
            out[urlsplit(row["permalink"]).path] = f"{why} ({row['path']})"
    return out


def problems(index: dict, hidden: dict, exists) -> list[str]:
    out = []
    for p in index.get("pages", []):
        u = p.get("u", "")
        if u in hidden:
            out.append(f"{u}: {hidden[u]} page is in the search index")
        elif not exists(u):
            out.append(f"{u}: in the search index but not built")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("built")
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    a = ap.parse_args(argv)
    with open(os.path.join(a.built, "search-index.json")) as fh:
        index = json.load(fh)
    listing = subprocess.run(["hugo", "list", "all"], cwd=a.root, check=True,
                             capture_output=True, text=True).stdout
    hidden = hidden_paths(listing, datetime.now(timezone.utc))

    def exists(u):
        rel = u.lstrip("/")
        return os.path.isfile(os.path.join(a.built, rel)) or \
            os.path.isfile(os.path.join(a.built, rel, "index.html"))
    out = problems(index, hidden, exists)
    for line in out:
        print(f"search-check: refusing: {line}", file=sys.stderr)
    print(f"search-check: {len(index.get('pages', []))} pages indexed, {len(hidden)} draft/future/expired "
          f"pages in the tree, {len(out)} problem(s)", file=sys.stderr)
    return 1 if out else 0


if __name__ == "__main__":
    sys.exit(main())
