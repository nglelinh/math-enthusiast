---
layout: post
title: "Elon Lindenstrauss: Measure Rigidity and Number Theory (Fields Medal 2010)"
chapter: '02'
order: 23
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Elon Lindenstrauss** received the **Fields Medal 2010** “for his results on measure rigidity in ergodic theory, and their applications to number theory.” The medal does not name a single closed Diophantine equation. It names a method: classify invariant measures for diagonalizable actions on homogeneous spaces so tightly that arithmetic questions—how well two irrationals can be approximated at once, how eigenfunctions of the Laplacian spread on an arithmetic surface—become theorems about those measures.

This essay is for learners who have seen orbits of a map or a group action and want the architecture of **homogeneous dynamics**. It does **not** claim that Littlewood’s conjecture is proved, nor that Lindenstrauss worked alone. It explains slogans carefully: rigidity of measures versus rigidity of orbits, positive entropy as a hypothesis, Hausdorff dimension zero as a statement about exceptions, and how a Fields-level program rearranges what “typical invariant measure” means.

---

## Learning objectives

After this lecture you should be able to:

- State **measure rigidity** in one paragraph: few invariant probability measures exist for a given action, and those that exist are algebraically special.
- Distinguish **unipotent** rigidity (Ratner) from **diagonalizable / Cartan** rigidity, where entropy hypotheses appear.
- Write Littlewood’s conjecture and explain what Einsiedler–Katok–Lindenstrauss actually proved about its exceptional set.
- Describe **arithmetic quantum unique ergodicity** as equidistribution of $$|\phi_j|^2$$ for Hecke eigenfunctions, not as a slogan that “quantum chaos is solved.”
- Attribute credit carefully: Furstenberg, Margulis, Ratner, Katok, Einsiedler, and the later non-compact complementary work on QUE.

**Prerequisites.** Linear algebra of $$\mathrm{SL}_n$$; the idea of a probability measure and of weak-* convergence; continued fractions or $$\|x\|=\mathrm{dist}(x,\mathbb{Z})$$ at slogan level. No prior ergodic theory course required.

**Seminar links.** LO1 / LO4 (hard programs; classical approximation ↔ modern rigidity). Pair with [Avila]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/) for a *typicality* culture in one-dimensional dynamics, [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/) for homogeneous dynamics as a number-theoretic language, and [Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/) for the Abel lineage that made invariant measures a tool of arithmetic.

---

## 1. Why measures, not only orbits

A first course in dynamics often follows a single orbit: is it periodic, dense, equidistributed? Homogeneous dynamics follows a **group** $$G$$ acting on a quotient $$X=\Gamma\backslash G$$ or $$G/\Gamma$$, typically with $$\Gamma$$ an arithmetic lattice such as $$\mathrm{SL}_n(\mathbb{Z})$$. Orbits of unipotent or diagonal subgroups become Diophantine problems in disguise.

**Measure rigidity** asks a sharper question than density. Which **probability measures** $$\mu$$ on $$X$$ are invariant under a prescribed subgroup $$A\subset G$$? If the only such measures are the obvious algebraic ones—Haar measure on a closed orbit of a larger group—then time averages along $$A$$-orbits cannot wander. Arithmetic corollaries follow because many counting and approximation problems are recoded as statements about those averages.

**Slogan.** Classify the measures, and the orbits that carry them become less mysterious.

---

## 2. History of the idea

Three laboratories prepared the ground.

**Furstenberg** showed that unique ergodicity and disjointness could force arithmetic structure: the famous $$\times 2,\times 3$$ action on the circle has a rigidity flavour that later higher-rank theorems echo. **Margulis** turned homogeneous dynamics into a machine for number theory, notably through the Oppenheim conjecture on values of indefinite quadratic forms. **Ratner** classified measures and orbit closures for **unipotent** flows: once a unipotent one-parameter group preserves $$\mu$$, $$\mu$$ is algebraic.

Diagonalizable actions are different. A higher-rank Cartan subgroup—diagonal matrices acting on

$$
X_3=\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})
$$

by left multiplication—need not be unipotent. Unique ergodicity can fail; singular measures may exist. Furstenberg and Margulis conjectured that, even so, invariant measures for higher-rank diagonal actions should still be scarce. Lindenstrauss’s contribution, as the 2010 IMU text emphasizes, was to establish this **under a positive-entropy hypothesis**, jointly with Einsiedler and Katok, and then to push the same circle of ideas into quantum unique ergodicity.

**Do not write** “Lindenstrauss invented homogeneous dynamics.” He made **measure rigidity for diagonal actions** a portable arithmetic machine.

---

## 3. Littlewood: a theorem about exceptions, not a closed conjecture

Littlewood asked whether every pair of real numbers $$\alpha,\beta$$ satisfies

$$
\liminf_{n\to\infty}\, n\,\|n\alpha\|\,\|n\beta\|=0.
$$

The conjecture is still open. What Einsiedler–Katok–Lindenstrauss proved (Annals of Mathematics, 2006) is a **dimension statement**: the set of exceptional pairs $$(\alpha,\beta)$$, if nonempty, has **Hausdorff dimension zero**. In homogeneous language, bad approximation corresponds to $$A$$-invariant measures on $$X_3$$ that refuse to be Haar measure on the whole space; positive entropy plus rigidity leaves too little room for a large exceptional set.

**Accuracy.** “The exceptions form a zero-dimensional set” is not “there are no exceptions.” A popular sentence that says Lindenstrauss “proved Littlewood” should be rewritten before it enters a seminar.

The same entropy-plus-rigidity package applies to other Diophantine problems. The medal citation is explicit that the impact “goes far beyond ergodic theory,” but the engine remains classification of measures.

---

## 4. Arithmetic quantum unique ergodicity

Rudnick and Sarnak asked how high-frequency eigenfunctions of the Laplacian spread on an **arithmetic** hyperbolic surface. If $$\phi_j$$ is a Hecke eigenfunction with eigenvalue $$\lambda_j\to\infty$$, does the probability measure $$|\phi_j|^2\,\mathrm{dvol}$$ become equidistributed with respect to hyperbolic volume? That is **arithmetic quantum unique ergodicity (QUE)**.

Lindenstrauss proved arithmetic QUE for **compact** arithmetic hyperbolic surfaces, by showing that quantum limits are $$A$$-invariant measures of a rigid type and then ruling out the non-volume possibilities in that compact arithmetic setting. The argument uses Hecke operators as extra symmetries that manufacture invariance and entropy.

**Accuracy.** The non-compact modular surface $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$ required complementary work (notably Holowinsky–Soundararajan for holomorphic forms, and further arguments for Maass forms). Do not collapse the whole QUE landscape into a single 2006 paper, and do not say that “quantum chaos is classified.”

**Slogan.** QUE is equidistribution of $$|\phi_j|^2$$. The rigidity theorem is about which measures can arise as limits.

---

## 5. Typicality versus rigidity

[Avila’s 2014 medal]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/) often celebrates **almost every** parameter: typical one-dimensional maps are regular or stochastic. Lindenstrauss’s culture is complementary. One wants **all** invariant measures—or all measures with a little entropy—to be algebraic. Typicality asks how large a good set is. Rigidity asks how small the zoo of measures can be forced to become.

[Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/) sits in the same homogeneous city with a different errand: subconvexity, sparse equidistribution, and topology of locally symmetric spaces. The Abel pairing of [Furstenberg and Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/) is the cultural preface: after them, a number theorist may treat an invariant measure as a legitimate arithmetic object. Lindenstrauss is a Fields-era chapter of that preface.

---

## 6. Why a Fields Medal

Three interlocking reasons:

1. **Difficulty.** Diagonalizable rigidity lacks Ratner’s unipotent classification; entropy, arithmetic symmetries, and delicate recurrence must replace it.
2. **Centrality.** Once measures on $$\mathrm{SL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{Z})$$ are classified even partially, Diophantine approximation and QUE become part of one conversation.
3. **Clarity of slogan with depth of method.** “Exceptions to Littlewood have dimension zero” is a sentence a graduate student can remember; the proofs are monuments of contemporary ergodic theory.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Lindenstrauss proved Littlewood’s conjecture.” | EKL proved that exceptions have Hausdorff dimension zero; the full conjecture remains open. |
| “Measure rigidity is the same as Ratner’s theorem.” | Ratner treats unipotent flows; the medal highlights higher-rank diagonal actions, often with entropy. |
| “QUE says every eigenfunction is uniformly distributed.” | Arithmetic QUE concerns Hecke eigenfunctions and weak-* limits of $$|\phi_j|^2$$, in specified geometric settings. |
| “Lindenstrauss invented ergodic methods in number theory.” | Furstenberg, Margulis, and Ratner built the culture; he advanced diagonal rigidity and its arithmetic payoffs. |
| “Dimension zero means the exceptional set is empty.” | A set can be nonempty and still have Hausdorff dimension zero (for instance, a countable set). |

---

## Exercises

1. In your own words: what does a rigidity theorem **forget** and **retain** about an invariant measure?
2. Write Littlewood’s conjecture in one display formula. Then write, in two sentences, the EKL theorem about exceptions.
3. Why might **positive entropy** be a natural extra hypothesis for diagonal actions but not for unipotent ones?
4. Distinguish QUE from “the eigenfunctions themselves converge.” What object is actually claimed to equidistribute?
5. **Accuracy practice.** Find a popular sentence that says Lindenstrauss “solved Littlewood.” Rewrite it in two precise sentences.
6. **Seminar stretch.** Compare [Avila’s typicality]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/) with Lindenstrauss rigidity: when would you rather know almost-every behavior, and when would you rather classify all invariant measures?

---

## Video sources and reading

1. **IMU citation** — Fields Medals 2010, Elon Lindenstrauss: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010).
2. **ICM 2010 laudatio text** — [IMU archive](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-elon-lindenstrauss.html).
3. **Orientation** — Princeton announcement: [Lindenstrauss wins the Fields Medal](https://www.princeton.edu/news/2010/08/20/lindenstrauss-wins-prestigious-fields-medal-mathematics-work).

**Status reminder:** Measure rigidity with arithmetic applications—**not** a complete proof of Littlewood, and not a classification of all quantum limits on every hyperbolic surface.

---

## References

1. IMU Fields Medal 2010 citation — Elon Lindenstrauss (mathunion.org).
2. **M. Einsiedler, A. Katok, E. Lindenstrauss**, Invariant measures and the set of exceptions to Littlewood’s conjecture, *Ann. of Math.* **164** (2006).
3. **E. Lindenstrauss**, Invariant measures and arithmetic quantum unique ergodicity, *Ann. of Math.* **163** (2006).
4. Surveys of homogeneous dynamics (Einsiedler–Lindenstrauss; Margulis; Ratner’s theorems as background).
5. Course neighbors: [Avila]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/), [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/), [Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/).

---

## Further directions

- Read a careful survey of Ratner’s theorems and list three ingredients that fail for diagonal actions.
- Compare Furstenberg’s $$\times 2,\times 3$$ rigidity with higher-rank Cartan rigidity: what is analogous, and what is new?
- Seminar A3 option: one page on what remains open in Littlewood and in QUE on non-arithmetic surfaces—without claiming the medal closed Diophantine approximation.
