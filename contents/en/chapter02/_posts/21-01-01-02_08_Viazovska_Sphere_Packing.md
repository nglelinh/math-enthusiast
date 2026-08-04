---
layout: post
title: "Viazovska and Sphere Packing (Fields Medal 2022)"
chapter: '02'
order: 10
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Maryna Viazovska** received the **Fields Medal 2022** for the proof that the $$E_8$$ lattice packing achieves the optimal density among sphere packings in dimension 8, and for further contributions to related extremal problems—including the optimality of the Leech lattice packing in dimension 24 with collaborators. She is the **second woman** to receive a Fields Medal (after Maryam Mirzakhani, 2014).

This essay follows:

**Packing density → low dimensions → exceptional lattices → Cohn–Elkies bounds → magic functions → modular forms → $$E_8$$ and Leech → Fields 2022.**

The goal is not to construct the modular form by hand, but to understand **what optimality means**, **why dimensions 8 and 24 are special**, and **how Fourier analysis turns packing into function design**.

What is the densest way to pack equal non-overlapping balls in Euclidean space $$\mathbb{R}^n$$? The **Cohn–Elkies linear programming bound** reduces upper bounds on packing density to the existence of special radial functions $$f$$ with sign constraints on $$f$$ and its Fourier transform $$\hat f$$. Sharpness requires a “magic” function attaining equality.

Viazovska (2016) constructed an optimal function in dimension 8 using modular forms, proving $$E_8$$ is densest. With Cohn, Kumar, Miller, and Radchenko, the method extended to the Leech lattice in dimension 24. Fields Medal 2022.

---

## Learning objectives

After this lecture you should be able to:

- Define packing density carefully (limit of covered volume fraction).
- State the classical solutions in dimensions 2 and 3 at slogan level.
- Explain why $$E_8$$ and the Leech lattice are natural candidates in dimensions 8 and 24.
- Describe the Cohn–Elkies bound as an optimization problem over radial functions.
- Separate Viazovska’s solo $$E_8$$ theorem from the collaborative Leech theorem.
- Avoid claiming that packing is solved in all dimensions.

**Prerequisites.** Volumes of balls, lattices as discrete subgroups of $$\mathbb{R}^n$$, and the idea of the Fourier transform of a radial function (details optional).

---

## 1. The sphere packing problem

Fix dimension $$n$$ and pack non-overlapping closed balls of equal radius in $$\mathbb{R}^n$$. The **density** of a packing is

$$
\delta=\limsup_{R\to\infty}\frac{\text{volume of balls inside }B(0,R)}{\operatorname{Vol} B(0,R)}.
$$

Equivalently (for lattice packings), one studies the volume of a fundamental domain versus the number of spheres centered at lattice points.

**Question.** What is $$\delta_n$$, the supremum of densities over all packings in dimension $$n$$? Which configurations attain it?

![Hexagonal packing]({{ site.baseurl }}/img/chapter_img/viazovska_packing_2d.svg)

*Figure. Hexagonal packing in the plane—the classical optimum in dimension 2.*

---

## 2. What is known in low dimensions

| Dimension | Optimal packing (status) |
|-----------|---------------------------|
| $$n=1$$ | Trivial (intervals on a line) |
| $$n=2$$ | Hexagonal lattice — classical |
| $$n=3$$ | FCC / HCP density — Kepler’s conjecture, proved by Hales (with computer assistance; now formally verified) |
| $$n=8$$ | $$E_8$$ lattice — **Viazovska (2016)** |
| $$n=24$$ | Leech lattice — **Cohn–Kumar–Miller–Radchenko–Viazovska** |
| generic $$n$$ | Mostly open; asymptotic bounds exist |

Most dimensions remain unsolved exactly. Dimensions 8 and 24 are miracles of symmetry.

---

## 3. Lattices, especially $$E_8$$ and Leech

A **lattice** $$\Lambda\subset\mathbb{R}^n$$ is a discrete subgroup spanning $$\mathbb{R}^n$$ (think $$\mathbb{Z}^n$$ after a linear change of variables). The **lattice packing** places balls at lattice points with radius half the minimal nonzero vector length.

### The $$E_8$$ root lattice

$$E_8\subset\mathbb{R}^8$$ is the unique (up to isometry) even unimodular lattice in dimension 8. It has:

- minimal vectors of norm 2 forming the $$E_8$$ root system (240 roots);
- extraordinary symmetry (Weyl group / automorphism group of huge order);
- long-conjectured optimal packing density among all packings—not only lattices.

### The Leech lattice $$\Lambda_{24}$$

In dimension 24, the **Leech lattice** is the unique even unimodular lattice with no roots (no norm-2 vectors). It is central to sporadic finite simple groups and was likewise conjectured to give the densest packing.

![E8 and Leech]({{ site.baseurl }}/img/chapter_img/viazovska_e8_leech.svg)

*Figure. Two exceptional lattices settled by Viazovska and collaborators.*

---

## 4. Cohn–Elkies: packing meets Fourier analysis

Cohn and Elkies showed that auxiliary radial functions yield **upper bounds** on packing density via linear programming / Poisson summation ideas.

**Slogan hypotheses** (schematic, constants suppressed):

- $$f$$ is a nice radial Schwartz function;  
- $$f(x)\le 0$$ for $$\|x\|\ge r$$ (outside a ball);  
- $$\hat f(\xi)\ge 0$$ for all frequencies $$\xi$$;  
- $$f(0)>0$$ and $$\hat f(0)>0$$.

Then the density of any packing is bounded above by a simple expression involving $$f(0)$$, $$\hat f(0)$$, and the ball volume scale set by $$r$$.

![Cohn–Elkies idea]({{ site.baseurl }}/img/chapter_img/viazovska_cohn_elkies.svg)

*Figure. Sign conditions on $$f$$ and $$\hat f$$ produce packing upper bounds.*

### The equality problem

To prove a lattice packing is optimal, one needs a function $$f$$ for which the Cohn–Elkies upper bound **matches** the lattice’s density. Such functions are called **magic functions**. Existence is extremely rigid: most candidates give only non-sharp bounds.

---

## 5. Viazovska’s magic function in dimension 8

Viazovska constructed an explicit radial Fourier eigenfunction (in a suitable sense) using **modular forms** and Laplace transforms of carefully chosen weakly holomorphic forms, engineered so that:

- the required sign conditions hold;  
- equality is forced for the $$E_8$$ packing data.

The proof is analytic and exact—not a numerical optimization that almost matches. That is why the result is a theorem of *Annals* depth rather than a high-precision conjecture check.

**Theorem (Viazovska, 2016/2017).**  
The $$E_8$$ lattice packing achieves the maximal density among all sphere packings in $$\mathbb{R}^8$$.

---

## 6. Dimension 24: collaboration

Building on the same philosophy, **Cohn, Kumar, Miller, Radchenko, and Viazovska** produced a magic function for dimension 24, proving optimality of the Leech lattice packing among all packings in $$\mathbb{R}^{24}$$.

**Credit literacy.**  
- Dimension 8: Viazovska solo.  
- Dimension 24: collaborative CKMRV.  
Popular accounts sometimes blur this; careful teaching should not.

---

## 7. Beyond a single density number

The Cohn–Elkies / Viazovska circle of ideas connects to:

- **universal optimality** and energy minimization for point configurations;  
- Fourier interpolation formulas (related Radchenko–Viazovska work);  
- the broader program of exact solutions in discrete geometry via harmonic analysis.

The Fields Medal recognizes both the packing theorems and the surrounding analytic contribution.

---

## 8. Why it matters

- Settles two of the most famous exact packing problems in mathematics.  
- Demonstrates modular forms as tools of **geometric optimization**, not only of number-theoretic $$L$$-functions.  
- Complements computer-assisted 3D (Hales) with a pure-analysis miracle in exceptional dimensions.  
- Gives Chapter 2 another bridge: **analysis ↔ discrete geometry**.

---

## 9. The paradox, restated

In most dimensions we cannot name the densest packing. In dimensions 8 and 24, exceptional lattices not only exist—they are **provably best possible**, because a single Fourier-designed function seals every competing arrangement.

$$
\text{symmetry of }E_8/\Lambda_{24}
\quad+\quad
\text{magic }f
\quad=\quad
\text{global packing optimum}.
$$

---

## Common misconceptions (fact-check)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Sphere packing is solved in all dimensions.” | **Fail** | Only special dimensions have exact optima. |
| “$$E_8$$ optimality is numerical.” | **Fail** | It is an exact theorem. |
| “Viazovska alone proved Leech optimality.” | **Fail** | Dimension 24 is collaborative. |
| “Lattice optimum automatically means global optimum.” | **Fail** | In general, nonlattice packings might win; the theorems rule that out in 8 and 24. |
| “This is only about root systems, not analysis.” | **Fail** | Fourier sign conditions are the engine of the upper bound. |

---

## Challenges and extensions

1. Why does increasing dimension make naive packing intuition fail?  
2. What does “even unimodular” buy you as a lattice designer?  
3. If $$\hat f$$ had a negative dip, how could a packing “escape” the bound?  
4. Compare proof cultures: Hales (3D, formal verification) vs Viazovska (modular forms).  
5. Kissing numbers vs packing density—related but not identical; explain one difference.

---

## Exercises

1. **Warm-up.** Compute the density of the integer lattice packing in $$\mathbb{R}^2$$ (unit balls at $$\mathbb{Z}^2$$ after suitable scaling discussion).  
2. **Definitions.** Define lattice packing density using fundamental volume.  
3. **Candidates.** Why are 240 roots a hint that $$E_8$$ is “tight”?  
4. **Cohn–Elkies.** In one paragraph, explain why Fourier positivity of $$\hat f$$ controls global arrangements.  
5. **Credit.** Write two sentences distinguishing the $$E_8$$ and Leech theorems’ authorship.  
6. **Research literacy.** Open Viazovska’s *Annals* paper (or a detailed survey); from the introduction, list the analytic ingredients named before modular forms appear.  
7. **Chapter link.** One paragraph comparing Viazovska’s “design a function to prove optimality” with Wang’s “control tubes to prove dimension.”

---


## Video sources (math-video-researcher pack)

Full ranking: `research/video-research/Viazovska_Sphere_Packing/`.

**Recommended order**

1. **Orientation** — Quanta (2016): [Sphere Packing Solved in Higher Dimensions](https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/).  
2. **Core lecture** — Einstein Lectures: Viazovska on sphere packing: [YouTube](https://www.youtube.com/watch?v=fH6KNlUJux0).  
3. **Foundation** — Breakthrough Prize Symposium talk: [YouTube](https://www.youtube.com/watch?v=VCZeVsTb7DU).  
4. **Primary paper** — Viazovska dim 8: [arXiv:1603.04246](https://arxiv.org/abs/1603.04246); Cohn IMU laudatio: [PDF](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/laudatio-mv.pdf).

**Status reminder:** Optimal packing known in dims 1, 2, 3, 8, 24—**not** all dimensions.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Viazovska_Sphere_Packing/transcripts/` · status: `research/video-research/Viazovska_Sphere_Packing/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Viazovska_Sphere_Packing_fH6KNlUJux0_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References and further reading


Full URL bibliography from video research (including secondary finds): `research/video-research/Viazovska_Sphere_Packing/references.md`.

### Complete URL list (audit)

1. https://www.youtube.com/watch?v=fH6KNlUJux0  
2. https://www.youtube.com/watch?v=VCZeVsTb7DU  
3. https://www.youtube.com/watch?v=qr6ZbYancMY  
4. https://arxiv.org/abs/1603.04246  
5. https://arxiv.org/pdf/1603.04246  
6. https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/laudatio-mv.pdf  
7. https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/  
8. https://en.wikipedia.org/wiki/Sphere_packing  
9. https://en.wikipedia.org/wiki/Maryna_Viazovska  
10. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022  
11. https://www.math.inc/sphere-packing  
12. https://en.wikipedia.org/wiki/E8_lattice  
13. https://en.wikipedia.org/wiki/Leech_lattice  

### Research pack

14. Course pack: `research/video-research/Viazovska_Sphere_Packing/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. **M. Viazovska** (2017). The sphere packing problem in dimension 8. *Annals of Mathematics*.  
2. **H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, M. Viazovska.** The sphere packing problem in dimension 24. *Annals of Mathematics*.  
3. **H. Cohn & N. Elkies.** New upper bounds on sphere packings I. *Annals of Mathematics*.  
4. Surveys / Quanta expositions on Viazovska’s work (for intuition).  
5. IMU Fields Medal 2022 — Maryna Viazovska.  
6. Background: Conway–Sloane, *Sphere Packings, Lattices and Groups* (classical lattice lore).

*Research note.* Optimality statements follow the published Annals papers. Figures are pedagogical schematics, not lattice renderings in 8D.

---

## Further directions

- Explore universal optimality and energy minimization papers in the Cohn–Viazovska circle.  
- Read a gentle introduction to modular forms for analysts (enough to see where special functions come from).  
- Compare with the Maynard and Green–Tao essays: exceptional structure (lattices / primes) proved by hard analysis.  
- Note one precise question you still have—good questions are part of mathematical practice.
