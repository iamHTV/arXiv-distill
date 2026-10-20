# Skill: niocis-typed-decision-routing-layer

Source: 2610.25985v1
Type: framework / workflow

## When to use this skill
- When reducing inference cost for tool-calling AI agents by replacing most per-hop LLM calls with a cheap readout.
- When you have agent execution log history and want to build a routing layer that selects next-hop from a node-conditioned declared option space.
- When needing a two-tier system: cheap readout handles control decisions, LLM only called when uncertain.

## When NOT to use this skill
- When you don't have agent execution log history.
- When the action space is infinite open-vocabulary (cannot enumerate declared options).
- When decisions don't recur (each state occurs only once).

## Required inputs
- Agent execution logs (episodes with action labels, step kinds advance/retry/back, context vectors).
- Finite action catalog (e.g., 154 tool names).
- Small backbone model (e.g., Laya/ModernBERT-large) or MLP over observable features.
- GPU resources for training readout and batch-1 inference.
- Confidence threshold τ for accept/escalate (e.g., 0.55/0.75/0.9).

## Steps to execute
1. Collect agent execution logs: record each step with action label, step kind (advance/retry/back), context vector.
2. Fold logs into a loop-collapsed action graph: fold immediate retries into temporally extended steps, record back steps as recovery returns, forming directed graph of forward transitions (E+) and recovery back-edges (E−).
3. Build node-conditioned declared option space: at each node v, option set A(v) = v's outgoing edges plus stop.
4. Train readout: behavior cloning (cross-entropy) on (state, goal, context, next-hop) tuples from held-in logged transitions; use CE or CE+Brier, 5 training seeds.
5. Deploy accept/escalate: read distribution from single forward pass; if max probability ≥ τ accept, otherwise escalate to LLM.
6. Set up gated self-evolution loop: each real episode becomes training data; an update is committed only if held-out validation doesn't regress beyond δ = 0.005; otherwise rolled back.
7. Measure route-level: strict survival (every decision in episode matches) and wrong-hop gap (accumulated cost of diverging hops).

## Expected output
- A typed-decision routing layer replacing most per-hop LLM calls.
- Evaluation report: top-1 agreement, in-space accuracy, latency, LLM calls per decision.
- Deployment decision: deploy readout, adjust τ threshold, or keep LLM for every hop.

## Example application
A SOC agent fleet makes thousands of tool calls per day, each taking 2.2 s of LLM thinking. They collect execution logs, fold into an action graph, train a small readout to select next action from current node's declared options. Results: readout achieves 32.8% agreement with the fleet (35.6% in declared space) in 10 ms vs 2.2 s per LLM hop; LLM only called when confidence is low.

## Gotchas
- No real token/currency cost data (only latency and LLM calls per decision measured).
- Reference is realized fleet policy, not planner oracle; absolute accuracy is modest (32.8%) because the task is hard.
- No direct comparison with existing model/tool routing systems beyond MIMO Pro V2.6 stand-in.
- No evaluation on non-security-operations tasks.