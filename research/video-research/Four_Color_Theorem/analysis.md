# Mode B — analysis: Four Color Theorem

## Status

**Proved** (1976 Appel–Haken; improved RSST; formalized in Coq by Gonthier 2005).  
**Solved ≠ trivial.** Century of attempts; first major computer-assisted proof culture shock.

## Statement

Every planar map (connected regions meeting along positive-length borders) is 4-colorable; equivalently every simple planar graph is 4-vertex-colorable.

Five-color theorem: classical short proofs (Heawood / Kempe-style induction).

## Proof architecture (slogans)

1. Minimal counterexample → unavoidable set of configurations.  
2. Each configuration **reducible** (cannot appear in a minimal counterexample).  
3. Finite but large case check historically done by computer.  
4. RSST: smaller unavoidable set (~633 configurations).  
5. Gonthier: machine-checked formalization — trust the proof assistant kernel.

## Extraction slogans

1. Computer checks **designed finite cases**, not “random maps.”  
2. Formalization strengthens confidence; does not mean the theorem “only now counts.”  
3. Higher genus: Heawood numbers (torus needs up to 7).  
4. Contrast with open analytic problems: finite combinatorial explosion vs infinite analytic landscape.

## Confusions

| Claim | Verdict |
|-------|---------|
| “Four colors sometimes not enough” | Fail under standard hypotheses |
| “Five colors also needs a computer” | Fail |
| “Solved problems are easy” | Fail |

## URLs

See `references.md`.
