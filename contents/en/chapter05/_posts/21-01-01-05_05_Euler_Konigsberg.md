---
layout: post
title: "Euler and the Königsberg Bridges"
chapter: '05'
order: 5
owner: Nguyen Le Linh
lang: en
categories:
- chapter05
---

On Sunday afternoons in eighteenth-century Königsberg (now Kaliningrad), citizens strolling along the Pregel River entertained themselves with a charming wager: *can you walk through the city crossing all seven bridges exactly once, never retracing a single bridge?* Plenty of locals wore out their shoes trying, scribbling routes on tavern napkins, only to find themselves stranded before the seventh bridge every single time.

When the puzzle reached **Leonhard Euler** in St. Petersburg, he initially brushed it off as a trivial pastime with little to do with mathematics. Then a sudden realization struck him: you do not need to visit Königsberg, measure a single bridge, or trace the curve of the river. By **throwing away all metric geometry** and keeping only dots and connecting lines, Euler not only proved the walk impossible in 1736—he founded **graph theory**.

**Lesson roadmap:** Key ideas (graph theory, adjacency matrices, invariants and early topology) → The historical puzzle & the one-stroke envelope game → Multigraph modeling → Vertex degrees and parity → Explanation: hand-checking Königsberg’s $$4\times 4$$ adjacency matrix, adding one bridge, and assembling DNA with a de Bruijn graph → Sufficiency and the Chinese Postman Problem.

---

## Learning objectives

After this lecture you should be able to:

- Model a bridge (or road) system as a multigraph with vertices for regions and edges for crossings.
- Define Eulerian paths and Eulerian circuits and state the classical degree criteria.
- Apply the criteria to Königsberg’s four odd-degree vertices and conclude impossibility.
- Explain why the proof is a modeling proof: abstraction is the first mathematical act.
- Construct small examples that *do* admit Eulerian tours and contrast them with Königsberg.
- Connect the idea to modern network reasoning at slogan level.

**Prerequisites.** Willingness to draw diagrams; parity of integers; the idea of a walk as a sequence of adjacent edges. No prior graph theory course required.

---

## Key ideas: Graph Theory, Adjacency Matrices, and Early Topology

Before 1736, "geometry" meant lengths, angles, areas, and coordinates. Euler’s short memoir opened three foundational pillars that every modern science, engineering, and economics graduate encounters:

### 1. What Is Graph Theory and What Does It Study?
**Graph theory** studies pure **connectivity**. A graph $$G = (V, E)$$ consists solely of objects (**vertices** $$V$$) and connections (**edges** $$E$$). Subway maps, social networks, circuit boards, and supply chains are all graphs: stretching a line or rotating a diagram by $$90^\circ$$ changes nothing about the underlying network. Core questions include shortest paths (Dijkstra), maximum network flow, graph coloring (scheduling), and edge/vertex traversals (Eulerian vs. Hamiltonian).

### 2. Combinatorial Invariants and Linear Algebra on Graphs
To prove a task is *impossible*, you cannot test every candidate path—their number explodes factorially. Instead, you look for an **invariant**: a property every valid solution *must* satisfy (here, degree parity). Moreover, in linear algebra and computer science, any graph encodes cleanly as an **adjacency matrix** $$M$$ (entry $$M_{ij}$$ counts edges between vertex $$i$$ and vertex $$j$$), turning network questions into matrix powers and eigenvalues (the engine behind Google’s PageRank).

### 3. Early Topology (*Geometria Situs*)
Euler called his approach *"the geometry of position"*—the direct ancestor of **topology**, which studies properties preserved under continuous stretching and bending without tearing. The seven bridges of Königsberg launch the conceptual thread running straight to the Four Color Theorem and the Poincaré Conjecture later in this chapter.

---

## 1. The historical puzzle — and the childhood one-stroke envelope game

Before looking at Königsberg, recall a classic playground puzzle: **draw a house (a square with an X inside and a triangular roof on top) in one continuous stroke without lifting your pen or retracing any line.** If you have ever tried it, you hit an eerie quirk: start at the roof’s peak and you always get stuck; start at either bottom corner and the whole drawing glides smoothly to completion!

Why does the starting corner matter so much? Because every time your pen passes *through* an intermediate junction, it uses **one edge going in** and **one edge going out**—consuming edges in pairs (an even count). Only two points are allowed to have an odd number of incident lines: where you put the pen down and where you lift it up. On the envelope/house, the two bottom corners have degree $$3$$ (odd) while every other junction is even—forcing you to start at one bottom corner and end at the other.

Königsberg is simply the one-stroke drawing game scaled up to a city: four land regions joined by seven bridges, with **all four regions having an odd number of bridges**. Euler’s 1736 memoir turned that walk into the founding theorem of graph theory.

---

## 2. The modeling idea

Replace each land mass by a **vertex**. Replace each bridge by an **edge** joining the vertices of the lands it connects. Multiple bridges between the same pair of lands become **multiple edges**. The city becomes a **multigraph** $$G=(V,E)$$.

A walk that crosses each bridge exactly once becomes an **Eulerian path** (or trail). If it starts and ends at the same vertex, it is an **Eulerian circuit** (or tour).

![Königsberg bridges graph]({{ site.baseurl }}/img/chapter_img/konigsberg_bridges.svg)

*Figure. Schematic: land masses as vertices, bridges as edges. (If the local image is unavailable, draw four dots and seven connections matching any standard Königsberg diagram.)*

**What the model throws away.** Exact distances, angles, bridge widths, and the embedding in the plane beyond connectivity.  
**What the model keeps.** Incidence: which regions meet which bridges, and how many times.

This discard-and-keep step *is* the mathematics. Anyone trying to solve Königsberg by drawing a more accurate city map is working at the wrong level of abstraction.

---

### Short video: The seven bridges as a graph

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/konigsberg-bridges_en.mp4"></video>
</div>

Turn land into dots and bridges into edges, then count the degree of each dot. Four dots of odd degree rule out a walk that crosses every bridge exactly once.


### Try it yourself: Walk the bridges

<div class="mex-explainer" data-mex="konigsberg" data-lang="en"></div>


## 3. Degrees and the parity obstruction

The **degree** $$\deg(v)$$ of a vertex $$v$$ is the number of edge ends at $$v$$ (counting multiplicity). Every pass through an intermediate vertex consumes **two** edge ends (one in, one out), yielding:

- In an **Eulerian circuit**, every vertex must have **even degree**.  
- In an **Eulerian path** that is not closed, at most **two** vertices may have odd degree—the start and the finish.

In Königsberg’s standard model, all four vertices have odd degree (three of degree $$3$$ and one of degree $$5$$). Since $$4 > 2$$, no Eulerian path can exist. Euler’s rule in one line: *count the odd vertices; if there are more than two, stop.*

---

## 4. Explanation: Hand-Checking Königsberg’s Matrix, Adding One Bridge, and Assembling DNA

To feel how graph theory turns spatial puzzles into crisp algebra and modern algorithms, work through three concrete checks by hand:

### Worked Check 1: Königsberg’s $$4 \times 4$$ Adjacency Matrix
Label the four land masses $$A$$ (central Kneiphof island), $$B$$ (north bank), $$C$$ (south bank), and $$D$$ (eastern island). Record the number of bridges between every pair in a symmetric adjacency matrix $$M$$:

$$
M \;=\;
\begin{pmatrix}
0 & 2 & 2 & 1 \\
2 & 0 & 0 & 1 \\
2 & 0 & 0 & 1 \\
1 & 1 & 1 & 0
\end{pmatrix}
\begin{array}{l}
\leftarrow \text{Row } A:\ 0+2+2+1 = \mathbf{5}\ (\text{odd}) \\
\leftarrow \text{Row } B:\ 2+0+0+1 = \mathbf{3}\ (\text{odd}) \\
\leftarrow \text{Row } C:\ 2+0+0+1 = \mathbf{3}\ (\text{odd}) \\
\leftarrow \text{Row } D:\ 1+1+1+0 = \mathbf{3}\ (\text{odd})
\end{array}
$$

Sum all four rows: $$5 + 3 + 3 + 3 = 14 = 2 \times 7$$, matching the **Handshaking Lemma** $$\sum \deg(v) = 2\lvert E\rvert$$! With **4 odd vertices**, no Eulerian path exists.

### Worked Check 2: What If the City Builds Just ONE New Bridge Between $$B$$ and $$C$$?
Add $$+1$$ to entries $$(B, C)$$ and $$(C, B)$$ of $$M$$. Immediately:
- $$\deg(A) = 5$$ (odd),
- $$\deg(B) = 3 + 1 = 4$$ (even!),
- $$\deg(C) = 3 + 1 = 4$$ (even!),
- $$\deg(D) = 3$$ (odd).

Now only **2 odd vertices** remain ($$A$$ and $$D$$), so an open Eulerian path covering all 8 bridges is guaranteed! Verify an explicit 8-bridge route by hand:

$$
A \xrightarrow{\text{bridge } 1} B \xrightarrow{\text{bridge } 2} A \xrightarrow{\text{bridge } 3} C \xrightarrow{\text{bridge } 4} A \xrightarrow{\text{bridge } 5} D \xrightarrow{\text{bridge } 6} B \xrightarrow{\text{new bridge}} C \xrightarrow{\text{bridge } 7} D.
$$

Count the edges: all 8 bridges crossed exactly once! (Remarkably, bombing during World War II destroyed two of the original bridges in Kaliningrad, reducing the odd-degree count to $$2$$—so today an open Eulerian walk really is possible.)

### Worked Check 3: Assembling DNA Genomes via de Bruijn Graphs
Modern DNA sequencers shatter a genome into millions of tiny overlapping reads. Suppose a sequencer hands you four unordered 3-letter fragments (3-mers): `TGC`, `AAT`, `GCT`, `ATG`. How do you reconstruct the original strand?
- **Step 1:** Turn each 3-mer into a **directed edge** from its first two letters to its last two letters:
  `AAT` ($$AA \to AT$$), `ATG` ($$AT \to TG$$), `TGC` ($$TG \to GC$$), `GCT` ($$GC \to CT$$).
- **Step 2:** Check in-degrees and out-degrees of the 2-mer vertices: `AA` has (in 0, out 1), `CT` has (in 1, out 0), and every intermediate vertex `AT, TG, GC` has (in 1, out 1).
- **Step 3:** Follow the unique **directed Eulerian path** from `AA` to `CT`:
  $$AA \to AT \to TG \to GC \to CT \implies \text{reconstructed DNA: } \mathbf{AATGCT}.$$

Billion-base-pair genome assembly runs directly on Euler’s 1736 insight!

---

## 5. Worked contrasts

### A graph that works

Consider a square cycle: four vertices, four edges, every degree 2. An Eulerian circuit exists: walk around the square. Add one diagonal: two vertices gain degree 3 (odd). An Eulerian path exists starting at one odd vertex and ending at the other, but no Eulerian circuit exists.

### A graph that fails like Königsberg

Any connected graph with four odd-degree vertices fails the path criterion. You need not inspect all possible walks; the invariant forbids them all at once.

### Handshaking lemma (supporting fact)

$$
\sum_{v\in V}\deg(v) = 2\lvert E\rvert.
$$

Consequently the number of odd-degree vertices is always even. Seeing four odd degrees is legal—and still non-Eulerian.

---

## 6. Sufficiency, briefly (so the criterion feels complete)

<div class="textbook-theorem" markdown="1">
**Theorem (classical, idea).** Let $$G$$ be a connected multigraph (more precisely: the edges lie in a single nontrivial connected component). Then:

- $$G$$ has an Eulerian circuit if and only if every vertex has even degree;  
- $$G$$ has an Eulerian path if and only if exactly zero or two vertices have odd degree (zero for the circuit case).
</div>

**Sufficiency idea.** Start at an odd vertex if one exists, otherwise anywhere; walk unused edges without repetition until stuck; if unused edges remain, splice in a circuit (Hierholzer’s algorithm). The degree criteria are the true heart.

---

## 7. Why it matters

- **Birth of graph theory.** Problems about networks become theorems about vertices and edges.  
- **Topology’s combinatorial face.** Properties independent of continuous deformation of the riverbanks.  
- **Algorithms.** Eulerian tours power de Bruijn genome assembly, snowplow and mail routing, PCB plotting, and single-stroke laser cutting.  
- **Proof culture.** Impossibility proofs via invariants (parity of degree) are a reusable template: find a quantity every successful object must have, then show the instance lacks it.

---

## 8. Beyond bridges: Chinese Postman and modern cousins

If all degrees are even, an Eulerian circuit is a perfect postal tour. If odd degrees exist, the **Chinese Postman Problem** asks for the shortest closed walk covering every edge at least once—equivalently, add a minimum-cost set of duplicate edges to pair odd vertices, then run an Eulerian circuit in the augmented graph. Königsberg is the special case forbidding duplication entirely.

---

## Common confusions

1. **“Euler proved you cannot visit every land mass.”** — Wrong target: the issue is covering **bridges (edges)**, not vertices. Hamiltonian paths (visit vertices once) are a different, harder story.  
2. **“If I draw the map more carefully, a path might appear.”** — The obstruction is invariant under redrawing.  
3. **“Odd degree means the city is disconnected.”** — No; degree parity is not connectivity.  
4. **“Four odd vertices contradict the handshaking lemma.”** — No; four is even, so it is allowed.  
5. **“Idea of proof means we skip the definition of walk.”** — We still need clear definitions; we skip only metric geometry.

---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/euler-konigsberg/analysis.md`.

### Status

**Proved** (Euler 1736 necessity; full sufficiency of Eulerian criteria completed later, Hierholzer). Founding theorem of graph theory.

### Core statement / slogan

A connected graph has an Eulerian circuit iff every vertex has even degree; an Eulerian trail iff exactly 0 or 2 odd-degree vertices. Königsberg multigraph has four odd vertices → impossible.

### Definitions to freeze

- **Degree.** Number of edge ends at a vertex (loops contribute 2).
- **Eulerian circuit / trail.** Closed / open walk using each edge exactly once.

### Hygiene (from confusions log)

- Thinking the answer depends on bridge lengths or geometry (only incidence matters).
- Mixing Hamiltonian (vertices once) with Eulerian (edges once).


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/euler-konigsberg/`.

**Recommended order**

1. **Orientation** — Numberphile — Seven Bridges of Königsberg (Cliff Stoll): [https://www.youtube.com/watch?v=W18FDEA1jRQ](https://www.youtube.com/watch?v=W18FDEA1jRQ).  
2. **Orientation** — TED-Ed — How the Königsberg bridge problem changed mathematics: [https://www.youtube.com/watch?v=nZwSo4vfw6c](https://www.youtube.com/watch?v=nZwSo4vfw6c).  
3. **Foundation** — Sarada Herke — Graph Theory: Seven Bridges of Konigsberg: [https://www.youtube.com/watch?v=eIb1cz06UwI](https://www.youtube.com/watch?v=eIb1cz06UwI).  
4. **Core** — Dr. Trefor Bazett — Euler Paths & 7 Bridges: [https://www.youtube.com/watch?v=dSK5jTEe-AM](https://www.youtube.com/watch?v=dSK5jTEe-AM).  

**Status reminder:** **Proved** (Euler 1736 necessity; full sufficiency of Eulerian criteria completed later, Hierholzer). Founding theorem of graph theory.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/euler-konigsberg/transcripts/` · status: `research/video-research/euler-konigsberg/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/euler-konigsberg_W18FDEA1jRQ_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

1. Euler, L. (1736). memoir on the Königsberg bridges (various translations/reprints).  
2. Any introductory graph theory text: sections on Eulerian paths (e.g. Bondy–Murty; Diestel; or discrete math surveys).  
3. Historical essays on early graph theory and topology.  
4. Course context: modeling proofs alongside [Four Color]({{ site.baseurl }}/contents/en/chapter05/05_07_Four_Color_Proof/) (planar graphs) in this chapter.

---


Full URL bibliography from video research: `research/video-research/euler-konigsberg/references.md`.

### Videos (recommended path)

- Numberphile — Seven Bridges of Königsberg (Cliff Stoll) (ORIENTATION): https://www.youtube.com/watch?v=W18FDEA1jRQ
- TED-Ed — How the Königsberg bridge problem changed mathematics (ORIENTATION): https://www.youtube.com/watch?v=nZwSo4vfw6c
- Sarada Herke — Graph Theory: Seven Bridges of Konigsberg (FOUNDATION): https://www.youtube.com/watch?v=eIb1cz06UwI
- Dr. Trefor Bazett — Euler Paths & 7 Bridges (CORE): https://www.youtube.com/watch?v=dSK5jTEe-AM

### Papers and web (from research pack)

- Wikipedia — Seven Bridges of Königsberg: https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg
- MathWorld — Königsberg Bridge Problem: https://mathworld.wolfram.com/KoenigsbergBridgeProblem.html
- Euler 1736 paper (historical translations / surveys): https://en.wikipedia.org/wiki/Leonhard_Euler
- Mathigon course — Bridges of Königsberg: https://mathigon.org/course/graph-theory/bridges
- Numberphile page: https://www.numberphile.com/videos/the-seven-bridges-of-knigsberg

### Course

- Research pack: `research/video-research/euler-konigsberg/` (especially `references.md`, `learning_path.md`).

## Further directions

- Read Hierholzer’s algorithm and implement it on a small multigraph.  
- Explore the Chinese Postman Problem as the natural optimization sequel.  
- Contrast edge-cover tours with vertex-cover tours (Hamilton) to feel complexity’s jump.  
- Note one precise question you still have—good questions are part of mathematical practice.

## Video tham khảo

- **xem trước** — [The Seven Bridges of Königsberg - Numberphile](https://www.youtube.com/watch?v=W18FDEA1jRQ) — Numberphile, English. Watch first. “The Seven Bridges of Königsberg - Numberphile” orients the lesson’s aim: Model a bridge (or road) system as a multigraph with vertices for regions and edges for crossings.
- [How the Königsberg bridge problem changed mathematics - Dan Van der Vieren](https://www.youtube.com/watch?v=nZwSo4vfw6c) — TED-Ed, English. A second pass once the main claim is in view: Model a bridge (or road) system as a multigraph with vertices for regions and edges for crossings.
- [Graph Theory: 01. Seven Bridges of Konigsberg](https://www.youtube.com/watch?v=eIb1cz06UwI) — Sarada Herke, English. Further depth after the first two, still tied to this lesson: Model a bridge (or road) system as a multigraph with vertices for regions and edges for crossings.
