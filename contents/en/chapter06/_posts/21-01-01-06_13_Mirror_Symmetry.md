---
layout: post
title: "Mirror Symmetry (Deep Dive)"
chapter: '06'
order: 13
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
lesson_type: deep-dive
---

In 1991, four string theorists (Candelas, de la Ossa, Green, and Parkes) published a table of numbers that stunned algebraic geometers. For decades, mathematicians had struggled to count rational curves of degree $$d$$ lying on a quintic Calabi–Yau threefold: $$2{,}875$$ lines in degree 1, $$609{,}250$$ conics in degree 2, and a grueling computer calculation in degree 3 (which even had a bug before being corrected to $$317{,}206{,}375$$). The four physicists never counted a single curve—they solved a classical differential equation on a *completely different* manifold and read off the entire infinite sequence for every degree $$d = 1, 2, 3, 4, \dots$$ at once!

That shockwave launched **Mirror Symmetry**. Born as a string-theory surprise—two topologically different Calabi–Yau spaces yielding the exact same physical theory—it blossomed into two landmark mathematical programs: Kontsevich’s **Homological Mirror Symmetry (HMS)** and the **Strominger–Yau–Zaslow (SYZ)** geometric picture. This deep dive expands [Duality as a principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/), giving you the conceptual machinery without requiring you to prove HMS or build mirrors by hand.

Pack: `research/video-research/mirror-symmetry/`.

---

## Background Knowledge Map: What Is Mirror Symmetry and What Does It Study?

To grasp what mirror symmetry actually links, separate two kinds of geometry usually taught in different rooms:

1. **Symplectic Geometry (A-Model — measuring *areas* and trajectories):** Born in Hamiltonian mechanics (position–momentum phase space), it carries an oriented area form $$\omega$$ rather than rigid lengths. Its signature questions—counting pseudoholomorphic curves (Gromov–Witten invariants) and Lagrangian intersections (Fukaya categories)—are notoriously hard to compute directly.
2. **Complex / Algebraic Geometry (B-Model — measuring *shapes* and polynomial equations):** Studies manifolds cut out by holomorphic or polynomial equations, where we vary *complex shape* continuously and compute classical period integrals via differential equations.

**Mirror symmetry** states that many Calabi–Yau manifolds come in pairs $$(X, \check X)$$ whose **symplectic geometry (A-side) on $$X$$ matches the complex geometry (B-side) on $$\check X$$**, and vice versa—turning brutal curve-counting problems into classical integrals.

---

## Learning objectives

After this lecture you should be able to:

- State the **physics slogan** of mirror symmetry and the **mathematical** A-model / B-model split.
- Explain the **Hodge diamond** intuition (numbers of complex structure vs Kähler moduli swap roles).
- Distinguish **SYZ** (geometric T-duality of torus fibrations) from **HMS** (categorical equivalence).
- Label status honestly: theorem islands vs open programs (**as of 2026**).
- Connect mirror symmetry to T-duality and to geometric Langlands / Hitchin duals at slogan level.
- Avoid claiming “string theory proved all of algebraic geometry.”

**Prerequisites.** Duality principle lesson; comfort with “complex manifold” and “symplectic form” as names. Derived categories and Floer theory appear as slogans only.

---

## 1. Where the idea came from

In the late 1980s–90s, string compactifications on Calabi–Yau threefolds predicted that certain **worldsheet** theories labeled by different geometries gave matching correlation functions. The matching suggested a **mirror map**: complex structure moduli of $$X$$ pair with Kähler moduli of a dual $$\check X$$, and vice versa. Enumerative counts of holomorphic curves on one side matched period integrals / variation of Hodge structure on the other—astonishing computational leverage.

Mathematics asked: *what theorem is hiding under the physics dictionary?* Two answers dominate modern culture.

---

## 2. A-model and B-model (the two faces)

| Face | Geometry emphasized | Typical data |
|------|---------------------|--------------|
| **A-model** | Symplectic structure of $$X$$ | Pseudoholomorphic curves; Gromov–Witten invariants; **Fukaya category** of Lagrangian submanifolds with Floer data |
| **B-model** | Complex structure of $$\check X$$ | Holomorphic bundles / coherent sheaves; **derived category** $$D^b\mathrm{Coh}(\check X)$$; period integrals |

Mirror symmetry claims (in refined forms) that A-data of $$X$$ equals B-data of $$\check X$$. That is a **duality of geometries**, not a continuous symmetry of one manifold.

**Calabi–Yau slogan (enough for this course).** A complex manifold with trivial canonical bundle (physics usually also wants a Ricci-flat Kähler metric). Mirror partners need not be diffeomorphic; they need matching dual data.

---

## 3. Hodge numbers and enumerative leverage

For Calabi–Yau threefolds, mirror symmetry classically swaps Hodge numbers in a characteristic pattern (e.g. $$h^{1,1}(X)$$ with $$h^{2,1}(\check X)$$ in the simplest pictures)—the famous **Hodge diamond flip**. More deeply, **genus-zero Gromov–Witten** generating functions on one side match **Yukawa couplings / periods** on the other after a mirror map of coordinates.

**Pedagogy.** You do not need to compute a single GW invariant here. You need the **shape**: hard curve counts ↔ integrals of holomorphic forms after a change of variables.

---

## 4. SYZ — mirror symmetry as T-duality

**Strominger–Yau–Zaslow (1996)** proposed a geometric mechanism: both $$X$$ and $$\check X$$ should fiber over a common base by **special Lagrangian** tori, with mirror fibers dual tori (T-duality fiberwise). Singular fibers encode crucial monodromy and discriminant data.

| SYZ strength | SYZ hardness |
|--------------|--------------|
| Explains *why* mirrors exist as dual torus bundles | Smooth special-Lagrangian fibrations are extremely hard to construct globally |
| Links to physics T-duality | Needs refined (often algebro-geometric) formulations—Gross–Siebert and others |

**Status.** SYZ is a **research program**, not a single closed theorem for general CY manifolds. Local and toric cases are better understood; global smooth pictures remain delicate.

---

### Deep-Dive Explanation: Checking Mirror Symmetry on a 2D Torus and the Hodge Diamond by Hand (Read Slowly)

Six-real-dimensional Calabi–Yau threefolds are impossible to picture directly. Fortunately, a **complex 1-dimensional** Calabi–Yau manifold is completely familiar: a flat **2D torus** (an elliptic curve $$E$$), built by gluing opposite edges of a rectangle of dimensions $$L_1 \times L_2$$.

1. **Swapping area (A-side) and shape (B-side) on a 2D torus:**
   On the rectangle $$L_1 \times L_2$$, the two fundamental geometric moduli are:
   - **Symplectic / Kähler parameter** (measuring *area*): $$\rho = i\,A = i\,L_1 L_2$$.
   - **Complex structure parameter** (measuring *aspect ratio / shape*): $$\tau = i\,\frac{L_2}{L_1}$$.

   Now apply **T-duality (the SYZ mechanism)** to the first circle: keep $$L_2$$ fixed and invert $$L_1 \mapsto \check L_1 = \frac{1}{L_1}$$! Compute both parameters of the mirror torus $$\check E$$ by hand:
   - New area parameter: $$\check\rho = i\,\check L_1 L_2 = i\,\frac{L_2}{L_1} = \tau$$.
   - New shape parameter: $$\check\tau = i\,\frac{L_2}{\check L_1} = i\,L_1 L_2 = \rho$$.

   **Concrete numerical check:** Take a $$2 \times 6$$ rectangle: area $$A = 12$$, aspect ratio $$6/2 = 3$$. Invert $$2 \mapsto 1/2$$ to get a $$\tfrac{1}{2} \times 6$$ mirror rectangle: its new area is $$\tfrac{1}{2}\cdot 6 = 3$$, and its new aspect ratio is $$6/(1/2) = 12$$! A single reciprocal **swaps area and shape cleanly ($$\rho \leftrightarrow \tau$$)**.

2. **Checking the Euler characteristic flip on a Calabi–Yau threefold:**
   For any Calabi–Yau threefold, the topological Euler characteristic is determined by its two unfixed Hodge numbers:
   $$
   \chi(X) = 2\bigl(h^{1,1}(X) - h^{2,1}(X)\bigr).
   $$
   For the quintic threefold $$X \subset \mathbb{P}^4$$, $$h^{1,1}(X) = 1$$ and $$h^{2,1}(X) = 101$$, so $$\chi(X) = 2(1 - 101) = -200$$. Its mirror $$\check X$$ swaps the two numbers to $$h^{1,1}(\check X) = 101,\ h^{2,1}(\check X) = 1$$, giving $$\chi(\check X) = 2(101 - 1) = +200$$. Because their Euler characteristics have opposite signs, $$X$$ and $$\check X$$ are **not even topologically homeomorphic**—mirror symmetry genuinely bridges two distinct geometries.

## 5. Homological mirror symmetry (Kontsevich)

**Kontsevich (1994)** upgraded enumerative matching to a categorical statement—**homological mirror symmetry (HMS)**:

$$
D^\pi\mathrm{Fuk}(X)\;\simeq\; D^b\mathrm{Coh}(\check X)
$$

(precise variants: Karoubi completion, Landau–Ginzburg models, wrapped Fukaya categories, etc.). Objects on the A-side are (roughly) Lagrangians with local systems; morphisms are Floer cohomologies. Objects on the B-side are complexes of coherent sheaves; morphisms are Ext groups.

**Why this is a duality principle.** Entire **homological algebras** match, so every theorem expressible in one derived category has a dual twin. Special cases (elliptic curves, toric Fanos, some local CY, certain hypersurfaces) are **proved**; the general conjecture remains open.

---

## 6. Status map (do not skip)

| Statement | Label (2026) |
|-----------|----------------|
| Many enumerative dualities / mirror maps for specific families | Theorem / established |
| HMS for large classes of examples | Theorem islands |
| Full HMS for general CY | Open program |
| Global smooth SYZ fibrations | Open / refined programs |
| Physics-inspired predictions | Muse + dictionary; math must still prove |

---

## 7. Bridges in this course

| Neighbor | Link |
|----------|------|
| [Duality principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/) | Parent map |
| [AdS/CFT]({{ site.baseurl }}/contents/en/chapter06/06_14_AdS_CFT/) | Another physical duality culture (holography, not CY mirrors) |
| [Geometric Langlands & S-duality]({{ site.baseurl }}/contents/en/chapter06/06_15_Geometric_Langlands_SDuality/) | Hitchin systems for $$G$$ and $$G^\vee$$ are SYZ-style mirrors |
| [Mathematical physics]({{ site.baseurl }}/contents/en/chapter06/06_11_Mathematical_Physics/) | Gauge / string interfaces |
| [Pardon / symplectic]({{ site.baseurl }}/contents/en/chapter02/02_13_Pardon_Symplectic/) | Symplectic geometry culture (different focus) |

---

## 8. Confusions

| Claim | Correction |
|-------|------------|
| “Mirror = same manifold written twice.” | Partners can be topologically different; dual *data* match. |
| “HMS is just Hodge numbers.” | Hodge is classical shadow; HMS is categorical. |
| “SYZ is proved in full.” | Program with partial results. |
| “T-duality = mirror always.” | SYZ proposes T-duality as mechanism; not every dual statement is a circle compactification. |
| “Physics already finished the math.” | Physics supplies dictionaries; proofs are mathematical. |

---

## Mode C — reconstructed notes from flagship video

*Reconstructed from auto-captions of Witten (Fields Medal Symposium 2012). Captions: `research/video-research/mirror-symmetry/transcripts/`. Units: `knowledge_units_mode_c.json`. Reconstruct; do not paste ASR.*

### C1. Why geometric Langlands “wants” four dimensions

Witten’s orientation bridges **mirror symmetry** language with **geometric Langlands**. A QFT in dimension $$d$$ naturally assigns a **category of boundary conditions** to a closed $$(d-2)$$-manifold. Geometric Langlands assigns categories to a **Riemann surface** (2-manifold), so the matching dimension is $$d=4$$: start from a four-dimensional theory.

### C2. $$\mathcal N=4$$ SYM as the natural theory

Among 4d gauge theories, the one with maximal supersymmetry—**$$\mathcal N=4$$ super Yang–Mills**—is the natural host. The gauge group $$G$$ (compact Lie group in physics packaging) and its dual enter through dualities; supersymmetric “odd symmetries” supply differentials that package the categorical structures mathematicians study.

### C3. Mirror + Hitchin culture (not a proof)

The talk mixes **mirror symmetry** (branes, dual geometries) with **Hitchin / moduli of bundles** data that feed geometric Langlands. For this course: treat as **research climate and dictionary**—not a board proof of full HMS or full geometric Langlands. Pair with [Geometric Langlands & S-duality]({{ site.baseurl }}/contents/en/chapter06/06_15_Geometric_Langlands_SDuality/) and [Witten mini]({{ site.baseurl }}/contents/en/chapter06/06_17_Witten_Physics_Math/).

### C4. Caption hygiene

- **Witten `S02ghGCdNDo`:** EN auto-captions extracted (2026-08-05).  
- **Chan HMS/SYZ `Kz6Dj8KSFjM`:** no subtitles available—watch for visuals only; do not invent Mode-C from missing ASR.

---

## Video sources (research pack)

Use for **orientation**, not as substitute for surveys. Pack: `research/video-research/mirror-symmetry/`.

1. **Orientation / Mode C** — Witten, Mirror Symmetry & Geometric Langlands: [https://www.youtube.com/watch?v=S02ghGCdNDo](https://www.youtube.com/watch?v=S02ghGCdNDo) · captions in pack  
2. **Core research talk (no captions)** — Chan, HMS via SYZ: [https://www.youtube.com/watch?v=Kz6Dj8KSFjM](https://www.youtube.com/watch?v=Kz6Dj8KSFjM)  
3. **Research** — Zaslow, Lagrangian fillings: [https://www.youtube.com/watch?v=Y3-sw3tjZiU](https://www.youtube.com/watch?v=Y3-sw3tjZiU)  
4. **Notes** — MIT OCW Mirror Symmetry: [https://ocw.mit.edu/courses/18-969-topics-in-geometry-mirror-symmetry-spring-2009/](https://ocw.mit.edu/courses/18-969-topics-in-geometry-mirror-symmetry-spring-2009/)  

Full URL list: `research/video-research/mirror-symmetry/references.md`.  
Transcript status: `research/video-research/mirror-symmetry/TRANSCRIPT_STATUS.md`.

---

## References

1. Kontsevich — Homological algebra of mirror symmetry — https://arxiv.org/abs/alg-geom/9411018  
2. Strominger–Yau–Zaslow — Mirror symmetry is T-duality — https://arxiv.org/abs/hep-th/9606040  
3. Gross — SYZ survey — https://arxiv.org/abs/1212.4220  
4. Auroux — Beginner’s Fukaya categories — https://arxiv.org/abs/1301.7056  
5. Hori et al. — *Mirror Symmetry* (Clay monograph)  
6. Wikipedia — Homological mirror symmetry; SYZ conjecture  
7. Pack folder: `research/video-research/mirror-symmetry/`  

## Video tham khảo

- **xem trước** — [Edward Witten: Mirror Symmetry & Geometric Langlands (2012)](https://www.youtube.com/watch?v=S02ghGCdNDo) — Graduate Mathematics, English. Watch first. “Edward Witten: Mirror Symmetry & Geometric Langlands (2012)” orients the lesson’s aim: State the physics slogan of mirror symmetry and the mathematical A-model / B-model split.
- [HMS for local CY manifolds via SYZ | Kwokwai Chan](https://www.youtube.com/watch?v=Kz6Dj8KSFjM) — Harvard CMSA, English. A second pass once the main claim is in view: State the physics slogan of mirror symmetry and the mathematical A-model / B-model split.
- [Lagrangian fillings what does the sheaf say? | Eric Zaslow](https://www.youtube.com/watch?v=Y3-sw3tjZiU) — Harvard CMSA, English. Further depth after the first two, still tied to this lesson: State the physics slogan of mirror symmetry and the mathematical A-model / B-model split.
