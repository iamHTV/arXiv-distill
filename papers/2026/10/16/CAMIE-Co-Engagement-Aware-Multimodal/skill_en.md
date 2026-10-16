# Skill: co-engagement-multimodal-embedding-ads
Source: 2608.30255v1
Type: workflow

## When to use this skill
- Building product/content recommendation or retrieval systems with both images and text.
- Have data where users interact with multiple items together in one session (co-engagement pairs).
- Want to improve retrieval quality without increasing serving cost.

## When NOT to use
- No user interaction data (only static content).
- Text-only or image-only retrieval, no multimodal need.

## Required input
- Item data with images and text descriptions.
- User interaction history: pairs of items viewed/bought/clicked together in the same session.
- An MLLM/embedding backbone that can be fine-tuned.

## Steps
1. Collect co-engagement pairs: two items users viewed or bought together in the same session.
2. Fine-tune the MLLM/embedding backbone on these pairs using content-derived labels (labels from interaction), not static labels.
3. Build a unified multimodal checkpoint to replace two separate encoders (text-only + image-only).
4. Drop-in replace the old encoders in the running retrieval system.
5. Measure CTR/CVR on an A/B test to confirm effectiveness.

## Expected output
- Increase CVR by +10.832% and CTR by +0.390% over multimodal control (in Snap product).
- Increase CTR by +18.958% and CVR by +13.12% over text-only control.
- Reduce serving cost by merging two encoders into one multimodal checkpoint (~1.1pp R@10, 0.5pp MRR trade-off).

## Example application
Solopreneur running a fashion product recommendation page: collect pairs of products viewed together in the same session (e.g. shirt + pants), fine-tune the embedding model to learn they go together. Replace the two old encoders (one image, one text) with a single multimodal checkpoint. Recommendation becomes more accurate, deployment cost lower.

## Gotchas
- Measurable benefit is mainly in conversion (CVR +10.832%), CTR change not significant (+0.390%) over multimodal control — co-engagement makes items more relevant, not necessarily more clicked.
- Needs sufficient co-engagement pair data; if data is scarce, fine-tuning won't help.
- Backbone spread is 5.8% relative, smaller than the 37.7% relative gain from co-engagement fine-tuning — focus on interaction data, not backbone selection.
