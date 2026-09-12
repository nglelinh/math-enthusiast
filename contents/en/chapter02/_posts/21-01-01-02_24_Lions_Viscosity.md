---
layout: post
title: "Pierre-Louis Lions: Viscosity Solutions and Nonlinear PDE (Fields Medal 1994)"
chapter: '02'
order: 24
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Pierre-Louis Lions** received the **Fields Medal 1994** for a body of work in nonlinear partial differential equations whose problems, as S. R. S. Varadhan stressed in the Zürich ICM lecture, “have always been motivated by applications.” The IMU page quotes that emphasis rather than a single closed-form theorem. The portable idea that a first course can actually *use* is the **viscosity solution** of a Hamilton–Jacobi equation: a notion of weak solution built from test functions that touch the graph from one side, designed so that uniqueness and stability survive after classical derivatives disappear.

This essay is for learners who have seen a first-order PDE and a minimization problem and want the architecture of late-twentieth-century nonlinear analysis. It does **not** present **mean field games** (Lasry–Lions, about 2006–07) as the 1994 citation—those are a later direction. It explains slogans carefully: viscosity inequalities, concentration-compactness, DiPerna–Lions kinetic theory, and what a Fields-level weak-solution theory rearranges.

---

## Learning objectives

After this lecture you should be able to:

- State the **viscosity** definition of a solution to a Hamilton–Jacobi equation in one careful paragraph (test functions, one-sided touching, inequality on $$H$$).
- Explain why a classical $$C^1$$ solution may fail to exist globally even when the equation is simple, and why vanishing-viscosity approximations suggest the name.
- Describe **concentration-compactness** as a trichotomy for minimizing sequences that lose compactness (vanish, split, or compactify after translation).
- Locate **DiPerna–Lions** as a large-data theory of the Boltzmann equation, not as a numerical fluid code.
- Keep the 1994 medal and the later Lasry–Lions mean-field-game program on **separate timelines**.

**Prerequisites.** Multivariable calculus; the idea of a PDE as an evolution or a stationary balance; Lipschitz functions and the method of characteristics at slogan level. No prior viscosity-solution course required.

**Seminar links.** LO1 / LO4 (hard analytic programs; applications as a source of theorems). Pair with [Deng / kinetic limits]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) for a later Boltzmann chapter, [Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/) for regularity of free boundaries, and [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/) only as a neighboring continuum question—not as a problem Lions closed.

---

## 1. Why first-order nonlinear equations need a new notion of solution

The Hamilton–Jacobi equation

$$
u_t + H(x,Du)=0
$$

arises from optimal control, geometric optics, and front propagation. The method of characteristics produces a smooth solution only until characteristics cross. After that, a Lipschitz function may still describe a value function or a propagating front, but $$Du$$ fails to exist on a crease, and a naive distributional interpretation of a fully nonlinear equation is often too weak to restore uniqueness.

Crandall and Lions (1983) proposed **viscosity solutions**. Suppose a smooth test function $$\varphi$$ touches $$u$$ from above at a point. Then the derivatives of $$\varphi$$ are eligible stand-ins for those of $$u$$, and the Hamiltonian inequality is required of $$\varphi$$:

$$
\varphi_t + H(x,D\varphi)\le 0
$$

at the contact point (subsolution). Touching from below reverses the inequality (supersolution). A viscosity solution is both. The later **Crandall–Ishii–Lions user’s guide** (Bulletin of the AMS, 1992) extended the language to fully nonlinear second-order degenerate elliptic equations and became the field’s instruction manual.

The name is not marketing. If one adds $$\varepsilon\Delta u$$ and lets $$\varepsilon\to 0$$, the limit of the parabolic approximations—when it exists—satisfies the viscosity inequalities. The definition, however, does not mention $$\varepsilon$$: it is intrinsic.

**Slogan.** When the graph is touched by a smooth test function, the PDE is tested on the test function.

---

## 2. What uniqueness rearranges

Once the definition is in place, the deep theorems are comparison and stability. If $$u$$ is a subsolution and $$v$$ a supersolution, and if they are ordered on the boundary or at infinity in a precise way, then $$u\le v$$. Uniqueness of the initial-value problem follows. Stability under uniform limits means that viscosity solutions are the right class for numerical schemes and for passing to the limit in approximations.

This rearranges the emotional geography of first-order PDE. Before viscosity theory, one often stopped when characteristics crossed, or one patched entropy conditions by hand in special conservation laws. Afterward, a large class of Hamilton–Jacobi and degenerate elliptic equations has a canonical weak solution that is unique, stable, and still tied to the control or geometric interpretation that motivated the equation.

**Accuracy.** Viscosity theory does not make every nonlinear PDE well posed. Conservation laws have their own entropy solutions; dispersive and fluid equations live in other laboratories. The medal recognizes a method family, not a claim that “nonlinear PDE is solved.”

---

## 3. Concentration-compactness

A second Lions machine addresses **loss of compactness** in the calculus of variations. On $$\mathbb{R}^n$$, a minimizing sequence for a functional with a critical Sobolev embedding may escape to infinity, split into widely separated “bubbles,” or—after a translation—remain compact. Lions’s **concentration-compactness** principle organizes these alternatives and converts them into existence theorems: if vanishing and splitting can be ruled out by energy or mass identities, a minimizer appears.

The principle is not a single equation. It is a way of reading minimizing sequences in problems motivated by mathematical physics—standing waves, prescribed curvature, and other variational PDEs—where the domain is noncompact or the embedding is critical.

---

## 4. DiPerna–Lions and kinetic equations

The Boltzmann equation tracks a density of particles in position–velocity space, with a collision operator. Global weak solutions for large data were a notorious obstruction. DiPerna and Lions constructed **renormalized solutions** (1989), giving the first robust large-data existence theory for the Boltzmann equation in a physically meaningful class.

This is the right ancestor to keep in view when this course later discusses [Deng’s kinetic limits]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/). Deng’s program asks when a particle or wave system *derives* a kinetic equation. DiPerna–Lions asked how to solve that kinetic equation once it is written. The questions are cousins, not the same theorem.

---

## 5. What the 1994 medal is not

**Mean field games**, developed by Lasry and Lions around 2006–07, describe equilibria of many rational agents coupled through a mean field. They use Hamilton–Jacobi and Fokker–Planck equations in a beautiful loop, and they are a major later chapter of Lions’s career. They are **not** why the 1994 committee met in Zürich. A seminar paragraph that opens with “Lions won the Fields Medal for mean field games” has the timeline backwards.

Varadhan’s ICM text presents a portfolio: nonlinear PDE motivated by applications, viscosity solutions, variational and kinetic work. Keep the portfolio, and date each piece.

---

## 6. Why a Fields Medal

Three interlocking reasons:

1. **Difficulty.** Fully nonlinear equations defeat many distributional theories; inventing a weak notion that still has uniqueness is rare.
2. **Centrality.** Hamilton–Jacobi equations sit under control theory, front propagation, and large parts of modern nonlinear elliptic theory.
3. **Clarity of slogan with depth of method.** “Test the PDE on functions that touch the graph” is a sentence a graduate student can remember; the comparison proofs and the user’s guide are monuments of analysis.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Viscosity solution means the equation has extra viscosity.” | The name recalls an approximation; the definition is an intrinsic test-function inequality. |
| “Lions won Fields for mean field games.” | Mean field games are a later (c. 2006–07) direction; the 1994 medal is about earlier nonlinear PDE. |
| “A viscosity solution is always smooth.” | The point is to allow kinks; regularity is a separate question. |
| “DiPerna–Lions solves Navier–Stokes.” | It is a Boltzmann / kinetic existence theory, not the Millennium regularity problem. |
| “Concentration-compactness is a compactness theorem like Rellich.” | It is a dichotomy (or trichotomy) that *analyzes* failure of compactness. |

---

## Exercises

1. In your own words: what does the viscosity definition **forget** and **retain** about a classical solution of $$u_t+H(Du)=0$$?
2. Why do crossing characteristics suggest that a globally defined $$C^1$$ solution may be the wrong class?
3. Write the subsolution inequality when a test function touches $$u$$ from above. Then write the supersolution inequality.
4. Give a slogan-level trichotomy for concentration-compactness (vanish / split / compactify).
5. **Accuracy practice.** Find a popular sentence that dates mean field games to the 1994 medal. Rewrite it in two precise sentences.
6. **Seminar stretch.** Compare DiPerna–Lions (solve Boltzmann) with [Deng]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) (derive Boltzmann). What question is each answering?

---

## Video sources and reading

1. **IMU citation** — Fields Medals 1994, Pierre-Louis Lions (Varadhan, ICM Proc. 1994): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994).
2. **User’s guide** — M. G. Crandall, H. Ishii, P.-L. Lions, *User’s guide to viscosity solutions of second order partial differential equations*, Bull. Amer. Math. Soc. **27** (1992).
3. **Orientation** — S. R. S. Varadhan, *The work of Pierre-Louis Lions*, ICM Zürich 1994 Proceedings.

**Status reminder:** Viscosity solutions, concentration-compactness, and kinetic existence—**not** mean field games as the medal citation, and not a resolution of Navier–Stokes regularity.

---

## References

1. IMU Fields Medal 1994 — Pierre-Louis Lions; S. R. S. Varadhan, ICM Proceedings, Zürich 1994.
2. **M. G. Crandall and P.-L. Lions**, Viscosity solutions of Hamilton–Jacobi equations (1983).
3. **M. G. Crandall, H. Ishii, P.-L. Lions**, User’s guide (Bull. AMS, 1992).
4. **P.-L. Lions**, concentration-compactness papers (1980s); **R. J. DiPerna and P.-L. Lions** on the Boltzmann equation (1989).
5. Course neighbors: [Deng]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/), [Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/).

---

## Further directions

- Work one comparison-principle exercise from the user’s guide at the level of a first reading.
- Compare viscosity solutions with entropy solutions of scalar conservation laws: cousins, not identical theories.
- Seminar A3 option: one page dating Lions’s later mean-field-game work honestly as a post-Fields chapter—without rewriting 1994.
