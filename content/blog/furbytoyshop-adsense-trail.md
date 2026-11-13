---
title: "A Furby fan site, a Mayan ruins guide, and one ad account"
slug: "furbytoyshop-adsense-trail"
url: "/blog/furbytoyshop-adsense-trail"
layout: "blog/single"
series: "hacker"
date: 2026-11-12T07:00:00-06:00
draft: false
review_status: "approved"
introduces: []
uses: []
cover_image: "/res/covers/furbytoyshop-adsense-trail.jpg"
cover_source: "stage:outbox/maxdraco-hack/2025-06-14/2025-06-14-01.jpg"
cover_alt: "Max at a hacker conference table under a towering stack of tinfoil hats, face covered by a dragon sticker."
summary: "Two unrelated hobby sites, one shared AdSense account. Here's how a public ID in page source ties sites together, and what a domain's history in the Wayback Machine says about who owns it now."
---

On a Friday night I put an {{< term "ai" >}} {{< term "llm" "chatbot" >}} on the witness stand. The subject was the {{< term "furry-fandom" "furry fandom" >}}, and the only question I cared about was where it was getting its answers. It wanted to keep talking; I wanted citations. When it finally produced a list, one of them was {{< term "furscience" >}}, a real research group that studies the fandom. Next to it was a Furby site. A site about the toy, testifying on furries. That's when I stopped cross-examining the machine and started cross-examining its sources. *(my account)*

Every site that runs {{< term "google" >}} {{< term "google-adsense" "AdSense" >}} puts its publisher ID in the {{< term "page-source" "page source" >}}. It looks like `ca-pub-` followed by sixteen digits, and it identifies the account that gets paid. Sites run by unrelated people don't share one. When two sites with nothing in common carry the same ID, they're paid out to the same account.

A Furby fan site and a travel guide to Mayan ruins carry the same one. Both {{< term "domain" "domains" >}} are years older than that ID: the {{< term "wayback-machine" "Wayback Machine" >}} shows each changing its {{< term "google-analytics" "tracking IDs" >}} at some point, which is what a change of hands looks like from the outside. Nothing here is a break-in, and none of it names a person. It's what anyone can read in public page source, with a date on each piece. This is written up the way {{< term "incident-report" "incident reports" >}} are, because the interesting part isn't these two sites. It's that the trail exists at all, for every site that runs ads.

## Impact

- **What's exposed:** the link between two sites that look unrelated. One public ID in page source says they're paid to the same account. *(measured 11-05)*
- **What else is exposed:** each domain's history. Old snapshots show which analytics and ad accounts the site used before, so a change of account shows up as a change of hands. *(measured 11-05, from Wayback snapshots)*
- **What it doesn't show:** who runs the account. The ID links sites to each other, not to a person, and this post names no one. *(inferred)*
- **Scale:** two sites confirmed here. When I first looked, in April 2025, a {{< term "reverse-lookup" "third-party lookup" >}} listed about seven sites under the ID. *(my recollection; my notes keep the lookup, not the list)* An ordinary web search doesn't index the ID at all, so the rest are unconfirmed. *(measured 11-12 for the two; the search result measured 11-12)*

Severity: none of this is a {{< term "vulnerability" "vulnerability" >}}. It's a property of how ad accounts work, and it applies to every site that runs ads.

## Timeline

| When | What happened | Evidence |
|---|---|---|
| 2010 | mayan-ruins.org first archived by the Wayback Machine: a one-line stub about Mayan ruins in Mexico. | measured ([snapshot, Jun 13 2010](https://web.archive.org/web/20100613014730/http://mayan-ruins.org/)) |
| 2012 to 2018 | furbytoyshop.com registered. "Buy Furbies Online at the Furby Toy Shop", a {{< term "wordpress" >}} shop, analytics ID `UA-5544598-8`. From 2017 it also runs its own AdSense account, `ca-pub-7095585455738924`. Last seen in May 2018. | measured ([Dec 2012](https://web.archive.org/web/20121210195558/http://furbytoyshop.com/), [Mar 2017](https://web.archive.org/web/20170325085832/http://furbytoyshop.com/), [May 2018](https://web.archive.org/web/20180509181558/http://furbytoyshop.com/) snapshots) |
| 2018 | mayan-ruins.org runs AdSense account `ca-pub-4180982658471453`, still there in January 2019. | measured ([Feb 2018](https://web.archive.org/web/20180207223633/http://www.mayan-ruins.org/), [Jan 2019](https://web.archive.org/web/20190119151011/http://www.mayan-ruins.org/) snapshots) |
| Late 2018 to Feb 2025 | furbytoyshop.com is "Best Furby Toys", with a different analytics ID (`UA-125743358-1`) and no AdSense. The change happened between May and November 2018. | measured ([Nov 2018](https://web.archive.org/web/20181112200117/http://furbytoyshop.com/), [Feb 2025](https://web.archive.org/web/20250213200241/https://furbytoyshop.com/) snapshots) |
| Feb 2019 | mayan-ruins.org is a registrar's parked page. | measured ([snapshot](https://web.archive.org/web/20190212185434/http://www.mayan-ruins.org/)) |
| By Feb 2021 | mayan-ruins.org is back, with new content and `ca-pub-8865241261618143`. | measured ([snapshot, Feb 22 2021](https://web.archive.org/web/20210222065111/http://www.mayan-ruins.org/)) |
| By Mar 2025 | furbytoyshop.com retitled "Best Furby Toy Reviews", with `ca-pub-8865241261618143`. | measured ([snapshot, Mar 17 2025](https://web.archive.org/web/20250317123926/https://furbytoyshop.com/)); I saw it on the live site in April (from my notes) |
| Apr 2025 | My first look at the two sites and the shared ID. | from my notes |
| Nov 5, 2026 | Live pages and history re-checked. Both sites still carry the shared ID; furbytoyshop.com now has a GA4 tag as well. | measured |

## How it was found, and why not sooner

An AI answer put it in front of me, cited as a source on the furry fandom next to actual research. A Furby review site has no business in that list, so I went and looked at what it actually was. *(my account)*

This section is mostly about the reader's side: the ID was always there. Nobody has to dig for it. It sits in the source of every page that serves an ad, and the Wayback Machine has kept dated copies for years. It goes unnoticed because nobody reads page source for fun, and an ad ID looks like noise. *(inferred)*

## What the evidence shows

**Two sites, one account.** As of November 2026:

| Site | Topic | AdSense publisher ID |
|---|---|---|
| furbytoyshop.com | Furby guides and reviews | `ca-pub-8865241261618143` |
| mayan-ruins.org | Travel guide to Mayan ruins | `ca-pub-8865241261618143` |

*(measured 11-05, live page source)*

{{< shot src="/res/furbytoyshop/furbytoyshop-2026.webp" alt="The furbytoyshop.com homepage: Furby Toy Shop, A little Furby. A lot to discover." caption="furbytoyshop.com, Nov 12, 2026 (screenshot)" >}}

{{< shot src="/res/furbytoyshop/mayan-ruins-2026.webp" alt="The mayan-ruins.org homepage: Discover the Maya world, over a photo of a stepped pyramid." caption="mayan-ruins.org, Nov 12, 2026 (screenshot). Same publisher ID as the Furby site." >}}

**Checked again, Nov 12.** furbytoyshop.com now also publishes the ID in its {{< term "ads-txt" "ads.txt" >}} file, the public list of who may sell its ad space: `google.com, pub-8865241261618143, DIRECT`. The Wayback Machine has that line by [July 2025](https://web.archive.org/web/20250717203412/https://furbytoyshop.com/ads.txt). mayan-ruins.org has no `ads.txt` line for it; the ID sits in the ad code on its pages. *(measured 11-12)*

{{< shot src="/res/furbytoyshop/furbytoyshop-ads-txt.webp" alt="One line of text: google.com, pub-8865241261618143, DIRECT, f08c47fec0942fa0" caption="furbytoyshop.com/ads.txt, Nov 12, 2026 (screenshot, enlarged)" >}}

**Did the traffic go up?** That was my hypothesis. What I'd seen was the Internet Archive's own record of the site: it was saving the Furby homepage far more often than it used to. Here's what that record says, counted as days with at least one saved copy of the homepage: *(measured 11-12, Wayback CDX: `web.archive.org/cdx/search/cdx?url=<site>/&collapse=timestamp:8`)*

| Year | furbytoyshop.com | mayan-ruins.org |
|---|---|---|
| 2019 | 7 | 5 |
| 2020 | 3 | 1 |
| 2021 | 8 | 3 |
| 2022 | 4 | 3 |
| 2023 | 3 | 3 |
| 2024 | 12 | 3 |
| 2025 | 22 | 9 |
| 2026, to Nov 12 | 17 | 6 |

What that shows, and what it doesn't:

- **These are crawler visits, not people.** A capture is the archive's robot deciding to save a copy. It says nothing about how many humans read the page.
- **The rise started in 2024,** a year before the early-2025 change of content. Whatever drove it, it wasn't the new content alone.
- **The Mayan site rose too,** from 3 a year to 9 in 2025, with no change of its own. That looks like the archive crawling more, not the Furby site getting popular.
- **The public traffic lists can't settle it either.** Neither site is in the {{< term "tranco" "Tranco" >}} list of the top million sites, in lists from before or after the change, and Google's real-user Chrome data has no entry for the Furby site. Both are too small to show up. *(measured 11-12: Tranco lists of Jan 15, Jun 15 and Nov 15 2025 and Nov 11 2026; PageSpeed Insights field data)*

So the honest answer is: I don't know if more people read it. The thing I took for a traffic signal turned out to be a crawler signal, which is the same lesson as the rest of this post. Check what the evidence actually measures before you lean on it.

**What else the Furby site runs.** Besides the ads: {{< term "affiliate-link" "Amazon affiliate" >}} links, Google Analytics, and two {{< term "session-recording" "session-recording" >}} and heatmap services that watch how visitors move around the page. *(measured 11-12, page source)* That seems like a lot of measurement for a site of toy reviews. *(my opinion)*

**The address in the footer.** The site's footer lists an "Our location" street address. It's a unit in a shopping plaza in Virginia that public listings attribute to other businesses. *(measured 11-12)* I'm not drawing a conclusion from that beyond the obvious one: a site's own claims about itself are worth checking too.

**The other sites.** When I first looked, a third-party lookup listed about seven sites under this ID. *(my recollection)* I didn't keep the list, and I'm only counting a site here if its own page source shows the ID. So I searched for every unique thing the two sites carry: the publisher ID with and without its prefix, the `ads.txt` line, the Furby site's other tracking IDs, the Mayan site's theme name, and each site's footer slogan. None of it turned up any other site carrying the ID. A couple of sites with similar slogans came up, and neither has the ID in its source. *(measured 11-12)* So two are confirmed, and the rest stay unconfirmed. Finding them again would take one of the paid indexes that store which IDs sit on which pages, and I'm not using those here.


**furbytoyshop.com's history** (registered 2012):

- **2012 to 2018:** "Buy Furbies Online at the Furby Toy Shop", a WordPress shop with Google Analytics ID `UA-5544598-8`, and from 2017 its own AdSense account, `ca-pub-7095585455738924`.
- **Late 2018 to February 2025:** "Best Furby Toys", a different analytics ID (`UA-125743358-1`), no AdSense.
- **By March 2025:** retitled "Best Furby Toy Reviews", with `ca-pub-8865241261618143`. It was on the live site when I first looked in April. It's still there today, now with a GA4 tag as well.

*(measured 11-12 from the Wayback snapshots in the timeline, and the live page; the April sighting from my notes)*

{{< shot src="/res/furbytoyshop/furbytoyshop-2018-wayback.webp" alt="The Wayback Machine's copy of furbytoyshop.com from January 3, 2018: a Furby Toy Shop banner and rows of Furby toys." caption="furbytoyshop.com as the Wayback Machine saved it on [Jan 3, 2018](https://web.archive.org/web/20180103133559/http://furbytoyshop.com/), before the change of hands (screenshot)" >}}

**mayan-ruins.org's history** (archived since 2010):

- **2018:** AdSense account `ca-pub-4180982658471453`, still there in January 2019.
- **February 2019:** a registrar's parked page, the kind a domain shows when nobody is running a site on it.
- **By February 2021:** back with new content and a different account, `ca-pub-8865241261618143`, which it still uses today.

*(measured 11-05, Wayback snapshots and the live page)*

**The content.** In my view, the current site reads like generated filler: guide-shaped text with nothing behind it. A typical line from the homepage: "Match the generation first: colours alone do not identify the features of a Furby." *(quoted from furbytoyshop.com, Nov 12, 2026)* That's my opinion of the writing, not a factual claim about how it was made. The page is now titled "Furby Toy Shop: Guides, Reviews & Collector Tips", and it carries an Amazon affiliate disclosure as well as the ads. *(measured 11-12)*

## Why it happened

**Why the ID is public.** AdSense works by putting the publisher ID in the page, so the ad code knows whose account to credit. It can't be hidden from visitors, because the visitor's browser has to read it. *(inferred)*

**Why it links sites.** One operator running several sites has every reason to use one account: one payout, one dashboard. So the ID that pays the operator also ties the sites together, for anyone who looks. *(inferred)*

**Why the history matters.** A different AdSense account on the same domain means the money goes somewhere else. Both domains show changes like that: mayan-ruins.org went from one AdSense account to a parked page to another account between 2019 and 2021, and furbytoyshop.com swapped its own AdSense and analytics accounts for new ones in 2018, then picked up the shared AdSense ID by 2025. It's what you'd expect to see when an {{< term "expired-domain" "established domain is bought" >}} for the {{< term "seo" "search ranking" >}} it has already built up, then filled with new content. That's a reading of the pattern, not something the IDs prove, and buying an expired domain is legal. *(inferred)*

## Findings, causes and contributing factors

1. furbytoyshop.com and mayan-ruins.org carry the same AdSense publisher ID, `ca-pub-8865241261618143`.
2. Both domains predate that ID's appearance on them.
3. furbytoyshop.com changed analytics and AdSense accounts in 2018, between its 2012-2018 shop and the "Best Furby Toys" version, and had the shared AdSense ID by March 2025.
4. mayan-ruins.org changed AdSense accounts between January 2019 and February 2021, with a parked page in between.
5. Searches for every unique ID and slogan on the two sites find no third site carrying the shared ID.
6. The Furby site's footer address is a plaza unit that public listings attribute to other businesses.
7. Nothing found shows a break-in, and nothing here identifies a person.

**Immediate cause:** ad and analytics IDs have to be in the page to work, so they're public.

**Systemic causes:** one account per operator is the natural way to run ads across many sites, and archives keep dated copies of every page, so both the link between sites and the change of hands are permanently readable.

**Contributing factors:** a domain keeps its age and history when it changes owner, and nothing on the page tells a visitor that it did.

## What went well, what went wrong, where I got lucky

**Went well:** every claim rests on a public ID with a date. The check was re-run in November 2026 against live pages and archived snapshots, not taken from my 2025 notes alone.

**Went wrong:** only two sites are confirmed. Finding the rest needs a reverse lookup of the ID, which is a third-party service's data, and that wasn't done for this post.

**Got lucky:** the Wayback Machine had snapshots on both sides of each change, close enough together to date them.

## What I changed, and what's still open

This is about other people's sites, so there's nothing for me to fix. What follows is for readers.

Recommendations:

- **To anyone checking a site:**
  1. Open the page source (view-source: in the address bar) and search for `ca-pub-`, `G-` and `UA-`.
  2. Look the domain up on web.archive.org and open snapshots a few years apart. Search each one for the same IDs.
  3. If the IDs change, the people collecting the money changed. If the same ad ID turns up on sites with nothing in common, it's probably one operator.
- **To anyone running ads on more than one site:** your publisher ID links them, publicly and permanently. If you'd rather two sites weren't connected, they can't share an account.

| Action | Type | Owner | Status |
|---|---|---|---|
| Re-check both live pages and their Wayback history | detect | me | done Nov 5, 2026 |
| Confirm other domains under the same ID, in page source, with dates | detect | me | open: two confirmed Nov 12; the others need the April 2025 list |

## Lessons

- **Anything a page needs to work, anyone can read.** An ad ID is an account number in plain sight.
- **Domains have memories.** The archive keeps the old owner's IDs next to the new owner's, with dates.
- **Say what the evidence shows, and no more.** Two IDs prove one account. They don't prove who, or why.

Search engines used to be the thing sites like this were built to fool. Now AI answers are too, and an AI won't tell you that its source is an old domain refilled with filler. It's a new round of the same SEO race.

This started with an AI putting a Furby site next to a research group. It ends with a habit. When a source turns up in an answer, look at who gets paid by it and how long it has been what it claims to be. View-source and the Wayback Machine won't tell you who runs a site. They'll tell you whether it's worth citing.
