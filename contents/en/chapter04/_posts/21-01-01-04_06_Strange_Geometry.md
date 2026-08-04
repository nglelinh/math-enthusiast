---
layout: post
title: "Strange Geometric Objects"
chapter: '04'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
---

Mathematics invents spaces that defy everyday intuition: surfaces with only one side, curves that fill squares, spheres with wild embeddings, and decompositions that double a ball. Each **strange geometric object** answers a precise question—and forces us to revise what “shape,” “boundary,” and “volume” mean. The beauty is not shock value alone; it is the discovery that intuition trained on smooth, tame sets is a special case.

**Path:** non-orientable surfaces → space-filling curves → wild embeddings → axiom of choice pathologies → dimension and pathology → why these objects matter → confusions, exercises, further directions.

---

## Learning objectives

After this lecture you should be able to:

- Describe the **Möbius band** and **Klein bottle** and explain non-orientability in elementary terms.
- State what a **space-filling curve** is and why Peano/Hilbert curves do not contradict dimension theory.
- Sketch the idea of the **Alexander horned sphere** as a wild embedding of $$S^2$$ in $$\mathbb{R}^3$$.
- Explain the **Banach–Tarski** statement at slogan level and the role of the **axiom of choice**.
- Distinguish “pathological with choice” from “explicitly constructible fractal pathology.”
- Avoid “Klein bottle holds liquid in 3D” and “space-filling curves raise dimension of the domain.”

**Prerequisites.** Basic topology vocabulary helps (open/closed, continuous image) but vivid geometric description is primary. Comfort with functions $$[0,1]\to\mathbb{R}^2$$.

---

## 1. One-sided surfaces: Möbius and Klein

Take a rectangular strip, give one end a half-twist, and glue the ends: the **Möbius band**. A walker of paint along the “center line” returns to the start after traversing what seemed like both sides—there is only one side and one boundary component (a single closed curve).

The **Klein bottle** is obtained by a more radical identification: a rectangle with opposite sides glued with a twist pattern that cannot be embedded in ordinary three-dimensional space without self-intersection. As an abstract surface (or immersed in $$\mathbb{R}^3$$), it is closed, non-orientable, and has no boundary. Popular glass models in museums are *immersions* with a self-intersecting circle—honest 3D embeddings do not exist for the standard Klein bottle in $$\mathbb{R}^3$$.

**Orientability** fails when there is no consistent choice of “clockwise” across the whole surface. Non-orientable surfaces are not bugs; they are geometric objects classified alongside spheres, tori, and projective planes in the topology of surfaces.

---

## 2. Space-filling curves

Can a continuous path fill a square? **Giuseppe Peano** (1890) and **David Hilbert** constructed continuous surjections

$$
\gamma:[0,1]\to[0,1]^2.
$$

The constructions are iterative: at each stage a polygonal path snakes through a finer grid; the uniform limit is continuous and visits every point of the square.

How does this not destroy the idea of dimension? Several clarifications:

- Continuity alone does not preserve dimension. The map $$\gamma$$ is continuous and surjective but **not injective**; it is not a homeomorphism onto the square.
- Topological dimension of the domain remains $$1$$; the image has topological dimension $$2$$. Dimension of domain and dimension of image need not match under continuous maps that collapse distinctions.
- Space-filling curves are nowhere differentiable in typical constructions—infinite oscillation is the price of filling area.

These examples forced mathematicians to refine “curve,” “path,” and “dimension,” paving the way for modern geometric measure theory and fractal geometry.

Hilbert’s construction is especially teachable: at stage $$n$$ the square is subdivided into $$4^n$$ smaller squares, and a polygonal path visits each in turn with controlled mesh. The limit map hits every point because every point lies in a nested sequence of squares visited at every stage. Continuity follows from uniform control on how far the path moves when the parameter changes little. The argument is elementary in outline and shocking in conclusion—ideal for this chapter’s theme that rigorous definitions sometimes license counterintuitive objects.

---

## 3. Wild embeddings: Alexander’s horned sphere

The standard unit sphere $$S^2\subset\mathbb{R}^3$$ separates space into inside and outside, each simply connected in the appropriate sense (outside is simply connected at infinity in familiar ways; every loop in the complement of a tame sphere can be understood cleanly). **J. W. Alexander** constructed a homeomorphic copy of $$S^2$$ in $$\mathbb{R}^3$$—the **horned sphere**—whose exterior is not simply connected: there are loops in the complement that cannot be contracted without hitting the surface, because infinite interlocking “horns” trap them.

The object is topologically a sphere (as an abstract space) but **wildly embedded**. Embedding type matters: how you place a set in ambient space can create complementary complexity invisible to the intrinsic topology of the set alone. Strange geometry here is about the difference between **what a space is** and **how it sits in another space**.

---

## 4. Banach–Tarski and the axiom of choice

The **Banach–Tarski paradox** (1924): a solid ball in $$\mathbb{R}^3$$ can be partitioned into finitely many pieces that can be rigidly rearranged (rotations and translations) to form **two** solid balls of the same radius as the original.

This does not contradict physical conservation of mass, because the pieces are not solid objects you can cut with a knife: they are non-measurable sets whose construction relies on the **axiom of choice** and exploits the non-commutative richness of the rotation group $$SO(3)$$. There is no constructive recipe that exhibits the pieces as open sets or polyhedra. Banach–Tarski is a theorem about the **limitations of finitely additive measures** defined on all subsets of space when free non-abelian group actions exist.

Compare with fractal constructions: Cantor sets and Koch curves are explicit and choice-free. Banach–Tarski is “strange” in a different register—**foundational pathology** rather than iterative geometry. Both revise intuition about volume; only one is algorithmically visualizable.

---

## 5. Other classics of geometric strangeness

- **Antoine’s necklace:** a wild embedding of a Cantor set in $$\mathbb{R}^3$$ whose complement is not simply connected.
- **Lakes of Wada:** three open “lakes” in the plane that share the same fractal boundary.
- **Exotic spheres:** in high dimensions, smooth manifolds homeomorphic but not diffeomorphic to the standard sphere (Milnor)—smooth structure can be non-unique.
- **Fractal boundaries and Julia sets:** smooth equations, non-smooth invariant sets (see the fractals lecture).

A unifying moral: **tame Euclidean intuition is a low-complexity corner of geometry**. Topology, measure theory, and differential topology each introduce objects that are “ordinary” in their category and “monstrous” in another.

---

## 6. Why these objects matter

- **Foundations of topology.** What should “surface,” “knot,” and “embedding” mean? Strange examples drive definitions.
- **Measure theory.** Vitali sets and Banach–Tarski show why Lebesgue measure cannot apply to all subsets if we keep isometry invariance and countable additivity.
- **Geometric analysis.** Wild boundaries appear in free-boundary problems and geometric measure theory; space-filling ideas relate to analysis on metric spaces.
- **Culture of counterexamples.** A single clear counterexample can kill a false conjecture faster than a thousand confirming instances.

Beautiful mathematics here is the disciplined shock: each object is a theorem-shaped surprise, not a random drawing.

---

## 7. Common confusions

1. **“The Klein bottle is a 3D vase.”** — Standard models self-intersect in $$\mathbb{R}^3$$; the abstract surface is 2-dimensional.
2. **“Space-filling curves mean $$[0,1]$$ is 2-dimensional.”** — The domain stays 1D; the continuous image can be 2D without a homeomorphism.
3. **“Banach–Tarski means physics is wrong.”** — Non-measurable pieces are not physical partitions.
4. **“All strange objects need the axiom of choice.”** — Many fractal and constructive pathologies do not.
5. **“Homeomorphic spheres always sit nicely in space.”** — Alexander’s horned sphere refutes naive embedding hopes.
6. **“Non-orientable means non-existent.”** — Möbius bands exist as physical paper models; non-orientability is real geometry.

---

### Strange geometry hygiene (from video research)

- [Vsauce Banach–Tarski](https://www.youtube.com/watch?v=s86-Z-CbaHA) is excellent culture; remember pieces are not physical volumes.
- Möbius demos ([Tokieda](https://www.youtube.com/watch?v=wKV0GYvR2X8)) train non-orientability better than definitions alone.
- Space-filling curves: continuous + surjective can still be nowhere injective-friendly; dimension theory is subtle.

## Exercises

1. Explain how to build a Möbius band from paper and what happens when you draw a longitudinal line until you return.
2. Why does a continuous surjection $$[0,1]\to[0,1]^2$$ not give a homeomorphism? Give one topological reason (e.g. removing a point).
3. In ≤200 words, contrast intrinsic topology of $$S^2$$ with wild embedding phenomena.
4. State Banach–Tarski carefully and list two hypotheses/ingredients (choice; rotations in 3D).
5. Distinguish constructive fractal strangeness from choice-based paradoxes with one example each.
6. (Stretch) Look up Lakes of Wada and explain the shared-boundary phenomenon in one paragraph.
7. (Stretch) How do exotic spheres (Milnor) change the slogan “homeomorphic implies same smooth shape”?
8. Connect this lecture to [Paradoxes]({{ site.baseurl }}/contents/en/chapter04/04_07_Paradoxes/) and [Fractals]({{ site.baseurl }}/contents/en/chapter04/04_03_Fractals/) in three sentences.

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/strange-geometry/`.

**Recommended order**

1. **CORE** — Vsauce — The Banach–Tarski Paradox: [https://www.youtube.com/watch?v=s86-Z-CbaHA](https://www.youtube.com/watch?v=s86-Z-CbaHA).
2. **ORIENTATION** — Numberphile — Unexpected Shapes / Möbius (Tokieda): [https://www.youtube.com/watch?v=wKV0GYvR2X8](https://www.youtube.com/watch?v=wKV0GYvR2X8).
3. **INTUITION** — Numberphile — An Unexpected Twist on Möbius Strips: [https://www.youtube.com/watch?v=izIKV98Awnw](https://www.youtube.com/watch?v=izIKV98Awnw).
4. **CORE** — Numberphile — Space-Filling Curves: [https://www.youtube.com/watch?v=x-DgL49CFlM](https://www.youtube.com/watch?v=x-DgL49CFlM).
5. **FRONTIER lite** — Alexander horned sphere visual topology talks: [https://en.wikipedia.org/wiki/Alexander_horned_sphere](https://en.wikipedia.org/wiki/Alexander_horned_sphere).
6. **ORIENTATION** — Numberphile — Klein Bottles: [https://www.youtube.com/watch?v=AAsICMPwGPY](https://www.youtube.com/watch?v=AAsICMPwGPY).

Complete URL bibliography: `research/video-research/strange-geometry/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/strange-geometry/transcripts/` · status: `research/video-research/strange-geometry/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/strange-geometry_s86-Z-CbaHA_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/strange-geometry/references.md`.

### Videos (primary path)

1. Vsauce — The Banach–Tarski Paradox — https://www.youtube.com/watch?v=s86-Z-CbaHA
2. Numberphile — Unexpected Shapes / Möbius (Tokieda) — https://www.youtube.com/watch?v=wKV0GYvR2X8
3. Numberphile — An Unexpected Twist on Möbius Strips — https://www.youtube.com/watch?v=izIKV98Awnw
4. Numberphile — Space-Filling Curves — https://www.youtube.com/watch?v=x-DgL49CFlM
5. Alexander horned sphere visual topology talks — https://en.wikipedia.org/wiki/Alexander_horned_sphere
6. Numberphile — Klein Bottles — https://www.youtube.com/watch?v=AAsICMPwGPY
7. Hilbert curve / Peano curve algorithm visuals — https://www.youtube.com/watch?v=x-DgL49CFlM
8. Axiom of choice explained carefully (philosophy-math) — https://www.youtube.com/watch?v=s86-Z-CbaHA

### Videos (secondary finds)

9. Tadashi Tokieda topology demos (Numberphile playlist) — https://www.youtube.com/watch?v=wKV0GYvR2X8

### Papers, books, OCW, and web

10. Wagon — The Banach–Tarski Paradox (Cambridge): https://www.cambridge.org/core/books/banachtarski-paradox/
11. Wikipedia — Möbius strip: https://en.wikipedia.org/wiki/M%C3%B6bius_strip
12. Wikipedia — Space-filling curve: https://en.wikipedia.org/wiki/Space-filling_curve
13. Wikipedia — Banach–Tarski paradox: https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox
14. Wikipedia — Alexander horned sphere: https://en.wikipedia.org/wiki/Alexander_horned_sphere
15. Wikipedia — Axiom of choice: https://en.wikipedia.org/wiki/Axiom_of_choice

### Course

16. Course links: [Paradoxes]({{ site.baseurl }}/contents/en/chapter04/04_07_Paradoxes/), [Fractals]({{ site.baseurl }}/contents/en/chapter04/04_03_Fractals/), [Higher dimensions]({{ site.baseurl }}/contents/en/chapter04/04_08_Higher_Dimensions/), [Impossible shapes]({{ site.baseurl }}/contents/en/chapter04/04_11_Impossible_Shapes/). Pack: `research/video-research/strange-geometry/`.

## Further directions

Logical cousins live in [Paradoxes]({{ site.baseurl }}/contents/en/chapter04/04_07_Paradoxes/). Scaling strangeness continues in [Fractals]({{ site.baseurl }}/contents/en/chapter04/04_03_Fractals/). Visual inconsistency without leaving drawings appears in [Impossible shapes]({{ site.baseurl }}/contents/en/chapter04/04_11_Impossible_Shapes/). Dimension as a parameter expands in [Higher dimensions]({{ site.baseurl }}/contents/en/chapter04/04_08_Higher_Dimensions/).
