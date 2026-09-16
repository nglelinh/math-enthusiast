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

## Learning objectives

After this optional note you should be able to describe three 2022–2026 computing systems that take Chapter 5’s craft—make a claim machine-checkable—into Lean and neuro-symbolic search, while still honoring Gödel: a verified kernel does not yield a complete theory of all arithmetic truths.

## Prerequisites

The proof essays, especially [Euclid / infinite primes]({{ site.baseurl }}/contents/en/chapter05/05_02_Euclid_Infinite_Primes/), [Gödel]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/), [four color]({{ site.baseurl }}/contents/en/chapter05/05_07_Four_Color_Proof/), and [Fermat]({{ site.baseurl }}/contents/en/chapter05/05_08_Fermat_Last_Theorem/). This page does not retell those arguments.

## Introduction

A proof is an idea that became an argument. Interactive theorem provers make the argument a program. The last few years turned that slogan into headlines: the Liquid Tensor Experiment finished in Lean in 2022; AlphaGeometry wrote olympiad geometry proofs in 2024; AlphaProof, trained with reinforcement learning in Lean, reached a silver-medal *score* at IMO 2024 (with multi-day compute and human formalization of statements). The Chapter 5 skill is to keep the *move* visible: construction, search, kernel checking—not banquet language about “AI solving mathematics.”

## Conceptual development

A proof assistant checks that a term inhabits a type. If $$T$$ is a formal statement, a Lean proof is an inhabitant of $$T$$, relative to the kernel, the axioms, and the libraries you trust. Gödel’s incompleteness says that any consistent, effectively axiomatized theory rich enough for arithmetic leaves some arithmetic sentences undecided. Those two facts live together. You can verify *this* theorem today and still not own a decision procedure for every theorem.

## Three landings

### 1. Liquid Tensor Experiment (2022)

On 14 July 2022 the Lean community, led by Johan Commelin with mathematical input from Scholze, announced completion of the Liquid Tensor Experiment: a formal verification of the main challenge theorem on liquid vector spaces (vanishing of certain $$\mathrm{Ext}$$ groups). The CS moral matches four-color and Kepler formalizations: a modern argument can be made to talk to a kernel, but only after a year-scale investment in libraries (abelian categories, cohomology). The *idea* of the theorem stayed Scholze–Clausen’s; the *artifact* is a repository.

### 2. AlphaGeometry (2024)

Trinh et al. (2024) pair a language model trained on synthetic geometry theorems with a symbolic deduction engine. The system emits human-readable proofs and solved 25 of 30 olympiad geometry problems in their benchmark. This is search plus a checker-friendly language, closer in spirit to a well-organized Euclid move than to a language-model essay. It does not replace the four-color computer proof’s lesson about *what counts* as a proof; it adds a generator that a human can still read.

### 3. AlphaProof and IMO 2024

DeepMind’s 25 July 2024 announcement, later expanded in a 2025 *Nature* paper, describes AlphaProof as an AlphaZero-style agent that searches for Lean proofs, using test-time RL on hard problems. Together with AlphaGeometry 2 it solved four of six IMO 2024 problems for 28 of 42 points—silver-medal *equivalent on the scoreboard*, with the important footnotes that statements were formalized by experts and that computation ran far beyond contest time. The Chapter 5 reading is precise: the kernel still decides what a proof is; the novelty is how candidates are proposed.

## Interpretation and insight

A green Lean check is a guarantee relative to a spec, as Chapter 9’s verification slogan also says. It is not a proof that the informal problem was formalized without a slip, and it is not an escape from incompleteness. AlphaProof’s silver-medal *score* is not a silver medal awarded to a student under IMO rules.

## Limitations and extensions

This note does not formalize FLT or Poincaré. It does not claim that combinatorics problems are now easy for Lean agents (the 2024 IMO combinatorics items were not solved by the system).

## Exercises

1. In the style of the Euclid essay, name the *move* in LTE: what is being reduced to a kernel check, and what had to be built first?
2. Why is “human-readable geometry proof” a different guarantee from “Lean kernel accepts a term”?
3. List three ways the IMO 2024 AlphaProof evaluation differed from the human contest, using only facts from the DeepMind note or the 2025 paper.
4. State Gödel incompleteness in one sentence that remains true after AlphaProof.

## References

- Lean community. (2022). Completion of the Liquid Tensor Experiment. [leanprover-community.github.io/blog/posts/lte-final](https://leanprover-community.github.io/blog/posts/lte-final/).
- Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482. [doi:10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5).
- Google DeepMind. (2024). AI achieves silver-medal standard solving International Mathematical Olympiad problems. [Blog, 25 July 2024](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/).
- Hubert, T., et al. (2025). Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature*. [doi:10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y).
