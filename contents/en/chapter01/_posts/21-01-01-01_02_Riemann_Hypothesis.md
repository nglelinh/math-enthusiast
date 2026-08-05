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

The **Riemann Hypothesis (RH)** is one of the Clay Millennium Prize Problems and, for many mathematicians, the most important unsolved problem in pure mathematics. It asks a precise question about the zeros of a single complex function—the **Riemann zeta function**—and, through that function, about how prime numbers are distributed among the integers.

This is the **Section 1 flagship** reading for the Math Enthusiast seminar: not a research paper, but a careful map of **what RH says**, **why primes care**, **what evidence we have**, and **what mathematics grew around the question**.

**Path through the essay:** primes and counting → Euler product → zeta and continuation → non-trivial zeros → RH → prime number theorem and error terms → why it is hard → partial results and analogues → open ends.

---

## Learning objectives

After this lecture you should be able to:

- State the **Riemann Hypothesis** in terms of non-trivial zeros of $$\zeta(s)$$ and the critical line $$\operatorname{Re}(s)=1/2$$.
- Explain how the **Euler product** connects $$\zeta(s)$$ to the primes (for $$\operatorname{Re}(s)>1$$).
- Distinguish **trivial** and **non-trivial** zeros, and say why the hypothesis concerns only the latter.
- Relate RH to the **prime number theorem** at the level of main term vs error term (not a full proof).
- Name at least two kinds of **partial progress** (numerical checks; zero-free regions / density results; function-field analogues).
- Avoid common confusions (RH is not “a formula for the $$n$$th prime”; checking many zeros is not a proof).

**Prerequisites.** Complex numbers as points in the plane; infinite series and products as formal objects; the idea that primes become rarer but never stop. No complex analysis course is required—the analytic continuation story is conceptual.

**Seminar link.** Supports course outcomes **LO1** (explain a major open problem) and parts of **LO2** (different notions of size/regularity: here, how “regular” prime gaps can be). Natural pairings: Twin Primes; BSD (another $$L$$-function story); Explorations on prime predictability.

---

## 1. What problem about primes is RH really about?

Let $$\pi(x)$$ be the number of primes less than or equal to $$x$$. The primes thin out:

$$
2,3,5,7,11,13,17,\ldots
$$

but Euclid already knew there are infinitely many. The modern quantitative question is: **how does $$\pi(x)$$ grow?**

Gauss and others guessed that $$\pi(x)$$ is about

$$
\operatorname{li}(x) = \int_2^x \frac{dt}{\log t}
$$

(or the simpler cousin $$x/\log x$$). The **prime number theorem (PNT)**, proved independently by Hadamard and de la Vallée Poussin in 1896, makes the main term rigorous:

$$
\pi(x) \sim \operatorname{li}(x) \qquad (x\to\infty).
$$

That is already a triumph. RH is about the **next level of precision**: once you subtract the main term, **how large can the remaining error be?** The zeros of zeta control that error. In slogans:

- PNT says primes have a predictable average density.
- RH says that density is **as regular as a certain analytic picture allows**—no “hidden irregularities” from zeros off the critical line.

![Prime counting main term vs error (schematic)]({{ site.baseurl }}/img/chapter_img/riemann_pnt_error.svg)

*Figure. Cartoon: $$\pi(x)$$ tracks a smooth main term; RH limits how wild the wiggles can be.*

![Gauss-style $$\pi(x)$$ vs smooth density]({{ site.baseurl }}/img/chapter_img/rh_pi_x_li_x_gauss_quanta.jpg)

*Figure. Popular visualization of prime counting against a smooth main-term curve (source: Quanta Magazine RH explainer with Alex Kontorovich).*

---

## 2. The zeta function and the Euler product

For a complex number $$s=\sigma+it$$ with real part $$\sigma>1$$, define

$$
\zeta(s) = \sum_{n=1}^{\infty} n^{-s} = 1 + 2^{-s} + 3^{-s} + 4^{-s} + \cdots.
$$

The series converges absolutely in that half-plane. Euler’s insight is that the same function factors over primes:

$$
\zeta(s) = \prod_{p\ \text{prime}} \bigl(1 - p^{-s}\bigr)^{-1}, \qquad \operatorname{Re}(s)>1.
$$

Every integer has a unique prime factorization; expanding the product recovers the series. So **$$\zeta(s)$$ is a dictionary between “all integers” and “all primes.”**

### Bridge box — why primes talk to zeros (read slowly)

Students often meet two slogans that feel disconnected: (A) “RH is about zeros of zeta,” and (B) “RH is about primes.” Here is the **one-way chain** that links them—no full explicit formula required.

1. **Primes build zeta (Euler product).** For $$\operatorname{Re}(s)>1$$, unique factorization turns the series over integers into a product over primes. If you change the set of primes, you change $$\zeta$$.  
2. **Zeta continues beyond the product region.** Analytic continuation + functional equation define $$\zeta(s)$$ on the whole plane (pole at $$s=1$$). Non-trivial zeros live in the critical strip even though the Euler product does not converge there.  
3. **Explicit formulas (slogan).** Weighted sums over primes (or prime powers) can be rewritten using sums over zeros of $$\zeta$$. Each zero contributes an oscillatory term; the real part $$\beta=\operatorname{Re}(\rho)$$ controls how large those oscillations can be.  
4. **Error terms in prime counting.** The Prime Number Theorem is the main term for $$\pi(x)$$ (or $$\psi(x)$$). The **size of the remainder** is governed by how far zeros sit from the line $$\operatorname{Re}(s)=1/2$$. RH is the strongest uniform claim that all non-trivial zeros have $$\beta=1/2$$, hence the cleanest classical bound on that error (up to logarithmic factors in standard formulations).

**What RH is *not*.** It is not a formula that “lists the next prime.” It is a **spectral constraint** on zeta that, through the dictionary above, becomes a **constraint on how irregular prime counting can be**.

**Micro-check.** For $$\operatorname{Re}(s)>1$$ the product converges and $$\zeta(s)\neq 0$$ there—so the mystery zeros are *not* read off by plugging primes into the product in the critical strip. Continuation first; zeros second; primes again via explicit formulas.

![Euler product]({{ site.baseurl }}/img/chapter_img/riemann_euler_product.svg)

*Figure. Two faces of zeta for $$\operatorname{Re}(s)>1$$: sum over $$n$$, product over primes.*

![Zeta series linked to primes]({{ site.baseurl }}/img/chapter_img/rh_zeta_series_primes_quanta.jpg)

*Figure. The Dirichlet series for $$\zeta(s)$$ (source: Quanta); Euler’s product rewrites the same object using the primes.*

If there were only finitely many primes, the product would be a finite product of analytic non-zero factors for $$\operatorname{Re}(s)>1$$, and $$\zeta(s)$$ could not have a pole at $$s=1$$. The harmonic series $$\sum 1/n$$ diverges, so $$\zeta(s)\to\infty$$ as $$s\to 1^+$$—another route to infinitude of primes. Analytic number theory sharpens this dictionary far beyond infinitude.

---

## 3. Analytic continuation and the functional equation (ideas only)

The series $$\sum n^{-s}$$ only converges for $$\operatorname{Re}(s)>1$$. Riemann showed that $$\zeta(s)$$ extends to a **meromorphic** function on the whole complex plane: holomorphic everywhere except for a **simple pole at $$s=1$$**.

There is also a **functional equation** relating $$\zeta(s)$$ to $$\zeta(1-s)$$ (usually packaged with a Gamma factor into a completed xi-function that is entire and symmetric about $$\operatorname{Re}(s)=1/2$$). You do not need the formula memorized for this course. What matters:

1. Zeta is defined far to the left of $$\operatorname{Re}(s)=1$$, not only by the series.
2. Symmetry of the functional equation makes the line $$\operatorname{Re}(s)=1/2$$ special.
3. Zeros come in two families.

![Trivial vs non-trivial zeros]({{ site.baseurl }}/img/chapter_img/riemann_trivial_vs_nontrivial.svg)

*Figure. Trivial zeros are well understood; non-trivial zeros live in the critical strip.*

**Trivial zeros** occur at the negative even integers $$s=-2,-4,-6,\ldots$$. They are “explained” by the Gamma factor in the functional equation and are not the mystery.

**Non-trivial zeros** lie in the **critical strip**

$$
0 < \operatorname{Re}(s) < 1.
$$

They are infinite in number, and their imaginary parts grow without bound. RH is entirely about these.

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

**What RH *does* say.** Among all zeros that affect prime distribution through explicit formulas, none sit off the line of symmetry. Off-line zeros would inject larger oscillations into the error term of $$\pi(x)-\operatorname{li}(x)$$.

---

## 5. Why the zeros control primes

There is a circle of ideas often called **explicit formulas** (Riemann, von Mangoldt, and later refinements): sums over primes (or prime powers) can be related to sums over zeros of zeta.

Very roughly: if you want to know how much $$\pi(x)$$ wiggles around its main term, each zero $$\rho=\beta+i\gamma$$ contributes an oscillatory term whose size is sensitive to the real part $$\beta$$. Zeros with $$\beta$$ closer to $$1$$ would allow larger errors. RH asserts that the worst real part you ever meet among non-trivial zeros is $$1/2$$, which translates into an essentially optimal error bound of the shape

$$
\pi(x) = \operatorname{li}(x) + O\bigl(x^{1/2}\log x\bigr)
$$

(up to standard technical formulations). Without RH, one still has error bounds, but weaker ones, coming from **zero-free regions** near $$\operatorname{Re}(s)=1$$ that power the classical proof of PNT.

So the logical chain is:

$$
\text{zeros of }\zeta \;\longleftrightarrow\; \text{oscillations in prime counting} \;\longleftrightarrow\; \text{quality of error terms}.
$$

RH is the strongest uniform claim about that first link in the classical zeta setting.

**Harmonics picture (Quanta / Kontorovich).** Think of a modified prime-counting staircase (stepping by $$\log p$$ at prime powers). Riemann showed this staircase can be rebuilt by summing **oscillatory harmonics** attached to the zeta zeros: a main contribution associated with the pole at $$s=1$$, plus corrections from each non-trivial zero. Adding more zeros refines the fit to the jagged counting function. **Where** those zeros sit (how large $$\beta=\operatorname{Re}(\rho)$$ can be) controls how large the remaining error can be—hence RH’s grip on prime distribution.

![Prime-counting staircase vs smooth approximation]({{ site.baseurl }}/img/chapter_img/rh_prime_counting_harmonics_quanta.jpg)

*Figure. Staircase of primes (or a close relative) versus a smooth main term; zeros supply the “music” of the error (source: Quanta).*

---

## 6. Why is RH hard?

Several complementary reasons:

**No elementary rearrangement.** Unlike Euclid’s infinitude proof, RH is not a short argument about factorizations alone. It lives in the analytic continuation of an infinite object.

**Global control from local data.** Zeros are global features of an analytic function. Estimates that work in one region of the strip do not automatically pin every zero to the line.

**Barriers to “obvious” strategies.** Many natural approaches in analytic number theory produce partial information (most zeros near the line; zeros in density; no zeros in certain regions) without forcing the exact line for all zeros.

**Depth of analogues.** When parallel statements *are* proved (e.g. for zeta functions of curves over finite fields), the proofs use heavy algebraic geometry—not a template one can casually copy to $$\zeta(s)$$ over the integers.

Hardness here means **resistance of the exact statement**, not lack of progress. The subject is rich with theorems that assume RH, theorems that approach RH, and theorems that replace RH by weaker hypotheses still useful in applications.

---

## 7. Evidence and partial results

### Numerical evidence

The first many billions of non-trivial zeros (ordered by imaginary part) have been checked to lie on the critical line, to extraordinary height—modern projects have gone into the trillions of zeros. This is strong evidence and a technological achievement; it is **not** a proof. A single counterexample at enormous height would disprove RH; none is known. Brute-force checking cannot reach infinity.

### Theoretical partial results

Without claiming completeness, important flavors include:

- **Zero-free regions.** There is a region near $$\operatorname{Re}(s)=1$$ containing no zeros; such regions imply PNT and effective error terms.
- **Density theorems.** Bounds on how many zeros can lie far from the critical line.
- **Positive proportion on the line.** A positive proportion of non-trivial zeros lie on $$\operatorname{Re}(s)=1/2$$ (Selberg; later improvements).
- **Moments and pair correlation.** Statistical models of zeros (including random matrix heuristics, Montgomery pair correlation) match data strikingly well and guide conjectures beyond RH itself.

### Function-field and geometric analogues

For zeta functions attached to curves (and more generally varieties) over finite fields, the analogue of RH was proved by **Weil** (curves) and in greater generality by **Deligne**. Those theorems are pillars of modern arithmetic geometry. They show that “RH-type” statements can be true in neighboring worlds—while the original zeta of $$\mathbb{Q}$$ remains open.

![Timeline]({{ site.baseurl }}/img/chapter_img/riemann_timeline.svg)

*Figure. Selected milestones from Riemann’s memoir to the present open status.*

---

## 8. What would follow from RH?

A huge web of conditional theorems in analytic number theory assumes RH or a generalized RH for Dirichlet $$L$$-functions. Themes include:

- Strong error terms in prime counting in arithmetic progressions.
- Bounds related to the least quadratic non-residue, class numbers, and other arithmetic statistics.
- Many “almost optimal” estimates that are known unconditionally only in weaker form.

Conversely, many applications need only weaker substitutes (zero density estimates, Siegel zeros caveats, etc.). Professional number theory is not “waiting for RH to do anything”—but RH remains the benchmark for the strongest classical error terms.

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
4. **“Zeta is only the series $$\sum n^{-s}$$. ”** — The series is the definition for $$\operatorname{Re}(s)>1$$; RH lives in the analytic continuation.  
5. **“If RH is false, primes are chaotic with no theorems.”** — PNT and much else are unconditional; false RH would worsen certain error terms, not erase the subject.

---

## Challenges and extensions

1. **Restate RH** in one sentence without the word “hypothesis,” then in one sentence with only the words zero, real part, and one-half.  
2. **Euler product test.** Why does the identity with the Euler product require unique factorization?  
3. **Error terms.** If a zero had real part $$0.9$$, would you expect larger or smaller oscillations in $$\pi(x)-\operatorname{li}(x)$$ than under RH? Why?  
4. **Analogue literacy.** What does it mean that RH is proved for curves over finite fields but open for $$\zeta(s)$$?  
5. **Critique practice (LO6).** Find a popular article on RH and mark one sentence that overstates numerical evidence as proof, or confuses trivial zeros with the hypothesis.

---

## Exercises

1. **Warm-up.** List three primes $$p$$ and verify numerically that $$(1-p^{-2})^{-1}$$ is the sum of the geometric series $$1+p^{-2}+p^{-4}+\cdots$$.  
2. **Definitions.** Write precise definitions of: critical strip; critical line; trivial zero; non-trivial zero; RH.  
3. **PNT vs RH.** In your own words, what does the prime number theorem assert, and what extra information does RH concern?  
4. **Counterfactual.** Suppose someone announces a zero at $$s=0.6+1000i$$. Does that disprove RH? Does it disprove PNT?  
5. **Synthesis (seminar A3 practice).** In ≤400 words, explain RH to a classmate who knows calculus but not complex analysis: include Euler product, non-trivial zeros, and one sentence on prime counting errors.  
6. **Research literacy.** Skim the Clay Mathematics Institute official RH problem description and list the prize rules’ requirement (proof must be…?). Optional: identify one survey (Titchmarsh; Edwards; Ivić; or a modern expository article) and note its intended audience.

---

## From the video / survey path: partial theorems vs full RH

Popular lectures (Quanta/Kontorovich; Conrey; Vaaler) and surveys (Bombieri Clay description; Conrey Notices) share a clean split students should keep:

| Layer | What is known (slogans) | What remains open |
|-------|-------------------------|-------------------|
| No zeros on $$\operatorname{Re}(s)=1$$ | Equivalent (in standard form) to the **prime number theorem** | — |
| Zero-free regions near $$\operatorname{Re}(s)=1$$ | Classical and modern refinements control some error terms | Width still far from the critical line |
| Zeros *on* the critical line | Positive proportion results (Hardy–Littlewood → Selberg → Levinson → Conrey lineage) | **100%** of non-trivial zeros on the line |
| Function-field / finite-field analogues | Weil / Deligne: RH-type statements **proved** for zeta of curves (and more) over finite fields | Does not automatically transfer to $$\zeta(s)$$ |
| Numerical verification | Billions of zeros checked on the line | Evidence, **not** a proof |

**Status (as of 2026):** the Riemann Hypothesis for the classical zeta function remains **open**—one of the six unsolved Clay Millennium problems.

**Seminar extraction (LO1 / LO6):** write two sentences after any video: (1) what RH *says*; (2) what the video’s “evidence” actually is (computation, density theorem, or analogue)—never “they checked many zeros, so RH is true.”

---

## Mode C — reconstructed notes from flagship videos

*Reconstructed knowledge units (not transcript dumps). Cross-check against the written sections above and against Clay/Bombieri-style surveys. Captions live under `research/video-research/Riemann_Hypothesis/transcripts/`.*

### C1. Quanta / Kontorovich orientation (*The Riemann Hypothesis, Explained*)

Orientation talks fix three student-facing images that must stay separate:

1. **Euler product.** For $$\operatorname{Re}(s)>1$$, the identity connecting $$\zeta(s)$$ to primes is the reason zeros can control prime distribution—not a free bonus.  
2. **Analytic continuation.** The series definition is not the whole story: Riemann needs a function that agrees with the series where both make sense and is meaningful on a larger domain (including the critical strip). Popular “two functions, one identity region” language is a slogan for continuation, not a full uniqueness course.  
3. **The critical line as a claim.** RH asserts a location for non-trivial zeros. Visualizations of many zeros on the line are **evidence graphics**, not a proof. Large-scale numerical searches (billions or trillions of zeros on the line in computational reports) remain **finite checks**.

**LO6 trap:** “A computer checked many zeros, so RH is true.” → Evidence for those zeros; the universal claim is open.

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
13. Marcus du Sautoy, *The Music of the Primes* — popular history (use with LO6 critique).  

### Course

14. [Twin primes]({{ site.baseurl }}/contents/en/chapter01/01_06_Twin_Prime_Conjecture/), [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/), [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [Wang / Kakeya]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/). Research pack: `research/video-research/Riemann_Hypothesis/`.

---

## Further directions

- Seminar **A3**: RH is a natural open-problem brief—state it, explain hardness, name surrounding tools (explicit formulas, zero-free regions, analogues).  
- Compare the *culture* of RH (analytic number theory) with P vs NP (complexity) or Kakeya (harmonic analysis / GMT).  
- Optional: Quanta → Conrey lecture → re-read §§2–5 here.  
- Stretch: Dirichlet $$L$$-functions and GRH.
