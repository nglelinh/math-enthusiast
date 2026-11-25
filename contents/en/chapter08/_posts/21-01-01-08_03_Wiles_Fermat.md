---
layout: post
title: "Andrew Wiles: Modularity and Fermat’s Last Theorem (Abel 2016)"
chapter: '08'
order: 3
owner: Nguyen Le Linh
lang: en
categories:
- chapter08
lesson_type: required
---

In 1963, a ten-year-old boy in Cambridge pulled a math book off a public library shelf and stumbled across a puzzle any grade-schooler could state: are there positive whole numbers satisfying $$a^n + b^n = c^n$$ when $$n \ge 3$$? Three hundred years earlier, Pierre de Fermat had scribbled in the margin of an ancient book that he had a "truly marvelous proof," only the margin was too narrow to hold it. For more than three centuries, generations of great mathematicians and passionate amateurs tried and failed. That ten-year-old boy, **Andrew Wiles**, made himself a quiet promise that one day he would solve it.

More than thirty years later—after seven years of near-secret work in his Princeton attic and a nerve-wracking year repairing a subtle gap alongside his former student Richard Taylor—Wiles did what many had begun to think impossible. In **2016**, **Sir Andrew J. Wiles** (University of Oxford) received the **Abel Prize**:

> “for his stunning proof of Fermat’s Last Theorem by way of the modularity conjecture for semistable elliptic curves, opening a new era in number theory.”  
> — [Abel Prize Committee citation](https://abelprize.no/abel-prize-laureates/2016)

What makes the story truly remarkable sits in the second half of that citation: Wiles did not crack Fermat’s equation head-on with clever divisibility tricks. Instead, he sailed across a seemingly unrelated continent of mathematics—the world of **elliptic curves** and **modular forms**—and built machinery that reshaped modern number theory. Official materials live at [abelprize.no](https://abelprize.no/).

**Lesson arc:** Key ideas (Diophantine equations, elliptic curves, modular forms) → The 350-year puzzle → The Frey curve → Modularity and a hand-checked "matching DNA" calculation → The 5-step contradiction skeleton → Galois representations and $$R = \mathbb{T}$$ → Real history and common confusions.

---

## Learning objectives

After this lecture you should be able to state FLT precisely for integers $$n\ge 3$$; explain the Frey curve → Ribet → modularity → contradiction strategy at idea level; distinguish Wiles’s semistable modularity advance from the later full modularity theorem of Breuil–Conrad–Diamond–Taylor; connect modularity to Galois representations and $$L$$-functions at slogan level; and avoid confusing “FLT is proved” with “all Diophantine problems are solved” or “Langlands is finished.”

**Prerequisites.** Comfort with integers, polynomials, and the idea of a curve given by an equation. No prior modular-forms course is assumed. Cross-links: [FLT in the proofs chapter]({{ site.baseurl }}/contents/en/chapter05/05_08_Fermat_Last_Theorem/), [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/), [Langlands]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/).

---

## Key ideas: What Are Number Theory, Elliptic Curves, and Modular Forms, and What Do They Study?

If you graduated in engineering or the natural sciences, calculus and linear algebra feel like home, while "elliptic curves" and "modular forms" can sound like objects from another planet. In reality, they rest on three clear, vivid pillars:

### 1. Number Theory and Diophantine Equations
Number theory studies the hidden laws of integers and primes. One of its oldest branches is **Diophantine equations**: finding integer or rational solutions to polynomial equations, like $$a^2 + b^2 = c^2$$ (Pythagorean triples, with infinitely many solutions like $$3^2 + 4^2 = 5^2$$) or $$a^n + b^n = c^n$$. What makes integer equations treacherous is that calculus cannot approximate your way to an answer—a real solution that misses an integer by $$0.00001$$ is completely useless.

### 2. Elliptic Curves and Their "Arithmetic DNA" $$a_p$$
An **elliptic curve** is *not* an ellipse! It is the solution set of a nonsingular cubic equation $$y^2 = x^3 + Ax + B$$ (or more generally $$y^2 + a_1xy + a_3y = x^3 + a_2x^2 + a_4x + a_6$$). Over the real numbers it forms a smooth curve; over the complex numbers it looks like the surface of a donut (a torus). Miraculously, points on an elliptic curve can be **"added" together** using a geometric secant-line rule (the very engine behind Elliptic Curve Cryptography securing modern banking). Even better, if you reduce the equation modulo each prime $$p$$, you can count the number of solutions $$N_p$$ (including the point at infinity $$\mathcal{O}$$) and record the defect $$a_p = p + 1 - N_p$$. The sequence $$(a_2, a_3, a_5, a_7, \dots)$$ acts as the curve’s **arithmetic DNA**.

### 3. Modular Forms and Their "Analytic DNA" $$c_p$$
A **modular form** belongs to an entirely different universe: **complex analysis**. It is a holomorphic function $$f(z)$$ on the upper half-plane ($$\operatorname{Im}(z) > 0$$) obeying an immense web of symmetries under fractional linear transformations $$z \mapsto \frac{az+b}{cz+d}$$ with $$ad - bc = 1$$. Because it is periodic ($$f(z+1) = f(z)$$), it expands as a Fourier series $$f(z) = \sum_{n=1}^{\infty} c_n q^n$$ (where $$q = e^{2\pi i z}$$). The prime-indexed coefficients $$(c_2, c_3, c_5, c_7, \dots)$$ form its **analytic DNA**.

**The twentieth-century shock (Modularity Theorem):** These two alien worlds—cubic equations over integers on one side, hyper-symmetric complex functions on the other—share the **exact same DNA**! Every elliptic curve over $$\mathbb{Q}$$ has a modular-form twin whose coefficients satisfy $$a_p = c_p$$ for almost every prime $$p$$. That unlikely bridge is what brought down Fermat’s Last Theorem.

---

## 1. The problem that waited three centuries

**Fermat’s Last Theorem.** For every integer $$n \ge 3$$, there do not exist positive integers $$a,b,c$$ satisfying

$$
a^n + b^n = c^n.
$$

For $$n = 2$$, solutions are abundant: $$(3,4,5)$$, $$(5,12,13)$$, $$(8,15,17)$$, and infinitely many more. Yet the moment the exponent reaches $$n = 3$$, the door slams shut. Pierre de Fermat asserted the claim around 1637 in the margin of Diophantus’s *Arithmetica*, claiming a “marvelous proof” too long for the margin. No general proof acceptable to the modern community existed before the 1990s. Special cases accumulated over centuries: Fermat himself for $$n=4$$ (via infinite descent); Euler for $$n=3$$; Sophie Germain for an entire family of primes; Ernst Kummer inventing ideal theory for regular primes; computers checking millions of exponents. None of that patchwork could exhaust infinitely many exponents $$n \ge 3$$.

The eventual solution does **not** simplify to high-school algebra. It rewrites the Diophantine statement in the language of **elliptic curves** and **modular forms**, then uses deep arithmetic geometry. Abel 2016 honors both the theorem and the retooling.

---

## 2. Elliptic curves enter

An elliptic curve over $$\mathbb{Q}$$ can be written, after standard transformations, as a nonsingular cubic

$$
y^2 = x^3 + Ax + B
$$

with rational coefficients $$A,B$$ (and nonvanishing discriminant $$\Delta = -16(4A^3 + 27B^2) \neq 0$$). Its set of rational points, together with a point at infinity, forms a finitely generated abelian group—the **Mordell–Weil theorem**. Elliptic curves also carry **$$L$$-functions** $$L(E,s)$$ assembled from the point counts $$a_p$$ across all primes $$p$$.

**Frey’s bold idea (1980s).** Suppose Fermat’s Last Theorem were *false*, so there existed a nontrivial solution $$a^p + b^p = c^p$$ for an odd prime $$p \ge 5$$ with coprime positive integers $$a, b, c$$. Rather than staring at that equation, Gerhard Frey used $$(a, b, c)$$ to build an explicit elliptic curve—the **Frey curve**:

$$
E_{a,b,c}:\quad y^2 = x(x - a^p)(x + b^p).
$$

Its discriminant is $$\Delta = 16(abc)^{2p}$$—an almost-perfect $$2p$$-th power! In the universe of elliptic curves, that freakish neatness is a red flag of pathology. Frey suspected that such a bizarre curve could **never be modular**—it could not have a twin in the world of modular forms. Turning that brilliant hunch into a rigorous theorem took deep work by Jean-Pierre Serre (the epsilon conjecture) and a landmark proof by Ken Ribet in 1986.

Pause to appreciate the conceptual leap: a pure Diophantine nonexistence statement became a geometric question about **which elliptic curves are allowed to exist** inside a modularity classification.

---

## 3. Modularity as the engine

The **modularity theorem** (formerly the Taniyama–Shimura–Weil conjecture) asserts that every elliptic curve $$E$$ over $$\mathbb{Q}$$ corresponds to a modular form $$f$$—an analytic object on the upper half-plane

$$
\mathbb{H} = \{ z\in\mathbb{C} : \operatorname{Im}(z)>0 \}
$$

with strong transformation laws under a congruence subgroup $$\Gamma_0(N)$$ of $$\mathrm{SL}_2(\mathbb{Z})$$, where $$N$$ is the **level** of the modular form. Through that correspondence, the arithmetic of the curve is mirrored by the Fourier coefficients and $$L$$-function of the form.

### Explanation: Checking the "Matching DNA" Between an Elliptic Curve and a Modular Form by Hand

To see that modularity is not an abstract fairy tale but an arithmetic identity you can **verify with pen and paper**, consider the famous level-$$11$$ elliptic curve:

$$
E:\quad y^2 + y = x^3 - x^2.
$$

#### Step 1: Count points $$N_p$$ and compute $$a_p = p + 1 - N_p$$ modulo $$p = 2, 3, 5$$
(Remember to add $$1$$ for the point at infinity $$\mathcal{O}$$ to the pairs $$(x, y) \in \mathbb{F}_p^2$$.)

- **For $$p = 2$$:** Test $$x, y \in \{0, 1\}$$. The left side $$y^2 + y \equiv 0 \pmod 2$$ for both $$y = 0, 1$$, and the right side $$x^3 - x^2 \equiv 0 \pmod 2$$ for both $$x = 0, 1$$. All 4 pairs $$(0,0), (0,1), (1,0), (1,1)$$ work! Adding $$\mathcal{O}$$ gives $$N_2 = 4 + 1 = 5$$, so:
  $$
  a_2 = 2 + 1 - 5 = -2.
  $$
- **For $$p = 3$$:** Evaluate modulo $$3$$:
  - Left side $$y^2 + y$$: $$y=0 \mapsto 0$$; $$y=1 \mapsto 2$$; $$y=2 \mapsto 6 \equiv 0$$.
  - Right side $$x^3 - x^2$$: $$x=0 \mapsto 0$$ (matches $$y=0,2$$ → 2 points); $$x=1 \mapsto 0$$ (matches $$y=0,2$$ → 2 points); $$x=2 \mapsto 8-4=4 \equiv 1$$ (no $$y$$ gives $$1$$ → 0 points).
  - Total $$N_3 = 4 + 1 = 5$$, so:
  $$
  a_3 = 3 + 1 - 5 = -1.
  $$
- **For $$p = 5$$:** Evaluate modulo $$5$$:
  - Left side $$y^2 + y$$: $$y=0 \mapsto 0$$; $$y=1 \mapsto 2$$; $$y=2 \mapsto 1$$; $$y=3 \mapsto 2$$; $$y=4 \mapsto 0$$.
  - Right side $$x^3 - x^2$$: $$x=0 \mapsto 0$$ (2 points); $$x=1 \mapsto 0$$ (2 points); $$x=2 \mapsto 4$$ (0 points); $$x=3 \mapsto 18 \equiv 3$$ (0 points); $$x=4 \mapsto 48 \equiv 3$$ (0 points).
  - Total $$N_5 = 4 + 1 = 5$$, so:
  $$
  a_5 = 5 + 1 - 5 = +1.
  $$

#### Step 2: Expand the level-11 modular form by hand
On the complex-analysis side, consider the infinite product $$f(q) = q \prod_{n=1}^{\infty} (1 - q^n)^2 (1 - q^{11n})^2$$. To find the coefficients up to $$q^5$$, we only need factors with powers $$\le 4$$ (since there is already a leading $$q$$):

$$
\begin{aligned}
f(q) &= q(1 - q)^2(1 - q^2)^2(1 - q^3)^2(1 - q^4)^2 \cdots \\
&= q(1 - 2q + q^2)(1 - 2q^2 + q^4)(1 - 2q^3 + \cdots)(1 - 2q^4 + \cdots) \\
&= q\bigl(1 - 2q - q^2 + 2q^3 + q^4 + \cdots\bigr) \\
&= q - 2q^2 - q^3 + 2q^4 + q^5 + \cdots
\end{aligned}
$$

#### Step 3: Compare the numbers!
Read off the coefficients of $$q^2, q^3, q^5$$ in $$f(q)$$: they are **$$-2,\ -1,\ +1$$**—an exact match, sign for sign, with $$a_2 = -2,\ a_3 = -1,\ a_5 = +1$$ that you just counted by hand in Step 1! And that match continues forever for every prime $$p$$!

**Ken Ribet’s level-lowering theorem.** Ribet proved that if a Frey curve were modular at some level $$N$$, then because its discriminant is a $$2p$$-th power, one could strip away prime factors from $$N$$ all the way down to **level $$N = 2$$**. Yet a classical fact was already known: **the space of weight-2 cusp forms of level $$N = 2$$ is completely empty!** Thus:

> If enough modularity is known for the relevant class of curves, FLT follows.

**Wiles’s breakthrough.** Wiles proved modularity for the crucial class of **semistable** elliptic curves over $$\mathbb{Q}$$. Semistability is a reduction-type condition at primes, and Frey curves arising from FLT counterexamples always satisfy it. The methods—**deformation theory of Galois representations** and a numerical criterion for **modularity lifting**—became a new industrial standard in number theory. A subtle gap in the 1993 argument was repaired in joint work with **Richard Taylor** (the Taylor–Wiles patching method).

Later, **Breuil–Conrad–Diamond–Taylor** completed modularity for **all** elliptic curves over $$\mathbb{Q}$$, not only the semistable ones. Abel’s wording carefully says “by way of the modularity conjecture for **semistable** elliptic curves”—historically exact.

---

### Short video: Andrew Wiles & Fermat’s Last Theorem: From equations to modularity

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/wiles-fermat_en.mp4"></video>
</div>

1-minute silent overview: Pythagoras n = 2 vs. near-miss n = 12 parity check, the Frey elliptic curve, Ribet’s level-lowering to N = 2, and Wiles’s modularity contradiction.


<div class="interactive-demo" markdown="1">
<div data-demo="fermat-explainer" data-preset="frey" data-lang="en"></div>
</div>
<script src="{{ '/public/js/explainers/fermat-explainer.js' | relative_url }}"></script>

## 4. Logical skeleton (idea of proof)

1. Assume $$a^n + b^n = c^n$$ with $$n\ge 3$$ and $$abc\neq 0$$ (reducing to odd prime $$p \ge 5$$).  
2. Build the semistable Frey elliptic curve $$E: y^2 = x(x - a^p)(x + b^p)$$ from $$(a,b,c)$$.  
3. By Ribet’s theorem, that curve cannot be modular (otherwise a nonexistent level-2 cusp form would exist).  
4. By Wiles (and Taylor–Wiles), every semistable elliptic curve over $$\mathbb{Q}$$ must be modular.  
5. Contradiction. Hence no such $$(a,b,c)$$ exists.

This is the **idea**. The technical bulk lives in step 4: controlling Galois representations attached to the curve, lifting residual modularity, and verifying hypotheses that make the lifting theorems apply. For seminar work, being able to narrate steps 1–5 cleanly already separates understanding from slogan.

---

## 5. Galois representations: the deeper map

Wiles’s method studies **Galois representations** attached to elliptic curves—homomorphisms

$$
\rho_{E,\ell} : \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \mathrm{GL}_2(\mathbb{Z}_\ell)
$$

(or residual versions modulo $$\ell$$)—and asks when such representations arise from modular forms. **Modularity lifting** theorems (often summarized as $$R = \mathbb{T}$$, comparing a universal deformation ring $$R$$ to a Hecke algebra $$\mathbb{T}$$) say, roughly: if a representation looks modular modulo a small prime (starting from Langlands–Tunnell at $$\ell = 3$$, plus Wiles’s $$3\text{–}5$$ switch), then under suitable hypotheses every lift to characteristic zero must also be modular.

That philosophy now drives enormous parts of the Langlands program for $$\mathrm{GL}_2$$ and beyond. FLT’s modern proof is a **representation-theoretic machine**, not a clever factorization trick. For this course, keep the takeaway: the Abel citation’s phrase “opening a new era” points at methods, not only at the nonexistence of solutions to $$a^n+b^n=c^n$$.

Downstream, full modularity supports the analytic theory of elliptic $$L$$-functions used in the [Birch–Swinnerton-Dyer]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/) landscape: when arithmetic rank meets analytic rank, modularity is part of the dictionary that makes the conjecture speak.

---

## 6. Why Abel called it an “era”

Three layers justify the language.

**New methods.** Galois deformation rings, Taylor–Wiles patching, modularity lifting—these became core technology. Later theorems (such as Sato–Tate and Serre’s modularity conjecture) begin where Wiles left the toolkit.

**New confidence.** Hard Diophantine problems can be attacked by modularity and Langlands-adjacent tools. The subject’s psychology shifted: some “impossible-looking” equations might be portals into geometry.

**New curriculum.** Graduate number theory courses reorganized around modularity, Galois representations, and automorphic forms. Abel 2016 honors both the theorem and the **retooling of arithmetic geometry**.

---

## 7. Historical texture (without mythology)

Wiles announced a proof in 1993; a gap was identified; the repaired proof with Taylor appeared in the mid-1990s (*Annals of Mathematics*, 1995). Popular accounts sometimes overplay solitude or underplay the network: Frey, Serre, Ribet, Mazur, Langlands, Taniyama, Shimura, Weil, and many others shaped the landscape Wiles closed for the semistable case. Abel materials and serious histories credit that chain.

Also: computers are **not** the essence of the proof. Numerical checks of special cases are historically important, but the Abel citation is about a human-written modularity theorem.

### What “semistable” means at slogan level

An elliptic curve over $$\mathbb{Q}$$ has, at each prime $$p$$, a reduction type describing the special fiber of a minimal model. When reduction is bad, a singularity can be either a **node** (the curve crosses itself cleanly like a figure-eight) or a sharp **cusp** (like the pinch of $$y^2 = x^3$$). **Semistable** reduction means every bad prime has only a mild node, never a sharp cusp. Frey curves arising from putative FLT counterexamples are semistable; therefore proving modularity on the semistable class is exactly the lever Ribet’s theorem needs. Full modularity removes the semistable restriction for all elliptic curves over $$\mathbb{Q}$$, which is conceptually cleaner and analytically powerful for $$L$$-functions—but historically FLT was already settled once the semistable modularity theorem was in place.

---

## 8. Confusions

| Claim | Correction |
|-------|------------|
| “Wiles only checked computers.” | Core is a modularity theorem; computers are not the essence. |
| “Fermat already had a general proof.” | No accepted general proof before Wiles. |
| “Wiles proved full modularity for all elliptic curves over $$\mathbb{Q}$$. ” | He proved the **semistable** case needed for FLT; full modularity came later (BCDT). |
| “Modularity = Langlands finished.” | One major case in a vast program. |
| “FLT closed all Diophantine problems.” | Vast open landscape remains (e.g. many cases of BSD, higher-dimensional Diophantine geometry). |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/wiles-fermat/`.

**From the research pack (must-know slogans)**

- Abel 2016: Wiles for FLT via **semistable modularity** of elliptic curves over $$\mathbb{Q}$$.
- Strategy slogan: Frey curve → Ribet (non-modular if counterexample) → Wiles modularity lifting → contradiction.
- Full modularity later: Breuil–Conrad–Diamond–Taylor; Abel wording carefully says semistable.
- Taylor–Wiles method repaired the original gap.

**Recommended order**

1. **Core** — Wiles Abel lecture — FLT abelian/non-abelian: [https://www.youtube.com/watch?v=4t1mgEBx1nQ](https://www.youtube.com/watch?v=4t1mgEBx1nQ).  
2. **Core** — Darmon — Wiles' marvelous proof: [https://www.youtube.com/watch?v=oqMaziDIBYY](https://www.youtube.com/watch?v=oqMaziDIBYY).  
3. **History** — Abel interview with Wiles: [https://www.youtube.com/watch?v=cWKAzX5U85Q](https://www.youtube.com/watch?v=cWKAzX5U85Q).  
4. **Orientation** — Live interview Wiles (Oslo): [https://www.youtube.com/watch?v=baUlp5EWhCk](https://www.youtube.com/watch?v=baUlp5EWhCk).  
5. **Orientation** — Alex Bellos on Wiles/FLT: [https://www.youtube.com/watch?v=2Pu4vZZu3JA](https://www.youtube.com/watch?v=2Pu4vZZu3JA).  
6. **History** — INI — Thirty years of proof (Wiles anniversary): [https://www.youtube.com/watch?v=nlUimyJpWtI](https://www.youtube.com/watch?v=nlUimyJpWtI).  

**Official / primary written hubs**

- Abel 2016 Wiles page: https://abelprize.no/abel-prize-laureates/2016  

Complete URL bibliography: `research/video-research/wiles-fermat/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/wiles-fermat/transcripts/` · status: `research/video-research/wiles-fermat/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/wiles-fermat_4t1mgEBx1nQ_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/wiles-fermat/references.md`.

1. Abel 2016 Wiles page — https://abelprize.no/abel-prize-laureates/2016  
2. Wiles Abel lecture — FLT abelian/non-abelian — https://www.youtube.com/watch?v=4t1mgEBx1nQ  
3. Darmon — Wiles' marvelous proof — https://www.youtube.com/watch?v=oqMaziDIBYY  
4. Abel interview with Wiles — https://www.youtube.com/watch?v=cWKAzX5U85Q  
5. Live interview Wiles (Oslo) — https://www.youtube.com/watch?v=baUlp5EWhCk  
6. Alex Bellos on Wiles/FLT — https://www.youtube.com/watch?v=2Pu4vZZu3JA  
7. INI — Thirty years of proof (Wiles anniversary) — https://www.youtube.com/watch?v=nlUimyJpWtI  
8. Nature — Wiles Abel Prize — https://www.nature.com/articles/nature.2016.19552  
9. Wikipedia — Wiles's proof of FLT — https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem  
10. Wikipedia — Modularity theorem — https://en.wikipedia.org/wiki/Modularity_theorem  
11. Research pack folder: `research/video-research/wiles-fermat/`.

1. Abel Prize 2016 — citation, biography, popular notes: [abelprize.no/abel-prize-laureates/2016](https://abelprize.no/abel-prize-laureates/2016).  
2. A. Wiles, *Modular elliptic curves and Fermat’s Last Theorem*, Ann. of Math. (1995); R. Taylor–A. Wiles, companion paper.  
3. Surveys: H. Darmon and others on modularity; popular: Simon Singh, *Fermat’s Enigma*.  
4. Course: [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/); [Langlands]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/); [FLT proofs chapter]({{ site.baseurl }}/contents/en/chapter05/05_08_Fermat_Last_Theorem/).

---

## Further directions

- Seminar A3 brief: “What was proved about modularity in the 1990s, and what remained for later authors?”  
- A4 adjacent: narrate the Frey–Ribet–Wiles skeleton as an idea-of-proof.  
- Cross-critique popular FLT documentaries for overclaim (methods vs mythology).  
- Compare with a related [Fields essay]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/).  
- Note one precise open question nearby: aspects of BSD; modularity in higher dimensions; broader Langlands correspondences.  
- Next: [Karen Uhlenbeck: Gauge Theory]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/).

## Video tham khảo

- **xem trước** — [Andrew Wiles: Fermat's Last theorem: abelian and non-abelian approaches](https://www.youtube.com/watch?v=4t1mgEBx1nQ) — The Abel Prize, English. Watch first. “Andrew Wiles: Fermat's Last theorem: abelian and non-abelian approaches” orients the lesson’s aim: After this lecture you should be able to state FLT precisely for integers n\ge 3; explain the Frey curve → Ribet → modularity → contradiction strategy at idea level; distinguish Wi…
- [Henri Darmon: Andrew Wiles' marvelous proof](https://www.youtube.com/watch?v=oqMaziDIBYY) — The Abel Prize, English. A second pass once the main claim is in view: After this lecture you should be able to state FLT precisely for integers n\ge 3; explain the Frey curve → Ribet → modularity → contradiction strategy at idea level; distinguish Wi…
- [Andrew Wiles - The Abel Prize interview 2016](https://www.youtube.com/watch?v=cWKAzX5U85Q) — The Abel Prize, English. Further depth after the first two, still tied to this lesson: After this lecture you should be able to state FLT precisely for integers n\ge 3; explain the Frey curve → Ribet → modularity → contradiction strategy at idea level; distinguish Wi…
