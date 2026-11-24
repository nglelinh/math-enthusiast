---
layout: post
title: "Studio: Draw a Duality Dictionary"
chapter: '07'
order: 10
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

> **Learning path — Duality track (studio step)**  
> **1.** [Duality as a principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/)  
> **2.** Optional deep dive: Mirror / AdS–CFT / Geometric Langlands  
> **3. You are here:** Ch.7 studio — **draw one dictionary**  
> *Time guide:* ~90–150 min notebook work (not a proof course).

In 1799, a French expedition in Egypt unearthed the Rosetta Stone. Because the exact same decree was carved in two different scripts, scholars finally unlocked ancient hieroglyphs that had been mute for over a millennium. In modern mathematics and theoretical physics, the grandest Rosetta Stones are called **dualities**: two theories that look like they inhabit completely unrelated worlds, yet describe the exact same underlying reality—so that a brutal calculation on one side turns into a gentle algebraic step on the other.

You do not need to prove AdS/CFT or Homological Mirror Symmetry in an afternoon. Instead, this studio invites you to work as a **lexicographer**: pick one dual pair, construct a clean two-column translation table, label honestly which rows are rock-solid **theorems** and which are **research programs** or **physics dictionaries**, and keep a log that records even the rows you had to revise.

**Lesson roadmap:** Background Knowledge Map (linear duality, Fourier duality & 21st-century duality programs) → Sample dictionary & master pairs table → Deep-Dive Explanation (Read Slowly): hand-verifying two classic dualities (matrix transpose $$f^*$$ and size-4 DFT circular convolution) → Studio tasks & log.

---

## Learning objectives

After this studio you should be able to:

- Choose one dual pair from the course map and state **what is swapped**.
- Produce a **two-column dictionary** (≥6 rows) of corresponding objects or slogans.
- Mark each major claim as **theorem / program / conjecture / physics dictionary / analogy**.
- Separate **ordinary symmetry of one theory** from **equivalence of two theories**.
- Keep a dated log with at least one failed or revised dictionary row.

**Prerequisites.** [Duality as a principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/). Deep dives optional.

---

## Background Knowledge Map: What Is Duality in Mathematics and Theoretical Physics?

If you took undergraduate linear algebra or signal processing, you have already used duality without necessarily calling it by name. Three escalating levels bridge undergrad math to frontier research:

### 1. Algebraic and Topological Duality ($$V \leftrightarrow V^*$$ and Poincaré Duality)

In **linear algebra**, duality pairs a vector space $$V$$ with its space of linear measurements $$V^* = \mathrm{Hom}(V, \mathbb{R})$$ (column vectors ↔ row vectors), and the matrix transpose $$A \mapsto A^T$$ reverses arrows across the bridge. In **algebraic topology**, **Poincaré duality** pairs $$k$$-dimensional holes with $$(n-k)$$-dimensional holes on a closed orientable $$n$$-manifold ($$H^k(M) \cong H_{n-k}(M)$$).

### 2. Analytic Duality (Fourier and Pontryagin)

The Fourier transform translates signals between *time* and *frequency*. Here duality shows its real superpower: heavy time-domain operations like **convolution** $$(f*g)(t)$$ and **differentiation** $$f'(t)$$ collapse into simple **pointwise multiplication** $$\hat f(\xi)\hat g(\xi)$$ and $$2\pi i \xi \hat f(\xi)$$ on the frequency side!

### 3. Twenty-First-Century Duality Programs (and Symmetry vs. Duality)

At the frontier, duality powers entire research landscapes: **Mirror Symmetry** connects symplectic geometry (measuring areas, counting curves) to complex algebraic geometry; **AdS/CFT** connects gravity in $$(d+1)$$-dimensional bulk space to a quantum field theory without gravity on its $$d$$-dimensional boundary; and the **Langlands Program** links number theory (Galois representations) to harmonic analysis (automorphic forms).

**Key distinction:** A **symmetry** maps a theory back to *itself* (like rotating a square by $$90^\circ$$). A **duality** bridges *two different descriptions* (often swapping strong coupling with weak coupling) that produce identical mathematical or physical answers.

---

## 1. Background (one page)

A duality dictionary is a table:

| Side A | Side B | Status label |
|--------|--------|--------------|
| object / statement | dual object / statement | theorem / … |

Here is a compact model using **Fourier duality on $$\mathbb{R}$$**:

| Side A (Time domain $$x$$) | Side B (Frequency domain $$\xi$$) | Status label |
|----------------------------|-----------------------------------|--------------|
| Signal $$f(x)$$ | Spectrum $$\hat f(\xi)$$ | Definition |
| Derivative $$f'(x)$$ | Multiplication by $$2\pi i \xi \hat f(\xi)$$ | Theorem (rapidly decaying functions) |
| Convolution $$(f*g)(x)$$ | Pointwise product $$\hat f(\xi)\hat g(\xi)$$ | Convolution theorem |
| Narrow pulse in time | Wide spread in frequency | Theorem (Uncertainty principle) |

#### Deep-Dive Explanation (Read Slowly): Hand-Verifying Two Classic Dualities (Transpose $$f^*$$ and Size-4 DFT)

Verify by hand that "translating from Side A to Side B" produces exact, checkable numbers:

**Example 1 — Proving the dual map $$f^*$$ has matrix $$A^T$$:**
Take the linear map $$f: \mathbb{R}^2 \to \mathbb{R}^2$$ given by $$f(x, y) = (x + 2y,\; 3x)$$, with matrix $$A = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$$.
Any linear functional $$\alpha \in (\mathbb{R}^2)^*$$ has the form $$\alpha(u, v) = c_1 u + c_2 v$$ (coordinate vector $$(c_1, c_2)$$). Its dual pullback $$(f^*\alpha)(x, y) := \alpha\bigl(f(x, y)\bigr)$$ is:
$$
(f^*\alpha)(x, y) = c_1(x + 2y) + c_2(3x) = (c_1 + 3c_2)\,x + (2c_1)\,y.
$$
Reading off the new coefficients gives $$(c_1 + 3c_2,\; 2c_1) = \begin{pmatrix} 1 & 3 \\ 2 & 0 \end{pmatrix}\begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$—the matrix of $$f^*$$ is literally **$$A^T$$**!

**Example 2 — Circular convolution ↔ Pointwise product on a 4-point DFT:**
Let $$x = (1, 1, 0, 0)$$ and $$y = (1, 0, 1, 0)$$ on $$\mathbb{Z}/4\mathbb{Z}$$.
- **Side A (Direct circular convolution):** $$(x * y)_m = \sum_{j=0}^{3} x_j y_{(m-j)\bmod 4}$$ gives:
  - $$m=0$$: $$1\cdot 1 + 1\cdot 0 = 1$$; $$m=1$$: $$1\cdot 0 + 1\cdot 1 = 1$$; $$m=2$$: $$1\cdot 1 + 1\cdot 0 = 1$$; $$m=3$$: $$1\cdot 0 + 1\cdot 1 = 1$$.
  Result: $$x * y = (1, 1, 1, 1)$$.
- **Side B (4-point DFT $$\hat u_k = \sum_{j=0}^{3} u_j (-i)^{jk}$$):**
  - $$\hat x = (2,\; 1-i,\; 0,\; 1+i)$$,
  - $$\hat y = (2,\; 0,\; 2,\; 0)$$.
  Multiply entry by entry: $$\hat x \odot \hat y = (4,\; 0,\; 0,\; 0)$$. Take the inverse DFT $$\frac{1}{4}\sum_{k=0}^{3} (\hat x \odot \hat y)_k\, i^{mk} = \frac{1}{4}(4, 4, 4, 4) = (1, 1, 1, 1)$$—**an exact match!**

Examples already in the course:

| Pair | Swap (slogan) | Status caution |
|------|---------------|----------------|
| Dual space $$V$$ / $$V^*$$ | vectors ↔ linear measurements | Theorem (linear algebra) |
| Fourier / Pontryagin | position ↔ frequency / characters | Theorem (LCA groups) |
| Poincaré duality | degree $$k$$ ↔ $$n-k$$ | Theorem (suitable manifolds) |
| Electric–magnetic | $$E\leftrightarrow B$$, charges ↔ monopoles | Maxwell: classical; Yang–Mills S-duality: program |
| Mirror A / B | symplectic ↔ complex | HMS: program + theorem islands |
| AdS / CFT | bulk gravity ↔ boundary QFT | Research correspondence |
| Langlands $$G$$ / $$G^\vee$$ | automorphic ↔ Galois / spectral | Vast program; lemmas are theorems |

**Rule of the studio.** If you cannot label the status, you do not yet understand the claim—look it up in the parent lesson, do not invent certainty.

---

## 2. Conjecture vs proof vs dictionary

| Label | Use when |
|-------|----------|
| **Theorem** | Proved under stated hypotheses (cite course lesson or standard name) |
| **Program / conjecture** | Open or partially proved web of statements |
| **Physics dictionary** | Standard in theoretical physics; math status may differ |
| **Analogy** | Pedagogical only—do not promote to theorem |

Success is **not** “prove Kapustin–Witten.” Success is an auditable notebook.

---

## 3. Studio tasks

### Task A — Choose a pair (15 min)

Pick **exactly one** primary pair from §1 table (or a carefully named variant, e.g. “RSA trapdoor vs factoring” is **not** a duality—reject category errors).

Write three sentences: (1) what lives on side A; (2) what lives on side B; (3) what is *not* claimed.

### Task B — Draw the dictionary (45–75 min)

Build a table with **≥6 rows**. At least two rows must be **objects**; at least two must be **questions or computations** that become easier after the dual.

Hand-drawn is fine. Photograph and embed in your log if required by the syllabus.

### Task C — Status audit (20 min)

For every row, add a status label. Flag one row you are **least sure** about and write what evidence would upgrade it.

### Task D — Mini-experiment (optional but recommended, 20–40 min)

Do **one**:

1. **Linear dual.** For $$V=\mathbb{R}^2$$, write bases of $$V$$ and $$V^*$$; dualize the map $$f(x,y)=(x+y,x)$$.  
2. **Fourier toy.** Discrete Fourier on $$\mathbb{Z}/n\mathbb{Z}$$: note that convolution ↔ pointwise product (state, do not prove full theory).  
3. **EM cartoon.** Write vacuum Maxwell equations and indicate the $$E\leftrightarrow B$$ symmetry (heuristic).  
4. **Langlands hygiene.** Two columns: arithmetic Langlands vs geometric Langlands (objects only)—cite Ch.2 + geometric deep dive.

### Task E — Research log (≥5 dated entries)

Intent → action → result → label → next step. Include at least one **revision** (a row you deleted or rewrote).

---

## 4. Deliverable checklist

| Item | Required |
|------|----------|
| Chosen dual pair + three-sentence scope | Yes |
| Dictionary ≥6 rows with status labels | Yes |
| Log ≥5 entries including one failure/revision | Yes |
| One paragraph: “symmetry ≠ theory equivalence” | Yes |
| Optional experiment from Task D | Strongly recommended |
| Claim you did **not** prove | Yes (explicit sentence) |

**Non-goals:** prove RH-type dualities, “solve” AdS/CFT, or assert “physics proved Langlands.”

---

## 5. Course links

| Resource | Role |
|----------|------|
| [Duality principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/) | Parent map |
| [Pontryagin / Fourier dual]({{ site.baseurl }}/contents/en/chapter06/06_16_Pontryagin_Fourier_Duality/) | Undergrad bridge |
| [Mirror]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/) | Deep dive option |
| [AdS/CFT]({{ site.baseurl }}/contents/en/chapter06/06_14_AdS_CFT/) | Deep dive option |
| [Geometric Langlands]({{ site.baseurl }}/contents/en/chapter06/06_15_Geometric_Langlands_SDuality/) | Deep dive option |
| [Witten mini]({{ site.baseurl }}/contents/en/chapter06/06_17_Witten_Physics_Math/) | Physics→math culture |

---

## References

1. Course duality track — Ch.6 lessons 12–17.  
2. nLab — duality (orientation only).  
3. Your log is the primary artifact.

## Video tham khảo

- **xem trước** — [Prof. Edward Witten | Duality, the Langlands Correspondence, and the Influence of Michael Atiyah](https://www.youtube.com/watch?v=fqHGe3acpC0) — INI Seminar Room 1, English. Watch first. “Prof. Edward Witten | Duality, the Langlands Correspondence, and the Influence of Micha…” orients the lesson’s aim: Choose one dual pair from the course map and state what is swapped.
- [AdS/CFT Correspondence, Part 1 - Juan Maldacena](https://www.youtube.com/watch?v=sYqtGXN59uE) — Institute for Advanced Study, English. A second pass once the main claim is in view: Choose one dual pair from the course map and state what is swapped.
- [Lecture 1: Geometric Langlands and S-duality in N = 4 SYM by Sergei Gukov](https://www.youtube.com/watch?v=bCpVL6flCxo) — International Centre for Theoretical Sciences, English. Further depth after the first two, still tied to this lesson: Choose one dual pair from the course map and state what is swapped.
