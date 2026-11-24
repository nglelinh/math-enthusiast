---
layout: post
title: "Ứng dụng hiện đại: Cập nhật 2022–2026"
chapter: '03'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
lesson_type: optional
---

Những ý tưởng nền tảng của Chương 3 — số học đồng dư trong RSA, đồ thị trong tìm kiếm, gradient trong tối ưu hóa, và biến đổi Fourier trong xử lý tín hiệu — đều đã có tuổi đời từ vài thập kỷ đến hàng thế kỷ. Vậy liệu chúng đã "đóng khung" thành lịch sử chưa? Hoàn toàn ngược lại! Chỉ trong giai đoạn **2022–2026**, chính trên bốn nền móng cổ điển ấy đã mọc lên bốn bước ngoặt công nghệ định hình lại hạ tầng Internet, AI khoa học và mô phỏng vật lý: mật mã dựa trên lưới trở thành chuẩn liên bang chính thức của Mỹ, Transformer kết hợp với đồ thị, mạng nơ-ron học trực tiếp toán tử giải PDE trong miền Fourier, và các mô hình tạo ảnh khuếch tán giải ngược phương trình vi phân ngẫu nhiên.

Bài cập nhật tùy chọn này không lặp lại các cơ chế nền tảng đã học ở các bài chính; nó nối thẳng từng bài toán cổ điển của Chương 3 với **các chuẩn công nghiệp và công trình cột mốc giai đoạn 2022–2026**.

---

## Mục tiêu học tập

Sau bài cập nhật tùy chọn này, bạn có thể gắn một công trình hoặc tiêu chuẩn giai đoạn 2022–2026 với mỗi hướng ứng dụng trong bốn hướng của Chương 3: mật mã khóa công khai, đồ thị, học máy khoa học gần với tối ưu hóa, và các mô hình thay thế (surrogate) cho PDE dựa trên Fourier — đồng thời giải thích chính xác *cái gì mới* và *cái gì vẫn giữ nguyên từ toán học cổ điển*.

## Kiến thức cần có

Các bài bắt buộc của chương, đặc biệt là [lý thuyết số → mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/), [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), [tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/), [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), và [phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).

---

## Bản đồ kiến thức nền: Bốn mũi nhọn 2022–2026 mở rộng toán học cổ điển như thế nào?

Điểm thú vị nhất của làn sóng công nghệ 2022–2026 là nó **không vứt bỏ** toán học Chương 3, mà nâng cấp *hệ tọa độ* hoặc *bài toán nền* thêm một tầng:

| Hướng cổ điển (Chương 3) | Giới hạn khi mở rộng sang 2022–2026 | Bước nhảy mới (2022–2026) |
|---|---|---|
| **Mật mã số học** (RSA, ECC) | Bị thuật toán lượng tử Shor đe dọa trong tương lai. | **Chuẩn NIST FIPS 203/204/205:** chuyển sang bài toán hình học lưới (Module-LWE) và hàm băm. |
| **Đồ thị & GNN truyền thống** | Chỉ truyền tin từng bước sang hàng xóm gần → khó nắm bắt quan hệ tầm xa (over-squashing). | **Graph Transformer (GraphGPS):** ghép truyền tin cục bộ với attention toàn cục tuyến tính $$O(N+E)$$. |
| **Bộ giải số PDE cổ điển** (FEM, CFD) | Chậm khi phải chạy lại hàng nghìn lần để tối ưu thiết kế hoặc dự báo thời tiết. | **Toán tử nơ-ron (FNO):** học ánh xạ trực tiếp giữa các *không gian hàm*, chạy nhanh gấp hàng trăm đến hàng nghìn lần lúc suy luận. |
| **Biến đổi Fourier & SDE** | Bộ lọc cổ điển do kỹ sư tự tay thiết kế; sinh ảnh từ nhiễu cần quỹ đạo ổn định. | **Học trực tiếp trong miền tần số** ($$\widehat{K}$$ học được) & **Mô hình khuếch tán (Diffusion)** giải ODE/SDE ngược. |

---

## Phát triển khái niệm

Một **cơ chế đóng gói khóa (KEM)** tạo ra một khóa bí mật chung $$K$$ kèm một bản đóng gói công khai gửi qua mạng. Trước đây $$K$$ được bảo vệ bởi bài toán phân tích thừa số hoặc logarit rời rạc; nay nó được bảo vệ bởi bài toán tìm vectơ bí mật ẩn trong nhiễu trên lưới nhiều chiều.

Về phía học trên đồ thị, biểu diễn của một đỉnh $$v$$ cần kết hợp cả **cấu trúc cục bộ** (hàng xóm nối trực tiếp với $$v$$) lẫn **tương tác toàn cục** (hai nguyên tử ở hai đầu một phân tử lớn vẫn tương tác hóa học với nhau).

Còn **Toán tử nơ-ron Fourier (FNO)** giữ nguyên định lý tích chập kinh điển — biến đổi tín hiệu sang miền tần số bằng FFT, nhân với một bộ lọc $$\widehat{K}(k)$$, rồi biến đổi ngược lại — điểm khác biệt duy nhất nhưng cực kỳ lợi hại là thay vì kỹ sư tự viết tay công thức lọc $$\widehat{K}(k)$$, mạng nơ-ron **tự học các hệ số $$\widehat{K}(k)$$ từ dữ liệu mô phỏng PDE**!

---

## Bốn cập nhật

### 1. Tiêu chuẩn hậu lượng tử cho hướng mật mã

Ngày 13 tháng 8 năm 2024, Viện Tiêu chuẩn và Công nghệ Quốc gia Mỹ (NIST) chính thức công bố ba chuẩn mật mã hậu lượng tử đầu tiên: **FIPS 203 (ML-KEM)**, **FIPS 204 (ML-DSA)** và **FIPS 205 (SLH-DSA)**.
- **ML-KEM** (xuất phát từ CRYSTALS-Kyber) là cơ chế đóng gói khóa dựa trên bài toán **Module-LWE** trên lưới đại số: khóa công khai cỡ ~1,2 KB (lớn hơn ECC 256-bit nhưng vẫn vừa gọn trong một gói tin mạng) và tốc độ chạy cực nhanh ngay trên CPU thường.
- **ML-DSA** (Dilithium) là lược đồ chữ ký số dựa trên lưới module.
- **SLH-DSA** (SPHINCS+) là lược đồ chữ ký dựa thuần trên hàm băm không cần lưu trạng thái — đóng vai trò phương án dự phòng an toàn tuyệt đối ngay cả khi toán học về lưới có bất ngờ.

Câu chuyện RSA và Diffie–Hellman của Chương 3 không hề sai; chỉ là từ năm 2024 trở đi chúng không còn là danh sách đầy đủ các thành phần khóa công khai *được phê duyệt*. Các trình duyệt lớn (Chrome, Cloudflare, Apple iMessage) hiện triển khai **chế độ lai (hybrid: X25519 + ML-KEM)** — nghĩa là kẻ tấn công phải phá được *cả hai* hệ mật cùng lúc mới đọc trộm được dữ liệu.

### 2. Graph Transformer cho hướng mạng

Mạng nơ-ron đồ thị (GNN) truyền thống truyền tin theo từng bước cạnh, nên thông tin từ hai nút xa nhau dễ bị "nén bẹp" qua các nút cổ chai (over-squashing). Trong khi đó, áp dụng thẳng Transformer chuẩn lên đồ thị $$N$$ nút sẽ tốn bộ nhớ $$O(N^2)$$ — không chạy nổi với mạng hàng triệu nút.

Rampášek và cộng sự (2022) đề xuất khung kiến trúc **GraphGPS** dung hòa cả hai thế giới bằng ba thành phần mô-đun: (1) **mã hóa vị trí/cấu trúc** (như vectơ riêng của ma trận Laplace đồ thị hay xác suất bước ngẫu nhiên), (2) một lớp **truyền thông tin cục bộ (MPNN)** dọc theo các cạnh, và (3) một lớp **attention toàn cục tuyến tính** (Performer, BigBird) kéo độ phức tạp xuống còn $$O(N+E)$$. Phân tử thuốc, đồ thị trích dẫn và đồ thị tri thức vẫn là đồ thị theo đúng nghĩa Euler từ thế kỷ XVIII; điều đổi mới là "GNN hay Transformer" đã trở thành các khối lắp ghép bổ trợ nhau, còn các khái niệm cổ điển như phổ Laplace hay luồng cực đại trở thành đặc trưng đầu vào đắt giá cho mô hình lớn.

### 3. Toán tử nơ-ron cho hướng phương trình vi phân

Hãy phân biệt hai cách dùng AI để giải PDE:
- **PINN (Physics-Informed Neural Network):** học một *hàm số* nghiệm $$u(x,t)$$ cho **một** điều kiện ban đầu cụ thể — hễ đổi hình dạng cánh máy bay hay đổi điều kiện đầu là phải huấn luyện lại từ đầu.
- **Toán tử nơ-ron (Neural Operator — Kovachki và cộng sự, 2023):** học cả một **ánh xạ giữa hai không gian hàm** $$\mathcal{G}: a(\cdot) \mapsto u(\cdot)$$ (đưa vào bất kỳ điều kiện đầu hay hệ số độ nhớt nào là trả ra ngay cả trường nghiệm!).

Trên các bài toán chuẩn kiểu Navier–Stokes hay dự báo thời tiết toàn cầu (như họ mô hình FourCastNet), sau khi huấn luyện xong, toán tử nơ-ron chạy nhanh hơn bộ giải PDE cổ điển hàng trăm đến hàng nghìn lần và có tính **bất biến theo độ phân giải lưới** (huấn luyện trên lưới thô vẫn dự đoán được trên lưới mịn). Tuy nhiên, nó đứng *bên cạnh* chứ không thay thế lý thuyết đặt chỉnh Hadamard hay điều kiện CFL: một mô hình thay thế chỉ đáng tin trong miền phân phối mà nó đã từng thấy khi huấn luyện.

### 4. Hệ số nhân Fourier như một nhân học được (và Mô hình khuếch tán)

Toán tử nơ-ron Fourier (FNO) cài đặt từng lớp mạng bằng đúng công thức lọc tín hiệu của bài Fourier:

$$
\bigl(\mathcal{K}v\bigr)(x)=\mathcal{F}^{-1}\bigl(\widehat{K}\cdot \mathcal{F}v\bigr)(x),
$$

trong đó $$\mathcal{F}$$ là FFT, $$\mathcal{F}^{-1}$$ là IFFT, còn $$\widehat{K}$$ là ma trận trọng số cắt gọn ở các tần số thấp được tối ưu bằng gradient descent.

Cùng lúc đó, trong lĩnh vực AI tạo sinh (hình ảnh, video), **Karras, Aittala, Aila và Laine (2022)** thống nhất không gian thiết kế của các **mô hình khuếch tán (diffusion models)**: quá trình làm mờ ảnh thành nhiễu trắng Gauss là một phương trình vi phân ngẫu nhiên (SDE) chạy xuôi, còn việc vẽ ra một bức ảnh sắc nét từ nhiễu thuần túy chính là **giải ngược một phương trình vi phân** (ODE dòng xác suất hoặc SDE ngược) bằng các bộ giải số kiểu Runge–Kutta/Heun quen thuộc từ bài [Phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/)! Cả hai đột phá cùng lặp lại một bài học sâu sắc của Chương 3: *khi đã làm chủ phép biến đổi và phương trình nền, bạn có thể gắn học máy trực tiếp lên chính các tọa độ toán học đó.*

---

## Diễn giải và nhận định

Một tiêu chuẩn FIPS là một quyết định kỹ thuật – thể chế dựa trên một giả định về độ khó tính toán. Một thí nghiệm loại bỏ thành phần (ablation) của GraphGPS là một quy luật thực nghiệm. Một toán tử nơ-ron Fourier khớp tuyệt đẹp ở số Reynolds $$1{.}000$$ vẫn có thể trật nhịp khi sang dòng chảy rối ở số Reynolds $$100{.}000$$. Bản lĩnh toán học mà Chương 3 rèn luyện cho bạn vẫn nguyên giá trị: **luôn gọi đúng tên cơ chế, và luôn soi rõ giả định đứng sau nó.**

## Giới hạn và hướng mở rộng

Trang này không trình bày lại JPEG, phương pháp đơn hình hay số học RSA. Các thuật toán mật mã hậu lượng tử được bàn sâu hơn ở bài [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

## Tài liệu tham khảo

- NIST. (2024). FIPS 203, 204, 205. [Thông báo](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips); [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203).
- Rampášek, L., et al. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Kovachki, N., et al. (2023). Neural operator: Learning maps between function spaces with applications to PDEs. *JMLR*, 24(89). [bài báo](https://jmlr.org/papers/v24/21-1524.html).
- Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. *NeurIPS*. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364).

## Video tham khảo

- **Xem trước**: [Post Quantum Cryptography - Computerphile](https://www.youtube.com/watch?v=_MoRcYLN-7U) (Computerphile, tiếng Anh). Giới thiệu vì sao máy tính lượng tử đe dọa mật mã hiện nay và các hướng mật mã hậu lượng tử. Nên xem trước khi đọc mục 1.
- [An Introduction to Graph Neural Networks: Models and Applications](https://www.youtube.com/watch?v=zCEYiCxrL_0) (Microsoft Research, tiếng Anh). Bài giảng giới thiệu mạng nơ-ron đồ thị và các ứng dụng. Nền tảng cho mục 2.
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) (Steve Brunton, tiếng Anh). Giải thích toán tử nơ-ron Fourier và cách nó học trên miền tần số. Xem cùng mục 3 và 4.
