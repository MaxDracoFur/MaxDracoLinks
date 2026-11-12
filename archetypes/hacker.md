---
# Hacker post in the incident-report (INC) format. Create with:
#   hugo new content blog/<slug>.md --kind hacker
# The format, each section's purpose and where it comes from: docs/hacker-inc-format.md
# Preview with ./preview.sh --drafts; Max approves the copy before draft goes false.
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
slug: "{{ .File.ContentBaseName }}"
url: "/blog/{{ .File.ContentBaseName }}"
layout: "blog/single"
series: "hacker"   # drives the home page Security badge and the hack. writeup list
date: {{ .Date }}
draft: true
review_status: "copy-review"
introduces: []   # concepts.yaml: what this post explains first
uses: []         # concepts.yaml: what it leans on from earlier posts
summary: ""      # one or two sentences for link previews: what failed, and what it cost
cover_image: ""  # REQUIRED: /res/covers/<slug>.jpg, square CD-album-style (tools/cover_check.py)
cover_alt: ""    # one line describing the cover for screen readers
# Evidence: tag every fact in the text as measured (I saw it: a capture, a query, a count) or
# inferred (I reasoned to it). Anything from older notes says so: "from my notes".
# Disclosure: if a vendor is involved and their fix or advisory isn't public yet, keep this
# file UNTRACKED and set date no earlier than the end of the disclosure window.
---

<!--
Blameless. The system and its conditions are the subject, not a person. "I" is fine for what I
did; the question is always why that was the reasonable thing to do with what I knew then.
"Human error" is never a cause: if a person's action shows up, the finding is whatever made
that action easy and its result invisible.

Plain prose for a blog reader. The order below is the format; the headings can be reworded to
suit the post. A section that doesn't apply gets one sentence saying so, not deletion.
These comments don't render.
-->

<!-- SUMMARY (no heading). Two or three short paragraphs: what happened, how bad, what fixed it.
     A reader who stops here should know the whole story. -->

## Impact

<!-- Who or what was affected, how much, for how long. Numbers with their evidence label.
     Say what was NOT affected too, and how severe it really is: don't inflate it. -->

## Timeline

<!-- Dates or times, oldest first, one line each. Include when it started, when it could have
     been seen, when it was seen, each change, and when it ended. Mark each row's evidence. -->

| When | What happened | Evidence |
|---|---|---|
|  |  | measured |

## How it was found, and why not sooner

<!-- DETECTION. What actually surfaced it: an alert, a person looking, luck. Then why nothing
     caught it earlier: which signal existed but nobody was watching, which check didn't exist. -->

## What the evidence shows

<!-- FACTUAL INFORMATION. Facts only, no conclusions yet: versions, config, the log line, the
     capture, the test matrix, the reproduction (safe: throwaway credentials, one request).
     Everything Analysis relies on has to appear here first. -->

## Why it happened

<!-- ANALYSIS. Work only from the facts above. Walk the chain: why each condition existed, why
     each defence that could have stopped it didn't. Deal openly with anything that doesn't fit. -->

## Findings, causes and contributing factors

<!-- Short numbered findings (no new facts here). Then the causes: the immediate one AND the
     deeper systemic ones, and contributing factors that made it worse or longer. -->

1. 

**Causes:** 

**Contributing factors:** 

## What went well, what went wrong, where I got lucky

**Went well:** 

**Went wrong:** 

**Got lucky:** 

## What I changed, and what's still open

<!-- SAFETY RECOMMENDATIONS (to others: the vendor, readers who run the same thing) and ACTION
     ITEMS (mine). Each action has a type, an owner and a status. Done items stay listed. -->

Recommendations:

- 

| Action | Type | Owner | Status |
|---|---|---|---|
|  | mitigate / prevent / detect / process | me | done |

## Lessons

<!-- Two to four lessons that carry to other systems, not restatements of the fix. -->
