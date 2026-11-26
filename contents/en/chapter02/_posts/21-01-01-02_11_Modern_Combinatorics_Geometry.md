---
layout: post
title: "June Huh and Modern Combinatorics–Geometry (Fields Medal 2022)"
chapter: '02'
order: 15
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

In high school, **June Huh** dropped out to write poetry. He did not fall in love with mathematics until his final year of college, when the legendary Fields Medalist Heisuke Hironaka visited Seoul National University and sparked a fascination with algebraic singularities. Less than fifteen years later, Huh stood on the stage of the 2022 Fields Medal ceremony—recognized for solving a string of fifty-year-old counting conjectures that had baffled combinatorialists for generations.

His secret? **Seeing hidden smooth geometry inside purely discrete counting problems.**

Ask a graph theorist how many ways you can color a network with $$q$$ colors so no two connected vertices share a color. You get a polynomial whose coefficients always rise to a single peak and then fall—and even more mysteriously, every coefficient squared is at least the product of its two neighbors (**log-concavity**). For half a century, nobody could prove this elementary-looking inequality for all graphs, let alone for their abstract cousins called **matroids**. Huh—together with Karim Adiprasito, Eric Katz, Petter Brändén, and others—imported the heavy machinery of **Hodge theory** from complex algebraic geometry straight into combinatorics, proving log-concavity even when no geometric variety exists at all!

This lesson serves two complementary roles: it is a **portrait of June Huh’s Fields Medal 2022 breakthrough** (complete with hand-checkable chromatic polynomials and matroids), and a **method map** showing how modern combinatorics trades tools with geometry, analysis, and computer science across Chapter 2.

---

## Learning objectives

After this lecture you should be able to:

- Compute chromatic polynomials of $$K_3$$ and $$K_4$$ by hand and verify **log-concavity** directly on their coefficients.
- Explain what a **matroid** is using a concrete 3-vector / triangle-graph example.
- Articulate **June Huh’s** Fields Medal breakthrough: building a combinatorial **Hodge package** (Chow ring, Hodge–Riemann relations) and **Lorentzian polynomials** to prove Read’s, Heron–Rota–Welsh, Dowling–Wilson, and strong Mason conjectures.
- Name five major bridges between combinatorics and geometry/analysis: **additive combinatorics**, **incidence geometry**, **spectral expanders**, the **polynomial method**, and **combinatorial Hodge theory**.
- Use this essay as a routing map connecting [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/), [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/), [Maynard]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/), and [Wang / Kakeya]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/).

**Prerequisites.** Graphs, basic counting, linear independence of vectors in $$\mathbb{R}^2$$, and eigenvalues of symmetric matrices.

**Related lessons.** Jump to [Chapter 7 explorations]({{ site.baseurl }}/contents/en/chapter07/) for hands-on discrete-geometry experiments, and to [Chapter 1 problem maps]({{ site.baseurl }}/contents/en/chapter01/) where combinatorial questions meet open analytic conjectures.

---

## Key ideas: Why Do Discrete Counting and Smooth Geometry Need Each Other?

At university, combinatorics (counting graphs, subsets, and colorings) and algebraic geometry (curved manifolds cut out by polynomials) are usually taught in completely different buildings. Modern mathematics thrives precisely where those two buildings connect.

### 1. Combinatorics & Matroids: The Abstract Essence of Independence
**What is it?** Combinatorics counts discrete structures—graphs, networks, subsets, tilings. A **matroid** distills the notion of "independence" that appears identically in two different worlds: linearly independent sets of vectors in linear algebra, and cycle-free forests of edges in graph theory.

**What does it study?**
- **Chromatic & characteristic polynomials:** Generating polynomials whose coefficients count colorings, independent sets, or regions of hyperplane arrangements.
- **Unimodality & log-concavity:** A sequence of positive numbers $$a_0, a_1, \dots, a_d$$ is **log-concave** if $$a_k^2 \ge a_{k-1} a_{k+1}$$ for every $$k$$ (which automatically forces it to rise to a single peak and then fall—**unimodality**). Proving log-concavity by raw counting is often hopeless; geometry turns it into a quadratic inequality!

### 2. Hodge Theory (from Algebraic Geometry): The Engine of Positivity
**What is it?** On a smooth complex projective variety (like a complex torus or a smooth hypersurface), **Hodge theory** studies the cohomology ring—an algebraic record of how sub-shapes intersect each other.

**What does it study?**
- **The Kähler / Hodge package:** Three miracle properties—Poincaré duality, Hard Lefschetz, and the **Hodge–Riemann bilinear relations**. Crucially, the Hodge–Riemann relations say a certain intersection pairing has a strict signature (one positive sign, the rest negative), which instantly spits out Cauchy–Schwarz-style inequalities of the form $$a_k^2 \ge a_{k-1}a_{k+1}$$!

### 3. Incidence Geometry, Expanders & the Polynomial Method
**What is it?** Beyond Hodge theory, three other geometric toolkits now power combinatorics:
- **Incidence geometry:** Counting how many times points and lines (or thin tubes) can meet—directly dual to Kakeya problems in harmonic analysis.
- **Spectral expanders:** Sparse graphs whose adjacency-matrix eigenvalue gap mimics the curvature/Cheeger constant of a smooth manifold.
- **The polynomial method:** Trapping a discrete point set inside the zero locus of a low-degree polynomial to force rigid counting bounds.

---

## 1. June Huh: Hodge theory without a variety (Fields Medal 2022)

Before diving into the wider method map, let us get our hands dirty with the exact phenomenon that launched June Huh’s career.

### Hand-Verifiable Example 1: Chromatic Polynomials & Log-Concavity for $$K_3$$ and $$K_4$$
How many ways can you color the vertices of a graph $$G$$ using $$q$$ available colors so that no two adjacent vertices receive the same color?

1. **The triangle graph $$K_3$$ (3 mutually connected vertices):**
   Pick a color for vertex 1 ($$q$$ choices), a different color for vertex 2 ($$q-1$$ choices), and a third color distinct from both for vertex 3 ($$q-2$$ choices):
   $$
   \chi_{K_3}(q) = q(q-1)(q-2) = q^3 - 3q^2 + 2q.
   $$
   Take the absolute values of the coefficients: $$(a_3, a_2, a_1) = (1, 3, 2)$$. Check log-concavity by hand:
   $$
   3^2 = 9 \;\ge\; 1 \times 2 = 2. \quad \checkmark
   $$
2. **The tetrahedron graph $$K_4$$ (4 mutually connected vertices):**
   $$
   \chi_{K_4}(q) = q(q-1)(q-2)(q-3) = q^4 - 6q^3 + 11q^2 - 6q.
   $$
   Absolute values of the coefficients: $$(1, 6, 11, 6)$$. Check both interior terms by hand:
   $$
   6^2 = 36 \;\ge\; 1 \times 11 = 11 \;\checkmark,
   \qquad
   11^2 = 121 \;\ge\; 6 \times 6 = 36 \;\checkmark!
   $$

Ronald Read conjectured in 1968 that the absolute values of the coefficients of **every** graph’s chromatic polynomial are unimodal; Hoggar (1974) strengthened this to **log-concave**; and Heron, Rota, and Welsh extended the conjecture to **every matroid**.

### Hand-Verifiable Example 2: What Is a Matroid? (3 Vectors = 1 Triangle)
Take three vectors in $$\mathbb{R}^2$$:
$$
v_1 = (1,0), \qquad v_2 = (0,1), \qquad v_3 = (1,1).
$$
Which subsets of $$\{v_1, v_2, v_3\}$$ are linearly independent?
- Any single vector: $$\{v_1\}, \{v_2\}, \{v_3\}$$.
- Any pair of vectors: $$\{v_1, v_2\}, \{v_1, v_3\}, \{v_2, v_3\}$$.
- **Not** all three together, because $$v_1 + v_2 - v_3 = (0,0)$$!

Now compare that with the 3 edges $$\{e_1, e_2, e_3\}$$ of the triangle graph $$K_3$$! Which edge subsets contain no cycle? Any single edge, any pair of edges, and **not** all three together (which form a triangle cycle)! The list of independent subsets is **100% identical**. A **matroid** is the abstract combinatorial object recording that exact family of independent sets—even for exotic matroids that **cannot** be realized by vectors over any field at all!

---

### Explanation: How Huh Proved Log-Concavity Without Geometry

Why did a 50-year-old counting conjecture suddenly surrender to complex algebraic geometry? Follow the four-step arc slowly:

#### Step 1: Realizable graphs & matroids hide a genuine algebraic variety
In 2012, as a PhD student, June Huh realized that for a graph (or a vector-realizable matroid), the coefficients $$a_k$$ of the chromatic/characteristic polynomial secretly equal **intersection numbers** (Milnor numbers / mixed multiplicities) on a smooth projective variety built by blowing up hyperplane arrangements! Once the numbers live on a smooth algebraic variety, the classical **Hodge–Riemann bilinear relations** immediately force $$a_k^2 \ge a_{k-1}a_{k+1}$$, proving Read’s 1968 conjecture!

#### Step 2: The wall—most matroids have NO algebraic variety!
Wait: what about **non-realizable matroids** (which make up almost all matroids)? There is no vector space, no hyperplane arrangement, and no complex manifold to apply classical Hodge theory to. That is why Heron–Rota–Welsh remained wide open.

#### Step 3: Build the "Hodge package" purely combinatorially (Adiprasito–Huh–Katz, 2018)
Karim Adiprasito, June Huh, and Eric Katz asked a daring question: *What if you keep the algebraic shadow—the **Chow ring $$A^*(M)$$** of the matroid—and prove Poincaré duality, Hard Lefschetz, and Hodge–Riemann directly on that finite-dimensional combinatorial ring by induction, without ever needing an underlying variety?* They pulled it off! Every matroid—realizable or not—obeys the Kähler package, immediately proving the **Heron–Rota–Welsh conjecture**.

#### Step 4: Distill positivity into Lorentzian polynomials (Brändén–Huh, 2020)
Even better: with Petter Brändén, Huh abstracted the essence of Hodge–Riemann signature into a sleek analytic class called **Lorentzian polynomials**—homogeneous polynomials whose Hessian matrices have at most one positive eigenvalue. That analytic engine effortlessly conquered the **strong Mason conjecture** (ultra-log-concavity of independent-set counts in every matroid) and opened bridges to optimization, sampling algorithms, and convex geometry.

In one schematic line:

$$
\text{Discrete graph / matroid }M
\;\xrightarrow{\;\text{Chow ring }A^*(M)\;}\;
\text{Combinatorial Hodge–Riemann}
\;\xrightarrow{\;\text{signature }(+, -, \dots, -)\;}\;
a_k^2 \ge a_{k-1}a_{k+1}.
$$

---


### Short Video 1: Chromatic Polynomials, Log-Concavity & Combinatorial Hodge Theory

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/huh-chromatic-logconcave_en.mp4"></video>
</div>

Short visual overview (36 sec): hand-checking K₃ and K₄ chromatic coefficients, Read's conjecture, and Adiprasito–Huh–Katz's Hodge theory on matroid Chow rings.

## 2. Structure versus randomness: additive combinatorics

Stepping back onto the broader Chapter 2 method map, **additive combinatorics** studies sumsets

$$
A+A=\{a+a':a,a'\in A\},
$$

difference sets, arithmetic progressions, and approximate groups inside abelian groups ($$\mathbb{Z}$$, $$\mathbb{Z}/N\mathbb{Z}$$, $$\mathbb{F}_p^n$$). Its guiding dichotomy is **structure versus randomness**:

- A **structured** set (an arithmetic progression or subgroup) has small doubling: $$\lvert A+A\rvert$$ is only a small constant times $$\lvert A\rvert$$.
- A **random-like** set has large doubling and noise-like Fourier coefficients.

**Szemerédi’s theorem** guarantees arbitrarily long arithmetic progressions in any dense subset of $$\mathbb{Z}$$. The primes have density zero, yet [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) transferred Szemerédi’s theorem into the primes by embedding them inside a **pseudorandom majorant**.

---

## 3. Incidence geometry: points, lines, and tubes

**Incidence geometry** asks how often points and lines (or thin tubes) can intersect. The classical **Szemerédi–Trotter theorem** bounds the number of point–line incidences $$I(P,L)$$ in $$\mathbb{R}^2$$:

$$
I(P,L)\;\ll\; \lvert P\rvert^{2/3}\lvert L\rvert^{2/3}+\lvert P\rvert+\lvert L\rvert.
$$

Why does this matter beyond discrete puzzles?

- Counting incidences is dual to controlling **overlaps of thin tubes**—the exact geometry powering restriction theory and Kakeya sets ([Wang / Kakeya]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/) and [Chapter 1 Kakeya map]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/)).
- Incidence bounds power **distinct distances** problems (Erdős; Guth–Katz in the plane).
- They provide sharp extremal benchmarks that continuous harmonic analysis must respect.

---

## 4. Spectral graphs and expanders

An **expander graph** is sparse yet fiercely connected: every subset of vertices has a large boundary relative to its size. Equivalently, for regular graphs, the **spectral gap** between the top two eigenvalues of the adjacency matrix is bounded away from zero.

Expansion is geometry without Riemannian metrics: random walks mix fast (analysis), cuts stay large (isoperimetry), and embeddings distort distances (metric geometry). **High-dimensional expanders** lift these ideas from graphs to simplicial complexes, uniting combinatorics, topology, and theoretical computer science.

---

## 5. The polynomial method

The **polynomial method** proves combinatorial bounds by constructing a low-degree polynomial vanishing on a configuration and extracting geometric constraints from its zeros and derivatives:

- **Dvir’s theorem (2008):** Solved the finite-field Kakeya conjecture in a breathtaking two-page proof using vanishing polynomials over $$\mathbb{F}_q^n$$.
- **Guth–Katz (2015):** Resolved the Erdős distinct distances problem in the plane (up to a logarithmic factor) via **polynomial partitioning** of $$\mathbb{R}^3$$.
- **Combinatorial Nullstellensatz (Alon):** Extracts existence results directly from leading coefficients.

---


### Short Video 2: Lorentzian Polynomials & Five Bridges of Modern Combinatorics

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/huh-lorentzian-bridges_en.mp4"></video>
</div>

Short visual walkthrough (33 sec): the Lorentzian Hessian signature (+, −, …, −) of Brändén–Huh (2020) and the five geometric bridges uniting modern combinatorics.

## 6. Packing, coloring, and other geometric peaks on the map

Several Chapter 2 portraits sit along this shared combinatorial–geometric mountain range:

| Peak | Combinatorial face | Geometric / analytic face |
|------|--------------------|---------------------------|
| [Viazovska packing]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/) | Sphere packing density, lattice enumerations | Modular forms, Fourier optimization (Cohn–Elkies) |
| [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) | Arithmetic progressions in sparse sets | Pseudorandomness, transference, ergodic ideas |
| [Maynard primes]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/) | Bounded prime gaps and constellations | Multidimensional sieve weights |
| [Wang / Kakeya]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/) | Directional tube configurations | Restriction, decoupling, measure vs. dimension |
| **June Huh (Fields 2022)** | Chromatic & characteristic polynomials of matroids | Combinatorial Hodge–Riemann / Lorentzian positivity |
| Four color theorem | Planar graph coloring | Topology of the plane; computer-assisted verification |

Modern combinatorics is a **trading zone**: analysts import extremal configurations; combinatorialists import Hodge theory, Fourier analysis, and algebraic geometry; computer scientists import expanders. The Fields Medals of the last two decades repeatedly celebrate mathematicians who speak several of these dialects fluently.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Green–Tao is only about dense sets.” | Primes are sparse; the point is transferring dense-set theorems into a sparse host. |
| “Incidences are just olympiad counting.” | Incidence geometry is central to modern discrete geometry and interacts deeply with harmonic analysis. |
| “Expanders are only a CS gadget.” | Spectral expansion is a geometric isoperimetric notion with wide pure-math applications. |
| “The polynomial method needs schemes.” | Many core applications use elementary vanishing and degree bounds over fields. |
| “This survey replaces the packing / Kakeya lectures.” | It indexes them; it does not replace their dedicated essays. |
| “Four color is unrelated to modern combinatorial geometry.” | It is a classical peak on the same map: topology constraining discrete structure. |
| “Huh classified all matroids.” | He (with collaborators) proved Hodge-theoretic positivity theorems (log-concavity, Mason, Dowling–Wilson); classification is not the theorem. |

---

## Video sources (math-video-researcher pack)

Use videos and primary sources for **orientation and research culture**. Full ranking and Mode B notes: `research/video-research/Modern_Combinatorics_Geometry/`.

**Recommended order**

1. **Orientation** — Numberphile, *g-conjecture* (June Huh): [YouTube](https://www.youtube.com/watch?v=4445Mbw8pYg).  
2. **Meta** — Simons / IMU Fields Medal videos (Huh): [Simons YT](https://www.youtube.com/watch?v=yO8lQWb6TZ4) · [IMU YT](https://www.youtube.com/watch?v=ritFtfoRYmY).  
3. **Profile** — Quanta: [He Dropped Out to Become a Poet. Now He’s Won a Fields Medal](https://www.quantamagazine.org/june-huh-high-school-dropout-wins-the-fields-medal-20220705/).  
4. **Optional extra** — Numberphile2 g-conjecture footage: [YouTube](https://www.youtube.com/watch?v=cFKGX3vAs_Q).

**Status reminder:** Medal work imports Hodge-theoretic ideas into combinatorics (matroids, log-concavity, Dowling–Wilson / Rota-type results)—not “only counting tricks.”

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Modern_Combinatorics_Geometry/transcripts/` · status: `research/video-research/Modern_Combinatorics_Geometry/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Modern_Combinatorics_Geometry_4445Mbw8pYg_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


Full URL bibliography from video research (including secondary finds): `research/video-research/Modern_Combinatorics_Geometry/references.md`.

### Complete URL list (audit)

1. https://www.simonsfoundation.org/2022/07/05/fields-medal-video-june-huh/  
2. https://arxiv.org/search/?query=Huh+matroid+Hodge&searchtype=all  
3. https://www.quantamagazine.org/june-huh-high-school-dropout-wins-the-fields-medal-20220705/  
4. https://www.ias.edu/scholars/june-huh  
5. https://en.wikipedia.org/wiki/June_Huh  
6. https://web.math.princeton.edu/~huh/  
7. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022  
8. https://www.youtube.com/watch?v=4445Mbw8pYg  
9. https://www.youtube.com/watch?v=cFKGX3vAs_Q  
10. https://www.youtube.com/watch?v=yO8lQWb6TZ4  
11. https://www.youtube.com/watch?v=ritFtfoRYmY  
12. https://arxiv.org/search/?query=Adiprasito+Huh+Katz&searchtype=all  
13. https://www.numberphile.com/videos/category/June+Huh  

### Research pack

14. Course pack: `research/video-research/Modern_Combinatorics_Geometry/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. **T. Tao and V. Vu**, *Additive Combinatorics*, Cambridge University Press.
2. Surveys on incidence geometry and the polynomial method (Guth; Zahl; Tao’s blog notes).
3. **S. Hoory, N. Linial, A. Wigderson**, “Expander graphs and their applications,” *Bull. AMS* — standard survey entry.
4. Cross-links in this course: [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/), [Maynard]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/), [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/), [Wang]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/), [Kakeya map]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/).
5. Classical: Appel–Haken four color theorem expositions (for the “topology constrains coloring” peak).

---

## Further directions

- Jump to [Explorations (Chapter 7)]({{ site.baseurl }}/contents/en/chapter07/) for discrete-geometry studio topics.
- Build a personal reading list of five survey first pages—one per method family on this map.
- Seminar option: present a 10-minute “method passport” (definitions only, no full proofs) for either incidences or expanders.
- Note open questions this survey raises: high-dimensional incidence bounds, explicit expanders with extreme parameters, and the ongoing dialogue between Kakeya-type analysis and discrete geometry.

## Video tham khảo

- **xem trước** — [g-conjecture - Numberphile](https://www.youtube.com/watch?v=4445Mbw8pYg) — Numberphile, English. Watch first. “g-conjecture - Numberphile” orients the lesson’s aim: Name at least five bridges between combinatorics and geometry or analysis.
- [Fields Medal: June Huh](https://www.youtube.com/watch?v=yO8lQWb6TZ4) — Simons Foundation, English. A second pass once the main claim is in view: Name at least five bridges between combinatorics and geometry or analysis.
- [Fields Medals 2022 June Huh](https://www.youtube.com/watch?v=ritFtfoRYmY) — International Mathematical Union, English. Further depth after the first two, still tied to this lesson: Name at least five bridges between combinatorics and geometry or analysis.
