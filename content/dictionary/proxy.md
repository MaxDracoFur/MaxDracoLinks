---
title: "Proxy (and reverse proxy)"
term_kind: concept
topics: [networking]
see_also: [tunnel, vpn, nginx]
summary: "A go-between that makes network requests on someone else's behalf and passes the answers back."
match: ['\bproxy\b', '\breverse proxies\b']
sources:
  - title: "RFC 9110: HTTP Semantics (section 3.7, Intermediaries)"
    url: "https://www.rfc-editor.org/info/rfc9110/"
    publisher: "IETF"
    primary: true
  - title: "Proxy server"
    url: "https://en.wikipedia.org/wiki/Proxy_server"
    publisher: "Wikipedia"
  - title: "Reverse proxy"
    url: "https://en.wikipedia.org/wiki/Reverse_proxy"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1090", topic: "Proxy",
     url: "https://attack.mitre.org/techniques/T1090/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A proxy is a go-between: instead of connecting straight to a server, a program connects to the proxy, which makes the request for it and passes the answer back. A forward proxy acts for the people browsing, and schools, offices and public networks often use one to control what can be reached. A reverse proxy sits in front of websites instead, taking visitors' requests and handing each one to the right application behind it, so only the proxy faces the internet. Attackers chain proxies too, to hide where their traffic really comes from.
