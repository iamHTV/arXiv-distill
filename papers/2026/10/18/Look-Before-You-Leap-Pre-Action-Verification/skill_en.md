# Skill: Pre-Action Verification Gate for LLM Agents (shell + code edit)
Source: 2609.11957v1 (Look Before You Leap)
Type: framework (oversight guard)

## When to use this skill
- The agent executes shell commands or applies code edits to real files, and one silent failure (an action that appears to succeed but hits the wrong target) can invalidate the entire downstream trajectory.
- You need a model-agnostic guard costing ~ms with no model call — wrapping an existing agent (even a closed frontier model).
- Do NOT use when: the action has no checkable surface (raw byte offset, opaque handle — change the interface instead of guarding); you need semantic correctness judged (edit in the right place but logically wrong — that needs tests/reviewers separately).

## Inputs required
- The action text (command string or edit spec) + the local environment (installed tools via PATH, current file content).
- For commands: a pre-extracted per-tool flag set (from --help, -h, man), cached once (cold cost p95 2.85 s per tool).
- For edits: the anchor content + Robust-Apply params (Kmin, τhi, δ), suggested (2, 0.90, 0.20).
- A deployment decision: safety floor (how many warns/refusals are acceptable) and whether a downstream check (tests/review) exists.

## Steps
1. Classify the representation: content-anchored (search/replace, unified diff) vs location-anchored (line range, function name). Prefer content-anchored; if the agent emits location-anchored, convert it or mark it ungroundable.
2. Run the oracle-exact core (blocking, 0% false positive): commands → bash -n + which (subcommand-aware); edits → exact then whitespace-normalized match, apply immediately if unique.
3. Run abstaining soft checks (warn, never block): flag validity (membership in the extracted flag set — abstain if the tool yields no flags or the token is single-dash multi-character); fuzzy match accepted only when s1 ≥ τhi AND s1 − s2 ≥ δ.
4. Two-tier gate: oracle-exact failure → BLOCK with a recoverable signal so the agent can retry; soft-check suspicion → WARN without blocking (7.0% warn-rate on valid commands in the shell study).
5. Apply edits through Robust-Apply: anchor smaller than Kmin → clean-fail; unique exact/wsnorm match → apply; fuzzy meeting floor + margin → commit through real patch; otherwise → REFUSE (clean-fail, never guess).
6. Return structured signals on refuse/warn: the suspected flag, or the ambiguous match plus its runner-up — the agent can act on them, not a bare rejection.
7. Measure the silent rate by the taxonomy — success / clean failure / silent failure among admitted actions — using the single silent-rate scalar as the safety axis and applicability as the other axis.

## Expected output
- Command gate: recall 0.958 @ FPR 0.070 (selective grounding); oracle-exact core recall 0.500 @ 0% FP; median 2.55 ms per command (warm).
- Edit gate: silent misapplication 0.01% (1/8,320) across every format and perturbation, preserving 60% of fuzzy's applies; applicability 0.51 vs 0.98 on perturbed single-hunk edits.

## Example application
- A coding agent wants to edit config.py: instead of emitting "replace lines 40–52" (location-anchored — corrupts 99.1% of files if the file shifted one line), it emits a search/replace block; the gate runs an exact match → unique → applies. If the anchor matches two places (ambiguous), the gate refuses and the agent receives "2 candidates: line 40 vs line 88" and re-chooses.

## Gotchas
- Never combine aggressive fuzzy matching with NO downstream check — silent corruption accumulates unobserved (fuzzy multi-hunk silent rate 39.3%).
- bash -n rejects incomplete fragments, which misses aliases/shell functions/session-updated PATH — treat these cases as abstentions, not blocks.
- The flag check is only as good as extraction coverage (91.1% of tools); the remaining ~9% are always abstained (unguarded) — they need per-tool completion specs.
- The guard checks realizability, not semantics: a valid command with a harmful effect, or an edit in the right place with wrong logic, is outside the guard — use tests/reviewers.
- Silent failures do NOT trigger rollback (rollback fires only on observed errors) — defense in depth: pre-action guard + differential testing + second-model reviewer.
