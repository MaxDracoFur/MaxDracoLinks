---
title: "Data retention"
term_kind: concept
topics: [logging-and-monitoring, security-operations]
see_also: [redaction, grafana-loki]
summary: "How long stored data, such as logs, is kept before it is deleted."
match: ['\bretention\b', '\bno expiry\b']
sources:
  - title: "retention period (glossary)"
    url: "https://csrc.nist.gov/glossary/term/retention_period"
    publisher: "NIST CSRC"
    primary: true
  - title: "Data retention"
    url: "https://en.wikipedia.org/wiki/Data_retention"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Data retention is the rule for how long stored data is kept before it is deleted. Log systems, mailboxes and backups usually have a retention setting, such as "keep 90 days". With no limit, everything is kept forever, so a password or key that once landed in a log stays readable for as long as the storage exists.
