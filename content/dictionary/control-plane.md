---
title: "Control plane"
term_kind: concept
topics: [networking, platforms-and-services]
see_also: [headscale, tailscale, kubernetes]
summary: "The part of a system that decides how things should be set up, as opposed to the part that carries the actual traffic or work."
match: ['\bcontrol planes?\b', '\bcoordination (?:service|server)s?\b']
sources:
  - title: "Kubernetes Components"
    url: "https://kubernetes.io/docs/concepts/overview/components/"
    publisher: "Kubernetes"
    primary: true
  - title: "How Tailscale works"
    url: "https://tailscale.com/blog/how-tailscale-works"
    publisher: "Tailscale"
  - title: "Control plane"
    url: "https://en.wikipedia.org/wiki/Control_plane"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Many systems are split in two: a control plane that makes the decisions and a data plane that does the work. In a mesh {{< term "vpn" >}} such as {{< term "tailscale" >}}, the control plane (a coordination service) tells devices about each other and hands out keys, while the {{< term "encryption" "encrypted" >}} traffic flows directly between the devices. Whoever runs the control plane can add or remove members, so it matters who operates it.
