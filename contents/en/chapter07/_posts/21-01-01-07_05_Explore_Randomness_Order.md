---
layout: post
title: "Can randomness create order?"
chapter: '07'
order: 5
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Course links**  
> [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) · [Prime predictability studio]({{ site.baseurl }}/contents/en/chapter07/07_04_Explore_Prime_Predictability/) · [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/)

Imagine tossing a fair coin for every integer from $$1$$ to $$1000$$ to decide whether to keep it or throw it away. Everyday intuition insists that randomness is the sworn enemy of order: how could coin flips ever draw a straight line or assemble a clean pattern? Yet in 1947, Paul Erdős stunned the mathematical world by using random coin-flip colorings to *prove* the existence of intricate graphs no human had been able to construct by hand for decades.

Modern mathematics pushes the paradox even further. Between rigid order and pure noise lies a fascinating middle country called **pseudorandomness**—completely deterministic objects (like the prime numbers) that pass battery after battery of statistical tests as if they had been rolled by dice. This studio invites you into a simulation lab to measure that boundary firsthand: when randomness erases structure, when density forces order to emerge, and why a slogan like *"randomness creates order"* only becomes real mathematics once you specify the scale and the test.

**Lesson roadmap:** Background Knowledge Map (Erdős's probabilistic method, additive combinatorics & structure vs. pseudorandomness) → When randomness destroys vs. proves existence → Deep-Dive Explanation (Read Slowly): hand-counting 3-APs in $$\{1..10\}$$, building an AP-free base-3 set, and proving $$R(4,4) > 6$$ by expectation → Roth, Szemerédi & Green–Tao → Studio experiments & log.

---

## Learning objectives

After this studio you should be able to:

- Give examples where randomness **destroys** structure and where probability **creates** proofs of structure (or of extremal objects).
- State Roth’s theorem slogan (dense sets contain 3-term APs) and contrast it with random sparse sets.
- Run a simulation: random subsets of $$\{1,\ldots,N\}$$ and counts of 3-term arithmetic progressions.
- Explain **pseudorandomness** as “indistinguishable from random by certain statistics,” with primes as a motivating story.
- Separate theorem, heuristic, and simulation artifact in a research log.
- Write a short essay connecting your experiment to Green–Tao’s philosophy without claiming you proved Green–Tao.

**Prerequisites.** Basic probability (expectation, independence at slogan level), modular arithmetic, and comfort with counting.

---

## Background Knowledge Map: What Are the Probabilistic Method and Additive Combinatorics?

Most undergraduates learn probability as a tool for noisy data and combinatorics as counting permutations. In modern research, fusing the two created three vibrant pillars behind this studio:

### 1. The Probabilistic Method (Erdős)

Pioneered by Paul Erdős in 1947, this is the art of *using probability to prove completely deterministic theorems*. Instead of laboriously building an object with property $$P$$, you define a random object and compute the expected number of "bad events" (violations of $$P$$). If $$\mathbb{E}[\text{bad events}] < 1$$, there *must* exist at least one outcome with **zero** bad events—even if you never exhibit it explicitly! Today this method underpins theoretical computer science, random graph theory, and algorithm design.

### 2. Additive Combinatorics

This field studies the tension between a set's *size (density)* and its *additive structure* (how large is $$A + A$$? Must $$A$$ contain an arithmetic progression $$a, a+d, a+2d$$?). The theorems of **Ramsey**, **Roth**, and **Szemerédi** all share one remarkable motto: *"Complete disorder is impossible."* Once a system is large enough or a subset is dense enough, pockets of clean order are forced to appear.

### 3. The Structure–Pseudorandomness Dichotomy

At the heart of the **Green–Tao theorem** lies a powerful lens: any complex set can be decomposed into a **structured** piece (nearly periodic, with large Fourier bias) and a **pseudorandom** piece (indistinguishable from random noise under statistical tests). Remarkably, *both* pieces force arithmetic progressions—the structured part by repetition, and the pseudorandom part by uniform density!

---

## 1. Background mathematics

### 1.1 What might “order” mean?

For this studio, treat **order** as the presence of recognizable patterns:

- arithmetic progressions (APs) $$a,a+d,a+2d$$;  
- monochromatic cliques in graph colorings;  
- geometric configurations (triangles, unit distances);  
- compressible descriptions (low Kolmogorov complexity)—mentioned only as a horizon.

**Randomness** will mean: sampling from a simple probability distribution (e.g., each integer included independently with probability $$p$$).

### 1.2 Randomness destroys some structures

Consider a random subset $$A\subset\{1,\ldots,N\}$$ where each $$n$$ is included independently with probability $$p$$. The expected number of 3-term APs in $$A$$ scales like $$p^3 N^2$$. If $$p$$ is tiny—say $$p=N^{-0.9}$$—the expectation is $$\Theta(N^{-0.7}) \ll 1$$, so with high probability $$A$$ is **AP-free**. Sparsity plus noise erase additive order.

Similarly, a random graph $$G(n,1/2)$$ almost surely has no independent set larger than about $$2\log_2 n$$, while almost surely containing every fixed small subgraph. Randomness is a sculptor: it carves away some patterns and forces others.

### 1.3 The probabilistic method creates existence

**Erdős’s probabilistic method:** to prove an object with property $$P$$ exists, define a random object and show $$\Pr[P]>0$$. The logic is ordinary finite probability theory: if every bad event is avoided on a set of positive probability, a good outcome sits in the sample space.

#### Deep-Dive Explanation (Read Slowly): Hand-Checking 3-APs, an AP-Free Base-3 Set, and Ramsey $$R(4,4) > 6$$

Work through two short hand calculations to see structure, randomness, and probabilistic existence collide in real numbers:

**Example 1 — Counting 3-APs in $$\{1, \dots, 10\}$$ vs. a structured base-3 set:**
- In $$\{1, 2, \dots, 10\}$$, list all 3-term APs $$(a, a+d, a+2d)$$ by step $$d$$:
  - $$d=1$$: $$(1,2,3), \dots, (8,9,10)$$ → **8** triples;
  - $$d=2$$: $$(1,3,5), \dots, (6,8,10)$$ → **6** triples;
  - $$d=3$$: $$(1,4,7), (2,5,8), (3,6,9), (4,7,10)$$ → **4** triples;
  - $$d=4$$: $$(1,5,9), (2,6,10)$$ → **2** triples.
  Total: $$8 + 6 + 4 + 2 = \mathbf{20}$$ triples (matching the exact formula $$\frac{N(N-2)}{4} = \frac{10\cdot 8}{4} = 20$$). A random subset keeping each element with probability $$p = 0.5$$ (average size 5) still expects $$20 \times (0.5)^3 = 2.5$$ three-term APs!
- Now pick a **structured** subset of size **6** (bigger than average!) in $$\{0, 1, \dots, 10\}$$ using only digits `0` and `1` in **base 3**:
  $$
  S = \{0_{(3)}, 1_{(3)}, 10_{(3)}, 11_{(3)}, 100_{(3)}, 101_{(3)}\} = \{0, 1, 3, 4, 9, 10\}.
  $$
  Check whether any distinct $$x < y < z$$ in $$S$$ can satisfy $$x + z = 2y$$! Since every base-3 digit of $$x, y, z$$ is `0` or `1`, adding $$x + z$$ produces **no carries** (digits lie in $$\{0, 1, 2\}$$), while $$2y$$ has digits only in $$\{0, 2\}$$. Matching digit by digit forces $$x$$ and $$z$$ to have identical digits everywhere, so $$x = y = z$$! Thus $$S$$ has **exactly 0 three-term APs**—at the same size, a random set is *richer* in arithmetic progressions than this carefully structured set!

**Example 2 — Proving $$R(4,4) > 6$$ without drawing a single edge:**
Color every edge of the complete graph $$K_n$$ independently Red or Blue with probability $$1/2$$. Any fixed subset of $$k$$ vertices spans $$\binom{k}{2}$$ edges, so the probability that all of them share one color is $$2 \cdot 2^{-\binom{k}{2}} = 2^{1 - \binom{k}{2}}$$. Letting $$X$$ be the number of monochromatic $$K_k$$ cliques, linearity of expectation gives:
$$
\mathbb{E}[X] = \binom{n}{k} 2^{1 - \binom{k}{2}}.
$$
Plug in $$k = 4$$ (so $$\binom{4}{2} = 6$$ edges per $$K_4$$) and $$n = 6$$:
$$
\mathbb{E}[X] = \binom{6}{4} \cdot 2^{1 - 6} = \frac{15}{32} < 1.
$$
Because $$X$$ is a non-negative integer whose average is strictly less than $$1$$, **there must exist a 2-coloring of $$K_6$$ with $$X = 0$$** (no monochromatic $$K_4$$), proving $$R(4,4) > 6$$ on the back of an envelope! (And for $$k=3, n=5$$, you can draw $$K_5$$ explicitly: color the outer pentagon Red and the inner five-pointed star Blue → **0 monochromatic triangles**, showing $$R(3,3) > 5$$.)

### 1.4 Structure theorems: when density forces order

**Roth’s theorem:** any subset of $$\{1,\ldots,N\}$$ with density at least $$\delta>0$$ (for $$N$$ large depending on $$\delta$$) contains a 3-term AP. Density, not randomness, forces additive order. **Szemerédi’s theorem** extends to $$k$$-term APs for any fixed $$k$$. Quantitatively, how small a density still forces a 3-AP is a living research area (Bloom–Sisask, Kelley–Meka 2023); your studio only needs the qualitative slogan and a feel for scales via simulation.

**Green–Tao** upgrades this philosophy to the primes: although primes have density zero, they are dense enough *inside a pseudorandom majorant* to inherit Szemerédi-type configurations via a **transference principle**.

**Counting 3-APs precisely.** The number of triples $$(a,d)$$ with $$d\ge 1$$ and $$a+2d\le N$$ equals

$$
\sum_{d=1}^{\lfloor(N-1)/2\rfloor}(N-2d)=\Theta(N^2),
$$

specifically $$\frac{N(N-2)}{4}$$ for even $$N$$ and $$\frac{(N-1)^2}{4}$$ for odd $$N$$ (giving $$2450$$ for $$N=100$$). Thus in the Bernoulli model the expected AP count is $$\Theta(p^3 N^2)$$, letting you predict right where expectation crosses $$1$$ as $$p$$ shrinks in Experiments A and B.

### 1.5 Pseudorandomness as a middle road

A sequence or set is **pseudorandom** (relative to a family of tests) if it passes those tests that a truly random object would pass with high probability—equidistribution in APs, correlation bounds, Fourier bias near zero, etc. The Liouville function $$\lambda(n)=(-1)^{\Omega(n)}$$ is conjectured to behave randomly in many averages (Chowla-type conjectures); partial results are major recent news. Primes fail naive i.i.d. models (every prime $$>2$$ is odd, and primes avoid $$0 \bmod q$$) yet satisfy sophisticated random-like statistics after accounting for those local obstructions.

**Moral for logs.** Always name the test. “Random” without a test is rhetoric.

### 1.6 Entropy, noise, and reconstruction (optional horizon)

In coding theory and statistics, randomness (noise) is what you fight, yet random codes achieve capacity. In unsupervised learning, stochastic gradient noise can help escape saddles. Mention these only if you want an applications paragraph; keep the mathematical core additive.

---

## 2. Conjecture versus proof versus experiment

| Label | Example |
|-------|---------|
| **Theorem** | Roth; Szemerédi; Green–Tao; existence via probabilistic method |
| **Conjecture** | Twin primes; Chowla; many Fourier bias conjectures |
| **Simulation** | “In 50 trials at $$N=200$$, $$p=0.2$$, mean AP count was …” |
| **Slogan** | “Randomness creates order” — must be unpacked each time |

**Success criteria:**

1. One documented simulation of random sets and 3-AP counts (parameters + results).  
2. One written example of randomness destroying structure, and one of probabilistic existence.  
3. A half-page Green–Tao moral in your words (structure vs pseudorandomness).  
4. Clear labels in the log; no “therefore Green–Tao is obvious from my plot.”  
5. One confusion you held at the start and revised.

---

## 3. Research log standards

**Date · Intent · Action · Parameters ($$N,p$$, trials) · Result · Label · Interpretation · Next step.**

Seeds for PRNGs belong in the log. If you change the definition of “3-AP” (e.g., distinct terms only, $$d>0$$), write it once and freeze it.

---

## 4. Experiments

Do at least **two** of A–E.

### Experiment A — Dense random sets and 3-APs (40–80 min)

For $$N\in\{50,100,200\}$$ and $$p\in\{0.1,0.3,0.5\}$$, sample a random set (Bernoulli), count 3-term APs, repeat $$T\ge 20$$ times, record mean and max. Implement AP counting carefully: loop over $$d\ge 1$$ and $$a$$ with $$a+2d\le N$$, check membership of all three terms. For speed at larger $$N$$, store the set in a hash set.

**Hypothesis:** “Mean AP count scales like $$p^3 N^2$$.” Check orders of magnitude, not just one cell of the table.

**Success criterion:** table + comparison to a back-of-envelope expectation + one plot of mean AP count vs $$p$$ at fixed $$N$$ if you can.

### Experiment B — Sparse regime (30–60 min)

Fix $$N=500$$. Decrease $$p$$ until the median AP count hits 0 in your trials. Relate to the heuristic threshold when expectation drops below 1.

**Success criterion:** approximate critical $$p$$ for your $$N$$ + honesty about finite-sample noise.

### Experiment C — Deterministic structured set (20–40 min)

Take an AP-free construction you can define (e.g., a geometric progression set, or integers with only digits 0 and 1 in base 3—Behrend/Salem–Spencer are advanced; a simple large AP-free set for small $$N$$ is fine). Compare AP counts to a random set of the same size.

**Success criterion:** same cardinality, different structure, different AP counts—quantified.

### Experiment D — Probabilistic method vignette (25–40 min)

Reproduce a textbook probabilistic lower bound for a Ramsey number or for the existence of a tournament without transitive triples, *at a tiny scale* where you can also brute-force check. Write both the expectation argument and the brute-force note.

**Success criterion:** proof sketch of existence + computational sanity check for small $$n$$.

### Experiment E — Pseudorandomness literacy (20–30 min)

Read the Green–Tao Ch.2 section on structure vs randomness (or an expository paragraph you cite). Rewrite the dichotomy in ≤8 sentences. List two tests a set might pass to be called pseudorandom.

**Success criterion:** rewrite without copying; two named tests.

---

## 5. Common confusions

1. **“Random sets never have patterns.”** — Dense random sets have many APs with high probability.  
2. **“Probabilistic proofs are incomplete.”** — Existence via positive probability is rigorous; it may not give algorithms.  
3. **“Green–Tao says primes are random.”** — It exploits pseudorandom majorants and structure theory; primes are not i.i.d. bits.  
4. **“Szemerédi needs randomness.”** — It needs density; proofs may use ergodic or Fourier tools.  
5. **“My simulation proves a theorem.”** — Simulations generate conjectures and illustrations.

---

## 7. Checkpoint rubric

| Done? | Item |
|-------|------|
| ☐ | Simulation table with parameters |
| ☐ | Destroy vs create examples (two short writeups) |
| ☐ | Green–Tao moral paragraph |
| ☐ | Log ≥3 labeled entries |
| ☐ | Revised confusion note |
| ☐ | Open question |

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/explore-randomness-order/`.

**From the research pack (must-know slogans)**

- **Pseudorandomness:** deterministic sets can statistically mimic random ones (and vice versa for structure).
- **Roth / Szemerédi:** dense sets contain arithmetic progressions; Green–Tao upgrades to primes.
- **Probabilistic method (Erdős):** existence via expectation without constructing.
- Randomness can **destroy** structure (sparse random sets) or **create** typicality (random graphs).
- Studio: simulate vs prove; label theorem / heuristic / simulation.

**Recommended order**

1. **Orientation** — Quanta — P vs NP (structure vs search; complexity culture): [https://www.youtube.com/watch?v=pQsdygaYcE4](https://www.youtube.com/watch?v=pQsdygaYcE4).  

**Official / primary written hubs**

- Green–Tao (structure in primes): https://arxiv.org/abs/math/0404188  
- Tao blog / notes on Szemerédi (expository entry): https://terrytao.wordpress.com/tag/szemeredi-theorem/  

Complete URL bibliography: `research/video-research/explore-randomness-order/references.md`.

## 8. References and course links


### Video research pack (all URLs)

Complete list: `research/video-research/explore-randomness-order/references.md`.

1. Quanta — P vs NP (structure vs search; complexity culture) — https://www.youtube.com/watch?v=pQsdygaYcE4  
2. Green–Tao (structure in primes) — https://arxiv.org/abs/math/0404188  
3. Tao blog / notes on Szemerédi (expository entry) — https://terrytao.wordpress.com/tag/szemeredi-theorem/  
4. Wikipedia — Probabilistic method — https://en.wikipedia.org/wiki/Probabilistic_method  
5. Wikipedia — Szemerédi's theorem — https://en.wikipedia.org/wiki/Szemer%C3%A9di%27s_theorem  
6. Wikipedia — Roth's theorem — https://en.wikipedia.org/wiki/Roth%27s_theorem  
7. Wikipedia — Pseudorandomness — https://en.wikipedia.org/wiki/Pseudorandomness  
8. Alon–Spencer book info (probabilistic method) — https://en.wikipedia.org/wiki/The_Probabilistic_Method  
9. Quanta — patterns in primes / structure — https://www.quantamagazine.org/tag/number-theory/  
10. Research pack folder: `research/video-research/explore-randomness-order/`.

1. Course: Green–Tao lecture; prime predictability studio; chaos lecture for dynamical “order from iteration.”  
2. Alon–Spencer, *The Probabilistic Method* (philosophy and classics).  
3. Expository accounts of Roth/Szemerédi (Tao blog posts are popular entry points if available).  
4. Nearby: [Iteration / Collatz]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/) for deterministic rules that look random.

---

## Further directions

If simulations hook you, implement a Fourier bias measure for indicator functions of subsets of $$\mathbb{Z}/N\mathbb{Z}$$ and compare structured vs random sets: structured sets (long APs, Bohr sets) show large bias at some frequency; random sets show small bias with high probability. If philosophy hooks you, write a longer essay on “order” definitions across combinatorics and dynamical systems—linking the chaos lecture’s sensitive dependence to the sense in which a deterministic Collatz orbit can still *look* statistically irregular. If you enjoyed Experiment D, push Ramsey lower bounds a few steps larger and record how expectation arguments outrun brute force.

**One-page synthesis prompt (recommended for the report).** Answer in connected prose: (i) when does randomness destroy additive structure in your data; (ii) when does density force structure in theorems you cite; (iii) how does pseudorandomness sit between those poles; (iv) what your simulation *cannot* say about primes.

### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/explore-randomness-order/transcripts/` · status: `research/video-research/explore-randomness-order/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/explore-randomness-order_pQsdygaYcE4_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*


## Video tham khảo

- **xem trước** — [Terence Tao: Structure and Randomness in the Prime Numbers, UCLA](https://www.youtube.com/watch?v=PtsrAw1LR3E) — UCLA, English. Watch first. “Terence Tao: Structure and Randomness in the Prime Numbers, UCLA” orients the lesson’s aim: Give examples where randomness destroys structure and where probability creates proofs of structure (or of extremal objects).
- [Chaos: The Science of the Butterfly Effect](https://www.youtube.com/watch?v=fDek6cYijxI) — Veritasium, English. A second pass once the main claim is in view: Give examples where randomness destroys structure and where probability creates proofs of structure (or of extremal objects).
