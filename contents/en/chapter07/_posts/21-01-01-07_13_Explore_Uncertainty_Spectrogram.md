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

You will not prove Pauli–Weyl. You will **see** that a short pulse is a wide spectrum, that a window length is not a UI preference, and that Pauli $$X$$ and $$Z$$ refuse to be sharp together.

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

Form three real signals on the same grid: a Gaussian $$e^{-\pi x^2}$$, a box (indicator of $$[-0.4,0.4]$$), and a two-tone $$\cos(2\pi\cdot 1.2 x)+\cos(2\pi\cdot 2.3 x)$$ times a wide Gaussian envelope. Plot $$|f|$$ and $$|\hat f|$$.

**Write:** which pair looks closest to saturating “both sides sharp”? Which looks like the drum-versus-tone cartoon in the lecture?

### Task B — Spectrogram window (25 min)

Build a linear chirp, e.g. $$f(t)=\sin(2\pi(0.5 t + 0.15 t^2))$$. Compute a spectrogram twice: short window, long window (STFT via overlapping FFTs, or `scipy.signal.spectrogram`).

**Write:** which window locates the chirp’s *time* of a given pitch? Which locates the *pitch* at a given time? One sentence connecting this to §8 of the [Fourier lecture]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/).

### Task C — Pauli Robertson (20 min)

Let $$X,Z$$ be Pauli matrices and $$\psi_\theta=(\cos(\theta/2),\,\sin(\theta/2))$$. For a dozen angles in $$[0,\pi]$$, compute $$\sigma_X$$, $$\sigma_Z$$, the product, and $$\tfrac12\bigl|\langle\psi|[X,Z]\psi\rangle\bigr|$$.

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

Estimate second moments of $$|f|^2$$ and $$|\hat f|^2$$ in Task A after centering, and discuss why the numerical product will not match $$1/4\pi$$ unless the FFT convention and the discrete inner product are aligned with the lecture.

---

## See also

- [Uncertainty principles]({{ site.baseurl }}/contents/en/chapter06/06_29_Uncertainty_Principles/)  
- [Fractal uncertainty]({{ site.baseurl }}/contents/en/chapter06/06_30_Fractal_Uncertainty/)  
- [Fourier applications]({{ site.baseurl }}/contents/en/chapter03/03_08_Fourier_Signal_Processing/)  
- [Hilbert / QM]({{ site.baseurl }}/contents/en/chapter06/06_18_Hilbert_Spectral_QM/)  

Pre-approved **A5** alternate (Mode S), same milestones as the other Bridge studios.
