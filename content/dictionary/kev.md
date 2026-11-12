---
title: "KEV (Known Exploited Vulnerabilities catalogue)"
term_kind: standard
topics: [security-operations]
see_also: [cisa, cve, vulnerability]
summary: "CISA's public list of software vulnerabilities known to be used in real attacks."
match: ['\bKEV\b', '\bKnown Exploited Vulnerabilities\b']
sources:
  - title: "Known Exploited Vulnerabilities Catalog"
    url: "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    primary: true
  - title: "Reducing the Significant Risk of Known Exploited Vulnerabilities"
    url: "https://www.cisa.gov/known-exploited-vulnerabilities-catalog/reducing-significant-risk-known-exploited-vulnerabilities"
    publisher: "CISA"
classification:
  - {standard: sp800-53, clause: "SI-2", topic: "Flaw Remediation",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SI-02"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
The Known Exploited Vulnerabilities (KEV) catalogue is a list kept by {{< term "cisa" >}}, the US government's cybersecurity agency, of {{< term "cve" "CVEs" >}} that attackers are known to be using. Each entry gives the vendor, the product, a short description and what to do about it, and the whole list is free to download as {{< term "json" >}}. It helps decide which updates to install first: a flaw on the list is being exploited, not just possible.
