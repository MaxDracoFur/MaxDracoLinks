---
title: "Router on a stick"
term_kind: concept
topics: [networking]
see_also: [vlan, router, vlan-hopping]
summary: "A setup where one cable between a switch and a router carries several VLANs, and the router passes traffic between them."
match: ['\brouter[- ]on[- ]a[- ]stick\b']
sources:
  - title: "IEEE 802.1Q: Bridges and Bridged Networks"
    url: "https://standards.ieee.org/ieee/802.1Q/6844/"
    publisher: "IEEE"
    primary: true
  - title: "Router on a stick"
    url: "https://en.wikipedia.org/wiki/Router_on_a_stick"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
This is a common way to wire a small network that is split into several {{< term "vlan" "VLANs" >}}. A single cable (the "stick") runs from a {{< term "network-switch" "switch" >}} to the {{< term "router" >}}, carrying every VLAN at once, with each frame tagged to say which one it belongs to. Traffic going from one VLAN to another travels up that cable to the router, which applies its rules and sends it back down; that one cable gives "router on a stick" its name. It saves ports and cables, but the shared cable's settings matter for security.
