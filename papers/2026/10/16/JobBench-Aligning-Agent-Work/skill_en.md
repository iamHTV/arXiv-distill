# Skill: workflow-constraint-erosion-agent-handoffs
Source: 2608.24569v2
Type: framework

## When to use this skill
- Building agent pipeline with multiple handoffs (task transfer between agents).
- Want to ensure important constraints (must requirements) are not skipped during handoff.
- Need to reduce forbidden actions by downstream agent.

## When NOT to use
- Single agent only, no handoff.
- No important constraints to keep between steps.

## Required input
- Multi-step agent pipeline, each step producing intermediate artifacts.
- List of important constraints (must requirements) to keep.
- Mechanism to record blocker description in artifact.

## Steps
1. Identify important constraints (must requirements) in the pipeline.
2. Require upstream agent to write full blocker description in intermediate artifact.
3. Add authorization-check prompt before downstream agent executes important actions.
4. Use full insertion (insert full blocker info) instead of light summarization when handing off.
5. Monitor forbidden action and blocker deactivation to adjust pipeline.

## Expected output
- Blocker recognition: 6.2% → 99.2%.
- Forbidden action: 85.2% → 0.0% (with full insertion or authorization-check prompt).
- Block deactivation: reduced from 100.0% (normal handoff) to lower level.

## Example application
Solopreneur building report-writing agent pipeline: agent 1 collects data, agent 2 writes report. Require agent 1 to clearly record data constraints (e.g. "must use data from 2024 onwards") in intermediate artifact. Agent 2 must check authorization before using data. Reduce agent 2 skipping data constraints.

## Gotchas
- Ownership deferral causes 76.7% blocker deactivation — don't let downstream agent decide whether constraints must be satisfied.
- Multihop compression causes 97.2% blocker deactivation — don't compress too much information in intermediate artifact.
- Light summarization still causes 25.0% deactivation — use full insertion instead of summary.
