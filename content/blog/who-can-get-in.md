---
title: "Who else can get into my home network? Counting it for Tailscale, ZeroTier, Cloudflare Tunnel and plain WireGuard"
slug: "who-can-get-in"
url: "/blog/who-can-get-in"
layout: "blog/single"
series: "hacker"
date: 2026-11-12T07:45:00-06:00
draft: false
review_status: "approved"
cover_image: "/res/covers/who-can-get-in.jpg"
cover_alt: "Album-style cover: the words Who Else beside a compact disc."
summary: "Every remote-access product says it's secure. I asked a narrower question: other than me, who can add a way into my house? For three popular options the answer is two companies. For the boring one, it's nobody."
---

When I wanted to reach my {{< term "homelab" "homelab" >}} from outside, the usual advice was "just use {{< term "tailscale" >}}." I said no, and later I said no to {{< term "cloudflare" >}} Tunnel for the same reason. This is the check on that reasoning, written up the way {{< term "incident-report" "incident reports" >}} are. Nothing broke. The thing under investigation is a condition: who, other than me, holds the power to add a new way into my house?

That's not the same as "is it {{< term "encryption" "encrypted" >}}." All four designs I compared encrypt. For Tailscale, {{< term "zerotier" >}}'s hosted controller and {{< term "cloudflare-tunnel" >}}, two parties besides me can open a door: the vendor and whoever controls my login. For plain {{< term "wireguard" >}} on my own {{< term "router" "router" >}}, it's nobody. I tested the claim people doubt most, that an open WireGuard port can't be {{< term "port-scanning" "found by a scanner" >}}, from outside my network. It can't: the {{< term "network-port" "open port" >}} answered junk with exactly the same silence as two closed ones.

The investigation also turned up the one exposure no {{< term "vpn" >}} choice closes. A gadget on my own network was holding a {{< term "tunnel" "vendor tunnel" >}} open to its maker's cloud, and nothing was looking at {{< term "egress-filtering" "outbound traffic" >}} until I started logging it. That tunnel is off now.

## Impact

- **For the three hosted designs:** two parties besides me could add a way in. For Cloudflare Tunnel, one of them also reads the traffic. *(inferred, from vendor docs checked 11-06)*
- **For plain WireGuard as I run it:** no party besides me can add a way in. What remains are availability risks: my {{< term "dns" >}} provider could lock me out, and so could the router hanging, which it did several times in September. *(inferred; the hangs are from my notes and the router's logs)*
- **The real exposure found:** a {{< term "kvm-over-ip" "remote-console" >}} gadget on the {{< term "lan" >}} held a steady connection to its maker's cloud, with a vendor tunnel built in. How long it had been doing that before outbound logging began isn't known. *(measured when found; the start is unknown)*
- **What wasn't affected:** I found no sign that anyone used any of these paths. The scanner-facing side showed nothing open. *(measured)*

Severity: a design question for most of it, and one latent {{< term "backdoor" "back door" >}} that was closed once it was visible.

## Timeline

| When (2026) | What happened | Evidence |
|---|---|---|
| Sep | Decided: no external company as a way into the house. | from my notes |
| Oct 28 | Broadened the rule to tunnels used for publishing, which ruled out Cloudflare Tunnel too. | from my notes; date inferred (the rule's change is dated Oct 28 in my notes) |
| Oct 28 | Outbound (LAN to internet) logging switched on. | from my notes |
| Oct 29 | The remote-console gadget found holding a vendor-cloud connection, in the router's table of open connections. | from my notes; date inferred (the note and the to-do item opened that morning agree) |
| Oct 30 | The gadget's vendor tunnel shut off. | from my notes |
| Nov 5 | Wrote the matrix of who can get in, one row per party. | from my notes |
| Nov 6 | Checked the vendor claims against each vendor's own docs. | from my notes |
| Nov 6 | Full sweep of every {{< term "tcp" >}} port on my {{< term "ip-address" "home address" >}} from outside: nothing open. | from my notes |
| Nov 6 | Targeted probe from outside (below), run twice with the same result. | measured |
| Nov 6 | A separate investigation into the router hangs closes: they matched a {{< term "usb" "USB" >}} network adapter, removed Sep 15, with none since. | inferred (router logs) |

## How it was found, and why not sooner

The investigation started from the advice itself. "Just use Tailscale" answers a different question from the one I cared about, so I wrote mine down and graded each design against it. *(from my notes)*

The gadget is the part that matters for detection. It went unseen because the network only watched what came in. A tunnel that dials out on port 443 looks like any other web traffic, and before October 28 nothing logged outbound connections at all. "Outbound-only" products are invisible to an inbound {{< term "firewall" "firewall" >}} by design, and this one was no exception. *(inferred)*

## What the evidence shows

**The four designs.**

- **Tailscale.** WireGuard underneath, plus a hosted {{< term "control-plane" "coordination service" >}} that tells your devices about each other. You log in with {{< term "google" >}}, {{< term "github" >}}, Microsoft and so on.
- **ZeroTier.** Its own encrypted network, with a controller that decides which devices are members. Most people use ZeroTier's hosted controller.
- **Cloudflare Tunnel.** A small program inside your network dials out to Cloudflare. {{< term "edge-network" "Cloudflare's edge" >}} accepts visitors and forwards their requests down the tunnel. It's a reverse {{< term "proxy" "proxy" >}}, not a VPN.
- **Plain WireGuard on my own router.** One {{< term "udp" "UDP" >}} port open. The router holds a short list of device {{< term "public-key-cryptography" "public keys" >}}. There's no account, no login and no company in the path.

*(vendor designs from each vendor's docs, checked 11-06; my own setup from my notes)*

**What the vendor docs say.** Tailnet Lock, when on, means a new device has to be signed by a key on one of your own devices. It's off by default, needs at least two signing devices, and trusts whatever state it sees first. ZeroTier's controller {{< term "authentication" "authorizes" >}} members, and {{< term "self-hosting" "self-hosting" >}} the controller is supported. Cloudflare's edge makes one encrypted connection to the visitor and a second one to you, so it terminates {{< term "tls" "TLS" >}} and the requests are readable in the middle. *(from vendor docs, checked 11-06)*

**The matrix.** `yes` = can get onto the network. `no` = can't, by design. `lock-out` = can stop me getting in, but can't get in themselves.

| Who | Tailscale | ZeroTier (hosted) | Cloudflare Tunnel | Plain WireGuard |
|---|---|---|---|---|
| Someone who {{< term "phishing" "phishes" >}} my Google/GitHub login | yes: log in, add a device | yes: log in, approve a device | yes: change the access policy or add a hostname | no: there's no login |
| The vendor (insider, breach, court order) | yes, unless Tailnet Lock is on | yes: their controller approves members | yes, and they see the traffic unencrypted | no: there's no vendor |
| Internet scanners | no | no | they can find the public hostnames on Cloudflare's edge | no (measured, below) |
| My DNS provider | not involved | not involved | not involved | lock-out only: a fake address leads to a host that can't complete the {{< term "handshake" "handshake" >}} |
| Someone who steals my unlocked laptop | yes, until I remove it | yes, until I remove it | yes, until the session expires | yes, until I delete its key |
| {{< term "malware" >}} already on a device at home | can install any of these and dial out | same | same | can't open a WireGuard door, but can dial out with any of the others |
| Whoever controls my router | yes | yes | yes | yes |

*(inferred from the vendor docs and my config; the scanner row for WireGuard is measured)*

**The probe.** From a machine outside my network I probed my home address on the common TCP ports ({{< term "ssh" >}}, web, {{< term "plex" "Plex" >}}, the WireGuard port itself). None answered. Then I sent 148 bytes of random junk to three UDP ports: the open WireGuard port and two closed ones. All three sent back **zero bytes**. *(measured 11-06, run twice)*

A full sweep of every TCP port a few hours earlier found nothing open. *(from my notes)*

The probe has to run from outside. From inside the network you'd be testing the router's hairpin {{< term "nat" "NAT" >}}, not what the internet sees. A non-zero UDP reply, or any open TCP port, would have been the finding.

**My setup's costs.** No {{< term "single-sign-on" "single sign-on" >}} and no {{< term "two-factor-authentication" "MFA" >}} prompt: the key lives on the device. Adding a device means making a key, adding it to the router and writing its rules by hand. The router hard-hung several times in September, until a USB network adapter it depended on came out. My home address changes, so a {{< term "dynamic-dns" "dynamic DNS" >}} hostname points at it. *(from my notes)*

**What limits the damage.** Each device has a short {{< term "allowlist" "allowlist" >}} (my phone can reach two things, not the whole network), and alerts fire when a device connects from outside or when one key shows up from two places at once. *(from my notes)*

## Why it happened

**"Outbound-only" describes the handshake, not the trust boundary.** Tailscale, ZeroTier and Cloudflare Tunnel all sell the same feature: no inbound port, because your side dials out. That's true. It's also exactly why the firewall can't see them as a door. The door still exists. It's opened from the vendor's side, so the real question for each is who can tell the vendor to open it. *(inferred)*

**Each hosted design adds two keyholders.** The vendor runs the part that decides membership, and the vendor trusts my login provider to say it's me. Either one, breached or compelled, can add a device. Tailnet Lock removes the vendor from Tailscale's row, but it's off by default, and the login provider stays in. Self-hosting the control plane ({{< term "headscale" >}} for Tailscale {{< term "client" "clients" >}}, or your own ZeroTier controller) removes the vendor too, and puts a new internet-facing service in its place, which is the thing these products were meant to save you from. *(inferred)*

**Cloudflare Tunnel is a different kind of thing.** It's a reverse proxy. Reading the requests in the middle is how its caching and filtering work, so the vendor isn't just a keyholder, it's in the traffic. That's the strongest single argument in the table. *(inferred, from vendor docs)*

**WireGuard's open port isn't something a scanner can find.** It doesn't reply to anything that isn't a valid handshake from a key it already knows. No banner to fingerprint, no login prompt to guess at. The probe showed exactly that. *(measured)*

**Why the gadget's tunnel stayed open.** Look at "malware already on a device at home" again. Any program that can reach the internet on port 443 can run its own tunnel with any of these products. My choice of VPN doesn't touch that row. The gadget shipped with one built in, and until outbound traffic was logged there was no signal to see it by. *(inferred; the gadget's tunnel measured when found)*

One thing that cuts the other way: the router I chose to trust is also a {{< term "single-point-of-failure" "single point of failure" >}}. It hung several times in September, and when it did nobody got in, me included. That cost me more remote access than any vendor outage has. The hangs stopped when I took out a USB network adapter on September 15: none in the 50 days after, against about one a day before. *(the hangs and the 50 quiet days from the router's logs; the cause and the comparison inferred)*

## Findings, causes and contributing factors

1. Tailscale, hosted ZeroTier and Cloudflare Tunnel each give two non-me parties (the vendor and the login provider) the power to add a way in. Tailscale drops to one with Tailnet Lock on.
2. Cloudflare Tunnel's vendor also reads every request.
3. Plain WireGuard on my router gives that power to nobody but me. The DNS provider can only lock me out.
4. The open WireGuard port is indistinguishable from a closed one to a scanner.
5. The router is the single point of trust and of failure for every design, including mine.
6. A device already inside the network can open an outbound tunnel with any of these products, whatever I run for remote access.
7. A gadget on the LAN was doing exactly that, and stayed unseen until outbound logging began.

**Immediate cause (of the one real exposure):** a gadget shipped with a vendor tunnel enabled, dialing out over ordinary web traffic.

**Systemic causes:** the network's defences faced inward. Outbound connections weren't logged or limited, so a door opened from inside had no signal. And hosted remote-access products place the decision about who gets in outside the house, behind a login and a company.

**Contributing factors:** "outbound-only, no open ports" is marketed as the safe property, which makes these doors easy to overlook; Tailnet Lock is off by default; self-hosting swaps a vendor for a new service to defend.

## What went well, what went wrong, where I got lucky

**Went well:** the question was narrow enough to answer. The claim people doubt most was measured from outside, twice, rather than assumed. Vendor claims were checked against the vendors' own docs before going in the table.

**Went wrong:** outbound traffic wasn't logged until late October, so a vendor tunnel from inside the house had nothing to show up in. The router I depend on hung several times in September.

**Got lucky:** the gadget was found as soon as outbound logging started, not by something using it. The hangs cost access, not security: a hung router lets nobody in.

## What I changed, and what's still open

Recommendations:

- **If you use Tailscale:** turn Tailnet Lock on. It takes the vendor out of that row. Your login provider is still in it.
- **If you run anything at home:** log outbound connections, and limit what can leave. That's the only control in this post that covers the row every design shares.
- **If you're choosing:** ask "who besides me can let someone in," not "is it encrypted." All four pass the second question.

| Action | Type | Owner | Status |
|---|---|---|---|
| Plain WireGuard on my own router; no external company as a way in | prevent | me | done (Sep, broadened Oct) |
| Short allowlist per device | mitigate | me | done |
| Alerts on a device connecting from outside, and on one key seen from two places | detect | me | done |
| Log outbound (LAN to internet) traffic | detect | me | done Oct 28 |
| Turn off the gadget's vendor tunnel; keep the outbound block as a backstop | mitigate | me | done Oct 30 |
| Off-LAN probe of the open port | detect | me | done Nov 6 |
| Router hangs: the single point of failure | mitigate | me | done Sep 15 (USB network adapter removed); cause confirmed Nov 6 *(inferred)* |

The router is still one box. The hangs are fixed; the single point of failure isn't, and every design in this post shares it. *(inferred)*

## Lessons

- **Count keyholders, not ciphers.** Encryption tells you who can read the traffic. It doesn't tell you who can add a door.
- **"Outbound-only" moves the door, it doesn't remove it.** If your firewall can't see it, find out who can.
- **Watch what leaves.** The one real back door here came from inside, and no remote-access choice would have closed it.
- **Picking the boring option moves the risk onto you.** I accepted that the router is my problem. It is.
