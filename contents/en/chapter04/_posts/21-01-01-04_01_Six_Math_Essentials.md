---
layout: post
title: "Six Math Essentials (after Terence Tao)"
chapter: '04'
order: 2
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
---

Step into a modern mathematics library and it is easy to feel overwhelmed: prime numbers sit on one shelf, curved manifolds on another, probability in a side aisle, and fluid equations behind a locked door. From the outside, mathematics can look like a giant warehouse of unrelated techniques.

In a [Big Think conversation](https://www.youtube.com/watch?v=OOMx2BHHWtE) introducing his forthcoming book *Six Math Essentials*, Terence Tao offers a far more welcoming picture. Rather than splintering the subject into hundreds of narrow subfields, he organizes a huge stretch of mathematics around **six familiar pillars**: numbers, algebra, geometry, probability, analysis, and dynamics. Each pillar begins with an everyday question—how many, how to combine operations, how to measure space, how to live with uncertainty—and then matures over centuries into a razor-sharp language for clear thought.

This lecture is a **course map**, not an endorsement of one textbook and not a claim that Tao's six themes exhaust mathematics. The pillars do not replace the Clay problems, the Fields portraits, or the proof essays elsewhere on the site. They give those pages a **shared grammar**. Once you can name which ancient pillar a modern story is practicing, you can travel across every chapter without losing the plot.

**Watch.** [One of the world's greatest mathematicians explains 6 essential concepts of math](https://www.youtube.com/watch?v=OOMx2BHHWtE) (Terence Tao, Big Think). Paraphrases below follow that conversation; they are not invented quotations.

**Research note.** Course pack: `research/video-research/tao-six-essentials/`.

---

## Learning objectives

After this lecture you should be able to:

- Name Tao’s six pillars and give one accessible example of each, without treating the list as a complete atlas of mathematics.
- Explain, in a sentence each, how number systems extend ($$\mathbb{N}\to\mathbb{Z}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}$$) and why the $$\sqrt{2}$$ shock belongs to that story.
- Distinguish **almost-sure eventual occurrence** from a **usable waiting time**, using the infinite-monkeys thought experiment.
- Connect one “curiosity first” story (parallel postulate, sphere packing, or compressed sensing) to a later scientific or technological use—without claiming mathematics always pays on a schedule.
- Navigate from this hub into the course essays on [$$\sqrt{2}$$]({{ site.baseurl }}/contents/en/chapter05/05_06_Irrationality_Sqrt2/), [infinity]({{ site.baseurl }}/contents/en/chapter04/04_02_Infinity/), [sphere packing]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/), [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/), [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/), [probability]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/), and [mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/).

**Prerequisites.** Comfort with high-school numbers, a little algebra, and the idea that a proof is an argument rather than a calculation. No graduate analysis is required.

---

## Background Knowledge Map: What Are the Six Pillars and How Do They Power Modern Mathematics?

In university, we usually take Calculus, Linear Algebra, and Probability as separate exam courses. Tao's lens helps a university graduate snap those separate pieces back into a single unified picture: **each pillar is a distinct habit of abstraction** applied to the same physical and logical world:

- **Numbers (Arithmetic & Number Theory):** Separate quantity from specific objects and extend the number system whenever an equation hits a wall ($$\mathbb{N}\to\mathbb{Z}\to\mathbb{Q}\to\mathbb{R}\to\mathbb{C}$$). Underpins cryptography, coding theory, and numerical computation.
- **Algebra:** Studies the *laws of operations* rather than individual numbers—scaling from scalar arithmetic to groups, rings, fields, and matrices. Forms the core engine of neural networks, 3D graphics, and particle physics.
- **Geometry (& Topology):** Measures distance, angle, curvature, and shape invariants under deformation—evolving from ancient land surveying to Einstein's curved spacetime and high-dimensional sphere packing.
- **Probability:** Quantifies uncertainty when a system is too complex for a full microscopic model. Powers statistics, clinical trials, quantitative finance, and statistical learning.
- **Analysis:** The art of controlling error bars, approximations, limits, and infinity. Serves as the safety harness for continuum physics, partial differential equations, and optimization.
- **Dynamics:** Asks what happens when a simple rule is iterated over long stretches of time—from planetary orbits and weather forecasting to diffusion models in generative AI.

The real magic of modern mathematics happens at the **intersections**: MRI compressed sensing merges analysis + linear algebra + probability; climate modeling merges analysis + dynamics + geometry; large language models sit at the crossroads of linear algebra (matrix multiplication), analysis (gradient optimization), and probability (token distributions).

---

## 1. A map, not a complete atlas

Tao’s starting observation is modest and useful. The six themes are old—some prehistoric, some a few centuries old—and they remain the words mathematicians reach for when a new subject has to be explained to a non-specialist. Strip away the technical clothing and you are left with ideas that are almost embarrassingly intuitive: how many, how to operate, how to measure space, how to live with uncertainty, how to control error and infinity, how things change in time. The sophistication is in the **language**, not in a secret seventh ingredient.

The list is a spine, not a census. Category theory, logic, and combinatorics are not expelled; they often appear as ways of talking *across* the pillars. This course already has other spines: famous unsolved problems, prize portraits, world-changing applications, famous proofs. Use the six essentials when you want to ask, “Which ancient habit of mind is this modern page still practicing?”

---

## 2. Numbers: precision, then extension

Numbers, Tao notes, are among the oldest inventions we can still see carved on bone. Without them, description stays poetic and drifts in the retelling. With them, quantity becomes portable: you can talk about grain, distance, or tax without pointing at the pile. Agriculture, trade, and the unromantic machinery of civilization all need that portability. Not every human decision should be reduced to a cost–benefit table—Tao is explicit that a date is a bad place for a spreadsheet—but finance and medicine are full of choices where quantitative thinking earns its keep.

The deeper story is that numbers **take on a life of their own**—every time an operation hits a wall, mathematics expands the number system while preserving consistency:

- Counting sheep gives $$\mathbb{N}=\{1,2,3,\ldots\}$$ with addition and subtraction. Because $$3 - 5$$ leaves $$\mathbb{N}$$, we invent zero and negatives ($$\mathbb{Z}$$) and find that $$(A-B)+B=A$$ still holds even when $$B>A$$.
- Division ($$3 \div 5$$) expands $$\mathbb{Z}$$ to fractions ($$\mathbb{Q}$$).
- Then comes the ancient shock: the diagonal of a unit square has length $$\sqrt{2}$$, yet no integers $$p, q$$ satisfy $$(p/q)^2 = 2$$. The Latin label *irrational* ("not a ratio") records how unsettling that felt. Filling all such gaps yields the real numbers $$\mathbb{R}$$.
- Finally, $$x^2 + 1 = 0$$ has no real root, giving birth to the complex numbers $$\mathbb{C}$$ with $$i^2 = -1$$—initially dismissed as "imaginary," yet later becoming the native tongue of electromagnetism, signal processing, and quantum mechanics.

**Course landing.** The proof that $$\sqrt{2}$$ is not a ratio is a Chapter 5 classic: [Irrationality of $$\sqrt{2}$$]({{ site.baseurl }}/contents/en/chapter05/05_06_Irrationality_Sqrt2/). The same extension story—new numbers invented so equations close, then unexpectedly useful—is the number-system moral of that essay.

---

## 3. Algebra: laws of operations, not just of numbers

Algebra, in Tao’s layering, is a second abstraction. Numbers already replaced sheep by symbols you can add. Algebra replaces specific numbers by $$x$$ and $$y$$, and then studies the **operations themselves**. Addition is commutative: $$A+B=B+A$$. Rotations of an object by $$30^\circ$$ then $$60^\circ$$ in the plane commute in the same algebraic sense; putting on socks and then shoes does not.

Why is spotting these abstract laws so powerful? Try multiplying two tiny $$2\times 2$$ matrices:

$$
A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}
\implies AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \neq \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} = BA.
$$

Matrices drop commutativity, yet they still obey associativity $$(AB)C = A(BC)$$ and distributivity $$A(B+C) = AB + AC$$. Because so much algebraic structure survives, techniques built for scalars scale seamlessly to giant arrays—the exact arrays that large language models multiply at industrial scale. See [linear algebra and AI]({{ site.baseurl }}/contents/en/chapter03/03_03_Linear_Algebra_AI/).

### Worked Example: Kepler at the Austrian Wine Market (1613)

Tao's favorite historical vignette is Johannes Kepler watching a wine merchant gauge the volume of a barrel by plunging a single straight rod through the bung-hole at the barrel's midpoint to the farthest bottom edge, reading off one length $$d$$. In principle, a single diagonal $$d$$ cannot fix a cylinder's volume—a tall skinny barrel and a short wide barrel can share the same $$d$$. Let's check with first-year calculus why the merchant's trick worked anyway:

1. Model the barrel as a cylinder of radius $$r$$ and height $$h$$. By Pythagoras, the rod from the midpoint (height $$h/2$$) to the far bottom rim (horizontal span $$2r$$) satisfies:
   $$d^2 = \left(\frac{h}{2}\right)^2 + (2r)^2 \implies r^2 = \frac{d^2 - h^2/4}{4}.$$
2. Express volume as a single-variable function of $$h$$:
   $$V(h) = \pi r^2 h = \frac{\pi}{4}\left(d^2 h - \frac{h^3}{4}\right).$$
3. Find the shape that maximizes volume for a fixed rod length $$d$$ by setting $$V'(h) = 0$$:
   $$V'(h) = \frac{\pi}{4}\left(d^2 - \frac{3}{4}h^2\right) = 0 \implies h^* = \frac{2}{\sqrt{3}}d \approx 1.1547\,d.$$
4. **Numerical check for $$d = 10\text{ dm}$$:**
   - At the optimal proportion $$h^* \approx 11.55\text{ dm}$$: $$V(11.55) \approx 604.6\text{ liters}$$.
   - For a slightly taller barrel with $$h = 12.0\text{ dm}$$ (nearly $$4\%$$ off in height): $$V(12.0) = \frac{\pi}{4}(1200 - 432) \approx 603.2\text{ liters}$$—**a volume error of only $$0.23\%$$!**

Because the curve $$V(h)$$ is flat at its peak ($$V'(h^*) = 0$$), small variations in barrel proportions barely budge the volume. Algebra plus an optimality insight turned a folk market rule into an ancestor of calculus. See [calculus in physics and engineering]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/).

---

## 4. Geometry: measuring what you cannot touch

Geometry is, literally, Earth-measurement. Distances, angles, and **similarity** let you infer a mountain’s distance from an elevation angle, or—already in antiquity—estimate the scale of the Earth, Moon, and Sun without leaving the ground. In the 3rd century BCE, Eratosthenes compared noon shadow angles in two Egyptian cities (differing by $$7.2^\circ$$, or $$1/50$$ of a full circle) and multiplied the $$800\text{ km}$$ distance between them by $$50$$ to estimate Earth's circumference at $$\approx 40{,}000\text{ km}$$. Geometry extends the senses.

The curiosity-driven sequel is the **parallel postulate**. Euclid’s other axioms feel inevitable; the claim that through a point off a line there is exactly one parallel does not. Drop it and two consistent geometries appear: **spherical** geometry, where great circles always meet (no parallels, triangle angle sum $$> 180^\circ$$), and **hyperbolic** geometry, where infinitely many parallels exist (triangle angle sum $$< 180^\circ$$). Once “the” geometry is no longer unique, curved spaces of every kind become thinkable. Riemannian geometry then supplies the language Einstein needed: mass–energy tells spacetime how to curve. The equations are brutal to solve—even two colliding black holes strain supercomputers—but they are natural to *state* once the geometric vocabulary exists.

**Course landings.** Non-Euclidean shock lives with [strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/). The packing sequel of the same chapter of Tao’s talk—Kepler’s cannonballs, Hales’s computer-assisted 3D proof, then discrete high-dimensional packings as wireless codes—lands in [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/) and the [sphere-packing studio]({{ site.baseurl }}/contents/en/chapter07/07_03_Explore_Sphere_Packing/).

---

## 5. Probability: living with uncertainty

School word problems are sanitized: Annie has thirty apples and nothing is in doubt. The world is not. A coin has a range of outcomes; even a “deterministic” flip is too expensive to predict from first principles. Probability records **which outcomes are more frequent**, not a fake certainty.

The subject’s origin story, as Tao tells it, is gambling correspondence: if you can compute the odds you can (in the long run) avoid being the person who cannot. It then escaped the casino. Any system too complicated for a complete mechanistic model—markets, a drug trial, a genetic lottery—invites a stochastic description. Probability works best on events that repeat often enough to estimate frequencies. **Once-in-a-century** events are a poorer fit; mathematics for truly rare disasters is still being built. Against that sobriety sits a miracle: **universality**. Sum 100 dice rolls, measurement noise in a lab, or height influenced by hundreds of independent genes, and wildly different microscopic mechanisms all converge to the exact same Gaussian bell curve (the Central Limit Theorem).

**Course landing.** [Probability and data science]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/). The analysis pillar will immediately warn you not to confuse “probability one” with “soon.”

---

## 6. Analysis: error bars, limits, and infinity with a seatbelt

Analysis, for Tao, is the mathematics of **inaccuracy** and of **infinity**. An object is two metres, plus or minus ten centimetres; the error bar is part of the statement. You can drive errors toward zero, but reaching zero may take an infinite budget of precision. Algebra’s rearrangement laws are safe for five summands and treacherous for infinitely many: the alternating harmonic series

$$
1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \cdots = \ln 2 \approx 0.693
$$

can be rearranged to sum to **any real number you choose**—or even diverge to $$\infty$$ (Riemann's rearrangement theorem)!

A gambling cartoon makes the danger concrete. Suppose you bet $$1$$ dollar on an even-money game and double after every loss: $$1, 2, 4, 8, 16, \ldots$$ A single win appears to recover everything and net $$1$$ dollar—**if** you have infinite capital. In reality, a streak of just $$10$$ losses in a row (probability $$1/1024$$, easily seen in a few evenings) costs $$1+2+\cdots+512 = 1023$$ dollars and demands a $$1024$$-dollar bet on round 11 just to chase $$1$$ dollar of profit. The strategy merely compresses ruin into a rare catastrophic event. Analysis is the seatbelt that exposes how "infinity cheats" and guides us safely back to finite money.

The **infinite monkeys** theorem is the same caution in another costume. If a monkey types forever, or infinitely many monkeys type, then any fixed finite text—including *Hamlet*—occurs **almost surely**. The proof idea is elementary: a positive chance per block, repeated independently, drives the probability of perpetual failure to zero. The waiting time, however, grows exponentially with the length of the text: on a 26-letter keyboard, a 4-letter word has chance $$1/26^4 \approx 1/457{,}000$$ (an afternoon on a laptop), while a 50-character sentence has chance $$1/26^{50} \approx 10^{-71}$$—tens of orders of magnitude longer than the age of the universe. “Almost surely eventually” is not a schedule.

Tao’s pedagogical cheat-code is borrowed from childhood video games: first give yourself infinite health, learn the map, then play the finite-resource version. Idealize (zero friction, infinite energy), solve, and use analysis to see which features survive the return trip. That is also his picture of mathematical process: failure is cheap, so you are allowed to explore the **negative space** of methods that do not work until the remaining path looks obvious—and the feeling is less “eureka” than “how did I miss this earlier?” High standards belong to **outcomes**; the **process** is allowed to be a long sequence of intelligent mistakes.

**Course landings.** Cardinal and ordinal infinity: [Infinity]({{ site.baseurl }}/contents/en/chapter04/04_02_Infinity/) (this chapter’s seminar flagship) and [Cantor’s diagonal]({{ site.baseurl }}/contents/en/chapter05/05_03_Cantor_Diagonal/). Studio: [Describe infinity]({{ site.baseurl }}/contents/en/chapter07/07_08_Explore_Describe_Infinity/).

---

## 7. Dynamics: simple rules, long time, surprise

Dynamics is change in time: a rule that takes a state to the next state, iterated until unexpected structure appears. Evolution’s local rules are simple and the biosphere is not. Each car on a freeway only tracks the car ahead; the network produces **traffic waves** that persist hours after the original accident is gone. Equilibria may be **stable** (a hanging pendulum) or **unstable** (the same pendulum balanced on its tip). Tao’s climate remark is a stability warning, not a political program: a long-lived near-equilibrium can be left, and the new dynamics may be less forgiving.

Newton could solve the **two-body** problem under inverse-square gravity and recover Kepler’s ellipses. The **three-body** problem gave him, by his own report as Tao retells it, a headache: no neat closed-form solution, and modern numerics show long stretches of near-periodicity interrupted by sudden rearrangements. Even the solar system, calm on human timescales, can hide long-term instabilities. After a point, the honest model of a deterministic chaotic system is often a **probability** model: forecasts blur.

**Course landings.** [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/), [emergence]({{ site.baseurl }}/contents/en/chapter04/04_12_Emergence/), [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/), [Explore iteration]({{ site.baseurl }}/contents/en/chapter07/07_09_Explore_Iteration/).

---

### Deep-Dive Explanation: Why Curiosity-Driven Ideas Become a Pipeline to Technology (Read Slowly)

Why do ideas invented purely for play—complex numbers, curved space, 8-dimensional sphere packing—keep turning into essential tools of physics and engineering decades later? Follow Tao's four-step perspective:

1. **Curiosity lets us drop hidden assumptions:** Free from immediate product deadlines, mathematicians dare to drop the parallel postulate, allow square roots of negatives, or leave 3D space just to see which structures remain coherent.
2. **Concise explanations are scarce:** Truly compact, unified mathematical structures (like Riemannian geometry or total-variation minimization in compressed sensing) are rare; when we find one, it often represents the *only* clean way to reconcile a set of constraints.
3. **Physics and engineering eventually hit the same wall:** Decades later, when Einstein drops absolute time or MRI engineers need faster scans from fewer measurements, the concise structure they need **coincides** with the mathematical language already built.
4. **The STEM pipeline cannot be cut in half:** Basic science $$\to$$ applied science $$\to$$ engineering $$\to$$ industry. Taking a "helicopter straight to the waterfall" without hiking the trails starves future technology of its deepest concepts.

**Quick check.** Pure mathematics does not promise every theorem will pay off on a schedule; its power is building a reservoir of exact languages before the world even knows it needs them.

---

## 8. How the pillars talk to science (and to this course)

Tao treats STEM as a pipeline: curiosity-driven basic science, then applied science, then engineering, then industry. Remove any community and the pipeline breaks. Eugene Wigner’s “unreasonable effectiveness” is the mystery that concepts invented for play—complex numbers, curved space—later fit a laboratory. Tao’s own working theory, offered as a theory and not as a theorem, is that short explanations are scarce, so a concise mathematical language and a concise physical language sometimes coincide after both sides have **unlearned** a bad assumption (absolute time is the relativity example).

Several stories from the same conversation reappear as course essays:

| Story (paraphrased from Big Think) | Course page |
|------------------------------------|-------------|
| $$\sqrt{2}$$ and extending the number system | [Irrationality of $$\sqrt{2}$$]({{ site.baseurl }}/contents/en/chapter05/05_06_Irrationality_Sqrt2/) |
| Parallel postulate → Riemannian geometry → gravity | [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/) |
| Cannonballs → Kepler → high-dimensional discrete packing → wireless codes | [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/) |
| MRI, least squares, total variation, unified “tricks” | [Green–Tao / Tao portrait]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) (compressed-sensing vignette) |
| Infinite monkeys; doubling bets | [Infinity]({{ site.baseurl }}/contents/en/chapter04/04_02_Infinity/) |
| 2-body vs 3-body; chaos as blurred prediction | [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/), [Navier–Stokes]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/) |
| Helicopter to the waterfall vs hiking the map | [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/) |

The compressed-sensing vignette is the one Tao tells in the first person: an MRI reconstruction that looked too good, a night spent trying to prove it was impossible, a failed step that reversed into an explanation, and then the realization that seismologists and astronomers had been using cousin tricks without a common theorem. The Fields portrait of Tao on this site is the Green–Tao theorem; the vignette is there so “Tao 2006” is not reduced to a single prime-progression headline.

On **AI**, Tao lists successive modes of science—theory, experiment, simulation, big data, and now automated assistance—and worries that a helicopter to the waterfall skips the side canyons you only find by hiking. Large language models, in his picture, are extraordinarily well-trained next-word engines: broad, fast, and complementary to human **depth**. Proofs can be generated and checked faster than the community can **digest** them into textbooks. That “proof indigestion” is a Chapter 6 theme, not a reason to abandon curiosity-driven research.

---

## 9. Common confusions

1. **“These six topics are all of mathematics.”** — They are a teaching spine. Logic, combinatorics, and many other fields remain first-class.
2. **“Almost surely means it happens soon.”** — The monkey types *Hamlet* with probability one in infinite time; the expected wait is not a life skill.
3. **“A doubling strategy beats the house.”** — Only with infinite capital; analysis is the seatbelt.
4. **“Non-Euclidean geometry was invented for Einstein.”** — The geometry was curiosity; the physics arrived later.
5. **“This page endorses a book or a video as official curriculum.”** — It is a map after one mathematician’s public framing, attributed to Big Think and a forthcoming book, sitting beside other maps in the course.

---

## Video sources

Use the conversation for **orientation and stories**, not as a substitute for theorems proved elsewhere in the course.

1. **ORIENTATION / CORE** — Terence Tao, *One of the world's greatest mathematicians explains 6 essential concepts of math* (Big Think): [https://www.youtube.com/watch?v=OOMx2BHHWtE](https://www.youtube.com/watch?v=OOMx2BHHWtE).
2. Companion portraits and proofs on this site (Green–Tao, Viazovska, infinity, $$\sqrt{2}$$, Navier–Stokes, mathematics of AI) have their own video-research packs.

**Status reminder.** *Six Math Essentials* is **forthcoming** as of the 2026 conversation. This page paraphrases a public talk; it is not the book.

---

## References

1. Terence Tao — Big Think conversation, YouTube OOMx2BHHWtE: https://www.youtube.com/watch?v=OOMx2BHHWtE
2. Course pack: `research/video-research/tao-six-essentials/`
3. Eugene Wigner, “The Unreasonable Effectiveness of Mathematics in the Natural Sciences” (historical essay Tao alludes to).
4. Course landings listed in Section 8; [Chapter 4 overview]({{ site.baseurl }}/contents/en/chapter04/).
5. Green–Tao and compressed sensing: see the vignette in [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) and the pack `research/video-research/Green_Tao/`.

*Literacy note.* Popular interviews compress history (Kepler, Euclid, Newton, Einstein, Hales). Prefer the dedicated essays when a date, a theorem statement, or a credit line is load-bearing.

---

## Further directions

Read [Infinity]({{ site.baseurl }}/contents/en/chapter04/04_02_Infinity/) next if you want the analysis pillar in slow motion; [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/) if you want dynamics. For prize-scale payoffs of the same habits of mind, jump to [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) and [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/). For the AI chapter of the same conversation, go to [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/). The point of a hub is not to finish the six pillars. It is to know which door you are opening.

## Video tham khảo

- **xem trước** — [One of the world's greatest mathematicians explains 6 essential concepts of math | Terence Tao](https://www.youtube.com/watch?v=OOMx2BHHWtE) — Big Think, English. Watch first. “One of the world's greatest mathematicians explains 6 essential concepts of math | Tere…” orients the lesson’s aim: Name Tao’s six pillars and give one accessible example of each, without treating the list as a complete atlas of mathematics.
