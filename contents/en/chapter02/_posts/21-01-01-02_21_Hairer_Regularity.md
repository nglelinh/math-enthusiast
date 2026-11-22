---
layout: post
title: "Martin Hairer: Regularity Structures for Stochastic PDEs (Fields Medal 2014)"
chapter: '02'
order: 21
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Martin Hairer** received the **Fields Medal 2014** for his outstanding contributions to the theory of stochastic partial differential equations, and in particular for the creation of a theory of regularity structures for such equations. The medal does not name a single closed-form solution. It names a calculus: when space-time white noise is too rough for ordinary products to make sense, one expands the solution in a local Taylor series whose “monomials” are themselves stochastic, then renormalizes the illegal products so that the expansion satisfies the equation.

This essay is for learners who have seen Itô calculus in finite dimensions and want the architecture of modern singular SPDEs. It does **not** claim that Hairer solved the deterministic Navier–Stokes Millennium problem, nor that regularity structures replace every earlier approach. It explains slogans carefully: why a product of distributions can fail, what Lyons’s rough paths already fixed in one dimension, and what Hairer’s machine rearranges for equations such as KPZ and $$\Phi^4_3$$.

---

## Learning objectives

After this lecture you should be able to:

- Explain why an SPDE such as KPZ is **singular**: the noise is a space-time distribution, and nonlinear terms are not defined by naive multiplication.
- Locate **Lyons rough paths** as a precursor that restores a chain rule (or an Itô–Stratonovich choice) for controlled ordinary paths.
- Describe a **regularity structure** at slogan level: a graded set of model symbols, a model that realizes them as distributions, and a reconstruction theorem that turns a modelled distribution into an actual distribution.
- Name two landmark equations made rigorous by the theory: the Kardar–Parisi–Zhang equation, and the $$\Phi^4_3$$ dynamics.
- Distinguish Hairer–Mattingly **ergodicity of two-dimensional stochastic Navier–Stokes** from the open Millennium question about deterministic three-dimensional regularity.

**Prerequisites.** Brownian motion and Itô integrals at slogan level; the heat equation as a smoother; the idea that a distribution need not be a function. No prior White Noise or Hopf-algebra background required.

**Seminar links.** LO1 / LO4 (hard analytic programs; formal physics equations ↔ renormalized calculus). Pair with [Deng]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) for another stochastic-to-deterministic PDE culture, and with the Navier–Stokes problem in Chapter 1 only to **separate** stochastic 2D ergodicity from the Millennium statement.

---

## 1. Why ordinary PDE calculus stops

A linear stochastic heat equation

$$
\partial_t u=\Delta u+\xi
$$

can be solved by convolution against the heat kernel even when $$\xi$$ is space-time white noise, a random distribution that is not a function. The solution $$u$$ is typically Hölder in space-time, but with a low exponent. As soon as the equation becomes nonlinear—KPZ,

$$
\partial_t h=\partial_{xx}h+(\partial_x h)^2+\xi,
$$

or the dynamical $$\Phi^4_3$$ equation on a three-dimensional torus—one must multiply objects whose regularities add to a negative number. In the language of distributions, that product is not defined. Physicists subtract infinities (renormalization) and obtain finite predictions; mathematicians need a space in which those subtractions are theorems.

**Slogan.** The difficulty is not “PDEs with randomness.” It is **multiplication of objects that are not functions**.

---

## 2. History of the idea: Lyons, then Hairer

Terry Lyons’s **rough path** theory (1990s) solved a one-parameter analogue. An ordinary differential equation driven by a non-smooth path $$X$$ cannot be interpreted from $$X$$ alone if $$X$$ is as rough as Brownian motion; one must also prescribe iterated integrals, a “lift” of $$X$$. Once the lift exists, controlled paths have a robust integral and a continuity theorem: nearby lifts give nearby solutions. Gubinelli’s controlled rough paths and related paracontrolled calculus (Gubinelli–Imkeller–Perkowski) later treated some SPDEs by similar bookkeeping.

Hairer’s **regularity structures** (Invent. Math., 2014) extend the idea from paths indexed by time to distributions indexed by space-time. One builds an abstract graded algebra of symbols (decorated trees encoding iterated integrals against the noise), a **model** that realizes each symbol as a concrete distribution, and a notion of **modelled distribution**—a function that looks, at every point, like a finite linear combination of those symbols, with coefficients that vary regularly enough. A reconstruction theorem produces an actual distribution. Renormalization becomes a systematic change of model, subtracting divergent constants (or, in later algebraic work with Bruned, Hairer, and Zambotti, organizing those constants by Hopf-algebraic coproducts).

The 2014 citation singles out this creation. Earlier Hairer papers—most famously the 2013 solution of the KPZ equation (Ann. of Math.)—already showed that a renormalized equation can be given a unique meaning; regularity structures turned the method into a portable machine.

---

## 3. What a regularity structure rearranges

Consider the slogan form of the program:

> Write the solution locally as a finite jet in a basis built from the noise; solve a fixed-point problem for the jet coefficients; reconstruct; renormalize so that the fixed point remains finite as the ultraviolet cutoff is removed.

What this rearranges is the list of equations that are **well posed** as continuum objects. Before regularity structures, many singular SPDEs were either interpreted only after extra smoothing, or treated by model-specific tricks. Afterward, a large class—including KPZ, the parabolic Anderson model in low dimension, and $$\Phi^4_3$$—falls under one analytic–algebraic roof.

**$$\Phi^4_3$$** is the stochastic quantization of the three-dimensional Euclidean $$\varphi^4$$ measure: a reaction–diffusion equation with a cubic term and space-time white noise. Making the dynamics well posed supplies a dynamical construction of a measure that constructive field theory had studied by other means. It is **not** a construction of a nontrivial four-dimensional interacting scalar field; compare the four-dimensional triviality theorems in the [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase/) portrait.

---

## 4. Hairer–Mattingly: ergodicity, not the Millennium problem

A different, earlier collaboration deserves a clean box so that popular accounts do not fuse it with Clay’s Navier–Stokes problem. Hairer and Mattingly (Ann. of Math., 2006) proved uniqueness of the invariant measure for the **two-dimensional incompressible Navier–Stokes equations with degenerate stochastic forcing**: noise is injected in only finitely many Fourier modes, yet hypoellipticity and a Lyapunov structure propagate randomness through the system, yielding ergodicity.

That theorem is about **statistical uniqueness for a stochastic 2D fluid**. The Millennium problem asks whether **deterministic** 3D Navier–Stokes solutions remain smooth for all time, or whether a critical norm can blow up. Hairer’s Fields citation is about SPDEs and regularity structures. Do not write that he “solved Navier–Stokes.”

---

## 5. Honest attribution

Regularity structures sit in a network:

| Laboratory | Credit to keep in view |
|------------|------------------------|
| Rough paths | Lyons; later Friz–Victoir, Gubinelli |
| Paracontrolled calculus | Gubinelli–Imkeller–Perkowski (a parallel route for some equations) |
| KPZ as physics | Kardar, Parisi, Zhang; Bertini–Giacomin; Quastel and many others on the KPZ universality class |
| Algebraic renormalization | Bruned–Hairer–Zambotti and subsequent work |
| Stochastic 2D NSE | Hairer–Mattingly; Flandoli, Da Prato–Zabczyk for the broader SPDE setting |

**Do not write** “Hairer invented stochastic PDEs.” Da Prato, Zabczyk, Walsh, and others already had a linear and semilinear theory. Hairer made a class of **subcritical singular** equations into a theory.

---

## 6. Why a Fields Medal

Three interlocking reasons:

1. **Difficulty.** Defining products such as $$(\partial_x h)^2$$ when $$\partial_x h$$ is a distribution required a new local calculus, not a clever choice of function space inside the classical scale.
2. **Centrality.** Once the machine exists, a list of physically famous equations becomes mathematics rather than formal series.
3. **Clarity of slogan with depth of method.** “Expand, reconstruct, renormalize” is a sentence a graduate student can remember; the analytic estimates and the algebraic renormalization are a decade of work.

For this course, Hairer sits next to other Fields stories that create **languages**—perfectoid spaces, SLE, regularity structures—rather than settle a single numerical conjecture.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Hairer solved Navier–Stokes.” | He did not solve the deterministic 3D Millennium problem. Hairer–Mattingly is 2D stochastic ergodicity. |
| “Regularity structures replace Itô calculus.” | Finite-dimensional Itô theory remains the baseline; regularity structures treat singular space-time products. |
| “KPZ was undefined until 2014.” | Hairer’s KPZ paper is 2013; regularity structures (2014) generalize the method. Cole–Hopf solutions existed in one dimension under restrictions. |
| “$$\Phi^4_3$$ is the same as 4D triviality.” | $$\Phi^4_3$$ is a 3D dynamical/constructive theory; 4D Euclidean $$\varphi^4$$ triviality is a different theorem. |
| “Rough paths already solved all SPDEs.” | Rough paths handle rough drivers in time; space-time singular products need a larger machine. |

---

## Exercises

1. In your own words: why is the product of two distributions not always defined? Give a Hölder-exponent slogan.
2. What does a rough-path **lift** add to a path $$X$$, and why might Brownian motion need one?
3. Write the KPZ equation in one line and mark the term that is not classically defined.
4. Distinguish “well-posed SPDE” from “the deterministic NSE Millennium problem” in a short paragraph.
5. **Accuracy practice.** Find a popular sentence that says Hairer “tamed all noisy equations.” Rewrite it in two precise sentences.
6. **Seminar stretch.** Compare regularity structures with [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase/) on $$\varphi^4$$: one constructs a 3D dynamics; one proves 4D scaling limits are Gaussian. How do the slogans fit together without contradiction?

---

## Video sources and reading

1. **IMU citation** — Fields Medallists 2014 brief citations: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014/fields-medallists-2014-awardees-brief-citations).
2. **Orientation** — Quanta profile: [In Noisy Equations, One Who Heard Music](https://www.quantamagazine.org/in-noisy-equations-one-who-heard-music-20140812/).
3. **Meta** — IMU Fields Medal 2014 page: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014).

**Status reminder:** A theory of singular SPDEs—**not** a solution of deterministic 3D Navier–Stokes.

---

## References

1. IMU Fields Medal 2014 citation — Martin Hairer (mathunion.org).
2. **M. Hairer** — A theory of regularity structures (Invent. Math., 2014); Solving the KPZ equation (Ann. of Math., 2013).
3. **T. Lyons** — rough path theory (1990s); surveys by Friz–Hairer.
4. **M. Hairer and J. C. Mattingly** — Ergodicity of the 2D Navier–Stokes equations with degenerate stochastic forcing (Ann. of Math., 2006).
5. Course neighbors: [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase/) for $$\varphi^4$$ in another dimension; Chapter 1 Navier–Stokes for the Millennium statement one must **not** conflate.

---

## Further directions

- Read the first sections of Hairer’s regularity-structure paper and list the objects: model, modelled distribution, reconstruction.
- Compare Cole–Hopf for one-dimensional KPZ with the regularity-structure construction: what does each method see?
- Seminar A3 option: one page on paracontrolled calculus versus regularity structures—without declaring one obsolete.
