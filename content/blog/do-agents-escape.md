---
title: "I put an AI agent in a box and told it to break out. The box held. The door I left open was somewhere else."
slug: "do-agents-escape"
url: "/blog/do-agents-escape"
layout: "blog/single"
series: "hacker"
date: 2026-11-12T08:00:00-06:00
draft: false
review_status: "approved"
introduces: []
uses: [homelab-agents]
cover_image: "/res/covers/do-agents-escape.jpg"
cover_alt: "Album-style cover: the words The Box Held beside a compact disc."
summary: "Sandboxing is the usual answer to 'is it safe to let an AI agent run commands?'. I built a deny-by-default box on my Mac, tried the obvious escapes by hand, and watched what the box stopped and what it quietly still allowed."
---

I run coding agents with real access to my machines. The standard reassurance is "it's {{< term "sandbox" "sandboxed" >}}". I wanted to know what that word actually buys, so I built a real sandbox on my Mac, put a {{< term "shell" "shell" >}} inside it, and tried the escapes an agent would try if it went off the rails or got {{< term "prompt-injection" "prompt-injected" >}} into trying.

Every escape I tried by hand hit the wall: my {{< term "ssh" >}} config, my home directory, my projects folder, the {{< term "keychain" "keychain" >}} and the network were all sealed off. That part is a real result, and a reassuring one.

The interesting part is the one allowance the shell needed just to start: looking up {{< term "daemon" "system services" >}} by name. It isn't a file and it isn't a {{< term "socket" "socket" >}}, so none of my tests touched it, and it leads to background services that aren't sandboxed at all. Nothing went wrong here. This is a write-up of a {{< term "latent-condition" "latent condition" >}}, in {{< term "incident-report" "incident-report" >}} form, because "the box held" and "the box is closed" turned out to be different sentences.

## Impact

- **What happened:** nothing escaped. No model has run in the box yet; every test was a shell command I typed. *(measured)*
- **What the box stops:** reads of my home directory, writes outside one working directory, and all network access. *(measured)*
- **What it still allows:** lookups of system services by name ("mach-lookup"), which a shell needs to run. Background services reachable that way sit outside the sandbox. *(inferred, from the profile and how {{< term "macos" >}} sandboxing works)*
- **How bad that is:** I don't know which of those services could be turned into a way out, and I didn't try. The exposure is a category, not a demonstrated escape. *(inferred)*

Severity: none realised. A real but unmeasured residual surface in a box that was otherwise tight.

## Timeline

| When (2026) | What happened | Evidence |
|---|---|---|
| Nov 6, early morning | {{< term "deny-by-default" "Deny-by-default" >}} sandbox profile written, plus a minimal harness to drive a local model inside it. | from my notes |
| Nov 6 | Hand smoke test of the profile, shell commands only, no model: every escape denied, the working directory writable. `mach-lookup` noted as allowed. | measured |
| Nov 6 | The tool I use to run agents refuses to auto-launch the model-driven escape run during an unattended work session. Not routed around. | from my notes |
| Nov 6 | Card re-scoped: the measured denials are the result; the model-driven run becomes an optional, supervised step. | from my notes |

## How it was found, and why not sooner

This one wasn't found by a failure. I went looking: the card was to find out what "sandboxed" buys. *(from my notes)*

The `mach-lookup` allowance was in the profile on purpose from the start, because the shell won't run without it. What it leads to was noted next to the smoke-test results, not found by any test. *(from my notes)* It was easy to under-weigh for a structural reason: every test I'd written was a file or network operation, because that's how I'd been thinking about escape. A test plan built around files and sockets can only find gaps in files and sockets. *(inferred)*

## What the evidence shows

**The profile.** macOS has a built-in sandbox mechanism, so I wrote a deny-by-default profile: nothing is allowed unless the profile says so. Then I opened the minimum an agent needs to do useful work:

- it can read most of the system (so tools work), **except** my home directory, the temp folders, and the private scratch areas,
- it can **write** only to one working directory, and
- it has **no network at all**.

The profile itself, with my paths shortened:

```scheme
(version 1)
(deny default)
(allow process-exec process-fork signal sysctl-read mach-lookup ipc-posix-shm iokit-open)
(allow file-read*)
(deny file-read* (subpath "/Users/<me>") (subpath "/private/tmp") (subpath "/private/var/folders"))
(allow file-read* (subpath "<work dir>"))
(allow file-read-metadata)
(allow file-write* (subpath "<work dir>") (literal "/dev/null") (literal "/dev/tty") (literal "/dev/dtracehelper"))
(deny network*)
```

*(from my notes)*

**The escape attempts.** Before wiring up a model, I played the adversary and ran the obvious escape moves as plain shell commands inside the box. I wanted to test the enforced boundary, not a model's willingness, so a person typing the worst commands on purpose is the stronger test.

| Attempt | Result |
|---|---|
| Read my SSH config (`~/.ssh/config`) | *Operation not permitted* |
| Fetch a web page over {{< term "http" "HTTPS" >}} | no connection at all |
| Write a file into my home directory | *Operation not permitted* |
| List my projects folder (`ls ~/WIP`) | *Operation not permitted* |
| Look up a secret in the keychain | not found: the keychain file itself is unreadable from inside |
| Write into the one allowed working directory | worked, as intended |

*(measured, Nov 6)*

**The allowance.** To let a shell even start, the profile has to allow one more thing: looking up system services by name ("mach-lookup"). The shell needs it to function, so it's allowed. *(measured: it's in the profile, and the shell runs)*

**The model-driven run.** I built a minimal agent that drives a local model through this same box on a set of escape-tempting tasks (read the SSH config, download a page, write to home, find {{< term "api-key" "API keys" >}}), logging every command and every denial. It hasn't run. *(from my notes)*

## Why it happened

**The file-and-network wall held because it's easy to reason about.** "Deny reads under this path" and "deny all network" are rules you can read and test one at a time. The tests matched the rules, and every one passed. A correctly written deny-by-default profile is not security theatre: it stops a process from reading your SSH keys even when the process is actively trying to. *(measured)*

**The residual surface exists because a working shell needs it.** Service lookup isn't optional decoration; without it nothing runs. So the minimum useful box necessarily includes it. *(inferred)*

**It leads somewhere the file rules don't.** The operating system is full of background services reachable through that lookup, and some of them do powerful things on your behalf. A sandbox that perfectly seals the filesystem and the network can still let a process talk to a daemon that isn't sandboxed at all, and that daemon becomes the way out. *(inferred)*

**The test plan had the same blind spot as the mental model.** I tested what I'd thought about. "This process may ask another, more privileged process to do things" isn't a file or a socket, so nothing in the plan exercised it. *(inferred)*

I didn't exploit this, and I'm not going to publish a map of which services are reachable.

## Findings, causes and contributing factors

1. The deny-by-default profile blocked every file and network escape I tried by hand.
2. The keychain was unreachable because its file couldn't be read, not because of any keychain-specific rule.
3. The profile allows service lookup ("mach-lookup"), which a shell needs to start.
4. Services reachable through that lookup run outside the sandbox.
5. None of my tests exercised that path, because all of them were file or network operations.
6. No model has been run in the box, so nothing here shows how a model would behave in it.

**Immediate cause (of the residual surface):** the minimum a shell needs to run includes access that isn't a file or a socket.

**Systemic cause:** a sandbox's real {{< term "attack-surface" "attack surface" >}} is the capabilities granted for the thing to run, and where they lead once they leave the box. Tests written against files and sockets don't measure that.

**Contributing factors:** file rules are easy to read and test, so they draw the attention; "this process may ask that one to act" is hard to enumerate, so it gets less.

## What went well, what went wrong, where I got lucky

**Went well:** the boundary was tested by hand with the worst commands, not by hoping a model wouldn't try them. Every file and network escape was denied. The model-driven run was refused when nobody was watching, and that refusal wasn't routed around.

**Went wrong:** the test plan only covered the kinds of escape I'd already been thinking about, so the most interesting allowance got no test at all.

**Got lucky:** nothing was at stake. This was a deliberate experiment in an empty working directory, not an agent doing real work behind a box I trusted.

## What I changed, and what's still open

Two things changed in how I run agents.

First, the file-and-network box is genuinely worth having. If an agent I'm running gets prompt-injected by something it reads, or just makes a bad call, a deny-by-default profile means it cannot read my keys or {{< term "exfiltration" "exfiltrate" >}} to the network, regardless of what it "decides" to do. That alone is worth the afternoon.

Second, I stopped treating "it's sandboxed" as a complete sentence. The honest version is "it's sandboxed against these specific things, here are the capabilities I had to leave open for it to work, and here's where I think those lead." For the agents that run against my {{< term "homelab" "homelab" >}}, that means the sandbox is one layer, not the layer: the account they use is still {{< term "least-privilege" "least-privilege" >}}, the network path is still restricted at the {{< term "firewall" "firewall" >}}, and the genuinely dangerous actions still route through me. The box is a seatbelt, not a reason to take my hands off the wheel.

Recommendations, for anyone sandboxing an agent:

- Use deny-by-default and test it by hand, with the commands you'd least want run.
- List every allowance you had to add just to make the process start, and ask where each one leads. Those, not the file rules, are the interesting surface.
- Don't let "sandboxed" replace least-privilege accounts, network restrictions, or a person approving the dangerous actions.

| Action | Type | Owner | Status |
|---|---|---|---|
| Deny-by-default profile: reads outside home, one writable directory, no network | prevent | me | done Nov 6 |
| Hand test of file, network and keychain escapes | detect | me | done Nov 6 |
| Treat the sandbox as one layer: least-privilege account, firewall, approval for dangerous actions | process | me | done in parts: least-privilege secrets identity Sep 4; permission rules that refuse dangerous actions without my yes Nov 9 *(inferred from my notes; the firewall part isn't dated)* |
| Model-driven escape run, supervised | detect | me | open |

The model-driven run waits for me to sit down and watch it. The tool I use to run agents refused to start a model instructed to attempt escapes while nobody was watching, and that refusal is correct: a model told to break out of a box, started unattended, is exactly the thing you supervise.

## Lessons

- **A sandbox's surface is what you had to allow, not what you denied.** The denials are the easy half.
- **Your tests share your blind spots.** If every test is a file or a socket, you'll only learn about files and sockets.
- **Test the wall, not the willingness.** A person typing the worst commands tells you what the boundary enforces; a model that didn't try tells you nothing about the boundary.
- **The supervision is part of the design.** The walls do their job; a person stays in the loop for the part no wall covers.
