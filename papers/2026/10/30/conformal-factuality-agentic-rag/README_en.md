# [2610.34872] Adaptive Retrieval, Selective Answers: Evaluating Conformal Factuality in Agentic RAG

## Core Value (1 sentence)

When deploying RAG agents, apply conformal filtering after the agent generates an answer — keeping only atomic claims whose relevance score exceeds a calibration-derived threshold — to achieve 89–95% full support at the 95% target, while reporting non-empty response coverage (17–60%) alongside to expose the reliability–informativeness trade-off.

## Problem

Retrieval-augmented generation (RAG) conditions language-model responses on external documents, but evidence retrieval does not ensure that every generated claim is factual or supported. Previous work studied claim-level conformal factuality in single-stage RAG and, more recently, multi-hop RAG. This work examines its behavior in agentic RAG, where a language-model policy adaptively issues follow-up retrieval queries or terminates retrieval before response generation. In agentic RAG, the evidence used to generate and score claims is acquired adaptively depending on the question and evidence observed so far, while the conformal post-processing stage remains conceptually the same.

## Contribution

1. A formal representation of the implemented agentic retrieval process as an evidence-dependent sequence of retrieval-policy decisions, plus a six-configuration evaluation with complete target sweeps and unfiltered baselines.
2. Retains the retrieval-based relevance-scoring formulation and post-generation conformal filtering, extending the evaluation from single-stage and multi-hop RAG to agentic RAG.
3. Shows that increasing conformal targets produces higher observed response-level support together with lower claim retention and non-empty answer coverage when evidence acquisition is agent-driven, characterizing the reliability–informativeness trade-off when conformal factuality is applied after agent termination.

## Method

The agentic retrieval trajectory is formalized as follows: given question x and document corpus K, retrieval operations are indexed by t. The initial query is the original question q(1) = x. With a top-k retriever having similarity cutoff θ, the initial document sequence is D1 = Unique(Retrieve(K, q(1); k, θ)). After t retrievals, let Qt = (q(1), ..., q(t)) and Dt contain the distinct passages accumulated in retrieval order. The decision state is Ht = (x, Ψ(Dt), Qt, t, B − t), where πω is the agent's policy, B is the retrieval-operation budget, Q is the space of follow-up queries, and Ψ(Dt) is the bounded evidence view supplied to the policy. If at = Retrieve(q(t+1)) is admissible, then Et+1 = Retrieve(K, q(t+1); k, θ) and Dt+1 = Dt ⊕ New(Et+1, Dt), where New removes duplicates already present in Dt and ⊕ appends previously unseen passages. The number of completed retrieval operations when the process terminates is τ(x), with 1 ≤ τ(x) ≤ B. After agent termination, the model generates a response and the claim decomposer extracts atomic statements: ŷ = G(x, Dπ(x)), C(x) = g(ŷ) = {c1, ..., cp(x)}. The number of extracted claims p(x) varies across questions. The factuality annotation for each claim belongs to {S, I, U, N}, where only S counts as supported. The agentic relevance score is Ragent(c; x) = max(0, max d∈Dπ(x) sret(d) sim(c, d)), where sim(c, d) measures semantic alignment between claim and passage. The thresholded retained set is Fλ(C(x)) = {c ∈ C(x) : eR(c) ≥ λ}, applied post-generation. A response is fully supported at threshold λ when every retained claim is supported: Bi(λ) = I[∀cij ∈ Fλ(Ci), Aij = 1]. The split-conformal order-statistic threshold is λα = V(kα) if kα ≤ n, else +∞, with kα = ⌈(n + 1)(1 − α)⌉. The five evaluated targets 1 − α ∈ {0.80, 0.85, 0.90, 0.925, 0.95} correspond, for n = 30, to kα ∈ {25, 27, 28, 29, 30}.

## KNOWLEDGE — Data & Concepts

- Six model–dataset configurations: GPT-6 Luna and Llama 3.1 8B on HotpotQA, Natural Questions (NQ), and TriviaQA.
- Each configuration uses 60 fixed questions, 100 seeded 30/30 calibration–test partitions, five conformal targets (80, 85, 90, 92.5, 95%), and a no-conformal-prediction baseline.
- Retriever: sentence-transformer embeddings (all-MiniLM-L6-v2), FAISS index, top-k = 10 documents per retrieval, similarity cutoff θ = 0.3, initial retrieval enabled, at most three retrieval operations and three policy decisions.
- At the 95% target: non-empty coverage spans 17.23% (GPT-6 Luna, NQ) to 60.17% (Llama 3.1 8B, TriviaQA); claim retention spans 10.72% to 43.16%; full-support fraction among non-empty outputs spans 89.14% to 95.56%; supported-claim fraction among retained claims spans 90.16% to 97.72%.
- Increasing the conformal target raises observed full support while reducing answer availability; the magnitude of the selectivity cost depends strongly on the dataset/model combination.
- NQ reaches much lower coverage than TriviaQA at stringent targets.
- Conformal filtering is post-generation: the conformal target does not control when the retrieval agent stops.
- An empty claim set is vacuously fully supported by convention.

## INSIGHT — Mechanism & Why

[Full support increases as the conformal target is raised] happens BECAUSE [a higher relevance threshold removes more unsupported claims, leaving fewer responses but a larger fraction of them fully supported]. This means [a clear reliability–informativeness trade-off: higher thresholds improve reliability but reduce answer availability].

[The magnitude of the trade-off depends strongly on the model/dataset combination] happens BECAUSE [NQ reaches much lower coverage than TriviaQA at stringent targets, showing the selectivity cost of a given target is not uniform across settings]. This means [evaluation should not be reduced to a single reliability number; answer availability and retained-claim fraction should accompany response-level full support in deployment-facing reports].

[Conformal filtering is post-generation and does not control when the retrieval agent stops] happens BECAUSE [the threshold is applied to claims after response generation, while the agent's stopping time is determined by its retrieval policy]. This means [the reliability–informativeness trade-off occurs at the claim level after evidence has been gathered, not at the retrieval decision time].

[An empty claim set is vacuously fully supported] happens BECAUSE [the all-claims-supported requirement is satisfied by convention when no claims are retained]. This means [response-level full-support rate includes vacuous cases, so non-empty response coverage must be reported alongside to avoid misinterpretation].

## IDEA — Actionable Applications

1. Apply post-generation conformal filtering to RAG agents: after the agent generates an answer, decompose it into atomic claims, score each claim's relevance against retrieved documents, and keep only claims exceeding the calibration-derived threshold. For whom: RAG agent systems needing per-claim factuality guarantees. First step: implement a claim decomposer and retrieval-based relevance scorer.

2. Report full support and answer availability side by side: when deploying a RAG agent, report both the full-support rate FS(λ) and the non-empty response coverage NE(λ), not just a single reliability number. For whom: evaluation and deployment teams for RAG systems. First step: add FS(λ) and NE(λ) metrics to the system evaluation dashboard.

3. Tune the conformal target per dataset: since the selectivity cost varies across datasets (NQ loses much more coverage than TriviaQA at stringent targets), adjust the conformal target per dataset rather than using a uniform threshold. For whom: RAG systems deployed across multiple datasets or domains. First step: run a conformal target sweep on a small evaluation set before selecting the production threshold.

## WISDOM — General Principle

- Principle: Post-generation claim filtering creates a reliability–informativeness trade-off: higher thresholds improve reliability but reduce answer availability; report both metrics together rather than a single number. Apply when building RAG agent systems needing per-claim factuality guarantees. Do not apply when every question must be answered regardless of evidence support.

## Assumptions & Limitations

- Conditions that must hold: separate calibration and test sets, ability to decompose responses into atomic claims, retrieval-based relevance scoring.
- Limitations acknowledged by the paper: evaluation is based on controlled subsets of 60 questions from each of three QA benchmarks (HotpotQA, Natural Questions, TriviaQA); the relatively small sample size may limit generalizability to larger and more diverse question sets; the agentic retrieval process is limited to a maximum of three retrieval operations and three policy decisions, leaving longer retrieval trajectories and alternative agent policies unexplored; experiments consider only two language models (GPT-6 Luna and Llama 3.1 8B); extending to other model families such as Qwen and DeepSeek would help establish robustness and generalizability.
- Limitations the paper does NOT state: effectiveness on larger RAG agents, conformal filtering operational cost at scale, and scalability to real-world environments beyond the three QA benchmarks evaluated.

## Metadata

- Year: 2026
- Authors: Muhammad Aimal Rehman, Chi-Kuang Yeh (Georgia State University)
- arXiv category: cs.CL
- PDF link: https://arxiv.org/pdf/2610.34872v1
- Citation count: [not found]