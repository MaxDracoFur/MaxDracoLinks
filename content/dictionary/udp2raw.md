---
title: "udp2raw"
term_kind: tool
topics: [networking]
see_also: [wstunnel, udp, tcp]
summary: "Open-source tool that disguises UDP traffic as TCP so it can pass networks that block UDP."
match: ['\budp2raw\b']
sources:
  - title: "udp2raw"
    url: "https://github.com/wangyu-/udp2raw"
    publisher: "udp2raw project"
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
udp2raw is a small {{< term "open-source" >}} {{< term "tunnel" >}} that takes {{< term "udp" >}} traffic, such as a {{< term "wireguard" >}} connection, and repackages each {{< term "packet" >}} so it looks like {{< term "tcp" >}} on the wire. It is used on networks that block or throttle UDP. The disguise is only skin-deep: equipment that inspects traffic closely can still tell it is not a real TCP conversation.
