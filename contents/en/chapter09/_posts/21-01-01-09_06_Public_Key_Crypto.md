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

For thousands of years—from Julius Caesar's shift ciphers to the Enigma machines of World War II—cryptography was trapped by a seemingly unbreakable paradox: to speak privately, two people first had to **meet in advance** (or dispatch a courier with a locked briefcase) to agree on a shared secret key. In the age of the Internet, how could your browser send a credit card number safely to a shop halfway across the planet when you have **never met** and every packet travels across public wires anyone can eavesdrop on?

In the mid-1970s, two mathematical breakthroughs shattered that paradox. **Whitfield Diffie** and **Martin Hellman** (with closely related work by Ralph Merkle) articulated **public-key cryptography** and proposed **Diffie–Hellman key exchange**, allowing two strangers to agree on a shared secret in plain view of eavesdroppers. Soon after, **Ron Rivest, Adi Shamir, and Leonard Adleman** published **RSA**, a public-key encryption and digital signature scheme whose trapdoor rests on the difficulty of factoring large integers.

Rivest, Shamir, and Adleman received the **ACM A.M. Turing Award in 2002**, and Diffie and Hellman received it in **2015** (official materials: [amturing.acm.org](https://amturing.acm.org/)). This lecture is a **mathematics-first** tour of the mechanisms—modular arithmetic, discrete logarithms, factoring trapdoors—not a cookbook for attacking systems, not legal advice, and not a guide to misuse. Security is computational hardness plus careful engineering; we teach the ideas that make that hardness work.

---

## Learning objectives

After this lecture you should be able to:

- Explain the **public-key idea**: separate capabilities to encrypt/verify from decrypt/sign via key pairs.
- Describe **Diffie–Hellman** as agreement on $$g^{ab}$$ from public $$g^a$$ and $$g^b$$.
- State the **discrete logarithm** problem as the hardness intuition behind many DH-style systems.
- Outline **RSA** at the level of $$n=pq$$, exponents $$e,d$$, and modular exponentiation.
- Connect these schemes to [number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/).
- Maintain **post-quantum caution**: classical public-key assumptions are threatened by large-scale quantum algorithms; migration is an active standardization story.
- Keep ethical framing: educational mechanisms, not operational attack instructions for harm.

**Prerequisites.** Congruences $$a \equiv b \pmod n$$; exponents; primes. Chapter 03’s crypto lecture is ideal preparation.

**Cross-links.** [Number theory → cryptography]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/); [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/); [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/); [Goldwasser–Micali foundations]({{ site.baseurl }}/contents/en/chapter09/09_07_Goldwasser_Micali/).

---

## Background Knowledge Map: What Are Public-Key Cryptography and Computational Number Theory?

Behind the little padlock icon in your browser sits a striking reversal of mindset from **Computational Number Theory** and **Public-Key Cryptography**. Normally in computer science, a *hard* problem is an enemy to defeat. In cryptography, **computational asymmetry**—easy forward, brutally hard backward—becomes our most valuable raw material!

The entire public-key edifice revolves around a **trapdoor one-way function**—like mixing two buckets of paint or shattering a ceramic vase: doing it takes a second, undoing it is practically impossible *unless* you hold a secret trapdoor. Two classical mathematical mines launched the field:
1. **The multiplicative group modulo a prime $$p$$ (Diffie–Hellman):** computing $$g^a \bmod p$$ is lightning fast ($$O(\log a)$$ multiplications via repeated squaring), yet recovering the exponent $$a$$ from $$g^a \bmod p$$ (**the discrete logarithm problem — DLP**) appears extraordinarily hard when $$p$$ has thousands of bits.
2. **Integer factorization (RSA):** multiplying two 1024-bit primes $$p \times q = n$$ takes microseconds, yet factoring $$n$$ back into $$p$$ and $$q$$ demands massive number-field sieve computations far beyond classical hardware.

Watch a **10-second toy Diffie–Hellman exchange with real numbers**: agree publicly on $$p = 23$$, $$g = 5$$. Alice picks secret $$a = 6$$ and broadcasts $$A = 5^6 \bmod 23 = 8$$. Bob picks secret $$b = 15$$ and broadcasts $$B = 5^{15} \bmod 23 = 19$$. Alice computes $$19^6 \bmod 23 = 2$$; Bob computes $$8^{15} \bmod 23 = 2$$. Both now share the secret $$K = 2$$ without ever transmitting $$a$$, $$b$$, or $$2$$!

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

### Worked Example (Step by Step): Hand-Running RSA ($$n = 55$$) with Repeated Squaring

Pick $$p = 5,\ q = 11 \implies n = 55$$ and $$\varphi(55) = 4 \times 10 = 40$$.
1. **Compute private exponent $$d$$ via the extended Euclidean algorithm:** pick $$e = 3$$ (since $$\gcd(3,40)=1$$). Dividing $$40$$ by $$3$$:
$$
40 = 13 \times 3 + 1 \implies (-13)\cdot 3 \equiv 1 \pmod{40} \implies d = -13 + 40 = 27.
$$
2. **Encrypt message $$m = 7$$:**
$$
c = 7^3 \bmod 55 = 343 \bmod 55 = 13 \qquad (\text{since } 343 = 6\times 55 + 13).
$$
3. **Decrypt $$13^{27} \bmod 55$$ by repeated squaring** (write $$27 = 16 + 8 + 2 + 1$$):
   - $$13^1 \equiv 13$$,
   - $$13^2 = 169 = 3\times 55 + 4 \equiv 4$$,
   - $$13^4 \equiv 4^2 = 16$$,
   - $$13^8 \equiv 16^2 = 256 = 4\times 55 + 36 \equiv -19$$,
   - $$13^{16} \equiv (-19)^2 = 361 = 6\times 55 + 31 \equiv 31 \pmod{55}$$.
   Multiply the four pieces: $$13^{27} \equiv 31 \cdot (-19) \cdot 4 \cdot 13$$. Pair them up: $$31\cdot 4 = 124 \equiv 14$$ and $$(-19)\cdot 13 = -247 = -5\times 55 + 28 \equiv 28$$. Finally, $$14 \cdot 28 = 392 = 7\times 55 + 7 \equiv 7 \pmod{55}$$ — **recovering the exact original message $$m = 7$$!**

### Deep-Dive Explanation: Four Steps Turning Modular Arithmetic into Your HTTPS Padlock (Read Slowly)

1. **Authenticate the server with digital signatures:** your browser verifies the server's certificate (signed via RSA/ECDSA) to be certain you are talking to your real bank and not a man-in-the-middle imposter.
2. **Negotiate a fresh session key via Diffie–Hellman / ECDHE:** both sides exchange public $$g^a, g^b$$ (on elliptic curves, increasingly hybridized with post-quantum ML-KEM) to derive a one-time shared secret $$K$$.
3. **Switch to high-speed symmetric encryption:** feed $$K$$ into AES-GCM or ChaCha20 to encrypt the actual webpage, images, and payment data at gigabit speeds.
4. **Destroy the session key when the tab closes (Forward Secrecy):** even if the server's long-term private key leaks five years later, past recorded traffic remains unreadable.

**Quick check.** Public-key cryptography is **not** used to encrypt a 1 GB video directly (far too slow); it solves *trust bootstrapping and key exchange*, while symmetric ciphers carry the bulk traffic.

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

## 6. Post-quantum caution

Shor’s algorithm (quantum) factors integers and computes discrete logs in polynomial time in the standard models—**if** a large-scale fault-tolerant quantum computer exists. That does not make RSA “already broken” on your laptop today; it **does** mean long-term confidentiality of recorded traffic and future public-key infrastructure must plan migration.

**Post-quantum cryptography (PQC)** studies classical algorithms believed resistant to quantum attack—lattices, codes, hash-based signatures, multivariate systems—now moving through NIST standardization and deployment. **Quantum key distribution** is a different technology family; it is not a drop-in replacement for all public-key use cases.

Media filter:

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

## Video tham khảo

- **xem trước** — [Secret Key Exchange (Diffie-Hellman) - Computerphile](https://www.youtube.com/watch?v=NmM9HA2MQGI) — Computerphile, English. Watch first. “Secret Key Exchange (Diffie-Hellman) - Computerphile” orients the lesson’s aim: Explain the public-key idea: separate capabilities to encrypt/verify from decrypt/sign via key pairs.
- [Diffie Hellman -the Mathematics bit- Computerphile](https://www.youtube.com/watch?v=Yjrfm_oRO0w) — Computerphile, English. A second pass once the main claim is in view: Explain the public-key idea: separate capabilities to encrypt/verify from decrypt/sign via key pairs.
- [Lecture 13: Diffie-Hellman Key Exchange and the Discrete Log Problem by Christof Paar](https://www.youtube.com/watch?v=aeOzBCbwxUo) — Introduction to Cryptography by Christof Paar, English. Further depth after the first two, still tied to this lesson: Explain the public-key idea: separate capabilities to encrypt/verify from decrypt/sign via key pairs.
