---
title: "Disc ID"
term_kind: concept
topics: [data-formats, hardware]
see_also: [cd-toc, musicbrainz, hash-function]
summary: "A short code calculated from a CD's track layout, used to look the album up online."
match: ['\bdisc IDs?\b', '\bCDDB IDs?\b', '\bshort ID\b']
sources:
  - title: "Disc ID"
    url: "https://musicbrainz.org/doc/Disc_ID"
    publisher: "MusicBrainz"
    primary: true
  - title: "Disc ID Calculation"
    url: "https://musicbrainz.org/doc/Disc_ID_Calculation"
    publisher: "MusicBrainz"
  - title: "CDDB"
    url: "https://en.wikipedia.org/wiki/CDDB"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A disc ID is a short code calculated from a CD's {{< term "cd-toc" "table of contents" >}}: how many tracks it has and exactly where each one starts. Online music databases such as {{< term "musicbrainz" >}} and the older CDDB, now run by {{< term "gracenote" >}}, use it to recognise an album the moment a disc goes in, without listening to the music. Because track positions often differ slightly between pressings of the same album, the ID can point to one specific pressing rather than just the album.
