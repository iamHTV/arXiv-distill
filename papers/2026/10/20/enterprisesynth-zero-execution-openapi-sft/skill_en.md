# Skill: EnterpriseSynth Bootstrap — zero-execution SFT + eval data for tool-use agents from OpenAPI specs
Source: 2610.22412v1
Type: workflow / framework

## When to use this skill
- You need training data for tool-using agents on INTERNAL APIs (CRM, ERP, HRIS, ticketing) but have no safe sandbox to call the real APIs.
- Bootstrapping tool-use capability for an on-prem model from existing OpenAPI/Swagger docs alone.
- You need a paired evaluation dataset without human ground-truth annotation.
- Do NOT use: APIs that already have real execution traces (real data is better); specs that are not machine-readable (auth only in prose); complex multi-step cascading tasks — this skill is single-endpoint at pilot scale.

## Inputs needed
- OpenAPI/Swagger spec file (JSON/YAML) of the target API.
- A generation LLM (Claude Sonnet 5 class) for the intent + trajectory agents.
- A deterministic JSON-Schema validator for the verification engine — do NOT use an LLM as the gate.
- An open-weight model to fine-tune (Qwen2.5-0.5B class or larger) + LoRA setup (rank 8, alpha 16, 3 epochs, LR 3e-4).
- Held-out specs (not used in training) + ideally 5 never-published private specs for the cold-start check.

## Steps
1. Parse the spec: extract endpoints, parameters, descriptions, auth, response-schema presence. TWO mandatory fixes: (a) resolve $ref-shared parameters (missing them hides up to 1,721 required params on a GitHub-class spec), (b) parse requestBody schema fields as typed parameters (POST/PUT/PATCH usually declare fields only there). Verify against ground truth recomputed independently, not by reusing the parser's logic.
2. Intent generation: 3+ enterprise intents per endpoint (business-scenario-specific, not generic). Manually inspect samples — coverage/diversity aggregates (100%) are weak proxies; semantic clustering does not exist yet.
3. Trajectory synthesis: per intent + candidate tool list (5 source endpoints + 10 seeded distractors, shuffled per trial) -> one call selecting the tool + parameters + reasoning + expected-response summary. CAVEAT: if the same model generates intents and selects tools, 100% TSA is self-consistency, not generalization; use cross-model or human intents for real accuracy.
4. Structural verification gate (deterministic, offline): check endpoint existence, HTTP method, required parameters, parameter types; admit only valid trajectories. ADVERSARIALLY TEST the verifier itself: plant corrupted variants (wrong method / missing required param / invalid path / type mismatch) — an initial pass typically catches only 57-80%; fix the type-checker + harness + parser until >=98% (43/44) before trusting the dataset.
5. LoRA fine-tune on verified trajectories; evaluate TSA + PV (parameter validity conditioned on correct selection) on held-out specs. Use >=5 seeds: per-seed variance is high (e.g. DigitalOcean +/-13.7 vs +/-21.2 — a single run can still lose even when the average wins).
6. Argument-level evaluation: an independent LLM judge scores argument selection AND values, not just endpoints — endpoint accuracy 48.9% but end-to-end only 21.3%. Use the end-to-end number for readiness decisions.

## Expected output
- Verified SFT dataset + EnterpriseSynth-style eval set + per-sample verification metadata. Readiness report: TSA/PV per held-out API, per-seed mean+/-std, private cold-start accuracy (expect private ~= public, e.g. 40.0% vs 39.6% = genuine grounding), end-to-end argument-level accuracy.

## Example application
- A solopreneur with a CRM REST API (10 endpoints): step 1 parse -> resolve $ref + requestBody -> 38 typed params; step 2: 15 intents (3 x 5 endpoints), all unique; step 3: 15 trajectories (TSA 100% but flagged self-consistency); step 4: corruption harness of 15 -> verifier catches 14/15 (93%) < 98% -> fix -> 15/15; valid pass 15/15; step 5: LoRA fine-tune Qwen2.5-0.5B, 5 seeds: held-out mean 66.2+/-18.0 vs base 12.5+/-0.0, Self-Instruct 23.7+/-10.3, with 1 losing seed (variance); step 6: argument-level judge -> ~21% end-to-end. Result: deploy a small on-prem model with an honest readiness number.

## Gotchas
- Structural gate is NOT semantic: a well-typed nonsense value (negated charge -$100) still passes -> add semantic/business-rule checks for business-meaningful fields.
- Auth is often not machine-readable (GitHub spec: zero securitySchemes) — auth-related trajectories are unverifiable from the spec alone.
- Self-consistency confound: do NOT report 100% TSA as generalization — require cross-model intents.
- Multi-step workflows (cascading variables) are unsupported at pilot scale — single-endpoint intents only.
- Fine-tune effect is non-uniform: always multi-seed; a single-run loss is genuine variance, do not rerun until it looks nice.

## Dry run test
- Hypothetical case (CRM, 10 endpoints): step 1 -> 10 endpoints + 38 typed params after the 2 fixes (naive parse sees only 9). Step 2 -> 15 unique intents, manual check scenario-specific (grant discount approval to role X). Step 3 -> 15 trajectories, TSA 100%/PV 100% (flagged self-consistency). Step 4 -> 15 corruptions -> catch 14 (93%) < 98% -> fix -> 15/15; valid pass 15/15. Step 5 -> LoRA Qwen2.5-0.5B, 5 seeds: held-out mean 66.2+/-18.0 vs base 12.5+/-0.0, SI 23.7+/-10.3, 1 losing seed. Step 6 -> argument-level ~21% end-to-end. Output: dataset + eval set + numeric readiness -> meaningful and followable -> [SKILL VALID].
