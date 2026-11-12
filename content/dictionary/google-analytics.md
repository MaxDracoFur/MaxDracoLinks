---
title: "Google Analytics (GA4)"
term_kind: tool
topics: [web-and-advertising, platforms-and-services]
see_also: [google, google-adsense, session-recording]
summary: "Google's service that counts and describes a website's visitors, using a tracking tag on each page."
match: ['\bGoogle Analytics\b', '\bGA4\b', '\bUniversal Analytics\b', '\bUA-\d{4,10}-\d{1,4}\b', '\btracking (?:tag|ID)s?\b', '\banalytics IDs?\b']
sources:
  - title: "GA4 has replaced Universal Analytics"
    url: "https://support.google.com/analytics/answer/11583528"
    publisher: "Google Analytics Help"
    primary: true
  - title: "[GA4] Find your Google tag ID"
    url: "https://support.google.com/analytics/answer/9539598"
    publisher: "Google Analytics Help"
  - title: "Google Analytics"
    url: "https://en.wikipedia.org/wiki/Google_Analytics"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Run by {{< term "google" >}}, Google Analytics is a free service that tells website owners how many people visit, where they come from and what they look at. The owner puts a small tracking tag on every page, and the tag carries the account's ID: older Universal Analytics IDs look like UA- followed by numbers, and the current version, GA4, uses IDs starting with G-. Because the ID sits in the public page, it can show that two sites are measured by the same account.
