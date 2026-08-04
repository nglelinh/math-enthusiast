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

The **Four Color Theorem** asserts that every planar map can be colored with at most four colors so that adjacent regions receive different colors. Stated in the nineteenth century and proved only in 1976 by **Kenneth Appel** and **Wolfgang Haken**, it was the first major theorem whose proof made **essential use of a computer**. The human contribution was not eliminated; it was reorganized. This lecture develops the **idea of the proof**: reduce an infinite family of maps to a finite checklist of configurations, show that some configuration from an “unavoidable set” must appear, and show each such configuration is “reducible” so it cannot appear in a minimal counterexample.

The philosophical aftershock still matters: What counts as a proof when no human reads every case? Later formal verifications in proof assistants partly answer by checking the finite reasoning inside a trusted kernel.

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

## 1. Statement and dual graph picture

**Four Color Theorem.** The countries of any political map drawn in the plane (or on a sphere), where each country is a connected region and adjacency means sharing a positive-length border (not merely a point), can be colored with four colors so that adjacent countries differ in color.

Graph-theoretically, one usually dualizes: place a vertex in each country and an edge between vertices of countries that share a border. The result is a **planar graph**, and the theorem becomes: every planar graph is **4-colorable** (vertices colored so adjacent vertices differ). Technical hygiene handles multiple edges, the connectivity of countries, and the precise meaning of adjacency; the idea-level statement is stable.

Five colors suffice by a classical theorem of Heawood (and earlier work in the lineage of Kempe). Three colors do **not** suffice for every planar graph: odd wheels and other examples require four. So four is the sharp universal number for the plane.

---

## 2. Why a direct attack is hard

There are infinitely many planar maps. A proof must either:

- find a structural reason that four colors always stretch far enough, or  
- reduce the infinite landscape to a **finite** set of situations that cover all possibilities.

The Appel–Haken proof (and its successors) take the second path, in the tradition of Kempe’s nineteenth-century attempts. Kempe’s published proof of the Four Color Conjecture was flawed; the flaw taught later generations which reductions were delicate. The successful proof repairs and vastly extends the configuration-and-discharging technology.

---

## 3. Minimal counterexamples

Assume, for contradiction, that some planar graphs are not 4-colorable. Among counterexamples, choose a **minimal** one—typically minimal number of vertices. A minimal counterexample has useful properties: it is hard to color, yet every smaller planar graph *is* 4-colorable. Therefore if one can show that a certain local piece of the graph can be collapsed or recolored using colors available from a smaller graph, that piece cannot occur in a minimal counterexample.

This is the logic of **reducibility**: a configuration is reducible if its presence would allow a 4-coloring of the whole graph to be built from a 4-coloring of a smaller graph, contradicting minimality of a counterexample that contains it.

---

## 4. Unavoidable sets

An **unavoidable set** of configurations is a list $$\mathcal{U}=\{C_1,\ldots,C_N\}$$ such that **every** minimal counterexample (or every graph in the class under study) must contain at least one $$C_i$$ as a subgraph in a specified way.

If every configuration in an unavoidable set is reducible, then no minimal counterexample can exist: it would have to contain a reducible configuration, which minimal counterexamples cannot. That contradiction proves the theorem.

The entire strategy collapses to two finite claims:

1. **Unavoidability:** every candidate minimal counterexample contains some $$C_i\in\mathcal{U}$$.  
2. **Reducibility:** each $$C_i$$ is reducible.

Claim 2, for large lists, is where computers shine: each configuration requires checking many coloring extensions and recoloring arguments. Claim 1 is often proved by a **discharging method**, a bookkeeping scheme on vertex degrees and face structures that shows “too sparse” graphs are impossible and “everyone must carry a dense local pattern from the list.”

---

## 5. Discharging (the human-designed engine)

Discharging is a finite, local redistribution argument. One assigns “charge” to vertices and faces—classically related to Euler’s formula

$$
V - E + F = 2
$$

for connected plane graphs—so that total charge is a known positive constant. Then one redistributes charge by local rules (a vertex of high degree donates charge to neighbors, and so on). After redistribution, every vertex or face has nonnegative charge only if certain dense configurations appear; otherwise some location would retain negative charge, which is impossible. Hence one of a designed list of configurations is unavoidable.

Designing the discharging rules and the configuration list is deep combinatorial craft. Verifying that the rules work and that each configuration is reducible became, historically, a machine-checkable mountain of cases—hundreds of configurations in Appel–Haken, later simplified lists in the Robertson–Sanders–Seymour–Thomas proof (1997), and eventually formal proofs in systems such as Coq (Gonthier et al.).

---

## 6. The idea of the proof, one page

1. Reformulate map coloring as planar graph 4-coloring.  
2. Assume a minimal counterexample $$G$$.  
3. Exhibit a finite unavoidable set $$\mathcal{U}$$ of configurations (via discharging + Euler).  
4. Prove each configuration in $$\mathcal{U}$$ is reducible (case analysis; computer-assisted).  
5. Conclude no minimal counterexample exists; every planar graph is 4-colorable.

Human insight designs $$\mathcal{U}$$ and the discharging scheme; machines (or proof assistants) audit the finite explosion of local coloring cases.

---

## 7. Computer-assisted proof and later verification

Appel–Haken’s 1976 announcement forced a debate: is an unreadable case bash a proof? Over time the community largely accepted computer-assisted proofs when:

- the algorithm is specified clearly;  
- the computation is reproducible in principle;  
- later independent checks and simplifications accrue.

The 1997 proof reduced the configuration set and clarified the structure. Georges Gonthier’s formal proof in Coq (announced 2005) encoded the argument so that a proof assistant checks every step against a small logical kernel. That does not make the theorem “only about computers”; it makes the finite reasoning **auditably airtight**.

For this course, the methodological moral sits beside the combinatorial one: *proof ideas can include the design of a finite verification task.*

Compare this with Euclid or $$\sqrt{2}$$, where a human can hold every step in working memory. Four color shows a third style of idea: **reduce infinity to a checklist, then audit the checklist**. The creativity is in the reduction and the discharging design; the endurance is in the audit. Neither half alone is the theorem.

Historically, resistance to computer proof often mixed two concerns that should be separated: (1) *correctness* of the finite cases, and (2) *understanding* of why four colors suffice. Formal verification primarily addresses (1). Expositions, simplified configuration lists, and toy discharging examples address (2). A mature reader wants both: confidence that the cases are right, and a narrative of the strategy that a classmate can follow without reading thousands of local checks.

---

## 8. What the theorem does *not* say

- It does not claim every map on every surface is 4-colorable; genus changes the chromatic story (Heawood’s formula for higher genus, with history of its own).  
- It does not give the fastest practical algorithm for all instances, though coloring planar graphs is polynomial-time in theory for fixed numbers of colors in appropriate formulations.  
- It does not say four colors are needed for *every* map—only that four always suffice and that three do not always suffice.  
- It is not the same as the **Five Color Theorem**, which has a short classical proof.

---

## Common confusions

1. **“The computer randomly verified maps.”** — No: it checked mathematical reducibility cases for configurations in a finite list.  
2. **“Humans did not prove anything.”** — Humans designed discharging, unavoidability, and reducibility notions.  
3. **“Four colors for planar graphs means four colors for all graphs.”** — Completely false; non-planar graphs can need arbitrarily many colors.  
4. **“Countries meeting at a point must get different colors.”** — Standard statement uses border segments, not point touches.  
5. **“Idea of proof means skip finite checklists.”** — The checklist *is* the proof’s spine; “idea” means understanding why the checklist works.

---

## Exercises

1. Explain dualization: why map coloring becomes vertex coloring of a planar graph.  
2. Show that $$K_4$$ is planar and needs 4 colors; explain why that does not yet prove sharpness for the whole theorem (need some planar graph with chromatic number 4—$$K_4$$ works).  
3. Why does a minimal counterexample help? Write five sentences.  
4. In your own words, define unavoidable set and reducible configuration.  
5. Look up (externally) the number of configurations in Appel–Haken vs Robertson et al.; record the numbers and one sentence on why reduction of the list matters.  
6. **Philosophy (≤250 words).** When is a computer-assisted proof acceptable to you? Name one criterion.  
7. **Narrative (≤350 words).** Explain the four-color proof idea to a classmate without listing all configurations.

---


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
