---
title: "Grafana Alloy"
term_kind: tool
summary: "Grafana Labs' collector that gathers logs, metrics and traces and sends them to storage like Loki."
match: ['\bAlloy\b']
topics: [logging-and-monitoring]
see_also: [promtail, grafana-loki]
sources:
  - title: "Grafana Alloy documentation"
    url: "https://grafana.com/docs/alloy/latest/"
    publisher: "Grafana Labs"
    primary: true
  - title: "grafana/alloy source code"
    url: "https://github.com/grafana/alloy"
    publisher: "GitHub"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:grafana:alloy", topic: "the name NVD files Alloy vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Agrafana%3Aalloy"}
  - {standard: sp800-53, clause: "AU-9(2)", topic: "Store on Separate Physical Systems or Components",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AU-09(02)"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary); Max approved it 2026-11-11.
# Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Alloy is an open-source telemetry collector from Grafana Labs. It receives or reads logs, metrics and traces, can change them on the way (for example, adding labels or dropping noisy lines), and forwards them to storage such as Loki or Prometheus. It is a distribution of the OpenTelemetry Collector and replaces Grafana's older agents, including Promtail.
