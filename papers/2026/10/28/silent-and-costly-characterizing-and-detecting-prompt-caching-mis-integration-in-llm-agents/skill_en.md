# Skill: cachelint-prompt-caching-misintegration-detection
Source: 2610.34817v1
Type: evaluation-method

## When to use this skill
- Need to detect prompt-caching mis-integration in LLM agent codebases (violations of provider requirements for enabling, configuring, or accounting for prompt caching).
- Want to find unguarded cache invocation sites before they silently increase API costs.
- Want to map root causes to their most common fixing strategies for fast remediation.

## When NOT to use this skill
- Provider enables caching automatically on the model side and the application configures no cache markers (implicit caching is out of scope).
- Want to detect defects requiring reasoning across multiple calls or turns (cross-turn mutation, prefix reassembly) — out of scope for single-site model.

## Required inputs
- Source code of the agent application (Python, JavaScript/TypeScript, Ruby, Go, C#).
- List of cache invocation sites: places attaching cache directives (cache_control, cachePoint, ttl, cachedContent, etc.) or reading accounting fields (cached_tokens, cache_read, cache_creation).
- Dated provider-capability oracle: lookup table of cache capability per provider with last_verified date.

## Steps to perform
1. Locate cache invocation sites using CodeQL: extract caching API call sites and surrounding code context.
2. For each site, extract the capability assumption: ⟨site, provider scope, capability, predicate⟩.
3. Discharge CAP condition: diff the code's capability assumption against the dated oracle; if code treats model as capable but oracle does not → BUG or SUSPECTED; if oracle marks model capable but code excludes it → LATENT miss.
4. Discharge STAB or ACCT condition: extract site context and ask the LLM guard check (gpt-5.4-mini) whether a discharging barrier reaches the site (e.g., date truncation or sort_keys canonicalizer).
5. When a check fails, report the site, verdict, and suggested fix class from the root-cause-to-fix-strategy map.

## Expected output
- Warnings for each unguarded cache invocation site.
- Site type, root cause, suggested fix strategy.
- Precision and recall on labeled dataset.

## Example application
A dev team's agent uses Anthropic cache_control. Code checks `if model.id.startswith("claude")` to decide whether to enable caching. When Anthropic renames a model, the check no longer matches and caching is silently disabled. Apply CACHELINT: CodeQL identifies the cache_control call site; guard check asks whether a capability lookup precedes the site; oracle evaluates whether the new model supports caching. If not → report BUG with suggestion to use `registry.supports_cache(model.id)`.

## Gotchas
- Guard check is not sound: LLM can overlook real guards or posit spurious ones, causing false warnings or missed defects.
- CACHELINT only detects defects at single deterministic program points; cross-turn mutation and prefix reassembly require reasoning across calls/turns and are out of scope.
- Oracle is dated — when providers change caching behavior, update affected entries and re-run CACHELINT.
- Each warning ships with a fix hint from the root-cause-to-fix-strategy map (modal repair).