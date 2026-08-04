---
layout: post
title: "Linear Algebra → AI & Machine Learning"
chapter: '03'
order: 3
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
lesson_type: required
---

A neural network does not “think in words” inside the GPU. It multiplies matrices, adds biases, applies simple nonlinearities, and repeats. Recommendation systems, image classifiers, language models, and PCA dashboards all speak the same mother tongue: **vectors, matrices, and linear maps**—with nonlinear spices.

**Path:** data as geometry → linear layers → depth and nonlinearity → SVD/PCA → gradients on parameters → structured maps (conv, attention) → what linear algebra does *not* explain → confusions.

This lecture maps the **mechanism chain** from abstract linear algebra to deployed machine learning—not “AI uses math” as a slogan, but *which* operations power training and inference.

---

## Learning objectives

After this lecture you should be able to:

- Interpret examples as vectors and datasets as matrices; interpret similarity via inner products and norms.
- Explain a linear layer $$x\mapsto Wx+b$$ and why composition of linear maps collapses without nonlinearities.
- State what the **singular value decomposition (SVD)** and **PCA** reveal (principal directions, compression, low-rank structure).
- Connect training to multivariable calculus: loss as a function of parameters, gradients, and chain rule (backprop).
- Describe convolution and attention as structured linear (or bilinear) operations.
- Avoid “AI is magic,” “AI is only statistics,” and “deeper always means smarter linear algebra.”

**Prerequisites.** Matrix multiplication, basic derivatives. Helpful: eigenvalues as “stretch factors along special directions.”

**Seminar links.** [Mathematics of AI (Ch.6)]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [Probability → data science]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/).

---

## 1. Data as geometry

A grayscale $$28\times 28$$ image is a vector in $$\mathbb{R}^{784}$$. A sentence embedding is a vector in $$\mathbb{R}^d$$. A batch of $$n$$ examples with $$d$$ features is a matrix $$X\in\mathbb{R}^{n\times d}$$. Once data lives in a vector space, **distance**, **angle**, **projection**, and **subspace** become natural languages for similarity and structure.

The inner product $$\langle u,v\rangle=u^\top v$$ measures alignment. Cosine similarity is the angle story used in retrieval and embeddings. Linear transformations $$x\mapsto Ax$$ rotate, stretch, shear, and project. Learning often means *choosing* transformations so that classes separate or reconstructions stay faithful.

**Mechanism slogan.**  
*Machine learning turns messy raw inputs into vectors, then learns maps on those vectors that make a task geometrically easy.*

---

## 2. The linear layer: affine maps as atoms

A basic neural layer is

$$
x \mapsto \sigma(Wx + b),
$$

where $$W\in\mathbb{R}^{m\times d}$$ is a weight matrix, $$b\in\mathbb{R}^m$$ a bias, and $$\sigma$$ a coordinatewise nonlinearity (ReLU, GELU, sigmoid, …). The map $$x\mapsto Wx+b$$ is **affine**—linear plus translation.

**Without** $$\sigma$$, stacking layers collapses:

$$
W_2(W_1 x+b_1)+b_2 = (W_2W_1)x + (W_2b_1+b_2),
$$

still a single affine map. **With** $$\sigma$$, composition becomes highly expressive: depth creates hierarchical features rather than one flat linear transform.

**Why this powers technology.** Inference is a long chain of matrix multiplies and cheap nonlinearities—operations that map onto GPUs and TPUs with extreme efficiency. The “AI hardware boom” is partly a linear-algebra hardware boom.

---

## 3. Depth, features, and representation

Early layers in vision models respond to edges and textures; later layers respond to parts and objects—empirically, not by magic. Algebraically, each layer re-embeds the previous representation:

$$
h^{(\ell+1)} = \sigma\bigl(W^{(\ell)} h^{(\ell)} + b^{(\ell)}\bigr).
$$

The final layer often is linear (or softmax-linear) for classification: scores $$Wh+b$$ over classes. Softmax turns scores into a probability vector; the linear algebra produced the scores.

**Universal approximation** theorems say shallow wide networks can approximate continuous functions on compact sets, but depth often yields better *inductive bias* and parameter efficiency for the same accuracy. Linear algebra alone does not pick the architecture; it *implements* whatever architecture you chose.

---

## 4. SVD, PCA, and low-rank structure

Any real matrix $$A\in\mathbb{R}^{m\times n}$$ admits a **singular value decomposition**

$$
A = U\Sigma V^\top,
$$

with orthogonal $$U,V$$ and nonnegative diagonal singular values in $$\Sigma$$. Truncating small singular values yields the best low-rank approximation in Frobenius (and spectral) norm—the **Eckart–Young** theorem.

**PCA** is the data cousin: center the data matrix, form a covariance (or work via SVD of the data matrix), and take top singular vectors as principal directions of variance. Compression, denoising, and exploratory visualization all ride this fact:

$$
\text{keep the directions where data varies most; discard near-null directions.}
$$

**Mechanism.**  
*High-dimensional data often concentrates near low-dimensional structure; SVD/PCA finds those axes as an optimization problem with a closed-form spectral answer.*

In recommender systems, user–item matrices are approximated as low-rank products $$UV^\top$$—collaborative filtering as linear algebra. In word embeddings and topic models, similar low-rank and factorization ideas recur.

---

## 5. Gradients: calculus on parameter space

Training chooses parameters $$\theta$$ (all weights and biases) to minimize a **loss** $$L(\theta)$$ averaged over data—for example cross-entropy for classification or squared error for regression.

A gradient step is

$$
\theta \leftarrow \theta - \eta \nabla_\theta L(\theta).
$$

Because $$L$$ is a composition of matrix multiplies and elementary nonlinearities, the **chain rule** computes $$\nabla_\theta L$$ layer by layer: **backpropagation**. No new mathematics beyond multivariable calculus—but the *graph* of computation is huge, so automatic differentiation engines matter.

**Link to this chapter.** Optimization theory studies when gradient methods converge, how step sizes behave, and what happens in nonconvex landscapes ([Optimization lecture]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/)). Probability enters when data are random and we care about **risk** (expected loss) rather than one finite sample ([Probability]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/)).

**Mechanism.**  
*Learning is optimization of a scalar loss on a high-dimensional parameter space; gradients are the local linear algebra of that scalar.*

**Shapes that matter in practice.** A mini-batch of inputs is a matrix; a linear layer is a matrix multiply (or a batched GEMM). Automatic differentiation engines track how each tensor depends on parameters so that one backward pass yields every partial derivative needed for the update. Numerical stability (vanishing/exploding gradients, mixed precision) is still linear algebra plus floating-point culture—condition numbers and scaling, not mysticism.

---

## 6. Structured linear maps: convolution and attention

Not every matrix is dense and unstructured.

**Convolution** (for images, audio) is a linear map with **shared local filters**: the same small kernel applied at every location. In matrix language it is highly structured (Toeplitz/circulant blocks). Parameter count stays small; translation equivariance is built in.

**Self-attention** (transformers) mixes tokens by

$$
\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\Bigl(\frac{QK^\top}{\sqrt{d}}\Bigr)V,
$$

where $$Q,K,V$$ are linear projections of the input. The product $$QK^\top$$ is bilinear in the data; softmax produces mixing weights; multiply by $$V$$ is another linear combination. The mechanism is still linear algebra plus a normalized nonlinearity—scalable sequence modeling without classical recurrence.

**Sparse and graph structure.** Graph neural networks replace dense $$W$$ with message passing along edges—linear maps that respect network topology (bridge to [Graph Theory]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/)).

---

## 7. Eigenviews: stability, modes, and kernels

Eigenvalues and eigenvectors appear when dynamics or quadratic forms matter:

- Linearized residual networks and recurrent nets: powers $$A^t$$ and spectral radius.
- Graph Laplacians: smoothness of signals on networks; spectral clustering.
- Kernel methods: Gram matrices $$K_{ij}=k(x_i,x_j)$$; learning in feature spaces without writing features explicitly.
- Gaussian covariance: principal axes of uncertainty ellipsoids.

You do not need a full spectral theory course to use PyTorch—but when training diverges, representations collapse, or a graph smoother oversmooths, spectral intuition is the debugging language.

---

## 8. What linear algebra does not finish

Linear algebra is necessary, not sufficient:

1. **Statistics / probability** — generalization, calibration, causal claims.  
2. **Optimization** — algorithms, learning rates, implicit bias of SGD.  
3. **Hardware and systems** — memory layouts, quantization, distributed training.  
4. **Data and objectives** — labels, rewards, human feedback; no matrix multiplies invent values.  
5. **Nonlinear phenomena** — chaos of training dynamics, emergent behaviors, adversarial examples.

Chapter 6’s [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/) returns to theory frontiers. Here the claim is narrower and firmer: **the computational substrate of modern ML is linear algebra with nonlinear glue**.

---

## 9. A minimal end-to-end picture

1. Encode inputs as vectors.  
2. Apply learned affine maps + nonlinearities (and structured variants).  
3. Read out predictions via a final linear map.  
4. Measure loss; backpropagate gradients; update parameters.  
5. Optionally compress or analyze representations with SVD/PCA.

Every “AI product” that classifies, ranks, embeds, or generates through neural nets executes some elaboration of this loop. The pure mathematics of vector spaces, duals, and spectral theorems is older than silicon; the industry is a colossal consumer of those ideas at scale.

---

### Linear algebra as ML substrate (from video research)

Recommended path: 3Blue1Brown [neural network](https://www.youtube.com/watch?v=aircAruvnKk) → [gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) → [backprop](https://www.youtube.com/watch?v=Ilg3gGewQ5U), plus Strang [18.06 Lec 1](https://www.youtube.com/watch?v=J7DzL2_Na80).

- A deep net without nonlinearities is still one affine map $$x\mapsto Wx+b$$.
- Training is (stochastic) gradient descent on a high-dimensional loss; backprop evaluates those gradients efficiently.
- SVD/PCA remain the linear baseline for compression and denoising before nonlinear representation learning.

## Common confusions

| Claim | Correction |
|-------|------------|
| “Neural nets are just linear regression.” | Layers are affine *plus* nonlinearities; depth matters because of those nonlinearities. |
| “PCA is unsupervised learning’s only tool.” | PCA is a linear baseline; modern representation learning is nonlinear and task-driven. |
| “More dimensions always help.” | High dimension brings geometry curses; structure and regularization matter. |
| “Backprop is a new kind of math.” | It is systematic chain rule / reverse-mode automatic differentiation. |
| “Attention is not linear algebra.” | Core mixing is matrix products + softmax; still linear-algebra-centric. |
| “If it multiplies matrices, it understands.” | Computation ≠ semantics; evaluation and alignment are separate problems. |

---

## Exercises

1. **Warm-up.** Let $$W=\begin{pmatrix}1&2\\0&1\end{pmatrix}$$, $$x=\begin{pmatrix}1\\1\end{pmatrix}$$. Compute $$Wx$$. What geometric effect does $$W$$ have?  
2. **Collapse.** Prove that a composition of affine maps is affine. Why does that force nonlinearities between layers?  
3. **PCA slogan.** In two sentences, why do top principal components maximize captured variance?  
4. **Gradient step.** If $$L(\theta)=(\theta-3)^2$$ and $$\eta=0.1$$, perform two gradient updates from $$\theta_0=0$$.  
5. **Mechanism sentence.** Write one sentence linking GPU matrix multiplies to neural inference.  
6. **Architecture literacy.** Is a $$3\times 3$$ convolution a sparse structured linear map? Explain.  
7. **Stretch.** For a centered data matrix $$X$$, relate the right singular vectors of $$X$$ to eigenvectors of $$X^\top X$$.

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/linear-algebra-ai/`.

**Recommended order**

1. **ORIENTATION** — 3Blue1Brown — But what is a neural network?: [https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk).
2. **CORE** — 3Blue1Brown — Gradient descent, how neural networks learn: [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w).
3. **CORE** — 3Blue1Brown — What is backpropagation really doing?: [https://www.youtube.com/watch?v=Ilg3gGewQ5U](https://www.youtube.com/watch?v=Ilg3gGewQ5U).
4. **FOUNDATION** — 3Blue1Brown — Essence of linear algebra (playlist): [https://www.3blue1brown.com/topics/linear-algebra](https://www.3blue1brown.com/topics/linear-algebra).
5. **FOUNDATION** — 3Blue1Brown — Essence of linear algebra ch.1 (vectors): [https://www.youtube.com/watch?v=fNk_zzaMoSs](https://www.youtube.com/watch?v=fNk_zzaMoSs).
6. **FOUNDATION** — MIT OCW 18.06 Strang — Geometry of linear equations: [https://www.youtube.com/watch?v=J7DzL2_Na80](https://www.youtube.com/watch?v=J7DzL2_Na80).

Complete URL bibliography: `research/video-research/linear-algebra-ai/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/linear-algebra-ai/transcripts/` · status: `research/video-research/linear-algebra-ai/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/linear-algebra-ai_aircAruvnKk_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/linear-algebra-ai/references.md`.

### Videos (primary path)

1. 3Blue1Brown — But what is a neural network? — https://www.youtube.com/watch?v=aircAruvnKk
2. 3Blue1Brown — Gradient descent, how neural networks learn — https://www.youtube.com/watch?v=IHZwWFHWa-w
3. 3Blue1Brown — What is backpropagation really doing? — https://www.youtube.com/watch?v=Ilg3gGewQ5U
4. 3Blue1Brown — Essence of linear algebra (playlist) — https://www.3blue1brown.com/topics/linear-algebra
5. 3Blue1Brown — Essence of linear algebra ch.1 (vectors) — https://www.youtube.com/watch?v=fNk_zzaMoSs
6. MIT OCW 18.06 Strang — Geometry of linear equations — https://www.youtube.com/watch?v=J7DzL2_Na80
7. MIT OCW 18.06 playlist (Strang) — https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8
8. MIT OCW 18.06 course page — https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
9. 3Blue1Brown neural networks playlist — https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi

### Videos (secondary finds)

10. Stanford CS229 / related ML theory lectures (optional survey) — https://www.youtube.com/@stanfordonline

### Papers, books, OCW, and web

11. Vaswani et al. — Attention Is All You Need (2017): https://arxiv.org/abs/1706.03762
12. Goodfellow, Bengio, Courville — Deep Learning (book site): https://www.deeplearningbook.org/
13. Strang — Linear Algebra and Learning from Data (MIT): https://math.mit.edu/~gs/learningfromdata/
14. Wikipedia — Singular value decomposition: https://en.wikipedia.org/wiki/Singular_value_decomposition
15. 3Blue1Brown linear algebra topic hub: https://www.3blue1brown.com/topics/linear-algebra

### Course

16. Course: [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [Probability]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/), [Math of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [High-dimensional geometry]({{ site.baseurl }}/contents/en/chapter06/06_08_High_Dimensional_Geometry/). Pack: `research/video-research/linear-algebra-ai/`.

## Further directions

- Continue to [Probability → Data Science]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/) for risk and generalization language.  
- Then [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/) for why gradient methods work (and fail).  
- Future-facing theory: [ML Theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/) and [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/).  
- Restate the core mechanism of this essay in one paragraph; note one precise question you still have.
