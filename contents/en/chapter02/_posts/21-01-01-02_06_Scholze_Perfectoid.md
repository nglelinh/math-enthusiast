---
layout: post
title: "Scholze’s Perfectoid Spaces (Fields Medal 2018)"
chapter: '02'
order: 7
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
---

Some Fields Medals honor the climber who conquers a single legendary peak—a century-old conjecture finally brought down. Others honor the cartographer who invents a **brand-new map and language**, suddenly turning an impassable mountain range into open terrain. The story of **Peter Scholze** and the **2018 Fields Medal** belongs squarely to the second kind.

For decades, arithmetic geometers lived split between two twin worlds separated by a stubborn wall: **characteristic $$0$$** (where ordinary integers and $$p$$-adic numbers live) and **characteristic $$p$$** (where arithmetic happens modulo a prime $$p$$, unlocking a magical symmetry called the *Frobenius map*). Major theorems were already proved in characteristic $$p$$ yet remained completely stuck in characteristic $$0$$. At age 24, in his landmark 2012 paper, Scholze introduced **perfectoid spaces** and a translation engine called **tilting**, turning what had long been regarded as a nightmare (*infinite wild ramification*) into the very bridge linking the two worlds.

**Lesson roadmap:** Background Knowledge Map (hand calculations in $$5$$-adic numbers, Frobenius magic in char $$3$$, why "carrying" builds the wall) → Deep-Dive Explanation (Read Slowly): adjoining $$p$$-power roots, tilting $$X \mapsto X^\flat$$, tilting equivalence, and weight-monodromy → Infrastructure impact & condensed mathematics.

---

## Learning objectives

After this lecture you should be able to:

- Verify by hand basic $$5$$-adic distances (including $$4 + 4\cdot 5 + 4\cdot 5^2 + \cdots = -1$$) and the Frobenius identity $$(x+y)^p = x^p + y^p$$ in characteristic $$p$$.
- Explain why **mixed characteristic** and **carrying in addition** separate $$\mathbb{Q}_p$$ from $$\mathbb{F}_p((t))$$.
- Follow the four-step mechanism of **perfectoid spaces** and **tilting**: why adjoining infinitely many $$p$$-power roots erases the carrying discrepancy.
- Name major impact zones (weight-monodromy, $$p$$-adic and prismatic cohomology, local Langlands) and distinguish the 2018 Fields work from **condensed mathematics** (with Clausen), which came afterward.

**Prerequisites.** Modular arithmetic, binomial expansion, and basic rings/fields. No prior schemes or adic spaces required.

**Seminar links.** Arithmetic geometry neighbors: [Langlands program / Ngô]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/), [Birch–Swinnerton-Dyer]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/), [Tsimerman arithmetic]({{ site.baseurl }}/contents/en/chapter02/02_14_Tsimerman_Arithmetic/), [Wiles / Fermat]({{ site.baseurl }}/contents/en/chapter08/08_03_Wiles_Fermat/), [cryptography applications of number theory]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/) (motivation for $$p$$-adics, not an application claim for perfectoids). Lifetime-foundations parallel: [Abel Prize overview]({{ site.baseurl }}/contents/en/chapter08/08_02_What_Is_Abel_Prize/).

---

## Background Knowledge Map: $$p$$-adic Numbers, Characteristic $$p$$, and the "Carrying Wall"

### 1. What Are $$p$$-adic Numbers? (Calculate by Hand for $$p = 5$$)
In the **$$5$$-adic** world, two integers are *close* if their difference is divisible by a high power of $$5$$: writing $$n = 5^k m$$ ($$5 \nmid m$$), define $$\vert n\vert_5 = 5^{-k}$$. Check two astonishing facts in the $$5$$-adic integers $$\mathbb{Z}_5$$:
- **Distance:** $$\vert 26 - 1\vert_5 = \vert 5^2\vert_5 = 1/25 = 0.04$$, and $$\vert 626 - 1\vert_5 = \vert 5^4\vert_5 = 1/625 = 0.0016$$—so $$626$$ sits right next to $$1$$!
- **An infinite series converging to $$-1$$:** Consider $$S = 4 + 4\cdot 5 + 4\cdot 5^2 + 4\cdot 5^3 + \cdots$$ Over $$\mathbb{R}$$ it diverges, but in $$\mathbb{Z}_5$$ the $$k$$-th term has size $$5^{-k} \to 0$$, so it **converges**! Add $$1$$ to $$S$$ using grade-school base-5 carrying:
  - Units place: $$1 + 4 = 5 = 0$$ (carry $$1$$).
  - $$5$$'s place: $$1 + 4 = 5 = 0$$ (carry $$1$$).
  - Forever onward → $$1 + S = 0 \implies S = -1$$! (Geometric series check: $$4 \cdot \frac{1}{1 - 5} = -1$$!)

Completing $$\mathbb{Q}$$ under $$\vert \cdot\vert_p$$ gives $$\mathbb{Q}_p$$ (power series $$\sum_{k \ge k_0} a_k p^k$$ with $$a_k \in \{0,\dots,p-1\}$$), the local microscope of $$p$$-adic arithmetic geometry.

### 2. Characteristic $$p$$ and the Frobenius Miracle (Check for $$p = 3$$)
Now look at $$\mathbb{Q}_p$$'s twin: the Laurent series field $$\mathbb{F}_p((t))$$ of series $$\sum_{k \ge k_0} a_k t^k$$ with coefficients in $$\mathbb{F}_p$$, where $$p = 0$$ (**characteristic $$p$$**). Here, raising to the $$p$$-th power—the **Frobenius map** $$\varphi(x) = x^p$$—is a ring homomorphism! Check $$p = 3$$:

$$
(x + y)^3 = x^3 + 3x^2 y + 3xy^2 + y^3 \;\equiv\; x^3 + y^3 \pmod 3.
$$

Every middle binomial coefficient is divisible by $$p$$ and vanishes!

### 3. The Wall Between Them: Carrying in Mixed Characteristic
If $$\mathbb{Q}_p$$ (series in $$p$$) and $$\mathbb{F}_p((t))$$ (series in $$t$$) look identical, why can't we just swap $$p \leftrightarrow t$$? Try adding $$3 + 4$$ in base $$5$$:
- In $$\mathbb{F}_5((t))$$: $$(3 + 0\cdot t) + (4 + 0\cdot t) = 2 + 0\cdot t$$ (**no carry**!).
- In $$\mathbb{Q}_5$$: $$(3 + 0\cdot 5) + (4 + 0\cdot 5) = 2 + \mathbf{1}\cdot 5$$ (**carries $$1$$ into the next digit**!).

That carrying discrepancy is the essence of **mixed characteristic** (generic fiber $$\mathbb{Q}_p$$ has char $$0$$, special fiber $$\mathbb{F}_p$$ has char $$p$$), and it blocked direct translation between the two worlds for decades.

---

## 1. Deep-Dive Explanation: How Perfectoid Spaces and Tilting Erase Carrying (Read Slowly)

#### Step 1: Adjoin infinitely many $$p$$-power roots — become "Perfectoid"
In characteristic $$p$$, a ring is **perfect** if Frobenius $$x \mapsto x^p$$ is bijective—meaning *every element has a $$p$$-th root* (e.g., completing $$\mathbb{F}_p((t^{1/p^\infty}))$$). In characteristic $$0$$, Scholze deliberately steps into **infinite wild ramification** by adjoining every $$p$$-power root of $$p$$:

$$
K \;=\; \widehat{\mathbb{Q}_p\bigl(p^{1/p},\; p^{1/p^2},\; p^{1/p^3},\; \dots\bigr)}.
$$

This is the prototype **perfectoid field**: a complete mixed-characteristic field with enough $$p$$-power roots that $$x \mapsto x^p$$ is surjective on $$\mathcal{O}_K / p\mathcal{O}_K$$.

#### Step 2: Define the Tilt $$K^\flat$$ via Compatible $$p$$-Power Root Sequences
Build the characteristic-$$p$$ twin $$K^\flat$$ ("$$K$$-flat") as the set of **compatible sequences** of $$p$$-power roots:

$$
x = \bigl(x^{(0)},\; x^{(1)},\; x^{(2)},\; \dots\bigr) \quad \text{with} \quad \bigl(x^{(n+1)}\bigr)^p = x^{(n)}.
$$

- **Multiplication** is coordinatewise: $$(x \cdot y)^{(n)} = x^{(n)} y^{(n)}$$.
- **Addition (the magic trick!):** take the limit of $$p^m$$-th powers:

$$
(x + y)^{(n)} \;=\; \lim_{m \to \infty} \bigl(x^{(n+m)} + y^{(n+m)}\bigr)^{p^m}.
$$

**Why carrying vanishes:** Every "carry" error introduced when raising a sum to the $$p^m$$-th power is divisible by $$p^m$$, so in the $$p$$-adic norm it shrinks at rate $$p^{-m} \to 0$$! Better yet, $$p^\flat = (p, p^{1/p}, p^{1/p^2}, \dots)$$ plays the role of $$t$$, and adding $$1$$ to itself $$p$$ times gives $$\lim_{m\to\infty} p^{p^m} = 0$$—so $$K^\flat$$ genuinely has **characteristic $$p$$**! Specifically:

$$
\widehat{\mathbb{Q}_p(p^{1/p^\infty})}^\flat \;\simeq\; \widehat{\mathbb{F}_p((t^{1/p^\infty}))}.
$$

#### Step 3: Tilting Equivalence for Perfectoid Spaces (Scholze, 2012)
Fontaine–Wintenberger (1979) proved that $$K$$ and $$K^\flat$$ have isomorphic Galois groups. Scholze's Fields-level leap was lifting tilting from *fields* to **full geometric spaces** (**perfectoid spaces**, glued from spectra of perfectoid algebras in Huber's adic-space framework): a mixed-characteristic perfectoid space $$X$$ and its char-$$p$$ tilt $$X^\flat$$ share the **exact same underlying topological space** and **equivalent categories of étale covers** (hence the same étale cohomology!).

#### Step 4: Tilt, Solve in Characteristic $$p$$, and Transfer Back
In his 2012 paper, Scholze immediately demonstrated this power on the **weight-monodromy conjecture** (proved by Deligne in char $$p$$ in 1980, stuck in char $$0$$ for 30 years): embed a char-$$0$$ projective variety into perfectoid projective space $$\mathbb{P}^{n,\mathrm{perf}}$$, **tilt** to char $$p$$, apply Deligne's theorem on the tilted side, and transport the cohomological conclusion back to characteristic $$0$$!

$$
\text{Mixed char } (\mathbb{Q}_p)
\;\xrightarrow{\text{Adjoin } p^{1/p^\infty}}\;
\text{Perfectoid space } X
\;\xrightarrow{\text{Tilt } (\cdot)^\flat}\;
\text{Char } p \; (X^\flat)
\;\xrightarrow{\text{Frobenius}}\;
\text{Solve \& transfer back}.
$$

---

## 2. Infrastructure Impact and Condensed Mathematics

Perfectoid geometry rewired modern $$p$$-adic arithmetic geometry: it fueled new comparison theorems in $$p$$-adic Hodge theory, **prismatic cohomology** (with Bhargav Bhatt), geometric **local Langlands** (the Fargues–Scholze program), and Shimura varieties.

| Style of Fields Achievement | Course Example | What Is Prized |
|-------|---------------------------|----------------|
| Close a sharp optimization conjecture | [Viazovska packing]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/) | Exact optimal configuration via modular forms |
| Complete a geometric PDE program | [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) | Ricci flow + surgery settles geometrization |
| **Foundations / new language** | **Scholze perfectoids**; [Ngô]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/) | New categories, equivalences, cohomology |

**Sequel chapter — Condensed Mathematics:** After 2018, Scholze and **Dustin Clausen** developed *condensed mathematics* to unify topology, functional analysis, and homological algebra. Keep them distinct: Fields 2018 honors **perfectoid spaces and $$p$$-adic geometry**; condensed mathematics is a later foundational program.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Perfectoid spaces replace all schemes.” | They are a powerful class of adic objects complementing schemes, not replacing them. |
| “Tilting erases number theory.” | It reorganizes arithmetic; deep number theory returns after transfer. |
| “Fields 2018 = condensed mathematics.” | The 2018 medal centers on perfectoid / $$p$$-adic geometry; condensed math (with Clausen) came later. |
| “Only one person works in this area.” | A large collaborative community (Bhatt, Fargues, Weinstein, Clausen, …); always credit coauthors. |
| “$$p$$-adic calculus is the same as real calculus.” | Nonarchimedean analysis has a completely different, tree-like topology. |

---

## Video sources (math-video-researcher pack)

Full ranking: `research/video-research/Scholze_Perfectoid/`.

**Recommended order**

1. **Orientation** — IMU Fields Medal video (Scholze 2018): [YouTube](https://www.youtube.com/watch?v=jGHyAqztdLY) · [Simons page](https://www.simonsfoundation.org/2018/08/01/fields-medal-video-peter-schloze/).  
2. **Foundation** — Jared Weinstein intro to perfectoid spaces (Fields Symposium 2021): [YouTube](https://www.youtube.com/watch?v=RApkRqoiZ1I).  
3. **Profile** — Quanta: [A Master of Numbers and Shapes…](https://www.quantamagazine.org/peter-scholze-becomes-one-of-the-youngest-fields-medalists-ever-20180801/).  
4. **Optional** — CIRM / carmin.tv Scholze interview hub: [link](https://www.carmin.tv/en/collections/fields-medallists-2018/video/interview-at-cirm-peter-scholze).

**Status reminder:** Perfectoid technology is a **toolkit** for $$p$$-adic geometry—not a claim that classical schemes are obsolete.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/Scholze_Perfectoid/transcripts/` · status: `research/video-research/Scholze_Perfectoid/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/Scholze_Perfectoid_jGHyAqztdLY_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


Full URL bibliography from video research (including secondary finds): `research/video-research/Scholze_Perfectoid/references.md`.

### Complete URL list (audit)

1. https://www.youtube.com/watch?v=jGHyAqztdLY  
2. https://www.youtube.com/watch?v=RApkRqoiZ1I  
3. https://www.simonsfoundation.org/2018/08/01/fields-medal-video-peter-schloze/  
4. https://www.carmin.tv/en/collections/fields-medallists-2018/video/interview-at-cirm-peter-scholze  
5. https://arxiv.org/search/?query=perfectoid+Scholze&searchtype=all  
6. https://www.quantamagazine.org/peter-scholze-becomes-one-of-the-youngest-fields-medalists-ever-20180801/  
7. https://plus.maths.org/ps  
8. https://en.wikipedia.org/wiki/Perfectoid_space  
9. https://en.wikipedia.org/wiki/Peter_Scholze  
10. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018  
11. https://en.wikipedia.org/wiki/P-adic_number  
12. https://www.mathematics.uni-bonn.de/people/scholze  

### Research pack

13. Course pack: `research/video-research/Scholze_Perfectoid/` (`README.md`, `analysis.md`, `learning_path.md`, `references.md`).

1. IMU Fields Medal 2018 citation — Peter Scholze.
2. P. Scholze, *Perfectoid spaces*, Publ. Math. IHÉS (2012).
3. Lecture notes and surveys on perfectoid geometry (Berkeley notes; various masterclass notes).
4. Background: Huber adic spaces; Fontaine period rings (as pointers, not required reading).
5. Scholze–Clausen materials on condensed mathematics (for later orientation only).
6. Course cross-links: [Langlands]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/), [BSD]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/), [Abel overview]({{ site.baseurl }}/contents/en/chapter08/08_02_What_Is_Abel_Prize/).

---

## Further directions

- Read a non-technical profile *alongside* the first few pages of a technical survey.
- Explore how local Langlands and Shimura varieties interact with modern $$p$$-adic geometry—gateway into research seminars.
- If you enjoy foundations, sample one expository talk on condensed mathematics after you can state tilting correctly.
- Contrast with [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/): analytic/dynamical synthesis versus geometric/foundational rebuild—two different 2018 Fields styles.

## Video tham khảo

- **xem trước** — [Fields Medal Winner 2018 Peter Scholze](https://www.youtube.com/watch?v=jGHyAqztdLY) — International Mathematical Union, English. Watch first. IMU profile introducing Scholze and perfectoid geometry.
- [Fields Medal Symposium 2021: Jared Weinstein introduces Perfectoid Spaces](https://www.youtube.com/watch?v=RApkRqoiZ1I) — Fields Institute, English. Clear mathematical introduction to perfectoid spaces and tilting.
