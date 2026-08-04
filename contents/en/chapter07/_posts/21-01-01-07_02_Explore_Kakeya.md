---
layout: post
title: "What is the smallest possible Kakeya set?"
chapter: '07'
order: 2
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Learning path A — Kakeya (step 3 of 3)**  
> **1.** [Ch.1 Kakeya map]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/)  
> **2.** [Ch.2 Wang lecture]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/)  
> **3. You are here:** Ch.7 studio (lab notebook)  
> *Prerequisite:* finish steps 1–2, or at least the Ch.1 status table + Ch.2 §§1–6.

This page is a **studio**, not a theorem dump. A Kakeya (Besicovitch) set contains a unit line segment in every direction. The classical shock is that such a set can have **Lebesgue measure zero** in the plane, yet still force **full dimension**. Your job is to **draw, compute, log, and revise** what “small” should mean—and to keep conjecture, construction, numerical observation, and theorem in separate boxes.

You will not reproduce Wang–Zahl. You will practice the research craft that makes their theorem meaningful: define size carefully, fail at minimization, and update beliefs when constructions outrun intuition.

---

## Learning objectives

After this studio you should be able to:

- State Kakeya’s needle problem and the definition of a Besicovitch (Kakeya) set in $$\mathbb{R}^n$$ in your own words.
- Distinguish **continuous needle motion** (arbitrarily small positive area for a half-turn) from a **static set** containing a unit segment in every direction (which may have measure zero).
- Explain why **measure zero** and **Hausdorff (or Minkowski) dimension** can diverge, with Davies’s theorem in the plane as the flagship example.
- Design and record at least two **experiments** (drawing, grid simulation, or rearrangement cartoon) with explicit success criteria.
- Keep a dated **research log** that separates hypothesis, result, and interpretation.
- State the 2D / 3D / higher-$$D$$ status table after consulting Ch.1–Ch.2, including Wang–Zahl (2025) for dimension 3.

**Prerequisites.** Euclidean space, basic area/volume, and the idea that fractals can have non-integer dimension. Fourier and δ-tube language from Ch.2 is optional but welcome in your log.

---

## 1. Background mathematics

### 1.1 Needle motion versus Besicovitch sets

In 1917, **Sōichi Kakeya** asked roughly: what is the smallest area of a planar region in which a unit-length needle can be **continuously reversed**—turned through every direction until it points the opposite way? Rotation about the midpoint fills a disk of radius $$1/2$$ (area $$\pi/4$$). Cleverer motions improve on the disk; a **deltoid** is a classical improvement. Still, naive intuition expects a **strictly positive** lower bound on area for continuous motion.

A **Kakeya set** (also called a **Besicovitch set**) in $$\mathbb{R}^n$$ is a set that contains a unit line segment in **every** direction. This is a **static** geometric condition: no continuous motion is required. **Abram Besicovitch** (around 1919–1928) proved that in the plane there exist such sets with **Lebesgue measure zero**. Equivalently, for every $$\varepsilon>0$$ one can build a set of area less than $$\varepsilon$$ that still houses a unit segment in every direction; a suitable limit yields measure exactly zero.

These two problems are related but not identical. Continuous-motion needle sets of **arbitrarily small positive** area exist (via Pál-type reductions and Besicovitch-type rearrangements). The measure-zero Besicovitch set is a limit object that need not support a continuous half-turn of a rigid needle without leaving the set. Log carefully which question you are exploring in each experiment.

### 1.2 Why measure can vanish while directions survive

Segment length is fixed at $$1$$. What one can do is force massive **reuse of the same points** across many directions, and pass to a fractal limit of thinner neighborhoods. A length-$$1$$, width-$$\delta$$ rectangle has area about $$\delta$$. As $$\delta\to 0$$ that area vanishes—but there are **infinitely many** directions. Besicovitch’s art is systematic reuse of space through iterated cutting and sliding.

A modern pedagogical picture is the **iterated Venetian-blind** construction: nearly parallel thin strips are tilted, cut, and restacked so directional information survives while total area collapses. Another cartoon is the **Perron tree**: thin triangles overlapped and rearranged so many directions share almost the same ink. A classical “fish” of three trees supports a half-turn story for continuous motion.

**Key geometric slogan.** Overlap is not a bug; it is the resource.

### 1.3 Dimension is not measure

**Roy Davies (1971)** proved that every Kakeya set in the plane has **Hausdorff dimension 2**:

$$
\lvert E\rvert = 0 \quad\text{is possible, yet}\quad \dim_H(E) = 2.
$$

First great paradox of Kakeya theory: **empty of area, full of dimension**. **Minkowski (box-counting) dimension** is often easiest to estimate experimentally: cover with boxes of side $$r$$ and read the scaling of the box count as $$r\to 0$$. Hausdorff dimension is a refined measure-theoretic cousin. For many “nice” sets they agree; Kakeya theory studies both carefully.

> **Volume zero does not imply dimension less than the ambient dimension.**  
> A set in $$\mathbb{R}^3$$ can have Lebesgue measure zero and still have Minkowski dimension 3.

### 1.4 The Kakeya set conjecture and status

**Conjecture (slogan).** Every Kakeya set in $$\mathbb{R}^n$$ has Hausdorff (and Minkowski) dimension $$n$$.

| Dimension | Status (studio-level) |
|-----------|------------------------|
| $$n=2$$ | True (Davies and related) |
| $$n=3$$ | True — **Wang–Zahl (2025)** |
| $$n\ge 4$$ | Open in full strength; partial lower bounds exist |

Wang–Zahl is the flagship of Ch.2’s harmonic analysis path: multiscale **δ-tube** estimates, clustering, planiness/graininess, and decoupling force extreme directional configurations to be high-dimensional. Your studio goal is not to prove this; it is to **feel** why measure and dimension diverge, and to log the status accurately.

![Unit segments pointing in many directions]({{ site.baseurl }}/img/chapter_img/kakeya_needle_directions.svg)

*Figure. A Kakeya set must contain a unit segment for every direction—the containing set need not look “full.”*

---

## 2. Conjecture versus proof versus experiment

Keep four labels in every log entry and report:

| Label | Meaning | Example |
|-------|---------|---------|
| **Theorem** | Published proof, cited | Davies: planar Kakeya sets have dim 2 |
| **Conjecture** | Open claim, named | Full Kakeya conjecture for $$n\ge 4$$ |
| **Construction** | Explicit or algorithmic object | Grid simulation covering 36 directions |
| **Observation** | What *you* saw in a finite experiment | Covered cells grew sublinearly in directions |

Success for this studio is **not** “prove Wang–Zahl.” Success is producing artifacts and a log that a peer could audit.

**Success criteria (choose and state explicitly in your proposal):**

1. Produce at least one drawing or program that hosts **at least 12** directions with measured “ink” (area or grid cells).  
2. Write two definitions of “small” (v1 before reading, v2 after Besicovitch/Davies).  
3. State the 2/3/≥4 status table correctly in your own words.  
4. Log one **failed intuition** with a corrected belief.  
5. Write one sentence linking tubes or Fourier restriction (even if fuzzy) to why dimension matters for analysis.

---

## 3. Research log standards

Each entry should include:

- **Date**  
- **Intent** (what you tried and why)  
- **Action** (drawing description, code summary, source consulted)  
- **Result** (numbers, sketch description, quote of a theorem you checked)  
- **Label** (theorem / conjecture / construction / observation)  
- **Interpretation** (what changed in your beliefs)  
- **Next step**

**Failed attempts count.** “Tried random segments and covered almost the whole square; switched to forced reuse near the origin” is excellent log material.

**AI policy reminder.** Code and search assistance allowed with disclosure; the log of *your* experiments, drawings, and interpretations must be yours.

---

## 4. Experiments

Do **at least two** of A–E. Time boxes are suggestions, not laws.

### Experiment A — Draw many directions (20–40 min)

On paper or a tablet, place unit-length segments in **8–12** directions and minimize the inked region. Can you reuse the same ink for two nearly parallel directions?

**Hypothesis before drawing:** “Nearly parallel directions need almost disjoint strips.”  
**After:** revise the hypothesis. Optional cue: sketch a **Perron tree** (thin triangles overlapped) and a three-tree **fish** for a half-turn (see media linked in Ch.1).

**Success criterion:** artifact + measured rough area (grid squares or pixel count) + written revision of “small.”

### Experiment B — Continuous motion vs static set (15–25 min)

Write a half-page dialogue between two characters:

- *Motion:* “I need a path of the needle through all angles.”  
- *Static:* “I only need the union of positions, not a continuous path inside the set.”

Then answer: is “smallest area under continuous half-turn” the same problem as “Besicovitch set of minimal dimension”? Cite one sentence from Ch.1 or Ch.2 that supports your answer.

**Success criterion:** clear separation of the two problems in a table of your own design.

### Experiment C — Grid simulation (30–90 min)

On an $$M\times M$$ grid, place unit-length discrete segments in $$K$$ directions (sample angles $$k\pi/K$$). Count covered cells as a function of $$K$$. Try:

1. segments through a fixed center;  
2. segments free to translate (greedy placement to maximize overlap);  
3. random placements for a baseline.

Plot covered cells vs $$K$$. Does reuse beat the random baseline?

**Success criterion:** plot or table for at least two strategies; one sentence on scaling.

### Experiment D — Dimension news desk (20–30 min)

Using only the Ch.1 status table and Ch.2 slogans (not a press release alone), write:

1. One sentence on Besicovitch measure zero.  
2. One sentence on Davies dimension 2.  
3. One sentence on Wang–Zahl dimension 3.  
4. One sentence on what remains open.

Optional media (log what you watched and one claim you verified against the course):

- **2025 story (EN, ~15 min):** [Quanta Kakeya](https://www.youtube.com/watch?v=5J3tYU_-IZI) — list the four tower levels (Kakeya → restriction → Bochner–Riesz → local smoothing) and one sentence on “grains.”  
- **Hausdorff formal (EN):** [CHALK part 1](https://www.youtube.com/watch?v=LJcWhcM4okQ&t=19s) (~13 min); [part 2 / MDP](https://www.youtube.com/watch?v=FQXbRGmAbUY) (~9 min).  
- **Continuous construction (EN):** [Mathologer squeegee](https://www.youtube.com/watch?v=IM-n9c-ARHU&t=632s) from **t≈10:32**.  
- Geometry-first (VI, ~15 min): [Pham Manh Tuyen](https://www.youtube.com/watch?v=XUkfpgFakMQ).  
- Race-history (VI, ~9 min): [TOÁN PRO](https://www.youtube.com/watch?v=pxVMKoZsVc8) from **t≈3:38**.

**Success criterion:** four sentences + one media note with a *course-checked* correction if captions err.

### Experiment E — δ-tube intuition (stretch, 30–60 min)

Imagine tubes of length $$1$$ and radius $$\delta$$. Rough volume of one tube is about $$\delta^{n-1}$$. If $$N$$ tubes in different directions overlap heavily, the union can be much smaller than $$N\delta^{n-1}$$. Write a back-of-envelope argument: if the union has volume $$\ll N\delta^{n-1}$$, what does that force about shared geometry? Connect (loosely is fine) to why harmonic analysis cares about Kakeya.

**Success criterion:** one page of dimensional analysis + one open question.

---

## 5. Common confusions

1. **“Measure zero means the set is tiny in every sense.”** — Dimension can still be full.  
2. **“Wang–Zahl solved Kakeya in all dimensions.”** — Dimension 3 is the celebrated recent case; higher dimensions remain open in full strength.  
3. **“Needle motion = Besicovitch set.”** — Related, not identical; continuous motion needs positive-area neighborhoods along a path.  
4. **“My drawing has small area, so dimension is small.”** — Finite drawings estimate area for a finite set of directions; dimension is an asymptotic, continuum-scale notion.  
5. **“Exploration means no standards.”** — Studio honesty standards are stricter than a calculation homework: labels, logs, and limits matter.

---

## 6. Exercises

1. Compute the area of a unit disk of radius $$1/2$$ and of a deltoid (look up the classical formula). Why is the deltoid still “large” compared to Besicovitch’s arbitrarily small sets?  
2. Explain in three sentences why a single unit segment has Hausdorff dimension 1, while a Kakeya set must be “directionally full.”  
3. On a $$20\times 20$$ grid, place segments in the four axis and diagonal directions through the center; count cells. Then allow translates to maximize shared cells; compare.  
4. Write a falsifiable hypothesis about your grid experiment (e.g., “greedy overlap reduces covered cells by at least 30% for $$K=16$$”). Run it; report alive or dead.  
5. Draft a 150–200 word studio proposal: question, definition of small, methods, success criteria, risks.

---

## 7. Checkpoint rubric

| Done? | Item |
|-------|------|
| ☐ | Drawing or code artifact with ≥12 directions |
| ☐ | Definition of “small” (v1 and v2) |
| ☐ | Status table 2 / 3 / ≥4 recalled correctly |
| ☐ | Log with at least three dated entries |
| ☐ | One failed intuition documented |
| ☐ | One link sentence to tubes / Fourier (even fuzzy) |
| ☐ | Open question for next week |

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/explore-kakeya/`.

**From the research pack (must-know slogans)**

- **Besicovitch set / Kakeya set:** unit segment in every direction; measure zero possible in the plane.
- **Davies (1971):** planar Kakeya sets have Hausdorff dimension 2 (measure zero ≠ dimension < 2).
- **Wang–Zahl (2025):** Kakeya set conjecture in dimension 3 — [arXiv:2502.17655](https://arxiv.org/abs/2502.17655).
- **Continuous needle motion** (arbitrarily small positive area) ≠ static measure-zero Besicovitch set.
- Studio moral: minimize with a frozen definition of “small”; log failures; never claim to have reproduced Wang–Zahl.

**Recommended order**

1. **Orientation** — Quanta — Once-in-a-Century Proof: Kakeya: [https://www.youtube.com/watch?v=5J3tYU_-IZI](https://www.youtube.com/watch?v=5J3tYU_-IZI).  
2. **Intuition** — Mathologer — Kakeya needle (squeegee): [https://www.youtube.com/watch?v=IM-n9c-ARHU](https://www.youtube.com/watch?v=IM-n9c-ARHU).  
3. **Foundation** — CHALK — What is Hausdorff Dimension?: [https://www.youtube.com/watch?v=LJcWhcM4okQ](https://www.youtube.com/watch?v=LJcWhcM4okQ).  
4. **Foundation** — CHALK — Estimating Hausdorff dim / MDP: [https://www.youtube.com/watch?v=FQXbRGmAbUY](https://www.youtube.com/watch?v=FQXbRGmAbUY).  
5. **Orientation** — Pham Manh Tuyen — Giả thuyết Kakeya (VI): [https://www.youtube.com/watch?v=XUkfpgFakMQ](https://www.youtube.com/watch?v=XUkfpgFakMQ).  
6. **Orientation** — TOÁN PRO — Phỏng đoán Kakeya (VI): [https://www.youtube.com/watch?v=pxVMKoZsVc8](https://www.youtube.com/watch?v=pxVMKoZsVc8).  

**Official / primary written hubs**

- Wang–Zahl Kakeya 3D (arXiv): https://arxiv.org/abs/2502.17655  
- Wang–Zahl sticky Kakeya (arXiv): https://arxiv.org/abs/2210.09581  

Complete URL bibliography: `research/video-research/explore-kakeya/references.md`.

## 8. References and course links


### Video research pack (all URLs)

Complete list: `research/video-research/explore-kakeya/references.md`.

1. Quanta — Once-in-a-Century Proof: Kakeya — https://www.youtube.com/watch?v=5J3tYU_-IZI  
2. Mathologer — Kakeya needle (squeegee) — https://www.youtube.com/watch?v=IM-n9c-ARHU  
3. CHALK — What is Hausdorff Dimension? — https://www.youtube.com/watch?v=LJcWhcM4okQ  
4. CHALK — Estimating Hausdorff dim / MDP — https://www.youtube.com/watch?v=FQXbRGmAbUY  
5. Pham Manh Tuyen — Giả thuyết Kakeya (VI) — https://www.youtube.com/watch?v=XUkfpgFakMQ  
6. TOÁN PRO — Phỏng đoán Kakeya (VI) — https://www.youtube.com/watch?v=pxVMKoZsVc8  
7. Wang–Zahl Kakeya 3D (arXiv) — https://arxiv.org/abs/2502.17655  
8. Wang–Zahl sticky Kakeya (arXiv) — https://arxiv.org/abs/2210.09581  
9. Quanta article Kakeya 2025 — https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/  
10. Wikipedia — Kakeya set — https://en.wikipedia.org/wiki/Kakeya_set  
11. Research pack folder: `research/video-research/explore-kakeya/`.

1. Course: [Ch.1 Kakeya map]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/), [Ch.2 Wang]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/).  
2. Besicovitch’s classical constructions; Davies on planar dimension (standard harmonic-analysis references).  
3. Wang–Zahl, arXiv:2502.17655 (existence and statement level—do not claim to have read all 100+ pages unless you did).  
4. Nearby studio: [sphere packing]({{ site.baseurl }}/contents/en/chapter07/07_03_Explore_Sphere_Packing/).

---

## Further directions

**Path A complete** when the checkpoint rubric is filled and linked to Ch.1/Ch.2 claims. Revisit Wang exercises if theory felt thin. Optional contrast: [Four Color path B]({{ site.baseurl }}/contents/en/chapter01/01_09_Four_Color_Theorem/) (solved, computer-assisted culture versus open analytic culture).

### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/explore-kakeya/transcripts/` · status: `research/video-research/explore-kakeya/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/explore-kakeya_5J3tYU_-IZI_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

