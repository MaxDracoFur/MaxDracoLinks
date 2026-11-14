---
title: "Reporting a vulnerability"
summary: "How to report a security problem in maxdraco.com or cds.maxdraco.com, and what happens next."
---
<!-- Vulnerability disclosure policy, section 1 as approved by Max 2026-11-12 (Guild GC-OPS-05).
     Linked from the Policy: line of /.well-known/security.txt on maxdraco.com and cds.maxdraco.com. -->

We welcome reports of security problems in sites we run. Thank you for helping keep people safe.

**How to report.** Email the address in this site's [`/.well-known/security.txt`](/.well-known/security.txt). Say what you found, where,
and how to reproduce it. Please do not include anyone's personal data beyond what is needed to show the issue.

**What happens next.** We are a small team. We aim to acknowledge your report within 3 business days and to
tell you within 10 business days whether we can reproduce it and what we plan to do. We aim to fix serious
issues within 30 days and others within 90 days. We tell you when it is fixed.

**Coordinated disclosure.** Please give us 90 days, or until a fix ships if that is sooner, before you
publish. If we need longer we will ask and say why. With your permission we credit you once it is fixed.

**Good-faith research.** If you make a good-faith effort to follow this policy, we will not pursue or support
legal action against you for that research. Stay within these limits: test only your own accounts and data;
stop and tell us if you reach someone else's data; do not degrade the service (no denial of service, no load
testing, no spam); no social engineering or physical attacks; do not keep data you did not need.

<!-- legal-ok unauthorized-access: scope limit in a disclosure policy; it restricts what researchers may test, it does not describe access (Max 11-13: "Yes, allowlist it") -->
**Out of scope.** Hosting and platforms we use (Cloudflare, Railway, GitHub, Google). Please report those to the
vendor through its own program. Also out of scope: findings with no security impact, such as missing headers on
static pages without a working exploit, or a version banner on its own.
