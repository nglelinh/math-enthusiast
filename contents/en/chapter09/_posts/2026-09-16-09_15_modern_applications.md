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

## Learning objectives

After this optional update you should be able to add three concrete 2022–2026 artifacts—compute-optimal training, Lean-based olympiad agents, and causal sequence models—to the [modern themes]({{ site.baseurl }}/contents/en/chapter09/09_14_Modern_Themes/) compass, without rewriting that survey’s slogans on differential privacy, coding theory, or quantum algorithms.

## Prerequisites

[Modern themes]({{ site.baseurl }}/contents/en/chapter09/09_14_Modern_Themes/), plus the prize essays you already use as doors: [deep learning trio]({{ site.baseurl }}/contents/en/chapter09/09_12_Deep_Learning_Trio/), [Pearl]({{ site.baseurl }}/contents/en/chapter09/09_11_Pearl_Causality/), [Valiant]({{ site.baseurl }}/contents/en/chapter09/09_09_Valiant_Learning/).

## Introduction

The modern-themes lecture is a compass: privacy, optimization/ML theory, coding, quantum awareness, verification. This page is a 2022–2026 *field report* on three needles that moved. Scaling laws became an allocation practice. Verification met reinforcement learning in Lean. Causal graphs met transformers on longitudinal data. The prize essays stay doors; these are rooms that opened after the doors were built.

## Conceptual development

Hoffmann et al. (2022) treat FLOPs as a budget split between parameters $$N$$ and tokens $$D$$. AlphaProof treats a Lean tactic search as an RL environment whose reward is a kernel check. A causal transformer treats a trajectory $$(X_t,A_t,Y_t)$$ as a sequence and tries to estimate counterfactual outcomes under alternative action sequences—the Pearl slogan “intervention $$\neq$$ conditioning,” now an architecture.

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

## Exercises

1. Add a sixth row to the modern-themes “walk back through the course” table for *compute-optimal training*. Which chapters does it point to?
2. Why is “kernel accepted” closer to Hoare-style verification than to a unit test, and why is it still relative to a spec?
3. In the Causal Transformer, which Pearl object is the adversarial loss trying to imitate?
4. A slide says “Turing Award ideas peaked in 2018 with deep learning.” Using this page, name two post-2018 math–CS objects that are not just bigger nets.

## References

- Hoffmann, J., et al. (2022). Training compute-optimal large language models. *NeurIPS*. [arXiv:2203.15556](https://arxiv.org/abs/2203.15556).
- Google DeepMind. (2024). AI achieves silver-medal standard solving IMO problems. [blog](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/).
- Hubert, T., et al. (2025). Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature*. [doi:10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y).
- Melnychuk, V., Frauen, D., & Feuerriegel, S. (2022). Causal Transformer for estimating counterfactual outcomes. *ICML*. [arXiv:2204.07258](https://arxiv.org/abs/2204.07258).
- Survey: [Modern themes]({{ site.baseurl }}/contents/en/chapter09/09_14_Modern_Themes/).
