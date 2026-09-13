---
layout: post
title: "Deligne’s Proof of the Weil Conjectures (Fields Medal 1978)"
chapter: '02'
order: 18
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Pierre Deligne** received the **Fields Medal 1978** for, in the standard IMU wording of that congress, giving a **solution of the Weil conjectures** concerning generalizations of the Riemann hypothesis to varieties over finite fields, work that “did much to unify algebraic geometry and algebraic number theory.” The medal is not a claim that one person built étale cohomology, nor that the **standard conjectures** on algebraic cycles, or the **Hodge conjecture**, were settled. **André Weil** asked the questions (1949). **Bernard Dwork** proved rationality by $$p$$-adic methods (1960). The **Grothendieck school** built étale cohomology and obtained the functional equation. Deligne proved the remaining purity statement—the Riemann-hypothesis analogue—in *La conjecture de Weil: I* (1974), and later a far-reaching sheaf-theoretic upgrade in *Weil II* (1980).

This essay is for learners who have met the ordinary Riemann zeta function and a projective variety, and want to see how a counting problem over $$\mathbb{F}_q$$ became a theorem about eigenvalues of Frobenius. A later honor, the **Abel Prize 2013**, recognized a lifetime of influence; it is distinct from Fields 1978 and should not be collapsed into it.

---

## Learning objectives

After this lecture you should be able to:

- State the Weil conjectures at slogan level: the zeta function of a smooth projective variety over a finite field is **rational**, satisfies a **functional equation**, and has zeros/poles on prescribed vertical lines (the **RH analogue**).
- Assign credit: **Dwork** (rationality), **Grothendieck–Artin étale cohomology** (cohomological expression and functional equation), **Deligne** (purity / RH analogue, Weil I and Weil II).
- Write the zeta generating function in $$T=q^{-s}$$ and interpret $$N_m$$ as the number of points over $$\mathbb{F}_{q^m}$$.
- Explain why étale cohomology is the *machine* and Deligne’s estimate on Frobenius eigenvalues is the *missing bound*.
- State, carefully, that Ramanujan–Petersson bounds for holomorphic modular forms of weight at least $$2$$ follow from the Weil conjectures applied to suitable varieties (Kuga–Sato / modular constructions)—not from a one-line argument on a single modular curve alone.
- Refuse two overclaims: Deligne did **not** prove the standard conjectures; he did **not** prove the Hodge conjecture.

**Prerequisites.** Finite fields $$\mathbb{F}_q$$; the idea of a projective variety and of counting its rational points; Euler products and the classical Riemann hypothesis as a *model* for a statement about zeros. Schemes and derived categories are not required—think “a geometric cohomology theory with a Lefschetz trace formula.”

**Seminar links.** The classical RH, still open: [Riemann hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/). Arithmetic geometry neighbors: [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/) ($$L$$-functions of curves over $$\mathbb{Q}$$), [Langlands]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/), [Scholze / $$p$$-adic cohomology]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/). Lifetime-prize parallel: [What is the Abel Prize?]({{ site.baseurl }}/contents/en/chapter08/08_02_What_Is_Abel_Prize/).

---

## 1. A history of counting points and guessing a zeta

Gauss already counted points on certain elliptic curves over finite fields while studying periods and cyclotomy. **Hasse** proved the RH analogue for elliptic curves: if $$E/\mathbb{F}_q$$ has $$N_1$$ points, then $$|N_1-(q+1)|\le 2\sqrt{q}$$. **Weil** proved the conjectures for curves of any genus and for abelian varieties, and in 1949 proposed the pattern for smooth projective varieties of every dimension. The generating function

$$
Z(X,T)=\exp\Bigl(\sum_{m\ge 1}N_m\frac{T^m}{m}\Bigr),\qquad T=q^{-s},
$$

should be a **rational** function of $$T$$; it should satisfy a **functional equation** relating $$Z(X,T)$$ to $$Z(X,1/q^n T)$$ (here $$n=\dim X$$); and the reciprocal roots of the degree-$$i$$ factor should have absolute value $$q^{i/2}$$—the **Riemann-hypothesis analogue**, or **purity**. A fourth clause identifies those degrees with Betti numbers of a complex lift, when one exists.

The analogy with topology was the scandal and the invitation. Over $$\mathbb{C}$$, the Lefschetz trace formula counts fixed points of a map from traces on cohomology. Over $$\mathbb{F}_q$$, Frobenius is a map, and $$N_m$$ is a count of its fixed points on $$X(\overline{\mathbb{F}}_q)$$. If a cohomology theory existed with a trace formula *and* a Poincaré duality that produced the functional equation, the RH analogue would become a bound on eigenvalues.

**Dwork (1960)** proved rationality by $$p$$-adic analysis, without constructing that cohomology. **Grothendieck**, **Michael Artin**, and the **SGA** community constructed **étale cohomology** with $$\ell$$-adic coefficients, proved a Lefschetz trace formula, and obtained rationality again together with the functional equation. Grothendieck hoped to deduce purity from his **standard conjectures** on algebraic cycles. Those conjectures remain open (except for pieces such as hard Lefschetz, which Deligne later established by extending the Weil work). The RH analogue therefore required a different argument.

---

## 2. Slogan: Frobenius acts, and its eigenvalues are pure

Once étale cohomology is granted, one has (under the standing smoothness and projectivity hypotheses) a factorization

$$
Z(X,T)=\frac{P_1(T)P_3(T)\cdots P_{2n-1}(T)}{P_0(T)P_2(T)\cdots P_{2n}(T)},
$$

where $$P_i(T)=\det\bigl(1-T\,\mathrm{Frob}\,;\,H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}},\mathbb{Q}_\ell)\bigr)$$ and $$P_0(T)=1-T$$, $$P_{2n}(T)=1-q^n T$$. The Lefschetz trace formula makes this an identity of generating functions, not a guess.

**Deligne’s theorem (Weil I, 1974).** Each reciprocal root $$\alpha$$ of $$P_i$$ satisfies $$|\alpha|=q^{i/2}$$. Equivalently, the eigenvalues of Frobenius on $$H^i$$ are **pure of weight $$i$$**.

**Slogan.** The Weil conjectures rearrange a counting problem into a **spectral** problem: point counts are traces; the RH analogue is a restriction on where those traces’ constituent eigenvalues may sit. Deligne supplies the restriction. Grothendieck’s school supplies the traces.

The proof is not a transcription of Weil’s argument for curves. It uses a fibered-power / correspondence argument, estimates of exponential sums, and a reduction that lets one deduce high-dimensional purity from more tractable geometric situations—circumventing the standard conjectures. Katz’s Helsinki ICM report (1980) remains a standard guide to the architecture at the time of the medal.

---

## 3. What Weil II rearranges, and what it does not

*La conjecture de Weil: II* (1980) is a generalization from the constant sheaf on a smooth projective variety to **mixed constructible $$\ell$$-adic sheaves** on more general schemes over finite fields. It bounds the **weights** of direct images, and it became the everyday language of $$\ell$$-adic sheaf theory: a theorem about a variety is often a special case of a theorem about a sheaf.

**What this rearranges.** Exponential sums, monodromy, and many estimates in analytic number theory become geometric weight statements. Deligne’s earlier work with **Serre** on $$\ell$$-adic representations of modular forms, and the deduction of **Ramanujan–Petersson**, sit in the same circle: once you know weights, you know bounds.

**Ramanujan–Petersson, stated carefully.** For the Ramanujan tau function, the conjecture $$|\tau(p)|\le 2p^{11/2}$$ is the RH analogue for a motive of weight $$11$$ attached to the discriminant modular form. Deligne reduced Ramanujan–Petersson for holomorphic cusp forms of weight $$\ge 2$$ to the Weil conjectures for certain higher-dimensional varieties (Kuga–Sato varieties, built from powers of universal elliptic curves over modular curves). Weil I therefore implies those bounds. Weight $$1$$ is a different story, completed in work of **Deligne–Serre**. Bounds for classical Kloosterman sums are related but easier in one dimension: they follow from Weil’s theorem for curves, already available before 1974. Do not say “Deligne bounded Kloosterman sums, hence Ramanujan”; the modular-form conjecture needs the higher-dimensional purity.

**What is not proved.** The **standard conjectures** (Grothendieck) remain open as a package. The **Hodge conjecture** remains open. Deligne defined **absolute Hodge cycles** as a usable surrogate in some arguments, and he created **mixed Hodge structures**, which organize weights in complex geometry; those are tools, not a proof of Hodge. Motives, in the strong sense Grothendieck wanted, are still a program.

---

## 4. Honest attribution

| Contributor | Role |
|-------------|------|
| Weil (1949; curves earlier) | The conjectures; proofs for curves and abelian varieties |
| Hasse | Elliptic curves over finite fields |
| Dwork (1960) | Rationality, $$p$$-adic |
| Grothendieck, M. Artin, SGA | Étale cohomology; trace formula; functional equation |
| Serre | Early cohomological and modular input; later Deligne–Serre |
| Deligne, Weil I (1974) | RH analogue / purity of Frobenius eigenvalues |
| Deligne, Weil II (1980) | Weights for sheaves; the working form of the theory |
| Later community | Perverse sheaves (BBD, with Beilinson–Bernstein–Gabber), applications |

Deligne was born in 1944 in Belgium, wrote a thesis under Grothendieck, and spent the Fields years at the IHÉS before moving to the Institute for Advanced Study. The 1978 medal recognizes the Weil work and the unification it made visible. The **Abel Prize 2013**—“for seminal contributions to algebraic geometry and for their transformative impact on number theory, representation theory, and related fields”—is a *lifetime* prize covering mixed Hodge theory, Deligne–Lusztig representations, moduli of curves with Mumford, and much else. Keep the two honors on separate lines.

---

## 5. Why a Fields Medal, and why the story still matters

The Weil conjectures were a generation-defining problem: they forced the invention of a cohomology theory and then demanded an estimate that the theory did not give for free. Completing them unified two descriptions of the same integers $$N_m$$—one from counting, one from topology over finite fields—and exported bounds into automorphic forms and exponential sums. For this course, Deligne is the portrait of a **program finished by several hands**, with one decisive estimate.

The classical [Riemann hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) remains open. That is not an embarrassment of the Weil story; it is a reminder that “RH analogue” means a *proved* restriction on weights in finite characteristic, not a proof of Riemann’s original statement. Students sometimes hear “Deligne proved RH.” He proved RH *for zeta functions of varieties over finite fields*.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Deligne invented étale cohomology.” | Grothendieck, Artin, and SGA built the machine. |
| “Dwork proved the Weil conjectures.” | Dwork proved **rationality**. Purity is Deligne. |
| “Deligne proved the standard conjectures / the Hodge conjecture.” | Both remain open (as general statements). |
| “Deligne proved the classical Riemann hypothesis.” | He proved the **analogue** for varieties over $$\mathbb{F}_q$$. |
| “Ramanujan follows from Weil for a single modular curve.” | Weight $$\ge 2$$ uses higher-dimensional (Kuga–Sato) geometry; weight 1 is Deligne–Serre. |
| “Abel 2013 is the same honor as Fields 1978.” | Abel is a later lifetime prize; Fields cited the Weil work in 1978. |

---

## Exercises

1. Write $$Z(X,T)$$ and say in words what $$N_m$$ counts. Check the formula for $$\mathbb{P}^1$$: $$N_m=q^m+1$$.
2. In the elliptic-curve case, Hasse’s bound $$|N_1-(q+1)|\le 2\sqrt{q}$$ is the RH analogue for $$n=1$$. Why do two complex numbers of absolute value $$\sqrt{q}$$ produce that inequality?
3. Who proved which piece: rationality, functional equation, purity? Fill a three-row table without looking.
4. Why did Grothendieck’s standard conjectures *look like* a path to purity, and why is it important that Deligne avoided needing them?
5. **Ramanujan, carefully.** State $$|\tau(p)|\le 2p^{11/2}$$ and write two sentences on why this is a Weil-type bound rather than an elementary estimate on the modular curve $$X_0(1)$$ alone.
6. **LO6.** Find a popular sentence that says “Deligne proved the Riemann hypothesis.” Rewrite it for this course.
7. Skim the first pages of Weil I or a survey (Katz, ICM 1978) and list five words to learn next (e.g. Lefschetz pencil, vanishing cycle, weight, $$\ell$$-adic, Poincaré duality).
8. **Seminar stretch.** Compare “purity of weights” here with [Scholze’s]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/) later $$p$$-adic cohomology languages: both are about moving information between cohomology theories. What problem is finite-field, and what problem is mixed-characteristic?

---

## Video and reading links

No course video-research pack is attached to this lesson.

1. IMU Fields Medals 1978 (Deligne citation): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1978).
2. Encyclopedia: [Pierre Deligne](https://en.wikipedia.org/wiki/Pierre_Deligne); [Weil conjectures](https://en.wikipedia.org/wiki/Weil_conjectures).
3. Abel Prize 2013 (lifetime honor, distinct from Fields): [abelprize.no/abel-prize-laureates/2013](https://abelprize.no/abel-prize-laureates/2013).
4. IAS press release (Abel 2013): [Pierre Deligne Awarded 2013 Abel Prize](https://www.ias.edu/press-releases/pierre-deligne-awarded-2013-abel-prize).
5. arXiv search: [Deligne Weil](https://arxiv.org/search/?query=Deligne+Weil&searchtype=all).
6. Course: [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/); [Abel overview]({{ site.baseurl }}/contents/en/chapter08/08_02_What_Is_Abel_Prize/).

**Status reminder:** Weil RH analogue over finite fields—**not** the classical RH, **not** Hodge, **not** the standard conjectures.

---

## References

1. International Mathematical Union, Fields Medals 1978 — Pierre Deligne (wording reproduced from the 1986 Albers–Alexanderson–Reid congress history on the IMU page).
2. **A. Weil**, *Numbers of solutions of equations in finite fields*, *Bull. Amer. Math. Soc.* (1949).
3. **B. Dwork**, *On the rationality of the zeta function of an algebraic variety*, *Amer. J. Math.* (1960).
4. **P. Deligne**, *La conjecture de Weil: I*, *Publ. Math. IHÉS* 43 (1974); *La conjecture de Weil: II*, *Publ. Math. IHÉS* 52 (1980).
5. **N. Katz**, *The work of Pierre Deligne*, ICM Helsinki 1978 proceedings (survey at the time of the medal).
6. SGA and étale-cohomology background: Grothendieck–Artin; a modern first course (e.g. Milne’s notes) as a pointer, not required reading.
7. Abel Prize 2013 citation — Pierre Deligne (abelprize.no).
8. Course: [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/), [Scholze]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/), [Langlands]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/).

---

## Further directions

- Compute $$Z(\mathbb{P}^n,T)$$ by hand; it is the Weil conjectures with no cohomology needed, and it calibrates the notation.
- Read a one-lecture account of the Lefschetz trace formula in étale cohomology before attempting Weil I.
- Seminar A3 option: a one-page “open after Deligne” brief—standard conjectures, Hodge, motives, classical RH—explicitly separating Fields 1978 from Abel 2013.
- If modular forms are your hook, follow Ramanujan–Petersson into Deligne’s papers and then into Deligne–Serre for weight one; keep the dimensional distinction on the page.
