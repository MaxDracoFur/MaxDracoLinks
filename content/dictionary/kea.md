---
title: "Kea (DHCP server)"
term_kind: tool
topics: [networking]
see_also: [dhcp, opnsense, ip-address]
summary: "Open-source DHCP server from ISC that hands out IP addresses to devices on a network."
match: ['\bKea\b']
sources:
  - title: "Kea"
    url: "https://www.isc.org/kea/"
    publisher: "Internet Systems Consortium"
    primary: true
  - title: "Kea Administrator Reference Manual"
    url: "https://kea.readthedocs.io/en/stable/"
    publisher: "Internet Systems Consortium"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:isc:kea", topic: "the name NVD files Kea vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Aisc%3Akea"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Kea is a {{< term "dhcp" >}} server made by the Internet Systems Consortium (ISC), the successor to their older ISC DHCP server. It hands out {{< term "ip-address" "IP addresses" >}} to devices as they join a network, for both IPv4 and IPv6, and keeps a record of which device has which address, called its leases. {{< term "firewall" "Firewall" >}} systems such as {{< term "opnsense" >}} ship it as their DHCP service.
