---
layout: post
title: "Dennis Sullivan: Topology, Dynamics, and Geometry (Abel 2022)"
chapter: '08'
order: 7
owner: Nguyen Le Linh
lang: en
categories:
- chapter08
lesson_type: required
---

If a mathematician spends decades cutting and gluing five- and six-dimensional curved manifolds in geometric topology, would you ever expect him to walk into the fractal world of Julia sets and cleanly settle a conjecture that had stood open for more than sixty years since Pierre Fatou? To most people, classifying high-dimensional manifolds and studying chaos under iterated complex functions look like distant continents. To **Dennis Parnell Sullivan**, they are simply different dialects of the same language of **shape and transformation**.

In **2022**, **Dennis Parnell Sullivan** (Stony Brook University; CUNY Graduate Center) received the **Abel Prize**:

> “for his groundbreaking contributions to topology in its broadest sense, and in particular its algebraic, geometric and dynamical aspects.”  
> — [Abel Prize Committee citation](https://abelprize.no/abel-prize-laureates/2022)

The committee praised him for repeatedly changing the landscape of topology, moving among algebraic, analytic, and geometric ideas “like a true virtuoso.” This lecture traces Sullivan’s arc across topology **and** dynamics—including his famous **no wandering domains** theorem—and contrasts a lifetime virtuoso career with single-theorem epics like Perelman’s proof of Poincaré via Ricci flow. Official materials: [abelprize.no](https://abelprize.no/).

**Lesson arc:** Key ideas (algebraic topology, geometric topology, complex dynamics) → Four landmark themes → Explanation: computing orbits of $$f(z) = z^2 - 1$$ by hand and Sullivan’s dimension-counting contradiction → Julia sets and Fatou classification → Comparing Sullivan and Perelman.

---

## Learning objectives

After this lecture you should be able to place Sullivan across algebraic topology, geometric topology, and complex dynamics; name the no wandering domains theorem for rational maps and state what a wandering Fatou component would be; explain “geometric structures on spaces” as a unifying theme; contrast lifetime topology with single-theorem epics (e.g. [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/)); and avoid reducing Abel 2022 to only one result.

**Prerequisites.** Comfort with continuous maps, basic topology vocabulary (open sets, manifolds at slogan level), and the idea of iterating a function $$f$$, $$f\circ f$$, $$f^{\circ n}$$. Complex analysis beyond “functions of a complex variable exist” is not required on a first pass.

---

## Key ideas: What Are Algebraic Topology, Geometric Topology, and Complex Dynamics, and What Do They Study?

The three phrases in Sullivan’s citation sound specialized, yet their core intuition rests on three pillars accessible to any university graduate:

### 1. Algebraic Topology and Rational Homotopy
How do you prove beyond doubt that a sphere and a donut (torus) can never be continuously deformed into each other without cutting? You attach an **"algebraic signature"** (fundamental group, homology, homotopy groups) that stays unchanged under stretching. **Rational homotopy theory**—where Sullivan invented *minimal models*—is a brilliant noise filter: by ignoring messy finite torsion details, it turns the entire homotopy shape of a space into clean polynomial algebra over $$\mathbb{Q}$$.

### 2. Geometric Topology and Manifold Surgery
Geometric topology studies **manifolds** directly (spaces that look locally flat like $$\mathbb{R}^n$$, just as Earth’s surface is a 2-manifold). **Surgery theory** works literally as named: to turn a sphere into a donut, cut out two small disks from the sphere and sew a cylinder connecting the two holes! High-dimensional topologists use standardized cutting-and-gluing operations like this to classify which manifolds can exist.

### 3. Complex Dynamics and Quasiconformal Maps
Take a simple complex map like $$f(z) = z^2 + c$$, pick a starting point $$z_0 \in \mathbb{C}$$, and iterate forever: $$z_1 = f(z_0), z_2 = f(z_1), \dots$$. The complex sphere splits into two complementary worlds: the **Fatou set** (tame regions where nearby points share the same long-term fate) and the **Julia set** (the chaotic fractal boundary). Meanwhile, a **quasiconformal map** relaxes angle preservation slightly, turning infinitesimal circles into ellipses of bounded eccentricity—flexible enough to deform at will, yet rigid enough to preserve analytic structure.

---

## 1. Topology in the broad sense

Sullivan’s career spans surgery theory, rational homotopy theory, manifold theory, quasiconformal mappings, and dynamical systems. Popular Abel materials stress a consistent vision: **geometric structures on spaces**—whether smooth manifolds or fractal Julia sets.

“Topology in its broadest sense” is not marketing fluff. It means:

- **Algebraic** tools (homotopy, cohomology operations, rational models);  
- **Geometric** tools (structures on manifolds, quasiconformal geometry);  
- **Dynamical** tools (iteration, rigidity of complex maps).

Few mathematicians move fluently among all three for decades. Abel 2022 awards that arc.

---

## 2. Landmark themes (selection)

No single paper is the whole story. A partial map:

### Surgery and manifold theory

Surgery theory asks when one manifold can be modified into another by cutting and gluing along standard pieces, relating homotopy information to geometric classification. Sullivan’s contributions helped shape high-dimensional topology’s modern language.

### Rational homotopy and algebraic models

Rational homotopy theory studies spaces “up to torsion,” often via algebraic models (differential graded algebras). Sullivan’s approach made algebraic models a practical language for homotopy types over $$\mathbb{Q}$$.

### Quasiconformal mappings and geometric structures

Quasiconformal maps distort angles in a controlled way; they are flexible enough for deformations yet rigid enough for geometric conclusions. Sullivan used such tools as bridges between analysis and topology.

### Dynamics: no wandering domains

In complex dynamics, iteration of rational maps on the Riemann sphere produces Fatou sets (order) and Julia sets (chaos). Sullivan proved that **rational maps have no wandering domains**, solving a long-standing conjecture and linking complex dynamics to topological rigidity.

---

## 3. Dynamics meets topology: no wandering domains

Let $$f:\widehat{\mathbb{C}}\to\widehat{\mathbb{C}}$$ be a rational map (quotient of polynomials), acting on the Riemann sphere. The **Fatou set** is the largest open set on which the family of iterates $$\{f^{\circ n}\}$$ is normal (equicontinuous on compact subsets, in the spherical metric). Connected components of the Fatou set are **Fatou components**.

A **wandering domain** would be a Fatou component $$U$$ such that the forward images

$$
U,\; f(U),\; f^{\circ 2}(U),\; \dots
$$

are all distinct—never cycling. Sullivan proved in 1985 that **no such wandering domains exist** for rational maps of degree $$d \ge 2$$: every Fatou component eventually lands in a periodic cycle.

### Explanation: Hand-Checking Orbits of $$f(z) = z^2 - 1$$ and Sullivan’s Dimension-Counting Proof

#### Part 1: Compute orbits of $$f(z) = z^2 - 1$$ (the "Basilica" Julia set) by hand
Try a few starting values $$z_0$$ directly:
- **Start at $$z_0 = 0$$:** $$0 \mapsto -1 \mapsto 0 \mapsto -1 \mapsto \cdots$$ — a **period-2 cycle**! Because the derivative of the 2-step map is $$(f^{\circ 2})'(0) = f'(-1)\cdot f'(0) = (-2)\cdot 0 = 0$$, the cycle $$\{0, -1\}$$ is *super-attracting*.
- **Start at $$z_0 = 0.2$$ (near $$0$$):**
  $$
  0.2 \mapsto -0.96 \mapsto -0.0784 \mapsto -0.9939 \mapsto -0.0122 \mapsto -0.99985 \dots
  $$
  The orbit bounces back and forth between the Fatou component around $$0$$ and the Fatou component around $$-1$$, locking onto $$\{0, -1\}$$!
- **Start at $$z_0 = 2$$:** $$2 \mapsto 3 \mapsto 8 \mapsto 63 \mapsto 3968 \to \infty$$ (inside the basin of $$\infty$$).
- **Repelling fixed points:** Solving $$z^2 - 1 = z$$ gives $$z = \frac{1 \pm \sqrt{5}}{2}$$ ($$\approx 1.618$$ and $$-0.618$$). Here $$\lvert f'(z)\rvert = \lvert 2z\rvert > 1$$, so both sit right on the **Julia set**!

#### Part 2: Sullivan’s contradiction by "counting dimensions"
How did Sullivan prove that a rational map can never have a wandering component $$U$$ drifting into fresh regions forever?
1. **Assume for contradiction** that $$U, f(U), f^{\circ 2}(U), \dots$$ are all pairwise disjoint. Because they never overlap, you can deform angles (quasiconformally) inside $$U$$ using **infinitely many independent parameters** and transport that deformation consistently along the orbit without ever colliding with yourself!
2. **Measurable Riemann Mapping Theorem:** Each such quasiconformal deformation produces a new rational map of the exact same degree $$d$$—yielding an **infinite-dimensional** family of distinct rational maps of degree $$d$$.
3. **Count the true dimension of degree-$$d$$ rational maps:** Every rational map of degree $$d$$ looks like
   $$
   f(z) = \frac{a_d z^d + \cdots + a_1 z + a_0}{b_d z^d + \cdots + b_1 z + b_0}.
   $$
   The numerator has $$d+1$$ coefficients and the denominator has $$d+1$$; scaling both by a nonzero constant removes $$1$$ degree of freedom, leaving exactly **$$2d + 1$$ complex parameters** (for $$d = 2$$, just $$5$$ complex dimensions!).
4. **Sharp contradiction:** You cannot pack an **infinite-dimensional** family of deformations inside a **$$2d + 1$$-dimensional** space! Therefore, wandering domains cannot exist.

That proof also opened **Sullivan’s Dictionary**, a profound parallel between complex dynamics of rational maps and hyperbolic geometry of 3D Kleinian groups.

### Contrast with entire maps

For some transcendental entire functions (such as $$f(z) = z + \sin(2\pi z) + 1$$), wandering domains **can** exist—because the space of entire functions is infinite-dimensional, so Step 3–4 no longer yields a contradiction. Precision about the class of maps is part of mathematical literacy.

---

## 4. Julia sets and the course’s “beautiful mathematics”

Iteration on the sphere produces Julia sets—often fractal portraits that appear in popular mathematics. Beauty is real; theorems are stricter. Sullivan’s result is not a picture; it is a classification constraint on the open set where dynamics is “tame.”

In this course, you can link Julia imagery to [beautiful mathematics]({{ site.baseurl }}/contents/en/chapter04/) while insisting that Abel 2022 cites **contributions to topology and dynamics**, not poster art.

---

## 5. Why Abel: the virtuoso career

Fields-style single-breakthrough stories (Poincaré via Ricci flow; a modularity proof of FLT) sit nearby in the curriculum. Sullivan’s Abel is the **long arc**: repeatedly introducing languages that let problems move between categories—algebraic models for homotopy, quasiconformal tools for geometry, rigidity for dynamics.

The committee’s “virtuoso” metaphor is apt if read mathematically: virtuosity means **transfer of technique across genres**, not merely virtuoso computation inside one genre.

A student-friendly test of that claim: pick any two of {surgery, rational homotopy, quasiconformal geometry, complex dynamics} and write one paragraph on how a problem in one dialect might be restated in the other. If you can feel the translation difficulty—and why a career spent building translators matters—you have understood the Abel citation better than a one-line summary of no wandering domains alone.

---

## 5b. Periodicity of Fatou components (what the theorem buys)

Once wandering domains are forbidden, every Fatou component $$U$$ of a rational map is **preperiodic**: some forward image $$f^{\circ m}(U)$$ is periodic, and the periodic cycle of components falls into classical types studied by Fatou, Julia, and later authors (attracting basins, parabolic basins, Siegel disks, Herman rings—subject to further constraints). The theorem does not classify all dynamics; it removes an entire pathological class so that the remaining taxonomy can proceed.

This is a typical Abel-scale pattern: a rigidity theorem that **clears the landscape** so structure theorems become possible. Compare Margulis-type rigidity clearing wild homomorphisms, or modularity clearing which elliptic curves can exist. Different subjects, same logical shape—constraints first, classification second.

---

## 6. Comparison with Perelman (careful)

| | Sullivan (Abel 2022) | Perelman (Fields 2006) |
|--|----------------------|-------------------------|
| Emphasis | Lifetime topology + dynamics | Ricci flow completing geometrization |
| Style | Many landscapes, many languages | Focused completion of Hamilton program |
| Flagship slogan | No wandering domains (among many) | Geometrization ⇒ Poincaré |
| Prize type | Abel lifetime | Fields (declined) + Clay (declined) |

Both connect geometry/analysis to topology. Neither should be flattened into the other.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “Abel 2022 is only about Julia sets.” | Julia sets are popular imagery; the citation is topology in the broad sense, including algebraic and geometric aspects. |
| “No wandering domains holds for all complex maps.” | It is a theorem about **rational** maps; some entire maps differ. |
| “Sullivan is only a dynamicist.” | Dynamics is one major strand; surgery, rational homotopy, and geometric topology are others. |
| “Virtuoso means not deep.” | Here it means deep across multiple dialects of topology. |
| “Lifetime prizes have no flagship theorems.” | They often do—and more besides. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/sullivan-topology/`.

**From the research pack (must-know slogans)**

- Abel 2022: topology in the broad sense — algebraic, geometric, dynamical.
- Highlights: rational homotopy / Sullivan models; **no wandering domains** for rational maps.
- Virtuoso career across topology and dynamics rather than a single theorem trophy.

**Recommended order**

1. **Core** — Sullivan Abel lecture — Gathering chestnuts… fluid motion: [https://www.youtube.com/watch?v=RRMBRiyNcjI](https://www.youtube.com/watch?v=RRMBRiyNcjI).  
2. **Orientation** — Abel Prize playlist Sullivan 2022: [https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw](https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw).  

**Official / primary written hubs**

- Abel 2022 Sullivan: https://abelprize.no/abel-prize-laureates/2022  

Complete URL bibliography: `research/video-research/sullivan-topology/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/sullivan-topology/transcripts/` · status: `research/video-research/sullivan-topology/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/sullivan-topology_RRMBRiyNcjI_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/sullivan-topology/references.md`.

1. Abel 2022 Sullivan — https://abelprize.no/abel-prize-laureates/2022  
2. Sullivan Abel lecture — Gathering chestnuts… fluid motion — https://www.youtube.com/watch?v=RRMBRiyNcjI  
3. Abel Prize playlist Sullivan 2022 — https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw  
4. Wikipedia — Dennis Sullivan — https://en.wikipedia.org/wiki/Dennis_Sullivan  
5. Wikipedia — No wandering domain theorem — https://en.wikipedia.org/wiki/No_wandering_domain_theorem  
6. Wikipedia — Rational homotopy theory — https://en.wikipedia.org/wiki/Rational_homotopy_theory  
7. Stony Brook / CUNY culture pages (search Sullivan Abel) — https://www.stonybrook.edu/  
8. Abel popular PDF topology (from laureate page materials) — https://abelprize.no/sites/default/files/2022-03/topolgy_eng.pdf  
9. Abel popular PDF no-wandering — https://abelprize.no/sites/default/files/2022-03/wanderingset_eng.pdf  
10. Research pack folder: `research/video-research/sullivan-topology/`.

1. Abel Prize 2022 — [abelprize.no/abel-prize-laureates/2022](https://abelprize.no/abel-prize-laureates/2022).  
2. D. Sullivan, *Quasiconformal homeomorphisms and dynamics I. Solution of the Fatou-Julia problem on wandering domains*, Ann. of Math. (1985).  
3. Popular profiles (Quanta and Abel popular PDFs) for orientation—always return to theorem statements.  
4. Course: [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/); beautiful mathematics chapter for Julia imagery with caution.

---


## Topology and chaos as one craft

Sullivan’s career argues that classifying spaces and classifying long-term motion are not opposites. Quasi-conformal maps, surgery, and dynamical rigidity share a habit: control geometric distortion until a topological conclusion follows. The Abel citation’s “broadest sense” of topology is an invitation to stop walling dynamics outside pure math.

## Seminar prompt

Pick a Julia-set image and write 150 words connecting visual chaos to a precise dynamical definition (orbit, Julia set, Fatou set)—without claiming you proved no wandering domains.

## Further directions

- Visual seminar: Julia sets as “beautiful mathematics” with a theorem attached.  
- Contrast rigidity theorems across fields (Sullivan; Margulis).  
- Compare with a related [Fields essay]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/).  
- Note one open direction in complex dynamics or geometric topology that still fascinates you.  
- Next: [Luis Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/).

## Video tham khảo

- **xem trước** — [Dennis Sullivan: Gathering chestnuts of math related to fluid motion](https://www.youtube.com/watch?v=RRMBRiyNcjI) — The Abel Prize, English. Watch first. “Dennis Sullivan: Gathering chestnuts of math related to fluid motion” orients the lesson’s aim: After this lecture you should be able to place Sullivan across algebraic topology, geometric topology, and complex dynamics; name the no wandering domains theorem for rational maps…
