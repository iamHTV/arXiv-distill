# Skill: chronos-code-agents-software-evolution
Source: 2610.11578v1
Type: framework

## When to use this skill
- Building code agents that use pull request history.
- Want agents to understand why code was written that way (design decisions, compatibility constraints, implementation patterns).
- Have real pull request history and codebase data.

## When NOT to use
- No pull request history or real codebase data.
- Only need agents to write code from scratch, no need to understand history.

## Required input
- Pull request history and real codebase data.
- An LLM agent system that can access and use pull request history.
- A mechanism to retrieve experience from pull request history (graph-grounded retrieval).

## Steps
1. Collect pull request history and real codebase data.
2. Build an LLM agent system that can access pull request history.
3. Build an experience retrieval mechanism from pull request history (graph-grounded retrieval) instead of flat semantic retrieval.
4. Before agent writes code or fixes bugs, agent retrieves relevant experience from pull request history.
5. Agent uses this experience to make better decisions about bug fixes, feature implementation, and code refactoring.

## Expected output
- Mean resolution rate from 69.2% to 72.9% (+3.7pp).
- SWE-Bench Pro: 48.3% → 51.7%; FEA-Bench Lite: 41.0% → 43.5%.
- Fraction of tasks receiving useful experience: 68% → 89%.

## Example application
Solopreneur building a bug-fixing agent for their software project: agent accesses pull request history to understand why code was written that way, then uses this experience to fix bugs correctly. Reduces agent providing inappropriate solutions or introducing new bugs.

## Gotchas
- Need enough pull request history and real codebase data; no data, no experience to retrieve.
- Need to build an experience retrieval mechanism (graph-grounded retrieval) suitable for your domain; don't use flat semantic retrieval alone.
- Need to evaluate quality of retrieved experience to ensure agent doesn't use irrelevant experience.
