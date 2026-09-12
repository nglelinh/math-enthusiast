---
layout: post
title: "Curtis McMullen: Động lực chỉnh hình và geometrization (Huy chương Fields 1998)"
chapter: '02'
order: 25
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Curtis T. McMullen** nhận **Huy chương Fields 1998** “for his contributions to the theory of holomorphic dynamics and geometrization of three-manifolds, including proofs of Bers’ conjecture on the density of cusp points in the boundary of the Teichmüller space, and Kra’s theta-function conjecture.” Huy chương đặt tên một cây cầu: iteration của ánh xạ chỉnh hình, hình học không gian Teichmüller, và cấu trúc hyperbolic trên đa tạp ba chiều chia sẻ một ngôn ngữ renormalization.

Bài này dành cho người đã thấy đa thức bậc hai $$z\mapsto z^2+c$$ và một mặt giống $$g\ge 2$$, muốn nắm kiến trúc động lực phức cuối thập niên 1990. Bài **không** tuyên bố tập Mandelbrot liên thông địa phương (MLC vẫn mở), cũng không nói McMullen hoàn tất chương trình geometrization của Thurston. Nó giải thích khẩu hiệu cẩn thận: ánh xạ kiểu bậc hai, mật độ cusp trên biên Bers, toán tử theta Poincaré, và một định lý độ cứng tầm Fields sắp xếp lại nhiều phòng thí nghiệm cùng lúc.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nêu trích dẫn 1998 của McMullen trong một đoạn cẩn thận, kể động lực chỉnh hình, geometrization, Bers, và Kra.
- Giải thích **ánh xạ kiểu bậc hai** (quadratic-like, Douady–Hubbard) như phủ phân nhánh chỉnh hình bậc hai hành xử như $$z^2+c$$ sau khi làm thẳng.
- Mô tả **giả thuyết Bers** ở mức khẩu hiệu: các điểm cusp (hữu hạn hình học) trù mật trong biên của một compact hóa Teichmüller / Bers.
- Mô tả **giả thuyết theta của Kra** như sự co chặt của toán tử chuỗi Poincaré trên vi phân toàn phương.
- Giữ **MLC** được gắn nhãn mở, và đặt McMullen cạnh [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/) và [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) mà không gộp ba huy chương thành một câu chuyện.

**Kiến thức nền.** Hàm chỉnh hình một biến; iteration đa thức ở mức biết tên tập Julia và Fatou; ý niệm mặt hyperbolic có không gian Teichmüller các metric được đánh dấu. Không cần khóa Kleinian group trước.

**Liên kết seminar.** LO1 / LO4 (chương trình khó; iteration cổ điển ↔ hình học moduli). Ghép [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/) cho typicality renormalization sau này, [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) cho động lực *trên* không gian moduli, và [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/) chỉ như *một* chương geometrization khác (Ricci flow), không phải phương pháp của McMullen.

---

## 1. Vì sao iteration phức cần moduli

Khóa động lực phức đầu tiên nghiên cứu một ánh xạ $$f(z)=z^2+c$$, tập Julia, và tập Mandelbrot $$M$$ các tham số có quỹ đạo tới hạn bị chặn. Đó là điểm khởi đúng. Đó là điểm kết sai cho lý thuyết đoạt Fields.

Động lực chỉnh hình hiện đại thường là lý thuyết các **ánh xạ trông như bậc hai sau đổi tọa độ**. Douady và Hubbard tách **ánh xạ kiểu bậc hai**: phủ phân nhánh chỉnh hình bậc hai $$f:U\to V$$ giữa các miền đơn liên trên mặt phẳng, với $$\overline{U}$$ compact trong $$V$$. **Định lý làm thẳng** của họ gửi $$f$$ ấy tới một đa thức bậc hai thật, miễn là quỹ đạo tới hạn không thoát. Renormalization—hạn chế, trở lại, đổi tỷ lệ—rồi sản sinh ánh xạ kiểu bậc hai mới từ ánh xạ cũ.

McMullen, xây trên Sullivan, Douady–Hubbard, và lý thuyết hình học renormalization đang hình thành, xem toán tử ấy như nguồn **độ cứng**: khi một ánh xạ renormalizable vô hạn nằm trong lớp thích hợp, hình học ở thang nhỏ được kiểm soát, và các ánh xạ lân cận không thể biến dạng quá tự do. Độ cứng ấy đi xa. Cùng phân tích thang nhỏ thông báo cho nhóm Kleinian và đa tạp hyperbolic ba chiều phân thớ trên đường tròn.

**Khẩu hiệu.** Động lực của ánh xạ trở thành hình học **trên** một không gian ánh xạ—rồi hình học đa tạp ba chiều.

---

## 2. Giả thuyết Bers: cusp trên biên

Không gian Teichmüller $$\mathcal{T}(S)$$ tham số hóa các metric hyperbolic được đánh dấu (hoặc cấu trúc phức) trên một mặt $$S$$ hữu hạn kiểu. Bers compact hóa các mảnh không gian này bằng đa tạp hyperbolic quasi-Fuchsian ba chiều có biên conformal gồm hai mặt Riemann. **Biên Bers** chứa nhiều điểm tương ứng nhóm suy biến.

Một điểm **cusp**, theo nghĩa trích dẫn, là suy biến hữu hạn hình học: một nhóm Kleinian đã có thêm phần tử parabolic, như mặt hyperbolic đang phát triển một châm. **Giả thuyết Bers**—do McMullen chứng minh—khẳng định các điểm cusp ấy **trù mật** trong biên liên quan của không gian Teichmüller.

**Điều này sắp xếp lại gì.** Biên không còn là bảo tàng riêng các giới hạn kỳ dị. Các suy biến hữu hạn hình học, hiểu được, nằm trù mật giữa những cái hoang hơn. Mật độ không phải phân loại mọi điểm biên; đó là phát biểu rằng các điểm “thuần” dày theo nghĩa tôpô.

---

## 3. Giả thuyết theta của Kra

Cho $$X$$ là mặt Riemann hyperbolic diện tích hữu hạn, với phủ phổ dụng $$\mathbb{H}\to X$$ và nhóm phủ $$G$$. Các vi phân toàn phương chỉnh hình chuẩn hữu hạn tạo không gian Banach $$Q(\mathbb{H})$$ và $$Q(X)$$. **Chuỗi Poincaré** (toán tử theta) lấy trung bình một vi phân trên đĩa theo $$G$$ và đáp xuống $$Q(X)$$. Chuẩn toán tử của nó không vượt quá một. **Giả thuyết Kra**, do McMullen chứng minh, nói chuẩn **chặt nhỏ hơn một**.

McMullen thực ra còn đặc trưng, với một lớp phủ rộng hơn, khi sự co chặt này đúng, bằng ngôn ngữ phủ **amenable**. Ước lượng giải tích không phải tò mò cô lập. Nó nuôi lý thuyết biến dạng nhóm Kleinian và, như lời ca ngợi 1998 nhấn mạnh, đóng góp cho chương trình của Thurston đặt metric hyperbolic trên một lớp lớn đa tạp ba chiều—đặc biệt những đa tạp phân thớ trên đường tròn, bối cảnh của chuyên khảo *Renormalization and 3-manifolds which fiber over the circle* (1996) của McMullen.

**Độ chính xác.** Đây là một chương của geometrization, không thay thế lời giải Ricci flow của Perelman cho toàn bộ giả thuyết geometrization.

---

## 4. Phần còn mở: MLC và bạn bè

**Liên thông địa phương của tập Mandelbrot (MLC)** là giả thuyết nổi tiếng của Douady–Hubbard. Liên thông địa phương sẽ mở một mô hình tổ hợp chính xác của $$M$$. Độ cứng renormalization của McMullen thuộc vòng ý tưởng quanh MLC, và nhiều lớp tham số đặc biệt đã hiểu. **Bản thân MLC chưa được chứng minh.** Câu seminar “McMullen chứng tỏ tập Mandelbrot liên thông địa phương” là sai.

Cùng vậy, “McMullen geometrize mọi đa tạp ba chiều” là sai. Mệnh đề geometrization trong trích dẫn cụ thể: động lực chỉnh hình thông báo cấu trúc hyperbolic, gồm đa tạp phân thớ và không gian biến dạng nhóm Kleinian.

---

## 5. Các bài kề trong khóa học

[Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/) thừa hưởng máy renormalization và hỏi các câu **typicality** trong động lực thực và quasi-periodic. Điểm nhấn 1998 của McMullen nghiêng **hình học và độ cứng**: mật độ cusp, co của toán tử theta, và từ điển giữa renormalization vô hạn và đa tạp hyperbolic ba chiều.

[Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) nghiên cứu dòng và phép đếm **trên** không gian moduli—earthquake, thể tích Weil–Petersson, trắc địa đóng đơn. McMullen nghiên cứu cách không gian Teichmüller ngồi như không gian biến dạng nhóm và cách biên của nó được cư trú. Cùng thành phố, việc khác.

**Đừng viết** “McMullen phát minh renormalization.” Feigenbaum, Sullivan, Douady và Hubbard đã biến nó thành đối tượng toán học. McMullen biến nó thành **cầu nối tới hình học hyperbolic ba chiều**.

---

## 6. Vì sao Huy chương Fields

Ba lý do khóa vào nhau:

1. **Độ khó.** Mật độ Bers và sự co chặt của Kra chống lại nỗ lực dài; chứng minh trộn giải tích phức, ý tưởng ergodic về amenability, và tôpô đa tạp ba chiều.
2. **Vị trí trung tâm.** Một khi renormalization nói chuyện với nhóm Kleinian, động lực chỉnh hình và geometrization chia sẻ định lý, không chỉ loại suy.
3. **Khẩu hiệu rõ, phương pháp sâu.** “Cusp trù mật trên biên Bers” là câu học viên cao học nhớ được; chứng minh là công trình lớn của hình học thập niên 1990.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “McMullen chứng minh MLC.” | Liên thông địa phương của tập Mandelbrot vẫn mở. |
| “Geometrization trong trích dẫn là định lý Perelman.” | McMullen đóng góp cấu trúc hyperbolic và đa tạp phân thớ; công trình Ricci flow của Perelman là hoàn tất sau, khác phương pháp. |
| “Mật độ Bers phân loại cả biên.” | Mật độ cusp không nhận diện mọi điểm biên. |
| “Giả thuyết Kra nói về hàm theta lý thuyết số.” | Nó nói về toán tử chuỗi Poincaré trên vi phân toàn phương. |
| “Renormalization ở đây chỉ là period-doubling Feigenbaum.” | Renormalization kiểu bậc hai rộng hơn và được dùng như máy hình học. |

---

## Bài tập

1. Bằng lời của bạn: làm thẳng một ánh xạ kiểu bậc hai **quên** và **giữ** điều gì?
2. Vì sao mật độ điểm cusp yếu hơn phân loại đầy đủ biên Bers?
3. Viết một câu nêu giả thuyết Kra không ký hiệu, rồi một câu đặt tên toán tử có chuẩn $$<1$$.
4. Phân biệt tập Julia (mặt phẳng động lực) với tập Mandelbrot (mặt phẳng tham số) trong một đoạn.
5. **Luyện độ chính xác.** Tìm một câu phổ thông nói MLC là định lý. Viết lại thành hai câu chính xác.
6. **Seminar mở rộng.** So văn hóa độ cứng/renormalization của McMullen với [typicality của Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/) và [động lực moduli của Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/). Mỗi bên trả lời câu hỏi nào?

---

## Nguồn video và đọc thêm

1. **Trích dẫn IMU** — Fields Medals 1998, Curtis T. McMullen: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998).
2. **Định hướng** — Phỏng vấn CIRM với McMullen (chủ đề nghiên cứu và huy chương): [carmin.tv](https://www.carmin.tv/en/collections/dynamics-and-geometry-in-the-teichmuller-space-dynamique-et-geometrie-dans-lespace-de-teichmuller/video/interview-at-cirm-curtis-mcmullen).
3. **Chuyên khảo** — C. T. McMullen, *Renormalization and 3-manifolds which fiber over the circle*, Princeton University Press, 1996.

**Nhắc trạng thái:** Động lực chỉnh hình và một số định lý geometrization chọn lọc—**không** chứng minh MLC, và không geometrization đầy đủ mọi đa tạp ba chiều.

---

## Tài liệu tham khảo

1. IMU Fields Medal 1998 — Curtis T. McMullen (mathunion.org).
2. **C. T. McMullen**, công trình mật độ Bers, giả thuyết Kra, và renormalization ánh xạ kiểu bậc hai; lời ca ngợi ICM 1998.
3. **A. Douady and J. H. Hubbard**, làm thẳng ánh xạ kiểu bậc hai; từ điển Sullivan giữa ánh xạ hữu tỷ và nhóm Kleinian.
4. Bài kề: [Avila]({{ site.baseurl }}/contents/vi/chapter02/02_16_Avila_Dynamics/), [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/) (đường geometrization tách biệt).

---

## Hướng đi tiếp

- Đọc một survey từ điển Sullivan (ánh xạ hữu tỷ ↔ nhóm Kleinian) và liệt kê ba mục khớp.
- So tính phổ quát Feigenbaum như phát hiện vật lý với renormalization hình học của McMullen.
- Tùy chọn seminar A3: một trang về điều MLC sẽ mở—và điều đã biết khi chưa có nó—không tuyên bố huy chương đã đóng động lực phức.
