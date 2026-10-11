# [2507.08616] AgentsNet: Coordination and Collaborative Reasoning in Multi-Agent LLMs

## Problem
LLMs organized in multi-agent systems have powerful problem-solving capabilities. But unclear whether these systems can leverage topology effectively. Existing benchmarks only cover 2-5 agents — don't test scalability. Need benchmark measuring coordination, self-organization, communication in larger networks.

## Contribution
1. **AgentsNet benchmark**: Measures ability of multi-agent systems to collaboratively form strategies, self-organize, communicate given network topology.
2. **Classical distributed systems problems**: Coloring, Consensus, Leader Election, Matching, Vertex Cover — adapted for LLM agents.
3. **Scalable**: Practically unlimited size — tests up to 100 agents.

## Method (core summary)
AgentsNet: inspired by distributed systems and graph theory. 5 tasks: Coloring (assign colors, no adjacent same), Consensus (agree on value), Leader Election (choose leader), Matching (pair nodes), Vertex Cover (minimum cover set). Homogeneous networks: agents must agree on basic protocols first. Evaluates frontier LLMs on different network sizes.

## Key Findings
- Claude 3.7 Sonnet: 0.70 AgentsNet score (best)
- Claude 3.5 Haiku: 0.26
- GPT-4.1 mini: 0.45
- Frontier LLMs strong on small networks, fall off at scale
- Consensus easiest (1.00 for Claude 3.7), Vertex Cover hardest (0.40)
- Scaling challenge: performance drops as network size increases

## Actionable Insights
1. **Topology matters for multi-agent**: When building multi-agent systems, consider network structure. Agents must agree on protocols first. Example: when deploying multi-agent customer service, agents must agree on communication protocol before collaborating.

2. **Consensus is easiest, coordination is hard**: Models excel at agreeing on values but struggle with complex coordination. Example: multi-agent pricing — agents easily agree on market price but struggle to coordinate competitive strategy.

3. **Scaling challenge**: Strong on small networks, weak at scale. Start small, expand gradually. Example: when deploying multi-agent system, start with 5-10 agents, test coordination, then scale.

## Assumptions & Limitations
**Conditions for benchmark to work:**
- Homogeneous agents (same model)
- Network topology defined
- Classical distributed systems problems adapted

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- Homogeneous agents only — heterogeneous not tested
- Classical problems may not capture real-world coordination
- Communication costs not modeled
- Real-world multi-agent tasks more complex

## Metadata
- Year: 2025
- Authors: Florian Grötschla, Luis Müller, Jan Tönshoff, Mikhail Galkin, Bryan Perozzi
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2507.08616
- Citation count: [EXTRACTION FAILED]
