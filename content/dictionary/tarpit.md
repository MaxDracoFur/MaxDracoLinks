---
title: "Tarpit"
term_kind: concept
topics: [security-operations, networking]
see_also: [timeout, ssh, port-scanning]
summary: "A server that deliberately answers connections as slowly as possible, to waste the time of whoever connects."
match: ['\btar ?pits?\b']
sources:
  - title: "Endlessh: an SSH tarpit"
    url: "https://github.com/skeeto/endlessh"
    publisher: "Endlessh project"
    primary: true
  - title: "Tarpit (networking)"
    url: "https://en.wikipedia.org/wiki/Tarpit_(networking)"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "SC-26", topic: "Decoys",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=SC-26"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A tarpit is a server that accepts a connection and then answers as slowly as it can, a byte at a time, so the program on the other end is stuck waiting. Defenders use tarpits to slow down automated scanners and spam bots, for example on an unused {{< term "ssh" >}} port. A {{< term "client" >}} only escapes if it has a {{< term "timeout" >}} that limits the whole exchange, not just each step.
