---
layout: post
title: "Hairer’s Regularity Structures (Fields Medal 2014)"
chapter: '02'
order: 21
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Watch the jagged glowing front of a burning sheet of paper, or the rough surface of falling snow piling up on a windowsill. Physicists love writing down partial differential equations driven by "white noise" to capture billions of tiny random kicks. On a chalkboard, those equations look crisp and evocative; to a mathematical analyst, they are a **logical nightmare**: the solutions are so rough that even squaring a derivative or cubing the solution means multiplying two infinite distributions together—an operation that has no meaning at all!

For decades, famous equations like **KPZ** and **dynamical $$\Phi^4_3$$** hung in mathematical limbo: everyone believed they described nature, yet nobody knew how to *define* what a solution even meant. In 2014, **Martin Hairer** received the **Fields Medal**

> “for his outstanding contributions to the theory of stochastic partial differential equations, and in particular for the creation of a theory of regularity structures for such equations.”
> — [IMU, Fields Medals 2014](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014)

This medal honors the creation of a **new language**. By upgrading classical Taylor polynomials—adding abstract "noise monomials" built directly from white noise alongside $$1, x, x^2, \ldots$$—Hairer’s **regularity structures** let analysts multiply rough distributions algebraically, perform **renormalization** rigorously, and then "reconstruct" a genuine solution. Along the way, we place Hairer’s theory beside **Terry Lyons’s rough paths** and the independent **paracontrolled distributions** of Gubinelli–Imkeller–Perkowski, while keeping two boundaries crisp: this does not solve the Clay 3D Navier–Stokes problem, and Hairer’s physics PhD is biography, not the theorem.

**Lesson roadmap:** Background Knowledge Map (distributions, white noise, singular SPDEs) → Hand-verifiable worked examples (why $$\delta_0^2$$ blows up & the regularity power-counting table for KPZ and $$\Phi^4_3$$) → Deep-Dive Explanation (Read Slowly): 4 steps from noise-tree Taylor expansions to reconstruction, renormalization, and Banach fixed points → Rough paths & paracontrolled distributions → Scope and limits of the medal.

---

## Learning objectives

After this lecture you should be able to:

- Compute by hand why $$\delta_\varepsilon(x)^2$$ diverges and use regularity power-counting to explain why $$(\partial_x h)^2$$ in KPZ and $$\Phi^3$$ in $$\Phi^4_3$$ are classically ill-defined.
- Describe a **regularity structure** $$(\mathcal{A}, T, G)$$ as an upgraded Taylor expansion containing noise-built tree monomials.
- Explain Hairer’s three-step engine: the **reconstruction theorem**, **model renormalization**, and a deterministic **Banach fixed-point** argument.
- Credit **Lyons’s rough paths** as a predecessor and **paracontrolled distributions** (Gubinelli–Imkeller–Perkowski) as a parallel independent toolkit.
- State the exact scope: **subcritical parabolic** singular SPDEs—not all SPDEs, and not the Clay 3D deterministic Navier–Stokes problem.

**Prerequisites.** The heat equation and the idea of a PDE; Brownian motion as a continuous but nowhere differentiable path; distributions as continuous linear functionals on test functions. Stochastic integrals at the level of “white noise is the derivative of Brownian motion” are enough. No prior rough-path course is assumed.

**Seminar links.** Place the story on the [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/) map (which already flags Hairer’s SPDEs as a well-posedness problem). Contrast with [Deng PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) (deterministic kinetic limits) and with [Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/) (regularity of nonlinear PDE *without* space-time white noise).

---

## Background Knowledge Map: What Do Distributions, White Noise, and Singular SPDEs Study?

### 1. Distributions: free derivatives at the price of multiplication
A step function jumping from $$0$$ to $$1$$ at $$x = 0$$ has no classical derivative. Laurent Schwartz’s **theory of distributions** defines generalized functions by testing against smooth functions $$\varphi$$: $$\langle u, \varphi \rangle = \int u(x)\varphi(x)\,dx$$. Integration by parts makes every distribution infinitely differentiable (the step function’s derivative is the Dirac delta $$\delta_0$$), but the price is steep: **two rough distributions cannot generally be multiplied**.

### 2. Brownian motion and space-time white noise
**Brownian motion** $$B_t$$ is continuous everywhere yet nowhere differentiable: $$\vert B_{t+h} - B_t \vert \sim \vert h \vert^{1/2}$$, giving Hölder regularity $$1/2-$$ (meaning $$1/2 - \kappa$$ for every $$\kappa > 0$$). Its distributional derivative is **white noise** $$\xi$$, which has *negative* regularity. In parabolic space-time with $$d$$ spatial dimensions (where time counts double because $$t \sim x^2$$, giving parabolic dimension $$d + 2$$), space-time white noise has regularity:

$$
\mathrm{reg}(\xi) = -\frac{d+2}{2}-.
$$

### 3. Why singular SPDEs break Itô calculus
Classical Itô calculus (1940s) solves ordinary SDEs in 1D time by separating past from future. For nonlinear **SPDEs** in space-time, space has no past/future arrow. When solutions are so rough that nonlinear terms multiply distributions whose regularities sum to $$\le 0$$, the equation is **singular**: making sense of it requires smoothing the noise to $$\xi^\varepsilon$$, subtracting explicit diverging counterterms (**renormalization**), and proving convergence as $$\varepsilon \to 0$$.

---

## 1. Hand-Verifiable Worked Examples: Why $$\delta_0^2$$ Blows Up and Power-Counting KPZ & $$\Phi^4_3$$

### Example 1: Squaring a Dirac delta box approximation
Approximate $$\delta_0$$ by a narrow rectangle of width $$\varepsilon$$ and height $$1/\varepsilon$$ around $$0$$:

$$
\delta_\varepsilon(x) = \frac{1}{\varepsilon}\,\mathbf{1}_{[-\varepsilon/2,\, \varepsilon/2]}(x).
$$

Its area is $$\varepsilon \cdot (1/\varepsilon) = 1$$, so $$\delta_\varepsilon \to \delta_0$$. Now **square** it: the box still has width $$\varepsilon$$, but its height shoots to $$1/\varepsilon^2$$, giving total area:

$$
\int_{\mathbb{R}} \delta_\varepsilon(x)^2\,dx = \varepsilon \cdot \frac{1}{\varepsilon^2} = \frac{1}{\varepsilon} \xrightarrow{\varepsilon \to 0} +\infty!
$$

The golden rule of harmonic analysis (Young/Bony) says a canonical product $$u \cdot v$$ exists only when **$$\mathrm{reg}(u) + \mathrm{reg}(v) > 0$$**.

### Example 2: Regularity power-counting for KPZ and dynamical $$\Phi^4_3$$
The heat inverse $$(\partial_t - \Delta)^{-1}$$ always **adds $$+2$$** to regularity, while a spatial derivative $$\partial_x$$ **subtracts $$-1$$**. Add the numbers directly:

| Equation | Spatial dim $$d$$ | Noise $$\xi$$ | Solution regularity (after $$+2$$) | Nonlinear term & sum of regularities |
|---|---|---|---|---|
| Stochastic heat $$\partial_t u = \Delta u + \xi$$ | $$d = 1$$ | $$-3/2-$$ | $$u \sim +1/2-$$ | None (linear, well-posed!) |
| **KPZ**: $$\partial_t h = \partial_x^2 h + (\partial_x h)^2 + \xi$$ | $$d = 1$$ | $$-3/2-$$ | $$h \sim +1/2- \implies \partial_x h \sim -1/2-$$ | $$(\partial_x h)^2$$: $$(-1/2-) + (-1/2-) = \mathbf{-1- < 0}$$ (Illegal!) |
| **Dynamical $$\Phi^4_3$$**: $$\partial_t\Phi = \Delta\Phi - \Phi^3 + \xi$$ | $$d = 3$$ | $$-5/2-$$ | $$\Phi \sim -1/2-$$ (a distribution!) | $$\Phi^3$$: $$3 \times (-1/2-) = \mathbf{-3/2- < 0}$$ (Illegal!) |

Those negative sums **$$-1-$$** and **$$-3/2-$$** show immediately why KPZ and $$\Phi^4_3$$ fail classically—and why smoothing the noise to $$\xi^\varepsilon$$ shifts $$(\partial_x h^\varepsilon)^2$$ by a diverging constant $$C_\varepsilon \sim 1/\varepsilon$$ that must be subtracted!

---

## 2. Deep-Dive Explanation: How Regularity Structures Tame Infinities (Read Slowly)

Martin Hairer (born 1975 in Geneva, physics PhD 2001 under Jean-Pierre Eckmann) had already proved ergodicity of 2D stochastic Navier–Stokes with degenerate noise (with Jonathan Mattingly, *Annals*, 2006) and drew inspiration from **Terry Lyons’s rough paths**. After solving KPZ pathwise in 2013 (*Annals*), he unveiled the general framework in *A theory of regularity structures* (*Inventiones*, 2014; arXiv:1303.5113) in four clean steps:

#### Step 1: Upgrade Taylor polynomials with "noise trees"
A smooth function $$f \in C^\gamma$$ looks locally like a Taylor polynomial in $$1, (y-x), (y-x)^2, \ldots$$. A singular SPDE solution does *not* look like a polynomial at tiny scales—it looks like iterated integrals of white noise!
Hairer defines a **regularity structure** $$(\mathcal{A}, T, G)$$ by adding a finite library of **tree symbols** (such as $$\Xi$$ for $$\xi$$ of degree $$-5/2-$$, $$\mathcal{I}(\Xi)$$ for the linear solution of degree $$-1/2-$$, $$\mathcal{I}(\Xi)^2$$ of degree $$-1-$$, etc.) alongside ordinary polynomials:
- $$\mathcal{A} \subset \mathbb{R}$$: homogeneity degrees (now allowing negative degrees);
- $$T = \bigoplus_{\alpha \in \mathcal{A}} T_\alpha$$: graded vector space spanned by polynomials and noise trees;
- $$G$$: structure group recentering expansions from basepoint $$y$$ to $$x$$ (generalizing the binomial theorem).

Inside the abstract algebra $$T$$, **multiplying two symbols simply grafts their trees together**—completely legal algebraically!

#### Step 2: Models $$(\Pi, \Gamma)$$ and the Reconstruction Theorem (Algebra $$\to$$ Analysis)
A **model** $$(\Pi, \Gamma)$$ turns each abstract symbol $$\tau \in T$$ at basepoint $$x$$ into an actual distribution $$\Pi_x\tau$$ scaling like $$\lambda^{\vert\tau\vert}$$ at scale $$\lambda$$. A **modelled distribution** $$f(x) \in T$$ is an abstract jet whose coefficients vary smoothly under recentering $$\Gamma_{xy}$$.
**Reconstruction Theorem:** If $$f$$ has positive regularity $$\gamma > 0$$, there exists a **unique** genuine distribution $$\mathcal{R}f \in \mathcal{S}'$$ that looks like $$\Pi_x f(x)$$ near every point $$x$$ up to error $$\lambda^\gamma$$.

#### Step 3: Renormalizing the model (Isolating all the probability in one place)
Smoothing $$\xi$$ to $$\xi^\varepsilon$$ produces natural models $$(\Pi^\varepsilon, \Gamma^\varepsilon)$$, whose nonlinear trees blow up as $$\varepsilon \to 0$$. Because the SPDE is **subcritical** (at small scales the nonlinearity weakens relative to the heat operator), only **finitely many** negative-degree trees diverge! Acting by a renormalization group (built from a Hopf algebra of rooted trees) subtracts a finite list of local counterterms (such as $$-C_\varepsilon \Phi$$ in $$\Phi^4_3$$), so the renormalized models $$(\hat{\Pi}^\varepsilon, \hat{\Gamma}^\varepsilon)$$ **converge probabilistically** to a limiting model $$(\hat{\Pi}, \hat{\Gamma})$$. Crucially, this probabilistic work is done *once* for finitely many basis trees!

#### Step 4: A completely deterministic Banach fixed point
Once the limiting model $$(\hat{\Pi}, \hat{\Gamma})$$ is in hand, everything else is **100% deterministic**: on the Banach space of modelled distributions, the singular SPDE becomes a short-time contraction mapping solved by Picard iteration! Applying $$\mathcal{R}$$ to the fixed point $$f$$ yields the genuine distribution $$\mathcal{R}f$$—giving the singular SPDE a rigorous, intrinsic solution!

Summary of Hairer’s machine:

$$
\text{Singular SPDE}
\;\xrightarrow{\text{noise trees}}\;
\text{Algebra } (\mathcal{A}, T, G)
\;\xrightarrow{\text{renormalize}}\;
\text{Model } (\hat{\Pi}, \hat{\Gamma})
\;\xrightarrow{\text{Picard + } \mathcal{R}}\;
\text{True solution } \mathcal{R}f.
$$

---

## 3. Paracontrolled Distributions, Rough Paths, and Scope of the Medal

- **Rough paths (Terry Lyons):** Showed that ODEs driven by rough signals can be solved pathwise once enhanced with iterated integrals; regularity structures extend that philosophy to PDEs.
- **Paracontrolled distributions (Massimiliano Gubinelli, Peter Imkeller, and Nicolas Perkowski,** *Forum Math. Pi*, 2015; arXiv:1210.2684): An **independent parallel toolkit** built on Fourier analysis and Bony paraproducts that also solves KPZ and $$\Phi^4_3$$—not Hairer’s invention and not a corollary of regularity structures.

**What the 2014 medal does not claim:** It covers **subcritical parabolic** singular SPDEs (critical models like $$\Phi^4_4$$, supercritical models, and many hyperbolic/fluid equations lie outside); Hairer–Mattingly (2006) is 2D *stochastic* Navier–Stokes, not the Clay 3D deterministic problem; and the physics PhD (plus the later 2021 Breakthrough Prize) is biographical context, not the citation itself.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “All SPDEs are now well-posed.” | A large class of *subcritical parabolic* singular SPDEs; not a universal existence theory. |
| “Hairer solved Navier–Stokes.” | He did not solve the Clay 3D deterministic problem. Stochastic 2D ergodicity is a different theorem. |
| “Paracontrolled distributions are part of regularity structures.” | Gubinelli–Imkeller–Perkowski built an independent, related toolkit. |
| “White noise is a function, so just multiply.” | White noise is a distribution; products need a theory. |
| “Reconstruction is the same as Taylor’s theorem.” | It *extends* Taylor: the jet includes noise symbols, and the output is a distribution. |
| “The Fields is for a physics doctorate.” | Biography; the citation is SPDE theory and regularity structures. |

---

## Links

- IMU Fields Medals 2014: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014)
- IMU brief citation (Hairer): [https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014/fields-medallists-2014-awardees-brief-citations](https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014/fields-medallists-2014-awardees-brief-citations)
- IMU note, “The Work of Martin Hairer” (PDF): [https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_hairer.pdf](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_hairer.pdf)
- Wikipedia — Martin Hairer: [https://en.wikipedia.org/wiki/Martin_Hairer](https://en.wikipedia.org/wiki/Martin_Hairer)
- Wikipedia — Regularity structure: [https://en.wikipedia.org/wiki/Regularity_structure](https://en.wikipedia.org/wiki/Regularity_structure)
- Quanta profile (2014): [https://www.quantamagazine.org/in-noisy-equations-one-who-heard-music-20140812/](https://www.quantamagazine.org/in-noisy-equations-one-who-heard-music-20140812/)
- Hairer, regularity structures (arXiv:1303.5113): [https://arxiv.org/abs/1303.5113](https://arxiv.org/abs/1303.5113)
- Gubinelli–Imkeller–Perkowski (arXiv:1210.2684): [https://arxiv.org/abs/1210.2684](https://arxiv.org/abs/1210.2684)
- arXiv search — Hairer KPZ: [https://arxiv.org/search/?query=Hairer+KPZ&searchtype=all](https://arxiv.org/search/?query=Hairer+KPZ&searchtype=all)

---

## References

1. IMU Fields Medal 2014 citation — Martin Hairer.
2. M. Hairer, “Solving the KPZ equation,” *Ann. of Math.* 178 (2013).
3. M. Hairer, “A theory of regularity structures,” *Invent. Math.* 198 (2014).
4. M. Gubinelli, P. Imkeller, and N. Perkowski, “Paracontrolled distributions and singular PDEs,” *Forum Math. Pi* 3 (2015).
5. T. Lyons, rough path theory (predecessor for pathwise SDEs).
6. M. Hairer and J. Mattingly, “Ergodicity of the 2D Navier–Stokes equations with degenerate stochastic forcing,” *Ann. of Math.* 164 (2006) — stochastic 2D, not Clay 3D.
7. Course: [Mathematical Physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/), [Deng PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/).

---

## Further directions

- Compare the Cole–Hopf transformation for KPZ with the regularity-structure construction: one exploits a special change of unknown; the other scales to equations with no such trick.
- Seminar question: in what sense is renormalization here the same as, and different from, renormalization in constructive quantum field theory?

## Video tham khảo

- **xem trước** — [Martin Hairer Colloquium Talk: Taming Infinities](https://www.youtube.com/watch?v=nBbx0wEgUXY) — Sydney Mathematical Research Institute - SMRI, English. Watch first. “Martin Hairer Colloquium Talk: Taming Infinities” orients the lesson’s aim: Explain, in one paragraph, why a product of distributions is not in general defined, and why that obstruction appears in nonlinear SPDEs with space-time white noise.
- [Martin Hairer Mini-course 1: Introduction to Regularity Structures](https://www.youtube.com/watch?v=c0HlcVA1SoI) — Sydney Mathematical Research Institute - SMRI, English. A second pass once the main claim is in view: Explain, in one paragraph, why a product of distributions is not in general defined, and why that obstruction appears in nonlinear SPDEs with space-time white noise.
- [Martin Hairer: Fine properties of random fields: from fluids to QTF](https://www.youtube.com/watch?v=VnmfSICGDo4) — Centre International de Rencontres Mathématiques, English. Further depth after the first two, still tied to this lesson: Explain, in one paragraph, why a product of distributions is not in general defined, and why that obstruction appears in nonlinear SPDEs with space-time white noise.
