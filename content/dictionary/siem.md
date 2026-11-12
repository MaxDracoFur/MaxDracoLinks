---
title: "SIEM"
term_kind: concept
summary: "Security information and event management: a system that collects logs from many sources so security events can be searched and alerted on."
match: ['\bSIEMs?\b']
topics: [security-operations, logging-and-monitoring]
see_also: [syslog, grafana-loki]
sources:
  - title: "NIST glossary: security information and event management (SIEM) tool"
    url: "https://csrc.nist.gov/glossary/term/security_information_and_event_management_tool"
    publisher: "NIST"
    primary: true
  - title: "Security information and event management"
    url: "https://en.wikipedia.org/wiki/Security_information_and_event_management"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "SI-4", topic: "System Monitoring",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SI-04"}
  - {standard: sp800-53, clause: "AU-6(3)", topic: "Correlate Audit Record Repositories",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AU-06(03)"}
  - {standard: cwe, clause: "CWE-778", topic: "Insufficient Logging",
     url: "https://cwe.mitre.org/data/definitions/778.html"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary); Max approved it 2026-11-11.
# Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
A SIEM gathers logs and events from servers, network devices and applications into one place, then lets a security team search them, correlate them and get alerts.
