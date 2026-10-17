# [2609.01556v1] Retrieved but not ranked: surface-form bias in structural retrieval, from mathematics to agent trajectories

## Problem
- Embedding retrieval is usually validated where surface form and meaning point the same way. Prior work does not address the case where they are pulled apart on purpose — retrieving items that share underlying structure but not wording, in two unrelated domains under one protocol.

## Contribution
- Two-domain evaluation of structural retrieval under a shared protocol: tiered disguise-requiring gold, exact chance baselines, rank-1 failure taxonomy, and bootstrap confidence intervals on every headline number.
- Evidence that embedding retrieval anchors on literal surface content in both domains: zero rank-1 accuracy under heavy disguise in mathematics with the answer retrievable below, and below-chance retrieval in trajectories once gold excludes the query's literal object and receptacle tokens.
- The lexical-control sign flip: the same lexical reranker damages mathematical retrieval and improves trajectory retrieval. A token-class ablation locates the mechanism, and the control's sign serves as a cheap diagnostic of a benchmark's surface-variation regime.
- A judge-dependence result for LLM reranking: recovery direction replicates across three independently trained judges in both domains, while effect size, tier profile, and even which judge is the outlier change with domain.
- A contamination probe: reranking gains concentrate on well-known competitions, confidently non-null in one of six judge-by-candidate cells under bootstrap resampling.
- A paired downstream null: oracle retrieval and adversarially bad retrieval are statistically indistinguishable (McNemar p = 0.678).

## Method (core summary)
- Shared protocol across both domains: mathematics (MathNet-Retrieve; 500 queries against 117,088-item corpus) and embodied-agent trajectories (ALFWorld-derived; 118 queries against 336 trajectories).
- Mathematics queries have three LLM-generated equivalent reformulations (easy, medium, hard disguise) and near-miss decoys that keep surface form and change mathematics. Corpora are byte-identical across tiers; only the gold designation changes.
- Metrics: strict Hit@k and lenient Hit@10. At hard tier, strict Hit@1 is 0.0% (degenerate — no bootstrap resample contains a hit); lenient Hit@10 is 99-100%.
- Failure structure: 84-98% of misses are the query's own planted near-miss; in 95.2-99.8% of misses, the false positive is more lexically similar to the query than gold is.
- Lexical reranker control vs LLM reranker (three judges: Gemini-j, GLM-j, Haiku-j), with bootstrap confidence intervals.

## Key Findings
- 2 authors, arXiv category: cs.LG.
- Mathematics: Strict Hit@1 at heaviest disguise tier is 0.0% for both production embedders (bootstrap 95% CI [0.0, 0.0]); correct item in top 10 nearly always; in 95.2-99.8% of misses, the winning candidate is more lexically similar to the query than gold.
- Trajectories: models land at or near hypergeometric chance when gold must involve a different target object; below chance for all three embedders when gold must involve a different object and receptacle.
- Lexical reranker: hurts in mathematics, helps in trajectories (closing 26-36% of recoverable gap).
- LLM reranker: recovers 5-63% of gap in mathematics, 43-76% in trajectories. Direction replicates across three judges (all 21 judge-by-configuration cells positive).
- Mathematics reranking gains concentrate on well-known competitions (+19.8 points, CI [+6.7, +33.2]).
- Paired downstream: oracle retrieval and adversarial retrieval are statistically indistinguishable (McNemar p = 0.678); complete-answers-only analysis shows 69.5% zero-shot accuracy is largely a truncation proxy.

## Actionable Insights
1. Embedding retrieval anchors on literal surface content rather than underlying structure. Application: evaluate retrieval systems on structural cases (same structure, different wording) rather than only surface-form-aligned cases.
2. The lexical-control sign flip depends on how benchmark surface variation was built (adversarial vs incidental). Application: use a lexical reranker as a cheap diagnostic of a benchmark's surface-variation regime.

## Assumptions & Limitations
- Mathematics uses a single fixed seed; bootstrap CIs quantify within-sample uncertainty only.
- Three judges is a small sample; magnitudes vary more than eightfold among them; each domain has a different outlier and tier profile.

## Metadata
- Year: 2026, authors: Nabira Rashid, Manolis Kellis (Independent; MIT CSAIL Kellis Lab; MIT CSAIL), arXiv category: cs.LG, PDF link: https://arxiv.org/pdf/2609.01556v1
