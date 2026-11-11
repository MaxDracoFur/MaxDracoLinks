---
title: "TLS"
term_kind: technology
summary: "Transport Layer Security: the encryption that protects data on its way across a network (the S in HTTPS)."
match: ['\bTLS\b']
sources:
  - title: "RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3"
    url: "https://www.rfc-editor.org/rfc/rfc8446"
    publisher: "IETF"
    primary: true
  - title: "Transport Layer Security"
    url: "https://en.wikipedia.org/wiki/Transport_Layer_Security"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first; health is checked daily.
draft: true
---
TLS encrypts a connection between two programs and lets the client check it is talking to the right server. It replaced SSL, and it is what puts the padlock on HTTPS websites. The current version, TLS 1.3, is defined in RFC 8446. Other protocols, syslog among them, can run over TLS too.

## Why it's on this site

Whenever a post asks whether something crosses my network in plain text, TLS is the usual fix.
