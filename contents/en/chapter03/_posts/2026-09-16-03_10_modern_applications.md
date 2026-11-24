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

The core ideas of Chapter 3—modular arithmetic in RSA, graphs in web search, gradients in optimization, and Fourier transforms in signal processing—are decades to centuries old. Have they settled into museum pieces? Quite the opposite. Between **2022 and 2026**, four technological breakthroughs grew directly out of those classical foundations, reshaping internet security, scientific AI, and physical simulation: lattice-based cryptography became an official U.S. federal standard; Transformers merged with graph neural networks; neural operators began solving PDEs directly in Fourier space; and diffusion models started generating images by integrating stochastic differential equations backward in time.

This optional update places those four 2022–2026 landmarks directly on top of Chapter 3’s mathematical toolkit—showing exactly which classical coordinates stayed fixed and which new layers were built on top.

---

## Background Knowledge Map: How Do 2022–2026 Breakthroughs Extend Classical Chapter 3 Math?

What makes the 2022–2026 wave so illuminating is that it **never discards** Chapter 3’s mathematics—it upgrades either the *coordinate system* or the *underlying hard problem* by one level:

| Classical thread (Chapter 3) | Bottleneck at 2022–2026 scale | Modern leap (2022–2026) |
|---|---|---|
| **Number-theoretic crypto** (RSA, ECC) | Threatened by Shor’s algorithm on a future fault-tolerant quantum computer. | **NIST FIPS 203/204/205:** migrates to lattice geometry (Module-LWE) and hash-based signatures. |
| **Graphs & message-passing GNNs** | Passing messages only to immediate neighbors causes long-range *over-squashing*. | **Graph Transformers (GraphGPS):** fuse local message passing with linear-time global attention $$O(N+E)$$. |
| **Classical PDE solvers** (FEM, CFD) | Too slow when thousands of forward runs are needed for design or weather ensembles. | **Neural Operators (FNO):** learn maps directly between *function spaces*, running $$100\times$$–$$1000\times$$ faster at inference. |
| **Fourier analysis & SDEs** | Classical filters are hand-crafted; generative sampling needs stable reverse paths. | **Learned frequency filters** ($$\widehat{K}$$ trained by gradient descent) & **Diffusion models** reversing ODEs/SDEs. |

---

## Learning objectives

After this optional update you should be able to attach one 2022–2026 citation to each of four Chapter 3 migrations—public-key cryptography, graphs, optimization-adjacent scientific ML, and Fourier-flavored PDE surrogates—without rewriting the required mechanism lectures.

## Prerequisites

The required sequence, especially [number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/), [graphs]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/), [optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [Fourier]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/), and [differential equations]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/).

## Introduction

Chapter 3 already told the migration stories: modular arithmetic became a handshake; a graph became a network; a gradient became a training step; a Fourier mode became a JPEG. Those mechanisms did not expire. What changed after 2022 is the *standard and the architecture* sitting on top of them. Lattice KEMs became federal standards. Graph models grew a Transformer branch. PDE solvers grew a learned-operator branch that still speaks Fourier.

## Conceptual development

A key-encapsulation mechanism produces a shared secret $$K$$ from public encapsulation. Classically, $$K$$ is protected by factoring or discrete log. After Shor, the hardness assumption moves. Graph learning, meanwhile, still needs a representation of a vertex $$v$$ that mixes *neighbors* with a *global* token mix. Fourier neural operators implement a learned kernel as a multiplier $$\widehat{K}(k)$$ in frequency space—the same dual picture as the Fourier lecture, now trained rather than designed.

### Deep-Dive Explanation: Reading a 2022–2026 Applied Math Paper Without Getting Lost in Jargon (Read Slowly)

Whenever a headline announces a dazzling new architecture or cryptographic standard, you can decode it in four calm steps—and check the mechanism on a concrete miniature calculation:

1. **Name the classical engine underneath:** ML-KEM is still linear algebra modulo $$q$$; GraphGPS is still graph adjacency plus matrix multiplication; FNO is still FFT/IFFT; Diffusion is still numerical ODE/SDE integration.
2. **Pinpoint the exact bottleneck removed:** Replacing factoring with Module-LWE removes the periodic structure Shor exploits; replacing $$O(N^2)$$ all-pairs attention with $$O(N+E)$$ hybrid attention scales to large graphs; replacing per-instance PDE solving with a learned operator $$\mathcal{G}$$ amortizes cost across thousands of queries.
3. **Separate what is “hard-coded” from what is “learned”:** Let us verify how a **Fourier Neural Operator (FNO)** layer acts on a 4-sample 1D signal $$u = (1, 0, -1, 0)$$ by hand:
   - **Fixed FFT step:** Its 4-point DFT is $$\widehat{u} = (0, 2, 0, 2)$$ (pure cosine mode at frequency $$k = \pm 1$$).
   - **Learned spectral multiplier:** Suppose the network learns a single complex weight $$\widehat{K}_1 = 0.5$$ on the low-frequency mode (damping it by half) and zeros out high modes: $$\widehat{v} = (0, 1, 0, 1)$$.
   - **Fixed IFFT step:** Transforming back gives $$v = (0.5, 0, -0.5, 0)$$—a global convolution across the entire domain computed in a single multiplication, independent of grid spacing!
4. **Inspect the validity domain and hardness assumptions:** FIPS standards rest on the conjectured hardness of Module-LWE; learned PDE surrogates are only trustworthy inside the parameter regime (such as the Reynolds-number range) seen during training.

**Quick check:** Modern applied mathematics rarely erases classical mathematics—it builds new optimization and architectural layers directly on top of classical coordinates.

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

## References

- NIST. (2024). FIPS 203, 204, 205. [Announcement](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips); [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203).
- Rampášek, L., et al. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Kovachki, N., et al. (2023). Neural operator: Learning maps between function spaces with applications to PDEs. *JMLR*, 24(89). [paper](https://jmlr.org/papers/v24/21-1524.html).
- Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. *NeurIPS*. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364).

## Video tham khảo

- **xem trước** — [Post Quantum Cryptography - Computerphile](https://www.youtube.com/watch?v=_MoRcYLN-7U) — Computerphile, English. Watch first. “Post Quantum Cryptography - Computerphile” orients the lesson’s aim: After this optional update you should be able to attach one 2022–2026 citation to each of four Chapter 3 migrations—public-key cryptography, graphs, optimization-adjacent scientifi…
- [An Introduction to Graph Neural Networks: Models and Applications](https://www.youtube.com/watch?v=zCEYiCxrL_0) — Microsoft Research, English. A second pass once the main claim is in view: After this optional update you should be able to attach one 2022–2026 citation to each of four Chapter 3 migrations—public-key cryptography, graphs, optimization-adjacent scientifi…
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, English. Further depth after the first two, still tied to this lesson: After this optional update you should be able to attach one 2022–2026 citation to each of four Chapter 3 migrations—public-key cryptography, graphs, optimization-adjacent scientifi…
