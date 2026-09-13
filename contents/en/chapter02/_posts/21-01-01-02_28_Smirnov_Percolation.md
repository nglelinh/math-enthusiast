---
layout: post
title: "Smirnov’s Percolation and the Planar Ising Model (Fields Medal 2010)"
chapter: '02'
order: 28
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Stanislav Smirnov** received the **Fields Medal 2010**

> “For the proof of conformal invariance of percolation and the planar Ising model in statistical physics.”  
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

The citation names two lattice models, not a slogan that “all critical 2D models are now theorems.” Physicists had long predicted that at criticality many planar models forget their microscopic lattice and remember only a conformal geometry. Making that prediction into mathematics required observables that stay under analytic control as the mesh tends to zero. Smirnov supplied such observables for **critical site percolation on the triangular lattice** (2001) and, with collaborators, for the **planar Ising model**. The continuum language for the resulting interfaces is **Schramm–Loewner evolution (SLE)**, invented by Oded Schramm and developed by Gregory Lawler, Schramm, and Wendelin Werner—see [Werner / SLE]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/). Later phase-transition theorems of Hugo Duminil-Copin sit in the same landscape: [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase_Transitions/).

This essay is for learners who have met complex analysis and elementary probability and want the architecture of the 2010 medal: what Cardy’s formula says, why the triangular lattice is essential, what Ising conformal invariance means at the level of fermionic observables, and which neighbouring statements remain open.

---

## Learning objectives

After this lecture you should be able to:

- State, at slogan level, what **Bernoulli percolation** is, and distinguish **site** percolation from **bond** percolation.
- Explain why a **critical** parameter $$p_c$$ is the interesting place to look for a nontrivial scaling limit.
- Describe **Cardy’s crossing formula** as a prediction for the probability that a critical cluster crosses a conformal rectangle, and name Smirnov’s 2001 theorem as the proof of that prediction for **critical site percolation on the triangular lattice**.
- Explain why the same result is **not** claimed here for arbitrary lattices, and in particular not for **bond percolation on the square lattice**.
- Place **SLE** as the scaling-limit language for interfaces, crediting Schramm for the definition and Lawler–Schramm–Werner for the analytic theory.
- Distinguish the percolation theorem from later **planar Ising** conformal invariance (Smirnov; Chelkak–Smirnov and collaborators).
- Attribute credit carefully and avoid the hype sentence “Smirnov solved 2D statistical physics.”

**Prerequisites.** Holomorphic functions and conformal maps of plane domains at the level of a first complex-analysis course; Bernoulli random variables and the idea of a scaling limit (mesh $$\delta\to 0$$); the difference between a discrete model and a continuum process. No prior SLE course is required.

**Seminar links.** LO1 / LO4 (a physicists’ conjecture made into a lattice-specific theorem; discrete models ↔ continuum conformal geometry). Pair with [Werner / SLE]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) for the curve language, and with [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase_Transitions/) for later sharp results on phase transitions.

---

## 1. Why statistical physics wanted conformal invariance

A **percolation** configuration on a graph is a random colouring of vertices (site percolation) or edges (bond percolation) as open or closed, independently, with probability $$p$$ of being open. The simplest geometric question is whether open sites form a path connecting two boundary arcs. For extreme $$p$$ the answer is dull; many two-dimensional lattices have a **critical value** $$p_c$$ at which the crossing probability of a large rectangle stays bounded away from both $$0$$ and $$1$$.

If one rescales to mesh $$\delta\to 0$$, the cluster geometry is expected to converge to a random continuum object. Two-dimensional conformal field theory suggested something stronger: the limit should be **conformally invariant**. John Cardy, using non-rigorous CFT methods, produced an explicit formula for the limiting crossing probability of a conformal rectangle (*J. Phys. A*, 1992). Lennart Carleson observed that the formula becomes simple on an equilateral triangle. The difficulty was not writing the formula; it was proving that a concrete lattice model converges and that the limit transforms as Cardy predicted.

---

## 2. Site percolation on the triangular lattice

Smirnov’s 2001 theorem concerns **critical site percolation on the triangular lattice** $$\mathbb{T}$$, with $$p=1/2$$. The *Comptes Rendus* note (Smirnov, *C. R. Acad. Sci. Paris* 333 (2001); longer account arXiv:0909.4499) introduces discrete harmonic conformal invariants built from crossing and colour-switching probabilities. Those functions are approximately harmonic and satisfy discrete Cauchy–Riemann relations from a **colour-switching identity** special to $$\mathbb{T}$$. They converge to explicit holomorphic functions of a Dirichlet–Neumann problem, yielding conformal invariance of crossings and **Cardy’s formula**. In Carleson’s form, on an equilateral triangle of side one the limiting crossing probability from a side to a point opposite is linear in position.

**Accuracy that must not be blurred.** The argument uses the threefold symmetry of $$\mathbb{T}$$ in an essential way. It is a theorem about **this** lattice model, not a theorem about “percolation in the plane” in full generality. In particular, **critical bond percolation on the square lattice**—the other most famous planar percolation—remains a celebrated open problem at the same level of conformal invariance. Universality is believed, and much partial progress exists, but this course will not pretend that Smirnov 2001 closed every lattice.

---

## 3. From crossings to curves: SLE as the limit language

Crossing probabilities are scalar conformal invariants. The richer object is the **interface**: the curve that separates open from closed, or the exploration path that follows the boundary of a cluster. Once crossings are under control, one can ask whether these random curves converge in law to a continuum process.

**Schramm–Loewner evolution** $$\mathrm{SLE}_\kappa$$, introduced by Oded Schramm in 2000 (*Israel J. Math.* 118, “Scaling limits of loop-erased random walks and uniform spanning trees”), is a one-parameter family of random growing hulls in a plane domain, generated by driving a Loewner differential equation with Brownian motion of variance $$\kappa$$. Schramm proved that if a chordal scaling limit exists and is conformally invariant (with a Markovian restriction property), it must be $$\mathrm{SLE}_\kappa$$ for some $$\kappa$$. For percolation the predicted value is $$\kappa=6$$.

Lawler, Schramm, and Werner developed the analytic theory of SLE: restriction properties, intersection and disconnection exponents, and the geometry of two-dimensional Brownian motion. That development is the subject of Werner’s 2006 Fields Medal and is **not** Smirnov’s citation; it is the language in which Smirnov’s lattice theorems are now read. Subsequent work (notably Camia–Newman, and later interface papers) used Smirnov’s crossing theorem as the gateway to identifying the percolation exploration path with $$\mathrm{SLE}_6$$. For this seminar, keep the division of labour:

| Contribution | Who, at slogan level |
|--------------|----------------------|
| Invented SLE | Schramm (2000) |
| Analytic theory of SLE; Brownian frontier; exponents | Lawler–Schramm–Werner |
| Cardy + conformal invariance for triangular site percolation | Smirnov (2001) |
| Planar Ising observables / interfaces | Smirnov; Chelkak–Smirnov and later collaborators |

---

## 4. The planar Ising model

The **Ising model** assigns spins $$\pm 1$$ to vertices of a planar graph, with a Boltzmann weight favouring aligned neighbours. At a critical temperature the model is expected to have a conformally invariant scaling limit, historically one of the first CFT success stories (Onsager’s exact solution already gave the 2D free energy; conformal invariance of the full geometry is a different, harder claim).

Smirnov introduced discrete **holomorphic fermions** for the critical Ising model (see “Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model,” *Ann. of Math.* 172 (2010)). With Dmitry Chelkak he proved that these fermionic observables have universal, conformally invariant scaling limits on a large family of planar graphs, not only on one lattice: Chelkak–Smirnov, “Universality in the 2D Ising model and conformal invariance of fermionic observables,” *Invent. Math.* 189 (2012), arXiv:0910.2045. Later work with Chelkak, Duminil-Copin, Hongler, Kemppainen, and others identified Ising interfaces with SLE curves (in particular $$\mathrm{SLE}_3$$ for spin interfaces, in the appropriate setup).

Two pedagogical points matter. First, “conformal invariance of the Ising model” in the medal citation refers to this program of observables and limits, not to Onsager’s 1944 solution of the partition function. Second, the Ising theory is in some respects **more universal** than the 2001 percolation theorem: the Chelkak–Smirnov setting covers a broad class of isoradial graphs, whereas the percolation Cardy theorem remains tied to the triangular lattice.

---

## 5. Design of the proofs, and why a Fields Medal

Both stories invent a discrete observable $$F_\delta$$ that encodes the event (a crossing, a spin, an interface), satisfies an approximate holomorphicity relation, and has boundary conditions that pass to a continuum Dirichlet or Riemann–Hilbert problem. Precompactness gives subsequential limits; uniqueness of the continuum problem identifies the limit; conformal covariance is inherited. For triangular percolation, a colour-switching identity equates two three-arm events and supplies discrete Cauchy–Riemann equations. For Ising, the observable is fermionic and discrete holomorphicity comes from integrability. The methods are cousins, not copies: the lattice must offer an identity strong enough to close the system, which is why one lattice can fall and another remain open.

The medal is not “he guessed Cardy’s formula.” A physicists’ conjecture became a theorem with an explicit crossing law; discrete holomorphic observables reorganized 2D statistical mechanics; and once those observables are conformally invariant, the Schramm–Lawler–Werner curve theory can attach $$\mathrm{SLE}_6$$ or $$\mathrm{SLE}_3$$ to a named lattice model. The 2010 class also included Lindenstrauss, Ngô, and Villani—see [Villani]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/) for a kinetic citation from the same congress.

---

## 6. What remains open, honestly

Critical bond percolation on the square lattice, and conformal invariance of percolation on general planar lattices, are still not theorems in the sense of Smirnov 2001. Many exponents and arm events are known for the triangular site model once conformal invariance is available; the corresponding statements on other lattices often remain conjectural or only partially transferred. Self-avoiding walk, whose predicted scaling limit is $$\mathrm{SLE}_{8/3}$$, is a famous neighbour that is **not** a Smirnov theorem. The Duminil-Copin portrait treats sharpness of phase transitions and related lattice results that complement, rather than repeat, the 2001 conformal-invariance theorem.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Smirnov proved conformal invariance of percolation on every lattice.” | The 2001 theorem is for **critical site percolation on the triangular lattice**. Square-lattice bond percolation is a famous remaining case. |
| “Cardy proved the crossing formula.” | Cardy derived it by non-rigorous CFT; Smirnov proved it for triangular site percolation. |
| “SLE was invented by Werner (or by Smirnov).” | SLE was introduced by **Schramm** (2000). Werner’s Fields is for developing SLE and 2D Brownian geometry, largely with Lawler and Schramm. |
| “The 2010 medal is only percolation.” | The IMU citation names percolation **and** the planar Ising model. |
| “Onsager’s solution is the same as conformal invariance of Ising.” | Onsager computed the 2D free energy (1944). Conformal invariance of observables and interfaces is a later geometric statement. |
| “Once you have SLE, every 2D model is solved.” | SLE is a candidate limit law. Identifying a lattice model with a given $$\kappa$$ is a separate theorem, often still open. |

---

## Exercises

1. In two sentences, distinguish **site** percolation from **bond** percolation. Why might a proof that uses a colour-switching identity on triangles fail to copy onto the square lattice?
2. What is a **crossing probability** of a conformal rectangle? Why is the critical value $$p_c$$ the only place where one expects a nontrivial, mesh-independent limit in $$(0,1)$$?
3. State Cardy’s formula at slogan level, and write one sentence on Carleson’s equilateral-triangle simplification.
4. Credit practice: assign **Schramm**, **Lawler–Schramm–Werner**, and **Smirnov** each one sentence that could appear in a referee’s report.
5. Skim the abstract of Chelkak–Smirnov (arXiv:0910.2045). What is the observable, and in what sense is the result more “universal” than Smirnov 2001?
6. Why is “the interface converges to $$\mathrm{SLE}_6$$” a stronger statement than “crossing probabilities converge to Cardy’s formula”? What extra compactness or identification work is needed, at slogan level?
7. **Accuracy practice.** Rewrite the popular sentence “Smirnov showed that 2D phase transitions are conformal” as two precise sentences suitable for this course.
8. **Seminar stretch.** Compare this medal with [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/): who supplied the curve process, and who supplied a lattice model that converges to it?

---

## Links

- IMU Fields Medals 2010 (requested index): [mathunion.org/…/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- IMU / ICM 2010 Smirnov page (working archive): [Fields Medal – Stanislav Smirnov](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-stanislav-smirnov.html)
- IMU Fields Medal index: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Wikipedia: [Stanislav Smirnov](https://en.wikipedia.org/wiki/Stanislav_Smirnov)
- arXiv: [0909.4499](https://arxiv.org/abs/0909.4499) (Smirnov, critical percolation); [0910.2045](https://arxiv.org/abs/0910.2045) (Chelkak–Smirnov, Ising); search [Smirnov percolation Cardy](https://arxiv.org/search/?query=Smirnov+percolation+Cardy&searchtype=all)
- Course: [Werner / SLE]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/), [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase_Transitions/), [Villani]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/)

---

## References

1. International Mathematical Union, Fields Medals 2010 citation for Stanislav Smirnov (IMU / ICM Hyderabad 2010 materials).
2. **S. Smirnov**, “Critical percolation in the plane: conformal invariance, Cardy’s formula, scaling limits,” *C. R. Acad. Sci. Paris Sér. I Math.* 333 (2001), 239–244; longer account arXiv:0909.4499.
3. **J. L. Cardy**, “Critical percolation in finite geometries,” *J. Phys. A* 25 (1992), L201–L206.
4. **O. Schramm**, “Scaling limits of loop-erased random walks and uniform spanning trees,” *Israel J. Math.* 118 (2000), 221–288.
5. **D. Chelkak and S. Smirnov**, “Universality in the 2D Ising model and conformal invariance of fermionic observables,” *Invent. Math.* 189 (2012), 515–580, arXiv:0910.2045.
6. **S. Smirnov**, “Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model,” *Ann. of Math.* 172 (2010), 1441–1473.
7. Wikipedia, [Stanislav Smirnov](https://en.wikipedia.org/wiki/Stanislav_Smirnov); course portraits of [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) and [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase_Transitions/).

---

## Further directions

- Read a survey of the colour-switching argument before the *Comptes Rendus* note; after [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/), write a half-page on the order SLE axioms → Cardy → identification with $$\mathrm{SLE}_6$$.
- Seminar option: a one-page “what is still open in 2D percolation” brief that does **not** claim universality is a theorem.
