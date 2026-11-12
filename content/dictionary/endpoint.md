---
title: "Endpoint (route)"
term_kind: concept
topics: [programming-and-ai, platforms-and-services]
see_also: [api, http, webhook]
summary: "One specific address on a web service that a program can call to do one job."
match: ['\bendpoints?\b']
sources:
  - title: "OpenAPI Specification"
    url: "https://spec.openapis.org/oas/latest.html"
    publisher: "OpenAPI Initiative"
    primary: true
  - title: "Web API"
    url: "https://en.wikipedia.org/wiki/Web_API"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
An endpoint is one specific address on a web service that a program can call, each doing one job: fetch a list, send a message, take a photo. An {{< term "api" >}} is a collection of endpoints; a program sends a request to one and gets data or an action back. Some tools call them routes. Each endpoint is a separate way into the service, so each one needs its own check of who is allowed to use it.
