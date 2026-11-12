---
title: "NetFlow (network flow records)"
term_kind: protocol
topics: [networking, logging-and-monitoring]
see_also: [packet, router]
summary: "A way for routers to record a summary of every network conversation: who talked to whom, when, and how much."
match: ['\bNetFlow\b', '\bIPFIX\b', '\bflow records?\b']
sources:
  - title: "RFC 3954: Cisco Systems NetFlow Services Export Version 9"
    url: "https://www.rfc-editor.org/info/rfc3954/"
    publisher: "IETF"
    primary: true
  - title: "NetFlow"
    url: "https://en.wikipedia.org/wiki/NetFlow"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
NetFlow is a format, created by {{< term "cisco" >}} and later standardised by the IETF as IPFIX, in which a {{< term "router" >}} or {{< term "firewall" >}} reports each network conversation as a short record: the two addresses, the ports, the start and end time, and how many bytes went each way. It doesn't keep the contents, so it is cheap enough to store for every connection. That makes flow records good evidence afterwards for which machines a piece of data could have gone to.
