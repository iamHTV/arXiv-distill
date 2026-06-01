# Skill: Strategic Perspective Activation for Decision Influence
Source: 2605.31581v1
Type: framework

## When to use this skill
- When persuading stakeholders by selecting an advantageous evaluation framework
- When a proposal is rejected on every front — need to deactivate hostile perspectives
- When preparing a pitch, presentation, or argument before a board/review committee

## When NOT to use
- Arguments based on facts/objective data (no strategic framing needed)
- No influence over the evaluation process
- Ethical constraint: should not be used to manipulate by hiding relevant information

## Required inputs
- List of all arguments (pros/cons) for the proposal
- List of relevant stakeholders/perspectives
- Mapping: which argument belongs to which perspective
- Attack relation: which argument counters which
- Knowledge of which perspectives you have influence to activate/deactivate

## Steps

### Step 1 — Map Argument Landscape
1. List all arguments related to the proposal (including counter-arguments)
2. Identify perspective/source of each argument (performance, finance, risk, user impact, etc.)
3. Draw attack relation: argument A attacks argument B and why

### Step 2 — Identify Structural Traps
1. Check: is there any argument where the defender is also the attacker?
   - If argument X defends Y but also attacks Y → structural trap
2. Check: under full relevance (all perspectives active), is the target argument accepted?
3. If rejected → identify bottleneck: which perspective causes rejection?

### Step 3 — Select Perspective Activation (ρ)
1. List all non-empty subsets of perspectives Π
2. For each subset ρ, check: is the target argument accepted?
3. Prioritize ρ that:
   - Deactivates the perspective causing the structural trap
   - Keeps active the perspective where proposal is strongest
   - Has an external perspective that defends without attacking back

### Step 4 — Execute Strategy
1. Select review tracks/forums corresponding to chosen ρ
2. Include stakeholders from active perspectives first
3. Frame discussion through the selected lens
4. If challenged through deactivated perspective → redirect to active lens

## Expected output
- Target argument accepted under selected perspective activation
- Strategic advantage: proposal evaluated through the most favorable lens
- Stakeholders aligned with the evaluation framework you chose

## Example application
**Scenario**: Engineering team proposes microservice migration. Arguments: latency improvement (performance), operational complexity (reliability), deployment cost (finance), regression risk (reliability). Finance reviewer strongly opposes.

**Application**:
- Perspectives: Π = {performance, reliability, finance}
- Target: accept migration proposal
- Full relevance: rejected (finance attacks cost, reliability attacks complexity)
- Select ρ = {performance, reliability}: deactivate finance lens
- Action: Schedule review with performance + reliability leads first, present as technical decision not cost decision
- Result: proposal accepted under technical evaluation, finance deferred to later phase

## Gotchas
1. **Ethical boundary**: Deactivating a perspective = hiding relevant information. Only ethical when the proposal genuinely fits the selected lens
2. **Backfire risk**: If deactivated stakeholder feels bypassed → political backlash
3. **Dynamic arguments**: Attack relations may change when new information appears → revisit map frequently
4. **Incomplete information**: You may not know all attack relations → structural trap analysis may be wrong
5. **Priority π is fixed**: You can choose ρ but cannot change π — if priority within that lens is unfavorable, deactivation alone is insufficient
