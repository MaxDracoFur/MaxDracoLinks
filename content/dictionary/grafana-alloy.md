---
title: "Grafana Alloy"
term_kind: tool
summary: "Grafana Labs' collector that gathers logs, metrics and traces and sends them to storage like Loki."
match: ['\bAlloy\b']
sources:
  - title: "Grafana Alloy documentation"
    url: "https://grafana.com/docs/alloy/latest/"
    publisher: "Grafana Labs"
    primary: true
  - title: "grafana/alloy source code"
    url: "https://github.com/grafana/alloy"
    publisher: "GitHub"
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first; health is checked daily.
draft: true
---
Alloy is an open-source telemetry collector from Grafana Labs. It receives or reads logs, metrics and traces, can change them on the way (for example, adding labels or dropping noisy lines), and forwards them to storage such as Loki or Prometheus. It is a distribution of the OpenTelemetry Collector and replaces Grafana's older agents, including Promtail.

## Why it's on this site

It's the program that receives my network's syslog and hands it to Loki, labelling each line on the way.
