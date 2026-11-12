---
title: "VLAN hopping"
term_kind: concept
topics: [networking, security-operations]
see_also: [vlan, network-switch, router-on-a-stick]
summary: "Attacks that let a device on one VLAN send traffic into another VLAN without passing the router."
match: ['\bVLAN[- ]hopping\b', '\bswitch spoofing\b', '\bdouble[- ]tagg(?:ing|ed)\b', '\bDTP\b', '\btrunk ports?\b']
sources:
  - title: "IEEE 802.1Q: Bridges and Bridged Networks"
    url: "https://standards.ieee.org/ieee/802.1Q/6844/"
    publisher: "IEEE"
    primary: true
  - title: "VLAN hopping"
    url: "https://en.wikipedia.org/wiki/VLAN_hopping"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1599", topic: "Network Boundary Bridging",
     url: "https://attack.mitre.org/techniques/T1599/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
{{< term "vlan" "VLANs" >}} keep networks apart on shared {{< term "network-switch" "switches" >}}; traffic between them is supposed to go through a {{< term "router" >}}. VLAN hopping gets around that. In switch {{< term "spoofing" >}}, a device pretends to be another switch (on {{< term "cisco" >}} gear, using a feature called DTP) to be handed a trunk port, a link that carries every VLAN. In double-tagging, a device on the trunk's untagged "native" VLAN sends frames with two VLAN tags, and the first switch strips the outer one and forwards the frame into the target VLAN. Disabling trunk negotiation and leaving the native VLAN empty stop both.
