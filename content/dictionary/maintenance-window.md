---
title: "Maintenance window"
term_kind: concept
topics: [security-operations]
see_also: [deployment, runbook]
summary: "A time set aside in advance for changes or repairs that may briefly interrupt a service."
match: ['\bmaintenance windows?\b']
sources:
  - title: "AWS Systems Manager Maintenance Windows"
    url: "https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows.html"
    publisher: "Amazon Web Services"
    primary: true
  - title: "Maintenance window"
    url: "https://en.wikipedia.org/wiki/Maintenance_window"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A maintenance window is an agreed time, usually when few people are using a system, for work that might cause an outage: updates, hardware swaps or risky configuration changes. Scheduling it in advance means people know to expect a disruption and someone is ready to fix things if the change goes wrong. Urgent security fixes sometimes can't wait for the next window.
