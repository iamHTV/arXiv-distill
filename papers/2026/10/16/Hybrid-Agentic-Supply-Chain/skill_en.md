# Skill: hybrid-agentic-supply-chain-analytics
Source: 2609.13561v1
Type: framework

## When to use this skill
- Building a supply chain analytics system for a business.
- Need to handle tasks requiring diverse expertise (database querying, KPI analysis, demand forecasting, performance diagnosis).
- Have supply chain data and want to use LLM agents for decision making.

## When NOT to use
- No supply chain data.
- Only need simple analysis, no multi-agent needed.

## Required input
- Supply chain data (sales, inventory, suppliers, demand).
- LLM models (reasoning and non-reasoning).
- An agentic framework (coordinator + specialist agents).

## Steps
1. Identify the domains of expertise to handle (database querying, KPI analysis, demand forecasting, performance diagnosis).
2. Create specialist agents for each domain, each specialist responsible for one type of task.
3. Create a coordinator agent to coordinate between specialists and make the final decision.
4. Use reasoning models for complex tasks (>90% accuracy), non-reasoning models for simple tasks (~65%).
5. Evaluate accuracy on real data before deployment.

## Expected output
- 90% accuracy for multi-agent design, competitive with single agent baseline.
- Reasoning models achieve >90%, non-reasoning models achieve ~65%.

## Example application
Solopreneur building an inventory management system for an online store: create a specialist agent for demand forecasting (using historical sales data), a specialist agent for KPI analysis (sell-through rate, excess inventory), and a coordinator to aggregate and suggest optimal inventory levels. Use reasoning models for complex forecasting, non-reasoning models for simple data queries.

## Gotchas
- Reasoning models are needed for complex tasks (>90% accuracy vs ~65% non-reasoning).
- Multi-agent design needs a good coordinator; if the coordinator is weak, the system is not effective.
- Need complete and accurate supply chain data for agents to make correct decisions.
