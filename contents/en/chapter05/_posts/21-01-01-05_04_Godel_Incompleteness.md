---
layout: post
title: "Gödel’s Incompleteness Theorems"
chapter: '05'
order: 4
owner: Nguyen Le Linh
lang: en
categories:
- chapter05
---

In September 1930, in the Prussian city of Königsberg—the very birthplace of Euler’s seven bridges—the titan of mathematics **David Hilbert** closed his retirement address with a rallying cry echoed across the century: *"Wir müssen wissen, wir werden wissen"* — *"We must know, we will know."* His lifelong vision (Hilbert’s Program) aimed to build a complete, airtight system of axioms that would never contradict itself and could prove or refute **every** mathematical claim.

The irony of history was instantaneous: the very day before, at a quiet roundtable at the same conference, a soft-spoken 24-year-old Viennese logician named **Kurt Gödel** had calmly announced a result that shattered that dream forever.

**Gödel’s incompleteness theorems** (1931) do not say "mathematics is broken" or "nothing can be proved." They state something far sharper: any consistent, effectively axiomatized formal system strong enough to express elementary arithmetic is **necessarily incomplete** (some true arithmetic statements can neither be proved nor refuted inside it), and such a system **cannot prove its own consistency** from within.

**Lesson roadmap:** Key ideas (syntax vs. semantics, formal systems PA/ZFC, computability) → Formal theories and the two theorems → Explanation: hand-encoding and decoding Gödel numbers ($$270$$ and $$808\,500$$) → From the Liar Paradox to the self-referential Gödel sentence $$G$$ → The second theorem → Diagonal kinship with Cantor and Turing.

---

## Learning objectives

After this lecture you should be able to:

- State informal but accurate versions of Gödel’s first and second incompleteness theorems.
- Explain Gödel numbering as “syntax becomes arithmetic.”
- Describe the self-referential sentence at slogan level (“I am not provable”) and why consistency makes it true yet unprovable.
- Distinguish incompleteness from inconsistency, and from undecidability in the computability sense (related but not identical).
- Avoid popular misreadings (relativism about all truth; claims that human minds transcend machines without further argument).
- Connect the argument’s diagonal flavor to Cantor and to later computability results.

**Prerequisites.** Comfort with the idea of formal proof as a finite string of symbols following rules; basic arithmetic. No prior logic course is assumed; we stay at idea level.

---

## Key ideas: Mathematical Logic, Formal Proofs, and Computability

Many university graduates hear about Gödel’s theorems in philosophy essays yet feel hazy on the mechanics because three pillars of **Mathematical Logic** are rarely laid out side by side:

### 1. Syntax ($$\vdash$$) vs. Semantics ($$\models$$)
Mathematical logic draws a razor-sharp wall between two worlds:
- **Syntax ($$\vdash$$):** A purely mechanical symbol game. Starting from a fixed list of starting strings (*axioms*), you apply finite mechanical inference rules to produce new strings. Writing $$T \vdash \varphi$$ means *"there exists a valid step-by-step derivation of $$\varphi$$ inside system $$T$$"*—with no appeal to what the symbols "mean."
- **Semantics ($$\models$$):** Whether the statement $$\varphi$$ is actually **true** in the real world of natural numbers $$\mathbb{N} = \{0, 1, 2, \ldots\}$$ (written $$\mathbb{N} \models \varphi$$).

### 2. Formal Axiom Systems and Hilbert’s Three Wishes
A formal system like **Peano Arithmetic (PA)** or **ZFC Set Theory** acts like a strict compiler checking every line of a proof. Hilbert hoped to build one system $$T$$ possessing three properties simultaneously:
- **Consistency:** Never proves both $$\varphi$$ and $$\neg \varphi$$ (never derives $$0 = 1$$).
- **Completeness:** For every sentence $$\varphi$$ in the language, proves either $$T \vdash \varphi$$ or $$T \vdash \neg\varphi$$.
- **Effective axiomatization:** A finite algorithm can tell whether any given string is an axiom.

### 3. Computability and the Permanent Gap Between Truth and Provability
Gödel’s first theorem proves that *arithmetic truth ($$\models$$) permanently outruns mechanical provability ($$\vdash$$)*. Translated into computer science (Alan Turing, 1936): the set of theorems provable in $$T$$ is recursively enumerable (a computer can print them out one by one), whereas the set of all true arithmetic sentences is not. Far from breaking mathematics, Gödel’s architecture laid the groundwork for theoretical computer science and formal verification.

---

## 1. What a formal theory is trying to be

A **formal axiom system** (theory) for arithmetic provides:

- a finite alphabet and a precise language ($$0$$, successor $$S$$, addition, multiplication, quantifiers, logical connectives);  
- a decidable set of axioms (or an effective axiom schema);  
- mechanical inference rules.

A **proof** is a finite sequence of formulas, each an axiom or following from earlier lines by a rule. Because proofs are finite combinatorial objects, questions about provability can—after coding—become questions about numbers.

---

## 2. The theorems (idea-level statements)

**First incompleteness theorem (informal).**  
Let $$T$$ be a consistent, effectively axiomatized theory capable of expressing elementary arithmetic (such as Peano Arithmetic). Then there exists a sentence $$G$$ in the language of $$T$$ such that $$T$$ proves neither $$G$$ nor $$\neg G$$. In particular, $$T$$ is incomplete.

**Second incompleteness theorem (informal).**  
Under similar hypotheses, if $$T$$ is consistent then $$T$$ cannot prove $$\mathrm{Con}(T)$$, a natural arithmetic sentence expressing the consistency of $$T$$. Roughly: a sufficiently strong theory cannot certify its own consistency from inside.

---

## 3. Explanation: Hand-Encoding and Decoding Gödel Numbers

Gödel’s first great breakthrough is the **arithmetization of syntax**: turning every symbol, every formula, and even an entire multi-line proof into a **single unique natural number**. To see there is zero mysticism involved, build a miniature code table and compute by hand:

| Symbol | `0` | `S` (successor) | `=` | `+` | `(` | `)` |
|--------|-----|-----------------|-----|-----|-----|-----|
| **Code** | $$1$$ | $$2$$ | $$3$$ | $$4$$ | $$5$$ | $$6$$ |

To encode a string of $$k$$ symbols with codes $$c_1, c_2, \ldots, c_k$$, raise the first $$k$$ primes $$2, 3, 5, 7, 11, \ldots$$ to those powers and multiply:

$$
\ulcorner c_1 c_2 \cdots c_k \urcorner \;=\; 2^{c_1} \cdot 3^{c_2} \cdot 5^{c_3} \cdots p_k^{c_k}.
$$

### Step 1: Encode Two Real Formulas by Hand
- **Formula 1:** `0=0` has three symbols with codes $$(1, 3, 1)$$. Its Gödel number is:
  $$
  \ulcorner 0=0 \urcorner \;=\; 2^1 \cdot 3^3 \cdot 5^1 \;=\; 2 \cdot 27 \cdot 5 \;=\; 270.
  $$
- **Formula 2:** `S0=S0` (meaning $$1 = 1$$) has five symbols with codes $$(2, 1, 3, 2, 1)$$. Its Gödel number is:
  $$
  \ulcorner S0=S0 \urcorner \;=\; 2^2 \cdot 3^1 \cdot 5^3 \cdot 7^2 \cdot 11^1 \;=\; 4 \cdot 3 \cdot 125 \cdot 49 \cdot 11.
  $$
  Multiply step by step: $$4 \times 3 = 12$$; $$12 \times 125 = 1\,500$$; $$1\,500 \times 49 = 73\,500$$; $$73\,500 \times 11 = 808\,500$$!

### Step 2: Decode Back via Unique Prime Factorization
Hand someone the integer $$270$$ and ask which formula it encodes: factoring gives $$270 = 2^1 \cdot 3^3 \cdot 5^1$$, reading off the exponents $$(1, 3, 1)$$ immediately recovers `0=0`! By the Fundamental Theorem of Arithmetic, no two distinct formulas can ever collide.

### Step 3: Turn "Provable" Into Pure Arithmetic
A full proof of $$r$$ lines with Gödel numbers $$g_1, g_2, \ldots, g_r$$ packs into one integer $$m = 2^{g_1} \cdot 3^{g_2} \cdots p_r^{g_r}$$. Because checking each inference rule is purely mechanical, the relation

$$
\mathrm{Proof}_T(m, n) \;\iff\; \text{"integer } m \text{ encodes a valid } T\text{-proof of the formula coded by } n\text{"}
$$

becomes a purely arithmetic property expressible using addition, multiplication, and divisibility! Provability inside $$T$$ is then simply:

$$
\mathrm{Prov}_T(n) \;:\iff\; \exists m\, \mathrm{Proof}_T(m, n).
$$

Something astonishing has happened: $$T$$, designed only to talk about numbers, can now talk about **proofs of statements about numbers**, because proofs have become numbers.

---

### Short video: Kurt Gödel (1931): Incompleteness Theorems

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/godel-incompleteness_en.mp4"></video>
</div>

94-second silent overview: Hilbert’s program, Gödel numbering encoding formulas via prime exponents (e.g. 270 = 2¹·3³·5¹), the fixed-point lemma constructing G ⇔ (T ⊬ G), and why truth outruns formal provability.

## 4. From the Liar Paradox to the Self-Referential Gödel Sentence

Start with an ancient everyday paradox—the **Liar Paradox**:

> *"This sentence is false."*

If it is true, it must be false; if it is false, it must be true! In English, self-reference plus "false" explodes into contradiction.

Gödel’s stroke of genius was realizing that while arithmetic *cannot* define its own truth predicate (Tarski’s undefinability theorem), it **can** define *"unprovable in $$T$$"* via Gödel numbering. Swapping "false" for *"unprovable in $$T$$"* turns a logical explosion into a razor-sharp theorem.

How does a formula talk about its own Gödel number without circularity? Philosopher W. V. O. Quine showed the exact trick in plain English:

> *"yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.*

Read that carefully: the quoted phrase names a substitution operation, and applying that operation to the phrase itself produces **the exact sentence you just read**! In arithmetic, the **Diagonal (Fixed-Point) Lemma** performs the exact numerical substitution: for any formula $$\psi(x)$$ with one free variable, there exists a sentence $$\varphi$$ such that

$$
T \vdash \varphi \;\leftrightarrow\; \psi(\ulcorner\varphi\urcorner).
$$

Applying this to $$\psi(x) \equiv \neg\mathrm{Prov}_T(x)$$ produces the **Gödel sentence $$G$$**:

$$
T \vdash G \;\leftrightarrow\; \neg\mathrm{Prov}_T(\ulcorner G\urcorner).
$$

In words: $$G$$ asserts *"$$G$$ is not provable in $$T$$."*

### Why Consistency Forces $$G$$ to Be True Yet Unprovable

- **Case 1:** Suppose $$T \vdash G$$. Then a concrete proof code $$m$$ exists, so $$T \vdash \mathrm{Prov}_T(\ulcorner G\urcorner)$$. Combined with $$T \vdash G \leftrightarrow \neg\mathrm{Prov}_T(\ulcorner G\urcorner)$$, we get $$T \vdash \neg G$$. Thus $$T$$ proves both $$G$$ and $$\neg G$$—**contradicting consistency**!
- **Case 2:** Therefore, if $$T$$ is consistent, **$$T \nvdash G$$**. Wait—that is literally what $$G$$ says! So $$G$$ is **true** in the standard natural numbers $$\mathbb{N}$$, yet **unprovable** in $$T$$! (Gödel originally used $$\omega$$-consistency to rule out $$T \vdash \neg G$$; in 1936, J. Barkley Rosser refined the sentence so plain consistency suffices.)

The entire proof architecture fits on one line:

**coding → internal provability predicate → diagonal self-reference → true but unprovable sentence.**

---

## 5. The second theorem: consistency is not free

The second incompleteness theorem states that $$\mathrm{Con}(T)$$ (expressing *"$$T$$ proves no contradiction,"* such as $$\neg\mathrm{Prov}_T(\ulcorner 0=1\urcorner)$$) cannot be proved inside $$T$$ whenever $$T$$ is consistent and strong enough. The intuition is wonderfully crisp: the first theorem’s argument (*"if $$T$$ is consistent, then $$G$$ is unprovable"*) can itself be formalized inside $$T$$ as

$$
T \vdash \mathrm{Con}(T) \rightarrow G.
$$

If $$T$$ also proved $$\mathrm{Con}(T)$$, then by *modus ponens* $$T$$ would prove $$G$$, contradicting the first theorem! Hence proving a strong system consistent always requires principles **outside** that system (e.g. ZFC can prove Peano Arithmetic consistent, but ZFC cannot certify itself).

---

## 6. What incompleteness is *not*

| Misreading | Correction |
|------------|------------|
| “Nothing can be proved.” | Vast parts of mathematics remain proved as always; incompleteness limits *complete* capture of arithmetic truth in one effective system. |
| “Every system is inconsistent.” | The theorems assume consistency to conclude incompleteness; inconsistency is a different failure mode. |
| “Humans can see truths machines cannot.” | The theorems alone do not establish a metaphysical superiority of human minds; that is a separate philosophical debate. |
| “Incompleteness equals undecidability of the halting problem.” | Closely related diagonal themes and historical kinship, but not the same theorem. |
| “Gödel showed mathematics is subjective.” | He showed formal limitations of certain axiomatic packages; mathematical practice continues with proofs, models, and relative consistency results. |

---

## 7. Diagonal kinship with Cantor and Turing

Cantor’s diagonal builds a real that escapes every list. Turing’s diagonal builds a behavior that escapes every machine. Gödel’s diagonal builds a sentence that escapes every proof in $$T$$ by referring to its own unprovability. The family resemblance is real:

- enumerate putative total solutions (lists, machines, proofs);  
- construct an object that disagrees on the diagonal;  
- conclude no complete effective solution exists inside the given framework.

Understanding Cantor makes Gödel’s strategy feel less like a magic trick and more like a high-precision cousin.

---

## 8. Why it matters

- **Foundations.** Completeness and consistency cannot be packaged together for strong arithmetic in the way Hilbert hoped.  
- **Mathematical practice.** Working mathematicians rarely hit Gödel sentences in daily work; they do inherit a culture that distinguishes truth in a model from provability in a theory, and that values relative consistency proofs.  
- **Computer science.** The boundary between what is formally derivable and what is true feeds into automated theorem proving, proof assistants, and the theory of formal verification—where “the system cannot prove its own consistency” is a living reminder to be careful about trust bases.  
- **Philosophy.** Debates about platonism, formalism, and the nature of mathematical truth were permanently reshaped.

---

## Common confusions

1. **“Incompleteness means our axioms are wrong.”** — It means no single effective axiomatization of sufficient strength is both consistent and complete for arithmetic.  
2. **“Adding $$G$$ as an axiom fixes everything forever.”** — The new theory $$T+G$$ has its *own* Gödel sentence; incompleteness recurs.  
3. **“Gödel numbering is arbitrary mysticism.”** — It is a coding scheme, no more mystical than Unicode, but powerful because arithmetic can express the coding relations.  
4. **“The second theorem says we can never trust mathematics.”** — It says a theory cannot be the sole judge of its own consistency; trust can still rest on practice, stronger systems, or other evidence.  
5. **“Idea of the proof means handwaving self-reference.”** — Legitimate self-reference here is engineered through the fixed-point lemma and representability, not through casual English paradoxes alone.

---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/godel-incompleteness/analysis.md`.

### Status

**Proved** (Gödel 1931). First and second incompleteness theorems are theorems of mathematical logic; popularizations often overclaim 'math is broken'.

### Core statement / slogan

Any consistent, effectively axiomatized theory capable of arithmetic is incomplete: there are true (in $$\mathbb{N}$$) sentences unprovable in the theory. Second: such a theory cannot prove its own consistency (under standard formalizations).

### Definitions to freeze

- **Formal theory.** Language + effective axioms + rules of inference; theorems = derivable sentences.
- **Gödel sentence (idea).** Self-referential arithmetical sentence asserting its own unprovability in $$T$$.

### Hygiene (from confusions log)

- Interpreting incompleteness as 'nothing can be proved' or 'all systems are inconsistent'.
- Conflating incompleteness with undecidability of arbitrary natural-language questions.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/godel-incompleteness/`.

**Recommended order**

1. **Orientation** — Numberphile — Gödel's Incompleteness Theorem (Marcus du Sautoy): [https://www.youtube.com/watch?v=O4ndIDcDSGc](https://www.youtube.com/watch?v=O4ndIDcDSGc).  
2. **Orientation** — TED-Ed — Paradox at the heart of mathematics (du Sautoy): [https://www.youtube.com/watch?v=I4pQbo5MQOs](https://www.youtube.com/watch?v=I4pQbo5MQOs).  
3. **Core** — Veritasium — Math's Fundamental Flaw (Gödel + undecidability arc): [https://www.youtube.com/watch?v=HeQX2HjkcNo](https://www.youtube.com/watch?v=HeQX2HjkcNo).  
4. **Foundation** — Computerphile — Gödel's Incompleteness (Altenkirch / Lean): [https://www.youtube.com/watch?v=IuX8QMgy4qE](https://www.youtube.com/watch?v=IuX8QMgy4qE).  
5. **Meta** — Numberphile page: [https://www.numberphile.com/videos/godels-incompleteness-theorem](https://www.numberphile.com/videos/godels-incompleteness-theorem).  

**Status reminder:** **Proved** (Gödel 1931). First and second incompleteness theorems are theorems of mathematical logic; popularizations often overclaim 'math is broken'.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/godel-incompleteness/transcripts/` · status: `research/video-research/godel-incompleteness/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/godel-incompleteness_O4ndIDcDSGc_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

1. Gödel, K. (1931). On formally undecidable propositions of *Principia Mathematica* and related systems I.  
2. Standard logic textbooks: Enderton; Mendelson; or Smullyan on Gödel’s theorems (various levels).  
3. Nagel & Newman — *Gödel’s Proof* (popular but classic).  
4. Course: [Cantor diagonal]({{ site.baseurl }}/contents/en/chapter05/05_03_Cantor_Diagonal/), [Infinity]({{ site.baseurl }}/contents/en/chapter04/04_02_Infinity/).

---


Full URL bibliography from video research: `research/video-research/godel-incompleteness/references.md`.

### Videos (recommended path)

- Numberphile — Gödel's Incompleteness Theorem (Marcus du Sautoy) (ORIENTATION): https://www.youtube.com/watch?v=O4ndIDcDSGc
- TED-Ed — Paradox at the heart of mathematics (du Sautoy) (ORIENTATION): https://www.youtube.com/watch?v=I4pQbo5MQOs
- Veritasium — Math's Fundamental Flaw (Gödel + undecidability arc) (CORE): https://www.youtube.com/watch?v=HeQX2HjkcNo
- Computerphile — Gödel's Incompleteness (Altenkirch / Lean) (FOUNDATION): https://www.youtube.com/watch?v=IuX8QMgy4qE
- Numberphile page (META): https://www.numberphile.com/videos/godels-incompleteness-theorem

### Papers and web (from research pack)

- Wikipedia — Gödel's incompleteness theorems: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
- Stanford Encyclopedia of Philosophy — Gödel's incompleteness: https://plato.stanford.edu/entries/goedel-incompleteness/
- N. Raatikainen SEP entry (same as above): https://plato.stanford.edu/entries/goedel-incompleteness/
- TED-Ed lesson page: https://ed.ted.com/lessons/the-paradox-at-the-heart-of-mathematics-godel-s-incompleteness-theorem-marcus-du-sautoy
- Wikipedia — Hilbert's program (context): https://en.wikipedia.org/wiki/Hilbert%27s_program

### Course

- Research pack: `research/video-research/godel-incompleteness/` (especially `references.md`, `learning_path.md`).

## Further directions

- Compare Rosser’s improvement of the first theorem (weaker consistency-like hypotheses).  
- Explore the connection between incompleteness and the undecidability of Hilbert’s tenth problem (different theorem, shared computability themes).  
- In proof assistants, ask: what is the trusted kernel, and how does that relate to “consistency lives in a meta-theory”?  
- Note one precise question you still have—good questions are part of mathematical practice.

## Video tham khảo

- **xem trước** — [Gödel's Incompleteness Theorem - Numberphile](https://www.youtube.com/watch?v=O4ndIDcDSGc) — Numberphile, English. Watch first. “Gödel's Incompleteness Theorem - Numberphile” orients the lesson’s aim: State informal but accurate versions of Gödel’s first and second incompleteness theorems.
- [The paradox at the heart of mathematics: Gödel's Incompleteness Theorem - Marcus du Sautoy](https://www.youtube.com/watch?v=I4pQbo5MQOs) — TED-Ed, English. A second pass once the main claim is in view: State informal but accurate versions of Gödel’s first and second incompleteness theorems.
- [Math's Fundamental Flaw](https://www.youtube.com/watch?v=HeQX2HjkcNo) — Veritasium, English. Further depth after the first two, still tied to this lesson: State informal but accurate versions of Gödel’s first and second incompleteness theorems.
