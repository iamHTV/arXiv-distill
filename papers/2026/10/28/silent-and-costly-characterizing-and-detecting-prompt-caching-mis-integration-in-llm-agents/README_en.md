# 2610.34817v1 Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents

## Core Value (1 sentence)
Prompt-caching mis-integration in LLM agents usually fails silently — 90% of defects cause no runtime errors but only increase API cost and latency, and CACHELINT (static analysis tool) can detect them with 0.86 precision on real-world projects.

## Problem
Prior work studied prompt defects and prompt caching performance, but overlooked the integration issues of prompt caching from the application side. When applications do not integrate correctly with provider-specific caching APIs (Anthropic, Amazon Bedrock, OpenAI, Gemini...), caching can be silently disabled without any error. The agent still produces correct output but inference cost increases because every call recomputes the full prompt instead of reusing the cached prefix. Test oracles based on crashes or assertions miss most defects because they cannot detect cost degradation.

## Contribution
1. The first empirical study of prompt-caching mis-integration, analyzing 120 prompt-caching-related defects from 10 popular open-source agent systems, characterizing their root causes, symptoms, and fixing strategies.
2. CACHELINT, a static analysis technique for detecting prompt-caching mis-integration. CACHELINT models each mis-integration as a pair of a caching invocation site and the preconditions required for correct cache integration. It locates invocation sites with CodeQL and discharges each precondition against a dated provider-capability oracle or an LLM guard check.
3. CACHELINT achieves 0.71 precision and 0.78 recall on 120 labeled mis-integrations across 10 studied agent systems. On 571 real-world agent projects, CACHELINT identifies 32 mis-integrations with 0.86 precision. These findings received 21 developer confirmations and led to 18 upstream fixes, including one in Anthropic's official SDK.

## Method
The CACHELINT pipeline has these main steps:
1. Prompt-caching integration modeling: each mis-integration pattern is modeled as a pair P = ⟨m, j⟩, where m is a caching invocation site (a program point that sends content to, or reads an accounting field from, the cache) and j is a conjunction of preconditions from three families: prefix stability (STAB), provider capability (CAP), and accounting safety (ACCT).
2. LOCATE invocation sites: CACHELINT uses CodeQL to identify caching API invocation sites and extract their surrounding code context.
3. Discharge preconditions: for CAP conjuncts, diff the code's capability assumption against a dated provider-capability oracle; for STAB or ACCT conjuncts, extract invocation-site context and ask an LLM (gpt-5.4-mini) whether a discharging barrier reaches the site (e.g., date truncation or sort_keys canonicalizer).
4. When a precondition check fails, report the invocation site with the verdict and a suggested fix class from the root-cause-to-fix-strategy map.

## KNOWLEDGE — Data & Concepts
- Prompt caching: an optimization that reduces LLM inference cost and latency by reusing computation of previously processed prompt prefixes.
- Prompt-caching mis-integration: application code that violates provider requirements for enabling, configuring, or accounting for prompt caching.
- 10 studied agent systems: OpenClaw, Hermes-Agent, AutoGPT, OpenCode, LobeHub, OpenHands, Cline, Goose, Aider, Nanobot.
- 120 prompt-caching defects from 148,947 merged PRs.
- 97 defects (81%) on request side, 23 (19%) on read side.
- 108/120 defects (90%) fail silently: no exception, no failed assertion, no crash, model output correct while only caching degrades.
- 86/108 (72%) are silent waste: cache stops hitting, run continues unchanged, only trace is extra spend or added latency.
- 22/108 (18%) produce wrong telemetry: caching works but cache-token counts are parsed/summed/displayed incorrectly.
- 12/120 (10%) crash, concentrated in incompatible markers (8/12).
- 8 root causes: provider compatibility (model-name gating 37, incompatible marker 10), prefix stability (prefix reassembly 15, volatile value 13, nondeterministic serialization 10, misplaced marker 3), cross-turn mutation (9), usage miscount (23).
- 6 fixing strategies: capability lookup (22), marker guard (22), prefix canonicalization (15), usage-counter fix (23), cache-boundary fix (23), lifecycle guard (15).
- CACHELINT: precision 0.71, recall 0.78 on 120 labeled defects; precision 0.86 on 571 real repos; found 32 new mis-integrations; 21 maintainer confirmations, 18 fixes.

## INSIGHT — Mechanism & Why
- [Silent mis-integration] occurs because a cache miss does not cause a runtime error — the model just recomputes the prefix and returns correct output, so no exception or assertion is triggered. The only signal is increased API cost or latency, visible only on usage meters. This means crash-based test oracles miss 90% of defects.
- [Heterogeneous provider APIs increase risk] occurs because providers have different opt-in settings, cache entry limits, and cache lifetimes (e.g., Anthropic requires opt-in and limits cache entries; Bedrock has 1-hour TTL tied to specific models; OpenAI and Gemini apply caching automatically). This means changing models or upgrading providers can silently disable caching without any code change.
- [Fixes are simple and patterned] occurs because 68% of fixes are small, static, local edits that recur across projects as reusable templates. Mapping each root cause to its most common fixing strategy correctly predicts 95/120 (79%) of fixes. This means diagnosis is the hard part; the fix itself is easy.

## IDEA — Actionable Applications
1. Apply CACHELINT to your company's agent codebase: run static analysis to identify unguarded cache invocation sites and report precondition violations. First step: integrate CACHELINT into your CI pipeline to check every commit for unguarded cache calls.
2. Replace model-name gating with capability lookup: instead of hardcoded model name checks to decide whether to enable caching, look up cache capability from a provider-capability matrix updated regularly. First step: change `if model.id.startswith("claude")` to `if registry.supports_cache(model.id)`.
3. Move per-request volatile values (timestamp, UUID) out of the cached span: put the timestamp in the user message instead of the system prompt, or coarsen the timestamp to day granularity with `.date().isoformat()`. First step: find `datetime.now().isoformat()` calls in system prompts and move them outside the cached prefix string.

## WISDOM — General Principle
- Principle: Silent cache misses are the most expensive errors because they don't crash — they just inflate the API bill. Monitor cache-hit rate as a primary metric, not just runtime errors.
- When to use: When deploying LLM agents using prompt caching to reduce inference cost.
- When NOT to use: When the provider enables caching automatically on the model side and the application configures no cache markers (implicit caching is outside CACHELINT's scope).

## Assumptions & Limitations
- Required condition: Each cache invocation site must be a single statically inspectable program point; multi-snapshot causes (cross-turn mutation, prefix reassembly) are outside CACHELINT's single-site model.
- Paper-acknowledged limitations: CACHELINT covers 96/120 (80%) of defects in the dataset; multi-snapshot defects are out of scope; recall on 571 repos is not measured because total defect count is unknown; results reflect the 2026-05-10 capability snapshot.
- Limitations the paper does NOT state: Does not address implicit caching when the provider enables caching automatically on the model side — request-side defects are only observable through responses (e.g., consistently zero cached tokens).

## Metadata
- Year: 2026
- Authors: Ying Zhang, Ruoqi Guo, Yi Liu, Gelei Deng, Yuekang Li, Yepang Liu, Leo Zhang
- arXiv category: cs.SE
- PDF link: https://arxiv.org/pdf/2610.34817v1
- Classification: [applied]