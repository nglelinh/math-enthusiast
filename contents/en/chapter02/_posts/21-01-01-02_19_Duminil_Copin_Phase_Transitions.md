---
layout: post
title: "Duminil-Copin’s Phase Transitions (Fields Medal 2022)"
chapter: '02'
order: 19
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Think of an ordinary iron bar magnet. As you heat it up, its magnetism weakens steadily; then, at one razor-sharp threshold—the Curie temperature, around $$770^\circ\text{C}$$—its magnetism vanishes completely. Or imagine water seeping through porous rock: nudge the density of open pores across a hair-thin threshold, and water suddenly finds a path all the way across the stone. These abrupt macroscopic shifts emerging from millions of tiny random local interactions are called **phase transitions**.

For decades, the mathematics of phase transitions was trapped in a strange paradox. In **two dimensions**, physicists and mathematicians had Onsager’s exact solution alongside the conformal-invariance machinery of [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/) and [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/). In **high dimensions** ($$d \ge 5$$), random paths rarely collide, so mean-field theory and the lace expansion worked smoothly. Yet the two dimensions where physical reality actually lives—**dimension three** (magnets and fluids) and **dimension four** (the spacetime of quantum field theory)—remained a stubborn blind spot packed with problems open since the 1970s and 1980s.

In 2022, **Hugo Duminil-Copin** received the **Fields Medal** for *"solving longstanding problems in the probabilistic theory of **phase transitions** in statistical physics, especially in dimensions **three** and **four**."* Together with collaborators, he proved **continuity** and **sharpness** of the phase transition for 3D Ising-type models; with **Michael Aizenman**, he proved **mean-field critical behavior** of the 4D Ising model and **triviality** of four-dimensional Euclidean scalar quantum field theory; and in 2D, he and collaborators classified continuity vs. discontinuity for dependent **Fortuin–Kasteleyn (FK)** percolation for all parameters, proved universality on isoradial graphs, and established **large-scale rotational invariance** as a step toward conformal invariance. Although Smirnov was his doctoral advisor, the 2022 medal is a sequel chapter in new dimensions, not a replay of 2010—and conformal invariance of the 3D Ising model remains open.

**Lesson roadmap:** Key ideas (percolation, Ising, and FK random-cluster models) → Hand-verifiable worked examples (a 4-edge 2D percolation cell and a $$2\times 2$$ Ising square) → Why dimensions 3 and 4 resisted for decades → Explanation: OSSS sharpness, random-current continuity in 3D, and multiscale triviality in 4D → Honest attribution & boundaries with Smirnov (2010) and Werner (2006).

---

## Learning objectives

After this lecture you should be able to:

- State the IMU 2022 short citation and summarize the three blocks of the long citation: 3D Ising continuity/sharpness; 4D mean-field / triviality with Aizenman; 2D FK continuity-discontinuity, universality, and rotational invariance.
- Compute by hand the crossing polynomial on a small 2D percolation cell and the Boltzmann weights of a $$2\times 2$$ Ising square to see critical thresholds and order parameters in action.
- Define **phase transition**, **critical point**, **continuity vs. discontinuity** of an order parameter, and **sharpness**.
- Explain why dimension **three** lacks exact planar solutions and why dimension **four** is the upper critical threshold ($$2 + 2 = 4$$) for scalar fields.
- Attribute each landmark accurately to its collaborators (**Aizenman–Duminil-Copin**, **Aizenman–Duminil-Copin–Sidoravicius**, **Duminil-Copin–Raoufi–Tassion**, and the 2D FK teams).
- Distinguish **large-scale rotational invariance** (2D FK) from **full conformal invariance**, and reject claims about 3D Ising conformal field theory.

**Prerequisites.** Independent Bernoulli percolation as a cartoon (edges open with probability $$p$$); the idea of an infinite connected component; a Hamiltonian and a Gibbs measure for the Ising model at inverse temperature $$\beta$$. No prior SLE or constructive QFT is required.

**Seminar links.** Same 2022 class: [Maynard]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/), [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/). Probability-and-physics cousins: [Smirnov / percolation]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/), [Werner / SLE]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/). Kinetic statistical physics of a different kind: [Deng]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/).

---

## Key ideas: What Does Lattice Statistical Mechanics Study?

Probabilistic statistical mechanics asks one central question: *how do simple, purely local random rules on an infinite grid conspire to produce sudden global changes?* Three lattice models form the shared language of the field.

### 1. Bernoulli percolation
Take the infinite grid $$\mathbb{Z}^d$$. Open each edge independently with probability $$p \in [0, 1]$$ and close it with probability $$1 - p$$. Does an **infinite connected cluster** of open edges appear? By Kolmogorov’s zero-one law, there is a sharp **critical probability** $$p_c \in (0, 1)$$: for $$p < p_c$$ all clusters are finite almost surely; for $$p > p_c$$ an infinite cluster exists almost surely.

### 2. The Ising model
Place a magnetic spin $$\sigma_x \in \{+1, -1\}$$ at every vertex $$x \in \mathbb{Z}^d$$. Each configuration $$\sigma$$ receives Boltzmann weight proportional to $$e^{-\beta H(\sigma)}$$, where $$\beta = 1/(k_B T)$$ is inverse temperature and the energy is

$$
H(\sigma) = -\sum_{\langle x,y\rangle} \sigma_x \sigma_y.
$$

Aligned neighbors lower the energy by $$-1$$. At high temperature (small $$\beta$$), thermal noise dominates and spontaneous magnetization $$M(\beta) = 0$$; at low temperature ($$\beta > \beta_c$$), spins align macroscopically so $$M(\beta) > 0$$.

### 3. The Fortuin–Kasteleyn (FK) random-cluster model
In the 1970s, Fortuin and Kasteleyn unified percolation and the Ising/Potts models into a two-parameter family $$(p, q)$$: each edge configuration $$\omega$$ has probability proportional to

$$
p^{\#(\text{open edges})}(1-p)^{\#(\text{closed edges})} \, q^{k(\omega)},
$$

where $$k(\omega)$$ counts the connected clusters. Setting $$q = 1$$ recovers independent percolation; setting $$q = 2$$ recovers the Ising model (by coloring each cluster independently $$\pm 1$$)!

---

## 1. Hand-Verifiable Worked Examples: A 4-Edge Percolation Cell and a $$2\times 2$$ Ising Square

### Example 1: Seeing a sharp threshold emerge from a 4-edge cell
Take the simplest 2D bridge network: two parallel paths from left to right, each consisting of two edges in series (4 edges total). A single 2-edge series path is open with probability $$p^2$$, so the probability that at least one of the two parallel paths connects left to right is:

$$
f(p) = 1 - (1 - p^2)^2 = 2p^2 - p^4.
$$

Now watch what happens when we zoom out—replacing each edge by a 4-edge cell, iterating $$p \mapsto f(p) \mapsto f(f(p)) \mapsto \cdots$$:
- Starting at $$p = 0.5$$: $$f(0.5) = 0.4375 \to 0.346 \to 0.225 \to 0.099 \to \cdots \to 0$$!
- Starting at $$p = 0.7$$: $$f(0.7) = 0.7399 \to 0.795 \to 0.865 \to 0.937 \to \cdots \to 1$$!
- The unstable fixed point solving $$2p^2 - p^4 = p$$ is $$p_c = \frac{\sqrt{5}-1}{2} \approx 0.618$$.

Even in this toy 4-edge cell, you see **sharpness** with your own eyes: nudge $$p$$ slightly below $$p_c$$ and large-scale connectivity collapses exponentially to $$0$$; nudge it slightly above $$p_c$$ and connectivity shoots to $$1$$. (On the true square lattice $$\mathbb{Z}^2$$, Kesten proved in 1980 that $$p_c = 1/2$$.)

### Example 2: A $$2\times 2$$ Ising square (4 vertices, 4 edges)
There are $$2^4 = 16$$ spin configurations:
- 2 fully aligned configurations (all $$+1$$ or all $$-1$$): 4 aligned pairs, energy $$H = -4$$, weight $$e^{4\beta}$$.
- 2 checkerboard configurations: 4 opposite pairs, energy $$H = +4$$, weight $$e^{-4\beta}$$.
- 12 mixed configurations: energy $$H = 0$$, weight $$1$$.

At high temperature ($$\beta = 0.1$$), aligned states outweigh mixed states by only $$e^{0.4} \approx 1.49$$, so the 12 disordered states dominate. At low temperature ($$\beta = 2$$), aligned states carry weight $$e^8 \approx 2981$$ and swallow almost all the probability! As lattice size $$N \to \infty$$, this tug-of-war between energy and entropy sharpens into a true phase transition at $$\beta_c$$.

---

## 2. Why Dimensions 3 and 4 Resisted for Decades

**Peierls (1936)** proved a transition exists for Ising in every dimension $$d \ge 2$$, and **Onsager (1944)** solved 2D Ising exactly, proving continuity. In **dimension 3**, all planar algebraic tricks fail: by the 1980s, nobody could prove whether 3D Ising magnetization vanished continuously at criticality ($$M(\beta_c) = 0$$) or jumped, nor establish general sharpness across dependent models.

In **dimension 4**, the obstacle sits right at the geometry of quantum field theory. Brownian paths (and the random-current paths representing Ising) have Hausdorff dimension $$2$$. Because $$2 + 2 = 4$$, two independent random paths in $$\mathbb{R}^d$$:
- collide heavily in $$d = 2, 3$$ (strong non-Gaussian interaction);
- almost never meet in $$d \ge 5$$ (where Aizenman and Fröhlich proved triviality in the early 1980s);
- **sit right on the borderline in $$d = 4$$!** At $$d = 4$$, intersection probabilities decay agonizingly slowly—like $$1/\ln L$$ rather than a power law—which blocked a complete proof for 40 years.

---

## 3. Explanation: Conquering Dimensions 3 and 4 Without Exact Formulas

Without an Onsager formula in 3D or 4D, Duminil-Copin and his collaborators forged a four-part probabilistic machine:

#### Step 1: OSSS randomized-algorithm inequality proves Sharpness
Let $$A$$ be the event that an open cluster connects the origin to the boundary of a box of radius $$n$$. To prove **sharpness** (exponential decay of connectivity for every $$p < p_c$$), one must show the derivative $$\frac{d}{dp}\mathbb{P}_p(A)$$ is large whenever $$\mathbb{P}_p(A)$$ is away from $$0$$ and $$1$$. **Duminil-Copin, Raoufi, and Tassion** imported the **OSSS inequality** from theoretical computer science (O’Donnell–Saks–Schramm–Servedio): any randomized decision tree that determines $$A$$ by querying edges one by one must reveal some edge with large influence. Designing a clever exploration algorithm that reveals clusters layer by layer, they proved a differential inequality forcing exponential decay throughout the entire subcritical phase—settling sharpness for a vast class of dependent models!

#### Step 2: Random currents prove Continuity of 3D Ising magnetization
**Aizenman, Duminil-Copin, and Sidoravicius (2015)** used the **random-current representation**, which rewrites spin correlations $$\langle \sigma_x \sigma_y \rangle$$ in terms of connectivity in a random graph of even-degree currents. Via the switching lemma, proving $$M(\beta_c) = 0$$ reduces to showing that two independent random currents at $$\beta_c$$ possess **no infinite cluster**. Combining reflection-positivity bounds with geometric percolation arguments, they ruled out an infinite cluster at $$\beta_c$$, proving $$M(\beta_c) = 0$$—the 3D Ising phase transition is **continuous**!

#### Step 3: Multiscale intersection estimates prove 4D Triviality (Aizenman–Duminil-Copin, 2021)
In *Annals of Mathematics* (2021), **Aizenman and Duminil-Copin** tackled the marginal dimension $$d = 4$$. In the random-current picture, the Ursell 4-point function $$U_4$$—which measures how far the field deviates from a Gaussian—is controlled directly by the probability that two independent random currents intersect. Through a delicate **multiscale analysis**, they proved that in 4D this intersection probability decays at least as $$C / (\ln L)^c \to 0$$ as $$L \to \infty$$! Consequently, every higher correlation function factorizes by Wick’s rule in the continuum scaling limit: critical 4D Ising exhibits **mean-field behavior**, and 4D Euclidean scalar $$\varphi^4$$ quantum field theory is **trivial**.

#### Step 4: Planar FK classification and large-scale rotational invariance
In 2D, Duminil-Copin and collaborators (Tassion, Manolescu, Sidoravicius, Kozlowski, Krachun, Oulamara, and others) proved that the planar FK transition is **continuous for $$1 \le q \le 4$$** and **discontinuous for $$q > 4$$**, established **universality** on isoradial graphs, and proved **large-scale rotational invariance**—showing that zoomed-out critical FK clusters forget the $$90^\circ$$ axes of the square lattice, a major milestone toward full 2D conformal invariance.

Summary of the breakthrough pipeline:

$$
\text{Lattice models (Ising / FK)}
\;\longleftrightarrow\;
\text{Geometric representations (Random currents / FK)}
\;\longleftrightarrow\;
\text{OSSS + Multiscale bounds}
\;\Longrightarrow\;
\text{3D Sharp \& Continuous + 4D Trivial}.
$$

---

## 4. Honest Attribution and What the Medal Does Not Claim

| Result (slogan) | Credit |
|-----------------|--------|
| Continuity of 3D Ising magnetization | Aizenman–Duminil-Copin–Sidoravicius and the random-current school |
| Sharpness for Ising-type / percolation models | Duminil-Copin–Raoufi–Tassion (and earlier sharpness literature) |
| 4D mean-field Ising and $$\varphi^4$$ triviality | Aizenman–Duminil-Copin (2021) |
| FK continuity/discontinuity for all $$q$$; isoradial universality | Duminil-Copin with Tassion, Manolescu, and others |
| Large-scale rotational invariance in critical planar FK-type models | Duminil-Copin with Kozlowski, Krachun, Manolescu, Oulamara, … |
| 2D percolation / Ising conformal invariance | **Smirnov (2010 Fields)** — see [that essay]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/) |
| SLE as the scaling-limit language | **Schramm; Lawler–Schramm–Werner; Werner (2006 Fields)** — see [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) |

*(An earlier landmark with Smirnov in 2012 proved the connective constant of self-avoiding walks on the honeycomb lattice is $$\sqrt{2+\sqrt{2}}$$—a gem of his early career, distinct from the 3D/4D emphasis of the 2022 citation.)*

Duminil-Copin (born 1985 in France) studied at ENS and Paris-Sud, completed his PhD in Geneva under Smirnov (2011), and holds professorships at the University of Geneva and IHÉS.

**Do not claim:** full conformal invariance of 3D Ising; a classification of all lattice models; a solution of 3D constructive QFT; or that SLE was reinvented in 2022.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “He proved conformal invariance of 3D Ising.” | Open. The 2D work is rotational invariance as a *step toward* conformal invariance of FK models. |
| “He proved conformal invariance in 2D (the Smirnov theorem).” | Smirnov (2010) is the conformal-invariance portrait; Duminil-Copin extends the 2D FK program and moves to 3D/4D. |
| “Triviality means the 4D Ising model is uninteresting.” | It means the *continuum scaling limit* is Gaussian, a deep statement about QFT. |
| “Sharpness is the same as continuity.” | Sharpness is about exponential decay off criticality; continuity is about the order parameter at $$\beta_c$$. |
| “The 2022 medal is a solo 3D proof.” | The IMU text says “together with collaborators”; 4D is with Aizenman. |
| “Phase transition = existence of $$p_c$$.” | Existence was often known; the medal is about the *nature* of the transition. |

---

## Video and reading links

No course video-research pack is attached to this lesson.

1. IMU Fields Medals 2022 (short citation): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022).
2. IMU long citation (PDF): [IMU_Fields22_Duminil-Copin_citation.pdf](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/IMU_Fields22_Duminil-Copin_citation.pdf).
3. Encyclopedia: [Hugo Duminil-Copin](https://en.wikipedia.org/wiki/Hugo_Duminil-Copin).
4. Quanta profile (2022): [Hugo Duminil-Copin Wins the Fields Medal](https://www.quantamagazine.org/hugo-duminil-copin-wins-the-fields-medal-20220705/).
5. arXiv search: [Duminil-Copin Ising](https://arxiv.org/search/?query=Duminil-Copin+Ising&searchtype=all); rotational invariance preprint [arXiv:2012.11672](https://arxiv.org/abs/2012.11672).
6. Related essays in this chapter: [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/), [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/), [Maynard]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/).

**Status reminder:** 3D continuity/sharpness and 4D triviality with collaborators—**not** 3D conformal invariance.

---

## References

1. International Mathematical Union, Fields Medal 2022 — Hugo Duminil-Copin, short and long citations (mathunion.org).
2. **M. Aizenman, H. Duminil-Copin**, *Marginal triviality of the scaling limits of critical 4D Ising and $$\varphi^4$$ models*, *Ann. of Math.* 194 (2021).
3. Works of Duminil-Copin with **Aizenman, Sidoravicius, Raoufi, Tassion, Manolescu**, and others on continuity, sharpness, and planar FK models (see the IMU citation for the grouping).
4. **H. Duminil-Copin, S. Smirnov**, connective constant of the honeycomb lattice, *Ann. of Math.* 175 (2012)—formation, not the 3D/4D citation.
5. Background: Onsager’s 2D Ising solution; Grimmett’s random-cluster book; surveys of constructive triviality (Aizenman, Fröhlich, …) as pointers.
6. Course: [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/), [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/), [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/).

---

## Further directions

- Learn the FK representation until you can say why Potts models are percolation models with dependence.
- Read an expository account of random currents before attempting the 3D continuity paper.
- Seminar A3 option: a one-page brief on *open conformal questions*—full 2D FK conformal invariance; 3D Ising CFT as physics versus mathematics—without awarding those theorems to 2022.
- If you prefer exact combinatorics, start from the honeycomb connective constant (with Smirnov) and then jump to the IMU’s 3D/4D list so the medal’s emphasis stays visible.

## Video tham khảo

- **xem trước** — [Fields Medal: Hugo Duminil-Copin](https://www.youtube.com/watch?v=5dXulZVstbY) — Simons Foundation, English. Watch first. “Fields Medal: Hugo Duminil-Copin” orients the lesson’s aim: State the IMU 2022 short citation and paraphrase the long citation’s three blocks: 3D Ising-type continuity/sharpness; 4D mean-field / triviality with Aizenman; 2D FK continuity-di…
- [Hugo DUMINIL-COPIN - Critical phenomena through the lens of the Ising model](https://www.youtube.com/watch?v=jNOffVsULVM) — Institut Fourier, English. A second pass once the main claim is in view: State the IMU 2022 short citation and paraphrase the long citation’s three blocks: 3D Ising-type continuity/sharpness; 4D mean-field / triviality with Aizenman; 2D FK continuity-di…
- [Lecture: Duminil-Copin | September 29](https://www.youtube.com/watch?v=s3KgdQXjsy8) — Heidelberg Laureate Forum, English. Further depth after the first two, still tied to this lesson: State the IMU 2022 short citation and paraphrase the long citation’s three blocks: 3D Ising-type continuity/sharpness; 4D mean-field / triviality with Aizenman; 2D FK continuity-di…
