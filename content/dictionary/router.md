---
title: "Router"
term_kind: thing
topics: [networking, hardware]
see_also: [firewall, subnet, nat]
summary: "A device that passes traffic between separate networks, such as a home network and the internet."
match: ['\brouters?\b']
sources:
  - title: "router (glossary)"
    url: "https://csrc.nist.gov/glossary/term/router"
    publisher: "NIST CSRC"
    primary: true
  - title: "RFC 1812: Requirements for IP Version 4 Routers"
    url: "https://www.rfc-editor.org/info/rfc1812/"
    publisher: "IETF"
  - title: "Router (computing)"
    url: "https://en.wikipedia.org/wiki/Router_(computing)"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A router connects separate networks and passes traffic between them, choosing where each {{< term "packet" >}} goes next. A home router sits between the home network and the internet, and usually also hands out addresses, keeps a list of connected devices and runs the {{< term "firewall" >}}. It can only apply rules to traffic that actually passes through it: devices on the same {{< term "subnet" "network segment" >}} talk to each other directly, without it.
