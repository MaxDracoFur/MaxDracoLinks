---
title: "Page source (view-source)"
term_kind: concept
topics: [web-and-advertising]
see_also: [source-code, wayback-machine, google-adsense]
summary: "The raw HTML code a web page is built from, which any browser can show."
match: ['\bpage source\b', '\bview-source\b']
sources:
  - title: "View Source"
    url: "https://firefox-source-docs.mozilla.org/devtools-user/view_source/index.html"
    publisher: "Mozilla (Firefox DevTools)"
    primary: true
  - title: "view-source URI scheme"
    url: "https://en.wikipedia.org/wiki/View-source_URI_scheme"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1594", topic: "Search Victim-Owned Websites",
     url: "https://attack.mitre.org/techniques/T1594/"}
  - {standard: cwe, clause: "CWE-615", topic: "Inclusion of Sensitive Information in Source Code Comments",
     url: "https://cwe.mitre.org/data/definitions/615.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A web page's source is the HTML code the browser receives and turns into what you see. Any browser can show it: typing view-source: in front of an address, or choosing View Page Source, shows the raw code. It often contains things visitors never see on screen, such as ad and analytics account IDs, the names of the tools the site is built with, and notes developers left in comments, which makes it a standard first stop when researching a website.
