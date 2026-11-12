---
title: "Session recording and heatmaps"
term_kind: concept
topics: [web-and-advertising]
see_also: [google-analytics]
summary: "Scripts that record how each visitor moves, clicks and types on a website so the owner can replay or map it."
match: ['\bsession[ -](?:replay|recording)s?\b', '\bheatmaps?\b']
sources:
  - title: "No boundaries: Exfiltration of personal data by session-replay scripts"
    url: "https://blog.citp.princeton.edu/2017/11/15/no-boundaries-exfiltration-of-personal-data-by-session-replay-scripts/"
    publisher: "Princeton CITP"
    primary: true
  - title: "Session replay"
    url: "https://en.wikipedia.org/wiki/Session_replay"
    publisher: "Wikipedia"
classification:
  - {standard: cwe, clause: "CWE-359", topic: "Exposure of Private Personal Information to an Unauthorized Actor",
     url: "https://cwe.mitre.org/data/definitions/359.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Session recording (also called session replay) services add a script to a website that records each visitor's mouse movements, scrolling, clicks and typing, so the owner can watch a replay of the visit. Heatmaps add those recordings up into a coloured map of where people click and how far they scroll. Researchers have found these scripts can capture personal details visitors type into forms, sometimes before they press submit.
