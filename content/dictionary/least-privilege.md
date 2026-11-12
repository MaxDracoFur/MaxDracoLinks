---
title: "Least privilege"
term_kind: concept
topics: [identity-and-access]
see_also: [authentication, machine-identity, allowlist]
summary: "The rule that every person or program should get only the access it needs for its job, and no more."
match: ['\bleast[- ]privileged?\b']
sources:
  - title: "Least privilege (glossary)"
    url: "https://csrc.nist.gov/glossary/term/least_privilege"
    publisher: "NIST"
    primary: true
  - title: "Principle of least privilege"
    url: "https://en.wikipedia.org/wiki/Principle_of_least_privilege"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "AC-6", topic: "Least Privilege",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AC-06"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Least privilege means giving each user, program or key only the permissions its task requires: a tool that only reads data gets read access, not the power to change or delete it. If that account is stolen or misbehaves, the damage is limited to that small set of permissions. The cost is more care up front, and a narrowly scoped account will sometimes be refused something it turns out to need.
