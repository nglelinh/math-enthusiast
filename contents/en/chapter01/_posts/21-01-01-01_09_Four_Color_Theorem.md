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

In October 1852, a young student named Francis Guthrie was coloring a map of the counties of England and noticed something curious: no matter how tangled the borders were, he never seemed to need more than **four** colors to keep neighboring counties distinct. He asked his brother, who asked Augustus De Morgan—and a century-long mathematical obsession was born.

The **Four Color Theorem (4CT)** asserts that every planar map can be colored with at most **four** colors so that any two regions sharing a border of positive length receive different colors—or equivalently, that every finite **planar graph** is 4-vertex-colorable. Unlike the Riemann Hypothesis, twin primes, or Collatz, 4CT is **proved**. Yet its solution did not arrive as a sleek five-line miracle. In 1976, Kenneth Appel and Wolfgang Haken delivered the first accepted proof only by pairing a subtle human combinatorial strategy with more than a thousand hours of computer case-checking. Even modern streamlined proofs (Robertson–Sanders–Seymour–Thomas, 1997; Georges Gonthier’s 2005 formalization in Coq) still rely on machine verification.

That makes this lesson both a tour of planar graph theory and a front-row seat to the **philosophy of mathematical proof**. *Solved* does not mean *trivial*—and the Four Color Theorem permanently changed what mathematicians mean when they say, “we have proved it.”

---

## Learning objectives

After this lecture you should be able to:

- State the Four Color Theorem in both **map language** and **graph language**, and translate maps into **dual planar graphs**.
- Use Euler’s formula $$v - e + f = 2$$ and the sparsity bound $$e \le 3v - 6$$ to prove why $$K_5$$ is non-planar and why five colors are dramatically easier than four.
- Explain **minimal counterexamples**, **unavoidable sets**, **reducible configurations**, and the **discharging method** with concrete hand calculations.
- Distinguish genuine **computer-assisted proofs** and **formal proof assistants (Coq)** from random simulation or numerical evidence.
- Contrast planar 4-coloring with **Heawood’s formula** on higher-genus surfaces (such as 7 colors on the torus).

**Prerequisites.** Graphs as vertices and edges, basic counting, and the idea of drawing edges without crossings. Euler’s formula and discharging are built from scratch below.

**Course links.** Pair with [Explore map colors]({{ site.baseurl }}/contents/en/chapter07/07_07_Explore_Map_Colors/) (studio), [Kakeya]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/) (open analytic culture vs. solved combinatorial culture), and [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) (computation in mathematics).

---

## Background Knowledge Map: What Fields Sit Behind the Four Color Theorem?

Why did an afternoon map-coloring puzzle spark a century of mathematics and launch formal proof verification? Three major disciplines meet inside 4CT.

### 1. Graph Theory and Structural Combinatorics
**Graph theory** strips away geography (country shapes, sizes, coastlines) and keeps only pure adjacency: vertices connected by edges. Coloring a map becomes finding the **chromatic number** $$\chi(G)$$ of a **planar graph**—the smallest number of colors needed so no two adjacent vertices share a color.
- **Core questions:** How does forbidding crossings restrict vertex degrees and local substructures? Which forbidden configurations force a graph to be $$k$$-colorable?
- **Real-world reach:** Register allocation in compilers, exam/classroom scheduling, wireless frequency assignment, and circuit-board layout.

### 2. Low-Dimensional Topology and Surface Embeddings
A flat sheet of paper and the surface of a sphere have the same **Euler characteristic** ($$\chi = 2$$), whereas a donut (torus) has $$\chi = 0$$. **Topology** reveals why planarity is such a tight straightjacket: adding even a single handle (genus $$g = 1$$) lets seven mutually touching countries coexist, jumping the color requirement from $$4$$ to $$7$$.
- **Core questions:** Which graphs can be drawn without crossings on a surface of genus $$g$$? How does topology bound chromatic numbers (*Heawood’s formula*)?
- **Real-world reach:** Mesh generation in 3D graphics, topological data analysis, and VLSI microchip routing across multiple layers.

### 3. Automated Reasoning and Formal Verification
When Appel and Haken used a computer to check nearly two thousand reducible configurations in 1976, mathematicians asked: *what if the code has a bug?* That debate accelerated **interactive theorem proving** (Coq, Lean, Isabelle), culminating in Georges Gonthier’s 2005 machine-checked formal proof of 4CT inside Coq.
- **Core questions:** How can we verify massive combinatorial proofs with absolute logical certainty? Can a tiny trusted proof kernel check every single logical step?
- **Real-world reach:** Verifying aerospace/automotive control software, cryptographic protocols, CPU microarchitecture, and modern math formalization projects.

---

## 1. The mapmakers’ question

Since the mid-nineteenth century—Guthrie, De Morgan, Cayley, Kempe, and Heawood—mathematicians asked how many colors suffice for any political map so that neighboring countries differ in color.

Two ground rules keep the question sharp:
- **Positive-length borders:** Two regions count as neighbors only if they share a border segment, not merely a single corner point (otherwise a pie sliced into 100 wedges meeting at the center would artificially require 100 colors).
- **Connected countries:** Each region must be a single connected piece (no disconnected exclaves forced to share one color; allowing disconnected countries lets you force arbitrarily many colors).

Quick color checks:
- **2 colors** fail as soon as three countries touch pairwise (an odd cycle).
- **3 colors** fail on four mutually adjacent countries (a central country surrounded by a ring of three mutually touching neighbors).
- **5 colors** were proved to suffice in 1890 by Percy Heawood.
- **4 colors** always suffice—but proving that final step from 5 down to 4 took another 86 years.

![Regions needing many colors]({{ site.baseurl }}/img/chapter_img/fourcolor_map_k4.svg)

*Figure. Cartoon of mutually adjacent regions—motivating the need for multiple colors.*

---

## 2. From maps to planar graphs

Graph theory converts geography into combinatorics via the **dual graph**: place one **vertex** inside each country and draw an **edge** crossing each shared border. Because the map lies on the plane, the dual graph can be drawn without any edges crossing—it is a **planar graph**. Coloring countries is now identical to **vertex coloring**, and the minimum number of colors needed is the **chromatic number** $$\chi(G)$$.

![Map dual graph]({{ site.baseurl }}/img/chapter_img/fourcolor_graph_dual.svg)

*Figure. Dual graph: vertices = regions; edges = shared borders.*

<div class="textbook-theorem" markdown="1">
**Theorem (4CT, graph form).** Every finite planar graph $$G$$ satisfies $$\chi(G)\le 4$$.
</div>

This dual viewpoint unlocks **Euler’s formula**: for any connected simple planar graph with $$v$$ vertices, $$e$$ edges, and $$f$$ faces,

$$
v - e + f = 2.
$$

Because every face of a simple planar graph (with $$v \ge 3$$) is bounded by at least $$3$$ edges and each edge borders at most $$2$$ faces, we have $$3f \le 2e$$, i.e., $$f \le \frac{2}{3}e$$. Substituting into Euler’s formula yields the **planar sparsity inequality**:

$$
e \le 3v - 6.
$$

---

### Worked Example 1: Why $$K_4$$ Fits on the Plane, $$K_5$$ Breaks, and $$K_7$$ Fits on a Donut

Why can’t five countries all touch one another on a flat map (which would immediately force 5 colors)? Let’s check the exact numbers using Euler’s sparsity bound!

1. **Test $$K_4$$ (4 mutually adjacent countries):**
   - Vertices $$v = 4$$, edges $$e = \binom{4}{2} = 6$$.
   - Planar ceiling: $$3v - 6 = 3(4) - 6 = 6$$.
   - Check: $$6 \le 6$$! Tight, and indeed $$K_4$$ draws cleanly in the plane (a triangle with one vertex inside), so 4 colors are *sometimes necessary*.
2. **Test $$K_5$$ (5 mutually adjacent countries):**
   - Vertices $$v = 5$$, edges $$e = \binom{5}{2} = 10$$.
   - Planar ceiling: $$3v - 6 = 3(5) - 6 = 9$$.
   - Check: $$10 > 9$$! **Impossible.** Five countries can never all share borders on a flat map.
3. **Now move to a torus (donut, genus $$g = 1$$):**
   - On a torus, Euler’s formula changes from $$2$$ to $$0$$: $$v - e + f = 0$$.
   - Combining with $$3f \le 2e$$ gives a relaxed bound: $$e \le 3v$$ (we gained 6 extra edges!).
   - Test **$$K_7$$** (7 mutually adjacent countries): $$v = 7$$, edges $$e = \binom{7}{2} = 21$$, and $$3v = 3(7) = 21$$! Indeed, $$K_7$$ embeds cleanly on a torus—so toroidal maps genuinely require **7 colors**!

**Takeaway:** A single arithmetic constant—the $$2$$ in $$v - e + f = 2$$—explains why $$K_5$$ cannot exist on a plane while $$K_7$$ thrives on a donut. (Note: forbidding $$K_5$$ alone does *not* prove 4CT, because planar graphs without $$K_5$$ could still theoretically have chromatic number 5—that is why 4CT was so much harder!)

---

## 3. Why five colors is easier

The **Five Color Theorem** fits cleanly on half a page:

1. From $$e \le 3v - 6$$, the average vertex degree is $$\frac{2e}{v} \le 6 - \frac{12}{v} < 6$$, so every simple planar graph has a vertex $$u$$ of degree at most $$5$$.
2. Delete $$u$$ and inductively 5-color the smaller graph $$G - u$$.
3. If $$u$$’s neighbors use at most 4 colors, pick the leftover color for $$u$$.
4. If $$u$$ has degree $$5$$ and its five neighbors $$v_1, v_2, v_3, v_4, v_5$$ (in cyclic order) use all five colors (say Red, Blue, Green, Yellow, Purple), consider the **Kempe chain** of Red–Green vertices starting at $$v_1$$. Either it fails to reach $$v_3$$ (swap Red/Green in that component to free Red for $$u$$), or it forms a closed Red–Green barrier separating $$v_2$$ (Blue) from $$v_4$$ (Yellow)—in which case the Blue–Yellow chain from $$v_2$$ *cannot* cross that barrier (by planarity!), so swapping Blue/Yellow frees Blue for $$u$$!

In 1879, Alfred Kempe tried the exact same trick for **four** colors—and the mathematical world celebrated for eleven years until Percy Heawood (1890) found a fatal flaw: when you try to swap *two* Kempe chains simultaneously in a degree-5 neighborhood with only 4 colors, the chains can tangle and interfere with each other! Heawood salvaged the Five Color Theorem, leaving the Four Color Conjecture wide open for another 86 years.

---

## 4. Minimal counterexamples, reducibility, and unavoidable sets

Modern proofs of 4CT do **not** “check every map on Earth.” Instead, they argue by contradiction around a hypothetical **minimal counterexample** $$G$$ (a planar triangulation with the smallest possible number of vertices that cannot be 4-colored).

Two concepts lock together like jaws of a vise:

- **Reducible configuration:** A local subgraph $$C$$ that *cannot* appear inside a minimal counterexample (because if $$C$$ appeared in $$G$$, you could delete or simplify $$C$$, 4-color the smaller graph by minimality, and extend the 4-coloring back across $$C$$).
- **Unavoidable set:** A finite list $$\mathcal{U}$$ of local configurations such that **every** planar triangulation (with minimum degree $$\ge 5$$) *must* contain at least one configuration from $$\mathcal{U}$$.

If you construct an unavoidable set $$\mathcal{U}$$ and verify that **every single configuration in $$\mathcal{U}$$ is reducible**, then no minimal counterexample can exist—so every planar graph is 4-colorable!

![Proof pipeline]({{ site.baseurl }}/img/chapter_img/fourcolor_proof_pipeline.svg)

*Figure. Unavoidable set + reducibility checks ⇒ no minimal counterexample.*

---

### Worked Example 2: Watching the Discharging Method Work by Hand

How do mathematicians ever prove a finite list of shapes is **unavoidable** across *all* infinitely many planar triangulations? By turning Euler’s formula into a **bank-account conservation law** called **discharging**!

In any planar triangulation (where every face is a triangle, so $$3f = 2e$$), Euler’s formula $$v - e + f = 2$$ multiplies by $$6$$ and rearranges (using $$2e = \sum_{u} \deg(u)$$) into the **master charge identity**:

$$
\sum_{u \in V} \bigl(6 - \deg(u)\bigr) = 12.
$$

Think of each vertex $$u$$ as starting with a bank balance of $$c(u) = 6 - \deg(u)$$ dollars:
- A degree-5 vertex starts **rich**: $$+1$$ dollar.
- A degree-6 vertex starts **break-even**: $$0$$ dollars.
- A degree-7 vertex starts in **debt**: $$-1$$ dollar; a degree-8 vertex at $$-2$$ dollars, and so on.
- **Conservation law:** No matter how huge the map is—even a billion countries—the sum of all bank balances across the entire map is **always exactly $$+12$$ dollars**!

Let’s test this by hand on two concrete examples:
1. **The regular icosahedron** (12 vertices, all of degree $$5$$): every vertex has charge $$6 - 5 = +1$$, so the total charge is $$12 \times (+1) = +12$$. Exact match!
2. **A mini-discharging rule:** Suppose a minimal counterexample has minimum degree $$5$$ and we want to prove it *must* contain either two adjacent degree-5 vertices, or a degree-5 vertex adjacent to a degree-6 vertex.
   - **Rule:** Every degree-5 vertex ($$+1$$) sends $$\frac{1}{5}$$ dollar to each of its 5 neighbors.
   - After redistribution, every degree-5 vertex ends with $$1 - 5\cdot\frac{1}{5} = 0$$ (unless it *received* money from an adjacent degree-5 neighbor!).
   - A degree-7 vertex (starting at $$-1$$) has 7 neighbors; even if all 7 were degree-5, it could reach $$-1 + 7/5 = +2/5 > 0$$—showing that a degree-7 vertex surrounded by many degree-5 neighbors is a configuration that stays positive and must be added to our unavoidable list (or refined by smarter rules)!
   - Because total money stays $$+12 > 0$$, **some** vertex must finish with a strictly positive balance—guaranteeing that at least one configuration in our finite list $$\mathcal{U}$$ *must* appear in the graph!

---

### Deep-Dive Explanation: How the Four Color Theorem Proof Actually Works (Read Slowly)

To see why 4CT is neither “magic” nor “guessing with a supercomputer,” walk through the four-stage architecture of the Appel–Haken / RSST / Gonthier proof slowly.

#### Step 1: Assume a smallest counterexample $$G$$ and normalize it
Suppose planar graphs that cannot be 4-colored exist. Pick one with the fewest vertices. Add edges until every face is a triangle (adding edges only makes coloring harder). By Euler’s formula and simple Kempe checks, $$G$$ cannot have any vertex of degree $$\le 4$$, nor any small separating cycles—so every vertex in $$G$$ has degree $$\ge 5$$.

#### Step 2: Design human discharging rules to build a finite unavoidable set $$\mathcal{U}$$
Assign initial charge $$6 - \deg(u)$$ to every vertex (total charge $$+12$$). Mathematicians craft a finite set of local charge-transfer rules (RSST uses just 32 rules!) and prove—purely by local case accounting—that if a planar triangulation avoids every configuration in their list $$\mathcal{U}$$ (633 configurations in RSST; ~1,936 originally in Appel–Haken), then every vertex ends up with charge $$\le 0$$. That contradicts total charge $$+12$$! Hence $$\mathcal{U}$$ is **unavoidable**.

#### Step 3: Let the computer verify that every configuration in $$\mathcal{U}$$ is reducible
For each of the 633 configurations $$C \in \mathcal{U}$$, surround $$C$$ with its boundary ring (say 10 to 14 vertices). The computer enumerates all valid 4-colorings of that boundary ring and systematically tests Kempe-chain swaps to prove that *every* coloring of the exterior can be modified to extend across $$C$$. This is finite, exact, deterministic discrete math—not random sampling—just too large (tens of thousands of ring colorings per configuration) for error-free human bookkeeping.

#### Step 4: Close the contradiction—and formalize the entire chain in Coq
Because $$G$$ must contain some $$C \in \mathcal{U}$$ (Step 2) yet cannot contain any reducible $$C$$ (Step 3), no minimal counterexample can exist. In 2005, Georges Gonthier went one step further: he encoded the *entire* discharging proof, the reducibility checker, and even the topological Jordan-curve planar-graph foundations inside the **Coq proof assistant**, so a tiny, independently audited logical kernel verified every single deduction from first principles.

---

## 5. Simplification, still machine-checked

Later breakthroughs dramatically cleaned up Appel and Haken’s 1976 proof without finding a short pencil-and-paper replacement:
- **Robertson, Sanders, Seymour, and Thomas (1997)** slashed the unavoidable set to **633 configurations** with a clean 32-rule discharging procedure and a quadratic-time 4-coloring algorithm.
- **Georges Gonthier (2005)** formally verified the entire proof inside the **Coq** proof assistant.

The theorem’s truth is completely settled: **4CT is a theorem**. What stays open is a philosophical and aesthetic wish: *does a short, human-surveyable conceptual proof exist?*

---

## 6. What “computer-assisted” means here

Never confuse the Four Color proof with Monte Carlo testing or checking millions of random maps!

- A **human mathematical argument** reduces infinitely many planar graphs to a **finite** checklist of 633 local configurations.
- The **computer** performs an exact, exhaustive logical verification of finite reducibility cases.
- **Formalization (Coq)** removes the worry of programmer bugs by verifying the proof inside a minimal logical kernel.

Philosophical questions remain lively in seminars: Must a proof be surveyable by one human mind? Does a formal proof assistant give *higher* certainty than a 300-page human-refereed paper? Either way, 4CT pioneered modern computer-verified mathematics.

---

## 7. Beyond the plane: Heawood’s map color theorem

The plane is special. On a surface with $$g \ge 1$$ handles (like a donut or a multi-hole pretzel), more colors are required. **Heawood’s number**

$$
H(g)=\left\lfloor\frac{7+\sqrt{1+48g}}{2}\right\rfloor
$$

gives the exact maximum chromatic number for graphs embeddable on an orientable surface of genus $$g \ge 1$$ (completed by Ringel and Youngs in 1968). Plugging in $$g = 1$$ (the torus) gives $$H(1) = \lfloor(7+7)/2\rfloor = 7$$—matching our Worked Example 1 showing $$K_7$$ embeds on a torus! Remarkably, plugging $$g = 0$$ into the formula gives $$4$$, yet the planar case resisted far longer than every higher-genus surface.

![Heawood formula]({{ site.baseurl }}/img/chapter_img/fourcolor_heawood.svg)

*Figure. Color needs grow with genus.*

**Disconnected regions.** Remember: if a “country” is allowed to split into disconnected pieces that must share one color, no finite color bound works. Standard 4CT strictly assumes connected regions.

---

## 8. Why it mattered for mathematics

Beyond answering Guthrie’s 1852 puzzle, the Four Color Theorem:
- launched the **discharging method** as a staple tool across structural graph theory;
- reshaped mathematical standards around **computer-assisted** and **formally verified** proofs;
- inspired deep open generalizations like **Hadwiger’s conjecture**; and
- stands as a vivid contrast to open analytic problems like RH and high-dimensional Kakeya.

---

## From videos: what “computer-assisted” actually means

Numberphile and Quanta’s map-coloring films, together with Gonthier’s Notices essay and Robin Thomas’s page, highlight four essentials:

1. The proof is **not** “try many maps and hope.” It is a **discharging / unavoidable set** argument reducing all planar maps to a **finite** list of configurations.  
2. The machine checks **reducibility** for those configurations—Appel–Haken (1976), streamlined by Robertson–Sanders–Seymour–Thomas (633 configurations).  
3. **Gonthier’s Coq formalization (2005)** machine-checks the full proof inside a trusted logical kernel.  
4. **Five colors** needs no computer; **Heawood** numbers govern higher-genus surfaces (torus needs up to 7).

**Status (as of 2026):** **proved**. Solved ≠ trivial.

---

## Common misconceptions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Four colors are sometimes not enough for planar maps.” | Fail | 4CT proves four always suffice (connected regions, positive-length borders). |
| “The computer randomly verified lots of maps.” | Fail | Exhaustive finite reducibility checks inside a discharging proof. |
| “The five-color theorem needs a computer too.” | Fail | Short classical hand proofs exist (Heawood, 1890). |
| “4CT decides coloring for every surface.” | Fail | Higher genus uses Heawood’s formula; a torus requires up to 7 colors. |
| “Any map with four countries needs four colors.” | Fail | Only if every pair shares a border ($$K_4$$); many 4-country maps need just 2 or 3. |
| “Solved problems are trivial.” | Fail | **Solved ≠ trivial**; 4CT took a century and transformed proof culture. |
| “Formalization made the 1976 proof ‘not count.’” | Fail | Formalization deepens trust; the theorem was already accepted and refined. |

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

Optional: trust in computer-assisted proof; Hadwiger’s conjecture (still open); “solved combinatorial mountain” vs “open analytic mountain” via [Kakeya]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/).

## Video tham khảo

- **xem trước** — [The Four Color Map Theorem - Numberphile](https://www.youtube.com/watch?v=NgbK43jB4rQ) — Numberphile, English. Watch first. “The Four Color Map Theorem - Numberphile” orients the lesson’s aim: State 4CT in map language and graph language, and explain the dual-graph translation.
- [The Map Coloring Puzzle That Changed Mathematics](https://www.youtube.com/watch?v=h7kqlYUV1l8) — Quanta Magazine, English. A second pass once the main claim is in view: State 4CT in map language and graph language, and explain the dual-graph translation.
- [John Conway - Four Color Theorem and Computer Proofs](https://www.youtube.com/watch?v=fPVXBurxfU8) — Simons Foundation, English. Further depth after the first two, still tied to this lesson: State 4CT in map language and graph language, and explain the dual-graph translation.
