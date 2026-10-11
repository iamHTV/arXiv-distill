# Skill: LLM Spatial Representation Bias — Sword, Shield, Achilles' Heel
Source: 2605.31404v1
Type: evaluation-method

## When to use this skill
- When designing spatial representations for LLM-based navigation/reasoning systems
- When evaluating linguistic inductive bias of LLMs
- When optimizing text-based spatial representations

## When NOT to use
- Multimodal systems (images + text) — text-based only
- Non-spatial reasoning tasks
- Real-world noisy environments (only synthetic tested)

## Required inputs
- Spatial reasoning task with topology, geometry, semantics
- Multiple representation formats (text, graph, structured)
- Multiple compression levels
- Model configs at different scales

## Steps

### Step 1 — Test Topological Integrity
1. Represent spatial info with accurate topology
2. Simplify/remove connections → test degradation
3. Expected: topology is sturdy shield — dominates geometry
4. Preserve topology as first-class constraint

### Step 2 — Test Linguistic Format
1. Vary format: natural text, structured, graph notation
2. Vary compression: detailed → compressed
3. Expected: double-edged sword — depends on model size, task
4. Calibrate format to model capacity

### Step 3 — Test Semantic Correctness
1. Inject semantic ambiguity: "warehouse A" = multiple locations?
2. Test: incorrect semantic cues derail planning
3. Expected: Achilles' heel — systematic planning failure
4. Ensure semantic disambiguation is mandatory

### Step 4 — Apply Engineering Guidance
1. Preserve topological integrity — don't simplify connections
2. Calibrate compression to model capacity:
   - Small models → detailed representations
   - Large models → more compression OK
3. Ensure semantic correctness — disambiguate all references
4. Select format task-aware — no single representation fits all

## Expected output
- Identification of which representation factors affect LLM planning
- Engineering guidelines for text-based spatial representations
- Model-specific recommendations

## Example application
**Scenario**: Build AI route planner for logistics company. LLM-based.

**Application**:
1. Topology: preserve accurate road connections — don't simplify
2. Compression: edge deployment (small model) → detailed. Cloud (large) → compressed
3. Semantics: ensure "warehouse A" always = same location. Disambiguate
4. Format: test multiple formats, pick best per model/task
5. Result: robust planning with fewer failures

## Gotchas
1. **Topology > geometry**: Preserve connections over distances. Topological integrity is most important
2. **Semantic correctness is MANDATORY**: Incorrect semantics derails planning systematically. Not optional
3. **Compression calibration**: Smaller models need less compression. Match to capacity
4. **No single representation**: Different tasks/models need different formats. Task-aware selection
5. **Synthetic limitation**: Results from synthetic environments. Validate on real-world
6. **Double-edged sword**: Linguistic format helps OR hurts depending on context. Test carefully
