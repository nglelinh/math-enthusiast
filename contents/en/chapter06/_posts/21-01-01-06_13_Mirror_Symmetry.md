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

**Mirror symmetry** began as a string-theory surprise: two Calabi–Yau spaces that look different as complex and symplectic geometries can produce the **same physical predictions**. Mathematics absorbed the surprise and turned it into two major programs—**homological mirror symmetry (HMS)** and the **Strominger–Yau–Zaslow (SYZ)** geometric picture—plus a web of enumerative dualities. This deep dive expands the slogan in [Duality as a principle]({{ site.baseurl }}/contents/en/chapter06/06_12_Duality_Principle/); it does **not** prove HMS or construct mirrors by hand.

**Path:** physics origin → A/B models → Hodge / enumerative flip → SYZ as T-duality geometry → HMS (Kontsevich) → status map → bridges to Langlands → exercises.

Pack: `research/video-research/mirror-symmetry/`.

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

## Exercises

1. In one paragraph, contrast A-model and B-model data.  
2. What does the Hodge diamond flip buy computationally?  
3. State SYZ in ≤3 sentences; name one difficulty.  
4. Write the HMS slogan as an equivalence of categories (informal OK).  
5. **≤150 words:** Why is mirror symmetry a *duality* in the sense of the parent lesson?  
6. Status literacy: list one theorematic island and one open program.  
7. **Optional:** Skim Auroux’s Fukaya intro abstract and list three words new to you.

---

## Video sources (research pack)

Use for **orientation**, not as substitute for surveys. Pack: `research/video-research/mirror-symmetry/`.

1. **Orientation** — Witten, Mirror Symmetry & Geometric Langlands: [https://www.youtube.com/watch?v=S02ghGCdNDo](https://www.youtube.com/watch?v=S02ghGCdNDo)  
2. **Core research talk** — Chan, HMS via SYZ: [https://www.youtube.com/watch?v=Kz6Dj8KSFjM](https://www.youtube.com/watch?v=Kz6Dj8KSFjM)  
3. **Research** — Zaslow, Lagrangian fillings: [https://www.youtube.com/watch?v=Y3-sw3tjZiU](https://www.youtube.com/watch?v=Y3-sw3tjZiU)  
4. **Notes** — MIT OCW Mirror Symmetry: [https://ocw.mit.edu/courses/18-969-topics-in-geometry-mirror-symmetry-spring-2009/](https://ocw.mit.edu/courses/18-969-topics-in-geometry-mirror-symmetry-spring-2009/)  

Full URL list: `research/video-research/mirror-symmetry/references.md`.

---

## References

1. Kontsevich — Homological algebra of mirror symmetry — https://arxiv.org/abs/alg-geom/9411018  
2. Strominger–Yau–Zaslow — Mirror symmetry is T-duality — https://arxiv.org/abs/hep-th/9606040  
3. Gross — SYZ survey — https://arxiv.org/abs/1212.4220  
4. Auroux — Beginner’s Fukaya categories — https://arxiv.org/abs/1301.7056  
5. Hori et al. — *Mirror Symmetry* (Clay monograph)  
6. Wikipedia — Homological mirror symmetry; SYZ conjecture  
7. Pack folder: `research/video-research/mirror-symmetry/`  
