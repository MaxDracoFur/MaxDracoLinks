---
title: "Secrets manager (vault)"
term_kind: concept
topics: [identity-and-access, security-operations]
see_also: [machine-identity, api-key, key-rotation]
summary: "A service that stores passwords, keys and tokens in one protected place and hands them out only to programs and people allowed to have them."
match: ['\bsecrets? (?:managers?|vaults?)\b', '\bthe vault\b']
sources:
  - title: "Secrets Management Cheat Sheet"
    url: "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html"
    publisher: "OWASP"
    primary: true
  - title: "What is Vault?"
    url: "https://developer.hashicorp.com/vault/docs/about-vault/what-is-vault"
    publisher: "HashiCorp"
classification:
  - {standard: sp800-53, clause: "IA-5", topic: "Authenticator Management",
     url: "https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_2_0/home?element=IA-05"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A secrets manager, often called a vault, keeps passwords, {{< term "api-key" "API keys" >}} and other credentials in one {{< term "encryption" "encrypted" >}}, access-controlled place instead of scattered across files, chat messages and scripts. Programs ask it for the secret they need when they need it, proving who they are first, and every request can be logged. It also makes replacing a leaked secret easier, because there is one place to change it.
