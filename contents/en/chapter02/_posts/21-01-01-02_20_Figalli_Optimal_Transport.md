---
layout: post
title: "Figalli’s Optimal Transport and Regularity (Fields Medal 2018)"
chapter: '02'
order: 20
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

In 1781, the French military engineer **Gaspard Monge** posed a thoroughly down-to-earth question: how do you shovel a pile of earth into a nearby excavation with the least total effort? Over two centuries later, that earth-moving problem has grown into one of modern mathematics’ great unifying languages—**optimal transport (OT)**—linking crystal shapes, atmospheric weather fronts, curved metric spaces, and machine learning.

Yet between knowing "an optimal transport plan exists" and actually *using* the transport map inside a partial differential equation lies a deep chasm: is the optimal map **smooth**, or does it rip the pile of sand apart along jagged tears? In 2018, **Alessio Figalli** received the **Fields Medal**

> “for contributions to the theory of optimal transport and its applications in partial differential equations, metric geometry and probability.”
> — [IMU, Fields Medals 2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)

Let us state one ground rule upfront: **Figalli did not invent optimal transport.** Monge posed the map problem, Kantorovich relaxed it into a linear program over couplings, Brenier connected quadratic cost to convex potentials, Caffarelli built the first deep regularity theory, and Ambrosio and Villani turned OT into a common language. Figalli’s Fields-level breakthroughs—often jointly with **Guido De Philippis**—sit at the hardest analytic core of that language: proving **Sobolev $$W^{2,1}$$ regularity**, **partial regularity** (controlling the singular set without convexity or MTW assumptions), and **quantitative stability**, turning regularity theory into infrastructure for geometric inequalities, meteorology, and probability. This essay picks up where [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) leaves off, while keeping Figalli’s 2018 medal distinct from his advisor Villani’s 2010 kinetic-theory medal in [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/).

**Lesson roadmap:** Background Knowledge Map (Monge–Kantorovich, Brenier, Monge–Ampère) → Hand-verifiable worked examples (moving 2 sand piles in 1D & tearing a 2D disk into two half-disks) → Deep-Dive Explanation (Read Slowly): from Caffarelli to $$W^{2,1}$$ and De Philippis–Figalli partial regularity → Three major applications (Wulff crystals, semigeostrophic fronts, random matrices) → Separating Figalli 2018 from Villani 2010.

---

## Learning objectives

After this lecture you should be able to:

- Place Figalli’s 2018 citation inside the long history of OT (Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani) without crediting the whole field to one person.
- Solve a discrete 2-pile transport problem by hand and explain the "torn disk" experiment showing why target non-convexity creates singularities.
- State Brenier’s theorem: for quadratic cost, an optimal map is the gradient of a convex potential $$\phi$$ solving the **Monge–Ampère** equation.
- Explain the three pillars of Figalli and De Philippis: $$W^{2,1}$$ Sobolev regularity, partial regularity (smoothness off a closed null set), and quantitative stability.
- Show how map regularity unlocks quantitative anisotropic isoperimetric inequalities (Wulff shapes) and global weak solutions of the semigeostrophic equations.
- Distinguish **Figalli 2018 (OT + applications)** from **Villani 2010 (Landau damping / Boltzmann)**.

**Prerequisites.** The Monge and Kantorovich formulations and the idea of a push-forward $$T_\#\mu=\nu$$, as in the Chapter 6 OT lecture; convex functions and the Hessian; the slogan that a fully nonlinear elliptic equation can have a regularity theory. No prior Monge–Ampère course is assumed.

**Seminar links.** Pair with [Caffarelli / free boundaries and Monge–Ampère]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/) for the Abel-level regularity culture that Figalli inherits, and with [Deng PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) only as a *different* PDE Fields story (kinetic limits, not transport maps).

---

## Background Knowledge Map: What Do Optimal Transport and Monge–Ampère Study?

### 1. Monge (1781) vs. Kantorovich (1942)
Given a source mass distribution $$\mu$$, a target distribution $$\nu$$, and a cost $$c(x,y)$$ to move one unit of mass from $$x$$ to $$y$$:
- **Monge** seeks a single **map** $$T$$ pushing $$\mu$$ onto $$\nu$$ ($$T_\#\mu = \nu$$) minimizing $$\int c(x, T(x))\,d\mu(x)$$. Because mass cannot split, the feasible set is non-convex and existence is hard.
- **Kantorovich** allows mass at $$x$$ to split among multiple destinations via a **coupling** (transport plan) $$\pi(x,y)$$, converting the problem into a linear program on a compact convex set where minimizers always exist.

### 2. Brenier’s theorem and the Monge–Ampère equation
For quadratic cost $$c(x,y) = \|x - y\|^2$$ and smooth densities $$\mu = f\,dx, \nu = g\,dy$$, **Yann Brenier** proved that the unique optimal transport plan is given by a map $$T = \nabla\phi$$ where $$\phi$$ is **convex**. By the change-of-variables formula, mass conservation $$T_\#\mu = \nu$$ yields the **Monge–Ampère equation**:

$$
f(x) = g\bigl(\nabla\phi(x)\bigr)\,\det D^2\phi(x).
$$

This PDE is **fully nonlinear**: the unknown appears inside the *determinant* of its Hessian matrix $$D^2\phi$$ (the product of all second-derivative eigenvalues).

### 3. What does regularity theory ask?
A convex potential $$\phi$$ is differentiable almost everywhere, so $$T = \nabla\phi$$ exists almost everywhere—but it can still jump or crease. Regularity theory asks: *when densities are smooth, is $$T$$ smooth? And when tears are unavoidable, how small is the singular set?*

---

## 1. Hand-Verifiable Worked Examples: Moving 2 Sand Piles and Tearing a Disk

### Example 1 (Discrete 1D): Moving 2 piles of sand—why optimal maps never cross
Suppose two equal 1-ton sand piles sit on the real line at $$x_1 = 0$$ and $$x_2 = 1$$, to be moved to two holes at $$y_1 = 0$$ and $$y_2 = 3$$ with quadratic cost $$c(x,y) = (x - y)^2$$. Compare the two possible maps:
- **Plan 1 (monotone, no crossing):** send $$0 \to 0$$ and $$1 \to 3$$. Total cost:
  $$
  C_1 = (0 - 0)^2 + (1 - 3)^2 = 0 + 4 = 4.
  $$
- **Plan 2 (crossing):** send $$0 \to 3$$ and $$1 \to 0$$. Total cost:
  $$
  C_2 = (0 - 3)^2 + (1 - 0)^2 = 9 + 1 = 10 > 4!
  $$

To minimize squared distance, transport rays **never cross**: $$x_1 < x_2$$ forces $$T(x_1) \le T(x_2)$$. In 1D, a non-decreasing function $$T$$ is literally the **derivative of a convex function** $$\phi$$ ($$T = \phi'$$)! In $$n$$ dimensions, "no crossing" generalizes directly to Brenier’s $$T = \nabla\phi$$ with $$\phi$$ convex.

### Example 2 (Geometric 2D): Tearing a uniform disk into two half-disks
Now picture $$\mathbb{R}^2$$:
- The source $$\mu$$ is a uniform **disk** $$B(0, 1)$$ (smooth density, convex domain).
- The target $$\nu$$ consists of **two disjoint half-disks**: the left half-disk shifted left to center $$(-2, 0)$$, and the right half-disk shifted right to center $$(+2, 0)$$—a **non-convex** target!

To minimize cost, the optimal map $$T = \nabla\phi$$ has no choice: it **rips the source disk cleanly down the vertical diameter $$x_1 = 0$$**, sending $$x_1 < 0$$ to $$x - (2,0)$$ and $$x_1 > 0$$ to $$x + (2,0)$$. The convex potential is $$\phi(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2) + 2\vert x_1 \vert$$, which has a **sharp crease along $$x_1 = 0$$**! Two grains of sand sitting millimeters apart on opposite sides of the diameter are torn 4 units apart!

This single experiment explains the arc from Caffarelli to Figalli:
- **Caffarelli (early 1990s)** proved that if the target is **convex** and densities are smooth and bounded away from $$0$$, no tear ever forms—$$\phi$$ is $$C^\infty$$ in the interior.
- **Figalli and De Philippis** asked what happens when the target is **not convex** (like our two half-disks) or the cost is general: tears (the singular set $$\Sigma$$) must appear, but is $$\Sigma$$ always thin (measure zero), or could it fatten into a positive-area fractal?

---

## 2. Deep-Dive Explanation: From Caffarelli to $$W^{2,1}$$ and Partial Regularity (Read Slowly)

Figalli trained under **Luigi Ambrosio** (Pisa) and **Cédric Villani** (ENS Lyon), completed his PhD in 2007, and joined ETH Zürich in 2016. His OT regularity breakthroughs with **Guido De Philippis** (and Kim, Loeper, and others) unfold in four clear steps:

#### Step 1: The hidden degeneracy of Monge–Ampère
In Laplace’s equation $$\Delta\phi = \lambda_1 + \lambda_2 = 1$$, the Hessian eigenvalues keep each other in check. In Monge–Ampère $$\det D^2\phi = \lambda_1 \lambda_2 = 1$$, one eigenvalue can shrink to $$\varepsilon$$ while the other explodes to $$1/\varepsilon$$! Geometrically, level sets of $$\phi$$ can stretch into needle-thin ellipses, breaking classical Calderón–Zygmund theory.

#### Step 2: The $$W^{2,1}$$ Sobolev threshold (De Philippis–Figalli, *Inventiones*, 2013)
For a convex Alexandrov solution of $$\det D^2\phi = f$$ ($$0 < c \le f \le C$$), a priori $$D^2\phi$$ is only a Radon measure (potentially carrying singular delta-like parts). Combining the **affine invariance** of Monge–Ampère (rescaling stretched sections back to round balls) with sharp geometric measure estimates, De Philippis and Figalli proved no singular part can survive: $$D^2\phi \in L^1_{\mathrm{loc}}$$ (in fact $$L\log^k L$$), so $$\phi \in W^{2,1}_{\mathrm{loc}}$$! That threshold is decisive: it lets analysts differentiate $$T = \nabla\phi$$ as an $$L^1$$ function and pass to strong Sobolev limits in nonlinear PDEs.

#### Step 3: Partial regularity without convexity or MTW (De Philippis–Figalli, *IHÉS*, 2015)
For general costs on $$\mathbb{R}^n$$ or $$c = d^2/2$$ on any Riemannian manifold—dropping both target convexity and the Ma–Trudinger–Wang (MTW) curvature condition—De Philippis and Figalli proved in *Partial regularity for optimal transport maps* (2015) that the optimal map between smooth densities is **$$C^\infty$$ outside a closed singular set $$\Sigma$$ of Lebesgue measure zero**! Even in wild geometries, the transport map is a smooth diffeomorphism on an open set of full measure.

#### Step 4: Turning map regularity into quantitative stability
Regularity and stability travel hand in hand. To test how close a shape $$E$$ is to an optimal body, one transports $$E$$ onto the model body via Brenier’s map: a small deficit in perimeter or energy translates into a small deviation of $$D^2\phi$$ from the identity matrix, which yields explicit geometric closeness!

Summary of Figalli’s analytic bridge:

$$
\text{Optimal map } T = \nabla\phi
\;\longleftrightarrow\;
\det D^2\phi = f/g(\nabla\phi)
\;\longleftrightarrow\;
W^{2,1} \text{ \& Smooth off } \Sigma\ (\vert\Sigma\vert=0)
\;\Longrightarrow\;
\text{Geometric stability \& Atmospheric PDE}.
$$

*(Later landmark work by Figalli, Serra, and Ros-Oton on the obstacle and Stefan problems sits in neighboring free-boundary analysis, outside the 2018 OT citation.)*

---

## 3. Three Major Applications: Crystals, Weather Fronts, and Random Matrices

1. **Quantitative anisotropic isoperimetric inequality (Wulff shapes).** In crystal physics, surface tension depends on orientation, so the energy-minimizing equilibrium shape is a convex **Wulff shape** rather than a sphere. **Figalli–Maggi–Pratelli** (*Inventiones*, 2010) used Brenier transport to prove the sharp quantitative inequality: if a set $$E$$ exceeds the Wulff perimeter by a small deficit $$\delta$$, its symmetric-difference distance to a translate of the Wulff shape is bounded by $$C\sqrt{\delta}$$ (optimal exponent $$1/2$$).
2. **Semigeostrophic (SG) equations in meteorology.** The SG system models large-scale atmospheric frontogenesis. In geostrophic coordinates (Cullen–Purser; Benamou–Brenier), the pressure potential is convex and its gradient is an optimal transport map between physical and geostrophic space. Using the new $$W^{2,1}$$ Monge–Ampère estimates, **Ambrosio–Colombo–De Philippis–Figalli** proved global weak Eulerian solutions on the 2D torus and 3D convex domains—here $$W^{2,1}$$ regularity is literally what makes the physical velocity field well-defined!
3. **Functional inequalities and probability.** With **Eric Carlen**, Figalli proved sharp stability for Gagliardo–Nirenberg and log-HLS inequalities (with Keller–Segel applications); with **Alice Guionnet**, he built approximate transport maps to prove universality in multi-matrix random models.

---

## 4. Two Fields Medals, Two Different Focuses

Because Figalli was Villani’s student, the two medals are often conflated. Keep them distinct:

| Medal | Citation focus | Shared vocabulary | Distinct claim |
|-------|----------------|-------------------|----------------|
| Villani, 2010 | Nonlinear Landau damping; convergence to equilibrium for Boltzmann | Entropy, inequalities, OT as a toolkit Villani also developed | Kinetic relaxation theorems |
| Figalli, 2018 | OT theory and applications to PDE, metric geometry, probability | Monge–Ampère, maps, stability | Regularity/stability of transport and geometric consequences |

See [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/) for the 2010 kinetic-theory story.

**Why a Fields Medal:** Figalli’s medal rewards **regularity as infrastructure**—solving borderline fully nonlinear PDE problems ($$W^{2,1}$$ and partial regularity) and exporting those estimates straight into crystal geometry, weather fronts, and random matrices.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Figalli invented optimal transport.” | Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani, and others built the subject; Figalli’s medal is regularity plus applications. |
| “Fields 2018 is the same as Villani 2010.” | Villani 2010 is Landau damping and Boltzmann; Figalli 2018 is OT and its uses. |
| “Brenier maps are always smooth.” | Convex potentials give maps a.e.; smoothness needs density, convexity, cost, and often only holds off a singular set. |
| “Caffarelli’s theory is obsolete.” | It is the foundation; later work asks what remains without its geometric hypotheses. |
| “Partial regularity means the map is $$C^\infty$$ everywhere.” | It means smooth off a closed null set; the singular set can be nonempty. |
| “OT regularity is only aesthetic.” | SG well-posedness and quantitative isoperimetry use the estimates as hypotheses, not as decoration. |

---

## Links

- IMU Fields Medals 2018: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)
- Wikipedia — Alessio Figalli: [https://en.wikipedia.org/wiki/Alessio_Figalli](https://en.wikipedia.org/wiki/Alessio_Figalli)
- ETH page (regularity of maps): [https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps](https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps)
- Quanta profile (2018): [https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/](https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/)
- arXiv search — Figalli Monge–Ampère: [https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all](https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all)
- De Philippis–Figalli $$W^{2,1}$$ (arXiv:1111.7207): [https://arxiv.org/abs/1111.7207](https://arxiv.org/abs/1111.7207)
- De Philippis–Figalli partial regularity (arXiv:1209.5640): [https://arxiv.org/abs/1209.5640](https://arxiv.org/abs/1209.5640)

---

## References

1. IMU Fields Medal 2018 citation — Alessio Figalli.
2. Y. Brenier, “Polar factorization and monotone rearrangement of vector-valued functions,” *Comm. Pure Appl. Math.* 44 (1991).
3. L. A. Caffarelli, papers on regularity of Monge–Ampère and OT maps (early 1990s); Abel 2023 citation.
4. G. De Philippis and A. Figalli, “$$W^{2,1}$$ regularity for solutions of the Monge–Ampère equation,” *Invent. Math.* 192 (2013); “Partial regularity for optimal transport maps,” *Publ. Math. IHÉS* 121 (2015); survey in *Bull. Amer. Math. Soc.* 51 (2014).
5. A. Figalli, F. Maggi, and A. Pratelli, “A mass transportation approach to quantitative isoperimetric inequalities,” *Invent. Math.* 182 (2010).
6. L. Ambrosio, M. Colombo, G. De Philippis, and A. Figalli, Eulerian well-posedness results for the semigeostrophic equations (2D periodic and 3D convex settings).
7. A. Figalli, *The Monge–Ampère Equation and Its Applications*, EMS (2017).
8. C. Villani, *Topics in Optimal Transportation*; *Optimal Transport: Old and New* — background language, not the 2010 Fields citation.
9. Course: [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/), [Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/), future [Villani]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Further directions

- Read Caffarelli’s interior estimates next to De Philippis–Figalli partial regularity: which geometric hypotheses moved from “assumed” to “unnecessary for a.e. smoothness”?
- Compare computational OT (Sinkhorn, Chapter 6) with the analytic theory: numerics regularize; regularity theory explains when the unregularized map was already almost smooth.

## Video tham khảo

- **xem trước** — [Alessio Figalli (2018 Fields Medal) explains Optimal Transport](https://www.youtube.com/watch?v=jyL6ZECM7oM) — Tom Rocks Maths, English. Watch first. “Alessio Figalli (2018 Fields Medal) explains Optimal Transport” orients the lesson’s aim: Place Figalli’s 2018 citation inside a longer OT history (Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani) without collapsing that history into one name.
- [Alessio Figalli at GYSS 2022 – Recent Developments in Optimal Transport Theory](https://www.youtube.com/watch?v=pu_WHpRDmKE) — National Research Foundation Singapore, English. A second pass once the main claim is in view: Place Figalli’s 2018 citation inside a longer OT history (Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani) without collapsing that history into one name.
