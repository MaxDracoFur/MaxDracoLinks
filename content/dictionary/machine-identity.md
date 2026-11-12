---
title: "Machine identity"
term_kind: concept
topics: [identity-and-access]
see_also: [least-privilege, secrets-manager, authentication]
summary: "An account that belongs to a program or service rather than a person, with its own credentials and permissions."
match: ['\bmachine identit(?:y|ies)\b']
sources:
  - title: "Machine identities"
    url: "https://infisical.com/docs/documentation/platform/identities/machine-identities"
    publisher: "Infisical"
    primary: true
  - title: "Non-person entity (glossary)"
    url: "https://csrc.nist.gov/glossary/term/non_person_entity"
    publisher: "NIST"
classification:
  - {standard: sp800-53, clause: "IA-9", topic: "Service Identification and Authentication",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=IA-09"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A machine identity is an account for software: a script, a server or an automated agent signs in as itself instead of borrowing a person's login. It gets its own credentials and only the permissions its job needs, so its access can be limited, logged and revoked separately from anyone's personal account. If its credentials leak, only that one identity has to be cut off and replaced.
