---
layout: post
title: "Number Theory → Cryptography"
chapter: '03'
order: 5
owner: Nguyen Le Linh
lang: en
categories:
- chapter03
lesson_type: required
---

Once the purest of pure mathematics—Gauss’s “queen of mathematics”—**number theory** now underwrites secure communication on the internet. Every TLS handshake, software signature, and messenger lock icon is a consumer of modular arithmetic, prime generation, and hard problems on groups.

This **Section 3 flagship** traces one clean mechanism chain:

**modular arithmetic → trapdoor functions → public-key cryptography (RSA, Diffie–Hellman, ECC) → protocols on the real internet → quantum shadows and post-quantum lattices.**

The goal is **LO4**: relate a classical field to a named technology with a correct one-step mechanism—not “number theory is used in crypto” as a slogan, but *which* hardness and *how* keys work at a conceptual level.

**Path:** congruences → symmetric vs public-key → RSA → DH → ECC → signatures/PKI/hybrid → hardness culture → PQC → confusions.

---

## Learning objectives

After this lecture you should be able to:

- Compute and interpret simple **congruences** $$a \equiv b \pmod{n}$$ and explain fast modular exponentiation.
- Explain the **public-key idea**: separate encryption capability from decryption capability via a trapdoor.
- State the **RSA mechanism** at the level of moduli $$n=pq$$, exponents $$e,d$$, and the informal factoring assumption.
- Describe **Diffie–Hellman** as agreement on $$g^{ab}$$ from public $$g^a,g^b$$ and the discrete-log intuition.
- Name why **elliptic curves** shrink keys and why **post-quantum** systems shift to lattices/codes/hashes.
- Avoid confusions (RSA is not “just multiply primes”; security is computational hardness plus engineering; PQC ≠ only QKD).

**Prerequisites.** Integers, primes, basic exponents. No prior crypto course.

**Seminar link.** LO4; pairs with [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) (hardness culture), [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/), [Riemann]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/) (primes as pure math).

---

## 1. Modular arithmetic: the algebra of remainders

Fix a positive integer $$n$$ (the **modulus**). We say

$$
a \equiv b \pmod{n}
$$

when $$n$$ divides $$a-b$$—equivalently, $$a$$ and $$b$$ leave the same remainder on division by $$n$$.

Working **mod $$n$$** is like a clock with $$n$$ hours: after $$n-1$$ you wrap to $$0$$. You can add and multiply congruences consistently:

$$
a\equiv a',\quad b\equiv b' \pmod{n} \implies a+b\equiv a'+b',\quad ab\equiv a'b' \pmod{n}.
$$

The ring $$\mathbb{Z}/n\mathbb{Z}$$ is the algebraic home of textbook crypto. When $$n=p$$ is prime, every nonzero residue has a multiplicative inverse—$$\mathbb{Z}/p\mathbb{Z}$$ is a field—so division works and linear algebra over finite fields becomes available (important for AES’s finite-field arithmetic and for elliptic curves over $$\mathbb{F}_p$$).

**Fast powering.** Computing $$a^e \bmod n$$ for huge $$e$$ is feasible via **repeated squaring** in $$O(\log e)$$ multiplications. Computing *eth roots* or *discrete logarithms* is believed hard in carefully chosen settings. That asymmetry—easy power, hard reverse—is the raw ore of public-key cryptography.

**Euler / Fermat flavor.** If $$p$$ is prime and $$p\nmid a$$, then $$a^{p-1}\equiv 1 \pmod{p}$$ (Fermat). More generally Euler’s theorem uses $$\varphi(n)$$, the count of residues coprime to $$n$$. RSA’s correctness rests on such modular exponent cancellation—not on secrecy of the algorithm (the algorithm is public).

**Euclid’s algorithm** computes $$\gcd$$ and modular inverses in logarithmic time—nineteenth-century number theory as twenty-first-century subroutine.

---

## 2. Symmetric crypto vs public-key crypto

**Symmetric** cryptography: Alice and Bob share a secret key in advance; encryption and decryption use the same secret (AES-GCM, ChaCha20-Poly1305, …). Excellent for bulk data at wire speed; terrible for the bootstrapping question: *how do we start talking securely if we never met and the network is full of eavesdroppers?*

**Public-key** cryptography (Diffie–Hellman 1976; RSA 1978; elliptic-curve variants thereafter): each party publishes a **public** key and keeps a **private** key. Anyone can encrypt to you with your public key; only you can decrypt. Digital signatures reverse the intuition: only you can sign; anyone can verify with your public key.

The mathematical miracle is a **trapdoor one-way function**: easy to compute, hard to invert without secret structure, easy to invert with the trapdoor.

**Kerckhoffs’s principle.** Security should rest on key secrecy, not on hiding the algorithm. Modern crypto assumes algorithms are public and under attack by experts.

---

## 3. RSA: factoring as a trapdoor (conceptual)

**Setup (simplified textbook RSA).**

1. Choose large secret primes $$p,q$$; publish $$n=pq$$ (but not $$p,q$$).  
2. Compute $$\varphi(n)=(p-1)(q-1)$$ (secret).  
3. Choose public exponent $$e$$ coprime to $$\varphi(n)$$ (often $$e=65537$$ in practice).  
4. Compute private $$d$$ with $$ed\equiv 1 \pmod{\varphi(n)}$$ (modular inverse).  
5. Encrypt message representative $$m$$: $$c \equiv m^e \pmod{n}$$.  
6. Decrypt: $$m \equiv c^d \pmod{n}$$.

**Mechanism in one sentence.**  
*Encrypting is modular exponentiation with a public exponent; decrypting needs an inverse exponent that is easy if you know $$\varphi(n)$$ (hence $$p,q$$) and believed hard if you only know $$n$$.*

**Hardness assumption (informal).** Factoring large semiprimes is computationally infeasible at recommended sizes (thousands of bits). If factoring were easy, RSA’s trapdoor would collapse. Nuance: security reductions relate RSA inversion to factoring only partially; also **padding** (OAEP, PSS) is mandatory—raw textbook RSA is malleable and not deployable as-is.

**What pure number theory contributed.** Euclid’s algorithm, modular inverses, Euler’s $$\varphi$$, prime generation (including probabilistic primality tests), and the computational complexity of factoring—Gauss-to-Gentry intellectual history compressed into a key exchange.

**Parameter hygiene.** Small $$e$$ with bad padding, shared primes across moduli, biased random primes, and side channels have all broken “mathematically correct” RSA in the wild. Number theory supplies the trapdoor; engineering supplies the rest of the attack surface.

---

## 4. Diffie–Hellman and discrete logarithms

Public parameters: a group (classically the multiplicative group modulo a prime, or an elliptic-curve group) and a generator $$g$$ of a large subgroup of prime order.

- Alice picks secret $$a$$, sends $$A=g^a$$.  
- Bob picks secret $$b$$, sends $$B=g^b$$.  
- Shared secret: $$A^b = B^a = g^{ab}$$.

**Discrete log problem (DLP):** given $$g$$ and $$g^a$$, recover $$a$$. If DLP is hard, eavesdroppers should not compute $$g^{ab}$$ from the public values alone (under CDH/DDH-style assumptions, carefully stated).

**Mechanism.**  
*Public transmissions are group exponentiations; the shared secret is a bilinear combination of secrets in the exponent—visible only to parties who know at least one exponent.*

**Finite-field DH** needs large primes and safe parameters against index-calculus attacks. This pressure helped motivate elliptic curves.

---

## 5. Elliptic curve cryptography (ECC)

An **elliptic curve** over a field (here a finite field $$\mathbb{F}_q$$) can be written, in simplified Weierstrass form, as

$$
y^2 = x^3 + Ax + B
$$

with nonzero discriminant. The set of points plus a point at infinity forms an abelian **group** under a geometric chord-and-tangent law. Scalar multiplication $$P\mapsto aP$$ (adding $$P$$ to itself $$a$$ times) is easy; inverting it (elliptic curve discrete log) is believed hard for well-chosen curves.

**Same protocol pattern as DH**, smaller keys for comparable conjectured classical security (e.g. 256-bit curves vs 3072-bit RSA moduli in common recommendations—exact numbers evolve with guidance). Your phone’s TLS stack almost certainly negotiates ECDHE.

**Mechanism.**  
*ECC relocates Diffie–Hellman from multiplicative groups of finite fields to groups of points on carefully chosen curves—same trapdoor shape, denser security per bit.*

Deep arithmetic geometry quietly enters commodity security—another chapter-theme win for “pure” mathematics.

---

## 6. Signatures, certificates, and hybrid encryption

Public-key encryption alone does not build the web. You also need:

- **Signatures** (RSA-PSS, ECDSA, EdDSA, …) so software updates and documents prove origin and integrity.  
- **Certificates** (PKI / X.509) binding keys to identities via trusted authorities or other trust models.  
- **Hybrid encryption**: use public-key crypto (or KEMs) to establish a symmetric session key, then AES (or similar) for bulk data.  
- **Authenticated encryption** so ciphertext cannot be silently mutated.

Number theory sits in the handshake; engineering, economics, and law sit in the trust model. Both can fail—bad randomness (Debian OpenSSL disaster), compromised CAs, protocol downgrade attacks—without the underlying hardness conjecture being “false.”

---

## 7. Hardness culture: crypto meets complexity

Cryptography needs problems that are:

1. Easy to sample instances of,  
2. Easy to solve with a trapdoor / secret,  
3. Hard for adversaries on **typical** instances (average-case, not only worst-case).

This is cousin to, but not the same as, **P vs NP**. NP-completeness is about worst-case difficulty of decision problems; crypto wants *usable* average-case hardness with structure (see [P vs NP lecture]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/)). Still, both sit in the culture of **computational intractability as a resource**.

One-way functions, pseudorandom generators, and zero-knowledge proofs refine this culture far beyond RSA—yet the undergraduate-accessible story still begins with modular arithmetic.

---

## 8. Quantum shadows and post-quantum cryptography

**Shor’s algorithm** (quantum) factors integers and computes discrete logarithms in polynomial time—threatening RSA and classical DH/ECC if large, reliable quantum computers arrive. Grover’s algorithm gives quadratic speedups for unstructured search, nudging symmetric key sizes but not destroying AES at doubled length the way Shor destroys RSA.

**Post-quantum cryptography (PQC)** shifts hardness assumptions toward problems not known to fall to Shor, notably:

- **Lattices** (Learning With Errors and relatives)—geometry of numbers as crypto,  
- **Codes** (McEliece-style),  
- **Hash-based signatures** (conservative, stateful or SPHINCS-like stateless designs),  
- Multivariate and isogeny-based ideas—always under active cryptanalysis (some isogeny systems have fallen).

NIST’s PQC standardization process (Kyber/ML-KEM, Dilithium/ML-DSA, etc., with evolving names and parameters) is the institutional face of this transition. See [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/).

**Mechanism shift.**  
*Classical public-key crypto mines number-theoretic one-wayness in multiplicative and elliptic groups; PQC mines hardness in high-dimensional lattices and related structures—still pure math feeding infrastructure.*

---

## 9. Why “pure” number theory was ready

Primality, modular inverses, group structure, and the obsession with primes long predated e-commerce. When Diffie, Hellman, Rivest, Shamir, and Adleman needed trapdoors, the toolbox was already on the shelf. The migration pure → applied did not require renaming the subject; it required recognizing that **conjectured computational hardness** is as valuable as a closed-form formula.

The Riemann Hypothesis ([Ch.1]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/)) remains a pure beacon about primes; cryptography is a different use of arithmetic—but both testify that integer structure is inexhaustible.

---

### Crypto video hygiene (from research)

Primary popular path: [Numberphile RSA](https://www.youtube.com/watch?v=M7kEpw1tn50) → [RSA-129](https://www.youtube.com/watch?v=YQw124CtvO0) → [Computerphile public key](https://www.youtube.com/watch?v=GSIDS_lvRv4) → [Diffie–Hellman](https://www.youtube.com/watch?v=NmM9HA2MQGI).

- Videos explain *trapdoors* well; they usually omit padding, side channels, and parameter hygiene.
- Correctness of RSA uses Euler/Fermat modular cancellation; security is computational, not information-theoretic.
- Post-quantum transition is policy + mathematics: see [NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography).

## Common confusions

| Claim | Correction |
|-------|------------|
| “RSA security is that multiplication is hard.” | Multiplication is easy; *factoring* the product is the hard direction. |
| “Hiding the algorithm makes it secure.” | Kerckhoffs: assume algorithms are public; secrets are keys. |
| “Bigger $$n$$ always saves you.” | Size matters, but so do padding, side channels, randomness, and protocols. |
| “ECC is secure because curves are complicated.” | Security rests on ECDLP hardness for the chosen curve group, plus correct implementation. |
| “Post-quantum means quantum crypto only.” | PQC usually means classical algorithms meant to resist quantum attacks; QKD is different. |
| “If P ≠ NP, RSA is forever safe.” | Crypto needs average-case hardness of specific problems; see P vs NP caveats. |

---

## Exercises

1. Compute $$17 \bmod 5$$, $$2^8 \bmod 7$$, and find $$x$$ with $$3x\equiv 1 \pmod{7}$$.  
2. Explain public vs private key in two sentences to a non-math friend.  
3. Why does publishing $$n=pq$$ not immediately publish $$p$$ and $$q$$ for large primes?  
4. Diffie–Hellman: if an eavesdropper sees $$g^a$$ and $$g^b$$, what would discrete log allow them to do?  
5. **LO4 synthesis (≤300 words).** State the one-step mechanism linking modular exponentiation to public-key encryption.  
6. Critique a popular article on “unbreakable crypto” for one overclaim (precision practice).  
7. **Stretch.** Why is hybrid encryption used on the web instead of encrypting all bulk traffic with RSA alone?

---

## Video sources (math-video-researcher pack)

Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/number-theory-cryptography/`.

**Recommended order**

1. **ORIENTATION** — Numberphile — Encryption and HUGE numbers (RSA): [https://www.youtube.com/watch?v=M7kEpw1tn50](https://www.youtube.com/watch?v=M7kEpw1tn50).
2. **INTUITION / history** — Numberphile — RSA-129: [https://www.youtube.com/watch?v=YQw124CtvO0](https://www.youtube.com/watch?v=YQw124CtvO0).
3. **FOUNDATION** — Computerphile — Public Key Cryptography: [https://www.youtube.com/watch?v=GSIDS_lvRv4](https://www.youtube.com/watch?v=GSIDS_lvRv4).
4. **CORE** — Computerphile — Diffie-Hellman Key Exchange: [https://www.youtube.com/watch?v=NmM9HA2MQGI](https://www.youtube.com/watch?v=NmM9HA2MQGI).
5. **SURVEY** — Numberphile/Computerphile crypto playlist: [https://www.youtube.com/playlist?list=PLt5AfwLFPxWLXe-ZqZyu0kSsaWd4FjXbj](https://www.youtube.com/playlist?list=PLt5AfwLFPxWLXe-ZqZyu0kSsaWd4FjXbj).
6. **FOUNDATION** — Khan Academy — Journey into cryptography (hub): [https://www.khanacademy.org/computing/computer-science/cryptography](https://www.khanacademy.org/computing/computer-science/cryptography).

Complete URL bibliography: `research/video-research/number-theory-cryptography/references.md`.



### Transcript & frames (flagship extract)

Caption transcripts and time-chunk units for pack videos: `research/video-research/number-theory-cryptography/transcripts/` · status: `research/video-research/number-theory-cryptography/TRANSCRIPT_STATUS.md` · master list: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Captions are auto-downloaded (yt-dlp); treat as navigation aids, not as a substitute for the lesson text.


![Flagship video sample frame]({{ site.baseurl }}/img/video_research/flagships/crypto_rsa_frame01.jpg)

*Figure. Sample still from a primary flagship video (see pack for timestamps).*

## References

Full URL bibliography from video research (including secondary finds): `research/video-research/number-theory-cryptography/references.md`.

### Videos (primary path)

1. Numberphile — Encryption and HUGE numbers (RSA) — https://www.youtube.com/watch?v=M7kEpw1tn50
2. Numberphile — RSA-129 — https://www.youtube.com/watch?v=YQw124CtvO0
3. Computerphile — Public Key Cryptography — https://www.youtube.com/watch?v=GSIDS_lvRv4
4. Computerphile — Diffie-Hellman Key Exchange — https://www.youtube.com/watch?v=NmM9HA2MQGI
5. Numberphile/Computerphile crypto playlist — https://www.youtube.com/playlist?list=PLt5AfwLFPxWLXe-ZqZyu0kSsaWd4FjXbj
6. Khan Academy — Journey into cryptography (hub) — https://www.khanacademy.org/computing/computer-science/cryptography
7. Stanford / Dan Boneh crypto course culture (Coursera/YouTube search) — https://crypto.stanford.edu/~dabo/courses/
8. NIST Post-Quantum Cryptography project — https://csrc.nist.gov/projects/post-quantum-cryptography

### Videos (secondary finds)

9. Numberphile — primes and primality culture videos — https://www.youtube.com/@numberphile

### Papers, books, OCW, and web

10. Rivest, Shamir, Adleman — A Method for Obtaining Digital Signatures… (1978): https://people.csail.mit.edu/rivest/Rsapaper.pdf
11. Diffie & Hellman — New Directions in Cryptography (1976): https://ee.stanford.edu/~hellman/publications/24.pdf
12. NIST PQC standards overview: https://csrc.nist.gov/projects/post-quantum-cryptography
13. Wikipedia — RSA (cryptosystem): https://en.wikipedia.org/wiki/RSA_(cryptosystem)
14. Wikipedia — Diffie–Hellman key exchange: https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
15. Wikipedia — Post-quantum cryptography: https://en.wikipedia.org/wiki/Post-quantum_cryptography

### Course

16. Course: [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/), [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/), [Riemann]({{ site.baseurl }}/contents/en/chapter01/01_02_Riemann_Hypothesis/), [Overview]({{ site.baseurl }}/contents/en/chapter03/03_00_Overview/). Pack: `research/video-research/number-theory-cryptography/`.

## Further directions

- Seminar path uses this flagship for LO4 mechanism writing.  
- Stretch: implement toy RSA with tiny primes (not secure); then discuss why toy sizes fail and why padding matters.  
- Continue to [Graph Theory → Networks]({{ site.baseurl }}/contents/en/chapter03/03_06_Graph_Theory_Networks/) or jump to [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/) for PQC depth.  
- Restate the core mechanism of this essay in one paragraph; note one precise question you still have.
