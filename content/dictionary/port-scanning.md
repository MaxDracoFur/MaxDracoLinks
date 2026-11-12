---
title: "Port scanning"
term_kind: tool
topics: [security-operations, networking]
see_also: [attack-surface, firewall, tarpit]
summary: "Knocking on many ports of a machine in turn to find out which services are listening."
match: ['\bport[- ]scan(?:s|ned|ning|ner|ners)?\b', '\binternet scanners?\b', '\bfound by a scanner\b']
sources:
  - title: "NIST CSRC Glossary: port scanning"
    url: "https://csrc.nist.gov/glossary/term/port_scanning"
    publisher: "NIST"
    primary: true
  - title: "Port Scanning Basics (Nmap Reference Guide)"
    url: "https://nmap.org/book/man-port-scanning-basics.html"
    publisher: "Nmap"
  - title: "Port scanner"
    url: "https://en.wikipedia.org/wiki/Port_scanner"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1595", topic: "Active Scanning",
     url: "https://attack.mitre.org/techniques/T1595/"}
  - {standard: attack, clause: "T1046", topic: "Network Service Discovery",
     url: "https://attack.mitre.org/techniques/T1046/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A port scanner contacts an address on many {{< term "network-port" "ports" >}}, one after another, to see which ones answer, and so which services are running there. Administrators use it to check what they expose; attackers use it to find something to break into. Automated scanners sweep the whole internet all the time, so a service that answers on a {{< term "ip-address" "public address" >}} will be found.
