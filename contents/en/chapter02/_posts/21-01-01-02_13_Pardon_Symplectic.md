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

In classical physics, every planetary orbit, swinging pendulum, or spinning top lives inside **phase space**—a space whose coordinates pair each position $$q_i$$ with its momentum $$p_i$$. As the system evolves under Hamilton’s equations, its shape can stretch wildly like taffy, yet something mysterious remains stubbornly conserved: a two-dimensional "area" measured by a skew-symmetric form $$\omega = \sum dq_i \wedge dp_i$$.

Out of that nineteenth-century mechanics grew **symplectic geometry**, one of the richest and most unruly corners of modern mathematics. Since Mikhail Gromov’s 1985 revolution, symplectic geometers have probed hidden global structure by **counting pseudoholomorphic curves**—curved 2D surfaces inside higher-dimensional symplectic spaces—and packaging those counts into algebraic engines called **Fukaya categories**. Yet for decades, a terrifying foundational crack ran underneath the entire edifice: the spaces of curves you want to count are almost never smooth manifolds! They pinch, bubble, and intersect tangentially, threatening to make the counts mathematically undefined.

At ICM 2026 in Philadelphia, **John Pardon** (Stony Brook / Simons Center) received the **Fields Medal 2026** for fortifying those very foundations—building clean, topological **virtual fundamental cycles** and **Fukaya categories**—while also solving major problems in **3-manifold group actions** and **knot theory**.

**IMU short citation (official):**  
For his achievements in symplectic geometry including new approaches to virtual fundamental cycles, Fukaya categories of certain manifolds and counting holomorphic curves, and for his contributions to other areas of geometry and topology, including group actions on 3-manifolds and knot theory.

This essay translates modern symplectic topology into concrete, hand-checkable intuition—starting from a $$2\times 2$$ matrix, Gromov’s famous "symplectic camel" non-squeezing theorem, and two intersecting circles—before looking at Pardon’s virtual cycles, Fukaya categories, and his ongoing ICM 2026 work on **log derived regularity** (marked **in progress**).

---

## Learning objectives

After this lecture you should be able to:

- Verify by hand using the skew-symmetric matrix $$J$$ why every **symplectic manifold** must have **even dimension** $$2n$$.
- Explain **Gromov’s non-squeezing theorem** ($$B^4(R) \not\hookrightarrow Z^4(r)$$ for $$r < R$$) to see why symplectic geometry is far more rigid than volume-preserving geometry.
- Use the concrete example of **two circles** (transverse, tangent, and coincident) to explain why counting geometric intersections requires a **virtual fundamental cycle** when transversality fails.
- Describe **Fukaya categories** as categorical invariants built from Lagrangian submanifolds and counts of holomorphic disks, feeding into homological mirror symmetry.
- Name Pardon’s contributions beyond symplectic geometry (**group actions on 3-manifolds** and **knot theory**) and distinguish the official IMU citation from his ongoing ICM 2026 lecture on **log derived regularity**.

**Prerequisites.** Multivariable calculus / differential forms, basic linear algebra (determinants), and elementary manifold intuition.

**Related lessons.** Pair with [Mirzakhani / moduli]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) for another moduli-space story, and with [Perelman / Poincaré]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) for 3-manifold topology.

---

## Background Knowledge Map: What Is Symplectic Topology?

If you met Euclidean geometry (lengths and angles) and differential topology (stretching rubber sheets), **symplectic geometry** sits dramatically right in between: far floppier than Riemannian geometry, yet astonishingly more rigid than pure volume-preserving topology.

### 1. Symplectic Geometry: The Geometry of Phase Space & Area
**What is it?** A **symplectic manifold** $$(M^{2n}, \omega)$$ is a smooth manifold equipped with a closed ($$d\omega = 0$$), nondegenerate 2-form $$\omega$$. Instead of measuring lengths of vectors (like a Riemannian metric), $$\omega(v,w)$$ measures the **signed area** of the parallelogram spanned by $$v$$ and $$w$$.

**What does it study?**
- **Hamiltonian flows:** Energy functions $$H: M \to \mathbb{R}$$ generate flows preserving $$\omega$$—the exact mathematical language of classical and celestial mechanics.
- **Symplectic rigidity:** Unlike volume-preserving maps (which can squeeze a ball into an arbitrarily thin tube), symplectomorphisms cannot squeeze a 4D ball into a narrower 4D cylinder (**Gromov non-squeezing**).

### 2. Pseudoholomorphic Curves & Moduli Spaces
**What is it?** Inspired by complex analysis, Gromov introduced **$$J$$-holomorphic curves**: maps $$u: \Sigma \to M$$ from a Riemann surface $$\Sigma$$ satisfying the Cauchy–Riemann equation $$du \circ j = J \circ du$$.

**What does it study?**
- **Curve counting invariants (Gromov–Witten, Floer homology):** Fixing boundary or incidence constraints, you collect all solutions into a **moduli space $$\mathcal{M}$$** and count them.
- **Virtual fundamental cycles:** Because $$\mathcal{M}$$ often fails to be smooth or has the wrong dimension, you need rigorous topological machinery (implicit atlases, Kuranishi structures, derived manifolds) to define a well-behaved "virtual count" $$[\mathcal{M}]^{\mathrm{vir}}$$.

### 3. Low-Dimensional Topology: 3-Manifolds & Knots
**What is it?** The study of 3-dimensional spaces and 1-dimensional loops (knots) embedded in 3D space.

**What does it study?**
- **Hilbert–Smith & group actions:** Which topological groups can act faithfully on a 3-manifold? (Pardon proved the Hilbert–Smith conjecture in dimension 3!)
- **Knot invariants:** Geometric and Floer-theoretic invariants distinguishing knots and measuring their complexity (such as knot distortion).

---

## 1. Symplectic geometry in one page (and two hand checks)

A **symplectic manifold** is a smooth manifold $$M$$ equipped with a closed, nondegenerate 2-form $$\omega$$:

$$
d\omega=0,\qquad \omega^n\neq 0\text{ at every point}.
$$

The prototype is $$\mathbb{R}^{2n}$$ with standard form $$\omega_0 = \sum_{i=1}^n dx_i \wedge dy_i$$, and more generally any cotangent bundle $$T^*Q$$ from classical mechanics.

### Hand-Verifiable Example 1: A 2-Line Proof That Symplectic Dimension Must Be Even
At any point $$p \in M^m$$, the skew-symmetric bilinear form $$\omega_p(v,w) = -\omega_p(w,v)$$ is represented in coordinates by an $$m \times m$$ real skew-symmetric matrix $$A$$ (so $$A^T = -A$$). In 2D, the prototype is

$$
J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad \det(J) = 1 \neq 0.
$$

Now take the determinant of $$A^T = -A$$ in dimension $$m$$:

$$
\det(A) = \det(A^T) = \det(-A) = (-1)^m \det(A).
$$

If $$m$$ were **odd**, then $$(-1)^m = -1$$, forcing $$\det(A) = -\det(A) \implies \det(A) = 0$$! That contradicts nondegeneracy ($$\det(A) \neq 0$$). Therefore **every symplectic manifold automatically has even dimension $$m = 2n$$**—you can never build a symplectic 3-manifold!

### Hand-Verifiable Example 2: Gromov’s Non-Squeezing Theorem ("The Symplectic Camel")
Compare two 4-dimensional shapes in $$\mathbb{R}^4$$ with coordinates $$(x_1, y_1, x_2, y_2)$$ and $$\omega_0 = dx_1\wedge dy_1 + dx_2\wedge dy_2$$:
- The **4D ball** of radius $$R$$: $$B^4(R) = \{x_1^2 + y_1^2 + x_2^2 + y_2^2 \le R^2\}$$ (finite volume $$\frac{1}{2}\pi^2 R^4$$).
- The **4D symplectic cylinder** of radius $$r$$: $$Z^4(r) = \{x_1^2 + y_1^2 \le r^2\}$$ (infinite volume!).

If you only preserve 4D volume, you can easily stretch $$B^4(R)$$ along $$(x_2, y_2)$$ and shrink $$(x_1, y_1)$$ to stuff the entire ball inside $$Z^4(r)$$ for *any* tiny $$r > 0$$! Yet in 1985, **Mikhail Gromov** proved a shocking theorem:

$$
\text{A symplectic embedding } B^4(R) \hookrightarrow Z^4(r) \text{ exists } \Longleftrightarrow R \le r.
$$

When $$r < R$$, no symplectomorphism in the universe can squeeze the ball through the cylinder! Gromov proved this by showing that a **pseudoholomorphic disk** must pass through the ball’s center with symplectic area at least $$\pi R^2$$, yet inside the cylinder its projection onto the $$(x_1, y_1)$$-plane has area at most $$\pi r^2$$!

---

## 2. Why counting curves is hard (and the two-circle intuition)

Since Gromov, counting pseudoholomorphic curves $$u: \Sigma \to M$$ (solutions to $$du \circ j = J \circ du$$) has become the central engine of symplectic topology. In an ideal world, the moduli space $$\mathcal{M}$$ of solutions is a smooth compact manifold of the expected dimension (given by the Riemann–Roch index formula), so when the expected dimension is $$0$$ you simply count signed points.

In reality, four disasters strike routinely: **transversality fails** (wrong dimension or singularities), **compactness fails** (curves bubble off spheres or break into buildings), **automorphisms** create orbifold singularities, and **coherent orientations** are delicate.

### Hand-Verifiable Example 3: Two Circles and Why You Need a Virtual Count
Forget infinite-dimensional PDEs for a moment and picture two unit circles $$C_1, C_2$$ in the plane $$\mathbb{R}^2$$. Expected dimension of their intersection $$C_1 \cap C_2$$ is $$1 + 1 - 2 = 0$$ (isolated points). Watch three cases:

1. **Transverse case:** Shift $$C_2$$ slightly so they cross cleanly at **2 points** (one with sign $$+1$$, one with sign $$-1$$; algebraic count $$+1 - 1 = 0$$). Everything is smooth and well-defined!
2. **Tangent case:** Slide $$C_2$$ until it barely kisses $$C_1$$ at **1 point**. Transversality fails—the naive point count jumps from $$2$$ to $$1$$, even though the topological intersection number is still $$0$$!
3. **Coincident case:** Place $$C_2$$ directly on top of $$C_1$$! Now $$C_1 \cap C_2 = C_1$$ has dimension **1** instead of the expected dimension **0**—infinitely many points!

In finite dimensions, you simply wiggle $$C_2$$ slightly to make the intersection transverse again. Inside a symplectic manifold, however, symmetries (such as multiple covers of a holomorphic sphere) make it **impossible** to perturb the geometric equation $$du \circ j = J \circ du$$ globally into a transverse position! You must instead extract a well-defined **virtual fundamental cycle** $$[\mathcal{M}]^{\mathrm{vir}}$$ directly from the obstructed moduli space itself.

---

### Deep-Dive Explanation: Pardon’s Implicit Atlases & Virtual Fundamental Cycles (Read Slowly)

For over twenty years, constructing rigorous virtual fundamental cycles in full generality was one of the most notoriously technical bottlenecks in symplectic geometry (with competing frameworks like Kuranishi structures and polyfolds). How did **John Pardon** transform this landscape? Follow the four-step arc slowly:

#### Step 1: Isolate what a virtual cycle actually needs (avoid over-engineering smoothness!)
Earlier approaches tried to give the singular moduli space $$\overline{\mathcal{M}}$$ a full smooth manifold-like atlas with smooth coordinate transition maps—which collides head-on with bubbling and gluing analysis, where gluing maps are often only continuous, not smoothly differentiable! Pardon asked: *To extract a homology class $$[\mathcal{M}]^{\mathrm{vir}} \in H_*(\overline{\mathcal{M}})$$, do we really need smooth transition maps?*

#### Step 2: Build an "implicit atlas" using purely topological charts
Pardon introduced **implicit atlases**: local thickening charts $$(V_\alpha, E_\alpha, s_\alpha)$$ where $$V_\alpha$$ is a finite-dimensional topological manifold, $$E_\alpha$$ is a finite-dimensional obstruction space, and the local moduli space is carved out as $$s_\alpha^{-1}(0)$$. Crucially, Pardon’s compatibility axioms require only **topological** (continuous, homological) gluing data—bypassing the brutal smooth-gluing bottleneck!

#### Step 3: Extract $$[\mathcal{M}]^{\mathrm{vir}}$$ via Čech cohomology and Alexander duality
Using clean algebraic topology (Čech cohomology, duality, and a clever homological algebra package), Pardon proved that every implicit atlas canonically determines a **virtual fundamental cycle** $$[\mathcal{M}]^{\mathrm{vir}}$$ compatible with boundary strata, gluing, and orientations—without ever needing to choose global generic perturbations!

#### Step 4: Power up Floer homology, contact homology, and Fukaya categories
With this rock-solid, flexible foundation, Pardon constructed rigorous **contact homology**, defined **Fukaya categories** for broad classes of symplectic manifolds (including Liouville sectors, in landmark joint work with Ganatra and Shende), and proved sweeping results on counting holomorphic curves—turning decades of conjectural symplectic algebra into airtight theorems.

In one schematic line:

$$
\text{Obstructed curve moduli }\overline{\mathcal{M}}
\;\xrightarrow{\;\text{implicit atlas (topological charts)}\;}\;
[\mathcal{M}]^{\mathrm{vir}} \in H_*(\overline{\mathcal{M}})
\;\xrightarrow{\;\text{gluing \& }A_\infty\text{ relations}\;}\;
\text{Rigorous Floer \& Fukaya invariants}.
$$

---

## 3. Fukaya categories: a slogan for mirror symmetry consumers

A **Lagrangian submanifold** $$L\subset (M^{2n},\omega)$$ is a half-dimensional ($$n$$-dimensional) submanifold on which $$\omega\vert_L = 0$$. The **Fukaya category** packages Lagrangian intersections into an $$A_\infty$$-category:

- **Objects:** Lagrangian submanifolds (with grading and orientation/spin data).
- **Morphisms:** Floer cochain complexes generated by intersection points of Lagrangians, with differentials and higher products $$m_k$$ counting holomorphic polygons bounded by those Lagrangians.

This algebraic machine is one half of **Kontsevich’s Homological Mirror Symmetry**: the Fukaya category of a symplectic manifold $$M$$ is predicted to be equivalent to the derived category of coherent sheaves on a mirror complex algebraic variety $$M^\vee$$. Constructing Fukaya categories rigorously on non-compact and singular spaces (such as Liouville sectors, developed by Ganatra–Pardon–Shende) makes that bridge concrete and computable.

---

## 4. Beyond symplectic: 3-manifold group actions and knot theory

Pardon’s medal is not solely a symplectic medal. The IMU citation explicitly highlights his breakthroughs in low-dimensional topology:

- **Group actions on 3-manifolds (2013):** Pardon proved the **3-dimensional Hilbert–Smith conjecture**: no $$p$$-adic integer group $$\mathbb{Z}_p$$ can act faithfully by homeomorphisms on a 3-manifold! (Meaning every locally compact group acting faithfully on a 3-manifold must be a Lie group.)
- **Knot theory (2011):** While still an undergraduate, Pardon settled Gromov’s 1983 question on **knot distortion**, proving that knots in $$\mathbb{R}^3$$ can have arbitrarily large distortion (no universal upper bound on how badly a knot must crumple in space).

Together with [Perelman’s geometrization story]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/), Pardon’s work shows how alive 3-dimensional topology remains across completely different toolkits.

---

## 5. ICM 2026 Fields lecture: log derived regularity (in progress)

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
  - **Log smooth / log geometry:** compactifications and degenerations with controlled normal-crossing structure.
  - **Derived moduli:** stacks that remember higher obstruction theory.
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

## 6. Why a Fields Medal

The 2026 citation clusters:
1. New approaches to **virtual fundamental cycles** and rigorous **curve counting**.
2. **Fukaya categories** of certain manifolds—categorical packages of Lagrangian Floer data.
3. Landmark contributions to **group actions on 3-manifolds** and **knot theory**.

Like [Scholze]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/) in $$p$$-adic geometry, Pardon earned the medal by strengthening the **language and foundational legality** of an entire field—turning fragile heuristic counts into rock-solid theorems.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Virtual cycles are only technical bookkeeping.” | They are the difference between undefined counts and rigorous theorems. |
| “Fukaya categories are just chain complexes of forms.” | They encode holomorphic-curve geometry categorically ($$A_\infty$$ structure from disks/polygons). |
| “Symplectic geometry is only classical mechanics.” | Mechanics is the historical origin; global topology via holomorphic curves is the modern core. |
| “The Log Derived Regularity Theorem is a finished published prize theorem on the slide.” | The slide explicitly says **in progress**. |
| “The Facebook reel is the full lecture.” | It is a short visual clip (~24 s) of one slide. |
| “Pardon works only in symplectic geometry.” | The IMU citation explicitly includes 3-manifold group actions and knot theory. |

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

## Video tham khảo

- **xem trước** — [2026 Fields Medal: John Pardon](https://www.youtube.com/watch?v=E4KP07YL0Js) — Simons Foundation, English. Watch first. “2026 Fields Medal: John Pardon” orients the lesson’s aim: State what symplectic geometry studies: closed nondegenerate 2-forms; Hamiltonian dynamics as structure-preserving flows.
- [ICM 2026 Fields Medal Award Lecture - John Pardon](https://www.youtube.com/watch?v=YZ7hKBlCeGs) — Simons Foundation, English. A second pass once the main claim is in view: State what symplectic geometry studies: closed nondegenerate 2-forms; Hamiltonian dynamics as structure-preserving flows.
- [Contact homology and virtual fundamental cycles - John Pardon](https://www.youtube.com/watch?v=Eh8Hrg1mQVk) — Institute for Advanced Study, English. Further depth after the first two, still tied to this lesson: State what symplectic geometry studies: closed nondegenerate 2-forms; Hamiltonian dynamics as structure-preserving flows.
