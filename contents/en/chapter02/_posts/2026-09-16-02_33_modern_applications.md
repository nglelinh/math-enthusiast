---
layout: post
title: "Modern Applications: Fields Ideas in Computer Science"
chapter: '02'
order: 33
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
lesson_type: optional
---

## Learning objectives

After this optional note you should be able to point to three 2022–2026 computer-science deployments that *reuse mathematical objects* featured in this chapter—optimal transport, high-dimensional lattices, and phase-transition thinking—without treating the note as a Fields biography and without repeating the Tao six-pillar hub in Chapter 4.

## Prerequisites

Skim the thematic map in the [overview]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/). You do **not** need the individual medal essays to use this page. Do not read this as a substitute for [Figalli / optimal transport]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska / packing]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/), or the statistical-physics portraits.

## Introduction

Fields essays in this chapter are portraits of people and theorems. Industry rarely ships a portrait. It ships a computational cousin: a neural map that approximates a transport plan, a lattice problem that is believed hard even for quantum adversaries, a solver that dies or lives on the SAT phase boundary. The intellectual tension is attribution. The medal work made the objects sharp; the CS systems make them *cheap enough to run*.

## Conceptual development

A (quadratic) optimal-transport problem seeks a coupling $$\pi$$ of two measures $$\mu,\nu$$ minimizing $$\int c(x,y)\,d\pi$$. Regularity theory asks when the optimizer is a map. Machine learning usually asks when a network can *parameterize* a map or plan well enough for unpaired translation. Separately, a module-lattice problem such as Module-LWE asks for a secret $$s$$ given noisy samples

$$
(A,\, As+e \bmod q),
$$

and packing-type geometry controls how close $$e$$ may sit before unique decoding fails. Neither paragraph is a biography.

## Three complementary landings

### 1. Neural optimal transport, not a transport biography

Korotin, Selikhanovych, and Burnaev (2023) train networks to represent strong and weak OT plans and prove a universal-approximation statement for transport plans. Their experiments include unpaired image-to-image translation. The object is the same Kantorovich plan that the Figalli portrait treats analytically. The paper does not prove new regularity of maps on $$\mathbb{R}^n$$; it shows that a differentiable model can stand in for a plan at image scale. If you want the medal story, stay in the Figalli essay. If you want the 2023 CS artifact, start here.

### 2. Module lattices as post-quantum key encapsulation

NIST FIPS 203 (August 2024) standardizes ML-KEM, a module-lattice key-encapsulation mechanism derived from CRYSTALS-Kyber, with parameter sets ML-KEM-512/768/1024. Security is tied to the difficulty of Module-LWE, not to a resolution of sphere packing in dimensions 8 or 24. The complementary link to this chapter is geometric: high-dimensional lattices, shortest-vector hardness, and packing-type decoding radii are the *language* in which the standard is written. The Viazovska essay remains the place for magic dimensions and modular forms.

### 3. Phase-transition thinking in SAT and graph learning

Random $$k$$-SAT and percolation both have sharp thresholds: below a density, typical instances are easy or connected; above it, they are not. Modern SAT competitions still live on crafted and industrial formulas near those walls. Graph transformers such as GraphGPS (Rampášek, Galkin, Dwivedi, Luu, Wolf, and Beaini, 2022) mix local message passing with global attention of complexity $$O(N+E)$$, and they inherit the same statistical-physics instinct—local neighborhoods versus a global mode. This is not a Duminil-Copin or Smirnov biography. It is the *habit* of looking for a critical density before you trust a solver or a GNN.

## Interpretation and insight

A transport network that “works” on CelebA is not a theorem about Monge–Ampère regularity. A KEM that survives a NIST process is not a packing theorem. A GNN that scores well on ZINC is not a proof of a continuum phase transition. The Fields objects remain the clean statements; the CS systems are calibrated approximations.

## Limitations and extensions

This note deliberately skips Hong Wang / Kakeya and Yu Deng portraits, and it does not retell Green–Tao compressed sensing. Those pages already exist. It also does not survey the 2026 medal citations.

## Exercises

1. Write one sentence that uses the word “plan” correctly for Korotin et al. and one sentence that would belong only in the Figalli essay.
2. ML-KEM-768 is recommended for many deployments. Which mathematical object is the hardness assumption, and which Fields packing theorem does *not* have to be invoked?
3. A teammate says GraphGPS “solves percolation.” What quantity on a finite attributed graph is actually being optimized?
4. Why does this page refuse to add another biographical paragraph to the gallery?

## References

- Korotin, A., Selikhanovych, D., & Burnaev, E. (2023). Neural optimal transport. *ICLR*. [arXiv:2201.12220](https://arxiv.org/abs/2201.12220).
- NIST. (2024). *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*. [doi:10.6028/NIST.FIPS.203](https://doi.org/10.6028/NIST.FIPS.203).
- Rampášek, L., Galkin, M., Dwivedi, V. P., Luu, A. T., Wolf, G., & Beaini, D. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Course portraits (do not duplicate here): [Figalli]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/).
