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

**Yoshua Bengio**, **Geoffrey Hinton**, and **Yann LeCun** shared the **A.M. Turing Award 2018** for conceptual and engineering breakthroughs that made **deep neural networks** a dominant paradigm in machine learning. The citation is not “they invented AI.” It is that a long winter of neural-network research—backpropagation culture, convolutional architectures, representation learning, and persistent scientific bets—became the foundation of modern practice when data, compute, and algorithmic refinements aligned.

This lecture is a **foundations and literacy** piece for Math Enthusiast: how layered models compose linear maps and nonlinearities; what backpropagation is as organized calculus; how CNNs, sequence models, and (lightly) transformers instantiate inductive biases; what “representation learning” claims; and how to practice LO6—**hype versus theorem**—using the same muscles as [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/) and [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/). Official materials: [amturing.acm.org](https://amturing.acm.org/).

---

## Learning objectives

After this lecture you should be able to write a layer map $$x\mapsto\sigma(Wx+b)$$ and describe a deep net as composition; explain training as empirical risk minimization with gradient-based updates and backpropagation as chain rule on a computational graph; name CNN, RNN/sequence, and transformer inductive biases at slogan level; define representation learning as learning features rather than only hand-crafting them; and rewrite one popular deep-learning claim into a precise statement about benchmarks, assumptions, or open theory (LO6).

**Prerequisites / seminar links.** Vectors/matrices; derivatives as local linear approximation; basic probability. Flagship twins: [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/), [optimization applications]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/). Chapter hub: [Turing overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/).

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

## 5. Hype versus theorem (LO6 workshop)

Practice rewriting claims:

| Hype form | More precise form |
|-----------|-------------------|
| “Deep learning solves intelligence.” | “Deep nets achieve high scores on specified benchmarks under stated training regimes; general intelligence is undefined/unproven here.” |
| “Backprop is how the brain learns.” | “Backprop is an efficient computational method for gradients; biological credit assignment is a separate scientific question.” |
| “Theory cannot explain deep learning, so theory is useless.” | “Classical capacity bounds can be vacuous; algorithm- and data-dependent theories are active research, not absence of mathematics.” |
| “Scale is all you need” (absolute). | “Empirical scaling laws describe trends on measured metrics within regimes; they are not theorems about all tasks or safety properties.” |

LO6 skill: cite **what was measured**, **what was assumed**, and **what remains open**. Turing 2018 honors foundations of a technology family; it does not close the mathematics of AI.

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

Next-token prediction and related pretext tasks turn raw sequences into training signal. That is still empirical risk minimization on a surrogate loss; the “foundation” metaphor means transfer to many downstream tasks after large-scale pretraining. Mathematically, one should still ask about distribution shift, calibration, causal misuse, and the gap between benchmark suites and deployment worlds—the same LO6 checklist as in [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/).

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

## Exercises

1. Write a two-layer network explicitly as nested maps with matrices $$W_1,W_2$$.  
2. In one paragraph, explain backpropagation as chain rule + computational graph.  
3. What inductive bias does weight sharing in a CNN encode?  
4. Empirical risk vs true risk: why can a net with near-zero training loss still fail in deployment?  
5. **LO6 (≤200 words):** Rewrite a breathless popular paragraph about “AI understanding” into measurable claims.  
6. Name one open mathematical question about deep learning (optimization, generalization, or approximation).  
7. Connect next-token prediction to representation learning in two sentences.  
8. Skim the 2018 Turing pages at [amturing.acm.org](https://amturing.acm.org/); list one contribution associated with each of Bengio, Hinton, and LeCun.

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
