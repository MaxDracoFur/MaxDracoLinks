# Hacker posts: the incident-report format

From 2026-11-11, hacker blog posts are written as incident reports. Start one with:

```sh
hugo new content blog/<slug>.md --kind hacker
```

That creates the draft from `archetypes/hacker.md`, with every section below in order.

## Where the format comes from

It merges three published standards, read at the source:

- **Google SRE, "Postmortem Culture"** (Site Reliability Engineering, ch. 15) and its **example
  postmortem** (Appendix D). The example's fields are Summary, Impact, Root Causes, Trigger,
  Resolution, Detection, Action Items (each with a type, owner and status), Lessons Learned
  (what went well, what went wrong, where we got lucky), Timeline, and Supporting information.
  The chapter defines blameless: assume everyone acted reasonably with what they knew, and fix
  the system and process, not the person.
  <https://sre.google/sre-book/postmortem-culture/>, <https://sre.google/sre-book/example-postmortem/>
- **ICAO Annex 13**, Appendix "Format of the Final Report" (detailed guidance in ICAO's
  accident investigation manuals, Doc 9756 / Doc 6920). Title, Synopsis, then four headings:
  1 Factual information, 2 Analysis (only facts from section 1 that bear on the conclusions),
  3 Conclusions (findings, and causes and/or contributing factors, both the immediate and the
  deeper systemic ones), 4 Safety recommendations (plus safety actions already taken). Its
  standard 3.1: the sole objective is prevention; it is not to apportion blame or liability.
- **NTSB final reports**, e.g. NTSB/AAR-14/01: Executive Summary, 1 Factual Information,
  2 Analysis, 3 Conclusions (3.1 Findings, 3.2 Probable Cause, with "contributing to the
  accident were ..."), 4 Recommendations, Appendixes. 49 CFR 831.4: investigations are not
  conducted to determine the rights, liabilities or blame of any person.

## The sections

| Section | Purpose | Source |
|---|---|---|
| Summary (the lede, no heading) | The whole story in two or three paragraphs: what failed, how bad, what fixed it. | Google Summary; ICAO Synopsis; NTSB Executive Summary |
| Impact | What was affected, how much, for how long, and what wasn't. Severity stated honestly, not inflated. | Google Impact; ICAO 1.2 to 1.4 (injuries, damage) |
| Timeline | Dated events oldest first, each with its evidence label: start, when it was first visible, when it was seen, each change, end. | Google Timeline; ICAO/NTSB 1.1 History of flight |
| How it was found, and why not sooner | Detection: what surfaced it, and which signal existed but went unwatched. | Google Detection; Google's postmortem trigger "monitoring failure" |
| What the evidence shows | Factual information: versions, config, captures, the reproduction. No conclusions. Everything the analysis uses appears here first. | ICAO/NTSB 1 Factual information (1.16 Tests and research, 1.17 Organizational information) |
| Why it happened | Analysis: the chain of conditions, and why each defence didn't stop it. Uses only the facts above; handles contrary evidence openly. | ICAO 2 Analysis; NTSB 2 Analysis |
| Findings, causes and contributing factors | Numbered findings, then the immediate cause, the deeper systemic causes, and contributing factors. No new facts. Never "human error". | ICAO 3 Conclusions; NTSB 3.1 Findings, 3.2 Probable Cause; Google Root Causes and Trigger |
| What went well / went wrong / got lucky | Three short lists. "Got lucky" names near misses that would have made it worse. | Google Lessons Learned |
| What I changed, and what's still open | Recommendations addressed to others (vendor, readers) and my action items, each with type (mitigate, prevent, detect, process), owner and status. Done items stay listed. | ICAO 4 Safety recommendations and actions taken; NTSB 4 Recommendations; Google Action Items |
| Lessons | Two to four lessons that carry beyond this system. | Google Lessons Learned |

The headings can be reworded to suit a post. The order and the content stay. A section that
doesn't apply gets one sentence saying so.

## Rules

- **Blameless.** The system is the subject. "I" is fine for what I did; the question is why it
  was the reasonable thing to do with what I knew then. "Human error" is never a cause: the
  finding is what made the action easy and its result invisible.
- **Evidence labels.** Every fact is *measured* (a capture, a query, a count I took) or
  *inferred* (reasoned to). Facts from older notes say so.
- **Readable.** It's a blog post. Plain prose for a reader, not a form to fill in.
- **Safe reproduction.** Throwaway credentials, the smallest request that shows it, and no
  key material in the post.
- **Disclosure.** A post about a vendor bug stays an untracked draft until the vendor's
  disclosure window ends. It says it was reported privately to the vendor, nothing more.
- **Every term gets a dictionary link.** The first mention of anything a non-technical reader
  might not know links to its `/dictionary/` page: products, but also concepts (SEO, domain,
  firewall, IP address...). If the page doesn't exist, write it (a definition for visitors,
  the primary source first, a taxonomy entry where one fits honestly) and get it approved
  before the post publishes. `tools/dictionary.py` enforces the link; it can't tell you a
  concept is missing a page, so read the draft as a newcomer would.
- **Primary sources.** Cite the source that owns the fact: the vendor's or standard's own
  page, the regulator, the dataset. A claim about a site's history cites the specific
  archive snapshot (`web.archive.org/web/<timestamp>/<url>`), not "the Wayback Machine".
- **Opinions are mine, and labelled.** A judgement ("reads like filler", "I think") is
  marked as my view. Only what the evidence shows is stated as fact, and a hypothesis the
  data doesn't support is written as a hypothesis, with what the data does show.
- **No publishing while the risk is open.** A post whose own action items describe a live
  weakness (an unrevoked credential, an untested isolation) carries a publish gate in its
  front matter and on its card, and stays unpublished until those items are done and
  re-tested. Then it's rewritten in the past tense.

## Cover image

- **Every post gets at least one square, CD-album-style cover.** It shows on the post and on its
  CD-case tile in the lists. Set `cover_image` (and `cover_alt`) in front matter; put the file
  under `assets/res/covers/` so it's watermarked on build.
- **Where it comes from:** my own phone photos, or a graphic made for the post. Never stock, never
  scraped. A phone photo only goes public through the stage app: approved for one maxdraco
  destination, exported rebuilt from pixels, so EXIF and GPS are gone.
- **Before a photo goes public:** no other people's faces, no addresses or number plates, no
  screens showing anything secret, nothing that ties back to my legal name.
- **Enforced:** `tools/cover_check.py check` refuses a post dated on or after 2026-11-12 that
  publishes without a cover (or whose cover file is missing); older posts are warned about.
  `plan` lists drafts still missing one. I approve the cover like any other copy.

## Previewing

- **Build drafts on current main.** The preview sandbox holds one build at a time, so a
  build from a stale tree hides work that's already on main (it happened: table outlines
  vanished from a drafts preview). Preview from a worktree of current main, with the drafts
  copied in, never from an old checkout or a copied folder.
- **The tooling refuses a stale tree.** `site_preview.py push --code-from <repo>` (what
  `./preview.sh` calls) fetches and refuses unless the tree's HEAD contains `origin/main`,
  and `deploy-cloudflare.sh` runs `site_preview.py fresh .` before it uploads. The fix is
  to rebase or merge `origin/main` and rebuild. A deliberately old build needs
  `PREVIEW_ALLOW_STALE=1` and says so.
- **A deploy publishes the build the sandbox shows.** Pushing a drafts preview replaces it,
  so run `./preview.sh` again right before `./deploy-cloudflare.sh`.
