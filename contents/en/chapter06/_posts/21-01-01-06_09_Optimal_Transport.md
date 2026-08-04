---
layout: post
title: "Optimal Transport"
chapter: '06'
order: 9
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

How do you move a pile of sand into the shape of another pile at minimal cost? That ancient-sounding question is the root of **optimal transport (OT)**, now a central language for comparing probability distributions, reshaping shapes, and building generative models. From Monge’s 1781 problem through Kantorovich’s linear programming relaxation to modern entropic regularization and computational geometry, OT sits at the crossroads of analysis, probability, optimization, and data science.

This lecture develops the Monge and Kantorovich formulations, Wasserstein distances, basic duality, computational ideas (including Sinkhorn), and applications—while marking theorems, numerical heuristics, and hype about “Wasserstein GANs solving generative modeling.”

---

## Learning objectives

After this lecture you should be able to:

- State Monge’s problem of transporting mass via a map $$T$$ minimizing cost, and explain why maps may fail to exist.
- Write the **Kantorovich** formulation as optimization over couplings $$\pi$$ with fixed marginals.
- Define the **$$p$$-Wasserstein distance** $$W_p$$ between probability measures with finite $$p$$-moments and interpret $$W_1$$ as a notion of distance sensitive to geometry.
- Explain, at slogan level, Kantorovich–Rubinstein duality for $$W_1$$ (Lipschitz dual).
- Describe why entropic regularization yields Sinkhorn iterations and what is gained/lost versus exact OT.
- Critique one popular ML claim that uses “Wasserstein” as a buzzword without specifying ground cost or estimator.

**Prerequisites.** Probability distributions as measures (integrals of test functions); basic optimization; Euclidean distance. Convex analysis helps but is not assumed in full.

---

## 1. Monge’s problem

Given probability measures $$\mu,\nu$$ on a space $$X$$ (think $$\mathbb{R}^d$$) and a cost $$c(x,y)$$, Monge asks for a transport **map** $$T:X\to X$$ pushing $$\mu$$ forward to $$\nu$$ ($$T_\#\mu=\nu$$) and minimizing

$$
\int_X c\bigl(x,T(x)\bigr)\,d\mu(x).
$$

Intuition: every grain at $$x$$ moves to a single location $$T(x)$$. Maps need not exist (e.g., splitting mass from one atom to two). Even when they exist, characterizing them is nontrivial. For cost $$c(x,y)=\|x-y\|^2$$ on $$\mathbb{R}^d$$, under regularity assumptions, Brenier’s theorem relates optimal maps to gradients of convex potentials: $$T=\nabla\phi$$.

---

## 2. Kantorovich’s relaxation: couplings

Kantorovich allows **splitting mass** via joint distributions $$\pi$$ on $$X\times X$$ with marginals $$\mu$$ and $$\nu$$:

$$
\inf_{\pi\in\Pi(\mu,\nu)} \int c(x,y)\,d\pi(x,y),
$$

where $$\Pi(\mu,\nu)$$ is the set of couplings. This is an infinite-dimensional linear program. Optimal $$\pi$$ are optimal **transport plans**. When an optimal plan concentrates on a graph of a map, one recovers Monge.

This formulation unlocked convex duality and a mature existence theory. It is the default mathematical starting point in modern OT.

---

## 3. Wasserstein distances

For $$p\ge 1$$ and measures with finite $$p$$-th moments, the **$$p$$-Wasserstein distance** is

$$
W_p(\mu,\nu) := \Bigl(\inf_{\pi\in\Pi(\mu,\nu)}\int \|x-y\|^p\,d\pi\Bigr)^{1/p}
$$

(on $$\mathbb{R}^d$$ with Euclidean ground cost; other metric spaces use $$d(x,y)^p$$). $$W_p$$ metrizes weak convergence plus convergence of $$p$$-moments under suitable conditions—more geometrically faithful than total variation or KL when supports differ. Moving a small bump across space costs roughly proportional to distance in $$W_1$$, whereas KL can be infinite if supports mismatch.

**Geometry of measure space.** The space of probability measures with finite second moment equipped with $$W_2$$ is a rich metric space (Otto calculus, geodesic convexity of certain functionals)—a frontier of analysis with PDE links (e.g., heat flow as gradient flow of entropy in Wasserstein space).

---

## 4. Duality (the useful face of OT)

For $$c(x,y)=\|x-y\|$$, the Kantorovich–Rubinstein theorem identifies

$$
W_1(\mu,\nu) = \sup_{\|f\|_{\mathrm{Lip}}\le 1} \Bigl(\int f\,d\mu - \int f\,d\nu\Bigr).
$$

Wasserstein-1 is the dual of Lipschitz functions with constant at most one. This dual view powers statistical bounds, robust optimization interpretations, and some generative modeling formulations (critic as Lipschitz function—**in theory**; in practice, Lipschitz constraints are approximated).

More general costs have $$c$$-concave potentials and complementary slackness structures ($$c$$-cyclical monotonicity of supports of optimal plans).

---

## 5. Computation: from LP to Sinkhorn

On discrete measures with $$n$$ support points, exact OT is a linear program with $$n^2$$ variables—solvable but costly at large $$n$$. **Entropic regularization** adds $$+\varepsilon \mathrm{KL}(\pi\|\mu\otimes\nu)$$ (or similar) to the objective, yielding a strictly convex problem solved by **Sinkhorn–Knopp** matrix scaling iterations. As $$\varepsilon\to 0$$, solutions approach optimal transport; for $$\varepsilon>0$$ one gets blurrier plans and a different divergence (Sinkhorn divergences need debiasing for some statistical uses).

Other computational paths: auction algorithms, network simplex, multiscale methods, sliced Wasserstein (project to 1D, average), and dynamical formulations (Benamou–Brenier) as fluid mechanics-type PDEs.

**Literacy.** “We used Wasserstein distance” in a paper may mean exact OT, entropic OT, sliced approximations, mini-batch biased estimates, or a loose dual penalty. These are **not interchangeable** statistically.

---

## 6. Applications map

| Domain | Role of OT |
|--------|------------|
| Statistics | Metrics between distributions; robust estimators |
| Vision / graphics | Color transfer, shape interpolation, registration |
| Economics | Matching markets; assignment (historical roots) |
| Generative ML | Distribution matching; WGAN dual heuristics; trajectory models |
| Biology | Comparing expression distributions; trajectory inference (careful) |
| PDE / physics | Gradient flows; aggregation-diffusion equations |

**Hype watch.** Wasserstein GANs popularized dual Lipschitz language; training stability claims are empirical and architecture-dependent, not pure corollaries of Kantorovich–Rubinstein. Mini-batch OT estimators can be badly biased in high dimension.

---

## 7. High dimension and sample complexity

Estimating $$W_p$$ between continuous measures in high ambient dimension from samples can require sample sizes exponential in dimension for some regimes—another face of the curse of dimensionality. Structure (low intrinsic dimension, smoothness) and alternative divergences change rates. This is active mathematical statistics, not a reason to abandon OT, but a reason to avoid naive claims.

---

## 8. Frontiers

1. Statistical rates for OT estimators and debiased Sinkhorn divergences.
2. OT on graphs, networks, and non-Euclidean spaces.
3. Multi-marginal transport and Wasserstein barycenters.
4. Causal and unbalanced transport (mass creation/destruction).
5. Gradient flows in metric measure spaces and links to sampling algorithms.
6. Scalable structured OT for large generative models with honest evaluation.

### Worked discrete example ($$2\times 2$$)

Suppose supply $$\mu=(1,0)$$ wait—better: masses $$a=(0.5,0.5)$$ at positions $$x_1,x_2$$ and $$b=(0.5,0.5)$$ at $$y_1,y_2$$. A coupling is a $$2\times 2$$ nonnegative matrix with row sums $$a$$ and column sums $$b$$. The cost is $$\sum_{ij}\pi_{ij}c_{ij}$$. If $$c_{11}$$ and $$c_{22}$$ are cheap while cross terms are expensive, the optimal plan prefers the diagonal; if geometry swaps, the plan swaps. Linear programming finds the optimum; you can solve tiny instances by enumerating the one-dimensional polytope of couplings.

Entropic OT replaces the hard optimum with a smoother objective, often unique, computed by alternating row/column scalings (Sinkhorn). Watching a $$3\times 3$$ cost matrix converge under Sinkhorn is worth more than a thousand slides.

### Why geometry of measures matters for learning

Training a generative model is, abstractly, making a pushforward measure $$G_\#\eta$$ close to a data measure $$\mu$$. Different divergences induce different geometries: mode-seeking vs mass-covering behavior, sensitivity to outliers, and sample complexity. Wasserstein metrics charge the cost of moving mass through space; that can match human notions of “nearby distributions” better than KL when supports barely overlap—**when** the ground metric is meaningful and the estimator is not destroyed by bias.

---

## Common confusions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Wasserstein is just another name for Earth Mover’s Distance.” | Roughly for $$W_1$$ discrete | EMD usually means discrete $$W_1$$; $$W_p$$ family is broader. |
| “OT always gives a map $$T$$.” | False | Kantorovich plans may split mass; maps need conditions. |
| “Sinkhorn equals exact OT.” | False | Entropic regularization biases the objective. |
| “WGAN trains true $$W_1$$.” | Overstated | Lipschitz constraints approximated; theory ≠ implementation. |
| “KL and $$W_p$$ measure the same mismatches.” | False | Different topologies and sensitivities. |
| “OT solves domain adaptation automatically.” | Heuristic | Useful toolkit; success is empirical and assumption-dependent. |

---

## Exercises

1. **Two Diracs.** Compute $$W_p(\delta_a,\delta_b)$$ for $$a,b\in\mathbb{R}$$.
2. **Why maps fail.** Explain why transporting $$\delta_0$$ to $$\tfrac12\delta_{-1}+\tfrac12\delta_{1}$$ cannot use a classical map without splitting.
3. **Coupling.** Write the set $$\Pi(\mu,\nu)$$ explicitly for two two-point discrete measures.
4. **Dual slogan.** Using Kantorovich–Rubinstein, why is $$W_1$$ large if means differ for measures on $$\mathbb{R}$$?
5. **Sinkhorn tradeoff.** Name one computational gain and one statistical/mathematical cost of entropic OT.
6. **Literacy.** Find a paper using “Wasserstein”; identify cost, discrete vs continuous, and exact vs approximate solver.
7. **Stretch.** Look up Brenier’s theorem statement; identify the cost function it targets.

---


---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/optimal-transport/analysis.md`.

### Status

**Mature theory, booming applications.** Monge–Kantorovich theory classical; Sinkhorn/entropic OT and gradient flows are modern computational engines.

### Core statement / slogan

Kantorovich problem: $$\inf_{\pi\in\Pi(\mu,\nu)}\int c\\,d\pi$$. Wasserstein-$$p$$ metrizes weak convergence (on suitable spaces). Brenier: under conditions, optimal maps are gradients of convex potentials.

### Definitions to freeze

- **Coupling.** Joint $$\pi$$ with marginals $$\mu,\nu$$.
- **Sinkhorn.** Entropic regularization of OT solved by matrix scaling.

### Hygiene (from confusions log)

- Thinking OT always yields a deterministic Monge map in discrete equal-mass unbalanced settings without hypotheses.
- Ignoring sample complexity blow-up of empirical W_p in high dimension.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/optimal-transport/`.

**Recommended order**

1. **Core** — Villani — Optimal Transport Theory (Imperial College): [https://www.youtube.com/watch?v=6DZjBcDfPHs](https://www.youtube.com/watch?v=6DZjBcDfPHs).  
2. **Foundation** — Fields Institute — Optimal Transportation Lecture 01: [https://www.youtube.com/watch?v=TAnoqeYfO1Y](https://www.youtube.com/watch?v=TAnoqeYfO1Y).  
3. **Orientation** — Simons — Crash Course on Optimal Transport: [https://www.youtube.com/watch?v=GMC7uOPAa_Y](https://www.youtube.com/watch?v=GMC7uOPAa_Y).  
4. **Computation** — UniHeidelberg — Sinkhorn iterations (discrete OT): [https://www.youtube.com/watch?v=BfOjrQAhG4M](https://www.youtube.com/watch?v=BfOjrQAhG4M).  

**Status reminder:** **Mature theory, booming applications.** Monge–Kantorovich theory classical; Sinkhorn/entropic OT and gradient flows are modern computational engines.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/optimal-transport/transcripts/` · status: `research/video-research/optimal-transport/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/optimal-transport_6DZjBcDfPHs_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References and further reading

1. C. Villani. *Topics in Optimal Transportation*; *Optimal Transport: Old and New*.
2. Peyré & Cuturi. *Computational Optimal Transport* (now classic applied monograph/survey).
3. Santambrogio. *Optimal Transport for Applied Mathematicians*.
4. Foundational: Monge; Kantorovich; Brenier.
5. Course links: [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [High-dimensional geometry]({{ site.baseurl }}/contents/en/chapter06/06_08_High_Dimensional_Geometry/), [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).

---


Full URL bibliography from video research: `research/video-research/optimal-transport/references.md`.

### Videos (recommended path)

- Villani — Optimal Transport Theory (Imperial College) (CORE): https://www.youtube.com/watch?v=6DZjBcDfPHs
- Fields Institute — Optimal Transportation Lecture 01 (FOUNDATION): https://www.youtube.com/watch?v=TAnoqeYfO1Y
- Simons — Crash Course on Optimal Transport (ORIENTATION): https://www.youtube.com/watch?v=GMC7uOPAa_Y
- UniHeidelberg — Sinkhorn iterations (discrete OT) (COMPUTATION): https://www.youtube.com/watch?v=BfOjrQAhG4M

### Papers and web (from research pack)

- Wikipedia — Transportation theory (mathematics): https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)
- Wikipedia — Wasserstein metric: https://en.wikipedia.org/wiki/Wasserstein_metric
- Peyré & Cuturi — Computational OT (arXiv survey): https://arxiv.org/abs/1803.00567
- Carmin.tv OT intro lectures: https://www.carmin.tv/en/video/introduction-to-optimal-transport-theory-lecture-2
- Wikipedia — Earth mover's distance: https://en.wikipedia.org/wiki/Earth_mover%27s_distance

### Course

- Research pack: `research/video-research/optimal-transport/` (especially `references.md`, `learning_path.md`).

## Further directions

- **Geometry of high-d samples:** [High-dimensional geometry]({{ site.baseurl }}/contents/en/chapter06/06_08_High_Dimensional_Geometry/).
- **Learning distributions:** [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/) and [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).
- **Practice:** solve a tiny discrete OT LP by hand ($$2\times 2$$ or $$3\times 3$$ supplies/demands); then try Sinkhorn on the same costs.
- **Reading path:** Peyré–Cuturi computational chapters → Villani intuition sections → one statistical rates paper abstract.
- Always specify: *ground cost, marginals, exact vs regularized, estimator*.
