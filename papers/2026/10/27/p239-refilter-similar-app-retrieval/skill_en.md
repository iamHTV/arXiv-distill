# Skill: Retrieve-then-Filter — High-Precision Similar-Item Retrieval Pipeline
Source: 2609.25306
Type: workflow (retrieval pipeline)

## When to use this skill
- You need FUNCTIONAL equivalents (functional substitutes — items a user would accept in exchange for another, same user need), not just topically close items: competitor analysis, related-content recommendation, product alternatives, catalog deduplication.
- Embedding-only retrieval precision/F1 is insufficient (paper ceiling ~60% F1) but full-corpus pairwise LLM evaluation is too expensive.
- You want a DYNAMIC output count (0..k) instead of fixed top-k — items with no substitute return an empty list.

## When NOT to use
- Tasks needing pure semantic/topical similarity (tag clouds, topic clustering) — embeddings alone suffice; the LLM filter is extra cost.
- Very small corpora (<100 items) — filter each pair directly with the LLM, no retrieval stage needed.
- No ability to define an annotation guideline for "substitute" — the filter has no ground truth to calibrate few-shot examples against.

## Input needed
- Corpus items with QUALITY TEXT descriptions (first sentence carries the core purpose — BGE-FIRST evidence shows functional cues appear early); screenshots/images NOT needed (multimodal adds noise).
- Text-only LLM-class embedding model (Linq-Embed-Mistral or equivalent); cosine similarity + ANN index (FAISS/ScaNN class).
- Filter LLM (GPT-5 class) able to output verdict + justification; 2-shot examples.
- Annotation guideline for functional similarity (primary user-facing purpose + same user need; secondary-only sharing = NOT a substitute).
- Budget ~$0.04/query + 4.2 s/query (GPT-5 scale) for the filter stage; embedding stage is one-time.

## Steps
1. **Preprocess corpus** (replicate the paper): filter non-English, remove privacy-policy/subscription/contact noise, strip emojis, lowercase, remove HTML, drop items with descriptions <200 chars or popularity <100. → clean corpus (paper: 34,364 seed → 20,635).
2. **Embed + candidate retrieval**: embed the full text of every item (no truncation); cosine similarity target vs corpus; take top-k candidates (k≈45 tested as best balance; precision peaks at k=5 — choose k per your recall needs).
3. **LLM filter 0-shot first**: prompt with the list of k candidates + descriptions, require a "functional substitute YES/NO" verdict + justification per item; do NOT fix the output count.
4. **Error analysis**: manually review ~75 zero-shot false negatives (or 50–100 at your scale) and categorize errors into the paper's five classes — (a) core feature secondary in candidate (28/75), (b) same goal, different implementation method (18/75), (c) candidate fulfills part of core feature (11/75), (d) misidentified core feature (10/75), (e) different purpose, same core feature (8/75).
5. **Pick 2-shot examples** covering recurring categories (a)+(b) first (46/75 = 61% of errors), NOT random picks. Re-run the filter 2-shot (97% precision, 84% recall, ~90% conditional F1 class). Do NOT go 4/6-shot (flat/declining).
6. **Stability**: if the LLM lacks temperature=0 → run 3 times per query and average (paper method).
7. **Evaluate**: precision / conditional recall / pooled recall / F1 (conditional + pooled); pooled recall is a LOWER BOUND (union of top-k across all methods) — state this in reports. Compare against built-in platform "similar items" if available (Wilcoxon signed-rank).
8. **Deploy**: embedding stage one-time offline; filter stage per-query online (~$0.04/query); log the output-count distribution per category → review dynamic density (Personalization/Social/Photography dense; Business/Tools/Sports sparse — paper pattern).

## Expected output
- Per target: a list of 0..k functional substitutes (dynamic count, zero when none exist), each with a justification; aggregate metrics precision ≥90% / CR-F1 ~90% / PR-F1 ~86% on a held-out test set; count-distribution table by category.

## Example application
- Blog with 500 posts: a reader finishes "how to write a CV" → embed all 500, cosine top-45, 2-shot GPT filter ("would a reader of this post accept the other post as a substitute — same user need of CV writing, not generic 'career advice' topic") → returns 12 truly related posts (vs 40 cosine-top posts full of generic career pieces), F1 ~90%; a post "10 pho-cooking secrets" with no substitute returns 0 instead of forced filler.

## Gotchas
- **Define "substitute" first**: without a clear annotation guideline the filter drifts (paper annotation κ=0.79); the guideline must state "primary user-facing purpose" + "same user need"; secondary features do not count.
- **Recall is a lower bound**: pooled-recall denominator = union of top-k across all methods → never claim absolute recall; use conditional recall for filter quality.
- **Multimodal hurts more than helps**: screenshots/permissions/UI layouts conflate descriptive similarity (password manager vs expense tracker share list UIs); text-only wins — skip image-embedding cost.
- **First sentence decides**: BGE-FIRST (first chunk) > BGE-AVG → functional cues live at the START of the text; put the core-purpose sentence first, truncation-friendly.
- **>2-shot examples add nothing**: 4-shot/6-shot flat or slightly declining — 2 examples covering recurring error patterns are the sweet spot; more examples waste context window.
- **Descriptions may be marketing-flawed**: falsified feature claims → the filter over-trusts descriptions; if you have real usage logs, prefer log signals.
- **Dynamic count needs monitoring**: output 0–45/target → UI must handle empty results gracefully; log density by category to know which categories are intrinsically sparse (Business/Tools/Sports).
- **Cost scales linearly**: $0.04/query × query volume — cache filter results for hot targets, filter cold items on-demand.
- **Platform lists ≠ substitutes**: Google Play-style "similar items" mean 93 vs functional 21 (p<0.001) — never use platform lists as ground truth or fallback for substitution tasks.
