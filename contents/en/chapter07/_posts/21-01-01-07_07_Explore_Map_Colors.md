---
layout: post
title: "How many colors are really needed to color a map?"
chapter: '07'
order: 7
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Learning path B — Four colors (step 2 of 2)**  
> **1.** [Ch.1 Four Color Theorem]({{ site.baseurl }}/contents/en/chapter01/01_09_Four_Color_Theorem/)  
> **2. You are here:** Ch.7 map-colors studio  
> *Prerequisite:* dual graphs + five-color outline from Ch.1.

In October 1852, young student Francis Guthrie was coloring a map of the counties of England when a disarmingly simple question struck him: *Can every planar map—no matter how tangled its borders—be colored with at most four colors so that no two bordering regions share a color?* Passed through his brother Frederick to Augustus De Morgan, the puzzle became a **124-year** obsession. In 1879, lawyer and mathematician Alfred Kempe published a celebrated "proof," and the world applauded for eleven years—until Percy Heawood exposed a subtle flaw in Kempe's color-swapping chains.

Only in 1976 did Kenneth Appel and Wolfgang Haken finally settle the **Four Color Theorem**, and they did so in a way that sparked decades of philosophical debate: by enlisting a computer to verify thousands of configurations. In this studio, you will not re-run that massive search. Instead, you will **draw maps and convert them into dual graphs**, watch 3 colors fail by hand, walk through the crisp human-readable **five-color proof**, jump onto a donut (torus) where **seven** colors are needed, and articulate your own standard for what counts as a proof in the age of machines.

**Lesson roadmap:** Background Knowledge Map (graph theory, surface topology & computer-assisted proofs) → Dual graphs & the five-color theorem → Deep-Dive Explanation (Read Slowly): hand-checking Euler's bound on $$K_4, K_5, K_7$$ and stepping through a Kempe-chain swap → Appel–Haken & Heawood numbers $$H(g)$$ → Studio experiments & log.

---

## Learning objectives

After this studio you should be able to:

- Convert a map to its **dual graph** and restate coloring as a graph vertex-coloring problem.
- Exhibit a planar map (or planar graph) that needs four colors, and argue why three fail.
- Outline the **five-color theorem** using Euler’s formula and the existence of a vertex of degree $$\le 5$$.
- Compute Heawood’s number $$H(g)=\bigl\lfloor(7+\sqrt{1+48g})/2\bigr\rfloor$$ for small genus $$g$$ and interpret it.
- Explain how **disconnected countries** (mutilated maps) can demand arbitrarily many colors.
- Write a reflection separating: elementary five-color proof, four-color computer-assisted proof, and surface-color theorems.

**Prerequisites.** Planar graphs, Euler’s formula $$v-e+f=2$$ for connected plane graphs, basic induction.

---

## Background Knowledge Map: What Are Graph Theory and Surface Topology?

Behind the childhood pastime of coloring maps stand three pillars of modern mathematics and computer science:

### 1. Graph Theory and Chromatic Number

Graph theory strips away irrelevant geometry (wiggly coastlines, country sizes) and keeps only **adjacency**: each country becomes a *vertex*, and two countries sharing a border segment are linked by an *edge*. Map coloring becomes finding the **chromatic number** $$\chi(G)$$ of the **dual graph** $$G$$. Beyond cartography, graph coloring directly models **exam timetabling** (courses sharing a student cannot share a time slot), **CPU register allocation** in compilers, and **cellular frequency assignment** to prevent signal interference.

### 2. Surface Topology and Genus $$g$$

Why does a flat map (or globe) need at most 4 colors while a map on a donut (torus) can demand **7**? Surface topology studies invariants unchanged by stretching without tearing. The key invariant is the **genus** $$g$$ (number of holes), linked to the **Euler characteristic** $$\chi = v - e + f = 2 - 2g$$. Extra holes let edges "tunnel through the handle" without crossing, letting denser complete graphs like $$K_7$$ embed cleanly on a torus.

### 3. Computer-Assisted Proofs and Formal Verification

The Four Color Theorem marked a cultural turning point: the first major theorem whose proof depended on machine-checked case analysis. Today, proof assistants like **Coq** (used by Georges Gonthier in 2005 to formally verify the entire Four Color Theorem) and **Lean** provide a small, auditable kernel that checks every single logical step with mechanical certainty.

---

## 1. Background mathematics

### 1.1 Maps, duals, and chromatic number

A **map** (for four-color purposes) is a division of the plane (or sphere) into finitely many connected regions (“countries”). Two countries are adjacent if they share a positive-length border (a point of contact does not count—otherwise a 100-slice pizza meeting at the center would need 100 colors!). Form the **dual graph** $$G$$: one vertex per country; an edge when countries share a border. Map coloring ≡ **vertex coloring** of $$G$$. The **chromatic number** $$\chi(G)$$ is the minimum colors needed.

The **Four Color Theorem (4CT):** every planar graph is 4-colorable; equivalently, every planar map is 4-colorable.

### 1.2 Why five colors is easier

From Euler’s formula for simple connected plane graphs, together with $$2e\ge 3f$$, one derives $$e\le 3v-6$$ for $$v\ge 3$$. Therefore the average degree satisfies $$2e/v<6$$, guaranteeing a vertex $$v$$ with $$\deg(v)\le 5$$.

#### Deep-Dive Explanation (Read Slowly): Hand-Checking Euler's Bound on $$K_4, K_5, K_7$$ and Running a Kempe Chain

Walk through two short hand calculations that unlock the whole chapter:

**Example 1 — Checking Euler's bound on $$K_4$$, $$K_5$$ (plane) and $$K_7$$ (torus):**
- **$$K_4$$ (four mutually bordering countries):** $$v = 4$$, $$e = \binom{4}{2} = 6$$. Planar bound: $$3v - 6 = 3(4) - 6 = 6 \ge e$$ → **fits!** Draw three countries $$A, B, C$$ in a ring around a central country $$D$$: $$f = 4$$ faces, $$v - e + f = 4 - 6 + 4 = 2$$, and because all 4 vertices touch pairwise, you are forced to use **4 colors**.
- **$$K_5$$ in the plane:** $$v = 5$$, $$e = \binom{5}{2} = 10$$. Planar bound allows at most $$3(5) - 6 = 9 < 10$$ edges → **impossible to draw $$K_5$$ flat!**
- **$$K_7$$ on the torus ($$g = 1$$):** Here $$v - e + f = 2 - 2(1) = 0$$. With $$f \le \frac{2}{3}e$$, we get $$e - v = f \le \frac{2}{3}e \implies \mathbf{e \le 3v}$$. For $$K_7$$: $$v = 7$$ and $$e = \binom{7}{2} = 21 = 3 \times 7$$—**hitting exact equality!** Thus $$K_7$$ embeds cleanly on a donut and forces **7 colors**.

**Example 2 — Stepping through a Kempe chain in the Five-Color Theorem:**
By induction, delete a vertex $$x$$ of degree $$\le 5$$ and 5-color the remaining graph. Suppose its 5 clockwise neighbors use all 5 colors: $$u_1(\text{Red}), u_2(\text{Blue}), u_3(\text{Yellow}), u_4(\text{Green}), u_5(\text{Purple})$$.
1. Follow all vertices reachable from $$u_1(\text{Red})$$ using only **Red and Yellow** vertices (the **Red–Yellow Kempe chain**).
2. **Case 1:** This chain *misses* $$u_3(\text{Yellow})$$. Swap **Red ↔ Yellow** throughout the chain! Now $$u_1$$ becomes Yellow while $$u_3$$ stays Yellow → **Red is freed** for $$x$$!
3. **Case 2:** The chain *connects* $$u_1$$ to $$u_3$$. Together with $$x$$, that Red–Yellow path forms a **closed loop** in the plane! By the Jordan Curve Theorem, this loop traps $$u_2(\text{Blue})$$ on one side and $$u_4(\text{Green})$$ on the other. Therefore the **Blue–Green** Kempe chain from $$u_2$$ *cannot cross the Red–Yellow wall* to reach $$u_4$$! Swap **Blue ↔ Green** on $$u_2$$'s component → **Blue is freed** for $$x$$!

In 1879, Kempe tried running **two** Kempe chains simultaneously to drop from 5 colors to **4**, and Heawood (1890) proved those two chains can tangle and wreck each other when swapped together.

### 1.3 What Appel–Haken did

The 4CT proof reduces the problem to a finite (but large) set of **unavoidable configurations** that are **reducible**: each cannot appear in a minimal counterexample. Unavoidability is proved via **discharging** (assigning charges from Euler’s formula and redistributing them until a configuration is forced). Reducibility means every coloring of the exterior extends inward after finitely many recoloring checks—originally 1,936 cases (later 1,476), streamlined by Robertson, Sanders, Seymour, and Thomas (1997) to 633 configurations, and formally verified in Coq by Georges Gonthier (2005).

**Studio question for your log:** does “computer-assisted” mean “not a proof”? Write your standards before and after reading Ch.1’s discussion.

### 1.4 Surfaces and Heawood

On a surface of genus $$g\ge 1$$, Euler’s formula changes (Euler characteristic $$\chi=2-2g$$ for closed orientable surfaces), and **Heawood’s number**

$$
H(g)=\left\lfloor\frac{7+\sqrt{1+48g}}{2}\right\rfloor
$$

gives the chromatic upper bound: $$H(0) = 4$$ (plane/sphere—though Heawood's argument alone does not prove 4CT), $$H(1) = \lfloor(7+\sqrt{49})/2\rfloor = 7$$ (torus), and $$H(2) = \lfloor(7+\sqrt{97})/2\rfloor = 8$$ (double torus). **Ringel and Youngs (1968)** proved that $$H(g)$$ is exact for every $$g \ge 1$$.

### 1.5 Rule changes that break four

If countries may be **disconnected** (pieces of the same empire must share a color), one can force arbitrarily many colors already in the plane (if each empire has at most $$m \ge 2$$ pieces, the sharp bound jumps to $$6m$$!). Always freeze the rules in your proposal: connected countries? positive-length borders? finite maps? sphere or plane?

### 1.6 Beyond maps

Graph coloring generalizes far past cartography. **Brooks’ theorem** says that for a connected graph that is neither complete nor an odd cycle, $$\chi(G)\le \Delta(G)$$. **Chromatic polynomials** count proper $$k$$-colorings as a polynomial in $$k$$. **Hadwiger’s conjecture** proposes that high chromatic number forces a large complete minor.

---

### Short video: Why 3 colors fail (K₄) and Heawood numbers by surface genus

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/four-color-kempe_en.mp4"></video>
</div>

2 min 04 sec video: map-to-dual reduction, why K₄ forces 4 colors, Euler’s bound e ≤ 3v − 6, both Kempe-chain cases in the five-color proof, Kempe’s 1879 pitfall, and Heawood numbers H(0) = 4 (plane) and H(1) = 7 (torus).


<div class="interactive-demo" markdown="1">
<div data-demo="fourcolor-explainer" data-preset="k4" data-lang="en"></div>
</div>
<script src="{{ '/public/js/explainers/fourcolor-explainer.js' | relative_url }}"></script>

## 2. Conjecture versus proof versus experiment

| Label | Example |
|-------|---------|
| **Theorem** | 4CT; five-color; Heawood for $$g\ge 1$$ (Ringel–Youngs) |
| **Historical almost** | Kempe’s flawed 4-color argument |
| **Construction** | Your map needing 4 colors; dual graph drawing |
| **Reflection** | Standards for computer-assisted proof |

**Success criteria:**

1. Artifact: planar map needing 4 colors + dual graph.  
2. Explicit failure of a 3-coloring attempt (which vertex/country blocks).  
3. Heawood values for $$g=0,1,2$$ computed by hand.  
4. Five-color outline in ≤12 bullet-free *sentences* (prose induction sketch).  
5. Paragraph on disconnected regions and/or computer-assisted proof standards.

---

## 3. Research log standards

**Date · Intent · Action · Result · Label · Interpretation · Next step.**

Photograph or scan drawings. If you generate maps with code (random planar graphs), record the generator. Disclose AI-drawn maps; still verify adjacency by hand for your 4-critical example.

---

## 4. Experiments

Do at least **two** of A–E (A is strongly recommended).

### Experiment A — Hands-on planar map (25–45 min)

Invent or find a map that needs four colors. Classical small examples include configurations whose dual contains a $$K_4$$ minor in an essential way, or carefully arranged countries where each of four regions meets the other three along positive-length borders. Build the dual carefully: vertices for countries, edges only for shared arcs (not mere point contacts). Attempt a 3-coloring systematically—perhaps by backtracking on a small dual—and record the obstruction (which vertex has three differently colored neighbors that block the fourth color under a three-color palette).

**Success criterion:** map + dual + written obstruction + a one-sentence explanation of why corner-touching does not create an edge.

### Experiment B — Five-color story (20–35 min)

From $$e\le 3v-6$$, prove there is a vertex of degree $$\le 5$$. Outline five-color induction in connected prose (not a bare bullet list): base cases, inductive step, and what you do when five neighbors use five colors. Where would the argument break for four colors (Kempe-chain failure slogan)? If you have time, sketch *one* Kempe chain picture with two colors swapping along a path connecting two neighbors—then note that chains for two different color pairs can interfere, which is the historical danger zone.

**Success criterion:** degree lemma + induction outline + one sentence on the four-color gap + optional Kempe sketch.

### Experiment C — Torus and genus (20–40 min)

Compute $$H(g)$$ for $$g=0,1,2,3$$. For $$g=1$$, find a reference image of a 7-color-critical toroidal map (cite URL/book). Explain why the plane’s “4” is harder than the torus’s “7” historically.

**Success criterion:** values table + cited image + historical note.

### Experiment D — Disconnected empires (20–30 min)

Design a map with two-piece countries forcing 5 colors under empire rules, or look up a standard construction and redraw it. Discuss how the dual changes (identify vertices?).

**Success criterion:** figure + rule statement + color lower bound argument.

### Experiment E — Proof culture essay (25–40 min)

After Ch.1 on Appel–Haken, write 5–8 sentences answering: What is a proof? Must a human survey every case? How do independent rechecks and formalization change confidence?

**Success criterion:** essay with a clear personal standard (not a rant).

---

## 5. Common confusions

1. **“Four colors are always necessary.”** — Many maps need only 2 or 3; four is the worst case for planar maps.  
2. **“Five-color needs a computer.”** — No; five is elementary. Four is the computer-assisted one.  
3. **“Heawood’s formula proves 4CT.”** — For $$g=0$$ the formula gives 4, but the classical Heawood proof technique does not settle the planar case the way Ringel–Youngs settles higher genus.  
4. **“Touching at a corner forces different colors.”** — Standard rules require shared boundary arcs.  
5. **“Any graph is a map dual.”** — Duals of proper maps are planar and have structure; arbitrary graphs may be nonplanar ($$\chi$$ can be huge).

---

## 7. Checkpoint rubric

| Done? | Item |
|-------|------|
| ☐ | Map + dual graph artifact |
| ☐ | Obstruction to 3 colors |
| ☐ | Heawood values $$g=0,1$$ (and preferably 2) |
| ☐ | Five-color outline in prose |
| ☐ | Disconnected regions or proof-culture paragraph |
| ☐ | Link back to Ch.1 misconceptions |
| ☐ | Log ≥3 entries |

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/explore-map-colors/`.

**From the research pack (must-know slogans)**

- **4CT:** every planar map is 4-colorable (Appel–Haken 1976; later simplifications / formal proofs).
- **Five-color theorem** has a short human proof; four requires reducibility + discharging + case check.
- Computer-assisted proof is still a proof if the method is finite and checkable in principle (Gonthier formalization culture).
- Studio: dual graphs, Kempe chains, attempt small reductions; discuss “what counts as proof.”

**Recommended order**

1. **Orientation** — Numberphile — Four Color Map Theorem: [https://www.youtube.com/watch?v=NgbK43jB4rQ](https://www.youtube.com/watch?v=NgbK43jB4rQ).  
2. **Intuition** — Numberphile — Four Color Theorem extra footage: [https://www.youtube.com/watch?v=laMkuPrad3s](https://www.youtube.com/watch?v=laMkuPrad3s).  

**Official / primary written hubs**


Complete URL bibliography: `research/video-research/explore-map-colors/references.md`.

## 8. References and course links


### Video research pack (all URLs)

Complete list: `research/video-research/explore-map-colors/references.md`.

1. Numberphile — Four Color Map Theorem — https://www.youtube.com/watch?v=NgbK43jB4rQ  
2. Numberphile — Four Color Theorem extra footage — https://www.youtube.com/watch?v=laMkuPrad3s  
3. Wikipedia — Four color theorem — https://en.wikipedia.org/wiki/Four_color_theorem  
4. Illinois Distributed Museum — 4CT — https://distributedmuseum.illinois.edu/exhibit/four-color-theorem/  
5. Appel–Haken BAMS announcement (Euclid) — https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-82/issue-5/Every-planar-map-is-four-colorable/bams/1183538218.full  
6. Celebratio — Haken four-color solution — https://celebratio.org/Haken_W/article/794/  
7. Gonthier formal proof discussion (MathOverflow thread) — https://mathoverflow.net/questions/44673/human-checkable-proof-of-the-four-color-theorem  
8. Wikipedia — Five color theorem — https://en.wikipedia.org/wiki/Five_color_theorem  
9. Wikipedia — Graph coloring — https://en.wikipedia.org/wiki/Graph_coloring  
10. Research pack folder: `research/video-research/explore-map-colors/`.

1. Course: [Four Color Theorem]({{ site.baseurl }}/contents/en/chapter01/01_09_Four_Color_Theorem/).  
2. Wilson, *Four Colors Suffice* (history).  
3. Standard graph theory texts: Euler’s formula, five-color proof, Heawood.  
4. Optional contrast: [Kakeya path A]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/) (open analytic culture vs computer proof culture).

---

## Further directions

**Path B complete** when the checkpoint rubric is filled and the dual-graph artifact is saved.

Advanced directions if the dual-graph language feels fluent: **Hadwiger’s conjecture** relates chromatic number to clique minors; **list coloring** asks whether choice numbers can exceed chromatic numbers (for planar graphs, Thomassen’s 5-choosability is a gem); **Grötzsch’s theorem** says triangle-free planar graphs are 3-colorable—so “how many colors” depends on extra hypotheses. Complexity adds another meaning: deciding 3-colorability of planar graphs is NP-hard in general, which does not contradict 4CT (which asserts a *uniform* upper bound of four, not an efficient algorithm for three).

**Synthesis prompt for the report.** In one page, contrast (i) five-color as a human induction, (ii) four-color as finite reducibility + machine check, (iii) Heawood/Ringel–Youngs as a surface story where the sharp number is sometimes easier to settle than the planar four. End with your personal standard for “what counts as a proof.”

### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/explore-map-colors/transcripts/` · status: `research/video-research/explore-map-colors/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/explore-map-colors_NgbK43jB4rQ_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*


## Video tham khảo

- **xem trước** — [The Four Color Map Theorem - Numberphile](https://www.youtube.com/watch?v=NgbK43jB4rQ) — Numberphile, English. Watch first. “The Four Color Map Theorem - Numberphile” orients the lesson’s aim: Convert a map to its dual graph and restate coloring as a graph vertex-coloring problem.
- [The Map Coloring Puzzle That Changed Mathematics](https://www.youtube.com/watch?v=h7kqlYUV1l8) — Quanta Magazine, English. A second pass once the main claim is in view: Convert a map to its dual graph and restate coloring as a graph vertex-coloring problem.
- [John Conway - Four Color Theorem and Computer Proofs](https://www.youtube.com/watch?v=fPVXBurxfU8) — Simons Foundation, English. Further depth after the first two, still tied to this lesson: Convert a map to its dual graph and restate coloring as a graph vertex-coloring problem.
