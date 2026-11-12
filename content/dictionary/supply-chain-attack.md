---
title: "Software supply chain (attack)"
term_kind: concept
topics: [security-operations]
see_also: [open-source, container, vulnerability]
summary: "Attacking people by tampering with software or tools they trust and install, instead of attacking them directly."
match: ['\bsupply[- ]chains?\b']
sources:
  - title: "supply chain attack (glossary)"
    url: "https://csrc.nist.gov/glossary/term/supply_chain_attack"
    publisher: "NIST CSRC"
    primary: true
  - title: "Supply chain attack"
    url: "https://en.wikipedia.org/wiki/Supply_chain_attack"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1195", topic: "Supply Chain Compromise",
     url: "https://attack.mitre.org/techniques/T1195/"}
  - {standard: sp800-53, clause: "SR-3", topic: "Supply Chain Controls and Processes",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SR-03"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A piece of software's supply chain is everything it is built from and delivered through: the libraries it uses, the build system, the download server, the update mechanism. A supply chain attack tampers with one of those links, so a trusted program arrives with something malicious inside and everyone who installs or updates it is hit at once. Security tools are software too, and have supply chains of their own.
