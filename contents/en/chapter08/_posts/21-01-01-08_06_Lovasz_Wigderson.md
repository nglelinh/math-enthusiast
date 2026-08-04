---
layout: post
title: "Lovász & Wigderson: Discrete Math and Theoretical CS (Abel 2021)"
chapter: '08'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter08
lesson_type: required
---

The **Abel Prize 2021** was awarded jointly to **László Lovász** and **Avi Wigderson**

> “for their foundational contributions to theoretical computer science and discrete mathematics, and their leading role in shaping them into central fields of modern mathematics.”  
> — [Abel Prize Committee citation](https://abelprize.no/abel-prize-laureates/2021)

This lecture explains why discrete mathematics and theoretical computer science (TCS) earned a “core pure math” lifetime prize; what the **Lovász local lemma**, graph theory, and combinatorial optimization contribute; what **randomness, derandomization, expanders, and computational complexity** contribute in Wigderson’s world; and how to place the prize next to the still-open [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) problem without confusion. Official materials: [abelprize.no](https://abelprize.no/).

---

## Learning objectives

After this lecture you should be able to explain why discrete math/TCS earned an Abel-scale recognition as central modern mathematics; name the Lovász local lemma and its purpose (existence amid many mostly independent bad events); state Wigderson’s randomness / derandomization theme; describe expanders as sparse yet highly connected graphs; and relate all of this to P vs NP **without** claiming that problem is solved.

**Prerequisites.** Graphs at the level of vertices and edges; basic probability (independence, union bounds); the idea that algorithms consume time as a function of input size. Cross-links: [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [graph theory & networks]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/), [Furstenberg–Margulis expanders mention]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/).

---

## 1. A cultural prize as well as a scientific one

Graphs, algorithms, and complexity were once treated as peripheral to “core” pure mathematics in some institutional cultures—important, yes, but siloed in computer science departments. Abel 2021 is a public affirmation that these areas host **deep structure theorems** and interact with geometry, algebra, and probability at the highest level.

The citation’s second clause matters: “shaping them into central fields of modern mathematics.” That is field-building, mentorship, books, problems lists, and decades of theorems—not a single headline result.

---

## 2. Lovász: discrete mathematics as a mathematical science

### Graphs, optimization, and geometry

Lovász’s work spans graph theory, combinatorial optimization, and geometric representations of graphs. A recurring theme is that discrete objects carry continuous shadows: embeddings, semi-definite relaxations, lattice algorithms, and later the culture of **graph limits** (graphons) that he helped enable. Optimization over combinatorial structures becomes a rigorous mathematical science with duality, algorithms, and hardness.

### The Lovász local lemma

The **local lemma** (Erdős–Lovász) is a profound existence principle. Suppose you have many “bad events” $$A_i$$, each of small probability, and each depending on only a limited number of others. Then, under quantitative hypotheses, the probability that **none** of the bad events occur is still positive:

$$
\mathbb{P}\Big(\bigcap_i A_i^c\Big) > 0.
$$

Union bounds fail when there are too many events; independence assumptions fail when there is some dependence. The local lemma thrives in the intermediate regime: **limited dependence**. It is a workhorse in combinatorics, probabilistic method, and algorithm design (including algorithmic versions developed later by others).

### Field-building

Beyond theorems, Lovász’s influence includes shaping discrete mathematics as a discipline with standards of proof, connections to geometry and optimization, and a global research community. Abel language about “leading role” points here.

---

## 3. Wigderson: randomness, complexity, and pseudorandomness

### Randomness as a resource

A central Wigderson theme: when do **randomized algorithms** outperform deterministic ones, and what is the power of randomness as a computational resource? Many algorithms flip coins—Monte Carlo primality tests historically, hashing, sampling, communication protocols. Complexity theory asks whether that randomness is essential or merely convenient.

### Derandomization

**Derandomization** asks when randomness can be removed—often under **hardness assumptions** (suitable hard functions imply pseudorandom generators). If the world contains enough computational hardness, then efficient deterministic simulations of randomized algorithms may exist. This links complexity lower bounds to algorithm design in a deep way.

### Expanders, interactive proofs, and bridges to pure math

**Expander graphs** are sparse yet highly connected—random-like mixing with few edges. They appear in derandomization, coding theory, network design, and pure group theory (explicit constructions historically include Margulis-type expanders). Wigderson’s world treats expanders and related objects as **pseudorandomness incarnate**.

Interactive proofs, zero-knowledge, and the structure of complexity classes form another major arc—bridges between logic, algebra, and algorithms. Wigderson’s book *Mathematics and Computation* presents TCS as mathematics for a broad audience of mathematicians.

---

## 4. Expanders: a junction map

An infinite family of $$d$$-regular graphs $$\{G_n\}$$ is an **expander family** if the spectral gap (or Cheeger constant) is bounded below independently of $$n$$. Equivalently, small sets expand: neighborhood sizes grow by a definite factor.

Consequences:

- random-walk mixing is fast;  
- error-correcting codes and derandomization gain explicit objects;  
- pure mathematics gains spectral graph theory and group-theoretic constructions.

Lovász’s structural/geometric graph theory and Wigderson’s pseudorandomness meet at expanders. Abel 2021 sits at that junction—and Abel 2020’s Margulis already touched expanders from dynamics/groups.

---

## 5. Beside P vs NP

[P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) remains open. Abel 2021 does **not** resolve it. Lovász–Wigderson work is the **toolkit and worldview** surrounding computational hardness: positive results, structural theory, randomness, optimization, and the mathematical legitimacy of discrete complexity.

A healthy seminar habit: list three “positive” TCS theorems that do not need a resolution of P vs NP (local lemma applications; expander constructions; interactive proof theorems; approximation algorithms under complexity assumptions; …). Lifetime mathematics includes the architecture of a field, not only its Everest.

### Hardness as a mathematical object

Even without settling P vs NP, complexity theory treats **hardness** as something one can *use*: reductions, completeness, conditional lower bounds, and cryptographic assumptions. Wigderson’s program often turns hardness into a constructive resource—pseudorandom generators that fool efficient tests—so that algorithmic design and lower-bound thinking become two faces of one subject. Lovász’s combinatorial optimization similarly treats discrete structure as geometry: polytopes, dualities, and approximation thresholds that are theorems, not mere heuristics.

For this course, the moral is aligned with Chapter 01’s open problems: **an unsolved flagship does not make a field empty**. Around P vs NP sits a mature mathematical civilization.

---

## 6. Why this is Abel-scale

Two careers, one message: discrete mathematics and TCS are not second-class citizens in pure mathematics. They have:

- deep theorems with geometric and algebraic content;  
- methods exported to other fields;  
- open problems of Hilbert-scale difficulty (P vs NP among them);  
- infrastructures (expanders, pseudorandom generators, combinatorial lemmas) used across sciences.

The Abel committee’s wording—“central fields of modern mathematics”—is the thesis of this lecture.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “Abel 2021 solved P vs NP.” | No. The prize honors foundational contributions and field-shaping; P vs NP is open. |
| “Discrete math is only algorithms.” | It includes structural graph theory, extremal combinatorics, optimization theory, and more. |
| “Randomized algorithms are always better.” | Randomness is a resource with costs and with derandomization programs; it is not magic. |
| “Expanders are just random graphs.” | Random graphs often expand; the point is **explicit** constructions and deterministic use. |
| “Local lemma needs full independence.” | It needs **limited dependence**, carefully quantified. |

---

## Exercises

1. State the Lovász local lemma in one sentence for a non-specialist.  
2. Give an example where randomness helps an existence proof or algorithm (even a toy example).  
3. What is derandomization trying to achieve? ≤100 words.  
4. **≤250 words:** Argue that TCS is pure mathematics using Abel 2021’s citation language.  
5. Link to [graphs & networks]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/) and write one sentence connecting expanders to network reliability intuition.  
6. After the P vs NP lesson: list three positive TCS theorems that do not require P ≠ NP.

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/lovasz-wigderson/`.

**From the research pack (must-know slogans)**

- Abel 2021: foundational contributions to TCS and discrete math; shaping them into central modern mathematics.
- Lovász: graph theory, optimization, local lemma, geometric graph theory.
- Wigderson: randomness, complexity, expanders, proof systems — later **Turing Award 2023** (not 2021).
- Does **not** solve P vs NP.

**Recommended order**

1. **Core** — Abel lectures Lovász & Wigderson: [https://www.youtube.com/watch?v=zqiL57ebP-k](https://www.youtube.com/watch?v=zqiL57ebP-k).  
2. **History** — Abel interview Lovász & Wigderson: [https://www.youtube.com/watch?v=VAk0rtlKtMA](https://www.youtube.com/watch?v=VAk0rtlKtMA).  
3. **Orientation** — WFSJ meet Lovász & Wigderson: [https://www.youtube.com/watch?v=J4yssMTZqC4](https://www.youtube.com/watch?v=J4yssMTZqC4).  
4. **Orientation** — Short interview Lovász: [https://www.youtube.com/watch?v=wg0di8dK0eI](https://www.youtube.com/watch?v=wg0di8dK0eI).  
5. **Orientation** — Short interview Wigderson: [https://www.youtube.com/watch?v=5VxOhzNv9To](https://www.youtube.com/watch?v=5VxOhzNv9To).  

**Official / primary written hubs**

- Abel 2021 Lovász & Wigderson: https://abelprize.no/abel-prize-laureates/2021  
- ACM Turing — Wigderson 2023: https://amturing.acm.org/award_winners/wigderson_3844537.cfm  

Complete URL bibliography: `research/video-research/lovasz-wigderson/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/lovasz-wigderson/transcripts/` · status: `research/video-research/lovasz-wigderson/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/lovasz-wigderson_zqiL57ebP-k_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/lovasz-wigderson/references.md`.

1. Abel 2021 Lovász & Wigderson — https://abelprize.no/abel-prize-laureates/2021  
2. Abel lectures Lovász & Wigderson — https://www.youtube.com/watch?v=zqiL57ebP-k  
3. Abel interview Lovász & Wigderson — https://www.youtube.com/watch?v=VAk0rtlKtMA  
4. WFSJ meet Lovász & Wigderson — https://www.youtube.com/watch?v=J4yssMTZqC4  
5. Short interview Lovász — https://www.youtube.com/watch?v=wg0di8dK0eI  
6. Short interview Wigderson — https://www.youtube.com/watch?v=5VxOhzNv9To  
7. NYT Abel 2021 — https://www.nytimes.com/2021/03/17/science/abel-prize-mathematics.html  
8. Nature Abel 2021 — https://www.nature.com/articles/d41586-021-00694-9  
9. ACM Turing — Wigderson 2023 — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
10. Wikipedia — Avi Wigderson — https://en.wikipedia.org/wiki/Avi_Wigderson  
11. Research pack folder: `research/video-research/lovasz-wigderson/`.

1. Abel Prize 2021 — [abelprize.no/abel-prize-laureates/2021](https://abelprize.no/abel-prize-laureates/2021).  
2. A. Wigderson, *Mathematics and Computation* (Princeton).  
3. N. Alon–J. Spencer, *The Probabilistic Method*; S. Arora–B. Barak, *Computational Complexity*.  
4. Course: [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/); [graphs]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/).

---


## Hardness as a mathematical object

Theoretical computer science treats **computational hardness** not as an annoyance but as a resource and a structure theory. One-way functions (if they exist) enable cryptography; average-case hardness differs from worst-case NP-completeness; fine-grained hypotheses refine P vs NP into precise running-time barriers. Lovász’s combinatorial geometry and Wigderson’s complexity worldview together show discrete mathematics generating **definitions as deep as any continuum theory**.

## Seminar prompt

List three theorems in TCS that remain interesting even if P = NP (e.g. communication complexity lower bounds, or coding theory limits). Explain why in two sentences each.

## Further directions

- Local lemma exercise: invent a toy bad-event setup (coloring, packing, scheduling).  
- Compare expander constructions historically (Margulis; later zigzag products; Ramanujan graphs).  
- Compare with a related [Fields essay]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/).  
- Note one precise open question: P vs NP; stronger derandomization; explicit constructions with optimal parameters.  
- Next: [Dennis Sullivan]({{ site.baseurl }}/contents/en/chapter08/08_07_Sullivan_Topology/).
