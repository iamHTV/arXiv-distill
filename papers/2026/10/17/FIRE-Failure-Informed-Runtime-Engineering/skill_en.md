# Skill: fire-runtime-policies-for-agent-reliability
Source: 2609.26048v1
Type: framework

## When to use this skill
- Agent has a working solution but fails to deliver it repeatedly due to procedural loss.
- Need a lightweight harness layer to protect existing model capabilities, without retraining or changing the user prompt.
- An observable state exists before the verifier evaluates (observable pre-verifier intervention point).

## When NOT to use this skill
- Failure due to missing model capability or domain knowledge (not procedural loss).
- No observable intermediate state before the verifier runs.
- Want to apply before knowing specific failure modes (policies are derived from observed failures).

## Input needed
- Agent harness able to intervene at events: prompt submission, before each tool call, when agent attempts to stop.
- Tasks with a verifier returning clear pass/fail.
- Action history and policy state accessible.
- Task descriptions for writing eligibility predicates.

## Steps to execute
1. Run the agent twice per task without any policy (policy-free), record each attempt.
2. Inspect tasks that fail one of two attempts (1/2) and both attempts (0/2) to find clear procedural omissions.
3. Exclude provider faults, verifier faults, missing capability, and failures without an observable intervention point.
4. Cluster failures by mechanism rather than task; register chain: state → intervention → behavior → verifier condition.
5. Write task-agnostic predicates; screen candidates on positive and nearby-negative tasks.
6. Revise or retire inert, over-broad, or harmful candidates.
7. Add a policy to the frozen portfolio only when: observable failure state, focused positive result, and acceptable routing audit.
8. Freeze source code, routing, and analysis rules.

## Expected output
- A frozen policy portfolio with clear rules, each rule containing eligibility predicate, runtime predicate, and intervention action.
- Reduced procedural-loss failures, increased pass∧2 (repeated success across two attempts) without large change to pass@2.

## Application example
- gRPC server task: agent launches server inside its own session then stops; server dies with the session. Policy fires at stop event: instruct agent to relaunch server detached from session with redirected streams, then issue a separate later command to probe the required port.

## Gotchas
- Policies only address procedural loss, not missing algorithms or domain knowledge.
- Policy content matters more than timing — generic "check your work" instructions do not help.
- Policy portfolios are model-specific; not directly transferable across model tiers.
- Building policies requires observing failures first — cannot apply before knowing failure modes.
