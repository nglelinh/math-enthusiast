#!/usr/bin/env python3
"""Generate Math Enthusiast course chapters (EN + VI) from structured data."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENTS = ROOT / "contents"

# ---------------------------------------------------------------------------
# Course data
# ---------------------------------------------------------------------------

CHAPTERS = [
    {
        "num": "01",
        "en_title": "Great Problems in Mathematics",
        "vi_title": "Những Bài Toán Lớn Của Toán Học",
        "en_blurb": (
            "Famous problems that challenged generations of mathematicians. "
            "The goal is not necessarily to solve them, but to understand "
            "what each problem is, why it is difficult, and what mathematics "
            "has grown around it."
        ),
        "vi_blurb": (
            "Những bài toán nổi tiếng đã thách thức nhiều thế hệ nhà toán học. "
            "Mục tiêu không nhất thiết là giải chúng, mà là hiểu bài toán là gì, "
            "vì sao khó, và những lý thuyết nào đã phát triển xung quanh chúng."
        ),
        "topics": [
            {
                "slug": "Riemann_Hypothesis",
                "en": "The Riemann Hypothesis",
                "vi": "Giả thuyết Riemann",
                "en_body": """The Riemann Hypothesis (RH) is one of the Millennium Prize Problems and, to many mathematicians, the most important unsolved problem in pure mathematics. It concerns the zeros of the **Riemann zeta function**

$$
\\zeta(s) = \\sum_{n=1}^{\\infty} n^{-s},
$$

initially defined for complex numbers $$s$$ with real part greater than $$1$$, and then extended by analytic continuation to almost the entire complex plane.

### What the problem asks

RH asserts that every non-trivial zero of $$\\zeta(s)$$ has real part exactly $$1/2$$. In other words, the zeros that matter for prime numbers all lie on the critical line $$\\operatorname{Re}(s) = 1/2$$.

### Why primes care

Through Euler’s product formula, $$\\zeta(s)$$ encodes the prime numbers:

$$
\\zeta(s) = \\prod_{p\\ \\text{prime}} \\bigl(1 - p^{-s}\\bigr)^{-1}.
$$

The location of zeros controls error terms in the **prime number theorem**, which describes how primes are distributed among the integers. If RH is true, primes are as regularly spaced as one can reasonably hope; if false, their distribution is more irregular than expected.

### Why it is hard

The zeta function is entire except for a pole at $$s=1$$, but controlling its zeros requires deep analysis on the critical strip. Partial results are many—billions of zeros have been checked numerically; zero-free regions and density theorems give useful bounds—yet a full proof or counterexample remains elusive after more than 160 years.

### Mathematics around it

RH sits at the crossroads of analytic number theory, harmonic analysis, random matrix theory, and arithmetic geometry (via analogues for curves over finite fields, where Deligne proved the corresponding statement). Studying RH means studying how primes, waves, and symmetry interact.
""",
                "vi_body": """Giả thuyết Riemann (RH) là một trong các bài toán Thiên niên kỷ và, với nhiều nhà toán học, là bài toán mở quan trọng nhất của toán học thuần túy. Nó liên quan đến các không điểm của **hàm zeta Riemann**

$$
\\zeta(s) = \\sum_{n=1}^{\\infty} n^{-s},
$$

được định nghĩa ban đầu khi phần thực của $$s$$ lớn hơn $$1$$, rồi mở rộng bằng thắc triển giải tích hầu khắp mặt phẳng phức.

### Bài toán hỏi gì

RH khẳng định mọi không điểm không tầm thường của $$\\zeta(s)$$ đều có phần thực đúng bằng $$1/2$$—tức nằm trên đường thẳng tới hạn $$\\operatorname{Re}(s) = 1/2$$.

### Vì sao liên quan đến số nguyên tố

Qua công thức tích Euler, $$\\zeta(s)$$ mã hóa các số nguyên tố. Vị trí các không điểm điều khiển sai số trong **định lý số nguyên tố**. Nếu RH đúng, phân bố số nguyên tố “đều” theo nghĩa tối ưu mà ta có thể kỳ vọng.

### Vì sao khó

Hàm zeta có cấu trúc giải tích phong phú, nhưng kiểm soát không điểm đòi hỏi phân tích sâu trên dải tới hạn. Hàng tỷ không điểm đã được kiểm tra số; nhiều vùng không-không-điểm đã được chứng minh—nhưng chứng minh hoặc phản ví dụ đầy đủ vẫn còn mở sau hơn 160 năm.

### Toán học xung quanh

RH nối lý thuyết số giải tích, phân tích điều hòa, lý thuyết ma trận ngẫu nhiên và hình học số học (với các phiên bản trên đường cong hữu hạn trường mà Deligne đã chứng minh).
""",
            },
            {
                "slug": "P_vs_NP",
                "en": "The P vs NP Problem",
                "vi": "Bài toán P đối với NP",
                "en_body": """**P vs NP** asks whether every problem whose solution can be *verified* quickly can also be *solved* quickly. Formally: is the complexity class **P** equal to **NP**?

### What the problem asks

- **P**: decision problems solvable in polynomial time by a deterministic Turing machine.
- **NP**: decision problems whose “yes” answers have short certificates verifiable in polynomial time.

Clearly $$\\mathrm{P} \\subseteq \\mathrm{NP}$$. The open question is whether the inclusion is strict.

### Why it matters

Thousands of central problems—SAT, traveling salesman (decision version), integer programming, protein folding models, scheduling—are **NP-complete**. If any one of them is in P, then all of them are. A proof that $$\\mathrm{P} \\neq \\mathrm{NP}$$ would confirm that many of these tasks are intrinsically hard (under standard models of computation). A proof that $$\\mathrm{P} = \\mathrm{NP}$$ would upend cryptography, optimization, and algorithm design.

### Why it is hard

The question is not about a single equation but about the *limits of efficient computation*. Techniques that separate other complexity classes often fail at the P/NP boundary. Relativization barriers, natural proofs, and algebrization results explain why many natural proof strategies cannot resolve the problem.

### Mathematics around it

Complexity theory, logic, cryptography, approximation algorithms, and fine-grained complexity all orbit P vs NP. Even without a full resolution, the *language* of NP-completeness organizes modern computer science.
""",
                "vi_body": """**P đối với NP** hỏi: mọi bài toán mà lời giải có thể *kiểm tra* nhanh có thể *giải* nhanh được không? Nói hình thức: lớp phức tạp **P** có bằng **NP**?

### Bài toán hỏi gì

- **P**: các bài toán quyết định giải được trong thời gian đa thức.
- **NP**: các bài toán quyết định có chứng chỉ “có” ngắn, kiểm tra được trong thời gian đa thức.

Rõ ràng $$\\mathrm{P} \\subseteq \\mathrm{NP}$$. Câu hỏi mở là bao hàm có chặt không.

### Vì sao quan trọng

Hàng nghìn bài toán trung tâm—SAT, người du lịch, quy hoạch nguyên, lập lịch—là **NP-đầy đủ**. Nếu một trong chúng thuộc P thì tất cả đều thuộc P. Chứng minh $$\\mathrm{P} \\neq \\mathrm{NP}$$ sẽ khẳng định nhiều bài toán “khó bản chất”; chứng minh đẳng thức sẽ đảo lộn mật mã học và tối ưu hóa.

### Vì sao khó

Đây không phải một phương trình đơn lẻ mà là giới hạn của tính toán hiệu quả. Các rào cản relativization, natural proofs và algebrization giải thích vì sao nhiều chiến lược chứng minh tự nhiên không đủ.

### Toán học xung quanh

Lý thuyết độ phức tạp, logic, mật mã, thuật toán xấp xỉ và fine-grained complexity đều xoay quanh P vs NP.
""",
            },
            {
                "slug": "Birch_Swinnerton_Dyer",
                "en": "The Birch and Swinnerton-Dyer Conjecture",
                "vi": "Giả thuyết Birch và Swinnerton-Dyer",
                "en_body": """The **Birch and Swinnerton-Dyer (BSD) conjecture** links the arithmetic of elliptic curves to the analytic behavior of their $$L$$-functions. It is another Millennium Prize Problem.

### What the problem asks

An elliptic curve $$E$$ over the rationals has a group of rational points $$E(\\mathbb{Q})$$. By Mordell’s theorem this group is finitely generated:

$$
E(\\mathbb{Q}) \\cong \\mathbb{Z}^{r} \\oplus E(\\mathbb{Q})_{\\mathrm{tors}}.
$$

The integer $$r$$ is the **rank**. BSD predicts that $$r$$ equals the order of vanishing of the $$L$$-function $$L(E,s)$$ at $$s=1$$, and gives a precise formula for the leading coefficient in terms of arithmetic invariants (Sha, regulator, periods, Tamagawa numbers).

### Why it is hard

Ranks are subtle: they can jump in families, and the Tate–Shafarevich group is itself difficult. Analytic continuation and functional equations of $$L(E,s)$$ were major theorems (now known in broad generality via modularity). Matching analytic order to algebraic rank requires deep tools from Iwasawa theory, Heegner points, and Euler systems—available in special cases, not yet in full generality.

### Mathematics around it

Elliptic curves sit at the heart of modern number theory and cryptography. BSD is a prototype for the broader philosophy: *special values of $$L$$-functions encode arithmetic*.
""",
                "vi_body": """**Giả thuyết Birch–Swinnerton-Dyer (BSD)** nối số học của đường cong elliptic với hành vi giải tích của hàm $$L$$ tương ứng. Đây cũng là một bài toán Thiên niên kỷ.

### Bài toán hỏi gì

Đường cong elliptic $$E$$ trên số hữu tỷ có nhóm điểm hữu tỷ $$E(\\mathbb{Q})$$, hữu hạn sinh theo định lý Mordell. Hạng $$r$$ của nhóm này, theo BSD, bằng bậc triệt tiêu của $$L(E,s)$$ tại $$s=1$$, kèm công thức chính xác cho hệ số dẫn đạo qua các bất biến số học (Sha, regulator, chu kỳ, số Tamagawa).

### Vì sao khó

Hạng tinh tế; nhóm Tate–Shafarevich khó nắm. Việc khớp bậc giải tích với hạng đại số cần lý thuyết Iwasawa, điểm Heegner, hệ Euler—có trong trường hợp đặc biệt, chưa đầy đủ nói chung.

### Toán học xung quanh

Đường cong elliptic là trung tâm của lý thuyết số hiện đại và mật mã. BSD là nguyên mẫu cho triết lý: *giá trị đặc biệt của hàm $$L$$ mã hóa số học*.
""",
            },
            {
                "slug": "Navier_Stokes",
                "en": "The Navier–Stokes Problem",
                "vi": "Bài toán Navier–Stokes",
                "en_body": """The **Navier–Stokes equations** describe the motion of viscous incompressible fluids. The Millennium problem asks for a rigorous theory of smooth solutions in three dimensions.

### What the problem asks

Given smooth, divergence-free initial data on $$\\mathbb{R}^3$$ (or the torus), does there always exist a unique smooth solution for all positive time, with reasonable growth control? Or can singularities form in finite time?

### Why it is hard

Energy estimates give global weak solutions (Leray), but uniqueness and regularity are open in 3D. The nonlinear term $$(u\\cdot\\nabla)u$$ can concentrate energy at fine scales. Partial results include regularity criteria (Beale–Kato–Majda, Escauriaza–Seregin–Šverák), mild solutions for small data, and extensive numerical evidence—but no complete theorem.

### Mathematics around it

PDEs, harmonic analysis, geometric measure theory, and turbulence modeling all feed into Navier–Stokes. The problem is a stress test for our understanding of nonlinear evolution equations in physics.
""",
                "vi_body": """**Phương trình Navier–Stokes** mô tả chuyển động của chất lỏng nhớt không nén. Bài toán Thiên niên kỷ đòi hỏi lý thuyết chặt chẽ về nghiệm trơn trong không gian ba chiều.

### Bài toán hỏi gì

Với dữ liệu ban đầu trơn, không phân kỳ trên $$\\mathbb{R}^3$$ (hoặc torus), luôn tồn tại nghiệm trơn duy nhất mọi thời gian dương (với kiểm soát tăng trưởng hợp lý) hay singularity có thể xuất hiện trong thời gian hữu hạn?

### Vì sao khó

Ước lượng năng lượng cho nghiệm yếu toàn cục (Leray), nhưng tính duy nhất và chính quy trong 3D vẫn mở. Hạng phi tuyến $$(u\\cdot\\nabla)u$$ có thể tập trung năng lượng ở thang nhỏ.

### Toán học xung quanh

PDE, phân tích điều hòa, lý thuyết độ đo hình học và mô hình rối đều gắn với Navier–Stokes—một bài kiểm tra cho hiểu biết của ta về phương trình tiến hóa phi tuyến trong vật lý.
""",
            },
            {
                "slug": "Twin_Prime_Conjecture",
                "en": "The Twin Prime Conjecture",
                "vi": "Giả thuyết Số nguyên tố sinh đôi",
                "en_body": """**Twin primes** are pairs of primes that differ by 2, such as $$(3,5)$$, $$(11,13)$$, $$(17,19)$$, and $$(101,103)$$. The **twin prime conjecture** asserts that there are infinitely many such pairs.

### What the problem asks

Are there infinitely many primes $$p$$ such that $$p+2$$ is also prime?

### Partial progress

Zhang (2013) proved that some even gap $$H < 70{,}000{,}000$$ occurs infinitely often between consecutive primes; the Polymath project and Maynard reduced admissible gaps dramatically (now into the hundreds). These results show *bounded gaps* infinitely often, but not yet the gap $$2$$ specifically. Chen’s theorem says there are infinitely many primes $$p$$ such that $$p+2$$ is either prime or a product of two primes.

### Why it is hard

Sieve methods detect almost-primes more readily than true primes. Parity problems in sieve theory obstruct simple paths to twin primes. The conjecture is a special case of the Hardy–Littlewood prime-tuples conjecture, which predicts asymptotic densities for many prime patterns.

### Mathematics around it

Analytic number theory, sieve theory, GPY methods, and Maynard’s multidimensional sieves form a living research area—illustrating how “simple” questions about primes drive sophisticated machinery.
""",
                "vi_body": """**Số nguyên tố sinh đôi** là cặp số nguyên tố cách nhau 2, như $$(3,5)$$, $$(11,13)$$. **Giả thuyết số nguyên tố sinh đôi** khẳng định có vô hạn cặp như vậy.

### Bài toán hỏi gì

Có vô hạn số nguyên tố $$p$$ sao cho $$p+2$$ cũng nguyên tố?

### Tiến bộ một phần

Zhang (2013) chứng minh một khoảng cách chẵn bị chặn xuất hiện vô hạn lần; Polymath và Maynard giảm mạnh ngưỡng. Kết quả cho *khoảng cách bị chặn* vô hạn lần, nhưng chưa riêng khoảng cách 2. Định lý Chen nói có vô hạn $$p$$ nguyên tố sao cho $$p+2$$ là nguyên tố hoặc tích hai nguyên tố.

### Vì sao khó

Phương pháp sàng bắt “gần nguyên tố” dễ hơn nguyên tố thật. Vấn đề parity trong lý thuyết sàng cản trở đường đi đơn giản. Giả thuyết là trường hợp đặc biệt của giả thuyết bộ nguyên tố Hardy–Littlewood.

### Toán học xung quanh

Lý thuyết số giải tích, sàng, phương pháp GPY và sàng đa chiều của Maynard—minh họa cách câu hỏi “đơn giản” về số nguyên tố thúc đẩy công cụ tinh vi.
""",
            },
            {
                "slug": "Collatz_Conjecture",
                "en": "The Collatz Conjecture",
                "vi": "Giả thuyết Collatz",
                "en_body": """The **Collatz conjecture** (also called the $$3x+1$$ problem) is elementary to state and stubbornly resistant to proof.

### What the problem asks

Start with a positive integer $$n$$. If $$n$$ is even, replace it by $$n/2$$; if odd, replace it by $$3n+1$$. Repeat. The conjecture asserts that every positive integer eventually reaches the cycle $$4 \\to 2 \\to 1 \\to 4 \\to \\cdots$$.

### Why it is hard

The map mixes multiplication and division by 2 in a way that destroys simple invariants. Heuristics from probabilistic models suggest almost-sure descent on average, and computers have verified the conjecture for enormous ranges, but a global proof would need to control all integer orbits simultaneously—something current dynamical and number-theoretic tools do not fully provide.

### Mathematics around it

Collatz sits near ergodic theory, discrete dynamical systems, and experimental mathematics. It is a reminder that difficulty is not the same as sophistication of statement: some of the hardest problems look like puzzles for a rainy afternoon.
""",
                "vi_body": """**Giả thuyết Collatz** (bài toán $$3x+1$$) phát biểu cực kỳ sơ cấp nhưng rất khó chứng minh.

### Bài toán hỏi gì

Bắt đầu từ số nguyên dương $$n$$. Nếu chẵn thì lấy $$n/2$$; nếu lẻ thì lấy $$3n+1$$. Lặp lại. Giả thuyết: mọi số nguyên dương cuối cùng đều rơi vào chu trình $$4 \\to 2 \\to 1$$.

### Vì sao khó

Ánh xạ trộn nhân và chia 2, phá vỡ bất biến đơn giản. Heuristic xác suất gợi ý trung bình giảm; máy tính kiểm tra dải cực lớn—nhưng chứng minh toàn cục đòi hỏi kiểm soát mọi quỹ đạo cùng lúc.

### Toán học xung quanh

Collatz gần lý thuyết ergodic, hệ động lực rời rạc và toán học thực nghiệm: độ khó không đồng nghĩa với phát biểu phức tạp.
""",
            },
            {
                "slug": "Kakeya_Conjecture",
                "en": "The Kakeya Conjecture",
                "vi": "Giả thuyết Kakeya",
                "en_body": """A **Kakeya set** (Besicovitch set) in $$\\mathbb{R}^n$$ is a set that contains a unit line segment in every direction. Surprisingly, such sets can have measure zero. The modern **Kakeya conjecture** concerns *dimension*: roughly, every Kakeya set in $$\\mathbb{R}^n$$ should have Hausdorff (and Minkowski) dimension $$n$$.

### What the problem asks

Can a set containing a unit segment in every direction be “small” in the sense of fractal dimension, or must it be as large as the ambient space?

### Why it is hard

Kakeya sits at the meeting point of geometric measure theory and harmonic analysis. It is intimately connected to restriction theorems for the Fourier transform, Bochner–Riesz means, and maximal functions. Progress in high dimensions used polynomial methods (Dvir over finite fields; later Guth–Katz and others in the Euclidean setting), but the full conjecture in dimensions $$n \\ge 3$$ has been a long-standing challenge, with dramatic recent advances reshaping the landscape.

### Mathematics around it

Fourier analysis, incidence geometry, multilinear restriction, and the polynomial method. Kakeya is a prototype for “geometric configurations force large dimension.”
""",
                "vi_body": """**Tập Kakeya** (tập Besicovitch) trong $$\\mathbb{R}^n$$ chứa một đoạn thẳng đơn vị theo mọi hướng. Đáng ngạc nhiên là tập như vậy có thể có độ đo không. **Giả thuyết Kakeya** hiện đại nói về *số chiều*: mọi tập Kakeya trong $$\\mathbb{R}^n$$ phải có chiều Hausdorff (và Minkowski) bằng $$n$$.

### Bài toán hỏi gì

Một tập chứa đoạn đơn vị mọi hướng có thể “nhỏ” theo nghĩa chiều fractal, hay buộc phải lớn bằng không gian xung quanh?

### Vì sao khó

Kakeya nằm giao giữa lý thuyết độ đo hình học và phân tích điều hòa, gắn với định lý restriction Fourier, trung bình Bochner–Riesz và hàm cực đại. Phương pháp đa thức (Dvir trên trường hữu hạn; Guth–Katz và các công trình sau) mang lại tiến bộ lớn.

### Toán học xung quanh

Phân tích Fourier, hình học liên thuộc, restriction đa tuyến và phương pháp đa thức—nguyên mẫu cho ý: cấu hình hình học buộc số chiều lớn.
""",
            },
            {
                "slug": "Four_Color_Theorem",
                "en": "The Four Color Theorem",
                "vi": "Định lý Bốn màu",
                "en_body": """The **Four Color Theorem** says that every planar map can be colored with at most four colors so that adjacent regions receive different colors. Equivalently, every planar graph is 4-colorable.

### What the problem asked

Since the 1850s, mapmakers and mathematicians wondered how many colors suffice. Five colors were proved enough early (Heawood); four remained open for over a century.

### The resolution

Appel and Haken (1976) proved the theorem using a computer-assisted discharge argument on a finite set of reducible configurations. Later simplifications (Robertson, Sanders, Seymour, Thomas) still rely on extensive machine checking. The theorem is widely accepted, yet it raised lasting questions about the nature of proof.

### Why it mattered

Beyond map coloring, the result catalyzed structural graph theory, discharging methods, and debates on computer-assisted mathematics. It is both a solved great problem and a philosophical landmark: *when is a proof a proof?*
""",
                "vi_body": """**Định lý Bốn màu** khẳng định mọi bản đồ phẳng có thể tô bằng tối đa bốn màu sao cho hai miền kề nhau khác màu. Tương đương: mọi đồ thị phẳng đều 4-tô màu được.

### Bài toán từng hỏi gì

Từ thập niên 1850: bao nhiêu màu là đủ? Năm màu được chứng minh sớm; bốn màu mở hơn một thế kỷ.

### Lời giải

Appel và Haken (1976) chứng minh với máy tính qua đối số xả trên hữu hạn cấu hình khả quy. Các đơn giản hóa sau vẫn cần kiểm tra máy quy mô lớn—gợi câu hỏi triết học về bản chất chứng minh.

### Vì sao quan trọng

Ngoài tô màu bản đồ, kết quả thúc đẩy lý thuyết đồ thị cấu trúc, phương pháp discharging, và tranh luận về chứng minh có máy tính hỗ trợ.
""",
            },
        ],
    },
    {
        "num": "02",
        "en_title": "Fields Medal & Modern Mathematics",
        "vi_title": "Huy chương Fields và Toán học Hiện đại",
        "en_blurb": (
            "Rather than studying the medal itself, this section explores the "
            "mathematical ideas behind Fields Medal–winning work. "
            "
        ),
        "vi_blurb": (
            "Thay vì nghiên cứu bản thân huy chương, phần này khám phá các ý "
            "tưởng toán học đứng sau các công trình đoạt Fields. Mỗi câu chuyện "
            ""
        ),
        "topics": [
            {
                "slug": "Langlands_Program",
                "en": "The Langlands Program",
                "vi": "Chương trình Langlands",
                "en_body": """The **Langlands program** is a vast web of conjectures linking number theory, representation theory, and algebraic geometry—often described as a “grand unified theory” of mathematics.

Classical reciprocity laws (quadratic reciprocity, class field theory) describe abelian extensions of number fields. What about non-abelian extensions?

Automorphic representations of reductive groups should correspond to Galois representations, matching $$L$$-functions on both sides.

**Breakthroughs.** Langlands’ conjectures (1960s–70s) set the agenda. Wiles’s proof of modularity for semistable elliptic curves (implying Fermat’s Last Theorem) was a spectacular special case. Later work by Breuil–Conrad–Diamond–Taylor and others completed modularity for all elliptic curves over $$\\mathbb{Q}$$. The geometric Langlands program and work of many Fields Medalists continue to expand the vision.

### Why it matters

Langlands organizes how arithmetic, analysis, and symmetry talk to each other. Even partial results have solved century-old problems and reshaped algebraic number theory.
""",
                "vi_body": """**Chương trình Langlands** là mạng lưới giả thuyết nối lý thuyết số, lý thuyết biểu diễn và hình học đại số—thường được gọi là “lý thuyết thống nhất” của toán học.

Các luật đối ngẫu cổ điển mô tả mở rộng abel. Còn mở rộng không abel?

Biểu diễn tự đẳng cấu của nhóm reductive tương ứng với biểu diễn Galois, khớp hàm $$L$$ hai phía.

Giả thuyết Langlands định hướng cả lĩnh vực. Chứng minh modularity của Wiles (kéo theo Định lý Cuối Fermat) là trường hợp đặc biệt rực rỡ. Chương trình Langlands hình học và nhiều công trình Fields tiếp tục mở rộng tầm nhìn.

### Vì sao quan trọng

Langlands tổ chức cách số học, giải tích và đối xứng nói chuyện với nhau; kết quả từng phần đã giải bài toán thế kỷ và định hình lại lý thuyết số đại số.
""",
            },
            {
                "slug": "Perelman_Poincare",
                "en": "Perelman and the Poincaré Conjecture",
                "vi": "Perelman và Giả thuyết Poincaré",
                "en_body": """Henri Poincaré asked whether every simply connected closed 3-manifold is homeomorphic to the 3-sphere. **Grigori Perelman** proved the full **geometrization conjecture** of Thurston, which implies Poincaré’s question.

Classify 3-manifolds; in particular, characterize the 3-sphere topologically.

Richard Hamilton’s **Ricci flow** evolves a Riemannian metric by its Ricci curvature, aiming to uniformize geometry—analogous to heat flow smoothing temperature.

Perelman introduced entropy functionals, surgery to continue past singularities, and a detailed analysis of ancient solutions. The result (2002–2003) resolved geometrization and earned a Fields Medal (declined).

### Why it matters

The proof fused differential geometry, PDEs, and topology. It showed that geometric evolution equations can answer purely topological questions—and became a model of deep, patient geometric analysis.
""",
                "vi_body": """Henri Poincaré hỏi: mọi đa tạp 3 đóng, đơn liên có đồng phôi với mặt cầu 3 không? **Grigori Perelman** chứng minh **giả thuyết hình học hóa** của Thurston, kéo theo câu hỏi Poincaré.

Phân loại đa tạp 3; đặc trưng mặt cầu 3 theo tôpô.

**Ricci flow** của Hamilton tiến hóa metric theo độ cong Ricci, nhằm “chuẩn hóa” hình học—tương tự phương trình nhiệt.

Perelman đưa vào phiếm hàm entropy, phẫu thuật qua singularity, phân tích nghiệm cổ xưa—giải geometrization (2002–2003).

### Vì sao quan trọng

Chứng minh hòa trộn hình học vi phân, PDE và tôpô: phương trình tiến hóa hình học có thể trả lời câu hỏi tôpô thuần túy.
""",
            },
            {
                "slug": "Green_Tao",
                "en": "The Green–Tao Theorem",
                "vi": "Định lý Green–Tao",
                "en_body": """The **Green–Tao theorem** (2004) states that the primes contain arbitrarily long arithmetic progressions: for every $$k$$, there exist primes $$p, p+d, \\ldots, p+(k-1)d$$ with $$d > 0$$.

Do primes contain long linear patterns?

Transfer the Szemerédi theorem (any positive-upper-density set of integers has long APs) to the primes, which have density zero, via a “pseudorandom” majorant and transference principle.

Green and Tao combined additive combinatorics, ergodic ideas, and analytic number theory. Later refinements give quantitative bounds and extensions to other linear patterns.

### Why it matters

The theorem shows that primes, though sparse, still carry rich additive structure. It helped fuse additive combinatorics with analytic number theory—an engine of 21st-century research (and a Fields Medal for Tao).
""",
                "vi_body": """**Định lý Green–Tao** (2004): tập số nguyên tố chứa cấp số cộng dài tùy ý—với mọi $$k$$ tồn tại cấp số cộng $$k$$ số hạng toàn nguyên tố.

Số nguyên tố có chứa mẫu tuyến tính dài?

Chuyển định lý Szemerédi (tập mật độ dương có AP dài) sang số nguyên tố mật độ không, qua majorant giả-ngẫu nhiên và nguyên lý chuyển.

Green và Tao kết hợp tổ hợp cộng tính, ý tưởng ergodic và lý thuyết số giải tích.

### Vì sao quan trọng

Số nguyên tố thưa vẫn mang cấu trúc cộng tính phong phú—hòa trộn tổ hợp cộng tính với lý thuyết số giải tích.
""",
            },
            {
                "slug": "Mirzakhani_Moduli",
                "en": "Mirzakhani and Moduli Spaces",
                "vi": "Mirzakhani và Không gian Mô-đun",
                "en_body": """**Maryam Mirzakhani** transformed the study of Riemann surfaces and their moduli spaces—spaces that parametrize shapes of surfaces.

How do geodesics, volumes, and dynamics behave on moduli spaces of hyperbolic surfaces?

Count simple closed geodesics using careful recursive and geometric integration; relate Weil–Petersson volumes to topological recursion; study earthquake flow and billiards via moduli dynamics.

Mirzakhani’s thesis and later work gave exact formulas and asymptotic growth for geodesic counting, proved the earthquake flow is ergodic (with Eskin), and opened new links between geometry, dynamics, and topology. She received the Fields Medal in 2014—the first woman to do so.

### Why it matters

Moduli spaces are central objects in geometry and mathematical physics. Mirzakhani made them computationally and dynamically tractable, leaving tools used across geometry and dynamics.
""",
                "vi_body": """**Maryam Mirzakhani** làm thay đổi nghiên cứu mặt Riemann và không gian mô-đun—không gian tham số hóa “hình dạng” của mặt.

Trắc địa, thể tích và động lực trên không gian mô-đun mặt hyperbolic hành xử ra sao?

Đếm trắc địa đóng đơn bằng đệ quy và tích phân hình học; liên hệ thể tích Weil–Petersson với đệ quy tôpô; nghiên cứu earthquake flow và bi-a qua động lực mô-đun.

Công thức chính xác và tiệm cận đếm trắc địa; ergodicity của earthquake flow (với Eskin); Fields 2014—nữ toán học đầu tiên.

### Vì sao quan trọng

Không gian mô-đun trung tâm trong hình học và vật lý toán; Mirzakhani làm chúng “tính được” và hiểu được về mặt động lực.
""",
            },
            {
                "slug": "Scholze_Perfectoid",
                "en": "Scholze’s Perfectoid Spaces",
                "vi": "Không gian Perfectoid của Scholze",
                "en_body": """**Peter Scholze** introduced **perfectoid spaces**, a geometric framework that simplifies deep problems in $$p$$-adic Hodge theory and arithmetic geometry.

How can one move information between characteristic zero and characteristic $$p$$, and control cohomology of $$p$$-adic spaces?

Perfectoid algebras and spaces create a tilting equivalence: certain highly ramified objects in mixed characteristic correspond to objects in characteristic $$p$$, where Frobenius is an isomorphism.

Perfectoid geometry led to breakthroughs on the weight-monodromy conjecture (special cases), $$p$$-adic cohomology theories, and the foundations of condensed/analytic geometry (with Clausen). Scholze received the Fields Medal in 2018.

### Why it matters

Perfectoid spaces rewired how arithmetic geometers think about $$p$$-adic worlds—turning intractable ramification into a flexible geometric language.
""",
                "vi_body": """**Peter Scholze** đưa vào **không gian perfectoid**, khung hình học đơn giản hóa các bài toán sâu trong lý thuyết Hodge $$p$$-adic và hình học số học.

Làm sao chuyển thông tin giữa đặc số 0 và đặc số $$p$$, và kiểm soát đối đồng điều không gian $$p$$-adic?

Đại số/không gian perfectoid tạo tương đương tilting: đối tượng phân nhánh mạnh đặc số hỗn hợp tương ứng với đặc số $$p$$, nơi Frobenius là đẳng cấu.

Weight-monodromy (trường hợp đặc biệt), đối đồng điều $$p$$-adic, hình học condensed/analytic (với Clausen); Fields 2018.

### Vì sao quan trọng

Perfectoid đổi cách nghĩ về thế giới $$p$$-adic—biến phân nhánh khó trị thành ngôn ngữ hình học linh hoạt.
""",
            },
            {
                "slug": "Venkatesh_Number_Theory",
                "en": "Venkatesh: Number Theory Meets Representation Theory",
                "vi": "Venkatesh: Lý thuyết Số gặp Lý thuyết Biểu diễn",
                "en_body": """**Akshay Venkatesh** works at the junction of analytic number theory, homogeneous dynamics, and automorphic forms—turning deep equidistribution problems into arithmetic statements.

How are arithmetic objects (integer points, special cycles, automorphic forms) distributed, and what hidden symmetries govern them?

Use dynamics on homogeneous spaces, representation theory of Lie groups, and topological methods to extract effective equidistribution and cohomology of arithmetic groups.

Major results on subconvexity of $$L$$-functions, sparse equidistribution, and the topology of locally symmetric spaces. Fields Medal 2018.

### Why it matters

Venkatesh’s work exemplifies modern number theory: primes and automorphic forms studied with tools from dynamics and topology as much as from classical analysis.
""",
                "vi_body": """**Akshay Venkatesh** làm việc tại giao điểm lý thuyết số giải tích, động lực thuần nhất và dạng tự đẳng cấu—biến bài toán phân bố đều thành phát biểu số học.

Đối tượng số học phân bố ra sao, đối xứng ẩn nào chi phối?

Động lực trên không gian thuần nhất, lý thuyết biểu diễn nhóm Lie, phương pháp tôpô cho equidistribution hiệu quả và đối đồng điều nhóm số học.

Subconvexity hàm $$L$$, equidistribution thưa, tôpô không gian đối xứng địa phương; Fields 2018.

### Vì sao quan trọng

Lý thuyết số hiện đại: số nguyên tố và dạng tự đẳng cấu được nghiên cứu bằng động lực và tôpô không kém giải tích cổ điển.
""",
            },
            {
                "slug": "Viazovska_Sphere_Packing",
                "en": "Viazovska and Sphere Packing",
                "vi": "Viazovska và Bài toán Xếp cầu",
                "en_body": """How densely can equal spheres pack in high dimensions? **Maryna Viazovska** solved the problem in dimensions 8 and (with coauthors) 24.

Find the maximal packing density of unit balls in $$\\mathbb{R}^n$$.

Linear programming bounds for packing (Cohn–Elkies) reduce the problem to constructing special radial functions with Fourier constraints. Viazovska produced an explicit “magic” modular form input that proves optimality of the $$E_8$$ lattice packing in dimension 8; the Leech lattice followed in dimension 24.

2016–2017 solutions; Fields Medal 2022.

### Why it matters

Sphere packing connects discrete geometry, modular forms, and information theory (error-correcting codes). Viazovska’s method is a masterpiece of analytic construction meeting geometric optimality.
""",
                "vi_body": """Xếp các quả cầu bằng nhau dày đặc nhất trong không gian cao chiều như thế nào? **Maryna Viazovska** giải quyết ở chiều 8 và (cùng đồng tác giả) chiều 24.

Mật độ xếp tối đa của quả cầu đơn vị trong $$\\mathbb{R}^n$$.

Chặn quy hoạch tuyến tính (Cohn–Elkies) quy về xây hàm xuyên tâm đặc biệt với ràng buộc Fourier. Viazovska tạo “dạng modular ma thuật” chứng minh tối ưu mạng $$E_8$$ (chiều 8); mạng Leech ở chiều 24.

2016–2017; Fields 2022.

### Vì sao quan trọng

Xếp cầu nối hình học rời rạc, dạng modular và lý thuyết thông tin (mã sửa sai).
""",
            },
            {
                "slug": "Maynard_Primes",
                "en": "Maynard’s Work on Prime Numbers",
                "vi": "Công trình của Maynard về Số nguyên tố",
                "en_body": """**James Maynard** reshaped the study of prime gaps and prime patterns with flexible multidimensional sieve methods.

How small can gaps between consecutive primes be infinitely often? Which patterns of primes occur infinitely often?

Optimize weights in GPY-type sieves over many linear forms simultaneously, obtaining stronger bounded-gap results and new limit-point theorems for prime gaps.

Independent refinement of Zhang’s bounded gaps; work on large gaps, primes with restricted digits, and related patterns. Fields Medal 2022.

### Why it matters

Maynard’s techniques are now standard tools in analytic number theory—showing how a new sieve perspective can reopen classical questions about primes.
""",
                "vi_body": """**James Maynard** định hình lại nghiên cứu khoảng cách và mẫu số nguyên tố bằng phương pháp sàng đa chiều linh hoạt.

Khoảng cách giữa số nguyên tố liên tiếp có thể nhỏ thế nào vô hạn lần? Mẫu nào xuất hiện vô hạn?

Tối ưu trọng số sàng kiểu GPY trên nhiều dạng tuyến tính đồng thời.

Cải tiến khoảng cách bị chặn sau Zhang; khoảng cách lớn; số nguyên tố chữ số hạn chế; Fields 2022.

### Vì sao quan trọng

Kỹ thuật Maynard trở thành công cụ chuẩn trong lý thuyết số giải tích.
""",
            },
            {
                "slug": "Birkar_Algebraic_Geometry",
                "en": "Birkar’s Work in Algebraic Geometry",
                "vi": "Công trình của Birkar trong Hình học Đại số",
                "en_body": """**Caucher Birkar** made fundamental contributions to the **birational classification** of algebraic varieties in higher dimensions.

Extend the classical classification of curves and surfaces to higher-dimensional varieties: when can one “reduce” a variety by birational operations to a simple model?

The minimal model program (MMP) seeks to construct minimal or Mori fiber space models using flips, divisorial contractions, and canonical rings.

Birkar (with Hacon, McKernan, Cascini and in solo work) proved major cases of existence of flips, boundedness of Fano varieties, and related structural results. Fields Medal 2018.

### Why it matters

Birational geometry is the global architecture of algebraic geometry. Birkar’s theorems complete large parts of the higher-dimensional classification program envisioned for decades.
""",
                "vi_body": """**Caucher Birkar** đóng góp nền tảng cho **phân loại birational** đa tạp đại số chiều cao.

Mở rộng phân loại đường cong và mặt lên chiều cao: khi nào có thể “rút gọn” đa tạp bằng phép birational?

Chương trình mô hình tối thiểu (MMP): xây mô hình tối thiểu hoặc không gian sợi Mori qua flip, co divisorial, vành chính tắc.

Tồn tại flip, boundedness đa tạp Fano và kết quả cấu trúc liên quan; Fields 2018.

### Vì sao quan trọng

Hình học birational là kiến trúc toàn cục của hình học đại số; định lý Birkar hoàn thiện phần lớn chương trình phân loại chiều cao.
""",
            },
            {
                "slug": "Modern_Combinatorics_Geometry",
                "en": "Modern Combinatorics and Geometry",
                "vi": "Tổ hợp và Hình học Hiện đại",
                "en_body": """Recent decades have seen a flowering of interactions between **combinatorics**, **geometry**, and **analysis**—often recognized by major prizes and Fields Medals.

### Themes

- **Incidence geometry**: how points and lines meet (Szemerédi–Trotter, Guth–Katz on the distinct distances problem).
- **Extremal combinatorics**: forbidden configurations and Turán-type problems, now powered by flag algebras and analytic limits.
- **High-dimensional geometry**: concentration of measure, discrete isoperimetry, and expander graphs.
- **Probabilistic method**: existence proofs via randomness, derandomization, and algorithmic versions.

### Why it matters

These areas feed theoretical computer science, coding theory, and pure geometry. They illustrate a modern style: mix discrete structure with continuous methods until a rigid pattern appears.
""",
                "vi_body": """Những thập niên gần đây chứng kiến sự giao thoa rực rỡ giữa **tổ hợp**, **hình học** và **giải tích**—thường được ghi nhận bằng các giải thưởng lớn.

### Chủ đề

- **Hình học liên thuộc**: điểm và đường gặp nhau thế nào (Szemerédi–Trotter, Guth–Katz về khoảng cách phân biệt).
- **Tổ hợp cực trị**: cấu hình cấm, flag algebra và giới hạn giải tích.
- **Hình học cao chiều**: tập trung độ đo, isoperimetry rời rạc, đồ thị expander.
- **Phương pháp xác suất**: tồn tại qua ngẫu nhiên và derandomization.

### Vì sao quan trọng

Các lĩnh vực này nuôi khoa học máy tính lý thuyết, lý thuyết mã và hình học thuần túy—phong cách hiện đại: trộn cấu trúc rời rạc với phương pháp liên tục.
""",
            },
        ],
    },
    {
        "num": "03",
        "en_title": "Mathematics That Changed the World",
        "vi_title": "Toán Học Làm Thay Đổi Thế Giới",
        "en_blurb": (
            "Mathematical ideas that became foundations for modern technology "
            "and science—from calculus in physics to linear algebra in AI."
        ),
        "vi_blurb": (
            "Những ý tưởng toán học trở thành nền tảng công nghệ và khoa học "
            "hiện đại—từ giải tích trong vật lý đến đại số tuyến tính trong AI."
        ),
        "topics": [
            {
                "slug": "Calculus_Physics_Engineering",
                "en": "Calculus → Physics & Engineering",
                "vi": "Giải tích → Vật lý & Kỹ thuật",
                "en_body": """**Calculus** — rates of change and accumulation — is the language in which classical physics and engineering are written.

### The idea

Differentiation measures instantaneous change; integration measures total accumulation. The fundamental theorem of calculus links them. Differential equations then express physical laws: Newton’s second law, Maxwell’s equations, heat flow, elasticity.

### World impact

Bridges, circuits, aircraft, climate models, and medical imaging all rely on continuous models solved with calculus and its numerical descendants. Without derivatives and integrals, the scientific revolution’s quantitative core would be unrecognizable.

### What to explore next

ODEs and PDEs, variational principles, and numerical analysis (finite elements, spectral methods).
""",
                "vi_body": """**Giải tích** — tốc độ biến thiên và tích lũy — là ngôn ngữ của vật lý cổ điển và kỹ thuật.

### Ý tưởng

Đạo hàm đo biến thiên tức thời; tích phân đo tích lũy tổng. Định lý cơ bản nối hai khái niệm. Phương trình vi phân diễn đạt định luật vật lý: Newton, Maxwell, truyền nhiệt, đàn hồi.

### Tác động

Cầu, mạch điện, máy bay, mô hình khí hậu, chẩn đoán hình ảnh đều dựa trên mô hình liên tục. Không có đạo hàm và tích phân, lõi định lượng của cách mạng khoa học sẽ khác hẳn.

### Khám phá tiếp

ODE/PDE, nguyên lý biến phân, phân tích số (phần tử hữu hạn, phổ).
""",
            },
            {
                "slug": "Linear_Algebra_AI",
                "en": "Linear Algebra → AI & Machine Learning",
                "vi": "Đại số Tuyến tính → AI & Học máy",
                "en_body": """Modern machine learning is built on **vectors, matrices, and linear maps**.

### The idea

Data points are vectors; datasets are matrices. Linear transformations rotate, stretch, and project. Eigenvalues reveal principal directions; singular value decomposition compresses information. Gradient descent updates parameters in high-dimensional vector spaces.

### World impact

Neural networks are compositions of linear layers and nonlinearities. Recommendation systems, computer vision, large language models, and PCA all speak linear algebra. Sparse matrices and randomized linear algebra make industrial scale possible.

### What to explore next

Spectral methods, optimization on manifolds, kernel methods, and the geometry of high-dimensional spaces.
""",
                "vi_body": """Học máy hiện đại xây trên **vector, ma trận và ánh xạ tuyến tính**.

### Ý tưởng

Điểm dữ liệu là vector; tập dữ liệu là ma trận. Biến đổi tuyến tính quay, kéo giãn, chiếu. Trị riêng lộ hướng chính; SVD nén thông tin. Gradient descent cập nhật tham số trong không gian cao chiều.

### Tác động

Mạng nơ-ron là ghép lớp tuyến tính và phi tuyến. Hệ gợi ý, thị giác máy tính, mô hình ngôn ngữ lớn đều nói ngôn ngữ đại số tuyến tính.

### Khám phá tiếp

Phương pháp phổ, tối ưu trên đa tạp, kernel, hình học không gian cao chiều.
""",
            },
            {
                "slug": "Probability_Data_Science",
                "en": "Probability → Data Science",
                "vi": "Xác suất → Khoa học Dữ liệu",
                "en_body": """**Probability** turns uncertainty into mathematics. **Statistics** turns data into inference.

### The idea

Random variables, expectation, variance, and concentration inequalities quantify fluctuation. Bayes’ rule updates beliefs. Stochastic processes model time-evolving randomness. Large-sample theorems (LLN, CLT) justify estimation.

### World impact

A/B testing, clinical trials, risk models, spam filters, and probabilistic machine learning rest on this foundation. Causality and experimental design refine what data can claim.

### What to explore next

Measure-theoretic probability, martingales, Bayesian methods, and high-dimensional statistics.
""",
                "vi_body": """**Xác suất** biến bất định thành toán học. **Thống kê** biến dữ liệu thành suy diễn.

### Ý tưởng

Biến ngẫu nhiên, kỳ vọng, phương sai, bất đẳng thức tập trung định lượng dao động. Bayes cập nhật niềm tin. Định lý số lớn và giới hạn trung tâm biện minh ước lượng.

### Tác động

Thử nghiệm A/B, thử lâm sàng, mô hình rủi ro, bộ lọc spam, học máy xác suất—tất cả dựa trên nền này.

### Khám phá tiếp

Xác suất lý thuyết độ đo, martingale, Bayes, thống kê cao chiều.
""",
            },
            {
                "slug": "Number_Theory_Cryptography",
                "en": "Number Theory → Cryptography",
                "vi": "Lý thuyết Số → Mật mã học",
                "en_body": """Once the purest pure mathematics, **number theory** now secures the internet.

### The idea

Hard computational problems on integers and curves—factoring large semiprimes, discrete logarithms in finite fields and elliptic curve groups—underpin public-key cryptography (RSA, Diffie–Hellman, ECC). Modular arithmetic is the everyday algebra of ciphers.

### World impact

TLS, digital signatures, cryptocurrencies, and secure messaging rely on number-theoretic assumptions. Post-quantum cryptography shifts toward lattices and codes as quantum algorithms threaten classical schemes.

### What to explore next

Elliptic curves, lattice-based crypto, zero-knowledge proofs, and computational complexity.
""",
                "vi_body": """Từng là toán thuần túy nhất, **lý thuyết số** nay bảo vệ internet.

### Ý tưởng

Bài toán tính toán khó trên số nguyên và đường cong—phân tích thừa số, log rời rạc trên trường hữu hạn và nhóm đường cong elliptic—nền tảng mật mã khóa công khai (RSA, Diffie–Hellman, ECC).

### Tác động

TLS, chữ ký số, tiền mã hóa, nhắn tin an toàn. Mật mã hậu lượng tử chuyển sang lưới và mã khi thuật toán lượng tử đe dọa sơ đồ cổ điển.

### Khám phá tiếp

Đường cong elliptic, mật mã lưới, zero-knowledge, độ phức tạp tính toán.
""",
            },
            {
                "slug": "Graph_Theory_Networks",
                "en": "Graph Theory → Networks & Algorithms",
                "vi": "Lý thuyết Đồ thị → Mạng & Thuật toán",
                "en_body": """A **graph** is a set of vertices connected by edges—the universal model of networks.

### The idea

Paths, connectivity, matchings, flows, and colorings organize discrete structure. Algorithms for shortest paths, minimum spanning trees, and max-flow/min-cut are infrastructure for computation. Random graphs and expanders explain robustness and mixing.

### World impact

The web, social networks, logistics, chip design, and compilers all use graph models. PageRank, recommendation graphs, and network epidemiology are applied graph theory at scale.

### What to explore next

Spectral graph theory, algorithmic graph theory, and geometric group theory’s discrete cousins.
""",
                "vi_body": """**Đồ thị** là tập đỉnh nối bởi cạnh—mô hình phổ quát của mạng.

### Ý tưởng

Đường đi, liên thông, ghép cặp, luồng, tô màu tổ chức cấu trúc rời rạc. Thuật toán đường ngắn nhất, cây khung nhỏ nhất, max-flow/min-cut là hạ tầng tính toán.

### Tác động

Web, mạng xã hội, logistics, thiết kế chip, biên dịch. PageRank và dịch tễ mạng là lý thuyết đồ thị quy mô lớn.

### Khám phá tiếp

Lý thuyết đồ thị phổ, thuật toán đồ thị, mở rộng hình học rời rạc.
""",
            },
            {
                "slug": "Optimization_Operations_AI",
                "en": "Optimization → Operations & AI",
                "vi": "Tối ưu hóa → Vận hành & AI",
                "en_body": """**Optimization** asks for the best decision under constraints—maximize, minimize, or find equilibrium.

### The idea

Linear and convex programming give reliable global optima; nonconvex landscapes host deep learning. Duality, gradients, proximal methods, and combinatorial optimization form a toolkit spanning continuous and discrete worlds.

### World impact

Supply chains, energy grids, portfolio design, airline scheduling, and training neural networks are optimization problems. Operations research and modern AI share the same mathematical spine.

### What to explore next

Convex analysis, integer programming, stochastic optimization, and nonsmooth methods.
""",
                "vi_body": """**Tối ưu hóa** tìm quyết định tốt nhất dưới ràng buộc—cực đại, cực tiểu, hoặc cân bằng.

### Ý tưởng

Quy hoạch tuyến tính và lồi cho cực trị toàn cục tin cậy; cảnh quan không lồi chứa học sâu. Đối ngẫu, gradient, proximal, tối ưu tổ hợp tạo bộ công cụ liên tục–rời rạc.

### Tác động

Chuỗi cung ứng, lưới điện, danh mục đầu tư, lịch bay, huấn luyện mạng nơ-ron—cùng một xương sống toán học.

### Khám phá tiếp

Phân tích lồi, quy hoạch nguyên, tối ưu ngẫu nhiên, phương pháp không trơn.
""",
            },
            {
                "slug": "Fourier_Signal_Processing",
                "en": "Fourier Analysis → Signal Processing",
                "vi": "Phân tích Fourier → Xử lý Tín hiệu",
                "en_body": """**Fourier analysis** decomposes functions into waves—sines, cosines, or complex exponentials.

### The idea

A signal in time becomes a spectrum in frequency. Convolution becomes multiplication. The FFT makes the transform practical on digital data. Wavelets and time-frequency analysis refine localization.

### World impact

Audio compression, MRI, wireless communication, image processing, and PDEs all use Fourier ideas. JPEG, MP3, and OFDM are engineering descendants of harmonic analysis.

### What to explore next

Distribution theory, pseudodifferential operators, compressed sensing, and harmonic analysis on groups.
""",
                "vi_body": """**Phân tích Fourier** phân rã hàm thành sóng—sin, cos, hoặc hàm mũ phức.

### Ý tưởng

Tín hiệu theo thời gian trở thành phổ theo tần số. Tích chập thành nhân. FFT làm biến đổi thực tế trên dữ liệu số. Wavelet tinh chỉnh định vị thời gian–tần số.

### Tác động

Nén âm thanh, MRI, truyền thông không dây, xử lý ảnh, PDE. JPEG, MP3, OFDM là hậu duệ kỹ thuật của phân tích điều hòa.

### Khám phá tiếp

Lý thuyết phân bố, toán tử giả vi phân, compressed sensing.
""",
            },
            {
                "slug": "Differential_Equations_Applications",
                "en": "Differential Equations → Physics & Engineering",
                "vi": "Phương trình Vi phân → Vật lý & Kỹ thuật",
                "en_body": """**Differential equations** relate unknown functions to their rates of change—the standard form of physical law.

### The idea

ODEs model lumped systems (circuits, populations, rigid bodies). PDEs model fields in space and time (waves, diffusion, elasticity, quantum mechanics). Well-posedness, stability, and numerical solvers are the practical backbone.

### World impact

Weather prediction, structural engineering, electromagnetism, epidemiology, and finance (Black–Scholes-type models) depend on DE models and their simulations.

### What to explore next

Dynamical systems, finite element methods, stochastic DEs, and geometric PDEs.
""",
                "vi_body": """**Phương trình vi phân** liên hệ hàm ẩn với tốc độ biến thiên—dạng chuẩn của định luật vật lý.

### Ý tưởng

ODE mô hình hệ tập trung (mạch, quần thể). PDE mô hình trường trong không gian–thời gian (sóng, khuếch tán, đàn hồi, lượng tử). Tính đặt đúng, ổn định và bộ giải số là xương sống thực tiễn.

### Tác động

Dự báo thời tiết, kỹ thuật kết cấu, điện từ, dịch tễ, tài chính định lượng.

### Khám phá tiếp

Hệ động lực, phần tử hữu hạn, SDE, PDE hình học.
""",
            },
        ],
    },
    {
        "num": "04",
        "en_title": "Beautiful Mathematics",
        "vi_title": "Toán Học Đẹp",
        "en_blurb": (
            "Mathematics that is fascinating simply because of the ideas "
            "themselves—infinity, symmetry, chaos, and strange geometries."
        ),
        "vi_blurb": (
            "Toán học hấp dẫn chỉ vì chính các ý tưởng—vô hạn, đối xứng, hỗn "
            "độn và những hình học lạ."
        ),
        "topics": [
            {
                "slug": "Infinity",
                "en": "Infinity",
                "vi": "Vô hạn",
                "en_body": """**Infinity** is not a number in the ordinary sense—it is a family of ideas about unbounded size and endless process.

### Core pictures

- Potential infinity: processes that continue without end (counting $$1,2,3,\\ldots$$).
- Actual infinity: completed infinite sets ($$\\mathbb{N}$$, $$\\mathbb{R}$$).
- Cantor’s hierarchy: $$\\lvert\\mathbb{N}\\rvert < \\lvert\\mathbb{R}\\rvert$$, and arbitrarily large cardinals.

### Why it is beautiful

Infinity forces precise definitions. Once made rigorous, it reveals unexpected structure: different sizes of infinity, well-orderings, and independence phenomena (continuum hypothesis).
""",
                "vi_body": """**Vô hạn** không phải một số theo nghĩa thông thường—mà là họ ý tưởng về kích thước không bị chặn và quá trình không kết thúc.

### Bức tranh cốt lõi

- Vô hạn tiềm năng: quá trình tiếp diễn (đếm $$1,2,3,\\ldots$$).
- Vô hạn thực sự: tập vô hạn hoàn chỉnh ($$\\mathbb{N}$$, $$\\mathbb{R}$$).
- Phân cấp Cantor: $$\\lvert\\mathbb{N}\\rvert < \\lvert\\mathbb{R}\\rvert$$ và các lực lượng lớn tùy ý.

### Vì sao đẹp

Vô hạn buộc định nghĩa chính xác—và lộ cấu trúc bất ngờ: nhiều “cỡ” vô hạn, sắp xếp tốt, hiện tượng độc lập (giả thuyết continuum).
""",
            },
            {
                "slug": "Fractals",
                "en": "Fractals",
                "vi": "Fractal",
                "en_body": """**Fractals** are shapes with structure at every scale—coastlines, Cantor sets, Julia sets, the Mandelbrot set.

### Core pictures

Self-similarity, fractional dimension (Hausdorff dimension), and iterative constructions $$z \\mapsto z^2 + c$$. Roughness becomes a measurable geometric quantity.

### Why it is beautiful

Fractals show that “pathological” sets are natural. Simple rules generate endless visual and mathematical complexity.
""",
                "vi_body": """**Fractal** là hình có cấu trúc ở mọi thang đo—bờ biển, tập Cantor, Julia, Mandelbrot.

### Bức tranh cốt lõi

Tự đồng dạng, chiều phân số (Hausdorff), phép lặp $$z \\mapsto z^2 + c$$. Độ gồ ghề trở thành đại lượng hình học đo được.

### Vì sao đẹp

Tập “bệnh lý” hóa ra tự nhiên; quy tắc đơn giản sinh phức tạp vô tận.
""",
            },
            {
                "slug": "Symmetry",
                "en": "Symmetry",
                "vi": "Đối xứng",
                "en_body": """**Symmetry** is sameness under transformation. Group theory is its language.

### Core pictures

Reflection, rotation, translation, and more exotic automorphisms. Crystallographic groups, Lie groups, and Galois groups encode structure in geometry, physics, and algebra.

### Why it is beautiful

Classifying symmetries often classifies objects themselves. Beauty and rigidity travel together: the more symmetric, the more constrained—and often the more elegant.
""",
                "vi_body": """**Đối xứng** là sự không đổi dưới biến đổi. Lý thuyết nhóm là ngôn ngữ của nó.

### Bức tranh cốt lõi

Phản xạ, quay, tịnh tiến và các tự đẳng cấu tinh vi hơn. Nhóm tinh thể, nhóm Lie, nhóm Galois mã hóa cấu trúc trong hình học, vật lý, đại số.

### Vì sao đẹp

Phân loại đối xứng thường phân loại chính đối tượng. Càng đối xứng càng bị ràng buộc—và thường càng thanh nhã.
""",
            },
            {
                "slug": "Chaos",
                "en": "Chaos",
                "vi": "Hỗn độn",
                "en_body": """**Chaos** is sensitive dependence on initial conditions in deterministic systems—the “butterfly effect” made mathematical.

### Core pictures

Logistic map, Lorenz attractor, Lyapunov exponents, and strange attractors. Predictability can fail even when the law of motion is exact.

### Why it is beautiful

Chaos reconciles determinism with practical unpredictability. Geometry of attractors and symbolic dynamics reveal order inside disorder.
""",
                "vi_body": """**Hỗn độn** là phụ thuộc nhạy cảm vào điều kiện ban đầu trong hệ tất định—“hiệu ứng cánh bướm” được toán học hóa.

### Bức tranh cốt lõi

Ánh xạ logistic, hấp dẫn Lorenz, số mũ Lyapunov, hấp dẫn lạ. Khả năng dự đoán có thể thất bại dù định luật chuyển động chính xác.

### Vì sao đẹp

Hòa giải tất định với không thể dự đoán thực tiễn; hình học hấp dẫn lộ trật tự trong rối loạn.
""",
            },
            {
                "slug": "Strange_Geometry",
                "en": "Strange Geometric Objects",
                "vi": "Đối tượng Hình học Lạ",
                "en_body": """Mathematics invents spaces that defy everyday intuition: non-orientable surfaces, space-filling curves, exotic spheres, fractal boundaries.

### Core pictures

Möbius band and Klein bottle; Peano and Hilbert curves; Alexander horned sphere; Banach–Tarski paradox (with the axiom of choice).

### Why it is beautiful

Each object answers a precise question—and forces us to revise what “shape” means.
""",
                "vi_body": """Toán học tạo không gian thách thức trực giác: mặt không định hướng, đường lấp đầy không gian, mặt cầu kỳ lạ, biên fractal.

### Bức tranh cốt lõi

Dải Möbius, chai Klein; đường Peano–Hilbert; mặt cầu sừng Alexander; nghịch lý Banach–Tarski.

### Vì sao đẹp

Mỗi đối tượng trả lời một câu hỏi chính xác—và buộc ta định nghĩa lại “hình dạng”.
""",
            },
            {
                "slug": "Paradoxes",
                "en": "Paradoxes",
                "vi": "Nghịch lý",
                "en_body": """**Paradoxes** are arguments that lead to contradiction or absurdity—signposts of hidden assumptions.

### Core pictures

Zeno’s paradoxes of motion; Russell’s paradox in naive set theory; unexpected hanging; sleeping beauty; non-measurable sets.

### Why it is beautiful

Resolving a paradox builds better foundations. Russell’s paradox led to axiomatic set theory; Zeno’s puzzles sharpened the theory of limits and infinite series.
""",
                "vi_body": """**Nghịch lý** là lập luận dẫn đến mâu thuẫn hoặc phi lý—biển báo cho giả định ẩn.

### Bức tranh cốt lõi

Zeno về chuyển động; Russell trong lý thuyết tập ngây thơ; treo cổ bất ngờ; tập không đo được.

### Vì sao đẹp

Giải nghịch lý xây nền tảng tốt hơn: Russell dẫn tới tiên đề hóa; Zeno mài giũa giới hạn và chuỗi.
""",
            },
            {
                "slug": "Higher_Dimensions",
                "en": "Higher Dimensions",
                "vi": "Không gian Cao chiều",
                "en_body": """**Higher dimensions** extend length, area, and volume beyond three coordinates.

### Core pictures

Hypercubes, hyperspheres, projections and slices as visualization tools. Concentration of measure: in high dimension, “most” mass sits near the equator of the sphere.

### Why it is beautiful

Dimension is a parameter that transforms geometry and probability. What is rare in 3D can be typical in 300D—central to modern data analysis.
""",
                "vi_body": """**Không gian cao chiều** mở rộng độ dài, diện tích, thể tích vượt ba tọa độ.

### Bức tranh cốt lõi

Siêu lập phương, siêu cầu; chiếu và lát cắt để hình dung. Tập trung độ đo: ở chiều cao, “hầu hết” khối lượng nằm gần xích đạo mặt cầu.

### Vì sao đẹp

Chiều là tham số biến hình học và xác suất—then chốt cho phân tích dữ liệu hiện đại.
""",
            },
            {
                "slug": "Minimal_Surfaces",
                "en": "Minimal Surfaces",
                "vi": "Mặt Tối thiểu",
                "en_body": """A **minimal surface** locally minimizes area—like a soap film spanning a wire.

### Core pictures

Mean curvature zero; catenoid, helicoid, Costa surface. Plateau’s problem: find a surface of least area with given boundary.

### Why it is beautiful

Analysis, geometry, and visual elegance meet. Minimal surfaces appear in materials science, general relativity (apparent horizons), and pure geometric analysis.
""",
                "vi_body": """**Mặt tối thiểu** cực tiểu hóa diện tích cục bộ—như màng xà phòng căng trên khung dây.

### Bức tranh cốt lõi

Độ cong trung bình không; catenoid, helicoid, mặt Costa. Bài toán Plateau: mặt diện tích nhỏ nhất với biên cho trước.

### Vì sao đẹp

Giải tích, hình học và vẻ đẹp thị giác gặp nhau—xuất hiện trong khoa học vật liệu và phân tích hình học.
""",
            },
            {
                "slug": "Tilings",
                "en": "Tilings",
                "vi": "Lát mặt phẳng",
                "en_body": """**Tilings** cover the plane without gaps or overlaps—periodic or not.

### Core pictures

Regular tessellations; Penrose aperiodic tilings; the recent discovery of aperiodic monotiles (“einstein” problem). Symmetry groups of wallpaper patterns.

### Why it is beautiful

Local rules generate global order—or enforced aperiodicity. Tilings connect art, crystallography, and logic (undecidability of the tiling problem in general).
""",
                "vi_body": """**Lát** phủ mặt phẳng không hở không chồng—tuần hoàn hoặc không.

### Bức tranh cốt lõi

Lưới đều; lát Penrose không tuần hoàn; monotile không tuần hoàn gần đây. Nhóm đối xứng họa tiết giấy dán tường.

### Vì sao đẹp

Quy tắc địa phương sinh trật tự toàn cục—nối nghệ thuật, tinh thể học và logic (bài toán lát nói chung không quyết định được).
""",
            },
            {
                "slug": "Impossible_Shapes",
                "en": "Impossible Shapes",
                "vi": "Hình Bất khả",
                "en_body": """**Impossible shapes** look locally consistent but cannot exist globally in 3D Euclidean space—Penrose triangle, Escher staircases.

### Core pictures

Projection ambiguity; inconsistency of depth cues; mathematical models via cohomology of local data or branched coverings.

### Why it is beautiful

They make global geometry tangible: local truths need not glue to a global object—a theme that reappears in advanced geometry and topology.
""",
                "vi_body": """**Hình bất khả** trông nhất quán cục bộ nhưng không tồn tại toàn cục trong không gian Euclid 3D—tam giác Penrose, cầu thang Escher.

### Bức tranh cốt lõi

Mơ hồ phép chiếu; mâu thuẫn gợi ý độ sâu; mô hình qua đối đồng điều dữ liệu địa phương.

### Vì sao đẹp

Hình học toàn cục trở nên sờ được: chân lý địa phương không luôn dán thành đối tượng toàn cục.
""",
            },
            {
                "slug": "Emergence",
                "en": "Emergence",
                "vi": "Hiện tượng Nảy sinh",
                "en_body": """**Emergence** is complexity arising from simple local rules—flocks, crystals, cellular automata, phase transitions.

### Core pictures

Conway’s Game of Life; Ising model; self-organized criticality; renormalization group intuition: macroscopic laws from microscopic interactions.

### Why it is beautiful

Mathematics explains how “more is different.” Collective behavior need not be written into any single particle’s law—yet becomes precise at the right scale.
""",
                "vi_body": """**Nảy sinh** là phức tạp từ quy tắc địa phương đơn giản—đàn chim, tinh thể, ô tự động, chuyển pha.

### Bức tranh cốt lõi

Game of Life; mô hình Ising; tới hạn tự tổ chức; nhóm chuẩn hóa: định luật vĩ mô từ tương tác vi mô.

### Vì sao đẹp

“Nhiều hơn là khác”: hành vi tập thể không cần ghi trong luật từng hạt—nhưng trở nên chính xác ở thang đúng.
""",
            },
        ],
    },
    {
        "num": "05",
        "en_title": "Mathematics Through Famous Proofs",
        "vi_title": "Toán Học Qua Các Chứng Minh Nổi Tiếng",
        "en_blurb": (
            "Learn mathematics by following remarkable proofs—focusing on the "
            "idea behind the argument, not memorization."
        ),
        "vi_blurb": (
            "Học toán bằng cách theo các chứng minh đáng nhớ—nhấn mạnh ý tưởng "
            "đằng sau lập luận, không chỉ ghi nhớ."
        ),
        "topics": [
            {
                "slug": "Euclid_Infinite_Primes",
                "en": "Euclid: Infinitely Many Primes",
                "vi": "Euclid: Vô hạn Số nguyên tố",
                "en_body": """**Euclid’s theorem:** there are infinitely many prime numbers.

### The idea of the proof

Suppose there were only finitely many primes $$p_1,\\ldots,p_k$$. Form

$$
N = p_1 p_2 \\cdots p_k + 1.
$$

Then $$N > 1$$, so $$N$$ has a prime factor. That prime cannot be any $$p_i$$, because each $$p_i$$ leaves remainder $$1$$ when dividing $$N$$. Contradiction.

### Why it matters

The argument is pure logic with minimal machinery—a model of elegance. Variants yield primes in arithmetic progressions under extra work (Dirichlet), but the original idea remains a perfect first proof.
""",
                "vi_body": """**Định lý Euclid:** có vô hạn số nguyên tố.

### Ý tưởng chứng minh

Giả sử chỉ có hữu hạn nguyên tố $$p_1,\\ldots,p_k$$. Lấy

$$
N = p_1 p_2 \\cdots p_k + 1.
$$

$$N > 1$$ nên có ước nguyên tố; ước đó không thể là $$p_i$$ nào vì mỗi $$p_i$$ chia $$N$$ dư $$1$$. Mâu thuẫn.

### Vì sao quan trọng

Lập luận thuần logic, tối giản—mẫu mực của sự thanh nhã.
""",
            },
            {
                "slug": "Cantor_Diagonal",
                "en": "Cantor’s Diagonal Argument",
                "vi": "Đối số Đường chéo Cantor",
                "en_body": """Cantor proved that the real numbers are **uncountable**: they cannot be listed in a sequence $$r_1, r_2, r_3, \\ldots$$ that includes every real.

### The idea of the proof

Any proposed list of reals in $$(0,1)$$ as infinite decimals can be defeated by building a number that differs from the $$n$$th listed number in the $$n$$th decimal place. The new number is missing from the list.

### Why it matters

Diagonalization is a universal pattern: different sizes of infinity, undecidability, and Gödel/Turing phenomena all reuse the move “construct something that escapes every enumeration.”
""",
                "vi_body": """Cantor chứng minh tập số thực **không đếm được**: không thể liệt kê thành dãy chứa mọi số thực.

### Ý tưởng chứng minh

Mọi danh sách số trong $$(0,1)$$ dạng thập phân vô hạn đều bị đánh bại bằng cách tạo số khác số thứ $$n$$ ở chữ số thứ $$n$$. Số mới không có trong danh sách.

### Vì sao quan trọng

Đường chéo là mẫu phổ quát: cỡ vô hạn khác nhau, không quyết định được, Gödel/Turing—cùng động tác “tạo thứ thoát mọi liệt kê”.
""",
            },
            {
                "slug": "Godel_Incompleteness",
                "en": "Gödel’s Incompleteness Theorems",
                "vi": "Định lý Bất toàn Gödel",
                "en_body": """**Gödel’s incompleteness theorems** limit what formal axiom systems can achieve.

### The idea of the proofs

By encoding syntax as numbers (Gödel numbering), a sufficiently strong system can talk about its own proofs. One then constructs a sentence that says, in effect, “I am not provable.” If the system is consistent, the sentence is true but unprovable. A second theorem shows that such a system cannot prove its own consistency (under mild conditions).

### Why it matters

Hilbert’s dream of a complete, finitary foundation for mathematics meets a structural obstacle. Incompleteness reshaped logic, philosophy of mathematics, and theoretical computer science.
""",
                "vi_body": """**Định lý bất toàn Gödel** giới hạn những gì hệ tiên đề hình thức có thể đạt.

### Ý tưởng chứng minh

Mã hóa cú pháp thành số (số Gödel) để hệ đủ mạnh nói về chứng minh của chính nó. Xây câu tương đương “tôi không chứng minh được”. Nếu nhất quán, câu đúng nhưng không chứng minh được. Định lý thứ hai: hệ không tự chứng minh nhất quán tính (dưới điều kiện ôn hòa).

### Vì sao quan trọng

Giấc mơ Hilbert về nền tảng đầy đủ, hữu hạn gặp chướng ngại cấu trúc—định hình lại logic và triết học toán.
""",
            },
            {
                "slug": "Euler_Konigsberg",
                "en": "Euler and the Königsberg Bridges",
                "vi": "Euler và Cầu Königsberg",
                "en_body": """The people of Königsberg asked whether one could walk through the city crossing each of seven bridges exactly once. **Euler** proved it impossible—and invented graph theory.

### The idea of the proof

Model land masses as vertices and bridges as edges. An Eulerian path (traverse each edge once) requires that zero or two vertices have odd degree. Königsberg had four odd-degree vertices, so no such walk exists.

### Why it matters

Topology and combinatorics of networks begin here: abstract the irrelevant geometry, keep incidence, and reason about degrees.
""",
                "vi_body": """Dân Königsberg hỏi có thể đi qua thành phố, mỗi trong bảy cầu đúng một lần không. **Euler** chứng minh không thể—và khai sinh lý thuyết đồ thị.

### Ý tưởng chứng minh

Đất liền là đỉnh, cầu là cạnh. Đường Euler (đi mỗi cạnh một lần) đòi hỏi không hoặc đúng hai đỉnh bậc lẻ. Königsberg có bốn đỉnh bậc lẻ.

### Vì sao quan trọng

Tôpô và tổ hợp mạng bắt đầu từ đây: trừu tượng hóa hình học thừa, giữ liên thuộc, lập luận về bậc.
""",
            },
            {
                "slug": "Irrationality_Sqrt2",
                "en": "Irrationality of √2",
                "vi": "Tính vô tỷ của √2",
                "en_body": """$$\\sqrt{2}$$ is not a ratio of integers—the classic Greek discovery that shattered the belief that all lengths are commensurable.

### The idea of the proof

Assume $$\\sqrt{2} = p/q$$ in lowest terms. Then $$p^2 = 2q^2$$, so $$p^2$$ is even, hence $$p$$ is even: $$p = 2k$$. Substitute to find $$q$$ even as well—contradicting lowest terms.

### Why it matters

Proof by infinite descent / parity is a prototype for number-theoretic rigor. It introduces the style: assume rationality, derive divisibility constraints, reach contradiction.
""",
                "vi_body": """$$\\sqrt{2}$$ không phải tỷ số hai số nguyên—phát hiện Hy Lạp cổ phá vỡ niềm tin mọi độ dài đều thông ước.

### Ý tưởng chứng minh

Giả sử $$\\sqrt{2} = p/q$$ tối giản. Khi đó $$p^2 = 2q^2$$ nên $$p$$ chẵn: $$p = 2k$$. Suy ra $$q$$ cũng chẵn—mâu thuẫn tối giản.

### Vì sao quan trọng

Chứng minh bằng chẵn lẻ / hạ vô hạn là nguyên mẫu sự chặt chẽ trong lý thuyết số.
""",
            },
            {
                "slug": "Four_Color_Proof",
                "en": "The Four Color Theorem (Proof Ideas)",
                "vi": "Định lý Bốn màu (Ý tưởng Chứng minh)",
                "en_body": """The **Four Color Theorem** was the first major theorem proved with essential computer assistance.

### The idea of the proof

Reduce the problem to a finite (but huge) checklist: every minimal counterexample must contain one of a set of “unavoidable” configurations, and each such configuration is “reducible” (cannot appear in a minimal counterexample). Computers verify reducibility case by case; human insight designs the discharging method that produces unavoidability.

### Why it matters

It expanded what counts as mathematical knowledge and spurred formal verification efforts (later proofs checked in proof assistants).
""",
                "vi_body": """**Định lý Bốn màu** là định lý lớn đầu tiên cần hỗ trợ máy tính cốt yếu.

### Ý tưởng chứng minh

Quy về danh sách hữu hạn (nhưng khổng lồ): mọi phản ví dụ tối thiểu chứa một cấu hình “không tránh khỏi”, và mỗi cấu hình đó “khả quy”. Máy kiểm tra từng trường hợp; con người thiết kế discharging để tạo tính không tránh khỏi.

### Vì sao quan trọng

Mở rộng ranh giới tri thức toán học và thúc đẩy kiểm chứng hình thức.
""",
            },
            {
                "slug": "Fermat_Last_Theorem",
                "en": "Fermat’s Last Theorem",
                "vi": "Định lý Cuối cùng của Fermat",
                "en_body": """**Fermat’s Last Theorem:** for integers $$n \\ge 3$$, there are no positive integers $$a,b,c$$ with $$a^n + b^n = c^n$$.

### The idea of the proof (modern)

Frey suggested that a counterexample would yield a strange elliptic curve (the Frey curve) that cannot be modular. Ribet proved that such a curve would violate the Taniyama–Shimura–Weil modularity conjecture for semistable curves. Wiles (with Taylor) proved enough modularity to obtain a contradiction. Thus no counterexample exists.

### Why it matters

The “idea” is not elementary number theory alone—it is a bridge: Diophantine equation → elliptic curves → modular forms. Entire fields advanced to settle one ancient line in a margin.
""",
                "vi_body": """**Định lý Cuối Fermat:** với $$n \\ge 3$$, không có số nguyên dương $$a,b,c$$ thỏa $$a^n + b^n = c^n$$.

### Ý tưởng chứng minh (hiện đại)

Phản ví dụ sẽ cho đường cong Frey không thể modular. Ribet chứng minh điều đó mâu thuẫn giả thuyết modularity (trường hợp semistable). Wiles (với Taylor) chứng minh đủ modularity để mâu thuẫn.

### Vì sao quan trọng

Ý tưởng là cây cầu: phương trình Diophantine → đường cong elliptic → dạng modular—cả lĩnh vực tiến lên vì một dòng ghi lề.
""",
            },
            {
                "slug": "Poincare_Proof",
                "en": "The Poincaré Conjecture (Proof Ideas)",
                "vi": "Giả thuyết Poincaré (Ý tưởng Chứng minh)",
                "en_body": """**Poincaré Conjecture (3D):** every simply connected closed 3-manifold is homeomorphic to $$S^3$$.

### The idea of the proof

Hamilton proposed Ricci flow to evolve metrics toward constant curvature. Singularities may form; Perelman showed how to perform surgeries, control entropy, and analyze the long-time picture so that a simply connected manifold becomes a round sphere after finite surgeries. Geometrization classifies all closed 3-manifolds more broadly.

### Why it matters

A topological statement is proved by geometric PDE methods—one of the great methodology transfers in modern mathematics.
""",
                "vi_body": """**Giả thuyết Poincaré (3D):** mọi đa tạp 3 đóng đơn liên đồng phôi với $$S^3$$.

### Ý tưởng chứng minh

Hamilton đề xuất Ricci flow để tiến hóa metric về độ cong hằng. Singularity có thể xuất hiện; Perelman chỉ cách phẫu thuật, kiểm soát entropy và phân tích dài hạn để đa tạp đơn liên trở thành mặt cầu tròn sau hữu hạn phẫu thuật.

### Vì sao quan trọng

Phát biểu tôpô được chứng minh bằng PDE hình học—chuyển phương pháp vĩ đại của toán hiện đại.
""",
            },
        ],
    },
    {
        "num": "06",
        "en_title": "Mathematics of the Future",
        "vi_title": "Toán Học Của Tương Lai",
        "en_blurb": (
            "Areas where mathematics is still developing rapidly—AI, quantum "
            "information, networks, optimal transport, and more."
        ),
        "vi_blurb": (
            "Những lĩnh vực toán học đang phát triển nhanh—AI, thông tin "
            "lượng tử, mạng, vận chuyển tối ưu, và hơn thế."
        ),
        "topics": [
            {
                "slug": "Mathematics_of_AI",
                "en": "Mathematics of AI",
                "vi": "Toán học của AI",
                "en_body": """What mathematical principles explain why deep networks work—and fail?

### Frontiers

Approximation theory (what functions can nets represent?), optimization landscapes, generalization bounds, implicit bias of gradient methods, equivariant architectures, and mechanistic interpretability with linear algebra and dynamical systems.

### Why it matters

AI systems are mathematical objects at industrial scale. Better theory means safer, more efficient, and more reliable models.
""",
                "vi_body": """Nguyên lý toán học nào giải thích vì sao mạng sâu hoạt động—và thất bại?

### Tiên phong

Lý thuyết xấp xỉ, cảnh quan tối ưu, chặn tổng quát hóa, thiên kiến ẩn của gradient, kiến trúc đẳng biến, diễn giải cơ chế bằng đại số tuyến tính và hệ động lực.

### Vì sao quan trọng

Hệ AI là đối tượng toán ở quy mô công nghiệp; lý thuyết tốt hơn nghĩa là mô hình an toàn và hiệu quả hơn.
""",
            },
            {
                "slug": "Quantum_Information",
                "en": "Quantum Information",
                "vi": "Thông tin Lượng tử",
                "en_body": """**Quantum information** studies computation and communication using quantum states—superposition, entanglement, and measurement.

### Frontiers

Quantum algorithms (Shor, Grover, Hamiltonian simulation), error-correcting codes, entanglement theory, quantum cryptography, and the mathematics of tensor networks and operator algebras.

### Why it matters

It redefines what is efficiently computable and how information can be secured—rooted in linear algebra over complex Hilbert spaces.
""",
                "vi_body": """**Thông tin lượng tử** nghiên cứu tính toán và truyền thông bằng trạng thái lượng tử—chồng chập, vướng víu, đo lường.

### Tiên phong

Thuật toán lượng tử (Shor, Grover), mã sửa sai, lý thuyết vướng víu, mật mã lượng tử, mạng tensor và đại số toán tử.

### Vì sao quan trọng

Định nghĩa lại cái gì tính được hiệu quả và bảo mật thông tin ra sao—gốc rễ là đại số tuyến tính trên không gian Hilbert phức.
""",
            },
            {
                "slug": "Mathematical_Biology",
                "en": "Mathematical Biology",
                "vi": "Toán Sinh học",
                "en_body": """**Mathematical biology** models life with equations and discrete structures—from neurons to ecosystems to evolution.

### Frontiers

Reaction–diffusion patterns, epidemiological networks, phylogenetic combinatorics, protein geometry, stochastic gene expression, and topological data analysis of biological shape.

### Why it matters

Biology generates high-dimensional, noisy data and complex feedback. Mathematics supplies mechanisms, not only statistics.
""",
                "vi_body": """**Toán sinh học** mô hình sự sống bằng phương trình và cấu trúc rời rạc—từ nơ-ron đến hệ sinh thái.

### Tiên phong

Mẫu reaction–diffusion, mạng dịch tễ, tổ hợp phát sinh loài, hình học protein, biểu hiện gen ngẫu nhiên, TDA hình dạng sinh học.

### Vì sao quan trọng

Sinh học tạo dữ liệu cao chiều, nhiễu và phản hồi phức tạp; toán cung cấp cơ chế, không chỉ thống kê.
""",
            },
            {
                "slug": "Network_Science",
                "en": "Network Science",
                "vi": "Khoa học Mạng",
                "en_body": """**Network science** studies structure and dynamics on graphs that model social, biological, and technological systems.

### Frontiers

Community detection, epidemic thresholds, higher-order networks (hypergraphs), temporal networks, and controllability of dynamical processes on graphs.

### Why it matters

From misinformation spread to power-grid stability, networked systems dominate modern infrastructure.
""",
                "vi_body": """**Khoa học mạng** nghiên cứu cấu trúc và động lực trên đồ thị mô hình hệ xã hội, sinh học, công nghệ.

### Tiên phong

Phát hiện cộng đồng, ngưỡng dịch, mạng bậc cao (siêu đồ thị), mạng thời gian, điều khiển quá trình động trên đồ thị.

### Vì sao quan trọng

Từ lan truyền tin giả đến ổn định lưới điện—hệ nối mạng chi phối hạ tầng hiện đại.
""",
            },
            {
                "slug": "Future_Cryptography",
                "en": "Cryptography (Frontiers)",
                "vi": "Mật mã học (Tiên phong)",
                "en_body": """Cryptography is racing toward a post-quantum world while expanding into privacy-preserving computation.

### Frontiers

Lattice-based and code-based schemes; fully homomorphic encryption; multiparty computation; zero-knowledge proofs and succinct arguments; isogeny-based ideas and their cryptanalysis.

### Why it matters

Security assumptions are mathematical conjectures with societal stakes. New primitives enable computation on encrypted data—an algebraic revolution in privacy.
""",
                "vi_body": """Mật mã đang chạy đua hậu lượng tử và mở rộng sang tính toán bảo vệ riêng tư.

### Tiên phong

Sơ đồ lưới và mã; mã hóa đồng cấu hoàn toàn; tính toán đa bên; zero-knowledge và lập luận ngắn gọn.

### Vì sao quan trọng

Giả định an ninh là giả thuyết toán có hệ quả xã hội; nguyên thủy mới cho phép tính trên dữ liệu đã mã hóa.
""",
            },
            {
                "slug": "Complexity_Theory",
                "en": "Complexity Theory",
                "vi": "Lý thuyết Độ phức tạp",
                "en_body": """Beyond P vs NP, complexity theory maps the landscape of efficient computation.

### Frontiers

Fine-grained complexity, circuit lower bounds, communication complexity, hardness of approximation, pseudorandomness, and average-case complexity for cryptography.

### Why it matters

It tells us which algorithmic improvements are plausible—and which would collapse entire webs of known hardness.
""",
                "vi_body": """Ngoài P vs NP, lý thuyết độ phức tạp vẽ bản đồ tính toán hiệu quả.

### Tiên phong

Fine-grained complexity, chặn dưới mạch, độ phức tạp giao tiếp, độ khó xấp xỉ, giả-ngẫu nhiên, độ phức tạp trường hợp trung bình cho mật mã.

### Vì sao quan trọng

Cho biết cải tiến thuật toán nào hợp lý—và cái nào sẽ sụp đổ cả mạng độ khó đã biết.
""",
            },
            {
                "slug": "High_Dimensional_Geometry",
                "en": "High-Dimensional Geometry",
                "vi": "Hình học Cao chiều",
                "en_body": """In high dimensions, intuition from 2D and 3D systematically fails—and new phenomena appear.

### Frontiers

Concentration of measure, random polytopes, embedding theorems, manifold learning, and the geometry of high-dimensional convex bodies (asymptotic geometric analysis).

### Why it matters

Data is high-dimensional. Understanding typical geometry is essential for statistics, optimization, and CS theory.
""",
                "vi_body": """Ở chiều cao, trực giác 2D/3D thường sai—và hiện tượng mới xuất hiện.

### Tiên phong

Tập trung độ đo, đa diện ngẫu nhiên, định lý nhúng, học đa tạp, hình học vật thể lồi cao chiều.

### Vì sao quan trọng

Dữ liệu cao chiều; hiểu hình học điển hình thiết yếu cho thống kê, tối ưu và CS lý thuyết.
""",
            },
            {
                "slug": "Optimal_Transport",
                "en": "Optimal Transport",
                "vi": "Vận chuyển Tối ưu",
                "en_body": """**Optimal transport** asks how to move mass from one distribution to another at minimal cost.

### Frontiers

Wasserstein geometry, computational OT (Sinkhorn), gradient flows in probability space, applications to generative models, economics, and PDEs (e.g., linking to porous medium equations).

### Why it matters

It provides a metric geometry on the space of probability measures—unifying analysis, probability, and data science.
""",
                "vi_body": """**Vận chuyển tối ưu** hỏi cách chuyển khối lượng từ phân bố này sang phân bố khác với chi phí nhỏ nhất.

### Tiên phong

Hình học Wasserstein, OT tính toán (Sinkhorn), dòng gradient trên không gian xác suất, mô hình sinh, kinh tế, PDE.

### Vì sao quan trọng

Cung cấp hình học metric trên không gian độ đo xác suất—thống nhất giải tích, xác suất và khoa học dữ liệu.
""",
            },
            {
                "slug": "ML_Theory",
                "en": "Machine Learning Theory",
                "vi": "Lý thuyết Học máy",
                "en_body": """**Learning theory** formalizes what it means to generalize from samples.

### Frontiers

PAC learning, Rademacher complexity, double descent and interpolation, online learning, causal learning, and theory of overparameterized models.

### Why it matters

Practice often outruns classical bounds. New theory aims to explain modern regimes where models fit noise yet still predict well.
""",
                "vi_body": """**Lý thuyết học** hình thức hóa việc tổng quát hóa từ mẫu.

### Tiên phong

PAC, độ phức tạp Rademacher, double descent, học trực tuyến, học nhân quả, mô hình quá tham số.

### Vì sao quan trọng

Thực tiễn thường vượt chặn cổ điển; lý thuyết mới nhằm giải thích chế độ mô hình khớp nhiễu nhưng vẫn dự đoán tốt.
""",
            },
            {
                "slug": "Mathematical_Physics",
                "en": "Mathematical Physics",
                "vi": "Vật lý Toán",
                "en_body": """**Mathematical physics** builds rigorous foundations for physical theories and exports physical ideas into pure math.

### Frontiers

Constructive QFT, spectral theory, integrable systems, topological phases, general relativity’s global analysis, and random matrix universality.

### Why it matters

Physics suggests structures; mathematics makes them theorems. The dialogue continues to generate Fields-level mathematics.
""",
                "vi_body": """**Vật lý toán** xây nền tảng chặt cho lý thuyết vật lý và xuất khẩu ý tưởng vật lý vào toán thuần túy.

### Tiên phong

QFT kiến thiết, lý thuyết phổ, hệ khả tích, pha tôpô, phân tích toàn cục tương đối tổng quát, phổ quát ma trận ngẫu nhiên.

### Vì sao quan trọng

Vật lý gợi cấu trúc; toán biến chúng thành định lý—đối thoại tiếp tục sinh toán tầm Fields.
""",
            },
        ],
    },
    {
        "num": "07",
        "en_title": "Mathematical Explorations",
        "vi_title": "Khám Phá Toán Học",
        "en_blurb": (
            "Open-ended investigations where there may be no immediate answer. "
            "Experiment, conjecture, visualize, and reason."
        ),
        "vi_blurb": (
            "Các điều tra mở, có thể chưa có câu trả lời ngay. Hãy thử nghiệm, "
            "đưa ra giả thuyết, hình dung và lập luận."
        ),
        "topics": [
            {
                "slug": "Explore_Kakeya",
                "en": "What is the smallest possible Kakeya set?",
                "vi": "Tập Kakeya nhỏ nhất có thể là gì?",
                "en_body": """A Kakeya set contains a unit segment in every direction. In the plane and higher dimensions, how “small” can such a set be?

### Explore

- Can you draw (or code) a set that contains many directions with small area?
- Look up Besicovitch’s construction: measure zero is possible—does that match your intuition?
- What should “small” mean—area, Hausdorff dimension, Minkowski dimension?

### Prompts

Formulate a conjecture for dimension 2, then ask what changes in dimension 3. Compare with recent news on the Kakeya conjecture.
""",
                "vi_body": """Tập Kakeya chứa đoạn đơn vị theo mọi hướng. Trong mặt phẳng và chiều cao, tập như vậy có thể “nhỏ” đến mức nào?

### Khám phá

- Vẽ (hoặc lập trình) tập chứa nhiều hướng với diện tích nhỏ?
- Tìm hiểu xây dựng Besicovitch: độ đo không là có thể—có khớp trực giác?
- “Nhỏ” nghĩa là gì—diện tích, chiều Hausdorff, Minkowski?

### Gợi ý

Đặt giả thuyết cho chiều 2, rồi hỏi chiều 3 đổi gì. So với tin tức gần đây về giả thuyết Kakeya.
""",
            },
            {
                "slug": "Explore_Sphere_Packing",
                "en": "How can we pack spheres most efficiently?",
                "vi": "Xếp cầu hiệu quả nhất như thế nào?",
                "en_body": """Orange-stacking in a market is a 3D packing problem. What is optimal in higher dimensions?

### Explore

- Why is the face-centered cubic packing efficient in 3D (Kepler’s conjecture, proved by Hales)?
- What special lattices appear in dimensions 8 and 24?
- Can you invent a packing in 2D and compute its density?

### Prompts

Relate packing density to coding theory: sphere packing and error-correcting codes share geometry.
""",
                "vi_body": """Xếp cam ngoài chợ là bài toán xếp 3D. Tối ưu ở chiều cao là gì?

### Khám phá

- Vì sao xếp lập phương tâm mặt hiệu quả trong 3D (giả thuyết Kepler, Hales)?
- Mạng đặc biệt nào xuất hiện ở chiều 8 và 24?
- Tự nghĩ một cách xếp 2D và tính mật độ?

### Gợi ý

Liên hệ mật độ xếp với lý thuyết mã: xếp cầu và mã sửa sai cùng hình học.
""",
            },
            {
                "slug": "Explore_Prime_Predictability",
                "en": "How predictable are prime numbers?",
                "vi": "Số nguyên tố dự đoán được đến mức nào?",
                "en_body": """Primes look irregular locally yet obey global laws (prime number theorem). How far does predictability go?

### Explore

- Plot gaps between primes up to a few thousand. What patterns appear?
- Compare with a random model (Cramér’s model). Where does randomness help or mislead?
- What does the twin prime conjecture claim about predictability of a simple pattern?

### Prompts

Distinguish statistical prediction from deterministic formulas that generate all primes.
""",
                "vi_body": """Số nguyên tố trông bất quy tắc cục bộ nhưng tuân luật toàn cục (định lý số nguyên tố). Khả năng dự đoán đi đến đâu?

### Khám phá

- Vẽ khoảng cách giữa các nguyên tố đến vài nghìn. Mẫu gì xuất hiện?
- So với mô hình ngẫu nhiên (Cramér). Ngẫu nhiên giúp hay đánh lừa?
- Giả thuyết sinh đôi nói gì về một mẫu đơn giản?

### Gợi ý

Phân biệt dự đoán thống kê với công thức tất định sinh mọi nguyên tố.
""",
            },
            {
                "slug": "Explore_Randomness_Order",
                "en": "Can randomness create order?",
                "vi": "Ngẫu nhiên có tạo ra trật tự?",
                "en_body": """Random constructions often produce highly structured objects—expanders, codes, graphs without short cycles.

### Explore

- Flip coins to build a random graph; estimate connectivity thresholds.
- Why do random methods prove existence of objects we cannot easily construct?
- Where does derandomization succeed?

### Prompts

Connect to the probabilistic method in combinatorics and to concentration: order can be a typical property of noise.
""",
                "vi_body": """Xây dựng ngẫu nhiên thường tạo đối tượng rất có cấu trúc—expander, mã, đồ thị không chu trình ngắn.

### Khám phá

- Tung đồng xu xây đồ thị ngẫu nhiên; ước lượng ngưỡng liên thông.
- Vì sao phương pháp ngẫu nhiên chứng minh tồn tại thứ ta khó xây tường minh?
- Derandomization thành công ở đâu?

### Gợi ý

Nối với phương pháp xác suất trong tổ hợp và tập trung độ đo: trật tự có thể là tính chất điển hình của nhiễu.
""",
            },
            {
                "slug": "Explore_Fourth_Dimension",
                "en": "What does a fourth dimension look like?",
                "vi": "Chiều thứ tư trông như thế nào?",
                "en_body": """We cannot see 4D directly, but we can project, slice, and reason by analogy.

### Explore

- How does a 3D being perceive a 4D hypercube passing through 3-space?
- Build coordinates $$(x,y,z,w)$$ and compute distances; generalize the sphere equation.
- Which properties of knots change in 4D?

### Prompts

Use linear algebra (orthonormal bases, projections) as a vision prosthetic for higher dimensions.
""",
                "vi_body": """Ta không thấy 4D trực tiếp, nhưng có thể chiếu, cắt lát và suy luận theo loại suy.

### Khám phá

- Sinh vật 3D “nhìn” siêu lập phương 4D xuyên không gian 3 ra sao?
- Dùng tọa độ $$(x,y,z,w)$$; tổng quát phương trình mặt cầu.
- Tính chất nút thắt đổi gì trong 4D?

### Gợi ý

Dùng đại số tuyến tính (cơ sở trực chuẩn, phép chiếu) như “thị giác giả” cho chiều cao.
""",
            },
            {
                "slug": "Explore_Map_Colors",
                "en": "How many colors are really needed to color a map?",
                "vi": "Cần bao nhiêu màu để tô bản đồ?",
                "en_body": """Four colors suffice for planar maps—but what if the surface changes?

### Explore

- Find a map that needs four colors (try to draw one).
- On a torus, the chromatic number of the surface is higher—can you find the formula $$\\bigl\\lfloor \\tfrac{7 + \\sqrt{1+48g}}{2}\\bigr\\rfloor$$ for genus $$g$$?
- What fails if countries can be disconnected?

### Prompts

Separate the planar four color theorem from Heawood’s map color theorem on higher surfaces.
""",
                "vi_body": """Bốn màu đủ cho bản đồ phẳng—nhưng nếu mặt đổi thì sao?

### Khám phá

- Tìm bản đồ cần bốn màu.
- Trên torus, số màu cao hơn—công thức Heawood theo giống $$g$$?
- Điều gì hỏng nếu quốc gia không liên thông?

### Gợi ý

Tách định lý bốn màu phẳng khỏi định lý tô màu Heawood trên mặt giống cao.
""",
            },
            {
                "slug": "Explore_Describe_Infinity",
                "en": "Can mathematics describe infinity?",
                "vi": "Toán học mô tả được vô hạn?",
                "en_body": """Infinity appears as process, as completed size, and as divergent behavior. Which descriptions are coherent?

### Explore

- Compare $$\\infty$$ in calculus (limits) with infinite sets in set theory.
- Is there a largest infinity? What does Cantor’s theorem say?
- Where do paradoxes force axiomatic care?

### Prompts

Write two short paragraphs: one treating infinity as a limit, one as a cardinality—and note what each forbids.
""",
                "vi_body": """Vô hạn xuất hiện như quá trình, như kích thước hoàn chỉnh, và như hành vi phân kỳ. Mô tả nào nhất quán?

### Khám phá

- So $$\\infty$$ trong giải tích (giới hạn) với tập vô hạn trong lý thuyết tập.
- Có vô hạn lớn nhất? Định lý Cantor nói gì?
- Nghịch lý buộc thận trọng tiên đề ở đâu?

### Gợi ý

Viết hai đoạn: vô hạn như giới hạn và như lực lượng—ghi điều mỗi cách cấm.
""",
            },
            {
                "slug": "Explore_Iteration",
                "en": "What happens when a rule is iterated forever?",
                "vi": "Điều gì xảy ra khi lặp một quy tắc mãi mãi?",
                "en_body": """Iteration turns a simple map $$x \\mapsto f(x)$$ into dynamics: fixed points, cycles, chaos, escape to infinity.

### Explore

- Iterate the logistic map $$x \\mapsto rx(1-x)$$ for various $$r$$; watch period doubling.
- Try Collatz on random seeds; record stopping times.
- How does complex iteration $$z \\mapsto z^2 + c$$ produce fractal boundaries?

### Prompts

Classify long-term fates: converge, cycle, dense orbit, diverge. Ask which fate is stable under perturbation.
""",
                "vi_body": """Lặp biến ánh xạ đơn giản $$x \\mapsto f(x)$$ thành động lực: điểm bất động, chu trình, hỗn độn, thoát ra vô hạn.

### Khám phá

- Lặp logistic $$x \\mapsto rx(1-x)$$ theo $$r$$; quan sát nhân đôi chu kỳ.
- Thử Collatz; ghi thời gian dừng.
- Lặp phức $$z \\mapsto z^2 + c$$ tạo biên fractal ra sao?

### Gợi ý

Phân loại số phận dài hạn: hội tụ, chu trình, quỹ đạo trù mật, phân kỳ. Cái nào ổn định dưới nhiễu?
""",
            },
        ],
    },
]


OWNER = "Nguyen Le Linh"


def write_index(lang: str, num: str, title: str) -> None:
    path = CONTENTS / lang / f"chapter{num}" / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
layout: page
lang: {lang}
title: "{title}"
chapter: "{num}"
owner: "{OWNER}"
---
""",
        encoding="utf-8",
    )


def write_overview(
    lang: str,
    num: str,
    title: str,
    blurb: str,
    topic_titles: list[str],
) -> None:
    posts = CONTENTS / lang / f"chapter{num}" / "_posts"
    posts.mkdir(parents=True, exist_ok=True)
    slug = "Overview" if lang == "en" else "Tong_quan"
    title_full = f"Overview: {title}" if lang == "en" else f"Tổng quan: {title}"
    if lang == "en":
        body = f"""{blurb}

## Topics in this section

"""
        for i, t in enumerate(topic_titles, 1):
            body += f"{i}. {t}\n"
        body += """
## How to read this section

Work through the essays in any order. Each page is written to stand alone: it states the central question, explains why the topic is hard or beautiful, and points toward the mathematics that grows around it. Use the language switch when a Vietnamese version is available.

## Learning goals

After exploring this section, you should be able to:

- State the main questions or themes of the section in your own words.
- Explain at least one deep idea or open problem with correct intuition (not only a slogan).
- See how the topics connect to the rest of Math Enthusiast—problems, proofs, applications, or explorations.
"""
    else:
        body = f"""{blurb}

## Các chủ đề trong phần này

"""
        for i, t in enumerate(topic_titles, 1):
            body += f"{i}. {t}\n"
        body += """
## Cách đọc phần này

Bạn có thể đọc các bài theo bất kỳ thứ tự nào. Mỗi trang được viết để đứng độc lập: nêu câu hỏi trung tâm, giải thích vì sao chủ đề khó hoặc đẹp, và chỉ ra toán học phát triển xung quanh. Dùng nút chuyển ngôn ngữ khi bản tiếng Anh/Việt tương ứng có sẵn.

## Mục tiêu học tập

Sau khi khám phá phần này, bạn có thể:

- Nêu các câu hỏi hoặc chủ đề chính bằng lời của mình.
- Giải thích ít nhất một ý tưởng sâu hoặc bài toán mở với trực giác đúng (không chỉ khẩu hiệu).
- Thấy cách các chủ đề nối với phần còn lại của khóa học—bài toán, chứng minh, ứng dụng, hoặc khám phá.
"""
    path = posts / f"21-01-01-{num}_00_{slug}.md"
    path.write_text(
        f"""---
layout: post
title: "{title_full}"
chapter: '{num}'
order: 1
owner: {OWNER}
lang: {lang}
categories:
- chapter{num}
---

{body}
""",
        encoding="utf-8",
    )


def write_topic(
    lang: str,
    num: str,
    order: int,
    slug: str,
    title: str,
    body: str,
) -> None:
    posts = CONTENTS / lang / f"chapter{num}" / "_posts"
    posts.mkdir(parents=True, exist_ok=True)
    fname = f"21-01-01-{num}_{order:02d}_{slug}.md"
    path = posts / fname
    if lang == "en":
        footer = """
## Further directions

- Revisit related essays in other sections (problems, proofs, applications, or explorations).
- Try to restate the core idea in one paragraph without looking back.
- Note one precise question you still have—good questions are part of mathematical practice.
"""
    else:
        footer = """
## Hướng đi tiếp

- Xem lại các bài liên quan ở phần khác (bài toán, chứng minh, ứng dụng, khám phá).
- Thử phát biểu lại ý tưởng cốt lõi trong một đoạn mà không nhìn lại.
- Ghi một câu hỏi chính xác bạn vẫn còn—câu hỏi tốt là một phần của thực hành toán học.
"""
    path.write_text(
        f"""---
layout: post
title: "{title}"
chapter: '{num}'
order: {order}
owner: {OWNER}
lang: {lang}
categories:
- chapter{num}
---

{body.rstrip()}
{footer}
""",
        encoding="utf-8",
    )


def main() -> None:
    for ch in CHAPTERS:
        num = ch["num"]
        write_index("en", num, ch["en_title"])
        write_index("vi", num, ch["vi_title"])

        en_titles = [t["en"] for t in ch["topics"]]
        vi_titles = [t["vi"] for t in ch["topics"]]
        write_overview("en", num, ch["en_title"], ch["en_blurb"], en_titles)
        write_overview("vi", num, ch["vi_title"], ch["vi_blurb"], vi_titles)

        for i, topic in enumerate(ch["topics"], start=2):
            write_topic("en", num, i, topic["slug"], topic["en"], topic["en_body"])
            write_topic("vi", num, i, topic["slug"], topic["vi"], topic["vi_body"])

        print(f"chapter{num}: {len(ch['topics'])} topics (+ overview) × 2 langs")

    print("Done.")


if __name__ == "__main__":
    main()
