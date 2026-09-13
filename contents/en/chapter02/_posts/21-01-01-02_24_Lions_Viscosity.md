---
layout: post
title: "Lions’s Viscosity Solutions and Nonlinear PDE (Fields Medal 1994)"
chapter: '02'
order: 24
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Pierre-Louis Lions** received the **Fields Medal 1994** at ICM Zürich. The standard ICM account, in S. R. S. Varadhan’s lecture on the work, does not isolate a single named conjecture. It records a *portfolio*: contributions spanning **probability** and **partial differential equations**, with especially beautiful work on **nonlinear equations**, and with problem choices consistently **motivated by applications**. The mathematical slogan this course teaches from that portfolio is **viscosity solutions** for nonlinear elliptic and parabolic PDE—introduced for Hamilton–Jacobi equations by **Crandall–Lions**, developed with **Evans** and others, and organized for second-order equations in the **Crandall–Ishii–Lions** user’s guide.

This essay is for learners who have met first-order PDE and the classical maximum principle and want to understand why a *weak* notion of solution, defined by touching with test functions rather than by pointwise second derivatives, became a language of modern nonlinear analysis. It does **not** claim that Lions solved the Clay Millennium problem on three-dimensional incompressible Navier–Stokes regularity. Mean field games (Lasry–Lions) appear only as **later** influence.

---

## Learning objectives

After this lecture you should be able to:

- Restate the 1994 ICM account as a **portfolio** (probability, nonlinear PDE, applications) rather than as a single theorem.
- Explain why classical $$C^2$$ solutions of Hamilton–Jacobi and fully nonlinear equations can fail, and what a **viscosity solution** is designed to allow.
- Describe the **comparison / maximum-principle** engine: if a viscosity subsolution lies below a supersolution on the boundary, it remains below inside.
- Credit **Crandall**, **Ishii**, **Evans**, and **Souganidis** at the right scale, and name the **Crandall–Ishii–Lions** user’s guide as the standard second-order reference.
- Place **DiPerna–Lions** theory (Boltzmann / transport) and **concentration-compactness** as other pillars of the same nonlinear-PDE portfolio.
- Keep **mean field games** (Lasry–Lions, mid-2000s) off the 1994 citation, and refuse the slogan “Lions solved Navier–Stokes.”

**Prerequisites.** Multivariable calculus; the idea of a first-order PDE such as a Hamilton–Jacobi equation $$u_t + H(x,\nabla u)=0$$; the classical maximum principle for harmonic or uniformly elliptic linear equations. Optimal control and kinetic theory are helpful as motivation, not required as formal courses.

**Seminar links.** LO1 (hard programs that reorganize a field’s language) and LO6 (citation hygiene). Analysis neighbors: [Yu Deng / kinetic PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) (Boltzmann as a later kinetic chapter), [Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/) (fully nonlinear regularity that *uses* viscosity solutions), and [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/) (to keep the Millennium problem distinct).

---

## 1. Why a weak theory was needed

A Hamilton–Jacobi equation of evolutionary type looks innocent,

$$
u_t + H\bigl(x,\nabla u\bigr) = 0,
$$

and in optimal control or geometric optics the unknown $$u$$ is a value function or an eikonal phase. The method of characteristics produces smooth solutions for a short time. Then characteristics cross: gradients jump, and no $$C^1$$ (let alone $$C^2$$) solution can continue. Fully nonlinear second-order equations

$$
F\bigl(x,u,\nabla u,D^2 u\bigr) = 0
$$

are worse. The unknown enters through the Hessian in a nonlinear way (examples include Hamilton–Jacobi–Bellman equations from stochastic control, and some curvature equations). Classical elliptic regularity does not apply off the shelf, and one cannot simply “integrate by parts” as in the linear divergence-form theory that produces Sobolev weak solutions.

The design problem is therefore conceptual: invent a class of **weak solutions** large enough to exist globally, small enough to be unique, and compatible with the **maximum principle** that elliptic and parabolic theory lives on. Distributional solutions are the wrong first language when $$F$$ is not linear in $$D^2 u$$. Viscosity solutions answer that design problem.

---

## 2. Viscosity solutions: touching instead of differentiating

The Crandall–Lions idea (announced and then developed in the early 1980s; the foundational Hamilton–Jacobi paper is **Crandall–Lions, Trans. Amer. Math. Soc. 1983**) is to test a merely continuous function $$u$$ by smooth functions that touch its graph from above or below. Slogan form for a stationary equation $$F(x,u,\nabla u,D^2 u)=0$$: $$u$$ is a viscosity **subsolution** if, whenever a smooth test function $$\varphi$$ touches $$u$$ from above at $$x_0$$, one has

$$
F\bigl(x_0,u(x_0),\nabla\varphi(x_0),D^2\varphi(x_0)\bigr) \le 0
$$

(with the inequality direction depending on the convention for $$F$$; the user’s guide fixes conventions carefully). A **supersolution** is the opposite touching condition. A **viscosity solution** is both.

Nothing in the definition requires $$u$$ itself to be differentiable. The derivatives that enter $$F$$ are borrowed from the test function at a contact point. If $$u$$ happens to be $$C^2$$, the definition collapses to the classical pointwise equation: that is the consistency check.

**Why “viscosity”?** One historical route approximates a first-order equation by adding a small second-order term $$\varepsilon\Delta u$$ (artificial viscosity) and passing to the limit $$\varepsilon\to 0$$. The inequalities that survive are exactly the touching conditions. The name remembers that vanishing-viscosity limit; the modern definition does not require constructing the approximation every time.

**Evans** (with Crandall and Lions) clarified equivalent formulations and basic properties. **Ishii** was central in extending the theory to fully nonlinear second-order equations. **Souganidis** (often with Lions and others) developed stability, approximation, and front-propagation aspects that made the theory usable in geometric and applied settings. Credit is communal; the 1983 definition and the 1992 guide are the two landmarks a seminar should name.

---

## 3. Comparison is the engine

Existence without uniqueness is cheap; uniqueness without existence is a slogan. Viscosity theory earns both through **comparison**. In a typical Dirichlet setting: if $$u$$ is a viscosity subsolution and $$v$$ a viscosity supersolution of a uniformly elliptic (or degenerate elliptic, under structural hypotheses) equation, and if $$u\le v$$ on the boundary, then $$u\le v$$ in the domain. Two viscosity solutions with the same boundary data therefore coincide.

The engine is a maximum-principle argument upgraded to non-differentiable functions. One considers a maximum of $$u(x)-v(y)$$ after a penalization that forces $$x$$ and $$y$$ together, applies the touching definition at nearly coincident points, and uses ellipticity of $$F$$ to obtain a contradiction unless the maximum is nonpositive. The **Crandall–Ishii–Lions user’s guide** (*Bull. Amer. Math. Soc.* 1992; also [arXiv:math/9207212](https://arxiv.org/abs/math/9207212)) is the standard exposition of this second-order calculus: jets, the theorem on sums, comparison, and stability under uniform limits.

**Stability** is the other gift. Uniform limits of viscosity solutions are viscosity solutions. That is why vanishing-viscosity approximations, numerical schemes, and control-theoretic value functions can be identified with the unique viscosity solution once a comparison principle is in hand.

**Slogan.** A viscosity solution is a weak solution whose law is the maximum principle, not an integration-by-parts identity.

---

## 4. Other pillars: DiPerna–Lions and concentration-compactness

The 1994 account is broader than Hamilton–Jacobi.

**DiPerna–Lions theory.** With **Ronald J. DiPerna**, Lions developed **renormalized solutions** for the Boltzmann equation: global existence and weak stability for large-data Cauchy problems (*Ann. of Math.* **1989**). The collision operator is hard to define on merely integrable densities; renormalization and velocity-averaging compactness restore a meaningful equation. The same circle produced **transport equations** with Sobolev vector fields: characteristics need not be Lipschitz-unique, yet a well-posed continuity equation survives (later extended by Ambrosio and others). Pair with [Deng’s kinetic chapter]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/): DiPerna–Lions is well-posedness of the kinetic equation; Deng–Hani–Ma is a particle derivation. Different rungs of Hilbert’s sixth problem.

**Concentration-compactness.** Minimizing sequences on $$\mathbb{R}^n$$ may escape by translation or dilation. Lions’s **concentration-compactness principle** (locally compact case **1984**; dilation/limit case **1985**) classifies those failures and restores compactness when a strict energy inequality prevents dichotomy. Moral: if a variational problem is invariant under a noncompact group, measure *how* compactness fails. Applications include Sobolev extremals and some Yamabe-type geometric problems.

The family resemblance with viscosity solutions is architectural: invent the right weak object, then prove a rigidity that makes it unique or attainable.

---

## 5. What the 1994 medal is not

**Not Navier–Stokes regularity.** Lions contributed existence theory for **compressible** Navier–Stokes systems in certain settings (part of the same DiPerna–Lions kinetic/fluid portfolio). That is not a solution of the Clay problem on global regularity of **three-dimensional incompressible** Navier–Stokes. Keep the [Millennium statement]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/) separate.

**Not mean field games as citation.** With **Jean-Michel Lasry**, Lions later introduced **mean field games** (notes and *Comptes Rendus* papers in **2006**): continuum limits of Nash equilibria for many rational agents, typically a coupled Hamilton–Jacobi–Bellman / Fokker–Planck system. The theory uses viscosity solutions and is a major subsequent influence on analysis, economics, and crowd models. It is **later than 1994**. Do not write it into the Fields citation.

**Not a solo invention.** Viscosity solutions are Crandall–Lions at birth, Evans–Ishii–Souganidis in the widening, and a community thereafter. The medal recognizes Lions’s role inside that network and inside a broader nonlinear-PDE portfolio.

---

## 6. Why a Fields Medal

Three interlocking reasons, matching Varadhan’s ICM emphasis.

1. **A new language.** Viscosity solutions turned equations without classical solutions into well-posed problems. Entire fields—optimal control, front propagation, some fully nonlinear geometry—could state uniqueness theorems that had been formally out of reach.
2. **Several deep machines, not one lemma.** Concentration-compactness and DiPerna–Lions theory are independent architectures; together they show a style: diagnose the failure of classical compactness or differentiability, then build a calculus around the failure.
3. **Applications as a source of theorems.** The ICM text insists that problem choice was motivated by applications. That is not a consolation prize. It is a research method: the Boltzmann collision operator, the value function of a control problem, and a Sobolev extremal on $$\mathbb{R}^n$$ each forced a new notion of solution or compactness.

A later chapter—mean field games, Collège de France lectures—continues the method. The 1994 medal already had enough.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Viscosity solutions are classical $$C^2$$ solutions with extra viscosity.” | They are *weak* solutions defined by test-function inequalities; a $$C^2$$ solution is a special case. |
| “Viscosity” means the physical viscosity of a fluid. | The name remembers vanishing-viscosity *approximations*; the definition does not require a fluid. |
| “Lions solved Navier–Stokes.” | No. Compressible existence results are not the Clay incompressible regularity problem. |
| “Mean field games earned the 1994 medal.” | Lasry–Lions mean field games are mid-2000s; subsequent influence only. |
| “Distributional solutions already suffice for fully nonlinear equations.” | When $$F$$ is nonlinear in $$D^2 u$$, integration by parts is the wrong engine; comparison is the right one. |
| “Lions invented viscosity solutions alone.” | Crandall–Lions; then Evans, Ishii, Souganidis, and many others. |
| “DiPerna–Lions derives Boltzmann from particles.” | It gives a well-posed kinetic theory; particle derivations are a different (later) story. |

---

## Exercises

1. In your own words: why can characteristics of $$u_t+H(\nabla u)=0$$ produce a gradient jump in finite time? Why does that force a weak theory?
2. Write the touching definition of a viscosity subsolution for $$u_t+H(\nabla u)=0$$, then check consistency: if $$u$$ is $$C^1$$, the definition reduces to the classical inequality.
3. Why is **comparison** more valuable than a formal existence construction? Answer in at most six sentences.
4. Skim the first pages of Crandall–Ishii–Lions (BAMS 1992 or arXiv:math/9207212). List three words of jargon (jet, test function, degenerate ellipticity) and give a one-line gloss for each.
5. Distinguish, in a table of your own, **viscosity solutions**, **DiPerna–Lions renormalized solutions**, and **concentration-compactness**. Which failure of classical theory does each address?
6. **Accuracy practice.** Find a sentence that says the 1994 medal was “for mean field games.” Rewrite it in two precise sentences.
7. **Seminar stretch.** Compare viscosity comparison with the maximum principle for harmonic functions: what is inherited, and what must be rebuilt for non-differentiable $$u$$?

---

## Links

- IMU Fields Medal page: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- IMU Fields Medals 1994: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994)
- Wikipedia, Pierre-Louis Lions: [https://en.wikipedia.org/wiki/Pierre-Louis_Lions](https://en.wikipedia.org/wiki/Pierre-Louis_Lions)
- Wikipedia, viscosity solution: [https://en.wikipedia.org/wiki/Viscosity_solution](https://en.wikipedia.org/wiki/Viscosity_solution)
- Crandall–Ishii–Lions user’s guide on arXiv: [https://arxiv.org/abs/math/9207212](https://arxiv.org/abs/math/9207212)
- Collège de France chair biography: [https://www.college-de-france.fr/en/chair/pierre-louis-lions-partial-differential-equations-and-applications-statutory-chair/biography](https://www.college-de-france.fr/en/chair/pierre-louis-lions-partial-differential-equations-and-applications-statutory-chair/biography)
- arXiv search, Lions viscosity: [https://arxiv.org/search/?query=Lions+viscosity+solutions&searchtype=all](https://arxiv.org/search/?query=Lions+viscosity+solutions&searchtype=all)

---

## References

1. S. R. S. Varadhan, lecture on the work of P.-L. Lions, *Proceedings of the ICM*, Zürich, 1994 (standard ICM account quoted on the IMU 1994 page).
2. **M. G. Crandall and P.-L. Lions**, “Viscosity solutions of Hamilton–Jacobi equations,” *Trans. Amer. Math. Soc.* **277** (1983).
3. **M. G. Crandall, L. C. Evans, and P.-L. Lions**, “Some properties of viscosity solutions of Hamilton–Jacobi equations,” *Trans. Amer. Math. Soc.* **282** (1984).
4. **M. G. Crandall, H. Ishii, and P.-L. Lions**, “User’s guide to viscosity solutions of second order partial differential equations,” *Bull. Amer. Math. Soc.* **27** (1992); [arXiv:math/9207212](https://arxiv.org/abs/math/9207212).
5. **R. J. DiPerna and P.-L. Lions**, “On the Cauchy problem for Boltzmann equations: global existence and weak stability,” *Ann. of Math.* **130** (1989).
6. **P.-L. Lions**, concentration-compactness papers, *Ann. Inst. H. Poincaré Anal. Non Linéaire* (1984) and *Rev. Mat. Iberoamericana* (1985).
7. **J.-M. Lasry and P.-L. Lions**, mean field games notes / *C. R. Math.* (2006)—subsequent influence, not the 1994 citation.
8. Course context: [Deng / kinetic equations]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/), [Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/), [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/).

---

## Further directions

- Read the user’s guide as a seminar text: comparison first, examples second.
- Compare vanishing-viscosity limits with entropy solutions of scalar conservation laws (a cousin weak theory, not the same definition).
- If you continue toward applications, treat mean field games as a *consumer* of viscosity solutions, dated after the medal.
- Seminar A3 option: a one-page “what viscosity solutions are not” brief (not NS, not MFG-as-citation, not a fluid viscosity).
