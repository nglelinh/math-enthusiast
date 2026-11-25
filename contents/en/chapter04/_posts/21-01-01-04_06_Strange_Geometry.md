---
layout: post
title: "Strange Geometric Objects"
chapter: '04'
order: 7
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
---

Take a strip of paper, give one end a single half-twist, and tape the ends together to make a **Möbius strip**. Now pick up a pair of scissors and cut straight down the middle of the strip. Everyday intuition says a loop cut in half becomes two narrower loops. Instead, your scissors finish the cut and leave you holding **one single loop**, twice as long and with two full twists. Now try a second Möbius strip, but start cutting one-third of the way from the edge: you walk around the strip *twice* before returning to your starting cut, and the strip splits into **two interlocked rings**—one narrow Möbius strip and one longer two-sided loop.

That thirty-second kitchen-table experiment captures the spirit of **strange geometric objects**. Mathematics is full of spaces that ambush everyday intuition: surfaces with only one side, continuous curves that completely fill a solid square, spheres whose exteriors tangle like infinite barbed wire, and decompositions that cut one solid ball into finitely many pieces and reassemble them into two identical balls. None of these are parlor tricks. Each one is a sharp diagnostic tool—forcing mathematicians to ask what "side," "dimension," "embedding," and "volume" actually mean when smooth Euclidean intuition reaches its limit.

**Path:** non-orientable surfaces and gluing coordinates → space-filling curves and Hilbert lengths → wild embeddings → Banach–Tarski and the axiom of choice → why counterexamples matter → common confusions and further directions.

---

## Learning objectives

After this lecture you should be able to:

- Describe the **Möbius band** and **Klein bottle** and explain non-orientability using coordinate gluing.
- State what a **space-filling curve** is, compute the exact length of the $$n$$-th Hilbert curve, and explain why it does not break dimension theory.
- Sketch **Alexander’s horned sphere** as a wild embedding of $$S^2$$ in $$\mathbb{R}^3$$.
- Explain the **Banach–Tarski paradox** at the conceptual level and identify the role of the **axiom of choice** and non-measurable sets.
- Distinguish constructive geometric pathologies (Hilbert curves, Cantor sets) from non-constructive choice-based pathologies (Banach–Tarski).
- Avoid claiming that "a Klein bottle holds water in 3D" or that "a space-filling curve makes $$[0,1]$$ two-dimensional."

**Prerequisites.** Basic familiarity with continuous functions $$[0,1]\to\mathbb{R}^2$$; a little topology vocabulary (open/closed, injective/surjective) helps, though geometric pictures carry the day.

---

## Key ideas: Why Topology Loves "Monsters"

In the nineteenth century, mathematicians called space-filling curves and nowhere-differentiable paths "monsters" and tried to banish them. By the twentieth century, they realized those monsters were actually lighthouses marking the exact boundaries of theorems across four pillars:

1. **Topology of Surfaces (Quotient Spaces):** Topologists build surfaces by taking flat polygons and gluing their edges according to rules. Two surfaces can look identical in every tiny neighborhood (both are locally flat 2D planes) yet differ globally—some are **orientable** (consistent "clockwise" everywhere, like a sphere or torus), while others are **non-orientable** (a Möbius band or Klein bottle).
2. **Dimension Theory & Continuity:** Before 1890, people assumed a continuous curve could only trace a 1D thin thread. Peano and Hilbert shattered that assumption, forcing mathematicians to prove **invariance of domain** (Brouwer): dimension *is* preserved by **homeomorphisms** (continuous bijections with continuous inverses), not by mere continuous surjections.
3. **Geometric Topology & Embeddings:** Knowing *what* a space is intrinsically (say, a sphere $$S^2$$) does not tell you *how* it sits inside a larger ambient space $$\mathbb{R}^3$$. Knot theory and wild embeddings like Alexander’s horned sphere study the topology of the *complement*—the space left over around the object.
4. **Measure Theory & Foundations:** Everyday volume works seamlessly on cubes, spheres, and smooth shapes. Vitali sets and the Banach–Tarski theorem prove that if you accept the **axiom of choice**, no volume function can measure *every* subset of $$\mathbb{R}^3$$ while staying invariant under rigid motions. That discovery gave birth to modern **Lebesgue measure theory**.

---

## 1. One-sided surfaces: Möbius and Klein

You can describe the **Möbius band** with total algebraic precision as a quotient of the rectangle $$[0,1]\times[-1,1]$$. Glue the right edge to the left edge *upside down*:

$$
(1, y) \sim (0, -y) \qquad \text{for all } y\in[-1,1].
$$

### Worked example 1: Tracking an arrow around a Möbius band

Imagine a tiny vertical arrow standing at the starting point $$(0,0)$$ and pointing upward toward $$(0, +\varepsilon)$$. Slide this arrow steadily to the right along the centerline $$y=0$$:
- At $$x = 0.5$$, it sits at $$(0.5, 0)$$ pointing toward $$(0.5, +\varepsilon)$$.
- When it reaches the right edge $$x = 1$$, its base is at $$(1, 0)$$ and its tip is at $$(1, +\varepsilon)$$.
- Now apply the gluing rule $$(1, y) \sim (0, -y)$$: the base $$(1, 0)$$ identifies with $$(0, 0)$$, while the tip $$(1, +\varepsilon)$$ identifies with $$(0, -\varepsilon)$$!

After one full trip around the band, the arrow returns to the exact same point—**pointing upside down**. That single sign flip $$y \mapsto -y$$ is the mathematical meaning of **non-orientability**: there is no consistent global definition of "up" or "clockwise" on the surface. It takes *two* full laps to return the arrow to its original orientation, which is also why the boundary of the Möbius strip is one single continuous edge rather than two.

The **Klein bottle** takes this one step further: take the unit square $$[0,1]^2$$, glue the top and bottom edges normally $$(x,1)\sim(x,0)$$, and glue the left and right edges with a twist $$(1,y)\sim(0,1-y)$$. The result is a closed, boundaryless, non-orientable surface. Unlike the Möbius band, the Klein bottle cannot sit in ordinary 3D space without passing through itself: museum glass models are *immersions* with a self-intersection loop, not true embeddings. In $$\mathbb{R}^4$$, however, the fourth coordinate provides enough room to lift one sheet over the other with zero self-intersection.

---

### Short video: The Hilbert curve, order by order

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/hilbert-curve_en.mp4"></video>
</div>

Order $$n$$ visits all $$4^n$$ cells of a $$2^n \times 2^n$$ grid in one unbroken path, and each finer order refines the previous one. The length keeps doubling, while the limit curve passes through every point of the square.


### Try it yourself: Explore the Hilbert curve

<div class="mex-explainer" data-mex="hilbert" data-lang="en"></div>


## 2. Space-filling curves

Can a continuous one-dimensional path pass through *every single point* of a two-dimensional square? In 1890, **Giuseppe Peano** shocked the mathematical world by answering yes, and a year later **David Hilbert** gave a cleaner geometric construction of a continuous surjection

$$
\gamma:[0,1]\to[0,1]^2.
$$

### Worked example 2: Exact length of the $$n$$-th Hilbert curve

At order $$n$$, divide the unit square $$[0,1]^2$$ into a $$2^n \times 2^n$$ grid of $$4^n$$ tiny squares, each of side length $$2^{-n}$$. The order-$$n$$ Hilbert curve connects the centers of all $$4^n$$ squares in one continuous polygonal chain without lifting the pen:
- Total number of cells visited: $$4^n$$.
- Number of straight segments connecting adjacent cell centers: $$4^n - 1$$.
- Length of each segment (distance between neighboring cell centers): $$2^{-n}$$.

Multiply to get the exact total length $$L_n$$:

$$
L_n = (4^n - 1)\cdot 2^{-n} = 2^n - 2^{-n}.
$$

| Order $$n$$ | Grid cells $$4^n$$ | Segment length $$2^{-n}$$ | Total length $$L_n = 2^n - 2^{-n}$$ |
| :--- | :--- | :--- | :--- |
| $$1$$ | $$4$$ | $$0.5$$ | $$1.5$$ |
| $$2$$ | $$16$$ | $$0.25$$ | $$3.75$$ |
| $$3$$ | $$64$$ | $$0.125$$ | $$7.875$$ |
| $$10$$ | $$1{,}048{,}576$$ | $$0.000977$$ | $$1023.999$$ |

As $$n\to\infty$$, the polygonal paths converge uniformly to a continuous curve $$\gamma:[0,1]\to[0,1]^2$$ whose length explodes to $$\infty$$ and whose image hits every point in the square!

**Why doesn’t this prove $$[0,1]$$ and $$[0,1]^2$$ have the same dimension?** Because $$\gamma$$ is **not injective**—it touches corners and boundary points multiple times (so it has no continuous inverse). In fact, $$[0,1]$$ and $$[0,1]^2$$ can *never* be homeomorphic: remove one interior point from $$[0,1]$$ and the interval breaks into two disconnected pieces, whereas removing any single point from the square $$[0,1]^2$$ still leaves it completely connected! Continuity alone can raise dimension; a true topological equivalence (homeomorphism) cannot.

---

## 3. Wild embeddings: Alexander’s horned sphere

An ordinary beach ball $$S^2 \subset \mathbb{R}^3$$ is tame: every closed loop of string floating in the air outside the ball can be shrunk smoothly to a point without touching the ball. In 1924, **J. W. Alexander** constructed a topological copy of $$S^2$$ inside $$\mathbb{R}^3$$—the **Alexander horned sphere**—by pushing out two horns from a sphere, splitting each horn into two smaller horns that almost hook around each other, and repeating infinitely many times.

As an abstract surface, the horned sphere is completely homeomorphic to the ordinary sphere $$S^2$$. Yet its *exterior* in $$\mathbb{R}^3$$ is not simply connected: a loop of string threaded around one of the interlocking pairs of horns can never be pulled free without slicing the surface. The lesson is profound: **what a space is intrinsically** and **how it sits inside a larger space** are two completely different questions.

---

## 4. Banach–Tarski and the axiom of choice

In 1924, Stefan Banach and Alfred Tarski proved one of the most famous counterintuitive theorems in mathematics: a solid ball in $$\mathbb{R}^3$$ can be partitioned into finitely many pieces (as few as **five**) and moved *only by rigid rotations and translations* to reassemble **two** solid balls, each identical in size to the original.

This does not violate physical conservation of mass, because you cannot cut those pieces with a knife or a laser. The pieces are **non-measurable sets**—infinitely scattered clouds of points built using the **axiom of choice** and exploiting the fact that the 3D rotation group $$SO(3)$$ contains a free non-commutative subgroup (a hidden cousin of Hilbert’s Hotel inside 3D rotations). In 2D, the rotation group $$SO(2)$$ is commutative, so no analogous Banach–Tarski doubling exists for a flat disk using rigid motions alone.

Compare the two flavors of geometric strangeness we have met:
- **Constructive (choice-free):** Möbius bands, Hilbert curves, and Alexander’s horned sphere have explicit step-by-step recipes you can code and visualize.
- **Foundational (requires choice):** Banach–Tarski pieces cannot be drawn or computed; they prove that no rotation-invariant, finitely additive volume function can exist on *all* subsets of $$\mathbb{R}^3$$.

---

### Explanation: Why "Pathological" Objects Are Actually Diagnostic Tools

Whenever a geometric object feels impossible, ask *which hidden assumption did it just expose?* Trace the four-step diagnostic pattern:

1. **Test local vs. global intuition.** A Möbius band is flat everywhere locally, yet the gluing twist $$(1,y)\sim(0,-y)$$ destroys global orientability. Local tameness never guarantees global simplicity.
2. **Separate continuity from topological equivalence.** Hilbert’s curve $$\gamma:[0,1]\to[0,1]^2$$ is continuous and surjective with length $$L_n = 2^n - 2^{-n} \to \infty$$, proving that continuity alone does not preserve dimension—you need a bijective homeomorphism (which fails the one-point-removal connectivity test).
3. **Separate intrinsic shape from ambient embedding.** Alexander’s horned sphere is intrinsically identical to a smooth sphere, yet its infinite branching traps loops in the surrounding 3D space.
4. **Separate physical matter from arbitrary set subsets.** Banach–Tarski shows that "every subset of space has a well-defined volume" is mathematically incompatible with the axiom of choice and rigid motions in 3D—forcing measure theory to restrict volume to *measurable* sets.

**Quick check.** If you remove a single point from the middle of the interval $$[0,1]$$, you get two disconnected pieces. What happens if you remove a single point from a circle $$S^1$$—and how many points must you remove to disconnect $$S^1$$?

---

## 5. Other classics of geometric strangeness

- **Antoine’s necklace:** A wild embedding of a Cantor set in $$\mathbb{R}^3$$ whose complement is not simply connected.
- **Lakes of Wada:** Three disjoint open "lakes" in the plane that share the *exact same* fractal boundary—every boundary point touches all three lakes simultaneously.
- **Exotic spheres:** John Milnor (1956) discovered 7-dimensional manifolds that are topologically homeomorphic to the standard 7-sphere $$S^7$$, yet carry a fundamentally incompatible smooth calculus structure (not diffeomorphic).
- **Fractal boundaries and Julia sets:** Simple complex polynomials generating infinitely intricate boundaries (see [Fractals]({{ site.baseurl }}/contents/en/chapter04/04_03_Fractals/)).

The unifying moral: **tame Euclidean geometry is just a quiet, low-complexity corner of the mathematical universe.**

---

## 6. Why these objects matter

- **Foundations of topology.** Strange examples forced crisp definitions of manifold, orientability, knot, and tame embedding.
- **Measure theory.** Vitali sets and Banach–Tarski explain why probability and integration rest on $$\sigma$$-algebras of measurable sets rather than arbitrary power sets.
- **Computer science & data indexing.** Space-filling curves (especially Hilbert curves) are used in real-world databases, geospatial indexing, and GPU memory layouts because they preserve spatial locality better than simple row-by-row scans!
- **The power of counterexamples.** One sharp counterexample refutes a false conjecture more decisively than a thousand confirming examples.

---

## 7. Common confusions

1. **“The Klein bottle is a 3D vase.”** — Standard glass models self-intersect in $$\mathbb{R}^3$$; the true abstract surface is 2-dimensional and embeds cleanly only in $$\mathbb{R}^4$$.
2. **“Space-filling curves mean $$[0,1]$$ is 2-dimensional.”** — The domain remains 1D; the map fails injectivity and is not a homeomorphism.
3. **“Banach–Tarski disproves conservation of mass.”** — Non-measurable point clouds have no physical volume and cannot be constructed from atoms.
4. **“All strange objects need the axiom of choice.”** — Möbius strips, Hilbert curves, and Alexander’s horned sphere are completely explicit and choice-free.
5. **“Homeomorphic spheres always sit nicely in space.”** — Alexander’s horned sphere refutes that assumption.
6. **“Non-orientable means imaginary.”** — You can build a Möbius band with paper and tape in ten seconds.

---

### Strange geometry hygiene (from video research)

- [Vsauce Banach–Tarski](https://www.youtube.com/watch?v=s86-Z-CbaHA) is excellent culture; remember pieces are not physical volumes.
- Möbius demos ([Tokieda](https://www.youtube.com/watch?v=wKV0GYvR2X8)) train non-orientability better than definitions alone.
- Space-filling curves: continuous + surjective can still be nowhere injective-friendly; dimension theory is subtle.

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

## Video tham khảo

- **xem trước** — [The Banach–Tarski Paradox](https://www.youtube.com/watch?v=s86-Z-CbaHA) — Vsauce, English. Watch first. “The Banach–Tarski Paradox” orients the lesson’s aim: Describe the Möbius band and Klein bottle and explain non-orientability in elementary terms.
- [Unexpected Shapes (Part 1) - Numberphile](https://www.youtube.com/watch?v=wKV0GYvR2X8) — Numberphile, English. A second pass once the main claim is in view: Describe the Möbius band and Klein bottle and explain non-orientability in elementary terms.
- [An Unexpected Twist on Möbius Strips - Numberphile](https://www.youtube.com/watch?v=izIKV98Awnw) — Numberphile, English. Further depth after the first two, still tied to this lesson: Describe the Möbius band and Klein bottle and explain non-orientability in elementary terms.
