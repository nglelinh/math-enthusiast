---
layout: post
title: "From Spacetime Geometry to Gravity"
chapter: '03'
order: 10
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
---

Newton treated gravity as a force acting across absolute space and universal time. Einstein’s **general relativity (GR)** replaced that picture with a geometric mechanism: matter and energy curve spacetime; free fall is motion along geodesics of a metric. The “force” is reinterpreted as geometry.

This lecture is an undergraduate map of that mechanism—not a GR course. You will meet the metric, curvature slogans, Einstein’s equation as a PDE relating geometry to stress-energy, and a precision table separating theorem, standard physics, and popular metaphor (**LO4**, **LO6**). It prepares the geometric instinct later reused by [gauge theory]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/): **physics as fields on a geometric background**, with curvature encoding interaction.

---

## Learning objectives

After this lecture you should be able to:

- State the **equivalence principle** slogan and how it motivates replacing gravitational force by free-fall geometry.
- Explain what a **metric** $$g_{\mu\nu}$$ packages (distances, angles, causal structure at slogan level).
- Distinguish **special relativity** (flat Minkowski spacetime) from **general relativity** (dynamical curved spacetime).
- Write Einstein’s equation schematically: $$\mathrm{Ric} - \tfrac12 R g = 8\pi T$$ and name what each side represents.
- Give one **one-step mechanism** from geometry to a prediction (e.g. light deflection, gravitational time dilation) without full tensor calculus.
- Avoid LO6 traps: “everything is relative,” “GR is only black-hole science fiction,” “curved space = curved embedding you can always see.”

**Prerequisites.** Multivariable calculus; linear algebra (inner products). Optional: [Calculus → Physics]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/) for grad/div/curl culture.

---

## 1. Special relativity as flat geometry

**Minkowski spacetime** is $$\mathbb{R}^4$$ with the indefinite inner product (signature convention varies)

$$
ds^2 = -c^2\,dt^2 + dx^2 + dy^2 + dz^2.
$$

Intervals, light cones, and the invariant speed of light are geometric. Lorentz transformations are linear isometries of this metric. There is still **no dynamical gravity**: spacetime is a fixed stage.

**Literacy.** “Relative” in relativity means **covariance under a specified symmetry group** and operational definitions of time/length—not “anything goes.”

---

## 2. The equivalence principle → curved spacetime

Rough slogan: in a small freely falling laboratory, gravity is locally indistinguishable from the absence of gravity (up to tidal effects). Einstein elevated this to a design principle: **gravitation is not a force field on a rigid stage; the stage itself carries geometry that freefallers follow.**

Tidal forces—relative acceleration of nearby free-fall paths—become **curvature**. If all free-fall trajectories could be straightened simultaneously everywhere, curvature would vanish and one would recover special relativity locally in a global inertial frame.

---

## 3. Metric, geodesics, curvature (seminar definitions)

A **Lorentzian metric** $$g$$ assigns to each event an inner product on tangent vectors with signature $$(-,+,+,+)$$ (or reverse). Proper time along a timelike worldline $$\gamma$$ is essentially

$$
\tau = \int \sqrt{-g(\dot\gamma,\dot\gamma)}\,dt
$$

(up to constants and parametrization). **Geodesics** extremize proper time (or satisfy the geodesic equation with Christoffel symbols built from $$g$$ and $$\partial g$$).

**Curvature tensors** (Riemann, Ricci, scalar $$R$$) measure the failure of second covariant derivatives to commute and the volume distortion of geodesic congruences. You need not compute components here; keep the slogan:

> **Matter tells spacetime how to curve; curved spacetime tells matter how to move.**

---

## 4. Einstein’s equation as a field equation

Schematically,

$$
G_{\mu\nu} := R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu},
$$

where $$G_{\mu\nu}$$ is the Einstein tensor built from the metric’s curvature, and $$T_{\mu\nu}$$ is the **stress-energy tensor** of matter and non-gravitational fields.

| Side | Meaning |
|------|---------|
| Left | Pure geometry (curvature combinations with automatic conservation identities) |
| Right | Energy, momentum, pressure, stresses of “stuff” |

In vacuum ($$T=0$$), one studies Ricci-flat metrics; Schwarzschild and Kerr black-hole solutions live in this world (with suitable asymptotics and symmetry).

**PDE character.** Einstein’s equation is a nonlinear system for the metric. Well-posedness of the Cauchy problem, stability of black holes, and cosmic censorship are major mathematical GR programs—some with spectacular recent progress, some still open.

---

## 5. One-step mechanisms (applications literacy)

**Gravitational time dilation.** Clocks deeper in a gravitational well tick slower relative to distant observers (GPS corrections are engineering proof that this is not optional poetry).

**Light deflection / lensing.** Null geodesics bend near mass; apparent positions of stars and galaxies shift.

**Gravitational waves.** Linearized perturbations of the metric propagate at $$c$$; LIGO/Virgo detect strains from distant mergers—geometry in motion.

**Cosmology.** Homogeneous isotropic metrics (FLRW) reduce Einstein’s equation to ODEs for a scale factor $$a(t)$$, linking expansion history to energy content.

Each is a **mechanism**: geometry → observable, not a buzzword list.

---

## 6. What mathematics kept

| Mathematical theme | GR contact |
|--------------------|------------|
| Riemannian / Lorentzian geometry | Metrics, curvature, geodesics |
| Global analysis / causality | Domain of dependence, singularity theorems (Penrose–Hawking) |
| Nonlinear hyperbolic PDE | Local well-posedness of Einstein evolution |
| Differential topology | Topology of horizons, positive mass theorems |
| Geometric analysis | Stability of Kerr, nonlinear wave equations on black-hole backgrounds |

GR is thus a **world-changing application of geometry** and a **generator of pure-math programs**—the Chapter 3 dual role.

---

## 7. Precision versus hype (LO6)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Einstein proved everything is relative.” | Misleading | Absolute structures remain (e.g. causal structure, $$c$$, curvature scalars). |
| “Space is curved like a ball you can see from outside.” | Optional metaphor | Spacetime curvature is intrinsic; embedding pictures are pedagogy, not ontology. |
| “Black holes violate physics.” | Overstated | They are solutions/regions in GR (+ quantum questions at horizons—separate frontier). |
| “GR and QM already unified.” | False | Semiclassical gravity exists; full quantum gravity is open. |
| “If GPS works, Einstein’s equation is completely understood as PDE.” | Category mix | Technology uses GR corrections; global mathematical GR still has open problems. |

---

## References and further reading

1. Hartle — *Gravity* (physics-first, undergraduate friendly).  
2. Carroll — *Spacetime and Geometry* (more complete).  
3. Misner, Thorne, Wheeler — *Gravitation* (classic encyclopedia).  
4. Course: [Calculus → Physics]({{ site.baseurl }}/contents/en/chapter03/03_02_Calculus_Physics_Engineering/), [DE applications]({{ site.baseurl }}/contents/en/chapter03/03_09_Differential_Equations_Applications/), [Mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/), [Gauge as geometry]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/).  
