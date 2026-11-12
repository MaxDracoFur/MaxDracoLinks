---
title: "Port (network)"
term_kind: concept
topics: [networking]
see_also: [tcp, udp, port-scanning]
summary: "A number from 0 to 65535 that tells a computer which program an incoming network message is for."
match: ['\bport (?:number|\d+)s?\b', '\bports \d+\b', '\bopen ports?\b', '\bport-based\b', '\b(?:inbound|listening|web) ports?\b', '\bport (?:blocks?|blocking|filtering|check)\b']
sources:
  - title: "Service Name and Transport Protocol Port Number Registry"
    url: "https://www.iana.org/assignments/service-names-port-numbers"
    publisher: "IANA"
    primary: true
  - title: "RFC 6335: IANA Procedures for the Management of the Service Name and Transport Protocol Port Number Registry"
    url: "https://www.rfc-editor.org/info/rfc6335/"
    publisher: "IETF"
  - title: "Port (computer networking)"
    url: "https://en.wikipedia.org/wiki/Port_(computer_networking)"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A port is a number that, together with an address, picks out one program on a computer: the address finds the machine, the port finds the service on it. Web servers usually listen on port 443, {{< term "ssh" >}} on 22, and each {{< term "tcp" >}} or {{< term "udp" >}} connection names the port it is aimed at. A port where a program is listening is called open, and every open port is a door that outsiders may try, which is why {{< term "firewall" "firewalls" >}} decide which ports are reachable from where.
