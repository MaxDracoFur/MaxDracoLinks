---
title: "Tailscale"
term_kind: tool
topics: [networking, platforms-and-services]
see_also: [wireguard, headscale, zerotier]
summary: "A commercial service that builds a private network between your devices on top of WireGuard, managed from the company's servers."
match: ['\bTailscale\b', '\bTailnet Lock\b']
sources:
  - title: "Tailscale"
    url: "https://tailscale.com/"
    publisher: "Tailscale"
    primary: true
  - title: "Tailnet Lock"
    url: "https://tailscale.com/docs/features/tailnet-lock"
    publisher: "Tailscale"
  - title: "Tailscale"
    url: "https://en.wikipedia.org/wiki/Tailscale"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1133", topic: "External Remote Services",
     url: "https://attack.mitre.org/techniques/T1133/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Tailscale is a service that connects your devices into one private network, wherever they are, using {{< term "wireguard" >}} for the {{< term "encryption" "encryption" >}}. Its appeal is that it needs almost no setup. The company's servers decide which devices may join, so by default the company, or anyone who controls your login, could add a device. An optional feature called Tailnet Lock makes your own devices approve every new one instead.
