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

Picture a problem that looks fit for a pocket calculator: take a polynomial equation with integer coefficients, say $$y^2 = x^3 + x + 1$$, and count how many solutions it has over the finite fields $$\mathbb{F}_5, \mathbb{F}_{25}, \mathbb{F}_{125}, \ldots$$. At first glance, this yields a discrete, jagged sequence of integers with not a trace of continuous geometry anywhere in sight. Yet in 1949, **André Weil** perceived an astonishing hidden architecture beneath those point counts: the sequence behaves exactly as if an algebraic variety over a finite field possessed topological "holes" like a sphere or a torus over $$\mathbb{C}$$, and its generating function obeys a full-fledged analogue of the Riemann hypothesis.

Turning that vision into a theorem took a quarter-century and a three-stage relay. **Bernard Dwork** (1960) proved rationality of the zeta function via $$p$$-adic analysis. **Alexander Grothendieck**, **Michael Artin**, and the **SGA** school constructed a vast new machine—**étale cohomology**—to express point counts via a Lefschetz trace formula and deduce the functional equation. Still, the deepest and most stubborn piece—the **Riemann-hypothesis analogue**, pinning down the exact moduli of the eigenvalues of Frobenius—resisted every attack. In 1974, at age 29, **Pierre Deligne** published *La conjecture de Weil: I*, bypassing his advisor Grothendieck’s still-open standard conjectures to prove the final purity estimate, and then generalized the entire machine to sheaves in *Weil II* (1980).

That breakthrough earned him the **Fields Medal 1978**, with the IMU noting that his solution of the Weil conjectures *"did much to unify algebraic geometry and algebraic number theory."* Let us keep the record crisp from the start: the 1978 medal does not mean Deligne built étale cohomology single-handedly, nor that the **standard conjectures** or the **Hodge conjecture** were solved. And his later **Abel Prize 2013** recognized an entire lifetime of transformative work—distinct from the 1978 Fields Medal.

**Lesson roadmap:** Background Knowledge Map (algebraic geometry, étale cohomology, Frobenius) → Hand-verifiable worked examples over $$\mathbb{F}_5$$ and $$\mathbb{F}_{25}$$ → The Weil conjectures and the three-stage relay → Deep-Dive Explanation (Read Slowly): how Deligne locks down Frobenius eigenvalues → *Weil II* and the Ramanujan–Petersson bound → Honest attribution & boundary with the classical Riemann hypothesis.

---

## Learning objectives

After this lecture you should be able to:

- State the Weil conjectures clearly: the zeta function of a smooth projective variety over a finite field is **rational**, satisfies a **functional equation**, and has zeros/poles on prescribed vertical lines (the **RH analogue** / **purity**).
- Compute by hand the zeta function $$Z(X,T)$$ for the projective line $$\mathbb{P}^1$$ and for an elliptic curve over $$\mathbb{F}_5$$, checking Hasse’s bound directly.
- Assign credit accurately: **Dwork** (rationality), **Grothendieck–Artin étale cohomology** (trace formula and functional equation), and **Deligne** (purity / RH analogue, *Weil I* and *Weil II*).
- Explain why étale cohomology is the *machine converting counts into traces*, while Deligne’s estimate on Frobenius eigenvalues is the *missing spectral bound*.
- State carefully that the **Ramanujan–Petersson** bounds for holomorphic cusp forms of weight $$\ge 2$$ follow from the Weil conjectures applied to higher-dimensional varieties (Kuga–Sato varieties), not from a single modular curve alone.
- Refuse common overclaims: Deligne did **not** prove the classical Riemann hypothesis, the standard conjectures, or the Hodge conjecture.

**Prerequisites.** Finite fields $$\mathbb{F}_q$$; the idea of a projective variety and of counting its rational points; Euler products and the classical Riemann hypothesis as a *model* for a statement about zeros. Schemes and derived categories are not required—think “a geometric cohomology theory with a Lefschetz trace formula.”

**Seminar links.** The classical RH, still open: [Riemann hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/). Arithmetic geometry neighbors: [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/) ($$L$$-functions of curves over $$\mathbb{Q}$$), [Langlands]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/), [Scholze / $$p$$-adic cohomology]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/). Lifetime-prize parallel: [What is the Abel Prize?]({{ site.baseurl }}/contents/en/chapter08/08_02_What_Is_Abel_Prize/).

---

## Background Knowledge Map: What Are Algebraic Geometry, Étale Cohomology, and Frobenius?

If you graduated in science or engineering without taking a graduate course in algebraic geometry, phrases like "$$\ell$$-adic étale cohomology" can sound intimidating. Underneath, three concrete ideas carry the whole story.

### 1. What does algebraic geometry over finite fields study?
In calculus, we study shapes defined by equations over $$\mathbb{R}$$ or $$\mathbb{C}$$ (like the sphere $$x^2 + y^2 + z^2 = 1$$) using derivatives and limits. **Algebraic geometry** studies solution sets of polynomial systems—**algebraic varieties**—over *any* field, including **finite fields** $$\mathbb{F}_q$$ (where $$q = p^r$$, such as $$\mathbb{F}_5 = \{0, 1, 2, 3, 4\}$$ with arithmetic modulo $$5$$). Arithmetic geometry asks three core questions:
- **Point counting:** How many points $$N_m = \#X(\mathbb{F}_{q^m})$$ does $$X$$ have as we climb the tower of extensions $$\mathbb{F}_q, \mathbb{F}_{q^2}, \mathbb{F}_{q^3}, \ldots$$?
- **Hidden geometry:** Does the integer sequence $$N_1, N_2, N_3, \ldots$$ remember the dimension and topological "holes" (genus $$g$$, Betti numbers) of the complex variety?
- **Sharp error bounds:** How closely does $$N_m$$ track naive estimates like $$q^m + 1$$?

### 2. Cohomology and the Lefschetz trace formula
In classical topology over $$\mathbb{C}$$, algebraic topology attaches to a space $$X$$ a sequence of finite-dimensional vector spaces $$H^0(X), H^1(X), \ldots, H^{2n}(X)$$. Their dimensions $$b_i = \dim H^i(X)$$—the **Betti numbers**—count $$i$$-dimensional holes:
- The sphere $$S^2 \cong \mathbb{P}^1(\mathbb{C})$$ has $$b_0 = 1,\; b_1 = 0,\; b_2 = 1$$.
- The torus $$T^2 \cong E(\mathbb{C})$$ (an elliptic curve) has $$b_0 = 1,\; b_1 = 2,\; b_2 = 1$$.

Crucially, every continuous map $$f: X \to X$$ induces a linear operator $$f^*$$ on each $$H^i(X)$$, and the **Lefschetz trace formula** counts its fixed points as an alternating sum of traces:

$$
\#\{x \in X : f(x) = x\} = \sum_{i=0}^{2n} (-1)^i \operatorname{Tr}\bigl(f^* \;\big\vert\; H^i(X)\bigr).
$$

### 3. The Frobenius map and étale cohomology
Over $$\mathbb{F}_q$$, geometry comes with a built-in endomorphism: the **Frobenius map** $$\mathrm{Frob}_q: (x_1, \ldots, x_k) \mapsto (x_1^q, \ldots, x_k^q)$$. By the finite-field version of Fermat’s little theorem ($$a^q = a \iff a \in \mathbb{F}_q$$), a point with coordinates in the algebraic closure $$\overline{\mathbb{F}}_q$$ lies in $$X(\mathbb{F}_{q^m})$$ **if and only if** it is a fixed point of $$\mathrm{Frob}_q^m$$!

The catch is that the classical Zariski topology of algebraic geometry is far too coarse to produce Betti numbers matching $$\mathbb{C}$$. **Grothendieck and Michael Artin** solved this by replacing "open subsets" with **étale covers** (the algebraic analogue of local diffeomorphisms), creating **étale cohomology** $$H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}}, \mathbb{Q}_\ell)$$ (with an auxiliary prime $$\ell \neq p$$). It recovers the classical Betti numbers, satisfies Poincaré duality and the Lefschetz trace formula, and turns arithmetic point-counting into linear algebra about Frobenius eigenvalues.

---

## 1. Hand-Verifiable Worked Examples: Counting Points over $$\mathbb{F}_5$$

Before stating the Weil conjectures in full generality, let us compute two concrete examples by hand so every symbol earns its keep.

### Example 1: The projective line $$\mathbb{P}^1$$ over $$\mathbb{F}_q$$
Over $$\mathbb{F}_{q^m}$$, $$\mathbb{P}^1$$ has $$q^m$$ finite points plus $$1$$ point at infinity, so $$N_m = q^m + 1$$. Substituting into the zeta generating function and using $$-\ln(1 - u) = \sum_{m\ge 1} u^m/m$$:

$$
Z(\mathbb{P}^1, T) = \exp\Bigl(\sum_{m\ge 1} (q^m + 1)\frac{T^m}{m}\Bigr) = \exp\bigl(-\ln(1 - qT) - \ln(1 - T)\bigr) = \frac{1}{(1 - T)(1 - qT)}.
$$

An infinite power series collapses into a simple **rational function**, with two denominator factors corresponding to the eigenvalues $$1 = q^{0/2}$$ on $$H^0$$ and $$q = q^{2/2}$$ on $$H^2$$!

### Example 2: The elliptic curve $$E: y^2 = x^3 + x + 1$$ over $$\mathbb{F}_5$$
Let us test every $$x \in \mathbb{F}_5 = \{0, 1, 2, 3, 4\}$$ (remembering the squares modulo $$5$$ are $$0^2 = 0,\; 1^2 = 4^2 = 1,\; 2^2 = 3^2 = 4$$):

| $$x \in \mathbb{F}_5$$ | $$x^3 + x + 1 \pmod 5$$ | Solutions $$y \in \mathbb{F}_5$$ | Finite points |
|---|---|---|---|
| $$0$$ | $$1$$ | $$y = 1, 4$$ | $$2$$ |
| $$1$$ | $$3$$ | None | $$0$$ |
| $$2$$ | $$8 + 2 + 1 = 11 \equiv 1$$ | $$y = 1, 4$$ | $$2$$ |
| $$3$$ | $$27 + 3 + 1 = 31 \equiv 1$$ | $$y = 1, 4$$ | $$2$$ |
| $$4$$ | $$64 + 4 + 1 = 69 \equiv 4$$ | $$y = 2, 3$$ | $$2$$ |

Adding $$1$$ point at infinity $$\mathcal{O}$$, we get:

$$
N_1 = \#E(\mathbb{F}_5) = 2 + 0 + 2 + 2 + 2 + 1 = 9.
$$

Check **Hasse’s bound**: the deviation from $$q + 1 = 6$$ is $$a_5 = (5 + 1) - 9 = -3$$, which satisfies $$\vert -3 \vert = 3 \le 2\sqrt{5} \approx 4.47$$!
Even better: the numerator polynomial is $$P_1(T) = 1 - a_5 T + 5T^2 = 1 + 3T + 5T^2$$, giving

$$
Z(E, T) = \frac{1 + 3T + 5T^2}{(1 - T)(1 - 5T)}.
$$

Factoring $$1 + 3T + 5T^2 = (1 - \alpha T)(1 - \bar{\alpha} T)$$ gives $$\alpha^2 + 3\alpha + 5 = 0$$, so

$$
\alpha, \bar{\alpha} = \frac{-3 \pm i\sqrt{11}}{2}, \qquad \vert\alpha\vert = \sqrt{\frac{9 + 11}{4}} = \sqrt{5} = 5^{1/2}!
$$

And from that single hand-count $$N_1 = 9$$ over $$\mathbb{F}_5$$, we can **predict the exact point count over $$\mathbb{F}_{25}$$** without testing 25 values of $$x$$:

$$
N_2 = 1 + 5^2 - (\alpha^2 + \bar{\alpha}^2) = 26 - \bigl((\alpha + \bar{\alpha})^2 - 2\alpha\bar{\alpha}\bigr) = 26 - (9 - 10) = 27!
$$

That is the miracle of the Weil conjectures in miniature: counting points over $$\mathbb{F}_q$$ reveals a characteristic polynomial whose complex eigenvalues sit **dead on the circle of radius $$\sqrt{q}$$**.

---

## 2. The Weil Conjectures (1949) and the Three-Stage Relay

Building on Hasse’s theorem for elliptic curves and his own proofs for curves of arbitrary genus ($$\vert N_1 - (q+1)\vert \le 2g\sqrt{q}$$) and abelian varieties, **André Weil** (1949) proposed four clauses for any smooth projective variety $$X$$ of dimension $$n$$ over $$\mathbb{F}_q$$ via the generating function

$$
Z(X,T)=\exp\Bigl(\sum_{m\ge 1}N_m\frac{T^m}{m}\Bigr),\qquad T=q^{-s}.
$$

1. **Rationality:** $$Z(X,T)$$ is a rational function of $$T$$, factoring as
   $$
   Z(X,T)=\frac{P_1(T)P_3(T)\cdots P_{2n-1}(T)}{P_0(T)P_2(T)\cdots P_{2n}(T)},
   $$
   with $$P_i(T) \in \mathbb{Z}[T]$$, $$P_0(T) = 1 - T$$, and $$P_{2n}(T) = 1 - q^n T$$.
2. **Functional equation:** $$Z(X, 1/(q^n T)) = \pm q^{n\chi/2} T^\chi Z(X, T)$$, where $$\chi$$ is the Euler–Poincaré characteristic.
3. **Riemann-hypothesis analogue (purity):** Every reciprocal root $$\alpha$$ of $$P_i(T)$$ is an algebraic integer with complex modulus $$\vert\alpha\vert = q^{i/2}$$ under every embedding into $$\mathbb{C}$$. Setting $$T = q^{-s}$$, all zeros and poles lie on the vertical lines $$\mathrm{Re}(s) = i/2$$.
4. **Betti numbers:** If $$X$$ lifts to a smooth projective variety over $$\mathbb{C}$$, then $$\deg P_i$$ equals its $$i$$-th Betti number $$b_i$$.

**The three-stage relay:**
- **Bernard Dwork (1960)** surprised everyone by proving **rationality** using $$p$$-adic analysis, without constructing any cohomology theory.
- **Grothendieck, Michael Artin, and SGA (1960s)** built **étale cohomology**, proved the Lefschetz trace formula and Poincaré duality, and recovered rationality, the functional equation, and the Betti-number comparison. Grothendieck hoped to deduce purity from his **standard conjectures** on algebraic cycles—but those conjectures remain open to this day!
- **Pierre Deligne (*Weil I*, 1974)** bypassed the standard conjectures completely to prove **purity** ($$\vert\alpha\vert = q^{i/2}$$).

---

## 3. Deep-Dive Explanation: How Deligne Locks Down Frobenius Eigenvalues (Read Slowly)

Once étale cohomology turns $$P_i(T)$$ into $$\det\bigl(1 - T\,\mathrm{Frob} \mid H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}}, \mathbb{Q}_\ell)\bigr)$$, why did proving $$\vert\alpha\vert = q^{i/2}$$ stop the Grothendieck school for a decade? Here is the 4-step architecture of Deligne’s *Weil I* (1974) and *Weil II* (1980):

#### Step 1: Poincaré duality collapses the equality into a single upper bound
By Poincaré duality in étale cohomology, if $$\alpha$$ is a Frobenius eigenvalue on $$H^i$$, then $$q^n/\alpha$$ is an eigenvalue on $$H^{2n-i}$$ (just as $$1$$ pairs with $$q$$ on $$\mathbb{P}^1$$, and $$\alpha$$ pairs with $$5/\alpha = \bar{\alpha}$$ on our elliptic curve). Therefore, if one proves the universal upper bound $$\vert\alpha\vert \le q^{i/2}$$ for *all* $$i$$ and all smooth projective varieties, applying it to $$q^n/\alpha$$ on $$H^{2n-i}$$ yields $$q^n/\vert\alpha\vert \le q^{(2n-i)/2} \iff \vert\alpha\vert \ge q^{i/2}$$, locking in the exact equality $$\vert\alpha\vert = q^{i/2}$$!

#### Step 2: Slicing the variety with a Lefschetz pencil
To argue by induction on dimension $$n$$, Deligne slices $$X$$ by a one-parameter family of hyperplanes—a **Lefschetz pencil**—parametrized by $$\mathbb{P}^1$$. Almost all slices are smooth $$(n-1)$$-dimensional varieties, except finitely many with mild nodal singularities. As a slice loops around those singular points, the cohomology $$H^{n-1}$$ undergoes transformations forming a **monodromy group**. By a theorem of Kazhdan–Margulis, this monodromy group is *maximally large* (the full symplectic group)—giving Deligne enormous geometric leverage.

#### Step 3: Rankin’s trick (even tensor powers $$2k$$) kills sign cancellation
Why is bounding an individual eigenvalue $$\alpha$$ from traces so tricky? Because complex eigenvalues can cancel each other out in sums! Borrowing **Rankin’s trick** from analytic number theory, Deligne takes the **$$2k$$-th tensor power** of the local system. Raising to an even power $$2k$$ makes all local Frobenius traces **non-negative real numbers**, eliminating cancellation! If any eigenvalue broke the barrier ($$\vert\alpha\vert > q^{i/2}$$), then as $$k \to \infty$$ its $$2k$$-th power would force a pole outside the convergence region dictated by the huge monodromy group from Step 2—a flat contradiction! Taking $$2k$$-th roots and letting $$k \to \infty$$ erases every auxiliary constant, leaving the razor-sharp bound $$\vert\alpha\vert \le q^{i/2}$$.

#### Step 4: From varieties to sheaves (*Weil II*, 1980)
In *La conjecture de Weil: II* (1980), Deligne lifted the theory from constant sheaves on smooth projective varieties to **mixed constructible $$\ell$$-adic sheaves** on general schemes over finite fields, proving that compactly supported direct images $$Rf_!$$ respect weight inequalities (if the input has weight $$\le w$$, then $$R^i f_!$$ has weight $$\le w + i$$). Armed with *Weil II*, deep estimates on exponential sums in analytic number theory became routine geometric weight calculations.

Summary of Deligne’s breakthrough:

$$
\text{Point counts } N_m
\;\longleftrightarrow\;
\text{Frobenius traces (Grothendieck)}
\;\longleftrightarrow\;
\text{Lefschetz pencil + Monodromy}
\;\longleftrightarrow\;
\text{Even power } 2k \text{ (Rankin)} \implies \vert\alpha\vert = q^{i/2}.
$$

Katz’s Helsinki ICM report remains the classic guide to this proof architecture at the time of the medal.

---

## 4. Ramanujan–Petersson, Honest Attribution, and What Remains Open

**Ramanujan–Petersson, stated carefully.** For Ramanujan’s tau function $$\tau(n)$$—the Fourier coefficients of the weight-12 discriminant modular form $$\Delta(q) = q \prod_{m\ge 1}(1 - q^m)^{24} = \sum_{n\ge 1} \tau(n)q^n$$—the famous conjecture

$$
\vert\tau(p)\vert \le 2p^{11/2}
$$

is the RH analogue for a weight-$$11$$ motive. In 1969 (following Serre’s insight), Deligne attached $$\ell$$-adic Galois representations to holomorphic cusp forms of weight $$k \ge 2$$ and reduced the Ramanujan–Petersson bound to the Weil conjectures for higher-dimensional **Kuga–Sato varieties** (built from $$(k-2)$$-fold fibered powers of the universal elliptic curve over a modular curve—dimension $$11$$ for $$\Delta$$!). Thus *Weil I* (1974) immediately implied $$\vert\tau(p)\vert \le 2p^{11/2}$$. Weight $$1$$ is a separate story completed by **Deligne–Serre**, while classical one-variable Kloosterman-sum bounds already followed from Weil’s theorem for curves before 1974.

**What is not proved.** Grothendieck’s **standard conjectures** remain open as a package (though Deligne deduced hard Lefschetz in positive characteristic from *Weil II*). The **Hodge conjecture** remains open; Deligne’s **mixed Hodge structures** and **absolute Hodge cycles** are powerful tools, not a proof of Hodge.

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

Deligne was born in 1944 in Belgium, wrote his thesis under Grothendieck, and spent the Fields years at IHÉS before moving to the Institute for Advanced Study. His **Abel Prize 2013** is a *lifetime* honor covering mixed Hodge theory, Deligne–Lusztig representations, moduli of curves with Mumford, and far more—keep it separate from the 1978 Fields Medal.

**Why it still matters.** The classical [Riemann hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) over $$\mathbb{Q}$$ remains open. That does not diminish the Weil story—it shows why number theorists still dream of finding a "cohomology" and a "Frobenius" for $$\mathrm{Spec}(\mathbb{Z})$$.

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

## Video tham khảo

- **xem trước** — [Timothy Gowers: The Weil conjectures explained](https://www.youtube.com/watch?v=PHkYqPX3Je4) — The Abel Prize, English. Watch first. “Timothy Gowers: The Weil conjectures explained” orients the lesson’s aim: State the Weil conjectures at slogan level: the zeta function of a smooth projective variety over a finite field is rational, satisfies a functional equation, and has zeros/poles o…
- [The Weil Conjectures, from Abel to Deligne - Sophie Morel](https://www.youtube.com/watch?v=iDgtP6ZpR70) — Institute for Advanced Study, English. A second pass once the main claim is in view: State the Weil conjectures at slogan level: the zeta function of a smooth projective variety over a finite field is rational, satisfies a functional equation, and has zeros/poles o…
- [The Weil conjectures - Lothar Goettsche - 2016](https://www.youtube.com/watch?v=kiQwnXT7j7g) — ICTP Mathematics, English. Further depth after the first two, still tied to this lesson: State the Weil conjectures at slogan level: the zeta function of a smooth projective variety over a finite field is rational, satisfies a functional equation, and has zeros/poles o…
