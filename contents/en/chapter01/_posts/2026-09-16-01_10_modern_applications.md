---
layout: post
title: "Modern Applications: Great Problems Meet Computer Science"
chapter: '01'
order: 10
owner: Nguyen Le Linh
lang: en
categories:
- chapter01
lesson_type: optional
---

## Learning objectives

After this optional note you should be able to name three places where a Chapter 1 problem—still open, or already a theorem—has become infrastructure or a research engine in computer science and data science since about 2022, without confusing a practical solver, a neural surrogate, or a medal-level geometry engine with a resolution of the original mathematical question.

## Prerequisites

The required essays in this chapter, especially [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/), [Four Color]({{ site.baseurl }}/contents/en/chapter01/01_09_Four_Color_Theorem/), and the [Collatz]({{ site.baseurl }}/contents/en/chapter01/01_07_Collatz_Conjecture/) studio. This page does not rewrite those statements.

## Introduction

A Clay problem can sit unsolved while industry ships code that *lives next to it*. SAT solvers attack NP-complete instances without proving $$\mathbf{P}\neq\mathbf{NP}$$. Learned operators forecast fluid fields without proving smooth Navier–Stokes solutions exist. A geometry engine can write olympiad proofs without settling Kakeya. The tension of this note is therefore hygienic. Recent CS/DS work is real; it is not a stealth solution of the great problems.

## Conceptual development

An NP-complete decision problem asks whether a certificate exists that a verifier can check in time polynomial in the input size $$n$$. Worst-case theory still waits. Practice asks a different question: on *this* formula, can a conflict-driven clause-learning (CDCL) search finish before the timeout? Likewise, a neural operator tries to approximate a solution map

$$
\mathcal{G}:u_0\mapsto u(\,\cdot\,,T)
$$

between function spaces, not to certify that $$u$$ stays smooth for every smooth divergence-free $$u_0$$.

## Four recent landings

### 1. SAT competitions as an industrial cousin of P vs NP

Annual SAT competitions through 2022–2024 still crown CDCL engines on huge industrial and crafted benchmarks. A solver that finishes does **not** place the instance in $$\mathbf{P}$$ as a complexity class, and a family that resists does **not** prove $$\mathbf{P}\neq\mathbf{NP}$$. What it does prove, operationally, is that the *certificate* view of NP is already a product: compilers, hardware verification, and planning emit CNF, and a search that learns conflict clauses is the default attack. Use this chapter’s P vs NP essay for the definitions; use the competition logs for the engineering fact.

### 2. Neural operators as Navier–Stokes surrogates

Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart, and Anandkumar (2023) formulate neural operators as maps between infinite-dimensional function spaces and test them on Burgers, Darcy flow, and Navier–Stokes. Fourier neural operators learn a surrogate $$\widehat{\mathcal{G}}$$ that can be evaluated orders of magnitude faster than a classical solver on similar grids. The Millennium question is existence and smoothness of the continuum equations. A small test error of $$\widehat{\mathcal{G}}$$ is an empirical regularity about one dataset and one architecture. Keep those labels apart.

### 3. AlphaGeometry as a computational attack on hard geometry

Trinh, Wu, Le, He, and Luong (2024) introduce AlphaGeometry, a neuro-symbolic prover trained on large-scale synthetic theorems. On a 30-problem olympiad geometry set it solves 25, approaching average IMO gold-medallist performance on that slice. This is a CS result about search, synthetic data, and a symbolic engine. It is not a proof of Kakeya, nor a substitute for the restriction-theory culture in this chapter and Chapter 2. It *is* evidence that “hard geometry” can be turned into a machine-checkable search space.

### 4. Exhaustive search beside Collatz

Barina (2021) reports a GPU-scale verification that the Collatz map reaches the trivial cycle for all starting values up to a bound on the order of $$2^{68}$$. Later engineering papers extend such searches. A finite initial segment, however large, is still a finite initial segment. Tao’s almost-all theorem and the open “every $$n$$” statement remain the mathematical objects. The CS contribution is a verified computation and a reminder of what a computation cannot finish.

## Interpretation and insight

In each case the great problem supplies a *shape*—certificates, continuum regularity, geometric construction, iteration—while the deployed system supplies a *budget*. Misreading the budget as a theorem is the characteristic error of 2020s science writing.

## Limitations and extensions

This note does not treat RH, BSD, or twin primes as crypto products; those stories belong with error terms and with Chapter 3’s number-theory essay. It also does not formalize SAT complexity beyond the slogan already in the P vs NP lecture.

## Exercises

1. A vendor says “our SAT solver shows P = NP on our customers’ netlists.” Rewrite the claim so that it is consistent with the definitions in the P vs NP essay.
2. A climate-start-up advertises a neural operator as having “solved Navier–Stokes.” Which two quantities would you demand (training distribution; a smoothness certificate) before you accept any weaker sentence?
3. AlphaGeometry solves 25 of 30 olympiad geometry problems. Why is that compatible with Kakeya remaining open?
4. If a Collatz search reaches $$2^{80}$$, what sentence in the Collatz essay remains exactly as true as it is today?

## References

- Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., & Anandkumar, A. (2023). Neural operator: Learning maps between function spaces with applications to PDEs. *JMLR*, 24(89), 1–97. [jmlr.org/papers/v24/21-1524.html](https://jmlr.org/papers/v24/21-1524.html).
- Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482. [doi:10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5).
- Barina, D. (2021). Convergence verification of the Collatz problem. *Journal of Supercomputing*, 77, 2681–2688. [doi:10.1007/s11227-020-03368-x](https://doi.org/10.1007/s11227-020-03368-x).
- [SAT Competition series](https://satcompetition.github.io/) (2022–2024 editions).
- Course: [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/), [Collatz]({{ site.baseurl }}/contents/en/chapter01/01_07_Collatz_Conjecture/).
