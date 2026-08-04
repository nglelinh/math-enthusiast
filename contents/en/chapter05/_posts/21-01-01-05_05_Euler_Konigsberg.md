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

In eighteenth-century Königsberg (now Kaliningrad), seven bridges connected two islands and the mainland banks of the Pregel River. Citizens asked a recreational question with serious mathematical offspring: *Is there a walk through the city that crosses each bridge exactly once?* **Leonhard Euler** proved that no such walk exists—and in doing so helped invent **graph theory**. The geometry of the river almost does not matter; what matters is how land masses are connected. This lecture develops the **idea of the proof**: model, reduce to degrees, and read off an obstruction.

The moral travels far beyond one city. Whenever a problem is really about incidence and traversal—networks, circuits, routing, molecular graphs—the Königsberg move is available: discard irrelevant geometry, keep the combinatorial skeleton, and reason about parity.

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

## 1. The historical puzzle

Königsberg’s layout can be sketched as four land regions:

- the north bank $$A$$,  
- the south bank $$B$$,  
- island $$C$$,  
- island (or kneiphof-style central island) $$D$$—

with seven bridges joining them. Different historical maps label regions differently; the combinatorial data that matter are stable: **four regions, seven bridges, and four vertices of odd degree** in the natural model.

The recreational challenge is not to minimize distance or avoid mud. It is a pure existence question about **traversing each bridge once**. Euler’s 1736 memoir is often cited as a founding document of graph theory and of topology’s combinatorial side: properties preserved when shape is ignored.

---

## 2. The modeling idea

Replace each land mass by a **vertex**. Replace each bridge by an **edge** joining the vertices of the lands it connects. Multiple bridges between the same pair of lands become **multiple edges**. The city becomes a **multigraph** $$G=(V,E)$$.

A walk that crosses each bridge exactly once becomes a walk that uses each edge exactly once: an **Eulerian path** (also called an Eulerian trail). If the walk starts and ends at the same vertex, it is an **Eulerian circuit** (Eulerian tour).

![Königsberg bridges graph]({{ site.baseurl }}/img/chapter_img/konigsberg_bridges.svg)

*Figure. Schematic: land masses as vertices, bridges as edges. (If the local image is unavailable, draw four dots and seven connections matching any standard Königsberg diagram.)*

**What the model throws away.** Exact distances, angles, bridge widths, and the embedding in the plane beyond connectivity.  
**What the model keeps.** Incidence: which regions meet which bridges, and how many times.

This discard-and-keep step *is* the mathematics. Students who try to solve Königsberg by drawing ever more careful city maps are working in the wrong category.

---

## 3. Degrees and the parity obstruction

The **degree** $$\deg(v)$$ of a vertex $$v$$ is the number of edge ends at $$v$$ (counting multiplicity; loops would contribute two, though Königsberg needs no loops).

### Local necessary condition

Imagine walking through the graph using each edge once. Every time you enter a vertex by an edge and leave by another, you consume **two** edge ends at that vertex. Therefore, at every intermediate visit pattern, edges at a vertex pair up as enter/leave.

More globally:

- In an **Eulerian circuit**, every vertex must have **even degree**: the tour pairs incident edges perfectly at every vertex.  
- In an **Eulerian path** that is not closed, exactly **two** vertices may have odd degree—the start and the end—where a single unpaired edge end is used to begin or finish. All other vertices must have even degree.

These conditions are not only necessary but, for connected graphs, essentially sufficient (with the usual connectedness hypothesis on the subgraph of edges). The sufficiency direction is a separate constructive argument (Hierholzer’s algorithm and classical theorems). For Königsberg, **necessity alone** kills the hope.

### Königsberg’s degrees

In the standard model of the seven bridges, all four vertices have odd degree (typically three vertices of degree 3 and one of degree 5, or an equivalent odd-degree multiset depending on exact historical labeling—what matters is that **four degrees are odd**). A connected graph cannot have an Eulerian path if it has more than two odd-degree vertices. Hence Königsberg admits no walk crossing each bridge exactly once.

Euler’s insight is often summarized: *count the odd vertices; if there are more than two, stop.*

---

## 4. The idea of the proof, compressed

1. **Model** land and bridges as a multigraph.  
2. **Translate** the tourist’s demand into existence of an Eulerian path.  
3. **Derive** the degree parity constraints from enter/leave pairing.  
4. **Compute** degrees for Königsberg; observe four odd degrees.  
5. **Conclude** impossibility.

No coordinate geometry, no continuous motion, no measurement. The proof is combinatorial and local-to-global: local pairing forces global parity restrictions.

---

## 5. Worked contrasts

### A graph that works

Consider a square cycle: four vertices, four edges, every degree 2. An Eulerian circuit exists: walk around the square.  
Add one diagonal: two vertices gain degree 3 (odd). An Eulerian path exists starting at one odd vertex and ending at the other, but no Eulerian circuit exists.

### A graph that fails like Königsberg

Any connected graph with four odd-degree vertices fails the path criterion. You need not inspect all possible walks; the invariant forbids them all at once. That is the power of an obstruction: it is a certificate of impossibility.

### Handshaking lemma (supporting fact)

The sum of degrees equals twice the number of edges:

$$
\sum_{v\in V}\deg(v) = 2\lvert E\rvert.
$$

Consequently the number of odd-degree vertices is always even. Seeing four odd degrees is consistent with this lemma; seeing three would be impossible for any graph. Königsberg’s data are graph-theoretically legal—and still non-Eulerian for trails that cover every edge.

---

## 6. Sufficiency, briefly (so the criterion feels complete)

**Theorem (classical, idea).** Let $$G$$ be a connected multigraph (more precisely: the edges lie in a single nontrivial connected component). Then:

- $$G$$ has an Eulerian circuit if and only if every vertex has even degree;  
- $$G$$ has an Eulerian path if and only if exactly zero or two vertices have odd degree (zero for the circuit case).

**Sufficiency idea.** Start at an odd vertex if one exists, otherwise anywhere; walk unused edges without repetition until stuck; one can show you are at the appropriate endpoint; if unused edges remain, they form a subgraph with even degrees, and one splices in a circuit (Hierholzer). The details are standard in any first graph theory chapter; the seminar takeaway is that the degree conditions are the true heart.

---

## 7. Why it matters

- **Birth of graph theory.** Problems about networks become theorems about vertices and edges.  
- **Topology’s combinatorial face.** Properties independent of continuous deformation of the riverbanks.  
- **Algorithms.** Eulerian tours appear in genome assembly slogans, routing, and plotting machines that should not lift a pen.  
- **Proof culture.** Impossibility proofs via invariants (parity of degree) are a template: find a quantity every successful object must have; show the instance lacks it.

The pedagogical power of Königsberg is that students can *draw* the obstruction. Unlike many impossibility results that hide behind long calculations, here the certificate is a handful of odd numbers written next to dots. That transparency is why the example still opens graph theory courses three centuries later: it teaches modeling, invariants, and clean negative proofs in one sitting.

A second moral concerns **abstraction ethics**. Throwing away the river’s beauty is not a loss of meaning; it is a gain of transfer. The same degree criterion decides whether a postal worker can traverse every street without retracing, whether a robot can mow every edge of a campus graph, and whether a certain DNA assembly graph has a path that reconstructs a genome. One proof idea, many surface stories.

---

## 8. Beyond bridges: Chinese Postman and modern cousins

If all degrees are even, an Eulerian circuit is a perfect postal tour. If odd degrees exist, the **Chinese Postman Problem** asks for the shortest closed walk covering every edge at least once—equivalently, add a minimum-cost set of duplicate edges to pair odd vertices, then run an Eulerian circuit in the augmented graph. Königsberg is the special case where one forbids duplication entirely and asks existence. The generalization shows how a negative classical answer seeds a positive optimization theory.

---

## Common confusions

1. **“Euler proved you cannot visit every land mass.”** — Wrong target: the issue is covering **bridges (edges)**, not vertices. Hamiltonian paths (visit vertices once) are a different, harder story.  
2. **“If I draw the map more carefully, a path might appear.”** — The obstruction is invariant under redrawing.  
3. **“Odd degree means the city is disconnected.”** — No; degree parity is not connectivity.  
4. **“Four odd vertices contradict the handshaking lemma.”** — No; four is even, so it is allowed.  
5. **“Idea of proof means we skip the definition of walk.”** — We still need clear definitions; we skip only metric geometry.

---

## Exercises

1. Draw the Königsberg multigraph, label degrees, and write a three-sentence impossibility proof.  
2. Invent a connected multigraph with exactly two odd-degree vertices and exhibit an Eulerian path.  
3. Prove that the number of odd-degree vertices in any finite graph is even, using $$\sum\deg=2\lvert E\rvert$$.  
4. Does there exist a graph with exactly one odd-degree vertex? Why or why not?  
5. Distinguish carefully: Eulerian path vs Hamiltonian path. Give a tiny graph that has one but not the other.  
6. **Modeling.** Translate a floor-plan with corridors into a graph so that “walk each corridor once” becomes an Eulerian question.  
7. **Narrative (≤300 words).** Explain to a tourist why no bridge tour exists without using the word “theorem.”

---


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
