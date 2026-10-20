# Skill: DAQ — Evaluating End-to-End Business-Task Delivery Agents
Source: 2610.24087 (OR-License)
Type: evaluation-method

## When to use this skill
- Evaluating an LLM agent on end-to-end business tasks: delivery scheduling, pricing, production planning — where hard constraints and a measurable objective exist.
- Comparing models/agents on the same real-world task before deployment.
- Do NOT use for tasks where no verifier can be built (creative writing, open strategy) — use subjective evaluation instead.

## Inputs required
- A task with: (a) hard constraints checkable by code, (b) an objective function, (c) an expert reference solution.
- If the task lacks client information: write a fact catalog plus disclosure rules (max 3 facts per query, like ORSim).

## Steps
1. Run the agent N=5 times per task; record the final deliverable of each run.
2. Run the verifier: a deliverable violating any constraint scores feasibility = 0 for that run.
3. Compute conditional quality = objective(deliverable) / objective(reference), for feasible runs only.
4. Feasibility = % of feasible runs. DAQ = mean(Feasibility × conditional quality) across tasks, tasks weighted equally.
5. (Optional) Analyze the HCAEU chain in logs: mark H (hypothesis) / C (mechanistic explanation) / A (executed experiment) / E (evidence interpretation) / U (evidence-grounded update); report complete-chain rate.

## Expected output
- A DAQ table per model plus a gap breakdown: how many points lost to infeasibility vs. quality.

## Example
- Delivery-scheduling agent for a shop: 5 runs, 4 feasible (feasibility 80%), mean conditional quality 95% → DAQ = 0.80 × 0.95 = 76%. Another model: feasibility 95%, quality 88% → DAQ 83.6% → pick model 2 despite lower conditional quality.

## Gotchas
- Never use conditional quality as the headline metric: a "high quality" model may simply abandon tasks that are hard to make feasible.
- The verifier must check hidden business rules, not just output format.
- DAQ is fair only when tasks are equally weighted; larger tasks need custom weights.
