---
layout: post
title: "Bengio, Hinton, LeCun: Deep Learning Foundations (Turing 2018)"
chapter: '09'
order: 12
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

In the mid-1990s, submitting a paper on multi-layer neural networks to a premier machine-learning conference often earned a brisk rejection: *"Nonconvex loss, no clean convergence theorems like SVMs, and far too heavy to train!"* Throughout that "neural network winter," three scientists—**Yoshua Bengio**, **Geoffrey Hinton**, and **Yann LeCun**—kept alive a contrarian bet: instead of hand-crafting features by human intuition, stack many nonlinear layers so machines **learn hierarchical representations** directly from raw data.

Then came 2012: as massive datasets and GPUs finally caught up with their ideas, AlexNet shattered the ImageNet benchmark and ignited the modern AI era. In **2018**, the trio shared the **A.M. Turing Award** for conceptual and engineering breakthroughs that made **deep neural networks** a critical component of computing (official materials: [amturing.acm.org](https://amturing.acm.org/)).

This lecture clears away the marketing fog around AI to examine the **mathematical engine** underneath: composed nonlinear maps, reverse-mode differentiation on computational graphs, inductive biases of convolutions and attention, and the major theoretical puzzles still wide open. Cross-links: [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/) and [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).

---

## Learning objectives

After this lecture you should be able to write a layer map $$x\mapsto\sigma(Wx+b)$$ and describe a deep net as composition; explain training as empirical risk minimization with gradient-based updates and backpropagation as chain rule on a computational graph; name CNN, RNN/sequence, and transformer inductive biases at slogan level; define representation learning as learning features rather than only hand-crafting them; and rewrite popular deep-learning claims into precise statements about benchmarks, assumptions, or open theory.

**Prerequisites / cross-links.** Vectors/matrices; derivatives as local linear approximation; basic probability. Flagship twins: [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/), [optimization applications]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/). Chapter hub: [Turing overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/).

---

## Background Knowledge Map: What Are Deep Learning and Representation Learning?

Strip away the "artificial brain" metaphor, and to a university graduate a deep neural network is the marriage of three familiar mathematical subjects: **Linear Algebra**, **Multivariable Calculus**, and **Stochastic Optimization**.

1. **Hierarchical Representation Learning:** rather than jumping from raw pixels straight to the label `"Cat"`, a deep network composes simple layers $$f(x) = f_L(\dots f_2(f_1(x))\dots)$$. Early layers detect light–dark edges; middle layers assemble edges into ears and eyes; top layers assemble parts into faces. Each layer acts as a **nonlinear coordinate warp** stretching space until tangled data becomes linearly separable at the final layer.
2. **Backpropagation:** simply the **multivariable chain rule** applied systematically from the scalar loss backward through the computational graph, yielding exact partial derivatives with respect to millions of weights at the same computational cost as a single forward pass.
3. **Architectural Inductive Bias:** feel the parameter savings with one crisp comparison—on a tiny $$28 \times 28 = 784$$-pixel image, a fully connected layer outputting $$784$$ neurons demands $$784 \times 784 \approx 614{,}656$$ weights! A $$3 \times 3$$ convolutional filter sliding across the entire image uses just **9 shared weights** (plus 1 bias)—nearly a **70,000-fold reduction** by encoding one geometric fact about vision: *"a cat's ear in the top-left corner is still a cat's ear in the bottom-right."*

---

## 1. Three careers, one paradigm shift

Rough caricatures (not full biographies):

- **Hinton:** multi-decade advocacy for neural networks, Boltzmann machines and deep belief nets as pretraining culture, backpropagation popularization, and later capsule/attention-related ideas; a public scientific role during the deep learning resurgence.  
- **LeCun:** convolutional networks for vision (LeNet lineage), energy-based and self-supervised themes, and institutional leadership connecting research to large-scale systems.  
- **Bengio:** sequence models, attention precursors and neural language modeling culture, generative models, and a research program on representation learning and, later, causality-aware AI arguments.

The Turing Award recognizes a **shared paradigm**: deep architectures trained by gradient methods on large data, learning hierarchical representations. Credit is collective across a community; the medal names three standard-bearers.

---

## 2. Neural networks as mathematical objects

### Layers

A fully connected layer is

$$
x \mapsto \sigma(Wx + b),
$$

with weight matrix $$W$$, bias $$b$$, and nonlinearity $$\sigma$$ applied coordinatewise (ReLU, GELU, sigmoid, …). A network of depth $$L$$ composes such maps (with architectural variants: residual links $$x\mapsto x+f_\theta(x)$$, normalizations, attention blocks).

### Function class, not magic

For fixed architecture, the net defines a parametric family $$f_\theta$$. Universal approximation theorems say shallow nets with enough width can approximate broad continuous function classes on compact sets—but existence of parameters is not efficient learnability. Depth can improve representation efficiency for some compositional target functions; proving *which* real tasks require depth remains a living theory problem.

### High-dimensional geometry

Inputs are vectors in high dimension (images, embeddings). Geometry and probability from [high-dimensional ideas]({{ site.baseurl }}/contents/en/chapter06/06_08_High_Dimensional_Geometry/) and concentration culture appear in generalization stories—even when practical tuning remains empirical.

---

## 3. Learning as optimization; backpropagation as culture

Training typically minimizes empirical risk

$$
\hat R_S(\theta) = \frac{1}{n}\sum_{i=1}^n \ell\bigl(f_\theta(x_i), y_i\bigr)
$$

by stochastic gradient descent or variants (momentum, Adam, …):

$$
\theta_{t+1} = \theta_t - \eta_t \widehat{\nabla_\theta \hat R}(\theta_t).
$$

**Backpropagation** is reverse-mode automatic differentiation: the chain rule factored through the computational graph so each weight receives $$\partial L/\partial \theta$$ efficiently. It is calculus plus dynamic programming on graphs—not a mysterious AI essence.

### Worked Example (Step by Step): Hand-Running One Backprop Step and One $$2\times 2$$ Convolution

To see firsthand that neural networks contain zero magic, execute both core calculations by hand:

**Part A — One training step of a 2-layer ReLU network via backpropagation.** Take input $$x = 2$$, target $$y = 1$$, initial weights $$w_1 = 0.5$$ and $$w_2 = 1.5$$ (omitting biases), hidden activation $$\mathrm{ReLU}(z) = \max(0, z)$$, and squared loss $$L = \tfrac{1}{2}(\hat{y} - y)^2$$:

1. **Forward pass:**
   - Layer 1: $$z_1 = w_1 x = 0.5 \times 2 = 1$$, then $$a_1 = \max(0, 1) = 1$$.
   - Layer 2: $$\hat{y} = w_2 a_1 = 1.5 \times 1 = 1.5$$.
   - Current loss: $$L = \tfrac{1}{2}(1.5 - 1)^2 = \mathbf{0.125}$$.
2. **Backward pass (chain rule):**
   - Output gradient: $$\dfrac{\partial L}{\partial \hat{y}} = \hat{y} - y = 1.5 - 1 = 0.5$$.
   - Gradient for $$w_2$$: $$\dfrac{\partial L}{\partial w_2} = \dfrac{\partial L}{\partial \hat{y}} \cdot a_1 = 0.5 \times 1 = \mathbf{0.5}$$.
   - Propagate error back to $$a_1$$: $$\dfrac{\partial L}{\partial a_1} = \dfrac{\partial L}{\partial \hat{y}} \cdot w_2 = 0.5 \times 1.5 = 0.75$$.
   - Since $$z_1 = 1 > 0$$, $$\mathrm{ReLU}'(z_1) = 1$$, giving $$\dfrac{\partial L}{\partial w_1} = \dfrac{\partial L}{\partial a_1} \cdot \mathrm{ReLU}'(z_1) \cdot x = 0.75 \times 1 \times 2 = \mathbf{1.5}$$.
3. **Gradient descent update (learning rate $$\eta = 0.1$$):**
   - $$w_2^{\text{new}} = 1.5 - 0.1 \times 0.5 = \mathbf{1.45}$$,
   - $$w_1^{\text{new}} = 0.5 - 0.1 \times 1.5 = \mathbf{0.35}$$.
4. **Verify the new forward pass:** $$z_1^{\text{new}} = 0.35 \times 2 = 0.7$$, $$\hat{y}^{\text{new}} = 1.45 \times 0.7 = \mathbf{1.015}$$, new loss $$L^{\text{new}} = \tfrac{1}{2}(0.015)^2 = \mathbf{0.0001125}$$ — down by over **1,100×** in a single step!

**Part B — A $$2\times 2$$ vertical-edge convolution (LeCun's LeNet in miniature).** Given a $$3 \times 3$$ image patch (bright left half = 10, dark right half = 0) and a $$2 \times 2$$ edge-detector kernel $$K$$:

$$
X = \begin{pmatrix} 10 & 10 & 0 \\ 10 & 10 & 0 \\ 10 & 10 & 0 \end{pmatrix}, \qquad K = \begin{pmatrix} 1 & -1 \\ 1 & -1 \end{pmatrix}.
$$

Slide $$K$$ across all four $$2 \times 2$$ windows of $$X$$ and sum elementwise products:
- Top-left: $$10(1)+10(-1)+10(1)+10(-1) = 0$$ (flat region, no edge).
- Top-right: $$10(1)+0(-1)+10(1)+0(-1) = \mathbf{20}$$ (strong vertical edge!).
- Bottom-left: $$0$$; bottom-right: $$\mathbf{20}$$.

The resulting feature map is $$\begin{pmatrix} 0 & 20 \\ 0 & 20 \end{pmatrix}$$: using just **4 shared weights**, the filter automatically flags the vertical light–dark boundary wherever it appears.

### Deep-Dive Explanation: Why "Depth + Nonlinearity + Weight Sharing" Sparked a Revolution (Read Slowly)

1. **Nonlinearity saves depth from collapsing:** without a nonlinear activation (like ReLU in Part A), 100 stacked matrix multiplications collapse into a single linear matrix—depth buys nothing. ReLU folds space at every layer, letting the number of linear regions grow exponentially with depth.
2. **Backprop turns the chain rule into linear-time accounting:** instead of perturbing each weight separately (millions of forward passes), the backward pass reuses cached activations $$a_1, z_1$$ to compute *every* gradient in one sweep.
3. **Architecture encodes geometry up front:** the space of all functions from pixels to labels is unimaginably vast. Convolutions (CNNs) restrict search to translation-equivariant maps; attention opens global token-to-token routing—every architecture is a geometric hypothesis about data.
4. **The theoretical frontier stays wide open:** we just watched SGD slash loss 1,100× on a 2-weight net. Yet why do billion-parameter nets capable of memorizing pure noise still generalize cleanly on real data? That is the open baton the 2018 Turing Award handed to the next generation of mathematicians.

**Quick check.** In Part A, what happens if we initialize $$w_1 = -0.5$$ for $$x = 2$$? Then $$z_1 = -1 < 0$$, so $$\mathrm{ReLU}(z_1) = 0$$ and $$\mathrm{ReLU}'(z_1) = 0$$—the gradient for $$w_1$$ is identically **0** (*dying ReLU*). One minus sign in initialization can freeze a neuron permanently, explaining why careful initialization (He/Xavier) and residual shortcuts (ResNet) are make-or-break.

**Culture.** “Backprop culture” means: define a differentiable scalar loss; rely on autodiff; iterate at scale. Non-differentiable pieces (discrete choices, hard attention historically) require relaxations or other estimators. The 2010s explosion combined this culture with GPUs, large labeled sets (and later web-scale unlabeled data), and architectural priors.

Open mathematics: nonconvex landscapes, implicit bias of SGD, when overparameterized nets interpolate yet generalize ([ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/)). Empirical success is real; complete theory is not.

---

## 4. Architectural inductive biases (CNN / RNN / transformers light)

### Convolutional nets (vision)

**CNNs** reuse local filters across spatial positions (weight sharing) and build hierarchy via stacking and pooling. Translation structure of images becomes a mathematical prior: a feature detector for an edge need not be relearned at every pixel independently. LeCun’s lineage made CNNs the default vision stack for a decade-plus of benchmarks.

### Sequence models

**RNNs** and related recurrent architectures process sequences by maintaining a state $$h_t = \phi(h_{t-1}, x_t)$$. They introduced end-to-end neural language and speech models but struggle with long dependencies and parallelization. Bengio and collaborators’ work on neural probabilistic language models and later attention-related ideas sits in this arc.

### Transformers (light)

**Transformers** replace much recurrence with attention: tokens mix via data-dependent weighted combinations of values, with queries and keys implementing similarity scores (softmax over scaled dot products). They parallelize well and dominate modern NLP and increasingly vision. For this lecture: treat transformers as a *successful inductive bias + systems story*, not as a proof that attention is the unique mathematical answer to intelligence.

### Representation learning

Classical ML often used hand-crafted features. Deep learning bets that **stacked trainable layers** learn features adapted to the task and data. Self-supervised objectives (predict masked parts, contrastive views, next-token prediction) extend the bet to unlabeled data. The phrase “representation learning” is a research program, not a single theorem.

---

## 5. Hype versus theorem

Practice rewriting claims:

| Hype form | More precise form |
|-----------|-------------------|
| “Deep learning solves intelligence.” | “Deep nets achieve high scores on specified benchmarks under stated training regimes; general intelligence is undefined/unproven here.” |
| “Backprop is how the brain learns.” | “Backprop is an efficient computational method for gradients; biological credit assignment is a separate scientific question.” |
| “Theory cannot explain deep learning, so theory is useless.” | “Classical capacity bounds can be vacuous; algorithm- and data-dependent theories are active research, not absence of mathematics.” |
| “Scale is all you need” (absolute). | “Empirical scaling laws describe trends on measured metrics within regimes; they are not theorems about all tasks or safety properties.” |

Key habit: cite **what was measured**, **what was assumed**, and **what remains open**. Turing 2018 honors foundations of a technology family; it does not close the mathematics of AI.

---

## 6. Links across the course

- [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/): stack from linear algebra to open problems.  
- [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/): generalization, overparameterization.  
- [Valiant / PAC]({{ site.baseurl }}/contents/en/chapter09/09_09_Valiant_Learning/): definitions of learnability that predate the deep era.  
- [Pearl]({{ site.baseurl }}/contents/en/chapter09/09_11_Pearl_Causality/): interventional questions when models act.  
- [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/): gradient methods as applied math.

Deep learning is where several course rivers meet: high-dimensional geometry, probability, optimization, and complexity-flavored caution about what efficient algorithms can guarantee.

### What the 2010s actually changed

Neural nets existed for decades; what changed was a **stack**:

- **Data scale** — large labeled sets (and later web-scale text/images) made high-capacity models statistically usable.  
- **Compute** — GPUs/TPUs matched dense linear algebra.  
- **Software** — frameworks made autodiff and batched training default engineering.  
- **Architecture priors** — convolutions, residual links, normalization, attention.  
- **Objectives** — from pure supervised losses toward self-supervised and generative objectives.

Turing 2018 sits at the scientific center of that stack’s research core, not at the claim that intelligence is solved. A fair reading of the citation is: without the intellectual persistence and technical foundations associated with these lineages, the stack would have been thinner when hardware and data arrived.

### Self-supervision and foundation models (light)

Next-token prediction and related pretext tasks turn raw sequences into training signal. That is still empirical risk minimization on a surrogate loss; the “foundation” metaphor means transfer to many downstream tasks after large-scale pretraining. Mathematically, one should still ask about distribution shift, calibration, causal misuse, and the gap between benchmark suites and deployment worlds—the same critical checklist as in [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/).

### Relation to Valiant

[PAC learning]({{ site.baseurl }}/contents/en/chapter09/09_09_Valiant_Learning/) asks when a class is learnable with polynomial samples and time under worst-case distributions. Deep learning often succeeds on structured natural distributions with algorithms that are not PAC-style proper learners of a clean concept class. The frameworks are not enemies: PAC supplies impossibility and sample slogans; deep learning supplies a working inductive-bias laboratory; modern theory tries to reconnect them.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “Turing 2018 invented neural nets.” | Neural nets are older; the award honors foundational modern deep learning contributions. |
| “More layers always strictly better.” | Depth helps some representations; optimization, data, and architecture interact; not a free monotone law. |
| “Autodiff removes the need to understand gradients.” | It removes hand derivation of each layer; analysis and debugging still need calculus literacy. |
| “CNNs are obsolete so convolutions were wrong.” | Inductive biases migrate; historical CNN success remains mathematically instructive. |
| “If it works on ImageNet/GLUE, the theory is done.” | Benchmarks are evaluations, not proofs of general laws. |
| “Deep learning replaced statistics.” | Training objectives, generalization, and calibration remain statistical problems. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/deep-learning-trio/`.

**From the research pack (must-know slogans)**

- Turing 2018: conceptual and engineering foundations of deep neural networks.
- Backprop culture, CNNs (LeCun), deep belief / representation learning (Hinton), sequence/attention lineage (Bengio school).
- Not a mathematical completeness theorem for AI; empirical + theoretical research program.
- Hinton later Nobel Physics 2024 (separate honor).

**Recommended order**


**Official / primary written hubs**

- Hinton Turing: https://amturing.acm.org/award_winners/hinton_4791679.cfm  
- LeCun Turing: https://amturing.acm.org/award_winners/lecun_6017366.cfm  
- Bengio Turing: https://amturing.acm.org/award_winners/bengio_3406375.cfm  
- Valiant PAC (learning theory ancestor): https://amturing.acm.org/award_winners/valiant_2612174.cfm  

Complete URL bibliography: `research/video-research/deep-learning-trio/references.md`.

## References


### Video research pack (all URLs)

Complete list: `research/video-research/deep-learning-trio/references.md`.

1. Hinton Turing — https://amturing.acm.org/award_winners/hinton_4791679.cfm  
2. LeCun Turing — https://amturing.acm.org/award_winners/lecun_6017366.cfm  
3. Bengio Turing — https://amturing.acm.org/award_winners/bengio_3406375.cfm  
4. ACM 2018 Turing announcement — https://awards.acm.org/about/2018-turing  
5. Wikipedia — Deep learning — https://en.wikipedia.org/wiki/Deep_learning  
6. Wikipedia — Backpropagation — https://en.wikipedia.org/wiki/Backpropagation  
7. Wikipedia — Convolutional neural network — https://en.wikipedia.org/wiki/Convolutional_neural_network  
8. Valiant PAC (learning theory ancestor) — https://amturing.acm.org/award_winners/valiant_2612174.cfm  
9. Course cross: Ch.6 Math of AI — contents/en/chapter06/  
10. Research pack folder: `research/video-research/deep-learning-trio/`.

1. ACM Turing Award 2018 — Bengio, Hinton, LeCun — [amturing.acm.org](https://amturing.acm.org/).  
2. Canonical surveys/textbooks: Goodfellow–Bengio–Courville *Deep Learning*; historical LeNet papers; modern transformer paper as primary source for attention architecture.  
3. Course: [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/); [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/); [Valiant]({{ site.baseurl }}/contents/en/chapter09/09_09_Valiant_Learning/).

---

## Further directions

- Reproduce a tiny autodiff example by hand (two layers, one loss).  
- Read one section of Goodfellow et al. on regularization and compare to ML theory bounds.  
- Track a scaling-law paper and separate fit curves from causal claims about intelligence.  
- After Pearl: write when a recommender system’s offline accuracy misleads under intervention.  
- Next: [Wigderson]({{ site.baseurl }}/contents/en/chapter09/09_13_Wigderson_Complexity/)—randomness and proofs, a different Turing mountain.

## Video tham khảo

- **xem trước** — [ACM A.M. Turing Award 2018: Yoshua Bengio, Yan Lecun and Geoffrey Hinton](https://www.youtube.com/watch?v=HzilDIhWhrE) — Association for Computing Machinery (ACM), English. Watch first. “ACM A.M. Turing Award 2018: Yoshua Bengio, Yan Lecun and Geoffrey Hinton” orients the lesson’s aim: After this lecture you should be able to write a layer map x\mapsto\sigma(Wx+b) and describe a deep net as composition; explain training as empirical risk minimization with gradien…
- [Geoffrey Hinton and Yann LeCun, 2018 ACM A.M. Turing Award Lecture "The Deep Learning Revolution"](https://www.youtube.com/watch?v=VsnQf7exv5I) — Association for Computing Machinery (ACM), English. A second pass once the main claim is in view: After this lecture you should be able to write a layer map x\mapsto\sigma(Wx+b) and describe a deep net as composition; explain training as empirical risk minimization with gradien…
- [AAAI 20 / AAAI 2020 Keynotes Turing Award Winners Event / Geoff Hinton, Yann Le Cunn, Yoshua Bengio](https://www.youtube.com/watch?v=UX8OubxsY8w) — ICML IJCAI ECAI 2018 Conference Videos, English. Further depth after the first two, still tied to this lesson: After this lecture you should be able to write a layer map x\mapsto\sigma(Wx+b) and describe a deep net as composition; explain training as empirical risk minimization with gradien…
