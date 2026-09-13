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

**Andrei Okounkov** received the **Fields Medal 2006** at ICM Madrid. The official IMU citation is a single bridging sentence, and this course keeps it official:

> For his contributions bridging probability, representation theory and algebraic geometry.

The longer IMU press text (2006) adds that the work is hard to classify because it touches many areas, with two recurring themes: **randomness** and **classical representation theory**, used against problems in algebraic geometry and statistical mechanics. This essay is for learners who have met partitions, symmetric groups, and the idea of a generating function, and who want to see why a measure on Young diagrams can speak to Gromov–Witten invariants or to instanton counting. It does **not** claim that Okounkov classified all representations, invented gauge theory, or replaced algebraic geometry by combinatorics.

The 2006 class also included **Terence Tao**, **Wendelin Werner**, and **Grigori Perelman** (who declined). Four medals, four styles of “bridge.”

---

## Learning objectives

After this lecture you should be able to:

- Restate the 2006 IMU citation as a **bridge**, not as a classification theorem.
- Describe the **Plancherel measure** on partitions of $$n$$ and the **limit-shape** landscape of Vershik–Kerov and Logan–Shepp.
- Explain, at slogan level, how representation theory of symmetric groups indexes partitions, and why randomness on those partitions is a probabilistic question.
- Place **Okounkov–Pandharipande** Gromov–Witten work (and related Hurwitz/completed-cycle generating functions) as enumerative geometry via representation-theoretic operators.
- Treat **Nekrasov–Okounkov** instanton counting as a **research bridge** to Seiberg–Witten geometry, not as “Okounkov invented gauge theory.”
- Name **Schur measures / Schur processes** (Okounkov; Borodin–Okounkov–Olshanski and collaborators) and dimer / melted-crystal pictures (including Kenyon–Okounkov) as neighboring combinatorial probability.
- Avoid the claim that he classified all representations of all groups.

**Prerequisites.** Partitions of an integer; the symmetric group $$S_n$$ at the level “irreducible representations are labelled by Young diagrams”; generating functions. Algebraic geometry at the level “curves in a variety can be counted in a virtual sense” is enough for Gromov–Witten slogans. No quantum field theory required.

**Seminar links.** LO1 (deep bridging programs) and LO6 (citation hygiene). Same-year neighbor: [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/). Geometry of moduli: [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) (different moduli, similar “spaces of shapes become dynamical or probabilistic”).

---

## 1. Partitions as a common alphabet

A **partition** of a positive integer $$n$$ is a weakly decreasing sequence of positive integers summing to $$n$$. One draws it as a **Young diagram** (a stack of boxes). The same diagrams index:

- conjugacy classes and **irreducible representations** of the symmetric group $$S_n$$;
- Schur functions in the ring of symmetric functions;
- many statistical-mechanical configurations (lozenge tilings, plane partitions, dimer coverings after a change of picture).

The **Plancherel measure** on partitions of $$n$$ is the probability

$$
\mathbb{P}(\lambda)=\frac{\bigl(\dim\lambda\bigr)^2}{n!},
$$

where $$\dim\lambda$$ is the dimension of the irreducible representation of $$S_n$$ labelled by $$\lambda$$. It is the most representation-theoretic of the natural measures on diagrams: it is the pushforward of Haar (uniform) measure on $$S_n$$ under the map that records the shape of a random Young tableau, equivalently the Plancherel decomposition of the regular representation.

**Vershik–Kerov** and independently **Logan–Shepp** (late 1970s) proved that a Plancherel-random diagram, scaled by $$\sqrt{n}$$, converges to a deterministic **limit shape**—a curve in the plane that looks like a rotated, smoothed staircase. The typical partition is not a long thin hook and not a square; it hugs a specific algebraic-looking profile. Fluctuations about that shape, and the statistics of the longest rows, became a 1990s industry connecting to random matrices.

**Slogan.** Once representations supply a privileged measure on diagrams, asymptotic representation theory *is* a chapter of probability.

---

## 2. Okounkov’s refinements: from BDJ to random surfaces

**Baik–Deift–Johansson** determined the fluctuations of the longest increasing subsequence of a random permutation (equivalently, the first row of a Plancherel-random partition) and observed the **Tracy–Widom** law of the largest eigenvalue of a Gaussian Hermitian matrix. They conjectured a matching for the joint law of the first few rows. Okounkov proved that conjecture by a distinctive route: both problems match a third problem about **counting random surfaces** (Feynman diagrams versus ramified coverings). A different proof was given by **Borodin–Okounkov–Olshanski**; Johansson also gave a proof. Credit the landscape, then Okounkov’s geometric comparison.

The IMU 2006 essay highlights this early result as a seed: a direct link among random matrices, random permutations, and algebraic geometry. Later work treats **random plane partitions** and “melted crystals”: if one removes boxes from a corner at random with suitable weights, the macroscopic liquid region is bounded by an **algebraic curve**. **Kenyon–Okounkov** (and related dimer work with Sheffield and others) made that surprising real-algebraic conclusion precise. Again the course slogan is a bridge: a statistical-mechanical shape theorem lands in algebraic geometry.

Okounkov did not invent limit shapes (Vershik–Kerov, Logan–Shepp) and did not invent random-matrix Tracy–Widom laws (Tracy–Widom; BDJ). He *connected* those objects to surfaces, coverings, and later to Gromov–Witten and gauge-theoretic generating functions.

---

## 3. Gromov–Witten theory as a generating function

**Gromov–Witten theory** counts (virtually) holomorphic maps from curves to a target variety, with incidence conditions—the modern language of enumerative geometry, enriched by physics. The numbers are packaged as generating functions. Okounkov, especially with **Rahul Pandharipande**, developed an operator formalism in which those generating functions become vacuum expectations in a Fock space (the infinite-wedge representation of the Heisenberg/fermion algebra—the same algebra that organizes Schur functions and partitions).

A concrete chapter: Gromov–Witten theory of target **curves**, including the **equivariant Gromov–Witten theory of $$\mathbb{P}^1$$**. Okounkov–Pandharipande identified the stationary sector with **Hurwitz theory** with **completed cycle** insertions, and showed that the equivariant theory of $$\mathbb{P}^1$$ is governed by the **2-Toda hierarchy**. The papers (including *Ann. of Math.* **163**, 2006, and the arXiv sequence starting from [math/0207233](https://arxiv.org/abs/math/0207233)) are the seminar-level landmarks.

With **Maulik, Nekrasov, and Pandharipande**, Okounkov also formulated well-known conjectures relating **Gromov–Witten** and **Donaldson–Thomas** invariants of threefolds—another bridge, this time between two enumerative theories, not a claim that either theory was invented in 2006.

**Slogan.** Enumerative geometry becomes computable when its generating function is recognized as a tau-function or a vacuum matrix element already studied in representation theory.

---

## 4. Nekrasov partition functions: a research bridge

**Nekrasov** (2002) gave a mathematically rigorous regularized definition of the partition function of certain four-dimensional $$\mathcal{N}=2$$ supersymmetric gauge theories, as an equivariant integral on instanton moduli (a localization substitute for a long-distance cutoff). **Nekrasov–Okounkov** showed that this localization integral can be rewritten as a measure on partitions with a periodic potential, and identified the Seiberg–Witten prepotential with the **surface tension of a limit shape**. Okounkov’s ICM-adjacent survey “Random partitions and instanton counting” ([arXiv:math-ph/0601062](https://arxiv.org/abs/math-ph/0601062)) is the readable map.

**Accuracy.** Seiberg–Witten geometry and Nekrasov’s definition precede or sit beside the joint work. Okounkov did not invent gauge theory. The contribution is a dictionary: instanton sums *are* random partitions; their thermodynamics *is* the Seiberg–Witten curve. That is exactly the kind of bridge the IMU citation names.

---

## 5. Schur processes, dimers, and what is not claimed

**Schur measures** (Okounkov) generalize Plancherel by weighting diagrams with Schur functions. **Schur processes** (Okounkov–Reshetikhin and the circle of **Borodin, Okounkov, Olshanski**) are measures on *sequences* of partitions with determinantal correlation functions. They model plane partitions, certain growth processes, and, after translation, dimer models and tilings. The course should name collaborators: this is not a solo census of all determinantal processes.

**What Okounkov did not do.**

- He did not classify all irreducible representations of all groups. Symmetric groups, infinite symmetric groups, and related combinatorial representation theory are the home territory; “classification of representations” is a different century-long program (finite groups, Lie groups, p-adic groups, …).
- He did not replace algebraic geometry. Gromov–Witten invariants remain geometric; the new fact is that their generating functions have representation-theoretic closed forms in important cases.
- He did not close Seiberg–Witten theory as physics. He supplied a mathematical identification in a regularized instanton model.

---

## 6. Why a Fields Medal

The 2006 IMU essay is unusually honest about genre: the work is difficult to classify. That is the point. A Fields Medal can reward a **dictionary** that makes three fields compute one another’s answers.

1. **A privileged measure became a geometric tool.** Plancherel and its Schur deformations moved from asymptotic group theory into random surfaces and enumerative geometry.
2. **Generating functions as theorems.** Toda hierarchies and vacuum expectations are not decorations; they *are* the GW theory of $$\mathbb{P}^1$$ in the Okounkov–Pandharipande formalism.
3. **Physics as a source of well-posed math.** Instanton counting, once regularized, became a limit-shape problem. The bridge is research-level and two-way.

Giovanni Felder’s Bourbaki-style / ICM exposition “The work of Andrei Okounkov” ([arXiv:math/0609847](https://arxiv.org/abs/math/0609847)) is the recommended next reading after this lecture.

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

## Exercises

1. Write the Plancherel weight $$\mathbb{P}(\lambda)$$ and explain in one sentence why it is representation-theoretic rather than uniform.
2. What does a **limit shape** forget, and what does it retain, about a random Young diagram of size $$n$$?
3. Baik–Deift–Johansson vs Okounkov vs Borodin–Okounkov–Olshanski: in three lines, who did what to the longest-increasing-subsequence / first-row problem?
4. State a one-sentence slogan for Okounkov–Pandharipande on $$\mathbb{P}^1$$: generating functions, operators, integrable hierarchy.
5. Why is “Nekrasov–Okounkov = Okounkov invented instantons” false? Write a two-sentence correction.
6. **Accuracy practice.** Rewrite “Okounkov classified representations and solved string theory” as two precise sentences suitable for this course.
7. **Seminar stretch.** Compare this bridge (probability $$\leftrightarrow$$ representations $$\leftrightarrow$$ enumerative geometry) with [Mirzakhani’s]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) bridge (hyperbolic geometry $$\leftrightarrow$$ moduli $$\leftrightarrow$$ dynamics). What is a “random shape” in each story?

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
