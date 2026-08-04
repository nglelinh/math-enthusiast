---
layout: post
title: "Lovász & Wigderson: Toán rời rạc và TCS (Abel 2021)"
chapter: '08'
order: 6
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

**Abel Prize 2021** trao chung cho **László Lovász** và **Avi Wigderson**

> “for their foundational contributions to theoretical computer science and discrete mathematics, and their leading role in shaping them into central fields of modern mathematics.”  
> — [Citation ủy ban Abel](https://abelprize.no/abel-prize-laureates/2021)

Bài này giải thích vì sao toán rời rạc và theoretical computer science (TCS) nhận giải “toán thuần cốt lõi” tầm trọn đời; **local lemma** Lovász, lý thuyết đồ thị, tối ưu tổ hợp đóng góp gì; **randomness, derandomization, expander, độ phức tạp** trong thế giới Wigderson đóng góp gì; và đặt giải cạnh [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) vẫn mở mà không nhầm. Tài liệu: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài, bạn có thể giải thích vì sao rời rạc/TCS xứng Abel như toán hiện đại trung tâm; nêu local lemma Lovász và mục đích (tồn tại khi nhiều sự kiện xấu gần độc lập); nêu chủ đề randomness / derandomization của Wigderson; mô tả expander như đồ thị thưa nhưng liên thông mạnh; nối tất cả với P vs NP **mà không** tuyên bố bài đó đã giải.

**Kiến thức nền.** Đồ thị (đỉnh, cạnh); xác suất cơ bản; ý thuật toán tốn thời gian theo kích thước input. Liên kết: [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [đồ thị & mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), [Furstenberg–Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/).

---

## 1. Giải văn hóa cũng như khoa học

Đồ thị, thuật toán, độ phức tạp từng bị coi ngoại vi “toán thuần cốt lõi” trong một số văn hóa thể chế—quan trọng nhưng tách khoa CS. Abel 2021 khẳng định công khai: các lĩnh vực này chứa **định lý cấu trúc sâu** và tương tác hình học, đại số, xác suất ở mức cao nhất.

Mệnh đề hai của citation quan trọng: “shaping them into central fields.” Đó là xây lĩnh vực, mentor, sách, danh sách bài toán, thập niên định lý—không một headline. Đọc citation Abel 2021 là luyện LO6: vinh danh **định hình**, không nhầm với “đã giải Everest của lĩnh vực.”

---

## 2. Lovász: toán rời rạc như khoa học toán

### Đồ thị, tối ưu, hình học

Công trình Lovász trải lý thuyết đồ thị, combinatorial optimization, biểu diễn hình học của đồ thị. Chủ đề lặp: đối tượng rời rạc mang bóng liên tục—embedding, semi-definite relaxation, lattice algorithm, và sau này văn hóa **graph limit** (graphon) mà ông giúp mở. Tối ưu trên cấu trúc tổ hợp trở thành khoa học toán nghiêm với duality, thuật toán, hardness.

### Lovász local lemma

**Local lemma** (Erdős–Lovász) là nguyên lý tồn tại sâu. Có nhiều “sự kiện xấu” $$A_i$$, mỗi cái xác suất nhỏ, mỗi cái chỉ phụ thuộc hữu hạn cái khác. Dưới giả thiết định lượng, xác suất **không** sự kiện xấu nào xảy ra vẫn dương:

$$
\mathbb{P}\Big(\bigcap_i A_i^c\Big) > 0.
$$

Union bound thất bại khi quá nhiều sự kiện; độc lập đầy đủ thất bại khi có phụ thuộc. Local lemma sống ở chế độ giữa: **phụ thuộc hạn chế**. Workhorse của tổ hợp, probabilistic method, và thiết kế thuật toán (kể cả phiên bản algorithmic sau này).

### Xây lĩnh vực

Ngoài định lý: định hình toán rời rạc với chuẩn chứng minh, cầu hình học/tối ưu, cộng đồng toàn cầu. Ngôn ngữ Abel “leading role” chỉ đây. Trọn đời toán rời rạc không chỉ là “chứng minh nhiều lemma,” mà là khiến ngôn ngữ ngành trở thành mặc định cho thế hệ sau.

---

## 3. Wigderson: randomness, complexity, pseudorandomness

### Randomness như tài nguyên

Chủ đề trung tâm Wigderson: khi nào **thuật toán ngẫu nhiên** vượt deterministic, và sức mạnh của randomness như tài nguyên tính toán? Nhiều thuật toán tung xu—kiểm tra nguyên tố Monte Carlo lịch sử, hashing, sampling, giao thức giao tiếp. Complexity hỏi randomness thiết yếu hay chỉ tiện.

### Derandomization

**Derandomization** hỏi khi nào gỡ được randomness—thường dưới **giả thiết hardness** (hàm khó thích hợp suy ra pseudorandom generator). Nếu thế giới đủ hardness tính toán, có thể có mô phỏng deterministic hiệu quả của thuật toán ngẫu nhiên. Nối lower bound complexity với thiết kế thuật toán một cách sâu: hardness không chỉ là rào cản, mà là nguyên liệu xây PRG.

### Expander, interactive proof, cầu toán thuần

**Expander graph** thưa nhưng liên thông mạnh—mixing giống ngẫu nhiên với ít cạnh. Xuất hiện trong derandomization, mã, mạng, và lý thuyết nhóm thuần (dựng tường minh lịch sử gồm expander kiểu Margulis). Thế giới Wigderson coi expander và họ hàng là **pseudorandomness nhập thể**.

Interactive proof, zero-knowledge, cấu trúc class complexity—cầu logic, đại số, thuật toán. Sách *Mathematics and Computation* trình bày TCS như toán cho cộng đồng toán rộng.

---

## 4. Expander: bản đồ giao điểm

Họ vô hạn đồ thị $$d$$-chính quy $$\{G_n\}$$ là **expander family** nếu spectral gap (hoặc hằng Cheeger) bị chặn dưới độc lập $$n$$. Tương đương: tập nhỏ giãn—lân cận tăng theo hệ số xác định.

Hệ quả: random walk trộn nhanh; mã và derandomization có đối tượng tường minh; toán thuần có spectral graph theory và dựng nhóm.

Lý thuyết đồ thị cấu trúc/hình học của Lovász và pseudorandomness của Wigderson gặp nhau ở expander. Abel 2021 ngồi giao điểm đó—và Abel 2020 Margulis đã chạm expander từ động lực/nhóm. Seminar có thể vẽ một tam giác: **cấu trúc đồ thị — randomness — động lực/nhóm**.

---

## 5. Bên cạnh P vs NP

[P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) vẫn mở. Abel 2021 **không** giải. Công trình Lovász–Wigderson là **toolkit và worldview** quanh hardness tính toán: kết quả dương, lý thuyết cấu trúc, randomness, tối ưu, và tính hợp pháp toán học của discrete complexity.

Thói quen seminar lành: liệt kê ba định lý TCS “dương” không cần lời giải P vs NP (ứng dụng local lemma; dựng expander; interactive proof; xấp xỉ dưới giả thiết complexity; …). Toán trọn đời gồm kiến trúc lĩnh vực, không chỉ Everest.

### Hardness như đối tượng toán

Dù chưa chốt P vs NP, complexity coi **hardness** là thứ có thể *dùng*: reduction, completeness, lower bound có điều kiện, giả thiết mật mã. Chương trình Wigderson thường biến hardness thành tài nguyên xây dựng—PRG lừa được test hiệu quả—nên thiết kế thuật toán và tư duy lower bound thành hai mặt một chủ đề. Tối ưu tổ hợp của Lovász cũng coi cấu trúc rời rạc như hình học: polytope, duality, ngưỡng xấp xỉ là định lý, không chỉ heuristic.

Đạo đức khóa học khớp chương 01: **cờ đầu mở không làm lĩnh vực trống**. Xung quanh P vs NP là nền văn minh toán trưởng thành.

---

## 6. Vì sao tầm Abel

Hai sự nghiệp, một thông điệp: toán rời rạc và TCS không công dân hạng hai trong toán thuần. Chúng có định lý sâu mang nội dung hình học/đại số; phương pháp xuất khẩu; bài mở tầm Hilbert (P vs NP trong số đó); hạ tầng (expander, PRG, lemma tổ hợp) dùng xuyên khoa học.

Lời ủy ban—“central fields of modern mathematics”—là luận đề bài này. Abel không “nâng cấp CS thành toán”; Abel **ghi nhận** rằng chúng đã là toán trung tâm từ lâu, và sự nghiệp hai laureate giúp cộng đồng toán rộng thấy rõ điều đó.

---

## 7. Nhầm lẫn

| Khẳng định | Chỉnh |
|------------|-------|
| “Abel 2021 giải P vs NP.” | Không. Vinh danh đóng góp nền tảng và định hình lĩnh vực. |
| “Rời rạc chỉ là thuật toán.” | Còn cấu trúc đồ thị, extremal combinatorics, lý thuyết tối ưu, … |
| “Thuật toán ngẫu nhiên luôn hơn.” | Randomness là tài nguyên có giá và chương trình derandomization. |
| “Expander chỉ là đồ thị ngẫu nhiên.” | Đồ thị ngẫu nhiên thường expand; điểm là dựng **tường minh** và dùng deterministic. |
| “Local lemma cần độc lập đầy đủ.” | Cần **phụ thuộc hạn chế**, định lượng cẩn thận. |

---

## Hardness như cấu trúc, không chỉ rào cản

TCS coi hardness tính toán như cấu trúc lý thuyết: hàm một chiều (nếu tồn tại) nuôi mật mã; hardness trung bình khác NP-completeness worst-case; giả thiết fine-grained tinh chỉnh P vs NP thành rào tốc độ chính xác. Hình học tổ hợp Lovász và worldview complexity Wigderson cùng cho thấy toán rời rạc sinh **định nghĩa sâu không thua lý thuyết continuum**.

**Gợi ý seminar.** Liệt kê ba định lý TCS vẫn thú vị ngay cả nếu P = NP (ví dụ lower bound complexity giao tiếp, giới hạn coding theory). Giải thích mỗi cái hai câu vì sao.

---

## Bài tập

1. Local lemma một câu cho người ngoài ngành.  
2. Ví dụ randomness giúp chứng minh tồn tại hoặc thuật toán (kể cả toy).  
3. Derandomization muốn đạt gì? ≤100 từ.  
4. **≤250 từ:** Lập luận TCS là toán thuần bằng ngôn ngữ citation Abel 2021.  
5. Nối [đồ thị & mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/): một câu expander và độ tin cậy mạng.  
6. Sau bài P vs NP: ba định lý TCS dương không cần P ≠ NP.

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/lovasz-wigderson/`.

**Khẩu hiệu từ gói nghiên cứu**

- Abel 2021: Lovász + Wigderson — TCS & toán rời rạc trung tâm.
- Wigderson còn **Turing 2023** (không phải 2021).
- Không giải P vs NP.

**Thứ tự xem gợi ý**

1. **CORE** — Abel lectures Lovász & Wigderson: [https://www.youtube.com/watch?v=zqiL57ebP-k](https://www.youtube.com/watch?v=zqiL57ebP-k).  
2. **HISTORY** — Abel interview Lovász & Wigderson: [https://www.youtube.com/watch?v=VAk0rtlKtMA](https://www.youtube.com/watch?v=VAk0rtlKtMA).  
3. **ORIENTATION** — WFSJ meet Lovász & Wigderson: [https://www.youtube.com/watch?v=J4yssMTZqC4](https://www.youtube.com/watch?v=J4yssMTZqC4).  
4. **ORIENTATION** — Short interview Lovász: [https://www.youtube.com/watch?v=wg0di8dK0eI](https://www.youtube.com/watch?v=wg0di8dK0eI).  
5. **ORIENTATION** — Short interview Wigderson: [https://www.youtube.com/watch?v=5VxOhzNv9To](https://www.youtube.com/watch?v=5VxOhzNv9To).  

**Cổng chính thức / tài liệu**

- Abel 2021 Lovász & Wigderson: https://abelprize.no/abel-prize-laureates/2021  
- ACM Turing — Wigderson 2023: https://amturing.acm.org/award_winners/wigderson_3844537.cfm  

Danh mục URL đầy đủ: `research/video-research/lovasz-wigderson/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/lovasz-wigderson/transcripts/` · trạng thái: `research/video-research/lovasz-wigderson/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/lovasz-wigderson_zqiL57ebP-k_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/lovasz-wigderson/references.md`.

1. Abel 2021 Lovász & Wigderson — https://abelprize.no/abel-prize-laureates/2021  
2. Abel lectures Lovász & Wigderson — https://www.youtube.com/watch?v=zqiL57ebP-k  
3. Abel interview Lovász & Wigderson — https://www.youtube.com/watch?v=VAk0rtlKtMA  
4. WFSJ meet Lovász & Wigderson — https://www.youtube.com/watch?v=J4yssMTZqC4  
5. Short interview Lovász — https://www.youtube.com/watch?v=wg0di8dK0eI  
6. Short interview Wigderson — https://www.youtube.com/watch?v=5VxOhzNv9To  
7. NYT Abel 2021 — https://www.nytimes.com/2021/03/17/science/abel-prize-mathematics.html  
8. Nature Abel 2021 — https://www.nature.com/articles/d41586-021-00694-9  
9. ACM Turing — Wigderson 2023 — https://amturing.acm.org/award_winners/wigderson_3844537.cfm  
10. Wikipedia — Avi Wigderson — https://en.wikipedia.org/wiki/Avi_Wigderson  
11. Thư mục gói: `research/video-research/lovasz-wigderson/`.

1. [Abel 2021](https://abelprize.no/abel-prize-laureates/2021).  
2. Wigderson, *Mathematics and Computation* (Princeton).  
3. Alon–Spencer, *The Probabilistic Method*; Arora–Barak, *Computational Complexity*.  
4. Khóa: [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/); [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/).

---

## Hướng đi tiếp

- Bài tập local lemma: dựng setup sự kiện xấu toy (tô màu, packing, lịch).  
- So dựng expander lịch sử (Margulis; zigzag; Ramanujan).  
- Ghi một bài mở chính xác: P vs NP; derandomization mạnh hơn; dựng tường minh tham số tối ưu.  
- So [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp: [Sullivan]({{ site.baseurl }}/contents/vi/chapter08/08_07_Sullivan_Topology/).
