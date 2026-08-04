---
layout: post
title: "Goldwasser, Micali, and Foundations of Modern Cryptography (Turing 2012)"
chapter: '09'
order: 7
owner: Nguyen Le Linh
lang: en
categories:
- chapter09
---

Inventing RSA and Diffie–Hellman gave the world **mechanisms**. **Shafi Goldwasser** and **Silvio Micali** helped give cryptography a **definitional backbone**: what does it mean, mathematically, for encryption to hide information from a computationally bounded adversary? What can be proved about a statement without revealing why it is true? How do interaction and randomness become resources in security proofs?

Goldwasser and Micali received the **ACM A.M. Turing Award in 2012** for “pioneering work that laid the complexity-theoretic foundations for the science of cryptography,” including probabilistic encryption and the development of zero-knowledge proofs (with Charles Rackoff in the classic zero-knowledge paper). Official materials: [amturing.acm.org](https://amturing.acm.org/). Related Turing-scale culture includes **Andrew Yao** (Turing 2000) on secure computation and complexity, and proof/complexity bridges associated with **Avi Wigderson** (Abel 2021 with Lovász; deep in interactive proofs and randomness).

This lecture stays at **idea level**: probabilistic encryption, semantic security slogans, zero-knowledge culture, interactive proofs, and the permanent distinction between **crypto theory** and **crypto engineering**.

---

## Learning objectives

After this lecture you should be able to:

- Explain why **deterministic public-key encryption** is insufficient as a security notion (equal messages → equal ciphertexts).
- State the slogan of **probabilistic encryption** and **semantic security** (ciphertext leaks no partial information feasible to compute).
- Describe **zero-knowledge proofs** as “convince without revealing the witness,” at intuition level.
- Outline what **interactive proofs** add beyond classical static proofs.
- Separate **definitional cryptography** from protocol engineering and from number-theoretic primitives alone.
- Name connections to Yao’s secure computation culture and Wigderson-style complexity/randomness themes.
- Apply LO6 to marketing claims (“military-grade,” “unbreakable,” “zero-knowledge means no data ever leaves your phone”).

**Prerequisites.** Public-key slogans from [09_06]({{ site.baseurl }}/contents/en/chapter09/09_06_Public_Key_Crypto/) or [Chapter 03 crypto]({{ site.baseurl }}/contents/en/chapter03/03_05_Number_Theory_Cryptography/); basic probability (negligible success probabilities). Complexity vocabulary from [P vs NP]({{ site.baseurl }}/contents/en/chapter01/01_03_P_vs_NP/) helps.

**Seminar links.** LO4, LO6; [Public-key Diffie/RSA]({{ site.baseurl }}/contents/en/chapter09/09_06_Public_Key_Crypto/); [Complexity theory]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/); [Lovász & Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/); [Future cryptography]({{ site.baseurl }}/contents/en/chapter06/06_06_Future_Cryptography/).

---

## 1. From algorithms to security definitions

A cryptosystem can be published in full and still be unusable if nobody knows **what property it claims**. Early public-key papers proposed schemes and informal hardness stories. Goldwasser–Micali and the school around them insisted on:

1. **Threat models** — what the adversary sees (ciphertext only? chosen plaintexts? chosen ciphertexts?) and what computational power they have.  
2. **Winning conditions** — e.g. recover the message, guess one bit, distinguish two ciphertexts.  
3. **Reductions** — proofs that breaking the scheme yields a break of a named hard problem (quadratic residuosity, factoring, DDH, …) with comparable efficiency.

This is the same intellectual move complexity theory made for algorithms: replace vibes with classes and reductions. Cryptography becomes a **mathematical science of definitions and implications**, not only a catalog of modular formulas.

---

## 2. Why randomness belongs in encryption

Suppose a public-key encryption algorithm is **deterministic**: the ciphertext is a fixed function $$c = E_{\mathrm{pk}}(m)$$. Then anyone can test whether a ciphertext encrypts a candidate message $$m_0$$ by recomputing $$E_{\mathrm{pk}}(m_0)$$—disastrous when message spaces are small (yes/no bids, votes, “pay $$X$$ dollars”). Equal messages produce equal ciphertexts, leaking equality patterns even for large spaces.

**Probabilistic encryption** makes encryption a randomized algorithm:

$$
c \leftarrow E_{\mathrm{pk}}(m; r)
$$

with fresh randomness $$r$$. The same message encrypts to many possible ciphertexts. Correctness requires decryption to recover $$m$$ despite $$r$$.

Goldwasser and Micali’s early probabilistic encryption scheme (based on quadratic residuosity) was a proof of concept that one could encrypt bit-by-bit with rigorous hardness links. Modern systems use different primitives, but the **necessity of randomness** in public-key encryption under standard goals remains.

---

## 3. Semantic security: the slogan

**Semantic security**, introduced by Goldwasser and Micali, formalizes a powerful intuition:

> Whatever an efficient adversary can compute about the plaintext from the ciphertext, it could already compute without the ciphertext—from prior knowledge alone.

In other words, ciphertexts are **computationally inert** as sources of new partial information. A closely related, often easier-to-use formulation is **IND-CPA** (indistinguishability under chosen-plaintext attack): the adversary picks two messages $$m_0,m_1$$; receives an encryption of a random one; and cannot tell which was encrypted with probability much better than $$1/2$$.

These definitions are asymptotic and computational: adversaries are poly-time (or concrete-bounded); advantages must be **negligible** as security parameters grow. Perfect information-theoretic secrecy (Shannon) requires keys as long as messages; semantic security aims for secrecy against *bounded* adversaries using short keys—matching public-key reality.

**LO6.** “Secure encryption” without a named game (CPA, CCA, …) is underspecified. Marketing adjectives are not definitions.

---

## 4. Zero-knowledge proofs

A **zero-knowledge proof** lets a prover convince a verifier that a statement is true—e.g. “this graph is 3-colorable,” “I know a discrete log,” “this transaction is valid”—without revealing a witness beyond the truth of the claim.

Classic intuition (graph 3-coloring): the prover commits to a random permutation of a coloring and repeatedly reveals colors on a verifier-chosen edge, showing they differ. The verifier becomes convinced the graph is colorable, yet learns nothing usable about the coloring because of randomization and commitments—formalized by a **simulator** that can fake transcripts without knowing the coloring if the verifier is honest (definition families vary: honest-verifier ZK, malicious-verifier ZK, computational vs statistical).

Properties typically demanded of interactive proof systems:

- **Completeness** — honest prover convinces honest verifier on true statements.  
- **Soundness** — cheating prover fails on false statements (except with negligible probability).  
- **Zero-knowledge** — transcripts can be simulated without the secret witness.

ZK protocols underwrite identification schemes, modern proof systems in blockchains, and privacy-preserving credentials—always with the caveat that **real deployments** need careful instantiation, trusted setup questions (in some SNARKs), and implementation security.

---

## 5. Interactive proofs more broadly

Classical NP witnesses are **static certificates**. **Interactive proofs** allow back-and-forth coin flips and messages between prover and verifier. Amazingly, interaction plus randomness can verify languages beyond NP in powerful ways; the IP = PSPACE theorem (Shamir; earlier Lund–Fortnow–Karloff–Nisan) is a crown jewel of complexity theory.

Goldwasser, Micali, and Rackoff’s work sits at the birth of this worldview: proofs as **protocols**, soundness as a game against cheaters, knowledge as something that can be extracted or simulated. Wigderson’s broader program on randomness, interaction, and pseudorandomness (see [Abel 2021 essay]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/)) is intellectual kin: complexity classes become laboratories for what efficient parties can establish.

---

## 6. Yao and the secure computation horizon

**Andrew Yao** (Turing 2000) developed foundational ideas in secure multiparty computation and circuit garbling slogans: parties compute a joint function of private inputs without revealing the inputs beyond the output. Together with zero-knowledge and encryption definitions, this paints cryptography as **computational integrity and privacy for protocols**, not only as “lock icons on websites.”

You need not master garbled circuits here. Carry the map:

| Theme | Question |
|-------|----------|
| Public-key primitives | Can strangers bootstrap confidentiality and authenticity? |
| Semantic security | What does “hides the message” mean against efficient adversaries? |
| Zero-knowledge | Can we prove without showing the witness? |
| Secure computation | Can we compute on secret data collaboratively? |

Goldwasser–Micali are central nodes in that map’s definitional core.

---

## 7. Theory versus engineering

**Crypto theory** proves theorems of the form: *If problem $$X$$ is hard, then scheme $$Y$$ meets definition $$D$$ against adversary class $$A$$.*

**Crypto engineering** chooses parameters, side-channel-resistant implementations, certificate infrastructures, protocol state machines, and human factors. Failures often occur at boundaries: correct definitions, wrong padding; right scheme, leaked randomness; secure building blocks, insecure composition.

A mathematically perfect IND-CPA scheme can still be misused if the product needs IND-CCA and the engineers encrypt without authentication. Conversely, deployed systems may be empirically robust while waiting on tighter reductions. Literacy means respecting both cultures without collapsing them.

---

## 8. Confusions

| Claim | Correction |
|-------|------------|
| “Randomized encryption means decryption is random.” | Encryption coins are fresh; decryption still recovers the unique plaintext (except failure modes). |
| “Semantic security is Shannon perfect secrecy.” | Semantic security is computational; perfect secrecy is information-theoretic and costlier in key material. |
| “Zero-knowledge means the verifier learns nothing including the bit ‘statement is true.’” | The verifier learns (is convinced of) validity; ZK limits *additional* witness leakage. |
| “Interactive proofs are only for cryptographers’ games.” | They reshaped complexity theory (IP = PSPACE) and practical proof systems. |
| “Turing 2012 replaced RSA.” | It foundationally *explained and strengthened* what security means; primitives remain complementary. |

---

## Exercises

1. Give a one-paragraph argument that deterministic public-key encryption leaks equality of messages.  
2. State semantic security in your own words without symbols, then with the IND-CPA game sketch.  
3. List completeness, soundness, and zero-knowledge in one sentence each.  
4. **≤200 words:** How do interactive proofs differ from NP certificates?  
5. Connect one idea here to Diffie–Hellman or RSA from [09_06]({{ site.baseurl }}/contents/en/chapter09/09_06_Public_Key_Crypto/) (e.g. why DH still needs authentication; why RSA needs padding/randomness).  
6. **LO6:** Critique the phrase “zero-knowledge blockchain = total privacy” in five careful sentences.  
7. Read the ACM citation abstract for Goldwasser–Micali at [amturing.acm.org](https://amturing.acm.org/) and underline every definitional noun (security, proof, encryption, …).  
8. Write a bridge paragraph from this lecture to [Wigderson/randomness]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/) or [complexity]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/).

---


## Video sources (math-video-researcher pack)

Use videos for **orientation and research culture**, not as proof substitutes. Full ranking and notes: `research/video-research/goldwasser-micali/`.

**From the research pack (must-know slogans)**

- Turing 2012: probabilistic encryption, semantic security, zero-knowledge proofs culture.
- Proofs as interactive protocols with soundness/completeness error.
- Connects to Wigderson interactive proofs / complexity.

**Recommended order**


**Official / primary written hubs**

- Goldwasser Turing: https://amturing.acm.org/award_winners/goldwasser_8627889.cfm  
- Micali Turing: https://amturing.acm.org/award_winners/micali_9954407.cfm  
- Wigderson Turing 2023 (proof systems culture): https://amturing.acm.org/award_winners/wigderson_3844537.cfm  

Complete URL bibliography: `research/video-research/goldwasser-micali/references.md`.

## References


### Video research pack (all URLs)

Complete list: `research/video-research/goldwasser-micali/references.md`.

1. Goldwasser Turing — https://amturing.acm.org/award_winners/goldwasser_8627889.cfm  
2. Micali Turing — https://amturing.acm.org/award_winners/micali_9954407.cfm  
3. Wikipedia — Shafi Goldwasser — https://en.wikipedia.org/wiki/Shafi_Goldwasser  
4. Wikipedia — Silvio Micali — https://en.wikipedia.org/wiki/Silvio_Micali  
5. Wikipedia — Zero-knowledge proof — https://en.wikipedia.org/wiki/Zero-knowledge_proof  
6. Wikipedia — Semantic security — https://en.wikipedia.org/wiki/Semantic_security  
7. Wikipedia — Goldwasser–Micali cryptosystem — https://en.wikipedia.org/wiki/Goldwasser%E2%80%93Micali_cryptosystem  
8. Wigderson Turing 2023 (proof systems culture) — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
9. ACM announcement culture 2012 — https://awards.acm.org/about/2012-turing  
10. Research pack folder: `research/video-research/goldwasser-micali/`.

1. ACM Turing Award — Shafi Goldwasser & Silvio Micali (2012): [amturing.acm.org](https://amturing.acm.org/).  
2. S. Goldwasser & S. Micali, “Probabilistic encryption,” *J. Computer and System Sciences*, 1984.  
3. S. Goldwasser, S. Micali, C. Rackoff, “The knowledge complexity of interactive proof systems,” *SIAM J. Comput.*, 1989.  
4. O. Goldreich, *Foundations of Cryptography* (vols. 1–2); Katz–Lindell textbook chapters on definitions and ZK.  
5. ACM Turing Award — Andrew C. Yao (2000); Abel Prize materials on Wigderson (2021) for interaction/randomness culture.  
6. Course: [09_06 Public-key]({{ site.baseurl }}/contents/en/chapter09/09_06_Public_Key_Crypto/); [08_06 Lovász–Wigderson]({{ site.baseurl }}/contents/en/chapter08/08_06_Lovasz_Wigderson/); [06_07 Complexity]({{ site.baseurl }}/contents/en/chapter06/06_07_Complexity_Theory/).

---

## Further directions

- Work through a textbook proof that semantic security is equivalent to IND-CPA in standard settings.  
- Study one honest-verifier ZK protocol (Schnorr-style identification) at gadget level.  
- Survey how modern SNARKs/STARKs change the *engineering* of succinct proofs while still living under soundness/ZK definitions.  
- Return to [Chapter 09 Overview]({{ site.baseurl }}/contents/en/chapter09/09_00_Overview/) and rewrite the chapter arc in six sentences using only mechanisms, not award years.
