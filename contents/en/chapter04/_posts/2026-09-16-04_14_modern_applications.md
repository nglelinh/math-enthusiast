---
layout: post
title: "Modern Applications: Beauty That Ships"
chapter: '04'
order: 14
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
lesson_type: optional
---

Across Chapter 4, you have met ideas that look like pure mathematical art: shapes that tile the infinite plane without ever repeating, deterministic differential equations that twist trajectories into intricate shapes, and microscopic rules that spark sudden collective behavior. It is tempting to admire them behind museum glass and assume they stay there. Yet between 2022 and 2026, three of those exact ideas walked straight out of pure mathematics and shipped inside modern software repositories, generative AI engines, and frontier computer-science debates: **SAT-assisted aperiodic monotiles**, **score-based diffusion models**, and the **emergence-vs.-metric-mirage debate** in large language models.

This optional note is a side door into how mathematical beauty behaves when it meets real code, benchmarks, and engineering trade-offs—without replacing the [Six Math Essentials]({{ site.baseurl }}/contents/en/chapter04/04_01_Six_Math_Essentials/) map.

---

## Learning objectives

After this optional note you should be able to:

- Connect three "beautiful" Chapter 4 objects—**aperiodic order**, **dynamical systems**, and **emergence**—to concrete 2022–2026 computer-science landmarks.
- Explain how **SAT solvers** and Heesch-number search helped verify the 2023 **hat** aperiodic monotile.
- Compute a concrete 1D **score function** $$s(x) = \nabla_x \ln p(x)$$ for a two-peak Gaussian mixture to see how diffusion models steer pure noise back toward data.
- Compute a concrete **$$p^4$$ exact-match metric table** illustrating why Schaeffer, Miranda, and Koyejo (2023) warned that apparent "emergent cliffs" in LLMs can be artifacts of discontinuous metrics.
- Keep the mathematical definition distinct from the shipping software benchmark.

**Prerequisites.** The core beauty sequence—especially [tilings]({{ site.baseurl }}/contents/en/chapter04/04_10_Tilings/), [chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/) / dynamics, and [emergence]({{ site.baseurl }}/contents/en/chapter04/04_12_Emergence/).

---

## Background Knowledge Map: How Pure Ideas Become Engineering Tools

When a pure mathematical concept crosses into computer science and AI, three distinct mathematical disciplines act as the translation layer:

1. **Automated Reasoning & SAT Solving (Combinatorial Geometry):** Proving that a single polygon never tiles periodically—or finding how many concentric rings ("coronas," measured by the **Heesch number**) a tile can surround itself with—can be translated into millions of Boolean logic clauses and handed to modern **SAT solvers**, turning geometry into high-speed automated search.
2. **Stochastic Differential Equations & Score Matching (Generative AI):** Instead of asking a neural network to paint an image in one leap, **diffusion models** borrow the dynamical-systems mindset: corrupt data smoothly into Gaussian noise, train a network to estimate the **score field** $$\nabla_x \ln p_t(x)$$, and integrate a reverse-time ODE/SDE to flow noise back into crisp images or 3D protein structures (like AlphaFold 3).
3. **Measurement Theory & Scaling Laws (Empirical ML):** In physics, a phase transition is defined sharply in the infinite-size limit. In machine learning, we observe finite models through *evaluation metrics*—and nonlinear, all-or-nothing metrics can manufacture dramatic cliff-shaped curves even when underlying token probabilities improve smoothly.

---

## Conceptual development

- An **aperiodic monotile** is a single prototile that admits infinite tilings of the plane but zero periodic tilings.
- **Diffusion generative models** learn to reverse a continuous noising process $$x_0 \mapsto x_t$$ by estimating the **score** $$\nabla_x \ln p_t(x)$$—a vector field pointing toward higher data density.
- **Emergence** in large language models (Wei et al., 2022) refers to abilities absent at small scale that appear abruptly at large scale on a benchmark metric; Schaeffer, Miranda, and Koyejo (2023) showed that many of those abrupt jumps flatten into smooth curves when graded with continuous metrics.

---

## Three complementary landings—with hands-on calculations

### 1. The hat monotile and SAT-assisted tiling

Smith, Myers, Kaplan, and Goodman-Strauss (2023/2024) exhibited the **"hat"**—a 13-sided polykite that tiles the plane strictly aperiodically—along with a continuous family of related polygons and a computer-assisted combinatorial proof. Craig Kaplan’s earlier **SAT-solver** machinery for computing Heesch numbers was part of the discovery pipeline: encoding local tile-adjacency constraints as Boolean satisfiability clauses let software test thousands of candidate neighborhoods in seconds, guiding human geometers toward the final hierarchical proof. Here, exhaustive search and SAT encodings serve as precision mathematical microscopes.

### 2. Diffusion as trained dynamics—a 1D score calculation by hand

Karras, Aittala, Aila, and Laine (2022) unified the design space of score-based diffusion models—separating preconditioning, noise schedules, and numerical ODE/SDE samplers—to produce sharp images in just tens of network evaluations. Mathematically, a diffusion generator is a **learned dynamical system** whose velocity field is driven by the score $$\nabla_x \ln p_t(x)$$.

#### Worked example 1: Computing the score vector field of a two-peak distribution

Imagine a tiny 1D "dataset" clustered around two modes at $$x = -2$$ and $$x = +2$$, modeled by an equal mixture of two unit-variance Gaussians:

$$
p(x) = \frac{1}{2\sqrt{2\pi}}e^{-(x+2)^2/2} + \frac{1}{2\sqrt{2\pi}}e^{-(x-2)^2/2} \;\propto\; e^{-x^2/2}\cosh(2x).
$$

Take the logarithm and differentiate with respect to $$x$$ to obtain the exact **score function**:

$$
s(x) = \frac{d}{dx}\ln p(x) = 2\tanh(2x) - x.
$$

Evaluate $$s(x)$$ at three starting points of a noisy particle:
- **At $$x = +3.0$$** (too far right): $$s(3.0) = 2\tanh(6) - 3 \approx 2(1.000) - 3 = -1.000 < 0$$ $$\implies$$ the score arrow pushes **left**, pulling the particle back toward the $$+2$$ cluster.
- **At $$x = +0.5$$** (in the valley, slightly right of center): $$s(0.5) = 2\tanh(1) - 0.5 \approx 2(0.7616) - 0.5 = +1.023 > 0$$ $$\implies$$ the score arrow pushes **right**, driving the particle out of the empty valley toward the $$+2$$ cluster!
- **At $$x = -0.5$$** (slightly left of center): $$s(-0.5) = 2\tanh(-1) + 0.5 = -1.023 < 0$$ $$\implies$$ pushes **left**, toward the $$-2$$ cluster!

That single derivative $$s(x) = 2\tanh(2x) - x$$ is the entire geometric soul of modern image and protein diffusion: in $$10^6$$ dimensions instead of 1D, a neural network learns that exact vector field so random Gaussian noise flows effortlessly onto the manifold of realistic images.

### 3. Emergence, with a metric warning—the $$p^4$$ mirage

Wei et al. (2022) catalogued reasoning tasks where large language models appeared to sit near $$0\%$$ accuracy across smaller scales and then suddenly leap upward at a threshold scale. Schaeffer, Miranda, and Koyejo (2023) replied with a crisp mathematical caution: **check whether the cliff lives in the model or in the ruler you used to grade it.**

#### Worked example 2: How a smooth skill climb creates an apparent "phase transition"

Suppose a model answers a 4-digit arithmetic problem by predicting each digit independently with per-digit accuracy $$p$$, which improves *smoothly* as model size increases. Compare two metrics—**per-digit accuracy** ($$p$$) versus **strict 4-digit Exact Match** ($$p^4$$):

| Per-digit accuracy $$p$$ | Exact Match $$p^4$$ | Change in $$p$$ | Jump in $$p^4$$ |
| :--- | :--- | :--- | :--- |
| $$0.50$$ | $$6.25\%$$ | — | — |
| $$0.70$$ | $$24.01\%$$ | $$+0.20$$ | $$+17.8\%$$ |
| $$0.85$$ | $$52.20\%$$ | $$+0.15$$ | $$+28.2\%$$ |
| $$0.95$$ | $$81.45\%$$ | $$+0.10$$ | $$+29.3\%$$ |

Look at the last two rows: improving per-digit accuracy by a modest $$+0.10$$ (from $$0.85$$ to $$0.95$$) sends the Exact Match score rocketing upward by nearly $$+30$$ percentage points! If the task required 10 exact tokens ($$p^{10}$$), the score would look completely flat near $$0\%$$ until $$p > 0.8$$ and then shoot almost vertically upward—creating a dramatic "emergent cliff" purely from the nonlinear power $$p^k$$.

Chapter 4’s emergence lecture already taught the remedy: **name the observable and the scaling limit before declaring a genuine phase transition.**

---

### Deep-Dive Explanation: How Pure Math Ideas Turn Into Production Software (Read Slowly)

When you read a breathless tech headline claiming a "mathematical breakthrough in AI or geometry," run this four-step reality check slowly:

1. **Identify the underlying mathematical object.** Is it a combinatorial tiling constraint (SAT), a reverse-time vector field (score-based ODE/SDE), or a scaling curve on a discrete benchmark?
2. **Test the mechanism on a tiny toy model.** Computing $$s(x) = 2\tanh(2x) - x$$ in 1D or $$p^4$$ on 4 digits strips away billion-parameter hype and exposes the exact mathematical engine in three lines.
3. **Separate the theorem from the engineering artifact.** A pretty hat tiling on a screen is not the full proof of aperiodicity; a low FID score does not prove the reverse SDE recovered the exact true data distribution; a sharp Exact Match jump does not automatically equal a physical phase transition.
4. **Keep both lenses sharp.** Pure mathematics gives you clean definitions and guarantees; software gives you scale, discovery tools (like SAT solvers), and empirical stress tests.

**Quick check.** In Worked Example 2, if a task requires **10** independent tokens to all be exact (Exact Match $$= p^{10}$$), what is the Exact Match score when per-token accuracy is $$p = 0.70$$ versus $$p = 0.95$$? *(Hint: $$0.70^{10} \approx 2.8\%$$ vs. $$0.95^{10} \approx 59.9\%$$—a 21-fold jump from a smooth 25-point rise in $$p$$!)*

---

## Interpretation and insight

A hat tiling on a laptop wallpaper is not a classification of all aperiodic monotiles. A strong FID score is not a proof that a reverse SDE is the exact data-generating process. A discontinuous accuracy cliff is not automatically a new law of nature. Keep the beautiful definition and the shipping artifact in separate hands—and let each sharpen the other.

## Limitations and extensions

This page does not re-list numbers, algebra, geometry, probability, analysis, and dynamics. If you want that grammar, return to [Six Math Essentials]({{ site.baseurl }}/contents/en/chapter04/04_01_Six_Math_Essentials/). Fractals, impossible figures, and minimal surfaces remain in their own dedicated lectures.

## References

- Smith, D., Myers, J. S., Kaplan, C. S., & Goodman-Strauss, C. (2024). An aperiodic monotile. *Combinatorial Theory*, 4(1). [arXiv:2303.10798](https://arxiv.org/abs/2303.10798).
- Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. *NeurIPS*. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364).
- Wei, J., et al. (2022). Emergent abilities of large language models. *TMLR*. [arXiv:2206.07682](https://arxiv.org/abs/2206.07682).
- Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *NeurIPS*. [arXiv:2304.15004](https://arxiv.org/abs/2304.15004).
- Kaplan’s hat page: [cs.uwaterloo.ca/~csk/hat](https://cs.uwaterloo.ca/~csk/hat/).

## Video tham khảo

- **xem trước** — [Discovery of the Aperiodic Monotile - Numberphile](https://www.youtube.com/watch?v=_ZS3Oqg1AX0) — Numberphile, English. Watch first. “Discovery of the Aperiodic Monotile - Numberphile” orients the lesson’s aim: After this optional note you should be able to connect three “beautiful” objects already in this chapter—aperiodic order, dynamical generation, and emergence—to 2022–2026 computer-…
- [But how do AI images and videos actually work? | Guest video by Welch Labs](https://www.youtube.com/watch?v=iv-5mZ_9CPY) — 3Blue1Brown, English. A second pass once the main claim is in view: After this optional note you should be able to connect three “beautiful” objects already in this chapter—aperiodic order, dynamical generation, and emergence—to 2022–2026 computer-…
- [Inventing Game of Life (John Conway) - Numberphile](https://www.youtube.com/watch?v=R9Plq-D1gEk) — Numberphile, English. Further depth after the first two, still tied to this lesson: After this optional note you should be able to connect three “beautiful” objects already in this chapter—aperiodic order, dynamical generation, and emergence—to 2022–2026 computer-…
