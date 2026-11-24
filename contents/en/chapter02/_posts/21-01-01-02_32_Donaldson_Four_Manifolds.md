---
layout: post
title: "Donaldson’s Four-Manifolds and Exotic Smooth Structures (Fields Medal 1986)"
chapter: '02'
order: 32
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Ask a seemingly innocent question from multivariable calculus: *how many genuinely different ways are there to do calculus on Euclidean space $$\mathbb{R}^n$$?* For $$n = 1, 2, 3$$, the answer is **exactly one**. For $$n = 5, 6, 7, \ldots, 100$$, the answer is still **exactly one**! Yet in the spring of 1982, a 24-year-old graduate student at Oxford named **Simon Donaldson**—wielding the **Yang–Mills equations** of particle physics—stunned the mathematical world by unleashing a collision that proved **Euclidean four-space $$\mathbb{R}^4$$ alone admits infinitely many (in fact, uncountably many!) "exotic smooth structures"**: spaces completely indistinguishable from $$\mathbb{R}^4$$ as continuous topological shapes, yet *impossible* to transform smoothly into standard $$\mathbb{R}^4$$.

At the 1986 ICM in Berkeley, **Simon Donaldson** received the **Fields Medal**, in the standard IMU account:

> primarily for his work on the topology of four-manifolds, especially for showing that there is a differential structure on Euclidean four-space which is different from the usual structure.  
> — [IMU, Fields Medals 1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)

To understand why 1986 was such a seismic event, place **three pieces** side by side: (1) **Michael Freedman’s** 1982 topological classification of simply connected four-manifolds (for which Freedman shared the 1986 Berkeley Fields stage, including the topological 4D Poincaré conjecture); (2) **Karen Uhlenbeck’s** analytic foundation of compactness, bubbling, and removable singularities for Yang–Mills fields (see [Uhlenbeck / gauge theory]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/)); and (3) **Donaldson’s** 1983 gauge-theoretic theorem placing a shocking iron vise on **smooth** intersection forms. It is the **head-on clash** between Freedman’s topological abundance and Donaldson’s smooth rigidity that spawns non-smoothable four-manifolds and exotic $$\mathbb{R}^4$$s. **Seiberg–Witten theory** (Witten, 1994) is a powerful later descendant (see the surrounding culture in [Mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/)), and the full classification of smooth four-manifolds remains open today.

**Lesson roadmap:** Background Knowledge Map (topological vs. smooth in dimension 4, intersection forms $$Q_X$$, anti-self-dual Yang–Mills) → Hand-verifiable matrix examples: $$\mathbb{CP}^2$$, $$S^2 \times S^2$$, and the $$8 \times 8$$ Cartan matrix of $$E_8$$ → The Freedman (1982) vs. Donaldson (1983) clash → Deep-Dive Explanation (Read Slowly): 4 steps using a 5D instanton moduli space to force $$Q_X$$ to diagonalize → Seiberg–Witten (1994) and later descendants.

---

## Learning objectives

After this lecture you should be able to:

- Explain why **dimension four** is the most anomalous dimension in topology: the Whitney trick fails smoothly because $$2 + 2 = 4$$, yet can be rescued topologically via Casson handles.
- Write out the **intersection form** $$Q_X$$ for $$\mathbb{CP}^2$$, $$S^2 \times S^2$$, and the $$E_8$$ lattice, and verify by hand why $$E_8$$ is positive definite, unimodular, and *not* diagonalizable over $$\mathbb{Z}$$.
- State **Donaldson’s theorem (1983)** (a definite intersection form of a closed, oriented, smooth four-manifold must be diagonalizable over $$\mathbb{Z}$$) alongside **Freedman’s theorem (1982)** (every unimodular form is realized by a simply connected topological four-manifold).
- Explain how the **Freedman + Donaldson** clash produces both (i) topological four-manifolds with **no smooth structure** and (ii) **exotic $$\mathbb{R}^4$$s**.
- Describe how **instanton moduli spaces** ($$F_A^+ = 0$$) and **Uhlenbeck compactness** (bubbling creating a boundary) turn gauge-theory PDEs into a 5D cobordism.
- Distinguish **Seiberg–Witten theory (1994)** from the 1986 medal and avoid claiming that Donaldson classified all four-manifolds.

**Prerequisites.** Smooth manifolds, homology, and cup product at the level of a first algebraic topology course; the idea of a vector bundle and a connection. No prior gauge theory is assumed: treat a connection as a way to differentiate sections, and curvature as the failure of mixed partials to commute.

**Seminar links.** Physics-inspired PDE as a topological machine; topological versus smooth categories. Pair with [Uhlenbeck]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/), [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) for a later geometric-analytic attack on three-manifolds, and [mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/).

---

## Background Knowledge Map: Four-Manifolds, Intersection Forms, and Gauge Theory

### 1. Topological vs. smooth—and why dimension 4 stands alone
A **topological manifold** only requires continuous coordinates (homeomorphism—stretching clay with creases allowed); a **smooth manifold** requires compatible differentiable coordinates everywhere (diffeomorphism).
- For $$n \ge 5$$, the **Whitney trick** has enough ambient room to slide away pairs of opposite-sign intersections, powering Smale’s $$h$$-cobordism and surgery classification machines.
- For $$n \le 3$$, classical cut-and-paste and Thurston–Perelman geometrization control everything cleanly.
- In **dimension $$n = 4$$**, two 2-dimensional disks generically intersect in isolated points ($$2 + 2 = 4$$), so sliding a disk to cancel old intersections creates brand-new ones! Topologically, you can push those intersections off to infinity into an infinite tower called a **Casson handle** (homeomorphic to a standard handle); smoothly, that tower refuses to straighten out.

### 2. The intersection form $$Q_X$$—a four-manifold’s integer fingerprint
Inside a closed, oriented four-manifold $$X$$, two generic 2-dimensional surfaces meet in finitely many signed points. Counting those signed intersections on $$H_2(X;\mathbb{Z})/\mathrm{torsion}$$ (equivalently, taking cup products on $$H^2$$) produces a symmetric integer matrix of determinant $$\pm 1$$ (unimodular, by Poincaré duality):

$$
Q_X : H_2(X;\mathbb{Z})/\mathrm{torsion} \times H_2(X;\mathbb{Z})/\mathrm{torsion} \to \mathbb{Z}.
$$

### 3. Anti-self-dual (ASD) Yang–Mills equations and instantons
On a smooth four-manifold $$X$$ carrying a principal $$\mathrm{SU}(2)$$ bundle, the Hodge star operator $$\star$$ maps 2-forms to 2-forms with $$\star^2 = 1$$—a symmetry **exclusive to dimension 4**. This splits the curvature $$F_A$$ of any connection $$A$$ into self-dual and anti-self-dual parts, $$F_A = F_A^+ + F_A^-$$. Connections minimizing the Yang–Mills energy $$\mathrm{YM}(A) = \int_X \lvert F_A\rvert^2$$ satisfy the first-order PDE **$$F_A^+ = 0$$** and are called **instantons**.

---

## 1. Worked Matrix Examples by Hand: $$\mathbb{CP}^2$$, $$S^2 \times S^2$$, and the $$E_8$$ Lattice

Write down the intersection matrices of three concrete spaces to see Donaldson’s shock with your own eyes:

1. **The complex projective plane $$\mathbb{CP}^2$$ (real dimension 4):** $$H_2(\mathbb{CP}^2; \mathbb{Z}) \cong \mathbb{Z}$$, generated by a complex line $$\mathbb{CP}^1$$. Any two distinct complex lines intersect transversely in exactly $$1$$ positive point, so:
   $$
   Q_{\mathbb{CP}^2} = \begin{pmatrix} 1 \end{pmatrix}.
   $$
   This form is **positive definite**, **odd**, and **already diagonal**.

2. **The product of two spheres $$S^2 \times S^2$$:** $$H_2(S^2 \times S^2; \mathbb{Z}) \cong \mathbb{Z}^2$$, generated by $$A = S^2 \times \{p\}$$ and $$B = \{q\} \times S^2$$. Pushing $$A$$ slightly off itself gives $$A \cdot A = 0$$; likewise $$B \cdot B = 0$$; and $$A$$ meets $$B$$ at the single point $$(q, p)$$, so $$A \cdot B = 1$$:
   $$
   Q_{S^2 \times S^2} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
   $$
   This form is **even** but **indefinite** (eigenvalues $$+1$$ and $$-1$$).

3. **The $$8 \times 8$$ Cartan matrix of $$E_8$$:** From algebra and sphere packing comes the celebrated $$E_8$$ matrix:
   $$
   E_8 = \begin{pmatrix}
   2 & -1 & 0 & 0 & 0 & 0 & 0 & 0 \\
   -1 & 2 & -1 & 0 & 0 & 0 & 0 & 0 \\
   0 & -1 & 2 & -1 & 0 & 0 & 0 & 0 \\
   0 & 0 & -1 & 2 & -1 & 0 & 0 & 0 \\
   0 & 0 & 0 & -1 & 2 & -1 & 0 & -1 \\
   0 & 0 & 0 & 0 & -1 & 2 & -1 & 0 \\
   0 & 0 & 0 & 0 & 0 & -1 & 2 & 0 \\
   0 & 0 & 0 & 0 & -1 & 0 & 0 & 2
   \end{pmatrix}.
   $$
   Verify three striking facts directly from this matrix:
   - Every diagonal entry is **$$2$$** (even), so for *every* integer vector $$v \in \mathbb{Z}^8$$, the quadratic value $$v^T E_8 v$$ is **even**—it can **never equal $$1$$**!
   - Its determinant is $$\det(E_8) = 1$$ (unimodular), and all leading principal minors are positive (**positive definite**).
   - Because no integer vector has $$v^T E_8 v = 1$$, the matrix $$E_8$$ **cannot be diagonalized over $$\mathbb{Z}$$** to the identity matrix $$I_8$$!

Now hold the two 1982–1983 theorems right next to $$E_8$$:
- **Freedman (1982, *J. Differential Geom.* 17):** *Every* unimodular symmetric bilinear form is realized by a closed, simply connected **topological** four-manifold (uniquely in the even case; with two homeomorphism types distinguished by the Kirby–Siebenmann bit in $$\mathbb{Z}/2$$ in the odd case, implying the **topological 4D Poincaré conjecture**). $$\implies$$ **There exists a topological four-manifold $$M_{E_8}$$ with intersection form $$E_8$$!**
- **Donaldson (1983, *J. Differential Geom.* 18):** If $$X$$ is a closed, oriented, **smooth** four-manifold (originally simply connected; later extended) whose intersection form is definite, then $$Q_X$$ **must be diagonalizable over $$\mathbb{Z}$$** (equivalent to $$\pm I_n$$). $$\implies$$ **$$M_{E_8}$$ admits NO smooth structure whatsoever!**

When you stage that exact same clash at the open ends of a smooth K3 surface (whose intersection form is $$2(-E_8) \oplus 3H$$) using Freedman’s topological capping, you produce an open four-manifold **homeomorphic to $$\mathbb{R}^4$$** that contains a compact set impossible to enclose inside any smoothly embedded $$S^3$$—an **exotic $$\mathbb{R}^4$$**! (In the very same 1983 journal volume, Robert Gompf constructed three explicit exotic $$\mathbb{R}^4$$s; Gompf and Taubes later proved there are **uncountably many** mutually nondiffeomorphic smooth structures on $$\mathbb{R}^4$$.)

---

## 2. Deep-Dive Explanation: How Do the Yang–Mills Equations Force $$Q_X$$ to Diagonalize? (Read Slowly)

Why should a particle-physics PDE ($$F_A^+ = 0$$) know anything about an integer matrix on $$H_2(X;\mathbb{Z})$$? Follow the four extraordinary steps of Donaldson’s 1983 proof:

#### Step 1: Build the instanton moduli space $$\mathcal{M}$$ — a 5-dimensional manifold
Take a closed, oriented, smooth, simply connected four-manifold $$X$$ with positive-definite intersection form $$Q_X$$. On the principal $$\mathrm{SU}(2)$$ bundle of instanton number $$k = 1$$, form the **moduli space** $$\mathcal{M}$$ of all solutions to $$F_A^+ = 0$$ modulo gauge transformations. By the Atiyah–Singer index theorem, $$\mathcal{M}$$ is a **5-dimensional manifold**, smooth almost everywhere.

#### Step 2: Count the singular points inside $$\mathcal{M}$$ — the footprint of $$Q_X$$
The only points where $$\mathcal{M}$$ fails to be smooth are the **reducible connections** (whose symmetry reduces from $$\mathrm{SU}(2)$$ to $$\mathrm{U}(1)$$). Remarkably, these singular points stand in **one-to-one correspondence** with pairs $$\pm \alpha \in H_2(X;\mathbb{Z})$$ satisfying $$\alpha \cdot \alpha = 1$$! Even better, a small neighborhood of each singular point inside the 5D space $$\mathcal{M}$$ looks exactly like a **cone over $$\mathbb{CP}^2$$**.

#### Step 3: Uhlenbeck "bubbling" creates a boundary equal to $$X$$ itself
The 5-manifold $$\mathcal{M}$$ is noncompact because an instanton can concentrate all its curvature energy at a **single point** $$x \in X$$ as its scale shrinks to $$0$$ (**bubbling**—just as the instanton moduli space on $$S^4$$ is a 5-ball whose boundary at infinity is $$S^4$$ itself). Using **Karen Uhlenbeck’s compactness and removable-singularities theorems** (see [Uhlenbeck]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/)), Donaldson proved that point-bubbling is the *only* degeneration: compactifying $$\mathcal{M}$$ by adding these point-instantons glues an exact, intact copy of **$$X$$** onto $$\mathcal{M}$$ as its outer boundary!

#### Step 4: Chop off the cone tips $$\implies$$ a 5D cobordism locking down $$Q_X$$
Excise a tiny cone neighborhood around each of the $$m$$ singular points (exposing $$m$$ boundary copies of $$\pm\mathbb{CP}^2$$). The compactified 5-manifold $$\overline{\mathcal{M}}$$ now forms a **5-dimensional cobordism** linking $$X$$ to the disjoint union of $$m$$ copies of $$\pm\mathbb{CP}^2$$!
Because signature is a cobordism invariant and $$Q_X$$ is positive definite (so its signature equals its rank $$b_2$$), we immediately get $$m \ge b_2$$—meaning there are at least $$b_2$$ classes with self-intersection $$\alpha_i \cdot \alpha_i = 1$$! A quick linear-algebra check then forces $$Q_X$$ to be **completely diagonalizable over $$\mathbb{Z}$$** to $$I_{b_2}$$!

Summary of Donaldson’s breakthrough chain:

$$
\text{Smooth 4-manifold } X
\;\xrightarrow{F_A^+ = 0}\;
\text{5D moduli } \mathcal{M}
\;\xrightarrow{\text{Uhlenbeck bubbling}}\;
\text{Cobordism: } X \sim \bigsqcup \pm\mathbb{CP}^2
\;\Longrightarrow\;
Q_X \cong I_{b_2}.
$$

*(Freed–Uhlenbeck’s 1984 book *Instantons and Four-Manifolds* became the first-generation text. Later, Donaldson’s 1990 polynomial invariants used higher-charge moduli spaces to distinguish infinitely many smooth structures on a single closed topological four-manifold—a continuation, still not a full classification.)*

---

## 3. Descendants That Are Not the 1986 Medal

- **Seiberg–Witten theory (1994):** Eight years later, **Edward Witten** introduced the Seiberg–Witten monopole equations from $$N=2$$ supersymmetric gauge theory (using abelian $$\mathrm{U}(1)$$ instead of $$\mathrm{SU}(2)$$). Their moduli spaces are automatically compact (no bubbling!), yielding shorter proofs of Donaldson’s theorem and many new constraints. Mention them as the 1994 descendant, not the 1986 medal.
- **Donaldson’s later chapters:** The Donaldson–Uhlenbeck–Yau theorem on Hermitian–Einstein metrics, symplectic Lefschetz pencils, and the Chen–Donaldson–Sun proof of the Yau–Tian–Donaldson conjecture for Kähler–Einstein metrics on Fano manifolds.

**Why the Fields Medal 1986:** Everyone expected dimension four to be hard; almost no one imagined that Yang–Mills analysis from physics would prove "definite implies diagonalizable" and, colliding with Freedman’s topological freedom, shatter the unity of topology and calculus in four dimensions. The 1986 Berkeley class was **Donaldson**, **Faltings** (Mordell), and **Freedman**—arithmetic geometry, topological four-manifolds, and smooth four-manifolds via gauge theory.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Donaldson classified all four-manifolds.” | He proved foundational constraints and later invariants. Classification remains open in the smooth category. |
| “Donaldson alone constructed exotic $$\mathbb{R}^4$$.” | Existence uses **Donaldson’s smooth constraints** together with **Freedman’s topological theory** (and early constructions of Gompf and others). |
| “Freedman’s Poincaré conjecture is the smooth one.” | Freedman proved the **topological** 4D Poincaré conjecture. The smooth 4D Poincaré conjecture remains open. |
| “Seiberg–Witten is the 1986 medal.” | Seiberg–Witten invariants appear in **1994**. |
| “Uhlenbeck compactness is a topological theorem.” | It is an **analytic** compactness/removable-singularities theorem that topology then uses. |
| “Exotic $$\mathbb{R}^4$$ contradicts the uniqueness of $$\mathbb{R}^n$$ for $$n\neq 4$$.” | For $$n\neq 4$$, Euclidean space has a unique smooth structure; dimension four is the exception. |

---

## Links

- IMU Fields Medals 1986: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1986)
- Wikipedia: [Simon Donaldson](https://en.wikipedia.org/wiki/Simon_Donaldson); [Exotic $$\mathbb{R}^4$$](https://en.wikipedia.org/wiki/Exotic_R4); [Donaldson’s theorem](https://en.wikipedia.org/wiki/Donaldson%27s_theorem)
- Course: [Uhlenbeck / gauge]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/), [Mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/), [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/)
- arXiv search (later Donaldson work; the 1983 papers predate arXiv): [Donaldson four-manifold](https://arxiv.org/search/?query=Donaldson+four-manifold+instanton&searchtype=all)

---

## References

1. International Mathematical Union, Fields Medals 1986 account of Simon K. Donaldson (Albers–Alexanderson–Reid / IMU page).
2. **S. K. Donaldson**, “An application of gauge theory to four-dimensional topology,” *J. Differential Geom.* 18 (1983), 279–315.
3. **M. H. Freedman**, “The topology of four-dimensional manifolds,” *J. Differential Geom.* 17 (1982), 357–453.
4. **R. Gompf**, “Three exotic $$\mathbf{R}^4$$’s and other anomalies,” *J. Differential Geom.* 18 (1983), 317–328.
5. **S. K. Donaldson and P. B. Kronheimer**, *The Geometry of Four-Manifolds*, Oxford, 1990.
6. **D. S. Freed and K. K. Uhlenbeck**, *Instantons and Four-Manifolds*, Springer, 1984; course essay [Uhlenbeck]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/).
7. **E. Witten**, “Monopoles and four-manifolds,” *Math. Res. Lett.* 1 (1994), 769–796. (Descendant, not the 1986 medal.)
8. Wikipedia, [Simon Donaldson](https://en.wikipedia.org/wiki/Simon_Donaldson), [Exotic R4](https://en.wikipedia.org/wiki/Exotic_R4).

---

## Further directions

- Read Atiyah’s ICM 1986 laudation, then Donaldson–Kronheimer Chapter 1; after the Uhlenbeck essay, note why bubbling is a feature (it produces $$\partial\mathcal{M}$$).
- Seminar prompt: what would a classification of smooth simply connected four-manifolds still need beyond intersection forms?

## Video tham khảo

- **xem trước** — [Simon Donaldson, Invariants of manifolds and the classification problem](https://www.youtube.com/watch?v=IO0HNEs8oxQ) — Clay Mathematics Institute, English. Watch first. “Simon Donaldson, Invariants of manifolds and the classification problem” orients the lesson’s aim: Explain why dimension four is special: Whitney trick and high-dimensional surgery fail, while low-dimensional cut-and-paste is not enough.
- [The Shaw Prize Lecture in Mathematical Sciences 2009 - by Professor Simon K Donaldson](https://www.youtube.com/watch?v=5yhxUCtNRQE) — The Shaw Prize, English. A second pass once the main claim is in view: Explain why dimension four is special: Whitney trick and high-dimensional surgery fail, while low-dimensional cut-and-paste is not enough.
- [Overview of gauge theory and submanifold geometry on G_2 manifolds - Simon Donaldson (2014)](https://www.youtube.com/watch?v=xIqLhsrgcBI) — Graduate Mathematics, English. Further depth after the first two, still tied to this lesson: Explain why dimension four is special: Whitney trick and high-dimensional surgery fail, while low-dimensional cut-and-paste is not enough.
