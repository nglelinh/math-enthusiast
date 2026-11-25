---
layout: post
title: "Wigderson: Randomness, Proofs, and Complexity (Turing 2023)"
chapter: '09'
order: 13
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

For decades, a deceptively simple paradox split theoretical computer science: *does flipping a fair coin actually help a computer solve problems faster?* If you want to test whether a 1,000-digit integer is prime, the randomized Miller–Rabin test picks a few dozen random witnesses and answers in a blink with error probability below $$10^{-30}$$, whereas humanity needed nearly thirty more years (2002) to find a deterministic polynomial-time test (AKS)! Yet **Avi Wigderson** helped prove something even more astonishing: under natural computational hardness assumptions, **every efficient randomized algorithm can be "derandomized" into a deterministic one**—the coin flips, in the end, can be manufactured out of *computational hardness* itself!

For reshaping theoretical computer science as a pillar of modern mathematics, **Avi Wigderson** made history as the first person to win both supreme honors: the **2021 Abel Prize** (shared with László Lovász, pure mathematics) and the **2023 A.M. Turing Award** (computer science). This lecture maps Wigderson's core ideas—randomness as a resource, **hardness versus randomness**, **interactive & zero-knowledge proofs**, and **expander graphs**—best read alongside the [Abel essay on Lovász & Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/). Official materials: [amturing.acm.org](https://amturing.acm.org/), [abelprize.no](https://abelprize.no/).

---

## Learning objectives

After this lecture you should be able to explain why randomness is treated as a computational resource comparable to time and space; state the derandomization slogan that suitable hardness assumptions imply efficient pseudorandom generators and collapse of randomized complexity toward deterministic classes; describe interactive proofs as a verification model beyond static NP witnesses; name expanders as sparse yet rapidly mixing graphs used as pseudorandom objects; and relate Turing 2023 to Abel 2021 without claiming either prize solved [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/).

**Prerequisites / cross-links.** [Complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/), [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [Yao / communication & minimax]({{ site.baseurl }}/contents/en/chapter09/09_08_Yao_Complexity/), [Abel Lovász–Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/), [graphs]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/). Chapter hub: [Turing overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/).

---

## Key ideas: What Are Pseudorandomness Theory and Expander Graphs?

When undergraduates code a randomized algorithm (like randomized Quicksort or testing a polynomial identity $$P(x_1,\dots,x_n) \equiv 0$$ at random points), `random()` feels like a free black box. In **Pseudorandomness & Derandomization Theory**, however, random bits are a **precious computational resource** to be budgeted just like CPU cycles or RAM.

Three mathematical cornerstones define Wigderson's universe:
1. **Hardness vs. Randomness (Nisan–Wigderson, Impagliazzo–Wigderson):** if a function $$f$$ is sufficiently hard for small Boolean circuits, we can turn $$f$$ into a **pseudorandom generator (PRG)** that stretches a tiny seed of length $$O(\log n)$$ into $$n$$ bits indistinguishable from true randomness to every polynomial-time algorithm. Once the seed has length $$c\log n$$, we simply **loop over all $$2^{c\log n} = n^c$$ seeds** and take a majority vote—turning **BPP** into deterministic **P** with zero coin flips!
2. **Expander Graphs:** picture a million-node network where every node connects to just $$d=4$$ neighbors (ultra-sparse), yet every subset of nodes sends many edges outward (no bottlenecks anywhere). A random walk on an expander mixes to near-uniform in just $$O(\log n)$$ steps! In **error amplification**, instead of running a randomized algorithm $$k$$ times with $$k \cdot r$$ fresh bits, you spend $$r$$ bits to pick 1 starting vertex and then walk $$k$$ steps on an expander (costing only $$\log_2 d$$ bits per step) while still crushing error exponentially as $$2^{-\Omega(k)}$$!
3. **Proofs as Protocols:** together with Goldreich and Micali (1986), Wigderson proved that **every language in NP admits a zero-knowledge proof** under one-way functions—launching modern verifiable cryptography (zk-SNARKs/STARKs).

---

## 1. Two medals, one mathematical identity

Abel 2021 honored Lovász and Wigderson for making discrete mathematics and theoretical computer science **central modern mathematics**. Turing 2023 focuses the computing community’s lens on Wigderson’s complexity-theoretic leadership: randomness, circuit complexity connections, proof systems, algorithms, and decades of field-building (including the expository book *Mathematics and Computation*).

For Math Enthusiast, the dual award is pedagogical gold. Students who think “Turing = engineering” and “Abel = pure math” meet a counterexample: the same theorems about expanders, derandomization, and interactive proofs are **both**.

---

## 2. Randomness as a resource

A randomized algorithm may use coin flips. Classes such as **BPP** capture languages decidable in polynomial time with two-sided bounded error. Historically, randomness seemed to buy genuine power: polynomial identity testing, some graph algorithms, hashing, sampling, communication protocols ([Yao]({{ site.baseurl }}/contents/en/chapter09/09_08_Yao_Complexity/)).

Complexity theory asks sharper questions:

- Is randomness *essential*, or can every efficient randomized algorithm be simulated efficiently without coins?  
- What is the minimal number of random bits?  
- How does randomness interact with interaction, nonuniformity (circuits), and cryptographic pseudorandomness?

Wigderson’s body of work treats these as structural mathematics—not only algorithm engineering.

---

## 3. Hardness versus randomness

### Pseudorandom generators (PRGs)

A **PRG** stretches a short random seed into a long string that looks random to a class of efficient tests (circuits of bounded size). If strong PRGs exist, an algorithm that needs many random bits can instead enumerate seeds or use the stretched string and still succeed with comparable guarantees—**derandomization**.

### The paradigm

A deep theme of modern complexity:

> **Computational hardness** can be converted into **pseudorandomness**. If there are functions hard enough for circuits, one can build PRGs that fool smaller circuits, implying derandomization consequences such as $$\mathbf{BPP}$$ sitting in deterministic subexponential or even polynomial time under strong enough assumptions.

Conversely, nontrivial derandomization often implies circuit lower bounds. Hardness and randomness are two faces of one theory.

**Literacy caution.** These are **conditional** theorems and research programs. They do not, by themselves, resolve P vs NP. They show how a lower-bound world would yield algorithmic dividends—and how algorithmic derandomization ambitions pressure lower-bound research.

### Worked Example (Step by Step): Schwartz–Zippel Identity Testing and 20× Randomness Savings on an Expander

Compute two concrete examples by hand to feel both halves of Wigderson's program—the **power of random coins** and **replacing coins with deterministic expanders**:

**Part A — Polynomial Identity Testing (PIT) at one random point.** Suppose an arithmetic circuit computes the degree-$$2$$ polynomial:

$$
P(x_1, x_2) = (x_1 + x_2)^2 - (x_1^2 + x_2^2).
$$

Instead of expanding it (which can blow up exponentially in hundreds of variables), sample $$(x_1, x_2)$$ uniformly from $$S = \{0, 1, 2, 3, 4\}$$ ($$\vert S\vert = 5$$) and evaluate:
- By the **Schwartz–Zippel lemma**, because $$P \not\equiv 0$$, the probability of accidentally hitting a root is at most $$\dfrac{d}{\vert S\vert} = \dfrac{2}{5} = \mathbf{40\%}$$.
- Verify by exact hand count! Since $$P(x_1,x_2) = 2x_1 x_2$$, out of $$25$$ pairs in $$S \times S$$, $$P = 0$$ iff $$x_1 = 0$$ (5 pairs) or $$x_2 = 0$$ (5 pairs), minus $$(0,0)$$ double-counted: exactly $$5 + 5 - 1 = \mathbf{9}$$ pairs.
- Actual false-zero rate: $$\dfrac{9}{25} = \mathbf{36\%} \le 40\%$$. Widening $$S$$ to $$\{0,1,\dots,99\}$$ immediately drops error below $$2/100 = 2\%$$!

**Part B — Cutting random bits by 20× with an expander walk.** Suppose a BPP algorithm needs $$r = 100$$ random bits per run with error $$1/3$$, and we want $$k = 50$$ runs to crush error exponentially ($$2^{-\Omega(50)}$$):
- **Naive 50 independent runs:** costs $$50 \times 100 = \mathbf{5{,}000}$$ random bits.
- **Expander walk on an $$8$$-regular expander with $$2^{100}$$ vertices:** spend $$100$$ bits to pick 1 start vertex, then take $$49$$ random steps where each step picks 1 of $$d=8$$ neighbors using just $$\log_2 8 = \mathbf{3}$$ bits! Total randomness:

$$
100 + 49 \times 3 = \mathbf{247\text{ bits}} \quad (\text{over } \mathbf{20\times}\text{ fewer random bits!})
$$

Why do expanders mix so fast? Check the normalized walk matrix of $$K_4$$ ($$3$$-regular, $$W = \frac{1}{3}(J - I)$$): its eigenvalues are $$1, -\tfrac{1}{3}, -\tfrac{1}{3}, -\tfrac{1}{3}$$, giving spectral gap $$1 - \lambda = \tfrac{2}{3}$$. Distance from uniform shrinks as $$\lambda^t = (1/3)^t$$—after just $$t = 3$$ steps it is already $$(1/3)^3 \approx 3.7\%$$! Explicit constructions like the **zig-zag product** (Reingold–Vadhan–Wigderson) preserve a constant degree $$d$$ and spectral gap even on $$2^{100}$$ vertices.

### Explanation: Turning "Hardness" into "Pseudorandom Coins"

1. **Flip the script on hard functions:** usually we dread functions that no small circuit can compute. Wigderson saw the upside: if a Boolean function $$f$$ is so hard that no polynomial-time test predicts $$f(x)$$ better than $$50\%$$, then $$f$$'s output looks **indistinguishable from a fair coin** to every efficient algorithm!
2. **Stretch a tiny seed via a PRG:** the Nisan–Wigderson generator slices a short $$O(\log n)$$-bit seed $$s$$ into nearly disjoint subsets and feeds them into the hard function $$f$$ to emit $$n$$ pseudorandom bits.
3. **Enumerate all seeds to erase randomness completely:** once $$n$$ random bits shrink to a $$c\log n$$-bit seed, a deterministic simulator simply **loops over all $$2^{c\log n} = n^c$$ seeds** (polynomial time!) and takes the majority answer: $$\mathbf{BPP} = \mathbf{P}$$.
4. **The two-way equivalence:** Kabanets and Impagliazzo proved the converse—even derandomizing PIT (Part A) alone *implies* proving major circuit lower bounds! Hardness and derandomization are mathematically locked together.

**Quick check.** If a PRG needs seed length $$s(n) = 3\log_2 n$$ bits, how many runs does full seed enumeration take? Exactly $$2^{3\log_2 n} = n^3$$—still polynomial time! By contrast, a $$\sqrt{n}$$-bit seed requires $$2^{\sqrt{n}}$$ runs (subexponential, not yet **P**). The whole derandomization race is about squeezing seed length down to $$O(\log n)$$.

---

## 4. Interactive proofs

### Beyond NP certificates

In **NP**, a powerful prover sends a short witness; a polynomial-time verifier checks it statically. **Interactive proof systems** allow multiple rounds of communication, often with randomness in the verifier. The class **IP** equals **PSPACE** (Shamir; Lund–Fortnow–Karloff–Nisan lineage)—a landmark: interaction + randomness can verify languages believed far beyond NP.

### Zero knowledge and the culture of proofs

**Zero-knowledge proofs** convince a verifier that a statement is true without revealing anything else feasible to compute. They are central to cryptography and to the modern “proofs as protocols” worldview. Wigderson’s contributions and collaborations helped shape complexity-theoretic foundations of proof systems and randomness-efficient verification.

### Seminar moral

“Proof” in TCS is not only a static PDF of implications. It can be a **protocol** with soundness error and completeness error, analyzed like an algorithm. That conceptual shift is Turing-scale.

---

## 5. Expanders and pseudorandom objects

An infinite family of $$d$$-regular graphs is an **expander family** if small sets expand by a definite factor (equivalently, spectral gap bounded below independently of size). Expanders mix random walks rapidly despite sparsity—they are deterministic objects that **behave randomly**. (With Omer Reingold and Salil Vadhan, Wigderson also invented the **zig-zag graph product**, enabling explicit expander constructions and Reingold's breakthrough proof that undirected reachability needs only logarithmic space: $$\mathbf{SL} = \mathbf{L}$$!)

Uses include:

- derandomization and deterministic amplification;  
- error-correcting codes;  
- network design robustness;  
- pure math connections (groups, spectral geometry)—also visible in Abel narratives involving Margulis-type constructions ([Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/) adjacency).

Wigderson’s world treats expanders as standard tools, the way analysts treat Fourier bases. See also the expander section of the [Abel Lovász–Wigderson lecture]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/).

---

## 6. Complexity as geometry of efficient computation

Wigderson’s expository program presents TCS topics—circuits, reductions, randomness, optimization, cryptography—as mathematics with definitions, theorems, and open problems of Hilbert-scale difficulty. [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) remains open; around it sit completed cathedrals: IP = PSPACE, PCP theorem and hardness of approximation, expander constructions, conditional derandomization theorems, communication complexity lower bounds.

When popular writing says “complexity theory failed because P vs NP is open,” answer with a list of theorems that do not require that resolution. Lifetime prizes honor **architecture of a field**.

### Randomness-efficient error reduction

A concrete mini-theme: suppose a BPP algorithm uses many random bits and errs with probability $$1/3$$. Independent repetition reduces error exponentially but multiplies the bit cost. **Expander walks** and related pseudorandom objects can reduce error while recycling randomness more thriftily—deterministic graph structure substitutes for fresh coins. This is a miniature of the whole program: combinatorial constructions buy resource savings that naive probability would pay for with independent samples.

### Circuits, nonuniformity, and advice

Complexity distinguishes uniform algorithms (one machine for all lengths) from **circuit families** (possibly a different circuit per input length). Derandomization theorems often speak in circuit language because “tests” that a PRG must fool are nonuniform. Wigderson-style theory is comfortable moving between uniform classes (P, BPP) and nonuniform ones (P/poly), which is essential literacy for reading modern papers even if this seminar never builds a PRG from a hard function step by step.

### Zero knowledge as a definition of “knowing”

Beyond IP = PSPACE, **zero knowledge** formalizes convincing without teaching. That definition reshaped cryptography (identification protocols, modern proof systems) and philosophy-adjacent questions about knowledge. It is a flagship example of TCS exporting a *definition* as powerful as a theorem: once “zero knowledge” is precise, one can prove protocols achieve it under assumptions, compose them, and audit popular claims that a system “reveals nothing.”

### Reading Wigderson next to Yao

[Yao]({{ site.baseurl }}/contents/en/chapter09/09_08_Yao_Complexity/) emphasizes communication lower bounds and minimax transfers between randomized and distributional complexity. Wigderson emphasizes when randomness can be **removed** and when interaction enlarges proof power. Together they bookend randomness: sometimes coins are information-theoretically or complexity-theoretically necessary in a model; sometimes hardness manufactures coins good enough for efficient algorithms.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “Turing 2023 / Abel 2021 solved P vs NP.” | No. Both honor foundational contributions; P vs NP is open. |
| “BPP is just P in practice, so randomness is uninteresting.” | Practical derandomization differs from proofs; the structural theory is deep and partly conditional. |
| “Interactive proofs are the same as NP certificates.” | Interaction and randomness change the verifier model; IP = PSPACE is a major theorem. |
| “Expanders are only random graphs.” | Random graphs often expand; the point includes **explicit** constructions and deterministic use. |
| “Derandomization means deleting probability from science.” | It means removing algorithmic dependence on random bits under resource bounds—not denying probabilistic models of data. |
| “Wigderson only does lower bounds.” | The program interlocks algorithms, pseudorandomness, proofs, and education. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/wigderson-complexity/`.

**From the research pack (must-know slogans)**

- **Turing Award year is 2023** (not 2021). Abel with Lovász was **2021**.
- Randomness as resource; hardness↔randomness; expanders; interactive proofs culture.
- Book *Mathematics and Computation*; dual Abel+Turing pedagogy.

**Recommended order**

1. **Core** — Wigderson Turing Award Lecture (ACM): [https://www.youtube.com/watch?v=f2NiGO8zC1c](https://www.youtube.com/watch?v=f2NiGO8zC1c).  
2. **Orientation** — IAS Q&A Wigderson Turing: [https://www.youtube.com/watch?v=TK_vD-VnsFw](https://www.youtube.com/watch?v=TK_vD-VnsFw).  
3. **Orientation** — CACM June 2024 Wigderson feature: [https://www.youtube.com/watch?v=Ur9XNF6TeYw](https://www.youtube.com/watch?v=Ur9XNF6TeYw).  
4. **Related** — Wigderson — Reading Alan Turing (Berkeley): [https://www.youtube.com/watch?v=BiFSUniv70c](https://www.youtube.com/watch?v=BiFSUniv70c).  
5. **Cross** — Abel lectures Lovász & Wigderson: [https://www.youtube.com/watch?v=zqiL57ebP-k](https://www.youtube.com/watch?v=zqiL57ebP-k).  

**Official / primary written hubs**

- Wigderson Turing 2023 page: https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
- Wigderson Turing lecture page: https://amturing.acm.org/vp/wigderson_3844537.cfm  
- Abel 2021 Lovász & Wigderson: https://abelprize.no/abel-prize-laureates/2021  

Complete URL bibliography: `research/video-research/wigderson-complexity/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/wigderson-complexity/transcripts/` · status: `research/video-research/wigderson-complexity/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/wigderson-complexity_f2NiGO8zC1c_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/wigderson-complexity/references.md`.

1. Wigderson Turing 2023 page — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
2. Wigderson Turing lecture page — https://amturing.acm.org/vp/wigderson_3844537.cfm  
3. Wigderson Turing Award Lecture (ACM) — https://www.youtube.com/watch?v=f2NiGO8zC1c  
4. IAS Q&A Wigderson Turing — https://www.youtube.com/watch?v=TK_vD-VnsFw  
5. CACM June 2024 Wigderson feature — https://www.youtube.com/watch?v=Ur9XNF6TeYw  
6. Wigderson — Reading Alan Turing (Berkeley) — https://www.youtube.com/watch?v=BiFSUniv70c  
7. Abel 2021 Lovász & Wigderson — https://abelprize.no/abel-prize-laureates/2021  
8. Abel lectures Lovász & Wigderson — https://www.youtube.com/watch?v=zqiL57ebP-k  
9. Wikipedia — Avi Wigderson — https://en.wikipedia.org/wiki/Avi_Wigderson  
10. byyear listing (confirm 2023) — https://amturing.acm.org/byyear.cfm  
11. Mathematics and Computation (book info) — https://www.math.ias.edu/avi/book  
12. Research pack folder: `research/video-research/wigderson-complexity/`.

1. ACM Turing Award 2023 — Avi Wigderson — [amturing.acm.org](https://amturing.acm.org/).  
2. Abel Prize 2021 — Lovász & Wigderson — [abelprize.no](https://abelprize.no/).  
3. A. Wigderson, *Mathematics and Computation* (Princeton); Arora–Barak, *Computational Complexity*; Vadhan surveys on pseudorandomness.  
4. Course: [Abel Lovász–Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/); [complexity]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/); [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/); [Yao]({{ site.baseurl }}/contents/en/chapter09/09_08_Yao_Complexity/).

---

## Further directions

- Read one chapter of *Mathematics and Computation* as a pure-math audience piece.  
- Compare Yao minimax lower-bound method with PRG-based derandomization upper-bound ambitions.  
- Study a concrete expander construction sketch (even Margulis-type existence/explicitness history).  
- After IP = PSPACE awareness: peek at PCP theorem’s role in approximation hardness.  
- Next: [Modern themes survey]({{ site.baseurl }}/contents/en/chapter09/09_14_Modern_Themes/)—privacy, optimization/ML theory, coding, quantum algorithms, verification.

## Video tham khảo

- **xem trước** — [Avi Wigderson Turing Award Lecture: “Alan Turing: A TCS Role Model”](https://www.youtube.com/watch?v=f2NiGO8zC1c) — Association for Computing Machinery (ACM), English. Watch first. “Avi Wigderson Turing Award Lecture: “Alan Turing: A TCS Role Model”” orients the lesson’s aim: After this lecture you should be able to explain why randomness is treated as a computational resource comparable to time and space; state the derandomization slogan that suitable…
- [Avi Wigderson, 2023 Turing Award Laureate, Q&A with David Nirenberg | Institute for Advanced Study](https://www.youtube.com/watch?v=TK_vD-VnsFw) — Institute for Advanced Study, English. A second pass once the main claim is in view: After this lecture you should be able to explain why randomness is treated as a computational resource comparable to time and space; state the derandomization slogan that suitable…
- [June 2024 CACM: Avi Wigderson, 2023 ACM A.M. Turing Awardee](https://www.youtube.com/watch?v=Ur9XNF6TeYw) — Association for Computing Machinery (ACM), English. Further depth after the first two, still tied to this lesson: After this lecture you should be able to explain why randomness is treated as a computational resource comparable to time and space; state the derandomization slogan that suitable…
