---
title: "OPNsense"
term_kind: tool
summary: "Open-source firewall and router software, built on FreeBSD."
match: ['\bOPNsense\b']
topics: [networking, security-operations]
sources:
  - title: "OPNsense"
    url: "https://opnsense.org/"
    publisher: "Deciso B.V."
    primary: true
  - title: "OPNsense documentation"
    url: "https://docs.opnsense.org/"
    publisher: "Deciso B.V."
  - title: "opnsense/core source code"
    url: "https://github.com/opnsense/core"
    publisher: "GitHub"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:opnsense:opnsense", topic: "the name NVD files OPNsense vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Aopnsense%3Aopnsense"}
  - {standard: attack, clause: "T1686.002", topic: "Network Device Firewall: attackers disabling or changing firewall rules",
     url: "https://attack.mitre.org/techniques/T1686/002/"}
  - {standard: attack, clause: "M1037", topic: "Filter Network Traffic: the defence a firewall provides",
     url: "https://attack.mitre.org/mitigations/M1037/"}
  - {standard: sp800-53, clause: "SC-7", topic: "Boundary Protection",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-07"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary); Max approved it 2026-11-11.
# Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
OPNsense is free, {{< term "open-source" "open-source" >}} software that turns a computer into a {{< term "firewall" "firewall" >}} and {{< term "router" "router" >}}. It runs on {{< term "freebsd" >}} and is managed from a web interface, with a REST {{< term "api" >}} for scripts that {{< term "authentication" "authenticates" >}} each call with an {{< term "api-key" "API key" >}} and secret. It can send its logs to a central server over {{< term "syslog" >}}. It started in 2015 as a fork of {{< term "pfsense" >}} and is developed by Deciso, a company in the Netherlands.
