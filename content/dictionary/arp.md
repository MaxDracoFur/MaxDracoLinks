---
title: "ARP"
term_kind: protocol
topics: [networking]
see_also: [mac-address, ip-address, lan]
summary: "Address Resolution Protocol: how a device on a local network finds the hardware address that goes with an IP address."
match: ['\bARP\b', '\bAddress Resolution Protocol\b']
sources:
  - title: "RFC 826: An Ethernet Address Resolution Protocol"
    url: "https://www.rfc-editor.org/rfc/rfc826.html"
    publisher: "IETF"
    primary: true
  - title: "Address Resolution Protocol"
    url: "https://en.wikipedia.org/wiki/Address_Resolution_Protocol"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1557.002", topic: "Adversary-in-the-Middle: ARP Cache Poisoning",
     url: "https://attack.mitre.org/techniques/T1557/002/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
ARP (Address Resolution Protocol) is how a device on a {{< term "lan" "local network" >}} finds out which piece of hardware has a given {{< term "ip-address" >}}. It shouts a question to the whole network ("who has this address?") and the owner replies with its {{< term "mac-address" >}}; each device keeps the answers in a short-lived ARP table. Sending these questions to every address is also a quick way to list what is on a network. ARP has no {{< term "authentication" >}}, so a device on the same network can lie in its replies and pull other devices' traffic through itself.
