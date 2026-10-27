# Skill: Tool-Trace Shortcut Audit — PT2D + Token-Class Redaction
Source: 2610.25540
Type: evaluation-method (agent shortcut auditing)

## When to use this skill
- You have an agent/LLM pipeline with tool calls or RAG, and want to VERIFY that the model actually reasons from retrieved evidence rather than pattern-matching identifiers or template artifacts inside tool outputs.
- The agent's benchmark accuracy is "too good vs baseline" or an improvement claim needs auditing before you trust or publicize it.
- You must audit a FROZEN model (production checkpoint) that you cannot or do not want to retrain — the diagnostic only needs TF-IDF + logistic regression.

## When NOT to use
- The reason for high accuracy is already explained (manual error analysis + alternative feature attribution) and tool outputs contain zero identifiers/templates.
- Tool outputs are entirely non-text (images/audio) and you don't control the serialization to text — the audit only covers the text portion.
- No labeled audit partition (a few hundred examples) — Stage 1 needs to fit a diagnostic classifier.

## Input needed
- Tool traces: ordered serialized results e(1)..e(T) per example (text form), with labels y ∈ {0,1} (or multi-class — adjust the chance baseline accordingly).
- Labeled audit partitions Dfit/Deval aligned with the evaluation protocol (peptide-disjoint / temporal / user-disjoint splits, NOT shuffled into identifier groups).
- A frozen LLM checkpoint with an identical generation/parsing/scoring pipeline for re-evaluation.
- Domain knowledge to define token classes (identifier types, version strings, file-path components) plus non-overlapping control classes.

## Steps
1. **Record per-tool results**: log EACH tool result separately (by tool index/name), not only the concatenated trace. A fixed tool order aids attribution.
2. **Stage 1 — PT2D**: per scope s ∈ {full, tools 1..T}: TF-IDF features (word 1–2-grams + char 2–5-grams + char 3–5-grams), balanced logistic regression fit on Dfit, AUROC As on Deval. No universal threshold — rank tools by comparing At to Afull, chance, and other tools.
3. **Fingerprint the shortcut type**: word AUROC ≈ chance + char AUROC spike → the signal lives in identifier fragments (NOT language); word spike → lexical/topic leakage. Read top logistic weights → discriminative substrings (e.g., "_21", "_17").
4. **Localize the serialized field**: map substrings to the source field (e.g., ThermoMPNN_inference_<pdb_id>.csv); a quick lookup test (2-digit prefix AUROC 0.6967) confirms strength before redaction.
5. **Define token classes**: group values sharing generating semantics — target the COMPLETE class (an isolated n-gram covers only part); pick ≥1 non-overlapping recurring class as CONTROL (the peptide's role in the paper).
6. **Stage 2 — Redaction**: replace every occurrence of class c in ALL prompt-bearing fields (input + tool outputs + system prompt) with a class-specific placeholder; preserve labels/reference answers; global replacement (prevents duplicates surviving); re-evaluate the FROZEN checkpoint identically → ∆Ac = Aorig − ARc, one class at a time.
7. **Verdict**: LARGE ∆A on the suspect class + STABLE ∆A on the control (≈0) → the model depends on the shortcut (behavioral evidence). Small suspect ∆A → associational pattern only, the model may be robust — still document. Caveat: redaction can remove correlated signals/shift the distribution → conclusions limited to model behavior.
8. **Dilution validation (optional)**: real tool-subset sweep (progressively appending tools → expect monotonic AUROC decay like 0.6365→0.4876) + synthetic label-independent additions (chance by K≈5) → confirms full-trace screening would have missed it.
9. **Remediate**: anonymize/strip the identifier class at the TOOL-SERIALIZATION layer (server-side, before results reach the prompt), regenerate traces, re-run the audit + evaluation; report the honest accuracy (paper analog: post-honest accuracy unknown — must re-measure).

## Expected output
- Audit report: per-tool AUROC table (word/char features), suspect class + serialized-field localization (top substrings), redaction table (∆A suspect vs control), a verdict "evidence-grounded" or "shortcut-dependent", plus a remediation plan and re-measured honest metric.

## Example application
- A support agent with 3 tools (CRM lookup, order DB, FAQ search) claims 85% resolution accuracy on a benchmark: PT2D → the order-DB tool's char-n-gram AUROC 0.66 (order-ID fragments "_INV-21" bind correct, "_INV-17" bind wrong); full-trace 0.51; redacting the order-ID class → 0.52 (∆A = +0.33), redacting a SKU control → 0.84 (∆A = −0.01) → verdict: the agent shortcut-matches order IDs. Remediate: hash order IDs at the tool layer → re-evaluate → 0.79 honest accuracy → publish 0.79, not 0.85.

## Gotchas
- **Never trust full-trace screening alone**: dilution makes carrier tools invisible (full-scope ≈0.48 while the carrier reaches 0.64; monotonic decay; synthetic decoys reproduce it) — per-tool decomposition is mandatory, not optional.
- **A control class is mandatory**: a drop without a stable control proves nothing (it could be an artifact of redaction itself); the control must be a non-overlapping recurring semantic class.
- **Complete class, not a single n-gram**: an isolated fragment covers only part of a shortcut-bearing value — redact the entire identifier format (e.g., all PDB IDs, not just the "_21" prefix).
- **Global replacement**: duplicated identifier values surviving in other fields nullify the intervention; replace across ALL prompt-bearing fields, including system prompt/history.
- **Linear diagnostic**: TF-IDF logistic regression misses non-linear shortcuts — if suspicion is high but AUROC stays flat, try a nonlinear probe (gradient-boosting class) before declaring clean.
- **Serialized forms vary per toolchain**: separators, casing, and prefixes differ, so token-class definition needs domain checks; tool version upgrades may change formats → re-audit.
- **The associational stage**: a positive PT2D does NOT prove the model uses it — Stage 2 is the behavioral proof; the 2-stage procedure is inseparable (PT2D alone only suggests).
- **Multi-class tasks**: the chance baseline differs from 0.5 — compute the appropriate chance floor for ∆A interpretation; imbalanced labels need a stratified/balanced fit (the paper used balanced regression).
- **Serialization-layer artifacts**: the act of serializing tool outputs (CSV headers, filenames) can itself CREATE shortcuts — audit the format design, not just the content.
- **Frozen-checkpoint discipline**: identical generation/parsing/scoring between original and redacted runs — a different pipeline makes ∆A meaningless.
