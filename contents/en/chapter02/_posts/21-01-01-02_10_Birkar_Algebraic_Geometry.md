---
layout: post
title: "Birkar’s Work in Algebraic Geometry (Fields Medal 2018)"
chapter: '02'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Suppose you are handed an infinite zoo of shapes carved out by polynomial equations in four, five, or a hundred complex dimensions. Every time you tweak a degree or add a variable, a brand-new shape appears. How could anyone possibly build a **periodic table of all algebraic shapes**?

In one complex dimension (curves), nineteenth-century mathematicians solved this completely: every smooth compact Riemann surface is sorted cleanly by a single integer, its **genus** $$g$$ (number of holes)—the sphere ($$g=0$$), the torus ($$g=1$$), or a multi-holed surface ($$g \ge 2$$). In two dimensions (surfaces), Italian and Japanese geometers achieved a celebrated classification by allowing controlled geometric surgeries. Above dimension two, however, the zoo explodes into wild, singular territory.

**Caucher Birkar**—who grew up on a subsistence farm in Iranian Kurdistan during the Iran–Iraq War before seeking asylum in the UK—received the **Fields Medal in 2018** for bringing breathtaking order to that higher-dimensional wilderness. Together with Paolo Cascini, Christopher Hacon, and James McKernan (BCHM), he helped establish core pillars of the **Minimal Model Program (MMP)**; then, in a solo tour de force, he proved the **Borisov–Alexeev–Borisov (BAB) conjecture** on the **boundedness of Fano varieties**—showing that the positively curved "atomic building blocks" of higher-dimensional algebraic geometry cannot run wild to infinity.

This essay unpacks the **architecture** of higher-dimensional classification using concrete, hand-checkable geometric examples—showing what birational equivalence keeps, how blow-ups heal singularities, why Fano varieties are the positively curved atoms, and what Birkar’s theorem really proves.

---

## Learning objectives

After this lecture you should be able to:

- Explain **birational equivalence** using the concrete circle-to-line stereographic projection, and see what it keeps versus forgets.
- Perform a **blow-up** by hand on the nodal curve $$y^2 = x^2(x+1)$$ to see how algebraic surgery resolves a singularity.
- State the goal of the **Minimal Model Program (MMP)**: simplify any projective variety into a minimal model or a Mori fiber space via divisorial contractions and flips.
- Identify **Fano varieties**, **Calabi–Yau varieties**, and **general-type varieties** on hypersurfaces in $$\mathbb{P}^3$$ using the canonical class $$K_X = (d-n-1)H$$.
- Distinguish **existence of flips** (collaborative BCHM) from **boundedness of Fano varieties** (Birkar’s solo BAB proof).
- Describe higher-dimensional classification as a living **reduction architecture**, not a finished encyclopedia of every variety.

**Prerequisites.** Familiarity with polynomials, curves, and basic complex/projective geometry helps; line bundles and canonical classes are introduced intuitively through concrete hypersurface examples.

**Related lessons.** Pair with [Beautiful Mathematics]({{ site.baseurl }}/contents/en/chapter04/) for "structure first" aesthetics, and compare with [Scholze / perfectoid geometry]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/) as a *different* foundational revolution inside algebraic geometry.

---

## Key ideas: What Is Birational Algebraic Geometry?

If your undergraduate background covered linear algebra and multivariable calculus, "algebraic geometry" can sound forbidding. At heart, its core ideas are vivid and geometric.

### 1. Algebraic Varieties: Shapes Carved by Polynomials
**What is it?** An algebraic variety is the solution set of polynomial equations—like the unit circle $$x^2 + y^2 = 1$$, a cubic surface in 3D, or a 10-dimensional manifold cut out by polynomials in projective space $$\mathbb{P}^N$$ (ordinary space plus "points at infinity" so parallel lines meet cleanly).

**What does it study?**
- **Smoothness vs. singularities:** Most points look like flat Euclidean space, while special points can pinch into corners, cusps, or self-intersections.
- **Curvature via the canonical class $$K_X$$:** In algebraic geometry, the **canonical divisor $$K_X$$** plays the role of curvature (technically, $$-K_X$$ corresponds to Ricci curvature). Just as surfaces split into sphere (positive curvature), torus (flat), and multi-holed donuts (negative curvature), higher-dimensional varieties split into three grand families: **Fano** ($$-K_X > 0$$), **Calabi–Yau** ($$K_X = 0$$), and **general type** ($$K_X > 0$$).

### 2. Birational Geometry: Allowing Clean Surgery
**What is it?** Classifying varieties up to strict isomorphism is too rigid: you can always "blow up" a single point on a smooth surface into a line, creating infinitely many slightly modified copies of the same shape. **Birational geometry** declares two shapes equivalent if they become isomorphic after deleting thin, lower-dimensional slices.

**What does it study?**
- **Blow-ups and contractions:** Replacing a point with a projective space of tangent directions (blowing up) to untangle singularities, or collapsing excess curves/divisors back down (contracting).
- **Minimal models:** Stripping away unnecessary "geometric fat" until a variety reaches its simplest representative.

### 3. Moduli & Boundedness: Can All Shapes Fit in One Finite Catalogue?
**What is it?** A **moduli space** is a geometric space whose points *are* other geometric shapes (for example, the space of all triangles or all elliptic curves).

**What does it study?**
- **Boundedness:** A family of shapes is **bounded** if a finite number of polynomial families with finitely many parameters captures every shape in the class. Without boundedness, you cannot even hope to construct a finite-type moduli space or a complete classification table.

---

## 1. Why higher dimensions feel different

In complex dimension one, compact Riemann surfaces fall into three crisp buckets by genus $$g$$: the sphere ($$g=0$$, positive curvature), elliptic curves ($$g=1$$, flat), and higher-genus curves ($$g\ge 2$$, negative curvature). In dimension two, the **Enriques–Kodaira classification** organizes smooth surfaces by contracting redundant $$(-1)$$-curves until you hit a clean minimal surface.

From dimension three upward, two dramatic shocks occur:
1. Even if you start with a **completely smooth** 3-fold, simplifying it inevitably creates **mild singularities**—so you must widen your category to include controlled singularities (such as **klt**, *Kawamata log terminal* singularities).
2. Ordinary contractions sometimes get stuck on tiny codimension-$$\ge 2$$ loci, forcing a subtle surgical move called a **flip**.

The modern answer is therefore not a giant list—it is an algorithm called the **Minimal Model Program (MMP)**.

---

## 2. Birational geometry: two hand-verifiable surgeries

Two irreducible varieties $$X$$ and $$Y$$ are **birational** if they share isomorphic dense open sets $$U \simeq V$$ (equivalently, the same field of rational functions).

### Hand-Verifiable Example 1: Why a Circle and a Line Are Birational
Consider the unit circle $$C: x^2 + y^2 = 1$$ and the straight line $$\mathbb{R}$$ with coordinate $$t$$. Project every point $$(x,y)$$ on the circle from the left pole $$(-1,0)$$ onto the vertical axis $$t$$:

$$
t = \frac{y}{1+x}
\qquad \Longleftrightarrow \qquad
x = \frac{1-t^2}{1+t^2}, \quad y = \frac{2t}{1+t^2}.
$$

Check by hand: $$x^2 + y^2 = \frac{(1-t^2)^2 + 4t^2}{(1+t^2)^2} = \frac{(1+t^2)^2}{(1+t^2)^2} = 1$$!
Notice the subtlety: the formula is undefined at the single point $$(-1,0)$$ on the circle, so the circle and the line are **not** isomorphic as affine curves—yet delete that one point, and they match one-to-one via rational functions! They are **birational**.

### Hand-Verifiable Example 2: Healing a Singularity with a Blow-Up
Now take the nodal cubic curve $$C: y^2 = x^2(x+1)$$ in the plane. At the origin $$(0,0)$$, the curve crosses itself like an "X" (with slopes $$+1$$ and $$-1$$)—a **singularity**.

How do algebraic geometers untangle it? **Blow up the origin** by introducing the slope coordinate $$t = y/x$$ (so $$y = tx$$) and substituting into the equation:

$$
(tx)^2 = x^2(x+1) \;\Longrightarrow\; x^2\bigl(t^2 - (x+1)\bigr) = 0.
$$

Factoring out the vertical exceptional line $$x=0$$ (the set of all slopes through the origin) leaves the **strict transform**

$$
\widetilde{C}: t^2 = x + 1,
$$

a completely **smooth parabola**! The two branches that collided at $$(0,0)$$ had different slopes ($$t=+1$$ and $$t=-1$$), so lifting the curve into $$(x,t)$$-space cleanly separates them at $$(0,1)$$ and $$(0,-1)$$.

Birational equivalence preserves the function field and the **Kodaira dimension**

$$
\kappa(X)=\operatorname{trdeg}\Bigl(\bigoplus_{m\ge 0} H^0(X,mK_X)\Bigr)-1,
$$

while freeing geometers to reshape singular or bloated compactifications into canonical building blocks.

---

## 3. Fano, Calabi–Yau, and General Type: Reading Curvature by Hand

How do you tell whether a smooth variety $$X$$ has positive, zero, or negative curvature?

### Hand-Verifiable Example 3: Hypersurfaces of Degree $$d$$ in Projective Space $$\mathbb{P}^n$$
Take a smooth hypersurface $$X \subset \mathbb{P}^n$$ cut out by a single homogeneous polynomial of degree $$d$$. By the classical **adjunction formula**, its canonical class is simply

$$
K_X = (d - n - 1) H,
$$

where $$H$$ is the positive hyperplane class! Now test $$n = 3$$ (smooth surfaces in $$\mathbb{P}^3$$):

- **$$d = 1, 2, 3$$ (planes, quadrics, cubic surfaces):** $$d - 4 < 0 \implies -K_X = (4-d)H > 0$$. These are **Fano varieties** (positive curvature—the higher-dimensional cousins of the sphere $$\mathbb{P}^1$$). For $$d=3$$, a smooth cubic surface famously contains exactly 27 straight lines!
- **$$d = 4$$ (quartic surfaces, like $$x_0^4 + x_1^4 + x_2^4 + x_3^4 = 0$$):** $$d - 4 = 0 \implies K_X = 0$$. These are **Calabi–Yau varieties** (specifically K3 surfaces, flat curvature—cousins of the torus).
- **$$d \ge 5$$ (quintics and higher):** $$d - 4 > 0 \implies K_X > 0$$. These are varieties of **general type** (negative curvature—cousins of genus $$\ge 2$$ surfaces).

In every dimension, **Fano varieties** ($$-K_X$$ ample) are the positively curved atoms: they appear as the fibers of Mori fiber spaces and serve as the flexible building blocks of birational geometry.

---


### Short Video 1: The Periodic Table of Varieties & the Minimal Model Program

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/birkar-fano-mmp_en.mp4"></video>
</div>

Short visual overview (37 sec): birational equivalence, blow-ups, the three building blocks (Fano, Calabi–Yau, General Type) via K_X, flips, and BCHM.

## 4. The Minimal Model Program: Contractions and Flips

Start with a projective variety $$X$$ (more generally, a klt pair $$(X,\Delta)$$). The MMP runs a directed simplification:

1. If $$K_X$$ is already **nef** ($$K_X \cdot C \ge 0$$ for every curve $$C \subset X$$), stop: you have reached a **minimal model**.
2. Otherwise, Mori’s Cone Theorem finds an extremal curve $$C$$ with $$K_X \cdot C < 0$$. You simplify $$X$$ along that ray using one of two surgeries:
   - **Divisorial contraction:** Collapse an entire codimension-1 wall (a divisor) to a smaller locus.
   - **Flip:** When the negative locus is too thin (codimension $$\ge 2$$), you cannot simply collapse it without destroying the canonical class. Instead, you surgically cut out the bad curve and glue in a different curve $$X^+ \to Z$$ on which $$K_{X^+}$$ becomes **positive**!
3. After finitely many steps, you expect to land on either a **minimal model** ($$K_X$$ nef) or a **Mori fiber space** $$X \to Z$$ whose general fiber is a **Fano variety**.

In 2010, **Birkar, Cascini, Hacon, and McKernan (BCHM)** proved a landmark theorem establishing the **existence of flips** and the **finite generation of canonical rings** in broad generality—completing a central engine of the MMP that had stalled for decades.

---

### Explanation: How Birkar Proved Boundedness of Fano Varieties

In dimension 1, there is only one Fano curve ($$\mathbb{P}^1$$). In dimension 2, there are 10 deformation families of smooth Fano (del Pezzo) surfaces. In dimension 3, Mori–Mukai classified smooth Fanos into 105 families. What about dimension $$n$$ when mild ($$\varepsilon$$-klt) singularities are allowed? Could wilder and wilder Fano varieties keep popping up with arbitrarily huge degrees and complexity?

The **Borisov–Alexeev–Borisov (BAB) conjecture** predicted **no**: for each fixed dimension $$n$$ and singularity threshold $$\varepsilon > 0$$, all $$\varepsilon$$-klt Fano varieties of dimension $$n$$ form a **bounded family**. Follow the four-step logic of Birkar’s 2016 proof slowly:

#### Step 1: Why Fano boundedness boils down to bounding volume and creating "complements"
To show a class of Fano varieties fits into finitely many polynomial families, you need two uniform controls: (a) an upper bound on the anticanonical volume $$\operatorname{vol}(-K_X)$$, and (b) a uniform integer $$m$$ (depending *only* on $$n$$ and $$\varepsilon$$) such that the linear system $$\lvert -mK_X \rvert$$ embeds $$X$$ into projective space. Equivalently, you want to find a well-behaved boundary divisor $$B$$ (an **$$N$$-complement**) such that $$N(K_X + B) \sim 0$$ with controlled singularities.

#### Step 2: Use MMP induction on dimension
Birkar attacked the problem by induction on dimension $$n$$. If you can cut a high-dimensional Fano variety $$X$$ by a carefully chosen hypersurface $$S \subset X$$ with controlled singularities, then $$S$$ is a lower-dimensional variety whose behavior is already controlled by the inductive hypothesis!

#### Step 3: Turn local singularity bounds into global finiteness (ACC for log canonical thresholds)
How do you stop singularities from secretly blowing up while you slice $$X$$? Earlier breakthrough work (Hacon–McKernan–Xu) proved the **Ascending Chain Condition (ACC) for log canonical thresholds**—meaning singularity sharpness cannot creep upward in an infinite sneaky staircase. Birkar fused this local rigidity with the existence of **bounded complements** to keep every inductive slice uniformly tame.

#### Step 4: Seal the BAB conjecture and unlock Fano moduli
Combining bounded complements, ACC for thresholds, and delicate birational surgeries (running specialized MMPs on pairs $$(X, B)$$), Birkar proved that **every $$\varepsilon$$-klt Fano variety of dimension $$n$$ lies in a bounded family**. Overnight, the "positive curvature" pillar of higher-dimensional algebraic geometry was locked inside a finite-type architectural frame—laying the foundation for modern K-stability and moduli spaces of Fano varieties.

In one schematic line:

$$
\text{MMP flips (BCHM)}
\;+\;
\text{Bounded complements}
\;+\;
\text{ACC for thresholds}
\;\Longrightarrow\;
\text{BAB boundedness of Fano varieties}.
$$

---


### Short Video 2: The BAB Conjecture & Boundedness of Fano Varieties

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/birkar-bab-complements_en.mp4"></video>
</div>

Short visual walkthrough (34 sec): ε-lc singularity bounds, volume control, bounded n-complements, and ACC for log canonical thresholds.

## 5. Classification architecture—not a finished encyclopedia

It is easy to misread “MMP + Fano boundedness” as “algebraic geometry is finished.” The real picture is architectural:

| Ingredient | Role |
|------------|------|
| Kodaira dimension $$\kappa$$ | Coarse birational invariant splitting varieties into regimes |
| Minimal models / Mori fiber spaces | Targets of the MMP reduction process |
| Flips and divisorial contractions | Elementary birational surgery steps |
| Fano boundedness (BAB) | Global finiteness control over the positively curved building blocks |
| Canonical rings / finite generation | Algebraic engine powering existence of flips and models |
| Singularities (klt, lc, …) | The precise language telling us which surgeries are legal |

Major open frontiers remain: **termination of flips** in full generality, effective explicit bounds for BAB, characteristic-$$p$$ analogues of the MMP, and explicit classification of special Fano manifolds. Birkar’s theorems redraw the **global map**; they do not list every street address.

---

## 6. Why a Fields Medal

Three interlocking reasons explain the 2018 medal:

1. **Difficulty.** Higher-dimensional flips and Fano boundedness resisted decades of effort; the proofs blend singularity theory, multiplier ideals, discrepancies, and deep inductive birational geometry.
2. **Centrality.** The MMP is the backbone of higher-dimensional algebraic geometry. Proving BAB boundedness reorganized the entire field—much like building the central bridge of a city changes every route across it.
3. **Clarity of slogan with depth of method.** “$$\varepsilon$$-klt Fano varieties of fixed dimension form a bounded family” is a sentence any graduate student can remember; its proof is a monument of twenty-first-century geometry.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “All algebraic varieties are Fano.” | Fano means $$-K_X$$ is ample (positive curvature); most varieties are Calabi–Yau or general type. |
| “Birational means isomorphic.” | Birational is weaker; blow-ups, contractions, and flips change lower-dimensional loci. |
| “Birkar classified all varieties.” | He proved foundational boundedness and MMP theorems; classification remains an active program. |
| “Flips are the same as blow-downs.” | Flips surgically replace codimension-$$\ge 2$$ loci when no divisorial contraction exists. |
| “Boundedness means only finitely many varieties.” | It means a family of finite type (continuous parameters allowed), not a finite discrete set. |
| “The 2018 medal is only solo work.” | Birkar’s solo BAB proof sits alongside a rich collaborative MMP network (BCHM and many others). |

---

## Video sources (math-video-researcher pack)

Full ranking: `research/video-research/Birkar_Algebraic_Geometry/`.

**Recommended order**

1. **Orientation** — Quanta video profile: [YouTube](https://www.youtube.com/watch?v=1EpMF16ShY0) · [article](https://www.quantamagazine.org/caucher-birkar-who-fled-war-and-found-asylum-wins-fields-medal-20180801/).  
2. **Interview** — Cambridge Fields interview: [YouTube](https://www.youtube.com/watch?v=CwMvjWL-gos).  
3. **Meta** — Simons Fields Medal video page: [link](https://www.simonsfoundation.org/2018/08/01/field-medals-video-caucher-birkar/).

**Status reminder:** Boundedness of Fanos + MMP contributions—**not** a complete classification of all varieties.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Birkar_Algebraic_Geometry/transcripts/` · status: `research/video-research/Birkar_Algebraic_Geometry/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Birkar_Algebraic_Geometry_1EpMF16ShY0_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


Full URL bibliography from video research (including secondary finds): `research/video-research/Birkar_Algebraic_Geometry/references.md`.

### Complete URL list (audit)

1. https://www.youtube.com/watch?v=1EpMF16ShY0  
2. https://www.youtube.com/watch?v=CwMvjWL-gos  
3. https://www.simonsfoundation.org/2018/08/01/field-medals-video-caucher-birkar/  
4. https://arxiv.org/search/?query=Birkar+Fano+boundedness&searchtype=all  
5. https://www.quantamagazine.org/caucher-birkar-who-fled-war-and-found-asylum-wins-fields-medal-20180801/  
6. https://www.maths.cam.ac.uk/features/professor-caucher-birkar-wins-2018-fields-medal  
7. https://en.wikipedia.org/wiki/Caucher_Birkar  
8. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018  
9. https://arxiv.org/search/math?query=Birkar+boundedness+Fano&searchtype=all&source=header  
10. https://en.wikipedia.org/wiki/Minimal_model_program  
11. https://en.wikipedia.org/wiki/Fano_variety  
12. https://arxiv.org/search/?query=Birkar+Fano&searchtype=all  

### Research pack

13. Course pack: `research/video-research/Birkar_Algebraic_Geometry/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. IMU Fields Medal 2018 citation — Caucher Birkar (mathunion.org).
2. **C. Birkar**, papers on boundedness of Fano varieties (BAB-type theorems); see also surveys announcing the 2016–2018 results.
3. **C. Birkar, P. Cascini, C. Hacon, J. McKernan (BCHM)** — existence of flips / finite generation of canonical rings in broad settings.
4. **J. Kollár and S. Mori**, *Birational Geometry of Algebraic Varieties*, Cambridge University Press — standard graduate background.
5. Surveys of the MMP (various authors; ICM proceedings and AMS notices expositions).
6. Course context: Chapter 2 overview and other “program-level” portraits such as [Scholze]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/).

---

## Further directions

- Compare surface classification (Enriques–Kodaira) with higher-dimensional MMP: which invariants survive, and which steps are new?
- Explore how singularities of the MMP (discrepancies, klt pairs) interact with the **canonical ring** and finite generation.
- Read a careful survey on BAB and complements to see how local thresholds become global boundedness.
- Seminar A3 option: write a one-page “open problems after Birkar” brief (effective bounds, positive characteristic, special Fano lists)—without claiming the medal closed algebraic geometry.

## Video tham khảo

- **xem trước** — [Caucher Birkar: An Innovator Who Brings Order to an Infinitude of Equations](https://www.youtube.com/watch?v=1EpMF16ShY0) — Quanta Magazine, English. Watch first. “Caucher Birkar: An Innovator Who Brings Order to an Infinitude of Equations” orients the lesson’s aim: State the goal of the minimal model program in one careful paragraph (reduce birationally toward a minimal model or a Mori fiber space).
- [2018 Fields Medal Recipient Caucher Birkar - Professor, University of Cambridge](https://www.youtube.com/watch?v=CwMvjWL-gos) — WebsEdgeScience, English. A second pass once the main claim is in view: State the goal of the minimal model program in one careful paragraph (reduce birationally toward a minimal model or a Mori fiber space).
