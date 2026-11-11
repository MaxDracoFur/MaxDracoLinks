---
title: "API key"
term_kind: thing
summary: "A secret string a program sends to prove which account it is calling an API as."
match: ['\bAPI[ _-]?keys?\b']
sources:
  - title: "API key"
    url: "https://en.wikipedia.org/wiki/API_key"
    publisher: "Wikipedia"
    primary: true
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording, then flips draft to false. Sources: primary/official first; health is checked daily.
draft: true
---
An API key is a long random string that identifies a program to a service's API, a bit like a password made for software. Some services use a key alone; others pair a key with a separate secret. Anyone who gets hold of a working key can act as its owner, so keys are kept private and replaced when they might have been exposed.

## Why it's on this site

My scripts and monitoring talk to my own devices through their APIs, each with its own key.
