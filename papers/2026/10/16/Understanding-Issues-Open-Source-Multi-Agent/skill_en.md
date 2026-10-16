# Skill: open-source-mas-issues-causes-solutions
Source: 2610.00905v1
Type: framework

## When to use this skill
- Building or maintaining LLM-based multi-agent systems (MAS).
- Want to understand common issues, causes, and solutions in open-source MAS.
- Need to prioritize what to invest in when building MAS.

## When NOT to use
- Not building MAS, only using single agents.
- No list of issues/bugs to analyze.

## Required input
- List of issues/bugs from the MAS system in operation.
- Understanding of MAS architecture (coordinator, specialist, workflow, etc.).

## Steps
1. Classify each issue into 17 categories (Orchestration & Execution, Memory & State Management, Tool Issue, etc.).
2. Extract causes from each issue (Workflow Problem, Tool Integration Problem, Memory Problem, etc.).
3. Apply corresponding solutions (Optimize Workflow, Adjust Configuration, Optimize Tool Integration, etc.).
4. Prioritize Optimize Workflow (OW) since it's the most common solution (26.0%) and solves most orchestration problems.
5. Monitor resolution rate: Documentation Issue highest (76.9%), Output Issue lowest (24.1%).

## Expected output
- Understand common MAS problems (Orchestration & Execution 22.0% is most frequent).
- Know to prioritize workflow design and agent coordination investment.

## Example application
Solopreneur building a customer support MAS: encountered agents handing off incorrectly (orchestration issue). Apply Optimize Workflow: redesign the handoff flow between agents, add gate validation before handoff. Reduce debugging time compared to fixing each agent individually.

## Gotchas
- Orchestration & Execution Issue accounts for 22.0% — this is the biggest problem, not individual agent issues.
- Workflow Problem is the most common cause (29.4%) — check workflow first before fixing individual agent code.
- Documentation Issue has highest resolution rate (76.9%) — investing in documentation helps solve problems faster.
