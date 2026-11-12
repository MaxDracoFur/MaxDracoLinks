---
title: "Network switch (managed switch)"
term_kind: thing
topics: [networking, hardware]
see_also: [vlan, router, ethernet]
summary: "A box with many network sockets that passes traffic between the wired devices plugged into it."
match: ['\b(?:managed|network|edge) switch(?:es)?\b', '\bswitch ports?\b', '\b(?:the|my|one|a|second|spare|single|this) switch\b']
sources:
  - title: "IEEE 802.1Q: Bridges and Bridged Networks"
    url: "https://standards.ieee.org/ieee/802.1Q/6844/"
    publisher: "IEEE"
    primary: true
  - title: "Network switch"
    url: "https://en.wikipedia.org/wiki/Network_switch"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A network switch connects wired devices on a {{< term "lan" >}}: each one plugs into its own numbered port on the switch (a switch port), and the switch learns which device is on which port and sends each message only where it needs to go. A plain switch just does that; a managed switch can also be configured, for example to split its ports into separate {{< term "vlan" "VLANs" >}}. Traffic between different networks still has to pass through a {{< term "router" >}} or {{< term "firewall" >}}.
