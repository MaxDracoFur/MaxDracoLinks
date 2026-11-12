---
title: "Flipper Zero"
term_kind: thing
topics: [hardware, security-operations]
summary: "Pocket-sized multi-tool for exploring radio, infrared, NFC and other wireless signals."
match: ['\bFlipper Zero\b', '\bFlipper\b']
sources:
  - title: "Flipper Zero"
    url: "https://flipper.net/"
    publisher: "Flipper Devices"
    primary: true
  - title: "Flipper Zero documentation"
    url: "https://docs.flipper.net/"
    publisher: "Flipper Devices"
  - title: "flipperdevices/flipperzero-firmware source code"
    url: "https://github.com/flipperdevices/flipperzero-firmware"
    publisher: "GitHub"
classification:
  - {standard: attack, clause: "T1200", topic: "Hardware Additions",
     url: "https://attack.mitre.org/techniques/T1200/"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Flipper Zero is a small handheld device for experimenting with the signals around everyday electronics. It can read, save and replay sub-GHz radio, infrared remote, NFC and RFID signals, act as a {{< term "usb" >}} keyboard, and talk to hardware through its GPIO pins. Its firmware is open source, and people extend it with their own apps. It is popular with hardware hackers and security testers.
