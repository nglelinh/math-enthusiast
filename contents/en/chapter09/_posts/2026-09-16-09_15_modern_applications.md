---
layout: post
title: "Modern Applications: Turing Themes, 2022–2026"
chapter: '09'
order: 15
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
lesson_type: optional
---

If a computer scientist from 2018—the very year the deep-learning trio won the Turing Award—stepped into a 2025 research lab, three parallel scenes would stop them in their tracks. In the first room, engineers are no longer blindly inflating parameter counts; they are carefully splitting a fixed compute budget (FLOPs) between model size and training tokens under **Chinchilla scaling**. In the second room, a reinforcement-learning agent called **AlphaProof** is writing formal proofs for International Mathematical Olympiad (IMO) problems in **Lean**, with every single step audited by a tiny logical kernel that never tolerates hallucination. In the third room, a **Transformer** isn't merely predicting the next word—it is estimating *counterfactual* patient outcomes across hospital days, bringing Judea Pearl's causal machinery into deep longitudinal sequences!

This optional **2022–2026 field report** sits right beside the [modern themes]({{ site.baseurl }}/contents/en/chapter09/09_14_Modern_Themes/) compass: rather than repeating differential privacy, coding theory, or quantum algorithms, it zooms in on those three fresh intersections of optimization, formal verification, and causal inference.

## Learning objectives

After this optional update you should be able to add three concrete 2022–2026 artifacts—compute-optimal training, Lean-based olympiad agents, and causal sequence models—to the [modern themes]({{ site.baseurl }}/contents/en/chapter09/09_14_Modern_Themes/) compass, distinguish *empirical scaling regularities* from *kernel-checked formal proofs* and *causal-approximation architectures*, and link all three back to Chapter 9's Turing foundations.

## Key ideas: Compute-Optimal Scaling, Formal AI Proofs, and Sequential Causal ML

These three 2022–2026 milestones crystallize three of the sharpest math–CS questions of the decade:

1. **Constrained Optimization Under a Compute Budget (Compute-Optimal Scaling):** training an $$N$$-parameter language model on $$D$$ tokens costs roughly $$C \approx 6ND$$ floating-point operations (FLOPs). Hoffmann et al. (2022) solved a constrained optimization problem: *for a fixed GPU budget $$C$$, which pair $$(N, D)$$ minimizes validation loss?* Empirically, $$N$$ and $$D$$ should scale in balance (roughly **20 tokens per parameter**—which is why 70B-parameter Chinchilla trained on 1.4T tokens handily outperformed 280B-parameter Gopher trained on far fewer tokens!).
2. **Reinforcement Learning Inside a Formal Proof Kernel:** natural-language math from LLMs is notoriously hard to verify automatically. Moving into a proof assistant like **Lean 4** turns each proof step (*tactic*) into a move in a formal game where a small, trusted **kernel** returns an exact True/False verdict. AlphaProof exploits this hallucination-free reward signal to achieve silver-medal IMO 2024 performance.
3. **Sequential Causal Inference on Longitudinal Data:** in intensive care (ICU) records, drug dose $$A_t$$ at hour $$t$$ depends on patient vitals $$X_t$$ and earlier doses—creating **time-varying confounding**. **Causal Transformers** pair self-attention with adversarial balancing losses so latent representations stop encoding treatment assignment, enabling counterfactual estimates (*"what if we switched regimens at hour 3?"*).

## Prerequisites

[Modern themes]({{ site.baseurl }}/contents/en/chapter09/09_14_Modern_Themes/), plus the prize essays you already use as doors: [deep learning trio]({{ site.baseurl }}/contents/en/chapter09/09_12_Deep_Learning_Trio/), [Pearl]({{ site.baseurl }}/contents/en/chapter09/09_11_Pearl_Causality/), [Valiant]({{ site.baseurl }}/contents/en/chapter09/09_09_Valiant_Learning/).

## Conceptual development

Hoffmann et al. (2022) treat FLOPs as a budget split between parameters $$N$$ and tokens $$D$$. AlphaProof treats a Lean tactic search as an RL environment whose reward is a kernel check. A causal transformer treats a trajectory $$(X_t,A_t,Y_t)$$ as a sequence and tries to estimate counterfactual outcomes under alternative action sequences—the Pearl slogan “intervention $$\neq$$ conditioning,” now an architecture.

### Worked Example (Step by Step): Splitting a FLOPs Budget via Chinchilla and Checking a $$3\times 3$$ Causal Mask

Run two brief hand calculations to see how 2022–2026 headlines reduce to elementary algebra and constrained optimization:

**Part A — Splitting a fixed GPU budget $$C = 6 \times 10^{23}$$ FLOPs.** Using $$C \approx 6ND$$, a fixed budget locks the product $$N \cdot D = 10^{23}$$. Compare two allocations on the exact same GPU bill:
- **Strategy A (Gopher-style, parameter-heavy):** pick $$N_A = 280 \times 10^9$$ parameters (280B). Remaining token budget is only $$D_A = \dfrac{10^{23}}{2.8 \times 10^{11}} \approx \mathbf{357 \times 10^9}$$ tokens—barely $$1.28$$ tokens per parameter (severely undertrained!).
- **Strategy B (Chinchilla-optimal, $$D \approx 20N$$):** substitute $$D = 20N$$ into $$N \cdot D = 10^{23}$$:

$$
20 N_B^2 = 10^{23} \implies N_B = \sqrt{5 \times 10^{21}} \approx \mathbf{70.7 \times 10^9\text{ parameters}} \quad (\approx 70\text{B}),
$$

$$
D_B = 20 N_B \approx \mathbf{1.41 \times 10^{12}\text{ tokens}} \quad (\approx 1.4\text{T tokens}).
$$

For the exact same training cost $$C$$, Strategy B achieves strictly lower validation loss *and* is **4× smaller**, slashing inference cost for end users by 4× as well!

**Part B — A $$3\times 3$$ Causal Attention Mask across 3 hospital days.** Suppose a Causal Transformer tracks a patient across days $$t = 1, 2, 3$$ with raw attention score matrix $$S$$ (row $$i$$ attends to column $$j$$). To prevent day $$t = 2$$ from **ever peeking** at future vitals or outcomes on day $$t = 3$$, we add a lower-triangular mask $$M$$ (putting $$-\infty$$ above the diagonal) before applying row-wise softmax:

$$
S = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 5 \\ 1 & 1 & 1 \end{pmatrix}, \qquad M = \begin{pmatrix} 0 & -\infty & -\infty \\ 0 & 0 & -\infty \\ 0 & 0 & 0 \end{pmatrix} \implies S + M = \begin{pmatrix} 1 & -\infty & -\infty \\ 0 & 0 & -\infty \\ 1 & 1 & 1 \end{pmatrix}.
$$

Evaluate Row 2 (day $$t = 2$$) by hand using $$\mathrm{softmax}(v)_j = \dfrac{e^{v_j}}{\sum_k e^{v_k}}$$: since $$e^{-\infty} = 0$$ and $$e^0 = 1$$, we obtain:

$$
\mathrm{softmax}(0,\; 0,\; -\infty) = \left(\frac{1}{1+1+0},\; \frac{1}{1+1+0},\; \frac{0}{2}\right) = \mathbf{(0.5,\; 0.5,\; 0)}.
$$

Even though the raw future score $$S_{2,3} = 5$$ was huge, the causal mask zeroes out backward time leakage to **0**—leaving the adversarial balancing loss to tackle past confounding from days $$t = 1, 2$$ in the spirit of Pearl's $$do(A_t)$$.

### Explanation: How 2022–2026 Connects Directly Back to Turing Award Foundations

1. **Constrained resource accounting (Knuth & Deep Learning Trio):** Chinchilla echoes computer science's oldest lesson—every computation has a budget. Modern scaling solves a constrained extremum along the iso-compute hyperbola $$6ND = C$$.
2. **Separating *creative search* from *exact verification* (Cook–Karp & Formal Methods):** in NP, finding a witness is hard while checking it is easy. AlphaProof exploits that exact asymmetry: neural nets freely propose bold steps, while Lean's kernel enforces zero-error mathematical validity.
3. **Embedding causal structure inside deep nets (Pearl & Bengio):** predicting observational sequences is not enough to prescribe clinical interventions. Causal Transformers marry deep representation learning (2018) with back-door debiasing (Pearl 2011).
4. **Keep empirical regularities distinct from theorems:** Chinchilla is an empirical fit (sensitive to data quality and architecture); AlphaProof still needs human formalization of problem statements; Causal Transformers still assume no unmeasured confounders. Knowing each boundary is the mark of genuine literacy.

**Quick check.** If your compute budget grows by **100×** ($$C' = 100C$$), how much do optimal parameters $$N$$ and optimal tokens $$D$$ each grow under Chinchilla's $$N \propto \sqrt{C}, D \propto \sqrt{C}$$ rule? Both scale up by exactly **$$\sqrt{100} = 10\times$$** (since $$10 \times 10 = 100$$).

## Three updates (not a second survey)

### 1. Compute-optimal training beside the optimization theme

Chinchilla’s regularity—scale tokens with parameters—changed how labs spend money. It does not replace Valiant’s PAC definition or the deep-learning trio’s backpropagation story. It *is* the optimization theme’s most visible 2022 artifact: an empirical answer to “what should we iterate on?” when each iteration costs a warehouse of GPUs. Label it regularity, then return to the AI and ML-theory essays for theorems.

### 2. AlphaProof beside the verification theme

The 2024 IMO evaluation and the 2025 *Nature* paper (Hubert et al.) show an agent that proposes Lean proofs and is scored by a kernel. That is the verification slogan made generative: testing found no bug; the kernel accepted a term. The footnotes from Chapter 5 still apply (expert formalization, extra compute, combinatorics unsolved). Chapter 9’s contribution is the *systems* reading: a trusted kernel plus a learned proposer is a new architecture at the math–CS border, not a Turing Award citation.

### 3. Causal Transformers beside Pearl

Melnychuk, Frauen, and Feuerriegel (2022) introduce a Causal Transformer for counterfactual outcomes on longitudinal data (e.g. MIMIC-style treatments). Adversarial losses try to make representations *not* predictive of the current treatment, a deep-learning echo of blocking back-door paths. This does not obsolete do-calculus. It shows what Pearl’s objects look like when the covariates are sequences.

## Interpretation and insight

The modern-themes lecture already warned: deployment pressure creates definitions. Chinchilla created an allocation definition of “enough data.” AlphaProof created a practice definition of “formal enough to score.” Causal transformers created an architectural definition of “balanced representation.” None of those definitions retires DP, polar codes, or Shor.

## Limitations and extensions

Do not skip the survey and read only this page. Privacy, coding, and quantum did not freeze in 2021; they are omitted here because the survey already carries them, and because FIPS 203 is treated in Chapters 3 and 6.

## References

- Hoffmann, J., et al. (2022). Training compute-optimal large language models. *NeurIPS*. [arXiv:2203.15556](https://arxiv.org/abs/2203.15556).
- Google DeepMind. (2024). AI achieves silver-medal standard solving IMO problems. [blog](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/).
- Hubert, T., et al. (2025). Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature*. [doi:10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y).
- Melnychuk, V., Frauen, D., & Feuerriegel, S. (2022). Causal Transformer for estimating counterfactual outcomes. *ICML*. [arXiv:2204.07258](https://arxiv.org/abs/2204.07258).
- Survey: [Modern themes]({{ site.baseurl }}/contents/en/chapter09/09_14_Modern_Themes/).

## Video tham khảo

- **xem trước** — [Chinchilla Explained: Compute-Optimal Massive Language Models](https://www.youtube.com/watch?v=PZXN7jm9IC0) — Edan Meyer, English. Watch for the compute-optimal training tradeoff (Chinchilla): parameters versus tokens. An explainer of the scaling paper, not a primary author lecture.
- [Improving on AlphaProof: IMO 2024 Problem 2 in Lean 4](https://www.youtube.com/watch?v=5IARsdn78xE) — David Renshaw, English. A Lean 4 formalization of an IMO 2024 problem in the AlphaProof style. Use it beside the lesson’s verification theme, not as an official DeepMind talk.
- [Keynote: Judea Pearl - The New Science of Cause and Effect](https://www.youtube.com/watch?v=ZaPV1OSEpHw) — PyData, English. Further depth after the first two, still tied to this lesson: After this optional update you should be able to add three concrete 2022–2026 artifacts—compute-optimal training, Lean-based olympiad agents, and causal sequence models—to the mode…
