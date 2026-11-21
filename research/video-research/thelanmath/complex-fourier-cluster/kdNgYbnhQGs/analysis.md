# Đạo Hàm Của Một Nốt Nhạc — Vì Sao Tiếng Piano Biết Thở

**URL:** https://www.youtube.com/watch?v=kdNgYbnhQGs
**Duration:** 467 s
**Deep extract:** 2026-08-08
**Role:** Piano envelope = exponential decay; partials; derivative as perceived change

## Knowledge units

### Piano ADSR as a real graph

Real recorded note: attack spike, decay, sustain-ish release. Envelope is a function of time (energy vs t); derivative is instantaneous rate of change—what the ear is highly sensitive to.

### Exponential decay ODE

If energy loses a fixed fraction per unit time, Ė = −kE ⇒ E(t)=E₀e^{−kt}. Measured time constant ~0.61s for the example (energy to ~37%). Exponential vs linear fade: ‘breathing’ vs abrupt cut. Model is approximate (multi-string partials).

### Partials / harmonic stack

One piano note is a stack of partials at roughly integer frequency multiples; each can decay differently—Fourier content of a ‘single’ note. Silence is practical threshold, not mathematical zero of the exponential.


## LO6
Popular explainer — verify against textbooks/papers.
Cluster: `research/video-research/thelanmath/complex-fourier-cluster/`
