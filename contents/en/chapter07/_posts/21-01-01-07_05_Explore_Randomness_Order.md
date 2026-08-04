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

Randomness seems like the enemy of structure: coin flips do not draw straight lines. Yet twentieth-century mathematics learned a double lesson. First, **typical** random objects avoid certain patterns. Second, the **probabilistic method** *proves* existence of highly structured—or highly extreme—objects by showing that a random construction succeeds with positive probability. Elsewhere, **pseudorandomness** means “looks random to a class of tests” while hiding deep structure (the primes being the celebrity example).

This studio is philosophical and experimental. You will run small simulations, write careful definitions, and connect slogans to Green–Tao’s moral: structure and randomness are not opposites; they are tools that trade places depending on scale and test.

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

## 1. Background mathematics

### 1.1 What might “order” mean?

For this studio, treat **order** as the presence of recognizable patterns:

- arithmetic progressions (APs) $$a,a+d,a+2d$$;  
- monochromatic cliques in graph colorings;  
- geometric configurations (triangles, unit distances);  
- compressible descriptions (low Kolmogorov complexity)—mentioned only as a horizon.

**Randomness** will mean: sampling from a simple probability distribution (e.g., each integer included independently with probability $$p$$).

### 1.2 Randomness destroys some structures

Consider a random subset $$A\subset\{1,\ldots,N\}$$ where each $$n$$ is included independently with probability $$p$$. The expected number of 3-term APs in $$A$$ can be estimated by counting candidate triples $$(a,d)$$ with $$a, a+d, a+2d\le N$$ and multiplying by $$p^3$$. If $$p$$ is tiny—say $$p=N^{-0.9}$$—the expectation may be $$\ll 1$$, so with high probability $$A$$ is **AP-free** (or almost so). Sparsity plus noise erase additive order.

Similarly, a random graph $$G(n,1/2)$$ almost surely has no huge independent set of a forbidden size in certain regimes, while also almost surely containing small subgraphs. Randomness is a sculptor: it carves away some patterns and forces others.

### 1.3 The probabilistic method creates existence

**Erdős’s probabilistic method:** to prove an object with property $$P$$ exists, define a random object and show $$\Pr[P]>0$$. You may never exhibit the object explicitly. The logic is ordinary measure theory on a finite probability space: if every bad event is avoided on a set of positive probability, a good outcome sits in the sample space.

Classic cartoon: there exist graphs with arbitrarily large girth and chromatic number—proved by random methods long before constructive approaches matured. Another cartoon: lower bounds on Ramsey numbers via random 2-colorings of edges: if the expected number of monochromatic cliques is less than 1, some coloring has none. A third cartoon, closer to number theory, is the existence of large sum-free subsets of $$\{1,\ldots,N\}$$ (take the odds, or use random methods for variants).

Here randomness is not chaos for its own sake; it is a **proof technology**. Your Experiment D is meant to make the technology tactile: compute an expectation by hand, conclude existence, then—for tiny $$n$$—search exhaustively to see the object.

### 1.4 Structure theorems: when density forces order

**Roth’s theorem:** any subset of $$\{1,\ldots,N\}$$ with density at least $$\delta>0$$ (for $$N$$ large depending on $$\delta$$) contains a 3-term AP. Density, not randomness, forces additive order. **Szemerédi’s theorem** extends to $$k$$-term APs for any fixed $$k$$. Quantitatively, how small a density still forces a 3-AP is a living research area (Bloom–Sisask and others have pushed bounds); your studio only needs the qualitative slogan and a feel for scales via simulation.

**Green–Tao** upgrades this philosophy to the primes: although primes have density zero, they are dense enough *inside a pseudorandom majorant* to inherit Szemerédi-type configurations. The deep idea is a structure-versus-pseudorandomness dichotomy: a set is somewhat periodic (structured) or looks random to certain Gowers norms (pseudorandom), and both cases yield APs by different mechanisms.

A useful mental picture is a **transference principle**: if a sparse set looks like a dense set *relative to a carefully chosen weight*, then configurations known in the dense world transfer to the sparse world. Green–Tao’s majorant plays that role for primes. You will not construct a majorant here. You will **simulate the dense and sparse stories** and write the dichotomy in your own words, so that when Ch.2 mentions “pseudorandom,” the word has experimental texture.

**Counting 3-APs precisely.** The number of triples $$(a,d)$$ with $$d\ge 1$$ and $$a+2d\le N$$ equals

$$
\sum_{d=1}^{\lfloor(N-1)/2\rfloor}(N-2d)=\Theta(N^2).
$$

Thus in the Bernoulli model the expected AP count is $$\Theta(p^3 N^2)$$. That single asymptotic is enough to design Experiment A/B intelligently: you know when expectation crosses 1 as $$p$$ shrinks.

### 1.5 Pseudorandomness as a middle road

A sequence or set is **pseudorandom** (relative to a family of tests) if it passes those tests that a truly random object would pass with high probability—equidistribution in APs, correlation bounds, Fourier bias near zero, etc. The Liouville function $$\lambda(n)=(-1)^{\Omega(n)}$$ is conjectured to behave randomly in many averages (Chowla-type conjectures); partial results are major recent news. Primes fail some naive random models (they are all >2 odd, they avoid residue 0 mod $$q$$) yet satisfy sophisticated random-like statistics after accounting for local obstructions.

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

## 6. Exercises

1. Count the number of triples $$(a,d)$$ with $$d>0$$ and $$a+2d\le N$$. Exact formula?  
2. If each point is kept with probability $$p$$ independently, what is the expected number of 3-APs?  
3. Explain why a positive-density subset of integers cannot look like an extremely sparse random set.  
4. Give a one-paragraph example of the probabilistic method from graphs or number theory.  
5. Proposal (≤200 words): which experiment, parameters, success criteria, risks (definition drift, seed bias).

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

