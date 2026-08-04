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

Four colors suffice for every planar map—**Appel–Haken (1976)** and later simplifications, including computer-checked case analysis. That sentence hides a century of almost-proofs, Kempe’s famous error, the clean **five-color theorem**, and a richer theory of graphs on surfaces via **Heawood numbers**. This studio is hands-on: draw maps, build duals, fail at 3-coloring, compute genus bounds, and write a careful essay on what counts as a proof when machines check cases.

You will not re-run the four-color computer search. You will **practice the definitions** that make the theorem meaningful and explore what changes when the surface or the rules change.

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

## 1. Background mathematics

### 1.1 Maps, duals, and chromatic number

A **map** (for four-color purposes) is a division of the plane (or sphere) into finitely many connected regions (“countries”). Two countries are adjacent if they share a positive-length border (a point of contact does not count). A **coloring** assigns colors so that adjacent countries differ.

Form the **dual graph** $$G$$: one vertex per country; an edge when countries share a border. Map coloring ≡ **vertex coloring** of $$G$$. For proper map duals, $$G$$ is planar (and typically bridgeless under mild assumptions). The **chromatic number** $$\chi(G)$$ is the minimum colors needed.

The **Four Color Theorem (4CT):** every planar graph is 4-colorable; equivalently, every planar map is 4-colorable.

### 1.2 Why five colors is easier

From Euler’s formula for simple connected plane graphs, together with the handshaking lemma for faces $$2e\ge 3f$$ (each face has at least three edges, each edge bounds at most two faces), one derives $$e\le 3v-6$$ for $$v\ge 3$$. Therefore the average degree satisfies $$2e/v<6$$, so there exists a vertex $$v$$ with $$\deg(v)\le 5$$. The **five-color theorem** proceeds by induction on $$v$$: remove a low-degree vertex, five-color the rest by induction, and if the neighbors of the deleted vertex use five distinct colors, attempt a Kempe-chain recoloring to free a color. The argument is completely human-checkable and is standard in every graph theory course.

Kempe’s 1879 attempt for **four** colors had a gap (exposed by Heawood in 1890). The gap is subtle—exactly the sort of thing worth reading once slowly in Ch.1. The moral for your studio is methodological: a beautiful inductive idea can be *almost* right and still fail at a single recoloring case. That is why computer-checked case analysis later entered the four-color story without entering the five-color story.

### 1.3 What Appel–Haken did

The 4CT proof reduces the problem to a finite (but large) set of **unavoidable configurations** that are **reducible**: each cannot appear in a minimal counterexample. Unavoidability means every minimal counterexample must contain one of the configurations (often proved via discharging: assign charges from Euler’s formula and redistribute until a configuration is forced). Reducibility means a coloring of the rest of the graph can be extended inward after finitely many recoloring checks. Checking reducibility involved computer enumeration of cases. Later work (Robertson, Sanders, Seymour, Thomas, and others) simplified the unavoidable set and rechecked with independent programs; formal verification efforts have further increased confidence. Still, the proof is unlike the five-color proof in length and method: a student can internalize five-color in an afternoon, while four-color is a research-scale case analysis even after simplifications.

**Studio question for your log:** does “computer-assisted” mean “not a proof”? Write your standards before and after reading Ch.1’s discussion. A productive middle position many mathematicians hold: a proof is a social object that the community can check in principle; machines are legitimate checkers when their programs and specifications are themselves auditable.

### 1.4 Surfaces and Heawood

On a surface of genus $$g\ge 1$$, Euler’s formula changes (Euler characteristic $$\chi=2-2g$$ for closed orientable surfaces), and average degree bounds weaken because the inequality relating edges and vertices depends on $$\chi$$. **Heawood’s number**

$$
H(g)=\left\lfloor\frac{7+\sqrt{1+48g}}{2}\right\rfloor
$$

gives an upper bound on colors for maps on the orientable surface of genus $$g$$ (for $$g=0$$ the formula yields 4, but the classical Heawood argument for the sphere/plane is not a complete 4CT proof—history matters). For the **torus** ($$g=1$$), $$H(1)=7$$, and 7 is sharp: there exist toroidal maps needing 7 colors. Computing $$H(g)$$ for small $$g$$ by hand is a mandatory fluency check in Experiment C.

Complete graphs $$K_n$$ embed on surfaces of sufficiently high genus; the **Ringel–Youngs** map color theorem settled the Heawood conjecture for $$g\ge 1$$, determining the chromatic number of each orientable surface. The contrast with the plane is cultural as well as technical: once genus is positive, the extremal complete-graph embeddings often pin down the sharp color number more cleanly than the planar four.

### 1.5 Rule changes that break four

If countries may be **disconnected** (two pieces of the same empire must share a color), one can force arbitrarily many colors already in the plane—identify pieces carefully so duals encode multi-component constraints. A standard construction idea is to take many pairs of regions that must share colors and arrange adjacencies so that those “super-vertices” form a large clique in the conflict graph. If borders can touch in wild ways, or if the map is infinite, statements change. Always freeze the rules in your proposal: connected countries? positive-length borders? finite maps? sphere or plane?

### 1.6 Beyond maps

Graph coloring generalizes far past cartography. **Brooks’ theorem** says that for a connected graph that is neither complete nor an odd cycle, $$\chi(G)\le \Delta(G)$$, the maximum degree—so local density of edges controls colors except in two famous families. **Chromatic polynomials** count proper $$k$$-colorings as a polynomial in $$k$$. **Hadwiger’s conjecture** proposes that high chromatic number forces a large complete minor. Optional stretch if the dual-graph language feels fluent; none of these is required to complete the studio checkpoint.

---

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

## 6. Exercises

1. From $$v-e+f=2$$ and $$2e\ge 3f$$ (assuming ≥3 edges per face), derive $$e\le 3v-6$$.  
2. Deduce existence of a vertex of degree $$\le 5$$.  
3. Show that $$K_5$$ is nonplanar (any standard argument) and explain why that does **not** by itself prove 4CT.  
4. Compute $$H(1)$$ and $$H(2)$$ carefully with the floor function.  
5. Proposal (≤150 words): artifact goals, rules frozen, success criteria.

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

