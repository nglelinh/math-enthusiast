---
layout: post
title: "Symmetry, Lie Groups, and Particle Physics"
chapter: '03'
order: 11
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
---

If geometry is the language of spacetime, **symmetry** is the language of conservation laws and particle classification. Twentieth-century particle physics made a precise bet: the fundamental forces and matter multiplets are organized by **continuous groups**—especially compact Lie groups such as $$U(1)$$, $$SU(2)$$, and $$SU(3)$$—acting as **gauge symmetries** or global flavor symmetries.

This lecture maps the mathematical idea of a Lie group and its representations to the physical payoff: Noether currents, selection rules, and the Standard Model gauge group

$$
G_{\mathrm{SM}} = U(1)_Y \times SU(2)_L \times SU(3)_c
$$

at slogan level. Pair with the beauty-side essay [Symmetry]({{ site.baseurl }}/contents/en/chapter04/04_04_Symmetry/) and the force-side essay [Gauge theory as geometry]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/).

---

## Learning objectives

After this lecture you should be able to:

- Define a **Lie group** informally (group + smooth manifold; group operations smooth).
- Explain why physicists care about **representations**: particles live in representation spaces, not only in the abstract group.
- State **Noether’s principle** slogan: continuous symmetry ↔ conserved current/charge.
- Name the Standard Model factors $$U(1)$$, $$SU(2)$$, $$SU(3)$$ and what force/charge each is associated with (hypercharge/EM after mixing, weak isospin, color).
- Distinguish **global symmetry** from **gauge symmetry** at the level of “redundancy vs physical symmetry” without full BRST.
- Avoid LO6 traps: “SU(3) means three quarks and nothing else,” “symmetry means the equations look pretty,” “gauge symmetry is just a global phase.”

**Prerequisites.** Matrix multiplication; eigenvalues of Hermitian matrices; complex numbers. [Linear algebra → AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/) for matrix culture.

---

## 1. Groups, continuous families, Lie algebras

A **group** is a set with associative multiplication, identity, and inverses—symmetries you can compose. A **Lie group** is a group that is also a smooth manifold, so symmetries form continuous families: rotations $$SO(3)$$, unitary matrices $$U(n)$$, special unitary $$SU(n)$$ (determinant 1).

Near the identity, a Lie group is controlled by its **Lie algebra**: the tangent space equipped with a bracket $$[X,Y]$$ measuring non-commutativity of infinitesimal transformations. For matrix groups, the algebra consists of matrices closed under commutators (e.g. traceless anti-Hermitian matrices for $$SU(n)$$, up to physics conventions with factors of $$i$$).

**Example.** $$SU(2)$$ is the group of $$2\times 2$$ unitary matrices with determinant 1. Its Lie algebra is 3-dimensional—the same dimension as angular momentum algebra—which is why spin-$$1/2$$ and isospin doublets share mathematics.

---

## 2. Representations: where particles live

An abstract group becomes physics when it **acts on a state space**. A (linear) **representation** is a homomorphism

$$
\rho: G \to GL(V)
$$

into invertible linear maps on a vector space $$V$$ (often a Hilbert space or a finite-dimensional complex space for internal degrees of freedom).

- **Irreducible representations** are the “elementary multiplets”: you cannot split $$V$$ into smaller invariant pieces.  
- Tensor products build multi-particle or multi-quark combinations (Clebsch–Gordan / Young-diagram combinatorics).  
- Characters and highest weights classify representations for compact groups—pure mathematics that particle physics uses as a catalog.

**One-step mechanism (LO4).** Measuring a particle species often means measuring **labels of a representation** (spin, charge, color indices) that dictate interaction patterns allowed by symmetry.

---

## 3. Noether’s theorem (slogan form)

If the laws of motion are invariant under a continuous family of transformations, there is a conserved current. Time-translation symmetry ↔ energy conservation; spatial translation ↔ momentum; rotation ↔ angular momentum; global $$U(1)$$ phase symmetry of a complex field ↔ electric charge conservation (in appropriate theories).

In field theory the statement is local (continuity equation $$\partial_\mu j^\mu = 0$$). The theorem is a bridge from **geometry of symmetry** to **bookkeeping of conserved quantities**.

---

## 4. Gauge symmetry vs global symmetry

| | Global symmetry | Gauge symmetry |
|--|-----------------|----------------|
| Transformation | Same group element for all space (or rigid) | Spacetime-dependent $$g(x)$$ |
| Meaning | Physical symmetry of the system | Often a **redundancy** in description (orbits = physical configs) |
| Consequence | Conserved charges; multiplet structure | Forces as compensating fields (connections) |

Maxwell theory already has $$U(1)$$ gauge symmetry: $$A_\mu \mapsto A_\mu + \partial_\mu \lambda$$. Yang–Mills generalizes this to non-abelian $$G$$. The Standard Model combines three gauge factors with specified fermion representations (left-handed doublets, color triplets, hypercharges, …).

**Higgs mechanism (one sentence).** Spontaneous breaking of electroweak gauge symmetry gives masses to $$W^\pm$$ and $$Z$$ while leaving a massless photon—symmetry of the equations vs symmetry of the vacuum, carefully distinguished.

---

## 5. The Standard Model group as a map entry

$$
\begin{aligned}
SU(3)_c &\quad \text{strong force / color (QCD)}\\
SU(2)_L &\quad \text{weak isospin (left-handed fermions)}\\
U(1)_Y &\quad \text{hypercharge (mixes with }W^3\text{ to give EM)}
\end{aligned}
$$

Quarks transform as color triplets; leptons are color singlets; weak interactions treat left- and right-handed fields differently (chirality)—representation data, not decoration.

This is **representation theory applied at industrial scale**: once the group and representations are fixed, interaction vertices are tightly constrained.

---

## 6. Mathematics fertilized by the same ideas

- Structure theory of semisimple Lie algebras (Cartan, Killing, Dynkin diagrams).  
- Representation rings, tensor categories (later: anyons, topological phases).  
- Infinite-dimensional groups and algebras in conformal field theory and integrable systems.  
- Duality of groups $$G$$ vs $$G^\vee$$ in Langlands and in gauge dualities ([Duality principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/)).

Particle physics did not invent Lie theory, but it **selected and stressed** representation-theoretic literacy for a century of physicists—and returned problems (anomalies, quantum symmetry) to mathematics.

---

## 7. Precision versus hype (LO6)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “The universe is $$SU(3)$$.” | Oversimplified | One factor of the gauge group of known forces; not a Theory of Everything. |
| “Gauge symmetry causes forces.” | Rough | Gauge *invariance* + locality motivates connection fields; dynamics need an action (YM, etc.). |
| “All symmetries are Lie groups.” | False | Discrete symmetries (parity, charge conjugation, crystal groups) matter too. |
| “Representation = pretty picture of a particle.” | Incomplete | It is a linear action on a state space with measurable quantum numbers. |

---

## Exercises

1. **Definition.** In your own words: group vs Lie group vs Lie algebra.  
2. **$$SU(2)$$.** Why are $$2\times 2$$ unitary determinant-1 matrices a natural home for spin-1/2?  
3. **Noether.** Match: time translation, rotation, global phase ↔ energy, angular momentum, charge.  
4. **Global vs gauge.** Give one sentence each.  
5. **SM literacy.** Which factor is primarily “color”? Which is “weak isospin”?  
6. **Bridge.** How does a representation of $$G$$ become “matter fields in an associated bundle” in the gauge geometry essay? (Slogan OK.)

---

## References and further reading

1. Hall — *Lie Groups, Lie Algebras, and Representations* (math-first).  
2. Georgi — *Lie Algebras in Particle Physics* (physics-first).  
3. Course: [Symmetry]({{ site.baseurl }}/contents/en/chapter04/04_04_Symmetry/), [Gauge as geometry]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/), [Yang–Mills mass gap]({{ site.baseurl }}/contents/en/chapter01/01_10_Yang_Mills_Mass_Gap/), [Linear algebra]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/).  
