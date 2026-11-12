---
title: "USB"
term_kind: standard
topics: [hardware]
summary: "The standard plug and protocol for connecting devices to computers."
match: ['\bUSB\b']
sources:
  - title: "USB Implementers Forum"
    url: "https://www.usb.org/"
    publisher: "USB-IF"
    primary: true
  - title: "USB"
    url: "https://en.wikipedia.org/wiki/USB"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1200", topic: "Hardware Additions",
     url: "https://attack.mitre.org/techniques/T1200/"}
  - {standard: attack, clause: "T1091", topic: "Replication Through Removable Media",
     url: "https://attack.mitre.org/techniques/T1091/"}
  - {standard: attack, clause: "M1034", topic: "Limit Hardware Installation",
     url: "https://attack.mitre.org/mitigations/M1034/"}
  - {standard: sp800-53, clause: "MP-7", topic: "Media Use",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=MP-07"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: true
---
USB (Universal Serial Bus) is the standard way to plug keyboards, storage, network adapters, phones and almost anything else into a computer, and to power them. A USB device tells the computer what kind of device it is, and the computer loads a driver to match. That trust is why a malicious device can pretend to be a keyboard, and why some systems limit which USB devices they accept.
