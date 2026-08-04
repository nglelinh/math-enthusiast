---
layout: post
title: "Mirzakhani and Moduli Spaces (Fields Medal 2014)"
chapter: '02'
order: 5
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Imagine you hold not one rubber torus with two handles, but a *space of all possible shapes* such surfaces can take once you declare two shapes the same if one can be smoothly deformed into the other without tearing. That space—**moduli space**—is itself a geometric object with its own geodesics, volumes, and dynamical systems. **Maryam Mirzakhani** (1977–2017) received the **Fields Medal 2014**—the first woman to do so—for transforming how mathematicians measure, count, and flow on the moduli spaces of **Riemann surfaces** and hyperbolic metrics. Her work sits where hyperbolic geometry, Teichmüller theory, and ergodic dynamics meet counting problems that sound almost combinatorial: how many simple closed curves of length at most $$L$$ live on a typical surface of genus $$g$$?

This essay is a seminar map, not a research monograph. We build enough vocabulary to state her geodesic-counting asymptotics and Weil–Petersson volume ideas, sketch the earthquake-flow ergodicity theorem with Alex Eskin, and connect flat surfaces to billiards—while keeping **LO6** discipline about popular accounts that reduce a deep program to a single slogan or a biography alone.

---

## Learning objectives

After this lecture you should be able to:

- Define, informally, a **Riemann surface** of genus $$g\ge 2$$, its **hyperbolic metric**, **Teichmüller space**, and **moduli space**.
- Explain why moduli space is a “space of shapes,” not a single surface drawn in space.
- State a counting problem about **simple closed geodesics** and the asymptotic growth Mirzakhani controlled.
- Describe Weil–Petersson volumes of moduli spaces as geometric measures on the space of shapes.
- Sketch what **earthquake flow** is and what **ergodicity** means at slogan level (with Eskin).
- Link flat surfaces / polygonal billiards to the same orbit of ideas.
- Record accurately that Mirzakhani was the **first woman Fields medalist** (2014), and practice **LO6** caution: the medal cites a body of work, not one tweetable formula.

**Prerequisites.** Surfaces of genus $$g$$ (sphere, torus, double torus, …); the idea of a Riemannian metric and geodesic length; comfort with asymptotic notation $$f(L)\sim c L^k$$. No prior Teichmüller theory assumed.

**Seminar links.** Course outcomes **LO1** (hard modern programs) and **LO6** (precision vs hype in medal narratives). Geometry cousins: [Perelman / Ricci flow]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) (evolving metrics), [Beautiful Mathematics / infinity and shape]({{ site.baseurl }}/contents/en/chapter04/04_02_Infinity/), [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/). Dynamics cousins in Ch.08: [Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/). Flat surfaces touch explorations in [tilings]({{ site.baseurl }}/contents/en/chapter04/04_10_Tilings/) and billiard intuition.

---

## 1. Riemann surfaces, hyperbolic metrics, and “shape”

A **closed Riemann surface** is a compact oriented surface without boundary equipped with a complex structure (locally like open sets in $$\mathbb{C}$$, with holomorphic transition maps). Topologically, for each integer $$g\ge 0$$ there is one closed orientable surface of **genus** $$g$$: sphere ($$g=0$$), torus ($$g=1$$), double torus ($$g=2$$), and so on. The Euler characteristic is

$$
\chi = 2-2g.
$$

For $$g\ge 2$$ one has $$\chi<0$$. By the uniformization theorem, every such surface admits a **hyperbolic metric** of constant curvature $$-1$$, unique up to isometry in its conformal class. Geodesics on that metric are the “straightest” curves; a **closed geodesic** is a closed curve that is locally length-minimizing.

**Simple** closed geodesics do not self-intersect. On a hyperbolic surface they are rigid geometric objects: each free homotopy class of essential simple closed curves contains a unique geodesic representative, and its length is a geometric invariant of the marked surface.

Why care? Length spectra encode shape. Counting geodesics of bounded length is a geometric cousin of counting primes of bounded size: both ask how discrete invariants distribute as a continuous parameter grows.

---

## 2. Teichmüller space versus moduli space

Two layers of “space of surfaces” must be distinguished carefully.

**Teichmüller space** $$\mathcal{T}_g$$ parametrizes hyperbolic (or complex) structures on a fixed topological surface of genus $$g$$, up to isotopy—equivalently, marked Riemann surfaces. Markings remember how the surface is identified with a reference surface, so $$\mathcal{T}_g$$ is simply connected and contractible in the classical picture; it is a real manifold of dimension

$$
\dim_{\mathbb{R}}\mathcal{T}_g = 6g-6 \qquad(g\ge 2).
$$

**Moduli space** $$\mathcal{M}_g$$ is the space of unmarked isomorphism classes: surfaces up to biholomorphism (or isometry of hyperbolic metrics). Formally one may think of

$$
\mathcal{M}_g \;\simeq\; \mathcal{T}_g / \mathrm{Mod}_g,
$$

where $$\mathrm{Mod}_g$$ is the **mapping class group** of isotopy classes of orientation-preserving homeomorphisms. Points of $$\mathcal{M}_g$$ are pure shapes; points of $$\mathcal{T}_g$$ are shapes with a labeling of curves and a deformation history.

**LO6 caution.** Popular articles sometimes say “moduli space is the surface.” It is not. A surface is a point; moduli space is a higher-dimensional geometric universe of such points. Confusing the two is the single most common seminar error.

---

## 3. Counting simple closed geodesics

Fix a hyperbolic surface $$X$$ of genus $$g\ge 2$$. Let $$N_X(L)$$ be the number of **simple** closed geodesics on $$X$$ of length at most $$L$$. (There are infinitely many closed geodesics if one allows self-intersections; simplicity makes the count finite for each $$L$$ and geometrically more rigid.)

Mirzakhani proved asymptotic formulas of the shape

$$
N_X(L) \;\sim\; c_X\, L^{6g-6} \qquad(L\to\infty),
$$

where the exponent $$6g-6$$ is exactly the real dimension of Teichmüller / moduli space, and the constant $$c_X$$ is expressed in terms of geometric data of $$X$$ (related to frequencies of curves in the unit ball of a length pairing). More refined counts distinguish topological types of curves (separating vs non-separating, fixed pants decompositions, etc.).

The method is not “draw the surface and list curves.” It integrates geometric measures over moduli space, uses recursive structure of surfaces cut along simple curves (pairs of pants decompositions), and exploits the relationship between length functions and Weil–Petersson symplectic geometry.

**Seminar moral.** A counting problem on one surface is solved by understanding a measure on the *space of all surfaces*. That leap—from object to moduli—is characteristic of Mirzakhani’s style.

---

## 4. Weil–Petersson volumes of moduli spaces

The **Weil–Petersson** (WP) symplectic form endows moduli (and Teichmüller) space with a natural volume element coming from hyperbolic geometry / complex analysis. Let $$V_{g,n}(L_1,\ldots,L_n)$$ denote the WP volume of the moduli space of genus-$$g$$ surfaces with $$n$$ geodesic boundary components of prescribed lengths $$L_i$$ (or equivalently, with punctures and length constraints in the compactification language).

Mirzakhani established recursive formulas for these volumes, relating $$V_{g,n}$$ to volumes of simpler surfaces obtained by cutting along simple closed curves. The recursions are explicit enough to compute volumes for many $$(g,n)$$ and to prove polynomiality in the length variables. Volumes enter counting theorems because integrating “how many curves of length $$\le L$$” against a measure on moduli is dual to asking “how large is the set of surfaces admitting a short curve of a given type.”

A schematic identity of the philosophy (not a full theorem statement) is:

$$
\text{curve counts on a typical }X
\quad\longleftrightarrow\quad
\text{geometry of WP volume on }\mathcal{M}_g.
$$

Connection to physics and random surfaces: WP volumes appear in 2D quantum gravity and related matrix-model stories; Mirzakhani’s recursions sharpened the mathematical side of that dictionary. For this seminar, retain the geometric meaning: volumes are not decorative—they are the integration engine for counting.

---

## 5. Earthquake flow and ergodicity (with Eskin)

**Thurston’s earthquake deformations** twist a hyperbolic surface along a measured geodesic lamination, producing a continuous family of new hyperbolic structures. Restricting to suitable laminations and normalizing, one obtains a flow on a bundle over moduli space—the **earthquake flow**—analogous in spirit to geodesic flow on a manifold, but built from shearing along curves rather than walking along a tangent vector of Teichmüller space.

**Ergodicity** of a flow means (roughly) that time averages along almost every orbit equal space averages: the flow mixes the space so thoroughly that long-term statistics are determined by the invariant measure alone.

With **Alex Eskin**, Mirzakhani proved that earthquake flow is ergodic (with respect to the natural measure in the setting they treat). The theorem links Thurston’s geometric constructions to measurable dynamics at the level of Fields-depth analysis. It sits in a broader 2010s revolution in **Teichmüller dynamics**: orbit closures of flat surfaces, classification of invariant measures, and rigidity phenomena (Eskin–Mirzakhani–Mohammadi and related work form a major constellation).

You need not absorb the full measure classification here. Hold the slogan: **deformations that look purely geometric can be studied as dynamical systems with ergodic theorems**, and those theorems feed back into geometric counting and equidistribution.

---

## 6. Flat surfaces, strata, and billiards

A parallel language uses **translation surfaces** (flat metrics with conical singularities, equivalently abelian differentials on Riemann surfaces). The moduli space of such flat surfaces decomposes into **strata** by singularity type. $$\mathrm{SL}_2(\mathbb{R})$$ acts by linear post-composition on charts; orbits encode renormalization of the flat structure.

**Polygonal billiards** connect via unfolding: a trajectory in a rational polygon unfolds to a straight line on a translation surface. Questions about periodic billiard paths, diffusion, and ergodicity of the directional flow translate into orbit problems on strata.

Mirzakhani’s circle of ideas—moduli, dynamics, counting—interacts with this flat world even when individual papers emphasize hyperbolic rather than flat metrics. Seminar takeaway: “billiards” is not a toy side quest; it is a concrete dynamical laboratory for the same moduli machinery.

---

## 7. Fields Medal 2014 and historical notes

The IMU awarded Mirzakhani the Fields Medal in 2014 for outstanding contributions to the dynamics and geometry of Riemann surfaces and their moduli spaces. She was the first woman and the first Iranian mathematician to receive the medal. She died in 2017; her influence continues through the problems she opened and the community she inspired.

**Collaborators.** Major theorems are often joint—especially dynamical results with Eskin and others. **LO6:** always check coauthorship before writing “Mirzakhani alone proved …” for a specific statement.

**What the medal is not.** It is not “she counted curves on a donut.” It is recognition of a program that made moduli spaces computable, dynamical, and countable in precise asymptotic senses.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Moduli space is the surface itself.” | A point of moduli space *is* a surface (up to isomorphism); the space is the collection of all such points. |
| “Teichmüller space and moduli space are the same.” | Teichmüller remembers markings; moduli quotients by the mapping class group. |
| “She only counted geodesics.” | Volume recursion, earthquake dynamics, and flat-surface interactions are equally central. |
| “Simple closed geodesics are just any closed curves.” | Simple means non-self-intersecting; geodesics are length-minimizing representatives. |
| “Ergodicity means every orbit is dense.” | Ergodicity is a measure-theoretic statement; density of orbits is related but not identical. |
| “First woman Fields = only story that matters.” | Biography matters culturally; the mathematics is the syllabus reason we are here. |

---

## Exercises

1. For $$g=2$$, compute $$6g-6$$ and interpret it as a dimension of the space of shapes. Why is the exponent in geodesic counting the same number?
2. Explain “space of shapes” to a classmate using the torus of revolution: what data might distinguish two different flat (or hyperbolic, after punching) geometries?
3. Define a simple closed geodesic in one careful sentence. Give an example of a closed curve that is *not* simple.
4. Why might a recursive formula for WP volumes of moduli with boundary help count curves on a closed surface?
5. State what ergodicity of a flow means in informal language (time average = space average). Why would one care for earthquake deformations?
6. **LO6 (≤250 words):** Find a popular article about Mirzakhani’s medal. Quote one sentence that is precise and one that is vague or overclaimed; rewrite the vague sentence accurately.
7. Sketch how unfolding a square billiard produces a flat torus; then ask (without solving) what harder polygons force higher-genus translation surfaces.
8. Stretch: look up “pairs of pants decomposition” and explain in three sentences how cutting a genus-$$g$$ surface into pants organizes length coordinates.

---


## Video sources (math-video-researcher pack)

Full ranking: `research/video-research/Mirzakhani_Moduli/`.

**Recommended order**

1. **Orientation** — Quanta/Simons, *Maryam Mirzakhani: A Tenacious Explorer of Abstract Surfaces*: [YouTube](https://www.youtube.com/watch?v=qNuh4uta8oQ).  
2. **Profile** — Quanta article: [A Tenacious Explorer of Abstract Surfaces](https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/).  
3. **Core** — IAS Morse lecture listing (moduli dynamics): [IAS](https://www.ias.edu/ideas/dynamics-moduli-spaces-curves-i).  
4. **Frontier reading** — Eskin–Mirzakhani “magic wand”: [arXiv:1302.3320](https://arxiv.org/abs/1302.3320).

**Status reminder:** Major moduli/dynamics theorems **proved**; moduli geometry remains an active field. Biography is culturally important; the syllabus reason is the mathematics.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Mirzakhani_Moduli/transcripts/` · status: `research/video-research/Mirzakhani_Moduli/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Mirzakhani_Moduli_qNuh4uta8oQ_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


Full URL bibliography from video research (including secondary finds): `research/video-research/Mirzakhani_Moduli/references.md`.

### Complete URL list (audit)

1. https://www.youtube.com/watch?v=qNuh4uta8oQ  
2. https://www.ias.edu/ideas/dynamics-moduli-spaces-curves-i  
3. https://arxiv.org/abs/1302.3320  
4. https://arxiv.org/abs/1305.3015  
5. https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/  
6. https://en.wikipedia.org/wiki/Maryam_Mirzakhani  
7. https://celebratio.org/Mirzakhani_M/article/1087/  
8. https://terrytao.wordpress.com/tag/maryam-mirzakhani/  
9. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014  
10. https://arxiv.org/search/?query=Mirzakhani+Weil-Petersson&searchtype=all  
11. https://news.stanford.edu/stories/2014/08/surfaces-mirzakhani-081214  

### Research pack

12. Course pack: `research/video-research/Mirzakhani_Moduli/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. IMU Fields Medal 2014 citation — Maryam Mirzakhani.
2. M. Mirzakhani — thesis and papers on Weil–Petersson volumes and counting simple closed geodesics.
3. A. Eskin & M. Mirzakhani — ergodicity of earthquake flow; related dynamics papers.
4. Surveys on Teichmüller dynamics, strata of abelian differentials, and orbit closures (various authors; lecture notes from graduate summer schools).
5. W. Thurston — foundations of earthquake deformations and measured laminations (background).
6. Course cross-links: [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/), [Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/), [Strange geometry]({{ site.baseurl }}/contents/en/chapter04/04_06_Strange_Geometry/).

---

## Further directions

- Read a short survey on WP volume recursions and compute a low-genus volume by hand if a formula is supplied in the survey.
- Explore flat surfaces and rational billiards as a sister seminar topic; compare counting periodic trajectories with counting simple geodesics.
- Compare Mirzakhani’s “moduli as a dynamical arena” with homogeneous dynamics in the [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/) essay—different spaces, shared ergodic philosophy.
- For LO6 practice, contrast a technical introduction with a memorial profile; keep both genres, but grade yourself on not confusing them.
