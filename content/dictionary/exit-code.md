---
title: "Exit code"
term_kind: concept
topics: [programming-and-ai]
see_also: [shell]
summary: "The number a program hands back when it finishes: zero for success, anything else for failure."
match: ['\bexit (?:codes?|status(?:es)?)\b', '\bexits? with an error\b']
sources:
  - title: "Shell Command Language: Exit Status for Commands (POSIX.1-2024)"
    url: "https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html"
    publisher: "The Open Group / IEEE"
    primary: true
  - title: "Exit status"
    url: "https://en.wikipedia.org/wiki/Exit_status"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
When a command-line program finishes, it hands back a small number called its exit code, or exit status. Zero means it succeeded and anything else means some kind of failure, so scripts in a {{< term "shell" >}} and automated checks can tell whether a step worked without reading its output. A check that "exits with an error" is using this number to say that something it tested failed.
