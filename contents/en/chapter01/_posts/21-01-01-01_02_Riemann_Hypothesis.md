---
layout: post
title: "The Riemann Hypothesis"
chapter: '01'
order: 2
owner: Nguyen Le Linh
lang: en
categories:
- chapter01
---

In the autumn of 1859, the young German mathematician Bernhard Riemann submitted a memoir just eight pages long to the Berlin Academy of Sciences. He could hardly have imagined that those eight pages would become the most celebrated unsolved mystery in pure mathematics. Looking at the prime numbers—the discrete "atoms" of arithmetic scattered seemingly at random along the number line—Riemann heard a symphony. He discovered that the rhythm of the primes is governed by the zeros of a single complex function: the **Riemann zeta function**, $$\zeta(s)$$.

More than a century and a half later, the **Riemann Hypothesis (RH)** stands as the crown jewel of the Clay Millennium Prize Problems. It is far more than a million-dollar puzzle about a complex function; it is the decisive question about how much deep order lives inside the integers.

This is the **Section 1 flagship** reading for the Math Enthusiast seminar: a careful, intuition-first tour of **what RH says**, **why zeros of a complex function control the primes**, **what evidence and partial theorems exist**, and **what mathematics blossomed around the question**.

**Path through the essay:** Key ideas → primes and numerical counting → Euler product → analytic continuation (via geometric series & $$\eta(s)$$) → non-trivial zeros → RH → explicit formulas & wave harmonics → why it is hard → partial results & analogues.

---

## Learning objectives

After this lecture you should be able to:

- State the **Riemann Hypothesis** in terms of non-trivial zeros of $$\zeta(s)$$ and the critical line $$\operatorname{Re}(s)=1/2$$.
- Explain how the **Euler product** connects $$\zeta(s)$$ to the primes (for $$\operatorname{Re}(s)>1$$).
- Distinguish **trivial** and **non-trivial** zeros, and say why the hypothesis concerns only the latter.
- Relate RH to the **prime number theorem** at the level of main term vs error term (not a full proof).
- Name at least two kinds of **partial progress** (numerical checks; zero-free regions / density results; function-field analogues).
- Avoid common confusions (RH is not “a formula for the $$n$$th prime”; checking many zeros is not a proof).

**Prerequisites.** Complex numbers as points in the plane; infinite series and products as formal objects; the idea that primes become rarer but never stop. No complex analysis course is required—analytic continuation is developed through familiar undergraduate examples.

**Course connections.** This essay lays the foundation for thinking about "size" and "regularity" across the course. Natural pairings: [Twin Primes]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/), [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/), and [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/).

---

## Key ideas: Complex Analysis and Analytic Number Theory

A university graduate with real calculus, linear algebra, and probability naturally asks: *if prime numbers are completely discrete positive integers, why on earth do we bring complex numbers and calculus into the room?* The answer sits at the crossroads of three pillars:

### 1. Complex Analysis (Functions $$f: \mathbb{C} \to \mathbb{C}$$)
In undergraduate calculus you studied differentiable real functions $$f: \mathbb{R} \to \mathbb{R}$$. **Complex analysis** studies functions of a complex variable $$s = \sigma + it$$. Complex differentiability (**holomorphicity**) is dramatically stricter than real differentiability: a function differentiable once in $$\mathbb{C}$$ is automatically infinitely differentiable and equal to its Taylor series! Because of this extraordinary **rigidity**, knowing a holomorphic function on even a tiny patch forces a **unique** extension to the rest of the complex plane—this is **analytic continuation**. Beyond pure math, complex analysis powers Laplace/Fourier transforms in signal processing, 2D aerodynamics, and quantum mechanics.

### 2. Analytic Number Theory
This is the art of using **continuous tools** (infinite series, integrals, complex functions, asymptotic estimates) to answer **discrete questions** about integers: how many primes lie below $$x$$? How small can prime gaps get? Can every even number $$>2$$ be written as a sum of two primes (Goldbach)?

### 3. The Spectral / Fourier Mindset
Discrete primes are jagged and hard to manipulate with elementary algebra alone. Packaging all primes into a smooth complex function like $$\zeta(s)$$ turns a discrete counting problem into a **spectral / wave-analysis problem**—just as an electrical engineer uses a Fourier transform to decompose a noisy signal into clean frequencies.

---

## 1. What problem about primes is RH really about?

Let $$\pi(x)$$ be the number of primes less than or equal to $$x$$. The primes thin out—$$2, 3, 5, 7, 11, 13, 17, \ldots$$—yet Euclid proved over two millennia ago that they never run out. The modern quantitative question is: **how fast does $$\pi(x)$$ grow?**

At age 15, Carl Friedrich Gauss pored over prime tables and noticed an uncanny pattern: near a large number $$t$$, the average density of primes is roughly $$1/\log t$$ (natural logarithm). Integrating that density from $$2$$ to $$x$$ gives the **logarithmic integral**:

$$
\operatorname{li}(x) = \int_2^x \frac{dt}{\log t}
$$

(alongside the rougher estimate $$x/\log x$$). Let us check concrete numbers to feel how astonishingly accurate Gauss's guess is:

- At $$x = 100$$: exact count $$\pi(100) = 25$$; $$100/\log 100 \approx 21.7$$; $$\operatorname{li}(100) \approx 30.1$$ (off by about 5).
- At $$x = 10^6$$ (one million): $$\pi(10^6) = 78\,498$$; $$10^6/\log(10^6) \approx 72\,382$$ (off by over 6,000), while $$\operatorname{li}(10^6) \approx 78\,628$$ — **off by just 130**, less than $$0.17\%$$!
- At $$x = 10^9$$ (one billion): $$\pi(10^9) = 50\,847\,534$$, while $$\operatorname{li}(10^9) \approx 50\,849\,235$$ — an error of only $$1\,701$$ out of more than 50 million primes!

The **Prime Number Theorem (PNT)**, proved independently by Hadamard and de la Vallée Poussin in 1896, confirms the main term:

$$
\pi(x) \sim \operatorname{li}(x) \qquad (x\to\infty).
$$

RH lives at the **next level of precision**: once you subtract the smooth main term $$\operatorname{li}(x)$$, **how big can the error $$\pi(x) - \operatorname{li}(x)$$ get?** Think of flipping a fair coin $$N$$ times in introductory probability: the number of heads drifts away from $$N/2$$ by roughly $$\sqrt{N}$$. Remarkably, RH asserts that prime counting behaves just as cleanly—the error stays on the scale of $$\sqrt{x}$$ (up to a $$\log x$$ factor)! In slogans:

- **PNT:** primes have a predictable average density.
- **RH:** that density is **as regular as analysis permits**, with no "hidden surges" caused by zeros off the critical line.

![Prime counting main term vs error (schematic)]({{ site.baseurl }}/img/chapter_img/riemann_pnt_error.svg)

*Figure. Cartoon: $$\pi(x)$$ tracks a smooth main term; RH limits how wild the wiggles can be.*

![Gauss-style $$\pi(x)$$ vs smooth density]({{ site.baseurl }}/img/chapter_img/rh_pi_x_li_x_gauss_quanta.jpg)

*Figure. Popular visualization of prime counting against a smooth main-term curve (source: Quanta Magazine RH explainer with Alex Kontorovich).*

---

### Short video: One number, two ways to build it

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/zeta-euler-product_en.mp4"></video>
</div>

Adding $$1/n^2$$ over all integers $$n \le x$$ and multiplying $$1/(1-p^{-2})$$ over only the primes $$p \le x$$ both climb toward $$\pi^2/6 \approx 1.6449$$. This is Euler's identity (sum over integers = product over primes) at $$s=2$$.


### Try it yourself: Add and multiply: the same limit

<div class="mex-explainer" data-mex="zeta" data-lang="en"></div>


## 2. The zeta function and the Euler product

For a complex number $$s=\sigma+it$$ with real part $$\sigma>1$$, define

$$
\zeta(s) = \sum_{n=1}^{\infty} n^{-s} = 1 + 2^{-s} + 3^{-s} + 4^{-s} + \cdots.
$$

The series converges absolutely in that half-plane (just like the $$p$$-series test in first-year calculus). In the 18th century, Leonhard Euler uncovered an algebraic miracle: the very same function factors as an infinite product over **primes alone**:

$$
\zeta(s) = \prod_{p\ \text{prime}} \bigl(1 - p^{-s}\bigr)^{-1}, \qquad \operatorname{Re}(s)>1.
$$

**Worked Example 1 — Expanding Euler's product by hand:**
Recall the geometric series $$\frac{1}{1-r} = 1 + r + r^2 + r^3 + \cdots$$ with $$r = p^{-s}$$:

$$
\prod_{p} \bigl(1 - p^{-s}\bigr)^{-1} = \bigl(1 + 2^{-s} + 4^{-s} + 8^{-s} + \cdots\bigr)\bigl(1 + 3^{-s} + 9^{-s} + \cdots\bigr)\bigl(1 + 5^{-s} + 25^{-s} + \cdots\bigr)\cdots
$$

When you multiply these parentheses out, how can you produce the term $$12^{-s}$$? Since $$12 = 2^2 \cdot 3$$ has a **unique prime factorization**, there is **exactly one way**: pick $$4^{-s} = (2^2)^{-s}$$ from the first factor, $$3^{-s}$$ from the second factor, and $$1$$ from every remaining factor! By the Fundamental Theorem of Arithmetic, every $$n^{-s}$$ appears once and only once. Thus **$$\zeta(s)$$ is a golden bridge between "all integers" and "all primes."**

### Explanation: Why Primes Talk to Zeros

Students often encounter two slogans that feel worlds apart: (A) "RH is about zeros of zeta," and (B) "RH is about primes." Here is the four-step chain linking them—no full explicit formula required:

#### Step 1: Primes build zeta (Euler product)
For $$\operatorname{Re}(s)>1$$, unique prime factorization turns the integer sum into a prime product. Change the primes, and you change $$\zeta(s)$$.

#### Step 2: Zeta extends beyond the product region (Analytic continuation)
Analytic continuation and the functional equation define $$\zeta(s)$$ across the entire complex plane (with one simple pole at $$s=1$$). The non-trivial zeros live inside the critical strip $$0 < \operatorname{Re}(s) < 1$$, where the Euler product no longer converges.

#### Step 3: Explicit formulas turn zeros into prime-counting waves
Weighted sums over primes (or prime powers) can be rewritten as a main term plus a sum of oscillatory waves—one wave for each non-trivial zero $$\rho = \beta + i\gamma$$. The real part $$\beta = \operatorname{Re}(\rho)$$ sets the **amplitude** $$x^\beta$$ of that wave!

#### Step 4: Pinning every zero to $$\beta = 1/2$$ minimizes the error
The Prime Number Theorem gives the main term $$\operatorname{li}(x)$$. How far zeros stray from $$\operatorname{Re}(s)=1/2$$ controls the size of the remainder. RH is the sharpest possible regularity statement: all non-trivial zeros sit at $$\beta = 1/2$$, locking the error to $$O(x^{1/2}\log x)$$.

**What RH is *not*.** It is not a formula that "lists the next prime." It is a **spectral constraint** on zeta that becomes a **regularity constraint** on prime counting.

**Quick check.** For $$\operatorname{Re}(s)>1$$, the Euler product converges and $$\zeta(s)\neq 0$$—so you cannot find critical-strip zeros by plugging primes directly into the product. The order is always: continue first, locate zeros second, return to primes via explicit formulas.

![Euler product]({{ site.baseurl }}/img/chapter_img/riemann_euler_product.svg)

*Figure. Two faces of zeta for $$\operatorname{Re}(s)>1$$: sum over $$n$$, product over primes.*

![Zeta series linked to primes]({{ site.baseurl }}/img/chapter_img/rh_zeta_series_primes_quanta.jpg)

*Figure. The Dirichlet series for $$\zeta(s)$$ (source: Quanta); Euler’s product rewrites the same object using the primes.*

Notice an immediate gem: if there were only finitely many primes, the Euler product would be a finite product of non-zero analytic factors and $$\zeta(s)$$ would stay finite as $$s \to 1^+$$. Yet the harmonic series $$\sum 1/n$$ diverges, so $$\zeta(s)\to\infty$$—Euler's analytic proof that primes are infinite! Analytic number theory pushes this dictionary vastly further.

---

## 3. Analytic continuation and the functional equation (with concrete intuition)

The series $$\sum n^{-s}$$ only converges when $$\operatorname{Re}(s)>1$$. Plugging $$s = -1$$ straight into the series produces the nonsense sum $$1 + 2 + 3 + \cdots$$. So how can $$\zeta(s)$$ be defined to the left of $$\operatorname{Re}(s)=1$$?

**Worked Example 2 — Seeing analytic continuation via two familiar series:**
1. **The geometric series warm-up:** The series $$f(z) = 1 + z + z^2 + z^3 + \cdots$$ only converges for $$\vert z \vert < 1$$; at $$z = -2$$ it diverges wildly ($$1 - 2 + 4 - 8 + \cdots$$). Yet on $$\vert z \vert < 1$$ it agrees identically with $$F(z) = \frac{1}{1-z}$$, which is smooth everywhere except $$z = 1$$ and gives $$F(-2) = \frac{1}{3}$$. Analytic continuation replaces a local formula (the series) with the **unique global holomorphic function** agreeing with it.
2. **Stepping into the critical strip with $$\eta(s)$$:** Consider the alternating Dirichlet eta series
   $$
   \eta(s) = 1 - 2^{-s} + 3^{-s} - 4^{-s} + 5^{-s} - \cdots
   $$
   For $$\operatorname{Re}(s) > 1$$, a quick algebraic check shows $$\eta(s) = (1 - 2^{1-s})\zeta(s)$$, so $$\zeta(s) = \frac{\eta(s)}{1 - 2^{1-s}}$$. Because the signs alternate, $$\eta(s)$$ converges for **all $$\operatorname{Re}(s) > 0$$**! With one line of algebra, the door into the entire critical strip $$0 < \operatorname{Re}(s) < 1$$ swings wide open.

With deeper tools, Riemann extended $$\zeta(s)$$ to a **meromorphic** function on the entire complex plane: holomorphic everywhere except for a **simple pole at $$s=1$$**. He also proved a **functional equation** linking $$\zeta(s)$$ to $$\zeta(1-s)$$ (packaged with a Gamma factor into a completed xi-function symmetric across $$\operatorname{Re}(s)=1/2$$). What matters most:

1. Zeta is well-defined across the entire plane, far beyond the original series.
2. The reflection symmetry $$s \leftrightarrow 1-s$$ makes the vertical line $$\operatorname{Re}(s)=1/2$$ the natural mirror axis.
3. The zeros split cleanly into two families.

![Trivial vs non-trivial zeros]({{ site.baseurl }}/img/chapter_img/riemann_trivial_vs_nontrivial.svg)

*Figure. Trivial zeros are well understood; non-trivial zeros live in the critical strip.*

**Trivial zeros** sit at the negative even integers $$s=-2,-4,-6,\ldots$$. They come directly from the sine/Gamma factor in the functional equation and hold no mystery.

**Non-trivial zeros** live inside the **critical strip**

$$
0 < \operatorname{Re}(s) < 1.
$$

There are infinitely many, arranged symmetrically across the real axis ($$\rho$$ and $$\bar{\rho}$$) and across $$\operatorname{Re}(s)=1/2$$ ($$\rho$$ and $$1-\rho$$). The very first non-trivial zeros sit at

$$
\rho_1 \approx \frac{1}{2} + 14.1347\,i, \qquad \rho_2 \approx \frac{1}{2} + 21.0220\,i, \qquad \rho_3 \approx \frac{1}{2} + 25.0109\,i.
$$

RH is entirely about this family.

---

## 4. Statement of the Riemann Hypothesis

**Riemann Hypothesis.** Every non-trivial zero of $$\zeta(s)$$ has real part exactly $$1/2$$.

Equivalently: every non-trivial zero lies on the **critical line**

$$
\operatorname{Re}(s) = \tfrac12.
$$

![Critical strip and critical line]({{ site.baseurl }}/img/chapter_img/riemann_critical_strip.svg)

*Figure. The critical strip $$0<\operatorname{Re}(s)<1$$ and the critical line $$\operatorname{Re}(s)=1/2$$ (schematic).*

![RH slogan card]({{ site.baseurl }}/img/chapter_img/rh_critical_line_statement_quanta.jpg)

*Figure. Popular one-line statement of RH (source: Quanta).*

![Non-trivial zeros on the critical line]({{ site.baseurl }}/img/chapter_img/rh_zeros_on_critical_line_quanta.jpg)

*Figure. Schematic zeros sitting on $$\operatorname{Re}(s)=1/2$$ inside the strip (source: Quanta).*

**What RH does *not* say.**

- It does not give a closed elementary formula for the $$n$$th prime.
- It does not claim that primes are “random” in a naive sense—though random models are useful heuristics.
- It is not settled by computing the first $$N$$ zeros on the line, for any finite $$N$$.

**What RH *does* say.** Among all zeros that affect prime distribution through explicit formulas, none sit off the line of symmetry. Even a single off-line zero (say at $$\beta = 0.6$$) would inject dramatically larger oscillations into $$\pi(x)-\operatorname{li}(x)$$.

---

## 5. Why the zeros control primes

**Explicit formulas** (Riemann, von Mangoldt, and later refinements) link weighted sums over prime powers directly to sums over the zeros $$\rho = \beta + i\gamma$$ of $$\zeta(s)$$.

To see the mechanism with undergraduate calculus, look at the term $$x^\rho$$ contributed by a single zero $$\rho = \beta + i\gamma$$. Using Euler's formula $$e^{i\theta} = \cos\theta + i\sin\theta$$:

$$
x^{\rho} = x^{\beta + i\gamma} = x^{\beta}\, e^{i\gamma \log x} = x^{\beta}\bigl(\cos(\gamma \log x) + i\sin(\gamma \log x)\bigr).
$$

Pause and admire that single line—it is the heartbeat of the entire lesson:
- The imaginary part $$\gamma$$ acts as the **frequency** of a wave (in logarithmic scale $$\log x$$).
- The real part $$\beta$$ controls the **amplitude** $$x^{\beta}$$ of that wave!

If a zero sat at $$\beta = 0.9$$, its wave would have amplitude $$x^{0.9}$$—at $$x = 10^{10}$$, that is $$10^9$$ versus $$10^5$$ for $$\beta = 0.5$$, a factor of **10,000 times larger**! Because zeros come in symmetric pairs $$(\beta, 1-\beta)$$, the smallest possible worst-case amplitude occurs precisely when **every zero is pinned to $$\beta = 1/2$$**, giving the near-optimal bound:

$$
\pi(x) = \operatorname{li}(x) + O\bigl(x^{1/2}\log x\bigr)
$$

(up to standard technical formulations). Without RH, one still has weaker error bounds coming from **zero-free regions** near $$\operatorname{Re}(s)=1$$ that power the classical proof of PNT.

So the logical chain is:

$$
\text{zeros of }\zeta \;\longleftrightarrow\; \text{oscillations in prime counting} \;\longleftrightarrow\; \text{quality of error terms}.
$$

**Harmonics picture (Quanta / Kontorovich).** Think of a modified prime-counting staircase (stepping by $$\log p$$ at prime powers). Riemann showed this staircase can be rebuilt by summing **oscillatory harmonics** attached to the zeta zeros: a main contribution associated with the pole at $$s=1$$, plus corrections from each non-trivial zero—just like summing sine waves in a Fourier series to reconstruct a step function. **Where** those zeros sit (how large $$\beta=\operatorname{Re}(\rho)$$ can be) controls how large the remaining error can be—hence RH’s grip on prime distribution.

![Prime-counting staircase vs smooth approximation]({{ site.baseurl }}/img/chapter_img/rh_prime_counting_harmonics_quanta.jpg)

*Figure. Staircase of primes (or a close relative) versus a smooth main term; zeros supply the “music” of the error (source: Quanta).*

---

## 6. Why is RH hard?

**No elementary rearrangement.** Unlike Euclid’s infinitude proof, RH is not a short argument about factorizations alone. It lives in the analytic continuation of an infinite object.

**Global control from local data.** Zeros are global features of an analytic function. Estimates that work in one region of the strip do not automatically pin every zero to the line.

**Barriers to “obvious” strategies.** Many natural approaches in analytic number theory produce partial information (most zeros near the line; zeros in density; no zeros in certain regions) without forcing the exact line for all zeros.

**Depth of analogues.** When parallel statements *are* proved (for zeta functions of curves over finite fields), the proofs rely on heavy algebraic geometry—where a natural geometric operator (Frobenius acting on étale cohomology) plays the role of a matrix with real eigenvalues. No comparable geometric space has yet been found for $$\zeta(s)$$ over $$\mathbb{Q}$$ (the dream behind the *Hilbert–Pólya conjecture*).

Hardness here means **resistance of the exact statement**, not lack of progress. The subject is rich with theorems that assume RH, theorems that approach RH, and theorems that replace RH by weaker hypotheses still useful in applications.

---

## 7. Evidence and partial results

### Numerical evidence

More than $$10^{13}$$ (ten trillion) non-trivial zeros have been computed and verified to lie on the critical line. This is strong evidence and a technological achievement; it is **not** a proof. In number theory, patterns can hold up to staggering heights before breaking (remember Littlewood's theorem that $$\pi(x) - \operatorname{li}(x)$$ eventually changes sign!). A single counterexample at enormous height would disprove RH; brute-force checking cannot reach infinity.

### Theoretical partial results

- **Zero-free regions.** There is a region near $$\operatorname{Re}(s)=1$$ containing no zeros; such regions imply PNT and effective error terms.
- **Density theorems.** Bounds on how many zeros can lie far from the critical line.
- **Positive proportion on the line.** Over 40% of all non-trivial zeros are proved to lie on $$\operatorname{Re}(s)=1/2$$ (Selberg; Levinson; Conrey and later refinements).
- **Moments and pair correlation.** Following a famous 1972 tea-time encounter at Princeton between number theorist Hugh Montgomery and physicist Freeman Dyson, mathematicians discovered that the spacing between zeta zeros follows the exact same statistics as **eigenvalues of random Hermitian matrices** (the GUE ensemble from nuclear physics)—one of the deepest clues about the hidden nature of RH.

### Function-field and geometric analogues

For zeta functions attached to curves (and more generally varieties) over finite fields, the analogue of RH was proved by **Weil** (curves) and in greater generality by **Deligne**. Those theorems are pillars of modern arithmetic geometry. They show that “RH-type” statements can be true in neighboring worlds—while the original zeta of $$\mathbb{Q}$$ remains open.

![Timeline]({{ site.baseurl }}/img/chapter_img/riemann_timeline.svg)

*Figure. Selected milestones from Riemann’s memoir to the present open status.*

---

## 8. What would follow from RH?

A huge web of conditional theorems in analytic number theory assumes RH or the Generalized Riemann Hypothesis (GRH) for Dirichlet $$L$$-functions. Themes include:

- Strong error terms in prime counting in arithmetic progressions (e.g., primes congruent to $$1 \pmod 4$$ vs $$3 \pmod 4$$).
- Sharp bounds on gaps between consecutive primes, the least quadratic non-residue, class numbers, and deterministic polynomial-time primality testing (Miller's test).
- Many “almost optimal” estimates that are known unconditionally only in weaker form.

Conversely, many applications need only weaker substitutes (such as the Bombieri–Vinogradov theorem, which acts like "GRH on average"). Professional number theory is not “waiting for RH to do anything”—but RH remains the benchmark for the strongest classical error terms.

---

## 9. RH among other great problems

| Problem | Flavor | Link to RH |
|---------|--------|------------|
| Twin primes | Additive patterns in primes | Same prime world; different tools (sieve) |
| BSD | Ranks of elliptic curves via $$L$$-functions | Sister philosophy: special values / zeros of $$L$$ encode arithmetic |
| P vs NP | Computational complexity | Unrelated mechanism; shared “central open problem” cultural role |
| Kakeya (dimension) | Geometric measure / analysis | Different field; both reward precise size notions |

For the seminar, RH is the prototype of: **one clean analytic statement, century-scale depth, vast conditional consequences.**

---

## 10. Common confusions (checklist)

1. **“They checked a billion zeros, so it’s true.”** — Evidence, not proof.  
2. **“RH gives the $$n$$th prime by a formula.”** — It constrains errors in counting functions; it is not a closed elementary formula for $$p_n$$.  
3. **“Trivial zeros violate RH.”** — No; RH is only about non-trivial zeros.  
4. **“Zeta is only the series $$\sum n^{-s}$$.”** — The series is the definition for $$\operatorname{Re}(s)>1$$; RH lives in the analytic continuation.  
5. **“If RH is false, primes are chaotic with no theorems.”** — PNT and much else are unconditional; false RH would worsen certain error terms, not erase the subject.

---

## From the video / survey path: partial theorems vs full RH

Popular lectures (Quanta/Kontorovich; Conrey; Vaaler) and surveys (Bombieri Clay description; Conrey Notices) share a clean split students should keep:

| Layer | What is known (slogans) | What remains open |
|-------|-------------------------|-------------------|
| No zeros on $$\operatorname{Re}(s)=1$$ | Equivalent (in standard form) to the **prime number theorem** | — |
| Zero-free regions near $$\operatorname{Re}(s)=1$$ | Classical and modern refinements control some error terms | Width still far from the critical line |
| Zeros *on* the critical line | Positive proportion results (Hardy–Littlewood → Selberg → Levinson → Conrey lineage) | **100%** of non-trivial zeros on the line |
| Function-field / finite-field analogues | Weil / Deligne: RH-type statements **proved** for zeta of curves (and more) over finite fields | Does not automatically transfer to $$\zeta(s)$$ |
| Numerical verification | Trillions of zeros checked on the line | Evidence, **not** a proof |

**Status (as of 2026):** the Riemann Hypothesis for the classical zeta function remains **open**—one of the six unsolved Clay Millennium problems.

**Note-taking tip after videos:** write two sentences after any talk: (1) what RH *says*; (2) what kind of "evidence" the talk presented (computation, density theorem, or analogue)—never "they checked many zeros, so RH is true."

---

## Mode C — reconstructed notes from flagship videos

*Reconstructed knowledge units (not transcript dumps). Cross-check against the written sections above and against Clay/Bombieri-style surveys. Captions live under `research/video-research/Riemann_Hypothesis/transcripts/`.*

### C1. Quanta / Kontorovich orientation (*The Riemann Hypothesis, Explained*)

Orientation talks fix three student-facing images that must stay separate:

1. **Euler product.** For $$\operatorname{Re}(s)>1$$, the identity connecting $$\zeta(s)$$ to primes is the reason zeros can control prime distribution—not a free bonus.  
2. **Analytic continuation.** The series definition is not the whole story: Riemann needs a function that agrees with the series where both make sense and is meaningful on a larger domain (including the critical strip). Popular “two functions, one identity region” language is a slogan for continuation, not a full uniqueness course.  
3. **The critical line as a claim.** RH asserts a location for non-trivial zeros. Visualizations of many zeros on the line are **evidence graphics**, not a proof. Large-scale numerical searches (billions or trillions of zeros on the line in computational reports) remain **finite checks**.

**Trap to avoid:** “A computer checked many zeros, so RH is true.” → Evidence for those zeros; the universal claim is open.

### C2. Vaaler-style foundation (Millennium lectures)

Longer survey lectures typically walk: unique factorization → Euler product → $$\pi(x)$$ vs smooth models of prime counting → error terms and zeros. Keep the hierarchy:

- **Prime number theorem** is a theorem (equivalences involving no zeros on $$\operatorname{Re}(s)=1$$ in standard formulations).  
- **RH** is a far stronger location statement that would sharpen error terms dramatically.  
- Teaching order matters: do not let RH swallow PNT as if PNT were still a conjecture.

### C3. “Beyond RH” culture (e.g. Lichtman / Numberphile frontier clips)

Some modern results ask for arithmetic consequences that would *follow from* RH and then prove related statements **without assuming full RH**, or go past square-root barriers in special counting problems. For seminar purposes:

| Phrase in a video | How to hear it |
|-------------------|----------------|
| “Beyond the Riemann Hypothesis” | Usually: stronger arithmetic conclusions, or unconditional results past former barriers—not “RH is false” |
| “World records” | Computational or analytic records about primes in progressions / bases—**not** a resolution of RH |
| “23% beyond…” | A quantitative slogan about a specific theorem’s strength relative to RH-conditional bounds—read the paper title before quoting |

**Status reminder:** classical RH for $$\zeta(s)$$ remains open as of 2026.

### C4. Pack timestamps for navigation

Use `research/video-research/Riemann_Hypothesis/TRANSCRIPT_STATUS.md` and `*_knowledge_units.json` to jump by ~90s chunks. Prefer the **reconstructed** table above for graded writing; use raw captions only to locate a spoken claim you will then restate in your own words.

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as a substitute for a proof (none is known for classical RH). Full ranking and Mode B notes: `research/video-research/Riemann_Hypothesis/`.

**Recommended order**

1. **Orientation** — Quanta / Alex Kontorovich, *The Riemann Hypothesis, Explained* (~16 min): [YouTube](https://www.youtube.com/watch?v=zlm1aajH6gY). Companion essay: [Quanta](https://www.quantamagazine.org/how-i-learned-to-love-and-fear-the-riemann-hypothesis-20210104/).  
2. **Culture** — Numberphile, *Riemann Hypothesis* (Edward Frenkel): [YouTube](https://www.youtube.com/watch?v=d6c6uIyieoo) · [page](https://www.numberphile.com/videos/riemann-hypothesis).  
3. **Foundation** — Jeff Vaaler, Millennium Prize lecture on RH: [YouTube](https://www.youtube.com/watch?v=Lf3gli_fR2c).  
4. **Core survey lecture** — Brian Conrey, *Primes and Zeros: A Million-Dollar Mystery* (MoMath): [YouTube](https://www.youtube.com/watch?v=OS2V6FLFmxU).  
5. **Frontier taste (optional)** — Numberphile, *23% Beyond the Riemann Hypothesis* (Lichtman): [YouTube](https://www.youtube.com/watch?v=dwe4-OiRw7M).

**After videos, remember:** positive-proportion theorems and numerical checks are **partial progress**; full RH for $$\zeta$$ is still **open** as of 2026.

---


### Transcript & frames (flagship extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Riemann_Hypothesis/transcripts/` · status: `research/video-research/Riemann_Hypothesis/TRANSCRIPT_STATUS.md` · master list: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Captions are auto-downloaded (yt-dlp); treat as navigation aids, not as a substitute for the lesson text.


![Flagship video sample frame]({{ site.baseurl }}/img/video_research/flagships/rh_quanta_frame01.jpg)

*Figure. Sample still from a primary flagship video (see pack for timestamps).*

## References

Full URL bibliography from video research: `research/video-research/Riemann_Hypothesis/references.md`.

### Official statements and surveys

1. **B. Riemann**, *Über die Anzahl der Primzahlen unter einer gegebenen Grösse* (1859) — founding memoir.  
2. **Clay Mathematics Institute**, [Riemann Hypothesis](https://www.claymath.org/millennium/riemann-hypothesis/) · Bombieri official PDF: [riemann.pdf](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf).  
3. **J. B. Conrey**, *The Riemann Hypothesis*, Notices AMS (2003): [PDF](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/conreyRH.pdf) · longer notes: [AIM](https://aimath.org/~kaur/publications/90.pdf).  
4. **H. M. Edwards**, *Riemann’s Zeta Function*; **E. C. Titchmarsh**, *The Theory of the Riemann Zeta-Function*; **A. Ivić**, *The Riemann Zeta-Function*.  
5. Wikipedia — [Riemann hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis).

### Videos (primary path)

6. Quanta — RH Explained (Kontorovich): https://www.youtube.com/watch?v=zlm1aajH6gY  
7. Numberphile — RH (Frenkel): https://www.youtube.com/watch?v=d6c6uIyieoo · https://www.numberphile.com/videos/riemann-hypothesis  
8. Vaaler Millennium lecture: https://www.youtube.com/watch?v=Lf3gli_fR2c  
9. Conrey MoMath lecture: https://www.youtube.com/watch?v=OS2V6FLFmxU  
10. Numberphile — 23% beyond RH: https://www.youtube.com/watch?v=dwe4-OiRw7M  

### Web expositions

11. Quanta companion essay (Kontorovich): https://www.quantamagazine.org/how-i-learned-to-love-and-fear-the-riemann-hypothesis-20210104/  
12. Clay lectures hub: https://www.claymath.org/lectures/  
13. Marcus du Sautoy, *The Music of the Primes* — popular history (read critically).  

### Course

14. [Twin primes]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/), [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/), [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [Wang / Kakeya]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/). Research pack: `research/video-research/Riemann_Hypothesis/`.

---

## Further directions

- Seminar **A3**: RH is a natural open-problem brief—state it, explain hardness, name surrounding tools (explicit formulas, zero-free regions, analogues).  
- Compare the *culture* of RH (analytic number theory) with P vs NP (complexity) or Kakeya (harmonic analysis / GMT).  
- Optional: Quanta → Conrey lecture → re-read §§2–5 here.  
- Stretch: Dirichlet $$L$$-functions and GRH.

## Video tham khảo

- **xem trước** — [The Riemann Hypothesis, Explained](https://www.youtube.com/watch?v=zlm1aajH6gY) — Quanta Magazine, English. Watch first. “The Riemann Hypothesis, Explained” orients the lesson’s aim: State the Riemann Hypothesis in terms of non-trivial zeros of \zeta(s) and the critical line \operatorname{Re}(s)=1/2.
- [Riemann Hypothesis - Numberphile](https://www.youtube.com/watch?v=d6c6uIyieoo) — Numberphile, English. A second pass once the main claim is in view: State the Riemann Hypothesis in terms of non-trivial zeros of \zeta(s) and the critical line \operatorname{Re}(s)=1/2.
- [The Riemann Hypothesis - Jeff Vaaler (Millennium Prize Problem, Official Introduction) (2001)](https://www.youtube.com/watch?v=Lf3gli_fR2c) — Graduate Mathematics, English. Further depth after the first two, still tied to this lesson: State the Riemann Hypothesis in terms of non-trivial zeros of \zeta(s) and the critical line \operatorname{Re}(s)=1/2.
