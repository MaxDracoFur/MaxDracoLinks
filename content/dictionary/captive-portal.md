---
title: "Captive portal"
term_kind: concept
topics: [networking, web-and-advertising]
see_also: [wi-fi, dns-tunneling]
summary: "The sign-in or terms page a public Wi-Fi network shows before it lets you onto the internet."
match: ['\bcaptive portals?\b']
sources:
  - title: "RFC 8952: Captive Portal Architecture"
    url: "https://www.rfc-editor.org/rfc/rfc8952.html"
    publisher: "IETF"
    primary: true
  - title: "Captive portal"
    url: "https://en.wikipedia.org/wiki/Captive_portal"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A captive portal is the page that pops up when you join {{< term "wi-fi" >}} in a hotel, airport or café, asking you to log in, pay, or accept terms. Until you do, the network blocks almost everything except that page, though name lookups ({{< term "dns" >}}) often still get through. Because the network is sitting between you and the internet, it can also see and interfere with traffic that isn't {{< term "encryption" "encrypted" >}}.
