---
title: "Two-factor authentication (2FA)"
term_kind: concept
topics: [identity-and-access]
see_also: [authentication, single-sign-on, phishing]
summary: "Signing in with two different kinds of proof, such as a password plus a code from a phone."
match: ['\b2FA\b', '\btwo-factor\b', '\bMFA\b', '\bmulti-?factor\b', '\bauthenticator apps?\b']
sources:
  - title: "multi-factor authentication (NIST CSRC glossary)"
    url: "https://csrc.nist.gov/glossary/term/multi_factor_authentication"
    publisher: "NIST"
    primary: true
  - title: "NIST SP 800-63B: Authentication and Authenticator Management"
    url: "https://pages.nist.gov/800-63-4/sp800-63b.html"
    publisher: "NIST"
  - title: "Multi-factor authentication"
    url: "https://en.wikipedia.org/wiki/Multi-factor_authentication"
    publisher: "Wikipedia"
classification:
  - {standard: attack, clause: "M1032", topic: "Multi-factor Authentication",
     url: "https://attack.mitre.org/mitigations/M1032/"}
  - {standard: sp800-53, clause: "IA-2(1)", topic: "Multi-factor Authentication to Privileged Accounts",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=IA-02(01)"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Two-factor {{< term "authentication" >}} (2FA) asks for two different kinds of proof before letting someone in: usually something they know, like a password, plus something they have, like a phone running an authenticator app or a hardware key. Multi-factor authentication (MFA) is the general name for two or more. A stolen password alone is then not enough. It only protects an account once it is actually switched on and required, not merely set up.
