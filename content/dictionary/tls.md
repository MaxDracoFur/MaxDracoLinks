---
title: "TLS"
term_kind: protocol
summary: "Transport Layer Security: the encryption that protects data on its way across a network (the S in HTTPS)."
match: ['\bTLS\b']
topics: [cryptography, networking]
see_also: [udp]
sources:
  - title: "RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3"
    url: "https://www.rfc-editor.org/rfc/rfc8446"
    publisher: "IETF"
    primary: true
  - title: "Transport Layer Security"
    url: "https://en.wikipedia.org/wiki/Transport_Layer_Security"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1557", topic: "Adversary-in-the-Middle",
     url: "https://attack.mitre.org/techniques/T1557/"}
  - {standard: capec, clause: "CAPEC-94", topic: "Adversary in the Middle (AiTM)",
     url: "https://capec.mitre.org/data/definitions/94.html"}
  - {standard: cwe, clause: "CWE-319", topic: "Cleartext Transmission of Sensitive Information",
     url: "https://cwe.mitre.org/data/definitions/319.html"}
  - {standard: cwe, clause: "CWE-295", topic: "Improper Certificate Validation",
     url: "https://cwe.mitre.org/data/definitions/295.html"}
  - {standard: sp800-53, clause: "SC-8", topic: "Transmission Confidentiality and Integrity",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-08"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary); Max approved it 2026-11-11.
# Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
TLS encrypts a connection between two programs and lets the client check it is talking to the right server. It replaced SSL, and it is what puts the padlock on HTTPS websites. The current version, TLS 1.3, is defined in RFC 8446. Other protocols, syslog among them, can run over TLS too.
