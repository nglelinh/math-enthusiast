---
layout: post
title: "Euclid and Cantor: Two Ideas of Proof"
chapter: '05'
order: 2
owner: Nguyen Le Linh
lang: en
categories:
- chapter05
---

Imagine a confident skeptic dropping two enormous directories onto your desk. The first, they boast, lists **every prime number** in existence—not a single one missing. The second, an endless ledger with pages numbered $$1, 2, 3, \ldots$$, lists **every real number** between $$0$$ and $$1$$.

You do not need to argue for hours, and you certainly do not need to check every page. For each directory, mathematics hands you a single razor-sharp move: use the skeptic’s own book to manufacture an outsider that **cannot possibly appear anywhere inside it**.

That is the story of two masterpieces separated by more than two millennia, placed side by side as this **Section 5 flagship**:

1. **Euclid (c. 300 BCE):** given any finite list of primes, build a number that forces a brand-new prime outside the list.
2. **Georg Cantor (late 19th century):** given any countable list of reals, build a real number that disagrees with every row on the diagonal.

Both proofs fit on half a page. Both reshaped what humanity knows about numbers and infinity. If you carry away only one sentence from this lecture, make it this: *a proof can be tiny and still world-changing when its construction escapes every allegedly complete inventory.*

**Lesson roadmap:** Background Knowledge Map (number theory, set theory, escape constructions) → Part I: Euclid and infinitely many primes → Deep-Dive Explanation (Read Slowly): hand-checking Euclid’s machine through $$30031 = 59 \times 509$$ and primes of the form $$4k+3$$ → Part II: Cantor and uncountability of the reals → Side-by-side comparison → Writing a proof-idea narrative.

---

## Learning objectives

After this lecture you should be able to:

- Write Euclid’s argument as assumption → construction → contradiction, with correct modular intuition (remainder 1 when dividing by each listed prime).
- Explain why Euclid’s proof shows *infinitude*, not a formula for the $$n$$th prime, and why $$N$$ itself need not be prime.
- Reconstruct Cantor’s diagonal idea and explain why it shows that no complete listing of reals exists.
- Compare the two proofs as **escape constructions** against a “too small” inventory—finite primes versus countable reals.
- Distinguish the *idea of a proof* from *full technical hygiene* (unique decimals, base representation, existence of prime factors).
- Produce a short **proof-idea narrative** suitable for practice toward seminar assignment A4.

**Prerequisites.** Comfort with proof by contradiction; familiarity with prime numbers and with writing numbers as infinite decimals (or binary expansions) at a naive level. No measure theory or formal set theory is required.

---

## Background Knowledge Map: Number Theory, Set Theory, and Escape Constructions

Before walking through the proofs, let us place both theorems on the map of university mathematics so you can see what each field actually studies and why their proof strategies rhyme:

### 1. What Is Number Theory and What Does It Study?
Just as chemistry studies matter through periodic-table elements, **number theory** studies the integers $$\mathbb{Z}$$ through their multiplicative atoms: the **prime numbers**. By the **Fundamental Theorem of Arithmetic**, every integer greater than $$1$$ factors uniquely into primes. Number theory asks deceptively simple questions about these atoms: Are there infinitely many? How fast do they thin out? Are there infinitely many twin primes $$(p, p+2)$$? Beyond pure mathematics, large primes form the security backbone of **RSA public-key cryptography** protecting modern internet traffic.

### 2. What Is Set Theory and What Does It Study?
By the late nineteenth century, mathematicians needed a rigorous way to compare the sizes of infinite collections—natural numbers $$\mathbb{N}$$, rationals $$\mathbb{Q}$$, real numbers $$\mathbb{R}$$, spaces of functions. **Set theory** measures size (**cardinality**) through **bijections** (exact one-to-one pairings with nothing left over). That single ruler revealed Cantor’s shock: infinity is not one monolith, but an endless hierarchy of strictly larger sizes.

### 3. Proof by Contradiction and Escape Constructions
When you want to prove no catalogue can ever be complete, you cannot inspect infinitely many catalogues one by one. Instead, you use **reductio ad absurdum**: grant the skeptic an allegedly complete list, then feed that very list into a deterministic recipe that outputs a **witness** guaranteed to sit outside it. Turning an opponent’s claimed inventory against itself is the exact architectural ancestor of Gödel’s incompleteness theorem and Turing’s halting problem.

---

## Part I — Euclid: infinitely many primes

### From the "Closed Periodic Table" Paradox to a Theorem

In everyday life, lists feel finite: the periodic table has just over a hundred elements; an alphabet has a few dozen letters. As you scan the primes $$2, 3, 5, 7, 11, 13, \ldots$$, they grow sparser and sparser, so a skeptic could reasonably ask: *"What if, past some astronomical threshold, every larger integer is just a product of the primes we already found?"* No computer search can silence that skeptic, because they can always say the list ends right after the largest prime you computed. Euclid’s genius was to build a machine that refutes *every* finite list at once.

### Theorem

There are infinitely many prime numbers.

### Historical and conceptual setting

Euclid’s argument (often identified with Book IX, Proposition 20 of the *Elements*) is among the oldest proofs still taught verbatim in spirit. Greek mathematics already knew many primes; the deep claim is not “there are quite a few,” but that **no finite catalogue can exhaust them**. That is a statement about *all* primes, hence a statement that cannot be settled by listing alone.

### The idea

Assume only finitely many primes exist; manufacture a number that forces a prime outside the list.

### The argument

Suppose the complete list of primes is $$p_1,p_2,\ldots,p_k$$. Define

$$
N = p_1 p_2 \cdots p_k + 1.
$$

Then $$N > 1$$, so $$N$$ has at least one prime factor $$q$$.  
For each $$i$$, dividing $$N$$ by $$p_i$$ leaves remainder $$1$$, so $$p_i \nmid N$$.  
Hence $$q$$ is a prime not in the list. Contradiction.

Therefore the list cannot be complete: there are infinitely many primes.

![Euclid construction]({{ site.baseurl }}/img/chapter_img/euclid_primes_proof.svg)

*Figure. From any finite list of primes, build $$N$$ that demands a new prime factor.*

### Deep-Dive Explanation (Read Slowly): Hand-Checking Euclid’s Machine and Primes of Form $$4k+3$$

To see why "remainder 1" destroys every finite list—and why $$N$$ itself **need not be prime**—check the arithmetic by hand:

1. **Step 1 — Run Euclid’s recipe on small lists:**

| Alleged complete list | Product $$P$$ | $$N = P + 1$$ | Factorization of $$N$$ | New prime(s) forced out |
|-----------------------|---------------|---------------|------------------------|-------------------------|
| $$\{2\}$$ | $$2$$ | $$3$$ | Prime | $$3$$ |
| $$\{2, 3\}$$ | $$6$$ | $$7$$ | Prime | $$7$$ |
| $$\{2, 3, 5\}$$ | $$30$$ | $$31$$ | Prime | $$31$$ |
| $$\{2, 3, 5, 7, 11\}$$ | $$2310$$ | $$2311$$ | Prime | $$2311$$ |
| $$\{2, 3, 5, 7, 11, 13\}$$ | $$30030$$ | $$30031$$ | $$59 \times 509$$ (composite!) | $$59$$ and $$509$$ |

2. **Step 2 — Verify the first composite case ($$30031$$) by hand:**
   - Multiply step by step: $$2 \times 3 = 6$$; $$6 \times 5 = 30$$; $$30 \times 7 = 210$$; $$210 \times 11 = 2310$$; $$2310 \times 13 = 30030$$. Add $$1$$ to get $$N = 30031$$.
   - Check remainders: since $$30030$$ is divisible by every prime in $$\{2, 3, 5, 7, 11, 13\}$$, dividing $$30031$$ by any of them leaves remainder $$1$$ ($$30031 \equiv 1 \pmod{p_i}$$).
   - Check the factorization: $$59 \times 509 = 59 \times 500 + 59 \times 9 = 29500 + 531 = 30031$$. Even though $$N$$ is composite, both prime factors $$59$$ and $$509$$ are **guaranteed outsiders**!

3. **Step 3 — Adapt the same machine to prove infinitely many primes of the form $$4k + 3$$:**
   Suppose only finitely many primes of the form $$4k+3$$ exist: $$p_1, p_2, \ldots, p_m$$ (say $$\{3, 7, 11\}$$). Define
   $$
   M = 4 p_1 p_2 \cdots p_m - 1.
   $$
   - Hand-check $$\{3, 7\}$$: $$M = 4 \cdot 3 \cdot 7 - 1 = 83$$ (a new prime $$\equiv 3 \pmod 4$$).
   - Hand-check $$\{3, 7, 11\}$$: $$M = 4 \cdot 3 \cdot 7 \cdot 11 - 1 = 923 = 13 \times 71$$. Notice $$13 \equiv 1 \pmod 4$$, while $$71 \equiv 3 \pmod 4$$! Because any product of numbers $$\equiv 1 \pmod 4$$ stays $$\equiv 1 \pmod 4$$, yet $$M \equiv 3 \pmod 4$$, $$M$$ **must** have at least one prime factor $$q \equiv 3 \pmod 4$$. And since $$M \equiv -1 \pmod{p_i}$$, $$q$$ cannot be on the list! One hand calculation shows that Euclid’s proof is a reusable engine, not a one-off trick.

### What the idea *is*

- **Reductio:** assume a finite complete inventory of primes.  
- **Witness construction:** $$N = P+1$$ where $$P$$ is the product of all listed primes.  
- **Local obstruction:** each listed prime fails to divide $$N$$.  
- **Global conclusion:** the inventory was incomplete, so there are infinitely many primes.

### What the idea is *not*

- It does not claim $$N$$ itself is prime ($$30031 = 59 \cdot 509$$ breaks that myth at step 6).  
- It does not produce primes in increasing order.  
- It does not give a practical primality test or a dense supply of primes.  
- It does not require the full strength of unique factorization in heavy form: the elementary fact “every integer greater than 1 has a prime factor” is enough for the idea-level argument.

### Why it is a model proof

Minimal definitions, maximal conceptual punch. It is often the first proof that feels like *mathematics* rather than calculation. Later theorems—Dirichlet’s theorem on primes in arithmetic progressions, the infinitude of primes of special forms, sieve-theoretic lower bounds—are far harder. Euclid’s *style*—construct a witness that escapes a finite scheme—reappears throughout number theory and combinatorics.

### Variants worth knowing at slogan level

One common variant uses $$N = p_1\cdots p_k - 1$$ when that is larger than 1; the modular obstruction is then remainder $$-1$$ rather than $$1$$. Another pedagogical move is to prove “there is a prime larger than $$n$$” for every $$n$$ by taking $$n! + 1$$—reframing infinitude as “primes are unbounded.” The underlying escape idea is unchanged.

---

## Part II — Cantor: the reals are uncountable

### From Hilbert’s Infinite Hotel to a Shocking Theorem

Before the late nineteenth century, most thinkers treated "infinity" as a single undifferentiated size. **Hilbert’s Hotel** illustrates why: a hotel with infinitely many rooms numbered $$1, 2, 3, \ldots$$—even when completely full—can always accommodate one more guest (move guest $$n$$ to room $$n+1$$), or even an infinite busload of new guests (move guest $$n$$ to room $$2n$, freeing every odd room). Using clever room assignments, we can fit all integers $$\mathbb{Z}$$ and even all rational numbers $$\mathbb{Q}$$ into rooms $$1, 2, 3, \ldots$$.

The natural question followed: *can we check every real number in $$(0, 1)$$ into Hilbert’s Hotel too?* Georg Cantor proved **no**—the real continuum is so vast that it breaks the hotel completely.

### Theorem

The set of real numbers is uncountable: there is no bijection between $$\mathbb{N}$$ and $$\mathbb{R}$$. Equivalently, no sequence $$r_1,r_2,r_3,\ldots$$ lists all reals.

### Historical and conceptual setting

Georg Cantor’s diagonal argument (late nineteenth century) forced mathematics to accept **different sizes of infinity**. Countable infinity—the size of the natural numbers, integers, and even the rationals—is not the only infinite cardinality. The continuum of real numbers is strictly larger. This was philosophically shocking and technically fertile: it launched modern set theory, clarified the meaning of “most” reals, and seeded diagonal methods across logic and computer science.

### The idea

Any proposed list of reals misses at least one real, built by disagreeing with the $$n$$th listed number in the $$n$$th place.

### The argument (decimal form, idea level)

It is enough to show that the open interval $$(0,1)$$ is uncountable, because if $$(0,1)$$ cannot be listed, neither can $$\mathbb{R}$$. Suppose

$$
r_1, r_2, r_3, \ldots
$$

is a list of all numbers in $$(0,1)$$, written as infinite decimals. Let the $$n$$th digit of $$r_n$$ be $$d_{nn}$$. Define a number $$d = 0.e_1 e_2 e_3\ldots$$ by choosing each digit $$e_n$$ so that $$e_n \neq d_{nn}$$—for example, pick $$e_n = 4$$ if $$d_{nn}\neq 4$$, and $$e_n=5$$ otherwise. Then $$d\in(0,1)$$, but $$d\neq r_n$$ for every $$n$$, since they differ in the $$n$$th digit. So the list was incomplete.

![Cantor diagonal]({{ site.baseurl }}/img/chapter_img/cantor_diagonal.svg)

*Figure. Flip the diagonal digits; the new number escapes every row.*

### A Hand-Verifiable 4-Row Example

Suppose a skeptic’s list begins with four familiar decimals in $$(0,1)$$ (from $$\pi/10, e/10, \phi/10, \sqrt{2}/10$$):

$$
\begin{align*}
r_1 &= 0.\mathbf{3}1415\ldots,\\
r_2 &= 0.2\mathbf{7}182\ldots,\\
r_3 &= 0.16\mathbf{1}80\ldots,\\
r_4 &= 0.141\mathbf{4}2\ldots.
\end{align*}
$$

Read down the bold diagonal: $$d_{11}=3$$, $$d_{22}=7$$, $$d_{33}=1$$, $$d_{44}=4$$. Apply the safe $$\{4, 5\}$$ flip rule (choose $$4$$ unless the diagonal digit is $$4$$, in which case choose $$5$$):

$$
e_1 = 4,\quad e_2 = 4,\quad e_3 = 4,\quad e_4 = 5 \implies d = 0.4445\ldots
$$

Check row by row: $$d \neq r_1$$ (digit 1: $$4 \neq 3$$), $$d \neq r_2$$ (digit 2: $$4 \neq 7$$), $$d \neq r_3$$ (digit 3: $$4 \neq 1$$), $$d \neq r_4$$ (digit 4: $$5 \neq 4$$). Because $$d$$ uses only digits $$4$$ and $$5$$, it can never end in all $$0$$s or all $$9$$s, completely dodging the dual-expansion trap $$0.1999\ldots = 0.2000\ldots$$.

### Hygiene (what a polished proof watches)

- **Non-unique decimals.** Identities such as $$0.1999\ldots=0.2000\ldots$$ mean that digitwise difference is not always real difference. A careful proof either restricts the allowed expansions (e.g. forbid infinite tails of 9s), chooses a digit-flip rule that avoids dual representations (like $$\{4, 5\}$$ above), or works in a base and coding where the ambiguity is controlled.  
- **Binary expansions** face a similar dual-representation issue (tails of 1s).  
- The pedagogical diagonal still captures the **idea**; full courses fix the representation issue without changing the escape strategy.

### What the idea *is*

- **Enumerate-and-escape:** against any proposed complete sequence, build a missing element.  
- **Diagonal disagreement:** the $$n$$th coordinate of the witness is chosen to differ from the $$n$$th listed object.  
- **Cardinality gap:** $$\lvert\mathbb{R}\rvert > \lvert\mathbb{N}\rvert$$ in the sense of no bijection.

### What the idea is *not*

- It does not claim that “you cannot count very far.” Uncountable means *no bijection with $$\mathbb{N}$$* exists, not that humans run out of patience.  
- It does not prove that the continuum is “the next infinity after countable.” Whether there is an intermediate cardinality is the **continuum hypothesis**, independent of standard set theory in a precise technical sense.  
- It does not require constructing $$d$$ by a “natural” formula independent of the list; the construction *depends on the proposed list*, which is exactly the point.

### Descendants of the idea

Gödel’s incompleteness encodings, Turing’s undecidability of the halting problem, and many diagonal arguments in logic and computer science all share the move: *against any listing of putative total solutions, build a counterexample that flips the diagonal.* Once you see Euclid and Cantor together, you start recognizing “escape constructions” as a family rather than isolated tricks.

---

## Part III — Compare the two proofs

| | Euclid | Cantor |
|--|--------|--------|
| Target | Infinitely many primes | Uncountably many reals |
| Enemy assumption | Finite complete list of primes | Countable complete list of reals |
| Weapon | Product plus one | Diagonal digit flip |
| Witness | A prime factor of $$N$$ | A real $$d$$ missing from the list |
| Field | Number theory | Set theory / foundations |
| Size of “inventory” defeated | Finite | Countably infinite |

**Shared moral.** A proof can be short yet world-changing. The *idea* is a reusable pattern: **escape any allegedly complete inventory of the “wrong size.”**

**Different morals.** Euclid enlarges an infinite *collection of atoms* (primes)—showing a discrete set is infinite. Cantor enlarges *order of infinity* itself—showing that even an infinite listing of reals is too small. Euclid defeats finiteness; Cantor defeats countability.

**Why teach them together.** Both train the same seminar skill: state the enemy assumption clearly, exhibit the construction, justify why the witness escapes, and name what you did *not* claim. That skeleton is exactly what assignment A4 asks you to narrate.

---

## Writing a proof-idea narrative (A4 practice)

A good seminar narrative (≈1200–1500 words for the formal assignment; for now, 300–500 words practice) includes:

1. **Theorem statement** in plain language and then in symbols if helpful.  
2. **Assumption for contradiction** (or constructive outline).  
3. **Key construction** (formula for $$N$$; rule for diagonal digits).  
4. **Why the witness works** (remainder 1; digit disagreement).  
5. **What is not claimed** (one hygiene caveat: $$N$$ may be composite; decimals may be non-unique).  
6. **One sentence on importance** (infinitude of primes; sizes of infinity / diagonal method).

Grade the *clarity of the skeleton*, not ornamental history. A beautiful paragraph of biography cannot replace a correct modular step.

---

## Common confusions

1. **“Euclid proves $$N$$ is always prime.”** — False; only that some new prime divides $$N$$.  
2. **“Euclid gives a formula for the $$n$$th prime.”** — False; it proves unboundedness of the set of primes.  
3. **“Cantor lists all reals then finds a contradiction in arithmetic.”** — He shows no complete list exists; the diagonal number is relative to any proposed list.  
4. **“Uncountable means you cannot count very far.”** — It means no bijection with $$\mathbb{N}$$.  
5. **“Idea of proof means handwaving.”** — It means a correct logical skeleton with named gaps for technical details (representation hygiene, existence of prime factors, etc.).  
6. **“The rationals are uncountable too, by the same argument.”** — No: the rationals *are* countable; diagonalization against a list of *all reals* uses that every infinite decimal sequence is a real, which is not how one enumerates rationals.

---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/euclid-infinite-primes/analysis.md`.

### Status

**Proved** (classical; Euclid, Elements IX.20). Status closed; pedagogy of the *idea* remains active.

### Core statement / slogan

There are infinitely many primes. Proof idea: from finite list $$p_1,\ldots,p_k$$, form $$N=P+1$$ with $$P=\prod p_i$$; any prime factor of $$N$$ is new.

### Definitions to freeze

- **Prime.** Integer $$p>1$$ whose only positive divisors are $$1$$ and $$p$$.
- **Euclid number (idea-level).** Given primes $$p_1,\ldots,p_k$$, set $$N=p_1\cdots p_k+1$$. $$N$$ need not be prime.

### Hygiene (from confusions log)

- Claiming $$N$$ itself is always prime (false; e.g. $$2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031=59\cdot509$$).
- Confusing infinitude with a formula for the $$n$$th prime.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/euclid-infinite-primes/`.

**Recommended order**

1. **Orientation** — Numberphile — Infinite Primes (James Grime / Euclid): [https://www.youtube.com/watch?v=ctC33JAV4FI](https://www.youtube.com/watch?v=ctC33JAV4FI).  
2. **Core** — blackpenredpen — Euclid's proof infinitely many primes: [https://www.youtube.com/watch?v=816JCX5tKD8](https://www.youtube.com/watch?v=816JCX5tKD8).  
3. **Foundation** — Wrath of Math — Proof: infinitely many primes: [https://www.youtube.com/watch?v=ZYkZws-23R8](https://www.youtube.com/watch?v=ZYkZws-23R8).  
4. **Foundation** — Maths and Stats — Number Theory: Infinitude of Primes (Euclid): [https://www.youtube.com/watch?v=YPb0JC18AC4](https://www.youtube.com/watch?v=YPb0JC18AC4).  

**Status reminder:** **Proved** (classical; Euclid, Elements IX.20). Status closed; pedagogy of the *idea* remains active.

---


### Transcript & frames (flagship extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/euclid-infinite-primes/transcripts/` · status: `research/video-research/euclid-infinite-primes/TRANSCRIPT_STATUS.md` · master list: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Captions are auto-downloaded (yt-dlp); treat as navigation aids, not as a substitute for the lesson text.


![Flagship video sample frame]({{ site.baseurl }}/img/video_research/flagships/euclid_numberphile_frame01.jpg)

*Figure. Sample still from a primary flagship video (see pack for timestamps).*

## References

1. Euclid, *Elements*, Book IX, Proposition 20 (classical infinitude of primes).  
2. Stillwell — *Roads to Infinity*; any introductory proofs textbook chapter on contradiction and infinite sets.  
3. Cantor’s diagonal argument as presented in standard set-theory or analysis introductions (many equivalent writeups).  
4. Course links: [Infinity]({{ site.baseurl }}/contents/en/chapter04/04_02_Infinity/), [Cantor page]({{ site.baseurl }}/contents/en/chapter05/05_03_Cantor_Diagonal/), [Gödel]({{ site.baseurl }}/contents/en/chapter05/05_04_Godel_Incompleteness/).

---


Full URL bibliography from video research: `research/video-research/euclid-infinite-primes/references.md`.

### Videos (recommended path)

- Numberphile — Infinite Primes (James Grime / Euclid) (ORIENTATION): https://www.youtube.com/watch?v=ctC33JAV4FI
- blackpenredpen — Euclid's proof infinitely many primes (CORE): https://www.youtube.com/watch?v=816JCX5tKD8
- Wrath of Math — Proof: infinitely many primes (FOUNDATION): https://www.youtube.com/watch?v=ZYkZws-23R8
- Maths and Stats — Number Theory: Infinitude of Primes (Euclid) (FOUNDATION): https://www.youtube.com/watch?v=YPb0JC18AC4

### Papers and web (from research pack)

- Euclid, Elements IX.20 (standard translation editions): https://en.wikipedia.org/wiki/Euclid%27s_Elements
- Wikipedia — Euclid's theorem (survey of proofs): https://en.wikipedia.org/wiki/Euclid%27s_theorem
- Proofs that there are infinitely many primes (math encyclopedia style): https://mathworld.wolfram.com/EuclidsTheorems.html
- Wikipedia — Euclid's theorem: https://en.wikipedia.org/wiki/Euclid%27s_theorem
- MacTutor / history of primes (background): https://mathshistory.st-andrews.ac.uk/HistTopics/Prime_numbers/
- Stanford Encyclopedia-style / intro number theory notes (search Euclid primes): https://en.wikipedia.org/wiki/Prime_number

### Course

- Research pack: `research/video-research/euclid-infinite-primes/` (especially `references.md`, `learning_path.md`).

## Further directions

Next proof ideas in this section: irrationality of $$\sqrt{2}$$ (parity and descent), Königsberg (modeling and degrees), the Four Color Theorem (finite case analysis and computers), Fermat’s Last Theorem and the Poincaré conjecture as modern epics where the *idea* spans whole fields. Each reuses the discipline practiced here: isolate the construction, state the obstruction, and know the limits of the claim.

## Video tham khảo

- **xem trước** — [Infinite Primes - Numberphile](https://www.youtube.com/watch?v=ctC33JAV4FI) — Numberphile, English. Watch first. “Infinite Primes - Numberphile” orients the lesson’s aim: Write Euclid’s argument as assumption → construction → contradiction, with correct modular intuition (remainder 1 when dividing by each listed prime).
- [Euclid's proof that there are infinitely many primes! Classic math proof!](https://www.youtube.com/watch?v=816JCX5tKD8) — blackpenredpen, English. A second pass once the main claim is in view: Write Euclid’s argument as assumption → construction → contradiction, with correct modular intuition (remainder 1 when dividing by each listed prime).
- [Proof: There are Infinitely Many Primes (There is no Largest Prime)](https://www.youtube.com/watch?v=ZYkZws-23R8) — Wrath of Math, English. Further depth after the first two, still tied to this lesson: Write Euclid’s argument as assumption → construction → contradiction, with correct modular intuition (remainder 1 when dividing by each listed prime).
