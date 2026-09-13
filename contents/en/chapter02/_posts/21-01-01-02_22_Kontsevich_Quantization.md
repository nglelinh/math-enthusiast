---
layout: post
title: "Kontsevich’s Quantization, Curves, and Knots (Fields Medal 1998)"
chapter: '02'
order: 22
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Maxim Kontsevich** received the **Fields Medal 1998**

> “For his contributions to algebraic geometry, topology, and mathematical physics, including the proof of Witten's conjecture of intersection numbers in moduli spaces of stable curves, construction of the universal Vassiliev invariant of knots, and formal quantization of Poisson manifolds.”
> — IMU citation, ICM 1998 (as recorded in the [Fields Medal](https://www.mathunion.org/imu-awards/fields-medal) record and standard biographical sources)

Three bullets, three subjects. The temptation, looking back from the 2020s, is to replace that list by later slogans—homological mirror symmetry, motivic integration, wall-crossing. Those programs are real, and several of them are Kontsevich’s. They are **not** the 1998 citation. This essay follows the official triad: **Witten’s conjecture** on $$\overline{\mathcal{M}}_{g,n}$$, the **universal Vassiliev invariant**, and **deformation quantization** of Poisson manifolds. Homological mirror symmetry appears only as a related 1994 ICM proposal, not as a claim that mirror symmetry was “solved.”

Kontsevich (born 1964) is a permanent professor at the Institut des Hautes Études Scientifiques and works across algebraic geometry, topology, and mathematical physics. The medal is a portrait of that crossing in the 1990s, not a lifetime dump.

---

## Learning objectives

After this lecture you should be able to:

- Recite the 1998 citation as **three** results, and refuse to replace the third bullet by homological mirror symmetry.
- State Witten’s conjecture at slogan level: a generating function of $$\psi$$-class intersections on $$\overline{\mathcal{M}}_{g,n}$$ is a tau-function of the KdV hierarchy; Kontsevich proved it by ribbon graphs / matrix models.
- Describe the Kontsevich integral as a **universal finite-type (Vassiliev) invariant**, with credit to Vassiliev and Bar-Natan for the surrounding theory.
- Explain deformation quantization: a star product deforming the pointwise product so that the first commutator recovers a Poisson bracket; Kontsevich’s formality theorem / graph formula produces such a product on any Poisson manifold.
- Mention homological mirror symmetry as a 1994 program, not as a completed classification and not as the Fields third bullet.
- Place the work on the [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/) map without treating physics as a substitute for proofs.

**Prerequisites.** The idea of a moduli space of curves; Poisson brackets on $$\mathbb{R}^{2n}$$ or on a symplectic manifold; the Jones polynomial as “a knot invariant that is not just the fundamental group.” Complex analysis and a first algebraic geometry course help; quantum field theory is optional atmosphere.

**Seminar links.** [Mirror symmetry]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/) for the HMS program as a *later reading*, kept separate from 1998. [Pardon / symplectic]({{ site.baseurl }}/contents/en/chapter02/02_13_Pardon_Symplectic/) for Fukaya-side consumers of HMS.

---

## 1. Why the 1998 list is the right outline

ICM prize lectures often outlive their citations. Kontsevich’s later influence is enormous: homological mirror symmetry became a field; motivic integration (a 1995 Orsay lecture, then Denef–Loeser) became a tool in singularity theory; stable maps and Gromov–Witten theory changed enumerative geometry. A course that dumped all of that into “Fields 1998” would be historically false.

The official sentence is already ambitious enough. It says: one person proved a conjecture of Witten about the tautological intersection theory of the moduli of stable curves; constructed a universal finite-type knot invariant; and quantized every Poisson manifold at the formal level. Algebraic geometry, topology, and mathematical physics are not three hobbies. They are three places where the same graph-and-integral instinct produced theorems.

---

## 2. Witten’s conjecture: intersections on $$\overline{\mathcal{M}}_{g,n}$$

Let $$\overline{\mathcal{M}}_{g,n}$$ be the Deligne–Mumford compactification of the moduli space of genus-$$g$$ curves with $$n$$ marked points. On this space live tautological line bundles $$\mathbb{L}_i$$ whose fibers are cotangent lines at the marked points; their first Chern classes are the **$$\psi$$-classes**. Intersection numbers

$$
\langle\tau_{d_1}\cdots\tau_{d_n}\rangle_g=\int_{\overline{\mathcal{M}}_{g,n}}\psi_1^{d_1}\cdots\psi_n^{d_n}
$$

are the simplest numerical invariants of the tautological ring (with the usual vanishing unless the degrees add to the dimension $$3g-3+n$$).

**Witten’s conjecture** (early 1990s) asserted that the generating function of these numbers is a tau-function of the **Korteweg–de Vries (KdV)** hierarchy—equivalently, that the numbers satisfy a system of partial differential equations whose first member is related to the Virasoro constraints / KdV. The conjecture came from two-dimensional quantum gravity: two matrix-model descriptions of random surfaces should agree, one combinatorial and one geometric.

**Kontsevich’s proof** (*Intersection theory on the moduli space of curves and the matrix Airy function*, *Comm. Math. Phys.* 147, 1992) identified the intersection theory with a combinatorial expansion over **ribbon graphs** (via Strebel differentials: a metric that decomposes the curve into fat graphs). The generating function becomes a matrix Airy integral, which is already known to satisfy KdV. Geometry is thereby reduced to a matrix model whose integrable hierarchy is classical.

**Slogan.** Witten guessed that the tautological intersection numbers of moduli of curves know KdV; Kontsevich exhibited a ribbon-graph dictionary that makes the guess a computation.

This is the algebraic-geometry bullet. It is not a classification of all curves; it is a theorem about a specific family of numbers on $$\overline{\mathcal{M}}_{g,n}$$.

---

## 3. Universal Vassiliev invariants and configuration spaces

**Vassiliev** (early 1990s) introduced finite-type invariants of knots: invariants that vanish on singular knots with enough double points, equivalently, invariants whose dependence on crossing changes is polynomial of bounded degree. **Bar-Natan** organized the combinatorial side: weight systems, chord diagrams, and the relationship to Lie algebras and to the Jones polynomial’s coefficients.

What was missing was a **universal** analytic machine that produces all finite-type invariants from a single construction. Kontsevich supplied one: the **Kontsevich integral**, built from iterated integrals over configuration spaces of points on the knot (and, in the perturbative Chern–Simons picture, of points in the ambient $$\mathbb{R}^3$$). The integrands are the same graph complexes that appear in Feynman expansions of Chern–Simons theory—now as convergent (after framing and regularization) differential forms.

The output is a knot invariant taking values in a completed diagram algebra. Every finite-type invariant factors through it; that is the meaning of **universal**. Gauss’s classical linking integral is the simplest ancestor.

**Credit.** Vassiliev posed the finite-type filtration; Bar-Natan and others made the combinatorics usable; Witten suggested a Chern–Simons path-integral source of invariants; Kontsevich gave a mathematical construction that realizes the universal object. The Fields bullet is that construction, not a claim that knot theory began in 1993.

---

## 4. Formal quantization of Poisson manifolds

A **Poisson manifold** $$(M,\pi)$$ carries a bivector $$\pi$$ such that $$\{f,g\}=\langle\pi,df\wedge dg\rangle$$ is a Lie bracket on $$C^\infty(M)$$ satisfying the Leibniz rule. Symplectic manifolds are the nondegenerate case; Lie–Poisson structures on duals of Lie algebras are the linear case.

**Deformation quantization** asks for a formal star product—a bilinear product on $$C^\infty(M)[\![\hbar]\!]$$—

$$
f\star g=fg+\hbar B_1(f,g)+\hbar^2 B_2(f,g)+\cdots,
$$

associative, reducing to the pointwise product at $$\hbar=0$$, and satisfying

$$
f\star g-g\star f=i\hbar\{f,g\}+O(\hbar^2).
$$

Existence on symplectic manifolds was known (De Wilde–Lecomte, Fedosov). The Poisson case was open: there is no Darboux chart in which $$\pi$$ is constant, so a local formula is not enough unless it is **natural** in $$\pi$$.

Kontsevich’s **formality theorem** says that the differential graded Lie algebra of Hochschild cochains of $$C^\infty(M)$$ is formal: it is quasi-isomorphic to its cohomology, the Lie algebra of polyvector fields with the Schouten–Nijenhuis bracket. Formality implies that every Poisson structure (a Maurer–Cartan element in polyvector fields) lifts to a star product. The proof supplies an **explicit graph formula**: a sum over certain admissible graphs, each weighted by a configuration-space integral on the upper half-plane, of bidifferential operators built from $$\pi$$.

The paper circulated as a 1997 preprint (arXiv:q-alg/9709040) and appeared in *Letters in Mathematical Physics* 66 (2003). “Formal” means in the formal power-series parameter $$\hbar$$; it is not a claim about analytic convergence of the series, nor about a Hilbert-space quantization of every Poisson manifold.

**Slogan.** Every Poisson bracket is the first-order shadow of a star product; Kontsevich wrote the product as a Feynman expansion whose amplitudes are numbers from configuration spaces.

---

## 5. Related programs that are not the third bullet

**Homological mirror symmetry (HMS).** In his 1994 ICM address (Zürich; arXiv:alg-geom/9411018), Kontsevich proposed that mirror symmetry should be a categorical equivalence: the derived category of coherent sheaves on a Calabi–Yau $$X$$ equivalent to the Fukaya category of a mirror $$Y$$ (A-model / B-model swap). That proposal organized a generation of symplectic and algebraic geometry; many cases are now theorems (due to many people). It is **not** the 1998 citation’s third item, and saying Kontsevich “solved mirror symmetry” is false. The course already treats HMS as an open-ended program in [Mirror Symmetry]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/).

**Motivic integration.** Kontsevich sketched it in a 1995 Orsay lecture; **Denef–Loeser** developed the published theory. Adjacent and later—not a Fields bullet.

**Stable maps.** Kontsevich’s compactification of maps from curves is central to Gromov–Witten theory. Taubes’s 1998 ICM report discusses it; the official citation does not make it the third prize item.

---

## 6. Why a Fields Medal

The 1998 medal sits among those that reward **dictionaries**: ribbon graphs $$\leftrightarrow$$ tautological intersections; Feynman graphs $$\leftrightarrow$$ knot invariants; admissible graphs $$\leftrightarrow$$ star products. Each dictionary turns a physics-inspired generating function into a proof.

For this course, Kontsevich is the portrait of mathematical physics as **theorem supply**, not as metaphor. The same graph-integral instinct appears three times, in three IMU clauses. Later programs (HMS, motives) show that the instinct did not stop in 1998; they do not rewrite the citation.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Kontsevich solved mirror symmetry.” | He proposed HMS in 1994; it is a program, with theorems in many cases by many authors. |
| “Fields 1998 = homological mirror symmetry.” | The third official bullet is formal quantization of Poisson manifolds. |
| “Witten’s conjecture classifies all curves.” | It constrains $$\psi$$-intersection numbers on $$\overline{\mathcal{M}}_{g,n}$$ via KdV. |
| “The Kontsevich integral is the Jones polynomial.” | It is a universal finite-type invariant; Jones is one of many specializations / extractions. |
| “Formal quantization is a Hilbert-space quantum mechanics.” | It is an associative deformation over $$\mathbb{R}[\![\hbar]\!]$$; analysis of convergence is separate. |
| “Motivic integration is a 1998 Fields result.” | Adjacent later work (Kontsevich lecture; Denef–Loeser). |

---

## Exercises

1. Write the 1998 citation from memory as three bullets. Which subject area is each bullet?
2. What is a $$\psi$$-class on $$\overline{\mathcal{M}}_{g,n}$$, at slogan level? Why does an intersection number need a compactification?
3. In the ribbon-graph proof, what is being identified with what? (Geometry of metrics / Strebel vs a matrix integral.)
4. What does **universal** mean for a Vassiliev invariant? Credit Vassiliev and Bar-Natan in your answer.
5. Write the first two axioms of a star product ($$ \hbar=0$$ limit; commutator vs Poisson). Why is the Poisson case harder than the symplectic case?
6. **Accuracy practice.** Take a sentence that says Kontsevich “proved mirror symmetry.” Replace it by two sentences: one about HMS 1994, one about the 1998 third bullet.
7. Skim the first two pages of arXiv:q-alg/9709040 or arXiv:alg-geom/9411018 (choose one) and list five keywords.
8. **Seminar stretch.** How does a “graph complex with configuration-space integrals” appear in *both* the knot invariant and the star product? One careful paragraph; do not invent a theorem that identifies them.

---

## Links

- IMU Fields Medal page: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Wikipedia — Maxim Kontsevich: [https://en.wikipedia.org/wiki/Maxim_Kontsevich](https://en.wikipedia.org/wiki/Maxim_Kontsevich)
- Kontsevich, deformation quantization (arXiv:q-alg/9709040): [https://arxiv.org/abs/q-alg/9709040](https://arxiv.org/abs/q-alg/9709040)
- Kontsevich, homological algebra of mirror symmetry (arXiv:alg-geom/9411018): [https://arxiv.org/abs/alg-geom/9411018](https://arxiv.org/abs/alg-geom/9411018)
- AMS Notices, “The Mathematical Work of the 1998 Fields Medalists”: [https://www.ams.org/notices/199901/fields.pdf](https://www.ams.org/notices/199901/fields.pdf)
- arXiv search — Kontsevich Witten moduli: [https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all](https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all)

---

## References

1. IMU Fields Medal 1998 citation — Maxim Kontsevich (ICM Berlin opening; see also Taubes, “The work of Maxim Kontsevich,” ICM 1998).
2. M. Kontsevich, “Intersection theory on the moduli space of curves and the matrix Airy function,” *Comm. Math. Phys.* 147 (1992).
3. E. Witten, two-dimensional gravity and intersection theory on moduli space (the conjecture).
4. M. Kontsevich, “Deformation quantization of Poisson manifolds,” *Lett. Math. Phys.* 66 (2003); preprint q-alg/9709040.
5. V. Vassiliev, finite-type knot invariants; D. Bar-Natan, weight systems and diagram complexes.
6. M. Kontsevich, “Homological algebra of mirror symmetry,” *Proc. ICM Zürich 1994* — related program, not the third 1998 bullet.
7. J. Denef and F. Loeser, papers on motivic integration (after Kontsevich’s Orsay lecture).
8. Course: [Mathematical Physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/), [Mirror Symmetry]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/).

---

## Further directions

- Read a modern exposition of tautological classes on $$\overline{\mathcal{M}}_{g,n}$$ to see what Witten–Kontsevich does *not* compute.
- If you continue to HMS, keep a two-column notebook: “1994 proposal” vs “theorems proved by later authors.”
