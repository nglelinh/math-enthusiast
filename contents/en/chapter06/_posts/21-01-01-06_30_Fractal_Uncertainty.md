---
layout: post
title: "The Fractal Uncertainty Principle"
chapter: '06'
order: 30
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

In the previous lesson, we saw that classical uncertainty forbids a wave and its Fourier transform from squeezing into two small **intervals**. Now imagine a trickier hiding place: instead of a solid interval, let the wave hide on **fractal dust**—like the Cantor set, riddled with gaps at every magnification, spanning the entire unit interval yet having total length zero. A classical billiard ball bouncing between curved obstacles can stay trapped forever on such fractal dust without ever escaping. Can a **quantum wave** do the same?

The answer is **no**—and the Fourier-analytic theorem that forces the wave to leak out is the **fractal uncertainty principle (FUP)**. This is live frontier mathematics unfolding right before our eyes: Jean Bourgain and Semyon Dyatlov proved the 1D version in 2016; nearly a decade later, MIT graduate student Alex Cohen proved the higher-dimensional version under the geometric condition of **line porosity** (*Annals of Mathematics* 2025; arXiv 2023), unlocking new breakthroughs in **quantum chaos**—while the field's grand dream, general quantum unique ergodicity (QUE), remains **open**. Companion to [uncertainty literacy]({{ site.baseurl }}/contents/en/chapter06/06_29_Uncertainty_Principles/).

---

## Background Knowledge Map: What Three Pillars Support the Fractal Uncertainty Principle?

With undergraduate Fourier transforms, wave equations, and the Cantor set, three pillars explain why FUP is one of the hottest tools in modern analysis:

### 1. Fractal Geometry and Porosity
A fractal like the middle-thirds Cantor set has zero length yet spans all of $$[0,1]$$, so classical variance inequalities fail to rule it out! Instead of length or variance, fractal geometry measures **porosity**: zoom in on *any* piece at *any* scale, and you always find a missing gap occupying a fixed fraction of that interval.

### 2. Semiclassical Analysis
To connect classical phase space (position $$x$$ and momentum $$\xi$$ together) with short-wavelength quantum waves ($$h \ll 1$$), analysts use the semiclassical Fourier transform:

$$
(\mathcal{F}_h f)(\xi) = \frac{1}{(2\pi h)^{d/2}} \int_{\mathbb{R}^d} e^{-i x \cdot \xi / h} f(x)\,dx.
$$

At wavelength $$h$$, a fractal $$X$$ is thickened to its $$h$$-neighborhood $$X(h)$$. **FUP** asserts a power-law operator-norm decay $$\|\mathbf{1}_{X(h)}\mathcal{F}_h\mathbf{1}_{Y(h)}\| \le C h^\beta$$ ($$\beta > 0$$) as $$h \to 0$$—a short-wavelength wave cannot simultaneously dodge the gaps in both space and frequency!

### 3. Quantum Chaos and the QUE Conjecture
On a negatively curved (hyperbolic) manifold, most classical trajectories wander everywhere, yet a porous fractal dust of trapped trajectories remains. Quantum chaos asks whether high-energy eigenfunctions delocalize away from those traps (**Dyatlov–Jin delocalization** is a theorem) or even equidistribute completely (**Rudnick–Sarnak QUE**, still a major open conjecture).

---

## Learning objectives

After this lecture you should be able to:

- State the FUP **slogan**: $$f$$ and $$\hat f$$ cannot both live near porous fractal sets.
- Explain **porosity** with the middle-thirds Cantor set, and why that is a stronger concentration constraint than “small interval.”
- Describe the **line obstruction** in dimension $$\ge 2$$ (a set containing a full line can be “full of holes” yet fail FUP).
- Define **line porosity** at slogan level and name Cohen’s theorem as FUP under that hypothesis.
- Separate **theorem** (FUP; Dyatlov–Jin delocalization on hyperbolic surfaces) from **conjecture** (Rudnick–Sarnak QUE).
- Avoid “every fractal in every dimension obeys FUP.”

**Prerequisites.** [Uncertainty principles]({{ site.baseurl }}/contents/en/chapter06/06_29_Uncertainty_Principles/); the Cantor set from [fractals]({{ site.baseurl }}/contents/en/chapter04/04_03_Fractals/); Fourier as in Chapter 3. Hyperbolic geometry stays at picture level.

---

## 1. From intervals to holes at every scale

Classical Pauli–Weyl forbids simultaneous concentration on two small intervals, one in space and one in frequency. A fractal can be **measure zero** and still large in a dimensional sense: the middle-thirds Cantor set is uncountable, length zero, and riddled with gaps at every generation.

![Middle-thirds Cantor construction, six generations]({{ site.baseurl }}/img/chapter_img/fup_cantor_porosity.png)

*Figure. At every scale the set is missing a definite fraction of each remaining interval. That is porosity, not mere “smallness.”*

**FUP slogan (1D).** If you try to build a function whose mass lives near a Cantor-like set, its Fourier transform **cannot** also live near a Cantor-like set. Adding together waves whose frequencies sit on fractal dust will not produce another fractal-looking envelope—the holes fill in.

### Deep-Dive Explanation: Measuring Fourier Leakage into Cantor Holes by Hand at $$N = 9$$ (Read Slowly)

To see FUP work with concrete numbers, take the 2nd-generation discrete Cantor set inside $$N = 3^2 = 9$$ points $$\{0, 1, \dots, 8\}$$: delete the middle third $$\{3, 4, 5\}$$ and the middle points $$1$$ and $$7$$ of the remaining thirds, leaving four points $$X = \{0, 2, 6, 8\} = \{0, 6\} + \{0, 2\}$$.

1. **Place a normalized wave entirely on $$X$$:** Take the unit vector $$v \in \mathbb{C}^9$$ with amplitude $$\frac{1}{2}$$ on $$X$$ and $$0$$ in all gaps:
   $$
   v = \frac{1}{2}(1,\ 0,\ 1,\ 0,\ 0,\ 0,\ 1,\ 0,\ 1)^T, \qquad \|v\|_2^2 = 4\cdot\frac{1}{4} = 1.
   $$
2. **Compute its unitary discrete Fourier transform** $$\hat{v}(k) = \frac{1}{\sqrt{9}}\sum_{j \in X} \frac{1}{2} e^{-2\pi i jk/9}$$: because $$X = \{0,6\} + \{0,2\}$$, the sum factors cleanly:
   $$
   \hat{v}(k) = \frac{1}{6}\bigl(1 + e^{-4\pi i k/3}\bigr)\bigl(1 + e^{-4\pi i k/9}\bigr).
   $$
3. **Evaluate the energy $$|\hat{v}(k)|^2$$ remaining on $$X = \{0, 2, 6, 8\}$$:**
   - At $$k = 0$$: $$\hat{v}(0) = \frac{1}{6}(2)(2) = \frac{2}{3} \implies |\hat{v}(0)|^2 = \frac{4}{9} \approx 0.4444$$.
   - At $$k = 6$$: $$|1 + e^{-8\pi i}| = 2$$ and $$|1 + e^{-8\pi i/3}| = |1 + e^{-2\pi i/3}| = 1 \implies |\hat{v}(6)|^2 = \bigl(\frac{2}{6}\bigr)^2 = \frac{1}{9} \approx 0.1111$$.
   - At $$k = 2$$: $$|1 + e^{-8\pi i/3}| = 1$$ and $$|1 + e^{-8\pi i/9}| = 2\cos(80^\circ) \approx 0.3473 \implies |\hat{v}(2)|^2 = \frac{1}{9}\cos^2(80^\circ) \approx 0.0034$$.
   - At $$k = 8$$: $$|1 + e^{-32\pi i/3}| = 1$$ and $$|1 + e^{-32\pi i/9}| = 2\cos(40^\circ) \approx 1.5321 \implies |\hat{v}(8)|^2 = \frac{1}{9}\cos^2(40^\circ) \approx 0.0652$$.
4. **Sum the surviving energy on $$X$$:**
   $$
   \sum_{k \in X} |\hat{v}(k)|^2 \approx 0.4444 + 0.1111 + 0.0034 + 0.0652 = 0.6241 < 1!
   $$
   After just **two generations**, nearly **38% of the wave's energy** has leaked straight into the Cantor gaps $$\{1, 3, 4, 5, 7\}$$! As the number of generations grows ($$N = 3^n$$), this leakage compounds across every scale, driving the operator norm down by a power law:

$$
\|\mathbf{1}_{X(h)}\,\mathcal{F}_h\,\mathbf{1}_{Y(h)}\|_{L^2 \to L^2} \le C h^\beta
$$

for some improvement exponent $$\beta > 0$$. Literacy is the slogan plus the geometric hypothesis; the estimates live in the paper.

---

## 2. Why physicists wanted this: trapped dust

A classical particle in a chaotic billiard usually wanders through the table. In rare cases it can bounce forever among a few obstacles. Mark the hit points on the bumpers over infinite time and you typically see **fractal dust**—the surviving trapped set.

A quantum particle is a wave. Waves leak. The question Dyatlov asked is whether that leak is forced by Fourier geometry: if the trapped set is fractal, can a wavefunction sit on it in both position and frequency? FUP says no. Hence a wave on a compact hyperbolic surface cannot hide from an open region forever: if you deleted every trajectory that entered the forbidden region, the remainder would be fractal dust, which a wave is not allowed to occupy. That is the skeleton of **Dyatlov–Jin** (2017) in two dimensions.

The same picture is why FUP is not a curiosity about Cantor sets. It is a device that turns **classical trapped sets** into **quantum delocalization**.

---

## 3. One dimension: Bourgain–Dyatlov

Jean Bourgain and Semyon Dyatlov proved a fractal uncertainty principle on the line (2016), using a method that was unusual even inside harmonic analysis. Roughly:

1. Isolate one peak of a fractal-like function at a time by multiplying by a **damping function** that is near 1 on that peak and near 0 on the others.
2. Each isolated peak has a Fourier transform that **spreads**.
3. The spreads cannot conspire to vanish on a porous set often enough to make $$\hat f$$ fractal-like.

Constructing the damping function is the hard step. It is a cousin of the **Beurling–Malliavin** multiplier theorem from the 1960s: you need a function with very specific size and Fourier-decay properties, built by a detour through complex analysis. Bourgain died in 2018; unpublished notes of his later helped unlock the higher-dimensional case.

**Status.** 1D FUP is a theorem. It already implied essential spectral gaps in some hyperbolic settings and the Dyatlov–Jin delocalization result for surfaces.

---

## 4. Higher dimensions: lines break the naive statement

In the plane, a straight line has area zero and is “full of holes” if you only look at area. Its Fourier transform (as a measure, or as a tubular neighborhood) is concentrated on the orthogonal line. So **a line and its dual line are both “porous” in the naive sense**, and they form a counterexample to any careless “no two fractals” slogan.

The Sierpiński gasket and many carpets contain straight line segments. Those sets can be highly porous in the ambient plane and still fail FUP for exactly this reason.

![Sierpiński gasket with its base highlighted as a full line]({{ site.baseurl }}/img/chapter_img/fup_sierpinski_line_obstruction.png)

*Figure. A set may look holey and still contain a line. Fourier analysis will send that line to another line. Naive FUP cannot hold for every fractal in dimension $$\ge 2$$.*

Cohen’s way out is not to ignore the counterexamples but to **exclude them by hypothesis**.

---

## 5. Line porosity and Cohen’s theorem

**Line porosity (slogan).** Draw any straight line. That line should itself meet the set in a porous way: as you travel along the line you keep hitting definite holes, at every scale, with quantitative constants. A full line sitting inside the set is forbidden. A Sierpiński carpet with extra squares removed can satisfy the condition; the usual carpet need not.

![Left: a line remains inside the set. Right: every test line is gapped]({{ site.baseurl }}/img/chapter_img/fup_line_porosity.png)

*Figure. The extra geometric hypothesis that makes higher-dimensional FUP possible. (Schematic; the paper’s definition is quantitative.)*

**Theorem (Cohen, arXiv:2305.05022; *Annals of Mathematics* **202** (2025)).** A fractal set in $$\mathbb{R}^d$$ that is line-porous obeys a fractal uncertainty principle. The main new ingredient is a **higher-dimensional Beurling–Malliavin multiplier theorem**—the damping function, rebuilt in several variables.

That is a theorem, not an announcement. Quanta’s August 2026 article is a narrative of the proof’s history (Bourgain’s notes, the 2016 IAS workshop’s pessimism, Cohen’s thesis). The contract for this course is the statement and the hypothesis, not a replay of the multiplier construction.

---

## 6. What it already unlocked, and what is still open

Once higher-dimensional FUP exists, delocalization arguments that worked on surfaces can try to move up. In 2025, Elena Kim and Nicholas Miller used Cohen’s theorem to extend “waves cannot hide” results to higher-dimensional hyperbolic spaces (under the geometric hypotheses that make the trapped set line-porous). Peter Sarnak has called this among the most spectacular applications so far.

A stronger dream is **quantum unique ergodicity (QUE)**: chaotic eigenfunctions should not only touch every region, they should **equidistribute**—look uniformly random at large scales, like a Monet that is noisy up close and a flat color from across the room. Rudnick–Sarnak (1994) formulated the conjecture for compact negatively curved manifolds; the arithmetic case was proved by Elon Lindenstrauss (2006; Soundararajan 2010), while the general geometric case remains a **major open conjecture**. FUP is an ingredient people hope to use, not a solution.

**Neighbor in this course.** The geometric taste—tubes, porosity, forbidding too much concentration on lines—is cousin to the Kakeya / restriction culture in [Wang’s harmonic analysis]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/). FUP is not Kakeya, and Kakeya is not FUP. They share the instinct that **Fourier concentration is a geometric problem**.

---

## 7. Precision versus hype

| Claim | Verdict | Correction |
|-------|---------|------------|
| “FUP says no function can be fractal.” | False | It constrains a function **and** its Fourier transform together. |
| “Every fractal in every dimension obeys FUP.” | False | Lines (and sets containing lines) are counterexamples without line porosity. |
| “Cohen solved quantum chaos.” | Overstated | He proved a Fourier theorem used in some quantum-chaos arguments. QUE is open. |
| “Classical particles and quantum waves have the same trapped sets.” | False | That difference is the point of applying FUP. |
| “Quanta proved the theorem.” | False | Cohen’s *Annals* paper did. Journalism is a map. |

---

## References and further reading

- Alex Cohen — [Fractal uncertainty in higher dimensions](https://arxiv.org/abs/2305.05022), *Annals of Mathematics* **202** (2025).
- Bourgain–Dyatlov — [Spectral gaps without the pressure condition](https://arxiv.org/abs/1612.09040) (1D FUP as a tool).
- Shalma Wegsman — [Graduate Student Proves a Quantum Uncertainty Principle for Fractals](https://www.quantamagazine.org/graduate-student-proves-the-fractal-uncertainty-principle-20260812/), *Quanta*, 12 Aug 2026 (accessed 2026-08-19).
- [Uncertainty literacy]({{ site.baseurl }}/contents/en/chapter06/06_29_Uncertainty_Principles/); [Wang]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/); [fractals]({{ site.baseurl }}/contents/en/chapter04/04_03_Fractals/); [chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/).
- Pack: `research/video-research/uncertainty-principles/`.
