---
title: "wstunnel"
term_kind: tool
topics: [networking]
see_also: [websocket, udp2raw, tunnel]
summary: "Open-source tool that carries other network traffic inside a WebSocket connection."
match: ['\bwstunnel\b']
sources:
  - title: "wstunnel"
    url: "https://github.com/erebe/wstunnel"
    publisher: "wstunnel project"
    primary: true
  - title: "RFC 6455: The WebSocket Protocol"
    url: "https://www.rfc-editor.org/rfc/rfc6455.html"
    publisher: "IETF"
classification:
  - {standard: attack, clause: "T1572", topic: "Protocol Tunneling",
     url: "https://attack.mitre.org/techniques/T1572/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
wstunnel is an {{< term "open-source" >}} {{< term "tunnel" >}} that wraps other traffic, including {{< term "udp" >}} such as a {{< term "wireguard" >}} connection, inside a {{< term "websocket" >}}. Run over {{< term "tls" >}} on {{< term "network-port" "port" >}} 443, it looks like an ordinary secure web page connection. That lets it get through networks that only allow web browsing.
