---
title: "Configuration drift"
term_kind: concept
topics: [security-operations]
see_also: [infrastructure-as-code, deployment]
summary: "When what is actually running gradually stops matching what was written down or approved."
match: ['\bconfig(?:uration)? drift\b', '\bdrifts? from what\b', '\balert on drift\b']
sources:
  - title: "SP 800-128, Guide for Security-Focused Configuration Management of Information Systems"
    url: "https://csrc.nist.gov/pubs/sp/800/128/upd1/final"
    publisher: "NIST"
    primary: true
  - title: "Configuration management"
    url: "https://en.wikipedia.org/wiki/Configuration_management"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "CM-2", topic: "Baseline Configuration",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=CM-02"}
  - {standard: sp800-53, clause: "CM-3", topic: "Configuration Change Control",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=CM-03"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Configuration drift is the slow gap that opens between how a system is supposed to be set up and how it actually is. A quick fix made by hand, a change that was never saved, or an update applied to one machine but not another all add up. Drift matters for security because nobody reviewed the parts that changed, so the usual cure is to keep the intended setup in one place, such as {{< term "infrastructure-as-code" >}}, and alert when the live system differs.
