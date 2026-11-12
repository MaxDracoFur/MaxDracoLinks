---
title: "Environment variable"
term_kind: concept
topics: [programming-and-ai]
see_also: [secrets-manager, shell]
summary: "A named setting a running program inherits from whatever started it."
match: ['\benvironment variables?\b', '\bfrom the environment\b', '\benv vars?\b']
sources:
  - title: "Environment Variables (POSIX.1-2024, Base Definitions, Chapter 8)"
    url: "https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap08.html"
    publisher: "The Open Group / IEEE"
    primary: true
  - title: "Environment variable"
    url: "https://en.wikipedia.org/wiki/Environment_variable"
    publisher: "Wikipedia"
classification:
  - {standard: cwe, clause: "CWE-526", topic: "Cleartext Storage of Sensitive Information in an Environment Variable",
     url: "https://cwe.mitre.org/data/definitions/526.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
An environment variable is a named setting that a running program inherits from whatever started it, such as the user's home folder or the language to use. Programs often receive passwords and {{< term "api-key" "API keys" >}} this way, so the secrets are not written into the {{< term "source-code" "source code" >}}. Changing one usually means restarting the program, and anything that can read the program's environment, or a crash report that dumps it, can see the secrets too.
