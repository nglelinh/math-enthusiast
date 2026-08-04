---
layout: post
title: "Irrationality of √2"
chapter: '05'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter05
---

The number $$\sqrt{2}$$ is not a ratio of integers. This classical discovery—associated with the Pythagorean tradition and often cast as a crisis for the belief that all lengths are commensurable—remains one of the best first proofs in a mathematics education. The argument is short, but its **idea** is deep: assume a lowest-terms representation, force a shared factor of 2, and contradict minimality. Parity becomes a wedge that splits the assumption of rationality.

This lecture develops that idea carefully, contrasts equivalent formulations (infinite descent, unique factorization light), and situates the result among other irrationality proofs. The goal is a skeleton you could teach at a whiteboard in ten minutes—and defend under questioning for an hour.

---

## Learning objectives

After this lecture you should be able to:

- State and prove that $$\sqrt{2}$$ is irrational via the even-even contradiction in lowest terms.
- Explain why “lowest terms” (or an equivalent minimality) is essential to the argument.
- Relate the proof to infinite descent and to divisibility by 2.
- Adapt the idea to $$\sqrt{3}$$ or to $$\sqrt{p}$$ for a prime $$p$$, noting where the same parity trick needs generalization.
- Avoid confusions such as “$$\sqrt{2}$$ is irrational because its decimal never ends.”
- Write a clean proof-idea narrative for seminar practice.

**Prerequisites.** Integers, even and odd, fractions in lowest terms, and the statement $$p^2=2q^2$$ as the algebraic form of $$\sqrt{2}=p/q$$. Proof by contradiction.

---

## 1. Commensurability and a geometric reading

Two lengths are **commensurable** if there is a common unit measuring both an integer number of times—equivalently, if their ratio is rational. The diagonal of a unit square has length $$\sqrt{2}$$. If $$\sqrt{2}$$ were rational, the side and diagonal would be commensurable. The irrationality proof says they are not: no common measuring stick with integer counts exists for both.

Greek mathematics did not use modern real-number language; the discovery was often phrased in terms of incommensurable magnitudes. Modern writeups use integers and squares because that is the cleanest algebraic packaging of the same idea.

---

## 2. Theorem and setup

**Theorem.** $$\sqrt{2}$$ is irrational: there are no integers $$p,q$$ with $$q\neq 0$$ such that $$\sqrt{2}=p/q$$.

Equivalently: the equation

$$
p^2 = 2q^2
$$

has no solutions in integers with $$q\neq 0$$. (If $$q<0$$ one may replace $$q$$ by $$\lvert q\rvert$$; signs do not help.)

---

## 3. The classical proof (idea with all essential steps)

Assume, for contradiction, that $$\sqrt{2}=p/q$$ where $$p,q$$ are integers, $$q>0$$, and the fraction is in **lowest terms**: $$\gcd(p,q)=1$$.

Then $$p^2 = 2q^2$$. The right-hand side is even, so $$p^2$$ is even. A standard lemma says that if $$p^2$$ is even then $$p$$ is even: if $$p$$ were odd, $$p^2$$ would be odd. Write

$$
p = 2k
$$

for some integer $$k$$. Substitute:

$$
(2k)^2 = 2q^2 \implies 4k^2 = 2q^2 \implies q^2 = 2k^2.
$$

Thus $$q^2$$ is even, so $$q$$ is even. But then $$2$$ divides both $$p$$ and $$q$$, contradicting $$\gcd(p,q)=1$$.

Therefore no such lowest-terms representation exists, and $$\sqrt{2}$$ is irrational.

### Why the lemma “even square ⇒ even root” holds

If $$p=2m+1$$, then

$$
p^2 = 4m^2+4m+1 = 2(2m^2+2m)+1,
$$

which is odd. So the only way $$p^2$$ is even is if $$p$$ is even. This is modular arithmetic in disguise:

$$
p\equiv 0\ \text{or}\ 1\pmod{2},\qquad p^2\equiv 0\ \text{or}\ 1\pmod{2}.
$$

---

## 4. What the idea *is*

- **Assume rationality** in a normalized form (lowest terms).  
- **Transfer divisibility** from $$p^2$$ to $$p$$ via modular constraints.  
- **Repeat** for $$q$$ after substitution.  
- **Contradict** the normalization (common factor 2).

The engine is not decimal expansions; it is **divisibility**.

---

## 5. Infinite descent formulation

One can rephrase without an explicit gcd. Suppose $$p^2=2q^2$$ with positive integers $$p,q$$. Then $$p$$ is even, $$p=2k$$, and $$q^2=2k^2$$, so $$q$$ is even, $$q=2\ell$$, and

$$
k^2 = 2\ell^2
$$

with strictly smaller positive integers $$k<p$$ (since $$p=2k$$ and $$p>0$$). Repeating forever yields an infinite decreasing sequence of positive integers, which is impossible.

This is **infinite descent** in Fermat’s style: a solution generates a smaller solution, ad infinitum. Lowest-terms language and descent language are two packages of the same contradiction.

---

## 6. What the idea is *not*

- It is not “the decimal of $$\sqrt{2}$$ never terminates, therefore irrational.” Many rationals have non-terminating decimals ($$1/3=0.333\ldots$$). Non-terminating *and non-repeating* is equivalent to irrationality for decimals, but proving non-repetition is not easier than the parity proof.  
- It is not a claim about approximations: $$\sqrt{2}$$ *is* a limit of rationals; irrationality denies equality with a ratio, not approximability.  
- It does not by itself classify all irrational numbers or prove transcendence ($$\sqrt{2}$$ is algebraic).

---

## 7. Extending the pattern: $$\sqrt{3}$$, $$\sqrt{p}$$

For $$\sqrt{3}$$, assume $$p^2=3q^2$$ in lowest terms. Then $$3\mid p^2$$ implies $$3\mid p$$ (because 3 is prime), write $$p=3k$$, obtain $$q^2=3k^2$$, hence $$3\mid q$$, contradiction. The key upgraded lemma is:

**If a prime divides a product (or a square), it divides the base.**

For general prime $$p$$, the same argument shows $$\sqrt{p}$$ is irrational. For general integer $$n$$ that is not a perfect square, $$\sqrt{n}$$ is irrational; the clean modern route uses unique factorization or the prime factorization of $$n$$ having an odd exponent. The $$\sqrt{2}$$ proof is the seed of that family.

---

## 8. Why it matters

- **Prototype of number-theoretic rigor.** Assumptions about integers yield contradictions via divisibility.  
- **Gateway to algebra.** Polynomial roots, algebraic integers, and field extensions all sit downstream of “not rational.”  
- **Proof culture.** Normalization (lowest terms), lemmas about parity, and descent are reusable tools.  
- **Historical consciousness.** Incommensurability forced Greek mathematics beyond pure rational measure—an early lesson that intuition about “all magnitudes are ratios” can fail.

In a seminar on *ideas of proof*, $$\sqrt{2}$$ earns its place beside Euclid and Cantor not because the result is exotic, but because the skeleton is teachable and the mistakes are diagnostic. When a student forgets lowest terms, they reveal that they do not yet see where the contradiction lives. When they appeal to “the decimal never ends,” they reveal a confusion between representation and rationality. Correcting those errors is part of training mathematical taste.

The same divisibility engine reappears in proving that $$\sqrt[3]{2}$$ is irrational, that certain Diophantine equations have no solutions, and—far downstream—in local-to-global principles where prime-by-prime constraints assemble into global impossibilities. Learning to hear “even square, hence even base” as a modular fact is small; learning to *look for* such transfer of divisibility is large.

---

## 9. A second proof sketch (unique factorization light)

Suppose $$p^2=2q^2$$. Factor $$p$$ and $$q$$ into primes. The exponent of 2 in the left side’s factorization is even (as a square), while on the right it is odd plus an even number (the extra factor 2 plus the even exponents in $$q^2$$)—contradiction. This version makes the **valuation** idea explicit: the 2-adic valuation $$v_2(p^2)$$ is even, but $$v_2(2q^2)=1+v_2(q^2)$$ is odd. Valuation parity is a modern packaging of the classical even-odd dance.

---

## Common confusions

1. **“Non-terminating decimal ⇒ irrational.”** — False; $$1/3$$ terminates only in the sense of repeating.  
2. **“Lowest terms is optional decoration.”** — Without minimality or descent, “both even” is not yet a contradiction.  
3. **“The proof shows $$\sqrt{2}$$ cannot be approximated by rationals.”** — False; rationals approximate it arbitrarily well.  
4. **“$$p^2$$ even implies $$p$$ even” is special magic for 2.”** — For prime moduli the analogue is Fermat/Euclid’s lemma style reasoning.  
5. **“Idea of proof means skip the odd-square lemma.”** — That lemma *is* the idea’s hinge; name it.

---

## Exercises

1. Write the full classical proof that $$\sqrt{2}$$ is irrational, including the odd-square lemma.  
2. Prove $$\sqrt{3}$$ is irrational by the same template.  
3. Where does the argument fail if you try to prove $$\sqrt{4}$$ is irrational? (It *is* rational.)  
4. Reformulate the $$\sqrt{2}$$ proof purely as infinite descent with no gcd words.  
5. Using prime factorizations, explain the valuation contradiction for $$p^2=2q^2$$.  
6. True or false: if $$x^2$$ is divisible by 4, then $$x$$ is divisible by 4? Prove or give a counterexample; contrast with divisibility by 2.  
7. **Narrative (≤300 words).** Explain the proof to a high-school student who knows even/odd but not the word “irrational.”  
8. Optional: show $$\sqrt[3]{2}$$ is irrational by a related divisibility argument.

---


---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/irrationality-sqrt2/analysis.md`.

### Status

**Proved** (classical Pythagorean / Euclidean tradition). Many independent proofs (parity, descent, unique factorization, geometric Apostol).

### Core statement / slogan

$$\sqrt{2}$$ is irrational: if $$a/b$$ in lowest terms with $$a^2=2b^2$$, then $$a$$ and $$b$$ are both even — contradiction.

### Definitions to freeze

- **Rational.** $$x=a/b$$ with $$a,b\in\mathbb{Z}$$, $$b\neq 0$$.
- **Infinite descent (idea).** From a positive integer solution produce a strictly smaller one — impossible.

### Hygiene (from confusions log)

- Thinking the proof only works for √2 and not primes $$p\equiv 3\pmod 4$$ etc. without adapting the parity argument.
- Confusing irrationality with transcendence.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/irrationality-sqrt2/`.

**Recommended order**

1. **Orientation** — D!NG — A Proof That The Square Root of Two Is Irrational: [https://www.youtube.com/watch?v=LmpLlcNjPj0](https://www.youtube.com/watch?v=LmpLlcNjPj0).  
2. **Core** — Wrath of Math — Most Beautiful Proof √2 irrational (Apostol geometric): [https://www.youtube.com/watch?v=NegYPgMAua4](https://www.youtube.com/watch?v=NegYPgMAua4).  
3. **Survey** — Tipping Point Math — 5 Best Proofs √2 irrational: [https://www.youtube.com/watch?v=zEXcsZo4hOQ](https://www.youtube.com/watch?v=zEXcsZo4hOQ).  
4. **Foundation** — Khan Academy — Proof √2 is irrational: [https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:irrational-numbers/x2f8bb11595b61c86:proofs-concerning-irrational-numbers/v/proof-that-square-root-of-2-is-irrational](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:irrational-numbers/x2f8bb11595b61c86:proofs-concerning-irrational-numbers/v/proof-that-square-root-of-2-is-irrational).  

**Status reminder:** **Proved** (classical Pythagorean / Euclidean tradition). Many independent proofs (parity, descent, unique factorization, geometric Apostol).

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/irrationality-sqrt2/transcripts/` · status: `research/video-research/irrationality-sqrt2/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/irrationality-sqrt2_NegYPgMAua4_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References

1. Classical Greek tradition on incommensurability (secondary historical sources).  
2. Any introduction to proofs textbook: chapter on contradiction and integers.  
3. Hardy & Wright — *An Introduction to the Theory of Numbers* (context for related irrationalities).  
4. Course: [Euclid infinitude]({{ site.baseurl }}/contents/en/chapter05/05_02_Euclid_Infinite_Primes/) for another classical number-theory proof idea.

---


Full URL bibliography from video research: `research/video-research/irrationality-sqrt2/references.md`.

### Videos (recommended path)

- D!NG — A Proof That The Square Root of Two Is Irrational (ORIENTATION): https://www.youtube.com/watch?v=LmpLlcNjPj0
- Wrath of Math — Most Beautiful Proof √2 irrational (Apostol geometric) (CORE): https://www.youtube.com/watch?v=NegYPgMAua4
- Tipping Point Math — 5 Best Proofs √2 irrational (SURVEY): https://www.youtube.com/watch?v=zEXcsZo4hOQ
- Khan Academy — Proof √2 is irrational (FOUNDATION): https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:irrational-numbers/x2f8bb11595b61c86:proofs-concerning-irrational-numbers/v/proof-that-square-root-of-2-is-irrational

### Papers and web (from research pack)

- Wikipedia — Square root of 2 / proofs of irrationality: https://en.wikipedia.org/wiki/Square_root_of_2
- Apostol, AMM 2000 geometric proof (reference): https://www.jstor.org/stable/2589021
- Homeschoolmath writeup of classical proof: https://www.homeschoolmath.net/teaching/proof_square_root_2_irrational.php
- Wikipedia — Proof that √2 is irrational: https://en.wikipedia.org/wiki/Square_root_of_2#Proofs_of_irrationality
- MathWorld — Irrational Number: https://mathworld.wolfram.com/IrrationalNumber.html

### Course

- Research pack: `research/video-research/irrationality-sqrt2/` (especially `references.md`, `learning_path.md`).

## Further directions

- Generalize to $$\sqrt{n}$$ for non-square $$n$$.  
- Explore continued fractions for $$\sqrt{2}$$ as the constructive twin of irrationality (best rational approximations).  
- Compare with irrationality of $$e$$ and $$\pi$$ (harder; different toolkits).  
- Note one precise question you still have—good questions are part of mathematical practice.
