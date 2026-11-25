---
layout: post
title: "Fourier Analysis → Signal Processing"
chapter: '03'
order: 8
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
lesson_type: required
---

When a pianist strikes a C–E–G chord, the speaker cone vibrates along **one single** wiggly pressure curve. Yet your ear—and a smartphone running Shazam—effortlessly pulls the three individual notes back out of that tangled waveform.

That “un-blending a smoothie back into separate fruits” magic is **Fourier Analysis**. Born in the early nineteenth century from Joseph Fourier’s study of heat conduction in a metal bar, the idea of decomposing signals into pure sines and cosines now runs quietly beneath nearly all digital technology: JPEG images, MP3 audio, 4G/5G/Wi-Fi wireless links, and hospital MRI scanners.

---

## Key ideas: What Is Fourier Analysis and What Does It Study?

If linear algebra teaches you to rotate coordinate axes in 3D space so a shape looks simpler, **Fourier analysis (harmonic analysis)** does the exact same thing for **spaces of functions and signals**.

Instead of describing a sound clip by air pressure at every millisecond (the time domain), Fourier analysis projects it onto an orthogonal coordinate system of pure frequencies $$e^{i\omega t}$$ (the frequency domain). That single change of basis is extraordinarily powerful for three reasons:

1. **Calculus becomes algebra:** Differentiation and convolution (filtering) in time turn into ordinary **pointwise multiplication** in frequency.
2. **Natural signals become sparse:** Photos and speech look dense in pixels or time samples, yet pack almost all their energy into a handful of frequency coefficients—making JPEG and MP3 compression possible.
3. **The Fast Fourier Transform (FFT):** Drops computational cost from $$O(N^2)$$ to $$O(N\log N)$$, fast enough to run in real time inside wireless earbuds.

Depending on the signal domain, the family splits into four tools: **Fourier series** (periodic continuous), **Fourier transform** (non-periodic continuous), **DFT/FFT** (finite digital arrays), and **STFT/Wavelets** (time-varying frequencies like music).

---

## Learning objectives

After this lecture you should be able to:

- Explain a signal as a superposition of oscillatory modes (sines/cosines or complex exponentials).
- State the idea of **Fourier series** on a circle/interval and **Fourier transform** on the line.
- Describe the **DFT** and why the **FFT** made digital signal processing practical.
- Give one-step mechanisms for compression (JPEG-style), filtering, and MRI frequency-space acquisition.
- Relate sampling rate to representable frequencies at slogan level (Nyquist idea).
- Avoid “Fourier is only music EQ” and “JPEG just deletes random pixels.”

**Prerequisites.** Integrals, complex numbers $$e^{i\theta}=\cos\theta+i\sin\theta$$ helpful. [Calculus]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/) continuum intuition.

**Seminar links.** [Wang harmonic analysis]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/), [DEs]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/) (separation of variables).

---

## 1. Frequency as a coordinate system

A pure tone is a sinusoid. A pure spatial stripe is a 2D sinusoid. Most real signals are mixtures: speech stacks formants; images stack edges and textures; heartbeats stack quasi-periodic components plus noise.

Fourier analysis supplies an orthonormal (or orthogonal) **basis of oscillations** and coefficients that say how much of each frequency is present. Changing basis does not lose information when the transform is invertible; it **reorganizes** information so that tasks become easy—compression, denoising, modulation, solving constant-coefficient PDEs.

**Mechanism slogan.**  
*Many operations that are complicated in time/space are multiplications or simple masks in frequency—and vice versa (convolution theorem).*

---

## 2. Fourier series: periodic worlds

For a nice function $$f$$ on $$[0,2\pi]$$ (or periodic on the circle),

$$
f(\theta)\sim\sum_{n=-\infty}^{\infty} \hat f(n)\,e^{in\theta},
\qquad
\hat f(n)=\frac1{2\pi}\int_0^{2\pi} f(\theta)e^{-in\theta}\,d\theta.
$$

Coefficients $$\hat f(n)$$ are inner products against pure harmonics. Partial sums are band-limited approximations. Gibbs ringing near jumps is a classical warning: truncation in frequency creates overshoot in space.

**Heat equation connection.** Expanding initial data in Fourier series turns $$\partial_t u=\kappa\partial_{xx}u$$ into independent ODEs for each mode: high frequencies decay faster. Separation of variables is Fourier analysis applied to [differential equations]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/).

---

### Short video: Building a square wave from sines

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/square-wave-fourier_en.mp4"></video>
</div>

Adding odd sine waves with shrinking amplitude builds a square wave. The overshoot at the jump (the Gibbs effect) does not disappear when more waves are added.


### Try it yourself: Add sine waves yourself

<div class="mex-explainer" data-mex="fourier" data-lang="en"></div>


## 3. Fourier transform: non-periodic signals

On the real line,

$$
\hat f(\xi)=\int_{-\infty}^{\infty} f(x)e^{-2\pi i x\xi}\,dx,
\qquad
f(x)=\int_{-\infty}^{\infty}\hat f(\xi)e^{2\pi i x\xi}\,d\xi
$$

(under suitable hypotheses; conventions on $$2\pi$$ placement vary). Now frequency $$\xi$$ is continuous. The transform intertwines:

- **Differentiation** ↔ multiplication by polynomials in $$\xi$$,  
- **Convolution** $$f*g$$ ↔ product $$\hat f\hat g$$,  
- **Translation** ↔ modulation phase factors.

**Filtering** multiplies $$\hat f$$ by a gain function $$H(\xi)$$ (low-pass, high-pass, band-pass). Designing $$H$$ is the algebra of removing noise or extracting bands—radio tuners and equalizers live here.

**Convolution theorem (mechanism spine).** A linear time-invariant filter applied in the time domain is a convolution $$(f*h)(t)=\int f(s)h(t-s)\,ds$$. Under Fourier transform this becomes ordinary multiplication $$\widehat{f*h}=\hat f\,\hat h$$. That single fact is why engineers “think in frequency” whenever they design equalizers, channel models, or blur kernels: multiplication is mentally cheaper than sliding integrals, and after discretization the FFT makes both directions cheap.

**Parseval / Plancherel energy accounting.** Up to convention-dependent constants,

$$
\int \lvert f(x)\rvert^2\,dx = \int \lvert\hat f(\xi)\rvert^2\,d\xi:
$$

total energy is the same whether you sum squares in time or in frequency. Compression and denoising algorithms decide *where* that energy lives and which coordinates are safe to discard.

---

## 4. Discrete reality: DFT and FFT

Computers store finite samples $$x_0,\ldots,x_{N-1}$$. The **discrete Fourier transform (DFT)** is

$$
\hat x_k=\sum_{n=0}^{N-1} x_n e^{-2\pi i kn/N},
\qquad
x_n=\frac1N\sum_{k=0}^{N-1}\hat x_k e^{2\pi i kn/N}.
$$

Naive evaluation is $$O(N^2)$$. The **Fast Fourier Transform (FFT)** family computes the DFT in $$O(N\log N)$$—one of the most important algorithmic facts of the twentieth century. Real-time audio, broadband communications, large integer multiplication, and scientific computing all ride FFT performance.

**Mechanism.**  
*Digital signal processing became ubiquitous because frequency-domain algorithms are not only beautiful but cheap enough at scale via the FFT.*

**Communications sketch.** Orthogonal frequency-division multiplexing (OFDM)—the workhorse of Wi-Fi and modern cellular physical layers—sends data on many carefully spaced subcarriers that are orthogonal over a symbol period. At the receiver, an FFT separates the subcarriers. Again: industrial RF is Fourier analysis wearing standards documents.

### Short video: Drawing the Koch snowflake with spinning circles

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/koch-fourier-epicycles_en.mp4"></video>
</div>

About 2 minutes 55 seconds. We sample 4096 evenly spaced points along the boundary of the level-4 Koch snowflake, use the FFT to get the complex Fourier coefficients $$c_k$$, and keep the $$N$$ largest ($$N=1,5,20,100,500$$): each coefficient is a circle of radius $$\vert c_k\vert$$ turning $$k$$ times per period. The error is the mean distance between the two curves (both directions) divided by the mean radius; it falls from 8.93% to 0.07%. At the end we zoom in on a sharp tip: a finite sum is always a smooth curve (rounded corners, Gibbs-like ripples), so what we rebuild is the level-4 Koch polygon, not the true fractal.

---

## 5. Sampling and the Nyquist idea

A continuous signal cannot be recorded as an infinite continuum on a chip. **Sampling** records values at rate $$f_s$$ samples per second. The classical **Nyquist–Shannon** slogan: to capture frequencies up to $$B$$ hertz without aliasing, sample faster than $$2B$$ (under ideal band-limited assumptions).

**Aliasing** is the impostor phenomenon: a high frequency masquerades as a lower one after sampling—wagon-wheel effects in video, moiré in images. Anti-aliasing filters (low-pass before sampling) are Fourier engineering, not cosmetics.

Modern compressed sensing weakens classical sampling under sparsity assumptions—optimization + harmonic analysis ([Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/)).

---

### Explanation: From Continuous Sound to MP3/5G—Plus a 4-Point DFT by Hand

Every modern signal pipeline (MP3, JPEG, 5G OFDM, MRI) follows four steps—and you can watch the frequency-domain magic happen by hand on a 4-sample signal $$x = (2, 0, -2, 0)$$:

1. **Sample above the Nyquist rate:** Sample continuous sound at $$f_s > 2B$$ (e.g., 44.1 kHz for 20 kHz human hearing) so high frequencies do not alias onto low ones.
2. **Compute the 4-point DFT by hand:** Using $$\omega = e^{-2\pi i/4} = -i$$, the formula $$X_k = \sum_{n=0}^3 x_n (-i)^{kn}$$ gives:
   - $$X_0 = 2 + 0 + (-2) + 0 = 0$$ (zero DC average),
   - $$X_1 = 2(1) + 0(-i) + (-2)(-1) + 0(i) = 4$$,
   - $$X_2 = 2(1) + 0(-1) + (-2)(1) + 0(-1) = 0$$,
   - $$X_3 = 2(1) + 0(i) + (-2)(-1) + 0(-i) = 4$$.
   All of the signal’s energy collapsed cleanly into just two frequency bins $$X = (0, 4, 0, 4)$$! Check **Parseval’s energy conservation** by hand:
   $$
   \sum_{n=0}^3 \lvert x_n\rvert^2 = 2^2 + 0^2 + (-2)^2 + 0^2 = 8
   \;=\; \frac{1}{4}\bigl(0^2 + 4^2 + 0^2 + 4^2\bigr) = \frac{1}{4}\sum_{k=0}^3 \lvert X_k\rvert^2.
   $$
3. **Process cheaply in frequency:** Denoise by zeroing noisy bins; compress JPEG/MP3 by quantizing tiny coefficients our eyes/ears barely notice; pack 5G/Wi-Fi data across orthogonal subcarriers (OFDM) using one IFFT at the transmitter and one FFT at the receiver.
4. **Invert back to space/time (IFFT/IDCT):** Reconstruct crisp audio, images, or MRI slices.

**Quick check:** FFT is not a different mathematical transform from the DFT—it is a **divide-and-conquer algorithm** computing the exact same DFT tens of thousands of times faster.

## 6. JPEG, audio, and the compression pipeline

**Images (JPEG-style idea).** Split into blocks; apply a discrete cosine transform (DCT)—a Fourier cousin with cosine basis suited to real signals and boundaries; quantize coefficients (throw away fine high-frequency detail the eye notices less); entropy-code what remains. Reconstruction inverts the transform.

**Mechanism in one sentence.**  
*Natural images are often sparse or compressible in a frequency-like basis; quantization keeps high-energy coefficients and discards low-energy ones.*

**Audio.** Perceptual codecs transform short windows (MDCT, etc.), allocate bits by psychoacoustic masking, and invert. Even simpler pipelines use STFT (short-time Fourier transform) for analysis and filtering.

**MP3 is not “Fourier deleted the music.”** It is frequency-domain perceptual coding with careful engineering and standards.

---

## 7. MRI and scientific imaging

Magnetic resonance imaging acquires data that are naturally samples of a **Fourier transform** of the desired spatial image (k-space). Reconstruction is essentially an inverse FFT (plus corrections for physics, nonuniform sampling, coil sensitivities). Undersampled MRI uses constrained reconstruction—again sparsity and optimization.

**Mechanism.**  
*The physics of spin precession encodes spatial information as frequencies; harmonic analysis is the decoding language.*

Related: CT reconstruction (Radon transform, filtered back-projection—another integral geometry / Fourier story), radar, and crystallography (diffraction patterns as Fourier magnitudes—phase retrieval hard).

---

## 8. Uncertainty, windows, and time-frequency

A pure infinite sinusoid is perfectly localized in frequency and nowhere localized in time. A Dirac impulse is perfectly localized in time and flat in frequency. **Heisenberg-type uncertainty principles** (in harmonic analysis form) limit simultaneous concentration: you cannot have arbitrarily sharp time and frequency localization at once.

**Windowed Fourier / STFT** and **wavelets** trade resolution across scales. The STFT slides a window across time, Fourier-transforms each short piece, and stacks the results into a **spectrogram**—the visual language of speech, music, and vibration diagnostics. Choose a long window: sharp frequency, blurry time. Choose a short window: the reverse. That trade-off is not a UI preference; it is uncertainty made operational.

Wavelets (another basis family) improved some compression and denoising tasks by offering multi-scale localization better matched to edges and transients; JPEG 2000 uses wavelets. The Fourier idea generalizes: choose a basis adapted to the signal class and to the errors you can tolerate.

---

## 9. PDEs, green functions, and the broader calculus

Fourier transforms turn constant-coefficient linear PDEs on $$\mathbb{R}^n$$ into algebraic equations in frequency. A linear constant-coefficient differential operator becomes multiplication by a symbol $$p(\xi)$$; solving the PDE (when legitimate) is dividing by that symbol and transforming back. Fundamental solutions and dispersive estimates are advanced chapters. Engineering finite-element solvers may not literally FFT the whole domain on irregular meshes, but modal analysis in structures and acoustics—natural frequencies, mode shapes, forced response—is pure frequency thinking after discretization yields a matrix eigenproblem.

The pure mathematical theory—convergence of series, Carleson’s theorem on pointwise Fourier inversion, restriction conjectures linking curved frequency surfaces to spacetime estimates—is vastly deeper than codecs require. Chapter 2’s [Wang lecture]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/) shows the research frontier where harmonic analysis meets geometric measure theory; this lecture shows why the same subject appears in your photo gallery, your phone radio, and the MRI suite.

**Chapter mechanism reminder.** Abstract orthogonality of exponentials → efficient algorithms (FFT) → compression, sensing, and communication infrastructure. Beauty and silicon share a coordinate system.

---

### Fourier slogans (from video research)

Primary path: [3B1B Fourier series](https://www.youtube.com/watch?v=r6sGWTCMz2k) → [Fourier transform](https://www.youtube.com/watch?v=spUNpyF58BY).

- Series for periodic worlds; transform for non-periodic; DFT for finite samples; FFT for fast DFT.
- Sampling below Nyquist aliases high frequencies into low ones — irreversible confusion in the discrete data.
- Compression keeps large coefficients in a Fourier/DCT basis where energy concentrates.

## Common confusions

| Claim | Correction |
|-------|------------|
| “Fourier is only for music.” | Images, MRI, radio, PDEs, data analysis all use it. |
| “JPEG randomly deletes pixels.” | It quantizes transform coefficients in a frequency-like basis. |
| “FFT is a different transform than DFT.” | FFT is a fast algorithm for the DFT. |
| “Higher sample rate always means better.” | Beyond Nyquist needs of the band, costs rise; anti-aliasing still matters. |
| “Low-pass filtering is always safe.” | It blurs edges and can destroy needed high-frequency content. |
| “If coefficients are small, they never matter.” | Phase and coherent sums can make small coefficients structurally important. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/fourier-signal-processing/`.

**Recommended order**

1. **CORE** — 3Blue1Brown — But what is a Fourier series?: [https://www.youtube.com/watch?v=r6sGWTCMz2k](https://www.youtube.com/watch?v=r6sGWTCMz2k).
2. **CORE** — 3Blue1Brown — But what is the Fourier Transform?: [https://www.youtube.com/watch?v=spUNpyF58BY](https://www.youtube.com/watch?v=spUNpyF58BY).
3. **SURVEY** — 3Blue1Brown — Fourier transform / series topic hub: [https://www.3blue1brown.com/topics/fourier-transform](https://www.3blue1brown.com/topics/fourier-transform).
4. **FOUNDATION** — Stanford EE261 / DSP culture (Oppenheim-style courses): [https://see.stanford.edu/Course/EE261](https://see.stanford.edu/Course/EE261).
5. **FOUNDATION** — MIT OCW 6.003 Signals and Systems: [https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/).
6. **INTUITION** — Veritasium — The Most Underrated Algorithm (FFT): [https://www.youtube.com/watch?v=nmgFG7PUHfo](https://www.youtube.com/watch?v=nmgFG7PUHfo).

Complete URL bibliography: `research/video-research/fourier-signal-processing/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/fourier-signal-processing/transcripts/` · status: `research/video-research/fourier-signal-processing/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/fourier-signal-processing_r6sGWTCMz2k_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/fourier-signal-processing/references.md`.

### Videos (primary path)

1. 3Blue1Brown — But what is a Fourier series? — https://www.youtube.com/watch?v=r6sGWTCMz2k
2. 3Blue1Brown — But what is the Fourier Transform? — https://www.youtube.com/watch?v=spUNpyF58BY
3. 3Blue1Brown — Fourier transform / series topic hub — https://www.3blue1brown.com/topics/fourier-transform
4. Stanford EE261 / DSP culture (Oppenheim-style courses) — https://see.stanford.edu/Course/EE261
5. MIT OCW 6.003 Signals and Systems — https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/
6. Veritasium — The Most Underrated Algorithm (FFT) — https://www.youtube.com/watch?v=nmgFG7PUHfo
7. Zach Star — Nyquist–Shannon Sampling Theorem intuition — https://www.youtube.com/watch?v=Jv5FU8oUWEY
8. Numberphile — Fourier culture / related — https://www.youtube.com/watch?v=r6sGWTCMz2k

### Videos (secondary finds)

9. JPEG compression math explainers — https://en.wikipedia.org/wiki/JPEG

### Papers, books, OCW, and web

10. Cooley & Tukey — An algorithm for the machine calculation of complex Fourier series (1965): https://www.ams.org/journals/mcom/1965-19-090/S0025-5718-1965-0178586-1/
11. Wikipedia — Fourier transform: https://en.wikipedia.org/wiki/Fourier_transform
12. Wikipedia — Fast Fourier transform: https://en.wikipedia.org/wiki/Fast_Fourier_transform
13. Wikipedia — Nyquist–Shannon sampling theorem: https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
14. Wikipedia — Discrete cosine transform: https://en.wikipedia.org/wiki/Discrete_cosine_transform
15. 3Blue1Brown Fourier hub: https://www.3blue1brown.com/topics/fourier-transform

### Course

16. Course: [Calculus]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/), [DEs]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/), [Wang harmonic analysis]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/), [Kakeya]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/). Pack: `research/video-research/fourier-signal-processing/`.

## Further directions

- Next: [Differential Equations → Applications]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/) (modes, numerics, well-posedness).  
- Pure frontier: [Wang]({{ site.baseurl }}/contents/en/chapter02/02_15_Wang_Harmonic_Analysis/) and [Kakeya]({{ site.baseurl }}/contents/en/chapter01/01_08_Kakeya_Conjecture/).  
- Restate the core mechanism of this essay in one paragraph; note one precise question you still have.

## Video tham khảo

- **xem trước** — [But what is a Fourier series? From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k) — 3Blue1Brown, English. Watch first. “But what is a Fourier series? From heat flow to drawing with circles | DE4” orients the lesson’s aim: Explain a signal as a superposition of oscillatory modes (sines/cosines or complex exponentials).
- [But what is the Fourier Transform? A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY) — 3Blue1Brown, English. A second pass once the main claim is in view: Explain a signal as a superposition of oscillatory modes (sines/cosines or complex exponentials).
- [The Most Underrated Algorithm](https://www.youtube.com/watch?v=nmgFG7PUHfo) — Veritasium, English. Further depth after the first two, still tied to this lesson: Explain a signal as a superposition of oscillatory modes (sines/cosines or complex exponentials).
