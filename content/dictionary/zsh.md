---
title: "zsh"
term_kind: tool
topics: [programming-and-ai]
see_also: [shell, macos]
summary: "The Z shell, a Unix command-line shell and the default on macOS."
match: ['\bzsh\b']
sources:
  - title: "Z Shell"
    url: "https://zsh.sourceforge.io/"
    publisher: "The Z Shell project"
    primary: true
  - title: "Z Shell manual: Redirection (Multios)"
    url: "https://zsh.sourceforge.io/Doc/Release/Redirection.html"
    publisher: "The Z Shell project"
  - title: "Z shell"
    url: "https://en.wikipedia.org/wiki/Z_shell"
    publisher: "Wikipedia"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:zsh:zsh", topic: "the name NVD files zsh vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Azsh%3Azsh"}
  - {standard: attack, clause: "T1059.004", topic: "Command and Scripting Interpreter: Unix Shell",
     url: "https://attack.mitre.org/techniques/T1059/004/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
zsh is a {{< term "shell" >}}: the program that reads the commands typed in a terminal and runs them. The name is short for Z shell. It has been the default on {{< term "macos" >}} since 2019 and is largely compatible with bash, but not entirely. Some of its extra features, such as sending one output to several places at once, change what familiar command lines actually do.
