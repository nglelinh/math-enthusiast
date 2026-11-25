---
layout: post
title: "Lindenstrauss’s Measure Rigidity (Fields Medal 2010)"
chapter: '02'
order: 23
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Play a simple game on the circle $$[0, 1)$$: at each step, multiply your position by $$2$$ and drop the integer part ($$x \mapsto 2x \bmod 1$$). This chaotic map admits a wild zoo of invariant probability measures—Lebesgue measure, periodic point masses, and uncountably many fractal measures supported on Cantor sets. Now add just one extra rule: demand that the measure be invariant *simultaneously* under multiplication by $$2$$ **and** multiplication by $$3$$. Hillel Furstenberg discovered a striking phenomenon called **measure rigidity**: adding a second independent commuting symmetry collapses nearly the entire fractal zoo, leaving only clean algebraic measures!

Even more astonishingly, that question about chaotic dynamics unlocks two of the deepest problems in **number theory** and **quantum physics**—simultaneous Diophantine approximation (**Littlewood’s conjecture**) and the high-energy distribution of quantum waves on negatively curved surfaces (**quantum unique ergodicity**). In 2010, **Elon Lindenstrauss** received the **Fields Medal**:

> “for his results on measure rigidity in ergodic theory, and their applications to number theory.”
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

The medal honors his measure-classification theorems for **higher-rank diagonalizable actions** on homogeneous spaces, and two headline exports: proving that exceptions to **Littlewood’s conjecture** have **Hausdorff dimension zero** (with Manfred Einsiedler and Anatole Katok), and proving **arithmetic quantum unique ergodicity (QUE)** for Hecke–Maass forms on compact arithmetic hyperbolic surfaces. We place Lindenstrauss inside the landscape built by Furstenberg, Margulis, Ratner, Katok, Einsiedler, and Host–Kra—while staying honest about what remains open (full Littlewood’s conjecture and non-arithmetic QUE).

**Lesson roadmap:** Key ideas (ergodic theory, homogeneous spaces of lattices, unipotent vs. higher-rank diagonal) → Hand-verifiable worked examples ($$\times 2$$ vs. $$\times 3$$ on the circle and translating Littlewood into a $$3\times 3$$ matrix orbit) → Explanation: 4 steps from EKL measure classification to Littlewood and arithmetic QUE → Landscape of contributors & comparison with Abel 2020.

---

## Learning objectives

After this lecture you should be able to:

- Define **measure rigidity** and illustrate it concretely by contrasting $$\times 2 \bmod 1$$ (abundant fractal measures) with $$\times 2, \times 3$$ (rigidified measures).
- Distinguish **unipotent** rigidity (Ratner’s complete algebraic classification) from **higher-rank diagonal** rigidity (Einsiedler–Katok–Lindenstrauss, requiring positive entropy).
- State **Littlewood’s conjecture**, translate it into bounded diagonal orbits on $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$, and state the exact EKL theorem (**Hausdorff dimension zero** for exceptions).
- State **arithmetic QUE** for compact arithmetic hyperbolic surfaces (Lindenstrauss, 2006), crediting Rudnick–Sarnak for the conjecture and Soundararajan (2010) for ruling out escape of mass on the modular surface.
- Credit Furstenberg, Margulis, Ratner, Katok, Einsiedler, Host–Kra, Bourgain, and Holowinsky–Soundararajan accurately, keeping Fields 2010 distinct from Abel 2020 in [Chapter 8]({{ site.baseurl }}/contents/en/chapter08/).

**Prerequisites.** Group actions; the idea of an invariant measure and of ergodicity; hyperbolic geometry of the upper half-plane at slogan level ($$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$). Homogeneous spaces $$\Gamma\backslash G$$ as “lattices acting on Lie groups” can be taken as a picture rather than a theory.

**Seminar links.** [Furstenberg & Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/) for the Abel 2020 worldview (dynamics as a tool for number theory). [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) for a different ergodic-to-arithmetic export. [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/) for homogeneous dynamics in a later Fields portrait.

---

## Key ideas: What Do Ergodic Theory, Homogeneous Dynamics, and Measure Rigidity Study?

### 1. Ergodic theory and measure rigidity
Ergodic theory studies long-term statistical averages of a measure-preserving group action $$(X, \mu, H)$$. An invariant probability measure $$\mu$$ is **ergodic** if it cannot be split into two nontrivial invariant pieces—it is a statistical "atom" of the dynamics. **Measure rigidity** asks the deeper prior question: *which ergodic invariant measures can exist at all?*

### 2. Homogeneous spaces $$\Gamma\backslash G$$—where number theory becomes motion
Every unit-volume lattice in $$\mathbb{R}^d$$ has the form $$g\mathbb{Z}^d$$ for $$g \in \mathrm{SL}_d(\mathbb{R})$$, and two matrices give the same lattice when they differ by a change of integer basis $$\gamma \in \mathrm{SL}_d(\mathbb{Z})$$. Thus the space of lattices is the **homogeneous space** $$\mathrm{SL}_d(\mathbb{R})/\mathrm{SL}_d(\mathbb{Z})$$. Diophantine approximation translates directly into geometry: *when we stretch and squeeze a lattice with diagonal matrices, does it ever acquire an abnormally short nonzero integer vector (sending its orbit deep into the cusp at infinity)?*

### 3. Unipotent flows vs. higher-rank diagonal actions
- **Unipotent flows** (like shear matrices $$\begin{pmatrix}1 & t \\ 0 & 1\end{pmatrix}$$): orbits separate slowly at **polynomial** speed. **Marina Ratner** (1990s) proved a complete algebraic classification of all ergodic invariant measures and orbit closures—with no entropy assumption needed! Earlier, **Margulis** used unipotent flows to prove the Oppenheim conjecture.
- **Higher-rank diagonal actions** (like the 2-parameter positive diagonal torus $$\mathrm{diag}(e^s, e^t, e^{-s-t})$$ on $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$): orbits diverge **exponentially**, creating wild fractal invariant sets. There is no unconditional Ratner theorem, yet Furstenberg and Margulis conjectured that imposing **positive entropy** eliminates pathological fractals and forces measures to be algebraic!

| Culture | Typical actor | Classification | Arithmetic export |
|---------|---------------|----------------|-------------------|
| Ratner / Margulis unipotent | Unipotent one-parameter groups | Complete, algebraic | Oppenheim, many others |
| Diagonal higher rank | Split tori, $$\times 2\times 3$$ | Partial; entropy hypotheses | Littlewood-type Diophantine |

---

## 1. Hand-Verifiable Worked Examples: $$\times 2$$ vs. $$\times 3$$ and the $$3\times 3$$ Littlewood Matrix

### Example 1: Why one map is "soft" while two commuting maps are "rigid"
Consider $$T_2(x) = 2x \bmod 1$$ on $$[0, 1)$$:
- Pick $$x = \frac{1}{3}$$: $$T_2(1/3) = \frac{2}{3}$$ and $$T_2(2/3) = \frac{4}{3} \equiv \frac{1}{3}$$. That 2-cycle immediately supports an invariant ergodic measure $$\mu = \frac{1}{2}\delta_{1/3} + \frac{1}{2}\delta_{2/3}$$.
- Write $$x$$ in binary $$0.b_1 b_2 b_3\ldots$$: $$T_2$$ is just the left shift! Flipping a biased coin with $$P(b_k = 1) = 0.7$$ independently for each bit generates a **fractal singular measure** invariant under $$T_2$$—there are uncountably many.
- Now impose invariance under $$T_3(x) = 3x \bmod 1$$ as well: $$1/3$$ is sent to $$0$$ (destroying the 2-cycle), and multiplying by $$3$$ scrambles binary digits completely! **Rudolph’s theorem (1990)** proved that any probability measure on the circle invariant under *both* $$T_2$$ and $$T_3$$ with **positive entropy** *must* be Lebesgue measure!

### Example 2: Translating Littlewood’s conjecture into a $$3\times 3$$ matrix orbit
**Littlewood’s conjecture (1930s)** asks whether every pair of real numbers $$(\alpha, \beta)$$ satisfies

$$
\liminf_{n\to\infty}\, n\,\|n\alpha\|\,\|n\beta\| = 0,
$$

where $$\|\cdot\|$$ is distance to the nearest integer. Encode $$(\alpha, \beta)$$ into the $$3\times 3$$ lattice matrix

$$
u_{\alpha,\beta} = \begin{pmatrix} 1 & 0 & 0 \\ \alpha & 1 & 0 \\ \beta & 0 & 1 \end{pmatrix} \in \mathrm{SL}_3(\mathbb{R}),
\qquad
a(s,t) = \begin{pmatrix} e^{-s-t} & 0 & 0 \\ 0 & e^s & 0 \\ 0 & 0 & e^t \end{pmatrix}.
$$

Act on any integer vector $$(n, -p, -q)^T \in \mathbb{Z}^3$$: the resulting vector is $$\bigl(e^{-s-t} n,\; e^s(n\alpha - p),\; e^t(n\beta - q)\bigr)^T$$, and the product of the absolute values of its three coordinates is **completely independent of $$s, t$$**:

$$
\vert e^{-s-t} n \vert \cdot \vert e^s(n\alpha - p) \vert \cdot \vert e^t(n\beta - q) \vert = \vert n \vert \cdot \vert n\alpha - p \vert \cdot \vert n\beta - q \vert!
$$

Look at what just happened: if $$(\alpha, \beta)$$ is a **counterexample** to Littlewood (so $$n\|n\alpha\|\|n\beta\| \ge c > 0$$ for all $$n \ge 1$$), then every nonzero vector in the lattice $$a(s,t)u_{\alpha,\beta}\mathbb{Z}^3$$ has length bounded below by $$c^{1/3} > 0$$ for *all* $$s, t \ge 0$$! By Mahler’s compactness criterion, **its entire diagonal orbit is trapped inside a compact subset**, never escaping into the cusp!

---

## 2. Explanation: From Measure Rigidity to Littlewood and Arithmetic QUE

How does classifying invariant measures on homogeneous spaces crack both Diophantine approximation and quantum chaos? Follow four steps:

#### Step 1: The EKL measure-classification theorem (Einsiedler–Katok–Lindenstrauss, *Annals*, 2006)
On $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$ (rank 2), EKL studied probability measures $$\mu$$ invariant and ergodic under the full positive diagonal torus $$A = \{a(s,t)\}$$. Using **coarse Lyapunov foliations** and entropy-decomposition techniques along expanding/contracting directions, they proved: any ergodic $$A$$-invariant measure with **positive entropy** (for some element of $$A$$) must be **algebraic** (Haar measure on a closed orbit of an intermediate subgroup)!

#### Step 2: Deduce Hausdorff dimension zero for Littlewood exceptions
Suppose the set of counterexamples $$(\alpha, \beta)$$ to Littlewood’s conjecture had positive Hausdorff dimension. By Frostman’s lemma and weak limits along their trapped compact orbits, one could construct an $$A$$-invariant measure supported on that compact set with **positive entropy**—contradicting Step 1! Therefore, **the exceptional set to Littlewood’s conjecture has Hausdorff dimension zero**! (Because a dimension-zero set can still be nonempty, full Littlewood’s conjecture remains open.)

#### Step 3: Microlocal lifts turn quantum waves (QUE) into geodesic-flow measures
On a hyperbolic surface $$M = \Gamma\backslash\mathbb{H}$$, a Maass form is an $$L^2$$ Laplacian eigenfunction $$-\Delta\phi = \lambda\phi$$ with probability density $$\mu_\phi = \vert\phi\vert^2 d\mathrm{vol}$$. **Quantum unique ergodicity (QUE)**, conjectured by **Rudnick–Sarnak (1994)**, asserts that *every* high-energy sequence $$\mu_\phi$$ converges to uniform volume (no "quantum scars" concentrating along closed geodesics). Via a **microlocal lift**, any weak limit $$\mu$$ lifts to a probability measure on the unit tangent bundle $$\Gamma\backslash\mathrm{SL}_2(\mathbb{R})$$ invariant under the **geodesic flow** (a rank-1 diagonal action!).

#### Step 4: Hecke operators supply the missing "second rank" (Lindenstrauss, *Annals*, 2006)
A rank-1 geodesic flow alone is too soft for measure rigidity. Lindenstrauss’s masterstroke for **arithmetic** hyperbolic surfaces was to exploit the fact that Hecke–Maass forms are joint eigenfunctions of infinitely many **Hecke operators**: this provides recurrence along extra $$p$$-adic / adelic directions (acting as a second commuting symmetry on $$\Gamma\backslash\mathrm{SL}_2(\mathbb{R}) \times L$$), while earlier joint work of **Bourgain–Lindenstrauss** guaranteed **positive entropy**! Feeding both into his measure-rigidity machine, Lindenstrauss proved that the unique arithmetic quantum limit on any **compact** arithmetic hyperbolic surface is normalized volume—settling **compact arithmetic QUE**!

*(On the non-compact modular surface $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$, Lindenstrauss’s method showed every limit is $$c\cdot d\mathrm{vol}$$ for $$c \in [0, 1]$$; **Kannan Soundararajan** (*Annals*, 2010) proved $$c = 1$$ (no escape of mass into the cusp), completing modular Hecke–Maass QUE. Parallel QUE for **holomorphic** Hecke cusp forms was proved by **Holowinsky–Soundararajan** (2010) via analytic number theory; general non-arithmetic QUE remains open.)*

Summary of Lindenstrauss’s bridge:

$$
\text{Number theory (Littlewood / Hecke–Maass)}
\;\longleftrightarrow\;
\text{Orbits on } \Gamma\backslash G
\;\xrightarrow{\text{Higher rank + Entropy } > 0}\;
\text{Unique algebraic measure}.
$$

---

## 3. Landscape of Contributors and Why a Fields Medal

| Name | Role in this story |
|------|---------------------|
| Furstenberg | $$\times 2,\times 3$$ and the idea that extra commuting maps rigidify measures; multiple recurrence |
| Margulis | Superrigidity, arithmeticity, unipotent flows, Oppenheim; conjectural diagonal rigidity |
| Ratner | Classification for unipotent flows—the completed sibling of the diagonal problem |
| Katok | Entropy, rigidity, and the EKL collaboration |
| Einsiedler | EKL and later homogeneous dynamics with Lindenstrauss and others |
| Host–Kra | Structure of multiple averages / nilfactors—the broader ergodic rigidity culture |
| Rudnick–Sarnak | QUE conjecture |
| Soundararajan | No escape of mass on $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$; holomorphic QUE with Holowinsky |
| Bourgain | Entropy of quantum limits (with Lindenstrauss) |

Elon Lindenstrauss (born 1970) earned his 1999 PhD at the Hebrew University under Benjamin Weiss, held a Clay fellowship (2003–2005), taught at Princeton and Jerusalem, and joined the permanent faculty of IAS in 2024—the first Israeli Fields medalist.

**Why a Fields Medal:** Rather than claiming one conjecture closed, the 2010 medal honors a **transformative method**—combining positive entropy, higher-rank/Hecke symmetries, and homogeneous dynamics to manufacture deep arithmetic theorems, carrying forward the Abel 2020 worldview of [Chapter 8]({{ site.baseurl }}/contents/en/chapter08/).

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Littlewood’s conjecture is proved.” | EKL: exceptions have Hausdorff dimension zero. The full statement is open. |
| “QUE is proved for all hyperbolic surfaces.” | Arithmetic Hecke–Maass, compact case (Lindenstrauss); modular surface with Soundararajan; general QUE is open. |
| “Lindenstrauss proved holomorphic QUE.” | Holowinsky–Soundararajan, by other methods. |
| “Measure rigidity is Ratner’s theorem.” | Ratner is the unipotent chapter; diagonal higher-rank is a different, partial chapter. |
| “Positive entropy is a minor extra assumption.” | It is the hypothesis that kills the most pathological invariant measures. |
| “Fields 2010 is the same as Abel 2020.” | Abel 2020 honors Furstenberg and Margulis’s lifetime use of dynamics; Lindenstrauss is a later Fields-scale implementation. |

---

## Links

- IMU Fields Medals 2010: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- IMU ICM 2010 laudation (Lindenstrauss): [https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-elon-lindenstrauss.html](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-elon-lindenstrauss.html)
- Wikipedia — Elon Lindenstrauss: [https://en.wikipedia.org/wiki/Elon_Lindenstrauss](https://en.wikipedia.org/wiki/Elon_Lindenstrauss)
- IAS announcement (2024 faculty): [https://www.ias.edu/news/three-world-leading-mathematicians-join-ias-faculty](https://www.ias.edu/news/three-world-leading-mathematicians-join-ias-faculty)
- Soundararajan, QUE for the modular surface (arXiv:0901.4060): [https://arxiv.org/abs/0901.4060](https://arxiv.org/abs/0901.4060)
- arXiv search — Einsiedler Katok Lindenstrauss Littlewood: [https://arxiv.org/search/?query=Einsiedler+Katok+Lindenstrauss+Littlewood&searchtype=all](https://arxiv.org/search/?query=Einsiedler+Katok+Lindenstrauss+Littlewood&searchtype=all)
- AMS Notices survey of the 2010 Fields medals: [https://www.ams.org/notices/201103/rtx110300453p.pdf](https://www.ams.org/notices/201103/rtx110300453p.pdf)

---

## References

1. IMU Fields Medal 2010 citation — Elon Lindenstrauss.
2. M. Einsiedler, A. Katok, and E. Lindenstrauss, “Invariant measures and the set of exceptions to Littlewood’s conjecture,” *Ann. of Math.* 164 (2006).
3. E. Lindenstrauss, “Invariant measures and arithmetic quantum unique ergodicity,” *Ann. of Math.* 163 (2006).
4. Z. Rudnick and P. Sarnak, “The behaviour of eigenstates of arithmetic hyperbolic manifolds,” *Comm. Math. Phys.* 161 (1994) — QUE conjecture.
5. K. Soundararajan, “Quantum unique ergodicity for $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$,” *Ann. of Math.* 172 (2010).
6. R. Holowinsky and K. Soundararajan, “Mass equidistribution for Hecke eigenforms,” *Ann. of Math.* 172 (2010) — holomorphic QUE, different methods.
7. M. Ratner, measure and orbit classification for unipotent flows; H. Furstenberg, $$\times 2,\times 3$$ and disjointness; G. Margulis, unipotent flows and Oppenheim.
8. B. Host and B. Kra, structure theorem for multiple ergodic averages (nilfactors).
9. Course: [Furstenberg & Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/), [Chapter 8 overview]({{ site.baseurl }}/contents/en/chapter08/), [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/).

---

## Further directions

- Read a short exposition of Ratner’s theorem before EKL, so the missing diagonal classification is felt as a gap rather than as a synonym.
- Seminar option: a one-page status sheet “Littlewood after EKL” that lists what a full proof would still need—without inventing one.

## Video tham khảo

- **xem trước** — [Conferências Magnas: Elon Lindenstrauss - Homogeneous dynamics and diagonalizable actions (2013)](https://www.youtube.com/watch?v=e9Gj1yohLCw) — Instituto de Matemática Pura e Aplicada, English. Watch first. “Conferências Magnas: Elon Lindenstrauss - Homogeneous dynamics and diagonalizable actio…” orients the lesson’s aim: Define measure rigidity as “scarce invariant measures, typically algebraic,” and contrast it with the abundance of measures for a single hyperbolic toral automorphism.
- [Elon Lindenstrauss - An effective proof of the Oppenheim Conjecture](https://www.youtube.com/watch?v=_hOglF2XvQ8) — International Centre for Theoretical Sciences, English. A second pass once the main claim is in view: Define measure rigidity as “scarce invariant measures, typically algebraic,” and contrast it with the abundance of measures for a single hyperbolic toral automorphism.
