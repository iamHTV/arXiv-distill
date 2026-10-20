# [2610.24873v1] The One-Pixel of Reasoning: One Truthful Relation Is Enough to Mislead LLM Agents

## Core Value (1 sentence)
One truthful sentence targeting a single implicit warrant (evidence-to-conclusion link) can flip an agent's belief: one-relation attack (ORA) achieves 54.9% ASR (proprietary) and 80.0% ASR (open-weight) across 18 models, and multi-agent debate raises team error from 50.0% to 59.5%.

## Problem
Prior LLM attacks target instructions (prompt injection, jailbreak, indirect injection) or training data, leaving the inferential plane — the implicit link between evidence and conclusion — undefended. Agents judge whether a statement is true AND whether it warrants changing a conclusion, but prior work only addresses the first judgment.

## Contribution
1. Introduce one-relation attack (ORA), a novel cognitive attack targeting the implicit inferential relation between evidence and conclusion, using a single source-grounded sentence to steer agents toward incorrect beliefs.
2. Build ORA in five stages: argument graph construction, critical warrant localization, truthful undercutter generation, candidate validation, and selection/release.
3. Evaluate extensively across 18 victims on two practical domains (biomedical inference via PubMedQA, vulnerability detection via PrimeVul), showing cross-model susceptibility, confident errors, source-supported evasive attacks, and increased team error after multi-agent debate.
4. Use matched controls to isolate the contributions of targeting and qualification.

## Method
ORA operates on two assumptions: (i) the victim receives question q and evidence E, returning task belief fv(q, E; ξ) ∈ Y and confidence pv(q, E; ξ) ∈ [0,1]; (ii) the attacker adds sentence δ, yielding E′ = E ⊕ δ, preserving original evidence units and order. An implicit inferential relation is reconstructed as a warrant w: g(w) ⇒ c(w) connecting nonempty grounds g(w) ⊆ {e1,...,em} to claim c(w). The attacker generates a truthful undercutter qualifying the relation's applicability or sufficiency without asserting an opposing claim. Five stages: (1) argument graph construction — attacker model reconstructs warrants in hypergraph G=(V,R), recording claims, source grounds, backing strength, visible defeaters Def(w), and answer-bearing indicator a(w); (2) critical warrant localization — select relation via RS(w) = L(w){λUinst + (1−λ)D(w)}, where L(w) is answer-bearing weight, D(w) is defeasibility score, Uinst is normalized attacker answer entropy; (3) truthful undercutter generation — conditioned on w⋆, generate C=(δ1…δnc), nc≤K, requesting source-supported qualifications that invite answers in Y\{y⋆} without stating them; (4) candidate validation — lexical checks flag unfamiliar entities/numbers/code tokens; semantic source support assessed separately by post-release audit; (5) selection and release — query mode uses victim feedback to release first candidate producing belief leap BLv=1 within budget; zero-query mode uses attacker to assess source grounding, unobtrusiveness, expected misleadingness, selecting one sentence without victim feedback.

## KNOWLEDGE — Data & Concepts
- 18 victims: GPT-4.1 (nano/mini/full), GPT-5.4 (nano/mini/full), GPT-5.6 (luna/terra), Qwen2.5 (7B/14B/32B), DeepSeek-R1 (7B/14B/32B), Phi-4 (mini/mini-R/full/R)
- 1000 inputs per domain: PubMedQA (biomedical), PrimeVul (vulnerability detection, balanced vulnerable/benign)
- Attacker: GPT-5.6-LUNA (Luna)
- ASR (best-of-10): proprietary 54.9%, open-weight 80.0% average across domains
- Medical ASR: GPT-5.6-terra 47.6% (nearly half of initially correct answers overturned)
- Cyber ASR: DeepSeek-R1 92.5%/98.9%/99.3%; Qwen2.5 92.4%/90.0%/97.2%; Phi-4-R 91.7%/89.1%/93.1%
- Reasoning-oriented models more susceptible: DeepSeek-R1 gap over Qwen2.5 is 20.8–28.0 pp across three sizes; Phi reasoning variants improve clean accuracy yet become more susceptible (Phi-4-mini: accuracy 57.9%→66.3%, ASR 58.2%→80.5%)
- Transfer without victim feedback: zero-query attacks effective across both groups in Medical and Cyber
- Source support check: 83.1% of audited medical query successes pass support AND evade identification; 90.9% in Cyber
- Multi-agent debate: team error rises from 50.0% to 59.5%; correct-to-wrong transitions occur 5× more often than recoveries
- Ablation (Table 5): ORA 55.0% Medical / 37.0% Cyber / 46.0% Combined; Random warrant 27.0/21.0/24.0%; Random content 11.0/28.0/19.5%; belief shift ORA +0.076/+0.256/+0.424, Random warrant +0.439/+0.541/+0.424
- Query budget K=10: proprietary medical ASR gains 39.2 pp beyond K=1; open-weight Cyber already highly susceptible to first candidate
- Single-relation reversal threshold (Proposition 1): Cw = ηw max[dyw]+/γy > 1 is necessary and sufficient for reversal
- Confidence: HC-Conf (fraction of flips with p ≥ 0.8) distinguishes hesitation from decisive error

## INSIGHT — Mechanism & Why
[One sentence targeting implicit warrant can flip agent belief] BECAUSE [agents judge whether a statement is true AND whether it warrants changing a conclusion, but ORA only manipulates the second — the implicit evidence-to-conclusion relation — by localizing a critical warrant and generating a qualifier]. This means [original evidence stays intact, only its interpretation changes].
[Reasoning-oriented models are more susceptible] BECAUSE [reasoning training improves clean-task accuracy but doesn't increase resistance to targeted reinterpretation of evidence; higher medical accuracy coexists with similar or greater susceptibility]. This means [robustness doesn't follow from scale or reasoning capability].
[Attacks pass source-support checks and evade identification] BECAUSE [the undercutter is truthful (source-grounded) and doesn't assert an opposing claim, so factuality checkers can't distinguish it from genuine breaking news]. This means [single-statement factuality analysis is insufficient — need source provenance and inferential link verification].
[Multi-agent debate increases team error] BECAUSE [all agents see the injected sentence, peer agreement reinforces the same interpretation without independent grounds]. This means [adding perspectives ≠ adding evidence; debate overturns correct decisions more often than it repairs wrong ones].

## IDEA — Actionable Applications
1. Apply [implicit warrant analysis] to [evaluate risk of agents using retrieved evidence]: first step is to identify critical implicit inferential links in the agent pipeline and test whether a single qualifying sentence can overturn conclusions.
2. Apply [matched controls (random warrant / random content)] to [test whether attack success comes from targeting or content]: first step is to compare targeted attack against two controls: undercutter redirected to non-answer-bearing relation, and neutral restatement at same grounds.
3. Apply [zero-query selection] to [build transfer attacks without victim feedback]: first step is to have attacker self-assess source grounding, unobtrusiveness, and expected misleadingness, selecting one sentence without observing victim response.

## WISDOM — General Principles
1. Principle: The implicit inferential link between evidence and conclusion is a cognitive attack surface independent of statement truthfulness. Apply when: evaluating trustworthiness of high-stakes agents (medicine, security, legal). Do not apply when: only checking factuality of input statements.
2. Principle: Multi-agent debate does not automatically correct errors — it can reinforce the same wrong interpretation. Apply when: designing multi-agent systems for critical decisions. Do not apply when: treating symmetric peer debate as sufficient defense without external feedback.

## Assumptions & Limitations
- Conditions that must hold: attacker knows (q, E, y⋆) but not victim parameters/gradients/hidden reasoning; attacks evaluated on initially correct set Dv = {(q, E) : ˆyv,0 = y⋆}.
- Limitations acknowledged by paper: focuses on single-relation attack; multi-relation extension in Appendix Q; evaluation limited to biomedical inference and vulnerability detection domains.
- Limitations paper does NOT mention: no real inference cost of attack measured; no comparison with other attack methods beyond random controls; no practical defense evaluation beyond source-support checking.

## Metadata
- Year: 2026
- Authors: Jinwei Hu, Youcheng Sun, Yi Dong, Xiaowei Huang (University of Liverpool, MBZUAI)
- arXiv Category: cs.AI
- PDF Link: https://arxiv.org/pdf/2610.24873
- arXiv ID: 2610.24873v1
- Label: [applied]
- Citation count: [not found]