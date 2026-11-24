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

Pick any positive whole number. If it is even, cut it in half. If it is odd, triple it and add one. Now repeat.

Try $$6$$: it glides straight down to $$1$$ in eight steps. Try $$27$$: suddenly it leaps like a hailstone caught in a thunderstorm, climbing all the way to $$9{,}232$$ before finally tumbling down to $$1$$ after $$111$$ steps. The **Collatz conjecture** (also known as the $$3x+1$$ problem or Syracuse problem) claims that **every** positive integer, no matter how monstrous, eventually lands in the tiny loop $$4 \to 2 \to 1$$.

A middle-schooler can test it on a napkin in thirty seconds. Yet after nearly a century of effort, nobody knows how to prove it. Paul Erdős famously warned that *“mathematics may not be ready for such problems,”* and Jeffrey Lagarias—its foremost chronicler—calls it extraordinarily resistant precisely because its one-line rule tangles multiplication by $$3$$ with division by $$2$$. That clash—**effortless to state, ferocious to prove**—is why Collatz is one of the finest mirrors of mathematical culture in this course.

---

## Learning objectives

After this lecture you should be able to:

- State the Collatz map $$T$$ and the conjecture that every positive integer eventually reaches the cycle $$4 \to 2 \to 1$$.
- Compute **orbits**, **stopping time**, **total stopping time**, and **Syracuse orbits** by hand for small seeds.
- Explain why massive computer verification (past $$2^{68}$$ and beyond) is **evidence**, not a proof for all positive integers.
- Derive the random-parity heuristic (average factor $$3/4 < 1$$) and contrast the positive domain with negative-integer cycles.
- State **Tao’s 2019 almost-all theorem** accurately (logarithmic density, almost bounded) and explain why it does **not** prove the full conjecture.
- Use Collatz as a disciplined experimental-mathematics sandbox in the Chapter 7 studio without overclaiming a proof.

**Prerequisites.** Positive integers, even/odd parity, basic probability (geometric distribution / expected value), and comfort iterating a simple rule by hand or in code.

**Course links.** Pair with [Exploration studio — Iterate]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/), [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) (verification vs. proof), and [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/) (iteration culture in continuous dynamics).

---

## Background Knowledge Map: What Fields Sit Behind Collatz?

Why does a two-branch arithmetic rule pull in some of the deepest machinery of modern mathematics? Collatz sits at the crossroads of three distinct fields.

### 1. Discrete Dynamical Systems and Ergodic Theory
In **dynamical systems**, you start at a point $$x_0$$ and repeatedly apply a rule $$x_{k+1} = T(x_k)$$ to study the long-term fate of orbits: do they settle into attractors, cycle periodically, wander chaotically, or escape to infinity? **Ergodic theory** studies statistical averages over typical orbits when individual trajectories are too erratic to track one by one.
- **Core questions:** What are all periodic cycles? Do almost all starting states converge to the same attractor?
- **Real-world reach:** Population dynamics, orbital mechanics, weather predictability, and Markov-chain Monte Carlo algorithms.

### 2. Number Theory and $$p$$-adic Analysis
Standard real numbers measure closeness by distance $$|a-b|$$. In **2-adic** and **3-adic** analysis, two integers are “close” if their difference is divisible by a high power of $$2$$ or $$3$$. Because $$3n+1$$ depends on parity (mod $$2$$) while multiplying by $$3$$ shifts 3-adic residues, Collatz is naturally a dynamical system on modular rings $$\mathbb{Z}/2^k\mathbb{Z}$$ and $$\mathbb{Z}/3^k\mathbb{Z}$$.
- **Core questions:** How do remainders modulo $$2^k$$ and $$3^k$$ redistribute under iteration? Could a hidden modular resonance sustain a giant nontrivial cycle?
- **Real-world reach:** Cryptographic hash functions, error-correcting codes, and fast arithmetic algorithms.

### 3. Computability Theory and Experimental Mathematics
In 1972, John Conway proved that a *generalized* family of Collatz-like piecewise-linear maps (FRACTRAN) can simulate arbitrary Turing machines—making their halting problem **undecidable**. Meanwhile, **experimental mathematics** uses modular sieves, inverse trees, and massive verification runs to discover statistical patterns and formulate falsifiable conjectures.
- **Core questions:** How far can modular pruning verify the conjecture? Where is the boundary between tractable arithmetic and algorithmic undecidability?
- **Real-world reach:** Program termination analysis in formal verification, automated theorem proving, and distributed scientific computing.

---

## 1. The rule and the conjecture

For a positive integer $$n$$, define the **Collatz map**

$$
T(n) =
\begin{cases}
n/2 & \text{if } n \text{ is even},\\
3n+1 & \text{if } n \text{ is odd}.
\end{cases}
$$

Start at any seed $$n_0$$ and iterate: $$n_0,\; n_1 = T(n_0),\; n_2 = T(n_1),\; \ldots$$ The rule is **100% deterministic**: there is no coin flipping anywhere in $$T$$—randomness appears only in the probabilistic *models* mathematicians invent to approximate typical orbits.

**Collatz conjecture.** Every positive integer eventually reaches the cycle $$4 \to 2 \to 1 \to 4 \to \cdots$$

Writing the orbit minimum as

$$
\operatorname{Col}_{\min}(N) = \inf_{k \ge 0} T^k(N),
$$

the conjecture states simply that $$\operatorname{Col}_{\min}(N) = 1$$ for every positive integer $$N$$. Notice that to refute the conjecture, there are exactly **two** possible ways it could fail:
1. A **divergent orbit** that climbs to infinity forever, or
2. A **nontrivial positive cycle** distinct from $$4 \to 2 \to 1$$.

**Many names, one problem.** You will also see the $$3x+1$$ problem, Syracuse problem, Ulam’s problem, Kakutani’s problem, Thwaites conjecture, or Hasse’s algorithm. Always check whether a source uses the standard map $$T$$ or an accelerated version before comparing step counts.

---

### Short video: An orbit that climbs before it falls

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/collatz-orbit-97_en.mp4"></video>
</div>

Follow the Collatz orbit of 97: it climbs to 9232 before falling back to 1 after 118 steps. Eventual descent need not look monotonic, and no one has proved it happens for every starting number.


### Try it yourself: Trace any Collatz orbit

<div class="mex-explainer" data-mex="collatz" data-lang="en"></div>


## 2. Orbits, stopping time, and total stopping time

Fix a seed $$n$$. Its **orbit** is the sequence $$n, T(n), T^2(n), \ldots$$ Two quantitative statistics turn the qualitative question “does it reach 1?” into measurable data:

- **Stopping time** $$\sigma(n)$$: the first step $$k \ge 1$$ where $$T^k(n) < n$$ (how long until the orbit drops strictly below its starting height).
- **Total stopping time** $$\sigma_\infty(n)$$: the first step $$k \ge 0$$ where $$T^k(n) = 1$$ (the full flight length to the attractor).

---

### Worked Example 1: Tracing $$n = 7$$ and $$n = 9$$ by Hand (Standard Map vs. Syracuse Map)

Let’s compute two neighboring odd seeds by hand and see how wildly their statistics differ—even though they sit just $$2$$ apart!

1. **Seed $$n = 7$$ under the standard map $$T$$:**
   $$
   7 \xrightarrow{1} 22 \xrightarrow{2} 11 \xrightarrow{3} 34 \xrightarrow{4} 17 \xrightarrow{5} 52 \xrightarrow{6} 26 \xrightarrow{7} 13 \xrightarrow{8} 40 \xrightarrow{9} 20 \xrightarrow{10} 10 \xrightarrow{11} \mathbf{5} \xrightarrow{12} 16 \xrightarrow{13} 8 \xrightarrow{14} 4 \xrightarrow{15} 2 \xrightarrow{16} \mathbf{1}.
   $$
   - **Peak height:** $$52$$ (more than $$7\times$$ its birth value).
   - **Stopping time $$\sigma(7) = 11$$** (first dips below $$7$$ at $$5$$).
   - **Total stopping time $$\sigma_\infty(7) = 16$$**.

2. **Seed $$n = 9$$ under the standard map $$T$$:**
   $$
   9 \xrightarrow{1} 28 \xrightarrow{2} 14 \xrightarrow{3} \mathbf{7} \xrightarrow{+16\text{ steps}} \mathbf{1}.
   $$
   - **Stopping time $$\sigma(9) = 3$$** (already drops below $$9$$ at step 3 when it hits $$7$$!).
   - **Total stopping time $$\sigma_\infty(9) = 3 + 16 = 19$$** (because it merges into the orbit of $$7$$, it inherits the same peak $$52$$!).

3. **Now compress $$n = 7$$ under the Syracuse map $$\operatorname{Syr}(N) = \dfrac{3N+1}{2^{a(N)}}$$** (stripping all powers of $$2$$ at once so every step lands on an odd number):
   - $$3(7)+1 = 22 = 2^1 \cdot 11 \implies \operatorname{Syr}(7) = 11$$ ($$a = 1$$)
   - $$3(11)+1 = 34 = 2^1 \cdot 17 \implies \operatorname{Syr}(11) = 17$$ ($$a = 1$$)
   - $$3(17)+1 = 52 = 2^2 \cdot 13 \implies \operatorname{Syr}(17) = 13$$ ($$a = 2$$)
   - $$3(13)+1 = 40 = 2^3 \cdot 5 \implies \operatorname{Syr}(13) = 5$$ ($$a = 3$$)
   - $$3(5)+1 = 16 = 2^4 \cdot 1 \implies \operatorname{Syr}(5) = 1$$ ($$a = 4$$)

   The 16-step standard orbit collapses into just **5 Syracuse steps**: $$7 \to 11 \to 17 \to 13 \to 5 \to 1$$!

**Lesson:** Notice how $$9$$ merges into $$7$$ after just 3 steps. Modern verification algorithms exploit this exact merging—once you prove every integer below $$N$$ reaches $$1$$, you only need to prove that $$N$$ has a *finite stopping time* (drops below $$N$$) to finish $$N$$!

---

## 3. Why people care

Four complementary qualities keep Collatz alive in both popular math and research:

- **Accessibility:** Anyone who can multiply by 3 and halve even numbers can explore it immediately.
- **Depth without jargon:** Unlike Birch–Swinnerton-Dyer or Yang–Mills, the barrier here is not heavy vocabulary—it is the genuine resistance of an elementary arithmetic dynamical system.
- **Culture of open problems:** Simplicity of statement and ease of proof do not track each other.
- **Experimental mathematics:** Stopping-time histograms, inverse trees, and modular sieves offer a clean training ground for disciplined computational inquiry.

---

## 4. Verification is not proof

Computational projects (including Barina’s distributed runs and successors) have verified the conjecture for every positive integer past **$$2^{68}$$, $$2^{70}$$, $$2^{71}$$** and beyond, finding zero counterexamples.

Impressive as that is, finite verification can never settle a universal claim over an infinite set. A counterexample—either a divergent trajectory or a colossal nontrivial cycle—could still lurk past the checked horizon. Just like verifying trillions of zeta zeros on the critical line, massive computation is **strong evidence, never a proof**.

---

## 5. Heuristics: expected decrease (and why domain matters!)

If the conjecture is true, why do orbits tend to shrink despite multiplying by $$3$$?

---

### Worked Example 2: The $$3/4$$ Drift Calculation — and a Surprise Cycle in the Negative Integers

Let’s do two quick hand calculations: one showing *why* orbits should drift downward, and one warning *why* heuristics can fail when you change the domain.

1. **The geometric drift calculation (Syracuse map):**
   When $$N$$ is odd, $$3N+1$$ is always even. Assuming its trailing powers of $$2$$ behave like a fair coin (divisible by $$2^1$$ with probability $$1/2$$, by $$2^2$$ with probability $$1/4$$, by $$2^k$$ with probability $$1/2^k$$), the expected number of halvings is
   $$
   \mathbb{E}[a(N)] = \sum_{k=1}^{\infty} \frac{k}{2^k} = 2.
   $$
   On average, each odd step multiplies by $$3$$ and divides by $$2^2 = 4$$, giving a geometric shrinkage factor of
   $$
   \frac{3}{4} = 0.75 < 1!
   $$
   In logarithmic terms, $$\log\operatorname{Syr}(N) - \log N \approx \log(3/4) \approx -0.288 < 0$$. Like a gambler playing a slightly unfavorable game, a typical orbit drifts steadily downward—and the critical exponent $$\dfrac{\log 3}{\log 4} \approx 0.7925$$ emerges naturally from comparing $$3$$ against $$4$$.

2. **Now test the exact same rule on negative integers (seed $$n = -5$$):**
   $$
   -5 \to -14 \to -7 \to -20 \to -10 \to -5!
   $$
   A genuine **nontrivial cycle of length 5**! (And $$n = -1$$ gives $$-1 \to -2 \to -1$$; $$n = -17$$ enters an 18-step cycle!)

**Why this matters:** The negative integers obey the *exact same* $$3/4$$ random-parity drift heuristic—yet they contain **three distinct cycles**! That single hand check proves why no naive probabilistic drift argument can ever settle Collatz: a deterministic system with downward average drift can still hide exceptional periodic loops.

---

## 6. Accelerated maps and the Syracuse formulation

Popular videos usually write the standard map $$T$$, whereas research talks (Tao, Lagarias, Chamberland) prefer the **Syracuse map** on odd integers:

$$
\operatorname{Syr}(N) = \frac{3N+1}{2^{a(N)}},
$$

where $$2^{a(N)}$$ is the largest power of $$2$$ dividing $$3N+1$$. Working directly on odd integers strips away the trivial halving steps and exposes the 2-adic and 3-adic statistics that power modern almost-all theorems. Always note which map an author uses before comparing stopping times or step counts.

---

## 7. Partial mathematics (without claiming completeness)

Lagarias’s surveys ([arXiv:2111.02635](https://arxiv.org/abs/2111.02635)) document decades of genuine partial progress. The most dramatic line of attack asks: *even if we cannot prove every $$N$$ reaches $$1$$, what can we prove for **almost all** $$N$$?*

### 7.1 Density and almost-all descent (timeline slogans)

| Result family | Slogan (undergrad-accessible) | Density type |
|---------------|-------------------------------|--------------|
| Krasikov–Lagarias type | Many integers $$N \le x$$ already satisfy $$\operatorname{Col}_{\min}(N) = 1$$ (quantitative lower bounds growing with $$x$$) | Counting up to $$x$$ |
| Terras (1976) | Almost all $$N$$ eventually drop **below** $$N$$ (finite stopping time) | Natural density |
| Allouche / Korec | Almost all $$N$$ satisfy $$\operatorname{Col}_{\min}(N) < N^\theta$$; Korec reaches $$\theta > \log 3 / \log 4 \approx 0.7925$$ | Natural density |
| **Tao (2019)** | Almost all $$N$$ satisfy $$\operatorname{Col}_{\min}(N) < f(N)$$ for **any** $$f(N) \to \infty$$, no matter how slowly | **Logarithmic density** |

**Tao’s theorem (2019).** For *any* function $$f(N) \to +\infty$$ (even something glacially slow like $$\log\log\log\log N$$), almost all positive integers $$N$$ (in the sense of **logarithmic density**) satisfy $$\operatorname{Col}_{\min}(N) < f(N)$$.

**What Tao (2019) is NOT:**
- **Not** a proof that *every* $$N$$ reaches $$1$$ (a sparse exceptional set of logarithmic density $$0$$ could still escape or cycle).
- **Not** natural density (logarithmic density weights smaller numbers slightly more heavily via $$\sum 1/n$$).
- **Not** a computer verification—it is a pure analytic and probabilistic theorem ([arXiv:1909.03562](https://arxiv.org/abs/1909.03562), [Tao’s blog](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/)).

---

### Deep-Dive Explanation: How Tao (2019) Reached "Almost Bounded" Orbits (Read Slowly)

Before 2019, mathematicians already knew that almost all integers drop below $$N^{0.7925}$$. Why couldn’t you simply apply that theorem again and again until you hit $$1$$? Follow these four steps to see the exact bottleneck Tao broke.

#### Step 1: Why naive iteration of Terras/Korec fails
Suppose you know that $$99.9\%$$ of integers drop from $$N$$ down to $$N^{0.79}$$. You might think: *“Great! Just feed those landed numbers back into the theorem and drop to $$(N^{0.79})^{0.79} = N^{0.62}$$, and repeat until you reach $$1$$!”* The trap: the Collatz map is **not** uniform! What if $$99.9\%$$ of starting numbers all funnel into the tiny $$0.1\%$$ “bad set” where the theorem doesn’t apply? To iterate descent, you must prove that the *output distribution* does not pile up inside bad sets.

#### Step 2: Switch to the Syracuse map and watch 3-adic bias
After one Syracuse step $$\operatorname{Syr}(N) = (3N+1)/2^{a(N)}$$, the output is **never** divisible by $$3$$ (because $$3N+1 \equiv 1 \pmod 3$$). More subtly, remainders modulo $$3^k$$ do *not* stay uniform—they drift toward a tilted, irregular 3-adic distribution. Ignoring that bias wrecks the iteration.

#### Step 3: Build an approximately invariant "Syracuse random variable"
Tao’s key insight was to discover a **skewed probability distribution** on $$\mathbb{Z}/3^n\mathbb{Z}$$ (constructed via *Syracuse random variables*) that is *almost invariant* under the Collatz/Syracuse dynamics. Instead of forcing the orbits to stay uniform, he tracked them using a custom-built weighted measure that naturally respects their 3-adic bias, proving that these laws stabilize as $$n$$ grows (using Fourier/characteristic-function estimates and renewal theory).

#### Step 4: Iterate all the way down—and see why $$1$$ still slips away
With an approximately invariant distribution in hand, Tao could safely chain descent steps together without losing control into bad sets, pushing $$\operatorname{Col}_{\min}(N)$$ below *any* growing function $$f(N) \to \infty$$! Why couldn’t he set $$f(N) = 1.5$$ (a constant) to prove $$\operatorname{Col}_{\min}(N) = 1$$? Because his error bounds shrink only as $$f(N)$$ grows—once an orbit gets down to a tiny constant neighborhood, the probabilistic averaging loses its leverage, and **logarithmic density** still allows a sparse set of exceptions.

---

### 7.2 Cycles, generalizations, and computation

- **Constraints on cycles:** Eliahou and successors proved that any nontrivial positive cycle of $$T$$ would have to be astronomically long (hundreds of billions of steps).
- **Generalizations:** Maps like $$5x+1$$ or Conway’s FRACTRAN exhibit genuine divergent orbits, extra cycles, and undecidability. Remember: undecidability of *generalized* Collatz maps does **not** prove that the classical $$3x+1$$ conjecture is undecidable.
- **Computational engineering:** Verification projects use modular sieves (mod $$2^k$$) and tree pruning to skip huge swathes of integers whose stopping times are already known to be finite.

---

## 8. Hardness in plain language

Why does a one-line recurrence resist a century of mathematics? Because it mixes two incompatible algebraic worlds: **base-2 division** ($$n/2$$) and **base-3 multiplication plus addition** ($$3n+1$$). Multiplication by $$3$$ scrambles base-2 digits completely, while dividing by $$2$$ scrambles base-3 digits. There is no known smooth energy or Lyapunov function that decreases monotonically along every orbit, leaving discrete arithmetic dynamics with few general-purpose weapons.

---

## 9. Course role: problem page vs exploration studio

| This page (Ch.1) | Studio (Ch.7) |
|------------------|---------------|
| Statement, culture, partial theorems, status | Experiments, code, plots, research logs |
| Conceptual understanding ("simple ≠ easy") | Hands-on creation and falsifiable hypotheses |
| No coding required | Python/notebook exploration encouraged |

In the [Chapter 7 Iteration Studio]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/), never frame your project as “proving Collatz.” Instead:
1. Choose a crisp measurable statistic (stopping time, peak height, residue distribution),
2. Generate reproducible data,
3. State a **falsifiable** hypothesis, and
4. Report honestly what the data support—and what remains unproved.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Checked to $$10^{20}$$ (or $$2^{70}$$), so it’s true.” | Evidence for a finite range only; the universal claim is open. |
| “The sequence is random.” | Completely deterministic; only its statistics look irregular. |
| “$$3n+1$$ grows, so orbits should explode.” | Paired with halvings, the average Syracuse factor is $$3/4 < 1$$. |
| “A viral proof online settled it.” | Extraordinary claims require peer review; the conjecture remains open. |
| “Only the $$4$$–$$2$$–$$1$$ cycle exists everywhere.” | Only in positive integers under $$T$$; negative integers have extra cycles (like $$-5 \to -14 \to -7 \to -20 \to -10 \to -5$$). |
| “Simple statement means it should be easy.” | Accessibility of statement and difficulty of proof are completely separate. |
| “Tao solved Collatz / almost all means every.” | Tao (2019) proved almost-all / almost-bounded (log density), **not** the full conjecture. |
| “Syracuse map is a different conjecture.” | It is the accelerated odd-integer form of the same positive Collatz problem. |
| “Collatz is proved undecidable.” | Certain *generalizations* are undecidable; the classical $$3x+1$$ conjecture’s status is open. |

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

Build a small computational laboratory around orbits and stopping times in the [Chapter 7 Iteration Studio]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/), keep a clean research log, and write up what remains open. For a solved-but-deep contrast after this open problem, visit the [Four Color Theorem]({{ site.baseurl }}/contents/en/chapter01/01_09_Four_Color_Theorem/).

## Video tham khảo

- **xem trước** — [The Simplest Math Problem No One Can Solve - Collatz Conjecture](https://www.youtube.com/watch?v=094y1Z2wpJg) — Veritasium, English. Watch first. “The Simplest Math Problem No One Can Solve - Collatz Conjecture” orients the lesson’s aim: State the Collatz map T and the conjecture that every positive integer eventually reaches the cycle 4\to 2\to 1.
- [UNCRACKABLE? The Collatz Conjecture - Numberphile](https://www.youtube.com/watch?v=5mFpVDpKX70) — Numberphile, English. A second pass once the main claim is in view: State the Collatz map T and the conjecture that every positive integer eventually reaches the cycle 4\to 2\to 1.
- [The 3x+1 Problem: Status and Recent Work Part 1](https://www.youtube.com/watch?v=t1I9uHF9X5Y) — Experimental mathematics, English. Further depth after the first two, still tied to this lesson: State the Collatz map T and the conjecture that every positive integer eventually reaches the cycle 4\to 2\to 1.
