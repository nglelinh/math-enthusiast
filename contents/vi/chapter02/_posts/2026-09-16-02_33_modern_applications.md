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

Khi khép lại hành trình qua hàng chục chân dung Huy chương Fields — từ những đa tạp 4 chiều kỳ lạ đến phương trình Monge–Ampère, lưới xếp cầu 8 chiều hay chuyển pha thống kê — một câu hỏi rất tự nhiên nảy ra: *những ý tưởng trừu tượng đỉnh cao này đi đâu khi bước ra khỏi giảng đường toán thuần túy?* Thú vị là, khi đi vào công nghiệp và khoa học máy tính giai đoạn 2022–2026, thứ được mang theo hiếm khi là tiểu sử hay một định lý nguyên khối, mà là **cấu trúc đối tượng toán học**: một mạng nơ-ron học cách xấp xỉ phương án vận chuyển tối ưu để dịch ảnh không cần dữ liệu ghép cặp, một bài toán hình học trên lưới nhiều chiều bảo vệ mọi kết nối Internet trước kỷ nguyên máy tính lượng tử, hay trực giác về ngưỡng chuyển pha giúp thiết kế bộ giải SAT và kiến trúc mạng đồ thị hiện đại.

Bài học tùy chọn này là cầu nối giúp bạn nhìn thấy ba dòng chảy sống động đó — đồng thời giữ vững sự tỉnh táo khoa học: **toán học đoạt Huy chương Fields làm sáng tỏ cấu trúc và chứng minh định lý chặt chẽ; còn khoa học máy tính và kỹ thuật hệ thống biến các cấu trúc ấy thành thuật toán đủ nhanh, đủ rẻ để chạy trên dữ liệu thật.**

---

## Mục tiêu học tập

Sau bài tùy chọn này, bạn có thể:

- Nêu và giải thích ba ứng dụng tiêu biểu trong khoa học máy tính giai đoạn 2022–2026 kế thừa trực tiếp ngôn ngữ toán học của Chương 2: **vận chuyển tối ưu bằng mạng nơ-ron**, **mật mã hậu lượng tử dựa trên lưới module**, và **tư duy ngưỡng chuyển pha trong bài toán SAT và học sâu trên đồ thị**.
- Phân biệt rành mạch ranh giới ghi công: đâu là định lý toán học chặt chẽ của các công trình Huy chương Fields ([Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/), Duminil-Copin, Smirnov), và đâu là xấp xỉ tính toán, giả thiết độ khó hay kiến trúc kỹ thuật của khoa học máy tính hiện đại.
- Hiểu bài này là phần mở rộng định hướng ứng dụng, không kể thêm tiểu sử Fields và không lặp lại bài tổng hợp sáu trụ cột của Terence Tao ở Chương 4.

**Kiến thức cần có.** Lướt qua bản đồ chủ đề trong [tổng quan]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/). Bạn **không** cần đọc hết từng bài chân dung mới đọc được trang này; ngược lại, trang này cũng không thay thế các bài chuyên sâu như [Figalli / vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska / xếp cầu]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/), hay các bài về vật lý thống kê.

---

## Bản đồ kiến thức nền: Từ đối tượng toán thuần túy đến bài toán tính toán

Trước khi đi vào từng ứng dụng giai đoạn 2022–2026, hãy nhìn cách ba khái niệm toán học thuần túy của Chương 2 được "dịch" sang ngôn ngữ của kỹ sư AI và mật mã học:

1. **Vận chuyển tối ưu (Optimal Transport):**
   - *Trong giải tích thuần túy (Figalli, Brenier, Caffarelli):* cho hai phân bố xác suất $$\mu, \nu$$, tìm phép ghép $$\pi$$ cực tiểu hóa $$\int c(x,y)\,d\pi(x,y)$$ và chứng minh khi nào nghiệm là ánh xạ trơn $$T = \nabla\phi$$.
   - *Trong học máy (AI):* ta chỉ có tập mẫu rời rạc (ví dụ 100.000 ảnh mặt người và 100.000 ảnh tranh vẽ anime, không hề ghép cặp!). Thay vì giải phương trình Monge–Ampère trên không gian hàng chục nghìn chiều, ta dùng **mạng nơ-ron** $$T_\theta$$ để tham số hóa trực tiếp ánh xạ hoặc phương án vận chuyển giữa hai phân bố dữ liệu!

2. **Hình học lưới nhiều chiều (High-dimensional Lattices):**
   - *Trong toán thuần túy (Viazovska):* tìm cách xếp các quả cầu đặc khít nhất trong chiều 8 (lưới $$E_8$$) và chiều 24 (lưới Leech) nhờ dạng modular.
   - *Trong mật mã hậu lượng tử:* không dùng $$E_8$$ hay lưới Leech, mà dùng các **lưới module** ngẫu nhiên trong chiều hàng trăm (như $$n = 512, 768, 1024$$) và bài toán **Module-LWE** (*Learning With Errors*): tìm vector bí mật $$s$$ khi chỉ quan sát được các mẫu đã bị trộn nhiễu

$$
(A,\, As+e \bmod q).
$$

   Chính trực giác **hình học xếp cầu** cho biết biên độ nhiễu $$e$$ được phép lớn đến đâu (bán kính giải mã quanh mỗi điểm lưới) để người nhận có khóa bí mật vẫn giải mã đúng duy nhất, trong khi kẻ tấn công (kể cả sở hữu máy tính lượng tử) phải đối mặt với bài toán tìm vector ngắn nhất cực kỳ khó!

3. **Ngưỡng chuyển pha (Phase Transitions):**
   - *Trong vật lý thống kê (Smirnov, Duminil-Copin):* khi mật độ cạnh mở $$p$$ vượt qua ngưỡng sắc $$p_c$$, mạng lưới đột ngột chuyển từ rời rạc sang liên thông toàn cục.
   - *Trong khoa học máy tính:* một hệ ràng buộc logic ngẫu nhiên (như $$3$$-SAT với tỷ lệ mệnh đề/biến $$\alpha = m/n$$) cũng có một **ngưỡng chuyển pha sắc nét** quanh $$\alpha_c \approx 4.26$$: dưới ngưỡng gần như chắc chắn có nghiệm và dễ tìm; trên ngưỡng gần như chắc chắn vô nghiệm; còn **ngay tại ngưỡng** là nơi mọi thuật toán tìm kiếm gặp độ khó cực đại!

---

## Ba ứng dụng bổ sung (2022–2026)

### 1. Vận chuyển tối ưu bằng mạng nơ-ron (Neural Optimal Transport)

Trong học sâu sinh ảnh, bài toán **dịch ảnh không cặp** (*unpaired image-to-image translation* — ví dụ biến ảnh chụp ban ngày thành ban đêm, hay ảnh khuôn mặt thành tranh sơn dầu mà không cần cặp ảnh khớp nhau sẵn) về bản chất chính là bài toán vận chuyển tối ưu giữa hai phân bố ảnh $$\mu$$ và $$\nu$$.

Công trình của **Korotin, Selikhanovych và Burnaev (ICLR 2023)** đề xuất khung **Neural Optimal Transport (NOT)**: họ huấn luyện mạng nơ-ron theo bài toán minimax đối ngẫu Kantorovich để biểu diễn trực tiếp các phương án vận chuyển tối ưu (theo cả nghĩa mạnh lẫn nghĩa yếu, cho phép một đầu vào sinh ra nhiều đầu ra đa dạng), đồng thời chứng minh định lý xấp xỉ phổ quát cho phương án vận chuyển.

**Ranh giới cần giữ rõ:** Đối tượng toán học vẫn là bài toán đối ngẫu Kantorovich trong bài [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), nhưng bài báo ICLR 2023 không chứng minh kết quả chính quy mới nào cho phương trình Monge–Ampère trên $$\mathbb{R}^n$$. Giá trị của nó nằm ở khía cạnh tính toán: chứng tỏ một mô hình mạng nơ-ron khả vi có thể xấp xỉ hiệu quả phương án vận chuyển ở quy mô ảnh thực tế độ phân giải cao.

### 2. Lưới module trong mật mã hậu lượng tử (NIST FIPS 203 — ML-KEM)

Thuật toán Shor trên máy tính lượng tử đủ lớn có thể phá vỡ hệ mật mã khóa công khai RSA và đường cong elliptic (ECC) hiện đang bảo vệ hầu hết giao dịch Internet. Tháng 8 năm 2024, Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST) chính thức ban hành tiêu chuẩn **FIPS 203** chuẩn hóa **ML-KEM** (*Module-Lattice-Based Key-Encapsulation Mechanism*, phát triển từ thuật toán CRYSTALS-Kyber) với ba mức bảo mật **ML-KEM-512 / 768 / 1024**.

**Ranh giới cần giữ rõ:** Độ an toàn của ML-KEM dựa trên giả thiết độ khó tính toán của bài toán **Module-LWE** trên lưới chiều cao, **không** sử dụng định lý xếp cầu chiều 8 hay chiều 24 của [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/) (vốn dùng các lưới cực kỳ đối xứng và dạng modular). Cầu nối với Chương 2 là **ngôn ngữ hình học chung**: lưới nhiều chiều, độ khó của bài toán tìm vector ngắn nhất (SVP), và hình học bán kính giải mã kiểu xếp cầu để cân bằng giữa tỷ lệ lỗi giải mã và độ an toàn lượng tử.

### 3. Tư duy chuyển pha trong bài toán SAT và học sâu trên đồ thị (GraphGPS)

Trong lý thuyết độ phức tạp và trí tuệ nhân tạo, tư duy về **ngưỡng tới hạn sắc nét** từ vật lý thống kê đã trở thành một nguyên lý thiết kế thực chiến:
- **Trong các cuộc thi giải SAT (SAT Competition):** Những bộ đề kiểm thử khó nhất để phân loại sức mạnh của các bộ giải SAT hiện đại (CDCL, tìm kiếm cục bộ) thường được tạo ra đúng tại **vùng chuyển pha** — nơi cấu trúc không gian nghiệm vỡ vụn thành các cụm rời rạc (hiện tượng tương tự thủy tinh spin trong vật lý thống kê!).
- **Trong học sâu trên đồ thị (Graph Neural Networks):** Các mạng truyền tin cục bộ (MPNN) truyền thông tin giữa các nút kề nhau (giống tương tác láng giềng gần nhất trong mô hình Ising/thấm), nhưng thường bị nghẽn cổ chai (*over-squashing*) khi cần truyền thông tin đường dài qua toàn đồ thị. Kiến trúc **GraphGPS** của **Rampášek, Galkin, Dwivedi, Luu, Wolf và Beaini (NeurIPS 2022)** kết hợp truyền tin cục bộ với cơ chế chú ý (*attention*) toàn cục có độ phức tạp tuyến tính $$O(N+E)$$.

**Ranh giới cần giữ rõ:** Đây không phải là chứng minh định lý chuyển pha của Duminil-Copin hay Smirnov trên mô hình liên tục; đó là một **thói quen tư duy khoa học** kế thừa từ vật lý thống kê — luôn khảo sát cân bằng giữa tương tác cục bộ và chế độ toàn cục, cũng như xác định ngưỡng tới hạn trước khi tin tưởng vào hiệu năng của một bộ giải hay một kiến trúc mạng đồ thị.

---

## Diễn giải và nhận định

Giữ ranh giới rõ ràng giữa toán học thuần túy và kỹ thuật tính toán giúp ta trân trọng đúng giá trị của cả hai thế giới:
- Một mạng vận chuyển tối ưu dịch ảnh đẹp mắt trên tập dữ liệu CelebA **không** phải là một định lý về tính chính quy $$W^{2,1}$$ của phương trình Monge–Ampère.
- Một cơ chế đóng gói khóa vượt qua 8 năm thẩm định khắt khe của NIST **không** phải là một định lý xếp cầu tối ưu.
- Một kiến trúc Graph Transformer đạt điểm cao nhất trên tập phân tử ZINC **không** chứng minh tính sắc hay bất biến bảo giác của chuyển pha.

Các công trình Huy chương Fields cung cấp **nền tảng chân lý và ngôn ngữ cấu trúc**; các hệ thống khoa học máy tính 2022–2026 cung cấp **những xấp xỉ tinh tế có thể vận hành ở quy mô toàn cầu**.

---

## Giới hạn và hướng mở rộng

Bài tùy chọn này chủ ý không lặp lại câu chuyện về Hong Wang và bài toán Kakeya, Yu Deng và phương trình Boltzmann, hay cảm biến nén (*compressed sensing*) của Candès–Tao (đã được trình bày chi tiết ở các bài và chương khác), và cũng không mở rộng sang khảo sát các Huy chương Fields năm 2026.

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
