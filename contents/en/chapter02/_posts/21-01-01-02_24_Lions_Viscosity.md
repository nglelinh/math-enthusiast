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

Try solving a first-order differential equation that looks like a freshman calculus warmup: $$\vert u'(x) \vert = 1$$ on $$[-1, 1]$$ with boundary values $$u(-1) = u(1) = 0$$. Everyone immediately sketches the triangular tent $$u_1(x) = 1 - \vert x \vert$$—yet that tent has a **sharp peak at $$x = 0$$ and is not differentiable there**! Worse still, once you allow corners (satisfying the equation almost everywhere), you can also draw the upside-down tent $$u_2(x) = \vert x \vert - 1$$, or **infinitely many sawtooth zigzags** with slope $$\pm 1$$ almost everywhere and $$0$$ at both endpoints! Which mathematical law picks out the *one* physically right solution?

That innocent puzzle sparked a revolution in late-twentieth-century nonlinear analysis. At ICM Zürich in 1994, **Pierre-Louis Lions** received the **Fields Medal**—not for one isolated conjecture, as S. R. S. Varadhan’s ICM lecture made clear, but for an extraordinary **portfolio** spanning probability and nonlinear PDE, consistently driven by real-world applications. Its flagship language is **viscosity solutions**—pioneered by **Crandall and Lions** (1983), widened by **Evans**, **Ishii**, and **Souganidis**, and codified for second-order fully nonlinear equations in the classic **Crandall–Ishii–Lions** *User’s Guide* (1992). Beside it stand two other towering pillars: **DiPerna–Lions** theory (Boltzmann and transport equations) and the **concentration-compactness principle**. We also keep two boundaries sharp: Lions did **not** solve the Clay 3D incompressible Navier–Stokes problem, and **mean field games** (Lasry–Lions, 2006) are a major *later* development, not part of the 1994 citation.

**Lesson roadmap:** Background Knowledge Map (fully nonlinear PDEs vs. distributional solutions) → Hand-verifiable worked example: testing the eikonal tent $$\vert u'(x)\vert - 1 = 0$$ with touching test functions and the vanishing-viscosity limit $$-\varepsilon u''$$ → Deep-Dive Explanation (Read Slowly): 4 steps from test-function touching to the comparison principle and stability → Other pillars (DiPerna–Lions & concentration-compactness) → What the 1994 medal is not.

---

## Learning objectives

After this lecture you should be able to:

- Present the 1994 ICM account as a **portfolio** (probability, nonlinear PDE, applications) rather than a single theorem.
- Apply the viscosity touching test by hand to $$\vert u'(x) \vert - 1 = 0$$ on $$[-1, 1]$$ to eliminate the upside-down tent and select the unique viscosity solution $$u_1(x) = 1 - \vert x \vert$$.
- Explain why Hamilton–Jacobi and fully nonlinear PDEs break integration by parts, requiring a weak theory built on the **maximum principle**.
- Describe the **comparison principle** (via doubling of variables and Ishii’s lemma) and credit **Crandall**, **Ishii**, **Evans**, and **Souganidis** accurately.
- Place **DiPerna–Lions** (Boltzmann / transport) and **concentration-compactness** alongside viscosity solutions as pillars of the 1994 portfolio.
- Keep **mean field games** (Lasry–Lions, 2006) off the 1994 citation and reject the claim that Lions solved Clay Navier–Stokes.

**Prerequisites.** Multivariable calculus; the idea of a first-order PDE such as a Hamilton–Jacobi equation $$u_t + H(x,\nabla u)=0$$; the classical maximum principle for harmonic or uniformly elliptic linear equations. Optimal control and kinetic theory are helpful as motivation, not required as formal courses.

**Seminar links.** Analysis neighbors: [Yu Deng / kinetic PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) (Boltzmann as a later kinetic chapter), [Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/) (fully nonlinear regularity that *uses* viscosity solutions), and [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/) (to keep the Millennium problem distinct).

---

## Background Knowledge Map: What Are Fully Nonlinear PDEs and Maximum-Principle Weak Solutions?

### 1. Why integration by parts fails
For a linear PDE like Laplace’s equation $$-\Delta u = f$$, if $$u$$ is not $$C^2$$ we multiply by a smooth test function $$\varphi$$ and integrate by parts: $$\int \nabla u \cdot \nabla\varphi = \int f\varphi$$. But in **Hamilton–Jacobi equations** $$u_t + H(x, \nabla u) = 0$$ (optimal control, geometric optics) or **fully nonlinear second-order PDEs** $$F(x, u, \nabla u, D^2 u) = 0$$ (Hamilton–Jacobi–Bellman, Monge–Ampère $$\det D^2 u = f$$), the derivatives of $$u$$ sit trapped inside nonlinear functions—**integration by parts is useless!**

### 2. The replacement engine: transferring derivatives via local extrema
Suppose $$u$$ is smooth ($$C^2$$) and a smooth test function $$\varphi$$ touches $$u$$ from **above** at $$x_0$$ (so $$u - \varphi$$ has a local maximum at $$x_0$$). Freshman calculus gives $$\nabla u(x_0) = \nabla\varphi(x_0)$$ and $$D^2 u(x_0) \le D^2\varphi(x_0)$$. When $$F$$ is degenerate elliptic (decreasing in the Hessian matrix $$D^2 u$$), $$F(x_0, u, \nabla u, D^2 u) = 0$$ forces $$F(x_0, u(x_0), \nabla\varphi(x_0), D^2\varphi(x_0)) \le 0$$. The masterstroke: **this inequality uses only derivatives of the smooth test function $$\varphi$$, so it makes perfect sense even when $$u$$ is merely continuous with sharp corners!**

---

## 1. Hand-Verifiable Worked Example: Solving the Eikonal Equation $$\vert u'(x) \vert - 1 = 0$$ on $$[-1, 1]$$

Consider $$F(u') = \vert u'(x) \vert - 1 = 0$$ on $$[-1, 1]$$ with $$u(-1) = u(1) = 0$$. Test our two obvious continuous candidates right at the corner $$x_0 = 0$$:

1. **The upward tent $$u_1(x) = 1 - \vert x \vert$$ at $$x_0 = 0$$:**
   - *Subsolution test* (smooth $$\varphi$$ touching $$u_1$$ from **above** at $$0$$): since $$\varphi$$ sits above a peak with left slope $$+1$$ and right slope $$-1$$, its tangent slope at $$0$$ must satisfy $$-1 \le \varphi'(0) \le 1$$, hence $$\vert\varphi'(0)\vert - 1 \le 0$$. **Passes!**
   - *Supersolution test* (smooth $$\varphi$$ touching $$u_1$$ from **below** at $$0$$): *no* smooth curve can fit underneath a sharp upward peak and touch it at $$0$$! Since the set of such test functions is empty, the condition holds vacuously. **Passes!**
   - Verdict: **$$u_1(x) = 1 - \vert x \vert$$ is a viscosity solution!**

2. **The upside-down tent $$u_2(x) = \vert x \vert - 1$$ at $$x_0 = 0$$:**
   - *Supersolution test* (smooth $$\varphi$$ touching $$u_2$$ from **below** at $$0$$): pick the constant function $$\varphi(x) \equiv -1$$! It touches the V-shaped bottom from below at $$x_0 = 0$$ with $$\varphi'(0) = 0$$. Plug into $$F$$:
     $$
     \vert\varphi'(0)\vert - 1 = 0 - 1 = -1 < 0 \quad (\text{fails the supersolution requirement } \ge 0!).
     $$
   - Verdict: **$$u_2(x) = \vert x \vert - 1$$ is rejected immediately!** (Every sawtooth zigzag with a V-shaped valley fails the exact same test!)

3. **Why the name "viscosity"?** Add a tiny smoothing term $$-\varepsilon u''$$ to get $$-\varepsilon u_\varepsilon''(x) + \vert u_\varepsilon'(x) \vert = 1$$ with $$u_\varepsilon(\pm 1) = 0$$. Its explicit smooth solution rounds off the peak at $$x = 0$$:
   $$
   u_\varepsilon(x) = 1 - \vert x \vert - \varepsilon \ln\left(\frac{1 + e^{-2\vert x \vert/\varepsilon}}{1 + e^{-2/\varepsilon}}\right) \xrightarrow{\varepsilon \to 0^+} 1 - \vert x \vert = u_1(x)!
   $$
   The name "viscosity solution" commemorates that vanishing-viscosity limit $$\varepsilon \to 0^+$$, even though the modern touching definition needs no fluid and no $$\varepsilon$$!

---

## 2. Deep-Dive Explanation: How Viscosity Theory Works for Second-Order PDEs (Read Slowly)

Following the 1983 Hamilton–Jacobi foundation (**Crandall–Lions**) and extensions by **Evans**, **Ishii**, and **Souganidis**, the second-order theory was organized in the famous **Crandall–Ishii–Lions** *User’s Guide* (*Bull. Amer. Math. Soc.* 1992; [arXiv:math/9207212](https://arxiv.org/abs/math/9207212)) in four steps:

#### Step 1: Touching definition (equivalently, second-order jets)
A continuous function $$u$$ is a **viscosity subsolution** if $$F(x_0, u(x_0), \nabla\varphi(x_0), D^2\varphi(x_0)) \le 0$$ whenever a smooth $$\varphi$$ touches $$u$$ from above at $$x_0$$; a **viscosity supersolution** if the reverse inequality $$\ge 0$$ holds for touching from below; and a **viscosity solution** if both hold. Any classical $$C^2$$ solution automatically satisfies this definition.

#### Step 2: The Comparison Principle—the engine of uniqueness
If $$u$$ is a viscosity subsolution and $$v$$ a viscosity supersolution on $$\Omega$$ with $$u \le v$$ on $$\partial\Omega$$, then $$u \le v$$ throughout $$\Omega$$. Immediately, **two viscosity solutions with the same boundary data must be identical!**
Because $$u$$ and $$v$$ need not be differentiable, the proof uses the **doubling-of-variables** trick: maximize $$u(x) - v(y) - \frac{1}{2\varepsilon}\vert x - y \vert^2$$ to pull $$x$$ and $$y$$ arbitrarily close, then apply **Ishii’s lemma (the theorem on sums)** to manufacture approximate Hessians at $$(x_\varepsilon, y_\varepsilon)$$ that contradict ellipticity of $$F$$ unless $$u \le v$$.

#### Step 3: Perron’s method turns comparison into existence
Once a comparison principle holds, Perron’s method (taking the pointwise supremum of all viscosity subsolutions lying beneath a supersolution) automatically builds a global viscosity solution—delivering **existence and uniqueness together**!

#### Step 4: Effortless stability under uniform limits
Unlike classical solutions (which require derivatives to converge), the uniform limit of any sequence of viscosity solutions is **automatically a viscosity solution**! Pairing stability with comparison immediately identifies vanishing-viscosity limits, monotone finite-difference schemes, and optimal-control value functions with the unique viscosity solution.

Summary of the Crandall–Ishii–Lions architecture:

$$
\text{Fully nonlinear PDE}
\;\xrightarrow{\text{touching tests}}\;
\text{Viscosity solution}
\;\xrightarrow{\text{doubling + Ishii}}\;
\text{Comparison + Stability} \implies \text{Existence \& Uniqueness}.
$$

---

## 3. Other Pillars of 1994 and What the Medal Is Not

- **DiPerna–Lions theory (1989):** With **Ronald J. DiPerna**, Lions constructed global **renormalized solutions** for the large-data Boltzmann equation (*Ann. of Math.* 1989) using velocity-averaging compactness, and established well-posedness of **transport equations** with Sobolev $$W^{1,1}$$ vector fields (later extended to BV by Ambrosio). Compare [Deng’s kinetic chapter]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/): DiPerna–Lions studies well-posedness of Boltzmann itself, while Deng–Hani–Ma derive Boltzmann from colliding particles.
- **Concentration-compactness principle (1984–1985):** Classifies exactly how minimizing sequences on non-compact $$\mathbb{R}^n$$ lose compactness—**vanishing**, **dichotomy** (splitting apart), or **compactness** (up to translation/dilation)—turning strict subadditivity energy inequalities into existence of minimizers for Sobolev extremals and Yamabe-type problems.
- **What the 1994 medal is not:** Lions’s existence results for **compressible** Navier–Stokes do **not** solve the Clay [Millennium problem]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/) for 3D **incompressible** Navier–Stokes; **mean field games** (with **Jean-Michel Lasry**) began in **2006**, more than a decade after 1994; and viscosity theory is a communal achievement of Crandall, Lions, Evans, Ishii, and Souganidis.

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

## Video tham khảo

- **xem trước** — [The Essentials of Viscosity Solutions in R^n II](https://www.youtube.com/watch?v=I_fsCAW3xrM) — USF GradMath, English. Watch first for a course introduction to viscosity solutions in R^n, the analytic object of Lions’s medal, before the lectures by Lions himself.
- [Pierre-Louis Lions: Complete" Analysis of the Master Equation: an Example](https://www.youtube.com/watch?v=k0G_fwTVqHA) — Centre de recherches mathématiques - CRM, English. A second pass once the main claim is in view: Restate the 1994 ICM account as a portfolio (probability, nonlinear PDE, applications) rather than as a single theorem.
- [Charlemagne Distingushed Lecture Series 2012 with Prof. Dr. Pierre-Louis Lions](https://www.youtube.com/watch?v=spkaGZPTt9Q) — IRTG 2379 MIP, English. Further depth after the first two, still tied to this lesson: Restate the 1994 ICM account as a portfolio (probability, nonlinear PDE, applications) rather than as a single theorem.
