---
layout: post
title: "Okounkov’s Bridges: Probability, Representations, and Geometry (Fields Medal 2006)"
chapter: '02'
order: 27
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Picture a game that sounds like pure recreational combinatorics: shuffle a deck of $$n = 1{,}000{,}000$$ numbered cards completely at random, and find the length of its **longest increasing subsequence**. Who would ever guess that the statistical fluctuations of that number follow the **exact same probability law** (the Tracy–Widom distribution) as the largest eigenvalue of a giant random matrix? And harder still to believe: the exact same box diagrams (Young diagrams) governing a shuffled deck of cards are quietly running both **curve counting in algebraic geometry** and **instanton counting in four-dimensional quantum gauge theory**!

The mathematician who saw—and engineered—the bridges connecting those three continents is **Andrei Okounkov**. At ICM Madrid in 2006—alongside **Terence Tao**, **Wendelin Werner**, and **Grigori Perelman**—he received the **Fields Medal** with one razor-sharp sentence:

> For his contributions bridging probability, representation theory and algebraic geometry.

As the IMU press essay candidly observed, Okounkov’s work refuses to sit in a single drawer: two recurring instincts—**randomness** and **classical representation theory** (symmetric groups and Young diagrams)—keep unlocking central problems in enumerative algebraic geometry and statistical mechanics. We start with a hands-on calculation for $$S_3$$, then walk across his three great bridges—melted crystals, Okounkov–Pandharipande Gromov–Witten theory, and Nekrasov–Okounkov instanton counting—while keeping credit sharp: he did not classify all representations of all groups, nor invent gauge theory.

**Lesson roadmap:** Background Knowledge Map ($$S_n$$ representations, Young diagrams, Fock space) → Hand-verifiable worked example: computing the complete Plancherel distribution on $$S_3$$ and running Robinson–Schensted on $$(2,1,3)$$ → From BDJ to melted crystals and real algebraic curves → Deep-Dive Explanation (Read Slowly): 4 steps linking partitions to Gromov–Witten ($$\mathbb{P}^1$$), Seiberg–Witten instantons, and Schur processes → What Okounkov did not claim.

---

## Learning objectives

After this lecture you should be able to:

- State the 2006 IMU citation as a **bridging program** across probability, representation theory, and algebraic geometry.
- Compute the **Plancherel measure** by hand for all partitions of $$n = 3$$ and trace Robinson–Schensted insertion on a concrete permutation.
- Explain the link between longest increasing subsequences, random-matrix Tracy–Widom laws, and Okounkov’s geometric bridge via **random surfaces**.
- Summarize **Okounkov–Pandharipande**: turning equivariant Gromov–Witten generating functions of $$\mathbb{P}^1$$ into Fock-space operator expectations governed by the **2-Toda hierarchy**.
- Describe **Nekrasov–Okounkov** accurately as a dictionary identifying regularized instanton partition functions with random partitions and Seiberg–Witten prepotentials.
- Name **Schur measures / Schur processes** (Okounkov, Reshetikhin, Borodin, Olshanski) and **melted crystals / dimers** (Kenyon–Okounkov) without exaggerating scope.

**Prerequisites.** Partitions of an integer; the symmetric group $$S_n$$ at the level “irreducible representations are labelled by Young diagrams”; generating functions. Algebraic geometry at the level “curves in a variety can be counted in a virtual sense” is enough for Gromov–Witten slogans. No quantum field theory required.

**Seminar links.** Same-year neighbor: [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/). Geometry of moduli: [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) (different moduli, similar “spaces of shapes become dynamical or probabilistic”).

---

## Background Knowledge Map: What Do $$S_n$$ Representations, Young Diagrams, and Fock Space Study?

### 1. Representation theory of the symmetric group $$S_n$$
**Representation theory** realizes abstract symmetry groups as invertible matrices and breaks them into indivisible "atoms" called **irreducible representations**. For the symmetric group $$S_n$$ (all $$n!$$ permutations), irreducible representations correspond **1–1** with **partitions** $$\lambda = (\lambda_1 \ge \lambda_2 \ge \cdots)$$ of $$n$$, drawn as **Young diagrams** (rows of stacked boxes).

### 2. Random Young diagrams and limit shapes
Because $$\sum_{\lambda \vdash n} (\dim\lambda)^2 = n!$$, representation theory hands probability a privileged distribution—the **Plancherel measure**:

$$
\mathbb{P}(\lambda) = \frac{(\dim\lambda)^2}{n!}.
$$

In the late 1970s, **Vershik–Kerov** and independently **Logan–Shepp** proved that as $$n \to \infty$$, a Plancherel-random diagram rescaled by $$\sqrt{n}$$ concentrates tightly around a smooth deterministic **limit shape**!

### 3. Fock space—turning Young diagrams into quantum operators
Declare every Young diagram $$\lambda$$ (of any size $$n \ge 0$$) to be an orthonormal basis vector $$\vert\lambda\rangle$$ of an infinite-dimensional Hilbert space called **Fock space** (the state space of 1D fermions). Adding or removing a box becomes a creation/annihilation operator—and remarkably, generating functions of **enumerative geometry (Gromov–Witten)** become vacuum matrix elements $$\langle 0 \vert \cdots \vert 0 \rangle$$ of those exact operators!

---

## 1. Hand-Verifiable Worked Example: Complete Plancherel Measure on $$S_3$$ and Robinson–Schensted

Take $$n = 3$$ ($$3! = 6$$ permutations). The integer $$3$$ has exactly **3 partitions**:

| Partition $$\lambda$$ | Young diagram | Standard tableaux ($$\dim\lambda$$) | Plancherel weight $$\frac{(\dim\lambda)^2}{3!}$$ |
|---|---|---|---|
| $$(3)$$ | 1 row of 3 boxes | $$1$$ (trivial rep) | $$1^2 / 6 = 1/6$$ |
| $$(2, 1)$$ | Row of 2 + row of 1 | $$2$$ (standard 2D rep) | $$2^2 / 6 = 4/6 = 2/3$$ |
| $$(1, 1, 1)$$ | 1 column of 3 boxes | $$1$$ (sign rep) | $$1^2 / 6 = 1/6$$ |

Total probability: $$\frac{1}{6} + \frac{4}{6} + \frac{1}{6} = 1$$! Notice how even at $$n = 3$$, the balanced middle shape $$(2, 1)$$ captures **$$2/3$$** of the probability—the miniature seed of the Vershik–Kerov–Logan–Shepp limit shape!

**Run Robinson–Schensted insertion on the permutation $$(2, 1, 3) \in S_3$$:**
- Insert $$2$$ into the empty tableau $$\to$$ row 1: `[2]`.
- Insert $$1$$: since $$1 < 2$$, $$1$$ bumps $$2$$ down to row 2 $$\to$$ row 1: `[1]`, row 2: `[2]`.
- Insert $$3$$: since $$3 > 1$$, append $$3$$ to row 1 $$\to$$ row 1: `[1, 3]`, row 2: `[2]`.

The resulting shape is **$$(2, 1)$$**, and its first row has length $$\lambda_1 = 2$$—**identical to the longest increasing subsequence** `(2, 3)` or `(1, 3)` of `(2, 1, 3)`! Running all 6 permutations of $$S_3$$ yields 1 copy of $$(3)$$, 4 copies of $$(2,1)$$, and 1 copy of $$(1,1,1)$$, matching the Plancherel measure **exactly**!

---

## 2. From BDJ Fluctuations to Melted Crystals and Algebraic Curves

In 1999, **Baik–Deift–Johansson (BDJ)** proved that fluctuations of $$\lambda_1$$ around $$2\sqrt{n}$$ (scaled by $$n^{1/6}$$) follow the **Tracy–Widom** distribution of the largest eigenvalue of a Gaussian Hermitian random matrix, conjecturing the same match for the joint law of the top $$k$$ rows. **Okounkov (2000)** proved that conjecture via a geometric bridge: both random-matrix moments and Plancherel moments count the same objects—**random surfaces** (ramified covers of the sphere / ribbon graphs)! (Independent determinantal proofs were given by **Borodin–Okounkov–Olshanski** and **Johansson**.)

Next, **Kenyon–Okounkov** (and Sheffield) analyzed **random 3D plane partitions** ("melted crystals" and planar **dimer** lozenge tilings): randomly melting unit cubes out of a 3D corner creates frozen flat facets separated from a chaotic liquid core by an *arctic curve*—which Kenyon–Okounkov proved is always a **real algebraic curve** (a Harnack curve)! Once again, statistical mechanics landed squarely inside algebraic geometry.

---

## 3. Deep-Dive Explanation: How Okounkov’s Three Bridges Compute Each Other’s Answers (Read Slowly)

Follow four steps to see how Young diagrams unlock enumerative geometry and 4D gauge theory:

#### Step 1: Equivariant Gromov–Witten theory of $$\mathbb{P}^1$$ via Fock space (Okounkov–Pandharipande)
**Gromov–Witten theory** virtually counts holomorphic maps from genus-$$g$$ curves into a target variety $$X$$. For target **$$\mathbb{P}^1$$**, **Okounkov and Pandharipande** (*Ann. of Math.* 163, 2006; [arXiv:math/0207233](https://arxiv.org/abs/math/0207233)) identified the stationary sector with **Hurwitz numbers** (counting ramified covers—multiplication in the center of the symmetric group algebra!) modified by **completed cycle** operators. Translated into the Young-diagram basis of Fock space, the entire equivariant Gromov–Witten generating function of $$\mathbb{P}^1$$ becomes a tau-function of the **2-Toda integrable hierarchy**!

#### Step 2: Bridging Gromov–Witten and Donaldson–Thomas (MNOP conjectures)
With **Maulik, Nekrasov, and Pandharipande**, Okounkov formulated the celebrated MNOP conjectures linking two totally different threefold counting theories: **Gromov–Witten** (counting curves) and **Donaldson–Thomas** (counting ideal sheaves—which on toric threefolds reduces right back to counting **3D plane partitions**!).

#### Step 3: Nekrasov instanton partition functions become random partitions (Nekrasov–Okounkov)
In 2002, **Nikita Nekrasov** gave a rigorous equivariant localization definition for the instanton partition function of 4D $$\mathcal{N}=2$$ supersymmetric gauge theory. By Atiyah–Bott localization, the fixed points on instanton moduli space are indexed by tuples of **Young diagrams**! **Nekrasov and Okounkov** ([arXiv:math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)) rewrote Nekrasov’s sum as a **random-partition measure** (deforming Plancherel) and used **limit-shape thermodynamics** to prove its surface tension matches the **Seiberg–Witten prepotential**!

#### Step 4: Schur measures and Schur processes unify determinantal probability
Generalizing Plancherel by weighting diagrams with Schur functions $$s_\lambda(x)s_\lambda(y)$$, **Okounkov** introduced **Schur measures**, and **Okounkov–Reshetikhin** (alongside **Borodin–Okounkov–Olshanski**) developed **Schur processes**—measures on sequences of partitions with exact determinantal correlation functions governing growth models, plane partitions, and dimers.

Summary of Okounkov’s triangle of bridges:

$$
\text{Probability (Plancherel / Schur)}
\;\longleftrightarrow\;
\text{Representations (} S_n\text{, Fock space)}
\;\longleftrightarrow\;
\text{Geometry (Gromov–Witten, Seiberg–Witten)}.
$$

---

## 4. What Okounkov Did Not Claim, and Why a Fields Medal

Okounkov did **not** classify all irreducible representations of all groups, did **not** replace algebraic geometry by combinatorics, and did **not** invent gauge theory or Seiberg–Witten theory. Rather, as Giovanni Felder’s ICM exposition (*"The work of Andrei Okounkov"*, [arXiv:math/0609847](https://arxiv.org/abs/math/0609847)) highlights, the 2006 Fields Medal honors a rare **two-way dictionary** letting probability, representation theory, and algebraic geometry compute one another’s hardest answers.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Okounkov classified all representations.” | He used representation theory of symmetric (and related) groups as a bridge; classification of representations is a different project. |
| “Okounkov invented the Plancherel limit shape.” | Vershik–Kerov and Logan–Shepp established the shape; Okounkov refined connections and applications. |
| “Okounkov invented gauge theory / Seiberg–Witten.” | Nekrasov defined the regularized partition function; Nekrasov–Okounkov identified it with random partitions. |
| “Gromov–Witten theory is only combinatorics.” | The invariants are geometric; some generating functions admit combinatorial/representation-theoretic formulas. |
| “Plancherel measure is uniform on partitions.” | It weights a diagram by $$(\dim\lambda)^2/n!$$, not by $$1/p(n)$$. |
| “The 2006 medal is only random matrices.” | Random-matrix links are one early chapter; GW and instanton bridges are equally central in public accounts. |
| “Schur processes are Okounkov alone.” | Okounkov, Reshetikhin, Borodin, Olshanski, and others. |

---

## Links

- IMU Fields Medals 2006: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2006](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2006)
- IMU Okounkov citation PDF: [https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2006/OkounkovengDEF.pdf](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2006/OkounkovengDEF.pdf)
- Wikipedia, Andrei Okounkov: [https://en.wikipedia.org/wiki/Andrei_Okounkov](https://en.wikipedia.org/wiki/Andrei_Okounkov)
- Felder, “The work of Andrei Okounkov”: [https://arxiv.org/abs/math/0609847](https://arxiv.org/abs/math/0609847)
- Okounkov, “Random partitions and instanton counting”: [https://arxiv.org/abs/math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)
- Okounkov–Pandharipande, equivariant GW of $$\mathbb{P}^1$$: [https://arxiv.org/abs/math/0207233](https://arxiv.org/abs/math/0207233)
- arXiv author search: [https://arxiv.org/search/math?searchtype=author&query=Okounkov%2C+A](https://arxiv.org/search/math?searchtype=author&query=Okounkov%2C+A)
- Course: [Perelman, same ICM]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/)

---

## References

1. IMU, Fields Medal 2006 citation and press essay for Andrei Okounkov (mathunion.org PDFs).
2. **G. Felder**, “The work of Andrei Okounkov,” [arXiv:math/0609847](https://arxiv.org/abs/math/0609847).
3. Limit shapes: Vershik–Kerov; Logan–Shepp. Fluctuations: Baik–Deift–Johansson; Okounkov’s proof; Borodin–Okounkov–Olshanski.
4. **A. Okounkov and R. Pandharipande**, Gromov–Witten / Hurwitz / completed cycles series, including *Ann. of Math.* **163** (2006) and [arXiv:math/0207233](https://arxiv.org/abs/math/0207233).
5. **N. Nekrasov and A. Okounkov**, Seiberg–Witten theory and random partitions (surveyed in [arXiv:math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)).
6. Schur measures and Schur processes: Okounkov; Okounkov–Reshetikhin; Borodin–Okounkov–Olshanski and later surveys.
7. Dimers / algebraic limit shapes: Kenyon–Okounkov (and related work).
8. Course: [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/), [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/).

---

## Further directions

- Read Felder’s short portrait, then one Okounkov–Pandharipande introduction, then the instanton survey—do not start with Seiberg–Witten as physics.
- Compare Plancherel with uniform measure on partitions: same diagrams, different typical shapes.
- Seminar A3: a one-page “bridge diagram” with three nodes (probability, representations, enumerative geometry) and two edges you can actually name (Plancherel; GW/Hurwitz operators).

## Video tham khảo

- **xem trước** — [On the crossroads of enumerative geometry and representation theory – Andrei Okounkov – ICM2018](https://www.youtube.com/watch?v=zlQ23vRAOCQ) — Rio ICM2018, English. Watch first. “On the crossroads of enumerative geometry and representation theory – Andrei Okounkov –…” orients the lesson’s aim: Restate the 2006 IMU citation as a bridge, not as a classification theorem.
- [Andrei Okounkov | Classical and quantum integrable systems in enumerative geometry](https://www.youtube.com/watch?v=xZNGyBFR0ao) — Harvard CMSA, English. A second pass once the main claim is in view: Restate the 2006 IMU citation as a bridge, not as a classification theorem.
