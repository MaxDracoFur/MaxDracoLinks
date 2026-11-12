---
title: "nginx"
term_kind: tool
topics: [networking, platforms-and-services]
see_also: [proxy, http]
summary: "Widely used open-source web server and reverse proxy."
match: ['\bnginx\b']
sources:
  - title: "nginx"
    url: "https://nginx.org/en/"
    publisher: "nginx"
    primary: true
  - title: "Nginx"
    url: "https://en.wikipedia.org/wiki/Nginx"
    publisher: "Wikipedia"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:f5:nginx", topic: "the name NVD files current nginx vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Af5%3Anginx"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
nginx (said "engine-x") is free, {{< term "open-source" >}} software that serves websites and passes web requests on to other programs. It is one of the most common web servers on the internet and is often used as a {{< term "proxy" "reverse proxy" >}} in front of applications. Because it usually faces the internet directly, keeping it updated matters more than for most software.
