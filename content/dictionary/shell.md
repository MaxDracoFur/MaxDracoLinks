---
title: "Shell (command line)"
term_kind: concept
topics: [programming-and-ai, platforms-and-services]
see_also: [zsh, environment-variable, exit-code]
summary: "The program that reads typed commands and runs them; bash and zsh are common ones."
match: ['\bshells?\b', '\bbash\b']
sources:
  - title: "Shell Command Language (POSIX.1-2024)"
    url: "https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html"
    publisher: "The Open Group / IEEE"
    primary: true
  - title: "GNU Bash Reference Manual"
    url: "https://www.gnu.org/software/bash/manual/bash.html"
    publisher: "GNU Project"
  - title: "Unix shell"
    url: "https://en.wikipedia.org/wiki/Unix_shell"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1059.004", topic: "Command and Scripting Interpreter: Unix Shell",
     url: "https://attack.mitre.org/techniques/T1059/004/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A shell is the program behind a command-line window: you type a command, it runs it and shows the result. bash is the long-standing default on {{< term "linux" >}}, and {{< term "zsh" >}} is the default on a Mac. Shells look alike but differ in small rules, so the same line can behave differently in two of them. Whoever gets a shell on a machine can usually do anything that machine's user account can.
