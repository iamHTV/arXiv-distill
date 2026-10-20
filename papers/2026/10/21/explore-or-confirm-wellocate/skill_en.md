# Skill: explore-or-confirm-wellocate

Source: 2610.25111v1
Type: framework / workflow

## When to use this skill
- When measuring how LLM agents split a noisy experiment budget between exploring new candidates and confirming promising ones by re-testing.
- When wanting to detect agent over-confirmation (too much re-testing) or under-confirmation (too little re-testing) in costly experiments.
- When needing to provide untried candidate lists to prevent agents from exhausting the search space.

## When NOT to use this skill
- When lacking a landscape with known true values for comparison.
- When experiments have no measurement noise (deterministic readings).
- When a single fixed rule suffices for all experimental situations.

## Required inputs
- Landscape with known true values for each candidate (or scrambled real protein data).
- Noise model simulating real experimental error (7.3% std dev of reading value).
- Fixed measurement budget (e.g., 60 measurements = 15 rounds × 4 slots).
- List of viable candidates (top 7% of landscape).
- Starting candidate (median viable).

## Steps to execute
1. Set up Wellocate: create landscape with known true values, scramble candidate names so models can't answer from memory.
2. Run agent: each round agent orders 4 candidates; environment returns noisy readings (true value + 7.3% noise); agent sees full record before each round.
3. Track re-testing share: fraction of slots spent on candidates the agent already ordered.
4. Evaluate final pick: split shortfall from landscape best into exploration loss (best measured candidate vs landscape best) and selection loss (nominated pick vs best measured candidate).
5. Compare against 3 scripted rules: guessing rule (re-tests current best fixed times per round), model-guided rule (learns from own readings), informed rule (told which candidates are viable).
6. Apply aids if needed: Menu (10 untried candidates one letter from top 3, ranked by simple model fit to readings), ledger (readings summary), landscape note (how landscape built).
7. For under-confirmers: try replacing final round with re-tests of top candidates.

## Expected output
- Re-testing share per model.
- Final pick value per model.
- Exploration loss and selection loss analysis.
- Effect of aids (ledger, landscape note, Menu) on re-testing and final pick.

## Example application
A lab uses an LLM agent to select protein variants for deep mutational scanning. The agent has 60 readings (15 rounds × 4 wells). With Wellocate, the lab measures the agent over-confirms (re-tests 94% of slots) and picks a worse final variant than the simplest scripted rule. Providing a Menu of untried variants helps the agent cut re-testing and pick a variant more than 3 units of true value better.

## Gotchas
- No real inference cost data for agents.
- No evaluation of agents with tools or external memory.
- No direct comparison with classical experimental design methods beyond the 3 scripted rules.
- Results on 3 landscapes (1 synthetic, 2 protein) may not generalize to all experiment types.
- Only 5 language models evaluated.