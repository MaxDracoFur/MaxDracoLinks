---
title: "HTTP"
term_kind: protocol
topics: [networking]
summary: "The protocol web browsers and servers use to request and send pages and data."
match: ['\bHTTPS?\b']
sources:
  - title: "RFC 9110: HTTP Semantics"
    url: "https://www.rfc-editor.org/rfc/rfc9110"
    publisher: "IETF"
    primary: true
  - title: "HTTP"
    url: "https://developer.mozilla.org/en-US/docs/Web/HTTP"
    publisher: "MDN Web Docs"
classification:
  - {standard: attack, clause: "T1071.001", topic: "Application Layer Protocol: Web Protocols",
     url: "https://attack.mitre.org/techniques/T1071/001/"}
  - {standard: cwe, clause: "CWE-319", topic: "Cleartext Transmission of Sensitive Information",
     url: "https://cwe.mitre.org/data/definitions/319.html"}
  - {standard: sp800-53, clause: "SC-8", topic: "Transmission Confidentiality and Integrity",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-08"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-12). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
HTTP (Hypertext Transfer Protocol) is how a browser or program asks a web server for something and gets an answer back. Each request names a method (GET to fetch, POST to send), a path, and headers; each response carries a {{< term "http-status-code" "status code" >}} such as 200 for OK or 404 for not found. Plain HTTP is readable by anyone on the path. HTTPS is the same protocol carried inside {{< term "tls" >}}, so it is {{< term "encryption" "encrypted" >}}.
