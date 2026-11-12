---
title: "Reverse lookup"
term_kind: concept
topics: [web-and-advertising, security-operations]
see_also: [dns, google-adsense, google-analytics]
summary: "Starting from an identifier, such as an IP address or an ad account ID, and finding everything that uses it."
match: ['\breverse lookups?\b', '\breverse DNS\b', '\bthird-party lookups?\b']
sources:
  - title: "RFC 1035: Domain Names - Implementation and Specification (IN-ADDR.ARPA, section 3.5)"
    url: "https://www.rfc-editor.org/rfc/rfc1035.html"
    publisher: "IETF"
    primary: true
  - title: "Reverse DNS lookup"
    url: "https://en.wikipedia.org/wiki/Reverse_DNS_lookup"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1596", topic: "Search Open Technical Databases",
     url: "https://attack.mitre.org/techniques/T1596/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A normal lookup goes from a name to a value, such as a website name to its address. A reverse lookup goes the other way: start from the value and find the names behind it. The classic example is reverse {{< term "dns" >}}, which turns an {{< term "ip-address" "IP address" >}} back into a host name. Commercial services do the same for ad and analytics account IDs, listing every website where an ID has been seen, which is a common way to find sites run by the same person.
