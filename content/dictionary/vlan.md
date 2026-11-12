---
title: "VLAN"
term_kind: standard
topics: [networking]
summary: "A way to split one physical network into separate virtual networks."
match: ['\bVLANs?\b']
sources:
  - title: "IEEE 802.1Q: Bridges and Bridged Networks"
    url: "https://standards.ieee.org/ieee/802.1Q/6844/"
    publisher: "IEEE"
    primary: true
  - title: "VLAN"
    url: "https://en.wikipedia.org/wiki/VLAN"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "M1030", topic: "Network Segmentation",
     url: "https://attack.mitre.org/mitigations/M1030/"}
  - {standard: attack, clause: "T1599", topic: "Network Boundary Bridging",
     url: "https://attack.mitre.org/techniques/T1599/"}
  - {standard: sp800-53, clause: "SC-7", topic: "Boundary Protection",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-07"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
A VLAN (virtual {{< term "lan" >}}) lets one set of switches and cables carry several separate networks. Each frame is tagged with a VLAN number, and switches only deliver it to ports in the same VLAN, so devices on different VLANs can't talk directly. Traffic between them has to go through a {{< term "router" "router" >}} or {{< term "firewall" "firewall" >}}, where rules decide what is allowed. Guest networks and networks for untrusted devices are usually built this way.
