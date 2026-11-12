---
title: "Client (client-server)"
term_kind: concept
topics: [networking]
see_also: [api, http]
summary: "A program that connects to a server to ask it for something."
match: ['\bclients?\b']
sources:
  - title: "client"
    url: "https://csrc.nist.gov/glossary/term/client"
    publisher: "NIST CSRC"
    primary: true
  - title: "Client-server model"
    url: "https://en.wikipedia.org/wiki/Client%E2%80%93server_model"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
In computing, a client is the program that asks and a server is the program that answers. A web browser is a client of a website; an email app is a client of the mail server; a script that calls an {{< term "api" >}} is a client of that API. The client decides how long to wait and what to do with the reply, so a badly behaved server can tie up a client that doesn't set limits.
