---
title: "WPA2 and WPA3"
term_kind: standard
topics: [networking, cryptography]
see_also: [wi-fi, password-cracking, handshake]
summary: "The security standards that encrypt Wi-Fi and control who can join it."
match: ['\bWPA[23]?\b']
sources:
  - title: "Wi-Fi Protected Access security"
    url: "https://www.wi-fi.org/security"
    publisher: "Wi-Fi Alliance"
    primary: true
  - title: "Wi-Fi Protected Access"
    url: "https://en.wikipedia.org/wiki/Wi-Fi_Protected_Access"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
WPA2 and WPA3 are the security standards for {{< term "wi-fi" >}}, set by the industry group the Wi-Fi Alliance: they decide how a device proves it knows the network password and how its traffic is then {{< term "encryption" "encrypted" >}}. With WPA2's password mode, someone who records a device joining can take that recording away and guess passwords against it at leisure ({{< term "password-cracking" "offline cracking" >}}). WPA3 changes the joining {{< term "handshake" >}} so that a recording no longer allows this.
