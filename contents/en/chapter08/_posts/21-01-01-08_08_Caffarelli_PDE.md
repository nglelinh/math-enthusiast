---
layout: post
title: "Luis Caffarelli: Free Boundaries and Nonlinear PDE (Abel 2023)"
chapter: '08'
order: 8
owner: Nguyen Le Linh
lang: en
categories:
- chapter08
lesson_type: required
---

**Luis A. Caffarelli** (University of Texas at Austin) received the **Abel Prize 2023**

> “for his seminal contributions to regularity theory for nonlinear partial differential equations including free-boundary problems and the Monge–Ampère equation.”  
> — [Abel Prize Committee citation](https://abelprize.no/abel-prize-laureates/2023)

This lecture explains what **regularity theory** aims to do; what a **free-boundary problem** is; why the **Monge–Ampère equation** sits at the center of fully nonlinear PDE and optimal transport; and how **Caffarelli–Kohn–Nirenberg partial regularity** for Navier–Stokes relates to—but does not solve—the Clay Millennium problem. Official materials: [abelprize.no](https://abelprize.no/).

---

## Learning objectives

After this lecture you should be able to define a free-boundary problem and give a physical example; explain regularity theory’s goal (when solutions and interfaces are smooth); locate Monge–Ampère among fully nonlinear equations; state what CKN partial regularity does and does **not** claim about Navier–Stokes; and distinguish derivation of fluid equations (e.g. kinetic bridges) from regularity of continuum NS.

**Prerequisites.** Multivariable calculus; the idea of a PDE such as Laplace’s equation $$\Delta u = 0$$. Cross-links: [Navier–Stokes Millennium]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/), [Deng PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/), [DE applications]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/).

---

## 1. Regularity theory

For linear elliptic equations with smooth coefficients, solutions are often smooth: elliptic regularity is a classical triumph. For **nonlinear** PDE, smooth data need not yield obviously smooth solutions. Singularities can form; free interfaces can develop cusps; weak solutions may exist without classical derivatives.

**Regularity theory** provides estimates and structure theorems: when solutions are $$C^\infty$$ or analytic; when free boundaries are smooth hypersurfaces; when singular sets have controlled dimension; when blow-up limits fall into a classified list of models.

Caffarelli’s career is a masterclass in that worldview applied to free boundaries, fully nonlinear equations, and fluid equations.

---

## 2. Free boundaries

### What is free?

In a fixed-boundary problem, the domain is given (solve $$\Delta u = 0$$ on a disk with boundary data). In a **free-boundary problem**, the region where a PDE holds is **unknown a priori**. The interface is part of the unknown.

Classical examples:

- **Obstacle problem:** an elastic membrane above an obstacle; the contact set’s boundary is free.  
- **Stefan problem:** melting ice; the solid–liquid interface moves and is free.  
- **Fluid interfaces:** regions occupied by different phases or fluids.

Mathematically one often studies a function $$u$$ satisfying different equations in $$\{u>0\}$$ and $$\{u=0\}$$, with transmission conditions on the free boundary $$\partial\{u>0\}$$.

### Caffarelli’s transformation of the field

Caffarelli developed **blow-up methods**, **monotonicity formulas**, and **classification techniques** that transformed free-boundary theory into a mature field with geometric conclusions. Questions shift from “does a weak solution exist?” to “how smooth is the free boundary, and what do singularities look like?”

Almost-optimal smoothness statements and classification of blow-up profiles became model cases for free-boundary programs broadly—including nonlocal and fully nonlinear variants pursued by later schools.

---

## 3. The obstacle problem as a model

The classical obstacle problem seeks the equilibrium of a membrane constrained to stay above an obstacle $$\varphi$$. Variationally, one minimizes Dirichlet energy among functions $$v\ge \varphi$$. The solution $$u$$ is harmonic (or solves a related elliptic equation) where it does not touch the obstacle, and the **coincidence set** $$\{u=\varphi\}$$ has a free boundary.

Regularity theory asks:

- How regular is $$u$$?  
- How regular is the free boundary?  
- What are possible blow-up shapes at free-boundary points?

Caffarelli’s results give deep answers in classical settings and set templates: zoom in, rescale, classify homogeneous limits, feed information back to original scale.

---

## 4. Fully nonlinear equations and Monge–Ampère

### Fully nonlinear elliptic equations

An equation is fully nonlinear when it depends nonlinearly on the Hessian $$D^2u$$, not only on $$u$$ and $$\nabla u$$. Linear elliptic theory does not apply off the shelf; one needs viscosity solutions, estimates of Krylov–Safonov type, and structural conditions (uniform ellipticity, convexity hypotheses).

### Monge–Ampère

The **Monge–Ampère equation**

$$
\det D^2 u = f(x,u,\nabla u)
$$

(in suitable form) is central in affine geometry, prescribed curvature problems, and **optimal transport** (where convex potentials satisfy Monge–Ampère-type equations relating measures). Caffarelli’s regularity theory for Monge–Ampère and related equations is a pillar of modern geometric analysis and transport.

The Abel citation names Monge–Ampère explicitly: not as a side project, but as a flagship of the nonlinear regularity program.

---

## 5. Navier–Stokes partial regularity (CKN)

With **Robert Kohn** and **Louis Nirenberg**, Caffarelli proved **partial regularity** results for suitable weak solutions of the Navier–Stokes equations: the singular set, if nonempty, is tightly constrained in space-time measure (in particular, it cannot be too large).

This is among the deepest partial results on NS regularity—and still **short of** global smoothness for all smooth initial data in 3D, which remains a [Clay Millennium Problem]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/).

### Three-axis comparison (seminar gold)

| Axis | Question | Status |
|------|----------|--------|
| Derivation / kinetic bridges | How continuum fluids relate to particle models | Active research (see [Deng]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/)) |
| CKN partial regularity | How large can singular sets of weak solutions be? | Major theorems; singular set controlled |
| Millennium openness | Are smooth 3D solutions always global and smooth? | Open |

Never collapse these three into one slogan.

---

## 6. Why Abel 2023

Nonlinear PDE regularity is infrastructure for geometry, physics, and applied analysis. Free boundaries appear in materials science and finance; Monge–Ampère in transport and geometry; NS in fluid dynamics. Caffarelli’s estimates and methods became the **language** in which much of that research speaks.

Abel honors the long program: not one equation’s lucky estimate, but a career that taught free boundaries to be smooth—or classified when they cannot.

### Blow-ups as a method (one paragraph you can reuse)

Across free-boundary theory, a standard move is: at a free-boundary point $$x_0$$, rescale

$$
u_r(x) = \frac{u(x_0 + r x)}{\text{normalization}(r)}
$$

and pass to limits as $$r\to 0$$. Limits are often homogeneous solutions of a model problem; classifying them yields information about the original free boundary’s regularity. Monotonicity formulas control the rescaling and prevent energy from oscillating wildly. Mastering this philosophy is more valuable for a first course than memorizing every theorem number—and it is exactly the philosophy Caffarelli’s school made standard.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “CKN solved Millennium NS.” | Partial regularity ≠ full regularity for all smooth data. |
| “Free boundary means boundary of the domain is free to choose for convenience.” | The interface is an **unknown** determined by the problem. |
| “Nonlinear PDE cannot have smooth solutions.” | Many do; regularity theory says when and how. |
| “Monge–Ampère is only optimal transport.” | OT is a major home; geometric PDE and affine geometry are others. |
| “Abel 2023 is only fluids.” | Free boundaries and Monge–Ampère are co-equal in the citation. |

---

## Exercises

1. Give one physical free-boundary example and identify the unknown interface.  
2. Distinguish partial regularity from full regularity in two sentences.  
3. Build a three-axis comparison: derivation (Deng) / partial regularity (CKN) / Millennium openness—one phrase each.  
4. **≤250 words:** Why is free-boundary regularity a geometric as well as analytic subject?  
5. Link to [DE applications]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/) with one applied sentence.  
6. Skim Abel 2023 materials at [abelprize.no](https://abelprize.no/) and list three keywords from the popular note.

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/caffarelli-pde/`.

**From the research pack (must-know slogans)**

- Abel 2023: regularity for nonlinear PDE — free boundaries, Monge–Ampère.
- **Caffarelli–Kohn–Nirenberg** partial regularity for Navier–Stokes ≠ Clay Millennium solution.
- Obstacle problem as flagship free-boundary model.

**Recommended order**

1. **Core** — Caffarelli Abel lecture — non-linear surface structure: [https://www.youtube.com/watch?v=dVGX6QhO8rU](https://www.youtube.com/watch?v=dVGX6QhO8rU).  
2. **History** — Abel interview Caffarelli 2023: [https://www.youtube.com/watch?v=rz3uPOIL9AA](https://www.youtube.com/watch?v=rz3uPOIL9AA).  
3. **Orientation** — Caffarelli short film: [https://www.youtube.com/watch?v=tdUBLu4fHbw](https://www.youtube.com/watch?v=tdUBLu4fHbw).  
4. **Orientation** — Reaction to Abel Prize call: [https://www.youtube.com/watch?v=ze4SKx5yBFw](https://www.youtube.com/watch?v=ze4SKx5yBFw).  

**Official / primary written hubs**

- Abel 2023 Caffarelli: https://abelprize.no/abel-prize-laureates/2023  

Complete URL bibliography: `research/video-research/caffarelli-pde/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/caffarelli-pde/transcripts/` · status: `research/video-research/caffarelli-pde/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/caffarelli-pde_dVGX6QhO8rU_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/caffarelli-pde/references.md`.

1. Abel 2023 Caffarelli — https://abelprize.no/abel-prize-laureates/2023  
2. Caffarelli Abel lecture — non-linear surface structure — https://www.youtube.com/watch?v=dVGX6QhO8rU  
3. Abel interview Caffarelli 2023 — https://www.youtube.com/watch?v=rz3uPOIL9AA  
4. Caffarelli short film — https://www.youtube.com/watch?v=tdUBLu4fHbw  
5. Reaction to Abel Prize call — https://www.youtube.com/watch?v=ze4SKx5yBFw  
6. Wikipedia — Luis Caffarelli — https://en.wikipedia.org/wiki/Luis_Caffarelli  
7. Wikipedia — Free boundary problem — https://en.wikipedia.org/wiki/Free_boundary_problem  
8. Wikipedia — Obstacle problem — https://en.wikipedia.org/wiki/Obstacle_problem  
9. Clay — Navier–Stokes (contrast partial regularity) — https://www.claymath.org/millennium/navier-stokes-equation/  
10. Abel popular PDFs (pde/obstacle/freeBoundary) — https://abelprize.no/abel-prize-laureates/2023  
11. Research pack folder: `research/video-research/caffarelli-pde/`.

1. Abel Prize 2023 — [abelprize.no/abel-prize-laureates/2023](https://abelprize.no/abel-prize-laureates/2023).  
2. Free-boundary surveys and Caffarelli’s papers on the obstacle problem; Monge–Ampère regularity literature.  
3. Caffarelli–Kohn–Nirenberg, partial regularity of suitable weak solutions of Navier–Stokes.  
4. C. Fefferman, Clay Millennium description of NS; course NS and Deng lectures.

---


## Blow-ups and universal profiles

A recurring method in free-boundary and singularity theory: **zoom in** at a candidate bad point until the picture stabilizes to a homogeneous limit problem. Classification of those limits yields regularity or identifies possible singular shapes. Caffarelli’s school made this philosophy algorithmic for free boundaries—parallel in spirit (not identical in equation) to geometric blow-ups elsewhere in geometric analysis.

## Seminar prompt

Explain, without formulas, why zooming in might turn a curved free boundary into a cone or half-space problem that is easier to classify.

## Further directions

- Engineering analogy: phase-change simulation vs theorem.  
- Seminar table: Millennium NS / CKN / free-boundary regularity.  
- Compare with a related [Fields essay]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/).  
- Note the open Millennium NS problem as a precise neighbor of CKN.  
- Next: [Michel Talagrand]({{ site.baseurl }}/contents/en/chapter08/08_09_Talagrand_Probability/).


## Free boundaries as unknown interfaces

In the classical obstacle problem, a membrane is stretched above an obstacle; the **coincidence set** where the membrane touches the obstacle has a free boundary whose regularity is not given a priori. Caffarelli’s work established fine structure theorems: free boundaries are smooth outside controlled singular sets under natural assumptions. The method mix—monotonicity formulas, blow-ups, classification of homogeneous solutions—became a template far beyond the obstacle problem.

## Partial regularity and Navier–Stokes neighbors

The Clay Millennium problem on 3D Navier–Stokes asks for global regularity (or a blow-up example) for smooth finite-energy data. Caffarelli–Kohn–Nirenberg proved **partial regularity** for suitable weak solutions: the singular set, if nonempty, has parabolic Hausdorff dimension small enough to be “rare.” That is not a solution of the Millennium problem; it is a sharp constraint on how bad singularities could be. Seminar essays should never collapse “partial regularity” into “NS is solved.”

## Monge–Ampère and fully nonlinear regularity

Caffarelli also transformed regularity theory for **Monge–Ampère** equations and related fully nonlinear elliptic equations, linking convex analysis, optimal transport geometry, and PDE estimates. When Chapter 06 discusses optimal transport, remember that regularity of transport maps often reduces to Monge–Ampère-type equations—another bridge from Abel-cited analysis to applied geometry.

## Undergrad-accessible takeaways

1. **Free boundary** = interface unknown in advance, coupled to a PDE.
2. **Blow-up** = zoom until a limiting homogeneous problem appears.
3. **Partial regularity** = smooth almost everywhere, with dimension bounds on the bad set.
4. **Prize-level analysis** often improves the *map of possible singularities*, not only existence of classical solutions.

## Seminar table (fill in class)

| Theme | Toy model | Hard cousin | What “regularity” means |
| --- | --- | --- | --- |
| Obstacle | 1D string over a bump | Higher-D free boundary | Interface smoothness |
| NS | Stokes linearization | Millennium NS | No blow-up / controlled singular set |
| MA | convex potential in 2D | Optimal transport maps | $$C^{1,\alpha}$$ / higher estimates |

## LO6 caution

Applied CFD codes “solve NS” daily with discretization and modeling. Mathematical open problems concern *exact continuum equations* under precise function-space claims. Keep engineering success and Millennium status in different columns of your essay.

