---
title: "Deep packet inspection (DPI)"
term_kind: concept
topics: [networking, security-operations]
see_also: [firewall, packet, wireguard]
summary: "Looking inside network traffic, not just at its addresses, to work out what it is."
match: ['\bdeep packet inspection\b', '\bDPI\b']
sources:
  - title: "Deep Packet Inspection"
    url: "https://csrc.nist.gov/glossary/term/deep_packet_inspection"
    publisher: "NIST CSRC"
    primary: true
  - title: "Deep packet inspection"
    url: "https://en.wikipedia.org/wiki/Deep_packet_inspection"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "M1031", topic: "Network Intrusion Prevention",
     url: "https://attack.mitre.org/mitigations/M1031/"}
  - {standard: sp800-53, clause: "SI-4", topic: "System Monitoring",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SI-04"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Ordinary {{< term "firewall" "firewalls" >}} decide what to allow from the outside of each {{< term "packet" >}}: where it comes from, where it is going, and which {{< term "network-port" "port" >}}. Deep packet inspection also looks at what is inside, and at the shape and timing of the traffic, to recognise particular programs or protocols. Networks use it to block attacks or unwanted apps, and censors use it to spot and block {{< term "vpn" "VPNs" >}}, even when they are disguised on common ports.
