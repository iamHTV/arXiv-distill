# Skill: qcar-adaptive-top-k-retrieval
Source: 2609.13489v2
Type: framework

## When to use this skill
- RAG system uses fixed top-k, causing over-retrieval on simple queries and under-retrieval on complex queries.
- Historical query log is available in a bounded domain.
- Can measure NDCG of the default retriever on a query sample.

## When NOT to use this skill
- Open-domain web search with unbounded query diversity.
- No historical query log or no relevance labeling mechanism.
- Need immediate response and cannot tolerate added latency from query embedding.

## Input needed
- Historical query log (cleaned, PII-filtered).
- Document corpus to retrieve from (case files, medical records, enterprise wikis, etc.).
- Retriever that can compute NDCG.
- Dense encoder (e.g., text-embedding-ada-002).
- Relevance labeling mechanism (LLM-as-a-Judge or human annotation).

## Steps to execute
1. Embed historical queries using a dense encoder (e.g., text-embedding-ada-002, dimension 1536) and cluster by semantic similarity (UMAP + k-means) to discover intent clusters.
2. For each cluster, sample queries and evaluate retrieval quality using NDCG to measure retrieval difficulty — quantifying how many documents are needed for acceptable recall.
3. Aggregate per-query difficulty estimates into a single recommended k* for each cluster, targeting high coverage (~95%) using a mean-plus-variance rule.
4. Build Query-Cluster Database D_qc containing: fitted projection model, cluster centroid locations, mapping from cluster ID to k*.
5. At runtime: scan query for scope markers; if found, set k* = k_max.
6. Otherwise, embed query, project into learned space, assign to nearest centroid, look up k* from D_qc.
7. Execute standard RAG with adaptive k*.
8. Periodically rebuild D_qc or trigger updates when distribution shift is detected.

## Expected output
- Adaptive retrieval depth system reducing tokens for simple queries without sacrificing accuracy.
- Query-Cluster Database with O(1) k* lookup.

## Application example
- Legal RAG assistant: simple query "What is the statute of limitations for personal injury in California?" gets small k* (e.g., k=10), reducing tokens 35.95% vs fixed k=50 and improving F1 +0.37; complex query "Explain how comparative negligence affects damages when the plaintiff is partially at fault, and cite relevant rules" gets larger k*, improving F1 +0.37 with more tokens.

## Gotchas
- Designed for bounded domains with stable, recurring query distributions.
- Documents from coherent domains (case files, medical records, enterprise wikis), not open web.
- Experiments focus on personal injury law; new verticals need historical query log, relevance labeling, domain-informed lexical patterns.
- Not stated: added latency from query embedding and nearest-neighbor search may accumulate at high traffic volume.
