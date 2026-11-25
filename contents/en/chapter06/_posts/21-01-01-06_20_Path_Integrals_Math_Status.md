---
layout: post
title: "Path Integrals: Idea, Power, and Mathematical Status"
chapter: '06'
order: 20
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

In classical mechanics, a tossed baseball follows one single parabolic arc—the unique trajectory that makes the *action* $$S[q]$$ stationary. Rethinking the double-slit experiment in the late 1940s, Richard Feynman pushed that picture to a breathtaking extreme: imagine opening three slits, four slits, then punching infinitely many holes through infinitely many screens between start and finish. A quantum particle traveling from $$(q_i,t_i)$$ to $$(q_f,t_f)$$ **does not pick one path—it explores every conceivable path simultaneously**, weighting each trajectory $$q(\cdot)$$ by a spinning unit complex arrow $$\exp\!\bigl(\tfrac{i}{\hbar}S[q]\bigr)$$:

$$
\langle q_f,t_f|q_i,t_i\rangle \;\sim\; \int \mathcal{D}q\; \exp\!\Big(\frac{i}{\hbar}S[q]\Big).
$$

As a physical idea, the **path integral** is dazzling: when $$\hbar$$ is small, wildly oscillating phases cancel out away from the classical path, while interference encodes all of quantum mechanics. Yet under the microscope of mathematical analysis, the symbol $$\mathcal{D}q$$ hides a sharp catch: there is **no translation-invariant Lebesgue measure on infinite-dimensional path space**. This lecture cleanly separates **the idea**, **what is already a theorem**, and **what remains heuristic**. Prerequisites: [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/); companion: [distributions]({{ site.baseurl }}/contents/en/chapter03/03_12_Distributions_Dirac/).

---

## Key ideas: What Do Functional Integration, Infinite-Dimensional Measure Theory, and Asymptotics Study?

When the variable of integration is no longer a point $$x \in \mathbb{R}^n$$ but an entire **continuous curve** $$q: [0,T] \to \mathbb{R}^d$$, three branches of analysis meet:

### 1. Infinite-Dimensional Measure Theory and Wiener Measure
In $$\mathbb{R}^n$$, a cube of side $$2$$ has volume $$2^n \to \infty$$ as $$n \to \infty$$, while a cube of side $$1/2$$ has volume $$(1/2)^n \to 0$$—so **no uniform "volume" (Lebesgue measure) exists on infinite-dimensional path space**. Norbert Wiener's 1923 breakthrough was to absorb the Gaussian kinetic factor $$e^{-\frac{1}{2}\int \dot{q}^2 dt}$$ *into* the measure itself, producing **Wiener measure**—a completely rigorous probability measure on continuous paths that underpins Brownian motion, quantitative finance (Black–Scholes), and the Feynman–Kac formula for imaginary-time quantum mechanics.

### 2. Stationary Phase and Asymptotic Analysis
For finite-dimensional oscillatory integrals $$\int e^{iS(x)/\hbar} a(x)\,dx$$ as $$\hbar \to 0$$, asymptotic analysis proves that the dominant contribution comes strictly from neighborhoods of **critical points** $$S'(x_0) = 0$$ (or saddles in imaginary time). Physically, this explains how classical least-action trajectories emerge from quantum interference.

### 3. Time-Slicing (Trotter) and Constructive Field Theory
To give $$\mathcal{D}q$$ precise meaning, mathematicians discretize time (or all of spacetime) into $$N$$ slices—reducing the path integral to an ordinary $$N$$-variable integral—and study the $$N \to \infty$$ limit via the **Trotter product formula** in quantum mechanics or lattice regularization in constructive QFT.

---

## Learning objectives

After this lecture you should be able to:

- State the path-integral slogan and its relation to the classical action $$S$$.
- Explain stationary-phase / $$\hbar\to 0$$ intuition connecting path integrals to classical mechanics.
- Distinguish **real-time Feynman integrals**, **imaginary-time (Euclidean) integrals**, and **Wiener measure**.
- Name at least two rigorous footholds (e.g. Trotter product formula → Schrödinger; Wiener measure for Brownian motion / imaginary time).
- Place path integrals in QFT: generating functionals, Feynman diagrams, and the open constructive status in 4D ([YM mass gap]({{ site.baseurl }}/contents/en/chapter01/01_10_Yang_Mills_Mass_Gap/)).
- Critique popular claims that “the path integral is fully rigorous mathematics for all QFTs.”

---

## 1. From Dirac’s observation to Feynman

Dirac (1930s) emphasized that short-time propagators relate to $$\exp(iS/\hbar)$$. Feynman (1948) turned the idea into a systematic formulation of quantum mechanics equivalent (under suitable conditions) to the Schrödinger picture: discretize time, integrate over intermediate positions, take a continuum limit.

### Explanation: Slicing Time and Summing Over Paths by Hand

To see that a path integral is not magic, let us compute the imaginary-time (Euclidean) propagator of a 1D free particle ($$m = 1, \hbar = 1$$) traveling from $$q_0 = 0$$ at $$\tau = 0$$ to $$q_2 = x$$ at $$\tau = 2\varepsilon$$ through **one intermediate point** $$q_1 \in \mathbb{R}$$ (summing over all two-segment polygonal paths $$0 \to q_1 \to x$$):

1. **Write the Euclidean action of the polygonal path:** With velocities $$\frac{q_1 - 0}{\varepsilon}$$ and $$\frac{x - q_1}{\varepsilon}$$, the total action $$S_E = \frac{1}{2}\sum v^2 \varepsilon$$ is
   $$
   S_E(q_1) = \frac{q_1^2}{2\varepsilon} + \frac{(x - q_1)^2}{2\varepsilon}.
   $$
2. **Complete the square in $$q_1$$:**
   $$
   q_1^2 + (x - q_1)^2 = 2q_1^2 - 2xq_1 + x^2 = 2\Bigl(q_1 - \frac{x}{2}\Bigr)^2 + \frac{x^2}{2}.
   $$
   Notice that the minimum action occurs right at $$q_1^* = \frac{x}{2}$$—the midpoint on the classical straight-line path!
3. **Integrate over all intermediate positions $$q_1 \in (-\infty,\infty)$$** (using $$\int_{-\infty}^{\infty} e^{-u^2/\varepsilon}\,du = \sqrt{\pi\varepsilon}$$):
   $$
   K(0 \to x;\, 2\varepsilon) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\varepsilon}}e^{-\frac{q_1^2}{2\varepsilon}} \cdot \frac{1}{\sqrt{2\pi\varepsilon}}e^{-\frac{(x-q_1)^2}{2\varepsilon}}\,dq_1 = \frac{1}{2\pi\varepsilon}\,e^{-\frac{x^2}{4\varepsilon}} \int_{-\infty}^{\infty} e^{-\frac{(q_1 - x/2)^2}{\varepsilon}}\,dq_1 = \frac{1}{\sqrt{4\pi\varepsilon}}\,e^{-\frac{x^2}{4\varepsilon}}.
   $$
4. **Check the result:** With $$T = 2\varepsilon$$, $$\frac{1}{\sqrt{2\pi T}}e^{-x^2/(2T)}$$ is **exact**—it is the heat kernel solving $$\partial_T u = \frac{1}{2}\partial_x^2 u$$ (standard Brownian motion)! Repeating with $$N$$ slices and sending $$N \to \infty$$ reproduces Wiener measure rigorously.

**Core mechanism.** Quantum evolution is assembled from **amplitudes of entire trajectories**, weighted by phase $$e^{iS/\hbar}$$ (or $$e^{-S_E/\hbar}$$ in Euclidean time), not only from differential evolution of a wavefunction—though the two pictures match when both are well-defined.

---

## 2. Finite-dimensional rehearsal

Ordinary oscillatory integrals

$$
I(\hbar)=\int_{\mathbb{R}^n} e^{iS(x)/\hbar}\,a(x)\,dx
$$

are classical analysis. Stationary phase says leading asymptotics as $$\hbar\to 0$$ come from critical points of $$S$$—the “classical paths.” Path integrals try to run the same story when $$x$$ is replaced by a path $$q(\cdot)$$ and $$n\to\infty$$.

---

## 3. What goes wrong measure-theoretically?

Path space $$C([0,T],\mathbb{R}^d)$$ is infinite-dimensional. There is no translation-invariant Lebesgue measure that behaves like finite-dimensional volume. The formal symbol $$\mathcal{D}q$$ must be interpreted as a **limit of finite-dimensional integrals**, a **Gaussian-type measure with a different quadratic form**, or another constructive prescription—not as “Lebesgue measure on paths.”

**Real time** makes the integrand oscillatory ($$e^{iS/\hbar}$$), which is analytically harder than positive integrands (Cameron's 1960 theorem proves that even the complex Gaussian weight does not form a countably additive complex measure of bounded variation). **Wick rotation** $$t\to -i\tau$$ (when justifiable) turns many problems into **Euclidean** integrals with damping $$e^{-S_E/\hbar}$$, closer to statistical mechanics.

---

## 4. Rigorous footholds

| Setting | Mathematical object | Status (seminar) |
|---------|---------------------|------------------|
| Brownian motion | **Wiener measure** on continuous paths | Fully rigorous; expectation of functionals well-defined |
| Imaginary-time QM | Feynman–Kac formula linking semigroups $$e^{-\tau H/\hbar}$$ to path expectations | Theorems under hypotheses on $$V$$ |
| Finite-dim lattice QFT | Ordinary integrals over many variables | Well-defined; continuum limit is the hard step |
| Perturbative QFT | Formal series of Feynman diagrams | Powerful; Borel/renormalon issues; not a non-perturbative definition |
| Constructive 4D YM | Continuum measure with gap | [Clay open]({{ site.baseurl }}/contents/en/chapter01/01_10_Yang_Mills_Mass_Gap/) |

The **Trotter product formula** and related operator theorems justify some continuum limits for quantum mechanics with reasonable potentials—connecting lattice path sums to $$e^{-itH/\hbar}$$ without pretending $$\mathcal{D}q$$ is elementary Lebesgue measure.

---

## 5. Instantons, tunneling, and topology

In Euclidean signature, non-perturbative saddles of $$S_E$$—including **instantons**—contribute exponentially small effects $$e^{-S_E/\hbar}$$ invisible in finite-order perturbation theory. That calculus is central to vacuum structure in gauge theory ([instantons & anomalies]({{ site.baseurl }}/contents/en/chapter06/06_21_Instantons_Anomalies/), [gauge as geometry]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/)).

Here path integrals are a **bookkeeping language** for saddle-point expansions; geometric analysis of classical solutions supplies the saddles.

---

## 6. Quantum field theory: power and gap

In QFT, path integrals formally compute correlation functions by integrating over field configurations $$\phi(x)$$ with weight $$e^{iS[\phi]/\hbar}$$. Expanding about free fields yields Feynman rules. Gauge fixing, ghosts, and BRST organize redundancies ([gauge essay]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/)).

**Power.** Unifies symmetries, generates diagrammatics, connects to statistical field theory via Euclidean formulations, and inspires topological quantum field theory (TQFT) and dualities ([Duality principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/)).

**Gap.** A general rigorous continuum construction of interacting 4D path-integral QFT matching the Standard Model remains unfinished mathematics—even while physics predictions succeed spectacularly in their regimes of validity.

---

## 7. Precision versus hype

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Path integrals are as rigorous as Riemann integrals for all systems.” | False | Infinite-dimensional measure theory is the issue. |
| “Because path integrals work in QED experiments, the measure exists as a theorem.” | Category mix | Empirical success ≠ constructive existence proof. |
| “Wiener measure is the Feynman path integral.” | Incomplete | Wiener relates to imaginary-time / diffusion; real-time oscillatory integrals differ. |
| “Path integrals replace Hilbert space.” | Misleading | In QM they are often equivalent formulations when both defined; Hilbert space remains central. |

---

## References and further reading

1. Feynman & Hibbs — *Quantum Mechanics and Path Integrals* (physics classic).  
2. Simon — *Functional Integration and Quantum Physics*.  
3. Glimm & Jaffe — constructive tradition.  
4. Course: [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/), [Instantons]({{ site.baseurl }}/contents/en/chapter06/06_21_Instantons_Anomalies/), [RG]({{ site.baseurl }}/contents/en/chapter06/06_22_Renormalization_Group/), [YM mass gap]({{ site.baseurl }}/contents/en/chapter01/01_10_Yang_Mills_Mass_Gap/).  
