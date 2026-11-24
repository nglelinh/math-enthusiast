---
layout: post
title: "Archimedes' Cattle Problem and Pell's Equation"
chapter: '04'
order: 13
owner: Nguyen Le Linh
lang: en
categories:
- chapter04
---

A 44-line Greek poem, sent by **Archimedes** to **Eratosthenes**, asks how many cattle belong to the Sun god. The first half looks like a school ratio puzzle. The second half turns it into one of the most famous **Pell equations** in history. The smallest herd that satisfies every condition has **206,545 digits**—a number that would fill dozens of printed pages.

This lecture is about that shock, and about the machine behind it: the equation $$x^2-dy^2=1$$, the group law that manufactures infinitely many solutions from one, and the continued-fraction algorithm that finds the first.

**Path:** the riddle → linear part vs square/triangle constraints → Pell (and the naming error) → Brahmagupta composition → continued fractions for $$d=2$$ → why sizes explode → negative Pell / Stevenhagen → confusions, exercises.

The source exposition is [Toán Khó (7 Aug 2026)](https://toankho.com/2026/08/07/bai-toan-dan-bo-cua-archimedes-va-phuong-trinh-pell/). What follows is reconstructed mathematics, not a translation of that page.

---

## Learning objectives

After this lecture you should be able to:

- Separate the cattle problem into a **linear** stage and a **Pell** stage, and say what each produces.
- State the **Pell equation** $$x^2-dy^2=1$$ ($$d>0$$ square-free) and name who actually developed it (not John Pell).
- Multiply two solutions by **Brahmagupta composition** and interpret the product as a unit in $$\mathbb{Z}[\sqrt{d}]$$.
- Compute the fundamental solution of $$x^2-2y^2=1$$ from convergents of $$\sqrt{2}$$, and generate the next few.
- Explain why a “tiny” change in $$d$$ can explode the number of digits, using $$d=61$$ and the cattle herd as exhibits.
- State Lagrange’s theorem for $$+1$$ and the **Stevenhagen** density for $$-1$$ without claiming “58% of all $$d$$.”

**Prerequisites.** Integers, squares, the idea of a continued fraction. The [irrationality of $$\sqrt{2}$$]({{ site.baseurl }}/contents/en/chapter05/05_06_Irrationality_Sqrt2/) lecture is the natural companion.

---

## 1. A poem that is not a folk riddle

Write $$W,B,Y,D$$ for the numbers of **bulls** that are white, black, yellow, and dappled, and $$w,b,y,d$$ for the corresponding **cows**. Archimedes’ seven ratio conditions are linear:

$$
\begin{aligned}
W &= Y + \tfrac{5}{6}B, &
B &= Y + \tfrac{9}{20}D, &
D &= Y + \tfrac{13}{42}W,\\
w &= \tfrac{7}{12}(B+b), &
b &= \tfrac{9}{20}(D+d), &
d &= \tfrac{11}{30}(Y+y), &
y &= \tfrac{13}{42}(W+w).
\end{aligned}
$$

Eight positive-integer unknowns and seven independent linear relations leave a **one-parameter family**. The smallest positive solution already has total herd

$$
W+B+Y+D+w+b+y+d = 50{,}389{,}082
$$

(with $$W=10{,}366{,}482$$, $$B=7{,}460{,}514$$, $$Y=4{,}149{,}387$$, $$D=7{,}358{,}060$$). That is large for a school puzzle, but it is still a number you can write down.

The poem then adds two **geometric** constraints:

$$
W+B = m^2, \qquad D+Y = \frac{n(n+1)}{2}
$$

for some integers $$m,n\ge 1$$ (bulls of two colours form a square; bulls of the other two form a triangular number). Substituting the linear family into these two conditions collapses the problem onto a single Pell equation. In unreduced form one meets

$$
x^2 - 410{,}286{,}423{,}278{,}424\, y^2 = 1;
$$

after stripping square factors the equation usually solved is

$$
u^2 - 4{,}729{,}494\, v^2 = 1.
$$

**Status.** The cattle problem is **solved**. It is not an open conjecture. The remaining drama is the *size* of the smallest solution and the *structure* that produces it.

---

## 2. The Pell equation, misnamed

For a positive integer $$d$$ that is **not a square**, the **Pell equation** is

$$
x^2 - d y^2 = 1, \qquad x,y\in\mathbb{Z}.
$$

The trivial solution $$(x,y)=(\pm 1,0)$$ always exists. The content of the theory is that there is a **fundamental solution** $$(x_1,y_1)$$ with $$x_1>1$$, $$y_1>0$$ smallest, and that every other positive solution is generated from it by a group law (next section).

**Naming.** Euler attached John Pell’s name to the equation by mistake. Pell contributed essentially nothing here. The European 17th-century work Fermat challenged, and Brouncker solved, is the relevant Western thread. A much older, deeper thread is Indian: **Brahmagupta** (628, *Brāhmasphuṭasiddhānta*) and **Bhāskara II** (12th century, *cakravāla*).

Lagrange (1768) proved that a nontrivial solution exists for **every** nonsquare $$d>0$$, and that there are infinitely many. That theorem is the $$+1$$ theory in finished form.

---

## 3. Brahmagupta’s composition, in one identity

If $$x_1^2-dy_1^2=k_1$$ and $$x_2^2-dy_2^2=k_2$$, then

$$
(x_1x_2+d y_1y_2)^2 - d(x_1y_2+x_2y_1)^2 = k_1k_2.
$$

In particular, solutions of $$x^2-dy^2=1$$ can be **multiplied**:

$$
(x_1,y_1)\ast(x_2,y_2) = (x_1x_2+d y_1y_2,\ x_1y_2+x_2y_1).
$$

The algebraic meaning is the norm-multiplicativity

$$
(x_1+y_1\sqrt{d})(x_2+y_2\sqrt{d}) = (x_1x_2+dy_1y_2)+(x_1y_2+x_2y_1)\sqrt{d}
$$

in the ring $$\mathbb{Z}[\sqrt{d}]$$. Solutions of Pell’s equation are precisely the units of **norm $$+1$$**. Powers of the fundamental unit of norm $$+1$$ therefore give every positive solution.

This is why “find one solution, get infinitely many” is not a slogan: it is the unit group of a real quadratic order, a baby case of Dirichlet’s unit theorem.

---

## 4. How to find the first solution: $$d=2$$

The continued fraction of a nonsquare is eventually periodic. For $$d=2$$,

$$
\sqrt{2} = [1;\overline{2}] = 1+\frac{1}{2+\frac{1}{2+\cdots}}.
$$

Convergents:

| $$n$$ | $$p_n/q_n$$ | $$p_n^2-2q_n^2$$ |
|------:|:-----------:|-----------------:|
| 0 | $$1/1$$ | $$-1$$ |
| 1 | $$3/2$$ | $$+1$$ |

So $$(x_1,y_1)=(3,2)$$ is the fundamental solution of $$x^2-2y^2=1$$. The previous convergent solves the **negative** Pell equation $$x^2-2y^2=-1$$.

Composing $$(3,2)$$ with itself:

$$
(3,2)\ast(3,2) = (9+8,\ 6+6) = (17,12),
$$

and then $$(17,12)\ast(3,2)=(99,70)$$. The sequence continues $$(1,0),\ (3,2),\ (17,12),\ (99,70),\ (577,408),\ \ldots$$.

![Integer points on the hyperbola x² − 2y² = 1]({{ site.baseurl }}/img/chapter_img/pell_hyperbola_d2_toankho.png)

*Figure. The hyperbola $$x^2-2y^2=1$$ and its integer points. The table of solutions is correct. The boxed formula $$x+y\sqrt{2}=(1+\sqrt{2})^n$$ is **not**: $$1+\sqrt{2}$$ has norm $$-1$$, so odd powers solve $$x^2-2y^2=-1$$. The $$+1$$ solutions are the even powers, equivalently $$(x+y\sqrt{2})=(3+2\sqrt{2})^n=(1+\sqrt{2})^{2n}$$. (Source illustration: [Toán Khó](https://toankho.com/2026/08/07/bai-toan-dan-bo-cua-archimedes-va-phuong-trinh-pell/); AI-generated.)*

Lagrange’s proof that a solution always exists is that some convergent of $$\sqrt{d}$$ satisfies $$p^2-dq^2=\pm 1$$, and composing a $$-1$$ solution with itself produces a $$+1$$ solution.

---

## 5. Why the numbers explode

Nothing in the shape of $$x^2-dy^2=1$$ warns you how large $$x_1$$ will be. The size is governed by the **regulator** $$\log(x_1+y_1\sqrt{d})$$, which can jump by orders of magnitude when $$d$$ changes by 1.

Fermat’s 1657 challenge $$x^2-61y^2=1$$ already has fundamental solution

$$
x_1 = 1{,}766{,}319{,}049, \qquad y_1 = 226{,}153{,}980.
$$

Ten and nine digits, for a coefficient you can count on two hands.

The cattle problem is the same phenomenon at theatrical scale. A. Amthor (1880) determined that the smallest total herd is

$$
\approx 7.760271\times 10^{206544},
$$

a **206,545-digit** integer—far larger than the number of atoms in the observable universe ($$\sim 10^{80}$$). Later machine computations (Williams–German–Zarnke 1965; Nelson 1981) produced the full decimal expansion. That computation **exhibits** the solution; it does not replace Lagrange’s existence theorem, which already applied to $$d=4{,}729{,}494$$.

![Popular poster for the cattle/Pell story]({{ site.baseurl }}/img/chapter_img/pell_digit_explosion_toankho.png)

*Figure. A popular poster from the source article. The digit count **206,545** is the size of Archimedes’ smallest full herd. The poster’s claim that this count belongs to $$d=226$$ is **false**—the reduced cattle discriminant is $$4{,}729{,}494$$. Use the picture as an LO6 exercise in reading popular math, not as a data source. (AI-generated illustration, Toán Khó.)*

---

## 6. What is proved, what is subtler

| Claim | Status |
|-------|--------|
| $$x^2-dy^2=1$$ has infinitely many solutions for every nonsquare $$d>0$$ | **Theorem** (Lagrange 1768) |
| A fundamental solution can be read from the continued fraction of $$\sqrt{d}$$ | **Theorem** |
| Archimedes’ cattle problem has a (gigantic) positive solution | **Solved** (existence 19th c.; full digits 20th c.) |
| $$x^2-dy^2=-1$$ is solvable for every such $$d$$ | **False** (local and global obstructions) |
| Among Stevenhagen’s eligible square-free $$d$$, the density of those for which $$-1$$ is solvable | **Theorem** (Stevenhagen’s conjecture, 1993; proved by Koymans–Pagano, 2022, [arXiv:2201.13424](https://arxiv.org/abs/2201.13424)). The constant is $$\approx 58.06\%$$, **not** “58% of all $$d$$.” |

The negative Pell equation $$x^2-dy^2=-1$$ asks whether the fundamental unit of $$\mathbb{Q}(\sqrt{d})$$ has norm $$-1$$. That is a question about the 2-part of class groups and Rédei symbols, not a second copy of Lagrange.

**Do not overclaim applications.** Real-quadratic units (Pell) and imaginary-quadratic **class groups** (the setting of CSIDH and some class-group VDFs) live in the same algebraic-number-theory neighbourhood. They are not the same object. Pell is not a post-quantum cryptosystem.

---

## Common misconceptions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Pell invented the Pell equation.” | **Fail** | Euler’s misattribution; see Brouncker / Brahmagupta / Bhāskara. |
| “The cattle poem is a few-thousand-head puzzle.” | **Fail** | Linear part: $$\sim 5\times 10^7$$. Full problem: $$206{,}545$$ digits. |
| “$$1+\sqrt{2}$$ generates the $$+1$$ solutions for $$d=2$$.” | **Fail** | It generates the **norm $$-1$$** solutions; square it. |
| “Stevenhagen says 58% of all $$d$$ work for $$-1$$.” | **Fail** | Density inside a specified eligible family, not among all square-free $$d$$. |
| “206,545 digits is the solution for $$d=226$$.” | **Fail** | That is the cattle herd; reduced $$d=4{,}729{,}494$$. |
| “Pell = CSIDH.” | **Fail** | Neighbouring arithmetic, different groups. |

---

## References

- Source page: [Bài toán đàn bò của Archimedes và phương trình Pell](https://toankho.com/2026/08/07/bai-toan-dan-bo-cua-archimedes-va-phuong-trinh-pell/) (Toán Khó, accessed 2026-08-13). Figures are AI-generated; treat numbers in the art as untrusted.
- Quanta: [Ancient Equations Offer New Look at Number Groups](https://www.quantamagazine.org/ancient-equations-offer-new-look-at-number-groups-20220810/) (10 Aug 2022).
- P. Koymans & C. Pagano, *On Stevenhagen’s conjecture*, [arXiv:2201.13424](https://arxiv.org/abs/2201.13424).
- H. W. Lenstra Jr., *Solving the Pell equation*, Notices AMS **49** (2002) — the standard modern survey.
- E. J. Barbeau, *Pell’s Equation* (Springer) — worked examples, including $$d=61$$.
- Companion in this course: [Irrationality of $$\sqrt{2}$$]({{ site.baseurl }}/contents/en/chapter05/05_06_Irrationality_Sqrt2/); [Number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/) (do not conflate Pell units with RSA/CSIDH).

---

## Further directions

- Run the continued-fraction algorithm for a few small $$d$$ (2, 3, 7, 13, 61) and watch the period length.
- Read Lenstra’s survey until the words *regulator* and *infrastructure* become slogans you could define.
- Ask a precise leftover question—for example: “Which convergents of $$\sqrt{d}$$ can fail to give a Pell unit, and why?”
