# Skill: Terminal Agent for Enterprise Automation
Source: 2604.00073
Type: workflow

## When to use this skill
- When building enterprise automation agents
- When evaluating agent architectures for enterprise tasks
- When wanting to simplify agent stack

## When NOT to use
- Platforms don't expose APIs
- GUI-only environments (no terminal access)
- Tasks need visual understanding

## Required inputs
- Enterprise platform with APIs
- Strong foundation model (Claude, GPT-5, Gemini)
- Sandboxed terminal environment
- Task descriptions

## Steps

### Step 1 — Setup Terminal Environment
1. Sandboxed terminal with filesystem access
2. API credentials for target platforms
3. Strong foundation model as backbone
4. Output: terminal agent environment

### Step 2 — Implement Agent
1. Coding agent that writes/runs code
2. Interacts directly with platform APIs
3. No GUI interaction needed
4. No predefined tool schemas needed

### Step 3 — Execute Tasks
1. Agent receives natural language task description
2. Discovers APIs dynamically
3. Writes code to complete task
4. Output: task completion

### Step 4 — Evaluate
1. Compare: terminal vs web vs MCP agents
2. Metric: success rate, cost
3. Expected: terminal agents competitive or better
4. Output: architecture recommendation

## Expected output
- Competitive success rate with complex architectures
- Lower cost than web agents
- Simpler implementation
- Dynamic API discovery

## Example application
**Scenario**: Enterprise wants to automate IT support tasks.

**Application**:
1. Setup: terminal agent with ServiceNow API access
2. Task: "Create incident ticket for server outage"
3. Agent: discovers ServiceNow API, writes code, creates ticket
4. Result: task completed, lower cost than web agent scraping GUI

## Gotchas
1. **APIs > GUI**: Expose stable APIs. Terminal agents + APIs > complex stacks
2. **Simple > complex**: Don't over-engineer. Terminal + filesystem enough
3. **Model quality matters**: Invest in better LLM, not complex architecture
4. **Dynamic discovery**: Terminal agents discover APIs on-the-fly
5. **Lower cost**: Terminal agents cheaper than web agents
6. **Platform-specific**: Results on ServiceNow/GitLab/ERPNext. Test on your platforms
