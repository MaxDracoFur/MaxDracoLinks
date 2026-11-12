---
title: "pfSense"
term_kind: tool
topics: [networking, security-operations]
summary: "Firewall and router software built on FreeBSD, made by Netgate."
match: ['\bpfSense\b']
sources:
  - title: "pfSense"
    url: "https://www.pfsense.org/"
    publisher: "Netgate"
    primary: true
  - title: "pfSense documentation"
    url: "https://docs.netgate.com/pfsense/en/latest/"
    publisher: "Netgate"
  - title: "pfsense/pfsense source code"
    url: "https://github.com/pfsense/pfsense"
    publisher: "GitHub"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:netgate:pfsense", topic: "the name NVD files pfSense vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Anetgate%3Apfsense"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-12). Sources: primary/official first. CPE checked against the NVD CPE API
# on 2026-11-11 (cpeMatchString returned matches).
draft: false
---
pfSense is firewall and router software that runs on {{< term "freebsd" >}} and is managed from a web interface. It dates from 2004 and is developed by Netgate, which offers a free Community Edition and a commercial pfSense Plus. In 2015 a group of developers forked it to create {{< term "opnsense" >}}.
