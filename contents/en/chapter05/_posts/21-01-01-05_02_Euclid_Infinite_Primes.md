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

This **Section 5 flagship** is about the **idea of a proof**, not the longest technical writeup. We study two masterpieces side by side:

1. **Euclid** — infinitely many primes (finite list → one new prime).  
2. **Cantor** — uncountability of the reals (any list → one escaped real).

Both are short. Both reshape what counts as mathematical knowledge. Together they train the skill of reconstructing a proof idea so a classmate can follow the skeleton without drowning in side conditions. If you leave this lecture with only one slogan, make it this: *a proof can be tiny and still world-changing when its construction escapes every allegedly complete inventory.*

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

## Part I — Euclid: infinitely many primes

### Theorem

There are infinitely many prime numbers.

### Historical and conceptual setting

Euclid’s argument (often identified with Book IX, Proposition 20 of the *Elements*) is among the oldest proofs still taught verbatim in spirit. Greek mathematics already knew many primes; the deep claim is not “there are quite a few,” but that **no finite catalogue can exhaust them**. That is a statement about *all* primes, hence a statement that cannot be settled by listing alone. The proof answers a potential skeptic who says: “Perhaps after some point every integer factors using only primes from this fixed finite set.” Euclid shows that such a skeptic is always wrong.

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

### Why remainder 1 is the whole local story

Write $$P = p_1\cdots p_k$$, so $$N = P+1$$. Then for each listed prime $$p_i$$,

$$
N \equiv 1 \pmod{p_i}.
$$

No listed prime divides $$N$$. Whatever prime factors $$N$$ has—whether $$N$$ itself is prime or composite—those factors cannot be among $$p_1,\ldots,p_k$$. The argument never needs to *find* the new prime explicitly as a closed formula; existence of a prime factor of an integer greater than 1 is enough.

### What the idea *is*

- **Reductio:** assume a finite complete inventory of primes.  
- **Witness construction:** $$N = P+1$$ where $$P$$ is the product of all listed primes.  
- **Local obstruction:** each listed prime fails to divide $$N$$.  
- **Global conclusion:** the inventory was incomplete, so there are infinitely many primes.

### What the idea is *not*

- It does not claim $$N$$ itself is prime. Sometimes $$N$$ is composite: for example,

$$
2\cdot 3\cdot 5\cdot 7\cdot 11\cdot 13 + 1 = 30031 = 59\cdot 509,
$$

and both $$59$$ and $$509$$ are primes outside $$\{2,3,5,7,11,13\}$$.  
- It does not produce primes in increasing order.  
- It does not give a practical primality test or a dense supply of primes.  
- It does not require the full strength of unique factorization in heavy form: the elementary fact “every integer greater than 1 has a prime factor” is enough for the idea-level argument.

### A worked micro-example

Take the incomplete list $$\{2,3,5\}$$. Then $$P=30$$ and $$N=31$$, which is prime and not on the list.  
Take $$\{2,3,5,7\}$$. Then $$P=210$$ and $$N=211$$, again prime.  
Take $$\{2,3,5,7,11,13\}$$ as above: $$N$$ is composite, but its prime factors are new. The moral is stable: **newness of a prime factor**, not primality of $$N$$.

### Why it is a model proof

Minimal definitions, maximal conceptual punch. It is often the first proof that feels like *mathematics* rather than calculation. Later theorems—Dirichlet’s theorem on primes in arithmetic progressions, the infinitude of primes of special forms, sieve-theoretic lower bounds—are far harder. Euclid’s *style*—construct a witness that escapes a finite scheme—reappears throughout number theory and combinatorics. Whenever you see “assume finitely many and build one more,” you are hearing Euclid’s echo.

### Variants worth knowing at slogan level

One common variant uses $$N = p_1\cdots p_k - 1$$ when that is larger than 1; the modular obstruction is then remainder $$-1$$ rather than $$1$$. Another pedagogical move is to prove “there is a prime larger than $$n$$” for every $$n$$ by taking the product of all primes up to $$n$$ (or of $$n!$$) and adding 1—this reframes infinitude as “primes unbounded,” which is equivalent for the natural numbers. The underlying escape idea is unchanged.

---

## Part II — Cantor: the reals are uncountable

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

### Hygiene (what a polished proof watches)

- **Non-unique decimals.** Identities such as $$0.1999\ldots=0.2000\ldots$$ mean that digitwise difference is not always real difference. A careful proof either restricts the allowed expansions (e.g. forbid infinite tails of 9s), chooses a digit-flip rule that avoids dual representations, or works in a base and coding where the ambiguity is controlled.  
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

### A tiny numerical cartoon

Suppose someone offers only three listed “reals” in $$(0,1)$$ for illustration:

$$
\begin{align*}
r_1 &= 0.31415\ldots,\\
r_2 &= 0.27182\ldots,\\
r_3 &= 0.16180\ldots.
\end{align*}
$$

Diagonal digits are $$3,7,1$$. Choosing $$e_1=4$$, $$e_2=4$$, $$e_3=4$$ produces $$d=0.444\ldots$$, which differs from each listed row in the corresponding place. In the infinite case the same move runs forever.

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

## Exercises

1. Run Euclid’s construction on $$\{2,3,5\}$$ and on $$\{2,3,5,7,11\}$$; factor $$N$$ if composite and exhibit a new prime.  
2. Write Euclid’s proof with no symbols, then with only symbols—compare clarity for a non-mathematical friend versus a classmate.  
3. Build a $$4\times 4$$ digit table of “listed” decimals and produce a diagonal escape string with an explicit digit rule.  
4. Why does diagonalization alone fail to show “infinitely many primes”? (Wrong domain: primes are not free infinite digit strings.)  
5. Explain in three sentences why $$0.1999\ldots=0.2000\ldots$$ threatens a careless diagonal argument, and how a digit rule using only digits $$\{4,5\}$$ helps.  
6. **A4 micro-draft (≤400 words):** proof-idea narrative for *either* Euclid *or* Cantor using the six-part template above.  
7. Optional: read the dedicated Cantor page in this chapter and the Infinity flagship in Chapter 4; add one sentence connecting cardinality language to diagonalization.

---


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
