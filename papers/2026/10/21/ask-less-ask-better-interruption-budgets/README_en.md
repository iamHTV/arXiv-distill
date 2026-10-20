# [2610.24411v1] Ask Less, Ask Better: Allocating User Attention in Proactive LLM Agents with Interruption Budgets

## Core Value (1 sentence)
An evaluation protocol that separates how often proactive agents ask (interruption budget) from how well they ask (user-attention cost): budgets of 1–3 questions cut user-attention cost by 36–73% while keeping 86–94% of task reward, and memory-guided review cuts cost by a further 13% with minimal reward loss.

## Problem
Current evaluations of proactive LLM agents measure user burden by counting questions, treating necessary and avoidable questions equally. But answering each question demands user time and effort, and attention is scarce — the benefit of asking must be weighed against interruption cost.

## Contribution
1. An evaluation protocol separating how often agents ask (interruption budget) from how well they ask (user-attention cost), with a budget capping questions per task and a user-attention cost charging extra for hard-to-read or low-value questions.
2. A human-validated user-attention cost metric: at equal question counts, human annotators agree with the cost on which conversation required more effort 75% of the time.
3. A memory-guided review (MGR) agent that checks each proposed question against persistent memory of users' earlier answers and task evidence, cutting attention cost by a further 13% at the same budget with minimal reward loss.
4. Evaluation across eight LLMs and four customer-service domains, showing models differ sharply in asking efficiency: at the same user-attention cost, the most efficient models gain more than twice as much reward from their questions as others.

## Method
The evaluation protocol uses an interruption budget to cap questions per task, and a user-attention cost to measure how demanding and justified each request is. A discretionary question (clarification, confirmation, or request to respond to a suggestion) after the initial request counts once; policy-required exchanges (authentication, mandatory confirmations) are exempt. User-attention cost: Afull(τ) = Σ(1 + κeff·e(q) + κval·w(q)), with κeff = κval = 1, each request costs 1–3 units. Reading effort: LLM judge rates on 5 dimensions (goal clarity, single ask, answer effort, actionability, conciseness), overall score r(q) ∈ [0,20], effort cost e(q) = 1 − r(q)/20. Question value: v(q) ∈ [0,10] by 4 criteria (answer missing from conversation, unretrievable with tools, needed for task, user-held), avoidability cost w(q) = 1 − v(q)/10. Utility: Uλ(τ) = R(τ) − λAfull(τ), λ = 0.03. The memory-guided review (MGR) agent: backbone LLM proposes a step, an LLM classifier routes it, and self-review checks the question against persistent memory M = (P, s, I), returning APPROVE/SUBSTITUTE/BLOCK. Persistent memory stores user records P (verbatim replies), task summary s, and evidence links I.

## KNOWLEDGE — Data & Concepts
- 4 customer-service domains (retail, airline, telecom from τ-bench/τ²-bench; Ambiguous WebShop), 382 customer-service test tasks, 559 interactive research tasks
- 8 models: GPT-6-Astra, GPT-5.4, GPT-4.1, Grok-4.6, Grok-4.3, GPT-OSS-120B, Llama-4-Maverick, Llama-3.3-70B
- 3 trials per model in main evaluation
- Unrestricted: asks 2.84 questions/session, cost 49.4, reward 29.5
- Budgeted (N=1–3): cost 44.7, reward 30.7, question value 69.4
- Budgeted + MGR: cost 43.9, reward 30.7, question value 71.7
- Budgets of 1–3 questions cut attention cost by 36–73% vs unrestricted, keeping 86–94% of task reward
- Only 49–80% of the added reward from asking is kept
- At the same budget, MGR cuts attention cost by a further 13% with minimal reward loss
- GPT-6-Astra and Grok-4.6 are the most efficient askers: 7.3–7.8 reward points per cost unit (more than twice any other model, max 3.3)
- Asking frequency does not predict efficiency: on Telecom unrestricted, GPT-4.1 asks 5.7 questions for 5.5-point gain, GPT-6-Astra asks 1.6 for 31.9-point gain
- MGR reduces cost for 7 of 8 models and raises judged value for 6, but reward gains at equal cost are supported only for Grok-4.6 and Llama-3.3
- Interactive research (5 models, N=1–8): budgets save only 15.6% of cost at 3.1-point reward loss, MGR a further 5.4% at further 0.9-point loss
- Human study: at equal counts, annotators judged higher-cost conversation more tiring in 75% of non-tie answers; cost agrees with annotators on 90% of held-out comparisons
- Break-even valuation λ∗ ≈ 0.02: users who would give up more than ~2 reward points to avoid 1 cost unit are better served by a budget
- Self-review and memory updates add ~1.8 model calls and ~15k tokens per session

## INSIGHT — Mechanism & Why
[Asking less and asking better are distinct goals] BECAUSE [a budget controls question frequency but not which questions are spent; an agent can ask few but low-value questions, or many but high-value questions]. This means [proactive agent evaluation should measure both].
[User-attention cost captures burden counts miss] BECAUSE [at equal question counts, conversations with unworthy questions feel more tiring; annotators agree higher-cost = more tiring 75% of the time]. This means [question length is not a good guide to overall burden — unworthy questions, not long ones, make conversations tiring].
[Persistent memory is key for selective review] BECAUSE [without memory, review lowers both reward and judged value at equal cost; with memory, cost is 6.2% lower and 2.9 value points higher at same N]. This means [agents need to know what users already said to avoid asking again].
[Best budget follows asking efficiency] BECAUSE [the most efficient asking models should be allowed more questions; at λ=0.03, the 3 most efficient askers do best with 2–3 questions, the other 5 with 1]. This means [budgets should be model-specific, not one common budget].

## IDEA — Actionable Applications
1. Apply [interruption budget] to [limiting clarifying questions in customer-service agents]: first step is to set a budget of 1–3 questions per session, refusing further discretionary requests once reached.
2. Apply [user-attention cost] to [evaluating question quality of agents]: first step is to use an LLM judge to score reading effort and question value, compute total cost per session, compare agents at equal cost rather than equal count.
3. Apply [memory-guided review] to [filtering out unworthy questions]: first step is to build persistent memory storing users' earlier answers and task evidence, checking each proposed question before delivery.

## WISDOM — General Principles
1. Principle: Question frequency is not a good measure of user burden — both frequency and question quality should be measured. Apply when: evaluating proactive agents that ask users in customer service. Do not apply when: only need simple interaction counting.
2. Principle: Persistent memory of users' earlier answers is a prerequisite for agents to avoid re-asking and ask better questions. Apply when: building agents that ask users across multiple turns. Do not apply when: single-turn tasks with no prior context.

## Assumptions & Limitations
- Conditions that must hold: simulated users reveal preferences only when asked, tools available for agents to look up information, LLM judge available to score reading effort and question value.
- Limitations acknowledged by paper: interactive research budgets save only 15.6% of cost at 3.1-point reward loss, MGR a further 5.4% at further 0.9-point loss, neither improves utility over unrestricted at λ=0.03; results depend on how forthcoming simulated users are.
- Limitations paper does NOT mention: no real inference cost data for self-review and memory (previously estimated ~1.8 model calls + ~15k tokens/session); no evaluation on tasks outside customer service and interactive research; no direct comparison with agents that don't ask.

## Metadata
- Year: 2026
- Authors: Xuanming Zhang, Amir H. Rezaeian, Miguel Ballesteros, Weiyi Sun, Werner Geyer, Lydia B. Chilton, Zhou Yu, Yassine Benajiba, Dan Roth (Columbia University, Oracle AI)
- arXiv Category: cs.CL
- PDF Link: https://arxiv.org/pdf/2610.24411
- arXiv ID: 2610.24411v1
- Label: [applied]
- Citation count: [not found]