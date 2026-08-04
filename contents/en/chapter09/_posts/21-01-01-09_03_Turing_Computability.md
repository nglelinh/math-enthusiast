---
layout: post
title: "Turing, Computability, and Undecidability"
chapter: '09'
order: 3
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

In **1936**, before electronic stored-program computers existed as consumer objects, **Alan Turing** published *On Computable Numbers, with an Application to the Entscheidungsproblem*. The paper did two things that still structure theoretical computer science: it proposed a precise mathematical model of mechanical calculation—the **Turing machine**—and it proved that some natural decision problems are **undecidable**: no algorithm, running forever if needed, can correctly answer every instance.

This lecture is about **what can be computed at all**, not yet about what can be computed *quickly*. Efficiency and NP-completeness come later. Here the drama is absolute: some well-posed questions about programs and formulas lie beyond every possible general method. That limit is a theorem, not a temporary lack of clever code.

---

## Learning objectives

After this lecture you should be able to:

- Describe the **Turing machine** model at slogan level (tape, head, finite control, step-by-step transition).
- Explain what **computable numbers** and computable functions meant in Turing’s 1936 setting.
- State the **Church–Turing thesis** as a working identification of “effectively calculable” with Turing-computable (a thesis, not a theorem).
- Sketch why the **halting problem** is undecidable (diagonal / self-reference idea).
- Connect undecidability to Hilbert’s **Entscheidungsproblem** and to the idea of a **universal machine**.
- Apply **LO6**: distinguish mathematical undecidability from “my laptop is slow” or “this app crashes.”
- Cross-link to [Gödel]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/) and [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) without collapsing the three stories.

**Prerequisites.** Comfort with algorithms as finite descriptions of step-by-step processes; basic logic vocabulary (yes/no questions, proof vs computation). No automata theory course required.

**Seminar links.** LO1, LO6; [Gödel incompleteness]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/); [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/); [Complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/); [What Is the Turing Award?]({{ site.baseurl }}/contents/en/chapter09/09_02_What_Is_Turing_Award/).

---

## 1. What problem Turing was answering

Early twentieth-century logic asked: when is a mathematical question **decidable** by a fixed method? Hilbert’s **Entscheidungsproblem** (decision problem) asked, roughly, for a general procedure that would take a first-order logical formula and answer whether it is valid—true in every interpretation—or not.

To settle such questions one needs a **definition** of “procedure.” Informal phrases—“finite combination of rules,” “mechanical method”—are not enough for a negative theorem. If you want to prove that *no* method works, you must quantify over a precise class of methods.

Turing’s move was to analyze what a human computer does when following a fixed rule: scanning symbols on paper, changing a finite amount of “state of mind,” writing or erasing according to a finite table of instructions. Idealizing that picture produced the Turing machine. Alonzo Church, in the same era, offered the **lambda calculus** as another formalization of effective calculability. The resulting convergence is the cultural content of the Church–Turing thesis.

---

## 2. The Turing machine model

A **Turing machine** consists of:

- an infinite **tape** divided into cells, each holding a symbol from a finite alphabet (including a blank);  
- a **read/write head** that sees one cell at a time;  
- a finite set of **states**, including a start state and accepting/rejecting or halting conventions;  
- a **transition function** that, given current state and scanned symbol, specifies a new symbol to write, a direction to move (left/right), and a next state.

Computation proceeds in discrete steps. On an input string written on the tape, the machine runs until it enters a designated halting configuration—or it may run forever.

Despite the model’s poverty of hardware, it is astonishingly expressive. With suitable encoding, Turing machines can simulate arithmetic, parse formulas, run any algorithm you can describe carefully, and even simulate other Turing machines. Variants (multi-tape, multi-head, nondeterministic) change constant factors and convenience, not the broad class of computable languages—up to standard equivalences taught in computability courses.

**Why mathematicians accept the model.** Anything that feels like a finite rulebook operating on finite inscriptions can be emulated by a TM. Conversely, a TM is clearly “mechanical.” That two-way fit is why the model stuck.

---

## 3. Computable numbers and computable functions

Turing’s title foregrounds **computable numbers**: real numbers whose decimal (or binary) expansion can be generated digit-by-digit by a mechanical process. Equivalently, one studies **partial computable functions** $$f: \mathbb{N} \rightharpoonup \mathbb{N}$$ given by machines that may diverge on some inputs.

Not every real is computable. There are only countably many Turing machines, hence only countably many computable reals, while $$\mathbb{R}$$ is uncountable. Most reals are algorithmically indescribable. That fact is a computability cousin of Cantor’s diagonal argument—see also [infinity]({{ site.baseurl }}/contents/en/chapter04/04_02_Infinity/) and [Cantor diagonal]({{ site.baseurl }}/contents/en/chapter05/05_03_Cantor_Diagonal/).

For decision problems we focus on **languages** $$L \subseteq \{0,1\}^*$$: the machine should accept strings in $$L$$ and reject (or fail to accept) strings outside. A language is **decidable** (recursive) if some machine halts on every input with the correct yes/no answer. It is **recognizable** (recursively enumerable) if some machine accepts exactly the strings in $$L$$, possibly looping forever on no-instances.

---

## 4. The universal machine

Turing observed that one can build a **universal Turing machine** $$U$$: a single machine that, given a description $$\langle M \rangle$$ of another machine $$M$$ together with an input $$x$$, simulates $$M$$ on $$x$$.

$$
U(\langle M \rangle, x) \;\;\text{behaves like}\;\; M(x).
$$

Universality is the conceptual ancestor of the **stored-program computer**: code is data. Interpreters, virtual machines, and “a CPU runs whatever program is loaded” are engineering echoes of a 1936 mathematical idea. Universality also enables diagonal arguments: machines can be fed their own descriptions.

---

## 5. The halting problem

Define the **halting problem** language:

$$
\textsc{Halt} = \{ \langle M, x \rangle \mid M \text{ is a TM that eventually halts on input } x \}.
$$

**Theorem (Turing).** $$\textsc{Halt}$$ is undecidable: no Turing machine $$H$$ correctly determines, for every pair $$\langle M,x\rangle$$, whether $$M$$ halts on $$x$$.

**Idea of the proof (diagonal).** Suppose toward contradiction that a decider $$H$$ exists. Build a machine $$D$$ that on input $$\langle M \rangle$$ runs $$H$$ on $$\langle M, \langle M \rangle \rangle$$ and then does the opposite of $$M$$’s predicted behavior: if $$H$$ says $$M$$ halts on its own description, $$D$$ loops forever; if $$H$$ says $$M$$ does not halt, $$D$$ halts. Now run $$D$$ on $$\langle D \rangle$$. Self-reference produces contradiction either way.

The argument is cousin to Cantor’s diagonal and to Gödel’s self-referential sentence—different formal settings, shared diagonal spirit.

**Consequences.** Many other problems reduce from halting: virus “does this program ever print 5?”, equivalence of arbitrary programs, and—via suitable encodings—various questions about mathematical theories. Undecidability spreads along reductions just as NP-hardness does in complexity theory, but here the resource is **any finite time**, not polynomial time.

---

## 6. Entscheidungsproblem and the limit of decision methods

Church and Turing showed that the Entscheidungsproblem is unsolvable: there is no general algorithm that decides validity of first-order logic sentences. The modern slogan is: **first-order validity is undecidable**.

That does not say mathematics is impossible. It says there is no *single* mechanical procedure that correctly classifies all first-order sentences. Specific theories may still be decidable (Presburger arithmetic is a famous example); others are not. Proof search may semi-decide theoremhood in some systems while non-theorems cause infinite search—recognizability without decidability.

Place this next to [Gödel incompleteness]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/): incompleteness limits what a fixed axiomatic theory can *prove*; undecidability limits what an algorithm can *decide*. Related, not identical.

---

## 7. Church–Turing thesis

The **Church–Turing thesis** asserts that the informal notion of effective calculability coincides with Turing-computability (equivalently, with lambda-definability, recursive functions, etc.).

It is a **thesis**, not a theorem, because “effective” is pre-formal. Its strength is empirical and conceptual: every serious attempt to formalize algorithms has yielded the same computable functions. Physical proposals for “hypercomputation” either smuggle non-implementable resources or fail to enlarge the mathematical class under realistic constraints.

For this course: use the thesis as a **license to think in algorithms** without obsessing over machine details—while remembering that **complexity** (time bounds) *does* care about models more finely than computability does.

---

## 8. Physical computers versus mathematical undecidability (LO6)

Students and media often confuse layers:

| Everyday phrase | Mathematical content |
|-----------------|----------------------|
| “The program froze” | Engineering: bugs, deadlocks, resource limits—not a proof of undecidability. |
| “Computers can’t solve this; it’s too slow” | Often a **complexity** issue (exponential time), not undecidability. |
| “No algorithm exists” | **Undecidability**: every candidate TM fails on some inputs (wrong answer or non-halting when it should decide). |
| “P ≠ NP” | Open **efficiency** question about polynomial time; both sides assume decidability of the problems involved. |

A problem can be decidable yet infeasible (try brute-force SAT on huge formulas). A problem can be undecidable even with unbounded time. [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) lives in the decidable world and asks about *efficient* algorithms. Do not say “NP-complete means undecidable.” NP-complete problems are decidable by brute force; the question is whether they admit poly-time algorithms.

---

## 9. Confusions

| Claim | Correction |
|-------|------------|
| “Undecidable means we haven’t found the algorithm yet.” | Undecidable means a proof rules out *any* correct total algorithm. |
| “Turing machines are obsolete; we have quantum computers.” | Quantum machines change *resource* classes (e.g. BQP); they do not decide the classical halting problem. |
| “Gödel already proved everything is undecidable.” | Incompleteness ≠ computability undecidability; related diagonal ideas, different theorems. |
| “If it loops, it is the halting problem.” | Non-termination on one run is not a classification of the decision problem’s status. |
| “Universal machine means AI consciousness.” | Universality is about simulation of formal machines, not a theory of mind. |

---

## Exercises

1. In your own words, list the components of a Turing machine and what one step does.  
2. Why does countability of machines imply most reals are non-computable? ≤100 words.  
3. Explain the role of the **universal** machine in the diagonal argument for $$\textsc{Halt}$$ at slogan level.  
4. Distinguish **decidable** from **recognizable** with one sentence each and one example class of phenomena (even toy examples).  
5. **≤250 words:** Compare Hilbert’s Entscheidungsproblem with a modern “can we automate all math checks?” headline using LO6.  
6. Write three bullet points separating undecidability, P vs NP, and “the server timed out.”  
7. After reading [Gödel]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/), name one similarity and one difference between incompleteness and undecidability.  
8. (Optional.) Look up a reduction from $$\textsc{Halt}$$ to another classic undecidable problem (e.g. the Post correspondence problem) and summarize the idea in five sentences.

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/turing-computability/`.

**From the research pack (must-know slogans)**

- **Turing machine** as a model of effective computation; Church–Turing thesis (informal).
- **Halting problem** undecidable; Entscheidungsproblem negative solution.
- Undecidability ≠ “we haven't found an algorithm yet” — proven impossibility within the model.

**Recommended order**

1. **Orientation** — Computerphile / Numberphile culture: search Turing halting: [https://www.youtube.com/watch?v=macM_MtS_w4](https://www.youtube.com/watch?v=macM_MtS_w4).  

**Official / primary written hubs**

- amturing.acm.org (award named for Turing): https://amturing.acm.org/  

Complete URL bibliography: `research/video-research/turing-computability/references.md`.


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/turing-computability/transcripts/` · status: `research/video-research/turing-computability/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/turing-computability_macM_MtS_w4_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References


### Video research pack (all URLs)

Complete list: `research/video-research/turing-computability/references.md`.

1. Wikipedia — Turing machine — https://en.wikipedia.org/wiki/Turing_machine  
2. Wikipedia — Halting problem — https://en.wikipedia.org/wiki/Halting_problem  
3. Wikipedia — Church–Turing thesis — https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis  
4. Wikipedia — Entscheidungsproblem — https://en.wikipedia.org/wiki/Entscheidungsproblem  
5. SEP — Turing machines — https://plato.stanford.edu/entries/turing-machine/  
6. SEP — Computability and complexity — https://plato.stanford.edu/entries/computability/  
7. Turing's 1936 paper (archive culture) — https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf  
8. amturing.acm.org (award named for Turing) — https://amturing.acm.org/  
9. Computerphile / Numberphile culture: search Turing halting — https://www.youtube.com/watch?v=macM_MtS_w4  
10. Research pack folder: `research/video-research/turing-computability/`.

1. A. M. Turing, “On Computable Numbers, with an Application to the Entscheidungsproblem,” *Proc. London Math. Soc.*, 1936/37.  
2. ACM Turing Award context and biography materials: [amturing.acm.org](https://amturing.acm.org/) (historical background on Turing).  
3. M. Sipser, *Introduction to the Theory of Computation* — standard undergrad treatment of TMs, decidability, reductions.  
4. H. Rogers, *Theory of Recursive Functions and Effective Computability*; or Soare’s computability texts for deeper study.  
5. Course: [Gödel]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/); [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/); [Complexity]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/).

---

## Further directions

- Read a modern textbook proof of the undecidability of $$\textsc{Halt}$$ end-to-end and rewrite it without symbols for a classmate.  
- Explore **Rice’s theorem**: nontrivial semantic properties of programs are undecidable—an industrial-strength corollary of the diagonal idea.  
- Survey how proof assistants and automated theorem provers live *with* undecidability (semi-decision, tactics, bounded search).  
- Next: [Cook, Karp, and NP-Completeness]({{ site.baseurl }}/contents/en/chapter09/09_04_Cook_Karp_NP/).
