---
layout: post
title: "High-Dimensional Geometry"
chapter: '06'
order: 8
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

Imagine buying a 100-dimensional orange of radius 10 cm with a peel 1 cm thick. For a familiar 3D orange at the market, the edible pulp makes up over $$72\%$$ of the volume. In 100 dimensions, however, the edible interior shrinks to $$0.9^{100} \approx 0.0027\%$$—meaning **more than 99.997% of the orange is peel**! Even stranger: pick two random arrows in 1000-dimensional space, and with overwhelming probability they will meet at almost a right angle, within a couple of degrees of $$90^\circ$$.

Human brains evolved to navigate two and three dimensions, so everyday geometric intuition routinely betrays us inside $$\mathbb{R}^{1000}$$—the native home of digital images, language embeddings, and neural network weights. **High-dimensional geometry**, paired with concentration of measure, forms the quiet backbone of modern data analysis, compressed sensing, random projections, and statistical learning theory. It does not only unleash “curses”; it also grants surprising gifts, turning random high-dimensional quantities remarkably stable and predictable.

This lecture develops the core effects—thin shells and equators, near-orthogonality of random vectors, Lipschitz concentration, Johnson–Lindenstrauss projections, and links to machine learning—while labeling theorems, heuristics, and hype clearly.

---

## Background Knowledge Map: What Is High-Dimensional Geometry and What Does It Study?

Whereas Euclidean geometry studies triangles, circles, and polyhedra in 2–3 dimensions, **High-Dimensional Geometry** (and Geometric Functional Analysis) studies how volumes, distances, angles, and convex bodies behave in $$\mathbb{R}^n$$ as $$n \to \infty$$. Tightly linked to **High-Dimensional Probability**, it rests on **four pillars**:

1. **Counterintuitive Volume Geometry:** Mass flees the center of a high-dimensional ball into a thin outer shell and narrow equatorial band, while a hypercube sprouts $$2^n$$ sharp corners reaching $$\sqrt{n}$$ times farther than its inscribed sphere.
2. **Concentration of Measure:** A geometric upgrade of the Law of Large Numbers—any smooth (Lipschitz) function of many independent random variables is pinned tightly near its median with high probability.
3. **Metric Embeddings & Random Projections (Johnson–Lindenstrauss):** High-dimensional space is so roomy that projecting $$N$$ points randomly down to $$O(\varepsilon^{-2}\log N)$$ dimensions preserves all pairwise Euclidean distances up to $$1 \pm \varepsilon$$.
4. **Low Intrinsic Dimension & Random Matrices:** Even when data sit in $$\mathbb{R}^n$$, real signals are often sparse or near low-dimensional manifolds—powering compressed sensing and random matrix spectral laws.

---

## Learning objectives

After this lecture you should be able to:

- Explain why most volume of a high-dimensional Euclidean ball lies near its equator/shell, and why that breaks “volume = interior” intuition.
- Compute or estimate typical squared norms and inner products for random vectors with i.i.d. coordinates under basic second-moment reasoning.
- State a **concentration** slogan: Lipschitz functions of many independent variables are nearly constant with high probability.
- Quote the **Johnson–Lindenstrauss** lemma informally: high-dimensional point sets embed into $$O(\varepsilon^{-2}\log N)$$ dimensions preserving pairwise distances up to $$1\pm\varepsilon$$.
- Connect high-d geometry to nearest neighbors, curse of dimensionality, and random features—without claiming dimension reduction always works.
- Critique “curse of dimensionality” as a single phrase covering multiple distinct phenomena.

**Prerequisites.** Euclidean norm, basic probability (expectation, variance, independence), comfort with $$\mathbb{R}^n$$. Measure theory is not required; volume arguments stay heuristic-plus-classical.

---

## 1. Volume in high dimension: shells and equators

Let $$B_2^n=\{x\in\mathbb{R}^n:\|x\|_2\le 1\}$$ be the Euclidean unit ball. The volume scales as

$$
\mathrm{Vol}(B_2^n) = \frac{\pi^{n/2}}{\Gamma(n/2+1)},
$$

which decays super-exponentially in $$n$$ after a peak—already a hint that “unit ball” is a thin object in high dimension. More geometrically: for $$r<1$$ close to $$1$$, the shell $$B_2^n\setminus r B_2^n$$ carries almost all the volume as $$n$$ grows. Similarly, most volume sits near an equatorial slab orthogonal to any fixed direction.

**Consequence.** Monte Carlo sampling, integration, and “typical set” thinking must respect that **typical points live near the surface**, not near the origin. The same phenomenon appears for Gaussians: a standard Gaussian vector in $$\mathbb{R}^n$$ has norm tightly concentrated near $$\sqrt{n}$$.

---

## 2. Random vectors: norms and angles

Let $$X=(X_1,\ldots,X_n)$$ with i.i.d. mean-zero, variance-$$\sigma^2$$ coordinates. Then

$$
\mathbb{E}\|X\|_2^2 = n\sigma^2,
$$

and under mild tail assumptions, $$\|X\|_2$$ concentrates around $$\sigma\sqrt{n}$$. For two independent isotropic random vectors, the inner product $$X\cdot Y$$ is typically order $$\sigma^2\sqrt{n}$$ in fluctuations while norms are order $$\sigma\sqrt{n}$$, so the cosine of the angle is typically order $$n^{-1/2}$$: **high-dimensional random vectors are nearly orthogonal**.

This is a theorem-shaped phenomenon under explicit measure assumptions (with quantitative concentration bounds), not a mystical property of “big data” alone.

---

## 3. Concentration of measure

A cornerstone: if $$f:\mathbb{R}^n\to\mathbb{R}$$ is Lipschitz with constant $$L$$ with respect to the Euclidean metric, and $$X$$ is a standard Gaussian vector, then $$f(X)$$ concentrates around its median (or mean) with sub-Gaussian tails:

$$
\mathbb{P}\bigl(\lvert f(X)-\mathrm{Med}\rvert > t\bigr) \le 2e^{-t^2/(2L^2)}
$$

(up to standard formulations). Similar results hold for other product measures and for Haar measure on high-dimensional spheres (Lévy’s lemma).

**Why it matters.** High dimension often makes *random* objects **rigid**: distances, singular values of random matrices, and empirical averages become predictable. Random matrix theory (Marchenko–Pastur, semicircle laws) is a sibling field.

---

## 4. Dimension reduction: Johnson–Lindenstrauss

**Johnson–Lindenstrauss (JL) lemma (informal).** For any $$0<\varepsilon<1$$ and any set of $$N$$ points in Euclidean space of any dimension, there exists a linear map into dimension

$$
k = O\bigl(\varepsilon^{-2}\log N\bigr)
$$

that preserves all pairwise distances up to a factor $$1\pm\varepsilon$$. Random projections (Gaussian or structured sparse maps) achieve this with high probability.

**Literacy.** JL preserves **pairwise Euclidean distances** for a **finite** set. It does not automatically preserve all manifold geometry, clusters under arbitrary metrics, or semantic “meaning.” It is a theorem about metric embeddings, not a free lunch for every ML pipeline.

---

### Deep-Dive Explanation: The Central Sphere That Bursts Out of a Hypercube (Read Slowly)

To feel the shock of high-dimensional geometry using nothing more than the Pythagorean theorem, try a famous thought experiment inside the $$n$$-dimensional hypercube $$[-2, 2]^n$$ (side length $$4$$, distance from the origin $$0$$ to every wall equal to $$2$$).

1. **Pack $$2^n$$ unit balls into the corners:** Place $$2^n$$ balls of radius $$1$$ centered at all points $$(\pm 1, \pm 1, \dots, \pm 1)$$. At $$n=2$$, that is 4 unit circles tucked neatly inside the square $$[-2, 2]^2$$. At $$n=3$$, it is 8 unit spheres inside the cube $$[-2, 2]^3$$.
2. **Squeeze a central sphere at the origin $$0$$** just large enough to touch all $$2^n$$ corner balls. Its radius $$r_n$$ is the distance from $$0$$ to a corner center minus the corner ball’s radius $$1$$:
   $$
   r_n = \sqrt{1^2 + 1^2 + \cdots + 1^2} - 1 = \sqrt{n} - 1.
   $$
3. **Plug in concrete dimensions:**
   - $$n = 2$$: $$r_2 = \sqrt{2} - 1 \approx 0.41$$ (tiny circle trapped in the middle).
   - $$n = 4$$: $$r_4 = \sqrt{4} - 1 = 1$$ (as big as the corner balls!).
   - $$n = 9$$: $$r_9 = \sqrt{9} - 1 = 2$$ (reaches the walls of the cube $$[-2, 2]^9$$!).
   - $$n = 16$$: $$r_{16} = \sqrt{16} - 1 = 3 > 2$$—**the central sphere trapped between the corner balls literally bursts OUTSIDE the hypercube $$[-2, 2]^{16}$$!**

4. **Check a Johnson–Lindenstrauss projection by hand:** Take two orthogonal points $$x = (1, 0, 0, 0)^\top$$ and $$y = (0, 1, 0, 0)^\top$$ in $$\mathbb{R}^4$$ (squared distance $$\|x - y\|_2^2 = 2$$) and project them into $$\mathbb{R}^2$$ with the scaled sign matrix

   $$
   R = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & -1 & 1 & 1 \\ 1 & 1 & -1 & 1 \end{pmatrix}.
   $$

   Then $$Rx = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}$$, $$Ry = \frac{1}{\sqrt{2}}\begin{pmatrix}-1\\1\end{pmatrix}$$, and the projected squared distance is

   $$
   \|Rx - Ry\|_2^2 = \frac{1}{2}\bigl((1 - (-1))^2 + (1 - 1)^2\bigr) = \frac{4}{2} = 2.
   $$

   The distance is preserved identically even though we cut the dimension in half! In general, random projections preserve squared distances in expectation, and concentration of measure keeps every pair within $$1\pm\varepsilon$$ once $$k = O(\varepsilon^{-2}\log N)$$.

## 5. Curse of dimensionality: several curses, not one

Popular discourse packs many issues into one phrase:

| Phenomenon | Rough content |
|------------|---------------|
| Volume emptiness | Empty space; exponential need for samples to fill grids |
| Distance concentration | Nearest and farthest neighbors become similar in ratio |
| Statistical cost | Estimation rates degrade with ambient or intrinsic dimension |
| Computational cost | Algorithms scale badly in $$n$$ without structure |
| Optimization landscape | Nonconvex high-d loss surfaces (related but distinct) |

Some problems **improve** with dimension (concentration, random projection, some convex geometries). “Curse” is not universal suffering; it is a checklist of failure modes when methods assume low-d intuition.

---

## 6. Geometry of data: intrinsic vs ambient dimension

Data in $$\mathbb{R}^n$$ often lie near low-dimensional structures: unions of subspaces, manifolds, sparse supports. **Intrinsic dimension** governs sample complexity more than ambient $$n$$ when structure is real and algorithms exploit it (sparse recovery, manifold learning, PCA). Compressed sensing shows that $$s$$-sparse vectors in $$\mathbb{R}^n$$ can be recovered from $$m=O(s\log(n/s))$$ linear measurements under restricted isometry conditions—high-d geometry plus convex or greedy optimization.

**Hype watch.** “Manifold hypothesis” is sometimes true enough to help and sometimes a cartoon. Empirical intrinsic-dimension estimates are delicate.

---

## 7. Links to machine learning and algorithms

1. **Nearest neighbors:** distance concentration can degrade classic NN unless features are informative.
2. **Kernel methods and random features:** approximate inner products in high feature spaces via concentration.
3. **Neural nets:** overparameterized regimes live in very high-d parameter spaces; implicit bias and geometry of level sets are research topics (see ML theory and Mathematics of AI).
4. **Optimization:** high-d convex bodies can have benign projection geometry (e.g., concentration of Lipschitz objectives).
5. **Privacy and hashing:** locality-sensitive hashing relies on geometric collision probabilities.

---

## 8. Frontiers

1. Non-Euclidean high-d geometry (graphs, hyperbolic embeddings, optimal transport metrics).
2. Precise geometric descriptions of neural network decision boundaries.
3. Homogenization between random matrix theory and deep learning Hessians/Jacobians.
4. Algorithmic high-d geometry: nearest neighbor search, clustering lower bounds.
5. Geometric functional analysis (Dvoretzky’s theorem: high-d convex bodies have almost Euclidean sections)—deep pure math with applied echoes.

### Worked calculation: shell volume ratio

The ratio of volumes of concentric Euclidean balls is

$$
\frac{\mathrm{Vol}(r B_2^n)}{\mathrm{Vol}(B_2^n)} = r^n.
$$

For $$r=0.9$$ and $$n=100$$, $$0.9^{100}\approx 2.7\times 10^{-5}$$: less than three thousandths of a percent of the volume sits inside radius $$0.9$$. Almost all the “mass” of the unit ball is in a thin outer shell. Any algorithm that assumes “most points are near the center” inherits a low-dimensional intuition that high-d geometry rejects.

### Random projection sketch

To preserve distances among $$N$$ points, JL-scale targets $$k\sim C\varepsilon^{-2}\log N$$. For $$N=10^6$$ and $$\varepsilon=0.1$$, $$\log N\approx 14$$ (natural log ≈13.8), so $$k$$ on the order of a few thousand is the scaling message—not a magic constant independent of proof details, but enough to see that **metric** dimension reduction can be logarithmic in $$N$$, independent of ambient dimension. Visualization in 2D remains a separate, lossy art.

---

## Common confusions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “High dimension always makes learning impossible.” | False | Structure and concentration can help; ambient vs intrinsic dimension. |
| “All pairs of points are equidistant in high-d data.” | Overstated | Can happen under noise+isotropic models; real data may be anisotropic. |
| “JL means we can always project to 2D for visualization without loss.” | False | $$k$$ depends on $$N$$ and $$\varepsilon$$; 2D is for pictures, not metric fidelity of large sets. |
| “Unit ball volume grows with dimension.” | False | Euclidean unit ball volume → 0 as $$n\to\infty$$. |
| “Random projection preserves classes for free.” | Heuristic | Preserves distances approximately; labels need separate analysis. |

---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/high-dimensional-geometry/analysis.md`.

### Status

**Classical + modern probability.** Concentration of measure and JL lemma are theorems; geometric aspects of data analysis remain active.

### Core statement / slogan

Concentration: Lipschitz functions on high-dimensional spheres/Gaussians are nearly constant. Johnson–Lindenstrauss: $$n$$ points in Euclidean space embed in $$O(\varepsilon^{-2}\log n)$$ dimensions preserving distances up to $$1\pm\varepsilon$$.

### Definitions to freeze

- **Concentration.** A r.v. $$X$$ concentrates if $$P(|X-\mathbb{E}X|>t)$$ decays rapidly in $$t$$.
- **Intrinsic dimension.** Effective degrees of freedom of a data set, often $$\ll$$ ambient $$d$$.

### Hygiene (from confusions log)

- Thinking all high-d phenomena are 'curses' (concentration also enables algorithms).
- Ignoring that data often lie near low-dimensional structures.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/high-dimensional-geometry/`.

**Recommended order**

1. **Core** — Roman Vershynin — High-Dimensional Probability Lecture 1: [https://www.youtube.com/watch?v=nKmYjFoiuYM](https://www.youtube.com/watch?v=nKmYjFoiuYM).  
2. **Foundation** — Simons Institute — High Dimensional Geometry and Concentration I: [https://www.youtube.com/watch?v=UHvT1MxFuvo](https://www.youtube.com/watch?v=UHvT1MxFuvo).  
3. **Meta** — Vershynin course page (all lectures): [https://www.math.uci.edu/~rvershyn/teaching/hdp/hdp.html](https://www.math.uci.edu/~rvershyn/teaching/hdp/hdp.html).  

**Status reminder:** **Classical + modern probability.** Concentration of measure and JL lemma are theorems; geometric aspects of data analysis remain active.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/high-dimensional-geometry/transcripts/` · status: `research/video-research/high-dimensional-geometry/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/high-dimensional-geometry_nKmYjFoiuYM_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References and further reading

1. Vershynin. *High-Dimensional Probability* — modern standard.
2. Boucheron, Lugosi, Massart. *Concentration Inequalities*.
3. Dasgupta & Gupta expositions of Johnson–Lindenstrauss.
4. Ball. Elementary high-d volume essays; geometric functional analysis introductions.
5. Course links: [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/), [Optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/).

---


Full URL bibliography from video research: `research/video-research/high-dimensional-geometry/references.md`.

### Videos (recommended path)

- Roman Vershynin — High-Dimensional Probability Lecture 1 (CORE): https://www.youtube.com/watch?v=nKmYjFoiuYM
- Simons Institute — High Dimensional Geometry and Concentration I (FOUNDATION): https://www.youtube.com/watch?v=UHvT1MxFuvo
- Vershynin course page (all lectures) (META): https://www.math.uci.edu/~rvershyn/teaching/hdp/hdp.html

### Papers and web (from research pack)

- Vershynin — High-Dimensional Probability (book PDF via author): https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html
- Wikipedia — Concentration of measure: https://en.wikipedia.org/wiki/Concentration_of_measure
- Wikipedia — Johnson–Lindenstrauss lemma: https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma
- Wikipedia — Curse of dimensionality: https://en.wikipedia.org/wiki/Curse_of_dimensionality
- Wikipedia — High-dimensional statistics: https://en.wikipedia.org/wiki/High-dimensional_statistics

### Course

- Research pack: `research/video-research/high-dimensional-geometry/` (especially `references.md`, `learning_path.md`).

## Further directions

- **Learning theory uses concentration:** [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).
- **Distributions as geometric objects:** [Optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/).
- **AI flagship:** [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/).
- **Practice:** sample random Gaussian vectors in dimensions 2, 20, 200; histogram norms and pairwise absolute cosines.
- **Reading path:** Vershynin early chapters → JL lemma → one random matrix vignette.

## Video tham khảo

- **xem trước** — [Lecture 1](https://www.youtube.com/watch?v=nKmYjFoiuYM) — Roman Vershynin, English. Watch first. “Lecture 1” orients the lesson’s aim: Explain why most volume of a high-dimensional Euclidean ball lies near its equator/shell, and why that breaks “volume = interior” intuition.
- [High Dimensional Geometry and Concentration I](https://www.youtube.com/watch?v=UHvT1MxFuvo) — Simons Institute for the Theory of Computing, English. A second pass once the main claim is in view: Explain why most volume of a high-dimensional Euclidean ball lies near its equator/shell, and why that breaks “volume = interior” intuition.
