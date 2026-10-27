# arXiv Distill Daily Report — 2026-10-28

Summary of 7 papers distilled today, each gone through the 6-step distill process, committed and pushed to GitHub. Each paper below has 3 parts: What it does, What we learn, Apply to you — written in simple English for solo entrepreneurs in Vietnam.

## 7 papers today

### [1] Task Success Is Not Enough: Side-effect-Aware Evaluation of Tool-Using Language Model Agents (2610.34167v1)
- What it does: Research shows evaluating an AI agent (autonomous task performer) only by whether it completes the task is insufficient. An agent can complete the task while still writing data (emails, tickets...) outside its authorized scope, happening in 15.2% of runs.
- What we learn: Need to check two things: is the task done AND did the agent write anything outside permitted scope. A confirmation policy before writing reduces this error by 52–71%.
- Apply to you: Before letting AI write emails or update orders automatically, list 3–5 permitted write operations and ask AI to show the list of operations it intends to perform for your approval first.

### [2] Lessons from Luck: Do LLM-Written Lessons Carry Chance into an Agent's Next Decision? (2610.33029v1)
- What it does: Lessons AI writes from previous runs can carry luck into later decisions. After a random tool failure, readers of that lesson chose a worse tool in 11.6% of runs, 29× higher than 0.4%.
- What we learn: Don't let AI save lessons from a single run's outcome without checking whether the decision was correct based on information available before knowing the outcome.
- Apply to you: If you use AI to auto-remember business experience (memory), add this requirement: "before writing a lesson, judge whether the decision was correct based only on information before the outcome; only recommend a change if the decision was wrong."

### [3] Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents (2610.34817v1)
- What it does: Errors from incorrect integration of prompt caching (technique to reuse processed prompt parts to reduce cost) often fail silently: 90% of errors don't crash or report errors, just increase the API bill because AI reprocesses the entire prompt every time.
- What we learn: Don't just wait for crashes; monitor cache-hit rate (times prompt is reused) to detect cost increases happening silently.
- Apply to you: If you use AI agents with prompt caching to reduce cost, check your API bill regularly — if cost rises abnormally while results remain correct, caching may have been silently disabled.

### [4] FlashScript: Compiling Recurring Agent Workflows into Reusable Neuro-Symbolic Programs (2610.33876v1)
- What it does: Compiles a successful AI run into a reusable program (neuro-symbolic program — combines code and AI calls). Repeated work runs identically every time, using ~70× fewer prompt calls and 1/3 of the time.
- What we learn: Repeated AI work should be turned into deterministic code rather than just saved as a "skill" or "memory", for stable results and controllable cost.
- Apply to you: For weekly repeated work (e.g. updating sales reports), run AI once successfully, then write a fixed code process to run each week instead of letting AI redo it from scratch.

### [5] Not Every Agent Needs the Strongest Model: Unified Prompt-Model Optimization for Heterogeneous LLM-based Multi-Agent Systems (2610.31743v2)
- What it does: Not every agent in a multi-agent system (multiple AI agents working together) needs the strongest model. Assigning lighter models to summarization tasks and stronger models to reasoning tasks achieves higher scores with 85.2% lower cost.
- What we learn: Should classify agent roles and assign appropriate model capabilities rather than using one model for everything.
- Apply to you: If you run multiple AI agents, use cheaper lighter models for text summarization tasks, and only use more expensive stronger models for tasks requiring reasoning or quality checking.

### [6] AgentOrch: How Close Can Global Orchestration Come to Step-by-Step Interaction? (2610.33375v1)
- What it does: Compares two ways to run enterprise workflows: planning everything upfront (global orchestration) uses 23.2× fewer AI prompt calls but is less accurate than step-by-step.
- What we learn: Can close the accuracy gap to about 8.5 points by building workflows incrementally and revising workflows based on execution results.
- Apply to you: If you use AI to automate business workflows (e.g. creating orders, updating CRM), try writing the entire workflow once and running it in a loop, only calling AI step-by-step when changes are needed based on previous results.

### [7] Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge (2610.32415v1)
- What it does: The ANT-OR multi-agent framework improves automatic labeling accuracy by 4.5 points over the strongest baseline and reaches a level consistent with how humans label (within 2 points by Fleiss' κ — coefficient measuring consistency among multiple labelers).
- What we learn: AI labeling should be evaluated by consistency with the distribution of opinions from multiple people, not just compared to a single answer.
- Apply to you: If you use AI to classify content or evaluate leads (potential customers), ask 3–5 people to review the same sample and use majority agreement as the standard instead of just one opinion.

## WHAT YOU CAN APPLY

1. Before letting AI write data automatically (emails, order updates), list permitted write operations and ask AI to show intended operations for your approval first. Helps avoid unintended side effects.
2. If you use AI to auto-remember business experience, require it to judge whether a decision was correct based on information before knowing the outcome, only recommend changes if the decision was wrong. Avoid letting lucky or unlucky outcomes override real business experience.
3. If you use AI agents with prompt caching to reduce cost, monitor your API bill regularly — abnormal cost increases may indicate caching was silently disabled.
4. Weekly repeated AI work should be turned into fixed code processes instead of letting AI redo from scratch, for stable results and controllable cost.
5. Classify AI agent roles and assign appropriate models: cheaper lighter models for text summarization, more expensive stronger models only for reasoning or quality-checking tasks. Helps reduce costs significantly.

---

All 7 papers have been fully distilled through 6 steps (README, skill, skill test, commit+push) and stored in papers/2026/10/28/.
