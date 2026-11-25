---
layout: post
title: "Complexity Theory"
chapter: '06'
order: 7
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

Picture a giant $$100 \times 100$$ Sudoku grid. If someone hands you a completed board, you can verify in minutes that every row, column, and block contains the numbers 1 through 100. Hand you an empty grid with a few clues and say “solve it,” however, and finding a valid solution can blow up beyond the age of the universe. Is the gap between **checking a solution** and **finding a solution** an unbreakable law of mathematics, or have we simply missed a clever shortcut?

Some problems feel hard because we chose a clumsy algorithm. Others seem hard because **every possible algorithm** must pay an exponential price. **Computational complexity theory** classifies problems by the intrinsic resources they demand—time, memory, randomness, interaction, quantum gates—and links them via reductions. It is the mathematics of *intrinsic difficulty*, underwriting modern cryptography, algorithm design, and sober reality checks on “magical” AI or quantum claims.

This lecture maps the landscape of **P**, **NP**, NP-completeness, randomness, interactive proofs, proof barriers, and quantum classes—built for frontier literacy rather than a full encyclopedia.

---

## Key ideas: What Is Complexity Theory and What Does It Study?

Whereas practical computer science asks *“how do I write a faster program?”*, **Computational Complexity Theory** asks the far harder converse: *“how do we prove that NO program can solve this problem faster than a given bound?”* It stands on **four pillars**:

1. **Resource Classes:** Grouping problems into complexity worlds—**P** (fast to solve), **NP** (fast to verify), **PSPACE** (polynomial memory), **BPP** (randomized), and **BQP** (quantum).
2. **Reductions & Completeness:** Because proving direct lower bounds is notoriously hard, complexity builds a web of polynomial-time translations showing that solving one **NP-complete** problem fast would immediately solve thousands of others.
3. **Meta-Mathematical Barriers:** Why has $$\mathbf{P} \stackrel{?}{=} \mathbf{NP}$$ resisted proof for over fifty years? Complexity theory proves *barriers* (relativization, natural proofs, algebrization) explaining why entire families of proof techniques cannot separate P from NP.
4. **Hardness as a Resource:** Difficulty is not only bad news—cryptography and derandomization harness computational hardness as raw fuel to lock secrets and manufacture pseudorandomness.

---

## Learning objectives

After this lecture you should be able to:

- Define decision problems and the classes **P** and **NP** in plain language and with the “deterministic poly-time” / “poly-time verifiable witness” slogans.
- Explain **polynomial-time reductions** and what **NP-complete** means (and does not mean).
- State the **P vs NP** problem as an open mathematical question, not a slogan about workplace productivity.
- Describe at a high level how **randomness** (BPP), **interaction** (IP), and **quantum** (BQP) enlarge the model of computation.
- Connect one-way functions and average-case hardness intuitions to cryptography without claiming unproven separations.
- Critique common confusions (“NP means not polynomial,” “quantum computers solve NP-complete problems”).

**Prerequisites.** Algorithms at the level of “runtime grows like $$n$$, $$n\log n$$, $$n^2$$, $$2^n$$”; basic discrete math. Formal Turing machines help but are not required for the literacy goals.

---

## 1. Problems, instances, and resources

A **decision problem** is a language $$L\subseteq\{0,1\}^*$$: on input $$x$$, accept if $$x\in L$$. Complexity groups languages by the cost of the best algorithm in a model (deterministic Turing machine, circuit family, quantum circuit, …). Time complexity $$T(n)$$ is a function of input length $$n=|x|$$.

**P** is the class of languages decidable in deterministic polynomial time: there exists $$c$$ and a machine running in $$O(n^c)$$. Polynomial time is a coarse but robust proxy for “efficient” across reasonable models (Cobham–Edmonds thesis as a working convention—not a theorem about the physical universe).

Search and optimization problems are related via decision versions (e.g., “does a graph have a clique of size $$k$$?”). Approximation algorithms and hardness of approximation refine the landscape when exact solutions are intractable.

---

## 2. NP and verification

**NP** consists of languages for which membership has short **witnesses** checkable in deterministic polynomial time. Formally, $$x\in L$$ iff there exists a witness $$w$$ with $$|w|\le\operatorname{poly}(|x|)$$ such that a verifier $$V(x,w)$$ accepts in poly time. Satisfiability of Boolean formulas (**SAT**) is the canonical example: a satisfying assignment is a witness.

**Important.** $$\mathbf{NP}$$ is *not* “non-polynomial.” It is “nondeterministic polynomial” in the classical naming, or equivalently “poly-time verifiable.” Every language in **P** is in **NP** (ignore the witness). Whether $$\mathbf{P}=\mathbf{NP}$$ is open.

---

## 3. Reductions and NP-completeness

A language $$A$$ **reduces** to $$B$$ in polynomial time (Karp reduction) if there is a poly-time function $$f$$ such that $$x\in A \Leftrightarrow f(x)\in B$$. If $$B\in\mathbf{P}$$ and $$A$$ reduces to $$B$$, then $$A\in\mathbf{P}$$. Thus hardness transfers **upward** along reductions.

**Cook–Levin theorem:** SAT is **NP-complete**—it is in **NP**, and every language in **NP** reduces to it. Thousands of natural problems are NP-complete (graph coloring, Hamiltonian cycle, integer programming decision versions, …). NP-completeness is a **conditional** hardness theory: if any NP-complete problem is in **P**, then $$\mathbf{P}=\mathbf{NP}$$.

**Literacy.** NP-complete means “hardest in NP under poly-time reductions,” not “impossible,” not “requires brute force in practice for all sizes,” and not “unsolvable for instances you care about.” Structured instances may be easy; heuristics may work; average-case may differ from worst-case.

---

### Explanation: Verifying 3-SAT and Reducing It to Independent Set by Hand

Hearing that “every problem in NP reduces to another via local gadgets” can feel mysterious until you build a real reduction yourself. Let us reduce a concrete **3-SAT** formula to the graph problem **Independent Set** (finding $$k$$ vertices with no edges between them).

Take a 3-SAT formula on 3 variables with $$k = 2$$ clauses:

$$
\varphi = \underbrace{(x_1 \lor \neg x_2 \lor x_3)}_{C_1} \;\land\; \underbrace{(\neg x_1 \lor x_2 \lor \neg x_3)}_{C_2}.
$$

1. **Fast verification (why 3-SAT is in NP):** Given a candidate witness $$w = (x_1=1,\, x_2=1,\, x_3=0)$$, plug it straight in:
   - $$C_1 = (1 \lor 0 \lor 0) = 1$$ (True),
   - $$C_2 = (0 \lor 1 \lor 1) = 1$$ (True).
   Checking takes linear time—even if finding $$w$$ on 500 variables is brutal.

2. **Build the reduction graph $$G = f(\varphi)$$ (6 vertices):**
   - **One triangle per clause:** Clause $$C_1$$ becomes a 3-vertex triangle labeled $$(x_1^{(1)},\, \neg x_2^{(1)},\, x_3^{(1)})$$; clause $$C_2$$ becomes a triangle $$(\neg x_1^{(2)},\, x_2^{(2)},\, \neg x_3^{(2)})$$. Because every triangle is fully connected, any independent set can pick **at most 1 vertex** per triangle.
   - **Add edges between contradictory literals:** Connect $$x_1^{(1)}$$ to $$\neg x_1^{(2)}$$, $$\neg x_2^{(1)}$$ to $$x_2^{(2)}$$, and $$x_3^{(1)}$$ to $$\neg x_3^{(2)}$$. These edges forbid setting the same variable both True and False!

3. **Verify the two-way equivalence by hand:**
   - **Forward:** From our satisfying assignment $$(1, 1, 0)$$, pick one True literal from each clause: $$x_1^{(1)}$$ from triangle 1 and $$x_2^{(2)}$$ from triangle 2. Check the graph: there is **no edge** between $$x_1^{(1)}$$ and $$x_2^{(2)}$$, so $$\{x_1^{(1)},\, x_2^{(2)}\}$$ is an independent set of size $$k = 2$$!
   - **Backward:** Any independent set of size $$2$$ must pick 1 vertex from each triangle, and the two chosen literals cannot contradict each other (no edge between them). Setting those two literals True satisfies both clauses automatically!

Translating $$\varphi \mapsto G$$ runs in linear time. Therefore, if anyone ever discovers a polynomial-time algorithm for Independent Set, we immediately get a polynomial-time solver for 3-SAT—collapsing all of **NP** into **P**.

## 4. Beyond P and NP: a postcard of classes

| Class / idea | Intuition |
|--------------|-----------|
| **PSPACE** | Polynomial memory (may use exponential time) |
| **EXPTIME** | Exponential time |
| **BPP** | Randomized poly-time with bounded error |
| **IP** | Interactive proofs; $$\mathbf{IP}=\mathbf{PSPACE}$$ (famous theorem) |
| **#P** | Counting solutions (e.g., number of satisfying assignments) |
| **PH** | Polynomial hierarchy (alternating quantifiers) |
| **BQP** | Bounded-error quantum poly-time |

Inclusions that are known are limited; many separations are open. Relativization, natural proofs, and algebrization are **barrier results** explaining why certain proof techniques cannot separate **P** from **NP** easily. This is meta-mathematics of complexity: understanding *why the question is hard*.

---

## 5. Randomness and derandomization

Randomized algorithms (polynomial identity testing, some graph algorithms historically) sit in **BPP**. A major theme is **derandomization**: under circuit lower-bound hypotheses, randomness may not enlarge poly-time power much ($$\mathbf{P}=\mathbf{BPP}$$ in some conjectural worlds). Pseudorandom generators connect hardness to randomness—another bridge to cryptography.

---

## 6. Average-case hardness and cryptography

Cryptography needs problems that are hard **on average** for efficiently sampleable distributions, not only worst-case monsters. One-way functions, pseudorandom generators, and public-key assumptions formalize this. There are deep results linking worst-case lattice problems to average-case LWE-type problems—rare and precious reductions. Complexity theory supplies the language; cryptanalysis and concrete security supply the numbers.

**Fine-grained complexity** (SETH, 3SUM-hardness, APSP hardness) studies precise polynomial exponents and conditional lower bounds for problems inside **P**—highly relevant to algorithm engineering. A quadratic-time algorithm for all-pairs shortest paths in dense graphs would refute popular fine-grained hypotheses; that is a different flavor of “hardness” than NP-completeness, aimed at the polynomial regime where most day-to-day algorithms live.

### Approximation and promise problems

When exact optimization is NP-hard, one asks for approximate solutions within factor $$\rho$$. The PCP theorem and hardness-of-approximation web explain why some ratios are impossible under $$\mathbf{P}\neq\mathbf{NP}$$. Promise problems (yes/no instances separated by a gap) appear in property testing and quantum complexity. These refinements matter when someone claims an AI system “solves” a hard combinatorial problem: often it approximates, restricts instance families, or uses exponential time on small $$n$$.

---

## 7. Quantum complexity (link)

**BQP** contains problems solvable efficiently on quantum computers with bounded error. Factoring is in **BQP** (Shor); it is not known to be in **P**, and not believed NP-complete. Quantum computers are not known to solve NP-complete problems in poly time; Grover gives quadratic black-box speedups for unstructured search, which still leaves exponential scaling for generic brute force over $$n$$-bit search spaces of size $$2^n$$.

See [Quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/) and [Cryptography frontiers]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/).

---

## 8. Complexity, AI, and hype

Machine learning practice often solves **heuristic** instances of hard problems (nonconvex optimization, formal verification, combinatorial search). Success on benchmarks is not a complexity-theoretic collapse of **P** vs **NP**. Conversely, NP-completeness of a formulation does not prove a real-world task is hopeless—encoding choices matter.

Circuit complexity and proof complexity connect to questions about what shallow neural nets or short proofs can represent—active interfaces, not slogans.

### A worked reduction cartoon (SAT → 3-coloring idea)

You need not memorize every classic reduction, but you should feel the *shape*. To show that problem $$B$$ is NP-hard, exhibit a poly-time $$f$$ such that formula $$\varphi$$ is satisfiable if and only if $$f(\varphi)$$ is a yes-instance of $$B$$. For graph 3-colorability, textbooks build a graph whose legal 3-colorings encode truth assignments and clause constraints: local gadgets force variables to two “truth colors,” and clause gadgets are colorable exactly when at least one literal is true. The details are fiddly; the meta-lesson is clean:

> **Hardness is contagious along poly-time reductions; easiness is contagious in the opposite direction.**

If tomorrow someone publishes a genuine poly-time algorithm for any NP-complete problem, the entire class **NP** collapses into **P**. That is why casual claims of “I solved an NP-complete problem efficiently” deserve cryptographic levels of scrutiny: either the instances were special, the algorithm is heuristic/exponential in the worst case, the encoding is wrong, or something historic has happened.

### What complexity *does not* say

Complexity theory is asymptotic and model-relative. It does not tell you the constant factors on your laptop, the best MIP solver cutoff for a 200-variable industrial IP, or whether a neural net will crack your puzzle contest. It *does* tell you which hopes require a conceptual breakthrough (poly-time SAT) versus engineering (better heuristics, average-case structure, approximation, parameterized algorithms). **Parameterized complexity** (FPT vs W-hierarchy) refines “hard” by measuring cost in a parameter $$k$$ (treewidth, solution size, …): some NP-hard problems are fixed-parameter tractable, which is a theorem-shaped escape hatch for practice.

---

## Common confusions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “NP means not polynomial.” | False etymology in popular use | NP = nondeterministic poly-time / poly-time verifiable. |
| “P vs NP is about whether hard work matters.” | Category error | It is a precise question about asymptotic algorithms for decision languages. |
| “NP-complete problems cannot be solved.” | False | They are solved daily at modest sizes; hardness is asymptotic worst-case (conditional). |
| “Quantum computers solve NP-complete problems.” | Unsupported | No known poly-time quantum algorithm for NP-complete problems. |
| “If P=NP, cryptography dies instantly in all forms.” | Too blunt | Much public-key crypto would be impacted; symmetric crypto and information-theoretic settings differ. |
| “A neural net got 99% on a hard puzzle ⇒ P=NP.” | Fail | Empirical performance ≠ proof of general poly-time decision procedure. |

---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/complexity-theory/analysis.md`.

### Status

**P vs NP remains open** (as of 2026). NP-completeness theory is mature; circuit lower bounds and derandomization are major frontiers.

### Core statement / slogan

Cook–Levin: SAT is NP-complete. Thousands of natural problems are NP-complete via poly-time reductions. P=NP? is open; most experts conjecture P≠NP.

### Definitions to freeze

- **P / NP.** P: decidable in poly time. NP: verifiable in poly time given a witness.
- **Reduction.** Poly-time many-one map preserving yes/no answers.

### Hygiene (from confusions log)

- Thinking NP means 'not polynomial' (it means nondeterministic poly / verifiable).
- Claiming AI solves NP-complete problems 'in general' in poly time.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/complexity-theory/`.

**Recommended order**

1. **Core** — Michael Sipser — Beyond Computation: P vs NP (Harvard): [https://www.youtube.com/watch?v=msp2y_Y5MLE](https://www.youtube.com/watch?v=msp2y_Y5MLE).  
2. **Foundation** — MIT OCW Sipser — NP-Completeness lecture: [https://www.youtube.com/watch?v=iZPzBHGDsWI](https://www.youtube.com/watch?v=iZPzBHGDsWI).  
3. **Orientation** — Quanta — Biggest Puzzle in CS: P vs NP (course-linked): [https://www.youtube.com/watch?v=pQsdygaYcE4](https://www.youtube.com/watch?v=pQsdygaYcE4).  

**Status reminder:** **P vs NP remains open** (as of 2026). NP-completeness theory is mature; circuit lower bounds and derandomization are major frontiers.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/complexity-theory/transcripts/` · status: `research/video-research/complexity-theory/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/complexity-theory_msp2y_Y5MLE_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References and further reading

1. Arora & Barak. *Computational Complexity: A Modern Approach*.
2. Sipser. *Introduction to the Theory of Computation* (accessible core).
3. Cook (1971); Levin; Karp’s reducibility paper — historical NP-completeness.
4. Survey notes on complexity barriers (relativization, natural proofs).
5. Wigderson. *Mathematics and Computation* — broad vision essay/book.
6. Course links: [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/), [Quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/), [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).

---


Full URL bibliography from video research: `research/video-research/complexity-theory/references.md`.

### Videos (recommended path)

- Michael Sipser — Beyond Computation: P vs NP (Harvard) (CORE): https://www.youtube.com/watch?v=msp2y_Y5MLE
- MIT OCW Sipser — NP-Completeness lecture (FOUNDATION): https://www.youtube.com/watch?v=iZPzBHGDsWI
- Quanta — Biggest Puzzle in CS: P vs NP (course-linked) (ORIENTATION): https://www.youtube.com/watch?v=pQsdygaYcE4

### Papers and web (from research pack)

- Wikipedia — P versus NP: https://en.wikipedia.org/wiki/P_versus_NP
- Clay Math — P vs NP: https://www.claymath.org/millennium-problems/p-vs-np-problem
- Wikipedia — NP-completeness: https://en.wikipedia.org/wiki/NP-completeness
- MIT OCW 18.404J Theory of Computation: https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/
- Wikipedia — Complexity class: https://en.wikipedia.org/wiki/Complexity_class
- Wikipedia — Cook–Levin theorem: https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem

### Course

- Research pack: `research/video-research/complexity-theory/` (especially `references.md`, `learning_path.md`).

## Further directions

- **Apply hardness:** [Cryptography frontiers]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/).
- **Quantum classes:** [Quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/).
- **Practice:** implement exponential vs poly algorithms for a small NP-complete problem (e.g., brute-force SAT on $$n\le 20$$) and plot wall-clock scaling.
- **Reading path:** Sipser NP chapter → one reduction diagram a day → Arora–Barak sampling.
- Keep a class inclusion postcard and annotate what is theorem vs conjecture.

## Video tham khảo

- **xem trước** — [Beyond Computation: The P vs NP Problem - Michael Sipser](https://www.youtube.com/watch?v=msp2y_Y5MLE) — PoincareDuality, English. Watch first. “Beyond Computation: The P vs NP Problem - Michael Sipser” orients the lesson’s aim: Define decision problems and the classes P and NP in plain language and with the “deterministic poly-time” / “poly-time verifiable witness” slogans.
- [15. NP-Completeness](https://www.youtube.com/watch?v=iZPzBHGDsWI) — MIT OpenCourseWare, English. A second pass once the main claim is in view: Define decision problems and the classes P and NP in plain language and with the “deterministic poly-time” / “poly-time verifiable witness” slogans.
- [P vs NP Explained: Computer Science's Biggest Puzzle](https://www.youtube.com/watch?v=pQsdygaYcE4) — Quanta Magazine, English. Further depth after the first two, still tied to this lesson: Define decision problems and the classes P and NP in plain language and with the “deterministic poly-time” / “poly-time verifiable witness” slogans.
