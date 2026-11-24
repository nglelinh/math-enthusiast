---
layout: post
title: "Uncertainty Principles: Fourier, Heisenberg, and Information"
chapter: '06'
order: 29
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

Listen to two everyday sounds: a crisp handclap lasting a few milliseconds, and a long, steady flute note. With the handclap, you know *precisely* when it happened, yet nobody can sing its musical pitch—it has no definite frequency! With the sustained flute note, you immediately hear its pitch ($$440\text{ Hz}$$, concert A), yet asking "at which exact millisecond did that note occur?" makes no sense. Those two musical facts **are already an uncertainty principle**, and not a single atom has entered the room.

When Werner Heisenberg introduced his famous principle in 1927, popular accounts blamed a clumsy microscope kicking an electron during measurement. The mathematical truth runs deeper: quantum mechanics inherits this exact wave limit directly from **Fourier analysis**, because a particle's position wavefunction and momentum wavefunction are a **Fourier pair**. Planck's constant $$\hbar$$ merely converts units; the inequality itself is pure analysis.

This lecture maps four faces of the same law—the **Fourier form**, the **Heisenberg–Kennard form**, the general **Robertson commutator bound**, and the **entropic information-theoretic upgrade**—sitting after [Hilbert space QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/) and alongside [Fourier in the world]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/). The 2025 fractal upgrade lives in the companion essay.

---

## Background Knowledge Map: What Three Pillars Unify Uncertainty Principles?

With undergraduate Fourier transforms and the Cauchy–Schwarz inequality, three pillars reveal the entire landscape of uncertainty theorems:

### 1. Harmonic Analysis: Time–Frequency Trade-Offs
Every signal $$f(x)$$ wears two dual faces: its spatial/time profile ($$|f(x)|^2$$) and its frequency/momentum spectrum ($$|\hat f(\xi)|^2$$). Measuring spread by variance yields the **Heisenberg–Pauli–Weyl** (and **Kennard** $$\sigma_x\sigma_p \ge \hbar/2$$) bound, saturated uniquely by **Gaussian** bell curves—governing radar resolution, audio spectrograms, and sparse signal recovery (Donoho–Stark / compressed sensing).

### 2. Noncommutative Algebra: Commutators and the Robertson Bound
In Hilbert space, *any* pair of noncommuting self-adjoint observables ($$[A, B] \neq 0$$, such as Pauli spin operators $$X, Z$$ or $$[X,P] = i\hbar$$) obeys a universal lower bound from Cauchy–Schwarz: **Robertson's inequality**. Handling the domains of unbounded operators leads to the **Weyl relations** and the **Stone–von Neumann uniqueness theorem**.

### 3. Information Theory: Entropic Uncertainty
Variance has a blind spot: two razor-thin spikes placed far apart have huge variance despite being tightly localized! **Entropic uncertainty** (Hirschman, Beckner, Maassen–Uffink) fixes that blind spot and underwrites security proofs in **quantum cryptography** (such as BB84).

---

## Learning objectives

After this lecture you should be able to:

- State a **Fourier uncertainty inequality** (Pauli–Weyl) and name Gaussians as minimizers.
- Write the **Kennard** bound $$\sigma_x\sigma_p\ge\hbar/2$$ and say which convention on $$\hbar$$ you are using.
- Derive the **Robertson** slogan $$\sigma_A\sigma_B\ge\tfrac12\bigl|\langle[A,B]\rangle\bigr|$$ from Cauchy–Schwarz (centered observables).
- Distinguish **canonical commutation relations** from the **Weyl** form and quote **Stone–von Neumann** as a uniqueness slogan, not a calculation you must finish.
- Refuse three mixups: observer-effect microscope as the theorem; energy–time as the same CCR; uncertainty as chaos or as thermodynamic entropy.
- State one **entropic** complementarity slogan that links to [quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/).

**Prerequisites.** Inner products; the idea of a Fourier transform ([Ch.3]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/)); self-adjoint operators as observables ([Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/)). No distribution theory required.

---

## 1. Not only quantum

A sinusoid that lasts forever is a spike in frequency and is nowhere localized in time. A Dirac pulse is perfectly timed and has a flat spectrum. Any honest interpolation lives in between: squeezing $$f(x)$$ to $$f(ax)$$ (narrower by $$a$$) stretches its Fourier transform to $$\frac{1}{|a|}\hat f(\xi/a)$$ (wider by $$a$$).

![A narrow pulse has a wide spectrum; a long tone has a sharp spectrum]({{ site.baseurl }}/img/chapter_img/uncertainty_time_freq_pairs.png)

*Figure. Dual sharpness is forbidden. Top: a short pulse and its spread-out Fourier transform. Bottom: a long almost-pure tone and two frequency spikes (cosine).*

This is the 3Blue1Brown moral, and it is the right on-ramp. Radar pulses, musical notes, and windowed spectrograms in the [Fourier applications lecture]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/) are the same geometry. Quantum mechanics is the case where the dual variable is **momentum**.

---

## 2. The Fourier inequality

Fix the unitary-friendly convention

$$
\hat f(\xi)=\int_{-\infty}^{\infty} f(x)\,e^{-2\pi i x\xi}\,dx,
$$

with inversion the same formula up to a sign in the exponent (on Schwartz functions, then by density on $$L^2$$). Write $$\|g\|_2^2=\int |g|^2$$. The **Heisenberg–Pauli–Weyl** inequality says that if $$f$$ is nice enough that the moments exist,

$$
\Bigl(\int x^2|f(x)|^2\,dx\Bigr)^{1/2}
\Bigl(\int \xi^2|\hat f(\xi)|^2\,d\xi\Bigr)^{1/2}
\ge \frac{1}{4\pi}\,\|f\|_2^2.
$$

If $$f$$ is centered so that the means of $$x$$ and $$\xi$$ vanish, the two factors are ordinary standard deviations in time and frequency. The constant $$1/4\pi$$ is tied to the $$2\pi$$ in the exponent; change the Fourier convention and the constant changes with it. What does **not** change is the phenomenon: you cannot send both factors to zero unless $$f=0$$.

**Minimizers.** Equality holds for **Gaussians**. In this normalization the function $$e^{-\pi x^2}$$ is its own Fourier transform. Translating, modulating, or scaling produces the remaining minimizers (adding a linear chirp $$e^{i\alpha x^2}$$ saturates only the stronger Schrödinger form, not this variance product). No other $$L^2$$ shapes saturate the bound.

![A Gaussian and its Fourier transform, the same shape]({{ site.baseurl }}/img/chapter_img/uncertainty_gaussian_minimizer.png)

*Figure. The unique (modulo the symmetries above) functions that are as localized as the inequality allows.*

**Intuition.** Integration by parts gives $$\|f\|_2^2 = -2\operatorname{Re}\langle xf, f'\rangle \le 2\|xf\|_2 \|f'\|_2$$ by Cauchy–Schwarz; Plancherel converts $$\|f'\|_2$$ into $$2\pi\|\xi\hat f\|_2$$, yielding $$1/(4\pi)$$ on the spot.

---

## 3. Position, momentum, Kennard

A particle on the line has a unit wavefunction $$\psi\in L^2(\mathbb{R})$$. Born’s rule reads $$|\psi(x)|^2$$ as a probability density for position. The momentum-space wavefunction is the Fourier transform with the physical frequency $$p/\hbar$$:

$$
\phi(p)=\frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty}\psi(x)\,e^{-ipx/\hbar}\,dx.
$$

Then $$|\phi(p)|^2$$ is the probability density for momentum. Because $$\psi$$ and $$\phi$$ are a Fourier pair, the analysis inequality becomes **Kennard’s form of Heisenberg’s principle** (1927, cleaned by Kennard and Weyl):

$$
\sigma_x\,\sigma_p \ge \frac{\hbar}{2}.
$$

Here $$\sigma_x^2=\langle X^2\rangle-\langle X\rangle^2$$ with $$X$$ multiplication by $$x$$, and $$\sigma_p$$ is the same construction for $$P=-i\hbar\frac{d}{dx}$$. Popular texts sometimes write $$h/4\pi$$; that is the same statement because $$\hbar=h/2\pi$$.

The constant is not a laboratory fudge factor. Once you accept (i) states as $$L^2$$ unit vectors, (ii) Born’s rule, and (iii) de Broglie’s identification of momentum with frequency, the inequality is a theorem.

---

## 4. Robertson: uncertainty is a commutator

Kennard is a special case. Let $$A$$ and $$B$$ be self-adjoint (on a common dense domain, with the usual domain caveats). Write $$\sigma_A^2=\bigl\|(A-\langle A\rangle)\psi\bigr\|^2$$ and likewise for $$B$$. Shifting by the means, one may assume $$\langle A\rangle=\langle B\rangle=0$$. Then

$$
\bigl|\langle\psi|[A,B]\psi\rangle\bigr|
= 2\bigl|\operatorname{Im}\langle A\psi,B\psi\rangle\bigr|
\le 2\,\|A\psi\|\,\|B\psi\|,
$$

which is Cauchy–Schwarz. Therefore

$$
\sigma_A\,\sigma_B \ge \frac12\bigl|\langle[A,B]\rangle\bigr|.
$$

This is **Robertson’s relation**. The stronger **Schrödinger** form adds a covariance term on the right-hand side; we will not need it.

If $$[X,P]=i\hbar$$, the right-hand side is $$\hbar/2$$ and Kennard returns. If $$A$$ and $$B$$ commute on the state, the bound is vacuous: both can be sharp together (think of two components of spin along the same axis, or of $$X$$ with itself). Uncertainty is not “everything is fuzzy.” It is **noncommutativity, quantified**.

![Bloch-plane cartoon: a state cannot sit on both the X and Z axes]({{ site.baseurl }}/img/chapter_img/uncertainty_robertson_pauli.png)

*Figure. Qubit toy. Pauli matrices satisfy $$[X,Z]=-2iY$$, so $$\sigma_X\sigma_Z\ge|\langle Y\rangle|$$. An eigenstate of $$Z$$ has $$\sigma_Z=0$$ and maximal spread in $$X$$.*

---

## 5. CCR, Weyl relations, Stone–von Neumann

The **canonical commutation relation**

$$
[X,P]=i\hbar I
$$

cannot hold for bounded operators on a Hilbert space (in finite dimensions, taking traces immediately gives $$0 = i\hbar n$$, a contradiction!). So $$X$$ and $$P$$ are **unbounded**, and the identity is an equality of operators on a specified domain. The safer package is the **Weyl form**: the one-parameter unitary groups $$U(a)=e^{-iaP/\hbar}$$ (translations) and $$V(b)=e^{-ibX/\hbar}$$ (modulations) satisfy

$$
U(a)V(b)=e^{-iab/\hbar}\,V(b)U(a).
$$

**Stone–von Neumann (slogan).** Any irreducible representation of the Weyl relations on a separable Hilbert space is unitarily equivalent to the Schrödinger representation on $$L^2(\mathbb{R}^n)$$. In that sense “position and momentum on the line” have only one quantum theory.

**What the slogan does not say.** Infinite degrees of freedom (fields) escape uniqueness—that is one reason [operator algebras]({{ site.baseurl }}/contents/en/chapter06/06_24_Operator_Algebras_QM/) appear. Domains, essential self-adjointness, and the difference between formal CCR and Weyl relations are exactly the issues the [Hilbert lecture]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/) flagged.

---

## 6. Energy–time is not the same theorem

There is no self-adjoint **time operator** $$T$$ on the usual Hilbert space that satisfies $$[H,T]=i\hbar$$ for a Hamiltonian bounded from below. Pauli already noted the obstruction: the Weyl relations would force the spectrum of $$H$$ to be all of $$\mathbb{R}$$. So the popular slogan $$\Delta E\,\Delta t\ge\hbar/2$$ is **not** Robertson applied to $$(H,T)$$.

Useful replacements exist and are different theorems. **Mandelstam–Tamm**, for example, bounds how fast a state can become orthogonal to itself: if $$\tau$$ is the time to reach overlap zero, then $$\tau\,\sigma_H\ge\hbar/2$$ (with sharp constant $$\pi\hbar/2$$). That is a speed limit, not a simultaneous-measurement claim about a time observable.

**Preparation versus disturbance.** Heisenberg’s 1927 γ-ray microscope story is about a measurement kicking a particle. The Kennard/Robertson inequality is about the **spread of a prepared state** in two noncommuting observables, with no apparatus in the sentence. Modern measurement-disturbance inequalities (Ozawa and later work) are a separate, more technical layer; this course maps them, it does not prove them.

---

## 7. Entropic complementarity

Variances can mislead. A density with two distant spikes has huge variance while still being “localized on a small set.” **Entropy** sees support size more honestly. Hirschman conjectured, and Beckner and Białynicki-Birula–Mycielski proved, an entropic Fourier inequality: the Shannon entropies of $$|\psi|^2$$ and $$|\phi|^2$$ cannot both be small.

In finite dimensions the clean statement is **Maassen–Uffink**. If you measure a state in two orthonormal bases $$\{|a_i\rangle\}$$ and $$\{|b_j\rangle\}$$, and if $$c=\max_{i,j}|\langle a_i|b_j\rangle|$$, then

$$
H(A)+H(B)\ge -2\log c,
$$

where $$H$$ is Shannon entropy of the outcome distribution. Computational-basis versus Hadamard-basis measurements of a qubit have $$c=1/\sqrt{2}$$, so the two outcome entropies sum to at least one bit.

### Deep-Dive Explanation: Comparing Robertson vs. Maassen–Uffink by Hand on a Qubit (Read Slowly)

Pick a concrete qubit state $$\psi = \begin{pmatrix} \sqrt{3}/2 \\ 1/2 \end{pmatrix}$$ (angle $$\theta = \pi/3$$ on the Bloch sphere) and measure Pauli $$Z = \operatorname{diag}(1, -1)$$ and $$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$:

1. **Compute standard deviations $$\sigma_Z$$ and $$\sigma_X$$:**
   - For $$Z$$: $$\langle Z \rangle = \frac{3}{4} - \frac{1}{4} = \frac{1}{2}$$; since $$Z^2 = I$$, $$\sigma_Z = \sqrt{1 - (1/2)^2} = \frac{\sqrt{3}}{2} \approx 0.866$$.
   - For $$X$$: $$\langle X \rangle = 2\cdot\frac{\sqrt{3}}{2}\cdot\frac{1}{2} = \frac{\sqrt{3}}{2}$$; since $$X^2 = I$$, $$\sigma_X = \sqrt{1 - 3/4} = \frac{1}{2} = 0.5$$.
   - Product: $$\sigma_X\sigma_Z = \frac{\sqrt{3}}{4} \approx 0.433$$.
2. **Check Robertson's right-hand side $$\frac{1}{2}|\langle[X,Z]\rangle| = |\langle Y\rangle|$$:** Because $$\psi$$ is purely real while $$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$$ is purely imaginary and skew-symmetric, $$\langle \psi|Y\psi\rangle = 0$$! So at this state, Robertson collapses to the trivial statement $$0.433 \ge 0$$!
3. **Now compute base-2 Shannon entropies for the exact same state:**
   - Measuring $$Z$$ gives outcome probabilities $$(3/4,\ 1/4)$$:
     $$
     H(Z) = -\frac{3}{4}\log_2\frac{3}{4} - \frac{1}{4}\log_2\frac{1}{4} \approx 0.811\text{ bit}.
     $$
   - Measuring $$X$$ (projecting onto $$|\pm\rangle = \frac{1}{\sqrt{2}}(1,\pm 1)^T$$) gives probabilities $$\frac{1\pm\sqrt{3}/2}{2} \approx (0.933,\ 0.067)$$:
     $$
     H(X) \approx -0.933\log_2(0.933) - 0.067\log_2(0.067) \approx 0.355\text{ bit}.
     $$
   - Total: $$H(Z) + H(X) \approx 1.166\text{ bit} \ge 1\text{ bit}$$!
4. **The takeaway:** Right where Robertson's lower bound drops to zero, **Maassen–Uffink** still enforces a rock-solid, state-independent $$1\text{ bit}$$ floor—which is why [quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/) and quantum cryptography build their security proofs on entropic uncertainty.

---

## 8. A map of nearby theorems (not extra lectures)

| Variant | Slogan | Status |
|---------|--------|--------|
| Donoho–Stark (1989) | A length-$$N$$ discrete signal cannot be concentrated on $$n_t$$ time bins and $$n_\omega$$ frequency bins unless $$n_t n_\omega\ge N$$ | Theorem; used in sparse recovery |
| Hardy / Beurling–Hörmander | If $$f$$ and $$\hat f$$ both decay faster than a critical Gaussian, then $$f=0$$ | Theorem |
| Balian–Low | A well-localized Gabor frame cannot be generated by a single window that is sharp in both time and frequency | Theorem |
| Landau–Pollak–Slepian | Dimension of approximately time- and band-limited functions; prolate spheroidal wave functions | Theorem |
| [Fractal uncertainty]({{ site.baseurl }}/contents/en/chapter06/06_30_Fractal_Uncertainty/) | $$f$$ and $$\hat f$$ cannot both live near line-porous fractals | Theorem in 1D (2016) and in higher D under line porosity (Cohen 2025) |

Pontryagin duality’s smoothness-versus-decay row in the [Fourier/Pontryagin bridge]({{ site.baseurl }}/contents/en/chapter06/06_16_Pontryagin_Fourier_Duality/) is the same trade-off in group language. Short-time Fourier windows in Chapter 3 are the inequality made into an instrument: pick the spread you can tolerate.

---

## 9. Precision versus hype

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Measuring position kicks the particle, therefore $$\sigma_x\sigma_p\ge\hbar/2$$.” | Wrong reason | The inequality is about a prepared state’s two spreads. Disturbance is a different theorem. |
| “Every pair of quantities is uncertain by $$h/2$$.” | False | Only noncommuting pairs; the bound is $$\tfrac12\vert\langle[A,B]\rangle\vert$$. |
| “Energy–time is the same CCR as $$x,p$$.” | False | No standard self-adjoint time operator. Use Mandelstam–Tamm or name the variant. |
| “Uncertainty is chaos / the second law.” | False | Sensitive dependence and thermodynamic entropy are other subjects ([chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/)). |
| “Gaussians are just a convenient example.” | Incomplete | They are the **minimizers**. |

---

## References and further reading

- 3Blue1Brown — [The more general uncertainty principle](https://www.youtube.com/watch?v=MBnnXbOM5S4) (2018); [lesson page](https://www.3blue1brown.com/lessons/uncertainty-principle/).
- Hall — *Quantum Theory for Mathematicians* (CCR, Robertson, domains).
- Wolff — [The uncertainty principle: variations on a theme](https://arxiv.org/html/2006.11206v3).
- Donoho–Stark — [Uncertainty principles and signal recovery](https://epubs.siam.org/doi/10.1137/0149053), *SIAM J. Appl. Math.* 1989.
- Maassen–Uffink, *Phys. Rev. Lett.* **60** (1988).
- Course: [Fourier]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/), [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/), [QI]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/), [Fractal UP]({{ site.baseurl }}/contents/en/chapter06/06_30_Fractal_Uncertainty/), [studio]({{ site.baseurl }}/contents/en/chapter07/07_13_Explore_Uncertainty_Spectrogram/).
- Pack: `research/video-research/uncertainty-principles/`.
