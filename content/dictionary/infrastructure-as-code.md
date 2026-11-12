---
title: "Infrastructure as code"
term_kind: concept
topics: [programming-and-ai, platforms-and-services]
see_also: [configuration-drift, git, deployment]
summary: "Managing servers and networks by writing their settings down in files that a tool applies, instead of setting each one up by hand."
match: ['\binfrastructure[- ]as[- ]code\b', '\bIaC\b']
sources:
  - title: "Infrastructure as code (glossary)"
    url: "https://csrc.nist.gov/glossary/term/infrastructure_as_code"
    publisher: "NIST CSRC"
    primary: true
  - title: "Infrastructure as code"
    url: "https://en.wikipedia.org/wiki/Infrastructure_as_code"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "CM-2", topic: "Baseline Configuration",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=CM-02"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Infrastructure as code means describing servers, networks and services in text files that a tool reads to build or change them, rather than setting each one up by hand. The files can be kept in {{< term "git" >}}, so every change is recorded, can be reviewed and can be undone, and a system can be rebuilt the same way twice. The catch is that a setting changed by hand makes the real system {{< term "configuration-drift" "drift" >}} away from what the files say.
