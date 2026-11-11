---
title: "Grafana Loki"
term_kind: tool
summary: "A log storage and search system from Grafana Labs that indexes labels, not the full text."
match: ['\bLoki\b']
sources:
  - title: "Grafana Loki"
    url: "https://grafana.com/oss/loki/"
    publisher: "Grafana Labs"
    primary: true
  - title: "Loki documentation"
    url: "https://grafana.com/docs/loki/latest/"
    publisher: "Grafana Labs"
  - title: "grafana/loki source code"
    url: "https://github.com/grafana/loki"
    publisher: "GitHub"
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first; health is checked daily.
draft: true
---
Loki stores logs and lets you search them. Instead of indexing every word of every line, it indexes a few labels per stream (which host, which app) and scans the text only when you search. That keeps it cheap to run. It is open source, made by Grafana Labs, and is usually queried from Grafana with a language called LogQL.

## Why it's on this site

It's where my homelab's logs end up, including the firewall's syslog.
