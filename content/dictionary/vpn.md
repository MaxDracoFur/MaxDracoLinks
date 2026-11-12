---
title: "VPN"
term_kind: concept
topics: [networking, cryptography]
summary: "An encrypted tunnel that joins a device to a network it isn't physically on."
match: ['\bVPNs?\b']
sources:
  - title: "NIST glossary: virtual private network"
    url: "https://csrc.nist.gov/glossary/term/virtual_private_network"
    publisher: "NIST"
    primary: true
  - title: "SP 800-77 Rev. 1: Guide to IPsec VPNs"
    url: "https://csrc.nist.gov/pubs/sp/800/77/r1/final"
    publisher: "NIST"
classification:
  - {standard: attack, clause: "T1133", topic: "External Remote Services",
     url: "https://attack.mitre.org/techniques/T1133/"}
  - {standard: attack, clause: "M1032", topic: "Multi-factor Authentication",
     url: "https://attack.mitre.org/mitigations/M1032/"}
  - {standard: sp800-53, clause: "AC-17", topic: "Remote Access",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AC-17"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
A VPN (virtual private network) creates an encrypted tunnel from a device to another network, so the device can use that network as if it were plugged in there. Companies use VPNs to let staff reach internal systems from home; individuals use them to get back to their home network, or to hide their traffic from the local network they're on. Anything on the local network sees only encrypted traffic going to the VPN server.
