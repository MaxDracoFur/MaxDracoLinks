---
title: "syslog"
term_kind: protocol
summary: "The standard way computers and network devices send log messages to a log server."
match: ['\bsyslog\b']
topics: [logging-and-monitoring, networking]
see_also: [grafana-alloy, siem]
sources:
  - title: "RFC 5424: The Syslog Protocol"
    url: "https://www.rfc-editor.org/rfc/rfc5424"
    publisher: "IETF"
    primary: true
  - title: "RFC 5426: Transmission of Syslog Messages over UDP"
    url: "https://www.rfc-editor.org/rfc/rfc5426"
    publisher: "IETF"
  - title: "RFC 5425: TLS Transport Mapping for Syslog"
    url: "https://www.rfc-editor.org/rfc/rfc5425"
    publisher: "IETF"
classification:
  - {standard: attack, clause: "T1685.006", topic: "Clear Linux or Mac System Logs",
     url: "https://attack.mitre.org/techniques/T1685/006/"}
  - {standard: cwe, clause: "CWE-117", topic: "Improper Output Neutralization for Logs",
     url: "https://cwe.mitre.org/data/definitions/117.html"}
  - {standard: sp800-53, clause: "AU-9", topic: "Protection of Audit Information",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AU-09"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary); Max approved it 2026-11-11.
# Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK 20.1 STIX, CWE 5.0 and CAPEC XML, NIST's 800-53 5.2.0 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Syslog is a simple format and protocol for log messages: each message has a timestamp, the host that sent it, how serious it is, and the text. It started on BSD Unix in the 1980s and is now an IETF standard. Devices can keep syslog locally or send it over the network to a central log server, classically over {{< term "udp" >}} port 514, or over {{< term "tls" >}} when the messages need protecting.
