---
title: "Base64"
term_kind: technology
summary: "A way to write any binary data using only 64 printable characters: A-Z, a-z, 0-9, + and /."
match: ['\bbase64\b']
sources:
  - title: "RFC 4648: The Base16, Base32, and Base64 Data Encodings"
    url: "https://www.rfc-editor.org/rfc/rfc4648"
    publisher: "IETF"
    primary: true
  - title: "Base64"
    url: "https://en.wikipedia.org/wiki/Base64"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first; health is checked daily.
draft: true
---
Base64 turns bytes into text so they can travel through systems that only handle letters and digits, such as email, URLs or config files. Every 3 bytes become 4 characters, and = signs pad the end. It is an encoding, not encryption: anyone can turn it back into the original bytes.

## Why it's on this site

Keys, tokens and certificates are often written in base64, so it turns up all over config files.
