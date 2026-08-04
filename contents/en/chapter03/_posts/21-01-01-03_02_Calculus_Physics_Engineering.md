---
layout: post
title: "Calculus → Physics & Engineering"
chapter: '03'
order: 2
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
---

A bridge does not stay up because someone “used formulas.” It stays up because **local rates of change** of stress and displacement were constrained by balance laws, then integrated—analytically or numerically—into a global design that tolerates load, wind, and fatigue. That pipeline is calculus as infrastructure.

**Path:** rates and accumulation → fundamental theorem → Newton’s law as ODE → space enters (PDEs) → variational thinking → finite elements → engineering domains → confusions.

This lecture is not a first course in derivatives. It is a map of **why calculus became the mother tongue of classical physics and much of engineering**, and what precise ideas make simulation, control, and design possible.

---

## Learning objectives

After this lecture you should be able to:

- Explain differentiation and integration as twin operations linked by the fundamental theorem of calculus.
- Write Newton’s second law as a differential equation and interpret force, mass, and acceleration in that language.
- Distinguish ordinary differential equations (ODEs) from partial differential equations (PDEs) and name canonical examples (heat, wave, Laplace).
- Describe, at slogan level, how the **finite element method** turns continuous balance laws into large linear algebra problems.
- Name three engineering domains that speak calculus fluently and say *what* is being differentiated or integrated.
- Avoid the confusions “calculus is only high-school formulas” and “simulation replaces mathematics.”

**Prerequisites.** High-school calculus intuition (slope, area). Comfort with the idea of a function of several variables helps for PDEs; no prior PDE course is required.

**Seminar links.** Pairs with [Differential Equations]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/), [Navier–Stokes (Ch.1)]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/), and Fourier methods later in this chapter.

---

## 1. Two ideas, one engine

**Differentiation** answers: how fast does something change *right now*? If position is $$x(t)$$, velocity is $$x'(t)$$ and acceleration is $$x''(t)$$. In economics, marginal cost is a derivative of total cost; in circuits, current can be the rate of change of charge.

**Integration** answers: how does change accumulate over an interval? Distance traveled is the integral of speed; work is the integral of force along a path; total heat content is an integral of a density over a body.

These are not two unrelated school topics. The **fundamental theorem of calculus** is the hinge that makes modeling possible: under suitable hypotheses, differentiation and integration are inverses. Local rates determine global totals; global constraints constrain local rates. Physics is written on that hinge.

Formally, if $$F'(x)=f(x)$$ on an interval, then

$$
\int_a^b f(x)\,dx = F(b)-F(a).
$$

The slogan for this course: **calculus is the algebra of continuous change**. Once you accept continuous state variables, nearly every classical continuum theory becomes a story about derivatives, integrals, and the equations that bind them.

---

## 2. From geometry to dynamics: Newton’s language

Historically, calculus emerged from geometry (tangents, areas) and became the tool of **dynamics**. Newton and Leibniz did not invent “tricks for exams”; they invented a language for continuous change.

**Newton’s second law** in one dimension,

$$
m \frac{d^2 x}{dt^2} = F\bigl(x,\tfrac{dx}{dt},t\bigr),
$$

is already a differential equation: the unknown is a *function* $$x(t)$$, constrained by its second derivative. Classical mechanics is a universe of such equations—with vectors, constraints, and Lagrangian/Hamiltonian reformulations in higher dimensions.

**Mechanism in one sentence.**  
*Physical laws often state how rates of change of state depend on the state itself; solving the resulting differential equations predicts future behavior from initial data.*

Once that is accepted, catalogs open: mass–spring–damper systems, idealized planetary motion, RC/RLC circuits, population models, chemical kinetics. Engineering control theory then asks the dual question: *what input force or voltage steers the state where we want it?*

---

## 3. Ordinary vs partial: when space enters

**Ordinary differential equations (ODEs)** involve derivatives with respect to one independent variable (often time). A scalar mass–spring system

$$
m\ddot{x} + c\dot{x} + kx = f(t)
$$

is an ODE. State lives in a finite-dimensional space (here position and velocity).

**Partial differential equations (PDEs)** involve several independent variables—typically space and time. The heat equation

$$
\partial_t u = \kappa \Delta u
$$

says temperature $$u(x,t)$$ changes at a rate proportional to the Laplacian $$\Delta u$$ (local averaging / curvature of the temperature field). The wave equation

$$
\partial_{tt} u = c^2 \Delta u
$$

propagates disturbances at finite speed $$c$$. Laplace’s equation $$\Delta u=0$$ describes steady-state potentials (electrostatics, incompressible flow potentials, equilibrium membranes under suitable idealizations).

**Why the distinction matters for technology.** ODE models dominate lumped circuits, rigid-body mechanics, and many control loops. PDE models dominate continuum fields: heat in engines, stress in solids, electromagnetic fields (Maxwell), fluid velocity (Navier–Stokes). “Simulation” in industry is often: discretize a PDE, solve huge algebraic systems, visualize fields—still calculus underneath, plus numerical analysis.

For the open analytic questions about fluids, see [Navier–Stokes existence and smoothness]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/).

---

## 4. Conservation, flux, and the continuum template

Much of continuum physics follows one template:

1. Pick a quantity (mass, energy, momentum, charge).
2. Write a **balance law**: rate of change inside a region equals flux through the boundary plus sources.
3. Convert the integral balance into a **differential** equation via the divergence theorem.
4. Close the system with **constitutive laws** (Fourier’s law for heat flux, Hooke’s law for stress–strain, Ohm’s law, etc.).

For heat, Fourier’s law says heat flux is proportional to $$-\nabla u$$. Combined with energy balance, one recovers the heat equation. The math is not decoration: the divergence theorem is the precise reason integral “accounting” becomes a PDE.

**Mechanism.**  
*Conservation + constitutive response → PDE; geometry of the domain and boundary conditions select which solutions are physical.*

---

## 5. Gradient, divergence, and curl (vector calculus toolkit)

Continuum models speak **fields**: a **scalar field** assigns a number to each point (temperature, pressure, height), and a **vector field** assigns a vector (wind, velocity, force). Once those objects are in place, three operators built from the del symbol $$\nabla$$ appear everywhere in physics and engineering.

### Scalar vs vector fields (quick vocabulary)

| Object | Meaning | Everyday picture |
|--------|---------|------------------|
| Scalar | Magnitude only | Temperature $$30^\circ\mathrm{C}$$ |
| Vector | Magnitude + direction | Wind 10 units east |
| Scalar field | Scalar at every point | Temperature map $$T(x,y)$$ |
| Vector field | Vector at every point | Wind map $$\mathbf{v}(x,y)$$ |

![Vector field example]({{ site.baseurl }}/img/chapter_img/veccalc_vector_field_example_bs.jpg)

*Figure. Vector field $$\mathbf{v}(x,y)=(2x,y)$$: each point carries an arrow (source: Brain Station Advanced, grad/div/curl explainer).*

### Gradient: steepest ascent

For a scalar field $$f$$ (a “hill” of height $$f(x,y)$$),

$$
\nabla f = \Bigl(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\ldots\Bigr).
$$

**Intuition.** $$\nabla f$$ points in the direction of **fastest increase** of $$f$$ (push a ball uphill as steeply as possible). The ball rolls naturally in the direction $$-\nabla f$$ (downhill / gradient descent).  
**Example.** $$f(x,y)=x^2+y^2$$ (bowl). At $$(1,2)$$ one has $$\nabla f=(2,4)$$—in the plane of the base, the uphill push direction.

![Gradient as uphill]({{ site.baseurl }}/img/chapter_img/veccalc_gradient_uphill_bs.jpg)

*Figure. Gradient of $$f=x^2+y^2$$: steepest-ascent arrows in the plane (source: same video).*

### Divergence: sources, sinks, and incompressible flow

For a vector field $$\mathbf{v}$$,

$$
\nabla\cdot\mathbf{v} = \frac{\partial v_1}{\partial x}+\frac{\partial v_2}{\partial y}+\frac{\partial v_3}{\partial z}
$$

is a **scalar**. Imagine a tiny control square in a fluid:

| Sign of $$\nabla\cdot\mathbf{v}$$ | Fluid picture |
|-----------------------------------|---------------|
| $$>0$$ | More leaves than enters → density drops (source / spreading) |
| $$<0$$ | More enters than leaves → density rises (sink / converging) |
| $$=0$$ | In = out (rotation, or uniform stream) |

**Examples.** $$\mathbf{v}=(x,y)$$ has $$\nabla\cdot\mathbf{v}=2$$ (outward source). $$\mathbf{v}=(-x,-y)$$ has divergence $$-2$$ (sink). $$\mathbf{v}=(-y,x)$$ (pure rotation) and a constant field have divergence $$0$$.

![Divergence source]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_source_bs.jpg)

*Figure. Outward field: positive divergence (source) (source: same video).*

![Divergence sink]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_sink_bs.jpg)

*Figure. Inward field $$\mathbf{v}=(-x,-y)$$: negative divergence (sink) (source: same video).*

![Divergence zero (uniform stream)]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_uniform_bs.jpg)

*Figure. Uniform stream $$\mathbf{v}=(2,0)$$: $$\nabla\cdot\mathbf{v}=0$$ (source: same video).*

In electromagnetism, positive charge acts like a **source** of the electric field (positive divergence); negative charge like a **sink**—one Maxwell equation is built on this intuition. Combined with the **divergence theorem**, this is exactly the step that turns integral balance laws into PDEs (Section 4).

### Curl: local rotation (paddle-wheel test)

Curl is the **cross product**

$$
\nabla\times\mathbf{v},
$$

a **vector** field. Place a tiny paddle wheel in the flow: if the fluid spins the wheel, curl is nonzero; if the wheel only translates without spinning, curl is zero. The usual determinant mnemonic with unit vectors $$\mathbf{i},\mathbf{j},\mathbf{k}$$ and partial derivatives computes the components.

![Curl and paddle wheel]({{ site.baseurl }}/img/chapter_img/veccalc_curl_paddle_bs.jpg)

*Figure. Rotational field and paddle-wheel intuition for curl (source: same video).*

### Why this section sits here

| Operator | Output | Physics slogan |
|----------|--------|----------------|
| $$\nabla f$$ | vector | Steepest change of a scalar (forces from potentials; Fourier’s law uses $$-\nabla T$$) |
| $$\nabla\cdot\mathbf{v}$$ | scalar | Local source/sink strength (continuity equation, Gauss’s law) |
| $$\nabla\times\mathbf{v}$$ | vector | Local spin (vorticity; Faraday/Ampère structure in Maxwell) |

These three operators are the native language of continuum models in Section 4 and of Maxwell / fluid / heat theory throughout engineering.

---

## 6. Variational principles: calculus of extrema

Newton’s laws are not the only organizing principle. Many equilibrium problems are **variational**: the physical configuration minimizes (or makes stationary) an energy.

A classic toy model is the Dirichlet principle: among functions with fixed boundary values, the one minimizing

$$
E[u] = \frac12\int_\Omega \lvert\nabla u\rvert^2\,dx
$$

solves Laplace’s equation in $$\Omega$$ (under suitable hypotheses). Elasticity, minimal surfaces, and many finite-element methods live in this variational world: approximate the energy over a finite-dimensional subspace of shapes, then minimize.

This is why linear algebra appears so forcefully in engineering software: discretized energies produce quadratic forms $$ \frac12 U^\top K U - F^\top U $$, whose critical points solve $$KU=F$$. Calculus of variations → sparse matrices → solvers.

---

## 7. Finite elements: industrialized calculus

Hand solutions of PDEs exist for special geometries. Real devices have messy shapes, mixed materials, and time-varying loads. The **finite element method (FEM)** is the industrial answer:

1. Partition the domain into elements (triangles, tetrahedra, bricks).
2. Restrict the unknown field to a finite-dimensional space of piecewise polynomials (hat functions, etc.).
3. Enforce the weak (integral/variational) form of the PDE on that space.
4. Assemble a large sparse system $$KU=F$$ (or a nonlinear/time-dependent analogue) and solve.

**What is “weak form” in one line?** Multiply the PDE by a test function, integrate by parts, and transfer derivatives onto the test function—exactly the step that makes low-regularity solutions and piecewise-linear approximations legitimate.

**Mechanism.**  
*FEM does not abandon continuous mathematics; it projects infinite-dimensional calculus problems onto high-dimensional linear algebra that computers can attack.*

Related industrial cousins: finite difference methods (grid stencils for derivatives), finite volume methods (flux balance on control volumes—natural for conservation laws), spectral methods (global basis expansions when geometry allows).

---

## 8. Engineering domains that speak calculus

| Domain | What is differentiated / integrated |
|--------|-------------------------------------|
| Mechanical design | Stress, strain, vibration modes; ODEs/PDEs of elasticity |
| Electrical engineering | Circuit ODEs; Maxwell PDEs for fields and waves |
| Civil / structural | Beam equations, load paths, FEM for buildings and bridges |
| Aerospace | Flight dynamics (ODE); CFD for Navier–Stokes numerics |
| Chemical / thermal | Heat and mass transfer PDEs; reaction–diffusion |
| Control systems | Linearization of nonlinear ODEs; Laplace-domain design |
| Biomedical devices | Soft-tissue mechanics, diffusion, blood-flow models |

**Control** deserves a special mention. Linearizing $$\dot{x}=f(x,u)$$ about an operating point produces $$\dot{\xi}=A\xi+B\mu$$. Eigenvalues of $$A$$ and controllability of $$(A,B)$$—linear algebra on top of calculus—decide whether feedback can stabilize the plant. Autopilots, power electronics, and process control are applied multivariable calculus with an engineering mission.

---

## 9. From continuous models to digital twins

Modern engineering often couples sensors, models, and optimization:

- **Model:** ODE/PDE or reduced-order surrogate.
- **Estimate:** assimilate measurements (filters, inverse problems—again derivatives and integrals).
- **Act:** optimize inputs under constraints (link to [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/)).

A “digital twin” of a turbine or a bridge is not magic; it is calibrated calculus plus data. Uncertainty quantification asks how noise in coefficients or loads propagates to predictions—probability enters (next lectures), but the skeleton remains differential.

**Honesty about limits.** Continuous models idealize. Turbulence, contact, fracture, and multiphase flow stress both analysis and numerics. Existence, uniqueness, and stability of PDE solutions are not automatic; well-posedness is a mathematical property with engineering consequences (garbage in, garbage out—and sometimes the continuous problem itself is delicate).

---

## 10. Why calculus still matters when software “just solves it”

It is tempting to treat commercial solvers as black boxes. Understanding calculus still pays:

1. **Modeling errors** dominate discretization errors when the constitutive law is wrong.
2. **Boundary conditions** encode the physics you chose; wrong BCs produce beautiful nonsense.
3. **Nondimensionalization** reveals which terms matter (Reynolds, Mach, Fourier numbers).
4. **Stability and stiffness** of time integrators are analytic notions that explain why some simulations explode.
5. **Verification and validation** require knowing what the continuous problem *should* do.

The mechanism chain of this chapter’s theme is:

**physical balance → differential equation → analysis/numerics → design decision.**

Calculus is the middle of that chain—not a school subject left behind, but the language in which the chain is written.

---

### Vector calculus slogans (from video research)

Primary intuition video: [Brain Station — Gradient, Divergence and Curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) (~15 min), cross-checked with standard multivariable calculus.

- **Gradient:** $$\nabla f$$ is the vector of partial derivatives; it points **uphill** (steepest ascent). Physical “rolling downhill” follows $$-\nabla f$$.
- **Divergence:** $$\nabla\cdot\mathbf{v}$$ is a *scalar*. Positive ≈ source, negative ≈ sink, zero ≈ volume-preserving flow (which can still move).
- **Curl:** $$\nabla\times\mathbf{v}$$ measures local rotation (paddle-wheel test).
- Pair with 3Blue1Brown’s [Essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) for the FTC narrative before the vector operators.

## Common confusions

| Claim | Correction |
|-------|------------|
| “Calculus is only formulas for exams.” | It is the language of continuous change; physics and engineering are written in it. |
| “If the software converges, the model is correct.” | Convergence is numerical; model error and bad BCs remain. |
| “ODEs and PDEs are the same difficulty.” | PDEs are infinite-dimensional in space; theory and numerics differ sharply. |
| “FEM replaces the need for calculus.” | FEM *is* discretized variational calculus plus linear algebra. |
| “Newton’s law is $$F=ma$$ as three letters, not an equation for functions.” | The unknown is a trajectory $$x(t)$$; the law is a differential equation. |
| “More mesh refinement always fixes everything.” | It reduces discretization error; it cannot fix a wrong physical model. |
| “Gradient points downhill.” | $$\nabla f$$ points **uphill** (steepest ascent); $$-\nabla f$$ is descent. |
| “Divergence zero means the fluid is still.” | Zero divergence means no net source/sink; the fluid can still move (rotation, uniform stream). |

---

## Exercises

1. **Warm-up.** If $$s(t)=\frac12 gt^2$$, compute velocity and acceleration. Interpret each derivative physically.  
2. **FTC narrative.** In three sentences, explain why “local rate” and “accumulated change” must be linked for modeling to work.  
3. **ODE vs PDE.** Classify as ODE or PDE and name the independent variables: (a) RC circuit voltage vs time; (b) temperature in a rod vs position and time; (c) planetary position vs time.  
4. **Mechanism sentence.** Write one sentence linking Fourier’s law to the heat equation (conservation + constitutive law).  
5. **Vector calculus.** For $$f(x,y)=x^2+y^2$$ compute $$\nabla f$$ at $$(1,2)$$. For $$\mathbf{v}=(x,y)$$ and $$\mathbf{w}=(-y,x)$$ compute $$\nabla\cdot\mathbf{v}$$ and $$\nabla\cdot\mathbf{w}$$; interpret signs.  
6. **FEM sketch.** Why does integrating by parts (weak form) allow piecewise-linear approximations that are not twice classically differentiable?  
7. **Engineering audit.** Pick a device you use (phone speaker, elevator, AC). Name one quantity that is differentiated or integrated in its design model.  
8. **Stretch.** Look up the weak form of $$-u''=f$$ on $$(0,1)$$ with $$u(0)=u(1)=0$$ and derive the bilinear form $$a(u,v)=\int_0^1 u'v'\,dx$$.

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/calculus-physics-engineering/`.

**Recommended order**

1. **ORIENTATION** — 3Blue1Brown — Essence of calculus (series / ch.1 derivative): [https://www.youtube.com/watch?v=WUvTyaaNkzM](https://www.youtube.com/watch?v=WUvTyaaNkzM).
2. **ORIENTATION** — 3Blue1Brown — Essence of calculus playlist hub: [https://www.3blue1brown.com/topics/calculus](https://www.3blue1brown.com/topics/calculus).
3. **CORE** — Brain Station Advanced — Gradient, Divergence and Curl: [https://www.youtube.com/watch?v=m_Psx7CdvDk](https://www.youtube.com/watch?v=m_Psx7CdvDk).
4. **FOUNDATION** — Khan Academy / 3B1B style multivariable (divergence theorem culture): [https://www.youtube.com/watch?v=rB83DpBJQsE](https://www.youtube.com/watch?v=rB83DpBJQsE).
5. **FOUNDATION** — MIT OCW 18.02 Multivariable Calculus (course page): [https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/](https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/).
6. **FOUNDATION** — MIT OCW 18.03 Differential Equations (video lectures): [https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/).

Complete URL bibliography: `research/video-research/calculus-physics-engineering/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/calculus-physics-engineering/transcripts/` · status: `research/video-research/calculus-physics-engineering/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/calculus-physics-engineering_WUvTyaaNkzM_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/calculus-physics-engineering/references.md`.

### Videos (primary path)

1. 3Blue1Brown — Essence of calculus (series / ch.1 derivative) — https://www.youtube.com/watch?v=WUvTyaaNkzM
2. 3Blue1Brown — Essence of calculus playlist hub — https://www.3blue1brown.com/topics/calculus
3. Brain Station Advanced — Gradient, Divergence and Curl — https://www.youtube.com/watch?v=m_Psx7CdvDk
4. Khan Academy / 3B1B style multivariable (divergence theorem culture) — https://www.youtube.com/watch?v=rB83DpBJQsE
5. MIT OCW 18.02 Multivariable Calculus (course page) — https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/
6. MIT OCW 18.03 Differential Equations (video lectures) — https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/
7. Gilbert Strang & Cleve Moler — Learn Differential Equations (overview) — https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/
8. 3Blue1Brown — Divergence and curl playlist (multivariable) — https://www.3blue1brown.com/topics/multivariable-calculus

### Videos (secondary finds)

9. Numberphile / related continuum modeling culture (optional) — https://www.youtube.com/user/numberphile

### Papers, books, OCW, and web

10. Evans — Partial Differential Equations (AMS Graduate Studies): https://bookstore.ams.org/gsm-19-r
11. Wikipedia — Fundamental theorem of calculus: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
12. Wikipedia — Finite element method: https://en.wikipedia.org/wiki/Finite_element_method
13. MIT OCW 18.02: https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/
14. MIT OCW 18.03: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/

### Course

15. Course: [Overview]({{ site.baseurl }}/contents/en/chapter03/03_00_Overview/), [DEs and applications]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/), [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/), [Fourier]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/). Pack: `research/video-research/calculus-physics-engineering/`.

## Further directions

- Next in this chapter: [Linear Algebra → AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/) (the discrete partner of continuous models) and [DEs]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/) (catalog and numerics).  
- Deep pure-math sibling: existence questions for continuum mechanics in [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/).  
- Optional: watch the [grad/div/curl video](https://www.youtube.com/watch?v=m_Psx7CdvDk) once, then re-read §5.  
- Practice: nondimensionalize the heat equation and identify the single dimensionless time scale.  
- Restate the core mechanism of this essay in one paragraph; note one precise question you still have.
