---
layout: post
title: "Operator Algebras from Quantum Theory"
chapter: '06'
order: 24
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

Finite-dimensional quantum mechanics lives in matrices. Infinite systems—quantum fields, thermodynamic limits, infinite spin chains—force a change of language: **algebras of operators** rather than a single fixed Hilbert space of “all degrees of freedom at once.” von Neumann algebras, C*-algebras, and algebraic quantum field theory grew from that pressure.

This is a **map essay** on the Physics–Math Bridge (P2): enough structure to read further, not a functional-analysis course (**LO4**, **LO6**). Pair with [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/) and [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/).

---

## Learning objectives

After this lecture you should be able to:

- Explain why **observables form an algebra** (sums, products, adjoints) beyond “list of matrices.”
- Distinguish **C*-algebra** (norm-complete, $$ \|a^*a\|=\|a\|^2 $$) from **von Neumann algebra** (weak-operator closed) at slogan level.
- State the **GNS construction** slogan: states → Hilbert space representations.
- Name one physical motivation: infinite degrees of freedom, superselection, or algebraic QFT locality.
- Avoid LO6: “operator algebras are just fancy linear algebra for the same finite qubits.”

**Prerequisites.** [Hilbert / spectral QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/); complex numbers and adjoints of matrices.

---

## 1. From matrices to abstract observables

On $$\mathbb{C}^n$$, observables are Hermitian matrices; they form a real vector space closed under polynomials, with product $$AB$$ generally noncommutative. Abstractly, a unital *-algebra packages: addition, multiplication, unit, and involution $$a\mapsto a^*$$ (adjoint).

**Physical slogan.** What you can measure and combine is primary; a Hilbert space may be a **representation** of that algebra, not the ontology.

---

## 2. C*-algebras (norm control)

A **C*-algebra** is a Banach *-algebra satisfying $$\|a^*a\|=\|a\|^2$$. Continuous functional calculus for normal elements, spectral radius formulas, and a rich representation theory follow. Examples: $$B(\mathcal{H})$$ (bounded operators), continuous functions $$C(X)$$ (commutative case—Gelfand duality: commutative C*-algebras ↔ locally compact Hausdorff spaces).

**Bridge to geometry.** Noncommutative geometry begins when one treats noncommutative C*-algebras as “function algebras of quantum spaces” ([NCG map]({{ site.baseurl }}/contents/en/chapter06/06_25_Noncommutative_Geometry_Map/)).

---

## 3. von Neumann algebras (weak closure)

A **von Neumann algebra** is a *-algebra of bounded operators on a Hilbert space closed in the weak operator topology (equivalently, equal to its double commutant $$M''=M$$). Factors (center scalars only) admit a type classification I / II / III—Murray–von Neumann, later Connes—connected historically to quantum statistics and modular theory (Tomita–Takesaki), which feeds algebraic QFT and statistical mechanics of infinite systems.

**Type I** includes $$B(\mathcal{H})$$ (ordinary QM). **Types II and III** appear naturally for infinite tensor products and local algebras of quantum fields—objects not reducible to “one big type I factor of the universe” in the naive way.

---

## 4. States, GNS, and superselection

A **state** on a C*-algebra is a positive normalized linear functional $$\omega$$. The **GNS construction** builds a Hilbert space $$\mathcal{H}_\omega$$, a representation $$\pi_\omega$$, and a cyclic vector such that $$\omega(a)=\langle \pi_\omega(a)\Omega,\Omega\rangle$$.

Different states can yield inequivalent representations—**superselection sectors** in physics language. That is a structural reason algebraic methods matter once systems are infinite.

---

## 5. Algebraic quantum field theory (slogan)

Haag–Kastler nets assign to spacetime regions algebras of local observables, with isotony, locality (spacelike commutativity), and covariance axioms. Particles and fields are reconstructed from the net rather than postulated first. Status: powerful mathematical framework; constructing interacting 4D examples with full physical content remains hard—the same open frontier as constructive QFT ([YM mass gap]({{ site.baseurl }}/contents/en/chapter01/01_10_Yang_Mills_Mass_Gap/), [path integrals]({{ site.baseurl }}/contents/en/chapter06/06_20_Path_Integrals_Math_Status/)).

---

## 6. Precision versus hype (LO6)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “All quantum theory is just matrices.” | Incomplete | Infinite systems need algebras / representations. |
| “von Neumann algebras solved QFT.” | Overstated | Deep structure theory; constructions still open. |
| “C* = noncommutative geometry finished.” | False | C* is one pillar; spectral triples etc. go further. |

---

## Exercises

1. **Algebra.** Why is the set of Hermitian matrices *not* closed under product $$AB$$, and what closure do physicists still use?  
2. **C* slogan.** What does $$\|a^*a\|=\|a\|^2$$ buy you intuitively?  
3. **GNS.** In one sentence: state → representation.  
4. **LO6.** Rewrite: “Operator algebras are philosophy, not math used in physics.”  
5. **Bridge.** How does “local algebra of observables” differ from “one global Hilbert space of the universe”?

---

## References and further reading

1. Bratteli & Robinson — *Operator Algebras and Quantum Statistical Mechanics*.  
2. Haag — *Local Quantum Physics*.  
3. Course: [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/), [NCG]({{ site.baseurl }}/contents/en/chapter06/06_25_Noncommutative_Geometry_Map/), [Math physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/).  
