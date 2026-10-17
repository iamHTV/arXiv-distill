# Skill: Evidence-Aware Agent Orchestration
Source: 2608.26990v1
Type: framework / workflow

## When to use this skill
- Building an LLM-agent system for research/reporting where evidence is heterogeneous (many sources, unequal quality) and multiple models/providers are involved.
- You want two tiers: a cheap default path for batch/scheduled work and an agentic path for deep analysis — without forcing multi-agent on every request.
- Optional skill/plugin extensions whose outputs need gating before entering the evidence chain.
- DO NOT use: systems needing only a single LLM call; or already-homogeneous evidence pipelines (uniform quality, uniform sources) — no state tagging needed.

## Inputs required
- List of data sources and the fields each supports (market adapters: quotes, bars, fundamentals, news, sentiment...).
- List of model routes (hosted, compatible endpoints, provider-specific, local) with each route's capabilities (structured output, tool calling, vision, context limit, latency, cost).
- List of core roles (e.g., technical, intelligence, risk, decision) and optional Strategy Skills with declared metadata + tool requirements.

## Steps
1. **Evidence acquisition + state tagging:** tag every evidence block with a state ∈ {available, missing, not_supported, fallback, stale, estimated, partial, fetch_failed}; retain source + timestamp metadata; a screening engine (deterministic filters, factor scores, risk constraints, optional LLM reranking) produces a bounded candidate set.
2. **Structured context construction:** compute features, build bounded evidence blocks; project states into the prompt — the model sees "field X: fetch_failed" instead of a blank field.
3. **Model & capability routing:** separate the routing layer from research logic; resolve request format + model name per route; report unsupported capabilities instead of silently substituting a different operation; capability admission is route-specific (generation route ≠ tool-capable agent route).
4. **Role + extension admission:** core role outputs go through role-specific parsers; Strategy Skill outputs go through a signal-eligibility partition O_ext* = {o : valid_signal(o)} — invalid ones move to diagnostics, never into the evidence chain.
5. **Disagreement-aware synthesis:** build a disagreement summary D = Disagreement(O_core ∪ O_ext*) as an explicit input to the decision agent; d_0 = Synthesize(E, O_core, O_ext*, D).
6. **Conservative risk override (RiskGuard):** post-synthesis, the risk step may only downgrade — veto buy→hold; downgrade buy→hold/sell, hold→sell; never upgrade.
7. **Freeze + conformance test:** pin git revision + environment (Python, pytest, LiteLLM version); run a claim-mapped test manifest; report exactly what passes and what is NOT established (quality, forecasts, returns).

## Expected output
- A structured research report + optional inspection record (selected context, evidence-quality summary, diagnostics).
- A conformance report: N/N contract tests pass, mapped by contract family, with a boundary statement (platform-unsupported routes, dependency pins).

## Example application
- VN-stock research agent: HOSE/HNX adapters + news + fundamentals, each block state-tagged; default profile runs overnight batch (1 generation call); agentic profile has technical/intelligence/risk/decision roles + 2 skills (MA crossover, volume breakout); invalid skill outputs go to diagnostics; disagreement summary feeds the decision agent; RiskGuard downgrades only; freeze revision + 500-case pytest manifest → conformance report 500/500, with NO forecast-accuracy claim.

## Gotchas
- Mocked tests passing ≠ semantic quality: mock-service tests don't prove quality under live data/models/credentials — state the boundary explicitly.
- A post-exploration selected manifest is not a prospective sample: don't report "all tests pass" as if it were the whole suite — record which cases were deselected and why.
- Disputed heuristics: many technical-analysis perspectives (Chan theory, wave theory) are disputed financial heuristics — combining them with an LLM does NOT create predictive value; a valid schema ≠ a correct conclusion.
- Trusted extension inputs: external strategy packages are trusted inputs — prompt injection, poisoned content, and unsafe tool requests can slip through; registered interfaces reduce exposure but don't eliminate it.
- Dependency pinning: tests can fail on versions within the declared range (DSA: timeout under LiteLLM 1.98.0) → pin versions and record it.
- Optional snapshots retain selected context, not complete context — no exact replay guarantee; don't call it a full audit trail.
- Separate native platform probes: keep platform-specific checks out of the portable manifest; don't count them as portable failures.
