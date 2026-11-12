---
title: "Trivy"
term_kind: tool
topics: [security-operations]
see_also: [vulnerability, container, cve]
summary: "Open-source scanner that checks container images and code for known vulnerabilities and leaked secrets."
match: ['\bTrivy\b']
sources:
  - title: "Trivy"
    url: "https://trivy.dev/"
    publisher: "Aqua Security"
    primary: true
  - title: "aquasecurity/trivy"
    url: "https://github.com/aquasecurity/trivy"
    publisher: "GitHub"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:aquasec:trivy", topic: "the name NVD files Trivy vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Aaquasec%3Atrivy"}
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Trivy is a free, {{< term "open-source" >}} security scanner made by Aqua Security. Pointed at a {{< term "container" >}} image, a code repository or a cloud setup, it lists the software inside and reports any known {{< term "vulnerability" "vulnerabilities" >}} ({{< term "cve" "CVEs" >}}), misconfigurations and exposed secrets. Like any tool that runs with wide access, it is itself software that has to be kept up to date.
