---
layout: post
title: "Impossible Shapes"
chapter: '04'
order: 11
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
---

**Impossible shapes** look locally consistent but cannot exist globally as ordinary objects in 3D Euclidean space—the Penrose triangle, Reutersvärd’s earlier triangle, Escher’s endless staircases, and endless gallery of “objects” that fool depth perception. They make a deep geometric theme tangible: **local truths need not glue to a global object**. That theme reappears in advanced geometry and topology whenever cocycles fail to be coboundaries—consistency conditions on overlaps.

**Path:** what “impossible” means → Penrose triangle and depth cues → Escher and closed paths of inconsistency → projection ambiguity → mathematical models (developments, cohomology idea) → related visual paradoxes → confusions, exercises, further directions.

Impossible figures train a habit that advanced geometry rewards repeatedly: before asking whether an object is beautiful or useful, ask whether the local data you wrote down are *glueable*. Manifolds, fiber bundles, discrete height functions on graphs, and CAD assemblies all face versions of this question. The Penrose triangle is simply the version you can put on a slide.

---

## Learning objectives

After this lecture you should be able to:

- Explain **local consistency vs global realizability** for drawings of solid objects.
- Describe the **Penrose triangle** and why each corner is fine while the whole is not.
- Relate impossible figures to **projection** from 3D to 2D and ambiguous depth assignments.
- State a mathematical moral in terms of gluing local data (optional cohomology slogan).
- Distinguish impossible *drawings* from non-orientable *surfaces* (Möbius) that do exist.
- Avoid “Escher proved geometry wrong” and “impossible shapes exist in the fourth dimension” as unexamined slogans.

**Prerequisites.** Basic 3D visualization; parallel projection idea. Topology of Möbius bands from strange geometry helps for contrasts.

---

## 1. Locally fine, globally impossible

A drawing of a cube is a 2D arrangement of lines that we interpret as a 3D object. Most line drawings admit a 3D realization: there exist depths and faces in space projecting to the drawing. An **impossible figure** is a drawing that *suggests* a 3D object with locally plausible junctions—yet no solid polyhedral object in Euclidean 3-space projects to the entire figure while respecting the intended face and occlusion structure.

The impossibility is not that the ink cannot be drawn; the ink is flat and real. The impossibility is **realizability as a single coherent 3D body**.

---

## 2. The Penrose triangle

The **Penrose triangle** (popularized by Roger Penrose; anticipated by Oscar Reutersvärd) shows three beams meeting at right angles in a triangular cycle. Each corner, covered by a hand, looks like a legitimate joint of square beams. The whole figure forces an inconsistent orientation of “out of the page” versus “into the page” as you travel around the loop.

One way to see the contradiction: assign a height function along the beams consistent with the drawn joints; after a full loop the height fails to match. The obstruction is global—supported on a closed path—while every proper subpath is fine.

Physical “Penrose triangles” in sculpture parks work by **forced perspective**: from one viewpoint the projection matches the drawing; walk aside and the beams separate. The 3D object is not a closed triangular prism of beams; it is an open configuration whose projection is special.

This distinction between **picture plane consistency** and **spatial consistency** is worth lingering on. Every line junction in the drawing may match a catalogue of possible 3D corners (arrow junctions, Y-junctions, T-junctions in the language of line-drawing interpretation). The catalogue is local. Global consistency requires a single depth or orientation assignment that satisfies every junction at once. Impossible figures are drawings whose junction constraints admit no global solution—even though every proper subset of constraints may be fine. They are the visual analogue of an unsatisfiable system of equations with satisfiable subsystems.

---

## 3. Escher’s staircases and visual narrative

M. C. Escher’s lithographs (*Ascending and Descending*, *Waterfall*) turn impossible configurations into architectural worlds. Stairs climb endlessly yet return to the start; water falls to power a wheel and flows back uphill. The art is rigorous in a geometric sense: the **projection graph** contains cycles with inconsistent elevation changes.

Escher collaborated with mathematical ideas (Penrose, Coxeter) without claiming that Euclidean geometry is false. He illustrated **multistable and inconsistent depth assignments**—a human visual system trying to complete local cues into a global 3D model and failing gracefully enough to remain beautiful.

---

## 4. Projection, ambiguity, and Necker cousins

Even *possible* objects have ambiguous drawings: the **Necker cube** flips between two depth interpretations. Impossible figures sit further along the spectrum: no single depth assignment works for the whole.

Orthographic or perspective projection

$$
\pi:\mathbb{R}^3\to\mathbb{R}^2
$$

collapses a dimension. Many preimages share a silhouette. Line drawings underdetermine 3D structure; additional assumptions (planarity of faces, right angles, opacity) still may not admit a solution. Computer vision and geometric constraint solving formalize this as systems of equations on vertex coordinates and incidences—sometimes overconstrained and inconsistent.

---

## 5. A mathematical language for inconsistency

Think of an impossible figure as an attempt to glue local 3D charts along overlaps (beam segments, faces). On each overlap, two charts related by a rigid motion or height shift. Around a closed loop of overlaps, the composition of transition maps should be the identity if a global object exists. If the composition is a nontrivial translation in depth, **the cocycle is not trivial**—no global section.

You do not need full sheaf cohomology to own the moral:

> **Local geometric data plus transition rules may fail the cycle condition required for global realization.**

The same pattern appears when constructing manifolds from charts, when bundles have nontrivial topology, and when discrete height functions on graphs have inconsistent cycles. Impossible figures are the coffee-table version of an obstruction class.

Related formalisms include:

- inconsistent linear systems for vertex coordinates,
- non-embeddable polyhedral metrics with given face shapes (Cauchy rigidity contrasts with flexible and impossible complexes),
- branched coverings and multi-valued depth.

---

## 6. What impossible shapes are not

- They are **not** Möbius bands: Möbius bands exist as subsets of $$\mathbb{R}^3$$ (or as abstract surfaces). Impossible triangles do not exist as the closed solid objects they depict.
- They are **not** automatic proof of higher dimensions: sometimes 4D embeddings can realize configurations that 3D cannot, but each claim needs a precise theorem—not a poster caption.
- They are **not** failures of logic: they are failures of a *particular* realizability problem.

Contrast with [strange geometric objects]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/) that *do* exist and challenge intuition by existing.

---

## 7. Why mathematicians and cognitive scientists care

- **Geometry:** constraints, rigidity, projections.
- **Topology:** obstruction to gluing.
- **Vision science:** how brains infer 3D from 2D cues; where inference breaks.
- **Computer graphics:** reverse engineering 3D from sketches; detecting inconsistency.
- **Pedagogy:** a visceral introduction to local-to-global principles.

Beautiful mathematics here is the precise sense in which a drawing can **lie without any single wrong line**.

---

### Impossible shapes slogans (from video research)

- Local junctions can be fine while the global depth/orientation graph has a cycle contradiction.
- These are not the same as optical brightness illusions; the math issue is **geometric consistency under projection**.
- Escher’s staircases dramatize closed inconsistent monotony of ascent.

## 8. Common confusions

1. **“The Penrose triangle exists as drawn.”** — Only as a 2D figure or as a perspective trick, not as the naive closed solid.
2. **“Impossible shapes refute Euclidean geometry.”** — They refute an over-interpreted drawing, not Euclid.
3. **“Same as non-orientable surfaces.”** — Different issues: existence vs inconsistent projection of a depicted solid.
4. **“Any weird drawing is mathematically deep.”** — Depth comes from clean local rules and a clear obstruction.
5. **“Escher staircases have infinite height.”** — In the inconsistent interpretation, height is multi-valued, not an actual infinite building.
6. **“Fixing one corner fixes the figure.”** — Obstructions are global; local edits may move but not remove cycle inconsistency without changing the figure type.

---

## Exercises

1. Cover two corners of a Penrose triangle sketch and describe why each visible corner looks possible.
2. Explain forced perspective sculptures of impossible figures in one paragraph.
3. How does the Necker cube differ from a Penrose triangle?
4. In ≤200 words, state the local-to-global moral with a height-function argument around a loop.
5. Contrast an impossible figure with a Möbius band: which exists in $$\mathbb{R}^3$$ as the object named?
6. (Stretch) Formalize a tiny inconsistent system: three edges with height changes $$+1,+1,+1$$ around a triangle of beams.
7. (Stretch) Find one Escher print and identify a closed path of inconsistent elevation.
8. Link to [tilings]({{ site.baseurl }}/contents/en/chapter04/04_10_Tilings/) (local matching rules) and [paradoxes]({{ site.baseurl }}/contents/en/chapter04/04_07_Paradoxes/) in three sentences.

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
