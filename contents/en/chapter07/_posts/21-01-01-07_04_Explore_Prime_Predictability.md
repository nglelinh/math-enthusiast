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

Walk along the positive integers and strike a bell every time you land on a prime—$$2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37\dots$$ Up close, the rhythm feels utterly capricious: two chimes ring almost on top of each other ($$101$$ and $$103$$), and then silence stretches across dozens—or eventually millions—of consecutive composites. Zoom in, and the primes look like coin flips.

Now step far back. Suddenly the noise dissolves into an astonishingly smooth curve. The **Prime Number Theorem** nails their global density; the **Riemann Hypothesis** aims at the sharpest possible error term; **bounded gaps** (Zhang, Maynard) guarantee infinitely many close encounters; and **Green–Tao** uncovers evenly spaced arithmetic progressions of any finite length hiding inside them. So *"Are primes predictable?"* has no simple yes-or-no answer. This studio trains you to **separate phenomena into layers**, **run controlled experiments**, and never mistake a gorgeous plot up to $$10^8$$ for a proof valid to infinity.

**Lesson roadmap:** Background Knowledge Map (analytic number theory, sieve methods & additive combinatorics) → Counting primes, gaps, twins & Green–Tao → Deep-Dive Explanation (Read Slowly): hand-checking all primes $$\le 100$$ and proving why a 6-prime AP must have step divisible by 30 → Layered status table → Studio experiments & log.

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

## Background Knowledge Map: What Is Analytic Number Theory and What Does It Study?

Prime numbers belong to discrete arithmetic, so university graduates are often surprised that the deepest breakthroughs about primes use integrals, complex variables, and waves. That bridge is **Analytic Number Theory**, built on three main pillars:

### 1. From Discrete Primes to Complex Functions via the Zeta Function

Leonhard Euler discovered the identity binding all integers to all primes:
$$
\zeta(s) = \sum_{n=1}^{\infty} n^{-s} = \prod_{p\text{ prime}} (1 - p^{-s})^{-1} \qquad (\operatorname{Re}(s) > 1).
$$
Bernhard Riemann extended $$\zeta(s)$$ to the complex plane and showed that the oscillations of the prime-counting function $$\pi(x)$$ are encoded by the nontrivial zeros of $$\zeta(s)$$—just as a musical waveform is assembled from harmonic frequencies.

### 2. Sieve Theory

Descending from the ancient Sieve of Eratosthenes (crossing off multiples of 2, 3, 5…), modern sieves (Selberg's sieve, the GPY sieve, and the multidimensional sieve of James Maynard and Terence Tao) estimate how many integers survive after filtering out small prime factors. That machinery proved there are infinitely many pairs of primes separated by at most **246**.

### 3. Additive Combinatorics and Probabilistic Models (Cramér's Model)

To predict additive patterns like twin primes $$(p, p+2)$$ or long arithmetic progressions, number theorists use **Cramér's heuristic**—imagining each integer $$n$$ flips a biased coin with probability $$1/\log n$$ to be "prime"—to guess asymptotic formulas, and then deploy Fourier analysis and structure theory (Green–Tao) to prove genuine theorems.

---

## 1. Background mathematics

### 1.1 Counting primes

Let $$p_n$$ be the $$n$$th prime and $$\pi(x)=\#\{p\le x: p\text{ prime}\}$$. The **Prime Number Theorem (PNT)** asserts

$$
\pi(x)\sim\frac{x}{\log x}\qquad(x\to\infty),
$$

or equivalently $$p_n\sim n\log n$$. A sharper classical approximation is the logarithmic integral $$\operatorname{li}(x) = \int_2^x \frac{dt}{\log t}$$. For instance, up to $$x = 10^6$$, there are exactly $$\pi(10^6) = 78\,498$$ primes: $$10^6/\log(10^6) \approx 72\,382$$, while $$\operatorname{li}(10^6) \approx 78\,627.5$$—off by only **130 primes** out of a million!

### 1.2 Gaps and twins

The **gap** after $$p_n$$ is $$g_n=p_{n+1}-p_n$$. Heuristically, gaps are typically on the order of $$\log p_n$$, yet arbitrarily large gaps occur via factorials:

$$
(n+1)!+2,\;(n+1)!+3,\;\ldots,\;(n+1)!+(n+1)
$$

are $$n$$ consecutive composites (for $$n=4$$, $$122, 123, 124, 125$$ are divisible by $$2, 3, 4, 5$$—though in fact four consecutive composites already appear right after $$23$$!).

**Twin primes** are pairs $$(p,p+2)$$ both prime. The twin prime conjecture asserts infinitely many. The **Hardy–Littlewood** heuristic predicts

$$
\#\{p\le X: p+2\text{ prime}\}\sim 2C_2\int_2^X\frac{dt}{(\log t)^2}
$$

with twin prime constant $$C_2 \approx 0.66016$$.

#### Deep-Dive Explanation (Read Slowly): Hand-Checking Primes $$\le 100$$ and Proving the "Multiple of 30" Rule

Before running code up to $$10^6$$, spend two minutes with pencil and paper on $$[1, 100]$$ to see both randomness and rigid arithmetic rules side by side:

1. **Direct tally up to $$x = 100$$:** There are exactly **25** primes:
   $$
   2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
   $$
   - **Gaps $$g_n$$:** The unique gap of $$1$$ is $$3 - 2$$; gap $$2$$ appears **8 times**, giving the 8 twin pairs $$(3,5), (5,7), (11,13), (17,19), (29,31), (41,43), (59,61), (71,73)$$. The largest gap below 100 is $$8$$ (between $$89$$ and $$97$$), nearly twice the typical scale $$\log(100) \approx 4.6$$.
   - **Comparing with Hardy–Littlewood:** At $$X = 100$$, the integral gives $$\approx 13.5$$ (small-$$X$$ noise is large); by $$X = 10^5$$, there are 1,224 twin pairs versus the prediction $$\approx 1{,}249$$—within $$2\%$$!

2. **Hand proof that any 6-term prime AP starting above 5 has common difference $$d$$ divisible by 30:**
   Suppose $$a, a+d, a+2d, a+3d, a+4d, a+5d$$ are all prime with $$a > 5$$.
   - *Divisible by 2:* If $$d$$ were odd, one of $$a, a+d$$ would be an even number $$> 2$$ (composite) → contradiction. Hence $$2 \mid d$$.
   - *Divisible by 3:* If $$3 \nmid d$$, then $$a, a+d, a+2d$$ hit all three residues $$0, 1, 2 \pmod 3$$, forcing a multiple of 3 larger than 3 → contradiction. Hence $$3 \mid d$$.
   - *Divisible by 5:* Likewise, if $$5 \nmid d$$, the first five terms hit all five residues $$0, 1, 2, 3, 4 \pmod 5$$, forcing a multiple of 5 larger than 5 → contradiction. Hence $$5 \mid d$$.
   - Conclusion: $$d$$ **must be a multiple of $$2 \times 3 \times 5 = 30$$**! Check the smallest 6-prime AP: $$7, 37, 67, 97, 127, 157$$—common difference literally $$d = 30$$!

### 1.3 Bounded gaps and Maynard

**Zhang (2013)** proved that $$\liminf (p_{n+1}-p_n)<\infty$$—initially with bound $$70{,}000{,}000$$—using GPY methods and Bombieri–Vinogradov-type ingredients. **Maynard** and Tao (independently) simplified and strengthened the multidimensional sieve approach; Polymath8 and subsequent work drove the unconditional bound down to **246**. Bounded gaps guarantee *occasional* close pairs; they do not by themselves settle twin primes (gap 2).

### 1.4 Arithmetic progressions: Green–Tao

**Green–Tao theorem:** the primes contain arithmetic progressions of arbitrary finite length. That is, for every $$k$$ there exist $$a,d$$ with

$$
a,\;a+d,\;\ldots,\;a+(k-1)d
$$

all prime (e.g., $$k=5$$: $$5, 11, 17, 23, 29$$ with $$d=6$$; $$k=6$$: $$7, 37, 67, 97, 127, 157$$ with $$d=30$$). The proof is a landmark of additive combinatorics and ergodic/structure theory, not elementary sieve play. Finding an explicit AP of length 4 or 5 by hand or machine is a great *exploration*; proving all lengths exist is not your studio task.

### 1.5 Riemann Hypothesis as an error-term statement

RH is often packaged as zeros of $$\zeta(s)$$, but for this studio keep the **prime-counting error** slogan:

$$
\pi(x)=\operatorname{li}(x)+O\bigl(x^{1/2}\log x\bigr)
$$

(under RH, in standard forms). In probabilistic language, $$x^{1/2}$$ is the signature fluctuation scale of a fair coin-flip random walk. Without RH, weaker error terms are known. Connecting zero-free regions to primes is deep analytic number theory—Ch.1’s RH lesson is the companion deep read.

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


## Video tham khảo

- **xem trước** — [The Riemann Hypothesis, Explained](https://www.youtube.com/watch?v=zlm1aajH6gY) — Quanta Magazine, English. Watch first. “The Riemann Hypothesis, Explained” orients the lesson’s aim: State the Prime Number Theorem at slogan level: \pi(x)\sim x/\log x, and compute \pi(x) for moderate x.
- [Twin Prime Conjecture - Numberphile](https://www.youtube.com/watch?v=QKHKD8bRAro) — Numberphile, English. A second pass once the main claim is in view: State the Prime Number Theorem at slogan level: \pi(x)\sim x/\log x, and compute \pi(x) for moderate x.
