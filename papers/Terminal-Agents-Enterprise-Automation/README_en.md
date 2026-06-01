# [2604.00073] Terminal Agents Suffice for Enterprise Automation

## Problem
Growing interest in building agents that interact with digital platforms to execute enterprise tasks. Approaches explored: tool-augmented agents (MCP) and web agents (GUI). But unclear whether complex agentic systems are necessary given cost and operational overhead. Is simpler sufficient?

## Contribution
1. **Terminal agents = sufficient**: Coding agent with terminal + filesystem can solve enterprise tasks by interacting directly with platform APIs.
2. **Match/outperform complex architectures**: Terminal agents match or outperform MCP-based agents and web agents.
3. **Lower cost, less overhead**: Simple programmatic interfaces + strong foundation models = sufficient for enterprise automation.

## Method (core summary)
Compares 3 paradigms: (1) Web agents (Playwright MCP — browser interaction); (2) Tool-augmented agents (platform-specific MCP servers); (3) Terminal agents (terminal + filesystem, interact directly with APIs). Platforms: ServiceNow, GitLab, ERPNext. Models: Claude Sonnet 4.6, Claude Opus 4.6, GPT-5.4 Thinking, Gemini 3.1 Pro. Metric: success rate (SR). 729 tasks total.

## Key Findings
- Terminal agents match/outperform complex architectures
- ServiceNow: terminal agents competitive with web agents
- GitLab: terminal agents competitive
- ERPNext: terminal agents competitive
- Lower cost than web agents
- Avoids brittleness of GUI interaction
- Avoids expressivity constraints of predefined tool schemas

## Actionable Insights
1. **Expose stable programmable interfaces**: When building enterprise platforms, expose stable APIs instead of adding abstraction layers. Terminal agents + APIs > complex agent stacks. Example: when deploying enterprise automation, invest in stable APIs rather than fancy agent frameworks.

2. **Simple > complex for enterprise**: Coding agent + terminal + filesystem sufficient for most enterprise tasks. Don't over-engineer. Example: when automating IT support, simple terminal agent calling APIs > complex MCP-based agent.

3. **Strong foundation models are key**: Terminal agents work because foundation models are strong enough. Invest in model quality rather than agent complexity. Example: when choosing automation approach, spend budget on better LLM rather than complex agent architecture.

## Assumptions & Limitations
**Conditions for method to work:**
- Platforms expose APIs
- Strong foundation models available
- Sandboxed terminal environment

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- ServiceNow/GitLab/ERPNext specific — may not generalize
- API quality dependency — poor APIs = poor terminal agents
- Long-horizon coordination across platforms not tested
- Human oversight integration not addressed
- Security implications of terminal access

## Metadata
- Year: 2026
- Authors: Patrice Bechard, Orlando Marquez Ayala, et al. (ServiceNow)
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2604.00073
- Citation count: [EXTRACTION FAILED]
