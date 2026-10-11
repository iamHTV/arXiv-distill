# Skill: GRASP — Gated Regression-Aware Self-Improvement
Source: 2605.29668
Type: workflow

## When to use this skill
- When needing to self-improve LLM agents in structured environments
- When accumulating guidance blindly causes regressions
- When procedural reliability matters

## When NOT to use
- Open-ended action spaces
- No verifiable tasks
- No held-out probe available

## Required inputs
- Structured environment with verifiable tasks
- Failed trajectories from agent runs
- Held-out probe episodes
- Skill-writing LLM

## Steps

### Step 1 — Classify Failures
1. After each batch, collect failed traces
2. Classify by mechanism-specific failure mode
3. Labels: "date_filter_omitted" not "wrong_answer"
4. Output: failure groups

### Step 2 — Generate Proposals
1. Skill-writing model proposes ADD/MODIFY/REMOVE edits
2. Process from largest failure group to smallest
3. Include: failing traces, passing traces, active skills, other failure labels
4. Output: candidate skill edits

### Step 3 — Validate with Regression Gate
1. Evaluate each candidate on held-out probe
2. Admit only if net improvement under hard regression budget
3. Check: no regression on previously passing examples
4. Output: validated skill edits

### Step 4 — Update Library
1. Apply accepted edits to skill library
2. Bounded library: ADD blocked at capacity unless paired REMOVE
3. Skills: trigger condition, behavioral rule, verification, contrastive example
4. Output: improved skill library

## Expected output
- +48 points on structured tasks (MedAgentBench)
- No regression on previously correct tasks
- Transferable skills across models

## Example application
**Scenario**: AI agent for clinical FHIR tasks. Current: 40.6% accuracy.

**Application**:
1. Classify: "date_filter_omitted", "wrong_endpoint", "missing_required_field"
2. Propose: skill for date filtering, skill for endpoint selection
3. Validate: test on held-out probe — date filter skill improves +30%, no regression
4. Admit date filter skill, reject others
5. Result: 40.6% → 88.8%

## Gotchas
1. **Validate before accepting**: Don't accumulate blindly. Test each skill
2. **Mechanism-specific labels**: Classify by failure mechanism, not outcome
3. **Hard regression budget**: No regression on previously correct tasks
4. **Frozen transfer**: Stronger model's skills help weaker models
5. **Bounded library**: Manage size with ADD/REMOVE pairing
