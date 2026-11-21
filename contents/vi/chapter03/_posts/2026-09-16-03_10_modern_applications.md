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

## Mục tiêu học tập

Sau bài cập nhật tùy chọn này, bạn có thể gắn một tài liệu giai đoạn 2022–2026 với mỗi hướng ứng dụng trong bốn hướng của Chương 3: mật mã khóa công khai, đồ thị, học máy khoa học gần với tối ưu hóa, và các mô hình thay thế (surrogate) cho PDE dựa trên Fourier. Bài không viết lại các bài bắt buộc về cơ chế.

## Kiến thức cần có

Các bài bắt buộc của chương, đặc biệt là [lý thuyết số → mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/), [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), [tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/), [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), và [phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).

## Mở đầu

Chương 3 đã kể cách toán học đi vào công nghệ: số học đồng dư trở thành giao thức bắt tay; đồ thị trở thành mạng; gradient trở thành bước huấn luyện; các mode Fourier trở thành JPEG. Những cơ chế đó không lỗi thời. Điều thay đổi sau năm 2022 là *các tiêu chuẩn và kiến trúc* được xây trên chúng. Cơ chế đóng gói khóa dựa trên lưới đã trở thành tiêu chuẩn liên bang của Mỹ. Các mô hình đồ thị có thêm một nhánh Transformer. Các bộ giải PDE có thêm một nhánh toán tử học được, nhưng vẫn dùng ngôn ngữ Fourier.

## Phát triển khái niệm

Một cơ chế đóng gói khóa (KEM) tạo ra một bí mật chung $$K$$ từ một bản đóng gói (encapsulation) được gửi công khai. Theo cách cổ điển, $$K$$ được bảo vệ bởi độ khó của bài toán phân tích thừa số hoặc logarit rời rạc. Sau thuật toán Shor, giả định về độ khó phải chuyển sang bài toán khác. Về phía học trên đồ thị, biểu diễn của một đỉnh $$v$$ vẫn cần kết hợp thông tin từ *các đỉnh lân cận* với một cơ chế trộn thông tin *toàn cục* giữa các token. Toán tử nơ-ron Fourier (Fourier neural operator) cài một nhân học được dưới dạng một hệ số nhân $$\widehat{K}(k)$$ trên miền tần số. Đó vẫn là bức tranh đối ngẫu của bài Fourier, chỉ khác là hệ số được huấn luyện thay vì được thiết kế.

## Bốn cập nhật

### 1. Tiêu chuẩn hậu lượng tử cho hướng mật mã

Ngày 13 tháng 8 năm 2024, NIST công bố FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) và FIPS 205 (SLH-DSA). ML-KEM là cơ chế đóng gói khóa dựa trên lưới module; ML-DSA là lược đồ chữ ký dựa trên lưới module; SLH-DSA là lược đồ chữ ký dựa trên hàm băm, không cần lưu trạng thái. Câu chuyện RSA/Diffie–Hellman của Chương 3 không sai; chỉ là nó không còn là danh sách đầy đủ các thành phần khóa công khai *được phê duyệt*. Triển khai lai (cổ điển + ML-KEM) là một lựa chọn kỹ thuật thận trọng hiện nay, không phải bằng chứng rằng RSA đã bị phá.

### 2. Graph Transformer cho hướng mạng

Rampášek và cộng sự (2022) đề xuất công thức GPS gồm: mã hóa vị trí hoặc cấu trúc, một lớp truyền thông tin cục bộ, và một lớp attention toàn cục với các biến thể tuyến tính độ phức tạp $$O(N+E)$$ (Performer, BigBird). Phân tử, đồ thị trích dẫn và đồ thị tri thức vẫn là đồ thị theo đúng nghĩa từ thời Euler mà chương này dùng. Điều thay đổi là "GNN hay Transformer" giờ là lựa chọn lắp ghép theo mô-đun trong sản phẩm, không còn là cuộc tranh cãi phe phái. Luồng cực đại và tô màu đồ thị không lỗi thời; chúng trở thành đặc trưng và hàm mất mát bên trong những mô hình lớn hơn.

### 3. Toán tử nơ-ron cho hướng phương trình vi phân

Kovachki và cộng sự (2023) học các ánh xạ giữa các không gian hàm và báo cáo tốc độ nhanh hơn nhiều so với bộ giải cổ điển trên các bài kiểm tra kiểu Navier–Stokes. Kết quả này đứng cạnh bài phương trình vi phân ứng dụng, không thay thế khái niệm đặt chỉnh hay điều kiện CFL. Một mô hình thay thế không phụ thuộc cách rời rạc hóa vẫn chỉ đáng tin trong phạm vi thước đo mà nó được huấn luyện.

### 4. Hệ số nhân Fourier như một nhân học được

Toán tử nơ-ron Fourier dùng các lớp có dạng

$$
\bigl(\mathcal{K}v\bigr)(x)=\mathcal{F}^{-1}\bigl(\widehat{K}\cdot \mathcal{F}v\bigr)(x),
$$

đúng là công thức lọc tín hiệu trong bài Fourier, với $$\widehat{K}$$ được huấn luyện. Karras, Aittala, Aila và Laine (2022) phân tích có hệ thống các lựa chọn thiết kế cho mô hình sinh dạng khuếch tán (dựa trên score), vốn cũng được mô tả bằng một phương trình vi phân (ngẫu nhiên hoặc tất định) trên không gian dữ liệu. Cả hai hướng cho cùng một bài học của Chương 3: khi đã nắm được một phép biến đổi, bạn có thể học trực tiếp trên các tọa độ sau biến đổi.

## Diễn giải và nhận định

Một tiêu chuẩn FIPS là một quyết định chính sách dựa trên một giả thuyết về độ khó. Một thí nghiệm loại bỏ thành phần (ablation) của GraphGPS là một quy luật thực nghiệm. Một hệ số nhân Fourier khớp tốt ở một số Reynolds có thể thất bại ở số Reynolds khác. Kỹ năng của Chương 3 vẫn dùng được: gọi tên cơ chế, rồi gọi tên giả định.

## Giới hạn và hướng mở rộng

Trang này không trình bày lại JPEG, phương pháp đơn hình hay số học RSA. Các thuật toán mật mã hậu lượng tử được bàn sâu hơn ở bài [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

## Bài tập

1. Giải thích trong hai câu vì sao việc triển khai ML-KEM *cùng với* phần bắt tay cổ điển của TLS 1.3 phù hợp với nguyên tắc "nói rõ cơ chế, không nói khẩu hiệu" của Chương 3.
2. GraphGPS đạt độ phức tạp $$O(N+E)$$ nhờ attention tuyến tính. Nếu bạn cần *chứng nhận* tính liên thông, chứ không phải một biểu diễn nhúng, thì thuật toán đồ thị nào trong bài mạng vẫn là công cụ đúng?
3. Viết lại công thức lớp hệ số nhân Fourier ở trên và đánh dấu ký hiệu nào được học, ký hiệu nào chính là DFT bạn đã gặp.
4. Một PINN và một toán tử nơ-ron đều "giải PDE". Cái nào xấp xỉ một *hàm số*, cái nào xấp xỉ một *ánh xạ giữa các hàm số*?

## Tài liệu tham khảo

- NIST. (2024). FIPS 203, 204, 205. [Thông báo](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips); [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203).
- Rampášek, L., et al. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Kovachki, N., et al. (2023). Neural operator: Learning maps between function spaces with applications to PDEs. *JMLR*, 24(89). [bài báo](https://jmlr.org/papers/v24/21-1524.html).
- Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. *NeurIPS*. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364).

## Video tham khảo

- **Xem trước**: [Post Quantum Cryptography - Computerphile](https://www.youtube.com/watch?v=_MoRcYLN-7U) (Computerphile, tiếng Anh). Giới thiệu vì sao máy tính lượng tử đe dọa mật mã hiện nay và các hướng mật mã hậu lượng tử. Nên xem trước khi đọc mục 1.
- [An Introduction to Graph Neural Networks: Models and Applications](https://www.youtube.com/watch?v=zCEYiCxrL_0) (Microsoft Research, tiếng Anh). Bài giảng giới thiệu mạng nơ-ron đồ thị và các ứng dụng. Nền tảng cho mục 2.
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) (Steve Brunton, tiếng Anh). Giải thích toán tử nơ-ron Fourier và cách nó học trên miền tần số. Xem cùng mục 3 và 4.
