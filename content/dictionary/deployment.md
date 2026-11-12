---
title: "Deployment (rollout)"
term_kind: concept
topics: [platforms-and-services]
see_also: [kubernetes, container, maintenance-window]
summary: "Putting a new or changed version of software into service, often gradually as a rollout."
match: ['\bdeploy(?:s|ed|ing|ments?)?\b', '\broll(?:s|ed|ing)? out\b', '\brollouts?\b']
sources:
  - title: "Deployments"
    url: "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/"
    publisher: "Kubernetes"
    primary: true
  - title: "Software deployment"
    url: "https://en.wikipedia.org/wiki/Software_deployment"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
Deploying software means putting a new or changed version into service, where people or other systems start relying on it. A rollout is the same step done gradually, for example replacing running copies one at a time so the service never goes fully down. Tools such as {{< term "kubernetes" >}} automate rollouts and can halt one whose new copies fail their {{< term "health-check" "health checks" >}}.
