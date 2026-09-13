---
layout: post
title: "Villani’s Nonlinear Landau Damping and the Boltzmann Equation (Fields Medal 2010)"
chapter: '02'
order: 29
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Cédric Villani** received the **Fields Medal 2010**

> “For his proofs of nonlinear Landau damping and convergence to equilibrium for the Boltzmann equation.”  
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

The citation is kinetic theory, not optimal transport. Villani is also the author of two standard books on optimal transportation—*Topics in Optimal Transportation* (AMS, 2003) and *Optimal Transport: Old and New* (Springer, 2009)—and that face of his work is essential to modern analysis and geometry. It is **not** what the IMU named in 2010. This course therefore treats transport as a neighbouring language: see [Optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) and [Figalli]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/). The memoir *Théorème vivant* / *Birth of a Theorem* is a narrative of how a proof felt; it is **not** a research paper and will not be cited as one.

The 2010 medal recognizes two PDE theorems in statistical physics. **Nonlinear Landau damping** (with Clément Mouhot) is a collisionless, Vlasov-theoretic statement: a homogeneous plasma equilibrium can erase macroscopic electric oscillations without collisions, even after the linearization of Lev Landau (1946) is left behind. **Convergence to equilibrium for the Boltzmann equation** (with Laurent Desvillettes and in Villani’s hypocoercivity program) is a collisional statement: entropy production, under regularity and positivity assumptions made explicit in the papers, forces solutions toward a Maxwellian. Neither result is a complete, unconditional theory of global smooth solutions for every physically interesting collision kernel. The medal is about **rates and mechanisms** once one is already in a regular regime, and about a nonlinear damping phenomenon that physicists had trusted for decades without a complete mathematical proof.

---

## Learning objectives

After this lecture you should be able to:

- Distinguish the **Vlasov** (collisionless, mean-field) setting of Landau damping from the **Boltzmann** (collisional) setting of trend to equilibrium.
- State Landau’s 1946 discovery at slogan level: linearized, collisionless plasmas can damp electric-field oscillations.
- Credit **Mouhot–Villani** for the nonlinear theorem (analytic, and some Gevrey, regularity; potentials no rougher than Coulomb/Newton).
- Describe Boltzmann’s $$H$$-theorem as entropy production, and explain why **spatial inhomogeneity** makes trend to equilibrium much harder than the spatially homogeneous case.
- Explain **hypocoercivity** as a slogan: a degenerate dissipation that still produces a spectral gap after mixing in complementary variables.
- State Desvillettes–Villani-type convergence results as **conditional** on smoothness, decay, and positivity—not as an unconditional global regularity theory.
- Separate the 2010 IMU citation from Villani’s **optimal-transport** books and from the popular memoir *Birth of a Theorem*.

**Prerequisites.** Ordinary and partial differential equations at the level of a first serious analysis course; the idea of a probability density $$f(t,x,v)$$ on position-velocity space; entropy as a Lyapunov functional. Hamiltonian mechanics and Fourier analysis help for Landau damping but are not assumed in full.

**Seminar links.** LO1 (programs that turn physical mechanisms into estimates). Pair with [optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) and [Figalli]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/) for Villani’s other face, and with [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/) for the broader culture. Same-year neighbour: [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/).

---

## 1. Two kinetic worlds

A kinetic equation describes a gas or plasma by a density $$f(t,x,v)$$ of particles at time $$t$$, position $$x$$, and velocity $$v$$. Two extreme closures dominate the medal.

In the **Vlasov–Poisson** (or Vlasov–Maxwell) world, particles do not collide. They feel a self-consistent field $$E$$ obtained from the charge density $$\rho=\int f\,dv-1$$ (background charge normalized). The schematic equation is

$$
\partial_t f + v\cdot\nabla_x f + E[f]\cdot\nabla_v f = 0.
$$

Reversibility is obvious at the level of characteristics: there is no Boltzmann collision operator, hence no immediate $$H$$-theorem. Damping, if it occurs, must come from **phase mixing**—filaments in $$(x,v)$$ that average to a quiet spatial density—not from collisions.

In the **Boltzmann** world, particles collide. The schematic equation is

$$
\partial_t f + v\cdot\nabla_x f = Q(f,f),
$$

where $$Q$$ is a bilinear collision operator encoding a microscopic collision law (hard spheres, cutoff kernels, Coulomb-type singularities, \ldots). Boltzmann’s $$H$$-functional $$H(f)=\int f\log f$$ decreases (under suitable hypotheses), and the only equilibria are Maxwellians. The mathematical questions are existence, regularity, and **how fast** $$f(t)$$ approaches the Maxwellian compatible with the conserved mass, momentum, and energy.

Villani’s citation lives in both worlds. Mixing them in a single sentence—“he proved gases equilibrate”—erases the distinction the IMU was careful to write.

---

## 2. Landau damping: linear then nonlinear

In 1946, Lev Landau analysed the linearized Vlasov–Poisson equation around a homogeneous equilibrium $$f^0(v)$$ (for example a Maxwellian). He found that the electric field can decay exponentially in time even though the equation is reversible and collisionless. The mechanism is not dissipation in the usual $$L^2$$ sense: it is a **phase-mixing** cancellation, visible after Fourier transform in $$x$$ and a careful contour deformation in the complex velocity plane (the Landau contour). Linear Landau damping became a cornerstone of plasma physics.

Nonlinear damping is a different theorem. The nonlinear term $$E[f]\cdot\nabla_v f$$ generates echoes and resonances; for a long time it was unclear whether they would destroy the linear decay. **Clément Mouhot** and **Cédric Villani** proved that, for analytic perturbations of a stable homogeneous equilibrium (and, in an extension, for certain Gevrey classes), and for interaction potentials no more singular than Coulomb or Newton, the nonlinear Vlasov equation exhibits exponential Landau damping: the force field decays, and the density converges to a nearby homogeneous state, while the distribution function itself remains close to a free-transport evolution in suitably adapted analytic norms. The paper is Mouhot–Villani, “On Landau damping,” *Acta Mathematica* 207 (2011), 29–201, arXiv:0904.2760.

The proof reinterprets damping as a **transfer of regularity** between kinetic and spatial variables rather than as an energy loss. It uses analytic norms measured against free transport, estimates on nonlinear echoes, and a Newton scheme with a flavour the authors compare to KAM theory. **Credit Mouhot.** The result is joint; popular accounts that say “Villani proved Landau damping” are incomplete.

**What the theorem does not say.** It is not an unconditional statement for arbitrary Sobolev data, nor a classification of all possible instabilities (two-stream and related linear instabilities remain unstable). It is a nonlinear stability-and-damping theorem in high regularity.

---

## 3. Boltzmann: entropy, inhomogeneity, conditionality

For the spatially **homogeneous** Boltzmann equation (no $$x$$-dependence), entropy methods and spectral-gap estimates have a long history; Villani contributed quantitative $$H$$-theorems and work on Cercignani-type inequalities (including “Cercignani’s conjecture is sometimes true and always almost true,” *Comm. Math. Phys.* 234 (2003)). The medal citation’s “convergence to equilibrium” is aimed especially at the **spatially inhomogeneous** equation, where transport $$v\cdot\nabla_x$$ and collisions $$Q$$ interact.

Desvillettes and Villani, “On the trend to global equilibrium for spatially inhomogeneous kinetic systems: The Boltzmann equation,” *Invent. Math.* 159 (2005), 245–316, obtain rates of the form $$O(t^{-\infty})$$—faster than any polynomial—**conditionally** on strong, natural bounds: smoothness, decay at large velocities, and strict positivity. The paper is explicit that those bounds had, at the time, been established only in particular cases. Subsequent work (Guo and school; hypocoercivity estimates of many authors) has enlarged the unconditional territory, but this course will not rewrite the 2005 theorem as a complete global regularity theory for Boltzmann.

The strategy combines a quantitative $$H$$-theorem (entropy production controls distance to the local Maxwellian), a quantitative instability of the hydrodynamic description when the Knudsen number is not small (you cannot hide in a slowly evolving fluid for too long), geometric inequalities (including a Korn-type inequality from earlier Desvillettes–Villani work), and a system of differential inequalities that convert local entropy production into global decay.

---

## 4. Hypocoercivity, transport, and why a Fields Medal

**Hypocoercivity** is Villani’s name (Memoirs of the AMS, 2009) for degenerate dissipation that still yields a coercive estimate after mixing by a conservative part. Collisions may damp only in $$v$$; the bracket with transport produces $$x$$-dissipation, in the spirit of Hörmander’s sum of squares. It is not a single IMU theorem; it is the culture in which “convergence to equilibrium” became constructive rates rather than a compactness argument without a speed. The 2006 ICM lecture already advertised hypocoercive diffusion; the 2010 medal looks back on that program as it met Boltzmann and Landau.

Monge’s problem, Kantorovich couplings, and Wasserstein distances $$W_p$$ are a lingua franca that Villani taught a generation, through *Topics in Optimal Transportation* and *Optimal Transport: Old and New*; Lott–Villani (and independently Sturm) synthetic Ricci curvature is a geometric outgrowth; Figalli’s 2018 Fields sits in transport regularity. **None of that is the 2010 sentence.** The seminar habit is a fork: Fields 2010 = Mouhot–Villani damping + Desvillettes–Villani / hypocoercive Boltzmann; parallel oeuvre = transport. Read [optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) and [Figalli]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/) for the second fork.

Kinetic theory had entropy, $$H$$-theorems, and Landau’s contour, but few nonlinear theorems matching the physical slogans at the level of rates. Mouhot–Villani turned a 1946 linear calculation into a nonlinear theorem; Desvillettes–Villani made “entropy increases” quantitative for inhomogeneous gases, with assumptions written in public. The memoir *Birth of a Theorem* is literature about that collaboration. The theorem is the *Acta* paper.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “The 2010 medal is for optimal transport.” | The IMU citation is Landau damping and Boltzmann equilibration. Transport is a major separate oeuvre. |
| “Villani alone proved nonlinear Landau damping.” | The theorem is **Mouhot–Villani**. |
| “Landau already proved the nonlinear result in 1946.” | Landau’s analysis is **linear**. The nonlinear problem remained open for decades. |
| “Desvillettes–Villani give unconditional global smooth solutions of Boltzmann.” | Their rates are **conditional** on regularity, decay, and positivity assumptions stated in the paper. |
| “*Birth of a Theorem* is the paper.” | It is a memoir (French 2012, English 2015), not a research article. |
| “Landau damping uses collisions.” | It is a **collisionless** (Vlasov) phenomenon; Boltzmann is the collisional counterpart in the citation. |

---

## Exercises

1. Write four sentences that a physicist would accept: what is linearized Landau damping, and why is reversibility of Vlasov not an immediate contradiction?
2. Why does the nonlinear term threaten the linear decay? Answer at slogan level (echoes / resonances), without pretending to reconstruct the *Acta* paper.
3. State the difference between a **conditional** trend-to-equilibrium theorem and a **global regularity** theorem. Which one is Desvillettes–Villani 2005?
4. Hypocoercivity in one paragraph: degenerate dissipation + mixing $$\Rightarrow$$ decay. Give a cartoon (transport in $$x$$, collisions in $$v$$).
5. Open *Topics in Optimal Transportation* or the course chapter on [optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) and write three sentences on Monge versus Kantorovich. Then write one sentence explaining why that material is **not** the 2010 citation.
6. Credit practice: assign **Landau (1946)**, **Mouhot**, **Desvillettes**, and **Villani** each one accurate clause.
7. **Accuracy practice.** Rewrite “Villani proved that entropy always kills chaos instantly” as two sentences this course would accept.
8. **Seminar stretch.** Compare this medal with [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/): both are “statistical physics,” but one is lattice/conformal and one is kinetic/PDE. What counts as a “scaling limit” in each story?

---

## Links

- IMU Fields Medals 2010 (requested index): [mathunion.org/…/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- IMU / ICM 2010 Villani page: [Fields Medal – Cédric Villani](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-cedric-villani.html)
- Wikipedia: [Cédric Villani](https://en.wikipedia.org/wiki/C%C3%A9dric_Villani)
- arXiv: [0904.2760](https://arxiv.org/abs/0904.2760) (Mouhot–Villani); search [Desvillettes Villani Boltzmann](https://arxiv.org/search/?query=Desvillettes+Villani+Boltzmann&searchtype=all)
- Course: [Optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/), [Figalli]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/), [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/), [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/)

---

## References

1. International Mathematical Union, Fields Medals 2010 citation for Cédric Villani (IMU / ICM Hyderabad 2010 materials).
2. **C. Mouhot and C. Villani**, “On Landau damping,” *Acta Math.* 207 (2011), 29–201, arXiv:0904.2760.
3. **L. Desvillettes and C. Villani**, “On the trend to global equilibrium for spatially inhomogeneous kinetic systems: The Boltzmann equation,” *Invent. Math.* 159 (2005), 245–316.
4. **C. Villani**, *Hypocoercivity*, Mem. Amer. Math. Soc. 202 (2009), no. 950.
5. **C. Villani**, *Topics in Optimal Transportation*, Grad. Stud. Math. 58, AMS, 2003; *Optimal Transport: Old and New*, Grundlehren 338, Springer, 2009. (Context; not the Fields citation.)
6. **C. Villani**, *Théorème vivant*, Grasset, 2012; English *Birth of a Theorem*, Farrar, Straus and Giroux, 2015. (Memoir, not a research paper.)
7. Wikipedia, [Cédric Villani](https://en.wikipedia.org/wiki/C%C3%A9dric_Villani); course chapters cited above.

---

## Further directions

- Read the opening of Mouhot–Villani (phase mixing versus energy loss) before the analytic norms; compare a homogeneous $$H$$-theorem with the inhomogeneous Desvillettes–Villani scheme.
- Seminar prompt: in what regularity class would you expect nonlinear Landau damping to fail, and why is that not a contradiction with the *Acta* theorem?
