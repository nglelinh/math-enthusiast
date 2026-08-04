---
layout: post
title: "Modern Themes: Algorithms, Systems, and the Math–CS Border"
chapter: '09'
order: 14
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

Not every idea that reshapes the mathematics of computation fits a single Turing Award year. This **survey lecture** maps living research themes at the border of mathematics and computer science: **differential privacy**, **optimization and ML theory**, **coding theory**, **quantum algorithms** (awareness), and **verification**. It is also a practical guide to reading citations and lectures on [amturing.acm.org](https://amturing.acm.org/) without drowning in résumé noise—and a closing map that sends you back through earlier course chapters.

Treat this as a **compass**, not an encyclopedia. Each section states a definition-level slogan, one reason mathematicians care, and a cross-link. Depth lives in the flagship lectures elsewhere in the course; here you practice **orientation and LO6 hygiene**.

---

## Learning objectives

After this lecture you should be able to name five modern math–CS themes (privacy, optimization/ML theory, coding, quantum algorithms awareness, verification) with one correct mechanism sentence each; explain differential privacy as a stability property of randomized mechanisms under neighboring datasets; relate optimization and generalization questions to [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/) and [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/); describe coding theory as reliable communication under noise with rate–distance tradeoffs; state what formal verification tries to guarantee; and use amturing.acm.org pages to extract *ideas* rather than only award years.

**Prerequisites / seminar links.** The chapter’s prize essays (Yao through Wigderson); [complexity]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/); [cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/); [quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/); [networks]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/). Overview: [Turing chapter]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/).

---

## 1. How to read a Turing citation (and this chapter)

### A method

On [amturing.acm.org](https://amturing.acm.org/), open a laureate page and extract:

1. **Objects** — what mathematical objects appear (circuits, protocols, graphs, nets, lattices, …)?  
2. **Resources** — time, space, randomness, communication, quantum gates, samples?  
3. **Guarantees** — worst-case, average-case, high probability, cryptographic negligible error?  
4. **Export** — which other fields use the idea (crypto, ML, databases, hardware)?  
5. **Open edge** — what did the work *not* settle?

Ignore banquet rhetoric until those five are filled. The same method works for Abel and Fields citations in Chapters 8 and 2.

### This survey’s role

Prize essays highlight people. Themes highlight **problems that outlive a year**. Differential privacy was shaped by many researchers; optimization for ML is a community; coding theory is a century-scale arc; quantum algorithms continue post-Shor; verification spans logic and systems. Turing history is one entrance; the border is wider.

---

## 2. Differential privacy

### Slogan

A randomized mechanism $$M$$ is **$$\varepsilon$$-differentially private** (pure DP) if for all neighboring datasets $$D,D'$$ (differing by one record, under a fixed adjacency relation) and all measurable sets $$S$$ of outputs,

$$
\mathbb{P}(M(D)\in S) \le e^{\varepsilon}\, \mathbb{P}(M(D')\in S).
$$

Approximate DP adds a small $$\delta$$ slack. Intuition: an individual’s presence barely changes the output distribution; privacy is a **stability** property, not merely “hide names.”

### Why mathematics

DP brings composition theorems, group privacy, conversion between divergence notions, and optimal noise mechanisms (Laplace, Gaussian) under sensitivity bounds. It is analysis + probability + algorithm design. Database reconstruction attacks motivate *why* ad hoc anonymization fails—connecting to information theory and complexity-flavored hardness of privacy.

### Course bridge

Statistics and [probability]({{ site.baseurl }}/contents/en/chapter03/03_04_Probability_Data_Science/); cryptographic threat models ([crypto]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/)); LO6 when a product claims “privacy-preserving AI” without a DP (or similar) definition.

---

## 3. Optimization and ML theory

### Slogan

Modern ML trains models by **iterative optimization** of empirical objectives, while **learning theory** asks when the result generalizes. The math–CS border here includes convex and nonconvex optimization, stochastic approximation, implicit bias of gradient methods, landscape analysis, and generalization bounds that may be algorithm-dependent.

### Why mathematics

Convergence rates, step-size schedules, and high-dimensional probability are theorems under hypotheses—even when deep learning practice runs ahead of tight bounds. Overparameterization changed the questions: interpolation, double descent as empirical regularity, and the search for non-vacuous certificates.

### Course bridge

[Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/), [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/), [optimization]({{ site.baseurl }}/contents/en/chapter03/03_07_Optimization_Operations_AI/), [Valiant PAC]({{ site.baseurl }}/contents/en/chapter09/09_09_Valiant_Learning/), [deep learning trio]({{ site.baseurl }}/contents/en/chapter09/09_12_Deep_Learning_Trio/). Seminar skill: label each sentence as theorem, empirical regularity, or engineering report.

---

## 4. Coding theory

### Slogan

An **error-correcting code** is a subset $$C\subseteq\Sigma^n$$ used to encode messages so that after noisy corruption, decoding recovers the message if few coordinates flip (or erase). Fundamental tradeoffs link **rate** (efficiency) and **distance** (noise tolerance). Shannon’s noisy-channel theorems give probabilistic existence and capacity; algorithmic coding seeks explicit codes with efficient encode/decode.

### Why mathematics

Algebraic geometry codes, expander codes, polar codes, LDPC ensembles, list decoding—each is a mathematical industry. Complexity enters via decoding hardness and cryptographic applications of noisy problems. Pseudorandomness and expanders ([Wigderson]({{ site.baseurl }}/contents/en/chapter09/09_13_Wigderson_Complexity/)) reappear as code constructions.

### Course bridge

Information and probability; [networks]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/) for graphical codes; cryptography’s error-oriented primitives; quantum error correction as a parallel tower in [quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/).

---

## 5. Quantum algorithms (awareness)

### Slogan

Quantum algorithms act on state vectors in $$\mathbb{C}^{2^n}$$ with unitary gates and measurement. **Shor’s algorithm** places integer factoring in **BQP**; **Grover’s algorithm** gives quadratic speedups for unstructured search. Quantum does **not** mean “NP-complete problems become easy” as a theorem.

### Why mathematics

Linear algebra, representation-ish structure of Fourier sampling over abelian groups, query complexity, and quantum complexity classes. Post-quantum cryptography redesigns public-key assumptions ([future crypto]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/)).

### Course bridge

[Quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/), [complexity]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/), [Yao]({{ site.baseurl }}/contents/en/chapter09/09_08_Yao_Complexity/) for early model-awareness. LO6: separate qubit-count press releases from asymptotic complexity statements.

---

## 6. Verification

### Slogan

**Formal verification** aims to prove that a system (hardware, compiler, protocol, concurrent program) satisfies a specification—safety (“bad states unreachable”), liveness, security properties—using logic, model checking, type systems, or interactive theorem provers. Testing shows presence of bugs; verification aims at proofs relative to models and specs.

### Why mathematics

Temporal logics, decision procedures, SMT solvers, abstract interpretation, and proof assistants (Coq, Lean, Isabelle, …) are logic and algorithms braided together. The math–CS border includes both undecidability barriers and spectacular successes on chips, compilers, and increasingly cryptographic protocols and distributed systems.

### Course bridge

[Gödel / limits of formal methods culture]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/) as intellectual humility (undecidability and incompleteness constrain universal dreams); complexity of model checking fragments; software correctness as a different *kind* of guarantee than statistical ML metrics.

**LO6.** “Formally verified” always means: verified **relative to** a spec and assumptions. Spec bugs are still bugs.

---

## 7. A walk back through the course map

| Theme | Chapter anchors |
|-------|-----------------|
| Hardness, P vs NP, classes | Ch.1 P vs NP; Ch.6 complexity; Yao, Valiant #P, Wigderson |
| Graphs & algorithms | Ch.3 networks; Hopcroft–Tarjan; expanders in Abel/Turing |
| Crypto & privacy | Ch.3 crypto; Ch.6 future crypto; DP in this survey |
| Learning & AI math | Ch.6 AI & ML theory; Valiant; deep learning trio; Pearl causality |
| Probability & high dimension | Ch.3 probability; Ch.6 high-dim geometry; concentration (Abel Talagrand) |
| Quantum | Ch.6 quantum; brief Yao/Wigderson adjacency |
| Proofs & foundations | Ch.5 famous proofs; interactive proofs; verification |

Chapter 9’s prize essays are **doors**. The rooms are the whole site.

### Systems that force definitions

Several modern themes share a pattern: **deployment pressure creates mathematical definitions**. Census and ad-tech pressure created demand for DP-style guarantees; unreliable channels created coding theory; chip bugs and protocol failures created verification cultures; large models created urgency around generalization and alignment-adjacent specifications (still partly informal). The math–CS border is not only “CS borrows math tools.” It is often “society needs a guarantee, and only a definition plus theorems will do.”

That pattern matches the prize essays: PAC made learning theorem-shaped; causal graphs made intervention theorem-shaped; communication complexity made bandwidth theorem-shaped. When you meet a new buzzword in 2026 media, ask whether it yet has a definition with composition properties—or only a demo.

### A short reading recipe for the rest of the site

1. Open a Turing or Abel citation; extract objects, resources, guarantees.  
2. Jump to the matching course chapter (table above).  
3. Write one LO6 sentence: what popular wording gets wrong.  
4. Write one LO4 sentence: a mechanism, not a brand name.  
5. Only then decide whether a deep dive (A3/A4/A6 material) is worth your week.

This survey ends the numbered Turing-arc lessons; your map should now be usable without memorizing award years.

---

## 8. Confusions

| Claim | Correction |
|-------|------------|
| “Modern CS theory is only deep learning.” | Privacy, coding, verification, quantum, complexity remain central mathematical CS. |
| “Differential privacy means data are encrypted.” | DP is distributional stability of outputs; encryption is a different tool. |
| “Quantum computers break all crypto / solve NP-complete problems.” | Shor targets specific structures (e.g. factoring/discrete log style); NP-complete generic hardness is not known to collapse into BQP. |
| “Verified software cannot fail.” | Proofs are relative to specs, models, and trusted kernels. |
| “If it is not a Turing Award topic, it is not foundational.” | Awards are spotlights; fields are larger than any medal list. |
| “Survey knowledge replaces flagship depth.” | Orientation helps; flagship lectures still do the deep work. |

---

## Exercises

1. Write the pure DP inequality and explain “neighboring datasets” in one sentence.  
2. Give one theorem-shaped question and one benchmark-shaped question about deep learning.  
3. Rate vs distance for codes: why is there a tradeoff at slogan level?  
4. Name a problem in BQP of cryptographic interest and one misconception about BQP.  
5. What does a model checker need as input besides the system model?  
6. Using amturing.acm.org, pick any laureate not essayed in this chapter; fill the five-point reading method.  
7. **≤250 words:** Draw a personal map from this survey to three earlier course chapters with mechanism sentences (LO4 practice).  
8. **LO6:** Find a product claim about “private,” “quantum-secure,” or “verified” and rewrite it with missing definitions inserted.

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/modern-themes/`.

**From the research pack (must-know slogans)**

- Survey hub: complexity, crypto, learning, causality, randomness, algorithms.
- Recent Turing themes include quantum information (e.g. 2025 Bennett–Brassard announcement culture).
- Use official by-year list to update seminar readings each year.

**Recommended order**

1. **Orientation** — Quanta P vs NP: [https://www.youtube.com/watch?v=pQsdygaYcE4](https://www.youtube.com/watch?v=pQsdygaYcE4).  

**Official / primary written hubs**

- Turing winners by year: https://amturing.acm.org/byyear.cfm  
- Turing Award home: https://amturing.acm.org/  
- Wigderson 2023 (randomness): https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
- Deep learning 2018 trio hub via Hinton: https://amturing.acm.org/award_winners/hinton_4791679.cfm  
- Goldwasser 2012: https://amturing.acm.org/award_winners/goldwasser_8627889.cfm  
- Abel Prize (math lifetime contrast): https://abelprize.no/  

Complete URL bibliography: `research/video-research/modern-themes/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/modern-themes/transcripts/` · status: `research/video-research/modern-themes/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/modern-themes_pQsdygaYcE4_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/modern-themes/references.md`.

1. Turing winners by year — https://amturing.acm.org/byyear.cfm  
2. Turing Award home — https://amturing.acm.org/  
3. Wigderson 2023 (randomness) — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
4. Deep learning 2018 trio hub via Hinton — https://amturing.acm.org/award_winners/hinton_4791679.cfm  
5. Goldwasser 2012 — https://amturing.acm.org/award_winners/goldwasser_8627889.cfm  
6. Quanta P vs NP — https://www.youtube.com/watch?v=pQsdygaYcE4  
7. Abel Prize (math lifetime contrast) — https://abelprize.no/  
8. Clay Millennium problems — https://www.claymath.org/millennium-problems/  
9. Wikipedia — Theoretical computer science — https://en.wikipedia.org/wiki/Theoretical_computer_science  
10. ACM Turing lectures playlist — https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6  
11. Research pack folder: `research/video-research/modern-themes/`.

1. ACM Turing Award site — [amturing.acm.org](https://amturing.acm.org/) (citation reading practice).  
2. Dwork–Roth, *The Algorithmic Foundations of Differential Privacy*; standard coding theory texts (MacWilliams–Sloane; modern lecture notes); Sipser/Arora–Barak for complexity; quantum surveys in Nielsen–Chuang or course notes; model checking / formal methods surveys.  
3. Course anchors: [AI math]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/); [ML theory]({{ site.baseurl }}/contents/en/chapter06/06_10_ML_Theory/); [complexity]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/); [quantum]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/); [crypto]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/); [Wigderson Turing essay]({{ site.baseurl }}/contents/en/chapter09/09_13_Wigderson_Complexity/).

---

## Further directions

- Implement Laplace mechanism on a toy counting query and empirically test distinguishability.  
- Read one short note on list decoding or polar codes after information-theory curiosity.  
- Compare DP composition to cryptographic hybrid arguments as “security accounting.”  
- Try a proof assistant tutorial (Lean or Coq) for a tiny theorem—verification as lived mathematics.  
- Synthesis: prepare A6-style paragraphs linking two Turing essays to one modern theme above.  
- Return to [chapter overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/) and re-read with the five-point citation method.
