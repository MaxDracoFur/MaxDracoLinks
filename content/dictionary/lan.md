---
title: "LAN"
term_kind: concept
topics: [networking]
summary: "A local area network: the devices connected together in one home, office or building."
match: ['\bLANs?\b']
sources:
  - title: "NIST glossary: local area network"
    url: "https://csrc.nist.gov/glossary/term/local_area_network"
    publisher: "NIST"
    primary: true
  - title: "Local area network"
    url: "https://en.wikipedia.org/wiki/Local_area_network"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1046", topic: "Network Service Discovery",
     url: "https://attack.mitre.org/techniques/T1046/"}
  - {standard: attack, clause: "T1557.002", topic: "ARP Cache Poisoning",
     url: "https://attack.mitre.org/techniques/T1557/002/"}
  - {standard: attack, clause: "M1030", topic: "Network Segmentation",
     url: "https://attack.mitre.org/mitigations/M1030/"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
A LAN (local area network) is the network inside one place: the computers, phones, printers and other devices in a home or office, connected by Ethernet cables or {{< term "wi-fi" >}} to the same switches. Devices on a LAN can usually reach each other directly, which is convenient but also means one compromised device can see and attack the others. A router connects the LAN to the internet.
