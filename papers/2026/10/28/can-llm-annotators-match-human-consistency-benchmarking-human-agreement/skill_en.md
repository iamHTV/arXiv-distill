# Skill: ant-or-contrastive-annotation-framework
Source: 2610.32415v1
Type: optimization-method

## When to use this skill
- Need to evaluate LLM annotation systems by distribution-aware agreement with human judgments (not just matching a single gold label).
- Want to build a multi-agent annotation system that adapts to detailed task guidelines and boundary cases.
- Want to transform annotation successes and failures into reusable structured decision knowledge.

## When NOT to use this skill
- Annotation tasks have clear, unambiguous answers (no need for complex multi-agent systems).
- No professional human annotators available to create reference labels and detailed guidelines.

## Required inputs
- Annotation dataset with detailed task guidelines (annotation guidelines).
- Group of human annotators (e.g., 10 annotators, each sample labeled by 5).
- LLM models as annotators and verifier (temperature = 0.1).
- Storage for correct and incorrect samples (contrastive sample pools).

## Steps to perform
1. Build multi-annotator evaluation benchmark: collect 5 independent human labels per sample; use Fleiss' κ to assess model alignment with human labeling distributions.
2. Implement annotator–verifier architecture: 3 independent annotators produce labels and rationales with separately optimized prompts; 1 verifier compares justifications to determine final label.
3. Perform contrastive knowledge mining: when agent makes wrong prediction (doesn't match at least 2/5 human labels), retrieve two semantically similar correct samples, form contrastive tuple, use LLM to mine discriminative dimension d from confusing cases.
4. Store discriminative dimensions in knowledge base with support count; retain only dimensions with support ≥ 2.
5. Perform Dimension–Sample Coupled Injection: select top-K highest-scoring samples and associated discriminative dimensions; inject both instance-level and rule-level into prompts.
6. Perform Attribution-Guided Optimization: attribute errors to responsible agents; refine prompts using LLMOpt(pa; {(q−, r)}, s+, d).
7. Re-evaluate on current batch; keep updated prompts only if batch-level performance improves; otherwise roll back to previous prompts.
8. Iterate over multiple epochs: evaluation, knowledge-base update, prompt refinement; add verified outcomes to contrastive sample pools.

## Expected output
- Agreement@≥2 accuracy and Fleiss' κ for the annotation system.
- Structured decision knowledge base.
- Optimized prompts for each agent.

## Example application
A company needs to label customer support tickets into categories (billing, technical, general). Detailed annotation guidelines have rules for boundary cases (e.g., tickets with both billing and technical issues should be labeled as billing). Apply ANT-OR: collect 5 human labels per ticket, deploy 3 annotator + 1 verifier, after each wrong prediction mine discriminative dimensions and store in knowledge base. Result: agreement@≥2 accuracy improves by 4.5 points over baseline; Fleiss' κ within 2 points of human inter-annotator agreement.

## Gotchas
- Need 5 independent annotators per sample for distribution-aware evaluation — high cost (USD $4,078 for 7 datasets × 1,500 samples).
- ANT-OR optimization cost is higher than SPO ($101.43 vs $65.94) but achieves better accuracy (+4.7 points).
- Need detailed task guidelines before starting — not applicable to annotation tasks without guidelines.
- Decision knowledge needs proper storage and retrieval for reuse in subsequent optimization rounds.