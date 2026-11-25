---
layout: post
title: "Impossible Shapes"
chapter: '04'
order: 12
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
---

Stare at M. C. Escher’s lithograph *Waterfall*. Water tumbles down a stone chute, spins a millwheel, and then glides calmly along a zigzagging aqueduct—right back to the top of the waterfall to fall all over again. Cover any single corner of the aqueduct with your hand, and the masonry looks completely solid, ordinary, and buildable. Lift your hand, follow the water around one full loop, and your brain slams into a quiet, delightful alarm bell: *every single corner is telling the truth, yet the whole building is telling a lie.*

**Impossible shapes**—the Penrose triangle, Oscar Reutersvärd’s early tribar, and Escher’s endless staircases—are much more than clever optical illusions. They are the most intuitive visual gateway to one of the deepest principles in modern geometry and topology: **local consistency does not guarantee global realizability.** Cover any two corners of a Penrose triangle, and a carpenter can build it out of wood; demand all three corners at once, and a simple $$3\times 3$$ linear system proves no solid 3D body can exist. In advanced mathematics, that exact failure to glue local pieces around a closed loop has a famous name: **cohomology**.

**Path:** local consistency vs. global realizability → the Penrose triangle as a $$3\times 3$$ linear system → Escher’s staircases → projection ambiguity and the Necker cube → gluing obstructions and cohomology intuition → common confusions and further directions.

---

## Learning objectives

After this lecture you should be able to:

- Explain **local consistency vs. global realizability** for 2D line drawings depicting 3D solids.
- Model the **Penrose triangle** as a $$3\times 3$$ system of depth equations $$D\mathbf{h} = \mathbf{b}$$ and prove algebraically why every pair of corners is solvable while all three together are inconsistent.
- Relate impossible figures to 3D-to-2D **projection** and ambiguous depth assignments (Necker cube).
- State the conceptual link between impossible figures and **gluing obstructions** (the intuition behind cohomology $$H^1$$).
- Distinguish impossible *drawings* from genuinely existing non-orientable *surfaces* like the Möbius band.
- Avoid claiming that "Escher proved Euclidean geometry wrong" or "fixing one corner removes a global obstruction."

**Prerequisites.** Basic 3D visualization, parallel projection, and solving a $$3\times 3$$ system of linear equations.

---

## Key ideas: Why an Optical Illusion Belongs in Algebraic Topology

Impossible figures sit at the crossroads of four disciplines that all wrestle with the same question: *when can local data be stitched into a single global object?*

1. **Projective Geometry & Computer Vision:** A 2D drawing is the shadow of a 3D scene under projection $$\pi:\mathbb{R}^3\to\mathbb{R}^2$$. Recovering 3D depth from 2D junctions (Y-junctions, T-junctions, arrows) is an inverse problem—formalized in computer vision (Huffman–Clowes labeling, Sugihara’s polyhedral realizability theorems) as systems of linear constraints on vertex depths.
2. **Linear Algebra & Inconsistent Systems:** Whenever local depth cues specify *differences* between neighboring vertices—like $$h_B - h_A = 1$$—global realizability reduces to checking whether a linear system $$D\mathbf{h} = \mathbf{b}$$ has a solution. If the sum around a cycle is nonzero, the system has no solution even though every subset of edges is consistent.
3. **Algebraic Topology & Cohomology ($$H^1$$):** In 1992, Roger Penrose explicitly used his impossible triangle to explain **sheaf cohomology**: each local piece has a valid depth coordinate, and on overlaps two coordinates differ by a shift. When the shifts around a closed loop fail to cancel, you get a nontrivial **1-cocycle**—a measurable topological obstruction to global existence.
4. **Cognitive Science of Perception:** Human vision evolved to infer 3D surfaces from local shading and junctions assuming general viewpoints. Impossible figures expose the exact local heuristics our visual cortex runs before checking global consistency.

---

## 1. Locally fine, globally impossible

A drawing of a cube is just ink on flat paper, yet our eyes immediately reconstruct a 3D solid whose projection matches the ink. An **impossible figure** is a 2D line drawing where every local junction matches a genuine 3D corner—yet **no single coherent 3D solid** in Euclidean space projects to the entire drawing while respecting all depicted face incidences and occlusions.

The ink is completely real and flat; what is impossible is **lifting** that 2D drawing to a single closed 3D object.

---

## 2. The Penrose triangle—and a $$3\times 3$$ linear-algebra proof of impossibility

The **Penrose triangle** (independently drawn by Oscar Reutersvärd in 1934 and analyzed by Lionel and Roger Penrose in 1958) shows three square beams meeting at right angles in a closed triangle. Cover any one of the three corners $$A, B, C$$, and the remaining L-shaped joint is completely buildable.

### Worked example: Turning the Penrose triangle into a $$3\times 3$$ matrix contradiction

Let $$h_A, h_B, h_C$$ represent the **depth** (distance toward the viewer) of the three corners $$A, B, C$$ along the line of sight. As you trace the beams around the triangle, the visual cues at each beam tell your brain that each beam angles steadily *toward* the viewer by some positive amount—say, $$1$$ unit per beam:

$$
\begin{cases}
h_B - h_A = 1 & \text{(beam } A\to B\text{ moves closer)}, \\
h_C - h_B = 1 & \text{(beam } B\to C\text{ moves closer)}, \\
h_A - h_C = 1 & \text{(beam } C\to A\text{ moves closer)}.
\end{cases}
$$

Write this system in matrix form $$D\mathbf{h} = \mathbf{b}$$:

$$
\underbrace{\begin{pmatrix}
-1 & 1 & 0 \\
0 & -1 & 1 \\
1 & 0 & -1
\end{pmatrix}}_{D}
\begin{pmatrix} h_A \\ h_B \\ h_C \end{pmatrix}
=
\underbrace{\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}}_{\mathbf{b}}.
$$

Now inspect two facts side by side:
1. **Local consistency (any 2 equations are solvable!):** Drop the third equation (representing cutting open the loop at corner $$C\to A$$). Choose $$h_A = 0$$; then $$h_B = 1$$ and $$h_C = 2$$ satisfy the first two equations effortlessly! Every proper open path of the triangle exists in 3D—which is why physical "Penrose triangle" sculptures in parks work by **forced perspective**: they are actually *open* 3-beam structures with a hidden gap that aligns only from one exact camera angle.
2. **Global obstruction (all 3 equations together explode!):** Notice that the three rows of $$D$$ sum to the zero vector:
   $$
   (-1+0+1,\; 1-1+0,\; 0+1-1) = (0, 0, 0),
   $$
   so $$\operatorname{rank}(D) = 2$$. Adding the left-hand sides of all three equations gives **$$0$$**, whereas adding the right-hand sides gives **$$1 + 1 + 1 = 3$$**:
   $$
   0 = (h_B - h_A) + (h_C - h_B) + (h_A - h_C) = 3 \quad \text{(contradiction!)}.
   $$

That discrepancy—$$3 \neq 0$$—is literally the **cohomology obstruction** around the closed loop! The matrix $$D$$ is the discrete derivative (coboundary operator), the vector $$\mathbf{b} = (1,1,1)^T$$ is a local depth-change prescription (a 1-cocycle), and the impossibility of solving $$D\mathbf{h} = \mathbf{b}$$ means $$\mathbf{b}$$ lies outside the column space of $$D$$ (it is not a coboundary).

---

## 3. Escher’s staircases and visual narrative

M. C. Escher’s *Ascending and Descending* (1960) and *Waterfall* (1961) turn that exact algebraic obstruction into architecture. In *Ascending and Descending*, four flights of stairs form a closed square where every flight climbs upward—a $$4\times 4$$ version of $$D\mathbf{h} = (1,1,1,1)^T$$ whose rows sum to $$0 = 4$$!

Escher collaborated directly with Roger Penrose and geometer H. S. M. Coxeter. He never claimed Euclidean geometry was broken; he dramatized how gracefully our visual system builds local 3D models and gets trapped when local rules fail a global cycle condition.

---

## 4. Projection, ambiguity, and Necker cousins

Even *completely possible* 3D objects lose depth under orthographic or perspective projection

$$
\pi:\mathbb{R}^3\to\mathbb{R}^2.
$$

The **Necker cube** is *underdetermined*: two different 3D depth assignments project to the exact same wireframe, so your brain flips back and forth between them. Impossible figures sit at the opposite extreme—they are *overdetermined and inconsistent*: no single depth assignment satisfies all local constraints at once.

---

### Explanation: From a Pencil Sketch to Cohomology

Why do mathematicians get excited about a drawing you can sketch on a napkin? Walk through the four-step translation slowly:

1. **Decode local constraints as differences.** Every beam or staircase in the drawing fixes a *relative* change in depth or elevation between adjacent corners ($$h_j - h_i = b_{ij}$$), never an absolute coordinate.
2. **Test every open piece locally.** Because no closed loop is formed when you cover one corner, you can always pick $$h_A = 0$$ and integrate the differences step by step along the path—every local patch is 100% realizable in $$\mathbb{R}^3$$.
3. **Close the loop and sum the differences.** Around any closed cycle, the telescoping sum of true differences $$(h_B-h_A)+(h_C-h_B)+(h_A-h_C)$$ *must* vanish identically ($$\operatorname{rank}(D) = 2$$).
4. **Measure the mismatch.** The nonzero cycle sum ($$3 \neq 0$$) is an **obstruction class**: the exact mathematical signature (in $$H^1$$) that local data cannot be glued into a global 3D shape.

**Quick check.** In our Penrose matrix $$D\mathbf{h} = \mathbf{b}$$, suppose we change the beam directions so that $$h_B - h_A = 1$$, $$h_C - h_B = 1$$, and $$h_A - h_C = -2$$. Does a globally consistent 3D depth assignment exist now? *(Hint: check the sum of the right-hand side!)*

---

## 5. What impossible shapes are not

- **Not Möbius bands:** A Möbius strip genuinely *exists* in $$\mathbb{R}^3$$ as a physical strip of paper (see [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/)). A closed Penrose triangle does not exist as the rigid solid it depicts.
- **Not automatic proof of 4D space:** Moving to 4D does not magically make an inconsistent height sum $$0=3$$ vanish—the obstruction is algebraic, not just a lack of elbow room.
- **Not failures of logic:** They are clean negative answers to a specific 3D realizability problem.

---

## 6. Why mathematicians and cognitive scientists care

- **Topology & geometry:** Impossible figures give an unforgettable hands-on picture of cocycles, fiber bundles, and gluing obstructions.
- **Computer vision & CAD:** Detecting inconsistent line drawings or impossible mechanical assemblies uses the exact same linear-algebraic rank tests.
- **Vision science:** They reveal that human perception prioritizes fast local junction matching over slow global consistency checks.

Beautiful mathematics here is the precise sense in which a drawing can **lie globally without containing a single false line**.

---

### Impossible shapes slogans (from video research)

- Local junctions can be fine while the global depth/orientation graph has a cycle contradiction.
- These are not the same as optical brightness illusions; the math issue is **geometric consistency under projection**.
- Escher’s staircases dramatize closed inconsistent monotony of ascent.

## 7. Common confusions

1. **“The Penrose triangle exists as drawn.”** — Only as a 2D picture or an open forced-perspective sculpture viewed from one special spot, never as a closed rigid tribar.
2. **“Impossible shapes refute Euclidean geometry.”** — They refute an inconsistent 3D interpretation of a 2D drawing, not Euclid.
3. **“They are the same as non-orientable surfaces.”** — Möbius bands exist in $$\mathbb{R}^3$$; impossible solids fail a realizability constraint.
4. **“Any weird drawing is mathematically deep.”** — Depth comes from clean local rules paired with a crisp global obstruction.
5. **“Escher staircases have infinite height.”** — Height is locally well-defined but globally multi-valued around the loop, not infinitely tall.
6. **“Tweaking one corner fixes the figure.”** — Obstructions live on the entire cycle; local tweaks only push the mismatch around the loop unless you break the cycle.

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/impossible-shapes/`.

**Recommended order**

1. **ORIENTATION** — SparksMaths — Building the Impossible Penrose Triangle / Penrose triangle culture: [https://www.youtube.com/watch?v=QpwddAqYzkA](https://www.youtube.com/watch?v=QpwddAqYzkA).
2. **ORIENTATION** — Stand-up Maths impossible geometry demos: [https://www.youtube.com/watch?v=QpwddAqYzkA](https://www.youtube.com/watch?v=QpwddAqYzkA).
3. **CORE culture** — Veritasium — Infinite Pattern (Penrose/Escher-adjacent order) documentaries / talks: [https://www.youtube.com/watch?v=48sCx-wBs34](https://www.youtube.com/watch?v=48sCx-wBs34).
4. **INTUITION** — Necker cube / multistable perception science videos: [https://en.wikipedia.org/wiki/Necker_cube](https://en.wikipedia.org/wiki/Necker_cube).
5. **FOUNDATION** — Projective geometry intro lectures: [https://en.wikipedia.org/wiki/Projective_geometry](https://en.wikipedia.org/wiki/Projective_geometry).
6. **CORE** — Graphics / impossible 3D models from 2D projections: [https://en.wikipedia.org/wiki/Impossible_object](https://en.wikipedia.org/wiki/Impossible_object).

Complete URL bibliography: `research/video-research/impossible-shapes/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/impossible-shapes/transcripts/` · status: `research/video-research/impossible-shapes/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/impossible-shapes_QpwddAqYzkA_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/impossible-shapes/references.md`.

### Videos (primary path)

1. SparksMaths — Building the Impossible Penrose Triangle / Penrose triangle culture — https://www.youtube.com/watch?v=QpwddAqYzkA
2. Stand-up Maths impossible geometry demos — https://www.youtube.com/watch?v=QpwddAqYzkA
3. Veritasium — Infinite Pattern (Penrose/Escher-adjacent order) documentaries / talks — https://www.youtube.com/watch?v=48sCx-wBs34
4. Necker cube / multistable perception science videos — https://en.wikipedia.org/wiki/Necker_cube
5. Projective geometry intro lectures — https://en.wikipedia.org/wiki/Projective_geometry
6. Graphics / impossible 3D models from 2D projections — https://en.wikipedia.org/wiki/Impossible_object
7. Penrose stairs explainers — https://en.wikipedia.org/wiki/Penrose_stairs
8. Course strange geometry sibling (internal) (LINK).

### Videos (secondary finds)

9. Optical illusion math museum talks — https://en.wikipedia.org/wiki/Impossible_object

### Papers, books, OCW, and web

10. Penrose & Penrose — Impossible objects (classic note culture): https://en.wikipedia.org/wiki/Penrose_triangle
11. Wikipedia — Penrose triangle: https://en.wikipedia.org/wiki/Penrose_triangle
12. Wikipedia — Impossible object: https://en.wikipedia.org/wiki/Impossible_object
13. Wikipedia — Penrose stairs: https://en.wikipedia.org/wiki/Penrose_stairs
14. Wikipedia — Necker cube: https://en.wikipedia.org/wiki/Necker_cube
15. Wikipedia — M. C. Escher: https://en.wikipedia.org/wiki/M._C._Escher

### Course

16. Course links: [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/), [Paradoxes]({{ site.baseurl }}/contents/en/chapter04/04_07_Paradoxes/), [Symmetry]({{ site.baseurl }}/contents/en/chapter04/04_04_Symmetry/), [Tilings]({{ site.baseurl }}/contents/en/chapter04/04_10_Tilings/). Pack: `research/video-research/impossible-shapes/`.

## Further directions

Existing strange objects: [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/). Logical paradoxes: [Paradoxes]({{ site.baseurl }}/contents/en/chapter04/04_07_Paradoxes/). Local rules with global consequences: [Tilings]({{ site.baseurl }}/contents/en/chapter04/04_10_Tilings/) and [Emergence]({{ site.baseurl }}/contents/en/chapter04/04_12_Emergence/).

## Video tham khảo

- **xem trước** — [Building the Impossible - A Penrose Triangle in Geogebra 3D](https://www.youtube.com/watch?v=QpwddAqYzkA) — SparksMaths, English. Watch first. “Building the Impossible - A Penrose Triangle in Geogebra 3D” orients the lesson’s aim: Explain local consistency vs global realizability for drawings of solid objects.
- [The Infinite Pattern That Never Repeats](https://www.youtube.com/watch?v=48sCx-wBs34) — Veritasium, English. A second pass once the main claim is in view: Explain local consistency vs global realizability for drawings of solid objects.
