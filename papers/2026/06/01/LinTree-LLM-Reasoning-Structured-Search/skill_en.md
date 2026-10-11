# Skill: LinTree — Structure Search History for LLM Reasoning
Source: 2605.31492v1
Type: prompt-pattern

## When to use this skill
- When designing reasoning prompts for LLMs on tree-structured problems
- When LLM backtracks or explores alternatives in reasoning
- When needing to improve search efficiency of LLM reasoning

## When NOT to use
- Task has no tree structure (linear tasks)
- Model too weak to utilize structured traces
- Trace length overhead too large for context window

## Required inputs
- Reasoning task with tree-structured search space
- LLM capable enough to process structured traces
- Format specification for parent pointers

## Steps

### Step 1 — Define Reasoning Step Format
1. Each reasoning step needs:
   - Step ID (unique)
   - Parent ID (which step it branched from)
   - Action/decision content
   - Status (active/abandoned/success)
2. Format: "Step 3 (parent: Step 1): Trying alternative approach X → [status]"

### Step 2 — Generate Structured Traces
1. When LLM reasons, append parent pointer to each step
2. When backtracking: explicitly state "Abandoning Step 3, returning to Step 1"
3. When exploring alternative: "From Step 1, trying Step 4 (different from Step 3)"
4. Maintain tree structure visible in trace

### Step 3 — Extract Plan from Structured Trace
1. Follow success path from root to solution
2. Parent pointers enable easy path extraction
3. Identify which branches succeeded vs failed
4. Output: final solution with reasoning path

### Step 4 — Optimize Search Efficiency
1. Parent pointers help model avoid revisiting failed branches
2. Model can learn from failures on other branches
3. Structured history enables better state tracking
4. Result: fewer search expansions, higher solve rate

## Expected output
- Improved solve rate on tree-structured reasoning tasks
- Fewer search expansions (more efficient)
- Clear reasoning path from root to solution
- Better plan extraction from traces

## Example application
**Scenario**: AI assistant helps debug complex code. Multiple possible causes, needs systematic exploration.

**Application**:
1. Step 1 (parent: root): Checking memory allocation → looks fine
2. Step 2 (parent: Step 1): Checking null pointer → found issue at line 45
3. Step 3 (parent: root): Checking concurrency → no race condition
4. Step 4 (parent: Step 2): Fixing null pointer at line 45 → SUCCESS
5. Structured trace: root → Step 2 → Step 4 (success path extracted)

## Gotchas
1. **Minimal change, big impact**: Just adding parent pointer field → improves performance. No complex restructuring needed
2. **Flat traces lose structure**: Sequential "Step 1, Step 2, Step 3" is NOT enough. Must show branching
3. **Parent pointers enable plan extraction**: Easy to trace back from solution to root
4. **Context window overhead**: Parent pointers add tokens. Balance structure vs length
5. **Not for linear tasks**: If task has no branching → parent pointers are overhead without benefit
6. **Model must be capable**: Weak models don't utilize structured traces → ensure model size is sufficient
