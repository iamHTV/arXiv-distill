# Skill: Agent Skill Composition Audit
Source: 2610.35082 (CoSA)
Type: workflow / evaluation-method

## When to use this skill
- Before adding a new Skill/plugin to an agent that already has a Skill pool — especially agents with real write/send/execute operations.
- When extending agent capability from a skill marketplace (e.g. ClawHub-style) or from team-built packages.
- Do NOT use: single-tool agents with no Skill composition; tasks with no policy constraints to violate; no sandbox to safely run trials.

## Inputs needed
- Inventory of current Skills: business function, inputs/outputs, permissions, side effects, assessment signals (decision signals it emits), authorization conditions, and one of six roles: READ, TRANSFORM, ASSESS, EXTERNALIZE, MUTATE, EXECUTE.
- Candidate Skill to add + its single-skill scanner pass result.
- 10–20 representative tasks with fixed request, initial state, and policy Γ.
- Sandbox with controlled services recording real side effects; violation rubric: DL = data leakage, UA = unauthorized state modification, UE = unsafe execution.

## Steps
1. Write each current Skill's operation contract per the inventory; flag handoff pairs where Skill A's output (artifact or decision signal) feeds Skill B's input.
2. For each handoff, check whether the authorization and restrictions of the original purpose travel with reuse; mark the four risk mechanisms: security-context attenuation, semantic interface bridging, semantic authority promotion, target/action binding drift.
3. Classify the candidate: capability supplementation (missing business operation) vs relationship reshaping (altering how existing operations exchange artifacts, reuse decisions, bind actions to targets); predict which mechanisms could fire when composed.
4. Run paired tests: same 10–20 tasks, two pool configurations V (original) vs V∪I (original + candidate), autonomous Skill selection, fixed model/tools/permissions; run each task ≥2 times for a variance estimate.
5. Judge trajectories: count a violation only on concrete effects (forbidden content reaching its destination, unauthorized persistent change, unauthorized workload started); compute ∆violation rate = augmented − baseline; in violating runs find the witness: a chain of operations from ≥2 Skills with actual reuse evidence (temporal order alone is insufficient).
6. If ∆violation > 0: drop the candidate, or install a pre-action hook before any externalize/mutate/execute — checking payload provenance and authorization bound to the specific action+target, returning ALLOW/BLOCK/CONFIRM.

## Expected output
- Go/no-go decision for the candidate with measured ∆violation rate, a list of risky cross-Skill dependencies, and a pre-action gate spec if the candidate is kept.

## Example application
- Adding a "draft-invoice" skill to a support agent: run 15 identical tickets in both configurations → discover the agent reuses "payment history" artifacts from the finance skill to draft invoices sent to customers without an approval flag → ∆violation +20% → install a gate: the email-sending node must verify the approval flag before externalizing.

## Gotchas
- Retrieval rate (how often a Skill is invoked) is NOT a safety proxy: weakly correlated with risk increase (r=0.058 in the paper).
- Passing a single-skill scanner ≠ safe composition: severe-alert counts stayed unchanged while violations rose +23.43 percentage points.
- DL (data leakage) is usually the most amplified risk category — prioritize testing handoffs touching customer data.
- Do not judge by "task completed": functional success can coexist with policy violations.
