---
layout: post
title: "Lovász & Wigderson: Discrete Math and Theoretical CS (Abel 2021)"
chapter: '08'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter08
lesson_type: required
---

There was a time in traditional mathematics departments when graphs, networks, and algorithm speed were treated as the suburbs—useful for computer engineers, perhaps, yet somehow less grand than algebraic geometry or functional analysis. Yet out of those "suburbs" came one of humanity’s deepest open questions ($$P \text{ vs } NP$$), alongside structures that shook cryptography, optimization, and pure mathematics itself: how do you prove a valid combinatorial configuration exists amid a million overlapping constraints? And does flipping a coin genuinely make a computer smarter?

In **2021**, the **Abel Prize** was awarded jointly to **László Lovász** and **Avi Wigderson** as a historic declaration by the mathematical community:

> “for their foundational contributions to theoretical computer science and discrete mathematics, and their leading role in shaping them into central fields of modern mathematics.”  
> — [Abel Prize Committee citation](https://abelprize.no/abel-prize-laureates/2021)

From the Lovász Local Lemma and LLL lattice reduction to Wigderson’s revolution in derandomization, zero-knowledge proofs, and expander graphs, these two careers moved discrete mathematics and theoretical computer science (TCS) straight into the center of modern mathematics—right next to [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), even while that million-dollar problem remains open. Official materials: [abelprize.no](https://abelprize.no/).

**Lesson arc:** Key ideas (discrete mathematics, complexity theory, hardness as a resource) → Lovász and the Local Lemma → Explanation: comparing the Union Bound vs. the Lovász Local Lemma on $$10$$-SAT and computing graph spectral gaps by hand → Wigderson, derandomization, and expanders → Beside P vs NP and common confusions.

---

## Learning objectives

After this lecture you should be able to explain why discrete math/TCS earned an Abel-scale recognition as central modern mathematics; name the Lovász local lemma and its purpose (existence amid many mostly independent bad events); state Wigderson’s randomness / derandomization theme; describe expanders as sparse yet highly connected graphs; and relate all of this to P vs NP **without** claiming that problem is solved.

**Prerequisites.** Graphs at the level of vertices and edges; basic probability (independence, union bounds); the idea that algorithms consume time as a function of input size. Cross-links: [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [graph theory & networks]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/), [Furstenberg–Margulis expanders mention]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/).

---

## Key ideas: What Are Discrete Mathematics and Computational Complexity Theory, and What Do They Study?

While calculus and differential geometry study the **continuous** world (smooth curves, flows, derivatives), the two fields of Lovász and Wigderson study the **discrete** world—with structural depth every bit as profound:

### 1. Discrete Mathematics and Geometric Graph Theory (Lovász)
This field studies countable, separated structures: graphs (modeling social networks, power grids, molecules), hypergraphs, combinatorics, integer lattices, and discrete optimization. One of Lovász’s signature discoveries is that the sharpest way to understand a discrete graph is often to **embed it in continuous geometry**—using matrices, eigenvalues, convex polytopes, and semidefinite programming.

### 2. Computational Complexity Theory (TCS)
Complexity theory does not care whether you code in Python or C++, or how fast your CPU clock runs. It asks about the **fundamental limits of computation**: as input size $$n$$ grows, how much time, memory, randomness, or communication does a problem inherently require? Complexity classes like **P** (fast deterministic time), **NP** (fast verification), and **BPP** (fast with coin flips) map the intrinsic hardness of the entire universe of problems.

### 3. Hardness as a Constructive Resource (Wigderson)
Surprisingly, computational hardness is not just bad news—it is the **raw material** behind internet cryptography, zero-knowledge proofs, and pseudorandom generators that fool every efficient algorithm.

---

## 1. A cultural prize as well as a scientific one

Graphs, algorithms, and complexity were once treated as peripheral to “core” pure mathematics in some institutional cultures—important, yes, but siloed in computer science departments. Abel 2021 is a public affirmation that these areas host **deep structure theorems** and interact with geometry, algebra, and probability at the highest level.

The citation’s second clause matters: “shaping them into central fields of modern mathematics.” That is field-building, mentorship, books, problems lists, and decades of theorems—not a single headline result.

---

## 2. Lovász: discrete mathematics as a mathematical science

### Graphs, optimization, geometry, and LLL

Lovász’s work spans graph theory, combinatorial optimization, and geometric representations of graphs. A recurring theme is that discrete objects carry continuous shadows: the **Lovász theta function** (using semidefinite programming to bound Shannon capacity), the **LLL lattice-reduction algorithm** (Lenstra–Lenstra–Lovász, finding short basis vectors in integer lattices—famous in polynomial factoring, cryptanalysis, and post-quantum cryptography), and **graph limits (graphons)** that view billion-vertex graphs as continuous analytic functions.

### The Lovász local lemma

The **local lemma** (Erdős–Lovász, 1975) is a profound existence principle. Suppose you have many “bad events” $$A_1, \dots, A_m$$, each occurring with probability at most $$p$$, and each depending on at most $$d$$ other bad events (*limited dependence*). As long as $$e \cdot p \cdot (d + 1) \le 1$$, no matter how astronomically large $$m$$ is, the probability that **none** of the bad events occur is strictly positive:

$$
\mathbb{P}\Big(\bigcap_{i=1}^m A_i^c\Big) > 0.
$$

Union bounds collapse when $$m$$ is huge; full independence fails when events overlap. The local lemma thrives right in the realistic middle regime: **limited dependence**.

### Explanation: Union Bound vs. Lovász Local Lemma and Graph Spectral Gaps by Hand

#### Example 1: Where the Union Bound collapses and the Local Lemma wins decisively
Consider a massive **$$10$$-SAT** Boolean formula with $$m = 1{,}000{,}000$$ clauses, where each clause is the OR of $$k = 10$$ literals, and each clause shares variables with at most $$d = 300$$ other clauses. Assign every variable True/False independently with probability $$1/2$$.
- The probability that a single clause is *falsified* (all 10 literals evaluate to False) is:
  $$
  p = 2^{-10} = \frac{1}{1024} \approx 0.0009766.
  $$
- **Classical Union Bound:** The sum of bad probabilities is $$m \cdot p = 1{,}000{,}000 / 1024 \approx \mathbf{976.6 > 1}$$ — completely useless!
- **Lovász Local Lemma:** We only check the local quantity (notice $$m = 1{,}000{,}000$$ vanishes completely!):
  $$
  e \cdot p \cdot (d + 1) \approx 2.7183 \times \frac{301}{1024} \approx \mathbf{0.799 \le 1}!
  $$
  The condition holds! The Local Lemma immediately guarantees that **at least one assignment satisfies all one million clauses simultaneously**—and the same proof still works for a trillion clauses as long as each overlaps with at most $$300$$ others! (Later, Moser and Tardos turned this existence lemma into a fast, simple algorithm.)

#### Example 2: Feeling a graph’s "spectral gap" through eigenvalues
For the adjacency matrix $$A$$ of a $$d$$-regular graph (every vertex has degree $$d$$), the largest eigenvalue is always $$\lambda_1 = d$$. The farther the second eigenvalue $$\lambda_2$$ stays below $$d$$, the faster the graph **expands** and mixes:
- **Cycle graph $$C_6$$** ($$6$$ vertices in a ring, degree $$d = 2$$): eigenvalues are $$2\cos(2\pi k/6)$$ for $$k = 0..5$$, namely $$2, 1, 1, -1, -1, -2$$. Here $$d - \lambda_2 = 1$$, but as $$n$$ grows in $$C_n$$, $$\lambda_2 = 2\cos(2\pi/n) \to 2$$ so the spectral gap collapses to $$0$$—rings are **not** expanders!
- **Complete graph $$K_4$$** ($$4$$ vertices all connected, degree $$d = 3$$): adjacency matrix $$J - I$$ has $$\lambda_1 = 3$$ and $$\lambda_2 = -1$$, a huge spectral gap! The hard art of building **expanders** is keeping the degree $$d$$ tiny and fixed (like $$d = 4$$) even as $$n \to \infty$$, while keeping $$\lambda_2 \le d - c$$ bounded safely away from $$d$$!

### Field-building

Beyond theorems, Lovász’s influence includes shaping discrete mathematics as a discipline with standards of proof, connections to geometry and optimization, and a global research community. Abel language about “leading role” points here.

---

## 3. Wigderson: randomness, complexity, and pseudorandomness

### Randomness as a resource

A central Wigderson theme: when do **randomized algorithms** outperform deterministic ones, and what is the power of randomness as a computational resource? Many algorithms flip coins—Monte Carlo primality tests historically, hashing, sampling, communication protocols. Complexity theory asks whether that randomness is essential or merely convenient ($$\mathrm{BPP} \stackrel{?}{=} \mathrm{P}$$).

### Derandomization

**Derandomization** asks when randomness can be removed—often under **hardness assumptions** (**Hardness vs. Randomness**: suitable hard functions imply pseudorandom generators). If the world contains enough computational hardness, then efficient deterministic simulations of randomized algorithms exist. This links complexity lower bounds to algorithm design in a deep way.

### Expanders, interactive proofs, and bridges to pure math

**Expander graphs** are sparse yet highly connected—random-like mixing with few edges. Wigderson and collaborators invented the combinatorial **zig-zag product** to build expanders explicitly, leading to Reingold’s breakthrough showing undirected connectivity uses only logarithmic space ($$\mathrm{SL} = \mathrm{L}$$). Interactive proofs, **zero-knowledge proofs** (proving any NP statement is true without revealing a single secret bit), and the structure of complexity classes form another major arc. Wigderson’s book *Mathematics and Computation* presents TCS as mathematics for a broad audience of mathematicians.

---

## 4. Expanders: a junction map

An infinite family of $$d$$-regular graphs $$\{G_n\}$$ is an **expander family** if the spectral gap (or Cheeger constant) is bounded below independently of $$n$$. Equivalently, small sets expand: neighborhood sizes grow by a definite factor.

Consequences:

- random-walk mixing is fast ($$O(\log n)$$ steps to spread almost uniformly);  
- error-correcting codes and derandomization gain explicit objects;  
- pure mathematics gains spectral graph theory and group-theoretic constructions.

Lovász’s structural/geometric graph theory and Wigderson’s pseudorandomness meet at expanders. Abel 2021 sits at that junction—and Abel 2020’s Margulis already touched expanders from dynamics/groups.

---

## 5. Beside P vs NP

[P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) remains open. Abel 2021 does **not** resolve it. Lovász–Wigderson work is the **toolkit and worldview** surrounding computational hardness: positive results, structural theory, randomness, optimization, and the mathematical legitimacy of discrete complexity.

A healthy seminar habit: list three “positive” TCS theorems that do not need a resolution of P vs NP (local lemma applications; expander constructions; interactive proof theorems; approximation algorithms under complexity assumptions; …). Lifetime mathematics includes the architecture of a field, not only its Everest.

### Hardness as a mathematical object

Even without settling P vs NP, complexity theory treats **hardness** as something one can *use*: reductions, completeness, conditional lower bounds, and cryptographic assumptions. Wigderson’s program often turns hardness into a constructive resource—pseudorandom generators that fool efficient tests—so that algorithmic design and lower-bound thinking become two faces of one subject. Lovász’s combinatorial optimization similarly treats discrete structure as geometry: polytopes, dualities, and approximation thresholds that are theorems, not mere heuristics.

For this course, the moral is aligned with Chapter 01’s open problems: **an unsolved flagship does not make a field empty**. Around P vs NP sits a mature mathematical civilization.

---

## 6. Why this is Abel-scale

Two careers, one message: discrete mathematics and TCS are not second-class citizens in pure mathematics. They have:

- deep theorems with geometric and algebraic content;  
- methods exported to other fields;  
- open problems of Hilbert-scale difficulty (P vs NP among them);  
- infrastructures (expanders, pseudorandom generators, combinatorial lemmas) used across sciences.

The Abel committee’s wording—“central fields of modern mathematics”—is the thesis of this lecture.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “Abel 2021 solved P vs NP.” | No. The prize honors foundational contributions and field-shaping; P vs NP is open. |
| “Discrete math is only algorithms.” | It includes structural graph theory, extremal combinatorics, optimization theory, and more. |
| “Randomized algorithms are always better.” | Randomness is a resource with costs and with derandomization programs; it is not magic. |
| “Expanders are just random graphs.” | Random graphs often expand; the point is **explicit** constructions and deterministic use. |
| “Local lemma needs full independence.” | It needs **limited dependence**, carefully quantified. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/lovasz-wigderson/`.

**From the research pack (must-know slogans)**

- Abel 2021: foundational contributions to TCS and discrete math; shaping them into central modern mathematics.
- Lovász: graph theory, optimization, local lemma, geometric graph theory.
- Wigderson: randomness, complexity, expanders, proof systems — later **Turing Award 2023** (not 2021).
- Does **not** solve P vs NP.

**Recommended order**

1. **Core** — Abel lectures Lovász & Wigderson: [https://www.youtube.com/watch?v=zqiL57ebP-k](https://www.youtube.com/watch?v=zqiL57ebP-k).  
2. **History** — Abel interview Lovász & Wigderson: [https://www.youtube.com/watch?v=VAk0rtlKtMA](https://www.youtube.com/watch?v=VAk0rtlKtMA).  
3. **Orientation** — WFSJ meet Lovász & Wigderson: [https://www.youtube.com/watch?v=J4yssMTZqC4](https://www.youtube.com/watch?v=J4yssMTZqC4).  
4. **Orientation** — Short interview Lovász: [https://www.youtube.com/watch?v=wg0di8dK0eI](https://www.youtube.com/watch?v=wg0di8dK0eI).  
5. **Orientation** — Short interview Wigderson: [https://www.youtube.com/watch?v=5VxOhzNv9To](https://www.youtube.com/watch?v=5VxOhzNv9To).  

**Official / primary written hubs**

- Abel 2021 Lovász & Wigderson: https://abelprize.no/abel-prize-laureates/2021  
- ACM Turing — Wigderson 2023: https://amturing.acm.org/award_winners/wigderson_3844537.cfm  

Complete URL bibliography: `research/video-research/lovasz-wigderson/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/lovasz-wigderson/transcripts/` · status: `research/video-research/lovasz-wigderson/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/lovasz-wigderson_zqiL57ebP-k_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/lovasz-wigderson/references.md`.

1. Abel 2021 Lovász & Wigderson — https://abelprize.no/abel-prize-laureates/2021  
2. Abel lectures Lovász & Wigderson — https://www.youtube.com/watch?v=zqiL57ebP-k  
3. Abel interview Lovász & Wigderson — https://www.youtube.com/watch?v=VAk0rtlKtMA  
4. WFSJ meet Lovász & Wigderson — https://www.youtube.com/watch?v=J4yssMTZqC4  
5. Short interview Lovász — https://www.youtube.com/watch?v=wg0di8dK0eI  
6. Short interview Wigderson — https://www.youtube.com/watch?v=5VxOhzNv9To  
7. NYT Abel 2021 — https://www.nytimes.com/2021/03/17/science/abel-prize-mathematics.html  
8. Nature Abel 2021 — https://www.nature.com/articles/d41586-021-00694-9  
9. ACM Turing — Wigderson 2023 — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
10. Wikipedia — Avi Wigderson — https://en.wikipedia.org/wiki/Avi_Wigderson  
11. Research pack folder: `research/video-research/lovasz-wigderson/`.

1. Abel Prize 2021 — [abelprize.no/abel-prize-laureates/2021](https://abelprize.no/abel-prize-laureates/2021).  
2. A. Wigderson, *Mathematics and Computation* (Princeton).  
3. N. Alon–J. Spencer, *The Probabilistic Method*; S. Arora–B. Barak, *Computational Complexity*.  
4. Course: [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/); [graphs]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/).

---


## Hardness as a mathematical object

Theoretical computer science treats **computational hardness** not as an annoyance but as a resource and a structure theory. One-way functions (if they exist) enable cryptography; average-case hardness differs from worst-case NP-completeness; fine-grained hypotheses refine P vs NP into precise running-time barriers. Lovász’s combinatorial geometry and Wigderson’s complexity worldview together show discrete mathematics generating **definitions as deep as any continuum theory**.

## Seminar prompt

List three theorems in TCS that remain interesting even if P = NP (e.g. communication complexity lower bounds, or coding theory limits). Explain why in two sentences each.

## Further directions

- Local lemma exercise: invent a toy bad-event setup (coloring, packing, scheduling).  
- Compare expander constructions historically (Margulis; later zigzag products; Ramanujan graphs).  
- Compare with a related [Fields essay]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/).  
- Note one precise open question: P vs NP; stronger derandomization; explicit constructions with optimal parameters.  
- Next: [Dennis Sullivan]({{ site.baseurl }}/contents/en/chapter08/08_07_Sullivan_Topology/).

## Video tham khảo

- **xem trước** — [The Abel lectures: László Lovász and Avi Wigderson](https://www.youtube.com/watch?v=zqiL57ebP-k) — The Abel Prize, English. Watch first. “The Abel lectures: László Lovász and Avi Wigderson” orients the lesson’s aim: After this lecture you should be able to explain why discrete math/TCS earned an Abel-scale recognition as central modern mathematics; name the Lovász local lemma and its purpose (…
- [Avi Wigderson & László Lovász - The Abel Prize interview 2021](https://www.youtube.com/watch?v=VAk0rtlKtMA) — The Abel Prize, English. A second pass once the main claim is in view: After this lecture you should be able to explain why discrete math/TCS earned an Abel-scale recognition as central modern mathematics; name the Lovász local lemma and its purpose (…
- [Interview with László Lovász and Avi Wigderson](https://www.youtube.com/watch?v=J4yssMTZqC4) — The Abel Prize, English. Further depth after the first two, still tied to this lesson: After this lecture you should be able to explain why discrete math/TCS earned an Abel-scale recognition as central modern mathematics; name the Lovász local lemma and its purpose (…
