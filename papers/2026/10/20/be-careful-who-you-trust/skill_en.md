# Skill: be-careful-who-you-trust
Source: 2609.31704v1
Type: framework

## When to use this skill
- Evaluating multi-agent LLM coordination robustness when public information can be corrupted/transformed.
- Need to separate the root cause of coordination failures: agent behavior change vs. public action transformation by the system.
- A multi-agent system with shared public transcript.

## When NOT to use this skill
- Evaluation based only on the public transcript without logging original actions.
- Concluding a "behavioral tipping point" solely from public-transcript collapse.

## Required inputs
- A multi-agent coordination game (e.g., Stag Hunt) with shared public information.
- A mechanism to log each agent's original (pre-flip) action before transformation.
- A mechanism to log each agent's public (post-flip) action shown in the transcript.
- Coordination threshold M and total agent count N.
- Payoff matrix to compute the cutoff q*.

## Steps
1. Set up an N-agent coordination game: each agent chooses an original action rt_i ∈ {Stag, Hare}, speaks in fixed order, conditions on the public transcript.
2. Log each agent's original action before any transformation.
3. If agents are designated corrupted, transform the public action (e.g., flip Stag↔Hare) and generate a new plausible justification; subsequent agents see only the transformed report.
4. Compute pre-flip success: apply threshold M to original actions of all agents.
5. Compute public success: apply threshold M to post-flip actions used for execution.
6. Compute realised payoff from post-flip actions and truthful-implementation payoff from original actions; the gap indicates the mechanical component.
7. Use the simple public-report benchmark (naive aggregate): compute the observed public Stag-report share and compare against the cutoff q* where Stag becomes optimal.
8. Evaluate descriptive match: fraction of turns where the agent's original action agrees with the benchmark-implied action.

## Expected output
- Clear analysis of whether coordination collapse is due to agent behavior change or public action transformation; a simple benchmark to describe agent coordination decisions.

## Example application
- A company's multi-agent customer support system: log each agent's original decision and the public decision sent to the customer; when success rate drops, use steps 4-6 to see whether the drop is due to agent error or system transformation of public messages.

## Gotchas
- Do not conclude behavior change solely from public-transcript collapse — much of it may be mechanical.
- Pre-flip success is not a no-corruption counterfactual, since later original actions may already reflect exposure to earlier corrupted reports.
- Benchmarks are descriptive uncorrected rules, not optimal corruption-aware policies.
- Paper uses homogeneous groups and fixed speaking order; results may differ with heterogeneous groups and free speaking order.

## Self-check
- Can someone who has not read the original paper follow these 8 steps? [YES] — each step is a concrete action.
- Which step is most vague? Step 7 (computing q* from the payoff matrix) requires understanding the Stag Hunt formula.
- Is the Input section sufficient? [YES] — multi-agent system, original/public action logging, threshold M, agent count N, payoff matrix are all covered.

## Dry run (hypothetical scenario)
- Scenario: A company has 5 coordinating agents to select a vendor, threshold M=3 agents agree; public information can be transformed.
- Run the skill: (1) Set up the 5-agent game, each agent agrees/disagrees; (2) log each agent's original decision; (3) transform public decisions of 2 corrupted agents; (4) compute pre-flip success from 5 original decisions; (5) compute public success from 3 unchanged + 2 transformed decisions; (6) compute realised payoff and the mechanical gap; (7) use naive aggregate benchmark vs cutoff q*; (8) if the gap is mainly mechanical, fix the communication system rather than changing agent prompts.

## Verdict: [SKILL VALID]
