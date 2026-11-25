---
layout: post
title: "Optimization → Operations & AI"
chapter: '03'
order: 7
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
lesson_type: required
---

Every morning, a major airline must assign hundreds of aircraft and thousands of crew members so no flight goes unstaffed, no pilot exceeds legal duty limits, and fuel burn stays minimal. Half a world away inside a data center, thousands of GPUs simultaneously nudge tens of billions of neural network weights to shave a fraction off next-token prediction loss.

On the surface, airline scheduling, hospital shifts, delivery routing, and training AI belong to separate industries. Under a mathematical lens, they are all disguises for **one universal question**: *among countless feasible choices, which one minimizes cost or error—and how do we find it fast?*

---

## Key ideas: What Is Mathematical Optimization and What Does It Study?

In high school, minimizing $$f(x)$$ meant setting $$f'(x)=0$$ and checking signs. In the real world, $$f$$ can have **millions of variables**, sharp non-differentiable corners, thousands of **inequality constraints**, or **integer requirements** (you cannot dispatch 1.4 airplanes!).

**Mathematical optimization** designs algorithms for those tough landscapes while answering two vital questions: *does the solver scale?* and *can we certify optimality?* The great fault lines of the field are **convex vs. nonconvex** and **continuous vs. discrete**:

- **Convex Optimization (LP, QP, Least Squares, SVM):** Shaped like a smooth bowl with a single global floor—fast polynomial solvers and ironclad duality certificates.
- **Discrete / Integer Programming (IP/MIP):** Yes/No operational decisions—NP-hard in worst-case theory, yet solved daily at industrial scale via branch-and-bound and convex relaxations.
- **Large-Scale Nonconvex Optimization (Deep Learning):** Rugged billion-dimensional landscapes navigated by stochastic first-order methods (SGD, Adam) seeking flat, well-generalizing valleys.

---

## Learning objectives

After this lecture you should be able to:

- Write a generic optimization problem $$\min_{x\in\mathcal{X}} f(x)$$ and identify objective, variables, and constraints in a word problem.
- Explain why **convexity** makes local minima global and why it is a gold standard for tractability.
- Describe gradient descent and the role of step size; connect to training ML models.
- State what linear programming (LP) and integer programming (IP) model in operations.
- Explain **duality** at slogan level (shadow prices / certificates of optimality).
- Avoid “gradient descent always finds the global minimum” and “convex means easy in practice without structure.”

**Prerequisites.** Multivariable derivatives (gradient). Helpful: [Linear Algebra]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/), [Probability / risk]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/).

**Seminar links.** [Math of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/).

---

## 1. The universal template

An optimization problem has the form

$$
\begin{aligned}
\min_{x}\quad & f(x) \\
\text{subject to}\quad & x\in\mathcal{X},
\end{aligned}
$$

where $$f$$ is the **objective** and $$\mathcal{X}$$ encodes **constraints** (equalities, inequalities, discrete sets, probability simplices, …). Maximization is minimization of $$-f$$. Feasibility ($$\mathcal{X}$$ nonempty) is itself a problem.

**Modeling skill** is half the field: translating “schedule nurses under labor rules” into variables and inequalities. Solvers only see the math.

**Mechanism slogan.**  
*Technology “optimizes” when it formulates decisions as objectives under constraints and applies algorithms with known guarantees or strong empirics.*

---

## 2. Convexity: the reliable landscape

A set $$\mathcal{X}$$ is **convex** if line segments between points of $$\mathcal{X}$$ stay in $$\mathcal{X}$$. A function $$f$$ is convex if

$$
f(tx+(1-t)y)\le t f(x)+(1-t)f(y), \quad t\in[0,1],
$$

i.e. the graph lies below chords (epigraph is a convex set). For differentiable $$f$$, convexity is equivalent to

$$
f(y)\ge f(x)+\langle\nabla f(x), y-x\rangle
$$

—the function lies above its tangents.

**Why it matters.** Any local minimum of a convex $$f$$ over a convex $$\mathcal{X}$$ is global. First-order optimality conditions become certificates, not just heuristics. Linear programs, least squares, many SVM formulations, and logarithmic barrier problems live in this world.

**Strict / strong convexity** refine uniqueness and linear/quadratic convergence rates for algorithms. Lipschitz gradients control how large a step size you may take.

---

## 3. Gradients and first-order methods

If $$f$$ is differentiable, the **gradient** $$\nabla f(x)$$ points toward steepest ascent. Gradient descent iterates

$$
x_{k+1}=x_k-\eta_k\nabla f(x_k).
$$

With appropriate step sizes $$\eta_k$$ and convex smooth assumptions, one proves convergence rates (e.g. $$O(1/k)$$ for convex smooth; linear rates for strongly convex). **Momentum**, **Nesterov acceleration**, and adaptive methods (Adagrad, RMSProp, **Adam**) modify the update using history of gradients—still first-order in spirit.

**Stochastic gradient descent (SGD).** When $$f(x)=\frac1n\sum_i f_i(x)$$ (empirical risk), estimate $$\nabla f$$ with one term or a mini-batch:

$$
x\leftarrow x-\eta\nabla f_i(x).
$$

Noise is not only a bug: it can help escape sharp bad regions and is computationally necessary at web scale. Probability explains concentration of the average gradient ([Probability lecture]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/)).

**Mechanism for AI.**  
*Training a neural net is large-scale nonlinear optimization of empirical risk; backprop supplies gradients; SGD-family methods update parameters.*

---

## 4. Constraints: projections, barriers, Lagrange

Hard constraints $$x\in\mathcal{X}$$ are handled by:

- **Projection** methods: gradient step then project onto $$\mathcal{X}$$ (projected gradient).  
- **Penalty / augmented Lagrangian** methods: soften constraints into the objective.  
- **Interior-point / barrier** methods: stay strictly feasible while driving a barrier parameter to zero (modern LP/QP engines).  
- **Active-set** strategies: guess which inequalities are tight.

For equality constraints $$g(x)=0$$, **Lagrange multipliers** $$\lambda$$ form the Lagrangian $$L(x,\lambda)=f(x)+\langle\lambda,g(x)\rangle$$. Stationarity $$\nabla_x L=0$$ plus feasibility are necessary conditions under regularity. Inequalities bring **KKT** conditions: stationarity, primal/dual feasibility, complementary slackness.

You need not memorize every KKT line to use CVXPY—but “multipliers as shadow prices” is the operational intuition: how much would the optimal value improve if a resource constraint relaxed by one unit?

---

## 5. Linear programming: the OR workhorse

A **linear program (LP)** has linear objective and linear constraints:

$$
\min_x\, c^\top x \quad\text{s.t.}\quad Ax\le b,\quad x\ge 0
$$

(or equality form). The feasible region is a polyhedron; optima occur at vertices (if they exist). The **simplex method** walks vertices; **interior-point methods** cut through the interior with polynomial-time worst-case theory (and excellent practice).

**Applications.** Blending, transportation, network flows (as LPs), production planning, many relaxations of harder problems. Airline scheduling and supply chains use LP/MIP stacks daily.

**Network flows** from the [Graph Theory]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/) lecture are special LPs with totally unimodular structure—integral optima without explicitly demanding integrality.

---

## 6. Integer programming: discrete decisions

When variables must be integers (or binary), we have **integer programs (IP/MIP)**:

$$
\min c^\top x \quad\text{s.t.}\quad Ax\le b,\quad x\in\mathbb{Z}^n.
$$

This models yes/no decisions: open a warehouse or not; assign a crew or not. General IP is NP-hard; practice uses branch-and-bound, cutting planes, heuristics, and strong formulations. The **LP relaxation** (drop integrality) gives bounds and guides search.

**Mechanism.**  
*Operations research succeeds by modeling discrete structure tightly enough that modern MIP solvers close the gap; pure worst-case hardness does not forbid industrial success on structured instances.*

---

## 7. Duality: certificates and prices

Every LP has a **dual**. Weak duality: any feasible dual objective bounds the primal. Strong duality (under feasibility/boundedness): optimal values match. A dual-optimal solution certifies optimality of a primal candidate—no need to trust the solver’s narrative alone.

Economically, dual variables are **shadow prices** of resources. Algorithmically, primal-dual methods maintain both sides. In convex optimization more broadly, Fenchel and Lagrangian duals organize entire algorithm families.

For flows, max-flow min-cut is a duality theorem in combinatorial clothing.

---

### Explanation: A 4-Step Playbook—Plus Solving a Primal–Dual LP with Shadow Prices by Hand

Whenever you face an optimization problem in engineering or AI, follow four steps—and see how **duality certifies optimality** on a concrete 2-variable Linear Program:

1. **Translate the problem into $$(x, f, \mathcal{X})$$:** Suppose a small workshop builds $$x_1$$ tables ($3 profit each) and $$x_2$$ chairs ($2 profit each), using wood ($$x_1 + x_2 \le 4$$) and labor hours ($$2x_1 + x_2 \le 6$$), with $$x_1, x_2 \ge 0$$.
2. **Check convexity and find the primal optimum:** Both the objective $$3x_1 + 2x_2$$ and the feasible polygon are convex (linear!). Testing the four corners of the feasible polygon:
   - $$(0,0) \to 0$$,
   - $$(0,4) \to 8$$,
   - $$(3,0) \to 9$$,
   - Intersection of $$x_1 + x_2 = 4$$ and $$2x_1 + x_2 = 6$$ gives **$$(x_1^*, x_2^*) = (2, 2)$$** with profit **$$3(2) + 2(2) = 10$$**.
3. **Certify optimality with dual shadow prices:** Assign shadow price $$y_1 \ge 0$$ to wood and $$y_2 \ge 0$$ to labor so the imputed resource cost covers every product’s profit ($$y_1 + 2y_2 \ge 3$$ and $$y_1 + y_2 \ge 2$$), while minimizing total resource valuation $$4y_1 + 6y_2$$.
   - Try **$$(y_1^*, y_2^*) = (1, 1)$$**: check feasibility $$1 + 2(1) = 3 \ge 3$$ and $$1 + 1 = 2 \ge 2$$.
   - Dual value: $$4(1) + 6(1) = 10$$!
   - Because any feasible primal profit $$\le$$ any feasible dual cost, hitting $$10 = 10$$ is an **airtight mathematical certificate** that $$(2, 2)$$ is globally optimal—and tells management immediately that buying 1 extra unit of wood or labor increases profit by exactly **$1**!
4. **Match solver to regime:** For structured convex/MIP problems, use interior-point or branch-and-bound solvers; for billion-parameter nonconvex neural nets, use SGD/Adam and validate generalization on held-out data.

**Quick check:** “Optimal” in operations research (an LP with a matching dual certificate) and “training converged” in deep learning (SGD settling in a flat basin) are two very different levels of guarantee.

## 8. Nonconvex optimization and deep learning

Neural net losses are typically **nonconvex**: many critical points, saddle-rich landscapes, symmetry-induced degeneracies. Theory no longer guarantees global optima from local search. Empirically, overparameterized models trained with SGD often reach solutions that *generalize*—a phenomenon still under active research ([ML Theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/), [Math of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/)).

Useful nonconvex tools:

- Random initialization + SGD with schedule.  
- Second-order heuristics (Gauss–Newton, K-FAC) at a cost.  
- Curriculum, normalization layers, residual connections—architecture as optimization preconditioning.  
- Global methods (branch and bound, multistart) when dimensions are small.

**Honesty.** “We train with Adam” is not a proof of optimality; it is an engineered procedure with empirical risk reduction and validation checks.

---

## 9. Optimization across this chapter’s technologies

| Domain | Typical formulation |
|--------|---------------------|
| Engineering design | PDE-constrained optimization; shape/topology |
| Control | LQR, MPC as repeated QPs |
| Operations | LP/MIP scheduling and routing |
| Statistics | MLE, ERM, regularized regression |
| ML training | Nonconvex ERM via SGD |
| Signal recovery | Basis pursuit, compressed sensing (convex proxies) |
| Transport | Optimal transport ([Ch.6]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/)) |

The unity is philosophical and practical: **write the objective, respect the constraints, know your landscape class, pick an algorithm with eyes open.**

---

### Optimization slogans (from video research)

Pair [3B1B gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) with Boyd’s free book [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).

- **Convexity:** every local minimum is global — the reason solvers can certify.
- **First-order methods:** only gradients; scale to high dimension at the cost of slow local conditioning.
- **Duality:** optimal dual variables price constraints; strong duality needs constraint qualifications.

## Common confusions

| Claim | Correction |
|-------|------------|
| “Gradient descent always finds the global min.” | Only under conditions (e.g. convexity); nonconvex nets are different. |
| “Convex problems are always trivial.” | High dimension, nonsmoothness, and constraints still challenge computation. |
| “LP and ML optimization are unrelated.” | Both minimize objectives under structure; algorithms and guarantees differ. |
| “Dual variables are just solver junk.” | They are shadow prices and optimality certificates. |
| “Integer programs can’t be solved because NP-hard.” | Structured industrial instances are solved daily; hardness is worst-case. |
| “Smaller training loss always means better model.” | Generalization is about risk, not only empirical loss. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/optimization-operations-ai/`.

**Recommended order**

1. **CORE** — 3Blue1Brown — Gradient descent, how neural networks learn: [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w).
2. **FOUNDATION** — Stanford / Boyd — Convex Optimization lectures (EE364): [https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h).
3. **FOUNDATION** — Boyd & Vandenberghe — Convex Optimization book (free PDF): [https://web.stanford.edu/~boyd/cvxbook/](https://web.stanford.edu/~boyd/cvxbook/).
4. **FOUNDATION** — MIT 6.255J / optimization OCW culture: [https://ocw.mit.edu/search/?q=optimization](https://ocw.mit.edu/search/?q=optimization).
5. **ORIENTATION** — StatQuest — Gradient Descent: [https://www.youtube.com/watch?v=sDv4f4s2SB8](https://www.youtube.com/watch?v=sDv4f4s2SB8).
6. **ORIENTATION** — 3Blue1Brown — Essence of calculus (derivatives for optimization): [https://www.youtube.com/watch?v=WUvTyaaNkzM](https://www.youtube.com/watch?v=WUvTyaaNkzM).

Complete URL bibliography: `research/video-research/optimization-operations-ai/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/optimization-operations-ai/transcripts/` · status: `research/video-research/optimization-operations-ai/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/optimization-operations-ai_IHZwWFHWa-w_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/optimization-operations-ai/references.md`.

### Videos (primary path)

1. 3Blue1Brown — Gradient descent, how neural networks learn — https://www.youtube.com/watch?v=IHZwWFHWa-w
2. Stanford / Boyd — Convex Optimization lectures (EE364) — https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h
3. Boyd & Vandenberghe — Convex Optimization book (free PDF) — https://web.stanford.edu/~boyd/cvxbook/
4. MIT 6.255J / optimization OCW culture — https://ocw.mit.edu/search/?q=optimization
5. StatQuest — Gradient Descent — https://www.youtube.com/watch?v=sDv4f4s2SB8
6. 3Blue1Brown — Essence of calculus (derivatives for optimization) — https://www.youtube.com/watch?v=WUvTyaaNkzM
7. Linear programming simplex culture (popular explainers) — https://en.wikipedia.org/wiki/Simplex_algorithm
8. Duality / Lagrange multipliers visual lectures — https://en.wikipedia.org/wiki/Lagrange_multiplier

### Videos (secondary finds)

9. Nocedal & Wright numerical optimization culture talks — https://web.stanford.edu/~boyd/cvxbook/

### Papers, books, OCW, and web

10. Boyd & Vandenberghe — Convex Optimization (PDF): https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf
11. Nesterov — Introductory Lectures on Convex Optimization: https://link.springer.com/book/10.1007/978-1-4419-8853-9
12. Wikipedia — Convex optimization: https://en.wikipedia.org/wiki/Convex_optimization
13. Wikipedia — Linear programming: https://en.wikipedia.org/wiki/Linear_programming
14. Wikipedia — Lagrange multiplier: https://en.wikipedia.org/wiki/Lagrange_multiplier
15. Wikipedia — Stochastic gradient descent: https://en.wikipedia.org/wiki/Stochastic_gradient_descent

### Course

16. Course: [Linear Algebra → AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/), [Probability]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/), [Graphs]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/), [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/), [ML Theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/). Pack: `research/video-research/optimization-operations-ai/`.

## Further directions

- Next: [Fourier → Signal Processing]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/) (another pure idea turned infrastructure).  
- Deeper learning theory: [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/).  
- Geometry of distributions: [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/).  
- Restate the core mechanism of this essay in one paragraph; note one precise question you still have.

## Video tham khảo

- **xem trước** — [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w) — 3Blue1Brown, English. Watch first. “Gradient descent, how neural networks learn | Deep Learning Chapter 2” orients the lesson’s aim: Write a generic optimization problem \min{x\in\mathcal{X}} f(x) and identify objective, variables, and constraints in a word problem.
- [Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8) — StatQuest with Josh Starmer, English. A second pass once the main claim is in view: Write a generic optimization problem \min{x\in\mathcal{X}} f(x) and identify objective, variables, and constraints in a word problem.
- [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) — 3Blue1Brown, English. Further depth after the first two, still tied to this lesson: Write a generic optimization problem \min{x\in\mathcal{X}} f(x) and identify objective, variables, and constraints in a word problem.
