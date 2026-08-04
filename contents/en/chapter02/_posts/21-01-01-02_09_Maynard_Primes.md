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

How small can the gap between consecutive primes be, infinitely often? Write $$p_n$$ for the $$n$$th prime. The prime number theorem suggests typical gaps near $$x$$ have size about $$\log x$$, which tends to infinity. Yet one can still ask whether

$$
\liminf_{n\to\infty}(p_{n+1}-p_n)
$$

is **finite**—that is, whether some fixed bound $$H$$ captures infinitely many consecutive prime pairs with gap at most $$H$$. **Yitang Zhang** shocked the mathematical world in 2013 by proving the liminf is finite. **James Maynard** independently developed a flexible **multidimensional sieve** framework that also yields bounded gaps, often simplifies and strengthens aspects of the argument, and extends to a wider landscape of prime patterns. He received the **Fields Medal 2022** for advances on the structure of the primes and related Diophantine problems—including large gaps and primes with restricted digits—not for a single tweetable number alone.

This essay narrates bounded gaps toward the standard unconditional story with

$$
\liminf_{n\to\infty}(p_{n+1}-p_n)\;\le\;246,
$$

stresses that this is **not** the twin prime conjecture, contrasts sieve methods with [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) arithmetic progressions, and links to the [twin prime lecture]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/). **LO6:** “Maynard almost proved twins” is false methodology dressed as numerical proximity.

---

## Learning objectives

After this lecture you should be able to:

- State a **bounded-gap** theorem: $$\liminf_n(p_{n+1}-p_n)\le H$$ for an explicit finite $$H$$.
- Place **Zhang (2013)**, **Maynard**, **Tao**, and **Polymath** in the community narrative.
- Explain why **sieves** (especially multidimensional GPY-type weights) detect prime patterns.
- Distinguish **bounded gaps** from the **twin prime conjecture** (gap exactly $$2$$ infinitely often).
- Describe Maynard’s contributions beyond small gaps: **large gaps**, **primes with restricted digits**.
- Contrast Maynard’s sieve viewpoint with **Green–Tao** additive combinatorics for long APs.
- Practice **LO6** on media claims about $$H=246$$ versus twins.

**Prerequisites.** Primes; modular arithmetic; the idea that primes have density about $$1/\log x$$. No prior sieve theory required—we define “detect almost primes” in prose.

**Seminar links.** **LO1** (open-adjacent breakthroughs), **LO6**. Core pair: [Twin Prime Conjecture]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/). Related: [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/), [Euclid infinitude]({{ site.baseurl }}/contents/en/chapter05/05_02_Euclid_Infinite_Primes/), [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) (fine-scale distribution culture), [prime predictability studio]({{ site.baseurl }}/contents/en/chapter07/07_04_Explore_Prime_Predictability/), [crypto number theory]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/).

---

## 1. Gaps between primes: typical, small, and large

Let $$p_1=2,p_2=3,p_3=5,\ldots$$. The gap $$g_n=p_{n+1}-p_n$$ satisfies, on average,

$$
\frac{1}{\pi(x)}\sum_{p_n\le x} g_n \;\sim\; \log x,
$$

so *typical* gaps grow. That does not forbid rare small gaps or rare huge gaps.

**Small gaps question.** Is $$\liminf g_n<\infty$$? Even stronger: is $$\liminf g_n=2$$ (twins)?

**Large gaps question.** How fast can $$g_n$$ grow along a subsequence? Classical constructions give gaps $$\gg \log p_n\log\log p_n/\log\log\log p_n$$ (order-of-magnitude form; constants and log-factors refined over decades).

Maynard’s Fields profile includes tools that speak to **both** ends of the gap spectrum, plus pattern theorems beyond consecutive primes.

---

## 2. Zhang’s breakthrough and the race to smaller $$H$$

In 2013, Zhang proved that there exists some finite $$H$$ (his paper gave $$H=70{,}000{,}000$$) such that

$$
p_{n+1}-p_n \le H
$$

for infinitely many $$n$$. Equivalently,

$$
\liminf_{n\to\infty}(p_{n+1}-p_n) < \infty
$$

with an explicit upper bound on the liminf. The proof used a variant of the **GPY method** (Goldston–Pintz–Yıldırım) together with a clever distribution estimate for primes in arithmetic progressions on average—weakening what one needs from Elliott–Halberstam-type hypotheses in a way that became available through deep exponential-sum / bilinear form technology.

Immediately, a worldwide **Polymath** project and independent work (including Maynard and Tao) drove the admissible $$H$$ down dramatically. In the now-standard unconditional narrative from Maynard’s multidimensional weights combined with Polymath optimizations, one reaches

$$
\liminf_{n\to\infty}(p_{n+1}-p_n)\;\le\;246.
$$

Under strong distribution conjectures (Elliott–Halberstam), the same circle of ideas can push toward much smaller $$H$$ (even $$H=6$$ in some conditional discussions of admissible tuples)—still **not** automatically $$H=2$$ without further breakthroughs past parity-type barriers.

**Credit culture.** Bounded gaps is a **community story**. Zhang opened the door with a finite $$H$$; Maynard’s sieve redesign is a central independent engine; Tao, Polymath, and many others optimized and extended. **LO6:** never write “Maynard alone discovered bounded gaps.”

---

## 3. Multidimensional sieve weights

Sieves detect numbers with few prime factors by weighting residue classes and using inclusion of local densities. The GPY method studies sums roughly of the shape

$$
\sum_n \Bigl(\sum_{i=1}^k \mathbf{1}_{\text{prime}}(n+h_i)\Bigr) w_n,
$$

where $$h_1,\ldots,h_k$$ is an **admissible** tuple of shifts (no fixed prime divides one of the linear forms for every $$n$$), and $$w_n\ge 0$$ are sieve weights concentrated on integers where the product $$\prod_i(n+h_i)$$ has small prime factors in a controlled way.

If the weighted count shows that the inner sum is often at least $$2$$, then at least two of the forms $$n+h_i$$ are prime infinitely often—hence a bounded gap of size at most $$\max h_i-\min h_i$$.

**Maynard’s insight** was to use **multidimensional weights**: optimize a weight depending on the vector of divisor information for several linear forms simultaneously, rather than a more rigid one-dimensional weight structure. This produces stronger detection of constellations and cleaner dependence on distribution theorems. The method is modular: once the weight optimization is set up, one can feed in different levels of prime-distribution input and read off which prime patterns follow.

Schematically:

$$
\text{admissible tuple }(h_i)
\;+\;
\text{multidimensional weights}
\;+\;
\text{distribution of primes in APs}
\;\Longrightarrow\;
\text{bounded gaps / patterns}.
$$

You do not need the full variational optimization of weights for seminar fluency; you need the **architecture**.

---

## 4. Not the twin prime conjecture

The **twin prime conjecture** asserts infinitely many primes $$p$$ with $$p+2$$ also prime: gap **exactly** $$2$$ infinitely often. Bounded gaps assert only that some even number $$H$$ in a fixed finite set occurs as a gap infinitely often (more precisely, that some gap $$\le H$$ occurs infinitely often for consecutive primes).

Implications:

$$
\text{twin primes}
\;\Longrightarrow\;
\liminf g_n = 2
\;\Longrightarrow\;
\liminf g_n \le 246,
$$

but none of the reverse arrows is known from current theorems. Numerical closeness of $$246$$ to $$2$$ is psychologically tempting and **methodologically misleading**. Sieve methods face **parity problems**: they struggle to distinguish numbers with an even number of prime factors from those with an odd number in ways that block pure “exactly two prime factors that are both size $$n$$” conclusions for twins.

**Chen’s theorem** (every large even integer is a sum of a prime and an almost-prime with at most two factors, in the classical Goldbach-adjacent form; and related almost-twin statements) illustrates how close sieves get to twins without reaching them. See the [twin prime lecture]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/) for Hardy–Littlewood heuristics and parity discussion.

---

## 5. Large gaps and primes with restricted digits

**Large gaps.** Maynard contributed to refined constructions and understandings of long stretches of composite numbers between primes—showing the sieve and covering ideas that force many consecutive integers to be composite can be pushed further. Large-gap theorems complement small-gap theorems: the primes are irregular in both directions.

**Restricted digits.** A celebrated result in this circle (Maynard and related work in the literature) constructs infinitely many primes that avoid certain digits in a given base—for example, primes whose decimal expansion misses a fixed digit, under appropriate hypotheses of the method. The surprise is that such a thin set still contains infinitely many primes. The proof uses a sophisticated combination of sieve ideas and harmonic analysis / circle-method-adjacent estimates; seminar takeaway: **modern sieve technology reaches far beyond consecutive gaps**.

These results explain why the Fields citation speaks of the **structure of prime numbers** broadly, not only of the number $$246$$.

---

## 6. Contrast with Green–Tao

| Feature | Green–Tao | Zhang–Maynard gaps |
|---------|-----------|---------------------|
| Pattern | Arbitrarily long APs of primes | Bounded consecutive gaps (and tuples) |
| Engine | Transference + pseudorandom majorants + Szemerédi | Multidimensional sieves + distribution in APs |
| Density issue | Primes have density zero vs Szemerédi | Need primes in many linear forms at once |
| Open twin-like end | Not about gap $$2$$ | Gap $$2$$ still open |
| Fields narrative | Tao 2006 (broad work; GT landmark) | Maynard 2022; Zhang not Fields for 2013 (timing/age rules aside—focus on math story) |

Both show that primes contain highly structured patterns. They answer **different pattern questions** with **different toolkits**. A strong seminar student can explain both without mixing the proofs.

---

## 7. Why it matters

Bounded gaps reopened a classical door: questions that felt eternally asymptotic-only became theorems with explicit constants. Maynard’s weights made the technology portable across pattern problems. Together with Green–Tao, the 2000s–2010s rewrote the public and professional sense of what is known about prime patterns.

**Accuracy notes.**

- Twin primes remain open.
- $$H=246$$ is a community-optimized figure in the standard account; always check current surveys for conditional improvements or refinements of related tuple results.
- Diophantine approximation components of Maynard’s profile are real but de-emphasized here in favor of the prime-structure narrative requested for this course map.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Bounded gaps = twin prime conjecture.” | Twins need gap $$2$$ infinitely often; bounded gaps allow a larger fixed $$H$$. |
| “Maynard alone discovered bounded gaps.” | Zhang’s 2013 breakthrough; Maynard, Tao, Polymath, and others developed the story. |
| “$$H=246$$ means twins are 99% done.” | Numerical gap to $$2$$ is small; parity/method barriers remain large. |
| “Green–Tao already gave bounded gaps.” | Green–Tao gives long APs, not a uniform bound on consecutive prime gaps. |
| “Sieves prove numbers are prime.” | Sieves often prove *almost-prime* or *at least two primes among forms*; full primality of a single form is harder. |
| “Large gaps contradict the prime number theorem.” | PNT controls averages; large gaps are rare spikes compatible with average $$\log x$$. |

---

## Exercises

1. Write the liminf statement for consecutive prime gaps and explain each symbol.
2. Why is “$$\liminf g_n\le 246$$” weaker than the twin prime conjecture? Two sentences.
3. What does a sieve “detect,” intuitively, when applied to several linear forms $$n+h_i$$?
4. In one table row each, contrast Green–Tao APs with Maynard-style gaps (pattern vs method).
5. Explain admissibility of a tuple $$(h_1,\ldots,h_k)$$ with a small example that fails (e.g. $$(0,1)$$) and one that works (e.g. $$(0,2)$$).
6. **LO6 (≤250 words):** Find a popular article on Zhang or Maynard. Flag any sentence that equates bounded gaps with twin primes; rewrite it correctly.
7. Stretch: if consecutive gaps are $$\le 246$$ infinitely often, must some *even* number $$\le 246$$ occur as a difference of primes infinitely often? Why is that still weaker than twins?
8. Seminar synthesis: connect this lecture to [Twin Primes Ch.01]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/) and [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) in a ≤300-word map of prime patterns (APs, bounded gaps, twins).

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
