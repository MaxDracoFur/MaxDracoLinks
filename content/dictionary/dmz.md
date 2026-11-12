---
title: "DMZ"
term_kind: concept
topics: [networking, security-operations]
see_also: [subnet, vlan, firewall]
summary: "A separate part of a network for machines that must be reachable from the internet."
match: ['\bDMZs?\b']
sources:
  - title: "DMZ (glossary)"
    url: "https://csrc.nist.gov/glossary/term/dmz"
    publisher: "NIST CSRC"
    primary: true
  - title: "DMZ (computing)"
    url: "https://en.wikipedia.org/wiki/DMZ_(computing)"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "SC-7", topic: "Boundary Protection",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-07"}
  - {standard: attack, clause: "M1030", topic: "Network Segmentation",
     url: "https://attack.mitre.org/mitigations/M1030/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A DMZ (demilitarised zone) is a separate part of a network for machines that need to be reachable from the internet, such as a web server. It sits between the internet and the private network, with {{< term "firewall" >}} rules on both sides, so if a machine in the DMZ is broken into, the attacker still can't reach the private devices directly. On a small network it is usually built as its own {{< term "vlan" >}} or {{< term "subnet" >}}.
