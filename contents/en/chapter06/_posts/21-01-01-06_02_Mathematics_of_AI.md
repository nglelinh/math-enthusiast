---
layout: post
title: "Mathematics of AI"
chapter: '06'
order: 2
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

A large language model answers a question in under a second. Behind that answer sit vectors in thousands of dimensions, matrices with billions of parameters, a loss surface nobody can draw, and a training process that is **optimization under uncertainty**. Modern AI systems are engineering products—and **mathematical objects**. This flagship lecture maps the mathematics that underwrites deep learning and the questions that remain open, without pretending the subject is settled theory.

The skill to practice here is **frontier literacy**: separating theorems, empirical regularities, heuristics, and marketing claims. Scale and clever engineering matter; so do linear algebra, probability, optimization, and high-dimensional geometry. The point is not to “solve AI” in one essay, but to see **what kind of mathematics is actually doing the work**.

---

## Learning objectives

After this lecture you should be able to:

- Describe a basic neural net as **composition of linear maps and nonlinearities** on vector spaces, and write a single layer as $$x \mapsto \sigma(Wx+b)$$.
- Explain **training** as numerical minimization of a loss over parameters, including the role of gradients and backpropagation as organized chain rule.
- Distinguish **empirical risk** (fit on training data) from **true risk** (expected loss on new data), and name why that gap is the heart of learning theory.
- Name at least four mathematical areas feeding ML (linear algebra, probability/statistics, optimization, high-dimensional geometry or approximation theory)—with one sentence each on *how*.
- List three **open mathematical questions** about deep learning that are not product features.
- Critique a popular AI claim using a precision-vs-hype restatement (theorem vs measurement vs speculation).

**Prerequisites.** Vectors and matrices at a conceptual level; derivatives as local rates of change; basic probability language (expectation, sampling). No production ML engineering experience is required.

---

## 1. Data lives in high-dimensional space

A grayscale image of size $$28\times 28$$ is a vector in $$\mathbb{R}^{784}$$. A color video frame, a token embedding, or a gene-expression profile is a vector in a higher ambient space. A dataset is a cloud of such points; a batch is a matrix. **Linear algebra** is the native language of those spaces: bases, projections, singular values, low-rank structure, and linear maps.

**Mechanism (one step).** Principal component analysis and the singular value decomposition find directions of largest variance so one can compress or denoise by projecting onto a principal subspace. If $$X$$ is a data matrix, the leading right singular vectors of a centered version of $$X$$ are the principal directions.

High dimension is not “more of the same coordinates.” Concentration of measure, typical sets, and the geometry of high-dimensional spheres change distance and angle intuition: most mass of a high-dimensional ball sits near the equator of a thin shell; random vectors are nearly orthogonal with high probability. Those facts feed modern stories about overparameterized models and about why naive nearest-neighbor geometry can mislead. (See the high-dimensional geometry lecture in this chapter for a sharper treatment.)

---

## 2. Models as functions built from simple pieces

A fully connected layer is a linear map followed by a coordinatewise nonlinearity:

$$
x \mapsto \sigma(Wx + b),
$$

with weight matrix $$W$$, bias $$b$$, and activation $$\sigma$$ (ReLU, GELU, sigmoid, …). A deep network **composes** many such layers. Convolutional nets reuse local linear filters with translation structure; residual connections rewrite a layer as $$x \mapsto x + f_\theta(x)$$; transformers implement **attention** as structured maps involving queries, keys, and values—bilinear forms and softmax-normalized weights that mix tokens as a data-dependent linear combination.

**Universal approximation (theorem vs practice).** Under mild conditions, shallow networks with enough width can approximate broad classes of continuous functions on compact sets (classical universal approximation theorems). That is a **representation** result: it says *there exist* parameters that approximate a target, not that gradient descent finds them efficiently. Depth changes *efficiency* of representation and inductive bias. The theory of *why deep often beats wide in practice* is subtler and still developing—approximation theory, harmonic analysis of compositions, and empirical scaling all contribute pieces.

![Math pipeline under ML]({{ site.baseurl }}/img/chapter_img/ai_math_pipeline.svg)

*Figure. Conceptual stack from data geometry to open theory (illustration if present in the course assets).*

---

## 3. Learning as optimization

Training chooses parameters $$\theta$$ to reduce a **loss** $$L(\theta)$$ that measures prediction error on data (often with regularizers or architectural constraints). A standard template is empirical risk minimization:

$$
\hat\theta \in \arg\min_\theta \frac{1}{n}\sum_{i=1}^n \ell\bigl(f_\theta(x_i), y_i\bigr),
$$

where $$\ell$$ is a pointwise loss (squared error, cross-entropy, …) and $$f_\theta$$ is the model.

**Gradient descent** and its stochastic variants move parameters opposite an estimate of the gradient:

$$
\theta_{t+1} = \theta_t - \eta \widehat{\nabla L}(\theta_t).
$$

Backpropagation is the chain rule organized for computational graphs: automatic differentiation yields exact gradients of the composed map with respect to each weight, up to floating-point arithmetic.

![Loss landscape cartoon]({{ site.baseurl }}/img/chapter_img/ai_loss_landscape.svg)

*Figure. Nonconvex loss landscapes: many basins; practice still finds useful ones.*

**What optimization mathematics asks.** When do methods converge? How do step sizes, momentum, and adaptive methods (Adam and relatives) behave? What is the role of batch size and noise? In deep learning, landscapes are nonconvex and enormous; classical **convex** guarantees rarely apply directly—yet empirically SGD-type methods often find parameters that work. Explaining that gap is a **research program**, not a slogan. Continuous-time limits (gradient flow), mean-field and NTK regimes, and landscape geometry (saddle points, basins, implicit bias) are active interfaces between analysis, probability, and practice.

---

## 4. Probability, statistics, and generalization

Data are modeled as samples from an unknown distribution $$\mathcal{D}$$. **True risk** is expected loss on a fresh sample; **empirical risk** averages loss on the training set. The central drama of learning is:

> Low training loss does not automatically mean low true risk.

Classical statistical learning theory bounds the generalization gap using complexity measures such as VC dimension and Rademacher complexity: roughly, if a hypothesis class is “small,” fitting the sample controls expected risk with high probability. Modern deep nets are heavily **overparameterized**—they can interpolate noisy labels—yet often generalize under structured real data. Phenomena such as **double descent** challenge simple “bias–variance U-curve” folklore that treats more parameters as pure overfitting. This is core **precision-vs-hype** territory: many popular explanations are incomplete or regime-specific.

**Probability also enters** as stochastic gradients, Bayesian and PAC-Bayesian views, calibration of predictive probabilities, and generative modeling (likelihoods, divergences, score matching, and links to optimal transport). Generative models learn *distributions*, not only decision boundaries; the mathematics is that of measures on high-dimensional spaces.

---

## 5. Other mathematical threads (map, not encyclopedia)

| Area | Role in AI/ML |
|------|----------------|
| Information theory | Cross-entropy loss, compression, mutual information heuristics for representation |
| Dynamical systems | Training trajectories; continuous-time limits of residual nets and optimizers |
| Harmonic analysis / approximation theory | Which functions are efficiently represented by compositions or kernels |
| Game theory | Adversarial training; GANs as idealized equilibrium problems |
| Causal inference | Beyond i.i.d. prediction—interventions, robustness, policy |
| Logic and formal methods | Specification, verification, and alignment constraints (nascent relative to scale) |
| Optimal transport | Distances between distributions; generative and domain-adaptation ideas |
| High-dimensional geometry | Concentration, random projections, geometry of embeddings |

You need not master all. You should see AI as a **consumer of many fields**, not a replacement for them. Linear algebra and calculus remain the daily tools; probability and optimization set the training story; geometry and statistics set the generalization story.

---

## 6. What is still mathematically open (honest list)

Formulations evolve; the list below is literacy, not a complete research agenda.

1. **Generalization of overparameterized nets.** Why does interpolating noise still predict well under realistic data structure? Classical capacity bounds are often vacuous at modern widths.
2. **Implicit bias of optimizers.** Among many zero-training-loss solutions, which does SGD (or Adam) select, and why does that selection help generalization?
3. **Feature learning vs kernels.** When do deep nets escape “lazy” or neural-tangent-kernel regimes and learn hierarchical features from data?
4. **Robustness and adversaries.** Small input perturbations can flip predictions; the geometry of decision boundaries and certified robustness remain hard.
5. **Scaling laws.** Empirical regularities of loss versus compute, data, and parameters are striking; full theoretical derivation remains partial.
6. **Foundation-model behavior.** In-context learning, long-context reasoning, and “emergence” claims mix measurement, definitional ambiguity, and marketing—separate carefully.

A seminar-ready stance: **empirical regularity ≠ theorem ≠ product claim.**

---

## 7. Hype vs precision (workshop material)

| Overclaim (common) | More precise restatement |
|--------------------|---------------------------|
| “Neural nets work like the brain.” | Loose analogies exist; architecture, learning rules, and embodiment differ deeply. |
| “We solved intelligence.” | Strong narrow-task performance ≠ general intelligence or reliable agency. |
| “No math left—only scale.” | Scale and data matter enormously; theory of generalization, robustness, and efficiency is unfinished. |
| “Loss going down means understanding.” | Training metrics ≠ conceptual understanding, causal competence, or safety. |
| “Attention *is* all you need as a scientific theory.” | Transformers are a successful architecture class; the slogan is not a completeness theorem for cognition. |

When you critique a popular AI article, demand four answers: **What is the mathematical object? What is proved? What is measured? What is speculated?**

---

## 8. From theory to practice: a minimal mechanism chain

One clean chain for LO-style writing:

**Data as vectors** → **model as composed maps** $$f_\theta$$ → **loss** measuring error → **gradient estimates** via backprop → **parameter update** → **deployed predictor** evaluated on held-out risk and task metrics.

Each arrow is a place where mathematics can go wrong or be improved: bad features, misspecified loss, vanishing/exploding gradients, distribution shift, or evaluation on the wrong metric. Engineering stacks (frameworks, GPUs, data pipelines) implement this chain at scale; they do not abolish it.

Cross-links in this course: linear algebra and optimization in applications chapters; high-dimensional geometry, ML theory, and optimal transport later in this chapter; cryptographic and complexity frontiers when security and hardness matter.

### A short worked narrative: training a classifier

Suppose we classify email as spam or not. Each email becomes a feature vector $$x\in\mathbb{R}^d$$ (bag-of-words counts, embeddings, …). A logistic model uses

$$
\mathbb{P}(Y=1\mid x)=\sigma(w^\top x+b),\qquad
\sigma(z)=\frac{1}{1+e^{-z}},
$$

with binary cross-entropy loss. Gradient descent updates $$(w,b)$$ using averages over a mini-batch. Already every major mathematical character has appeared: vectors and inner products; a nonlinear link function; a probabilistic loss; stochastic optimization; and evaluation on a held-out risk estimate.

Replace the linear map with a deep net and the same skeleton remains—only the hypothesis class, optimization landscape, and compute graph grow. That continuity is why “mathematics of AI” is not a new subject that abolishes linear algebra; it is linear algebra, probability, and optimization under new scales and architectures.

### Evaluation literacy

Accuracy on a test set is an **empirical estimate**, not a PAC bound. Calibration, subgroup performance, robustness to shift, and adversarial risk are different mathematical targets. Leaderboard culture optimizes what is measured; theory reminds you what is *not* measured. When a press release says “human-level,” ask: on which distribution, which metric, which contamination controls, which uncertainty?

---

## Common confusions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “AI is only statistics.” | Incomplete | Statistics is central; so are optimization, linear algebra, and approximation theory. |
| “Gradient descent always finds the global minimum.” | False in general | Nonconvex landscapes; practice often finds *useful* critical points, not proven global optima. |
| “More parameters always overfit.” | Classical folklore | Modern overparameterized regimes can interpolate yet generalize; architecture and optimizer matter. |
| “Universal approximation explains deep learning success.” | Overstated | Existence of good parameters ≠ efficient findability or good inductive bias. |
| “Theory must finish before engineering is legitimate.” | False history | Flight preceded full Navier–Stokes control; still, theory reduces risk and guides design. |
| “Scaling laws are theorems.” | Usually not | Often empirical fits; theoretical explanations are partial and model-dependent. |

---

## Exercises

1. **Warm-up.** Write a $$2\times 2$$ matrix–vector product by hand; interpret it as a linear layer without bias.
2. **Definitions.** Define empirical risk and true risk; give one sentence on why they can diverge.
3. **Mechanism (≤250 words).** Chain: data → model → loss → gradient update → deployed predictor. Name one mathematical failure mode at each step.
4. **Three fields.** One sentence each: how linear algebra, probability, and optimization appear when training a classifier.
5. **Precision vs hype.** Find a news claim about AI; rewrite it in two sentences separating measurement from speculation.
6. **Open question literacy.** Pick one item from Section 6; write a falsifiable *empirical* question and a *mathematical* question related to it (they need not be the same).
7. **Stretch.** Skim an abstract on double descent or neural tangent kernels; list three terms to look up and one claim that is theorem-shaped versus one that is experiment-shaped.

---


---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/mathematics-of-ai/analysis.md`.

### Status

**Active research field.** Core engineering practice is mature; mathematical understanding of deep learning (generalization, optimization landscapes, feature learning) remains partial as of 2026.

### Core statement / slogan

Universal approximation (classical) is a *representation* theorem, not a training theorem. Training is empirical risk minimization via SGD on nonconvex $$L(\theta)$$. Generalization of overparameterized nets is not settled by classical VC alone.

### Definitions to freeze

- **Layer map.** $$x\mapsto \sigma(Wx+b)$$ with nonlinearity $$\sigma$$.
- **Empirical risk.** $$\frac1n\sum_i \ell(f_\theta(x_i),y_i)$$ vs true risk $$\mathbb{E}\ell$$.

### Hygiene (from confusions log)

- Universal approximation ⇒ training finds the approximator.
- Equating product demos with mathematical theorems.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/mathematics-of-ai/`.

**Recommended order**

1. **Orientation** — 3Blue1Brown — But what is a neural network?: [https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk).  
2. **Core** — 3Blue1Brown — Gradient descent, how neural networks learn: [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w).  
3. **Core** — 3Blue1Brown — What is backpropagation really doing?: [https://www.youtube.com/watch?v=Ilg3gGewQ5U](https://www.youtube.com/watch?v=Ilg3gGewQ5U).  
4. **Foundation** — 3Blue1Brown — Backpropagation calculus: [https://www.youtube.com/watch?v=tIeHLnjs5U8](https://www.youtube.com/watch?v=tIeHLnjs5U8).  
5. **Meta** — 3Blue1Brown Neural Networks playlist: [https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi).  

**Status reminder:** **Active research field.** Core engineering practice is mature; mathematical understanding of deep learning (generalization, optimization landscapes, feature learning) remains partial as of 2026.

---



### Transcript & frames (flagship extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/mathematics-of-ai/transcripts/` · status: `research/video-research/mathematics-of-ai/TRANSCRIPT_STATUS.md` · master list: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Captions are auto-downloaded (yt-dlp); treat as navigation aids, not as a substitute for the lesson text.


![Flagship video sample frame]({{ site.baseurl }}/img/video_research/flagships/ai_3b1b_nn_frame01.jpg)

*Figure. Sample still from a primary flagship video (see pack for timestamps).*

## References and further reading

1. I. Goodfellow, Y. Bengio, and A. Courville. *Deep Learning*. MIT Press — conceptual backbone (layers, training, regularization).
2. Survey courses and notes on generalization of deep networks (rapidly evolving; prefer recent graduate surveys over older blog folklore).
3. Classical learning theory: Vapnik’s statistical learning framework; modern expositions of Rademacher complexity.
4. Neural tangent kernel and mean-field limits — research literature on lazy vs feature-learning regimes.
5. Course links: [Linear algebra → AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/), [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/), [High-dimensional geometry]({{ site.baseurl }}/contents/en/chapter06/06_08_High_Dimensional_Geometry/), [Optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/).

*Literacy note.* Product demos and press releases are not theorems. Prefer primary papers and careful surveys when a claim is load-bearing for your argument.

---


Full URL bibliography from video research: `research/video-research/mathematics-of-ai/references.md`.

### Videos (recommended path)

- 3Blue1Brown — But what is a neural network? (ORIENTATION): https://www.youtube.com/watch?v=aircAruvnKk
- 3Blue1Brown — Gradient descent, how neural networks learn (CORE): https://www.youtube.com/watch?v=IHZwWFHWa-w
- 3Blue1Brown — What is backpropagation really doing? (CORE): https://www.youtube.com/watch?v=Ilg3gGewQ5U
- 3Blue1Brown — Backpropagation calculus (FOUNDATION): https://www.youtube.com/watch?v=tIeHLnjs5U8
- 3Blue1Brown Neural Networks playlist (META): https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi

### Papers and web (from research pack)

- Goodfellow, Bengio, Courville — Deep Learning (book site): https://www.deeplearningbook.org/
- Wikipedia — Universal approximation theorem: https://en.wikipedia.org/wiki/Universal_approximation_theorem
- Double descent literature hub (Belkin et al. 2019): https://arxiv.org/abs/1812.11118
- 3Blue1Brown site: https://www.3blue1brown.com/
- Wikipedia — Deep learning: https://en.wikipedia.org/wiki/Deep_learning

### Course

- Research pack: `research/video-research/mathematics-of-ai/` (especially `references.md`, `learning_path.md`).

## Further directions

- **Next in this chapter:** [Quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/) for a different model of information and computation; [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/) for PAC-style and modern generalization formalisms.
- **Depth on geometry and distributions:** [High-dimensional geometry]({{ site.baseurl }}/contents/en/chapter06/06_08_High_Dimensional_Geometry/) and [Optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/).
- **Applications backbone:** [Linear algebra → AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/) if you want the matrix toolkit emphasized.
- **Practice:** train a tiny model (even logistic regression or a two-layer net) and log train vs test curves; annotate where the mathematical story of Section 4 becomes visible.
- **Seminar stance:** keep a running table of claims labeled *theorem / bound / empirical law / hype*.
