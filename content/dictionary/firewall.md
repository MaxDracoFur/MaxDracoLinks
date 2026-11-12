---
title: "Firewall"
term_kind: concept
topics: [networking, security-operations]
see_also: [egress-filtering, router, dmz]
summary: "A device or program that decides which network traffic is allowed to pass."
match: ['\bfirewalls?\b']
sources:
  - title: "SP 800-41 Rev. 1: Guidelines on Firewalls and Firewall Policy"
    url: "https://csrc.nist.gov/pubs/sp/800/41/r1/final"
    publisher: "NIST"
    primary: true
  - title: "Firewall (glossary)"
    url: "https://csrc.nist.gov/glossary/term/firewall"
    publisher: "NIST CSRC"
  - title: "Firewall (computing)"
    url: "https://en.wikipedia.org/wiki/Firewall_(computing)"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "SC-7", topic: "Boundary Protection",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-07"}
  - {standard: attack, clause: "M1037", topic: "Filter Network Traffic",
     url: "https://attack.mitre.org/mitigations/M1037/"}
  - {standard: attack, clause: "T1686", topic: "Disable or Modify System Firewall",
     url: "https://attack.mitre.org/techniques/T1686/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A firewall decides which network traffic is allowed to pass, using rules such as "let visitors reach this web server, block everything else". It can be a dedicated box where a network meets the internet, often the same box as the {{< term "router" >}}, or software on a single computer. A firewall only sees traffic that passes through it: devices on the same {{< term "subnet" "network segment" >}} talk to each other directly, and connections a device opens outward look like normal use unless {{< term "egress-filtering" "outbound traffic" >}} is filtered too.
