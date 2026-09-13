---
layout: post
title: "Figalli’s Optimal Transport and Regularity (Fields Medal 2018)"
chapter: '02'
order: 20
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Alessio Figalli** received the **Fields Medal 2018**

> “for contributions to the theory of optimal transport and its applications in partial differential equations, metric geometry and probability.”
> — [IMU, Fields Medals 2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)

The citation is a program citation, not a claim that one person invented a subject. **Optimal transport (OT)** is older than Figalli: Monge posed the map problem in 1781, Kantorovich recast it as a linear program over couplings, Brenier identified quadratic-cost maps with gradients of convex potentials, Caffarelli built the first deep regularity theory for those potentials, and Ambrosio, Villani, and many others turned OT into a language for PDE, metric geometry, and probability. Figalli’s medal recognizes what he did *inside* that language: he made the regularity, stability, and free-boundary theory of transport maps sharp enough to feed geometric inequalities, atmospheric models, and quantitative analysis.

This essay is for learners who have seen the Monge–Kantorovich slogans in [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/) and want the **regularity** chapter those notes only point toward. It does **not** treat Figalli as the founder of OT, and it does **not** confuse Fields 2018 with Villani’s 2010 medal. A later kinetic portrait will live at [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Learning objectives

After this lecture you should be able to:

- Place Figalli’s 2018 citation inside a longer OT history (Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani) without collapsing that history into one name.
- State Brenier’s slogan: for quadratic cost, an optimal map is the gradient of a convex potential, and the potential solves a **Monge–Ampère** equation.
- Explain why **regularity of the map** is a PDE question, and why Caffarelli’s theory is the predecessor rather than a footnote.
- Describe, at slogan level, what interior regularity, stability, and partial regularity / free-boundary control of OT maps mean, with credit to De Philippis and other collaborators.
- Name two application zones (quantitative isoperimetric inequalities; semigeostrophic equations) and say why map regularity is the bridge.
- Distinguish **Figalli 2018 (OT + applications)** from **Villani 2010 (Landau damping / Boltzmann)**.

**Prerequisites.** The Monge and Kantorovich formulations and the idea of a push-forward $$T_\#\mu=\nu$$, as in the Chapter 6 OT lecture; convex functions and the Hessian; the slogan that a fully nonlinear elliptic equation can have a regularity theory. No prior Monge–Ampère course is assumed.

**Seminar links.** Pair with [Caffarelli / free boundaries and Monge–Ampère]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/) for the Abel-level regularity culture that Figalli inherits, and with [Deng PDE]({{ site.baseurl }}/contents/en/chapter02/02_12_Deng_PDE/) only as a *different* PDE Fields story (kinetic limits, not transport maps).

---

## 1. A subject Figalli did not invent

The opening pedagogical duty is negative and useful. If you remember only one sentence from a popular profile, make it this: **Figalli did not invent optimal transport.**

Monge asked how to move a pile of earth to a prescribed target at minimal cost, insisting on a **map** $$T$$. Kantorovich allowed mass to split, replacing maps by **couplings** $$\pi$$ with fixed marginals, and unlocked convex duality. In the 1980s–1990s, Brenier proved that for cost $$c(x,y)=\|x-y\|^2$$ (under standard moment hypotheses), an optimal map exists and has the form

$$
T=\nabla\phi,
$$

where $$\phi$$ is convex. McCann, Gangbo, and others extended the convex-potential picture to Riemannian and more general cost geometries. Caffarelli then asked the analyst’s question: if the densities are nice, how nice is $$\phi$$? Ambrosio developed OT as a tool for gradient flows and BV theory; Villani wrote the books that made the subject a common language and used it for geometric inequalities and Ricci-type curvature—while his **Fields Medal 2010** citation is about kinetic equations, not about founding OT.

Figalli studied with **Luigi Ambrosio** (Pisa) and **Cédric Villani** (ENS Lyon), finished his doctorate in 2007, and has been at ETH Zürich since 2016. The medal is a regularity-and-applications award inside a mature field.

---

## 2. From Brenier maps to Monge–Ampère

Suppose $$\mu=f\,dx$$ and $$\nu=g\,dy$$ are absolutely continuous probabilities on (regions of) $$\mathbb{R}^n$$, and $$T=\nabla\phi$$ pushes $$\mu$$ onto $$\nu$$. A formal change of variables gives the Jacobian identity

$$
f(x)=g\bigl(\nabla\phi(x)\bigr)\,\det D^2\phi(x).
$$

That is a **Monge–Ampère** equation for the convex potential $$\phi$$. The equation is fully nonlinear: the unknown appears inside a determinant of second derivatives. Weak notions of solution (Alexandrov solutions, viscosity solutions) exist long before one knows whether $$\phi$$ is $$C^2$$.

Why regularity matters. If $$\phi$$ is merely convex, $$T=\nabla\phi$$ is defined almost everywhere but may jump, fold, or fail to be differentiable on a large set. Geometric applications want more: they want the map to be a diffeomorphism on large open sets, or they want quantitative control on how much it can deviate from a model map (a translation, a linear isometry, the identity). In atmospheric models, the same map is a change of coordinates; if it is too rough, the PDE in physical space does not even make distributional sense.

So the OT regularity program is not aesthetic polish. It is the difference between “a map exists a.e.” and “the map is a usable change of variables.”

---

## 3. Caffarelli’s regularity theory as predecessor

The first deep regularity theory for quadratic-cost OT maps is **Caffarelli’s**. In the early 1990s he showed that Alexandrov solutions of Monge–Ampère enjoy interior $$C^{1,\alpha}$$ and, under convexity of the target and smoothness of the densities, higher—ultimately $$C^\infty$$—interior regularity. Boundary regularity needs still more geometry.

The Abel Prize 2023 citation for Caffarelli names this culture: regularity for nonlinear PDE, free boundaries, and Monge–Ampère. Figalli sits downstream. A fair seminar sentence is:

> Caffarelli showed that, in the convex, quadratic, Euclidean setting, optimal maps can be as regular as the densities; Figalli and collaborators asked what survives when convexity, the cost, or the ambient geometry is no longer that kind.

The Ma–Trudinger–Wang condition later isolated a structural hypothesis on a general cost that restores full smoothness. When it fails, or when supports are not convex, one no longer expects a globally smooth map. The modern question becomes **partial regularity**: is the singular set small?

---

## 4. Interior regularity, stability, and free boundaries of maps

Figalli’s OT analysis—often jointly with **Guido De Philippis**, and in other papers with Kim, Loeper, and others—has three interlocking slogans.

**Higher integrability and Sobolev regularity.** Convex Alexandrov solutions need not a priori have $$D^2\phi$$ in $$L^1_{\mathrm{loc}}$$. De Philippis–Figalli proved $$W^{2,1}$$ regularity for Monge–Ampère (Inventiones, 2013), a threshold that sounds technical until one remembers that $$W^{2,1}$$ is what lets one differentiate the map in an $$L^1$$ sense and pass to the limit in nonlinear expressions. Follow-up work gave second-order stability: if densities converge, the maps converge strongly in Sobolev norms, not merely weakly.

**Partial regularity.** In *Partial regularity for optimal transport maps* (Publ. Math. IHÉS, 2015), De Philippis–Figalli proved that for general costs on $$\mathbb{R}^n$$, or for $$c=d^2/2$$ on a Riemannian manifold, optimal maps between smooth densities are smooth **outside a closed singular set of measure zero**. The result does not need MTW and does not need convex supports. It is a free-boundary / singular-set theorem in spirit: the map is a diffeomorphism on a large open set, and the bad set is closed and null. Earlier two-dimensional $$C^1$$ results (Figalli–Loeper) and partial regularity for Brenier solutions (Figalli–Kim) belong to the same cluster.

**Stability of inequalities.** Regularity and stability travel together. If a map is close to a model map, geometric functionals (perimeter, Sobolev constants, entropy production) should be close to their optima, with an explicit deficit. That is the bridge from PDE estimates to quantitative geometry.

Later free-boundary work on the obstacle and Stefan problems (Figalli–Serra, Figalli–Ros-Oton–Serra) is neighboring analysis, not the 2018 citation’s third bullet. The medal text is OT and its applications.

---

## 5. Applications: inequalities, atmosphere, probability

**Quantitative isoperimetric inequalities.** Figalli–Maggi–Pratelli (Inventiones, 2010) used mass transport to prove a sharp quantitative form of the **anisotropic** isoperimetric inequality: if a set almost minimizes anisotropic perimeter, it is close (in a precise distance) to a translate of the Wulff shape. The method is OT-theoretic: a transport map from the set to a model body converts a deficit in perimeter into a deficit in the map, which regularity/stability then turns into geometric closeness. This is the “metric geometry” clause of the IMU sentence made concrete.

**Semigeostrophic equations.** The semigeostrophic (SG) system is a frontogenesis model in atmospheric science. After a change to geostrophic coordinates, the pressure potential is convex and its gradient is an optimal transport map between the fluid density and a reference measure. Benamou–Brenier and Cullen made that dictionary standard; Ambrosio–Colombo–De Philippis–Figalli then used the new Sobolev estimates for Monge–Ampère to obtain global weak Eulerian solutions on the two-dimensional torus and, under convexity assumptions, in three-dimensional convex domains. Here OT regularity is not a corollary. It is the reason the physical-space velocity is a well-defined distribution.

**Functional inequalities and probability.** With Carlen, Figalli proved stability for Gagliardo–Nirenberg and log-HLS inequalities (with a Keller–Segel application). With Guionnet he used approximate transport maps for universality in several-matrix models. That is the citation’s “probability” clause: transport as a comparison of measures, not only as a map between piles of sand.

---

## 6. Two Fields medals, two kinetic cultures

Because Figalli was Villani’s student, it is easy to smear the two medals together. They are not the same prize.

| Medal | Citation focus | Shared vocabulary | Distinct claim |
|-------|----------------|-------------------|----------------|
| Villani, 2010 | Nonlinear Landau damping; convergence to equilibrium for Boltzmann | Entropy, inequalities, OT as a toolkit Villani also developed | Kinetic relaxation theorems |
| Figalli, 2018 | OT theory and applications to PDE, metric geometry, probability | Monge–Ampère, maps, stability | Regularity/stability of transport and geometric consequences |

Villani’s IMU 2010 text does mention that he pioneered applications of OT to inequalities and wrote a book on mass transport; that is background, not the medal sentence. Figalli’s 2018 sentence *is* the OT sentence. A future lecture, [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/), will keep the kinetic theorems in their own file.

---

## 7. Why a Fields Medal

Three reasons, none of which require calling OT “Figalli’s theory.”

1. **Difficulty.** Partial regularity and Sobolev thresholds for fully nonlinear equations sit at the edge of what convex analysis and Calderón–Zygmund theory can see; the proofs mix Alexandrov maximum principles, affine invariance, and geometric measure theory.
2. **Export.** Once maps are $$W^{2,1}$$ or smooth off a null set, other fields can use them: Wulff shapes, SG fronts, matrix models, Keller–Segel.
3. **Clarity of the remaining map.** After Caffarelli, one knew the convex Euclidean story. After Figalli–De Philippis and the surrounding school, one knows what a theorem looks like when the cost is general, the domain is a manifold, or the application only needs a Sobolev map.

For this course, Figalli is **regularity as infrastructure**: not one named conjecture closed, but a toolkit made strong enough that other theorems become legal.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Figalli invented optimal transport.” | Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani, and others built the subject; Figalli’s medal is regularity plus applications. |
| “Fields 2018 is the same as Villani 2010.” | Villani 2010 is Landau damping and Boltzmann; Figalli 2018 is OT and its uses. |
| “Brenier maps are always smooth.” | Convex potentials give maps a.e.; smoothness needs density, convexity, cost, and often only holds off a singular set. |
| “Caffarelli’s theory is obsolete.” | It is the foundation; later work asks what remains without its geometric hypotheses. |
| “Partial regularity means the map is $$C^\infty$$ everywhere.” | It means smooth off a closed null set; the singular set can be nonempty. |
| “OT regularity is only aesthetic.” | SG well-posedness and quantitative isoperimetry use the estimates as hypotheses, not as decoration. |

---

## Exercises

1. In two sentences, what does Brenier’s theorem add to Kantorovich’s existence theory for quadratic cost?
2. Write the formal Monge–Ampère equation relating densities $$f,g$$ to a convex potential $$\phi$$. Which term is nonlinear, and why does that obstruct naive elliptic regularity?
3. Why does **convexity of the target** appear in Caffarelli’s full-regularity theorems? Give a slogan, not a proof.
4. State the De Philippis–Figalli partial-regularity slogan (smooth off a closed null set). What hypotheses does it *drop* relative to Caffarelli’s classical setting?
5. Explain, in at most eight sentences, how an optimal map enters the semigeostrophic dictionary. Why would $$W^{2,1}$$ regularity of the potential matter for a weak Eulerian formulation?
6. **Accuracy practice.** Find a sentence that says Figalli “created optimal transport.” Rewrite it in two precise sentences suitable for this course.
7. Compare Figalli 2018 with Villani 2010 in a four-row table of your own: citation, equations, role of OT, what not to claim.
8. **Seminar stretch.** Skim the introduction of De Philippis–Figalli, *The Monge–Ampère equation and its link to optimal transportation* (Bull. AMS, 2014), and list five keywords to learn next (e.g. Alexandrov solution, MTW, c-convexity, Wulff shape, Cullen–Purser coordinates).

---

## Links

- IMU Fields Medals 2018: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)
- Wikipedia — Alessio Figalli: [https://en.wikipedia.org/wiki/Alessio_Figalli](https://en.wikipedia.org/wiki/Alessio_Figalli)
- ETH page (regularity of maps): [https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps](https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps)
- Quanta profile (2018): [https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/](https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/)
- arXiv search — Figalli Monge–Ampère: [https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all](https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all)
- De Philippis–Figalli $$W^{2,1}$$ (arXiv:1111.7207): [https://arxiv.org/abs/1111.7207](https://arxiv.org/abs/1111.7207)
- De Philippis–Figalli partial regularity (arXiv:1209.5640): [https://arxiv.org/abs/1209.5640](https://arxiv.org/abs/1209.5640)

---

## References

1. IMU Fields Medal 2018 citation — Alessio Figalli.
2. Y. Brenier, “Polar factorization and monotone rearrangement of vector-valued functions,” *Comm. Pure Appl. Math.* 44 (1991).
3. L. A. Caffarelli, papers on regularity of Monge–Ampère and OT maps (early 1990s); Abel 2023 citation.
4. G. De Philippis and A. Figalli, “$$W^{2,1}$$ regularity for solutions of the Monge–Ampère equation,” *Invent. Math.* 192 (2013); “Partial regularity for optimal transport maps,” *Publ. Math. IHÉS* 121 (2015); survey in *Bull. Amer. Math. Soc.* 51 (2014).
5. A. Figalli, F. Maggi, and A. Pratelli, “A mass transportation approach to quantitative isoperimetric inequalities,” *Invent. Math.* 182 (2010).
6. L. Ambrosio, M. Colombo, G. De Philippis, and A. Figalli, Eulerian well-posedness results for the semigeostrophic equations (2D periodic and 3D convex settings).
7. A. Figalli, *The Monge–Ampère Equation and Its Applications*, EMS (2017).
8. C. Villani, *Topics in Optimal Transportation*; *Optimal Transport: Old and New* — background language, not the 2010 Fields citation.
9. Course: [Optimal Transport]({{ site.baseurl }}/contents/en/chapter06/06_09_Optimal_Transport/), [Caffarelli]({{ site.baseurl }}/contents/en/chapter08/08_08_Caffarelli_PDE/), future [Villani]({{ site.baseurl }}/contents/en/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Further directions

- Read Caffarelli’s interior estimates next to De Philippis–Figalli partial regularity: which geometric hypotheses moved from “assumed” to “unnecessary for a.e. smoothness”?
- Compare computational OT (Sinkhorn, Chapter 6) with the analytic theory: numerics regularize; regularity theory explains when the unregularized map was already almost smooth.
