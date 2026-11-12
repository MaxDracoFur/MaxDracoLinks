---
title: "Single point of failure"
term_kind: concept
topics: [platforms-and-services]
see_also: [high-availability, cluster]
summary: "One part of a system that, if it fails, takes the whole system down with it."
match: ['\bsingle points? of failure\b', '\bSPOFs?\b']
sources:
  - title: "SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems"
    url: "https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final"
    publisher: "NIST"
    primary: true
  - title: "Single point of failure"
    url: "https://en.wikipedia.org/wiki/Single_point_of_failure"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A single point of failure is any one part, such as a box, a cable, a power supply or a person, that the whole system depends on, so when it fails everything stops. The usual fix is redundancy: a second copy that can take over. Finding them is harder than it sounds, because shared things like one power strip or one {{< term "network-switch" "network switch" >}} are easy to overlook.
