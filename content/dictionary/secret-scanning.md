---
title: "Secret scanning"
term_kind: concept
topics: [security-operations, identity-and-access]
see_also: [api-key, regular-expression, key-rotation]
summary: "Automatically searching code, logs or files for passwords, keys and tokens that should not be there."
match: ['\bsecrets? scann(?:ing|ers?)\b', '\bscan(?:s|ned|ning)?\b[^.]{0,40}\bfor secrets\b']
sources:
  - title: "About secret scanning"
    url: "https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning"
    publisher: "GitHub"
    primary: true
  - title: "Secrets Management Cheat Sheet"
    url: "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html"
    publisher: "OWASP"
classification:
  - {standard: attack, clause: "T1552", topic: "Unsecured Credentials",
     url: "https://attack.mitre.org/techniques/T1552/"}
  - {standard: cwe, clause: "CWE-532", topic: "Insertion of Sensitive Information into Log File",
     url: "https://cwe.mitre.org/data/definitions/532.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Secret scanning is an automatic search through code, logs or other stored files for things that look like passwords, {{< term "api-key" "API keys" >}} or {{< term "access-token" "access tokens" >}}. Most secrets have a recognisable shape, such as a fixed prefix or a long random string, so a program can spot them with patterns. Finding one means it has leaked somewhere it shouldn't be, and the safe response is to replace it, not just delete the copy.
