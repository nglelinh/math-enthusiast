---
layout: post
title: "Geometric Langlands & S-Duality (Deep Dive)"
chapter: '06'
order: 15
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
lesson_type: deep-dive
---

**Geometric Langlands** is a duality program in pure mathematics: categories of sheaves on the moduli of $$G$$-bundles on a curve correspond to spectral / local-system data for the **Langlands dual group** $$G^\vee$$. Independently, physicists developed **S-duality** (electric–magnetic / strong–weak duality) for four-dimensional supersymmetric gauge theory, which also swaps $$G$$ with $$G^\vee$$. **Kapustin–Witten (2006)** proposed that geometric Langlands is the mathematical shadow of S-duality of a twisted $$\mathcal N=4$$ super Yang–Mills theory compactified on a Riemann surface—with **mirror symmetry of Hitchin systems** as a geometric engine.

This deep dive sits at the junction of:

- [Duality as a principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/)  
- [Langlands / Ngô]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/) (arithmetic program; dual group)  
- [Mirror symmetry]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/) (Hitchin SYZ culture)

**Do not** confuse Ngô’s Fundamental Lemma with “Langlands finished,” or physics dictionaries with complete proofs of every geometric correspondence.

Pack: `research/video-research/geometric-langlands-sduality/`.

---

## Learning objectives

After this lecture you should be able to:

- Separate **arithmetic** Langlands from **geometric** Langlands (objects and base fields differ; dual-group spirit is shared).
- State geometric Langlands at slogan level: sheaves on $$\mathrm{Bun}_G(C)$$ ↔ spectral data for $$G^\vee$$.
- Explain **S-duality** of $$\mathcal N=4$$ SYM as strong/weak and $$G\leftrightarrow G^\vee$$.
- Sketch the **Kapustin–Witten** compactification picture (4d theory on $$C\times \Sigma$$ → 2d sigma models / brane categories).
- Relate **Hitchin systems** for $$G$$ and $$G^\vee$$ to mirror symmetry.
- Keep status honest and credit physics as **bridge and muse**, not as automatic proof.

**Prerequisites.** Duality principle; Ch.2 Langlands overview. Reductive groups and moduli stacks appear as names first.

---

## 1. Two Langlands worlds

| | Arithmetic Langlands | Geometric Langlands |
|--|----------------------|---------------------|
| Base | Number fields / adeles | Algebraic curves (often over $$\mathbb{C}$$) |
| Automorphic side | Automorphic representations of $$G(\mathbb{A})$$ | Sheaves / D-modules on $$\mathrm{Bun}_G(C)$$ |
| Galois / spectral side | Galois representations | Local systems / Higgs / spectral covers for $$G^\vee$$ |
| Dual group | $$G^\vee$$ | $$G^\vee$$ |
| Famous tools | Trace formula, endoscopy, $$L$$-functions | Hecke eigensheaves, derived categories, Hitchin |

**Ngô’s Fields work** unlocks the Fundamental Lemma for **endoscopic comparison** in the arithmetic/trace-formula machine—it is *not* a proof of the full geometric correspondence, and *not* “the Langlands program done.”

---

## 2. Geometric Langlands slogan

Fix a smooth projective curve $$C$$ and a reductive group $$G$$. Roughly:

> Categories of (suitable) sheaves on the moduli stack $$\mathrm{Bun}_G(C)$$ of $$G$$-bundles on $$C$$ are dual to categories built from $$G^\vee$$-local systems (or related spectral data) on $$C$$.

A classical form emphasizes **Hecke eigensheaves**: sheaves that are eigenvectors for Hecke operators with eigenvalues given by a local system for $$G^\vee$$. Modern formulations use derived algebraic geometry and more refined categorical equivalences; statements evolve with the literature.

**Pedagogy.** Memorize the **shape**—automorphic geometry of $$G$$ dual to spectral geometry of $$G^\vee$$—not a full stack-theoretic definition.

---

## 3. S-duality in gauge theory

**Maxwell** theory already has an electric–magnetic duality ($$E\leftrightarrow B$$, charges ↔ monopoles in extended settings). **Montonen–Olive** and later work promote this to nonabelian **S-duality**: strong coupling maps to weak coupling of a dual theory, and the gauge group is replaced by the **Langlands dual** $$G^\vee$$ (e.g. $$\mathrm{SU}(n)$$ dual related to $$\mathrm{SU}(n)/\mathbb{Z}_n$$ structures—details group-dependent).

For $$\mathcal N=4$$ super Yang–Mills in four dimensions, S-duality is especially sharp: the coupling $$\tau$$ transforms under $$\mathrm{SL}(2,\mathbb{Z})$$-type actions, and dual theories share the same BPS spectrum in controlled ways.

---

## 4. Kapustin–Witten bridge

**Kapustin–Witten** (arXiv:hep-th/0604151) argue, roughly:

1. Start with a topologically twisted version of 4d $$\mathcal N=4$$ SYM with gauge group $$G$$.  
2. Compactify on a Riemann surface $$C$$ (the curve of geometric Langlands).  
3. The effective theory involves sigma models on moduli of Higgs bundles / Hitchin moduli—and **categories of branes** on those spaces.  
4. **S-duality** of the 4d theory becomes a duality of those 2d categories, matching the geometric Langlands correspondence for $$G$$ and $$G^\vee$$.  
5. Along the way, **mirror symmetry** of Hitchin systems (A-branes ↔ B-branes) appears as the geometric engine—linking this lesson to the mirror deep dive.

**Literacy.** This is a **physics-derived dictionary and motivation** that reshaped mathematical research agendas. It is not a substitute for pure mathematical proofs of geometric Langlands statements.

---

## 5. Hitchin systems as mirrors

The **Hitchin fibration** presents the moduli of Higgs bundles as an integrable system over a base of characteristic polynomials. For Langlands dual groups $$G$$ and $$G^\vee$$, fibers are dual abelian varieties (generically)—a **SYZ-type mirror** pair (Hausel–Thaddeus and related work). Thus:

```text
S-duality (4d gauge)
    ↓ compactify
Mirror symmetry of Hitchin systems
    ↓ categories of branes
Geometric Langlands correspondence
```

That diagram is the seminar heart of the Kapustin–Witten culture.

---

## 6. Status map (2026)

| Statement | Label |
|-----------|--------|
| Dual group organizes arithmetic & geometric programs | Established design principle |
| Fundamental Lemma (Ngô et al.) | **Theorem** (arithmetic endoscopy tool) |
| Geometric Langlands (various formulations) | Major advances; still a living program |
| Kapustin–Witten dictionary | Influential; physics ↔ math bridge |
| Full arithmetic Langlands functoriality | Largely **open** |

---

## 7. Course landscape

| Lesson | Link |
|--------|------|
| [Langlands / Ngô]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/) | Arithmetic program + Fundamental Lemma |
| [Duality principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/) | Parent map |
| [Mirror symmetry]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/) | HMS / SYZ; Hitchin mirrors |
| [AdS/CFT]({{ site.baseurl }}/contents/en/chapter06/06_14_AdS_CFT/) | Different duality (holography) |
| [Atiyah–Singer]({{ site.baseurl }}/contents/en/chapter08/08_11_Atiyah_Singer_Index/) | Index / characteristic classes (cousin culture) |
| [Uhlenbeck]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/) | Gauge analysis infrastructure |

---

## 8. Confusions

| Claim | Correction |
|-------|------------|
| “Geometric = arithmetic Langlands.” | Shared dual-group spirit; different mathematical objects. |
| “Ngô proved geometric Langlands.” | Ngô: Fundamental Lemma for endoscopy / trace formula. |
| “Physics proved Langlands.” | Physics supplies S-duality dictionaries; math proves math statements. |
| “S-duality is only string theory.” | Lives in QFT ($$\mathcal N=4$$ SYM) before full strings. |
| “Hitchin = already HMS for all CY.” | Hitchin mirrors are a key special geometric family. |

---

## Exercises

1. Two columns: arithmetic vs geometric Langlands—base, objects, dual group.  
2. State geometric Langlands in ≤3 sentences.  
3. What does S-duality swap (coupling and group)?  
4. Sketch Kapustin–Witten compactification in 4 bullet points.  
5. Why do Hitchin systems for $$G$$ and $$G^\vee$$ matter for mirror symmetry?  
6. **≤150 words:** Why is “bridge, not proof” the right slogan for physics → geometric Langlands?  
7. **Optional:** Open Kapustin–Witten abstract and list five keywords.

---

## Video sources (research pack)

Pack: `research/video-research/geometric-langlands-sduality/`.

1. **Core** — Kapustin, EM duality and geometric Langlands: [https://www.youtube.com/watch?v=oJRD3PshFjY](https://www.youtube.com/watch?v=oJRD3PshFjY)  
2. **Core** — Gukov, Geometric Langlands and S-duality: [https://www.youtube.com/watch?v=bCpVL6flCxo](https://www.youtube.com/watch?v=bCpVL6flCxo)  
3. **Orientation** — Frenkel, Gauge Theory, Geometric Langlands: [https://www.youtube.com/watch?v=8Pkw25J-Bg0](https://www.youtube.com/watch?v=8Pkw25J-Bg0)  
4. **Bridge** — Witten, Mirror & Geometric Langlands: [https://www.youtube.com/watch?v=S02ghGCdNDo](https://www.youtube.com/watch?v=S02ghGCdNDo)  

Full URLs: `research/video-research/geometric-langlands-sduality/references.md`.

---

## References

1. Kapustin–Witten — Electric-Magnetic Duality and the Geometric Langlands Program — https://arxiv.org/abs/hep-th/0604151  
2. Frenkel — Lectures on the Langlands Program and CFT — https://arxiv.org/abs/hep-th/0512172  
3. Gukov–Witten — Gauge theory, ramification, geometric Langlands — https://arxiv.org/abs/hep-th/0612073  
4. Hausel–Thaddeus — Mirror symmetry, Langlands duality, Hitchin — https://arxiv.org/abs/math/0205236  
5. Course: [Langlands / Ngô]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/)  
6. Pack: `research/video-research/geometric-langlands-sduality/`  
