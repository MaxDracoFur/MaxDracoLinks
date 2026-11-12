---
title: "Sandbox (sandbox escape)"
term_kind: concept
topics: [security-operations, programming-and-ai]
see_also: [least-privilege, deny-by-default, attack-surface]
summary: "A restricted environment that limits what a program can touch; a sandbox escape is a way out of it."
match: ['\bsandbox(?:es|ed|ing)?\b']
sources:
  - title: "sandbox (glossary)"
    url: "https://csrc.nist.gov/glossary/term/sandbox"
    publisher: "NIST CSRC"
    primary: true
  - title: "Sandbox (computer security)"
    url: "https://en.wikipedia.org/wiki/Sandbox_(computer_security)"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "M1048", topic: "Application Isolation and Sandboxing",
     url: "https://attack.mitre.org/mitigations/M1048/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A sandbox is a fenced-off environment that runs a program with restricted access: only certain files, no network, or no way to start other programs. It is used for untrusted code, such as web pages in a browser, phone apps, or an {{< term "ai" "AI" >}} agent. A sandbox escape is a flaw or a forgotten allowance that lets the program reach things outside the fence. A sandbox is only as tight as the things it had to allow for the program to work at all.
