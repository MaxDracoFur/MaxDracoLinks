---
title: "WebSocket"
term_kind: protocol
topics: [networking]
see_also: [http, tls, wstunnel]
summary: "A web standard for a long-lived, two-way connection between a browser and a server."
match: ['\bWeb ?Sockets?\b']
sources:
  - title: "RFC 6455: The WebSocket Protocol"
    url: "https://www.rfc-editor.org/rfc/rfc6455.html"
    publisher: "IETF"
    primary: true
  - title: "WebSockets Standard"
    url: "https://websockets.spec.whatwg.org/"
    publisher: "WHATWG"
classification:
  - {standard: cwe, clause: "CWE-1385", topic: "Missing Origin Validation in WebSockets",
     url: "https://cwe.mitre.org/data/definitions/1385.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A WebSocket is a connection that starts as an ordinary {{< term "http" >}} request and then stays open, so the browser and server can both send messages at any time. Live chat, notifications and dashboards that update on their own use it. Run over {{< term "tls" >}} it looks like any other secure web traffic, which is also why tools use it to carry other kinds of traffic through strict networks.
