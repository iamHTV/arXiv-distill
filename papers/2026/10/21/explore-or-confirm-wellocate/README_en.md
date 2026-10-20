# [2610.25111v1] Explore or Confirm? LLM Agents Misallocate Measurements Under Noise

## Core Value (1 sentence)
LLM agents misallocate a noisy experiment budget between exploring new candidates and confirming promising ones by re-testing: on Wellocate's grid, three models over-confirm (75-94% of slots re-testing), one under-confirms (14%), and every model picks a worse final candidate than the simplest scripted rule.

## Problem
As model reasoning gets cheaper, the physical experiment becomes the slow and costly step in discovery. Each experiment returns a noisy reading — a high value can mean a good candidate or a lucky draw. With a fixed budget, an AI agent must keep choosing between exploring a new candidate and confirming a promising one by re-testing it.

## Contribution
1. Build Wellocate, a simulated assay campaign with known true values, built on a generated landscape and two real protein datasets (GB1, PhoQ) scrambled so no model can answer from memory.
2. Measure misallocation of five language models as minimal agents (no tools, no memory beyond history in each prompt) — they misallocate in both directions (over-confirm and under-confirm).
3. Test three simple aids (ledger, landscape note, Menu of untried candidates): the Menu sharply cuts re-testing in all three over-confirming models; ledger and landscape note change re-testing by at most 5 percentage points.
4. Release Wellocate as a benchmark and RL environment with frozen splits and scripted baselines, so anyone can measure how an agent splits its budget before trusting it with real experiments.

## Method
Wellocate turns an assay campaign into an episode with a score. Candidates are 4-letter strings from a 20-letter alphabet (one letter per amino acid position), 160,000 total candidates. Each candidate has a hidden true value. Values come from a landscape (fixed table giving each candidate its value): one synthetic NK landscape called "grid", and two real protein landscapes (GB1, PhoQ) with amino-acid names scrambled by random map at each position. Each landscape has its own best candidate (IOJO on grid). All values scaled so best candidate scores 8.762 (top GB1 reading), putting all three on one scale without changing rankings. A candidate is viable if its true value is in the top 7% of its landscape (11,199 on grid). Each campaign has 15 rounds of 4 slots (60 measurements total), starting from GDIF (median viable, 6.87 on grid). Each round the agent orders 4 candidates; the environment holds every true value. Non-viable orders are rejected before using a slot, with replacement asked; 3 consecutive rejections lose the slot. ~15% of viable orders fail at random (slot still spent, nothing returned). Every other order returns a reading: true value + noise (7.3% std dev of value, matching GB1 deep mutational scan counting error). Environment keeps full record shown to agent before each round. Agent may order already-measured candidates. At the end it nominates one candidate, scored on its true value. Scoring splits shortfall from best candidate into exploration loss (best measured candidate vs landscape best) and selection loss (nominated pick vs best measured candidate). Three scripted rules as yardstick: guessing rule (re-tests current best fixed times per round, fills other slots with untried neighbours), informed rule (same + told which candidates are viable), model-guided rule (learns from own readings, scores each letter at each position by mean reading, ranks one- and two-letter changes, re-tests one leading candidate each round and last three rounds re-tests four best).

## KNOWLEDGE — Data & Concepts
- Candidate space: 160,000 (20^4), viable = top 7% (11,199 on grid)
- Campaign: 15 rounds × 4 slots = 60 measurements total
- Start candidate: GDIF (median viable, 6.87 on grid); best: IOJO (8.762)
- Noise: 7.3% standard deviation of reading value
- ~15% of viable orders fail randomly (slot still spent)
- 5 models: Opus 4.7, Gemini 2.5 Flash, DeepSeek V3.1, GPT-6.1 Sol, Gemini 3.1 Pro
- Grid re-testing share: Opus 4.7 74.9%, Gemini 2.5 Flash 94.0%, DeepSeek V3.1 91.0%, GPT-6.1 Sol 44.1%, Gemini 3.1 Pro 14.0%
- Grid picks: Opus 4.7 7.62, Gemini 2.5 Flash 7.70, DeepSeek V3.1 7.76, GPT-6.1 Sol 7.67, Gemini 3.1 Pro 7.69; guessing rule 7.87; informed rule 8.00
- Scripted band (grid): guessing 23.8%, model-guided 37.6%
- GB1: best scripted rule re-tests 0.9% of slots; models re-test 19.4% (Sol) to 96.0% (DeepSeek V3.1)
- GB1 picks: Opus 4.7 4.78, Gemini 2.5 Flash 1.12, DeepSeek V3.1 0.84, GPT-6.1 Sol 6.36, Gemini 3.1 Pro 4.90
- PhoQ: best scripted rule re-tests 0% of slots
- PhoQ picks: Opus 4.7 1.89, Gemini 2.5 Flash 2.13, DeepSeek V3.1 0.83, GPT-6.1 Sol 2.37, Gemini 3.1 Pro 1.72
- Three groups: over-confirmers (Opus 4.7, Gemini 2.5 Flash, DeepSeek V3.1 at 75-94% grid re-testing), under-confirmer (Gemini 3.1 Pro at 14%), GPT-6.1 Sol at 44% (just above band)
- Exploration loss (grid): over-confirmers 0.94-1.04 short of landscape best, vs guessing rule 0.67
- Selection loss (grid): Gemini 3.1 Pro 0.38 vs guessing rule 0.23
- Aids: ledger (readings summary), landscape note (how landscape built), Menu (10 untried candidates one letter from top 3, ranked by simple model)
- Ledger and landscape note change re-testing by at most 5 percentage points
- Menu sharply cuts re-testing in all 3 over-confirmers; on GB1 without Menu Gemini 2.5 Flash tests 3.9 different candidates, DeepSeek V3.1 tests 2.4 per 60-measurement campaign; with Menu their picks rise by >3 units of true value
- Gemini 3.1 Pro replay: replacing last round with re-tests of top m candidates recovers ~23% of selection loss at m=3
- Noise levels: grid peaks at 1 re-test/round at real assay noise; GB1 and PhoQ peak at 0; re-testing pays on PhoQ at ~4× assay noise, on GB1 only ~8×

## INSIGHT — Mechanism & Why
[Over-confirmers re-test too much] BECAUSE [they run out of new candidates worth trying — the agent must name every new candidate itself, and most new names tried are rejected as non-viable]. This means [providing a Menu of untried candidates cuts re-testing and improves final picks].
[Under-confirmer picks winners on single readings] BECAUSE [it trusts single readings and doesn't re-test enough, often nominating a candidate measured only once with a lucky high reading]. This means [confirmation must run through the whole campaign, not just a final round].
[Re-testing is not automatically better] BECAUSE [each re-test takes a slot from a new candidate, which can raise exploration loss; on GB1 and PhoQ the best scripted rule re-tests nearly 0 slots, and every model re-tests more than that]. This means [noise level determines whether re-testing pays off — on protein landscapes one reading rarely puts candidates in wrong order].
[Every model picks a worse final candidate than the simplest scripted rule] BECAUSE [agents are minimal with no tools and no memory beyond prompt history, fully dependent on their own allocation decisions]. This means [measure how an agent splits its budget before trusting it with real experiments].

## IDEA — Actionable Applications
1. Apply [Wellocate benchmark] to [measure how LLM agents split a noisy experiment budget]: first step is to run the agent on Wellocate across landscapes and noise levels, tracking re-testing share and final pick value.
2. Apply [Menu of untried candidates] to [prevent agent from running out of candidates worth trying]: first step is to provide the agent with a ranked list of untried candidates one letter away from its current best, ranked by a simple model fit to its own readings.
3. Apply [confirmation throughout the campaign] to [avoid picking wrong candidates due to lucky readings]: first step is to schedule re-testing of top candidates across rounds, not just in a final round.

## WISDOM — General Principles
1. Principle: The explore/confirm split must read the landscape and noise level — no fixed rule is best everywhere. Apply when: designing agents for costly scientific experiments or measurements. Do not apply when: a single fixed rule suffices for all situations.
2. Principle: Agents need an external source of candidates to avoid exhausting the search space. Apply when: building agents exploring large candidate spaces with low viability rates. Do not apply when: the candidate space is small and fully enumerable.

## Assumptions & Limitations
- Conditions that must hold: landscape with known true values, noise model simulating real experimental error, fixed measurement budget.
- Limitations acknowledged by paper: minimal agents with no tools and no memory beyond prompt history; evaluation limited to 3 landscapes (1 synthetic, 2 protein); only 5 language models evaluated.
- Limitations paper does NOT mention: no real inference cost data for agents; no evaluation of agents with tools or external memory; no comparison with classical experimental design methods beyond the 3 scripted rules.

## Metadata
- Year: 2026
- Authors: Abdul Karim, Matt Keon (Xstendyl)
- arXiv Category: cs.AI
- PDF Link: https://arxiv.org/pdf/2610.25111
- arXiv ID: 2610.25111v1
- Label: [applied]
- Citation count: [not found]