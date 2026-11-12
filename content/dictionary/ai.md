---
title: "AI"
term_kind: concept
topics: [programming-and-ai]
summary: "Artificial intelligence: software that performs tasks usually thought to need human judgement."
match: ['\bAI\b']
sources:
  - title: "AI Risk Management Framework"
    url: "https://www.nist.gov/itl/ai-risk-management-framework"
    publisher: "NIST"
    primary: true
  - title: "Artificial intelligence"
    url: "https://en.wikipedia.org/wiki/Artificial_intelligence"
    publisher: "Wikipedia"
classification:
  - {standard: atlas, clause: "AML.T0051", topic: "LLM Prompt Injection",
     url: "https://atlas.mitre.org/techniques/AML.T0051"}
  - {standard: atlas, clause: "AML.T0054", topic: "LLM Jailbreak",
     url: "https://atlas.mitre.org/techniques/AML.T0054"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: true
---
AI (artificial intelligence) is a broad name for software that does things such as recognising images, understanding text or making decisions, usually by learning patterns from large amounts of data rather than following hand-written rules. Today the term most often means large language models, which generate text and can be connected to tools to carry out tasks. Because they act on instructions written in plain language, they can also be tricked by instructions hidden in the data they read.
