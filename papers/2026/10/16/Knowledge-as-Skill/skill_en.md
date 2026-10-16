# Skill: knowledge-as-skill-3-layer-kb
Source: 2609.25991v1
Type: framework

## When to use this skill
- Building a knowledge base for an LLM agent to query autonomously.
- Want the agent to decide when to retrieve knowledge, not let simple RAG inject everything.
- Have source documents (PDF, Word, web) to convert into a knowledge structure for the agent.

## When NOT to use
- Agent doesn't need external knowledge (answers only from internal knowledge).
- Don't want the agent to decide retrieval; just want simple RAG.

## Required input
- Source documents (PDF, Word, web) to convert into a knowledge base.
- An agent system capable of autonomous query decisions.

## Steps
1. Split source documents into chunks corresponding to specific skills/knowledge items.
2. Write SKILL.md for each chunk: purpose, when to use, applicability conditions.
3. Create index.md: index linking knowledge parts together.
4. Add frontmatter YAML to the top of each file: metadata (title, author, date, tags...).
5. The agent reads SKILL.md to decide when to query this knowledge, checks index.md to find relevant sections, and stops when it has enough information.

## Expected output
- The agent autonomously decides when to retrieve knowledge instead of RAG injecting everything.
- Factuality 0.889, Context Recall 0.816, Hallucination Rate 4.5% (on WixQA).

## Example application
Solopreneur building a knowledge base for a customer support agent: each return policy, exchange procedure, and product price is written as a SKILL.md with index.md and YAML frontmatter. The support agent reads SKILL.md to know when to apply the return policy, finds relevant sections via index.md, and answers the customer once it has enough information.

## Gotchas
- Evaluation is still preliminary; needs testing on more domains.
- The agent needs autonomous decision-making capability; if the agent is weak, the 3-layer structure doesn't help much.
- Requires investment in writing SKILL.md and index.md for each knowledge part.
