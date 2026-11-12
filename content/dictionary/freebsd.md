---
title: "FreeBSD"
term_kind: tool
topics: [platforms-and-services]
summary: "Free, open-source Unix-like operating system descended from BSD Unix."
match: ['\bFreeBSD\b']
sources:
  - title: "The FreeBSD Project"
    url: "https://www.freebsd.org/"
    publisher: "The FreeBSD Project"
    primary: true
  - title: "FreeBSD Handbook"
    url: "https://docs.freebsd.org/en/books/handbook/"
    publisher: "The FreeBSD Project"
  - title: "freebsd/freebsd-src source code"
    url: "https://github.com/freebsd/freebsd-src"
    publisher: "GitHub"
classification:
  - {standard: cpe, clause: "cpe:2.3:o:freebsd:freebsd", topic: "the name NVD files FreeBSD vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Ao%3Afreebsd%3Afreebsd"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-12). Sources: primary/official first. CPE checked against the NVD CPE API
# on 2026-11-11 (cpeMatchString returned matches).
draft: false
---
FreeBSD is a free, {{< term "open-source" "open-source" >}} operating system descended from the Berkeley Software Distribution (BSD), the University of California's version of Unix. The {{< term "kernel" "kernel" >}}, {{< term "driver" "drivers" >}} and basic tools are developed together as one project, which is part of why it is popular for servers, storage and network appliances. {{< term "firewall" "Firewalls" >}} such as {{< term "pfsense" >}} and {{< term "opnsense" >}} are built on it.
