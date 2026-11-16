---
title: "What I check before Furcago books a venue: its Public Place of Amusement licence"
search_phrase: "Public Place of Amusement"
slug: "venue-licence-check"
url: "/blog/venue-licence-check"
layout: "blog/single"
series: "furcago"
date: 2026-11-16
draft: true
# Cut from 1,670 words to this on 2026-11-15, after Max read the long version: "reads as someone
# who understands legal operations of running a local meetup where you haven't fully understood it,
# made assumptions, made me act like I know it and then try to sell it."
#
# What changed: it claims only what Max does (looks a venue up before booking), not what the law
# requires of a reader. The under-100 exemption is no longer explained as though it were settled --
# the post says plainly that he could not work out whose premises the sentence means. Gone: the
# evidence labels, "The trap in the capacity test", "The two-minute check", and the walkthrough of
# three exemptions, which was the part written in the voice of someone who knows.
#
# Still true and read at the source on 2026-11-13: the six people in violation and the $10,000
# (MCC 4-156-300(a)), that incidental use still counts (300(b)), that the definition of "amusement"
# names bowling and dancing (4-156-010), and the licence status codes from the city's own dataset
# description. Diversey River Bowl and the Music Box were both checked that day and both pass.
# MAX: cut anything that still sounds like me telling people the law.
# ON HOLD 2026-11-15, Max: "we should consult a lawyer before posting something like this,
# especially as this is connected to my llc." Not to be published until a lawyer has read it.
# Two reasons it matters more than it looked: anything describing what an ordinance requires,
# published by someone attached to an LLC, can read as the company giving advice; and the post
# names the exemption Furcago might itself rely on, which is a live question for that entity.
# Tracked on card furcago-liability-shield. Do not set draft: false.
review_status: "legal-hold"
introduces: [furcago]
cover_image: "/res/covers/venue-licence-check.jpg"
cover_source: "stage:outbox/maxdraco-furry/2025-06-14/2025-06-14-01.jpg"
cover_alt: "A fursuiter with arms spread outside the entrance of a bowling alley, under its neon BOWL sign."
summary: "Chicago can fine the organiser, not just the venue, when an event happens somewhere without an amusement licence. Here is the lookup I run before Furcago books anywhere, and the part of it I still can't answer."
---

I am not a lawyer. This is what I do before [Furcago](https://furcago.com/) books a room, and why.

A while back I went looking for what a meetup organiser is actually on the hook for in Chicago, and found something I had not expected. If entertainment happens at a place without the right licence, the city can fine the people who put the event on, not only the people who own the room. The section is [4-156-300(a)](https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2634203), and it lists six people who are in violation at once: the owner, whoever holds the lease, the manager, and the three that mean me, the producer, the presenter and the person conducting it. Each one can be fined up to $10,000.

The licence it wants is a **Public Place of Amusement** licence, which is Chicago's permit for a place where entertainment happens. "Amusement" is broader than it sounds: the [definition](https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2634034) names dancing and bowling outright, which is half of what we do. It applies even when entertainment is not the venue's main business.

So now I look the venue up first.

## Take a minute to look the venue up before you book it

Chicago publishes every business licence as a public table anyone can search, with no account.

1. Open the city's Business Licenses data and search the venue's name or street address.
2. Look for a row whose type is **Public Place of Amusement**.
3. Read the status and the expiry date on that row.

Step three is where I nearly fooled myself. The table keeps one row for every licence term going back years, and the status is a code rather than a word. The dataset's own description spells them out: `AAI` means the licence was issued, `AAC` means it was cancelled during its term. A venue can show a long history of Public Place of Amusement rows that are every one of them cancelled or expired. Look for `AAI` with an expiry still in the future.

When I ran it on the bowling alley on the cover, it came back with a live one that runs to November 2027. The Music Box Theatre holds four live licences at once, that one among them, into 2028.

## What I still can't answer

There is an exemption for small free events, under 100 people with nothing charged at the door. I can't tell you whether it would cover a Furcago night in the back room of a bar, because the sentence that defines the 100 counts "the premises of the business operating the amusement", and I don't know whether that means the bar or me. No lawyer has told me either way. So I treat it as unsettled rather than as cover.

## If you organise things too

- A missing row is not proof of anything. Public records lag in both directions, and the right next step is asking the venue, not posting about them. Getting that wrong in public can be defamation, and it can hurt a business that did nothing wrong.
- The table says which licences exist. It doesn't say what a licence allows, what the room's legal capacity is, or whether selling tickets pulls in the city's amusement tax, which is a separate thing again.
- I only name venues here that I checked and that came back licensed.

All of this is me reading the rules that apply to me, on 13 November 2026, and telling you what I do about them. It isn't legal advice and I'm not qualified to give you any. If there's a deposit or a contract in it, ask someone who is.

<!-- MAX, optional: a closing line telling other organisers where to ask you. -->
