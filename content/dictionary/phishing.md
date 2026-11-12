---
title: "Phishing"
term_kind: concept
topics: [identity-and-access, security-operations]
see_also: [two-factor-authentication, single-sign-on]
summary: "Tricking someone into giving away a password or running something harmful, with a message that pretends to come from someone they trust."
match: ['\bphish(?:es|ed|ing|er|ers)?\b']
sources:
  - title: "NIST CSRC Glossary: phishing"
    url: "https://csrc.nist.gov/glossary/term/phishing"
    publisher: "NIST"
    primary: true
  - title: "Phishing"
    url: "https://en.wikipedia.org/wiki/Phishing"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1566", topic: "Phishing",
     url: "https://attack.mitre.org/techniques/T1566/"}
  - {standard: capec, clause: "CAPEC-98", topic: "Phishing",
     url: "https://capec.mitre.org/data/definitions/98.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Phishing is a message, usually an email or text, dressed up to look as if it comes from a bank, a colleague or a service you use, that tries to get you to type your password into a fake page or open something harmful. A convincing fake sign-in page can capture a password and a one-time {{< term "two-factor-authentication" "two-factor" >}} code as you type them. Phishing-resistant sign-in, such as a passkey or a hardware security key, checks the real website's address itself, so a lookalike site gets nothing it can use.
