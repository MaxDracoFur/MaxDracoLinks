---
title: "Cloudflare Tunnel"
term_kind: tool
topics: [networking, platforms-and-services]
see_also: [cloudflare, tunnel, vpn]
summary: "Cloudflare's service that publishes something on a private network to the internet without opening it to incoming connections."
match: ['\bCloudflare Tunnels?\b']
sources:
  - title: "Cloudflare Tunnel"
    url: "https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/"
    publisher: "Cloudflare"
    primary: true
  - title: "cloudflared"
    url: "https://github.com/cloudflare/cloudflared"
    publisher: "Cloudflare"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:cloudflare:cloudflared", topic: "the name NVD files cloudflared vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Acloudflare%3Acloudflared"}
  - {standard: attack, clause: "T1572", topic: "Protocol Tunneling",
     url: "https://attack.mitre.org/techniques/T1572/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
This service from {{< term "cloudflare" >}} lets you put a website or app on the internet without opening your network to it. A small program called cloudflared runs inside your network and makes an outgoing connection to Cloudflare, and Cloudflare then passes visitors' requests down that {{< term "tunnel" >}} to your service, so nothing on the network has to accept incoming connections. The trade-off is that Cloudflare sits in the middle and handles every request.
