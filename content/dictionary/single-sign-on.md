---
title: "Single sign-on (SSO)"
term_kind: concept
topics: [identity-and-access]
see_also: [authentication, two-factor-authentication]
summary: "Logging in once with one account to get into many separate apps or services."
match: ['\bsingle sign-on\b', '\bSSO\b']
sources:
  - title: "single sign-on (glossary)"
    url: "https://csrc.nist.gov/glossary/term/single_sign_on"
    publisher: "NIST CSRC"
    primary: true
  - title: "Single sign-on"
    url: "https://en.wikipedia.org/wiki/Single_sign-on"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Single sign-on lets you log in once, usually with a work or {{< term "google" >}} account, and then use many separate apps without logging in to each. The apps trust one login provider to vouch for who you are. It means fewer passwords and one place to switch someone's access off, but whoever controls that login provider can get into everything behind it.
