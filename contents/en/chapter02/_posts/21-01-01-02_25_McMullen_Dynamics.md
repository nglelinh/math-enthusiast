---
layout: post
title: "McMullen’s Holomorphic Dynamics and Teichmüller Geometry (Fields Medal 1998)"
chapter: '02'
order: 25
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Curtis T. McMullen** received the **Fields Medal 1998** at ICM Berlin. Unlike the 1990 and 1994 medals, 1998 carries an official short citation, and this course uses it verbatim:

> For his contributions to the theory of holomorphic dynamics and geometrization of three-manifolds, including proofs of Bers’ conjecture on the density of cusp points in the boundary of the Teichmüller space, and Kra’s theta-function conjecture.

This essay is for learners who have met Riemann surfaces and complex iteration at the level of Julia sets of quadratic polynomials and want the **architecture** that joins those pictures to Teichmüller theory and to Thurston’s program for hyperbolic 3-manifolds. It does **not** say that McMullen proved full geometrization or the Poincaré conjecture—that is [Perelman’s]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) completion of the Hamilton–Thurston program. McMullen’s 3-manifold work lives *inside* the Thurston culture: renormalization, rigidity, and hyperbolic structures on manifolds that fiber over the circle.

---

## Learning objectives

After this lecture you should be able to:

- State the official 1998 citation and name its two explicitly cited theorems (Bers density of cusps; Kra’s theta-function conjecture).
- Sketch **holomorphic dynamics** of a rational map: Julia set versus Fatou set, and why **renormalization** (Sullivan, Douady–Hubbard, then McMullen) is a machine rather than a single formula.
- Explain, at slogan level, **Teichmüller space** of a surface and what a **cusp** on Bers’s boundary is trying to be.
- Distinguish McMullen’s contributions to the **Thurston geometrization culture** from Perelman’s proof of full geometrization.
- Cross-link [Mirzakhani’s moduli]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/) as a later moduli-and-dynamics chapter (McMullen was Mirzakhani’s doctoral advisor—an accurate biographical fact, not a substitute for her theorems).
- Practice LO6: the medal is a *body of work* with two named conjectures, not “McMullen classified all Julia sets.”

**Prerequisites.** Holomorphic functions on $$\mathbb{C}$$ and the Riemann sphere $$\widehat{\mathbb{C}}$$; the idea of a compact Riemann surface of genus $$g\ge 2$$ with a hyperbolic metric; comfort with “iteration” as repeating a map. No prior Kleinian-group course is assumed.

**Seminar links.** LO1 (programs that reorganize geometry and dynamics together). Geometry cousins: [Mirzakhani / moduli]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/). Complex-dynamics landscape: Fatou, Julia, Sullivan, Douady–Hubbard, Thurston, Yoccoz.

---

## 1. Holomorphic dynamics: maps, Julia, Fatou, renormalization

A **rational map** $$f:\widehat{\mathbb{C}}\to\widehat{\mathbb{C}}$$ is a holomorphic self-map of the Riemann sphere, equivalently a ratio of polynomials. Iteration produces a discrete dynamical system $$z\mapsto f(z)\mapsto f^{\circ 2}(z)\mapsto\cdots$$. The **Fatou set** is the open set of points whose orbits are equicontinuous (normal families); the **Julia set** $$J(f)$$ is the complement, typically a fractal where nearby orbits diverge. Quadratic polynomials $$z\mapsto z^2+c$$ organize into the **Mandelbrot set** in the parameter plane: a dictionary, due especially to **Douady–Hubbard**, between combinatorial data and hyperbolic components.

**Renormalization** asks what happens when a small piece of the dynamics looks like a copy of a simpler map—classically, when an iterate restricted to a neighborhood of the critical point is **quadratic-like** in the Douady–Hubbard sense. **Sullivan** recast much of the theory in the language of Riemann surface laminations and measurable dynamics. McMullen’s book *Complex Dynamics and Renormalization* (Annals of Mathematics Studies **135**, 1994) develops infinitely renormalizable quadratic polynomials, rigidity, and the geometry of towers of quadratic-like maps. Steve Smale’s ICM 1998 lecture on the work emphasizes that, for density of hyperbolic polynomials in degree two, the finitely renormalizable case had been treated by **Yoccoz**; McMullen’s analysis addresses infinitely renormalizable points in the Mandelbrot set.

**Slogan.** Holomorphic dynamics is not only pictures of Julia sets. It is a rigidity theory: when two maps are combinatorially similar, geometric limits and expansion often force them to be the same, or force their Julia sets to be locally connected, or force hyperbolicity to be dense in a parameter slice.

McMullen’s doctoral work (Harvard, 1985, advisor **Dennis Sullivan**) already sat in this landscape: families of rational maps and iterative root-finding. The Fields citation names the broader theory, not a single algorithm.

---

## 2. Teichmüller space and Bers’s boundary

Let $$S$$ be a closed orientable surface of genus $$g\ge 2$$ (or a finite-type hyperbolic surface). **Teichmüller space** $$\mathcal{T}(S)$$ parametrizes marked hyperbolic structures—or equivalently marked Riemann surfaces—on the topological surface $$S$$. It is a finite-dimensional cell (real dimension $$6g-6$$ for a closed surface of genus $$g$$). The **mapping class group** acts, and the quotient is moduli space; that is the setting of the [Mirzakhani lecture]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/).

**Bers** embedded Teichmüller space as a bounded domain in a space of holomorphic quadratic differentials (the Bers embedding). The **Bers boundary** is the frontier of that embedding. Points on the boundary correspond to (typically degenerate) Kleinian groups: limits of quasifuchsian representations in which some curves on the surface have been pinched. A **maximal cusp** is a geometrically finite limit in which a maximal system of disjoint simple closed curves has been pinched to rank-one cusps.

**Bers’s conjecture**, in the form McMullen proved, is that **cusps are dense** in this boundary: maximal cusps are dense in Bers’s boundary of Teichmüller space. McMullen’s paper “Cusps are dense,” *Ann. of Math.* **133** (1991), proves the density. The argument uses an estimate for the algebraic effect of a unit quasiconformal deformation supported in the thin part of the surface—pinching is not an infinitely delicate operation; it can be approximated from the interior densely.

**Slogan.** The “edge” of the space of nice hyperbolic surfaces is populated, densely, by surfaces that have been pinched along curves until those curves become cusps. Degeneration is not rare; it is typical on the boundary.

This is a theorem about the *boundary of Teichmüller space*, not a classification of all 3-manifolds.

---

## 3. Kra’s theta-function conjecture

A covering of hyperbolic Riemann surfaces $$Y\to X$$ induces an inclusion of Teichmüller spaces $$\mathcal{T}(X)\hookrightarrow\mathcal{T}(Y)$$. Whether that inclusion is an isometry or a contraction for the Teichmüller metric depends on the covering. McMullen proved that the inclusion is an isometry if the covering is **amenable**, and strictly contracting otherwise (*Invent. Math.* **97**, 1989).

A classical special case is the Poincaré series operator $$\Theta$$ that averages a holomorphic quadratic differential on the disk down to a finite-type surface. **Kra’s theta-function conjecture** asserted that this operator is a strict contraction: $$\|\Theta\|<1$$ for classical Poincaré series. McMullen proved the conjecture as a consequence of the amenability criterion.

The citation names this theorem because it is a sharp analytic fact with geometric consequences: contraction estimates feed later work on iteration on Teichmüller space and on rigidity of hyperbolic structures. Smale’s ICM lecture notes that, armed with the theta-conjecture work, McMullen could contribute substantially to Thurston’s program of putting hyperbolic metrics on a large class of 3-manifolds.

---

## 4. Geometrization culture—not Perelman’s theorem

**Thurston’s geometrization conjecture** proposed that every closed 3-manifold decomposes into pieces, each carrying one of eight homogeneous geometries; the hyperbolic pieces are the deepest. Thurston proved large parts of the program (notably for Haken manifolds). **Perelman** proved the full conjecture via Ricci flow with surgery, implying the Poincaré conjecture; see [the Perelman lecture]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/).

McMullen’s contribution is of a different species. The 1996 book *Renormalization and 3-Manifolds Which Fiber over the Circle* (Annals of Mathematics Studies **142**) gives a unified treatment of two constructions: fixed points of renormalization in complex dynamics, and hyperbolic structures on 3-manifolds that **fiber over the circle**. Both are studied through geometric limits and rigidity. Open hyperbolic manifolds are shown to be inflexible in a quantitative sense that complements Mostow rigidity. This is the “geometrization of three-manifolds” clause in the citation: a renormalization-and-rigidity approach inside Thurston’s program, especially for fibered manifolds—not a claim that McMullen closed geometrization in full.

**Accuracy sentence for this course.** McMullen worked *in* the geometrization program; Perelman *finished* geometrization (and Poincaré). Those are compatible statements.

---

## 5. Why the two named conjectures sit together

Bers density and Kra’s contraction look like analysis on Teichmüller space. Holomorphic dynamics looks like iteration on the sphere. The unity is **rigidity of conformal dynamical systems**, whether the system is a rational map or a Kleinian group (a discrete subgroup of $$\mathrm{PSL}(2,\mathbb{C})$$ acting on the Riemann sphere and on hyperbolic 3-space). Sullivan’s dictionary between the two subjects is the cultural background; McMullen’s theorems are concrete contractions, densities, and geometric limits that make the dictionary produce proofs.

The same sensibility later appears in McMullen’s students’ work—including **Maryam Mirzakhani**—on moduli, dynamics, and hyperbolic surfaces. Cite that as lineage, then send the reader to [Mirzakhani’s own theorems]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/).

---

## 6. Why a Fields Medal

1. **Named, long-open points.** Density of cusps on Bers’s boundary and Kra’s $$\|\Theta\|<1$$ were recognized targets; proving them is citation-grade.
2. **A dictionary that computes.** Renormalization is not only philosophy. McMullen’s books turn it into estimates that move information between quadratic-like maps and hyperbolic 3-manifolds.
3. **Centrality.** Complex dynamics, Teichmüller theory, and 3-manifold geometry were already major fields; the work showed they share compactness and rigidity mechanisms.

1998 classmates included **Borcherds**, **Gowers**, and **Kontsevich**—a reminder that one ICM can celebrate moonshine, Banach-space combinatorics, and deformation quantization alongside conformal dynamics.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “McMullen proved geometrization / Poincaré.” | Full geometrization is Perelman. McMullen contributed inside Thurston’s program (fibered hyperbolization / renormalization). |
| “Cusps dense means every Riemann surface has a cusp.” | The theorem is about *Bers’s boundary* of Teichmüller space, not about a typical smooth surface in the interior. |
| “Teichmüller space is moduli space.” | Teichmüller remembers markings; moduli quotients by the mapping class group. |
| “Julia set = Mandelbrot set.” | Julia lives in the dynamical plane of one map; Mandelbrot lives in the parameter plane of a family. |
| “Renormalization is just zooming a picture.” | It is a return-map construction with quadratic-like mappings and a rigidity theory. |
| “The medal is only Bers + Kra.” | Those are the named items; the citation also names holomorphic dynamics and 3-manifold geometrization culture. |
| “McMullen classified all rational maps.” | No. The work is rigidity, density, and renormalization, not a census of conjugacy classes. |

---

## Exercises

1. Define Fatou and Julia sets of a rational map in two sentences. Why is $$J(f)$$ usually the “interesting” set for rigidity?
2. What is a quadratic-like map (Douady–Hubbard slogan)? Why does renormalization produce one?
3. State Bers’s density-of-cusps conjecture in one careful sentence that includes the words **boundary** and **Teichmüller**.
4. Kra’s conjecture is an operator-norm inequality $$\|\Theta\|<1$$. Why might a *strict* contraction on Teichmüller space be geometrically useful?
5. Write four sentences that a classmate could use: McMullen vs Perelman on “geometrization.”
6. Read the official citation aloud. Which two conjectures are named? Which two subject headings surround them?
7. **Seminar stretch.** Compare Teichmüller space here with moduli space in the [Mirzakhani lecture]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/): what is remembered, what is forgotten, and why dynamics can live on both.

---

## Links

- IMU Fields Medal page: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- IMU Fields Medals 1998: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998)
- Wikipedia, Curtis T. McMullen: [https://en.wikipedia.org/wiki/Curtis_T._McMullen](https://en.wikipedia.org/wiki/Curtis_T._McMullen)
- McMullen’s Harvard page: [https://people.math.harvard.edu/~ctm/](https://people.math.harvard.edu/~ctm/)
- Course: [Mirzakhani / moduli]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/)
- arXiv search, McMullen dynamics: [https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all](https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all)

---

## References

1. Official Fields Medal 1998 citation for C. T. McMullen (IMU / ICM Berlin); see also Yuri Manin’s address as committee chair.
2. **S. Smale**, “The work of Curtis T. McMullen,” *Doc. Math.*, Extra Vol. ICM 1998.
3. **C. T. McMullen**, “Cusps are dense,” *Ann. of Math.* **133** (1991).
4. **C. T. McMullen**, “Amenability, Poincaré series and quasiconformal maps,” *Invent. Math.* **97** (1989) (Kra’s theta conjecture).
5. **C. T. McMullen**, *Complex Dynamics and Renormalization*, Ann. of Math. Studies **135**, Princeton, 1994.
6. **C. T. McMullen**, *Renormalization and 3-Manifolds Which Fiber over the Circle*, Ann. of Math. Studies **142**, Princeton, 1996.
7. Background: Douady–Hubbard on quadratic-like maps and the Mandelbrot set; Sullivan on Riemann surface laminations and the dictionary with Kleinian groups; Thurston on geometrization (Haken / fibered cases).
8. Course: [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/), [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/).

---

## Further directions

- Read Smale’s short ICM portrait before the 1994/1996 books.
- Compare Bers’s boundary with the boundary of the Mandelbrot set: both are conjecturally organized by laminations (Thurston; Douady–Hubbard); McMullen’s density of cusps supports one side of that analogy.
- Seminar A3: a one-page “dictionary” of three parallel words (rational map / Kleinian group; Julia set / limit set; renormalization / fibered hyperbolization)—without claiming the dictionary is an equivalence of categories.
