---
title: "Public-key cryptography"
term_kind: concept
topics: [cryptography, identity-and-access]
see_also: [encryption, hash-function, tls]
summary: "Cryptography that uses a pair of keys: a public one you can share and a private one you keep secret."
match: ['\bpublic[- ]keys?\b', '\bkey[- ]?pairs?\b']
sources:
  - title: "NIST CSRC Glossary: public key cryptography"
    url: "https://csrc.nist.gov/glossary/term/public_key_cryptography"
    publisher: "NIST"
    primary: true
  - title: "Public-key cryptography"
    url: "https://en.wikipedia.org/wiki/Public-key_cryptography"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
In public-key cryptography each person or device has two linked keys. The public key can be handed out freely; the private key never leaves its owner. Anything locked with the public key can only be opened with the private key, and a signature made with the private key can be checked by anyone holding the public key. This lets two sides that have never met set up {{< term "encryption" "encrypted" >}} connections, and it underpins {{< term "tls" >}}, {{< term "ssh" >}} and {{< term "wireguard" >}}.
