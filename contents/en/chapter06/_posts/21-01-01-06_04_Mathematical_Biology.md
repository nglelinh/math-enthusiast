---
layout: post
title: "Mathematical Biology"
chapter: '06'
order: 4
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

Biology is noisy, multi-scale, and historically descriptive—yet every successful quantitative claim eventually becomes mathematics: rates, balances, geometries, stochastic processes, and inference from incomplete data. **Mathematical biology** is not a single theorem; it is a family of modeling languages that turn living systems into objects one can analyze, simulate, and sometimes control. The frontier is honesty about scales: a beautiful ODE can be right for a well-mixed tank and wrong for a tissue; a genome-scale network can be structurally interesting and still underdetermined by measurements.

This lecture maps core model classes—population dynamics, reaction kinetics, spatial pattern formation, stochastic gene expression, evolutionary games, and network biology—while practicing **theorem vs heuristic vs hype** literacy in a domain flooded with “AI for biology” headlines.

---

## Learning objectives

After this lecture you should be able to:

- Write and interpret a simple **compartment ODE** (e.g., logistic growth or SIR) and explain what “well-mixed” assumes.
- Describe mass-action chemical kinetics as a system $$\dot x = f(x)$$ built from reaction stoichiometry, and name when stochastic models become essential.
- State the idea of **Turing pattern formation** (diffusion-driven instability) without claiming it explains every biological pattern.
- Explain why molecular noise matters in gene regulation using a birth–death or chemical master equation intuition.
- Distinguish structural network properties (graphs of interactions) from dynamical predictions that require parameters and kinetics.
- Critique one overclaim about “mathematical models predicting life” or “AI solving biology.”

**Prerequisites.** Elementary ODEs and derivatives; basic probability; comfort with “rate of change” language. Linear algebra helps for multi-variable systems.

---

## 1. Populations and compartments: the ODE workhorse

The logistic equation

$$
\frac{dN}{dt} = rN\Bigl(1 - \frac{N}{K}\Bigr)
$$

models growth limited by carrying capacity $$K$$. Epidemiological **SIR** models partition a population into susceptible, infected, and recovered compartments with mass-action infection terms:

$$
\dot S = -\beta SI,\qquad
\dot I = \beta SI - \gamma I,\qquad
\dot R = \gamma I.
$$

Threshold quantities such as the basic reproduction number $$R_0$$ arise from linearization at disease-free equilibria: if $$R_0>1$$, invasion is possible in the idealized model.

**What is theorem-shaped here?** Local stability criteria for equilibria of smooth ODEs; threshold theorems in structured epidemic models under explicit assumptions. **What is modeling judgment?** Choice of compartments, contact structure, time-varying parameters, and behavioral feedback. COVID-era public communication often blurred these layers; good literacy separates mathematical consequences of a model from empirical fit and policy.

---

## 2. Biochemical networks: stoichiometry and kinetics

A reaction network with species concentrations $$x\in\mathbb{R}^n_{\ge 0}$$ and stoichiometry matrix $$\Gamma$$ can be written

$$
\dot x = \Gamma\, v(x),
$$

where $$v(x)$$ are reaction rates (mass-action polynomials, Michaelis–Menten terms, Hill functions, …). Deficiency theory and chemical reaction network theory (CRNT) give structural results: for some network classes, existence and uniqueness of positive equilibria, or absence of multistationarity, can be read partly from graph structure independent of rate constants.

**Systems biology** builds large annotated networks (metabolism, signaling). Structural properties—conservation laws, elementary flux modes—are mathematical; quantitative prediction still needs parameters, many of which are poorly known. Identifiability and sloppiness of multiparameter models are research topics at the interface of algebra, statistics, and experiment design.

---

## 3. Space: PDEs, diffusion, and pattern formation

When concentrations vary in space, reaction–diffusion systems appear:

$$
\partial_t u = D\Delta u + f(u),
$$

with diffusion matrix $$D$$ and local kinetics $$f$$. **Alan Turing** (1952) showed that diffusion, usually thought of as smoothing, can destabilize a homogeneous equilibrium and produce spatial patterns under activator–inhibitor-type kinetics. That is a precise linear-stability mechanism—not a universal explanation of zebra stripes, embryogenesis, or cities.

Spatial ecology, morphogen gradients, and biofilm models all live here. Boundary conditions, domain growth, and stochastic spatial models (individual-based) change conclusions. PDE theory (existence, regularity, long-time behavior) supplies theorems; matching them to embryos supplies science.

---

## 4. Stochasticity: when molecules are few

In a cell, some species exist in tens of copies. Continuous ODEs can mislead. The **chemical master equation** evolves the probability $$P(n,t)$$ of molecule counts $$n$$; Gillespie’s stochastic simulation algorithm samples trajectories. Birth–death processes for gene expression produce bursty mRNA and protein distributions; noise can be a feature (bet-hedging) or a bug (fragility).

Mathematically one meets continuous-time Markov chains on countable state spaces, moment closures, large-deviation heuristics, and hybrid models coupling discrete switches to continuous concentrations. **Theorem vs approximation:** exact CME solutions are rare; diffusion approximations (Fokker–Planck, Langevin) are controlled in some scaling limits and uncontrolled folklore in others.

---

## 5. Evolution, games, and fitness landscapes

Population genetics and evolutionary game theory replace pure optimization with **replicator dynamics** and stochastic fixation in finite populations. A simple payoff-driven update can be written in continuous form as

$$
\dot x_i = x_i\bigl((Ax)_i - x^\top Ax\bigr),
$$

for strategy frequencies $$x$$ and payoff matrix $$A$$. Fitness landscapes, adaptive dynamics, and multilocus models connect to dynamical systems and probability. Genomic data add statistical inference: phylogenetics (trees as combinatorial objects with Markov substitution models), selection tests, and demographic history—each with likelihoods and model-misspecification hazards.

---

## 6. Biological networks as graphs—and their limits

Protein–protein interaction maps, gene regulatory networks, and connectomes are **graphs** (or hypergraphs, multiplex networks). Degree distributions, motifs, controllability heuristics, and community structure are graph-theoretic. Linking a hub node to “importance” without dynamics or causal experiments is a classic overclaim.

Network science tools transfer (see the network science lecture), but biological edges are noisy, incomplete, and context-dependent (tissue, time, post-translational state). The mathematical object is often a random graph model or a partially observed dynamical system—not a perfect wiring diagram of life.

---

## 7. Data, inference, and the “AI for biology” wave

Single-cell RNA-seq, cryo-EM, and protein structure prediction (e.g., deep learning models for folding) changed practice. Distinguish carefully:

| Layer | Content |
|-------|---------|
| Measurement model | Noise, bias, batch effects |
| Statistical estimator | What is identified from data? |
| Mechanistic model | ODE/PDE/stochastic kinetics |
| ML surrogate | Flexible fit; may lack mechanism |
| Biological claim | Causal or functional statement |

Structure prediction success is a major empirical and engineering achievement with deep mathematical ingredients (geometry of proteins, optimization, representation learning). It does not automatically yield full dynamical understanding of pathways, development, or ecosystems. Hype collapses these layers; literacy keeps them separate.

---

## 8. Frontiers (selected)

1. Multi-scale coupling (molecules → cells → tissues → organisms) with controllable error.
2. Identifiability and experimental design for nonlinear dynamical systems.
3. Stochastic spatial models and rigorous continuum limits.
4. Topological and geometric data analysis on biological shapes—promising tools, not magic.
5. Control of synthetic gene circuits with feedback and noise.
6. Integration of mechanistic models with modern ML under distribution shift.

### Worked micro-example: $$R_0$$ as linear algebra

In a simple SIR model with constant population normalized so the disease-free state has $$S=1$$, the infected equation near $$I=0$$ behaves like $$\dot I \approx (\beta-\gamma)I$$. Growth occurs when $$\beta>\gamma$$, i.e. $$R_0=\beta/\gamma>1$$. In multi-group models the same idea becomes a next-generation matrix: $$R_0$$ is a spectral radius. That is a precise mathematical object derived from a precise model—not a mystical “contagiousness number” floating free of assumptions about mixing, susceptibility, and recovery.

When public dashboards quote a single $$R_t$$, literacy asks: which generation interval, which reporting delay correction, which contact structure? The symbol migrated from linearization theory into operational epidemiology; both uses can be valid if labeled.

### Dimensional analysis habit

Before trusting a simulation, nondimensionalize. Logistic growth has a natural time $$1/r$$ and size $$K$$. Reaction–diffusion has diffusion lengths $$\sqrt{D/\text{rate}}$$. Nondimensional groups reveal whether a regime is reaction-limited or diffusion-limited and prevent unit mistakes that look like “new biology.”

---

## Common confusions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “The model is the biology.” | Fail | A model is a hypothesis with assumptions; validation is empirical. |
| “Turing patterns explain all morphogenesis.” | Overclaim | One mechanism among many; developmental biology is richer. |
| “Scale-free networks prove biological optimality.” | Weak | Degree statistics alone rarely prove evolutionary optimality. |
| “More equations mean more truth.” | False | Overparameterized models can fit noise; simpler models can predict better. |
| “AI solved biology.” | Hype | Important task successes ≠ complete theory of living systems. |
| “Stochastic models are only for when ODEs fail numerically.” | Incomplete | Discrete noise can change qualitative behavior (extinction, switching). |

---

## Exercises

1. **Logistic.** Solve or sketch $$N(t)$$ for logistic growth; interpret $$r$$ and $$K$$.
2. **SIR threshold.** Linearize SIR at $$(S,I,R)=(1,0,0)$$ (normalized) and relate invasion to $$R_0=\beta/\gamma$$ under standard scaling.
3. **Mass action.** For $$A+B \xrightarrow{k} C$$, write the ODE contribution to $$\dot a,\dot b,\dot c$$ under mass-action kinetics.
4. **Noise intuition.** If protein production occurs in rare bursts, why might the protein distribution be overdispersed relative to Poisson?
5. **Network caution.** Give an example where high degree does not imply functional importance.
6. **Literacy.** Read an abstract on protein structure prediction; list one measurement, one computational method, and one biological claim that still needs separate validation.
7. **Stretch.** Nondimensionalize logistic or SIR and identify dimensionless groups.

---


---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/mathematical-biology/analysis.md`.

### Status

**Broad applied field.** ODE/PDE population models are classical; stochastic chemical kinetics, spatial pattern formation, and data-driven inference remain active.

### Core statement / slogan

SIR-type compartment models: $$\dot S=-\beta SI$$, $$\dot I=\beta SI-\gamma I$$, $$\dot R=\gamma I$$. Threshold $$R_0=\beta/\gamma$$ governs invasion. Pattern formation via Turing instability is a classical PDE mechanism.

### Definitions to freeze

- **$$R_0$$.** Expected secondary cases from one infectious in a fully susceptible population.
- **Mass-action incidence.** Infection term $$\beta SI$$ in well-mixed ODEs.

### Hygiene (from confusions log)

- Treating ODE forecasts as exact predictions without parameter/structural uncertainty.
- Ignoring stochastic extinction in small populations.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/mathematical-biology/`.

**Recommended order**

1. **Orientation** — 3Blue1Brown — Epidemic modeling / differential equations (related DE series): [https://www.youtube.com/watch?v=Kas0tIxDvrg](https://www.youtube.com/watch?v=Kas0tIxDvrg).  
2. **Foundation** — 3Blue1Brown — Differential equations playlist entry points: [https://www.youtube.com/playlist?list=PLZHQObOWTQDDr3M1VmPZyiHkqHe7pf4Rs](https://www.youtube.com/playlist?list=PLZHQObOWTQDDr3M1VmPZyiHkqHe7pf4Rs).  
3. **Orientation** — Dr. Trefor Bazett — The MATH of Pandemics | Intro to the SIR Model: [https://www.youtube.com/watch?v=Qrp40ck3WpI](https://www.youtube.com/watch?v=Qrp40ck3WpI).  
4. **Orientation** — Numberphile — The Coronavirus Curve (SIR): [https://www.youtube.com/watch?v=k6nLfCbAzgo](https://www.youtube.com/watch?v=k6nLfCbAzgo).  

**Status reminder:** **Broad applied field.** ODE/PDE population models are classical; stochastic chemical kinetics, spatial pattern formation, and data-driven inference remain active.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/mathematical-biology/transcripts/` · status: `research/video-research/mathematical-biology/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/mathematical-biology_Kas0tIxDvrg_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References and further reading

1. J. D. Murray. *Mathematical Biology* — classic PDE/ODE patterns and populations.
2. L. Edelstein-Keshet. *Mathematical Models in Biology*.
3. M. Feinberg. Chemical reaction network theory expositions.
4. N. G. van Kampen. *Stochastic Processes in Physics and Chemistry* (master equations).
5. Turing (1952). The chemical basis of morphogenesis.
6. Course links: [Network science]({{ site.baseurl }}/contents/en/chapter06/06_05_Network_Science/), [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [Optimal transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) (for distribution comparison in data).

---


Full URL bibliography from video research: `research/video-research/mathematical-biology/references.md`.

### Videos (recommended path)

- 3Blue1Brown — Epidemic modeling / differential equations (related DE series) (ORIENTATION): https://www.youtube.com/watch?v=Kas0tIxDvrg
- 3Blue1Brown — Differential equations playlist entry points (FOUNDATION): https://www.youtube.com/playlist?list=PLZHQObOWTQDDr3M1VmPZyiHkqHe7pf4Rs
- Dr. Trefor Bazett — The MATH of Pandemics | Intro to the SIR Model (ORIENTATION): https://www.youtube.com/watch?v=Qrp40ck3WpI

### Papers and web (from research pack)

- Wikipedia — Mathematical biology: https://en.wikipedia.org/wiki/Mathematical_and_theoretical_biology
- Wikipedia — Compartmental models in epidemiology: https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology
- Murray — Mathematical Biology (standard textbook reference): https://en.wikipedia.org/wiki/James_D._Murray
- Wikipedia — Reaction–diffusion system / Turing pattern: https://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system
- Wikipedia — Lotka–Volterra equations: https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations
- Wikipedia — Chemical master equation: https://en.wikipedia.org/wiki/Chemical_master_equation

### Course

- Research pack: `research/video-research/mathematical-biology/` (especially `references.md`, `learning_path.md`).

## Further directions

- **Graphs in vivo:** [Network science]({{ site.baseurl }}/contents/en/chapter06/06_05_Network_Science/) for random-graph models and epidemics on networks.
- **Learning from data:** [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/) when biological claims are statistical.
- **Practice:** simulate SIR and a simple birth–death gene circuit; compare ODE mean to stochastic trajectories.
- **Reading path:** one compartment model chapter + one stochastic gene expression paper + one critical essay on model limits.
- Ask always: *At which scale is this equation valid?*
