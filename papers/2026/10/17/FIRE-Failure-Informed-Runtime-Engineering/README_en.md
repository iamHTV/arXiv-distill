# [2609.26048v1] FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents

## Problem
- Language-model agents often reach a working solution but fail to consistently deliver it. Prior work does not address procedural loss — where the model produces the substance of a solution but the system loses it during delivery — because it focuses on asking the model to check its own work (reflection, self-refinement) or on improving model capability, rather than intervening at the agent harness layer.

## Contribution
- Runtime policies: targeted natural-language instructions and action denials applied by the agent harness at states preceding observed failures, without changing model weights or the user prompt.
- Policy abstraction P = (E, G, A, R, S): eligibility predicate, runtime predicate, intervention, release condition, state tracking.
- Method to build and freeze a policy portfolio from failed attempts.

## Method (core summary)
- Run the policy-free agent twice per task, inspect 1/2 and 0/2 failures to find clear procedural omissions.
- Cluster by mechanism rather than task, register state → intervention → behavior → verifier condition, write task-agnostic predicates.
- Screen candidates on positive and nearby-negative tasks; revise or retire inert, over-broad, or harmful candidates.
- A policy enters the frozen portfolio only with an observable failure state, a focused positive result, and an acceptable routing audit.
- Frozen Terra portfolio: 8 families in 7 source files and 11 rules.

## Key Findings
- Terminal-Bench 2.1, 87 tasks, 2 attempts each: Luna pass∧2 50.6%→54.0%, Terra 55.2%→60.9%, Sol 64.4%→73.6%.
- Sol: pass@2 nearly flat (+1.2 points) but pass∧2 rises 9.2 points — policies convert reachable solutions into dependable delivery.
- Five-arm randomized panel: real policies reach 61% on 14 eligible tasks vs 39% no policy, 36% timing-matched sham, 39-43% generic verification/reconsideration.
- Intended corrective behavior appears in 22 of 24 real-policy attempts vs at most 14 in any other arm.
- Policy-guided Terra reaches 71.4% on 14 covered tasks vs 64.3% for unassisted Sol, at about half the cost ($7.19 vs $14.48).

## Actionable Insights
1. Runtime policies make capabilities the model already has substantially more repeatable, without changing the model. Application: add a Policy Engine to the agent harness, listen for stop and before-tool-call events, inject guidance when a risky state is detected (server not detached from session, database opened before copying).
2. Policy content matters more than timing — generic "check your work" instructions do not help. Application: write specific policies for each procedural failure type (service persistence, database evidence preservation) instead of using generic prompts.

## Assumptions & Limitations
- Two attempts per task; pass∧2 is an observed rate, not a long-run reliability estimate.
- Panel tasks come from the development population.
- Constraints: one English benchmark (Terminal-Bench 2.1), one harness (Codex CLI), one model family, one reasoning effort.
- Models identified by provider route rather than immutable checkpoint hash.
- Policies target procedural loss, not missing knowledge or capability.
- Not stated: building policies requires observing failures first; policy portfolios are model-specific.

## Metadata
- Year: 2026, authors: Nikita Agarwal, Nivedit Jain (Failproof AI), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2609.26048v1
