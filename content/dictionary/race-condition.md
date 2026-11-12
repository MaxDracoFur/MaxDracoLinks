---
title: "Race condition"
term_kind: concept
topics: [programming-and-ai]
see_also: [polling, kernel]
summary: "A bug where the outcome depends on which of two things happens first."
match: ['\brace conditions?\b', '\bknown race\b']
sources:
  - title: "CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')"
    url: "https://cwe.mitre.org/data/definitions/362.html"
    publisher: "MITRE"
    primary: true
  - title: "Race condition"
    url: "https://en.wikipedia.org/wiki/Race_condition"
    publisher: "Wikipedia"
classification:
  - {standard: cwe, clause: "CWE-362", topic: "Concurrent Execution using Shared Resource with Improper Synchronization",
     url: "https://cwe.mitre.org/data/definitions/362.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A race condition is a bug where the result depends on which of two things happens first. When two programs, or two parts of one program, use the same thing at the same moment without taking turns, one can act on information the other has just changed. Races are hard to reproduce because they depend on timing, and some can be exploited, for example by slipping a change in between a security check and the action it was guarding.
