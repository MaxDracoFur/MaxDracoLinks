---
title: "PHY (network chip)"
term_kind: thing
topics: [hardware, networking]
see_also: [ethernet, driver]
summary: "The chip, or part of a chip, that turns a network connection's data into signals on the cable and back."
match: ['\bPHY\b', '\bnetwork chip\b']
sources:
  - title: "IEEE 802.3: Standard for Ethernet"
    url: "https://standards.ieee.org/ieee/802.3/10422/"
    publisher: "IEEE"
    primary: true
  - title: "PHY"
    url: "https://en.wikipedia.org/wiki/PHY"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
PHY is short for physical layer. In a network card or {{< term "usb" >}} {{< term "ethernet" >}} adapter, the PHY is the part that actually drives the cable: it sends and receives the electrical signals and works out whether a link is up and at what speed. The computer's {{< term "driver" >}} reads the PHY's status to know whether a cable is connected.
