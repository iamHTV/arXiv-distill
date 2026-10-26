# 2609.31422 Active Provenance Gate for Multi-Agent Debate Synthesis

## Problem
- Prior work (PROV, PROV-AGENT) treats multi-agent debate (MAD) logs as passive artifacts for post-hoc inspection, not control mechanisms. Self-refine methods do not enforce hard, verifiable constraints at the synthesis boundary (where debate drafts become the final deliverable).
- Consequence: synthesis models optimized for fluency turn irreconcilable positions into fabricated consensus not grounded in the debate history. Most dangerous in crisis settings, where operators over-trust fluent agreement (automation bias).

## Contribution
- Active Provenance Gate (APG): a Phase-4 layer inserted between debate and publication, transitioning provenance from passive logging to active conditional blocking before publication.
- The only permissible outputs are a synthesis with verifiable provenance, or a Divergence Report listing unresolved claims and the conflicting sources behind the deadlock.

## Method (core summary)
- Testbed: crisis-management committee simulation on the kg_cfr_full corpus with 90 knowledge-annotated trajectories, from the open-source Resilient MAS Framework.
- Assembly: merges the public chat transcript, deduplicated KG/RAG documents, and private traces into a SynthesisState — a closed-world corpus with stable addresses; the Proposer may only compress, expose conflict, and perform logical deduction.
- Heterogeneous Proposer–Validator pair: PROPOSER NODE = Gemini 3 Flash (cheap, consensus-oriented prompting); VALIDATOR NODE = Gemini 3.1 Pro as a strict NLI (natural language inference) engine returning JSON {verdict, provenance_fidelity, unsupported_sentences}.
- PF (Provenance Fidelity) = fraction of sentences with strict NLI entailment support over total sentences. Hard gate PF >= 0.95; on failure, the FALLBACK NODE generates a correction hint and the Proposer retries up to MAX_SYNTHESIS_ITER = 3; exhausted budget forces a hard exit emitting a JSON DIVERGENCE_REPORT with _infer_conflicting_sources.

## Key Findings
- Baseline synthesis: initial PF 0.288 (high conflict) / 0.183 (low conflict) — very high hallucination rates despite perfectly grounded RAG/KG traces.
- Bounded self-healing lifts terminal PF to 0.617 / 0.586 (more than doubles in difficult conditions); divergence rate 75.0% under zero-sum conflict vs 60.0% low-conflict.
- 30-run ablation: symmetric setup (Gemini 3 Flash as both generator and auditor) wrongly validated unsafe compromises 85.6% of the time; asymmetric setup (Gemini 3.1 Pro as validator) downgraded identical texts to PF 0.300 and rejected 63.3% of irreconcilable outputs.
- Blind A/B human study (N=33): 66.7% rated the baseline more "fluent and diplomatic"; in scenario S026 (zero-sum stalemate) 75.8% judged the APG output more faithful; 5-point Likert trust: APG M=3.27 SD=1.21 vs baseline M=2.45 SD=0.90, paired t-test t(32)=3.12, p=0.0039. Recovered sessions retain 97.3% text length.

## Actionable Insights
1. Never let the same model write and audit its own synthesis — symmetric setups fail 85.6% of the time. Example: an agent drafting a summary email from 5 sources should have a stronger model (or a distinct system prompt) audit each sentence before sending.
2. Replace soft prompting with a programmatic gate: a hard PF >= 0.95 rule plus an explicit divergence report is trusted by 75.8% of users over fluent fabrication. Example: a customer-service messaging dashboard shows "insufficient data" plus the two conflicting sources instead of a smooth made-up message.
3. Retry budget = 3, then stop: sessions failing after 2 hints enter oscillatory loops and further retries only burn compute. Example: cap agent self-repair at 3 attempts, then flag "human review needed".

## Assumptions & Limitations
- Conditions: a closed corpus with stable addresses; validator must be more capable than the proposer; zero-shot NLI auditing available.
- Acknowledged: synthetic simulations with hard-coded shocks; closed-world (corpus, not external reality); N=33 convenience sample (STEM students) without expert/crowd split; zero-shot NLI auditing prone to linguistic and verbosity bias and prompt sensitivity; metric circularity because the auditor is an LLM.
- Not stated but visible: the gate blocks 60-75% of outputs under conflict, an operational availability cost; ablation uses only Gemini models; the human study lacks real domain experts under time pressure.

## Metadata
- Year: 2026 (25 Sep 2026), authors: Jakub Masłowski, Jarosław A. Chudziak (Warsaw University of Technology), category: cs.MA, accepted at ICTAI 2026, PDF: https://arxiv.org/pdf/2609.31422v1, citation count: no data (very recent; Semantic Scholar API rate-limited)
