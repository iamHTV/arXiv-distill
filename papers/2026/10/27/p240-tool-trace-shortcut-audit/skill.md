# Skill: Tool-Trace Shortcut Audit — PT2D + Token-Class Redaction
Source: 2610.25540
Type: evaluation-method (agent shortcut auditing)

## Khi nào dùng skill này
- Bạn có agent/LLM pipeline với tool calls hoặc RAG, và muốn VERIFY rằng model thực sự lý luận từ retrieved evidence — không pattern-match identifiers/template artifacts trong tool outputs.
- Benchmark accuracy agent "quá tốt so với baseline" hoặc improvement claim cần audit trước khi trust/publicize.
- Bạn cần audit model FROZEN (production checkpoint) không thể/ko muốn retrain — diagnostic chỉ cần TF-IDF + logistic regression.

## Khi KHÔNG nên dùng
- Lý do accuracy cao đã được giải thích rõ (manual error analysis + feature attribution khác) và tool outputs chứa zero identifiers/templates.
- Tool outputs hoàn toàn non-text (images/audio) và bạn không control serialization sang text — audit chỉ cover phần text.
- Không có labeled audit partition (vài trăm examples) — Stage 1 cần fit diagnostic classifier.

## Input cần có
- Tool traces: ordered serialized results e(1)..e(T) per example (dạng text), với labels y ∈ {0,1} (hoặc multi-class — chance baseline adjust phù hợp).
- Labeled audit partitions Dfit/Deval aligned với eval protocol (peptide-disjoint/temporal/user-disjoint splits KHÔNG shuffle lẫn vào identifier groups).
- Frozen LLM checkpoint với identical generation/parsing/scoring pipeline để re-evaluate.
- Domain knowledge để define token classes (identifier types, version strings, file-path components) + control classes non-overlapping.

## Các bước thực hiện
1. **Record per-tool results**: log MỖI tool result riêng (theo tool index/name), KHÔNG chỉ concatenated trace. Fixed tool order giúp attribution.
2. **Stage 1 — PT2D**: per scope s ∈ {full, tools 1..T}: TF-IDF features (word 1–2-grams + char 2–5-grams + char 3–5-grams), balanced logistic regression fit trên Dfit, AUROC As trên Deval. KHÔNG có universal threshold — rank tool bằng compare At vs Afull, chance, other tools.
3. **Fingerprint shortcut type**: word AUROC ≈ chance + char AUROC spike → signal trong identifier fragments (KHÔNG phải language); word spike → lexical/topic leakage. Đọc top logistic weights → discriminative substrings (ví dụ "_21", "_17").
4. **Localize serialized field**: map substrings về field gốc (ví dụ ThermoMPNN_inference_<pdb_id>.csv); quick lookup test (2-digit prefix AUROC 0.6967) xác nhận strength trước khi redact.
5. **Define token classes**: group values cùng generating semantics — target COMPLETE class (isolated n-gram chỉ cover phần); chọn ≥1 non-overlapping recurring class làm CONTROL (peptide role trong paper).
6. **Stage 2 — Redaction**: replace mọi occurrence class c trong ALL prompt-bearing fields (input + tool outputs + system prompt) bằng class-specific placeholder; preserve labels/reference answers; global replacement (ngăn duplicates sống sót); re-eval FROZEN checkpoint identically → ∆Ac = Aorig − ARc, 1 class/lần.
7. **Verdict**: ∆A suspect LARGE + ∆A control STABLE (≈0) → model depends on shortcut (behavioral evidence). ∆A suspect small → pattern assocation only, model có thể robust — nhưng document. Caveat: redaction có thể remove correlated signals/shift distribution → conclusion limited to model behavior.
8. **Dilution validation (optional)**: real tool-subset sweep (append tools progressively → expect monotonic AUROC decay 0.6365→0.4876-style) + synthetic label-independent additions (chance by K≈5) → confirms full-trace screening would miss it.
9. **Remediate**: anonymize/strip identifier class tại TOOL-SERIALIZATION layer (server-side, before results reach prompt), regenerate traces, re-run audit + eval; report honest accuracy (paper analog: post-honest accuracy chưa biết — phải re-measure).

## Output mong đợi
- Audit report: per-tool AUROC table (word/char features), suspect class + serialized field localization (top substrings), redaction table (∆A suspect vs control), verdict "evidence-grounded" hoặc "shortcut-dependent", remediation plan + re-measured honest metric.

## Ví dụ áp dụng
- Support agent 3 tools (CRM lookup, order DB, FAQ search) claim 85% resolution accuracy trên benchmark: PT2D → order-DB tool char-n-gram AUROC 0.66 (order-ID fragments "_INV-21" bind correct, "_INV-17" bind wrong); full-trace 0.51; redact order-ID class → 0.52 (∆A = +0.33), redact SKU control → 0.84 (∆A = −0.01) → verdict: agent shortcut-matches order IDs. Remediate: hash order IDs ở tool layer → re-eval → 0.79 honest accuracy → công bố 0.79, không 0.85.

## Gotchas
- **Never trust full-trace screening alone**: dilution makes carrier tools invisible (full-scope ≈0.48 while carrier 0.64; monotonic decay; synthetic decoys reproduce) — per-tool decomposition là mandatory, không optional.
- **Control class mandatory**: drop mà không có stable control = chứng minh nothing (artifact of redaction itself); control phải non-overlapping recurring semantics.
- **Complete class, not single n-gram**: isolated fragment cover chỉ phần shortcut-bearing value — redact entire identifier format (ví dụ toàn bộ PDB-ID, không chỉ prefix "_21").
- **Global replacement**: duplicated identifier values sống sót ở field khác → nullifies intervention; replace trong ALL prompt-bearing fields kể cả system prompt/history.
- **Linear diagnostic**: logistic regression TF-IDF misses non-linear shortcuts — nếu suspicion cao nhưng AUROC flat, thử nonlinear probe (gradient boosting class) trước khi kết luận clean.
- **Serialized forms vary per toolchain**: separators, casing, prefixes differ → token-class definition cần domain check; tool version upgrades có thể đổi format → re-audit.
- **Associational stage**: PT2D positive ≠ model uses it — Stage 2 mới là behavioral proof; quy trình 2 stage là inseparable (PT2D alone chỉ gợi ý).
- **Multi-class tasks**: chance baseline khác 0.5 — compute appropriate chance floor cho ∆A interpretation; imbalanced labels cần stratified/balanced fit (paper dùng balanced regression).
- **Serialization layer artifacts**: chính việc serialize tool output (CSV headers, filenames) có thể CREATE shortcuts — audit cả format design, không chỉ content.
- **Frozen checkpoint discipline**: identical generation/parsing/scoring giữa original và redacted runs — khác pipeline = ∆A meaningless.
