---
title: "Metrics"
term_kind: concept
topics: [logging-and-monitoring]
see_also: [prometheus, exporter, grafana]
summary: "Numbers a system records over time, such as request counts or temperature, used to watch its health."
match: ['\bmetrics\b']
sources:
  - title: "Metrics"
    url: "https://opentelemetry.io/docs/concepts/signals/metrics/"
    publisher: "OpenTelemetry"
    primary: true
  - title: "Data model"
    url: "https://prometheus.io/docs/concepts/data_model/"
    publisher: "Prometheus"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Metrics are measurements a system takes of itself at regular intervals: how many requests it served, how many failed, how full a disk is, how hot a chip is running. Each one is stored as a series of numbers over time, which makes them cheap to keep and easy to graph and alert on. A monitoring tool such as {{< term "prometheus" >}} collects them; gaps in the series can be as telling as the values.
