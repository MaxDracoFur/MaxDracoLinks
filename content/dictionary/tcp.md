---
title: "TCP"
term_kind: protocol
topics: [networking]
summary: "The internet protocol that delivers data reliably and in order between two programs."
match: ['\bTCP\b']
sources:
  - title: "RFC 9293: Transmission Control Protocol (TCP)"
    url: "https://www.rfc-editor.org/rfc/rfc9293"
    publisher: "IETF"
    primary: true
  - title: "Transmission Control Protocol"
    url: "https://en.wikipedia.org/wiki/Transmission_Control_Protocol"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1095", topic: "Non-Application Layer Protocol",
     url: "https://attack.mitre.org/techniques/T1095/"}
  - {standard: capec, clause: "CAPEC-287", topic: "TCP SYN Scan",
     url: "https://capec.mitre.org/data/definitions/287.html"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-12). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
TCP (Transmission Control Protocol) is one of the two basic ways programs send data over the internet (the other is {{< term "udp" >}}). Before sending anything, the two sides set up a connection with a short {{< term "handshake" "handshake" >}}. TCP then numbers the data, resends anything lost and puts it back in order, so the receiving program sees one reliable stream. The web, email and {{< term "ssh" >}} all run over it.
