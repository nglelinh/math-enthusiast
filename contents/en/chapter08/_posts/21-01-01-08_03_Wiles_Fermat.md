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

**Sir Andrew J. Wiles** (University of Oxford) received the **Abel Prize 2016**

> “for his stunning proof of Fermat’s Last Theorem by way of the modularity conjecture for semistable elliptic curves, opening a new era in number theory.”  
> — [Abel Prize Committee citation](https://abelprize.no/abel-prize-laureates/2016)

This lecture is a deep map of that story: what Fermat’s Last Theorem (FLT) says; how a Diophantine statement became a statement about elliptic curves and modular forms; what Wiles actually proved about **semistable modularity**; and why the Abel Prize treats the achievement as an **era-opening body of method**, not only a trophy for one equation. Official materials are at [abelprize.no](https://abelprize.no/).

---

## Learning objectives

After this lecture you should be able to state FLT precisely for integers $$n\ge 3$$; explain the Frey curve → Ribet → modularity → contradiction strategy at idea level; distinguish Wiles’s semistable modularity advance from the later full modularity theorem of Breuil–Conrad–Diamond–Taylor; connect modularity to Galois representations and $$L$$-functions at slogan level; and avoid confusing “FLT is proved” with “all Diophantine problems are solved” or “Langlands is finished.”

**Prerequisites.** Comfort with integers, polynomials, and the idea of a curve given by an equation. No prior modular-forms course is assumed. Cross-links: [FLT in the proofs chapter]({{ site.baseurl }}/contents/en/chapter05/05_08_Fermat_Last_Theorem/), [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/), [Langlands]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/).

---

## 1. The problem that waited three centuries

**Fermat’s Last Theorem.** For every integer $$n \ge 3$$, there do not exist positive integers $$a,b,c$$ satisfying

$$
a^n + b^n = c^n.
$$

Pierre de Fermat asserted the claim around 1637 in a famous margin note, saying he had a “marvelous proof” that the margin was too narrow to contain. No general proof acceptable to the modern community was known before the 1990s. Special cases accumulated over centuries: Fermat himself for $$n=4$$ (via infinite descent); Euler and others for small exponents; Kummer and algebraic number theory for regular primes; computer-assisted checks for large ranges of exponents. None of that patchwork is a uniform proof for all $$n\ge 3$$.

The eventual solution does **not** simplify to high-school algebra. It rewrites the Diophantine statement in the language of **elliptic curves** and **modular forms**, then uses deep arithmetic geometry. Abel 2016 honors both the theorem and the retooling.

---

## 2. Elliptic curves enter

An elliptic curve over $$\mathbb{Q}$$ can be written, after standard transformations, as a nonsingular cubic

$$
y^2 = x^3 + Ax + B
$$

with rational coefficients $$A,B$$ (and nonvanishing discriminant). Its set of rational points, together with a point at infinity, forms a finitely generated abelian group—the **Mordell–Weil theorem**. Elliptic curves also carry **$$L$$-functions** $$L(E,s)$$ that encode arithmetic information; modularity relates those analytic objects to modular forms.

**Frey’s idea (1980s).** Suppose there existed a nontrivial solution of $$a^n + b^n = c^n$$ with $$n\ge 3$$. One can manufacture an elliptic curve—the **Frey curve**—with extremely unusual arithmetic properties. Heuristically, the curve would be so pathological that it could not fit the modularity dictionary conjectured for elliptic curves over $$\mathbb{Q}$$. Making that heuristic into a theorem required major work by Serre, Ribet, and others.

The conceptual leap is enormous: a pure Diophantine nonexistence statement becomes a claim about **which elliptic curves can exist** inside a modularity classification.

---

## 3. Modularity as the engine

The **modularity theorem** (formerly the Taniyama–Shimura–Weil conjecture) asserts, roughly, that every elliptic curve $$E$$ over $$\mathbb{Q}$$ corresponds to a modular form—an analytic object on the upper half-plane

$$
\mathbb{H} = \{ z\in\mathbb{C} : \operatorname{Im}(z)>0 \}
$$

with strong transformation laws under congruence subgroups of $$\mathrm{SL}_2(\mathbb{Z})$$. Through that correspondence, arithmetic of the curve is mirrored by Fourier coefficients and $$L$$-function data of the form.

**Ken Ribet** proved a level-lowering theorem implying that a Frey curve arising from an FLT counterexample **cannot be modular**. Therefore:

> If enough modularity is known for the relevant class of curves, FLT follows.

**Wiles** proved modularity for the crucial class of **semistable** elliptic curves over $$\mathbb{Q}$$. Semistability is a reduction-type condition at primes; Frey curves arising from FLT counterexamples fall into the class covered by Wiles’s theorem. The methods—**deformation theory of Galois representations** and a numerical criterion for **modularity lifting**—became a new industrial standard in number theory. A gap in the original argument was repaired in joint work with **Richard Taylor** (the Taylor–Wiles method).

Later, **Breuil–Conrad–Diamond–Taylor** completed modularity for **all** elliptic curves over $$\mathbb{Q}$$, not only the semistable ones. Abel’s wording carefully says “by way of the modularity conjecture for **semistable** elliptic curves”—historically precise.

---

## 4. Logical skeleton (idea of proof)

1. Assume $$a^n + b^n = c^n$$ with $$n\ge 3$$ and $$abc\neq 0$$.  
2. Build the Frey elliptic curve from $$(a,b,c)$$.  
3. By Ribet’s theorem, that curve cannot be modular.  
4. By Wiles (semistable modularity covering Frey curves), it must be modular.  
5. Contradiction. Hence no such $$(a,b,c)$$ exists.

This is the **idea**. The technical bulk lives in step 4: controlling Galois representations attached to the curve, lifting residual modularity, and verifying hypotheses that make the lifting theorems apply. For seminar work, being able to narrate steps 1–5 cleanly already separates understanding from slogan.

---

## 5. Galois representations: the deeper map

Wiles’s method studies **Galois representations** attached to elliptic curves—homomorphisms

$$
\rho_{E,\ell} : \operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \mathrm{GL}_2(\mathbb{Z}_\ell)
$$

(or residual versions modulo $$\ell$$)—and asks when such representations arise from modular forms. **Modularity lifting** theorems say, roughly: if a representation looks modular modulo a prime, then under suitable hypotheses it is modular in characteristic zero.

That philosophy now drives enormous parts of the Langlands program for $$\mathrm{GL}_2$$ and beyond. FLT’s modern proof is a **representation-theoretic machine**, not a clever factorization trick. For this course, keep the takeaway: the Abel citation’s phrase “opening a new era” points at methods, not only at the nonexistence of solutions to $$a^n+b^n=c^n$$.

Downstream, full modularity supports the analytic theory of elliptic $$L$$-functions used in the [Birch–Swinnerton-Dyer]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/) landscape: when arithmetic rank meets analytic rank, modularity is part of the dictionary that makes the conjecture speak.

---

## 6. Why Abel called it an “era”

Three layers justify the language.

**New methods.** Galois deformation rings, Taylor–Wiles patching, modularity lifting—these became core technology. Later theorems often begin where Wiles left the toolkit.

**New confidence.** Hard Diophantine problems can be attacked by modularity and Langlands-adjacent tools. The subject’s psychology shifted: some “impossible-looking” equations might be portals into geometry.

**New curriculum.** Graduate number theory courses reorganized around modularity, Galois representations, and automorphic forms. Abel 2016 honors both the theorem and the **retooling of arithmetic geometry**.

---

## 7. Historical texture (without mythology)

Wiles announced a proof in 1993; a gap was identified; the repaired proof with Taylor appeared in the mid-1990s (*Annals of Mathematics*, 1995). Popular accounts sometimes overplay solitude or underplay the network: Frey, Serre, Ribet, Mazur, Langlands, Taniyama, Shimura, Weil, and many others shaped the landscape Wiles closed for the semistable case. Abel materials and serious histories credit that chain.

Also: computers are **not** the essence of the proof. Numerical checks of special cases are historically important, but the Abel citation is about a human-written modularity theorem.

### What “semistable” means at slogan level

An elliptic curve over $$\mathbb{Q}$$ has, at each prime $$p$$, a reduction type describing the special fiber of a minimal model. **Semistable** reduction (nodal rather than cuspidal bad reduction, in the usual slogan) is a regularity condition on those reductions. Frey curves arising from putative FLT counterexamples are semistable; therefore proving modularity on the semistable class is exactly the lever Ribet’s theorem needs. Full modularity removes the semistable restriction for all elliptic curves over $$\mathbb{Q}$$, which is conceptually cleaner and analytically powerful for $$L$$-functions—but historically FLT was already settled once the semistable modularity theorem was in place.

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

## Exercises

1. Write FLT for exponent $$4$$ in words and as an equation. Explain why special cases do not constitute a general proof.  
2. Give the Frey–Ribet–Wiles chain in four bullets, without technical jargon beyond “modular” and “elliptic curve.”  
3. What does “semistable” buy you in the Abel story (one paragraph slogan)?  
4. **≤300 words:** Restate the official Abel 2016 citation in your own words, naming methods not only FLT.  
5. Compare this lecture with the course [FLT page]({{ site.baseurl }}/contents/en/chapter05/05_08_Fermat_Last_Theorem/) and list two differences in emphasis (proof ideas vs lifetime methods).  
6. **Stretch:** In one paragraph, explain what a Galois representation is trying to package (symmetry of arithmetic vs linear algebra).

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
