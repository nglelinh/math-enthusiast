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

**Martin Hairer** received the **Fields Medal 2014**

> “for his outstanding contributions to the theory of stochastic partial differential equations, and in particular for the creation of a theory of regularity structures for such equations.”
> — [IMU, Fields Medals 2014](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014)

The citation names a **language**, not a claim that every stochastic PDE is now well-posed. Classical Itô calculus tamed ordinary stochastic differential equations in the 1940s. Singular **stochastic partial differential equations (SPDEs)**—equations whose solutions are so rough that the nonlinear terms are products of distributions—sat outside that calculus. Hairer’s **regularity structures** supply a Taylor-like expansion for those solutions, a reconstruction theorem that turns an abstract jet into a genuine distribution, and a renormalization-and-fixed-point scheme that gives a rigorous meaning to equations that physicists had written for decades.

This essay aims at seminar fluency: why the product fails, what KPZ and dynamical $$\Phi^4_3$$ look like as test cases, what a regularity structure is trying to be, and how **paracontrolled distributions** (Gubinelli–Imkeller–Perkowski) sit beside Hairer’s theory as a related independent toolkit. It does **not** claim that the Clay Navier–Stokes problem is solved, and it does **not** treat Hairer’s earlier physics doctorate as the medal.

---

## Learning objectives

After this lecture you should be able to:

- Explain, in one paragraph, why a product of distributions is not in general defined, and why that obstruction appears in nonlinear SPDEs with space-time white noise.
- Name two singular equations (KPZ; dynamical $$\Phi^4_3$$) and say what “singular” means for each.
- Describe regularity structures as a **graded expansion language**—Taylor polynomials upgraded to include noise-built monomials.
- State the slogan of the **reconstruction theorem**: an abstract modelled distribution determines a unique actual distribution that looks like the model near every point.
- Credit **Lyons’s rough paths** as a predecessor and **paracontrolled distributions** as a parallel approach, not as Hairer’s invention.
- Practice accuracy: the 2014 medal is for SPDE theory / regularity structures; a physics PhD is biographical background; 3D deterministic Navier–Stokes remains open.

**Prerequisites.** The heat equation and the idea of a PDE; Brownian motion as a continuous but nowhere differentiable path; distributions as continuous linear functionals on test functions. Stochastic integrals at the level of “white noise is the derivative of Brownian motion” are enough. No prior rough-path course is assumed.

**Seminar links.** Place the story on the [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/) map (which already flags Hairer’s SPDEs as a well-posedness problem). Contrast with [Deng PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) (deterministic kinetic limits) and with [Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/) (regularity of nonlinear PDE *without* space-time white noise).

---

## 1. When the product does not exist

A Schwartz distribution $$u\in\mathcal{S}'(\mathbb{R}^d)$$ can be differentiated any number of times, but it cannot always be multiplied by another distribution. Pointwise products require enough regularity: if $$u$$ is a measure and $$v$$ is a continuous function the product is fine; if both are as rough as the derivative of Brownian motion, there is in general **no canonical product**.

Space-time white noise $$\xi$$ is, informally, a Gaussian distribution whose covariance is a delta function. It is far rougher than a function. Linear SPDEs such as the stochastic heat equation

$$
\partial_t u=\Delta u+\xi
$$

still make sense: one convolves $$\xi$$ with the heat kernel and obtains a Hölder distribution (in one space dimension, roughly Hölder-$$1/2-$$ in space). The trouble starts when the equation is **nonlinear** in that solution. Two canonical examples:

**Kardar–Parisi–Zhang (KPZ).** A model for a growing interface,

$$
\partial_t h=\partial_x^2 h+(\partial_x h)^2+\xi.
$$

The solution $$h$$ is expected to be as rough as the stochastic heat equation, so $$\partial_x h$$ is a distribution, and $$(\partial_x h)^2$$ is the illegal product.

**Dynamical $$\Phi^4_3$$.** A stochastic quantization of the $$\Phi^4$$ field in three space dimensions,

$$
\partial_t\Phi=\Delta\Phi-\Phi^3+\xi.
$$

Here $$\Phi$$ itself is distribution-valued, and the cube $$\Phi^3$$ is again undefined as a pointwise product.

“Singular” in this literature does not mean “we have not tried hard enough.” It means the naive equation is **not a well-defined PDE** until one specifies a limiting procedure (smooth the noise, subtract divergences, pass to the limit) and proves the limit exists.

---

## 2. Hairer’s route: from KPZ to a general language

Hairer was born in Geneva in 1975, studied mathematics and physics at the University of Geneva, and wrote a **physics** PhD (2001) under Jean-Pierre Eckmann. That background explains his ease with formal field-theoretic calculations. The Fields Medal is for the **mathematical** SPDE theory.

Two earlier strands matter. With **Jonathan Mattingly**, he proved ergodicity for **two-dimensional stochastic Navier–Stokes** with degenerate noise (Annals, 2006)—a stochastic fluid theorem, not the Clay problem for deterministic 3D Navier–Stokes. Separately, **Terry Lyons’s rough paths** had shown that ordinary SDEs driven by irregular signals can be solved if one enhances the signal by iterated integrals. IMU’s 2014 note says Hairer built on that idea.

In *Solving the KPZ equation* (Annals of Mathematics, 2013), Hairer gave a pathwise meaning to KPZ by a regularity structure adapted to that equation (after related Cole–Hopf and uniqueness work in the probability community). The general machine appeared as *A theory of regularity structures* (Inventiones Mathematicae, 2014; arXiv:1303.5113): a framework that treats KPZ, $$\Phi^4_3$$, the parabolic Anderson model, and a large class of **subcritical parabolic** singular SPDEs by the same algebra-plus-analysis pattern.

**Subcritical** is a scaling slogan: after a power-counting of the noise and the nonlinearity, the equation becomes less singular at small scales than a critical model would. Regularity structures are not a license to write an arbitrary SPDE and declare it solved.

---

## 3. Regularity structures: Taylor polynomials with noise monomials

A classical $$C^\gamma$$ function $$f$$ on $$\mathbb{R}^d$$ is one that looks, near every point $$x$$, like a Taylor polynomial of degree $$\lfloor\gamma\rfloor$$, with a Hölder remainder. Hairer’s idea is to keep the “looks like an expansion near $$x$$” but to enlarge the list of allowed monomials.

A **regularity structure** is a triple $$(\mathcal{A},T,G)$$: an index set $$\mathcal{A}\subset\mathbb{R}$$ of homogeneities, a graded vector space $$T=\bigoplus_{\alpha\in\mathcal{A}}T_\alpha$$ whose basis elements behave like abstract monomials (ordinary polynomials *and* symbols built from the noise), and a structure group $$G$$ that recenters expansions from one base point to another, the way Taylor polynomials transform under $$x\mapsto y$$.

A **model** $$(\Pi,\Gamma)$$ realizes those symbols as actual distributions: $$\Pi_x\tau$$ is “the concrete jet of the symbol $$\tau$$ based at $$x$$,” and $$\Gamma_{xy}$$ converts an expansion based at $$y$$ into one based at $$x$$. Analytic bounds say that $$\Pi_x\tau$$ scales like $$\lambda^{|\tau|}$$ when tested on a bump of width $$\lambda$$.

A **modelled distribution** is then a map $$x\mapsto f(x)\in T$$ that is Hölder with respect to $$\Gamma$$—an abstract Taylor jet whose coefficients vary in a controlled way. The whole theory is local and algebraic until one reconstructs.

**Slogan.** Ordinary Taylor theory expands in $$1,\,(y-x),\,(y-x)^2,\ldots$$. A regularity structure expands in those *and* in a finite list of “polynomials made from the regularized noise,” chosen so that the PDE’s nonlinearity can be multiplied in the abstract space even when it cannot be multiplied in $$\mathcal{S}'$$.

---

## 4. Reconstruction, renormalization, fixed point

**Reconstruction theorem.** Given a model and a modelled distribution $$f$$ of positive regularity, there exists a unique distribution $$\mathcal{R}f$$ such that, near each $$x$$, $$\mathcal{R}f$$ looks like $$\Pi_x f(x)$$ up to the expected Hölder error. Reconstruction is the bridge from algebra back to analysis: it is the reason the abstract jet is not mere bookkeeping.

**Renormalization.** If one smooths the noise as $$\xi^\varepsilon$$ and builds the corresponding model, many products diverge as $$\varepsilon\to 0$$. One subtracts (or, more invariantly, recenters) a finite list of constants or local counterterms—the same instinct as renormalization in quantum field theory, now as a theorem that the renormalized models converge. The reconstructed solutions then converge to a limit that one *defines* to be the solution of the singular SPDE.

**Fixed point.** In the space of modelled distributions, the PDE becomes a contraction mapping for short time (or globally in dissipative cases), exactly as Picard iteration works for ODEs in Banach spaces. Existence and uniqueness are not metaphysical; they are fixed-point theorems in a space designed so that the illegal product is legal.

Hairer’s theory therefore does three jobs at once: it **defines** the equation, it **constructs** solutions, and it **identifies** the limit of natural regularizations. That is why the IMU text says he gave, for the first time, a rigorous intrinsic meaning to many SPDEs arising in physics.

---

## 5. Paracontrolled distributions: a related independent toolkit

Around the same years, **Massimiliano Gubinelli**, **Peter Imkeller**, and **Nicolas Perkowski** developed **paracontrolled distributions** (Forum of Mathematics, *Pi*, 2015; preprint arXiv:1210.2684). The idea is Fourier-analytic rather than jet-theoretic: one uses Bony paraproducts to say that a solution $$u$$ is “controlled” by the linear stochastic objects built from the noise, and one multiplies in the paraproduct calculus.

This is **not** Hairer’s invention, and it is not a corollary of regularity structures. It is a parallel toolkit that treats overlapping families of singular SPDEs (including KPZ and $$\Phi^4_3$$). Later work has compared, translated, and sometimes combined the two languages; seminar honesty requires naming both.

A third neighbor, for orientation only, is the theory of **rough paths** (Lyons) and its branched-rough-path extensions: regularity structures can be read as a PDE-scale enrichment of that philosophy.

---

## 6. What the medal is not

Accuracy constraints for this course:

- **Not all SPDEs.** The theory targets a class of subcritical parabolic equations. Critical and supercritical models, hyperbolic problems, and many fluid equations remain outside, or only partly inside, the machine.
- **Not Clay Navier–Stokes.** Hairer–Mattingly ergodicity is for *stochastic* 2D Navier–Stokes. The deterministic 3D regularity problem is untouched by regularity structures as a solution, and the IMU citation does not claim otherwise.
- **Not “physics PhD therefore Fields.”** The doctorate explains taste and technique; the prize is the SPDE theory.
- **Not a uniqueness of method.** Paracontrolled calculus, energy methods, and Cole–Hopf transformations solve some of the same equations by other routes.

Later chairs (Warwick, Imperial, EPFL) and the 2021 Breakthrough Prize do not change the 2014 sentence.

---

## 7. Why it matters on a modern map

Singular SPDEs sit where probability, PDE, and quantum field theory share a wall: easy to write, hard to interpret. Regularity structures changed the default from “formal” to “renormalized fixed point” for a large, explicitly described class.

For this chapter, Hairer is an **infrastructure** portrait: a new category of expansions that makes old formal objects legal. Some Fields medals reward a language.

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

## Exercises

1. Why is $$(\partial_x h)^2$$ undefined if $$h$$ is only as regular as the one-dimensional stochastic heat equation? Answer in the language of products of distributions.
2. Write the dynamical $$\Phi^4_3$$ equation and mark the illegal term. What does “3” in the subscript refer to?
3. In one paragraph, what extra data does a **model** add to the abstract regularity structure $$(A,T,G)$$?
4. State the reconstruction slogan without using the word “magic.” Why is uniqueness of $$\mathcal{R}f$$ important for defining a PDE?
5. What is **renormalization** doing in this story—cancelling a physical force, or specifying a limit of regularized equations?
6. Name one thing regularity structures and paracontrolled distributions **share**, and one way they **differ** (jets vs paraproducts is enough).
7. **Accuracy practice.** Rewrite “Hairer solved all noisy equations, including turbulence” as two sentences that could appear in this course.
8. **Seminar stretch.** Skim the first pages of Hairer, arXiv:1303.5113, and list five words to learn next (e.g. modelled distribution, structure group, subcritical, Hopf algebra of trees, renormalization group).

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
