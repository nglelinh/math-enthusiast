---
layout: post
title: "How can we pack spheres most efficiently?"
chapter: '07'
order: 3
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Context path — packing**  
> **Deep read:** [Ch.2 Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/)  
> **You are here:** Ch.7 packing studio (experiments + log)  
> *Optional:* kissing numbers, lattice vs nonlattice, high-dimensional weirdness.

This studio asks a deceptively physical question: what is the densest way to pack equal non-overlapping balls in $$\mathbb{R}^n$$? In the plane you can settle the dispute with coins. In three dimensions Kepler’s conjecture waited centuries. In dimensions 8 and 24, modular forms and Fourier analysis decide optimality. Most dimensions remain open.

Your goal is not to construct Viazovska’s magic function. Your goal is to **define density carefully**, **measure real packings**, **compare candidates**, and practice the difference between a **sharp theorem** in special dimensions and a **heuristic** or **numerical upper/lower bound** elsewhere.

---

## Learning objectives

After this studio you should be able to:

- Define packing density as a limit of covered volume fraction, and compute it exactly for the square and hexagonal lattice packings in 2D.
- Explain the kissing number problem and state classical values in dimensions 2 and 3 (and the qualitative jump in higher dimensions).
- Distinguish **lattice packings** from general packings, and say why nonlattice configurations might win in some dimensions.
- Summarize the status table: hexagonal (2D), Kepler/Hales (3D), $$E_8$$ (8), Leech (24), generic $$n$$ open.
- Design at least two experiments with success criteria and log them with conjecture/observation labels.
- State the Cohn–Elkies idea at slogan level: upper bounds via special radial functions and their Fourier transforms.

**Prerequisites.** Area and volume of balls; vectors in $$\mathbb{R}^2$$ and $$\mathbb{R}^3$$; the idea of a lattice as a discrete subgroup spanning space.

---

## 1. Background mathematics

### 1.1 Density

Fix dimension $$n$$ and pack non-overlapping closed balls of equal radius in $$\mathbb{R}^n$$. One standard definition of **density** is

$$
\delta=\limsup_{R\to\infty}\frac{\text{volume of balls inside }B(0,R)}{\operatorname{Vol} B(0,R)}.
$$

For a **lattice packing** with centers at lattice points $$\Lambda$$ and minimal nonzero distance $$2r$$ (so balls of radius $$r$$ just touch), density reduces to the volume of one ball divided by the volume of a fundamental cell:

$$
\delta(\Lambda)=\frac{\operatorname{Vol}(B(0,r))}{\operatorname{Vol}(\mathbb{R}^n/\Lambda)}.
$$

**Question.** What is $$\delta_n$$, the supremum of densities over all packings in dimension $$n$$? Which configurations attain it?

### 1.2 Two dimensions: square versus hexagon

Place coins on a table.

- **Square lattice.** Centers at $$(2r\,i,\,2r\,j)$$. Each ball occupies a square of side $$2r$$, so

$$
\delta_{\square}=\frac{\pi r^2}{4r^2}=\frac{\pi}{4}\approx 0.785.
$$

- **Hexagonal lattice.** Each center has six neighbors at distance $$2r$$. A standard fundamental cell yields

$$
\delta_{\mathrm{hex}}=\frac{\pi}{2\sqrt{3}}\approx 0.907.
$$

Hexagonal packing is optimal in the plane (classical). Your first experiment should *feel* this gap before you quote the theorem.

### 1.3 Three dimensions and kissing

**Kepler’s conjecture** asserts that no packing of equal balls in $$\mathbb{R}^3$$ exceeds the face-centered cubic (FCC) / hexagonal close packing (HCP) density

$$
\delta_{\mathrm{FCC}}=\frac{\pi}{3\sqrt{2}}\approx 0.74048.
$$

**Thomas Hales** proved this (with substantial computer assistance); the result is now also formalized in a proof assistant. The **kissing number** in 3D is 12: a central ball can touch at most twelve equal balls (though the arrangement is subtle—there is “wiggle room” that misled some historical arguments).

### 1.4 Exceptional dimensions 8 and 24

| Dimension | Optimal packing (status) |
|-----------|---------------------------|
| $$n=1$$ | Intervals on a line (trivial) |
| $$n=2$$ | Hexagonal lattice — classical |
| $$n=3$$ | FCC/HCP density — Hales |
| $$n=8$$ | $$E_8$$ lattice — **Viazovska (2016)** |
| $$n=24$$ | Leech lattice — **Cohn–Kumar–Miller–Radchenko–Viazovska** |
| generic $$n$$ | Mostly open; asymptotic bounds exist |

The **$$E_8$$** and **Leech** lattices are miracles of symmetry: extremely dense shells of minimal vectors and rich automorphism groups. Viazovska constructed a radial “magic” function whose Fourier sign pattern matches the Cohn–Elkies linear programming bound *exactly* in dimension 8, proving optimality of $$E_8$$ among *all* packings (not only lattices).

### 1.5 Cohn–Elkies in one paragraph

Roughly: if a radial Schwartz function $$f$$ on $$\mathbb{R}^n$$ satisfies $$f(x)\le 0$$ for $$\lvert x\rvert\ge 1$$ and $$\hat f(\xi)\ge 0$$ for all $$\xi$$, with $$f(0)$$ and $$\hat f(0)$$ positive, then packing density is bounded above by a constant built from $$f(0)/\hat f(0)$$ (after scaling). The Poisson summation formula is the bridge: it relates values of $$f$$ on a lattice to values of $$\hat f$$ on the dual lattice, turning geometric non-overlap constraints into analytic sign constraints. Sharpness needs a function that “touches” the constraints in a way compatible with a lattice’s distance set—vanishing at the right radii so that equality cases can be read off. Modular forms supplied such functions in dimensions 8 and 24. You need not build $$f$$; you should understand that **packing became function design**, which is why a Fields Medal could be awarded for constructing the right auxiliary function rather than for stacking more oranges.

### 1.6 High-dimensional strangeness

As dimension grows, the volume of the unit ball

$$
V_n=\frac{\pi^{n/2}}{\Gamma(n/2+1)}
$$

peaks and then tends to 0. Most of the volume of a high-dimensional cube hides near the boundary; spheres become poor at filling space in naive coordinates. Best known packings, kissing numbers, and the gap between lattice and nonlattice optima behave irregularly. Link this studio to the fourth-dimension exploration if you enjoy volume paradoxes.

---

## 2. Conjecture versus proof versus experiment

| Label | Meaning | Example |
|-------|---------|---------|
| **Theorem** | Settled | Hexagonal optimum in 2D; Viazovska for $$E_8$$ |
| **Conjecture / open** | Unknown exact optimum | Most dimensions $$n\notin\{1,2,3,8,24\}$$ |
| **Lower bound** | Explicit packing density | Your coin packing; known lattice tables |
| **Upper bound** | Analytic/LP bound | Cohn–Elkies numerical bounds |

**Success criteria (state in your proposal):**

1. Measure densities for at least two 2D packings (square and hex) within 2% of the exact formulas.  
2. Produce one artifact: photo of coins, diagram, or simulation.  
3. Write a status table for $$n=2,3,8,24$$ and “generic $$n$$.”  
4. One paragraph on Cohn–Elkies / magic functions without claiming you constructed one.  
5. Log one misconception you corrected (e.g., “12 kissing is obvious from geometry of icosahedron alone”).

---

## 3. Research log standards

Each entry: **Date · Intent · Action · Result · Label · Interpretation · Next step**.

Include raw measurements (coin diameters, grid spacing, simulation parameters). Failed packings—overlaps you had to undo—belong in the log.

**AI disclosure.** Allowed for code; packing density *you* measured must be reproducible from your notes.

---

## 4. Experiments

Do at least **two** of A–E.

### Experiment A — Coin packing (25–40 min)

Pack equal coins in a large rectangular tray (or on paper with traced circles).

1. Force a square grid; estimate density = (number of coins × coin area) / tray area (use an inscribed region to reduce boundary bias).  
2. Force a hexagonal pattern; estimate density.  
3. Compare to $$\pi/4$$ and $$\pi/(2\sqrt{3})$$.

**Hypothesis before measuring:** “Boundary effects will dominate; I cannot see the 0.78 vs 0.91 gap.” Then check whether a large enough region reveals it.

**Success criterion:** two estimates + percent error vs exact formulas.

### Experiment B — Kissing in 2D and 3D (20–40 min)

- In 2D: show that 6 equal circles kiss a central equal circle, and argue 7 is impossible by angle $$60^\circ$$.  
- In 3D: try (with balls, oranges, or a 3D sketch) to place 12 around 1. Write why “rattling” caused historical confusion. Look up the known kissing numbers for $$n=4,8,24$$ and copy them with sources—**do not invent**.

**Success criterion:** 2D proof sketch + 3D narrative + cited table for a few higher $$n$$.

### Experiment C — Lattice density calculator (30–60 min)

Write a short program: given generating vectors for a 2D lattice and minimal distance, compute density. Verify square and hex. Optional: implement a random search for good 2D lattices (parameterize by angle and aspect) and plot density landscape.

**Success criterion:** code + verification that hex beats square; optional contour plot.

### Experiment D — Status and story (20–30 min)

After reading Ch.2 Viazovska (or the status table there), write a one-page “press release for mathematicians”:

- What was known before 2016?  
- What did Viazovska alone prove?  
- What was collaborative in dimension 24?  
- What remains open?

**Success criterion:** no conflation of solo $$E_8$$ with collaborative Leech; correct density slogans.

### Experiment E — Dimension and waste (stretch)

Using the formula for $$V_n$$, plot or tabulate unit-ball volume for $$n=1,\ldots,20$$. Connect to packing: if balls have tiny volume relative to cubes, how should packing density behave? Compare your intuition to known density bounds from a reliable table (cite).

**Success criterion:** table/plot + two sentences connecting volume decay to packing hardness.

---

## 5. Common confusions

1. **“Hexagonal packing is only locally optimal.”** — In 2D it is globally optimal among all packings.  
2. **“Viazovska solved packing in every dimension.”** — 8 and (with coauthors) 24; not all $$n$$.  
3. **“Lattice packings always win.”** — Not known in general; some dimensions may favor nonlattice packings.  
4. **“Kissing number equals coordination number of the densest packing.”** — Related but not automatic; definitions differ.  
5. **“Density is just how many balls fit in a box.”** — Boundary effects matter; the limit definition exists for a reason.

---

## 6. Exercises

1. Derive $$\delta_{\square}=\pi/4$$ carefully from first principles.  
2. Derive or look up and *re-explain* $$\delta_{\mathrm{hex}}=\pi/(2\sqrt{3})$$ with a clear fundamental cell.  
3. Show that if you scale all lengths by $$\lambda>0$$, density is unchanged. Why is that important for the definition?  
4. Explain in your own words why a Fourier upper bound can rule out packings denser than a given lattice even if you never list all packings.  
5. Draft a studio proposal (≤200 words): question, methods, success criteria, risks (boundary bias, unit conversion, software bugs).

---

## 7. Checkpoint rubric

| Done? | Item |
|-------|------|
| ☐ | Coin or simulation density for square and hex |
| ☐ | Density definition in your own words |
| ☐ | Status table $$2,3,8,24$$ + open generic |
| ☐ | One sentence on magic functions / Cohn–Elkies |
| ☐ | Log with ≥3 dated entries |
| ☐ | Open question (e.g., a specific dimension $$n$$) |

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/explore-sphere-packing/`.

**From the research pack (must-know slogans)**

- **Density** is a limit of volume ratios in large regions; boundary effects matter in finite boxes.
- **Hexagonal packing** maximizes density in 2D (Thue / Hales line of results); Kepler conjecture (3D) settled by Hales.
- **Viazovska (2016+):** optimal packing in dimensions 8 (E₈) and 24 (Leech) via modular-form “magic functions” and Cohn–Elkies LP bounds.
- Fourier / linear-programming upper bounds can rule out denser packings without listing them.
- Studio: measure densities carefully; separate theorem / conjecture / numerical observation.

**Recommended order**

1. **Core** — Viazovska — Einstein Lectures sphere packing: [https://www.youtube.com/watch?v=fH6KNlUJux0](https://www.youtube.com/watch?v=fH6KNlUJux0).  
2. **Core** — Viazovska — Sphere packing intro (ICMU): [https://www.youtube.com/watch?v=VR3Ezxo5wo8](https://www.youtube.com/watch?v=VR3Ezxo5wo8).  
3. **Research** — Viazovska — Simons Lecture Day 1 (MIT): [https://www.youtube.com/watch?v=mf_XOB7594c](https://www.youtube.com/watch?v=mf_XOB7594c).  
4. **Intuition** — Numberphile — Best Way to Pack Spheres: [https://www.youtube.com/watch?v=mceaM2_zQd8](https://www.youtube.com/watch?v=mceaM2_zQd8).  

**Official / primary written hubs**

- Viazovska E8 packing (arXiv:1603.04246): https://arxiv.org/abs/1603.04246  
- Cohn et al. dimension 24 (arXiv:1603.06518): https://arxiv.org/abs/1603.06518  
- Cohn–Elkies LP bounds (arXiv survey lineage): https://arxiv.org/abs/math/0110009  

Complete URL bibliography: `research/video-research/explore-sphere-packing/references.md`.

## 8. References and course links


### Video research pack (all URLs)

Complete list: `research/video-research/explore-sphere-packing/references.md`.

1. Viazovska — Einstein Lectures sphere packing — https://www.youtube.com/watch?v=fH6KNlUJux0  
2. Viazovska — Sphere packing intro (ICMU) — https://www.youtube.com/watch?v=VR3Ezxo5wo8  
3. Viazovska — Simons Lecture Day 1 (MIT) — https://www.youtube.com/watch?v=mf_XOB7594c  
4. Numberphile — Best Way to Pack Spheres — https://www.youtube.com/watch?v=mceaM2_zQd8  
5. Viazovska E8 packing (arXiv:1603.04246) — https://arxiv.org/abs/1603.04246  
6. Cohn et al. dimension 24 (arXiv:1603.06518) — https://arxiv.org/abs/1603.06518  
7. Cohn–Elkies LP bounds (arXiv survey lineage) — https://arxiv.org/abs/math/0110009  
8. Quanta — Sphere packing higher dimensions — https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/  
9. Quanta — Viazovska Fields profile — https://www.quantamagazine.org/ukrainian-mathematician-maryna-viazovska-wins-fields-medal-20220705/  
10. Wikipedia — Sphere packing — https://en.wikipedia.org/wiki/Sphere_packing  
11. Simons Foundation Fields video page (Viazovska) — https://www.simonsfoundation.org/2022/07/05/fields-medal-video-maryna-viazovska/  
12. Research pack folder: `research/video-research/explore-sphere-packing/`.

1. Course: [Viazovska essay]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/).  
2. Conway–Sloane, *Sphere Packings, Lattices and Groups* (classical handbook).  
3. Cohn–Elkies linear programming bounds; Viazovska 2016 $$E_8$$ paper.  
4. Nearby studios: [Kakeya]({{ site.baseurl }}/contents/en/chapter07/07_02_Explore_Kakeya/), [Fourth dimension]({{ site.baseurl }}/contents/en/chapter07/07_06_Explore_Fourth_Dimension/).

---

## Further directions

If density formulas felt easy but Fourier bounds felt opaque, re-read the Cohn–Elkies section of Ch.2 slowly and rewrite it as a five-sentence story for a friend who knows only integrals. If you enjoy discrete geometry more than analysis, pivot experiments toward kissing numbers and root lattices.

### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/explore-sphere-packing/transcripts/` · status: `research/video-research/explore-sphere-packing/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/explore-sphere-packing_fH6KNlUJux0_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

