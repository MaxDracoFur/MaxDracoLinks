---
title: "Buying used CDs in bulk: sixty dollars in a box of dimes"
search_phrase: "buying used CDs in bulk"
slug: "sixty-dollars-in-a-box-of-dimes"
url: "/blog/sixty-dollars-in-a-box-of-dimes"
layout: "blog/single"
date: 2026-11-15
draft: true
# Copy review (2026-11-12, card blog-cds-remarkable-find, session zero-r24-blog-drafts): Claude
# drafted this from the Blog pipeline outline, Max's 11-12 answers and his own sales/lot records.
# Second pass 2026-11-15 against the rules added since: search_phrase added and carried in the
# title; the three evidence labels rewritten as plain sentences (no-jargon rule); the grading
# section's open "verify in a browser" block resolved and a factual error in it corrected (see
# GRADING below); the link to an unwritten bootleg post removed; have/want figures re-read.
# Stays draft until Max reads it and approves. Nothing here publishes it.
# Max 11-12: "pull it rather than check my memory"; "only CDs" (no vinyl); "not black sabbath"
# (that one is the separate mis-ID post, card blog-cds-wrong-release-match). Find confirmed:
# John Morales, The M+M Mixes Volume IV. Source: Brown Elephant, Chicago (Max). Lot price
# deliberately UNSTATED: the sale (2025-12-10) predates every itemised lot.
# Evidence levels (MEASURED 2026-11-12, read-only from the arbitrage DB = his own Discogs
# history; no buyer or lot-seller columns used):
#   - 11,130 items sold since 2025-06-04; median $0.85; 10,576 (95%) under $5; 6,525 (59%) under
#     $1; 25 over $25.
#   - The find: Discogs release 11194232 (BBE BBE287CCD, 4xCD, UK, Dec 1 2017), sold 2025-12-10
#     for $60.00, no refund, buyer satisfied (no buyer data or message text in the post).
#     Discogs community: 344 have / 272 want, READ IN A BROWSER 2026-11-15 (unchanged since
#     11-12; this pair moves over time, so the post dates it).
#   - 39 lots, 14,573 discs, ~$7,547 (2026-01-01..2026-10-02). Thrift stores 22 / 1,120 / ~41c a
#     disc; music stores 14 / 481 / ~64c; individuals 2 / 3,525 / ~58c; biggest 3,500 for
#     $2,000; cheapest 668 for $24.52. His own opening stock (one "lot" of 9,447) left out.
#   - Scrap reasons: other 149, resurfaceable 61, duplicate 35, scratched 32, pirated 8,
#     destroyed 3, unplayable 1 (units.scrap_reason).
#   - Shelf time: FLOOR, not exact. Discogs `posted` moves on every reprice and the sale predates unit
#     tracking, so the listing date is bounded by listing-ID order: a higher-numbered listing sold
#     2025-06-04 (his first order), so Morales was listed by then; sold 2025-12-10 => at least ~6 months.
#     MEASURED 11-12 (Blog pipeline session).
# GRADING (READ IN A BROWSER 2026-11-15, both pages 200): Discogs "How To Grade Items"
#   https://support.discogs.com/hc/en-us/articles/360001566193-How-To-Grade-Items and Goldmine
#   "Record Grading 101" https://www.goldminemag.com/collector-resources/record-grading-101.
#   Discogs uses the Goldmine standard, community-extended for CDs. Full scale: Mint, Near Mint,
#   Very Good Plus, Very Good, Good/Good Plus, Poor/Fair. CORRECTION to the first draft, which
#   said the disc and its case are graded separately: Discogs states "Standard Jewel Cases are
#   not graded as they are replaceable" -- what is graded beside the disc is the insert, inlay,
#   booklet, sleeve or digipak. The percentage anchors (VG+ ~50% of Near Mint, VG ~25%, G 10-15%,
#   P 0-5%) are stated for VINYL in both sources and are NOT claimed for CDs here.
# Max 11-12 (round 4): buy rule "right now I'm setting it at 25 cents for a CD with case and 5 cents for
#   no-case CDs" (Max to confirm it's the buy price); lot figures ROUNDED; how he spotted it:
#   "it looked cool". Takeaways drafted from his rule + the numbers, for him to confirm.
# Persona: no LLC name, no seller names, no buyer data.
# COVER: still a CREATED graphic (2026-11-12), which the stage-photo rule no longer allows. The
#   set itself is sold, so a photo cover has to be the bins or a lot, tagged in Stage -- Max's call.
#   cover_source left unset deliberately: the approval gate should keep refusing until it is real.
review_status: "copy-review"
series: "cds"          # rotation area: security -> CDs -> travel -> events
introduces: []
uses: []
summary: "My median sale is 85 cents. The best CD I've found sold for $60: a four-disc disco box from a Chicago thrift shop. How bulk lots get bought, graded and priced, and what one find says about the rest of the bin."
cover_image: "/res/covers/sixty-dollars-in-a-box-of-dimes.jpg"
cover_alt: "Album-style cover: the words Sixty in the Dimes beside a compact disc."
# Card: blog-cds-remarkable-find
---

I sell used CDs on {{< term "discogs" >}}. Since June 2025 I've sold 11,130 items. The median sale is **85 cents**. Ninety-five out of every hundred went for under five dollars, and more than half went for under one.

The best CD I've found went for **$60**. It came out of a thrift shop in Chicago, and on the shelf it looked like nothing much.

## What a bulk lot is

I don't buy CDs one at a time. I buy them by the bin and the box: a thrift store's CD shelf, a music store's cull pile, someone clearing out a collection they've stopped playing. Nobody wants to price two thousand discs one by one, so the box gets a single price.

From my own records, 39 lots since the start of 2026 brought in about 14,600 discs for about $7,500 in all:

| Where from | Lots | Discs | About per disc |
|---|---:|---:|---:|
| Thrift stores | 22 | about 1,100 | about 40¢ |
| Music stores | 14 | about 500 | about 65¢ |
| Individuals | 2 | about 3,500 | about 60¢ |

The biggest was about 3,500 discs for about $2,000. The cheapest per disc was a box of about 670 for about $25, under four cents each.

The useful way to think about a box is that you aren't buying CDs. You're buying a distribution: hundreds of discs worth less than a dollar, a few dozen worth a few dollars, and, if you're lucky, one that pays for the box.

So how much is a box worth? What I pay right now is 25 cents for a CD that still has its case and 5 cents for one that doesn't. A disc without its case is a disc I have to re-case or sell for almost nothing, so it's worth a fifth as much to me going in.

## Grading is most of the price

Every disc that comes in gets {{< term "media-grading" "graded" >}} before it's listed. The scale isn't Discogs' own invention: it's the one *Goldmine* magazine wrote for records, which Discogs adopted and its sellers extended with definitions for CDs. It runs Mint, Near Mint, Very Good Plus, Very Good, Good or Good Plus, and Poor or Fair at the bottom. Grading is done by eye, not by playing the disc, so the rule among sellers is to grade low and let the buyer be pleasantly surprised.

Two things on a CD get a grade, and the jewel case isn't one of them. The disc gets one, and so do the printed parts: booklet, inlay, digipak. Discogs counts a standard jewel case as replaceable and doesn't grade it at all. That's why a cracked case costs me a few cents and a scratched disc costs me the sale.

Grade moves price more than anything except the title itself. A Very Good Plus copy of a common album sells. A scratched copy of the same album doesn't, at any price. A multi-disc set I grade on its worst piece, because that's what the buyer gets: one missing disc out of four turns a good sale into a refund.

Not everything makes it. Of the discs I've thrown out instead of listing since I started logging a reason, about half were "other". After that came 61 scratched badly enough that resurfacing might save them, 35 duplicates of stock already listed, 32 scratched past saving, and 8 that turned out to be counterfeit pressings.

## Pricing: the shape of the shelf

With a median of 85 cents, most of a lot earns its keep by volume, not by any one disc. Out of 11,130 sales, 25 went for more than $25. That's about one in 450.

A price comes from a few things: what the lowest comparable copy is listed for, the condition of mine against theirs, how many copies are for sale, and how many people want one. Discogs shows that last part directly. Members mark a release as one they have or one they want, and a title where the wants come close to the haves is one buyers are looking for.

## The find

*The M+M Mixes Volume IV* is a four-CD set of disco and boogie remixes by John Morales, who started out DJing in Bronx clubs in the 1970s and became one of the early makers of the extended mix. The UK label BBE put it out in December 2017, catalogue number BBE287CCD. It isn't a famous album, and nothing about a DJ-mix compilation says "valuable" to someone flicking through a bin of greatest-hits discs.

It came from [Brown Elephant](https://brownelephant.org/), a group of Chicago resale shops whose sales fund Howard Brown Health. Checking the release page today, 344 Discogs members have it and 272 want it. For a CD, that's a lot of people looking for a copy.

It sold on December 10, 2025, for $60, about seventy times my median sale. No return, no dispute, and the buyer was happy with it.

Why did I pick it up? Honestly, it looked cool. Not a price guide, not a phone app. A chunky four-disc box from a label I didn't know, in a bin of greatest-hits discs, and it looked like something somebody had cared about.

It wasn't a quick sale either. My listing records don't keep the exact date it went up, but they do show it was listed by early June 2025 at the latest, and it sold that December. It sat at least six months before the right buyer found it.

## What I'd tell someone buying their first box

- **Pay for the median, not the miracle.** At an 85-cent median, a box has to work at 25 cents a cased disc. The $60 find is a bonus, not the business plan.
- **Cases are most of the value going in.** A no-case disc is worth a fifth as much to me, 5 cents against 25, so count the cases before you count the titles.
- **Trust your eye on the odd ones.** The best thing I've found was the one that looked interesting: a box set on a small specialist label, not the famous album.
- **Be patient with the good ones.** My best CD sat for at least six months. A fair price on a wanted title waits for its buyer.
- **Budget for the discs that never sell.** Some are scratched, duplicated or fake, and they're part of what the box cost.

<!-- DICTIONARY: discogs and media-grading written 2026-11-15 (both draft: true, awaiting Max);
     first mentions linked by tools/dictionary.py link. "Bulk lot" is deliberately NOT a
     dictionary term: the post defines it in plain words in its own section, which is what the
     no-jargon rule asks for, and inventing an outside source for a trade phrase would be worse.
SOURCES (primary): Discogs release https://www.discogs.com/release/11194232 (have/want read in a
     browser 2026-11-15); Discogs "How To Grade Items" + Goldmine "Record Grading 101" (both read
     2026-11-15, see GRADING in the front matter); Brown Elephant's own site for the Howard Brown
     Health line. Sales/lot numbers: Max's own sales records, measured 2026-11-12.
     BBE's own product page for BBE287CCD was NOT reachable to check, so the catalogue number and
     release date come from the Discogs release page instead.
DISCOGS RULES: only Max's own sales/inventory, never another seller's data, no buyer names,
     usernames, locations or message text (memory feedback_discogs_customer_pii). -->
