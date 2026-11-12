---
title: "Cloudflare"
term_kind: organisation
topics: [platforms-and-services, networking]
summary: "Company whose network sits in front of websites to speed them up and protect them."
match: ['\bCloudflare\b']
sources:
  - title: "Cloudflare"
    url: "https://www.cloudflare.com/"
    publisher: "Cloudflare, Inc."
    primary: true
  - title: "Cloudflare"
    url: "https://en.wikipedia.org/wiki/Cloudflare"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1090", topic: "Proxy",
     url: "https://attack.mitre.org/techniques/T1090/"}
  - {standard: attack, clause: "T1102", topic: "Web Service",
     url: "https://attack.mitre.org/techniques/T1102/"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Cloudflare is a US company that runs a large global network in front of other people's websites. Visitors connect to Cloudflare, which serves cached copies, filters attacks and forwards the rest to the real server. It also offers {{< term "dns" >}}, hosting for static sites, and tunnels that publish a service without opening a port on your own firewall. A large share of websites use it.
