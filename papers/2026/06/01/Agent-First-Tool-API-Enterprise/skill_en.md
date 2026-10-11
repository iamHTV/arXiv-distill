# Skill: Agent-First Tool API — Semantic Interface for Enterprise AI
Source: 2605.10555
Type: framework

## When to use this skill
- When designing APIs for AI agents in enterprise
- When migrating from CRUD APIs to agent-friendly APIs
- When needing structured tool interactions for autonomous agents

## When NOT to use
- Simple CRUD operations sufficient
- No AI agents in system
- Legacy APIs cannot be modified

## Required inputs
- Enterprise API inventory
- Tool registration system
- Governance policies
- Risk escalation rules

## Steps

### Step 1 — Implement Six-Verb Protocol
1. Search: agent finds suitable tools
2. Resolve: agent determines specific tool with parameters
3. Preview: agent previews expected results
4. Execute: agent executes tool
5. Verify: agent verifies results
6. Recover: agent recovers from errors
7. Output: structured tool interaction flow

### Step 2 — Define NTC (Normalized Tool Contract)
1. Each tool response contains:
   - Confidence score
   - Evidence chain
   - Suggested next actions
2. Output: structured metadata per response

### Step 3 — Setup Governance
1. Static policies: what tools can do (read, write, delete limits)
2. Dynamic risk: real-time escalation rules
3. Output: dual-layer governance

### Step 4 — Deploy & Monitor
1. Register tools with NTC
2. Monitor task success rates
3. Track human interventions
4. Output: production agent system

## Expected output
- 88% task success rate (vs 64% CRUD)
- 72.7% reduction in human interventions
- 5.8x better error recovery

## Example application
**Scenario**: Enterprise SaaS platform wants to expose APIs for AI agents.

**Application**:
1. Six-Verb: agent searches "find customer" → resolves customer ID → previews data → executes update → verifies change → recovers if error
2. NTC: API returns {data: ..., confidence: 0.95, evidence: ["db_record"], next_actions: ["verify_email"]}
3. Governance: static (agent can read, not delete) + dynamic (bulk delete → escalate)
4. Result: 88% success, 72.7% fewer human interventions

## Gotchas
1. **Six-Verb Protocol**: Search → Resolve → Preview → Execute → Verify → Recover
2. **NTC is key**: Structured metadata in responses for agent decision support
3. **Dual-layer governance**: Static policies + dynamic risk
4. **Migration cost**: Moving from CRUD to Agent-First requires effort
5. **Backward compatible**: Orthogonal to MCP, operates as semantic layer above
