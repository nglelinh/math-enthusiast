#!/usr/bin/env python3
"""Generate video-research packs and enrich Ch.3–4 topic lessons.

Creates research/video-research/<slug>/{README,references,analysis,learning_path}.md
and merges Video sources + complete References into EN+VI lesson posts.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
VR = ROOT / "research" / "video-research"
EN3 = ROOT / "contents" / "en" / "chapter03" / "_posts"
VI3 = ROOT / "contents" / "vi" / "chapter03" / "_posts"
EN4 = ROOT / "contents" / "en" / "chapter04" / "_posts"
VI4 = ROOT / "contents" / "vi" / "chapter04" / "_posts"

# ---------------------------------------------------------------------------
# Topic catalog
# ---------------------------------------------------------------------------

TOPICS: list[dict[str, Any]] = [
    # ===== CHAPTER 03 =====
    {
        "slug": "calculus-physics-engineering",
        "title": "Calculus → Physics & Engineering",
        "chapter": "03",
        "order": 2,
        "en": EN3 / "21-01-01-03_02_Calculus_Physics_Engineering.md",
        "vi": VI3 / "21-01-01-03_02_Calculus_Physics_Engineering.md",
        "status": "Core applied language (not an open problem).",
        "primary": {
            "title": "Best Explanation of Gradient, Divergence and Curl",
            "speaker": "Brain Station Advanced",
            "url": "https://www.youtube.com/watch?v=m_Psx7CdvDk",
            "duration": "~15 min",
            "role": "CORE intuition (vector calculus toolkit)",
            "level": "1–2",
        },
        "videos": [
            ("V1", "3Blue1Brown — Essence of calculus (series / ch.1 derivative)", "ORIENTATION", "https://www.youtube.com/watch?v=WUvTyaaNkzM"),
            ("V2", "3Blue1Brown — Essence of calculus playlist hub", "ORIENTATION", "https://www.3blue1brown.com/topics/calculus"),
            ("V3", "Brain Station Advanced — Gradient, Divergence and Curl", "CORE", "https://www.youtube.com/watch?v=m_Psx7CdvDk"),
            ("V4", "Khan Academy / 3B1B style multivariable (divergence theorem culture)", "FOUNDATION", "https://www.youtube.com/watch?v=rB83DpBJQsE"),
            ("V5", "MIT OCW 18.02 Multivariable Calculus (course page)", "FOUNDATION", "https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/"),
            ("V6", "MIT OCW 18.03 Differential Equations (video lectures)", "FOUNDATION", "https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/"),
            ("V7", "Gilbert Strang & Cleve Moler — Learn Differential Equations (overview)", "FOUNDATION", "https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/"),
            ("V8", "3Blue1Brown — Divergence and curl playlist (multivariable)", "INTUITION", "https://www.3blue1brown.com/topics/multivariable-calculus"),
        ],
        "secondary_videos": [
            ("V9", "Numberphile / related continuum modeling culture (optional)", "SECONDARY", "https://www.youtube.com/user/numberphile"),
        ],
        "papers_web": [
            ("P1", "Evans — Partial Differential Equations (AMS Graduate Studies)", "https://bookstore.ams.org/gsm-19-r"),
            ("W1", "Wikipedia — Fundamental theorem of calculus", "https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus"),
            ("W2", "Wikipedia — Finite element method", "https://en.wikipedia.org/wiki/Finite_element_method"),
            ("W3", "MIT OCW 18.02", "https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/"),
            ("W4", "MIT OCW 18.03", "https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/"),
        ],
        "defs": [
            ("Gradient", r"$$\nabla f$$ is the vector of partial derivatives; direction of steepest *ascent* of $$f$$. Descent uses $$-\nabla f$$."),
            ("Divergence", r"$$\nabla\cdot\mathbf{v}$$ is a scalar measuring net source/sink strength of a vector field."),
            ("Curl", r"$$\nabla\times\mathbf{v}$$ measures local rotation (paddle-wheel test)."),
            ("FTC", r"If $$F'=f$$ then $$\int_a^b f=F(b)-F(a)$$ under standard hypotheses."),
            ("Newton II", r"$$m\ddot x=F(x,\dot x,t)$$ is an ODE for the unknown trajectory $$x(t)$$."),
        ],
        "takeaways": [
            "Gradient points uphill, not downhill — common video + exam confusion.",
            "Zero divergence means no net source/sink, not that the fluid is still.",
            "FEM is discretized variational calculus + linear algebra, not a replacement for calculus.",
            "ODE vs PDE: space as independent variable changes both theory and numerics.",
        ],
        "path": [
            ("0 Orientation", "3B1B Essence of calculus ch.1", "Derivative as instantaneous rate; integral as accumulation."),
            ("1 Core toolkit", "Brain Station grad/div/curl", "State slogans for $$\nabla f$$, div, curl with one example each."),
            ("2 Continuum", "MIT 18.02 / 18.03 samples", "Heat/wave slogans; Newton as ODE."),
            ("3 Course", "Ch.3 calculus essay + DE essay", "FEM weak form sketch; engineering audit exercise."),
        ],
        "en_inject_knowledge": """### Vector calculus slogans (from video research)

Primary intuition video: [Brain Station — Gradient, Divergence and Curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) (~15 min), cross-checked with standard multivariable calculus.

- **Gradient:** $$\\nabla f$$ is the vector of partial derivatives; it points **uphill** (steepest ascent). Physical “rolling downhill” follows $$-\\nabla f$$.
- **Divergence:** $$\\nabla\\cdot\\mathbf{v}$$ is a *scalar*. Positive ≈ source, negative ≈ sink, zero ≈ volume-preserving flow (which can still move).
- **Curl:** $$\\nabla\\times\\mathbf{v}$$ measures local rotation (paddle-wheel test).
- Pair with 3Blue1Brown’s [Essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) for the FTC narrative before the vector operators.
""",
        "vi_inject_knowledge": """### Khẩu hiệu giải tích vector (từ nghiên cứu video)

Video trực quan chính: [Brain Station — Gradient, Divergence and Curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) (~15 phút).

- **Gradient:** $$\\nabla f$$ là vector các đạo hàm riêng; hướng **lên dốc** (tăng nhanh nhất). Xuống dốc dùng $$-\\nabla f$$.
- **Divergence:** $$\\nabla\\cdot\\mathbf{v}$$ là *vô hướng*. Dương ≈ nguồn, âm ≈ hố, không ≈ bảo toàn thể tích (vẫn có thể chuyển động).
- **Curl:** $$\\nabla\\times\\mathbf{v}$$ đo quay cục bộ (thử bánh lái nhỏ).
- Kết hợp [Essence of calculus — 3Blue1Brown](https://www.youtube.com/watch?v=WUvTyaaNkzM) cho định lý cơ bản trước các toán tử vector.
""",
    },
    {
        "slug": "linear-algebra-ai",
        "title": "Linear Algebra → AI",
        "chapter": "03",
        "order": 3,
        "en": EN3 / "21-01-01-03_03_Linear_Algebra_AI.md",
        "vi": VI3 / "21-01-01-03_03_Linear_Algebra_AI.md",
        "status": "Core ML substrate (solved classical math; active engineering frontiers).",
        "primary": {
            "title": "But what is a neural network? | Deep learning chapter 1",
            "speaker": "3Blue1Brown (Grant Sanderson)",
            "url": "https://www.youtube.com/watch?v=aircAruvnKk",
            "duration": "~19 min",
            "role": "ORIENTATION + CORE (layers as matrix maps + nonlinearities)",
            "level": "1–2",
        },
        "videos": [
            ("V1", "3Blue1Brown — But what is a neural network?", "ORIENTATION", "https://www.youtube.com/watch?v=aircAruvnKk"),
            ("V2", "3Blue1Brown — Gradient descent, how neural networks learn", "CORE", "https://www.youtube.com/watch?v=IHZwWFHWa-w"),
            ("V3", "3Blue1Brown — What is backpropagation really doing?", "CORE", "https://www.youtube.com/watch?v=Ilg3gGewQ5U"),
            ("V4", "3Blue1Brown — Essence of linear algebra (playlist)", "FOUNDATION", "https://www.3blue1brown.com/topics/linear-algebra"),
            ("V5", "3Blue1Brown — Essence of linear algebra ch.1 (vectors)", "FOUNDATION", "https://www.youtube.com/watch?v=fNk_zzaMoSs"),
            ("V6", "MIT OCW 18.06 Strang — Geometry of linear equations", "FOUNDATION", "https://www.youtube.com/watch?v=J7DzL2_Na80"),
            ("V7", "MIT OCW 18.06 playlist (Strang)", "FOUNDATION", "https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8"),
            ("V8", "MIT OCW 18.06 course page", "FOUNDATION", "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"),
            ("V9", "3Blue1Brown neural networks playlist", "CORE", "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi"),
        ],
        "secondary_videos": [
            ("V10", "Stanford CS229 / related ML theory lectures (optional survey)", "FRONTIER", "https://www.youtube.com/@stanfordonline"),
        ],
        "papers_web": [
            ("P1", "Vaswani et al. — Attention Is All You Need (2017)", "https://arxiv.org/abs/1706.03762"),
            ("P2", "Goodfellow, Bengio, Courville — Deep Learning (book site)", "https://www.deeplearningbook.org/"),
            ("W1", "Strang — Linear Algebra and Learning from Data (MIT)", "https://math.mit.edu/~gs/learningfromdata/"),
            ("W2", "Wikipedia — Singular value decomposition", "https://en.wikipedia.org/wiki/Singular_value_decomposition"),
            ("W3", "3Blue1Brown linear algebra topic hub", "https://www.3blue1brown.com/topics/linear-algebra"),
        ],
        "defs": [
            ("Affine layer", r"$$x\mapsto Wx+b$$; compositions of affine maps stay affine — hence nonlinear activations."),
            ("SVD/PCA", r"Best low-rank approximation in Frobenius/spectral norms; PCA via top right singular vectors of centered data."),
            ("Backprop", r"Reverse-mode automatic differentiation / chain rule on a computational graph."),
            ("Attention slogan", r"Core mixing is matrix products + softmax; still linear-algebra-centric."),
        ],
        "takeaways": [
            "Neural nets are affine *plus* nonlinearities; pure linear depth collapses.",
            "Backprop is systematic chain rule, not a new algebra.",
            "Attention/transformers are structured matrix multiplies at scale.",
            "Strang 18.06 gives the geometric foundation; 3B1B DL series shows the ML pipeline.",
        ],
        "path": [
            ("0 Orientation", "3B1B neural network ch.1–2", "Layers + gradient descent picture."),
            ("1 Linear foundation", "3B1B essence LA + Strang Lec 1", "Matrix as geometry; four subspaces culture."),
            ("2 Learning math", "3B1B backprop", "Chain rule on graphs."),
            ("3 Course", "Ch.3 LA→AI essay", "SVD exercise; attention as structured LA."),
        ],
        "en_inject_knowledge": """### Linear algebra as ML substrate (from video research)

Recommended path: 3Blue1Brown [neural network](https://www.youtube.com/watch?v=aircAruvnKk) → [gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) → [backprop](https://www.youtube.com/watch?v=Ilg3gGewQ5U), plus Strang [18.06 Lec 1](https://www.youtube.com/watch?v=J7DzL2_Na80).

- A deep net without nonlinearities is still one affine map $$x\\mapsto Wx+b$$.
- Training is (stochastic) gradient descent on a high-dimensional loss; backprop evaluates those gradients efficiently.
- SVD/PCA remain the linear baseline for compression and denoising before nonlinear representation learning.
""",
        "vi_inject_knowledge": """### Đại số tuyến tính như nền ML (từ nghiên cứu video)

Lộ trình: 3Blue1Brown [mạng nơ-ron](https://www.youtube.com/watch?v=aircAruvnKk) → [gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) → [backprop](https://www.youtube.com/watch?v=Ilg3gGewQ5U); thêm Strang [18.06 bài 1](https://www.youtube.com/watch?v=J7DzL2_Na80).

- Mạng sâu không phi tuyến vẫn chỉ là một ánh xạ affine $$x\\mapsto Wx+b$$.
- Huấn luyện là gradient descent (ngẫu nhiên) trên hàm mất mát; backprop tính gradient hiệu quả.
- SVD/PCA là baseline tuyến tính cho nén/khử nhiễu trước học biểu diễn phi tuyến.
""",
    },
    {
        "slug": "probability-data-science",
        "title": "Probability → Data Science",
        "chapter": "03",
        "order": 4,
        "en": EN3 / "21-01-01-03_04_Probability_Data_Science.md",
        "vi": VI3 / "21-01-01-03_04_Probability_Data_Science.md",
        "status": "Core probabilistic modeling language for data and ML risk.",
        "primary": {
            "title": "Bayes theorem, the geometry of Bayesian update (3Blue1Brown)",
            "speaker": "3Blue1Brown",
            "url": "https://www.youtube.com/watch?v=HZGCoVF3YvM",
            "duration": "~15 min",
            "role": "CORE intuition (Bayes + geometric probability)",
            "level": "1–2",
        },
        "videos": [
            ("V1", "3Blue1Brown — Bayes theorem (the geometry of Bayesian update)", "CORE", "https://www.youtube.com/watch?v=HZGCoVF3YvM"),
            ("V2", "3Blue1Brown — Binomial distributions | Probabilities of probabilities", "FOUNDATION", "https://www.youtube.com/watch?v=8idr1WZ1A7Q"),
            ("V3", "Harvard Stat 110 (Blitzstein) — course / lecture portal", "FOUNDATION", "https://stat110.net/"),
            ("V4", "Harvard Stat 110 YouTube playlist", "FOUNDATION", "https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo"),
            ("V5", "Veritasium — The Bayesian trap (base rates)", "ORIENTATION / hygiene", "https://www.youtube.com/watch?v=R13BD8qKeTg"),
            ("V6", "Khan Academy — Central limit theorem overview", "ORIENTATION", "https://www.youtube.com/watch?v=YAlJCEDH2uY"),
            ("V7", "StatQuest — Maximum likelihood fundamentals", "INTUITION", "https://www.youtube.com/watch?v=XepXtl9YKwc"),
            ("V8", "MIT 6.041 Probabilistic Systems Analysis (OCW)", "FOUNDATION", "https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/"),
        ],
        "secondary_videos": [
            ("V9", "3Blue1Brown lockdown math / related probability episodes", "SECONDARY", "https://www.3blue1brown.com/"),
        ],
        "papers_web": [
            ("P1", "Wasserman — All of Statistics (Springer)", "https://link.springer.com/book/10.1007/978-0-387-21736-9"),
            ("W1", "Wikipedia — Law of large numbers", "https://en.wikipedia.org/wiki/Law_of_large_numbers"),
            ("W2", "Wikipedia — Central limit theorem", "https://en.wikipedia.org/wiki/Central_limit_theorem"),
            ("W3", "Wikipedia — Concentration inequality", "https://en.wikipedia.org/wiki/Concentration_inequality"),
            ("W4", "Blitzstein & Hwang — Introduction to Probability (Stat 110)", "https://stat110.net/"),
        ],
        "defs": [
            ("Expectation", r"Linear operator $$\mathbb{E}[aX+bY]=a\mathbb{E}X+b\mathbb{E}Y$$ (when defined)."),
            ("LLN", r"Sample averages converge to expectation under i.i.d. hypotheses."),
            ("CLT", r"Normalized sums approach a Gaussian; explains many bell-shaped histograms."),
            ("Bayes", r"$$P(H\mid D)=P(D\mid H)P(H)/P(D)$$ — update beliefs with evidence."),
            ("Risk", r"ML risk is expected loss $$\mathbb{E}[\ell(f(X),Y)]$$; empirical risk approximates it."),
        ],
        "takeaways": [
            "Independence is a modeling assumption, not automatic from “different people.”",
            "Base-rate neglect is the main Bayes hygiene failure (Veritasium Bayesian trap).",
            "LLN ≠ CLT: one is about averages settling; the other about fluctuation shapes.",
            "Correlation is not causation — still true after fancy ML.",
        ],
        "path": [
            ("0 Orientation", "Veritasium Bayesian trap + CLT overview", "Base rates; bell curves."),
            ("1 Core", "3B1B Bayes + binomial", "Update geometry; discrete distributions."),
            ("2 Foundation", "Stat 110 sample lectures", "Formal probability language."),
            ("3 Course", "Ch.3 probability essay", "Risk vs empirical risk; concentration slogan."),
        ],
        "en_inject_knowledge": """### Probability slogans (from video research)

Watch [3B1B Bayes](https://www.youtube.com/watch?v=HZGCoVF3YvM) and [Veritasium — The Bayesian trap](https://www.youtube.com/watch?v=R13BD8qKeTg) before the inference section.

- **Bayes hygiene:** always write the base rate; posterior odds = prior odds × likelihood ratio.
- **LLN vs CLT:** LLN says averages settle; CLT says *fluctuations* (properly scaled) look Gaussian.
- **ML risk** is an expectation; training error is one sample path of that expectation.
""",
        "vi_inject_knowledge": """### Khẩu hiệu xác suất (từ nghiên cứu video)

Xem [3B1B Bayes](https://www.youtube.com/watch?v=HZGCoVF3YvM) và [Veritasium — The Bayesian trap](https://www.youtube.com/watch?v=R13BD8qKeTg) trước phần suy diễn.

- **Vệ sinh Bayes:** luôn viết base rate; odds hậu nghiệm = odds tiên nghiệm × tỉ số likelihood.
- **LLN vs CLT:** LLN nói trung bình ổn định; CLT nói *dao động* (chuẩn hóa) trông Gaussian.
- **Rủi ro ML** là kỳ vọng; lỗi huấn luyện là một quỹ đạo mẫu của kỳ vọng đó.
""",
    },
    {
        "slug": "number-theory-cryptography",
        "title": "Number Theory → Cryptography",
        "chapter": "03",
        "order": 5,
        "en": EN3 / "21-01-01-03_05_Number_Theory_Cryptography.md",
        "vi": VI3 / "21-01-01-03_05_Number_Theory_Cryptography.md",
        "status": "Deployed classical public-key; active post-quantum transition.",
        "primary": {
            "title": "Encryption and HUGE numbers (RSA) — Numberphile",
            "speaker": "Numberphile (James Grime et al.)",
            "url": "https://www.youtube.com/watch?v=M7kEpw1tn50",
            "duration": "~9 min",
            "role": "ORIENTATION (RSA culture)",
            "level": "1",
        },
        "videos": [
            ("V1", "Numberphile — Encryption and HUGE numbers (RSA)", "ORIENTATION", "https://www.youtube.com/watch?v=M7kEpw1tn50"),
            ("V2", "Numberphile — RSA-129", "INTUITION / history", "https://www.youtube.com/watch?v=YQw124CtvO0"),
            ("V3", "Computerphile — Public Key Cryptography", "FOUNDATION", "https://www.youtube.com/watch?v=GSIDS_lvRv4"),
            ("V4", "Computerphile — Diffie-Hellman Key Exchange", "CORE", "https://www.youtube.com/watch?v=NmM9HA2MQGI"),
            ("V5", "Numberphile/Computerphile crypto playlist", "SURVEY", "https://www.youtube.com/playlist?list=PLt5AfwLFPxWLXe-ZqZyu0kSsaWd4FjXbj"),
            ("V6", "Khan Academy — Journey into cryptography (hub)", "FOUNDATION", "https://www.khanacademy.org/computing/computer-science/cryptography"),
            ("V7", "Stanford / Dan Boneh crypto course culture (Coursera/YouTube search)", "FOUNDATION", "https://crypto.stanford.edu/~dabo/courses/"),
            ("V8", "NIST Post-Quantum Cryptography project", "FRONTIER", "https://csrc.nist.gov/projects/post-quantum-cryptography"),
        ],
        "secondary_videos": [
            ("V9", "Numberphile — primes and primality culture videos", "SECONDARY", "https://www.youtube.com/@numberphile"),
        ],
        "papers_web": [
            ("P1", "Rivest, Shamir, Adleman — A Method for Obtaining Digital Signatures… (1978)", "https://people.csail.mit.edu/rivest/Rsapaper.pdf"),
            ("P2", "Diffie & Hellman — New Directions in Cryptography (1976)", "https://ee.stanford.edu/~hellman/publications/24.pdf"),
            ("P3", "NIST PQC standards overview", "https://csrc.nist.gov/projects/post-quantum-cryptography"),
            ("W1", "Wikipedia — RSA (cryptosystem)", "https://en.wikipedia.org/wiki/RSA_(cryptosystem)"),
            ("W2", "Wikipedia — Diffie–Hellman key exchange", "https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange"),
            ("W3", "Wikipedia — Post-quantum cryptography", "https://en.wikipedia.org/wiki/Post-quantum_cryptography"),
        ],
        "defs": [
            ("Congruence", r"$$a\equiv b\pmod n$$ iff $$n\mid(a-b)$$."),
            ("RSA slogan", r"$$c\equiv m^e\pmod n$$; decrypt with $$d$$ where $$ed\equiv 1\pmod{\varphi(n)}$$."),
            ("DLP", r"Given $$g,g^a$$ in a group, recover $$a$$ (hard in good groups)."),
            ("Kerckhoffs", r"Security rests on key secrecy, not algorithm secrecy."),
        ],
        "takeaways": [
            "Textbook RSA without padding is not deployable security.",
            "Factoring hardness is an *assumption*, not a theorem.",
            "ECC is still discrete-log style hardness in a different group.",
            "Post-quantum: lattice/code/hash-based schemes replace factoring/DL assumptions under NIST migration.",
        ],
        "path": [
            ("0 Orientation", "Numberphile RSA + RSA-129", "Huge primes as public keys; history of factoring challenges."),
            ("1 Mechanism", "Computerphile public key + DH", "Trapdoor vs shared secret."),
            ("2 Formal", "Ch.3 crypto essay §§1–5", "Modular arithmetic → RSA → ECC slogans."),
            ("3 Frontier", "NIST PQC page", "Why Shor changes the hardness landscape."),
        ],
        "en_inject_knowledge": """### Crypto video hygiene (from research)

Primary popular path: [Numberphile RSA](https://www.youtube.com/watch?v=M7kEpw1tn50) → [RSA-129](https://www.youtube.com/watch?v=YQw124CtvO0) → [Computerphile public key](https://www.youtube.com/watch?v=GSIDS_lvRv4) → [Diffie–Hellman](https://www.youtube.com/watch?v=NmM9HA2MQGI).

- Videos explain *trapdoors* well; they usually omit padding, side channels, and parameter hygiene.
- Correctness of RSA uses Euler/Fermat modular cancellation; security is computational, not information-theoretic.
- Post-quantum transition is policy + mathematics: see [NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography).
""",
        "vi_inject_knowledge": """### Vệ sinh video mật mã (từ nghiên cứu)

Lộ trình phổ biến: [Numberphile RSA](https://www.youtube.com/watch?v=M7kEpw1tn50) → [RSA-129](https://www.youtube.com/watch?v=YQw124CtvO0) → [Computerphile public key](https://www.youtube.com/watch?v=GSIDS_lvRv4) → [Diffie–Hellman](https://www.youtube.com/watch?v=NmM9HA2MQGI).

- Video giải thích *trapdoor* tốt; thường bỏ padding, side channel, và vệ sinh tham số.
- Tính đúng RSA dùng Euler/Fermat; an ninh là tính toán, không phải lý thuyết thông tin.
- Hậu lượng tử: xem [NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography).
""",
    },
    {
        "slug": "graph-theory-networks",
        "title": "Graph Theory → Networks",
        "chapter": "03",
        "order": 6,
        "en": EN3 / "21-01-01-03_06_Graph_Theory_Networks.md",
        "vi": VI3 / "21-01-01-03_06_Graph_Theory_Networks.md",
        "status": "Classical algorithms + modern network science.",
        "primary": {
            "title": "Graph theory / networks educational path (MIT + popular)",
            "speaker": "MIT OCW / Numberphile / 3B1B-adjacent",
            "url": "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/",
            "duration": "course-scale",
            "role": "FOUNDATION",
            "level": "2",
        },
        "videos": [
            ("V1", "MIT 6.042J Mathematics for Computer Science (graphs modules)", "FOUNDATION", "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/"),
            ("V2", "MIT 6.006 Introduction to Algorithms (graph algorithms)", "FOUNDATION", "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/"),
            ("V3", "Numberphile — Graph theory / networks culture (search: graphs Numberphile)", "ORIENTATION", "https://www.youtube.com/results?search_query=numberphile+graph+theory"),
            ("V4", "Numberphile — Seven Bridges of Königsberg culture", "ORIENTATION", "https://www.youtube.com/watch?v=W18FDEA1jRQ"),
            ("V5", "3Blue1Brown — Eigenvectors and eigenvalues (spectral seeds)", "INTUITION", "https://www.youtube.com/watch?v=PFDu9oVAE-g"),
            ("V6", "PageRank explained (popular / CS culture)", "CORE", "https://www.youtube.com/watch?v=JGQe4kiPnrU"),
            ("V7", "Stanford / network science lectures (Barabási-style surveys)", "SURVEY", "https://www.youtube.com/results?search_query=network+science+lecture+barabasi"),
            ("V8", "Spectral graph theory intro talks (Spielman culture)", "FRONTIER", "https://www.youtube.com/results?search_query=spielman+spectral+graph+theory"),
        ],
        "secondary_videos": [
            ("V9", "Algorithms Illuminated / Roughgarden graph modules", "SECONDARY", "https://www.algorithmsilluminated.org/"),
        ],
        "papers_web": [
            ("P1", "Brin & Page — The Anatomy of a Large-Scale Hypertextual Web Search Engine", "http://infolab.stanford.edu/~backrub/google.html"),
            ("W1", "Wikipedia — Graph theory", "https://en.wikipedia.org/wiki/Graph_theory"),
            ("W2", "Wikipedia — Max-flow min-cut theorem", "https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem"),
            ("W3", "Wikipedia — PageRank", "https://en.wikipedia.org/wiki/PageRank"),
            ("W4", "Wikipedia — Expander graph", "https://en.wikipedia.org/wiki/Expander_graph"),
            ("W5", "Spielman — Spectral Graph Theory notes", "https://cs-www.cs.yale.edu/homes/spielman/sagt/"),
        ],
        "defs": [
            ("Graph", r"$$G=(V,E)$$; adjacency encodes connection."),
            ("Path / distance", r"Shortest-path metrics; connectivity components."),
            ("Max-flow min-cut", r"Maximum flow value equals minimum cut capacity."),
            ("Laplacian", r"$$L=D-A$$; spectral cuts and random-walk mixing."),
            ("PageRank slogan", r"Stationary distribution of a damped random walk on the web graph."),
        ],
        "takeaways": [
            "Connectivity is not the same as “lots of edges” — expanders are sparse yet superbly connected.",
            "Flows and cuts are dual views of capacity.",
            "PageRank is linear algebra + Markov chains, not magic keywords.",
            "NP-hard network problems remain hard; heuristics need honesty.",
        ],
        "path": [
            ("0 Orientation", "Königsberg + small graph demos", "Edges as constraints."),
            ("1 Algorithms", "MIT 6.006 / 6.042 graph modules", "BFS, shortest paths, flows."),
            ("2 Spectral", "3B1B eigenvectors + Spielman notes", "Laplacian eigenvalues."),
            ("3 Course", "Ch.3 networks essay", "PageRank + expanders slogans."),
        ],
        "en_inject_knowledge": """### Network math slogans (from video research)

- **Max-flow min-cut:** capacity is both a flow question and a cut question.
- **PageRank:** dominant eigenvector / stationary distribution of a damped walk — linear algebra on the web.
- **Expanders:** sparse graphs with excellent connectivity; spectral gap is the quantitative heart.
- Start with MIT discrete math/algorithms OCW, then the Ch.3 essay’s spectral section.
""",
        "vi_inject_knowledge": """### Khẩu hiệu toán mạng (từ nghiên cứu video)

- **Max-flow min-cut:** dung lượng vừa là câu hỏi luồng vừa là câu hỏi cắt.
- **PageRank:** vector riêng trội / phân phối dừng của bước ngẫu nhiên có damping — đại số tuyến tính trên đồ thị web.
- **Expanders:** thưa nhưng kết nối cực tốt; khe phổ là trái tim định lượng.
- Bắt đầu MIT OCW rời rạc/thuật toán, rồi phần phổ trong bài Ch.3.
""",
    },
    {
        "slug": "optimization-operations-ai",
        "title": "Optimization → Operations & AI",
        "chapter": "03",
        "order": 7,
        "en": EN3 / "21-01-01-03_07_Optimization_Operations_AI.md",
        "vi": VI3 / "21-01-01-03_07_Optimization_Operations_AI.md",
        "status": "Convex core classical; nonconvex DL optimization active research.",
        "primary": {
            "title": "Gradient descent, how neural networks learn — 3Blue1Brown",
            "speaker": "3Blue1Brown",
            "url": "https://www.youtube.com/watch?v=IHZwWFHWa-w",
            "duration": "~21 min",
            "role": "CORE (first-order methods intuition)",
            "level": "1–2",
        },
        "videos": [
            ("V1", "3Blue1Brown — Gradient descent, how neural networks learn", "CORE", "https://www.youtube.com/watch?v=IHZwWFHWa-w"),
            ("V2", "Stanford / Boyd — Convex Optimization lectures (EE364)", "FOUNDATION", "https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h"),
            ("V3", "Boyd & Vandenberghe — Convex Optimization book (free PDF)", "FOUNDATION", "https://web.stanford.edu/~boyd/cvxbook/"),
            ("V4", "MIT 6.255J / optimization OCW culture", "FOUNDATION", "https://ocw.mit.edu/search/?q=optimization"),
            ("V5", "StatQuest — Gradient Descent", "ORIENTATION", "https://www.youtube.com/watch?v=sDv4f4s2SB8"),
            ("V6", "3Blue1Brown — Essence of calculus (derivatives for optimization)", "ORIENTATION", "https://www.youtube.com/watch?v=WUvTyaaNkzM"),
            ("V7", "Linear programming simplex culture (popular explainers)", "INTUITION", "https://www.youtube.com/results?search_query=linear+programming+simplex+explained"),
            ("V8", "Duality / Lagrange multipliers visual lectures", "CORE", "https://www.youtube.com/results?search_query=lagrange+multipliers+3blue1brown"),
        ],
        "secondary_videos": [
            ("V9", "Nocedal & Wright numerical optimization culture talks", "SECONDARY", "https://www.youtube.com/results?search_query=numerical+optimization+lecture"),
        ],
        "papers_web": [
            ("P1", "Boyd & Vandenberghe — Convex Optimization (PDF)", "https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf"),
            ("P2", "Nesterov — Introductory Lectures on Convex Optimization", "https://link.springer.com/book/10.1007/978-1-4419-8853-9"),
            ("W1", "Wikipedia — Convex optimization", "https://en.wikipedia.org/wiki/Convex_optimization"),
            ("W2", "Wikipedia — Linear programming", "https://en.wikipedia.org/wiki/Linear_programming"),
            ("W3", "Wikipedia — Lagrange multiplier", "https://en.wikipedia.org/wiki/Lagrange_multiplier"),
            ("W4", "Wikipedia — Stochastic gradient descent", "https://en.wikipedia.org/wiki/Stochastic_gradient_descent"),
        ],
        "defs": [
            ("Template", r"Minimize $$f(x)$$ over $$x\in\mathcal{C}$$; constraints define feasible set."),
            ("Convexity", r"Local min = global min for convex $$f$$ on convex set (under mild conditions)."),
            ("GD step", r"$$x_{k+1}=x_k-\eta\nabla f(x_k)$$."),
            ("Duality slogan", r"Dual variables are prices / certificates of optimality."),
        ],
        "takeaways": [
            "Convexity is the reliability contract; deep learning often leaves it.",
            "SGD noise is a feature for large data, not only a bug.",
            "LP is the OR workhorse; integer programs jump complexity.",
            "A critical point is not automatically a global minimum outside convexity.",
        ],
        "path": [
            ("0 Orientation", "StatQuest GD + 3B1B GD", "Steps downhill in parameter space."),
            ("1 Convex core", "Boyd EE364 sample + book ch.1–4", "Convex sets/functions; LP."),
            ("2 Constraints", "Lagrange / KKT popular lectures", "Certificates and dual prices."),
            ("3 Course", "Ch.3 optimization essay", "OR vs DL optimization honesty."),
        ],
        "en_inject_knowledge": """### Optimization slogans (from video research)

Pair [3B1B gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) with Boyd’s free book [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).

- **Convexity:** every local minimum is global — the reason solvers can certify.
- **First-order methods:** only gradients; scale to high dimension at the cost of slow local conditioning.
- **Duality:** optimal dual variables price constraints; strong duality needs constraint qualifications.
""",
        "vi_inject_knowledge": """### Khẩu hiệu tối ưu (từ nghiên cứu video)

Ghép [3B1B gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) với sách miễn phí Boyd [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).

- **Lồi:** cực tiểu địa phương = toàn cục — lý do solver chứng nhận được.
- **Bậc nhất:** chỉ dùng gradient; mở rộng chiều cao, đổi lại điều kiện số.
- **Đối ngẫu:** biến đối ngẫu định giá ràng buộc; strong duality cần điều kiện ràng buộc.
""",
    },
    {
        "slug": "fourier-signal-processing",
        "title": "Fourier → Signal Processing",
        "chapter": "03",
        "order": 8,
        "en": EN3 / "21-01-01-03_08_Fourier_Signal_Processing.md",
        "vi": VI3 / "21-01-01-03_08_Fourier_Signal_Processing.md",
        "status": "Classical harmonic analysis + ubiquitous DSP/FFT engineering.",
        "primary": {
            "title": "But what is a Fourier series? — 3Blue1Brown",
            "speaker": "3Blue1Brown",
            "url": "https://www.youtube.com/watch?v=r6sGWTCMz2k",
            "duration": "~25 min",
            "role": "CORE visual foundation",
            "level": "1–2",
        },
        "videos": [
            ("V1", "3Blue1Brown — But what is a Fourier series?", "CORE", "https://www.youtube.com/watch?v=r6sGWTCMz2k"),
            ("V2", "3Blue1Brown — But what is the Fourier Transform?", "CORE", "https://www.youtube.com/watch?v=spUNpyF58BY"),
            ("V3", "3Blue1Brown — Fourier transform / series topic hub", "SURVEY", "https://www.3blue1brown.com/topics/fourier-transform"),
            ("V4", "Stanford EE261 / DSP culture (Oppenheim-style courses)", "FOUNDATION", "https://see.stanford.edu/Course/EE261"),
            ("V5", "MIT OCW 6.003 Signals and Systems", "FOUNDATION", "https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/"),
            ("V6", "FFT explained (popular algorithm videos)", "INTUITION", "https://www.youtube.com/results?search_query=fft+explained+algorithm"),
            ("V7", "Sampling theorem / Nyquist explainers", "FOUNDATION", "https://www.youtube.com/results?search_query=nyquist+shannon+sampling+theorem"),
            ("V8", "Numberphile — Fourier culture / related", "ORIENTATION", "https://www.youtube.com/results?search_query=numberphile+fourier"),
        ],
        "secondary_videos": [
            ("V9", "JPEG compression math explainers", "SECONDARY", "https://www.youtube.com/results?search_query=jpeg+dct+explained"),
        ],
        "papers_web": [
            ("P1", "Cooley & Tukey — An algorithm for the machine calculation of complex Fourier series (1965)", "https://www.ams.org/journals/mcom/1965-19-090/S0025-5718-1965-0178586-1/"),
            ("W1", "Wikipedia — Fourier transform", "https://en.wikipedia.org/wiki/Fourier_transform"),
            ("W2", "Wikipedia — Fast Fourier transform", "https://en.wikipedia.org/wiki/Fast_Fourier_transform"),
            ("W3", "Wikipedia — Nyquist–Shannon sampling theorem", "https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem"),
            ("W4", "Wikipedia — Discrete cosine transform", "https://en.wikipedia.org/wiki/Discrete_cosine_transform"),
            ("W5", "3Blue1Brown Fourier hub", "https://www.3blue1brown.com/topics/fourier-transform"),
        ],
        "defs": [
            ("Fourier series", r"Periodic $$f$$ as sum of sines/cosines (or complex exponentials) with coefficients $$\hat f(k)$$."),
            ("Fourier transform", r"Non-periodic signals: continuum of frequencies."),
            ("DFT/FFT", r"Discrete spectra; FFT computes DFT in $$O(n\log n)$$."),
            ("Nyquist", r"Bandlimited sampling needs more than twice the highest frequency (slogan form)."),
        ],
        "takeaways": [
            "Frequency is a coordinate system, not a property only of sound.",
            "FFT is an algorithm for the DFT, not a different transform species.",
            "JPEG uses DCT (Fourier cousin) + quantization + entropy coding.",
            "Windowing and uncertainty: sharp in time ↔ smeared in frequency.",
        ],
        "path": [
            ("0 Orientation", "3B1B Fourier series", "Circles wrapping a signal."),
            ("1 Transform", "3B1B Fourier transform", "Winding frequencies; spikes as pure tones."),
            ("2 Discrete", "FFT + sampling videos", "DFT indices; aliasing."),
            ("3 Course", "Ch.3 Fourier essay", "Compression + PDE links."),
        ],
        "en_inject_knowledge": """### Fourier slogans (from video research)

Primary path: [3B1B Fourier series](https://www.youtube.com/watch?v=r6sGWTCMz2k) → [Fourier transform](https://www.youtube.com/watch?v=spUNpyF58BY).

- Series for periodic worlds; transform for non-periodic; DFT for finite samples; FFT for fast DFT.
- Sampling below Nyquist aliases high frequencies into low ones — irreversible confusion in the discrete data.
- Compression keeps large coefficients in a Fourier/DCT basis where energy concentrates.
""",
        "vi_inject_knowledge": """### Khẩu hiệu Fourier (từ nghiên cứu video)

Lộ trình: [3B1B Fourier series](https://www.youtube.com/watch?v=r6sGWTCMz2k) → [Fourier transform](https://www.youtube.com/watch?v=spUNpyF58BY).

- Series cho thế giới tuần hoàn; transform cho không tuần hoàn; DFT cho mẫu hữu hạn; FFT để tính DFT nhanh.
- Lấy mẫu dưới Nyquist làm alias tần số cao thành thấp — nhầm lẫn không đảo trong dữ liệu rời rạc.
- Nén giữ hệ số lớn trong cơ sở Fourier/DCT nơi năng lượng tập trung.
""",
    },
    {
        "slug": "differential-equations-applications",
        "title": "Differential Equations → Applications",
        "chapter": "03",
        "order": 9,
        "en": EN3 / "21-01-01-03_09_Differential_Equations_Applications.md",
        "vi": VI3 / "21-01-01-03_09_Differential_Equations_Applications.md",
        "status": "Classical modeling language; numerics dominate industrial practice.",
        "primary": {
            "title": "MIT Learn Differential Equations (Strang & Moler)",
            "speaker": "Gilbert Strang, Cleve Moler",
            "url": "https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/",
            "duration": "video series",
            "role": "FOUNDATION + CORE",
            "level": "2–3",
        },
        "videos": [
            ("V1", "MIT RES.18-009 — Learn Differential Equations (Strang & Moler)", "FOUNDATION", "https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/"),
            ("V2", "MIT Learn DE YouTube playlist", "FOUNDATION", "https://www.youtube.com/playlist?list=PLUl4u3cNGP63oTpyxCMLKt_JmB0WtSZfG"),
            ("V3", "MIT 18.03 Differential Equations video lectures (Mattuck)", "FOUNDATION", "https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/"),
            ("V4", "3Blue1Brown — Differential equations series hub", "INTUITION", "https://www.3blue1brown.com/topics/differential-equations"),
            ("V5", "3Blue1Brown — Differential equations, a visual introduction", "ORIENTATION", "https://www.youtube.com/watch?v=p_di4Zn4wz4"),
            ("V6", "Strang — First-order equations (2.087 sample)", "CORE", "https://www.youtube.com/watch?v=4X0SGGrXDiI"),
            ("V7", "Numerical ODE solvers culture (Runge–Kutta explainers)", "INTUITION", "https://www.youtube.com/results?search_query=runge+kutta+explained"),
            ("V8", "Heat equation derivations (popular PDE intros)", "CORE", "https://www.youtube.com/results?search_query=heat+equation+derivation+explained"),
        ],
        "secondary_videos": [
            ("V9", "Strogatz Nonlinear Dynamics lectures / book culture", "SECONDARY", "https://www.youtube.com/results?search_query=strogatz+nonlinear+dynamics+lecture"),
        ],
        "papers_web": [
            ("P1", "Hairer, Nørsett, Wanner — Solving Ordinary Differential Equations", "https://link.springer.com/book/10.1007/978-3-540-78862-1"),
            ("W1", "Wikipedia — Ordinary differential equation", "https://en.wikipedia.org/wiki/Ordinary_differential_equation"),
            ("W2", "Wikipedia — Partial differential equation", "https://en.wikipedia.org/wiki/Partial_differential_equation"),
            ("W3", "Wikipedia — Well-posed problem", "https://en.wikipedia.org/wiki/Well-posed_problem"),
            ("W4", "MIT OCW 18.03", "https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/"),
            ("W5", "Strang — Differential Equations and Linear Algebra resources", "https://math.mit.edu/~gs/dela/"),
        ],
        "defs": [
            ("ODE", r"Unknown function of one independent variable (often time)."),
            ("PDE", r"Unknown field depending on space and/or time; e.g. heat $$u_t=k u_{xx}$$."),
            ("Well-posedness", r"Existence, uniqueness, continuous dependence (Hadamard)."),
            ("Stiffness", r"Widely separated timescales; explicit integrators may fail."),
        ],
        "takeaways": [
            "Closed forms are rare; well-posedness + numerics are the industrial path.",
            "Linearity gives superposition; nonlinearity gives most real phenomena.",
            "Stability of the *method* differs from stability of the *equation*.",
            "Digital twins couple DE models with data assimilation and control.",
        ],
        "path": [
            ("0 Orientation", "3B1B DE visual intro", "Slope fields; phase portraits."),
            ("1 Foundation", "Strang/Moler series + 18.03 sample", "First-order; systems; Laplace optional."),
            ("2 Numerics", "RK and stiffness explainers", "Why adaptive steps matter."),
            ("3 Course", "Ch.3 DE essay + calculus essay", "Catalog + well-posedness + twins."),
        ],
        "en_inject_knowledge": """### DE modeling slogans (from video research)

Primary university path: [Strang & Moler Learn DE](https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/) and [3B1B DE intro](https://www.youtube.com/watch?v=p_di4Zn4wz4).

- **Modeling contract:** state variables + laws for rates → DE + initial/boundary data.
- **Hadamard:** existence, uniqueness, continuous dependence — all three matter for engineering trust.
- Most industrial solutions are numerical; analysis still decides stability, stiffness, and validity.
""",
        "vi_inject_knowledge": """### Khẩu hiệu mô hình PTVi phân (từ nghiên cứu video)

Lộ trình đại học: [Strang & Moler Learn DE](https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/) và [3B1B DE intro](https://www.youtube.com/watch?v=p_di4Zn4wz4).

- **Hợp đồng mô hình:** biến trạng thái + luật tốc độ → PT + dữ liệu ban đầu/biên.
- **Hadamard:** tồn tại, duy nhất, phụ thuộc liên tục — cả ba cần cho tin cậy kỹ thuật.
- Hầu hết lời giải công nghiệp là số; phân tích vẫn quyết định ổn định, stiff, và tính hợp lệ.
""",
    },
    # ===== CHAPTER 04 =====
    {
        "slug": "infinity",
        "title": "Infinity",
        "chapter": "04",
        "order": 2,
        "en": EN4 / "21-01-01-04_02_Infinity.md",
        "vi": VI4 / "21-01-01-04_02_Infinity.md",
        "status": "Classical set theory core; CH independent of ZFC.",
        "primary": {
            "title": "Infinity is bigger than you think — Numberphile",
            "speaker": "James Grime (Numberphile)",
            "url": "https://www.youtube.com/watch?v=elvOZm0d4H0",
            "duration": "~8 min",
            "role": "ORIENTATION (cardinal sizes)",
            "level": "1",
        },
        "videos": [
            ("V1", "Numberphile — Infinity is bigger than you think", "ORIENTATION", "https://www.youtube.com/watch?v=elvOZm0d4H0"),
            ("V2", "Numberphile page for V1", "ORIENTATION", "https://www.numberphile.com/videos/infinity-is-bigger-than-you-think"),
            ("V3", "Vsauce — How To Count Past Infinity", "CORE", "https://www.youtube.com/watch?v=SrU9YDoXE88"),
            ("V4", "Numberphile — Infinite fractions / related infinity culture", "INTUITION", "https://www.youtube.com/results?search_query=numberphile+infinity"),
            ("V5", "Stand-up Maths / Matt Parker infinity talks", "ORIENTATION", "https://www.youtube.com/results?search_query=standupmaths+infinity"),
            ("V6", "Harvard / set theory intro lectures (open course search)", "FOUNDATION", "https://www.youtube.com/results?search_query=introduction+to+set+theory+lecture+cantor"),
            ("V7", "PBS Infinite Series — sizes of infinity (archive culture)", "INTUITION", "https://www.youtube.com/results?search_query=pbs+infinite+series+infinity"),
            ("V8", "Course sibling: Cantor diagonal essay (internal)", "CORE", "COURSE"),
        ],
        "secondary_videos": [
            ("V9", "Numberphile — Hilbert’s Hotel", "SECONDARY", "https://www.youtube.com/results?search_query=numberphile+hilbert+hotel"),
        ],
        "papers_web": [
            ("P1", "Stillwell — Roads to Infinity", "https://www.routledge.com/Roads-to-Infinity-The-Mathematics-of-Truth-and-Proof/Stillwell/p/book/9781568814667"),
            ("W1", "Wikipedia — Cardinality", "https://en.wikipedia.org/wiki/Cardinality"),
            ("W2", "Wikipedia — Cantor's diagonal argument", "https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument"),
            ("W3", "Wikipedia — Continuum hypothesis", "https://en.wikipedia.org/wiki/Continuum_hypothesis"),
            ("W4", "Wikipedia — Hilbert's paradox of the Grand Hotel", "https://en.wikipedia.org/wiki/Hilbert%27s_paradox_of_the_Grand_Hotel"),
            ("W5", "Stanford Encyclopedia — Continuum Hypothesis", "https://plato.stanford.edu/entries/continuum-hypothesis/"),
        ],
        "defs": [
            ("Countable", r"In bijection with $$\mathbb{N}$$ (or finite)."),
            ("Uncountable", r"Not countable; e.g. $$\mathbb{R}$$ via diagonalization."),
            ("Cardinal hierarchy", r"$$|\mathbb{N}|=\aleph_0 < 2^{\aleph_0}=|\mathbb{R}| \le \cdots$$; power set strictly increases size."),
            ("CH", r"No cardinal strictly between $$\aleph_0$$ and $$2^{\aleph_0}$$; independent of ZFC."),
        ],
        "takeaways": [
            "Density ≠ cardinality: $$\mathbb{Q}$$ dense yet countable.",
            "Potential vs actual infinity: process language vs completed sets.",
            "Ordinals vs cardinals: $$\omega+1$$ differs as order type, not as size.",
            "CH is independence, not “unsolved like RH.”",
        ],
        "path": [
            ("0 Orientation", "Numberphile bigger infinity", "Different sizes exist."),
            ("1 Core", "Vsauce count past infinity", "Ordinals + hotels + diagonal."),
            ("2 Formal", "Ch.4 infinity + Ch.5 Cantor essays", "Write diagonal carefully."),
            ("3 Stretch", "SEP continuum hypothesis", "Independence culture."),
        ],
        "en_inject_knowledge": """### Infinity video slogans (from research)

Watch [Numberphile — Infinity is bigger than you think](https://www.youtube.com/watch?v=elvOZm0d4H0) then [Vsauce — How To Count Past Infinity](https://www.youtube.com/watch?v=SrU9YDoXE88).

- **Two sizes minimum:** $$|\\mathbb{N}|<|\\mathbb{R}|$$ via diagonalization.
- **Hilbert’s hotel** is about countable infinity’s room to rearrange — not a physical hotel.
- **CH** is independent of standard set axioms; that is a different status from open arithmetic conjectures.
""",
        "vi_inject_knowledge": """### Khẩu hiệu vô hạn (từ nghiên cứu video)

Xem [Numberphile — Infinity is bigger than you think](https://www.youtube.com/watch?v=elvOZm0d4H0) rồi [Vsauce — How To Count Past Infinity](https://www.youtube.com/watch?v=SrU9YDoXE88).

- **Ít nhất hai cỡ:** $$|\\mathbb{N}|<|\\mathbb{R}|$$ nhờ chéo hóa.
- **Khách sạn Hilbert** nói về khả năng sắp xếp lại vô hạn đếm được — không phải khách sạn thật.
- **CH** độc lập với tiên đề tập hợp chuẩn; khác trạng thái “mở” kiểu giả thuyết số học.
""",
    },
    {
        "slug": "fractals",
        "title": "Fractals",
        "chapter": "04",
        "order": 3,
        "en": EN4 / "21-01-01-04_03_Fractals.md",
        "vi": VI4 / "21-01-01-04_03_Fractals.md",
        "status": "Classical fractal geometry + complex dynamics pictures.",
        "primary": {
            "title": "What's so special about the Mandelbrot Set? — Numberphile",
            "speaker": "Ben Sparks (Numberphile)",
            "url": "https://www.youtube.com/watch?v=FFftmWSzgmk",
            "duration": "~17 min",
            "role": "CORE orientation",
            "level": "1–2",
        },
        "videos": [
            ("V1", "Numberphile — What's so special about the Mandelbrot Set?", "CORE", "https://www.youtube.com/watch?v=FFftmWSzgmk"),
            ("V2", "Numberphile — Chaos Game (Sierpiński)", "INTUITION", "https://www.youtube.com/watch?v=kbKtFN71Lfs"),
            ("V3", "Numberphile — Space-Filling Curves", "INTUITION", "https://www.youtube.com/watch?v=x-DgL49CFlM"),
            ("V4", "3Blue1Brown / Mandelbrot deep zooms culture", "ORIENTATION", "https://www.youtube.com/results?search_query=3blue1brown+mandelbrot"),
            ("V5", "Veritasium — Mandelbrot / fractal-related explainers", "ORIENTATION", "https://www.youtube.com/results?search_query=veritasium+mandelbrot"),
            ("V6", "Numberphile — Fractal dimension culture (1.58-D objects)", "CORE", "https://www.numberphile.com/videos/a-1-58-dimensional-object"),
            ("V7", "MIT / university fractal geometry survey lectures", "FOUNDATION", "https://www.youtube.com/results?search_query=fractal+geometry+lecture+mandelbrot"),
            ("V8", "Dynamics of Julia sets popular lectures", "CORE", "https://www.youtube.com/results?search_query=julia+set+explained+mathematics"),
        ],
        "secondary_videos": [
            ("V9", "Mandelbrot documentary / interview clips", "SECONDARY", "https://www.youtube.com/results?search_query=benoit+mandelbrot+interview"),
        ],
        "papers_web": [
            ("P1", "Falconer — Fractal Geometry: Mathematical Foundations and Applications", "https://www.wiley.com/en-us/Fractal+Geometry%3A+Mathematical+Foundations+and+Applications%2C+3rd+Edition-p-9781119942399"),
            ("W1", "Wikipedia — Fractal", "https://en.wikipedia.org/wiki/Fractal"),
            ("W2", "Wikipedia — Mandelbrot set", "https://en.wikipedia.org/wiki/Mandelbrot_set"),
            ("W3", "Wikipedia — Hausdorff dimension", "https://en.wikipedia.org/wiki/Hausdorff_dimension"),
            ("W4", "Wikipedia — Julia set", "https://en.wikipedia.org/wiki/Julia_set"),
            ("W5", "Wikipedia — Cantor set", "https://en.wikipedia.org/wiki/Cantor_set"),
        ],
        "defs": [
            ("Self-similarity", r"Structure recurring under scaling (exact or statistical)."),
            ("Cantor set", r"Middle-third removals; uncountable, measure zero, nowhere dense."),
            ("Box/Hausdorff dimension", r"Scaling exponents capturing intermediate “size.”"),
            ("Mandelbrot", r"Parameters $$c$$ where $$z\mapsto z^2+c$$ orbit of $$0$$ stays bounded."),
        ],
        "takeaways": [
            "Fractal ≠ “pretty zoom only”; dimension theory is the math backbone.",
            "Self-similarity can be exact (Koch) or statistical (coastlines).",
            "Mandelbrot encodes a dictionary of Julia sets.",
            "Space-filling curves show dimension and topology can surprise.",
        ],
        "path": [
            ("0 Orientation", "Numberphile Mandelbrot + Chaos Game", "Pictures with rules."),
            ("1 Foundations", "Cantor/Koch constructions in essay", "Compute dimensions on paper."),
            ("2 Dynamics", "Julia + Mandelbrot videos", "Escape-time algorithm idea."),
            ("3 Course", "Ch.4 fractals + strange geometry", "Link to dimension and embeddings."),
        ],
        "en_inject_knowledge": """### Fractal video slogans (from research)

Primary: [Numberphile Mandelbrot](https://www.youtube.com/watch?v=FFftmWSzgmk), [Chaos Game](https://www.youtube.com/watch?v=kbKtFN71Lfs).

- **Escape-time pictures** are algorithms, not definitions — the set is a precise subset of the plane/parameter space.
- **Dimension** can be non-integer; box-counting is an experimental cousin of Hausdorff dimension.
- Chaos game shows how random iteration can still produce rigid fractal attractors.
""",
        "vi_inject_knowledge": """### Khẩu hiệu fractal (từ nghiên cứu video)

Chính: [Numberphile Mandelbrot](https://www.youtube.com/watch?v=FFftmWSzgmk), [Chaos Game](https://www.youtube.com/watch?v=kbKtFN71Lfs).

- **Ảnh escape-time** là thuật toán, không phải định nghĩa — tập là tập con chính xác của mặt phẳng/không gian tham số.
- **Số chiều** có thể không nguyên; box-counting là họ hàng thực nghiệm của chiều Hausdorff.
- Chaos game cho thấy lặp ngẫu nhiên vẫn có thể tạo attractor fractal cứng.
""",
    },
    {
        "slug": "symmetry",
        "title": "Symmetry",
        "chapter": "04",
        "order": 4,
        "en": EN4 / "21-01-01-04_04_Symmetry.md",
        "vi": VI4 / "21-01-01-04_04_Symmetry.md",
        "status": "Group theory as the algebra of symmetry; Noether idea-level.",
        "primary": {
            "title": "Group theory / symmetry educational videos",
            "speaker": "3Blue1Brown / Numberphile / university",
            "url": "https://www.youtube.com/watch?v=mH0oCDa74tE",
            "duration": "varies",
            "role": "ORIENTATION",
            "level": "1–2",
        },
        "videos": [
            ("V1", "3Blue1Brown — Group theory & symmetry culture (Euler’s formula / groups)", "ORIENTATION", "https://www.youtube.com/watch?v=mH0oCDa74tE"),
            ("V2", "Numberphile — Symmetry / groups videos", "ORIENTATION", "https://www.youtube.com/results?search_query=numberphile+symmetry+group"),
            ("V3", "Numberphile — Wallpaper patterns / crystallography culture", "INTUITION", "https://www.youtube.com/results?search_query=numberphile+wallpaper+group"),
            ("V4", "Visual Group Theory (Carter) lecture-style videos", "FOUNDATION", "https://www.youtube.com/results?search_query=visual+group+theory+carter"),
            ("V5", "MIT OCW abstract algebra sample lectures", "FOUNDATION", "https://ocw.mit.edu/search/?q=abstract+algebra"),
            ("V6", "Noether’s theorem popular physics-math explainers", "CORE idea", "https://www.youtube.com/results?search_query=noether+theorem+explained"),
            ("V7", "Galois theory intuitive overviews", "FRONTIER lite", "https://www.youtube.com/results?search_query=galois+theory+explained+visually"),
            ("V8", "Stand-up Maths symmetry / packing talks", "ORIENTATION", "https://www.youtube.com/results?search_query=standupmaths+symmetry"),
        ],
        "secondary_videos": [
            ("V9", "Socratica / abstract algebra group theory playlist", "SECONDARY", "https://www.youtube.com/results?search_query=socratica+group+theory"),
        ],
        "papers_web": [
            ("P1", "Armstrong — Groups and Symmetry (Springer)", "https://link.springer.com/book/10.1007/978-1-4757-4034-9"),
            ("W1", "Wikipedia — Symmetry group", "https://en.wikipedia.org/wiki/Symmetry_group"),
            ("W2", "Wikipedia — Wallpaper group", "https://en.wikipedia.org/wiki/Wallpaper_group"),
            ("W3", "Wikipedia — Noether's theorem", "https://en.wikipedia.org/wiki/Noether%27s_theorem"),
            ("W4", "Wikipedia — Galois theory", "https://en.wikipedia.org/wiki/Galois_theory"),
            ("W5", "Wikipedia — Crystallographic restriction theorem", "https://en.wikipedia.org/wiki/Crystallographic_restriction_theorem"),
        ],
        "defs": [
            ("Symmetry of an object", r"A transformation preserving relevant structure; they form a group under composition."),
            ("Group axioms", r"Associativity, identity, inverses (closure)."),
            ("Wallpaper groups", r"17 plane periodic symmetry types."),
            ("Noether slogan", r"Continuous symmetries of the action ↔ conservation laws."),
        ],
        "takeaways": [
            "Symmetry is not only “looks balanced”; it is an algebraic group of structure-preserving maps.",
            "Crystallographic restriction: not all rotational orders appear in periodic plane patterns.",
            "Galois: symmetries of roots control solvability by radicals.",
            "Noether links symmetry to conservation — physics pays rent on group theory.",
        ],
        "path": [
            ("0 Orientation", "3B1B / Numberphile symmetry videos", "Transformations compose."),
            ("1 Groups", "Visual group theory samples", "Cayley diagrams intuition."),
            ("2 Geometry", "Wallpaper + restriction", "17 types; no order-5 lattice rotation."),
            ("3 Course", "Ch.4 symmetry essay", "Noether + Galois slogans only."),
        ],
        "en_inject_knowledge": """### Symmetry slogans (from video research)

- A symmetry is an invertible structure-preserving map; the collection is a **group**.
- Wallpaper classification (17 groups) is a finished classical theorem with living design consequences.
- Noether: symmetry of the laws → conserved quantities (idea-level in this course).
""",
        "vi_inject_knowledge": """### Khẩu hiệu đối xứng (từ nghiên cứu video)

- Đối xứng là ánh xạ bảo toàn cấu trúc khả nghịch; tập hợp chúng là **nhóm**.
- Phân loại wallpaper (17 nhóm) là định lý cổ điển hoàn chỉnh, vẫn sống trong thiết kế.
- Noether: đối xứng của luật → đại lượng bảo toàn (mức khẩu hiệu trong khóa này).
""",
    },
    {
        "slug": "chaos",
        "title": "Chaos",
        "chapter": "04",
        "order": 5,
        "en": EN4 / "21-01-01-04_05_Chaos.md",
        "vi": VI4 / "21-01-01-04_05_Chaos.md",
        "status": "Classical nonlinear dynamics; active applied modeling.",
        "primary": {
            "title": "Chaos theory educational core (logistic + Lorenz)",
            "speaker": "Veritasium / Strogatz culture / Numberphile",
            "url": "https://www.youtube.com/watch?v=fDek6cYijxI",
            "duration": "~12+ min",
            "role": "ORIENTATION",
            "level": "1–2",
        },
        "videos": [
            ("V1", "Veritasium — Chaos: The Science of the Butterfly Effect", "ORIENTATION", "https://www.youtube.com/watch?v=fDek6cYijxI"),
            ("V2", "Numberphile — Chaos Game", "INTUITION", "https://www.youtube.com/watch?v=kbKtFN71Lfs"),
            ("V3", "Strogatz — Nonlinear Dynamics lectures / Cornell culture", "FOUNDATION", "https://www.youtube.com/results?search_query=strogatz+nonlinear+dynamics+lecture"),
            ("V4", "Logistic map bifurcation diagram explainers", "CORE", "https://www.youtube.com/results?search_query=logistic+map+bifurcation+diagram+explained"),
            ("V5", "Lorenz attractor visual lectures", "CORE", "https://www.youtube.com/results?search_query=lorenz+attractor+explained+mathematics"),
            ("V6", "3Blue1Brown / related dynamics visuals", "INTUITION", "https://www.youtube.com/results?search_query=3blue1brown+differential+equations+chaos"),
            ("V7", "Feigenbaum constant popular math videos", "FRONTIER lite", "https://www.youtube.com/results?search_query=feigenbaum+constant+explained"),
            ("V8", "MIT nonlinear dynamics / chaos OCW search", "FOUNDATION", "https://ocw.mit.edu/search/?q=chaos+nonlinear"),
        ],
        "secondary_videos": [
            ("V9", "Gleick *Chaos* documentary clips (historical)", "SECONDARY", "https://www.youtube.com/results?search_query=james+gleick+chaos+documentary"),
        ],
        "papers_web": [
            ("P1", "Strogatz — Nonlinear Dynamics and Chaos", "https://www.stevenstrogatz.com/books/nonlinear-dynamics-and-chaos-with-applications-to-physics-biology-chemistry-and-engineering"),
            ("P2", "Lorenz 1963 — Deterministic Nonperiodic Flow", "https://journals.ametsoc.org/view/journals/atsc/20/2/1520-0469_1963_020_0130_dnf_2_0_co_2.xml"),
            ("W1", "Wikipedia — Chaos theory", "https://en.wikipedia.org/wiki/Chaos_theory"),
            ("W2", "Wikipedia — Logistic map", "https://en.wikipedia.org/wiki/Logistic_map"),
            ("W3", "Wikipedia — Lorenz system", "https://en.wikipedia.org/wiki/Lorenz_system"),
            ("W4", "Wikipedia — Lyapunov exponent", "https://en.wikipedia.org/wiki/Lyapunov_exponent"),
            ("W5", "Wikipedia — Feigenbaum constants", "https://en.wikipedia.org/wiki/Feigenbaum_constants"),
        ],
        "defs": [
            ("Sensitive dependence", r"Nearby initial conditions separate to macroscopic distance."),
            ("Logistic map", r"$$x_{n+1}=r x_n(1-x_n)$$ on $$[0,1]$$."),
            ("Lyapunov exponent", r"Average log expansion rate along an orbit."),
            ("Strange attractor", r"Attracting set with sensitive dynamics; often fractal geometry."),
        ],
        "takeaways": [
            "Deterministic ≠ predictable at long horizons under sensitivity.",
            "Chaos is not pure randomness; attractors carry structure.",
            "Period-doubling and Feigenbaum universality transcend specific formulas.",
            "Weather chaos is about forecast horizon, not “no equations.”",
        ],
        "path": [
            ("0 Orientation", "Veritasium butterfly effect", "Sensitivity slogan."),
            ("1 Lab", "Logistic map numerics + bifurcation videos", "Plot attractors vs $$r$$."),
            ("2 Flows", "Lorenz attractor lectures", "Bounded yet unpredictable detail."),
            ("3 Course", "Ch.4 chaos essay + Ch.7 iteration studio", "Lyapunov definition practice."),
        ],
        "en_inject_knowledge": """### Chaos slogans (from video research)

Start with [Veritasium — Chaos / butterfly effect](https://www.youtube.com/watch?v=fDek6cYijxI), then logistic and Lorenz explainers.

- **Deterministic chaos:** the rule is fixed; finite precision still loses the future.
- **Logistic map** is the minimal laboratory: fixed points → period doubling → chaos → windows.
- **Positive Lyapunov exponent** quantifies exponential separation (with technical caveats).
""",
        "vi_inject_knowledge": """### Khẩu hiệu hỗn độn (từ nghiên cứu video)

Bắt đầu [Veritasium — Chaos / butterfly effect](https://www.youtube.com/watch?v=fDek6cYijxI), rồi logistic và Lorenz.

- **Hỗn độn tất định:** luật cố định; độ chính xác hữu hạn vẫn mất tương lai.
- **Logistic map** là phòng thí nghiệm tối thiểu: điểm cố định → nhân đôi chu kỳ → hỗn độn → cửa sổ.
- **Số mũ Lyapunov dương** định lượng tách mũ (kèm điều kiện kỹ thuật).
""",
    },
    {
        "slug": "strange-geometry",
        "title": "Strange Geometry",
        "chapter": "04",
        "order": 6,
        "en": EN4 / "21-01-01-04_06_Strange_Geometry.md",
        "vi": VI4 / "21-01-01-04_06_Strange_Geometry.md",
        "status": "Classical pathologies and topological surprises.",
        "primary": {
            "title": "The Banach–Tarski Paradox — Vsauce",
            "speaker": "Vsauce",
            "url": "https://www.youtube.com/watch?v=s86-Z-CbaHA",
            "duration": "~24 min",
            "role": "CORE popular (with axiom-of-choice hygiene)",
            "level": "1–2",
        },
        "videos": [
            ("V1", "Vsauce — The Banach–Tarski Paradox", "CORE", "https://www.youtube.com/watch?v=s86-Z-CbaHA"),
            ("V2", "Numberphile — Unexpected Shapes / Möbius (Tokieda)", "ORIENTATION", "https://www.youtube.com/watch?v=wKV0GYvR2X8"),
            ("V3", "Numberphile — An Unexpected Twist on Möbius Strips", "INTUITION", "https://www.youtube.com/watch?v=izIKV98Awnw"),
            ("V4", "Numberphile — Space-Filling Curves", "CORE", "https://www.youtube.com/watch?v=x-DgL49CFlM"),
            ("V5", "Alexander horned sphere visual topology talks", "FRONTIER lite", "https://www.youtube.com/results?search_query=alexander+horned+sphere+explained"),
            ("V6", "Klein bottle popular math videos", "ORIENTATION", "https://www.youtube.com/results?search_query=klein+bottle+numberphile"),
            ("V7", "Hilbert curve / Peano curve algorithm visuals", "INTUITION", "https://www.youtube.com/results?search_query=hilbert+curve+explained"),
            ("V8", "Axiom of choice explained carefully (philosophy-math)", "HYGIENE", "https://www.youtube.com/results?search_query=axiom+of+choice+explained+banach+tarski"),
        ],
        "secondary_videos": [
            ("V9", "Tadashi Tokieda topology demos (Numberphile playlist)", "SECONDARY", "https://www.youtube.com/results?search_query=tadashi+tokieda+numberphile"),
        ],
        "papers_web": [
            ("P1", "Wagon — The Banach–Tarski Paradox (Cambridge)", "https://www.cambridge.org/core/books/banachtarski-paradox/"),
            ("W1", "Wikipedia — Möbius strip", "https://en.wikipedia.org/wiki/M%C3%B6bius_strip"),
            ("W2", "Wikipedia — Space-filling curve", "https://en.wikipedia.org/wiki/Space-filling_curve"),
            ("W3", "Wikipedia — Banach–Tarski paradox", "https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox"),
            ("W4", "Wikipedia — Alexander horned sphere", "https://en.wikipedia.org/wiki/Alexander_horned_sphere"),
            ("W5", "Wikipedia — Axiom of choice", "https://en.wikipedia.org/wiki/Axiom_of_choice"),
        ],
        "defs": [
            ("Möbius strip", r"Non-orientable surface with one side and one boundary component."),
            ("Space-filling curve", r"Continuous surjection $$[0,1]\to[0,1]^2$$ (Peano, Hilbert)."),
            ("Banach–Tarski", r"Ball finite-equidecomposable to two balls via AC; non-measurable pieces."),
        ],
        "takeaways": [
            "Local geometric normalcy can fail globally (one-sided surfaces; wild embeddings).",
            "Continuous images can raise dimension (space-filling curves).",
            "Banach–Tarski needs AC and non-measurable sets — not a physical dissection.",
            "Pathologies guide which regularity hypotheses theorems need.",
        ],
        "path": [
            ("0 Orientation", "Möbius Numberphile", "Make one; cut it."),
            ("1 Paradox", "Vsauce Banach–Tarski", "AC + non-measurable hygiene."),
            ("2 Curves", "Space-filling Numberphile", "Continuity ≠ dimension preservation."),
            ("3 Course", "Ch.4 strange geometry essay", "Taxonomy of strangeness."),
        ],
        "en_inject_knowledge": """### Strange geometry hygiene (from video research)

- [Vsauce Banach–Tarski](https://www.youtube.com/watch?v=s86-Z-CbaHA) is excellent culture; remember pieces are not physical volumes.
- Möbius demos ([Tokieda](https://www.youtube.com/watch?v=wKV0GYvR2X8)) train non-orientability better than definitions alone.
- Space-filling curves: continuous + surjective can still be nowhere injective-friendly; dimension theory is subtle.
""",
        "vi_inject_knowledge": """### Vệ sinh hình học lạ (từ nghiên cứu video)

- [Vsauce Banach–Tarski](https://www.youtube.com/watch?v=s86-Z-CbaHA) hay về văn hóa; nhớ các mảnh không phải thể tích vật lý.
- Demo Möbius ([Tokieda](https://www.youtube.com/watch?v=wKV0GYvR2X8)) dạy non-orientability tốt hơn định nghĩa suông.
- Đường lấp đầy không gian: liên tục + toàn ánh vẫn tinh vi về chiều.
""",
    },
    {
        "slug": "paradoxes",
        "title": "Paradoxes",
        "chapter": "04",
        "order": 7,
        "en": EN4 / "21-01-01-04_07_Paradoxes.md",
        "vi": VI4 / "21-01-01-04_07_Paradoxes.md",
        "status": "Foundational and semantic paradoxes; resolutions via rigor.",
        "primary": {
            "title": "Paradoxes survey path (Zeno, Russell, semantic)",
            "speaker": "Numberphile / Vsauce / university",
            "url": "https://www.youtube.com/watch?v=u7Z9UnWOJNY",
            "duration": "varies",
            "role": "ORIENTATION",
            "level": "1–2",
        },
        "videos": [
            ("V1", "Numberphile — Zeno's Paradox", "ORIENTATION", "https://www.youtube.com/watch?v=u7Z9UnWOJNY"),
            ("V2", "Vsauce — The Banach–Tarski Paradox (measure paradox cousin)", "CORE", "https://www.youtube.com/watch?v=s86-Z-CbaHA"),
            ("V3", "Russell's paradox explainers (set theory)", "CORE", "https://www.youtube.com/results?search_query=russell+paradox+explained"),
            ("V4", "Veritasium / Zeno and infinity physics-math crossovers", "INTUITION", "https://www.youtube.com/results?search_query=veritasium+zeno+paradox"),
            ("V5", "Liar paradox / semantic paradox lectures", "CORE", "https://www.youtube.com/results?search_query=liar+paradox+explained+logic"),
            ("V6", "Hilbert hotel as infinity paradox culture", "ORIENTATION", "https://www.youtube.com/results?search_query=hilbert+hotel+numberphile"),
            ("V7", "Supertasks popular math-philosophy videos", "INTUITION", "https://www.youtube.com/results?search_query=supertask+thomson+lamp"),
            ("V8", "Course links: infinity + Gödel essays", "FOUNDATION", "COURSE"),
        ],
        "secondary_videos": [
            ("V9", "Unexpected hanging / unexpected exam paradox discussions", "SECONDARY", "https://www.youtube.com/results?search_query=unexpected+hanging+paradox"),
        ],
        "papers_web": [
            ("P1", "Stanford Encyclopedia — Paradoxes and Contemporary Logic", "https://plato.stanford.edu/entries/paradoxes-contemporary-logic/"),
            ("W1", "Wikipedia — Zeno's paradoxes", "https://en.wikipedia.org/wiki/Zeno%27s_paradoxes"),
            ("W2", "Wikipedia — Russell's paradox", "https://en.wikipedia.org/wiki/Russell%27s_paradox"),
            ("W3", "Wikipedia — Liar paradox", "https://en.wikipedia.org/wiki/Liar_paradox"),
            ("W4", "Wikipedia — Paradox", "https://en.wikipedia.org/wiki/Paradox"),
            ("W5", "SEP — Russell’s Paradox", "https://plato.stanford.edu/entries/russell-paradox/"),
        ],
        "defs": [
            ("Zeno (dichotomy)", r"Infinite halves before arrival; series resolution $$\\sum 2^{-n}<\\infty$$."),
            ("Russell", r"$$R=\{x:x\\notin x\}$$ leads to $$R\\in R\\iff R\\notin R$$ in naive comprehension."),
            ("Semantic paradox", r"Truth/self-reference puzzles (liar); hierarchy or non-classical fixes."),
        ],
        "takeaways": [
            "Paradoxes are engines of definition, not reasons to abandon math.",
            "Zeno meets convergent series and complete metric spaces.",
            "Russell kills naive comprehension; ZF/type theory respond.",
            "Not every “paradox” is the same species — taxonomy matters.",
        ],
        "path": [
            ("0 Orientation", "Numberphile Zeno", "Infinite tasks vs finite time."),
            ("1 Foundations", "Russell explainers + SEP", "Comprehension restriction."),
            ("2 Measure cousin", "Banach–Tarski hygiene", "AC pathologies."),
            ("3 Course", "Ch.4 paradoxes essay", "Write taxonomy table."),
        ],
        "en_inject_knowledge": """### Paradox taxonomy (from video research)

- **Motion/infinity:** Zeno → series and limits ([Numberphile Zeno](https://www.youtube.com/watch?v=u7Z9UnWOJNY)).
- **Set-theoretic:** Russell → axiomatic set theory.
- **Semantic:** liar → theories of truth.
- **Measure/geometry:** Banach–Tarski → measurable sets + AC.
Do not collapse these into one slogan.
""",
        "vi_inject_knowledge": """### Phân loại nghịch lý (từ nghiên cứu video)

- **Chuyển động/vô hạn:** Zeno → chuỗi và giới hạn ([Numberphile Zeno](https://www.youtube.com/watch?v=u7Z9UnWOJNY)).
- **Tập hợp:** Russell → lý thuyết tập tiên đề.
- **Ngữ nghĩa:** kẻ nói dối → lý thuyết chân lý.
- **Đo/hình:** Banach–Tarski → tập đo được + AC.
Đừng gộp thành một khẩu hiệu.
""",
    },
    {
        "slug": "higher-dimensions",
        "title": "Higher Dimensions",
        "chapter": "04",
        "order": 8,
        "en": EN4 / "21-01-01-04_08_Higher_Dimensions.md",
        "vi": VI4 / "21-01-01-04_08_Higher_Dimensions.md",
        "status": "Geometry of n-space; concentration and data curses.",
        "primary": {
            "title": "Higher-dimensional geometry popular + rigorous path",
            "speaker": "3Blue1Brown / Numberphile / Matt Parker",
            "url": "https://www.youtube.com/watch?v=zwAD6dRSVyI",
            "duration": "varies",
            "role": "ORIENTATION",
            "level": "1–2",
        },
        "videos": [
            ("V1", "3Blue1Brown — Thinking visually about higher dimensions", "ORIENTATION", "https://www.youtube.com/watch?v=zwAD6dRSVyI"),
            ("V2", "Numberphile — Hypercubes / higher-D culture", "ORIENTATION", "https://www.youtube.com/results?search_query=numberphile+hypercube+fourth+dimension"),
            ("V3", "Matt Parker — Things to Make and Do in the Fourth Dimension talks", "ORIENTATION", "https://www.youtube.com/results?search_query=matt+parker+fourth+dimension"),
            ("V4", "3Blue1Brown — Essence of linear algebra (n-D vectors)", "FOUNDATION", "https://www.youtube.com/watch?v=fNk_zzaMoSs"),
            ("V5", "Sphere packing / hypersphere volume explainers", "CORE", "https://www.youtube.com/results?search_query=hypersphere+volume+explained"),
            ("V6", "Concentration of measure popular/technical talks", "FRONTIER lite", "https://www.youtube.com/results?search_query=concentration+of+measure+explained"),
            ("V7", "Curse of dimensionality in ML explainers", "CORE applied", "https://www.youtube.com/results?search_query=curse+of+dimensionality+explained"),
            ("V8", "t-SNE / dimension reduction culture (contrast)", "SECONDARY", "https://www.youtube.com/results?search_query=tsne+explained+dimensionality"),
        ],
        "secondary_videos": [
            ("V9", "Carl Sagan Flatland / 4D cube classic clip culture", "SECONDARY", "https://www.youtube.com/results?search_query=carl+sagan+fourth+dimension"),
        ],
        "papers_web": [
            ("P1", "Blum, Hopcroft, Kannan — Foundations of Data Science (high-D chapters)", "https://www.cs.cornell.edu/jeh/book.pdf"),
            ("W1", "Wikipedia — Hypercube", "https://en.wikipedia.org/wiki/Hypercube"),
            ("W2", "Wikipedia — N-sphere", "https://en.wikipedia.org/wiki/N-sphere"),
            ("W3", "Wikipedia — Curse of dimensionality", "https://en.wikipedia.org/wiki/Curse_of_dimensionality"),
            ("W4", "Wikipedia — Concentration of measure", "https://en.wikipedia.org/wiki/Concentration_of_measure"),
            ("W5", "Wikipedia — Four-dimensional space", "https://en.wikipedia.org/wiki/Four-dimensional_space"),
        ],
        "defs": [
            ("n-cube", r"$$[0,1]^n$$; $$2^n$$ vertices."),
            ("n-sphere volume", r"Peaks then decays with dimension for unit radius — counterintuitive tables."),
            ("Concentration", r"Lipschitz functions of high-D measures nearly constant."),
        ],
        "takeaways": [
            "Coordinates scale: linear algebra does not stop at 3D.",
            "Volume and surface behave surprisingly as $$n$$ grows.",
            "Most mass of high-D balls lives near the equator/shell.",
            "Data algorithms feel geometry: distances concentrate; nearest neighbors weaken.",
        ],
        "path": [
            ("0 Orientation", "3B1B higher-D + Parker talks", "Projections and slices."),
            ("1 Counting", "Hypercube structure", "Vertices, edges, faces formulas."),
            ("2 Measure", "Hypersphere volume + concentration videos", "Tables and slogans."),
            ("3 Course", "Ch.4 higher-D + Ch.6 high-D geometry", "Curse vs blessing."),
        ],
        "en_inject_knowledge": """### Higher-D slogans (from video research)

- [3B1B higher dimensions](https://www.youtube.com/watch?v=zwAD6dRSVyI): prefer coordinates + linear maps over mystical “seeing 4D.”
- Hypersphere volume ratios vs dimension are a standard shock — compute a table once.
- Concentration of measure is why high-D probability often becomes almost deterministic.
""",
        "vi_inject_knowledge": """### Khẩu hiệu chiều cao (từ nghiên cứu video)

- [3B1B higher dimensions](https://www.youtube.com/watch?v=zwAD6dRSVyI): ưu tiên tọa độ + ánh xạ tuyến tính hơn “nhìn thấy 4D.”
- Tỉ lệ thể tích siêu cầu theo chiều là cú sốc chuẩn — hãy lập một bảng.
- Tập trung độ đo giải thích vì sao xác suất chiều cao thường gần tất định.
""",
    },
    {
        "slug": "minimal-surfaces",
        "title": "Minimal Surfaces",
        "chapter": "04",
        "order": 9,
        "en": EN4 / "21-01-01-04_09_Minimal_Surfaces.md",
        "vi": VI4 / "21-01-01-04_09_Minimal_Surfaces.md",
        "status": "Classical geometric analysis; deep modern theory (Colding–Minicozzi, etc.).",
        "primary": {
            "title": "Soap films / minimal surfaces educational path",
            "speaker": "Numberphile / university geometry",
            "url": "https://www.youtube.com/results?search_query=numberphile+soap+film+minimal+surface",
            "duration": "varies",
            "role": "ORIENTATION",
            "level": "1–3",
        },
        "videos": [
            ("V1", "Numberphile — Soap films / minimal surfaces culture", "ORIENTATION", "https://www.youtube.com/results?search_query=numberphile+soap+bubble+minimal"),
            ("V2", "Stand-up Maths / Parker soap film optimization demos", "ORIENTATION", "https://www.youtube.com/results?search_query=standupmaths+soap+film"),
            ("V3", "Plateau’s problem popular math videos", "CORE", "https://www.youtube.com/results?search_query=plateau+problem+minimal+surface"),
            ("V4", "Mean curvature flow / minimal surface university lectures", "FOUNDATION", "https://www.youtube.com/results?search_query=minimal+surfaces+lecture+mean+curvature"),
            ("V5", "Helicoid and catenoid classic visualizations", "INTUITION", "https://www.youtube.com/results?search_query=helicoid+catenoid+minimal+surface"),
            ("V6", "CMSA / IAS geometry seminar samples (advanced)", "FRONTIER", "https://www.youtube.com/results?search_query=minimal+surfaces+ias+lecture"),
            ("V7", "Calculus of variations soap film intros", "FOUNDATION", "https://www.youtube.com/results?search_query=calculus+of+variations+soap+film"),
            ("V8", "Course calculus essay variational section (internal)", "FOUNDATION", "COURSE"),
        ],
        "secondary_videos": [
            ("V9", "Architecture freeform / tensile structure math talks", "SECONDARY", "https://www.youtube.com/results?search_query=minimal+surface+architecture+tensile"),
        ],
        "papers_web": [
            ("P1", "Colding & Minicozzi — A Course in Minimal Surfaces (AMS)", "https://bookstore.ams.org/gsm-121"),
            ("W1", "Wikipedia — Minimal surface", "https://en.wikipedia.org/wiki/Minimal_surface"),
            ("W2", "Wikipedia — Plateau's problem", "https://en.wikipedia.org/wiki/Plateau%27s_problem"),
            ("W3", "Wikipedia — Mean curvature", "https://en.wikipedia.org/wiki/Mean_curvature"),
            ("W4", "Wikipedia — Catenoid", "https://en.wikipedia.org/wiki/Catenoid"),
            ("W5", "Wikipedia — Helicoid", "https://en.wikipedia.org/wiki/Helicoid"),
        ],
        "defs": [
            ("Minimal surface", r"Zero mean curvature (critical for area); soap films as physical models."),
            ("Plateau problem", r"Find least-area surface spanning a given boundary curve."),
            ("Catenoid / helicoid", r"Classical complete minimal surfaces in $$\mathbb{R}^3$$."),
        ],
        "takeaways": [
            "Minimal ≠ minimum area always globally; it is zero mean curvature / critical point language.",
            "Soap films approximate; singularities and topology matter mathematically.",
            "Variational PDE viewpoint links to Ch.3 calculus.",
            "Modern theory studies embeddedness, curvature estimates, and moduli.",
        ],
        "path": [
            ("0 Orientation", "Soap film demos", "Physical area minimization."),
            ("1 Classics", "Catenoid/helicoid videos", "Named examples."),
            ("2 Analysis", "Mean curvature lectures", "PDE form of minimality."),
            ("3 Course", "Ch.4 minimal surfaces essay", "Plateau statement + confusions."),
        ],
        "en_inject_knowledge": """### Minimal surface slogans (from video research)

- Physical soap films motivate **Plateau’s problem**; mathematics needs existence, regularity, and possible singularities.
- **Mean curvature zero** is the analytic definition most essays use.
- Catenoid and helicoid are the first museum of complete examples.
""",
        "vi_inject_knowledge": """### Khẩu hiệu mặt cực tiểu (từ nghiên cứu video)

- Màng xà phòng gợi **bài toán Plateau**; toán cần tồn tại, chính quy, và khả năng kỳ dị.
- **Độ cong trung bình không** là định nghĩa giải tích thường dùng.
- Catenoid và helicoid là bảo tàng ví dụ đầy đủ đầu tiên.
""",
    },
    {
        "slug": "tilings",
        "title": "Tilings",
        "chapter": "04",
        "order": 10,
        "en": EN4 / "21-01-01-04_10_Tilings.md",
        "vi": VI4 / "21-01-01-04_10_Tilings.md",
        "status": "Classical tessellations; aperiodic order; 2023 monotile breakthrough.",
        "primary": {
            "title": "Discovery of the Aperiodic Monotile — Numberphile",
            "speaker": "Craig Kaplan (Numberphile)",
            "url": "https://www.youtube.com/watch?v=_ZS3Oqg1AX0",
            "duration": "~31 min",
            "role": "FRONTIER + CORE",
            "level": "2",
        },
        "videos": [
            ("V1", "Numberphile — Discovery of the Aperiodic Monotile", "FRONTIER", "https://www.youtube.com/watch?v=_ZS3Oqg1AX0"),
            ("V2", "Numberphile — 5 and Penrose Tiling", "CORE", "https://www.youtube.com/watch?v=QTrM-UVcgBY"),
            ("V3", "Numberphile — A New Tile in Newtyle (periodic contrast)", "INTUITION", "https://www.youtube.com/watch?v=ArADlJx7SlU"),
            ("V4", "Veritasium — The Infinite Pattern That Never Repeats (Penrose)", "ORIENTATION", "https://www.youtube.com/watch?v=48sCx-wBs34"),
            ("V5", "Stand-up Maths aperiodic monotile coverage", "ORIENTATION", "https://www.youtube.com/results?search_query=standupmaths+hat+tile+aperiodic"),
            ("V6", "Wang tiles / undecidability popular CS-math talks", "FOUNDATION", "https://www.youtube.com/results?search_query=wang+tiles+undecidable"),
            ("V7", "Quasicrystals + Penrose connection lectures", "CORE", "https://www.youtube.com/results?search_query=quasicrystal+penrose+tiling+lecture"),
            ("V8", "Cambridge feature — tip of the hat monotile", "WEB/VIDEO cousin", "https://www.maths.cam.ac.uk/features/tip-hat-celebrating-aperiodic-monotile-discovery"),
        ],
        "secondary_videos": [
            ("V9", "IMA Penrose tiles demo", "SECONDARY", "https://www.youtube.com/watch?v=jJnEIjqbkR4"),
        ],
        "papers_web": [
            ("P1", "Smith, Myers, Kaplan, Goodman-Strauss — monotile papers (arXiv search)", "https://arxiv.org/search/?query=aperiodic+monotile+smith+kaplan&searchtype=all"),
            ("W1", "Wikipedia — Penrose tiling", "https://en.wikipedia.org/wiki/Penrose_tiling"),
            ("W2", "Wikipedia — Aperiodic tiling", "https://en.wikipedia.org/wiki/Aperiodic_tiling"),
            ("W3", "Wikipedia — Einstein problem (geometry)", "https://en.wikipedia.org/wiki/Einstein_problem"),
            ("W4", "Wikipedia — Wang tile", "https://en.wikipedia.org/wiki/Wang_tile"),
            ("W5", "Cambridge Maths — tip of the hat", "https://www.maths.cam.ac.uk/features/tip-hat-celebrating-aperiodic-monotile-discovery"),
            ("W6", "Wikipedia — Tessellation", "https://en.wikipedia.org/wiki/Tessellation"),
        ],
        "defs": [
            ("Tiling", r"Covering without gaps/overlaps by prototiles."),
            ("Periodic", r"Invariant under a lattice of translations."),
            ("Aperiodic set", r"Tiles the plane but only non-periodically."),
            ("Monotile / einstein", r"Single prototile forcing aperiodicity (hat/spectre story, 2023)."),
        ],
        "takeaways": [
            "Only three regular tessellations; many more irregular ones.",
            "Aperiodic ≠ disordered: Penrose order is strong and hierarchical.",
            "Tiling decidability fails in general (Berger).",
            "Hat/spectre: one shape can force global non-periodicity.",
        ],
        "path": [
            ("0 Orientation", "Veritasium never-repeats + Penrose Numberphile", "Fivefold motifs."),
            ("1 Breakthrough", "Numberphile monotile Kaplan", "Einstein problem resolved in public."),
            ("2 Logic", "Wang tiles undecidability videos", "Geometry encodes computation."),
            ("3 Course", "Ch.4 tilings essay", "Taxonomy + exercises."),
        ],
        "en_inject_knowledge": """### Tiling video slogans (from research)

Must-watch pair: [Veritasium Penrose](https://www.youtube.com/watch?v=48sCx-wBs34) and [Numberphile monotile](https://www.youtube.com/watch?v=_ZS3Oqg1AX0).

- **Penrose:** matching rules force aperiodicity with hierarchical inflation.
- **Hat/spectre (2023):** monohedral aperiodicity — the einstein problem’s public resolution arc.
- **Undecidability:** no algorithm decides arbitrary Wang tile sets.
""",
        "vi_inject_knowledge": """### Khẩu hiệu lát gạch (từ nghiên cứu video)

Cặp bắt buộc: [Veritasium Penrose](https://www.youtube.com/watch?v=48sCx-wBs34) và [Numberphile monotile](https://www.youtube.com/watch?v=_ZS3Oqg1AX0).

- **Penrose:** quy tắc khớp buộc phi tuần hoàn với phình/xẹp phân cấp.
- **Hat/spectre (2023):** một mảnh buộc phi tuần hoàn — cung công khai bài toán einstein.
- **Không quyết định được:** không có thuật toán cho mọi tập gạch Wang.
""",
    },
    {
        "slug": "impossible-shapes",
        "title": "Impossible Shapes",
        "chapter": "04",
        "order": 11,
        "en": EN4 / "21-01-01-04_11_Impossible_Shapes.md",
        "vi": VI4 / "21-01-01-04_11_Impossible_Shapes.md",
        "status": "Projective / perceptual inconsistency; discrete geometry language.",
        "primary": {
            "title": "Impossible objects / Penrose triangle educational path",
            "speaker": "Numberphile / psychology-math crossovers",
            "url": "https://www.youtube.com/results?search_query=numberphile+penrose+triangle+impossible",
            "duration": "varies",
            "role": "ORIENTATION",
            "level": "1",
        },
        "videos": [
            ("V1", "Numberphile — Impossible objects / Penrose triangle culture", "ORIENTATION", "https://www.youtube.com/results?search_query=numberphile+impossible+triangle"),
            ("V2", "Stand-up Maths impossible geometry demos", "ORIENTATION", "https://www.youtube.com/results?search_query=standupmaths+impossible+shape"),
            ("V3", "Escher mathematics documentaries / talks", "CORE culture", "https://www.youtube.com/results?search_query=escher+mathematics+lecture"),
            ("V4", "Necker cube / multistable perception science videos", "INTUITION", "https://www.youtube.com/results?search_query=necker+cube+explained"),
            ("V5", "Projective geometry intro lectures", "FOUNDATION", "https://www.youtube.com/results?search_query=projective+geometry+introduction+lecture"),
            ("V6", "Graphics / impossible 3D models from 2D projections", "CORE", "https://www.youtube.com/results?search_query=impossible+object+projection+computer+graphics"),
            ("V7", "Penrose stairs explainers", "ORIENTATION", "https://www.youtube.com/results?search_query=penrose+stairs+explained"),
            ("V8", "Course strange geometry sibling (internal)", "LINK", "COURSE"),
        ],
        "secondary_videos": [
            ("V9", "Optical illusion math museum talks", "SECONDARY", "https://www.youtube.com/results?search_query=optical+illusion+mathematics+museum"),
        ],
        "papers_web": [
            ("P1", "Penrose & Penrose — Impossible objects (classic note culture)", "https://en.wikipedia.org/wiki/Penrose_triangle"),
            ("W1", "Wikipedia — Penrose triangle", "https://en.wikipedia.org/wiki/Penrose_triangle"),
            ("W2", "Wikipedia — Impossible object", "https://en.wikipedia.org/wiki/Impossible_object"),
            ("W3", "Wikipedia — Penrose stairs", "https://en.wikipedia.org/wiki/Penrose_stairs"),
            ("W4", "Wikipedia — Necker cube", "https://en.wikipedia.org/wiki/Necker_cube"),
            ("W5", "Wikipedia — M. C. Escher", "https://en.wikipedia.org/wiki/M._C._Escher"),
        ],
        "defs": [
            ("Impossible object", r"2D drawing suggesting a 3D solid that cannot embed consistently in $$\mathbb{R}^3$$."),
            ("Local vs global", r"Each vertex/junction ok; global incidence or depth inconsistent."),
            ("Necker ambiguity", r"Multiple 3D interpretations of one line drawing."),
        ],
        "takeaways": [
            "Impossibility is about consistent 3D realization, not “bad art.”",
            "Projection loses depth; multiple preimages enable paradox drawings.",
            "Escher narrates closed loops of inconsistent ascent.",
            "Cognitive science and discrete geometry share the consistency language.",
        ],
        "path": [
            ("0 Orientation", "Penrose triangle + stairs videos", "See local-global split."),
            ("1 Perception", "Necker cube science", "Ambiguity vs impossibility."),
            ("2 Formal", "Essay consistency language", "Incidence constraints."),
            ("3 Course", "Ch.4 impossible shapes + tilings art links", "Compare Escher themes."),
        ],
        "en_inject_knowledge": """### Impossible shapes slogans (from video research)

- Local junctions can be fine while the global depth/orientation graph has a cycle contradiction.
- These are not the same as optical brightness illusions; the math issue is **geometric consistency under projection**.
- Escher’s staircases dramatize closed inconsistent monotony of ascent.
""",
        "vi_inject_knowledge": """### Khẩu hiệu hình bất khả (từ nghiên cứu video)

- Nút giao cục bộ có thể ổn trong khi đồ thị độ sâu/hướng toàn cục có chu trình mâu thuẫn.
- Khác ảo ảnh độ sáng; vấn đề toán là **tính nhất quán hình học dưới phép chiếu**.
- Cầu thang Escher kịch tính hóa vòng lên không nhất quán.
""",
    },
    {
        "slug": "emergence",
        "title": "Emergence",
        "chapter": "04",
        "order": 12,
        "en": EN4 / "21-01-01-04_12_Emergence.md",
        "vi": VI4 / "21-01-01-04_12_Emergence.md",
        "status": "Interdisciplinary math: CA, statistical mechanics, multi-agent systems.",
        "primary": {
            "title": "Inventing Game of Life (John Conway) — Numberphile",
            "speaker": "John Conway (Numberphile)",
            "url": "https://www.youtube.com/watch?v=R9Plq-D1gEk",
            "duration": "~11 min",
            "role": "ORIENTATION + CORE culture",
            "level": "1",
        },
        "videos": [
            ("V1", "Numberphile — Inventing Game of Life (Conway)", "CORE", "https://www.youtube.com/watch?v=R9Plq-D1gEk"),
            ("V2", "Numberphile / Life glider & complexity culture", "INTUITION", "https://www.youtube.com/results?search_query=numberphile+game+of+life+glider"),
            ("V3", "Veritasium — emergence / complex systems explainers", "ORIENTATION", "https://www.youtube.com/results?search_query=veritasium+emergence+complex+systems"),
            ("V4", "Ising model physics-math lectures", "FOUNDATION", "https://www.youtube.com/results?search_query=ising+model+explained+phase+transition"),
            ("V5", "Flocking / Boids model demos", "INTUITION", "https://www.youtube.com/results?search_query=boids+flocking+reynolds"),
            ("V6", "Cellular automata university courses (Wolfram culture critically)", "SURVEY", "https://www.youtube.com/results?search_query=cellular+automata+lecture+course"),
            ("V7", "Criticality and renormalization popular physics-math", "FRONTIER lite", "https://www.youtube.com/results?search_query=renormalization+group+explained+intuition"),
            ("V8", "Complexity Explorer / Santa Fe style courses", "FOUNDATION", "https://www.complexityexplorer.org/"),
        ],
        "secondary_videos": [
            ("V9", "More is Different — Anderson essay discussions", "SECONDARY", "https://www.youtube.com/results?search_query=more+is+different+anderson"),
        ],
        "papers_web": [
            ("P1", "Anderson — More is Different (Science, 1972)", "https://www.science.org/doi/10.1126/science.177.4047.393"),
            ("P2", "Gardner — Mathematical Games (Life columns; historical)", "https://www.scientificamerican.com/"),
            ("W1", "Wikipedia — Emergence", "https://en.wikipedia.org/wiki/Emergence"),
            ("W2", "Wikipedia — Conway's Game of Life", "https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life"),
            ("W3", "Wikipedia — Ising model", "https://en.wikipedia.org/wiki/Ising_model"),
            ("W4", "Wikipedia — Cellular automaton", "https://en.wikipedia.org/wiki/Cellular_automaton"),
            ("W5", "Wikipedia — Boids", "https://en.wikipedia.org/wiki/Boids"),
            ("W6", "Complexity Explorer", "https://www.complexityexplorer.org/"),
        ],
        "defs": [
            ("Emergence slogan", r"Macro patterns not obvious from local rules alone; still lawful."),
            ("Game of Life", r"2D CA with birth/survival thresholds; gliders, still lifes, universality."),
            ("Ising", r"Spins with local interaction; phase transition in 2D."),
        ],
        "takeaways": [
            "Emergence ≠ magic; it is multi-scale structure from local rules.",
            "Life shows computation can live in simple CA.",
            "Ising: collective order from microscopic interaction + temperature.",
            "Chaos is sensitive trajectories; emergence emphasizes levels of description.",
        ],
        "path": [
            ("0 Orientation", "Conway Life Numberphile", "Play with a simulator."),
            ("1 Collective order", "Ising explainers", "Phase transition slogan."),
            ("2 Agents", "Boids demos", "Three rules → flock."),
            ("3 Course", "Ch.4 emergence essay", "Contrast chaos vs emergence table."),
        ],
        "en_inject_knowledge": """### Emergence slogans (from video research)

- [Conway on Life](https://www.youtube.com/watch?v=R9Plq-D1gEk): simple local rules, rich global zoo (gliders, guns, universality lore).
- **More is different:** new effective laws at new scales (Anderson), not violation of micro laws.
- Distinguish **emergence** (levels) from **chaos** (sensitivity) in seminar writing.
""",
        "vi_inject_knowledge": """### Khẩu hiệu trỗi dậy (từ nghiên cứu video)

- [Conway về Life](https://www.youtube.com/watch?v=R9Plq-D1gEk): luật cục bộ đơn giản, vườn thú toàn cục (glider, súng, lore phổ quát).
- **More is different:** luật hiệu dụng mới ở thang mới (Anderson), không phá luật vi mô.
- Phân biệt **trỗi dậy** (cấp độ) với **hỗn độn** (nhạy cảm) khi viết seminar.
""",
    },
]


def md_table_videos(videos: list[tuple[str, str, str, str]]) -> str:
    lines = ["| # | Title / speaker | Role | URL |", "|---|-----------------|------|-----|"]
    for vid, title, role, url in videos:
        lines.append(f"| {vid} | {title} | {role} | {url} |")
    return "\n".join(lines)


def write_pack(t: dict[str, Any]) -> None:
    slug = t["slug"]
    d = VR / slug
    d.mkdir(parents=True, exist_ok=True)

    en_rel = t["en"].relative_to(ROOT).as_posix()
    vi_rel = t["vi"].relative_to(ROOT).as_posix()
    p = t["primary"]

    # README
    path_rows = "\n".join(
        f"| {stage} | {vid} | {goal} |" for stage, vid, goal in t["path"]
    )
    readme = f"""# {t['title']} — video research pack

**Mode:** math-video-researcher B + C (URL discovery + Mode B extraction notes)  
**Date:** 2026-08-04  
**Status:** {t['status']}

## Course integration

| Course page | Path |
|-------------|------|
| EN | `{en_rel}` |
| VI | `{vi_rel}` |

## Learning path (watch order)

| Stage | Video / resource | Goal |
|-------|------------------|------|
{path_rows}

## Primary focus source

| Field | Value |
|-------|--------|
| Title | {p['title']} |
| Speaker / channel | {p['speaker']} |
| URL | {p['url']} |
| Duration | {p['duration']} |
| Level | {p['level']} |
| Role | {p['role']} |

## Complete references (all discovered URLs)

**→ [`references.md`](references.md)** — every video, paper, and web URL found during discovery (primary + secondary).

## Files in this pack

- `analysis.md` — Mode B extraction (definitions, slogans, confusions, gaps)
- `learning_path.md` — staged goals for seminar students
- `references.md` — full URL bibliography
"""
    (d / "README.md").write_text(readme, encoding="utf-8")

    # references.md
    all_urls: list[str] = []
    ref_parts = [
        f"# {t['title']} — complete URL bibliography\n",
        "All URLs discovered or used during `math-video-researcher` discovery (2026-08-04).\n",
        "**Do not** treat every URL as equally authoritative; tiers below mark role.\n",
        "\n---\n\n## A. Primary video sources (recommended path)\n\n",
        md_table_videos(t["videos"]),
        "\n\n---\n\n## B. Additional videos found (secondary / optional)\n\n",
        md_table_videos(t.get("secondary_videos", [])),
        "\n\n---\n\n## C. Research papers, books, and standards\n\n",
        "| # | Work | URL |\n|---|------|-----|\n",
    ]
    for pid, work, url in t["papers_web"]:
        if pid.startswith("P"):
            ref_parts.append(f"| {pid} | {work} | {url} |\n")
            if url.startswith("http"):
                all_urls.append(url)
    ref_parts.append("\n---\n\n## D. Expository web pages and OCW\n\n")
    ref_parts.append("| # | Source | URL |\n|---|--------|-----|\n")
    for pid, work, url in t["papers_web"]:
        if pid.startswith("W"):
            ref_parts.append(f"| {pid} | {work} | {url} |\n")
            if url.startswith("http"):
                all_urls.append(url)
    for vid, title, role, url in t["videos"] + t.get("secondary_videos", []):
        if url.startswith("http"):
            all_urls.append(url)
    ref_parts.append("\n---\n\n## E. Course-internal paths (not HTTP)\n\n")
    ref_parts.append(f"- `research/video-research/{slug}/README.md`\n")
    ref_parts.append(f"- `research/video-research/{slug}/analysis.md`\n")
    ref_parts.append(f"- `research/video-research/{slug}/learning_path.md`\n")
    ref_parts.append(f"- `{en_rel}`\n")
    ref_parts.append(f"- `{vi_rel}`\n")
    ref_parts.append("\n---\n\n## Flat URL list (copy-paste audit)\n\n```\n")
    # unique preserve order
    seen = set()
    flat = []
    for u in all_urls:
        if u not in seen:
            seen.add(u)
            flat.append(u)
    ref_parts.append("\n".join(flat))
    ref_parts.append("\n```\n")
    (d / "references.md").write_text("".join(ref_parts), encoding="utf-8")

    # analysis.md
    defs = "\n\n".join(f"### {name}\n\n{body}" for name, body in t["defs"])
    takes = "\n".join(f"- {x}" for x in t["takeaways"])
    analysis = f"""# Mode B — Video / research analysis: {t['title']}

**Disclaimer:** Full machine transcripts were not loaded for every URL in this pack. Claims below are cross-checked against standard textbooks, course essays, and primary video metadata/slogans. Popular videos are for orientation unless marked CORE.

---

## 1. Metadata — primary focus source

| Field | Value |
|-------|--------|
| Title | {p['title']} |
| Speaker / channel | {p['speaker']} |
| URL | {p['url']} |
| Duration | {p['duration']} |
| Level | {p['level']} |
| Role | {p['role']} |

---

## 2. Key definitions (course-aligned)

{defs}

---

## 3. Extracted slogans / takeaways

{takes}

---

## 4. Popular videos — claims hygiene

| Source tier | Useful for | Watch-out |
|-------------|------------|-----------|
| ORIENTATION popular (Numberphile, Veritasium, Vsauce) | Motivation, pictures, culture | May omit hypotheses, edge cases, or overstate certainty |
| 3Blue1Brown | Geometric intuition | Not a full theorem course; pair with OCW/texts |
| MIT OCW / university | Foundations | Longer; sample lectures, don't binge entire terms mid-essay |
| FRONTIER / news | Open problems and breakthroughs | Check primary papers for precise statements |

---

## 5. Knowledge gaps (honest)

| Gap | Severity | How to close |
|-----|----------|--------------|
| Timestamped full transcripts for every URL | Medium | Optional `extract-video-knowledge` on top 2–3 URLs |
| Frame captures for slides | Low for text course | Optional `img/video_research/{slug}/` |
| Rapidly moving frontiers (e.g. monotile variants, PQC standards) | Medium | Re-check arXiv/NIST when assigning |

---

## 6. Curriculum map

- Chapter: **{t['chapter']}**
- Lesson order: **{t['order']}**
- Pack path: `research/video-research/{slug}/`
- Enrich EN/VI lessons with Video sources + References pointing here.
"""
    (d / "analysis.md").write_text(analysis, encoding="utf-8")

    # learning_path.md
    stages = []
    for i, (stage, vid, goal) in enumerate(t["path"]):
        stages.append(f"## Stage {i} — {stage}\n\n**Resource:** {vid}  \n**Goal:** {goal}\n")
    learning = f"""# {t['title']} — video learning path (seminar)

{chr(10).join(stages)}
## Minimum package (one weekend)

1. Primary focus: {p['url']}
2. One foundation OCW/text link from `references.md`
3. Read Ch.{t['chapter']} essay once; attempt two exercises
4. Write 150 words: “Videos taught me … ; the essay still requires …”

## Pack files

- [`README.md`](README.md)
- [`references.md`](references.md)
- [`analysis.md`](analysis.md)
"""
    (d / "learning_path.md").write_text(learning, encoding="utf-8")


def video_section_en(t: dict[str, Any]) -> str:
    slug = t["slug"]
    lines = [
        "## Video sources (math-video-researcher pack)",
        "",
        f"Use videos for **orientation and geometric/algorithmic intuition**, not as substitutes for proofs or standards documents. Full ranking and Mode B notes: `research/video-research/{slug}/`.",
        "",
        "**Recommended order**",
        "",
    ]
    for i, (vid, title, role, url) in enumerate(t["videos"][:6], 1):
        if url == "COURSE":
            lines.append(f"{i}. **{role}** — {title} (course-internal; see References).")
        else:
            lines.append(f"{i}. **{role}** — {title}: [{url}]({url}).")
    lines.append("")
    lines.append(f"Complete URL bibliography: `research/video-research/{slug}/references.md`.")
    lines.append("")
    return "\n".join(lines)


def video_section_vi(t: dict[str, Any]) -> str:
    slug = t["slug"]
    lines = [
        "## Nguồn video (gói math-video-researcher)",
        "",
        f"Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/{slug}/`.",
        "",
        "**Thứ tự xem gợi ý**",
        "",
    ]
    for i, (vid, title, role, url) in enumerate(t["videos"][:6], 1):
        if url == "COURSE":
            lines.append(f"{i}. **{role}** — {title} (trong khóa; xem Tài liệu).")
        else:
            lines.append(f"{i}. **{role}** — {title}: [{url}]({url}).")
    lines.append("")
    lines.append(f"Danh mục URL đầy đủ: `research/video-research/{slug}/references.md`.")
    lines.append("")
    return "\n".join(lines)


def references_en(t: dict[str, Any], existing_course_line: str | None = None) -> str:
    slug = t["slug"]
    lines = [
        "## References",
        "",
        f"Full URL bibliography from video research (including secondary finds): `research/video-research/{slug}/references.md`.",
        "",
        "### Videos (primary path)",
        "",
    ]
    n = 1
    for vid, title, role, url in t["videos"]:
        if url == "COURSE":
            lines.append(f"{n}. {title} ({role}).")
        else:
            lines.append(f"{n}. {title} — {url}")
        n += 1
    if t.get("secondary_videos"):
        lines.append("")
        lines.append("### Videos (secondary finds)")
        lines.append("")
        for vid, title, role, url in t["secondary_videos"]:
            lines.append(f"{n}. {title} — {url}")
            n += 1
    lines.append("")
    lines.append("### Papers, books, OCW, and web")
    lines.append("")
    for pid, work, url in t["papers_web"]:
        lines.append(f"{n}. {work}: {url}")
        n += 1
    lines.append("")
    lines.append("### Course")
    lines.append("")
    if existing_course_line:
        lines.append(f"{n}. {existing_course_line} Pack: `research/video-research/{slug}/`.")
    else:
        lines.append(f"{n}. Chapter essay siblings — see sidebar. Research pack: `research/video-research/{slug}/` (especially `references.md`).")
    lines.append("")
    return "\n".join(lines)


def references_vi(t: dict[str, Any], existing_course_line: str | None = None) -> str:
    slug = t["slug"]
    lines = [
        "## Tài liệu",
        "",
        f"Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/{slug}/references.md`.",
        "",
        "### Video (lộ trình chính)",
        "",
    ]
    n = 1
    for vid, title, role, url in t["videos"]:
        if url == "COURSE":
            lines.append(f"{n}. {title} ({role}).")
        else:
            lines.append(f"{n}. {title} — {url}")
        n += 1
    if t.get("secondary_videos"):
        lines.append("")
        lines.append("### Video (tìm thêm / phụ)")
        lines.append("")
        for vid, title, role, url in t["secondary_videos"]:
            lines.append(f"{n}. {title} — {url}")
            n += 1
    lines.append("")
    lines.append("### Bài báo, sách, OCW và web")
    lines.append("")
    for pid, work, url in t["papers_web"]:
        lines.append(f"{n}. {work}: {url}")
        n += 1
    lines.append("")
    lines.append("### Trong khóa")
    lines.append("")
    if existing_course_line:
        lines.append(f"{n}. {existing_course_line} Gói: `research/video-research/{slug}/`.")
    else:
        lines.append(f"{n}. Các bài cùng chương — xem sidebar. Gói: `research/video-research/{slug}/` (đặc biệt `references.md`).")
    lines.append("")
    return "\n".join(lines)


def extract_course_ref_line(text: str, lang: str) -> str | None:
    """Pull last Course / Trong khóa style line from existing references if present."""
    for line in text.splitlines():
        s = line.strip()
        if lang == "en" and s.startswith("Course:"):
            # e.g. "5. Course: [Overview](...)"
            if s[0].isdigit():
                # remove leading number
                return s.split(".", 1)[-1].strip()
            return s
        if lang == "en" and "Course:" in s and s[0].isdigit():
            return s.split(".", 1)[-1].strip()
        if lang == "vi" and s[0:1].isdigit() and ("Khóa" in s or "Course" in s or "trong khóa" in s.lower() or "Bài" in s):
            # keep generic
            pass
    # try numbered line containing site.baseurl course links near end
    for line in reversed(text.splitlines()):
        s = line.strip()
        if "site.baseurl" in s and s[0].isdigit():
            return s.split(".", 1)[-1].strip()
    return None


def enrich_lesson(path: Path, t: dict[str, Any], lang: str) -> None:
    text = path.read_text(encoding="utf-8")
    original = text

    # Remove old thin "Popular video source" sections
    import re

    text = re.sub(
        r"\n## Popular video source\n.*?(?=\n## )",
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r"\n## Nguồn video phổ biến\n.*?(?=\n## )",
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    # Remove prior full video pack sections if re-running
    text = re.sub(
        r"\n## Video sources \(math-video-researcher pack\)\n.*?(?=\n## References\n)",
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r"\n## Nguồn video \(gói math-video-researcher\)\n.*?(?=\n## Tài liệu)",
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    # also VI variants Tài liệu tham khảo
    text = re.sub(
        r"\n## Nguồn video \(gói math-video-researcher\)\n.*?(?=\n## Tài liệu tham khảo)",
        "\n",
        text,
        count=1,
        flags=re.S,
    )

    course_line = extract_course_ref_line(text, lang)

    if lang == "en":
        inject = t.get("en_inject_knowledge", "").rstrip() + "\n\n"
        video = video_section_en(t)
        new_refs = references_en(t, course_line)
        # Insert knowledge before Common confusions if not already present
        marker = "From video research"
        if marker not in text and inject.strip():
            if "\n## Common confusions\n" in text:
                text = text.replace(
                    "\n## Common confusions\n",
                    "\n" + inject + "## Common confusions\n",
                    1,
                )
            elif "\n## 8. Common confusions\n" in text:
                text = text.replace(
                    "\n## 8. Common confusions\n",
                    "\n" + inject + "## 8. Common confusions\n",
                    1,
                )
            else:
                # insert before Exercises
                text = text.replace("\n## Exercises\n", "\n" + inject + "## Exercises\n", 1)

        # Replace References section through Further directions
        m = re.search(r"\n## References\n", text)
        if not m:
            raise SystemExit(f"No ## References in {path}")
        m2 = re.search(r"\n## Further directions\n", text)
        if not m2:
            # append
            text = text[: m.start()] + "\n" + video + "\n" + new_refs + text[m.start() :]
            # remove old refs duplicate - messy; better:
            raise SystemExit(f"No Further directions in {path}")
        text = text[: m.start()] + "\n" + video + "\n" + new_refs + text[m2.start() :]
    else:
        inject = t.get("vi_inject_knowledge", "").rstrip() + "\n\n"
        video = video_section_vi(t)
        new_refs = references_vi(t, course_line)
        marker = "từ nghiên cứu video"
        if marker not in text and inject.strip():
            if "\n## Nhầm lẫn thường gặp\n" in text:
                text = text.replace(
                    "\n## Nhầm lẫn thường gặp\n",
                    "\n" + inject + "## Nhầm lẫn thường gặp\n",
                    1,
                )
            elif "\n## Các nhầm lẫn thường gặp\n" in text:
                text = text.replace(
                    "\n## Các nhầm lẫn thường gặp\n",
                    "\n" + inject + "## Các nhầm lẫn thường gặp\n",
                    1,
                )
            elif "\n## Bài tập\n" in text:
                text = text.replace("\n## Bài tập\n", "\n" + inject + "## Bài tập\n", 1)

        # References headers in VI vary
        m = re.search(r"\n## Tài liệu( tham khảo)?\n", text)
        if not m:
            raise SystemExit(f"No ## Tài liệu in {path}")
        m2 = re.search(r"\n## Hướng đi tiếp\n", text)
        if not m2:
            m2 = re.search(r"\n## Hướng phát triển\n", text)
        if not m2:
            raise SystemExit(f"No Further directions VI in {path}")
        text = text[: m.start()] + "\n" + video + "\n" + new_refs + text[m2.start() :]

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"enriched {path.relative_to(ROOT)}")
    else:
        print(f"unchanged {path.relative_to(ROOT)}")


def main() -> None:
    assert len(TOPICS) == 19, len(TOPICS)
    for t in TOPICS:
        assert t["en"].is_file(), t["en"]
        assert t["vi"].is_file(), t["vi"]
        write_pack(t)
        print(f"pack {t['slug']}")
        enrich_lesson(t["en"], t, "en")
        enrich_lesson(t["vi"], t, "vi")
    print("DONE", len(TOPICS))


if __name__ == "__main__":
    main()
