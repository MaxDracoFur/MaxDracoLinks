---
title: "GitHub"
term_kind: organisation
topics: [platforms-and-services]
summary: "Website for hosting code with Git, owned by Microsoft."
match: ['\bGitHub\b']
sources:
  - title: "GitHub"
    url: "https://github.com/"
    publisher: "GitHub, Inc."
    primary: true
  - title: "GitHub Docs"
    url: "https://docs.github.com/"
    publisher: "GitHub, Inc."
classification:
  - {standard: attack, clause: "T1213.003", topic: "Data from Information Repositories: Code Repositories",
     url: "https://attack.mitre.org/techniques/T1213/003/"}
  - {standard: attack, clause: "T1567.001", topic: "Exfiltration Over Web Service: Exfiltration to Code Repository",
     url: "https://attack.mitre.org/techniques/T1567/001/"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: true
---
GitHub is a website for storing code and working on it together. Projects live in repositories that keep every change ever made, using the Git version-control system. Public repositories can be read by anyone, which is how most open-source software is shared, so a secret committed by mistake is quickly found by automated scanners. GitHub has been owned by Microsoft since 2018.
