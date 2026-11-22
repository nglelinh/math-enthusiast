---
layout: post
title: "Hugo Duminil-Copin: Phase Transitions in Statistical Physics (Fields Medal 2022)"
chapter: '02'
order: 19
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Hugo Duminil-Copin** received the **Fields Medal 2022** for solving longstanding problems in the probabilistic theory of phase transitions in statistical physics, especially in dimensions three and four. The medal does not name a single closed-form theorem. It names a laboratory: lattice models whose macroscopic behavior changes abruptly when a parameter crosses a critical value, and a collection of proofs that made those changes mathematically sharp in dimensions where exact solvability fails.

This essay is for learners who have seen a first percolation or Ising model and want the architecture of modern rigorous statistical mechanics. It does **not** claim that “conformal invariance of all two-dimensional models is finished,” nor that Duminil-Copin worked alone. It explains slogans carefully: continuity versus discontinuity of a transition, sharpness, mean-field triviality in four dimensions, and how Fortuin–Kasteleyn percolation sits next to the conformal stories of [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/) and [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/).

---

## Learning objectives

After this lecture you should be able to:

- State a **phase transition** as a change in the infinite-volume law of a lattice model when a parameter (temperature, edge-weight, cluster-weight) crosses a critical value.
- Distinguish **continuity** of magnetization or percolation density at criticality from **sharpness** (exponential decay on the subcritical side, no intermediate phase).
- Explain why dimension four is **marginal** for Ising and $$\varphi^4$$: mean-field Gaussian behavior with logarithmic corrections, after Aizenman–Fröhlich triviality in dimensions $$d\ge 5$$.
- Describe Fortuin–Kasteleyn (FK) percolation as a geometric representation of Potts/Ising models, and say what continuity versus discontinuity of the FK transition on $$\mathbb{Z}^2$$ means.
- Attribute credit carefully: random currents, OSSS-type sharpness, and rotational invariance are collaborative; full conformal invariance of every planar FK model is **not** the 2022 citation.

**Prerequisites.** Independent bond percolation on $$\mathbb{Z}^d$$ at slogan level; the Ising Hamiltonian as a sum of neighbor spin products; the idea that infinite-volume limits may depend on boundary conditions. No prior conformal field theory required.

**Seminar links.** LO1 / LO4 (hard programs; lattice probability ↔ continuum scaling limits). Pair with [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/) for conformal invariance of critical site percolation on the triangular lattice, and with [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) for SLE as the continuum language those limits speak when they exist.

---

## 1. Why a lattice model needs theorems, not only pictures

A first course writes the Ising energy on a finite box $$\Lambda\subset\mathbb{Z}^d$$ as

$$
H_\Lambda(\sigma)=-\sum_{\{x,y\}\subset\Lambda}J_{xy}\sigma_x\sigma_y-h\sum_{x\in\Lambda}\sigma_x,\qquad \sigma_x=\pm 1,
$$

and the Gibbs weight $$e^{-\beta H}$$. As $$\beta$$ increases, neighbor spins prefer to align. In infinite volume one asks whether the magnetization

$$
m(\beta)=\lim_{h\downarrow 0}\langle\sigma_0\rangle_{\beta,h}
$$

is zero or positive. The same question, for Bernoulli percolation, asks whether the origin belongs to an infinite open cluster with positive probability.

Pictures of “ordered” and “disordered” phases are easy. Theorems are not. Existence of a critical inverse temperature $$\beta_c\in(0,\infty)$$ in dimensions $$d\ge 2$$ is classical; what happens **at** $$\beta_c$$, and how fast correlations decay **just below** it, resisted decades of effort in three dimensions. Two-dimensional Ising was solved by Onsager; that exact solution does not export to $$d=3$$ or to dependent percolation models whose weights are not independent coin flips.

**Slogan.** A phase transition is a theorem about infinite-volume measures, not a plot of a finite-box magnetization.

---

## 2. History of the idea

Onsager’s 1944 solution of two-dimensional Ising made continuity of magnetization at $$\beta_c$$ a calculation. Percolation theory, from Broadbent–Hammersley onward, supplied a geometric language: open clusters, critical probabilities, and Russo–Seymour–Welsh crossing estimates. Fortuin and Kasteleyn recast Potts models as **random-cluster** (FK) measures, so spin correlations become connection probabilities. Aizenman’s **random current** representation turned Ising correlations into intersection properties of integer-valued currents.

By the 1980s–2000s, two-dimensional conformal invariance had become a program: Smirnov on triangular percolation, Schramm’s SLE, Werner on continuum interfaces. That program is spectacular and **dimension-specific**. Dimensions three and four demand currents, randomized algorithms (OSSS), infrared bounds, and multiscale intersection estimates. The 2022 citation emphasizes closing those higher-dimensional and dependent-model problems, not replacing the two-dimensional conformal story.

---

## 3. Continuity and sharpness, especially in three dimensions

**Continuity** at criticality for ferromagnetic Ising models asks whether the spontaneous magnetization vanishes at $$\beta_c$$. For the nearest-neighbor Ising model on $$\mathbb{Z}^3$$ this was a long-standing question. With Aizenman and Sidoravicius, Duminil-Copin proved continuity by studying infinite-volume random currents and using uniqueness of infinite clusters in that representation. The same circle of ideas yields continuity for a class of ferromagnetic Ising systems that includes the standard three-dimensional lattice.

**Sharpness** is a different statement. Below criticality, one wants exponential decay of connectivity or of spin correlations, and finiteness of susceptibility; above criticality, one wants a uniformly positive density of the infinite cluster or a strictly positive magnetization. There should be no “fuzzy” interval of parameters where correlations decay slowly but no infinite cluster exists. Duminil-Copin and Tassion gave a new proof of sharpness for Bernoulli percolation and Ising on general transitive graphs. Later work with Raoufi and Tassion used the OSSS inequality to treat FK and related dependent models in a unified way.

**Accuracy.** Continuity and sharpness are siblings, not synonyms. A transition can be continuous yet require a separate argument to be sharp; Potts models with large $$q$$ can be discontinuous.

---

## 4. Four dimensions: mean-field and triviality

Constructive quantum field theory asked whether a nontrivial Euclidean scalar field with $$\varphi^4$$ interaction exists in four dimensions. Aizenman and Fröhlich independently showed in the early 1980s that, in dimensions $$d\ge 5$$, scaling limits of critical Ising and lattice $$\varphi^4$$ models are Gaussian: Wick’s law holds, and the continuum theory is “trivial” as an interacting field.

Dimension four is **marginal**. Infrared bounds still constrain the two-point function, but the tree-diagram estimate on the deviation from Wick’s law is not quite strong enough. With Aizenman, Duminil-Copin proved **marginal triviality**: scaling limits of critical and near-critical four-dimensional Ising and $$\varphi^4_4$$ models are Gaussian. The proof improves the tree bound by a logarithmic factor, via a multiscale analysis of intersection probabilities of random currents. In the language of the citation, this is mean-field critical behavior of four-dimensional Ising and triviality of four-dimensional Euclidean scalar quantum field theory.

**Slogan.** “Trivial” here means Gaussian as a Euclidean field, not “easy to prove.”

---

## 5. FK percolation: continuity, discontinuity, and a step toward conformal invariance

The random-cluster measure with cluster-weight $$q\ge 1$$ interpolates Bernoulli percolation ($$q=1$$) and the geometric representation of $$q$$-state Potts models. On the square lattice the critical point is known (Beffara–Duminil-Copin). With Sidoravicius and Tassion, Duminil-Copin proved that the FK transition on $$\mathbb{Z}^2$$ is **continuous** for $$q\in[1,4]$$ and **discontinuous** for $$q>4$$, matching the prediction that $$q=4$$ is the threshold.

Continuity of the planar FK transition is not **conformal invariance** of a scaling limit. A later collaboration (Kozlowski, Krachun, Manolescu, Oulamara) established **rotational invariance** of critical two-dimensional FK for a range of $$q$$—a genuine step toward conformal invariance, **not** a proof that every planar FK model has an SLE or CFT scaling limit. Smirnov’s triangular percolation and Schramm–Werner SLE remain the models of a complete continuum identification. FK conformal invariance is a neighboring program, still open in full generality.

---

## 6. Why a Fields Medal

Three interlocking reasons:

1. **Difficulty.** Continuity of three-dimensional Ising and triviality in four dimensions were classical open problems; the proofs use representations that are easy to name and hard to close.
2. **Centrality.** Phase transitions organize statistical mechanics. Once continuity, sharpness, and mean-field thresholds are theorems, the map of which models can have nontrivial continuum limits is sharper.
3. **Clarity of slogan with depth of method.** “The 3D Ising transition is continuous; 4D Ising is Gaussian at scale” is a sentence a graduate student can remember; the current-intersection and OSSS arguments are monuments of contemporary probability.

For this course, Duminil-Copin sits between the two-dimensional conformal Fields stories and the constructive-field-theory question of whether an interacting scalar field can exist in four dimensions.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “He proved conformal invariance of all FK models.” | He proved continuity/discontinuity theorems and rotational invariance steps; full conformal invariance remains open in general. |
| “Continuity equals sharpness.” | Continuity is about the order parameter at $$\beta_c$$; sharpness is about the absence of an intermediate phase and exponential decay below $$\beta_c$$. |
| “Triviality means the Ising model is uninteresting.” | It means the scaling limit is Gaussian as a Euclidean field. |
| “Onsager already did three dimensions.” | Onsager solved two-dimensional Ising; $$d=3$$ has no such closed form. |
| “The medal is only 2D percolation.” | The citation stresses dimensions three and four, plus a broader probabilistic theory of transitions. |

---

## Exercises

1. In your own words: what does an **infinite-volume** Gibbs measure forget and retain compared with a finite-box partition function?
2. Why does a statement that magnetization **vanishes at** $$\beta_c$$ feel different from a statement that correlations **decay exponentially** for all $$\beta<\beta_c$$?
3. Write the random-cluster weight schematically (edge-weight $$p$$, cluster-weight $$q$$) and say which $$(p,q)$$ recover Bernoulli percolation and which recover Ising.
4. Aizenman–Fröhlich treated $$d\ge 5$$; Aizenman–Duminil-Copin treated $$d=4$$. What does “marginal” mean in one paragraph?
5. **Accuracy practice.** Find a popular sentence that says Duminil-Copin “proved conformal invariance in 3D.” Rewrite it in two precise sentences.
6. **Seminar stretch.** Compare this portrait with [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/) and [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/): one laboratory identifies a continuum object; the other proves lattice theorems that make a continuum limit conceivable. When would you want each?

---

## Video sources and reading

1. **IMU citation** — Fields Medals 2022 page and the official citation PDF: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022) · [citation](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/IMU_Fields22_Duminil-Copin_citation.pdf).
2. **Orientation** — Quanta profile: [Hugo Duminil-Copin Wins the Fields Medal](https://www.quantamagazine.org/hugo-duminil-copin-wins-the-fields-medal-20220705/).
3. **Survey** — M. Biskup, *The work of Hugo Duminil-Copin* (arXiv:2207.02022), written for the 2022 award.

**Status reminder:** Continuity, sharpness, and 4D triviality—**not** a claim that every planar FK model is conformally invariant.

---

## References

1. IMU Fields Medal 2022 citation — Hugo Duminil-Copin (mathunion.org).
2. **M. Aizenman, H. Duminil-Copin, V. Sidoravicius** — Random currents and continuity of Ising magnetization (2015).
3. **H. Duminil-Copin and V. Tassion** — Sharpness of the phase transition for percolation and Ising (2016); later OSSS work with A. Raoufi.
4. **M. Aizenman and H. Duminil-Copin** — Marginal triviality of critical 4D Ising and $$\varphi^4_4$$ (Ann. of Math., 2021).
5. Course neighbors: [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/), [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/).

---

## Further directions

- Read a survey of random currents and list three identities that turn spin correlations into geometric events.
- Compare Onsager’s exact two-dimensional solution with the three-dimensional continuity theorem: what does “solved” mean in each culture?
- Seminar A3 option: one page on what remains open for conformal invariance of planar FK models—without claiming the 2022 medal closed that program.
