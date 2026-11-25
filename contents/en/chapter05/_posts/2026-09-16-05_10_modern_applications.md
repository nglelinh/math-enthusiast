---
layout: post
title: "Modern Applications: Proof Ideas in Computing"
chapter: '05'
order: 10
owner: Nguyen Le Linh
lang: en
categories:
- chapter05
lesson_type: optional
---

In December 2020, Fields medalist **Peter Scholze** posted an unusually candid blog entry: he and Dustin Clausen had just proved a foundational theorem in condensed mathematics, packed with dozens of pages of delicate homological algebra—so intricate that even Scholze was not 100% certain a subtle slip wasn’t hiding somewhere. He issued a public challenge—the **Liquid Tensor Experiment**: *could a computer formally verify a brand-new theorem at the frontier of research mathematics?*

Eighteen months later, the **Lean** community answered with a solid green checkmark. Two years after that (2024), neuro-symbolic AI systems like **AlphaGeometry** and **AlphaProof** began discovering Olympiad proofs of their own and handing them straight to Lean’s kernel for audit. The arc from Euclid, Cantor, Gödel, and the Four Color Theorem has entered a new chapter: proofs are no longer just chalk on a board, but **axiom-checked computer programs**.

**Lesson roadmap:** Key ideas (formal proofs & Curry–Howard, category theory, the de Bruijn criterion) → Explanation: reading a real Lean 4 proof and hand-checking a category → Three 2022–2026 landmarks (Liquid Tensor Experiment, AlphaGeometry, AlphaProof) → Living alongside Gödel’s limits.

---

## Learning objectives

After this optional note you should be able to describe three 2022–2026 computing systems that take Chapter 5’s craft—make a claim machine-checkable—into Lean and neuro-symbolic search, while still honoring Gödel: a verified kernel does not yield a complete theory of all arithmetic truths.

---

## Key ideas: Formal Proofs, Type Theory, and Category Theory

News stories about Lean, the Liquid Tensor Experiment, and AlphaProof throw around intimidating terms. Here is the clean university-level intuition behind all three pillars:

### 1. Formal Proofs and Type Theory (The Curry–Howard Correspondence)
In ordinary programming, a function takes an `Int` and returns a `Bool`, and the compiler rejects type mismatches. Through the **Curry–Howard correspondence**, proof assistants like **Lean** and **Coq** unify mathematics with dependent type theory:
- Every **mathematical proposition $$T$$** is a **Type**.
- A **proof** of $$T$$ is a **program / term** inhabiting type $$T$$!
If your argument contains even the tiniest logical gap, the program simply **fails to type-check**.

### 2. Category Theory — The Mathematics of Structures and Arrows
Where undergraduate algebra studies individual structures (groups, rings, vector spaces), **category theory** zooms out one level to study **structures and the arrows (morphisms) between them**. A category consists of *objects*, *arrows* between objects, associative *composition*, and *identity* arrows. Structure-preserving bridges between two categories are called **functors** (for example, mapping a topological space to its fundamental group $$\pi_1$$ is a functor from Topology to Algebra!). That categorical language (abelian categories, $$\mathrm{Ext}$$ cohomology groups) is the exact infrastructure the Liquid Tensor Experiment had to build inside Lean.

### 3. The "Who Guards the Guards?" Paradox and the de Bruijn Criterion
When an AI writes a five-page proof, an immediate paradox arises: *"AI models hallucinate—so who checks the AI? If a second AI checks it, who checks the second AI?"* Proof assistants break that infinite regress via the **de Bruijn criterion**: completely separate the **search engine** (a human or a billion-parameter neural network free to guess wildly) from a tiny **trusted kernel** of only a few thousand lines of pure code. Humans only need to audit that tiny kernel—once the kernel says yes, the proof is guaranteed valid from the axioms!

---

## Prerequisites

The proof essays, especially [Euclid / infinite primes]({{ site.baseurl }}/contents/en/chapter05/05_02_Euclid_Infinite_Primes/), [Gödel]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/), [four color]({{ site.baseurl }}/contents/en/chapter05/05_07_Four_Color_Proof/), and [Fermat]({{ site.baseurl }}/contents/en/chapter05/05_08_Fermat_Last_Theorem/). This page does not retell those arguments.

---

## Explanation: Reading a Real Lean 4 Proof and Checking a Category by Hand

To make "proofs as programs" and "category theory" concrete, walk through two miniature hand-verifiable examples:

### Worked Check 1: A Real Lean 4 Proof (Curry–Howard in Action)
Consider the basic logical rule *Modus Ponens*: *"If $$P$$ holds, and $$P \implies Q$$ holds, then $$Q$$ holds."* In Lean 4, it is literally a one-line function:

```lean
theorem modus_ponens (P Q : Prop) (hp : P) (hpq : P → Q) : Q :=
  hpq hp
```

Read it like a programmer:
- `P Q : Prop` declares two propositions (types).
- `hp : P` is a witness (term) of type `P`.
- `hpq : P → Q` is a **function** turning any proof of `P` into a proof of `Q`.
- The goal `: Q` demands a term of type `Q`.
- The proof `hpq hp` simply **applies the function `hpq` to the input `hp`**! Lean’s kernel checks the types—`hp : P` and `hpq : P → Q` yield `hpq hp : Q`—and flashes **green**.

Likewise, proving *"if $$n$$ is even then $$n^2$$ is even"* means taking a witness $$n = 2k$$, supplying the new witness $$m = 2k^2$$, and letting the kernel verify $$(2k)^2 = 2(2k^2)$$. Even towering projects like the Liquid Tensor Experiment are built out of thousands of tightly checked bricks just like this.

### Worked Check 2: Verifying a Category and a Functor by Hand
Take the most familiar category in mathematics, **$$\mathbf{Set}$$**:
- **Objects:** sets (e.g. $$A = \{1, 2\},\ B = \{x, y\},\ C = \{\text{Red}, \text{Blue}\}$$)
- **Arrows (morphisms):** functions $$f: A \to B$$ and $$g: B \to C$$.
- **Check the two category axioms by hand:**
  1. *Identity:* For each set $$A$$, $$\mathrm{id}_A(a) = a$$ satisfies $$f \circ \mathrm{id}_A = f$$ and $$\mathrm{id}_B \circ f = f$$.
  2. *Associativity:* For $$f: A \to B$$, $$g: B \to C$$, $$h: C \to D$$, at every $$a \in A$$ we have $$\bigl((h \circ g) \circ f\bigr)(a) = h\bigl(g(f(a))\bigr) = \bigl(h \circ (g \circ f)\bigr)(a)$$.

Replace sets by **vector spaces** and functions by **linear maps (matrices)** and you get the category **$$\mathbf{Vect}$$**. Taking the determinant $$\det(M)$$ turns matrix multiplication into scalar multiplication ($$\det(AB) = \det(A)\det(B)$$, $$\det(I) = 1$$)—a textbook **functor** preserving composition and identities!

---

## Conceptual development: Lean, AI, and Gödel’s Boundary

A proof assistant checks that a term inhabits a type. If $$T$$ is a formal statement, a Lean proof is an inhabitant of $$T$$, relative to the kernel, the axioms, and the libraries you trust.

**Why does this not contradict Gödel’s Incompleteness Theorems?** Gödel proved that any consistent, effectively axiomatized theory rich enough for arithmetic leaves some arithmetic sentences undecided—and no universal algorithm can decide *every* mathematical claim. Both realities coexist peacefully:

| What Lean & AlphaProof **CAN DO** | What Gödel Still **FORBIDS** |
|-----------------------------------|------------------------------|
| Certify *one specific proof* with total precision once a valid term is constructed. | No algorithm can guarantee finding a proof (or disproof) for *every* arithmetic statement. |
| Pair creative AI search with a tiny kernel to eliminate human oversight errors. | Lean’s own axiom system cannot prove its own absolute consistency from inside itself. |

You can verify *this* theorem today and still not own a decision procedure for every theorem.

---

## Three landings (2022–2026)

### 1. Liquid Tensor Experiment (2022)

On 14 July 2022 the Lean community, led by Johan Commelin with mathematical input from Scholze, announced completion of the Liquid Tensor Experiment: a formal verification of the main challenge theorem on liquid vector spaces (vanishing of certain $$\mathrm{Ext}$$ groups).

To even state Scholze’s theorem to a computer, contributors spent months building tens of thousands of lines of `mathlib` infrastructure in **category theory** (abelian categories, chain complexes, cohomology) and coordinating via a dependency *blueprint* that split the monolith into hundreds of parallelizable lemmas. The *idea* of the theorem stayed Scholze–Clausen’s; the *artifact* is an auditable repository.

### 2. AlphaGeometry (2024)

Trinh et al. (2024) pair a language model trained on hundreds of millions of synthetic geometry theorems with a symbolic deduction engine. The system emits human-readable proofs and solved **25 of 30** olympiad geometry problems in their benchmark.

In Olympiad geometry, symbolic engines excel at angle-chasing and similar triangles, yet stall whenever a problem requires **drawing an auxiliary point or line** (such as a midpoint $$M$$ or an extra circumcircle). AlphaGeometry delegates that creative "auxiliary construction" spark to the language model while leaving rigorous verification to the symbolic engine—closer to an organized Euclid move than a language-model essay.

### 3. AlphaProof and IMO 2024

DeepMind’s 25 July 2024 announcement, later expanded in a 2025 *Nature* paper, describes AlphaProof as an AlphaZero-style agent that searches for Lean proofs using *test-time reinforcement learning* on hard problems—generating millions of simpler variants around a target problem to train itself on the fly.

Together with AlphaGeometry 2 it solved **4 of 6** IMO 2024 problems (including the notorious Problem 6) for **28 of 42 points**—silver-medal *equivalent on the scoreboard*, with the essential footnotes that statements were formalized by human experts and computation ran for days rather than the 9-hour contest window. The Chapter 5 reading stays crisp: **the kernel still decides what counts as a proof**; the novelty is how candidate proofs are proposed.

---

## Interpretation and insight

A green Lean check is a guarantee relative to a specification, as Chapter 9’s verification theme emphasizes. It does not prove that the informal human statement was translated into Lean without a slip, and it is not an escape from incompleteness. AlphaProof’s silver-medal *score* is not a silver medal awarded to a student under IMO rules.

## Limitations and extensions

This note does not formalize FLT or Poincaré (though a major community project led by Kevin Buzzard is actively formalizing Fermat’s Last Theorem in Lean!). It does not claim that combinatorics problems are now easy for Lean agents (neither of the 2024 IMO combinatorics problems was solved by the system).

## References

- Lean community. (2022). Completion of the Liquid Tensor Experiment. [leanprover-community.github.io/blog/posts/lte-final](https://leanprover-community.github.io/blog/posts/lte-final/).
- Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482. [doi:10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5).
- Google DeepMind. (2024). AI achieves silver-medal standard solving International Mathematical Olympiad problems. [Blog, 25 July 2024](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/).
- Hubert, T., et al. (2025). Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature*. [doi:10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y).

## Video tham khảo

- **xem trước** — [Proving theorems with computers - Kevin Buzzard](https://www.youtube.com/watch?v=KccjCojGVO4) — Stony Brook Mathematics, English. Watch first. “Proving theorems with computers - Kevin Buzzard” orients the lesson’s aim: After this optional note you should be able to describe three 2022–2026 computing systems that take Chapter 5’s craft—make a claim machine-checkable—into Lean and neuro-symbolic se…
- [The AI that solved IMO Geometry Problems | Guest video by @Aleph0](https://www.youtube.com/watch?v=4NlrfOl0l8U) — 3Blue1Brown, English. A second pass once the main claim is in view: After this optional note you should be able to describe three 2022–2026 computing systems that take Chapter 5’s craft—make a claim machine-checkable—into Lean and neuro-symbolic se…
- [Improving on AlphaProof: IMO 2024 Problem 2 in Lean 4](https://www.youtube.com/watch?v=5IARsdn78xE) — David Renshaw, English. A Lean 4 formalization of an IMO 2024 problem in the AlphaProof style. Use it beside the lesson’s verification theme, not as an official DeepMind talk.
