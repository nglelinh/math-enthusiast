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

An ordinary glass of water on your desk holds roughly $$10^{25}$$ $$\text{H}_2\text{O}$$ molecules colliding billions of times per second. No supercomputer on Earth could ever track every molecule's trajectory—yet at the human scale, that glass of water obeys astonishingly crisp laws: at $$0^\circ\text{C}$$ it snaps abruptly into ice, and at $$100^\circ\text{C}$$ it erupts into steam, with pressure and heat capacity predictable to many decimal places. How does microscopic chaos crystallize into razor-sharp jumps called **phase transitions**?

**Equilibrium statistical mechanics** answers this through the lens of **probability theory**: instead of tracking a single trajectory, we place a probability distribution—a **Gibbs measure** weighted by $$e^{-\beta E(s)}$$—over all microscopic configurations, package the entire system into one generating function called the **partition function $$Z$$**, and send the particle count $$N \to \infty$$. This exact framework both fuels modern probability theory (large deviations, concentration of measure, SLE) and—via Wick rotation—mirrors Euclidean quantum field theory.

This bridge map deepens §4 of the [mathematical physics hub]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/) and links [RG]({{ site.baseurl }}/contents/en/chapter06/06_22_Renormalization_Group/) and [path integrals]({{ site.baseurl }}/contents/en/chapter06/06_20_Path_Integrals_Math_Status/).

---

## Key ideas: What Three Pillars Anchor Mathematical Statistical Mechanics?

If you know undergraduate probability (expectations, law of large numbers, and the softmax function in machine learning), three clear pillars unlock this entire field:

### 1. Boltzmann–Gibbs Weights and the Energy–Entropy Tug-of-War
The familiar softmax function in neural networks is literally the **Boltzmann–Gibbs distribution** $$p(s) = \frac{1}{Z}e^{-\beta E(s)}$$ with inverse temperature $$\beta = 1/(k_B T)$$. Every equilibrium phenomenon is a tug-of-war between **energy** (pulling the system toward low-energy ordered states) and **entropy** (the overwhelming number of disordered configurations): at high $$T$$ ($$\beta \to 0$$) entropy wins (gas/paramagnet); at low $$T$$ ($$\beta \to \infty$$) energy wins (crystal/ferromagnet).

### 2. The Thermodynamic Limit and Phase Transitions as Singularities
For any finite number of particles $$N$$, $$Z_N(\beta)$$ is a finite sum of smooth positive exponentials, so it can never have a sharp corner or jump. A mathematical **phase transition** emerges strictly in the limit $$N \to \infty$$, when the free-energy density $$f(\beta) = \lim_{N\to\infty} -\frac{1}{\beta N}\log Z_N(\beta)$$ develops a **non-analytic singularity**, signaling the coexistence of *multiple* infinite-volume Gibbs measures.

### 3. Strongly Interacting Probability and Cross-Disciplinary Reach
Unlike introductory probability's *independent* random variables, statistical mechanics studies infinitely many **strongly interacting** variables on a lattice $$\mathbb{Z}^d$$—spawning large deviations, MCMC sampling and diffusion models in data science, 2D SLE scaling limits, and constructive Euclidean QFT.

---

## Learning objectives

After this lecture you should be able to:

- Write a partition function $$Z=\sum_s e^{-\beta E(s)}$$ and interpret $$\beta=1/(kT)$$.
- Explain the **thermodynamic limit** slogan: $$N\to\infty$$ with density fixed; phase transitions as singularities of free energy.
- Connect Ising-type models to **phase transitions** and universality / RG fixed points.
- State what a **Gibbs measure** is trying to be (probability on configurations weighted by energy).
- Distinguish equilibrium statistical mechanics from nonequilibrium / turbulence frontiers.
- Avoid the loose claim that “a phase transition is just when a simulation plot looks jumpy.”

**Prerequisites.** Basic probability (expectation, independence idea); exponential function. [Probability → data science]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/) helpful.

---

## 1. Micro to macro in one formula

For a finite system with configurations $$s$$ and energy $$E(s)$$,

$$
Z(\beta)=\sum_s e^{-\beta E(s)},\qquad
\langle O\rangle = \frac{1}{Z}\sum_s O(s)\,e^{-\beta E(s)}.
$$

Free energy $$F=-\beta^{-1}\log Z$$ generates all of equilibrium thermodynamics: differentiating $$\log Z$$ with respect to $$\beta$$ gives $$\langle E\rangle = -\partial_\beta \log Z$$ and $$\operatorname{Var}(E) = \partial_\beta^2 \log Z$$ (proportional to heat capacity!). Probabilities $$p(s)\propto e^{-\beta E(s)}$$ are the **Boltzmann–Gibbs** weights.

### Explanation: Solving the 2-Spin Ising Model Completely by Hand

To see how $$Z(\beta)$$ generates every macroscopic observable, solve a tiny 2-spin magnet $$\sigma_1, \sigma_2 \in \{+1, -1\}$$ with ferromagnetic energy $$E(\sigma_1, \sigma_2) = -J\sigma_1\sigma_2$$ ($$J > 0$$):

1. **List all four configurations and their Boltzmann weights:**
   - Aligned states $$(+1, +1)$$ and $$(-1, -1)$$: energy $$E = -J$$, weight $$e^{+\beta J}$$ each.
   - Anti-aligned states $$(+1, -1)$$ and $$(-1, +1)$$: energy $$E = +J$$, weight $$e^{-\beta J}$$ each.
2. **Sum to obtain the partition function $$Z(\beta)$$:**
   $$
   Z(\beta) = 2e^{\beta J} + 2e^{-\beta J} = 4\cosh(\beta J).
   $$
3. **Read off average energy and spin correlation by differentiating $$\log Z$$:**
   $$
   \langle E \rangle = -\frac{\partial}{\partial\beta}\log\bigl(4\cosh(\beta J)\bigr) = -J\tanh(\beta J),
   $$
   and since $$E = -J\sigma_1\sigma_2$$, the **two-spin correlation** is immediately
   $$
   \langle \sigma_1\sigma_2 \rangle = \frac{2e^{\beta J} - 2e^{-\beta J}}{4\cosh(\beta J)} = \tanh(\beta J).
   $$
4. **Test two concrete temperatures:**
   - **High temperature ($$\beta J = 0.1$$):** $$\langle \sigma_1\sigma_2 \rangle = \tanh(0.1) \approx 0.10$$—the two spins barely notice each other.
   - **Low temperature ($$\beta J = 3$$):** $$\langle \sigma_1\sigma_2 \rangle = \tanh(3) \approx 0.995$$—over $$99.7\%$$ probability that both spins lock together!
   - Yet notice that $$\tanh(\beta J)$$ is infinitely smooth everywhere—showing visually why only the $$N \to \infty$$ limit can create a sharp phase transition!

**Core mechanism.** Equilibrium macroscopic observables are **expectations under an energy-biased probability measure**, not single trajectories.

---

## 2. Thermodynamic limit and phases

Interesting singularities (first-order jumps, critical points) typically appear only after $$N\to\infty$$. Finite systems have smooth $$Z$$; non-analytic free energy density is a limit phenomenon—hence mathematical care with existence and non-uniqueness of infinite-volume Gibbs measures (Dobrushin–Lanford–Ruelle equations).

**Ising model.** Spins $$\pm 1$$ on a lattice $$\mathbb{Z}^d$$ with neighbor coupling $$E(\sigma) = -J\sum_{i\sim j}\sigma_i\sigma_j$$:
- In **1D**: no phase transition at any positive temperature (Ising, 1925).
- In **2D**: Lars Onsager (1944) solved the free energy exactly, pinpointing a sharp transition at $$\beta_c J = \frac{1}{2}\ln(1+\sqrt{2})$$—a landmark where physics and rigorous mathematics met.
- In **3D** and higher: phase transitions exist (Peierls argument), yet no closed-form Onsager solution exists; determining exact critical exponents remains an active frontier.

---

## 3. Probability structures

| Idea | Role |
|------|------|
| Large deviations | Exponential cost of rare events (Cramér, Donsker–Varadhan) |
| Correlation decay / mixing | Uniqueness of Gibbs measures; convergence rates of MCMC samplers |
| Scaling limits | Continuum fields from lattice models (connect RG, SLE in 2D—Fields Medals for Werner, Smirnov, Duminil-Copin) |
| Concentration | Typical configurations hug means (Talagrand's spin-glass theorems) |

Statistical mechanics is thus a **source of probability theorems**, not only an application of undergrad combinatorics.

---

## 4. Bridge to QFT and RG

Euclidean quantum field theory formally looks like a continuum statistical field theory with action playing the role of energy and $$\hbar$$ playing the role of $$k_B T$$ ([path integrals]({{ site.baseurl }}/contents/en/chapter06/06_20_Path_Integrals_Math_Status/)). Critical phenomena and continuum limits are organized by the renormalization group ([RG]({{ site.baseurl }}/contents/en/chapter06/06_22_Renormalization_Group/)). Constructive field theory often proceeds by controlling lattice approximations and limits—same spirit as infinite-volume statistical mechanics.

---

## 5. Precision versus hype

| Claim | Verdict | Correction |
|-------|---------|------------|
| “A phase transition is when my plot looks discontinuous.” | Loose | Mathematical phase transitions concern thermodynamic limits and free-energy singularities. |
| “Statistical mechanics is only for chemists.” | False | Core pure-math interfaces with probability, PDE, and QFT. |
| “Because Onsager solved 2D Ising, all critical phenomena are solved.” | False | 2D Ising is a jewel; general theories (especially 3D and nonequilibrium/turbulence) remain rich and open. |

---

## References and further reading

1. Baxter — *Exactly Solved Models in Statistical Mechanics*.  
2. Georgii — *Gibbs Measures and Phase Transitions*.  
3. Course: [Math physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/), [RG]({{ site.baseurl }}/contents/en/chapter06/06_22_Renormalization_Group/), [Probability]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/).  
