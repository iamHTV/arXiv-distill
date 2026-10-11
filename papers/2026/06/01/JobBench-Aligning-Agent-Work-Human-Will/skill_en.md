# Skill: Delegation Readiness Assessment
Source: 2605.26329v1
Type: evaluation-method

## When to use this skill
- When evaluating AI readiness for workplace automation
- When prioritizing tasks to automate based on worker delegation desire
- When designing AI agent evaluation frameworks

## When NOT to use
- Only need economic cost-benefit analysis
- Tasks are not knowledge work
- No access to worker feedback

## Required inputs
- Worker survey data: delegation desire ratings per work duty
- Task descriptions with heterogeneous reference materials
- Evaluation rubrics: fact-anchored binary criteria
- AI models/agents to evaluate

## Steps

### Step 1 — Survey Worker Delegation Desire
1. Survey workers in target occupations
2. Rate each work duty: delegation desire (1-5 scale)
3. Identify tasks workers WANT delegated AND spend most time on
4. Prioritize tasks with: high delegation desire + high time spent
5. Output: prioritized task list

### Step 2 — Build Heterogeneous Workspaces
1. For each prioritized task, collect reference materials:
   - Multiple data sources (CSVs, documents, reports)
   - Conflicting information
   - Cluttered formats
2. Package task = workspace with all reference files
3. Include noise — irrelevant files, outdated data
4. Output: task workspace packages

### Step 3 — Design Fact-Anchored Rubric Chains
1. Define rubric chain per task:
   - Step 1: Sources located? (binary)
   - Step 2: Data reconciled? (binary)
   - Step 3: Analysis sound? (binary)
   - Step 4: Conclusion supported? (binary)
2. Average 35+ binary criteria per task
3. Award credit ONLY when EVERY step holds
4. Output: rubric chains per task

### Step 4 — Evaluate AI Agents
1. Deploy AI agents on task workspaces
2. Record: outputs, tool calls, runtime, trajectory
3. Grade using rubric chains
4. Compare across models/scaffolds
5. Output: agent performance scores

### Step 5 — Analyze Gaps & Act
1. Identify tasks where agents score highest → delegate first
2. Identify tasks where agents score lowest → keep human, improve agent
3. Compare: agent capability vs worker delegation desire
4. Prioritize automation by: high delegation desire + high agent capability
5. Output: delegation roadmap

## Expected output
- Worker delegation desire rankings per occupation
- Agent performance scores per task
- Delegation readiness matrix: tasks ranked by desire × capability
- Prioritized automation roadmap

## Example application
**Scenario**: Company wants to automate knowledge work. 50 workers across 10 occupations. Want to know which tasks to delegate to AI first.

**Application**:
1. Survey: workers rate delegation desire for 200 work duties
2. Top desire: data reconciliation (4.8/5), report generation (4.5/5), fact-checking (4.7/5)
3. Build workspaces: each task with heterogeneous reference files
4. Evaluate: AI agent scores 45% on data reconciliation, 60% on report generation
5. Delegate: report generation first (high desire + decent capability). Data reconciliation needs improvement (high desire but low capability)

## Gotchas
1. **Worker desire ≠ economic value**: Most economically valuable tasks may not be tasks workers WANT to delegate. Survey workers, not just economists
2. **Heterogeneous workspaces are key**: Real work has cluttered, conflicting data. Clean inputs don't represent real capability
3. **Rubric chains prevent gaming**: Binary criteria per step → agents can't fake quality. EVERY step must hold
4. **Current agents are weak**: Even strongest (Claude Opus 4.7) only 45.9%. Don't overestimate AI capability
5. **GDPVal saturation is misleading**: GDPVal 83% ≠ real capability. JobBench 38.9% = more realistic
6. **U.S.-centric limitation**: Survey data U.S. only. Worker preferences may differ in other countries
