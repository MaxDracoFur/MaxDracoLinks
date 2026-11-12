---
title: "Handshake"
term_kind: concept
topics: [networking, cryptography]
see_also: [tls, tcp, wpa]
summary: "The opening exchange of messages in which two devices agree to talk and set up how."
match: ['\bhandshakes?\b']
sources:
  - title: "Handshake (glossary)"
    url: "https://csrc.nist.gov/glossary/term/handshake"
    publisher: "NIST CSRC"
    primary: true
  - title: "RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3"
    url: "https://www.rfc-editor.org/info/rfc8446/"
    publisher: "IETF"
  - title: "Handshake (computing)"
    url: "https://en.wikipedia.org/wiki/Handshake_(computing)"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12.
draft: false
---
A handshake is the short exchange of messages at the start of a connection, before any real data flows. The two sides confirm they can reach each other and agree on settings; in {{< term "encryption" "encrypted" >}} protocols such as {{< term "tls" >}} or {{< term "wireguard" >}} they also prove who they are and agree on fresh keys for the session. If the handshake doesn't complete, there is no connection. Anyone nearby can record a handshake, so a good design gives an eavesdropper nothing to work with, while older {{< term "wpa" "Wi-Fi security" >}} let a recorded handshake be used to {{< term "password-cracking" "guess the password offline" >}}.
