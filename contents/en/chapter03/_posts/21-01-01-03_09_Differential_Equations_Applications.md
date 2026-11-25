---
layout: post
title: "Differential Equations → Applications"
chapter: '03'
order: 9
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
lesson_type: required
---

An epidemiologist wants to know whether a flu wave will peak in three weeks or subside if schools close. A meteorologist wants to track a tropical cyclone over the next 72 hours. An electrical engineer wants to verify that a power circuit will not ring and burn out when switched on. None of them owns a crystal ball—yet all three do the exact same thing: **write down the rule stating how the current state determines the rate of change in the very next instant**.

That rule is a **differential equation**. If calculus is the alphabet, differential equations are the complete sentences describing how the physical, biological, and engineered universe evolves in space and time.

---

## Key ideas: What Is the Theory of Differential Equations?

Solving an algebraic equation like $$x^2 - 5x + 6 = 0$$ yields a few numbers. Solving a **differential equation** means finding an **entire unknown function** $$x(t)$$ or field $$u(x,y,z,t)$$ describing a system’s whole evolution.

Many students leave undergraduate courses thinking differential equations are a bag of integration tricks for closed-form formulas. In reality, 99% of real-world scientific equations **have no closed-form solution**. Modern differential-equation theory therefore focuses on **four deeper pillars**:

1. **Well-Posedness (Hadamard):** Does a solution exist, is it unique, and does a $$0.1\%$$ measurement error stay small or explode?
2. **Qualitative Analysis & Dynamical Systems:** Without ever writing a formula, determining whether trajectories settle to stable equilibria, oscillate periodically, or enter chaos.
3. **Structural Classification (ODEs and Elliptic / Parabolic / Hyperbolic PDEs):** Recognizing the physical character—does the equation smooth information (heat), propagate waves (acoustics), or enforce static equilibrium (Laplace)?
4. **Numerical Analysis:** Designing discretization schemes that stay stable on computers without letting rounding errors blow up the simulation.

---

## Learning objectives

After this lecture you should be able to:

- Distinguish ODEs from PDEs and autonomous from non-autonomous systems at a glance.
- Recognize canonical equations: linear ODE systems, heat, wave, Laplace, transport, reaction–diffusion.
- State Hadamard’s **well-posedness** slogan (existence, uniqueness, continuous dependence) and why engineers need it.
- Explain eigenmode / Fourier ideas for linear constant-coefficient problems.
- Describe finite difference / finite element / time-stepping as the industrial path when closed forms fail.
- Avoid “if I wrote an equation, it has a unique nice solution” and “numerics is just pressing solve.”

**Prerequisites.** Derivatives and the [calculus infrastructure lecture]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/). Helpful: [Fourier]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/), [Linear Algebra]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/).

---

## 1. The modeling contract

A **differential equation** relates an unknown function to its derivatives. An **initial-value problem (IVP)** adds data at a starting time; a **boundary-value problem (BVP)** adds data on a spatial boundary.

The modeling contract has three clauses:

1. **State variables** (what evolves),  
2. **Laws** (how rates depend on state, inputs, parameters),  
3. **Side conditions** (initial/boundary data that select a unique physical trajectory—when the math cooperates).

**Mechanism slogan.**  
*Prediction is solving a DE; design is often inverse—choose parameters/inputs so the solution meets specifications (optimization constrained by DEs).*

---

## 2. ODE catalog: finite-dimensional state

**First-order normal form.** Many ODEs reduce to

$$
\dot{x}=f(x,t),\qquad x(t_0)=x_0,
$$

with $$x(t)\in\mathbb{R}^d$$. Higher-order scalar equations become first-order systems by stacking $$(x,\dot{x},\ldots)$$.

**Linear systems.**

$$
\dot{x}=Ax+Bu(t)
$$

are the backbone of classical control: matrix exponential $$e^{At}$$, controllability, stability via eigenvalues of $$A$$ (for linearization, local stability). RLC circuits and linearized aircraft dynamics live here.

**Nonlinear classics.** Logistic growth $$\dot{x}=rx(1-x/K)$$; pendulum $$\ddot{\theta}+(g/\ell)\sin\theta=0$$; Lotka–Volterra predator–prey; SIR epidemic compartments. Qualitative theory (phase portraits, equilibria, Lyapunov functions) often matters more than closed formulas.

**Existence theory (ODE).** Picard–Lindelöf: if $$f$$ is Lipschitz in $$x$$, local unique solutions exist. Finite-time blowup can still occur for nonlinear $$f$$ (think $$\dot{x}=x^2$$).

---

## 3. PDE catalog: fields in space-time

| Equation | Form (schematic) | Phenomena |
|----------|------------------|-----------|
| Transport | $$\partial_t u+v\cdot\nabla u=0$$ | Advection of quantities |
| Heat / diffusion | $$\partial_t u=\kappa\Delta u$$ | Smoothing, temperature |
| Wave | $$\partial_{tt}u=c^2\Delta u$$ | Finite-speed propagation |
| Laplace / Poisson | $$\Delta u=0$$ / $$\Delta u=f$$ | Equilibrium potentials |
| Schrödinger | $$i\hbar\partial_t\psi=H\psi$$ | Quantum amplitudes |
| Reaction–diffusion | $$\partial_t u=D\Delta u+R(u)$$ | Patterns, chemistry, ecology |
| Navier–Stokes | Momentum + incompressibility | Fluids ([Ch.1]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/)) |

**Order and type** (elliptic / parabolic / hyperbolic) classify qualitative behavior: instant smoothing vs finite propagation vs boundary-driven equilibria. Getting the type wrong means using the wrong intuition and often the wrong numerical method.

**Maxwell, elasticity, general relativity** are PDE systems of immense technological and scientific impact—still the same contract: fields + equations + gauge/boundary conditions.

---

## 4. Well-posedness: Hadamard’s slogan

A problem is **well-posed** (Hadamard) if:

1. A solution **exists**,  
2. The solution is **unique**,  
3. The solution depends **continuously** on the data (stability).

Ill-posed problems are not “useless”—they appear in inverse problems (inferring the past from the present in heat flow; tomography with limited data)—but they require regularization ([Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), statistical priors).

**Engineering stakes.** Continuous dependence means small measurement or manufacturing errors do not destroy predictions. Without it, simulation can amplify nonsense. Chaos in nonlinear ODEs shows sensitive dependence even in well-posed IVPs: uniqueness can coexist with practical unpredictability over long horizons ([Chaos, Ch.4]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/) if present in course).

**Navier–Stokes Millennium problem** asks refined existence/smoothness questions in 3D—well-posedness in the strong sense is not fully settled for the equations that fly planes in CFD practice (which uses models, numerics, and engineering margins).

---

## 5. Linear structure: superposition and modes

Linear homogeneous DEs obey **superposition**: sums of solutions are solutions. For constant-coefficient linear ODEs, solutions are spans of exponentials $$e^{\lambda t}$$ with characteristic roots $$\lambda$$. For PDEs on boxes or circles, **separation of variables** produces eigenfunctions (sines, Fourier modes, spherical harmonics) with time coefficients solving simple ODEs.

**Mechanism.**  
*[Fourier analysis]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/) diagonalizes many linear constant-coefficient operators; each mode evolves independently by a scalar ODE.*

Eigenvalues determine decay (heat), oscillation (wave), or instability (positive real parts). Modal analysis in mechanical engineering is exactly this: natural frequencies and mode shapes from a discrete $$K\phi=\omega^2 M\phi$$ generalized eigenproblem after FEM discretization.

---

## 6. Nonlinear behavior: the reason closed forms fail

Nonlinearity brings:

- Multiple equilibria and bifurcations (qualitative change as parameters vary),  
- Limit cycles (van der Pol; heartbeat metaphors),  
- Chaos and strange attractors (Lorenz),  
- Shocks in conservation laws (traffic, gas dynamics)—weak solutions, entropy conditions,  
- Pattern formation (Turing) in reaction–diffusion.

Technology response: **simulate**, **reduce order**, **control**, and **validate** against experiment. Analytic exact solutions become rare treasures rather than the default.

---

## 7. Numerical methods: the industrial majority path

**Time stepping for ODEs.** Euler, Runge–Kutta, multistep methods; **stiff** equations (fast and slow scales) need implicit methods (A-stability notions). Adaptive step size is standard in solvers (ode45-class, CVODE, …).

**Space discretization for PDEs.**

- **Finite differences** — replace derivatives by stencils on grids.  
- **Finite volumes** — flux balance; conservation built-in.  
- **Finite elements** — weak forms + piecewise polynomial spaces ([Calculus lecture]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/)).  
- **Spectral / spectral-element** — high-order global or elemental bases when geometry allows.

After discretization, one solves large linear or nonlinear algebraic systems—[linear algebra]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/) and [optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/) re-enter. Stability of the scheme (CFL conditions for hyperbolic problems) is analysis, not superstition.

**Verification vs validation.** Verify that the code solves the equations; validate that the equations model reality. Both are required for trust. A beautifully converged simulation of the wrong boundary condition is still wrong—an echo of the [calculus lecture]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/) warning that software convergence is not model correctness.

**Order-of-accuracy intuition.** If you refine a mesh by a factor of two and a stable scheme’s global error drops by about four for a second-order method, you are seeing analysis at work. If error stalls, you may be limited by geometry approximation, iterative solver tolerance, or model error—not by “needing more CPU” alone.

---

### Explanation: Why a Supercomputer Simulation Can Still Explode—Checked by Hand

Even when your physical model is 100% right, choosing the wrong numerical step can ruin the answer. Verify this dramatically by hand on the simple stiff decay ODE $$y'(t) = -10 y(t)$$ with $$y(0) = 1$$ (whose exact solution $$y(t) = e^{-10t}$$ smoothly decays to $$0$$), using time step $$\Delta t = 0.25$$:

1. **Explicit (Forward) Euler blows up:** $$y_{n+1} = y_n + \Delta t\,(-10 y_n) = (1 - 10\cdot 0.25)\,y_n = (-1.5)\,y_n$$.
   - $$y_0 = 1,\quad y_1 = -1.5,\quad y_2 = +2.25,\quad y_3 = -3.375,\quad y_4 = +5.0625, \dots$$
   Because $$\lvert 1 - 10\Delta t \rvert = 1.5 > 1$$, the numerical solution **oscillates wildly to $$\pm\infty$$** even though the true solution vanishes!
2. **Implicit (Backward) Euler stays rock-solid:** $$y_{n+1} = y_n + \Delta t\,(-10 y_{n+1}) \;\Longrightarrow\; y_{n+1} = \frac{y_n}{1 + 10(0.25)} = \frac{y_n}{3.5}$$.
   - $$y_0 = 1,\quad y_1 \approx 0.286,\quad y_2 \approx 0.082,\quad y_3 \approx 0.023, \dots$$
   Clean, monotone decay to $$0$$ at the exact same step size!
3. **Beware ill-posed inverse problems:** Running the heat equation *backward* in time amplifies tiny sensor noise exponentially—refining the mesh actually makes errors worse unless you regularize.
4. **Separate Verification from Validation:** *Verification* checks “does my code solve the written equations accurately (mesh convergence)?”; *Validation* checks “do those equations match real-world experiments?”

**Quick check:** A gorgeous colorful CFD plot only earns trust after clearing both gates: **numerical stability/convergence** and **experimental validation**.

## 8. Control, inverse problems, and digital twins

**Control.** Choose input $$u(t)$$ so that $$x(t)$$ tracks a reference or stabilizes at a point. Linear-quadratic regulators, PID (classical), and model-predictive control (repeated online optimization) wrap DEs in feedback loops—autopilots, process control, robotics.

**Inverse problems.** Estimate coefficients (conductivity, stiffness) or initial state from partial observations—often ill-posed, regularized by optimization and probability.

**Digital twins.** Couple sensor streams with DE models and estimators; update parameters; optimize maintenance. The differential equation is the prior physical skeleton; data corrects it.

---

## 9. How this lecture sits in Chapter 3

| Thread | Role of DEs |
|--------|-------------|
| Calculus | Rates and accumulation become equations |
| Linear algebra | Discretized operators; modes; $$Ax=b$$ |
| Probability | Stochastic DEs; noisy data assimilation |
| Optimization | PDE-constrained design; MPC |
| Fourier | Diagonalize linear constant-coefficient PDEs |
| Graphs | Spatial discretizations; network dynamics |

The chapter theme returns: **a mathematical object (here, an equation for a function) becomes infrastructure when mechanisms—well-posedness, structure, numerics—are understood well enough to ship.**

---

### DE modeling slogans (from video research)

Primary university path: [Strang & Moler Learn DE](https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/) and [3B1B DE intro](https://www.youtube.com/watch?v=p_di4Zn4wz4).

- **Modeling contract:** state variables + laws for rates → DE + initial/boundary data.
- **Hadamard:** existence, uniqueness, continuous dependence — all three matter for engineering trust.
- Most industrial solutions are numerical; analysis still decides stability, stiffness, and validity.

## Common confusions

| Claim | Correction |
|-------|------------|
| “Writing a DE guarantees a unique global solution.” | Need existence theory; blowup and non-uniqueness can occur. |
| “CFD proves Navier–Stokes is solved as mathematics.” | Numerics and modeling ≠ Millennium well-posedness proof. |
| “Stiff means the user is stiff.” | Stiffness is a multiscale spectral property of the ODE. |
| “Finer meshes always give better answers.” | Need stable convergent schemes; model error remains. |
| “Nonlinear = unsolvable = useless.” | Qualitative theory + numerics + control are powerful. |
| “Initial and boundary conditions are optional decoration.” | They select the solution; wrong BCs yield wrong physics. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/differential-equations-applications/`.

**Recommended order**

1. **FOUNDATION** — MIT RES.18-009 — Learn Differential Equations (Strang & Moler): [https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/](https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/).
2. **FOUNDATION** — MIT Learn DE YouTube playlist: [https://www.youtube.com/playlist?list=PLUl4u3cNGP63oTpyxCMLKt_JmB0WtSZfG](https://www.youtube.com/playlist?list=PLUl4u3cNGP63oTpyxCMLKt_JmB0WtSZfG).
3. **FOUNDATION** — MIT 18.03 Differential Equations video lectures (Mattuck): [https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/).
4. **INTUITION** — 3Blue1Brown — Differential equations series hub: [https://www.3blue1brown.com/topics/differential-equations](https://www.3blue1brown.com/topics/differential-equations).
5. **ORIENTATION** — 3Blue1Brown — Differential equations, a visual introduction: [https://www.youtube.com/watch?v=p_di4Zn4wz4](https://www.youtube.com/watch?v=p_di4Zn4wz4).
6. **CORE** — Strang — First-order equations (2.087 sample): [https://www.youtube.com/watch?v=4X0SGGrXDiI](https://www.youtube.com/watch?v=4X0SGGrXDiI).

Complete URL bibliography: `research/video-research/differential-equations-applications/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/differential-equations-applications/transcripts/` · status: `research/video-research/differential-equations-applications/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/differential-equations-applications_p_di4Zn4wz4_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/differential-equations-applications/references.md`.

### Videos (primary path)

1. MIT RES.18-009 — Learn Differential Equations (Strang & Moler) — https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/
2. MIT Learn DE YouTube playlist — https://www.youtube.com/playlist?list=PLUl4u3cNGP63oTpyxCMLKt_JmB0WtSZfG
3. MIT 18.03 Differential Equations video lectures (Mattuck) — https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/
4. 3Blue1Brown — Differential equations series hub — https://www.3blue1brown.com/topics/differential-equations
5. 3Blue1Brown — Differential equations, a visual introduction — https://www.youtube.com/watch?v=p_di4Zn4wz4
6. Strang — First-order equations (2.087 sample) — https://www.youtube.com/watch?v=4X0SGGrXDiI
7. Numerical ODE solvers culture (Runge–Kutta explainers) — https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods
8. Heat equation derivations (popular PDE intros) — https://en.wikipedia.org/wiki/Heat_equation

### Videos (secondary finds)

9. Strogatz Nonlinear Dynamics lectures / book culture — https://www.youtube.com/watch?v=PVo1mHnU7WU

### Papers, books, OCW, and web

10. Hairer, Nørsett, Wanner — Solving Ordinary Differential Equations: https://link.springer.com/book/10.1007/978-3-540-78862-1
11. Wikipedia — Ordinary differential equation: https://en.wikipedia.org/wiki/Ordinary_differential_equation
12. Wikipedia — Partial differential equation: https://en.wikipedia.org/wiki/Partial_differential_equation
13. Wikipedia — Well-posed problem: https://en.wikipedia.org/wiki/Well-posed_problem
14. MIT OCW 18.03: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/
15. Strang — Differential Equations and Linear Algebra resources: https://math.mit.edu/~gs/dela/

### Course

16. Course: [Calculus]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/), [Fourier]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/), [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/), [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [Deng PDE (Ch.2)]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) if exploring modern PDE research culture. Pack: `research/video-research/differential-equations-applications/`.

## Further directions

- Re-read [Calculus → Physics & Engineering]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/) for FEM variational view.  
- Pure open problem: [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/).  
- Signal side: [Fourier]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/).  
- Restate the core mechanism of this essay in one paragraph; note one precise question you still have.

## Video tham khảo

- **xem trước** — [Differential equations, a tourist's guide | DE1](https://www.youtube.com/watch?v=p_di4Zn4wz4) — 3Blue1Brown, English. Watch first. “Differential equations, a tourist's guide | DE1” orients the lesson’s aim: Distinguish ODEs from PDEs and autonomous from non-autonomous systems at a glance.
- [2. First-Order Equations](https://www.youtube.com/watch?v=4X0SGGrXDiI) — MIT OpenCourseWare, English. A second pass once the main claim is in view: Distinguish ODEs from PDEs and autonomous from non-autonomous systems at a glance.
- [Logistic Map Explained (Strogatz Ch. 10): Period-Doubling Route to Chaos | Part 1](https://www.youtube.com/watch?v=PVo1mHnU7WU) — Dr. Shane Ross, English. Further depth after the first two, still tied to this lesson: Distinguish ODEs from PDEs and autonomous from non-autonomous systems at a glance.
