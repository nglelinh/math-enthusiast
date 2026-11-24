---
layout: post
title: "Venkatesh: Number Theory Meets Representation Theory (Fields Medal 2018)"
chapter: '02'
order: 8
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Imagine walking into an old library where four scholars sit in four separate rooms, each staring at an apparently unrelated puzzle. In the first room, an analytic number theorist is fighting to bound the size of a wild oscillating $$L$$-function along the critical line. In the second room, a dynamicist is watching points drift across a curved space of lattices, asking whether their trajectory visits every region fairly. In the third room, a representation theorist is decomposing wave harmonics on a matrix group. In the fourth room, a topologist is counting strange "torsion" holes inside a high-dimensional manifold.

**Akshay Venkatesh** won the **Fields Medal in 2018** because he walked into that library, tore down the walls between the four rooms, and showed that **all four scholars were staring at different shadows of the same mathematical object**.

In Venkatesh’s hands, questions about values of $$L$$-functions, the equidistribution of integer points on spheres, and the cohomology of arithmetic manifolds all turn into questions about group orbits and spectral analysis on arithmetic quotients such as

$$
\mathrm{SL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{Z}).
$$

This essay focuses on **synthesis as a mathematical method** just as much as on any single headline theorem. Subconvexity bounds for $$L$$-functions, sparse equidistribution, and the topology of locally symmetric spaces are three windows onto one unified toolkit—a reminder that a Fields Medal is earned by concrete theorems and new bridges, not by a vague reputation for breadth.

---

## Learning objectives

After this lecture you should be able to:

- Give concrete examples of problems that sit at the crossroads of **number theory** and **dynamics**.
- Explain **homogeneous dynamics** intuitively using the space of unimodular lattices $$\mathrm{SL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{Z})$$.
- Compute by hand why the **convexity bound** for the Riemann zeta function has exponent $$1/4$$, and explain why breaking past it (**subconvexity**) matters.
- Describe **sparse equidistribution**—uniform distribution along thin sequences—and illustrate how integer points spread across spheres $$x^2+y^2+z^2=D$$.
- Connect **locally symmetric spaces** to topology (cohomology, torsion) and automorphic forms.
- Articulate Venkatesh’s **synthesis style**: moving a stuck problem into whichever mathematical language offers cancellation or rigidity, then translating the answer back.

**Prerequisites.** Modular arithmetic and the basic idea of modular forms; linear algebra of $$\mathrm{SL}_n$$; elementary Fourier / spectral intuition. No prior course in ergodic theory is required—orbits and averages are introduced from scratch.

**Related lessons.** Neighbors in this course: [Langlands program]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/), [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) ($$L$$-functions culture), [Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/) (structure vs. randomness via a different engine), [Mirzakhani moduli dynamics]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) (dynamics on moduli spaces vs. homogeneous spaces), [Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/) (the homogeneous dynamics lineage), and [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/) ($$L$$-functions of elliptic curves).

---

## Background Knowledge Map: What Are the Fields Behind Venkatesh’s Work?

If you graduated in engineering, computer science, or mathematics, you may have met linear algebra, differential equations, and Fourier transforms—yet never seen how they fuse into modern number theory. Venkatesh’s work sits at the intersection of three major disciplines.

### 1. Analytic Number Theory & $$L$$-Functions: Listening to the Music of Integers
**What is it?** Rather than studying equations one integer at a time, analytic number theory packages arithmetic data—prime numbers, counts of integer points on curves, coefficients of modular forms—into complex-analytic generating functions called **$$L$$-functions**, such as the Riemann zeta function $$\zeta(s) = \sum_{n=1}^{\infty} n^{-s}$$.

**What does it study?**
- **Zeros and poles:** Where $$L(s)$$ vanishes controls error terms in counting primes (the Riemann Hypothesis is the flagship mystery).
- **Size estimates (subconvexity):** How large can $$\lvert L(\tfrac{1}{2}+it)\rvert$$ grow as $$t \to \infty$$ or as the arithmetic complexity (conductor) grows? Tighter bounds mean stronger cancellation between oscillating terms.
- **Equidistribution:** When integer solutions exist, do they clump in one corner of space or spread out evenly?

### 2. Homogeneous Dynamics: Billiards on a Space of Lattices
**What is it?** A **homogeneous space** is a curved arena $$G/\Gamma$$ built by taking a continuous symmetry group $$G$$ (such as $$\mathrm{SL}_n(\mathbb{R})$$, all $$n\times n$$ real matrices of determinant $$1$$) and modding out by a discrete lattice $$\Gamma$$ (such as $$\mathrm{SL}_n(\mathbb{Z})$$, integer matrices of determinant $$1$$).

**What does it study?**
- **Group flows:** Multiplying on the left by a one-parameter family of matrices $$g_t \in G$$ moves points along orbits $$g_t \cdot x$$, much like watching a billiard ball bounce inside a curved room.
- **Ergodicity and mixing:** Does a typical orbit spend equal fractions of time in regions of equal volume? How fast do correlations decay?
- **Rigidity:** Unlike chaotic flows on generic manifolds, unipotent matrix flows on $$G/\Gamma$$ are extraordinarily rigid—Ratner’s theorems classify every possible orbit closure, turning dynamical statements into sharp arithmetic theorems.

### 3. Representation Theory & Topology of Locally Symmetric Spaces
**What is it?** Take the quotient $$X = \Gamma \backslash G / K$$ (where $$K$$ is a maximal compact subgroup, like rotations $$\mathrm{SO}_n(\mathbb{R})$$). You obtain a geometric manifold (or orbifold) called a **locally symmetric space**—the hyperbolic modular surface $$\mathrm{SL}_2(\mathbb{Z})\backslash \mathbb{H}$$ is the simplest example.

**What does it study?**
- **Harmonic analysis on $$G/\Gamma$$:** Just as a violin string vibrates in sine waves, functions on $$G/\Gamma$$ decompose into irreducible representations of $$G$$ (**automorphic forms**).
- **Cohomology and torsion:** Topological invariants—holes and "twists" (torsion classes) in the homology of $$\Gamma\backslash G/K$$—turn out to encode deep Galois and motivic invariants in number theory.

---

## 1. Automorphic forms and arithmetic quotients

Classical modular forms are holomorphic functions on the upper half-plane $$\mathbb{H}$$ with transformation laws under subgroups of $$\mathrm{SL}_2(\mathbb{Z})$$. They produce $$L$$-functions whose special values and analytic growth encode arithmetic (Fourier coefficients, point counts over finite fields, ranks of elliptic curves).

In higher rank, one studies **automorphic forms** on groups such as $$\mathrm{GL}_n$$: functions on the adelic quotient

$$
G(\mathbb{Q})\backslash G(\mathbb{A})
$$

or, in a classical real-variable picture, functions on **locally symmetric spaces**

$$
\Gamma\backslash G/K,
$$

where $$G$$ is a semisimple Lie group, $$K$$ a maximal compact subgroup, and $$\Gamma$$ an arithmetic lattice (for example, $$\mathrm{SL}_n(\mathbb{Z})$$ inside $$\mathrm{SL}_n(\mathbb{R})$$).

The geometry of $$\Gamma\backslash G/K$$ carries three interlocking layers of arithmetic information:

- **Spectrum of the Laplacian / Casimir operator:** Eigenvalues correspond to automorphic forms and govern mixing rates.
- **Closed geodesics and periodic orbits:** Their lengths and distributions encode class numbers and periods of quadratic fields.
- **Cohomology and homology:** Topological invariants of $$\Gamma\backslash G/K$$ carry Galois representations and special $$L$$-values.

**Takeaway.** Number-theoretic objects (modular forms, $$L$$-functions) are simultaneously spectral and geometric objects on arithmetic quotients. Venkatesh’s work exploits that dictionary in both directions.

---

## 2. Homogeneous dynamics: $$\mathrm{SL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{Z})$$

A **homogeneous space** for our purposes is a quotient $$G/\Gamma$$ where a Lie group $$G$$ acts transitively. The flagship example is

$$
X_n = \mathrm{SL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{Z}),
$$

which parametrizes **unimodular lattices** in $$\mathbb{R}^n$$ (discrete grids of covolume $$1$$).

### Hand-Verifiable Example 1: Watching a 2D Lattice Stretch and Shear
Take $$n=2$$. Every matrix $$g \in \mathrm{SL}_2(\mathbb{R})$$ defines a 2D lattice $$g\mathbb{Z}^2 \subset \mathbb{R}^2$$ whose fundamental parallelogram has area $$\det(g)=1$$. Multiplying $$g$$ on the right by an integer matrix $$\gamma \in \mathrm{SL}_2(\mathbb{Z})$$ merely picks a different basis for the **exact same lattice**—that is why the space of all unit-area lattices is the quotient $$X_2 = \mathrm{SL}_2(\mathbb{R})/\mathrm{SL}_2(\mathbb{Z})$$.

Now act on the left by two famous one-parameter matrix families:

1. **The geodesic (diagonal) flow:**
   $$
   a_t = \begin{pmatrix} e^t & 0 \\ 0 & e^{-t} \end{pmatrix}.
   $$
   Applying $$a_t$$ stretches the horizontal axis by $$e^t$$ and squeezes the vertical axis by $$e^{-t}$$, keeping the area $$e^t \cdot e^{-t} = 1$$ intact. On the standard square lattice $$\mathbb{Z}^2$$, as $$t$$ grows, horizontal basis vectors stretch while vertical ones collapse—corresponding to shooting straight up into the cusp of the modular surface.
2. **The horocycle (unipotent) flow:**
   $$
   u_s = \begin{pmatrix} 1 & s \\ 0 & 1 \end{pmatrix}.
   $$
   Applying $$u_s$$ shears the lattice horizontally by $$s$$. Watch what happens to the standard square lattice $$\mathbb{Z}^2$$ when $$s=1$$: the basis vectors $$(1,0)$$ and $$(0,1)$$ become $$(1,0)$$ and $$(1,1)$$, which span the **exact same square lattice**! So $$u_s \cdot \mathbb{Z}^2$$ is a periodic orbit of period $$1$$. By contrast, if you start at a lattice with an irrational slope, the sheared orbit $$u_s \cdot x$$ winds densely and equidistributes across the entire space $$X_2$$.

Classic triumphs of this viewpoint include Minkowski’s geometry of numbers reinterpreted via compact sets in $$X_n$$, Margulis’s proof of the Oppenheim conjecture using unipotent flows, and Duke–Rudnick–Sarnak’s equidistribution of integer points on varieties. Venkatesh pushed this engine further by proving **effective** and **sparse** equidistribution theorems and converting them into sharp analytic bounds for $$L$$-functions.

**Contrast with Mirzakhani.** In [Mirzakhani’s work]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), the ambient arena is the moduli space of Riemann surfaces (which is *not* homogeneous); here it is a homogeneous space of lattices. Yet both share the same deep strategy: **embed an arithmetic or geometric counting question inside a space with a group action, then prove equidistribution**.

---

## 3. Subconvexity of $$L$$-functions

An $$L$$-function $$L(s,\pi)$$ attached to an automorphic form (or Dirichlet character) is a Dirichlet series with an analytic continuation and a functional equation relating $$s$$ to $$1-s$$. Understanding its size on the critical line $$\operatorname{Re}(s)=\tfrac{1}{2}$$ is one of the central problems of analytic number theory.

### Hand-Verifiable Example 2: Computing the Convexity Exponent $$1/4$$ for $$\zeta(s)$$
Why is the **convexity bound** so easy to state, and why is beating it so hard? Let us calculate it by hand for the Riemann zeta function $$\zeta(\sigma + it)$$ as $$\lvert t\rvert \to \infty$$:

- **Right edge ($$\sigma = 1$$):** The series $$\sum n^{-1-it}$$ barely diverges at $$t=0$$, and for large $$\lvert t\rvert$$ it grows at most logarithmically: $$\lvert \zeta(1 + it)\rvert \ll \lvert t\rvert^{\varepsilon}$$ (exponent $$0$$).
- **Left edge ($$\sigma = 0$$):** The functional equation links $$\zeta(it)$$ to $$\zeta(1-it)$$ through a Gamma factor whose size by Stirling’s formula is $$\lvert t\rvert^{1/2}$$. Therefore $$\lvert \zeta(it)\rvert \ll \lvert t\rvert^{1/2 + \varepsilon}$$ (exponent $$1/2$$).
- **Midpoint ($$\sigma = \tfrac{1}{2}$$):** Complex analysis (the **Phragmén–Lindelöf convexity principle**) says that on a vertical strip, the growth exponent is at most the **linear interpolation** of the two boundary exponents! Midway between $$0$$ and $$1/2$$ sits

$$
\theta_{\mathrm{convex}} = \frac{1}{2}\left(\frac{1}{2} + 0\right) = \frac{1}{4},
\qquad\text{so}\qquad
\left\lvert \zeta\!\left(\tfrac{1}{2} + it\right)\right\rvert \ll \lvert t\rvert^{1/4 + \varepsilon}.
$$

That $$1/4$$ is the **convexity bound**—what you get "for free" purely from the functional equation without exploiting any deeper cancellation. Any exponent strictly smaller than $$1/4$$—say,

$$
\lvert L(s_0,\pi)\rvert \;\ll\; C^{\theta},
\qquad
\theta < \theta_{\mathrm{convex}},
$$

where $$C$$ is the analytic conductor—is called a **subconvexity bound**.

Breaking the convexity barrier (even by a tiny $$\delta > 0$$) is famously difficult because it demands proving genuine **oscillatory cancellation** beyond symmetry alone. Together with Philippe Michel, Venkatesh solved the general subconvexity problem for $$\mathrm{GL}_2$$ $$L$$-functions over arbitrary number fields—not by classical exponential-sum gymnastics alone, but by translating the $$L$$-function into an integral period on a homogeneous space and harnessing **spectral gap and mixing** from representation theory and dynamics.

**Careful about the Riemann Hypothesis.** The [Riemann Hypothesis]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) implies the Lindelöf Hypothesis (exponent $$0+\varepsilon$$, the ultimate subconvexity). Subconvexity theorems prove weaker exponents **unconditionally**—a huge step forward, but distinct from proving RH.

---

## 4. Sparse equidistribution and integer points on spheres

Equidistribution means that a sequence of points spreads out uniformly with respect to a natural measure. Classical Weyl equidistribution studies $$\{n\alpha\} \bmod 1$$ on the circle. In homogeneous dynamics, one studies orbits $$g_t \cdot x \in G/\Gamma$$.

**Sparse equidistribution** asks a much harder question: if you sample an orbit only along a **thin subset** of times—such as $$n^2$$, prime numbers, or a sparse algebraic sequence—does the sample *still* become uniformly distributed? Standard ergodic theorems fail immediately because a thin sequence has density zero inside the full flow.

### Hand-Verifiable Example 3: Integer Points Spreading Evenly on Spheres $$x^2+y^2+z^2=D$$
To feel equidistribution with your bare hands, count integer solutions $$(x,y,z)\in\mathbb{Z}^3$$ to the sphere equation $$x^2+y^2+z^2=D$$, then project them onto the unit sphere $$S^2$$ by dividing by $$\sqrt{D}$$:

- **$$D = 3$$:** The only squares summing to $$3$$ are $$1+1+1$$. Choosing signs $$(\pm 1, \pm 1, \pm 1)$$ gives $$2^3 = 8$$ points—the vertices of a cube inscribed in $$S^2$$.
- **$$D = 5$$:** We need $$2^2 + 1^2 + 0^2 = 5$$. There are $$3! = 6$$ ways to permute $$(2,1,0)$$ and $$2^2 = 4$$ sign choices for the two nonzero coordinates, giving $$6 \times 4 = 24$$ points on $$S^2$$.
- **$$D = 14$$:** We need $$3^2 + 2^2 + 1^2 = 14$$. Permuting $$(3,2,1)$$ gives $$3! = 6$$ arrangements and choosing signs gives $$2^3 = 8$$ choices, yielding $$6 \times 8 = 48$$ points on $$S^2$$.

As $$D \to \infty$$ (avoiding $$D \equiv 0, 4, 7 \pmod 8$$ where obstructions occur), Duke proved in 1988—using half-integral weight modular forms and subconvexity—that these projected points **equidistribute** across the entire unit sphere $$S^2$$: any patch covering $$10\%$$ of the sphere’s surface area captures approximately $$10\%$$ of the integer points!

Venkatesh’s breakthrough in **sparse equidistribution** showed that even when you thin out orbits dramatically (using spectral gaps, quantitative mixing, and additive structure), equidistribution often survives—unlocking new bounds for representation numbers, Heegner points, and special cycles.

---

### Deep-Dive Explanation: How Venkatesh Turns Number Theory into Dynamics (Read Slowly)

Why does a question about prime numbers or $$L$$-functions suddenly yield to matrix flows on $$\mathrm{SL}_n(\mathbb{R})/\mathrm{SL}_n(\mathbb{Z})$$? Follow the four-step engine below slowly:

#### Step 1: Translate the arithmetic sum into a geometric period
Suppose you want to estimate an $$L$$-function value $$L(\tfrac{1}{2}, \pi)$$ or count integer points on a sphere. Instead of staring at a raw infinite sum $$\sum a_n n^{-1/2}$$, represent that value as an **integral** (a *period*) of an automorphic form $$\varphi$$ over a geometric cycle or orbit inside $$G/\Gamma$$. Now the arithmetic quantity is literally an average of a wave along a geometric path.

#### Step 2: Decompose the wave into spectral frequencies (representation theory)
Just as Fourier analysis breaks a sound wave into pure frequencies, the Hilbert space $$L^2(G/\Gamma)$$ splits into irreducible representations of $$G$$. Crucially, the constant function (the uniform average) is separated from all non-constant oscillating waves by a **spectral gap**: non-trivial waves cannot linger near zero frequency.

#### Step 3: Let the group flow mix and cancel oscillations (homogeneous dynamics)
Because of the spectral gap, acting on the wave by matrix flows $$g_t$$ causes correlations between distant points to decay **exponentially fast** (quantitative mixing). Even if you only sample along a sparse subset of times, the fast decay of correlations forces the oscillating error terms to cancel out—producing a strict saving over the naive convexity bound!

#### Step 4: Translate cancellation back into an arithmetic theorem
Reversing Step 1, that dynamical saving becomes a **subconvexity bound** $$\lvert L(\tfrac{1}{2},\pi)\rvert \ll C^{\theta_{\mathrm{convex}}-\delta}$$, an equidistribution theorem for integer points, or a structural relation for cohomology classes.

In one schematic line:

$$
\text{Arithmetic sum / }L\text{-value}
\;\xrightarrow{\;\text{period integral}\;}\;
\text{Wave on }G/\Gamma
\;\xrightarrow{\;\text{spectral gap + mixing}\;}\;
\text{Cancellation}
\;\xrightarrow{\;\text{translate back}\;}\;
\text{Subconvexity \& equidistribution}.
$$

---

## 5. Topology of locally symmetric spaces

Locally symmetric spaces $$\Gamma\backslash G/K$$ are not only spectral arenas; they are topological manifolds (or orbifolds) with intricate cohomology. Key questions include:

- how Betti numbers grow as $$\Gamma$$ shrinks through a tower of congruence subgroups;
- how **torsion** (finite-order classes, such as elements satisfying $$p \cdot \alpha = 0$$) behaves in the homology of arithmetic groups;
- how characteristic classes and regulators link topology to special values of $$L$$-functions.

Venkatesh (in solo work and with collaborators such as Calegari, Prasanna, and Bergeron) discovered surprising **derived Hecke algebra** actions and conjectured deep links between the cohomology of locally symmetric spaces, motivic cohomology, and special values of adjoint $$L$$-functions. The takeaway for learners: the very same arithmetic groups that produce modular forms also build manifolds whose topological holes carry arithmetic meaning.

---

## 6. Synthesis as method

A fair one-sentence portrait of Venkatesh’s mathematical signature:

> Venkatesh solves arithmetic problems by moving them into dynamics, representation theory, or topology—whichever language yields cancellation or rigidity—and then translating the answer back.

Compare that shape of achievement with neighboring Chapter 2 stories:

- **Sieve-first prime pattern work** ([Maynard]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/), Zhang): sharp combinatorial weights tuned directly to primes.
- **Additive combinatorics transference** ([Green–Tao]({{ site.baseurl }}/contents/en/chapter02/02_04_Green_Tao/)): embedding primes inside a pseudorandom host.
- **Perfectoid rebuilds of $$p$$-adic geometry** ([Scholze]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/)): forging a new geometric foundation from scratch.

All are deep; the **architecture** differs. Learning from Venkatesh means developing the instinct to ask, whenever a calculation hits a wall: *is this problem stuck only because I am writing it in the wrong language?*

**Collaborators.** As is standard across modern synthesis, many landmark papers are joint (for instance, Michel–Venkatesh on $$\mathrm{GL}_2$$ subconvexity, Einsiedler–Lindenstrauss–Michel–Venkatesh on periodic orbits, Bergeron–Venkatesh on torsion growth, and Prasanna–Venkatesh on motivic cohomology).

---

## 7. Why it matters on the course map

Analytic number theory in the twenty-first century is inseparable from homogeneous dynamics and automorphic spectral theory. Venkatesh is a central architect of that fusion. Popular profiles often highlight that he "works across many fields," which is true—but the Fields Medal recognizes **concrete theorems and transferable methods** at the interfaces, not simply collecting subject labels.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “This is only about primes.” | $$L$$-functions, automorphic forms, equidistribution, and topology are central. |
| “Dynamics replaces analysis.” | Synthesis: dynamics, analysis, and representation theory cooperate. |
| “Subconvexity proves RH.” | Subconvexity is a weaker/related size bound; RH is about the exact location of zeros. |
| “Homogeneous space = moduli space of curves.” | Different geometries; both host dynamics relevant to Fields-level work. |
| “Sparse equidistribution means the set is dense.” | Equidistribution governs measure and proportions along a sequence, not merely topological density. |
| “One Fields style fits all 2018 medals.” | Scholze, Birkar, Figalli, and Venkatesh illustrate four distinct shapes of achievement in the same year. |

---

## Video sources (math-video-researcher pack)

Full ranking: `research/video-research/Venkatesh_Number_Theory/`.

**Recommended order**

1. **Profile** — Quanta: [A Number Theorist Who Bridges Math and Time](https://www.quantamagazine.org/fields-medalist-akshay-venkatesh-bridges-math-and-time-20180801/).  
2. **Core** — Fields Medal Symposium 2022 (Venkatesh): [YouTube](https://www.youtube.com/watch?v=4EEjHji6axA).  
3. **Institutional** — Stanford news: [link](https://news.stanford.edu/stories/2018/08/akshay-venkatesh-wins-fields-medal); IMU Fields 2018: [link](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018).

**Status reminder:** Citation emphasizes **synthesis** across analytic number theory, dynamics, topology, representation theory—not a single closed conjecture.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Venkatesh_Number_Theory/transcripts/` · status: `research/video-research/Venkatesh_Number_Theory/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Venkatesh_Number_Theory_4EEjHji6axA_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


Full URL bibliography from video research (including secondary finds): `research/video-research/Venkatesh_Number_Theory/references.md`.

### Complete URL list (audit)

1. https://www.youtube.com/watch?v=4EEjHji6axA  
2. https://www.quantamagazine.org/fields-medalist-akshay-venkatesh-bridges-math-and-time-20180801/  
3. https://news.stanford.edu/stories/2018/08/akshay-venkatesh-wins-fields-medal  
4. https://en.wikipedia.org/wiki/Akshay_Venkatesh  
5. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018  
6. https://www.ias.edu/scholars/venkatesh  
7. https://arxiv.org/search/?query=Venkatesh+subconvexity&searchtype=all  
8. https://arxiv.org/search/?query=Michel+Venkatesh&searchtype=all  
9. https://en.wikipedia.org/wiki/Homogeneous_dynamics  
10. https://en.wikipedia.org/wiki/Analytic_number_theory  

### Research pack

11. Course pack: `research/video-research/Venkatesh_Number_Theory/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. IMU Fields Medal 2018 citation — Akshay Venkatesh.
2. Selected papers and surveys on subconvexity, equidistribution, and arithmetic quotients (Venkatesh and collaborators).
3. Background: Duke–Rudnick–Sarnak; Einsiedler–Ward or other homogeneous dynamics introductions; Iwaniec–Kowalski for analytic $$L$$-function estimates.
4. Course cross-links: [Langlands]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/), [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/), [Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/), [Scholze]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/).

---

## Further directions

- Compare Venkatesh’s synthesis with Ngô / Langlands as different bridges between geometry/analysis and arithmetic.
- Explore a single equidistribution theorem (e.g. integer points on spheres or special orthogonal orbits) as a mini-project before returning to $$L$$-functions.
- For dynamics lovers: read an expository account of unipotent flows and Ratner-type rigidity, then ask which arithmetic applications need only mixing and which need classification of measures.
- Pair with [Maynard]({{ site.baseurl }}/contents/en/chapter02/02_09_Maynard_Primes/) in a seminar session on “two engines of analytic number theory: sieves vs dynamics/spectra.”

## Video tham khảo

- **xem trước** — [2022 Fields Medal Symposium: Akshay Venkatesh](https://www.youtube.com/watch?v=4EEjHji6axA) — Fields Institute, English. Watch first. “2022 Fields Medal Symposium: Akshay Venkatesh” orients the lesson’s aim: Give examples of problems that sit between number theory and dynamics.
