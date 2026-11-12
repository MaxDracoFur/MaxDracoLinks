---
title: "MAC address"
term_kind: concept
topics: [networking, hardware]
see_also: [ip-address, arp, spoofing]
summary: "The hardware address that identifies a network card on its local network."
match: ['\bMAC address(?:es)?\b', '\bMAC (?:spoofing|randomi[sz]ation|rotation)\b', '\b(?:randomi[sz]ed|cloned) MACs?\b']
sources:
  - title: "IEEE Registration Authority"
    url: "https://standards.ieee.org/products-programs/regauth/"
    publisher: "IEEE"
    primary: true
  - title: "MAC address"
    url: "https://en.wikipedia.org/wiki/MAC_address"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A MAC address is a 48-bit number, written like 3c:22:fb:12:34:56, that names a network card on the local network; switches use it to deliver traffic to the right device. Its first half normally identifies the manufacturer, from blocks handed out by the IEEE. It is easy to change in software, so it is not proof of who a device is: modern phones pick random ones for privacy, and an intruder can {{< term "spoofing" "copy" >}} a trusted device's address.
