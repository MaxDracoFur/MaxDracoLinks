---
title: "UTC"
term_kind: standard
topics: [logging-and-monitoring]
see_also: [syslog, metrics]
summary: "Coordinated Universal Time, the world's reference clock, used for timestamps that mean the same thing everywhere."
match: ['\bUTC\b']
sources:
  - title: "ITU-R TF.460: Standard-frequency and time-signal emissions"
    url: "https://www.itu.int/rec/R-REC-TF.460"
    publisher: "ITU"
    primary: true
  - title: "Coordinated Universal Time"
    url: "https://en.wikipedia.org/wiki/Coordinated_Universal_Time"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
UTC (Coordinated Universal Time) is the time standard the world's clocks are set from. It has no daylight saving and belongs to no country, and local times are described as offsets from it, such as UTC-6. Computers and logs often record times in UTC so that events from different places and seasons line up without confusion.
