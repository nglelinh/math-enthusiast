---
layout: post
title: "Kontsevich’s Quantization, Curves, and Knots (Fields Medal 1998)"
chapter: '02'
order: 22
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

In the early 1990s, theoretical physics kept tossing astonishing prophecies across the fence to mathematics: from 2D quantum gravity, Edward Witten predicted that geometric intersection numbers on moduli spaces of curves must obey the shallow-water Korteweg–de Vries (KdV) equation; from Chern–Simons quantum field theory, physicists suggested that formally ill-defined path integrals encode every finite-type invariant of knots in $$\mathbb{R}^3$$; and from quantum mechanics, a 20-year-old algebraic question still stood open—can *every* classical Poisson phase space be deformation-quantized?

**Maxim Kontsevich** stepped straight into that crossroads armed with a single, razor-sharp instinct: **weighted sums over graphs**, where the weights are integrals over configuration spaces. One by one, he turned all three into rigorous theorems, earning the **Fields Medal 1998**:

> “For his contributions to algebraic geometry, topology, and mathematical physics, including the proof of Witten's conjecture of intersection numbers in moduli spaces of stable curves, construction of the universal Vassiliev invariant of knots, and formal quantization of Poisson manifolds.”
> — IMU citation, ICM 1998 (as recorded in the [Fields Medal](https://www.mathunion.org/imu-awards/fields-medal) record and standard biographical sources)

Because Kontsevich (born 1964, permanent professor at IHÉS) later launched monumental programs such as **homological mirror symmetry** (HMS), motivic integration, and wall-crossing, it is tempting to rewrite the 1998 list in hindsight. This essay stays faithful to the official triad—**Witten’s conjecture** on $$\overline{\mathcal{M}}_{g,n}$$, the **universal Vassiliev invariant**, and **formal deformation quantization** of Poisson manifolds—while placing homological mirror symmetry in its proper seat: a landmark 1994 ICM proposal, not the third bullet of the 1998 Fields Medal.

**Lesson roadmap:** Key ideas (Poisson manifolds, moduli spaces $$\overline{\mathcal{M}}_{g,n}$$, Vassiliev knot invariants) → Hand-verifiable worked examples (Moyal star product on $$q \star p$$ and $$q^2 \star p^2$$, plus the first intersection numbers on $$\overline{\mathcal{M}}_{g,n}$$) → Witten’s conjecture & the Kontsevich integral → Explanation: Formality theorem and the upper-half-plane graph formula → Homological mirror symmetry (1994) & keeping the 1998 record clean.

---

## Learning objectives

After this lecture you should be able to:

- Recite the 1998 citation as **three** distinct theorems, refusing to swap the third bullet for homological mirror symmetry.
- Compute the Moyal star product by hand up to order $$\hbar^2$$ on $$(q,p)$$ to see associativity and the first-order Poisson bracket in action.
- State Witten’s conjecture (generating function of $$\psi$$-class intersections on $$\overline{\mathcal{M}}_{g,n}$$ is a KdV tau-function) and explain how Kontsevich proved it via Strebel ribbon graphs and a matrix Airy integral.
- Describe the Kontsevich integral as the **universal finite-type (Vassiliev) knot invariant**, crediting Vassiliev and Bar-Natan for the combinatorial framework.
- Explain why general Poisson manifolds are far harder than symplectic manifolds (no Darboux coordinates), and how Kontsevich’s **formality theorem** and graph formula solve the problem formally.
- Place these results on the [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/) map without confusing physical heuristics for proofs.

**Prerequisites.** The idea of a moduli space of curves; Poisson brackets on $$\mathbb{R}^{2n}$$ or on a symplectic manifold; the Jones polynomial as “a knot invariant that is not just the fundamental group.” Complex analysis and a first algebraic geometry course help; quantum field theory is optional atmosphere.

**Seminar links.** [Mirror symmetry]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/) for the HMS program as a *later reading*, kept separate from 1998. [Pardon / symplectic]({{ site.baseurl }}/contents/en/chapter02/02_13_Pardon_Symplectic/) for Fukaya-side consumers of HMS.

---

## Key ideas: What Do Deformation Quantization, Moduli Spaces, and Knot Theory Study?

### 1. Deformation quantization of Poisson manifolds
In classical mechanics, observables are smooth functions $$f(q,p), g(q,p)$$ on phase space multiplied point-by-point ($$fg = gf$$), equipped with an antisymmetric **Poisson bracket** $$\{f, g\}$$ obeying the Jacobi identity and Leibniz rule (a **Poisson manifold**). In quantum mechanics, position and momentum no longer commute: $$[\hat{q}, \hat{p}] = i\hbar$$. **Deformation quantization** asks an algebraic question: *can we deform pointwise multiplication into an **associative** star product $$f \star g = fg + \hbar B_1(f,g) + \hbar^2 B_2(f,g) + \cdots$$ on $$C^\infty(M)[\![\hbar]\!]$$ such that $$f\star g - g\star f = i\hbar\{f,g\} + O(\hbar^2)$$?*

### 2. Moduli spaces $$\overline{\mathcal{M}}_{g,n}$$ and intersection theory
The set of all complex algebraic curves (Riemann surfaces) of genus $$g$$ with $$n$$ marked points forms the **moduli space** $$\mathcal{M}_{g,n}$$; adding degenerate nodal curves yields the compact Deligne–Mumford space $$\overline{\mathcal{M}}_{g,n}$$ of complex dimension $$3g - 3 + n$$. Intersection theory asks what numerical laws govern integrals of natural tautological classes (the **$$\psi$$-classes**) over $$\overline{\mathcal{M}}_{g,n}$$.

### 3. Finite-type (Vassiliev) knot invariants
A **knot** is a closed loop in $$\mathbb{R}^3$$. **Vassiliev** organized knot invariants like higher-order derivatives: every time you flip an over-crossing to an under-crossing, you take the difference; an invariant that vanishes after $$m + 1$$ crossing differences has **finite type $$\le m$$**. The key question: *is there one universal invariant from which every finite-type invariant factors?*

---

## 1. Hand-Verifiable Worked Examples: The Moyal Star Product and First Intersection Numbers

### Example 1: Computing the Moyal star product on $$\mathbb{R}^2$$ by hand
On the classical phase plane $$(q,p)$$ with the constant Poisson bracket $$\{f,g\} = f_q g_p - f_p g_q$$ (so $$\{q,p\} = 1$$), the **Moyal star product** is:

$$
(f \star g)(q,p) = fg + \frac{i\hbar}{2}(f_q g_p - f_p g_q) + \frac{1}{2!}\left(\frac{i\hbar}{2}\right)^2(f_{qq}g_{pp} - 2f_{qp}g_{qp} + f_{pp}g_{qq}) + \cdots
$$

Plug in two concrete pairs:
1. **$$f = q,\; g = p$$:** only first derivatives survive ($$f_q = 1, g_p = 1$$):
   $$
   q \star p = qp + \frac{i\hbar}{2}, \qquad p \star q = pq - \frac{i\hbar}{2} \;\Longrightarrow\; q \star p - p \star q = i\hbar = i\hbar\{q, p\}!
   $$
2. **$$f = q^2,\; g = p^2$$:** here $$f_q = 2q, f_{qq} = 2$$ and $$g_p = 2p, g_{pp} = 2$$, activating the $$\hbar^2$$ term:
   $$
   q^2 \star p^2 = q^2 p^2 + 2i\hbar qp - \frac{\hbar^2}{2}.
   $$
   Check associativity on $$(q \star q) \star p = q^2 \star p = q^2 p + i\hbar q$$ versus $$q \star (q \star p) = q \star (qp + \tfrac{i\hbar}{2}) = q^2 p + \tfrac{i\hbar}{2}q + \tfrac{i\hbar}{2}q = q^2 p + i\hbar q$$—exact match!

Moyal’s formula works effortlessly *only* because the Poisson bivector $$\pi$$ has constant coefficients! On a general Poisson manifold where $$\pi(x)$$ varies with $$x$$ (such as $$\{x,y\} = xy$$), derivatives of $$\pi$$ break Moyal’s associativity right at order $$\hbar^2$$!

### Example 2: The first two intersection numbers of Witten’s conjecture
The tautological intersection numbers $$\langle\tau_{d_1}\cdots\tau_{d_n}\rangle_g = \int_{\overline{\mathcal{M}}_{g,n}} \psi_1^{d_1}\cdots\psi_n^{d_n}$$ vanish unless $$\sum d_i = 3g - 3 + n$$:
- For $$g = 0, n = 3$$: $$\dim\overline{\mathcal{M}}_{0,3} = 0$$ (a single point), so $$\langle\tau_0^3\rangle_0 = 1$$.
- For $$g = 1, n = 1$$: $$\dim\overline{\mathcal{M}}_{1,1} = 1$$, and the orbifold integral gives $$\langle\tau_1\rangle_1 = \frac{1}{24}$$.

**Witten’s conjecture** asserted that the generating function of *all* these numbers is a tau-function of the **KdV hierarchy**—meaning the KdV / Virasoro recursion uniquely computes every single number in every genus starting solely from $$\langle\tau_0^3\rangle_0 = 1$$!

---

## 2. The First Two Bullets of Fields 1998: Witten’s Conjecture and the Kontsevich Integral

**1. Proving Witten’s conjecture (1992).** In *Intersection theory on the moduli space of curves and the matrix Airy function* (*Comm. Math. Phys.* 147), Kontsevich used **Strebel differentials** to cut each marked Riemann surface canonically into a **ribbon graph** ("fat graph"). This cell decomposition converts geometric integrals of $$\psi$$-classes on $$\overline{\mathcal{M}}_{g,n}$$ into a **sum over trivalent ribbon graphs**—which, by Feynman rules, is precisely the asymptotic expansion of a **matrix Airy integral** over $$N\times N$$ Hermitian matrices! Since the matrix Airy integral was already known to satisfy KdV, Witten’s conjecture became a theorem.

**2. The universal Vassiliev invariant (1993).** **Vassiliev** introduced the finite-type filtration and **Bar-Natan** systematized the combinatorics of **chord diagrams** and **weight systems** (linking Lie algebras like $$\mathfrak{sl}_2$$ to the Jones polynomial). Kontsevich supplied the missing **universal** analytic invariant: embedding a knot $$K \subset \mathbb{C} \times \mathbb{R}$$ and taking **iterated integrals** of $$\frac{dz_j - dz'_j}{z_j - z'_j}$$ over configuration spaces of horizontal slice points. At degree $$1$$ it recovers Gauss’s classical linking integral; at all degrees it realizes the perturbative Chern–Simons expansion suggested by Witten, and every finite-type invariant factors through it.

---

## 3. Explanation: The Formality Theorem and Poisson Quantization

Why did deformation quantization of general **Poisson manifolds** remain open for 20 years after De Wilde–Lecomte (1983) and Fedosov (1994) solved the symplectic case? Here is Kontsevich’s 4-step breakthrough (1997 preprint arXiv:q-alg/9709040; *Lett. Math. Phys.* 2003):

#### Step 1: Why symplectic gluing fails on Poisson manifolds
On a symplectic manifold, Darboux’s theorem provides local coordinates where $$\pi$$ is constant, so one can glue local Moyal star products together. On a general Poisson manifold (like $$\{x, y\} = x^2 + y^2$$, where $$\pi$$ vanishes at the origin), no Darboux chart exists—any local formula must be **canonical** for arbitrary varying $$\pi$$.

#### Step 2: Recast both sides as Maurer–Cartan equations in two DGLAs
Kontsevich embedded both "Poisson structures" and "associative star products" as solutions of the **Maurer–Cartan equation** $$d\gamma + \frac{1}{2}[\gamma,\gamma] = 0$$ in two differential graded Lie algebras:
- **Geometric side ($$T_{\mathrm{poly}}$$):** polyvector fields with the Schouten–Nijenhuis bracket and $$d = 0$$; Maurer–Cartan elements are Poisson bivectors $$[\pi, \pi] = 0$$.
- **Algebraic side ($$D_{\mathrm{poly}}$$):** Hochschild cochains (multidifferential operators on $$C^\infty(M)$$); Maurer–Cartan elements are **associative star products**!

By the Hochschild–Kostant–Rosenberg (HKR) theorem, $$T_{\mathrm{poly}}$$ is the cohomology of $$D_{\mathrm{poly}}$$, but the linear HKR map fails to preserve the Lie bracket!

#### Step 3: The Formality Theorem ($$L_\infty$$ quasi-isomorphism)
Kontsevich proved that although the linear HKR map misses the bracket, one can add higher nonlinear maps $$U_1, U_2, U_3, \ldots$$ to build an **$$L_\infty$$ quasi-isomorphism** from $$T_{\mathrm{poly}}$$ to $$D_{\mathrm{poly}}$$! Immediately, every Maurer–Cartan element on the geometric side (every Poisson structure $$\pi$$) maps to a Maurer–Cartan element on the algebraic side (an **associative star product**), classifying star products up to gauge equivalence in 1–1 correspondence with formal Poisson structures!

#### Step 4: The explicit upper-half-plane graph formula
On $$\mathbb{R}^d$$, Kontsevich wrote down the star product explicitly:

$$
f \star g = fg + \sum_{n=1}^{\infty} \frac{\hbar^n}{n!} \sum_{\Gamma \in G_n} w_\Gamma \, B_{\Gamma, \pi}(f, g).
$$

Each admissible directed graph $$\Gamma$$ has $$n$$ interior vertices (carrying $$\pi$$) and $$2$$ boundary vertices (carrying $$f, g$$), defining a bidifferential operator $$B_{\Gamma,\pi}(f,g)$$. Its numerical weight $$w_\Gamma$$ is an explicit integral of hyperbolic angle forms over the configuration space of $$n$$ points in the **Poincaré upper half-plane** $$\mathbb{H}$$! Stokes’s theorem on the compactified configuration-space boundary proves associativity to every order in $$\hbar$$!

Summary of the graph-integral thread uniting all three 1998 theorems:

$$
\text{Ribbon graphs} \leftrightarrow \text{Witten–KdV}, \qquad
\text{Chord diagrams} \leftrightarrow \text{Universal Vassiliev}, \qquad
\text{Graphs on } \mathbb{H} \leftrightarrow \text{Poisson star product}.
$$

*(Note: "formal" means in formal power series $$\mathbb{R}[\![\hbar]\!]$$; analytic convergence in $$\hbar$$ and Hilbert-space quantization are separate questions.)*

---

## 4. Related Programs Not in the 1998 Triad, and Why a Fields Medal

- **Homological mirror symmetry (HMS):** Proposed in Kontsevich’s famous 1994 ICM address (arXiv:alg-geom/9411018) as an equivalence between the derived category of coherent sheaves on a Calabi–Yau $$X$$ and the Fukaya category of its mirror $$Y$$. Many landmark cases are now theorems by many authors, but it remains an ongoing program (see [Mirror Symmetry]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/))—**not** the third bullet of Fields 1998.
- **Motivic integration** (1995 Orsay lecture, developed by **Denef–Loeser**) and **stable maps** (Gromov–Witten compactification) are major adjacent achievements outside the official 1998 triad.

**Why a Fields Medal:** Kontsevich turned physical intuition into three rigorous graph-integral dictionaries across algebraic geometry, topology, and mathematical physics—demonstrating that mathematical physics can supply complete algebraic structures and proofs, not merely metaphors.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Kontsevich solved mirror symmetry.” | He proposed HMS in 1994; it is a program, with theorems in many cases by many authors. |
| “Fields 1998 = homological mirror symmetry.” | The third official bullet is formal quantization of Poisson manifolds. |
| “Witten’s conjecture classifies all curves.” | It constrains $$\psi$$-intersection numbers on $$\overline{\mathcal{M}}_{g,n}$$ via KdV. |
| “The Kontsevich integral is the Jones polynomial.” | It is a universal finite-type invariant; Jones is one of many specializations / extractions. |
| “Formal quantization is a Hilbert-space quantum mechanics.” | It is an associative deformation over $$\mathbb{R}[\![\hbar]\!]$$; analysis of convergence is separate. |
| “Motivic integration is a 1998 Fields result.” | Adjacent later work (Kontsevich lecture; Denef–Loeser). |

---

## Links

- IMU Fields Medal page: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Wikipedia — Maxim Kontsevich: [https://en.wikipedia.org/wiki/Maxim_Kontsevich](https://en.wikipedia.org/wiki/Maxim_Kontsevich)
- Kontsevich, deformation quantization (arXiv:q-alg/9709040): [https://arxiv.org/abs/q-alg/9709040](https://arxiv.org/abs/q-alg/9709040)
- Kontsevich, homological algebra of mirror symmetry (arXiv:alg-geom/9411018): [https://arxiv.org/abs/alg-geom/9411018](https://arxiv.org/abs/alg-geom/9411018)
- AMS Notices, “The Mathematical Work of the 1998 Fields Medalists”: [https://www.ams.org/notices/199901/fields.pdf](https://www.ams.org/notices/199901/fields.pdf)
- arXiv search — Kontsevich Witten moduli: [https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all](https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all)

---

## References

1. IMU Fields Medal 1998 citation — Maxim Kontsevich (ICM Berlin opening; see also Taubes, “The work of Maxim Kontsevich,” ICM 1998).
2. M. Kontsevich, “Intersection theory on the moduli space of curves and the matrix Airy function,” *Comm. Math. Phys.* 147 (1992).
3. E. Witten, two-dimensional gravity and intersection theory on moduli space (the conjecture).
4. M. Kontsevich, “Deformation quantization of Poisson manifolds,” *Lett. Math. Phys.* 66 (2003); preprint q-alg/9709040.
5. V. Vassiliev, finite-type knot invariants; D. Bar-Natan, weight systems and diagram complexes.
6. M. Kontsevich, “Homological algebra of mirror symmetry,” *Proc. ICM Zürich 1994* — related program, not the third 1998 bullet.
7. J. Denef and F. Loeser, papers on motivic integration (after Kontsevich’s Orsay lecture).
8. Course: [Mathematical Physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/), [Mirror Symmetry]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/).

---

## Further directions

- Read a modern exposition of tautological classes on $$\overline{\mathcal{M}}_{g,n}$$ to see what Witten–Kontsevich does *not* compute.
- If you continue to HMS, keep a two-column notebook: “1994 proposal” vs “theorems proved by later authors.”

## Video tham khảo

- **xem trước** — [HLF Laureate Portraits: Maxim Kontsevich](https://www.youtube.com/watch?v=1CXvSRQVoZY) — Heidelberg Laureate Forum, English. Watch first. “HLF Laureate Portraits: Maxim Kontsevich” orients the lesson’s aim: Recite the 1998 citation as three results, and refuse to replace the third bullet by homological mirror symmetry.
- [Maxim Kontsevich | On the History of quantum cohomology and homological mirror symmetry](https://www.youtube.com/watch?v=Ml2x5NnEQ1I) — Harvard CMSA, English. A second pass once the main claim is in view: Recite the 1998 citation as three results, and refuse to replace the third bullet by homological mirror symmetry.
