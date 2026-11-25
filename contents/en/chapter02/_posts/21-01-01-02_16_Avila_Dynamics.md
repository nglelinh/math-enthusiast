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

Take a humble high-school parabola—$$f_r(x) = r x (1-x)$$—and feed its output back into itself over and over again. For small values of $$r$$, the sequence settles calmly to a single number. Turn the knob past $$r = 3$$, and it bounces forever between two values. Turn it a little further, and it splits into four, then eight, then plunges into full-blown **chaos**—yet hidden inside that chaos are infinitely many tiny windows of calm order!

Now jump to a seemingly unrelated world: an electron hopping along a 1D crystal inside a magnetic field (the **almost Mathieu operator**). Plot its allowed quantum energy levels against the magnetic flux, and a surreal fractal emerges—the **Hofstadter butterfly**. Mark Kac famously offered **ten martinis** to anyone who could prove that for every irrational magnetic flux, those energy levels shatter into a **Cantor set**.

What on earth connects a bouncing quadratic map, a quantum electron in a magnetic field, and billiards on a polygonal table? **Artur Avila**—the first Latin American mathematician to win the Fields Medal—received the **Fields Medal in 2014** for turning **renormalization** (the art of zooming in, rescaling, and seeing the same system reborn at a smaller scale) into a universal dictionary linking all three worlds.

This essay unpacks Avila’s unifying lens with hand-verifiable examples—calculating stability of the logistic map, turning the almost Mathieu operator into a $$2\times 2$$ matrix cocycle, and tracing how renormalization solves problems across dynamics while honoring Avila’s rich web of collaborators (Jitomirskaya, Forni, Viana, de Melo, and Lyubich).

---

## Learning objectives

After this lecture you should be able to:

- State the IMU 2014 citation clearly: **renormalization** as a unifying principle across dynamical systems (not a solo invention by Avila).
- Compute by hand the fixed point and stability of the **logistic map** $$f_r(x) = rx(1-x)$$ at $$r=2.5$$ (attracting) versus $$r=3.2$$ (period-2 bifurcation).
- Rewrite the **almost Mathieu operator** as a $$2\times 2$$ **$$\mathrm{SL}_2(\mathbb{R})$$ Schrödinger cocycle** and explain what the **Ten Martini problem** (Avila–Jitomirskaya) asserts.
- Explain **renormalization** intuitively: passing to a first-return or rescaled map to turn a messy system into a simpler copy of itself.
- Describe **interval exchange transformations (IETs)** and **Teichmüller Lyapunov exponents**, crediting collaborators (**Avila–Forni**, **Avila–Viana**) accurately.
- Avoid media hype: Avila proved deep measure-theoretic ("almost every") theorems for flagship classes rather than "classifying all chaos."

**Prerequisites.** Iterating functions, basic derivatives, $$2\times 2$$ matrices and eigenvalues, and the basic notion of a Cantor set.

**Related lessons.** Dynamics cousins: [Mirzakhani / moduli and Teichmüller]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) (same 2014 class; flat surfaces and moduli). Arithmetic dynamics: [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/).

---

## Key ideas: What Are Dynamical Systems, Renormalization & Cocycles?

If you met differential equations and linear algebra at university, you already hold the starting keys to Avila’s world.

### 1. Dynamical Systems: Watching Rules Repeat Forever
**What is it?** A dynamical system takes a space $$X$$ and a rule $$f: X \to X$$ (discrete time) or a flow $$\phi_t$$ (continuous time), and asks what happens to orbits $$x, f(x), f(f(x)), \dots$$ as time goes to infinity.

**What does it study?**
- **Regular vs. chaotic behavior:** Do orbits settle into a periodic cycle (regular), or spread unpredictably with sensitive dependence on initial conditions (stochastic / chaotic)?
- **Typical ("almost every") behavior:** Because individual orbits can be wildly exotic, modern dynamics asks what happens for *almost every* parameter or initial condition in Lebesgue measure.

### 2. Renormalization: A Microscope on the Space of Systems
**What is it?** Originally born in statistical physics (Kenneth Wilson) and period-doubling chaos (Mitchell Feigenbaum), **renormalization** zooms into a small subregion of a dynamical system, waits for orbits to return to that subregion (**first-return map**), and rescales it back to unit size.

**What does it study?**
- **An operator on systems:** Renormalization maps one dynamical system $$f$$ to a new dynamical system $$\mathcal{R}(f)$$ of the same type. Repeating $$\mathcal{R}$$ reveals universal scaling laws and simplifies tangled long-time behavior into clean local geometry.

### 3. Quasiperiodic Schrödinger Operators & Matrix Cocycles
**What is it?** In quantum mechanics, an electron moving in a crystal with two incommensurate periodicities obeys a discrete Schrödinger equation.

**What does it study?**
- **Transfer matrices (cocycles):** Rewriting a 2nd-order recurrence equation as a product of $$2\times 2$$ determinant-1 matrices $$A_n \in \mathrm{SL}_2(\mathbb{R})$$.
- **Lyapunov exponents & spectra:** How fast the norm $$\|A_n \cdots A_1\|$$ grows exponentially (the **Lyapunov exponent**) determines whether quantum wavefunctions localize or spread—and whether the allowed energy spectrum forms smooth intervals or a fractal **Cantor set**.

---

## 1. Looking again at a smaller scale (and a hand calculation)

### Hand-Verifiable Example 1: Order Turning into Period-2 in the Logistic Map
Take the famous logistic map $$f_r(x) = rx(1-x)$$ on $$[0,1]$$. Find its nonzero fixed point $$f_r(x^*) = x^*$$ by hand:

$$
r x^*(1 - x^*) = x^* \;\Longrightarrow\; 1 - x^* = \frac{1}{r} \;\Longrightarrow\; x^* = 1 - \frac{1}{r}.
$$

Is $$x^*$$ stable (attracting nearby orbits) or unstable (repelling them)? Check the derivative $$f_r'(x) = r(1 - 2x)$$ right at $$x^*$$:

$$
f_r'(x^*) = r\left(1 - 2\left(1 - \frac{1}{r}\right)\right) = 2 - r!
$$

Now plug in two concrete values of $$r$$:
1. **$$r = 2.5$$:** Fixed point $$x^* = 1 - \frac{1}{2.5} = 0.6$$, and $$\lvert f'_{2.5}(0.6)\rvert = \lvert 2 - 2.5\rvert = 0.5 < 1$$. Every nearby point is **pulled straight into $$0.6$$** (regular attracting behavior!).
2. **$$r = 3.2$$:** Fixed point $$x^* = 1 - \frac{1}{3.2} = 0.6875$$, and $$\lvert f'_{3.2}(0.6875)\rvert = \lvert 2 - 3.2\rvert = 1.2 > 1$$! The fixed point turns **repelling**, and orbits split into a stable **period-2 cycle** bouncing forever between $$0.5130\dots$$ and $$0.7995\dots$$!

Keep turning $$r$$ up past $$3.449\dots$$, $$3.544\dots$$, and you witness Feigenbaum’s period-doubling cascade into chaos. In 2003, **Avila, Welington de Melo, and Mikhail Lyubich** used renormalization to prove the celebrated **regular-or-stochastic dichotomy**: for almost every parameter in a real-analytic unimodal family, the map is *either* regular (an attracting cycle) *or* stochastic (chaotic with an absolutely continuous invariant measure).

---

## 2. The almost Mathieu operator and the Ten Martini problem

The **almost Mathieu operator** on $$\ell^2(\mathbb{Z})$$ is

$$
(H_{\lambda,\alpha}\psi)_n = \psi_{n+1} + \psi_{n-1} + 2\lambda\cos(2\pi n\alpha)\,\psi_n,
$$

with coupling $$\lambda \in \mathbb{R}$$ and frequency $$\alpha$$.

### Hand-Verifiable Example 2: Turning a Quantum Equation into a $$2\times 2$$ Matrix Cocycle
How does a quantum eigenvalue equation $$H_{\lambda,\alpha}\psi = E\psi$$ become a dynamical system? Solve for $$\psi_{n+1}$$:

$$
\psi_{n+1} = \bigl(E - 2\lambda\cos(2\pi n\alpha)\bigr)\psi_n - \psi_{n-1}.
$$

Stack $$\psi_n$$ and $$\psi_{n-1}$$ into a 2D vector! You instantly get an exact $$2\times 2$$ matrix update:

$$
\begin{pmatrix} \psi_{n+1} \\ \psi_n \end{pmatrix}
=
\underbrace{\begin{pmatrix} E - 2\lambda\cos(2\pi n\alpha) & -1 \\ 1 & 0 \end{pmatrix}}_{A(n\alpha)}
\begin{pmatrix} \psi_n \\ \psi_{n-1} \end{pmatrix}.
$$

Check the determinant by hand: $$\det A(n\alpha) = (E - 2\lambda\cos(2\pi n\alpha))\cdot 0 - (-1)(1) = 1$$! So $$A(\theta)$$ always lives in **$$\mathrm{SL}_2(\mathbb{R})$$**! Stepping from $$n$$ to $$n+1$$ simply rotates the angle $$\theta \mapsto \theta + \alpha$$ and multiplies by $$A(\theta)$$—a **quasiperiodic $$\mathrm{SL}_2(\mathbb{R})$$ cocycle**!

In 2009 (*Annals of Mathematics*), **Artur Avila and Svetlana Jitomirskaya** solved Mark Kac’s **Ten Martini problem** completely: for **every irrational $$\alpha$$** and **every nonzero $$\lambda$$**, the spectrum of $$H_{\lambda,\alpha}$$ is a **Cantor set** (closed, nowhere dense, with no isolated points).

---

### Explanation: How Renormalization Unifies Avila’s Three Worlds

Why did the IMU call renormalization a **unifying principle** across Avila’s work? Follow the four-step logic connecting three seemingly separate fields:

#### Step 1: Identify the "microscopic" return or frequency-scaling move
Every one of Avila’s arenas has a natural zoom-in operation:
- **Unimodal maps:** Replace $$f$$ by its rescaled return map $$f^2$$ near the critical point.
- **Interval exchange transformations (IETs):** Cut off the rightmost subinterval and watch the first-return map (**Rauzy–Veech induction**), which is itself a new IET—and geometrically equals stepping forward along the **Teichmüller geodesic flow**!
- **Schrödinger cocycles:** Replace the irrational rotation $$\alpha$$ by its continued-fraction renormalization (passing to close return times $$q_k$$ where $$q_k \alpha \approx p_k$$).

#### Step 2: Complexify and track Lyapunov exponents (Avila’s global theory)
For one-frequency cocycles $$A(\theta)$$, Avila had a dazzlingly simple yet revolutionary idea: shift the real phase $$\theta$$ into the complex plane, $$\theta \mapsto \theta + i\varepsilon$$, and study the Lyapunov exponent $$L(\varepsilon)$$ as a function of $$\varepsilon$$! He proved **quantization of acceleration**: the slope $$\frac{dL}{d\varepsilon}$$ is always an **integer**! That single rigidity theorem splits every energy $$E$$ cleanly into three regimes: **subcritical** (almost reducible to constant rotations), **critical**, and **supercritical** (positive Lyapunov exponent).

#### Step 3: Bridge the Diophantine vs. Liouville divide
In the Ten Martini problem, earlier proofs split in two: "well-approximable" (Liouville) irrationals fell to periodic approximations, while "badly approximable" (Diophantine) irrationals fell to KAM/localization methods—leaving an impossible no-man’s-land in between. Avila and Jitomirskaya used **almost reducibility** (via renormalization) and **Aubry duality** to close the gap across *all* irrationals and *all* couplings $$\lambda \neq 0$$.

#### Step 4: Turn renormalization ergodicity into "almost every" global theorems
The same renormalization microscope yielded two more landmarks:
- **Avila–Forni (2007):** Proved that almost every non-rotational interval exchange transformation is **weakly mixing** (no hidden periodic clocks!).
- **Avila–Viana (2007):** Proved the **Zorich–Kontsevich conjecture**: all nontrivial Lyapunov exponents of the Teichmüller geodesic flow on moduli spaces of Abelian differentials are **distinct (simple)**!

In one schematic line:

$$
\text{Zoom \& rescale (renormalization)}
\;\longrightarrow\;
\begin{cases}
\text{Unimodal maps: regular or stochastic (Avila–de Melo–Lyubich)} \\
\text{Schrödinger cocycles: global theory \& Ten Martini (Avila–Jitomirskaya)} \\
\text{IETs / Teichmüller flow: weak mixing \& simple exponents (Avila–Forni, Avila–Viana)}
\end{cases}
$$

---

## 3. Honest attribution

The 2014 IMU news release explicitly highlights Avila’s remarkably collaborative style—working with roughly thirty coauthors across Brazil, France, and the world:

| Result (slogan) | Credit |
|-----------------|--------|
| Regular vs. stochastic typical unimodal maps | Avila–de Melo–Lyubich (2003) |
| Weak mixing of almost every IET / translation flow | Avila–Forni (2007) |
| Cantor spectrum of almost Mathieu (Ten Martini) | Avila–Jitomirskaya (*Annals*, 2009) |
| Simplicity of Lyapunov exponents of Teichmüller flow | Avila–Viana (Zorich–Kontsevich) |
| Global theory of one-frequency Schrödinger operators | Avila (and a broad spectral-theory community) |
| Renormalization as a concept | Wilson, Feigenbaum, Sullivan, Lyubich, Yoccoz, … |

Avila grew up in Rio de Janeiro, earned his PhD at **IMPA** at age 21 under **Welington de Melo**, and went on to CNRS (Paris) and the University of Zurich—becoming the **first Brazilian** (and first Latin American) Fields Medalist.

---

## 4. Why a Fields Medal

Three reasons explain the 2014 award without resorting to hype:
1. Closing the Diophantine–Liouville no-man’s-land to finish **Ten Martini** (with Jitomirskaya).
2. Turning **renormalization** and **global cocycle theory** into a unified default language across three major branches of dynamics.
3. Proving sharp measure-theoretic ("almost every") laws—weak mixing of IETs, regular/stochastic unimodal maps, simple Teichmüller Lyapunov exponents—where pointwise classification is hopeless.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Avila invented renormalization.” | The idea is older (Wilson, Feigenbaum, Sullivan, …); Avila unified major branches of dynamics with it. |
| “He classified all dynamical systems.” | He proved deep measure-theoretic theorems for specific, central classes. |
| “Ten Martini is Avila’s alone.” | It is joint work: **Avila–Jitomirskaya**. |
| “The spectrum is a Cantor set for every Schrödinger operator.” | Ten Martini is for the almost Mathieu family (and later extensions); general operators have richer spectra. |
| “Weak mixing is the same as mixing.” | IETs are never strongly mixing; Avila–Forni proves *weak* mixing for typical exchanges. |
| “Lyapunov exponents of Teichmüller flow are Avila’s solo theorem.” | Simplicity is **Avila–Viana**, settling the Zorich–Kontsevich conjecture. |

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

## Video tham khảo

- **xem trước** — [Dynamical Systems and Renormalisation by Prof. Artur Avila](https://www.youtube.com/watch?v=F3e5g5BwDu8) — swissQuant, English. Watch first. “Dynamical Systems and Renormalisation by Prof. Artur Avila” orients the lesson’s aim: State the IMU 2014 citation in one careful sentence, with renormalization as a unifying tool rather than a personal invention.
- [Artur Avila - Poincaré series and renormalization MCA 2013](https://www.youtube.com/watch?v=Hff4sJm0xBA) — MCA2013, English. A second pass once the main claim is in view: State the IMU 2014 citation in one careful sentence, with renormalization as a unifying tool rather than a personal invention.
- [Fields Medal Winner 2014 Artur Avila](https://www.youtube.com/watch?v=405_UtglyoQ) — International Mathematical Union, English. Further depth after the first two, still tied to this lesson: State the IMU 2014 citation in one careful sentence, with renormalization as a unifying tool rather than a personal invention.
