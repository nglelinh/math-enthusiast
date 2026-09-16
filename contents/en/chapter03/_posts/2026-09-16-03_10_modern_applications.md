---
layout: post
title: "Modern Applications: 2022–2026 Updates"
chapter: '03'
order: 10
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
lesson_type: optional
---

## Learning objectives

After this optional update you should be able to attach one 2022–2026 citation to each of four Chapter 3 migrations—public-key cryptography, graphs, optimization-adjacent scientific ML, and Fourier-flavored PDE surrogates—without rewriting the required mechanism lectures.

## Prerequisites

The required sequence, especially [number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/), [graphs]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/), [optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [Fourier]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/), and [differential equations]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/).

## Introduction

Chapter 3 already told the migration stories: modular arithmetic became a handshake; a graph became a network; a gradient became a training step; a Fourier mode became a JPEG. Those mechanisms did not expire. What changed after 2022 is the *standard and the architecture* sitting on top of them. Lattice KEMs became federal standards. Graph models grew a Transformer branch. PDE solvers grew a learned-operator branch that still speaks Fourier.

## Conceptual development

A key-encapsulation mechanism produces a shared secret $$K$$ from public encapsulation. Classically, $$K$$ is protected by factoring or discrete log. After Shor, the hardness assumption moves. Graph learning, meanwhile, still needs a representation of a vertex $$v$$ that mixes *neighbors* with a *global* token mix. Fourier neural operators implement a learned kernel as a multiplier $$\widehat{K}(k)$$ in frequency space—the same dual picture as the Fourier lecture, now trained rather than designed.

## Four updates

### 1. Post-quantum standards on the crypto migration

On 13 August 2024 NIST published FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), and FIPS 205 (SLH-DSA). ML-KEM is a module-lattice KEM; ML-DSA is a module-lattice signature; SLH-DSA is a stateless hash-based signature. The Chapter 3 RSA/DH story is not false; it is no longer a complete inventory of *approved* public-key primitives. Hybrid deployments (classical + ML-KEM) are the present engineering compromise, not a theorem that RSA is already broken.

### 2. Graph Transformers on the network migration

Rampášek et al. (2022) give a GPS recipe: positional or structural encodings, a local message-passing layer, and a global attention layer with linear $$O(N+E)$$ variants (Performer, BigBird). Molecules, citation graphs, and knowledge graphs are still graphs in the Euler sense of this chapter. What changed is that “GNN versus Transformer” is now a modular product choice rather than a religious war. Max-flow and coloring did not become obsolete; they became features and losses inside larger models.

### 3. Neural operators on the DE migration

Kovachki et al. (2023) learn maps between function spaces and report large speed-ups versus classical solvers on Navier–Stokes-type benchmarks. This sits beside the DE applications lecture, not in place of well-posedness or CFL conditions. A surrogate that is discretization-invariant is still only as honest as its training measure.

### 4. Fourier multipliers as learned kernels

The Fourier neural operator implements layers of the form

$$
\bigl(\mathcal{K}v\bigr)(x)=\mathcal{F}^{-1}\bigl(\widehat{K}\cdot \mathcal{F}v\bigr)(x),
$$

which is the signal-processing identity from the Fourier lecture with $$\widehat{K}$$ trained. Karras, Aittala, Aila, and Laine (2022) separately cleaned the design space of *score-based* generative models, which are also dynamics in function space. Both lines show the same Chapter 3 moral: once you own a transform, you can learn in the transformed coordinates.

## Interpretation and insight

A FIPS number is a policy object built on a hardness conjecture. A GraphGPS ablation is an empirical regularity. A Fourier multiplier that fits one Reynolds number may fail at another. Chapter 3’s skill—name the mechanism, then name the assumption—still applies.

## Limitations and extensions

This page does not redo JPEG, simplex, or RSA arithmetic. Deeper PQC algorithms live also in [future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/).

## Exercises

1. Explain, in two sentences, why deploying ML-KEM *alongside* TLS 1.3’s classical handshake is consistent with Chapter 3’s “mechanism, not slogan” rule.
2. GraphGPS claims $$O(N+E)$$ with linear attention. Which graph algorithm from the networks lecture is still the right tool if you need a *certificate* of connectivity, not an embedding?
3. Write the Fourier-multiplier layer above and mark which symbol is learned and which is the same DFT you already met.
4. A PINN and a neural operator both “solve PDEs.” Which one approximates a *function*, and which one approximates a *map between functions*?

## References

- NIST. (2024). FIPS 203, 204, 205. [Announcement](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips); [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203).
- Rampášek, L., et al. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Kovachki, N., et al. (2023). Neural operator: Learning maps between function spaces with applications to PDEs. *JMLR*, 24(89). [paper](https://jmlr.org/papers/v24/21-1524.html).
- Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. *NeurIPS*. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364).
