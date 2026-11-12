---
title: "Dynamic DNS"
term_kind: concept
topics: [networking]
see_also: [dns, domain, ip-address]
summary: "Keeping a hostname pointed at an address that changes, such as a home internet connection."
match: ['\bdynamic DNS\b', '\bDDNS\b']
sources:
  - title: "RFC 2136: Dynamic Updates in the Domain Name System (DNS UPDATE)"
    url: "https://www.rfc-editor.org/info/rfc2136/"
    publisher: "IETF"
    primary: true
  - title: "Dynamic DNS"
    url: "https://en.wikipedia.org/wiki/Dynamic_DNS"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Dynamic {{< term "dns" "DNS" >}} keeps a name pointing at an address that keeps changing. Most home internet connections are given a new public {{< term "ip-address" "IP address" >}} from time to time; a small program at home notices the change and updates the name's record, so the name always leads back to the house. Anyone who knows the name can find the current address, so it should only point at services meant to be reached from outside.
