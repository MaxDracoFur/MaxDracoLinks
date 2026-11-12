---
title: "Spoofing"
term_kind: concept
topics: [networking, security-operations]
see_also: [ip-address, packet, ingress-filtering]
summary: "Faking the sender of a message or network packet so it looks like it came from somewhere it didn't."
match: ['\bspoof(?:s|ed|ing)?\b']
sources:
  - title: "spoofing (glossary)"
    url: "https://csrc.nist.gov/glossary/term/spoofing"
    publisher: "NIST CSRC"
    primary: true
  - title: "IP address spoofing"
    url: "https://en.wikipedia.org/wiki/IP_address_spoofing"
    publisher: "Wikipedia"
classification:
  - {standard: capec, clause: "CAPEC-151", topic: "Identity Spoofing",
     url: "https://capec.mitre.org/data/definitions/151.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Spoofing means faking who sent something: an email that claims to be from your bank, or a network {{< term "packet" >}} with a made-up return address. A spoofed packet can still be delivered, but any reply goes to the faked address, not to the sender, so the attack is usually blind and one-way. Networks defend against it by dropping traffic whose sender address can't be right for where it came from.
