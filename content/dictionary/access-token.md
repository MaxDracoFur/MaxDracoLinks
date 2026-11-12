---
title: "Access token"
term_kind: concept
topics: [identity-and-access]
see_also: [api-key, key-rotation, secrets-manager]
summary: "A secret string a program presents to a service to prove it is allowed to act, often for a limited time."
match: ['\b(?:access|bearer|bot|API) tokens?\b', '\bbearer credentials?\b', '\btokens?\b']
sources:
  - title: "RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage"
    url: "https://www.rfc-editor.org/rfc/rfc6750.html"
    publisher: "IETF"
    primary: true
  - title: "RFC 6749: The OAuth 2.0 Authorization Framework"
    url: "https://www.rfc-editor.org/rfc/rfc6749.html"
    publisher: "IETF"
  - title: "Access token"
    url: "https://en.wikipedia.org/wiki/Access_token"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "T1528", topic: "Steal Application Access Token",
     url: "https://attack.mitre.org/techniques/T1528/"}
  - {standard: attack, clause: "T1550.001", topic: "Use Alternate Authentication Material: Application Access Token",
     url: "https://attack.mitre.org/techniques/T1550/001/"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
An access token is a long secret string that a program sends with each request to show it is allowed to use a service, much like an {{< term "api-key" >}}. Many are "bearer" tokens: whoever holds the string gets the access, with no further check of who they are. That makes a leaked token as good as a stolen password until it is revoked, which is why tokens are kept out of logs and chat, given an expiry, and replaced regularly.
