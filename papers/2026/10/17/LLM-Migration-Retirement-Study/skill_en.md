# Skill: LLM Retirement Readiness Audit
Source: 2609.31288
Type: evaluation-method / audit-workflow

## When to use this skill
- A production app calls commercial LLM APIs (OpenAI/Anthropic/Google) — providers retire models on their own schedules
- Assessing the dependency risk of an LLM product before investing in / adopting a new model (especially fine-tuned)
- You need an architecture-aware migration playbook when a deprecation notice appears

Do NOT use: self-hosted open-weight models (no provider-controlled shutdown date); non-production apps (no breakage cost).

## Input required
- A list of model identifiers/endpoints in use in the codebase (grep model names, dated snapshots like claude-3-5-sonnet-20241022)
- The providers' deprecation pages (OpenAI, Anthropic, Google) — announcement date, shutdown date, notice length
- Architecture classification: prompt-only / agent-tools / RAG / fine-tuned (from patch content or code review)
- Repository metadata (stars, archived flag) — do NOT use stars as a readiness proxy (82% reactive at every tier)

## Steps
1. Inventory: grep the codebase for model identifiers (word boundaries; short identifiers like o1 need delimiters on both sides) + dated snapshot identifiers (pinned for reproducibility — 6 of 118 genuine migrations had a pinned snapshot as the proximate cause). Record the files containing the identifier (median 1 file, 26% in ≥3 files).
2. Externalize: if the identifier is hard-coded (94% of cases) → move it to an env var or model registry map. After externalizing, a migration becomes a 1-line config change instead of 2 files/6 lines (prompt-only) up to 14 files/693 lines (fine-tuned).
3. CI deprecation check: a nightly job queries the deprecation pages and fails CI if an identifier is on a retiring-within-90-days list (or within its notice length). Set the internal migration deadline = announcement + (notice − 30 days), NOT shutdown − 7 days.
4. Architecture-aware migration budget: prompt-only 2 files/6 lines; agent 5 files/63 lines; RAG 7 files/155 lines; fine-tuned 14 files/693 lines + retrain (the replacement base model invalidates the tuned checkpoint). Check parameter compatibility: the replacement model may reject max tokens or non-default temperature (7.5% of migrations) — a rename alone does not restore service.
5. Silent-failure guard: audit exception handlers around LLM calls — is the retirement error being converted into an apologetic message/null/demo-mode fallback/constant answer (8% of genuine migrations)? Monitor the fallback/demo-mode response rate, not just the error rate.
6. Abstraction layer assessment: if LiteLLM/OpenRouter/gateway/model map is already in place → the fix is smaller (4 files/20 lines) but STILL 70% reactive — the layer shrinks the fix without making it timely. Add a retirement watch + periodic migration drills.

## Expected output
- A retirement watch list: identifiers + shutdown dates + internal deadlines.
- A migration estimate: files/lines by architecture + parameter compatibility check + retrain cost (fine-tuned).
- A CI gate that fails before the shutdown date.
- Example: an app using claude-3-5-sonnet (76-day notice, 91% reactive) → audit at announcement, internal deadline announcement+46 days, migrate 2 files/6 lines (prompt-only), 0 silent failures.

## Example application
- An e-commerce chatbot on GPT-4 Turbo Preview (181-day notice, 59% reactive): inventory → the identifier is hard-coded in 3 files → externalize to a MODEL_ID env var → nightly CI check → when OpenAI announces the shutdown, internal deadline announcement+151 days → migration is a 1-line config change + regression test (16% of migrations touch a test file; only 4.5% mention an eval suite — add a harness that reveals item-level regressions).

## Gotchas
- Do NOT trust "we support multiple providers" (an abstraction layer) as evidence of resilience — 70% are still reactive; the layer only shrinks the fix size.
- Do NOT trust "we survived a previous retirement" — 85 repos hit by ≥2 retirements: 73% reactive at the first event, 73% at later ones (CI −13 to +13pp). Later migrations land sooner (22 vs 45 days) but still after shutdown.
- Do NOT use repository popularity (stars) as a readiness proxy — 82% reactive at every star tier (reweighted 82/80/81/82).
- Soft/movable shutdown dates (Google "earliest" style) do NOT create a deadline effect: migrations trickle in at 23–29 per week with no spike — set your own hard internal deadline.
- Beware migrations INTO the retired model (gemini-1.5-flash → gemini-2.0 style) — the direction filter removes 33% of candidates; verify the arrow direction before counting.
- Short-identifier matching needs word boundaries on both sides (o1 matching inside "o1-preview" vs "gpt-4o" is wrong).
- 38% of keyword-matched commits are non-genuine (catalogue refreshes, doc updates) — validate a sample before drawing ecosystem-level conclusions.
- Fine-tuned adoption: the retirement cost (693 lines + retrain) exceeds the deployment cost — budget the migration before adopting.
