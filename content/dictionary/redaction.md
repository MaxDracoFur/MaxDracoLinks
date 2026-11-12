---
title: "Redaction"
term_kind: concept
topics: [logging-and-monitoring, security-operations]
see_also: [secret-scanning, retention, regular-expression]
summary: "Removing or masking secrets and personal details before text is stored or shared."
match: ['\bredact(?:ion|ions|ed|s|ing)?\b']
sources:
  - title: "NIST CSRC Glossary: redaction"
    url: "https://csrc.nist.gov/glossary/term/redaction"
    publisher: "NIST"
    primary: true
  - title: "Logging Cheat Sheet"
    url: "https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html"
    publisher: "OWASP"
classification:
  - {standard: cwe, clause: "CWE-532", topic: "Insertion of Sensitive Information into Log File",
     url: "https://cwe.mitre.org/data/definitions/532.html"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Redaction means blanking out the sensitive parts of something, such as passwords, {{< term "api-key" "API keys" >}} or personal details, before it is saved, shown or handed on, while leaving the rest readable. In computer logs it is usually done automatically, with a {{< term "regular-expression" "pattern" >}} that finds secrets and swaps them for a placeholder. It has to happen before the text is stored: once a secret is written to a log, anyone who can read the log can read the secret.
