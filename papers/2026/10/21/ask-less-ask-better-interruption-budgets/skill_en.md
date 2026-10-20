# Skill: interruption-budget-user-attention-cost

Source: 2610.24411v1
Type: framework / workflow

## When to use this skill
- When evaluating user burden when proactive LLM agents ask clarifying questions in customer service.
- When wanting to limit the number of questions agents ask per session (interruption budget) and measure question quality (user-attention cost).
- When needing to build a memory-guided review agent to filter out unworthy questions before presenting them to users.

## When NOT to use this skill
- When only needing simple agent-user interaction counting.
- When lacking simulated users who reveal preferences only when asked.
- When lacking an LLM judge to score reading effort and question value.

## Required inputs
- User's initial request and customer-service tasks.
- Tools for agents to look up information (order IDs, customer profiles, etc.).
- Simulated users who reveal preferences only when asked.
- LLM judge scoring reading effort (5 dimensions: goal clarity, single ask, answer effort, actionability, conciseness) and question value (4 criteria: missing, unretrievable, needed, user-held).
- Question budget N (1–3 questions for customer service).
- Persistent memory storing users' earlier answers and task evidence (for MGR).

## Steps to execute
1. Set up interruption budget: cap discretionary questions per session (N=1–3 for customer service).
2. Define discretionary questions: clarification, confirmation, request to respond to a suggestion after the initial request; policy-required exchanges (authentication, mandatory confirmations) are exempt.
3. Compute user-attention cost: Afull(τ) = Σ(1 + κeff·e(q) + κval·w(q)), κeff=κval=1; e(q)=1−r(q)/20 (reading effort, 5 dimensions, 0–20); w(q)=1−v(q)/10 (question value, 4 criteria, 0–10).
4. Run agent with budget: while budget remains, discretionary questions go to self-review (APPROVE/SUBSTITUTE/BLOCK); when spent, further discretionary requests are refused.
5. Apply memory-guided review (optional): self-review checks questions against persistent memory (users' earlier answers, task summary, evidence links), APPROVEs questions only users can answer, SUBSTITUTES clearer questions, BLOCKs questions answerable from memory or tools.
6. Evaluate: task reward R(τ), user-attention cost Afull(τ), utility Uλ(τ) = R(τ) − λAfull(τ) (λ=0.03), question value V(q).
7. Compare agents at equal attention cost rather than equal question count.

## Expected output
- Evaluation report: task reward, user-attention cost, question value, utility per model and per budget.
- List of blocked questions from memory-guided review.
- Optimal budget decision per model (most efficient asking models should be allowed more questions).

## Example application
An e-commerce customer support agent. Customer requests "I want a larger size of the perfume I ordered." Without a budget, the agent asks 3 questions: "What's the order ID?", "What size do you want?", "What payment method?". With interruption budget N=1 and memory-guided review, the agent looks up the order via tools, sees there's only one order, and asks just one question: "I found a larger version of your perfume: woody, 100ml. Want to exchange your current one for it?". Attention cost drops from 3 questions to 1, task reward preserved.

## Gotchas
- No real inference cost data for self-review and memory (previously estimated ~1.8 model calls + ~15k tokens/session).
- No evaluation on tasks outside customer service and interactive research.
- No direct comparison with agents that don't ask.
- Results depend on how forthcoming simulated users are.