# [2605.31581v1] Choosing the Lens: Strategic Perspective Activation in Context-Dependent Argumentation

## Problem
Prior work fails to address strategic manipulation in argumentation because: Dung's framework and Value-Based Argumentation Frameworks (VAFs) both treat the evaluation regime as fixed — there is no formal mechanism for an agent to choose which "lens" applies when evaluating arguments. VAFs allow reranking values but not deactivating them, so strategic options are limited.

## Contribution
1. **Context-Dependent Argumentation Frameworks (CDAFs)**: Extends Dung's theory — defeat function δ determines per-context which attacks succeed, rather than being fixed
2. **Perspective-labeled CDAF**: Derives defeat function from relevance set ρ (agent's action space) and priority π (institutional structure). Agent chooses ρ, cannot change π
3. **ACTIVATION-MANIPULATION problem**: Decision problem — can the agent choose ρ such that the target argument is accepted? Baseline complexity bounds are recorded

## Method (core summary)
CDAF = ⟨𝒜, R, 𝒞, δ⟩: arguments 𝒜, attack relation R, contexts 𝒞, defeat function δ. Perspective-labeled specialization: each argument has source perspective src(a) ∈ Π. Context c activates subset ρ(c) ⊆ Π with priority π. Attack (a,b) is active when src(a) ∈ ρ(c) ∧ π(src(a)) ≥ π(src(b)). Key asymmetry: deactivating a perspective removes attacks mounted by its arguments, but the arguments remain eligible for acceptance. Worked example: argument t is rejected under every full-relevance injective priority (structural trap: defender b also attacks t), but accepted under ρ={β,γ} (deactivate α, d defends t against b).

## Key Findings
- [NO BENCHMARK] — purely theoretical, no empirical evaluation
- Result 1: Under full relevance (ρ=Π), target argument t is rejected for EVERY injective priority — structural trap where defender doubles as attacker
- Result 2: Under partial activation (ρ={β,γ}), t is accepted — deactivating α breaks the trap
- Key insight: Partial perspective activation has strategic power that VAF audiences do NOT have — VAFs can only rerank, not deactivate
- Complexity: ACTIVATION-MANIPULATION baseline bounds recorded, tight bounds left open

## Actionable Insights
1. **Choose evaluation lens before arguing**: When proposing an idea, don't fight on every front. Select the subset of stakeholders/lenses where the proposal is strongest. Example: technical proposal → activate performance + reliability reviewers, deactivate finance lens if cost argument is weak.

2. **Deactivate hostile perspectives**: If an argument is attacked from a perspective you cannot win, deactivate it instead of counter-arguing. Example: product launch proposal attacked by finance reviewer on cost → instead of arguing cost, redirect discussion to user impact lens (ρ={user_impact, market_share}), finance perspective remains present but is not an active attacker.

3. **Structural trap awareness**: When a defender is also an attacker (same perspective), the argument is trapped. Solution: introduce an external perspective (d) that defends without attacking back. Example: if engineering argument both defends and attacks the proposal → introduce customer success perspective to defend without conflict.

## Assumptions & Limitations
**Conditions for the framework to work:**
- Arguments and attack relations must be determined in advance (fixed structure)
- Agent must have influence over which perspectives are activated (ρ)
- Priority π is institutional structure, agent cannot change it

**Limitations the paper acknowledges:**
- Only a small worked example, no scalability study
- Tight complexity bounds left open
- Multi-agent variants left open
- Fuller study beyond scope

**Limitations the paper does NOT mention:**
- Does not discuss how to determine perspectives Π in practice
- Does not address dynamic argumentation (arguments evolve over time)
- Does not consider partial information (agent doesn't know others' π)
- Purely formal — no empirical validation on real decision scenarios
- Does not address persuasion ethics (deactivation = manipulation?)

## Metadata
- Year: 2026
- Authors: Albert Sadowski, Jarosław A. Chudziak (Warsaw University of Technology)
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.31581v1
- Citation count: [EXTRACTION FAILED]
