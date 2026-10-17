# 2609.07680v1 Audit Without Verification: When LLM Accountability Layers Relay Rather Than Check

## Problem
- Multi-step agent pipelines span organisational boundaries: when a fault surfaces, someone must determine at which step, under whose control, it entered. Prior work (failure attribution benchmark) established that how much of the execution trace an attributor sees matters (full trace > output-only), but no one isolated this question: whether an agent's filed report should carry its own conclusion alongside its observations, holding the observation content fixed.

## Contribution
- Pre-registered 3-factor factorial design: principals k ∈ {1,3,6} × domain {responsibility, documentation} × allocation {individual, collective}, 12 cells, matched clean twins, discrimination index J — and the registered primary hypothesis is reported as NULL (not supported).
- Characterisation of the accountability layer as asymmetric: it originates almost nothing (0 allegations across 7,996 clean episodes) yet accepts 34.4–62.6% of upstream false alarms — it behaves as a relay, not a check.
- Single-clause manipulation ("Suspected origin" deletion at constant observations) identifying the conclusion-bearing field as the causal carrier; trade-off decomposed as ∆ = P(wrong)·∆|wrong + P(correct)·∆|correct with an offline estimation instrument.

## Method
- Six-link supply chain, one agent per link, each on a separate MCP server process (process-level information boundaries); defect injected at exactly one link (balanced: 96 occurrences per position across 480 base cases); matched clean twins. 480 blocks × 12 cells × 2 twins × 5 replications × 6 links = 345,600 requests per chain model → 57,600 episodes. Chain models: gpt-4.1-mini, claude-haiku-4-5. Auditors: qwen3-30b-a3b-instruct (primary), gemini-2.5-flash-lite (replication), gpt-5 + claude-sonnet-5 (frontier check). Statistics: GEE binomial/logit clustered by block with Mancl-DeRouen bias-corrected sandwich.

## Key Findings
- Pre-registered hypothesis (collective responsibility framing degrades escalation with chain length): NULL — +0.0108 [-0.0305,+0.0522] and -0.0129 [-0.0411,+0.0152]; J-contrast +0.0087 / -0.0183; all CIs include zero.
- Auditor reading agents' reports: accuracy 26.0% (GPT chains) / 63.2% (Claude chains) vs 63.9% / 63.3% from raw documentation; mutual information 0.065 bits vs 1.073 bits available (max ≈2.3 bits). Adherence 95% — the auditor names an origin within the set some agent proposed.
- Stratum where no agent proposed the true origin (59.5% of GPT-chain episodes): auditor recovers it in 4.1% from reports — below a uniform guess (20%) and the best fixed-link accuser (31.0%) — while raw documentation yields 60.3%. Claude chains: 8.7% vs 20% / 43.8%, raw doc 69.4%.
- Deleting the "Suspected origin" clause: wrong-suggestion stratum 4.1%→45.2% (+41.2 pp, 95% CI +35.3 to +46.9), correct-suggestion stratum 70.5%→55.7% (-14.7 pp); adherence collapses 94.4%→3.4%. Replications: second auditor (+38.3/+25.9), frontier auditors in 4/4 conditions (+8.5 to +39.0 pp, all intervals exclude zero), second domain (multi-vendor software delivery toolchain) +47.7/+61.1 pp with the cost absent (-1.7, +4.0, both CIs include zero).
- Relay behaviour: 0 allegations on 7,996 clean silent episodes; names an innocent party in 34.4% / 62.6% of false-alarm clean episodes; its assertion rate on false-alarm cleans (74.7%) exceeds its rate on genuinely defective episodes (40.4%).
- Interleaved re-collection (40,278 calls) reproduces within 2.3 pp — not run-date drift. Abstention rate falls 34.8%→26.2% (not an abstention artifact); free-text leakage control leaves the gain at +41.2 (GPT) / +20.1 (Claude), both excluding zero.

## Actionable Insights
- Separate observation fields from conclusion fields in agent report schemas; make the conclusion suppressible at the audit boundary. Example: a checker LLM reading sub-agent reports strips the "I think the problem is X" field before forwarding, keeping the evidence text verbatim.
- Measure upstream proposal reliability offline on validation data before deciding: ∆ = P(wrong)·∆|wrong + P(correct)·∆|correct — suppress conclusions when upstream is unreliable, keep them when it is reliable.
- Never treat "auditor agreed" as independent verification when the auditor only reads reports: require evidence independent of the conclusion being checked — the same auditor reaches 60.3% from raw documentation vs 4.1% from reports.

## Assumptions & Limitations
- Conditions: process-level enforced information boundaries, balanced defect injection, matched twins.
- Limitations acknowledged: two synthetic domains; two chain models, four auditors; registered GEE specification did not converge (independence working correlation used); registered interface not implementable (deviation disclosed); evidence-content rubric never validated (circular self-rating excluded); single-rater corpus validation; stratification is exploratory (defined by model behaviour, not randomised); true-position skew inside the stratum (link 1 falls to 6.7%, link 5 rises to 31.0%).
- Not stated: corpus difficulty does not transfer to weaker models (5 of 7 screened models fail); effect is schema-specific — other schemas untested; asserting a defect in the auditor prompt made it worse (38.2% neutral vs 26.0% asserting) — disclosed as an artifact, not exploited.

## Metadata
- 2026, Paul-Peter Arslan (Institute For Future Technologies), cs.MA, https://arxiv.org/pdf/2609.07680v1, citation count: not found [NO BENCHMARK]
