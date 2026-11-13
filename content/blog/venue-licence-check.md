---
title: "Check the venue's Public Place of Amusement licence before your meetup books it"
search_phrase: "Public Place of Amusement"
slug: "venue-licence-check"
url: "/blog/venue-licence-check"
layout: "blog/single"
series: "furcago"
# Rotation (Max 11-13: Cyber, CDs, Furry, repeat): the Furry slot after the CD post.
# Placeholder date: Max picks the real one.
date: 2026-12-24
draft: true
# Rewritten 2026-11-13 from the 11-04 draft, to the quality bar: payoff first, length to match.
# EVERY legal claim re-read at the primary source on 2026-11-13, in a browser (the code library
# blocks automated fetches): Municipal Code of Chicago 4-156-010 (definition of "amusement"),
# 4-156-300(a),(b) and 4-156-305(c),(d),(g) and its closing paragraph, at
# codelibrary.amlegal.com/codes/chicago/latest/chicago_il/ (0-0-0-2634034 and 0-0-0-2634203).
# Licence data measured 2026-11-13 from data.cityofchicago.org dataset r5kz-chrr, whose own
# description defines the status codes: AAI issued, AAC cancelled during term, REV revoked.
# Two things the earlier draft missed, both now in the post: the capacity test counts EVERY room
# of the premises, and a cancelled licence still shows in the data unless you filter on status.
# REVIEW FLAGS for Max:
#  - Only venues that PASS are named: Diversey River Bowl (PPA to 2027-11-15) and the Music Box
#    (PPA to 2028-06-15), both checked 11-13. Don't add one without re-checking it.
#  - The intro needs a line or two from you on what Furcago is: this post introduces it.
#  - COVER: is that your suit outside the bowling alley? If it's someone else's, say and I'll swap
#    the photo. Number plates and faces are cropped out; the venue is named in the post anyway.
#  - You built a tool for this check; the post describes the manual steps instead. Say if you want
#    it mentioned, and whether it is public.
#  - Not legal advice: that line stays.
review_status: "copy-review"
introduces: [furcago]
cover_image: "/res/covers/venue-licence-check.jpg"
cover_source: "stage:outbox/maxdraco-furry/2025-06-14/2025-06-14-01.jpg"
cover_alt: "A fursuiter with arms spread outside the entrance of a bowling alley, under its neon BOWL sign."
summary: "In Chicago, if the venue your meetup books has no Public Place of Amusement licence, the organizer can be fined too. The lookup takes two minutes, and the city's own data has a trap in it."
---

<!-- MAX: one or two lines on what Furcago is, in your words. This post introduces it to
     maxdraco.com readers, so later posts can lean on it. -->

I run Furcago, a Chicago furry meetup group. Most of what we do is ordinary: bowling, a bar night, a movie. Before booking any of it I check one thing, and almost no organizer I've asked has heard of it: whether the venue holds a **Public Place of Amusement** licence. If it doesn't, the city can fine the organizer, not just the venue. *(my account)*

The check takes about two minutes against the city's own public data, and there's a trap in that data that will tell you a venue is fine when it isn't.

## Why the organizer is on the hook

Chicago's Municipal Code says that if an amusement happens somewhere without that licence, six different people are in violation at once: the owner of the property, the lessee, the manager, **the producer of the amusement, the presenter of it, and the person conducting it**. Each one "shall be subject to a fine of up to $10,000.00". *(measured 11-13, [§ 4-156-300(a)](https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2634203))*

For a meetup, the last three are the organizer. You don't have to own the room to be on that list.

It also doesn't matter that amusement isn't what the venue mainly does. The licence is required "regardless of whether the use is incidental to the property's principal use". *(measured 11-13, § 4-156-300(b))*

## "Amusement" is broader than it sounds

The code's definition runs to three paragraphs and names, among much else, dancing, bowling, billiards, pool, skating, swimming, motion picture shows, musical performances and "any entertainment or recreational activity offered for public participation or on a membership or other basis". *(measured 11-13, [§ 4-156-010](https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2634034))*

Read that list against a normal furry meetup calendar. Bowling is on it by name. So is dancing. So is a movie.

## The exceptions that actually help

Three of them cover a lot of small events. All are in [§ 4-156-305](https://codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2634203). *(measured 11-13)*

- **(c) Small and free.** Music, dancing or other amusement needs no licence if the venue's capacity is under 100 **and** there is no admission fee, minimum purchase, membership fee "or other fee or charge" to get in.
- **(d) A private event at a restaurant.** Live or recorded music and dancing at a banquet hall or restaurant that holds a retail food licence, at an event "not open or advertised to the general public", with no charge to get in. The code's own examples are a wedding, a graduation, a religious celebration.
- **(g) A private club or lodge.** For members and their guests only, on premises it owns or leases for at least two years, where the club is a not-for-profit that has existed three years or more and has more than 50 members paying dues on a regular basis. Dues collected at the door don't count.

A public meetup announced online is not "not advertised to the general public". And a ticket of any size, or a door charge, or a required minimum spend, knocks out (c) and (d) on its own.

## The trap in the capacity test

This is the part I'd have got wrong. The capacity in exception (c) is not the capacity of your room. The last line of § 4-156-305 says that when working out whether a venue holds more than 100 people, "the total occupancy of all rooms or other occupancy areas of the premises of the business operating the amusement shall be calculated". *(measured 11-13)*

So the back room of a bar that seats 40 doesn't get you the exception if the bar as a whole holds 150.

## The two-minute check

Chicago publishes every business licence as open data, and you can search it by name or address without an account or an {{< term "api" "API" >}} key.

1. Open the city's Business Licenses dataset and search the venue's name or street address.
2. Look for a row whose licence type is **Public Place of Amusement**.
3. **Check the status and the expiry on that row**, which is where people get caught out. See below.

**The trap:** the dataset holds one row per licence *term*, going back years, and the status column is a code. The dataset's own description defines them: `AAI` means the licence was issued, `AAC` means it "was cancelled during its term", `REV` revoked, `REA` revocation appealed. A venue can show a long history of Public Place of Amusement rows that are every one of them cancelled or expired. Filter for `AAI` with an expiry date in the future, or you'll read a dead licence as a live one. *(measured 11-13)*

When I ran it on the bowling alley on the cover, Diversey River Bowl, it came back with a live Public Place of Amusement licence that runs to 15 November 2027. The Music Box Theatre holds four live licences at once, Public Place of Amusement among them, to 15 June 2028. *(measured 11-13)*

<!-- MAX: say how you actually run it (you built a small tool) or keep the manual steps above.
     Don't name venues that came back without a licence. -->

## What the check can't tell you

The city's table says which licences exist. It doesn't say what a licence's plan of operation allows, and it doesn't give you the room's occupancy, which is the number on the venue's posted occupancy sign and isn't published anywhere. Selling tickets can also bring Chicago's amusement tax into it, which is a separate question from the licence.

So treat the lookup as a first screen. The real check is still asking the venue directly, before anyone pays a deposit.

*This is general information from reading the ordinance, not legal advice.*

<!-- MAX: closing line / where other organizers can ask you about it. -->
