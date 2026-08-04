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

Water pours from a faucet, air rushes over a wing, blood flows in an artery. Engineers model these motions with the **Navier–Stokes equations**—partial differential equations for velocity and pressure in a viscous fluid. Those equations are used every day: aircraft design, weather forecasting, pipe networks, cardiovascular simulation. Yet one of the Clay Millennium Prize Problems asks a question that no supercomputer can settle by itself: from smooth, finite-energy initial data in three dimensions, does the continuum solution stay smooth for all time, or can singularities form in finite time?

This is **not** the same as “can we run a simulation?” Simulations discretize, truncate, and model turbulence. The Millennium question is about the **ideal continuum PDE**: existence, uniqueness, and regularity of classical solutions in 3D. Engineers fly planes without a Clay certificate; mathematicians still want to know whether the equations of incompressible viscous flow are globally well-posed in the classical sense.

This essay maps the equations, their physical meaning, what Clay actually asks, what Leray weak solutions give and withhold, major partial regularity and criteria, why three dimensions are special, how kinetic theory (Hilbert’s sixth problem; Deng’s program) relates without solving the Millennium statement, and a caution table for LO6-style literacy.

---

## Learning objectives

After this lecture you should be able to:

- Write the **incompressible Navier–Stokes** system (velocity, pressure, divergence-free constraint) and name the role of each term.
- Distinguish **engineering use** of NS (CFD, turbulence models) from the **Millennium regularity problem**.
- Explain **Leray weak solutions** versus classical smooth solutions, and why uniqueness of weak solutions in 3D is open.
- State the open problem: global existence and uniqueness of smooth solutions for smooth finite-energy 3D data—or a blow-up example.
- Name partial result families: short-time existence; 2D global regularity; small-data global results; Beale–Kato–Majda; Caffarelli–Kohn–Nirenberg partial regularity.
- Use a caution table (**LO6**): simulation ≠ weak solution theory ≠ smooth classical theory.

**Prerequisites.** Multivariable calculus (gradients, divergence, Laplacian); the idea of a PDE as a local balance law. No graduate fluids course is required—the analysis is conceptual, with precise slogans where theorems live.

**Seminar links.** Course outcome **LO1**. Pair with [Yu Deng / kinetic PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) (derivation of continuum models from particles; Hilbert’s sixth problem). Abel-facing context: [Luis Caffarelli and free boundaries / regularity]({{ site.baseurl }}/contents/en/chapter08/) when that essay is in play; partial regularity of NS is part of the same regularity culture. Applied cousin: [Differential equations applications]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/).

---

## 1. The incompressible Navier–Stokes equations

Let $$u(x,t) \in \mathbb{R}^3$$ be the **velocity** of a fluid at position $$x$$ and time $$t$$, and let $$p(x,t)$$ be the **pressure**. The incompressible Navier–Stokes system reads

$$
\begin{aligned}
\partial_t u + (u\cdot\nabla)u &= \nu \Delta u - \nabla p + f,\\
\nabla\cdot u &= 0,
\end{aligned}
$$

with viscosity coefficient $$\nu > 0$$ and optional external force $$f$$. On all of space $$\mathbb{R}^3$$ or on the periodic torus $$\mathbb{T}^3$$, one typically prescribes smooth divergence-free initial data $$u(x,0)=u_0(x)$$ with suitable decay or integrability (finite energy).

Term by term:

- $$\partial_t u$$ — local acceleration of the velocity field.
- $$(u\cdot\nabla)u$$ — **nonlinear advection**: the fluid carries its own momentum along streamlines. This is the mathematical source of much of the difficulty.
- $$\nu\Delta u$$ — **viscous diffusion**: viscosity smooths velocity gradients; larger $$\nu$$ means stickier fluid (honey vs water, in a rough metaphor).
- $$-\nabla p$$ — pressure gradient force; pressure adjusts instantaneously to enforce the constraint.
- $$\nabla\cdot u = 0$$ — **incompressibility**: the flow is volume-preserving (density constant in the simplest model); fluid does not create or destroy volume locally.
- $$f$$ — body forces (gravity, stirring, …), often set to zero in the pure mathematical problem.

The pressure is not an independent free field in the same way as $$u$$: given a divergence-free velocity evolution, $$p$$ is recovered (up to constants) by solving a Poisson-type equation obtained by taking the divergence of the momentum equation. Incompressibility is a constraint; pressure is the Lagrange multiplier that maintains it.

---

## 2. Physical meaning without drowning in continuum mechanics

**Viscosity** encodes internal friction. Momentum diffuses from fast layers to slow ones. In the limit $$\nu\to 0$$ one approaches the **Euler equations** for ideal inviscid flow—another deep PDE story, also with open problems, but not identical to the Millennium NS statement (which keeps $$\nu>0$$).

**Pressure** transmits forces through the fluid so that volume is preserved. Squeeze a parcel of incompressible fluid and pressure rises to push fluid out of the way rather than compress it.

**Incompressibility** is an idealization excellent for water and for air at low Mach number. Compressible models (density as a variable, sound waves) matter for shocks and high-speed aerodynamics; the Clay problem focuses on the incompressible viscous case as formulated by Fefferman.

**Energy.** Taking the inner product of the momentum equation with $$u$$ and integrating (with suitable boundary or decay assumptions) yields an **energy inequality**: the kinetic energy

$$
E(t) = \frac12 \int |u(x,t)|^2\,dx
$$

is controlled by the initial energy and the work of forces, while viscosity dissipates enstrophy-type quantities. Energy control is strong enough to build weak solutions—and not strong enough, by itself, to prevent possible concentration of gradients in 3D.

---

## 3. What the Millennium problem asks

Charles Fefferman’s official Clay description (paraphrased carefully) asks for a proof of one of the following in the standard function-space setting on $$\mathbb{R}^3$$ (or the torus):

- **Global regularity:** given smooth, divergence-free initial data of finite energy (and suitable force), there exists a unique smooth solution $$u,p$$ for all $$t>0$$, with quantitative control (no finite-time blow-up of natural norms); or
- **Blow-up:** there exist smooth finite-energy data for which the smooth solution cannot be continued past some finite time $$T_*$$—some norm of velocity or vorticity becomes unbounded as $$t\to T_*^-$$.

Related open issues include **uniqueness** of Leray–Hopf weak solutions and the geometric nature of any possible singular set. The prize is for a theorem in the continuum PDE, not for a numerical experiment that “looks singular” on a grid.

**Status (2026):** **open**. One of the six unsolved Millennium problems. The only solved Millennium problem is Poincaré (Perelman).

---

## 4. What is known: short time, two dimensions, weak solutions

**Short-time existence.** For smooth divergence-free initial data, there is a unique smooth solution on a positive time interval $$[0,T)$$ whose length depends on the size of the data (in suitable Sobolev or Hölder norms). The question is whether $$T=\infty$$ always, or whether $$T$$ can be finite for some data.

**Two dimensions.** In 2D, global regularity of smooth solutions is classical. A key structural reason: **vorticity stretching** is absent or far more controllable. Vorticity $$\omega = \nabla\times u$$ satisfies a transport-diffusion equation without the full 3D stretching term $$(\omega\cdot\nabla)u$$ that can amplify vorticity along vortex lines. So “2D Navier–Stokes is unsolved” is false; the Millennium hardness is three-dimensional.

**Leray (1934).** Jean Leray constructed global **weak solutions** in 3D: vector fields that satisfy the equations in a distributional sense, obey an energy inequality, and match the initial data in an appropriate topology. Existence is not the empty part of the theory. What remains open is whether these weak solutions are smooth for smooth data, whether they are unique, and whether every weak solution is classical when the data are nice.

So the landscape is not “nothing is known.” It is “global weak existence is known; global smooth well-posedness is not.”

---

## 5. Regularity criteria, small data, and partial regularity

**Conditional regularity.** If certain norms of the solution remain finite on $$[0,T]$$, then the solution stays smooth up to $$T$$. A famous example is the **Beale–Kato–Majda** criterion: control of the time integral of the $$L^\infty$$ norm of vorticity

$$
\int_0^{T} \|\omega(\cdot,t)\|_{L^\infty}\,dt < \infty
$$

prevents blow-up up to time $$T$$. Many variants exist (Prodi–Serrin conditions on velocity in mixed space-time Lebesgue spaces; Escauriaza–Seregin–Šverák endpoint results). These theorems reduce the Millennium problem to: *prove that those norms cannot explode*—or *construct data for which they do*.

**Small data.** If the initial data are sufficiently small in suitable critical spaces (e.g. small in certain scale-invariant norms), global smooth solutions exist. Large data are the battleground: the nonlinearity can, in principle, focus energy into small scales.

**Partial regularity.** For suitable weak solutions, the **Caffarelli–Kohn–Nirenberg** theorem (building on Scheffer) shows that the singular set in space-time has **parabolic Hausdorff dimension** at most 1—singularities, if any, are “small” in a precise geometric measure sense. That is a profound regularity theorem; it is not full regularity. It sits in the same intellectual neighborhood as free-boundary and minimal-surface regularity: control the size of the bad set when you cannot yet show the bad set is empty.

**Other landmarks** (names for literacy, not a complete catalog): Ladyzhenskaya, Prodi, Serrin; Kato mild solutions; modern convex integration constructions related to non-uniqueness phenomena for *weaker* notions of solution (Onsager-type and related programs)—a fast-moving area that students should treat carefully when reading popular accounts.

---

## 6. Why three-dimensional regularity is hard

The enemy is the **nonlinear term** together with **vortex stretching** in 3D. Energy estimates control the $$L^2$$ norm of velocity but do not automatically close estimates for higher derivatives. Cascades of energy to small scales—the mathematical shadow of turbulence—could, in a worst-case continuum scenario, drive gradients to infinity in finite time.

Intuition pumps in both directions:

- Viscosity *smooths*, so maybe singularities are impossible.
- Nonlinearity *concentrates*, so maybe viscosity loses the race for some data.

Neither slogan is a proof. Numerical turbulence displays wild small-scale structure, but discretization, under-resolution, finite precision, and model closures mean that a “blow-up on the computer” is not a Clay proof—and a smooth-looking simulation is not a global regularity theorem.

---

## 7. Kinetic foundations, Hilbert’s sixth problem, and Deng

There is a second great question about fluids: not only “do continuum equations stay smooth?” but “do continuum equations correctly emerge from microscopic particle systems?” That is the spirit of **Hilbert’s sixth problem** (rigorous passage from atomistic mechanics through statistical laws to continuum equations).

**Yu Deng**’s Fields-recognized program (with collaborators including Hani and Ma) builds rigorous bridges from hard-sphere dynamics toward Boltzmann kinetics and, in appropriate regimes, toward fluid equations. That supports the *derivation* of continuum models under stated hypotheses. It does **not**, by itself, prove 3D Navier–Stokes global regularity for the continuum Millennium statement.

Use the [Deng essay]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) to understand **why fluid equations exist as limits**. Use *this* essay to understand **whether those continuum equations stay smooth**. Derivation and regularity are adjacent chapters of the same book, not the same theorem.

Caffarelli’s Abel-era regularity culture (free boundaries, nonlinear PDE) is another bridge: partial regularity for NS is a cousin of geometric measure and free-boundary techniques—analysis that controls singularities without always eliminating them.

---

## 8. Engineering CFD is not the Millennium problem (LO6)

| Practice | Millennium problem |
|----------|-------------------|
| DNS / LES / RANS simulations | Global smooth theory for ideal incompressible NS |
| Mesh size, time step, turbulence closures | Existence / uniqueness / regularity theorems |
| Reynolds-number cost of resolving eddies | Analytic estimates and possible blow-up |
| Validation against experiments | Proofs in function spaces |

Both care about multi-scale energy cascades. Only one is a Clay problem. Claiming “Navier–Stokes is solved because ANSYS runs” fails LO6; claiming “planes should not fly because Clay is open” fails common sense and LO6 equally.

---

## From lectures: Tao’s blow-up culture and Caffarelli’s regularity culture

Numberphile (Crawford), Caffarelli’s Clay Millennium lecture, and Tao’s Einstein lecture share complementary slogans:

- **Caffarelli lineage:** partial regularity and free-boundary / geometric-measure ideas constrain *how bad* singularities of suitable weak solutions can be (Caffarelli–Kohn–Nirenberg is the NS landmark). Knowing the singular set is “small” is not the same as proving it is empty.
- **Tao lineage:** finite-time blow-up for *averaged* or *toy* 3D models highlights **supercriticality**—energy estimates sit at the wrong scaling to close a bootstrap for large smooth data. A blow-up theorem for a modified equation is **not** a Clay solution for true NS, and neither is a numerical “looks singular” experiment.
- **Engineering coexistence:** DNS/LES/RANS and successful CFD live in a discretized, modeled world; Clay asks continuum theorems.

**Status (as of 2026):** 3D incompressible global regularity / blow-up remains **open** (Millennium).

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Navier–Stokes is unsolved, so planes shouldn’t fly.” | Engineering models, empiricism, and CFD work; Clay asks a pure existence/regularity theorem. |
| “Someone simulated blow-up, so the problem is solved.” | Simulation ≠ proof for the continuum PDE. |
| “Deng solved Navier–Stokes.” | Deng advanced kinetic derivations; continuum 3D regularity remains open. |
| “2D and 3D are the same.” | 2D global regularity is known; 3D is the hard case. |
| “Leray already solved existence, so nothing is open.” | Weak existence ≠ smooth unique global solutions. |
| “Viscosity always prevents singularities.” | That is a hope/heuristic, not a theorem in 3D large-data NS. |

---

## Exercises

1. In the incompressible NS system, identify the nonlinear term and the viscous term. Which one is linear?
2. What does $$\nabla\cdot u = 0$$ mean physically for a fluid parcel?
3. Contrast a Leray weak solution with a classical smooth solution in two sentences each.
4. Why is the 2D theory easier at slogan level (vortex stretching)?
5. **LO1 synthesis (≤300 words):** state the Millennium NS problem, why it is hard, and one partial result family (Leray; BKM; CKN; small data—pick one and explain).
6. **LO6 table practice.** Fill in your own one-line distinction for: (a) DNS simulation, (b) Leray weak solution, (c) smooth classical solution on $$[0,\infty)$$.
7. After reading Deng: write three sentences distinguishing *derivation* of NS from *regularity* of NS.
8. Stretch: read Fefferman’s Clay official problem description and list the function-space setting he uses for initial data (names of spaces or decay conditions, as stated there).

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

### Course

9. [Yu Deng]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/), [DE applications]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/). Pack: `research/video-research/Navier_Stokes/`.

---

## Further directions

- Seminar **A3**: global regularity vs blow-up; Leray; one criterion (BKM or CKN); engineering vs Clay boundary.  
- Optional studio: Kolmogorov cascade as *heuristic*—not a proof.  
- Deng next for kinetic derivation; return here for continuum well-posedness.
