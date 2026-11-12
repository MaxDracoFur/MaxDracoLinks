---
title: "Prometheus"
term_kind: tool
topics: [logging-and-monitoring]
summary: "Open-source monitoring system that collects numbers over time and raises alerts."
match: ['\bPrometheus\b']
sources:
  - title: "Prometheus"
    url: "https://prometheus.io/"
    publisher: "Prometheus Authors"
    primary: true
  - title: "Prometheus overview"
    url: "https://prometheus.io/docs/introduction/overview/"
    publisher: "Prometheus Authors"
  - title: "prometheus/prometheus source code"
    url: "https://github.com/prometheus/prometheus"
    publisher: "GitHub"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:prometheus:prometheus", topic: "the name NVD files Prometheus vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Aprometheus%3Aprometheus"}
  - {standard: sp800-53, clause: "SI-4", topic: "System Monitoring",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SI-04"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-12). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Prometheus is a free, {{< term "open-source" "open-source" >}} monitoring system. Every few seconds it visits a list of targets and reads their {{< term "metrics" "metrics" >}}, numbers such as CPU use, request counts or temperature, then stores them as time series. You query them with a language called PromQL, draw them as graphs, and write alert rules that fire when a value goes wrong. Small programs called {{< term "exporter" "exporters" >}} translate other systems' numbers into Prometheus's format.
