---
layout: post
title: "Higher Dimensions"
chapter: '04'
order: 9
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
---

Imagine buying an orange whose radius is $$1$$ and whose peel is paper-thin—just $$1\%$$ of the radius, leaving an edible core of radius $$0.99$$. In our familiar 3-dimensional world, that peel is a modest $$1 - 0.99^3 \approx 3\%$$ of the fruit’s volume; $$97\%$$ is juicy orange. Now carry that exact same orange into 100 dimensions. The core volume shrinks to $$0.99^{100} \approx 0.366$$, meaning **$$63.4\%$$ of the entire orange is peel**. Carry it into 1,000 dimensions, and the peel swallows **$$99.996\%$$** of the volume—leaving practically nothing inside!

That single calculation reveals the great shock of **higher dimensions**. Moving from $$\mathbb{R}^3$$ to $$\mathbb{R}^n$$ is not just "3D with extra coordinates." As you turn the dimension dial $$n$$ upward, the rules of geometry invert: unit spheres shrink to zero volume, corners of cubes poke far outside inscribed balls, and almost any two randomly chosen directions turn out to be nearly perpendicular. Far from being sci-fi mysticism, this bizarre high-dimensional geometry is the everyday operating system of modern probability, statistical physics, and machine learning—where embeddings routinely live in thousands of dimensions.

**Path:** coordinates and Euclidean norm → hypercubes and the 100D orange → hypersphere volumes and the sphere-in-a-box paradox → slices and projections → concentration of measure and nearly orthogonal vectors → data science and the curse of dimensionality → common confusions and further directions.

---

## Learning objectives

After this lecture you should be able to:

- Use coordinates and the Euclidean norm on $$\mathbb{R}^n$$ confidently without needing to "picture" four perpendicular axes.
- Compute volume scaling for **hypercubes** and **hyperspheres**, and explain why the unit ball’s volume peaks at $$n=5$$ before collapsing to $$0$$.
- Work through the **sphere-in-a-box** calculation showing how a tiny inner sphere pokes *outside* its surrounding box in dimension $$n \ge 10$$.
- Explain **concentration of measure**: why most volume sits in a thin outer shell and why random high-dimensional vectors are nearly orthogonal.
- Connect high-dimensional geometry to machine learning phenomena (the **curse of dimensionality**, random projections, and manifold structure).
- Avoid claiming that "the fourth dimension must be time, so geometry stops at 3."

**Prerequisites.** Vectors and dot products in $$\mathbb{R}^2$$ and $$\mathbb{R}^3$$; Pythagorean theorem; basic variance or standard deviation helps for the orthogonality calculation.

---

## Key ideas: What Is High-Dimensional Geometry and Why Does It Matter?

At $$n=1,2,3$$, your eyes are trustworthy guides. At $$n=10$$, linear algebra still works effortlessly while visual intuition breaks down. At $$n=1000$$, probability and geometry merge. Four pillars carry the subject:

1. **Euclidean Linear Algebra in $$\mathbb{R}^n$$:** Coordinates $$(x_1,\ldots,x_n)$$, inner products $$\langle x,y\rangle$$, and norms $$\|x\|_2$$ work identically for $$n=3$$ and $$n=10{,}000$$. Algebra gives us exact control long after 3D visualization gives out.
2. **Convex & Asymptotic Geometry:** Comparing simple shapes—balls, cubes, simplices—as $$n\to\infty$$ uncovers startling asymptotic laws. In high dimensions, cubes become "spiky" (almost all volume concentrates in the $$2^n$$ corners), while balls concentrate their mass in a razor-thin equatorial belt and outer crust.
3. **Concentration of Measure & High-Dimensional Probability:** When you average $$n$$ independent coordinates, fluctuations shrink like $$1/\sqrt{n}$$. On a high-dimensional sphere $$S^{n-1}$$, smooth functions become almost constant everywhere—turning high-dimensional randomness into near-determinism (the engine behind Monte Carlo integration and **Johnson–Lindenstrauss** random projections).
4. **Data Science & Machine Learning:** A single $$100\times 100$$ grayscale image is a point in $$\mathbb{R}^{10{,}000}$$; a modern language-model token embedding lives in $$\mathbb{R}^{4096}$$ or higher. Understanding why naive distances blur (**curse of dimensionality**) and why real data concentrates on low-dimensional manifolds is essential for building algorithms that actually work.

---

## 1. Coordinates without fear

Euclidean $$n$$-space is simply the set of ordered $$n$$-tuples of real numbers:

$$
\mathbb{R}^n=\{(x_1,x_2,\ldots,x_n):x_i\in\mathbb{R}\},
$$

equipped with the Euclidean distance

$$
\|x-y\|_2=\sqrt{\sum_{i=1}^n(x_i-y_i)^2}.
$$

Linear subspaces, orthogonality ($$\langle x,y\rangle = 0$$), and orthogonal projections obey the exact same formulas in $$\mathbb{R}^{100}$$ as in $$\mathbb{R}^3$$. There is nothing mystical about $$n=4$$ or $$n=100$$: geometry does not require your eyes to hallucinate four mutually perpendicular axes in a room. (Physics models spacetime as 4-dimensional with a non-Euclidean Lorentzian signature, which is a model of nature—separate from pure Euclidean $$\mathbb{R}^n$$.)

---

## 2. Hypercubes and the tyranny of exponents

The unit hypercube $$[0,1]^n$$ has $$2^n$$ vertices and $$n\cdot 2^{n-1}$$ edges. A cube of side length $$a$$ has volume $$a^n$$: if $$a=0.99$$, $$a^n\to 0$$; if $$a=1.01$$, $$a^n\to\infty$. Already this tells you the #1 rule of high dimensions: **exponents in $$n$$ crush 3D intuition.**

The skeleton of the $$n$$-cube is also a workhorse in computer science: every vertex is an $$n$$-bit binary string, and **Gray codes** trace a Hamiltonian path along its edges by flipping one bit at a time.

---

### Short video: Volume of the unit ball by dimension

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/ball-volume-dimensions_en.mp4"></video>
</div>

The volume of the unit ball peaks in dimension 5 (about 5.26) and then falls toward 0, and it fills a vanishing share of the cube $$[-1,1]^n$$.


### Try it yourself: Slide through the dimensions

<div class="mex-explainer" data-mex="ball" data-lang="en"></div>


## 3. Hyperspheres: vanishing volume and the sphere-in-a-box paradox

The unit ball $$B^n = \{x\in\mathbb{R}^n : \|x\|_2 \le 1\}$$ sits snugly inside the cube $$[-1,1]^n$$ of volume $$2^n$$. Its exact $$n$$-dimensional volume is

$$
V_n = \frac{\pi^{n/2}}{\Gamma\!\left(\frac{n}{2}+1\right)}.
$$

Watch what happens to $$V_n$$ and its share of the surrounding cube $$[-1,1]^n$$ as $$n$$ increases:

| Dimension $$n$$ | Unit ball volume $$V_n$$ | Cube volume $$2^n$$ | Share $$V_n / 2^n$$ |
| :--- | :--- | :--- | :--- |
| $$2$$ | $$\pi \approx 3.142$$ | $$4$$ | $$78.5\%$$ |
| $$3$$ | $$\tfrac{4}{3}\pi \approx 4.189$$ | $$8$$ | $$52.4\%$$ |
| $$5$$ | $$\tfrac{8}{15}\pi^2 \approx 5.264$$ | $$32$$ | $$16.4\%$$ |
| $$10$$ | $$\tfrac{\pi^5}{120} \approx 2.550$$ | $$1{,}024$$ | $$0.249\%$$ |
| $$20$$ | $$\tfrac{\pi^{10}}{10!} \approx 0.0258$$ | $$1{,}048{,}576$$ | $$0.0000025\%$$ |

The denominator $$\Gamma(\tfrac{n}{2}+1)$$ grows like a factorial—beating the exponential $$\pi^{n/2}$$ hands down! So after peaking at $$n=5$$, the unit ball’s volume collapses toward **zero**, while almost all the volume of the cube $$[-1,1]^n$$ migrates out into its $$2^n$$ pointy corners.

### Worked example 1: The sphere trapped in the center that pokes *outside* the box

How "spiky" do those cube corners really get? Try this famous calculation:
1. Take the box $$[-2,2]^n$$ (side length $$4$$, centered at the origin).
2. Pack $$2^n$$ unit balls of radius $$1$$ into its $$2^n$$ quadrants, centered at $$(\pm 1, \pm 1, \ldots, \pm 1)$$. Every unit ball touches the walls of the box.
3. Now drop a tiny ball centered at the origin $$(0,0,\ldots,0)$$ and inflate it until it just touches all $$2^n$$ surrounding unit balls. What is its radius $$r_n$$?

The distance from the origin to any corner center $$(\pm 1,\ldots,\pm 1)$$ is $$\sqrt{1^2 + 1^2 + \cdots + 1^2} = \sqrt{n}$$. Subtracting the radius $$1$$ of the corner ball gives the exact radius of the central ball:

$$
r_n = \sqrt{n} - 1.
$$

Check the numbers:
- In **2D** ($$n=2$$): $$r_2 = \sqrt{2} - 1 \approx 0.414$$—a cozy little circle tucked inside the box (half-width $$2$$).
- In **4D** ($$n=4$$): $$r_4 = \sqrt{4} - 1 = 1$$—already as big as the corner balls!
- In **9D** ($$n=9$$): $$r_9 = \sqrt{9} - 1 = 2$$—it touches the outer walls of the box $$[-2,2]^9$$!
- In **10D** ($$n=10$$): $$r_{10} = \sqrt{10} - 1 \approx 2.162 > 2$$—**the central ball, while still wedged tightly between the $$2^{10}$$ corner balls, bulges straight outside the box!**

That is not a trick of algebra; it is a direct window into how vast the diagonal "corners" of a high-dimensional cube become compared to its faces.

---

## 4. Seeing the unseen: slices and projections

Humans infer 3D objects from 2D shadows and cross-sections. We explore 4D shapes the exact same way:

- **Projections:** Cast a 4D tesseract onto 3D or 2D (Schlegel diagrams, rotating wireframes), just as a cube casts a 2D shadow.
- **Slices:** Intersect a 4D hypersphere with a moving 3D hyperplane—just like an MRI machine scans a 3D body into 2D slices, a 4D ball appears as a 3D point that inflates into a sphere and shrinks back to a point.
- **Analogy chains:** Point ($$0$$D) $$\to$$ segment ($$1$$D) $$\to$$ square ($$2$$D) $$\to$$ cube ($$3$$D) $$\to$$ tesseract ($$4$$D), doubling vertices and adding connecting edges at every step.

---

## 5. Concentration of measure: why random vectors are nearly orthogonal

On a high-dimensional sphere $$S^{n-1}$$, smooth (Lipschitz) functions become nearly constant—almost all surface area concentrates near the equator perpendicular to any fixed direction:

$$
\mathbb{P}\bigl(\lvert f(X)-\mathrm{Med}(f)\rvert>t\bigr)\le 2e^{-c n t^2}.
$$

### Worked example 2: Picking two random directions in $$\mathbb{R}^n$$

Take two random unit vectors $$u, v$$ whose coordinates are chosen independently as $$\pm \frac{1}{\sqrt{n}}$$ with equal probability $$1/2$$. What is the cosine of the angle $$\theta$$ between them?

$$
\cos\theta = \langle u, v\rangle = \frac{1}{n}\sum_{i=1}^n s_i,
$$

where each $$s_i = n u_i v_i \in \{-1, +1\}$$ is an independent fair coin flip with mean $$0$$ and variance $$1$$. Compute the mean and standard deviation of $$\cos\theta$$:

$$
\mathbb{E}[\cos\theta] = 0, \qquad \mathrm{SD}(\cos\theta) = \sqrt{\frac{1}{n^2}\cdot n} = \frac{1}{\sqrt{n}}.
$$

Watch what happens to the typical angle $$\theta$$ as $$n$$ grows:
- In **$$n = 2$$**: $$\mathrm{SD}(\cos\theta) = 0.707$$—vectors point every which way.
- In **$$n = 100$$**: $$\mathrm{SD}(\cos\theta) = 0.10$$—most pairs have $$\cos\theta \in [-0.1, 0.1]$$, meaning $$\theta \in [84^\circ, 96^\circ]$$.
- In **$$n = 10{,}000$$**: $$\mathrm{SD}(\cos\theta) = 0.01$$—almost every pair of random directions sits within $$0.6^\circ$$ of a perfect $$90^\circ$$ right angle!

In $$\mathbb{R}^3$$ you can fit at most $$3$$ mutually perpendicular directions. In $$\mathbb{R}^{10{,}000}$$, you can pack *millions* of *almost* perpendicular directions—a geometric miracle that powers modern neural-network superposition and high-dimensional vector embeddings!

---

## 6. Data, algorithms, and the curse of dimensionality

When a dataset of $$N$$ points lives in $$\mathbb{R}^n$$ with large $$n$$:

- **Sparsity explodes:** To cover $$[0,1]^n$$ with a grid of spacing $$0.1$$ requires $$10^n$$ points—$$100$$ in 2D, but $$10^{100}$$ in 100D (more than the atoms in the observable universe). That is the **curse of dimensionality**.
- **Distances concentrate:** For random unstructured points in high dimension, the ratio between nearest-neighbor and farthest-neighbor distances approaches $$1$$, breaking naive distance-based search.
- **Structure rescues algorithms:** Real-world data (images, speech, text) does *not* fill $$\mathbb{R}^n$$ uniformly—it concentrates near lower-dimensional subspaces or curved manifolds, which is why PCA, random projections, and deep representation learning succeed.

---

### Explanation: How Dimension Turns Geometry Inside Out

High-dimensional surprises feel like magic until you see they all stem from one engine—**independent coordinates compounding multiplicatively**. Walk through the four steps slowly:

1. **Powers amplify tiny ratios.** Shrink a radius by just $$1\%$$ ($$0.99$$) and raise it to the $$n$$-th power: $$0.99^{100} \approx 0.366$$ and $$0.99^{1000} \approx 0.000043$$. That immediately forces almost all volume into the outer peel.
2. **Diagonals outgrow sides by $$\sqrt{n}$$.** A cube’s face sits at distance $$1$$ from the center, while its corner sits at distance $$\sqrt{n}$$. Once $$n \ge 10$$, $$\sqrt{n}-1 > 2$$, so the central sphere wedged between corner balls bursts outside the box.
3. **Independent signs cancel like $$1/\sqrt{n}$$.** Taking a dot product of two random unit vectors averages $$n$$ random $$\pm 1$$ steps, giving standard deviation $$1/\sqrt{n}$$. Hence random high-dimensional directions are almost always perpendicular.
4. **Algorithms must trade volume for structure.** Because raw volume grows exponentially while random distances concentrate, high-dimensional computing relies on sparsity, low-dimensional manifolds, and concentration inequalities rather than 3D geometric habits.

**Quick check.** For the 100D orange with radius $$1$$, how thin would the peel have to be for the peel and the inner core to have roughly *equal* volume ($$50\%$$ each)? *(Hint: solve $$(1 - \delta)^{100} = 0.5$$, giving $$\delta \approx \frac{\ln 2}{100} \approx 0.0069$$—less than $$0.7\%$$ of the radius!)*

---

## 7. Why mathematicians care

- **Linear algebra and analysis.** Infinite-dimensional function spaces (Hilbert and Banach spaces) are the natural limit of high-dimensional $$\mathbb{R}^n$$.
- **Probability.** Concentration of measure unifies classical limit theorems with modern random matrix theory.
- **Geometry and coding.** Sphere packings in dimensions 8 and 24 (see [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/)) govern optimal error-correcting codes.
- **AI and optimization.** Every modern embedding space is a high-dimensional Euclidean or spherical playground.

---

### Higher-D slogans (from video research)

- [3B1B higher dimensions](https://www.youtube.com/watch?v=zwAD6dRSVyI): prefer coordinates + linear maps over mystical “seeing 4D.”
- Hypersphere volume ratios vs dimension are a standard shock — compute a table once.
- Concentration of measure is why high-D probability often becomes almost deterministic.

## 8. Common confusions

1. **“Only three dimensions exist.”** — Physical space models may have 3 spatial dimensions; mathematical $$\mathbb{R}^n$$ exists for every $$n \ge 1$$.
2. **“The fourth dimension must be time.”** — Time is one physical coordinate in relativity, not the definition of Euclidean $$\mathbb{R}^4$$.
3. **“High-dimensional unit balls are huge.”** — Their volume peaks at $$n=5$$ and tends to $$0$$ as $$n\to\infty$$.
4. **“Projection shows everything.”** — Lower-dimensional shadows lose information; different 4D shapes can cast identical 3D shadows.
5. **“Concentration means all points collapse together.”** — *Functions* of random points concentrate around their median; the space itself remains vast.
6. **“Curse of dimensionality means high-D math is useless.”** — It warns that naive grid methods fail, while structured and probabilistic methods thrive.

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/higher-dimensions/`.

**Recommended order**

1. **ORIENTATION** — 3Blue1Brown — Thinking visually about higher dimensions: [https://www.youtube.com/watch?v=zwAD6dRSVyI](https://www.youtube.com/watch?v=zwAD6dRSVyI).
2. **ORIENTATION** — Numberphile — Perfect Shapes in Higher Dimensions / higher-D culture: [https://www.youtube.com/watch?v=2s4TqVAbfz4](https://www.youtube.com/watch?v=2s4TqVAbfz4).
3. **ORIENTATION** — Numberphile — The Puzzling Fourth Dimension and Do in the Fourth Dimension talks: [https://www.youtube.com/watch?v=CVOr7f_VALc](https://www.youtube.com/watch?v=CVOr7f_VALc).
4. **FOUNDATION** — 3Blue1Brown — Essence of linear algebra (n-D vectors): [https://www.youtube.com/watch?v=fNk_zzaMoSs](https://www.youtube.com/watch?v=fNk_zzaMoSs).
5. **CORE** — Sphere packing / hypersphere volume explainers: [https://www.youtube.com/watch?v=zwAD6dRSVyI](https://www.youtube.com/watch?v=zwAD6dRSVyI).
6. **FRONTIER lite** — Concentration of measure popular/technical talks: [https://en.wikipedia.org/wiki/Concentration_of_measure](https://en.wikipedia.org/wiki/Concentration_of_measure).

Complete URL bibliography: `research/video-research/higher-dimensions/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/higher-dimensions/transcripts/` · status: `research/video-research/higher-dimensions/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/higher-dimensions_zwAD6dRSVyI_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/higher-dimensions/references.md`.

### Videos (primary path)

1. 3Blue1Brown — Thinking visually about higher dimensions — https://www.youtube.com/watch?v=zwAD6dRSVyI
2. Numberphile — Perfect Shapes in Higher Dimensions / higher-D culture — https://www.youtube.com/watch?v=2s4TqVAbfz4
3. Numberphile — The Puzzling Fourth Dimension and Do in the Fourth Dimension talks — https://www.youtube.com/watch?v=CVOr7f_VALc
4. 3Blue1Brown — Essence of linear algebra (n-D vectors) — https://www.youtube.com/watch?v=fNk_zzaMoSs
5. Sphere packing / hypersphere volume explainers — https://www.youtube.com/watch?v=zwAD6dRSVyI
6. Concentration of measure popular/technical talks — https://en.wikipedia.org/wiki/Concentration_of_measure
7. Curse of dimensionality in ML explainers — https://en.wikipedia.org/wiki/Curse_of_dimensionality
8. t-SNE / dimension reduction culture (contrast) — https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding

### Videos (secondary finds)

9. Carl Sagan Flatland / 4D cube classic clip culture — https://www.youtube.com/watch?v=2s4TqVAbfz4

### Papers, books, OCW, and web

10. Blum, Hopcroft, Kannan — Foundations of Data Science (high-D chapters): https://www.cs.cornell.edu/jeh/book.pdf
11. Wikipedia — Hypercube: https://en.wikipedia.org/wiki/Hypercube
12. Wikipedia — N-sphere: https://en.wikipedia.org/wiki/N-sphere
13. Wikipedia — Curse of dimensionality: https://en.wikipedia.org/wiki/Curse_of_dimensionality
14. Wikipedia — Concentration of measure: https://en.wikipedia.org/wiki/Concentration_of_measure
15. Wikipedia — Four-dimensional space: https://en.wikipedia.org/wiki/Four-dimensional_space

### Course

16. Course links: [Viazovska sphere packing]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/), [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/), [Explore fourth dimension]({{ site.baseurl }}/contents/en/chapter07/07_06_Explore_Fourth_Dimension/), [Linear algebra / AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/). Pack: `research/video-research/higher-dimensions/`.

## Further directions

Hands-on prompts: [Explore the fourth dimension]({{ site.baseurl }}/contents/en/chapter07/07_06_Explore_Fourth_Dimension/). Extreme packing geometry: [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/). Data geometry: [Linear algebra and AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/). Strange embeddings back in 3D: [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/).

## Video tham khảo

- **xem trước** — [Thinking outside the 10-dimensional box](https://www.youtube.com/watch?v=zwAD6dRSVyI) — 3Blue1Brown, English. Watch first. “Thinking outside the 10-dimensional box” orients the lesson’s aim: Use coordinates and the Euclidean norm on \mathbb{R}^n confidently.
- [Perfect Shapes in Higher Dimensions - Numberphile](https://www.youtube.com/watch?v=2s4TqVAbfz4) — Numberphile, English. A second pass once the main claim is in view: Use coordinates and the Euclidean norm on \mathbb{R}^n confidently.
- [The Puzzling Fourth Dimension (and exotic shapes) - Numberphile](https://www.youtube.com/watch?v=CVOr7f_VALc) — Numberphile, English. Further depth after the first two, still tied to this lesson: Use coordinates and the Euclidean norm on \mathbb{R}^n confidently.
