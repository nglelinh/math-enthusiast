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

Number theory often wants geometry over the **$$p$$-adic numbers**—completions of the rationals where divisibility by a prime $$p$$ defines distance. That world mixes two characteristics at once: the “generic” fiber behaves like characteristic $$0$$, while the residue field has characteristic $$p$$. Classical algebraic geometry, born over fields and discrete valuation rings of mild ramification, strains under **wild ramification** and highly ramified towers. **Peter Scholze** received the **Fields Medal 2018** for creating **perfectoid spaces**, a class of objects that turn parts of this chaos into a dictionary: certain mixed-characteristic geometries correspond, via **tilting**, to geometries in characteristic $$p$$ where the Frobenius endomorphism is an isomorphism.

This essay aims at undergrad-seminar fluency: what “mixed characteristic” means, what the tilting slogan claims, which problem areas felt the impact (weight-monodromy ideas, $$p$$-adic cohomology, arithmetic geometry infrastructure), and how to read Scholze’s prize as a **foundations** award—closer in spirit to rewiring the language than to settling a single named conjecture. **LO6:** “perfectoid spaces solved number theory” is hype; they reorganized a toolkit.

---

## Learning objectives

After this lecture you should be able to:

- Explain the **mixed-characteristic** difficulty in one clear paragraph.
- State the **tilting** slogan: a dictionary between certain mixed-characteristic objects and characteristic-$$p$$ objects with bijective Frobenius.
- Describe perfectoid rings/spaces as a highly ramified class designed so that tilting works.
- Name at least two application zones (e.g. weight-monodromy-type results, $$p$$-adic cohomology / period rings).
- Compare Scholze’s medal narrative to other “infrastructure” prizes (Langlands foundations, representation-theoretic rebuilds) rather than only to “one conjecture” medals.
- Mention **condensed mathematics** (with Clausen) as a later foundational layer—awareness, not mastery.
- Practice **LO6**: distinguish IMU citations and technical surveys from popular “young genius rewrote math” tropes.

**Prerequisites.** Rings and fields; the idea of completion ($$p$$-adic integers $$\mathbb{Z}_p$$ and field $$\mathbb{Q}_p$$); Frobenius $$x\mapsto x^p$$ on characteristic-$$p$$ rings. Schemes are helpful but not required—think “geometric spaces glued from spectra of rings.”

**Seminar links.** **LO1** (deep programs), **LO6** (critique medal hype). Arithmetic geometry neighbors: [Langlands program / Ngô]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/), [Birch–Swinnerton-Dyer]({{ site.baseurl }}/contents/en/chapter01/01_04_Birch_Swinnerton_Dyer/), [Tsimerman arithmetic]({{ site.baseurl }}/contents/en/chapter02/02_14_Tsimerman_Arithmetic/), [Wiles / Fermat]({{ site.baseurl }}/contents/en/chapter08/08_03_Wiles_Fermat/), [cryptography applications of number theory]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/) (motivation for $$p$$-adics, not an application claim for perfectoids). Lifetime-foundations parallel: [Abel Prize overview]({{ site.baseurl }}/contents/en/chapter08/08_02_What_Is_Abel_Prize/).

---

## 1. Why $$p$$-adic geometry is hard

Fix a prime $$p$$. The field $$\mathbb{Q}_p$$ is the completion of $$\mathbb{Q}$$ for the $$p$$-adic absolute value. Its ring of integers is $$\mathbb{Z}_p$$. Finite extensions of $$\mathbb{Q}_p$$ and their integer rings are the local laboratories of arithmetic geometry: elliptic curves over $$\mathbb{Q}_p$$, Galois representations of $$\mathrm{Gal}(\overline{\mathbb{Q}}_p/\mathbb{Q}_p)$$, and special fibers of integral models all live here.

**Mixed characteristic** means: the fraction field has characteristic $$0$$, while the residue field (integers modulo the maximal ideal) has characteristic $$p$$. Geometry over $$\mathbb{Z}_p$$ therefore interpolates between a characteristic-$$0$$ generic fiber and a characteristic-$$p$$ special fiber. When extensions are **wildly ramified**, Galois groups and ramification filtrations become complicated; cohomology theories that work smoothly in equal characteristic need new comparison isomorphisms; and “limit” objects of infinite ramification towers are hard to control with classical scheme theory alone.

A cartoon of the difficulty:

$$
\underbrace{\text{char }0}_{\text{generic fiber}}
\;\longleftrightarrow\;
\underbrace{\text{integral model}}_{\text{mixed}}
\;\longleftrightarrow\;
\underbrace{\text{char }p}_{\text{special fiber}}.
$$

One wants theorems that move information across the arrows without drowning in ramification.

---

## 2. Perfectoid rings: Frobenius becomes an isomorphism

In characteristic $$p$$, every ring $$R$$ has a Frobenius endomorphism $$\varphi:R\to R$$, $$x\mapsto x^p$$. If $$\varphi$$ is an **isomorphism**, $$R$$ is called **perfect** (for reduced rings of characteristic $$p$$, this matches the classical notion). Perfect rings are often more tractable: one can take $$p$$-power roots freely, and certain cohomology theories simplify.

Scholze isolated **perfectoid** algebras—highly ramified complete topological rings (in a precise nonarchimedean topology) that admit a surjective “Frobenius-like” map with controlled kernel, so that after a tilting construction one lands in the perfect world. The exact algebraic definition involves almost mathematics, Fontaine’s period rings, and completed perfections; seminar fluency needs the design goal more than the full axiom list:

> Perfectoid objects are those for which infinite $$p$$-power roots exist in a coherent way, making them look “as perfect as mixed characteristic allows.”

**Perfectoid spaces** are geometric objects glued from spectra of perfectoid algebras in the style of adic spaces (Huber’s framework), not classical varieties over a field. They form a category rich enough to host cohomology and Galois actions, yet rigid enough for tilting.

---

## 3. Tilting: a dictionary between two worlds

The headline construction is **tilting**. To a perfectoid algebra $$R$$ in mixed characteristic one associates a perfectoid algebra $$R^\flat$$ (“$$R$$ flat”) in characteristic $$p$$. At the level of spaces, there is an equivalence of categories (in the appropriate perfectoid setup):

$$
\{\text{perfectoid spaces over a mixed-char base}\}
\;\simeq\;
\{\text{perfectoid spaces over the tilted char-$$p$$ base}\}.
$$

Slogan form used throughout the literature:

$$
\text{mixed characteristic}
\quad\xrightarrow{\ \text{tilt}\ }
\text{characteristic }p\text{ (perfect)},
\quad
\text{then transfer theorems back}.
$$

Why does this help? Many hard questions about ramification and cohomology become easier after tilt, because one works with perfect rings and characteristic-$$p$$ techniques (including Frobenius as an automorphism). Results proved on the tilted side can often be transported back to the original mixed-characteristic side via the equivalence.

**LO6 caution.** Tilting does **not** erase number theory or replace schemes by a single magic category for all purposes. It is a powerful equivalence on a carefully chosen class of objects. Ordinary schemes of finite type over $$\mathbb{Z}$$ are not perfectoid; one often passes to pro-systems, covers, or untilts of characteristic-$$p$$ objects to access classical questions.

---

## 4. Weight-monodromy and $$p$$-adic cohomology

Two families of impact are safe to name at seminar level.

**Weight-monodromy-type ideas.** In $$p$$-adic and $$\ell$$-adic cohomology of varieties over local fields, monodromy operators and weight filtrations organize how cohomology behaves under degeneration. Deligne proved the weight-monodromy conjecture for varieties over function fields (equal characteristic). Mixed-characteristic analogues are harder. Perfectoid methods gave new approaches and special cases by moving geometric situations into settings where Frobenius and monodromy interact more cleanly after tilt. Treat precise theorem lists as reading assignments, not exam slogans without citations.

**$$p$$-adic cohomology and periods.** Comparing étale, de Rham, crystalline, and other cohomologies of $$p$$-adic varieties is a classical theme (Fontaine, Faltings, Tsuji, …). Perfectoid geometry supplied new constructions of period sheaves, new proofs and extensions of comparison theorems, and a flexible language for infinitely ramified covers. Again: the medal recognizes infrastructure that makes such comparisons more geometric and more functorial.

Additional touchpoints often appear in surveys: local Shimura varieties, facets of the local Langlands program in geometric language, and prismatic cohomology (Bhatt–Scholze and collaborators)—a later evolution that builds on the perfectoid revolution. For this course, remember the pattern: **new spaces → better cohomology → arithmetic applications**.

---

## 5. Infrastructure prizes: parallel to foundations, not only to “solved conjectures”

Fields Medals sometimes highlight a single spectacular theorem (a packing problem, a conjecture closed). Scholze’s 2018 citation centers on transforming arithmetic geometry through perfectoid spaces—closer to **rewiring foundations** so that many theorems become accessible.

Useful comparisons inside this course:

| Style | Example in the course map | What is prized |
|-------|---------------------------|----------------|
| Close a sharp conjecture | [Viazovska packing]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/) | One decisive theorem (with beautiful method) |
| Complete a geometric program | [Perelman]({{ site.baseurl }}/contents/en/chapter02/02_03_Perelman_Poincare/) | Ricci flow + surgery finishes geometrization |
| Foundations / language | Scholze perfectoids; parts of [Langlands]({{ site.baseurl }}/contents/en/chapter02/02_02_Langlands_Program/) | New categories, equivalences, cohomology |

**Abel / lifetime parallel.** Prizes that honor lifelong foundational impact (e.g. representation theory, algebraic analysis, Langlands-related work in Abel narratives) share the “infrastructure” flavor even when the award ceremony differs. The pedagogical point is not to rank medals, but to recognize **different shapes of mathematical achievement**.

---

## 6. Condensed mathematics (light awareness)

With **Dustin Clausen**, Scholze developed **condensed mathematics**, a foundational framework treating topological algebraic objects (topological abelian groups, complete modules, …) via sheaves on profinite sets, aiming to repair poor formal behavior of naive topological algebra in homological settings. Analytic geometry in the condensed/liquid language is an ongoing program.

**Seminar rule.** Know the name and the motivation (topology + algebra + homological algebra need a better base category). Do **not** pretend condensed mathematics is required to state the 2018 Fields citation; it is a sequel chapter of the same foundational ambition.

---

## 7. Why it matters for a modern mathematics map

Perfectoid geometry changed how experts talk about highly ramified $$p$$-adic spaces. Students meeting arithmetic geometry after 2012 inherit a language in which infinite ramification is geometric rather than purely Galois-theoretic bookkeeping. Even if you never prove a tilting equivalence, knowing that **mixed characteristic can be tilted** is part of mathematical literacy for the 2020s.

**Accuracy notes.** Many theorems are collaborative; check coauthors. Not every advance in $$p$$-adic Hodge theory after 2012 is “because of perfectoids alone”—the field has many strands—but the perfectoid package is a central strand.

---

## Common confusions

| Claim | Correction |
|-------|------------|
| “Perfectoid spaces replace all schemes.” | They are a powerful class of adic/perfectoid objects, not a total replacement for schemes. |
| “Tilting erases number theory.” | It reorganizes arguments; arithmetic returns after transfer. |
| “Everything is now easy in char $$p$$.” | Tilting moves *some* problems; deep arithmetic still remains. |
| “Fields 2018 = condensed mathematics.” | The medal centers on perfectoid / $$p$$-adic breakthroughs; condensed work is later/parallel foundations. |
| “Only one person works in this area.” | Large collaborative community; always name coauthors for specific results. |
| “$$p$$-adic = same as real calculus with $$p$$.” | Nonarchimedean analysis has different topology and geometry. |

---

## Exercises

1. In one sentence, what is “mixed characteristic”?
2. Why might making Frobenius an isomorphism (perfect rings) simplify cohomology or ramification arguments?
3. State the tilting slogan without using the word “magic.”
4. Name two problem areas influenced by perfectoid methods and one area you should *not* casually claim is “solved by perfectoids” without a citation.
5. Compare, in a short table of your own, a “one conjecture” Fields story with Scholze’s infrastructure story (use another lecture from Ch.02).
6. **LO6 (≤250 words):** Critique a popular profile of Scholze for precision vs hype. Does it state a theorem or only adjectives?
7. Skim the introduction of Scholze’s *Perfectoid spaces* (or a survey) and list five keywords to learn next (e.g. adic space, untilt, almost mathematics, period sheaf, prism).
8. Stretch: how does the desire for better foundations here resemble—and differ from—the desire for better foundations in [category-flavored modern geometry]({{ site.baseurl }}/contents/en/chapter02/02_13_Pardon_Symplectic/) or algebraic topology? One careful paragraph.

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

- Read a non-technical profile *alongside* the first few pages of a technical survey; keep a two-column “media vs math” notebook (LO6 habit).
- Explore how local Langlands and Shimura varieties interact with modern $$p$$-adic geometry—gateway into research seminars.
- If you enjoy foundations, sample one expository talk on condensed mathematics after you can state tilting correctly.
- Contrast with [Venkatesh]({{ site.baseurl }}/contents/en/chapter02/02_07_Venkatesh_Number_Theory/): analytic/dynamical synthesis versus geometric/foundational rebuild—two different 2018 Fields styles.
