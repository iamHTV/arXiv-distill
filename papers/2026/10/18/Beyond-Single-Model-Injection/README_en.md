# [2609.22949v1] Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems

## Problem
Existing prompt injection research focuses on single-model chatbot scenarios, where an attacker manipulates one LLM through crafted input. Multi-agent systems amplify this threat through three mechanisms absent from single-model settings: inter-agent message passing creates injection channels invisible to perimeter defenses, shared tool access enables privilege escalation across agent boundaries, and trust propagation allows a compromised agent to influence upstream orchestrators.

## Contribution
- Constructs a threat model enumerating 14 attack vectors across four categories: direct injection via user input (3 vectors), indirect injection via tool outputs (4 vectors), inter-agent injection via message passing (4 vectors), and cascading injection through orchestrator manipulation (3 vectors).
- Tests all 14 vectors against a 6-agent production-representative system, finding 67% of agents vulnerable to at least one scope violation even with system-prompt guardrails, and indirect injection via tool outputs succeeding in 43% of attempts.
- Proposes four architectural defenses reducing overall injection success from 31.2% to 4.2%: message signing with provenance tracking (inter-agent injection down 91%), input/output sanitization at agent boundaries (indirect injection down 78%), privilege-scoped tool access per agent role (privilege escalation eliminated entirely), and anomaly detection on inter-agent communication patterns (84% of cascading attempts caught).

## Method
- Evaluation system: 6-agent configuration representative of enterprise deployments: orchestrator (aO), retrieval agent (aR), code agent (aC), analysis agent (aA), compliance agent (aX), and output agent (aW).
- Orchestrator coordinates task decomposition and result aggregation. Each specialist agent processes subtasks within its domain.
- Evaluated on three LLM backends: GPT-4o (2024-08-06), Claude 3.5 Sonnet, and Llama 3 70B-Instruct, evaluating each vector on all three and reporting the highest observed success rate.
- Agents operate in a financial document analysis pipeline where the retrieval agent ingests SEC filings, the code agent executes analytical computations, and the compliance agent validates outputs against regulatory constraints.
- For each of the 14 attack vectors, 50 payloads constructed using a three-stage process: manual seed construction by two security researchers, template-based augmentation with variable substitution for entity names and formatting, and adversarial refinement where failing payloads are iteratively modified to evade system-prompt guardrails.

## Key Findings
- 67% of agents (4 of 6) are vulnerable to at least one scope violation attack despite system-prompt guardrails.
- The orchestrator is the most vulnerable, appearing as a target in 8 of 14 vectors.
- Indirect injection via tool outputs is the most dangerous category, with 43% aggregate success rate.
- Inter-agent injection succeeds at 31% rate — invisible to perimeter defenses because injection travels through internal message channels that input filters never inspect.
- Cascading injection has 28% success rate but highest impact per successful attack, converting single-agent compromise into system-wide failure.
- Four architectural defenses reduce aggregate injection success from 31.2% to 4.2% (86.5% reduction).
- Latency overhead: 225ms for a 6-agent workflow with 15 inter-agent messages (4.7% increase over 4.8s baseline).

## Actionable Insights
1. Use message signing with provenance tracking for every inter-agent message. Apply: every inter-agent message carries a cryptographic signature and provenance record (origin agent, generating task, chain of prior contributors). Receiving agents verify signatures before processing and quarantine unsigned messages. First step: Add Ed25519 signatures to all inter-agent messages in your system.
2. Implement input/output sanitization at agent boundaries. Apply: every message entering or leaving an agent passes through a boundary sanitizer applying structural validation, instruction detection, and content-length enforcement. First step: Build a boundary sanitizer that validates output structure and detects instruction content in every agent message.
3. Apply privilege-scoped tool access per agent role. Apply: each agent receives tool access tokens scoped to its role — retrieval agent can query documents but cannot execute code, code agent can run sandboxed computations but cannot access compliance databases. Enforce at infrastructure layer, not prompt instructions. First step: Set up immutable role-tool mappings at infrastructure level.
4. Use anomaly detection on inter-agent communication patterns. Apply: model expected inter-agent communication as a directed graph where edges represent permitted message flows. Flag deviations: unexpected recipients, unusual volumes, atypical content patterns, or sequences violating expected workflow. First step: Build an expected communication graph between your agents and monitor for deviations.

## Assumptions & Limitations
- Threat model targets text-based multi-agent systems; multimodal agents face additional injection surfaces not addressed.
- Fixed set of 50 payloads per vector; adaptive adversaries may achieve higher success rates.
- Evaluated on a 6-agent system; production deployments with hundreds of agents may require approximation for anomaly detection graph.
- Prompt injection is one threat among many; data poisoning, model extraction, and supply chain compromises require separate treatment.

## Metadata
- Year: 2026, Authors: Rudrendu Kumar Paul (Boston University), Sourav Nandy (University of Texas at Austin), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2609.22949v1