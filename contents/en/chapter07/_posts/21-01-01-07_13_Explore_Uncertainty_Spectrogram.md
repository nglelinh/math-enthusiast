---
layout: post
title: "Studio: Spectrograms, Gaussians, and Uncertainty"
chapter: '07'
order: 13
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Learning path — Uncertainty (hands-on)**  
> **1.** [Fourier applications]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/) §8  
> **2.** [Uncertainty principles]({{ site.baseurl }}/contents/en/chapter06/06_29_Uncertainty_Principles/)  
> **3. You are here:** compute a Fourier pair, a spectrogram trade-off, and a qubit bound  
> *Time guide:* ~60–120 min; numpy/scipy (or any FFT) plus pencil.

Listen closely to two everyday sounds: a crisp handclap and a long, steady note held on a violin. With the handclap, you can pinpoint the *exact instant* it occurred, yet you cannot hum its "pitch" (frequency) as a C or a G—because a short, sharp pulse spreads energy across a broad smear of frequencies. With the sustained violin note, your ear locks onto the exact pitch immediately, yet you cannot point to a single moment in time and say "the note lives *only* here."

Remarkably, that familiar acoustic trade-off is **the very same mathematical law** as Heisenberg's Uncertainty Principle in quantum mechanics. It has nothing to do with clumsy stopwatches or imperfect microscopes; it is an unbreakable constraint woven into waves and Hilbert spaces. In this studio, you will not prove Pauli–Weyl from scratch. Instead, with a few dozen lines of FFT code and a handful of $$2\times 2$$ matrix multiplications, you will **see** all three faces of uncertainty with your own eyes: a short pulse forces a wide spectrum, a spectrogram window length is a physical trade-off rather than a UI preference, and non-commuting Pauli operators $$X$$ and $$Z$$ refuse to be sharp together.

**Lesson roadmap:** Background Knowledge Map (time–frequency analysis, mathematical quantum mechanics & Robertson's inequality) → Deep-Dive Explanation: computing $$\sigma_X\sigma_Z$$ by hand for real and complex qubits (hitting exact equality!) → FFT setup → Spectrogram, chirp & qubit experiments.

---

## Learning objectives

After this studio you should be able to:

- Compare, on a plot, a Gaussian, a box, and a two-tone signal against their discrete Fourier transforms.
- Change an STFT window length on a chirp and describe which axis sharpens.
- Compute $$\sigma_X\sigma_Z$$ for a one-parameter family of qubit states and compare with Robertson’s right-hand side.
- Label observation versus theorem in your log.
- List one misconception you held (e.g. “a nicer window beats uncertainty”).

**Prerequisites.** [Uncertainty literacy]({{ site.baseurl }}/contents/en/chapter06/06_29_Uncertainty_Principles/) §§1–4; complex numbers; an FFT.

---

## Background Knowledge Map: What Are Time–Frequency Analysis and Mathematical Quantum Mechanics, and What Do They Study?

Electrical engineers encounter uncertainty while designing audio filters, radar pulses, and image compression; physicists encounter it in atoms and qubits. Underneath both worlds sit three pillars sharing the same analytic core:

### 1. Time–Frequency Analysis and Spectrograms

A piece of music changes pitch from second to second, so taking a single Fourier transform of the entire recording mixes every note together. To tell *which note played when*, engineers and mathematicians slice the signal with a sliding window of length $$T$$ and compute the Fourier transform on each slice—this is the **Short-Time Fourier Transform (STFT)**, whose magnitude forms a **spectrogram**. The Fourier uncertainty theorem (Gabor / Heisenberg–Pauli–Weyl) enforces a hard lower bound on the product of time spread and frequency spread:
$$
\Delta t \cdot \Delta \xi \ge \frac{1}{4\pi}.
$$
The **Gaussian function** $$f(x) = e^{-\pi x^2}$$ is the unique champion that saturates this bound (because the Fourier transform of a Gaussian is again a Gaussian!).

### 2. Mathematical Quantum Mechanics and Robertson's Inequality

In quantum mechanics, measurable observables are self-adjoint operators $$A, B$$ acting on a Hilbert space. For any normalized state $$\psi$$, **Robertson's inequality** (1929) states:
$$
\sigma_A(\psi)\,\sigma_B(\psi) \ge \frac{1}{2}\,\bigl\lvert \langle \psi \vert [A, B] \psi \rangle \bigr\rvert,
$$
where the commutator is $$[A, B] = AB - BA$$. Whenever $$A$$ and $$B$$ **fail to commute** ($$AB \neq BA$$), algebra itself erects a barrier preventing both measurements from being simultaneously sharp.

### 3. Discrete and Fractal Uncertainty (Modern Extensions)

Even on a finite discrete signal (a DFT of length $$N$$), a vector with $$s$$ nonzero entries whose transform has $$\hat s$$ nonzero entries must satisfy $$s \cdot \hat s \ge N$$ (and when $$N$$ is prime, Terence Tao proved the sharper additive bound $$s + \hat s \ge N + 1$$). This exact principle powers **Compressed Sensing** in modern MRI scanners, letting them reconstruct crisp images from far fewer measurements.

---

### Deep-Dive Explanation (Read Slowly): Verifying Robertson's Inequality by Hand on Real and Complex Qubits

Let's compute every single term by hand for the familiar Pauli matrices:
$$
X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}.
$$
First, evaluate the commutator $$[X, Z] = XZ - ZX$$:
$$
XZ = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad ZX = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \implies [X, Z] = \begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix} = -2iY.
$$
Notice that $$X^2 = I$$ and $$Z^2 = I$$, so for any normalized state $$\psi$$ the standard deviations simplify beautifully: $$\sigma_X = \sqrt{1 - \langle X\rangle^2}$$ and $$\sigma_Z = \sqrt{1 - \langle Z\rangle^2}$$. Now test two concrete states:

1. **Real state $$\psi_\theta = (\cos(\theta/2),\; \sin(\theta/2))^T$$:**
   - At $$\theta = 0$$ ($$\psi_0 = (1, 0)^T$$): $$\langle Z \rangle = 1 \implies \sigma_Z = 0$$; $$\langle X \rangle = 0 \implies \sigma_X = 1$$. The product is $$\sigma_X \sigma_Z = 0$$, and Robertson's right-hand side is also $$0$$.
   - At $$\theta = \pi/4$$: $$\langle Z \rangle = \cos(\pi/4) = \frac{\sqrt{2}}{2} \implies \sigma_Z = \frac{\sqrt{2}}{2}$$; $$\langle X \rangle = \sin(\pi/4) = \frac{\sqrt{2}}{2} \implies \sigma_X = \frac{\sqrt{2}}{2}$$, so **the left-hand side is $$\sigma_X \sigma_Z = 0.5$$**. Now check **the right-hand side**: because $$\psi_\theta$$ has purely real entries, $$\langle \psi_\theta \vert (-2iY) \psi_\theta \rangle = -2i \cdot 0 = \mathbf{0}$$! That is a great experimental catch: along the real $$XZ$$ great circle, the inequality holds ($$0.5 \ge 0$$), yet the commutator bound collapses to zero!
2. **Complex state $$\tilde\psi = \frac{1}{\sqrt{2}}(1,\; i)^T$$ (an eigenstate of $$Y$$):**
   - $$\langle Z \rangle = \frac{1}{2}(1 - 1) = 0 \implies \sigma_Z = 1$$;
   - $$\langle X \rangle = \frac{1}{2}(1\cdot i + (-i)\cdot 1) = 0 \implies \sigma_X = 1$$;
   - **Left-hand side:** $$\sigma_X \sigma_Z = 1 \times 1 = \mathbf{1}$$.
   - **Right-hand side:** $$\frac{1}{2}\bigl\lvert \langle \tilde\psi \vert (-2iY)\tilde\psi \rangle \bigr\rvert = \bigl\lvert \langle \tilde\psi \vert Y \tilde\psi \rangle \bigr\rvert = \bigl\lvert \tfrac{1}{2}(1\cdot 1 + (-i)(i)) \bigr\rvert = \mathbf{1}$$!
   We hit **exact equality $$1 = 1$$**—the state $$\tilde\psi$$ simultaneously maximizes the spreads of $$X$$ and $$Z$$ right on Robertson's lower bound!

---

## 1. Setup

Use any language. The snippets below are Python sketches, not a required library.

```python
import numpy as np

N = 2048
x = np.linspace(-8, 8, N, endpoint=False)
dx = x[1] - x[0]
xi = np.fft.fftshift(np.fft.fftfreq(N, d=dx))

def pair(f):
    fhat = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(f))) * dx
    return f, fhat
```

Conventions in `numpy.fft` are **not** the $$2\pi$$-unitary convention of the lecture. Do not chase the exact $$1/4\pi$$ constant unless you carefully normalize. The studio asks for **shapes and trends**.

---

## 2. Tasks

### Task A — Three Fourier pairs (30 min)

Form three real signals on the same grid: a Gaussian $$e^{-\pi x^2}$$, a box (indicator of $$[-0.4,0.4]$$), and a two-tone $$\cos(2\pi\cdot 1.2 x)+\cos(2\pi\cdot 2.3 x)$$ times a wide Gaussian envelope. Plot $$\lvert f \rvert$$ and $$\lvert \hat f \rvert$$.

**Write:** which pair looks closest to saturating “both sides sharp”? Which looks like the drum-versus-tone cartoon in the lecture? Notice also that the box's transform is a $$\operatorname{sinc}$$ function with slowly decaying oscillating tails—why does a sharp cliff in time force such long tails in frequency?

### Task B — Spectrogram window (25 min)

Build a linear chirp, e.g. $$f(t)=\sin(2\pi(0.5 t + 0.15 t^2))$$. Compute a spectrogram twice: short window, long window (STFT via overlapping FFTs, or `scipy.signal.spectrogram`).

**Write:** which window locates the chirp’s *time* of a given pitch? Which locates the *pitch* at a given time? One sentence connecting this to §8 of the [Fourier lecture]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/).

### Task C — Pauli Robertson (20 min)

Let $$X,Z$$ be Pauli matrices and $$\psi_\theta=(\cos(\theta/2),\,\sin(\theta/2))$$. For a dozen angles in $$[0,\pi]$$, compute $$\sigma_X$$, $$\sigma_Z$$, the product, and $$\tfrac12\bigl\lvert\langle\psi\vert [X,Z]\psi\rangle\bigr\rvert$$. *(Bonus: also test the complex family $$\tilde\psi_\theta = (\cos(\theta/2),\, i\sin(\theta/2))$$ to watch Robertson's right-hand side come alive!)*

**Write:** where is the bound tight? What happens at an eigenstate of $$Z$$?

### Task D — Optional Cantor DFT (15 min)

Build a length-$$N=3^5$$ vector that is 1 on a discrete middle-thirds Cantor set of remaining indices and 0 elsewhere. Plot the magnitude of its DFT. You are **not** proving FUP. You are looking: does the transform look as holey as the set?

### Task E — Log

One error you almost made (e.g. treating energy–time as Kennard, or blaming the “wrong FFT library” for a genuine spread).

---

## 3. Success criteria

| Criterion | Pass |
|-----------|------|
| Pairs | Three plots with a written comparison |
| Spectrogram | Both windows; trade-off named |
| Qubit | Product vs Robertson plotted or tabulated |
| Log | ≥1 misconception noted |
| Honesty | No claim that Task D proves FUP |

---

## 4. Optional stretch

Estimate second moments of $$\lvert f \rvert^2$$ and $$\lvert \hat f \rvert^2$$ in Task A after centering, and discuss why the numerical product will not match $$1/4\pi$$ unless the FFT convention and the discrete inner product are aligned with the lecture.

---

## See also

- [Uncertainty principles]({{ site.baseurl }}/contents/en/chapter06/06_29_Uncertainty_Principles/)  
- [Fractal uncertainty]({{ site.baseurl }}/contents/en/chapter06/06_30_Fractal_Uncertainty/)  
- [Fourier applications]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/)  
- [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/)  

Pre-approved **A5** alternate (Mode S), same milestones as the other Bridge studios.
