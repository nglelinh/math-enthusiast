---
layout: post
title: "Ứng dụng hiện đại: Ý tưởng Fields trong khoa học máy tính"
chapter: '02'
order: 33
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
lesson_type: optional
---

Khi khép lại hành trình qua hơn 30 chân dung Huy chương Fields — từ những đa tạp 4 chiều ngoại lai, phương trình Monge–Ampère, lưới xếp cầu 8 chiều cho đến chuyển pha thống kê — một câu hỏi rất tự nhiên nảy ra: *những ý tưởng toán học đỉnh cao ấy đi đâu khi bước ra khỏi giảng đường thuần túy?* Thú vị là, khi bước vào khoa học máy tính và công nghiệp giai đoạn 2022–2026, thứ được mang theo hiếm khi là tiểu sử hay nguyên văn một định lý trừu tượng, mà là **cấu trúc đối tượng tính toán**: một mạng nơ-ron học cách xấp xỉ phương án vận chuyển tối ưu để dịch ảnh không cặp, một bài toán hình học trên lưới nhiều chiều bảo vệ mọi giao dịch Internet trước kỷ nguyên máy tính lượng tử, hay thói quen săn tìm ngưỡng chuyển pha để thiết kế bộ giải SAT và kiến trúc mạng đồ thị hiện đại.

Bài học tùy chọn này là nhịp cầu giúp bạn cầm nắm ba dòng chảy ứng dụng sống động đó — đồng thời giữ vững sự tỉnh táo ghi công: **toán học đoạt Huy chương Fields làm sáng tỏ cấu trúc và chứng minh định lý chặt chẽ; còn khoa học máy tính biến các cấu trúc ấy thành những hệ thống đủ nhanh, đủ rẻ để chạy trên dữ liệu thực.**

**Mạch bài học:** Bản đồ kiến thức nền (từ đối tượng toán thuần túy sang bài toán tính toán) → Ví dụ số cầm tay chỉ việc cho cả ba ứng dụng (mẫu Module-LWE modulo 17, phương án OT rời rạc, ngưỡng 3-SAT) → Khung giải thích chậm: 3 bước chuyển dịch từ định lý Fields sang hệ thống 2022–2026 (Neural OT, NIST FIPS 203 ML-KEM, SAT & GraphGPS) → Diễn giải ranh giới giữa định lý và xấp xỉ kỹ thuật.

---

## Mục tiêu học tập

Sau bài tùy chọn này, bạn có thể:

- Nêu và giải thích ba ứng dụng tiêu biểu trong khoa học máy tính giai đoạn 2022–2026 kế thừa trực tiếp đối tượng toán học của Chương 2: **vận chuyển tối ưu bằng mạng nơ-ron (NOT)**, **mật mã hậu lượng tử trên lưới module (ML-KEM / FIPS 203)**, và **tư duy chuyển pha trong SAT và học sâu trên đồ thị (GraphGPS)**.
- Tự tay tính một mẫu bài toán **Module-LWE** nhỏ theo modulo $$17$$ để thấy vì sao nhiễu nhỏ và hình học lưới bảo vệ khóa bí mật.
- Phân biệt rành mạch ranh giới giữa định lý toán học chặt chẽ ([Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/), Duminil-Copin, Smirnov) với các xấp xỉ mạng nơ-ron, giả thiết độ khó mật mã và kiến trúc kỹ thuật.
- Nắm rõ phạm vi bài tùy chọn này: không kể thêm tiểu sử Fields và không lặp lại bài tổng hợp sáu trụ cột của Terence Tao ở Chương 4.

**Kiến thức cần có.** Lướt qua bản đồ chủ đề trong [tổng quan]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/). Bạn **không** cần đọc từng bài về các huy chương mới dùng được trang này. Tuy nhiên, trang này không thay thế được các bài [Figalli / vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska / xếp cầu]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/), hay các bài về vật lý thống kê.

---

## Bản đồ kiến thức nền: Ba đối tượng toán thuần túy biến thành bài toán tính toán như thế nào?

### 1. Vận chuyển tối ưu (Optimal Transport) trong Học sâu
Trong giải tích thuần túy (Figalli, Brenier, Caffarelli), ta tìm phép ghép $$\pi$$ cực tiểu hóa $$\int c(x,y)\,d\pi$$ giữa hai mật độ $$\mu, \nu$$ và hỏi khi nào nghiệm là ánh xạ trơn $$T = \nabla\phi$$. Trong **học máy**, ta chỉ có hai tập mẫu dữ liệu rời rạc hàng chục nghìn chiều (ví dụ ảnh khuôn mặt và ảnh tranh vẽ, không ghép cặp sẵn), nên thay vì giải phương trình Monge–Ampère, ta dùng **mạng nơ-ron** tham số hóa trực tiếp ánh xạ hoặc phương án vận chuyển.

### 2. Hình học lưới nhiều chiều (Lattices) trong Mật mã hậu lượng tử
Trong toán thuần túy (Viazovska), ta xếp các quả cầu đặc khít nhất trong chiều 8 ($$E_8$$) và chiều 24 (lưới Leech) nhờ dạng modular. Trong **mật mã học**, ta không dùng $$E_8$$ mà dùng **lưới module** ngẫu nhiên trong chiều hàng trăm và bài toán **Module-LWE** (*Learning With Errors*): tìm vector bí mật $$s$$ từ các mẫu có trộn nhiễu

$$
(A,\; As + e \bmod q).
$$

Trực giác hình học xếp cầu cho biết biên độ nhiễu $$e$$ (bán kính quả cầu giải mã quanh mỗi điểm lưới) được phép lớn đến đâu để người có khóa bí mật giải mã đúng duy nhất, trong khi kẻ tấn công (kể cả có máy tính lượng tử) mắc kẹt trước bài toán tìm vector ngắn nhất.

### 3. Ngưỡng chuyển pha (Phase Transitions) trong SAT và Mạng đồ thị
Giống như mô hình thấm có ngưỡng sắc $$p_c$$ (Smirnov, Duminil-Copin), bài toán thỏa mãn logic ngẫu nhiên $$k$$-SAT cũng có một ngưỡng sắc nét theo tỷ lệ mệnh đề/biến $$\alpha = m/n$$, nơi độ khó tìm kiếm tăng vọt; còn các mạng nơ-ron đồ thị (GNN / Graph Transformer) phải giải bài toán cân bằng giữa truyền tin lân cận cục bộ và tương tác toàn cục trên toàn đồ thị.

---

## 1. Ví dụ cầm tay chỉ việc: tính một mẫu LWE nhỏ theo modulo 17 và xem ngưỡng 3-SAT

### Ví dụ 1: Cầm tay một mẫu mật mã lưới LWE với $$q = 17$$
Giả sử số nguyên tố modulo là $$q = 17$$, ma trận công khai $$A$$ và vector bí mật $$s$$ là:

$$
A = \begin{pmatrix} 3 & 5 \\ 7 & 2 \end{pmatrix}, \qquad s = \begin{pmatrix} 4 \\ 1 \end{pmatrix}.
$$

- **Nếu KHÔNG thêm nhiễu $$e$$:** tính $$As \bmod 17 = \begin{pmatrix} 3\cdot 4 + 5\cdot 1 \\ 7\cdot 4 + 2\cdot 1 \end{pmatrix} = \begin{pmatrix} 17 \\ 30 \end{pmatrix} \equiv \begin{pmatrix} 0 \\ 13 \end{pmatrix} \pmod{17}$$. Kẻ tấn công chỉ cần giải hệ tuyến tính $$As \equiv b \pmod{17}$$ bằng khử Gauss trong tích tắc là lộ sạch bí mật $$s$$!
- **Khi THÊM vector nhiễu nhỏ $$e = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$$:** ta công bố
  $$
  b = As + e \equiv \begin{pmatrix} 0 + 1 \\ 13 - 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 12 \end{pmatrix} \pmod{17}.
  $$
  Chỉ cần một chút nhiễu nhỏ $$\vert e_i \vert \le 1$$, khử Gauss lập tức **sụp đổ hoàn toàn** vì nhiễu bị nhân khuếch đại hỗn loạn khi khử từng hàng! Trong thực tế (chuẩn ML-KEM với chiều $$n = 512, 768, 1024$$), việc tìm lại $$s$$ từ $$(A, b)$$ tương đương với bài toán tìm điểm lưới gần nhất trong không gian hàng trăm chiều — bài toán mà ngay cả máy tính lượng tử hiện nay cũng không biết thuật toán đa thức nào để phá!

### Ví dụ 2: Ngưỡng chuyển pha trong bài toán $$3$$-SAT ngẫu nhiên
Cho $$n = 1000$$ biến Boolean và $$m$$ mệnh đề ngẫu nhiên dạng $$(x_i \lor \neg x_j \lor x_k)$$. Đặt tỷ lệ mật độ $$\alpha = m/n$$:
- Khi $$\alpha = 2.0$$ ($$2000$$ mệnh đề): hầu như chắc chắn **có nghiệm**, bộ giải tìm ra trong vài mili-giây.
- Khi $$\alpha = 6.0$$ ($$6000$$ mệnh đề): quá nhiều ràng buộc mâu thuẫn, hầu như chắc chắn **vô nghiệm**.
- Ngay sát **ngưỡng chuyển pha $$\alpha_c \approx 4.26$$** ($$4260$$ mệnh đề): xác suất có nghiệm rơi thẳng đứng từ $$1$$ xuống $$0$$ như một bậc thang, và không gian nghiệm vỡ vụn thành nhiều cụm tách biệt — tạo ra những bài toán khó nhất cho mọi bộ giải SAT hiện đại!

---

## 2. Khung giải thích: Ba ứng dụng khoa học máy tính 2022–2026 kế thừa ý tưởng Fields ra sao? (nên đọc chậm)

Hãy nhìn kỹ 3 công trình tiêu biểu giai đoạn 2022–2026 để thấy rõ cầu nối và ranh giới ghi công:

#### Bước 1: Vận chuyển tối ưu bằng mạng nơ-ron (Korotin–Selikhanovych–Burnaev, ICLR 2023)
**Korotin, Selikhanovych và Burnaev (2023)** xây dựng khung **Neural Optimal Transport (NOT)**: huấn luyện mạng nơ-ron theo bài toán đối ngẫu minimax Kantorovich để biểu diễn trực tiếp các phương án vận chuyển tối ưu (theo cả nghĩa mạnh và nghĩa yếu), kèm định lý xấp xỉ phổ quát và ứng dụng dịch ảnh không cặp.
- *Ghi công đúng:* Đối tượng vẫn là phương án Kantorovich mà bài [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/) phân tích chính quy bằng PDE; bài báo ICLR 2023 không chứng minh định lý chính quy mới nào cho Monge–Ampère, mà chứng tỏ mạng nơ-ron khả vi xấp xỉ hiệu quả phương án vận chuyển ở quy mô ảnh thực tế.

#### Bước 2: Mật mã hậu lượng tử trên lưới module (NIST FIPS 203 — ML-KEM, tháng 8/2024)
Tháng 8 năm 2024, **NIST** ban hành tiêu chuẩn **FIPS 203** chuẩn hóa **ML-KEM** (phát triển từ CRYSTALS-Kyber) với ba bộ tham số **ML-KEM-512 / 768 / 1024** để thay thế RSA và ECC trước nguy cơ máy tính lượng tử.
- *Ghi công đúng:* Độ an toàn của ML-KEM dựa vào độ khó của **Module-LWE**, hoàn toàn không cần dùng lời giải xếp cầu chiều 8 hay 24 của [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/). Điểm giao nhau là ngôn ngữ hình học chung: lưới nhiều chiều, bài toán vector ngắn nhất và bán kính giải mã kiểu xếp cầu.

#### Bước 3: Tư duy chuyển pha trong SAT và GraphGPS (Rampášek et al., NeurIPS 2022)
Các cuộc thi SAT hiện nay vẫn dùng các bộ đề nằm sát ngưỡng chuyển pha làm thước đo phân loại sức mạnh thuật toán. Ở mảng học sâu trên đồ thị, **GraphGPS** (**Rampášek, Galkin, Dwivedi, Luu, Wolf và Beaini, 2022**) kết hợp truyền tin cục bộ (MPNN) với cơ chế chú ý (*attention*) toàn cục tuyến tính $$O(N+E)$$, giải quyết hiện tượng nghẽn thông tin tầm xa.
- *Ghi công đúng:* Đây không phải chứng minh chuyển pha liên tục kiểu Duminil-Copin hay Smirnov, mà là một **thói quen tư duy vật lý thống kê**: luôn cân bằng giữa lân cận cục bộ với chế độ toàn cục và khảo sát ngưỡng tới hạn trước khi tin vào một thuật toán hay GNN.

Tóm tắt cầu nối từ Chương 2 sang công nghệ 2022–2026:

$$
\text{Định lý Fields (OT / Lưới / Chuyển pha)}
\;\xrightarrow{\text{Chuyển hóa cấu trúc}}\;
\text{Hệ thống 2022–2026 (Neural OT / ML-KEM / SAT \& GraphGPS)}.
$$

---

## 3. Diễn giải ranh giới và phạm vi

Một mạng vận chuyển "chạy mượt" trên tập ảnh CelebA **không** phải là một định lý về tính chính quy của phương trình Monge–Ampère. Một cơ chế đóng gói khóa vượt qua tiêu chuẩn NIST **không** phải là một định lý xếp cầu tối ưu. Một GNN đạt điểm cao trên tập ZINC **không** chứng minh tính sắc hay bất biến bảo giác của chuyển pha. Các kết quả Huy chương Fields là những phát biểu toán học chặt chẽ; các hệ thống tin học là những xấp xỉ kỹ thuật đã được tinh chỉnh để vận hành thực tế.

Bài tùy chọn này cố ý không bàn về Hong Wang (bài toán Kakeya), Yu Deng (phương trình Boltzmann), cảm biến nén (Candès–Tao) hay các Huy chương Fields năm 2026 vì các nội dung đó thuộc các trang khác của khóa học.

---

## Tài liệu tham khảo

- Korotin, A., Selikhanovych, D., & Burnaev, E. (2023). Neural optimal transport. *ICLR*. [arXiv:2201.12220](https://arxiv.org/abs/2201.12220).
- NIST. (2024). *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*. [doi:10.6028/NIST.FIPS.203](https://doi.org/10.6028/NIST.FIPS.203).
- Rampášek, L., Galkin, M., Dwivedi, V. P., Luu, A. T., Wolf, G., & Beaini, D. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Chân dung khóa học (không lặp ở đây): [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/).

## Video tham khảo

- **Xem trước**: [Alessio Figalli (2018 Fields Medal) explains Optimal Transport](https://www.youtube.com/watch?v=jyL6ZECM7oM) (Tom Rocks Maths, tiếng Anh). Figalli tự giải thích bài toán vận chuyển tối ưu bằng ngôn ngữ dễ hiểu. Nên xem trước khi đọc mục 1.
- [Post Quantum Cryptography - Computerphile](https://www.youtube.com/watch?v=_MoRcYLN-7U) (Computerphile, tiếng Anh). Giới thiệu mật mã hậu lượng tử và vì sao cần thay thế các hệ mật mã hiện nay. Xem cùng mục 2.
- [Fields Medal: Hugo Duminil-Copin](https://www.youtube.com/watch?v=5dXulZVstbY) (Simons Foundation, tiếng Anh). Phim ngắn về Duminil-Copin và các mô hình chuyển pha như mô hình thấm. Xem cùng mục 3 để hiểu nguồn gốc trực giác về ngưỡng.
