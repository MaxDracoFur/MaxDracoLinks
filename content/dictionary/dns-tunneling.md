---
title: "DNS tunneling"
term_kind: concept
topics: [security-operations, networking]
see_also: [dns, exfiltration, tunnel]
summary: "Hiding other data inside DNS lookups to slip it past a network that blocks everything else."
match: ['\bDNS tunnel(?:s|ing|ling)?\b', '\bsmuggled through\b']
sources:
  - title: "Application Layer Protocol: DNS (T1071.004)"
    url: "https://attack.mitre.org/techniques/T1071/004/"
    publisher: "MITRE ATT&CK"
    primary: true
  - title: "Protocol Tunneling (T1572)"
    url: "https://attack.mitre.org/techniques/T1572/"
    publisher: "MITRE ATT&CK"
  - title: "Tunneling protocol"
    url: "https://en.wikipedia.org/wiki/Tunneling_protocol"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1071.004", topic: "Application Layer Protocol: DNS",
     url: "https://attack.mitre.org/techniques/T1071/004/"}
  - {standard: attack, clause: "T1572", topic: "Protocol Tunneling",
     url: "https://attack.mitre.org/techniques/T1572/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
{{< term "dns" "DNS" >}} tunneling hides other data inside name lookups, the requests a device makes to turn a name into an address. Almost every network lets those lookups through, even one that blocks everything else, so a program can encode data in made-up names and in the answers that come back. It is slow, but it works, which is why attackers use it to sneak data out of a network or to control machines they have broken into.
