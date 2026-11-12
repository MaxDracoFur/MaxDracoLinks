---
title: "Prompt injection"
term_kind: concept
topics: [programming-and-ai, security-operations]
see_also: [llm, sandbox, least-privilege]
summary: "Hiding instructions in text an AI model reads, so that it follows them instead of its user."
match: ['\bprompt[- ]inject(?:ion|ions|ed)\b']
sources:
  - title: "NIST CSRC Glossary: prompt injection"
    url: "https://csrc.nist.gov/glossary/term/prompt_injection"
    publisher: "NIST"
    primary: true
  - title: "LLM01: Prompt Injection"
    url: "https://genai.owasp.org/llmrisk/llm01-prompt-injection/"
    publisher: "OWASP"
  - title: "Prompt injection"
    url: "https://en.wikipedia.org/wiki/Prompt_injection"
    publisher: "Wikipedia"
classification:
  - {standard: atlas, clause: "AML.T0051", topic: "LLM Prompt Injection",
     url: "https://atlas.mitre.org/techniques/AML.T0051"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A {{< term "llm" "large language model" >}} can't reliably tell its user's instructions apart from instructions written inside the text it is reading, such as a web page, an email or a document. Prompt injection exploits that: an attacker plants text like "ignore your previous instructions and..." where the model will read it. It matters most when the model can take actions, such as sending messages or calling an {{< term "api" >}}, because the planted text can then make it do things its user never asked for.
