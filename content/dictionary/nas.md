---
title: "NAS (network attached storage)"
term_kind: thing
topics: [hardware]
see_also: [self-hosting, homelab]
summary: "A storage box full of disks that shares its files with other computers over the network."
match: ['\bNAS\b', '\bnetwork[- ]attached storage\b']
sources:
  - title: "Network attached storage (glossary)"
    url: "https://csrc.nist.gov/glossary/term/network_attached_storage"
    publisher: "NIST"
    primary: true
  - title: "Network-attached storage (NAS)"
    url: "https://www.snia.org/education/online-dictionary/term/network-attached-storage"
    publisher: "SNIA"
  - title: "Network-attached storage"
    url: "https://en.wikipedia.org/wiki/Network-attached_storage"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A NAS is a small computer whose main job is holding disks and serving their files to other devices on the network. Homes and offices use them for shared folders, backups and media libraries, often with several disks arranged so that one can fail without losing data. Because a NAS holds so much data in one place, it is a favourite target for ransomware, and its web admin page should never be reachable from the internet.
