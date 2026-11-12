---
title: "Wayback Machine (web archive)"
term_kind: tool
topics: [web-and-advertising]
see_also: [page-source, domain]
summary: "The Internet Archive's public library of saved copies of web pages, going back to 1996."
match: ['\bWayback Machine\b', '\bWayback\b', '\bweb\.archive\.org\b']
sources:
  - title: "Wayback Machine General Information"
    url: "https://help.archive.org/help/wayback-machine-general-information/"
    publisher: "Internet Archive"
    primary: true
  - title: "Using the Wayback Machine"
    url: "https://help.archive.org/help/using-the-wayback-machine/"
    publisher: "Internet Archive"
  - title: "Wayback Machine"
    url: "https://en.wikipedia.org/wiki/Wayback_Machine"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1593", topic: "Search Open Websites/Domains",
     url: "https://attack.mitre.org/techniques/T1593/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
The Wayback Machine, at web.archive.org, is run by the non-profit Internet Archive. It regularly saves copies of public web pages and lets anyone open a page as it looked on a past date. Each saved copy, called a snapshot, keeps the page's code as well as its text, so it can show how a site changed over the years and who it was paying or tracking with at the time.
