---
layout: post
title: "John Pardon: Symplectic Geometry and Topology (Fields Medal 2026)"
chapter: '02'
order: 12
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**John Pardon** (Stony Brook / Simons Center) received the **Fields Medal 2026** for achievements in **symplectic geometry** and for contributions across geometry and topology. Where some medals celebrate a single conjecture closed, Pardon’s citation emphasizes **foundations**: how to count holomorphic curves rigorously when classical transversality fails, how to build Fukaya-type categorical invariants on interesting manifolds, and how the same geometric sensibility reaches into **3-manifold group actions** and **knot theory**.

**IMU short citation (official):**  
For his achievements in symplectic geometry including new approaches to virtual fundamental cycles, Fukaya categories of certain manifolds and counting holomorphic curves, and for his contributions to other areas of geometry and topology, including group actions on 3-manifolds and knot theory.

This essay is for learners who have met differential forms and basic topology and want the **slogans** of modern symplectic topology without a full Floer-theory course. It preserves the official IMU wording above and expands carefully around it—including a window into advanced moduli work presented at the ICM 2026 Fields lecture (log derived regularity), clearly marked as **in progress** and not a replacement for the prize citation.

---

## Learning objectives

After this lecture you should be able to:

- State what **symplectic geometry** studies: closed nondegenerate 2-forms; Hamiltonian dynamics as structure-preserving flows.
- Explain why counting **holomorphic curves** often needs **virtual** techniques (moduli spaces are rarely smooth of expected dimension).
- Name **Fukaya categories** as homological invariants built from Lagrangians and holomorphic disks / curves (mirror symmetry consumers).
- List the non-symplectic items in Pardon’s citation: **group actions on 3-manifolds** and **knot theory**.
- Separate the **IMU Fields citation** from later or ongoing lecture material (e.g. log derived regularity marked in progress).
- See Pardon’s profile as spanning symplectic foundations and low-dimensional topology, not a single construction.

**Prerequisites.** Smooth manifolds, differential forms, and the idea of a moduli space of maps. Complex analysis of curves at the level of Riemann surfaces is helpful but not required.

**Seminar links.** LO1 (foundational programs); LO4 (classical geometric topology ↔ modern categorical invariants). Pair with [Mirzakhani / moduli]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) for another “moduli of geometric objects” story, and with [Perelman / Poincaré]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) for 3-manifold topology—different tools, shared low-dimensional gravity.

---

## 1. Symplectic geometry in one page

A **symplectic manifold** is a smooth even-dimensional manifold $$M^{2n}$$ equipped with a closed, nondegenerate 2-form $$\omega$$:

$$
d\omega=0,\qquad \omega^n\neq 0\text{ at every point}.
$$

Nondegeneracy means that at each tangent space the bilinear form $$\omega_p$$ induces an isomorphism $$T_pM\to T_p^*M$$. The basic example is $$\mathbb{R}^{2n}$$ with

$$
\omega_0=\sum_{i=1}^{n} dx_i\wedge dy_i,
$$

and more generally cotangent bundles $$T^*Q$$ with the canonical symplectic form of classical mechanics.

**Hamiltonian dynamics.** A smooth function $$H:M\to\mathbb{R}$$ determines a vector field $$X_H$$ by $$\iota_{X_H}\omega=dH$$. The flow of $$X_H$$ preserves $$\omega$$—phase space volume and symplectic structure are conserved. Symplectic geometry is, among other things, the geometry of Hamiltonian mechanics stripped of coordinates.

**Almost complex structures and curves.** An almost complex structure $$J$$ on $$M$$ is **compatible** with $$\omega$$ if $$g(v,w)=\omega(v,Jw)$$ is a Riemannian metric. **Pseudoholomorphic curves** are maps $$u:\Sigma\to M$$ from a Riemann surface $$(\Sigma,j)$$ satisfying

$$
du\circ j = J\circ du
$$

(the Cauchy–Riemann equation for $$J$$). Since Gromov’s 1985 work, such curves have been the primary probes of global symplectic topology: they detect non-squeezing, generate Floer homology, and feed the construction of Fukaya categories.

---

## 2. Why counting curves is hard

Naively, one hopes the moduli space $$\mathcal{M}$$ of holomorphic curves in a fixed homology class (with constraints) is a smooth manifold of **expected dimension** given by an index formula, so that one can count points when that dimension is zero, or integrate cohomology classes when it is positive.

In practice, several disasters occur:

1. **Transversality fails.** The linearized Cauchy–Riemann operator may not be surjective; $$\mathcal{M}$$ may be singular or of the wrong dimension.
2. **Compactness fails in the usual topology.** Sequences of curves can bubble, break, or escape, producing Gromov–Floer compactifications with tree-like or building-like strata.
3. **Automorphisms and orbifold issues.** Curves with symmetry produce orbifold points rather than manifold points.
4. **Orientations and coherence.** Even when virtual dimensions work, coherent orientations are needed for signed counts and for chain-level algebra.

When the moduli space is not a manifold, one cannot literally “count points.” One needs a substitute fundamental class in homology (or a chain-level enhancement) that behaves as if a smooth fundamental class existed—compatible with boundary strata that encode gluing of curves. That substitute is the **virtual fundamental cycle** (or virtual fundamental class).

**Slogan.** Virtual techniques are not bookkeeping optional extras; they are the difference between an undefined count and a theorem.

---

## 3. Virtual fundamental cycles: Pardon’s foundational emphasis

The IMU citation highlights **new approaches to virtual fundamental cycles**. Several schools of virtual techniques exist in the literature (Kuranishi structures, polyfolds, algebraic virtual classes, implicit atlases, and others). The technical goal is always similar:

- package obstruction bundles / obstruction theories over charts of the moduli space;
- glue charts so that a global virtual class

$$
[\mathcal{M}]^{\mathrm{vir}}\in H_*(\overline{\mathcal{M}})
$$

(or a chain-level analogue) is well-defined;
- ensure that when transversality *does* hold, the virtual class recovers the ordinary fundamental class.

Pardon’s contributions reorganize and strengthen parts of this foundation—making constructions more flexible, more topological, or better adapted to the geometric situations needed for curve counts and categorical invariants. For this course, the precise comparison of foundations is less important than the **recognition**: modern symplectic topology is as much about the legality of its counts as about the geometry those counts detect.

---

## 4. Fukaya categories: a slogan for mirror symmetry consumers

A **Lagrangian submanifold** $$L\subset (M,\omega)$$ is a middle-dimensional submanifold on which $$\omega|_L=0$$. Lagrangian intersections, under Hamiltonian isotopy, are a central theme of symplectic topology (Arnold-type conjectures, Floer homology).

The **Fukaya category** (in rough outline) has:

- **objects:** Lagrangian submanifolds (with extra data: grading, spin structure / orientation data, bounding cochains in more advanced setups);
- **morphisms:** Floer cochain complexes built from intersection points of Lagrangians, with differentials and higher products counting holomorphic disks (or polygons) with boundary on the Lagrangians.

The higher operations $$m_k$$ assemble into an $$A_\infty$$-category. This structure is a primary input to **homological mirror symmetry**: the Fukaya category of a symplectic manifold is conjecturally equivalent (in a suitable sense) to a category of coherent sheaves (or matrix factorizations) on a mirror complex manifold.

**Constructing** Fukaya categories rigorously on interesting manifolds is a major enterprise precisely because of the virtual-cycle issues above. The IMU citation’s phrase “Fukaya categories of certain manifolds and counting holomorphic curves” packages this foundational geometric algebra together with the curve-counting that feeds it.

---

## 5. Beyond symplectic: 3-manifold group actions and knot theory

Pardon’s medal is not only a symplectic medal. The official citation explicitly includes:

- **group actions on 3-manifolds**;
- **knot theory**.

Low-dimensional topology has long studied which groups can act on which 3-manifolds (smoothly, continuously, or by homeomorphisms), and how knots and links encode both geometric and algebraic data (fundamental groups of complements, Floer-theoretic invariants, concordance). Pardon’s portfolio connects the analytic/categorical sophistication of symplectic methods with classical topological questions—breadth that the IMU short citation deliberately records.

For readers coming from [Perelman’s geometrization story]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/), the moral is complementary: 3-manifold topology remains a live source of deep problems, some attacked by Ricci flow, some by gauge theory or Floer theory, some by group-action rigidity, some by knot-theoretic invariants. Pardon works in several of these dialects.

---

## 6. ICM 2026 Fields lecture: log derived regularity (in progress)

At the **International Congress of Mathematicians 2026** (Philadelphia), Pardon’s Fields Medal lecture included advanced moduli-theoretic work beyond the short IMU citation’s headline items. A short public reel of the lecture shows the final slide (19/19) of a talk segment titled **Logarithmic derived regularity**.

### Theorem (Log Derived Regularity Theorem; in progress)

*Reconstructed from the lecture slide (not a verbatim transcript of the oral talk).*

Let

$$
W \xrightarrow{\mathrm{strict}} C \xrightarrow{\mathrm{exact}} B
$$

be an **elliptic section problem** over a **log smooth** manifold $$B$$. Assume $$C\to B$$ is proper and of depth one, and assume either **non-degenerate ends** or **Morse–Bott ends** with a compatible exponential-decay structure.

Then:

1. The full **log derived smooth moduli stack** is representable:
   $$
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogDSm}} \in \mathrm{LogDSm}.
   $$
2. The comparison map to the **log topological** moduli space is an isomorphism:
   $$
   (\mathrm{LogDSm}\to\mathrm{LogTop})_*\,
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogDSm}}
   \;\simeq\;
   \underline{\mathrm{Hol}}_B(C,W)_{\mathrm{LogTop}}.
   $$

![ICM 2026 slide: Log Derived Regularity Theorem]({{ site.baseurl }}/img/chapter_img/pardon_log_derived_regularity_icm2026.jpg)

*Figure. Slide from John Pardon’s 2026 Fields Medal lecture (ICM 2026), as captured in a public reel — theorem marked **in progress** on the slide itself.*

### How to read this (for this course)

- **Not** a replacement for the IMU Fields citation (virtual cycles, Fukaya categories, 3-manifold topology). It is **ongoing/advanced** work presented at the prize lecture.
- **Theme continuity:** both the prize work and this theorem concern **moduli of maps/sections** when classical smoothness and transversality fail—here in a **logarithmic + derived** setting rather than classical almost-complex curve counts alone.
- **Vocabulary touchpoints:**
  - **Log smooth / log geometry:** compactifications and degenerations with controlled normal-crossing type structure.
  - **Derived moduli:** stacks that remember higher obstruction theory (not only classical schemes/orbifolds).
  - **Representability in LogDSm:** the moduli object is a legitimate geometric object in a category of log derived smooth stacks.
  - **Comparison to LogTop:** analytic/topological moduli match the derived-smooth description under the stated end hypotheses.

### Accuracy notes from the source video

| Item | Evidence |
|------|----------|
| Event | On-stage banner: International Congress of Mathematicians 2026 |
| Speaker context | Overlay / reel title: 2026 Fields Medal Lecture — John Pardon |
| Theorem status | Slide header: **in progress** |
| Source | Facebook reel `1666056391140628` (~24 s; visual slide capture) |
| Oral transcript | No captions available; content reconstructed from slide text |

---

## 7. Why a Fields Medal

The citation clusters:

1. New approaches to **virtual fundamental cycles** and rigorous **curve counting**.
2. **Fukaya categories** of certain manifolds—categorical packages of Lagrangian Floer data.
3. Contributions to **group actions on 3-manifolds** and **knot theory**.

Bigger than a single numerical theorem: a strengthening of the **language and legality** of symplectic topology, plus breadth into classical geometric topology. The ICM lecture snippet shows the same mathematician still pushing **moduli foundations** (log/derived regularity) at the prize podium—not only classical Fukaya setups.

For this course, compare foundational medals (Pardon; also [Scholze]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/) in a different field) with single-conjecture medals: both reshape what the next decade can say.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Virtual cycles are only technical bookkeeping.” | They are the difference between undefined counts and theorems. |
| “Fukaya categories are just chain complexes of forms.” | They encode holomorphic-curve geometry categorically ($$A_\infty$$ structure from disks/polygons). |
| “Symplectic geometry is only classical mechanics.” | Mechanics is origin and inspiration; global topology via curves is the modern core. |
| “The Log Derived Regularity Theorem is a finished published prize theorem on the slide.” | The slide explicitly says **in progress**. |
| “The Facebook reel is the full lecture.” | It is a short visual clip (~24 s) of one slide. |
| “Pardon works only in symplectic geometry.” | The IMU citation includes 3-manifold group actions and knot theory. |

---

## Exercises

1. What does **nondegeneracy** of a 2-form mean linearly (at a single tangent space)?
2. Why do moduli spaces of holomorphic curves fail transversality “often”? Name two independent reasons.
3. What is a **Lagrangian** submanifold, slogan-level? Check the definition on the zero section of $$T^*Q$$.
4. Name **two non-symplectic** topics in Pardon’s official citation.
5. Skim a survey of Fukaya categories and list three prerequisites you would need for a serious reading course.
6. **From the ICM slide:** In one paragraph, separate (a) hypotheses on $$W\to C\to B$$ from (b) the two conclusions (representability; comparison isomorphism).
7. **Research literacy:** Why might “log” geometry appear when studying moduli of maps near degenerations or boundary strata?
8. **Comparison.** In at most twelve sentences, compare Pardon’s “virtual class for moduli” problem with Perelman’s “control singularities of a geometric flow” problem—as two styles of making a geometric process legal.

---


## Video sources (math-video-researcher pack)

Full ranking: `research/video-research/Pardon_Symplectic/`. Full ICM lecture may supersede the short reel.

**Recommended order**

1. **Profile** — Quanta: [John Pardon Wins the 2026 Fields Medal…](https://www.quantamagazine.org/john-pardon-wins-the-2026-fields-medal-for-work-in-symplectic-geometry-20260723/).  
2. **Official** — IMU citation: [PDF](https://www.mathunion.org/fileadmin/documents/2026-07/John_Pardon_Citations.pdf) · [Fields 2026 page](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026).  
3. **Visual clip** — ICM 2026 reel (Facebook; no full captions): [reel](https://www.facebook.com/reel/1666056391140628).  
4. **Publications hub** — [Pardon homepage](https://www.math.stonybrook.edu/~jpardon/).

**Status reminder:** Virtual fundamental cycles make curve-counting **legal** when transversality fails—foundations, not a single popular conjecture slogan.

---

## References


Full URL bibliography from video research (including secondary finds): `research/video-research/Pardon_Symplectic/references.md`.

### Complete URL list (audit)

1. https://www.facebook.com/reel/1666056391140628  
2. https://www.math.stonybrook.edu/~jpardon/  
3. https://www.quantamagazine.org/john-pardon-wins-the-2026-fields-medal-for-work-in-symplectic-geometry-20260723/  
4. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026  
5. https://www.mathunion.org/fileadmin/documents/2026-07/John_Pardon_Citations.pdf  
6. https://news.stonybrook.edu/university/john-pardon-wins-2026-fields-medal-for-outstanding-mathematical-achievement/  
7. https://www.claymath.org/news/2026-fields-medals/  
8. https://www.princeton.edu/news/2026/07/23/princeton-alumni-awarded-three-four-2026-fields-medals-math  
9. https://en.wikipedia.org/wiki/John_Pardon  
10. https://arxiv.org/search/?query=Pardon+virtual+fundamental&searchtype=all  
11. https://en.wikipedia.org/wiki/Symplectic_geometry  
12. https://en.wikipedia.org/wiki/Fukaya_category  
13. https://scgp.stonybrook.edu/  

### Research pack

14. Course pack: `research/video-research/Pardon_Symplectic/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. IMU Fields Medal 2026 — John Pardon (citation PDF / mathunion.org).
2. Selected papers of John Pardon on virtual cycles / symplectic topology / low-dimensional topology.
3. Background: **D. McDuff and D. Salamon**, *J-holomorphic Curves and Symplectic Topology*; surveys on Floer/Fukaya theory.
4. University / Simons Center announcements (2026).
5. **Source video (ICM 2026 reel):** [2026 Fields Medal Lecture: John Pardon](https://www.facebook.com/reel/1666056391140628) — logarithmic derived regularity slide (accessed 2026-08-03). Visual reconstruction; no official captions on the reel.
6. Course: [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/), [Scholze]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/) (foundations of a different kind).

---

## Further directions

- Explore **mirror symmetry** as a consumer of Fukaya categories (Kontsevich’s homological mirror symmetry conjecture as a roadmap, not a homework problem).
- Compare foundational medals (Pardon, Scholze) with single-conjecture medals in this chapter.
- For log geometry vocabulary: look up *log smooth morphisms* and *derived stacks* in a survey before chasing research papers.
- If a full ICM lecture video appears, re-run knowledge extraction for multi-unit segmentation beyond this single theorem slide.
- Seminar A3 option: write a one-page brief “What must a virtual fundamental class satisfy?” with three axioms in your own words.
