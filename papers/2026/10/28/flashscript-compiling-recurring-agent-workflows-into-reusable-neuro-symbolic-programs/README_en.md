# 2610.33876v1 FlashScript: Compiling Recurring Agent Workflows into Reusable Neuro-Symbolic Programs

## Core Value (1 sentence)
FlashScript compiles a successful agent run into a reusable neuro-symbolic program (NSP) — actions and data transformations become code, instance-specific values become parameters, and decisions needing model judgment become typed LLM calls (llm<T>) — making recurring work run identically every time, using ~70× fewer input tokens and 1/3 the runtime of a skill-guided agent.

## Problem
AI agents increasingly perform recurring tasks on behalf of end users. However, agentic workflows do not behave like conventional software: an agent reconstructs the procedure on every run, so repeated executions of the same request can diverge in path and outcome. A successful execution holds valuable procedural knowledge, but this knowledge is buried within a session — a user may inspect, correct, and approve a run, but that effort never carries over to future executions. Prior methods (experience-based memory, programming-by-demonstration, trajectory compilation) either help agents reuse experience but runs still vary, or preserve execution directly but generalize poorly when inputs or environment change.

## Contribution
1. FlashScript — authoring guidance for writing neuro-symbolic programs (NSPs) from prior agent runs. Compiles a completed run into a script with an additional operation llm<T>, sending a prompt to a model and returning a value of declared type. Actions become code, reasoning becomes model calls when future runs need judgment.
2. Identifies three layers where model calls belong: input layer (unstructured text → typed values), computation layer (semantic decisions hard to express as rules), output layer (render computed results in natural language). Identifies three techniques to replace most calls with code: caching observed values behind a guard, codifying judgments as rules, clubbing independent questions into one call.
3. Evaluated on 120 WorkBench analytics tasks with Claude Haiku 4.5: NSPs correct and identical on every run, using ~70× fewer input tokens and 1/3 the runtime of a skill-guided agent. On composite tasks, skill-guided agent accuracy fell to 23% while NSPs stayed correct. NSPs solved all 108 unseen instances (100% accuracy vs 96% for skill-guided agent).

## Method
The FlashScript pipeline has these main steps:
1. Each completed agent run becomes the starting point — a successful run reached through turns of feedback and manual fixes.
2. Compile the run into a script with llm<T> operation: actions become code, instance-specific values become parameters, each decision needing model judgment becomes a typed call llm<T> returning a value of declared type T at a fixed point in code.
3. Identify three layers where model calls belong: input layer, computation layer, output layer.
4. Apply three techniques to reduce model calls: caching observed values behind a guard, codifying judgments as heuristic rules, clubbing independent questions into one call or running in parallel.
5. Bound each neural call: NSP selects its inputs, checks response type, makes call at fixed point in code. Control flow determines when model is queried, for what, and how response is used.

## KNOWLEDGE — Data & Concepts
- Neuro-symbolic program (NSP): program combining code and calls to learned models, with each call having explicit input format, output type, and defined use in the NSP.
- llm<T>: model call operation returning a value of declared type T (string, Boolean, option).
- Three layers of model calls: input layer, computation layer, output layer.
- Three techniques to reduce model calls: caching, codify, clubbing.
- 120 WorkBench analytics tasks from 69 request templates with 10 instances each; 12 Analytics templates (120 tasks).
- Model: Claude Haiku 4.5, temperature 1.
- NSP: correct and identical tool calls on every run; ~70× fewer input tokens; 1/3 runtime vs skill-guided agent.
- Composite tasks: skill-guided agent accuracy 23%, NSP 100%.
- 108 unseen instances of same templates: NSP 100% accuracy vs 96% skill-guided agent.
- 69 neural calls total across all NSPs: 49 guarded input calls + 20 reply calls, averaging 1.5 calls per run.
- Three conditions (C1-C3): consistent, generalizable, cheap.

## INSIGHT — Mechanism & Why
- [Agent runs are inconsistent] occurs because an agent reconstructs the procedure on every run, so repeated executions of the same request can diverge in path and outcome. This means a user cannot trust a reviewed procedure will run the same way next time.
- [Skill helps but does not eliminate inconsistency] occurs because skill provides guidance but the agent still decides how to execute it, so runs still vary (skill-guided agent reaches 99% consistency but not 100%). This means having a skill alone is not enough — need to compile into deterministic code.
- [NSP localizes nondeterminism] occurs because NSP does not remove nondeterminism but localizes it, so the deterministic program and its neural calls can be reviewed and tested separately. Each neural call has explicit input format, output type, and defined use in the NSP. This means testing and maintenance can separate deterministic code from neural components.

## IDEA — Actionable Applications
1. Apply FlashScript to your company's recurring work: take a successful agent run, compile into a Python NSP with bounded llm<T> calls, then run the NSP instead of the agent on each recurrence. First step: pick a recurring task (e.g., weekly report update), run the agent once successfully, then write the NSP from that run following FlashScript guidance.
2. Use caching of observed values: keep values observed in a run and check a condition before reusing in a future run; call the model only if the condition fails. First step: find stable values in prompts (e.g., sheet name, city code) and store in a dictionary instead of asking the model every time.
3. Apply codify for repeated judgments: replace repeated judgments with heuristic rules (e.g., regex to flag pre-visit money transfer requests as scams). First step: identify repeated decisions in the agent and write rules instead of calling the model every time.

## WISDOM — General Principle
- Principle: Recurring agent work should be compiled into testable, maintainable software, not just saved as a skill or memory — deterministic code for consistency, bounded LLM calls for cost control.
- When to use: When you have recurring agent work with new data or small changes each time (weekly reports, order processing, data analysis...).
- When NOT to use: When work does not recur (each time completely different) or when consistency is not needed (creative chatbot, free-form writing...).

## Assumptions & Limitations
- Required condition: Need a successful agent run as starting point; user has spent time clarifying the request and manually editing to get desired output.
- Paper-acknowledged limitations: NSPs do not remove nondeterminism, only localize it; generalization depends on how many decisions are left for model calls (delegating more handles more variation but reduces consistency and efficiency).
- Limitations the paper does NOT state: Does not explain how to automatically generate NSP from a run without human intervention (currently needs a coding agent to write NSP from FlashScript instructions).

## Metadata
- Year: 2026
- Authors: Sadra Sabouri, Hosein Hasanbeig, Adam Sage, Shreya Sinha, Cale Darling, Ashish Tiwari, Katie Garms, Souti Chattopadhyay, Sumit Gulwani
- arXiv category: cs.HC
- PDF link: https://arxiv.org/pdf/2610.33876v1
- Classification: [applied]