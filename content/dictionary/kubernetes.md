---
title: "Kubernetes"
term_kind: tool
topics: [platforms-and-services]
summary: "Open-source system for running and managing containers across many machines."
match: ['\bKubernetes\b', '\bk8s\b']
sources:
  - title: "Kubernetes"
    url: "https://kubernetes.io/"
    publisher: "Cloud Native Computing Foundation"
    primary: true
  - title: "Kubernetes documentation"
    url: "https://kubernetes.io/docs/home/"
    publisher: "Cloud Native Computing Foundation"
  - title: "kubernetes/kubernetes source code"
    url: "https://github.com/kubernetes/kubernetes"
    publisher: "GitHub"
classification:
  - {standard: cpe, clause: "cpe:2.3:a:kubernetes:kubernetes", topic: "the name NVD files Kubernetes vulnerabilities under",
     url: "https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=cpe%3A2.3%3Aa%3Akubernetes%3Akubernetes"}
  - {standard: attack, clause: "T1609", topic: "Container Administration Command",
     url: "https://attack.mitre.org/techniques/T1609/"}
  - {standard: attack, clause: "T1610", topic: "Deploy Container",
     url: "https://attack.mitre.org/techniques/T1610/"}
  - {standard: attack, clause: "T1613", topic: "Container and Resource Discovery",
     url: "https://attack.mitre.org/techniques/T1613/"}
# Copy review: Claude drafted this entry (card maxdraco-dictionary, 2026-11-11). Max approves the
# wording (Max approved it 2026-11-11). Sources: primary/official first. classification ids checked against
# MITRE's ATT&CK STIX, CWE 5.0, CAPEC and ATLAS data, NIST's 800-53 rev5 OSCAL catalog and the NVD CPE API on 2026-11-11.
draft: false
---
Kubernetes (often written k8s) runs software packaged as containers across a group of machines called a cluster. You describe what should be running, such as three copies of a web app with a given amount of memory, and Kubernetes starts them, restarts them when they fail and moves them when a machine goes down. It began at {{< term "google" >}} and is now an open-source project of the Cloud Native Computing Foundation.
