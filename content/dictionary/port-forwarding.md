---
title: "Port forwarding"
term_kind: concept
topics: [networking]
see_also: [nat, tunnel, proxy]
summary: "Passing connections that arrive on a port of one machine on to a port on another."
match: ['\bport[- ]forward(?:s|ed|ing)?\b']
sources:
  - title: "RFC 4254: The Secure Shell (SSH) Connection Protocol"
    url: "https://www.rfc-editor.org/info/rfc4254/"
    publisher: "IETF"
    primary: true
  - title: "Port forwarding"
    url: "https://en.wikipedia.org/wiki/Port_forwarding"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Port forwarding takes connections arriving at one {{< term "network-port" "port" >}} and hands them on to another address. On a home {{< term "router" >}} it is how a device inside the network is made reachable from the internet, which also makes it reachable to anyone scanning for it. {{< term "ssh" "SSH" >}} and similar tools can forward a port through an {{< term "encryption" "encrypted" >}} connection instead, so one program can reach something on a distant network.
