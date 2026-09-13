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

**Hugo Duminil-Copin** received the **Fields Medal 2022** for, in the IMU’s short citation, “solving longstanding problems in the probabilistic theory of **phase transitions** in statistical physics, especially in dimensions **three** and **four**.” The long citation is more precise, and this essay follows it. Together with collaborators he established **continuity** and **sharpness** of the phase transition for Ising-type models in dimension three—questions open since the 1980s. In dimension four, with **Michael Aizenman**, he proved **mean-field critical behavior** of the Ising model and the **triviality** of four-dimensional Euclidean scalar quantum field theory, an old physics conjecture. In two dimensions, for dependent **Fortuin–Kasteleyn (FK)** percolation, he and collaborators determined continuity or discontinuity for all parameter values, proved universality on isoradial graphs, and established **rotational invariance** at large scale as a step toward conformal invariance.

This essay is for learners who have seen the Ising model as spins on a lattice, or percolation as open and closed edges, and want the architecture of a Fields-level probability paper. It does **not** claim that Duminil-Copin proved conformal invariance of the three-dimensional Ising model. That remains open. It also distinguishes his work from [Smirnov’s]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/) 2010 conformal invariance theorems in two dimensions and from [Werner’s]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) SLE program—adjacent portraits, not the same theorems. Duminil-Copin’s doctoral advisor was Smirnov; the 2022 medal is a sequel chapter, not a reprint.

---

## Learning objectives

After this lecture you should be able to:

- State the IMU 2022 short citation and paraphrase the long citation’s three blocks: 3D Ising-type continuity/sharpness; 4D mean-field / triviality with Aizenman; 2D FK continuity-discontinuity, universality, rotation.
- Define, at slogan level, a **phase transition**, the **critical point**, **continuity vs discontinuity** of an order parameter, and **sharpness** (exponential decay below criticality; percolation above).
- Explain why dimension **three** was hard for the Ising model even after two-dimensional exact solutions, and why dimension **four** is the mean-field threshold for scalar fields.
- Attribute the 4D triviality theorem jointly to **Aizenman–Duminil-Copin**, and attribute 3D and 2D results to **named groups of collaborators** rather than to a single author.
- Distinguish **rotational invariance at large scale** (a 2D step toward conformal invariance) from **full conformal invariance**, and from any claim about 3D Ising CFT.
- Practice **LO6**: “he solved statistical physics” is hype.

**Prerequisites.** Independent Bernoulli percolation as a cartoon (edges open with probability $$p$$); the idea of an infinite connected component; a Hamiltonian and a Gibbs measure for the Ising model at inverse temperature $$\beta$$. No prior SLE or constructive QFT is required.

**Seminar links.** Same 2022 class: [Maynard]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/), [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/). Probability-and-physics cousins (future portraits in this chapter): [Smirnov / percolation]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/), [Werner / SLE]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/). Kinetic statistical physics of a different kind: [Deng]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/).

---

## 1. A history of transitions, exact in two dimensions and stubborn in three

A **phase transition** is a sharp change in the large-scale behavior of a system as a parameter varies—temperature, density, or an edge-weight. The **Ising model** on $$\mathbb{Z}^d$$ assigns spins $$\sigma_x=\pm 1$$ to vertices and weights configurations by $$e^{-\beta H}$$ with $$H=-\sum_{\langle x,y\rangle}\sigma_x\sigma_y$$. At high temperature (small $$\beta$$) correlations decay and the **spontaneous magnetization** vanishes; at low temperature a plus-boundary condition can force a nonzero magnetization $$M(\beta)$$. **Onsager** solved the two-dimensional Ising model exactly (1944) and exhibited a continuous transition. **Peierls** had already shown that a transition exists in dimension two and higher. Percolation—opening edges independently at probability $$p$$—has a similarly sharp **critical probability** $$p_c$$, with an infinite cluster for $$p>p_c$$.

By the 1980s the *existence* of a transition for nearest-neighbour Ising models in dimension $$d\ge 2$$ was classical, but several “what kind of transition?” questions were open in dimension three. Does $$M(\beta)$$ tend to $$0$$ as $$\beta\downarrow\beta_c$$ (continuity of the phase transition)? Are correlations exponentially small for all $$\beta<\beta_c$$, with a matching supercritical picture (**sharpness**)? Mean-field heuristics and lace expansion gave answers in *high* dimension; dimension three sat below those methods. Dimension four, the upper critical dimension for the scalar $$\varphi^4$$ theory, was a different embarrassment: physicists expected the scaling limit of critical 4D Ising / $$\varphi^4$$ to be a **Gaussian free field**—no interacting continuum scalar QFT in four Euclidean dimensions—but a complete mathematical proof was missing.

Two-dimensional **dependent** models, notably the **random-cluster (FK)** representation of Potts and Ising, raised a third family of questions. For FK parameter $$q$$, when is the transition continuous and when does the order parameter jump? After [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/) proved conformal invariance for site percolation on the triangular lattice and for the 2D Ising model, a program remained: treat *dependent* FK percolation for all $$q$$, on more graphs than the square lattice, and produce the missing symmetries (rotation, then full conformal invariance) that would connect the lattice models to 2D conformal field theory. [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) and Lawler–Schramm–Werner had already shown how **SLE** describes scaling limits once conformal invariance is known. Duminil-Copin’s 2D work lives in that pipeline; it does not replace Smirnov or SLE.

---

## 2. Slogan: read the transition, not only its existence

**Slogan.** A modern theorem in this subject does not merely say “$$p_c$$ exists.” It says *how the system approaches* $$p_c$$: continuously or with a jump; with exponential decay or with power laws; with mean-field exponents or with non-classical ones; with rotation invariance at large scale or only with lattice symmetries.

Three words from the IMU citation deserve definitions.

**Continuity** of the phase transition means that the order parameter—magnetization for Ising, percolation probability for FK—tends to its critical value without a jump. For 3D Ising, that is the statement that $$M(\beta_c)=0$$ (no residual magnetization at criticality), open since the 1980s in the form the citation names.

**Sharpness** means that the subcritical regime is *uniformly* subcritical: connectivities decay exponentially in distance, and the susceptibility is finite, for every $$\beta<\beta_c$$ or $$p<p_c$$, not merely for $$\beta$$ far below criticality. Duminil-Copin, Raoufi, and Tassion developed randomized-algorithm / OSSS methods that proved sharpness for a wide class of models, including 3D Ising-type settings.

**Mean-field / triviality** in dimension four means that critical exponents match the Gaussian (mean-field) ones and that the scaling limit of the lattice field is Gaussian. In physics language: four-dimensional Euclidean $$\varphi^4$$ theory is **trivial**—it does not yield a nontrivial interacting continuum limit of this type. **Aizenman–Duminil-Copin** (2021) is the paper the citation points to.

---

## 3. What the theorems rearrange, with collaborators named

**Dimension 3 (Ising-type).** Continuity of the spontaneous magnetization and sharpness of the transition move 3D Ising from “a transition exists” to “the transition is of the type everyone expected but could not prove.” Credit is collaborative. Continuity of magnetization for the 3D Ising model is associated with work of **Aizenman, Duminil-Copin, and Sidoravicius** (random-current representation). Sharpness is associated with **Duminil-Copin, Raoufi, and Tassion**. Treat any single-name slogan as a mistake.

**Dimension 4 (with Aizenman).** Mean-field critical behavior of Ising and triviality of 4D Euclidean scalar QFT close a conjecture that had lived in constructive field theory and mathematical physics since the 1970s (with earlier partial results in *high* dimension and for other models). Attribute this block **jointly** to Aizenman and Duminil-Copin.

**Dimension 2 (FK / random-cluster).** For the planar random-cluster model, Duminil-Copin and collaborators proved that the transition is continuous or discontinuous for **all** $$q>0$$: continuous for $$q\le 4$$, discontinuous for $$q>4$$, completing a classical picture of Baxter and others at the level of a theorem for the standard lattice models. **Universality** on **isoradial** graphs says that the critical behavior does not depend on the particular isoradial embedding. **Rotational invariance** at large scale (Duminil-Copin, Kozlowski, Krachun, Manolescu, Oulamara, and related works) is, in the IMU’s words, “an important step towards establishing their large-scale conformal invariance,” which would be the missing ingredient for a rigorous link to 2D CFT. It is **not** a complete proof of conformal invariance for all these FK models, and it is **not** a statement about three-dimensional Ising.

**Earlier 2D landmark, for context.** With Smirnov, Duminil-Copin proved that the connective constant of the honeycomb lattice is $$\sqrt{2+\sqrt{2}}$$ (self-avoiding walks). That is part of his formation, not the 2022 citation’s 3D/4D emphasis.

---

## 4. Honest attribution and what the medal is not

| Result (slogan) | Credit |
|-----------------|--------|
| Continuity of 3D Ising magnetization | Aizenman–Duminil-Copin–Sidoravicius and the random-current school |
| Sharpness for Ising-type / percolation models | Duminil-Copin–Raoufi–Tassion (and earlier sharpness literature) |
| 4D mean-field Ising and $$\varphi^4$$ triviality | Aizenman–Duminil-Copin (2021) |
| FK continuity/discontinuity for all $$q$$; isoradial universality | Duminil-Copin with Tassion, Manolescu, and others |
| Large-scale rotational invariance in critical planar FK-type models | Duminil-Copin with Kozlowski, Krachun, Manolescu, Oulamara, … |
| 2D percolation / Ising conformal invariance | **Smirnov (2010 Fields)** — see [that essay]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/) |
| SLE as the scaling-limit language | **Schramm; Lawler–Schramm–Werner; Werner (2006 Fields)** — see [Werner]({{ site.baseurl }}/contents/en/chapter02/02_30_Werner_SLE/) |

Duminil-Copin was born in 1985 in France, studied at ENS and Paris-Sud, wrote his PhD in Geneva under Smirnov (2011), and holds positions at the University of Geneva and the IHÉS. The biographical colour is optional; the collaborator table is not.

**Do not claim:** full conformal invariance of 3D Ising; a classification of all lattice models; a solution of constructive QFT in dimension three; that SLE was reinvented in 2022.

---

## 5. Why a Fields Medal

Lattice statistical mechanics is full of beautiful predictions and few theorems in the dimensions where physics actually happens. Dimension two had Onsager, conformal field theory, SLE, and Smirnov. High dimension had mean-field and lace expansion. Dimensions three and four were the gap the IMU names. Closing continuity and sharpness in 3D, and triviality in 4D, changed what a “physically realistic dimension” theorem can look like: probabilistic representations (random currents, random-cluster measures), sharp threshold tools from computer science, and classical correlation inequalities, rather than an exact solution.

For this course, Duminil-Copin is a portrait of **inherited language, new dimensions**. He writes in the vocabulary of Smirnov and Werner and Aizenman; the medal is for making that vocabulary prove the 3D and 4D statements that had been advertised as open for decades.

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

## Exercises

1. In your own words: what is a **phase transition** for percolation, and what extra information does **sharpness** add beyond the existence of $$p_c$$?
2. Why is dimension 2 “exactly solvable” in a way that dimension 3 is not, at slogan level? (Onsager vs no closed-form 3D Ising.)
3. State the 4D triviality result in one sentence, and name **both** authors.
4. Continuity vs discontinuity: draw a cartoon of $$M(\beta)$$ with a jump and without a jump. Which cartoon is 2D FK for $$q>4$$?
5. **Accuracy practice.** A headline: “Mathematician proves 3D magnets are conformal.” Rewrite in two sentences for this course.
6. Compare [Smirnov]({{ site.baseurl }}/contents/en/chapter02/02_28_Smirnov_Percolation/) and Duminil-Copin in a four-line table: dimension, model, what was proved, what remains.
7. Why would **rotational invariance** be a necessary step toward conformal invariance, yet not a sufficient one? One paragraph.
8. **Seminar stretch.** The IMU mentions “non-integrable cases in dimension 2.” What does “integrable” mean as a warning (exact formulas exist only for special $$q$$ or special lattices), and why is a proof that avoids those formulas more valuable?

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
