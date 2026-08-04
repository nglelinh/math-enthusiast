#!/usr/bin/env python3
"""Generate video-research packs and enrich Ch.07–09 EN+VI lessons (skip overviews)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "research" / "video-research"
DATE = "2026-08-04"

# ---------------------------------------------------------------------------
# Topic research data (5–12+ quality URLs each; Abel/Turing official hubs)
# ---------------------------------------------------------------------------

TOPICS: list[dict] = [
    # ========== CH 07 studios ==========
    {
        "slug": "explore-kakeya",
        "chapter": "07",
        "en": "07_02_Explore_Kakeya",
        "vi": "07_02_Explore_Kakeya",
        "title": "Exploration Studio: Kakeya sets",
        "kind": "studio",
        "parent": "Ch.1 Kakeya + Ch.2 Wang (Path A)",
        "knowledge_en": [
            "**Besicovitch set / Kakeya set:** unit segment in every direction; measure zero possible in the plane.",
            "**Davies (1971):** planar Kakeya sets have Hausdorff dimension 2 (measure zero ≠ dimension < 2).",
            "**Wang–Zahl (2025):** Kakeya set conjecture in dimension 3 — [arXiv:2502.17655](https://arxiv.org/abs/2502.17655).",
            "**Continuous needle motion** (arbitrarily small positive area) ≠ static measure-zero Besicovitch set.",
            "Studio moral: minimize with a frozen definition of “small”; log failures; never claim to have reproduced Wang–Zahl.",
        ],
        "knowledge_vi": [
            "**Tập Kakeya / Besicovitch:** đoạn đơn vị mọi hướng; diện tích 0 khả dĩ trên mặt phẳng.",
            "**Davies (1971):** dim_H = 2 trên mặt phẳng dù measure 0.",
            "**Wang–Zahl (2025):** conjecture Kakeya chiều 3 — arXiv:2502.17655.",
            "Chuyển động kim liên tục (diện tích dương tùy nhỏ) ≠ tập tĩnh measure 0.",
            "Studio: đóng băng định nghĩa “nhỏ”; ghi log; không nhận đã tái tạo Wang–Zahl.",
        ],
        "urls": [
            ("V", "ORIENTATION", "Quanta — Once-in-a-Century Proof: Kakeya", "https://www.youtube.com/watch?v=5J3tYU_-IZI"),
            ("V", "INTUITION", "Mathologer — Kakeya needle (squeegee)", "https://www.youtube.com/watch?v=IM-n9c-ARHU"),
            ("V", "FOUNDATION", "CHALK — What is Hausdorff Dimension?", "https://www.youtube.com/watch?v=LJcWhcM4okQ"),
            ("V", "FOUNDATION", "CHALK — Estimating Hausdorff dim / MDP", "https://www.youtube.com/watch?v=FQXbRGmAbUY"),
            ("V", "ORIENTATION", "Pham Manh Tuyen — Giả thuyết Kakeya (VI)", "https://www.youtube.com/watch?v=XUkfpgFakMQ"),
            ("V", "ORIENTATION", "TOÁN PRO — Phỏng đoán Kakeya (VI)", "https://www.youtube.com/watch?v=pxVMKoZsVc8"),
            ("P", "PAPER", "Wang–Zahl Kakeya 3D (arXiv)", "https://arxiv.org/abs/2502.17655"),
            ("P", "PAPER", "Wang–Zahl sticky Kakeya (arXiv)", "https://arxiv.org/abs/2210.09581"),
            ("W", "WEB", "Quanta article Kakeya 2025", "https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/"),
            ("W", "WEB", "Wikipedia — Kakeya set", "https://en.wikipedia.org/wiki/Kakeya_set"),
        ],
    },
    {
        "slug": "explore-sphere-packing",
        "chapter": "07",
        "en": "07_03_Explore_Sphere_Packing",
        "vi": "07_03_Explore_Sphere_Packing",
        "title": "Exploration Studio: Sphere packing",
        "kind": "studio",
        "parent": "Ch.2 Viazovska",
        "knowledge_en": [
            "**Density** is a limit of volume ratios in large regions; boundary effects matter in finite boxes.",
            "**Hexagonal packing** maximizes density in 2D (Thue / Hales line of results); Kepler conjecture (3D) settled by Hales.",
            "**Viazovska (2016+):** optimal packing in dimensions 8 (E₈) and 24 (Leech) via modular-form “magic functions” and Cohn–Elkies LP bounds.",
            "Fourier / linear-programming upper bounds can rule out denser packings without listing them.",
            "Studio: measure densities carefully; separate theorem / conjecture / numerical observation.",
        ],
        "knowledge_vi": [
            "**Mật độ** là giới hạn tỉ lệ thể tích; hiệu ứng biên quan trọng trong hộp hữu hạn.",
            "Xếp lục giác tối ưu 2D; Kepler 3D (Hales); **Viazovska** cho chiều 8 và 24.",
            "Chặn Fourier/LP (Cohn–Elkies) loại packing dày hơn mà không liệt kê hết.",
            "Studio: đo cẩn thận; tách định lý / conjecture / quan sát số.",
        ],
        "urls": [
            ("V", "CORE", "Viazovska — Einstein Lectures sphere packing", "https://www.youtube.com/watch?v=fH6KNlUJux0"),
            ("V", "CORE", "Viazovska — Sphere packing intro (ICMU)", "https://www.youtube.com/watch?v=VR3Ezxo5wo8"),
            ("V", "RESEARCH", "Viazovska — Simons Lecture Day 1 (MIT)", "https://www.youtube.com/watch?v=mf_XOB7594c"),
            ("V", "INTUITION", "Numberphile — Best Way to Pack Spheres", "https://www.youtube.com/watch?v=mceaM2_zQd8"),
            ("P", "PAPER", "Viazovska E8 packing (arXiv:1603.04246)", "https://arxiv.org/abs/1603.04246"),
            ("P", "PAPER", "Cohn et al. dimension 24 (arXiv:1603.06518)", "https://arxiv.org/abs/1603.06518"),
            ("P", "PAPER", "Cohn–Elkies LP bounds (arXiv survey lineage)", "https://arxiv.org/abs/math/0110009"),
            ("W", "WEB", "Quanta — Sphere packing higher dimensions", "https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/"),
            ("W", "WEB", "Quanta — Viazovska Fields profile", "https://www.quantamagazine.org/ukrainian-mathematician-maryna-viazovska-wins-fields-medal-20220705/"),
            ("W", "WEB", "Wikipedia — Sphere packing", "https://en.wikipedia.org/wiki/Sphere_packing"),
            ("W", "WEB", "Simons Foundation Fields video page (Viazovska)", "https://www.simonsfoundation.org/2022/07/05/fields-medal-video-maryna-viazovska/"),
        ],
    },
    {
        "slug": "explore-prime-predictability",
        "chapter": "07",
        "en": "07_04_Explore_Prime_Predictability",
        "vi": "07_04_Explore_Prime_Predictability",
        "title": "Exploration Studio: Prime predictability",
        "kind": "studio",
        "parent": "Ch.1 RH / twins · Ch.2 Green–Tao / Maynard",
        "knowledge_en": [
            "**PNT:** π(x) ~ x/log x — density law, not a “formula for the n-th prime.”",
            "**RH** refines error terms via zeros of ζ; open (as of 2026).",
            "**Twin primes / bounded gaps:** Zhang, Maynard, Polymath — finite gaps infinitely often; twin prime conjecture still open.",
            "**Green–Tao:** primes contain arbitrarily long arithmetic progressions.",
            "Studio: plot gaps and π(x); never confuse verification with proof.",
        ],
        "knowledge_vi": [
            "**PNT:** π(x) ~ x/log x.",
            "**RH** tinh chỉnh sai số qua zero ζ — còn mở (2026).",
            "Khe twin / bounded gaps: Zhang–Maynard–Polymath; twin conjecture vẫn mở.",
            "**Green–Tao:** AP nguyên tố dài tùy ý.",
            "Studio: vẽ gaps; không nhầm kiểm chứng với chứng minh.",
        ],
        "urls": [
            ("V", "ORIENTATION", "Quanta — Riemann Hypothesis Explained", "https://www.youtube.com/watch?v=zlm1aajH6gY"),
            ("V", "INTUITION", "Numberphile — Twin primes / prime gaps (search Numberphile primes)", "https://www.youtube.com/watch?v=QKHKD8bRAro"),
            ("V", "CORE", "Numberphile — Twin Prime Conjecture (Maynard)", "https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem"),
            ("P", "PAPER", "Green–Tao arXiv classic", "https://arxiv.org/abs/math/0404188"),
            ("P", "PAPER", "Maynard small gaps between primes", "https://arxiv.org/abs/1311.4600"),
            ("W", "WEB", "Quanta RH article hub", "https://www.quantamagazine.org/tag/riemann-hypothesis/"),
            ("W", "WEB", "Wikipedia — Prime number theorem", "https://en.wikipedia.org/wiki/Prime_number_theorem"),
            ("W", "WEB", "Wikipedia — Twin prime", "https://en.wikipedia.org/wiki/Twin_prime"),
            ("W", "WEB", "Wikipedia — Green–Tao theorem", "https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem"),
            ("W", "WEB", "Clay Math — Riemann Hypothesis", "https://www.claymath.org/millennium/riemann-hypothesis/"),
        ],
    },
    {
        "slug": "explore-randomness-order",
        "chapter": "07",
        "en": "07_05_Explore_Randomness_Order",
        "vi": "07_05_Explore_Randomness_Order",
        "title": "Exploration Studio: Randomness and order",
        "kind": "studio",
        "parent": "Green–Tao · probabilistic method · chaos lecture",
        "knowledge_en": [
            "**Pseudorandomness:** deterministic sets can statistically mimic random ones (and vice versa for structure).",
            "**Roth / Szemerédi:** dense sets contain arithmetic progressions; Green–Tao upgrades to primes.",
            "**Probabilistic method (Erdős):** existence via expectation without constructing.",
            "Randomness can **destroy** structure (sparse random sets) or **create** typicality (random graphs).",
            "Studio: simulate vs prove; label theorem / heuristic / simulation.",
        ],
        "knowledge_vi": [
            "Tập xác định có thể trông “ngẫu nhiên”; mật độ tạo AP (Roth/Szemerédi/Green–Tao).",
            "Phương pháp xác suất: tồn tại qua kì vọng.",
            "Studio: mô phỏng vs chứng minh; gắn nhãn.",
        ],
        "urls": [
            ("V", "ORIENTATION", "Quanta — P vs NP (structure vs search; complexity culture)", "https://www.youtube.com/watch?v=pQsdygaYcE4"),
            ("P", "PAPER", "Green–Tao (structure in primes)", "https://arxiv.org/abs/math/0404188"),
            ("P", "PAPER", "Tao blog / notes on Szemerédi (expository entry)", "https://terrytao.wordpress.com/tag/szemeredi-theorem/"),
            ("W", "WEB", "Wikipedia — Probabilistic method", "https://en.wikipedia.org/wiki/Probabilistic_method"),
            ("W", "WEB", "Wikipedia — Szemerédi's theorem", "https://en.wikipedia.org/wiki/Szemer%C3%A9di%27s_theorem"),
            ("W", "WEB", "Wikipedia — Roth's theorem", "https://en.wikipedia.org/wiki/Roth%27s_theorem"),
            ("W", "WEB", "Wikipedia — Pseudorandomness", "https://en.wikipedia.org/wiki/Pseudorandomness"),
            ("W", "WEB", "Alon–Spencer book info (probabilistic method)", "https://en.wikipedia.org/wiki/The_Probabilistic_Method"),
            ("W", "WEB", "Quanta — patterns in primes / structure", "https://www.quantamagazine.org/tag/number-theory/"),
        ],
    },
    {
        "slug": "explore-fourth-dimension",
        "chapter": "07",
        "en": "07_06_Explore_Fourth_Dimension",
        "vi": "07_06_Explore_Fourth_Dimension",
        "title": "Exploration Studio: Fourth dimension",
        "kind": "studio",
        "parent": "Sphere packing · geometry",
        "knowledge_en": [
            "Coordinates: a point in $$\\mathbb{R}^4$$ is $$(x_1,x_2,x_3,x_4)$$ — geometry is linear algebra + distance.",
            "**Tesseract / 4-cube** and **3-sphere $$S^3$$** are standard visualization anchors.",
            "Volume concentration and packing behave differently in high dimension (measure concentrates).",
            "Studio: compute volumes/projections; avoid sci-fi “time is the fourth dimension” as a definition of Euclidean $$\\mathbb{R}^4$$.",
        ],
        "knowledge_vi": [
            "Điểm $$\\mathbb{R}^4$$ là tọa độ bốn; tesseract và $$S^3$$ là neo hình học.",
            "Mật độ/packing khác biệt theo chiều; tránh định nghĩa “thời gian = chiều 4” cho Euclidean studio.",
        ],
        "urls": [
            ("V", "INTUITION", "Numberphile — Perfect Shapes in Higher Dimensions (packing link)", "https://www.youtube.com/watch?v=mceaM2_zQd8"),
            ("V", "CORE", "Viazovska sphere packing (high-D density culture)", "https://www.youtube.com/watch?v=fH6KNlUJux0"),
            ("W", "WEB", "Wikipedia — Four-dimensional space", "https://en.wikipedia.org/wiki/Four-dimensional_space"),
            ("W", "WEB", "Wikipedia — Tesseract", "https://en.wikipedia.org/wiki/Tesseract"),
            ("W", "WEB", "Wikipedia — 3-sphere", "https://en.wikipedia.org/wiki/3-sphere"),
            ("W", "WEB", "Wikipedia — Hypersphere", "https://en.wikipedia.org/wiki/N-sphere"),
            ("P", "PAPER", "Viazovska E8 (high-D packing theorem)", "https://arxiv.org/abs/1603.04246"),
            ("W", "WEB", "3Blue1Brown essence of linear algebra (basis for coordinates)", "https://www.3blue1brown.com/topics/linear-algebra"),
            ("W", "WEB", "Quanta high-dimensional geometry tag", "https://www.quantamagazine.org/tag/geometry/"),
        ],
    },
    {
        "slug": "explore-map-colors",
        "chapter": "07",
        "en": "07_07_Explore_Map_Colors",
        "vi": "07_07_Explore_Map_Colors",
        "title": "Exploration Studio: Map colors (4CT)",
        "kind": "studio",
        "parent": "Ch.1 Four Color Theorem",
        "knowledge_en": [
            "**4CT:** every planar map is 4-colorable (Appel–Haken 1976; later simplifications / formal proofs).",
            "**Five-color theorem** has a short human proof; four requires reducibility + discharging + case check.",
            "Computer-assisted proof is still a proof if the method is finite and checkable in principle (Gonthier formalization culture).",
            "Studio: dual graphs, Kempe chains, attempt small reductions; discuss “what counts as proof.”",
        ],
        "knowledge_vi": [
            "**4CT:** bản đồ phẳng 4 màu (Appel–Haken 1976).",
            "Định lý 5 màu có chứng minh tay ngắn; 4 màu cần máy/case.",
            "Studio: đồ thị dual, Kempe; tranh luận “chứng minh là gì.”",
        ],
        "urls": [
            ("V", "ORIENTATION", "Numberphile — Four Color Map Theorem", "https://www.youtube.com/watch?v=NgbK43jB4rQ"),
            ("V", "INTUITION", "Numberphile — Four Color Theorem extra footage", "https://www.youtube.com/watch?v=laMkuPrad3s"),
            ("W", "WEB", "Wikipedia — Four color theorem", "https://en.wikipedia.org/wiki/Four_color_theorem"),
            ("W", "WEB", "Illinois Distributed Museum — 4CT", "https://distributedmuseum.illinois.edu/exhibit/four-color-theorem/"),
            ("W", "WEB", "Appel–Haken BAMS announcement (Euclid)", "https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-82/issue-5/Every-planar-map-is-four-colorable/bams/1183538218.full"),
            ("W", "WEB", "Celebratio — Haken four-color solution", "https://celebratio.org/Haken_W/article/794/"),
            ("W", "WEB", "Gonthier formal proof discussion (MathOverflow thread)", "https://mathoverflow.net/questions/44673/human-checkable-proof-of-the-four-color-theorem"),
            ("W", "WEB", "Wikipedia — Five color theorem", "https://en.wikipedia.org/wiki/Five_color_theorem"),
            ("W", "WEB", "Wikipedia — Graph coloring", "https://en.wikipedia.org/wiki/Graph_coloring"),
        ],
    },
    {
        "slug": "explore-describe-infinity",
        "chapter": "07",
        "en": "07_08_Explore_Describe_Infinity",
        "vi": "07_08_Explore_Describe_Infinity",
        "title": "Exploration Studio: Describing infinity",
        "kind": "studio",
        "parent": "Ch.4 / Ch.5 infinity & proofs culture",
        "knowledge_en": [
            "**Potential vs actual infinity:** process vs completed set.",
            "**Hilbert hotel:** countable infinity $$\\aleph_0$$ rebookings; bijections $$\\mathbb{N}\\leftrightarrow\\mathbb{Z}$$.",
            "**Cantor diagonal:** $$\\lvert\\mathbb{R}\\rvert > \\lvert\\mathbb{N}\\rvert$$; continuum size.",
            "**CH** independent of ZFC — not “open like RH.”",
            "Studio: write explicit bijections; separate paradox rhetoric from theorems.",
        ],
        "knowledge_vi": [
            "Vô hạn tiềm năng vs thực; hotel Hilbert; chéo Cantor; CH độc lập ZFC.",
            "Studio: song ánh tường minh; tách nghịch lý văn chương khỏi định lý.",
        ],
        "urls": [
            ("V", "ORIENTATION", "Numberphile — Infinity Paradoxes (Hilbert hotel)", "https://www.youtube.com/watch?v=dDl7g_2x74Q"),
            ("V", "FOUNDATION", "Wi-Phi / Rayo — Sizes of Infinity Part 1 (Hilbert)", "https://www.youtube.com/watch?v=p1KkXA0vKsQ"),
            ("V", "INTUITION", "Numberphile — Infinite hotel keys problem", "https://www.youtube.com/watch?v=uezOrcmHzrQ"),
            ("W", "WEB", "Khan Academy — Wi-Phi Hilbert hotel", "https://www.khanacademy.org/partner-content/wi-phi/wiphi-metaphysics-epistemology/wiphi-metaphysics/v/sizes-of-infinity-part-1-hilberts-hotel"),
            ("W", "WEB", "Wikipedia — Hilbert's paradox of the Grand Hotel", "https://en.wikipedia.org/wiki/Hilbert%27s_paradox_of_the_Grand_Hotel"),
            ("W", "WEB", "Wikipedia — Cantor's diagonal argument", "https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument"),
            ("W", "WEB", "Wikipedia — Continuum hypothesis", "https://en.wikipedia.org/wiki/Continuum_hypothesis"),
            ("W", "WEB", "Wikipedia — Cardinality", "https://en.wikipedia.org/wiki/Cardinality"),
            ("W", "WEB", "Stanford Encyclopedia — Continuum Hypothesis (survey)", "https://plato.stanford.edu/entries/continuum-hypothesis/"),
        ],
    },
    {
        "slug": "explore-iteration",
        "chapter": "07",
        "en": "07_09_Explore_Iteration",
        "vi": "07_09_Explore_Iteration",
        "title": "Exploration Studio: Iteration (Collatz)",
        "kind": "studio",
        "parent": "Ch.1 Collatz · pack collatz/",
        "reuse_pack": "collatz",
        "knowledge_en": [
            "Reuse full Collatz video pack: `research/video-research/collatz/`.",
            "**Tao 2019** almost-all / almost-bounded ≠ full Collatz (still **open** as of 2026).",
            "Freeze map $$T$$ vs Syracuse; log stopping times; computation ≠ proof.",
        ],
        "knowledge_vi": [
            "Dùng gói Collatz: `research/video-research/collatz/`.",
            "Tao 2019 almost-all ≠ giải Collatz (vẫn **mở** 2026).",
        ],
        "urls": [
            ("V", "ORIENTATION", "Veritasium — Collatz", "https://www.youtube.com/watch?v=094y1Z2wpJg"),
            ("V", "INTUITION", "Numberphile — UNCRACKABLE Collatz", "https://www.youtube.com/watch?v=5mFpVDpKX70"),
            ("V", "FOUNDATION", "Chamberland 3x+1 status Part 1", "https://www.youtube.com/watch?v=t1I9uHF9X5Y"),
            ("V", "CORE", "Tao Notorious Collatz (mathtube)", "https://mathtube.org/lecture/video/notorious-collatz-conjecture"),
            ("V", "CORE", "Tao Notorious Collatz (YouTube)", "https://www.youtube.com/watch?v=X2p5eMWyaFs"),
            ("V", "FRONTIER", "Tao IAS almost-all Collatz", "https://www.youtube.com/watch?v=k-dtx8s2ehM"),
            ("P", "PAPER", "Tao arXiv:1909.03562", "https://arxiv.org/abs/1909.03562"),
            ("P", "PAPER", "Lagarias overview arXiv:2111.02635", "https://arxiv.org/abs/2111.02635"),
            ("W", "WEB", "Full bibliography (pack)", "research/video-research/collatz/references.md"),
            ("W", "WEB", "Quanta Tao Collatz", "https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/"),
        ],
    },
    # ========== CH 08 Abel ==========
    {
        "slug": "what-is-abel-prize",
        "chapter": "08",
        "en": "08_02_What_Is_Abel_Prize",
        "vi": "08_02_Giai_Abel_la_gi",
        "title": "What is the Abel Prize?",
        "kind": "abel",
        "knowledge_en": [
            "Abel Prize: Norwegian Academy of Science and Letters; annual since 2003; no age limit; lifetime/body-of-work emphasis.",
            "Not a Nobel category — informal “Nobel of math” analogy only.",
            "Official hub: citations, biographies, Abel lectures on YouTube channel The Abel Prize.",
            "Contrast Fields (≤40, breakthrough snapshot) vs Abel (career climate).",
        ],
        "knowledge_vi": [
            "Giải Abel: Viện Hàn lâm Na Uy; từ 2003; không giới hạn tuổi; nhấn sự nghiệp/công cụ.",
            "Không phải hạng mục Nobel; so Fields (≤40) vs Abel (dài hạn).",
            "Cổng: abelprize.no.",
        ],
        "urls": [
            ("W", "OFFICIAL", "The Abel Prize home", "https://abelprize.no/"),
            ("W", "OFFICIAL", "Abel laureates list", "https://abelprize.no/winners"),
            ("W", "OFFICIAL", "Abel FAQ", "https://abelprize.no/page/faq-frequently-asked-questions"),
            ("W", "OFFICIAL", "Abel lectures events", "https://abelprize.no/events/abel-lectures-0"),
            ("V", "ORIENTATION", "Abel Prize YouTube channel", "https://www.youtube.com/channel/UCIJF5m5y70ZQoDCXVq0k50A"),
            ("W", "WEB", "Wikipedia — Abel Prize", "https://en.wikipedia.org/wiki/Abel_Prize"),
            ("W", "WEB", "Wikipedia — Niels Henrik Abel", "https://en.wikipedia.org/wiki/Niels_Henrik_Abel"),
            ("W", "WEB", "Wikipedia — Fields Medal (contrast)", "https://en.wikipedia.org/wiki/Fields_Medal"),
            ("W", "WEB", "Norwegian Academy of Science and Letters", "https://dnva.no/en"),
        ],
    },
    {
        "slug": "wiles-fermat",
        "chapter": "08",
        "en": "08_03_Wiles_Fermat",
        "vi": "08_03_Wiles_Fermat",
        "title": "Wiles: Modularity and FLT (Abel 2016)",
        "kind": "abel",
        "year": 2016,
        "knowledge_en": [
            "Abel 2016: Wiles for FLT via **semistable modularity** of elliptic curves over $$\\mathbb{Q}$$.",
            "Strategy slogan: Frey curve → Ribet (non-modular if counterexample) → Wiles modularity lifting → contradiction.",
            "Full modularity later: Breuil–Conrad–Diamond–Taylor; Abel wording carefully says semistable.",
            "Taylor–Wiles method repaired the original gap.",
        ],
        "knowledge_vi": [
            "Abel 2016: Wiles — FLT qua modularity **semistable**.",
            "Frey → Ribet → Wiles; Taylor–Wiles vá gap; full modularity sau (BCDT).",
        ],
        "urls": [
            ("W", "OFFICIAL", "Abel 2016 Wiles page", "https://abelprize.no/abel-prize-laureates/2016"),
            ("V", "CORE", "Wiles Abel lecture — FLT abelian/non-abelian", "https://www.youtube.com/watch?v=4t1mgEBx1nQ"),
            ("V", "CORE", "Darmon — Wiles' marvelous proof", "https://www.youtube.com/watch?v=oqMaziDIBYY"),
            ("V", "HISTORY", "Abel interview with Wiles", "https://www.youtube.com/watch?v=cWKAzX5U85Q"),
            ("V", "ORIENTATION", "Live interview Wiles (Oslo)", "https://www.youtube.com/watch?v=baUlp5EWhCk"),
            ("V", "ORIENTATION", "Alex Bellos on Wiles/FLT", "https://www.youtube.com/watch?v=2Pu4vZZu3JA"),
            ("V", "HISTORY", "INI — Thirty years of proof (Wiles anniversary)", "https://www.youtube.com/watch?v=nlUimyJpWtI"),
            ("W", "WEB", "Nature — Wiles Abel Prize", "https://www.nature.com/articles/nature.2016.19552"),
            ("W", "WEB", "Wikipedia — Wiles's proof of FLT", "https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem"),
            ("W", "WEB", "Wikipedia — Modularity theorem", "https://en.wikipedia.org/wiki/Modularity_theorem"),
        ],
    },
    {
        "slug": "uhlenbeck-gauge",
        "chapter": "08",
        "en": "08_04_Uhlenbeck_Gauge",
        "vi": "08_04_Uhlenbeck_Gauge",
        "title": "Uhlenbeck: Gauge theory analysis (Abel 2019)",
        "kind": "abel",
        "year": 2019,
        "knowledge_en": [
            "First woman Abel laureate (2019): geometric PDE, gauge theory, integrable systems.",
            "Key slogans: **bubbling**, removable singularities, compactness for Yang–Mills / harmonic maps.",
            "Infrastructure analysis enabling gauge-theoretic topology (Donaldson program culture).",
        ],
        "knowledge_vi": [
            "Abel 2019: Uhlenbeck — PDE hình học, gauge, bubbling / singularity.",
            "Nữ laureate đầu tiên; hạ tầng phân tích cho topology gauge.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Abel 2019 Uhlenbeck", "https://abelprize.no/abel-prize-laureates/2019"),
            ("V", "CORE", "Uhlenbeck Abel lecture — Calculus of Variations", "https://www.youtube.com/watch?v=1WepO8tFGto"),
            ("V", "CORE", "Bryant — Bubbles & singularities (on Uhlenbeck)", "https://www.youtube.com/watch?v=EZNpi8H6q1Q"),
            ("V", "ORIENTATION", "Abel Prize Interview Uhlenbeck", "https://www.youtube.com/watch?v=0fOaetX4eHM"),
            ("V", "ORIENTATION", "Live interview Uhlenbeck", "https://www.youtube.com/watch?v=mmWdPPwSi64"),
            ("V", "HISTORY", "Abel announcement 2019", "https://www.youtube.com/watch?v=arrl_nM0T4s"),
            ("W", "WEB", "Quanta — Uhlenbeck Abel", "https://www.quantamagazine.org/karen-uhlenbeck-uniter-of-geometry-and-analysis-wins-abel-prize-20190319/"),
            ("W", "WEB", "Celebratio Mathematica — Uhlenbeck", "https://celebratio.org/Uhlenbeck_K/cover/472/"),
            ("W", "WEB", "AMS Notices survey (Donaldson on Uhlenbeck PDF)", "https://www.ams.org/journals/notices/201903/rnoti-p303.pdf"),
            ("W", "WEB", "Wikipedia — Karen Uhlenbeck", "https://en.wikipedia.org/wiki/Karen_Uhlenbeck"),
        ],
    },
    {
        "slug": "furstenberg-margulis",
        "chapter": "08",
        "en": "08_05_Furstenberg_Margulis",
        "vi": "08_05_Furstenberg_Margulis",
        "title": "Furstenberg & Margulis: Dynamics for arithmetic (Abel 2020)",
        "kind": "abel",
        "year": 2020,
        "knowledge_en": [
            "Abel 2020: probability & dynamics methods in group theory, number theory, combinatorics.",
            "**Furstenberg:** multiple recurrence → structure in large sets (Szemerédi culture).",
            "**Margulis:** superrigidity, arithmeticity, expanders from groups, Oppenheim conjecture.",
            "Cultural message: ergodic theory as an engine for pure math.",
        ],
        "knowledge_vi": [
            "Abel 2020: động lực/xác suất → số học & tổ hợp.",
            "Furstenberg recurrence; Margulis superrigidity / expander / Oppenheim.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Abel 2020 Furstenberg & Margulis", "https://abelprize.no/abel-prize-laureates/2020"),
            ("V", "CORE", "Abel lectures 2020 Furstenberg & Margulis", "https://www.youtube.com/watch?v=2i5UJwKN7os"),
            ("V", "HISTORY", "Abel interview Furstenberg", "https://www.youtube.com/watch?v=01IdfSRYawE"),
            ("V", "HISTORY", "Abel interview Margulis", "https://www.youtube.com/watch?v=FInTu9-MHHU"),
            ("V", "ORIENTATION", "Popular presentation of 2020 work (Bellos clip)", "https://www.youtube.com/watch?v=Fqdl_jyw8OE"),
            ("V", "RELATED", "Margulis on Kolmogorov–Sinai entropy (earlier Abel week)", "https://www.youtube.com/watch?v=cuYO5NQieRA"),
            ("W", "WEB", "NYT Abel 2020", "https://www.nytimes.com/2020/03/18/science/abel-prize-mathematics.html"),
            ("W", "WEB", "Nature Abel 2020", "https://www.nature.com/articles/d41586-020-00799-7"),
            ("W", "WEB", "Wikipedia — Hillel Furstenberg", "https://en.wikipedia.org/wiki/Hillel_Furstenberg"),
            ("W", "WEB", "Wikipedia — Grigory Margulis", "https://en.wikipedia.org/wiki/Grigory_Margulis"),
        ],
    },
    {
        "slug": "lovasz-wigderson",
        "chapter": "08",
        "en": "08_06_Lovasz_Wigderson",
        "vi": "08_06_Lovasz_Wigderson",
        "title": "Lovász & Wigderson (Abel 2021)",
        "kind": "abel",
        "year": 2021,
        "knowledge_en": [
            "Abel 2021: foundational contributions to TCS and discrete math; shaping them into central modern mathematics.",
            "Lovász: graph theory, optimization, local lemma, geometric graph theory.",
            "Wigderson: randomness, complexity, expanders, proof systems — later **Turing Award 2023** (not 2021).",
            "Does **not** solve P vs NP.",
        ],
        "knowledge_vi": [
            "Abel 2021: Lovász + Wigderson — TCS & toán rời rạc trung tâm.",
            "Wigderson còn **Turing 2023** (không phải 2021).",
            "Không giải P vs NP.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Abel 2021 Lovász & Wigderson", "https://abelprize.no/abel-prize-laureates/2021"),
            ("V", "CORE", "Abel lectures Lovász & Wigderson", "https://www.youtube.com/watch?v=zqiL57ebP-k"),
            ("V", "HISTORY", "Abel interview Lovász & Wigderson", "https://www.youtube.com/watch?v=VAk0rtlKtMA"),
            ("V", "ORIENTATION", "WFSJ meet Lovász & Wigderson", "https://www.youtube.com/watch?v=J4yssMTZqC4"),
            ("V", "ORIENTATION", "Short interview Lovász", "https://www.youtube.com/watch?v=wg0di8dK0eI"),
            ("V", "ORIENTATION", "Short interview Wigderson", "https://www.youtube.com/watch?v=5VxOhzNv9To"),
            ("W", "WEB", "NYT Abel 2021", "https://www.nytimes.com/2021/03/17/science/abel-prize-mathematics.html"),
            ("W", "WEB", "Nature Abel 2021", "https://www.nature.com/articles/d41586-021-00694-9"),
            ("W", "CROSS", "ACM Turing — Wigderson 2023", "https://amturing.acm.org/award_winners/wigderson_3844537.cfm"),
            ("W", "WEB", "Wikipedia — Avi Wigderson", "https://en.wikipedia.org/wiki/Avi_Wigderson"),
        ],
    },
    {
        "slug": "sullivan-topology",
        "chapter": "08",
        "en": "08_07_Sullivan_Topology",
        "vi": "08_07_Sullivan_Topology",
        "title": "Sullivan: Topology & dynamics (Abel 2022)",
        "kind": "abel",
        "year": 2022,
        "knowledge_en": [
            "Abel 2022: topology in the broad sense — algebraic, geometric, dynamical.",
            "Highlights: rational homotopy / Sullivan models; **no wandering domains** for rational maps.",
            "Virtuoso career across topology and dynamics rather than a single theorem trophy.",
        ],
        "knowledge_vi": [
            "Abel 2022: topology rộng — đại số, hình học, động lực.",
            "No wandering domains; mô hình Sullivan; sự nghiệp virtuoso.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Abel 2022 Sullivan", "https://abelprize.no/abel-prize-laureates/2022"),
            ("V", "CORE", "Sullivan Abel lecture — Gathering chestnuts… fluid motion", "https://www.youtube.com/watch?v=RRMBRiyNcjI"),
            ("V", "ORIENTATION", "Abel Prize playlist Sullivan 2022", "https://www.youtube.com/playlist?list=PLKeZo7pFBx1sOsQMh_Nwr193fWCeeLjsw"),
            ("W", "WEB", "Wikipedia — Dennis Sullivan", "https://en.wikipedia.org/wiki/Dennis_Sullivan"),
            ("W", "WEB", "Wikipedia — No wandering domain theorem", "https://en.wikipedia.org/wiki/No_wandering_domain_theorem"),
            ("W", "WEB", "Wikipedia — Rational homotopy theory", "https://en.wikipedia.org/wiki/Rational_homotopy_theory"),
            ("W", "WEB", "Stony Brook / CUNY culture pages (search Sullivan Abel)", "https://www.stonybrook.edu/"),
            ("W", "WEB", "Abel popular PDF topology (from laureate page materials)", "https://abelprize.no/sites/default/files/2022-03/topolgy_eng.pdf"),
            ("W", "WEB", "Abel popular PDF no-wandering", "https://abelprize.no/sites/default/files/2022-03/wanderingset_eng.pdf"),
        ],
    },
    {
        "slug": "caffarelli-pde",
        "chapter": "08",
        "en": "08_08_Caffarelli_PDE",
        "vi": "08_08_Caffarelli_PDE",
        "title": "Caffarelli: Free boundaries & regularity (Abel 2023)",
        "kind": "abel",
        "year": 2023,
        "knowledge_en": [
            "Abel 2023: regularity for nonlinear PDE — free boundaries, Monge–Ampère.",
            "**Caffarelli–Kohn–Nirenberg** partial regularity for Navier–Stokes ≠ Clay Millennium solution.",
            "Obstacle problem as flagship free-boundary model.",
        ],
        "knowledge_vi": [
            "Abel 2023: chính quy PDE phi tuyến, free boundary, Monge–Ampère.",
            "CKN partial regularity NS ≠ giải Clay NS.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Abel 2023 Caffarelli", "https://abelprize.no/abel-prize-laureates/2023"),
            ("V", "CORE", "Caffarelli Abel lecture — non-linear surface structure", "https://www.youtube.com/watch?v=dVGX6QhO8rU"),
            ("V", "HISTORY", "Abel interview Caffarelli 2023", "https://www.youtube.com/watch?v=rz3uPOIL9AA"),
            ("V", "ORIENTATION", "Caffarelli short film", "https://www.youtube.com/watch?v=tdUBLu4fHbw"),
            ("V", "ORIENTATION", "Reaction to Abel Prize call", "https://www.youtube.com/watch?v=ze4SKx5yBFw"),
            ("W", "WEB", "Wikipedia — Luis Caffarelli", "https://en.wikipedia.org/wiki/Luis_Caffarelli"),
            ("W", "WEB", "Wikipedia — Free boundary problem", "https://en.wikipedia.org/wiki/Free_boundary_problem"),
            ("W", "WEB", "Wikipedia — Obstacle problem", "https://en.wikipedia.org/wiki/Obstacle_problem"),
            ("W", "WEB", "Clay — Navier–Stokes (contrast partial regularity)", "https://www.claymath.org/millennium/navier-stokes-equation/"),
            ("W", "WEB", "Abel popular PDFs (pde/obstacle/freeBoundary)", "https://abelprize.no/abel-prize-laureates/2023"),
        ],
    },
    {
        "slug": "talagrand-probability",
        "chapter": "08",
        "en": "08_09_Talagrand_Probability",
        "vi": "08_09_Talagrand_Probability",
        "title": "Talagrand: Concentration & spin glasses (Abel 2024)",
        "kind": "abel",
        "year": 2024,
        "knowledge_en": [
            "Abel 2024: probability, functional analysis — concentration of measure, generic chaining, spin glasses.",
            "**Concentration:** high-dimensional measures are tightly concentrated; Lipschitz functions nearly constant.",
            "Chaining controls suprema of stochastic processes.",
        ],
        "knowledge_vi": [
            "Abel 2024: Talagrand — concentration, chaining, spin glass.",
            "Độ đo cao chiều tập trung; chaining khống chế supremum quá trình ngẫu nhiên.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Abel 2024 Talagrand", "https://abelprize.no/abel-prize-laureates/2024"),
            ("V", "CORE", "Talagrand Abel lecture — Chaining: a long story", "https://www.youtube.com/watch?v=3yIwl6XC0xA"),
            ("V", "CORE", "Assaf Naor — Talagrand almost everywhere", "https://www.youtube.com/watch?v=atrxvobEdOo"),
            ("V", "ORIENTATION", "Abel lectures 2024 playlist", "https://www.youtube.com/playlist?list=PLKeZo7pFBx1tm7M9d6KYBPcPuazokxqkm"),
            ("P", "PAPER", "Survey arXiv: Talagrand's journey to Abel 2024", "https://arxiv.org/abs/2410.07945"),
            ("W", "WEB", "Wikipedia — Michel Talagrand", "https://en.wikipedia.org/wiki/Michel_Talagrand"),
            ("W", "WEB", "Wikipedia — Concentration of measure", "https://en.wikipedia.org/wiki/Concentration_of_measure"),
            ("W", "WEB", "Wikipedia — Generic chaining", "https://en.wikipedia.org/wiki/Generic_chaining"),
            ("W", "WEB", "Abel popular — concentration PDF", "https://abelprize.no/sites/default/files/2024-03/Concentration%20of%20measure.pdf"),
        ],
    },
    {
        "slug": "kashiwara-dmodules",
        "chapter": "08",
        "en": "08_10_Kashiwara_DModules",
        "vi": "08_10_Kashiwara_DModules",
        "title": "Kashiwara: D-modules & crystals (Abel 2025)",
        "kind": "abel",
        "year": 2025,
        "knowledge_en": [
            "Abel 2025: algebraic analysis & representation theory — **D-modules**, crystal bases/graphs.",
            "D-modules: algebraic language for systems of linear PDEs (Sato school / microlocal analysis).",
            "Crystal bases: combinatorial skeletons of representations (quantum groups culture).",
        ],
        "knowledge_vi": [
            "Abel 2025: Kashiwara — D-module, crystal bases.",
            "Phân tích đại số PDE tuyến tính; biểu diễn lượng tử tổ hợp.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Abel 2025 Kashiwara", "https://abelprize.no/abel-prize-laureates/2025"),
            ("W", "OFFICIAL", "Announcement article 2025", "https://abelprize.no/article/2025/japanese-mathematician-masaki-kashiwara-awarded-abel-prize-2025"),
            ("V", "CORE", "Abel Lectures 2025 playlist", "https://www.youtube.com/playlist?list=PLKeZo7pFBx1uGqwO463MpxuvxMpBCnddj"),
            ("V", "RELATED", "IHES related lectures playlist (Kashiwara events)", "https://www.youtube.com/playlist?list=PLx5f8IelFRgEe8LACp8Pt3ijJb6PLIbgC"),
            ("W", "WEB", "IHES news Kashiwara Abel", "https://www.ihes.fr/en/abel-prize-2025/"),
            ("W", "WEB", "Wikipedia — Masaki Kashiwara", "https://en.wikipedia.org/wiki/Masaki_Kashiwara"),
            ("W", "WEB", "Wikipedia — D-module", "https://en.wikipedia.org/wiki/D-module"),
            ("W", "WEB", "Wikipedia — Crystal base", "https://en.wikipedia.org/wiki/Crystal_base"),
            ("W", "WEB", "Abel popular — crystal bases PDF", "https://abelprize.no/sites/default/files/2025-03/krystallENG.pdf"),
            ("W", "WEB", "Abel glimpse PDF Kashiwara", "https://abelprize.no/sites/default/files/2025-03/MasakiKashiwara_s_work_for_non_mathematicians_AbelPrize_2025.pdf"),
        ],
    },
    # ========== CH 09 Turing ==========
    {
        "slug": "what-is-turing-award",
        "chapter": "09",
        "en": "09_02_What_Is_Turing_Award",
        "vi": "09_02_What_Is_Turing_Award",
        "title": "What is the Turing Award?",
        "kind": "turing",
        "knowledge_en": [
            "ACM A.M. Turing Award: highest distinction in computing; often called “Nobel of computing.”",
            "Named after Alan Turing; administered by ACM; $1M prize (Google support historically).",
            "Contrast Fields / Abel (math) vs Turing (computing) — overlapping people (e.g. Wigderson Abel+Turing).",
            "Official: amturing.acm.org",
        ],
        "knowledge_vi": [
            "Turing Award ACM: vinh dự cao nhất tin học; amturing.acm.org.",
            "So Fields/Abel; một số người nhận cả hai (Wigderson).",
        ],
        "urls": [
            ("W", "OFFICIAL", "ACM A.M. Turing Award home", "https://amturing.acm.org/"),
            ("W", "OFFICIAL", "Winners by year", "https://amturing.acm.org/byyear.cfm"),
            ("W", "OFFICIAL", "Alphabetical listing", "https://amturing.acm.org/alphabetical.cfm"),
            ("W", "WEB", "ACM about the award", "https://www.acm.org/about-acm/acm-history/acm-awards/turing-award"),
            ("W", "WEB", "Wikipedia — Turing Award", "https://en.wikipedia.org/wiki/Turing_Award"),
            ("W", "WEB", "Wikipedia — Alan Turing", "https://en.wikipedia.org/wiki/Alan_Turing"),
            ("W", "WEB", "Wikipedia — Association for Computing Machinery", "https://en.wikipedia.org/wiki/Association_for_Computing_Machinery"),
            ("V", "ORIENTATION", "ACM Turing Award lectures playlist", "https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6"),
            ("W", "CROSS", "Abel Prize (contrast)", "https://abelprize.no/"),
        ],
    },
    {
        "slug": "turing-computability",
        "chapter": "09",
        "en": "09_03_Turing_Computability",
        "vi": "09_03_Turing_Computability",
        "title": "Turing: Computability and undecidability",
        "kind": "turing",
        "knowledge_en": [
            "**Turing machine** as a model of effective computation; Church–Turing thesis (informal).",
            "**Halting problem** undecidable; Entscheidungsproblem negative solution.",
            "Undecidability ≠ “we haven't found an algorithm yet” — proven impossibility within the model.",
        ],
        "knowledge_vi": [
            "Máy Turing; bài toán dừng không quyết định được; Entscheidungsproblem.",
            "Không quyết định được ≠ “chưa tìm ra thuật toán.”",
        ],
        "urls": [
            ("W", "WEB", "Wikipedia — Turing machine", "https://en.wikipedia.org/wiki/Turing_machine"),
            ("W", "WEB", "Wikipedia — Halting problem", "https://en.wikipedia.org/wiki/Halting_problem"),
            ("W", "WEB", "Wikipedia — Church–Turing thesis", "https://en.wikipedia.org/wiki/Church%E2%80%93Turing_thesis"),
            ("W", "WEB", "Wikipedia — Entscheidungsproblem", "https://en.wikipedia.org/wiki/Entscheidungsproblem"),
            ("W", "WEB", "SEP — Turing machines", "https://plato.stanford.edu/entries/turing-machine/"),
            ("W", "WEB", "SEP — Computability and complexity", "https://plato.stanford.edu/entries/computability/"),
            ("W", "WEB", "Turing's 1936 paper (archive culture)", "https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf"),
            ("W", "OFFICIAL", "amturing.acm.org (award named for Turing)", "https://amturing.acm.org/"),
            ("V", "ORIENTATION", "Computerphile / Numberphile culture: search Turing halting", "https://www.youtube.com/watch?v=macM_MtS_w4"),
        ],
    },
    {
        "slug": "cook-karp-np",
        "chapter": "09",
        "en": "09_04_Cook_Karp_NP",
        "vi": "09_04_Cook_Karp_NP",
        "title": "Cook & Karp: NP-completeness",
        "kind": "turing",
        "knowledge_en": [
            "Cook (1982 Turing): Cook–Levin — SAT is NP-complete.",
            "Karp (1985 Turing): polynomial reductions; 21 NP-complete problems zoo.",
            "P vs NP open (Clay Millennium); reductions transfer hardness.",
            "Cross: Quanta P vs NP video on Ch.1.",
        ],
        "knowledge_vi": [
            "Cook–Levin SAT NP-complete; Karp zoo; P vs NP mở.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Cook Turing page", "https://amturing.acm.org/award_winners/cook_n991950.cfm"),
            ("W", "OFFICIAL", "Karp Turing page", "https://amturing.acm.org/award_winners/karp_3256708.cfm"),
            ("V", "ORIENTATION", "Quanta — Biggest Puzzle: P vs NP", "https://www.youtube.com/watch?v=pQsdygaYcE4"),
            ("V", "ORIENTATION", "Cook clip — why P=NP matters", "https://www.youtube.com/watch?v=4rzstuDyVGA"),
            ("V", "RELATED", "Cook lecture Techfest limits of computers", "https://www.youtube.com/watch?v=UulagVcxuo4"),
            ("W", "WEB", "Clay — P vs NP", "https://www.claymath.org/millennium/p-vs-np/"),
            ("W", "WEB", "Wikipedia — Cook–Levin theorem", "https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem"),
            ("W", "WEB", "Wikipedia — Karp's 21 NP-complete problems", "https://en.wikipedia.org/wiki/Karp%27s_21_NP-complete_problems"),
            ("W", "WEB", "Wikipedia — NP-completeness", "https://en.wikipedia.org/wiki/NP-completeness"),
            ("W", "WEB", "Cook interview (amturing)", "https://amturing.acm.org/interviews/cook_n991950.cfm"),
        ],
    },
    {
        "slug": "knuth-algorithms",
        "chapter": "09",
        "en": "09_05_Knuth_Algorithms",
        "vi": "09_05_Knuth_Algorithms",
        "title": "Knuth: Analysis of algorithms",
        "kind": "turing",
        "knowledge_en": [
            "Knuth Turing 1974: analysis of algorithms; *The Art of Computer Programming*; TeX.",
            "Literate programming; rigorous average/worst-case analysis culture.",
            "Algorithms as mathematical objects with exact counts, not only asymptotics.",
        ],
        "knowledge_vi": [
            "Knuth Turing 1974: phân tích thuật toán; TAOCP; TeX.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Knuth Turing page", "https://amturing.acm.org/award_winners/knuth_1013846.cfm"),
            ("W", "WEB", "Wikipedia — Donald Knuth", "https://en.wikipedia.org/wiki/Donald_Knuth"),
            ("W", "WEB", "Wikipedia — The Art of Computer Programming", "https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming"),
            ("W", "WEB", "Wikipedia — Analysis of algorithms", "https://en.wikipedia.org/wiki/Analysis_of_algorithms"),
            ("W", "WEB", "Knuth home (Stanford)", "https://www-cs-faculty.stanford.edu/~knuth/"),
            ("W", "WEB", "Wikipedia — TeX", "https://en.wikipedia.org/wiki/TeX"),
            ("W", "WEB", "Wikipedia — Literate programming", "https://en.wikipedia.org/wiki/Literate_programming"),
            ("V", "ORIENTATION", "YouTube search: Knuth Christmas tree lecture / interviews", "https://www.youtube.com/watch?v=PUJ_XdmSDZw"),
            ("W", "WEB", "ACM DL Knuth materials", "https://dl.acm.org/"),
        ],
    },
    {
        "slug": "public-key-crypto",
        "chapter": "09",
        "en": "09_06_Public_Key_Crypto",
        "vi": "09_06_Public_Key_Crypto",
        "title": "Public-key cryptography (Diffie–Hellman, Rivest–Shamir–Adleman)",
        "kind": "turing",
        "knowledge_en": [
            "Diffie–Hellman (2015 Turing): public-key exchange; discrete log hardness culture.",
            "Rivest–Shamir–Adleman (2002 Turing): RSA — factoring-based public-key encryption/signatures.",
            "Asymmetry: easy forward operations vs hard inverses without trapdoor knowledge.",
            "Cross-link Ch.3 crypto applications.",
        ],
        "knowledge_vi": [
            "Diffie–Hellman 2015; RSA 2002; khóa công khai.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Diffie Turing", "https://amturing.acm.org/award_winners/diffie_8371646.cfm"),
            ("W", "OFFICIAL", "Hellman Turing", "https://amturing.acm.org/award_winners/hellman_4055781.cfm"),
            ("W", "OFFICIAL", "Rivest Turing", "https://amturing.acm.org/award_winners/rivest_1562803.cfm"),
            ("W", "OFFICIAL", "Shamir Turing", "https://amturing.acm.org/award_winners/shamir_2327856.cfm"),
            ("W", "OFFICIAL", "Adleman Turing", "https://amturing.acm.org/award_winners/adleman_7308544.cfm"),
            ("W", "WEB", "Wikipedia — Public-key cryptography", "https://en.wikipedia.org/wiki/Public-key_cryptography"),
            ("W", "WEB", "Wikipedia — Diffie–Hellman key exchange", "https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange"),
            ("W", "WEB", "Wikipedia — RSA (cryptosystem)", "https://en.wikipedia.org/wiki/RSA_(cryptosystem)"),
            ("W", "WEB", "Original DH paper culture (IEEE)", "https://ee.stanford.edu/~hellman/publications/24.pdf"),
        ],
    },
    {
        "slug": "goldwasser-micali",
        "chapter": "09",
        "en": "09_07_Goldwasser_Micali",
        "vi": "09_07_Goldwasser_Micali",
        "title": "Goldwasser–Micali: Crypto foundations / ZK culture",
        "kind": "turing",
        "knowledge_en": [
            "Turing 2012: probabilistic encryption, semantic security, zero-knowledge proofs culture.",
            "Proofs as interactive protocols with soundness/completeness error.",
            "Connects to Wigderson interactive proofs / complexity.",
        ],
        "knowledge_vi": [
            "Turing 2012 Goldwasser–Micali: mã hóa xác suất, zero-knowledge.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Goldwasser Turing", "https://amturing.acm.org/award_winners/goldwasser_8627889.cfm"),
            ("W", "OFFICIAL", "Micali Turing", "https://amturing.acm.org/award_winners/micali_9954407.cfm"),
            ("W", "WEB", "Wikipedia — Shafi Goldwasser", "https://en.wikipedia.org/wiki/Shafi_Goldwasser"),
            ("W", "WEB", "Wikipedia — Silvio Micali", "https://en.wikipedia.org/wiki/Silvio_Micali"),
            ("W", "WEB", "Wikipedia — Zero-knowledge proof", "https://en.wikipedia.org/wiki/Zero-knowledge_proof"),
            ("W", "WEB", "Wikipedia — Semantic security", "https://en.wikipedia.org/wiki/Semantic_security"),
            ("W", "WEB", "Wikipedia — Goldwasser–Micali cryptosystem", "https://en.wikipedia.org/wiki/Goldwasser%E2%80%93Micali_cryptosystem"),
            ("W", "CROSS", "Wigderson Turing 2023 (proof systems culture)", "https://amturing.acm.org/award_winners/wigderson_3844537.cfm"),
            ("W", "WEB", "ACM announcement culture 2012", "https://awards.acm.org/about/2012-turing"),
        ],
    },
    {
        "slug": "yao-complexity",
        "chapter": "09",
        "en": "09_08_Yao_Complexity",
        "vi": "09_08_Yao_Complexity",
        "title": "Yao: Communication complexity & minimax",
        "kind": "turing",
        "knowledge_en": [
            "Yao Turing 2000: theory of computation — communication complexity, pseudorandomness, quantum computing foundations culture.",
            "**Yao's minimax principle** for randomized algorithms / distributional complexity.",
            "Communication complexity as a resource theory (bits exchanged).",
        ],
        "knowledge_vi": [
            "Yao Turing 2000: communication complexity, minimax, PRG/quantum culture.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Yao Turing page", "https://amturing.acm.org/award_winners/yao_1611524.cfm"),
            ("W", "WEB", "Wikipedia — Andrew Yao", "https://en.wikipedia.org/wiki/Andrew_Yao"),
            ("W", "WEB", "Wikipedia — Communication complexity", "https://en.wikipedia.org/wiki/Communication_complexity"),
            ("W", "WEB", "Wikipedia — Yao's principle", "https://en.wikipedia.org/wiki/Yao%27s_principle"),
            ("W", "WEB", "Wikipedia — Pseudorandom generator", "https://en.wikipedia.org/wiki/Pseudorandom_generator"),
            ("W", "WEB", "Yao class / IIIS Tsinghua culture", "https://iiis.tsinghua.edu.cn/en/"),
            ("W", "CROSS", "Wigderson randomness (related resource theory)", "https://amturing.acm.org/award_winners/wigderson_3844537.cfm"),
            ("W", "WEB", "Survey entry: Kushilevitz–Nisan book culture", "https://en.wikipedia.org/wiki/Communication_complexity"),
        ],
    },
    {
        "slug": "valiant-learning",
        "chapter": "09",
        "en": "09_09_Valiant_Learning",
        "vi": "09_09_Valiant_Learning",
        "title": "Valiant: Computational learning theory",
        "kind": "turing",
        "knowledge_en": [
            "Valiant Turing 2010: **PAC learning** — Probably Approximately Correct framework.",
            "Learning as a computational complexity problem (sample + time resources).",
            "Bridge to modern ML theory; not a claim that deep learning is “solved.”",
        ],
        "knowledge_vi": [
            "Valiant Turing 2010: PAC learning — học như bài toán độ phức tạp.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Valiant Turing page", "https://amturing.acm.org/award_winners/valiant_2612174.cfm"),
            ("W", "WEB", "Wikipedia — Leslie Valiant", "https://en.wikipedia.org/wiki/Leslie_Valiant"),
            ("W", "WEB", "Wikipedia — Probably approximately correct learning", "https://en.wikipedia.org/wiki/Probably_approximately_correct_learning"),
            ("W", "WEB", "Wikipedia — Computational learning theory", "https://en.wikipedia.org/wiki/Computational_learning_theory"),
            ("W", "WEB", "Valiant PAC paper culture (CACM / JACM lineage)", "https://dl.acm.org/doi/10.1145/1968.1972"),
            ("W", "CROSS", "Deep Learning Trio Turing 2018", "https://amturing.acm.org/award_winners/hinton_4791679.cfm"),
            ("W", "WEB", "Wikipedia — VC dimension (related theory)", "https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension"),
            ("W", "WEB", "ACM awards page Valiant", "https://awards.acm.org/award-recipients/valiant_2612174"),
        ],
    },
    {
        "slug": "hopcroft-tarjan",
        "chapter": "09",
        "en": "09_10_Hopcroft_Tarjan",
        "vi": "09_10_Hopcroft_Tarjan",
        "title": "Hopcroft–Tarjan: Algorithmic graph theory",
        "kind": "turing",
        "knowledge_en": [
            "Hopcroft (1986) & Tarjan (1986) Turing: fundamental algorithms / data structures for graphs.",
            "Planarity testing, connectivity, DFS-based algorithms, amortized analysis culture (Tarjan).",
            "Graph algorithms as discrete mathematics + rigorous implementation analysis.",
        ],
        "knowledge_vi": [
            "Hopcroft & Tarjan Turing 1986: thuật toán đồ thị nền tảng.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Hopcroft Turing", "https://amturing.acm.org/award_winners/hopcroft_1053917.cfm"),
            ("W", "OFFICIAL", "Tarjan Turing", "https://amturing.acm.org/award_winners/tarjan_1092048.cfm"),
            ("W", "WEB", "Wikipedia — John Hopcroft", "https://en.wikipedia.org/wiki/John_Hopcroft"),
            ("W", "WEB", "Wikipedia — Robert Tarjan", "https://en.wikipedia.org/wiki/Robert_Tarjan"),
            ("W", "WEB", "Wikipedia — Hopcroft–Tarjan algorithm (planarity)", "https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Tarjan_planarity_test"),
            ("W", "WEB", "Wikipedia — Depth-first search", "https://en.wikipedia.org/wiki/Depth-first_search"),
            ("W", "WEB", "Wikipedia — Union–find / disjoint set (Tarjan)", "https://en.wikipedia.org/wiki/Disjoint-set_data_structure"),
            ("W", "WEB", "Hopcroft–Ullman automata book culture", "https://en.wikipedia.org/wiki/Introduction_to_Automata_Theory,_Languages,_and_Computation"),
        ],
    },
    {
        "slug": "pearl-causality",
        "chapter": "09",
        "en": "09_11_Pearl_Causality",
        "vi": "09_11_Pearl_Causality",
        "title": "Pearl: Causality",
        "kind": "turing",
        "knowledge_en": [
            "Pearl Turing 2011: probabilistic and causal reasoning — Bayesian networks, do-calculus.",
            "Correlation ≠ causation; formal language for interventions and counterfactuals.",
            "Impact on AI, statistics, epidemiology, social science methodology.",
        ],
        "knowledge_vi": [
            "Pearl Turing 2011: nhân quả, Bayesian nets, do-calculus.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Pearl Turing page", "https://amturing.acm.org/award_winners/pearl_2658896.cfm"),
            ("W", "WEB", "Wikipedia — Judea Pearl", "https://en.wikipedia.org/wiki/Judea_Pearl"),
            ("W", "WEB", "Wikipedia — Causal model", "https://en.wikipedia.org/wiki/Causal_model"),
            ("W", "WEB", "Wikipedia — Bayesian network", "https://en.wikipedia.org/wiki/Bayesian_network"),
            ("W", "WEB", "Wikipedia — Do-calculus", "https://en.wikipedia.org/wiki/Do_calculus"),
            ("W", "WEB", "Book of Why (popular entry)", "https://en.wikipedia.org/wiki/The_Book_of_Why"),
            ("W", "WEB", "UCLA Cognitive Systems Lab (Pearl)", "http://bayes.cs.ucla.edu/jp_home.html"),
            ("V", "ORIENTATION", "YouTube search: Pearl causality Turing", "https://www.youtube.com/watch?v=iNm4nFBFmvo"),
        ],
    },
    {
        "slug": "deep-learning-trio",
        "chapter": "09",
        "en": "09_12_Deep_Learning_Trio",
        "vi": "09_12_Deep_Learning_Trio",
        "title": "Bengio–Hinton–LeCun: Deep learning (Turing 2018)",
        "kind": "turing",
        "knowledge_en": [
            "Turing 2018: conceptual and engineering foundations of deep neural networks.",
            "Backprop culture, CNNs (LeCun), deep belief / representation learning (Hinton), sequence/attention lineage (Bengio school).",
            "Not a mathematical completeness theorem for AI; empirical + theoretical research program.",
            "Hinton later Nobel Physics 2024 (separate honor).",
        ],
        "knowledge_vi": [
            "Turing 2018: Bengio–Hinton–LeCun — deep learning foundations.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Hinton Turing", "https://amturing.acm.org/award_winners/hinton_4791679.cfm"),
            ("W", "OFFICIAL", "LeCun Turing", "https://amturing.acm.org/award_winners/lecun_6017366.cfm"),
            ("W", "OFFICIAL", "Bengio Turing", "https://amturing.acm.org/award_winners/bengio_3406375.cfm"),
            ("W", "WEB", "ACM 2018 Turing announcement", "https://awards.acm.org/about/2018-turing"),
            ("W", "WEB", "Wikipedia — Deep learning", "https://en.wikipedia.org/wiki/Deep_learning"),
            ("W", "WEB", "Wikipedia — Backpropagation", "https://en.wikipedia.org/wiki/Backpropagation"),
            ("W", "WEB", "Wikipedia — Convolutional neural network", "https://en.wikipedia.org/wiki/Convolutional_neural_network"),
            ("W", "CROSS", "Valiant PAC (learning theory ancestor)", "https://amturing.acm.org/award_winners/valiant_2612174.cfm"),
            ("W", "WEB", "Course cross: Ch.6 Math of AI", "contents/en/chapter06/"),
        ],
    },
    {
        "slug": "wigderson-complexity",
        "chapter": "09",
        "en": "09_13_Wigderson_Complexity",
        "vi": "09_13_Wigderson_Complexity",
        "title": "Wigderson: Randomness & complexity (Turing 2023)",
        "kind": "turing",
        "knowledge_en": [
            "**Turing Award year is 2023** (not 2021). Abel with Lovász was **2021**.",
            "Randomness as resource; hardness↔randomness; expanders; interactive proofs culture.",
            "Book *Mathematics and Computation*; dual Abel+Turing pedagogy.",
        ],
        "knowledge_vi": [
            "**Turing 2023** (không 2021); Abel 2021 chung Lovász.",
            "Ngẫu nhiên–hardness; expander; IP.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Wigderson Turing 2023 page", "https://amturing.acm.org/award_winners/wigderson_3844537.cfm"),
            ("W", "OFFICIAL", "Wigderson Turing lecture page", "https://amturing.acm.org/vp/wigderson_3844537.cfm"),
            ("V", "CORE", "Wigderson Turing Award Lecture (ACM)", "https://www.youtube.com/watch?v=f2NiGO8zC1c"),
            ("V", "ORIENTATION", "IAS Q&A Wigderson Turing", "https://www.youtube.com/watch?v=TK_vD-VnsFw"),
            ("V", "ORIENTATION", "CACM June 2024 Wigderson feature", "https://www.youtube.com/watch?v=Ur9XNF6TeYw"),
            ("V", "RELATED", "Wigderson — Reading Alan Turing (Berkeley)", "https://www.youtube.com/watch?v=BiFSUniv70c"),
            ("W", "CROSS", "Abel 2021 Lovász & Wigderson", "https://abelprize.no/abel-prize-laureates/2021"),
            ("V", "CROSS", "Abel lectures Lovász & Wigderson", "https://www.youtube.com/watch?v=zqiL57ebP-k"),
            ("W", "WEB", "Wikipedia — Avi Wigderson", "https://en.wikipedia.org/wiki/Avi_Wigderson"),
            ("W", "WEB", "byyear listing (confirm 2023)", "https://amturing.acm.org/byyear.cfm"),
            ("W", "WEB", "Mathematics and Computation (book info)", "https://www.math.ias.edu/avi/book"),
        ],
    },
    {
        "slug": "modern-themes",
        "chapter": "09",
        "en": "09_14_Modern_Themes",
        "vi": "09_14_Modern_Themes",
        "title": "Modern themes at the math–CS border",
        "kind": "turing",
        "knowledge_en": [
            "Survey hub: complexity, crypto, learning, causality, randomness, algorithms.",
            "Recent Turing themes include quantum information (e.g. 2025 Bennett–Brassard announcement culture).",
            "Use official by-year list to update seminar readings each year.",
        ],
        "knowledge_vi": [
            "Tổng quan biên toán–CS; cập nhật amturing.acm.org/byyear mỗi năm.",
        ],
        "urls": [
            ("W", "OFFICIAL", "Turing winners by year", "https://amturing.acm.org/byyear.cfm"),
            ("W", "OFFICIAL", "Turing Award home", "https://amturing.acm.org/"),
            ("W", "OFFICIAL", "Wigderson 2023 (randomness)", "https://amturing.acm.org/award_winners/wigderson_3844537.cfm"),
            ("W", "OFFICIAL", "Deep learning 2018 trio hub via Hinton", "https://amturing.acm.org/award_winners/hinton_4791679.cfm"),
            ("W", "OFFICIAL", "Goldwasser 2012", "https://amturing.acm.org/award_winners/goldwasser_8627889.cfm"),
            ("V", "ORIENTATION", "Quanta P vs NP", "https://www.youtube.com/watch?v=pQsdygaYcE4"),
            ("W", "CROSS", "Abel Prize (math lifetime contrast)", "https://abelprize.no/"),
            ("W", "WEB", "Clay Millennium problems", "https://www.claymath.org/millennium-problems/"),
            ("W", "WEB", "Wikipedia — Theoretical computer science", "https://en.wikipedia.org/wiki/Theoretical_computer_science"),
            ("W", "WEB", "ACM Turing lectures playlist", "https://www.youtube.com/playlist?list=PLn0nrSd4xjjYCkOxtYqozyDuwt-4sC2L6"),
        ],
    },
]


def find_post(lang: str, chapter: str, key: str) -> Path:
    d = ROOT / "contents" / lang / f"chapter{chapter}" / "_posts"
    matches = list(d.glob(f"*{key}.md"))
    if not matches:
        raise FileNotFoundError(f"{lang} {key}")
    return matches[0]


def write_pack(t: dict) -> Path:
    """Write research pack unless reuse_pack points to existing collatz."""
    if t.get("reuse_pack"):
        # Only ensure a thin pointer README exists
        slug = t["slug"]
        p = PACK / slug
        p.mkdir(parents=True, exist_ok=True)
        (p / "README.md").write_text(
            f"""# {t['title']} — video research pack

**Date:** {DATE}  
**Primary pack:** [`../{t['reuse_pack']}/`](../{t['reuse_pack']}/) (full Collatz bibliography)

## Course pages

| Lang | Path |
|------|------|
| EN | `contents/en/chapter{t['chapter']}/_posts/*{t['en']}.md` |
| VI | `contents/vi/chapter{t['chapter']}/_posts/*{t['vi']}.md` |

## Learning path

Follow **`research/video-research/collatz/`** stages 0–3, then run the Ch.7 studio portfolio.

## Files

- This folder: studio pointer + lesson enrichment cross-links.
- Full URLs: [`../collatz/references.md`](../collatz/references.md)
- Analysis: [`../collatz/analysis.md`](../collatz/analysis.md)
- Learning path: [`../collatz/learning_path.md`](../collatz/learning_path.md)
""",
            encoding="utf-8",
        )
        # slim references pointing to collatz
        urls = t["urls"]
        lines = [
            f"# {t['title']} — URL bibliography\n",
            f"Primary complete list: `research/video-research/collatz/references.md`.\n",
            "Studio-facing subset:\n\n",
            "| # | Role | Title | URL |\n|---|------|-------|-----|\n",
        ]
        for i, (kind, role, title, url) in enumerate(urls, 1):
            lines.append(f"| {i} | {role} | {title} | {url} |\n")
        lines.append("\n## Flat URL list\n\n```\n")
        for *_, url in urls:
            lines.append(url + "\n")
        lines.append("```\n")
        (p / "references.md").write_text("".join(lines), encoding="utf-8")
        (p / "analysis.md").write_text(
            f"""# Analysis pointer — Iteration / Collatz studio

See **`research/video-research/collatz/analysis.md`** for definitions ($$T$$, $$\\mathrm{{Col}}_{{\\min}}$$, Syracuse map), Tao 2019 slogan, and confusions.

## Studio-specific extraction

"""
            + "\n".join(f"- {k}" for k in t["knowledge_en"])
            + "\n",
            encoding="utf-8",
        )
        (p / "learning_path.md").write_text(
            """# Learning path — Collatz studio

1. Stage 0–2 of `../collatz/learning_path.md`
2. Ch.1 Collatz essay exercises
3. Ch.7 portfolio (proposal → experiments → log → report)
""",
            encoding="utf-8",
        )
        return p

    p = PACK / t["slug"]
    p.mkdir(parents=True, exist_ok=True)
    urls = t["urls"]

    # README
    table_rows = []
    for i, (kind, role, title, url) in enumerate(urls, 1):
        if kind == "V":
            table_rows.append(f"| {i} | {role} | {title} | {url} |")
    readme = f"""# {t['title']} — video research pack

**Date:** {DATE}  
**Chapter:** {t['chapter']}  
**Kind:** {t.get('kind','topic')}  
**Parent theory:** {t.get('parent', '—')}

## Course pages

| Lang | Glob key |
|------|----------|
| EN | `contents/en/chapter{t['chapter']}/_posts/*{t['en']}.md` |
| VI | `contents/vi/chapter{t['chapter']}/_posts/*{t['vi']}.md` |

## Ranked video path (primary)

| # | Role | Title | URL |
|---|------|-------|-----|
{chr(10).join(table_rows) if table_rows else '| — | — | (see references for official pages / web) | — |'}

## Knowledge slogans (extract)

{chr(10).join('- ' + k for k in t['knowledge_en'])}

## Complete references

→ [`references.md`](references.md)

## Files

- `analysis.md` — definitions / status / confusions
- `learning_path.md` — staged goals
- `references.md` — **all** discovered URLs
"""
    (p / "README.md").write_text(readme, encoding="utf-8")

    # references.md
    ref = [f"# {t['title']} — complete URL bibliography\n\nDiscovered {DATE}.\n\n"]
    ref.append("## A. Videos\n\n| # | Role | Title | URL |\n|---|------|-------|-----|\n")
    n = 1
    for kind, role, title, url in urls:
        if kind == "V":
            ref.append(f"| V{n} | {role} | {title} | {url} |\n")
            n += 1
    ref.append("\n## B. Papers / primary literature\n\n| # | Title | URL |\n|---|-------|-----|\n")
    n = 1
    for kind, role, title, url in urls:
        if kind == "P":
            ref.append(f"| P{n} | {title} | {url} |\n")
            n += 1
    ref.append("\n## C. Official / web\n\n| # | Title | URL |\n|---|-------|-----|\n")
    n = 1
    for kind, role, title, url in urls:
        if kind == "W":
            ref.append(f"| W{n} | {title} | {url} |\n")
            n += 1
    ref.append("\n## Flat URL list (audit)\n\n```\n")
    for *_, url in urls:
        ref.append(url + "\n")
    ref.append("```\n")
    (p / "references.md").write_text("".join(ref), encoding="utf-8")

    # analysis.md
    analysis = f"""# Mode B analysis — {t['title']}

**Disclaimer:** No full machine transcripts claimed. Claims cross-checked against official prize pages, arXiv, and standard encyclopedic sources where cited.

## Slogans / extraction

{chr(10).join('### Point' + str(i+1) + chr(10) + chr(10) + k + chr(10) for i, k in enumerate(t['knowledge_en']))}

## Status notes

- Prize years and official citations: prefer abelprize.no / amturing.acm.org over media headlines.
- Open problems remain open unless a peer-accepted proof is cited with year.
- Popular videos are for **orientation**, not proof substitutes.

## Common confusions

- Confusing popular metaphors with theorem statements.
- Mixing prize years (especially Wigderson: **Abel 2021**, **Turing 2023**).
- Treating verification / simulation as proof on infinite domains.
"""
    (p / "analysis.md").write_text(analysis, encoding="utf-8")

    # learning_path.md
    vids = [(role, title, url) for kind, role, title, url in urls if kind == "V"]
    lp = [f"# Learning path — {t['title']}\n\n"]
    if vids:
        lp.append("## Stage 0 — Orientation\n\n")
        for role, title, url in vids[:2]:
            lp.append(f"- **{role}:** {title} — {url}\n")
        if len(vids) > 2:
            lp.append("\n## Stage 1 — Core\n\n")
            for role, title, url in vids[2:5]:
                lp.append(f"- **{role}:** {title} — {url}\n")
        if len(vids) > 5:
            lp.append("\n## Stage 2 — Depth / frontier\n\n")
            for role, title, url in vids[5:]:
                lp.append(f"- **{role}:** {title} — {url}\n")
    else:
        lp.append("Start with official pages in `references.md`, then one survey/paper abstract.\n")
    lp.append("\n## Stage final — Course lesson\n\nRead the EN/VI lecture, complete exercises, cite the pack in any A2/A5 writeup.\n")
    (p / "learning_path.md").write_text("".join(lp), encoding="utf-8")
    return p


MARK_EN = "math-video-researcher pack"
MARK_VI = "gói math-video-researcher"


def video_section_en(t: dict) -> str:
    pack = t.get("reuse_pack") or t["slug"]
    lines = [
        f"\n\n## Video sources ({MARK_EN})\n\n",
        f"Use videos for **orientation and research culture**, not as proof substitutes. ",
        f"Full ranking and notes: `research/video-research/{pack}/`.\n\n",
        "**From the research pack (must-know slogans)**\n\n",
    ]
    for k in t["knowledge_en"]:
        lines.append(f"- {k}\n")
    lines.append("\n**Recommended order**\n\n")
    n = 1
    for kind, role, title, url in t["urls"]:
        if kind == "V":
            lines.append(f"{n}. **{role.title()}** — {title}: [{url}]({url}).  \n")
            n += 1
    # also list official hubs first among W
    lines.append("\n**Official / primary written hubs**\n\n")
    for kind, role, title, url in t["urls"]:
        if kind in ("W", "P") and role in ("OFFICIAL", "PAPER", "CROSS"):
            lines.append(f"- {title}: {url}  \n")
    lines.append(
        f"\nComplete URL bibliography: `research/video-research/{pack}/references.md`.\n"
    )
    return "".join(lines)


def video_section_vi(t: dict) -> str:
    pack = t.get("reuse_pack") or t["slug"]
    lines = [
        f"\n\n## Nguồn video ({MARK_VI})\n\n",
        f"Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. ",
        f"Chi tiết: `research/video-research/{pack}/`.\n\n",
        "**Khẩu hiệu từ gói nghiên cứu**\n\n",
    ]
    for k in t["knowledge_vi"]:
        lines.append(f"- {k}\n")
    lines.append("\n**Thứ tự xem gợi ý**\n\n")
    n = 1
    for kind, role, title, url in t["urls"]:
        if kind == "V":
            lines.append(f"{n}. **{role}** — {title}: [{url}]({url}).  \n")
            n += 1
    lines.append("\n**Cổng chính thức / tài liệu**\n\n")
    for kind, role, title, url in t["urls"]:
        if kind in ("W", "P") and role in ("OFFICIAL", "PAPER", "CROSS"):
            lines.append(f"- {title}: {url}  \n")
    lines.append(
        f"\nDanh mục URL đầy đủ: `research/video-research/{pack}/references.md`.\n"
    )
    return "".join(lines)


def refs_block_en(t: dict) -> str:
    pack = t.get("reuse_pack") or t["slug"]
    lines = [
        f"\n\n### Video research pack (all URLs)\n\n",
        f"Complete list: `research/video-research/{pack}/references.md`.\n\n",
    ]
    n = 1
    for kind, role, title, url in t["urls"]:
        lines.append(f"{n}. {title} — {url}  \n")
        n += 1
    lines.append(f"{n}. Research pack folder: `research/video-research/{pack}/`.\n")
    return "".join(lines)


def refs_block_vi(t: dict) -> str:
    pack = t.get("reuse_pack") or t["slug"]
    lines = [
        f"\n\n### Gói nghiên cứu video (mọi URL)\n\n",
        f"Danh mục đầy đủ: `research/video-research/{pack}/references.md`.\n\n",
    ]
    n = 1
    for kind, role, title, url in t["urls"]:
        lines.append(f"{n}. {title} — {url}  \n")
        n += 1
    lines.append(f"{n}. Thư mục gói: `research/video-research/{pack}/`.\n")
    return "".join(lines)


REF_HEADERS_EN = re.compile(
    r"^## (References.*|Further directions)\s*$", re.M
)
# Prefer inserting before References; if only Further directions, before that.


def enrich_file(path: Path, t: dict, lang: str) -> str:
    text = path.read_text(encoding="utf-8")
    mark = MARK_EN if lang == "en" else MARK_VI
    if mark in text:
        # Still ensure all URLs appear in References if missing some
        missing = [u for *_, u in t["urls"] if u not in text and not u.startswith("contents/")]
        if not missing:
            return "skip-complete"
        # append missing urls before Further directions if possible
        block = refs_block_en(t) if lang == "en" else refs_block_vi(t)
        if "## Further directions" in text or "## Hướng đi tiếp" in text:
            text = re.sub(
                r"\n## (Further directions|Hướng đi tiếp)\s*\n",
                lambda m: block + "\n## " + m.group(1) + "\n\n",
                text,
                count=1,
            )
            path.write_text(text, encoding="utf-8")
            return "urls-appended"
        path.write_text(text + block, encoding="utf-8")
        return "urls-appended-end"

    vsec = video_section_en(t) if lang == "en" else video_section_vi(t)
    rsec = refs_block_en(t) if lang == "en" else refs_block_vi(t)

    # Insert video section before References / Tài liệu / Further directions
    patterns = [
        r"\n## References[^\n]*\n",
        r"\n## Tài liệu[^\n]*\n",
        r"\n## 8\. References[^\n]*\n",
        r"\n## 8\. Tài liệu[^\n]*\n",
        r"\n## 11\. References[^\n]*\n",
        r"\n## Further directions\n",
        r"\n## Hướng đi tiếp\n",
    ]
    inserted = False
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            # video section before this header; refs block after the references header block is harder —
            # put video before header, and refs block immediately after video (still before header)
            # Actually: Video sources before References; expand inside References by inserting after header
            if "References" in m.group(0) or "Tài liệu" in m.group(0):
                # Video before References; full URL list right after the References header line
                text = text[: m.start()] + vsec + text[m.start() : m.end()] + rsec + text[m.end() :]
            else:
                # No references header — put both before Further directions
                text = text[: m.start()] + vsec + rsec + text[m.start() :]
            inserted = True
            break
    if not inserted:
        text = text.rstrip() + vsec + rsec + "\n"

    # Body knowledge box: insert after first "---" following LOs if studio-like and no prior pack slogans
    if "research pack (must-know" not in text and "Khẩu hiệu từ gói" not in text:
        # already in video section
        pass

    path.write_text(text, encoding="utf-8")
    return "enriched"


def main():
    results = []
    for t in TOPICS:
        pack_path = write_pack(t)
        en_path = find_post("en", t["chapter"], t["en"])
        vi_path = find_post("vi", t["chapter"], t["vi"])
        st_en = enrich_file(en_path, t, "en")
        st_vi = enrich_file(vi_path, t, "vi")
        nurl = len(t["urls"])
        results.append(
            {
                "slug": t["slug"],
                "chapter": t["chapter"],
                "nurl": nurl,
                "pack": str(pack_path.relative_to(ROOT)),
                "en": st_en,
                "vi": st_vi,
                "en_file": str(en_path.relative_to(ROOT)),
                "vi_file": str(vi_path.relative_to(ROOT)),
            }
        )
        print(f"OK {t['slug']}: pack={pack_path.name} urls={nurl} en={st_en} vi={st_vi}")

    # curriculum touch
    cur = ROOT / "curriculum.md"
    ctext = cur.read_text(encoding="utf-8")
    note = (
        "\n- Ch.07–09 topic lessons video-research packs (studios + Abel + Turing) "
        f"enriched {DATE}; packs under `research/video-research/<slug>/`; "
        "Wigderson Turing **2023** (Abel 2021 with Lovász).\n"
    )
    if "Ch.07–09 topic lessons video-research packs" not in ctext:
        if "## Video sources absorbed" in ctext:
            ctext = ctext.replace(
                "## Video sources absorbed",
                "## Video sources absorbed" + note,
                1,
            )
        else:
            ctext += "\n## Video sources absorbed\n" + note
        cur.write_text(ctext, encoding="utf-8")
        print("Updated curriculum.md")

    # completion table
    print("\n## COMPLETION TABLE\n")
    print("| Slug | Ch | URLs | Pack | EN | VI |")
    print("|------|----|------|------|----|----|")
    for r in results:
        print(
            f"| {r['slug']} | {r['chapter']} | {r['nurl']} | {r['pack']} | {r['en']} | {r['vi']} |"
        )
    print(f"\nTotal topics: {len(results)}")


if __name__ == "__main__":
    main()
