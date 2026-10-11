# Skill: DeepAgent — Reasoning Agent with Tool Use RL
Source: 2510.21618
Type: workflow

## When to use this skill
- When building end-to-end reasoning agents with tool use
- When needing autonomous thinking, tool discovery, action execution
- When training agents for long-horizon interactions

## When NOT to use
- Simple tasks that don't need tool use
- Predefined workflows sufficient
- No LLM-simulated APIs available

## Required inputs
- LLM base model
- Tool/API definitions
- LLM-simulated APIs for training
- Auxiliary LLM for memory folding

## Steps

### Step 1 — Setup Autonomous Thinking
1. Agent reasons through problem autonomously
2. No predefined workflow constraints
3. Dynamic tool discovery during reasoning
4. Single coherent reasoning process

### Step 2 — Implement Memory Folding
1. Agent triggers <fold_thought> token at logical points
2. Auxiliary LLM compresses history into 3 memories:
   - Episodic: key events, decision points
   - Working: current state, obstacles, plans
   - Tool: tool interactions, effectiveness
3. Replace raw history with compressed memories
4. Reduces error accumulation

### Step 3 — Train with ToolPO
1. LLM-simulated APIs for training
2. Tool-call advantage attribution
3. Fine-grained credit to tool invocation tokens
4. Align tool calls with end-task success

### Step 4 — Deploy & Evaluate
1. Test on general tool-use tasks
2. Test on downstream applications
3. Compare: end-to-end vs workflow-based
4. Expected: end-to-end > workflows

## Expected output
- Superior performance on tool-use benchmarks
- Better long-horizon task completion
- Autonomous tool discovery
- Reduced error accumulation via memory folding

## Example application
**Scenario**: Build AI assistant that can use multiple tools (search, code, APIs).

**Application**:
1. Setup: agent reasons autonomously, discovers tools dynamically
2. Memory folding: compress past interactions at logical points
3. Training: ToolPO with simulated APIs
4. Result: 89% on TMDB, 91.8% on ALFWorld — outperforms workflow agents

## Gotchas
1. **End-to-end > workflows**: Don't constrain with rigid workflows. Let agent reason
2. **Memory folding is key**: Reduces error accumulation. Trigger at logical points
3. **ToolPO improves tool use**: Aligns tool calls with task success
4. **Open-set tool discovery**: More robust than pre-retrieved tools
5. **Auxiliary LLM needed**: For memory folding compression
6. **LLM-simulated APIs**: For training. Real-world fidelity may differ
