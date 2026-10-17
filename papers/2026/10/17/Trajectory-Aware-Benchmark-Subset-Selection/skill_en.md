# Skill: trajectory-aware-subset-selection
Source: 2609.24928v2
Type: framework

## When to use this skill
- Selecting a subset for SWE-agent regression testing to reduce token cost.
- Have trajectory data from previous agent runs on benchmark instances.
- Need to estimate full-suite resolve rate from a small subset.

## When NOT to use this skill
- No trajectory data from previous runs.
- Don't need to estimate full-suite resolve rate, only need to evaluate on the subset.
- No ability to run a full regression to get historical outcomes.

## Input needed
- Trajectories from previous agent runs on benchmark instances.
- Test outcomes (pass/fail) for each instance in the most recent full run.
- An embedding model to generate numerical representations from trajectories.
- The set of benchmark instances to evaluate.

## Steps to execute
1. Parse raw trajectories into a standardized JSON schema.
2. Sanitize trajectories to remove outcome signals (passed/failed tokens, exit code 0, repository names, test-harness artifacts) so embeddings cluster by behavior not result.
3. Pass sanitized trajectories through an embedding model to generate numerical representations.
4. Group test instances by their test outcome in the most recent full test run to preserve historical pass/fail rate.
5. Select a small subset by picking instances closest to the centroid of each outcome group in embedding space.
6. In later runs, evaluate only the selected subset and use its resolve rate to estimate the full suite's resolve rate.

## Expected output
- Small subset (5% or 10% of test instances) with median estimation error below 5%.
- Token cost reduced by ~90% vs running the full suite.
- Average estimation error reduced by 3-11% and worst-case error by 4-11% vs typical draw, 38-46% vs 95th-percentile draw of strongest baseline.

## Application example
- Evaluating SWE-agent on SWE-Bench: instead of running all 2,200 instances, select a 10% subset (~220 instances) based on trajectory embedding closest to each outcome group's centroid (passed/failed), evaluate on this subset, and use its resolve rate to estimate full suite resolve rate.

## Gotchas
- Evaluated on code-repair benchmarks from GitHub issues; may not transfer to agent benchmarks in other domains.
- Each configuration run once.
- Still need to run full regression to get historical outcomes.
- Sanitizing outcome signals from trajectories is critical to prevent embeddings clustering by result rather than behavior.
