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

## Mục tiêu học tập

Sau bài tùy chọn này, bạn có thể nêu được ba ứng dụng trong khoa học máy tính giai đoạn 2022–2026 có dùng lại các đối tượng toán học đã gặp trong chương: vận chuyển tối ưu, lưới (lattice) nhiều chiều, và cách tư duy về chuyển pha. Bài không kể thêm tiểu sử người đoạt Fields, và cũng không lặp lại bài tổng hợp sáu trụ cột của Tao ở Chương 4.

## Kiến thức cần có

Lướt qua bản đồ chủ đề trong [tổng quan]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/). Bạn **không** cần đọc từng bài về các huy chương mới dùng được trang này. Tuy nhiên, trang này không thay thế được các bài [Figalli / vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska / xếp cầu]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/), hay các bài về vật lý thống kê.

## Mở đầu

Các bài về Huy chương Fields trong chương này kể về con người và định lý. Khi sang công nghiệp, cái được mang theo hiếm khi là câu chuyện về một người. Thứ được mang theo là một đối tượng tính toán: một mạng nơ-ron xấp xỉ một phương án vận chuyển, một bài toán trên lưới được tin là khó ngay cả với máy tính lượng tử, hay một bộ giải SAT chạy nhanh hoặc chậm tùy vào vị trí so với ngưỡng chuyển pha. Điều cần cẩn thận là ghi công cho đúng. Công trình đoạt huy chương làm cho các đối tượng này trở nên rõ ràng, chính xác. Các hệ thống tin học làm cho chúng *đủ rẻ để chạy được*.

## Phát triển khái niệm

Bài toán vận chuyển tối ưu (với chi phí bậc hai) tìm một phép ghép (coupling) $$\pi$$ giữa hai độ đo $$\mu,\nu$$ sao cho $$\int c(x,y)\,d\pi$$ nhỏ nhất. Lý thuyết chính quy hỏi khi nào nghiệm tối ưu là một ánh xạ. Học máy thì thường hỏi khi nào một mạng nơ-ron *tham số hóa* được một ánh xạ hoặc một phương án vận chuyển đủ tốt để dùng cho bài toán dịch ảnh không cặp.

Một bài toán khác hẳn là bài toán trên lưới module, chẳng hạn Module-LWE: tìm bí mật $$s$$ khi biết các mẫu có nhiễu

$$
(A,\, As+e \bmod q),
$$

và hình học kiểu xếp cầu cho biết sai số $$e$$ được phép lớn đến đâu trước khi việc giải mã không còn duy nhất. Không đoạn nào ở trên là tiểu sử.

## Ba ứng dụng bổ sung

### 1. Vận chuyển tối ưu bằng mạng nơ-ron

Korotin, Selikhanovych và Burnaev (2023) huấn luyện mạng nơ-ron để biểu diễn các phương án vận chuyển tối ưu (OT) theo nghĩa mạnh và nghĩa yếu, đồng thời chứng minh một kết quả xấp xỉ phổ quát cho phương án vận chuyển. Các thí nghiệm gồm bài toán dịch ảnh không cặp. Đối tượng ở đây vẫn là phương án Kantorovich mà bài Figalli nghiên cứu bằng giải tích. Bài báo không chứng minh kết quả chính quy mới nào cho ánh xạ trên $$\mathbb{R}^n$$. Nó chỉ cho thấy một mô hình khả vi có thể thay thế một phương án vận chuyển ở quy mô dữ liệu ảnh. Nếu muốn tìm hiểu câu chuyện huy chương, hãy đọc bài Figalli. Nếu muốn xem một sản phẩm tin học năm 2023, hãy bắt đầu từ bài báo này.

### 2. Lưới module trong mật mã hậu lượng tử

Tiêu chuẩn NIST FIPS 203 (tháng 8 năm 2024) chuẩn hóa ML-KEM, một cơ chế đóng gói khóa dựa trên lưới module, phát triển từ CRYSTALS-Kyber, với các bộ tham số ML-KEM-512/768/1024. Độ an toàn của nó dựa vào độ khó của bài toán Module-LWE, không liên quan đến lời giải bài toán xếp cầu ở chiều 8 hay 24. Mối liên hệ với chương này nằm ở hình học: lưới nhiều chiều, độ khó của bài toán tìm vectơ ngắn nhất, và bán kính giải mã kiểu xếp cầu là *ngôn ngữ* dùng để viết tiêu chuẩn. Muốn tìm hiểu các chiều đặc biệt 8 và 24 cùng dạng modular, hãy đọc bài Viazovska.

### 3. Tư duy chuyển pha trong SAT và học trên đồ thị

Bài toán $$k$$-SAT ngẫu nhiên và mô hình thấm (percolation) đều có ngưỡng sắc. Dưới một mật độ nhất định, trường hợp điển hình thì dễ giải (với SAT) hoặc liên thông (với thấm); vượt quá ngưỡng thì không còn như vậy. Các cuộc thi SAT ngày nay vẫn dùng những bộ đề nhân tạo và đề công nghiệp nằm gần các ngưỡng này. Các graph transformer như GraphGPS (Rampášek, Galkin, Dwivedi, Luu, Wolf và Beaini, 2022) kết hợp truyền tin cục bộ với cơ chế chú ý (attention) toàn cục có độ phức tạp $$O(N+E)$$. Chúng kế thừa cùng một trực giác từ vật lý thống kê: sự cân bằng giữa các lân cận cục bộ và một chế độ toàn cục. Đây không phải tiểu sử của Duminil-Copin hay Smirnov. Đây là một *thói quen*: tìm mật độ tới hạn trước khi tin vào một bộ giải hay một mạng nơ-ron đồ thị (GNN).

## Diễn giải và nhận định

Một mạng vận chuyển "chạy tốt" trên tập ảnh CelebA không phải là một định lý về tính chính quy của phương trình Monge–Ampère. Một cơ chế đóng gói khóa vượt qua quy trình tuyển chọn của NIST không phải là một định lý xếp cầu. Một GNN đạt điểm cao trên tập ZINC không chứng minh được gì về chuyển pha trong mô hình liên tục. Các kết quả gắn với Huy chương Fields là những phát biểu toán học chặt chẽ; các hệ thống tin học là những xấp xỉ đã được tinh chỉnh.

## Giới hạn và hướng mở rộng

Bài này cố ý không bàn về Hong Wang và bài toán Kakeya hay Yu Deng, và không kể lại công trình về cảm biến nén (compressed sensing) của Candès–Tao. Các nội dung đó đã có ở những trang khác. Bài cũng không khảo sát các huy chương năm 2026.

## Bài tập

1. Viết một câu dùng đúng từ "phương án vận chuyển" (plan) cho bài báo của Korotin và cộng sự, và một câu chỉ phù hợp với bài Figalli.
2. ML-KEM-768 được khuyến nghị cho nhiều ứng dụng thực tế. Giả thiết về độ khó của nó dựa trên đối tượng toán học nào? Định lý xếp cầu đoạt Fields nào *không* cần dùng đến?
3. Một đồng nghiệp nói GraphGPS "giải được bài toán thấm". Trên một đồ thị hữu hạn có thuộc tính, đại lượng nào thực sự đang được tối ưu?
4. Vì sao trang này không thêm một đoạn tiểu sử nữa vào loạt bài chân dung?

## Tài liệu tham khảo

- Korotin, A., Selikhanovych, D., & Burnaev, E. (2023). Neural optimal transport. *ICLR*. [arXiv:2201.12220](https://arxiv.org/abs/2201.12220).
- NIST. (2024). *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*. [doi:10.6028/NIST.FIPS.203](https://doi.org/10.6028/NIST.FIPS.203).
- Rampášek, L., Galkin, M., Dwivedi, V. P., Luu, A. T., Wolf, G., & Beaini, D. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Chân dung khóa học (không lặp ở đây): [Figalli]({{ site.baseurl }}/contents/vi/chapter02/02_20_Figalli_Optimal_Transport/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/).

## Video tham khảo

- **Xem trước**: [Alessio Figalli (2018 Fields Medal) explains Optimal Transport](https://www.youtube.com/watch?v=jyL6ZECM7oM) (Tom Rocks Maths, tiếng Anh). Figalli tự giải thích bài toán vận chuyển tối ưu bằng ngôn ngữ dễ hiểu. Nên xem trước khi đọc mục 1.
- [Post Quantum Cryptography - Computerphile](https://www.youtube.com/watch?v=_MoRcYLN-7U) (Computerphile, tiếng Anh). Giới thiệu mật mã hậu lượng tử và vì sao cần thay thế các hệ mật mã hiện nay. Xem cùng mục 2.
- [Fields Medal: Hugo Duminil-Copin](https://www.youtube.com/watch?v=5dXulZVstbY) (Simons Foundation, tiếng Anh). Phim ngắn về Duminil-Copin và các mô hình chuyển pha như mô hình thấm. Xem cùng mục 3 để hiểu nguồn gốc trực giác về ngưỡng.
