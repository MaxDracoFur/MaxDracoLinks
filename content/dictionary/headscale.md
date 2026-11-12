---
title: "Headscale"
term_kind: tool
topics: [networking, identity-and-access]
see_also: [tailscale, zerotier, control-plane]
summary: "Open-source, self-hosted replacement for Tailscale's coordination server."
match: ['\bHeadscale\b']
sources:
  - title: "Headscale"
    url: "https://headscale.net/"
    publisher: "Headscale project"
    primary: true
  - title: "juanfont/headscale"
    url: "https://github.com/juanfont/headscale"
    publisher: "GitHub"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12.
draft: false
---
Headscale is a free, {{< term "self-hosting" "self-hosted" >}} version of the {{< term "control-plane" "coordination server" >}} behind {{< term "tailscale" >}}. Tailscale devices connect to each other directly over {{< term "wireguard" >}}, but a central server decides which devices belong to the network and passes their keys around. Headscale lets you run that server yourself instead of relying on the company's, which also makes keeping it secure your job.
