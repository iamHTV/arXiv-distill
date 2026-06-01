# [2510.18155] LLM-Based Multi-Agent System for Simulating and Analyzing Marketing and Consumer Behavior

## Problem
Prior work fails to simulate complex consumer behavior because: post-event analyses and rule-based ABMs struggle to capture the complexity of human behavior and social interaction. Conventional ABMs rely on fixed heuristics, cannot model cognitive depth, social influence, and individual variation.

## Contribution
1. **LLM-powered multi-agent simulation framework**: Generative agents can interact, express internal reasoning, form habits, and make purchasing decisions WITHOUT predefined rules
2. **Emergent social dynamics**: Agents self-organize, spread information, form habits — behaviors not pre-programmed
3. **Actionable strategy-testing outcomes**: Simulate price discount scenario before real-world deployment

## Method (core summary)
11 agents in a virtual town with 10 locations: residential, business district, main street. Each agent has a unique persona — demographics, income, preferences. Needs system: grocery, energy, finance. Agents use DeepSeek-V3 to plan daily routines, make dining decisions, converse with other agents. Fried Chicken Shop offers 20% midweek discount. Simulation runs 7 days, agents have memory, planning, reflection capabilities.

## Key Findings
- Fried Chicken Shop revenue increased 51% from Day 2 ($100.6) to Day 3 ($152.11) despite discount
- Market share: Fried Chicken Shop from 30% → 41% (Day 3), Local Diner from 62% → 48%
- Promotional effect lasted 2-3 days before declining
- Coffee Shop stable at $30-40/day — different segment, less sensitive to lunch/dinner promotions
- Delayed peak on Day 3 — gradual information diffusion through agent network
- Substitution effect: customers shifted between providers, did NOT increase total spending
- Emergent social dynamics: agents self-organized breakfast plans, invited friends — natural word-of-mouth diffusion
- Habit formation: repeat visits after discount ended

## Actionable Insights
1. **Test marketing strategy before deployment**: Use LLM multi-agent simulation to simulate campaigns before running them. Example: want to test 20% discount on product → simulate with virtual consumers with diverse personas → observe purchase behavior, loyalty, word-of-mouth before spending real budget.

2. **Emergent behavior reveals hidden patterns**: Simulation can reveal patterns that rule-based models miss. Example: agents self-form breakfast clubs, invite friends → insight: discount not only drives direct sales but also creates social events → opportunity for event-based marketing.

3. **Substitution vs expansion**: Discount primarily drove substitution between providers, did NOT increase overall market. Example: 20% discount attracts customers from competitors but total market size unchanged → need to combine with market expansion strategies.

## Assumptions & Limitations
**Conditions for the method to work:**
- Needs capable LLM to generate realistic agent behavior — here uses DeepSeek-V3
- Needs virtual environment with spatial dynamics
- Agent personas must be diverse enough to capture behavioral variation

**Limitations the paper acknowledges (from section headers):**
- LLM Sensitivity and Prompt Robustness
- Execution Sensitivity and Energy Recovery Handling
- Age-Specific Behavioral Fidelity
- [Detailed limitation content not available in HTML]

**Limitations the paper does NOT mention:**
- Only 11 agents — too few to simulate real market (need 1000+)
- Only 1 scenario (discount) — not tested with other marketing strategies
- Not validated against real-world data — only literature validation
- Virtual town too simple — real consumer behavior much more complex
- Does not discuss cost of running LLM simulations at scale
- Does not address LLM hallucination in agent reasoning

## Metadata
- Year: 2025
- Authors: Man-Lin Chu, Lucian Terhorst, Kadin Reed, Tom Ni, Weiwei Chen, Rongyu Lin
- Category: cs.AI, cs.MA
- Conference: IEEE ICEBE 2025
- PDF: https://arxiv.org/pdf/2510.18155
- Citation count: [EXTRACTION FAILED]
