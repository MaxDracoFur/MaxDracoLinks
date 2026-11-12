---
title: "Allowlist"
term_kind: concept
topics: [identity-and-access, security-operations]
see_also: [deny-by-default, firewall, least-privilege]
summary: "A list of the things that are explicitly permitted; everything not on it is refused."
match: ['\ballow-?lists?(?:ed|ing)?\b', '\bwhitelists?(?:ed|ing)?\b']
sources:
  - title: "allowlist (Glossary)"
    url: "https://csrc.nist.gov/glossary/term/allowlist"
    publisher: "NIST CSRC"
    primary: true
  - title: "Whitelist"
    url: "https://en.wikipedia.org/wiki/Whitelist"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "SC-7(5)", topic: "Boundary Protection: Deny by Default, Allow by Exception",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-07(05)"}
  - {standard: sp800-53, clause: "CM-7(5)", topic: "Least Functionality: Authorized Software, Allow by Exception",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=CM-07(05)"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
An allowlist (older name: whitelist) is a list of exactly what is permitted: which addresses may connect, which programs may run, which actions a user or program may take. Anything not on the list is refused. It is safer than a blocklist, which tries to name everything bad, because something new or unexpected is turned away by default. The weak point is the list itself: one wrong entry quietly lets something through.
