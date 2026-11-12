---
title: "Deny by default"
term_kind: concept
topics: [security-operations, identity-and-access]
see_also: [allowlist, least-privilege, sandbox]
summary: "A security rule where nothing is allowed unless a rule specifically permits it."
match: ['\bdeny[- ]by[- ]default\b', '\bdefault[- ]deny\b']
sources:
  - title: "Deny by Default (glossary)"
    url: "https://csrc.nist.gov/glossary/term/deny_by_default"
    publisher: "NIST CSRC"
    primary: true
  - title: "SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations"
    url: "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final"
    publisher: "NIST"
  - title: "Whitelist"
    url: "https://en.wikipedia.org/wiki/Whitelist"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "SC-7(5)", topic: "Deny by Default — Allow by Exception",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-07(05)"}
  - {standard: sp800-53, clause: "CM-7(5)", topic: "Authorized Software — Allow-by-exception",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=CM-07(05)"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Deny by default is a security rule of thumb: nothing is allowed unless a rule specifically permits it. A {{< term "firewall" >}} set up this way blocks every connection except the ones on its list, and a {{< term "sandbox" >}} set up this way stops a program touching any file or network it hasn't been granted. The opposite approach, allowing everything and blocking known-bad things, fails whenever someone finds something the block list forgot.
