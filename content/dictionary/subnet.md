---
title: "Subnet (network segment)"
term_kind: concept
topics: [networking]
see_also: [ip-address, vlan, router]
summary: "A block of addresses, and the group of devices using them, that forms one section of a network."
match: ['\bsubnets?\b', '\bnetwork segments?\b', '\bnetwork segmentation\b', '\baddress ranges?\b']
sources:
  - title: "RFC 950: Internet Standard Subnetting Procedure"
    url: "https://www.rfc-editor.org/info/rfc950/"
    publisher: "IETF"
    primary: true
  - title: "Subnet"
    url: "https://en.wikipedia.org/wiki/Subnet"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "M1030", topic: "Network Segmentation",
     url: "https://attack.mitre.org/mitigations/M1030/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A subnet is one section of a network, defined by a block of {{< term "ip-address" "IP addresses" >}}, such as every address from 192.168.1.0 to 192.168.1.255. Devices in the same subnet, or network segment, talk to each other directly. Traffic to a different subnet has to go through a {{< term "router" >}}, which is where rules can be applied, so splitting a network into segments is a basic way to keep untrusted devices away from important ones.
