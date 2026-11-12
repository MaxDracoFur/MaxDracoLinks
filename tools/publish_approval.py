#!/usr/bin/env python3
"""Publish gate: a post goes on maxdraco.com only with Max's own approval of that exact text and cover.

Why (Max 2026-11-12): three hacker posts went live at 08:26 on an agent's reading of "3 today",
each with `review_status: "approved"` the agent wrote itself and a made-up title-card cover. Max
pulled them the same morning: "that shouldn't have happened ... yes, fix the gate".

    python3 tools/publish_approval.py approve <slug>   # Max, in his own terminal
    python3 tools/publish_approval.py check            # deploy/preview: exit 1 on an unapproved post
    python3 tools/publish_approval.py plan             # drafts too: what each still needs; never fails

- `approve` shows the post, its cover and where to read it in the sandbox, and records it only when
  y or yes is typed on the controlling terminal (/dev/tty); anything else is no. An agent's shell has no terminal,
  so piping "y" into it does nothing. Agents never run `approve`, by any route.
- approvals.json pins sha256 of the post (front matter minus date/draft/review_status, plus body)
  and of the cover file. Editing either afterwards voids the approval; scheduling doesn't.
- `review_status` in front matter is ignored: anyone can type it.
- Posts dated on/after PHOTO_FROM need `cover_source: "stage:<outbox path>"`: one of Max's photos,
  exported by the stage app (approved for a maxdraco destination, rebuilt from pixels, no EXIF/GPS).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from concepts import _split, _when  # noqa: E402

RULE_FROM = datetime(2026, 11, 12)    # approval needed from here
PHOTO_FROM = datetime(2026, 11, 13)   # stage-photo cover needed from here
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SANDBOX = "http://site-preview.home.arpa"
UNHASHED = ("date", "draft", "review_status")


def _posts(root: str):
    blog = os.path.join(root, "content", "blog")
    for name in sorted(os.listdir(blog)):
        if name.endswith(".md") and not name.startswith("_"):
            path = os.path.join(blog, name)
            fm, body = _split(open(path).read())
            yield name, str(fm.get("slug") or name[:-3]), fm, body


def _cover_path(root: str, fm: dict):
    rel = str(fm.get("cover_image") or "").strip().lstrip("/")
    for d in ("assets", "static"):
        p = os.path.join(root, d, rel)
        if rel and os.path.isfile(p):
            return p
    return None


def hashes(root: str, fm: dict, body: str) -> dict:
    keep = {k: fm[k] for k in sorted(fm) if k not in UNHASHED}
    text = json.dumps(keep, sort_keys=True, default=str) + "\n---\n" + body
    cover = _cover_path(root, fm)
    return {"post": hashlib.sha256(text.encode()).hexdigest(),
            "cover": hashlib.sha256(open(cover, "rb").read()).hexdigest() if cover else None}


def _load(root: str) -> dict:
    p = os.path.join(root, "approvals.json")
    return json.load(open(p)) if os.path.exists(p) else {}


def record(root: str, slug: str, via: str) -> dict:
    for _, s, fm, body in _posts(root):
        if s == slug:
            entry = {**hashes(root, fm, body), "cover_image": fm.get("cover_image"),
                     "cover_source": fm.get("cover_source"), "via": via,
                     "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
            data = _load(root)
            data[slug] = entry
            with open(os.path.join(root, "approvals.json"), "w") as f:
                json.dump(data, f, indent=2, sort_keys=True)
                f.write("\n")
            return entry
    raise SystemExit(f"approve: no post with slug {slug!r}")


def problems(root: str, now: datetime, drafts: bool):
    data, out = _load(root), []
    for name, slug, fm, body in _posts(root):
        when, draft = _when(fm.get("date")), bool(fm.get("draft", False))
        publishes = not draft and when is not None and when <= now
        if not (publishes or drafts) or (when is not None and when < RULE_FROM):
            continue
        why = []
        src = str(fm.get("cover_source") or "").strip()
        if (when is None or when >= PHOTO_FROM) and not src.startswith("stage:"):
            why.append("cover_source must be stage:<outbox path> (one of Max's photos via the stage app)")
        got, h = data.get(slug), hashes(root, fm, body)
        if not got:
            why.append(f"not approved: Max runs `tools/publish_approval.py approve {slug}`")
        elif (got.get("post"), got.get("cover")) != (h["post"], h["cover"]):
            why.append("changed since Max approved it (text or cover): needs approving again")
        if why:
            out.append((name, publishes, why))
    return out


def approve(root: str, slug: str) -> int:
    # Two handles, not one "r+": a terminal isn't seekable, and Python's "r+" text mode raises
    # io.UnsupportedOperation (an OSError) on every real terminal, which read as "no terminal".
    # With no controlling terminal (an agent's shell) the open itself fails with ENXIO.
    try:
        tty_in = open("/dev/tty", "r")
        tty = open("/dev/tty", "w")
    except OSError:
        print("approve: needs Max at a real terminal (no controlling terminal here). "
              "Agents never approve posts.", file=sys.stderr)
        return 2
    for name, s, fm, body in _posts(root):
        if s != slug:
            continue
        cover = _cover_path(root, fm)
        tty.write(f"\n{fm.get('title')}\n  file:   content/blog/{name}\n"
                  f"  words:  {len(body.split())}\n  cover:  {fm.get('cover_image')} "
                  f"({'present' if cover else 'MISSING'})\n  source: {fm.get('cover_source') or '(none)'}\n"
                  f"  read it: {SANDBOX}/blog/{slug}/  (./preview.sh --drafts first)\n\n"
                  f"Approve this exact text and cover for maxdraco.com? [y/N] ")
        tty.flush()
        if tty_in.readline().strip().lower() not in ("y", "yes"):  # Max 2026-11-12
            tty.write("Not approved.\n")
            return 1
        e = record(root, slug, via="terminal")
        tty.write(f"Approved {slug} (post {e['post'][:12]}, cover {str(e['cover'])[:12]}). "
                  f"Commit approvals.json with the post.\n")
        return 0
    print(f"approve: no post with slug {slug!r}", file=sys.stderr)
    return 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("approve", "check", "plan"))
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--now", help="YYYY-MM-DD (tests)")
    a = ap.parse_args(argv)
    if a.mode == "approve":
        if not a.slug:
            ap.error("approve needs a slug")
        return approve(a.root, a.slug)
    now = datetime.fromisoformat(a.now) if a.now else datetime.now(timezone.utc).replace(tzinfo=None)
    found = problems(a.root, now, drafts=a.mode == "plan")
    refuse = [f for f in found if f[1]]
    for name, publishes, why in found:
        word = "refusing" if publishes and a.mode == "check" else "todo"
        for w in why:
            print(f"approval: {word}: {name}: {w}", file=sys.stderr)
    if refuse and a.mode == "check":
        return 1
    print("approval: every published post is approved as it stands" if not found else
          f"approval: {len(found)} post(s) need Max's approval", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
