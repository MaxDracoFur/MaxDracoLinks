---
title: "Domain name"
term_kind: concept
topics: [web-and-advertising, networking]
see_also: [dns, expired-domain]
summary: "A human-readable name for a place on the internet, such as example.com, rented through a registrar."
match: ['\bdomain names?\b', '\bdomains?\b']
sources:
  - title: "RFC 1034: Domain Names - Concepts and Facilities"
    url: "https://www.rfc-editor.org/rfc/rfc1034.html"
    publisher: "IETF"
    primary: true
  - title: "Beginner's guides"
    url: "https://www.icann.org/en/beginners"
    publisher: "ICANN"
  - title: "Domain name"
    url: "https://en.wikipedia.org/wiki/Domain_name"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A domain name is the readable address of a website or service, such as example.com. Behind the scenes, {{< term "dns" >}} turns the name into the numeric address of the computer that answers for it. Nobody owns a domain outright: it is registered through a registrar for a yearly fee, and if the fee isn't paid the name expires and someone else can register it.
