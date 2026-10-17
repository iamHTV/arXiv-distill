# Skill: Factionalism Detection & Agent-Facing Anonymization
Source: 2609.35928v1
Type: evaluation-method + workflow

## When to use this skill
- A multi-agent system mixes several model families (heterogeneous fleet) and agents can see each other's identity (names, headers, model labels in system prompts).
- Consensus/coordination tasks (leader election, exclusion, review panels) where factionalism slows decisions and lowers success.
- DO NOT use: single-model systems; tasks without peer interaction; or fleets where agents are already fully anonymous (nothing to strip).

## Inputs required
- Interaction trace logs: per round, each agent's commitment (vote/decision) and its recipient list (peers who received its message). If recipient choice is not logged, enable logging first.
- The identity labels currently visible to agents (model family, names, tags).
- Roster composition: agents per family (balanced/unbalanced).

## Steps
1. **Build the agreement graph:** from traces, compute edge weight w(i→j) = rate at which j's next-round commitment matches i's commitment when i chose j as recipient (normalize by contact volume, Eq. 1 of the paper).
2. **Measure homophily:** EDR (Edge Density Ratio) = mean within-label / between-label edge weight; run a per-run permutation null test (shuffle labels, keep group sizes).
3. **Measure community structure:** symmetrize the graph (sum both directions, missing = 0), weight by match counts, run Louvain community detection, compute AMI (Adjusted Mutual Information) between communities and the label partition.
4. **Apply the decision rule:** 4 tests (2 EDR + 2 AMI), Holm–Bonferroni correction at α=0.05 — declare factionalism only when all four pass (EDR is necessary but not sufficient).
5. **Anonymize:** remove model-family identity from the agents' interaction context (names → Agent-k, drop model headers, drop family labels in system prompts); the orchestrator keeps the mapping for routing, calibration, debugging, accountability.
6. **A/B verify:** rerun the same config (≥50 seeds) labeled vs anonymized; measure rounds, tokens, success; compute tokens per successful run — expect anonymized: rounds ~1.0× (vs 1.38–1.46×), tokens ~1.0× (vs 1.35–1.86×), success ratio back to baseline.

## Expected output
- AMI/EDR report per configuration + factionalism verdict (4-test pass/fail).
- After anonymization: AMI back to 0.02–0.08 (permutation baseline), tokens per successful run down 1.5–2.2×.

## Example application
- 9-agent content review workflow (3 Gemma, 3 Qwen, 3 GLM) with model names visible: log 50 runs → AMI 0.43 (Exclusion-like), EDR significant, 4/4 tests pass → factionalism confirmed. Rename to Agent-1..Agent-9, orchestrator keeps the map → 50 new runs: AMI 0.05, rounds 1.42×→1.00×, success 0.89→0.96 baseline.

## Gotchas
- EDR alone is insufficient: homophily is necessary but not sufficient — community alignment (AMI) is also required, and the decision rule demands all 4 tests pass.
- Normalize contact volume: a pair that communicates more must not get a higher weight just for talking more (ratio, Eq. 1).
- Mislabeled control: if you suspect the effect comes from style recognition rather than labels — run mislabeled (shuffled labels) plus the stylistic-vs-adoption probe: factions following the announced label = label-driven, not style.
- Unbalanced rosters: include balance as a covariate in the GLM when comparing costs, or results skew.
- N=25 Exclusion: labeled runs may never converge (0/100) — compare success rates, not round counts.
- Neutral color labels also cause factions (AMI up to 0.95) — "renaming models to color codes" is NOT a fix; only fully removing identity from the peer context works.
