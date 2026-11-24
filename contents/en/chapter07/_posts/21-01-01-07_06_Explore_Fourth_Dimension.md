---
layout: post
title: "What does a fourth dimension look like?"
chapter: '07'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Course links**  
> [Sphere packing / Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/) · [Packing studio]({{ site.baseurl }}/contents/en/chapter07/07_03_Explore_Sphere_Packing/) · [Infinity studio]({{ site.baseurl }}/contents/en/chapter07/07_08_Explore_Describe_Infinity/)

In 1884, schoolmaster and author Edwin A. Abbott published *Flatland*, a charming novella about a Square living in a two-dimensional plane who is visited one day by a three-dimensional Sphere. To the Square, the Sphere has no whole shape at all—it appears only as a sequence of circular cross-sections: a dot, expanding into a disk, shrinking back to a dot, and vanishing! If a four-dimensional visitor ever passed through our room, *we* would be the bewildered Square.

Fortunately, mathematics is not trapped inside human eyeballs. In geometry, the fourth dimension is no ghost story: it is simply **$$\mathbb{R}^4$$**—ordered quadruples of real numbers equipped with the ordinary Euclidean distance

$$
\lVert x\rVert=\sqrt{x_1^2+x_2^2+x_3^2+x_4^2}.
$$

Where visual imagination hits a wall, **coordinates, linear algebra, and counting** walk right through. This studio builds your "algebraic eyes" for 4D and beyond: counting the faces of a tesseract, projecting and slicing it into 3D/2D, and witnessing the shock of high-dimensional volume collapsing to zero—an effect that turns everyday 3D intuition upside down.

**Lesson roadmap:** Background Knowledge Map (high-dimensional geometry, concentration of measure & Euclidean $$\mathbb{R}^4$$ vs. Minkowski spacetime) → Hypercubes $$I^n$$, projections & slices → Deep-Dive Explanation (Read Slowly): hand-computing a 4D→2D projection matrix, catching a false crossing, and solving the sphere-in-the-center-gap paradox → Unit-ball volume $$V_n \to 0$$ → Studio experiments & log.

---

## Learning objectives

After this studio you should be able to:

- Use coordinates to define distance, hyperplanes, and balls in $$\mathbb{R}^n$$ for general $$n$$.
- Complete a table of vertices, edges, faces, and cells for the hypercube $$I^n=[0,1]^n$$ for $$n=1,2,3,4$$ (and state binomial formulas).
- Explain perspective or parallel projection of a tesseract into 2D/3D as a map, not as magic.
- Discuss the volume $$V_n$$ of the unit ball and why $$V_n\to 0$$ as $$n\to\infty$$.
- Give one helpful analogy and one misleading analogy for “the fourth dimension.”
- Connect high-$$D$$ volume concentration to packing weirdness or random vectors (at slogan level).

**Prerequisites.** Vectors, dot products, basic combinatorics (binomial coefficients), willingness to draw.

---

## Background Knowledge Map: What Are High-Dimensional Geometry and Geometric Probability?

Why should a university graduate in engineering, data science, or applied math care about 4, 100, or 10,000 dimensions when we live in 3D? Three modern pillars explain why:

### 1. High-Dimensional Geometry

Every independent parameter of a system—temperature, pressure, humidity, and wind speed; 1,000 pixel intensities in an image; or 1,536 embedding coordinates of a word in a language model—is **one spatial dimension**. High-dimensional geometry uses linear algebra and convex analysis to study polytopes, spheres, orthogonal rotations, and volume in $$\mathbb{R}^n$$, revealing phenomena that differ *qualitatively* from 2D and 3D.

### 2. Geometric Probability and Concentration of Measure

Pick two independent random vectors on the unit sphere $$S^{n-1}$$ in $$n = 1000$$ dimensions: their dot product clusters tightly around $$0$$, meaning **random high-dimensional vectors are almost always orthogonal!** Peel off just the outer $$1\%$$ skin of a 1,000-dimensional orange (keeping radius $$0.99$$): the remaining interior occupies only $$(0.99)^{1000} \approx 0.000043$$ of the total volume—over **$$99.995\%$$ of the orange lives inside its outermost $$1\%$$ peel**!

### 3. Euclidean $$\mathbb{R}^4$$ vs. Minkowski Spacetime

Physics often calls time "the fourth dimension," but **Minkowski spacetime** uses an indefinite quadratic form $$\Delta s^2 = -c^2\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2$$ (allowing zero "distance" along light rays), completely different from the positive-definite Euclidean metric on $$\mathbb{R}^4$$. Keeping those two geometries distinct is essential mathematical hygiene.

---

## 1. Background mathematics

### 1.1 Dimension as degrees of freedom

A point in $$\mathbb{R}^n$$ is an $$n$$-tuple $$(x_1,\ldots,x_n)$$. Linear subspaces have dimensions equal to the size of a basis. The sphere

$$
S^{n-1}=\{x\in\mathbb{R}^n:\lVert x\rVert=1\}
$$

is $$(n-1)$$-dimensional as a manifold. None of this requires mysticism: the fourth coordinate is as legitimate as the third.

### 1.2 The hypercube $$I^n$$

The unit hypercube $$I^n=[0,1]^n$$ has:

| Object | Count |
|--------|-------|
| Vertices | $$2^n$$ |
| Edges | $$n\cdot 2^{n-1}$$ |
| $$k$$-dimensional faces | $$\binom{n}{k}2^{n-k}$$ |

Reason for edges: each vertex has $$n$$ bits; flipping exactly one bit moves along an edge; each edge is counted twice if you sum degrees, so $$E=\tfrac12\cdot 2^n\cdot n=n2^{n-1}$$. Reason for $$k$$-faces: choose which $$k$$ coordinates vary in $$[0,1]$$ and fix each of the other $$n-k$$ coordinates to $$0$$ or $$1$$.

For $$n=4$$ (the **tesseract**): 16 vertices, 32 edges, 24 square faces, 8 cubic cells. Its main diagonal from $$(0,0,0,0)$$ to $$(1,1,1,1)$$ has length $$\sqrt{4} = 2$$—twice the edge length!

### 1.3 Projections, shadows, and slices

A linear map $$P:\mathbb{R}^4\to\mathbb{R}^3$$ (or to $$\mathbb{R}^2$$) sends the tesseract to a polyhedron or planar figure. Edges map to segments; crossings in the drawing are often **not** intersections in 4D. Slicing by a 3D hyperplane $$\{x_4=t\}$$ (or a slanted hyperplane $$x_1+x_2+x_3+x_4=t$$) yields a movie of 3D cross-sections.

#### Deep-Dive Explanation (Read Slowly): Hand-Computing a 4D→2D Projection and the Center-Sphere Paradox

Let us make 4D concrete with two quick calculations you can verify line by line:

**Example 1 — Catching a false crossing under a 4D→2D projection matrix:**
Pick the explicit linear projection $$P: \mathbb{R}^4 \to \mathbb{R}^2$$ given by
$$
P = \begin{pmatrix} 1 & 0 & 0.5 & 0.3 \\ 0 & 1 & 0.5 & -0.4 \end{pmatrix},
$$
which sends $$(x_1, x_2, x_3, x_4)$$ to $$(x_1 + 0.5x_3 + 0.3x_4,\; x_2 + 0.5x_3 - 0.4x_4)$$ on your sheet of paper.
Consider two edges of the tesseract $$I^4$$ that are completely **disjoint** in 4D:
- **Edge 1:** from $$A(0,0,0,0)$$ to $$B(1,0,0,0)$$ → projects to the horizontal segment from $$(0,0)$$ to $$(1,0)$$.
- **Edge 2:** from $$E(0,0,0,1)$$ to $$F(0,1,0,1)$$ (living entirely at $$x_4 = 1$$, a full unit away from Edge 1!). Under $$P$$:
  - $$P(E) = (0.3,\; -0.4)$$,
  - $$P(F) = (0.3,\; 0.6)$$.
On your 2D page, the vertical segment $$P(E)P(F)$$ slices right through the horizontal segment $$P(A)P(B)$$ at $$(0.3,\; 0)$$—yet in $$\mathbb{R}^4$$ they never come within distance $$1$$ of each other! That is why rotating tesseract videos look tangled: almost every apparent crossing is a **projection artifact**.

**Example 2 — The sphere trapped in the center of $$[-1, 1]^n$$ escapes the box!**
Inside the square $$[-1,1]^2$$, place $$2^2 = 4$$ disks of radius $$1/2$$ centered at $$(\pm\tfrac{1}{2}, \pm\tfrac{1}{2})$$. Each center is distance $$\frac{\sqrt{2}}{2}$$ from the origin, so the largest disk fitting in the central gap has radius
$$
r_2 = \frac{\sqrt{2}}{2} - \frac{1}{2} = \frac{\sqrt{2}-1}{2} \approx 0.207 \quad (\text{tucked well inside the box}).
$$
Now repeat in $$[-1, 1]^n$$ with $$2^n$$ balls of radius $$1/2$$ centered at $$(\pm\tfrac{1}{2}, \dots, \pm\tfrac{1}{2})$$. The distance from the origin to each center is $$\frac{\sqrt{n}}{2}$$, so the central-gap sphere has radius:
$$
r_n = \frac{\sqrt{n} - 1}{2}.
$$
Plug in dimensions by hand:
- $$n = 4$$: $$r_4 = \frac{\sqrt{4}-1}{2} = 0.5$$ (matches the corner balls!).
- $$n = 9$$: $$r_9 = \frac{\sqrt{9}-1}{2} = 1.0$$ (touches all walls of the box $$[-1,1]^9$$!).
- $$n = 10$$: $$r_{10} = \frac{\sqrt{10}-1}{2} \approx 1.081 > 1$$ — the sphere nestled in the "central gap" **bulges right outside the entire hypercube**!!

### 1.4 Slices

Intersecting a tesseract with $$\{x_4=t\}$$ for $$t\in[0,1]$$ yields the unit cube $$[0,1]^3$$; slicing instead with the slanted hyperplane $$x_1+x_2+x_3+x_4=t$$ transforms the cross-section from a point ($$t=0$$) into a regular tetrahedron, then a **regular octahedron** at $$t=2$$, and back to a point at $$t=4$$.

### 1.5 Volume of the unit ball

The volume of the Euclidean unit ball $$B^n=\{x:\lVert x\rVert\le 1\}$$ is

$$
V_n=\frac{\pi^{n/2}}{\Gamma\!\left(\frac{n}{2}+1\right)}.
$$

Hand values: $$V_1=2$$, $$V_2=\pi\approx 3.142$$, $$V_3=\frac{4}{3}\pi\approx 4.189$$, $$V_4=\frac{\pi^2}{2}\approx 4.935$$, peaking at $$V_5 = \frac{8\pi^2}{15}\approx 5.264$$, before plunging toward $$0$$ ($$V_{10}\approx 2.550$$, $$V_{20}\approx 0.0258$$). Meanwhile the cube $$[-1,1]^n$$ has volume $$2^n\to\infty$$ (over a million at $$n=20$$!). High-dimensional space is **spiky**—volume hides in the corners of cubes and near the equators of spheres.

### 1.6 Concentration and random vectors

For a uniform random point on the sphere $$S^{n-1}$$, coordinates are typically size about $$1/\sqrt{n}$$. Almost all of the measure of a high-dimensional ball sits in a thin shell near the boundary. These facts power modern high-dimensional probability and explain why naive intuition from $$n=2,3$$ fails for packing, polytopes, and data science geometry.

### 1.7 Regular polytopes

In 2D: infinitely many regular polygons. In 3D: five Platonic solids. In 4D: six regular polytopes (including the 24-cell, which has no perfect 3D analogue). In $$n\ge 5$$: only three regular polytopes (simplex, cube, cross-polytope). Dimension constrains symmetry.

---

## 2. Conjecture versus proof versus experiment

Here most claims you meet are **theorems** (counting formulas, volume formulas) or **definitions**. The “conjectural” part is often your **intuition**—treat wrong intuitions as hypotheses to kill.

| Label | Example |
|-------|---------|
| **Theorem** | $$V_n\to 0$$; face-count formulas |
| **Model** | Spacetime vs Euclidean 4D |
| **Visualization** | Projection chosen; artifacts of drawing |
| **Observation** | “In my plot, $$V_n$$ peaks near $$n=5$$” |

**Success criteria:**

1. Complete hypercube count table for $$n=1..4$$ with at least one binomial check.  
2. One projection or slice sketch (hand or code) with the map named.  
3. Table or plot of $$V_n$$ for $$n=1..15$$ with peak identified.  
4. One helpful + one misleading analogy, each justified.  
5. Link paragraph to packing or probability.

---

## 3. Research log standards

**Date · Intent · Action · Result · Label · Interpretation · Next step.**

If you use code for volumes, cite the library’s gamma function. If you use AI to generate a tesseract SVG, disclose and still compute vertex counts yourself.

---

## 4. Experiments

Do at least **two** of A–E.

### Experiment A — Hypercube census (25–40 min)

Fill:

| $$n$$ | Vertices | Edges | Squares | Cubes | 4-cells |
|-------|----------|-------|---------|-------|---------|
| 1 | | | — | — | — |
| 2 | | | | — | — |
| 3 | | | | | — |
| 4 | | | | | |

Verify edges $$=n 2^{n-1}$$ and vertices $$=2^n$$.

**Success criterion:** full table + one inductive story (“to go from $$n$$ to $$n+1$$, extrude two copies”).

### Experiment B — Projection sketch (30–60 min)

Draw a tesseract as “cube within a cube” with corresponding vertices joined, or write code that projects 16 points with a $$2\times 4$$ or $$3\times 4$$ matrix. Label which edges cross only in the drawing.

**Success criterion:** figure + explicit note on false crossings.

### Experiment C — Slice storyboard (30–50 min)

For $$t\in\{0,0.25,0.5,0.75,1\}$$, describe the set $$I^4\cap\{x_4=t\}$$. How does the 3D slice change? Optional: compare to slicing a 3D cube with planes $$z=t$$.

**Success criterion:** five short descriptions or sketches.

### Experiment D — Volume peak (30–45 min)

Compute $$V_n$$ numerically for $$n=1,\ldots,20$$. Plot. Where is the maximum? Confirm $$V_n\to 0$$. Compare $$V_n/2^n$$ (ball vs cube $$[-1,1]^n$$).

**Success criterion:** plot/table + two-sentence moral about concentration.

### Experiment E — Analogy autopsy (20–30 min)

Write:

1. Helpful analogy (e.g., Flatland: how 2D beings meet a sphere).  
2. Misleading analogy (e.g., “time is just like space” without metric caveats; or “the fourth dimension is spiritual”).  

Explain the failure mode of the misleading one.

**Success criterion:** both paragraphs; no unexamined mysticism.

---

## 5. Common confusions

1. **“The fourth dimension is time, full stop.”** — Physics uses 4D spacetime with a different metric; Euclidean $$\mathbb{R}^4$$ is a separate object.  
2. **“If I cannot visualize it, it is not rigorous.”** — Coordinates are the rigor.  
3. **“Projections show true intersections.”** — Drawings introduce artifacts.  
4. **“Unit ball volume grows forever with dimension.”** — It eventually decays.  
5. **“High dimension is just more of the same.”** — Concentration phenomena qualitatively change geometry and probability.

---

## 7. Checkpoint rubric

| Done? | Item |
|-------|------|
| ☐ | Hypercube table $$n=1..4$$ |
| ☐ | Projection or slice artifact |
| ☐ | $$V_n$$ table/plot with peak |
| ☐ | Helpful + misleading analogy |
| ☐ | Packing or probability link |
| ☐ | Log ≥3 entries |

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/explore-fourth-dimension/`.

**From the research pack (must-know slogans)**

- Coordinates: a point in $$\mathbb{R}^4$$ is $$(x_1,x_2,x_3,x_4)$$ — geometry is linear algebra + distance.
- **Tesseract / 4-cube** and **3-sphere $$S^3$$** are standard visualization anchors.
- Volume concentration and packing behave differently in high dimension (measure concentrates).
- Studio: compute volumes/projections; avoid sci-fi “time is the fourth dimension” as a definition of Euclidean $$\mathbb{R}^4$$.

**Recommended order**

1. **Intuition** — Numberphile — Perfect Shapes in Higher Dimensions (packing link): [https://www.youtube.com/watch?v=mceaM2_zQd8](https://www.youtube.com/watch?v=mceaM2_zQd8).  
2. **Core** — Viazovska sphere packing (high-D density culture): [https://www.youtube.com/watch?v=fH6KNlUJux0](https://www.youtube.com/watch?v=fH6KNlUJux0).  

**Official / primary written hubs**

- Viazovska E8 (high-D packing theorem): https://arxiv.org/abs/1603.04246  

Complete URL bibliography: `research/video-research/explore-fourth-dimension/references.md`.

## 8. References and course links


### Video research pack (all URLs)

Complete list: `research/video-research/explore-fourth-dimension/references.md`.

1. Numberphile — Perfect Shapes in Higher Dimensions (packing link) — https://www.youtube.com/watch?v=mceaM2_zQd8  
2. Viazovska sphere packing (high-D density culture) — https://www.youtube.com/watch?v=fH6KNlUJux0  
3. Wikipedia — Four-dimensional space — https://en.wikipedia.org/wiki/Four-dimensional_space  
4. Wikipedia — Tesseract — https://en.wikipedia.org/wiki/Tesseract  
5. Wikipedia — 3-sphere — https://en.wikipedia.org/wiki/3-sphere  
6. Wikipedia — Hypersphere — https://en.wikipedia.org/wiki/N-sphere  
7. Viazovska E8 (high-D packing theorem) — https://arxiv.org/abs/1603.04246  
8. 3Blue1Brown essence of linear algebra (basis for coordinates) — https://www.3blue1brown.com/topics/linear-algebra  
9. Quanta high-dimensional geometry tag — https://www.quantamagazine.org/tag/geometry/  
10. Research pack folder: `research/video-research/explore-fourth-dimension/`.

1. Course packing lectures and studio for high-$$D$$ density.  
2. Coxeter, *Regular Polytopes* (classical).  
3. High-dimensional probability notes (Vershynin-style expositions) for concentration.  
4. Nearby: [Describe infinity]({{ site.baseurl }}/contents/en/chapter07/07_08_Explore_Describe_Infinity/) for different “sizes” of infinite-dimensional phenomena (function spaces)—keep categories straight.

---

## Further directions

Code a 4D rotation as a block-diagonal orthogonal matrix and animate a projection. Or compute solid angles / kissing configurations in dimension 4 and compare to the known kissing number 24.

### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/explore-fourth-dimension/transcripts/` · status: `research/video-research/explore-fourth-dimension/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/explore-fourth-dimension_mceaM2_zQd8_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*


## Video tham khảo

- **xem trước** — [Strange Spheres in Higher Dimensions - Numberphile](https://www.youtube.com/watch?v=mceaM2_zQd8) — Numberphile, English. Watch first. “Strange Spheres in Higher Dimensions - Numberphile” orients the lesson’s aim: Use coordinates to define distance, hyperplanes, and balls in \mathbb{R}^n for general n.
- [Einstein Lectures: Maryna Viazovska - The sphere packing problem](https://www.youtube.com/watch?v=fH6KNlUJux0) — Universität Bern, English. A second pass once the main claim is in view: Use coordinates to define distance, hyperplanes, and balls in \mathbb{R}^n for general n.
