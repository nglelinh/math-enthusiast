---
layout: post
title: "Edward Witten: Physics into Modern Geometry"
chapter: '06'
order: 17
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
lesson_type: profile
---

In August 1990, at the International Congress of Mathematicians in Kyoto, a rare moment unfolded: the **Fields Medal**—pure mathematics' highest honor—was awarded to a theoretical physicist, **Edward Witten** (Institute for Advanced Study, Princeton). For much of the twentieth century, pure mathematics and theoretical physics felt like neighbors speaking different dialects: one insisting every logical brick lock tightly into place, the other willing to leap across chasms on physical intuition. Witten achieved something extraordinary: he took the bold dualities of quantum field theory and string theory seriously, translated them into sharp geometric and topological targets, and redrew the research map of modern mathematics for the next three decades.

This is a **mini-profile** of Witten's method inside our **duality track**—not a biography and not a QFT textbook. What matters here is not the aura around a name, but *how physical intuition turns into rigorous mathematical structure*.

---

## Key ideas: What Does Witten-Style Mathematical Physics Study?

If you graduated with multivariable calculus, linear algebra, differential equations, and introductory quantum mechanics, you might wonder what modern *Witten-style mathematical physics* actually bridges:

### 1. Low-Dimensional Topology and Invariants (Knots & 3–4 Manifolds)
Topology studies properties that survive continuous stretching without tearing—like telling two tangled knots apart in 3D space, or distinguishing two smooth calculus structures on the same 4D space. Classical topology uses algebraic invariants (fundamental groups, knot polynomials). Witten's approach builds brand-new invariants by placing a **topological quantum field theory (TQFT)** directly onto the manifold.

### 2. Enumerative Geometry and Moduli Spaces
A classic question of algebraic geometry asks: how many algebraic curves of degree $$d$$ pass through a given set of points on a curved complex surface or a 6D Calabi–Yau manifold? Direct counting becomes ferocious as $$d$$ grows. Through the lens of string theory (**mirror symmetry**), those curve counts appear as coefficients in a physical energy expansion—and duality swaps an impossible counting problem on space $$X$$ for a classical calculus integral on its mirror space $$Y$$!

### 3. Topological Quantum Field Theory (TQFT) and S-Duality
Unlike ordinary physics, which depends on distances and metrics, a **TQFT** depends only on topology. Consequently, physical observables—partition functions $$Z(M)$$ or Wilson loop expectations—**automatically become topological invariants** of $$M$$. Meanwhile, when two wildly different quantum theories are dual (like S-duality swapping electric/magnetic charges and strong/weak coupling), the mathematical structures behind them must be equivalent—acting as an astonishing **conjecture-generating engine** for pure geometry.

---

## Learning objectives

After this lecture you should be able to:

- Place Witten’s Fields Medal (1990) in the culture of “physics-inspired mathematics.”
- Name at least three themes where his influence appears in modern geometry/topology (e.g. knot invariants / Chern–Simons, mirror symmetry culture, geometric Langlands / S-duality).
- Explain the course rule: **physics as muse and bridge, not automatic proof**.
- Connect Witten to [Atiyah–Singer]({{ site.baseurl }}/contents/en/chapter08/08_11_Atiyah_Singer_Index/), [mirror symmetry]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/), and [geometric Langlands & S-duality]({{ site.baseurl }}/contents/en/chapter06/06_15_Geometric_Langlands_SDuality/).
- Avoid hero worship without objects: always name a **mathematical structure**, not only a person.

**Prerequisites.** Duality principle; mathematical-physics map. No string theory course required.

---

## 1. Why a physicist appears in a mathematics course

Twentieth-century geometry already talked to physics (Einstein, gauge theory, index theory). From the 1980s onward, **quantum field theory and string theory** generated a flood of precise *conjectural dictionaries*: correlators as intersection numbers, dualities as equivalences of categories or of moduli problems, anomalies as topological indices.

Consider the signature breakthrough behind the 1990 Fields Medal: in 1984, Vaughan Jones discovered a startling new knot polynomial (the Jones polynomial) via operator algebras, whose combinatorial formula seemed to have no obvious 3D geometric meaning. In 1989, Witten showed that if you run a 3D topological quantum field theory called **Chern–Simons theory** and evaluate the expectation value of a Wilson loop along the knot, you get *precisely the Jones polynomial*—and the definition automatically generalizes to knots inside any curved 3-manifold!

### Explanation: How Does a TQFT "Count" the Shape of Space?

To make "TQFT" completely concrete, let us compute a full **2-dimensional TQFT** by hand using nothing more than linear algebra! By the Atiyah–Dijkgraaf classification theorem, a 2D TQFT is equivalent to a finite-dimensional commutative **Frobenius algebra** $$(A, \theta)$$: the state space on a circle is $$A$$, merging two circles into one ("a pair of pants") is multiplication in $$A$$, and capping off a circle with a hemisphere is a trace functional $$\theta: A \to \mathbb{C}$$.

Pick a tiny concrete example: $$A = \mathbb{C}e_1 \oplus \mathbb{C}e_2$$ with orthogonal idempotents $$e_1^2 = e_1,\ e_2^2 = e_2,\ e_1 e_2 = 0$$ (unit $$1 = e_1 + e_2$$), and choose trace $$\theta(e_1) = 1,\ \theta(e_2) = \frac{1}{2}$$.

1. **Build the "handle operator" $$H$$ (attaching one donut hole):** The bilinear pairing $$\eta(a,b) = \theta(ab)$$ is diagonal $$\operatorname{diag}(1, \tfrac{1}{2})$$, so the dual basis is $$e^1 = e_1$$ and $$e^2 = 2e_2$$. Gluing on one handle corresponds to multiplying by
   $$
   H = e_1 e^1 + e_2 e^2 = e_1 + 2e_2.
   $$
2. **Compute the partition function $$Z(\Sigma_g)$$ of a closed surface with $$g$$ holes** by multiplying by $$H$$ exactly $$g$$ times and taking the trace $$\theta$$:
   - **Sphere $$S^2$$ ($$g=0$$ holes):** $$Z(S^2) = \theta(1) = \theta(e_1 + e_2) = 1 + \frac{1}{2} = \frac{3}{2}$$.
   - **Torus $$T^2$$ ($$g=1$$ hole):** $$Z(T^2) = \theta(H) = \theta(e_1 + 2e_2) = 1 + 2\cdot\frac{1}{2} = 2$$ (equals $$\dim A = 2$$—a universal TQFT theorem: the torus partition function always counts the dimension of the state space!).
   - **Genus-2 surface $$\Sigma_2$$ ($$g=2$$):** $$H^2 = (e_1 + 2e_2)^2 = e_1 + 4e_2 \implies Z(\Sigma_2) = \theta(e_1 + 4e_2) = 1 + 4\cdot\frac{1}{2} = 3$$.
   - **General genus $$g$$:** $$Z(\Sigma_g) = 1 + 2^{g-1}$$.
3. **See the principle:** From two lines of algebra, $$Z(\Sigma_g)$$ knows nothing about size, curvature, or bumps—it depends **strictly on the genus $$g$$**. In 3D (Chern–Simons) and 4D (Donaldson–Witten), Witten elevated this exact "cut–glue–trace" logic to generate deep knot and 4-manifold invariants.

Witten’s distinctive role was to turn many of those insights into **mathematical programs** with clean geometric targets. Collaborators and successors proved large pieces; the method outlived any single paper.

**Seminar moral.** When a duality first appears in physics, ask: *what theorem-shaped statement would make this rigorous?* That question is the bridge.

---

## 2. Themes (objects, not aura)

| Theme | Mathematical object (slogan) | Course landing |
|-------|------------------------------|----------------|
| Topological QFT / Chern–Simons | Knot and 3-manifold invariants | Topology / physics interface |
| Mirror symmetry culture | A/B models; enumerative geometry | [Mirror deep dive]({{ site.baseurl }}/contents/en/chapter06/06_13_Mirror_Symmetry/) |
| Seiberg–Witten / dualities | Smooth 4-manifold invariants; dual QFTs | Gauge / [Uhlenbeck]({{ site.baseurl }}/contents/en/chapter08/08_04_Uhlenbeck_Gauge/) culture |
| Geometric Langlands bridge | S-duality of $$\mathcal N=4$$ SYM → categories on Hitchin moduli | [GL & S-duality]({{ site.baseurl }}/contents/en/chapter06/06_15_Geometric_Langlands_SDuality/) (Kapustin–Witten) |
| Index / anomaly intuition | Dirac operators, characteristic classes | [Atiyah–Singer]({{ site.baseurl }}/contents/en/chapter08/08_11_Atiyah_Singer_Index/) |

You are **not** asked to master these theories. You are asked to recognize the **pattern**: duality or path integral → geometric category or invariant → theorem program.

---

## 3. Kapustin–Witten as a case study

In the geometric Langlands deep dive, **Kapustin–Witten** argue that electric–magnetic S-duality of twisted 4d $$\mathcal N=4$$ super Yang–Mills, compactified on a curve, organizes the geometric Langlands correspondence—with mirror symmetry of Hitchin systems as engine.

**What students should take away:**

1. Dual group $$G\leftrightarrow G^\vee$$ appears on both physics and math sides (for instance $$SU(n) \leftrightarrow PSU(n)$$ and $$SO(2n+1) \leftrightarrow Sp(2n)$$).  
2. Categories of branes / sheaves replace informal “states.”  
3. The paper is a **bridge**, not a replacement for pure geometric Langlands proofs.  
4. Status labeling still applies: arithmetic Langlands remains largely open; geometric formulations advance on their own mathematical timeline.

---

## 4. Fields culture and Abel culture

| Signal | Example in course |
|--------|-------------------|
| Fields (under 40, breakthrough objects) | Witten 1990; Ngô 2010; many Ch.2 medals |
| Abel (lifetime / infrastructure) | Serre 2003; Atiyah–Singer 2004; Langlands 2018 |

Witten’s Fields citation culture is closer to “opened highways between physics and geometry” than to a single elementary contest problem—similar in *climate* to Abel bridge prizes, different in career-stage rules.

---

## 5. Confusions

| Claim | Correction |
|-------|------------|
| “Witten proved the Langlands program.” | No. Influence and duality dictionaries ≠ full arithmetic Langlands. |
| “Physics proofs replace math proofs.” | Different standards; best work invites translation into theorems. |
| “String theory is the same as geometric Langlands.” | Related via S-duality culture; not identical subjects. |
| “Only string theorists need dualities.” | Dualities organize pure math (mirror, Langlands, index) independently of belief in strings. |

---

## References

1. IMU / Fields Medal 1990 materials on Witten.  
2. Kapustin–Witten — https://arxiv.org/abs/hep-th/0604151  
3. Course: duality track 12–15; Atiyah–Singer; Langlands Ch.2.  
4. Popular orientation talks (Frenkel, Witten symposium videos) — culture only.  

## Video tham khảo

- **xem trước** — [Prof. Edward Witten | Duality, the Langlands Correspondence, and the Influence of Michael Atiyah](https://www.youtube.com/watch?v=fqHGe3acpC0) — INI Seminar Room 1, English. Watch first. “Prof. Edward Witten | Duality, the Langlands Correspondence, and the Influence of Micha…” orients the lesson’s aim: Place Witten’s Fields Medal (1990) in the culture of “physics-inspired mathematics.”
- [Edward Witten, Gauge theory and the analytic approach to geometric Langlands](https://www.youtube.com/watch?v=QOi_yBoE2kA) — Clay Mathematics Institute, English. A second pass once the main claim is in view: Place Witten’s Fields Medal (1990) in the culture of “physics-inspired mathematics.”
- [The Universe Speaks in Numbers: Robbert Dijkgraaf and Edward Witten in Conversation](https://www.youtube.com/watch?v=RjthuCDzAnY) — Institute for Advanced Study, English. Further depth after the first two, still tied to this lesson: Place Witten’s Fields Medal (1990) in the culture of “physics-inspired mathematics.”
