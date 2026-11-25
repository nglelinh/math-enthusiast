---
layout: post
title: "The Twin Prime Conjecture"
chapter: '01'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter01
lesson_type: required
---

Walk out along the number line and listen for prime numbers: $$2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, \ldots$$ As the numbers grow larger, primes thin out—their average spacing grows like $$\log x$$, so near $$10^{100}$$ you might wander across two hundred composite numbers before spotting a single prime. Yet every so often, two odd primes still appear shoulder to shoulder, separated by the smallest possible gap of $$2$$: $$(3,5)$$, $$(5,7)$$, $$(11,13)$$, $$(17,19)$$, $$(29,31)$$, $$(101,103)$$, $$(107,109)$$, and even pairs hundreds of thousands of digits long.

The **Twin Prime Conjecture** asks a deceptively simple question: *do these close companions keep appearing forever?*

More than two thousand years ago, Euclid proved in five lines that there are infinitely many primes. Proving there are infinitely many *twin* primes remains wide open. Yet in 2013, the field experienced one of the most dramatic breakthroughs of the twenty-first century. A relatively unknown lecturer named **Yitang Zhang** proved that *some* bounded even gap (less than $$70{,}000{,}000$$) occurs infinitely often between consecutive primes. Within months, **James Maynard**, **Terence Tao**, and the collaborative **Polymath8** project drove that unconditional bound all the way down to **$$H = 246$$**. Numerically, $$246$$ looks a stone’s throw from $$2$$. Mathematically, a formidable wall—the **parity barrier**—still stands in between.

---

## Learning objectives

After this lecture you should be able to:

- State the **Twin Prime Conjecture** cleanly and distinguish twin pairs from non-examples.
- Explain why Euclid’s proof of infinitely many primes does not carry over to twin primes.
- Derive and test the **Hardy–Littlewood** heuristic and the twin prime constant $$C_2$$ on small primes.
- State the **bounded gaps** theorem ($$\liminf_{n\to\infty}(p_{n+1}-p_n) \le 246$$) and trace the roles of **Zhang (2013)**, **Maynard**, **Tao**, and **Polymath8**.
- Explain what an **admissible tuple** is and why the **parity barrier** stops current sieves from reaching gap $$2$$.
- Connect twin primes to the [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) and [Maynard’s Fields Medal work]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/).

**Prerequisites.** Primes, basic modular arithmetic (remainders mod $$p$$), and the Prime Number Theorem heuristic that primes near $$x$$ have density roughly $$1/\log x$$.

**Course links.** Pair with [Maynard’s Fields Medal essay]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/), [Euclid’s infinitude of primes]({{ site.baseurl }}/contents/en/chapter05/05_02_Euclid_Infinite_Primes/), and the [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/).

---

## Key ideas: What Fields Sit Behind Twin Primes?

Why does a question a ten-year-old can understand require Fields-Medal-level machinery? Twin primes sit at the intersection of three major pillars of modern number theory.

### 1. Analytic Number Theory
Instead of studying primes purely through algebra, **analytic number theory** uses calculus, complex analysis, and asymptotic estimates to measure how primes behave *on average*. Its flagship result, the Prime Number Theorem, says the density of primes near $$x$$ is about $$1/\log x$$.
- **Core questions:** How evenly are primes distributed across residue classes $$a \pmod q$$? How small—and how large—can consecutive prime gaps $$p_{n+1}-p_n$$ become?
- **Real-world reach:** Prime generation and primality testing in RSA/public-key cryptography, hashing, and pseudorandom number design.

### 2. Sieve Theory
Start with the ancient **Sieve of Eratosthenes**: cross out multiples of $$2$$, then $$3$$, then $$5$$, and see what survives. Modern **sieve theory** (Brun, Selberg, Goldston–Pintz–Yıldırım, Maynard) replaces raw crossing-out with carefully optimized *weights* $$\lambda_d$$ so we can rigorously estimate how many integers in a sequence avoid small prime divisors.
- **Core questions:** How can we detect primes inside sparse sets like $$\{p+2\}$$ or $$\{n^2+1\}$$? How close can we get to primes when sieves only see small factors (*almost primes*)?
- **Real-world reach:** Integer factorization algorithms (Quadratic Sieve, Number Field Sieve) that directly set security key-length standards in modern cryptography.

### 3. Additive Combinatorics and Prime Patterns
Multiplication defines primes, yet asking for $$p$$ and $$p+2$$ both to be prime mixes **multiplication** with **addition** ($$+2$$). That tension between additive shifts and multiplicative indivisibility is the signature of additive number theory (twin primes, Goldbach’s conjecture, Green–Tao’s arithmetic progressions of primes).
- **Core questions:** Which additive constellations $$\{n+h_1,\ldots,n+h_k\}$$ appear infinitely often inside the primes?
- **Real-world reach:** Coding theory, expander graphs, and pseudorandom constructions in theoretical computer science.

---

## 1. Statement and first examples

**Twin Prime Conjecture.** There are infinitely many primes $$p$$ such that $$p+2$$ is also prime.

Equivalently, the equation $$p' - p = 2$$ has infinitely many solutions in prime pairs $$(p, p')$$.

Except for $$(2,3)$$ (gap $$1$$, unique because $$2$$ is the only even prime), every consecutive prime pair has an even gap, and the tightest possible gap is $$2$$. Note that $$(2,4)$$ is *not* a twin pair ($$4=2^2$$) and $$(7,9)$$ fails ($$9=3^2$$): **both** numbers must be prime.

Below $$100$$, there are exactly **8** twin prime pairs:

$$
(3,5),\ (5,7),\ (11,13),\ (17,19),\ (29,31),\ (41,43),\ (59,61),\ (71,73).
$$

Computers have found twin primes with hundreds of thousands of digits, and the density tracks theoretical predictions closely. Still, any finite list—even up to $$10^{18}$$—proves nothing about infinity.

---

## 2. Euclid’s infinitude versus twins

Euclid’s classic proof of infinitely many primes is effortless: given any finite list $$p_1,\ldots,p_k$$, form $$N = p_1\cdots p_k + 1$$. Because $$N$$ leaves remainder $$1$$ when divided by every $$p_i$$, any prime divisor of $$N$$ must be brand new.

Why doesn’t a quick tweak prove twin primes? Because adding $$+2$$ breaks the clean multiplicative lock. You can force $$N$$ to avoid small prime factors, yet $$N+2$$ can still be composite for completely unrelated reasons. Even worse, $$N$$ itself is usually composite—Euclid only grabs *some* prime factor of $$N$$, giving zero control over whether that factor’s neighbor $$p+2$$ is prime.

---

### Short video: Counting twin primes against the heuristic

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/twin-primes-count_en.mp4"></video>
</div>

The grid marks the 8 twin prime pairs below 100. The chart compares the actual number of twin pairs up to $$x$$ (dots) with the Hardy–Littlewood prediction (curve): 8169 against about 8248 at $$x = 10^6$$. A good fit is evidence, not a proof.


### Try it yourself: Count twin primes yourself

<div class="mex-explainer" data-mex="twins" data-lang="en"></div>


## 3. Heuristics: Hardy–Littlewood and the twin prime constant

By the Prime Number Theorem, a random integer near $$n$$ is prime with “probability” roughly $$1/\log n$$. If $$n$$ and $$n+2$$ behaved independently, the probability that *both* are prime would be $$1/(\log n)^2$$. Since

$$
\sum_{n=3}^{\infty} \frac{1}{(\log n)^2} = \infty,
$$

the naive model already predicts infinitely many twin primes.

Of course, $$n$$ and $$n+2$$ are **not** independent! For example, if $$n$$ is odd (not divisible by $$2$$), then $$n+2$$ is *automatically* odd too—giving twin pairs a $$2\times$$ boost at the prime $$2$$! **Hardy and Littlewood (1923)** turned this modular bookkeeping into a sharp quantitative conjecture: the number of twin prime pairs $$\pi_2(X)$$ up to $$X$$ should satisfy

$$
\pi_2(X) \sim 2C_2 \int_2^{X} \frac{dt}{(\log t)^2}, \qquad C_2 = \prod_{p\ge 3}\left(1 - \frac{1}{(p-1)^2}\right) \approx 0.6601618\ldots
$$

---

### Worked Example 1: Computing the Hardy–Littlewood Factor by Hand at $$p = 2, 3, 5$$

Where does the mysterious factor $$2C_2 \approx 1.32032$$ come from? Let’s compute the first three local correction factors by hand, comparing the **actual** chance that neither $$n$$ nor $$n+2$$ is divisible by $$p$$ against the **independent** chance $$\bigl(1-\frac{1}{p}\bigr)^2$$:

1. **At $$p = 2$$:**
   - Independent guess: both $$n$$ and $$n+2$$ are odd with probability $$\frac{1}{2}\cdot\frac{1}{2} = \frac{1}{4}$$.
   - Reality: $$n$$ and $$n+2$$ have the *same* parity, so $$1$$ out of $$2$$ residue classes ($$n \equiv 1 \pmod 2$$) works! Probability $$= \frac{1}{2}$$.
   - Local correction factor: $$\dfrac{1/2}{1/4} = 2$$.
2. **At $$p = 3$$:**
   - Independent guess: $$\bigl(\frac{2}{3}\bigr)^2 = \frac{4}{9}$$.
   - Reality: $$n \not\equiv 0$$ and $$n+2 \not\equiv 0 \pmod 3$$ forbid *two* classes ($$0$$ and $$1$$), leaving only $$n \equiv 2 \pmod 3$$. Probability $$= \frac{1}{3}$$.
   - Local correction factor: $$\dfrac{1/3}{4/9} = \dfrac{3}{4} = 1 - \dfrac{1}{(3-1)^2}$$.
3. **At $$p = 5$$:**
   - Independent guess: $$\bigl(\frac{4}{5}\bigr)^2 = \frac{16}{25}$$.
   - Reality: forbid $$n \equiv 0$$ and $$n \equiv 3 \pmod 5$$, leaving $$3$$ of $$5$$ classes. Probability $$= \frac{3}{5}$$.
   - Local correction factor: $$\dfrac{3/5}{16/25} = \dfrac{15}{16} = 1 - \dfrac{1}{(5-1)^2}$$.

Multiply just those first three primes:

$$
2 \times \frac{3}{4} \times \frac{15}{16} = \frac{45}{32} = 1.40625.
$$

Continuing over all odd primes $$p \ge 7$$ pulls $$1.40625$$ gently down to $$2C_2 \approx 1.32032$$! Plugging this into the integral at $$X = 10^6$$ predicts **$$\approx 8{,}248$$** twin pairs, while the exact count is **$$8{,}169$$**—within $$1\%$$! Evidence this tight explains why virtually every number theorist believes the conjecture, even though heuristics are never proofs.

---

## 4. Why sieves struggle: almost primes and the parity barrier

**Sieve methods** systematically filter out multiples of small primes. In 1919, **Viggo Brun** used a combinatorial sieve to prove that the sum of reciprocals of twin primes converges ($$\sum \bigl(\frac{1}{p}+\frac{1}{p+2}\bigr) \approx 1.90216$$, **Brun’s constant**)—in sharp contrast to Euler’s diverging sum $$\sum 1/p = \infty$$. That proved twin primes are much rarer than ordinary primes, while remaining compatible with either finitely or infinitely many twins.

The closest classical siege on twin primes is **Chen’s theorem (1973)**: there are infinitely many primes $$p$$ such that $$p+2$$ is either prime or a product of two primes ($$P_2$$).

Why couldn’t Chen’s sieve go the last inch from “at most 2 prime factors” to “exactly 1 prime factor”? Because of the **parity barrier** (identified by Atle Selberg): classical sieves only see divisibility by small primes, and from that information alone they cannot cleanly tell whether a surviving integer has an **odd** number of prime factors (like a prime, $$1$$ factor) or an **even** number of prime factors (like a semiprime $$q_1 q_2$$, $$2$$ factors).

---

## 5. Bounded gaps: Zhang, Maynard, Polymath

In April 2013, **Yitang Zhang** stunned the mathematical world by proving

$$
\liminf_{n\to\infty} (p_{n+1}-p_n) < 70{,}000{,}000.
$$

For the first time in history, we knew that prime gaps do not have to grow forever—some fixed finite gap occurs **infinitely often**.

Zhang built on the **Goldston–Pintz–Yıldırım (GPY)** sieve for **admissible tuples** of shifts $$\{h_1,\ldots,h_k\}$$, combined with a breakthrough estimate on primes in arithmetic progressions past the classical Bombieri–Vinogradov threshold.

Then the race exploded:

- **Polymath8a** (led online by Terence Tao) optimized Zhang’s argument, slashing $$70{,}000{,}000$$ down to $$4{,}680$$.
- **James Maynard** (and independently Terence Tao) invented a **multidimensional sieve weighting** that bypassed Zhang’s delicate distribution bottleneck entirely—immediately dropping the bound to $$600$$ and proving *arbitrarily many* primes in bounded intervals!
- **Polymath8b** combined Maynard–Tao with refined admissible tuples to reach the current unconditional benchmark:

$$
\liminf_{n\to\infty} (p_{n+1}-p_n) \le 246.
$$

Under the unproved **Elliott–Halberstam conjecture**, the same machinery drops to $$H = 6$$—still stopping short of $$H = 2$$ because of the parity barrier. Maynard’s innovations on prime gaps earned him a **Fields Medal in 2022** (see the [Maynard Fields essay]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/)).

---

### Worked Example 2: Checking Admissible Tuples by Hand — Why $$\{0,2,4\}$$ Dies and $$\{0,2,6\}$$ Survives

In the Zhang–Maynard–Tao breakthrough, you don’t search directly for two primes $$\{n, n+2\}$$. You pick a **$$k$$-tuple** of shifts $$\mathcal{H} = \{h_1,\ldots,h_k\}$$ and hope that at least **two** of $$n+h_1,\ldots,n+h_k$$ are simultaneously prime infinitely often.

For that even to be *possible*, $$\mathcal{H}$$ must be **admissible**: for every prime $$p$$, the shifts $$h_i \pmod p$$ must **miss at least one remainder** mod $$p$$. Otherwise, for *every* integer $$n$$, one of the $$n+h_i$$ is guaranteed to be divisible by $$p$$!

Let’s test two tiny 3-tuples by hand:

1. **Test $$\mathcal{H}_1 = \{0, 2, 4\}$$:**
   - Mod $$2$$: residues are $$\{0, 0, 0\}$$ — misses $$1 \pmod 2$$. (OK!)
   - Mod $$3$$: residues are $$\{0, 2, 1\}$$ — covers **all three** remainders $$\{0,1,2\}$$!
   - **Verdict:** **Inadmissible.** For *every* $$n$$, one of $$n, n+2, n+4$$ is a multiple of $$3$$. The only prime triple of this shape is $$(3,5,7)$$; beyond that, it is dead forever.
2. **Test $$\mathcal{H}_2 = \{0, 2, 6\}$$:**
   - Mod $$2$$: residues are $$\{0, 0, 0\}$$ — misses $$1 \pmod 2$$. (OK!)
   - Mod $$3$$: residues are $$\{0, 2, 0\}$$ — misses $$1 \pmod 3$$. (OK!)
   - Any prime $$p \ge 5$$: there are only $$3$$ numbers in $$\mathcal{H}_2$$, so they can cover at most $$3 < p$$ remainders mod $$p$$. (Automatically OK!)
   - **Verdict:** **Admissible!** Indeed, try $$n = 5 \to (5,7,11)$$, $$n = 11 \to (11,13,17)$$, $$n = 17 \to (17,19,23)$$.

To get the bound $$H = 246$$, Polymath8b constructed an admissible **50-tuple** of width $$246$$ (from $$h_1 = 0$$ to $$h_{50} = 246$$). The Maynard–Tao sieve guarantees that for infinitely many $$n$$, at least **2** of those 50 shifted slots are prime—so their difference is at most $$246$$!

---

### Explanation: How Zhang, Maynard, and Polymath8 Outflanked the Parity Barrier

How did mathematicians prove $$H = 246$$ when the parity barrier still blocks $$H = 2$$? Follow these four steps.

#### Step 1: Trade "both are prime" for "at least 2 out of $$k$$ are prime"
A sieve trying to prove twin primes ($$k = 2$$, tuple $$\{0, 2\}$$) has to verify that *both* $$n$$ and $$n+2$$ have exactly $$1$$ prime factor. The parity barrier blocks this directly. Instead, GPY, Zhang, and Maynard widen the target to a large admissible $$k$$-tuple $$\{n+h_1,\ldots,n+h_k\}$$. You no longer need *all* $$k$$ slots to be prime—you only need the weighted average number of primes in the tuple to exceed **$$1$$**!

#### Step 2: Set up the weighted pigeonhole inequality
Assign a nonnegative weight $$w(n) \ge 0$$ to each integer $$n$$ that rewards $$n$$ when $$n+h_1,\ldots,n+h_k$$ have few small prime factors. Compute the ratio
$$
\frac{\sum_{N < n \le 2N} \bigl(\text{number of primes among } n+h_1,\ldots,n+h_k\bigr)\, w(n)}{\sum_{N < n \le 2N} w(n)}.
$$
If this average is **strictly greater than $$1$$** for arbitrarily large $$N$$, then by the pigeonhole principle, infinitely many $$n$$ must contain **at least 2 primes** inside the window $$[n+h_1, n+h_k]$$!

#### Step 3: Why GPY fell a hair short—and how Maynard unlocked it
GPY used a 1-dimensional weight depending only on the product $$\prod (n+h_i)$$. With the classical Bombieri–Vinogradov level of distribution $$\theta = 1/2$$, the GPY ratio topped out right at $$1$$—missing $$> 1$$ by an infinitesimal hair! Zhang (2013) pushed slightly past $$\theta = 1/2$$ for smooth moduli, nudging the ratio above $$1$$ for $$k \approx 3.5 \times 10^6$$. Months later, Maynard allowed the weights to depend *separately* on each factor $$n+h_i$$ (a multidimensional sieve). That boosted the ratio to $$\sim \frac{1}{2}\log k$$—which easily beats $$1$$ (and even beats any integer $$m$$!) as soon as $$k$$ is moderately large, using only classical Bombieri–Vinogradov!

#### Step 4: Why $$k = 50$$ (width 246) works, yet $$k = 2$$ (width 2) stays locked
For Maynard’s multidimensional ratio to beat $$1$$ unconditionally, you need $$k \ge 50$$—and the narrowest admissible 50-tuple has diameter $$246$$. Even if you assumed the full Elliott–Halberstam conjecture ($$\theta = 1$$), the parity barrier still prevents the ratio for a 2-tuple $$\{0,2\}$$ from crossing $$1$$: a 2-tuple is simply too tight for pure sieve weights to separate primes from semiprimes. Cracking gap $$2$$ will require a genuinely new idea beyond current sieve theory.

---

## 6. What is proved and what remains open

| Statement | Status |
|-----------|--------|
| Infinitely many primes | **Proved** (Euclid) |
| Infinitely many twin primes (gap $$2$$) | **Open** |
| Some bounded even gap infinitely often | **Proved** (Zhang / Maynard / Polymath) |
| $$\liminf (p_{n+1}-p_n) \le 246$$ | **Proved** (unconditional benchmark) |
| Gap $$= 2$$ infinitely often | **Open** |
| Chen’s theorem ($$p+2$$ prime or semiprime) | **Proved** |
| Hardy–Littlewood asymptotic for twins | **Open** (conjectural) |

Bounded gaps prove that primes cluster tightly infinitely often. Twin primes demand the tightest possible even cluster. The step from $$246$$ to $$2$$ is tiny on a number line and monumental in method.

---

## 7. Polignac, prime tuples, and the wider landscape

**de Polignac’s conjecture** predicts that every positive even gap $$2k$$ occurs infinitely often between consecutive primes; twin primes are the case $$k = 1$$. Bounded-gap theorems prove that *at least one* even gap in a finite admissible set occurs infinitely often, without yet pinning it to $$2$$.

**Prime tuples.** More generally, the Hardy–Littlewood $$k$$-tuple conjecture predicts that *every* admissible tuple $$\{h_1,\ldots,h_k\}$$ generates infinitely many simultaneous prime constellations. Meanwhile, the **Green–Tao theorem** (arbitrarily long arithmetic progressions of primes) attacks prime patterns from additive combinatorics rather than sieves.

**Connections to RH.** The [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) controls global counting errors of primes via zeta zeros, whereas twin primes are an additive correlation problem. Assuming RH or GRH sharpens many prime-distribution estimates, yet does not by itself imply the Twin Prime Conjecture.

---

## 8. Mathematics around the problem (toolkit map)

- **Sieve theory:** Selberg sieve, combinatorial sieves, GPY method, Maynard–Tao multidimensional weights.
- **Primes in arithmetic progressions:** Bombieri–Vinogradov theorem (GRH on average); Elliott–Halberstam conjecture.
- **Admissible tuples:** minimizing the diameter $$h_k - h_1$$ for a given $$k$$ (turning $$k=50$$ into $$H=246$$).
- **Computational number theory:** searching record twin primes and testing Hardy–Littlewood predictions.

---

## From videos: the 2013–2014 cascade in slogans

Numberphile’s Zhang and Maynard videos, Maynard’s Princeton colloquium, and the 2013 Quanta narrative tell one connected story:

1. **GPY (Goldston–Pintz–Yıldırım)** built a sieve that *would* yield bounded gaps if primes had slightly better distribution in arithmetic progressions than Bombieri–Vinogradov provides.  
2. **Zhang (2013)** broke past the $$1/2$$ barrier for smooth moduli, proving $$\liminf (p_{n+1}-p_n) < 70{,}000{,}000$$ (optimized by Polymath8a).  
3. **Maynard (and independently Tao)** introduced multidimensional sieve weights that bypassed the $$1/2$$ bottleneck; Polymath8b optimized the unconditional bound to **$$H = 246$$**.  
4. **Still open:** gap $$2$$ (twin primes), where the **parity barrier** still blocks the final step.

**Status (as of 2026):** Twin Prime Conjecture **open**; bounded gaps **proved**.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Zhang proved twin primes.” | He proved *some* bounded gap infinitely often, not gap $$2$$. |
| “Bounded gaps = twin primes.” | Bounded means $$\le H$$ for some fixed $$H$$; twins require $$H=2$$. |
| “There are only finitely many twins in tables.” | Tables are finite by definition; the conjecture is about infinity. |
| “Euclid’s proof adapts easily to twins.” | Euclid’s product $$+1$$ trick does not force a twin pair. |
| “Maynard alone discovered bounded gaps.” | Zhang’s 2013 breakthrough opened the door; Maynard, Tao, and Polymath pushed it dramatically further. |
| “$$H=246$$ is almost $$2$$, so twins are nearly done.” | Numerically close, but methodologically blocked by the parity barrier. |

---

## Video sources (math-video-researcher pack)

Full ranking and notes: `research/video-research/Twin_Prime_Conjecture/`.

**Recommended order**

1. **Orientation** — Numberphile, *Gaps between Primes* (Zhang story): [YouTube](https://www.youtube.com/watch?v=vkMXdShDdtY).  
2. **Core popular** — Numberphile, *Twin Prime Conjecture* (James Maynard): [YouTube](https://www.youtube.com/watch?v=QKHKD8bRAro) · [page](https://www.numberphile.com/videos/twin-prime-conjecture).  
3. **Research lecture** — Maynard, *Small Gaps Between Primes* (Princeton colloquium): [YouTube](https://www.youtube.com/watch?v=E-W47F9upkU).  
4. **Written story** — Quanta (2013): [closing the prime gap](https://www.quantamagazine.org/mathematicians-team-up-on-twin-primes-conjecture-20131119/).  
5. **Paper** — Maynard arXiv: [1311.4600](https://arxiv.org/abs/1311.4600).

**After videos:** bounded gaps **proved**; twin primes (gap $$2$$) **open** as of 2026. Do not write “Zhang proved the twin prime conjecture.”

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Twin_Prime_Conjecture/transcripts/` · status: `research/video-research/Twin_Prime_Conjecture/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Twin_Prime_Conjecture_vkMXdShDdtY_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full bibliography: `research/video-research/Twin_Prime_Conjecture/references.md`.

### Papers and surveys

1. Y. Zhang — bounded gaps between primes (*Annals of Mathematics*, 2014).  
2. J. Maynard — [arXiv:1311.4600](https://arxiv.org/abs/1311.4600) · [Annals](https://annals.math.princeton.edu/2015/181-1/p07) · survey [arXiv:1910.13450](https://arxiv.org/abs/1910.13450).  
3. Polymath8 — optimizations toward $$H=246$$: http://bit.ly/polymath8  
4. Hardy–Littlewood prime tuples; Chen’s almost-twins; Halberstam–Richert / Friedlander–Iwaniec.  
5. Wikipedia — [Twin prime](https://en.wikipedia.org/wiki/Twin_prime).  

### Videos and news

6. Numberphile Zhang gaps: https://www.youtube.com/watch?v=vkMXdShDdtY  
7. Numberphile Maynard twins: https://www.youtube.com/watch?v=QKHKD8bRAro  
8. Maynard Princeton colloquium: https://www.youtube.com/watch?v=E-W47F9upkU  
9. Quanta 2013: https://www.quantamagazine.org/mathematicians-team-up-on-twin-primes-conjecture-20131119/  
10. HK Laureate Forum note: https://www.hklaureateforum.org/en/the-twin-prime-conjecture-and-the-polymath-project  

### Course

11. [Maynard Ch.2]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/), [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/), [Euclid]({{ site.baseurl }}/contents/en/chapter05/05_02_Euclid_Infinite_Primes/). Pack: `research/video-research/Twin_Prime_Conjecture/`.

---

## Further directions

- Seminar brief: twins vs Euclid; Zhang→Maynard→$$H=246$$; gap $$2$$ open / parity barrier.  
- Studio: count twins vs Hardy–Littlewood integral—evidence, not proof.  
- Read the [Maynard Fields essay]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/) for multidimensional weights.

## Video tham khảo

- **xem trước** — [Gaps between Primes - Numberphile](https://www.youtube.com/watch?v=vkMXdShDdtY) — Numberphile, English. Watch first. “Gaps between Primes - Numberphile” orients the lesson’s aim: State the twin prime conjecture and give several twin prime pairs.
- [Twin Prime Conjecture - Numberphile](https://www.youtube.com/watch?v=QKHKD8bRAro) — Numberphile, English. A second pass once the main claim is in view: State the twin prime conjecture and give several twin prime pairs.
- [Small Gaps Between Primes - James Maynard](https://www.youtube.com/watch?v=E-W47F9upkU) — princetonmathematics, English. Further depth after the first two, still tied to this lesson: State the twin prime conjecture and give several twin prime pairs.
