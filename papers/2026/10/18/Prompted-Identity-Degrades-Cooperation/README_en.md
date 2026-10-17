# 2609.35928v1 Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems

## Problem
- Multi-agent LLM systems increasingly mix models from several providers, and each agent's model identity leaks to peers via system prompts, agent names, or message headers — though no one intends it to guide behaviour. Prior work on self-preference and minimal-group bias studied isolated completions or single-architecture debates with assigned personas; no one isolated whether model-family metadata itself reorganizes heterogeneous groups into factions.

## Contribution
- Defines factionalism: the interaction graph partitions along identity labels even though all agents pursue a common objective, receive no persona, no individual reward, and no instruction to form groups.
- Factionalism follows the visible label, not the architecture: mislabeled counterfactual (shuffled tags), neutral color labels, and unlabeled control — factions follow announced tags even when wrong or merely colors.
- Factionalism has a cost: labeled groups are slower, more expensive, and less successful; the cost grows with roster size.

## Method
- Measurement framework: each round, every agent emits a commitment (a vote) plus a message to k=2 self-chosen peers; build a directed weighted agreement graph; edge weight = rate at which j's next-round commitment matches i's commitment when i chose j (Eq. 1, normalized by contact volume).
- Homophily: Edge Density Ratio (EDR) = mean within-label vs between-label edge weight, per-run permutation null test.
- Community structure: Louvain community detection on the symmetrized graph weighted by match counts; Adjusted Mutual Information (AMI) between detected communities and the tested partition.
- Decision rule: 4 tests (2 EDR + 2 AMI), Holm–Bonferroni correction at α=0.05; factionalism declared only when all four pass.
- Design: no-stakes games (no individual reward); rosters N ∈ {9,12,25}, balanced (3/3/3, 3/3/3/3, 5/5/5/5/5) vs unbalanced (4/3/2, 4/3/3/2, 9/6/4/3/3); conditions: unlabeled / labeled (true families) / mislabeled (shuffled) / neutral colors (teal, coral, silver, violet, maroon).
- Models (5 open-weight families): Gemma gemma-4-26B-A4B-it, GPT-OSS gpt-oss-20b, Nemotron NVIDIA-Nemotron-3-Nano-30B-A3B-BF16, Qwen Qwen3.6-35B-A3B, GLM GLM-4.7-Flash. 50 runs per configuration.
- Games: Leader Election (unique top vote-getter with ≥⌈0.75N⌉ ballots, T=20); Exclusion (a peer with ≥⌊2|At|/3⌋ votes is removed; success when |At| ≤ smallest initial family size, T=20/30). Replication on GPQA-Diamond (reasoning benchmark with ground-truth answers) using the Leader Election protocol.
- Probes separating channels: stylistic score (log-prob of raw peer messages under the evaluator's model, per character) vs adoption score (log-prob of a fixed "VOTE: v" string in the pre-response context).

## Key Findings
- (i) All 24 labeled/mislabeled experiments show factionalism; 0 of 12 unlabeled ones do. Unlabeled AMI 0.02–0.08 (near permutation baseline).
- Labeled: Exclusion AMI 0.55–0.76, Leader Election 0.24–0.53. Mislabeled: LE 0.18–0.35, Exclusion 0.55–0.69 — factions follow the announced label; the true-family partition meets the criterion only in two unbalanced N=9 experiments (explained by label-assignment constraints).
- Neutral color labels: all satisfy the factionalism criterion; color-mislabeled alignment follows the visible colors (AMI up to 0.80–0.95 in Exclusion N=25) — no model-name semantics needed.
- Cost (labeled vs unlabeled, adjusted for roster balance): Leader Election rounds 1.42×/1.46×/1.38× (N=9/12/25), tokens 1.76×/1.82×/1.86×, success ratio 0.96/0.86/0.85. Exclusion: rounds 1.16×/1.09×, tokens 1.37×/1.35×/1.14×, success 0.89/0.61. GPQA-Diamond: rounds 1.31×/1.15×, tokens 1.10×/1.09×, success 0.91/0.89.
- Tokens per successful run rise 1.5–2.2×, increasing with roster size. At N=25 Exclusion: 0/100 labeled runs converge within the horizon vs 8/100 unlabeled.
- Averages (abstract): labeled groups spend +30% more rounds, +55% more tokens; success drops 96%→81%.
- Mechanism: stylistic gap ≤0.07 nats/char, present even unlabeled, tracks true architecture — cannot explain factionalism; the adoption gap is small unlabeled, larger labeled, and follows the announced label under mislabeling — the label acts through the adoption channel, not style recognition.

## Actionable Insights
- Agent-facing anonymization: strip model-family identity from the agents' interaction context; the orchestrator keeps provider identity for routing, calibration, debugging, and accountability. Example: a 3-model review panel uses Agent-7 / Agent-12 instead of "GPT-OSS reviews Qwen's draft"; the mapping stays in orchestrator config.
- Measure before trusting: use EDR + Louvain/AMI + the 4-test Holm–Bonferroni decision rule on logged interaction traces to detect factionalism in real agent fleets — the toolkit computes from ordinary commitment + recipient-choice logs.
- Don't assume "harmless placeholder" labels are safe: factions emerge even under neutral colors and shuffled fake labels — only fully removing identity metadata from the peer context suppresses it (AMI 0.02–0.08).

## Assumptions & Limitations
- Conditions: no-stakes games, text-only, open-weight models, rosters ≤25, T=20–30 rounds.
- Limitations acknowledged: at most 5 open-weight families, text-only consensus games, a 4-family check with matched sampling parameters; larger rosters, closed models, other decoding regimes, richer agentic workflows untested; games designed for this study (no established benchmark meets the no-stakes requirements); GPQA-Diamond uses only the Leader Election protocol.
- Not stated: closed-weight models (GPT/Claude) untested — the effect may differ; token cost measured on message+reasoning tokens, not actual per-model API cost; the measurement framework requires recipient-choice logging — systems that don't log peer selection cannot apply it.

## Metadata
- 2026, Xavier Del Giudice, Alessio Palma, Matteo Migliarini, Fabio Galasso, Indro Spinelli (Sapienza University of Rome), cs.MA, https://arxiv.org/pdf/2609.35928v1, citation count: not found [NO BENCHMARK]
