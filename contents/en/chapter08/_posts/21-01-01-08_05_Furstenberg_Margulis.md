---
layout: post
title: "Furstenberg & Margulis: Dynamics, Ergodic Theory, Rigidity (Abel 2020)"
chapter: '08'
order: 5
owner: Nguyen Le Linh
lang: en
categories:
- chapter08
lesson_type: required
---

Imagine a puzzle that seems to have nothing to do with physics or motion: pick any subset of the positive integers that makes up at least 1% of the number line—no matter how chaotically you scramble your choices, must it still contain an evenly spaced arithmetic progression of length 100? Or take another riddle: plug any three integers $$x, y, z$$ into $$x^2 + y^2 - \sqrt{2}\,z^2$$—can you force the output arbitrarily close to *every* real number?

For decades, pure questions like these about whole numbers resisted classical counting methods. Then two mathematicians entered with a daring shift in perspective that redrew the map of pure mathematics: **turn static numbers into motion!** Instead of counting integers one by one, watch them as the orbit of a point moving through a symmetric space, guided by probability and dynamical systems.

In **2020**, the **Abel Prize** was awarded jointly to **Hillel Furstenberg** (Hebrew University of Jerusalem) and **Gregory Margulis** (Yale University):

> “for pioneering the use of methods from probability and dynamics in group theory, number theory and combinatorics.”  
> — [Abel Prize Committee citation](https://abelprize.no/abel-prize-laureates/2020)

Pairing two very different mathematical styles in one Abel year sent an unmistakable message: probability and dynamics are not side appendices to applied math—they are central engines for solving deep problems in arithmetic, combinatorics, and group theory. Official materials: [abelprize.no](https://abelprize.no/).

**Lesson arc:** Key ideas (dynamical systems, ergodic theory, Lie groups and homogeneous spaces) → Ergodic theory in one page → Explanation: calculating an irrational rotation orbit and Oppenheim values by hand → Furstenberg and multiple recurrence → Margulis, superrigidity, and expanders → Common confusions.

---

## Learning objectives

After this lecture you should be able to define ergodic theory as the study of averages along orbits and invariant measures; state one Furstenberg theme (multiple recurrence / structure in dense integer sets); state one Margulis theme (superrigidity / arithmeticity / homogeneous dynamics); explain dynamics as a **tool** for arithmetic and combinatorics rather than only as a subject about chaos; and relate this worldview to [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) without claiming identical methods.

**Prerequisites.** Comfort with groups acting on spaces, basic probability (averages, measures), and integer subsets. No prior ergodic theory course is assumed; orbits and invariant measures are introduced at slogan level.

---

## Key ideas: What Are Ergodic Theory, Dynamical Systems, and Lie Groups, and What Do They Study?

If you graduated in science or engineering and took probability or differential equations, three pillars unlock the entire world of Furstenberg and Margulis without requiring a graduate textbook:

### 1. Dynamical Systems and Orbits
A **dynamical system** is any rule describing how a state evolves over time. In discrete time, we have a space $$X$$ and a map $$T: X \to X$$; starting at a point $$x$$, we follow its **orbit** $$x, Tx, T^2x, T^3x, \dots$$. The simplest example is an **irrational rotation on a circle**: at each step, jump forward by an irrational fraction of a full turn (say $$\sqrt{2}$$). The orbit never repeats its starting point and gradually spreads evenly around the entire circle.

### 2. Ergodic Theory
Born from Boltzmann’s statistical mechanics of gas molecules bouncing inside a box, **ergodic theory** asks: *if you track a single particle over a very long time (a time average), does that match taking a snapshot of all possible states in the box at one instant (a space average)?* A system that cannot be split into two separate invariant regions that never talk to each other is called **ergodic**. When a system is ergodic, almost every orbit visits every region with frequency equal to that region’s size (measure).

### 3. Lie Groups, Lattices, and Homogeneous Spaces
A **Lie group** $$G$$ is a group of symmetries that is simultaneously a smooth curved space—such as 3D rotations $$\mathrm{SO}(3)$$ or $$3\times 3$$ matrices of determinant 1, $$\mathrm{SL}_3(\mathbb{R})$$. Inside $$G$$ can sit a regular discrete grid $$\Gamma$$ called a **lattice** (like the integer grid $$\mathbb{Z}^n$$ inside $$\mathbb{R}^n$$, or $$\mathrm{SL}_3(\mathbb{Z})$$ inside $$\mathrm{SL}_3(\mathbb{R})$$). Folding $$G$$ along $$\Gamma$$ produces a **homogeneous space** $$G/\Gamma$$ (just as folding $$\mathbb{R}^2$$ by $$\mathbb{Z}^2$$ gives a donut $$\mathbb{T}^2$$). **Homogeneous dynamics** studies natural flows on $$G/\Gamma$$—and miraculously, their orbits decode classical problems in number theory!

---

## 1. The shared revolution

Classical number theory often counts and estimates: lattice points, primes in progressions, values of quadratic forms. Furstenberg and Margulis showed that many such problems become transparent—or at least newly approachable—once recast as **orbit problems** for a group acting on a space, with **invariant measures** controlling asymptotics.

The shared message is cultural as well as technical:

> Probability and dynamics are **core pure mathematics**, not only applied add-ons.

That message now saturates modern analytic number theory, geometric group theory, and parts of combinatorics. Abel 2020 awards the pioneers of that migration.

---

## 2. Ergodic theory in one page

A **dynamical system** in the measure-preserving sense is a space $$X$$ with a probability measure $$\mu$$ and a transformation $$T:X\to X$$ (or a group of transformations) that preserves $$\mu$$. An **orbit** of a point $$x$$ is

$$
\{ x,\, Tx,\, T^2x,\, T^3x,\, \dots \}.
$$

**Ergodic theorems** relate time averages along orbits to space averages with respect to $$\mu$$. Heuristically, if the system is ergodic (indecomposable), “almost every orbit sees the whole space” in the average sense:

$$
\lim_{N\to\infty}\frac{1}{N}\sum_{k=0}^{N-1} f(T^k x) = \int_X f\, d\mu
$$

for integrable observables $$f$$, for $$\mu$$-almost every $$x$$.

### Explanation: Two Hand-Checkable Calculations — Irrational Orbits and the Oppenheim Form

To feel firsthand how motion unlocks number theory, walk through two quick calculations you can check on a pocket calculator or by hand:

#### Example 1: The irrational rotation $$Tx = (x + \sqrt{2}) \bmod 1$$ on the circle $$[0, 1)$$
Starting at $$x_0 = 0$$, since $$\sqrt{2} \approx 1.4142$$, the fractional parts of $$k\sqrt{2}$$ hop as follows:
- $$k = 0 \implies x_0 = 0.0000$$
- $$k = 1 \implies x_1 = 0.4142$$
- $$k = 2 \implies x_2 = 0.8284$$
- $$k = 3 \implies x_3 = 0.2426$$ (since $$0.8284 + 0.4142 = 1.2426 \equiv 0.2426 \pmod 1$$)
- $$k = 4 \implies x_4 = 0.6569$$
- $$k = 5 \implies x_5 = 0.0711$$

In just 5 steps, the orbit has already placed points into nearly every subinterval $$[0, 0.2), [0.2, 0.4), [0.4, 0.6), [0.6, 0.8), [0.8, 1)$$, and it **never repeats** (if $$k\sqrt{2} \equiv m\sqrt{2} \pmod 1$$ for $$k \neq m$$, then $$\sqrt{2}$$ would be rational!). By the ergodic theorem, the fraction of steps landing in any arc of length $$0.1$$ converges to exactly $$0.1$$.

#### Example 2: Hunting near-zero values of the Oppenheim form $$Q(x, y, z) = x^2 + y^2 - \sqrt{2}\,z^2$$
Can we choose nonzero integer triples $$(x, y, z)$$ to push $$\lvert Q(x, y, z)\rvert$$ arbitrarily close to $$0$$?
- Try $$(1, 1, 1)$$: $$Q(1, 1, 1) = 1^2 + 1^2 - \sqrt{2} = 2 - 1.4142 \approx \mathbf{+0.5858}$$.
- Try $$(3, 2, 3)$$: $$Q(3, 2, 3) = 9 + 4 - 9\sqrt{2} = 13 - 12.7279 \approx \mathbf{+0.2721}$$.
- Try $$(28, 10, 25)$$: $$28^2 + 10^2 = 784 + 100 = 884$$, while $$25^2\sqrt{2} = 625 \times 1.41421356 \approx 883.8835$$, giving $$Q(28, 10, 25) \approx \mathbf{+0.1165}$$!

By brute force, trying to push $$\lvert Q\rvert < 10^{-50}$$ makes $$x, y, z$$ explode, and you never know whether values secretly hit a positive floor. Margulis’s miracle was to translate this integer hunt into the **orbit of the symmetry group $$\mathrm{SO}(2, 1)$$** acting on the space of 3D lattices $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$: proving that the orbit cannot stay trapped in a compact set immediately guarantees $$\lvert Q(x, y, z)\rvert$$ gets arbitrarily small!

---

## 3. Furstenberg: recurrence, structure, boundaries

### Multiple recurrence and Szemerédi-type structure

Szemerédi’s theorem says that any subset of the integers with positive upper density contains arithmetic progressions of arbitrary finite length. Furstenberg gave a revolutionary ergodic-theoretic proof in 1977 by translating density and progressions into **multiple recurrence**: for a measure-preserving system and a positive-measure set $$A$$, there are return times $$n$$ such that

$$
\mu\big(A \cap T^{-n}A \cap T^{-2n}A \cap \cdots \cap T^{-(k-1)n}A\big) > 0
$$

under appropriate hypotheses—capturing $$k$$-term progressions dynamically. Where Poincaré’s classical recurrence guaranteed returning to $$A$$ once ($$k = 2$$), Furstenberg proved a point returns $$k$$ times in an evenly spaced rhythm!

The idea is profound: **recurrence of orbits encodes combinatorial configurations**. Structure theorems for dynamical systems—splitting them into "structured" (compact) and "random-like" (weakly mixing) pieces—became structure theorems for large sets of integers, directly inspiring the later Green–Tao theorem on primes.

### Structure theory and arithmetic applications

Beyond a single theorem, Furstenberg developed structure theories and applications that tied dynamical systems to number theory and combinatorics. Boundary theory of random walks and group actions (**Furstenberg boundary**) is another major theme: how groups act on boundaries and what measures reveal about algebraic structure.

### Style

Furstenberg’s style often turns hard discrete questions into continuous, measure-theoretic ones—then harvests rigidity or recurrence. The Abel citation’s “probability and dynamics” clause is literal.

---

## 4. Margulis: rigidity, arithmeticity, homogeneous dynamics

### Superrigidity

**Superrigidity** theorems (Margulis and related work) assert that homomorphisms of higher-rank lattices (such as $$\mathrm{SL}_3(\mathbb{Z}) \subset \mathrm{SL}_3(\mathbb{R})$$) into algebraic groups are tightly constrained—essentially of algebraic origin. Heuristically: high-rank geometry is as rigid as diamond, forcing maps to be algebraic rather than wild.

### Arithmeticity

**Arithmeticity** results (which earned Margulis the 1978 Fields Medal) say that irreducible lattices in higher-rank semisimple Lie groups must arise from algebraic groups over number fields. Discrete geometry is forced to be arithmetic.

### Homogeneous dynamics

A **homogeneous space** is a quotient $$G/\Gamma$$ of a Lie group $$G$$ by a discrete subgroup $$\Gamma$$ (or related constructions). Flows on such spaces—especially unipotent flows—have rigid orbit-closure behavior (later completed in full generality by Marina Ratner). Margulis-type ideas exploit that rigidity to constrain number-theoretic sets: values of forms, orbit closures, equidistribution.

The crown jewel is Margulis’s 1986 proof of the **Oppenheim conjecture** on values of indefinite quadratic forms in three or more variables (like $$x^2 + y^2 - \sqrt{2}\,z^2$$ above). Diophantine approximation and form values became orbit-closure questions.

### Expanders and the pure/CS interface

Margulis also constructed the first explicit **expander graphs** (1973) using Kazhdan’s property (T) from group theory—sparse yet highly expanding graphs central to computer science, coding theory, and pure mathematics. Abel 2020 thus touches the same pure/CS border later honored in Abel 2021 (Lovász–Wigderson), from a dynamics/groups angle.

---

## 5. Homogeneous dynamics slogan (deeper map)

Unipotent flows on homogeneous spaces often have **rigid** orbit closures: closures are themselves homogeneous, not fractal chaos. That rigidity is a gift to number theory. Instead of estimating error terms by hand in every problem, one sometimes identifies a dynamical system whose orbit closures classify the arithmetic possibilities.

Furstenberg-type ideas and Margulis-type ideas are not identical machines. Furstenberg often leans on structure and recurrence in abstract measure-preserving systems (with combinatorial payoffs). Margulis often leans on algebraic groups, lattices, and homogeneous spaces (with arithmetic and geometric payoffs). Abel paired them because both made **dynamics a language of pure mathematics**.

---

## 6. Why Abel paired them

Different styles, same message. After Furstenberg and Margulis, it became normal for a number theorist to speak of invariant measures, for a combinatorialist to cite ergodic proofs, and for a geometer of discrete groups to live inside homogeneous dynamics. Probability ceased to be “only applied”; dynamics ceased to be “only chaos pictures.”

Compare with [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/): arithmetic progressions in the primes use ideas from additive combinatorics and ergodic-adjacent culture in a later Fields-era story. The Abel 2020 citation is about the pioneers who made such migrations possible at scale.

### A worked slogan: density → recurrence → configuration

Suppose $$A\subset\mathbb{Z}$$ has positive upper density. One builds (via a limiting procedure) a measure-preserving system and a set $$\widetilde{A}$$ whose measure reflects that density. Multiple recurrence then produces times $$n$$ for which

$$
\widetilde{A},\; T^{-n}\widetilde{A},\; T^{-2n}\widetilde{A}
$$

intersect nontrivially in measure—translating back to a 3-term arithmetic progression in $$A$$. The same philosophy scales to longer progressions with more sophisticated structure theory. You need not master the proofs to see the **dictionary**: combinatorial density speaks the language of dynamical recurrence.

Margulis-type slogans run differently: identify a homogeneous space and a flow; prove orbit closures are algebraic; read number-theoretic consequences off the classification. Both dictionaries are Abel-worthy infrastructure.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “Ergodic theory is only physics/stat mech.” | It is a pure mathematical theory of measure-preserving systems with arithmetic applications. |
| “Furstenberg proved Szemerédi first.” | Szemerédi’s combinatorial proof came first; Furstenberg gave a foundational ergodic proof and broader framework. |
| “Rigidity means nothing moves.” | It means maps/orbits are highly constrained—often algebraic—rather than arbitrary. |
| “Expanders are only CS.” | They are central in pure math too (groups, geometry, spectral graph theory). |
| “Dynamics solves all number theory.” | It is a powerful toolkit for *some* problems; many remain outside current dynamical reach. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/furstenberg-margulis/`.

**From the research pack (must-know slogans)**

- Abel 2020: probability & dynamics methods in group theory, number theory, combinatorics.
- **Furstenberg:** multiple recurrence → structure in large sets (Szemerédi culture).
- **Margulis:** superrigidity, arithmeticity, expanders from groups, Oppenheim conjecture.
- Cultural message: ergodic theory as an engine for pure math.

**Recommended order**

1. **Core** — Abel lectures 2020 Furstenberg & Margulis: [https://www.youtube.com/watch?v=2i5UJwKN7os](https://www.youtube.com/watch?v=2i5UJwKN7os).  
2. **History** — Abel interview Furstenberg: [https://www.youtube.com/watch?v=01IdfSRYawE](https://www.youtube.com/watch?v=01IdfSRYawE).  
3. **History** — Abel interview Margulis: [https://www.youtube.com/watch?v=FInTu9-MHHU](https://www.youtube.com/watch?v=FInTu9-MHHU).  
4. **Orientation** — Popular presentation of 2020 work (Bellos clip): [https://www.youtube.com/watch?v=Fqdl_jyw8OE](https://www.youtube.com/watch?v=Fqdl_jyw8OE).  
5. **Related** — Margulis on Kolmogorov–Sinai entropy (earlier Abel week): [https://www.youtube.com/watch?v=cuYO5NQieRA](https://www.youtube.com/watch?v=cuYO5NQieRA).  

**Official / primary written hubs**

- Abel 2020 Furstenberg & Margulis: https://abelprize.no/abel-prize-laureates/2020  

Complete URL bibliography: `research/video-research/furstenberg-margulis/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/furstenberg-margulis/transcripts/` · status: `research/video-research/furstenberg-margulis/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/furstenberg-margulis_2i5UJwKN7os_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/furstenberg-margulis/references.md`.

1. Abel 2020 Furstenberg & Margulis — https://abelprize.no/abel-prize-laureates/2020  
2. Abel lectures 2020 Furstenberg & Margulis — https://www.youtube.com/watch?v=2i5UJwKN7os  
3. Abel interview Furstenberg — https://www.youtube.com/watch?v=01IdfSRYawE  
4. Abel interview Margulis — https://www.youtube.com/watch?v=FInTu9-MHHU  
5. Popular presentation of 2020 work (Bellos clip) — https://www.youtube.com/watch?v=Fqdl_jyw8OE  
6. Margulis on Kolmogorov–Sinai entropy (earlier Abel week) — https://www.youtube.com/watch?v=cuYO5NQieRA  
7. NYT Abel 2020 — https://www.nytimes.com/2020/03/18/science/abel-prize-mathematics.html  
8. Nature Abel 2020 — https://www.nature.com/articles/d41586-020-00799-7  
9. Wikipedia — Hillel Furstenberg — https://en.wikipedia.org/wiki/Hillel_Furstenberg  
10. Wikipedia — Grigory Margulis — https://en.wikipedia.org/wiki/Grigory_Margulis  
11. Research pack folder: `research/video-research/furstenberg-margulis/`.

1. Abel Prize 2020 — [abelprize.no/abel-prize-laureates/2020](https://abelprize.no/abel-prize-laureates/2020).  
2. Expositions on homogeneous dynamics and Margulis’s work; surveys on Furstenberg multiple recurrence.  
3. Szemerédi’s theorem: combinatorial and ergodic proofs as parallel literatures.  
4. Course: [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/); later [Lovász–Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/) on discrete math/TCS.

---

## Further directions

- Bridge to additive combinatorics without full ergodic prerequisites: “dynamics detects patterns.”  
- Optional reading: popular accounts of the Oppenheim conjecture via dynamics.  
- Contrast rigidity theorems across fields (Margulis; Sullivan’s no wandering domains next).  
- Compare with a related [Fields essay]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/).  
- Note one open problem in homogeneous dynamics or additive combinatorics that still resists.  
- Next: [Lovász & Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/).

## Video tham khảo

- **xem trước** — [The Abel lectures: Hillel Furstenberg and Gregory Margulis](https://www.youtube.com/watch?v=2i5UJwKN7os) — The Abel Prize, English. Watch first. “The Abel lectures: Hillel Furstenberg and Gregory Margulis” orients the lesson’s aim: After this lecture you should be able to define ergodic theory as the study of averages along orbits and invariant measures; state one Furstenberg theme (multiple recurrence / stru…
- [Hillel Furstenberg - The Abel Prize interview 2020](https://www.youtube.com/watch?v=01IdfSRYawE) — The Abel Prize, English. A second pass once the main claim is in view: After this lecture you should be able to define ergodic theory as the study of averages along orbits and invariant measures; state one Furstenberg theme (multiple recurrence / stru…
- [Gregory Margulis - The Abel Prize interview 2020](https://www.youtube.com/watch?v=FInTu9-MHHU) — The Abel Prize, English. Further depth after the first two, still tied to this lesson: After this lecture you should be able to define ergodic theory as the study of averages along orbits and invariant measures; state one Furstenberg theme (multiple recurrence / stru…
