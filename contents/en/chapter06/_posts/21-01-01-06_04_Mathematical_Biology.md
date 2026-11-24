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

In 1952, already famous for laying the foundations of computer science and helping crack Enigma, Alan Turing published a paper that had nothing to do with computers. He asked why leopards have spots, zebras have stripes, and a uniform sphere of embryonic cells spontaneously breaks symmetry into a living body. He wrote down two deceptively simple reaction–diffusion equations—and watched biological patterns emerge from mathematical instability.

Biology has long been known as a noisy, multi-scale, exception-filled world, the opposite of physics’ clean symmetries. Yet every quantitative claim in biology—when an epidemic will peak, how a gene bursts on and off inside a single cell, or whether predator and prey coexist—ultimately becomes mathematics: rates of change, equilibria, spatial geometry, stochastic processes, and inference from noisy data. **Mathematical biology** is not a single theorem; it is the craft of matching the right mathematical language to the right biological scale.

The hardest virtue here is **honesty about scales**: a clean ODE may describe a well-stirred flask accurately yet fail in solid tissue, while a genome-scale interaction graph can look impressive structurally yet leave dynamics completely underdetermined. This lecture surveys the core modeling families and sharpens your eye for “AI has solved biology” hype.

---

## Background Knowledge Map: What Is Mathematical Biology and What Does It Study?

Whereas classical physics often searches for one universal equation valid everywhere, **Mathematical Biology** works like a cartographer’s workshop producing maps at different resolutions. Depending on the biological scale, the mathematics shifts completely:

1. **Populations & Epidemics (Ordinary Differential Equations — ODEs):** Ignoring individual spatial locations, we track total counts or fractions over time: logistic growth, Lotka–Volterra predator–prey cycles, and compartmental SIR epidemic models.
2. **Tissues & Morphogenesis (Partial Differential Equations — PDEs):** When space matters—cells migrating, chemicals diffusing across an embryo—reaction–diffusion PDEs capture traveling waves and Turing pattern formation.
3. **Inside Single Cells (Stochastic Processes — Markov Chains & Master Equations):** When a cell contains only a handful of mRNA molecules, “continuous concentration” breaks down; each reaction is a random jump governed by the chemical master equation.
4. **Evolution & Systems (Game Theory & Graphs):** Natural selection is not static optimization—the fitness of a strategy depends on *what everyone else is playing* (replicator dynamics), while gene and protein networks form intricate feedback graphs.

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

### Short video: SIR epidemics for three values of R₀

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/sir-r0-epidemic_en.mp4"></video>
</div>

The same SIR model with $$R_0 = 0.8, 1.5, 3$$, starting with 3% infected. Below 1 the outbreak fades; above 1 it grows to a peak, and a larger $$R_0$$ gives a higher, earlier peak and more people infected in total.


### Try it yourself: Change R₀ and watch the epidemic

<div class="mex-explainer" data-mex="sir" data-lang="en"></div>


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

### Deep-Dive Explanation: Computing the SIR Epidemic Peak and Herd Immunity by Hand (Read Slowly)

People often assume the nonlinear SIR system can only be understood through computer simulation. In fact, one clever division from first-year calculus lets you calculate the **exact height of the epidemic peak** without ever solving for $$I(t)$$ as a function of time!

1. **Find an exact conserved quantity (first integral):** Divide $$\dot I = \beta SI - \gamma I$$ by $$\dot S = -\beta SI$$ to eliminate time $$t$$:

   $$
   \frac{dI}{dS} = \frac{\beta SI - \gamma I}{-\beta SI} = -1 + \frac{\gamma}{\beta S} = -1 + \frac{1}{R_0 S}, \qquad \text{where } R_0 = \frac{\beta}{\gamma}.
   $$

   Integrating both sides with respect to $$S$$ gives a quantity that stays constant along the entire epidemic trajectory:

   $$
   I(t) + S(t) - \frac{1}{R_0}\ln S(t) \;=\; I_0 + S_0 - \frac{1}{R_0}\ln S_0.
   $$

2. **Plug in concrete numbers (matching the video above):** Take $$R_0 = 3$$, starting with $$3\%$$ infected and $$97\%$$ susceptible ($$S_0 = 0.97,\ I_0 = 0.03,\ S_0 + I_0 = 1$$).
   - **When does the peak occur?** Exactly when $$\dot I = 0 \Leftrightarrow \beta SI = \gamma I \Leftrightarrow S_{\text{peak}} = \frac{1}{R_0} = \frac{1}{3} \approx 0.333$$.
   - **How high is the peak?** Substitute $$S_{\text{peak}} = \frac{1}{3}$$ into the conserved quantity:
     $$
     I_{\text{peak}} = (S_0 + I_0) - S_{\text{peak}} + \frac{1}{R_0}\ln\Bigl(\frac{S_{\text{peak}}}{S_0}\Bigr)
     = 1 - \frac{1}{3} + \frac{1}{3}\ln\Bigl(\frac{1/3}{0.97}\Bigr)
     \approx 0.667 + \frac{1}{3}(-1.068) \approx 0.311.
     $$
     More than **31% of the entire population is infected at the exact same moment**—explaining immediately why healthcare systems strain when $$R_0 = 3$$!

3. **Herd immunity threshold:** To prevent an outbreak from growing at $$t=0$$, we need $$\dot I(0) \le 0 \Leftrightarrow S_0 \le \frac{1}{R_0}$$. For $$R_0 = 3$$, the minimum vaccinated fraction is

   $$
   p_c = 1 - \frac{1}{R_0} = 1 - \frac{1}{3} = \frac{2}{3} \approx 66.7\%.
   $$

Every number above is an exact theorem *inside the well-mixed SIR model*. In real life, the decisive scientific question is never whether the integral was done right—it is how far real contact networks and changing behavior depart from the well-mixed assumption.

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

## Video tham khảo

- **xem trước** — [Exponential growth and epidemics](https://www.youtube.com/watch?v=Kas0tIxDvrg) — 3Blue1Brown, English. Watch first. “Exponential growth and epidemics” orients the lesson’s aim: Write and interpret a simple compartment ODE (e.g., logistic growth or SIR) and explain what “well-mixed” assumes.
- [The MATH of Pandemics | Intro to the SIR Model](https://www.youtube.com/watch?v=Qrp40ck3WpI) — Dr. Trefor Bazett, English. A second pass once the main claim is in view: Write and interpret a simple compartment ODE (e.g., logistic growth or SIR) and explain what “well-mixed” assumes.
- [The Coronavirus Curve - Numberphile](https://www.youtube.com/watch?v=k6nLfCbAzgo) — Numberphile, English. Further depth after the first two, still tied to this lesson: Write and interpret a simple compartment ODE (e.g., logistic growth or SIR) and explain what “well-mixed” assumes.
