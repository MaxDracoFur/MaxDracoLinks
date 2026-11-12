---
title: "Back door"
term_kind: concept
topics: [security-operations]
see_also: [attack-surface, malware]
summary: "A hidden or forgotten way into a system that gets around its normal security checks."
match: ['\bback[- ]?doors?\b']
sources:
  - title: "backdoor"
    url: "https://csrc.nist.gov/glossary/term/backdoor"
    publisher: "NIST CSRC"
    primary: true
  - title: "Backdoor (computing)"
    url: "https://en.wikipedia.org/wiki/Backdoor_(computing)"
    publisher: "Wikipedia"
classification:
  - {standard: cwe, clause: "CWE-912", topic: "Hidden Functionality",
     url: "https://cwe.mitre.org/data/definitions/912.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A back door is a way into a computer or service that skips the normal front door of logins and permissions. Some are planted on purpose by an attacker or a careless developer; others are leftovers, such as an old account, a test setting or a forgotten connection that still works. Either way, the owner usually doesn't know it is there, which is what makes it dangerous.
