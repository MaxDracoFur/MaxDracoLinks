---
title: "Paging (on-call alert)"
term_kind: concept
topics: [logging-and-monitoring, security-operations]
see_also: [metrics, runbook, false-positive]
summary: "An urgent alert that interrupts an on-call person, by phone, text or app, so they act right away."
match: ['\bpaging\b', '\b(?:could|would) page\b', '\bnever pages\b']
sources:
  - title: "Being On-Call (Site Reliability Engineering)"
    url: "https://sre.google/sre-book/being-on-call/"
    publisher: "Google"
    primary: true
  - title: "On-call"
    url: "https://en.wikipedia.org/wiki/On-call"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
To page someone is to send an alert that interrupts them, on a phone or pager, because something needs a person right now. The name comes from the pagers that on-call staff used to carry. Monitoring is usually tuned so that only urgent, real problems page; everything else goes to email or a ticket, because people who are woken by {{< term "false-positive" "false alarms" >}} soon start ignoring alerts.
