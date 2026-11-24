---
layout: post
title: "Pearl and the Mathematics of Causality (Turing 2011)"
chapter: '09'
order: 11
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

Try confronting a paradox that once baffled both doctors and statisticians (**Simpson's Paradox**): a hospital aggregates kidney-stone treatment records and discovers that Treatment A has a higher recovery rate than Treatment B for **both** small-stone patients and large-stone patients. Yet when all 700 charts are pooled into a single table, Treatment B suddenly beats Treatment A! Looking purely at the numbers, which treatment should you choose? Astonishingly, the answer *does not live inside the data table*—it depends on the **causal story** behind the data (doctors tended to assign the stronger open surgery to harder, large-stone cases).

For a full century, classical statistics treated the word "cause" as near-taboo, repeating the mantra *"correlation is not causation."* **Judea Pearl** (winner of the **2011 A.M. Turing Award**) broke that silence by giving causality a **complete mathematical language** of directed acyclic graphs (DAGs), the intervention operator $$do(x)$$, and **do-calculus**. The medal is not for a faster sorting routine—it is for making causation a formal object that supports algorithms across AI, epidemiology, and policy. Official materials: [amturing.acm.org](https://amturing.acm.org/). Cross-links: [probability & data science]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/), [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).

---

## Learning objectives

After this lecture you should be able to distinguish association (conditioning) from intervention (the $$do$$ operator) in slogan form; explain a causal Bayesian network as a directed acyclic graph (DAG) plus local conditional distributions; state what a confounder is and why “control for everything” is not always right; describe do-calculus as a symbolic calculus for reducing interventional queries to observational expressions when the graph permits; and critique a media causal claim with a graph-shaped objection.

**Prerequisites / cross-links.** Basic probability: conditional probability $$\mathbb{P}(A\mid B)$$, chain rule, independence. Graphs as directed edges. No measure-theoretic probability required. Chapter hub: [Turing overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/).

---

## Background Knowledge Map: What Are Causal Inference and Probabilistic Graphical Models?

Most data-science and machine-learning graduates are comfortable estimating conditional probabilities $$p(y \mid x)$$—for instance, *"given that a shopper bought diapers, what is the probability they buy beer?"* Yet the moment you step into decision-making—*"if we actively cut the price of drug $$X$$, how will recovery rate $$Y$$ change?"*—observational probability $$p(y \mid x)$$ breaks down, because **seeing $$X=x$$** (passive observation) is fundamentally different from **forcing $$X=x$$** (active intervention)!

That is the arena of **Causal Inference** and **Probabilistic Graphical Models**, resting on three pillars:
1. **Directed Acyclic Graphs (DAGs) as Mechanism Maps:** instead of treating every column in a flat table symmetrically, we draw arrows $$A \to B$$ to assert that $$A$$ is a direct cause of $$B$$. A DAG factors a massive joint distribution into local conditionals and lets us read off conditional independencies via **d-separation**.
2. **The $$do(x)$$ Operator and Do-Calculus:** intervening via $$do(X=x)$$ performs "graph surgery": **sever every incoming arrow into $$X$$** (since we now set $$X$$ ourselves rather than letting confounders choose it) and compute the new distribution of $$Y$$. Pearl's **do-calculus** gives exactly three algebraic rewrite rules answering when $$p(y \mid do(x))$$ can be computed purely from observational data without running an expensive randomized controlled trial (RCT).
3. **Structural Causal Models (SCMs) and Counterfactuals:** at the deepest layer, each variable obeys a structural equation $$X_i := f_i(\mathrm{Pa}_i, U_i)$$ with background noise $$U_i$$. Holding a specific individual's noise $$U_i$$ fixed while altering the equation for $$X$$ defines **counterfactuals** (*"what would have happened to this patient had they skipped the drug?"*)—the mathematical bedrock of personalized medicine and algorithmic fairness.

---

## 1. Seeing is not doing

### Association

Observational data give joint distributions. From a large table of variables $$(X,Y,Z,\ldots)$$ one can estimate conditionals such as $$\mathbb{P}(Y\mid X=x)$$. That answers: **among units that have $$X=x$$, what is the distribution of $$Y$$?** It does not automatically answer: **if we set $$X$$ to $$x$$ by intervention, what happens to $$Y$$?**

### Intervention

Pearl’s notation $$P(Y\mid do(X=x))$$ denotes the distribution of $$Y$$ after an intervention that forces $$X$$ to $$x$$, ideally breaking incoming causal influences to $$X$$ (the “graph surgery” picture: remove edges into $$X$$, then set $$X=x$$). Randomized controlled trials are the classical empirical realization of interventions; causal graphs aim to state when observational data, plus assumptions, identify the same quantities.

### Why the distinction is mathematical, not pedantic

Many policy and product questions are interventional: what if we change a price, a drug dose, a ranking algorithm, a recommendation? Predictive machine learning often optimizes $$\mathbb{P}(Y\mid X)$$ under a static distribution. When deployment *changes* the world, association can fail. Causal literacy is part of responsible AI mathematics—not a replacement for experiments, but a language for assumptions.

---

## 2. Bayesian networks: factoring uncertainty on a graph

A **Bayesian network** on a DAG $$G$$ with nodes $$V_1,\ldots,V_n$$ represents a joint distribution by local conditionals:

$$
\mathbb{P}(v_1,\ldots,v_n) = \prod_{i=1}^n \mathbb{P}\bigl(v_i \mid \mathrm{pa}(v_i)\bigr),
$$

where $$\mathrm{pa}(v_i)$$ are the parents of $$v_i$$ in $$G$$. Missing edges encode conditional independencies (Markov properties). Exact and approximate inference algorithms (variable elimination, belief propagation, MCMC, …) compute marginals and conditionals on this factored representation.

Pearl’s earlier work on Bayesian networks transformed AI’s handling of uncertainty: from brittle logic-only systems toward coherent probabilistic reasoning with structure. The Turing citation includes this probabilistic graph culture *and* the later causal layer built on related graphical ideas.

**Literacy.** The DAG is an assumption about factorization and independence—not a proof that the world is acyclic. Model criticism remains part of the science.

---

## 3. Causal graphs and confounders

### Directed edges as causal mechanisms (modeling choice)

In a **causal** DAG interpretation, an arrow $$X\to Y$$ asserts a direct mechanism: intervening on $$X$$ can change $$Y$$ along pathways the graph represents, subject to the model’s semantics. Paths carry distinct meanings:

- **Chains** $$X\to Z\to Y$$: mediation.  
- **Forks** $$X\leftarrow Z\to Y$$: common causes (**confounders**).  
- **Colliders** $$X\to Z\leftarrow Y$$: common effects; conditioning on colliders can *create* associations (selection bias).

### Confounding slogan

If $$Z$$ influences both treatment $$X$$ and outcome $$Y$$, the observational association between $$X$$ and $$Y$$ mixes the causal effect with the spurious path through $$Z$$. Adjusting for $$Z$$ (when appropriate) blocks the fork. Adjusting for a collider can open a biasing path. Hence the key rule:

> “Control for all variables” is not a theorem; **which** variables you condition on depends on the causal graph.

### Worked Example (Step by Step): Dissecting Simpson's Paradox on 700 Kidney-Stone Patients

Check the famous kidney-stone dataset (Charig et al., 1986) on **700 patients**—350 given **Treatment A** (open surgery) and 350 given **Treatment B** (percutaneous nephrolithotomy). Stone size $$Z$$ ($$Z=0$$: small, $$Z=1$$: large) is a **confounder** affecting both the doctor's choice $$X$$ and recovery $$Y$$ (graph: $$Z \to X$$, $$Z \to Y$$, $$X \to Y$$):

| Subgroup by Stone Size ($$Z$$) | Treatment A ($$X=A$$) | Treatment B ($$X=B$$) | Subgroup Winner |
|---|---|---|---|
| Small stones ($$Z=0$$, $$357$$ total) | $$81 / 87 = 93.1\%$$ | $$234 / 270 = 86.7\%$$ | **A wins** ($$+6.4\%$$) |
| Large stones ($$Z=1$$, $$343$$ total) | $$192 / 263 = 73.0\%$$ | $$55 / 80 = 68.8\%$$ | **A wins** ($$+4.2\%$$) |
| **Pooled raw rate (observational $$p(Y=1 \vert X)$$)** | **$$273 / 350 = 78.0\%$$** | **$$289 / 350 = 82.6\%$$** | **B wins** ($$+4.6\%$$)! |

Why does pooling reverse the winner? Look at the denominators: doctors assigned Treatment A to $$263/350 = 75.1\%$$ **large-stone** (harder) cases, while Treatment B got $$270/350 = 77.1\%$$ **small-stone** (easier) cases!

Now apply Pearl's **back-door adjustment formula** $$p(Y=1\mid do(x)) = \sum_z p(Y=1\mid x,z)\,p(z)$$ using the true population proportions of stone sizes:

$$
p(Z=0) = \frac{87 + 270}{700} = \frac{357}{700} = 51.0\%, \qquad p(Z=1) = \frac{263 + 80}{700} = \frac{343}{700} = 49.0\%.
$$

Weighting by population $$p(Z)$$ instead of the biased assignment $$p(Z\mid X)$$:

$$
p(Y=1 \mid do(X=A)) = 0.51 \times 0.931 + 0.49 \times 0.730 \approx 0.4748 + 0.3577 = \mathbf{83.25\%},
$$

$$
p(Y=1 \mid do(X=B)) = 0.51 \times 0.867 + 0.49 \times 0.688 \approx 0.4422 + 0.3371 = \mathbf{77.93\%}.
$$

The reversal vanishes: **Treatment A genuinely beats Treatment B by $$+5.32$$ percentage points** ($$83.25\%$$ vs. $$77.93\%$$)!

And in two lines, here is **Rung 3 (Counterfactual)** on a linear SCM $$Y := 2X + U_Y$$ (study hours $$X$$, exam score $$Y$$, student aptitude $$U_Y$$): observing $$X'=1$$ and $$Y'=7$$ fixes $$U_Y = 7 - 2(1) = 5$$ (*abduction*), so *"had this exact student studied $$X=3$$ hours, their score would have been $$Y_{X=3} = 2(3) + 5 = 11$$."*

### Deep-Dive Explanation: Why Intervention Is "Graph Surgery" (Read Slowly)

1. **Separate *seeing* from *doing*:** computing $$p(Y=1 \mid X=A)$$ filters for patients whom doctors *naturally chose* for A—which leaks information backward up $$Z \to X$$ that they mostly had large stones ($$75.1\%$$).
2. **Sever all incoming arrows to $$X$$:** performing $$do(X=A)$$ (assigning A to a random patient) **deletes** the arrow $$Z \to X$$ from the graph. Stone size $$Z$$ no longer influences treatment, so $$Z$$'s distribution snaps back to the population mix $$p(Z) = (51\%, 49\%)$$.
3. **Keep every other mechanism intact:** the biological response $$p(Y=1 \mid X, Z)$$ (arrows $$X \to Y$$ and $$Z \to Y$$) stays unchanged, so averaging stratum rates against $$p(Z)$$ recovers the exact causal effect.
4. **Watch out when the causal story changes:** if $$Z$$ were *not* pre-treatment stone size, but **post-treatment blood pressure** (a mediator $$X \to Z \to Y$$), there is *no* back-door path into $$X$$—adjusting for $$Z$$ would **block the drug's own effect**! The exact same 700-row table yields opposite medical advice under two different causal graphs.

**Quick check.** If a city's population shifted to $$p(Z=0)=80\%$$ small stones and $$p(Z=1)=20\%$$ large stones, what would $$p(Y=1 \mid do(X=A))$$ become? $$0.8 \times 93.1\% + 0.2 \times 73.0\% = 74.48\% + 14.60\% = \mathbf{89.08\%}$$—the causal population rate tracks $$p(Z)$$ even while the biological stratum rates stay fixed.

### Identification

**Causal identification** asks whether $$P(Y\mid do(X=x))$$ is a functional of the observational distribution given the graph. Sometimes yes (back-door adjustment, front-door criterion, …); sometimes no, without experiments or extra assumptions. Graphs make non-identifiability visible.

---

## 4. Do-calculus (slogan level)

Pearl’s **do-calculus** is a set of inference rules for expressions involving $$do(\cdot)$$ and ordinary conditioning, justified by graphical criteria (properties of d-separation in surgically modified graphs). In practice, textbooks show how repeated rule applications can eliminate $$do$$ operators and leave estimable observational quantities.

For this course you need not memorize the three rules’ formal statements. You need the meta-theorem:

> Under an assumed causal DAG, some interventional queries reduce algorithmically to observational statistics; others are marked impossible without more data or assumptions.

That is mathematics of causality: **syntax and rewrite rules** for causal expressions, not only verbal philosophy.

---

## 5. Correlation, regression, and ML—where they fit

Linear regression coefficients are not automatically causal effects. A coefficient in $$Y=\beta X+\gamma Z+\varepsilon$$ estimates a causal parameter only under assumptions (no unmeasured confounding for the target contrast, correct functional form, etc.). Machine learning predictors minimize predictive risk; they can be ingredients in causal estimators (nuisance functions in double machine learning, propensity models) but **prediction ≠ causation**.

Connections to course chapters:

- [Probability & data science]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/): conditionals, Bayes, estimation.  
- [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/): generalization under i.i.d. draws—often the *observational* regime.  
- [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/): systems that act in the world need causal caution when they intervene (recommend, moderate, diagnose).

**Counterfactuals** (what would have happened to *this* unit under another treatment?) sit at a higher layer of Pearl’s hierarchy: association < intervention < counterfactuals.

---

## 6. Causality and the Turing-scale AI story

Pearl has argued publicly that progress toward human-like reasoning requires causal models, not only curve fitting. Agree or disagree on timelines; the mathematical contribution stands independently: graphs + interventions + algorithms for identification and inference. Competing and complementary frameworks exist (potential outcomes / Rubin causal model; structural equation models; invariant risk minimization research in ML). Good scholarship names frameworks and assumptions rather than brand loyalty.

For Math Enthusiast, Pearl’s Turing Award is a bridge from discrete graphs and probability to **scientific epistemology with teeth**.

### A miniature worked distinction

Suppose ice-cream sales $$X$$ and drowning incidents $$Y$$ rise together across days. A fork through temperature $$Z$$ explains the association: heat drives swimming and ice cream. Then $$\mathbb{P}(Y\mid X)$$ can look strong while $$P(Y\mid do(X))$$ is essentially unchanged—banning ice cream does not save swimmers. A regression of $$Y$$ on $$X$$ without $$Z$$ reports association; a causal claim needs a design or a graph-justified adjustment (here, account for $$Z$$, or better, intervene). The example is cartoonish on purpose: it forces the notation split that media prose erases.

### Pearl’s ladder (association / intervention / counterfactual)

Pearl often describes a hierarchy: (1) association—what is? (2) intervention—what if we do? (3) counterfactuals—what if we had done otherwise, for a unit that already experienced an outcome? Machine learning products mostly live on rung (1). Policy, medicine, and accountability questions often need rung (2). Legal and moral “but-for” reasoning pushes toward rung (3), which requires stronger assumptions. When a demo claims a model “understands causes,” ask which rung has evidence.

### Compatibility with potential outcomes

Statisticians often write potential outcomes $$Y(1),Y(0)$$ for treatment and control. Pearl’s graphs and the potential-outcomes framework are largely **translatable** when assumptions are stated carefully; tribal debates sometimes obscure that both are languages for the same scientific need. For this course, fluency means: never confuse a predictive conditional with an interventional contrast, whatever notation a paper prefers.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “Correlation never implies causation, end of story.” | Correlation does not *suffice*; with design/assumptions/graphs, causal effects can be identified. Absolute slogan is incomplete. |
| “$$P(Y\mid X)$$ is the causal effect of $$X$$ on $$Y$$.” | That is association; causal effect uses $$do(X)$$ (or potential outcomes notation). |
| “Conditioning on more variables always reduces bias.” | Collider bias and overadjustment can hurt; graph criteria matter. |
| “Bayesian networks are automatically causal.” | Factorization DAGs need a causal interpretation and assumptions to support interventions. |
| “Do-calculus replaces randomized trials.” | Trials implement interventions; do-calculus organizes when observation + assumptions identify effects. |
| “Causal inference is only for social science.” | Medicine, genetics, advertising, and AI systems all face interventional questions. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/pearl-causality/`.

**From the research pack (must-know slogans)**

- Pearl Turing 2011: probabilistic and causal reasoning — Bayesian networks, do-calculus.
- Correlation ≠ causation; formal language for interventions and counterfactuals.
- Impact on AI, statistics, epidemiology, social science methodology.

**Recommended order**

1. **Orientation** — YouTube search: Pearl causality Turing: [https://www.youtube.com/watch?v=iNm4nFBFmvo](https://www.youtube.com/watch?v=iNm4nFBFmvo).  

**Official / primary written hubs**

- Pearl Turing page: https://amturing.acm.org/award_winners/pearl_2658896.cfm  

Complete URL bibliography: `research/video-research/pearl-causality/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/pearl-causality/transcripts/` · status: `research/video-research/pearl-causality/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/pearl-causality_iNm4nFBFmvo_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/pearl-causality/references.md`.

1. Pearl Turing page — https://amturing.acm.org/award_winners/pearl_2658896.cfm  
2. Wikipedia — Judea Pearl — https://en.wikipedia.org/wiki/Judea_Pearl  
3. Wikipedia — Causal model — https://en.wikipedia.org/wiki/Causal_model  
4. Wikipedia — Bayesian network — https://en.wikipedia.org/wiki/Bayesian_network  
5. Wikipedia — Do-calculus — https://en.wikipedia.org/wiki/Do_calculus  
6. Book of Why (popular entry) — https://en.wikipedia.org/wiki/The_Book_of_Why  
7. UCLA Cognitive Systems Lab (Pearl) — http://bayes.cs.ucla.edu/jp_home.html  
8. YouTube search: Pearl causality Turing — https://www.youtube.com/watch?v=iNm4nFBFmvo  
9. Research pack folder: `research/video-research/pearl-causality/`.

1. ACM Turing Award — Judea Pearl — [amturing.acm.org](https://amturing.acm.org/).  
2. J. Pearl, *Causality* (Cambridge); Pearl–Glymour–Jewell, *Causal Inference in Statistics: A Primer*.  
3. Spirtes–Glymour–Scheines; modern surveys on causal graphical models; potential-outcomes texts for a parallel language.  
4. Course: [probability]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/); [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/); [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).

---

## Further directions

- Work a tiny three-variable example with numbers: association vs intervention under a known SEM.  
- Read one explainer on front-door vs back-door criteria.  
- Compare Pearl graphs with potential-outcomes notation on the same toy experiment.  
- Compare an A/B test writeup against an observational “AI discovered that…” claim.  
- Next: [Bengio, Hinton, LeCun]({{ site.baseurl }}/contents/en/chapter09/09_12_Deep_Learning_Trio/)—learning systems at scale, still needing causal humility when they act.

## Video tham khảo

- **xem trước** — [Judea Pearl, 2012 ACM A.M. Turing Award Lecture "The Mechanization of Causal Inference"](https://www.youtube.com/watch?v=iNm4nFBFmvo) — Association for Computing Machinery (ACM), English. Watch first. “Judea Pearl, 2012 ACM A.M. Turing Award Lecture "The Mechanization of Causal Inference"” orients the lesson’s aim: After this lecture you should be able to distinguish association (conditioning) from intervention (the do operator) in slogan form; explain a causal Bayesian network as a directed…
