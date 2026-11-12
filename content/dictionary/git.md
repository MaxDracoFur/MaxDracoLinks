---
title: "Git"
term_kind: tool
topics: [programming-and-ai]
see_also: [github, source-code]
summary: "Free software that records every change to a set of files, used to keep the history of most software projects."
match: ['\bgit\b', '\bmain branch\b', '\bversion control\b', '\b(?:public|private|git) repos?\b', '\b(?:public|private|git) repositor(?:y|ies)\b']
sources:
  - title: "About Git"
    url: "https://git-scm.com/about"
    publisher: "Git project"
    primary: true
  - title: "Git"
    url: "https://en.wikipedia.org/wiki/Git"
    publisher: "Wikipedia"
classification:
  - {standard: cwe, clause: "CWE-527", topic: "Exposure of Version-Control Repository to an Unauthorized Control Sphere",
     url: "https://cwe.mitre.org/data/definitions/527.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Git is a free version control system: it keeps the full history of a project's files, so you can see who changed what and when, and go back to any earlier version. A project's files and their history together are a repository, or repo. Work happens on branches, and the main branch usually holds the current agreed version. Sites like {{< term "github" >}} host repositories online. Because the history keeps everything, a password or key committed to a public repository stays readable even after it is deleted from the latest version.
