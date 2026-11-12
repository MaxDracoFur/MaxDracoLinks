---
title: "Incident report (postmortem)"
term_kind: concept
topics: [security-operations]
see_also: [runbook, latent-condition, blast-radius]
summary: "A written account of something that went wrong, or nearly did, focused on causes and fixes rather than blame."
match: ['\bincident[- ]reports?\b', '\bpost-?mortems?\b']
sources:
  - title: "Postmortem Culture: Learning from Failure (Site Reliability Engineering, chapter 15)"
    url: "https://sre.google/sre-book/postmortem-culture/"
    publisher: "Google"
    primary: true
  - title: "SP 800-61 Rev. 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management"
    url: "https://csrc.nist.gov/pubs/sp/800/61/r3/final"
    publisher: "NIST"
classification:
  - {standard: sp800-53, clause: "IR-4", topic: "Incident Handling",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=IR-04"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
An incident report, often called a postmortem, is a write-up made after something goes wrong, or nearly does. The common format, popularised by {{< term "google" >}}'s site reliability engineers, gives the impact, a timeline, the root cause and what contributed to it, what went well and what was luck, and a list of fixes with owners. A good one is blameless: it assumes people acted sensibly with what they knew and asks what about the system let the mistake happen, so that people report problems instead of hiding them.
