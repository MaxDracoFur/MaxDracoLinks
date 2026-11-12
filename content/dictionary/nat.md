---
title: "NAT (and hairpin NAT)"
term_kind: concept
topics: [networking]
see_also: [router, ip-address, port-forwarding]
summary: "Network address translation: how a router lets many devices share one public internet address."
match: ['\bNAT\b', '\bnetwork address translation\b']
sources:
  - title: "RFC 2663: IP Network Address Translator (NAT) Terminology and Considerations"
    url: "https://www.rfc-editor.org/info/rfc2663/"
    publisher: "IETF"
    primary: true
  - title: "RFC 4787: NAT Behavioral Requirements for Unicast UDP"
    url: "https://www.rfc-editor.org/info/rfc4787/"
    publisher: "IETF"
  - title: "Network address translation"
    url: "https://en.wikipedia.org/wiki/Network_address_translation"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
NAT (network address translation) is what a home {{< term "router" >}} does so that every device in the house can share one public {{< term "ip-address" "IP address" >}}: it rewrites the addresses on outgoing traffic and remembers which reply belongs to which device. A side effect is that outsiders can't start a connection to a device inside unless a {{< term "port-forwarding" "port forward" >}} allows it. Hairpin NAT is the trick that lets a device inside reach the network's own public address and loop back in, so testing from inside doesn't show what the internet sees.
