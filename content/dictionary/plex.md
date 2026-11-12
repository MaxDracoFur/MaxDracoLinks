---
title: "Plex Media Server"
term_kind: tool
topics: [platforms-and-services]
see_also: [self-hosting, cve]
summary: "Software that serves your own films, TV and music to your devices, like a personal streaming service."
match: ['\bPlex\b']
sources:
  - title: "What is Plex?"
    url: "https://support.plex.tv/articles/200288286-what-is-plex/"
    publisher: "Plex"
    primary: true
  - title: "Plex Inc."
    url: "https://en.wikipedia.org/wiki/Plex_Inc."
    publisher: "Wikipedia"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:plex:media_server", topic: "the name NVD files Plex Media Server vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Aplex%3Amedia_server"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Plex Media Server is software from the company Plex that you run on your own computer or {{< term "nas" >}}. It organises your films, TV and music and streams them to apps on phones, TVs and browsers, at home or over the internet. Because it is often reachable from outside the home, flaws in it have been used to break into the networks it runs on.
