---
layout: post
title: "Ứng dụng hiện đại: Ý tưởng trọn đời trong hệ thống hiện nay"
chapter: '08'
order: 13
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: optional
---

## Mục tiêu học tập

Sau bài tùy chọn này, bạn có thể nhận ra ba *ý tưởng* lớn của các bài giải Abel trong chương, gồm hiện tượng tập trung, tính chính quy của nghiệm liên tục và cấu trúc rời rạc xem như toán học thực thụ, khi chúng xuất hiện trong các hệ thống CS/DS giai đoạn 2022–2026. Bài này không thêm tiểu sử nào vào phần giới thiệu các laureate.

## Kiến thức cần có

Phần tổng quan của chương, cùng ít nhất một trong các bài [Talagrand]({{ site.baseurl }}/contents/vi/chapter08/08_09_Talagrand_Probability/), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) hoặc [Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/). Bài này không nhắc lại phần trích dẫn giải thưởng.

## Mở đầu

Các bài về giải Abel nói về những công cụ được xây dựng qua hàng chục năm. Trong sản phẩm hiện nay, chúng thường xuất hiện dưới những cái tên khác. Các bất đẳng thức tập trung nằm sau nhiều phát biểu chung về khả năng tổng quát hóa. Lý thuyết chính quy cho PDE giúp ta hỏi một bộ giải học được có đang trả lời một câu hỏi có nghĩa hay không. Đồ thị expander và các cấu trúc đồ thị làm nền cho cả lý thuyết mã lẫn các graph Transformer hiện đại. Điều cần làm là giữ lại ý tưởng cốt lõi và bỏ đi phần ồn ào xung quanh.

## Phát triển khái niệm

Một hàm Lipschitz $$f$$ của nhiều biến độc lập thường tập trung quanh giá trị trung tâm: xác suất lệch cỡ $$t$$ giảm theo $$e^{-t^2/c}$$. Lý thuyết học máy biến trực giác này thành các cận PAC–Bayes và cận dựa trên lý thuyết thông tin cho độ chênh $$R(\hat h)-\hat R_S(\hat h)$$. Với PDE liên tục, câu hỏi là một biên tự do hay một trường Navier–Stokes có thể sinh ra kỳ dị hay không; một neural operator không quan tâm đến câu hỏi đó vẫn có thể nội suy tốt một tập dữ liệu. Còn toán rời rạc cho ta biết những expander và cách mã hóa đồ thị nào mà một mạng nơ-ron có thể dùng.

## Ba ví dụ

### 1. Hiện tượng tập trung và khả năng tổng quát hóa

Alquier (2024) có một bài tổng quan về các cận PAC–Bayes theo cách người làm học máy dùng được: từ một phân phối posterior (hoặc một bộ dự đoán ngẫu nhiên), ta có cận với xác suất cao cho rủi ro thật, tính từ rủi ro thực nghiệm cộng thêm một số hạng phức tạp. Ý tưởng hình học của Talagrand giải thích vì sao ở chiều cao, các đại lượng Lipschitz gần như là hằng số. Bài tổng quan trên đưa ý tưởng này vào việc chứng nhận chất lượng huấn luyện. Phần lớn các cận cho mạng sâu hiện vẫn quá lỏng để có giá trị về mặt số; đó là hạn chế của cách áp dụng, không phải bằng chứng rằng hiện tượng tập trung vô dụng.

### 2. Bộ giải liên tục và vấn đề kỳ dị

Kovachki và cộng sự (2023) trình bày các thí nghiệm neural operator trên những ánh xạ kiểu Navier–Stokes. Hãy đọc chúng cùng với lý thuyết chính quy của Caffarelli: nếu bài toán liên tục có thể có kỳ dị, thì một mạng trơn chỉ là mô hình của một thế giới *đã được làm trơn*. PINN và neural operator là những kỹ thuật hữu ích, nhưng chúng không thay thế được lý thuyết chính quy mà chương này nhắc đến.

### 3. Đồ thị là thành phần cơ bản trong kiến trúc

Rampášek và cộng sự (2022) kết hợp mã hóa vị trí, truyền thông điệp cục bộ và attention toàn cục trong kiến trúc GPS. Đây là bài học theo tinh thần Lovász–Wigderson: cấu trúc rời rạc không chỉ là bước khởi động cho giải tích, và nó được đưa vào một kiến trúc ở hội nghị NeurIPS. Hiệu ứng trộn giống expander là một lý do khiến attention toàn cục có ích, nhưng điều đó không chứng minh rằng mô hình *chính là* một expander.

## Diễn giải và nhận định

Một cận PAC–Bayes tính ra trong phòng thí nghiệm không phải là bất đẳng thức Talagrand. Một hình ảnh xoáy đẹp không phải là định lý của Caffarelli. Một checkpoint GraphGPS không phải là một cách dựng expander. Điều cần ghi nhớ là luôn biết mình đang mượn bổ đề nào.

## Giới hạn và hướng mở rộng

Lý thuyết gauge của Uhlenbeck, $$D$$-môđun của Kashiwara và định lý Atiyah–Singer được trình bày ở các bài riêng. Chúng cũng có ứng dụng trong khoa học máy tính (tính chỉ số, đại số tính toán), nhưng trong các sản phẩm giai đoạn 2022–2026 thì ít thấy hơn so với hiện tượng tập trung, PDE và đồ thị.

## Bài tập

1. Viết một câu về PAC–Bayes dùng hiện tượng tập trung đúng cách, và một câu nói quá, kiểu “chúng tôi đã chứng minh khả năng tổng quát hóa của GPT”.
2. Một neural operator được huấn luyện trên lực cưỡng bức trơn. Câu hỏi nào theo kiểu Caffarelli vẫn chưa được đặt ra?
3. Chỉ ra một thành phần của GPS thuộc lý thuyết đồ thị và một thành phần thuộc đại số tuyến tính (attention). Vì sao toán rời rạc trong giải Abel lại quan tâm đến việc cả hai đều là toán?
4. Vì sao bài này không thêm một đoạn kể lại các năm trao giải?

## Tài liệu tham khảo

- Alquier, P. (2024). User-friendly introduction to PAC–Bayes bounds. *Foundations and Trends in Machine Learning*. [arXiv:2110.11216](https://arxiv.org/abs/2110.11216).
- Kovachki, N., et al. (2023). Neural operator. *JMLR*, 24(89).
- Rampášek, L., et al. (2022). Recipe for a general, powerful, scalable graph transformer. *NeurIPS*. [arXiv:2205.12454](https://arxiv.org/abs/2205.12454).
- Các bài liên quan: [Talagrand]({{ site.baseurl }}/contents/vi/chapter08/08_09_Talagrand_Probability/), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/), [Lovász–Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).

## Video tham khảo

- **Xem trước** — [Michel Talagrand: Chaining: a long story](https://www.youtube.com/watch?v=3yIwl6XC0xA) — The Abel Prize, tiếng Anh. Bài giảng của Talagrand về kỹ thuật chaining, liên quan đến ví dụ về hiện tượng tập trung.
- [Luis Caffarelli: Non-linear and non-local surface structure problems and some of its applications](https://www.youtube.com/watch?v=dVGX6QhO8rU) — The Abel Prize, tiếng Anh. Xem sau khi đã nắm ý chính, liên quan đến ví dụ về tính chính quy của PDE.
- [The Abel lectures: László Lovász and Avi Wigderson](https://www.youtube.com/watch?v=zqiL57ebP-k) — The Abel Prize, tiếng Anh. Góc nhìn bổ sung về cấu trúc rời rạc, liên quan đến ví dụ về đồ thị.
