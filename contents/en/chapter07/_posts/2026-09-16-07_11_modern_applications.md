---
layout: post
title: "Modern Applications: Computers in the Studio"
chapter: '07'
order: 11
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
lesson_type: optional
---

## Learning objectives

After this optional studio companion you should be able to borrow three 2022–2026 computational instruments—SAT-assisted tiling, neuro-symbolic geometry search, and large-bound Collatz checks—without letting a finished computation impersonate a finished exploration log.

## Prerequisites

The studio overview and at least one of [iteration / Collatz]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/), [tilings / map colors]({{ site.baseurl }}/contents/en/chapter07/07_07_Explore_Map_Colors/), [Kakeya]({{ site.baseurl }}/contents/en/chapter07/07_02_Explore_Kakeya/), or [sphere packing]({{ site.baseurl }}/contents/en/chapter07/07_03_Explore_Sphere_Packing/).

## Introduction

Chapter 7 is a notebook, not a lecture hall. Recent CS systems are extremely tempting notebooks: they return a tile, a proof sketch, or a bound of $$2^{68}$$. The studio habit is older than those systems. Form a conjecture, design a small experiment, record a failure, separate observation from proof. This page shows how to *use* the new instruments inside that habit.

## Conceptual development

A SAT solver returns satisfiable or unsatisfiable for a finite encoding. A geometry engine returns a proof in a formal geometry language. A Collatz checker returns “all $$n\le N$$ reached 1.” Each output is an observation about a *finite* object. The studio’s open prompts—how small can a Kakeya set be? does every $$n$$ reach 1?—remain infinite. The useful move is to write the finite object into the log as data, then write the still-open sentence beside it.

## Three instruments

### 1. SAT and the hat, as a tiling studio

Smith, Myers, Kaplan, and Goodman-Strauss (2023/2024) used computational searches (including SAT-based Heesch bounds) on the way to the hat monotile. For the map-color and tiling studios, the transferable lesson is not “download a hat and stop.” It is: encode a local matching rule, ask a solver for a patch of radius $$R$$, and let unsatisfiability *inform* a conjecture. Kaplan’s public hat page is a model of sharing code and pictures with the argument.

### 2. AlphaGeometry as a geometry notebook, not an oracle

Trinh et al. (2024) show that a synthetic-data language model plus a symbolic engine can emit readable olympiad proofs. In a Kakeya or fourth-dimension studio you might use such a tool to chase a Euclidean lemma. You still owe the log a sentence about what was assumed (plane geometry, a translation of the problem) and what was not (a continuum Kakeya bound).

### 3. Collatz search as a bounded experiment

Barina (2021) and later GPU checks push exhaustive Collatz verification to enormous $$N$$. The Chapter 7 iteration studio already forbids writing “checked up to $$N$$” as “true for all $$n$$.” Use the published bound as one row in your table; use Tao’s almost-all theorem as a different row; keep the universal claim open.

## Interpretation and insight

Computers are outstanding at filling tables. They are average at noticing that the table is not the theorem. The studio grade, if this course is taught, is for the log’s honesty, not for the largest $$N$$.

## Limitations and extensions

Sphere-packing numerics, prime-gap plots, and randomness-vs-order coin-flip labs can use the same pattern. Duality dictionaries (the last studio) are still hand-drawn maps; a language model that fills the table is a draft, not a dictionary.

## Exercises

1. Encode, in words, a SAT question that would help a *map-color* studio without claiming four color as your result.
2. Take an AlphaGeometry-style proof of a simple concurrence. What two lines belong in your exploration log?
3. Add a row to a Collatz table: $$N=2^{68}$$, method = GPU search, status = finite check. Write the adjacent row for “every positive integer.”
4. Why is “the solver returned UNSAT” closer to a proof than “the neural net’s loss is small”—and when is it still not a proof of the infinite statement you care about?

## References

- Smith, D., Myers, J. S., Kaplan, C. S., & Goodman-Strauss, C. (2024). An aperiodic monotile. *Combinatorial Theory*, 4(1). [arXiv:2303.10798](https://arxiv.org/abs/2303.10798).
- Trinh, T. H., et al. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482.
- Barina, D. (2021). Convergence verification of the Collatz problem. *Journal of Supercomputing*, 77, 2681–2688.
- Kaplan, C. S. Hat resources: [cs.uwaterloo.ca/~csk/hat](https://cs.uwaterloo.ca/~csk/hat/).
- Studio: [Iteration]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/).
