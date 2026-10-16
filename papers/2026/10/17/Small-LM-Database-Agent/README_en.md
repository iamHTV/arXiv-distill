# 2609.21341 — What Stops a Small Language Model From Driving a Database Agent

## Problem
- Prevailing framing: a capability threshold — below some parameter count a model cannot sustain a tool-calling loop. Its prediction: failures should look like models that do NOT act. Observed: close to the opposite — most failures are models that DID act, established something true, then lost it at the model–server boundary.

## Contribution
- Production-scale field record: 11 days, 8,199 runs, 40 models (39 open-weight local + 1 hosted), 110,711 ledger events, 14,008 refused tool calls on the LibreDB Studio agent (6 surfaces)
- 4-class failure taxonomy (clock, capability, verification, transport) + transport decomposition from captured tool-call arguments + 5 server-side interventions + 2 measurement confounds

## Method
- Constrained agent loop + verifier: every claim in a report must cite an artifact (correlation id of a completed read, or schema-snapshot fingerprint) — anti-hallucination, and a substantial source of loss. Verifier (not a human judge): answered/unanswered; succeeded ≠ pass (2,204 model-stopped runs, 1,405 unanswered).
- Classification in load-bearing order: clock (timeout/turn-limit/deadline) → capability (invoked no tool) → verification (report filed then rejected) → transport (invoked tools, no timeout, no deliverable).

## Key Findings
- 2,100 model-attributed agent-mode losses: transport 761 (36.2%), clock 542 (25.8%), verification 434 (20.7%), capability 363 (17.3%). 75.7% of losses (1,590) came from runs that invoked ≥1 tool — holds in 99.7% of clustered resamples, 15 of 22 models. Capability is the SMALLEST class — the capability-threshold framing is wrong.
- Transport decomposition: of 69 stopping turns examined, 27 contained a complete, correct tool call (true claims, populated evidence, genuine correlation id) written into the assistant text channel instead of being called. None of the 27 parse as JSON; 24 fail identically (array closes twice); 20 use key "name", 7 use "action".
- 5 server changes (no model/prompt/sampling change): granite4.2:3b 21→28/30, mistral-nemo:12b 18→26, llama3.1:8b 10→24, cogito:8b 0→21, glm4:latest 0→16, deepseek-r1:8b 18→24/28. The isolated text-channel reader alone gave +1,0,0,−1 (within variance) — the argument-shape readers moved the table.
- Pass rate by surface: planning 83.2% → data-analysis 38.8%; the ordering tracks how many schema-constrained objects the model must emit, not intuitive difficulty.

## Actionable Insights
- Measure failure with a structured ledger (record arguments verbatim + refusal codes + verdicts), not process exit — production ledgers record only refusal codes; arguments were invisible for ten days; capturing them exposed 5 server defects.
- Repair server-side before blaming the model: 5 changes touching no model/prompt/sampling moved 6 models by 6–21 cells of 30 — transport failures are mechanical shapes, fixable by recognizing calls by naming rather than strict JSON parsing.
- Control memory confounds before concluding "the model is weak": cap serving context (a 12B model with a 262k-token window held 51 GB RAM on a 64 GB machine → planning cell 0/5; capped at 32k → 5/5); watch swap growth, not free memory.

## Assumptions & Limitations
- Uncontrolled field observations, not randomized; run counts per model 3–629 (operational interest); taxonomy shares over 2,100 losses are the more robust figure than per-model rates.
- Section 5 figures were taken before the context cap → per-model rates are a lower bound with unknown bias (large-context models penalized more).
- Single machine, single database, single harness; the 450s run deadline is a hard boundary (one 8B model passes at 443–444s, fails at the deadline).

## Metadata
- 2026, Cevheri Bozoğlan, Yusuf Gündoğdu, Abdullah Kaya, Koray Şirin (independent researchers, LibreDB Studio contributors), cs.SE, https://arxiv.org/pdf/2609.21341
