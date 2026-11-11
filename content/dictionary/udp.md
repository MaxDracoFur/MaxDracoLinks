---
title: "UDP"
term_kind: technology
summary: "User Datagram Protocol: a simple, connectionless way to send small messages over a network, with no delivery guarantee and no encryption."
match: ['\bUDP\b']
sources:
  - title: "RFC 768: User Datagram Protocol"
    url: "https://www.rfc-editor.org/rfc/rfc768"
    publisher: "IETF"
    primary: true
  - title: "User Datagram Protocol"
    url: "https://en.wikipedia.org/wiki/User_Datagram_Protocol"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1095", topic: "Non-Application Layer Protocol",
     url: "https://attack.mitre.org/techniques/T1095/"}
  - {standard: capec, clause: "CAPEC-308", topic: "UDP Scan",
     url: "https://capec.mitre.org/data/definitions/308.html"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary); Max approved it 2026-11-11.
# Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
UDP is one of the two basic ways programs send data over the internet (the other is TCP). A sender just fires off a datagram: there is no connection set-up, no confirmation it arrived, and nothing on its own that encrypts it. That makes it fast and simple, which is why DNS, games, video calls and classic syslog use it.
