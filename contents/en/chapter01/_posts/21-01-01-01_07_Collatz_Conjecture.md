---
layout: post
title: "The Collatz Conjecture"
chapter: '01'
order: 7
owner: Nguyen Le Linh
lang: en
categories:
- chapter01
lesson_type: required
---

The **Collatz conjecture** (also called the $$3x+1$$ problem, the Syracuse problem, or Hasse’s algorithm) is elementary enough that a middle-school student can play with it for an afternoon, and stubborn enough that no proof is known after nearly a century of attention. Paul Erdős is often quoted as saying that mathematics may not be ready for such problems; Jeffrey Lagarias, who has surveyed the subject for decades, has called it extraordinarily difficult despite its simple appearance. That tension—**simple statement, deep resistance**—is exactly why Collatz belongs in a course on great problems.

This page is the **Chapter 1 problem map**: rule, orbits, stopping times, verification culture, heuristics, partial theorems, and a clear handoff to the Chapter 7 exploration studio. It is not a claim that the conjecture is nearly solved, and it is not an invitation to “prove Collatz for the portfolio.” Treat it as a carefully chosen object for disciplined experimental mathematics.

**Path through this essay:** the map $$T$$ → the conjecture and the cycle $$4\to 2\to 1$$ → orbits and stopping times → verification as evidence → heuristics and partial results → cycles and hardness → course studio link → confusions and exercises.

---

## Learning objectives

After this lecture you should be able to:

- State the Collatz map $$T$$ and the conjecture that every positive integer eventually reaches the cycle $$4\to 2\to 1$$.
- Compute **orbits**, **stopping time**, and **total stopping time** for small seeds, and explain what those quantities measure.
- Explain why massive computer verification is **evidence**, not a proof of a statement about all positive integers.
- Describe at slogan level at least one **heuristic** (expected decrease under random parity) and one type of **partial result** (density of integers that reach 1; constraints on cycles).
- State **Tao’s 2019 almost-all theorem** in slogan form and explain why it is **not** a full proof of Collatz.
- Distinguish the standard map $$T$$ from an **accelerated / Syracuse** formulation when comparing sources.
- Use Collatz as the default **A5 exploration** object without claiming a solution.
- Articulate **LO6** in this setting: a problem that is easy to state need not be easy to settle.

**Prerequisites.** Positive integers, even/odd parity, and comfort iterating a simple rule by hand or with a short program. No dynamical systems course is required.

**Seminar links.** LO1, LO5, LO6; [Exploration studio — Iterate]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/); [Riemann]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) (verification vs proof); [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/) (iteration culture, different mathematics).

---

## 1. The rule and the conjecture

For a positive integer $$n$$, define

$$
T(n) =
\begin{cases}
n/2 & \text{if } n \text{ is even},\\
3n+1 & \text{if } n \text{ is odd}.
\end{cases}
$$

Start at any seed $$n_0$$ and iterate:

$$
n_0,\quad n_1 = T(n_0),\quad n_2 = T(n_1),\quad \ldots
$$

The sequence is completely deterministic: the next term depends only on the parity of the current term. There is no randomness in the rule—only in the heuristics people invent to model typical behavior.

**Worked orbit.** Begin at $$6$$:

$$
6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1 \to 4 \to 2 \to 1 \to \cdots
$$

Once the sequence hits $$4$$, it is trapped in the three-cycle

$$
4 \to 2 \to 1 \to 4 \to \cdots
$$

(equivalently, once it hits $$1$$, the next steps are $$1\to 4\to 2\to 1$$ under the same map). Another famous seed is $$27$$, which climbs into the hundreds before eventually descending to $$1$$—a reminder that “eventual descent” need not look monotonic.

**Collatz conjecture.** Every positive integer eventually reaches the cycle $$4\to 2\to 1$$.

Equivalent popular formulations say every positive integer eventually reaches $$1$$, or that the only cycle in the positive integers under $$T$$ is the trivial one (with the usual caveats about accelerated maps that jump over even steps). The conjecture is open: no proof, no counterexample.

**Many names, one problem.** You will also see $$3x+1$$ problem, Syracuse problem, Ulam’s problem, Kakutani’s problem, Thwaites conjecture, or Hasse’s algorithm. In video lectures and surveys these labels are usually interchangeable for the *classical positive-integer* story—always check the exact map (standard vs accelerated).

**Orbit minimum notation (research lectures).** Writing

$$
\operatorname{Col}_{\min}(N)=\inf_{k\ge 0} T^{k}(N)
$$

makes the conjecture $$\operatorname{Col}_{\min}(N)=1$$ for every positive integer $$N$$. This is the language of Tao’s public talks and arXiv notes.

---

## 2. Orbits, stopping time, and total stopping time

Fix a seed $$n$$. Its **orbit** (or trajectory) is the infinite sequence $$n, T(n), T^2(n), \ldots$$. Studying Collatz is largely about understanding these orbits: how high they climb, how long they wander, whether they ever enter a cycle, and whether they diverge to infinity.

Two classical bookkeeping quantities appear throughout the literature:

- The **stopping time** of $$n$$ is the first step at which the iterate drops **below** the starting value $$n$$. Roughly: how long until the sequence has made “progress” relative to its birth height.
- The **total stopping time** of $$n$$ is the first step at which the iterate reaches $$1$$ (or, equivalently in the positive conjecture, enters the $$4$$–$$2$$–$$1$$ cycle). This measures the full length of the journey to the known attractor.

For small seeds these are easy to compute by hand; for large seeds they become a natural computational experiment. Plots of total stopping time against $$n$$ look irregular—spiky, not smooth—which is part of the folklore of the problem: local arithmetic quirks create long excursions even when nearby seeds settle quickly.

**Why the language matters.** “The sequence eventually hits 1” is a qualitative claim. Stopping times turn that claim into quantitative data you can plot, compare, and hypothesize about. In the Chapter 7 studio, good explorations almost always begin by defining a measurable statistic (max height, total stopping time, residue class of the odd terms, …) rather than staring at raw lists of numbers.

---

## 3. Why people care

Several complementary reasons keep Collatz alive in popular mathematics and research surveys alike.

**Accessibility.** Anyone who can divide by two and multiply by three can generate data. That makes the problem ideal for seminars: low barrier, high ceiling.

**Depth without jargon.** Unlike the Birch–Swinnerton-Dyer conjecture or high-dimensional geometric analysis, Collatz does not require a semester of prerequisites to *state*. Yet the best partial results use nontrivial ideas from ergodic theory, probability, and careful arithmetic combinatorics. Difficulty here is not “obscure language”; it is resistance of an elementary dynamical system on the integers.

**Culture of open problems.** Collatz is a clean exhibit for **LO6**: sophistication of statement and difficulty of resolution need not track each other. A one-line recurrence can outlast generations of technique.

**Experimental mathematics.** Residue statistics, inverse trees (numbers that map to a given value), height records, and stopping-time histograms are legitimate mathematical objects of study even while the full conjecture remains open. The problem rewards careful logging and honest negative results as much as flashy plots.

---

## 4. Verification is not proof

The conjecture has been checked for all starting values up to **astronomically large bounds**. Computational projects have pushed past $$2^{68}$$, $$2^{70}$$, $$2^{71}$$, and related limits; the record moves, so when you write an A3 brief or A5 portfolio, cite a current survey or verification paper rather than memorizing a single exponent from this page. No counterexample is known in the positive integers.

That is impressive evidence. It is not a theorem about all positive integers. The logical gap is the same one you met with zeros of the zeta function on the critical line:

- A counterexample could, in principle, hide beyond the checked range.
- A **divergent trajectory** (orbit unbounded and never cycling) would refute the conjecture.
- A **nontrivial cycle** (a cycle other than $$4\to 2\to 1$$ in the positives) would also refute it.
- Checking finitely many seeds never exhausts an infinite statement.

So the correct seminar sentence is: *Collatz has been verified to a huge finite bound; the universal claim remains open.* Same moral as RH numerics: **strong evidence, not a proof**.

---

## 5. Heuristics: expected decrease

If the conjecture is true, something about the map must “pull most orbits downward on average,” even though a single odd step multiplies by three and adds one. Heuristic models make that intuition quantitative.

A standard slogan: when you apply $$3n+1$$ to an odd integer, the result is even, so at least one division by $$2$$ follows; often more than one. If one models the number of trailing factors of $$2$$ after an odd step as roughly geometric (a common random model of parity), the expected logarithmic change per “odd-centered” step is negative. In probabilistic models of this type, almost every trajectory is predicted to reach small values—hence the widespread belief that the conjecture is true.

**Crucial caveats.**

- The map is **deterministic**. Calling the statistics “random” is a modeling choice, not a claim that $$T$$ flips coins.
- Heuristics that work for “almost all” integers do not automatically control **all** integers. Exceptional sparse sets could still misbehave.
- Different formulations (accelerated Collatz maps that collapse runs of halvings) change constants in the heuristic without removing the need for a real proof.

Use heuristics to guide experiments and to explain why mathematicians are not surprised by the absence of small counterexamples. Do not confuse a probabilistic prediction with a demonstration.

A recurring critical constant in density theory is

$$
\frac{\log 3}{\log 4}\approx 0.7925.
$$

It appears in almost-all descent theorems of Korec type (orbits that drop below a power $$N^\theta$$ for almost all $$N$$ when $$\theta$$ is larger than this threshold) and in heuristics that balance multiplication by $$3$$ against typical division by powers of $$2$$. You do not need to prove the constant in this course—you should recognize it when a survey or Tao lecture writes it on a slide.

---

## 6. Accelerated maps and the Syracuse formulation

Popular videos usually use the full map $$T$$ above. Research talks (Tao, Lagarias surveys, Chamberland) often pass to an **accelerated** map on **odd** integers so that each step does exactly one multiplication by $$3$$.

Define the **Syracuse map** on odd positive integers by

$$
\operatorname{Syr}(N)=\frac{3N+1}{2^{a(N)}},
$$

where $$2^{a(N)}$$ is the highest power of $$2$$ dividing $$3N+1$$ (so $$\operatorname{Syr}(N)$$ is again odd). Iterating $$\operatorname{Syr}$$ tracks the odd terms of a Collatz orbit after all forced halvings.

**Why research prefers it.** Modular statistics mod powers of $$3$$ become cleaner; probabilistic models of the 2-valuation $$a(N)$$ (often geometric with mean $$2$$ in random models) sit at the center of modern almost-all proofs. **Seminar warning:** numerical orbits printed under $$T$$ and under $$\operatorname{Syr}$$ look different—compare sources only after fixing the convention.

Another common accelerated form collapses “odd step + at least one halving” into a single formula used in older papers; again, match the author’s definition before counting steps.

---

## 7. Partial mathematics (without claiming completeness)

The serious literature is large; Lagarias’s surveys are the standard entry point ([arXiv:2111.02635](https://arxiv.org/abs/2111.02635) and classical Monthly-style surveys). Without pretending to survey everything, here are types of results you should recognize by name and purpose—including the modern almost-all line featured in Tao’s lectures.

### 7.1 Density and almost-all descent (timeline slogans)

| Result family | Slogan (undergrad-accessible) | Density type |
|---------------|-------------------------------|--------------|
| Krasikov–Lagarias type | Many integers $$N\le x$$ already satisfy $$\operatorname{Col}_{\min}(N)=1$$ (quantitative lower bounds grow with $$x$$) | Counting up to $$x$$ |
| Terras | Almost all $$N$$ eventually drop **below** $$N$$ | Natural density |
| Allouche / Korec | Almost all $$N$$ satisfy $$\operatorname{Col}_{\min}(N)<N^\theta$$ for suitable $$\theta$$; Korec reaches down near $$\theta>\log 3/\log 4$$ | Natural density |
| **Tao (2019)** | Almost all $$N$$ satisfy $$\operatorname{Col}_{\min}(N)<f(N)$$ for **any** $$f\to\infty$$, no matter how slowly | **Logarithmic density** |

**Formal statement of Tao’s theorem (blog/arXiv).** Let $$f$$ be any function from positive integers to reals with $$f(N)\to+\infty$$ as $$N\to\infty$$. Then

$$
\operatorname{Col}_{\min}(N) < f(N)
$$

for almost all positive integers $$N$$ in the sense of **logarithmic density**. In particular, for almost all $$N$$ one can force the orbit minimum below iterated logarithms such as $$\log\log\log\log N$$.

**Intuition vs formality.**

- *Intuition (from Tao’s exposition):* classical almost-all theorems give **local-in-time** control—orbits of typical seeds descend for a window of length about $$c\log N$$. Reaching *nearly bounded* values needs something closer to **global** control. Naively concatenating “most points drop a bit” fails if the distribution of arrival values concentrates on a bad exceptional set. An approximately **invariant** probabilistic model for accelerated (Syracuse) dynamics is used to repair that concatenation.
- *Formal status:* a published partial theorem. **Not** the Collatz conjecture.

**What Tao 2019 is not (repeat until automatic).**

- Not: every $$N$$ reaches $$1$$.  
- Not: a pure computer verification result.  
- Not: the same as “natural density” (log density is a different averaging).  
- Not: a solution announced in a viral video.

Quanta Magazine’s popular account is useful orientation; the authoritative statements are the [arXiv paper](https://arxiv.org/abs/1909.03562) and [Tao’s blog post](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/).

### 7.2 Proof architecture at slogan level (Tao 2019)

For seminar literacy only (not a homework to reconstruct):

1. Pass to the **Syracuse** map on odds.  
2. Study **3-adic** irregularity of iterates (odd terms avoid multiples of $$3$$; residue frequencies are uneven).  
3. Model modular distributions by **Syracuse random variables** on $$\mathbb{Z}/3^n\mathbb{Z}$$.  
4. Prove **stabilization** of those laws as $$n$$ grows.  
5. Use that structure so local almost-sure descent can be **iterated** toward almost-global almost-boundedness.  
6. Technical tools in the paper include Fourier/characteristic-function estimates and a **renewal process** argument.

LO essays should state the *conclusion* of Theorem 2 and the open full conjecture—not pretend to reproduce renewal estimates.

### 7.3 Cycles, generalizations, computation

**Constraints on cycles.** Researchers study what a nontrivial periodic orbit would have to look like—constraints on length, modular conditions, and growth. In the positive integers under the standard map, the **only known cycle** is $$4\to 2\to 1$$. (Other cycles appear if one allows negative integers or different maps; mention those carefully and do not confuse them with a counterexample in the classical positive conjecture.)

**Generalizations.** Maps of the form $$mx+1$$, other piecewise-defined integer dynamics, and Collatz-like problems over other rings generate a broader experimental and theoretical landscape. Some **generalized** Collatz-type problems connect to undecidability phenomena in computability theory; that does **not** mean the classical conjecture has been proved undecidable. (Popular videos sometimes blur this; see the Easy Theory corrective linked in References.)

**Computational structure theory.** Efficient verification is itself mathematical engineering: tree pruning, modular filters, and careful use of residual classes to avoid rechecking trajectories that merge into already-verified paths.

None of these partial results is a full proof. Together they show that Collatz is not a barren curiosity: it sits inside active research on integer dynamics—exactly the culture of Tao’s “Notorious Collatz” lectures and Lagarias’s surveys.

---

## 8. Hardness in plain language

Why is an elementary recurrence so hard?

The map **mixes** multiplication (the $$3n+1$$ branch) with division by powers of two. Multiplication by three and division by two do not share a simple common invariant that decreases at every step for every seed. Trajectories can climb for a long time before falling; total stopping times fluctuate irregularly; and the discrete nature of the problem blocks many tools from smooth dynamical systems (where Lyapunov functions and continuous phase portraits are available).

Erdős’s remark—that mathematics may not be ready—captures a cultural judgment: existing toolkits do not obviously apply. Lagarias’s assessments emphasize the same point from inside the literature: enormous effort has produced structure and partial theorems, not a resolution. Hardness here means **resistance of the exact universal statement**, not absence of interesting mathematics around the problem.

---

## 9. Course role: problem page vs exploration studio

| This page (Ch.1) | Studio (Ch.7) |
|------------------|---------------|
| Statement, culture, status | Experiments, logs, portfolio |
| LO1 explanation; LO6 “simple ≠ easy” | LO5 creation and disciplined inquiry |
| No coding required | Coding, plotting, and hypothesis logs encouraged |

The default A5 object in this course is Collatz-style iteration (see [Explore Iteration]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/)). Do **not** treat A5 as “prove Collatz.” Treat it as:

1. choosing a precise statistic or question,
2. generating data with a reproducible method,
3. stating a **falsifiable** hypothesis,
4. reporting what the data do and do not support.

That is how open problems teach scientific maturity.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Checked to $$10^{20}$$ (or $$2^{70}$$), so true.” | Evidence for that finite range only; the universal claim is open. |
| “The sequence is random.” | Fully deterministic; statistics of orbits can look irregular. |
| “$$3n+1$$ always grows, so orbits explode.” | Combined with halvings, orbits often descend on average—make heuristics precise if you use them. |
| “A viral ‘proof’ or Lean ‘disproof’ online settled it.” | Extraordinary claims need community verification; the conjecture remains open in standard mathematics (watch for bugs, incomplete cases, and jokes). |
| “Only the cycle $$4$$–$$2$$–$$1$$ exists in every integer system.” | State the domain carefully; negatives and variant maps can have other cycles. |
| “Simple statement means it should be easy.” | **LO6:** accessibility of statement is not difficulty of proof. |
| “Tao solved Collatz / almost all means every.” | Tao 2019 is almost-all / almost-bounded (log density), **not** the full conjecture. |
| “Syracuse map is a different conjecture.” | Usually an accelerated form of the *same* positive Collatz story—match definitions before comparing numbers. |
| “Collatz is known undecidable.” | Some **generalizations** relate to undecidability; the classical conjecture’s status is open and subtle—do not overclaim from a popular clip. |

---

## Exercises

1. Compute the orbit of $$27$$ until $$1$$. Count the number of steps (total stopping time) and record the maximum value attained.
2. Define **stopping time** and **total stopping time** in one sentence each, and compute both for $$n=6$$ and $$n=7$$.
3. Give two independent reasons that finite verification cannot prove Collatz for all positive integers.
4. **LO1 (≤250 words):** state the Collatz conjecture, explain why it is hard in plain language, and name one surrounding idea (heuristics, density results, or cycle constraints).
5. **LO6 (short paragraph):** contrast Collatz with a problem that is hard primarily because of specialized language (e.g. BSD). What pedagogical role does each play in Chapter 1?
6. Draft one **A5 hypothesis** you could falsify with a plot or table (example: “for $$n\le N$$, total stopping time is at most $$c\log n$$”—pick something you can actually test and revise).
7. Stretch: read an abstract (or introduction) of a Lagarias survey on the $$3x+1$$ problem and list three subtopics that go beyond naive iteration.
8. **Tao hygiene (≤200 words):** Write two sentences of the form “Tao proved …” and “Tao did **not** prove …,” naming logarithmic density and $$\operatorname{Col}_{\min}$$.
9. **Map variants:** Compute the first four *odd* terms of the orbit of $$7$$ under $$T$$, then write $$\operatorname{Syr}(7)$$ using the definition in §6. Explain in one sentence why step counts differ.

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for a proof (none is known). Full ranking and Mode B notes: `research/video-research/collatz/`.

**Recommended order**

1. **Orientation** — Veritasium, *The Simplest Math Problem No One Can Solve – Collatz* (~22 min): [YouTube](https://www.youtube.com/watch?v=094y1Z2wpJg).  
2. **Culture** — Numberphile, *UNCRACKABLE? The Collatz Conjecture* (Eisenbud): [YouTube](https://www.youtube.com/watch?v=5mFpVDpKX70).  
3. **Survey** — Marc Chamberland, *The 3x+1 Problem: Status and Recent Work* (Part 1): [YouTube](https://www.youtube.com/watch?v=t1I9uHF9X5Y).  
4. **Core research lecture** — Terence Tao, *The Notorious Collatz conjecture* (Guy lecture): [mathtube](https://mathtube.org/lecture/video/notorious-collatz-conjecture) · [YouTube](https://www.youtube.com/watch?v=X2p5eMWyaFs) · [slides PDF](https://terrytao.files.wordpress.com/2020/02/collatz.pdf).  
5. **Frontier (optional)** — Tao @ IAS, *Almost all Collatz Orbits Attain Almost Bounded Values* (~61 min): [YouTube](https://www.youtube.com/watch?v=k-dtx8s2ehM). Pairs with [arXiv:1909.03562](https://arxiv.org/abs/1909.03562).  
6. **Hygiene (optional)** — Easy Theory on a Veritasium wording issue: [YouTube](https://www.youtube.com/watch?v=Lr6qc_9M0Ks).

**After videos, remember:** Tao (2019) is a major **almost-all / almost-bounded** theorem (logarithmic density), **not** a solution of the full conjecture. Status remains **open** as of 2026.

Caption transcripts (for navigation, not as lesson text) and sample frames live in the research pack:

- Transcripts / units: `research/video-research/collatz/transcripts/`
- Status table: `research/video-research/collatz/TRANSCRIPT_STATUS.md`
- Sample stills (Numberphile / Tipping Point):  

![Collatz orbit board (Numberphile sample frame)]({{ site.baseurl }}/img/video_research/collatz/5mFpVDpKX70_frame01.jpg)

*Figure. Still from Numberphile *UNCRACKABLE?* (Eisenbud interview), sample frame ~1 min — pedagogical illustration only.*

![Collatz color visualization sample]({{ site.baseurl }}/img/video_research/collatz/LqKpkdRRLZw_frame01.jpg)

*Figure. Still from Numberphile *Collatz in Color* — visual pattern culture, not a proof.*

---

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/collatz/references.md`.

### Research papers and author writing

1. J. C. Lagarias — *The 3x+1 Problem: An Overview*: [arXiv:2111.02635](https://arxiv.org/abs/2111.02635) · [PDF](https://arxiv.org/pdf/2111.02635).  
2. J. C. Lagarias — classical survey mirror: [SFU organics](http://www.cecm.sfu.ca/organics/papers/lagarias/); course PDF copy of *3x+1 and its generalizations*: [Williams](https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa15/addcomments/Lagarias_3x+1AndItsGeneralizations.pdf).  
3. T. Tao — *Almost all Collatz orbits attain almost bounded values*: [arXiv:1909.03562](https://arxiv.org/abs/1909.03562) · [PDF](https://arxiv.org/pdf/1909.03562) · [blog](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/).  
4. T. Tao — earlier Collatz notes (2011): [blog](https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/).  
5. M. Chamberland — 2003 update survey PDF: [Grinnell](http://www.math.grinnell.edu/~chamberl/papers/3x_survey_eng.pdf).  
6. Computational verification literature (e.g. Barina and successors)—check current bounds when citing.

### Videos (primary path)

7. Veritasium — Collatz orientation: https://www.youtube.com/watch?v=094y1Z2wpJg  
8. Numberphile — UNCRACKABLE? (Eisenbud): https://www.youtube.com/watch?v=5mFpVDpKX70 · page: https://www.numberphile.com/videos/uncrackable-the-collatz-conjecture  
9. Chamberland — *3x+1* status Part 1: https://www.youtube.com/watch?v=t1I9uHF9X5Y  
10. Tao — *Notorious Collatz* (mathtube): https://mathtube.org/lecture/video/notorious-collatz-conjecture · YouTube: https://www.youtube.com/watch?v=X2p5eMWyaFs · slides: https://terrytao.files.wordpress.com/2020/02/collatz.pdf · listing: https://www.rism.it/rism-channel/2021/riemann-prize-week/the-notorious-collatz-conjecture-terence-tao  
11. Tao @ IAS — almost-all orbits: https://www.youtube.com/watch?v=k-dtx8s2ehM  
12. Easy Theory — Veritasium wording corrective: https://www.youtube.com/watch?v=Lr6qc_9M0Ks  

### Videos (secondary finds)

13. Tipping Point Math — *Simplest Impossible Problem*: https://www.youtube.com/watch?v=m4CjXk_b8zo  
14. Numberphile — Collatz in Color: https://www.youtube.com/watch?v=LqKpkdRRLZw · extra: https://www.youtube.com/watch?v=O2_h3z1YgEU · realtime color: https://youtu.be/wH141HLD57o  
15. Lex Clips — Tao on Collatz: https://www.youtube.com/watch?v=vT4VJyXWHlo  

### Web expositions and news

16. Wikipedia — Collatz conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture  
17. Quanta Magazine (Tao 2019): https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/  
18. Chamberland hub: https://chamberland.math.grinnell.edu/3x.html  
19. University of Basel news (Tao lecture): https://dmi.unibas.ch/en/news/details/lecture-in-basel-terence-tao-and-the-notorious-collatz-conjecture/  
20. Stanford event note: https://mathematics.stanford.edu/events/kiddie-colloquium/almost-almost-collatz  
21. Pitt Mathematics note: https://www.mathematics.pitt.edu/content/note-collatz-conjecture  
22. Study.com history lesson (low research trust): https://study.com/academy/lesson/history-of-the-collatz-conjecture.html  

### Course

23. [Collatz / iteration studio]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/), [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/), [Riemann]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/). Research pack: `research/video-research/collatz/` (especially `references.md`).

---

## Further directions

Default **A5** topic for the seminar: build a small computational laboratory around orbits and stopping times, keep a research log, and write up what remains open. Optional alternatives in the same studio family include logistic-map iteration as a chaos-lite comparison (different mathematics, similar discipline of experiment). For a solved-but-deep contrast after this open problem, visit the [Four Color Theorem]({{ site.baseurl }}/contents/en/chapter01/01_09_Four_Color_Theorem/).
