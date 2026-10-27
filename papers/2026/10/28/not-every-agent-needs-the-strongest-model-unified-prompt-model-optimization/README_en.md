# 2610.31743v2 Not Every Agent Needs the Strongest Model: Unified Prompt-Model Optimization for Heterogeneous LLM-based Multi-Agent Systems

## Core Value (1 sentence)
UniMASO jointly optimizes agent prompts and model assignments in heterogeneous MAS — structured/summarization agents use lighter models (Qwen3.5-9B 43.5%), reasoning/verification agents use stronger models (DeepSeek-V4-Flash 45.5%) — achieving average score 70.40 with 85.2% lower deployment cost than the strongest homogeneous configuration.

## Problem
Prior work on prompt optimization typically keeps model assignments fixed, leaving differences in role requirements and their associated inference costs outside the search. This creates role–capability misalignment: strong models can be wasted on routine roles or lightweight models can bottleneck demanding roles, while prompt edits cannot supply missing capabilities. Existing methods either optimize prompts (fixing execution models) or do model routing (fixing prompts), but do not jointly search both.

## Contribution
1. Formulates heterogeneous MAS optimization over prompt–model configurations, making role–capability misalignment explicit.
2. Develops cost- and topology-aware search coupling local multi-granularity evaluation with system-level co-evolution.
3. Introduces cross-level trajectory memory that turns local feedback, global outcomes, and cost observations into experience for later rounds.
4. Evaluates on five benchmarks (AGIEval-MATH, GPQA-Diamond, BFCL-V3, LiveCodeBench v6, HotpotQA) and five execution topologies (Independent, Centralized, Sequential, Decentralized, Dynamic): UniMASO achieves better quality–cost trade-offs than homogeneous configurations. Under centralized execution, UniMASO raises average score from 69.79 to 70.40 while reducing token-weighted deployment cost by 85.2% relative to DeepSeek-V4-Pro with MASPO.
5. Role-conditioned model allocation: Qwen3.5-9B selected most for structured/summarization (43.5%), DeepSeek-V4-Flash dominates reasoning/verification (45.5%).

## Method
The UniMASO pipeline has these main steps:
1. Model an N-agent system as a directed graph G = (V, E). Each agent vi has prompt space Pi and is assigned a role prompt pi ∈ Pi and an execution model mi from heterogeneous pool M. Write assignment as zi = (pi, mi) and full system configuration as z = (z1, ..., zN).
2. Trace-guided candidate generation: optimizer Mopt samples traces containing inputs, contexts, outputs, and feedback, then proposes candidates from current configuration.
3. Multi-granularity interaction evaluation: compare candidate and reference executions at three granularities — local validity, lookahead utility, global alignment. Utility: Ui(p') = α·qloc_i(p') + β·qlook_i(p') + γ·qglob_i(p'), α + β + γ = 1.
4. Cost-aware beam search: expand candidate when Ui(p')·ηi(p')−λ > uref (λ ≥ 0 cost weight, uref = 1/2 neutral point). Retain non-dominated quality–cost candidates.
5. Topology-aware heterogeneous model adaptation: extend local candidates to prompt–model pairs z'i = (p'i, m'i). Best local update ¯zi = (¯pi, ¯mi) passed to system coordination.
6. Topology-conditioned multi-view proposals: each optimizable logical agent forms a focal view conditioned on roles, dependencies, execution order, local search results, and model capability–cost information.
7. Proposal-entropy consensus: πi(m) = (1/J)·Σj I[ˆm(j)i = m], Ai(m) = πi(m)(1 − H̄i). Configuration-level decision solved subject to feasibility and capability–cost balance.
8. Cross-level trajectory memory: ξt = (zt, at, qt, Ct, bt). Group records into low-cost global successes, local successes with global failures, high-cost global successes. Category-balanced retrieval (up to Kmem per category).

## KNOWLEDGE — Data & Concepts
- Heterogeneous MAS: multi-agent system where each agent can use different models.
- Prompt–model optimization: joint search of prompts and model assignments for quality–cost trade-off.
- Role–capability misalignment: strong models wasted on routine roles or lightweight models bottleneck demanding roles.
- Cost-aware Pareto search: retain candidates non-dominated in quality and cost.
- Topology-aware co-evolution: coordinate updates according to agent roles and dependencies.
- Cross-level trajectory memory: turn local feedback, global outcomes, and cost observations into experience.
- Model pool: Qwen3.5-4B, Qwen3.5-9B, Qwen3.5-27B, DeepSeek-V4-Flash, DeepSeek-V4-Pro.
- 5 benchmarks: AGIEval-MATH (difficulty 5), GPQA-Diamond, BFCL-V3, LiveCodeBench v6, HotpotQA.
- 5 topologies: Independent, Centralized, Sequential, Decentralized, Dynamic.
- Centralized execution: average score 69.79→70.40, cost 208.28M→30.92M (85.2% reduction).
- UniMASO leads on AGIEval-MATH (82.42 vs 78.12) and HotpotQA (63.80 vs 62.80).
- Qwen3.5-9B selected 43.5% for structured/summarization; DeepSeek-V4-Flash dominates reasoning/verification (45.5%).
- Qwen3.5-27B + DeepSeek-V4-Flash combined share rises from 47.8% to 78.8% between groups.
- Optimization cost: 4,710.6M→206.3M (95.6% reduction).
- Input tokens: 29.42M→23.33M (20.7%); output tokens: 0.439M→0.369M (15.9%).
- Cost-of-Pass: 1.241→0.184 (85.2% reduction).
- 3 optimization rounds with search depths 3–2–2. Cost weight λ = 0.2; Kmem = 2 records per category.

## INSIGHT — Mechanism & Why
- [Joint prompt–model adaptation is necessary] occurs because optimizing prompts first then assigning models afterward may make the prompt fit the original executor better than the model ultimately assigned to that role. Jointly evaluating both decisions is consistent with observed improvement in quality and cost.
- [Co-evolution is useful when one agent's change affects successors] occurs because local updates are evaluated with the rest of configuration fixed, so their combination may change inter-agent behavior. System-level coordination resolves this mismatch.
- [Cost-aware search improves operating point] occurs because task quality alone does not identify an efficient configuration — removing cost-aware Pareto search lowers average score from 70.40 to 69.42 while raising deployment cost from 30.92M to 62.40M. Need to consider both execution cost and task utility when selecting candidates.

## IDEA — Actionable Applications
1. Apply UniMASO to your company's multi-agent system: jointly optimize prompts and model assignments instead of optimizing prompts with fixed models. First step: identify agent roles in your system and available model pool, then run joint prompt–model search for each role.
2. Distribute models by role requirements: assign lighter models to structured/summarization roles (e.g., Qwen3.5-9B) and stronger models to reasoning/verification roles (e.g., DeepSeek-V4-Flash). First step: classify agents into structured/summarization and reasoning/verification groups, then assign appropriate models.
3. Use cross-level trajectory memory: store records of preceding configuration, proposed modification, and evaluation (quality, cost, acceptance outcome) for reuse in later optimization rounds. First step: set up trajectory optimization storage and category-balanced retrieval with Kmem = 2.

## WISDOM — General Principle
- Principle: Not every agent in a multi-agent system needs the strongest model — assign model capability according to role requirements and jointly optimize prompts with model assignments.
- When to use: When designing multi-agent LLM systems with different roles and wanting to optimize quality–cost trade-off.
- When NOT to use: When the system has only a single agent or all agents have the same capability requirements.

## Assumptions & Limitations
- Required condition: Need a multi-agent system with directed graph execution topology and a homogeneous model pool to choose from.
- Paper-acknowledged limitations: Experiments limited to five benchmarks and five topologies; results may not generalize to other tasks or topologies.
- Limitations the paper does NOT state: Does not state the meta-optimization cost of running UniMASO itself relative to the target task cost.

## Metadata
- Year: 2026
- Authors: Mingxiu Cai, Haoyang Xian, Xinyu Ma, Yutong Wang, Zhenxi Song, Jing Li, Xuebo Liu
- arXiv category: cs.MA
- PDF link: https://arxiv.org/pdf/2610.31743v2
- Classification: [applied]