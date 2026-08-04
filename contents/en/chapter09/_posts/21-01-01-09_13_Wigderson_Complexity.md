---
layout: post
title: "Wigderson: Randomness, Proofs, and Complexity (Turing 2023)"
chapter: '09'
order: 13
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

**Avi Wigderson** received the **A.M. Turing Award 2023** for foundational contributions to the theory of computation—especially **randomness in computation**, complexity theory, and the reshaping of theoretical computer science as a mathematical discipline. The same year he shared the **Abel Prize 2021** with László Lovász, a rare double spotlight: computing’s highest honor and pure mathematics’ lifetime prize for overlapping intellectual territory.

This lecture develops the Wigderson themes at seminar depth: randomness as a resource; **derandomization** and the hardness-versus-randomness paradigm; **interactive proofs** and the power of interaction and randomness in verification; expanders and pseudorandomness as bridges to discrete math; and how to read the Turing story *together with* the [Abel essay on Lovász & Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/). Official materials: [amturing.acm.org](https://amturing.acm.org/), [abelprize.no](https://abelprize.no/).

---

## Learning objectives

After this lecture you should be able to explain why randomness is treated as a computational resource comparable to time and space; state the derandomization slogan that suitable hardness assumptions imply efficient pseudorandom generators and collapse of randomized complexity toward deterministic classes; describe interactive proofs as a verification model beyond static NP witnesses; name expanders as sparse yet rapidly mixing graphs used as pseudorandom objects; and relate Turing 2023 to Abel 2021 without claiming either prize solved [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/).

**Prerequisites / seminar links.** [Complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/), [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [Yao / communication & minimax]({{ site.baseurl }}/contents/en/chapter09/09_08_Yao_Complexity/), [Abel Lovász–Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/), [graphs]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/). Chapter hub: [Turing overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/).

---

## 1. Two medals, one mathematical identity

Abel 2021 honored Lovász and Wigderson for making discrete mathematics and theoretical computer science **central modern mathematics**. Turing 2023 focuses the computing community’s lens on Wigderson’s complexity-theoretic leadership: randomness, circuit complexity connections, proof systems, algorithms, and decades of field-building (including the expository book *Mathematics and Computation*).

For Math Enthusiast, the dual award is pedagogical gold. Students who think “Turing = engineering” and “Abel = pure math” meet a counterexample: the same theorems about expanders, derandomization, and interactive proofs are **both**.

---

## 2. Randomness as a resource

A randomized algorithm may use coin flips. Classes such as **BPP** capture languages decidable in polynomial time with two-sided bounded error. Historically, randomness seemed to buy genuine power: polynomial identity testing, some graph algorithms, hashing, sampling, communication protocols ([Yao]({{ site.baseurl }}/contents/en/chapter09/09_08_Yao_Complexity/)).

Complexity theory asks sharper questions:

- Is randomness *essential*, or can every efficient randomized algorithm be simulated efficiently without coins?  
- What is the minimal number of random bits?  
- How does randomness interact with interaction, nonuniformity (circuits), and cryptographic pseudorandomness?

Wigderson’s body of work treats these as structural mathematics—not only algorithm engineering.

---

## 3. Hardness versus randomness

### Pseudorandom generators (PRGs)

A **PRG** stretches a short random seed into a long string that looks random to a class of efficient tests (circuits of bounded size). If strong PRGs exist, an algorithm that needs many random bits can instead enumerate seeds or use the stretched string and still succeed with comparable guarantees—**derandomization**.

### The paradigm

A deep theme of modern complexity:

> **Computational hardness** can be converted into **pseudorandomness**. If there are functions hard enough for circuits, one can build PRGs that fool smaller circuits, implying derandomization consequences such as $$\mathbf{BPP}$$ sitting in deterministic subexponential or even polynomial time under strong enough assumptions.

Conversely, nontrivial derandomization often implies circuit lower bounds. Hardness and randomness are two faces of one theory.

**Literacy caution.** These are **conditional** theorems and research programs. They do not, by themselves, resolve P vs NP. They show how a lower-bound world would yield algorithmic dividends—and how algorithmic derandomization ambitions pressure lower-bound research.

---

## 4. Interactive proofs

### Beyond NP certificates

In **NP**, a powerful prover sends a short witness; a polynomial-time verifier checks it statically. **Interactive proof systems** allow multiple rounds of communication, often with randomness in the verifier. The class **IP** equals **PSPACE** (Shamir; Lund–Fortnow–Karloff–Nisan lineage)—a landmark: interaction + randomness can verify languages believed far beyond NP.

### Zero knowledge and the culture of proofs

**Zero-knowledge proofs** convince a verifier that a statement is true without revealing anything else feasible to compute. They are central to cryptography and to the modern “proofs as protocols” worldview. Wigderson’s contributions and collaborations helped shape complexity-theoretic foundations of proof systems and randomness-efficient verification.

### Seminar moral

“Proof” in TCS is not only a static PDF of implications. It can be a **protocol** with soundness error and completeness error, analyzed like an algorithm. That conceptual shift is Turing-scale.

---

## 5. Expanders and pseudorandom objects

An infinite family of $$d$$-regular graphs is an **expander family** if small sets expand by a definite factor (equivalently, spectral gap bounded below independently of size). Expanders mix random walks rapidly despite sparsity—they are deterministic objects that **behave randomly**.

Uses include:

- derandomization and deterministic amplification;  
- error-correcting codes;  
- network design robustness;  
- pure math connections (groups, spectral geometry)—also visible in Abel narratives involving Margulis-type constructions ([Furstenberg–Margulis]({{ site.baseurl }}/contents/en/chapter08/08_05_Furstenberg_Margulis/) adjacency).

Wigderson’s world treats expanders as standard tools, the way analysts treat Fourier bases. See also the expander section of the [Abel Lovász–Wigderson lecture]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/).

---

## 6. Complexity as geometry of efficient computation

Wigderson’s expository program presents TCS topics—circuits, reductions, randomness, optimization, cryptography—as mathematics with definitions, theorems, and open problems of Hilbert-scale difficulty. [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) remains open; around it sit completed cathedrals: IP = PSPACE, PCP theorem and hardness of approximation, expander constructions, conditional derandomization theorems, communication complexity lower bounds.

For LO6: when popular writing says “complexity theory failed because P vs NP is open,” answer with a list of theorems that do not require that resolution. Lifetime prizes honor **architecture of a field**.

### Randomness-efficient error reduction

A concrete mini-theme: suppose a BPP algorithm uses many random bits and errs with probability $$1/3$$. Independent repetition reduces error exponentially but multiplies the bit cost. **Expander walks** and related pseudorandom objects can reduce error while recycling randomness more thriftily—deterministic graph structure substitutes for fresh coins. This is a miniature of the whole program: combinatorial constructions buy resource savings that naive probability would pay for with independent samples.

### Circuits, nonuniformity, and advice

Complexity distinguishes uniform algorithms (one machine for all lengths) from **circuit families** (possibly a different circuit per input length). Derandomization theorems often speak in circuit language because “tests” that a PRG must fool are nonuniform. Wigderson-style theory is comfortable moving between uniform classes (P, BPP) and nonuniform ones (P/poly), which is essential literacy for reading modern papers even if this seminar never builds a PRG from a hard function step by step.

### Zero knowledge as a definition of “knowing”

Beyond IP = PSPACE, **zero knowledge** formalizes convincing without teaching. That definition reshaped cryptography (identification protocols, modern proof systems) and philosophy-adjacent questions about knowledge. It is a flagship example of TCS exporting a *definition* as powerful as a theorem: once “zero knowledge” is precise, one can prove protocols achieve it under assumptions, compose them, and audit popular claims that a system “reveals nothing.”

### Reading Wigderson next to Yao

[Yao]({{ site.baseurl }}/contents/en/chapter09/09_08_Yao_Complexity/) emphasizes communication lower bounds and minimax transfers between randomized and distributional complexity. Wigderson emphasizes when randomness can be **removed** and when interaction enlarges proof power. Together they bookend randomness: sometimes coins are information-theoretically or complexity-theoretically necessary in a model; sometimes hardness manufactures coins good enough for efficient algorithms. Seminar synthesis prompt: pick one problem and argue whether you are in a “randomness helps / lower bound” mood or a “derandomize under hardness” mood.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “Turing 2023 / Abel 2021 solved P vs NP.” | No. Both honor foundational contributions; P vs NP is open. |
| “BPP is just P in practice, so randomness is uninteresting.” | Practical derandomization differs from proofs; the structural theory is deep and partly conditional. |
| “Interactive proofs are the same as NP certificates.” | Interaction and randomness change the verifier model; IP = PSPACE is a major theorem. |
| “Expanders are only random graphs.” | Random graphs often expand; the point includes **explicit** constructions and deterministic use. |
| “Derandomization means deleting probability from science.” | It means removing algorithmic dependence on random bits under resource bounds—not denying probabilistic models of data. |
| “Wigderson only does lower bounds.” | The program interlocks algorithms, pseudorandomness, proofs, and education. |

---

## Exercises

1. State one problem where a randomized algorithm is simpler or faster at slogan level.  
2. What is a PRG trying to fool, and why would that derandomize algorithms?  
3. Hardness vs randomness: explain the two-way street in ≤150 words.  
4. How does an interactive proof differ from a classical NP witness check?  
5. Define expander family in one sentence (expansion or spectral gap).  
6. **≤250 words:** Why can the same person win both Abel and Turing for related work? Use citation themes.  
7. List three TCS theorems that remain interesting even if P = NP (reuse Abel lecture discipline).  
8. Skim Wigderson’s Turing page at [amturing.acm.org](https://amturing.acm.org/) and Abel 2021 materials; write four keywords that appear in both narratives.

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/wigderson-complexity/`.

**From the research pack (must-know slogans)**

- **Turing Award year is 2023** (not 2021). Abel with Lovász was **2021**.
- Randomness as resource; hardness↔randomness; expanders; interactive proofs culture.
- Book *Mathematics and Computation*; dual Abel+Turing pedagogy.

**Recommended order**

1. **Core** — Wigderson Turing Award Lecture (ACM): [https://www.youtube.com/watch?v=f2NiGO8zC1c](https://www.youtube.com/watch?v=f2NiGO8zC1c).  
2. **Orientation** — IAS Q&A Wigderson Turing: [https://www.youtube.com/watch?v=TK_vD-VnsFw](https://www.youtube.com/watch?v=TK_vD-VnsFw).  
3. **Orientation** — CACM June 2024 Wigderson feature: [https://www.youtube.com/watch?v=Ur9XNF6TeYw](https://www.youtube.com/watch?v=Ur9XNF6TeYw).  
4. **Related** — Wigderson — Reading Alan Turing (Berkeley): [https://www.youtube.com/watch?v=BiFSUniv70c](https://www.youtube.com/watch?v=BiFSUniv70c).  
5. **Cross** — Abel lectures Lovász & Wigderson: [https://www.youtube.com/watch?v=zqiL57ebP-k](https://www.youtube.com/watch?v=zqiL57ebP-k).  

**Official / primary written hubs**

- Wigderson Turing 2023 page: https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
- Wigderson Turing lecture page: https://amturing.acm.org/vp/wigderson_3844537.cfm  
- Abel 2021 Lovász & Wigderson: https://abelprize.no/abel-prize-laureates/2021  

Complete URL bibliography: `research/video-research/wigderson-complexity/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/wigderson-complexity/transcripts/` · status: `research/video-research/wigderson-complexity/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/wigderson-complexity_f2NiGO8zC1c_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/wigderson-complexity/references.md`.

1. Wigderson Turing 2023 page — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
2. Wigderson Turing lecture page — https://amturing.acm.org/vp/wigderson_3844537.cfm  
3. Wigderson Turing Award Lecture (ACM) — https://www.youtube.com/watch?v=f2NiGO8zC1c  
4. IAS Q&A Wigderson Turing — https://www.youtube.com/watch?v=TK_vD-VnsFw  
5. CACM June 2024 Wigderson feature — https://www.youtube.com/watch?v=Ur9XNF6TeYw  
6. Wigderson — Reading Alan Turing (Berkeley) — https://www.youtube.com/watch?v=BiFSUniv70c  
7. Abel 2021 Lovász & Wigderson — https://abelprize.no/abel-prize-laureates/2021  
8. Abel lectures Lovász & Wigderson — https://www.youtube.com/watch?v=zqiL57ebP-k  
9. Wikipedia — Avi Wigderson — https://en.wikipedia.org/wiki/Avi_Wigderson  
10. byyear listing (confirm 2023) — https://amturing.acm.org/byyear.cfm  
11. Mathematics and Computation (book info) — https://www.math.ias.edu/avi/book  
12. Research pack folder: `research/video-research/wigderson-complexity/`.

1. ACM Turing Award 2023 — Avi Wigderson — [amturing.acm.org](https://amturing.acm.org/).  
2. Abel Prize 2021 — Lovász & Wigderson — [abelprize.no](https://abelprize.no/).  
3. A. Wigderson, *Mathematics and Computation* (Princeton); Arora–Barak, *Computational Complexity*; Vadhan surveys on pseudorandomness.  
4. Course: [Abel Lovász–Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/); [complexity]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/); [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/); [Yao]({{ site.baseurl }}/contents/en/chapter09/09_08_Yao_Complexity/).

---

## Further directions

- Read one chapter of *Mathematics and Computation* as a pure-math audience piece.  
- Compare Yao minimax lower-bound method with PRG-based derandomization upper-bound ambitions.  
- Study a concrete expander construction sketch (even Margulis-type existence/explicitness history).  
- After IP = PSPACE awareness: peek at PCP theorem’s role in approximation hardness.  
- Next: [Modern themes survey]({{ site.baseurl }}/contents/en/chapter09/09_14_Modern_Themes/)—privacy, optimization/ML theory, coding, quantum algorithms, verification.
