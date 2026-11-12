---
title: "Webhook"
term_kind: concept
topics: [programming-and-ai]
see_also: [polling, api, http]
summary: "A way for one service to notify another of an event by sending it a web request."
match: ['\bweb ?hooks?\b']
sources:
  - title: "About webhooks"
    url: "https://docs.github.com/en/webhooks/about-webhooks"
    publisher: "GitHub"
    primary: true
  - title: "Webhook"
    url: "https://en.wikipedia.org/wiki/Webhook"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A webhook is an address a program gives to a service, saying "when something happens, send the details here". The service then makes an {{< term "http" >}} request to that address each time the event occurs. It is the opposite of {{< term "polling" >}}, where the program keeps asking whether anything is new. Because anyone who learns the address can send it requests, webhooks are usually protected with a shared secret.
