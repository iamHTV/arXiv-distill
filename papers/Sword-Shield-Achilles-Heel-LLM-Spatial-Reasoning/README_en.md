# [2605.31404v1] The Sword, Shield, and Achilles' Heel: LLMs for Spatial Reasoning in Navigation Planning

## Problem
LLM-based navigation systems commonly construct explicit spatial representations and translate them into textual descriptions. But linguistic structures and contextual features in representations are often treated as neutral engineering decisions — NOT TRUE! They actively shape LLMs' behavior.

## Contribution
1. **Dual-interventional framework**: Disentangles linguistic structures from contextual cues. Representation intervention: varies linguistic format and compression degree. Context intervention: controls cue availability, injects conflicts.
2. **3 metaphors**: Topological info = Shield (sturdy backbone). Linguistic format = Sword (double-edged). Semantic info = Achilles' Heel (fatal weakness).
3. **Engineering guidance**: Preserve topological integrity, calibrate compression to model capacity, ensure semantic correctness.

## Method (core summary)
Dual-interventional framework: (1) Representation intervention: vary linguistic format (text, graph, structured) and compression degree under strict information equivalence — clarify when representations support/inhibit planning; (2) Context intervention: control cue availability (topology, geometry, semantics), inject cue conflicts — reveal preferences and vulnerabilities. Experiments across diverse spatial reasoning tasks and multiple model scales.

## Key Findings
- Topological information = sturdy shield, backbone of robust planning — dominates geometry-based cues
- Linguistic format = double-edged sword: effect depends on model size, task demands, compression level
- Semantic information = fatal Achilles' heel: incorrect semantic cues systematically derail planning
- Pattern consistent across tasks and model scales
- Effective representations: preserve topology, calibrate compression, ensure semantic correctness

## Actionable Insights
1. **Topological integrity is first-class constraint**: When building LLM navigation/reasoning systems, preserve topological structure. Don't simplify connections. Example: when building AI route planner, maintain accurate road connections — topology matters more than geometry details.

2. **Calibrate compression to model capacity**: Smaller models need less compression. Larger models handle higher compression. Example: when deploying navigation AI on edge device (small model), use detailed representation. Cloud (large model) → more compression OK.

3. **Semantic correctness is mandatory**: Incorrect semantic cues derail planning systematically. Treat semantic disambiguation as mandatory, not auxiliary. Example: when building AI logistics planner, ensure "warehouse A" always refers to same location — semantic ambiguity = planning failure.

## Assumptions & Limitations
**Conditions for experiment to work:**
- Controlled synthetic environments with strict information equivalence
- Multiple model scales tested
- Diverse spatial reasoning tasks

**Limitations the paper acknowledges:**
- Focus on controlled synthetic environments — real-world more complex

**Limitations the paper does NOT mention:**
- Synthetic environments may not capture real-world noise
- Specific to spatial reasoning — generalizability unclear
- Model-scale dependency may change with future larger models
- Not tested with multimodal inputs (images + text)

## Metadata
- Year: 2026
- Authors: Xudong Zhang, Jian Yang, et al.
- Category: cs.CL, cs.AI
- PDF: https://arxiv.org/pdf/2605.31404v1
- Citation count: [EXTRACTION FAILED]
