---
layout: post
title: "Minimal Surfaces"
chapter: '04'
order: 10
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
---

Bend a copper wire into a twisted loop, dip it into soapy water, and lift it out into the light. Instantly, a shimmering membrane snaps taut across the wire, wobbling for a fraction of a second before freezing into a glassy, saddle-shaped sculpture. Without writing a single line of code, surface tension has just solved a nonlinear partial differential equation in real time—minimizing the surface area spanning your wire.

In calculus, finding the minimum of a function $$f(x)$$ means setting its derivative to zero: $$f'(x)=0$$. **Minimal surface theory** is the breathtaking geometric upgrade of that exact idea: the unknown is no longer a number $$x$$, it is an entire two-dimensional *shape* $$S$$, and the condition for stationary area becomes **zero mean curvature** ($$H = 0$$). Pull two wire rings apart in soapy water and you witness a **catenoid** stretch, lose stability, and pop into two flat disks—a living demonstration of differential geometry, the calculus of variations, and topology colliding in your hands.

**Path:** soap films and Plateau’s problem → principal curvatures and $$H=0$$ → verifying $$H=0$$ on the catenoid by hand → classical examples and the Costa revolution → stability and topology → modern applications → common confusions and further directions.

---

## Learning objectives

After this lecture you should be able to:

- State **Plateau’s problem**: find a surface of least area spanning a given boundary curve $$\Gamma$$.
- Explain **principal curvatures** $$\kappa_1, \kappa_2$$ and why **mean curvature** $$H = \frac{\kappa_1+\kappa_2}{2} = 0$$ characterizes minimal surfaces.
- Verify by direct calculation that the **catenoid** $$r(z) = a\cosh(z/a)$$ has $$H=0$$ everywhere, whereas a sphere has $$H = 1/R \neq 0$$.
- Recognize the classical gallery (**plane**, **catenoid**, **helicoid**) and explain why the **Costa surface** (1982) reignited the field.
- Distinguish a **critical point of area** (minimal surface) from a **global area minimizer**, using the two-ring soap film jump.
- Avoid claiming that "zero mean curvature means flat" or "minimal means smallest possible surface in the universe."

**Prerequisites.** Single-variable derivatives (including $$\cosh$$ and $$\sinh$$) and multivariable intuition for graphs $$z = u(x,y)$$. PDE literacy is helpful but not required.

---

## Key ideas: Where Calculus Meets Sculpture

Minimal surfaces sit at one of the richest intersections in all of mathematics, uniting four distinct traditions:

1. **Calculus of Variations:** Instead of optimizing a function $$f(x)$$ of a real number, you optimize a *functional*—like surface area $$A(S)$$—over an infinite-dimensional space of shapes. Setting the first variation $$\delta A = 0$$ yields the **Euler–Lagrange equation**, which for area is precisely $$H=0$$.
2. **Differential Geometry of Surfaces:** At any point on a smooth surface, slice the surface with normal planes and measure how sharply the slice bends. The maximum and minimum bendings are the **principal curvatures** $$\kappa_1, \kappa_2$$. Their *product* $$K = \kappa_1\kappa_2$$ is **Gaussian curvature** (intrinsic bending), while their *average* $$H = \frac{\kappa_1+\kappa_2}{2}$$ is **mean curvature** (how area responds to pushing the surface outward).
3. **Nonlinear PDEs & Geometric Measure Theory:** Expressing $$H=0$$ for a graph $$z=u(x,y)$$ gives a nonlinear elliptic PDE. Proving that solutions exist and are smooth—even when soap films meet along $$120^\circ$$ seams in foams—drove the creation of **geometric measure theory** (Douglas, Radó, De Giorgi, Federer, Almgren).
4. **Complex Analysis (Weierstrass–Enneper):** Remarkably, minimal surfaces in $$\mathbb{R}^3$$ can be generated directly from pairs of holomorphic functions in the complex plane—turning complex analysis into a factory for 3D sculptures.

---

## 1. Soap films and Plateau’s problem

In the nineteenth century, the Belgian physicist **Joseph Plateau** dipped wire frames of every imaginable shape into soap solution and catalogued the resulting films. **Plateau’s problem** asks mathematically: given a closed curve $$\Gamma \subset \mathbb{R}^3$$, does there always exist a surface $$S$$ with boundary $$\Gamma$$ of least possible area, and how smooth is it?

A physical soap film minimizes surface-tension energy, which is proportional to surface area (when air pressure is equal on both sides). Proving existence and regularity rigorously took nearly a century: Jesse Douglas (winning one of the first two Fields Medals in 1936) and Tibor Radó solved the disk-type case, and twentieth-century geometric measure theory extended the theory to higher dimensions and singular foams.

---

## 2. Mean curvature and the minimal surface equation

At every point on an oriented surface, the two principal curvatures $$\kappa_1, \kappa_2$$ measure bending in two perpendicular principal directions. The **mean curvature** is their average:

$$
H = \frac{\kappa_1 + \kappa_2}{2}.
$$

If you nudge a small patch of surface outward by a tiny distance $$\varepsilon$$ along its normal vector, its area changes at first order by $$-2\varepsilon H \cdot (\text{area})$$. Therefore, for the surface to be a **stationary point of area** (no first-order reduction in area from any tiny bump), we must have

$$
H \equiv 0 \iff \kappa_1 = -\kappa_2.
$$

Geometrically, **every minimal surface is saddle-shaped at every non-flat point**: if it curves *upward* along one direction ($$\kappa_1 > 0$$), it must curve *downward* by the exact same amount along the perpendicular direction ($$\kappa_2 = -\kappa_1 < 0$$) so the two tensions cancel out!

Contrast this with a **soap bubble** (a sphere of radius $$R$$): every direction curves inward equally, so $$\kappa_1 = \kappa_2 = \frac{1}{R}$$ and $$H = \frac{1}{R} \neq 0$$! A sphere is *not* a minimal surface—it minimizes area only under the extra constraint of enclosing a fixed volume of trapped air (giving *constant* nonzero mean curvature, balanced by higher air pressure inside the bubble).

If a minimal surface is written as a graph $$z = u(x,y)$$, the condition $$H=0$$ becomes the **minimal surface equation**:

$$
\mathrm{div}\!\left(\frac{\nabla u}{\sqrt{1+|\nabla u|^2}}\right) = 0,
$$

a classic quasilinear elliptic PDE.

---

### Short video: A soap film between two rings

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/soap-film-catenoid_en.mp4"></video>
</div>

Between two rings of radius 1 the film is a catenoid. As the rings move apart its area grows: from about 1.06 radii apart two flat discs (area $$2\pi \approx 6.28$$) already have less area, and past about 1.33 radii no catenoid exists, so the film pops into two discs.


### Try it yourself: Pull the rings apart

<div class="mex-explainer" data-mex="catenoid" data-lang="en"></div>


## 3. Classical examples—and verifying $$H=0$$ on the catenoid by hand

### Worked example: Direct curvature cancellation on the catenoid

Rotate the catenary curve $$r(z) = a\cosh(z/a)$$ around the $$z$$-axis (with neck radius $$a > 0$$). This forms the **catenoid**—the *only* non-flat minimal surface of revolution. Let us verify $$H = 0$$ directly using standard formulas for surfaces of revolution!

For any profile $$r(z)$$, compute the first and second derivatives:

$$
r'(z) = \sinh(z/a), \qquad r''(z) = \frac{1}{a}\cosh(z/a),
$$

and recall the golden hyperbolic identity $$1 + \sinh^2(u) = \cosh^2(u)$$, which gives $$\sqrt{1 + (r')^2} = \cosh(z/a)$$.

Now plug into the two principal curvatures of a surface of revolution:
1. **Meridian curvature** (bending along the curved profile $$r(z)$$—curving *outward* away from the axis):
   $$
   \kappa_1 = \frac{-r''}{\bigl(1+(r')^2\bigr)^{3/2}} = \frac{-\frac{1}{a}\cosh(z/a)}{\cosh^3(z/a)} = -\frac{1}{a\cosh^2(z/a)}.
   $$
2. **Parallel circle curvature** (bending around the circular waist of radius $$r(z)$$—curving *inward* toward the axis):
   $$
   \kappa_2 = \frac{1}{r\sqrt{1+(r')^2}} = \frac{1}{a\cosh(z/a)\cdot\cosh(z/a)} = +\frac{1}{a\cosh^2(z/a)}.
   $$

Add them together:

$$
H = \frac{\kappa_1 + \kappa_2}{2} = \frac{1}{2}\!\left(-\frac{1}{a\cosh^2(z/a)} + \frac{1}{a\cosh^2(z/a)}\right) = 0 \qquad \text{for every } z!
$$

Notice the miracle: at the narrowest neck ($$z=0$$), $$\kappa_1 = -1/a$$ and $$\kappa_2 = +1/a$$; further out toward the rings, both curvatures shrink at the exact same rate $$\operatorname{sech}^2(z/a)$$, staying locked in perfect cancellation everywhere!

Now watch what happens in the **two-ring soap film experiment** (unit rings of radius $$R=1$$ separated by distance $$d$$):
- For $$d < 1.055$$: the catenoid is the **global area minimizer** (less area than two flat disks of total area $$2\pi \approx 6.283$$).
- For $$1.055 < d < 1.325$$: the catenoid is still a **local minimum** (metastable!)—the soap film hangs on even though two separate flat disks would actually have *less* area!
- At $$d \approx 1.325$$ (the Goldschmidt limit): **no catenoid solution exists at all**, and the soap film violently snaps into two flat disks.

### The rest of the classical gallery

- **Plane:** $$\kappa_1 = \kappa_2 = 0$$ everywhere—trivial, flat, and globally area-minimizing.
- **Helicoid:** A spiral staircase ramp swept out by a rotating, rising line. Amazingly, the catenoid and helicoid are **locally isometric**—you can smoothly bend a catenoid into a helicoid without stretching or tearing it, passing through a continuous family of minimal surfaces at every instant!
- **Costa surface (1982):** For two centuries, mathematicians suspected that the plane, catenoid, and helicoid were the *only* complete, embedded minimal surfaces of finite topology. Celso Costa shattered that belief in 1982 with a brand-new minimal surface of genus 1 with three ends, which David Hoffman and William Meeks visualized with computer graphics and proved was embedded—launching a modern renaissance in minimal surface discovery.

---

### Explanation: Why a Curved Saddle Can Minimize Area

At first glance, "curved" sounds like "longer/bigger," so how can a curved surface like a catenoid have minimal area? Walk through the four-step logic slowly:

1. **Remember the boundary constraint.** A flat plane has the smallest area between *coplanar* curves, but if your wire frame twists in 3D—or consists of two separated rings—a single flat sheet cannot span the boundary.
2. **Balance two opposing pulls.** At every point on a stretched film, pulling along one direction tightens one curvature ($$\kappa_1$$) while pulling along the perpendicular direction tightens the other ($$\kappa_2$$). Equilibrium demands exact cancellation: $$\kappa_1 + \kappa_2 = 0$$, forcing a saddle geometry.
3. **Separate first variation ($$H=0$$) from global minimality.** Just like $$f'(x)=0$$ in 1D calculus catches local minima, local maxima, and saddle points, $$H=0$$ catches *all* critical surfaces of area—including metastable catenoids ($$1.06 < d < 1.325$$) that lose to two flat disks globally.
4. **Watch topology jump when solutions disappear.** Past $$d \approx 1.325$$, the smooth PDE solution ceases to exist, forcing a discontinuous jump from one connected surface (catenoid) to two disconnected disks.

**Quick check.** A soap bubble floating freely in air is a sphere of radius $$R$$, so $$H = 1/R \neq 0$$. Why doesn’t it collapse into a saddle surface with $$H=0$$? *(Hint: what physical constraint keeps the bubble inflated?)*

---

## 4. Topology, completeness, and embeddedness

Modern minimal surface research orbits four deep questions:
- Which topologies admit complete minimal immersions in $$\mathbb{R}^3$$?
- When is a minimal surface **embedded** (no self-intersections) versus merely immersed?
- How do its **ends** behave as they stretch out to infinity?
- Which complete minimal surfaces are **stable** under compactly supported deformations?

Landmark theorems of Fischer-Colbrie, do Carmo, Schoen, and Colding–Minicozzi show that combining the analytic condition $$H=0$$ with global topology produces astonishing **rigidity**.

---

## 5. Beyond soap films: applications and relatives

- **Materials science & biology:** Lipid bilayers, block copolymers, and crystal grain boundaries self-assemble into periodic minimal surfaces (like the gyroid) to minimize interfacial energy.
- **Architecture:** Frei Otto’s famous tensile roofs (such as the Munich Olympic Stadium) used physical soap-film models for structural form-finding.
- **General relativity:** Minimal surfaces play a starring role in proving the **Positive Mass Theorem** (Schoen–Yau) and analyzing black-hole apparent horizons.
- **Geometric analysis:** Min-max theory uses minimal hypersurfaces as geometric probes to uncover the shape of curved higher-dimensional manifolds.

---

## 6. Why it is beautiful

One compact equation—$$H=0$$—spins out planes, catenoids, helicoids, gyroids, and the Costa labyrinth, uniting calculus of variations, PDEs, complex analysis, and a childhood soap bubble wand.

---

## 7. Common confusions

1. **“Minimal means globally smallest possible area.”** — Minimal surfaces are *critical points* of area ($$H=0$$); global minimizers are a smaller subclass.
2. **“Soap films always find the global minimum.”** — Metastable films (like the catenoid between $$d=1.06$$ and $$1.325$$) sit in local minima until disturbed.
3. **“Zero mean curvature means flat.”** — Catenoids and helicoids are genuinely curved ($$\kappa_1 = -\kappa_2 \neq 0$$), yet have $$H = 0$$.
4. **“A soap bubble is a minimal surface.”** — A sphere has constant *nonzero* mean curvature $$H = 1/R$$ because of enclosed air pressure.
5. **“All minimal surfaces are graphs $$z=u(x,y)$$.”** — Complete surfaces like the catenoid and Costa surface fold back over themselves and cannot be written as single graphs.
6. **“Costa’s surface finished the classification.”** — On the contrary, it reopened an entire frontier of embedded minimal surfaces.

---

### Minimal surface slogans (from video research)

- Physical soap films motivate **Plateau’s problem**; mathematics needs existence, regularity, and possible singularities.
- **Mean curvature zero** is the analytic definition most essays use.
- Catenoid and helicoid are the first museum of complete examples.

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/minimal-surfaces/`.

**Recommended order**

1. **ORIENTATION** — Mathemaniac — Physics/math soap films & Plateau-style problems / minimal surfaces culture: [https://www.youtube.com/watch?v=Cvs8iRqG6lg](https://www.youtube.com/watch?v=Cvs8iRqG6lg).
2. **ORIENTATION** — Stand-up Maths / Parker soap film optimization demos: [https://www.youtube.com/watch?v=Cvs8iRqG6lg](https://www.youtube.com/watch?v=Cvs8iRqG6lg).
3. **CORE** — Camillo De Lellis — Plateau's problem lecture math videos: [https://www.youtube.com/watch?v=aTS69X-DBiA](https://www.youtube.com/watch?v=aTS69X-DBiA).
4. **FOUNDATION** — Mean curvature flow / minimal surface university lectures: [https://www.youtube.com/watch?v=aTS69X-DBiA](https://www.youtube.com/watch?v=aTS69X-DBiA).
5. **INTUITION** — Helicoid and catenoid classic visualizations: [https://www.youtube.com/watch?v=Cvs8iRqG6lg](https://www.youtube.com/watch?v=Cvs8iRqG6lg).
6. **FRONTIER** — CMSA / IAS geometry seminar samples (advanced): [https://www.youtube.com/watch?v=aTS69X-DBiA](https://www.youtube.com/watch?v=aTS69X-DBiA).

Complete URL bibliography: `research/video-research/minimal-surfaces/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/minimal-surfaces/transcripts/` · status: `research/video-research/minimal-surfaces/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/minimal-surfaces_Cvs8iRqG6lg_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/minimal-surfaces/references.md`.

### Videos (primary path)

1. Mathemaniac — Physics/math soap films & Plateau-style problems / minimal surfaces culture — https://www.youtube.com/watch?v=Cvs8iRqG6lg
2. Stand-up Maths / Parker soap film optimization demos — https://www.youtube.com/watch?v=Cvs8iRqG6lg
3. Camillo De Lellis — Plateau's problem lecture math videos — https://www.youtube.com/watch?v=aTS69X-DBiA
4. Mean curvature flow / minimal surface university lectures — https://www.youtube.com/watch?v=aTS69X-DBiA
5. Helicoid and catenoid classic visualizations — https://www.youtube.com/watch?v=Cvs8iRqG6lg
6. CMSA / IAS geometry seminar samples (advanced) — https://www.youtube.com/watch?v=aTS69X-DBiA
7. Calculus of variations soap film intros — https://www.youtube.com/watch?v=Cvs8iRqG6lg
8. Course calculus essay variational section (internal) (FOUNDATION).

### Videos (secondary finds)

9. Architecture freeform / tensile structure math talks — https://en.wikipedia.org/wiki/Minimal_surface

### Papers, books, OCW, and web

10. Colding & Minicozzi — A Course in Minimal Surfaces (AMS): https://bookstore.ams.org/gsm-121
11. Wikipedia — Minimal surface: https://en.wikipedia.org/wiki/Minimal_surface
12. Wikipedia — Plateau's problem: https://en.wikipedia.org/wiki/Plateau%27s_problem
13. Wikipedia — Mean curvature: https://en.wikipedia.org/wiki/Mean_curvature
14. Wikipedia — Catenoid: https://en.wikipedia.org/wiki/Catenoid
15. Wikipedia — Helicoid: https://en.wikipedia.org/wiki/Helicoid

### Course

16. Course links: [Symmetry]({{ site.baseurl }}/contents/en/chapter04/04_04_Symmetry/), [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/), [Optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [Navier–Stokes / continuum models]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/). Pack: `research/video-research/minimal-surfaces/`.

## Further directions

Variational cousins appear in [optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/). Geometric strangeness of surfaces: [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/). Symmetry constraints on shapes: [Symmetry]({{ site.baseurl }}/contents/en/chapter04/04_04_Symmetry/). Continuum modeling culture: [Navier–Stokes problem map]({{ site.baseurl }}/contents/en/chapter01/01_05_Navier_Stokes/).

## Video tham khảo

- **xem trước** — [How physics solves a math problem (and a 3D graphics problem)](https://www.youtube.com/watch?v=Cvs8iRqG6lg) — Mathemaniac, English. Watch first. “How physics solves a math problem (and a 3D graphics problem)” orients the lesson’s aim: State Plateau’s problem: find a surface of least area with a given boundary curve.
- [Camillo De Lellis (UZH) Pieces of soap films: boundaries and Plateau's problem](https://www.youtube.com/watch?v=aTS69X-DBiA) — Math UniPD, English. A second pass once the main claim is in view: State Plateau’s problem: find a surface of least area with a given boundary curve.
