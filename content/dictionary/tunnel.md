---
title: "Tunnel (networking)"
term_kind: concept
topics: [networking]
see_also: [vpn, wireguard, cloudflare-tunnel]
summary: "A connection that carries one kind of network traffic wrapped inside another."
match: ['\b(?:a|the|its|vendor|outbound|own|encrypted) tunnels?\b']
sources:
  - title: "tunneling (NIST CSRC glossary)"
    url: "https://csrc.nist.gov/glossary/term/tunneling"
    publisher: "NIST"
    primary: true
  - title: "Tunneling protocol"
    url: "https://en.wikipedia.org/wiki/Tunneling_protocol"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1572", topic: "Protocol Tunneling",
     url: "https://attack.mitre.org/techniques/T1572/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A tunnel wraps network traffic inside another connection, so it can cross a network that would otherwise not carry it. A {{< term "vpn" >}} is the most common example: traffic between two places travels inside one {{< term "encryption" "encrypted" >}} connection. Because a tunnel can dial out from inside a network and look like ordinary web traffic, it can also become a way in that the network's owner never approved.
