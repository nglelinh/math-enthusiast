---
layout: post
title: "The Four Color Theorem (Proof Ideas)"
chapter: '05'
order: 7
owner: Nguyen Le Linh
lang: en
categories:
- chapter05
---

In London in 1852, a young graduate named **Francis Guthrie** was coloring a map of the counties of England so that no two bordering counties shared a color. A question simple enough for a ten-year-old suddenly struck him: *are four colors always enough for **every** possible flat map?*

Nobody guessed that this innocent crayon puzzle would torment mathematicians for **124 years**. In 1879, barrister and mathematician Alfred Kempe published an elegant proof and the world celebrated—until eleven years later, Percy Heawood uncovered a subtle fatal flaw hidden in Kempe’s color-swapping chains (the argument sufficed for **Five Colors**, not Four!). Only in 1976 did **Kenneth Appel** and **Wolfgang Haken** close the case by enlisting a computer to audit nearly two thousand local configurations—making the Four Color Theorem the first major theorem whose proof made **essential use of a computer**.

**Lesson roadmap:** Key ideas (planar graphs, duality, Euler’s formula, formal verification in Coq) → Statement and the $$K_4/K_5$$ intuition trap → Minimal counterexamples and unavoidable sets → Explanation: deriving $$\sum (6 - \deg(v)) = 12$$ by hand, checking platonic solids, and tracing Kempe’s 5-color chain swap → Discharging and formal verification.

---

## Learning objectives

After this lecture you should be able to:

- State the Four Color Theorem in map form and graph form (planar graph vertex coloring dualized carefully).
- Explain the strategy: minimal counterexample, unavoidable sets, reducible configurations, discharging.
- Describe the division of labor between human insight and machine enumeration.
- Distinguish four colors (true) from “three colors for all planar graphs” (false) and from five colors (easier classical theorem).
- Discuss, briefly and fairly, what computer-assisted proof changed about mathematical knowledge.
- Avoid confusions about maps on other surfaces and about algorithmic map coloring in practice.

**Prerequisites.** Informal idea of a planar graph; what a finite case analysis is. No need to run the 1976 code.

---

## Key ideas: Planar Graphs, Chromatic Number, and Computer-Assisted Proofs

Before diving into discharging and reducibility, anchor the theorem in three pillars of university discrete mathematics and computer science:

### 1. Planar Graphs, Duality, and Euler’s Formula
A graph is **planar** if it can be drawn on a flat sheet without any two edges crossing. Every political map turns into a planar graph by **duality**: drop one vertex into each country’s capital and draw an edge between any two countries sharing a positive-length border. Coloring countries becomes coloring vertices so adjacent vertices differ. Every connected planar graph obeys **Euler’s formula**:

$$
V - E + F = 2,
$$

where $$V$$ counts vertices, $$E$$ counts edges, and $$F$$ counts faces (including the unbounded outer region). That single identity forces every simple planar graph to contain at least one vertex of degree $$\le 5$$.

### 2. Chromatic Number ($$\chi(G)$$) and Reducibility
The **chromatic number** $$\chi(G)$$ is the minimum number of colors needed to color the vertices of $$G$$ properly. Far beyond cartography, graph coloring models **compiler register allocation** (variables alive at the same time cannot share a CPU register), **exam timetabling**, and **radio-frequency assignment** for cell towers. The Four Color Theorem asserts $$\chi(G) \le 4$$ for every planar graph.

### 3. Computer-Assisted Proof vs. Formal Verification (Coq)
Appel and Haken’s 1976 proof checked 1,936 configurations by computer, sparking a fierce philosophical debate: *what if the code had a bug?* In 2005, Georges Gonthier formalized the entire proof inside the **Coq** proof assistant, where a tiny logical kernel audited every single deduction down to the axioms—turning a controversial case-bash into one of the most thoroughly audited theorems in mathematics.

---

## 1. Statement, dual graph picture — and the $$K_4/K_5$$ intuition trap

Try drawing a map that forces as many colors as possible on paper. Three mutually touching countries are easy (3 colors). Wrap a fourth country touching all three—that is the complete graph $$K_4$$, forcing 4 colors. Now try adding a fifth country touching *all four* without tunneling through the paper: you get trapped immediately because $$K_5$$ is **non-planar**!

That creates a tempting—but **false**—intuition: *"since five countries can never all touch each other, four colors must obviously suffice."* In graph theory, there exist graphs containing *no triangles at all* (no $$K_3$$!) that still require 4, 5, or 100 colors! Color constraints can ripple across a map in long interlocking chains—and it was precisely two crossing **Kempe chains** that broke Kempe’s famous 1879 proof.

**Four Color Theorem.** Every planar map (or equivalently, every planar graph) is **4-colorable**: adjacent regions sharing a positive-length border (not merely a point) can be colored with at most four colors so no two neighbors match. Five colors suffice by Heawood’s classical theorem (1890); three colors fail on $$K_4$$; so four is sharp.

---

## 2. Why a direct attack is hard

There are infinitely many planar maps. A proof must either find a structural reason why four colors always stretch far enough, or collapse the infinite universe into a **finite** checklist of unavoidable local situations. Appel and Haken (and later Robertson–Sanders–Seymour–Thomas) took the second path, repairing and vastly extending Kempe’s nineteenth-century vision.

---

## 3. Minimal counterexamples and unavoidable sets

Assume, for contradiction, that some planar graphs are not 4-colorable, and pick a **minimal counterexample** $$G$$ (fewest vertices): $$G$$ itself cannot be 4-colored, yet every smaller planar graph *can*.

- **Reducible configuration:** A local pattern that cannot appear in $$G$$, because its presence would let us lift a 4-coloring of a smaller planar graph into a 4-coloring of $$G$$.
- **Unavoidable set:** A finite list $$\mathcal{U} = \{C_1, \ldots, C_N\}$$ such that **every** minimal counterexample must contain at least one $$C_i \in \mathcal{U}$$.

If every configuration in an unavoidable set $$\mathcal{U}$$ is reducible, then no minimal counterexample can exist—proving the theorem!

---

## 4. Explanation: Deriving the "Charge" Equation and Running a Kempe Chain by Hand

To see how *discharging* and *Kempe chains* actually work with pen and paper, verify three concrete steps:

### Step 1: Derive the Discharging Identity $$\sum (6 - \deg(v)) = 12$$ by Hand
Assume $$G$$ is a planar **triangulation** (add edges until every face is a triangle—adding edges only makes coloring harder, so 4-coloring triangulations implies 4-coloring all planar graphs).
1. Each triangular face has $$3$$ edges and each edge borders $$2$$ faces, so $$3F = 2E \implies F = \frac{2}{3}E$$.
2. Substitute $$F = \frac{2}{3}E$$ into Euler’s formula $$V - E + F = 2$$:
   $$
   V - E + \frac{2}{3}E = 2 \;\implies\; V - \frac{1}{3}E = 2 \;\implies\; 6V - 2E = 12.
   $$
3. Apply the Handshaking Lemma $$2E = \sum_{v \in V} \deg(v)$$:
   $$
   \sum_{v \in V} \bigl(6 - \deg(v)\bigr) = 12.
   $$

**Hand-check on three familiar polyhedra:**

| Triangulated planar graph | $$V$$ | $$E$$ | $$F$$ | Check $$V - E + F$$ | Vertex degrees | Total charge $$\sum (6 - \deg(v))$$ |
|---------------------------|-------|-------|-------|---------------------|----------------|-------------------------------------|
| **Tetrahedron ($$K_4$$)** | $$4$$ | $$6$$ | $$4$$ | $$4 - 6 + 4 = 2$$ | All degree $$3$$ | $$4 \times (6 - 3) = \mathbf{12}$$ |
| **Octahedron** | $$6$$ | $$12$$ | $$8$$ | $$6 - 12 + 8 = 2$$ | All degree $$4$$ | $$6 \times (6 - 4) = \mathbf{12}$$ |
| **Icosahedron** | $$12$$ | $$30$$ | $$20$$ | $$12 - 30 + 20 = 2$$ | All degree $$5$$ | $$12 \times (6 - 5) = \mathbf{12}$$ |

Because the total "charge" is always **$$+12 > 0$$**, **at least one vertex must have degree $$\le 5$$** (if every vertex had degree $$\ge 6$$, the sum would be $$\le 0$$!).

### Step 2: Reduce Degree $$\le 3$$ (for 4 Colors) and Degree $$5$$ (for 5 Colors) by Hand
- **Degree $$\le 3$$:** If $$G$$ has a vertex $$v$$ with $$\le 3$$ neighbors, delete $$v$$, 4-color the smaller graph $$G - v$$, and reinsert $$v$$: its $$\le 3$$ neighbors use at most $$3$$ colors, leaving at least $$1$$ free color for $$v$$! Thus degree $$\le 3$$ is immediately reducible.
- **Degree $$5$$ (Five Color Theorem by hand):** Suppose we have 5 colors (Red, Blue, Green, Yellow, Purple) and $$v$$ has 5 clockwise neighbors $$v_1$$ (Red), $$v_2$$ (Blue), $$v_3$$ (Green), $$v_4$$ (Yellow), $$v_5$$ (Purple).
  - Follow the connected subgraph of **Red and Green** vertices starting at $$v_1$$ (the **Red–Green Kempe chain**).
  - *Case A:* The chain **misses $$v_3$$**. Swap Red $$\leftrightarrow$$ Green along that chain: $$v_1$$ becomes Green while all other neighbors keep their colors—freeing Red for $$v$$!
  - *Case B:* The chain **reaches $$v_3$$**. By planarity, the Red–Green chain plus $$v_1 - v - v_3$$ forms a **closed wall** separating $$v_2$$ (Blue) inside from $$v_4$$ (Yellow) outside! Hence the **Blue–Yellow** chain from $$v_2$$ **cannot cross the wall to reach $$v_4$$**—swap Blue $$\leftrightarrow$$ Yellow around $$v_2$$ to free Blue for $$v$$!

### Step 3: Why 4 Colors Breaks Kempe’s Trick—and Requires Discharging
With only 4 colors, the 5 neighbors of $$v$$ must repeat a color (say $$v_1, v_3$$ are both Red while $$v_2, v_4, v_5$$ hold the other 3 colors). Trying to run *two* Kempe swaps simultaneously lets the first swap tangle and break the wall protecting the second (Kempe’s 11-year flaw!). Because a single degree-5 vertex is no longer reducible for 4 colors, Appel and Haken designed **discharging rules**—redistributing the $$+1$$ charge of degree-5 vertices toward negatively charged high-degree neighbors while preserving total charge $$+12 > 0$$—to force the graph to contain at least one of **1,936 larger clusters**, each audited as reducible by computer!

---

## 5. Discharging (the human-designed engine)

Designing the discharging rules and the configuration list is deep combinatorial craft. Verifying reducibility became a machine-checkable mountain of cases: **1,936 configurations** in Appel–Haken (1976), trimmed to **633 configurations** in Robertson–Sanders–Seymour–Thomas (1997), and fully formalized inside **Coq** by Georges Gonthier and collaborators (2005).

---

## 6. The idea of the proof, one page

1. Reformulate map coloring as planar graph 4-coloring.  
2. Assume a minimal counterexample $$G$$.  
3. Exhibit a finite unavoidable set $$\mathcal{U}$$ of configurations (via discharging + Euler’s $$\sum(6-\deg(v)) = 12$$).  
4. Prove each configuration in $$\mathcal{U}$$ is reducible (case analysis; computer-assisted).  
5. Conclude no minimal counterexample exists; every planar graph is 4-colorable.

Human insight designs $$\mathcal{U}$$ and the discharging scheme; machines (or proof assistants) audit the finite explosion of local coloring cases.

---

## 7. Computer-assisted proof and later verification

Appel–Haken’s 1976 announcement forced a debate: is an unreadable case bash a proof? Over time the community accepted computer-assisted proofs when the algorithm is clearly specified, reproducible, and independently verified. The 1997 simplification and Gonthier’s 2005 Coq formalization made the finite reasoning **auditably airtight**. The methodological moral sits beside the combinatorial one: *proof ideas can include the design of a finite verification task.*

---

## 8. What the theorem does *not* say

- It does not claim every map on every surface is 4-colorable; genus changes the chromatic number (on a donut/torus, some maps genuinely require **7 colors**!).  
- It does not give the fastest practical algorithm for all instances.  
- It does not say four colors are needed for *every* map—only that four always suffice and three do not.  
- It is not the same as the **Five Color Theorem**, which has a short classical proof.

---

## Common confusions

1. **“The computer randomly verified maps.”** — No: it checked mathematical reducibility cases for configurations in a finite list.  
2. **“Humans did not prove anything.”** — Humans designed discharging, unavoidability, and reducibility notions.  
3. **“Four colors for planar graphs means four colors for all graphs.”** — Completely false; non-planar graphs can need arbitrarily many colors.  
4. **“Countries meeting at a point must get different colors.”** — Standard statement uses border segments, not point touches.  
5. **“Idea of proof means skip finite checklists.”** — The checklist *is* the proof’s spine; “idea” means understanding why the checklist works.

---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/four-color-proof/analysis.md`.

### Status

**Proved** (Appel–Haken 1976; simplified/verified later, Robertson et al., computer-checked formalizations). Philosophical debate about computer proofs is separate from theorem status.

### Core statement / slogan

Every planar graph is 4-colorable (equivalently, every map on the plane/sphere can be colored with 4 colors so adjacent regions differ). Proof architecture: unavoidable set of reducible configurations + discharging.

### Definitions to freeze

- **Planar graph.** Graph drawable in the plane without edge crossings.
- **Reducible configuration.** Local pattern that cannot appear in a minimal counterexample.

### Hygiene (from confusions log)

- Thinking 4 colors are needed for *every* map (many need fewer; 4 is worst-case bound).
- Conflating 'computer-assisted' with 'unverified' after modern checks.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/four-color-proof/`.

**Recommended order**

1. **Orientation** — Numberphile — Four Color Map Theorem (James Grime): [https://www.youtube.com/watch?v=NgbK43jB4rQ](https://www.youtube.com/watch?v=NgbK43jB4rQ).  
2. **Core** — Quanta — Math's Map Coloring Problem / first computer-assisted proof: [https://www.youtube.com/watch?v=h7kqlYUV1l8](https://www.youtube.com/watch?v=h7kqlYUV1l8).  
3. **Hygiene** — Up and Atom — Four Color Theorem: What Counts as a Proof?: [https://www.youtube.com/watch?v=42-ws3bkrKM](https://www.youtube.com/watch?v=42-ws3bkrKM).  
4. **Secondary** — Numberphile2 — Four Color extra footage: [https://www.youtube.com/watch?v=laMkuPrad3s](https://www.youtube.com/watch?v=laMkuPrad3s).  

**Status reminder:** **Proved** (Appel–Haken 1976; simplified/verified later, Robertson et al., computer-checked formalizations). Philosophical debate about computer proofs is separate from theorem status.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/four-color-proof/transcripts/` · status: `research/video-research/four-color-proof/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/four-color-proof_NgbK43jB4rQ_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

1. Appel, K. & Haken, W. (1977). Every planar map is four colorable. *Illinois J. Math.*  
2. Robertson, N., Sanders, D., Seymour, P., & Thomas, R. (1997). The four-colour theorem. *J. Combin. Theory Ser. B.*  
3. Gonthier, G. Formal proof of the Four Color Theorem (Coq); related papers and Microsoft Research reports.  
4. Historical surveys on Kempe’s attempt and Heawood’s five-color theorem.  
5. Course: [Euler–Königsberg]({{ site.baseurl }}/contents/en/chapter05/05_05_Euler_Konigsberg/) for combinatorial modeling.

---


Full URL bibliography from video research: `research/video-research/four-color-proof/references.md`.

### Videos (recommended path)

- Numberphile — Four Color Map Theorem (James Grime) (ORIENTATION): https://www.youtube.com/watch?v=NgbK43jB4rQ
- Quanta — Math's Map Coloring Problem / first computer-assisted proof (CORE): https://www.youtube.com/watch?v=h7kqlYUV1l8
- Up and Atom — Four Color Theorem: What Counts as a Proof? (HYGIENE): https://www.youtube.com/watch?v=42-ws3bkrKM
- Numberphile2 — Four Color extra footage (SECONDARY): https://www.youtube.com/watch?v=laMkuPrad3s

### Papers and web (from research pack)

- Wikipedia — Four color theorem: https://en.wikipedia.org/wiki/Four_color_theorem
- Appel & Haken historical account (survey pages): https://en.wikipedia.org/wiki/Kenneth_Appel
- Robertson, Sanders, Seymour, Thomas — new proof survey (1997 era): https://en.wikipedia.org/wiki/Four_color_theorem#Simplification_and_verification
- Numberphile page: https://www.numberphile.com/videos/the-four-color-map-theorem
- Quanta Magazine related articles (map coloring / computer proofs): https://www.quantamagazine.org/

### Course

- Research pack: `research/video-research/four-color-proof/` (especially `references.md`, `learning_path.md`).

## Further directions

- Read a careful exposition of discharging with a tiny toy unavoidable set (many graph theory notes include micro-examples).  
- Explore chromatic numbers of graphs on the torus and other surfaces.  
- Sample how proof assistants encode finite case distinctions.  
- Note one precise question you still have—good questions are part of mathematical practice.

## Video tham khảo

- **xem trước** — [The Four Color Map Theorem - Numberphile](https://www.youtube.com/watch?v=NgbK43jB4rQ) — Numberphile, English. Watch first. “The Four Color Map Theorem - Numberphile” orients the lesson’s aim: State the Four Color Theorem in map form and graph form (planar graph vertex coloring dualized carefully).
- [The Map Coloring Puzzle That Changed Mathematics](https://www.youtube.com/watch?v=h7kqlYUV1l8) — Quanta Magazine, English. A second pass once the main claim is in view: State the Four Color Theorem in map form and graph form (planar graph vertex coloring dualized carefully).
- [The Four Color Theorem - What Counts as a Proof?](https://www.youtube.com/watch?v=42-ws3bkrKM) — Up and Atom, English. Further depth after the first two, still tied to this lesson: State the Four Color Theorem in map form and graph form (planar graph vertex coloring dualized carefully).
