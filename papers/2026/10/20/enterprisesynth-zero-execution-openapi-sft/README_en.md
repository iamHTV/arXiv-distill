# [2610.22412v1] EnterpriseSynth: Zero-Execution SFT and Evaluation Data from OpenAPI Specs

## Problem
- Tool-using LLM agents need large training + evaluation datasets, but collecting execution traces from enterprise APIs is often unsafe, expensive, or infeasible: access controls, compliance constraints, rate limits, risk of modifying production data. State-of-the-art synthetic generators (ToolBench, API-Bank) call live servers and collapse behind the enterprise firewall. The paper names this the Execution Paradox: (1) high-fidelity sandboxes rarely exist for internal systems, (2) exploratory agent loops against production risk corrupting state / violating compliance / triggering destructive actions, (3) live calls bounded by latency and rate limits.

## Contribution
- EnterpriseSynth: a zero-execution framework converting an OpenAPI specification into supervised fine-tuning (SFT) trajectories and paired evaluation instances WITHOUT invoking any API.
- Combines three properties no prior framework combines: grounding in a real target spec (AgentInstruct, seeded from code, can hallucinate an API surface), a hard per-sample structural verification gate (vs AgentInstruct's soft editorial loop + LLM judge), and no live-execution dependency at any stage (vs API-Bank / ToolBench).
- Generalizing methodological finding: a verifier's correctness cannot be established by checking it accepts good input alone; it must be tested against input it is specifically supposed to reject.

## Method (core)
- Four-stage pipeline: Spec Parser -> Intent Generation Agent (Claude Sonnet 5) -> Trajectory Generation Agent (selects tool + generates parameters, reasoning, expected-response summary in one call) -> Schema Verification Engine (compiler-style firewall, deterministic, NOT an LLM call: endpoint existence, HTTP method, required parameters, parameter types).
- Jointly emits SFT dataset + EnterpriseSynth-Eval + verification metadata + intent specifications from a single generation pass.
- Fine-tuning: Qwen2.5-0.5B-Instruct via LoRA (rank 8, alpha 16, 3 epochs, LR 3e-4) — a hardware-scoped substitute for the paper's 7-8B target (Mistral-7B-Instruct / Llama-3-8B).

## Key Findings
- Spec parsing: all four extraction metrics 100% on 3 APIs (GitHub 845 methods, Stripe 446, Slack 174) — but only after two fixes: resolving $ref-shared parameters (GitHub required-param count 67 -> 1,721) and parsing requestBody schema fields as typed parameters (Stripe's POST /v1/charges declares zero OpenAPI parameters; all fields live in requestBody).
- Intent generation: 5 endpoints x 3 intents per API (45 total): 100% coverage, 100% exact-string diversity (15/15 unique) — a weak proxy (semantic clustering not implemented); manual inspection shows business-scenario-specific intents (rotate a named secret, restrict it to specific repos).
- Trajectories: TSA (tool selection accuracy) 100% GitHub/Stripe, 93.3-100% Slack; PV (parameter validity) 100% — with a self-consistency caveat: the same Claude Sonnet 5 generated intents and selected tools, so 100% measures recovering its own intent, not generalization.
- Verification (core result): valid pass rate 100% (45/45); corrupted detection 98% (43/44) — wrong method 12/12, missing required parameter 11/11, invalid path 12/12, type mismatch 8/9; an initial pass caught only 57-80%, reaching 98% only after adversarial testing forced fixes to verifier type-checking, the corruption harness, and the parser.
- Downstream (held-out Zoom, 16 intents, single run): Base 12.5% (2/16), Self-Instruct 25.0% (4/16), EnterpriseSynth 87.5% (14/16) — ~3.5x the Self-Instruct gain; PV 0.0% / 50.0% (2/4) / 57.1% (8/14).
- 5-seed sweep (mean +/- std): Zoom Base 12.5+/-0.0 / SI 23.7+/-10.3 / ES 66.2+/-18.0; DigitalOcean Base 31.2+/-0.0 / SI 37.5+/-21.2 / ES 53.7+/-13.7 (high per-seed variance: a single run can still lose); ES wins on average on all three APIs (Spotify base 46.3+/-7.1; extracted table scrambled -> per-cell Spotify values unreliable, use prose averages).
- Cold-start: 5 hand-authored never-published specs (CRM, HRIS, Procurement, Ticketing, Asset Management; 28 endpoints): Base 23.3% -> ES 40.0% (private, n=30) vs public held-out Base 18.8% -> ES 39.6% (n=48) — almost no degradation = genuine schema-grounding, not pretraining familiarity. Six more public APIs (Twilio, Notion, OpenAI, Jira, Asana, Trello) all beat baseline -> 17 APIs total.
- Readiness warning: an independent LLM-based evaluation shows endpoint-selection accuracy 48.9% FALLING to 21.3% when argument selection and values are also evaluated — endpoint-level metrics substantially overestimate end-to-end correctness.

## Actionable Insights
- Bootstrap tool-use agents for internal APIs from OpenAPI specs alone (docs already exist): 45 verified trajectories lift a 0.5B model 12.5% -> 87.5% on a held-out API — cold-start without a production sandbox. E.g. a team with a CRM REST spec generates SFT data overnight and fine-tunes a small on-prem model.
- Adversarially test every verifier: plant corrupted trajectories (wrong method / missing param / invalid path / type mismatch) and measure detection — initial 57-80% -> 98% only after fixes. Checking only "valid inputs pass" trusts a broken verifier.
- Evaluate tool-use readiness at the argument level, not endpoint level: TSA 48.9% but end-to-end (args + values) only 21.3%. E.g. an agent picking the right endpoint with a wrong item ID still counts as FAIL.

## Assumptions & Limitations
- Conditions: machine-readable OpenAPI spec exists; spec quality is the ceiling (GitHub documents auth in prose with zero securitySchemes, so auth extraction has nothing to check against).
- Authors admit: pilot scale (3-5 APIs, 45-89 examples per experiment; target ~65 specs); self-consistency confound (same model generates intents and selects tools); model-scale gap (0.5B substitute, untested at 7-8B); non-uniform generalization (DigitalOcean single-run loss is genuine variance); the structural gate is not semantic — well-typed but nonsensical values (a negated charge) still pass; workflow completeness (multi-step) N/A at pilot; prompt-only and AgentInstruct baselines not yet implemented; dependency-graph planning layer not implemented.
- Not stated: intent diversity is exact-string only (semantic diversity unmeasured); single-endpoint trajectories do not cover cascading multi-step variables (the exact intro failure mode); dependence on Claude Sonnet 5's cost/quality (open-source generator untested); OpenAPI only, no GraphQL/gRPC.

## Metadata
- Year: 2026 | Authors: Rashmi Thimmaraju (Long Island University), Natan Vidra (Anote AI), Spurthi Setty (Stevens Institute of Technology) | Category: cs.SE | PDF: https://arxiv.org/pdf/2610.22412v1 | Citations: [NO DATA — published 14 Oct 2026]
