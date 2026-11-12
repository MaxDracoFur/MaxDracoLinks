---
title: "Key rotation"
term_kind: concept
topics: [identity-and-access, cryptography]
see_also: [secrets-manager, api-key, access-token]
summary: "Replacing a password, key or token with a new one and retiring the old one."
match: ['\b(?:key|credential|token|secret|password)s? rotations?\b', '\b(?:key|credential|token|secret|password)s? (?:(?:was|were|is|are|got|has been|have been|had to be) )?rotated\b', '\brotated (?:keys?|tokens?|credentials?|secrets?|passwords?)\b', '\brotate (?:the|a|an|its|that|every) (?:keys?|tokens?|credentials?|secrets?|passwords?)\b', '\b(?:had to be|were|are) rotated afterwards\b', '\brotation drill\b']
sources:
  - title: "Key rotation (glossary)"
    url: "https://csrc.nist.gov/glossary/term/key_rotation"
    publisher: "NIST"
    primary: true
  - title: "SP 800-57 Part 1 Rev. 5: Recommendation for Key Management"
    url: "https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final"
    publisher: "NIST"
classification:
  - {standard: sp800-53, clause: "IA-5", topic: "Authenticator Management",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=IA-05"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Key rotation means swapping a secret, such as a password, an {{< term "api-key" "API key" >}} or an {{< term "access-token" "access token" >}}, for a fresh one and switching the old one off. It is done on a schedule, so no single secret stays in use for too long, and straight away whenever a secret may have leaked. Rotation is what actually ends a leak: deleting the copy that escaped does not, because whoever saw the old secret can keep using it until it stops working.
