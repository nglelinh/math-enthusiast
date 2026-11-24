---
layout: post
title: "Zelmanov and the Restricted Burnside Problem (Fields Medal 1994)"
chapter: '02'
order: 31
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Imagine a bizarre Rubik’s cube with only $$d = 2$$ basic twists, $$a$$ and $$b$$, obeying one ironclad law: *no matter what sequence of moves $$x$$ you compose*, repeating $$x$$ exactly $$n$$ times brings the cube back to its starting state ($$x^n = 1$$). Intuition insists that under such a tight rule, the total number of reachable cube configurations must be finite. In 1902, **William Burnside** posed that exact question for group theory—and over the next century, it triggered some of the wildest plot twists in modern algebra.

Plot twist number one: that intuition is **false**. Even when a single exponent $$n$$ is fixed for every element, there exist **infinite** two-generator groups in which every element satisfies $$x^n = 1$$ (constructed by Golod–Shafarevich, and for bounded exponents by Novikov–Adian, Ol’shanskii, Ivanov, and Lysënok). Yet amid this jungle of infinite monsters, algebraists in the 1930s asked a sharper question—named by Wilhelm Magnus the **restricted Burnside problem**: if we look *only* at **finite** $$d$$-generated groups of exponent $$n$$, can their orders grow arbitrarily large, or are they all trapped under one universal ceiling depending only on $$(d, n)$$?

In 1990–1991, through a breathtaking translation from group theory into **Lie algebras** and **Jordan algebras**, **Efim Zelmanov** proved the answer is **YES** for every $$d$$ and every $$n$$—earning the **Fields Medal 1994**:

> “For the solution of the restricted Burnside problem.”  
> — [IMU, Fields Medals 1994](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994)

That single adjective **restricted** is the entire pedagogical heart of this lesson: keeping three distinct Burnside problems from collapsing into one slogan, seeing why Zelmanov’s positive theorem lives peacefully beside the infinite groups of Novikov–Adian, and watching how Lie and Jordan algebras conquer a century-old problem about finite groups.

**Lesson roadmap:** Background Knowledge Map (three Burnside problems, linearizing a group into a Lie algebra, Jordan algebras) → Hand-verifiable worked examples: proving $$\vert B(d,2)\vert = 2^d$$ in two lines and building $$B(2,3)$$ of order $$27$$ with its Engel-2 identity → Deep-Dive Explanation (Read Slowly): the 4-step path from Hall–Higman and Kostrikin to Zelmanov (1990–1991) → Summary table and why this won the 1994 Fields Medal.

---

## Learning objectives

After this lecture you should be able to:

- Distinguish cleanly among **three Burnside problems**: the **general** problem (periodic, no uniform exponent), the **bounded Burnside problem** (free Burnside group $$B(d,n)$$ of fixed exponent $$n$$), and the **restricted Burnside problem** (bounding the size of *finite* $$d$$-generated groups of exponent $$n$$).
- Prove by hand that $$B(d,2)$$ is elementary abelian of order $$2^d$$, and explain via $$3\times 3$$ matrices over $$\mathbb{F}_3$$ how $$x^3 = 1$$ produces an Engel-type Lie bracket identity.
- Explain why $$B(d,n)$$ can be **infinite** while its largest finite quotient $$B_0(d,n)$$ remains **finite**.
- Credit the key milestones accurately: **Golod–Shafarevich**, **Novikov–Adian**, **Ol’shanskii**, and **Ivanov–Lysënok** (infinite counterexamples); **Hall–Higman** (reduction to prime powers); **Kostrikin** (prime exponent $$p$$); and **Zelmanov** (all exponents $$n$$).
- Describe Zelmanov’s method: pass from groups to associated **Lie rings / Lie algebras**, then deploy **Jordan-algebra** structure theory to prove nilpotence.

**Prerequisites.** Groups given by generators and relations; the difference between “every element has finite order” and “there is a uniform $$n$$ with $$x^n=1$$”; the idea of a Lie algebra as a bilinear bracket with Jacobi and $$[x,x]=0$$. No prior combinatorial group theory is assumed.

**Seminar links.** A classical question that split into several theorems, and medal hype that drops the word “restricted.” Pair with other “one named problem, several meanings” portraits in this chapter, and with the Abel-side culture of long structural programs in [Chapter 8]({{ site.baseurl }}/contents/en/chapter08/).

---

## Background Knowledge Map: Burnside Groups, Lie Algebras, and Jordan Algebras

### 1. Three Burnside problems—never conflate them
- **General Burnside problem (1902):** Must every finitely generated periodic group (where each $$x$$ has its own finite order $$n_x$$) be finite? $$\Rightarrow$$ **NO** (Golod–Shafarevich, 1964).
- **Bounded Burnside problem:** Is the **free Burnside group** $$B(d,n)$$ (the largest $$d$$-generated group satisfying $$x^n = 1$$ for all $$x$$) finite? $$\Rightarrow$$ **YES** for $$n = 2, 3, 4, 6$$; **NO** for many large exponents (Novikov–Adian 1968 for odd $$n > 4381$$, later lowered to $$665$$; Ol’shanskii’s Tarski monsters; Ivanov 1994 and Lysënok 1996 for large even $$n$$); and still **OPEN** for small cases like $$B(2,5)$$!
- **Restricted Burnside problem (1930s):** Among **finite** $$d$$-generated groups of exponent $$n$$, is there a uniform bound on their order—equivalently, is the largest finite quotient $$B_0(d,n)$$ finite? $$\Rightarrow$$ **YES, for all $$d$$ and $$n$$** (Kostrikin for prime $$n = p$$; **Zelmanov 1990–1991** for all $$n$$).

### 2. Why an infinite $$B(d,n)$$ does not contradict a finite $$B_0(d,n)$$
An infinite group can have very few—or even no—finite quotients! For instance, an infinite simple group has no nontrivial finite-index normal subgroups at all, so its largest finite quotient has order $$1$$. Likewise, inside an infinite $$B(d,n)$$, the intersection of all finite-index normal subgroups (its finite residual) is enormous and infinite, while the maximal finite quotient $$B_0(d,n)$$ sits cleanly on top with finite order.

### 3. Linearizing a group into a Lie algebra—and where Jordan algebras enter
By filtering a group $$G$$ along its lower central series $$G = G_1 \supseteq G_2 \supseteq \cdots$$ ($$G_{k+1} = [G_k, G]$$), we turn a nonabelian group into a **graded Lie algebra** $$L(G) = \bigoplus_{k \ge 1} G_k/G_{k+1}$$, with the Lie bracket induced by the group commutator $$[g,h] = g^{-1}h^{-1}gh$$. The group law $$x^n = 1$$ translates into an **Engel identity** $$(\mathrm{ad}\,x)^m = 0$$ inside $$L(G)$$. Remarkably, special elements inside such Lie algebras—**sandwich elements** satisfying $$(\mathrm{ad}\,a)^2 = 0$$—naturally carry the structure of a **Jordan algebra** (a nonassociative algebra with symmetric product $$A \circ B = \frac{1}{2}(AB + BA)$$).

---

## 1. Worked Examples by Hand: Proving $$\vert B(d,2)\vert = 2^d$$ and Exploring $$B(2,3)$$ of Order $$27$$

### Example 1: Exponent $$n = 2$$ — a two-line proof that $$B(d,2)$$ is finite
Suppose every element $$x$$ in a group $$G$$ satisfies $$x^2 = 1$$ (so $$x = x^{-1}$$). Pick any two elements $$a, b \in G$$:

$$
(ab)^2 = 1 \;\Longrightarrow\; ab = (ab)^{-1} = b^{-1}a^{-1} = ba.
$$

The group $$G$$ is automatically **abelian**! Since the $$d$$ generators $$x_1, \ldots, x_d$$ commute and each can only appear to power $$0$$ or $$1$$, every element of $$B(d,2)$$ has the unique form $$x_1^{\varepsilon_1}\cdots x_d^{\varepsilon_d}$$ ($$\varepsilon_i \in \{0,1\}$$), giving:

$$
\vert B(d, 2) \vert = 2^d.
$$

### Example 2: Exponent $$n = 3$$ — commutativity breaks, and the Lie bracket appears
Consider $$B(2,3)$$, generated by $$a, b$$ subject to $$x^3 = 1$$ for every element $$x$$. Is it abelian? **No!** Look at the Heisenberg group of $$3 \times 3$$ unitriangular matrices over $$\mathbb{F}_3$$:

$$
M(u, v, w) = \begin{pmatrix} 1 & u & w \\ 0 & 1 & v \\ 0 & 0 & 1 \end{pmatrix}, \qquad u, v, w \in \mathbb{F}_3.
$$

There are exactly $$3^3 = 27$$ matrices, generated by $$a = M(1,0,0)$$ and $$b = M(0,1,0)$$, and you can cube any matrix by hand in seconds:

$$
M(u, v, w)^3 = \begin{pmatrix} 1 & 3u & 3w + 3uv \\ 0 & 1 & 3v \\ 0 & 0 & 1 \end{pmatrix} \equiv \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \pmod{3}.
$$

Check the commutators: $$c = [a,b] = M(0,0,1) \neq I$$, yet the triple commutators vanish: $$[c,a] = [[a,b],a] = I$$ and $$[c,b] = [[a,b],b] = I$$!
Burnside (1902) and Levi–van der Waerden proved that this exact 27-element group *is* all of $$B(2,3)$$. Now look at $$[[a,b],a] = 1$$ inside the associated Lie algebra $$L(G)$$ over $$\mathbb{F}_3$$: it becomes the **Engel-2 identity**:

$$
(\mathrm{ad}\,x)^2(y) = [[y, x], x] = 0 \quad \forall x, y \in L(G).
$$

This tiny 27-element matrix group exposes the entire strategy of the Russian algebra school: instead of wrestling with long words in a group, translate $$x^{p^k} = 1$$ into an Engel-type identity in $$L(G)$$ and prove that $$L(G)$$ must be nilpotent.

---

## 2. Deep-Dive Explanation: The 4-Step Road from Hall–Higman and Kostrikin to Zelmanov (Read Slowly)

As Walter Feit noted in his 1994 ICM laudation, the restricted Burnside problem is *"to a large extent a problem in Lie algebras."* Here is how the 60-year-old fortress finally fell:

#### Step 1: The Hall–Higman reduction (1956) — reduce any exponent $$n$$ to prime powers $$p^k$$
Factor $$n = p_1^{k_1}\cdots p_r^{k_r}$$. **Philip Hall and Graham Higman (1956)** proved a deep structural reduction—made unconditional once the **Classification of Finite Simple Groups** was completed in the early 1980s: the restricted Burnside problem holds for exponent $$n$$ **if and only if** it holds for every **prime-power** factor $$p_i^{k_i}$$.

#### Step 2: Kostrikin’s breakthrough (1959) — conquering prime exponent $$n = p$$
For a finite $$p$$-group $$G$$ of prime exponent $$p$$, **Alexei Kostrikin** showed that the associated Lie algebra $$L(G)$$ over $$\mathbb{F}_p$$ satisfies the $$(p-1)$$-Engel identity $$(\mathrm{ad}\,x)^{p-1} = 0$$. Using his **sandwich method** (hunting for nonzero elements $$a$$ with $$(\mathrm{ad}\,a)^2 = 0$$), he proved that every $$d$$-generated Lie algebra over $$\mathbb{F}_p$$ satisfying the $$(p-1)$$-Engel identity is **nilpotent** of bounded class—settling the restricted Burnside problem for all prime exponents $$p$$ (recounted in his classic book *Around Burnside*).

#### Step 3: The $$p^k$$ wall ($$k \ge 2$$) and Zelmanov’s Jordan-algebra breakthrough (1990–1991)
For thirty years after Kostrikin, even $$n = p^2$$ blocked every attack. For a prime power $$p^k$$, the associated Lie algebra $$L(G)$$ (built from the Jennings–Zassenhaus $$p$$-series) satisfies an Engel condition only on **homogeneous** elements—not on arbitrary linear combinations—plus a weaker polynomial identity.
In two landmark papers—**1990** for **odd** prime powers (*Izv. Akad. Nauk SSSR*, English *Math. USSR-Izv.* 36) and **1991** for **$$2$$-groups** (*Mat. Sb.*, English *Math. USSR-Sb.* 72, the hardest case because characteristic $$2$$ breaks standard linearization tricks)—**Efim Zelmanov** unleashed the full machinery he had built in his earlier career on **infinite-dimensional Jordan algebras** (including Glennie’s identity and special Jordan structures) to control sandwich elements and prove the core theorem: *every $$d$$-generated Lie algebra over $$\mathbb{F}_p$$ satisfying a polynomial identity and a linearized Engel condition on homogeneous elements is **nilpotent**.*

#### Step 4: Translate Lie nilpotency back to a uniform bound on $$\vert G \vert$$
Because $$L(G)$$ is nilpotent of class at most $$c(d, p^k)$$, its dimension over $$\mathbb{F}_p$$ is bounded by a constant $$N(d, p^k)$$, forcing the order of any finite $$d$$-generated group $$G$$ of exponent $$p^k$$ to satisfy $$\vert G \vert \le p^{N(d, p^k)}$$. Combined with Step 1, the restricted Burnside problem is solved completely for **all $$d$$ and all $$n$$**.

Summary of Zelmanov’s algebraic translation chain:

$$
\text{Finite group } G\ (x^n=1)
\;\xrightarrow{\text{Hall–Higman}}\;
p\text{-group } (x^{p^k}=1)
\;\xrightarrow{\text{Jennings–Zassenhaus}}\;
\text{Lie algebra } L(G)
\;\xrightarrow{\text{Jordan algebras (Zelmanov)}}\;
L(G) \text{ nilpotent} \implies \vert G\vert \le C(d,n).
$$

---

## 3. Summary Table and Why It Won the 1994 Fields Medal

The theorem gives a **uniform bound** (though effective bounds are astronomical); it does not list the finite groups or decide open bounded cases like $$B(2,5)$$.

| Question | Answer |
|----------|--------|
| Are all finitely generated periodic groups finite? | **No** (Golod–Shafarevich, 1964). |
| Are all $$B(d,n)$$ finite? | **No** for many large $$n$$ (Novikov–Adian, Ol’shanskii, Ivanov, Lysënok); **yes** for $$n = 2, 3, 4, 6$$; some small cases like $$B(2,5)$$ remain **open**. |
| Are there only finitely many *finite* $$d$$-generated groups of exponent $$n$$? | **Yes**, for all $$d,n$$ (Kostrikin for $$n=p$$; **Zelmanov** in general). |

**Why the Fields Medal 1994:** In a subject famous for bizarre infinite counterexamples (like Ol’shanskii’s Tarski monsters), the restricted Burnside problem was the last great finiteness question one could still hope to answer affirmatively. Zelmanov closed it by deepening structural Lie and Jordan algebra rather than small-cancellation geometry—representing the pure-algebra face of the 1994 Zürich congress alongside Bourgain, Lions, and Yoccoz.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Zelmanov solved the Burnside problem.” | He solved the **restricted** Burnside problem. The unrestricted/bounded problems have negative answers in general. |
| “All groups of finite exponent are finite.” | False: $$B(d,n)$$ is infinite for many $$n$$. |
| “Golod–Shafarevich already settled everything.” | They killed the *general* (not uniformly bounded) problem. Restricted Burnside is about finite groups of fixed exponent. |
| “Kostrikin did the whole restricted problem.” | Kostrikin: **prime** exponent. Zelmanov: odd exponents and $$2$$-groups, hence all $$n$$. |
| “Restricted means ‘easier, so groups are finite.’” | Restricted means “ask only about **finite** groups.” The free Burnside group may still be infinite. |
| “The proof is purely group-theoretic combinatorics.” | The engine is **Lie rings / Lie algebras**, with Jordan-algebraic background. |

---

## Links

- IMU Fields Medals 1994: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994)
- Wikipedia: [Efim Zelmanov](https://en.wikipedia.org/wiki/Efim_Zelmanov); [Burnside problem](https://en.wikipedia.org/wiki/Burnside_problem)
- arXiv search: [Zelmanov restricted Burnside](https://arxiv.org/search/?query=Zelmanov+restricted+Burnside&searchtype=all)
- MacTutor history page on the Burnside problem (linked from the Wikipedia article)

---

## References

1. International Mathematical Union, Fields Medals 1994 citation for Efim Zelmanov (Feit, ICM Zürich 1994 laudation).
2. **E. I. Zelmanov**, “Solution of the restricted Burnside problem for groups of odd exponent,” *Math. USSR-Izv.* 36 (1991), 41–60.
3. **E. I. Zelmanov**, “A solution of the restricted Burnside problem for $$2$$-groups,” *Math. USSR-Sb.* 72 (1992), 543–565.
4. **A. I. Kostrikin**, *Around Burnside*, Springer, 1990 (prime-exponent case).
5. **W. Burnside**, “On an unsettled question in the theory of discontinuous groups,” *Quart. J. Pure Appl. Math.* 33 (1902), 230–238.
6. Wikipedia, [Efim Zelmanov](https://en.wikipedia.org/wiki/Efim_Zelmanov) and [Burnside problem](https://en.wikipedia.org/wiki/Burnside_problem) (Novikov–Adian, Golod–Shafarevich, Ol’shanskii, Ivanov, Lysënok).

---

## Further directions

- Read a survey page on why large odd exponents make $$B(d,n)$$ infinite (small cancellation), then return to the Lie-ring machine; note that $$B(2,5)$$ remains a famous open bounded case.
- Seminar prompt: if effective bounds are huge, what is the theorem *for*?

## Video tham khảo

- **xem trước** — [Why Do People Hate Mathematics? Efim Zelmanov (Fields Medal 1994)](https://www.youtube.com/watch?v=Nz3_RzZzuO8) — Tom Rocks Maths, English. Watch first for Zelmanov on mathematical taste around the 1994 medal. This is an interview, not a proof of the restricted Burnside problem developed in the lesson.
