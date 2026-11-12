---
title: "Runbook"
term_kind: concept
topics: [security-operations]
see_also: [incident-report, paging, maintenance-window]
summary: "A written, step-by-step guide for a routine operation or for responding to a known problem."
match: ['\brunbooks?\b']
sources:
  - title: "On-Call (The Site Reliability Workbook)"
    url: "https://sre.google/workbook/on-call/"
    publisher: "Google"
    primary: true
  - title: "Runbook"
    url: "https://en.wikipedia.org/wiki/Runbook"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A runbook (also called a playbook) is a written set of steps for doing a routine operation or for handling a known problem: what to check, what to run, and in what order. It lets whoever is on duty act correctly at 3 a.m. without having to work everything out from scratch. A runbook that has drifted out of date with the real system can be worse than none, because people trust it.
