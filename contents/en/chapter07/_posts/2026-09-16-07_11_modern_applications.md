---
layout: post
title: "Modern Applications: Computers in the Studio"
chapter: '07'
order: 11
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
lesson_type: optional
---

In November 2022, David Smith—a retired print technician in Yorkshire who enjoyed tinkering with geometric shapes on his computer—emailed mathematician Craig Kaplan a quirky 13-sided polygon shaped like a fedora hat. Nobody anticipated that this single cutout was the elusive "einstein" (from the German *ein Stein*, one stone) that geometers had hunted for sixty years: a single tile that covers the infinite plane **without ever repeating periodically**. Just months later, between 2023 and 2024, a neuro-symbolic AI system named **AlphaGeometry** solved 25 out of 30 International Mathematical Olympiad (IMO) geometry problems, while GPU clusters pushed exhaustive verification of the Collatz conjecture past the staggering threshold of $$2^{68} \approx 2.95 \times 10^{20}$$.

Faced with instruments this dazzling, it is tempting to fall into a subtle illusion: *can a computer now keep our research notebook for us?* The answer is **no**. On the contrary, the more powerful the machine, the sharper the human discipline must be: state a conjecture cleanly before pressing Run, record the exact scope of what was computed, and never let a finished finite computation masquerade as an infinite proof. Chapter 7 is a notebook, not a lecture hall—this companion shows how to bring 2022–2026 computational tools inside that studio habit.

**Lesson roadmap:** Key ideas (SAT solvers & UNSAT certificates, neuro-symbolic AI & GPU verification) → Explanation: hand-encoding 2-coloring of triangle $$K_3$$ as a SAT formula and proving UNSAT in 4 lines → Three modern instruments (2022–2026) → Studio log discipline.

## Learning objectives

After this optional studio companion you should be able to:

- Borrow three 2022–2026 computational instruments—SAT-assisted tiling, neuro-symbolic geometry search, and large-bound Collatz checks—without letting a finished computation impersonate a finished exploration log.
- Integrate machine output into a research notebook with scientific precision, keeping a crisp boundary between a *finite check*, an *UNSAT certificate*, and a *mathematical theorem*.
- Recognize the inherent limits of each instrument so you never overclaim beyond what the computation actually established.

## Key ideas: What Are Formal Proofs, SAT Solvers, and Computer-Assisted Mathematics?

When university students open Python or MATLAB, they usually picture the computer as a fast numerical calculator. In modern mathematics, however, computers also participate directly in **logic and proof** through three branches overlapping with computer science:

### 1. Boolean Satisfiability (SAT) and UNSAT Certificates

A **SAT solver** takes thousands or millions of logical clauses built from *AND / OR / NOT* (Conjunctive Normal Form, CNF) and searches for a True/False assignment that satisfies every clause simultaneously. What makes modern solvers (such as CaDiCaL or Kissat) revolutionary for mathematics is what happens when they answer **UNSAT (unsatisfiable)**: they emit a **proof certificate** that a tiny, independent checker can verify step by logical step! In this way, a finite computer search becomes a rigorous piece of a mathematical proof (as in the Boolean Pythagorean Triples problem or computing Heesch numbers of tiles).

### 2. Neuro-Symbolic AI

Large language models excel at intuitive guesswork—suggesting a clever auxiliary point or circumcircle in a geometry diagram—yet easily hallucinate during long chains of deduction. Systems like **AlphaGeometry** pair two halves: a neural network proposes auxiliary constructions, while a deterministic **symbolic deduction engine** verifies every logical step—guaranteeing that every proof line emitted is 100% valid.

### 3. Large-Scale Verification

GPU arrays and distributed clusters can sweep across quintillions of cases (checking Collatz up to $$2^{68}$$ or verifying zeros of the Riemann zeta function). This approach is unmatched for **hunting counterexamples**—a single counterexample refutes a conjecture instantly—yet on its own it can **never** prove a statement for all natural numbers.

## Prerequisites

The studio overview and at least one of [iteration / Collatz]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/), [tilings / map colors]({{ site.baseurl }}/contents/en/chapter07/07_07_Explore_Map_Colors/), [Kakeya]({{ site.baseurl }}/contents/en/chapter07/07_02_Explore_Kakeya/), or [sphere packing]({{ site.baseurl }}/contents/en/chapter07/07_03_Explore_Sphere_Packing/).

---

### Explanation: Hand-Encoding Graph Coloring as a SAT Formula and Proving UNSAT

To see how a combinatorial or tiling problem is fed into a SAT solver, let's encode the smallest possible example by hand: **can we color the 3 vertices of triangle $$K_3$$ (vertices $$1, 2, 3$$) using 2 colors (Red = `0`, Blue = `1`) so that no two adjacent vertices share a color?**

1. **Choose Boolean variables:** Since each vertex has 2 color choices, we need only 3 variables: $$x_1, x_2, x_3 \in \{\text{True (Blue)},\; \text{False (Red)}\}$$.
2. **Translate "vertices $$u, v$$ have different colors" into CNF clauses:** Two vertices differ in color if and only if they are *not both Blue* ($$\neg x_u \lor \neg x_v$$) AND *not both Red* ($$x_u \lor x_v$$).
3. **Write the full CNF formula across all 3 edges $$(1,2), (2,3), (1,3)$$:**
   $$
   (\neg x_1 \lor \neg x_2) \;\land\; (x_1 \lor x_2) \;\land\;
   (\neg x_2 \lor \neg x_3) \;\land\; (x_2 \lor x_3) \;\land\;
   (\neg x_1 \lor \neg x_3) \;\land\; (x_1 \lor x_3).
   $$
4. **Run SAT-style deduction by hand (unit propagation):**
   - Branch $$x_1 = \text{True}$$: clause $$(\neg x_1 \lor \neg x_2)$$ forces $$x_2 = \text{False}$$; clause $$(\neg x_1 \lor \neg x_3)$$ forces $$x_3 = \text{False}$$ → violates clause $$(x_2 \lor x_3)$$! (**Contradiction!**)
   - Branch $$x_1 = \text{False}$$: clause $$(x_1 \lor x_2)$$ forces $$x_2 = \text{True}$$; clause $$(x_1 \lor x_3)$$ forces $$x_3 = \text{True}$$ → violates clause $$(\neg x_2 \lor \neg x_3)$$! (**Contradiction!**)
   - Both branches lead to contradiction → the formula is **UNSAT**, and those 4 lines of deduction constitute a **rigorous proof certificate** that $$\chi(K_3) > 2$$!

In real research (like analyzing the hat monotile or 3-coloring a 50-region map), the principle is identical—you simply replace 3 variables and 6 clauses with tens of thousands of variables and hundreds of thousands of clauses.

---

## Conceptual development

A SAT solver returns satisfiable or unsatisfiable for a finite encoding. A geometry engine returns a proof in a formal geometry language. A Collatz checker returns “all $$n\le N$$ reached 1.” Each output is an observation about a *finite* object or a *fixed* axiomatic system. The studio’s open prompts—how small can a Kakeya set be? does every $$n$$ reach 1?—remain infinite. The useful move is to write the finite object into the log as cited data, then write the still-open sentence right beside it.

## Three instruments

### 1. SAT and the hat, as a tiling studio

Smith, Myers, Kaplan, and Goodman-Strauss (2023/2024) used computational searches—including SAT-based **Heesch number** bounds (the maximum number of complete concentric rings a tile can surround itself with before getting stuck)—on the way to discovering and proving the aperiodicity of the hat monotile.

For the map-color and tiling studios, the transferable lesson is not “download a hat and stop.” It is how to **encode a local matching rule as SAT**: for instance, on a 50-region map you can define $$50 \times 3 = 150$$ Boolean variables $$x_{v,c}$$ (“region $$v$$ receives color $$c$$”), add clauses requiring “every region gets at least one color” and “adjacent regions never share a color,” and ask a solver whether a 3-coloring exists. If the solver returns **UNSAT**, you gain solid evidence that 3 colors fail on that map, letting unsatisfiability *inform* your conjecture or guide you to the obstructing subgraph (such as $$K_4$$). Kaplan’s public hat page is a model of sharing code and pictures alongside the mathematical argument.

### 2. AlphaGeometry as a geometry notebook, not an oracle

Trinh et al. (2024) show that a language model trained on 100 million synthetic geometry proofs, paired with a symbolic deduction engine, can emit readable olympiad proofs that humans can inspect line by line.

In a Kakeya or fourth-dimension studio you might use such a tool to chase or verify an elementary Euclidean lemma (for example, computing the overlap area of two slid triangles inside a Perron tree). Even so, you still owe your log two explicit sentences: (1) what was assumed when translating the problem into formal geometry, and (2) what the output *did not* establish (a finite triangle lemma does not automatically yield a continuum Hausdorff-dimension bound for Kakeya sets).

### 3. Collatz search as a bounded experiment

Barina (2021) and later GPU checks push exhaustive Collatz verification past $$N = 2^{68} \approx 2.95 \times 10^{20}$$ (and climbing, via congruence-class sieves). To appreciate the scale: checking one integer per nanosecond on a single CPU core would take nearly 10,000 years; grouping residue classes on parallel GPUs compresses that into months.

Yet the Chapter 7 iteration studio already forbids writing “checked up to $$2^{68}$$” as “true for all $$n$$.” Number theory is famous for conjectures (such as Pólya's conjecture or the inequality $$\pi(x) < \operatorname{li}(x)$$) that held across hundreds of millions—even $$10^{316}$$—cases before abruptly failing! Record the published GPU bound as one row in your table, record Terence Tao’s (2019) “almost all” theorem as a different row, and keep the universal claim explicitly **open**.

## Interpretation and insight

Computers are outstanding at filling tables and tirelessly checking billions of cases. They are poor at noticing that the table is not the theorem. The studio grade, if this course is taught, is for the log’s honesty and clarity, not for whoever owns the GPU cluster with the largest $$N$$.

## Limitations and extensions

Sphere-packing numerics, prime-gap plots, and randomness-vs-order coin-flip labs can use the exact same “microscope, not judge” discipline. Duality dictionaries and physics↔math dictionaries remain hand-drawn maps; a language model that pre-fills a table gives you a rough draft to verify row by row, not a finished dictionary.

## References

- Smith, D., Myers, J. S., Kaplan, C. S., & Goodman-Strauss, C. (2024). An aperiodic monotile. *Combinatorial Theory*, 4(1). [arXiv:2303.10798](https://arxiv.org/abs/2303.10798).
- Trinh, T. H., et al. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482.
- Barina, D. (2021). Convergence verification of the Collatz problem. *Journal of Supercomputing*, 77, 2681–2688.
- Kaplan, C. S. Hat resources: [cs.uwaterloo.ca/~csk/hat](https://cs.uwaterloo.ca/~csk/hat/).
- Studio: [Iteration]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/).

## Video tham khảo

- **xem trước** — [Discovery of the Aperiodic Monotile - Numberphile](https://www.youtube.com/watch?v=_ZS3Oqg1AX0) — Numberphile, English. Watch first. “Discovery of the Aperiodic Monotile - Numberphile” orients the lesson’s aim: After this optional studio companion you should be able to borrow three 2022–2026 computational instruments—SAT-assisted tiling, neuro-symbolic geometry search, and large-bound Col…
- [The AI that solved IMO Geometry Problems | Guest video by @Aleph0](https://www.youtube.com/watch?v=4NlrfOl0l8U) — 3Blue1Brown, English. A second pass once the main claim is in view: After this optional studio companion you should be able to borrow three 2022–2026 computational instruments—SAT-assisted tiling, neuro-symbolic geometry search, and large-bound Col…
- [UNCRACKABLE? The Collatz Conjecture - Numberphile](https://www.youtube.com/watch?v=5mFpVDpKX70) — Numberphile, English. Further depth after the first two, still tied to this lesson: After this optional studio companion you should be able to borrow three 2022–2026 computational instruments—SAT-assisted tiling, neuro-symbolic geometry search, and large-bound Col…
