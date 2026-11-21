---
layout: post
title: "Luis Caffarelli: Free Boundary và PDE Phi tuyến (Abel 2023)"
chapter: '08'
order: 8
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

**Luis A. Caffarelli** (Đại học Texas tại Austin) nhận **Giải Abel 2023**

> “for his seminal contributions to regularity theory for nonlinear partial differential equations including free-boundary problems and the Monge–Ampère equation.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2023)

Bài này giải thích **lý thuyết chính quy** nhằm mục đích gì; **bài toán biên tự do** là gì; vì sao **Monge–Ampère** nằm ở trung tâm của các PDE hoàn toàn phi tuyến và của vận chuyển tối ưu; và **tính chính quy từng phần Caffarelli–Kohn–Nirenberg** cho Navier–Stokes liên quan đến bài toán Clay Millennium, nhưng không giải nó. Tài liệu: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài này, bạn có thể định nghĩa bài toán biên tự do và cho một ví dụ vật lý; giải thích mục tiêu của lý thuyết chính quy (khi nào nghiệm và mặt phân cách là trơn); đặt Monge–Ampère vào họ phương trình hoàn toàn phi tuyến; nêu tính chính quy từng phần CKN làm được gì và **không** làm được gì cho Navier–Stokes; và phân biệt việc suy ra phương trình chất lỏng (cầu nối động học) với tính chính quy của Navier–Stokes trong môi trường liên tục.

**Kiến thức nền.** Giải tích nhiều biến; ý niệm về PDE như phương trình Laplace $$\Delta u=0$$. Liên kết: [Navier–Stokes (Millennium)]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Deng và PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/), [ứng dụng của phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).

---

## 1. Lý thuyết chính quy

Với PDE elliptic tuyến tính có hệ số trơn, nghiệm thường trơn: tính chính quy của phương trình elliptic là một chiến thắng cổ điển. Với PDE **phi tuyến**, dữ liệu trơn không đương nhiên cho nghiệm trơn. Kỳ dị có thể hình thành; mặt phân cách tự do có thể có điểm nhọn; nghiệm yếu có thể tồn tại mà không có đạo hàm theo nghĩa cổ điển.

**Lý thuyết chính quy** cung cấp các ước lượng và định lý cấu trúc: khi nào nghiệm là $$C^\infty$$ hay giải tích; khi nào biên tự do là một siêu mặt trơn; khi nào tập kỳ dị có chiều được kiểm soát; khi nào giới hạn phóng đại (blow-up) rơi vào một danh sách mô hình đã được phân loại.

Sự nghiệp của Caffarelli là một lớp học bậc thầy về cách nhìn đó, trên biên tự do, các phương trình hoàn toàn phi tuyến và phương trình chất lỏng. Giải Abel 2023 vinh danh một **chương trình nghiên cứu**: dạy cách chứng minh biên tự do là trơn, hoặc phân loại khi nó không trơn, chứ không phải một ước lượng may mắn.

---

## 2. Biên tự do

### Cái gì “tự do”?

Bài toán biên cố định: miền được cho trước (giải $$\Delta u=0$$ trên đĩa với dữ liệu biên). Với **bài toán biên tự do**, vùng mà PDE thực sự được thỏa mãn là **chưa biết trước**. Mặt phân cách là một phần của ẩn số.

Các ví dụ cổ điển:

- **Bài toán chướng ngại (obstacle problem):** một màng đàn hồi đặt trên vật cản; biên của vùng tiếp xúc là tự do.  
- **Bài toán Stefan:** băng tan; mặt phân cách giữa rắn và lỏng chuyển động.  
- **Mặt phân cách chất lỏng:** các vùng pha hay chất lỏng khác nhau.

Về toán, thường ta nghiên cứu $$u$$ thỏa các phương trình khác nhau trên $$\{u>0\}$$ và $$\{u=0\}$$, với một điều kiện truyền trên biên tự do $$\partial\{u>0\}$$.

### Caffarelli làm thay đổi lĩnh vực

Ông phát triển các kỹ thuật **phóng đại (blow-up)**, **công thức đơn điệu** và **phân loại**, biến lý thuyết biên tự do thành một lĩnh vực chín muồi với các kết luận hình học. Câu hỏi chuyển từ “nghiệm yếu có tồn tại không?” sang “biên tự do trơn đến mức nào, và các kỳ dị trông ra sao?”.

Các phát biểu về độ trơn gần tối ưu và việc phân loại các profile phóng đại đã trở thành khuôn mẫu cho chương trình nghiên cứu biên tự do rộng hơn, kể cả các biến thể phi địa phương và hoàn toàn phi tuyến của các trường phái sau này.

---

## 3. Bài toán chướng ngại như một mô hình

Bài toán chướng ngại cổ điển tìm vị trí cân bằng của một màng bị ràng buộc nằm trên một vật cản $$\varphi$$. Dưới dạng biến phân: cực tiểu hóa năng lượng Dirichlet trong lớp $$v\ge\varphi$$. Nghiệm $$u$$ là điều hòa (hoặc thỏa một phương trình elliptic liên quan) ở những nơi không chạm vật cản; **tập tiếp xúc** $$\{u=\varphi\}$$ có biên tự do.

Lý thuyết chính quy hỏi: $$u$$ chính quy đến đâu? Biên tự do chính quy đến đâu? Dạng phóng đại tại một điểm của biên tự do là gì?

Các kết quả của Caffarelli cho những câu trả lời sâu sắc trong bối cảnh cổ điển và đặt ra mô thức: phóng to, đổi tỉ lệ, phân loại các giới hạn thuần nhất, rồi đưa thông tin trở lại thang ban đầu. Biên tự do ở đây không phải do ta “tự chọn cho tiện”: mặt phân cách **do chính bài toán quyết định**.

---

## 4. Hoàn toàn phi tuyến và Monge–Ampère

### Phương trình elliptic hoàn toàn phi tuyến

Phương trình phụ thuộc phi tuyến vào Hessian $$D^2u$$, không chỉ vào $$u$$ và $$\nabla u$$. Lý thuyết elliptic tuyến tính không áp dụng “nguyên si” được; cần đến nghiệm nhớt (viscosity), các ước lượng kiểu Krylov–Safonov, và điều kiện cấu trúc (elliptic đều, tính lồi, …).

### Monge–Ampère

Phương trình **Monge–Ampère**

$$
\det D^2 u = f(x,u,\nabla u)
$$

(ở dạng thích hợp) là trung tâm của hình học affine, bài toán độ cong cho trước, và **vận chuyển tối ưu** (một thế lồi thỏa Monge–Ampère sẽ nối hai độ đo). Lý thuyết chính quy của Caffarelli cho Monge–Ampère là một trụ cột của giải tích hình học và lý thuyết vận chuyển hiện đại.

Citation của Abel nêu Monge–Ampère một cách tường minh: nó không phải một dự án phụ, mà là một đầu tàu của chương trình chính quy phi tuyến. Khi chương 06 đề cập đến vận chuyển tối ưu, hãy nhớ rằng tính chính quy của ánh xạ vận chuyển thường quy về PDE kiểu Monge–Ampère: đó là cầu nối từ giải Abel sang hình học ứng dụng.

---

## 5. Tính chính quy từng phần của Navier–Stokes (CKN)

Cùng với **Robert Kohn** và **Louis Nirenberg**, Caffarelli chứng minh **tính chính quy từng phần** cho các nghiệm yếu thích hợp của Navier–Stokes: tập kỳ dị, nếu không rỗng, bị ràng buộc chặt về độ đo trong không–thời gian (không thể “quá lớn”; chiều Hausdorff parabolic của tập kỳ dị được kiểm soát).

Đây là một trong những kết quả từng phần sâu nhất về tính chính quy của Navier–Stokes, và vẫn **chưa đủ** để có tính trơn toàn cục cho mọi dữ liệu trơn trong 3D. Nó vẫn là [bài toán Clay Millennium]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).

### Ba trục cần phân biệt (rất quan trọng cho seminar)

| Trục | Câu hỏi | Trạng thái |
|------|---------|------------|
| Suy ra phương trình / cầu nối động học | Mô hình liên tục liên hệ thế nào với mô hình hạt | Nghiên cứu sôi nổi ([Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/)) |
| Tính chính quy từng phần CKN | Tập kỳ dị của nghiệm yếu lớn đến mức nào? | Định lý lớn; tập kỳ dị được kiểm soát |
| Bài toán Millennium còn mở | Nghiệm trơn 3D có luôn trơn toàn cục không? | Còn mở |

Đừng gộp ba trục này thành một khẩu hiệu. Điểm chính của bài: **tính chính quy từng phần không có nghĩa là Navier–Stokes đã được giải**.

---

## 6. Vì sao đáng giải Abel 2023

Chính quy của PDE phi tuyến là hạ tầng của hình học, vật lý và giải tích ứng dụng. Biên tự do xuất hiện trong khoa học vật liệu và tài chính; Monge–Ampère trong lý thuyết vận chuyển và hình học; Navier–Stokes trong động lực học chất lỏng. Các ước lượng và phương pháp của Caffarelli đã trở thành **ngôn ngữ** mà nhiều hướng nghiên cứu cùng nói.

Giải Abel vinh danh một chương trình dài hơi: không phải một ước lượng may mắn, mà là sự nghiệp dạy cách chứng minh biên tự do trơn, hoặc phân loại khi nó không trơn.

### Phóng đại như một phương pháp (một đoạn dùng lại được)

Xuyên suốt lý thuyết biên tự do, động tác chuẩn là: tại một điểm $$x_0$$ trên biên tự do, đổi tỉ lệ

$$
u_r(x) = \frac{u(x_0 + r x)}{\text{normalization}(r)}
$$

rồi lấy giới hạn $$r\to 0$$. Giới hạn thường là nghiệm thuần nhất của bài toán mô hình; việc phân loại chúng cho ta thông tin chính quy về biên tự do ban đầu. Công thức đơn điệu kiểm soát việc đổi tỉ lệ và ngăn năng lượng dao động hoang dại. Nắm được triết lý này ngay từ lần đầu còn giá trị hơn việc nhớ mọi con số trong các định lý, và đó chính là triết lý mà trường phái Caffarelli đã chuẩn hóa.

---

## 7. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “CKN giải xong bài toán Millennium về Navier–Stokes.” | Chính quy từng phần khác với chính quy hoàn toàn cho mọi dữ liệu trơn. |
| “Biên tự do là biên của miền ta chọn cho tiện.” | Mặt phân cách là **ẩn số**, do chính bài toán quyết định. |
| “PDE phi tuyến không thể có nghiệm trơn.” | Nhiều phương trình có; lý thuyết chính quy nói khi nào và như thế nào. |
| “Monge–Ampère chỉ dành cho vận chuyển tối ưu.” | Vận chuyển tối ưu là một mái nhà lớn; PDE hình học và hình học affine là những mái nhà khác. |
| “Giải Abel 2023 chỉ nói về chất lỏng.” | Biên tự do và Monge–Ampère có vị trí ngang nhau trong citation. |

---

## Điều rút ra ở mức đại học

1. **Biên tự do** là mặt phân cách chưa biết trước, gắn với một PDE.  
2. **Phóng đại** là phóng to cho đến khi bài toán thuần nhất xuất hiện.  
3. **Chính quy từng phần** nghĩa là trơn hầu như khắp nơi, với một chặn về chiều của tập “xấu”.  
4. **Giải tích tầm cỡ giải thưởng** thường cải thiện *bản đồ các kỳ dị có thể có*, chứ không chỉ chứng minh sự tồn tại nghiệm cổ điển.

### Bảng cho seminar (điền trong lớp)

| Chủ đề | Mô hình đơn giản | Người anh em khó | “Chính quy” nghĩa là gì |
|--------|------------------|------------------|--------------------------|
| Bài toán chướng ngại | Sợi dây 1D đặt trên gờ | Biên tự do chiều cao | Mặt phân cách trơn |
| Navier–Stokes | Tuyến tính hóa thành phương trình Stokes | Bài toán Millennium về Navier–Stokes | Không nổ; tập kỳ dị được kiểm soát |
| Monge–Ampère | Thế lồi 2D | Ánh xạ vận chuyển tối ưu | Ước lượng $$C^{1,\alpha}$$ hoặc cao hơn |

### Cảnh báo về CFD

Các chương trình CFD “giải Navier–Stokes” hằng ngày bằng rời rạc hóa và mô hình hóa. Bài toán mở của toán học nói về *phương trình liên tục chính xác* trong một lớp không gian hàm được phát biểu chặt chẽ. Hãy để thành công kỹ thuật và trạng thái Millennium ở **hai cột khác nhau** trong bài luận của bạn.

---

## Bài tập

1. Cho một ví dụ vật lý về biên tự do; chỉ ra mặt phân cách ẩn.  
2. Chính quy từng phần và chính quy hoàn toàn: hai câu.  
3. Ba trục: suy ra phương trình (Deng) / từng phần (CKN) / Millennium còn mở. Mỗi trục một cụm từ.  
4. **Không quá 250 từ:** vì sao tính chính quy của biên tự do vừa mang tính hình học vừa mang tính giải tích?  
5. Nối với [ứng dụng của phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/) bằng một câu về ứng dụng.  
6. Lướt qua trang Abel 2023 trên [abelprize.no](https://abelprize.no/); ghi ba từ khóa.  
7. **Seminar:** không dùng công thức, giải thích vì sao phóng to có thể biến một biên tự do cong thành bài toán hình nón hay nửa không gian, dễ phân loại hơn.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2023: tính chính quy của PDE phi tuyến, biên tự do, Monge–Ampère.
- Chính quy từng phần CKN cho Navier–Stokes không phải là lời giải của bài toán Clay.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: bài giảng Abel của Caffarelli, về cấu trúc mặt phi tuyến: [https://www.youtube.com/watch?v=dVGX6QhO8rU](https://www.youtube.com/watch?v=dVGX6QhO8rU).  
2. **Lịch sử**: phỏng vấn Caffarelli của giải Abel 2023: [https://www.youtube.com/watch?v=rz3uPOIL9AA](https://www.youtube.com/watch?v=rz3uPOIL9AA).  
3. **Định hướng**: phim ngắn về Caffarelli: [https://www.youtube.com/watch?v=tdUBLu4fHbw](https://www.youtube.com/watch?v=tdUBLu4fHbw).  
4. **Định hướng**: phản ứng khi nhận cuộc gọi về giải Abel: [https://www.youtube.com/watch?v=ze4SKx5yBFw](https://www.youtube.com/watch?v=ze4SKx5yBFw).  

**Cổng chính thức và tài liệu**

- Abel 2023 Caffarelli: https://abelprize.no/abel-prize-laureates/2023  

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/caffarelli-pde_dVGX6QhO8rU_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu

### Danh mục nguồn

1. Abel 2023 Caffarelli — https://abelprize.no/abel-prize-laureates/2023  
2. Caffarelli Abel lecture — non-linear surface structure — https://www.youtube.com/watch?v=dVGX6QhO8rU  
3. Abel interview Caffarelli 2023 — https://www.youtube.com/watch?v=rz3uPOIL9AA  
4. Caffarelli short film — https://www.youtube.com/watch?v=tdUBLu4fHbw  
5. Reaction to Abel Prize call — https://www.youtube.com/watch?v=ze4SKx5yBFw  
6. Wikipedia — Luis Caffarelli — https://en.wikipedia.org/wiki/Luis_Caffarelli  
7. Wikipedia — Free boundary problem — https://en.wikipedia.org/wiki/Free_boundary_problem  
8. Wikipedia — Obstacle problem — https://en.wikipedia.org/wiki/Obstacle_problem  
9. Clay — Navier–Stokes (contrast partial regularity) — https://www.claymath.org/millennium/navier-stokes-equation/  
10. Abel popular PDFs (pde/obstacle/freeBoundary) — https://abelprize.no/abel-prize-laureates/2023  

1. [Abel 2023](https://abelprize.no/abel-prize-laureates/2023).  
2. Bài khảo sát về biên tự do; văn liệu về Monge–Ampère.  
3. Caffarelli–Kohn–Nirenberg (chính quy từng phần của Navier–Stokes).  
4. Bài mô tả bài toán Navier–Stokes của Fefferman cho Clay; bài về Navier–Stokes và Deng trong khóa học.

---

## Hướng đi tiếp

- Một ẩn dụ kỹ thuật: mô phỏng sự đổi pha so với định lý.  
- Bảng cho seminar: Millennium Navier–Stokes / CKN / chính quy của biên tự do.  
- Ghi lại rằng bài toán Millennium về Navier–Stokes là người láng giềng gần nhất của CKN.  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp theo: [Talagrand]({{ site.baseurl }}/contents/vi/chapter08/08_09_Talagrand_Probability/).

## Video tham khảo

- **Xem trước** — [Luis Caffarelli: Non-linear and non-local surface structure problems and some of its applications](https://www.youtube.com/watch?v=dVGX6QhO8rU) — The Abel Prize, tiếng Anh. Xem trước để nghe chính Caffarelli giới thiệu các bài toán cấu trúc mặt phi tuyến và các ứng dụng.
- [Luis A. Caffarelli - The Abel Prize Interview 2023](https://www.youtube.com/watch?v=rz3uPOIL9AA) — The Abel Prize, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để nghe ông kể về con đường làm toán.
- [Luis A. Caffarelli - the 2023 Abel Prize Laureate](https://www.youtube.com/watch?v=tdUBLu4fHbw) — The Abel Prize, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, qua một đoạn phim ngắn giới thiệu laureate.
