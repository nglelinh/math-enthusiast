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

Among the primes—$$2,3,5,7,11,13,17,19,23,29,31,\ldots$$—some come in tight pairs differing by two: $$(3,5)$$, $$(5,7)$$, $$(11,13)$$, $$(17,19)$$, $$(29,31)$$, $$(101,103)$$, $$(107,109)$$, …. These are **twin primes**. The **twin prime conjecture** asserts that there are **infinitely many** such pairs: no matter how far you travel along the number line, another couple $$p$$ and $$p+2$$, both prime, waits further on.

Euclid proved infinitely many primes more than two thousand years ago. Infinitely many *twins* remains open. The conjecture is not a Clay Millennium Prize Problem, but it is one of the most famous questions in number theory—and the 2010s delivered a spectacular partial victory: **bounded gaps** between primes infinitely often. Yitang Zhang, James Maynard, Terence Tao, and the Polymath projects showed that some even gap no larger than a fixed finite $$H$$ occurs infinitely often. Optimized bounds give $$H=246$$ in the standard unconditional narrative. Gap exactly $$2$$—true twins—still resists.

This essay states the conjecture, explains Hardy–Littlewood heuristics, sketches why sieves struggle (parity), narrates the bounded-gaps revolution, places twins among Polignac and prime tuples, and links to RH fine-scale thinking and Maynard’s Fields Medal story.

---

## Learning objectives

After this lecture you should be able to:

- State the **twin prime conjecture** and give several twin prime pairs.
- Contrast **infinitude of primes** (Euclid, known) with **infinitude of twins** (open).
- Explain the **Hardy–Littlewood** heuristic and the twin prime constant at slogan level.
- State **bounded gaps**: there exists $$H$$ such that $$p_{n+1}-p_n \le H$$ for infinitely many $$n$$, and name **Zhang (2013)**, **Maynard**, and **Polymath** in the narrative toward $$H=246$$.
- Explain why gap $$2$$ specifically remains out of reach of current sieve methods (**parity barrier** slogan).
- Connect to [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) (fine-scale prime patterns) and [Maynard]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/) (Fields Medal 2022).

**Prerequisites.** Primes; basic modular arithmetic (even gaps, residue classes). Comfort with the idea that primes become rarer—density about $$1/\log x$$—is enough for the heuristics.

**Seminar links.** Course outcome **LO1**. [Maynard Fields essay]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/); [Euclid’s infinitude of primes]({{ site.baseurl }}/contents/en/chapter05/05_02_Euclid_Infinite_Primes/); [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) for fine-scale distribution culture.

---

## 1. Statement and first examples

**Twin prime conjecture.** There are infinitely many primes $$p$$ such that $$p+2$$ is also prime.

Equivalently: the equation $$p'-p=2$$ has infinitely many solutions in prime pairs $$(p,p')$$.

Except for $$(2,3)$$—sometimes discussed separately because $$2$$ is the only even prime—all twin pairs are of the form $$(p,p+2)$$ with both odd. The pair $$(2,4)$$ is *not* twins: $$4$$ is composite. The pair $$(7,9)$$ fails because $$9=3^2$$. Twins must both be prime.

A short list to internalize the pattern:

$$
(3,5),\ (5,7),\ (11,13),\ (17,19),\ (29,31),\ (41,43),\ (59,61),\ (71,73).
$$

Computations find twins at enormous heights; they become rarer, consistent with heuristics below. Rarity is not finiteness—the conjecture is about the infinite.

---

## 2. Euclid’s infinitude versus twins

Euclid’s theorem: there are infinitely many primes. One classical idea: given finitely many primes $$p_1,\ldots,p_k$$, form $$N = p_1\cdots p_k + 1$$; then $$N$$ has a prime factor outside the list. That argument produces *some* new prime; it does not produce a prime $$p$$ such that $$p+2$$ is also prime.

There is no known simple variant that forces twins. Adjoining “$$+2$$” breaks the clean factorization argument: $$N$$ and $$N+2$$ can share small factors in ways that wreck naive constructions. The twin prime conjecture is elementary to *state* and resistant to *Euclid-style* proof—a common signature of deep additive questions about primes.

---

## 3. Heuristics: Hardy–Littlewood and the twin prime constant

Primes near $$x$$ have density about $$1/\log x$$ (prime number theorem). If primality of $$n$$ and of $$n+2$$ were independent events with those probabilities, the “probability” that both are prime would be on the order of $$1/(\log n)^2$$. The series

$$
\sum_{n=3}^{\infty} \frac{1}{(\log n)^2}
$$

diverges (compare to the integral $$\int_3^\infty (\log x)^{-2}\,dx$$, which grows like $$x/(\log x)^2$$ after integration by parts). Divergent expected count suggests infinitely many twins.

Independence is false—$$n$$ and $$n+2$$ are linked by modular constraints—but the correction is a constant factor, not a change from divergence to convergence. **Hardy–Littlewood** conjectured a precise asymptotic: the number of twin primes up to $$X$$ should behave like

$$
\sim 2C_2 \int_2^{X} \frac{dt}{(\log t)^2},
$$

where $$C_2$$ is the **twin prime constant**

$$
C_2 = \prod_{p\ge 3}\Bigl(1 - \frac{1}{(p-1)^2}\Bigr) \approx 0.66016\ldots.
$$

The product encodes, for each odd prime $$p$$, the local probability adjustment that neither of two numbers distance $$2$$ apart is divisible by $$p$$. Heuristics organize data beautifully: twins keep appearing at roughly the predicted rate. Heuristics are not proofs.

---

## 4. Why sieves struggle: almost primes and the parity barrier

**Sieve methods** (Eratosthenes, Brun, Selberg, combinatorial sieves, …) systematically remove numbers with small prime factors. They excel at detecting **almost primes**—integers with few prime factors. Brun famously showed that the sum of reciprocals of twin primes converges (the “twin prime constant” in a different sense: Brun’s constant), which is compatible with either finitely many or infinitely many twins, but shows twins are sparse enough for that series to converge.

Turning “almost prime twice” into “prime twice” hits structural limits. The **parity problem** (in sieve theory) is the slogan: classical sieves have difficulty distinguishing numbers with an even number of prime factors from those with an odd number, in settings where that distinction is exactly what separates primes from products of two primes.

A celebrated near-miss is **Chen’s theorem**: there are infinitely many primes $$p$$ such that $$p+2$$ is either prime or a product of two primes (a almost-twin). That is tantalizingly close to the twin prime conjecture—and still not the conjecture.

So the obstruction is not “nobody tried sieves.” The obstruction is that sieves, as currently understood, deliver *almost* the truth about twins.

---

## 5. Bounded gaps: Zhang, Maynard, Polymath

In 2013, **Yitang Zhang** proved that

$$
\liminf_{n\to\infty} (p_{n+1}-p_n) < 70{,}000{,}000.
$$

That is: among gaps between consecutive primes, some gap smaller than seventy million occurs **infinitely often**. The number was large but **finite**—the first theorem of its kind. Before Zhang, one did not know that liminf of consecutive gaps was finite; primes might have been forced farther and farther apart in the limit inferior sense.

The method built on **Goldston–Pintz–Yıldırım (GPY)** ideas about detecting primes in admissible tuples of linear forms, combined with deep distribution estimates for primes in arithmetic progressions in a delicate averaged form. Zhang’s breakthrough was a new way to obtain enough distribution without assuming the strongest conjectures.

Rapid improvements followed:

- **Polymath** projects (notably Polymath8) optimized Zhang’s approach, shrinking the admissible bound dramatically through community collaboration.
- **James Maynard** (and independently related ideas in Tao’s circle) introduced a more flexible **multidimensional sieve weighting**, allowing several linear forms to be weighted together more efficiently. Maynard’s framework often simplifies and strengthens gap results and extends to richer prime patterns.

After optimization, the best published unconditional bound of the form

$$
\liminf_{n\to\infty} (p_{n+1}-p_n) \le H
$$

stands at **$$H = 246$$** in the standard exposition of Maynard–Polymath (expository accounts sometimes quote nearby optimized numbers; $$246$$ is the seminar’s reference value). Under strong hypotheses such as the **Elliott–Halberstam conjecture** on primes in arithmetic progressions, the methods can push toward single-digit even gaps (e.g. $$6$$), but **reaching $$H=2$$**—infinitely many twin primes—appears to require ideas beyond the current sieve paradigm. The parity barrier is the usual slogan for why $$2$$ is special.

Maynard’s work on small gaps, large gaps, and related sieve innovations formed part of his **Fields Medal 2022** recognition. The [Maynard chapter essay]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/) develops that story in the Fields Medal sequence.

---

## 6. What is proved and what remains open

| Statement | Status |
|-----------|--------|
| Infinitely many primes | **Proved** (Euclid, …) |
| Infinitely many twin primes (gap $$2$$) | **Open** |
| Some bounded even gap infinitely often | **Proved** (Zhang / Maynard / Polymath) |
| $$\liminf (p_{n+1}-p_n) \le 246$$ | **Proved** (optimized unconditional bound) |
| Gap $$=2$$ infinitely often | **Open** |
| Chen’s theorem ($$p+2$$ prime or semiprime) | **Proved** |
| Hardy–Littlewood asymptotic for twins | **Open** (conjectural) |

Bounded gaps show that primes form tight clusters infinitely often. Twin primes demand the tightest even cluster. The distance from $$246$$ to $$2$$ is small as a ratio of integers and enormous as a mathematical barrier.

---

## 7. Polignac, prime tuples, and the wider landscape

**de Polignac’s conjecture** predicts that for every even positive integer $$2k$$, there are infinitely many prime pairs differing by $$2k$$. Twin primes are the case $$k=1$$. Bounded-gap theorems show that *at least one* even difference in a finite admissible set occurs infinitely often; they do not yet pin that difference to $$2$$.

**Prime tuples.** More generally, one studies patterns $$n+h_1,\ldots,n+h_m$$ simultaneously prime for admissible shifts $$h_i$$ (admissible means the shifts are not forced to cover all residues mod $$p$$ for some small $$p$$). Hardy–Littlewood prime tuples conjectures predict asymptotics for such constellations. Green–Tao’s theorem on arbitrarily long arithmetic progressions of primes is a different triumph—additive combinatorics rather than pure sieve gaps—but it lives in the same world of “primes contain rich patterns.”

**Connections to RH.** The [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) controls fine-scale regularity of prime counting errors. Twin primes are an additive configuration problem. Tools differ (explicit formulas vs sieves), but both ask how regularly primes can arrange themselves. Assuming RH or GRH helps many estimates in prime distribution; it does not, by itself, currently yield twins through a short argument you can put on a problem set.

---

## 8. Mathematics around the problem (toolkit map)

- **Sieve theory:** Selberg sieve, combinatorial sieves, GPY method, Maynard weights.
- **Primes in arithmetic progressions:** Bombieri–Vinogradov theorem (averaged Siegel–Walfisz / GRH strength on average); Elliott–Halberstam conjectures (stronger distribution).
- **Admissible tuples** and diameter optimization (how small can the width of a tuple be while remaining admissible?).
- **Computational number theory:** searching large twins; checking heuristics against data.

You do not need to master these tools to state the conjecture correctly—but naming them prevents the illusion that the problem is “just elementary trial division at large $$N$$.”

---

## From videos: the 2013–2014 cascade in slogans

Numberphile’s Zhang and Maynard videos, plus Maynard’s colloquium and the 2013 Quanta narrative, form a single LO1 story:

1. **GPY (Goldston–Pintz–Yıldırım)** built a sieve framework that *would* yield bounded gaps if primes were distributed slightly better in arithmetic progressions than Bombieri–Vinogradov guarantees.  
2. **Zhang (2013)** proved a weakened level-of-distribution result strong enough to get $$\liminf (p_{n+1}-p_n) \le 70{,}000{,}000$$ (later optimized by Polymath8a).  
3. **Maynard (and independently Tao)** refined multidimensional sieve weights so bounded gaps no longer required breaking the $$1/2$$-barrier in the same way; bounds fell dramatically; Polymath8b optimized toward **$$H=246$$** unconditionally.  
4. **Still open:** gap $$2$$ (twin primes), and the **parity barrier** remains the honest name for why sieves do not easily finish the last step.

**Status (as of 2026):** twin prime conjecture **open**; bounded gaps **proved**.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Zhang proved twin primes.” | He proved *some* bounded gap infinitely often, not gap $$2$$. |
| “Bounded gaps = twin primes.” | Bounded means $$\le H$$ for some fixed $$H$$; twins need $$H=2$$. |
| “There are only finitely many twins in tables.” | Tables are finite by definition; the conjecture is about infinity. |
| “Euclid’s proof adapts easily to twins.” | Euclid’s construction does not force a twin pair. |
| “Maynard alone discovered bounded gaps.” | Zhang’s 2013 breakthrough opened the door; Maynard, Tao, Polymath, and others advanced the story. |
| “$$H=246$$ is almost $$2$$, so twins are nearly done.” | Numerically close; methodologically still blocked by parity-type limitations. |

---

## Exercises

1. List five twin prime pairs with both members larger than $$100$$.
2. Why is $$(2,4)$$ not a twin prime pair? Why is $$(7,9)$$ not?
3. State Zhang’s theorem in your own words without the number seventy million (use “some finite bound”).
4. Explain in two sentences the difference between “$$\liminf (p_{n+1}-p_n) \le 246$$” and “infinitely many twin primes.”
5. **LO1 synthesis (≤300 words):** twin prime conjecture, why it is hard, surrounding math (heuristics; sieves; bounded gaps).
6. Compare twin primes with [Collatz]({{ site.baseurl }}/contents/en/chapter01/01_07_Collatz_Conjecture/): both elementary to state—how do their “surrounding toolkits” differ in one short paragraph?
7. One sentence: why does a divergent series of $$1/(\log n)^2$$ *suggest* infinitely many twins without proving it?
8. Stretch: read a Quanta-style account of Zhang 2013 (or the Maynard Fields citation) and list three mathematical ingredients named there (e.g. GPY, distribution in AP, sieve weights).

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

- **A3** brief: twins vs Euclid; Zhang→Maynard→$$H=246$$; gap $$2$$ open / parity barrier.  
- Studio: count twins vs Hardy–Littlewood integral—evidence, not proof.  
- Maynard Fields essay for multidimensional weights.
