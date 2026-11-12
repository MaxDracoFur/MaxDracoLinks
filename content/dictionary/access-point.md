---
title: "Access point (Wi-Fi)"
term_kind: thing
topics: [networking, hardware]
see_also: [wi-fi, network-switch, vlan]
summary: "The device that broadcasts a Wi-Fi network and connects wireless devices to the wired network."
match: ['\b(?:wireless )?access points?\b']
sources:
  - title: "IEEE 802.11-2020: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications"
    url: "https://standards.ieee.org/ieee/802.11/7028/"
    publisher: "IEEE"
    primary: true
  - title: "Wireless access point"
    url: "https://en.wikipedia.org/wiki/Wireless_access_point"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "AC-18", topic: "Wireless Access",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AC-18"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
An access point is the box that creates a {{< term "wi-fi" >}} network. Phones and laptops connect to it by radio, and it passes their traffic onto the wired network, usually through a cable to a {{< term "network-switch" "switch" >}} or {{< term "router" >}}; home Wi-Fi routers have one built in. Many can broadcast several networks at once, such as a guest network, but keeping guests apart from everything else only works if the access point and the network behind it actually separate that traffic, typically with a {{< term "vlan" >}}.
