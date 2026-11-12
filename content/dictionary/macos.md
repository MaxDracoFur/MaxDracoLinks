---
title: "macOS"
term_kind: tool
topics: [platforms-and-services]
summary: "Apple's operating system for Mac computers."
match: ['\bmacOS\b']
sources:
  - title: "macOS"
    url: "https://www.apple.com/macos/"
    publisher: "Apple"
    primary: true
  - title: "Apple Platform Security"
    url: "https://support.apple.com/guide/security/welcome/web"
    publisher: "Apple"
classification:
  - {standard: cpe, clause: "cpe:2.3:o:apple:macos", topic: "the name NVD files macOS vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Ao%3Aapple%3Amacos"}
  - {standard: attack, clause: "T1543.004", topic: "Create or Modify System Process: Launch Daemon",
     url: "https://attack.mitre.org/techniques/T1543/004/"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
macOS is the operating system Apple ships on its Mac computers. Underneath the graphical interface it is a Unix system, so it has a terminal and many of the same command-line tools as Linux. It keeps passwords and keys in an encrypted store called the Keychain, and runs background services through a system called launchd.
