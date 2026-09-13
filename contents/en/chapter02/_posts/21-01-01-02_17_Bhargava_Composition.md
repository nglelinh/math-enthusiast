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

**Manjul Bhargava** received the **Fields Medal 2014** for, in the IMU’s words, “developing powerful new methods in the **geometry of numbers**, which he applied to **count rings of small rank** and to **bound the average rank of elliptic curves**.” The citation is a pair of applications of one taste: parametrize arithmetic objects by integer points in representations of algebraic groups, then count those points with enough error control to extract densities and averages. Gauss already knew a composition law for binary quadratic forms. Bhargava found a web of **higher composition laws** and used them to enumerate orders in number fields of degree $$2,3,4,5$$ and, with **Arul Shankar**, to bound how large the Mordell–Weil rank of an elliptic curve over $$\mathbb{Q}$$ is *on average*.

This essay is for learners who have seen the class group of a quadratic order, or the group $$E(\mathbb{Q})$$ of rational points on an elliptic curve, and want the architecture of Bhargava’s counting program. It does **not** claim that he solved the [Birch–Swinnerton-Dyer conjecture]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/). The proved statements are about **Selmer groups** and therefore about algebraic ranks: a positive proportion of elliptic curves have rank $$0$$; the average rank, ordered by height, is finite and in fact bounded by an explicit constant; most curves, in the same ordering, have rank $$0$$ or $$1$$. Heuristics that the average rank should be $$1/2$$ remain heuristics.

---

## Learning objectives

After this lecture you should be able to:

- State the IMU 2014 citation in one paragraph, naming **geometry of numbers**, **rings of small rank**, and **average elliptic ranks**.
- Explain Gauss composition of binary quadratic forms as a group law on forms of fixed discriminant, and say what a **higher composition law** is allowed to be (an algebraic parametrization, not a mystery binary operation on all forms).
- Describe, at slogan level, how orbits in integral representations parametrize rings of rank $$2,3,4,5$$ over $$\mathbb{Z}$$.
- Distinguish **average size of a Selmer group** from a proof of BSD, and quote a correct rank conclusion (positive proportion of rank $$0$$; average rank bounded).
- Place the method in the **prehomogeneous vector space** tradition (Sato–Shintani, Wright, Yukie, Datskovsky–Wright) rather than in a vacuum.
- Record the common biographical account: Bhargava is the **first person of Indian origin** to receive a Fields Medal. Practice **LO6** on “he solved elliptic curves.”

**Prerequisites.** Rings and ideals at the level of a first algebra course; binary quadratic forms $$ax^2+bxy+cy^2$$ and the discriminant $$b^2-4ac$$; the slogan that an elliptic curve over $$\mathbb{Q}$$ has a finitely generated group of rational points $$E(\mathbb{Q})\simeq\mathbb{Z}^r\oplus E(\mathbb{Q})_{\mathrm{tors}}$$. No prior class-field theory is required.

**Seminar links.** The rank story is the arithmetic twin of [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/): same objects, different question (averages versus $$L$$-functions). Nearby portraits: [Tsimerman]({{ site.baseurl }}/contents/en/chapter02/02_14_Tsimerman_Arithmetic/), [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/), [Langlands / Ngô]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/). Same 2014 class: [Avila]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/), [Mirzakhani]({{ site.baseurl }}/contents/en/chapter02/02_05_Mirzakhani_Moduli/).

---

## 1. A history of composing forms

In 1801, **Gauss** described a law for composing two primitive binary quadratic forms of the same discriminant. In modern language, classes of such forms correspond to ideal classes in the quadratic order of that discriminant, and composition is the class-group law written in coordinates $$(a,b,c)$$. The construction is elementary and notorious: students meet it as a thicket of identities long before they meet Picard groups.

The twentieth century recast the same phenomenon as **representation theory plus geometry of numbers**. Integer orbits of a group such as $$\mathrm{SL}_2(\mathbb{Z})$$ acting on a lattice of forms parametrize arithmetic objects; Minkowski’s geometry of numbers, and later the geometry of **prehomogeneous vector spaces** (Sato, Shintani, and the arithmetic developments of Wright, Yukie, Datskovsky–Wright, and others), supply a way to *count* those orbits with bounded discriminant. Cubic rings and cubic fields were already accessible in that language. Quartic and quintic rings looked messier: the natural spaces of forms are larger, the stabilizers more delicate, and the passage from an order to its field of fractions loses information that a count of *fields* still needs.

Bhargava’s thesis *Higher composition laws* (Princeton, 2001, advised by **Andrew Wiles**) and the subsequent *Annals* series (2004–2008) rebuilt the dictionary. A memorable piece of linear algebra—the **Bhargava cube**, a $$2\times 2\times 2$$ box of integers—can be sliced in three ways into pairs of $$2\times 2$$ matrices, yielding three binary quadratic forms whose Gauss composition is encoded by the cube. That is not a party trick. It is the rank-$$2$$ case of a systematic pattern: interesting rings appear as orbits in concrete integral representations, and composition laws are the algebraic identities that make the orbit space into a groupoid or a fibered product of class groups.

**Slogan.** To count rings, first *parametrize* them by integer points; then count the points. Composition is the structure that tells you the parametrization is not an accident.

---

## 2. What the theorems rearrange: rings of rank 2, 3, 4, 5

A **ring of rank $$n$$** over $$\mathbb{Z}$$ is a ring whose underlying abelian group is isomorphic to $$\mathbb{Z}^n$$ (an order in an étale $$\mathbb{Q}$$-algebra of dimension $$n$$, in the typical number-theoretic case). The discriminant of such a ring is an integer; the counting problem asks for the number of isomorphism classes with $$|\mathrm{disc}|<X$$, as $$X\to\infty$$.

Bhargava’s higher composition laws give orbit parametrizations:

- **Rank 2.** Quadratic rings, recovered from Gauss composition and from cubes / pairs of forms.
- **Rank 3.** Cubic rings, related to binary cubic forms and to pairs of ternary quadrics—the cubic analogue of Gauss composition (*Higher composition laws II*).
- **Rank 4.** Quartic rings, parametrized in *Higher composition laws III*.
- **Rank 5.** Quintic rings, parametrized in *Higher composition laws IV*.

Once the parametrization is in hand, geometry-of-numbers estimates—volumes of fundamental domains, cusps, and error terms for the number of lattice points—produce **asymptotics for the density of discriminants** of quartic and quintic rings and fields. That is the sense in which the IMU says he *counted* rings of small rank: not a finite list, but a main term in $$X$$ (and a controlled error) for each small $$n$$.

**What this rearranges.** Cubic fields already had a Davenport–Heilbronn-type density story; quartic and quintic fields sat at the edge of what prehomogeneous methods had digested. After the papers, degree $$\le 5$$ is one chapter: the same orbit-counting machine, with more elaborate representations. Degree $$6$$ and beyond remain a different world.

**Honesty about tradition.** The line includes Minkowski, Siegel, Davenport–Heilbronn, and the prehomogeneous counts of Wright, Yukie, and Datskovsky–Wright. Bhargava’s contribution is a new supply of parametrizations—especially for quartic and quintic rings—and error control that later unlocked elliptic curves. Geometry of numbers did not begin in 2001.

---

## 3. Average ranks of elliptic curves, with Shankar

An elliptic curve over $$\mathbb{Q}$$ may be written in short Weierstrass form $$y^2=x^3+Ax+B$$, and ordered by a **height** built from $$A,B$$. Mordell–Weil says

$$
E(\mathbb{Q})\simeq\mathbb{Z}^{r_E}\oplus E(\mathbb{Q})_{\mathrm{tors}},
$$

and the integer $$r_E$$ is the **algebraic rank**. The [BSD conjecture]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/) predicts that $$r_E$$ equals the order of vanishing of the $$L$$-function $$L(E,s)$$ at $$s=1$$. That equality is **not** what Bhargava proved.

What *is* accessible, if you can count integral orbits of binary quartic forms (and later ternary cubics, and higher Selmer representations), is the **2-Selmer group** $$\mathrm{Sel}_2(E)$$. It sits in an exact sequence that squeezes the rank:

$$
0\to E(\mathbb{Q})/2E(\mathbb{Q})\to\mathrm{Sel}_2(E)\to\Sha(E)[2]\to 0.
$$

An upper bound on the average size of $$\mathrm{Sel}_2$$ is therefore an upper bound on the average of $$2^{r_E}$$ (up to the 2-torsion, which is cheap). **Bhargava–Shankar** proved that the average size of the 2-Selmer group, for elliptic curves over $$\mathbb{Q}$$ ordered by height, is **$$3$$**. A formal consequence is that the **average rank is at most $$1.5$$**—in particular finite, which was not known unconditionally in this ordering. Their paper on ternary cubic forms shows that a **positive proportion** of curves have rank $$0$$. Later papers in the same program (3-Selmer, 4-Selmer, 5-Selmer, and work with other collaborators) strengthen the picture: a majority of curves have rank $$0$$ or $$1$$. A companion preprint of Bhargava–Skinner, already flagged in the 2014 IMU news release, shows a positive proportion of rank one.

**What you must not say.** You must not say that the average rank *equals* $$1/2$$ as a theorem. Random-matrix and BSD heuristics suggest that most curves have rank $$0$$ or $$1$$ with a slight bias toward rank $$0$$, so that the average should be $$1/2$$; that is a **conjectural** average, not the Bhargava–Shankar theorem. You must not say that BSD is proved. Knowing that $$r_E\le 1$$ for most $$E$$ is compatible with BSD and is a major arithmetic input; it is not the identification of $$r_E$$ with an analytic rank for every curve.

**Slogan.** Selmer groups are *finite, countable shadows* of the Mordell–Weil group. Average Selmer size is a geometry-of-numbers problem. Average rank is what remains after you throw away the part of Selmer that might be Sha.

---

## 4. Honest attribution and biography

| Ingredient | Role |
|------------|------|
| Gauss composition | The rank-2 ancestor |
| Sato–Shintani, Wright, Yukie, Datskovsky–Wright | Prehomogeneous counts; cubic densities |
| Bhargava, *Higher composition laws* I–IV | Parametrizations of rings of rank $$2$$–$$5$$ |
| Bhargava–Shankar | Average 2-Selmer size $$3$$; positive proportion of rank $$0$$; bounded average rank |
| Later Selmer papers; Bhargava–Skinner and others | Rank $$0$$ or $$1$$ for most curves; positive proportion of rank one |
| BSD (Birch, Swinnerton-Dyer; Clay problem) | Still open as a general identification of algebraic and analytic ranks |

Bhargava was born in 1974 in Hamilton, Ontario, grew up largely on Long Island, and is an Indian-Canadian-American mathematician at Princeton. The standard public account is that he is the **first person of Indian origin** to win a Fields Medal—a fact about the medal’s history, not a theorem. His advisor was Wiles; that is not a claim that the composition laws are a chapter of Fermat’s Last Theorem.

---

## 5. Why a Fields Medal

The medal is for a *method that became a factory*. Higher composition laws are interesting as algebra; they become Fields-level when the same orbit spaces that classify rings also classify 2-Selmer elements of elliptic curves. Counting then answers questions number theory had wanted since at least the 1960s—how many fields? how large a typical rank?—at the asymptotic, average-case scale of modern arithmetic statistics.

BSD remains a flagship open problem in Chapter 1. Bhargava’s 2014 work *rearranges the landscape around* it: a typical elliptic curve over $$\mathbb{Q}$$ is arithmetically small. That is a different achievement from proving $$L(E,1)\neq 0$$ for one famous curve.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Bhargava solved BSD.” | He bounded average *algebraic* ranks via Selmer groups. BSD is still open. |
| “The average rank is $$1/2$$.” | That is a heuristic. The theorem is that the average is finite (e.g. $$\le 1.5$$ from 2-Selmer) and that most ranks are $$0$$ or $$1$$. |
| “He invented the geometry of numbers.” | Minkowski, Davenport–Heilbronn, and the prehomogeneous school precede him. |
| “Higher composition is a law on all binary forms of all degrees.” | It is a family of orbit parametrizations defined on specific representations. |
| “Counting rings means listing them.” | It means asymptotics for the number of isomorphism classes of bounded discriminant. |
| “Rank 0 for a positive proportion proves the $$L$$-function does not vanish.” | Algebraic rank $$0$$ is not automatically analytic rank $$0$$; that implication is a piece of BSD. |

---

## Exercises

1. In one paragraph, what does Gauss composition *do* for quadratic orders? Use the words “class group” and “discriminant.”
2. Why does a $$2\times 2\times 2$$ cube of integers have *three* natural pairs of binary quadratic forms? (Slicing directions.) No need for the full identities.
3. What is a ring of rank $$4$$ over $$\mathbb{Z}$$, at slogan level? Why is counting them harder than counting quadratic orders?
4. Write the exact sequence that relates $$E(\mathbb{Q})/2E(\mathbb{Q})$$, $$\mathrm{Sel}_2(E)$$, and $$\Sha(E)[2]$$. Where does average rank hide?
5. **Accuracy practice.** A headline reads “Mathematician solves 350-year-old elliptic curve mystery.” Rewrite it in two sentences that could appear in this course.
6. How would a proof of BSD *plus* Bhargava–Shankar change the meaning of “average analytic rank”? One careful paragraph.
7. Skim the IMU 2014 news release on Bhargava and list two results that are *not* about elliptic curves (e.g. hyperelliptic points, the 290 theorem with Hanke).
8. **Seminar stretch.** Compare “average rank of elliptic curves” with [Avila’s]({{ site.baseurl }}/contents/en/chapter02/02_16_Avila_Dynamics/) “typical unimodal map”: both replace classification by a measure on a space of objects. What is the measure here?

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

- Work one Gauss-composition example by hand (discriminant $$-23$$ or $$-31$$) before reading *Higher composition laws I*.
- Read an expository account of 2-Selmer groups (e.g. a first chapter of Silverman plus a survey of arithmetic statistics) until the exact sequence above feels inevitable.
- Seminar A3 option: a one-page brief on *what remains open*—the exact average rank, BSD, and counting fields of degree $$\ge 6$$—without inflating 2014 into a closing of number theory.
- If you like cubes more than ranks, stay with the parametrizations; if you like ranks more than cubes, go to [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/) next and keep the Selmer/$$L$$-function distinction on the page.
