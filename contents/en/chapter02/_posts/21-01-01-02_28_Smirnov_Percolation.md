---
layout: post
title: "Smirnov’s Percolation and the Planar Ising Model (Fields Medal 2010)"
chapter: '02'
order: 28
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Spread out an enormous honeycomb board made of millions of hexagonal tiles, and flip a fair coin for each tile: heads paints it **yellow**, tails paints it **blue**. Now step far back until the individual hexagons blur into a continuous picture, and ask: what determines the probability of finding a continuous yellow path connecting the left boundary of a shape to the right? Statistical physicists predicted a miracle: right at the critical threshold $$p_c = 1/2$$, the random pattern **forgets** its hexagonal grid completely and becomes **conformally invariant**—bend the domain by any angle-preserving complex-analytic map, and the crossing probability stays unchanged!

For decades, that dream had not a single rigorous proof for any concrete lattice model. In 2001, in a breathtaking **6-page paper**, **Stanislav Smirnov** proved Cardy’s formula and conformal invariance for critical site percolation on the triangular lattice—and then invented **discrete holomorphic fermions** to conquer the **planar Ising model**. In 2010, he received the **Fields Medal**:

> “For the proof of conformal invariance of percolation and the planar Ising model in statistical physics.”  
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

Read the citation with precision: it names **two specific lattice models**, not every 2D critical model (even critical bond percolation on the square lattice remains open!). Smirnov’s discrete lattice theorems lock directly into the continuum **SLE** curve language of Oded Schramm and [Wendelin Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) (Fields 2006), and paved the way for his doctoral student [Hugo Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase_Transitions/) (Fields 2022).

**Lesson roadmap:** Key ideas (conformal maps, site vs. bond percolation, discrete complex analysis) → Hand-verifiable worked examples (Hex board symmetry at $$p_c = 1/2$$ & Cardy–Carleson’s linear law on an equilateral triangle) → Explanation: 4 steps from color-switching to discrete Cauchy–Riemann, $$\mathrm{SLE}_6$$, and Ising fermions → What remains open (square-lattice bond percolation, self-avoiding walk).

---

## Learning objectives

After this lecture you should be able to:

- Distinguish **site** percolation from **bond** percolation, and explain why only the critical point $$p_c$$ yields a nontrivial scaling limit.
- Compute crossing probabilities on an equilateral triangle via **Cardy–Carleson’s formula** and explain the Hex symmetry argument for $$p_c = 1/2$$.
- Explain why Smirnov’s 2001 proof relies essentially on the threefold symmetry of the **triangular lattice**, leaving **square-lattice bond percolation** open.
- Assign credit cleanly: **Schramm** invented SLE, **Lawler–Schramm–Werner** built its analytic theory, and **Smirnov** proved discrete lattice models converge to conformally invariant limits.
- Describe **discrete holomorphic fermions** for the **planar Ising model** (Smirnov; Chelkak–Smirnov on isoradial graphs) and explain why the Ising result is *more universal* than the 2001 percolation theorem.

**Prerequisites.** Holomorphic functions and conformal maps of plane domains at the level of a first complex-analysis course; Bernoulli random variables and the idea of a scaling limit (mesh $$\delta\to 0$$); the difference between a discrete model and a continuum process. No prior SLE course is required.

**Seminar links.** Pair with [Werner / SLE]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) for the curve language, and with [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase_Transitions/) for later sharp results on phase transitions.

---

## Key ideas: What Do Conformal Invariance and Discrete Complex Analysis Study?

### 1. Conformal maps—angle-preserving geometry
A holomorphic map $$f: \Omega_1 \to \Omega_2$$ with $$f'(z) \neq 0$$ is **conformal**: locally it only scales and rotates, never distorting angles. By the Riemann mapping theorem, every simply connected planar domain (square, disk, triangle, blob) maps conformally to any other. If a critical lattice model is **conformally invariant**, solving it on one simple shape (an equilateral triangle) immediately gives the exact answer on *every* planar domain!

### 2. Triangular site percolation vs. square bond percolation
- **Site percolation on the triangular lattice $$\mathbb{T}$$** (equivalently, coloring hexagonal cells of the dual honeycomb grid yellow with probability $$p$$, blue with $$1-p$$): $$p_c = 1/2$$.
- **Bond percolation on the square lattice $$\mathbb{Z}^2$$:** each edge is open with probability $$p$$ (also $$p_c = 1/2$$). Physicists expect **universality** (identical conformal limits for both), yet mathematically only the triangular site model is proved!

### 3. Discrete complex analysis
How do you prove a discrete probability function $$F_\delta$$ on a mesh of size $$\delta$$ converges to a holomorphic function as $$\delta \to 0$$? Find an exact combinatorial identity on the lattice forcing $$F_\delta$$ to satisfy **discrete Cauchy–Riemann equations** (contour sums around every tiny cell vanish). Taking $$\delta \to 0$$ forces every subsequential limit to be holomorphic and uniquely fixed by boundary conditions!

---

## 1. Hand-Verifiable Worked Examples: The Game of Hex and Cardy–Carleson’s Linear Law

### Example 1: Why $$p_c = 1/2$$ on an $$N \times N$$ honeycomb (Hex) board
Color every hexagon of an $$N \times N$$ rhombus board yellow or blue independently with probability $$p = 1/2$$.
- A famous topological theorem (equivalent to Brouwer’s fixed-point theorem!) says the game of **Hex can never end in a draw**: either a yellow path connects left to right, or a blue path connects top to bottom—*exactly one* occurs!
- At $$p = 1/2$$, the two colors are perfectly symmetric, so:
  $$
  \mathbb{P}_{1/2}(\text{yellow crosses left–right}) = \mathbb{P}_{1/2}(\text{blue crosses top–bottom}) = \frac{1}{2} \quad \text{for EVERY } N!
  $$
Even as $$N \to \infty$$ (mesh $$\delta \to 0$$), the crossing probability stays pinned at $$1/2$$ instead of collapsing to $$0$$ or $$1$$—the unmistakable signature of criticality!

### Example 2: Cardy–Carleson’s formula on an equilateral triangle of side $$1$$
In 1992, **John Cardy** used non-rigorous CFT to guess a hypergeometric crossing formula for any conformal rectangle $$(\Omega; A, B, C, D)$$. **Lennart Carleson** noticed that if you map $$\Omega$$ conformally onto an **equilateral triangle $$ABC$$ of side length $$1$$**, placing $$D$$ on side $$AC$$ at distance $$x \in [0, 1]$$ from $$C$$, Cardy’s hypergeometric formula collapses to pure linearity:

$$
\mathbb{P}(\text{yellow path connects side } AB \text{ to segment } CD) = x!
$$

Plug in concrete positions along $$AC$$:
- $$x = 0.25$$ (one quarter up): limiting crossing probability is **$$25\%$$**.
- $$x = 0.50$$ (midpoint): limiting crossing probability is **$$50\%$$**.
- $$x = 0.75$$ (three quarters up): limiting crossing probability is **$$75\%$$**.

---

## 2. Explanation: How Smirnov Proved Conformal Invariance for Percolation and Ising

Both of Smirnov’s Fields breakthroughs follow a crisp 4-step discrete-holomorphicity blueprint:

#### Step 1: The color-switching trick on the triangular lattice (Percolation, 2001)
In his 6-page *Comptes Rendus* paper (2001; full account [arXiv:0909.4499](https://arxiv.org/abs/0909.4499)), Smirnov defines three probabilities inside a domain $$\Omega$$ with boundary arcs $$AB, BC, CA$$: let $$H_A(z)$$ be the probability of a yellow path separating $$z$$ and $$BC$$ from $$A$$ (and similarly $$H_B, H_C$$).
Stepping $$z$$ across one hexagonal edge changes $$H_A$$ by the probability of a "three-arm" event (two yellow arms and one blue arm meeting at that edge). Using a dazzling **color-switching bijection**—flipping the colors along one arm at $$p = 1/2$$ while exploiting the exact $$120^\circ$$ threefold symmetry of hexagons—Smirnov proved that the discrete directional derivatives of $$H_A, H_B, H_C$$ along the three lattice axes match!

#### Step 2: Passing to $$\delta \to 0$$ yields Cardy–Carleson’s formula
The complex combination $$F_\delta(z) = H_A(z) + \tau H_B(z) + \tau^2 H_C(z)$$ (with $$\tau = e^{2\pi i/3}$$) satisfies **discrete Cauchy–Riemann equations**! As $$\delta \to 0$$, Russo–Seymour–Welsh precompactness guarantees subsequential limits that are **holomorphic** and satisfy boundary conditions mapping $$\Omega$$ onto the equilateral triangle—proving **Cardy’s formula** and **conformal invariance** in one stroke!

#### Step 3: Locking into Schramm–Lawler–Werner’s SLE language
One year earlier, **Oded Schramm (2000)** had defined $$\mathrm{SLE}_\kappa$$ as the unique conformally invariant, domain-Markov candidate for critical interfaces. Armed with Smirnov’s 2001 crossing theorem, Smirnov and **Camia–Newman** proved that the percolation exploration path converges in law to **$$\mathrm{SLE}_6$$**!

| Contribution | Who, at slogan level |
|--------------|----------------------|
| Invented SLE | Schramm (2000) |
| Analytic theory of SLE; Brownian frontier; exponents | Lawler–Schramm–Werner |
| Cardy + conformal invariance for triangular site percolation | Smirnov (2001) |
| Planar Ising observables / interfaces | Smirnov; Chelkak–Smirnov and later collaborators |

#### Step 4: Discrete holomorphic fermions for the planar Ising model (2010–2012)
For the critical **planar Ising model** (going far beyond Onsager’s 1944 free-energy calculation), **Smirnov** (*Ann. of Math.* 172, 2010) introduced a **discrete holomorphic fermionic observable**: a weighted sum over spin interfaces ending at an edge, multiplied by a complex spinor phase $$e^{-i \cdot \frac{1}{2}\text{winding}}$$. At the exact critical temperature $$\beta_c$$, local cancellations make this observable *s-holomorphic* with Riemann–Hilbert boundary conditions, converging to a conformally invariant holomorphic limit!
Together with **Dmitry Chelkak** (*Invent. Math.* 189, 2012; [arXiv:0910.2045](https://arxiv.org/abs/0910.2045)), Smirnov proved this limit is **universal across all planar isoradial graphs**—strictly more universal than the 2001 percolation theorem—and follow-up work (with Duminil-Copin, Hongler, Kemppainen) identified Ising spin interfaces with **$$\mathrm{SLE}_3$$**.

Summary of Smirnov’s discrete-complex-analysis machine:

$$
\text{Critical lattice model}
\;\xrightarrow{\text{Color-switching / Fermions}}\;
\text{Discrete Cauchy–Riemann}
\;\xrightarrow{\delta \to 0}\;
\text{Conformally invariant limit}
\;\longrightarrow\;
\mathrm{SLE}_6 \text{ \& } \mathrm{SLE}_3.
$$

---

## 3. What Remains Open and Why a Fields Medal

- **Critical bond percolation on the square lattice $$\mathbb{Z}^2$$** (and universality of planar percolation across general lattices) remains open, because Smirnov’s color-switching identity requires the threefold symmetry of $$\mathbb{T}$$.
- **Self-avoiding walk** (conjecturally $$\mathrm{SLE}_{8/3}$$) remains a famous open problem.
- Later work by [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase_Transitions/) (Fields 2022) complements this story with 2D FK rotational invariance and 3D/4D phase-transition theorems.

**Why a Fields Medal 2010:** Smirnov turned flagship predictions of 2D statistical physics into rigorous theorems, forged **discrete complex analysis** into a modern powerhouse, and anchored Schramm–Lawler–Werner’s SLE directly to concrete lattice models—alongside 2010 classmates Lindenstrauss, Ngô, and [Villani]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Smirnov proved conformal invariance of percolation on every lattice.” | The 2001 theorem is for **critical site percolation on the triangular lattice**. Square-lattice bond percolation is a famous remaining case. |
| “Cardy proved the crossing formula.” | Cardy derived it by non-rigorous CFT; Smirnov proved it for triangular site percolation. |
| “SLE was invented by Werner (or by Smirnov).” | SLE was introduced by **Schramm** (2000). Werner’s Fields is for developing SLE and 2D Brownian geometry, largely with Lawler and Schramm. |
| “The 2010 medal is only percolation.” | The IMU citation names percolation **and** the planar Ising model. |
| “Onsager’s solution is the same as conformal invariance of Ising.” | Onsager computed the 2D free energy (1944). Conformal invariance of observables and interfaces is a later geometric statement. |
| “Once you have SLE, every 2D model is solved.” | SLE is a candidate limit law. Identifying a lattice model with a given $$\kappa$$ is a separate theorem, often still open. |

---

## Links

- IMU Fields Medals 2010 (requested index): [mathunion.org/…/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- IMU / ICM 2010 Smirnov page (working archive): [Fields Medal – Stanislav Smirnov](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-stanislav-smirnov.html)
- IMU Fields Medal index: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Wikipedia: [Stanislav Smirnov](https://en.wikipedia.org/wiki/Stanislav_Smirnov)
- arXiv: [0909.4499](https://arxiv.org/abs/0909.4499) (Smirnov, critical percolation); [0910.2045](https://arxiv.org/abs/0910.2045) (Chelkak–Smirnov, Ising); search [Smirnov percolation Cardy](https://arxiv.org/search/?query=Smirnov+percolation+Cardy&searchtype=all)
- Course: [Werner / SLE]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/), [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase_Transitions/), [Villani]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/)

---

## References

1. International Mathematical Union, Fields Medals 2010 citation for Stanislav Smirnov (IMU / ICM Hyderabad 2010 materials).
2. **S. Smirnov**, “Critical percolation in the plane: conformal invariance, Cardy’s formula, scaling limits,” *C. R. Acad. Sci. Paris Sér. I Math.* 333 (2001), 239–244; longer account arXiv:0909.4499.
3. **J. L. Cardy**, “Critical percolation in finite geometries,” *J. Phys. A* 25 (1992), L201–L206.
4. **O. Schramm**, “Scaling limits of loop-erased random walks and uniform spanning trees,” *Israel J. Math.* 118 (2000), 221–288.
5. **D. Chelkak and S. Smirnov**, “Universality in the 2D Ising model and conformal invariance of fermionic observables,” *Invent. Math.* 189 (2012), 515–580, arXiv:0910.2045.
6. **S. Smirnov**, “Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model,” *Ann. of Math.* 172 (2010), 1441–1473.
7. Wikipedia, [Stanislav Smirnov](https://en.wikipedia.org/wiki/Stanislav_Smirnov); course portraits of [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) and [Duminil-Copin]({{ site.baseurl }}/contents/en/chapter02/02_19_Duminil_Copin_Phase_Transitions/).

---

## Further directions

- Read a survey of the colour-switching argument before the *Comptes Rendus* note; after [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/), write a half-page on the order SLE axioms → Cardy → identification with $$\mathrm{SLE}_6$$.
- Seminar option: a one-page “what is still open in 2D percolation” brief that does **not** claim universality is a theorem.

## Video tham khảo

- **xem trước** — [Stanislav Smirnov - 2d Percolation Revisited](https://www.youtube.com/watch?v=6QOnfvWqVoo) — MIT Department of Mathematics, English. Watch first. “Stanislav Smirnov - 2d Percolation Revisited” orients the lesson’s aim: State, at slogan level, what Bernoulli percolation is, and distinguish site percolation from bond percolation.
- [Stanislav Smirnov, Percolation crossings and complex analysis](https://www.youtube.com/watch?v=6hCSSCV7lvQ) — Clay Mathematics Institute, English. A second pass once the main claim is in view: State, at slogan level, what Bernoulli percolation is, and distinguish site percolation from bond percolation.
- [Stanislav Smirnov - Percolation revisited](https://www.youtube.com/watch?v=ZNpbvrhfWPA) — Department of Mathematics - Northwestern University, English. Further depth after the first two, still tied to this lesson: State, at slogan level, what Bernoulli percolation is, and distinguish site percolation from bond percolation.
