---
title: "Base64"
term_kind: technology
summary: "A way to write any binary data using only 64 printable characters: A-Z, a-z, 0-9, + and /."
match: ['\bbase64\b']
sources:
  - title: "RFC 4648: The Base16, Base32, and Base64 Data Encodings"
    url: "https://www.rfc-editor.org/rfc/rfc4648"
    publisher: "IETF"
    primary: true
  - title: "Base64"
    url: "https://en.wikipedia.org/wiki/Base64"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1132.001", topic: "Standard Encoding",
     url: "https://attack.mitre.org/techniques/T1132/001/"}
  - {standard: attack, clause: "T1027", topic: "Obfuscated Files or Information",
     url: "https://attack.mitre.org/techniques/T1027/"}
  - {standard: attack, clause: "T1140", topic: "Deobfuscate/Decode Files or Information",
     url: "https://attack.mitre.org/techniques/T1140/"}
  - {standard: capec, clause: "CAPEC-267", topic: "Leverage Alternate Encoding",
     url: "https://capec.mitre.org/data/definitions/267.html"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: true
---
Base64 turns bytes into text so they can travel through systems that only handle letters and digits, such as email, URLs or config files. Every 3 bytes become 4 characters, and = signs pad the end. It is an encoding, not encryption: anyone can turn it back into the original bytes.
