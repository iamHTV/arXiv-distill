# Skill: Prompt Injection Defense Architecture for Multi-Agent Systems

Source: 2609.22949v1
Type: framework

## When to use this skill
- You are building multi-agent systems and want to protect against prompt injection attacks.
- You need to understand attack surfaces unique to multi-agent systems (not just single-model prompt injection).
- You want to implement architectural defenses rather than relying only on system-prompt guardrails.

## When NOT to use this skill
- Single-agent systems (no inter-agent communication).
- You don't need high security for your agent system.

## Input required
- Multi-agent system with agents having different roles and tools.
- Infrastructure to deploy message signing, boundary sanitization, role-scoped tool access, and anomaly detection.
- Cryptographic signing library (Ed25519) for inter-agent messages.

## Steps to execute
1. Build a threat model for your multi-agent system: enumerate attack vectors (direct via user input, indirect via tool outputs, inter-agent via messaging, cascading via orchestrator).
2. Implement message signing with provenance: every inter-agent message carries a cryptographic signature and provenance record; receiving agents verify signatures before processing.
3. Implement input/output sanitization at agent boundaries: structural validation, instruction detection, content-length enforcement.
4. Set up privilege-scoped tool access per agent role: each agent only has access to tools permitted by its role, enforced at infrastructure layer.
5. Deploy anomaly detection on inter-agent communication patterns: model expected communication as a directed graph, flag deviations.

## Expected output
- A multi-agent system with robust protection against prompt injection attacks.
- Injection success rate reduced from 31.2% to 4.2%.
- Layered defenses: message signing, boundary sanitization, privilege-scoped tool access, anomaly detection.

## Example application
You build a multi-agent system for processing financial documents. Agents exchange internal messages (retrieval agent sends data to analysis agent, analysis agent sends results to compliance agent). You implement message signing to authenticate every inter-agent message, boundary sanitization to prevent instructions embedded in tool outputs, role-scoped tool access to prevent code agent from accessing compliance databases, and anomaly detection to catch routing manipulation. Injection success rate drops from 31.2% to 4.2%.

## Gotchas
- System-prompt guardrails are insufficient — agents cannot reliably distinguish injected instructions from legitimate inter-agent messages when both arrive through the same text channel.
- Boundary classifier introduces 2.3% false positive rate and may not generalize to unseen injection formats.
- Adaptive adversaries may achieve higher success rates than fixed payloads.