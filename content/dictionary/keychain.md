---
title: "Keychain (macOS)"
term_kind: tool
topics: [identity-and-access, platforms-and-services]
see_also: [macos, secrets-manager]
summary: "The built-in encrypted store where Apple devices keep passwords, keys and certificates."
match: ['\bkeychains?\b']
sources:
  - title: "Keychain data protection"
    url: "https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web"
    publisher: "Apple"
    primary: true
  - title: "What is Keychain Access on Mac?"
    url: "https://support.apple.com/guide/keychain-access/what-is-keychain-access-kyca1083/mac"
    publisher: "Apple"
  - title: "Keychain (software)"
    url: "https://en.wikipedia.org/wiki/Keychain_(software)"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1555.001", topic: "Credentials from Password Stores: Keychain",
     url: "https://attack.mitre.org/techniques/T1555/001/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
The keychain is the password store built into {{< term "macos" >}} and Apple's other systems. It keeps passwords, keys and certificates {{< term "encryption" "encrypted" >}} on disk and hands each one only to the apps allowed to read it, so programs don't need to keep secrets in plain text files. Because it holds so many credentials in one place, attackers who get onto a Mac often try to read it.
