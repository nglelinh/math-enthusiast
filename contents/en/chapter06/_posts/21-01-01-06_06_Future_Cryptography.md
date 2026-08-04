---
layout: post
title: "Cryptography (Frontiers)"
chapter: '06'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter06
---

Cryptography is the mathematics of **adversarial communication**: how to compute and interact so that secrets stay secret, authenticity holds, and protocols remain sound even when some parties cheat. Classical public-key systems that secure much of the internet rest on number-theoretic hardness assumptions—factoring, discrete logarithms—that are **believed** hard for classical computers and **known** to be breakable in polynomial time by a large-scale fault-tolerant quantum computer via Shor’s algorithm. That single sentence is why “future cryptography” is not optional fashion; it is migration engineering guided by theorems, reductions, and careful cryptanalysis.

This lecture separates **symmetric** primitives, **public-key** assumptions, **post-quantum** candidates, **quantum key distribution**, and **advanced protocols** (zero knowledge, FHE, MPC), with relentless attention to what is proved relative to what assumption.

---

## Learning objectives

After this lecture you should be able to:

- Distinguish symmetric encryption (shared key) from public-key encryption and digital signatures at the protocol-role level.
- Explain why RSA/ECC-style schemes are threatened by Shor, while well-designed symmetric schemes mainly face Grover-type quadratic search (key-length adjustments)—without overstating either.
- Name major **post-quantum** families (lattices, codes, hashes, multivariate, isogenies with caution) and what “security reduction” aims to mean.
- Contrast **QKD** (quantum channel + model assumptions) with **PQC** (classical algorithms, quantum-resistant assumptions).
- State, informally, what zero-knowledge proofs and homomorphic encryption enable, and why efficiency and assumptions matter.
- Critique migration hype: “quantum-safe” labels without parameters, proofs, or side-channel stories.

**Prerequisites.** Modular arithmetic comfort; basic probability. Complexity classes at slogan level help; see the complexity lecture for depth.

---

## 1. Goals and threat models

Cryptography specifies **algorithms** plus a **threat model**: what the adversary sees (ciphertext only? chosen plaintexts?), what they can do (online queries? quantum computers?), and what counts as a break (full key recovery vs distinguishing ciphertexts vs forging one signature).

Provable security typically shows reductions: *if* an adversary breaks the scheme, *then* one can break a named hard problem (e.g., LWE) with comparable resources. Reductions can be tight or loose; models can be idealized (random oracles). **Heuristic** security (surviving cryptanalysis) remains essential because assumptions might be false and models might miss side channels.

---

## 2. Symmetric cryptography: still the workhorse

Block ciphers, stream ciphers, hash functions, and MACs protect bulk data once keys exist. AES and SHA-family hashes are not known to collapse under Shor-style quantum attacks the way factoring does. Grover’s algorithm gives a generic quadratic speedup for brute-force key search, which is why longer keys (e.g., AES-256 vs AES-128 in some threat models) appear in quantum-aware recommendations.

**Literacy.** Symmetric crypto does not solve key distribution by itself—that is why public-key and QKD exist. Implementation attacks (timing, power, faults) break systems without breaking the mathematical primitive.

---

## 3. Public-key cryptography and the quantum break

RSA-style encryption and signatures rely on factoring-related assumptions; Diffie–Hellman and elliptic-curve schemes rely on discrete-log-type assumptions in carefully chosen groups. Shor’s algorithm solves factoring and discrete log in polynomial time on a fault-tolerant quantum computer. Hence long-term confidentiality of recorded ciphertexts (“harvest now, decrypt later”) motivates **early** migration for high-value data—even before large quantum machines exist.

This is **algorithmic mathematics meeting engineering timelines**. The theorem is about asymptotic quantum complexity; the risk management is about when cryptographically relevant machines appear and how long secrets must last.

---

## 4. Post-quantum cryptography (PQC)

PQC redesigns classical public-key schemes to resist quantum adversaries. Major families:

| Family | Hardness intuition (informal) | Notes |
|--------|-------------------------------|-------|
| Lattices (e.g., Kyber/ML-KEM, Dilithium/ML-DSA style schemes) | Short vectors / LWE / Module-LWE | NIST selections; strong research base |
| Codes | Decoding random linear codes | Classic McEliece-type ideas; large keys |
| Hash-based signatures | Security of underlying hash | Conservative; stateful vs stateless designs |
| Multivariate | Solving multivariate quadratic systems | Mixed history; careful cryptanalysis |
| Isogenies | Maps between elliptic curves | Some schemes broken (e.g., SIDH); field ongoing |

**NIST standardization** (and national analogs) is a multi-year cryptanalytic and engineering process—not a pure math contest. Parameter choices balance security estimates, key sizes, and performance. “Lattice-based” is not automatically safe: wrong parameters, weak implementations, or future algorithms can still break systems.

Mathematical backbone includes geometry of numbers, algebraic number theory (module lattices), coding theory, and average-case to worst-case reductions for problems like LWE (Regev and followers)—reductions that are jewels of modern theoretical cryptography.

---

## 5. Quantum key distribution vs PQC

**QKD** uses quantum states so that eavesdropping on the quantum channel disturbs statistics, enabling detection under stated physical models. It typically still needs classical authenticated channels and careful engineering against side channels. **PQC** runs on classical networks with new algorithms.

| | PQC | QKD |
|--|-----|-----|
| Channel | Classical | Quantum + classical |
| Core assumption style | Computational hardness | Physical/information-theoretic in a model |
| Deployment | Software/hardware crypto libraries | Specialized optical/quantum infrastructure |
| Complements | Yes—often layered | Yes—not a full replacement for all crypto goals |

They answer related security anxieties with **different** trust anchors. Popular media often conflates them.

---

## 6. Advanced protocols: ZK, FHE, MPC

**Zero-knowledge proofs** let a prover convince a verifier that a statement is true without revealing a witness (beyond what the statement implies). Modern succinct proof systems power blockchains and privacy tools; security rests on cryptographic assumptions and careful circuit/arithmetization design. Soundness errors, trusted setups (in some systems), and bugs in implementations are practical hazards.

**Fully homomorphic encryption (FHE)** allows computation on ciphertexts: $$\mathsf{Dec}(f(\mathsf{Enc}(x))) = f(x)$$ for broad classes of $$f$$. Foundational breakthroughs (Gentry and subsequent generations) use lattice techniques; costs remain high for many applications, though improving.

**Secure multiparty computation (MPC)** lets parties compute a joint function without revealing inputs beyond the output, under honest-majority or dishonest-majority models with different tools (secret sharing, garbled circuits, OT).

These are **mathematical protocol theories** with real deployments—and with a wide gap between asymptotic feasibility and cheap ubiquitous use. Hype (“FHE solves all privacy”) skips performance, leakage via access patterns, and key management.

---

## 7. Migration literacy and open problems

1. Hybrid classical+PQC handshakes during transition.
2. Cryptanalysis of new primitives (classical and quantum algorithms).
3. Side-channel-resistant implementations.
4. Protocol composition: proving security of systems built from parts.
5. Long-term signatures and key agility.
6. Formal verification of crypto code and proofs.
7. Realistic quantum threat assessment without panic or denial.

### Concrete migration picture (conceptual)

A modern TLS-like handshake might negotiate classical elliptic-curve key exchange **and** a lattice KEM, combining shared secrets so that an attacker must break **both** to recover the session key (hybrid mode). Signatures used for software updates may move to hash-based or lattice schemes with different size/performance profiles. Certificates, HSMs, constrained IoT devices, and long-lived document signatures each impose different constraints—there is no single “switch to PQC” button.

**Harvest-now-decrypt-later** risk is asymmetric across data types. A medical or diplomatic ciphertext that must stay confidential for fifty years is urgent; a session key that expires in minutes is less so. Risk management multiplies (value of secret) × (time secret must last) × (probability of cryptographically relevant quantum computers within that horizon)—a Fermi estimate, not a theorem, but better than vibes.

### Side channels and “math vs silicon”

Even perfect reductions fail if implementations leak keys through timing, cache, power, or fault injection. Constant-time coding, masking, and formal verification of crypto code are first-class security work. Post-quantum schemes with large keys and new arithmetic (NTTs for lattices, big matrices for codes) create **new** side-channel surfaces. Frontier literacy includes: a scheme can be “NIST-selected” and still be broken in a product by a bad RNG or a leaky comparison.

---

## Common confusions

| Claim | Verdict | Correction |
|-------|---------|------------|
| “Quantum computers already break RSA in the wild.” | False today | No public cryptographically relevant break of standard RSA-2048 via Shor on real hardware. |
| “AES is broken by Shor.” | Misleading | Grover affects brute force; double key length is the usual discussion, not Shor factoring. |
| “PQC is unproven so useless.” | Too strong | All public-key crypto uses assumptions; PQC assumptions are newer and under intense study. |
| “QKD makes all cryptography obsolete.” | False | Limited deployment scope; authentication and broader goals remain. |
| “Zero knowledge means zero information in every sense.” | Careful | Defined relative to a simulation paradigm; implementations can leak. |
| “NIST standardized ⇒ forever safe.” | Overclaim | Standards reduce risk; cryptanalysis continues. |

---

## Exercises

1. **Roles.** Match: confidentiality of bulk data, key exchange, non-repudiation—to symmetric encryption, KEM/key exchange, signatures.
2. **Harvest now.** Explain in three sentences why long-lived secrets motivate PQC before large quantum computers exist.
3. **Shor vs Grover.** One paragraph each on public-key vs symmetric impact.
4. **Reduction literacy.** What does a reduction from LWE to a scheme’s security claim to show? What does it *not* show?
5. **QKD vs PQC table.** Fill the comparison table from memory, then check Section 5.
6. **ZK idea.** Invent a toy “I know a password hash preimage” story and say what should not leak.
7. **Critique.** Find a vendor “quantum-safe” claim; list missing details (parameters, scheme name, side channels, hybrid mode).

---


---

## Knowledge extracted from video research

Seminar-facing distillation (cross-checked against written sources; **no fabricated transcripts**). Pack: `research/video-research/future-cryptography/analysis.md`.

### Status

**Standards evolving.** NIST released first PQC FIPS (203–205) in 2024; migration is ongoing. QKD is a different technology stack from classical PQC algorithms.

### Core statement / slogan

Shor's algorithm breaks RSA/ECC on a large fault-tolerant quantum computer (theorem in circuit model). PQC bases security on lattice/code/hash/isogeny-type problems believed hard for quantum adversaries — hardness is *conjectural*, not proved.

### Definitions to freeze

- **PQC.** Classical crypto designed to resist quantum adversaries.
- **Crypto-agility.** Ability to swap algorithms as standards/attacks evolve.

### Hygiene (from confusions log)

- Assuming quantum computers already break RSA at scale today.
- Equating QKD with PQC (different trust and deployment models).


---

## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as substitutes for primary proofs or papers when a claim is load-bearing. Full ranking and Mode B notes: `research/video-research/future-cryptography/`.

**Recommended order**

1. **Orientation** — SandboxAQ — NIST's PQC Standardization Explained: [https://www.youtube.com/watch?v=crPe69NeTdk](https://www.youtube.com/watch?v=crPe69NeTdk).  
2. **Core** — IBM Research — NIST post-quantum standards webcast: [https://www.youtube.com/watch?v=YJ00O4gBs0I](https://www.youtube.com/watch?v=YJ00O4gBs0I).  
3. **Foundation** — Cryptography 101 — PQC Standards explained: [https://www.youtube.com/watch?v=P9g1CMCu8DI](https://www.youtube.com/watch?v=P9g1CMCu8DI).  

**Status reminder:** **Standards evolving.** NIST released first PQC FIPS (203–205) in 2024; migration is ongoing. QKD is a different technology stack from classical PQC algorithms.

---


### Transcript & frames (batch extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/future-cryptography/transcripts/` · status: `research/video-research/future-cryptography/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Sample video frame]({{ site.baseurl }}/img/video_research/nonflagships/future-cryptography_crPe69NeTdk_thumb.jpg)

*Figure. Sample still from a pack primary video (see pack for timestamps).*

## References and further reading

1. Katz & Lindell. *Introduction to Modern Cryptography*.
2. NIST PQC project documentation and selected algorithm specs.
3. Regev. On lattices, learning with errors, random linear codes, and cryptography.
4. Shor (1994/1997). Quantum factoring/discrete log algorithms.
5. Surveys on FHE, ZK proof systems, and MPC (Boneh–Shoup chapters; recent SoK papers).
6. Course links: [Quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/), [Complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/), [Mathematics of AI]({{ site.baseurl }}/contents/en/chapter06/06_02_Mathematics_of_AI/) (threat models vs hype patterns).

---


Full URL bibliography from video research: `research/video-research/future-cryptography/references.md`.

### Videos (recommended path)

- SandboxAQ — NIST's PQC Standardization Explained (ORIENTATION): https://www.youtube.com/watch?v=crPe69NeTdk
- IBM Research — NIST post-quantum standards webcast (CORE): https://www.youtube.com/watch?v=YJ00O4gBs0I
- Cryptography 101 — PQC Standards explained (FOUNDATION): https://www.youtube.com/watch?v=P9g1CMCu8DI

### Papers and web (from research pack)

- NIST — What is Post-Quantum Cryptography?: https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography
- NIST PQC project: https://csrc.nist.gov/projects/post-quantum-cryptography
- Wikipedia — NIST PQC Standardization: https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization
- NIST video page — PQC Good/Bad/Powerful: https://www.nist.gov/video/post-quantum-cryptography-good-bad-and-powerful
- Wikipedia — Post-quantum cryptography: https://en.wikipedia.org/wiki/Post-quantum_cryptography
- Wikipedia — Shor's algorithm: https://en.wikipedia.org/wiki/Shor%27s_algorithm

### Course

- Research pack: `research/video-research/future-cryptography/` (especially `references.md`, `learning_path.md`).

## Further directions

- **Quantum threat model in full:** [Quantum information]({{ site.baseurl }}/contents/en/chapter06/06_03_Quantum_Information/).
- **Hardness language:** [Complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/).
- **Practice:** compare public key sizes and operation counts for a classical ECC scheme vs a lattice KEM using published benchmarks (order-of-magnitude only).
- **Reading path:** Katz–Lindell core chapters → NIST PQC FAQ → one LWE survey paragraph a day.
- Maintain a personal threat-model checklist before trusting any “unbreakable” claim.
