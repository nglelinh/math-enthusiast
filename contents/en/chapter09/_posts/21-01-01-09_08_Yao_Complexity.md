---
layout: post
title: "Yao: Minimax, Communication Complexity, and Foundations (Turing 2000)"
chapter: '09'
order: 8
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

Picture two data scientists on opposite continents: Alice holds a massive 1-billion-bit file $$x$$, and Bob holds a 1-billion-bit file $$y$$. They want to answer one simple yes/no question: *are our two files bit-for-bit identical?* If they insist on 100% certainty with zero chance of error, they practically have to transmit all 1 billion bits across the ocean. Yet if they allow a few coin flips and tolerate an error below one in a billion, Alice only needs to send a tiny hash fingerprint a few dozen bits long!

That deceptively simple puzzle launched an entire empire of theoretical computer science pioneered by **Andrew Chi-Chih Yao**, winner of the **2000 A.M. Turing Award** for fundamental contributions to the theory of computation—including complexity-based cryptography, communication complexity, and the analysis of randomized algorithms. The citation names a distinctive *style* of mathematics: turn informal computational questions into sharp combinatorial or information-theoretic objects, then prove lower bounds that no clever coding trick can evade.

This lecture unpacks three interlocking ideas: **Yao’s minimax principle**, **communication complexity**, and Yao’s bridge to **pseudorandomness** and early **quantum computing** theory. Official materials: [amturing.acm.org](https://amturing.acm.org/).

---

## Learning objectives

After this lecture you should be able to state Yao’s minimax principle in slogan form and explain why it equates average-case deterministic cost under a hard distribution with worst-case randomized cost; define two-party communication complexity of a Boolean function $$f$$ and give the equality and disjointness examples at literacy level; relate communication lower bounds to “why some tasks need many bits no matter the protocol”; name one connection from Yao-style complexity thinking to cryptography or pseudorandomness; and place early quantum complexity (Yao’s quantum circuit model contributions among others) as *foundations awareness* next to [quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/) without claiming a full quantum algorithms course.

**Prerequisites / cross-links.** Comfort with expectation and basic probability; the idea that algorithms may flip coins; decision problems from [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) and [complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/). Cryptography as application culture: [number theory & crypto]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/). Chapter overview: [Turing chapter]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/).

---

## Key ideas: What Are Communication Complexity and Yao's Minimax Principle?

When mathematicians try to prove a problem is *hard* on ordinary Turing machines (like P vs NP), they often hit a wall because CPU steps are wildly tangled to analyze. **Communication Complexity**, introduced by Yao in 1979, made a brilliantly clean move: **grant Alice and Bob unlimited local computing power, and count only the bits they must exchange!**

Why is this seemingly idealized model so potent? Because lower bounds on **information crossing a cut** can be proved with crisp linear algebra (matrix rank), combinatorial rectangles, and information theory—and then **transfer directly** to real-world bottlenecks:
- **Streaming algorithms:** how much RAM is required to count distinct items in a 10-billion-event stream? Slice the stream into a first half (Alice) and second half (Bob)—the RAM state handed across the midpoint *is* Alice's message to Bob!
- **VLSI chip design and data structures:** the wires crossing the midline of a silicon chip form a literal communication channel.
- **Yao's Minimax Principle:** borrowing John von Neumann's minimax theorem from zero-sum game theory (like Rock–Paper–Scissors), Yao recast the battle between *Algorithm Designer* and *Worst-Case Adversary* as a matrix game. To prove that *every* randomized algorithm is slow, you don't have to analyze randomized algorithms one by one—you just construct **one hard input distribution** and prove every *deterministic* algorithm is slow on average under it!

---

## 1. Why Yao’s mathematics feels different

Many algorithm lectures optimize upper bounds: “here is a clever data structure; here is runtime $$O(n\log n)$$.” Yao’s signature contribution to *foundations* is the dual skill: **lower bounds under resource accounting**. If you only know upper bounds, you do not know when you are done. Communication complexity, circuit complexity interfaces, and complexity-based cryptography all need impossibility theorems that survive clever encodings.

Yao’s career also helped shape theoretical computer science as a *mathematical* culture in Asia and globally: research institutes, student lineages, and the insistence that discrete problems admit rigorous combinatorial analysis. The Turing medal is a spotlight on that culture as much as on any single paper.

---

## 2. Randomized algorithms and Yao’s minimax principle

### The setup

A **randomized algorithm** for a problem may flip coins during execution. Its cost on an input $$x$$ is a random variable (time, number of queries, communication bits, …). One often studies **worst-case expected cost**:

$$
\max_x \mathbb{E}[\mathrm{cost}(A,x)],
$$

where the expectation is over the algorithm’s coins, and the max is over inputs of a given size.

A **deterministic** algorithm has no coins; its cost on $$x$$ is fixed. Given a distribution $$\mu$$ on inputs, one studies **average cost** $$\mathbb{E}_{x\sim\mu}[\mathrm{cost}(D,x)]$$.

### The principle (slogan form)

Yao’s minimax principle, in the form used in algorithms and complexity, says roughly:

> The **worst-case expected cost of the best randomized algorithm** equals the **average cost, under a worst-case input distribution, of the best deterministic algorithm**.

More formally (for a finite set of deterministic algorithms and inputs, with cost matrix $$C_{D,x}$$), viewing randomization as a distribution over deterministic algorithms, the value of the zero-sum game between algorithm-chooser and input-chooser equals the dual game where nature first picks a hard distribution and the algorithm responds deterministically. In analysis practice this means:

- to **lower bound** randomized complexity, it suffices to exhibit a distribution $$\mu$$ such that *every* deterministic algorithm has high average cost under $$\mu$$;
- to **upper bound**, a randomized algorithm is a distribution over deterministic ones, so average-case deterministic analysis under any $$\mu$$ cannot exceed the randomized worst-case cost.

This is von Neumann minimax applied to computational cost. The intellectual gift is not the game theory per se—it is the **method**: hard distributions become lower-bound tools.

### Explanation: How Yao's Minimax Principle Works in Four Steps

1. **Frame the lower bound as a zero-sum game:** the designer picks an algorithm $$A \in \mathcal{A}$$, the adversary picks an input $$x \in \mathcal{X}$$, and the payoff (penalty) is the cost $$C(A, x)$$.
2. **View a randomized algorithm as a mixed strategy:** instead of tracking messy internal coin flips, view any randomized algorithm $$R$$ as simply sampling a deterministic algorithm $$A$$ according to a distribution $$R$$.
3. **Flip min and max via von Neumann's theorem:** the best randomized algorithm's worst-case cost is always at least the best **deterministic** algorithm's average cost on *any* input distribution $$\mu$$ you invent.
4. **Crush the lower bound with a single hard distribution:** to prove every randomized algorithm needs at least $$L$$ steps, craft one clever distribution $$\mu$$ and prove every deterministic algorithm averages $$\ge L$$ on $$\mu$$!

**Quick check.** Yao's principle does *not* claim "randomness never helps"—for Equality, randomness slashes communication from $$n$$ bits to $$O(\log n)$$! Rather, Yao gives us the sharpest hammer for proving **unbreakable limits** even for randomized algorithms.

### Why students should care

Whenever someone claims “randomization must help,” Yao’s principle asks: help against *which* cost measure? Against a fixed worst-case input, coins may help. But the principle forces apples-to-apples comparisons and supplies a standard proof pattern for lower bounds in decision trees, communication, and property testing.

---

## 3. Communication complexity

### The model

Two parties, Alice and Bob, hold inputs $$x\in\{0,1\}^n$$ and $$y\in\{0,1\}^n$$ respectively. They wish to compute a function $$f(x,y)$$ (often Boolean) by exchanging messages according to a **protocol**. The **communication complexity** is the number of bits exchanged in the worst case (or expected bits for randomized protocols), minimized over protocols that correctly compute $$f$$ (exactly, or with small error).

No other resource is free magic: local computation can be unbounded in the classical model. The scarce resource is **bits across the cut**.

### Equality and disjointness (literacy examples)

**Equality:** $$f(x,y)=1$$ iff $$x=y$$. Deterministic communication needs $$\Theta(n)$$ bits in the worst case (intuition: the communication transcript partitions the space into combinatorial rectangles; equality forces many leaves). Randomized protocols with small error can do vastly better using fingerprinting: hash to a short random seed and compare hashes—communication $$O(\log n+\log(1/\varepsilon))$$ scale depending on error model details. This is a canonical example where **randomness changes the game**.

**Set disjointness:** interpret $$x,y$$ as characteristic vectors of sets; $$f=1$$ iff the sets are disjoint. Disjointness is a flagship hard function for randomized communication: roughly $$\Omega(n)$$ bits are needed even allowing small error (famous lower bounds in the literature). Hardness of disjointness is a workhorse reduction target for streaming algorithms, data structure lower bounds, and distributed computation.

### Worked Example (Step by Step): $$4\times 4$$ Communication Matrices for Equality and Set Disjointness ($$n = 2$$)

List all $$n = 2$$ bit strings in order: `00, 01, 10, 11`, and build the $$4 \times 4$$ communication matrix $$M_f[x, y] = f(x, y)$$:

1. **Equality ($$\mathrm{EQ}(x,y)=1 \iff x=y$$):**
$$
M_{\mathrm{EQ}} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} = I_4 \implies \operatorname{rank}(M_{\mathrm{EQ}}) = 4.
$$
Every deterministic $$c$$-bit protocol partitions $$M_f$$ into at most $$2^c$$ monochromatic rectangles (each of rank $$\le 1$$), so $$2^c \ge \operatorname{rank}(M_{\mathrm{EQ}}) = 4 \implies c \ge \log_2 4 = 2$$ bits (in general, $$n$$ bits)!
2. **Randomized fingerprinting for Equality:** suppose Alice holds $$x = 100$$ and Bob holds $$y = 105$$ (difference $$\lvert x - y\rvert = 5$$). Alice picks a random prime $$p \in \{2, 3, 5, 7\}$$ and sends $$(p, x \bmod p)$$ to Bob:
   - $$p = 2$$: $$100\bmod 2 = 0 \neq 105\bmod 2 = 1$$ → mismatch detected!
   - $$p = 3$$: $$1 \neq 0$$ → mismatch detected!
   - $$p = 7$$: $$2 \neq 0$$ → mismatch detected!
   - Only $$p = 5$$ collides ($$0 = 0$$). For $$n$$-bit files, picking $$p$$ up to $$O(n^2)$$ costs only $$O(\log n)$$ bits while making collisions vanishingly rare!
3. **Set Disjointness ($$\mathrm{DISJ}(x,y)=1 \iff$$ no coordinate is 1 in both):**
$$
M_{\mathrm{DISJ}} = \begin{pmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix} \implies \det(M_{\mathrm{DISJ}}) = 1 \neq 0 \implies \operatorname{rank}(M_{\mathrm{DISJ}}) = 4.
$$
Remarkably, unlike Equality, even when coin flips are allowed, $$\mathrm{DISJ}$$ stays locked at $$\Theta(n)$$ bits—making it the cornerstone reduction target for proving RAM lower bounds in streaming algorithms!

### Rectangles and lower-bound geometry

A deterministic protocol transcript induces a partition of the input space $$\{0,1\}^n\times\{0,1\}^n$$ into **combinatorial rectangles** $$A\times B$$ (Alice’s inputs consistent with the transcript form $$A$$; Bob’s form $$B$$). Correct protocols cannot mix 0- and 1-inputs of $$f$$ inside one monochromatic rectangle. Counting or measuring rectangles yields lower bounds. Randomized and quantum variants refine the geometry (distributions over rectangles; quantum messages), but the rectangle intuition remains the first picture to own.

---

## 4. From communication to the rest of theory

Communication complexity is not a silo. Circuit depth and formula size relate to multiparty or KW games in certain regimes; streaming lower bounds often reduce to communication; distributed graph algorithms inherit cut constraints. When Chapter 3 discusses [networks]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/), the mathematical cousin is: **bandwidth across a cut is a theorem-shaped bottleneck**, not only an engineering inconvenience.

Yao’s influence includes treating such bottlenecks as first-class mathematical objects with completeness phenomena, reductions, and combinatorial dichotomies.

---

## 5. Cryptography, pseudorandomness, and foundations

Complexity-based cryptography needs one-way functions, pseudorandom generators, and careful notions of computational indistinguishability. Yao’s contributions to this culture include foundational formulations connecting hardness to the inability of efficient adversaries to distinguish pseudorandom strings from uniform—and more broadly the program of basing security on computational assumptions rather than on perfect information-theoretic secrecy alone.

**Literacy caution.** “Cryptography is number theory” is incomplete; modern theory is **hardness + protocol design + reductions**. Number theory supplies candidate hard problems ([crypto lecture]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/)); complexity supplies the language of adversaries, negligible functions, and asymptotic security.

Pseudorandomness also links to derandomization themes you will meet again with [Wigderson]({{ site.baseurl }}/contents/en/chapter09/09_13_Wigderson_Complexity/) and the [Abel portrait]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/): hardness can *create* randomness that fools efficient tests.

---

## 6. Quantum computing: early contributions as awareness

Yao’s name appears in the history of **quantum circuit models** and early complexity framing of quantum computation—work that helped standardize how theorists talk about quantum algorithms as circuits with unitary gates, measurement, and complexity classes. For this course, treat that as **foundations awareness**:

- quantum computation is a precise mathematical model, not magic;  
- complexity classes such as **BQP** live next to classical **BPP** and **P** ([complexity map]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/));  
- quantum *communication* complexity is a natural extension of the classical two-party model.

Do not confuse “Yao worked on quantum foundations” with “Yao invented Shor’s algorithm.” Different contributions, same scientific era of making quantum computing rigorous.

---

## 7. Confusions

| Claim | Correction |
|-------|------------|
| “Yao’s minimax says randomness never helps.” | It relates randomized worst-case cost to distributional deterministic cost; randomness can still change complexity for a fixed input or for Monte Carlo error models. |
| “Communication complexity is about network latency in practice only.” | It is a mathematical model of bit exchange; applications to systems exist, but theorems are combinatorial. |
| “Equality always needs $$n$$ bits.” | Deterministic yes (order $$n$$); randomized fingerprinting can use far fewer bits with error. |
| “Lower bounds mean the problem is unsolvable.” | They bound a *resource* under a *model*; change the model (shared randomness, quantum messages, approximation) and the number may change. |
| “Cryptography is only RSA.” | Complexity-based crypto is a general theory; RSA is one classical candidate family. |
| “Quantum communication complexity is science fiction.” | It is a standard theoretical model with theorems; engineering is separate. |

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/yao-complexity/`.

**From the research pack (must-know slogans)**

- Yao Turing 2000: theory of computation — communication complexity, pseudorandomness, quantum computing foundations culture.
- **Yao's minimax principle** for randomized algorithms / distributional complexity.
- Communication complexity as a resource theory (bits exchanged).

**Recommended order**


**Official / primary written hubs**

- Yao Turing page: https://amturing.acm.org/award_winners/yao_1611524.cfm  
- Wigderson randomness (related resource theory): https://amturing.acm.org/award_winners/wigderson_3844537.cfm  

Complete URL bibliography: `research/video-research/yao-complexity/references.md`.

## References


### Video research pack (all URLs)

Complete list: `research/video-research/yao-complexity/references.md`.

1. Yao Turing page — https://amturing.acm.org/award_winners/yao_1611524.cfm  
2. Wikipedia — Andrew Yao — https://en.wikipedia.org/wiki/Andrew_Yao  
3. Wikipedia — Communication complexity — https://en.wikipedia.org/wiki/Communication_complexity  
4. Wikipedia — Yao's principle — https://en.wikipedia.org/wiki/Yao%27s_principle  
5. Wikipedia — Pseudorandom generator — https://en.wikipedia.org/wiki/Pseudorandom_generator  
6. Yao class / IIIS Tsinghua culture — https://iiis.tsinghua.edu.cn/en/  
7. Wigderson randomness (related resource theory) — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
8. Survey entry: Kushilevitz–Nisan book culture — https://en.wikipedia.org/wiki/Communication_complexity  
9. Research pack folder: `research/video-research/yao-complexity/`.

1. ACM Turing Award page for Andrew C. Yao — [amturing.acm.org](https://amturing.acm.org/).  
2. Kushilevitz–Nisan, *Communication Complexity*; Rao–Yehudayoff modern notes/books on communication complexity.  
3. Yao, classic papers on communication complexity and on minimax / randomized complexity (see Turing bibliography).  
4. Course: [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/); [complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/); [cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/); [quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/).

---

## Further directions

- Work a toy decision-tree lower bound via hard distributions (minimax practice).  
- Read a short survey chapter on disjointness lower bounds and one streaming application.  
- Compare classical vs quantum communication complexity slogans after the quantum lecture.  
- Bridge forward to [Valiant / PAC learning]({{ site.baseurl }}/contents/en/chapter09/09_09_Valiant_Learning/) (different Turing story, same “definitions that created a field” pattern).  
- Next in sequence: Valiant.

## Video tham khảo

- **xem trước** — [Andrew C. Yao - Some Perspectives on Computational and Communication Complexity](https://www.youtube.com/watch?v=g7KzDojwAuM) — IEEE Information Theory Society, English. Watch first. “Andrew C. Yao - Some Perspectives on Computational and Communication Complexity” orients the lesson’s aim: After this lecture you should be able to state Yao’s minimax principle in slogan form and explain why it equates average-case deterministic cost under a hard distribution with wors…
- [【Kyoto Prize Commemorative Lecture】Andrew Chi-Chih Yao “A Journey Through Computer Science”](https://www.youtube.com/watch?v=9BPksehCgOU) — Kyoto Prize, English. A second pass once the main claim is in view: After this lecture you should be able to state Yao’s minimax principle in slogan form and explain why it equates average-case deterministic cost under a hard distribution with wors…
- [Andrew Chi Chih Yao: Building Up Computer Science by Asking Good Questions #ICBS2024](https://www.youtube.com/watch?v=lRwCImYTLkE) — BIMSA, English. Further depth after the first two, still tied to this lesson: After this lecture you should be able to state Yao’s minimax principle in slogan form and explain why it equates average-case deterministic cost under a hard distribution with wors…
