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

Around 200 BCE, **Archimedes of Syracuse** sent a 44-line Greek epigram to his friend **Eratosthenes**, the chief librarian of Alexandria, playfully challenging him to count the Sun god’s sacred herd of cattle grazing on the plains of Sicily. The first half of the poem reads like an innocent school ratio puzzle—white bulls, black bulls, yellow cows, and dappled cows linked by clean fractions. Solve those seven linear equations and you get a brisk 50-million-head herd. Then the poem’s closing lines add two deceptively harmless geometric twists—making one pair of bulls form a square and another form a triangle—and the puzzle detonates. The smallest herd satisfying the entire poem is a number with **206,545 digits**, dwarfing the number of atoms in the observable universe by more than 206,000 orders of magnitude!

Hidden inside Archimedes’ ancient poem is one of the most enchanting machines in all of number theory: **Pell’s equation**

$$
x^2 - d y^2 = 1.
$$

In this lecture, you will see how a single tiny integer equation bridges ancient Indian algebra (Brahmagupta), continued fractions, algebraic number rings $$\mathbb{Z}[\sqrt{d}]$$, and a 2022 breakthrough on the negative Pell equation.

**Path:** Archimedes’ poem (linear vs. Pell stage) → Pell’s misnamed history → Brahmagupta composition worked out → continued-fraction machine for $$\sqrt{2}$$ and $$\sqrt{7}$$ → why solutions explode ($$d=60$$ vs. $$d=61$$) → negative Pell, modulo-3 obstruction, and Stevenhagen’s theorem → common misconceptions and further directions.

The source exposition is [Toán Khó (7 Aug 2026)](https://toankho.com/2026/08/07/bai-toan-dan-bo-cua-archimedes-va-phuong-trinh-pell/). What follows is reconstructed mathematics, not a translation of that page.

---

## Learning objectives

After this lecture you should be able to:

- Separate Archimedes’ cattle problem into its **linear** stage ($$\sim 5\times 10^7$$) and its **Pell** stage (206,545 digits).
- State **Pell’s equation** $$x^2 - dy^2 = 1$$ ($$d > 0$$ nonsquare) and credit its true pioneers (Brahmagupta, Bhāskara II, Brouncker, Lagrange—not John Pell).
- Multiply two solutions via **Brahmagupta composition** and interpret them as norm-$$+1$$ units in $$\mathbb{Z}[\sqrt{d}]$$.
- Run the **continued-fraction algorithm** by hand for $$\sqrt{2}$$ and $$\sqrt{7}$$ to extract the fundamental solution and generate larger solutions.
- Explain why a tiny change in $$d$$ (from $$60$$ to $$61$$) explodes the fundamental solution, and use a modulo-3 check to show why $$x^2 - 3y^2 = -1$$ has no integer solutions.
- State Lagrange’s theorem for $$+1$$ and the **Stevenhagen–Koymans–Pagano** density for $$-1$$ accurately without claiming "58% of all $$d$$."

**Prerequisites.** Integers, squares, modular arithmetic, and basic fractions. The [irrationality of $$\sqrt{2}$$]({{ site.baseurl }}/contents/en/chapter05/05_06_Irrationality_Sqrt2/) lecture is a natural companion.

---

## Key ideas: Where Ancient Riddles Meet Algebraic Number Theory

Pell’s equation looks like high-school algebra, yet it is the doorway to four towering branches of number theory:

1. **Diophantine Equations:** Solving polynomial equations strictly in *integers* is vastly harder than solving them in real numbers. While $$x^2 - dy^2 = 1$$ is just a smooth hyperbola in $$\mathbb{R}^2$$, hunting for integer lattice points $$(x,y)\in\mathbb{Z}^2$$ on that hyperbola requires deep arithmetic structure.
2. **Algebraic Number Theory (Rings of Integers & Units):** Factoring $$x^2 - dy^2 = (x + y\sqrt{d})(x - y\sqrt{d}) = 1$$ reveals that Pell solutions are precisely the **units of norm $$+1$$** in the real quadratic ring $$\mathbb{Z}[\sqrt{d}]$$. That explains why finding *one* solution generates *all infinitely many* solutions via powers—a baby case of **Dirichlet’s Unit Theorem**.
3. **Continued Fractions & Diophantine Approximation:** Because $$x^2 - dy^2 = 1 \implies \frac{x}{y} \approx \sqrt{d}$$, every Pell solution gives an extraordinarily accurate rational approximation to $$\sqrt{d}$$. Expanding $$\sqrt{d}$$ as a periodic continued fraction automatically manufactures those best rational approximations—guaranteeing a solution exists for *every* nonsquare $$d > 0$$ (Lagrange, 1768).
4. **Arithmetic Statistics (Negative Pell & Class Groups):** Switching $$+1$$ to $$-1$$ ($$x^2 - dy^2 = -1$$) turns an always-solvable equation into a subtle mystery governed by local modular obstructions and the 2-torsion of class groups—culminating in Koymans and Pagano’s 2022 proof of **Stevenhagen’s conjecture**.

---

## 1. A poem that is not a folk riddle

Write $$W,B,Y,D$$ for the numbers of white, black, yellow, and dappled **bulls**, and $$w,b,y,d$$ for the corresponding **cows**. Archimedes’ seven ratio conditions are linear:

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

Eight positive-integer unknowns and seven independent linear equations leave a **one-parameter family**. The smallest positive integer solution gives a total herd of

$$
W+B+Y+D+w+b+y+d = 50{,}389{,}082
$$

(with $$W=10{,}366{,}482$$, $$B=7{,}460{,}514$$, $$Y=4{,}149{,}387$$, $$D=7{,}358{,}060$$). Big for a school exercise, yet still fits comfortably on one line.

Then the poem adds two **geometric** constraints:

$$
W+B = m^2, \qquad D+Y = \frac{n(n+1)}{2}
$$

for positive integers $$m,n$$ (a square and a triangular number). Plugging the linear family into those two conditions collapses the entire riddle into one Pell equation—in unreduced form

$$
x^2 - 410{,}286{,}423{,}278{,}424\, y^2 = 1,
$$

and after stripping square factors,

$$
u^2 - 4{,}729{,}494\, v^2 = 1.
$$

**Status.** Archimedes’ cattle problem is **completely solved**—not an open conjecture. Its drama lies in the astronomical size of its smallest solution and the elegant algebra that produces it.

---

## 2. The Pell equation, misnamed

For a positive nonsquare integer $$d$$, **Pell’s equation** is

$$
x^2 - d y^2 = 1, \qquad x,y\in\mathbb{Z}.
$$

Beyond the trivial solution $$(\pm 1, 0)$$, **Joseph-Louis Lagrange** (1768) proved that a nontrivial positive solution *always* exists for every nonsquare $$d > 0$$, and that there is a smallest positive **fundamental solution** $$(x_1, y_1)$$ from which all other positive solutions are generated.

**Historical note:** Leonhard Euler accidentally attributed the equation to English mathematician John Pell, who had almost nothing to do with it. In Europe, Pierre de Fermat posed it as a challenge and William Brouncker solved it; centuries earlier in India, **Brahmagupta** (628 CE) and **Bhāskara II** (12th century, *cakravāla* method) had already built powerful algorithms for it.

---

## 3. Brahmagupta’s composition: multiplying solutions

If $$x_1^2 - dy_1^2 = k_1$$ and $$x_2^2 - dy_2^2 = k_2$$, then Brahmagupta’s identity says:

$$
(x_1x_2 + d y_1y_2)^2 - d(x_1y_2 + x_2y_1)^2 = k_1k_2.
$$

Why does this magic identity work? Factor inside the ring $$\mathbb{Z}[\sqrt{d}]$$:

$$
(x_1 + y_1\sqrt{d})(x_2 + y_2\sqrt{d}) = (x_1x_2 + dy_1y_2) + (x_1y_2 + x_2y_1)\sqrt{d}.
$$

Taking the algebraic norm $$N(x+y\sqrt{d}) = x^2 - dy^2$$ multiplies norms: $$N(\alpha\beta) = N(\alpha)N(\beta)$$. Thus solutions of $$x^2 - dy^2 = 1$$ are **units of norm $$+1$$**!

### Worked example 1: Generating solutions for $$d=3$$ by hand

For $$x^2 - 3y^2 = 1$$, spot the fundamental solution by inspection: $$(x_1, y_1) = (2, 1)$$, since $$2^2 - 3(1)^2 = 4 - 3 = 1$$. Now square the unit $$2 + \sqrt{3}$$:

$$
(2 + \sqrt{3})^2 = (4 + 3) + (2 + 2)\sqrt{3} = 7 + 4\sqrt{3}.
$$

Check $$(7, 4)$$: $$7^2 - 3(4)^2 = 49 - 48 = 1$$! Multiply again by $$2+\sqrt{3}$$:

$$
(7 + 4\sqrt{3})(2 + \sqrt{3}) = (14 + 12) + (7 + 8)\sqrt{3} = 26 + 15\sqrt{3},
$$

and sure enough, $$26^2 - 3(15)^2 = 676 - 675 = 1$$! One solution automatically unlocks an infinite ladder of solutions.

---

## 4. Finding the first solution: continued fractions for $$d=2$$ and $$d=7$$

For $$d=2$$, expanding $$\sqrt{2} = [1;\overline{2}]$$ gives convergents $$p_0/q_0 = 1/1$$ ($$1^2 - 2\cdot 1^2 = -1$$) and $$p_1/q_1 = 3/2$$ ($$3^2 - 2\cdot 2^2 = +1$$). Thus $$(3,2)$$ is the fundamental solution of $$x^2 - 2y^2 = 1$$, and powers of $$3+2\sqrt{2}$$ generate $$(3,2), (17,12), (99,70), (577,408), \ldots$$

![Integer points on the hyperbola x² − 2y² = 1]({{ site.baseurl }}/img/chapter_img/pell_hyperbola_d2_toankho.png)

*Figure. The hyperbola $$x^2-2y^2=1$$ and its integer points. The table of solutions is correct. The boxed formula $$x+y\sqrt{2}=(1+\sqrt{2})^n$$ is **not**: $$1+\sqrt{2}$$ has norm $$-1$$, so odd powers solve $$x^2-2y^2=-1$$. The $$+1$$ solutions are the even powers, equivalently $$(x+y\sqrt{2})=(3+2\sqrt{2})^n=(1+\sqrt{2})^{2n}$$. (Source illustration: [Toán Khó](https://toankho.com/2026/08/07/bai-toan-dan-bo-cua-archimedes-va-phuong-trinh-pell/); AI-generated.)*

### Worked example 2: Cracking $$x^2 - 7y^2 = 1$$ via the continued fraction of $$\sqrt{7}$$

What if the fundamental solution isn’t obvious at a glance? Run the continued-fraction algorithm on $$\sqrt{7} \approx 2.64575$$:
1. $$a_0 = \lfloor \sqrt{7}\rfloor = 2$$, remainder $$\sqrt{7}-2$$.
2. Invert: $$\frac{1}{\sqrt{7}-2} = \frac{\sqrt{7}+2}{3} \approx 1.548 \implies a_1 = 1$$, remainder $$\frac{\sqrt{7}-1}{3}$$.
3. Invert: $$\frac{3}{\sqrt{7}-1} = \frac{\sqrt{7}+1}{2} \approx 1.823 \implies a_2 = 1$$, remainder $$\frac{\sqrt{7}-1}{2}$$.
4. Invert: $$\frac{2}{\sqrt{7}-1} = \frac{\sqrt{7}+1}{3} \approx 1.215 \implies a_3 = 1$$, remainder $$\frac{\sqrt{7}-2}{3}$$.
5. Invert: $$\frac{3}{\sqrt{7}-2} = \sqrt{7}+2 \approx 4.645 \implies a_4 = 4$$, and the remainder cycles back to $$\sqrt{7}-2$$!

So $$\sqrt{7} = [2; \overline{1, 1, 1, 4}]$$ (period length $$4$$). Build the convergents $$p_n/q_n$$ using $$p_n = a_n p_{n-1} + p_{n-2}$$ and $$q_n = a_n q_{n-1} + q_{n-2}$$:

| $$n$$ | $$a_n$$ | Convergent $$p_n/q_n$$ | $$p_n^2 - 7q_n^2$$ |
| :--- | :--- | :--- | :--- |
| $$0$$ | $$2$$ | $$2/1$$ | $$4 - 7 = -3$$ |
| $$1$$ | $$1$$ | $$3/1$$ | $$9 - 7 = +2$$ |
| $$2$$ | $$1$$ | $$5/2$$ | $$25 - 28 = -3$$ |
| $$3$$ | $$1$$ | $$8/3$$ | $$64 - 63 = +1$$ |

Right before the period closes ($$n = 3$$), out pops the exact fundamental solution **$$(x_1, y_1) = (8, 3)$$**! Square $$8 + 3\sqrt{7}$$ via Brahmagupta composition to get the next solution instantly:

$$
(8 + 3\sqrt{7})^2 = (64 + 63) + 48\sqrt{7} = 127 + 48\sqrt{7} \implies 127^2 - 7(48)^2 = 16{,}129 - 16{,}128 = 1.
$$

---

## 5. Why the numbers explode: $$d=60$$ vs. $$d=61$$

Nothing in the innocent formula $$x^2 - dy^2 = 1$$ warns you how long the continued-fraction period of $$\sqrt{d}$$ will be—and the size of $$x_1$$ grows *exponentially* with that period (governed by the **regulator** $$\ln(x_1 + y_1\sqrt{d})$$).

Compare two neighbors right next to each other:
- **$$d = 60$$:** The fundamental solution is tiny—$$(x_1, y_1) = (31, 4)$$, since $$31^2 - 60(4)^2 = 961 - 960 = 1$$.
- **$$d = 61$$** (Fermat’s famous 1657 challenge): The period of $$\sqrt{61}$$ stretches to 11 terms, and the smallest positive solution explodes to ten digits:
  $$
  x_1 = 1{,}766{,}319{,}049, \qquad y_1 = 226{,}153{,}980.
  $$

Archimedes’ cattle problem ($$d = 4{,}729{,}494$$) is the exact same explosion on a grand stage. In 1880, Carl Amthor calculated that the smallest total herd is

$$
\approx 7.760271 \times 10^{206544},
$$

a **206,545-digit** integer! Modern computers (Williams–German–Zarnke 1965; Nelson 1981) printed all 206,545 digits—exhibiting explicitly what Lagrange’s theorem had already guaranteed to exist.

![Popular poster for the cattle/Pell story]({{ site.baseurl }}/img/chapter_img/pell_digit_explosion_toankho.png)

*Figure. A popular poster from the source article. The digit count **206,545** is the size of Archimedes’ smallest full herd. The poster’s claim that this count belongs to $$d=226$$ is **false**—the reduced cattle discriminant is $$4{,}729{,}494$$. Use the picture as an exercise in reading popular math critically, not as a data source. (AI-generated illustration, Toán Khó.)*

---

## 6. What is proved, what is subtler: the negative Pell equation

Switching the right-hand side from $$+1$$ to $$-1$$ gives the **negative Pell equation** $$x^2 - dy^2 = -1$$. Unlike $$+1$$, this does *not* always have a solution!

Check **$$d = 3$$** modulo 3:

$$
x^2 - 3y^2 = -1 \implies x^2 \equiv -1 \equiv 2 \pmod 3.
$$

Yet every integer square modulo 3 is either $$0^2 \equiv 0$$ or $$(\pm 1)^2 \equiv 1$$—never $$2$$! That one-line **local modular obstruction** proves $$x^2 - 3y^2 = -1$$ has zero integer solutions (and the same argument rules out any $$d$$ divisible by a prime $$p \equiv 3 \pmod 4$$). Even when no local obstruction exists (like $$d = 34 = 2\cdot 17$$), global arithmetic obstructions can still block a solution!

| Claim | Status |
| :--- | :--- |
| $$x^2-dy^2=1$$ has infinitely many solutions for every nonsquare $$d>0$$ | **Theorem** (Lagrange 1768) |
| A fundamental solution can be read from the continued fraction of $$\sqrt{d}$$ | **Theorem** |
| Archimedes’ cattle problem has a (gigantic) positive solution | **Solved** (existence 19th c.; full digits 20th c.) |
| $$x^2-dy^2=-1$$ is solvable for every such $$d$$ | **False** (local and global obstructions) |
| Among Stevenhagen’s eligible square-free $$d$$, the density of those for which $$-1$$ is solvable | **Theorem** (Stevenhagen’s conjecture, 1993; proved by Koymans–Pagano, 2022, [arXiv:2201.13424](https://arxiv.org/abs/2201.13424)). The constant is $$\approx 58.06\%$$, **not** “58% of all $$d$$.” |

**Do not overclaim applications.** Real-quadratic units (Pell) and imaginary-quadratic **class groups** (used in CSIDH and some class-group VDFs) live in neighboring parts of algebraic number theory, but they are not the same object. Pell is not a post-quantum cryptosystem.

---

### Explanation: Why a Simple Quadratic Equation Hides 206,545-Digit Giants

How can an equation with two variables and exponent 2 hide solutions bigger than the universe—yet remain 100% solvable by a mechanical algorithm? Trace the four-step engine slowly:

1. **Rewrite integer solutions as algebraic units.** Factoring $$x^2 - dy^2 = (x+y\sqrt{d})(x-y\sqrt{d}) = 1$$ reveals that solutions multiply cleanly inside $$\mathbb{Z}[\sqrt{d}]$$: finding *one* fundamental solution $$(x_1,y_1)$$ immediately generates all infinitely many via $$(x_1 + y_1\sqrt{d})^n$$.
2. **Translate the equation into rational approximation.** Dividing by $$y^2$$ gives $$\frac{x}{y} - \sqrt{d} = \frac{1}{y(x+y\sqrt{d})}$$, forcing $$x/y$$ to be an exceptionally close rational approximation—which must appear among the convergents of the periodic continued fraction of $$\sqrt{d}$$.
3. **Watch period length drive exponential growth.** Each step of the continued fraction multiplies $$p_n, q_n$$ roughly geometrically. A short period ($$d=60$$) gives $$(31,4)$$; a long period ($$d=61$$ or $$d=4{,}729{,}494$$) explodes to 10 or 206,545 digits.
4. **Distinguish $$+1$$ from $$-1$$.** Squaring a $$-1$$ solution always yields a $$+1$$ solution, so $$+1$$ *always* succeeds; reaching $$-1$$ requires an odd continued-fraction period and faces both local modular obstructions (like mod 3) and deep class-group obstructions.

**Quick check.** Using the exact same modulo-3 trick we used for $$d=3$$, explain in one sentence why $$x^2 - 7y^2 = -1$$ has no integer solutions. *(Hint: reduce the equation modulo 7—or modulo 4! Check squares modulo 4: $$x^2 \equiv 0, 1 \pmod 4$$, while $$7y^2 - 1 \equiv 3y^2 - 1 \pmod 4$$.)*

---

## Common misconceptions

| Claim | Verdict | Correction |
| :--- | :--- | :--- |
| “Pell invented the Pell equation.” | **Fail** | Euler’s misattribution; see Brouncker / Brahmagupta / Bhāskara. |
| “The cattle poem is a few-thousand-head puzzle.” | **Fail** | Linear part: $$\sim 5\times 10^7$$. Full problem: $$206{,}545$$ digits. |
| “$$1+\sqrt{2}$$ generates the $$+1$$ solutions for $$d=2$$.” | **Fail** | It generates the **norm $$-1$$** solutions; square it to get $$3+2\sqrt{2}$$. |
| “Stevenhagen says 58% of all $$d$$ work for $$-1$$.” | **Fail** | Density inside a specified eligible family (no prime factor $$\equiv 3\pmod 4$$), not among all square-free $$d$$. |
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
