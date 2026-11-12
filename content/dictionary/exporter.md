---
title: "Exporter (metrics exporter)"
term_kind: concept
topics: [logging-and-monitoring]
see_also: [prometheus, metrics, polling]
summary: "A small program that gathers numbers from a system and publishes them for monitoring to collect."
match: ['\bexporters?\b', '\bscrape[sd]?\b']
sources:
  - title: "Exporters and integrations"
    url: "https://prometheus.io/docs/instrumenting/exporters/"
    publisher: "Prometheus"
    primary: true
  - title: "Writing exporters"
    url: "https://prometheus.io/docs/instrumenting/writing_exporters/"
    publisher: "Prometheus"
  - title: "Glossary"
    url: "https://prometheus.io/docs/introduction/glossary/"
    publisher: "Prometheus"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
In {{< term "prometheus" >}}-style monitoring, an exporter is a small program that gathers {{< term "metrics" "measurements" >}} from something that can't report them itself, such as a {{< term "router" >}} or a cloud account, and publishes them on a web page in a format the monitoring system reads. The monitoring system fetches that page on a fixed timer; each fetch is called a scrape, and whatever is being scraped is a target. The separate parts of an exporter that each gather one kind of data are often called collectors.
