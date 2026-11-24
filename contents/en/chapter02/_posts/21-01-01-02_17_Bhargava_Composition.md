---
layout: post
title: "Bhargava’s Composition Laws and Average Ranks (Fields Medal 2014)"
chapter: '02'
order: 17
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

One evening in 1998, a young Princeton graduate student named **Manjul Bhargava** sat in his dorm room fiddling with a miniature **$$2\times 2\times 2$$ Rubik’s cube**—imagining an integer written on each of its eight corners. When he sliced the cube in three different directions (front/back, left/right, top/bottom) and took simple $$2\times 2$$ determinants, three quadratic polynomials popped out—and miraculously, they obeyed **Carl Friedrich Gauss’s legendary 1801 composition law**!

In that playful flash of insight, a 200-year-old algebraic thicket of twenty pages of formulas collapsed into a single 3D box of eight numbers. Even better, that cube was only the first of **fourteen new "higher composition laws"** Bhargava uncovered—turning abstract number rings of degrees $$2, 3, 4, 5$$ into concrete integer lattice points you can literally count by computing volumes!

When Bhargava and **Arul Shankar** aimed that same counting engine at **elliptic curves**, they cracked a half-century mystery: proving that the **average rank** of elliptic curves over $$\mathbb{Q}$$ is **finite and bounded** (and that a positive proportion have rank $$0$$). For these breakthroughs, **Manjul Bhargava**—also an accomplished tabla player and the first person of Indian origin to win the prize—received the **Fields Medal in 2014**.

This essay walks you by hand through an actual **Bhargava $$2\times 2\times 2$$ cube** (discriminant $$-23$$), contrasts rank-0 and rank-1 elliptic curves, and explains how counting **Selmer groups** bounds average ranks—while keeping a crystal-clear boundary between Bhargava–Shankar’s theorems and the still-open [Birch–Swinnerton-Dyer (BSD) conjecture]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/).

---

## Learning objectives

After this lecture you should be able to:

- Compute by hand the three binary quadratic forms produced by a **$$2\times 2\times 2$$ Bhargava cube** (discriminant $$-23$$) and verify directly that they compose to the identity.
- Explain what **higher composition laws** do: parametrize rings of small rank (degrees $$2,3,4,5$$) by integer orbits so the **geometry of numbers** can count them asymptotically.
- Compare a concrete rank-0 elliptic curve ($$y^2 = x^3 - x$$) with a rank-1 curve ($$y^2 = x^3 - 2$$ with point $$(3,5)$$) to understand Mordell–Weil rank.
- Follow how **Bhargava–Shankar’s** theorem that the average 2-Selmer size is $$3$$ implies $$\mathbb{E}[r_E] \le 1.5$$ (and $$< 0.885$$ via 5-Selmer).
- Distinguish Bhargava–Shankar’s proved average-rank bounds from the unproven **$$1/2$$ heuristic** and the still-open **BSD conjecture**.

**Prerequisites.** Basic $$2\times 2$$ determinants, quadratic polynomials $$ax^2+bxy+cy^2$$ with discriminant $$b^2-4ac$$, and the basic notion of rational points on an elliptic curve.

**Related lessons.** Arithmetic twin: [BSD conjecture]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/). Nearby portraits: [Tsimerman]({{ site.baseurl }}/contents/en/chapter02/02_14_Tsimerman_Arithmetic/), [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/), [Langlands / Ngô]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/). Same 2014 class: [Avila]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/), [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/).

---

## Background Knowledge Map: What Are Arithmetic Statistics and the Geometry of Numbers?

Instead of trying to solve one Diophantine equation at a time (which can be impossible!), **arithmetic statistics** asks: *if you pick a number field or an elliptic curve "at random," what does a typical one look like?* Three classical ingredients power Bhargava’s factory.

### 1. Geometry of Numbers: Counting Lattice Points by Measuring Volume
**What is it?** Founded by Hermann Minkowski in the 1890s, the **geometry of numbers** estimates how many integer grid points $$\mathbb{Z}^N$$ lie inside a geometric region $$\mathcal{R} \subset \mathbb{R}^N$$ by computing $$\operatorname{Vol}(\mathcal{R})$$—provided you can control thin, spiky "cusps" where the region stretches off to infinity!

**What does it study?**
- **Orbit parametrizations:** Turning an algebraic object (like a cubic or quartic number ring) into an equivalence class of integer tensors under a symmetry group like $$\mathrm{SL}_n(\mathbb{Z})$$.
- **Prehomogeneous vector spaces:** A tradition (Sato–Shintani, Wright, Yukie, Datskovsky–Wright) that counts integral orbits of algebraic groups to obtain asymptotic densities of number fields.

### 2. Quadratic Forms & Number Rings: From Gauss (1801) to Degree 5
**What is it?** A **binary quadratic form** $$Q(x,y) = ax^2 + bxy + cy^2$$ with integer coefficients has **discriminant** $$D = b^2 - 4ac$$. Gauss shocked mathematics in 1801 by showing that equivalence classes of forms of the same discriminant $$D$$ can be "multiplied" together to form a finite abelian group (the **ideal class group** of the quadratic ring of discriminant $$D$$).

**What does it study?**
- **Counting rings of rank $$n$$:** How many degree-$$n$$ number rings/fields have discriminant $$\lvert D\rvert < X$$ as $$X \to \infty$$?

### 3. Elliptic Curves, Mordell–Weil Rank & Selmer Groups
**What is it?** An **elliptic curve** $$E: y^2 = x^3 + Ax + B$$ has a group law on its rational points $$E(\mathbb{Q})$$. By the **Mordell–Weil theorem**,
$$
E(\mathbb{Q}) \simeq \mathbb{Z}^{r_E} \oplus E(\mathbb{Q})_{\mathrm{tors}},
$$
where $$r_E \ge 0$$ is the **rank**: $$r_E = 0$$ means only finitely many rational points; $$r_E \ge 1$$ means infinitely many!

**What does it study?**
- **Selmer groups $$\mathrm{Sel}_n(E)$$:** Directly computing $$r_E$$ is famously hard, so number theorists wrap $$E(\mathbb{Q})/nE(\mathbb{Q})$$ inside a finite, computable "shadow group" called the **$$n$$-Selmer group**—whose elements turn out to be parametrized by integer polynomials (binary quartics for $$n=2$, ternary cubics for $$n=3$, etc.)!

---

## 1. The Bhargava $$2\times 2\times 2$$ cube: verifying Gauss composition by hand

### Hand-Verifiable Example 1: One Cube, Three Forms, Discriminant $$-23$$
Place eight integers on the corners of a $$2\times 2\times 2$$ cube by writing its front face $$M_1$$ and back face $$M_2$$:

$$
M_1 = \begin{pmatrix} -1 & 1 \\ 1 & 1 \end{pmatrix},
\qquad
M_2 = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}.
$$

Now compute the binary quadratic form $$Q_1(x,y) = -\det(M_1 x + M_2 y)$$ by hand! First form the combined $$2\times 2$$ matrix:

$$
M_1 x + M_2 y = \begin{pmatrix} -x + y & x + y \\ x + y & x - 2y \end{pmatrix}.
$$

Take the negative determinant:

$$
\begin{aligned}
Q_1(x,y) &= -\Bigl((-x+y)(x-2y) - (x+y)^2\Bigr) \\
&= -\Bigl((-x^2 + 3xy - 2y^2) - (x^2 + 2xy + y^2)\Bigr) \\
&= -\bigl(-2x^2 + xy - 3y^2\bigr) = 2x^2 - xy + 3y^2!
\end{aligned}
$$

Check its discriminant:
$$
D = b^2 - 4ac = (-1)^2 - 4(2)(3) = 1 - 24 = -23.
$$

Now slice the exact same cube **left/right** and **top/bottom**! Because our cube was chosen symmetrically (every face pair equals $$(M_1, M_2)$$), all three slicings yield the **exact same form**:

$$
Q_1 = Q_2 = Q_3 = 2x^2 - xy + 3y^2 \quad (\text{discriminant } -23).
$$

Bhargava’s Cube Law states that the three forms sliced from **any** $$2\times 2\times 2$$ integer cube always multiply to the identity in Gauss’s class group:

$$
Q_1 \cdot Q_2 \cdot Q_3 = 1 \;\Longrightarrow\; (2x^2 - xy + 3y^2)^3 = 1!
$$

In six lines of elementary determinant arithmetic, you just constructed an element of order $$3$$ in the class group of $$\mathbb{Q}(\sqrt{-23})$$—no 20-page Gauss identities required!

---

## 2. Higher composition laws: counting rings of rank 2, 3, 4, and 5

That $$2\times 2\times 2$$ cube was merely the appetizer. In his Princeton PhD thesis (advised by Andrew Wiles) and four landmark *Annals of Mathematics* papers (*Higher composition laws I–IV*, 2004–2008), Bhargava discovered a whole zoo of **higher composition laws** parametrizing rings of small rank over $$\mathbb{Z}$$:

- **Rank 2 (quadratic rings):** $$2\times 2\times 2$$ cubes and binary quadratic forms.
- **Rank 3 (cubic rings):** Pairs of $$3\times 3$$ symmetric matrices / binary cubic forms.
- **Rank 4 (quartic rings):** Pairs of ternary quadratic forms ($$2\times 3\times 3$$ symmetric boxes!).
- **Rank 5 (quintic rings):** Quadruples of skew-symmetric $$5\times 5$$ matrices ($$4\times \Lambda^2 \mathbb{Z}^5$$)!

Once rings are parametrized as integer orbits, the **geometry of numbers** computes the exact asymptotic number of quartic and quintic number fields of discriminant $$\lvert D\rvert < X$$—completing a quest that had stalled at degree 3 since Davenport–Heilbronn (1971). (Degree $$6$$ and higher remain wide open!)

---

## 3. Average ranks of elliptic curves (with Arul Shankar)

### Hand-Verifiable Example 2: Rank 0 vs. Rank 1 Elliptic Curves
Before bounding average ranks, feel the difference between rank $$0$$ and rank $$1$$ on two concrete curves:

- **Rank 0: $$E_0: y^2 = x^3 - x$$.** Factor the right side as $$x(x-1)(x+1)$$. Its only rational points are $$(0,0), (1,0), (-1,0)$$ plus the point at infinity—just **4 points total** (all torsion), so $$r_{E_0} = 0$$!
- **Rank 1: $$E_1: y^2 = x^3 - 2$$.** Check $$(x,y) = (3,5)$$ by hand: $$5^2 = 25 = 27 - 2 = 3^3 - 2$$! Using the chord-and-tangent law, doubling $$(3,5)$$ produces $$\left(\frac{129}{100}, -\frac{383}{1000}\right)$$, and repeating generates **infinitely many** rational points, so $$r_{E_1} = 1$$!

Now order all elliptic curves $$y^2 = x^3 + Ax + B$$ by their naive height $$H(E) = \max(4\lvert A\rvert^3, 27B^2)$$. What is the **average rank** $$\mathbb{E}[r_E]$$? Before 2010, nobody could even prove unconditionally that the average rank was **finite**—for all anyone knew, it could have diverged to $$\infty$$!

---

### Deep-Dive Explanation: How Bhargava–Shankar Bounded Average Elliptic Ranks (Read Slowly)

How did a $$2\times 2\times 2$$ cube for Gauss composition end up bounding the average rank of elliptic curves? Follow the four-step factory slowly:

#### Step 1: Trap the rank inside the finite $$2$$-Selmer group
The Mordell–Weil rank $$r_E$$ sits inside an exact sequence with the **2-Selmer group** $$\mathrm{Sel}_2(E)$$ and the mysterious Shafarevich–Tate group $$\Sha(E)$$:

$$
0 \longrightarrow E(\mathbb{Q})/2E(\mathbb{Q}) \longrightarrow \mathrm{Sel}_2(E) \longrightarrow \Sha(E)[2] \longrightarrow 0.
$$

Because $$\lvert E(\mathbb{Q})/2E(\mathbb{Q})\rvert \ge 2^{r_E}$$, we get the elementary inequality

$$
2^{r_E} \le \lvert \mathrm{Sel}_2(E)\rvert.
$$

And since $$2^r \ge 2r$$ for every integer $$r \ge 0$$ (check by hand: $$r=0: 1 \ge 0$$; $$r=1: 2 \ge 2$$; $$r=2: 4 \ge 4$$; $$r=3: 8 \ge 6$$!), bounding the average of $$\lvert \mathrm{Sel}_2(E)\rvert$$ instantly bounds the average rank!

#### Step 2: Parametrize 2-Selmer elements by binary quartic forms!
Miraculously, every element of $$\mathrm{Sel}_2(E)$$ corresponds to an equivalence class of **binary quartic forms** $$f(x,y) = ax^4 + bx^3y + cx^2y^2 + dxy^3 + ey^4$$ (a close cousin of Bhargava’s higher composition spaces!) whose classical invariants $$(I, J)$$ match the curve’s coefficients $$(A, B)$$.

#### Step 3: Count integer quartics via the geometry of numbers (averaging trick + cusp slicing)
To count binary quartic forms of bounded invariants, Bhargava and Shankar had to tame wicked infinite cusps in the fundamental domain of $$\mathrm{PGL}_2(\mathbb{Z})$$. Using Bhargava’s signature **averaging method** (averaging over a compact ball of translates to fatten up the cusp) together with a sharp **uniformity/sieve estimate**, they proved an astonishingly clean exact number:

$$
\text{Average size of }\mathrm{Sel}_2(E) = 3!
$$

Check the immediate arithmetic consequence by hand! Using $$r_E \le \frac{1}{2}\lvert \mathrm{Sel}_2(E)\rvert$$ (and in fact $$2r_E \le 2^{r_E} \implies \mathbb{E}[r_E] \le \frac{1}{2}\mathbb{E}[2^{r_E}]$$, or more sharply $$r_E \le \frac{1}{2}(\lvert \mathrm{Sel}_2(E)\rvert - 1)$$? Wait—using $$2r \le 2^r$$ directly gives $$\mathbb{E}[r_E] \le \frac{3}{2} = 1.5$$!):

$$
\mathbb{E}[r_E] \le \frac{1}{2}\,\mathbb{E}\bigl[\lvert \mathrm{Sel}_2(E)\rvert\bigr] = \frac{3}{2} = 1.5!
$$

#### Step 4: Push to 3-, 4-, and 5-Selmer groups (and positive proportions)
Bhargava and Shankar didn’t stop at 2-Selmer! Counting ternary cubics (3-Selmer, average size $$4$$), pairs of quaternary quadrics (4-Selmer, average size $$7$$), and $$5\times 5$$ skew-symmetric spaces (5-Selmer, average size $$6$$) pushed the unconditional upper bound on average rank all the way down to **$$< 0.885$$**—proving that a **positive proportion** of elliptic curves have rank $$0$$ (and, with Christopher Skinner, a positive proportion have rank $$1$$, and over $$66\%$$ of all elliptic curves satisfy BSD!).

In one schematic line:

$$
\mathrm{Sel}_n(E)
\;\xrightarrow{\;\text{higher composition orbit space}\;}\;
\text{Geometry of numbers (average size }3,4,7,6\text{)}
\;\xrightarrow{\;n^{r_E} \le \lvert \mathrm{Sel}_n(E)\rvert\;}\;
\mathbb{E}[r_E] < 0.885.
$$

**What you must not say.** Heuristics predict the true average rank is $$1/2$$ (half rank $$0$$, half rank $$1$$, and $$0\%$$ rank $$\ge 2$$)—that remains a **conjecture**, not a theorem. And the [Birch–Swinnerton-Dyer conjecture]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/) remains open in full generality.

---

## 4. Honest attribution and biography

| Ingredient | Role |
|------------|------|
| Gauss composition (1801) | The rank-2 ancestor |
| Sato–Shintani, Wright, Yukie, Datskovsky–Wright | Prehomogeneous counts; cubic densities |
| Bhargava, *Higher composition laws* I–IV | Parametrizations and counts of rings of rank $$2$$–$$5$$ |
| Bhargava–Shankar | Average 2-Selmer size $$3$$ ($$\mathbb{E}[r_E] \le 1.5$$); 3/4/5-Selmer ($$\mathbb{E}[r_E] < 0.885$$); positive proportion of rank $$0$$ |
| Bhargava–Skinner (and others) | Positive proportion of rank $$1$$ and BSD for a positive proportion of curves |
| BSD (Birch, Swinnerton-Dyer; Millennium Problem) | Still open as a general identification of algebraic and analytic ranks |

Bhargava was born in 1974 in Hamilton, Ontario, grew up largely on Long Island, and is a professor at Princeton—the **first person of Indian origin** to win a Fields Medal.

---

## 5. Why a Fields Medal

The 2014 medal celebrates a **method that became a factory**. Higher composition laws are beautiful algebra on their own; they became transformative when the very same integral orbit spaces classifying number rings also classified Selmer elements of elliptic curves—turning arithmetic statistics into one of the most dynamic frontiers of twenty-first-century number theory.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Bhargava solved BSD.” | He bounded average *algebraic* ranks via Selmer groups (and proved BSD for a positive proportion of curves with Skinner); general BSD is still open. |
| “The average rank is proved to be $$1/2$$.” | $$1/2$$ is a heuristic; the proved theorem is that average rank is finite ($$\le 1.5$$ from 2-Selmer, $$< 0.885$$ from 5-Selmer). |
| “He invented the geometry of numbers.” | Minkowski, Davenport–Heilbronn, and the prehomogeneous school precede him. |
| “Higher composition is a law on all binary forms of all degrees.” | It is a specific family of orbit parametrizations on particular representations. |
| “Counting rings means listing them.” | It means proving asymptotic counts of isomorphism classes with $$\lvert\mathrm{disc}\rvert < X$$. |
| “Rank 0 for a positive proportion automatically proves $$L(E,1)\neq 0$$.” | Connecting algebraic rank $$0$$ to analytic rank $$0$$ requires deep modularity/Iwasawa inputs (as in Bhargava–Skinner). |

---

## Video and reading links

No course video-research pack is attached to this lesson.

1. IMU Fields Medals 2014 (citation): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014).
2. IMU news release, *The Work of Manjul Bhargava*: [PDF](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_bhargava.pdf).
3. Encyclopedia: [Manjul Bhargava](https://en.wikipedia.org/wiki/Manjul_Bhargava).
4. Quanta profile (2014): [The Musical, Magical Number Theorist](https://www.quantamagazine.org/number-theorist-manjul-bhargava-is-awarded-fields-medal-20140812/).
5. arXiv search: [Bhargava composition](https://arxiv.org/search/?query=Bhargava+composition&searchtype=all); [Bhargava Shankar elliptic](https://arxiv.org/search/?query=Bhargava+Shankar+elliptic&searchtype=all).
6. Course deep read on ranks and $$L$$-functions: [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/).

**Status reminder:** Average Selmer / average rank theorems—**not** a solution of BSD.

---

## References

1. International Mathematical Union, Fields Medals 2014 — Manjul Bhargava citation and news release.
2. **M. Bhargava**, *Higher composition laws* I–IV, *Ann. of Math.* (2004–2008).
3. **M. Bhargava, A. Shankar**, *Binary quartic forms having bounded invariants, and the boundedness of the average rank of elliptic curves*, *Ann. of Math.* 181 (2015).
4. **M. Bhargava, A. Shankar**, *Ternary cubic forms having bounded invariants, and the existence of a positive proportion of elliptic curves having rank 0*, *Ann. of Math.* 181 (2015).
5. Pointers for the older counting tradition: Davenport–Heilbronn; Datskovsky–Wright; surveys of prehomogeneous vector spaces (Wright, Yukie).
6. Course: [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/), [Tsimerman]({{ site.baseurl }}/contents/en/chapter02/02_14_Tsimerman_Arithmetic/), [Avila]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/).

---

## Further directions

- Work another Gauss-composition example by hand (discriminant $$-31$$) using a $$2\times 2\times 2$$ cube before reading *Higher composition laws I*.
- Read an expository account of 2-Selmer groups (e.g. a first chapter of Silverman plus a survey of arithmetic statistics) until the exact sequence above feels inevitable.
- Seminar A3 option: a one-page brief on *what remains open*—the exact average rank, BSD, and counting fields of degree $$\ge 6$$—without inflating 2014 into a closing of number theory.
- If you like cubes more than ranks, stay with the parametrizations; if you like ranks more than cubes, go to [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/) next and keep the Selmer/$$L$$-function distinction on the page.

## Video tham khảo

- **xem trước** — [Manjul Bhargava, The average rank of elliptic curves](https://www.youtube.com/watch?v=t5S8PO2PQgU) — Clay Mathematics Institute, English. Watch first. “Manjul Bhargava, The average rank of elliptic curves” orients the lesson’s aim: State the IMU 2014 citation in one paragraph, naming geometry of numbers, rings of small rank, and average elliptic ranks.
- [Manjul Bhargava - The average rank of elliptic curves: data, conjectures, and theorems](https://www.youtube.com/watch?v=zm1v_FaTglw) — princetonmathematics, English. A second pass once the main claim is in view: State the IMU 2014 citation in one paragraph, naming geometry of numbers, rings of small rank, and average elliptic ranks.
- [Manjul Bhargava - Rational points on elliptic and hyperelliptic curves MCA 2013](https://www.youtube.com/watch?v=6NHO-0FKAjM) — MCA2013, English. Further depth after the first two, still tied to this lesson: State the IMU 2014 citation in one paragraph, naming geometry of numbers, rings of small rank, and average elliptic ranks.
