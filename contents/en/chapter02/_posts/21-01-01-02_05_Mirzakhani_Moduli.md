---
layout: post
title: "Mirzakhani and Moduli Spaces (Fields Medal 2014)"
chapter: '02'
order: 5
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Picture a billiard table shaped like an exotic polygon, and imagine striking a frictionless ball that rolls forever. Will its path close into a periodic loop, or will it eventually paint the entire table evenly? What sounds like a recreational puzzle leads straight into one of the most abstract and breathtaking landscapes of modern mathematics: the geometry of **curved surfaces** and the **space of all possible shapes** they can take—called **moduli space**.

In 2014, **Maryam Mirzakhani** (1977–2017) became the **first woman** in history to receive the **Fields Medal**, honored for transforming how mathematicians measure, count, and run dynamical systems on **Riemann surfaces** and their moduli spaces. Rather than treating moduli space as an ethereal abstraction, Mirzakhani made this "universe of shapes" both **computable** (exact recursive formulas for its volumes and curve counts) and **dynamical** (ergodic flows and the celebrated *Magic Wand Theorem* with Alex Eskin), uniting hyperbolic geometry, Teichmüller theory, and ergodic dynamics.

**Lesson roadmap:** Key ideas (hyperbolic geometry, moduli space via tori $$\mathbb{H}/\mathrm{SL}_2(\mathbb{Z})$$, ergodic theory) → Counting the $$6g-6$$ Fenchel–Nielsen coordinates by hand → Counting simple closed geodesics → Explanation: Weil–Petersson volumes, $$V_{1,1}(L)$$, and why counting on *one* surface integrates over *all* surfaces → Earthquake flow, billiards, and the Magic Wand Theorem.

---

## Learning objectives

After this lecture you should be able to:

- Define informally a **Riemann surface** of genus $$g \ge 2$$, its **hyperbolic metric**, **Teichmüller space**, and **moduli space**.
- Verify by hand why the moduli space of tori is $$\mathbb{H}/\mathrm{SL}_2(\mathbb{Z})$$ and why a genus-$$g$$ surface has exactly $$6g-6$$ Fenchel–Nielsen coordinates.
- State Mirzakhani's asymptotic growth law $$N_X(L) \sim c_X L^{6g-6}$$ for **simple closed geodesics**.
- Follow the four-step bridge connecting **Weil–Petersson volumes** (such as $$V_{1,1}(L) = \frac{1}{24}(L^2 + 4\pi^2)$$) to geodesic counting.
- Sketch **earthquake flow**, **translation surfaces** (unfolding polygonal billiards), and the **Magic Wand Theorem** with Alex Eskin.

**Prerequisites.** Surfaces of genus $$g$$ (sphere, torus, double torus), basic complex numbers, and asymptotic notation $$f(L) \sim cL^k$$. No prior Teichmüller theory assumed.

**Seminar links.** Geometry cousins: [Perelman / Ricci flow]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/), [Beautiful Mathematics / infinity and shape]({{ site.baseurl }}/contents/en/chapter04/04_02_Infinity/), [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/). Dynamics cousins in Ch.08: [Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/). Flat surfaces touch [tilings]({{ site.baseurl }}/contents/en/chapter04/04_10_Tilings/) and billiard intuition.

---

## Key ideas: Hyperbolic Geometry, Moduli Space, and Ergodic Theory

### 1. What Does Hyperbolic Geometry Study?
In flat Euclidean geometry, a triangle's angles sum to $$180^\circ$$ (curvature $$0$$). On a sphere, triangles bulge outward so angles sum to $$> 180^\circ$$ (curvature $$+1$$). **Hyperbolic geometry** is the saddle-shaped third world: constant negative curvature $$-1$$, angles summing to $$< 180^\circ$$, and triangle area equal to the angle defect $$\pi - (\alpha + \beta + \gamma)$$! Its standard model is the **upper half-plane** $$\mathbb{H} = \{x + iy : y > 0\}$$ with length element $$ds = \frac{\sqrt{dx^2 + dy^2}}{y}$$, where "straight lines" (**geodesics**) are vertical rays and semicircles meeting the real axis at right angles. By the **Uniformization Theorem**, every closed surface with **two or more holes** (genus $$g \ge 2$$) naturally carries a hyperbolic metric!

### 2. What Is Moduli Space? (Two Hand-Verifiable Examples)
A **moduli space** is a geometric space in which **each point represents an entire shape**:
- **Example 1 — All rectangles of area 1:** Every unit-area rectangle is determined by its aspect ratio $$r \ge 1$$, so the moduli space of unit-area rectangles is simply the ray $$[1, \infty)$$.
- **Example 2 — Moduli space of tori ($$g = 1$$):** Glue opposite sides of a parallelogram in $$\mathbb{C}$$ spanned by $$1$$ and $$\tau$$ ($$\operatorname{Im}\tau > 0$$) to form a torus. Two parameters $$\tau, \tau'$$ produce the *same* torus shape (same lattice up to rotation/scaling) precisely when $$\tau' = \frac{a\tau + b}{c\tau + d}$$ for a matrix $$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathrm{SL}_2(\mathbb{Z})$$! For instance, $$\tau = i$$ (a square) and $$\tau' = i + 1$$ (a $$45^\circ$$ sheared parallelogram) generate the exact same square lattice $$\mathbb{Z}[i]$$, so they represent the **same point** in $$\mathcal{M}_1 = \mathbb{H}/\mathrm{SL}_2(\mathbb{Z})$$!

### 3. Ergodic Theory — Why Step Out of One Surface into Moduli Space?
Ergodic theory asks whether long-term time averages along a typical orbit equal space averages. Rather than standing on *one* fixed hyperbolic surface $$X$$ and trying to list its tangled simple geodesics by hand, Mirzakhani stepped back into **moduli space $$\mathcal{M}_g$$**, using volume integration and ergodic flows on the space of *all* surfaces to solve the counting problem on $$X$$!

---

## 1. Pairs of Pants and Counting the $$6g - 6$$ Coordinates by Hand

For $$g \ge 2$$, **Teichmüller space** $$\mathcal{T}_g$$ parametrizes *marked* hyperbolic surfaces (remembering labels of curves), while **moduli space** $$\mathcal{M}_g = \mathcal{T}_g / \mathrm{Mod}_g$$ quotients out relabelings by the **mapping class group** $$\mathrm{Mod}_g$$.

**Verify $$\dim_{\mathbb{R}} \mathcal{T}_g = 6g - 6$$ by hand:** Cut a $$g$$-holed donut along disjoint simple closed curves into the smallest possible pieces: each piece is a **pair of pants** (a sphere with 3 holes removed, Euler characteristic $$\chi = 2 - 3 = -1$$).
- Since Euler characteristic adds along circles ($$\chi(S^1) = 0$$), a genus-$$g$$ surface ($$\chi = 2 - 2g$$) decomposes into exactly **$$2g - 2$$ pairs of pants**.
- Those pants have $$3(2g - 2) = 6g - 6$$ boundary cuffs, glued in pairs along **$$3g - 3$$ cutting curves**.
- A hyperbolic pair of pants is uniquely fixed by its 3 cuff lengths, giving **$$3g - 3$$ length parameters** $$(\ell_1, \dots, \ell_{3g-3})$$. Gluing each cuff pair allows an arbitrary twist angle, adding **$$3g - 3$$ twist parameters** $$(\theta_1, \dots, \theta_{3g-3})$$.

Total: $$(3g - 3) + (3g - 3) = \mathbf{6g - 6}$$ real **Fenchel–Nielsen coordinates**! For a 2-holed torus ($$g = 2$$): **2 pairs of pants**, **3 cuts**, and **6 coordinates**!

---

## 2. Counting Simple Closed Geodesics

On a fixed hyperbolic surface $$X$$ of genus $$g \ge 2$$, self-intersecting closed geodesics proliferate exponentially ($$\sim e^L/L$$). Restricting to **simple** (non-self-intersecting) closed geodesics makes them far more rigid, and Mirzakhani proved polynomial growth:

$$
N_X(L) \;\sim\; c_X\, L^{6g-6} \qquad (L \to \infty).
$$

The exponent $$6g - 6$$ matches the real dimension of moduli space! Even more remarkably, Mirzakhani determined exact ratios between topological curve types: on a genus-2 surface, a long random simple closed geodesic is **48 times** more likely to be non-separating than to cut the surface into two pieces—a crisp rational ratio read straight off moduli-space volumes!

---

## 3. Explanation: From Counting on One Surface to Volumes of Moduli Space

#### Step 1: The Weil–Petersson Volume Form
By Wolpert's theorem, the **Weil–Petersson (WP)** symplectic form in Fenchel–Nielsen coordinates is astonishingly simple:

$$
\omega_{\mathrm{WP}} = \sum_{i=1}^{3g-3} d\ell_i \wedge d\theta_i.
$$

Taking its top exterior power yields a natural volume $$V_{g,n}(L_1, \dots, L_n)$$ on the moduli space $$\mathcal{M}_{g,n}(L_1, \dots, L_n)$$ of genus-$$g$$ surfaces with $$n$$ geodesic boundaries of lengths $$L_1, \dots, L_n$$.

#### Step 2: Mirzakhani's Volume Recursion (Check $$V_{1,1}(L)$$ by Hand!)
Shooting geodesic rays perpendicularly inward from boundary $$L_1$$ and recording which ray first hits itself or a boundary splits $$L_1$$ into a sum over pairs of pants containing $$L_1$$ (a **generalized McShane identity**). Integrating over moduli space yields an explicit **recursion** computing $$V_{g,n}$$ from simpler surfaces! For a one-holed torus ($$g = 1, n = 1$$) with boundary length $$L$$, Mirzakhani's recursion gives the clean quadratic polynomial:

$$
V_{1,1}(L) = \frac{1}{24}\bigl(L^2 + 4\pi^2\bigr).
$$

Check the cusp limit $$L \to 0$$: $$V_{1,1}(0) = \frac{\pi^2}{6}$$, recovering the classical WP volume of the modular surface! In general, every $$V_{g,n}(L_1, \dots, L_n)$$ is a **polynomial in $$L_1^2, \dots, L_n^2$$** whose top coefficients encode intersection numbers on moduli space—yielding a breathtaking new geometric proof of the **Witten–Kontsevich conjecture** from 2D quantum gravity.

#### Step 3: Integrating "Curve Counts" Turns into Integrating WP Volumes
Fix a topological curve type $$\gamma$$. Integrating the count of $$\gamma$$-type curves of length $$\le L$$ over *all* surfaces $$X \in \mathcal{M}_g$$ lets you swap the order of integration: instead of fixing $$X$$ and summing over curves, **cut the surface along a curve of length $$\ell \le L$$** and integrate the volume $$V_{g', n'}(\ell, \ell)$$ of the remaining surface from $$\ell = 0$$ to $$L$$! Since $$V_{g',n'}$$ has degree $$6g - 8$$ in $$\ell$$ (times a twist factor $$\ell$$), $$\int_0^L \ell \cdot \ell^{6g-8}\,d\ell$$ immediately produces the exact exponent **$$L^{6g-6}$$**!

#### Step 4: Ergodicity of Earthquake Flow Pins Down Each Individual Surface $$X$$
Step 3 computes the *average* over $$\mathcal{M}_g$$. To show the asymptotic holds for every *individual* surface $$X$$, Mirzakhani proved **ergodicity of Thurston's earthquake flow** (shearing a surface along measured laminations like geological fault lines), guaranteeing that long curves equidistribute across moduli space.

$$
\text{Pants decomposition}
\;\xrightarrow{\text{Recursion}}\;
\text{Polynomial } V_{g,n}(L)
\;\xrightarrow{\text{Swap integrals}}\;
\text{Average } \sim L^{6g-6}
\;\xrightarrow{\text{Ergodicity}}\;
N_X(L) \sim c_X L^{6g-6}.
$$

---

## 4. Flat Surfaces, Polygonal Billiards, and the "Magic Wand Theorem"

Return to the polygonal billiard table from the opening: every time the ball bounces off an edge, *reflect the entire table* across that edge so the ball travels in a straight line! Gluing reflected copies together produces a **translation surface** (a flat surface with cone singularities). The matrix group $$\mathrm{SL}_2(\mathbb{R})$$ acts naturally on the space (strata) of translation surfaces by stretching and shearing.

In their landmark 2013 paper—dubbed the **"Magic Wand Theorem"**—**Alex Eskin and Maryam Mirzakhani** (with Amir Mohammadi) proved that every $$\mathrm{SL}_2(\mathbb{R})$$-invariant measure and orbit closure on these strata is remarkably rigid (an affine submanifold), bringing Ratner-style rigidity into Teichmüller dynamics and transforming the study of polygonal billiards.

**Attribution note:** Mirzakhani was the first woman and first Iranian mathematician to win the Fields Medal (2014). Many major dynamical results are joint—especially with **Alex Eskin**; always check coauthorship for specific theorems.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Moduli space is the surface itself.” | A point of moduli space *is* a surface (up to isomorphism); moduli space is the higher-dimensional universe of all such shapes. |
| “Teichmüller space and moduli space are the same.” | Teichmüller remembers markings; moduli quotients by the mapping class group: $$\mathcal{M}_g \simeq \mathcal{T}_g/\mathrm{Mod}_g$$. |
| “She only counted geodesics.” | WP volume recursions, Witten's conjecture, earthquake dynamics, and the Magic Wand Theorem are equally central. |
| “Simple closed geodesics are just any closed curves.” | Simple means non-self-intersecting; geodesics are locally length-minimizing representatives. |
| “Ergodicity means every orbit is periodic.” | Ergodicity is a measure-theoretic property: time averages equal space averages for almost every orbit. |

---

## Video sources (math-video-researcher pack)

Full ranking: `research/video-research/Mirzakhani_Moduli/`.

**Recommended order**

1. **Orientation** — Quanta/Simons, *Maryam Mirzakhani: A Tenacious Explorer of Abstract Surfaces*: [YouTube](https://www.youtube.com/watch?v=qNuh4uta8oQ).  
2. **Profile** — Quanta article: [A Tenacious Explorer of Abstract Surfaces](https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/).  
3. **Core** — IAS Morse lecture listing (moduli dynamics): [IAS](https://www.ias.edu/ideas/dynamics-moduli-spaces-curves-i).  
4. **Frontier reading** — Eskin–Mirzakhani “magic wand”: [arXiv:1302.3320](https://arxiv.org/abs/1302.3320).

**Status reminder:** Major moduli/dynamics theorems **proved**; moduli geometry remains an active field. Biography is culturally important; the syllabus reason is the mathematics.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Mirzakhani_Moduli/transcripts/` · status: `research/video-research/Mirzakhani_Moduli/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Mirzakhani_Moduli_qNuh4uta8oQ_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


Full URL bibliography from video research (including secondary finds): `research/video-research/Mirzakhani_Moduli/references.md`.

### Complete URL list (audit)

1. https://www.youtube.com/watch?v=qNuh4uta8oQ  
2. https://www.ias.edu/ideas/dynamics-moduli-spaces-curves-i  
3. https://arxiv.org/abs/1302.3320  
4. https://arxiv.org/abs/1305.3015  
5. https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/  
6. https://en.wikipedia.org/wiki/Maryam_Mirzakhani  
7. https://celebratio.org/Mirzakhani_M/article/1087/  
8. https://terrytao.wordpress.com/tag/maryam-mirzakhani/  
9. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014  
10. https://arxiv.org/search/?query=Mirzakhani+Weil-Petersson&searchtype=all  
11. https://news.stanford.edu/stories/2014/08/surfaces-mirzakhani-081214  

### Research pack

12. Course pack: `research/video-research/Mirzakhani_Moduli/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. IMU Fields Medal 2014 citation — Maryam Mirzakhani.
2. M. Mirzakhani — thesis and papers on Weil–Petersson volumes and counting simple closed geodesics.
3. A. Eskin & M. Mirzakhani — ergodicity of earthquake flow; related dynamics papers.
4. Surveys on Teichmüller dynamics, strata of abelian differentials, and orbit closures (various authors; lecture notes from graduate summer schools).
5. W. Thurston — foundations of earthquake deformations and measured laminations (background).
6. Course cross-links: [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/), [Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/), [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/).

---

## Further directions

- Read a short survey on WP volume recursions and compute a low-genus volume by hand.
- Explore flat surfaces and rational billiards as a sister seminar topic; compare counting periodic trajectories with counting simple geodesics.
- Compare Mirzakhani’s “moduli as a dynamical arena” with homogeneous dynamics in the [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/) essay—different spaces, shared ergodic philosophy.

## Video tham khảo

- **xem trước** — [Maryam Mirzakhani: A Tenacious Explorer of Abstract Surfaces](https://www.youtube.com/watch?v=qNuh4uta8oQ) — Quanta Magazine, English. Watch first. Portrait of Mirzakhani and the abstract surfaces she studied.
- [Dynamics on the Moduli Spaces of Curves, I - Maryam Mirzakhani](https://www.youtube.com/watch?v=8Az_W2wv4Zo) — Institute for Advanced Study, English. Mirzakhani's own lecture on dynamics on moduli spaces of curves.
- [Maryam Mirzakhani, Dynamics Moduli Spaces of Curves I](https://www.youtube.com/watch?v=tprlQMClSYQ) — Harvard Mathematics Department, English. Further depth from Mirzakhani's lecture series.
