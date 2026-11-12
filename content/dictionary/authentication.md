---
title: "Authentication (and authorisation)"
term_kind: concept
topics: [identity-and-access]
see_also: [two-factor-authentication, api-key, least-privilege]
summary: "Checking who someone is (authentication), then deciding what they are allowed to do (authorisation)."
match: ['\bunauthenticated\b', '\bauthenticat(?:e|es|ed|ing)\b', '\bno authentication\b', '\baccess control\b', '\bauthori[sz](?:e|es|ed|ing|ation)\b', '\bauthz\b']
sources:
  - title: "authentication"
    url: "https://csrc.nist.gov/glossary/term/authentication"
    publisher: "NIST CSRC"
    primary: true
  - title: "access control"
    url: "https://csrc.nist.gov/glossary/term/access_control"
    publisher: "NIST CSRC"
  - title: "Authentication"
    url: "https://en.wikipedia.org/wiki/Authentication"
    publisher: "Wikipedia"
classification:
  - {standard: sp800-53, clause: "IA-2", topic: "Identification and Authentication (Organizational Users)",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=IA-02"}
  - {standard: sp800-53, clause: "AC-3", topic: "Access Enforcement",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=AC-03"}
  - {standard: cwe, clause: "CWE-306", topic: "Missing Authentication for Critical Functionality",
     url: "https://cwe.mitre.org/data/definitions/306.html"}
  - {standard: cwe, clause: "CWE-862", topic: "Missing Authorization",
     url: "https://cwe.mitre.org/data/definitions/862.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Authentication is how a system checks who is asking: a password, an {{< term "api-key" "API key" >}}, a code from a phone. Authorisation (sometimes shortened to "authz") comes next and decides what that person or program may do; together they are called access control. A service that skips the first step is "unauthenticated": anyone who can reach it can use it. That is one of the most common ways systems get misused.
