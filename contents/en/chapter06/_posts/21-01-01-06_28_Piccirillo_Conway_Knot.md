---
layout: post
title: "Piccirillo and the Conway Knot: When ‘Homework’ Was Annals Material"
chapter: '06'
order: 28
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

In summer 2018, at a low-dimensional topology conference, graduate student **Lisa Piccirillo** (University of Texas at Austin) heard a “nice little problem” about the **Conway knot**—an eleven-crossing tangle famous enough that its diagram appears as sculpture on a gate of the Isaac Newton Institute in Cambridge. She worked on it in the **evenings**. By her own account she did not allow daytime research hours for it: she did not think of it as “real math.” It felt like homework.

Within **less than a week** she had a proof: the Conway knot is **not smoothly slice**. The smooth-sliceness question for this knot had resisted experts for about **fifty years**. Among knots with **twelve or fewer crossings**, every other case had been settled; Conway was the stubborn remainder. The published theorem **completes the classification of slice knots under thirteen crossings**.

When she casually mentioned the result to senior topologist **Cameron Gordon**, he asked why she was not more excited—and said the paper belonged in the *Annals of Mathematics*. It appeared there in 2020. About **fourteen months** after her PhD, she was on the MIT faculty track.

This lecture turns the story into seminar mathematics: definitions of sliceness, why Conway was uniquely hard, the **0-trace transfer** and **Rasmussen $$s$$-invariant**, the link to exotic four-space, and precision versus hype (**LO1**, **LO3**, **LO6**). Pair with [Donaldson–Seiberg–Witten]({{ site.baseurl }}/contents/en/chapter06/06_23_Donaldson_Seiberg_Witten/) and the [fourth-dimension studio]({{ site.baseurl }}/contents/en/chapter07/07_06_Explore_Fourth_Dimension/).

**Primary source.** Lisa Piccirillo, “The Conway knot is not slice,” *Annals of Mathematics* **191** (2020), 581–591; [arXiv:1808.02923](https://arxiv.org/abs/1808.02923) (submitted 8 August 2018).

---

## Learning objectives

After this lecture you should be able to:

- Define a **knot** in $$S^3$$ and what it means for a knot to be **smoothly slice** vs **topologically slice**.
- State Piccirillo’s theorem and two structural consequences (small-crossing classification; first topologically slice positive mutant of a slice knot that fails to be smoothly slice).
- Explain why the Conway knot defeated classical and many modern **slice obstructions** (Alexander polynomial $$1$$; positive mutant of the slice Kinoshita–Terasaka knot).
- Reconstruct the **proof idea**: same **0-trace** $$X(K)\cong X(K')$$ ⇒ shared sliceness; show $$s(K')=2\neq 0$$ ⇒ $$K'$$ not slice ⇒ Conway not slice.
- State the **trace embedding lemma** at slogan level: $$K$$ slice ⇔ $$X(K)$$ smoothly embeds in $$S^4$$.
- Locate the result in the smooth-vs-topological gap of **dimension four** (exotic $$\mathbb{R}^4$$ culture).
- Practice LO6: short solution time ≠ easy problem; popular narrative ≠ full theorem statement.

**Prerequisites.** Willingness to treat “embedded circle / disk / 4-ball” as geometric slogans. No prior knot-theory course. Handle calculus is named but not required for the idea-level proof.

---

## 1. Knots, concordance, and two kinds of disk

A **knot** is a smoothly embedded circle in the 3-sphere $$S^3$$ (a closed loop in space, up to ambient isotopy—deformations without cutting).

Classically, a knot is trivial in 3-space if it bounds an embedded disk in $$S^3$$. **Concordance** (Fox) is the four-dimensional upgrade: ask whether the knot bounds an embedded disk in the **4-ball** $$B^4$$ whose boundary is $$S^3$$.

| Notion | What disk is allowed? |
|--------|------------------------|
| **Smoothly slice** (often just “slice” in modern papers) | Smoothly embedded disk $$\Delta\subset B^4$$ with $$\partial\Delta=K$$ |
| **Topologically slice** | Locally flat disk in the topological category (Freedman-type “crumpled” spheres allowed) |

There are many slice knots that are not the unknot, and many topologically slice knots that are **not** smoothly slice. That distinction is a low-dimensional probe of the same phenomenon that makes smooth four-manifolds wilder than topological ones—see §6 and [Donaldson–SW]({{ site.baseurl }}/contents/en/chapter06/06_23_Donaldson_Seiberg_Witten/).

**Seminar slogan.** *Slice knots are the knots that become “unknots from the four-dimensional viewpoint”—but you must say whether the disk is smooth.*

---

## 2. The Conway knot’s résumé (why it was the last small case)

| Fact | Detail |
|------|--------|
| Diagram | **11 crossings**; Rolfsen notation **11n34** |
| Discovery / tables | Conway’s enumeration era (~1970); among the first complete lists to 11 crossings |
| Sibling | **Positive mutant** of the **Kinoshita–Terasaka (KT)** knot—the smallest positive-mutant pair |
| Alexander polynomial | $$\Delta=1$$ (among the smallest nontrivial knots with this property) |
| Topological sliceness | Both Conway and KT are **topologically slice** (Freedman, 1980s) |
| KT smooth sliceness | Readily shown to be **smoothly slice** |
| Conway smooth sliceness | **Open until Piccirillo (2018)** |

**Positive mutation.** A *Conway sphere* meets the knot in four points and splits it into two tangles; regluing after an involution of the sphere produces a **mutant**. Positive mutants keep a coherent orientation. Mutation preserves a long list of 3D invariants (Alexander, Jones, HOMFLY, Kauffman polynomials; hyperbolic volume; 2-fold branched covers; …). Several powerful modern invariants are *conjectured* mutation-invariant (e.g. aspects of Khovanov homology). Studying sliceness for a **positive mutant of a slice knot** is therefore especially hard: many obstructions vanish automatically.

**Why Alexander polynomial $$1$$ hurts.** Classical abelian and most metabelian sliceness obstructions vanish. For topological sliceness, Freedman’s disk theorem already gives the answer for such knots; the remaining drama is **smooth**.

**Historical classification statement (paper).** Completing Conway settles **slice knots under 13 crossings** (cf. Cha–Livingston tables). Popular accounts often say: among knots with **≤12 crossings**, only Conway’s smooth sliceness was unknown—same practical picture.

**First-example claim (paper, independent of the human story).** Piccirillo gives the **first** example of a knot that is simultaneously:

1. not smoothly slice,  
2. **topologically slice**, and  
3. a **positive mutant of a slice knot**.

Earlier non-slice mutants of slice knots were detected by metabelian methods that also obstruct *topological* sliceness—so they could not catch a Freedman-slice knot like Conway.

---

## 3. Why direct invariants kept failing

Think of sliceness detectors as tools with **blind spots**. Conway sat at their intersection:

- Mutant of a slice knot ⇒ many 3D and concordance invariants “look slice.”  
- $$\Delta=1$$ ⇒ classical algebraic obstructions die.  
- Topologically slice ⇒ purely topological slice tests cannot give a negative answer.  
- For the Conway diagram itself, Rasmussen’s $$s$$-invariant and related tools were not known to return a useful non-zero value in the way one would hope for a direct kill. (Indeed $$s$$ is often conjectured to vanish on such mutants.)

Joshua Greene (quoted in Quanta): it was “the knot that we couldn’t handle,” a touchstone for new invariants. Mark Hughes’s neural-net experiments famously gave roughly **50–50** predictions on Conway sliceness—an anecdote about stubbornness, not a theorem.

**Research moral.** When the famous representative is engineered to fool every standard meter, **change the representative** while preserving the four-dimensional property you care about.

---

## 4. The 0-trace and the transfer lemma

### 4.1. Definition

The **0-framed knot trace** (or **0-trace**) of a knot $$K$$ is the smooth 4-manifold

$$
X(K) \;=\; B^4 \;\cup\; \text{(0-framed 2-handle attached along $$K$$)}.
$$

Intuition: take a 4-ball, sew a solid “cap” along the knot with framing zero. The trace **encodes the knot in a strong four-dimensional way**.

### 4.2. Embedding lemma (folklore; Kirby–Melvin style)

<div class="textbook-lemma" markdown="1">
**Lemma (seminar form).**  
A knot $$K$$ is smoothly slice **if and only if** $$X(K)$$ smoothly embeds in $$S^4$$.
</div>

*Idea of one direction.* If $$K$$ bounds a smooth disk in a 4-ball, glue the complementary ball to a neighborhood of that disk to build an embedded copy of the trace in $$S^4$$. The converse recovers a smooth disk from an embedding of the trace by “unwinding” the 2-handle core after removing a cone point (piecewise-linear care, smooth away from one point).

### 4.3. Shared traces share sliceness

<div class="textbook-theorem" markdown="1">
**Corollary.** If $$X(K)\cong X(K')$$ as smooth 4-manifolds (diffeomorphic), then

$$
K \text{ is smoothly slice} \quad\Longleftrightarrow\quad K' \text{ is smoothly slice}.
$$
</div>

**Important subtlety (from the paper).** Such $$K'$$ need **not** be *concordant* to $$K$$. Trace twins share **sliceness**, not the full concordance class. That is enough for a non-sliceness proof.

---

## 5. Piccirillo’s construction of a twin $$K'$$

### 5.1. Strategy (her words, compressed)

> Abandon the Conway diagram. Build $$K'$$ with the same trace. Detect non-sliceness of $$K'$$ with a modern invariant that Conway itself would not reveal.

### 5.2. Dualizable patterns and unknotting number one

Producing distinct knots with diffeomorphic traces is a classical-but-underused industry: **dualizable patterns** (Akbulut; Lickorish; Gompf–Miyazaki; reworked by Piccirillo in her trace/shake-genus work). A flexible special case: **unknotting number one** knots admit an explicit handle-link construction yielding a twin with the same trace.

The Conway knot has unknotting number one. Piccirillo runs the machine (with careful isotopies to keep diagrams manageable) and exhibits a concrete twin $$K'$$:

$$
X(C) \;\cong\; X(K').
$$

(Her paper’s Figures 2 and 4–5 are the handle calculus; seminar students need only the existence slogan.)

### 5.3. Prior joint insight with Miller

With **Allison Miller**, Piccirillo had shown that trace twins need **not** look the same to all sliceness invariants. That justified the hope: maybe $$s$$ (or Floer correction terms) sees $$K'$$ even when it cannot kill $$C$$ directly.

---

## 6. Killing $$K'$$ with Rasmussen’s $$s$$-invariant

### 6.1. What $$s$$ is (map level)

- **Khovanov homology** categorifies the Jones polynomial (Khovanov, 2000).  
- **Lee’s deformation** of the differential yields a spectral sequence from Khovanov homology to **Lee homology**.  
- For any knot, Lee homology is two-dimensional over $$\mathbb{Q}$$, supported in homological grading $$0$$.  
- **Rasmussen** extracts an integer $$s(K)$$ from the quantum gradings of those generators.

<div class="textbook-theorem" markdown="1">
**Theorem (Rasmussen).** If $$K$$ is smoothly slice, then $$s(K)=0$$.
</div>

(The invariant also bounds smooth slice genus more generally; we only need the slice vanishing.)

### 6.2. Computation for the twin

Piccirillo computes the rational Khovanov homology of $$K'$$ (via Bar-Natan’s FastKh routines / Knot Atlas-type software), then uses the **bidegrees of spectral-sequence differentials** to show that a generator in grading $$(0,3)$$ survives. Conclusion:

$$
s(K') \;=\; 2 \;\neq\; 0.
$$

Hence $$K'$$ is **not** smoothly slice. By the shared-trace corollary, neither is the Conway knot.

**Remark (paper).** For *any* twin of Conway with the same 0-trace, the Heegaard Floer **$$\tau$$-invariant** can be shown to vanish: $$\tau(K')=0$$. So $$\tau$$ is blind on this whole trace family; **$$s$$ is not**. That is a precise reason the dualization was worth doing.

### 6.3. Proof skeleton (LO3 narrative)

1. **Lemma:** slice ⇔ 0-trace embeds smoothly in $$S^4$$.  
2. **Construction:** dualizable-pattern / unknotting-number-1 calculus ⇒ twin $$K'$$ with $$X(C)\cong X(K')$$.  
3. **Computation:** Khovanov + Lee spectral sequence ⇒ $$s(K')=2$$.  
4. **Rasmussen:** $$s\neq 0$$ ⇒ $$K'$$ not slice.  
5. **Transfer:** Conway not slice.

```text
Conway C  ── same 0-trace ──►  K'
     │                           │
     │                      s(K') = 2 ≠ 0
     │                           │
     └──── not smoothly slice ◄──┘
```

---

## 7. Human timeline and seminar morals (LO6)

| Claim in popular media | Careful reading |
|------------------------|-----------------|
| “Solved in under a week.” | True as self-report after years of training on *traces*; the open problem was decades old. |
| “She thought it was homework.” | Self-assessment of prestige, not of difficulty; Gordon’s reaction recalibrated the prestige. |
| “Evening work only.” | Constraint ≠ unimportance. |
| “One paper made the career.” | Flagship result *plus* a coherent program (traces, shake genus, concordance); Annals + MIT followed a body of work. |

**What experts recognized.** The leftover box in the small-crossing tables was a **touchstone**. Closing it with a method that generalizes (trace twins + modern homology) is why the community yelled *Annals*.

**What the week measures.** Once the strategy “build a cooperative twin” is live in your hands, computation can finish quickly. Inventing the strategy is the research.

---

## 8. Why four dimensions break the pattern

### 8.1. Freedman vs Donaldson (1980s culture)

- **Freedman:** topological 4-manifolds and locally flat disks are surprisingly flexible (disk theorem, topological h-cobordism phenomena).  
- **Donaldson:** smooth 4-manifolds are rigidly constrained by **gauge theory** (instantons; later Seiberg–Witten)—see course essays on [gauge geometry]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/) and [Donaldson–SW]({{ site.baseurl }}/contents/en/chapter06/06_23_Donaldson_Seiberg_Witten/).

Together they produce the industry of objects that exist topologically but not smoothly—including **topologically slice, not smoothly slice** knots.

### 8.2. Exotic $$\mathbb{R}^4$$

For every dimension $$n\neq 4$$, a smooth manifold homeomorphic to Euclidean space $$\mathbb{R}^n$$ is diffeomorphic to the standard smooth structure. In **dimension four** there are **uncountably many** pairwise nondiffeomorphic smooth structures on the topological manifold $$\mathbb{R}^4$$ (**exotic $$\mathbb{R}^4$$s**: Freedman–Donaldson–Casson–Taubes–Gompf…).

Not 3. Not 5. Not 11. **Four** is the outlier. Knot sliceness is often called a **lowest-dimensional probe** of that exotic world: slice knots help build and detect exotic 4-spaces.

### 8.3. Piccirillo’s tools vs Donaldson’s tools

| Program | Probe of smooth 4D |
|---------|---------------------|
| Donaldson / SW | Moduli of connections / monopoles on closed 4-manifolds |
| Piccirillo (Conway) | Knot traces + Khovanov–Rasmussen $$s$$ |

Same category (smooth embeddings in dimension 4); different machines. The course places both under “four dimensions are special.”

---

## 9. Precision versus hype (LO6)

| Claim | Verdict | Correction |
|-------|---------|------------|
| “All knots with ≤12 crossings were open problems.” | False | Only Conway’s *smooth* sliceness remained among those small cases. |
| “The knot is not slice in any sense.” | Incomplete | It **is** topologically slice; it is **not** smoothly slice. |
| “She reinvented 4D topology in a week.” | Overstated | She closed a famous residual case with a sharp reduction inside a mature toolkit she already developed. |
| “$$s$$ vanishes on all mutants, so the proof is impossible.” | Confused | Directly on Conway, $$s$$ was unhelpful; on the **trace twin**, $$s(K')=2$$ works. |
| “Same trace ⇒ same knot.” | False | Twins can be distinct as knots (and even non-concordant). |
| “Because 4D is exotic, every knot problem is hopeless.” | False | Most small knots *were* classified; Conway was hard, not mystical. |

---

## 10. Course web

| Essay / studio | Connection |
|----------------|------------|
| [Donaldson–SW]({{ site.baseurl }}/contents/en/chapter06/06_23_Donaldson_Seiberg_Witten/) | Smooth vs topological 4-manifolds; gauge probes |
| [Uhlenbeck]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/) | Analytic control of gauge moduli (sibling culture) |
| [Gauge as geometry]({{ site.baseurl }}/contents/en/chapter06/06_19_Gauge_Geometry_YM/) | Connections behind Donaldson |
| [Fourth-dimension studio]({{ site.baseurl }}/contents/en/chapter07/07_06_Explore_Fourth_Dimension/) | Coordinates vs smooth exotica |
| [Higher dimensions]({{ site.baseurl }}/contents/en/chapter04/04_08_Higher_Dimensions/) | High-$$D$$ geometry (different theme) |

---

## Exercises

1. **Definitions (≤80 words each).** Smoothly slice vs topologically slice.  
2. **Why hard?** List three reasons Conway defeated standard slice tests.  
3. **Trace lemma.** State the embedding characterization of sliceness; give one-sentence intuition for one direction.  
4. **Transfer.** If $$X(K)\cong X(K')$$ and $$s(K')=2$$, why is $$K$$ not smoothly slice? Write the three-line chain.  
5. **Mutation literacy.** What is a positive mutant, and why does that matter when the sibling is slice?  
6. **$$s$$ vs $$\tau$$.** In ≤60 words: why might one need $$s$$ even if $$\tau=0$$ on an entire trace family?  
7. **LO6 rewrite.** Correct: “A grad student casually solved an easy knot puzzle over a weekend, proving 4D topology was overrated.”  
8. **Bridge paragraph.** Connect this story to the slogan “smooth structure in dimension 4 is detectable by refined invariants” without claiming Piccirillo used Yang–Mills moduli.  
9. **Stretch.** Watch Borcherds’s expository talk (link below); list three definitions he emphasizes that match this essay.

---

## Video sources

Use for orientation; claims load-bearing for theorems still rest on the paper.

1. **Richard E. Borcherds** — “Is the Conway knot slice? (After Lisa Piccirillo)” — [YouTube](https://www.youtube.com/watch?v=XewXN4i5Or4) (~24 min).  
2. **Quanta / popular** — narrative companion to Klarreich’s article (optional).

---

## References and further reading

1. **Lisa Piccirillo**, “The Conway knot is not slice,” *Ann. of Math.* **191** (2) (2020), 581–591. DOI [10.4007/annals.2020.191.2.5](https://doi.org/10.4007/annals.2020.191.2.5). PDF via [Annals](https://annals.math.princeton.edu/2020/191-2/p05).  
2. **arXiv:1808.02923** — same paper; readable HTML on [ar5iv](https://ar5iv.labs.arxiv.org/html/1808.02923).  
3. **Erica Klarreich**, “Graduate Student Solves Decades-Old Conway Knot Problem,” *Quanta Magazine*, 19 May 2020 — human story; verify against (1).  
4. **Jacob Rasmussen**, “Khovanov homology and the slice genus,” *Invent. Math.* **182** (2010) — $$s$$-invariant.  
5. **Allison N. Miller & Lisa Piccirillo**, “Knot traces and concordance,” *Journal of Topology* **11** (2018) — traces vs concordance invariants.  
6. **Lisa Piccirillo**, PhD thesis / “Knot traces and the slice genus” materials (UT Austin) — broader program.  
7. Cha–Livingston tables of knot sliceness (small crossings).  
8. Course links in §10.  
