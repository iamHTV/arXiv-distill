# [2609.02264v1] Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems

## Problem
Adapting the communication topology of an LLM multi-agent system to each query improves both accuracy and efficiency, but current designers treat this as conditional graph generation: a variational, autoregressive, or diffusion decoder searches the N×N adjacency space, and a graph-network proxy trained on utility and a structural cost such as edge count ranks the sampled candidates. Three empirical observations reject this formulation: (1) reward-surviving topologies collapse to about six distinct graphs even when codebook capacity grows from 8 to 64; (2) edge count is negatively correlated with measured token consumption (Pearson r ≈ −0.4), so sparsifying the graph makes inference more expensive; (3) a message-passing scorer over agent-profile nodes is adjacency-invariant when agents share a profile — the default configuration of published benchmarks — so it cannot rank candidates at all in that regime.

## Contribution
- Introduces Codebook Agent: a vector-quantized autoencoder compresses successful topologies into a query-independent 16-entry codebook; a reward-weighted MLP maps the query embedding to a distribution over codes; and an MLP proxy that reads the flattened adjacency, regressed on measured utility and per-task normalized token cost, reranks the top decoded candidates in a single batched forward pass.
- With no iterative search and no message passing at test time, Codebook Agent is the most accurate method on all six benchmarks compared (84.6 average against 83.0 for the strongest prior designer), emits a topology in 2.4 ms, and uses 21.9–33.2% fewer LLM tokens.

## Method
- Axis A (candidate generator): Codebook Agent instantiates a discrete codebook with a query-conditioned prior. A VQ autoencoder compresses observed topologies: flatten off-diagonal entries a = vec(A) ∈ {0,1}^{N(N−1)}, encode ze = Encψ(a) ∈ R^dz, find k⋆ = arg min ||ze − ek||², decode zq = ek⋆. Codebook size K = 16, dz = 32. Codebook updated by exponential moving averages (decay 0.99), commitment coefficient β = 0.25, straight-through gradients, reinitialization of unused codes after 50 batches. Trained only on records with u_j > 0.5 (topologies that solved their task). Neither encoder nor decoder is conditioned on the query; after training, code k decodes to binary topology A(k), and all query dependence is carried by the predictor below.
- Axis B (scorer): A reward-weighted MLP predictor p_θ(k|c) is fit to reward-weighted soft targets. An MLP proxy f_ϕ reads flattened adjacency, regressed on measured utility and per-task normalized token cost. At test time, top M codes are decoded, deduplicated, and scored in one batched proxy call; the candidate maximizing û − λĉ is executed.
- Problem setup: A team of N agents has profile texts p_1,...,p_N embedded as x_i = E(p_i) ∈ R^d by a frozen sentence encoder (d = 384). A topology is a directed adjacency matrix A ∈ {0,1}^{N×N} without self-loops. Executing the team on query q under A returns utility u(A,q) ∈ {0,1} and token cost τ(A,q). Goal: a generator mapping c = E(q) to a topology maximizing R = u − λτ̃, with τ̃ normalized cost and λ = 0.1.

## Key Findings
- Codebook Agent achieves 84.6 average accuracy on six benchmarks, beating 83.0 for the strongest prior designer.
- Emits a topology in 2.4 ms (vs 301–396 ms for iterative methods).
- Reduces LLM token consumption by 21.9–33.2%.
- No iterative search and no message passing at test time.
- The practical design space is very small: only about six distinct graphs survive the reward filter.

## Actionable Insights
1. The practical topology design space is very small — only about six distinct graphs survive reward filtering. Apply: instead of continuously searching the adjacency manifold, build a codebook of the best topologies and select from this short list. First step: Collect successful topologies from training tasks, cluster them into similar groups, and pick representatives for each group.
2. Edge count is not a good cost metric — edge count correlates negatively with token consumption (r ≈ −0.4), so sparsifying the graph can make inference more expensive. Apply: when designing topology, use measured token cost rather than edge count as the cost objective. First step: Measure actual tokens for each topology configuration and use that as the optimization target.
3. No iterative search needed at test time — select from a pre-computed codebook. Apply: when deploying multi-agent systems, train a topology codebook offline and only select from the codebook at runtime. First step: Build a system that selects topology from a codebook based on query embedding.

## Assumptions & Limitations
- Evaluated on six benchmarks with two LLM backends; may differ on other tasks/domains.
- Only evaluated with agents sharing profiles (homogeneous teams); may differ on heterogeneous teams.
- Codebook has fixed size of 16 entries; may not be sufficient for very complex tasks.
- Does not compare against all existing topology design methods.

## Metadata
- Year: 2026, Authors: Jinxi Yu, Yubei Li, Eric Hanchen Jiang, Zhi Zhang, Dong Liu, Wenxiao Zhao, Levina Li, Kai-Wei Chang, Ying Nian Wu (University of California, Los Angeles), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2609.02264v1