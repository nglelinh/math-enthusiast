---
layout: post
title: "Modern Applications: Fields Ideas in Computer Science"
chapter: '02'
order: 33
owner: Nguyen Le Linh
lang: en
categories:
- chapter02
lesson_type: optional
---

After touring more than thirty Fields Medal portraits—from exotic four-manifolds and Monge–Ampère regularity to 8-dimensional sphere packings and sharp phase transitions—a natural question surfaces: *where do these deep mathematical ideas go when they leave pure mathematics?* Interestingly, when they land in computer science and industry in 2022–2026, what gets shipped is almost never a biography or a verbatim abstract theorem. It is a **computational cousin**: a neural network that approximates an optimal transport plan for unpaired image translation, a high-dimensional lattice problem that shields Internet traffic from future quantum computers, or a habit of hunting for sharp phase transitions when designing SAT solvers and modern graph transformers.

This optional note bridges those three live engineering landings while keeping attribution crystal clear: **the Fields Medal work made the mathematical objects sharp; the computer-science systems make them cheap enough to run at scale.**

**Lesson roadmap:** Background Knowledge Map (how pure mathematical objects turn into computational problems) → Hand-verifiable worked examples (a toy Module-LWE sample mod $$17$$ and the random $$3$$-SAT phase transition near $$\alpha_c \approx 4.26$$) → Deep-Dive Explanation (Read Slowly): three 2022–2026 CS deployments (Neural OT, NIST FIPS 203 ML-KEM, SAT & GraphGPS) → Boundaries between theorems and engineering approximations.

---

## Learning objectives

After this optional note you should be able to:

- Point to three 2022–2026 computer-science deployments that reuse mathematical objects featured in Chapter 2: **Neural Optimal Transport (NOT)**, **module-lattice post-quantum cryptography (ML-KEM / FIPS 203)**, and **phase-transition thinking in SAT solvers and graph transformers (GraphGPS)**.
- Work out a toy **Module-LWE** sample modulo $$17$$ by hand to see why a tiny noise vector defeats Gaussian elimination and ties security to lattice geometry.
- Separate strict mathematical theorems ([Figalli]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/), Duminil-Copin, Smirnov) from neural approximations, cryptographic hardness assumptions, and heuristic architectures.
- Keep the scope clean: this page is neither a Fields biography nor a repetition of the Tao six-pillar hub in Chapter 4.

**Prerequisites.** Skim the thematic map in the [overview]({{ site.baseurl }}/contents/en/chapter02/02_00_Overview/). You do **not** need the individual medal essays to use this page. Do not read this as a substitute for [Figalli / optimal transport]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska / packing]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/), or the statistical-physics portraits.

---

## Background Knowledge Map: How Three Pure Mathematical Objects Become Computational Systems

### 1. Optimal transport in deep learning
In pure analysis (Figalli, Brenier, Caffarelli), one seeks a coupling $$\pi$$ minimizing $$\int c(x,y)\,d\pi$$ between two densities $$\mu, \nu$$ and asks when the optimizer is a smooth map $$T = \nabla\phi$$. In **machine learning**, we only have two unpaired datasets in tens of thousands of dimensions (say, photographs of faces and oil paintings). Instead of solving the Monge–Ampère PDE directly, practitioners train **neural networks** to parameterize the transport map or plan.

### 2. High-dimensional lattices in post-quantum cryptography
In pure mathematics (Viazovska), modular forms prove that $$E_8$$ and the Leech lattice give the densest sphere packings in dimensions 8 and 24. In **cryptography**, one does not use $$E_8$$ directly, but random **module lattices** in hundreds of dimensions via **Module-LWE** (*Learning With Errors*): recover a secret vector $$s$$ from noisy linear samples

$$
(A,\, As + e \bmod q).
$$

Packing-type geometry governs how large the error $$e$$ (the decoding sphere radius around each lattice point) can sit before unique decryption fails, while an adversary—even with a quantum computer—faces a high-dimensional shortest-vector / closest-vector barrier.

### 3. Phase-transition thinking in SAT solvers and graph learning
Just as percolation has a sharp critical threshold $$p_c$$ (Smirnov, Duminil-Copin), random $$k$$-SAT exhibits a razor-sharp threshold in the clause-to-variable ratio $$\alpha = m/n$$ where solver runtime explodes. Meanwhile, graph neural networks and graph transformers inherit the statistical-physics instinct of balancing **local neighborhood propagation** against **global long-range modes**.

---

## 1. Worked Examples by Hand: A Toy LWE Sample Mod $$17$$ and the $$3$$-SAT Phase Wall

### Example 1: Hand-checking a Module-LWE sample with $$q = 17$$
Set the modulus $$q = 17$$, with public matrix $$A$$ and secret vector $$s$$:

$$
A = \begin{pmatrix} 3 & 5 \\ 7 & 2 \end{pmatrix}, \qquad s = \begin{pmatrix} 4 \\ 1 \end{pmatrix}.
$$

- **WITHOUT noise $$e$$:** compute $$As \bmod 17 = \begin{pmatrix} 3\cdot 4 + 5\cdot 1 \\ 7\cdot 4 + 2\cdot 1 \end{pmatrix} = \begin{pmatrix} 17 \\ 30 \end{pmatrix} \equiv \begin{pmatrix} 0 \\ 13 \end{pmatrix} \pmod{17}$$. An attacker solves the linear system $$As \equiv b \pmod{17}$$ by Gaussian elimination in milliseconds and recovers $$s$$ completely!
- **WITH a tiny noise vector $$e = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$$:** we publish
  $$
  b = As + e \equiv \begin{pmatrix} 0 + 1 \\ 13 - 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 12 \end{pmatrix} \pmod{17}.
  $$
  Even with tiny noise $$\vert e_i \vert \le 1$$, Gaussian elimination **collapses completely** because row operations multiply and scramble the unknown errors! At real cryptographic scales (ML-KEM dimensions $$512, 768, 1024$$), recovering $$s$$ from $$(A, b)$$ reduces to finding a near-closest lattice point in hundreds of dimensions—a problem with no known polynomial-time classical *or* quantum algorithm.

### Example 2: The sharp phase transition in random $$3$$-SAT
Generate $$m$$ random clauses of the form $$(x_i \lor \neg x_j \lor x_k)$$ over $$n = 1000$$ Boolean variables, and dial the clause density $$\alpha = m/n$$:
- At $$\alpha = 2.0$$ ($$2000$$ clauses): almost surely **satisfiable**; modern solvers find a solution in milliseconds.
- At $$\alpha = 6.0$$ ($$6000$$ clauses): massively over-constrained; almost surely **unsatisfiable**.
- Right at the **critical threshold $$\alpha_c \approx 4.26$$** ($$4260$$ clauses): the satisfiability probability drops off a cliff from $$1$$ to $$0$$, and the solution space shatters into disconnected clusters—producing the hardest benchmark instances for SAT solvers!

---

## 2. Deep-Dive Explanation: Three 2022–2026 Computer-Science Landings (Read Slowly)

Examine three concrete 2022–2026 systems to see both the mathematical lineage and the attribution boundary:

#### Step 1: Neural Optimal Transport (Korotin, Selikhanovych, and Burnaev, ICLR 2023)
**Korotin, Selikhanovych, and Burnaev (2023)** train neural networks via a Kantorovich minimax objective to represent both strong and weak optimal-transport plans, proving a universal-approximation theorem for transport plans and demonstrating unpaired image-to-image translation.
- *Clean attribution:* The object is the same Kantorovich plan analyzed via PDEs in [Figalli’s portrait]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/). The ICLR 2023 paper proves no new regularity theorems for Monge–Ampère on $$\mathbb{R}^n$$; it shows that a differentiable model can stand in for a transport plan at real image scale.

#### Step 2: Module lattices as post-quantum key encapsulation (NIST FIPS 203 — ML-KEM, August 2024)
In August 2024, **NIST** standardized **FIPS 203 (ML-KEM)**—derived from CRYSTALS-Kyber—with parameter sets **ML-KEM-512 / 768 / 1024** to replace RSA and ECC against quantum adversaries.
- *Clean attribution:* Security rests on the presumed hardness of **Module-LWE**, not on solving sphere packing in dimensions 8 or 24 ([Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/)). The bridge is the shared geometric language: high-dimensional lattices, shortest-vector hardness, and packing-type decoding radii.

#### Step 3: Phase-transition thinking in SAT and GraphGPS (Rampášek et al., NeurIPS 2022)
Modern SAT competitions still live on crafted and industrial formulas hovering near critical phase walls. In graph representation learning, **GraphGPS** (**Rampášek, Galkin, Dwivedi, Luu, Wolf, and Beaini, 2022**) pairs local message passing (MPNN) with global linear-time attention of complexity $$O(N+E)$$, resolving long-range information bottlenecks.
- *Clean attribution:* This is not a Duminil-Copin or Smirnov biography or a continuum phase-transition proof—it is the statistical-physics *habit* of balancing local neighborhoods against global modes and checking for critical thresholds before trusting a solver or GNN.

Summary of the Chapter 2 to 2022–2026 engineering bridge:

$$
\text{Fields theorems (OT / Lattices / Phase transitions)}
\;\xrightarrow{\text{Computational reuse}}\;
\text{2022–2026 systems (Neural OT / ML-KEM / SAT \& GraphGPS)}.
$$

---

## 3. Interpretation, Insight, and Scope

A transport network that “works” on CelebA is not a theorem about Monge–Ampère regularity. A key-encapsulation mechanism that survives a NIST standardization process is not a sphere-packing theorem. A graph transformer that scores well on ZINC is not a proof of a continuum phase transition. The Fields objects remain the clean, rigorous statements; the CS systems are calibrated approximations built to run in the real world.

This note deliberately skips Hong Wang / Kakeya and Yu Deng portraits, does not retell Green–Tao compressed sensing (those pages already exist elsewhere in the course), and does not survey the 2026 medal citations.

---

## References

- Korotin, A., Selikhanovych, D., & Burnaev, E. (2023). Neural optimal transport. *ICLR*. [arXiv:2201.12220](https://arxiv.org/abs/2201.12220).
- NIST. (2024). *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*. [doi:10.6028/NIST.FIPS.203](https://doi.org/10.6028/NIST.FIPS.203).
- Rampášek, L., Galkin, M., Dwivedi, V. P., Luu, A. T., Wolf, G., & Beaini, D. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Course portraits (do not duplicate here): [Figalli]({{ site.baseurl }}/contents/en/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska]({{ site.baseurl }}/contents/en/chapter02/02_08_Viazovska_Sphere_Packing/).

## Video tham khảo

- **xem trước** — [Alessio Figalli (2018 Fields Medal) explains Optimal Transport](https://www.youtube.com/watch?v=jyL6ZECM7oM) — Tom Rocks Maths, English. Watch first. “Alessio Figalli (2018 Fields Medal) explains Optimal Transport” orients the lesson’s aim: After this optional note you should be able to point to three 2022–2026 computer-science deployments that reuse mathematical objects featured in this chapter—optimal transport, hig…
- [Post Quantum Cryptography - Computerphile](https://www.youtube.com/watch?v=_MoRcYLN-7U) — Computerphile, English. A second pass once the main claim is in view: After this optional note you should be able to point to three 2022–2026 computer-science deployments that reuse mathematical objects featured in this chapter—optimal transport, hig…
- [Fields Medal: Hugo Duminil-Copin](https://www.youtube.com/watch?v=5dXulZVstbY) — Simons Foundation, English. Further depth after the first two, still tied to this lesson: After this optional note you should be able to point to three 2022–2026 computer-science deployments that reuse mathematical objects featured in this chapter—optimal transport, hig…
