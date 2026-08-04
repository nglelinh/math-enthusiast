---
layout: post
title: "How predictable are prime numbers?"
chapter: '07'
order: 4
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Course links**  
> [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) · [Twin primes]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/) · [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) · [Maynard]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/)

Primes look like coin flips scattered among the integers—until they do not. The **Prime Number Theorem** predicts global density; the **Riemann Hypothesis** would refine error terms; **twin primes** and **bounded gaps** probe local clustering; **Green–Tao** finds arithmetic progressions of arbitrary length. This studio trains you to **separate phenomena**, **run small experiments**, and never confuse a striking plot with a theorem.

You will not prove RH or the twin prime conjecture. You will build a personal map of what is known, what is open, and what your computer can honestly claim.

---

## Learning objectives

After this studio you should be able to:

- State the Prime Number Theorem at slogan level: $$\pi(x)\sim x/\log x$$, and compute $$\pi(x)$$ for moderate $$x$$.
- Plot or tabulate prime gaps $$g_n=p_{n+1}-p_n$$ and describe their qualitative behavior (typical size vs rare large gaps).
- Separate, in a written table: PNT, RH, twin primes, bounded gaps (Zhang/Maynard), Green–Tao APs.
- Design experiments with explicit ranges and success criteria; label results as observation, not proof.
- Explain why verification up to a large $$X$$ is evidence for a range, not a proof for all integers.
- Form at least one **falsifiable** numerical conjecture and attempt to kill it.

**Prerequisites.** Divisibility, sieves at a cartoon level, logarithms, and willingness to write a short program (or use a CAS).

---

## 1. Background mathematics

### 1.1 Counting primes

Let $$p_n$$ be the $$n$$th prime and $$\pi(x)=\#\{p\le x: p\text{ prime}\}$$. The **Prime Number Theorem (PNT)** asserts

$$
\pi(x)\sim\frac{x}{\log x}\qquad(x\to\infty),
$$

or equivalently $$p_n\sim n\log n$$. A more refined classical approximation is the logarithmic integral $$\operatorname{li}(x)$$. Empirically, $$\pi(x)$$ tracks these approximations closely for accessible $$x$$—but “closely” is a quantitative statement about error terms, and that is where RH lives.

### 1.2 Gaps and twins

The **gap** after $$p_n$$ is $$g_n=p_{n+1}-p_n$$. Heuristically, gaps are typically on the order of $$\log p_n$$, yet larger gaps occur; one can force arbitrarily large gaps by factorial constructions:

$$
(n+1)!+2,\;(n+1)!+3,\;\ldots,\;(n+1)!+(n+1)
$$

are $$n$$ consecutive composites. So “gaps stay bounded” is false, while “gaps are *usually* about $$\log p$$” can still be true in an average sense.

**Twin primes** are pairs $$(p,p+2)$$ both prime. The twin prime conjecture asserts infinitely many. The **Hardy–Littlewood** heuristic predicts

$$
\#\{p\le X: p+2\text{ prime}\}\sim 2C_2\int_2^X\frac{dt}{(\log t)^2}
$$

for a product constant $$C_2>0$$ (the twin prime constant). Numerics often match the shape of this prediction long before a proof exists.

### 1.3 Bounded gaps and Maynard

**Zhang (2013)** proved that $$\liminf (p_{n+1}-p_n)<\infty$$—in fact an explicit (large) bound—using GPY methods and Bombieri–Vinogradov-type ingredients. **Maynard** and Tao (independently, related work) simplified and strengthened the multidimensional sieve approach; the best unconditional numerical bounds on the liminf have been driven down dramatically by Polymath and subsequent work. Bounded gaps say something precise about *occasional* clustering; they do not by themselves yield twins (gap 2).

### 1.4 Arithmetic progressions: Green–Tao

**Green–Tao theorem:** the primes contain arithmetic progressions of arbitrary finite length. That is, for every $$k$$ there exist $$a,d$$ with

$$
a,\;a+d,\;\ldots,\;a+(k-1)d
$$

all prime. The proof is a landmark of additive combinatorics and ergodic/structure theory, not elementary sieve play. Finding an explicit AP of length 4 or 5 by hand or machine is a good *exploration*; proving all lengths exist is not your studio task.

### 1.5 Riemann Hypothesis as an error-term statement

RH is often packaged as zeros of $$\zeta(s)$$, but for this studio keep the **prime-counting error** slogan:

$$
\pi(x)=\operatorname{li}(x)+O\bigl(x^{1/2}\log x\bigr)
$$

(under RH, in standard forms). Without RH, weaker error terms are known. Connecting zero-free regions to primes is deep analytic number theory—Ch.1’s RH lesson is the companion deep read.

### 1.6 Predictability is layered

Think in layers:

| Layer | Question | Status flavor |
|-------|----------|---------------|
| Density | How many primes up to $$x$$? | PNT proved |
| Error | How good is the approximation? | RH open; partial bounds |
| Local pairs | Infinitely many twins? | Open; heuristics + massive data |
| Occasional close pairs | Bounded gaps infinitely often? | Proved (Zhang/Maynard line) |
| Patterns | APs of length $$k$$? | Green–Tao: all $$k$$ |
| Extremal gaps | Largest gaps near $$x$$? | Bounds; finer laws open |

“Predictable” is not a yes/no. Your studio product is a **map**, not a slogan.

---

## 2. Conjecture versus proof versus experiment

| Label | Example |
|-------|---------|
| **Theorem** | PNT; Green–Tao; liminf gaps finite |
| **Conjecture** | Twin primes; RH; many Hardy–Littlewood tuples |
| **Observation** | “In my range $$X=10^6$$, twin count was …” |
| **Heuristic** | Cramér model; Hardy–Littlewood integrals |

**Never write:** “I checked to $$10^8$$, so twin primes are infinite.”  
**Do write:** “I checked to $$10^8$$; the twin count tracks the Hardy–Littlewood integral within __%.”

**Success criteria:**

1. Gap plot or table for the first ≥200 primes (more if you can).  
2. At least one explicit AP of primes of length ≥4, with common difference shown.  
3. A phenomenon/status/tool table with ≥5 rows.  
4. One falsifiable numerical hypothesis tested and marked alive/dead.  
5. A short paragraph on verification vs proof (echo RH lesson).

---

## 3. Research log standards

**Date · Intent · Action · Result · Label · Interpretation · Next step.**

Record software (SymPy, Sage, custom sieve), primality method, and exact ranges. If you use probabilistic Miller–Rabin for huge $$n$$, say so—deterministic checks for your range are preferred.

---

## 4. Experiments

Do at least **two** of A–F.

### Experiment A — Gap plot (30–60 min)

Generate the first $$N$$ primes (start $$N=200$$, then $$10^4$$ if possible). Plot $$g_n$$ vs $$p_n$$ or vs $$n$$. Mark the running maximum gap.

**Hypothesis before plotting:** “Gaps increase smoothly like $$\log p$$.”  
After: describe spikes and typical size.

**Success criterion:** figure + 5-sentence caption separating average behavior from extremes.

### Experiment B — Twin counts vs heuristic (45–90 min)

For $$X=10^3,10^4,10^5$$ (go higher if feasible), count twins $$p\le X$$ with $$p+2$$ prime. Compare to

$$
2C_2\int_2^X\frac{dt}{(\log t)^2}
$$

with $$C_2\approx 0.66016$$. Numerical integration can be crude (rectangle rule) if documented.

**Success criterion:** table of actual vs predicted; percent error; statement of *not* proving infinitude.

### Experiment C — Find arithmetic progressions (30–60 min)

Search for prime APs of length 4 and 5 with small difference $$d$$. Record examples. Optional: time how hard length 6 becomes in a naive search.

**Success criterion:** at least one length-4 AP written as $$a+kd$$; note on search limits.

### Experiment D — Phenomenon map (20–30 min)

Fill a table:

| Phenomenon | Known? | Tool family | Studio experiment? |
|------------|--------|-------------|---------------------|
| PNT | | | |
| RH | | | |
| Twins infinite | | | |
| Bounded gaps | | | |
| Green–Tao | | | |
| Large gaps | | | |

**Success criterion:** no row confuses “proved” with “verified numerically.”

### Experiment E — Residue bias (stretch)

Among primes up to $$X$$, compare counts in residue classes mod 3, mod 4, or mod 10 (last digits 1,3,7,9). Discuss Chebyshev-type biases if you read about them—carefully separate theorem from observation.

**Success criterion:** counts table + caution about small-$$X$$ illusions.

### Experiment F — Literacy on records

Look up (reliable source) how far twin primes or prime gaps have been tabulated. Cite the source. Write three sentences on data vs proof.

**Success criterion:** citation + reflection.

---

## 5. Common confusions

1. **“Primes are random, so no theorems.”** — Random models are heuristics; PNT and Green–Tao are theorems.  
2. **“Bounded gaps imply twin primes.”** — Gap ≤246 (or whatever current bound you cite) is not gap =2.  
3. **“Green–Tao says primes are periodic.”** — It says APs of arbitrary finite length exist; density zero sets can still have rich additive structure.  
4. **“RH is about the density of primes only.”** — PNT is density; RH refines errors / zeros.  
5. **“A long AP of primes contradicts ‘randomness’.”** — Structure and pseudorandomness coexist; see the randomness studio.

---

## 6. Exercises

1. Prove that there are arbitrarily large gaps (factorial construction).  
2. Show that except for $$(3,5,7)$$ there is no prime triple $$(p,p+2,p+4)$$. Why does mod 3 kill it?  
3. Compute $$\pi(100)$$ and $$\pi(1000)$$ by hand or code; compare to $$x/\log x$$.  
4. Find an AP of length 4; verify each term prime.  
5. Write a 150-word proposal: which layer of predictability will you study, with what range and success criteria?

---

## 7. Checkpoint rubric

| Done? | Item |
|-------|------|
| ☐ | Gap plot/table (≥200 primes) |
| ☐ | Phenomenon status table |
| ☐ | AP example length ≥4 |
| ☐ | Verification vs proof paragraph |
| ☐ | Log ≥3 entries with labels |
| ☐ | One killed or surviving numerical conjecture |

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/explore-prime-predictability/`.

**From the research pack (must-know slogans)**

- **PNT:** π(x) ~ x/log x — density law, not a “formula for the n-th prime.”
- **RH** refines error terms via zeros of ζ; open (as of 2026).
- **Twin primes / bounded gaps:** Zhang, Maynard, Polymath — finite gaps infinitely often; twin prime conjecture still open.
- **Green–Tao:** primes contain arbitrarily long arithmetic progressions.
- Studio: plot gaps and π(x); never confuse verification with proof.

**Recommended order**

1. **Orientation** — Quanta — Riemann Hypothesis Explained: [https://www.youtube.com/watch?v=zlm1aajH6gY](https://www.youtube.com/watch?v=zlm1aajH6gY).  
2. **Intuition** — Numberphile — Twin primes / prime gaps (search Numberphile primes): [https://www.youtube.com/watch?v=QKHKD8bRAro](https://www.youtube.com/watch?v=QKHKD8bRAro).  
3. **Core** — Numberphile — Twin Prime Conjecture (Maynard): [https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem](https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem).  

**Official / primary written hubs**

- Green–Tao arXiv classic: https://arxiv.org/abs/math/0404188  
- Maynard small gaps between primes: https://arxiv.org/abs/1311.4600  

Complete URL bibliography: `research/video-research/explore-prime-predictability/references.md`.

## 8. References and course links


### Video research pack (all URLs)

Complete list: `research/video-research/explore-prime-predictability/references.md`.

1. Quanta — Riemann Hypothesis Explained — https://www.youtube.com/watch?v=zlm1aajH6gY  
2. Numberphile — Twin primes / prime gaps (search Numberphile primes) — https://www.youtube.com/watch?v=QKHKD8bRAro  
3. Numberphile — Twin Prime Conjecture (Maynard) — https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem  
4. Green–Tao arXiv classic — https://arxiv.org/abs/math/0404188  
5. Maynard small gaps between primes — https://arxiv.org/abs/1311.4600  
6. Quanta RH article hub — https://www.quantamagazine.org/tag/riemann-hypothesis/  
7. Wikipedia — Prime number theorem — https://en.wikipedia.org/wiki/Prime_number_theorem  
8. Wikipedia — Twin prime — https://en.wikipedia.org/wiki/Twin_prime  
9. Wikipedia — Green–Tao theorem — https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem  
10. Clay Math — Riemann Hypothesis — https://www.claymath.org/millennium/riemann-hypothesis/  
11. Research pack folder: `research/video-research/explore-prime-predictability/`.

1. Course: RH, twin primes, Green–Tao, Maynard lectures linked above.  
2. Hardy–Littlewood circle method heuristics (survey level).  
3. Soundararajan / Granville expository pieces on primes and gaps (any edition you can access).  
4. Nearby studio: [Randomness and order]({{ site.baseurl }}/contents/en/chapter07/07_05_Explore_Randomness_Order/).

---

## Further directions

If you care about zeros more than gaps, pivot experiments to partial sums of the Möbius function or comparisons of $$\pi(x)$$ and $$\operatorname{li}(x)$$ (with careful trust of libraries). If you care about additive structure, deepen Green–Tao literacy and try small AP searches with modular constraints.

### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/explore-prime-predictability/transcripts/` · status: `research/video-research/explore-prime-predictability/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/explore-prime-predictability_zlm1aajH6gY_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

