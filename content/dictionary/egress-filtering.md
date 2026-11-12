---
title: "Outbound (egress) traffic and filtering"
term_kind: concept
topics: [networking, security-operations]
see_also: [ingress-filtering, firewall, exfiltration]
summary: "Controlling which connections may leave a network, not just which may come in."
match: ['\begress\b', '\boutbound (?:traffic|connections?|logging)\b', '\boutbound-only\b']
sources:
  - title: "Egress Filtering (glossary)"
    url: "https://csrc.nist.gov/glossary/term/egress_filtering"
    publisher: "NIST CSRC"
    primary: true
  - title: "SP 800-41 Rev. 1: Guidelines on Firewalls and Firewall Policy"
    url: "https://csrc.nist.gov/pubs/sp/800/41/r1/final"
    publisher: "NIST"
  - title: "Egress filtering"
    url: "https://en.wikipedia.org/wiki/Egress_filtering"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "M1037", topic: "Filter Network Traffic",
     url: "https://attack.mitre.org/mitigations/M1037/"}
  - {standard: sp800-53, clause: "SC-7", topic: "Boundary Protection",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-07"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Egress means traffic leaving a network, as opposed to {{< term "ingress-filtering" "ingress" >}}, traffic coming in. Egress filtering is a {{< term "firewall" >}} policy that limits which outgoing connections are allowed, for example letting each device reach only the services it needs. Most home and small-office networks block unwanted incoming connections but let anything out, which is how {{< term "malware" >}}, or a gadget quietly phoning its maker, can talk to the outside world unnoticed.
