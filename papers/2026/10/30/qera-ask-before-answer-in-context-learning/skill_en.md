# Skill: qera-ask-before-answer (ask before you answer for context learning)
Source: 2610.35083
Type: workflow / prompt-pattern

## When to use this skill
- An AI assistant must answer over a long, messy, multi-turn conversation: group chats, community threads, activity logs, revision histories — where the real requirements are scattered in earlier turns and NOT present in the final request.
- You need replies faithful to the user's words, with an audit trail: a verdict plus quotes for every requirement.
- Do NOT use: question answering over a single short document (the request is nearly the full specification); tasks needing retrieval because the context exceeds the model's context window (this skill keeps the WHOLE conversation in every call); real-time latency-critical use that cannot afford 3–4 LLM calls.

## Inputs required
- The full conversation x (all messages, pasted materials, logs) — must fit the model's context window.
- A frozen LLM M (same model for every call, high reasoning effort), ~4 calls/task budget plus token budget ~5× direct answering (112k–131k API tokens per task in practice with 19.4K-token contexts).
- A code runtime for three non-LLM filters/verifiers: faithfulness filters Φ, measure m + audit E†, guard Γ.
- NOT needed: rubrics, demonstrations, training, task-specific prompts.

## Steps
1. **Ask — one structured JSON call:** produce a requirement checklist O (each requirement o_k = the user's words u_k verbatim + scope s_k (people/items/period/units/criterion) + kind κ_k ∈ {list, count, compare, infer, write} + answer format + required strings + exclusions + layout of an older edited reply) and typed information needs N (n_j = description d_j in the user's words + type τ_j ∈ {lookup, enumerate, count, compute, compare, judge} + requirements served R_j + where to start w_j). List/count-or-compute/timeline/summary/classification requirements automatically add an enumerate need.
2. **Faithfulness filters Φ (code):** remove from O, N everything unsupported by the user's words U(x): exclusions quoting absent words, absent required strings, caution/brevity clauses no user turn requests, never-set date windows, unrequested formats, stale templates. Add coverage needs for Kset/Tset (enumerate, count, compute). Output: questions Q (7.8 needs/task in practice).
3. **Answer — one call:** draft y-tilde = M(x, π, Q) with the fixed answer protocol π: (i) read every relevant part including later corrections; (ii) specifics the materials give, not category words; (iii) EVERY qualifying item, no self-imposed threshold; (iv) yes/no/count/ranking opens with a committed verdict; (v) show the inputs of every total/share/rate; (vi) keep attributions/format/length/language/exclusions, no disclaimers. Q is advisory only — the user's words and materials override Q.
4. **Measure (code):** m = word/sentence/item counts, user limits, missing strings/headings, excluded items, leaked labels in y-tilde.
5. **Check — one structured JSON call:** answer every question in Q again against y-tilde and the whole conversation → E: verdict v_k (pass/partial/fail) + a quote a_k of the draft per requirement; findings F_j (a fact + a quote under 25 words + its location; one per item for enumerate/count, one per input for compute); status σ_j (correct/missing/incomplete/wrong/not applicable); latent gaps, unsupported facts, format violations, an edit plan of at most 12 edits. Three rules: a count is wrong only if the check names the item missed/added; an inference resting on stated evidence is not unsupported; no edit may hedge a committed verdict.
6. **Audit (code):** a finding whose quote does not occur in x is flagged and the repair may not use it; recompute typed needs: lookup → measured lengths/counts + required strings + exclusions; enumerate → one finding per item; count → count = number of items; compute → inputs' sum/average equals the result; compare → facts on each side the draft never names; judge → quotes + found values. E† = actionable items + audit findings + m gaps. If E† is empty, return y-tilde (3 calls total).
7. **Repair — one call (only if E† is non-empty):** patch ONLY what E† flags: apply fixes with the check's facts and quotes; skip fixes the materials contradict; keep definite answers definite; propagate changed numbers; preserve the rest → y-hat.
8. **Guard Γ (code):** the patch must be non-empty and not cut off; unless a length fix was requested it keeps ≥50% of the draft's length and ≥30% of its numbers; it adds no year outside the conversation; and it keeps every word limit, count, required string and exclusion the draft met. Pass → y = y-hat; fail → y = y-tilde. A final code pass restores quotations to their source text.

## Expected output
- Final reply y plus requirement checklist O and evidence E† (verdicts + quotes + recomputed numbers) — an audit trail for reviewers.
- Verified: highest solving rate on 4/4 frontier LLMs (21.0% avg vs 18.2% PSCI, 14.6% direct); rubric pass 75.6%; lead on implicit rubrics (82% of classified) +2.5 points over the best baseline, tie on explicit; Pareto-front cost (10–26% fewer tokens than PSCI, 4–5% of Ctx2Skill's); the 2-call draft already beats every baseline.
- Real numbers from the ablation: answer protocol +3.8 rubric points, questions +1.6 (89% of the gain comes before the answer); check & repair only +0.9 on numeric rubrics (47% of all) while consuming 51–56% of tokens → optional when cost matters.

## Example application
- Summarizing decisions from a group chat: the user pastes a 200-message Zalo group and asks "recap the pricing decisions". Step 1 Ask finds the requirement "quote prices in USD" (a rule from turn 3) plus an enumerate need "every pricing decision". Step 3 drafts with committed verdicts. Step 5 Check: verdict fail on the "USD" requirement (draft used VND) + 2 missing decisions, with quotes. Step 6 Audit: quotes verified in the conversation ✓. Step 7 Repair: switch VND→USD, add the 2 decisions. Step 8 Guard: patch keeps 60% of length and all limits → accepted. Output: summary + checklist + quotes.

## Gotchas
- Questions must be anchored to the user's words — a question the user never implied makes the answer hedge, narrow or reformat; the Φ code filter is mandatory, do not skip it.
- The check stage consumes 51–56% of tokens while only refining numeric requirements — when cost matters, run draft-only (Ask + Answer, 2 calls), which already beats baselines; enable Check/Repair for tasks with numbers/counts.
- Fix a count only when the check names the item missed/added; never let an edit hedge a committed verdict — without the paper's three rules the check can do harm.
- The guard rejected 27 of 1,385 repairs in practice (empty/cut-off/overspecific-dropping patches) — always keep the fallback to the draft, never return an unchecked patch.
- Numbers and counts remain the hardest (QERA passes 71.4% vs 79.2% on other rubrics): numeric-heavy tasks (logs, tracking) deserve a more careful check budget.
- The whole conversation goes into every call → the context window is a hard limit; contexts longer than the window must be chunked, and chunking loses carried-forward rules (the skill then no longer matches its design).
- Every stage sends the conversation to the LLM provider → deployments inherit the provider's data-retention terms; personal/sensitive traces need local hosting plus consent handling.
