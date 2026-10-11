# [2605.31484v1] Balanced LoRA: Removing Parameter Invariance to Accelerate Convergence

## Problem
LoRA (Low-Rank Adaptation) is the most widely adopted method for fine-tuning LLMs. But LoRA is inherently overparameterized: multiple pairs of low-rank factors can yield the same adapted weight matrix. Different pairs exhibit significantly different condition numbers, directly impacting convergence rate. Prior work has not addressed this parameter invariance.

## Contribution
1. **Theoretical analysis**: Proves LoRA overparameterization creates varying condition numbers across minimizers. Balanced minimizers achieve optimal conditioning.
2. **BaLoRA (Balanced Low-Rank Adaptation)**: Projects iterates onto balanced manifold → improves conditioning of loss landscape while preserving adapted matrix. Projection step is computationally lightweight.
3. **Empirical validation**: BaLoRA converges faster than standard LoRA, superior performance across fine-tuning tasks on Llama-3.2-3B and Qwen-2.5-3B.

## Method (core summary)
LoRA: W_adapted = W + AB, where A ∈ R^{a×r}, B ∈ R^{r×a}. Problem: many (A,B) pairs give same W_adapted but different condition numbers. BaLoRA: after each optimization step, project (A,B) onto balanced manifold — enforce balanced condition. Projection step: computationally lightweight, integrates seamlessly into existing pipelines. Key: balanced minimizers have optimal conditioning → faster convergence.

## Key Findings
- Synthetic experiments: BaLoRA starts slower, then enters fast convergence regime, significantly outperforms LoRA
- Llama-3.2-3B + Qwen-2.5-3B on 10+ datasets: BaLoRA consistently outperforms standard LoRA
- Largest advantage at high ranks (r=64, 128)
- BaLoRA more stable to high learning rates and initialization scalings
- Negligible computational overhead
- Matches or surpasses state-of-the-art variants (DoRA, OLoRA, LoRA-GA)

## Actionable Insights
1. **Use BaLoRA instead of standard LoRA**: When fine-tuning LLMs, use BaLoRA instead of standard LoRA — negligible overhead but faster convergence. Example: when fine-tuning Llama-3B for specific task, BaLoRA converges faster with same compute budget.

2. **Higher ranks benefit more**: BaLoRA advantage is largest at r=64, 128. If using high-rank LoRA, BaLoRA is particularly useful. Example: when needing high-capacity adaptation, use BaLoRA with r=128 instead of LoRA r=128.

3. **More stable hyperparameter sensitivity**: BaLoRA is more robust to high learning rates and initialization scalings. Less hyperparameter tuning needed. Example: when fine-tuning in production setting with limited tuning budget, BaLoRA is more reliable.

## Assumptions & Limitations
**Conditions for method to work:**
- LoRA overparameterization must exist
- Balanced manifold must be computationally accessible
- Projection step must preserve adapted matrix

**Limitations the paper acknowledges:**
- Synthetic experiments limited scope
- Focus on optimization speed, not final accuracy superiority
- Tested on 3B models — larger models untested

**Limitations the paper does NOT mention:**
- No comparison with full fine-tuning
- No testing on models >3B — scalability unclear
- No interaction with other LoRA variants (QLoRA, etc.)
- Projection step may have numerical stability issues at very high ranks?
- No discussion of when NOT to use BaLoRA

## Metadata
- Year: 2026
- Authors: Valérie Castin, Kimia Nadjahi, Pierre Ablin, Gabriel Peyré
- Category: cs.LG
- PDF: https://arxiv.org/pdf/2605.31484v1
- Citation count: [EXTRACTION FAILED]
