---
layout: post
title: "Wigderson: Ngẫu nhiên, Chứng minh và Độ phức tạp (Turing 2023)"
chapter: '09'
order: 13
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**Avi Wigderson** nhận **A.M. Turing Award 2023**

> “for foundational contributions to the theory of computation, including reshaping our understanding of the role of randomness in computation, and for his decades of intellectual leadership in theoretical computer science.”  
> — [ACM Turing Award](https://amturing.acm.org/)

Hai năm trước, **Abel Prize 2021** (chung Lovász) đã kéo Wigderson vào spotlight toán thuần; Turing 2023 khẳng định cùng sự nghiệp từ phía ACM. Bài này **không** lặp [chân dung Abel]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/) nguyên văn: nó đào **ngẫu nhiên như tài nguyên**, **derandomization**, **expander**, **interactive proof / zero-knowledge văn hóa**, và worldview *Mathematics and Computation*. Đọc cặp đôi Abel+Turing: một giải nhấn “toán trung tâm”, một giải nhấn “tính toán trung tâm”—cùng người, cùng thông điệp hai chiều. Nền: [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/), [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/).

---

## Mục tiêu học tập

Sau bài, bạn có thể giải thích **BPP** vs **P** như câu hỏi “ngẫu nhiên có cần cho poly-time không?”; mô tả **derandomization** dưới giả thiết hardness (PRG lừa mạch kích thước bị chặn); định nghĩa **expander family** mức khẩu hiệu (thưa + spectral gap / edge expansion); nêu vì sao expander là “pseudorandomness nhập thể”; nối interactive proofs ($$\mathbf{IP}=\mathbf{PSPACE}$$) với ý “chứng minh tương tác + xu”; phân biệt Turing 2023 và Abel 2021 mà không gộp thành “đã giải P vs NP”; phê nhầm “thuật toán ngẫu nhiên luôn thắng” và “derandomization = tắt RNG trong code production”.

**Kiến thức nền.** Xác suất cơ bản; lớp P/NP; đồ thị chính quy. Đã đọc [Lovász–Wigderson Abel]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/) là lợi thế, không bắt buộc.

---

## 1. Ngẫu nhiên: tiện lợi hay sức mạnh?

### Thuật toán ngẫu nhiên ở đâu

Kiểm tra nguyên tố lịch sử (Miller–Rabin), polynomial identity testing (PIT), hashing, sampling, volume estimation, routing—nhiều protocol **đơn giản hơn** hoặc **duy nhất biết** khi có xu. Lớp **BPP**: quyết định poly-time, lỗi hai phía chặn (ví dụ $$\le 1/3$$, khuếch đại bằng lặp).

Câu hỏi Wigderson-shaped: liệu $$\mathbf{P}=\mathbf{BPP}$$? Nếu đúng, mọi randomized poly-time decision (lỗi chặn) có bản deterministic poly-time. Đây **không** đã chứng minh; đây là **thế giới conjecture** nuôi cả PRG theory.

### Randomness như tài nguyên đo được

Số bit ngẫu nhiên là cost—như thời gian và không gian. Seed ngắn + **stretch** thành chuỗi dài trông ngẫu nhiên với observer yếu = **pseudorandom generator**. Chất lượng PRG đo bằng class test (mạch size $$s$$, time $$t$$, …).

Yao đã nối indistinguishability với hardness; dòng Impagliazzo–Wigderson và Nisan–Wigderson cho thấy: **nếu có hàm đủ cứng với mạch**, thì có PRG đủ mạnh để derandomize BPP. Hardness ⇒ randomness “rẻ”. Đảo văn hóa: lower bound không chỉ tiêu cực.

---

## 2. Derandomization: chương trình, không nút bấm

### Nisan–Wigderson generator (hình dạng)

Từ seed ngắn, tính các bit output bằng hàm cứng trên subset seed theo design combinatorial. Nếu hàm không xấp xỉ được bởi mạch nhỏ, output đánh lừa mạch test. Schema:

$$
\text{strong circuit lower bounds}\;\Rightarrow\;\text{PRG}\;\Rightarrow\;\mathbf{BPP}=\mathbf{P}
$$

trong các định lý “nếu–thì” chính xác (size, average-case hardness…).

### Ý nghĩa sư phạm

Derandomization **có điều kiện** là thành tựu: ta hiểu *cái giá* randomness. Nó khác “viết lại code bỏ `random()`”. PIT và một số bài vẫn là front: black-box vs white-box derandomization, hardness vs randomness tradeoffs.

### Connection to crypto

PRG crypto đòi observer adversarial poly-time mạnh; PRG complexity cho derandomization có thể nhắm class mạch cụ thể. Cùng tinh thần computational indistinguishability—xem [mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) và [Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/).

---

## 3. Expander graphs: đồ thị thưa, hành xử ngẫu nhiên

### Định nghĩa làm việc

Họ $$\{G_n\}$$ $$d$$-chính quy, $$d$$ cố định, $$n\to\infty$$, là **expander** nếu hằng số Cheeger / spectral gap

$$
\lambda_2(G_n)\le d-\varepsilon
$$

(hoặc edge expansion $$h(G)\ge\varepsilon$$) với $$\varepsilon>0$$ độc lập $$n$$. Random walks trộn nhanh: sau $$O(\log n)$$ bước gần stationary.

### Dùng làm gì

- **Derandomization:** walk trên expander tiết kiệm bit so random thuần khi sample.  
- **Mã sửa lỗi** và concentrators.  
- **Proofs** probabilistic method constructive.  
- **Toán thuần:** dựng tường minh (Margulis, LPS, …) nối [nhóm và động lực]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/).

Expander là chỗ **Lovász-world** (cấu trúc đồ thị) gặp **Wigderson-world** (pseudorandomness). Abel 2021 ngồi đúng giao điểm; Turing 2023 nhấn phía randomness/complexity.

### Explicit vs random

Đồ thị ngẫu nhiên thường expand với high probability—nhưng thuật toán cần **mô tả ngắn** và xây dựng deterministic. Explicit expanders là vàng: tồn tại + dùng được trong circuit/algorithm.

---

## 4. Chứng minh tương tác, zero-knowledge, IP = PSPACE

### Interactive proof

Verifier poly-time tương tác với prover không giới hạn; completeness / soundness với xu. **$$\mathbf{IP}=\mathbf{PSPACE}$$** (Shamir; Lund–Fortnow–Karloff–Nisan lineage) là định lý chấn động: tương tác + randomness cho phép chứng minh mọi language bộ nhớ poly. Wigderson nằm trong hệ sinh thái zero-knowledge và randomness in proofs—cùng văn hóa Goldwasser–Micali–Rackoff.

### Zero-knowledge

Prover thuyết phục verifier mệnh đề đúng **mà không leak** gì thêm. Ngẫu nhiên và simulator là xương. Ứng dụng crypto protocol; ý niệm “chứng minh không lộ witness” là di sản TCS mang toán xác suất–complexity.

Khóa học Math Enthusiast: **chứng minh không còn chỉ là văn bản tĩnh**. Tương tác và xu đổi class power—song song Gödel-era “proof = string” mở rộng.

---

## 5. Mathematics and Computation: worldview

Sách và bài giảng Wigderson trình bày TCS như **toán**: định lý, open problems kiểu Hilbert, cầu đại số–giải tích–tổ hợp. Thông điệp trùng Abel citation “central fields of modern mathematics”, nay thêm Turing “intellectual leadership”.

Open problems tiêu biểu vẫn mở:

- P vs NP (và circuit lower bounds mạnh).  
- $$\mathbf{P}$$ vs $$\mathbf{BPP}$$ unconditional.  
- Explicit objects (extractors, expanders tối ưu, rigid matrices…).  
- VP vs VNP (đại số).

[P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) vẫn là Everest; công trình Wigderson là **địa hình và dụng cụ** quanh núi—không phải cờ trên đỉnh.

---

## 6. Turing 2023 vs Abel 2021 (đọc giải đúng)

| | Abel 2021 | Turing 2023 |
|--|-----------|-------------|
| Đồng giải | Lovász + Wigderson | Wigderson (cá nhân) |
| Nhấn | Discrete math + TCS là toán trung tâm | Randomness trong computation + leadership TCS |
| Khán giả | Cộng đồng toán quốc tế | ACM / computing |

Không “đổi năm cho vui”. Hai giải **bổ sung**. Seminar có thể so citation word-by-word: overlap “foundations”, khác “randomness” vs “discrete mathematics” pairing.

---

## 7. Nhầm lẫn thường gặp

| Tuyên bố | Chỉnh |
|----------|--------|
| “Wigderson giải P vs NP.” | Không. |
| “BPP = P đã chứng minh.” | Có điều kiện hardness; unconditional vẫn mở. |
| “Expander = đồ thị random.” | Random thường expand; điểm là *explicit* + dùng deterministic. |
| “Interactive proof = zero-knowledge luôn.” | ZK là tính chất thêm; IP là class power. |
| “Turing 2021.” | Abel 2021; **Turing Award của Wigderson là 2023**. |
| “Derandomization vô dụng thực tế.” | Vừa lý thuyết class, vừa kỹ thuật tiết kiệm entropy / seed. |

---

## 8. Studio: hardness ⇒ PRG một trang

1. Giả sử $$f:\{0,1\}^{k}\to\{0,1\}$$ hard on average cho mạch size $$s$$.  
2. Design subsets $$S_1,\ldots,S_m\subset[t]$$ của seed length $$t$$.  
3. Output bit $$i$$: $$f(\mathrm{seed}|_{S_i})$$.  
4. Hybrid argument: nếu test phân biệt output với random, xây mạch xấp xỉ $$f$$—mâu thuẫn hardness.  
5. Kết luận: seed $$t\ll m$$ đủ cho test class size $$s$$.

Chi tiết combinatorial design và parameters là sách giáo khoa; skeleton trên đủ để *đọc* survey derandomization.

---

## 9. Extractors, dilute randomness, và “weak random sources”

Không phải mọi thực tế đều có bit hoàn hảo. **Randomness extractors** chưng cất nguồn entropy yếu (min-entropy bị chặn) thành bit gần đều, đôi khi với seed ngắn public. Lý thuyết extractor giao expander, hashing phổ dụng, và crypto. Wigderson-era TCS coi entropy thô như nguyên liệu; câu hỏi là *chưng cất được bao nhiêu, với giả thiết nào*. Đây là tầng dưới RNG thư viện: trước khi tin `random()`, hỏi mô hình entropy.

### Coding và pseudorandomness

Mã sửa lỗi, expanders, và extractors chia toolkit tuyến tính–tổ hợp. Một code tốt vừa chống nhiễu kênh vừa (trong một số chế độ) cho object pseudorandom. Worldview: **các định nghĩa “trông ngẫu nhiên với observer bị giới hạn”** lặp lại từ communication tests đến circuit tests đến statistical distance.

### Vì sao leadership quan trọng trong citation

Turing 2023 nêu *decades of intellectual leadership*: open problem lists, mentoring, books, “what is the right question?”. Math Enthusiast học được: giải thưởng đôi khi vinh danh **kiến trúc lĩnh vực**, không chỉ một lemma. Song song Abel “shaping them into central fields”. Khi viết essay seminar, tách *định lý bạn trích* khỏi *chương trình bạn theo*.

---

## Bài tập

1. Định nghĩa BPP mức khẩu hiệu; nêu một thuật toán ngẫu nhiên bạn biết.  
2. Derandomization muốn đạt gì với BPP? ≤80 từ.  
3. Expander: một câu “thưa nhưng trộn nhanh”.  
4. **≤200 từ:** Hardness có thể *tạo* PRG—giải thích tinh thần không proof.  
5. So Turing 2023 và Abel 2021 bằng bảng 3 dòng của bạn.  
6. Nối [Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/): minimax / communication vs randomness resource—một giống (tài nguyên tinh), một khác.  
7. **Seminar:** Đọc abstract *Mathematics and Computation* (hoặc chapter online); chọn 2 open problems; gắn với P vs NP hay không.

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/wigderson-complexity/`.

**Khẩu hiệu từ gói nghiên cứu**

- **Turing 2023** (không 2021); Abel 2021 chung Lovász.
- Ngẫu nhiên–hardness; expander; IP.

**Thứ tự xem gợi ý**

1. **CORE** — Wigderson Turing Award Lecture (ACM): [https://www.youtube.com/watch?v=f2NiGO8zC1c](https://www.youtube.com/watch?v=f2NiGO8zC1c).  
2. **ORIENTATION** — IAS Q&A Wigderson Turing: [https://www.youtube.com/watch?v=TK_vD-VnsFw](https://www.youtube.com/watch?v=TK_vD-VnsFw).  
3. **ORIENTATION** — CACM June 2024 Wigderson feature: [https://www.youtube.com/watch?v=Ur9XNF6TeYw](https://www.youtube.com/watch?v=Ur9XNF6TeYw).  
4. **RELATED** — Wigderson — Reading Alan Turing (Berkeley): [https://www.youtube.com/watch?v=BiFSUniv70c](https://www.youtube.com/watch?v=BiFSUniv70c).  
5. **CROSS** — Abel lectures Lovász & Wigderson: [https://www.youtube.com/watch?v=zqiL57ebP-k](https://www.youtube.com/watch?v=zqiL57ebP-k).  

**Cổng chính thức / tài liệu**

- Wigderson Turing 2023 page: https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
- Wigderson Turing lecture page: https://amturing.acm.org/vp/wigderson_3844537.cfm  
- Abel 2021 Lovász & Wigderson: https://abelprize.no/abel-prize-laureates/2021  

Danh mục URL đầy đủ: `research/video-research/wigderson-complexity/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/wigderson-complexity/transcripts/` · trạng thái: `research/video-research/wigderson-complexity/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/wigderson-complexity_f2NiGO8zC1c_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu tham khảo


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/wigderson-complexity/references.md`.

1. Wigderson Turing 2023 page — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
2. Wigderson Turing lecture page — https://amturing.acm.org/vp/wigderson_3844537.cfm  
3. Wigderson Turing Award Lecture (ACM) — https://www.youtube.com/watch?v=f2NiGO8zC1c  
4. IAS Q&A Wigderson Turing — https://www.youtube.com/watch?v=TK_vD-VnsFw  
5. CACM June 2024 Wigderson feature — https://www.youtube.com/watch?v=Ur9XNF6TeYw  
6. Wigderson — Reading Alan Turing (Berkeley) — https://www.youtube.com/watch?v=BiFSUniv70c  
7. Abel 2021 Lovász & Wigderson — https://abelprize.no/abel-prize-laureates/2021  
8. Abel lectures Lovász & Wigderson — https://www.youtube.com/watch?v=zqiL57ebP-k  
9. Wikipedia — Avi Wigderson — https://en.wikipedia.org/wiki/Avi_Wigderson  
10. byyear listing (confirm 2023) — https://amturing.acm.org/byyear.cfm  
11. Mathematics and Computation (book info) — https://www.math.ias.edu/avi/book  
12. Thư mục gói: `research/video-research/wigderson-complexity/`.

1. ACM Turing Award — Avi Wigderson (2023).  
2. Abel Prize 2021 — Lovász & Wigderson; [bài khóa]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).  
3. Wigderson — *Mathematics and Computation* (Princeton).  
4. Arora & Barak — derandomization, IP, expanders chapters.  
5. Vadhan — survey pseudorandomness; Hoory–Linial–Wigderson expander survey.  
6. Khóa: [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/); [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/); [Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/); [Furstenberg–Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/).

---

## Hướng đi tiếp

- Cặp Abel: [Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).  
- Communication & minimax: [Yao]({{ site.baseurl }}/contents/vi/chapter09/09_08_Yao_Complexity/).  
- Crypto PRG: [mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/).  
- Thực hành: mô phỏng random walk trên cycle vs expander nhỏ; đo mixing.  
- Đọc: expander survey intro → NW generator sketch → một chapter Wigderson book.  
- Tiếp: [Chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/).
