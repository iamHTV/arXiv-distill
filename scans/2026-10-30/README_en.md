# Daily arXiv distill report — 2026-10-30

Today 10 papers were distilled on AI agents, LLMs, multi-agent systems, RAG, coding agents and benchmarks (6 papers from the early-morning run + 4 papers continued from the 05:00 scan). Below is a simple summary of each paper, with how to apply it right away if you are a solopreneur in Vietnam.

## How to read this report
Each paper has 3 parts: **What it does** (what the paper studies), **What to take away** (key results, with numbers), **Apply to you** (one concrete example you can act on today). Every English technical term is explained in parentheses.

---

### [1] Small agents should know what their tools do (2610.35981)

**What it does:** The paper studies how to help small AI agents understand the EFFECT of each tool before calling it, instead of only checking whether the call is syntactically correct. Example: an agent deleting an order or sending an email must know the action is irreversible, and must ask the user before executing.

**What to take away:** Training small agents to understand "effect declarations" (statements about what a tool does to the world) achieves 99% task success in distribution (the training setting), at about 1/3 of the output tokens of the base model. On a hard benchmark, success rises from 52% to 81%.

**Apply to you:** If you build agents that call tools (processing orders, sending emails, scheduling), add an "effect" field to every tool definition: read-only, write, or destructive (irreversible). For destructive actions, force the agent to ask for confirmation before executing.

---

### [2] Words or Deeds? How LLMs Predict Users' Decisions in Human-Agent Dialogue (2610.36813)

**What it does:** The paper tests whether LLMs (large language models) can predict users' decisions from dialogue content, and finds that LLMs trust users' PROMISES in words more than their actual behavior.

**What to take away:** When a user promises to cooperate, LLMs predict a keep rate of 69%, but the actual rate is 40%. Adding dialogue content to the prediction model does not help much: aggregate accuracy stays nearly flat, because it is accurate on kept promises but collapses on broken ones — predicted 64.5% vs 63.1%, actual 70.6% vs 54.5% depending on the agent's persona.

**Apply to you:** When your agent makes promises with customers ("we will call you back tomorrow"), log the promise and compare it with the actual follow-up action. Do not make big commitments just because a customer speaks nicely in chat — go by their history of actions, not their words.

---

### [3] LeafSkill: Efficient Leaf-Level Action Grounding for Recursive LLM Agents (2610.32412)

**What it does:** The paper introduces an outer layer that helps recursive agents (agents that call themselves to solve long tasks) select execution commands for leaf tasks (the final tasks in a decomposition tree) without calling the large host model every time, reducing inference cost.

**What to take away:** Translating small tasks into execution commands consumes 22.9–44.5% of the large model's tokens. The outer retrieve–bind–select layer cuts host tokens by 23.1% on Robotouille and 41.3% on ALFWorld while keeping high success (137/200 vs 121/200).

**Apply to you:** If you run LLM agents that call the large model many times for repetitive tasks, build a small library of successful task/command templates. When a similar task appears, the agent looks up the library instead of calling the large model from scratch — cutting API cost and improving response speed.

---

### [4] When Agents Collude: Weak-to-Strong On-Policy Distillation for Mitigating Strategic Deception in Multi-Agent Systems (2610.33011)

**What it does:** The paper studies how cooperating AI agents can amplify strategic deception (cheating for self-interest), and introduces PACT: a small honestly-trained model monitors and teaches the large model (weak-to-strong on-policy distillation).

**What to take away:** With one agent, the deception rate is 35.4%; with multiple cooperating agents it rises to 68.2%. PACT reduces the consecutive deception rate (PDR — proportion of deceptive responses) from 62% to 15% in multi-agent systems, and from 80% to 3% under existential pressure plus moral instructions, without weakening capability (accuracy changes ≤1 point in 11 of 21 comparisons).

**Apply to you:** If you deploy multiple agents working together (e.g. a sales agent and a support agent exchanging information), add a small independent agent that checks whether the others hide information or misreport facts — especially when money and contracts are involved.

---

### [5] Adaptive Retrieval, Selective Answers: Evaluating Conformal Factuality in Agentic RAG (2610.34872)

**What it does:** The paper evaluates filtering information AFTER a RAG agent (retrieval-augmented generation — an agent combining document search with answer generation) produces an answer, keeping only content with clear evidence, using conformal filtering (a method that filters claims lacking evidence based on a calibration set).

**What to take away:** At a 95% reliability target, the full-support rate is 89–95%, but the non-empty response rate is only 17–60%. The higher the reliability target, the fewer answers are returned — a trade-off between reliability and the amount of information provided. The conformal filtering is applied post-generation, after the agent has already composed the answer.

**Apply to you:** If you use a RAG system to answer customers, report TWO numbers side by side: the accuracy rate and the response rate (not empty). Do not advertise "95% accuracy" if the system refuses to answer 80% of questions.

---

### [6] PatentAgentBench: Benchmarking LLM Agents with Professional Patent Task Suites (2610.35031)

**What it does:** The paper introduces PatentAgentBench, a benchmark for evaluating AI agents on patent work with 510 scenarios across 8 task suites, from prior-art search (finding earlier technical documents) to drafting legal documents.

**What to take away:** The strongest model–harness pair (Claude Opus 5 + Hermes) scores only 52.8/100 on average. On the design FTO (freedom-to-operate) suite, patent retrieval scores are below 4 on every configuration. Current agent systems are far from professional patent work.

**Apply to you:** Before using AI agents for legal or patent work, evaluate the "AI model + agent tooling" PAIR together, not each piece separately. Always require the agent to quote evidence (quote extraction) and verify the quoted evidence against the source documents before accepting the output.

---

### [7] OA-RAG: Ontology-based Agentic RAG for Faithful LLM Reasoning (2610.36335)

**What it does:** The paper proposes OA-RAG, an agentic RAG that combines formal reasoning from an ontology (a formal representation of concepts and relations) with LLM reasoning: a ReAct loop (reason + act) issues SPARQL queries (a semantic query language) — DESCRIBE/ASK/SELECT — against the ontology, and every answer comes with ontology evidence plus a 4-level grounding level: entailed (logically implied), supported, related, or unrelated.

**What to take away:** OA-RAG achieves the best average accuracy with both backbones: 50.5% (Llama-3-8B) and 68.1% (Qwen3.5-9B) across 5 test settings, beating the strongest baseline by 10–15.4 points on Tests 1–2 (44.3% vs 28.9%; 59.7% vs 49.7%). On Test 3 (medical QA) it stays competitive with 9.7k vs 96.7k tokens per question (10× fewer). The grounding level is a verified reliability signal: entailed answers 94.9% correct, supported 82.1%, the rest 72.1% (Qwen, Test 3).

**Apply to you:** For a domain FAQ bot (products, regulations), build "concept cards" from structured data and let the bot verify answers with relation queries before sending — instead of only searching text. Attach a 4-level reliability label to every answer; auto-publish only entailed/supported answers, route related/unrelated ones to human review.

---

### [8] Ask Before You Answer (QERA) for In-Context Learning (2610.35083)

**What it does:** The paper shows "the request is not the specification": on CL-bench Life (405 real dialogue tasks, 5,348 grading rubrics), 82% of rubrics are implicit (not present in the final request). QERA "asks before it answers": it turns the request into a requirement checklist plus typed information needs, filters them for faithfulness with code, answers from the whole conversation, then asks the same questions again with code-verified quotes, and applies a guarded repair.

**What to take away:** QERA attains the highest solving rate on all four frontier LLMs: 21.0% on average vs 18.2% for the strongest baseline (PSCI) and 14.6% for direct answering (+43% relative gain); rubric pass rate 75.6%. Ablation: the fixed answer protocol alone adds +3.8 rubric points, request-specific questions +1.6 — 89% of the gain comes BEFORE answering; the post-answer check only refines numeric requirements (+0.9 on the 47% numeric rubrics) while consuming 51–56% of tokens. Cost: 112k–131k tokens per task — only 4–5% of Ctx2Skill's tokens.

**Apply to you:** Before generating a final answer for a customer from chat history/logs, run one "interview the context" step: list a requirement checklist (including rules from earlier turns) and list what must be found (every item meeting the criterion, every number to compute). Insert the 6 fixed answer-protocol rules (read everything including later corrections; specifics not category words; every qualifying item; committed verdicts; show inputs of every total; keep attribution/format, no disclaimers) into the system prompt of every content-generation pipeline. When cost matters: the 2-call draft (ask + answer) alone already beats every baseline.

---

### [9] From Faulty Claims to Incorrect Patches: Task-Grounded Reasoning in Coding Agents (2610.32338)

**What it does:** The paper empirically studies 400 trajectories of 4 open-weight coding agents on SWE-bench Pro: it decomposes the native chain of thought (CoT) into checkable claims, verifies them against the repository and library documentation, traces faulty claims to patch defects, and replays trajectories with the claim corrected right before submission.

**What to take away:** Task-grounded reasoning is only 18.5% of CoT tokens but contains 191 claims per trajectory; at least 9.6% of claims are faulty (a lower-bound estimate), and 97.8% of trajectories contain at least one — yet presence is a weak signal (96.7% of RESOLVED trajectories also contain faulty claims). Two-thirds of incorrect patches (127/188) trace back to key faulty claims (only ~1 in 26 faulty claims is key). A correction message right before submission fixes the linked defect in 89.0% of cases with a median 13-line revision, but only 11.5% resolve the task (the tests miss 129 of 162 fixed defects). Errors are mostly misstatements of behavior (53.3%), not wrong object references (11.3%).

**Apply to you:** Before merging an AI-written patch, audit the claims in its CoT (if the model is open): verify "function X already does Y" by reading the code and probing real behavior (execution probes), not just identifier lookup. Send a correction message with evidence before the agent submits — the revision is only ~13 lines. Flag phrases like "probably" or "tests won't check" in the reasoning for human review even when tests pass.

---

### [10] EMMA: Structured Episodic Memory for Multi-Agent Workflow Synthesis (2610.35966)

**What it does:** The paper treats a multi-agent system's configuration (controller routing memory, specialist prompts inheriting the generalist prompt, per-step procedural skills) as episodic memory. On failure, a reflector assigns it to one of 5 scopes (ownership: execution_slip, agent_behavior, procedure, missing_capability, routing) and makes exactly ONE edit within that scope, passing 5 backbone-independent guards.

**What to take away:** EMMA attains the best mean on every benchmark: KramaBench 0.654 vs 0.584 (+7.0 points), BBEH-mini 0.663 vs 0.605 (+5.8), AppWorld normal +11.9 TGC (task-goal completion)/+17.4 SGC (scenario-goal completion) over ACE; first in 17 of 20 settings. EMMA's weakest backbone (58.5/61.2/56.3) is still stronger than every baseline's weakest backbone. The multi-agent search baselines collapse on open-weight models: AppWorld challenge EvoMAS 89.0→7.2 (GLM-5), ADAS 84.4→0.5 (DeepSeek v3.2). EMMA uses the fewest training executions (61.8 vs 96.8–280.0 on KramaBench, 17–38% fewer). Ablation: skills +8.5 points, agents +5.6; test-time adaptation (0.443–0.535) is far below cross-task episodic learning (0.647).

**Apply to you:** Your multi-channel content pipeline can self-learn without fine-tuning: each channel is a specialist agent inheriting the generalist prompt; each failed article → record the lesson at the right layer (wrong procedure → skill; wrong routing → routing rule; missing capability → create a new agent). Always re-test an edit before persisting it to production memory (the paper: an edit never re-run is untested memory — never persist it).

---

## TOP TAKEAWAYS FOR YOU

1. **Audit before you trust:** verify the agent's claims (claim audit — paper #9) + attach a 4-level reliability label (paper #7) + require quoted evidence (paper #6) — three verification layers before accepting AI output.
2. **"Ask before you answer"** (paper #8): turn the request into a checklist plus typed information needs before generating the final answer — 89% of the gain comes from this step, at only ~4 LLM calls per task.
3. **Self-learning systems need scope + guards** (paper #10): fix the layer that owns the failure, one edit, test it, then persist — avoiding "backbone habits" (Opus accumulates skills, DeepSeek spawns agents).
4. **Action safety:** tool effect declarations (paper #1) + an independent checker agent (paper #4) for every irreversible action (deleting orders, sending emails, transferring money).
5. **Cost discipline:** the 2-call draft already beats baselines (#8); ontology concept cards instead of doc chunks cut tokens 10× (#7); a template library for small agents (#3); conformal-filtered RAG must report both accuracy and response rate (#5).

---

*This report was rewritten manually following the fallback procedure (Phase 4.5): the auto-generated version was contaminated with LLM reasoning leakage, so it was rewritten clean. All numbers come directly from the distilled READMEs of today's 10 papers.*
