---
title: "Wi-Fi"
term_kind: standard
topics: [networking, hardware]
summary: "Wireless networking based on the IEEE 802.11 standards."
match: ['\bWi[-‑]?Fi\b']
sources:
  - title: "Wi-Fi Alliance"
    url: "https://www.wi-fi.org/"
    publisher: "Wi-Fi Alliance"
    primary: true
  - title: "Wi-Fi"
    url: "https://en.wikipedia.org/wiki/Wi-Fi"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1669", topic: "Wi-Fi Networks",
     url: "https://attack.mitre.org/techniques/T1669/"}
  - {standard: sp800-53, clause: "AC-18", topic: "Wireless Access",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AC-18"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: true
---
Wi-Fi is the everyday name for wireless local networking, built on the IEEE 802.11 standards and certified by the Wi-Fi Alliance. Devices connect to an access point by network name and, usually, a password; WPA2 and WPA3 encrypt the traffic between the device and the access point. Because radio reaches beyond walls, anyone nearby can see a Wi-Fi network and try to join it.
