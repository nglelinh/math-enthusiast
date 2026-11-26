---
layout: post
title: "Maynard’s Work on Prime Numbers (Fields Medal 2022)"
chapter: '02'
order: 9
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

As you march further out along the number line, prime numbers grow lonelier and lonelier. Near $$10^{100}$$, the average gap between one prime and the next is roughly $$230$$; near $$10^{1000}$$, it is over $$2{,}300$$. Yet every now and then, two primes suddenly appear almost side by side—like $$29$$ and $$31$$, or $$10{,}000{,}000{,}000{,}000{,}061$$ and $$10{,}000{,}000{,}000{,}000{,}063$$.

For centuries, mathematicians wondered: **do primes ever stop coming close together, or is there some fixed ceiling $$H$$ such that infinitely many consecutive primes sit at most $$H$$ apart?** Formally, writing $$p_n$$ for the $$n$$th prime, is

$$
\liminf_{n\to\infty}(p_{n+1}-p_n) < \infty?
$$

In April 2013, **Yitang Zhang** stunned the world by proving the answer is yes—with $$H = 70{,}000{,}000$$. Months later, a young postdoc named **James Maynard** (and independently Terence Tao) unveiled a far simpler, astonishingly flexible **multidimensional sieve** that slashed the bound down to $$600$$—and, via the collaborative **Polymath8b** project, all the way to

$$
\liminf_{n\to\infty}(p_{n+1}-p_n)\;\le\;246.
$$

Maynard went on to crack major open problems on **large prime gaps**, **primes missing a decimal digit**, and **Duffin–Schaeffer Diophantine approximation**, earning the **Fields Medal in 2022**. This essay unpacks how his sieve actually works (with hand-checkable examples!), why $$246$$ is **not** "almost twin primes," and how sieve theory differs from [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/).

---

## Learning objectives

After this lecture you should be able to:

- State the **bounded-gap theorem**: $$\liminf_n(p_{n+1}-p_n)\le H$$ for an explicit finite $$H$$ (currently $$246$$ unconditionally).
- Check by hand whether a tuple of shifts $$(h_1,\dots,h_k)$$ is **admissible** (avoiding congruence obstructions).
- Explain the weighted pigeonhole principle behind **multidimensional sieve weights** on the simplex $$\Delta_k$$.
- Place **Zhang (2013)**, **Maynard**, **Tao**, and **Polymath8** accurately in the community story.
- Explain clearly why bounded gaps ($$H=246$$) do **not** almost prove the **twin prime conjecture** (the parity barrier).
- Describe Maynard’s achievements beyond small gaps: **large gaps** and **primes with restricted digits**.
- Contrast Maynard’s sieve toolkit with **Green–Tao’s** additive-combinatorics transference.

**Prerequisites.** Primes, modular arithmetic, and the intuition that primes near $$x$$ have density about $$1/\ln x$$. No prior sieve theory is required.

**Related lessons.** Core pair: [Twin Prime Conjecture]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/). Related: [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/), [Euclid infinitude]({{ site.baseurl }}/contents/en/chapter05/05_02_Euclid_Infinite_Primes/), [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/), [prime predictability studio]({{ site.baseurl }}/contents/en/chapter07/07_04_Explore_Prime_Predictability/), and [crypto number theory]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/).

---

## Key ideas: What Is Analytic Sieve Theory?

If you remember the Sieve of Eratosthenes from school—crossing out multiples of $$2$$, then $$3$$, then $$5$$—you have already met the ancestor of Maynard’s toolkit. Modern sieve theory turns that childhood algorithm into a precision analytic instrument.

### 1. Sieve Theory: Detecting Primes Without Listing Them
**What is it?** Directly counting primes is notoriously hard. Sieve theory instead assigns a smooth, non-negative **weight** $$w_n \ge 0$$ to each integer $$n$$, making $$w_n$$ large when $$n$$ (or a cluster $$n+h_1, \dots, n+h_k$$) has no small prime divisors, and tiny otherwise.

**What does it study?**
- **Almost primes & prime constellations:** Using smooth weights (Selberg’s sieve, GPY, Maynard–Tao) to prove that among $$k$$ shifted numbers $$n+h_1, \dots, n+h_k$$, at least $$m$$ of them are simultaneously prime infinitely often.
- **The parity barrier:** A fundamental obstruction discovered by Selberg: pure sieve weights built only from divisor information cannot tell the difference between a number with an **odd** number of prime factors (like a prime, $$1$$ factor) and an **even** number of prime factors (like $$p_1 p_2$$, $$2$$ factors).

### 2. Distribution of Primes in Arithmetic Progressions
**What is it?** Every sieve needs an input telling it how evenly primes are distributed across remainder classes $$a \bmod q$$ (for $$\gcd(a,q)=1$$).

**What does it study?**
- **Bombieri–Vinogradov theorem (1965):** Proves unconditionally that primes are uniformly distributed in arithmetic progressions "on average" up to moduli $$q \le x^{\theta}$$ with **level of distribution $$\theta = \tfrac{1}{2}$$**—essentially as strong as the Generalized Riemann Hypothesis on average!
- **Elliott–Halberstam conjecture:** Predicts that $$\theta$$ can be pushed all the way to $$1$$. One of Maynard’s greatest triumphs is that his multidimensional sieve works using **only** Bombieri–Vinogradov ($$\theta = \tfrac{1}{2}$$), requiring no unproven conjecture at all.

### 3. Harmonic Analysis on Digits & Diophantine Approximation
**What is it?** Beyond prime gaps, Maynard also wields Fourier analysis (the circle method and Markov/Fourier estimates on base-$$10$$ digit expansions) and metric number theory to answer questions like: *Are there infinitely many primes with no digit $$7$$?* and *Which rational approximations occur for almost every real number?*

---


### Short Video 1: Bounded Gaps Between Primes (70 Million → 246)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/maynard-bounded-gaps_en.mp4"></video>
</div>

Short visual overview (1 min 1 sec): from Yitang Zhang's 70,000,000 bound to Maynard's 600 and Polymath8b's 246, m-tuples of primes in bounded intervals, and the parity barrier.

## 1. Gaps between primes: typical, small, and large

Let $$p_1=2,p_2=3,p_3=5,\ldots$$. By the Prime Number Theorem, the average gap $$g_n=p_{n+1}-p_n$$ up to $$x$$ satisfies

$$
\frac{1}{\pi(x)}\sum_{p_n\le x} g_n \;\sim\; \ln x,
$$

so *typical* gaps grow slowly to infinity. Yet averages hide extremes on both sides:

- **Small gaps:** Is $$\liminf g_n < \infty$$? Even stronger, is $$\liminf g_n = 2$$ (infinitely many twin primes)?
- **Large gaps:** How long can a prime-free desert of consecutive composite numbers stretch? Classical constructions give gaps $$\gg \frac{\ln p_n \ln\ln p_n \ln\ln\ln\ln p_n}{(\ln\ln\ln p_n)^2}$$, and Maynard (together with Ford, Green, Konyagin, and Tao) broke a 76-year-old bottleneck to resolve Erdős’s \$10,000 large-gap prize.

---

## 2. Zhang’s breakthrough and the race to $$H=246$$

In 2013, **Yitang Zhang** proved that $$\liminf_{n\to\infty}(p_{n+1}-p_n) \le 70{,}000{,}000$$. Using the **GPY method** (Goldston–Pintz–Yıldırım, 2005), which had been stranded right at the edge of Bombieri–Vinogradov’s $$\theta = \tfrac{1}{2}$$ threshold, Zhang ingeniously pushed the level of distribution *slightly past $$\tfrac{1}{2}$$* for smooth moduli using deep algebraic-geometric exponential sum bounds (Deligne).

Immediately, a worldwide **Polymath8** collaboration drove Zhang’s $$70{,}000{,}000$$ down to $$4{,}680$$. Then, in November 2013, **James Maynard** (and independently **Terence Tao**) changed the game completely: instead of pushing past $$\theta = \tfrac{1}{2}$$, they redesigned the sieve weights themselves! Maynard’s first paper immediately yielded $$H \le 600$$ using only the classical 1965 Bombieri–Vinogradov theorem—and proved something Zhang’s method could not: **for every integer $$m \ge 2$$, there exist infinitely many bounded intervals containing at least $$m$$ primes!** Combining Maynard’s weights with Polymath8b optimizations brought the unconditional bound down to

$$
\liminf_{n\to\infty}(p_{n+1}-p_n)\;\le\;246.
$$

Under the unproven generalized Elliott–Halberstam conjecture, the same machinery reaches $$H \le 6$$—yet still cannot reach $$H=2$$ without breaking the parity barrier.

**Credit culture.** Bounded gaps is a **community triumph**: Zhang opened the door in 2013; Maynard (and independently Tao) built the cleaner, stronger multidimensional sieve; Polymath8 optimized the bound to $$246$$.

---

## 3. Admissible tuples and multidimensional sieve weights

Before hunting for prime constellations $$n+h_1, \dots, n+h_k$$, we must make sure simple modular arithmetic does not kill our tuple from the start.

### Hand-Verifiable Example 1: Admissible vs. Inadmissible Tuples
A tuple $$(h_1, \dots, h_k)$$ is **admissible** if for *every* prime $$p$$, the shifts $$h_i \bmod p$$ miss at least one residue class modulo $$p$$. Check two triples by hand:

- **Inadmissible triple $$(n, n+2, n+4)$$:** Reduce modulo $$3$$! The shifts $$(0, 2, 4)$$ become $$(0, 2, 1) \bmod 3$$—they hit **all three** residue classes modulo $$3$$. That means for *every* integer $$n$$, one of $$n, n+2, n+4$$ is divisible by $$3$$. The only all-prime triple is $$(3, 5, 7)$$; after that, the pattern dies forever!
- **Admissible triple $$(n, n+2, n+6)$$:**
  - Mod $$2$$: shifts are $$(0, 0, 0)$$ — misses $$1 \bmod 2$$ (safe whenever $$n$$ is odd).
  - Mod $$3$$: shifts are $$(0, 2, 0)$$ — misses $$1 \bmod 3$$ (safe whenever $$n \equiv 2 \pmod 3$$).
  - Mod $$p \ge 5$$: there are only $$3$$ shifts and at least $$5$$ residue classes, so at least two classes are automatically missed!

Check it on small integers $$n \equiv 5 \pmod 6$$:
- $$n=5 \implies (5, 7, 11)$$ (all 3 prime!)
- $$n=11 \implies (11, 13, 17)$$ (all 3 prime!)
- $$n=17 \implies (17, 19, 23)$$ (all 3 prime!)
- $$n=41 \implies (41, 43, 47)$$ (all 3 prime!)

### Hand-Verifiable Example 2: The Weighted Pigeonhole Principle
How does a sieve prove that at least two (or $$m$$) entries in an admissible $$k$$-tuple $$(n+h_1, \dots, n+h_k)$$ are prime? Pick non-negative weights $$w_n \ge 0$$ and form the difference

$$
S(N) = \sum_{N < n \le 2N} \left(\sum_{i=1}^{k} \mathbf{1}_{\text{prime}}(n+h_i) - (m-1)\right) w_n.
$$

Look at the logic—it is pure pigeonhole! If every $$n$$ in $$(N, 2N]$$ had at most $$m-1$$ primes among $$n+h_1, \dots, n+h_k$$, then every term inside the parentheses would be $$\le 0$$, forcing $$S(N) \le 0$$. Therefore, **if you can prove $$S(N) > 0$$ for arbitrarily large $$N$$, there MUST be infinitely many $$n$$ for which at least $$m$$ of the numbers $$n+h_1, \dots, n+h_k$$ are simultaneously prime!**

---

### Explanation: Why Maynard’s Multidimensional Sieve Succeeded

Why did the 2005 GPY sieve stall right at the $$\theta = \tfrac{1}{2}$$ wall, while Maynard’s 2013 sieve sailed effortlessly past it? Follow the four steps slowly:

#### Step 1: The GPY 1D bottleneck
GPY chose weights $$w_n$$ depending only on the **product** $$\prod_{i=1}^k (n+h_i)$$—a single one-dimensional variable $$t = t_1 + \dots + t_k$$ measuring the total size of divisors across the tuple. Because that 1D weight treats all $$k$$ coordinates rigidly together, its prime-detection ratio (the quotient of the prime sum to the total weight sum) caps out at a limit that is *just barely* too small when $$\theta = \tfrac{1}{2}$$.

#### Step 2: Maynard’s leap to $$k$$ independent variables on the simplex $$\Delta_k$$
Maynard replaced the single divisor variable with $$k$$ separate divisor variables $$d_1 \mid (n+h_1), \dots, d_k \mid (n+h_k)$$ controlled by a smooth symmetric function $$F(t_1, \dots, t_k)$$ supported on the $$k$$-dimensional simplex

$$
\Delta_k = \left\{(t_1,\dots,t_k) \in [0,1]^k : t_1 + t_2 + \dots + t_k \le 1\right\}.
$$

Now the sieve can reward integers $$n$$ where individual components $$n+h_i$$ individually avoid small prime divisors, rather than lumping them into one product.

#### Step 3: Turn prime detection into a calculus maximization problem
Using Bombieri–Vinogradov ($$\theta = \tfrac{1}{2}$$), Maynard evaluated both sums asymptotically in terms of two explicit $$k$$-dimensional integrals $$I_k(F)$$ and $$J_k(F)$$. The pigeonhole condition $$S(N) > 0$$ reduces cleanly to finding a smooth function $$F$$ on $$\Delta_k$$ such that

$$
\frac{\theta}{2} \cdot \frac{k\, J_k(F)}{I_k(F)} > m - 1.
$$

#### Step 4: The logarithmic explosion $$M_k \to \infty$$
Let $$M_k = \sup_F \frac{k\, J_k(F)}{I_k(F)}$$. Whereas the 1D GPY ratio stayed bounded below $$4$$ no matter how huge $$k$$ was, Maynard proved that in $$k$$ dimensions,

$$
M_k > \ln k - 2\ln\ln k - 2 \;\longrightarrow\; \infty \quad \text{as } k \to \infty!
$$

That single divergence changes everything: **for ANY positive level of distribution $$\theta > 0$$ and ANY desired number of primes $$m$$**, you simply pick $$k$$ large enough that $$\frac{\theta}{2} M_k > m-1$$! For $$m=2$$ and $$\theta=\tfrac{1}{2}$$, choosing $$k=50$$ (with diameter $$246$$, optimized by Polymath8b) pushes $$\frac{1}{4}M_{50} > 1$$, locking in $$\liminf (p_{n+1}-p_n) \le 246$$.

In one schematic line:

$$
\text{Admissible }k\text{-tuple}
\;+\;
k\text{-variable weight }F\text{ on }\Delta_k
\;+\;
\text{Bombieri–Vinogradov }(\theta=\tfrac{1}{2})
\;\Longrightarrow\;
M_k \to \infty \implies \text{bounded gaps \& }m\text{-clusters}.
$$

---


### Short Video 2: How the Maynard–Tao Multidimensional Sieve Breaks the 1D Bottleneck

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/maynard-multidim-sieve_en.mp4"></video>
</div>

Short visual walkthrough (40 sec): admissible tuples like (0, 2, 6), the GPY 1D bottleneck at level of distribution 1/2, and smooth k-variable weights on the simplex.

## 4. Not the twin prime conjecture

The **twin prime conjecture** asserts infinitely many primes $$p$$ with $$p+2$$ also prime—gap **exactly** $$2$$ infinitely often. Bounded gaps assert only that some even gap $$\le 246$$ occurs infinitely often.

$$
\text{twin primes}
\;\Longrightarrow\;
\liminf g_n = 2
\;\Longrightarrow\;
\liminf g_n \le 246,
$$

but none of the reverse arrows follows from current theorems. Seeing $$246$$ and thinking "we are 99% of the way to $$2$$" is a classic trap. Even if you take $$k=2$$ (the twin tuple $$(n, n+2)$$), the **parity barrier** prevents pure sieve weights from proving $$\frac{\theta}{2} M_2 > 1$$ unless you somehow had $$\theta > 1$$—which is impossible! Closing the gap from $$246$$ to $$2$$ requires a genuinely new mechanism outside classical sieve weights.

**Chen’s theorem** (every sufficiently large even integer is $$p + P_2$$, a prime plus a product of at most two primes) illustrates the exact same parity wall from another angle. See the [twin prime lecture]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/) for Hardy–Littlewood heuristics and parity discussion.

---

## 5. Large gaps and primes with restricted digits

Maynard’s Fields Medal recognizes a sweeping body of work on the structure of primes, far beyond $$246$$:

- **Large gaps (with Ford, Green, Konyagin, Tao):** Proved that gaps between consecutive primes can be arbitrarily large multiples of $$\frac{\ln p_n \ln\ln p_n \ln\ln\ln\ln p_n}{(\ln\ln\ln p_n)^2}$$, settling a classic Erdős problem by combining hypergraph covering ideas with Maynard’s multidimensional sieve.
- **Primes with restricted digits (2019):** Proved there are infinitely many prime numbers whose base-10 expansion **never uses the digit 7** (or any single forbidden digit $$d \in \{0,\dots,9\}$$)! Numbers missing a digit are astonishingly sparse—up to $$10^N$$, only $$9^N = (10^N)^{0.954\dots}$$ integers survive, a zero-density fractal set. Maynard fused sieve theory with delicate Fourier analysis on base-10 expansions to prove primes still thrive inside it.
- **Duffin–Schaeffer conjecture (with Koukoulopoulos, 2019):** Settled an 80-year-old foundational conjecture in Diophantine approximation using graph-theoretic "GCD graphs" to measure overlap of rational approximations.

---


### Short Video 3: Infinitely Many Primes Missing the Digit 7

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/maynard-missing-digits_en.mp4"></video>
</div>

Short visual walkthrough (36 sec): Maynard's 2019 theorem on primes with restricted decimal digits via Fourier analysis on digit expansions and the Hardy–Littlewood circle method.

## 6. Contrast with Green–Tao

| Feature | Green–Tao | Zhang–Maynard gaps |
|---------|-----------|---------------------|
| Pattern | Arbitrarily long APs of primes | Bounded consecutive gaps (and $$m$$-prime clusters) |
| Engine | Transference + pseudorandom majorants + Szemerédi | Multidimensional sieves + Bombieri–Vinogradov |
| Density issue | Primes have density zero vs. Szemerédi | Need primes in multiple linear forms simultaneously |
| Open twin-like end | Not about gap $$2$$ | Gap $$2$$ still open (parity barrier) |
| Fields narrative | Tao 2006 (broad work; GT landmark) | Maynard 2022; Zhang’s 2013 breakthrough opened the door |

Both prove primes harbor rich structure, yet they answer **different pattern questions** with **different engines**.

---

## 7. Why it matters

Bounded gaps reopened a centuries-old frontier: asymptotic hopes became theorems with explicit constants. Maynard’s multidimensional weights turned a fragile breakthrough into a portable engine powering small gaps, prime clusters, large gaps, and restricted-digit primes alike.

**Accuracy notes.**
- Twin primes remain open.
- $$H=246$$ is the standard unconditional community-optimized figure (Maynard + Polymath8b).

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Bounded gaps = twin prime conjecture.” | Twins need gap $$2$$ infinitely often; bounded gaps allow a larger fixed $$H$$. |
| “Maynard alone discovered bounded gaps.” | Zhang’s 2013 breakthrough opened the field; Maynard, Tao, and Polymath8 simplified and sharpened it. |
| “$$H=246$$ means twins are 99% done.” | Numerical distance to $$2$$ is small; the parity barrier is a conceptual wall. |
| “Green–Tao already gave bounded gaps.” | Green–Tao gives long arithmetic progressions, not a uniform bound on consecutive gaps. |
| “Sieves prove numbers are prime.” | Sieves detect *almost primes* or force *at least $$m$$ primes inside a larger $$k$$-tuple*; isolating one exact prime form hits parity limits. |
| “Large gaps contradict the prime number theorem.” | PNT controls averages; large gaps are rare spikes compatible with average $$\ln x$$. |

---

## Video sources (math-video-researcher pack)

Use videos and primary sources for **orientation and research culture**. Full ranking and Mode B notes: `research/video-research/Maynard_Primes/`.

**Recommended order**

1. **Orientation** — Numberphile, *Twin Prime Conjecture* (James Maynard): [YouTube](https://www.youtube.com/watch?v=QKHKD8bRAro).  
2. **History** — Numberphile, *Gaps between Primes* (Zhang-era): [YouTube](https://www.youtube.com/watch?v=vkMXdShDdtY) · extra: [YouTube](https://www.youtube.com/watch?v=D4_sNKoO-RA).  
3. **Core** — Maynard, *Patterns in prime numbers* (G-Research): [YouTube](https://www.youtube.com/watch?v=ey_57qWhGEM).  
4. **Meta** — Simons Fields Medal video page: [link](https://www.simonsfoundation.org/2022/07/05/fields-medal-video-james-maynard/); Numberphile Fields conversation: [YouTube](https://www.youtube.com/watch?v=eupAXdWPvX8).

**Status reminder:** Bounded gaps **proved**; twin primes (gap $$2$$ infinitely often) remain **open**. Zhang’s breakthrough is part of the same story.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Maynard_Primes/transcripts/` · status: `research/video-research/Maynard_Primes/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Maynard_Primes_QKHKD8bRAro_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


Full URL bibliography from video research (including secondary finds): `research/video-research/Maynard_Primes/references.md`.

### Complete URL list (audit)

1. https://www.youtube.com/watch?v=QKHKD8bRAro  
2. https://www.youtube.com/watch?v=vkMXdShDdtY  
3. https://www.youtube.com/watch?v=D4_sNKoO-RA  
4. https://www.youtube.com/watch?v=ey_57qWhGEM  
5. https://www.simonsfoundation.org/2022/07/05/fields-medal-video-james-maynard/  
6. https://arxiv.org/abs/1311.4600  
7. https://arxiv.org/pdf/1311.4600  
8. https://arxiv.org/abs/1412.5029  
9. https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/laudatio-jm.pdf  
10. https://www.quantamagazine.org/number-theorist-james-maynard-wins-the-fields-medal-20220705/  
11. https://www.numberphile.com/videos/twin-prime-conjecture  
12. https://en.wikipedia.org/wiki/Twin_prime  
13. https://en.wikipedia.org/wiki/James_Maynard_(mathematician)  
14. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022  
15. https://www.youtube.com/watch?v=eupAXdWPvX8  

### Research pack

16. Course pack: `research/video-research/Maynard_Primes/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. IMU Fields Medal 2022 citation — James Maynard.
2. Y. Zhang — bounded gaps between primes (*Annals of Mathematics*, 2014).
3. J. Maynard — small gaps between primes; work on large gaps and restricted digits.
4. Polymath8 projects — optimizations of Zhang’s bound; expositions of Maynard weights and $$H=246$$.
5. Goldston–Pintz–Yıldırım — GPY method background; classical sieve texts (Halberstam–Richert; Friedlander–Iwaniec).
6. Course cross-links: [Twin primes]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/), [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/), [Euclid]({{ site.baseurl }}/contents/en/chapter05/05_02_Euclid_Infinite_Primes/).

---

## Further directions

- Read a gentle introduction to the Selberg sieve, then revisit multidimensional weights as a modern upgrade.
- Study Polymath as a model of collaborative analytic number theory (process + mathematics).
- Exploration studio: compute consecutive prime gaps up to a bound $$N$$ and plot the running liminf candidate; discuss how computation illustrates but does not prove infinitude.
- Optional: conditional world under Elliott–Halberstam—what $$H$$ become available, and why $$H=2$$ still resists.
- Return to [Ch.01 twins]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/) for heuristics; stay here for the Fields-level sieve technology story.

## Video tham khảo

- **xem trước** — [Twin Prime Conjecture - Numberphile](https://www.youtube.com/watch?v=QKHKD8bRAro) — Numberphile, English. Watch first. “Twin Prime Conjecture - Numberphile” orients the lesson’s aim: State a bounded-gap theorem: \liminfn(p{n+1}-pn)\le H for an explicit finite H.
- [Gaps between Primes - Numberphile](https://www.youtube.com/watch?v=vkMXdShDdtY) — Numberphile, English. A second pass once the main claim is in view: State a bounded-gap theorem: \liminfn(p{n+1}-pn)\le H for an explicit finite H.
- [James Maynard - Patterns in prime numbers](https://www.youtube.com/watch?v=ey_57qWhGEM) — G-Research, English. Further depth after the first two, still tied to this lesson: State a bounded-gap theorem: \liminfn(p{n+1}-pn)\le H for an explicit finite H.
