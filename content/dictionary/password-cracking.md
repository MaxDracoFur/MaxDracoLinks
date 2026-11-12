---
title: "Offline password cracking"
term_kind: concept
topics: [identity-and-access, cryptography]
see_also: [hash-function, handshake, wpa]
summary: "Guessing a password by testing candidates against a stolen copy of something derived from it, away from the system it protects."
match: ['\bpassword[- ]cracking\b', '\bcrack(?:s|ed|ing)? (?:the |a )?passwords?\b', '\bguess(?:es|ed|ing)? the password offline\b', '\boffline (?:password )?(?:cracking|guessing)\b']
sources:
  - title: "NIST CSRC Glossary: offline attack"
    url: "https://csrc.nist.gov/glossary/term/offline_attack"
    publisher: "NIST"
    primary: true
  - title: "Password cracking"
    url: "https://en.wikipedia.org/wiki/Password_cracking"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1110.002", topic: "Brute Force: Password Cracking",
     url: "https://attack.mitre.org/techniques/T1110/002/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
If an attacker gets hold of something derived from a password, such as a stored {{< term "hash-function" "hash" >}} or a recorded {{< term "wi-fi" >}} {{< term "handshake" >}}, they can test guesses against it on their own computers. Nothing on the real system sees those guesses, so there is no lockout and no alert, and modern hardware can try billions of guesses a second. Long, random passwords are what defeat it; short or common ones fall quickly.
