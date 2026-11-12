---
title: "Python"
term_kind: tool
topics: [programming-and-ai]
summary: "Popular general-purpose programming language known for readable code."
match: ['\bPython\b']
sources:
  - title: "Python"
    url: "https://www.python.org/"
    publisher: "Python Software Foundation"
    primary: true
  - title: "Python documentation"
    url: "https://docs.python.org/3/"
    publisher: "Python Software Foundation"
classification:
  - {standard: attack, clause: "T1059.006", topic: "Command and Scripting Interpreter: Python",
     url: "https://attack.mitre.org/techniques/T1059/006/"}
  - {standard: cpe, clause: "cpe:2.3:a:python:python", topic: "the name NVD files Python vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Apython%3Apython"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Python is a free, open-source programming language designed to be easy to read. It comes with a large standard library and is widely used for scripts, automation, web services, data analysis and security tooling. Programs run through an interpreter rather than being compiled first, so a script is just a text file you can read and change.
