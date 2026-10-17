# Skill: Audit-Boundary Report Schema (separating observation from conclusion in agent reports)
Source: 2609.07680v1
Type: workflow

## When to use this skill
- Building an accountability/audit layer for a multi-agent pipeline where the auditor only receives agents' filed reports, not full execution traces.
- Multi-vendor pipelines where each step is controlled by a different party and faults must be attributed to the correct step.
- DO NOT use: the auditor already has access to raw logs/full traces (full-trace attribution already beats output-only); or a single-step pipeline with no upstream.

## Inputs required
- Current report schema of the agents (fields: escalation flag, anomaly type, suspected origin, free-text evidence).
- Representative validation data with ground truth on the faulty step, large enough (paper: 480 base cases × replications).
- An auditor model distinct from the chain models (avoid same-model coupling).

## Steps
1. **Inventory the schema:** tag every field as observation or conclusion. The conclusion-bearing field ("Suspected origin: step N") is the dependence carrier — the skill's target.
2. **Measure upstream reliability offline:** on validation data, compute P(agents' proposed set contains the true origin). Paper measurements: 40.5% (GPT chains) and 65.3% (Claude chains).
3. **Measure both conditional magnitudes:** run the auditor on two report variants — full field vs conclusion clause deleted — split by stratum (suggestion wrong vs correct). Compute ∆|wrong and ∆|correct (paper: +41.2 pp and -14.7 pp on GPT chains).
4. **Compute the trade-off sign:** ∆ = P(wrong)·∆|wrong + P(correct)·∆|correct. Weak upstream (high P(wrong)) → deleting the conclusion pays; strong upstream → keep it.
5. **Design a two-zone schema:** observation fields and conclusion fields separated; conclusions suppressible at the audit boundary — available to consumers who benefit, withholdable from the component whose independence it compromises.
6. **Verify auditor independence:** measure mutual information between auditor output and available information (paper: 0.065 bits vs 1.073 bits — near zero means relay); run a clean-episode origination test (zero allegations on clean episodes is the bar); compare against a fixed-link accuser baseline and uniform guess.

## Expected output
- A per-field carry/suppress decision for the report schema, with an expected ∆ estimate.
- Auditor mutual-information report + origination rate on clean episodes — evidence the auditor is a check, not a relay.

## Example application
- 3-agent content pipeline (writer → editor → publisher): editor report carries "Suspected origin: writer". Measured on 200 validation cases: writer proposes correctly 45% of the time → P(wrong)=0.55. Auditor with full report: 30% accuracy on the wrong stratum, 70% on the correct stratum; with clause deleted: 65% (+35) and 58% (-12). ∆ = 0.55×35 + 0.45×(-12) = +13.85 pp → enable conclusion suppression for the auditor, split the fields in the schema.

## Gotchas
- Abstention confound: check abstention rates in both conditions — if deleting the clause makes the auditor abstain more, accuracy gains may be an artifact. Paper: abstention falls 34.8%→26.2%, so not a confound.
- Free-text leakage: the free-text report may still name the true origin — exclude leaking episodes and recompute (paper: gain stays +41.2 GPT, +20.1 Claude).
- Asserting prompt: never write "a defect was introduced" in the auditor prompt — it makes the auditor worse (38.2% neutral vs 26.0% asserting); use a neutral prompt stating a defect may or may not exist.
- Stratification by model behaviour skews true positions (link 1 is over-accused) → use within-stratum comparators, do not carry the design-level 20% baseline into the stratum.
- Re-collect interleaved: run both conditions shuffled together in a single execution to rule out run-date drift (model/API changes between runs).
