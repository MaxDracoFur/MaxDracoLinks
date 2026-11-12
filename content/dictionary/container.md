---
title: "Container and container image"
term_kind: concept
topics: [platforms-and-services]
see_also: [kubernetes, cluster, sandbox]
summary: "A packaged program with everything it needs to run, kept separate from other programs on the same machine."
match: ['\bcontainers?\b', '\bapp images?\b']
sources:
  - title: "SP 800-190, Application Container Security Guide"
    url: "https://csrc.nist.gov/pubs/sp/800/190/final"
    publisher: "NIST"
    primary: true
  - title: "Open Container Initiative"
    url: "https://opencontainers.org/"
    publisher: "Open Container Initiative"
  - title: "Containerization (computing)"
    url: "https://en.wikipedia.org/wiki/Containerization_(computing)"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1611", topic: "Escape to Host",
     url: "https://attack.mitre.org/techniques/T1611/"}
  - {standard: attack, clause: "T1525", topic: "Implant Internal Image",
     url: "https://attack.mitre.org/techniques/T1525/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A container image is a bundle holding a program plus all the files and libraries it needs, built once and copied wherever it should run. A container is that image running: it shares the machine's {{< term "kernel" >}} but sees its own files, network and processes, so programs don't get in each other's way. Containers keep programs apart, but they are a weaker wall than a separate machine, and a flaw can let a program break out to the host.
