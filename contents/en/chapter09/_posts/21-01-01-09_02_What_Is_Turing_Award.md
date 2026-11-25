---
layout: post
title: "What Is the Turing Award?"
chapter: '09'
order: 2
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

In **1966**, when computers were still room-sized steel cabinets humming in university basements, the Association for Computing Machinery (ACM) decided to create an annual honor making a bold statement: computing was no longer just wiring circuits or writing payroll scripts—it had matured into a science with conceptual foundations rivaling physics and mathematics. They named the prize after **Alan Mathison Turing** (1912–1954), who had died twelve years earlier yet left an enduring mathematical blueprint in his 1936 paper *On Computable Numbers*. (One common trivia trap worth clearing up immediately: Alan Turing himself **never** received the award named after him!)

Today, the **A.M. Turing Award** is routinely described—sometimes carefully, sometimes as newspaper shorthand—as the **“Nobel Prize of computing.”** Official citations, biographies, lectures, and press materials live at [amturing.acm.org](https://amturing.acm.org/). This lecture is not a hall-of-fame quiz. It is a map of **what the Turing Award is for**, how its citation culture differs from the Fields Medal and the Abel Prize, and why a mathematics enthusiast should treat Turing citations as portals into **mathematical ideas**—computability, complexity, algorithms, cryptography, learning theory—rather than as prestige wallpaper.

---

## Learning objectives

After this lecture you should be able to:

- State what the ACM A.M. Turing Award is, when it began, and where to find official materials.
- Contrast **Turing**, **Fields**, and **Abel** on cadence, age rules, institutional home, and typical emphasis.
- Explain what a Turing **citation** emphasizes (foundational ideas, systems, theory, or field-shaping influence).
- Give three reasons a mathematics student should care about Turing-scale computing research.
- Extract mathematical objects from a short citation phrase and connect them to course chapters.
- Avoid treating “Nobel of computing” as a literal institutional claim.

**Prerequisites.** No research background in computer science is required. You should be comfortable reading short technical English and recognizing names of broad fields (algorithms, cryptography, logic, networks). Familiarity with the [Fields chapter overview]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/) and [Abel Prize overview]({{ site.baseurl }}/contents/en/chapter08/08_02_What_Is_Abel_Prize/) will sharpen comparisons.

**Cross-links.** Pair with [Chapter 09 Overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/) and [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/).

---

## Key ideas: What Is Computational Mathematics and What Do Turing Awards Study?

When a university graduate scans nearly sixty years of Turing Award winners, the list can look wildly eclectic: compiler builders, UNIX pioneers, relational database architects, and pure theorists proving theorems about expander graphs or prime numbers. What deeper thread unites them?

Modern computer science stands on **two interlocking legs**:
1. **The Theoretical Leg (Computational Mathematics):** constructing formal models of machines, defining complexity classes (P, NP, #P, BPP, IP), proving algorithms correct and fast, designing cryptographic protocols with mathematical security proofs, and establishing statistical and logical foundations for learning and causality.
2. **The Systems Leg (Computing Engineering):** turning those abstractions into real silicon architectures (RISC, GPUs), global networking (TCP/IP), database engines, computer graphics, and planetary-scale deep learning infrastructure.

In *Math Enthusiast*, Chapter 9 deliberately selects the **most mathematically rich** Turing Awards to spotlight the bridge between pure mathematics and computing. The clearest emblem of that unity is **Avi Wigderson**: he received the **2021 Abel Prize** (pure mathematics) and the **2023 Turing Award** (computer science) for the very same body of work on randomness, complexity, and expander graphs—proving that once a question goes deep enough, the border between the two disciplines dissolves.

---

## 1. Why the prize exists

Alan Turing’s 1936 paper *On Computable Numbers* made precise the idea of a general-purpose computational process and proved that some well-posed problems are **undecidable**. Later work on codes, early machines, and the philosophy of intelligence helped invent the conceptual world we now call computer science. Naming ACM’s top award after Turing is a statement about **origins**: computing is not only engineering gadgets; it is a science with theorems about what machines can and cannot do.

For most of the twentieth century, computing grew as an industrial and military technology *and* as a mathematical theory. Universities built departments; industry built platforms; pure mathematicians imported logic and discrete mathematics. The Turing Award, administered by ACM, creates an annual public focus on people whose ideas rewired that dual landscape—sometimes through elegant theory, sometimes through systems that became infrastructure, often through both.

Unlike the Fields Medal’s four-year ICM cadence or Abel’s Norwegian Academy framing of pure mathematics, Turing is explicitly a **computing** prize: software and hardware architectures, programming languages, databases, networks, AI, cryptography, complexity, and numerical methods all appear among laureates. The common thread is **lasting technical importance**, not a narrow purity filter.

---

## 2. Citation culture: how to read a Turing citation

Open a laureate page at [amturing.acm.org](https://amturing.acm.org/). You will typically find a short official citation, a longer technical description, a biographical note, and often a Turing Award lecture. The verbs tend to cluster around **foundational**, **pioneering**, **fundamental contributions**, and **for inventing / developing / establishing**.

Useful student practice:

1. **Circle the objects.** Turing machines? NP-completeness? Public-key protocols? Relational databases? Compilers? Neural nets?  
2. **Separate mechanism from fame.** “Invented RSA” is a slogan; the mechanism is modular arithmetic plus a factoring-based trapdoor intuition.  
3. **Ask what later work became easier.** Good citations change other people’s toolkits.  
4. **Link to a course chapter.** Complexity → Chapters 01 and 06; crypto → Chapters 03 and 06; logic → Chapter 05; discrete math → Chapter 08’s Wigderson arc.

Turing citations sometimes honor **systems that became ambient** (operating systems, languages, the Web’s protocols) and sometimes honor **theorems that became curricula**. Both can be mathematical: an architecture can embody a model of concurrency; a language design can crystallize type theory. Do not assume “systems award” means “no ideas.”

### Worked Example (Step by Step): Dissecting a Turing Citation into Concrete Arithmetic

When you read Shafi Goldwasser and Silvio Micali's 2012 Turing citation (*"transformative work that laid the complexity-theoretic foundations for the science of cryptography"*), don't skim past the adjectives. Peel open one core mechanism inside that sentence—**probabilistic encryption**—using tiny arithmetic modulo $$N = 3 \times 5 = 15$$:

- Suppose you want to encrypt a single secret bit $$b \in \{0, 1\}$$ (say `0 = Buy`, `1 = Sell`).
- If you use a *deterministic* function (like textbook RSA without random padding), encrypting `0` produces the exact same ciphertext every time—an eavesdropper seeing two identical ciphertexts immediately knows you repeated yesterday's trade!
- Goldwasser and Micali flipped the script using **quadratic residues modulo $$N = 15$$**: pick a fresh random number $$r$$ coprime to 15 (from $$\{1,2,4,7,8,11,13,14\}$$):
  - To encrypt bit `0`, send a square: $$c = r^2 \bmod 15$$ (choosing $$r=2 \implies c=4$$; choosing $$r=4 \implies c=1$$).
  - To encrypt bit `1`, multiply by a fixed non-square $$z = 2$$: send $$c = 2r^2 \bmod 15$$ (choosing $$r=2 \implies c=8$$; choosing $$r=4 \implies c=2$$).
- Result: encrypting `0` twice produces `4` the first time and `1` the second time! Anyone holding the secret factors $$p=3, q=5$$ checks whether $$c$$ is a square mod 3 and mod 5 in an instant, whereas an eavesdropper facing a 2048-bit modulus $$N$$ cannot distinguish encryptions of `0` from `1`. One crisp Turing citation just unpacked into a transparent mathematical engine.

### Explanation: A Four-Step Routine for Reading Any Turing Award

1. **Underline the technical nouns in the citation:** strip away ceremonial praise to isolate the mathematical objects (Turing machines, reductions, probabilistic encryption, causal graphs, pseudorandom generators).
2. **Locate the computational layer:** does the work live in *computability* (Turing), the *P vs NP frontier* (Cook–Karp), *efficiency inside P* (Knuth, Hopcroft–Tarjan), *security and interaction* (RSA, Goldwasser–Micali), or *learning and causality* (Valiant, Pearl)?
3. **Test it by hand on a toy instance:** run a 4-vertex graph, a $$2\times 2$$ matrix, or arithmetic mod 15 so you feel the mechanism click rather than memorizing a slogan.
4. **Ask what assumptions remain open:** every Turing Award opens a new frontier—identify what is still unproven (such as $$\mathbf{P} \neq \mathbf{NP}$$, hardness of integer factoring, or the derandomization conjecture $$\mathbf{BPP} = \mathbf{P}$$).

**Quick check.** A Turing Award honors **a new foundation or working language for an entire field**, not necessarily the resolution of a Millennium Prize Problem (Cook and Karp won for NP-completeness even though P vs NP remains open).

---

## 3. Fields, Abel, and Turing: a comparison table

Keep the three major honors distinct. Informal media often collapses them into a single “genius prize” metaphor.

| Honor | Institutional home | Cadence / age | Typical stage | Typical emphasis |
|-------|--------------------|---------------|---------------|------------------|
| **Fields Medal** | IMU / ICM | Every 4 years; under 40 | Pure mathematics | Breakthrough(s), often a flagship theorem early in a career |
| **Abel Prize** | Norwegian Academy of Science and Letters | Annual; no age limit | Pure mathematics | Lifetime / field-shaping body of work |
| **A.M. Turing Award** | ACM | Annual; no age limit | Computing (theory + systems) | Lasting technical importance to computing |

Two pedagogical distinctions matter.

First, **Turing is not “Fields for computer science.”** Some Turing work is theorem-heavy (Cook, Karp, Goldwasser–Micali, Diffie–Hellman culture); some is engineering-scale infrastructure; many careers mix both. Fields optimizes for early pure-math breakthroughs under an age constraint. Abel optimizes for lifetime pure-math climate change. Turing optimizes for lasting impact on *computing as a field*.

Second, **overlapping people and topics do not collapse the prizes.** Avi Wigderson’s world appears in Abel 2021 (with Lovász) and in complexity culture that Turing-scale cryptographers and complexity theorists inhabit. Cryptography links number theory (Chapter 03) to Turing awards (Diffie, Hellman, Rivest–Shamir–Adleman, Goldwasser–Micali). Shared mathematics is a feature of modern science, not a bug in award taxonomy.

---

## 4. Why mathematics enthusiasts should care

A mathematics student might ask: *If this is a computing prize, why is it in a math course?*

**First, origins are mathematical.** Computability, undecidability, and the Church–Turing thesis are logic and analysis of what “algorithm” means—siblings of Gödel’s incompleteness, not distant cousins of gadget catalogs. See the next lecture on [Turing, computability, and undecidability]({{ site.baseurl }}/contents/en/chapter09/09_03_Turing_Computability/) and [Gödel]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/).

**Second, complexity theory is pure mathematics with industrial consequences.** NP-completeness, reductions, and the still-open [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) problem are theorem-shaped. Cook and Karp’s Turing Awards (1982 and 1985) sit at the foundation of that subject.

**Third, cryptography is number theory and probability wearing a protocol jacket.** Diffie–Hellman, RSA, and the foundations of modern cryptographic definitions (semantic security, zero-knowledge) turn modular arithmetic and interactive proof into security guarantees. Those stories appear later in this chapter and in [number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/).

**Fourth, algorithms analysis is asymptotic mathematics.** Knuth’s *Art of Computer Programming* and the culture of rigorous average-case and worst-case analysis treat programs as mathematical objects. Big-$$O$$ culture is analysis, combinatorics, and discrete probability—not merely coding style.

**Fifth, shared open problems.** Whether randomness is essential, how quantum computers reshape hardness, whether P equals NP—these are mathematical questions with engineering stakes. Reading Turing citations trains you to see **mechanisms**, which is this course’s permanent habit.

---

## 5. A mini-tour of this chapter’s arc

The essays that follow sample Turing-scale ideas that a mathematics audience can own, not a complete chronology of ACM awards.

- **What is the Turing Award?** (this lecture) — institutional map and reading method.  
- **Turing, computability, undecidability** — the 1936 model, the halting problem, and the Entscheidungsproblem.  
- **Cook, Karp, and NP-completeness** — reductions, SAT, and the hard-problem zoo (Turing 1982 / 1985).  
- **Knuth and the analysis of algorithms** — rigorous asymptotics and *The Art of Computer Programming* (Turing 1974).  
- **Public-key cryptography** — Diffie–Hellman and RSA (Turing 2015 / 2002).  
- **Goldwasser, Micali, and modern crypto foundations** — probabilistic encryption, semantic security, zero-knowledge culture (Turing 2012).

Read them as a set: from **what can be computed at all**, to **what can be computed efficiently**, to **how we analyze algorithms**, to **how hardness becomes security**, to **how security is defined mathematically**.

---

## 6. How to study Turing essays in this course

Use a four-step method on every later lecture.

1. **Copy the citation phrase** from amturing.acm.org when you can.  
2. **Name the mathematical objects** (machines, languages, reductions, modular groups, interactive protocols).  
3. **State one explainable mechanism** in a paragraph a classmate could follow.  
4. **Write one cross-link** to Chapters 01–08 (problems, Fields, applications, beauty, proofs, frontiers, Abel).

Avoid two failure modes. The first is **celebrity without content**: listing award years without objects. The second is **overclaiming**: treating a Turing citation as if it closed every nearby open problem (NP-completeness culture ≠ P ≠ NP proved; public-key inventions ≠ quantum-safe forever).

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “The Turing Award is literally a Nobel Prize.” | Informal analogy only. Nobels are Swedish/Norwegian institutions with fixed categories; Turing is ACM’s top computing award. |
| “Turing only goes to pure theorists.” | Citations span theory, systems, languages, AI, networks, graphics, and more. |
| “Fields is for math; Turing is for coding.” | Both can be deeply mathematical; Turing’s stage is computing, which includes theorems about computation. |
| “If someone won Turing, their field has no open problems left.” | Awards highlight foundational impact; flagship questions (P vs NP, post-quantum security, etc.) often remain open. |
| “Alan Turing himself received the Turing Award.” | The award is named in his honor; he died in 1954, before the prize existed (first awarded 1966). |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/what-is-turing-award/`.

**From the research pack (must-know slogans)**

- ACM A.M. Turing Award: highest distinction in computing; often called “Nobel of computing.”
- Named after Alan Turing; administered by ACM; $1M prize (Google support historically).
- Contrast Fields / Abel (math) vs Turing (computing) — overlapping people (e.g. Wigderson Abel+Turing).
- Official: amturing.acm.org

**Recommended order**

1. **Orientation** — ACM Turing Award lectures playlist: [https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6](https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6).  

**Official / primary written hubs**

- ACM A.M. Turing Award home: https://amturing.acm.org/  
- Winners by year: https://amturing.acm.org/byyear.cfm  
- Alphabetical listing: https://amturing.acm.org/alphabetical.cfm  
- Abel Prize (contrast): https://abelprize.no/  

Complete URL bibliography: `research/video-research/what-is-turing-award/references.md`.

## References


### Video research pack (all URLs)

Complete list: `research/video-research/what-is-turing-award/references.md`.

1. ACM A.M. Turing Award home — https://amturing.acm.org/  
2. Winners by year — https://amturing.acm.org/byyear.cfm  
3. Alphabetical listing — https://amturing.acm.org/alphabetical.cfm  
4. ACM about the award — https://www.acm.org/about-acm/acm-history/acm-awards/turing-award  
5. Wikipedia — Turing Award — https://en.wikipedia.org/wiki/Turing_Award  
6. Wikipedia — Alan Turing — https://en.wikipedia.org/wiki/Alan_Turing  
7. Wikipedia — Association for Computing Machinery — https://en.wikipedia.org/wiki/Association_for_Computing_Machinery  
8. ACM Turing Award lectures playlist — https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6  
9. Abel Prize (contrast) — https://abelprize.no/  
10. Research pack folder: `research/video-research/what-is-turing-award/`.

1. Official site — citations, biographies, lectures: [ACM A.M. Turing Award](https://amturing.acm.org/).  
2. ACM — Association for Computing Machinery; award administration and announcements.  
3. Course cross-links: [Chapter 09 Overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/); [Fields overview]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/); [What Is the Abel Prize?]({{ site.baseurl }}/contents/en/chapter08/08_02_What_Is_Abel_Prize/); [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/).  
4. Historical context on Alan Turing: standard biographies and the 1936 computable-numbers paper (see next lecture).  
5. For comparison of pure-math awards: [abelprize.no](https://abelprize.no/).

---

## Further directions

- Compare this lecture’s table with the Abel comparison table in [08_02]({{ site.baseurl }}/contents/en/chapter08/08_02_What_Is_Abel_Prize/) and write three precise differences, not slogans.  
- Browse one full Turing Award lecture video or transcript and extract a single definition the laureate treats as central.  
- Note one open mathematical question still living next to any Turing theme in this chapter (P vs NP; discrete log / factoring vs quantum algorithms; average-case vs worst-case hardness).  
- Next: [Turing, Computability, and Undecidability]({{ site.baseurl }}/contents/en/chapter09/09_03_Turing_Computability/).

## Video tham khảo

- **xem trước** — [Celebrating 50 Years of the ACM A.M. Turing Award and Computing's Greatest Achievements](https://www.youtube.com/watch?v=MuTGa_xvCgc) — Association for Computing Machinery (ACM), English. Watch first. “Celebrating 50 Years of the ACM A.M. Turing Award and Computing's Greatest Achievements” orients the lesson’s aim: State what the ACM A.M. Turing Award is, when it began, and where to find official materials.
- [“Computer Science as a Major Body of Accumulated Knowledge,” at ACM Turing 50 Celebration](https://www.youtube.com/watch?v=ACsQ4ixtqTc) — Association for Computing Machinery (ACM), English. A second pass once the main claim is in view: State what the ACM A.M. Turing Award is, when it began, and where to find official materials.
- [Turing the Man](https://www.youtube.com/watch?v=nvwK-11uxSo) — Association for Computing Machinery (ACM), English. Further depth after the first two, still tied to this lesson: State what the ACM A.M. Turing Award is, when it began, and where to find official materials.
