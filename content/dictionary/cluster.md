---
title: "Cluster"
term_kind: concept
topics: [platforms-and-services]
see_also: [kubernetes, high-availability, container]
summary: "A group of computers working together as one system; in Kubernetes, the machines it runs your programs on."
match: ['\bclusters?\b', '\bpods?\b']
sources:
  - title: "Cluster Architecture"
    url: "https://kubernetes.io/docs/concepts/architecture/"
    publisher: "Kubernetes"
    primary: true
  - title: "Pods"
    url: "https://kubernetes.io/docs/concepts/workloads/pods/"
    publisher: "Kubernetes"
  - title: "Computer cluster"
    url: "https://en.wikipedia.org/wiki/Computer_cluster"
    publisher: "Wikipedia"
# Copy review: Claude drafted this entry (2026-11-12) (card maxdraco-dictionary). Max approved it 2026-11-12.
# Sources: primary/official first, each fetched 200 on 2026-11-12. classification ids checked at their canonical URLs.
draft: false
---
A cluster is a group of computers, each called a node, that are set up to act as one. In {{< term "kubernetes" >}}, the cluster decides which node runs each program and moves programs to another node if one fails. The smallest unit it runs is a pod: one or more {{< term "container" "containers" >}} that are started, stopped and moved together.
