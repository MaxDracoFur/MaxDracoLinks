---
title: "AI agents in my homelab, and the things they still have to ask me about"
slug: "agents-without-the-keys"
url: "/blog/agents-without-the-keys"
layout: "blog/single"
series: "hacker"
date: 2026-11-12T07:30:00-06:00
draft: false
review_status: "approved"
introduces: [homelab-agents]
cover_image: "/res/covers/agents-without-the-keys.jpg"
cover_alt: "Album-style cover: the words Without the Keys beside a compact disc."
summary: "I let AI coding agents do real work on my homelab. Here's what they can do alone, what still needs my yes, and the incident that wrote one of the rules."
---

Most of the work in my {{< term "homelab" "homelab" >}} now gets done by {{< term "ai" >}} coding agents, Claude Code sessions specifically. They {{< term "deployment" "deploy" >}} apps, write alert rules, chase down flaky hardware and fix their own bugs. They have real access, because an agent that can't touch anything can't do anything useful. So the question isn't whether to give them access. It's where the edges are, and who is standing at each one.

In October one of those edges failed quietly. An agent added a guard to a deploy script so the script would refuse to create a database, then ran the script to test the guard. The guard had never been written: the edit failed without a sound. The script ran for real and created a database and a user in my shared {{< term "postgresql" "Postgres" >}}, the exact thing the guard existed to prevent.

That incident, and an older pattern of credentials passing through the chat, wrote most of the rules below. This is the write-up, as an {{< term "incident-report" "incident report" >}}, of how the agents' edges are drawn and why.

## Impact

- **The October run:** one unwanted database and one unwanted user created in the shared Postgres that my other apps use. *(from my notes)* The script's job was to create them, and that's what it did. The new database was empty and nothing connected to it, and the new user had no special powers; no other database is recorded as touched. Both were removed on October 30. *(from my notes; the removal date inferred from the to-do record, which logs the removal and a check that nothing was left)*
- **The same session, a second loss:** a configuration file for that old app, which wasn't in {{< term "git" "git" >}} yet, was deleted along the way. A few hundred bytes of edits were gone for good, and the file was partly rebuilt from a copy on another machine. *(from my notes)*
- **Credentials in the chat:** before secrets had their own path, keys were pasted into agent chats when an agent needed one, and more than five {{< term "key-rotation" "had to be rotated afterwards" >}}. *(from my notes; the count is my account)*
- **What wasn't affected:** nothing I've recorded points to anything outside my network, or to a pasted key being used by anyone else. *(inferred)*

Severity: low. A stray database is cleanup, and a rotated key is a chore. Both are the kind of thing that's low only because it was caught.

## Timeline

| When (2026) | What happened | Evidence |
|---|---|---|
| Before Sep 4 | When an agent needs a credential, it's pasted into the chat. Some keys are rotated afterwards. | from my notes |
| Sep 4 | Agents get their own {{< term "machine-identity" "machine identity" >}} in my {{< term "secrets-manager" "secrets manager" >}}. | from my notes; date inferred (the identity's stored credential and the fetch script both date from that afternoon) |
| Oct 20, evening | Retiring an old app, an agent adds a guard to its deploy script. The edit fails silently. The agent runs the script to test the guard; it creates a database and a user in the shared Postgres. | from my notes; date inferred (the incident record logs the creation at 21:23 Chicago time) |
| After Oct 20 | Two rules added for every agent: never test a guard by running what it guards, and check an edit landed before relying on it. | from my notes |
| Oct 30 | The stray database and user removed; a check finds nothing left. | from my notes; date inferred (to-do record) |
| Nov 2, late evening | Builds only from pushed commits, and an alert when what's running {{< term "configuration-drift" "drifts from what" >}}'s pushed. | from my notes; date inferred (the commits that add the build tool and the alert rule, 23:00 and 23:13 Chicago time) |

## How it was found, and why not sooner

The October run was noticed through the script's own output: it said what it was creating as it created it. *(from my notes)*

The October run wasn't hidden; the script did what it was written to do, out loud. What nothing caught was the moment before it: the failed edit. *(inferred)*

- **The edit.** The insert failed, and nothing between that failure and the next command stopped the work. *(inferred)*
- **The guard.** A guard that didn't install looks exactly like one that did, unless you look for it. Nothing looked. *(inferred)*
- **The test.** The only check of the guard was running the guarded command, so the check and the damage were the same event. *(from my notes)*

For pasted keys, there was nothing to catch: pasting was the only route a credential had. *(inferred)*

## What the evidence shows

**The October edit.** The guard was anchored on a line that appeared twice in the deploy script. The insert failed and nothing was added. The script then ran for real and created a database and a user in my shared Postgres. *(from my notes)*

**What an agent can do alone.** Plenty: read logs and {{< term "metrics" "metrics" >}}, build and deploy {{< term "container" "app images" >}}, roll out a new version, write and ship alert rules, file and close work on my roadmap board. Most work runs off cards on that board, and every attempt on a card gets logged with an outcome (solved, partial, failed or abandoned), so I can see what happened while I wasn't watching. *(from my notes)*

When an agent can't finish because it needs my login, my hands, a purchase or a decision, it doesn't leave the card quietly stuck. It puts a question on the card, and the board shows me that question instead of a "work on this" button. *(from my notes)*

**What still needs my yes.** Some actions get refused by the agent's own permission checks, and the only way past is me saying yes in the chat. Among them:

- installing anything that keeps itself running on a host, like a new {{< term "daemon" "system service" >}} or timer;
- changing any {{< term "dns" >}} record;
- widening a {{< term "firewall" "firewall" >}} or {{< term "allowlist" "allowlist" >}}, even to let my own laptop back in at a new address;
- writing secrets into the {{< term "cluster" "cluster" >}};
- installing or upgrading operating-system packages on a server.

*(from my notes)*

**Secrets.** Agents fetch credentials from my {{< term "self-hosting" "self-hosted" >}} secrets manager, using their own machine identity that can only see infrastructure credentials. The {{< term "access-token" "bearer credential" >}} for that identity sits in the {{< term "macos" >}} {{< term "keychain" "Keychain" >}}, not in a plaintext file. *(from my notes)*

**Builds.** Image builds refuse to run from a working tree with uncommitted changes, or from a commit that isn't pushed yet. Each image is tagged with the commit it came from. If what's running drifts from what's pushed for more than a day, an alert fires. *(from my notes)*

## Why it happened

**A failed edit and a successful one look the same from outside.** The anchor line wasn't unique, so the insert couldn't know where to go, and it stopped. That's the correct behaviour for the tool. But the next step didn't depend on checking the result; it depended on assuming it. *(from my notes; the reading is inferred)*

**The test exercised the thing it was guarding.** Running the script was the natural way to see the guard work, and it would have been harmless if the guard were there. With the guard missing, the only possible outcome of that test was the incident. *(inferred)*

**Scripts that write to shared systems don't look different from ones that don't.** Nothing about the command said "this creates things in the database every app uses". *(inferred)*

**Credentials went through the chat because the chat was the only path.** When an agent needed a key and there was no other way to hand it over, pasting was the reasonable thing to do. The fix was a path, not a resolution to paste less. *(inferred)*

## Findings, causes and contributing factors

1. The guard's edit was anchored on a line that appeared twice in the script, and the insert failed.
2. The failure didn't stop the work that depended on it.
3. The guard was tested by running the script it guarded.
4. The script created a database and a user in the shared Postgres.
5. Before agents had their own identity in the secrets manager, credentials reached them through the chat, and some were rotated afterwards.

**Immediate cause:** running the guarded script while the guard was absent.

**Systemic causes:** nothing checked that an edit had landed before the next step relied on it, and the only test of a guard was the action it was meant to block. For credentials: no route existed other than the chat.

**Contributing factors:** a non-unique anchor line in a script; a guard test whose failure mode was the incident itself; no visible marker that a script writes to shared infrastructure.

## What went well, what went wrong, where I got lucky

**Went well:** the incident turned into two rules that every agent now works under, instead of a note about one script. Credentials got their own path, with a {{< term "least-privilege" "least-privilege" >}} identity and its own credential kept out of plaintext.

**Went wrong:** a silent edit failure flowed straight into a real run. The guard's test and the guard's failure were the same event.

**Got lucky:** the script created things rather than deleting them. A guard on a drop or a cutover, tested the same way, would have been much worse. *(inferred)*

## What I changed, and what's still open

The rule I hold the agents to underneath all of this: don't route around a refusal through another tool or another session. Stage the change, write down the exact command, and ask.

Two rules came out of October, and every agent works under them now:

1. **Never test a guard by running the thing it guards.** Test the guard's condition on its own, or ask a question that can't trigger the action.
2. **After an edit, check that it actually landed** before doing anything that depends on it.

And for secrets, the rule is simple: if a secret is missing, the agent asks me to put it in the vault. It doesn't ask me to paste it.

Recommendations, for anyone giving agents real access:

- Decide which actions need a yes, and make the agent's own permission checks enforce it, not its good intentions.
- Give agents their own least-privilege identity for secrets, so the chat is never the path.
- Make builds traceable to a pushed commit, and alert on drift.
- Test guards without triggering what they guard.

| Action | Type | Owner | Status |
|---|---|---|---|
| Never test a guard by running what it guards | process | me (all agents) | done |
| Check an edit landed before relying on it | prevent | me (all agents) | done |
| Agents fetch secrets with their own machine identity; never via chat | prevent | me | done Sep 4 |
| Permission checks refuse host services, DNS, firewall widening, cluster secrets, OS packages without my yes | prevent | me | done |
| Builds only from pushed commits; images tagged with their commit | prevent | me | done Nov 2 |
| Alert when what's running drifts from what's pushed for over a day | detect | me | done Nov 2 |
| Agents ask on the card instead of leaving it stuck | process | me | done |

**Me in the loop.** Agents draft things for me, this post included. Nothing goes out under my name until I've read it and signed off on what it says. They're very good at doing the work. Deciding what I'm willing to stand behind is still my job.

## Lessons

- **A guard that didn't install looks exactly like one that did.** Treat a failed edit as the dangerous case.
- **If the only way to test a check is to trigger what it prevents, the test is the incident.** Test the condition, not the consequence.
- **Fix the path, not the habit.** Credentials stopped going through the chat when there was somewhere else for them to go.
- **When I come back to something, I can always answer "what is actually running, and why?"** That's what makes giving agents access survivable.
