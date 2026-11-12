---
title: "Ingress filtering"
term_kind: concept
topics: [networking, security-operations]
see_also: [egress-filtering, vlan-hopping, spoofing]
summary: "Dropping incoming traffic at the point where it enters a device or network when it has no business arriving there."
match: ['\bingress[- ]filter(?:ing|s|ed)?\b']
sources:
  - title: "IEEE 802.1Q: Bridges and Bridged Networks"
    url: "https://standards.ieee.org/ieee/802.1Q/6844/"
    publisher: "IEEE"
    primary: true
  - title: "RFC 2827 (BCP 38): Network Ingress Filtering"
    url: "https://www.rfc-editor.org/info/rfc2827/"
    publisher: "IETF"
classification:
  - {standard: attack, clause: "M1037", topic: "Filter Network Traffic",
     url: "https://attack.mitre.org/mitigations/M1037/"}
  - {standard: sp800-53, clause: "SC-7", topic: "Boundary Protection",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-07"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Ingress filtering means checking traffic as it comes in and dropping anything that shouldn't be arriving on that connection. On a {{< term "network-switch" "switch" >}}, it drops traffic tagged for a {{< term "vlan" >}} that the incoming port doesn't belong to, which blocks one way of jumping between VLANs but not every way. On the internet, it means a network refusing traffic whose sender address couldn't really be behind the link it came in on, which makes {{< term "spoofing" >}} harder.
