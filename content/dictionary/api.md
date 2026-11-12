---
title: "API"
term_kind: concept
topics: [programming-and-ai]
summary: "A defined way for one program to ask another for data or actions."
match: ['\bAPIs?\b']
sources:
  - title: "NIST glossary: application programming interface"
    url: "https://csrc.nist.gov/glossary/term/application_programming_interface"
    publisher: "NIST"
    primary: true
  - title: "API"
    url: "https://developer.mozilla.org/en-US/docs/Glossary/API"
    publisher: "MDN Web Docs"
classification:
  - {standard: cwe, clause: "CWE-306", topic: "Missing Authentication for Critical Functionality",
     url: "https://cwe.mitre.org/data/definitions/306.html"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-12). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
An API (application programming interface) is the set of requests a piece of software accepts from other programs, and the answers it gives back. A web API usually works over {{< term "http" >}}: a script sends a request to an address such as /api/status and gets data back, often as JSON. APIs let programs work together without a person clicking through a screen, so they usually need their own way to check who is calling, such as an {{< term "api-key" >}}.
