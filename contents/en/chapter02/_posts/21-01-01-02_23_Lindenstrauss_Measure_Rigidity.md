---
layout: post
title: "Lindenstrauss’s Measure Rigidity (Fields Medal 2010)"
chapter: '02'
order: 23
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Elon Lindenstrauss** received the **Fields Medal 2010**

> “for his results on measure rigidity in ergodic theory, and their applications to number theory.”
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

**Measure rigidity** is the slogan that a group action which looks a priori chaotic often admits **very few** invariant probability measures—and that those few measures are algebraic (Haar measure on a closed orbit, Lebesgue on a subtorus). Once the measures are classified, equidistribution theorems and Diophantine statements become corollaries. Lindenstrauss’s medal recognizes a body of such classifications for **higher-rank diagonalizable actions**, and two celebrated exports: a Hausdorff-dimension-zero theorem for exceptions to **Littlewood’s conjecture** (with Einsiedler and Katok), and **arithmetic quantum unique ergodicity** for compact arithmetic hyperbolic surfaces (in the Hecke–Maass setting of Rudnick–Sarnak).

This essay does **not** say that Littlewood’s conjecture is fully proved. It does **not** treat quantum unique ergodicity as a theorem about every hyperbolic surface. It places Lindenstrauss in a landscape already shaped by Furstenberg, Margulis, Ratner, Katok, Einsiedler, and Host–Kra.

---

## Learning objectives

After this lecture you should be able to:

- Define measure rigidity as “scarce invariant measures, typically algebraic,” and contrast it with the abundance of measures for a single hyperbolic toral automorphism.
- Distinguish **unipotent** rigidity (Ratner’s theorems) from **diagonal / higher-rank** rigidity (Furstenberg-type problems; Einsiedler–Katok–Lindenstrauss).
- State Littlewood’s conjecture and the EKL theorem: it holds except possibly on a set of **Hausdorff dimension zero**.
- State arithmetic QUE for compact arithmetic hyperbolic surfaces (Hecke–Maass), credit Rudnick–Sarnak for the conjecture, and describe Soundararajan’s role on the non-compact modular surface (no escape of mass).
- Name Furstenberg, Margulis, Ratner, Katok, Einsiedler, and Host–Kra as landscape, not as a single school with one theorem.
- Connect the story to the Abel-level dynamics culture in [Chapter 8]({{ site.baseurl }}/contents/en/chapter08/) without claiming the Abel prize is the Fields prize.

**Prerequisites.** Group actions; the idea of an invariant measure and of ergodicity; hyperbolic geometry of the upper half-plane at slogan level ($$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$). Homogeneous spaces $$\Gamma\backslash G$$ as “lattices acting on Lie groups” can be taken as a picture rather than a theory.

**Seminar links.** [Furstenberg & Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/) for the Abel 2020 worldview (dynamics as a tool for number theory). [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) for a different ergodic-to-arithmetic export. [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/) for homogeneous dynamics in a later Fields portrait.

---

## 1. Ergodic theory as a classification machine

A measure-preserving action of a group $$H$$ on a probability space $$(X,\mu)$$ is **ergodic** if every invariant measurable set is trivial. Ergodic theory studies averages along orbits. **Measure rigidity** studies a prior question: *which* measures $$\mu$$ can be invariant in the first place?

For a single hyperbolic toral automorphism—say $$x\mapsto 2x$$ on $$\mathbb{R}/\mathbb{Z}$$—invariant measures are plentiful: Lebesgue, Dirac at $$0$$, and a zoo of fractal measures supported on Cantor sets. There is no hope of listing them all. Rigidity appears when the action is richer: several commuting maps, or a unipotent flow, or a higher-rank diagonal subgroup of a Lie group. Extra invariance can force $$\mu$$ to be algebraic.

Furstenberg’s $$\times 2,\times 3$$ problem is the model conjecture of this type: the only nonatomic probability measure on the circle invariant under both $$x\mapsto 2x$$ and $$x\mapsto 3x$$ should be Lebesgue. The problem is still open in full; partial results (Rudolph, Johnson, Host, …) already show that positive entropy plus extra invariance is a powerful constraint. Host–Kra later classified the structural factors of multiple ergodic averages, revealing nilsystems as the characteristic obstructions—another rigidity theorem in the same culture, not a lemma in Lindenstrauss’s papers.

Lindenstrauss’s contribution is to push this culture onto **homogeneous spaces** $$\Gamma\backslash G$$, where $$G$$ is a Lie group or an adelic group, and to extract number theory.

---

## 2. Unipotent versus diagonal

**Ratner’s theorems** (1990s) classified orbit closures and invariant measures for **unipotent** flows on homogeneous spaces. Unipotent elements (think of strictly upper-triangular matrices) have polynomial orbits; the classification is complete and algebraic. Margulis’s work on unipotent flows and Oppenheim’s conjecture is the celebrated arithmetic ancestor: once orbit closures are understood, values of indefinite quadratic forms at integers become dense.

**Diagonal** actions are different. A split torus—positive diagonal matrices acting by left multiplication on, say, $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$—is **higher rank** when the torus has dimension at least two. Orbits are exponential, not polynomial. There is no Ratner theorem in the same generality. Furstenberg and Margulis formulated conjectures that invariant measures for such actions should still be scarce. The technical price is extra hypotheses: positive entropy, recurrence in extra directions, compatibility with Hecke correspondences.

**Einsiedler–Katok–Lindenstrauss** (Annals of Mathematics, 2006) proved a measure-classification theorem for higher-rank diagonal actions under a **positive entropy** assumption: an ergodic invariant measure with positive entropy (for some element of the torus) is algebraic. IMU’s 2010 laudation states that this established a Furstenberg–Margulis-type conjecture under that extra hypothesis. Positive entropy is not cosmetic; it rules out the most degenerate fractal measures.

The pedagogical contrast:

| Culture | Typical actor | Classification | Arithmetic export |
|---------|---------------|----------------|-------------------|
| Ratner / Margulis unipotent | Unipotent one-parameter groups | Complete, algebraic | Oppenheim, many others |
| Diagonal higher rank | Split tori, $$\times 2\times 3$$ | Partial; entropy hypotheses | Littlewood-type Diophantine |

Lindenstrauss works on the second row, using entropy, recurrence, and sometimes adelic extra symmetries.

---

## 3. Littlewood’s conjecture, almost

**Littlewood’s conjecture** (1930s) asks whether every pair of real numbers $$(\alpha,\beta)$$ satisfies

$$
\liminf_{n\to\infty}\, n\,\|n\alpha\|\,\|n\beta\|=0,
$$

where $$\|\cdot\|$$ is distance to the nearest integer. Equivalently: can one always find integers $$n$$ making $$n\alpha$$ and $$n\beta$$ *simultaneously* unusually close to integers, with a product bound that improves on Dirichlet? The conjecture is still **open**.

The homogeneous-dynamics translation (Cassels, Swinnerton-Dyer, and later the modern school) realizes exceptional $$(\alpha,\beta)$$ as points whose diagonal orbits on a space of lattices stay away from the cusp in a controlled way. If every invariant measure of the relevant torus action is Haar on a closed orbit, exceptions cannot accumulate.

**Einsiedler–Katok–Lindenstrauss** deduced that the set of exceptions has **Hausdorff dimension zero**. Almost every pair (in a very strong fractal sense) satisfies Littlewood; any counterexample set is thinner than every positive-dimensional subset of the plane. That is a theorem. It is not a proof of Littlewood’s conjecture. Popular summaries that say “Littlewood is solved” are wrong.

---

## 4. Arithmetic quantum unique ergodicity

A Maass form on a hyperbolic surface $$M=\Gamma\backslash\mathbb{H}$$ is an $$L^2$$ eigenfunction of the Laplace–Beltrami operator. The measures

$$
\mu_\phi=\lvert\phi\rvert^2\,d\mathrm{vol}
$$

describe how the mass of a high-energy eigenfunction sits on $$M$$. **Quantum ergodicity** (Šnirel’man, Zelditch, Colin de Verdière) says that *almost all* such measures equidistribute toward volume, on compact manifolds of negative curvature. **Quantum unique ergodicity (QUE)**, conjectured by **Rudnick–Sarnak** (1994), asks whether *every* sequence of eigenfunctions equidistributes—no exceptional scarring.

On arithmetic surfaces one has extra Hecke operators. Restricting to joint eigenfunctions (Hecke–Maass forms) is **arithmetic QUE**. It is expected that the Laplacian spectrum is simple, so the Hecke condition would be automatic; that simplicity is not known.

**Lindenstrauss** (*Invariant measures and arithmetic quantum unique ergodicity*, Annals of Mathematics, 163, 2006) proved arithmetic QUE for **compact** arithmetic hyperbolic surfaces: the only arithmetic quantum limit is normalized volume. The proof classifies measures on an extended space $$\Gamma\backslash\mathrm{SL}(2,\mathbb{R})\times L$$ that are invariant under a diagonal flow, have positive entropy, and are recurrent in the extra (Hecke / adelic) directions; microlocal lifts of Hecke–Maass mass measures produce such objects.

For **non-compact** congruence surfaces, including the modular surface $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$, the same method shows that any arithmetic quantum limit is $$c$$ times volume for some $$c\in[0,1]$$. Mass might escape into the cusp. **Kannan Soundararajan** (*Quantum unique ergodicity for $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$*, Annals, 2010) ruled out escape of mass for Hecke–Maass forms on the modular surface; combined with Lindenstrauss, this proves arithmetic QUE there. Earlier joint work of Bourgain–Lindenstrauss supplied entropy bounds used in the program.

**Holomorphic** Hecke eigenforms are a parallel QUE problem. **Holowinsky–Soundararajan** (Annals, 2010) proved QUE for holomorphic Hecke cusp forms on the modular surface by analytic number theory, not by measure rigidity. Do not attribute that theorem to Lindenstrauss.

QUE for general (non-arithmetic) compact hyperbolic surfaces remains open.

---

## 5. A landscape of names

| Name | Role in this story |
|------|---------------------|
| Furstenberg | $$\times 2,\times 3$$ and the idea that extra commuting maps rigidify measures; multiple recurrence |
| Margulis | Superrigidity, arithmeticity, unipotent flows, Oppenheim; conjectural diagonal rigidity |
| Ratner | Classification for unipotent flows—the completed sibling of the diagonal problem |
| Katok | Entropy, rigidity, and the EKL collaboration |
| Einsiedler | EKL and later homogeneous dynamics with Lindenstrauss and others |
| Host–Kra | Structure of multiple averages / nilfactors—the broader ergodic rigidity culture |
| Rudnick–Sarnak | QUE conjecture |
| Soundararajan | No escape of mass on $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$; holomorphic QUE with Holowinsky |
| Bourgain | Entropy of quantum limits (with Lindenstrauss) |

Lindenstrauss (born 1970) wrote a 1999 PhD at the Hebrew University with Benjamin Weiss. He was a Clay long-term prize fellow (2003–2005), taught at Princeton, returned to Jerusalem, and in 2024 joined the permanent faculty of the Institute for Advanced Study. He was the first Israeli Fields medalist. Biography is not the theorem; the theorem is the scarcity of measures.

---

## 6. Why a Fields Medal

IMU’s 2010 text emphasizes two exports—Littlewood-type Diophantine approximation and arithmetic QUE—and the depth of the underlying classification. The medal is not “a conjecture closed.” Littlewood is not closed. QUE is closed in the arithmetic compact case and, with Soundararajan, on the modular surface for Hecke–Maass forms. What is closed is a **method**: entropy plus extra invariance plus homogeneous dynamics as a machine that manufactures arithmetic theorems.

For this course, Lindenstrauss is the Fields-scale counterpart of the Abel story in [Chapter 8]({{ site.baseurl }}/contents/en/chapter08/): dynamics as number theory’s hidden algebra. The prizes differ; the culture is shared.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Littlewood’s conjecture is proved.” | EKL: exceptions have Hausdorff dimension zero. The full statement is open. |
| “QUE is proved for all hyperbolic surfaces.” | Arithmetic Hecke–Maass, compact case (Lindenstrauss); modular surface with Soundararajan; general QUE is open. |
| “Lindenstrauss proved holomorphic QUE.” | Holowinsky–Soundararajan, by other methods. |
| “Measure rigidity is Ratner’s theorem.” | Ratner is the unipotent chapter; diagonal higher-rank is a different, partial chapter. |
| “Positive entropy is a minor extra assumption.” | It is the hypothesis that kills the most pathological invariant measures. |
| “Fields 2010 is the same as Abel 2020.” | Abel 2020 honors Furstenberg and Margulis’s lifetime use of dynamics; Lindenstrauss is a later Fields-scale implementation. |

---

## Exercises

1. In one paragraph, what is an invariant measure, and why might *classifying* them be harder than proving a single ergodic theorem?
2. Contrast unipotent flows with diagonal torus actions in three slogans: orbit shape, status of classification, typical arithmetic corollary.
3. Write Littlewood’s conjecture. Write the EKL conclusion. Circle the words that must not be deleted (“except possibly,” “Hausdorff dimension zero”).
4. What extra structure makes QUE *arithmetic*? Why does compactness remove the escape-of-mass issue that Soundararajan later treated?
5. Why does Rudnick–Sarnak QUE not follow from quantum ergodicity (Šnirel’man–Zelditch–Colin de Verdière)?
6. **Accuracy practice.** Rewrite “an Israeli mathematician solved Littlewood and quantum chaos” as three precise sentences.
7. Skim the abstract of Lindenstrauss, Annals 163 (2006), or of EKL, Annals 164 (2006), and list the hypotheses you would need to look up next (entropy, recurrence, congruence lattice, microlocal lift).
8. **Seminar stretch.** Compare Furstenberg’s $$\times 2,\times 3$$ problem with EKL: same rigidity instinct, different groups. What is still open in the circle case?

---

## Links

- IMU Fields Medals 2010: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- IMU ICM 2010 laudation (Lindenstrauss): [https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-elon-lindenstrauss.html](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-elon-lindenstrauss.html)
- Wikipedia — Elon Lindenstrauss: [https://en.wikipedia.org/wiki/Elon_Lindenstrauss](https://en.wikipedia.org/wiki/Elon_Lindenstrauss)
- IAS announcement (2024 faculty): [https://www.ias.edu/news/three-world-leading-mathematicians-join-ias-faculty](https://www.ias.edu/news/three-world-leading-mathematicians-join-ias-faculty)
- Soundararajan, QUE for the modular surface (arXiv:0901.4060): [https://arxiv.org/abs/0901.4060](https://arxiv.org/abs/0901.4060)
- arXiv search — Einsiedler Katok Lindenstrauss Littlewood: [https://arxiv.org/search/?query=Einsiedler+Katok+Lindenstrauss+Littlewood&searchtype=all](https://arxiv.org/search/?query=Einsiedler+Katok+Lindenstrauss+Littlewood&searchtype=all)
- AMS Notices survey of the 2010 Fields medals: [https://www.ams.org/notices/201103/rtx110300453p.pdf](https://www.ams.org/notices/201103/rtx110300453p.pdf)

---

## References

1. IMU Fields Medal 2010 citation — Elon Lindenstrauss.
2. M. Einsiedler, A. Katok, and E. Lindenstrauss, “Invariant measures and the set of exceptions to Littlewood’s conjecture,” *Ann. of Math.* 164 (2006).
3. E. Lindenstrauss, “Invariant measures and arithmetic quantum unique ergodicity,” *Ann. of Math.* 163 (2006).
4. Z. Rudnick and P. Sarnak, “The behaviour of eigenstates of arithmetic hyperbolic manifolds,” *Comm. Math. Phys.* 161 (1994) — QUE conjecture.
5. K. Soundararajan, “Quantum unique ergodicity for $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$,” *Ann. of Math.* 172 (2010).
6. R. Holowinsky and K. Soundararajan, “Mass equidistribution for Hecke eigenforms,” *Ann. of Math.* 172 (2010) — holomorphic QUE, different methods.
7. M. Ratner, measure and orbit classification for unipotent flows; H. Furstenberg, $$\times 2,\times 3$$ and disjointness; G. Margulis, unipotent flows and Oppenheim.
8. B. Host and B. Kra, structure theorem for multiple ergodic averages (nilfactors).
9. Course: [Furstenberg & Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/), [Chapter 8 overview]({{ site.baseurl }}/contents/en/chapter08/), [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/).

---

## Further directions

- Read a short exposition of Ratner’s theorem before EKL, so the missing diagonal classification is felt as a gap rather than as a synonym.
- Seminar option: a one-page status sheet “Littlewood after EKL” that lists what a full proof would still need—without inventing one.
