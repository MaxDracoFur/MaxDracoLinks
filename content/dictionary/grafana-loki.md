---
title: "Grafana Loki"
term_kind: tool
summary: "A log storage and search system from Grafana Labs that indexes labels, not the full text."
match: ['\bLoki\b']
topics: [logging-and-monitoring]
see_also: [grafana-alloy, promtail]
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
classification:
  - {standard: cpe, clause: "cpe:2.3:a:grafana:loki", topic: "the name NVD files Loki vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Agrafana%3Aloki"}
  - {standard: sp800-53, clause: "AU-11", topic: "Audit Record Retention",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AU-11"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary); Max approved it 2026-11-11.
# Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Loki stores logs and lets you search them. Instead of indexing every word of every line, it indexes a few labels per stream (which host, which app) and scans the text only when you search. That keeps it cheap to run. It is {{< term "open-source" "open source" >}}, made by {{< term "grafana" "Grafana Labs" >}}, and is usually queried from Grafana with a language called LogQL.
