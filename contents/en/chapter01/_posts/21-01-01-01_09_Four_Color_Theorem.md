---
layout: post
title: "The Four Color Theorem"
chapter: '01'
order: 9
owner: Nguyen Le Linh
lang: en
categories:
- chapter01
---

> **Learning path B — Four colors (2 steps)**  
> **1. You are here:** Ch.1 Four Color Theorem (this page) — theory + proof culture  
> **2. Next:** [Ch.7 Map-colors studio]({{ site.baseurl }}/contents/en/chapter07/07_07_Explore_Map_Colors/) — draw duals, Heawood, write-up  
> *Time guide:* ~2 h essay → ~1–2 h studio.

The **Four Color Theorem (4CT)** asserts that every planar map can be colored with at most **four** colors so that regions sharing a positive-length border receive different colors. Equivalently, in graph language: every finite **planar graph** is 4-vertex-colorable. Unlike the Riemann Hypothesis, twin primes, or Collatz, 4CT is **solved**—and that fact is part of its pedagogical value. The solution did not arrive as a short conceptual “aha.” Appel and Haken (1976) completed the first accepted proof with a massive computer-checked case analysis; later simplifications (Robertson–Sanders–Seymour–Thomas and others) still rely on extensive machine verification. Formal proof assistants have since re-checked versions of the argument.

So this essay is both a graph-theory story and a **philosophy-of-proof** story. Solved does not mean trivial. A theorem can be true, accepted, and still reshape what the community means by “we have a proof.”

**Path through this essay:** map coloring folklore → dual graphs → five-color theorem → minimal counterexamples, reducibility, unavoidable sets → discharging and computers → what machine assistance means → Heawood on higher surfaces → culture and course links.

---

## Learning objectives

After this lecture you should be able to:

- State 4CT in **map language** and **graph language**, and explain the dual-graph translation.
- Sketch why **five** colors are classically easier than four (Euler → low-degree vertex → induction / Kempe-style recoloring).
- Describe **unavoidable sets** and **reducible configurations** at slogan level, and how they combine into a proof strategy.
- Discuss **computer-assisted proof** as a mathematical and philosophical issue (finite checks vs surveyability; formalization).
- Contrast planar 4CT with **Heawood’s formula** on higher-genus surfaces.
- Link to the Chapter 7 map-colors studio and to Euler / Königsberg culture in the course.
- Internalize: **solved ≠ trivial**—a settled theorem can still be deep, historically hard, and conceptually rich.

**Prerequisites.** Graphs as vertices and edges; the idea of a planar drawing (edges can be drawn without crossings). No advanced graph theory required; Euler’s formula will be used at slogan level.

**Seminar link.** LO1 plus “what is a proof?” discussion. Natural pairings: [Kakeya]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/) (open analytic culture vs solved combinatorial culture); [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) (computation in mathematics); [Explore map colors]({{ site.baseurl }}/contents/en/chapter07/07_07_Explore_Map_Colors/).

---

## 1. The mapmakers’ question

Since the mid-nineteenth century—Guthrie, De Morgan, Cayley, and a long line of amateur and professional contributors—people have asked: how many colors suffice for political maps so that neighboring countries differ in color?

The question is more subtle than it sounds. Neighboring means sharing a **border of positive length**, not merely meeting at a point (otherwise four countries meeting at a crossroads would incorrectly force four pairwise conflicts from a single point). Standard formulations also treat regions as connected; maps that allow disconnected “countries” (enclaves counted as the same region) change the problem entirely.

Color counts in plain language:

- **Two colors** fail as soon as an odd wheel of mutually adjacent regions appears—think of countries arranged so that an odd cycle of adjacencies forces a third color.
- **Three colors** fail for some planar maps (a country surrounded by an odd ring of mutually adjacent neighbors, in suitable arrangements, is a classic obstruction).
- **Four colors** were conjectured to suffice for every planar map.
- **Five colors** were proved to suffice by classical arguments long before four was settled (Heawood’s five-color theorem and related developments).

The conjecture that four always work became one of the most famous problems in discrete mathematics—easy to explain at a dinner table, resistant for more than a century.

![Regions needing many colors]({{ site.baseurl }}/img/chapter_img/fourcolor_map_k4.svg)

*Figure. Cartoon of mutually adjacent regions—motivating the need for multiple colors.*

---

## 2. From maps to planar graphs

Graph theory converts geography into combinatorics. Associate to each region a **vertex**. Draw an **edge** between two vertices when the corresponding regions share a border of positive length. Under mild hypotheses on the map, the result is a **planar graph**: it can be drawn in the plane without edge crossings.

Coloring regions so that adjacent regions differ is then exactly **vertex coloring**: assign colors to vertices so that adjacent vertices receive different colors. The least number of colors needed for a graph $$G$$ is its **chromatic number** $$\chi(G)$$.

![Map dual graph]({{ site.baseurl }}/img/chapter_img/fourcolor_graph_dual.svg)

*Figure. Dual graph: vertices = regions; edges = shared borders.*

**Theorem (4CT, graph form).** Every finite planar graph $$G$$ satisfies $$\chi(G)\le 4$$.

This dual viewpoint is not cosmetic. It lets one import Euler’s formula and degree-counting arguments. For a connected simple plane graph with $$v$$ vertices, $$e$$ edges, and $$f$$ faces,

$$
v - e + f = 2
$$

(on the sphere / plane). Combined with face-degree inequalities, one obtains the classical sparsity bound $$e \le 3v - 6$$ for simple planar graphs with $$v\ge 3$$. Sparsity implies that planar graphs always have a vertex of small degree—fuel for induction.

Historical culture note: Euler’s formula also sits behind the Königsberg bridge story and the birth of graph theory as a subject. Four-color work is part of that same combinatorial lineage, even when the final proof is far from Euler’s original recreational setting.

---

## 3. Why five colors is easier

The **five-color theorem** has short classical proofs that every student should see at least in outline. A typical skeleton:

1. From Euler / sparsity, every simple planar graph has a vertex $$v$$ of degree at most $$5$$.
2. Remove $$v$$; color the rest by induction with five colors.
3. Try to extend the coloring to $$v$$. If the neighbors of $$v$$ do not use all five colors, assign a free color.
4. If they do use all five, use **Kempe-chain** recoloring arguments: swap colors along connected two-color components to free a color for $$v$$. For five colors, the chain arguments can be arranged to work.

Kempe believed in 1879 that he had proved the **four**-color case by similar methods. In 1890 Heawood found a flaw in the four-color argument and salvaged a correct five-color theorem. The gap between five and four hid roughly a century of work. That history is worth remembering: a plausible recoloring idea can fail in subtle configurations; the difference between “almost a proof” and “a proof” can be enormous.

---

## 4. Minimal counterexamples, reducibility, and unavoidable sets

Modern proofs of 4CT are organized around a proof by contradiction that is combinatorial rather than “check every map on Earth.”

Assume $$G$$ is a **minimal planar graph that is not 4-colorable**—a smallest counterexample (by number of vertices, after suitable normalizations). Then one can argue structural properties: roughly triangulation-like maximality after reductions; no vertices of degree less than 5; and strong constraints on local neighborhoods.

Two definitions carry the logic:

- A configuration $$C$$ is **reducible** if, whenever it appears in a larger graph, a 4-coloring of the graph with $$C$$ removed (or contracted in a controlled way) can be extended, after possible recoloring, to a 4-coloring of the whole graph. Thus a reducible configuration **cannot appear** in a minimal counterexample: if it did, the remainder would be 4-colorable and the coloring would extend.
- A set $$\mathcal{U}$$ of configurations is **unavoidable** if every minimal counterexample must contain at least one configuration from $$\mathcal{U}$$.

If you exhibit an unavoidable set $$\mathcal{U}$$ in which **every** member is reducible, you obtain a contradiction: a minimal counterexample would have to contain some $$C\in\mathcal{U}$$, yet no reducible $$C$$ can appear. Therefore no minimal counterexample exists, and every finite planar graph is 4-colorable.

![Proof pipeline]({{ site.baseurl }}/img/chapter_img/fourcolor_proof_pipeline.svg)

*Figure. Unavoidable set + reducibility checks ⇒ no minimal counterexample.*

**Discharging** is the human-designed engine that produces unavoidable sets. One assigns “charges” to vertices (or faces) using Euler’s formula so that total charge is positive (or otherwise constrained), then redistributes charge according to local rules. If every configuration outside a proposed list ends up with nonpositive charge under the rules, something in the list must occur—unavoidability. Designing good discharging rules is deep combinatorial craft; checking reducibility for each listed configuration is finite but enormous.

Appel and Haken produced a large unavoidable set and verified reducibility with a custom computer program, together with substantial hand work. The 1976–77 announcement was a watershed: for the first time, a major theorem’s proof relied on a machine-checked case analysis at a scale no human could survey line by line.

---

## 5. Simplification, still machine-checked

Later work improved the proof’s hygiene without returning to a short hand proof. Robertson, Sanders, Seymour, and Thomas (1997) gave a simplified argument with a much smaller unavoidable set and a clearer logical structure, still relying on computer verification of reducibility. Other presentations and independent checks followed. Formalizations in proof assistants (notably Gonthier’s Coq development of a 4CT proof) addressed a different worry: not only “did the program run?” but “is the mathematical statement of each case correctly formalized and checked by a trusted kernel?”

The community status is settled: **4CT is a theorem**. What remains lively is methodology—how to design discharging, how to minimize case lists, how to formalize combinatorial arguments—not whether four colors suffice for planar maps.

---

## 6. What “computer-assisted” means here

It is important to distinguish this from Monte Carlo simulation or “the computer guessed the theorem.”

In the Appel–Haken / RSST tradition:

- a **finite** combinatorial checklist is derived from a human-designed discharging method;
- each case is a finite graph-coloring extension / reducibility problem;
- the machine enumerates and checks cases too numerous for reliable hand calculation;
- the overall logic (why the list is unavoidable; why reducibility yields contradiction) is a human mathematical argument.

Philosophical questions remain popular in seminars and essays:

- Must a proof be **surveyable** by a single human mind in a reasonable time?
- If a proof assistant verifies a formalization, does that restore a form of surveyability at the level of the kernel and the formal text?
- Are we satisfied with the **existence** of a finite check, or do we still seek a short conceptual reason that makes 4CT “obvious” in hindsight?

Different mathematicians answer differently. Mathematically, 4CT is accepted as proved. Conceptually, it is a landmark in **proof technology**—a precursor to today’s broader world of formal verification and large case analyses in other fields.

---

## 7. Beyond the plane: Heawood’s map color theorem

The plane is special. On a surface of genus $$g\ge 1$$, more colors may be needed. **Heawood’s number**

$$
H(g)=\left\lfloor\frac{7+\sqrt{1+48g}}{2}\right\rfloor
$$

gives (in the classical completed story) the maximum chromatic number for graphs embeddable on that surface. For the torus ($$g=1$$), seven colors are tight: some toroidal maps need seven, and seven always suffice. The case $$g=0$$ formally plugs into the formula to give $$4$$, but historically Heawood’s work gave five for the plane; the sharp planar four required the full 4CT.

![Heawood formula]({{ site.baseurl }}/img/chapter_img/fourcolor_heawood.svg)

*Figure. Color needs grow with genus.*

This contrast is excellent pedagogy: **planarity** is a strong geometric constraint that collapses the color bound to four, while a single handle (the torus) jumps the tight bound to seven. In the Chapter 7 studio you can explore duals, small maps that force three or four colors, and the Heawood count as a formula to test on toy surfaces.

**Disconnected regions.** If a “country” may have multiple connected components that must share one color, the problem changes: one can construct maps needing arbitrarily many colors. Standard 4CT assumes connected regions (or treats components carefully). Always state the model when you color maps.

---

## 8. Why it mattered for mathematics

Beyond settling a famous conjecture, 4CT:

- catalyzed **discharging methods** and structural thinking about planar graphs;
- forced the community to articulate standards for **machine-checked mathematics**;
- provided a century-long laboratory for recoloring, reducibility, and unavoidable sets;
- remains a perfect teaching contrast with **open** analytic and arithmetic problems (RH, Kakeya in high dimensions, Collatz).

It also sits near graph minors, Hadwiger’s conjecture (still open), and broader questions about structure and chromatic number.

---

## From videos: what “computer-assisted” actually means

Numberphile and Quanta’s map-coloring films, together with Gonthier’s Notices essay and the Thomas FC page, fix the LO1 slogan:

1. The proof is **not** “try many maps and hope.” It is a classical **discharging / unavoidable set** argument reducing the infinite planar case to a **finite** list of configurations.  
2. The machine checks **reducibility** (and related combinatorial bookkeeping) for those configurations—Appel–Haken (1976), streamlined by Robertson–Sanders–Seymour–Thomas (~633 configurations).  
3. **Gonthier’s Coq formalization (2005)** machine-checks a full mathematical development (largely following RSST), so trust concentrates on the proof assistant’s kernel rather than on ad-hoc C programs alone.  
4. **Five colors** needs no computer; **Heawood** numbers handle higher genus (torus up to seven).

**Status (as of 2026):** **proved**. Solved ≠ trivial. Contrast with open problems in this chapter (RH, P vs NP, twins, NS, BSD, high-dimensional Kakeya).

---

## Common misconceptions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Four colors are sometimes not enough for planar maps.” | Fail | 4CT says four always suffice (standard hypotheses: connected regions, positive-length borders). |
| “The computer randomly verified lots of maps.” | Fail | Finite reducibility checks inside a designed discharging proof. |
| “The five-color theorem needs a computer too.” | Fail | Classical short proofs exist. |
| “4CT decides coloring for every surface.” | Fail | Higher genus uses Heawood-type numbers; torus needs up to seven. |
| “Any map with four countries needs four colors.” | Fail | Only if every pair shares a border; many four-country maps need fewer. |
| “Solved problems are trivial.” | Fail | **Solved ≠ trivial**; 4CT was hard for a century and remains deep as proof culture. |
| “Formalization made the 1976 proof ‘not count.’” | Fail | Formalization strengthens confidence; the theorem was already accepted, with ongoing improvements in presentation. |

---

## Exercises

1. Draw a planar map that needs **three** colors and argue carefully why two colors fail.
2. Translate your map into a dual graph and 3-color the vertices.
3. From $$e\le 3v-6$$ for simple planar graphs with $$v\ge 3$$, prove that some vertex has degree at most $$5$$.
4. Outline the five-color induction in four bullet points (low-degree vertex → remove → color → extend / recolor).
5. In your own words: what is an **unavoidable set**, and what does it mean for a configuration to be **reducible**? How do the two notions combine?
6. Research literacy: read a short history of Appel–Haken; list one historical criticism of computer proof and one response (e.g. independent checks, RSST simplification, Coq formalization).
7. Exploration: try the [Ch.7 map-color studio]({{ site.baseurl }}/contents/en/chapter07/07_07_Explore_Map_Colors/) prompts; compute Heawood’s number for $$g=1$$ and $$g=2$$.
8. Compare proof cultures in one paragraph: 4CT’s finite case explosion vs Perelman’s Ricci-flow approach to the Poincaré conjecture (community verification without the same style of machine case list).

---

## Video sources (math-video-researcher pack)

Full ranking and notes: `research/video-research/Four_Color_Theorem/`.

**Recommended order**

1. **Orientation** — Numberphile, *The Four Color Map Theorem*: [YouTube](https://www.youtube.com/watch?v=NgbK43jB4rQ).  
2. **Core popular** — Quanta, *The Map Coloring Puzzle That Changed Mathematics*: [YouTube](https://www.youtube.com/watch?v=h7kqlYUV1l8) · [article](https://www.quantamagazine.org/only-computers-can-solve-this-map-coloring-problem-from-the-1800s-20230329/).  
3. **Extra culture** — Numberphile extra footage: [YouTube](https://www.youtube.com/watch?v=laMkuPrad3s); Conway on computer proofs (Simons): [YouTube](https://www.youtube.com/watch?v=fPVXBurxfU8).  
4. **Formalization essay** — Gonthier, *Formal Proof—The Four-Color Theorem* (Notices AMS): [PDF](https://www.ams.org/notices/200811/tx081101382p.pdf).  
5. **RSST portal** — Robin Thomas: [fourcolor.html](https://thomas.math.gatech.edu/FC/fourcolor.html).

**After videos:** 4CT is **proved** (as of long before 2026). Computer assistance ≠ random search; formalization ≠ “only now true.”

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Four_Color_Theorem/transcripts/` · status: `research/video-research/Four_Color_Theorem/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Four_Color_Theorem_NgbK43jB4rQ_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full bibliography: `research/video-research/Four_Color_Theorem/references.md`.

### Classical and formal

1. K. Appel & W. Haken (1976/77) — computer-assisted landmark.  
2. N. Robertson, D. Sanders, P. Seymour, R. Thomas — simplified proof; [Thomas FC page](https://thomas.math.gatech.edu/FC/fourcolor.html).  
3. G. Gonthier — [Formal Proof—The Four-Color Theorem](https://www.ams.org/notices/200811/tx081101382p.pdf) (Notices AMS).  
4. Heawood — five colors; map coloring on surfaces.  
5. Wikipedia — [Four color theorem](https://en.wikipedia.org/wiki/Four_color_theorem); [MathWorld](https://mathworld.wolfram.com/Four-ColorTheorem.html).  
6. Illinois museum: https://distributedmuseum.illinois.edu/exhibit/four-color-theorem/  

### Videos and news

7. Numberphile: https://www.youtube.com/watch?v=NgbK43jB4rQ · extra: https://www.youtube.com/watch?v=laMkuPrad3s  
8. Quanta video: https://www.youtube.com/watch?v=h7kqlYUV1l8 · [article](https://www.quantamagazine.org/only-computers-can-solve-this-map-coloring-problem-from-the-1800s-20230329/)  
9. Conway (Simons): https://www.youtube.com/watch?v=fPVXBurxfU8  

### Course

10. [Explore map colors]({{ site.baseurl }}/contents/en/chapter07/07_07_Explore_Map_Colors/); contrast [Kakeya]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/). Pack: `research/video-research/Four_Color_Theorem/`.

---

## Further directions

**Continue Learning path B**

1. Done: Ch.1 Four Color (this page).  
2. **Next →** [Ch.7 Map-colors studio]({{ site.baseurl }}/contents/en/chapter07/07_07_Explore_Map_Colors/).

Optional: trust in computer-assisted proof; Hadwiger’s conjecture (still open); “solved combinatorial mountain” vs “open analytic mountain” via Kakeya.
