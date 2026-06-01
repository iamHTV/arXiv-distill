# Skill: Privacy-Preserving LLM Recommendations
Source: 2505.00951
Type: workflow

## When to use this skill
- When building LLM-based recommendation systems needing privacy protection
- When user data contains sensitive information (health, finance, personal)
- When deploying recommendations on consumer-grade hardware

## When NOT to use
- No sensitive data in purchase history
- Cloud-only deployment (no local compute)
- Non-LLM recommendation systems

## Required inputs
- User purchase history
- Sensitivity classification model (BERT-based)
- Local LLM for de-obfuscation (Llama 3.2 1B)
- Cloud LLM for main recommendations

## Steps

### Step 1 — Classify Product Sensitivity
1. BERT-based classifier: sensitive vs nonsensitive
2. Health products → sensitive
3. Electronics, clothing → nonsensitive
4. Output: sensitivity labels per product

### Step 2 — Obfuscate Sensitive Data
1. Remove sensitive products from purchase history
2. Keep nonsensitive products only
3. Send modified history to cloud LLM
4. Output: nonsensitive-based recommendations

### Step 3 — Local De-obfuscation
1. Local LLM processes sensitive products
2. Reconstructs sensitive-category recommendations
3. Runs on consumer-grade hardware
4. Output: sensitive-category recommendations

### Step 4 — Merge Recommendations
1. Combine cloud (nonsensitive) + local (sensitive) recommendations
2. Ensure category distribution alignment
3. Output: privacy-preserving recommendations

## Expected output
- Almost same utility as full-data sharing
- Large privacy preservation
- Consumer-grade hardware feasibility
- Better HR@10 than obfuscation-only

## Example application
**Scenario**: E-commerce app wants LLM recommendations without exposing health purchases.

**Application**:
1. Classify: vitamins → sensitive, laptop → nonsensitive
2. Obfuscate: remove vitamins from history sent to cloud
3. Cloud LLM: recommends electronics, clothing based on laptop history
4. Local LLM: recommends vitamin-related products locally
5. Merge: combine both recommendation sets
6. Result: privacy preserved, utility maintained

## Gotchas
1. **Classification errors matter**: False negatives → privacy leakage. False positives → utility loss. Tune classifier carefully
2. **Cumulative patterns not addressed**: Individual products may seem nonsensitive but patterns reveal information. Additional protection needed
3. **Consumer hardware feasible**: Llama 3.2 1B runs locally. No specialized hardware needed
4. **Fixed privacy definition**: Health-based only. Expand to user-specific preferences
5. **Category distribution important**: Don't just match items — match category diversity
6. **Local inference cost**: Mobile devices may have limited compute. Optimize local model
