# [2609.13489v2] Pre-retrieval Query Clustering for Adaptive Top-k Document Retrieval in RAG Systems

## Problem
- RAG systems commonly retrieve a fixed number of documents (top-k) to ground generation, but this static approach is brittle: simple queries suffer over-retrieval (adding noise and cost) while complex queries are under-retrieved, causing recall failures that cascade into incorrect answers. Prior work does not address the question of how many documents must be retrieved to answer an arbitrary query reliably.

## Contribution
- QCAR (Query-Clustering Adaptive Retrieval) — a pre-retrieval, query-centric framework for adaptive retrieval depth.
- Offline: estimate per-query retrieval difficulty by measuring NDCG under the default retriever and deriving a query-specific "saturation" point k* from the NDCG–k curve; cluster a large set of queries in embedding space and summarize each cluster with a recommended retrieval depth targeting high coverage (~95%) using a mean-plus-variance rule.
- Runtime: assign incoming query to a cluster and select the corresponding top-k in constant time.
- Pre-retrieval and query-centric, robust in heterogeneous case-like corpora, applicable across legal, healthcare, finance, and enterprise search domains.

## Method (core summary)
- Offline 3 steps: (1) Discover intent clusters — embed historical queries using a dense encoder and cluster by semantic similarity; queries within a cluster share similar retrieval requirements. (2) Measure retrieval difficulty — for a sample of queries from each cluster, evaluate retrieval quality using NDCG, quantifying how many documents the retriever must fetch to achieve acceptable recall. (3) Assign cluster-level depth recommendations — aggregate per-query difficulty estimates into a single recommended k* for each cluster, targeting high coverage (~95%) using a mean-plus-variance rule. Output is a Query-Cluster Database D_qc containing: (i) fitted projection model, (ii) cluster centroid locations, (iii) mapping from cluster ID to recommended retrieval depth.
- Online: (1) Lexical check — scan query for scope markers; if found, set k* = k_max and proceed to retrieval. (2) Cluster assignment — embed query, project into learned space, assign to nearest centroid, look up k* from D_qc. (3) Retrieval and generation — execute standard RAG with adaptive k*.
- Overhead: lexical matching <1ms, one embedding call 30-50ms (already required for retrieval), projection transform 1ms, nearest-neighbor search over K centroids <1ms for K ~100, O(1) cluster lookup.

## Key Findings
- 6,820 questions from 20,000 raw user queries (after cleaning and PII filtering).
- Against k=50 baseline: simple queries — 35.95% token reduction, F1 +0.37; complex queries — F1 +0.37 at 85.95% token increase.
- Full-traffic A/B test: F1 improved over 36% while reducing token usage by 14% on low-complexity clusters without accuracy loss.
- End-to-end: dynamic k reduces token consumption up to 23% while maintaining conceptual parity with baseline for simple queries; improves factual recall by 9-17% for complex queries.
- UMAP + k-means best: n_components=190, n_neighbors=200, min_dist=0.0, k=80 clusters (SS=0.6, DBI=0.46).

## Actionable Insights
1. Estimate per-query difficulty before retrieval (pre-retrieval query difficulty estimation) to select adaptive top-k depth instead of a fixed number. Application: build a Query-Cluster Database from historical query logs, assign new queries to the nearest cluster and select the corresponding top-k, reducing tokens for simple queries without sacrificing accuracy.
2. Pre-retrieval query clustering is more robust than post-retrieval confidence methods for case-like corpora. Application: use UMAP + k-means to cluster historical queries, compute NDCG–k curves per cluster, determine saturation point k* using a mean-plus-variance rule.

## Assumptions & Limitations
- Designed for bounded-domain RAG systems with stable, recurring query distributions and available historical queries.
- Documents drawn from coherent domains (case files, medical records, enterprise wikis) rather than the open web.
- Open-domain settings are a distinct setting where query diversity is unbounded.
- Experiments focus on personal injury law; adapting to a new vertical requires a historical query log, a relevance labeling mechanism (LLM-as-a-Judge or human annotation), and optionally domain-informed lexical patterns.
- Not stated: added latency from query embedding and nearest-neighbor search may accumulate at high traffic volume.

## Metadata
- Year: 2026, authors: Ye Xia (Portland State University), Emre Yamangil, Haixun Wang (EvenUp), arXiv category: cs.IR, PDF link: https://arxiv.org/pdf/2609.13489v2, conference: CIKM '26, Rome, Italy
