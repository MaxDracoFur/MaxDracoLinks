---
title: "DHCP"
term_kind: protocol
topics: [networking]
see_also: [kea, ip-address, mac-address]
summary: "The protocol that gives a device joining a network its address and settings automatically."
match: ['\bDHCP(?:v[46])?\b']
sources:
  - title: "RFC 2131: Dynamic Host Configuration Protocol"
    url: "https://www.rfc-editor.org/info/rfc2131/"
    publisher: "IETF"
    primary: true
  - title: "RFC 8415: Dynamic Host Configuration Protocol for IPv6 (DHCPv6)"
    url: "https://www.rfc-editor.org/info/rfc8415/"
    publisher: "IETF"
  - title: "Dynamic Host Configuration Protocol"
    url: "https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1557.003", topic: "Adversary-in-the-Middle: DHCP Spoofing",
     url: "https://attack.mitre.org/techniques/T1557/003/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
DHCP (Dynamic Host Configuration Protocol) is how a device joining a network gets its settings without anyone typing them in: an {{< term "ip-address" "IP address" >}}, the {{< term "router" >}} to send traffic through, and the {{< term "dns" >}} servers to ask. A DHCP server hands out addresses from a pool; a reservation ties one address to a device's {{< term "mac-address" "MAC address" >}} so it always gets the same one. DHCPv6 does the same job for IPv6. The protocol has no {{< term "authentication" >}}, so any device on the network can pretend to be the DHCP server.
