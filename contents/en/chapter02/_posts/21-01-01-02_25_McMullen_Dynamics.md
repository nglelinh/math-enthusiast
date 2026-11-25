---
layout: post
title: "McMullen’s Holomorphic Dynamics and Teichmüller Geometry (Fields Medal 1998)"
chapter: '02'
order: 25
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Anyone who has zoomed into the boundary of the **Mandelbrot set** remembers the shock: buried deep inside its endless fractal filigree sit tiny, pristine baby copies of the Mandelbrot set itself! At first glance, iterating $$z \mapsto z^2 + c$$ on the complex plane seems light-years away from **negatively curved three-dimensional geometry**—the hyperbolic 3-manifolds at the heart of William Thurston’s geometrization program. Yet in the 1980s and 1990s, Sullivan’s dictionary and the razor-sharp theorems of **Curtis T. McMullen** revealed that both worlds run on the *exact same engine*: **renormalization** and **rigidity of conformal dynamical systems**.

At ICM Berlin in 1998, **Curtis T. McMullen** received the **Fields Medal** with the official citation:

> For his contributions to the theory of holomorphic dynamics and geometrization of three-manifolds, including proofs of Bers’ conjecture on the density of cusp points in the boundary of the Teichmüller space, and Kra’s theta-function conjecture.

This essay walks from hands-on quadratic iteration to **Teichmüller space**, **Bers’s boundary**, **Kra’s Poincaré series operator**, and **hyperbolic 3-manifolds that fiber over the circle**. One boundary is essential from the start: McMullen built powerful renormalization and rigidity tools *inside* Thurston’s geometrization program, whereas the complete proof of full geometrization and the Poincaré conjecture belongs to [Grigori Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/).

**Lesson roadmap:** Key ideas (holomorphic dynamics, Teichmüller space, Sullivan’s dictionary) → Hand-verifiable worked examples (iterating $$z^2 + c$$ at $$c = 0, -2, -1$$ & pinching a genus-2 surface into a maximal cusp) → Bers’s cusp density & Kra’s amenability theorem → Explanation: how renormalization unifies Mandelbrot rigidity with fibered 3-manifolds → Lineage to Mirzakhani and boundary with Perelman.

---

## Learning objectives

After this lecture you should be able to:

- Recite the 1998 citation and state its two named theorems (**Bers’s conjecture** on density of cusps; **Kra’s theta-function conjecture** $$\|\Theta\| < 1$$).
- Compute by hand the Fatou and Julia sets for $$z^2$$, $$z^2 - 2$$, and $$z^2 - 1$$, and explain what **renormalization** (quadratic-like maps) means.
- Explain **Teichmüller space** $$\mathcal{T}(S)$$, the Bers embedding, and how pinching simple closed curves produces a **maximal cusp** on the Bers boundary.
- State McMullen’s **amenability criterion** for coverings of Riemann surfaces and how it implies Kra’s contraction inequality $$\|\Theta\| < 1$$.
- Distinguish McMullen’s work inside **Thurston’s geometrization program** from Perelman’s completion of geometrization, and link his lineage to [Mirzakhani’s moduli]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/).

**Prerequisites.** Holomorphic functions on $$\mathbb{C}$$ and the Riemann sphere $$\widehat{\mathbb{C}}$$; the idea of a compact Riemann surface of genus $$g\ge 2$$ with a hyperbolic metric; comfort with “iteration” as repeating a map. No prior Kleinian-group course is assumed.

**Seminar links.** Geometry cousins: [Mirzakhani / moduli]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/). Complex-dynamics landscape: Fatou, Julia, Sullivan, Douady–Hubbard, Thurston, Yoccoz.

---

## Key ideas: What Do Holomorphic Dynamics, Teichmüller Space, and Sullivan’s Dictionary Study?

### 1. Holomorphic dynamics
Take a rational map $$f: \widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$$ (simplest case: $$f_c(z) = z^2 + c$$) and iterate $$z \mapsto f(z) \mapsto f^{\circ 2}(z) \mapsto \cdots$$. The Riemann sphere splits into two invariant pieces:
- **Fatou set** (stability): nearby points share the same long-term fate.
- **Julia set $$J(f)$$** (chaos): the fractal frontier where arbitrarily close starting points diverge.
In parameter space $$c \in \mathbb{C}$$, the **Mandelbrot set** collects all $$c$$ for which the orbit of $$0$$ stays bounded (equivalently, $$J(f_c)$$ is connected).

### 2. Teichmüller space $$\mathcal{T}(S)$$
For a closed orientable surface $$S$$ of genus $$g \ge 2$$, **Teichmüller space** $$\mathcal{T}(S)$$ parametrizes all marked hyperbolic (or Riemann surface) structures on $$S$$—a smooth cell of real dimension $$6g - 6$$. Quotienting out the markings by the mapping class group produces **moduli space** $$\mathcal{M}_g$$ (the stage of [Mirzakhani’s lecture]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/)).

### 3. Sullivan’s dictionary—the bridge between 2D iteration and 3D hyperbolic geometry
A **Kleinian group** (a discrete subgroup of Möbius maps $$\mathrm{PSL}(2,\mathbb{C})$$) acts conformally on the Riemann sphere at infinity (splitting it into a domain of discontinuity and a fractal **limit set**, just like Fatou and Julia!) while simultaneously acting by isometries on **hyperbolic 3-space** $$\mathbb{H}^3$$ inside! **Dennis Sullivan** mapped out a deep dictionary between rational maps and Kleinian groups—and McMullen turned that dictionary into analytic proofs.

---

## 1. Hand-Verifiable Worked Examples: Iterating $$z^2 + c$$ and Pinching a Genus-2 Surface

### Example 1: Three concrete values of $$c$$ in $$f_c(z) = z^2 + c$$
1. **$$c = 0$$ ($$f_0(z) = z^2$$):** if $$\vert z\vert < 1$$, $$z^{2^n} \to 0$$; if $$\vert z\vert > 1$$, $$z^{2^n} \to \infty$$. The **Julia set** is the unit circle $$\vert z\vert = 1$$!
2. **$$c = -2$$ ($$f_{-2}(z) = z^2 - 2$$):** substitute $$z = 2\cos\theta$$ to get $$f_{-2}(2\cos\theta) = 4\cos^2\theta - 2 = 2\cos(2\theta)$$! The critical orbit is $$0 \mapsto -2 \mapsto 2 \mapsto 2 \cdots$$ (bounded, sitting at the leftmost tip of the Mandelbrot set), and the **Julia set** collapses to the real interval $$[-2, 2]$$!
3. **$$c = -1$$ ($$f_{-1}(z) = z^2 - 1$$):** the critical orbit cycles $$0 \mapsto -1 \mapsto 0 \cdots$$ (superattracting period 2), and the Julia set blooms into the famous **basilica** fractal.

Now picture **renormalization**: pick $$c$$ inside a tiny baby Mandelbrot copy of period $$p$$. Restricting the $$p$$-th iterate $$f_c^{\circ p}$$ to a small disk around $$0$$ yields a **quadratic-like map** (Douady–Hubbard) that behaves just like a new quadratic polynomial. While **Yoccoz** (Fields 1994) solved the *finitely* renormalizable case of density of hyperbolicity, McMullen’s 1994 monograph attacked the stubborn **infinitely renormalizable** regime via geometric towers!

### Example 2: Pinching a 2-holed torus ($$g = 2$$) to a maximal cusp on Bers’s boundary
Take a closed genus-2 surface $$S$$. Cutting along $$3g - 3 = 3$$ disjoint simple closed curves decomposes $$S$$ into two "pairs of pants," giving $$6g - 6 = 6$$ real Fenchel–Nielsen parameters (3 lengths and 3 twists) for $$\mathcal{T}(S)$$.
- **Bers** embedded $$\mathcal{T}(S)$$ as a bounded domain in holomorphic quadratic differentials.
- Pinching a waist curve’s length down to $$0$$ stretches the surface into two infinite funnels (**cusps**), landing on the **Bers boundary** $$\partial\mathcal{T}(S)$$.
- Pinching all $$3$$ waist curves simultaneously produces a **maximal cusp**.

**Bers’s conjecture (1970)** asked whether maximal cusps are **dense** across the entire Bers boundary. In *"Cusps are dense"* (*Ann. of Math.* 133, 1991), **McMullen proved yes!** Degeneration is not exceptional on the edge of Teichmüller space—it is dense everywhere.

---

## 2. Kra’s Theta-Function Conjecture and the Amenability Criterion

Any covering of hyperbolic Riemann surfaces $$Y \to X$$ induces an inclusion $$\mathcal{T}(X) \hookrightarrow \mathcal{T}(Y)$$ and, dually, the **Poincaré series operator** $$\Theta$$ averaging quadratic differentials from $$Y$$ down to $$X$$. Always $$\|\Theta\| \le 1$$; **Kra’s theta-function conjecture** asserted strict contraction $$\|\Theta\| < 1$$ for the universal cover $$\mathbb{D} \to X$$ of a finite-type surface.

In 1989 (*Invent. Math.* 97), **McMullen** proved a sweeping topological-analytic criterion:

$$
\|\Theta\| = 1 \quad \Longleftrightarrow \quad \text{the covering } Y \to X \text{ is amenable}.
$$

Because the fundamental group of a finite-type hyperbolic surface contains a free group (hence is *non-amenable*), strict contraction $$\|\Theta\| < 1$$ follows immediately—handing geometry a sharp fixed-point contraction engine!

---

## 3. Explanation: How Renormalization Unifies Complex Dynamics and 3-Manifolds

McMullen’s twin classics—*Complex Dynamics and Renormalization* (1994) and *Renormalization and 3-Manifolds Which Fiber over the Circle* (1996)—run the exact same 4-step argument in two dimensions and in three:

#### Step 1: Frame both worlds as fixed-point problems
- *Complex dynamics:* Renormalization $$\mathcal{R}$$ sends a quadratic-like map to a rescaled return map; rigidity asks whether the iterates converge to a unique **renormalization fixed point**.
- *3-manifolds:* Take $$S \times [0,1]$$ and glue $$S \times \{1\}$$ to $$S \times \{0\}$$ by a pseudo-Anosov twist $$\psi: S \to S$$ to form a **3-manifold fibering over the circle**. Putting a hyperbolic metric on it requires finding a **fixed point** of Thurston’s *skinning map* on $$\mathcal{T}(S)$$.

#### Step 2: Measure "flexibility" via quasiconformal deformations
To test whether two combinatorially equivalent systems must coincide (rigidity), assume a nontrivial quasiconformal deformation exists (an invariant field of infinitesimal ellipses on the Riemann sphere) and track how it transforms under iteration or covering.

#### Step 3: Contraction (Kra) and quantitative inflexibility crush deformations exponentially
Using his amenability contraction estimates (Kra’s theorem) and a new **quantitative inflexibility theorem** for open hyperbolic 3-manifolds (deepening Mostow rigidity), McMullen showed that deep inside a renormalization tower—or inside the infinite cyclic cover of a fibered 3-manifold—every quasiconformal deformation contracts **exponentially** to $$0$$!

#### Step 4: Clean boundary between McMullen and Perelman
This unified mechanism yields both rigidity for bounded-type infinitely renormalizable quadratic polynomials and a fresh, transparent proof of **Thurston’s hyperbolization theorem for 3-manifolds fibering over the circle**. Keep the credit clean: McMullen contributed renormalization and rigidity *inside* Thurston’s geometrization program; [Grigori Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) *completed* full geometrization (and the Poincaré conjecture) via Ricci flow with surgery.

Summary of McMullen’s bridge:

$$
\text{Sullivan’s dictionary}
\;\longrightarrow\;
\text{Bers (cusps dense) + Kra (}\|\Theta\| < 1\text{)}
\;\longrightarrow\;
\text{Renormalization rigidity (2D complex }\leftrightarrow\text{ 3D fibered)}.
$$

---

## 4. Lineage and Why a Fields Medal

The same conformal-dynamics sensibility passed directly to McMullen’s doctoral students at Harvard—most famously **Maryam Mirzakhani** (see [Mirzakhani’s own theorems]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/)).

**Why a Fields Medal 1998:** McMullen solved two longstanding named conjectures (**Bers** and **Kra**), turned renormalization from a metaphor into a sharp analytic engine bridging 2D complex dynamics and 3D hyperbolic geometry, and unified three major fields through shared compactness and rigidity mechanisms—alongside 1998 classmates **Borcherds**, **Gowers**, and **Kontsevich**.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “McMullen proved geometrization / Poincaré.” | Full geometrization is Perelman. McMullen contributed inside Thurston’s program (fibered hyperbolization / renormalization). |
| “Cusps dense means every Riemann surface has a cusp.” | The theorem is about *Bers’s boundary* of Teichmüller space, not about a typical smooth surface in the interior. |
| “Teichmüller space is moduli space.” | Teichmüller remembers markings; moduli quotients by the mapping class group. |
| “Julia set = Mandelbrot set.” | Julia lives in the dynamical plane of one map; Mandelbrot lives in the parameter plane of a family. |
| “Renormalization is just zooming a picture.” | It is a return-map construction with quadratic-like mappings and a rigidity theory. |
| “The medal is only Bers + Kra.” | Those are the named items; the citation also names holomorphic dynamics and 3-manifold geometrization culture. |
| “McMullen classified all rational maps.” | No. The work is rigidity, density, and renormalization, not a census of conjugacy classes. |

---

## Links

- IMU Fields Medal page: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- IMU Fields Medals 1998: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998)
- Wikipedia, Curtis T. McMullen: [https://en.wikipedia.org/wiki/Curtis_T._McMullen](https://en.wikipedia.org/wiki/Curtis_T._McMullen)
- McMullen’s Harvard page: [https://people.math.harvard.edu/~ctm/](https://people.math.harvard.edu/~ctm/)
- Course: [Mirzakhani / moduli]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/)
- arXiv search, McMullen dynamics: [https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all](https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all)

---

## References

1. Official Fields Medal 1998 citation for C. T. McMullen (IMU / ICM Berlin); see also Yuri Manin’s address as committee chair.
2. **S. Smale**, “The work of Curtis T. McMullen,” *Doc. Math.*, Extra Vol. ICM 1998.
3. **C. T. McMullen**, “Cusps are dense,” *Ann. of Math.* **133** (1991).
4. **C. T. McMullen**, “Amenability, Poincaré series and quasiconformal maps,” *Invent. Math.* **97** (1989) (Kra’s theta conjecture).
5. **C. T. McMullen**, *Complex Dynamics and Renormalization*, Ann. of Math. Studies **135**, Princeton, 1994.
6. **C. T. McMullen**, *Renormalization and 3-Manifolds Which Fiber over the Circle*, Ann. of Math. Studies **142**, Princeton, 1996.
7. Background: Douady–Hubbard on quadratic-like maps and the Mandelbrot set; Sullivan on Riemann surface laminations and the dictionary with Kleinian groups; Thurston on geometrization (Haken / fibered cases).
8. Course: [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/).

---

## Further directions

- Read Smale’s short ICM portrait before the 1994/1996 books.
- Compare Bers’s boundary with the boundary of the Mandelbrot set: both are conjecturally organized by laminations (Thurston; Douady–Hubbard); McMullen’s density of cusps supports one side of that analogy.
- Seminar A3: a one-page “dictionary” of three parallel words (rational map / Kleinian group; Julia set / limit set; renormalization / fibered hyperbolization)—without claiming the dictionary is an equivalence of categories.

## Video tham khảo

- **xem trước** — [Curtis McMullen: Manifolds, topology and dynamics](https://www.youtube.com/watch?v=g0fQDrV-UuE) — The Abel Prize, English. Watch first. “Curtis McMullen: Manifolds, topology and dynamics” orients the lesson’s aim: State the official 1998 citation and name its two explicitly cited theorems (Bers density of cusps; Kra’s theta-function conjecture).
- [Planes in number theory, geometry and dynamics: C. McMullen](https://www.youtube.com/watch?v=hlDDHnk5aRU) — Fields Institute, English. A second pass once the main claim is in view: State the official 1998 citation and name its two explicitly cited theorems (Bers density of cusps; Kra’s theta-function conjecture).
- [Dynamics on K3 Surfaces - Curtis McMullen](https://www.youtube.com/watch?v=gWTi1xvGMb8) — Stony Brook Mathematics, English. Further depth after the first two, still tied to this lesson: State the official 1998 citation and name its two explicitly cited theorems (Bers density of cusps; Kra’s theta-function conjecture).
