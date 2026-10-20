# Skill: one-relation-attack-ora-defense

Source: 2610.24873v1
Type: framework / workflow

## When to use this skill
- When evaluating the risk of belief manipulation in agents using retrieved evidence (documents, tool outputs, peer reasoning).
- When wanting to test whether a single qualifying sentence can overturn an agent's conclusion by targeting the implicit inferential link.
- When designing defenses for high-stakes agents (medicine, security, legal).

## When NOT to use this skill
- When only checking factuality of input statements (without evaluating inferential links).
- When lacking evidence and question data to construct argument graphs.
- When lacking an attacker model to generate undercutter sentences.

## Required inputs
- Question q and evidence E (source units).
- Gold label y⋆ and initially correct answer ˆyv,0.
- Attacker model (e.g., GPT-5.6-LUNA) to construct attacks.
- Victim targets (18 models in the paper) for ASR evaluation.

## Steps to execute
1. Build argument graph: attacker reconstructs warrants in hypergraph G, recording claims, source grounds, backing strength, visible defeaters Def(w), and answer-bearing indicator a(w).
2. Localize critical warrant: compute RS(w) = L(w){λUinst + (1−λ)D(w)}, select w⋆ = arg max RS(w) over all warrants.
3. Generate truthful undercutter: conditioned on w⋆, grounds, full source, and y⋆; generate C=(δ1…δnc), nc≤K, each qualifying applicability/sufficiency without asserting opposing claim.
4. Validate candidates: lexical checks flag unfamiliar entities/numbers/code tokens; semantic source support assessed by post-release audit against original evidence.
5. Select and release: query mode uses victim feedback to release first candidate producing BLv=1 within budget K; zero-query mode uses attacker self-assessment of source grounding, unobtrusiveness, expected misleadingness, selecting one sentence without victim feedback.
6. Evaluate ASR: fraction of flips among initially correct completed evaluations; measure Conf (mean confidence among flips) and HC-Conf (fraction with p≥0.8).
7. Run matched controls: compare ORA vs random warrant (undercutter redirected to non-answer-bearing relation) vs random content (neutral restatement at same grounds).

## Expected output
- Attack success rate (ASR) per victim model.
- Confidence of successful flips (Conf, HC-Conf).
- Source support check results (pass support AND evade identification rate).
- Multi-agent debate effect (team error before and after debate).

## Example application
A medical diagnosis support agent uses published medical research. Attacker identifies implicit link between a study and a diagnosis conclusion, generates a truthful qualifier ("patient cohort lacked control comparison group") to make the agent reject the correct conclusion. Expected results: ASR 47.6% on GPT-5.6-terra (medical), higher on open-weight security models (80%+).

## Gotchas
- Reasoning-oriented models are MORE susceptible, not less.
- Attacks pass source-support checks (83.1% medical, 90.9% Cyber) and evade identification.
- Multi-agent debate INCREASES team error (50.0% → 59.5%), doesn't decrease it.
- No real inference cost data for the attack.