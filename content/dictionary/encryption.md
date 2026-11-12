---
title: "Encryption"
term_kind: concept
topics: [cryptography]
see_also: [public-key-cryptography, tls, hash-function]
summary: "Scrambling data with a key so only someone holding the right key can read it."
match: ['\bencrypt(?:s|ed|ion|ing)?\b']
sources:
  - title: "Encryption (glossary)"
    url: "https://csrc.nist.gov/glossary/term/encryption"
    publisher: "NIST CSRC"
    primary: true
  - title: "Encryption"
    url: "https://en.wikipedia.org/wiki/Encryption"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "SC-13", topic: "Cryptographic Protection",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-13"}
  - {standard: sp800-53, clause: "SC-8", topic: "Transmission Confidentiality and Integrity",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-08"}
  - {standard: cwe, clause: "CWE-311", topic: "Missing Encryption of Sensitive Data",
     url: "https://cwe.mitre.org/data/definitions/311.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Encryption scrambles data with a key so that only someone holding the right key can turn it back into something readable. It protects data travelling over a network, as {{< term "tls" >}} does for websites, and data stored on a disk or in a backup. It keeps outsiders from reading the data, but it says nothing about who holds the keys: anyone who has them can read everything.
