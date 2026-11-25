---
layout: post
title: "Can mathematics describe infinity?"
chapter: '07'
order: 8
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Course links**  
> [Beautiful infinity / Cantor themes in Ch.4–5 if present]({{ site.baseurl }}/contents/en/) · [Collatz studio]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/) · [Prime studio]({{ site.baseurl }}/contents/en/chapter07/07_04_Explore_Prime_Predictability/) · [Fourth dimension]({{ site.baseurl }}/contents/en/chapter07/07_06_Explore_Fourth_Dimension/)

In the late nineteenth century, when most mathematicians still treated "infinity" as something to admire only from afar through limits, Georg Cantor dared to put infinity on a balance scale and **weigh one infinity against another**. What he discovered startled even his own former teacher, Leopold Kronecker: there is not just *one* infinity, but an **endless tower of strictly larger infinities**—the real numbers $$\mathbb{R}$$ genuinely outnumber the natural numbers $$\mathbb{N}$$ by an unbridgeable gulf!

Popular-science riddles like *"Is infinity plus one bigger than infinity?"* or *"Are there half as many even numbers as integers?"* sound paradoxical only because one word—"infinity"—is doing four different jobs at once: potential infinity in calculus, cardinals for size, ordinals for order, and points at infinity in projective geometry. This studio puts Cantor's measuring stick directly in your hands: you will build explicit bijections, run the diagonal argument on paper, and dissolve famous paradoxes with exact definitions.

**Lesson roadmap:** Key ideas (set theory, ZFC axioms & cardinals vs. ordinals) → Potential vs. actual infinity → Explanation: hand-checking Cantor's pairing function $$\pi(i,j)$$ and a $$5\times 5$$ binary diagonal table → Hilbert's Hotel & the Continuum Hypothesis → Studio experiments & log.

---

## Learning objectives

After this studio you should be able to:

- Distinguish **potential** infinity (unending process) from **actual** infinity (a completed set such as $$\mathbb{N}$$).
- Construct explicit bijections showing $$\lvert\mathbb{N}\rvert=\lvert\mathbb{Z}\rvert=\lvert\mathbb{N}\times\mathbb{N}\rvert$$ (countable infinity).
- Present Cantor’s diagonal argument that $$\mathbb{R}$$ (or $$\{0,1\}^{\mathbb{N}}$$) is uncountable.
- Explain Hilbert’s hotel as a story about countably infinite sets absorbing additions and even countable unions of countable sets.
- Point to where calculus “hides” infinity (limits, series, improper integrals) without treating $$\infty$$ as a real number.
- Keep paradoxes (Zeno, hotel, Galileo’s squares) in a **resolution box**: which definition dissolves the paradox?

**Prerequisites.** Functions, injections/surjections/bijections, basic proof writing, sequences and series at calculus level.

---

## Key ideas: What Are Set Theory and the Foundations of Mathematics?

Every branch of university mathematics—analysis, linear algebra, probability—rests on a single basement floor: **Set Theory** and **Mathematical Logic**. This field is built on three major pillars:

### 1. Measuring Infinity via Bijections: Cardinals vs. Ordinals

For finite sets, we count $$1, 2, 3\dots$$ For infinite sets, Cantor replaced counting with **one-to-one pairing (bijection)**: if every guest sits in one chair and no chair is empty, there are as many guests as chairs without counting either! This splits infinity into two distinct arithmetics:
- **Cardinals (pure size):** $$\aleph_0 = \lvert\mathbb{N}\rvert$$, $$\mathfrak{c} = 2^{\aleph_0} = \lvert\mathbb{R}\rvert$$. For cardinals, $$\aleph_0 + 1 = \aleph_0$$.
- **Ordinals (order type):** Compare $$1, 2, 3, \dots$$ (order type $$\omega$$) with $$2, 3, 4, \dots; 1$$—the same natural numbers with $$1$$ pushed behind all the others (order type $$\omega + 1$$). As bare sets they have the exact same *cardinality* ($$\aleph_0$$), yet as *ordered* sets they differ: the second has a largest element ($$1$$) while the first does not!

### 2. The ZFC Axioms (Zermelo–Fraenkel with Choice)

In the early twentieth century, Russell's paradox (*"Does the set $$R = \{x : x \notin x\}$$ contain itself?"*) showed that naive set theory can self-destruct. Mathematicians built the axiomatic system **ZFC** as a precise constitution governing which sets exist without generating contradictions.

### 3. Independence and the Limits of Formal Proof

Kurt Gödel (1940) and Paul Cohen (1963) proved a landmark result: the **Continuum Hypothesis (CH)**—asking whether any infinite size sits strictly between $$\aleph_0$$ and $$2^{\aleph_0}$$—is **independent** of ZFC. Neither CH nor its negation can be proved from the standard axioms of mathematics!

---

## 1. Background mathematics

### 1.1 Potential versus actual

Aristotelian **potential infinity** is the idea that a process can continue without end: you can always write a larger natural number; you need not accept “the set of all naturals” as a finished object. Modern calculus often speaks potentially: $$\lim_{n\to\infty}a_n=L$$ means a finite challenge-response with $$\varepsilon$$ and $$N$$, never a number called $$\infty$$ in $$\mathbb{R}$$.

**Actual infinity** treats infinite sets as objects. Cantor’s theory assigns **cardinalities**: two sets have the same cardinality if there is a bijection between them. Both modes are useful; confusion begins when one switches without notice.

### 1.2 Countable infinity

A set is **countably infinite** if it is equinumerous with $$\mathbb{N}=\{0,1,2,\ldots\}$$. Classic bijections:

- $$\mathbb{N}\leftrightarrow\mathbb{Z}$$: explicit formula
  $$
  f(n)=\begin{cases} n/2 & n\text{ even},\\ -(n+1)/2 & n\text{ odd},\end{cases}
  $$
  listing $$0, -1, 1, -2, 2, \dots$$
- $$\mathbb{N}\leftrightarrow\mathbb{N}\times\mathbb{N}$$: Cantor's pairing function $$\pi(i,j) = \frac{(i+j)(i+j+1)}{2} + j$$.
- $$\mathbb{N}\leftrightarrow\mathbb{Q}$$: diagonal listing of fractions $$p/q$$ skipping duplicates.

**Hilbert’s hotel.** A hotel with rooms numbered by $$\mathbb{N}$$, all full, can still accommodate one new guest ($$n\mapsto n+1$$) or countably many new guests ($$n\mapsto 2n$$, freeing all odd rooms). Even if *countably many* buses each carrying countably many guests pull up at once, prime powers solve it cleanly: move existing guest $$n$$ to room $$2^n$$, and send guest $$k$$ from bus $$b$$ to room $$p_{b+1}^k$$ (where $$p_2=3, p_3=5, p_4=7,\dots$$)! Unique prime factorization guarantees zero collisions, illustrating $$\aleph_0 \cdot \aleph_0 = \aleph_0$$.

### 1.3 Uncountable infinity

**Cantor’s diagonal argument.** Suppose $$f:\mathbb{N}\to\{0,1\}^{\mathbb{N}}$$ listed all infinite binary sequences. Build $$s$$ with $$s_n=1-f(n)_n$$. Then $$s$$ differs from every listed sequence at its own index. Hence $$\{0,1\}^{\mathbb{N}}$$ (and $$\mathbb{R}$$) is **uncountable**.

#### Explanation: Hand-Checking Cantor's Pairing Function and a $$5\times 5$$ Diagonal Table

Make Cantor's arguments completely tangible with two quick hand checks:

**Example 1 — Evaluating Cantor's pairing function $$\pi(i, j) = \frac{(i+j)(i+j+1)}{2} + j$$ on the $$3\times 3$$ grid:**
- Diagonal $$i+j=0$$: $$\pi(0,0) = 0$$.
- Diagonal $$i+j=1$$: $$\pi(1,0) = \frac{1\cdot 2}{2}+0 = 1$$; $$\pi(0,1) = \frac{1\cdot 2}{2}+1 = 2$$.
- Diagonal $$i+j=2$$: $$\pi(2,0) = 3$$; $$\pi(1,1) = 4$$; $$\pi(0,2) = 5$$.
- Diagonal $$i+j=3$$: $$\pi(2,1) = 7$$; $$\pi(1,2) = 8$$.
- Diagonal $$i+j=4$$: $$\pi(2,2) = \frac{4\cdot 5}{2}+2 = 12$$.

Every non-negative integer appears **exactly once**! You can even invert any output by hand: for $$\pi(i,j) = 10$$, the largest triangular number $$\le 10$$ is $$T_4 = \frac{4\cdot 5}{2} = 10$$, so $$i+j = 4$$ and $$j = 10 - 10 = 0 \implies (i,j) = (4,0)$$.

**Example 2 — Running diagonalization bit by bit on 5 binary sequences:**
Suppose someone claims to list every infinite binary sequence, starting with these five rows (diagonal bits in bold):
- $$f(1) = (\mathbf{0},\; 1,\; 1,\; 0,\; 1,\; \dots)$$
- $$f(2) = (1,\; \mathbf{1},\; 0,\; 1,\; 0,\; \dots)$$
- $$f(3) = (0,\; 0,\; \mathbf{0},\; 1,\; 1,\; \dots)$$
- $$f(4) = (1,\; 1,\; 1,\; \mathbf{1},\; 0,\; \dots)$$
- $$f(5) = (0,\; 1,\; 0,\; 0,\; \mathbf{0},\; \dots)$$

Read the diagonal $$(\mathbf{0}, \mathbf{1}, \mathbf{0}, \mathbf{1}, \mathbf{0}, \dots)$$ and **flip every bit** ($$0 \leftrightarrow 1$$):
$$
s = (\mathbf{1},\; \mathbf{0},\; \mathbf{1},\; \mathbf{0},\; \mathbf{1},\; \dots).
$$
Check directly: $$s$$ differs from $$f(1)$$ at bit 1 ($$1 \neq 0$$), from $$f(2)$$ at bit 2 ($$0 \neq 1$$), from $$f(3)$$ at bit 3, and in general $$s \neq f(n)$$ for **every** $$n \in \mathbb{N}$$! Working in $$\{0,1\}^{\mathbb{N}}$$ sidesteps the decimal dual-representation quibble $$0.1999\dots = 0.2000\dots$$ completely. (And for decimal reals, simply pick digit `4` when the diagonal digit is not `4`, and `5` when it is `4`—no trailing `0`s or `9`s can ever appear!)

So infinity has **scales**: $$\lvert\mathbb{N}\rvert=\aleph_0$$ and $$\lvert\mathbb{R}\rvert=2^{\aleph_0}=\mathfrak{c}$$. Cantor’s theorem $$\lvert X\rvert<\lvert\mathcal{P}(X)\rvert$$ generates an endless hierarchy of infinities.

### 1.4 Continuum Hypothesis (status awareness)

**CH:** no cardinal strictly between $$\aleph_0$$ and $$2^{\aleph_0}$$. Independent of standard ZFC set theory (Gödel, Cohen). For this studio, CH is a **status icon**: some precise infinity questions are independent, not merely unsolved.

### 1.5 Ordinals versus cardinals

Cardinals measure size. **Ordinals** measure order type: $$\omega$$ is the order type of $$\mathbb{N}$$; $$\omega+1$$ is a copy of $$\mathbb{N}$$ followed by an extra point at the end—**not** the same ordered set as $$\omega$$, even though both are countably infinite as bare sets. “Infinity plus one” is meaningful for ordinals and trivial for cardinals $$\aleph_0$$.

### 1.6 Infinity in analysis and geometry

- Series $$\sum 1/n^2 = \pi^2/6$$ converges: infinite sum of positive terms can be finite.  
- Harmonic series diverges: infinite sum can be infinite.  
- Improper integrals and measures assign $$\infty$$ as an extended value.  
- Projective geometry adds a line at infinity.  
- Fractal sets can have infinite length in finite area (Koch snowflake).

Each is a different formal device. Your log should name the device.

### 1.7 Infinity in this course’s other studios

- **Collatz:** infinite forward orbits; conjecture about all $$n\in\mathbb{N}$$.  
- **Primes:** infinitely many primes (Euclid); open infinitudes (twins).  
- **Kakeya:** infinitely many directions; limits of constructions as $$\delta\to 0$$.

Infinity is the silent stage of almost every exploration.

---

## 2. Conjecture versus proof versus experiment

| Label | Example |
|-------|---------|
| **Theorem** | Infinitely many primes; uncountability of $$\mathbb{R}$$; Hilbert hotel bijections |
| **Independent** | Continuum Hypothesis (relative to ZFC) |
| **Paradox (resolved)** | Galileo’s evens; hotel full yet free rooms |
| **Metaphor** | “Infinity is a journey” — potential-mode poetry, not a proof |

**Success criteria:**

1. Hilbert hotel rewrite in your own words with at least two guest-arrival scenarios.  
2. Explicit bijection $$\mathbb{N}\leftrightarrow\mathbb{Z}$$ written as a formula or clear listing rule.  
3. Diagonal argument written in full sentences with a concrete numerical toy (finite diagonal fails; explain why the infinite case works).  
4. One calculus example where infinity is potential ($$\varepsilon$$-$$N$$) and one where a completed infinite set is used.  
5. Paradox + resolution slogan for at least one classic paradox.

---

## 3. Research log standards

**Date · Intent · Action · Result · Label · Interpretation · Next step.**

When you “experiment,” you often mean **proof attempts** and **counterexample searches** (e.g., trying to list reals). Record failed listing attempts—they are pedagogically gold.

---

## 4. Experiments

Do at least **two** of A–E.

### Experiment A — Hotel script (20–40 min)

Write a short dialogue or comic script: full hotel, one guest, then a bus of $$\mathbb{N}$$ guests, then countably many buses. Each scene needs an explicit reassignment rule.

**Success criterion:** three scenes + formulas for room maps.

### Experiment B — Bijections workshop (30–50 min)

1. Formula for a bijection $$\mathbb{N}\to\mathbb{Z}$$.  
2. Diagram for $$\mathbb{N}\times\mathbb{N}\to\mathbb{N}$$.  
3. Optional: show $$(0,1)\sim\mathbb{R}$$ via tan or similar.

**Success criterion:** peer could check your rules without asking you.

### Experiment C — Diagonal on paper (25–40 min)

List five made-up binary sequences as if starting an enumeration; construct the diagonal antagonist. Then write why no *complete* list of all sequences can succeed. Address the dual-representation quibble for decimal expansions of reals (0.1999…=0.2000…).

**Success criterion:** full writeup with the quibble handled or sidestepped via $$\{0,1\}^{\mathbb{N}}$$.

### Experiment D — Calculus infinity hunt (20–35 min)

Pick two textbook theorems (e.g., intermediate value theorem; definition of series convergence). Mark every appeal to infinity as potential or actual. Rewrite one proof sentence to make the mode explicit.

**Success criterion:** annotated theorems + one rewrite.

### Experiment E — Course cross-links (20–30 min)

Choose Collatz, primes, or Kakeya. Write a half page: which infinite quantifiers appear (“for all $$n$$”, “there exist infinitely many”, “limit as $$\delta\to 0$$”)? Which are theorems vs conjectures?

**Success criterion:** quantifier inventory with labels.

---

## 5. Common confusions

1. **“Infinity is not a number, so math cannot talk about it.”** — Infinity is not a real number; it is many rigorous objects.  
2. **“$$\infty+1>\infty$$ always.”** — Cardinal $$\aleph_0+1=\aleph_0$$; ordinal $$\omega+1>\omega$$.  
3. **“Uncountable means cannot be described.”** — Individual reals can be definable; the *set* cannot be listed as a sequence.  
4. **“Diagonalization is a trick that fails for reals because of 0.999…=1.”** — Handle representations or use binary sequences.  
5. **“CH is unsolved like RH.”** — RH is a definite arithmetic statement (open); CH is independent of ZFC.

---

## 7. Checkpoint rubric

| Done? | Item |
|-------|------|
| ☐ | Hotel rewrite with maps |
| ☐ | Bijection $$\mathbb{N}\leftrightarrow\mathbb{Z}$$ |
| ☐ | Diagonal argument writeup |
| ☐ | Potential vs actual examples |
| ☐ | Paradox + resolution |
| ☐ | Cross-link to another chapter/studio |
| ☐ | Log ≥3 entries |

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/explore-describe-infinity/`.

**From the research pack (must-know slogans)**

- **Potential vs actual infinity:** process vs completed set.
- **Hilbert hotel:** countable infinity $$\aleph_0$$ rebookings; bijections $$\mathbb{N}\leftrightarrow\mathbb{Z}$$.
- **Cantor diagonal:** $$\lvert\mathbb{R}\rvert > \lvert\mathbb{N}\rvert$$; continuum size.
- **CH** independent of ZFC — not “open like RH.”
- Studio: write explicit bijections; separate paradox rhetoric from theorems.

**Recommended order**

1. **Orientation** — Numberphile — Infinity Paradoxes (Hilbert hotel): [https://www.youtube.com/watch?v=dDl7g_2x74Q](https://www.youtube.com/watch?v=dDl7g_2x74Q).  
2. **Foundation** — Wi-Phi / Rayo — Sizes of Infinity Part 1 (Hilbert): [https://www.youtube.com/watch?v=p1KkXA0vKsQ](https://www.youtube.com/watch?v=p1KkXA0vKsQ).  
3. **Intuition** — Numberphile — Infinite hotel keys problem: [https://www.youtube.com/watch?v=uezOrcmHzrQ](https://www.youtube.com/watch?v=uezOrcmHzrQ).  

**Official / primary written hubs**


Complete URL bibliography: `research/video-research/explore-describe-infinity/references.md`.

## 8. References and course links


### Video research pack (all URLs)

Complete list: `research/video-research/explore-describe-infinity/references.md`.

1. Numberphile — Infinity Paradoxes (Hilbert hotel) — https://www.youtube.com/watch?v=dDl7g_2x74Q  
2. Wi-Phi / Rayo — Sizes of Infinity Part 1 (Hilbert) — https://www.youtube.com/watch?v=p1KkXA0vKsQ  
3. Numberphile — Infinite hotel keys problem — https://www.youtube.com/watch?v=uezOrcmHzrQ  
4. Khan Academy — Wi-Phi Hilbert hotel — https://www.khanacademy.org/partner-content/wi-phi/wiphi-metaphysics-epistemology/wiphi-metaphysics/v/sizes-of-infinity-part-1-hilberts-hotel  
5. Wikipedia — Hilbert's paradox of the Grand Hotel — https://en.wikipedia.org/wiki/Hilbert%27s_paradox_of_the_Grand_Hotel  
6. Wikipedia — Cantor's diagonal argument — https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument  
7. Wikipedia — Continuum hypothesis — https://en.wikipedia.org/wiki/Continuum_hypothesis  
8. Wikipedia — Cardinality — https://en.wikipedia.org/wiki/Cardinality  
9. Stanford Encyclopedia — Continuum Hypothesis (survey) — https://plato.stanford.edu/entries/continuum-hypothesis/  
10. Research pack folder: `research/video-research/explore-describe-infinity/`.

1. Any rigorous intro analysis for limits; any set theory primer for cardinality.  
2. Hilbert’s hotel expositions (popular and textbook).  
3. Course studios on primes, Collatz, Kakeya for quantifiers over infinite domains.  
4. Optional: continuum hypothesis independence (historical survey level).

---

## Further directions

If diagonalization felt easy, try proving $$\lvert\mathbb{R}\rvert=\lvert\mathbb{R}\times\mathbb{R}\rvert$$. If philosophy appeals, write a careful comparison of potentialism vs classical set theory—without abandoning formal clarity. If computation appeals, discuss how infinite objects are represented finitely (generators, oracles, streams) in programming.

### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/explore-describe-infinity/transcripts/` · status: `research/video-research/explore-describe-infinity/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/explore-describe-infinity_dDl7g_2x74Q_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*


## Video tham khảo

- **xem trước** — [Infinity Paradoxes - Numberphile](https://www.youtube.com/watch?v=dDl7g_2x74Q) — Numberphile, English. Watch first. “Infinity Paradoxes - Numberphile” orients the lesson’s aim: Distinguish potential infinity (unending process) from actual infinity (a completed set such as \mathbb{N}).
- [PHILOSOPHY - Mathematics: Sizes of Infinity, Part 1 (Hilbert's Hotel) (HD)](https://www.youtube.com/watch?v=p1KkXA0vKsQ) — Wireless Philosophy, English. A second pass once the main claim is in view: Distinguish potential infinity (unending process) from actual infinity (a completed set such as \mathbb{N}).
- [A Problem with Infinite Hotel Keys - Numberphile](https://www.youtube.com/watch?v=uezOrcmHzrQ) — Numberphile, English. Further depth after the first two, still tied to this lesson: Distinguish potential infinity (unending process) from actual infinity (a completed set such as \mathbb{N}).
