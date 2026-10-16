# Skill: sustainable-agent-design-pareto
Source: 2610.03010v1
Type: framework

## When to use this skill
- Building AI dev pipeline (code generation, technical debt detection, vulnerability detection, log analysis).
- Want to balance accuracy, energy, and latency (cost).
- Deciding whether to use multi-agent or not.

## When NOT to use
- Simple single-step task, no agent needed.
- Don't care about energy/latency cost, only absolute accuracy.

## Required input
- List of dev tasks to perform.
- Available LLM models (from small to large).
- Prompt strategies (zero-shot, few-shot) that can be applied.

## Steps
1. Identify dev task and select appropriate LLM model (not necessarily the largest).
2. Try no-agent (NA) or single-agent (SA) configuration first, don't jump to multi-agent.
3. Apply few-shot prompting with concrete examples for output-format-sensitive tasks (e.g. log parsing).
4. Measure energy, latency, and accuracy on each configuration, build Pareto front.
5. Only add multi-agent (MA) if there is clear evidence that accuracy benefit outweighs 6.36× energy and 6.07× time cost.

## Expected output
- Lightweight configurations typically occupy 55–90% of Pareto-optimal points.
- Save energy and time compared to default multi-agent.

## Example application
Solopreneur building automated bug-fixing pipeline: start with single-agent + few-shot prompt (3 bug-fix examples), measure energy and latency. Only consider multi-agent if single-agent doesn't reach sufficient accuracy and extra cost is acceptable.

## Gotchas
- Multi-agent consumes 6.36× energy and 6.07× time vs non-agentic, worst-case 160× slowdown.
- MA appears in only 1/66 Pareto-optimal configurations — should not be the default choice.
- Few-shot sometimes constrains or distracts (e.g. code generation better at zero-shot 97.3% vs 92.7%).
