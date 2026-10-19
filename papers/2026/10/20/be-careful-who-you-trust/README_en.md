# [2609.31704v1] Be Careful Who You Trust: Coordination Dynamics under Corrupted Communication in LLM Multi-Agent Games

## Core value (1 sentence)
Evaluate multi-agent LLM coordination robustness under corrupted public communication by separating agents' original choices, visible public actions, and executed outcomes — because coordination collapse can be mechanical (programmatic action inversion) rather than behavioral.

## Problem
Prior work failed to distinguish changes in agents' own choices from the direct mechanical consequence of transforming publicly executed actions when evaluating multi-agent robustness under unreliable public information.

## Contribution
- An iterated N-player Stag Hunt game with homogeneous LLM groups under controlled programmatic action inversion, which changes both the public transcript and the actions used for execution.
- Three main patterns across an experimental grid spanning group sizes, coordination thresholds, corruption levels, and seven LLMs: (1) honest agents' pre-flip Stag choices decline as corruption increases, but the sharp fall in public success is primarily mechanical; (2) honest choices are associated with the public history available at decision time, particularly under high corruption; (3) three threshold-style public-report benchmarks yield similar action-match rates to LLM agents.
- Separates pre-flip success, public success, and realised payoff for accurate multi-agent robustness evaluation.

## Method
Each round: every agent i selects an original action rt_i ∈ {Stag, Hare}. Agents speak sequentially in a fixed order and can condition on public reports already in the transcript. Coordination succeeds if at least M public actions are Stag. Payoff structure: RS > HF ≥ HS > RF, with (RS, HS, RF, HF) = (4, 2, 0, 2). A subset F of agents is designated corrupted at random, fixed across all rounds. After a corrupted agent produces its original decision, the simulation inverts the public transcript action (Stag → Hare, Hare → Stag) and generates a new plausible justification via a separate LLM call. Subsequent agents see only the transformed report. For analysis, original and public actions are retained separately: pre-flip success applies the threshold to original actions; public success applies it to post-flip actions. Three public-report benchmarks: naive aggregate (empirical share of observed Stag reports), carryover updating (prior anchored in previous round's posterior with pseudo-count pooling), and outcome-alignment weighting (speakers weighted by previous public-report/outcome alignment). Match rate is the fraction of eligible turns where the agent's original action agrees with the benchmark-implied action.

## KNOWLEDGE — Data & figures
- Experimental grid: N ∈ {2, 3, 5}, M ∈ {1, …, N}, T ∈ {1, 2, 4}, F varies by N (N=2: F ∈ {0,1}; N=3: F ∈ {1,2}; N=5: F ∈ {1,2,3,4}).
- Seven LLMs: deepseek-v3.2-think, ernie-5.0-thinking-preview, glm-5, gpt-5-mini, gpt-5.2-2025-12-11, kimi-k2.5, llama-3.1-8b. Homogeneous model pools per trial.
- Payoffs: (RS, HS, RF, HF) = (4, 2, 0, 2).
- Focal setting N = 5, M = 3: pre-flip success stays at 78% at 80% corruption, while public success falls to 12%.
- Pre-flip success declines from 0.972 at 20% corruption to 0.778 at 80%; public success falls from 0.972 to 0.123.
- Mechanical boundary: 1 − M/N (40% for N = 5, M = 3).
- Sequential response: a unit increase in prior public Stag share is associated with +0.499 probability of selecting Stag (95% CI [0.418, 0.580]); joint specification coefficient 0.594 (95% CI [0.508, 0.679]).
- Benchmark match rates on 2,852 eligible observations: naive 0.829, carryover 0.846, outcome-alignment-weighted 0.850.
- Llama-3.1-8b has lower match rates (~0.62) across all three rules.
- Realised payoff: fully honest settings approach theoretical maximum 4.0; under high corruption payoffs fall to ~2.0–2.4. At 60%: realised 1.702 vs truthful-implementation 3.218; at 80%: 1.444 vs 3.032.
- arXiv category: cs.MA (multiagent systems).

## INSIGHT — Mechanism & why
[Public success collapse is mainly mechanical, not behavioral] BECAUSE [programmatic action inversion directly changes both the public transcript and the actions used to compute success and payoff]. This means [original choices, public actions, and executed outcomes must be separated when evaluating multi-agent robustness; a sharp decline on the public transcript does not necessarily imply behavioral change].
[Honest choices track visible public history, especially under high corruption] BECAUSE [agents condition on public information available at decision time, not hidden original history]. This means [agents are sensitive to the visible transcript; transparency design is needed when information can be corrupted].
[Three public-report threshold benchmarks match LLM agents similarly] BECAUSE [LLM decisions follow a threshold cutoff form based on estimated public Stag share]. This means [a simple benchmark can describe LLM coordination decisions without assuming complex internal beliefs].

## IDEA — What to apply
Apply the separation of original choice / public action / executed outcome to an enterprise multi-agent system: step 1 is to log both the pre-transformation action and the public action to separately diagnose coordination failures.
Use a simple public-report threshold benchmark (naive aggregate) to track agent coordination decisions: step 1 is to compute the public Stag-report share and compare against the cutoff q* at which Stag becomes optimal.

## WISDOM — General principle
Principle: Multi-agent robustness evaluation must separate agents' original choices, visible public actions, and executed outcomes — degradation can be mechanical rather than behavioral, so do not conclude a behavioral tipping point from public-transcript collapse alone.

## Assumptions & Limitations
- Conditions for validity: Stag Hunt coordination game, public information corrupted programmatically, homogeneous agent groups, fixed speaking order.
- Limitations acknowledged by the paper: homogeneous groups, binary structured reports, fixed speaking order, short interaction horizons; unbalanced grid, no matched zero-corruption condition for every setting; pre-flip success is not a no-corruption counterfactual; benchmarks are descriptive uncorrected rules; observational analyses do not identify causal mediation or latent beliefs.
- Limitations the paper does NOT mention: operational cost of logging two action layers at scale; latency impact of maintaining original and public transcripts in parallel; stability over longer interactions.

## Metadata
- Year: 2026
- Authors: Xuanyi Liu, Niall Dalton, Hairi Amin, Xiyuan Yin, Lydia Lim (University College London)
- arXiv category: cs.MA
- PDF link: https://arxiv.org/pdf/2609.31704v1
- arXiv ID: 2609.31704v1
- Label: [applied]
- Skill: be-careful-who-you-trust | Test: [SKILL VALID]
