---
title: "IP address (IPv4/IPv6)"
term_kind: concept
topics: [networking]
see_also: [mac-address, subnet, dhcp]
summary: "The number that identifies a device on a network so that traffic can be delivered to it."
match: ['\bIP address(?:es)?\b', '\bIPv[46]\b', '\b(?:private|public|static|fixed|home) address(?:es)?\b']
sources:
  - title: "RFC 791: Internet Protocol"
    url: "https://www.rfc-editor.org/info/rfc791/"
    publisher: "IETF"
    primary: true
  - title: "RFC 8200: Internet Protocol, Version 6 (IPv6) Specification"
    url: "https://www.rfc-editor.org/info/rfc8200/"
    publisher: "IETF"
  - title: "IP address"
    url: "https://en.wikipedia.org/wiki/IP_address"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1590.005", topic: "Gather Victim Network Information: IP Addresses",
     url: "https://attack.mitre.org/techniques/T1590/005/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
An IP address is the number that identifies a device on a network, the way a street address identifies a house: everything sent across the internet carries the address it came from and the one it is going to. The older IPv4 form looks like 198.51.100.7; the newer IPv6 form is much longer and written in hexadecimal. Some ranges are private, used only inside home and office networks, and addresses are either handed out automatically by {{< term "dhcp" >}} or fixed by hand. Every site you contact sees your public address, which reveals roughly where you are and which internet provider you use.
