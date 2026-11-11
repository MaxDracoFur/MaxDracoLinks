---
title: "UDP"
term_kind: technology
summary: "User Datagram Protocol: a simple, connectionless way to send small messages over a network, with no delivery guarantee and no encryption."
match: ['\bUDP\b']
sources:
  - title: "RFC 768: User Datagram Protocol"
    url: "https://www.rfc-editor.org/rfc/rfc768"
    publisher: "IETF"
    primary: true
  - title: "User Datagram Protocol"
    url: "https://en.wikipedia.org/wiki/User_Datagram_Protocol"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first; health is checked daily.
draft: true
---
UDP is one of the two basic ways programs send data over the internet (the other is TCP). A sender just fires off a datagram: there is no connection set-up, no confirmation it arrived, and nothing on its own that encrypts it. That makes it fast and simple, which is why DNS, games, video calls and classic syslog use it.

## Why it's on this site

A lot of my network's plumbing, DNS among it, runs over UDP.
