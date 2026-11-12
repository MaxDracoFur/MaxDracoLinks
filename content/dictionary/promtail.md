---
title: "Promtail"
term_kind: tool
summary: "Grafana Labs' older log shipper for Loki, now replaced by Grafana Alloy."
match: ['\bPromtail\b']
topics: [logging-and-monitoring]
see_also: [grafana-alloy]
sources:
  - title: "Promtail documentation"
    url: "https://grafana.com/docs/loki/latest/send-data/promtail/"
    publisher: "Grafana Labs"
    primary: true
  - title: "Migrate from Promtail to Grafana Alloy"
    url: "https://grafana.com/docs/alloy/latest/set-up/migrate/from-promtail/"
    publisher: "Grafana Labs"
classification:
  - {standard: sp800-53, clause: "AU-9(2)", topic: "Store on Separate Physical Systems or Components",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AU-09(02)"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary); Max approved it 2026-11-11.
# Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Promtail was the agent that read log files (or received {{< term "syslog" >}}), attached labels and pushed the lines to {{< term "grafana-loki" "Loki" >}}. Grafana Labs has deprecated it in favour of {{< term "grafana-alloy" >}}, which does the same job and more; its documentation includes a migration guide.
