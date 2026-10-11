# Skill: AI Brand Persona Audit
Source: 2605.30207v1
Type: evaluation-method

## When to use this skill
- When auditing brand visibility on AI chatbots and assistants
- When wanting to know if brand appears in AI recommendations
- When designing AI brand perception measurement protocol

## When NOT to use
- Only need to test 1 simple prompt (no persona variation needed)
- No access to multiple AI models
- Product is not consumer-facing

## Required inputs
- List of brands to audit (including competitors)
- List of buyer personas (minimum 5, recommended 10)
- Commercial prompts related to product (minimum 4)
- Access to AI models (OpenAI, Anthropic, or others)
- Rerun capability: N=10 per cell

## Steps

### Step 1 — Define Buyer Personas
1. Create 5-10 personas representing buyer segments:
   - Solo founder
   - Enterprise VP
   - SMB owner
   - Budget-conscious buyer
   - Feature-focused buyer
   - Geographic variants (US, UK, EU, APAC)
2. Each persona: 2-3 sentences describing context, role, priorities

### Step 2 — Design Prompts
1. Create 4-8 commercial prompts:
   - "best [category] software"
   - "top [category] for [use case]"
   - "[category] comparison"
   - "recommend [category] for [persona need]"
2. Prompts must be generic enough for persona variation to have effect

### Step 3 — Run Audit
1. For each (persona × prompt × model) combination:
   - Prefix user message with persona description
   - Run N=10 reruns
   - Record all brand mentions in response
2. Test on multiple models (OpenAI, Anthropic, others)
3. Control: run same prompts WITHOUT persona prefix (baseline)

### Step 4 — Extract Brand Mentions
1. Use 2 LLM judges (different) to extract brand mentions
2. Intersection classification: count brand only when BOTH judges agree
3. Consensus recommendation set = union of brands across N reruns
4. Track: brand name, frequency, context of mention

### Step 5 — Compute Persona Effect
1. Within-persona Jaccard: similarity between recommendation sets of same persona across reruns
2. Cross-persona Jaccard: similarity between recommendation sets of different personas
3. Persona-shift effect Δ = cross-persona Jaccard - within-persona Jaccard
4. Stratify by brand prominence: L1 (leader), L3 (mid-market), L5 (niche)

### Step 6 — Analyze & Act
1. If Δ < -0.10 → persona conditioning is substantial
2. Identify persona-sensitive brands vs persona-resistant brands
3. Design segment-targeted content for persona-sensitive brands
4. Re-run audit periodically to track temporal drift

## Expected output
- Brand visibility score per persona segment
- Persona-shift effect size (Δ)
- List of persona-sensitive vs persona-resistant brands
- Actionable content strategy recommendations

## Example application
**Scenario**: CRM company wants to audit brand visibility on AI chatbots. Brands: Salesforce (L1 leader), HubSpot (L1), Freshworks (L3 mid-market), Pipedrive (L3 mid-market).

**Application**:
1. Personas: startup founder, enterprise VP, UK SMB owner, budget-conscious, feature-focused
2. Prompts: "best CRM software", "top CRM for small business", "CRM comparison"
3. Run 10 reruns per (persona × prompt × model) on OpenAI + Anthropic
4. Results: Salesforce 80% consistency across personas (persona-resistant). Freshworks 25% consistency, 75% swap (persona-sensitive)
5. Action: Freshworks creates segment-targeted pages: "Best CRM for Startups", "Best CRM for Enterprise" instead of 1 generic page

## Gotchas
1. **Jaccard metric limitation**: Only measures set similarity, doesn't capture ranking order. Brand #1 vs Brand #5 have same Jaccard contribution
2. **Temporal drift**: Persona effects may change over time as models update → re-run quarterly
3. **Non-English personas**: Audit is English-only → global brands need additional non-English persona testing
4. **Retrieval vs priors**: Models using more retrieval → smaller persona effect. Check model architecture when interpreting results
5. **Sample size**: N=10 reruns minimum. N=30+ for tighter confidence intervals
6. **Judge agreement**: If 2 judges disagree often (>30%) → low extraction quality, need to refine prompts
