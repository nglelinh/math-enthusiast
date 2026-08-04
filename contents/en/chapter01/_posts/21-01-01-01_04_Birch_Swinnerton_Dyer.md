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

Take a curve drawn by a cubic equation in two variables, look for points whose coordinates are rational numbers, and ask how many independent infinite families of such points exist. That integer—the **rank**—seems purely algebraic: it is about solving Diophantine equations. Now attach to the same curve an **$$L$$-function**, built from counting points over finite fields, and ask how many times that analytic function vanishes at the central point $$s=1$$. The **Birch and Swinnerton-Dyer (BSD) conjecture**, a Clay Millennium Prize Problem, asserts that these two numbers are equal.

In slogan form: *special values of $$L$$-functions encode arithmetic.* Riemann’s zeta encodes the primes; BSD says an elliptic curve’s $$L$$-function encodes its rational points. Same music, different instrument—and for elliptic curves over $$\mathbb{Q}$$, the score is still unfinished.

This essay maps elliptic curves and rank, $$L$$-functions and modularity, the BSD statements, partial theorems, and what cryptography does *not* need from the Millennium problem.

---

## Learning objectives

After this lecture you should be able to:

- Define an **elliptic curve** over $$\mathbb{Q}$$ at a working level (nonsingular Weierstrass cubic) and say what the group law does in slogan form.
- State the **Mordell–Weil theorem**: $$E(\mathbb{Q})$$ is finitely generated, and identify the **rank** $$r$$ as the free part.
- Explain how the **$$L$$-function** $$L(E,s)$$ is assembled from local factors, and why **modularity** makes it an entire (or at least globally analytic) object of the right kind.
- State BSD: $$\operatorname{ord}_{s=1} L(E,s) = r$$, and outline the refined leading-coefficient formula at slogan level (period, regulator, torsion, Tamagawa, Sha).
- Name major partial results: Coates–Wiles (CM, rank 0); Gross–Zagier / Kolyvagin for many rank $$\le 1$$ curves; computational checks; awareness of average-rank statistics (Bhargava et al.).
- Avoid a practical confusion (**LO6**): elliptic-curve cryptography uses the group law of an elliptic curve; it does **not** require BSD to be solved.

**Prerequisites.** Congruences and modular arithmetic; comfort with “group of points” as an algebraic structure (associative operation, identity, inverses). No algebraic geometry course is required—the geometric language stays light.

**Seminar links.** Course outcome **LO1**. Pair with [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) ($$L$$-functions); [Number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/) (ECC); [Fermat’s Last Theorem]({{ site.baseurl }}/contents/en/chapter05/05_08_Fermat_Last_Theorem/) (modularity / Wiles).

---

## 1. Elliptic curves: equations before geometry jargon

An **elliptic curve** over the rationals can, after a change of variables, be written in **Weierstrass form**

$$
y^2 = x^3 + Ax + B
$$

with $$A,B \in \mathbb{Q}$$. Not every cubic is allowed: the curve must be **nonsingular**. Concretely, the discriminant

$$
\Delta = -16(4A^3 + 27B^2)
$$

must be nonzero (for this short Weierstrass model). If $$\Delta = 0$$, the cubic and its derivative share a root and the curve has a cusp or node—singular points break the beautiful group law below.

“Elliptic” does **not** mean “ellipse.” The name is historical (elliptic integrals, elliptic functions). The object is a smooth genus-one curve with a distinguished point—the **point at infinity** $$O$$ on the projective model. Over $$\mathbb{Q}$$ we care about points $$(x,y)$$ with rational coordinates, together with $$O$$.

---

## 2. The group law: chord, tangent, and infinity

The set $$E(\mathbb{Q})$$ of rational points (including $$O$$) carries an abelian group structure, the **chord-and-tangent law**:

- To add $$P$$ and $$Q$$, draw the line through them (the tangent if $$P=Q$$). It meets the cubic at a third point $$R'$$. Reflect $$R'$$ across the $$x$$-axis to get $$P+Q$$.
- The identity is $$O$$: “vertical lines through a point and its reflection meet at infinity.”
- Negation is reflection in the $$x$$-axis: $$-(x,y) = (x,-y)$$.

Associativity is the nontrivial algebraic fact. Once accepted, $$E(\mathbb{Q})$$ is an ordinary abelian group, so the toolkit of finitely generated abelian groups applies.

**Worked micro-example.** On $$y^2 = x^3 - 2$$, the point $$P = (3,5)$$ is rational: $$5^2 = 25 = 3^3 - 2$$. Doubling and adding $$P$$ produces further rational points (often with huge denominators). Finding a full set of *generators* is much harder than verifying one point.

---

## 3. Mordell–Weil: finite generation and rank

**Mordell–Weil theorem (over $$\mathbb{Q}$$).** For an elliptic curve $$E/\mathbb{Q}$$,

$$
E(\mathbb{Q}) \cong \mathbb{Z}^{r} \oplus E(\mathbb{Q})_{\mathrm{tors}}.
$$

That is: the group of rational points is **finitely generated**. The torsion subgroup $$E(\mathbb{Q})_{\mathrm{tors}}$$ is finite; over $$\mathbb{Q}$$ its possible structures were classified by **Mazur**. The integer $$r \ge 0$$ is the **rank**—the number of independent infinite-order points needed to generate the free part.

What rank measures: $$r=0$$ means only finitely many rational points (all torsion); $$r=1$$ means one infinite-order generator (plus torsion) produces infinitely many points via multiples $$nP$$; $$r\ge 2$$ means at least two independent infinite families.

Computing $$r$$ is subtle—points can have enormous height and still be generators. Algorithms use search and **descent**, often proving upper and lower bounds that only later match. A deep obstruction is the **Tate–Shafarevich group** $$Ш(E/\mathbb{Q})$$ (Sha): it measures failures of local-to-global principles for principal homogeneous spaces under $$E$$. Sha is conjecturally finite; that finiteness is tied to BSD machinery and is known in important cases, not historically for all $$E$$ as a free-standing theorem.

---

## 4. The $$L$$-function: local factors, Euler product, modularity

To each elliptic curve $$E/\mathbb{Q}$$ one attaches an **$$L$$-function** $$L(E,s)$$. At a prime $$p$$ of good reduction, reduce the Weierstrass equation modulo $$p$$ and count points over the finite field $$\mathbb{F}_p$$. Write

$$
a_p = p + 1 - \#E(\mathbb{F}_p)
$$

(with standard adjustments at primes of bad reduction). The local Euler factor is essentially $$1 - a_p p^{-s} + p^{1-2s}$$ (good ordinary case), and

$$
L(E,s) = \prod_p L_p(E,s)^{-1}
$$

is an Euler product, convergent for $$\operatorname{Re}(s)$$ large enough—the same formal spirit as the Euler product for zeta, but with coefficients recording the arithmetic of $$E$$ mod $$p$$.

For the product alone, $$L(E,s)$$ is only defined in a half-plane. The **modularity theorem**—Wiles for semistable curves (in the proof of Fermat’s Last Theorem); completed for all $$E/\mathbb{Q}$$ by Breuil–Conrad–Diamond–Taylor—identifies $$L(E,s)$$ with the $$L$$-function of a weight-2 newform. That supplies **analytic continuation** (an entire function) and a **functional equation** relating $$s$$ to $$2-s$$. The central point for BSD is $$s=1$$.

Modularity is not a side note: without a global analytic object, “order of vanishing at $$s=1$$” is not a clean question. Modularity builds the stage; BSD is the arithmetic play—and the play is still open.

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

(up to the precise normalization conventions in textbooks). Here:

- $$\Omega$$ is a **real period** (integral of a Néron differential over the real components);
- $$\operatorname{Reg}$$ is the **regulator** of a basis of the free part (determinant of the Néron–Tate height pairing);
- $$\# E(\mathbb{Q})_{\mathrm{tors}}$$ is the order of the torsion subgroup;
- $$c_p$$ are **Tamagawa numbers** (local indices measuring bad reduction);
- $$\#Ш$$ is the order of the Tate–Shafarevich group (conjecturally finite).

The refined formula matters as much as the rank equality: it predicts not only *how many* independent points exist, but a precise **measure** of their size, and it makes Sha a concrete integer rather than a pure obstruction.

---

## 6. Why the conjecture is hard

**Two languages.** Rank is Diophantine and global; $$L$$-functions are analytic and built from local counts. Bridging them needs Heegner points, Euler systems, Iwasawa theory, modularity lifting—not a rearrangement of the Weierstrass equation.

**Sha is elusive.** Bounding Selmer groups is not the same as proving finiteness of Sha or reading off exact ranks. Computational checks of the refined formula often assume or conditionally control Sha.

**High rank is rare.** Large-rank curves exist but are hard to certify; the distribution of ranks is a research industry, not a closed chapter.

**History of the stage.** Full modularity for every $$E/\mathbb{Q}$$ is late-20th / early-21st century; Birch and Swinnerton-Dyer formulated the conjecture from 1960s numerics before the analytic stage was completely built.

Hardness means **resistance of the full statement**, not an empty subject—low-rank partial theorems are crown jewels of modern number theory.

---

## 7. Evidence and partial results

**Numerical checks.** Cremona tables and LMFDB record ranks, torsion, and special values of $$L$$. For vast numbers of curves, analytic and algebraic ranks match, and the refined formula holds to high precision when Sha is controlled. Strong evidence—not a universal proof.

**Coates–Wiles.** For certain **complex multiplication** (CM) curves, Coates–Wiles and related work prove BSD-type results in rank-zero settings: vanishing of $$L(E,1)$$ links to the absence of infinite-order points in the cases covered.

**Gross–Zagier and Heegner points.** Gross–Zagier relates $$L'(E,1)$$ to the Néron–Tate height of a **Heegner point** from imaginary quadratic fields. When $$L(E,1)=0$$ but $$L'(E,1)\ne 0$$, one obtains a rational point of infinite order.

**Kolyvagin Euler systems.** Euler systems built from Heegner points control Selmer groups and yield BSD for many curves of analytic rank 0 and 1: under the method’s hypotheses, algebraic rank equals analytic rank and Sha is finite of predicted order when the analytic rank is at most 1.

Together, Gross–Zagier + Kolyvagin give a substantial **rank $$\le 1$$** theory. Higher analytic rank remains far harder.

**Averages.** Bhargava, Shankar, and collaborators on average ranks (and Selmer averages), with related work of Skinner–Urban, Zhang, and others, reshape “typical” rank: most curves are expected to have rank 0 or 1, with deep progress on averages even while individual high-rank BSD stays open.

**Status (2026).** BSD is **still open** in full generality—one of the six unsolved Millennium problems (only Poincaré is solved, by Perelman).

---

## 8. Sister philosophy: special values encode arithmetic

BSD sits in a web with **class number formulas**, **Bloch–Kato** conjectures, and the culture that “$$L$$-functions know arithmetic.” [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) is the prime-distribution face; BSD is the elliptic-curve face. If RH is about *where* zeros lie, BSD is about *how deep* a zero sits at a fixed central point—and what that depth means for rational points.

---

## 9. Cryptography does not need BSD solved (LO6)

Elliptic-curve cryptography uses $$E(\mathbb{F}_q)$$ over a **finite field**, not primarily $$E(\mathbb{Q})$$. Security rests on discrete-log hardness in carefully chosen groups. Implementers need nonsingular curves, large prime-order subgroups, and attack resistance—not a proof that algebraic rank equals analytic rank over $$\mathbb{Q}$$.

| Practice (ECC) | Millennium BSD |
|----------------|----------------|
| Group law over finite fields | Rank of $$E(\mathbb{Q})$$ vs $$\operatorname{ord}_{s=1} L(E,s)$$ |
| Discrete log hardness | Analytic–algebraic equality and refined formula |
| Curve selection criteria | Sha, regulators, Tamagawa numbers |

**Using** elliptic curves and **settling** BSD are different games. Chapter 3 develops ECC; this essay only insists on the LO6 boundary.

---

## From lectures: what rank ≤ 1 theorems actually give

Bhargava’s Abel exposition and Mazur’s Clay/CMSA lecture (2026) both emphasize a split students must keep for LO1:

- **Stage setting (proved for all $$E/\mathbb{Q}$$):** modularity ⇒ $$L(E,s)$$ has analytic continuation and a functional equation, so the **analytic rank** $$\operatorname{ord}_{s=1} L(E,s)$$ is defined.
- **Low-rank arithmetic (large partial theory):** Gross–Zagier + Kolyvagin (and CM ancestors such as Coates–Wiles) give BSD-type conclusions for many curves of analytic rank $$0$$ or $$1$$: algebraic rank matches analytic rank, and Sha is finite of the predicted order under the method’s hypotheses.
- **Still open:** arbitrary rank; the full refined formula for every $$E/\mathbb{Q}$$; a uniform algorithm-free picture of high-rank Sha.

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

## Exercises

1. For $$y^2 = x^3 - 2$$, verify that $$(3,5)$$ is a rational point. Explain in one sentence what “rank at least 1” would mean if $$(3,5)$$ has infinite order.
2. Restate the Mordell–Weil theorem in plain English without symbols, then rewrite it with the isomorphism $$E(\mathbb{Q})\cong \mathbb{Z}^r \oplus E(\mathbb{Q})_{\mathrm{tors}}$$.
3. What does $$\operatorname{ord}_{s=1} L(E,s) = 0$$ predict about rational points of infinite order, according to BSD?
4. Why does the discriminant condition $$\Delta \ne 0$$ matter for the group law story?
5. **LO1 synthesis (≤350 words):** state BSD (rank part), say why it is hard, and name two surrounding tools (modularity; Heegner points / Kolyvagin).
6. **LO6 boundary.** In three sentences, distinguish “elliptic curves in cryptography” from “BSD as a Millennium problem.”
7. One sentence linking BSD to RH-style thinking about zeros or orders of vanishing of $$L$$-functions.
8. Stretch: open LMFDB or Cremona tables, pick one curve, and record its rank, torsion, and whether $$L(E,1)$$ is reported as zero or nonzero.

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
