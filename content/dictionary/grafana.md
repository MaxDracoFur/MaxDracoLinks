---
title: "Grafana"
term_kind: tool
topics: [logging-and-monitoring]
see_also: [grafana-loki, prometheus, metrics]
summary: "Open-source dashboard tool for graphing, exploring and alerting on metrics and logs."
match: ['\bGrafana[.,;:!?)]', '\bGrafana (?:dashboards?|Labs|panels?|Cloud)\b']
sources:
  - title: "Grafana documentation"
    url: "https://grafana.com/docs/grafana/latest/"
    publisher: "Grafana Labs"
    primary: true
  - title: "Grafana"
    url: "https://en.wikipedia.org/wiki/Grafana"
    publisher: "Wikipedia"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:grafana:grafana", topic: "the name NVD files Grafana vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Agrafana%3Agrafana"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Grafana is a tool for building dashboards: web pages of graphs and tables drawn live from data sources such as {{< term "prometheus" >}} for {{< term "metrics" >}} and {{< term "grafana-loki" "Loki" >}} for logs. It can also send an alert when a value crosses a line someone has set. The company that makes it uses the same name for its other products, such as Loki and {{< term "grafana-alloy" "Alloy" >}}, so "Grafana" on its own usually means the dashboard tool.
