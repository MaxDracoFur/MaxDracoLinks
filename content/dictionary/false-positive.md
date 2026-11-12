---
title: "False positive"
term_kind: concept
topics: [security-operations, logging-and-monitoring]
see_also: [vulnerability, paging]
summary: "An alarm or match that fires when nothing is actually wrong."
match: ['\bfalse positives?\b', '\bfalse match(?:es)?\b', '\bfalse alarms?\b']
sources:
  - title: "False Positive (glossary)"
    url: "https://csrc.nist.gov/glossary/term/false_positive"
    publisher: "NIST CSRC"
    primary: true
  - title: "False positives and false negatives"
    url: "https://en.wikipedia.org/wiki/False_positives_and_false_negatives"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A false positive is an alarm that goes off when nothing is actually wrong: a {{< term "vulnerability" "vulnerability scanner" >}} flags software that isn't affected, or a check matches the wrong thing. The opposite, a false negative, is a real problem the check misses. Too many false positives teach people to ignore alerts, so a good check is tuned to keep them rare without letting real problems slip past.
