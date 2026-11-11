---
title: "Promtail"
term_kind: tool
summary: "Grafana Labs' older log shipper for Loki, now replaced by Grafana Alloy."
match: ['\bPromtail\b']
sources:
  - title: "Promtail documentation"
    url: "https://grafana.com/docs/loki/latest/send-data/promtail/"
    publisher: "Grafana Labs"
    primary: true
  - title: "Migrate from Promtail to Grafana Alloy"
    url: "https://grafana.com/docs/alloy/latest/set-up/migrate/from-promtail/"
    publisher: "Grafana Labs"
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first; health is checked daily.
draft: true
---
Promtail was the agent that read log files (or received syslog), attached labels and pushed the lines to Loki. Grafana Labs has deprecated it in favour of Grafana Alloy, which does the same job and more; its documentation includes a migration guide.

## Why it's on this site

My log pipeline ran on Promtail before I moved it to Alloy, so older posts and configs mention it.
