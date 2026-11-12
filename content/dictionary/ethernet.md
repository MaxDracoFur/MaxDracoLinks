---
title: "Ethernet (and USB Ethernet dongle)"
term_kind: protocol
topics: [networking, hardware]
see_also: [lan, packet, phy]
summary: "The standard for wired computer networks: the cables, plugs and signals that connect devices."
match: ['\bEthernet\b']
sources:
  - title: "IEEE 802.3: Standard for Ethernet"
    url: "https://standards.ieee.org/ieee/802.3/10422/"
    publisher: "IEEE"
    primary: true
  - title: "IEEE 802.3 Ethernet Working Group"
    url: "https://www.ieee802.org/3/"
    publisher: "IEEE 802"
  - title: "Ethernet"
    url: "https://en.wikipedia.org/wiki/Ethernet"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Ethernet is the standard for wired networks: the cables, plugs and signals that connect computers, {{< term "network-switch" "switches" >}} and {{< term "router" "routers" >}}, defined by the IEEE 802.3 standard. Data travels in chunks called {{< term "packet" "frames" >}}, each addressed to a device's {{< term "mac-address" "MAC address" >}}. A {{< term "usb" >}} Ethernet dongle adds a wired connection to a computer that has none, through a small network adapter inside the plug.
