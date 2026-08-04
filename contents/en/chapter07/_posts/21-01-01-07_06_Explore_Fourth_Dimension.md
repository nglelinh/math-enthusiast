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

The fourth dimension is not a ghost story. It is **$$\mathbb{R}^4$$**: ordered quadruples of real numbers with the Euclidean metric

$$
\lVert x\rVert=\sqrt{x_1^2+x_2^2+x_3^2+x_4^2}.
$$

Visualization is hard because eyes and evolution are three-dimensional, but **coordinates, linear algebra, and counting** do not care. This studio builds intuition through hypercubes, projections, slices, and volume paradoxes—then links high-dimensional geometry to packing and probability.

You will not “see” 4D as you see a chair. You will **compute** what 4D forces you to believe.

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

## 1. Background mathematics

### 1.1 Dimension as degrees of freedom

A point in $$\mathbb{R}^n$$ is an $$n$$-tuple $$(x_1,\ldots,x_n)$$. Linear subspaces have dimensions equal to the size of a basis. The sphere

$$
S^{n-1}=\{x\in\mathbb{R}^n:\lVert x\rVert=1\}
$$

is $$(n-1)$$-dimensional as a manifold. None of this requires mysticism: the fourth coordinate is as legitimate as the third.

Time is sometimes called a fourth dimension in physics (spacetime), but **Minkowski spacetime** is not Euclidean $$\mathbb{R}^4$$—the metric has a different signature. Keep Euclidean geometry and physics models in separate log boxes unless you deliberately compare them.

### 1.2 The hypercube $$I^n$$

The unit hypercube $$I^n=[0,1]^n$$ has:

| Object | Count |
|--------|-------|
| Vertices | $$2^n$$ |
| Edges | $$n\cdot 2^{n-1}$$ |
| $$k$$-dimensional faces | $$\binom{n}{k}2^{n-k}$$ |

Reason for edges: each vertex has $$n$$ bits; flipping exactly one bit moves along an edge; each edge is counted twice if you sum degrees, so $$E=\tfrac12\cdot 2^n\cdot n=n2^{n-1}$$. Reason for $$k$$-faces: choose which $$k$$ coordinates vary in $$[0,1]$$ and fix each of the other $$n-k$$ coordinates to $$0$$ or $$1$$.

For $$n=4$$ (the **tesseract**): 16 vertices, 32 edges, 24 square faces, 8 cubic cells. Build this table yourself before trusting a video. An inductive picture helps: to form $$I^{n+1}$$, take two copies of $$I^n$$ and join corresponding vertices by new edges—the “extrusion” metaphor that makes 4D feel like a movie of 3D cubes.

### 1.3 Projections and shadows

A linear map $$P:\mathbb{R}^4\to\mathbb{R}^3$$ (or to $$\mathbb{R}^2$$) sends the tesseract to a polyhedron or planar figure. Edges map to segments; crossings in the drawing are often **not** intersections in 4D. Schlegel diagrams and double rotations (in coordinate planes $$(x_1x_2)$$ and $$(x_3x_4)$$) produce the famous rotating-tesseract animations.

**Studio discipline.** When you watch a video, write the mathematical map: which coordinates are discarded or combined? Otherwise the animation is entertainment, not geometry.

### 1.4 Slices

Intersecting a tesseract with a 3-dimensional hyperplane $$\{x_4=t\}$$ yields a cube that grows and shrinks as $$t$$ varies—analogous to slicing a 3D cube with a plane to get rectangles, hexagons, etc. Slicing is often more trustworthy than projection for “what appears.”

### 1.5 Volume of the unit ball

The volume of the Euclidean unit ball $$B^n=\{x:\lVert x\rVert\le 1\}$$ is

$$
V_n=\frac{\pi^{n/2}}{\Gamma\!\left(\frac{n}{2}+1\right)}.
$$

Values: $$V_1=2$$, $$V_2=\pi$$, $$V_3=\frac{4}{3}\pi$$, then growth, then decay toward 0 as $$n\to\infty$$. Meanwhile the volume of the cube $$[-1,1]^n$$ is $$2^n\to\infty$$. So the unit ball becomes a vanishingly small fraction of the circumscribed cube: high-dimensional space is **spiky**—volume concentrates in corners of cubes and near equators of spheres.

A related surface-area story: almost all of the measure of $$B^n$$ sits in a thin shell near radius 1. That is why high-dimensional probability often reduces geometric questions to behavior on spheres, and why naive “volume intuition” from oranges and boxes misleads packing experiments in the companion studio.

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

## 6. Exercises

1. Prove that $$I^n$$ has $$2^n$$ vertices by induction.  
2. Show that the number of edges is $$n 2^{n-1}$$.  
3. Using the formula for $$V_n$$, verify $$V_2$$ and $$V_3$$ by hand.  
4. Compute the Euclidean distance between $$(0,0,0,0)$$ and $$(1,1,1,1)$$. Compare to the 3D body diagonal of the unit cube.  
5. Proposal (≤150 words): which experiment will be your centerpiece and what counts as success?

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

