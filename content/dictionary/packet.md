---
title: "Packet (and packet capture)"
term_kind: concept
topics: [networking]
see_also: [ethernet, deep-packet-inspection, mac-address]
summary: "A small chunk of data sent across a network, with a header saying where it came from and where it is going."
match: ['\bpackets\b', '\ba (?:spoofed |single )?packet\b', '\bpacket (?:size|sizes|capture|captures|loss)\b', '\bon the wire\b', '\b(?:double-tagged|untagged|tagged|Ethernet|network) frames?\b', '\bMTU\b']
sources:
  - title: "NIST CSRC Glossary: packet"
    url: "https://csrc.nist.gov/glossary/term/packet"
    publisher: "NIST"
    primary: true
  - title: "Network packet"
    url: "https://en.wikipedia.org/wiki/Network_packet"
    publisher: "Wikipedia"
  - title: "Maximum transmission unit"
    url: "https://en.wikipedia.org/wiki/Maximum_transmission_unit"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1040", topic: "Network Sniffing",
     url: "https://attack.mitre.org/techniques/T1040/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Networks don't send data as one continuous stream: they cut it into packets, each with a header saying where it came from and where it is going. On an {{< term "ethernet" >}} network the same unit is called a frame. Every link has a largest packet it will carry, its MTU (maximum transmission unit), and anything bigger has to be split up or is dropped. A packet capture records packets exactly as they crossed the network ("on the wire"), so anything that wasn't {{< term "encryption" "encrypted" >}} can be read straight out of it.
