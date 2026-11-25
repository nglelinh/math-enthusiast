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

In finite-dimensional quantum mechanics—one particle or a handful of qubits—everything fits snugly inside a single Hilbert space $$\mathcal{H}$$; the Stone–von Neumann theorem even guarantees that for finitely many degrees of freedom, every representation of the canonical commutation relations is equivalent. Yet the moment you step into an **infinite crystal of $$10^{23}$$ spins** or a **quantum field** stretching across spacetime, that uniqueness shatters! Infinitely many *inequivalent* Hilbert spaces emerge for different physical phases (spin-up ferromagnet vs. spin-down, or different temperatures). Faced with this, John von Neumann, Francis Murray, Israel Gelfand, and Mark Naimark inverted the foundation: **start with the algebra of observables (operator algebras)**, and let the Hilbert space appear afterward as a *representation* determined by the physical state you inhabit.

This is a **map essay** on the Physics–Math Bridge: enough structure to read deeper literature without needing a full course in functional analysis. Pair with [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/) and [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/).

---

## Key ideas: What Three Pillars Define Operator Algebras?

As an undergraduate, you already know $$M_n(\mathbb{C})$$—square $$n \times n$$ matrices with addition, noncommutative multiplication, conjugate transpose $$A \mapsto A^*$$, and operator norm $$\|A\|$$. **Operator algebra theory** extends matrix analysis to infinite dimensions along three pillars:

### 1. C*-Algebras = "Noncommutative Topology"
A C*-algebra is a complete normed *-algebra satisfying the golden **C*-identity** $$\|a^*a\| = \|a\|^2$$. When commutative, it is always $$C_0(X)$$ (continuous functions on a topological space $$X$$). When noncommutative, it provides the abstract home for quantum observables before picking any particular Hilbert space.

### 2. von Neumann Algebras = "Noncommutative Measure Theory"
Closed in the weaker operator topology (equivalently $$M'' = M$$), a von Neumann algebra is rich in **orthogonal projections** ("yes/no" quantum measurements). The Murray–von Neumann–Connes classification of factors into **Types I, II, and III** uncovered genuinely infinite-dimensional worlds: "continuous dimensions" (Type II, where the Jones knot polynomial was born!) and algebras with no finite trace at all (Type III, which govern local spacetime regions in quantum field theory and modern black-hole entropy studies).

### 3. The GNS Construction and Algebraic QFT
Rather than fixing one Hilbert space up front, the **GNS construction** builds a tailor-made Hilbert space $$\mathcal{H}_\omega$$ directly from any expectation-value functional (state) $$\omega$$—naturally explaining distinct thermodynamic phases and superselection sectors within a single observable algebra.

---

## Learning objectives

After this lecture you should be able to:

- Explain why **observables form an algebra** (sums, products, adjoints) beyond “list of matrices.”
- Distinguish **C*-algebra** (norm-complete, $$\|a^*a\|=\|a\|^2$$) from **von Neumann algebra** (weak-operator closed) at slogan level.
- State the **GNS construction** slogan: states → Hilbert space representations.
- Name one physical motivation: infinite degrees of freedom, superselection, or algebraic QFT locality.
- Avoid the misconception that “operator algebras are just fancy linear algebra for the same finite qubits.”

**Prerequisites.** [Hilbert / spectral QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/); complex numbers and adjoints of matrices.

---

## 1. From matrices to abstract observables

On $$\mathbb{C}^n$$, observables are Hermitian matrices; they form a real vector space closed under polynomials, though the product $$AB$$ of two Hermitian matrices is no longer Hermitian when $$AB \neq BA$$—so we work inside the full complex *-algebra $$M_n(\mathbb{C})$$ containing them. Abstractly, a unital *-algebra packages addition, multiplication, unit, and involution $$a\mapsto a^*$$ (adjoint).

**Physical slogan.** What you can measure and combine is primary; a Hilbert space is a **representation** of that algebra, not a single pre-ordained container for every phase.

---

## 2. C*-algebras (norm control)

A **C*-algebra** is a Banach *-algebra satisfying $$\|a^*a\|=\|a\|^2$$. That single identity locks analysis to algebra (if a C*-norm exists, it is unique!). Continuous functional calculus for normal elements, spectral radius formulas, and a rich representation theory follow. Examples: $$B(\mathcal{H})$$ (bounded operators), and continuous functions $$C_0(X)$$ (commutative case—Gelfand–Naimark duality: commutative C*-algebras ↔ locally compact Hausdorff spaces).

**Bridge to geometry.** Noncommutative geometry begins when one treats noncommutative C*-algebras as “function algebras of quantum spaces” ([NCG map]({{ site.baseurl }}/contents/en/chapter06/06_25_Noncommutative_Geometry_Map/)).

---

## 3. von Neumann algebras (weak closure)

A **von Neumann algebra** is a *-algebra of bounded operators on a Hilbert space closed in the weak operator topology (equivalently, equal to its double commutant $$M''=M$$). Factors (algebras whose center consists only of scalars) admit the celebrated type classification I / II / III—pioneered by Murray–von Neumann and deepened by Alain Connes—connected to quantum statistics and Tomita–Takesaki modular theory, which feeds algebraic QFT and statistical mechanics of infinite systems.

**Type I** includes $$B(\mathcal{H})$$ (ordinary QM). **Types II and III** appear naturally for infinite tensor products and local algebras of quantum fields—objects not reducible to “one big type I factor of the universe” in any naïve way.

---

## 4. States, GNS, and superselection

A **state** on a C*-algebra $$\mathcal{A}$$ is a positive normalized linear functional $$\omega$$ ($$\omega(a^*a)\ge 0,\ \omega(1)=1$$)—simply the expectation value of every observable $$a$$. The **GNS construction** builds a Hilbert space $$\mathcal{H}_\omega$$, a representation $$\pi_\omega$$, and a cyclic vector $$\Omega$$ such that $$\omega(a)=\langle \pi_\omega(a)\Omega,\Omega\rangle$$.

### Explanation: Running the GNS Construction by Hand on $$M_2(\mathbb{C})$$

GNS sounds abstract, yet on $$2 \times 2$$ matrices $$\mathcal{A} = M_2(\mathbb{C})$$ you can execute every single step by hand in four lines:

1. **Pick a pure state $$\omega_1$$:** For $$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$, define $$\omega_1(A) = a$$ (the top-left entry). Check immediately: $$\omega_1(I) = 1$$ and $$\omega_1(A^*A) = |a|^2 + |c|^2 \ge 0$$.
2. **Form the inner product and find the zero-length null space $$\mathcal{N}_{\omega_1}$$:** Set $$\langle A, B \rangle_{\omega_1} = \omega_1(A^*B) = \overline{a_1}a_2 + \overline{c_1}c_2$$—simply the standard inner product of the **first columns** of $$A$$ and $$B$$! Matrices of "length zero" satisfy $$|a|^2 + |c|^2 = 0$$, i.e., all matrices $$\begin{pmatrix} 0 & b \\ 0 & d \end{pmatrix}$$ with vanishing first column.
3. **Quotient out the null space to get $$\mathcal{H}_{\omega_1} = \mathcal{A}/\mathcal{N}_{\omega_1}$$:** Two matrices lie in the same equivalence class iff they share the same first column, so $$\mathcal{H}_{\omega_1} \cong \mathbb{C}^2$$ with cyclic vector $$\Omega = [I] = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$! Left multiplication $$\pi_{\omega_1}(A)[B] = [AB]$$ acts by multiplying $$A$$ onto the first column, and
   $$
   \langle \Omega, \pi_{\omega_1}(A)\Omega \rangle = \begin{pmatrix} 1 & 0 \end{pmatrix}\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = a = \omega_1(A)!
   $$
4. **Now switch to the mixed trace state $$\omega_{\mathrm{tr}}(A) = \frac{1}{2}\operatorname{tr}(A) = \frac{a+d}{2}$$:** Here $$\omega_{\mathrm{tr}}(A^*A) = \frac{1}{2}(|a|^2+|b|^2+|c|^2+|d|^2) = 0 \iff A = 0$$! The null space is trivial, so the GNS Hilbert space has **4 dimensions** ($$\mathcal{H}_{\omega_{\mathrm{tr}}} \cong \mathbb{C}^4$$)—completely different from $$\mathbb{C}^2$$!

In infinite dimensions, the exact same mechanism splits an infinite spin chain's "all-up" state $$\omega_\uparrow$$ and "all-down" state $$\omega_\downarrow$$ into **unitarily inequivalent Hilbert spaces**—**superselection sectors** in physics language, explaining both spontaneous symmetry breaking and exact charge conservation.

---

## 5. Algebraic quantum field theory (slogan)

Haag–Kastler nets assign to spacetime regions algebras of local observables, with isotony, locality (spacelike commutativity), and covariance axioms. Particles and fields are reconstructed from the net rather than postulated first. Status: powerful mathematical framework; constructing interacting 4D examples with full physical content remains hard—the same open frontier as constructive QFT ([YM mass gap]({{ site.baseurl }}/contents/en/chapter01/01_10_Yang_Mills_Mass_Gap/), [path integrals]({{ site.baseurl }}/contents/en/chapter06/06_20_Path_Integrals_Math_Status/)).

---

## 6. Precision versus hype

| Claim | Verdict | Correction |
|-------|---------|------------|
| “All quantum theory is just matrices.” | Incomplete | Infinite systems need algebras / representations. |
| “von Neumann algebras solved QFT.” | Overstated | Deep structure theory; constructions still open. |
| “C* = noncommutative geometry finished.” | False | C* is one pillar; spectral triples etc. go further. |

---

## References and further reading

1. Bratteli & Robinson — *Operator Algebras and Quantum Statistical Mechanics*.  
2. Haag — *Local Quantum Physics*.  
3. Course: [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/), [NCG]({{ site.baseurl }}/contents/en/chapter06/06_25_Noncommutative_Geometry_Map/), [Math physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/).  
