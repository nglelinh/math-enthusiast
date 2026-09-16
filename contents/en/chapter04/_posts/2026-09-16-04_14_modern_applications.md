---
layout: post
title: "Modern Applications: Beauty That Ships"
chapter: '04'
order: 14
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
lesson_type: optional
---

## Learning objectives

After this optional note you should be able to connect three “beautiful” objects already in this chapter—aperiodic order, dynamical generation, and emergence—to 2022–2026 computer-science artifacts, without treating the page as a second [Six Math Essentials]({{ site.baseurl }}/contents/en/chapter04/04_01_Six_Math_Essentials/) hub and without retelling Tao’s Big Think pillars.

## Prerequisites

The required beauty sequence, especially [tilings]({{ site.baseurl }}/contents/en/chapter04/04_10_Tilings/), [chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/) / dynamics, and [emergence]({{ site.baseurl }}/contents/en/chapter04/04_12_Emergence/). The Tao hub remains the map; this page is a side door into recent applications.

## Introduction

Chapter 4 was written as a permission slip to enjoy shocks: infinity has sizes; a tile set can force non-periodicity; a deterministic flow can look random; a crowd can do what no individual does. Those shocks now have repositories. The 2023 hat monotile was found with SAT-flavored computation. Score-based generative models are dynamical systems trained at industrial scale. “Emergent abilities” of language models became a 2022 slogan and a 2023 measurement dispute. None of that rewrites the six pillars.

## Conceptual development

An aperiodic monotile is a single prototile that admits tilings of the plane but no periodic tiling. Diffusion generative models learn to reverse a noising process $$x_0\mapsto x_t$$, often by estimating a score $$\nabla_x \log p_t(x)$$. Emergence, in the Wei et al. (2022) usage, is a capability that is absent at small scale and present at large scale on a chosen metric. Schaeffer, Miranda, and Koyejo (2023) reply that some apparent jumps are artifacts of discontinuous metrics. Beauty becomes applied when these definitions hit software.

## Three complementary landings

### 1. The hat monotile and SAT-assisted tiling

Smith, Myers, Kaplan, and Goodman-Strauss (2023/2024) exhibit the “hat,” a polykite that tiles the plane aperiodically, with a continuum of related polygons and a computer-assisted combinatorial argument. Kaplan’s earlier SAT machinery for Heesch numbers was part of the discovery path. This is Chapter 4’s tiling essay made suddenly concrete, and it is a CS story: exhaustive search and SAT encodings as research instruments, not as a new Tao pillar.

### 2. Diffusion as trained dynamics

Karras, Aittala, Aila, and Laine (2022) separate the design choices of score-based generators—preconditioning, noise schedules, samplers—and obtain strong FID numbers with tens of network evaluations. The object is a stochastic dynamical system whose vector field is learned. That is the chaos/dynamics habit of this chapter, now a production image model (and, later, a piece of AlphaFold 3’s assembly stage). It is not a replacement for the logistic-map studio.

### 3. Emergence, with a metric warning

Wei et al. (2022) catalog tasks on which large language models appear to jump from near-chance to useful accuracy. Schaeffer et al. (2023) show that switching to smoother metrics can turn many of those cliffs into slopes. Chapter 4’s emergence lecture already warned that collective behavior needs a definition. The 2022–2023 pair is the same warning in ML clothes: name the metric before you name a phase transition.

## Interpretation and insight

A hat tiling on a laptop wallpaper is not a classification of all aperiodic monotiles. A pretty FID is not a proof that the reverse SDE is the data-generating process. A discontinuous accuracy cliff is not automatically a new law of nature. Keep the beautiful definition and the shipping artifact in separate hands.

## Limitations and extensions

This page does not re-list numbers, algebra, geometry, probability, analysis, and dynamics. If you want that grammar, return to [Six Math Essentials]({{ site.baseurl }}/contents/en/chapter04/04_01_Six_Math_Essentials/). Fractals, impossible figures, and minimal surfaces are left to their own essays.

## Exercises

1. Why did a SAT encoding help *before* the hat was known to tile, and why is that still not a substitute for the aperiodicity proof?
2. In the EDM sampler, which object is closest to a vector field from the chaos lecture?
3. Take a task scored by exact-match accuracy. Following Schaeffer et al., propose one smoother metric and say what “emergence” would look like on it.
4. Write one sentence that could appear on this page and one that belongs only on the Tao hub.

## References

- Smith, D., Myers, J. S., Kaplan, C. S., & Goodman-Strauss, C. (2024). An aperiodic monotile. *Combinatorial Theory*, 4(1). [arXiv:2303.10798](https://arxiv.org/abs/2303.10798).
- Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. *NeurIPS*. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364).
- Wei, J., et al. (2022). Emergent abilities of large language models. *TMLR*. [arXiv:2206.07682](https://arxiv.org/abs/2206.07682).
- Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *NeurIPS*. [arXiv:2304.15004](https://arxiv.org/abs/2304.15004).
- Kaplan’s hat page: [cs.uwaterloo.ca/~csk/hat](https://cs.uwaterloo.ca/~csk/hat/).
