---
layout: post
title: "The Navier–Stokes Problem"
chapter: '01'
order: 5
owner: Nguyen Le Linh
lang: en
categories:
- chapter01
lesson_type: required
---

Turn on a kitchen faucet and watch a glassy column of water shatter into white, churning foam. Watch smoke curl lazily off a candle before snapping into tangled eddies, or air rush past an aircraft wing at nine hundred kilometers per hour. Since the nineteenth century, physicists and engineers have described all of these motions with a single compact pair of equations: the **Navier–Stokes equations**. They are among the most heavily used equations in all of applied science—powering weather forecasts, jet-engine design, blood-flow simulations, and ocean climate models every single day.

Yet hidden inside those familiar symbols sits one of the six unsolved **Clay Millennium Prize Problems**. It asks a question no wind tunnel and no supercomputer can settle on its own: if you start an idealized three-dimensional viscous fluid from a completely smooth, finite-energy state, does the mathematical solution stay smooth forever—or can the fluid spontaneously focus its own motion into an infinite spike of velocity or vorticity in finite time?

This is **not** a question about whether engineers can simulate turbulence or whether airplanes are safe to fly. Simulations chop space into grids, step forward in discrete ticks, and approximate small-scale eddies with turbulence models. The Millennium Prize asks about the **exact continuum partial differential equations** themselves: whether three-dimensional incompressible viscous flow is globally well-posed in the classical sense.

---

## Learning objectives

After this lecture you should be able to:

- Write the **incompressible Navier–Stokes** system (velocity, pressure, divergence-free constraint) and explain the physical and mathematical role of each term.
- Distinguish **engineering CFD** (discretized simulations and turbulence models) from the **Millennium regularity problem** for the continuum PDE.
- Explain the gap between **Leray weak solutions** and classical smooth solutions, and why uniqueness and smoothness in 3D remain open.
- State the Clay problem cleanly: global existence and smoothness for smooth finite-energy 3D data—or a finite-time blow-up example.
- Recognize the main partial results: short-time smooth existence, 2D global regularity, small-data global regularity, Beale–Kato–Majda, and Caffarelli–Kohn–Nirenberg partial regularity.
- Separate three distinct worlds cleanly: numerical simulation ≠ weak solution theory ≠ classical smooth solution theory.

**Prerequisites.** Multivariable calculus (gradients, divergence, Laplacian) and the idea of a PDE as a local balance law. No graduate fluid-mechanics course is required—everything is built from concrete examples and clear physical intuition.

**Course links.** Pair with [Yu Deng / kinetic PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) (deriving continuum fluid models from colliding particles; Hilbert’s sixth problem), [Luis Caffarelli and regularity]({{ site.baseurl }}/contents/en/chapter08/) (free boundaries and partial regularity culture), and [Differential equations applications]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/).

---

## Key ideas: What Fields Sit Behind Navier–Stokes?

To understand why a classic nineteenth-century physics equation still defies twenty-first-century mathematics, it helps to see the three mathematical disciplines that meet inside Navier–Stokes.

### 1. Partial Differential Equations (PDEs) and Continuum Mechanics
A **partial differential equation** links a function of several variables—here, velocity $$u(x,t)$$ and pressure $$p(x,t)$$ depending on space $$x \in \mathbb{R}^3$$ and time $$t \ge 0$$—to its rates of change in space and time. Navier–Stokes is simply Newton’s second law $$F = ma$$ written for every infinitesimal parcel of fluid simultaneously.
- **Core questions:** Given smooth initial data, does a solution exist? Is it unique? Does it remain smooth for all time, or can derivatives blow up in finite time (*finite-time singularity*)?
- **Real-world reach:** Aerodynamics, weather and climate modeling, arterial blood flow, oil pipelines, acoustics, and structural vibration.

### 2. Functional Analysis and Sobolev Spaces
In undergraduate calculus, you differentiate smooth functions pointwise. In nonlinear PDEs, you often cannot prove smoothness up front—so mathematicians work in **function spaces** such as $$L^2$$ (finite kinetic energy) and **Sobolev spaces** $$H^k$$ (functions whose derivatives up to order $$k$$ have finite $$L^2$$ energy), using **weak (distributional) solutions** defined via integration by parts.
- **Core questions:** How do integral energy bounds control higher derivatives? When does a weak solution automatically upgrade to a smooth classical solution (*regularity theory*)?
- **Real-world reach:** Finite element methods (FEM) in engineering software, signal processing, inverse problems in medical imaging, and rigorous error bounds for numerical PDE solvers.

### 3. Scaling Analysis, Harmonic Analysis, and Geometric Measure Theory
Navier–Stokes has an exact **scaling symmetry**: if you zoom in on space by a factor $$\lambda$$, speed up time by $$\lambda^2$$, and rescale velocity by $$\lambda$$, a solution maps to another solution. Comparing how conserved quantities (like kinetic energy) behave under this zoom tells you whether your estimates get stronger or weaker at tiny scales—a distinction called **subcritical**, **critical**, or **supercritical**.
- **Core questions:** If singularities do occur, how large can the singular set be in space-time? Can energy cascade to arbitrarily small scales fast enough to defeat viscous smoothing?
- **Real-world reach:** Turbulence modeling, multiscale physics, atmospheric boundary layers, and image denoising via geometric PDEs.

---

## 1. The incompressible Navier–Stokes equations

Let $$u(x,t) \in \mathbb{R}^3$$ be the **velocity** of a fluid at position $$x$$ and time $$t$$, and let $$p(x,t)$$ be the **pressure**. The incompressible Navier–Stokes system reads

$$
\begin{aligned}
\partial_t u + (u\cdot\nabla)u &= \nu \Delta u - \nabla p + f,\\
\nabla\cdot u &= 0,
\end{aligned}
$$

with kinematic viscosity $$\nu > 0$$ and optional external force $$f$$. On all of space $$\mathbb{R}^3$$ or on the periodic torus $$\mathbb{T}^3$$, one prescribes smooth divergence-free initial data $$u(x,0)=u_0(x)$$ with finite kinetic energy.

Read it term by term as a tug-of-war:

- $$\partial_t u$$ — local acceleration of the velocity field at a fixed point.
- $$(u\cdot\nabla)u$$ — **nonlinear advection**: the fluid carries its own momentum along streamlines. Because velocity multiplies its own gradient, this quadratic term can steepen gradients and create eddies—it is the heart of the mathematical difficulty.
- $$\nu\Delta u$$ — **viscous diffusion**: internal friction smooths out sharp velocity differences, just like heat diffusion smooths temperature spikes. Larger $$\nu$$ means thicker, stickier fluid (honey versus water).
- $$-\nabla p$$ — pressure-gradient force pushing fluid from high pressure to low pressure.
- $$\nabla\cdot u = 0$$ — **incompressibility**: every small parcel preserves its volume as it moves.
- $$f$$ — external body forces (gravity, stirring), usually set to $$0$$ in the pure mathematical problem.

Notice that pressure $$p$$ has no time-derivative term $$\partial_t p$$ of its own. Taking the divergence of the momentum equation and using $$\nabla\cdot u = 0$$ gives a Poisson equation $$-\Delta p = \nabla\cdot\bigl((u\cdot\nabla)u\bigr)$$ (when $$f=0$$). Incompressibility is a rigid constraint, and pressure acts instantaneously as the Lagrange multiplier that enforces it across the entire fluid.

---

### Worked Example 1: Verifying an Exact Solution by Hand (Poiseuille Pipe Flow)

Before wrestling with 3D turbulence, let’s check a real, exact solution of Navier–Stokes with nothing more than first-year multivariable calculus. Imagine water flowing steadily between two horizontal plates at $$y = -1$$ and $$y = 1$$, driven by a constant pressure drop along the $$x$$-axis. Consider the parabolic velocity profile (2D **Poiseuille flow**):

$$
u(x,y,t) = \bigl(U(1-y^2),\, 0\bigr), \qquad p(x,y,t) = -2\nu U x,
$$

where $$U > 0$$ is the centerline speed and $$f = 0$$. Let’s substitute every term directly into the equations:

1. **Incompressibility ($$\nabla\cdot u = 0$$):**
   $$
   \partial_x\bigl(U(1-y^2)\bigr) + \partial_y(0) = 0 + 0 = 0. \quad \checkmark
   $$
2. **Time derivative ($$\partial_t u$$):** The flow is steady, so $$\partial_t u = (0,0)$$.
3. **Nonlinear advection ($$(u\cdot\nabla)u$$):**
   $$
   (u\cdot\nabla)u_x = u_x \partial_x u_x + u_y \partial_y u_x = U(1-y^2)\cdot 0 + 0\cdot (-2Uy) = 0,
   $$
   and similarly $$(u\cdot\nabla)u_y = 0$$. The fluid layers slide neatly past one another without mixing, so the dreaded nonlinearity vanishes identically!
4. **Viscous diffusion ($$\nu\Delta u$$):**
   $$
   \nu\Delta u_x = \nu\bigl(\partial_{xx} + \partial_{yy}\bigr)\bigl(U(1-y^2)\bigr) = \nu(0 - 2U) = -2\nu U, \qquad \nu\Delta u_y = 0.
   $$
5. **Pressure gradient ($$-\nabla p$$):**
   $$
   -\nabla p = -\bigl(\partial_x(-2\nu Ux),\, \partial_y(-2\nu Ux)\bigr) = (2\nu U,\, 0).
   $$
6. **Balance check:** Left-hand side $$= (0,0)$$. Right-hand side $$= \nu\Delta u - \nabla p = (-2\nu U, 0) + (2\nu U, 0) = (0,0)$$. Exact match!

**What this teaches us:** When flow is laminar and symmetric, the nonlinear term $$(u\cdot\nabla)u$$ cancels out, and pressure simply balances friction. The Millennium Prize nightmare begins in full 3D when streamlines twist and fold so that $$(u\cdot\nabla)u$$ does *not* vanish—instead, it feeds on itself.

---

## 2. Physical meaning without drowning in continuum mechanics

**Viscosity** encodes internal friction: momentum diffuses from fast-moving layers to slower neighbors. In the inviscid limit $$\nu\to 0$$, Navier–Stokes formally turns into the **Euler equations** for ideal frictionless flow—another deep PDE story with its own open blow-up questions, distinct from the Millennium problem (which strictly keeps $$\nu > 0$$).

**Incompressibility** is an accurate idealization for water and for air well below the speed of sound. Compressible models (varying density, shock waves) govern supersonic flight; Charles Fefferman’s Clay formulation focuses on the incompressible viscous case.

**Energy.** Taking the inner product of the momentum equation with $$u$$ and integrating over space (with $$f=0$$ and suitable decay at infinity) makes the nonlinear advection and pressure terms integrate to zero, leaving the fundamental **energy identity** (for smooth solutions):

$$
\frac{d}{dt}\left(\frac{1}{2}\int_{\mathbb{R}^3} |u(x,t)|^2\,dx\right) = -\nu \int_{\mathbb{R}^3} |\nabla u(x,t)|^2\,dx.
$$

In plain words: kinetic energy $$E(t) = \frac{1}{2}\int |u|^2\,dx$$ can only decrease, and the rate of loss equals viscosity times the total squared velocity gradient (**enstrophy**). That single conservation-dissipation law is strong enough to construct global weak solutions—yet, as we are about to calculate by hand, it is *not* strong enough to stop gradients from concentrating at tiny scales in 3D.

---

## 3. What the Millennium problem asks

Charles Fefferman’s official Clay problem statement asks for a rigorous proof of **either** of the following on $$\mathbb{R}^3$$ (or the periodic torus $$\mathbb{T}^3$$):

- **Global regularity:** for every smooth, divergence-free initial velocity $$u_0$$ of finite energy (and smooth rapidly decaying force, or $$f=0$$), there exists a unique smooth solution $$(u,p)$$ defined for all $$t > 0$$, with bounded kinetic energy; **or**
- **Finite-time blow-up:** there exist smooth, finite-energy initial data for which the smooth solution breaks down at some finite time $$T_* < \infty$$—some norm of velocity or vorticity explodes as $$t \to T_*^-$$.

Related open questions include **uniqueness** of Leray–Hopf weak solutions and the exact geometry of any possible singular set. The prize rewards a mathematical theorem about the continuum PDE, not a simulation that merely *looks* singular on a finite mesh.

**Status (2026):** **open**—one of the six unsolved Millennium Prize Problems (only Poincaré has been solved, by Grigori Perelman).

---

## 4. What is known: short time, two dimensions, weak solutions

**Short-time existence.** Starting from smooth divergence-free initial data, there is always a unique smooth solution on some positive time interval $$[0, T)$$ whose length depends on the size of the initial data. The entire mystery is whether $$T$$ can always be extended to $$\infty$$, or whether some clever initial swirl forces $$T < \infty$$.

**Two dimensions are solved.** In 2D, global existence and uniqueness of smooth solutions has been known since the 1950s (Ladyzhenskaya and others). Structurally, **vortex stretching** is impossible in a flat plane: the vorticity $$\omega = \nabla \times u$$ is just a scalar perpendicular to the plane, so it merely gets carried and diffused without the 3D stretching term $$(\omega\cdot\nabla)u$$ that amplifies spin when a vortex tube is pulled thinner (like a figure skater pulling in their arms).

**Leray’s weak solutions (1934).** Long before computers, Jean Leray proved that global **weak solutions** exist in 3D for any finite-energy initial data: vector fields satisfying the equations in a distributional (integrated) sense and obeying the energy inequality. So existence itself is *not* the missing piece. What remains open is whether Leray’s weak solutions stay smooth, whether they are unique, and whether smooth data can ever develop a singularity.

---

### Worked Example 2: Scaling the Kinetic Energy — Why 2D Works and 3D Hits a Wall

Why is 2D Navier–Stokes a classical theorem while 3D is worth a million dollars? One three-line calculation reveals the exact mathematical cliff.

Navier–Stokes (with $$f=0$$) is invariant under **parabolic rescaling**: if $$u(x,t)$$ is a solution on $$\mathbb{R}^d$$, then for any zoom factor $$\lambda > 0$$,

$$
u_\lambda(x,t) = \lambda\, u(\lambda x,\, \lambda^2 t), \qquad p_\lambda(x,t) = \lambda^2\, p(\lambda x,\, \lambda^2 t)
$$

is *also* an exact solution! Think of $$\lambda \gg 1$$ as zooming into a tiny region of size $$1/\lambda$$ over a tiny time window $$1/\lambda^2$$, where a potential blow-up would live.

Now compute the kinetic energy $$E(u_\lambda)$$ at time $$t=0$$ by substituting $$y = \lambda x$$ (so $$dx = \lambda^{-d}\,dy$$):

$$
E(u_\lambda) = \frac{1}{2}\int_{\mathbb{R}^d} |\lambda\, u(\lambda x)|^2\,dx = \frac{1}{2}\lambda^2 \int_{\mathbb{R}^d} |u(y)|^2\,\lambda^{-d}\,dy = \lambda^{2-d}\, E(u).
$$

Plug in the dimension $$d$$ and watch what happens as you zoom into a tiny scale ($$\lambda \to \infty$$):

| Dimension $$d$$ | Rescaled Energy $$E(u_\lambda)$$ | As $$\lambda \to \infty$$ (tiny scale) | Regime |
|-----------------|----------------------------------|----------------------------------------|--------|
| $$d = 2$$ | $$\lambda^{2-2}\,E(u) = E(u)$$ | Stays **constant** | **Critical** (energy controls small scales!) |
| $$d = 3$$ | $$\lambda^{2-3}\,E(u) = \lambda^{-1} E(u)$$ | Shrinks to **0**! | **Supercritical** (energy goes blind!) |

**What this means:** In 3D, a tiny, ultra-violent vortex of size $$1/\lambda$$ with huge velocity $$\sim \lambda$$ carries only $$\lambda^{-1}$$ of the original kinetic energy. You could pack a blow-up singularity inside an arbitrarily small budget of kinetic energy! Because the only global conserved/dissipated quantity we know—energy—becomes *tiny* at small scales in 3D, energy bounds alone cannot rule out a blow-up. This **supercriticality barrier** is the central technical obstacle of the Millennium problem.

---

## 5. Regularity criteria, small data, and partial regularity

Even without a full solution, analysts have mapped out a rich landscape of partial theorems:

- **Conditional regularity (Beale–Kato–Majda, 1984).** If the time integral of peak vorticity stays finite on $$[0,T]$$,
  $$
  \int_0^{T} \|\omega(\cdot,t)\|_{L^\infty}\,dt < \infty,
  $$
  then the solution stays smooth up to $$T$$. Related **Prodi–Serrin** and **Escauriaza–Seregin–Šverák** criteria give sharp mixed space-time integrability thresholds. In short: a solution cannot blow up quietly—its vorticity must spike hard enough to make this integral diverge.
- **Small-data global regularity.** If the initial velocity is sufficiently small in a *scale-invariant (critical)* norm, viscous smoothing wins permanently and a unique global smooth solution exists. The battleground is strictly **large initial data**.
- **Partial regularity (Caffarelli–Kohn–Nirenberg, 1982).** Building on Scheffer, they proved that for *suitable* weak solutions in 3D, any possible singular set in 4D space-time has **1-dimensional parabolic Hausdorff measure zero**—meaning singularities, if they exist at all, cannot even form a continuous 1D curve in space-time! It is a triumph of geometric regularity theory, yet knowing the bad set has dimension $$< 1$$ still falls short of proving it is empty.
- **Modern non-uniqueness context.** Recent **convex integration** results (Buckmaster–Vicol and collaborators) constructed non-unique *very weak* solutions (weaker than Leray–Hopf, without the local energy inequality). They show how subtle the notion of "solution" is, without yet settling Leray–Hopf uniqueness or smooth blow-up.

---

### Explanation: From Vortex Stretching to the Supercriticality Barrier

If you want to carry the whole mathematical plot of 3D Navier–Stokes in your head without getting lost in functional-analysis notation, follow these four steps slowly.

#### Step 1: Take the curl to watch vorticity stretch in 3D
Apply the curl operator ($$\nabla \times$$) to the Navier–Stokes momentum equation. Pressure disappears ($$\nabla\times\nabla p = 0$$), leaving the **vorticity equation** for $$\omega = \nabla \times u$$:
$$
\partial_t \omega + (u\cdot\nabla)\omega = \nu \Delta \omega + (\omega\cdot\nabla)u.
$$
In 2D, the stretching term $$(\omega\cdot\nabla)u$$ is identically zero, so vorticity obeys a clean transport-diffusion equation and peak vorticity can never explode. In 3D, $$(\omega\cdot\nabla)u$$ acts like a quadratic feedback loop ($$\sim |\omega|^2$$): stretching a vortex tube makes it thinner and spins it faster, just like an ice skater pulling in their arms. If $$\dot{y} = y^2$$, the solution $$y(t) = 1/(1-t)$$ hits infinity at $$t = 1$$. The entire 3D problem is whether $$\nu\Delta\omega$$ always beats this geometric self-amplification.

#### Step 2: Why Leray (1934) could prove global existence—but not smoothness
Because the energy identity gives a rock-solid global bound on $$\int |u|^2\,dx$$ and $$\int_0^T \int |\nabla u|^2\,dx\,dt$$, Jean Leray could approximate the equation, take a weak limit, and produce a global **weak solution** for every finite-energy initial condition. The catch: taking weak limits in $$L^2$$ preserves energy, but it does *not* prevent high-frequency oscillations from concentrating at a point. So Leray proved a solution exists globally, without being able to guarantee it stays smooth or unique.

#### Step 3: Why every known global estimate is "supercritical"
As we saw in Worked Example 2, under the exact scaling $$u_\lambda(x,t) = \lambda u(\lambda x, \lambda^2 t)$$, kinetic energy scales as $$\lambda^{-1}$$ in 3D. Every known unconditional global quantity for 3D Navier–Stokes is similarly **supercritical**—meaning that if you zoom into a putative blow-up point, the known global bound becomes weaker, not stronger. In 2016, Terence Tao sharpened this diagnosis by constructing an *averaged* 3D Navier–Stokes model that obeys the exact same energy identity and scaling laws—and proved that it **does** blow up in finite time! His message: any proof of global regularity for true Navier–Stokes *must* use fine geometric structure of the nonlinear term, not just energy and scaling.

#### Step 4: Why supercomputers cannot close the Millennium gap
Direct Numerical Simulation (DNS) at high Reynolds numbers reveals breathtaking cascades of tiny vortices, and occasional numerical studies look tantalizingly close to blow-up. Yet a computer always operates on a finite grid with finite floating-point precision. A simulated spike might simply be grid under-resolution, while a smooth-looking simulation might miss an ultra-thin blow-up profile hiding in an unstable corner of infinite-dimensional function space. Only a theorem in the continuum PDE settles the Clay prize.

---

## 6. Why three-dimensional regularity is hard

Intuition pulls convincingly in both directions:

- **Viscosity smooths**, so perhaps every sharp gradient is smeared out before it can reach infinity.
- **Nonlinearity concentrates**, so perhaps a carefully orchestrated collision of vortex rings can focus energy to a single point faster than viscosity can diffuse it.

Neither intuition is a proof. That balance—between a smoothing Laplacian and a stretching nonlinearity in a supercritical dimension—is what keeps 3D Navier–Stokes standing more than ninety years after Leray.

---

## 7. Kinetic foundations, Hilbert’s sixth problem, and Deng

There is a second great question about fluids: not only *“do the continuum equations stay smooth?”*, but *“do those continuum equations rigorously emerge from trillions of colliding microscopic particles?”* That is the heart of **Hilbert’s sixth problem**.

**Yu Deng**’s program (with Zaher Hani and Xiao Ma) builds rigorous mathematical bridges from microscopic hard-sphere dynamics to the Boltzmann kinetic equation and, in appropriate scaling limits, toward continuum fluid equations. That advances the *derivation* of fluid equations from particle physics; it does **not**, by itself, prove global smooth regularity for the continuum 3D Navier–Stokes Millennium problem.

Use the [Deng essay]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) to understand **why continuum fluid equations emerge as limits**, and *this* essay to understand **whether those continuum equations stay smooth for all time**. Derivation and regularity are adjacent chapters of the same book, not the same theorem.

Caffarelli’s regularity culture (free boundaries, nonlinear PDE) is the complementary bridge: partial regularity for Navier–Stokes belongs to the same geometric-measure tradition that bounds how bad singularities can be even before proving they cannot exist.

---

## 8. Engineering CFD is not the Millennium problem

| Engineering Practice (CFD) | Clay Millennium Problem |
|----------------------------|-------------------------|
| DNS / LES / RANS simulations | Global smooth theory for ideal incompressible 3D NS |
| Mesh resolution, time step, turbulence closures | Existence, uniqueness, and regularity theorems |
| Computing cost at high Reynolds numbers | Analytic estimates and possible finite-time blow-up |
| Validation against wind tunnels & experiments | Rigorous proofs in infinite-dimensional function spaces |

Both worlds care deeply about multi-scale energy cascades. Only one is a Clay Prize problem. Claiming “Navier–Stokes is solved because ANSYS simulates airplanes” confuses numerical approximation with continuum proof; claiming “planes shouldn’t fly because Clay is open” confuses a mathematical regularity question with validated engineering.

---

## From lectures: Tao’s blow-up culture and Caffarelli’s regularity culture

Numberphile (Tom Crawford), Luis Caffarelli’s Clay Millennium lecture, and Terence Tao’s Einstein lecture offer three complementary lenses:

- **Caffarelli lineage:** partial regularity and geometric-measure ideas constrain *how bad* singularities of suitable weak solutions can be (Caffarelli–Kohn–Nirenberg). Knowing the singular set is tiny is not the same as proving it is empty.
- **Tao lineage:** finite-time blow-up for *averaged* 3D models exposes **supercriticality**—energy estimates sit at the wrong scaling to close a bootstrap for large smooth data. A blow-up theorem for a modified equation is **not** a Clay solution for true Navier–Stokes, and neither is a numerical experiment.
- **Engineering coexistence:** DNS/LES/RANS live in a discretized, modeled world; Clay asks for continuum theorems.

In a lighter [Big Think conversation](https://www.youtube.com/watch?v=OOMx2BHHWtE) for *Six Math Essentials*, Tao points to a classical neighbor: Newton’s **two-body** problem is solved in closed form, while the **three-body** problem already erupts into long-term unpredictability. Navier–Stokes is not literally “the three-body problem for water,” yet it sits in the same territory where simple deterministic laws still owe us a global mathematical theory. See [Six Math Essentials]({{ site.baseurl }}/contents/en/chapter04/04_01_Six_Math_Essentials/) and [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/).

**Status (as of 2026):** 3D incompressible global regularity / blow-up remains **open** (Millennium).

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Navier–Stokes is unsolved, so planes shouldn’t fly.” | Engineering models, wind tunnels, and CFD work reliably; Clay asks a pure continuum regularity theorem. |
| “Someone simulated blow-up, so the problem is solved.” | Numerical simulation ≠ proof for the continuum PDE. |
| “Deng solved Navier–Stokes.” | Deng advanced kinetic derivations from particles; continuum 3D regularity remains open. |
| “2D and 3D are the same.” | 2D global regularity is a classical theorem; 3D is the open supercritical case. |
| “Leray already solved existence, so nothing is open.” | Global weak existence ≠ unique, globally smooth classical solutions. |
| “Viscosity always prevents singularities.” | That is a physical hope, not a theorem for large-data 3D Navier–Stokes. |

---

## Video sources (math-video-researcher pack)

Full ranking and notes: `research/video-research/Navier_Stokes/`.

**Recommended order**

1. **Orientation** — Numberphile, *Navier-Stokes Equations* (Tom Crawford): [YouTube](https://www.youtube.com/watch?v=ERBVFcutl3M) · [page](https://www.numberphile.com/videos/navier-stokes-equations).  
2. **Intuition** — vcubingx, *The million dollar equation*: [YouTube](https://www.youtube.com/watch?v=Ra7aQlenTb8).  
3. **Foundation** — Luis Caffarelli, Clay Millennium lecture on NS existence/smoothness: [YouTube](https://www.youtube.com/watch?v=ta6Q70y6YVU).  
4. **Core research lecture** — Terence Tao, *Can the Navier-Stokes Equations Blow Up in Finite Time?* (Einstein Lecture): [YouTube](https://www.youtube.com/watch?v=DgmuGqeRTto).  
5. **Written official** — Fefferman PDF: [navierstokes.pdf](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf) · [Clay page](https://www.claymath.org/millennium/navier-stokes-equation/).

**After videos:** CFD success ≠ Clay theorem. Weak ≠ smooth. Status **open** as of 2026.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Navier_Stokes/transcripts/` · status: `research/video-research/Navier_Stokes/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Navier_Stokes_ERBVFcutl3M_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full bibliography: `research/video-research/Navier_Stokes/references.md`.

### Official and surveys

1. Clay — [Navier–Stokes Equation](https://www.claymath.org/millennium/navier-stokes-equation/) · Fefferman PDF: https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf  
2. J. C. Robinson — [The Navier–Stokes regularity problem](https://royalsocietypublishing.org/rsta/article/378/2174/20190526/111659/The-Navier-Stokes-regularity-problem).  
3. Wikipedia — [NS existence and smoothness](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness).  
4. Constantin & Foias; CKN partial regularity; Beale–Kato–Majda.  

### Videos

5. Numberphile NS: https://www.youtube.com/watch?v=ERBVFcutl3M  
6. vcubingx: https://www.youtube.com/watch?v=Ra7aQlenTb8  
7. Caffarelli Clay lecture: https://www.youtube.com/watch?v=ta6Q70y6YVU  
8. Tao Einstein lecture: https://www.youtube.com/watch?v=DgmuGqeRTto  
8b. Tao Big Think (six essentials; 2-body vs 3-body): https://www.youtube.com/watch?v=OOMx2BHHWtE  

### Course

9. [Yu Deng]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/), [DE applications]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/). Pack: `research/video-research/Navier_Stokes/`.

---

## Further directions

- Seminar brief: global regularity vs blow-up; Leray weak solutions; one criterion (BKM or CKN); engineering CFD vs Clay boundary.  
- Optional studio: Kolmogorov cascade as a *heuristic*—not a proof.  
- Read [Yu Deng]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) next for kinetic derivation; return here for continuum well-posedness.

## Video tham khảo

- **xem trước** — [Navier-Stokes Equations - Numberphile](https://www.youtube.com/watch?v=ERBVFcutl3M) — Numberphile, English. Watch first. “Navier-Stokes Equations - Numberphile” orients the lesson’s aim: Write the incompressible Navier–Stokes system (velocity, pressure, divergence-free constraint) and name the role of each term.
- [The million dollar equation (Navier-Stokes equations)](https://www.youtube.com/watch?v=Ra7aQlenTb8) — vcubingx, English. A second pass once the main claim is in view: Write the incompressible Navier–Stokes system (velocity, pressure, divergence-free constraint) and name the role of each term.
- [Luis Caffarelli, Navier-Stokes existence and smoothness](https://www.youtube.com/watch?v=ta6Q70y6YVU) — Clay Mathematics Institute, English. Further depth after the first two, still tied to this lesson: Write the incompressible Navier–Stokes system (velocity, pressure, divergence-free constraint) and name the role of each term.
