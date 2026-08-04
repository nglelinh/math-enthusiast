---
layout: post
title: "Public-Key Cryptography: Diffie, Hellman, and RSA (Turing 2015 / 2002)"
chapter: '09'
order: 6
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

Until the mid-1970s, practical cryptography was largely **symmetric**: Alice and Bob needed a shared secret *before* they could talk privately. **Whitfield Diffie** and **Martin Hellman** (with contributions in the same intellectual neighborhood by Ralph Merkle) articulated **public-key cryptography** and proposed **Diffie–Hellman key exchange**, allowing two parties to agree on a shared secret over a public channel under hardness assumptions. Soon after, **Ron Rivest, Adi Shamir, and Leonard Adleman** published **RSA**, a public-key encryption and signature scheme whose trapdoor is tied to the difficulty of factoring large integers.

Rivest, Shamir, and Adleman received the **ACM A.M. Turing Award in 2002**. Diffie and Hellman received the **Turing Award in 2015**. Official citations and biographies: [amturing.acm.org](https://amturing.acm.org/).

This lecture is a **mathematics-first** tour of the mechanisms at slogan level—modular arithmetic, discrete logarithms, factoring trapdoors—not a cookbook for attacking systems, not legal advice, and not a guide to criminal misuse. Security is computational hardness plus careful engineering; we teach the ideas that make the hardness plausible.

---

## Learning objectives

After this lecture you should be able to:

- Explain the **public-key idea**: separate capabilities to encrypt/verify from decrypt/sign via key pairs.
- Describe **Diffie–Hellman** as agreement on $$g^{ab}$$ from public $$g^a$$ and $$g^b$$.
- State the **discrete logarithm** problem as the hardness intuition behind many DH-style systems.
- Outline **RSA** at the level of $$n=pq$$, exponents $$e,d$$, and modular exponentiation.
- Connect these schemes to [number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/).
- Apply **LO6 / post-quantum caution**: classical public-key assumptions are threatened by large-scale quantum algorithms; migration is an active standardization story.
- Keep ethical framing: educational mechanisms, not operational attack instructions for harm.

**Prerequisites.** Congruences $$a \equiv b \pmod n$$; exponents; primes. Chapter 03’s crypto lecture is ideal preparation.

**Seminar links.** LO4, LO6; [Number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/); [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/); [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/); [Goldwasser–Micali foundations]({{ site.baseurl }}/contents/en/chapter09/09_07_Goldwasser_Micali/).

---

## 1. The problem public keys solve

**Symmetric cryptography** (AES and friends) is excellent for bulk data once a key is shared. The bootstrap problem remains: how do strangers agree on a key when eavesdroppers hear everything?

**Public-key cryptography** equips each party with a **public key** (publishable) and a **private key** (secret). Roughly:

- Anyone can **encrypt** to you with your public key; only your private key **decrypts**.  
- Only your private key can **sign**; anyone can **verify** with your public key.

The mathematical engine is a **trapdoor one-way function**: easy to compute, hard to invert without secret structure, easy to invert with the trapdoor. Diffie–Hellman emphasizes **key agreement**; RSA emphasizes **encryption and signatures** via factoring structure. Real internet protocols often use public-key operations to establish symmetric session keys (**hybrid encryption**)—the best of both worlds.

**Kerckhoffs’s principle.** Algorithms are public; secrecy lives in keys. Textbook schemes here are conceptual; deployment needs padding standards, randomness, certificates, and side-channel resistance far beyond this essay.

---

## 2. Modular exponentiation: the workhorse

Fix a prime modulus $$p$$ (or a composite modulus $$n$$ in RSA). Computing

$$
a^e \bmod m
$$

is feasible for huge $$e$$ via **repeated squaring** in $$O(\log e)$$ modular multiplications. Inverting the map—extracting eth roots, or discrete logs—appears hard in carefully chosen groups. That asymmetry is the ore of classical public-key cryptography.

Number-theoretic lemmas (Fermat/Euler) explain correctness of RSA-style cancellation; they do not by themselves prove security. Security is a computational claim about what efficient adversaries can do.

---

## 3. Diffie–Hellman key exchange

**Public parameters.** A large prime $$p$$ and a generator $$g$$ of a large subgroup of $$\mathbb{Z}/p\mathbb{Z}^\times$$ (modern deployments often use elliptic-curve groups instead of plain multiplicative groups; the slogan is the same).

**Protocol sketch.**

1. Alice picks secret $$a$$, sends $$A = g^a \bmod p$$.  
2. Bob picks secret $$b$$, sends $$B = g^b \bmod p$$.  
3. Alice computes $$B^a = g^{ba}$$; Bob computes $$A^b = g^{ab}$$. They share $$g^{ab} \bmod p$$.

An eavesdropper sees $$g, p, g^a, g^b$$ and wants $$g^{ab}$$. The naive path is to compute $$a$$ from $$g^a$$—the **discrete logarithm problem (DLP)**:

$$
\text{given } g, g^a, \text{ find } a.
$$

If DLP is hard in the chosen group, recovering the secrets from the transcripts should be hard. (Formal security reductions and the **computational / decisional Diffie–Hellman** problems refine this slogan; see crypto textbooks.)

**Why it felt revolutionary.** No prior shared secret is required—only authentic public parameters and, in practice, authentication to defeat man-in-the-middle attacks. The 2015 Turing Award citation emphasizes the invention of public-key cryptography and the DH key exchange paradigm.

---

## 4. RSA: factoring as a trapdoor

**Key generation (conceptual).**

1. Choose large primes $$p,q$$; set $$n = pq$$.  
2. Compute $$\varphi(n) = (p-1)(q-1)$$ (or use $$\lambda(n)$$ in modern descriptions).  
3. Choose public exponent $$e$$ coprime to $$\varphi(n)$$; compute $$d$$ with

$$
ed \equiv 1 \pmod{\varphi(n)}.
$$

4. Public key $$(n,e)$$; private key $$d$$ (and usually $$p,q$$).

**Encryption / decryption (textbook, simplified).** Message representative $$m$$ with $$0 \le m < n$$:

$$
c \equiv m^e \pmod n, \qquad m \equiv c^d \pmod n.
$$

Correctness follows from Euler/Fermat-type cancellation when $$\gcd(m,n)=1$$ (and standard fixes handle edge cases). Intuition: anyone can raise to the eth power mod $$n$$; extracting eth roots without $$d$$ appears hard, and knowing $$d$$ is tightly connected to knowing the factorization of $$n$$ in classical treatments.

**Signatures (slogan).** Sign by applying the private exponent to a hashed message representative; verify with the public exponent. Details require padding schemes (e.g. PSS); bare textbook RSA is not a complete secure implementation.

The **2002 Turing Award** honors RSA as a practical public-key cryptosystem that helped create an industry and a mathematical research field.

---

## 5. Hardness culture: not the same as P vs NP

Classical crypto assumptions—“factoring is hard,” “DLP is hard in this group”—are **average-case, concrete** conjectures about specific problems, not theorems that $$\mathbf{P} \ne \mathbf{NP}$$.

- NP-completeness is worst-case combinatorial hardness under poly-time reductions.  
- Factoring is in NP ∩ coNP under natural decision versions and is not believed NP-complete.  
- Crypto needs problems that are hard **on typical random instances** for key generation, yet easy for honest parties with trapdoors.

See [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) for the complexity map and Chapter 03 for number-theoretic mechanism chains. Do not say “RSA is secure because SAT is NP-complete.”

---

## 6. Post-quantum caution (LO6)

Shor’s algorithm (quantum) factors integers and computes discrete logs in polynomial time in the standard models—**if** a large-scale fault-tolerant quantum computer exists. That does not make RSA “already broken” on your laptop today; it **does** mean long-term confidentiality of recorded traffic and future public-key infrastructure must plan migration.

**Post-quantum cryptography (PQC)** studies classical algorithms believed resistant to quantum attack—lattices, codes, hash-based signatures, multivariate systems—now moving through NIST standardization and deployment. **Quantum key distribution** is a different technology family; it is not a drop-in replacement for all public-key use cases.

LO6 media filter:

| Headline flavor | Careful reading |
|-----------------|-----------------|
| “Quantum computers destroy all encryption tomorrow” | Timeline and scope unclear; symmetric crypto with larger keys is less affected than RSA/ECC. |
| “We’re safe forever because AES exists” | Key exchange and signatures still need quantum-aware public-key (or shared secrets). |
| “PQC is pure hype” | Standardization and migration are active, serious engineering-math programs. |

Details: [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/).

---

## 7. Ethics and scope

Public-key mathematics protects hospitals, journalists, and ordinary users; the same mathematics can be discussed by attackers. This course teaches **definitions and mechanisms for literacy**, not operational guidance for unauthorized access, fraud, or interception. Academic crypto also studies adversarial models precisely so defenders can design better systems—see the next lecture on **semantic security** and zero-knowledge.

---

## 8. Confusions

| Claim | Correction |
|-------|------------|
| “Public-key means my messages are publicly readable.” | Public *keys* are publishable; ciphertexts should still be confidential under the security model. |
| “DH transmits the password $$g^{ab}$$ in the clear.” | $$g^{ab}$$ is computed locally; only $$g^a,g^b$$ are sent (still need authentication in practice). |
| “RSA security is only ‘multiply two primes.’” | Keygen uses primes; security rests on the hardness of inverting the trapdoor without factorization/related secrets, plus padding and implementation. |
| “If P = NP, only crypto dies.” | Much more would collapse; conversely, P ≠ NP alone does not automatically yield secure cryptosystems. |
| “Elliptic curves change the slogan completely.” | Groups change; the DH-style exponent agreement slogan remains. |

---

## Exercises

1. In two sentences, contrast symmetric and public-key cryptography’s bootstrap problems.  
2. Write the Diffie–Hellman messages and the shared secret algebraically.  
3. Define the discrete log problem in $$\mathbb{Z}/p\mathbb{Z}^\times$$ in one line.  
4. Given tiny pedagogical primes (classroom toy sizes only), compute an RSA key pair and encrypt a small integer—then explain why toy sizes teach mechanisms but not security.  
5. **≤200 words:** Why is “factoring is NP-complete” the wrong slogan for RSA?  
6. **LO6:** Rewrite a hyperbolic quantum-crypto headline into three precise sentences.  
7. Link one mechanism here to a concrete lemma in [Chapter 03]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/) (Fermat/Euler, gcd, modular inverse).  
8. What problem does hybrid encryption solve that pure RSA message encryption does not solve well at internet scale?

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/public-key-crypto/`.

**From the research pack (must-know slogans)**

- Diffie–Hellman (2015 Turing): public-key exchange; discrete log hardness culture.
- Rivest–Shamir–Adleman (2002 Turing): RSA — factoring-based public-key encryption/signatures.
- Asymmetry: easy forward operations vs hard inverses without trapdoor knowledge.
- Cross-link Ch.3 crypto applications.

**Recommended order**


**Official / primary written hubs**

- Diffie Turing: https://amturing.acm.org/award_winners/diffie_8371646.cfm  
- Hellman Turing: https://amturing.acm.org/award_winners/hellman_4055781.cfm  
- Rivest Turing: https://amturing.acm.org/award_winners/rivest_1562803.cfm  
- Shamir Turing: https://amturing.acm.org/award_winners/shamir_2327856.cfm  
- Adleman Turing: https://amturing.acm.org/award_winners/adleman_7308544.cfm  

Complete URL bibliography: `research/video-research/public-key-crypto/references.md`.

## References


### Video research pack (all URLs)

Complete list: `research/video-research/public-key-crypto/references.md`.

1. Diffie Turing — https://amturing.acm.org/award_winners/diffie_8371646.cfm  
2. Hellman Turing — https://amturing.acm.org/award_winners/hellman_4055781.cfm  
3. Rivest Turing — https://amturing.acm.org/award_winners/rivest_1562803.cfm  
4. Shamir Turing — https://amturing.acm.org/award_winners/shamir_2327856.cfm  
5. Adleman Turing — https://amturing.acm.org/award_winners/adleman_7308544.cfm  
6. Wikipedia — Public-key cryptography — https://en.wikipedia.org/wiki/Public-key_cryptography  
7. Wikipedia — Diffie–Hellman key exchange — https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange  
8. Wikipedia — RSA (cryptosystem) — https://en.wikipedia.org/wiki/RSA_(cryptosystem)  
9. Original DH paper culture (IEEE) — https://ee.stanford.edu/~hellman/publications/24.pdf  
10. Research pack folder: `research/video-research/public-key-crypto/`.

1. ACM Turing Award — Rivest, Shamir, Adleman (2002): [amturing.acm.org](https://amturing.acm.org/).  
2. ACM Turing Award — Diffie & Hellman (2015): [amturing.acm.org](https://amturing.acm.org/).  
3. W. Diffie & M. Hellman, “New directions in cryptography,” *IEEE Trans. Inf. Theory*, 1976.  
4. R. Rivest, A. Shamir, L. Adleman, “A method for obtaining digital signatures and public-key cryptosystems,” *Comm. ACM*, 1978.  
5. J. Katz & Y. Lindell, *Introduction to Modern Cryptography*; D. Boneh & V. Shoup, *A Graduate Course in Applied Cryptography* (online).  
6. Course: [Number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/); [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/).

---

## Further directions

- Read a modern treatment of **IND-CPA / IND-CCA** security definitions as preparation for Goldwasser–Micali.  
- Compare finite-field DH with elliptic-curve DH at the level of group choice and key sizes.  
- Follow NIST PQC project summaries for lattice-based KEM/signature names and migration vocabulary.  
- Next: [Goldwasser, Micali, and Foundations of Modern Cryptography]({{ site.baseurl }}/contents/en/chapter09/09_07_Goldwasser_Micali/).
