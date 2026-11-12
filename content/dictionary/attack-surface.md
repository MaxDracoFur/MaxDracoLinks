---
title: "Attack surface"
term_kind: concept
topics: [security-operations]
see_also: [vulnerability, least-privilege]
summary: "All the places where an attacker could try to get into or misuse a system."
match: ['\battack surfaces?\b']
sources:
  - title: "attack surface"
    url: "https://csrc.nist.gov/glossary/term/attack_surface"
    publisher: "NIST CSRC"
    primary: true
  - title: "Attack surface"
    url: "https://en.wikipedia.org/wiki/Attack_surface"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "SA-15(5)", topic: "Attack Surface Reduction",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SA-15(05)"}
  - {standard: sp800-53, clause: "CM-7", topic: "Least Functionality",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=CM-07"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A system's attack surface is the sum of the ways in from the outside: every open {{< term "network-port" "port" >}}, login page, feature, cable and piece of software an attacker could poke at. Each one is a place where a {{< term "vulnerability" >}} might be found. The usual advice is to make it smaller: switch off features nobody uses, close what doesn't need to be open, and give programs only the access they need.
