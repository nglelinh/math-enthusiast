---
layout: post
title: "Avila’s Renormalization in Dynamical Systems (Fields Medal 2014)"
chapter: '02'
order: 16
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Artur Avila** received the **Fields Medal 2014** for, in the IMU’s words, “his profound contributions to dynamical systems theory, which have changed the face of the field, using the powerful idea of **renormalization** as a unifying principle.” The citation names a *method*, not a single named conjecture closed in isolation. Avila did not invent renormalization—Wilson’s physics, Feigenbaum’s period-doubling, Sullivan’s holomorphic dynamics, and a long Brazilian and French school of one-dimensional maps were already there. What the medal records is a body of theorems in which looking at a system at a new scale, again and again, became a *dictionary* across one-dimensional maps, quasiperiodic Schrödinger operators, and Teichmüller dynamics.

This essay is for learners who have seen iteration of a map $$f:[0,1]\to[0,1]$$, or a linear recurrence with a varying coefficient, and want the architecture of Avila’s landscape. It does **not** claim that he classified all dynamical systems, nor that the Ten Martini spectrum theorem is a solo result. It explains slogans carefully: regular versus stochastic unimodal maps; cocycles and almost reducibility; Cantor spectrum of the almost Mathieu operator; weak mixing of interval exchanges; and how to attribute credit to collaborators such as Jitomirskaya, Forni, Viana, de Melo, and Lyubich.

---

## Learning objectives

After this lecture you should be able to:

- State the IMU 2014 citation in one careful sentence, with **renormalization** as a unifying tool rather than a personal invention.
- Explain, at slogan level, what it means to **renormalize** a dynamical system: pass to a first-return or rescaled map and study the new map as an object of the same type.
- Describe the **almost Mathieu operator** and the **Ten Martini** question (Cantor spectrum), and attribute the resolution jointly to **Avila–Jitomirskaya**.
- Distinguish one-frequency quasiperiodic Schrödinger **cocycles** from a claim that “all quantum spectra are Cantor sets.”
- Sketch interval exchange maps / Teichmüller dynamics and the role of **Lyapunov exponents**, naming collaborators (Forni, Viana, and others) rather than a single hero.
- Practice **LO6**: “Avila classified chaos” is hype; the theorems rearrange specific, hard classes.

**Prerequisites.** Iteration of a real map; the idea of an orbit and of sensitive dependence; matrices and eigenvalues enough to hear “Lyapunov exponent” as an exponential growth rate; comfort with a Cantor set as a nowhere-dense perfect subset of the line. No prior Teichmüller theory or spectral theory of ergodic operators is required.

**Seminar links.** Dynamics cousins: [Mirzakhani / moduli and Teichmüller]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) (same 2014 class; surfaces rather than spectra). Arithmetic dynamics of a different flavour: [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/). For “unifying languages” elsewhere in the chapter, compare [Scholze / tilting]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/) as infrastructure, not as the same toolbox.

---

## 1. A history of looking again at a smaller scale

Dynamical systems theory asks what happens if you iterate a rule. The logistic family $$x\mapsto rx(1-x)$$ already shows the pedagogical shock of the 1970s: a quadratic polynomial, as the parameter $$r$$ varies, can pass from attracting cycles through period-doubling into chaos. **Mitchell Feigenbaum** extracted universal scaling constants from that cascade. In physics, **Kenneth Wilson** had already made renormalization a way to move between scales in statistical mechanics. In holomorphic dynamics, **Dennis Sullivan** and others recast one-dimensional maps so that a first-return map, after affine rescaling, again looks like a map of the same class—an operator on a space of maps, not a single orbit.

By the 1990s the Brazilian school around IMPA (de Melo, Palis, Yoccoz, Lyubich on the quadratic family) had a precise dream: a typical unimodal map should be either **regular** (an attracting cycle organizes the future) or **stochastic** (an absolutely continuous invariant measure). A 2003 paper of **Avila, Welington de Melo, and Mikhail Lyubich** closed that chapter for real-analytic unimodal families. Renormalization compares a small-scale return map with the original family and turns “typical” into a theorem.

**Slogan.** Renormalization is not a new equation of motion. It is a *change of coordinates on the space of systems*: zoom in, rescale, and ask whether the new system is simpler, conjugate to a known model, or itself renormalizable again.

Avila’s later work treats that slogan as portable. The same instinct—compare a cocycle over a rotation with a renormalized cocycle, or a first-return of an interval exchange with a simpler exchange—reappears in spectral theory and in Teichmüller dynamics. That portability is what the IMU means by a unifying principle.

---

## 2. What a renormalization theorem rearranges

A typical “hard” theorem in this landscape does not list every orbit. It **rearranges the parameter space**. Before the theorem, you have a zoo: Diophantine frequencies and Liouville frequencies; hyperbolic and parabolic combinatorics; maps that renormalize infinitely often and maps that do not. After the theorem, large regions of the zoo are declared equivalent, or are reduced to a model whose Lyapunov exponents, spectra, or mixing properties you already understand.

Three rearrangements are safe to name at seminar level.

**Unimodal maps (with de Melo and Lyubich).** The regular/stochastic dichotomy for typical analytic unimodal maps turns a decades-long case study into a global picture: chaos is not an exotic leftover; it is one of two typical phases, and renormalization organizes the boundary.

**One-frequency Schrödinger operators and cocycles.** A quasiperiodic potential, the simplest being a cosine sampled along an irrational rotation, produces a discrete Schrödinger operator on $$\ell^2(\mathbb{Z})$$. The associated **Schrödinger cocycle** is a map that updates a solution by a $$2\times 2$$ matrix depending on the phase. Avila’s **global theory of one-frequency cocycles** (developed through the 2000s and published in the following decade) uses renormalization and complexification of the energy to divide the energy axis into regimes: in some, the cocycle is close to constant after a change of coordinates (**almost reducibility**); in others, Lyapunov exponents are positive and the spectral measures are more singular. The almost Mathieu family is the emblematic example, not the only one.

**Interval exchanges and Teichmüller flow (with collaborators).** Cutting an interval into subintervals and permuting them—an **interval exchange transformation (IET)**—is the one-dimensional shadow of a translation flow on a flat surface. **Avila–Forni** proved that almost every IET (not a rotation) is weakly mixing. **Avila–Viana** proved the Zorich–Kontsevich conjecture on simplicity of the nontrivial Lyapunov exponents of the Teichmüller geodesic flow on the moduli space of Abelian differentials. These are theorems about *typical* systems in a measure-theoretic sense, not a classification of every surface or every permutation.

**What is not rearranged.** There is no theorem that “classifies all dynamical systems.” High-dimensional smooth dynamics remains active; Avila later contributed (with Crovisier, Wilkinson, and others) to entropy and ergodicity far from unimodal maps. The citation is a *style of reduction*, not an encyclopedia.

---

## 3. The almost Mathieu operator and the Ten Martini problem

The **almost Mathieu operator** on $$\ell^2(\mathbb{Z})$$ is

$$
(H_{\lambda,\alpha}\psi)_n=\psi_{n+1}+\psi_{n-1}+2\lambda\cos\bigl(2\pi n\alpha\bigr)\,\psi_n,
$$

with coupling $$\lambda\in\mathbb{R}$$ and frequency $$\alpha$$. When $$\alpha$$ is rational the spectrum is a finite union of bands. When $$\alpha$$ is irrational the spectrum is independent of a phase parameter (omitted here) and has been expected, since work of Azbel and the numerical **Hofstadter butterfly**, to be a **Cantor set**: closed, nowhere dense, without isolated points. **Mark Kac** offered ten martinis for a proof; **Barry Simon** named the **Ten Martini problem**.

Partial results accumulated for decades (Bellissard–Simon, Sinai, Helffer–Sjöstrand, Last, Puig, and others), often under Diophantine conditions on $$\alpha$$ or away from the **critical** coupling $$|\lambda|=1$$. In 2005–2009, **Artur Avila** and **Svetlana Jitomirskaya** proved the complete statement: the spectrum is a Cantor set for **all irrational frequencies and all nonzero couplings**. The non-critical regime $$|\lambda|\neq 1$$ is the cleanest slogan for a first reading; the paper’s difficulty is that Diophantine and Liouville techniques do not mesh automatically, and a thin “interface” of parameters had to be treated by hand. Attribute the theorem **jointly**. Later work by Jitomirskaya and others extends Cantor-spectrum phenomena beyond the exact cosine potential; that is a sequel, not the 2014 citation.

**Accuracy.** Ten Martini is about the *shape* of the spectrum as a subset of $$\mathbb{R}$$. Separate conjectures concern the *measure* of the spectrum (Aubry–André / Lebesgue measure $$|4-4|\lambda||$$) and localization of eigenfunctions. Do not collapse those into one sentence.

---

## 4. Honest attribution

The IMU news release on Avila’s work is unusually explicit: nearly all of it was done with collaborators—on the order of thirty mathematicians. A fair seminar table looks like this.

| Result (slogan) | Credit |
|-----------------|--------|
| Regular vs stochastic typical unimodal maps | Avila–de Melo–Lyubich (2003) |
| Weak mixing of almost every IET / translation flow | Avila–Forni (2007) |
| Cantor spectrum of almost Mathieu (Ten Martini) | Avila–Jitomirskaya (Annals, 2009) |
| Simplicity of Lyapunov exponents of Teichmüller flow | Avila–Viana (Zorich–Kontsevich) |
| Global theory of one-frequency Schrödinger operators | Avila (and a long spectral-theory community) |
| Renormalization as an idea | Wilson, Feigenbaum, Sullivan, Lyubich, Yoccoz, … |

Avila grew up in Rio de Janeiro, earned his PhD at **IMPA** in 2001 under **Welington de Melo**, and has been affiliated with the French CNRS and later the University of Zurich. He is the **first Brazilian** Fields Medalist, and in common accounts the first from South America (and more broadly the first Latin American). Those biographical facts explain a public narrative; they do not replace the theorems.

---

## 5. Why a Fields Medal

Three reasons, none of them “he tamed chaos in general.” Quasiperiodic spectral theory splits into Diophantine and Liouville worlds; closing Ten Martini required moving between them. Renormalization already existed—making it a *default language* for several flagship problems changed what a paper is allowed to try. And weak mixing of IETs, or regular/stochastic unimodal maps, are statements about *almost every* system in a natural measure: the modern substitute, in much of dynamics, for a hopeless pointwise classification.

In this course Avila sits next to [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) as a 2014 story about moduli of surfaces and their flows—adjacent geometry, different questions.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Avila invented renormalization.” | The idea is older (Wilson, Feigenbaum, Sullivan, …). He used it as a unifying tool. |
| “He classified all dynamical systems.” | He proved deep theorems for specific, central classes. |
| “Ten Martini is Avila’s alone.” | It is **Avila–Jitomirskaya**. |
| “The spectrum is a Cantor set for every Schrödinger operator.” | The theorem is for the almost Mathieu family (and later extensions); general one-frequency operators have a richer phase diagram. |
| “Weak mixing is the same as mixing.” | IETs are never strongly mixing; Avila–Forni is about *weak* mixing of typical exchanges. |
| “Lyapunov exponents of Teichmüller flow are Avila’s solo theorem.” | Simplicity is Avila–Viana, completing a conjecture of Zorich–Kontsevich; Forni and others are part of the same story. |

---

## Exercises

1. In your own words: what does a **renormalization step** forget, and what does it retain, when you pass from a unimodal map to a rescaled first-return map?
2. Why might physicists and mathematicians both care whether a spectrum is a Cantor set? Separate “pretty picture (Hofstadter)” from “theorem (closed set with empty interior, no isolated points).”
3. Write the almost Mathieu operator and mark the **coupling** and the **frequency**. What happens, at slogan level, if the frequency is rational?
4. Ten Martini: state the theorem in one sentence and name **both** authors. Then write one sentence you would *refuse* to print (“Avila showed all quantum spectra are fractal”).
5. Interval exchanges: explain with a sketch why cutting-and-stacking need not mix like a riffle shuffle, and what “weak mixing” is trying to salvage.
6. **Attribution practice.** Take any popular sentence that says Avila “solved chaos.” Rewrite it in two precise sentences suitable for this course.
7. Skim the IMU 2014 text on Avila (or the news-release PDF) and list **three** results that are *not* Ten Martini.
8. **Seminar stretch.** Compare Avila’s “typical unimodal map” theorems with [Mirzakhani’s]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) theorems about typical geodesics on moduli space: both are about *spaces of systems*. What is the space in each story?

---

## Video and reading links

No course video-research pack is attached to this lesson. Use official and encyclopedia sources first.

1. IMU Fields Medals 2014 (citation): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014).
2. IMU news release, *The Work of Artur Avila*: [PDF](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_avila.pdf).
3. Encyclopedia orientation: [Artur Avila](https://en.wikipedia.org/wiki/Artur_Avila); [almost Mathieu operator](https://en.wikipedia.org/wiki/Almost_Mathieu_operator).
4. Quanta profile (2014): [A Brazilian Wunderkind Who Calms Chaos](https://www.quantamagazine.org/artur-avila-is-first-brazilian-mathematician-to-win-fields-medal-20140812/).
5. arXiv search (renormalization + Avila): [query](https://arxiv.org/search/?query=Avila+renormalization&searchtype=all).
6. Avila–Jitomirskaya, *The Ten Martini Problem*, *Annals of Mathematics* (2009): [annals page](https://annals.math.princeton.edu/2009/170-1/p08).

**Status reminder:** Renormalization as a unifying method; Ten Martini is joint; no classification of all dynamics.

---

## References

1. International Mathematical Union, Fields Medals 2014 — Artur Avila citation and news release (mathunion.org).
2. **A. Avila, S. Jitomirskaya**, *The Ten Martini Problem*, *Ann. of Math.* 170 (2009).
3. **A. Avila, G. Forni**, *Weak mixing for interval exchange transformations and translation flows*, *Ann. of Math.* (2007).
4. **A. Avila, W. de Melo, M. Lyubich**, *Regular or stochastic dynamics in real analytic families of unimodal maps*, *Invent. Math.* (2003).
5. **A. Avila, M. Viana**, work on simplicity of Lyapunov exponents for Teichmüller flow (Zorich–Kontsevich conjecture).
6. Background pointers (not claimed as Avila’s theorems): Feigenbaum period-doubling; Sullivan holomorphic renormalization; surveys of quasiperiodic Schrödinger operators.
7. Course: [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/), [Chapter 2 overview]({{ site.baseurl }}/contents/en/chapter02/).

---

## Further directions

- Read a short survey on one-frequency cocycles until you can say “almost reducibility” without quoting a blog.
- Compare IET weak mixing with translation flows on flat surfaces; this is the bridge toward Mirzakhani’s moduli world and toward billiards.
- Seminar A3 option: a one-page “open problems after Avila” brief (higher-frequency Schrödinger operators; effective constants; conservative diffeomorphisms)—without claiming the medal closed dynamical systems.
- When you meet a Hofstadter butterfly picture, write the Ten Martini *theorem* next to it so the image does not replace the statement.
