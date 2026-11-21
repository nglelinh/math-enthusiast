---
layout: post
title: "Studio: Toy Circle Gauge and Aharonov–Bohm Intuition"
chapter: '07'
order: 12
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Learning path — Gauge geometry (hands-on)**  
> **1.** [Gauge theory as geometry]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/)  
> **2.** Optional: [Distributions]({{ site.baseurl }}/contents/en/chapter03/03_12_Distributions_Dirac/) (flux / Stokes care)  
> **3. You are here:** compute a **toy holonomy** on a circle  
> *Time guide:* ~60–120 min; calculus + complex numbers only.

You will not solve Yang–Mills. You will feel **connection → parallel transport → holonomy**, including the Aharonov–Bohm slogan: **local $$F=0$$ need not imply trivial global phase**.

---

## Learning objectives

After this studio you should be able to:

- Treat a $$U(1)$$ connection on the circle as a 1-form $$A=a(\theta)\,d\theta$$ (or constant $$A=a\,d\theta$$).
- Compute parallel transport / phase $$e^{iq\oint A}$$ for a charged particle going once around $$S^1$$.
- Explain why flux through a region can equal line integral of $$A$$ (Stokes) even when you avoid the support of $$B$$.
- Label what is **theorem (calculus)** vs **physics interpretation**.
- Log one misconception you held about “potential is pure gauge, so unphysical.”

**Prerequisites.** Line integrals; $$e^{i\phi}$$; [Gauge as geometry]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/) § on abelian holonomy.

---

## 1. Setup

Identify the circle $$S^1$$ with $$\theta\in[0,2\pi]$$ and endpoints glued. A constant connection form:

$$
A = a\,d\theta,\qquad a\in\mathbb{R}.
$$

Field strength on the circle alone: for a pure 1D base, think of $$A$$ as the restriction of a plane connection with magnetic flux through the disk. On $$\mathbb{R}^2\setminus\{0\}$$, a standard model is

$$
A = a\,d\theta
$$

in polar coordinates (away from the origin), with

$$
\oint_{S^1} A = 2\pi a.
$$

If $$F=dA=0$$ on the punctured plane, Stokes still relates the loop integral to **flux concentrated at the origin** in a distributional sense—care with [distributions]({{ site.baseurl }}/contents/en/chapter03/03_12_Distributions_Dirac/).

---

## 2. Tasks

### Task A — Phase around the loop (30 min)

Take charge $$q$$ and compute the holonomy phase factor

$$
U = \exp\!\Big(iq \oint_{S^1} A\Big) = \exp(iq\cdot 2\pi a)
$$

for $$a=0,\;1/2,\;1$$ (set $$q=1$$ if you like). Record when $$U=1$$ vs $$U=-1$$.

**Write:** which values of flux give trivial holonomy?

### Task B — Gauge transform (20 min)

On the punctured plane, try $$A'=A+d\lambda$$ with a smooth single-valued $$\lambda$$. Show $$\oint A'=\oint A$$.  

Then discuss (qualitatively) what goes wrong if $$\lambda$$ jumps by $$2\pi$$ when you go around the circle (large gauge / multi-valued angle).

### Task C — Aharonov–Bohm slogan (20 min)

In ≤120 words: how can interference depend on flux in a region the particle’s path does not enter, while local $$B=0$$ along the path?

### Task D — Dictionary row (15 min)

Add four rows to a mini physics↔math table: $$A$$, $$F$$, holonomy, gauge transform—with status labels.

### Task E — Log

One error you almost made (e.g. “$$F=0$$ everywhere ⇒ $$A=0$$”).

---

## 3. Success criteria

| Criterion | Pass |
|-----------|------|
| Computation | Correct $$U$$ for three values of $$a$$ |
| Stokes literacy | Flux ↔ loop integral explained carefully |
| AB slogan | Clear, no superluminal signaling claims |
| Log | ≥1 misconception noted |

---

## 4. Optional stretch

Replace $$U(1)$$ by constant $$SU(2)$$ matrix connection along the circle (path-ordered exponential reduces to ordinary matrix exp if $$A$$ is constant in a fixed gauge). Compute $$ \mathcal{P}\exp\oint A $$ for a simple diagonal generator.

---

## See also

- [Gauge as geometry]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/)  
- [Physics↔math dictionary studio]({{ site.baseurl }}/contents/en/chapter07/07_11_Explore_Physics_Math_Dictionary/)  
- [Lie groups]({{ site.baseurl }}/contents/en/chapter03/03_11_Lie_Groups_Particle_Physics/)  
