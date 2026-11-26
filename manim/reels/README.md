# Short Manim reels (1080x1920, dark background, no music)

Source for the `### Video ngắn` / `### Short video` clips in the lessons.
Render both languages: `REEL_LANG=vi|en manim -qh <file>.py <Scene>`
(9x16 frame, 1 unit = 120 px, background #10121a). Captions live in the `TX` dict of each scene; numbers are asserted inside each scene.
Compress: ffmpeg -i in.mp4 -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p -movflags +faststart -an out.mp4
Output: public/videos/reels/<slug>_<lang>.mp4

| scene file | class | slug |
|---|---|---|
| collatz.py | Collatz | collatz-orbit-97 |
| cantor.py | Cantor | cantor-diagonal |
| sqrt2.py | Sqrt2 | sqrt2-irrational-squares |
| logistic.py | Logistic | logistic-two-orbits |
| chaosgame.py | ChaosGame | chaos-game-sierpinski |
| fourier.py | Fourier | square-wave-fourier |
| packing.py | Packing | disc-packing-2d |
| konigsberg.py | Konigsberg | konigsberg-bridges |

## Batch 2 (needs `common_b.py`; same render/compress recipe)

| scene file | class | slug |
|---|---|---|
| euler.py | Euler | zeta-euler-product |
| twins.py | Twins | twin-primes-count |
| kakeya.py | Kakeya | kakeya-deltoid-needle |
| clt.py | CLT | clt-dice-bell |
| dh.py | DH | diffie-hellman-mod23 |
| hilbert.py | Hilbert | hilbert-curve |
| ball.py | Ball | ball-volume-dimensions |
| life.py | Life | life-r-pentomino |
| catenoid.py | Catenoid | soap-film-catenoid |
| sir.py | SIR | sir-r0-epidemic |
| ot.py | OT | optimal-transport-1d |
| chsh.py | CHSH | chsh-bell-game |

Every scene asserts its numbers before drawing (e.g. twin counts 8/35/205/1224/8169, deltoid area = pi/8 and chords inside the curve, 5 is a primitive root mod 23, R-pentomino has 116 cells at generation 1103, catenoid limits 0.6627 and Goldschmidt 0.528, CHSH = 2 sqrt 2 via the Phi+ state).

## Batch 3 (uses `common_b.py`; same render/compress recipe)

| scene file | class | slug |
|---|---|---|
| pagerank.py | PageRank | pagerank-markov |
| fourcolor.py | FourColor | four-color-kempe |
| zkp.py | ZKP | zkp-3color |
| tarjan.py | TarjanSCC | tarjan-scc |

## Batch 4 (uses `common_b.py` + `vo_gemini.py`)

| scene file | class | slug |
|---|---|---|
| wiles.py | WilesFermat | wiles-fermat |
| halting.py | HaltingProblem | turing-halting |
| godel.py | GodelIncompleteness | godel-incompleteness |
| langlands.py | LanglandsFundamentalLemma | langlands-fundamental-lemma |
| langlands_hitchin.py | LanglandsHitchinFibration | langlands-hitchin-geometry |
| langlands_variants.py | LanglandsVariants | langlands-arithmetic-vs-geometric |
| perelman.py | PerelmanPoincare | perelman-poincare |
| perelman_ricci.py | PerelmanRicciFlow | perelman-ricci-surgery |
| perelman_entropy.py | PerelmanEntropyTools | perelman-entropy-kappa |
| `greentao.py` | `GreenTaoTheorem` | `greentao-theorem_{vi,en}.mp4` | `02_04_Green_Tao` |
| `greentao_gowers.py` | `GreenTaoTransference` | `greentao-majorant-gowers_{vi,en}.mp4` | `02_04_Green_Tao` |
| `greentao_cs.py` | `TaoCompressedSensing` | `tao-compressed-sensing_{vi,en}.mp4` | `02_04_Green_Tao` |

## Batch 5: Fourier epicycles (vi has Gemini TTS voiceover, en silent)

| scene file | class | slug | lesson |
|---|---|---|---|
| koch_fourier.py (math: koch_math.py, voice: koch_vo.py) | KochFourier | koch-fourier-epicycles | chapter03 03_08 Fourier Signal Processing (section 4) |

Pipeline: `source ~/.config/gemini/tts.env && python koch_vo.py synth` -> `REEL_LANG=vi manim -qh koch_fourier.py KochFourier` (writes `vo/koch/starts_vi.json`) -> compress as above -> `python koch_vo.py mux <compressed.mp4> ../../public/videos/reels/koch-fourier-epicycles_vi.mp4`. English: `REEL_LANG=en`, compress only. No LaTeX needed (Unicode Text). `vo/` and `media/` are not to be committed.
| `mirzakhani.py` | `MirzakhaniModuli` | `mirzakhani-moduli-geodesics_{vi,en}.mp4` | `02_05_Mirzakhani_Moduli` |
| `mirzakhani_wp.py` | `MirzakhaniWPVolume` | `mirzakhani-wp-volume_{vi,en}.mp4` | `02_05_Mirzakhani_Moduli` |
| `mirzakhani_magicwand.py` | `MirzakhaniMagicWand` | `mirzakhani-billiards-magicwand_{vi,en}.mp4` | `02_05_Mirzakhani_Moduli` |
| `scholze.py` | `ScholzePerfectoid` | `scholze-perfectoid-overview_{vi,en}.mp4` | `02_06_Scholze_Perfectoid` |
| `scholze_tilting.py` | `ScholzeTilting` | `scholze-tilting-bridge_{vi,en}.mp4` | `02_06_Scholze_Perfectoid` |
| `scholze_impact.py` | `ScholzeImpact` | `scholze-weight-monodromy_{vi,en}.mp4` | `02_06_Scholze_Perfectoid` |

## Batch 4: Gamma function (vi has Gemini TTS voiceover, en silent)

| scene file | class | slug | lesson |
|---|---|---|---|
| gamma_reel.py (math: gamma_math.py, voice: gamma_vo.py) | GammaReel | gamma-function-factorial | chapter01 01_02 Riemann Hypothesis (end of section 3) |

Same pipeline as Batch 3 (`python gamma_vo.py synth`, `REEL_LANG=vi manim -qh gamma_reel.py GammaReel`, compress, `python gamma_vo.py mux ...`). `gamma_math.py` needs `mpmath` and `scipy` (`pip install mpmath` in the manim venv) and asserts every number (Euler integral, recurrence, residues, Bohr–Mollerup counter-example, reflection formula, xi symmetry and trivial zeros, V5 = 8pi^2/15). Unicode text only, no LaTeX.

## Chapter 2 Batch (02_07 – 02_09, vi has Gemini TTS `Algenib` voiceover, en silent)

| scene file | class | slug | lesson |
|---|---|---|---|
| `venkatesh.py` | `VenkateshOverview` | `venkatesh-dynamics-overview_{vi,en}.mp4` | `02_07_Venkatesh_Number_Theory` |
| `venkatesh_subconvexity.py` | `VenkateshSubconvexity` | `venkatesh-subconvexity-mixing_{vi,en}.mp4` | `02_07_Venkatesh_Number_Theory` |
| `venkatesh_topology.py` | `VenkateshTopology` | `venkatesh-torsion-topology_{vi,en}.mp4` | `02_07_Venkatesh_Number_Theory` |
| `viazovska_e8.py` | `ViazovskaE8Magic` | `viazovska-e8-magic-function_{vi,en}.mp4` | `02_08_Viazovska_Sphere_Packing` |
| `viazovska_leech.py` | `ViazovskaLeech24D` | `viazovska-leech-24d_{vi,en}.mp4` | `02_08_Viazovska_Sphere_Packing` |
| `maynard.py` | `MaynardOverview` | `maynard-bounded-gaps_{vi,en}.mp4` | `02_09_Maynard_Primes` |
| `maynard_sieve.py` | `MaynardSieve` | `maynard-multidim-sieve_{vi,en}.mp4` | `02_09_Maynard_Primes` |
| `maynard_digits.py` | `MaynardDigits` | `maynard-missing-digits_{vi,en}.mp4` | `02_09_Maynard_Primes` |
| `birkar_mmp.py` | `BirkarMMP` | `birkar-fano-mmp_{vi,en}.mp4` | `02_10_Birkar_Algebraic_Geometry` |
| `birkar_bab.py` | `BirkarBAB` | `birkar-bab-complements_{vi,en}.mp4` | `02_10_Birkar_Algebraic_Geometry` |
| `huh_chromatic.py` | `HuhChromatic` | `huh-chromatic-logconcave_{vi,en}.mp4` | `02_11_Modern_Combinatorics_Geometry` |
| `huh_lorentzian.py` | `HuhLorentzian` | `huh-lorentzian-bridges_{vi,en}.mp4` | `02_11_Modern_Combinatorics_Geometry` |
| `deng_hilbert6.py` | `DengHilbert6` | `deng-hilbert6-boltzmann_{vi,en}.mp4` | `02_12_Deng_PDE` |
| `deng_wave_kinetic.py` | `DengWaveKinetic` | `deng-wave-kinetic_vi.mp4` | `02_12_Deng_PDE` |
| `pardon_symplectic.py` | `PardonSymplectic` | `pardon-symplectic-vfc_vi.mp4` | `02_13_Pardon_Symplectic` |
| `pardon_fukaya.py` | `PardonFukaya` | `pardon-fukaya-logderived_vi.mp4` | `02_13_Pardon_Symplectic` |
| `tsimerman_o_minimal.py` | `TsimermanOMinimal` | `tsimerman-o-minimal_vi.mp4` | `02_14_Tsimerman_Arithmetic` |
| `tsimerman_andre_oort.py` | `TsimermanAndreOort` | `tsimerman-andre-oort_vi.mp4` | `02_14_Tsimerman_Arithmetic` |
| `wang_kakeya.py` | `WangKakeya` | `wang-kakeya-3d_vi.mp4` | `02_15_Wang_Harmonic_Analysis` |
| `wang_restriction.py` | `WangRestriction` | `wang-fourier-restriction_vi.mp4` | `02_15_Wang_Harmonic_Analysis` |
| `avila_renormalization.py` | `AvilaRenormalization` | `avila-renormalization-dynamics_vi.mp4` | `02_16_Avila_Dynamics` |
| `avila_cocycles.py` | `AvilaCocycles` | `avila-cocycles-martini_vi.mp4` | `02_16_Avila_Dynamics` |
| `bhargava_cubes.py` | `BhargavaCubes` | `bhargava-cubes-composition_vi.mp4` | `02_17_Bhargava_Composition` |
| `bhargava_elliptic.py` | `BhargavaElliptic` | `bhargava-elliptic-rank_vi.mp4` | `02_17_Bhargava_Composition` |
| `deligne_weil.py` | `DeligneWeil` | `deligne-weil-conjectures_vi.mp4` | `02_18_Deligne_Weil` |
| `deligne_etale.py` | `DeligneEtale` | `deligne-etale-weil2_vi.mp4` | `02_18_Deligne_Weil` |
| `duminil_ising.py` | `DuminilIsing` | `duminil-ising-3d-4d_vi.mp4` | `02_19_Duminil_Copin_Phase_Transitions` |
| `duminil_percolation.py` | `DuminilPercolation` | `duminil-percolation-saw_vi.mp4` | `02_19_Duminil_Copin_Phase_Transitions` |
| `figalli_monge_ampere.py` | `FigalliMongeAmpere` | `figalli-monge-ampere_vi.mp4` | `02_20_Figalli_Optimal_Transport` |
| `figalli_applications.py` | `FigalliApplications` | `figalli-applications-transport_vi.mp4` | `02_20_Figalli_Optimal_Transport` |
| `hairer_spde.py` | `HairerSPDE` | `hairer-regularity-structures_vi.mp4` | `02_21_Hairer_Regularity_Structures` |
| `hairer_paracontrol.py` | `HairerParacontrol` | `hairer-paracontrol-subcritical_vi.mp4` | `02_21_Hairer_Regularity_Structures` |
| `kontsevich_witten.py` | `KontsevichWitten` | `kontsevich-witten-knots_vi.mp4` | `02_22_Kontsevich_Quantization` |
| `kontsevich_formality.py` | `KontsevichFormality` | `kontsevich-formality-quantization_vi.mp4` | `02_22_Kontsevich_Quantization` |
| `lindenstrauss_rigidity.py` | `LindenstraussRigidity` | `lindenstrauss-measure-rigidity_vi.mp4` | `02_23_Lindenstrauss_Measure_Rigidity` |
| `lindenstrauss_que.py` | `LindenstraussQUE` | `lindenstrauss-arithmetic-que_vi.mp4` | `02_23_Lindenstrauss_Measure_Rigidity` |
| `lions_viscosity.py` | `LionsViscosity` | `lions-viscosity-solutions_vi.mp4` | `02_24_Lions_Viscosity` |
| `lions_boltzmann.py` | `LionsBoltzmann` | `lions-boltzmann-mfg_vi.mp4` | `02_24_Lions_Viscosity` |
| `mcmullen_dynamics.py` | `McMullenDynamics` | `mcmullen-mandelbrot-renorm_vi.mp4` | `02_25_McMullen_Dynamics` |
| `mcmullen_teichmuller.py` | `McMullenTeichmuller` | `mcmullen-bers-kra-cusp_vi.mp4` | `02_25_McMullen_Dynamics` |
| `mori_hartshorne.py` | `MoriHartshorne` | `mori-hartshorne-bend-break_vi.mp4` | `02_26_Mori_MMP` |
| `mori_mmp.py` | `MoriMMP` | `mori-3d-mmp-flip_vi.mp4` | `02_26_Mori_MMP` |
| `okounkov_plancherel.py` | `OkounkovPlancherel` | `okounkov-plancherel-young_vi.mp4` | `02_27_Okounkov_Representation` |
| `okounkov_bridges.py` | `OkounkovBridges` | `okounkov-fock-gw-instanton_vi.mp4` | `02_27_Okounkov_Representation` |
| `smirnov_percolation.py` | `SmirnovPercolation` | `smirnov-cardy-percolation_vi.mp4` | `02_28_Smirnov_Percolation` |
| `smirnov_ising.py` | `SmirnovIsing` | `smirnov-ising-fermion-sle_vi.mp4` | `02_28_Smirnov_Percolation` |
| `villani_landau.py` | `VillaniLandau` | `villani-landau-damping_vi.mp4` | `02_29_Villani_Landau_Boltzmann` |
| `villani_boltzmann.py` | `VillaniBoltzmann` | `villani-boltzmann-hypocoercivity_vi.mp4` | `02_29_Villani_Landau_Boltzmann` |
| `werner_sle.py` | `WernerSLE` | `werner-loewner-sle_vi.mp4` | `02_30_Werner_SLE` |
| `werner_brownian.py` | `WernerBrownian` | `werner-brownian-4-3_vi.mp4` | `02_30_Werner_SLE` |
| `zelmanov_burnside.py` | `ZelmanovBurnside` | `zelmanov-three-burnside-problems_vi.mp4` | `02_31_Zelmanov_Burnside` |
| `zelmanov_jordan.py` | `ZelmanovJordan` | `zelmanov-lie-jordan-proof_vi.mp4` | `02_31_Zelmanov_Burnside` |
| `donaldson_intersection.py` | `DonaldsonIntersection` | `donaldson-intersection-form-e8_vi.mp4` | `02_32_Donaldson_Four_Manifolds` |
| `donaldson_instanton.py` | `DonaldsonInstanton` | `donaldson-yang-mills-exotic-r4_vi.mp4` | `02_32_Donaldson_Four_Manifolds` |
