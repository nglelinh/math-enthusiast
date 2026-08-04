# Mode B — analysis: P vs NP

## 1. Primary video

| Field | Value |
|-------|--------|
| Title | Biggest Puzzle in Computer Science: P vs. NP |
| Channel | Quanta Magazine (features Scott Aaronson) |
| URL | https://www.youtube.com/watch?v=pQsdygaYcE4 |
| Duration | ~20 min |
| Role | ORIENTATION / CORE popular |

## 2. Key definitions

- **P:** decision problems solvable in deterministic polynomial time.
- **NP:** decision problems with polynomial-time **verifiable certificates** (equivalently, nondeterministic poly-time).
- Immediate: $$\mathbf{P}\subseteq\mathbf{NP}$$.
- **Open:** is $$\mathbf{NP}\subseteq\mathbf{P}$$?

### Cook–Levin (proved)

SAT is **NP-complete**: every problem in NP reduces to SAT in poly time. Hence one poly-time algorithm for any NP-complete problem collapses P and NP.

### Barriers (slogans only)

- **Relativization:** some oracles have P = NP, some P ≠ NP — pure diagonalization that relativizes cannot settle.
- **Natural proofs (Razborov–Rudich):** large classes of “natural” circuit lower-bound techniques are blocked if strong pseudorandom generators exist.
- **Algebrization:** further barrier for certain algebraic extensions of relativization.

## 3. Status (2026)

**Open.** Community consensus leans **P ≠ NP**, but consensus is not a proof. No Clay-accepted solution.

## 4. Confusions (LO6)

| Claim | Verdict |
|-------|---------|
| “NP means not polynomial” | **False** |
| “AI solved NP” | **False** (heuristics ≠ class membership) |
| “Crypto is NP-complete so P≠NP freezes RSA” | **Careful false** — crypto needs average-case hardness of specific problems |
| “SAT solvers are fast ⇒ SAT ∈ P” | **False** (worst-case poly-time algorithm missing) |

## 5. Extraction slogans

1. Verify vs search.  
2. NP-complete = one key opens the whole class.  
3. Barriers explain *why naive proof strategies fail*, not that P ≠ NP is unprovable.  
4. Engineering solvers live happily while the worst-case question stays open.

## 6. URLs

See `references.md`.
