---
layout: post
title: "Maxim Kontsevich: Witten, Vassiliev, and Quantization (Fields Medal 1998)"
chapter: '02'
order: 22
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Maxim Kontsevich** received the **Fields Medal 1998** for his contributions to algebraic geometry, topology, and mathematical physics, including the proof of Witten’s conjecture of intersection numbers in moduli spaces of stable curves, construction of the universal Vassiliev invariant of knots, and formal quantization of Poisson manifolds. The medal does **not** name a single “Kontsevich theorem.” It names three completed constructions that sit in different rooms of geometry—moduli of curves, finite-type knot invariants, and deformation quantization—and that share a taste for making a physicist’s generating function into a precise algebraic or combinatorial object.

This essay is for learners who have seen a first moduli space or a first Poisson bracket and want the architecture of those three citation items. It does **not** treat homological mirror symmetry as the official 1998 one-liner (that was already the 1994 ICM proposal), nor does it treat motivic integration as the Fields slogan (a later Kontsevich idea, developed with Denef–Loeser). Those neighbors appear in a dedicated section so that credit stays honest.

---

## Learning objectives

After this lecture you should be able to:

- Recite the **three items** of the 1998 citation without collapsing them into one theorem.
- State Witten’s conjecture at slogan level: a generating function of intersection numbers on $$\overline{\mathcal{M}}_{g,n}$$ satisfies the KdV hierarchy (and the string equation).
- Describe the **Kontsevich integral** as a universal finite-type (Vassiliev) invariant of knots, built from iterated integrals along a knot.
- Explain **formal deformation quantization**: a star product on functions that deforms the pointwise product, with first-order commutator given by a Poisson bracket.
- Place homological mirror symmetry and motivic integration as **related Kontsevich programs**, not as the official Fields list.

**Prerequisites.** The idea that a moduli space parametrizes geometric objects; the Poisson bracket on functions on $$\mathbb{R}^{2n}$$ or on a symplectic manifold; the distinction between a knot and its diagram. No prior operad or $$A_\infty$$ course required.

**Seminar links.** LO1 / LO4 (hard programs; physics generating functions ↔ algebraic constructions). Pair with [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) for another moduli-of-curves culture, and with [Pardon]({{ site.baseurl }}/contents/en/chapter02/02_13_Pardon_Symplectic/) if you later meet Fukaya categories as consumers of mirror symmetry.

---

## 1. Three items, not one theorem

Popular accounts sometimes invent a phantom “Kontsevich theorem” that explains string theory, knots, and quantization in one sentence. The IMU text is more disciplined. It lists three achievements:

1. Proof of **Witten’s conjecture** on intersection numbers of tautological classes on moduli spaces of stable curves.
2. Construction of the **universal Vassiliev invariant** of knots.
3. **Formal quantization** of Poisson manifolds.

Each has its own definitions, predecessors, and later industry. What they share is a method: write a generating function or a formal series whose coefficients are geometric, then produce a combinatorial or homological machine that computes them and proves the expected identities.

**Slogan.** The 1998 medal is a **triple citation**, not a unification theorem.

---

## 2. Witten’s conjecture and moduli of curves

Let $$\overline{\mathcal{M}}_{g,n}$$ be the Deligne–Mumford compactification of the moduli space of genus-$$g$$ curves with $$n$$ marked points. On this orbifold live tautological line bundles $$\mathbb{L}_i$$ whose first Chern classes $$\psi_i=c_1(\mathbb{L}_i)$$ measure the cotangent line at the $$i$$-th mark. Intersection numbers

$$
\langle\tau_{k_1}\cdots\tau_{k_n}\rangle_g=\int_{\overline{\mathcal{M}}_{g,n}}\psi_1^{k_1}\cdots\psi_n^{k_n}
$$

package the enumerative geometry of those classes. Witten conjectured that the generating function assembled from these numbers is a tau-function of the KdV hierarchy—equivalently, that the intersections satisfy a system of recursive PDEs predicted by two-dimensional gravity.

Kontsevich proved the conjecture (Comm. Math. Phys., 1992) by replacing the moduli space, for the purposes of these intersections, with a combinatorial model: ribbon graphs (or, equivalently, Strebel differentials) whose cells compute the $$\psi$$-integrals, together with a matrix Airy integral whose asymptotic expansion reproduces the generating function. The proof is a bridge between algebraic geometry and matrix models, not a “classification of all curves.”

**Accuracy.** Witten formulated the conjecture; Kontsevich proved it. Later proofs (Okounkov–Pandharipande, Mirzakhani, and others) recast the same identities in other languages. Mirzakhani’s Weil–Petersson volumes are a neighboring moduli story, not a replacement of the 1992 paper.

---

## 3. The Kontsevich integral and Vassiliev invariants

Vassiliev’s finite-type invariants of knots vanish on diagrams with enough double points; they form a filtered algebra whose associated graded piece is described by weight systems on chord diagrams. A **universal** Vassiliev invariant is a knot invariant with values in a completed diagram algebra that specializes to every finite-type invariant once a weight system is chosen.

Kontsevich constructed such an invariant by an iterated-integral formula (the **Kontsevich integral**): one embeds the knot in space, writes a series of configuration-space integrals along pairs of points on the knot, and takes values in a chord-diagram algebra. After suitable normalization (and, in the full story, a Drinfeld associator to handle the framed or parenthesized version), the integral is universal over $$\mathbb{C}$$.

**Do not write** that Kontsevich “classified all knots.” Finite-type invariants do not separate all knots; the integral is universal for that filtered class, not a complete knot table.

---

## 4. Formal quantization of Poisson manifolds

A Poisson manifold $$(M,\pi)$$ carries a bilinear bracket $$\{\,,\,\}$$ on functions satisfying Jacobi and Leibniz. Deformation quantization asks for a star product

$$
f\star g=fg+\sum_{k\ge 1}h^k B_k(f,g)
$$

on formal power series in a parameter $$h$$ (often written $$\hbar$$), associative, with

$$
f\star g-g\star f=h\{f,g\}+O(h^2).
$$

For symplectic manifolds, Fedosov and others had constructions. Kontsevich proved that **every** Poisson manifold admits a canonical formal star product, given by an explicit sum over admissible graphs: each graph contributes a bidifferential operator whose coefficients are contractions of $$\pi$$ and its derivatives. The deeper engine is a **formality** theorem: an $$L_\infty$$ quasi-isomorphism between the differential graded Lie algebra of polyvector fields and the Hochschild cochains of the algebra of functions. Poisson structures are Maurer–Cartan elements on one side; star products are Maurer–Cartan elements on the other.

**Accuracy.** The theorem is about **formal** series in $$h$$. It does not by itself produce a $$C^*$$-algebra of a Poisson manifold, nor does it “quantize gravity.”

---

## 5. Related work that is not the 1998 one-liner

Two neighboring programs are easy to mis-file.

**Homological mirror symmetry.** Kontsevich’s 1994 ICM lecture proposed that mirror symmetry is an equivalence of categories: the derived Fukaya category of a symplectic manifold and the derived category of coherent sheaves on a mirror complex manifold. By 1998 this was already an influential conjecture and a research program. It is **not** one of the three items named in the Fields citation. Treat it as related work that later became a field of its own (see the course’s mirror-symmetry chapter).

**Motivic integration.** In a 1995 lecture Kontsevich suggested an integration theory with values in a Grothendieck ring of varieties, designed in part to prove that birational Calabi–Yau varieties have equal Hodge numbers. Denef and Loeser developed the theory systematically. It is a major Kontsevich idea; it is **not** the 1998 one-liner.

When you write a seminar paragraph, name the laboratory you mean. Do not let HMS or motives impersonate the citation.

---

## 6. Why a Fields Medal

Three interlocking reasons:

1. **Difficulty.** Each item solved or constructed something the community had named and not completed: Witten’s KdV claim, a universal finite-type invariant, a star product for arbitrary Poisson structures.
2. **Centrality.** Moduli of curves, quantum topology, and deformation theory are three highways of late-twentieth-century geometry; the citation places Kontsevich on all three.
3. **Clarity of slogan with depth of method.** “Prove Witten; write the universal Vassiliev invariant; quantize every Poisson manifold” is a list a student can remember; each proof invents a machine (ribbon graphs, configuration integrals, formality graphs).

For this course, Kontsevich sits next to other Fields portraits that complete **named programs** rather than a single numerical conjecture—and next to later portraits that consumed HMS without rewriting the 1998 citation.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “The Fields Medal was for homological mirror symmetry.” | HMS is the 1994 ICM proposal; the 1998 citation lists Witten, Vassiliev, and quantization. |
| “There is one Kontsevich theorem.” | There is a triple citation plus a large later corpus. |
| “Motivic integration is the 1998 one-liner.” | It is a later/related idea, developed especially with Denef–Loeser. |
| “The Kontsevich integral classifies knots.” | It is universal for Vassiliev invariants, not a complete classifier. |
| “Deformation quantization is a Hilbert-space representation.” | The 1998 item is a formal star product, not an analytic representation theory. |

---

## Exercises

1. Write the three 1998 citation items from memory. Check yourself against the opening paragraph.
2. What does an intersection number $$\langle\tau_{k_1}\cdots\tau_{k_n}\rangle_g$$ forget and retain about a moduli space of curves?
3. In one paragraph: why does “universal Vassiliev invariant” not mean “complete knot invariant”?
4. Write the first two terms of a star product and the commutator condition that matches a Poisson bracket.
5. **Accuracy practice.** Find a popular sentence that says Kontsevich “won the Fields Medal for mirror symmetry.” Rewrite it in two precise sentences.
6. **Seminar stretch.** Compare this triple citation with [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) on moduli of curves: one proves a Witten generating-function claim; the other measures Weil–Petersson volumes. What is shared, and what is not?

---

## Video sources and reading

1. **IMU citation** — Fields Medals 1998 (Berlin ICM): official one-liner as quoted above; see the IMU Fields Medal pages and the 1998 ICM proceedings.
2. **Primary papers** — Kontsevich, *Intersection theory on the moduli space of curves and the matrix Airy function* (1992); *Deformation quantization of Poisson manifolds* (preprint 1997; Lett. Math. Phys., 2003).
3. **Related, not the citation** — Kontsevich, *Homological algebra of mirror symmetry* (1994 ICM); Denef–Loeser on motivic integration.

**Status reminder:** Three named constructions—**not** a single theorem, and **not** “Fields for HMS.”

---

## References

1. IMU Fields Medal 1998 citation — Maxim Kontsevich (algebraic geometry, topology, mathematical physics; Witten, Vassiliev, Poisson quantization).
2. **M. Kontsevich** — Intersection theory on the moduli space of curves and the matrix Airy function (Comm. Math. Phys., 1992).
3. **M. Kontsevich** — Vassiliev’s knot invariants / the Kontsevich integral (early 1990s).
4. **M. Kontsevich** — Deformation quantization of Poisson manifolds (1997/2003).
5. Course neighbors: [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/); mirror symmetry as a later consumer of the 1994 ICM lecture, not as the 1998 list.

---

## Further directions

- Read a modern exposition of Witten’s conjecture (e.g. a survey that compares Kontsevich, Okounkov–Pandharipande, and Mirzakhani) and list which objects each proof treats as fundamental.
- Sketch, at slogan level, why formality of the Hochschild complex produces star products from Poisson bivectors.
- Seminar A3 option: one page that files HMS, motivic integration, and the 1998 citation in three drawers—without inventing a fourth “main theorem.”
