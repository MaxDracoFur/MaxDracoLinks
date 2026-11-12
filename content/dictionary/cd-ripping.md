---
title: "CD ripping"
term_kind: concept
topics: [hardware, data-formats]
see_also: [cd-toc, disc-id, musicbrainz]
summary: "Copying the audio from a CD onto a computer as files."
match: ['\bripp(?:ing|ers?|ed)\b', '\brip logs?\b']
sources:
  - title: "IEC 60908:1999 Audio recording: Compact disc digital audio system"
    url: "https://webstore.iec.ch/en/publication/3885"
    publisher: "IEC"
    primary: true
  - title: "Ripping"
    url: "https://en.wikipedia.org/wiki/Ripping"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Ripping a CD means reading its digital audio and saving it as files on a computer. Ripping software (a "ripper") first reads the disc's {{< term "cd-toc" "table of contents" >}}, works out which album it is by looking up a {{< term "disc-id" >}} in an online database such as {{< term "musicbrainz" >}}, and then copies each track, often checking the copy is exact. Many rippers keep a log of every disc they read.
