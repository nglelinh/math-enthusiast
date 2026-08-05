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

This page is a **studio**, not a theorem dump. Duality is a principle with many faces. Your job is to **pick one dual pair**, draw a two-column dictionary, label **theorem vs conjecture**, and keep a short research log. You will not prove AdS/CFT or HMS. You will practice the craft that makes those programs readable.

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

## 1. Background (one page)

A duality dictionary is a table:

| Side A | Side B | Status label |
|--------|--------|--------------|
| object / statement | dual object / statement | theorem / … |

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

## Exercises (seminar exit ticket)

1. In one sentence: what did your dual pair **swap**?  
2. Name one dictionary row that is a **theorem** and one that is only a **program**.  
3. Give an example of a popular claim that confuses symmetry with duality.  
4. **≤100 words:** Why does status labeling protect you from overclaiming?

---

## References

1. Course duality track — Ch.6 lessons 12–17.  
2. nLab — duality (orientation only).  
3. Your log is the primary artifact.
