# Skill: Codebook-Based Multi-Agent Topology Design

Source: 2609.02264v1
Type: framework

## When to use this skill
- You are building an LLM multi-agent system and want to design optimal communication topology for each query.
- You need to reduce token cost and increase accuracy of multi-agent systems.
- You want to avoid iterative search at inference time.

## When NOT to use this skill
- Single-agent systems (no multi-agent topology needed).
- You don't have training data to build a topology codebook.

## Input required
- Training data containing (query, topology, utility, token cost) tuples.
- Frozen sentence encoder to embed queries and agent profiles.
- VQ autoencoder to build the codebook.
- MLP for code prediction and MLP proxy for reranking.

## Steps to execute
1. Collect execution records: for each query, run fixed topologies (complete, chain, star, and three Erdos-Renyi samples) with real LLM agents, logging (topology, query embedding, utility, token cost).
2. Train VQ autoencoder to compress successful topologies (utility > 0.5) into a 16-entry codebook, query-independent.
3. Train MLP code predictor p_θ(k|c) mapping query embedding to distribution over codebook codes, reward-weighted.
4. Train MLP proxy reading flattened adjacency, regressed on measured utility and per-task normalized token cost.
5. At test time: decode top M codes from codebook, deduplicate, score with MLP proxy in one batched call, select candidate maximizing û − λĉ.

## Expected output
- A system that selects optimal multi-agent topology for each query.
- Higher accuracy than prior topology design methods.
- Very fast topology emission (2.4 ms).
- 21.9–33.2% reduction in LLM token consumption.

## Example application
You build a multi-agent system for complex coding tasks. Instead of letting agents decide communication topology themselves, Codebook Agent: before runtime, a codebook of 16 best topologies is built from training data. When a new query arrives, the system embeds the query, selects a distribution over codebook codes, decodes top M codes, scores them with an MLP proxy, and executes the best topology. The system achieves higher accuracy and reduces 21.9–33.2% tokens compared to other topology design methods.

## Gotchas
- Edge count is not a good cost metric — edge count correlates negatively with token consumption, so sparsifying can make inference more expensive.
- Message-passing scorer cannot rank candidates when agents share profiles (default benchmark configuration).
- The practical design space is very small (~6 distinct graphs), so larger codebook capacity doesn't help much.