---
title: "API key"
term_kind: concept
summary: "A secret string a program sends to prove which account it is calling an API as."
match: ['\bAPI[ _-]?keys?\b']
topics: [identity-and-access]
see_also: [base64]
sources:
  - title: "API key"
    url: "https://en.wikipedia.org/wiki/API_key"
    publisher: "Wikipedia"
    primary: true
classification:
  - {standard: attack, clause: "T1552.001", topic: "Credentials In Files",
     url: "https://attack.mitre.org/techniques/T1552/001/"}
  - {standard: attack, clause: "T1550.001", topic: "Application Access Token",
     url: "https://attack.mitre.org/techniques/T1550/001/"}
  - {standard: cwe, clause: "CWE-798", topic: "Use of Hard-coded Credentials",
     url: "https://cwe.mitre.org/data/definitions/798.html"}
  - {standard: cwe, clause: "CWE-522", topic: "Insufficiently Protected Credentials",
     url: "https://cwe.mitre.org/data/definitions/522.html"}
  - {standard: sp800-53, clause: "IA-5", topic: "Authenticator Management",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=IA-05"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary); Max approved it 2026-11-11.
# Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
An API key is a long random string that identifies a program to a service's API, a bit like a password made for software. Some services use a key alone; others pair a key with a separate secret. Anyone who gets hold of a working key can act as its owner, so keys are kept private and replaced when they might have been exposed.
