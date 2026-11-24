---
layout: post
title: "Distributions: Making Dirac Honest"
chapter: '03'
order: 12
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
---

In 1930, while writing his classic textbook on quantum mechanics, physicist Paul Dirac casually introduced an outrageous “function” $$\delta(x)$$: it equals $$0$$ everywhere except $$x = 0$$, spikes to $$+\infty$$ at $$x = 0$$, and somehow encloses a total area of **exactly $$1$$**!

Classical analysts objected immediately: under rigorous Lebesgue integration, any function equal to $$0$$ everywhere except one point *must* have integral $$0$$, never $$1$$! Yet Dirac’s “illegal function” worked astonishingly well—not only in quantum mechanics, but across electrical engineering, signal processing, and PDE Green’s functions. In the late 1940s, Laurent Schwartz finally gave Dirac’s impulse an airtight home—winning the 1950 Fields Medal for **Distribution Theory (Generalized Functions)**.

---

## Background Knowledge Map: What Is Distribution Theory and What Does It Study?

Classical calculus defines a function $$f$$ by specifying its **pointwise value** $$x \mapsto f(x)$$ at every individual point. That viewpoint breaks immediately for natural physical ideals: an instantaneous hammer strike (impulse), a point electron charge, or an abrupt on/off switch (jump discontinuity with no classical derivative at $$t = 0$$).

**Distribution theory** solves this by **flipping the definition** to match how real physical sensors work:
- A real thermometer never measures temperature at a zero-volume mathematical point; it measures a **smooth weighted average** $$\int f(x)\,\varphi(x)\,dx$$ around the probe.
- Instead of asking *“what is the value of $$T$$ at point $$x$$?”*, we define $$T$$ completely by its **measurement outcomes $$\langle T, \varphi \rangle$$ against every infinitely smooth, compactly supported “probe” (test function $$\varphi$$)**.

Through this dual shift, every discontinuous, kinked, or spiky object can be added, differentiated infinitely many times, and Fourier-transformed with 100% rigor.

---

## Learning objectives

After this lecture you should be able to:

- Explain why the classical function $$\delta$$ cannot live in $$L^1_{\mathrm{loc}}$$ yet still “acts” on smooth test functions.
- Define a **distribution** as a continuous linear functional on a space of test functions (slogan: $$T(\varphi)=\langle T,\varphi\rangle$$).
- Differentiate distributions weakly: $$\langle T',\varphi\rangle = -\langle T,\varphi'\rangle$$.
- State the Fourier transform slogan for tempered distributions and why it matters for PDE and QFT heuristics.
- Use a caution table: formal Dirac identities that need hypotheses vs rigorous distribution identities.
- Place distributions in the Physics–Math Bridge as the honesty layer for continuum QM and field theory notation.

**Prerequisites.** One-variable calculus; integration by parts. Multivariable calculus helps. No measure theory required for the map.

---

## 1. The physical demand

Impulse forces, point charges, Green’s functions, and position “eigenstates” all push ordinary functions past their limits. If $$G$$ solves $$-\Delta G = \delta$$ on $$\mathbb{R}^n$$ (in a suitable sense), then convolving with $$G$$ inverts the Laplacian for many sources—the backbone of potential theory and linear PDE.

Dirac’s notation packaged this economy. The cost was that “$$\delta$$ is a function” is false in the classical sense: no locally integrable function has those properties. The mathematical repair is to **change the category of object**, not to force $$\delta$$ into $$L^1$$.

---

## 2. Test functions and distributions

Fix an open set $$\Omega\subset\mathbb{R}^n$$. **Test functions** $$\mathcal{D}(\Omega)=C_c^\infty(\Omega)$$ are smooth functions with compact support. A **distribution** $$T\in\mathcal{D}'(\Omega)$$ is a continuous linear map $$T:\mathcal{D}(\Omega)\to\mathbb{C}$$ (continuity in the appropriate inductive-limit topology—seminar slogan: “if $$\varphi_j\to 0$$ nicely, then $$T(\varphi_j)\to 0$$”).

Every $$f\in L^1_{\mathrm{loc}}(\Omega)$$ defines a regular distribution

$$
\langle f,\varphi\rangle = \int_\Omega f(x)\,\varphi(x)\,dx.
$$

The Dirac mass at $$a\in\Omega$$ is the distribution

$$
\langle \delta_a,\varphi\rangle = \varphi(a).
$$

It is **not** given by integration against a classical function, but it is a perfectly honest continuous linear functional.

---

## 3. Differentiation always works

Define

$$
\langle \partial_i T,\varphi\rangle = -\langle T,\partial_i \varphi\rangle.
$$

Integration by parts with vanishing boundary terms (compact support) motivates the sign. Consequences:

- Every distribution is infinitely differentiable in this weak sense.
- Heaviside step $$H$$ satisfies $$H'=\delta$$ as distributions on $$\mathbb{R}$$.
- Weak (distributional) solutions of PDE are equations in $$\mathcal{D}'$$—the language behind many existence theorems and behind “weak solutions” of Navier–Stokes ([NS essay]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/)).

**One-step mechanism (LO4).** Point sources and jumps become legal when derivatives act on **test functions**, not on the singular object itself.

---

### Deep-Dive Explanation: Differentiating a Jump Discontinuity by Hand in 3 Lines (Read Slowly)

How does distribution theory rigorously prove the engineer’s favorite slogan that “the derivative of a step switch $$H(x)$$ is the Dirac delta $$\delta_0$$”? Follow the exact four-step rescue—and verify two derivatives by hand:

1. **Shift from pointwise values to test-function pairings:** Define the Heaviside step function $$H(x) = 1$$ for $$x > 0$$ and $$0$$ for $$x < 0$$ via its action $$\langle H, \varphi \rangle = \int_0^{\infty} \varphi(x)\,dx$$ on any smooth compactly supported test function $$\varphi$$ (which vanishes at $$\pm\infty$$).
2. **Move the derivative onto $$\varphi$$ by integration by parts:** By definition, $$\langle T', \varphi \rangle := -\langle T, \varphi' \rangle$$. Apply this to $$H$$:
   $$
   \langle H', \varphi \rangle
   = -\langle H, \varphi' \rangle
   = -\int_0^{\infty} \varphi'(x)\,dx
   = -\bigl[\varphi(\infty) - \varphi(0)\bigr]
   = \varphi(0)
   = \langle \delta_0, \varphi \rangle!
   $$
   No dividing by zero, no infinite spikes—just the Fundamental Theorem of Calculus proving **$$H' = \delta_0$$** in one line!
3. **Differentiate the kinked function $$f(x) = \lvert x \rvert$$ twice by hand:**
   - First derivative: $$f'(x) = \operatorname{sign}(x) = 2H(x) - 1$$ (jumps by $$+2$$ at $$x=0$$).
   - Second derivative: $$f'' = 2H' - 0 = 2\delta_0$$! You can double-check by testing against $$\varphi(x) = e^{-x^2}$$ (in Schwartz space): $$\langle f'', \varphi \rangle = 2\varphi(0) = 2$$.
4. **Know the safe boundary:** Every **linear** operation with smooth coefficients (differentiation, shifts, Fourier transforms in $$\mathcal{S}'$$) is 100% legal; **multiplying two singular distributions** (like $$\delta_0^2$$) is generally undefined without microlocal analysis or renormalization.

**Quick check:** Weak solutions in $$\mathcal{D}'$$ are not “sloppy approximate solutions”—they are the rigorous backbone behind Finite Element engineering software and modern PDE theory.

## 4. Multiplication, wavefronts, and danger zones

You may multiply a distribution by a smooth function: $$\langle fT,\varphi\rangle=\langle T,f\varphi\rangle$$. Multiplying **two** arbitrary distributions is not always defined ($$\delta^2$$ is notorious). Hörmander’s wavefront-set calculus and microlocal analysis control when products and restrictions make sense—advanced territory that QFT renormalization brushes against when multiplying operator-valued distributions at coinciding points.

**Seminar rule of thumb.** Linear operations and smooth coefficients: safe distributionally. Nonlinear operations and pointwise products of singular objects: need extra structure.

---

## 5. Tempered distributions and Fourier analysis

**Schwartz space** $$\mathcal{S}$$ of rapidly decreasing smooth functions admits the Fourier transform as an automorphism. Its dual $$\mathcal{S}'$$ consists of **tempered distributions**—including polynomials, $$L^p$$ functions of polynomial growth, and $$\delta$$. Then

$$
\langle \hat T,\varphi\rangle = \langle T,\hat\varphi\rangle
$$

extends Fourier analysis to objects far rougher than classical signals ([Fourier lecture]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/)).

PDE slogan: constant-coefficient linear operators become multiplication by polynomials on the Fourier side; fundamental solutions live naturally in $$\mathcal{S}'$$ or $$\mathcal{D}'$$.

---

## 6. Quantum mechanics and field theory notation

Position kets $$|x\rangle$$ and $$\langle x|x'\rangle=\delta(x-x')$$ are formal; a rigorous reading uses spectral measures of the position operator or rigged Hilbert spaces (Gelfand triples) that place $$\mathcal{S}\subset L^2\subset\mathcal{S}'$$ ([Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/)).

In quantum field theory, Wightman distributions and time-ordered products again live in distribution language; the hard analytic problem is often **defining nonlinear functionals of those distributions** (renormalization)—see [path integrals]({{ site.baseurl }}/contents/en/chapter06/06_20_Path_Integrals_Math_Status/) and [renormalization group]({{ site.baseurl }}/contents/en/chapter06/06_22_Renormalization_Group/).

---

## 7. Precision versus hype (LO6)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “$$\delta$$ is the function that is infinite at 0.” | Heuristic only | It is a distribution, not a classical function. |
| “Distributions make every formal physics calculation rigorous.” | False | Products and nonlinearities can fail. |
| “Weak solutions are fake solutions.” | Misleading | They are solutions in a precise dual sense; uniqueness/regularity are separate questions. |
| “Engineers using $$\delta$$ are being non-mathematical.” | Unfair | Impulse calculus is justified by distribution theory (or Laplace transforms) under stated hypotheses. |

---

## References and further reading

1. Strichartz — *A Guide to Distribution Theory and Fourier Transforms* (gentle).  
2. Rudin — *Functional Analysis* (tempered distributions).  
3. Schwartz — original distribution theory (historical).  
4. Course: [Fourier]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/), [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/), [Path integrals]({{ site.baseurl }}/contents/en/chapter06/06_20_Path_Integrals_Math_Status/), [Mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/).  
