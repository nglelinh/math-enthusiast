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

**Hong Wang** (NYU Courant; permanent professor at IHES) received the **Fields Medal 2026** at ICM Philadelphia. The IMU short citation states:

> For her work in harmonic analysis and geometric measure theory, including applications of multiscale and decoupling techniques to the local smoothing conjecture for the planar wave equation, and major advances in Fourier restriction, Falconer distance sets, Furstenberg sets in the plane, and the Kakeya problem in three dimensions.  
> — [IMU, Fields Medal 2026 citation](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf)

She is the **third woman** to receive a Fields Medal (after Maryam Mirzakhani, 2014, and Maryna Viazovska, 2022). The flagship geometric achievement most often highlighted in public accounts is the **three-dimensional Kakeya set conjecture**, proved jointly with **Joshua Zahl** (arXiv:2502.17655, 2025). The medal, however, recognizes a **body of work**, not a single paper.

This essay follows:

**Needle problem → Besicovitch sets → measure vs dimension → δ-tubes → Wang–Zahl → harmonic analysis → Fields portfolio.**

The goal is not to reproduce a 127-page proof, but to understand **what was asked**, **why it resisted a century of work**, and **what mathematics sits underneath**.

How small can a set in $$\mathbb{R}^n$$ be while still containing a unit segment in every direction? Separately: how do multiscale directional configurations control Fourier restriction, distance sets, Furstenberg sets, and local smoothing for waves?

Modern approaches recast directional geometry as estimates for families of thin **δ-tubes**, and use multiscale structural analysis (clustering, graininess, planiness, decoupling) so that extreme overlap is forced to produce exploitable geometry rather than pure chaos. With Zahl: volume estimates for unions of tubes under convex-containment hypotheses imply that every Kakeya set in $$\mathbb{R}^3$$ has Hausdorff and Minkowski dimension 3. More broadly (IMU long citation): local smoothing for the planar wave equation with Guth–Zhang; Falconer-type distance results with Guth–Iosevich–Ou; Furstenberg sets in the plane with Ren; and related restriction advances. Fields Medal 2026.

---

## Learning objectives

After this lecture you should be able to:

- State Kakeya’s needle problem and Besicovitch’s measure-zero construction in the plane.
- Explain why **Lebesgue measure zero** does not force **Hausdorff (or Minkowski) dimension** less than the ambient dimension.
- Formulate the **Kakeya set conjecture** in $$\mathbb{R}^n$$ and state what is known for $$n=2$$ and $$n=3$$.
- Describe the **δ-tube** picture and why heavy overlap is the real difficulty.
- Place **Wang–Zahl (2025)** and **Wang’s Fields Medal (2026)** in a longer historical line.
- Summarize, with collaborators named, Wang’s contributions beyond Kakeya (local smoothing, Falconer, Furstenberg, restriction).
- Avoid common confusions (needle motion vs Besicovitch set; joint credit; volume vs dimension).

**Prerequisites.** Euclidean space, basic measure intuition, and the idea that fractals can have non-integer dimension. Fourier remarks stay conceptual.

---

## 1. The needle problem: simple to state, strange to solve

In 1917, **Sōichi Kakeya** asked (roughly): what is the smallest area of a planar region in which a unit-length needle can be continuously reversed—turned through every direction until it points the opposite way?

Naive intuition suggests a substantial region. Rotation about the midpoint fills a disk of radius $$1/2$$ (area $$\pi/4$$). Cleverer motions improve on the disk; a **deltoid** is a classical improvement. Still, one expects a **positive** lower bound on area.

Besicovitch showed something far stronger than “the area can be a bit smaller.”

![Unit segments pointing in many directions]({{ site.baseurl }}/img/chapter_img/kakeya_needle_directions.svg)

*Figure. A Kakeya set must contain a unit segment for every direction—the containing set need not look “full.”*

---

## 2. Besicovitch sets: every direction, measure zero

A **Kakeya set** (also called a **Besicovitch set**) in $$\mathbb{R}^n$$ is a set that contains a unit line segment in **every** direction.

**Abram Besicovitch** (around 1919–1928) proved that in the plane there exist such sets with **Lebesgue measure zero**. Equivalently: for every $$\varepsilon>0$$ one can build a set of area less than $$\varepsilon$$ that still houses a unit segment in every direction; a suitable limit yields measure exactly zero.

Historically, Besicovitch’s first motivation concerned **iterated integrals** in Riemann integration; the construction also solved Kakeya’s problem (via related needle sets of arbitrarily small positive area and Pál-type reductions). Calling these objects **Besicovitch sets** is historically fair.

### How can area be zero?

Segment length is fixed at $$1$$. What one can do is force massive **reuse of the same points** across many directions, and pass to a fractal limit of thinner neighborhoods.

![Triangle cut and shift]({{ site.baseurl }}/img/chapter_img/besicovitch_triangle_overlap.svg)

*Figure. Classical cartoon: cut an equilateral triangle, shift halves to increase overlap, iterate.*

A modern pedagogical picture is the **iterated Venetian-blind** construction: nearly parallel thin strips are tilted, cut, and restacked so directional information survives while total area collapses.

![Venetian blind rearrangement]({{ site.baseurl }}/img/chapter_img/venetian_blinds_kakeya.svg)

*Figure. Schematic Venetian-blind rearrangement (not a literal full construction).*

**Key insight.** A length-$$1$$, width-$$\delta$$ rectangle has area about $$\delta$$. As $$\delta\to 0$$ that area vanishes—but there are **infinitely many** directions. Besicovitch’s art is systematic **reuse of space** through iterated cutting and sliding.

### Davies (1971): dimension is still 2

Measure zero does **not** mean the set is one-dimensional. **Roy Davies** proved that every Kakeya set in the plane has **Hausdorff dimension 2**:

$$
\lvert E\rvert = 0 \quad\text{is possible, yet}\quad \dim_H(E) = 2.
$$

First great paradox of Kakeya theory: **empty of area, full of dimension**.

---

## 3. Dimension is not only 1, 2, 3

Ordinary geometry assigns integer dimensions to lines, planes, and space. Fractals allow intermediate values (e.g. $$1.5$$ or $$2.7$$).

**Minkowski (box-counting) dimension** is often easiest: cover with boxes of side $$r$$ and read the scaling exponent of the box count as $$r\to 0$$.

**Hausdorff dimension** is a refined measure-theoretic cousin. For many “nice” sets they agree; Kakeya theory studies both.

> **Volume zero does not imply dimension less than 3.**  
> A set in $$\mathbb{R}^3$$ can have Lebesgue measure zero and still have Minkowski dimension 3.

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

Besicovitch already knew that **measure-zero** Kakeya sets exist in higher dimensions. The conjecture says they still cannot be “too thin” in the fractal sense: they fill the ambient dimension.

---

## 5. Why three dimensions is hard: δ-tubes

Replace each unit segment by a thin **tube** of length about $$1$$ and radius $$\delta$$ (a $$\delta$$-**tube**). A Kakeya set at scale $$\delta$$ looks like a large family of such tubes, one for each direction (or a fine net of directions).

![δ-tubes with heavy overlap]({{ site.baseurl }}/img/chapter_img/kakeya_delta_tubes.svg)

*Figure. Many δ-tubes; heavy overlap is where the geometry becomes subtle.*

If tubes barely overlap, the volume of the union in $$\mathbb{R}^3$$ is roughly on the order of $$N\cdot \delta^{2}$$ (each tube has volume $$\sim\delta^{2}$$). The difficulty is **massive overlap**:

$$
\bigl\lvert \bigcup_i T_i\bigr\rvert \;\ll\; \sum_i \lvert T_i\rvert.
$$

> **How small can the union of many multi-directional tubes be?**

### Spaghetti intuition

Imagine millions of extremely thin strands, each forced into a different direction, packed into the smallest possible region.

- **Dispersed.** The strands fill a large region; dimension is “obviously” large.  
- **Clustered.** They form thick bundles. Extreme clustering is not pure chaos: near-parallel families, concentration near curves or surfaces, and **regulus-like** ruled configurations appear.

Wang–Zahl-type analysis turns the slogan into theorems: **extreme overlap forces geometric structure** that can be exploited at other scales.

### Multi-scale graininess

At coarse scales a configuration may look like a solid blob; zoom in and thin tubes appear; zoom further and new grain structure appears. The problem is inherently multi-scale:

$$
1 \;\to\; \delta \;\to\; \delta^{2} \;\to\; \cdots
$$

In three dimensions, tubes can intersect transversely, be nearly parallel, concentrate along curves or surfaces, or form regulus-like configurations. Two-dimensional methods do not simply “tensor up.” Specialist expositions (e.g. Larry Guth’s outline of the Wang–Zahl argument) emphasize that the proof is long because it tracks structure across many scales at once.

---

## 6. What Wang and Zahl proved

**Theorem (Wang–Zahl, 2025).**  
Every Kakeya set $$K\subset\mathbb{R}^3$$ satisfies

$$
\dim_H(K) = \dim_M(K) = 3.
$$

Primary source: *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions* ([arXiv:2502.17655](https://arxiv.org/abs/2502.17655); 127 pages). The abstract states the technical engine clearly: for families of $$\delta$$-tubes in $$\mathbb{R}^3$$ such that not too many tubes lie in a common convex set $$V$$, the union has **almost maximal volume**; dimension 3 for Kakeya sets follows as a consequence.

They do **not** claim positive volume for 3D Kakeya sets—Besicovitch-type zero volume remains possible. The theorem is deeper:

> You may have **volume zero**, but you cannot host all directions while living in a fractal of dimension strictly less than 3.

### Strategy in outline (not the proof)

1. Recast Kakeya as estimates for families of thin tubes.  
2. Analyze intersections and clustering.  
3. If overlap is extreme, prove **geometric structure** must appear (stickiness, graininess, planiness—themes already in the Katz–Tao program).  
4. Exploit that structure to force the configuration to **expand** at another scale (**self-improvement**).  
5. Run an **induction on scales**.  
6. Conclude that dimension cannot stay below 3.

**Self-improvement slogan.**

$$
\text{bad configuration at one scale}
\;\Longrightarrow\;
\text{hidden structure}
\;\Longrightarrow\;
\text{better configuration at another scale}.
$$

Earlier joint work of Wang and Zahl on **sticky Kakeya** sets was a major stepping stone. Sticky sets exhibit approximate multi-scale self-similarity and had already played a role in Katz–Łaba–Tao (1999). Wang–Zahl proved the sticky Kakeya conjecture in three dimensions ([arXiv:2210.09581](https://arxiv.org/abs/2210.09581); *J. Amer. Math. Soc.* **39** (2026), 515–585).

**Credit.** This is **joint work**. The result crowns a century-long program involving Besicovitch, Davies, Wolff, Bourgain, Katz, Tao, Guth, Zahl, Wang, and many others. It is a summit of a research mountain, not a theorem from empty space.

![Historical timeline]({{ site.baseurl }}/img/chapter_img/kakeya_history_timeline.svg)

*Figure. Selected milestones from Kakeya (1917) to Wang’s Fields Medal (2026).*

---

## 7. Why harmonic analysis cares

Kakeya sits at the junction of:

- **geometric measure theory** (size of wild sets),
- **harmonic analysis** (Fourier restriction, maximal functions, oscillatory integrals),
- **PDE** (local smoothing for the wave equation, concentration of solutions).

The **Fourier transform** pairs $$f(x)$$ with its frequency portrait $$\hat f(\xi)$$. When one studies waves of similar wavelength but many directions—or restriction of the Fourier transform to curved surfaces—energy is often organized into **wave packets** living on long thin tubes. How those tubes may overlap governs whether energy can **concentrate** or must **spread**.

![From Kakeya to harmonic analysis]({{ site.baseurl }}/img/chapter_img/kakeya_to_harmonic_analysis.svg)

*Figure. Conceptual chain from tube geometry to Fourier and PDE themes.*

Related open towers (restriction, Bochner–Riesz, local smoothing in higher dimensions or sharper quantitative forms) still depend on Kakeya-type geometry. Solving Kakeya in 3D reshapes the landscape; it does not end the story.

**Popular hierarchy (Quanta).** A public map used widely after the 2025 announcement (and excellent for students) is:

**Kakeya** → **restriction** → **Bochner–Riesz** → **local smoothing** (wave PDE).

Historically, **Fefferman**’s work in the 1970s already made Kakeya geometry a harmonic-analysis engine, not a puzzle. The Wang–Zahl theorem is celebrated as a once-in-a-generation base-case breakthrough for that tower; it does **not** by itself resolve every layer above. See [Quanta video](https://www.youtube.com/watch?v=5J3tYU_-IZI) and [Quanta article](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/).

**Slogan of the 2025 strategy (from public lectures / Quanta).** Sticky case first; then **grains** (forced clustering of tubes) and **induction on scales** that raise the lower bound on dimension without catastrophic multiscale loss (the “Chinese whispers” failure mode). Full details: arXiv:2502.17655 and § earlier in this essay.

---

## 8. Beyond Kakeya: the Fields portfolio (IMU long citation)

The medal citation is deliberately broader than one theorem. A compact research map:

| Theme | Collaborators (selected) | What was advanced |
|-------|--------------------------|-------------------|
| **Local smoothing** (planar wave equation) | Larry Guth, Ruixiang Zhang | Multiscale + decoupling methods resolving the local smoothing conjecture in the plane (IMU long citation) |
| **Falconer distance sets** | Guth, Alex Iosevich, Yumeng Ou | Major results linking Hausdorff dimension to distance distributions |
| **Furstenberg sets** (plane) | Kevin Ren | Resolution of the 2D Furstenberg set conjecture ([arXiv:2308.08819](https://arxiv.org/abs/2308.08819)): a $$(s,t)$$-Furstenberg set has dimension at least $$\min\bigl(s+t,\frac{3s+t}{2},s+1\bigr)$$ |
| **Fourier restriction** | various | Structural advances feeding the restriction tower |
| **Kakeya in 3D** | Joshua Zahl | Sticky case (JAMS 2026) and full Kakeya dimension 3 (arXiv:2502.17655) |

**WHY.** Directional fractal configurations control how energy and measure can concentrate.  
**HOW.** Multiscale analysis, decoupling, and incidence/tube geometry.  
**WHAT.** A sequence of sharp geometric measure / harmonic analysis theorems, of which Kakeya 3D is the most public flagship.

### Path (brief biography)

Born in Guilin, China; studies at Peking University and École Polytechnique; PhD at MIT with **Larry Guth**; positions including IAS and UCLA, then NYU Courant and IHES. A cascade of prizes (Salem, Ostrowski, Clay Research Award, New Horizons, …) preceded the Fields Medal at **ICM 2026 (Philadelphia)**.

### Accuracy checklist

- The 3D Kakeya theorem is **joint** with **Joshua Zahl**.  
- The Fields Medal recognizes Wang’s **body of work**; Kakeya 3D is the best-known piece, not the whole citation.  
- She is the **third woman** Fields medalist.  
- **Higher-dimensional Kakeya** ($$n\ge 4$$) and several sharp analytic conjectures remain open as of 2026.

---

## 9. The deepest paradox, restated

$$
\operatorname{Vol}(K)=0
\quad\text{is possible,}\quad
\dim(K)=3
\quad\text{is mandatory in }\mathbb{R}^3.
$$

You cannot pack unit segments in all three-dimensional directions into a genuinely lower-dimensional fractal. That is the content of the 3D Kakeya set conjecture—and of Wang–Zahl’s theorem.

---

## Common misconceptions (fact-check)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Wang alone solved Kakeya in 3D.” | **Fail** | Joint with Joshua Zahl. |
| “Kakeya sets in 3D must have positive volume.” | **Fail** | Measure zero remains possible; the theorem is about **dimension**. |
| “The Fields Medal is only for Kakeya.” | **Fail** | IMU citation also names local smoothing, restriction, Falconer, Furstenberg. |
| “Needle continuous motion = Besicovitch set.” | **Fail** | Related but distinct: continuous **motion** vs a **static set** containing all directions. |
| “Kakeya is finished in all dimensions.” | **Fail** | $$n\ge 4$$ is open. |

---

## Mode C — reconstructed notes from flagship videos

*Reconstructed from pack captions (Quanta Kakeya; Mathologer needle; Hausdorff-dimension lectures; VI orientation). Not a substitute for the Wang–Zahl paper or IMU citation. Transcripts: `research/video-research/Wang_Harmonic_Analysis/transcripts/`.*

### C1. Needle motion vs Kakeya *sets* (Mathologer / Numberphile culture)

Popular “turn a needle 180° with small swept area” stories train continuous **motion**. The modern Kakeya **set** conjecture is about a static set that contains a unit segment in every direction. Both are about “all directions,” but they are not the same definition. Seminar rule: freeze which object you mean before comparing theorems.

### C2. Measure zero is compatible with full directional content

Besicovitch-type constructions (and Davies’s planar refinements with thin rectangles / tubes) show that “contains every direction” need not force positive area in the plane. That is why the deep conjecture in higher dimensions is about **dimension** (Hausdorff / Minkowski), not “must have positive volume.”

### C3. Hausdorff dimension as a scale of size (supporting lectures)

Hausdorff measure with gauge functions is a way to say “how big” when volume is zero. A set can have volume zero and still have Hausdorff dimension equal to the ambient dimension. **LO2 target:** measure zero does **not** imply “dimension zero,” and high dimension does **not** imply positive Lebesgue measure.

### C4. What 3D Kakeya asserts (Quanta / popular science of Wang–Zahl)

The three-dimensional Kakeya set conjecture (in the form popular expositions state) forces every Kakeya set in $$\mathbb{R}^3$$ to have full dimension three (Hausdorff and Minkowski, in the sense of the theorem). Wang–Zahl prove this; popular narratives emphasize multi-scale structure of δ-tubes and controlling “sticky” configurations as scale changes. For grades:

| Must say | Must not say |
|----------|--------------|
| Joint work **Wang and Zahl** | “Wang alone solved Kakeya” |
| About **dimension** in 3D | “Every Kakeya set has positive volume” |
| $$n\ge 4$$ remains open | “Kakeya is finished forever” |
| IMU citation is broader than Kakeya alone | “Fields Medal = only Kakeya” |

### C5. VI orientation clips

Vietnamese popular videos can help orientation; treat automatic captions and “Fields/Fibonacci” type slips as **LO6 practice**—verify names (Wang–Zahl), year, and theorem type against arXiv/IMU before quoting.

### C6. Navigation

See `TRANSCRIPT_STATUS.md` and `*_knowledge_units.json` for time chunks. Graded writing must restate claims in the lesson’s notation (δ-tubes, Hausdorff dimension, sticky), not paste caption noise.

---

## Challenges and extensions

1. Distinguish continuous **needle motion** from a **static Besicovitch set**.  
2. What lower bounds hold for $$\lvert\bigcup T_i\rvert$$ in terms of $$\delta$$ and the number of directions?  
3. Why might the **sticky** case be a natural enemy of the conjecture?  
4. Rephrase Kakeya as a statement about possible concentration of wave packets.  
5. List two geometric difficulties that worsen in dimension 4.

---

## Exercises

1. **Warm-up.** Why is a line segment in the plane area zero but not a Kakeya set?  
2. **Definitions.** Define: Kakeya set in $$\mathbb{R}^n$$; Hausdorff dimension (informal OK); δ-tube.  
3. **Davies vs Besicovitch.** Why is Davies a **refinement** of Besicovitch rather than a contradiction?  
4. **Volume heuristic.** If $$N$$ tubes of volume $$c\delta^{2}$$ are pairwise disjoint, estimate the union. What changes if every pair intersects in volume $$\approx\delta^{3}$$?  
5. **Synthesis.** Draw  
   `Kakeya → tubes → multi-scale structure → Fourier / PDE`  
   and annotate each arrow with one sentence.  
6. **Research literacy.** Open [arXiv:2502.17655](https://arxiv.org/abs/2502.17655); from abstract and introduction only, quote the main volume statement and list three prior directions the authors build on.  
7. **Citation literacy.** Compare the [IMU short citation](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf) with a popular-science summary; which collaborators appear only in the official text?

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

- Mental model: treat δ-tubes as multi-scale clustering with an inductive invariant.  
- Open targets: **higher-dimensional Kakeya** and sharp **restriction / local smoothing** (as of 2026).
