---
layout: post
title: "Donaldson’s Four-Manifolds and Exotic Smooth Structures (Fields Medal 1986)"
chapter: '02'
order: 32
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Simon Donaldson** received the **Fields Medal 1986**, in the standard IMU account,

> primarily for his work on the topology of four-manifolds, especially for showing that there is a differential structure on Euclidean four-space which is different from the usual structure.  
> — [IMU, Fields Medals 1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)

(The 1986 IMU page reproduces the Albers–Alexanderson–Reid congress history.) The sentence is right as a headline and incomplete as a proof credit. **Exotic smooth structures on $$\mathbb{R}^4$$**—manifolds homeomorphic to Euclidean four-space but not diffeomorphic to it—arise from a clash between two 1982–83 theorems: Michael Freedman’s topological classification of simply connected four-manifolds, and Donaldson’s gauge-theoretic constraints on **smooth** intersection forms. Freedman received a Fields Medal at the same Berkeley congress, for topological methods that include the four-dimensional Poincaré conjecture in the topological category. This essay treats the pair as a single 1986 event with two engines.

The engine on Donaldson’s side is **Yang–Mills gauge theory**: anti-self-dual connections (instantons) and the topology of their moduli spaces. The analytic infrastructure that makes those moduli spaces usable—compactness, bubbling, removable singularities—owes a central debt to Karen Uhlenbeck; see [Uhlenbeck / gauge theory]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/). **Seiberg–Witten theory** (Witten, 1994) is a later, different gauge-theoretic engine that simplified many four-manifold arguments; it is a descendant, not part of the 1986 medal. There is no dedicated “Donaldson–Seiberg–Witten” lesson in Chapter 6 of this course; the surrounding mathematical-physics culture is sketched in [Mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/). Donaldson did **not** classify all four-manifolds.

---

## Learning objectives

After this lecture you should be able to:

- Explain why dimension four is special: Whitney trick and high-dimensional surgery fail, while low-dimensional cut-and-paste is not enough.
- Define the **intersection form** of a closed oriented four-manifold as the pairing on $$H_2$$ (or $$H^2$$) given by algebraic intersection (or cup product).
- State **Donaldson’s theorem** (1983): a definite intersection form of a smooth, closed, oriented four-manifold is diagonalizable over $$\mathbb{Z}$$ (originally under a simply-connected hypothesis; later extended).
- Contrast that with **Freedman**: every unimodular symmetric bilinear form is realized by a simply connected **topological** four-manifold, and such manifolds are classified by the form plus a Kirby–Siebenmann bit in the odd case.
- Explain, at slogan level, how the clash produces (i) topological four-manifolds with **no smooth structure** and (ii) **exotic $$\mathbb{R}^4$$s**.
- Describe instanton moduli spaces as the geometric source of Donaldson’s constraints, and name Uhlenbeck compactness as analytic infrastructure.
- Place Seiberg–Witten (1994) as a later descendant, not as the 1986 work.
- Avoid the sentence “Donaldson classified all four-manifolds.”

**Prerequisites.** Smooth manifolds, homology and cup product at the level of a first algebraic topology course; the idea of a vector bundle and a connection. No prior gauge theory is assumed: treat a connection as a way to differentiate sections, and curvature as the failure of mixed partials to commute.

**Seminar links.** LO1 / LO4 (physics-inspired PDE as a topological machine; topological versus smooth categories). Pair with [Uhlenbeck]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/), [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) for a later geometric-analytic attack on three-manifolds, and [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/).

---

## 1. Why four dimensions are not “just one more $$n$$”

For $$n\ge 5$$, the high-dimensional surgery and $$h$$-cobordism theorems (Smale, and the topological work of Kirby–Siebenmann) give a classification machine: the homotopy type plus some algebraic $$K$$-theory and surgery obstructions largely determine the manifold in a given category. For $$n\le 3$$, geometrization and classical cut-and-paste dominate. Dimension four is the remaining battlefield. The Whitney trick, which needs room to cancel intersections, fails in the smooth category in dimension four; Casson handles and wildly embedded disks appear; and the smooth and topological categories **part company**.

The basic algebraic invariant of a closed oriented four-manifold $$X$$ is its **intersection form**

$$
Q_X: H_2(X;\mathbb{Z})/\mathrm{torsion}\times H_2(X;\mathbb{Z})/\mathrm{torsion}\to\mathbb{Z},
$$

the unimodular symmetric bilinear form given by algebraic intersection of surfaces (equivalently, cup product on $$H^2$$ evaluated on the fundamental class). By Poincaré duality the form is unimodular. Over $$\mathbb{R}$$ it is classified by rank and signature; over $$\mathbb{Z}$$ there are many more isomorphism types (the $$E_8$$ lattice is the emblematic even, definite, non-diagonalizable example).

Rohlin’s theorem already constrained **smooth** spin four-manifolds (signature divisible by $$16$$). Freedman and Donaldson turned the integral form into a near-complete topological classification and a severe smooth obstruction, respectively.

---

## 2. Freedman: topological four-manifolds

Michael Freedman, “The topology of four-dimensional manifolds,” *J. Differential Geom.* 17 (1982), proved that every unimodular symmetric bilinear form is realized as the intersection form of a closed simply connected **topological** four-manifold, and that in the even case the form determines the homeomorphism type; in the odd case there are two homeomorphism types, distinguished by the Kirby–Siebenmann invariant in $$\mathbb{Z}/2$$. As a corollary he proved the **four-dimensional Poincaré conjecture in the topological category**: a homotopy four-sphere is homeomorphic to $$S^4$$.

The constructions use Casson handles—infinite towers that are topologically standard but smoothly exotic in general. Freedman’s world is therefore larger than the smooth world: many forms appear topologically that cannot appear smoothly.

---

## 3. Donaldson’s theorem: definite forms, smoothly

Donaldson’s first shock, obtained while he was still a postgraduate student at Oxford (Hitchin, then Atiyah), is the 1983 theorem:

> If $$X$$ is a closed, oriented, smooth, simply connected four-manifold whose intersection form is definite, then that form is diagonalizable over the integers: equivalent to $$\langle\pm 1\rangle\oplus\cdots\oplus\langle\pm 1\rangle$$.

The paper is “An application of gauge theory to four-dimensional topology,” *J. Differential Geom.* 18 (1983), 279–315; a short announcement is “Self-dual connections and the topology of smooth 4-manifolds,” *Bull. Amer. Math. Soc.* 8 (1983). Atiyah’s ICM account famously said the work “stunned the mathematical world.” Later papers (including *J. Differential Geom.* 26 (1987) on orientations of moduli spaces) removed the simply-connected hypothesis in the form used today.

Combined with Freedman, the theorem immediately produces **non-smoothable topological four-manifolds**: take the simply connected topological manifold with intersection form $$E_8$$ (or $$E_8\oplus E_8$$). It exists topologically and cannot admit any smooth structure, because $$E_8$$ is definite and not diagonalizable.

The same clash, arranged at the ends of open four-manifolds rather than on closed ones, produces **exotic $$\mathbb{R}^4$$s**. Freedman’s topological embeddings and proper $$h$$-cobordism let one cap off pieces in the topological category; Donaldson’s constraints forbid the resulting open four-manifold from being diffeomorphic to standard $$\mathbb{R}^4$$ (for instance, it may contain a compact set not enclosed by any smoothly embedded $$S^3$$). Explicit early constructions appear in the same 1983 volume of the *Journal of Differential Geometry* (Gompf, “Three exotic $$\mathbf{R}^4$$’s and other anomalies”). Later work of Gompf, Taubes, and others produced infinitely many—indeed uncountably many—nondiffeomorphic smooth structures on the topological four-space. The IMU headline that Donaldson showed there is a nonstandard differential structure on Euclidean four-space is the public name of this **Donaldson + Freedman** phenomenon, not a claim that a single instanton moduli space is itself an exotic $$\mathbb{R}^4$$.

---

## 4. Instantons as topological tools

Let $$P\to X$$ be an $$\mathrm{SU}(2)$$ (or $$\mathrm{SO}(3)$$) principal bundle. A connection $$A$$ has curvature $$F_A$$. In dimension four the Hodge star sends two-forms to two-forms, and one can impose the **anti-self-dual** (ASD) equation $$F_A^+=0$$ (or the self-dual equation). Solutions of finite Yang–Mills energy

$$
\mathrm{YM}(A)=\int_X \lvert F_A\rvert^2
$$

are **instantons**. The space of such connections modulo gauge transformations is a **moduli space** $$\mathcal{M}$$. For a definite four-manifold with a suitable bundle, Donaldson showed that $$\mathcal{M}$$ can be compactified to a manifold-with-boundary (or a stratified space) whose boundary involves a copy of $$X$$ itself—energy bubbling off at points, in the model of the instanton moduli space on $$S^4$$, which is a five-ball with $$S^4$$ at infinity. That topological constraint on $$\mathcal{M}$$ forces the intersection form to be diagonalizable: a nonstandard definite form cannot occur.

**Uhlenbeck compactness** and **removable singularities** make $$\mathcal{M}$$ usable: bounded-energy sequences converge smoothly away from finitely many points, and small-energy isolated singularities fill in. See [Uhlenbeck]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/). Donaldson uses the compactified moduli space as a cobordism between $$X$$ and a model; Uhlenbeck guarantees the compactification. Freed–Uhlenbeck, *Instantons and Four-Manifolds* (1984), was the first-generation text. Later Donaldson polynomials (*Topology* 29 (1990)) distinguish smooth structures on a fixed topological four-manifold; that is a continuation, still not a classification of all four-manifolds.

---

## 5. Descendants that are not the medal

In 1994 Witten introduced the **Seiberg–Witten** monopole equations from $$N=2$$ supersymmetric gauge theory (“Monopoles and four-manifolds,” *Math. Res. Lett.* 1 (1994)), often easier to compute than Donaldson polynomials. Mention them as the next engine, not as the 1986 work, and do not invent a Chapter 6 path `Donaldson_Seiberg_Witten`. Donaldson’s later Hermitian–Einstein / DUY work, symplectic Lefschetz pencils, and the Chen–Donaldson–Sun Kähler–Einstein theorem for Fanos are a different chapter. The 1986 medal is four-manifold topology via ASD Yang–Mills.

Dimension four was expected to be hard; that Yang–Mills analysis would force “definite implies diagonalizable,” and that Freedman’s topological abundance would then yield non-smoothable manifolds and exotic $$\mathbb{R}^4$$s, was not. The 1986 class was Donaldson, Faltings (Mordell), and Freedman: arithmetic geometry; topological four-manifolds; smooth four-manifolds via gauge theory.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Donaldson classified all four-manifolds.” | He proved foundational constraints and later invariants. Classification remains open in the smooth category. |
| “Donaldson alone constructed exotic $$\mathbb{R}^4$$.” | Existence uses **Donaldson’s smooth constraints** together with **Freedman’s topological theory** (and early constructions of Gompf and others). |
| “Freedman’s Poincaré conjecture is the smooth one.” | Freedman proved the **topological** 4D Poincaré conjecture. The smooth 4D Poincaré conjecture remains open. |
| “Seiberg–Witten is the 1986 medal.” | Seiberg–Witten invariants appear in **1994**. |
| “Uhlenbeck compactness is a topological theorem.” | It is an **analytic** compactness/removable-singularities theorem that topology then uses. |
| “Exotic $$\mathbb{R}^4$$ contradicts the uniqueness of $$\mathbb{R}^n$$ for $$n\neq 4$$.” | For $$n\neq 4$$, Euclidean space has a unique smooth structure; dimension four is the exception. |

---

## Exercises

1. What does it mean for a bilinear form over $$\mathbb{Z}$$ to be **unimodular**? Why does Poincaré duality give that for $$Q_X$$?
2. State Donaldson’s definite-form theorem and Freedman’s realization theorem. Deduce, in three sentences, that a topological $$E_8$$-manifold cannot be smoothed.
3. Why is “homeomorphic but not diffeomorphic to $$\mathbb{R}^4$$” possible only after one has **both** a topological flexibility and a smooth rigidity?
4. Instanton moduli in one paragraph: ASD equation, gauge quotient, bubbling at points, compactification involving $$X$$. What topological conclusion is drawn for definite $$X$$?
5. Credit practice: one accurate clause each for **Donaldson**, **Freedman**, **Uhlenbeck**, **Witten (1994)**.
6. The smooth four-dimensional Poincaré conjecture is open. How does that differ from Freedman’s theorem?
7. **Accuracy practice.** Rewrite “Donaldson found a weird smooth $$\mathbb{R}^4$$ by solving Yang–Mills” as two sentences this course would accept.
8. **Seminar stretch.** Compare this 1986 gauge-theory story with [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/): Ricci flow in dimension three versus instantons in dimension four. What is being compactified or degenerated in each?

---

## Links

- IMU Fields Medals 1986: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)
- Wikipedia: [Simon Donaldson](https://en.wikipedia.org/wiki/Simon_Donaldson); [Exotic $$\mathbb{R}^4$$](https://en.wikipedia.org/wiki/Exotic_R4); [Donaldson’s theorem](https://en.wikipedia.org/wiki/Donaldson%27s_theorem)
- Course: [Uhlenbeck / gauge]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/), [Mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/), [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/)
- arXiv search (later Donaldson work; the 1983 papers predate arXiv): [Donaldson four-manifold](https://arxiv.org/search/?query=Donaldson+four-manifold+instanton&searchtype=all)

---

## References

1. International Mathematical Union, Fields Medals 1986 account of Simon K. Donaldson (Albers–Alexanderson–Reid / IMU page).
2. **S. K. Donaldson**, “An application of gauge theory to four-dimensional topology,” *J. Differential Geom.* 18 (1983), 279–315.
3. **M. H. Freedman**, “The topology of four-dimensional manifolds,” *J. Differential Geom.* 17 (1982), 357–453.
4. **R. Gompf**, “Three exotic $$\mathbf{R}^4$$’s and other anomalies,” *J. Differential Geom.* 18 (1983), 317–328.
5. **S. K. Donaldson and P. B. Kronheimer**, *The Geometry of Four-Manifolds*, Oxford, 1990.
6. **D. S. Freed and K. K. Uhlenbeck**, *Instantons and Four-Manifolds*, Springer, 1984; course essay [Uhlenbeck]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/).
7. **E. Witten**, “Monopoles and four-manifolds,” *Math. Res. Lett.* 1 (1994), 769–796. (Descendant, not the 1986 medal.)
8. Wikipedia, [Simon Donaldson](https://en.wikipedia.org/wiki/Simon_Donaldson), [Exotic R4](https://en.wikipedia.org/wiki/Exotic_R4).

---

## Further directions

- Read Atiyah’s ICM 1986 laudation, then Donaldson–Kronheimer Chapter 1; after the Uhlenbeck essay, note why bubbling is a feature (it produces $$\partial\mathcal{M}$$).
- Seminar prompt: what would a classification of smooth simply connected four-manifolds still need beyond intersection forms?
