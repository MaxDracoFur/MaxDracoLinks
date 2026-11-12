---
title: "ads.txt"
term_kind: format
topics: [web-and-advertising]
see_also: [google-adsense]
summary: "A public text file on a website listing which ad companies and accounts are allowed to sell its ad space."
match: ['\b(?:app-)?ads\.txt\b']
sources:
  - title: "ads.txt - Authorized Digital Sellers"
    url: "https://iabtechlab.com/ads-txt/"
    publisher: "IAB Tech Lab"
    primary: true
  - title: "ads.txt Specification Version 1.1"
    url: "https://github.com/InteractiveAdvertisingBureau/Supply-Chain-Validation/blob/main/ads.txt%20v1.1.md"
    publisher: "IAB Tech Lab"
  - title: "Ads.txt"
    url: "https://en.wikipedia.org/wiki/Ads.txt"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
ads.txt is a plain text file a website publishes at the top of its address (example.com/ads.txt). Each line names an ad company and the account number allowed to sell ads on that site, for example a {{< term "google-adsense" >}} publisher ID. Advertisers read it before they buy, to confirm which ad accounts the site has authorised to sell its ad space. Because it is public, it also tells anyone which ad accounts a site is paid through.
