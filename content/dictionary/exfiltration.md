---
title: "Exfiltration"
term_kind: concept
topics: [security-operations]
see_also: [egress-filtering, dns-tunneling, malware]
summary: "Moving data out of a system or network without permission."
match: ['\bexfiltrat(?:e|es|ed|ing|ion)\b']
sources:
  - title: "exfiltration (glossary)"
    url: "https://csrc.nist.gov/glossary/term/exfiltration"
    publisher: "NIST CSRC"
    primary: true
  - title: "Data exfiltration"
    url: "https://en.wikipedia.org/wiki/Data_exfiltration"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1048", topic: "Exfiltration Over Alternative Protocol",
     url: "https://attack.mitre.org/techniques/T1048/"}
  - {standard: attack, clause: "T1567", topic: "Exfiltration Over Web Service",
     url: "https://attack.mitre.org/techniques/T1567/"}
  - {standard: sp800-53, clause: "SC-7(10)", topic: "Prevent Exfiltration",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-07(10)"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Exfiltration is moving data out of a system or network without permission: an intruder, or a program acting for one, copying passwords, keys or files to somewhere they control. It is often the whole point of a break-in, and the data is usually hidden inside normal-looking traffic such as web requests or {{< term "dns" >}} lookups. Limiting what a machine or program may send out, {{< term "egress-filtering" "egress filtering" >}}, is the main defence.
