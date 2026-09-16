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

Sau bài cập nhật tùy chọn này, bạn gắn được một trích dẫn 2022–2026 vào mỗi trong bốn cuộc di cư của Chương 3—mật mã khóa công khai, đồ thị, học máy khoa học sát tối ưu hóa, và surrogate PDE mang vị Fourier—mà không viết lại các bài cơ chế bắt buộc.

## Kiến thức cần có

Chuỗi bắt buộc, đặc biệt [lý thuyết số → mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/), [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), [tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/), [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), và [phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).

## Mở đầu

Chương 3 đã kể các cuộc di cư: số học modulo thành cái bắt tay; đồ thị thành mạng; gradient thành bước huấn luyện; mode Fourier thành JPEG. Những cơ chế ấy không hết hạn. Điều đổi sau 2022 là *tiêu chuẩn và kiến trúc* ngồi trên chúng. KEM lattice thành tiêu chuẩn liên bang. Mô hình đồ thị mọc một nhánh Transformer. Bộ giải PDE mọc một nhánh toán tử học được mà vẫn nói tiếng Fourier.

## Phát triển khái niệm

Một cơ chế đóng gói khóa sinh một bí mật chung $$K$$ từ encapsulation công khai. Cổ điển, $$K$$ được bảo vệ bằng phân tích thừa số hoặc log rời rạc. Sau Shor, giả định độ khó dịch chỗ. Học đồ thị, về phần mình, vẫn cần một biểu diễn đỉnh $$v$$ trộn *láng giềng* với một hòa trộn token *toàn cục*. Fourier neural operator cài một nhân học được như một hệ số nhân $$\widehat{K}(k)$$ trên không gian tần số—cùng bức tranh đối ngẫu của bài Fourier, nay được huấn luyện chứ không thiết kế.

## Bốn cập nhật

### 1. Tiêu chuẩn hậu lượng tử trên cuộc di cư mật mã

Ngày 13 tháng 8 năm 2024, NIST công bố FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), và FIPS 205 (SLH-DSA). ML-KEM là KEM module-lattice; ML-DSA là chữ ký module-lattice; SLH-DSA là chữ ký dựa trên hàm băm không trạng thái. Câu chuyện RSA/DH của Chương 3 không sai; nó không còn là kiểm kê đầy đủ các nguyên thủy khóa công khai *được phê duyệt*. Triển khai lai (cổ điển + ML-KEM) là thỏa hiệp kỹ thuật hiện nay, không phải định lý rằng RSA đã bị phá.

### 2. Graph Transformer trên cuộc di cư mạng

Rampášek et al. (2022) đưa một công thức GPS: mã hóa vị trí hoặc cấu trúc, một lớp truyền tin cục bộ, và một lớp attention toàn cục với các biến thể tuyến tính $$O(N+E)$$ (Performer, BigBird). Phân tử, đồ thị trích dẫn, và đồ thị tri thức vẫn là đồ thị theo nghĩa Euler của chương này. Điều đổi là “GNN đối lập Transformer” nay là lựa chọn sản phẩm mô-đun chứ không phải chiến tranh tôn giáo. Max-flow và tô màu không lỗi thời; chúng thành đặc trưng và hàm mất mát bên trong mô hình lớn hơn.

### 3. Neural operator trên cuộc di cư phương trình vi phân

Kovachki et al. (2023) học ánh xạ giữa không gian hàm và báo tăng tốc lớn so với bộ giải cổ điển trên benchmark kiểu Navier–Stokes. Điều này ngồi cạnh bài ứng dụng DE, không thay well-posedness hay điều kiện CFL. Một surrogate bất biến rời rạc hóa vẫn chỉ trung thực bằng độ đo huấn luyện của nó.

### 4. Hệ số nhân Fourier như nhân học được

Fourier neural operator cài các lớp dạng

$$
\bigl(\mathcal{K}v\bigr)(x)=\mathcal{F}^{-1}\bigl(\widehat{K}\cdot \mathcal{F}v\bigr)(x),
$$

đúng là đẳng thức xử lý tín hiệu của bài Fourier với $$\widehat{K}$$ được huấn luyện. Karras, Aittala, Aila và Laine (2022) tách riêng không gian thiết kế của mô hình sinh *dựa trên score*, vốn cũng là động lực trên không gian hàm. Cả hai dòng cho cùng bài học Chương 3: một khi bạn sở hữu một biến đổi, bạn có thể học trên tọa độ đã biến đổi.

## Diễn giải và nhận định

Một số FIPS là đối tượng chính sách xây trên một giả thuyết độ khó. Một ablation GraphGPS là regularity thực nghiệm. Một hệ số nhân Fourier khớp một số Reynolds có thể hỏng ở số khác. Kỹ năng Chương 3—gọi tên cơ chế, rồi gọi tên giả định—vẫn áp dụng.

## Giới hạn và hướng mở rộng

Trang này không làm lại JPEG, simplex, hay số học RSA. Thuật toán PQC sâu hơn cũng nằm ở [mật mã tương lai]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

## Bài tập

1. Giải thích, trong hai câu, vì sao triển khai ML-KEM *cùng với* bắt tay cổ điển của TLS 1.3 khớp quy tắc “cơ chế, không khẩu hiệu” của Chương 3.
2. GraphGPS tuyên bố $$O(N+E)$$ với attention tuyến tính. Thuật toán đồ thị nào từ bài mạng vẫn là đúng công cụ nếu bạn cần *chứng chỉ* liên thông, không phải một embedding?
3. Viết lớp hệ số nhân Fourier ở trên và đánh dấu ký hiệu nào được học, ký hiệu nào là cùng DFT bạn đã gặp.
4. Một PINN và một neural operator đều “giải PDE.” Cái nào xấp xỉ một *hàm*, cái nào xấp xỉ một *ánh xạ giữa các hàm*?

## Tài liệu tham khảo

- NIST. (2024). FIPS 203, 204, 205. [Thông báo](https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips); [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203).
- Rampášek, L., et al. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Kovachki, N., et al. (2023). Neural operator: Learning maps between function spaces with applications to PDEs. *JMLR*, 24(89). [bài báo](https://jmlr.org/papers/v24/21-1524.html).
- Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. *NeurIPS*. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364).
