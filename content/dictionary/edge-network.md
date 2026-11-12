---
title: "Edge network (CDN)"
term_kind: concept
topics: [platforms-and-services, networking]
see_also: [cloudflare, proxy, cloudflare-tunnel]
summary: "A provider's servers spread around the world that sit between visitors and a website."
match: ['\bCloudflare(?:''|’)s edge\b', '\bedge (?:network|servers?)\b', '\bCDNs?\b', '\bcontent delivery networks?\b']
sources:
  - title: "Content Delivery Network (CDN) Reference Architecture"
    url: "https://developers.cloudflare.com/reference-architecture/architectures/cdn/"
    publisher: "Cloudflare"
    primary: true
  - title: "Traffic flow through Cloudflare"
    url: "https://developers.cloudflare.com/fundamentals/concepts/traffic-flow-cloudflare/"
    publisher: "Cloudflare"
  - title: "Content delivery network"
    url: "https://en.wikipedia.org/wiki/Content_delivery_network"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A content delivery network (CDN) is a set of servers spread around the world, called its edge, that sit between visitors and a website. A visitor connects to the nearest edge server, which answers from its own copy of the site or passes the request on to the site's real server, called the origin. Because visitors only ever talk to the edge, the provider can soak up attack traffic and hide the origin's address, but it also sees everything that passes through. {{< term "cloudflare" >}} runs one of the largest.
