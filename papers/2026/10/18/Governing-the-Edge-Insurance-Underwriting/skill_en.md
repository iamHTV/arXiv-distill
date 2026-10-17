# Skill: Multi-Agent Compliance-First Workflow for Insurance Underwriting

Source: 2609.37454v1
Type: framework

## When to use this skill
- You are building multi-agent to automate processing of forms with strict compliance requirements (insurance, finance, legal).
- You need to ensure sensitive data is not leaked to the cloud.
- You want compliance rules to be enforced structurally (structural governance), not just checked after the fact.

## When NOT to use this skill
- Simple processes without strict compliance requirements.
- You don't have a local backend system to process sensitive data.

## Input required
- List of compliance rules (STOP and WARN) for your domain.
- List of sensitive data fields to keep local.
- Local LLM (e.g., Gemma 2) and cloud LLM (e.g., Claude Sonnet).
- LangGraph or equivalent library to build state graph.

## Steps to execute
1. Design a LangGraph state graph with agent nodes and edge conditions checking compliance before state transition.
2. Split agents into two tiers: local tier processes sensitive data, cloud tier processes anonymized scores.
3. Write hard-stop rules (STOP) as deterministic Python functions, not dependent on LLM output.
4. Each agent can only call bound tools; every call is logged to audit log.
5. If compliance returns FAIL, route to human escalation — agent cannot continue.
6. If confidence score is below threshold (e.g., 0.80), route to human escalation interrupt.

## Expected output
- A multi-agent workflow with compliance built into graph structure.
- Sensitive data never leaves local environment.
- Complete audit trail for every agent action.
- Hard-stops enforced correctly and reproducibly.

## Example application
You build an agent to automatically process bank loan applications. STOP rules (e.g., credit score too low, income unverified) are written as deterministic Python functions and set as edge conditions between agents. If any STOP rule fails, the application is routed to a bank officer for approval — the agent cannot decide on its own. Sensitive customer data (ID number, account number) is processed locally only; cloud agents receive only anonymized risk scores.

## Gotchas
- External tools are synthetic stubs in the current prototype, not connected to live APIs.
- STOP rules depend on fields extracted at temperature 0; accuracy depends on field extraction quality.
- On-device inference makes the framework slower per submission than a single cloud prompt.