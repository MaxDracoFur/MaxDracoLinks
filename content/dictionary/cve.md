---
title: "CVE"
term_kind: standard
topics: [security-operations]
see_also: [vulnerability, kev, cisa]
summary: "A public ID number, like CVE-2024-12345, given to a specific known security flaw."
match: ['\bCVEs?\b']
sources:
  - title: "Overview"
    url: "https://www.cve.org/About/Overview"
    publisher: "CVE Program"
    primary: true
  - title: "Common Vulnerabilities and Exposures"
    url: "https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "RA-5", topic: "Vulnerability Monitoring and Scanning",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=RA-05"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
CVE (Common Vulnerabilities and Exposures) is a shared naming system for publicly known security flaws. Each {{< term "vulnerability" >}} gets an ID made of the year and a number, such as CVE-2024-12345, so vendors, scanners and alerts can all be sure they mean the same bug. The program is run by MITRE with US government funding; an ID says a flaw exists, not how serious it is or whether anyone is using it.
