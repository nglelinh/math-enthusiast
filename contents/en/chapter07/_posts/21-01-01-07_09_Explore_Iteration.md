---
layout: post
title: "Exploration Studio: Iteration and the Collatz Map"
chapter: '07'
order: 9
owner: Nguyen Le Linh
lang: en
categories:
- chapter07
---

This **Section 7 flagship** is the seminar’s default **exploration portfolio** (**A5** / **LO5**). You will not prove the Collatz conjecture. You will **design experiments**, **keep a research log**, and **report what you learned**—including failed attempts, dead ends, and revised definitions.

**Theme.** What happens when a simple deterministic rule is iterated forever?

**Companion problem page.** [Collatz conjecture (Ch.1)]({{ site.baseurl }}/contents/en/chapter01/01_07_Collatz_Conjecture/) · Related: [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/) · [RH]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) (verification vs proof).

---

## Learning objectives

After this studio you should be able to:

- State the **Collatz ($$3n+1$$) rule** and the open conjecture in precise language.
- Define and compute **total stopping time** (or a clearly documented variant: steps to 1, steps to a smaller value, etc.) for sample seeds.
- Design at least two **controlled experiments** with frozen parameters (range of $$n$$, statistics, plots).
- Keep a **dated research log** with hypotheses, results, surprises, and labels (theorem / conjecture / observation / heuristic).
- Write a short report separating **theorem**, **conjecture**, **numerical observation**, and **speculation**.
- Explain why enormous computational verification is not a proof, using Collatz and RH as parallel morals.
- Transfer the studio method to another Section 7 prompt if you switch topics (with instructor approval).

**Prerequisites.** Integer arithmetic, modular thinking, ability to write a short program (or use a CAS), and willingness to plot data.

---

## 1. Background mathematics

### 1.1 The map

For a positive integer $$n$$, define one Collatz step:

$$
T(n)=
\begin{cases}
n/2 & \text{if }n\text{ is even},\\
3n+1 & \text{if }n\text{ is odd}.
\end{cases}
$$

(Some authors use $$(3n+1)/2$$ when $$n$$ is odd, compressing an automatic even step; **freeze your convention** in the proposal and never mix counts.)

Iterate $$n,\;T(n),\;T(T(n)),\;\ldots$$. The **Collatz conjecture** asserts that for every positive integer $$n$$, some iterate equals 1 (equivalently, the orbit reaches the cycle $$4\to 2\to 1\to 4\to\cdots$$).

![Collatz rule]({{ site.baseurl }}/img/chapter_img/collatz_tree.svg)

*Figure. One step of the map; the conjecture is about all orbits under iteration.*

### 1.2 Stopping times

Common statistics (define carefully):

- **Total stopping time** $$\sigma_\infty(n)$$: number of applications of $$T$$ needed to reach 1.  
- **Stopping time** $$\sigma(n)$$: number of steps to reach a value **strictly smaller** than $$n$$.  
- **Maximum excursion**: largest value appearing in the orbit before descent to 1.

These are empirical probes, not substitutes for a proof. Record formulas in code comments and in the log.

### 1.3 Why the problem is hard (studio-level)

The map mixes a contracting operation (division by 2) with an expanding one ($$3n+1$$). On average, heuristic models suggest orbits tend to decrease—roughly, an odd step followed by the expected number of factors of 2 multiplies by about $$3/4$$—but heuristics are not proofs, and they can hide rare counterexample-shaped events. The map is deterministic, yet statistics of stopping times look irregular; that is **complexity of orbits**, not randomness of the rule.

Partial results exist (density of integers that eventually fall below themselves; verification to enormous bounds; results on almost all integers in various senses). Your studio should **cite** partial results you mention, not invent them.

**From the video/research pack (must-know slogans for A5 writeups).**

- **$$\operatorname{Col}_{\min}(N)$$** = smallest value appearing in the forward orbit of $$N$$. Full Collatz: $$\operatorname{Col}_{\min}(N)=1$$ for every positive $$N$$ (**open**).  
- **Tao (2019):** for almost all $$N$$ (logarithmic density), $$\operatorname{Col}_{\min}(N)<f(N)$$ whenever $$f(N)\to\infty$$—no matter how slowly. This is a **theorem about almost all seeds**, not a proof of the full conjecture. Cite [arXiv:1909.03562](https://arxiv.org/abs/1909.03562) if you mention it.  
- **Syracuse / accelerated maps** change step counts: freeze $$T$$ vs odd-only map in your proposal.  
- **Critical constant** $$\log 3/\log 4\approx 0.7925$$ appears in classical almost-all power-saving results (Korec line)—optional reading, not required code.

Full extraction: Ch.1 Collatz essay §6–7 and `research/video-research/collatz/analysis.md`.

### 1.4 Inverse tree

Working backwards: every $$m$$ has preimage $$2m$$. If $$m\equiv 2\pmod{3}$$ and $$(m-1)/3$$ is a positive odd integer (check conditions carefully for your $$T$$), that may also be a preimage. The tree of numbers flowing to 1 is a rich experimental object: breadth at depth $$k$$, residue patterns, coverage of $$\mathbb{N}$$.

### 1.5 Iteration beyond Collatz

The same studio method applies to:

- logistic map $$x\mapsto rx(1-x)$$ on $$[0,1]$$ (chaos lite);  
- Syracuse-type maps;  
- Babylonian square-root iteration;  
- Newton’s method on a polynomial.

If you switch topic, keep the **portfolio structure** below. Collatz remains the default because it is elementary to code and genuinely open.

### 1.6 Verification versus proof

Collatz has been checked for all starting values up to extremely large bounds (cite a reliable source in your report—the bound changes over time). Parallel moral from RH: zeros computed high on the critical line support belief but do not close the problem. **Infinite domains are not exhausted by finite searches.**

---

## 2. Portfolio structure (A5 milestones)

| Milestone | Week (passport) | Deliverable |
|-----------|-----------------|-------------|
| Proposal | W11 | Question, definitions, methods, tools, success criteria (1–2 pages) |
| Process log | W13 | Dated entries; experiments; dead ends |
| Final report | W15 | 6–10 pages equivalent: findings + limits + next questions |

**AI policy.** Code assistance allowed with disclosure; the **log of your experiments and interpretations** must be yours. Paste transcripts of AI chats if required by the syllabus.

---

## 3. Conjecture versus proof versus experiment

| Label | Meaning | Example |
|-------|---------|---------|
| **Theorem** | Proved statement | “If $$n$$ is a power of 2, orbit reaches 1 in $$\log_2 n$$ halvings” |
| **Conjecture** | Open | Full Collatz for all positive integers |
| **Verification** | Checked for $$n\le N$$ | Cite bound and method |
| **Observation** | Your data | “Mean stopping time for $$n\le 10^4$$ was …” |
| **Heuristic** | Probabilistic model | Average multiplicative factor arguments |

**Success criteria (customize, but be concrete):**

1. Proposal accepted with frozen definitions before major coding.  
2. At least two experiments from §5 completed with figures or tables.  
3. Log with ≥8 dated entries including at least two failures.  
4. Report states explicitly what you did **not** prove.  
5. One numerical conjecture formed, tested, and marked alive/dead/inconclusive.  
6. Verification-vs-proof paragraph with a citation to computational bounds.

Non-goals: “prove Collatz,” “find a counterexample for fame without methodology,” “run $$N=10^{18}$$ without a plan.”

---

## 4. Research log standards

Each entry should include:

- **Date**  
- **Intent** (what you tried and why)  
- **Action** (code snippet summary, parameters, hand calc)  
- **Result** (numbers, plot description, errors)  
- **Label** (theorem / conjecture / observation / heuristic / bug)  
- **Interpretation** (what changed in your beliefs)  
- **Next step**

**Failed attempts count.** “Tried $$N=10^7$$ and ran out of memory; switched to sampling” is excellent. **Bugs count.** Off-by-one in stopping time is a log event, not a silent fix.

**Reproducibility.** Record language, integer overflow policy (Python big ints vs fixed width), and PRNG seeds if sampling.

---

## 5. Experiments

Do **at least two** of A–G; flagship students should aim for three.

### Experiment A — Hand orbits (20–40 min)

Compute orbits for $$n=1,2,\ldots,20$$ by hand or with a tiny program. Record steps to 1.

**Hypothesis before computing:** “Odd starts always take longer than even starts nearby.” Then check.

**Success criterion:** complete table + hypothesis verdict.

### Experiment B — Stopping time plot (45–120 min)

For $$n=1$$ to $$N$$ (start with $$N=200$$, then $$10^4$$ or $$10^5$$), plot total stopping time vs $$n$$. Mark record holders.

![Stopping time sketch]({{ site.baseurl }}/img/chapter_img/collatz_stopping_time.svg)

*Figure. Cartoon of irregular stopping times—make a real plot in your log.*

**Success criterion:** plot + list of top 5 record $$n$$ in range + caption separating observation from law.

### Experiment C — Residue patterns (40–90 min)

Condition on $$n\bmod 8$$ or $$n\bmod 16$$. Compare average stopping times and average maxima.

**Caution:** correlation ≠ law; small moduli can mislead; multiple-testing bias if you scan many moduli.

**Success criterion:** table of means by residue + skeptical interpretation paragraph.

### Experiment D — Inverse tree (stretch, 60–120 min)

Build all numbers that reach 1 in exactly $$k$$ steps for $$k\le K$$ (choose feasible $$K$$). Plot counts vs $$k$$. Which residue classes dominate early layers?

**Success criterion:** algorithm description + count table + one surprise.

### Experiment E — Verification literacy (30–45 min)

Find a reliable source on how far Collatz has been checked computationally. Cite it. Write three sentences on verification vs proof, linking the RH lesson.

**Success criterion:** citation + reflection (no blog-of-unknown-quality alone).

### Experiment F — Heuristic micro-model (45–90 min)

Write a probabilistic cartoon: odd numbers map to $$3n+1$$ then divide by 2 until odd again; estimate expected log-change. Compare the cartoon’s predicted growth of stopping time with your empirical means (order-of-magnitude only).

**Success criterion:** derivation of the cartoon + empirical comparison + “not a proof” banner.

### Experiment G — Alternate iteration (if switching)

Logistic map at $$r=4$$: histogram of iterates; sensitive dependence demo. Or Newton on $$z^2-1$$ in complex plane (basins)—only with instructor OK. Reuse proposal/log/report structure.

**Success criterion:** same portfolio quality as Collatz.

---

## 6. Proposal template (fill this)

1. **Question.** Example: “How does total stopping time grow for $$n\le N$$? Are there residue classes with systematically longer trajectories?”  
2. **Definitions.** Freeze $$T$$, stopping time, and any reduced Syracuse map.  
3. **Methods.** Language, ranges, plots, statistics, hardware limits.  
4. **Success criteria.** Not “prove Collatz.” Instead: “plots for $$N=10^5$$; two empirically supported conjectures; falsify one naive guess.”  
5. **Risks.** Overflow (if not using big integers); off-by-one; selection bias; p-hacking moduli; AI-written code you do not understand.  
6. **Ethics / disclosure.** AI tools list.

Submit the proposal before major coding so the question is not reverse-engineered from plots.

---

## 7. Report outline

1. Introduction: Collatz statement; what you are *not* proving.  
2. Definitions and methods (frozen conventions).  
3. Experiments: design, results, figures.  
4. Conjectures you formed; which died; which survived *your* tests.  
5. Limitations (range, bias, bugs found).  
6. Connection to course themes (iteration, open problems, experimental math, verification vs proof).  
7. References and AI disclosure.

**Rubric emphasis (seminar):** clarity of question, quality of log, correctness of small computations, honesty about limits—not novelty of a “new Collatz theorem.”

---

## 8. Common confusions

1. **“I checked to $$10^{18}$$, so Collatz is true.”** — Strong evidence for the range checked; not a proof for all $$n$$.  
2. **“The rule is random.”** — Fully deterministic; orbit statistics can still look irregular.  
3. **“$$3n+1$$ always increases forever.”** — Combined with divisions by 2, trajectories often descend on average (heuristic)—make this precise only if you discuss heuristics carefully.  
4. **“A cycle other than 4–2–1 is known for positive integers.”** — Do not claim exotic cycles without a cited, verified source; the standard conjecture is that none exist for positive integers under $$T$$.  
5. **“Exploration means no standards.”** — Studio honesty standards are stricter than calculation homework.  
6. **“Stopping time definitions are universal.”** — They are not; mismatched definitions produce fake disagreements.  
7. **“Tao already solved Collatz.”** — Tao 2019 is almost-all / almost-bounded (logarithmic density), not the full conjecture—see Ch.1 §7.

---

## 9. Exercises (warm-up before proposal)

1. Compute the full orbit of $$27$$ until 1; count steps under your frozen $$T$$.  
2. Prove that every power of 2 reaches 1; give exact step count.  
3. Show that there is no prime triple $$(p,p+2,p+4)$$ except $$(3,5,7)$$—and explain why this exercise is *not* Collatz (toolkit separation from the primes studio).  
4. Write pseudocode for `stopping_time(n)` with an explicit overflow/timeout policy.  
5. Formulate one falsifiable hypothesis about stopping times.  
6. Draft A5 proposal Sections 1–2 (question + definitions) in ≤200 words.

---

## 10. Checkpoint rubric

| Done? | Item |
|-------|------|
| ☐ | Proposal with frozen definitions and success criteria |
| ☐ | ≥2 experiments with figures/tables |
| ☐ | Log ≥8 dated entries, ≥2 failures |
| ☐ | Verification-vs-proof paragraph with citation |
| ☐ | Report labels theorem/conjecture/observation |
| ☐ | AI disclosure |
| ☐ | One open question for future work |

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/collatz/`.

**From the research pack (must-know slogans)**

- Reuse full Collatz video pack: `research/video-research/collatz/`.
- **Tao 2019** almost-all / almost-bounded ≠ full Collatz (still **open** as of 2026).
- Freeze map $$T$$ vs Syracuse; log stopping times; computation ≠ proof.

**Recommended order**

1. **Orientation** — Veritasium — Collatz: [https://www.youtube.com/watch?v=094y1Z2wpJg](https://www.youtube.com/watch?v=094y1Z2wpJg).  
2. **Intuition** — Numberphile — UNCRACKABLE Collatz: [https://www.youtube.com/watch?v=5mFpVDpKX70](https://www.youtube.com/watch?v=5mFpVDpKX70).  
3. **Foundation** — Chamberland 3x+1 status Part 1: [https://www.youtube.com/watch?v=t1I9uHF9X5Y](https://www.youtube.com/watch?v=t1I9uHF9X5Y).  
4. **Core** — Tao Notorious Collatz (mathtube): [https://mathtube.org/lecture/video/notorious-collatz-conjecture](https://mathtube.org/lecture/video/notorious-collatz-conjecture).  
5. **Core** — Tao Notorious Collatz (YouTube): [https://www.youtube.com/watch?v=X2p5eMWyaFs](https://www.youtube.com/watch?v=X2p5eMWyaFs).  
6. **Frontier** — Tao IAS almost-all Collatz: [https://www.youtube.com/watch?v=k-dtx8s2ehM](https://www.youtube.com/watch?v=k-dtx8s2ehM).  

**Official / primary written hubs**

- Tao arXiv:1909.03562: https://arxiv.org/abs/1909.03562  
- Lagarias overview arXiv:2111.02635: https://arxiv.org/abs/2111.02635  

Complete URL bibliography: `research/video-research/collatz/references.md`.

### Transcript & frames (flagship extract)

Caption transcripts and time-chunk units for Collatz pack videos: `research/video-research/collatz/transcripts/` · status: `research/video-research/collatz/TRANSCRIPT_STATUS.md` · master list: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

**Sample frames** (orientation stills for studio context):

![Collatz video sample frame]({{ site.baseurl }}/img/video_research/collatz/5mFpVDpKX70_frame01.jpg)

*Figure. Sample still from a primary Collatz orientation video (see pack for timestamps).*

## 11. References and course links


### Video research pack (all URLs)

Complete list: `research/video-research/collatz/references.md`.

1. Veritasium — Collatz — https://www.youtube.com/watch?v=094y1Z2wpJg  
2. Numberphile — UNCRACKABLE Collatz — https://www.youtube.com/watch?v=5mFpVDpKX70  
3. Chamberland 3x+1 status Part 1 — https://www.youtube.com/watch?v=t1I9uHF9X5Y  
4. Tao Notorious Collatz (mathtube) — https://mathtube.org/lecture/video/notorious-collatz-conjecture  
5. Tao Notorious Collatz (YouTube) — https://www.youtube.com/watch?v=X2p5eMWyaFs  
6. Tao IAS almost-all Collatz — https://www.youtube.com/watch?v=k-dtx8s2ehM  
7. Tao arXiv:1909.03562 — https://arxiv.org/abs/1909.03562  
8. Lagarias overview arXiv:2111.02635 — https://arxiv.org/abs/2111.02635  
9. Full bibliography (pack) — research/video-research/collatz/references.md  
10. Quanta Tao Collatz — https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/  
11. Research pack folder: `research/video-research/collatz/`.

Complete URL list from Collatz video research: `research/video-research/collatz/references.md`. Do **not** treat popular videos as proofs.

1. Lagarias overview: https://arxiv.org/abs/2111.02635 · PDF https://arxiv.org/pdf/2111.02635 · SFU mirror http://www.cecm.sfu.ca/organics/papers/lagarias/  
2. Tao almost-all paper: https://arxiv.org/abs/1909.03562 · PDF https://arxiv.org/pdf/1909.03562 · blog https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/  
3. Tao 2011 Collatz blog: https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/  
4. Primary videos: Veritasium https://www.youtube.com/watch?v=094y1Z2wpJg · Numberphile https://www.youtube.com/watch?v=5mFpVDpKX70 · Chamberland https://www.youtube.com/watch?v=t1I9uHF9X5Y · Tao mathtube https://mathtube.org/lecture/video/notorious-collatz-conjecture · Tao YT https://www.youtube.com/watch?v=X2p5eMWyaFs · slides https://terrytao.files.wordpress.com/2020/02/collatz.pdf · IAS https://www.youtube.com/watch?v=k-dtx8s2ehM · Easy Theory https://www.youtube.com/watch?v=Lr6qc_9M0Ks  
5. Secondary videos: https://www.youtube.com/watch?v=m4CjXk_b8zo · https://www.youtube.com/watch?v=LqKpkdRRLZw · https://www.youtube.com/watch?v=O2_h3z1YgEU · https://youtu.be/wH141HLD57o · https://www.youtube.com/watch?v=vT4VJyXWHlo · https://www.numberphile.com/videos/uncrackable-the-collatz-conjecture  
6. Web: Wikipedia https://en.wikipedia.org/wiki/Collatz_conjecture · Quanta https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/ · Chamberland hub https://chamberland.math.grinnell.edu/3x.html · Basel https://dmi.unibas.ch/en/news/details/lecture-in-basel-terence-tao-and-the-notorious-collatz-conjecture/ · Stanford https://mathematics.stanford.edu/events/kiddie-colloquium/almost-almost-collatz · Pitt https://www.mathematics.pitt.edu/content/note-collatz-conjecture · Chamberland PDF http://www.math.grinnell.edu/~chamberl/papers/3x_survey_eng.pdf · Lagarias PDF https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa15/addcomments/Lagarias_3x+1AndItsGeneralizations.pdf · RISM https://www.rism.it/rism-channel/2021/riemann-prize-week/the-notorious-collatz-conjecture-terence-tao  
7. Course: [Collatz problem page]({{ site.baseurl }}/contents/en/chapter01/01_07_Collatz_Conjecture/), [Chaos]({{ site.baseurl }}/contents/en/chapter04/04_05_Chaos/), [Riemann]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/). Pack: `research/video-research/collatz/`.  
8. Optional alternate studios: Kakeya, packing, primes, randomness, fourth dimension, map colors, infinity—reuse this portfolio structure.

---

## Further directions

W11–W13 of the seminar are built around this studio. Bring plots to class; peer feedback targets methods, not bravado. If Collatz becomes psychologically sticky (perfectly normal), schedule a hard stop and write about limits of computation as a feature of the project, not a personal failure.

### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/explore-iteration/transcripts/` · status: `research/video-research/explore-iteration/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/explore-iteration_094y1Z2wpJg_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

