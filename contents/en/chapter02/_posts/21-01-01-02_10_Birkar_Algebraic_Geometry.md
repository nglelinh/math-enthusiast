---
layout: post
title: "Birkar’s Work in Algebraic Geometry (Fields Medal 2018)"
chapter: '02'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

**Caucher Birkar** received the **Fields Medal 2018** for his proof of the **boundedness of Fano varieties** and for deep contributions to the **minimal model program (MMP)** in higher-dimensional algebraic geometry. The medal recognizes a program, not a single isolated lemma: birational geometry asks how to organize algebraic varieties of arbitrary dimension the way Riemann surfaces and algebraic surfaces were organized a century earlier—by reducing them, step by step, to models whose geometry is controlled.

This essay is for learners who have seen curves and surfaces in a first algebraic geometry course and want the **architecture** of higher-dimensional classification. It does **not** claim that “all varieties are classified,” nor that Birkar worked alone. It explains slogans carefully: birational equivalence, divisorial contractions and flips, Fano varieties as anticanonical positivity, BAB-type boundedness, and what a Fields-level theorem actually rearranges in the landscape.

---

## Learning objectives

After this lecture you should be able to:

- State the goal of the **minimal model program** in one careful paragraph (reduce birationally toward a minimal model or a Mori fiber space).
- Explain **birational equivalence** as “same dense open set, different compactification,” and why it is weaker than isomorphism.
- Define a **Fano variety** at slogan level: the anticanonical class $$-K_X$$ is ample (positive curvature in a complex-geometric sense).
- Distinguish **existence of flips** from **boundedness of Fanos**—related MMP pillars, different statements.
- Describe higher-dimensional classification as an **architecture of reduction steps**, not a finished encyclopedia of isomorphism types.
- Attribute credit carefully: Birkar’s solo Fano boundedness sits inside a long collaborative network (Cascini, Hacon, McKernan, and many others).

**Prerequisites.** Projective varieties over $$\mathbb{C}$$ (or algebraically closed fields of characteristic zero) at the level of a first course; line bundles and ampleness as “positivity”; the idea that a curve has a genus. No prior MMP required.

**Seminar links.** LO1 / LO4 (hard open-adjacent programs; classical classification ↔ modern reduction tools). Pair with [Beautiful Mathematics]({{ site.baseurl }}/contents/en/chapter04/) for “structure first” aesthetics, and with [Scholze / perfectoid geometry]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/) only as a *different* foundational revolution in algebraic geometry—not the same toolbox.

---

## 1. Why higher dimensions feel different

In complex dimension one, compact Riemann surfaces are classified up to biholomorphism by the **genus** $$g$$: the sphere ($$g=0$$), elliptic curves ($$g=1$$), and higher-genus curves ($$g\ge 2$$) with a moduli space of expected dimension $$3g-3$$. In dimension two, the **Enriques–Kodaira** classification organizes surfaces by Kodaira dimension and a finite list of geometric types (ruled, elliptic, general type, …), after allowing birational modifications and controlled singularities.

From dimension three upward, a naive hope—“list all isomorphism types”—collapses. There are simply too many varieties, and even basic invariants (Hodge numbers, canonical rings) interact with singularities in ways that defeat surface-style tables. The modern answer is not a bigger table. It is a **program**: given a reasonably nice projective variety $$X$$, perform a sequence of **birational operations** that improve the pair $$(X,K_X)$$ until one reaches a model whose canonical class is **nef** (non-negative on curves), or a fibration whose fibers carry positive curvature in a precise sense.

That program is the **minimal model program**. Birkar’s work is one of its central late chapters.

---

## 2. Birational geometry: what you keep and what you forget

Two irreducible varieties $$X$$ and $$Y$$ are **birational** if there exist dense open sets $$U\subset X$$ and $$V\subset Y$$ with an isomorphism $$U\simeq V$$. Equivalently, their function fields are isomorphic. Birational maps may blow up or blow down exceptional loci; they may change the topology of the total space while preserving the “generic” geometry.

What birational equivalence **retains**: the function field; many invariants of the open dense set; in good situations, the plurigenera and the Kodaira dimension

$$
\kappa(X)=\operatorname{trdeg}\Bigl(\bigoplus_{m\ge 0} H^0(X,mK_X)\Bigr)-1
$$

(with the usual conventions when the ring is zero or finite-dimensional).

What it **forgets**: the full isomorphism type; the configuration of exceptional divisors; some singularity data (until one carefully tracks pairs $$(X,\Delta)$$); and, dramatically, the topology of compactifications.

**Slogan for this course.** Classification *up to birational equivalence* is coarser than classification *up to isomorphism*, but it is deep enough to organize higher-dimensional geometry—and it is the only scale at which a global program currently exists.

---

## 3. The minimal model program: goals in one page

Start with a smooth projective variety $$X$$ of dimension $$n$$ (or, more generally, a klt pair $$(X,\Delta)$$). The MMP attempts to **run a directed process**:

1. If the canonical class $$K_X$$ is already **nef**—$$K_X\cdot C\ge 0$$ for every curve $$C$$—stop: one has a **minimal model** (in the smooth case; mild singularities appear in the general theory).
2. If not, the cone theorem of Mori theory produces a curve on which $$K_X$$ is negative. One contracts (or flips) the extremal ray generated by that curve.
3. After finitely many such steps (in good situations), one expects either a minimal model or a **Mori fiber space**: a fibration $$X\to Z$$ whose general fiber is Fano-like ($$-K$$ ample on fibers relative to the base).

In dimension two this story is classical (Castelnuovo contractions, minimal models of surfaces). In dimension three it required the 1980s–1990s theory of flips (Mori and others). In higher dimensions, even the **existence of flips** was a decades-long challenge.

Two kinds of steps appear:

- **Divisorial contraction.** A morphism that contracts a divisor (codimension-one locus) to something smaller. This changes the Picard number by one in a relatively transparent way.
- **Flip.** When the locus one wants to “improve” is small (often codimension $$\ge 2$$ on both sides), there is no morphism that simply contracts a divisor. Instead one replaces a small contraction $$X\to Z$$ by another small birational map $$X^+\to Z$$ so that $$K_{X^+}$$ becomes more positive relative to $$Z$$. Flips are harder because one must **construct** $$X^+$$ and prove it exists with the right singularities.

**Slogan.** Contractions remove excess negative directions by shrinking loci you can see as divisors; flips surgically replace bad small loci when no divisorial contraction is available.

---

## 4. Fano varieties: the positive-curvature generators

A projective variety $$X$$ is **Fano** if the anticanonical line bundle $$-K_X$$ is **ample**. On smooth complex manifolds this is related to positive Ricci curvature (by Yau and others in related contexts); for this course, take ampleness of $$-K_X$$ as the definition.

Fano varieties generate many birational phenomena:

- They appear as **fibers** of Mori fiber spaces.
- They are “positively curved,” so their geometry is expected to be more rigid than that of general type varieties (where $$K_X$$ is positive).
- Families of Fanos control much of the **moduli and boundedness** landscape: if Fanos of fixed dimension are “bounded,” then many moduli problems become finite-type in a precise sense.

**Examples (low dimension).** In dimension one, Fano curves are isomorphic to $$\mathbb{P}^1$$. In dimension two, del Pezzo surfaces form a classical bounded family. In higher dimensions, Fano threefolds were classified by Iskovskikh, Mori, Mukai, and others into finitely many families—already a hint that **boundedness** might be true in general.

---

## 5. Boundedness: the BAB slogan and Birkar’s theorem

A class of varieties is **bounded** if its members appear as fibers of a family of finite type—roughly, only “finitely many continuous parameters and discrete types” are needed. For Fano varieties of fixed dimension, the **Borisov–Alexeev–Borisov (BAB) conjecture** predicted that $$\varepsilon$$-klt Fano varieties of dimension $$n$$ form a bounded family (for each fixed $$n$$ and $$\varepsilon>0$$; precise formulations vary slightly by author and context).

**Birkar’s breakthrough (around 2016, recognized by Fields 2018)** established the boundedness of Fano varieties in the form needed by modern birational geometry: after fixing dimension (and appropriate singularity thresholds), Fano varieties cannot “escape to infinity” through wilder and wilder families. Combined with earlier and concurrent advances on flips and the MMP (including the landmark **Birkar–Cascini–Hacon–McKernan** work on existence of flips and finite generation of canonical rings in broad settings), this supplies structural control over the positive side of the classification architecture.

**What boundedness buys you.**

- It limits the possible Hilbert polynomials and volumes of anticanonical systems in fixed dimension.
- It feeds **moduli** constructions: one cannot build a reasonable moduli space of a class that is unbounded in the worst way.
- It interacts with **complements**, **ACC for log canonical thresholds**, and other MMP pillars that convert local singularity bounds into global finiteness.

**Accuracy.** The 2018 medal citation highlights Birkar’s Fano boundedness and related MMP contributions. Always attribute specific theorems carefully: existence of flips in full generality was a community achievement with Birkar as a central author in key papers; Fano boundedness is the result most tightly attached to his solo late work in public accounts.

---

## 6. Classification architecture—not a finished encyclopedia

It is easy to misread “MMP + boundedness” as “algebraic geometry is finished.” The correct picture is architectural:

| Ingredient | Role |
|------------|------|
| Kodaira dimension $$\kappa$$ | Coarse birational invariant splitting cases |
| Minimal models / Mori fiber spaces | Targets of the reduction process |
| Flips and divisorial contractions | Elementary steps of the process |
| Fano boundedness | Control of the “positive” fibers and many families |
| Canonical rings / finite generation | Algebraic engine behind many existence theorems |
| Singularities (klt, lc, …) | The language in which steps are legal |

What remains open or unfinished includes: effective bounds in many cases; characteristic $$p$$ analogues; full moduli compactifications in high dimension; and countless concrete classifications of special Fano manifolds with extra structure (group actions, Hodge-theoretic constraints, …). Birkar’s theorems rearrange the **global map**; they do not list every variety.

---

## 7. Why a Fields Medal

Three interlocking reasons:

1. **Difficulty.** Higher-dimensional flips and Fano boundedness resisted decades of effort; the proofs combine sophisticated singularity theory, multiplier ideals / discrepancies, and inductive geometry of exceptional loci.
2. **Centrality.** The MMP is the backbone of modern birational geometry. Progress on its foundations reorganizes the field the way a new bridge reorganizes a city—not by painting one building, but by changing what trips are possible.
3. **Clarity of slogan with depth of method.** “Fanos of fixed dimension form a bounded family” is a sentence a graduate student can remember; the proof is a monument of contemporary algebraic geometry.

For this course, Birkar sits next to other Fields stories that complete **programs** rather than settle single numerical conjectures: compare the MMP’s multi-decade arc with, for example, the Langlands-inspired or perfectoid-inspired revolutions elsewhere in Chapter 2—different subjects, similar “architectural” impact.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “All algebraic varieties are Fano.” | Fano is a positivity condition on $$-K$$; most varieties are not Fano. |
| “Birational means isomorphic.” | Birational is weaker; exceptional loci and singularities intervene. |
| “Birkar classified all varieties.” | He proved foundational boundedness / MMP results; classification remains a program. |
| “Flips are the same as blow-downs.” | Flips replace small loci when no divisorial contraction exists; they are not ordinary blow-downs. |
| “Boundedness means only finitely many varieties.” | It means a family of finite type (continuous moduli allowed); not a finite discrete list. |
| “The 2018 medal is only solo work.” | The citation highlights Birkar’s contributions inside a long collaborative MMP network. |

---

## Exercises

1. In your own words: what does birational equivalence **forget** and **retain**? Give one geometric example (e.g. blowing up a point in a surface).
2. Why are **flips** harder than **divisorial contractions**, at slogan level? What fails if you try to “just contract” a small locus?
3. State a one-sentence definition of a **Fano variety**. Check it on $$\mathbb{P}^n$$: why is projective space Fano?
4. Why would **boundedness** of a class of varieties matter for moduli theory? Answer in at most eight sentences.
5. Distinguish carefully: “existence of flips” vs “boundedness of Fanos.” Which is about a process step, and which is about a class of varieties?
6. Skim an ICM or survey exposition of the MMP and list **three milestones before Birkar 2018** (e.g. Mori’s 3-fold flips, BCHM, surface classification).
7. **Accuracy practice.** Find a popular science sentence that says Birkar “classified all shapes.” Rewrite it in two precise sentences suitable for this course.
8. **Seminar stretch.** Compare Enriques–Kodaira surface classification with the higher-dimensional MMP: what becomes a “type” in each story?

---


## Video sources (math-video-researcher pack)

Full ranking: `research/video-research/Birkar_Algebraic_Geometry/`.

**Recommended order**

1. **Orientation** — Quanta video profile: [YouTube](https://www.youtube.com/watch?v=1EpMF16ShY0) · [article](https://www.quantamagazine.org/caucher-birkar-who-fled-war-and-found-asylum-wins-fields-medal-20180801/).  
2. **Interview** — Cambridge Fields interview: [YouTube](https://www.youtube.com/watch?v=CwMvjWL-gos).  
3. **Meta** — Simons Fields Medal video page: [link](https://www.simonsfoundation.org/2018/08/01/field-medals-video-caucher-birkar/).

**Status reminder:** Boundedness of Fanos + MMP contributions—**not** a complete classification of all varieties.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Birkar_Algebraic_Geometry/transcripts/` · status: `research/video-research/Birkar_Algebraic_Geometry/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Birkar_Algebraic_Geometry_1EpMF16ShY0_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


Full URL bibliography from video research (including secondary finds): `research/video-research/Birkar_Algebraic_Geometry/references.md`.

### Complete URL list (audit)

1. https://www.youtube.com/watch?v=1EpMF16ShY0  
2. https://www.youtube.com/watch?v=CwMvjWL-gos  
3. https://www.simonsfoundation.org/2018/08/01/field-medals-video-caucher-birkar/  
4. https://arxiv.org/search/?query=Birkar+Fano+boundedness&searchtype=all  
5. https://www.quantamagazine.org/caucher-birkar-who-fled-war-and-found-asylum-wins-fields-medal-20180801/  
6. https://www.maths.cam.ac.uk/features/professor-caucher-birkar-wins-2018-fields-medal  
7. https://en.wikipedia.org/wiki/Caucher_Birkar  
8. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018  
9. https://arxiv.org/search/math?query=Birkar+boundedness+Fano&searchtype=all&source=header  
10. https://en.wikipedia.org/wiki/Minimal_model_program  
11. https://en.wikipedia.org/wiki/Fano_variety  
12. https://arxiv.org/search/?query=Birkar+Fano&searchtype=all  

### Research pack

13. Course pack: `research/video-research/Birkar_Algebraic_Geometry/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. IMU Fields Medal 2018 citation — Caucher Birkar (mathunion.org).
2. **C. Birkar**, papers on boundedness of Fano varieties (BAB-type theorems); see also surveys announcing the 2016–2018 results.
3. **C. Birkar, P. Cascini, C. Hacon, J. McKernan (BCHM)** — existence of flips / finite generation of canonical rings in broad settings.
4. **J. Kollár and S. Mori**, *Birational Geometry of Algebraic Varieties*, Cambridge University Press — standard graduate background.
5. Surveys of the MMP (various authors; ICM proceedings and AMS notices expositions).
6. Course context: Chapter 2 overview and other “program-level” portraits such as [Scholze]({{ site.baseurl }}/contents/en/chapter02/02_06_Scholze_Perfectoid/).

---

## Further directions

- Compare surface classification (Enriques–Kodaira) with higher-dimensional MMP: which invariants survive, and which steps are new?
- Explore how singularities of the MMP (discrepancies, klt pairs) interact with the **canonical ring** and finite generation.
- Read a careful survey on BAB and complements to see how local thresholds become global boundedness.
- Seminar A3 option: write a one-page “open problems after Birkar” brief (effective bounds, positive characteristic, special Fano lists)—without claiming the medal closed algebraic geometry.
