---
# Furry travel post. Create with:
#   hugo new content blog/travel/<con-and-year>.md --kind travel
# Preview drafts with `hugo server -D`; set draft: false to publish.
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
draft: true
series: travel
con: ""          # e.g. "Example Con 2026"
con_url: ""      # the con's own site, optional
city: ""         # e.g. "Rosemont, IL"
dates: ""        # e.g. "Dec 4-7, 2026"
cover_image: ""  # /res/travel/<file>.jpg (put the file in static/res/travel/)
cover_alt: ""    # one line describing the photo
summary: ""      # one sentence for link previews
---

<!--
Before publishing:
  - Strip photo metadata (GPS, camera owner name):  exiftool -all= -overwrite_original static/res/travel/*.jpg
  - Only name people who said yes. Use badge/fursona names, never legal names.
  - No hotel names or room numbers, and nothing that says where you are right now: post after you're home.
Delete any section you don't need. These comments don't render.
-->

## Getting there

<!-- How you got there and how it went: drive, train, flight, who you rode with. -->

## The con

<!-- Panels, dances, the dealers' den, what you did there. -->

## Off the con floor

<!-- The city itself: food, sights, the place everyone ended up at 1am. -->

## Suit and gear

<!-- What came along, what held up, what you'd pack differently. -->

## Would I go back?

<!-- A straight answer and one reason. -->
