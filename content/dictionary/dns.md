---
title: "DNS"
term_kind: protocol
topics: [networking]
summary: "The internet's system for turning names like example.com into IP addresses."
match: ['\bDNS\b']
sources:
  - title: "RFC 1034: Domain Names, Concepts and Facilities"
    url: "https://www.rfc-editor.org/rfc/rfc1034"
    publisher: "IETF"
    primary: true
  - title: "Domain Name System"
    url: "https://en.wikipedia.org/wiki/Domain_Name_System"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1071.004", topic: "Application Layer Protocol: DNS",
     url: "https://attack.mitre.org/techniques/T1071/004/"}
  - {standard: attack, clause: "T1584.002", topic: "Compromise Infrastructure: DNS Server",
     url: "https://attack.mitre.org/techniques/T1584/002/"}
  - {standard: capec, clause: "CAPEC-142", topic: "DNS Cache Poisoning",
     url: "https://capec.mitre.org/data/definitions/142.html"}
  - {standard: sp800-53, clause: "SC-20", topic: "Secure Name/Address Resolution Service (Authoritative Source)",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-20"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: true
---
DNS (the Domain Name System) is how a computer finds out which numeric address belongs to a name such as example.com. Your device asks a resolver, the resolver asks the servers responsible for that name, and the answer is cached for a while. Almost every connection starts with a DNS lookup, which makes DNS a useful place both to block things and to watch what a network is doing.
