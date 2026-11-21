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

Richard Feynman’s **path integral** rewrites quantum amplitudes as a “sum over histories”: roughly

$$
\langle q_f,t_f|q_i,t_i\rangle \;\sim\; \int \mathcal{D}q\; \exp\!\Big(\frac{i}{\hbar}S[q]\Big),
$$

where $$S[q]$$ is the classical action of a path from $$(q_i,t_i)$$ to $$(q_f,t_f)$$. The idea is physically brilliant—classical paths dominate by stationary phase when $$\hbar$$ is small; interference encodes quantum mechanics—and it organizes perturbation theory, instanton calculus, and large parts of quantum field theory pedagogy.

Mathematically, the object $$\mathcal{D}q$$ is subtle: there is typically **no Lebesgue measure on infinite-dimensional path space** with the properties physicists casually assume. This lecture separates **the idea**, **what can be made rigorous**, and **what remains heuristic**, for Bridge literacy (**LO1**, **LO6**). Prerequisites: [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/); companion: [distributions]({{ site.baseurl }}/contents/en/chapter03/03_12_Distributions_Dirac/).

---

## Learning objectives

After this lecture you should be able to:

- State the path-integral slogan and its relation to the classical action $$S$$.
- Explain stationary-phase / $$\hbar\to 0$$ intuition connecting path integrals to classical mechanics.
- Distinguish **real-time Feynman integrals**, **imaginary-time (Euclidean) integrals**, and **Wiener measure**.
- Name at least two rigorous footholds (e.g. Trotter product formula heuristics → Schrödinger; Wiener measure for Brownian motion / imaginary time).
- Place path integrals in QFT: generating functionals, Feynman diagrams, and the open constructive status in 4D ([YM mass gap]({{ site.baseurl }}/contents/en/chapter01/01_10_Yang_Mills_Mass_Gap/)).
- Critique popular claims that “the path integral is fully rigorous mathematics for all QFTs.”

---

## 1. From Dirac’s observation to Feynman

Dirac (1930s) emphasized that short-time propagators relate to $$\exp(iS/\hbar)$$. Feynman (1948) turned the idea into a systematic formulation of quantum mechanics equivalent (under suitable conditions) to the Schrödinger picture: discretize time, integrate over intermediate positions, take a continuum limit.

**One-step mechanism (LO4).** Quantum evolution is assembled from **amplitudes of entire trajectories**, weighted by phase $$e^{iS/\hbar}$$, not only from differential evolution of a wavefunction—though the two pictures match when both are well-defined.

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

**Real time** makes the integrand oscillatory ($$e^{iS/\hbar}$$), which is analytically harder than positive integrands. **Wick rotation** $$t\to -i\tau$$ (when justifiable) turns many problems into **Euclidean** integrals with damping $$e^{-S_E/\hbar}$$, closer to statistical mechanics.

---

## 4. Rigorous footholds

| Setting | Mathematical object | Status (seminar) |
|---------|---------------------|------------------|
| Brownian motion | **Wiener measure** on continuous paths | Fully rigorous; expectation of functionals well-defined |
| Imaginary-time QM | Feynman–Kac formula linking semigroups $$e^{-\tau H/\hbar}$$ to path expectations | Theorems under hypotheses on $$V$$ |
| Finite-dim lattice QFT | Ordinary integrals over many variables | Well-defined; continuum limit is the hard step |
| Perturbative QFT | Formal series of Feynman diagrams | Powerful; Borel/ renormalon issues; not a non-perturbative definition |
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

## 7. Precision versus hype (LO6)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Path integrals are as rigorous as Riemann integrals for all systems.” | False | Infinite-dimensional measure theory is the issue. |
| “Because path integrals work in QED experiments, the measure exists as a theorem.” | Category mix | Empirical success ≠ constructive existence proof. |
| “Wiener measure is the Feynman path integral.” | Incomplete | Wiener relates to imaginary-time / diffusion; real-time oscillatory integrals differ. |
| “Path integrals replace Hilbert space.” | Misleading | In QM they are often equivalent formulations when both defined; Hilbert space remains central. |

---

## Exercises

1. **Slogan.** Write the path-integral idea in ≤60 words for a classmate who knows the Schrödinger equation only.  
2. **Stationary phase.** Why do classical paths dominate as $$\hbar\to 0$$ in the formal integral?  
3. **Euclidean vs real time.** One paragraph on why Wick rotation helps analysis.  
4. **Wiener.** What probability measure makes Brownian-path expectations rigorous?  
5. **LO6.** Critique: “Mathematicians refuse path integrals because they dislike physics.”  
6. **Bridge.** Link path-integral saddles to instanton topology in one careful paragraph.

---

## References and further reading

1. Feynman & Hibbs — *Quantum Mechanics and Path Integrals* (physics classic).  
2. Simon — *Functional Integration and Quantum Physics*.  
3. Glimm & Jaffe — constructive tradition.  
4. Course: [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/), [Instantons]({{ site.baseurl }}/contents/en/chapter06/06_21_Instantons_Anomalies/), [RG]({{ site.baseurl }}/contents/en/chapter06/06_22_Renormalization_Group/), [YM mass gap]({{ site.baseurl }}/contents/en/chapter01/01_10_Yang_Mills_Mass_Gap/).  
