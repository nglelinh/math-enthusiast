---
layout: post
title: "Statistical Mechanics and Probability"
chapter: '06'
order: 27
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

Macroscopic laws—pressure, magnetization, phase diagrams—emerge from enormous numbers of microscopic degrees of freedom. **Equilibrium statistical mechanics** turns that emergence into probability: Gibbs measures, partition functions, thermodynamic limits. The same structures feed probability theory (large deviations, Gibbs point processes) and, via Euclidean path integrals, quantum field theory.

This P2 map deepens §4 of the [mathematical physics hub]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/) and links [RG]({{ site.baseurl }}/contents/en/chapter06/06_22_Renormalization_Group/) and [path integrals]({{ site.baseurl }}/contents/en/chapter06/06_20_Path_Integrals_Math_Status/) (**LO2**-adjacent size ideas, **LO4**, **LO6**).

---

## Learning objectives

After this lecture you should be able to:

- Write a partition function $$Z=\sum_s e^{-\beta E(s)}$$ and interpret $$\beta=1/(kT)$$.
- Explain the **thermodynamic limit** slogan: $$N\to\infty$$ with density fixed; phase transitions as singularities of free energy.
- Connect Ising-type models to **phase transitions** and universality / RG fixed points.
- State what a **Gibbs measure** is trying to be (probability on configurations weighted by energy).
- Distinguish equilibrium statistical mechanics from nonequilibrium / turbulence frontiers.
- Avoid LO6: “phase transition = graph looks jumpy in a simulation.”

**Prerequisites.** Basic probability (expectation, independence idea); exponential function. [Probability → data science]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/) helpful.

---

## 1. Micro to macro in one formula

For a finite system with configurations $$s$$ and energy $$E(s)$$,

$$
Z(\beta)=\sum_s e^{-\beta E(s)},\qquad
\langle O\rangle = \frac{1}{Z}\sum_s O(s)\,e^{-\beta E(s)}.
$$

Free energy $$F=-\beta^{-1}\log Z$$ generates thermodynamics. Probabilities $$p(s)\propto e^{-\beta E(s)}$$ are the **Boltzmann–Gibbs** weights.

**One-step mechanism (LO4).** Equilibrium macroscopic observables are **expectations under an energy-biased probability measure**, not single trajectories.

---

## 2. Thermodynamic limit and phases

Interesting singularities (first-order jumps, critical points) typically appear only after $$N\to\infty$$. Finite systems have smooth $$Z$$; non-analytic free energy density is a limit phenomenon—hence mathematical care with existence of infinite-volume Gibbs measures (Dobrushin–Lanford–Ruelle, etc.).

**Ising model.** Spins $$\pm 1$$ on a lattice with neighbor coupling: exactly solved in 2D (Onsager)—a landmark where physics and rigorous math met. Higher dimensions and long-range models remain active.

---

## 3. Probability structures

| Idea | Role |
|------|------|
| Large deviations | Exponential cost of rare events (Cramér, Donsker–Varadhan) |
| Correlation decay / mixing | Uniqueness of Gibbs measures; approach to equilibrium |
| Scaling limits | Continuum fields from lattice models (connect RG, SLE in 2D) |
| Concentration | Typical configurations hug means (Talagrand culture—see Abel essays) |

Statistical mechanics is thus a **source of probability theorems**, not only an application of undergrad combinatorics.

---

## 4. Bridge to QFT and RG

Euclidean quantum field theory formally looks like a continuum statistical field theory with action playing the role of energy ([path integrals]({{ site.baseurl }}/contents/en/chapter06/06_20_Path_Integrals_Math_Status/)). Critical phenomena and continuum limits are organized by the renormalization group ([RG]({{ site.baseurl }}/contents/en/chapter06/06_22_Renormalization_Group/)). Constructive field theory often proceeds by controlling lattice approximations and limits—same spirit as infinite-volume statistical mechanics.

---

## 5. Precision versus hype (LO6)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “A phase transition is when my plot looks discontinuous.” | Loose | Mathematical phase transitions concern thermodynamic limits and free-energy singularities. |
| “Statistical mechanics is only for chemists.” | False | Core pure-math interfaces with probability, PDE, and QFT. |
| “Because Onsager solved 2D Ising, all critical phenomena are solved.” | False | 2D Ising is a jewel; general theories remain rich and open. |

---

## Exercises

1. **Two-state system.** Energies $$0$$ and $$E$$: write $$Z$$ and mean energy vs $$\beta$$.  
2. **Thermodynamic limit.** Why might $$F$$ be smooth for finite $$N$$ but not in the limit?  
3. **Gibbs.** In ≤40 words, what does $$p(s)\propto e^{-\beta E(s)}$$ encode?  
4. **Bridge.** One paragraph: Euclidean QFT as “statistical mechanics of fields.”  
5. **LO6.** Rewrite: “Simulations show a jump, so we proved a phase transition theorem.”

---

## References and further reading

1. Baxter — *Exactly Solved Models in Statistical Mechanics*.  
2. Georgii — *Gibbs Measures and Phase Transitions*.  
3. Course: [Math physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/), [RG]({{ site.baseurl }}/contents/en/chapter06/06_22_Renormalization_Group/), [Probability]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/).  
