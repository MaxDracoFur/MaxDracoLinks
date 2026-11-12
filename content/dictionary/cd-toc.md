---
title: "CD table of contents (TOC)"
term_kind: format
topics: [data-formats, hardware]
see_also: [disc-id, cd-ripping]
summary: "The list at the start of an audio CD saying how many tracks it has and exactly where each one starts."
match: ['\bTOCs?\b', '\b(?:disc|CD)\S{0,2} table of contents\b']
sources:
  - title: "IEC 60908:1999 Audio recording: Compact disc digital audio system"
    url: "https://webstore.iec.ch/en/publication/3885"
    publisher: "IEC"
    primary: true
  - title: "Disc ID Calculation"
    url: "https://musicbrainz.org/doc/Disc_ID_Calculation"
    publisher: "MusicBrainz"
  - title: "Compact Disc Digital Audio"
    url: "https://en.wikipedia.org/wiki/Compact_Disc_Digital_Audio"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Every audio CD begins with a table of contents, or TOC: the number of tracks and the position where each one starts, measured in frames of 1/75 of a second. A player reads it to know where to jump. Because the exact positions differ from album to album, the TOC works like a fingerprint, and the common {{< term "disc-id" "disc IDs" >}} are calculated from it. It can also reveal things like hidden audio before the first track or a data section on an enhanced CD.
