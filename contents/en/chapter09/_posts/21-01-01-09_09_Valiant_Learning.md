---
layout: post
title: "Valiant and Computational Learning Theory (Turing 2010)"
chapter: '09'
order: 9
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

**Leslie Valiant** received the **A.M. Turing Award 2010** for transformative contributions to the theory of computation, notably **PAC learning**—*probably approximately correct* learning—and for foundational work on computational complexity including **counting complexity** (the class **#P**) and later themes such as **holographic algorithms**. The award is a reminder that “machine learning” did not begin as a pile of benchmarks; it began, in part, as a *mathematical question*: when is learning from examples a computationally and statistically well-posed problem?

This lecture develops PAC learning as a definition that made learning theory a science; states sample-complexity slogans that every seminar student should own; sketches why **counting** is harder than deciding in Valiant’s #P world; mentions holographic algorithms only as a light frontier pointer; and links explicitly to [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/) and [mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/). Official materials: [amturing.acm.org](https://amturing.acm.org/).

---

## Learning objectives

After this lecture you should be able to explain the PAC learning slogan—return a hypothesis that is *approximately* correct *with high probability* after seeing finitely many samples—and write true risk versus empirical risk at the level of Chapter 6; state a sample-complexity slogan of the form “order $$(1/\varepsilon)\log(1/\delta)$$ times a complexity measure” without claiming a single universal formula for deep nets; define **#P** as counting accepting witnesses rather than deciding existence; relate Valiant’s learning framework to modern ML theory without equating PAC with “how GPT trains”; and critique one popular overstatement about learnability (LO6).

**Prerequisites / seminar links.** Probability at the level of expectation and “with probability at least $$1-\delta$$”; algorithms literacy. Strongly recommended twins: [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/), [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/). Chapter hub: [Turing overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/).

---

## 1. Learning needed a theorem-shaped question

Before a definition, “learning” is a word that means everything and therefore nothing: children learn language; gradient descent fits parameters; scientists learn laws. Valiant’s 1984 PAC framework asked a precise question roughly of the form:

> Is there an algorithm that, given access to random examples labeled by an unknown target concept from a class $$\mathcal{C}$$, outputs with probability at least $$1-\delta$$ a hypothesis whose error under the same distribution is at most $$\varepsilon$$, using time and samples polynomial in the relevant parameters (size, $$1/\varepsilon$$, $$1/\delta$$, …)?

The power is in the **quantifiers**: for every target in the class, for every distribution on instances (distribution-free in the classical PAC setting), success is only *probable* and only *approximate*. That is not a weakness of the definition; it is fidelity to statistics. Perfect recovery from finite samples is generally impossible; exact identification of an arbitrary function is hopeless.

PAC turned learning into something you can *prove theorems about*: which concept classes are efficiently learnable, which require exponential samples, which become hard under cryptographic assumptions, and how complexity of the hypothesis class governs sample size.

---

## 2. True risk, empirical risk, and the protocol

Let instances $$x$$ be drawn from a distribution $$\mathcal{D}$$ on a domain $$X$$, and let a target concept $$c$$ label examples (or more generally a joint distribution on $$(x,y)$$). A hypothesis $$h$$ has **true error** (true risk for 0–1 loss)

$$
\mathrm{err}_{\mathcal{D}}(h) := \mathbb{P}_{x\sim\mathcal{D}}\bigl(h(x)\neq c(x)\bigr)
$$

in the realizable Boolean setting (analogous definitions hold for real-valued losses in statistical learning). Given a sample $$S$$ of size $$m$$, **empirical error** is the fraction of mistakes on $$S$$.

**PAC success** means: with probability at least $$1-\delta$$ over the draw of $$S$$, the algorithm outputs $$h$$ with $$\mathrm{err}_{\mathcal{D}}(h)\le\varepsilon$$ (realizable case), or within $$\varepsilon$$ of the best hypothesis in a class (agnostic variants). The algorithm may be improper (output outside the original concept class) or proper; efficiency constraints turn statistical questions into computational ones.

This is the same skeleton as modern [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/), which enriches PAC with VC dimension, Rademacher complexity, margins, PAC-Bayes, and algorithm-dependent analyses for deep nets.

---

## 3. Sample complexity slogans (what to remember)

For many finite hypothesis classes $$\mathcal{H}$$ of size $$\lvert\mathcal{H}\rvert$$, uniform convergence and union bounds yield sample sizes on the order of

$$
m = O\Bigl(\frac{1}{\varepsilon}\log\frac{\lvert\mathcal{H}\rvert}{\delta}\Bigr)
$$

in simple realizable settings (constants and exact forms depend on the textbook theorem). For infinite classes, **VC dimension** $$d=\mathrm{VCdim}(\mathcal{H})$$ replaces $$\log\lvert\mathcal{H}\rvert$$ with terms like $$d\log(1/\varepsilon)$$, schematically

$$
m = O\Bigl(\frac{d}{\varepsilon}\log\frac{1}{\varepsilon}+\frac{1}{\varepsilon}\log\frac{1}{\delta}\Bigr)
$$

for realizable PAC (again: schematic literacy, not a claim about neural nets’ tight constants).

**What the slogans teach**

- Accuracy $$\varepsilon$$ and confidence $$\delta$$ enter as $$1/\varepsilon$$ and $$\log(1/\delta)$$ scale factors—better confidence is cheap; better accuracy costs samples.  
- Model complexity (log of class size, VC dimension, …) multiplies the sample need.  
- Distribution-free guarantees are deliberately pessimistic: they hold for every $$\mathcal{D}$$, so they can be loose for structured data.

**What the slogans do *not* teach**

- They do not say deep networks are PAC-learned by SGD with these bounds.  
- Vacuous numerical bounds (greater than 1) can be *true theorems* and still useless as certificates for a given architecture.  
- Optimization computational cost is a separate axis from sample complexity.

Seminar discipline: when a blog says “learning theory is obsolete,” ask which theorem was tested against which model class.

---

## 4. Computational learning: not only samples, but time

PAC includes **efficient** learnability: polynomial time in the size parameters, $$1/\varepsilon$$, $$1/\delta$$. Some classes are statistically learnable but believed computationally hard (connections to cryptography: if you could learn certain functions efficiently, you could break pseudorandom objects). Valiant’s framework thus sits at the junction of **statistics and complexity**, not in a pure statistics silo.

Representation matters: decision trees, DNF formulas, finite automata, neural nets of bounded size—each class has a literature of positive algorithms and hardness results. The course does not require memorizing the catalog; it requires recognizing the *shape* of a learnability theorem.

---

## 5. Counting complexity: #P

Valiant also transformed **counting**. The class **#P** consists of functions that count the number of accepting witnesses of a polynomial-time nondeterministic machine—equivalently, count solutions to NP search problems. Example: given a Boolean formula, output the number of satisfying assignments (**#SAT**), not merely whether one exists.

**Moral.** Counting can be harder than deciding in a precise sense: Toda’s theorem and related results place the power of #P very high in the polynomial hierarchy landscape. Even for problems whose decision version is in **P**, counting versions may be #P-complete (classic examples include counting perfect matchings in bipartite graphs—related to the permanent).

For this course’s complexity map ([Ch.6]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/)), #P is the postcard: **verification of a count is different from existence**, and approximate counting / sampling became major algorithmic theories of their own.

---

## 6. Holographic algorithms (light)

Valiant’s **holographic algorithms** are a surprising positive algorithmic theme: certain counting problems that look #P-hard admit polynomial-time algorithms via linear-algebraic “holographic” reductions and matchgate signatures—an exotic island of tractability. Treat this as a *light* pointer for curiosity, not a technical requirement of the seminar. The LO message is cultural: complexity theory is not only bad news; it also discovers unexpected algorithms when the right algebraic structure appears.

---

## 7. Bridge to modern machine learning

Deep learning practice optimizes nonconvex losses over enormous parameter spaces; data are not adversarial worst-case distributions; foundation models transfer across tasks. Classical PAC does not “explain GPT” as a theorem. It still contributes:

- the vocabulary of generalization gaps and hypothesis classes;  
- the insistence on probabilistic guarantees;  
- hardness results that police impossible claims;  
- a research lineage into modern learning theory, online learning, and computational statistics.

[Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/) stresses optimization and representation; this Valiant lecture stresses **definitions that made learning mathematical**. Both are needed for LO6 literacy: hype collapses when definitions appear.

Valiant’s later popular writing on “ecorhythms” and biologically flavored computation is optional context; the Turing core for this course remains PAC + complexity.

---

## 8. Confusions

| Claim | Correction |
|-------|------------|
| “PAC means the hypothesis is probably exactly correct.” | Approximate ($$\varepsilon$$) and probable ($$1-\delta$$)—both quantifiers matter. |
| “PAC learning is how neural nets are trained.” | PAC is a theoretical framework; training is typically SGD on empirical risk with engineering choices. |
| “Finite VC dimension guarantees practical deep learning bounds.” | It yields distribution-free schema; applied to huge nets, bounds may be vacuous. |
| “#P is another name for NP.” | #P counts solutions; NP is about existence/decision (and related search). |
| “If a class is PAC-learnable, learning is easy in practice.” | Efficiency, noise models, model misspecification, and optimization still matter. |
| “Valiant only did learning.” | Counting complexity and other TCS contributions are co-equal pillars of the Turing case. |

---

## Exercises

1. State PAC learning in one carefully quantified sentence.  
2. Write formulas for true error and empirical error for 0–1 loss.  
3. Why does $$\log(1/\delta)$$ appear in sample bounds (union bound / concentration intuition)?  
4. Give one reason a computationally efficient PAC algorithm might not exist even if samples suffice statistically.  
5. What does #SAT ask for, and how does it differ from SAT?  
6. **≤200 words:** Connect Valiant’s PAC to one section of [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/).  
7. **LO6:** Rewrite a vague headline “AI has solved learning theory” into a precise claim or a clear non-claim.  
8. Optional: look up one holographic algorithm slogan and write two sentences on why unexpected tractability matters culturally in TCS.

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/valiant-learning/`.

**From the research pack (must-know slogans)**

- Valiant Turing 2010: **PAC learning** — Probably Approximately Correct framework.
- Learning as a computational complexity problem (sample + time resources).
- Bridge to modern ML theory; not a claim that deep learning is “solved.”

**Recommended order**


**Official / primary written hubs**

- Valiant Turing page: https://amturing.acm.org/award_winners/valiant_2612174.cfm  
- Deep Learning Trio Turing 2018: https://amturing.acm.org/award_winners/hinton_4791679.cfm  

Complete URL bibliography: `research/video-research/valiant-learning/references.md`.

## References


### Video research pack (all URLs)

Complete list: `research/video-research/valiant-learning/references.md`.

1. Valiant Turing page — https://amturing.acm.org/award_winners/valiant_2612174.cfm  
2. Wikipedia — Leslie Valiant — https://en.wikipedia.org/wiki/Leslie_Valiant  
3. Wikipedia — Probably approximately correct learning — https://en.wikipedia.org/wiki/Probably_approximately_correct_learning  
4. Wikipedia — Computational learning theory — https://en.wikipedia.org/wiki/Computational_learning_theory  
5. Valiant PAC paper culture (CACM / JACM lineage) — https://dl.acm.org/doi/10.1145/1968.1972  
6. Deep Learning Trio Turing 2018 — https://amturing.acm.org/award_winners/hinton_4791679.cfm  
7. Wikipedia — VC dimension (related theory) — https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension  
8. ACM awards page Valiant — https://awards.acm.org/award-recipients/valiant_2612174  
9. Research pack folder: `research/video-research/valiant-learning/`.

1. ACM Turing Award — Leslie G. Valiant — [amturing.acm.org](https://amturing.acm.org/).  
2. L. Valiant, “A theory of the learnable,” *CACM* 1984; Kearns–Vazirani, *An Introduction to Computational Learning Theory*.  
3. Standard complexity references for #P (Arora–Barak; textbooks treating permanent vs determinant).  
4. Course: [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/); [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/); [complexity]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/).

---

## Further directions

- Compare agnostic PAC vs realizable PAC after reading ML theory.  
- Explore Occam algorithms and compression bounds as cousins of sample complexity.  
- Read a short note on approximate counting and Markov-chain sampling.  
- Cross-check LO6 skills on a modern foundation-model press release.  
- Next: [Hopcroft & Tarjan]({{ site.baseurl }}/contents/en/chapter09/09_10_Hopcroft_Tarjan/)—algorithms as craft, not only classes.
