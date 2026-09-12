---
layout: post
title: "Curtis McMullen: Holomorphic Dynamics and Geometrization (Fields Medal 1998)"
chapter: '02'
order: 25
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Curtis T. McMullen** received the **Fields Medal 1998** “for his contributions to the theory of holomorphic dynamics and geometrization of three-manifolds, including proofs of Bers’ conjecture on the density of cusp points in the boundary of the Teichmüller space, and Kra’s theta-function conjecture.” The medal names a bridge: iteration of holomorphic maps, the geometry of Teichmüller space, and hyperbolic structures on three-manifolds share a renormalization language.

This essay is for learners who have seen a quadratic polynomial $$z\mapsto z^2+c$$ and a surface of genus $$g\ge 2$$ and want the architecture of late-1990s complex dynamics. It does **not** claim that the Mandelbrot set is locally connected (MLC remains open), nor that McMullen finished Thurston’s geometrization program. It explains slogans carefully: quadratic-like maps, cusp density on a Bers boundary, the Poincaré theta operator, and how a Fields-level rigidity theorem rearranges several laboratories at once.

---

## Learning objectives

After this lecture you should be able to:

- State McMullen’s 1998 citation in one careful paragraph, naming holomorphic dynamics, geometrization, Bers, and Kra.
- Explain a **quadratic-like map** (Douady–Hubbard) as a holomorphic degree-two branched cover that behaves like $$z^2+c$$ after straightening.
- Describe **Bers’ conjecture** at slogan level: cusp (geometrically finite) points are dense in the boundary of a Teichmüller / Bers compactification.
- Describe **Kra’s theta-function conjecture** as a strict contraction of the Poincaré series operator on quadratic differentials.
- Keep **MLC** labeled open, and locate McMullen next to [Avila]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/) and [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) without collapsing the three medals into one story.

**Prerequisites.** Holomorphic functions of one variable; iteration of polynomials at the level of Julia and Fatou sets as names; the idea that a hyperbolic surface has a Teichmüller space of marked metrics. No prior Kleinian-group course required.

**Seminar links.** LO1 / LO4 (hard programs; classical iteration ↔ moduli geometry). Pair with [Avila]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/) for later renormalization typicality, [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) for dynamics *on* moduli space, and [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) only as a *different* geometrization chapter (Ricci flow), not as McMullen’s method.

---

## 1. Why complex iteration needed moduli

A first course in complex dynamics studies a single map $$f(z)=z^2+c$$, its Julia set, and the Mandelbrot set $$M$$ of parameters whose critical orbit stays bounded. That is the right starting point. It is the wrong ending point for the theory that earned a Fields Medal.

Modern holomorphic dynamics is frequently a theory of **maps that look quadratic after a change of coordinates**. Douady and Hubbard isolated **quadratic-like maps**: holomorphic degree-two branched covers $$f:U\to V$$ between simply connected plane domains, with $$\overline{U}$$ compact in $$V$$. Their **straightening theorem** sends such an $$f$$ to a genuine quadratic polynomial, provided the critical orbit does not escape. Renormalization—restrict, return, rescale—then produces a new quadratic-like map from an old one.

McMullen, building on Sullivan, Douady–Hubbard, and the emerging geometric theory of renormalization, treated that operator as a source of **rigidity**: when an infinitely renormalizable map sits in a suitable class, its geometry at small scales is controlled, and nearby maps cannot deform too freely. That rigidity travels. The same small-scale analysis informs Kleinian groups and hyperbolic three-manifolds that fiber over the circle.

**Slogan.** Dynamics of maps becomes geometry **on** a space of maps—and then geometry of three-manifolds.

---

## 2. Bers’ conjecture: cusps on the boundary

Teichmüller space $$\mathcal{T}(S)$$ parametrizes marked hyperbolic metrics (or complex structures) on a surface $$S$$ of finite type. Bers compactified pieces of this space using quasi-Fuchsian hyperbolic three-manifolds whose conformal boundary consists of two Riemann surfaces. The **Bers boundary** contains many points that correspond to degenerate groups.

A **cusp** point, in the sense of the citation, is a geometrically finite degeneration: a Kleinian group that has acquired parabolic elements, like a hyperbolic surface developing a puncture. **Bers’ conjecture**—proved by McMullen—asserts that such cusp points are **dense** in the relevant boundary of Teichmüller space.

**What this rearranges.** The boundary is no longer a private museum of exotic limits. Geometrically finite, understandable degenerations sit densely among the wilder ones. Density is not a classification of every boundary point; it is a statement that the “tame” points are thick in the topological sense.

---

## 3. Kra’s theta-function conjecture

Let $$X$$ be a hyperbolic Riemann surface of finite area, with universal cover $$\mathbb{H}\to X$$ and covering group $$G$$. Holomorphic quadratic differentials of finite norm form Banach spaces $$Q(\mathbb{H})$$ and $$Q(X)$$. The **Poincaré series** (theta operator) averages a differential on the disk over $$G$$ and lands in $$Q(X)$$. Its operator norm is at most one. **Kra’s conjecture**, proved by McMullen, says the norm is **strictly less than one**.

McMullen in fact characterized, for a broader class of coverings, when this strict contraction holds, in the language of **amenable** covers. The analytic estimate is not an isolated curiosity. It feeds deformation theory of Kleinian groups and, as the 1998 laudation stressed, contributes to Thurston’s program of putting hyperbolic metrics on a large class of three-manifolds—especially those that fiber over the circle, the setting of McMullen’s monograph *Renormalization and 3-manifolds which fiber over the circle* (1996).

**Accuracy.** This is a chapter of geometrization, not a substitute for Perelman’s Ricci-flow resolution of the full geometrization conjecture.

---

## 4. What remains open: MLC and friends

The **local connectivity of the Mandelbrot set (MLC)** is a famous conjecture of Douady–Hubbard. Local connectivity would unlock a precise combinatorial model of $$M$$. McMullen’s renormalization rigidity is part of the circle of ideas surrounding MLC, and many special classes of parameters are understood. **MLC itself is not proved.** A seminar sentence that says “McMullen showed the Mandelbrot set is locally connected” is false.

Likewise, “McMullen geometrized all three-manifolds” is false. The citation’s geometrization clause is specific: holomorphic dynamics informing hyperbolic structures, including fibered manifolds and deformation spaces of Kleinian groups.

---

## 5. Neighbors in this course

[Avila]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/) inherits the renormalization machine and asks **typicality** questions in real and quasi-periodic dynamics. McMullen’s 1998 emphasis is more **geometric and rigid**: density of cusps, contraction of theta operators, and the dictionary between infinite renormalization and hyperbolic three-manifolds.

[Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) studies flows and counting **on** moduli space—earthquakes, Weil–Petersson volumes, simple closed geodesics. McMullen studies how Teichmüller space sits as a deformation space of groups and how its boundary is populated. Same city, different errands.

**Do not write** “McMullen invented renormalization.” Feigenbaum, Sullivan, Douady, and Hubbard already made it a mathematical object. McMullen made it a **bridge to three-dimensional hyperbolic geometry**.

---

## 6. Why a Fields Medal

Three interlocking reasons:

1. **Difficulty.** Bers density and Kra’s strict contraction resisted long effort; the proofs mix complex analysis, ergodic ideas about amenability, and three-manifold topology.
2. **Centrality.** Once renormalization talks to Kleinian groups, holomorphic dynamics and geometrization share theorems, not only analogies.
3. **Clarity of slogan with depth of method.** “Cusps are dense on the Bers boundary” is a sentence a graduate student can remember; the proofs are monuments of 1990s geometry.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “McMullen proved MLC.” | Local connectivity of the Mandelbrot set remains open. |
| “Geometrization in the citation is Perelman’s theorem.” | McMullen contributed to hyperbolic structures and fibered manifolds; Perelman’s Ricci-flow work is a later, different completion. |
| “Bers density classifies the whole boundary.” | Density of cusps does not identify every boundary point. |
| “Kra’s conjecture is about theta functions of number theory.” | It is about the Poincaré series operator on quadratic differentials. |
| “Renormalization here is only Feigenbaum period-doubling.” | Quadratic-like renormalization is broader and is used as a geometric machine. |

---

## Exercises

1. In your own words: what does straightening a quadratic-like map **forget** and **retain**?
2. Why is density of cusp points a weaker statement than a full classification of the Bers boundary?
3. Write one sentence that states Kra’s conjecture without symbols, then one sentence that names the operator whose norm is $$<1$$.
4. Distinguish Julia sets (dynamical plane) from the Mandelbrot set (parameter plane) in one paragraph.
5. **Accuracy practice.** Find a popular sentence that says MLC is a theorem. Rewrite it in two precise sentences.
6. **Seminar stretch.** Compare McMullen’s rigidity/renormalization culture with [Avila’s typicality]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/) and [Mirzakhani’s moduli dynamics]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/). Which question is each answering?

---

## Video sources and reading

1. **IMU citation** — Fields Medals 1998, Curtis T. McMullen: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998).
2. **Orientation** — CIRM interview with McMullen (research themes and the medal): [carmin.tv](https://www.carmin.tv/en/collections/dynamics-and-geometry-in-the-teichmuller-space-dynamique-et-geometrie-dans-lespace-de-teichmuller/video/interview-at-cirm-curtis-mcmullen).
3. **Monograph** — C. T. McMullen, *Renormalization and 3-manifolds which fiber over the circle*, Princeton University Press, 1996.

**Status reminder:** Holomorphic dynamics and selected geometrization theorems—**not** a proof of MLC, and not the full geometrization of every three-manifold.

---

## References

1. IMU Fields Medal 1998 citation — Curtis T. McMullen (mathunion.org).
2. **C. T. McMullen**, work on Bers density, Kra’s conjecture, and renormalization of quadratic-like maps; ICM 1998 laudation.
3. **A. Douady and J. H. Hubbard**, straightening of quadratic-like maps; Sullivan’s dictionary between rational maps and Kleinian groups.
4. Course neighbors: [Avila]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/), [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) (separate geometrization path).

---

## Further directions

- Read a survey of the Sullivan dictionary (rational maps ↔ Kleinian groups) and list three matching entries.
- Compare Feigenbaum universality as a physics discovery with McMullen’s geometric renormalization.
- Seminar A3 option: one page on what MLC would unlock—and what is already known without it—without claiming the medal closed complex dynamics.
