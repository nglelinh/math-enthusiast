---
layout: post
title: "The Birch and Swinnerton-Dyer Conjecture"
chapter: '01'
order: 4
owner: Nguyen Le Linh
lang: en
categories:
- chapter01
lesson_type: required
---

In the early 1960s, two young mathematicians at Cambridge—Bryan Birch and Peter Swinnerton-Dyer—sat in front of EDSAC-2, a room-sized vacuum-tube computer that was one of the earliest electronic machines in the world. They were chasing a question as old as ancient Greece: given a cubic equation $$y^2 = x^3 + Ax + B$$, how can you tell whether it has *finitely many* or *infinitely many* rational solutions?

Searching for rational solutions directly is brutally hard, because even the simplest solution can have numerators and denominators dozens of digits long. So they tried a clever detour: instead of hunting over all of $$\mathbb{Q}$$, they asked EDSAC-2 to count solutions modulo primes $$p = 2, 3, 5, 7, \ldots$$—a finite task computers handle effortlessly. Plotting the resulting data revealed an astonishing whisper: **curves with more rational points seemed to have systematically more solutions modulo $$p$$, and that abundance showed up directly in how deeply an analytic function vanished at $$s = 1$$!**

That daring computational discovery became the **Birch and Swinnerton-Dyer (BSD) conjecture**, one of the Clay Millennium Prize Problems. It builds a breathtaking bridge between two worlds of an elliptic curve over $$\mathbb{Q}$$:

- an **algebraic** invariant: the **rank** $$r$$ of its group of rational points;
- an **analytic** invariant: the order of vanishing of its **$$L$$-function** at the central point $$s = 1$$.

In slogan form: *special values of $$L$$-functions encode arithmetic.* Riemann’s zeta encodes the primes; BSD says an elliptic curve’s $$L$$-function encodes its rational points. Same music, different instrument—and for elliptic curves over $$\mathbb{Q}$$, the score is still unfinished.

---

## Learning objectives

After this lecture you should be able to:

- Define an **elliptic curve** over $$\mathbb{Q}$$ at a working level (nonsingular Weierstrass cubic) and explain the chord-and-tangent group law.
- State the **Mordell–Weil theorem**: $$E(\mathbb{Q})$$ is finitely generated, and identify the **rank** $$r$$ as the free part.
- Explain how the **$$L$$-function** $$L(E,s)$$ is assembled from local mod-$$p$$ point counts, and why **modularity** supplies its analytic continuation.
- State BSD: $$\operatorname{ord}_{s=1} L(E,s) = r$$, and outline the refined leading-coefficient formula (period, regulator, torsion, Tamagawa numbers, Sha).
- Name major partial results: Coates–Wiles; Gross–Zagier / Kolyvagin for rank $$\le 1$$; computational checks; average-rank theorems (Bhargava et al.).
- Distinguish elliptic-curve cryptography (ECC over finite fields) from the Millennium BSD problem (arithmetic over $$\mathbb{Q}$$).

**Prerequisites.** Congruences and modular arithmetic; comfort with “group of points” as an algebraic structure. No algebraic geometry course is required.

**Course connections.** Pair with [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) ($$L$$-functions), [Number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/) (ECC), and [Fermat’s Last Theorem]({{ site.baseurl }}/contents/en/chapter05/05_08_Fermat_Last_Theorem/) (modularity / Wiles).

---

## Background Knowledge Map: Algebraic Geometry, Arithmetic Geometry, and $$L$$-Functions

To a university graduate trained in linear algebra and calculus, *algebraic geometry* and *arithmetic geometry* can sound intimidating—yet they rest on three approachable pillars:

### 1. Algebraic Geometry
Linear algebra studies solution sets of *degree-1* equations (lines, planes, subspaces). **Algebraic geometry** steps up to higher degrees: shapes defined by **polynomial equations** of degree 2, 3, or higher (circles $$x^2+y^2=1$$, cubics $$y^2 = x^3 + Ax + B$$, higher-dimensional varieties). Its signature strength is two-way translation—turning dry algebra into visual geometry (curvature, intersections, symmetry), and using algebra to compute geometric invariants exactly. Beyond pure math, it underpins robot kinematics, 3D computer vision, satellite error-correcting codes, and cryptography.

### 2. Arithmetic Geometry & Diophantine Equations
In ordinary geometry, we look for real points $$(x,y) \in \mathbb{R}^2$$ forming a smooth curve. **Arithmetic geometry** asks a vastly harder question: *which points on that curve have rational (or integer) coordinates?* For degree 2 (like the circle $$x^2+y^2=1$$), antiquity already solved the problem completely via Pythagorean triples. Stepping up just one degree to **degree 3**—elliptic curves—lands us straight at the frontier of modern mathematics, home to Fermat's Last Theorem and BSD.

### 3. $$L$$-Functions and Modular Forms (The Analytic–Arithmetic Bridge)
Because finding global rational points over $$\mathbb{Q}$$ is so difficult, mathematicians gather the finite point counts **modulo every prime $$p$$** into a single complex function—the **$$L$$-function** $$L(E,s)$$. Thanks to the **Modularity Theorem**, this $$L$$-function matches a highly symmetric analytic wave (a *modular form*), letting us extend it across the complex plane and inspect its behavior right at $$s = 1$$.

---

## 1. Elliptic curves: equations before geometry jargon

An **elliptic curve** over the rationals can, after a change of variables, be written in **Weierstrass form**

$$
y^2 = x^3 + Ax + B
$$

with $$A,B \in \mathbb{Q}$$ and nonzero discriminant

$$
\Delta = -16(4A^3 + 27B^2) \neq 0.
$$

If $$\Delta = 0$$, the curve develops a sharp cusp or self-intersection that breaks the group law. “Elliptic” does **not** mean “ellipse”—the name comes historically from elliptic integrals measuring arc length of ellipses.

---

## 2. The group law: chord, tangent, and infinity

The set $$E(\mathbb{Q})$$ of rational points (together with the **point at infinity** $$\mathcal{O}$$, acting as zero) carries an abelian group structure via the **chord-and-tangent law**: draw the line through $$P$$ and $$Q$$ (the tangent line if $$P = Q$$); because the equation is cubic, it meets the curve at a third rational point $$R$$; reflect $$R$$ across the $$x$$-axis to obtain $$P + Q$$.

### Worked Example 1: Doubling a Rational Point by Hand on $$y^2 = x^3 - 2$$

Take $$E: y^2 = x^3 - 2$$ and spot the neat integer point $$P = (3, 5)$$, since $$5^2 = 25 = 3^3 - 2$$. Let us compute $$2P$$ step by step using first-year calculus:

1. **Slope of the tangent line:** Implicit differentiation gives $$2y\,y' = 3x^2 \implies m = \frac{3 \cdot 3^2}{2 \cdot 5} = \frac{27}{10}$$.
2. **Tangent line equation:** $$y = \frac{27}{10}(x - 3) + 5 = \frac{27}{10}x - \frac{31}{10}$$.
3. **Third intersection point:** Substituting into $$y^2 = x^3 - 2$$ gives a cubic $$x^3 - m^2 x^2 + \cdots = 0$$ with a double root at $$x = 3$$. By Vieta's formula (sum of the three roots equals $$m^2$$):
   $$
   x_{2P} = m^2 - 2\cdot 3 = \frac{729}{100} - 6 = \frac{129}{100}.
   $$
4. **Reflect across the $$x$$-axis:** Plugging $$x_{2P}$$ into the tangent gives $$y = \frac{27}{10}\cdot\frac{129}{100} - \frac{31}{10} = \frac{383}{1000}$$; flipping its sign yields:
   $$
   2P = \left(\frac{129}{100},\, -\frac{383}{1000}\right).
   $$

Check it directly: $$\left(\frac{129}{100}\right)^3 - 2 = \frac{2\,146\,689 - 2\,000\,000}{1\,000\,000} = \frac{146\,689}{1\,000\,000} = \left(-\frac{383}{1000}\right)^2$$! Starting from a tiny integer point $$(3,5)$$, a single doubling explodes the denominator to 1,000—and repeating $$3P, 4P, \ldots$$ generates infinitely many rational points of rapidly growing height. (Another classic connection: the *congruent number problem*—which integers $$n$$ are areas of rational right triangles—turns out to ask whether $$y^2 = x^3 - n^2 x$$ has positive rank; e.g., $$n = 6$$ corresponds to the $$3\text{-}4\text{-}5$$ right triangle!)

---

## 3. Mordell–Weil: finite generation and rank

**Mordell–Weil theorem (over $$\mathbb{Q}$$).** For an elliptic curve $$E/\mathbb{Q}$$,

$$
E(\mathbb{Q}) \cong \mathbb{Z}^{r} \oplus E(\mathbb{Q})_{\mathrm{tors}}.
$$

The group of rational points is **finitely generated**. The torsion subgroup $$E(\mathbb{Q})_{\mathrm{tors}}$$ is finite (classified by **Mazur**: at most 16 points over $$\mathbb{Q}$$). The integer $$r \ge 0$$ is the **rank**—the number of independent infinite-order generators.

Computing $$r$$ is subtle—generators can have enormous height. A deep obstruction is the **Tate–Shafarevich group** $$Ш(E/\mathbb{Q})$$ (Sha), measuring failures of the local-to-global principle. Sha is conjecturally finite, a fact proved in key low-rank cases but still open in general.

---

## 4. The $$L$$-function: local factors, Euler product, modularity

### Worked Example 2: Counting Points Modulo $$p$$ by Hand on $$y^2 = x^3 - 2$$

Finding rational points over $$\mathbb{Q}$$ is hard, but counting points **modulo a prime $$p$$** is finite and easy! Let us do $$p = 5$$ and $$p = 7$$ on $$E: y^2 = x^3 - 2$$:

- **At $$p = 5$$** (squares mod 5 are $$0, 1, 4$$):
  - $$x=0 \implies x^3-2 \equiv 3 \pmod 5$$ (no square root: 0 points)
  - $$x=1 \implies x^3-2 \equiv 4 = (\pm 2)^2 \pmod 5$$ → **2 points**: $$(1,2), (1,3)$$
  - $$x=2 \implies x^3-2 \equiv 6 \equiv 1 = (\pm 1)^2 \pmod 5$$ → **2 points**: $$(2,1), (2,4)$$
  - $$x=3 \implies x^3-2 \equiv 25 \equiv 0 = 0^2 \pmod 5$$ → **1 point**: $$(3,0)$$
  - $$x=4 \implies x^3-2 \equiv 62 \equiv 2 \pmod 5$$ (0 points)
  - Adding the point at infinity $$\mathcal{O}$$ gives $$N_5 = 5 + 1 = 6$$ points, so $$a_5 = (5 + 1) - N_5 = 0$$.

- **At $$p = 7$$** (squares mod 7 are $$0, 1, 2, 4$$):
  - For $$x \in \{0, 1, 2, 4\}$$: $$x^3 - 2 \pmod 7$$ gives $$5, 6, 6, 6$$ (none are squares: 0 points).
  - For $$x \in \{3, 5, 6\}$$: $$x^3 - 2 \pmod 7$$ equals $$4 = (\pm 2)^2$$ in all three cases → 6 finite points $$(3,2),(3,5),(5,2),(5,5),(6,2),(6,5)$$.
  - Adding $$\mathcal{O}$$ gives $$N_7 = 6 + 1 = 7$$ points, so $$a_7 = (7 + 1) - N_7 = 1$$.

Packaging every good prime's $$a_p = p + 1 - N_p$$ (plus standard bad-prime adjustments) into an Euler product yields the **$$L$$-function**:

$$
L(E,s) = \prod_{p\ \text{bad}} L_p(E,s)^{-1} \cdot \prod_{p\ \text{good}} \frac{1}{1 - a_p p^{-s} + p^{1-2s}}.
$$

### Deep-Dive Explanation: Why Counting Points Mod $$p$$ Reveals Global Rational Points (Read Slowly)

How can finite mod-$$p$$ counts know the number of infinite-order rational generators over $$\mathbb{Q}$$? Follow these four steps:

#### Step 1: Local counts $$N_p$$ feel global abundance
If $$E(\mathbb{Q})$$ has many independent rational points (large rank $$r$$), reducing those rational points modulo $$p$$ tends to populate $$E(\mathbb{F}_p)$$ with *more* points than the baseline average $$p$$ (so $$N_p > p$$ more often than not).

#### Step 2: Plugging $$s = 1$$ formally into the Euler product
Look at a single good Euler factor when you substitute $$s = 1$$:
$$
\frac{1}{1 - a_p p^{-1} + p^{-1}} = \frac{p}{p + 1 - a_p} = \frac{p}{N_p}!
$$
Every factor is literally $$\frac{p}{N_p}$$! Whenever $$N_p$$ systematically exceeds $$p$$, each fraction $$\frac{p}{N_p}$$ is slightly less than $$1$$, and multiplying infinitely many numbers below $$1$$ drags $$L(E,s)$$ **down to 0 at $$s = 1$$**—the higher the rank, the faster it plunges to zero!

#### Step 3: Modularity makes $$s = 1$$ rigorous
The Euler product itself only converges for $$\operatorname{Re}(s) > 3/2$$, stopping short of $$s = 1$$. The **Modularity Theorem** (Wiles; Breuil–Conrad–Diamond–Taylor) proves that $$L(E,s)$$ equals the $$L$$-function of a weight-2 modular form, giving **analytic continuation** to the entire complex plane and a functional equation symmetric about $$s = 1$$.

#### Step 4: Equality of two worlds (BSD)
BSD conjectures that the heuristic from Step 2 is **exact**: the analytic order of vanishing at $$s = 1$$ does not merely correlate with the algebraic rank $$r$$—it equals $$r$$ identically!

---

## 5. Statement of BSD

**BSD (rank part).** For an elliptic curve $$E/\mathbb{Q}$$,

$$
\operatorname{ord}_{s=1} L(E,s) = r = \operatorname{rank}\, E(\mathbb{Q}).
$$

The left side is analytic (multiplicity of the zero of $$L$$ at the central point). The right side is algebraic (free rank of rational points). Equality is the conjecture.

**BSD (refined part).** Write the Taylor expansion

$$
L(E,s) = c\, (s-1)^{r} + \text{higher-order terms},
$$

with leading coefficient $$c \ne 0$$. BSD predicts an exact formula for $$c$$ as a product of arithmetic invariants, schematically

$$
c = \frac{\Omega \cdot \operatorname{Reg} \cdot \#Ш \cdot \prod_p c_p}{(\# E(\mathbb{Q})_{\mathrm{tors}})^2}
$$

(up to standard normalization conventions). Here $$\Omega$$ is the **real period**, $$\operatorname{Reg}$$ is the **regulator** (determinant of the Néron–Tate height pairing), $$\# E(\mathbb{Q})_{\mathrm{tors}}$$ is the torsion order, $$c_p$$ are **Tamagawa numbers**, and $$\#Ш$$ is the order of the Tate–Shafarevich group (conjecturally finite).

The refined formula matters as much as the rank equality: it predicts not only *how many* independent points exist, but a precise **measure** of their arithmetic size, turning Sha into a concrete integer rather than a pure obstruction.

---

## 6. Why the conjecture is hard

**Two languages.** Rank is Diophantine and global; $$L$$-functions are analytic and built from local counts. Bridging them requires Heegner points, Euler systems, Iwasawa theory, and modularity lifting.

**Sha is elusive.** Bounding Selmer groups is not the same as proving finiteness of Sha or reading off exact ranks.

**High rank is rare.** Large-rank curves exist (the current record, found by Elkies and Klagsbrun in 2024, has rank at least 29) but are hard to certify; the distribution of ranks is an active research frontier.

**History of the stage.** Full modularity for every $$E/\mathbb{Q}$$ was only completed around 2001; Birch and Swinnerton-Dyer formulated the conjecture from 1960s numerics decades before the analytic stage was completely built.

---

## 7. Evidence and partial results

**Numerical checks.** Cremona tables and LMFDB record ranks, torsion, and special values of $$L$$ for millions of curves. Analytic and algebraic ranks match across vast datasets, and the refined formula holds to high precision when Sha is controlled. Strong evidence—not a universal proof.

**Coates–Wiles (1977).** For curves with **complex multiplication (CM)**, Coates and Wiles proved BSD in the rank-0 case: $$L(E,1) \neq 0$$ implies only finitely many rational points.

**Gross–Zagier and Heegner points (1986).** Gross and Zagier linked $$L'(E,1)$$ directly to the Néron–Tate height of a **Heegner point** constructed from modular forms. When $$L(E,1)=0$$ and $$L'(E,1)\ne 0$$, that point has nonzero height—explicitly constructing a rational point of infinite order!

**Kolyvagin Euler systems (1988).** Euler systems built from Heegner points control Selmer groups and establish BSD (and finiteness of Sha) for all elliptic curves over $$\mathbb{Q}$$ of analytic rank 0 or 1.

Together, Gross–Zagier + Kolyvagin give a magnificent **rank $$\le 1$$** theory. For analytic rank $$\ge 2$$, Heegner points vanish identically and new tools are needed.

**Averages.** Bhargava, Shankar, and collaborators—alongside Skinner–Urban, Wei Zhang, and others—proved that a positive proportion (over 66%) of all elliptic curves over $$\mathbb{Q}$$ satisfy BSD (via rank 0 or 1), while individual high-rank curves remain open.

**Status (2026).** BSD is **still open** in full generality—one of the six unsolved Millennium problems (only Poincaré is solved, by Perelman).

---

## 8. Sister philosophy: special values encode arithmetic

BSD sits in a web with **class number formulas**, **Bloch–Kato** conjectures, and the culture that “$$L$$-functions know arithmetic.” [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) is the prime-distribution face; BSD is the elliptic-curve face. If RH asks *where* zeros lie, BSD asks *how deep* a zero sits at $$s=1$$—and what that depth means for rational points.

---

## 9. Cryptography does not need BSD solved

Elliptic-curve cryptography (**ECC**) uses the finite group $$E(\mathbb{F}_q)$$ over a **finite field**, not $$E(\mathbb{Q})$$. Security rests on discrete-log hardness in carefully chosen groups. Implementers need nonsingular curves, large prime-order subgroups, and attack resistance—not a proof that algebraic rank equals analytic rank over $$\mathbb{Q}$$.

| Practice (ECC) | Millennium BSD |
|----------------|----------------|
| Group law over finite fields | Rank of $$E(\mathbb{Q})$$ vs $$\operatorname{ord}_{s=1} L(E,s)$$ |
| Discrete log hardness | Analytic–algebraic equality and refined formula |
| Curve selection criteria | Sha, regulators, Tamagawa numbers |

**Using** elliptic curves and **settling** BSD are different games: **same geometric object, different arithmetic question**. Chapter 3 develops ECC in detail.

---

## From lectures: what rank ≤ 1 theorems actually give

Bhargava’s Abel exposition and Mazur’s Clay/CMSA lecture (2026) both emphasize a clean three-tier split:

- **Stage setting (proved for all $$E/\mathbb{Q}$$):** modularity ⇒ $$L(E,s)$$ has analytic continuation and a functional equation, so the **analytic rank** $$\operatorname{ord}_{s=1} L(E,s)$$ is defined.
- **Low-rank arithmetic (large partial theory):** Gross–Zagier + Kolyvagin (and CM ancestors such as Coates–Wiles) give BSD-type conclusions for curves of analytic rank $$0$$ or $$1$$.
- **Still open:** arbitrary rank; the full refined formula for every $$E/\mathbb{Q}$$; a uniform picture of high-rank Sha.

**Status (as of 2026):** BSD remains **open** as a Clay Millennium problem in full generality—even while rank-$$\le 1$$ theory is a crown jewel of modern number theory.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Elliptic curve means ellipse.” | Historical name; the object is a nonsingular cubic of genus one with a rational point (at infinity). |
| “BSD is about drawing curves.” | It is about arithmetic of rational points and analysis of $$L$$-functions. |
| “Modularity finished BSD.” | Modularity supplies analytic continuation of $$L(E,s)$$; the rank equality remains open. |
| “Rank is easy: just find points.” | Finding and proving a full set of generators can be extremely hard; Sha and heights intervene. |
| “ECC is unsafe until BSD is proved.” | ECC uses finite-field groups; it does not depend on the Millennium statement over $$\mathbb{Q}$$. |
| “Analytic rank 0 means no rational points.” | It predicts no *infinite-order* rational points; torsion points may still exist. |

---

## Video sources (math-video-researcher pack)

Full ranking and notes: `research/video-research/Birch_Swinnerton_Dyer/`.

**Recommended order**

1. **Orientation** — Manjul Bhargava (Abel Prize), *What is the Birch-Swinnerton-Dyer Conjecture?*: [YouTube](https://www.youtube.com/watch?v=_-feKGb6-gc).  
2. **Foundation** — Richard Borcherds, *BSD: Introduction*: [YouTube](https://www.youtube.com/watch?v=3vGiWK_ZyKs).  
3. **Core research culture** — Barry Mazur, *About the Birch and Swinnerton–Dyer Conjecture* (Harvard CMSA / Clay lecture, 2026): [YouTube](https://www.youtube.com/watch?v=14-9iCoclFE) · [event page](https://cmsa.fas.harvard.edu/event/clay_2426/).  
4. **Written official** — Clay BSD page: [claymath.org](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/).  
5. **Database studio** — [LMFDB](https://www.lmfdb.org/).

**After videos:** modularity builds the stage; rank-$$\le 1$$ theorems are deep partial results; full BSD is **open** as of 2026. ECC does **not** wait on the prize.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Birch_Swinnerton_Dyer/transcripts/` · status: `research/video-research/Birch_Swinnerton_Dyer/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Birch_Swinnerton_Dyer__-feKGb6-gc_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full bibliography: `research/video-research/Birch_Swinnerton_Dyer/references.md`.

### Official and books

1. Clay — [Birch and Swinnerton-Dyer Conjecture](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/) · [BSD at 25 lecture note](https://www.claymath.org/lectures/the-birch-swinnerton-dyer-conjecture-a-millennium-prize-problem-at-25/).  
2. J. H. Silverman — *The Arithmetic of Elliptic Curves*; Silverman–Tate — *Rational Points on Elliptic Curves*.  
3. Wikipedia — [BSD conjecture](https://en.wikipedia.org/wiki/Birch_and_Swinnerton-Dyer_conjecture).  
4. LMFDB — https://www.lmfdb.org/ ; Cremona tables.  
5. Gross–Zagier; Kolyvagin Euler systems; Coates–Wiles (CM); Wiles modularity / BCDT.

### Videos

6. Bhargava Abel lecture: https://www.youtube.com/watch?v=_-feKGb6-gc  
7. Borcherds BSD intro: https://www.youtube.com/watch?v=3vGiWK_ZyKs  
8. Mazur CMSA 2026: https://www.youtube.com/watch?v=14-9iCoclFE  
9. Mazur site: https://sites.harvard.edu/barry-mazur/  

### Course

10. [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/), [Cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/), [FLT]({{ site.baseurl }}/contents/en/chapter05/05_08_Fermat_Last_Theorem/). Pack: `research/video-research/Birch_Swinnerton_Dyer/`.

---

## Further directions

- Seminar **A3**: rank equality, modularity as stage-setting, Gross–Zagier/Kolyvagin for rank $$\le 1$$, refined formula with Sha.  
- Optional studio: LMFDB ranks 0 and 1—what BSD predicts for $$L(E,1)$$ and $$L'(E,1)$$.  
- Stretch: class number formula as special-value sibling; twin primes as sieve neighbor in this chapter.

## Video tham khảo

- **xem trước** — [Manjul Bhargava: What is the Birch-Swinnerton-Dyer Conjecture, and what is known about it?](https://www.youtube.com/watch?v=_-feKGb6-gc) — The Abel Prize, English. Watch first. “Manjul Bhargava: What is the Birch-Swinnerton-Dyer Conjecture, and what is known about it?” orients the lesson’s aim: Define an elliptic curve over \mathbb{Q} at a working level (nonsingular Weierstrass cubic) and say what the group law does in slogan form.
- [Birch Swinnerton-Dyer conjecture: Introduction](https://www.youtube.com/watch?v=3vGiWK_ZyKs) — Richard E Borcherds, English. A second pass once the main claim is in view: Define an elliptic curve over \mathbb{Q} at a working level (nonsingular Weierstrass cubic) and say what the group law does in slogan form.
- [Barry Mazur | About the Birch and Swinnerton–Dyer Conjecture](https://www.youtube.com/watch?v=14-9iCoclFE) — Harvard CMSA, English. Further depth after the first two, still tied to this lesson: Define an elliptic curve over \mathbb{Q} at a working level (nonsingular Weierstrass cubic) and say what the group law does in slogan form.
