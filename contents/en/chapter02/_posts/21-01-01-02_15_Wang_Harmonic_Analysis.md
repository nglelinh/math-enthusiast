---
layout: post
title: "Hong Wang: Harmonic Analysis and Geometric Measure Theory (Fields Medal 2026)"
chapter: '02'
order: 14
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

> **Learning path A — Kakeya (step 2 of 3)**  
> **1. Before:** [Ch.1 Kakeya problem map]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/)  
> **2. You are here:** Ch.2 Wang lecture (full theory)  
> **3. Next:** [Ch.7 Kakeya studio]({{ site.baseurl }}/contents/en/chapter07/07_02_Explore_Kakeya/)  
> *Do Ch.1 first if this is your first encounter with Kakeya.*

Imagine holding a thin 1-meter needle inside a room and trying to point it in **every possible direction in three-dimensional space**. You might guess that a shape containing a 1-meter line segment in every direction must occupy a solid chunk of volume. Remarkably, Abram Besicovitch proved a century ago that you are wrong: by cleverly overlapping segments like a fractal Venetian blind, you can pack **every single direction** into a set whose total 3D volume is literally **zero**!

Yet a deeper mystery lingered for a hundred years: even if such a **Kakeya set** has zero volume, can it be squashed down into a lower-dimensional fractal—say, dimension $$2.5$$ or $$2.9$$—or must its **Hausdorff and Minkowski dimension** still be the full **3**?

In February 2025, **Hong Wang** (NYU Courant / IHES) and **Joshua Zahl** (UBC) posted a landmark 127-page proof settling the **three-dimensional Kakeya set conjecture**: every Kakeya set in $$\mathbb{R}^3$$ has dimension 3. At ICM 2026 in Philadelphia, **Hong Wang** received the **Fields Medal 2026**—becoming the **third woman** in history to win the prize (after Maryam Mirzakhani in 2014 and Maryna Viazovska in 2022).

> For her work in harmonic analysis and geometric measure theory, including applications of multiscale and decoupling techniques to the local smoothing conjecture for the planar wave equation, and major advances in Fourier restriction, Falconer distance sets, Furstenberg sets in the plane, and the Kakeya problem in three dimensions.  
> — [IMU, Fields Medal 2026 citation](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf)

This essay traces the full arc—with hand-checkable Cantor-set and $$\delta$$-tube calculations—from a playful 1917 needle puzzle to one of the deepest multiscale breakthroughs in harmonic analysis:

**Needle problem → Besicovitch sets → measure vs. dimension → $$\delta$$-tubes → Wang–Zahl (2025) → harmonic analysis → Fields portfolio.**

---

## Learning objectives

After this lecture you should be able to:

- State Kakeya’s needle problem and Besicovitch’s measure-zero construction in the plane.
- Compute by hand the Lebesgue measure ($$0$$) and Hausdorff/Minkowski dimension ($$\ln 2/\ln 3 \approx 0.631$$) of the Cantor set to see why **volume zero does not force low dimension**.
- Formulate the **Kakeya set conjecture** in $$\mathbb{R}^n$$ and state what is proved for $$n=2$$ (Davies) and $$n=3$$ (Wang–Zahl) versus open for $$n\ge 4$$.
- Count $$\delta$$-tubes in $$\mathbb{R}^3$$ by hand ($$N \sim \delta^{-2}$$ tubes of volume $$\pi\delta^2$$) and explain why heavy overlap is the heart of the difficulty.
- Follow the 4-step **multiscale self-improvement** logic of Wang–Zahl (2025) without losing track of joint credit.
- Summarize Wang’s broader Fields portfolio with collaborators named (local smoothing, Falconer distance sets, 2D Furstenberg sets, Fourier restriction).

**Prerequisites.** Euclidean geometry, basic measure intuition, and comfort with logarithms and fractals.

---

## Key ideas: What Are Harmonic Analysis and Geometric Measure Theory?

Why did a playful puzzle about turning a needle become one of the central problems of twenty-first-century analysis? Because it lives at the exact meeting point of two major disciplines.

### 1. Geometric Measure Theory (GMT): Measuring Wild Fractal Shapes
**What is it?** Classical calculus measures smooth lengths, areas, and volumes. **Geometric measure theory** extends measurement to rough, jagged, zero-volume fractal sets—asking how much space they "fill" across finer and finer scales.

**What does it study?**
- **Hausdorff & Minkowski dimension:** Fine-grained rulers that distinguish a 1D line, a $$0.631$$-dimensional Cantor dust, and a zero-volume yet full-3D Kakeya set.
- **Projections, distances, and directional sets:** Falconer’s distance-set problem, Furstenberg sets, and Kakeya sets—all measuring how strongly lines, tubes, or distances can overlap.

### 2. Harmonic Analysis & Wave Packets: Seeing Directions in Frequency Space
**What is it?** Harmonic analysis decomposes waves and signals via the **Fourier transform**. When you build a solution to the **wave equation** or study **Fourier restriction** (restricting a wave’s frequencies to a curved surface like a sphere or paraboloid), the wave naturally splits into localized **wave packets**—each shaped like a long, thin **$$\delta$$-tube** pointing in a specific direction!

**What does it study?**
- **Interference & concentration:** If wave packets from many directions can pile up on a tiny region without spreading out, wave energy can focus explosively. Proving that tubes pointing in different directions *must* spread out (the Kakeya problem!) is the geometric backbone of **Fourier restriction**, **Bochner–Riesz**, and **local smoothing** for wave PDEs.

### 3. Multiscale Analysis & Decoupling: Zooming Across Scales
**What is it?** When a problem looks chaotic at a single scale $$\delta$$, modern analysts examine it simultaneously across a ladder of intermediate scales $$1 \gg \rho_1 \gg \rho_2 \gg \dots \gg \delta$$.

**What does it study?**
- **Decoupling (Bourgain–Demeter) & induction on scales:** Proving that if tubes overlap catastrophically at one scale, they are forced into rigid geometric patterns (like sticky bundles or thin flat "grains") that can be exploited to gain volume at another scale!

---

## 1. The needle problem: simple to state, strange to solve

In 1917, **Sōichi Kakeya** asked: what is the smallest area of a planar region in which a unit-length needle can be continuously turned $$180^\circ$$? Rotating around the midpoint sweeps a disk of area $$\pi/4$$; a three-pointed **deltoid** cuts that in half to $$\pi/8$$. Everyone expected a positive minimum area—until Besicovitch shattered that intuition.

![Unit segments pointing in many directions]({{ site.baseurl }}/img/chapter_img/kakeya_needle_directions.svg)

*Figure. A Kakeya set must contain a unit segment for every direction—the containing set need not look “full.”*

---

## 2. Besicovitch sets: every direction, measure zero

A **Kakeya set** (also called a **Besicovitch set**) in $$\mathbb{R}^n$$ is a static set containing a unit line segment in **every** direction.

**Abram Besicovitch** (1919–1928) proved that in the plane (and in every $$\mathbb{R}^n$$, $$n\ge 2$$) there exist Kakeya sets of **Lebesgue measure zero**! By cutting a triangle into thin slivers, sliding them so they heavily overlap, and iterating (the **Perron tree** / **Venetian blind** trick), you preserve every direction while driving the total area down to zero.

![Triangle cut and shift]({{ site.baseurl }}/img/chapter_img/besicovitch_triangle_overlap.svg)

*Figure. Classical cartoon: cut an equilateral triangle, shift halves to increase overlap, iterate.*

![Venetian blind rearrangement]({{ site.baseurl }}/img/chapter_img/venetian_blinds_kakeya.svg)

*Figure. Schematic Venetian-blind rearrangement (not a literal full construction).*

### Davies (1971): empty of area, full of dimension
In 1971, **Roy Davies** proved that every Kakeya set $$E \subset \mathbb{R}^2$$ has **Hausdorff dimension 2**:

$$
\lvert E\rvert = 0 \quad\text{is possible, yet}\quad \dim_H(E) = 2.
$$

---

## 3. Measure versus dimension (a hand-checkable fractal)

How can a set have zero length/area/volume and still carry large dimension?

### Hand-Verifiable Example 1: The Middle-Thirds Cantor Set
Start with the unit interval $$[0,1]$$. At each step $$k$$, delete the open middle third of every remaining interval:
- After $$k$$ steps, you have $$N_k = 2^k$$ intervals, each of length $$r_k = (1/3)^k$$.
- **Total length (Lebesgue measure):** $$L_k = 2^k \cdot (1/3)^k = (2/3)^k \longrightarrow 0$$ as $$k \to \infty$$! So the Cantor set has **measure zero**.
- **Minkowski / Hausdorff dimension:** Count how many boxes of size $$r_k = 3^{-k}$$ are needed to cover it: $$N(r_k) = 2^k$$. Taking the scaling exponent:
  $$
  \dim_M(C) = \lim_{k\to\infty} \frac{\ln N(r_k)}{\ln(1/r_k)} = \lim_{k\to\infty} \frac{\ln(2^k)}{\ln(3^k)} = \frac{\ln 2}{\ln 3} \approx 0.631!
  $$

Measure is a blunt yes/no scale at top dimension; **Hausdorff and Minkowski dimension** measure how fast the covering count explodes as the ruler shrinks!

> **Volume zero does not imply dimension less than 3.**  
> A set in $$\mathbb{R}^3$$ can have Lebesgue measure zero and still have Hausdorff and Minkowski dimension 3.

![Measure versus dimension]({{ site.baseurl }}/img/chapter_img/measure_vs_dimension.svg)

*Figure. Two different notions of size: measure vs dimension.*

---

## 4. The Kakeya set conjecture

**Conjecture (Kakeya set conjecture in $$\mathbb{R}^n$$).**  
Every Kakeya set $$K\subset\mathbb{R}^n$$ has Hausdorff and Minkowski dimension $$n$$:

$$
\dim_H(K) = \dim_M(K) = n.
$$

| Ambient dimension | Status |
|-------------------|--------|
| $$n=1$$ | Trivial |
| $$n=2$$ | Proved (Davies, 1971) |
| $$n=3$$ | Proved (**Wang–Zahl**, 2025) |
| $$n\ge 4$$ | Open (partial lower bounds exist) |

---

## 5. Why three dimensions is hard: counting $$\delta$$-tubes

To attack Kakeya quantitatively, thicken each unit line segment into a cylinder of length $$1$$ and radius $$\delta$$—a **$$\delta$$-tube**.

### Hand-Verifiable Example 2: Counting $$\delta$$-Tubes in $$\mathbb{R}^3$$
How many $$\delta$$-separated directions exist on the 2D unit sphere $$S^2$$ (area $$4\pi$$)?
- Each direction patch of angular radius $$\delta$$ covers area $$\sim \pi\delta^2$$ on $$S^2$$, so a full $$\delta$$-separated net of directions in $$\mathbb{R}^3$$ contains roughly
  $$
  N \sim \frac{4\pi}{\pi\delta^2} \sim \delta^{-2} \text{ tubes!}
  $$
- Each individual $$\delta$$-tube has length $$1$$ and cross-sectional area $$\pi\delta^2$$, so its volume is $$\lvert T_i\rvert = \pi\delta^2$$.
- Multiply them together! If the tubes barely overlapped, their total volume would be
  $$
  N \cdot \lvert T_i\rvert \sim \delta^{-2} \cdot (\pi\delta^2) = \pi = O(1) \quad (\text{dimension } 3!).
  $$
- If instead the union $$\bigcup_{i=1}^N T_i$$ had volume $$\sim \delta^{3-d}$$ (corresponding to dimension $$d < 3$$), then on average every point inside the union would have to be pierced by **$$\sim \delta^{-(3-d)}$$ different tubes at once**!

![δ-tubes with heavy overlap]({{ site.baseurl }}/img/chapter_img/kakeya_delta_tubes.svg)

*Figure. Many δ-tubes; heavy overlap is where the geometry becomes subtle.*

In 2D, two lines pointing in different directions cross at a single point—simple! In 3D, skew lines can narrowly miss each other, or conspire to lie along curved ruled surfaces (like a **regulus**, a hyperbolic paraboloid saddle) or cluster into tiny flat "grains." Two-dimensional arguments completely fail to scale up.

---

## 6. What Wang and Zahl proved

<div class="textbook-theorem" markdown="1">
**Theorem (Wang–Zahl, 2025).**  
Every Kakeya set $$K\subset\mathbb{R}^3$$ satisfies

$$
\dim_H(K) = \dim_M(K) = 3.
$$
</div>

Primary source: *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions* ([arXiv:2502.17655](https://arxiv.org/abs/2502.17655); 127 pages).

---

### Explanation: Wang–Zahl’s Multiscale Self-Improvement Engine

Why did 3D Kakeya resist legends like Wolff, Bourgain, Katz, Tao, and Guth for decades, and how did Hong Wang and Joshua Zahl finally crack it in 2025? Follow the four-step architecture slowly:

#### Step 1: Generalize from Kakeya sets to "convex-Wolf" tube families
Instead of restricting only to sets with one tube per direction, Wang and Zahl formulated a sharper, more flexible **inductive hypothesis**: consider *any* family of $$\delta$$-tubes in $$\mathbb{R}^3$$ obeying a **non-concentration (convex-containment) bound**—no convex shape $$V$$ (such as a flat slab, cylinder, or box) is allowed to trap disproportionately too many tubes. Proving almost-maximal volume for all such tube families automatically implies $$\dim(K)=3$$ for every Kakeya set.

#### Step 2: Conquer the hardest extreme first—"sticky" Kakeya sets (2022)
In a **sticky** Kakeya set, tubes pointing in nearly the same direction stick together tightly inside fatter intermediate $$\rho$$-tubes, creating approximate self-similarity across scales $$1 \to \rho \to \delta$$. Earlier, Wang and Zahl ([arXiv:2210.09581](https://arxiv.org/abs/2210.09581), *J. Amer. Math. Soc.* 2026) proved the **sticky Kakeya conjecture in 3D**—showing that if tubes stick together tightly, they still must fill dimension 3.

#### Step 3: Force hidden structure ("grains") whenever overlap is extreme
Now consider a *general* hypothetical 3D Kakeya counterexample with dimension $$d < 3$$. Because the union of $$\delta$$-tubes is unusually small, tubes must overlap furiously. Wang and Zahl proved a structural dichotomy across intermediate scales $$1 \gg \rho \gg \delta$$: either the tubes are **sticky** (already handled!) or they shatter into tiny flat **grains** (thin pancake-like regions where bundles of tubes intersect heavily along planes).

#### Step 4: Multiscale self-improvement without "Chinese whispers" loss
Classical induction on scales suffered from cumulative error loss—like a game of telephone ("Chinese whispers") where passing through many scales degrades the exponent. By tracking convex-set non-concentration directly across scales, Wang and Zahl turned any bad configuration at scale $$\delta$$ into a strictly **better** configuration at another scale—forcing a contradiction whenever $$d < 3$$ and locking in $$\dim_H(K) = \dim_M(K) = 3$$!

In one schematic line:

$$
\text{Suppose }\dim(K) < 3
\;\xrightarrow{\;\text{extreme }\delta\text{-tube overlap}\;}\;
\text{Sticky bundles or flat grains}
\;\xrightarrow{\;\text{convex-set multiscale induction}\;}\;
\text{Self-improvement contradiction} \implies \dim(K) = 3.
$$

**Credit.** This is **joint work** of **Hong Wang and Joshua Zahl**, crowning a century-long climb built on Besicovitch, Davies, Wolff, Bourgain, Katz, Tao, and Guth.

![Historical timeline]({{ site.baseurl }}/img/chapter_img/kakeya_history_timeline.svg)

*Figure. Selected milestones from Kakeya (1917) to Wang’s Fields Medal (2026).*

---

## 7. Why harmonic analysis cares

Kakeya sits at the base of the famous harmonic-analysis tower:

**Kakeya** → **Fourier restriction** → **Bochner–Riesz** → **local smoothing** (wave PDE).

When waves of similar wavelength travel in many directions, their energy organizes into wave packets supported on $$\delta$$-tubes. How those tubes overlap governs whether wave energy can focus explosively or must disperse.

![From Kakeya to harmonic analysis]({{ site.baseurl }}/img/chapter_img/kakeya_to_harmonic_analysis.svg)

*Figure. Conceptual chain from tube geometry to Fourier and PDE themes.*

Solving 3D Kakeya is a once-in-a-generation foundation breakthrough; higher-dimensional Kakeya ($$n \ge 4$$) and sharp restriction/Bochner–Riesz conjectures remain exciting open frontiers. See [Quanta video](https://www.youtube.com/watch?v=5J3tYU_-IZI) and [Quanta article](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/).

---

## 8. Beyond Kakeya: the Fields portfolio (IMU long citation)

The 2026 Fields Medal recognizes a sweeping body of work across harmonic analysis and geometric measure theory:

| Theme | Collaborators (selected) | What was advanced |
|-------|--------------------------|-------------------|
| **Local smoothing** (planar wave equation) | Larry Guth, Ruixiang Zhang | Multiscale + decoupling methods resolving the local smoothing conjecture in the plane (IMU long citation) |
| **Falconer distance sets** | Guth, Alex Iosevich, Yumeng Ou | Major results linking Hausdorff dimension to distance distributions |
| **Furstenberg sets** (plane) | Kevin Ren | Resolution of the 2D Furstenberg set conjecture ([arXiv:2308.08819](https://arxiv.org/abs/2308.08819)): a $$(s,t)$$-Furstenberg set has dimension at least $$\min\bigl(s+t,\frac{3s+t}{2},s+1\bigr)$$ |
| **Fourier restriction** | various | Structural advances feeding the restriction tower |
| **Kakeya in 3D** | Joshua Zahl | Sticky case (JAMS 2026) and full Kakeya dimension 3 (arXiv:2502.17655) |

### Path (brief biography)

Born in Guilin, China; studied at Peking University and École Polytechnique; PhD at MIT under **Larry Guth**; held positions at IAS and UCLA before joining NYU Courant and IHES. A cascade of honors (Salem Prize, Maryam Mirzakhani New Horizons Prize, Ostrowski Prize, Clay Research Award) led to the Fields Medal at **ICM 2026 (Philadelphia)**.

---

## 9. The deepest paradox, restated

$$
\operatorname{Vol}(K)=0
\quad\text{is possible,}\quad
\dim(K)=3
\quad\text{is mandatory in }\mathbb{R}^3.
$$

You cannot pack unit segments in all three-dimensional directions into a genuinely lower-dimensional fractal.

---

## Common misconceptions (fact-check)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Wang alone solved Kakeya in 3D.” | **Fail** | Joint work with Joshua Zahl. |
| “Kakeya sets in 3D must have positive volume.” | **Fail** | Measure zero remains possible; the theorem is about **dimension**. |
| “The Fields Medal is only for Kakeya.” | **Fail** | IMU citation also names local smoothing, restriction, Falconer, and Furstenberg sets. |
| “Needle continuous motion = Besicovitch set.” | **Fail** | Related but distinct: continuous **motion** vs. a **static set** containing all directions. |
| “Kakeya is finished in all dimensions.” | **Fail** | $$n\ge 4$$ remains open. |

---

## Mode C — reconstructed notes from flagship videos

*Reconstructed from pack captions (Quanta Kakeya; Mathologer needle; Hausdorff-dimension lectures; VI orientation). Not a substitute for the Wang–Zahl paper or IMU citation. Transcripts: `research/video-research/Wang_Harmonic_Analysis/transcripts/`.*

### C1. Needle motion vs Kakeya *sets* (Mathologer / Numberphile culture)

Popular “turn a needle 180° with small swept area” stories train continuous **motion**. The modern Kakeya **set** conjecture is about a static set that contains a unit segment in every direction. Both are about “all directions,” but they are not the same definition. Freeze which object you mean before comparing theorems.

### C2. Measure zero is compatible with full directional content

Besicovitch-type constructions (and Davies’s planar refinements with thin rectangles / tubes) show that “contains every direction” need not force positive area in the plane. That is why the deep conjecture in higher dimensions is about **dimension** (Hausdorff / Minkowski), not “must have positive volume.”

### C3. Hausdorff dimension as a scale of size (supporting lectures)

Hausdorff measure with gauge functions is a way to say “how big” when volume is zero. A set can have volume zero and still have Hausdorff dimension equal to the ambient dimension: measure zero does **not** imply “dimension zero,” and high dimension does **not** imply positive Lebesgue measure.

### C4. What 3D Kakeya asserts (Quanta / popular science of Wang–Zahl)

The three-dimensional Kakeya set conjecture forces every Kakeya set in $$\mathbb{R}^3$$ to have full dimension three (Hausdorff and Minkowski). Wang–Zahl prove this using multi-scale structure of $$\delta$$-tubes and controlling “sticky” configurations as scale changes:

| Must say | Must not say |
|----------|--------------|
| Joint work **Wang and Zahl** | “Wang alone solved Kakeya” |
| About **dimension** in 3D | “Every Kakeya set has positive volume” |
| $$n\ge 4$$ remains open | “Kakeya is finished forever” |
| IMU citation is broader than Kakeya alone | “Fields Medal = only Kakeya” |

### C5. VI orientation clips

Vietnamese popular videos can help orientation; treat automatic captions and transcription slips carefully—verify names (Wang–Zahl), year, and theorem type against arXiv/IMU before quoting.

### C6. Navigation

See `TRANSCRIPT_STATUS.md` and `*_knowledge_units.json` for time chunks. Restate claims in the lesson’s notation ($$\delta$$-tubes, Hausdorff dimension, sticky) rather than pasting caption noise.

---

## Video sources (math-video-researcher pack)

Full ranking and Mode B notes: `research/video-research/Wang_Harmonic_Analysis/`. (Popular Kakeya path already woven through this essay’s references.)

**Recommended order**

1. **Orientation ★** — Quanta, *A Once-in-a-Century Proof: The Kakeya Conjecture*: [YouTube](https://www.youtube.com/watch?v=5J3tYU_-IZI) · [article](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/).  
2. **Foundation** — CHALK Hausdorff dimension: [YouTube](https://www.youtube.com/watch?v=LJcWhcM4okQ) · MDP: [YouTube](https://www.youtube.com/watch?v=FQXbRGmAbUY).  
3. **Intuition** — Mathologer Kakeya needle (squeegee): [YouTube](https://www.youtube.com/watch?v=IM-n9c-ARHU).  
4. **VI path** — Pham Manh Tuyen: [YouTube](https://www.youtube.com/watch?v=XUkfpgFakMQ); TOÁN PRO: [YouTube](https://www.youtube.com/watch?v=pxVMKoZsVc8) (fact-check names/years against this essay).  
5. **Primary** — Wang–Zahl: [arXiv:2502.17655](https://arxiv.org/abs/2502.17655); IMU citation: [PDF](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf).

**Status reminder:** 3D Kakeya **proved**. Higher-dimensional Kakeya and sharp restriction largely **open**.

---


### Transcript & frames (flagship extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Wang_Harmonic_Analysis/transcripts/` · status: `research/video-research/Wang_Harmonic_Analysis/TRANSCRIPT_STATUS.md` · master list: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Captions are auto-downloaded (yt-dlp); treat as navigation aids, not as a substitute for the lesson text.


![Flagship video sample frame]({{ site.baseurl }}/img/video_research/flagships/kakeya_mathologer_frame01.jpg)

*Figure. Sample still from a primary flagship video (see pack for timestamps).*

## References and further reading


Full URL bibliography from video research (including secondary finds): `research/video-research/Wang_Harmonic_Analysis/references.md`.

### Complete URL list (audit)

1. https://www.youtube.com/watch?v=5J3tYU_-IZI  
2. https://www.youtube.com/watch?v=LJcWhcM4okQ  
3. https://www.youtube.com/watch?v=FQXbRGmAbUY  
4. https://www.youtube.com/watch?v=IM-n9c-ARHU  
5. https://www.youtube.com/watch?v=XUkfpgFakMQ  
6. https://www.youtube.com/watch?v=pxVMKoZsVc8  
7. https://arxiv.org/abs/2502.17655  
8. https://arxiv.org/abs/2210.09581  
9. https://arxiv.org/abs/2308.08819  
10. https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf  
11. https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/  
12. https://www.math.ubc.ca/~ilaba/kakeya.html  
13. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026  
14. https://en.wikipedia.org/wiki/Kakeya_set  
15. https://en.wikipedia.org/wiki/Restriction_problem  

### Research pack

16. Course pack: `research/video-research/Wang_Harmonic_Analysis/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. **H. Wang & J. Zahl** (2025). *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions*. [arXiv:2502.17655](https://arxiv.org/abs/2502.17655).  
2. **H. Wang & J. Zahl** (2026). Sticky Kakeya sets and the sticky Kakeya conjecture. *Journal of the American Mathematical Society*, *39*, 515–585. [arXiv:2210.09581](https://arxiv.org/abs/2210.09581).  
3. **K. Ren & H. Wang** (2023). *Furstenberg sets estimate in the plane*. [arXiv:2308.08819](https://arxiv.org/abs/2308.08819).  
4. **R. O. Davies** (1971). Some remarks on the Kakeya problem. *Proceedings of the Cambridge Philosophical Society*, *69*.  
5. **International Mathematical Union** (2026). *Fields Medal 2026 — Hong Wang* (short and long citations). [PDF](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf).  
6. **I. Łaba**. [The Kakeya problem and connections to harmonic analysis](https://www.math.ubc.ca/~ilaba/kakeya.html) — classic survey page.  
7. **T. Tao** (2014). *Stickiness, graininess, planiness…* (blog) — culture of proof strategies that shaped later work.  
8. **L. Guth**. Outline / survey notes of the Wang–Zahl argument (circulating expositions, 2025–2026).  
9. **Quanta Magazine** (2025). *‘Once in a Century’ Proof Settles Math’s Kakeya Conjecture*; (2026) coverage of Wang’s Fields Medal.  
10. **NYU / IHES / CNRS** institutional announcements of the 2026 Fields Medal.  
11. Cross-links in this course: Great Problems (Kakeya) and Explorations (smallest Kakeya set).  
12. **Popular video ★ (English, Quanta):** [A Once-in-a-Century Proof: The Kakeya Conjecture](https://www.youtube.com/watch?v=5J3tYU_-IZI) (~15 min) — tower narrative, Fefferman hinge, sticky/grains/induction; interviews Tao/Hickman/Wang/Zahl. Article: [Quanta 2025-03-14](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/). Accessed 2026-08-03.  
13. **Popular video A (English, CHALK):** [What is Hausdorff Dimension?](https://www.youtube.com/watch?v=LJcWhcM4okQ) (~13 min) — gauge functions, $$\mathcal{H}^s$$, critical $$s=\dim_H$$; deep-link `&t=19s`. Accessed 2026-08-03.  
14. **Popular video A′ (English, CHALK):** [Estimating Hausdorff Dimension / Mass Distribution Principle](https://www.youtube.com/watch?v=FQXbRGmAbUY) (~9 min) — covering upper bounds + MDP lower bounds. Accessed 2026-08-03.  
15. **Popular video B (English, Mathologer):** [The Kakeya needle problem (the squeegee approach)](https://www.youtube.com/watch?v=IM-n9c-ARHU) (~17 min) — continuous motion: parallel transfer, disk/triangle/deltoid, Perron trees, three-tree fish; deep-link `&t=632s`. Accessed 2026-08-03.  
16. **Popular video C (Vietnamese, Pham Manh Tuyen):** [Giả Thuyết Kakeya…](https://www.youtube.com/watch?v=XUkfpgFakMQ) (~15 min) — disk/deltoid → Perron → Minkowski vs Hausdorff → Davies → 3D tubes → Wang–Zahl sketch. Accessed 2026-08-03.  
17. **Popular video D (Vietnamese, TOÁN PRO):** [Phỏng Đoán Kakeya…](https://www.youtube.com/watch?v=pxVMKoZsVc8) — shorter race-history path. Accessed 2026-08-03. Correct ASR name/year errors against this essay.

*Research note.* Claims about the 2025–2026 Kakeya theorem and the Fields citation above are checked against arXiv abstracts and the official IMU PDF. Popular biographies (Quanta, institutional press) and the popular VI videos are used only for non-technical path details.

---

## Further directions

**Continue Learning path A**

1. [Ch.1 Kakeya map]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/) (review status table; optional [Mathologer](https://www.youtube.com/watch?v=IM-n9c-ARHU&t=632s) / [Pham Manh Tuyen](https://www.youtube.com/watch?v=XUkfpgFakMQ) / [TOÁN PRO](https://www.youtube.com/watch?v=pxVMKoZsVc8)).  
2. Done: Wang lecture (this page).  
3. **Next →** [Ch.7 Kakeya studio]({{ site.baseurl }}/contents/en/chapter07/07_02_Explore_Kakeya/) — timed draw/code/write blocks.  

- Mental model: treat $$\delta$$-tubes as multi-scale clustering with an inductive invariant.  
- Open targets: **higher-dimensional Kakeya** and sharp **restriction / local smoothing** (as of 2026).

## Video tham khảo

- **xem trước** — [A Once-in-a-Century Proof: The Kakeya Conjecture](https://www.youtube.com/watch?v=5J3tYU_-IZI) — Quanta Magazine, English. Watch first. “A Once-in-a-Century Proof: The Kakeya Conjecture” orients the lesson’s aim: State Kakeya’s needle problem and Besicovitch’s measure-zero construction in the plane.
- [What is Hausdorff Dimension? Intuition, Gauge Functions, and Hausdorff Measures](https://www.youtube.com/watch?v=LJcWhcM4okQ) — CHALK, English. A second pass once the main claim is in view: State Kakeya’s needle problem and Besicovitch’s measure-zero construction in the plane.
- [Methods for Estimating Hausdorff Dimension: Bounds and The Mass Distribution Principle](https://www.youtube.com/watch?v=FQXbRGmAbUY) — CHALK, English. Further depth after the first two, still tied to this lesson: State Kakeya’s needle problem and Besicovitch’s measure-zero construction in the plane.
