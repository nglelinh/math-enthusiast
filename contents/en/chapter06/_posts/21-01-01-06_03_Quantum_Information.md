---
layout: post
title: "Quantum Information"
chapter: '06'
order: 3
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

For seven decades, every photograph you took, every message you sent, and even the largest AI model has been built from a single elementary brick: the **classical bit**—either $$0$$ or $$1$$, like a light switch with two positions. In the 1980s, Richard Feynman asked a disarmingly simple question: if nature at the microscopic scale obeys quantum mechanics rather than classical physics, what happens when we let a quantum system itself carry information?

The answer opened an entire discipline built around the **qubit**: a unit vector in a two-dimensional complex Hilbert space $$\mathbb{C}^2$$ whose complex amplitudes can interfere constructively or cancel each other out like waves on water. Join multiple qubits together, and the state space multiplies via the **tensor product**, unlocking nature’s strangest resource: **entanglement**.

Superposition, entanglement, and measurement are not science-fiction metaphors. They are crisp structures of complex linear algebra and probability, complete with theorems, no-go results, and dramatic algorithmic consequences. This lecture builds **frontier literacy** for quantum information science: what is solid mathematics, what is an ambitious engineering roadmap, and what is hype about “quantum supremacy” or “quantum AI.”

---

## Key ideas: What Is Quantum Information Science and What Does It Study?

Where Shannon’s classical information theory asks how to compress, transmit, and protect strings of $$0/1$$ bits over noisy channels, **Quantum Information Science (QIS)** asks the exact same questions when the information carrier obeys quantum laws. You do not need a prior physics course in quantum mechanics to grasp its mathematical backbone—it stands on **four pillars**:

1. **State Geometry & Unitary Dynamics (Complex Linear Algebra):** One qubit lives in $$\mathbb{C}^2$$; $$n$$ qubits live in the exponentially huge space $$\mathbb{C}^{2^n}$$. Quantum gates are unitary matrices (length-preserving complex rotations).
2. **Quantum Algorithms (Amplitude Interference & Complexity):** Quantum computers do *not* simply “try every answer at once.” Their power comes from choreographing rotations so wrong branches **interfere destructively** (cancelling out like opposite waves) while the right branch **interferes constructively** so measurement hits the answer with high probability.
3. **Quantum Error Correction (Codes in Hilbert Space):** Physical qubits are fragile—stray heat or electromagnetic noise causes *decoherence*. Because the no-cloning theorem forbids copying an unknown qubit like a classical bit, quantum error correction spreads one logical qubit across an entangled state of many physical qubits to detect errors without reading the secret state.
4. **Quantum Communication & Cryptography:** Using entanglement and measurement disturbance to distribute secret keys (QKD) where eavesdropping leaves an unavoidable statistical footprint.

---

## Learning objectives

After this lecture you should be able to:

- Represent a single qubit as a unit vector in $$\mathbb{C}^2$$ (up to phase) and a measurement in an orthonormal basis as a probabilistic collapse rule.
- Explain the **tensor-product** structure of multi-qubit states and why entanglement is not a classical correlation of predetermined bit values.
- State, at slogan-plus-formula level, what **Shor’s** and **Grover’s** algorithms achieve, and what they do *not* claim.
- Describe why **quantum error correction** is necessary and name the obstacle of decoherence without treating NISQ devices as universal solvers.
- Distinguish quantum **key distribution** (information-theoretic / physical security assumptions) from post-quantum **classical** cryptography (hardness assumptions)—see also the cryptography lecture.
- Critique one popular claim using theorem vs experiment vs roadmap language.

**Prerequisites.** Complex numbers, vectors and inner products, basic probability. Linear algebra comfort helps; no prior quantum course is assumed.

---

## 1. States: Hilbert space, not magic

A pure state of a qubit is a unit vector

$$
\lvert\psi\rangle = \alpha\lvert 0\rangle + \beta\lvert 1\rangle,
\qquad
\lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1,
$$

where $$\lvert 0\rangle, \lvert 1\rangle$$ form an orthonormal basis of $$\mathbb{C}^2$$. Global phase $$e^{i\phi}\lvert\psi\rangle$$ represents the same physical pure state. Mixed states—relevant under noise—are **density operators**: positive semidefinite Hermitian matrices of trace one.

Measurement in the computational basis yields $$0$$ or $$1$$ with probabilities $$\lvert\alpha\rvert^2$$ and $$\lvert\beta\rvert^2$$, and the post-measurement state is the corresponding basis vector (idealized projective measurement). Different bases give different statistics. This is **Born’s rule** packaged for computation: amplitudes are complex; probabilities are moduli squared.

**Unitary evolution.** Closed-system dynamics between measurements are unitary maps $$U$$ with $$U^\dagger U = I$$. Quantum gates are unitary matrices (or approximate implementations thereof). Composition of gates is matrix multiplication; parallelism of wires is tensor product.

---

### Short video: The CHSH game and the limit 2

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/chsh-bell-game_en.mp4"></video>
</div>

Any fixed classical strategy gives $$|S| = 2$$, so no mixture of strategies exceeds 2. For an entangled pair measured at 0°, 90°, 45° and −45°, quantum theory predicts $$S = 2\sqrt{2} \approx 2.83$$, and Bell experiments observe violations of the bound 2.


### Try it yourself: Play with the CHSH angles

<div class="mex-explainer" data-mex="chsh" data-lang="en"></div>


## 2. Many qubits: tensor products and entanglement

Two qubits live in $$\mathbb{C}^2\otimes\mathbb{C}^2 \cong \mathbb{C}^4$$. A product state factors as $$\lvert\psi\rangle\otimes\lvert\phi\rangle$$. States that cannot be written as a single product (or convex combinations of products, in the mixed case) are **entangled**. The Bell state

$$
\lvert\Phi^+\rangle = \frac{1}{\sqrt{2}}\bigl(\lvert 00\rangle + \lvert 11\rangle\bigr)
$$

is the canonical example: measurement outcomes on the two parties are perfectly correlated in ways that cannot be simulated by shared classical randomness alone under locality constraints (Bell’s theorem and experimental violations of Bell inequalities).

**Literacy point.** Entanglement is a precise resource theory in quantum information (measures, conversion rates, monogamy). It is not a synonym for “spooky unlimited bandwidth.” No-communication theorems prevent using entanglement alone to send messages faster than light; classical communication is still needed for teleportation protocols.

---

### Explanation: Building a Bell State and Breaking the CHSH Limit by Hand

To see that “quantum entanglement” is concrete $$4\times 4$$ linear algebra rather than mysticism, let us turn two unentangled qubits $$\lvert 00\rangle$$ into the Bell state $$\lvert \Phi^+\rangle$$ by hand, then verify directly how it beats the classical CHSH bound of $$2$$.

1. **Build the Bell state with matrices:** In the basis $$\{\lvert 00\rangle, \lvert 01\rangle, \lvert 10\rangle, \lvert 11\rangle\}$$, start at $$\lvert 00\rangle = (1, 0, 0, 0)^\top$$.
   - **Step 1 — Apply Hadamard to qubit 1 ($$H \otimes I$$):** maps $$\lvert 0\rangle \mapsto \frac{\lvert 0\rangle + \lvert 1\rangle}{\sqrt{2}}$$ while leaving qubit 2 untouched:
     $$\lvert \psi_1\rangle = \frac{1}{\sqrt{2}}(\lvert 00\rangle + \lvert 10\rangle) = \frac{1}{\sqrt{2}}(1, 0, 1, 0)^\top.$$
     So far the two qubits are still a product state (unentangled).
   - **Step 2 — Apply CNOT (flip qubit 2 whenever qubit 1 is 1):** swaps $$\lvert 10\rangle \leftrightarrow \lvert 11\rangle$$ and leaves $$\lvert 00\rangle$$ fixed:
     $$\mathrm{CNOT}\,\lvert \psi_1\rangle = \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1\\0\\1\\0\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\0\\0\\1\end{pmatrix} = \frac{\lvert 00\rangle + \lvert 11\rangle}{\sqrt{2}} = \lvert \Phi^+\rangle.$$

2. **Verify the CHSH violation $$2\sqrt{2} > 2$$ by hand:**
   - **Classical ceiling:** Suppose Alice pre-commits to $$a_0, a_1 \in \{-1, +1\}$$ and Bob to $$b_0, b_1 \in \{-1, +1\}$$. Factor the CHSH score:
     $$S = a_0 b_0 + a_0 b_1 + a_1 b_0 - a_1 b_1 = a_0(b_0 + b_1) + a_1(b_0 - b_1).$$
     Since $$b_0, b_1 \in \{\pm 1\}$$, one of $$(b_0 + b_1)$$ or $$(b_0 - b_1)$$ must be $$0$$ and the other must be $$\pm 2$$. Hence every classical strategy (and any probabilistic mixture of them) obeys $$\lvert S \rvert \le 2$$.
   - **Quantum strategy on $$\lvert \Phi^+\rangle$$:** Measuring Alice’s qubit at Bloch angle $$\alpha$$ and Bob’s at $$\beta$$ gives correlation $$E(\alpha, \beta) = \cos(\alpha - \beta)$$. Plug in the exact four angles from the video above—$$\alpha_0 = 0^\circ,\ \alpha_1 = 90^\circ,\ \beta_0 = 45^\circ,\ \beta_1 = -45^\circ$$:
     - $$E(0^\circ, 45^\circ) = \cos(-45^\circ) = \frac{\sqrt{2}}{2}$$,
     - $$E(0^\circ, -45^\circ) = \cos(45^\circ) = \frac{\sqrt{2}}{2}$$,
     - $$E(90^\circ, 45^\circ) = \cos(45^\circ) = \frac{\sqrt{2}}{2}$$,
     - $$E(90^\circ, -45^\circ) = \cos(135^\circ) = -\frac{\sqrt{2}}{2}$$.
     Sum them into the CHSH expression:
     $$S = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} - \Bigl(-\frac{\sqrt{2}}{2}\Bigr) = 2\sqrt{2} \approx 2.828 > 2.$$

In four lines of trigonometry, you have verified by hand why quantum correlations cannot be reproduced by any classical local hidden-variable model.

## 3. Computation model: circuits, oracles, and complexity

A standard model is the **quantum circuit**: a sequence of unitary gates drawn from a universal gate set, applied to qubits initialized in $$\lvert 0\rangle^{\otimes n}$$, followed by measurement. Complexity theory compares quantum and classical resource classes (e.g., **BQP** versus **BPP**/**P**). Relative to certain oracles, separations are known; absolute separations face the same deep obstacles as classical complexity (we do not know $$\mathbf{P}\neq\mathbf{NP}$$, and we do not have a full map of quantum class inclusions).

**Shor’s algorithm** (1994) factors integers and computes discrete logarithms in polynomial time on an idealized fault-tolerant quantum computer, using period finding via the quantum Fourier transform. Cryptographic consequence: widely deployed public-key schemes based on factoring or discrete log (RSA, finite-field Diffie–Hellman, elliptic-curve variants in common use) are broken *in that model*. That is a theorem about asymptotic quantum complexity, not a claim that a cryptographically relevant machine exists today.

**Grover’s algorithm** searches an unstructured database of size $$N$$ in $$O(\sqrt{N})$$ queries, with matching lower bounds in the black-box model. Quadratic speedup is real and important; it is **not** exponential for generic search, and it does not magically solve NP-complete problems in polynomial time on known algorithms.

**Hamiltonian simulation and quantum linear algebra.** Many proposed applications reduce to simulating quantum dynamics or estimating properties of operators. Algorithms exist with rigorous resource estimates under idealized models; constant factors, error rates, and data-loading costs dominate practical discussion.

---

## 4. Noise, NISQ, and error correction

Physical qubits couple to environments. **Decoherence** turns pure superpositions toward classical mixtures; gate and readout errors accumulate. Near-term devices are often called **NISQ** (noisy intermediate-scale quantum): tens to hundreds of imperfect qubits without full fault tolerance.

**Quantum error-correcting codes** encode logical information into entangled states of many physical qubits so that local errors can be detected and corrected without destroying the logical state (e.g., surface codes and other stabilizer codes, with roots in the theory of Pauli groups and symplectic geometry over finite fields). The **threshold theorem** says that if physical error rates are below a threshold and errors are sufficiently well-modeled, fault-tolerant computation is possible with polylog overhead—an existence result with demanding engineering hypotheses.

**Hype check.** Variational algorithms on NISQ hardware are experimental research, not a proof that chemistry or optimization is “solved.” Benchmark claims of quantum advantage must specify the task, the classical baseline, error bars, and whether the task is useful or contrived.

---

## 5. Communication and cryptography (quantum side)

**Quantum key distribution (QKD)** protocols (BB84 and descendants) use quantum states so that eavesdropping introduces detectable disturbance under stated physical and implementation assumptions. Security proofs are information-theoretic *relative to a model*; side channels and device imperfections are engineering and formal-methods problems.

**Quantum teleportation** transfers an unknown state using entanglement and classical communication—not physical transport of a particle, and not faster-than-light signaling.

Do not confuse QKD with **post-quantum cryptography**, which redesigns *classical* public-key schemes to resist quantum adversaries (lattices, codes, hashes, isogenies with care after attacks). Both are “future security” topics; their threat models and trust assumptions differ. Cross-link: [Cryptography frontiers]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/).

---

## 6. Mathematical toolkit (what to study next)

| Tool | Role |
|------|------|
| Hilbert spaces, tensor products | State spaces of composite systems |
| Unitary groups, Lie algebras | Continuous families of gates; control |
| Operator algebras / C*-ideas | Infinite systems, algebraic QFT interfaces |
| Representation theory | Symmetries; some algorithm analyses |
| Stabilizer formalism, symplectic forms over $$\mathbb{F}_2$$ | Efficient classical simulation of Clifford circuits; code design |
| Tensor networks | Condensed-matter states; contraction complexity |
| Concentration and random matrix theory | Typical noise, random circuits, complexity conjectures |

Quantum information is as much **mathematics and theoretical CS** as experimental physics. Linear algebra fluency is the on-ramp; complexity and coding theory deepen the computer-science side.

---

## 7. What is theorem, experiment, or roadmap

| Claim type | Example | Status |
|------------|---------|--------|
| Theorem (idealized model) | Shor factors in poly time on fault-tolerant QC | Mathematical algorithm + complexity analysis |
| No-go / structural theorem | No-cloning; Bell nonlocality under assumptions | Proven under stated axioms |
| Experiment | Bell tests; small-scale algorithms; error rates | Empirical, device-specific |
| Engineering roadmap | Large-scale fault-tolerant machines | Plausible R&D, not guaranteed timeline |
| Hype | “Quantum will replace all classical computing next year” | Ignore; wrong complexity and cost model |

Frontier literacy means refusing to collapse these rows.

### A minimal end-to-end story: Deutsch’s problem (intuition)

Deutsch’s (and Deutsch–Jozsa) problem is a teaching classic: determine whether a Boolean function is constant or balanced with fewer queries than the worst-case classical requirement, using superposition and interference. The point is not that the problem is industrially important; it is that **quantum algorithms rearrange information with interference**, then extract a global property with few measurements. Shor’s period finding is a far more powerful instance of “extract global algebraic structure via Fourier analysis over abelian groups.” Grover is a different design pattern: amplitude amplification boosts the marked state’s probability gradually. Recognizing these **patterns** matters more than memorizing circuit diagrams on first pass.

### Complexity postcard (quantum)

- **BQP**: efficient quantum computers with bounded error.  
- Factoring ∈ **BQP**; relation of **BQP** to **NP** is not settled, but NP-complete problems are not known to lie in **BQP**.  
- Oracle separations show worlds where quantum query complexity beats classical; they are evidence and intuition pumps, not absolute proofs about the physical Church–Turing thesis.  
- Simulation of general quantum circuits by classical computers is believed hard, which underpins both crypto interest and complexity conjectures—but “believed hard” is not a theorem.

---

## Common confusions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Superposition means the computer tries all answers at once.” | Misleading | Amplitudes interfere; you do not get free exponential classical parallelism with free readout of all branches. |
| “Entanglement enables FTL messaging.” | False | No-communication theorems; classical channels still needed for teleportation. |
| “Grover solves NP-complete problems efficiently.” | False as known | Quadratic black-box speedup ≠ poly-time NP solver. |
| “Shor already broke RSA on the internet.” | False today | Cryptographically relevant factoring requires large fault-tolerant machines not currently available. |
| “NISQ variational methods are proved optimal for chemistry.” | Overclaim | Active empirical research; classical algorithms compete fiercely. |
| “Quantum AI will automatically yield AGI.” | Hype | No such theorem; quantum ML is a research niche with unproven broad advantage. |

---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/quantum-information/analysis.md`.

### Status

**Mature mathematical framework** (states, channels, entanglement) with **engineering frontiers** (fault tolerance, NISQ algorithms). Shor/Grover are theorems in the circuit model; physical scalability is experimental.

### Core statement / slogan

Qubit state $$|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$$ in $$\mathbb{C}^2$$; multipartite systems use tensor products. Unitary evolution + measurement projectors. No-cloning is a theorem; Bell nonlocality is experimentally confirmed.

### Definitions to freeze

- **Qubit.** Unit vector in $$\mathbb{C}^2$$ up to global phase; density matrices for mixed states.
- **Entanglement.** Non-product multipartite state; cannot write as $$|\psi\rangle\otimes|\phi\rangle$$.

### Hygiene (from confusions log)

- Thinking measurement 'computes all answers at once' without readout/post-processing structure.
- Conflating QKD with post-quantum classical crypto.


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/quantum-information/`.

**Recommended order**

1. **Core** — Michael Nielsen — Quantum computing for the determined (playlist): [https://www.youtube.com/playlist?list=PL1826E60FD05B44E4](https://www.youtube.com/playlist?list=PL1826E60FD05B44E4).  
2. **Orientation** — Veritasium — How does a quantum computer work?: [https://www.youtube.com/watch?v=g_IaVepNDT4](https://www.youtube.com/watch?v=g_IaVepNDT4).  
3. **Orientation** — Veritasium — How to make a quantum bit: [https://www.youtube.com/watch?v=zNzzGgr2mhk](https://www.youtube.com/watch?v=zNzzGgr2mhk).  
4. **Foundation** — Ronald de Wolf — Intro to Quantum Computing (lecture 1): [https://www.youtube.com/watch?v=MvSYyxZcAr8](https://www.youtube.com/watch?v=MvSYyxZcAr8).  

**Status reminder:** **Mature mathematical framework** (states, channels, entanglement) with **engineering frontiers** (fault tolerance, NISQ algorithms). Shor/Grover are theorems in the circuit model; physical scalability is experimental.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/quantum-information/transcripts/` · status: `research/video-research/quantum-information/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/quantum-information_g_IaVepNDT4_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References and further reading

1. M. A. Nielsen and I. L. Chuang. *Quantum Computation and Quantum Information* — standard textbook.
2. J. Preskill. Lecture notes on quantum computation; essays on NISQ.
3. P. W. Shor (1994/1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer.
4. L. K. Grover (1996). A fast quantum mechanical algorithm for database search.
5. Surveys on quantum error correction and surface codes (Gottesman; Fowler et al. and later reviews).
6. Course links: [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/), [Complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/), [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/) (for contrast on classical ML hype patterns).

---


Full URL bibliography from video research: `research/video-research/quantum-information/references.md`.

### Videos (recommended path)

- Michael Nielsen — Quantum computing for the determined (playlist) (CORE): https://www.youtube.com/playlist?list=PL1826E60FD05B44E4
- Veritasium — How does a quantum computer work? (ORIENTATION): https://www.youtube.com/watch?v=g_IaVepNDT4
- Veritasium — How to make a quantum bit (ORIENTATION): https://www.youtube.com/watch?v=zNzzGgr2mhk
- Ronald de Wolf — Intro to Quantum Computing (lecture 1) (FOUNDATION): https://www.youtube.com/watch?v=MvSYyxZcAr8

### Papers and web (from research pack)

- Nielsen & Chuang — Quantum Computation and Quantum Information: https://en.wikipedia.org/wiki/Quantum_Computation_and_Quantum_Information
- Wikipedia — Quantum information: https://en.wikipedia.org/wiki/Quantum_information
- Wikipedia — Shor's algorithm: https://en.wikipedia.org/wiki/Shor%27s_algorithm
- OSU QIS prep resources (video list): https://u.osu.edu/quantinfo/research/researchprep/
- Wikipedia — Qubit: https://en.wikipedia.org/wiki/Qubit

### Course

- Research pack: `research/video-research/quantum-information/` (especially `references.md`, `learning_path.md`).

## Further directions

- **Security double feature:** this page + [Cryptography frontiers]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/) — quantum algorithms as threat model; PQC and QKD as responses.
- **Complexity:** [Complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/) for BQP in the wider map of hardness.
- **Practice:** simulate a two-qubit Bell circuit in a small notebook (statevector simulator); measure correlations.
- **Reading plan:** Nielsen–Chuang chapters on states/measurement, then Shor at high level, then one modern survey on error correction.
- Keep a personal glossary: *state, unitary, entanglement, mixed state, fault tolerance, oracle separation*.

## Video tham khảo

- **xem trước** — [How Does a Quantum Computer Work?](https://www.youtube.com/watch?v=g_IaVepNDT4) — Veritasium, English. Watch first. “How Does a Quantum Computer Work?” orients the lesson’s aim: Represent a single qubit as a unit vector in \mathbb{C}^2 (up to phase) and a measurement in an orthonormal basis as a probabilistic collapse rule.
- [How To Make a Quantum Bit](https://www.youtube.com/watch?v=zNzzGgr2mhk) — Veritasium, English. A second pass once the main claim is in view: Represent a single qubit as a unit vector in \mathbb{C}^2 (up to phase) and a measurement in an orthonormal basis as a probabilistic collapse rule.
