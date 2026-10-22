# Skill: Task-specific harness update isolation for self-evolving agents
Source: 2610.25858
Type: framework

## When to use this skill
- Agent needs to adapt continually to new tasks without forgetting old ones (continual learning).
- Agent harness is shared across multiple task groups.
- Do NOT use when tasks come from the same domain but require conflicting workflows — you need a clearer separation mechanism.

## Input needed
- Initial agent harness (system prompt, memory, skill libraries, control code).
- A continuous streaming task stream.
- Evaluation mechanism for performance on each task group (hold-out sets).

## Steps
1. Design the harness so updates for task A do not affect task B (e.g., separate namespaces or modules per task group instead of a single global prompt).
2. If using experience memory retrieval, add a context filter before feeding retrieved memories into the prompt: check whether the stored memory's workflow is compatible with the incoming task.
3. Avoid applying global edits to the system prompt or shared workspace for all subsequent tasks.
4. Monitor stability (S) across checkpoints on previous task groups, not just on the currently training group.

## Expected output
- Reduced cross-task interference and post-block forgetting compared to global prompt modification methods (GEPA/Meta-Harness).
- Higher average stability (S = −1.9 vs −4.3 for GEPA) at the cost of lower plasticity (P = +3.3 vs +6.2 for GEPA).

## Example application
- A coding assistant handling tasks from multiple programming languages: each language has its own skill module, updates for Python do not affect JavaScript, skill retrieval only fires when context matches the workflow.

## Gotchas
- Base model fixed (Gemini 3.6 Flash), not a broad sweep across model families.
- Task blocks are contiguous; interleaved tasks still cause degradation (GEPA terminal advantage drops from +5.8 to +0.9 when interleaved).
- Similarity-based retrieval cannot separate tasks that use the same embedding space but require different workflows.