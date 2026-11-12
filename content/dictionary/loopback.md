---
title: "Loopback (localhost)"
term_kind: concept
topics: [networking]
see_also: [ip-address, network-port]
summary: "A computer's network connection to itself, reached at the name localhost or the address 127.0.0.1."
match: ['\bloopback\b', '\blocalhost\b', '\b127\.0\.0\.1\b']
sources:
  - title: "RFC 1122: Requirements for Internet Hosts -- Communication Layers"
    url: "https://www.rfc-editor.org/info/rfc1122/"
    publisher: "IETF"
    primary: true
  - title: "RFC 6761: Special-Use Domain Names"
    url: "https://www.rfc-editor.org/info/rfc6761/"
    publisher: "IETF"
  - title: "localhost"
    url: "https://en.wikipedia.org/wiki/Localhost"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Loopback is a network interface that never leaves the machine: anything a program sends to it comes straight back to the same computer. It has the name localhost and the {{< term "ip-address" "IP address" >}} 127.0.0.1 (::1 in IPv6). Developers use it to run and test network programs safely on one machine, and services that should never be reachable from outside are often set to listen only there.
