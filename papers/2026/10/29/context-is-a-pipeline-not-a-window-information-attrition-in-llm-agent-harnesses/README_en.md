# 2610.36114 Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses

## Core value (1 sentence)
The agent harness cuts tool output by character position, not by value, so critical evidence gets deleted while the context window sits 93% empty — measure loss at every pipeline boundary, not just accuracy.

## Problem
Prior work focuses on context window size and how the model attends within it, or how to extend it with memory. But the real gap is: between a tool producing a result and the model reading it, the harness serializes it, cuts it to a budget, keeps or drops parts across turns, and passes it between phases. Each step is a design choice and each step can lose information. The run log records what the tool delivered, not what it produced — so a loss on the way into the log cannot be found in the log. No prior work measures failure at each boundary of this path.

## Contribution
- Models an agent's context as a 5-stage pipeline with one measurable failure at each stage, plus an instrument: per-stage counts and a yield number, applied to their own harness (Sec. II).
- Replay evidence, including a case where the shipped cut deletes an entire evidence class at production scale (Sec. III).
- A registered controlled experiment whose result is a compensation tax: when the agent has another way to reach the answer, the cut costs extra work, not accuracy (Sec. IV).
- A survey of seven agent frameworks: two cut tool output the same unsafe way, and the rest offer no consistent, safer alternative (Sec. III).

## Method (core summary)
The core idea: model the information path from tool to model as five consecutive boundaries:
- S1 produce → deliver: tool produces a result, the harness turns it into text and fits it in a budget before the model ever reads it.
- S2 deliver → act: a worker acts on what it receives, turn by turn.
- S3 act → retain: a worker keeps only so much conversation history before older turns get dropped.
- S4 retain → transfer: a worker that computes something worth reporting must hand it off to whatever writes the final verdict; if it doesn't, the computation is lost even though it happened.
- S5 transfer → persist: nothing carries to the next run (turned off by design to keep runs independent).

S1 and S4 destroy evidence outright: a result or finding is simply gone. S2 cuts a worker off before it finishes, so some work never happens at all. S3 doesn't destroy anything; it only makes a run more expensive by resending history that didn't need resending. S5 looks absent in their setup, but that's a choice, not a failure: they turned it off on purpose. Yield = findings recorded ÷ computations run, a narrow measurable proxy for "work that reached the decision," not relevance.

## KNOWLEDGE — Data & concepts
- Across 720 runs, the single largest prompt was only 23k tokens against a 400k window = 5.75% (window nearly empty).
- 3,827 of 11,189 tool results were cut before reaching the model (34%), and every cut result became broken JSON.
- One field reached the model in only 4.7% of 742 calls; a second field, right next to it in the same payload, reached the model in 99.3% of calls.
- Diagnosis accuracy: spawned faults (culprit process starts mid-trace) scored 40–55/60; resident faults (already running) scored 0–24/60.
- Controlled experiment: from repaired → S1 defect → S1 reversed, tool calls rose 53 → 68 → 76 (+28%, then +43%), computations rose 18 → 32 → 36 (nearly doubled), yield fell 0.61 → 0.34 → 0.31.
- Seven agent frameworks surveyed: langchain-core 1.6.12, langchain 1.4.6, smolagents 1.26.0, openai-agents 0.24.0, autogen-agentchat 0.7.5, pyautogen 0.10.0, crewai 0.11.2. Two cut unsafely (langchain-core slices serialized tool output down to 500 characters, keeping only the front; smolagents deletes the middle of any observation over 20k characters). Three do not cut tool output at all. One cuts only its own tracing data. One structure-aware cutter: a shell middleware that cuts by whole lines and says so.
- Replay of 864 recorded results from 31 runs: every result over the budget broke under the prefix slice, every time; none broke under the row-aware cut. 50% of process-listing calls broke, plus 43% of the agent's own analysis outputs and 1% of small summaries. Only 2.5% of all calls were affected at all.

## INSIGHT — Mechanism & why
- [Agent misdiagnoses resident faults] happens BECAUSE [the harness cuts payload by character position, not by value, so evidence at the end of the payload is deleted entirely while the first field stays intact]. This means [the fault may lie in the harness, not the model, and single-number accuracy does not detect this degradation].
- [Cutting data only increases work, not wrong answers] happens BECAUSE [when the agent has another route to the answer, the loss first shows up as extra work, then as errors]. This means [single-number accuracy testing will miss harness faults; need to measure yield and tool call count].
- Condition: this insight only holds when the agent has an alternative route. With a quiet culprit (only one piece of evidence, no alternative route), cutting data causes definite errors (e.g. resident fault scored 0–24/60).

## IDEA — Actionable applications
1. Apply harness output-cutting checks to your own agent system: first step is to instrument every pipeline boundary (S1–S5), count evidence delivered vs produced, and report yield alongside accuracy on every agent evaluation.
2. Apply structure-aware cutting instead of character cutting: first step is to change the tool output cutting function in langchain/smolagents you use to cut by line or by JSON field rather than by fixed prefix.
3. Apply the "don't cut if you can't parse structure" rule: first step is, before deploying an agent to production, replay real tool results through both cutting rules (prefix and row-aware) to see which evidence disappears.

## WISDOM — General principle
- Principle: "Context is not a window, it is pipeline output — measure loss at every boundary, not just accuracy." When to use: when evaluating or designing LLM agent systems that use tools. When NOT to use: when the system has no tool use or does not run through an agent harness.
- Example outside original domain: CI logs truncated before a developer reads them cause missed build failures — similarly, measure how much of the log remains vs how much was produced, rather than treating build pass/fail as sufficient.

## Assumptions & Limitations
- Conditions required for the method to work: the agent must run through a harness that controls tool data before passing it to the model; tool output must have structure (JSON/lines) for structure-aware cutting to be meaningful.
- Limitations the paper acknowledges: one harness, one domain (kernel traces), one model; hasn't measured other harnesses end-to-end, nor a conventional build-test-fix coding agent; the experiment reintroduces a defect they wrote themselves under registered predictions, not a repair story; 5 recordings per class with paired repeats of the same five recordings, not five independent fault instances; the accuracy split in field data remains correlation, not cause.
- Limitations the paper does NOT state: hasn't measured the impact of cutting on end-to-end latency cost (only notes extra tokens are unnecessary inference cost that won't show up in end-to-end latency, without real numbers); hasn't evaluated cutting impact across multiple models simultaneously (only temperature 0).

## Metadata
- Year: 2026 | Authors: Yuvraj Sehgal (Brock University), Mahsa Panahandeh (University of Ottawa), Naser Ezzati-Jivan (Brock University)
- arXiv category: cs.SE (Computer Science - Software Engineering)
- PDF link: https://arxiv.org/pdf/2610.36114v1
- Abstract link: https://arxiv.org/abs/2610.36114
- Replication package: https://doi.org/10.5281/zenodo.23614755
- Citation count: [not found]
