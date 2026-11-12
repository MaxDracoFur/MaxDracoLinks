---
title: "Hash"
term_kind: concept
topics: [cryptography]
see_also: [public-key-cryptography, encryption]
summary: "A calculation that turns any data into a short, fixed-length value that is always the same for the same input."
match: ['\bhash(?:es|ed|ing)?\b', '\bchecksums?\b', '\bSHA-?(?:1|2|256|512)\b', '\bkey fingerprints?\b']
sources:
  - title: "Hash function (glossary)"
    url: "https://csrc.nist.gov/glossary/term/hash_function"
    publisher: "NIST CSRC"
    primary: true
  - title: "FIPS 180-4: Secure Hash Standard (SHS)"
    url: "https://csrc.nist.gov/pubs/fips/180-4/upd1/final"
    publisher: "NIST"
  - title: "Hash function"
    url: "https://en.wikipedia.org/wiki/Hash_function"
    publisher: "Wikipedia"
classification:
  - {standard: cwe, clause: "CWE-328", topic: "Use of Weak Hash",
     url: "https://cwe.mitre.org/data/definitions/328.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A hash function turns data of any size into a short, fixed-length value called a hash. The same input always gives the same hash, and a good cryptographic hash such as SHA-256 makes it practically impossible to work back to the input or to find two inputs with the same hash (a collision). Hashes are used to check that files haven't changed, to store passwords, and as a short fingerprint of a key; a checksum is a simpler cousin that catches accidents but not tampering. A hash doesn't hide an input that can be guessed: anyone can hash each likely value and compare. Older hashes such as SHA-1 are no longer considered safe.
