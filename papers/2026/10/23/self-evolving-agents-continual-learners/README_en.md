# 2610.25858 Are Self-Evolving Agents Continual Learners?

## Problem
LLM agents are often deployed in environments where new knowledge, tools, and workflows keep arriving. They are expected to adapt continually — learning new tasks as they arrive without forgetting earlier ones. This resembles continual learning, but at a pace conventional gradient updates cannot sustain. Nonparametric self-evolving agents adapt by rewriting their own harness (system prompt, accumulated memory, skill libraries, control code) from task feedback while model weights stay frozen. The question: are such agents effective continual learners across drifting task streams?

## Contribution
- Constructs four drifting task streams isolating topic drift, workflow drift, domain drift, and compound drift, built from BIRD, BFCL, and ScienceWorld.
- Evaluates three representative self-evolving methods spanning experience retrieval and self-modification: ReasoningBank, GEPA, and Meta-Harness.
- Three findings: (1) current methods trade stability for plasticity (plasticity-stability trade-off), (2) self-modification causes cross-task interference and overwriting, (3) similarity-based retrieval cannot prevent interference or retrieval collision.

## Method
A task stream S_w is a sequence of inputs drawn from a mixture over task families F_k, with weight schedule w_t one-hot and piecewise-constant: the stream is a sequence of contiguous blocks, each drawing all tasks from a single task group, and the active group changes only at block boundaries. The agent maintains one shared harness across the entire horizon and is never told it operates in a drifting stream.

Metrics:
- Terminal advantage (Term.): average of A[T,k] − B_k over all K families at stream end.
- Average advantage (Δ̄): average of A[t_m,k] − B_k over all K families and all M post-seed checkpoints.
- Plasticity P: advantage over seed at end of each family's block, averaged over all K families.
- Stability S: degradation a family incurs while the stream trains other families, combining pre-block interference (Ī) and post-block forgetting (F̄).

Three methods: ReasoningBank distills completed episodes into memory items in an external store and retrieves the top-1 most similar item into the context of later episodes; GEPA rewrites a shared strategy section in the system prompt by reflective mutation over collected rollouts; Meta-Harness proposes edits to a persistent workspace (system prompt, memory and skill files, controller code harness.py) through a coding agent, accepting an edit only when it improves validation accuracy on the active sub-block.

Model: Gemini 3.6 Flash in a ReAct-style loop. Each stream has contiguous blocks of 50 training tasks per group, evaluated on disjoint hold-out sets Deval_k of 50 tasks per group (90 for ScienceWorld).

## KNOWLEDGE — Data & Concepts
- Across 4 drifting streams, average advantage (Δ̄) ranges from +1.8 to +3.1 pp; terminal advantage reaches +3.7 (GEPA), +2.5 (ReasoningBank), +1.4 (Meta-Harness).
- Only topic drift yields near-zero or slightly negative net change (−1.7 GEPA, +0.3 ReasoningBank, −1.5 Meta-Harness).
- Plasticity: GEPA highest in every scenario (+6.2 average, reaching +11.0 on workflow drift and +7.5 on compound drift). ReasoningBank roughly half GEPA's plasticity (+3.3 average).
- Stability: ReasoningBank highest (−1.9 average, −0.4 domain drift, −1.4 compound drift). GEPA largest stability loss (−4.3 average). Meta-Harness least stable on domain and compound drift (S = −3.1 and −4.4).
- Pre-block interference: on domain drift, training ScienceWorld lowers BFCL-Base at position 50 by 5.5 (GEPA) and 1.5 (Meta-Harness). On compound drift, training two BIRD blocks degrades BFCL-Miss before any BFCL task arrives, reaching −6.8 (GEPA) and −4.8 (Meta-Harness) at position 100.
- Post-block forgetting: on compound drift, GEPA condenses seven BIRD SQL sections (3,386 chars at position 100) into one 1,034-char section, reducing BIRD-F1's share from 59.5% (position 100) to 5.8% (position 150), erasing its +4.0 gain by stream end.
- Retrieval collision: on workflow drift, BFCL-Miss and BFCL-Base use the same API catalog with nearly identical language (mean pairwise cosine 0.667, nearest-match 0.835–0.840), indistinguishable from within-group similarity (0.664–0.666 pairwise, 0.834–0.837 nearest-match). No similarity threshold can separate them. 52% of BFCL-Miss episodes at stream end retrieve a BFCL-Base memory, dropping BFCL-Miss accuracy by 8.0 points (+12.5 → +4.5).

## INSIGHT — Mechanism & Why
[Self-modification applies global edits to a shared prompt or workspace] happens BECAUSE every update writes to a shared instruction or workspace surface injected into all subsequent rollouts, creating pre-block interference (rules specialized for one block applied unconditionally to unseen tasks) and post-block forgetting (later blocks continue modifying the same shared prompt/workspace, compressing or overwriting earlier instructions). This means [rules learned on one block interfere with unseen tasks and are compressed or overwritten by later blocks, most severely when consecutive blocks share a domain but require conflicting workflows].
[Similarity-based retrieval] happens BECAUSE retrieval always injects the nearest stored match without a similarity threshold, so any group evaluated before its own training block begins receives foreign memories in 100% of episodes; and when different task groups occupy the same region of embedding space, no similarity threshold can separate them. This means [semantic similarity between queries captures topical overlap but cannot determine whether a stored trajectory's workflow is compatible with the incoming task].

## IDEA — Actionable Applications
1. Apply the principle of task-specific update isolation into agent harness design: first step is to design the agent harness so updates for task A do not affect task B (e.g., use separate namespaces or modules per task group instead of a single global prompt).
2. Apply retrieval conditioning beyond surface query similarity: first step is to add a context filter before feeding retrieved memories into the prompt, checking whether the stored memory's workflow is compatible with the incoming task.

## WISDOM — General Principle
Principle: In continual learning for agents, plasticity and stability are always in tension; global updates into a shared harness give fast learning but fast forgetting, while localized retrieval prevents forgetting but still suffers collision when different tasks use the same embedding space. Use when: the agent needs to adapt continually to new tasks without forgetting old ones. Do NOT use when: tasks come from the same domain but require conflicting workflows — you need a clearer separation mechanism.

## Assumptions & Limitations
- Base model fixed (Gemini 3.6 Flash), not a broad sweep across model families and sizes.
- Task blocks are contiguous; uniformly interleaved tasks still cause degradation (GEPA terminal advantage drops from +5.8 to +0.9).
- Evaluated on agentic benchmarks (BIRD, BFCL, ScienceWorld), not extended to other domains.
- No separate Limitations section; limitations are discussed in Conclusion and analysis.

## Metadata
- Year 2026; authors: Xiaoyin Chen (Mila, Université de Montréal), Yizheng Huang, Yinglun Xu, Ziyun Zhao, Emmett McQuinn, Julie Liu, Hope Yao (Google DeepMind); category: cs.AI; PDF: https://arxiv.org/pdf/2610.25858v1; citation count: [NO DATA — paper 2026-10-19]