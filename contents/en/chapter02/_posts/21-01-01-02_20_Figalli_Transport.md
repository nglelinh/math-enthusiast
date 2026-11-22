---
layout: post
title: "Alessio Figalli: Optimal Transport and Its Applications (Fields Medal 2018)"
chapter: '02'
order: 20
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Alessio Figalli** received the **Fields Medal 2018** for contributions to the theory of optimal transport and its applications in partial differential equations, metric geometry and probability. The medal does not name a single closed-form theorem. It names a dictionary: once you know how to move one mass distribution onto another at minimal cost, you inherit a convex potential, a Monge–Ampère equation, and a way to measure how close a nearly optimal shape is to a ball or a crystal.

This essay is for learners who have seen a first calculus-of-variations problem and want the architecture of modern optimal transport (OT). It does **not** claim that Figalli invented OT, nor that Cédric Villani’s Fields Medal 2010 was “for optimal transport.” Villani’s 2010 citation is Landau damping and the Boltzmann equation; his books remain the standard OT references, but the medals are different stories. For the transport chapter of this course see [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/); for Villani’s kinetic portrait see [Villani / Landau]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau/).

---

## Learning objectives

After this lecture you should be able to:

- State the **Monge** and **Kantorovich** problems: find a map, or a coupling, that moves $$\mu$$ onto $$\nu$$ while minimizing a cost.
- Explain why, for quadratic cost, an optimal map is the gradient of a convex function and therefore solves a **Monge–Ampère** equation.
- Distinguish **full regularity** (Caffarelli-type estimates when data are nice) from **partial regularity** (singularities on a small set when convexity of the target fails).
- Describe **stability** of isoperimetric and Wulff shapes: almost-minimizers of perimeter or anisotropic surface energy are close to the ball or the Wulff crystal.
- Attribute credit carefully: Brenier, McCann, Caffarelli, Ambrosio, Villani, and De Philippis–Figalli occupy different rooms of the same house.

**Prerequisites.** Gradients of convex functions; the idea of a probability measure on $$\mathbb{R}^n$$; the classical isoperimetric inequality at slogan level. No prior Monge–Ampère theory required.

**Seminar links.** LO1 / LO4 (hard analytic programs; geometry of shapes ↔ PDE regularity). Pair with [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) for the broader dictionary, and with [Villani]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau/) only as a *different* Fields story that happens to share an author of famous OT books.

---

## 1. What the transport problem actually asks

Monge asked how to move a pile of soil $$\mu$$ onto an excavation $$\nu$$ so that the total work is minimal. In modern notation one seeks a measurable map $$T$$ with $$T_\sharp\mu=\nu$$ minimizing

$$
\int c\bigl(x,T(x)\bigr)\,d\mu(x).
$$

Kantorovich relaxed maps to **couplings**: joint measures $$\pi$$ on the product space with the correct marginals. The relaxed problem is a linear program in an infinite-dimensional space; it always has solutions under mild assumptions on the cost $$c$$. When $$c(x,y)=\lvert x-y\rvert^2$$ and the source is absolutely continuous, Brenier’s theorem says the optimizer is unique and of the form $$T=\nabla\varphi$$ for a convex potential $$\varphi$$.

Pushing $$\mu=f\,dx$$ forward to $$\nu=g\,dy$$ by $$\nabla\varphi$$ produces, at the level of densities, the Monge–Ampère equation

$$
\det D^2\varphi(x)=\frac{f(x)}{g\bigl(\nabla\varphi(x)\bigr)}
$$

on the source, with $$\nabla\varphi$$ mapping the support of $$f$$ onto the support of $$g$$. Regularity of $$T$$ becomes regularity of a fully nonlinear elliptic equation whose right-hand side and domain geometry can be unfriendly.

**Slogan.** Optimal transport is not a slogan about “moving things efficiently.” It is a machine that manufactures convex potentials and Monge–Ampère data.

---

## 2. History of the idea

Monge (1781) posed the map problem; Kantorovich (1940s) introduced couplings and duality. In the 1980s–1990s, Brenier, Rüschendorf, and McCann identified optimal maps with gradients of convex functions and extended the theory to Riemannian manifolds. Caffarelli developed an interior regularity theory for strictly convex Alexandrov solutions of Monge–Ampère when the densities are smooth and the target is convex: the potential is smooth, hence so is the map.

Villani’s monographs organized the field for a generation and connected OT to Ricci curvature and kinetic theory. Figalli’s generation inherited a theory that could state existence cleanly and prove smoothness in convex, smooth situations—and that broke as soon as the target failed to be convex, or the cost failed to be quadratic, or one asked **how close** an almost-minimizer is to the exact optimizer.

The 2018 citation recognizes work that made those “broken” regimes into theorems: Sobolev and partial regularity for Monge–Ampère and transport maps, quantitative stability of geometric inequalities, and applications in which transport is a tool rather than the object of study.

---

## 3. Regularity: from Caffarelli to De Philippis–Figalli

When the target support is not convex, Caffarelli’s global smoothness can fail: the optimal map may develop singularities. The realistic theorem is then **partial regularity**. With Guido De Philippis, Figalli proved that optimal maps (for a broad class of costs) are smooth outside a closed set of measure zero, and that Alexandrov solutions of Monge–Ampère enjoy $$W^{2,1}$$ regularity of the potential—second derivatives in $$L^1_{\mathrm{loc}}$$—which is the natural integrability once one leaves the uniformly convex, smooth world.

Those results rearrange the emotional geography of the subject. Before them, singularity of a transport map felt like a pathology one hoped not to meet. Afterward, singularities are localized: the map is as regular as the equation permits on a full-measure set, and the second derivatives are integrable enough to justify many PDE arguments that had been formal.

**Accuracy.** Caffarelli’s theory remains the smoothness engine when hypotheses hold. De Philippis–Figalli supply the theory of what happens when they do not. Neither paper “solves Monge–Ampère” in the sense of a closed-form solution.

---

## 4. Stability of balls and Wulff shapes

The classical isoperimetric inequality says that among sets of given volume, the ball minimizes perimeter. The **Wulff** problem replaces Euclidean perimeter by an anisotropic surface energy (the energy of a crystal face depending on direction); the minimizer is the Wulff shape associated with that energy.

**Stability** asks a quantitative question: if a set almost achieves the minimal energy, how close is it to the ball or the Wulff crystal? With Maggi and Pratelli, Figalli proved sharp quantitative versions of the anisotropic isoperimetric inequality by a mass-transportation argument, building on Gromov’s transport proof of the isoperimetric inequality and on the Brenier–McCann map. Later work (including crystalline norms with Zhang) pushed strong stability into settings where the Wulff shape has flat faces and the geometry is less smooth.

Quanta’s profile famously framed Figalli as a “master of soap bubbles and transport.” The soap-bubble slogan is fair as poetry—isoperimetric problems are bubble problems—but the theorems are stability estimates, not a classification of every capillary surface.

---

## 5. Transport as a tool in PDE, geometry, and probability

The citation’s second half—“applications in partial differential equations, metric geometry and probability”—is not decoration. Figalli has used transport maps and their regularity to study semigeostrophic equations, stability of functional inequalities (Sobolev, Brunn–Minkowski, Prékopa–Leindler), and problems in which an approximate coupling must be upgraded to a nearly optimal map. The pattern is portable: an inequality with a known equality case becomes a stability theorem once one controls the transport map that appears in a sharp proof.

This is why the medal is not “Figalli completed OT.” Existence and duality were already mature. The rearrangement is that **regularity and stability** became robust enough to travel into neighboring fields.

---

## 6. Why a Fields Medal

Three interlocking reasons:

1. **Difficulty.** Partial regularity for maps generated by convex potentials, and sharp stability for anisotropic isoperimetry, required a mix of geometric measure theory and fully nonlinear PDE that does not follow from citing Brenier’s theorem.
2. **Centrality.** OT had become a lingua franca. Improving its regularity and stability theories improves arguments across analysis.
3. **Clarity of slogan with depth of method.** “Almost-minimizers are close to Wulff shapes; singular maps are singular on a small set” is memorable; the proofs are not.

For this course, Figalli sits next to the [OT chapter]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) as a Fields-level refinement of a dictionary students meet as a tool, and next to [Villani]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau/) as a reminder that two medals can share a bookshelf without sharing a citation.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Villani’s Fields Medal was for optimal transport.” | Villani 2010 is Landau damping / Boltzmann; he wrote the OT books, but that is not the citation. |
| “Figalli invented optimal transport.” | Monge, Kantorovich, Brenier, Caffarelli, and many others built the theory; Figalli reshaped regularity and stability. |
| “Monge–Ampère always has smooth solutions.” | Smoothness needs hypotheses; otherwise one has partial regularity and Sobolev estimates. |
| “Stability means the ball is the unique minimizer.” | Uniqueness of the minimizer is older; stability is a quantitative closeness statement. |
| “Wulff shapes are always round.” | They are crystals of an anisotropic energy; they may have flat faces. |

---

## Exercises

1. In your own words: what does the Kantorovich relaxation **forget** and **retain** compared with Monge’s map problem?
2. Why does $$T=\nabla\varphi$$ for convex $$\varphi$$ turn a quadratic transport problem into Monge–Ampère? Write the density identity in one line.
3. Distinguish Caffarelli’s interior smoothness from De Philippis–Figalli partial regularity in four sentences.
4. State the isoperimetric inequality and its stability upgrade in parallel slogans (“minimizers are balls” versus “almost-minimizers are close to balls”).
5. **Accuracy practice.** Find a popular sentence that says Villani “won the Fields Medal for optimal transport.” Rewrite it in two precise sentences.
6. **Seminar stretch.** Skim [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) and list three uses of OT that do **not** require Figalli-level partial regularity. When would you need the regularity theory anyway?

---

## Video sources and reading

1. **IMU citation** — Fields Medals 2018: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018).
2. **Orientation** — Quanta profile: [Alessio Figalli, a Master of Soap Bubbles and Transport](https://www.quantamagazine.org/alessio-figalli-a-master-of-soap-bubbles-and-transport-20180801/).
3. **Background** — Villani, *Topics in Optimal Transportation* and *Optimal Transport: Old and New* (the books, not the 2010 medal).

**Status reminder:** Regularity and stability of transport—**not** a claim that OT began in 2018, and **not** Villani’s Fields citation.

---

## References

1. IMU Fields Medal 2018 citation — Alessio Figalli (mathunion.org).
2. **G. De Philippis and A. Figalli** — $$W^{2,1}$$ regularity for Monge–Ampère (Invent. Math., 2013); partial regularity for optimal transport maps (Publ. Math. IHÉS, 2015).
3. **A. Figalli, F. Maggi, A. Pratelli** — A mass transportation approach to quantitative isoperimetric inequalities (Invent. Math., 2010).
4. **L. Caffarelli** — regularity theory for Monge–Ampère and optimal maps (1990s).
5. Course neighbors: [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/), [Villani]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau/).

---

## Further directions

- Compare Brenier’s existence theorem with Caffarelli’s smoothness theorem: which hypotheses enter where?
- Read a survey of Wulff shapes and ask what “crystalline” changes in a stability proof.
- Seminar A3 option: one page on OT in metric-measure spaces (Lott–Villani, Sturm)—without assigning that theory to Figalli’s 2018 one-liner.
