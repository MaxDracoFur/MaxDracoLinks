---
title: "Google"
term_kind: organisation
topics: [platforms-and-services]
summary: "US technology company behind the Google search engine, Gmail, Android and Google Analytics."
match: ['\bGoogle\b']
sources:
  - title: "About Google"
    url: "https://about.google/"
    publisher: "Google"
    primary: true
  - title: "Google"
    url: "https://en.wikipedia.org/wiki/Google"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1102", topic: "Web Service",
     url: "https://attack.mitre.org/techniques/T1102/"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Google is a US technology company, part of Alphabet, best known for its search engine. It also runs Gmail, YouTube, the Android phone operating system, an advertising network that pays websites to show ads, and Google Analytics, which tells site owners who visits. Because so many people trust and use its services, attackers sometimes hide their own traffic inside them.
