---
title: "WAN"
term_kind: concept
topics: [networking]
see_also: [lan, router, dmz]
summary: "Wide area network: the outside network, usually the internet connection, as opposed to the local network."
match: ['\bWANs?\b']
sources:
  - title: "wide area network (NIST CSRC glossary)"
    url: "https://csrc.nist.gov/glossary/term/wide_area_network"
    publisher: "NIST"
    primary: true
  - title: "Wide area network"
    url: "https://en.wikipedia.org/wiki/Wide_area_network"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A WAN (wide area network) is a network that spans a large area, and the internet is the biggest one. On a home or office {{< term "router" >}}, the WAN side is the connection to the internet provider, and the {{< term "lan" >}} side is the local network. Everything arriving on the WAN side comes from the outside world, so that is where the {{< term "firewall" >}}'s strictest rules apply.
