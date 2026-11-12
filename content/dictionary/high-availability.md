---
title: "High availability (HA)"
term_kind: concept
topics: [platforms-and-services]
see_also: [single-point-of-failure, cluster, maintenance-window]
summary: "Designing a system so it keeps working when one of its parts fails."
match: ['\bhighly available\b', '\bhigh[- ]availability\b', '\bfail-?overs?\b', '\bsplit[- ]brain\b', '\bfloating address(?:es)?\b']
sources:
  - title: "High availability (glossary)"
    url: "https://csrc.nist.gov/glossary/term/high_availability"
    publisher: "NIST CSRC"
    primary: true
  - title: "High availability"
    url: "https://en.wikipedia.org/wiki/High_availability"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12.
draft: false
---
A highly available system is built to keep running when one of its parts fails, usually by keeping spare machines ready to take over. When one fails, another takes its place (a failover), often by taking over a shared floating address that everyone else connects to. Machines in a group usually vote, and only a side holding a majority carries on, so that two halves cut off from each other can't both act in charge, a fault called split-brain. How available a system is should be stated as a number, such as how many failures it survives, not as a label.
