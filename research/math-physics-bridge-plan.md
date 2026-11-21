# Physics–Math Bridge Track — Integration Plan

**Status:** P0+P1+P2 complete (Mode S); **P3** uncertainty complete 2026-08-19  
**Decisions locked (2026-08-06):**

| Choice | Decision |
|--------|----------|
| Seminar mode | **Mode S** — optional track; 15-week spine unchanged |
| Bridge deep flagship | **B4 Gauge theory as geometry** (alternate W10 optional) |
| Lie groups home | **Chapter 03** (+ polish link from `04_04` Symmetry) |
| Donaldson–SW home | **Chapter 06** (P1); ch02 short cross-ref later |
| Bilingual | EN+VI same sprint for P0 |

## Seven axes

1. Hilbert & spectrum (QM)  
2. Groups & representations  
3. Spacetime geometry (GR)  
4. Gauge = geometry (Yang–Mills)  
5. Topology meets physics (index, instanton, anomaly)  
6. Infinities under control (distributions, path integral, RG, constructive QFT)  
7. Pure-math feedback (Donaldson–SW, duality, NCG)

## P0 deliverables (this sprint)

| ID | Title | Path |
|----|-------|------|
| B1 | Hilbert Space & Spectral Language of QM | `ch06` order 18 |
| B2 | From Spacetime Geometry to Gravity | `ch03` order 10 |
| B3 | Symmetry, Lie Groups & Particle Physics | `ch03` order 11 |
| B4 | Gauge Theory as Geometry | `ch06` order 19 |
| B5 | Yang–Mills Existence & Mass Gap | `ch01` order 10 |
| Hub | Math Physics rewrite + overviews + home | `06_11`, overviews, contents |

## P1 deliverables — **done 2026-08-07**

| ID | Title | Path |
|----|-------|------|
| C1 | Distributions: Making Dirac Honest | `ch03` order 12 |
| C2 | Path Integrals: Idea, Power, Math Status | `ch06` order 20 |
| C3 | Instantons, Topology, and Anomalies | `ch06` order 21 |
| C4 | Renormalization Group | `ch06` order 22 |
| C5 | Donaldson to Seiberg–Witten | `ch06` order 23 |

VI mirrors under `contents/vi/` same basenames. Hub/overview/Uhlenbeck/Atiyah cross-links updated.

## P2 deliverables — **done 2026-08-07**

| ID | Title | Path |
|----|-------|------|
| D1 | Operator Algebras from Quantum Theory | `ch06` order 24 |
| D2 | Noncommutative Geometry (map) | `ch06` order 25 |
| D3 | Spinors, Clifford, Dirac | `ch06` order 26 |
| D4 | Statistical Mechanics and Probability | `ch06` order 27 |
| D5 | Studio: Physics ↔ Math Dictionary | `ch07` order 11 |
| D6 | Studio: Toy Circle Gauge / Aharonov–Bohm | `ch07` order 12 |

VI mirrors under `contents/vi/`. **Track P0+P1+P2 complete** (Mode S optional path).

## P3 deliverables — **done 2026-08-19**

| ID | Title | Path |
|----|-------|------|
| E1 | Uncertainty Principles: Fourier, Heisenberg, Information | `ch06` order 29 |
| E2 | Fractal Uncertainty Principle (Cohen 2025) | `ch06` order 30 |
| E3 | Studio: Spectrograms, Gaussians, Uncertainty | `ch07` order 13 |

Pack: `research/video-research/uncertainty-principles/`. QUE remains open; FUP higher-D is theorem under line porosity.

## Reading path (Mode S)

```
ch01 YM mass gap + Navier–Stokes
  → ch03 GR geometry + Lie groups + Distributions
  → ch04 Symmetry (companion)
  → ch06 Hilbert → Uncertainty (P3) → Fractal UP → Gauge (deep) → Path integral → Instanton/anomaly
       → RG → Donaldson–SW → Math Physics hub → Duality cluster
  → ch08 Uhlenbeck + Atiyah–Singer
  → ch07 Duality dictionary studio (existing)
```

## Definition of done (P0)

- [x] Plan file  
- [x] Hub + overviews EN/VI  
- [x] B1–B5 EN+VI  
- [x] curriculum + passport note + knowledge_graph nodes  

**Shipped 2026-08-06 (P0):**

| ID | EN path |
|----|---------|
| B5 | `contents/en/chapter01/_posts/21-01-01-01_10_Yang_Mills_Mass_Gap.md` |
| B2 | `contents/en/chapter03/_posts/21-01-01-03_10_Geometry_Spacetime_GR.md` |
| B3 | `contents/en/chapter03/_posts/21-01-01-03_11_Lie_Groups_Particle_Physics.md` |
| B1 | `contents/en/chapter06/_posts/21-01-01-06_18_Hilbert_Spectral_QM.md` |
| B4 | `contents/en/chapter06/_posts/21-01-01-06_19_Gauge_Geometry_YM.md` |

VI mirrors use the same basenames under `contents/vi/`.
