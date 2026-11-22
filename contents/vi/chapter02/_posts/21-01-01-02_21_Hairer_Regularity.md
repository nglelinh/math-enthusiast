---
layout: post
title: "Martin Hairer: Cấu trúc Chính quy cho PDE Ngẫu nhiên (Huy chương Fields 2014)"
chapter: '02'
order: 21
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

**Martin Hairer** nhận **Huy chương Fields 2014** vì những đóng góp xuất sắc cho lý thuyết phương trình đạo hàm riêng ngẫu nhiên, và đặc biệt vì việc tạo ra một lý thuyết các cấu trúc chính quy (regularity structures) cho những phương trình ấy. Huy chương không đặt tên một nghiệm dạng đóng duy nhất. Nó đặt tên một phép tính: khi nhiễu trắng không-thời gian quá thô để tích thông thường còn nghĩa, người ta khai triển nghiệm thành chuỗi Taylor địa phương mà các “đơn thức” tự chúng là ngẫu nhiên, rồi renormalize các tích bất hợp pháp để khai triển thỏa phương trình.

Bài này dành cho người học đã gặp phép tính Itô hữu hạn chiều và muốn nắm kiến trúc của các SPDE kỳ dị hiện đại. Bài **không** khẳng định Hairer giải bài toán Thiên niên kỷ Navier–Stokes tất định, cũng không khẳng định cấu trúc chính quy thay mọi cách tiếp cận trước. Nó giải thích khẩu hiệu cẩn thận: vì sao tích của các phân bố có thể thất bại, điều mà rough paths của Lyons đã sửa ở một chiều, và máy của Hairer sắp xếp lại điều gì cho các phương trình như KPZ và $$\Phi^4_3$$.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao một SPDE như KPZ là **kỳ dị**: nhiễu là phân bố không-thời gian, và các hạng tử phi tuyến không được định nghĩa bằng phép nhân ngây thơ.
- Định vị **rough paths của Lyons** như tiền thân khôi phục quy tắc chuỗi (hoặc lựa chọn Itô–Stratonovich) cho các đường được kiểm soát.
- Mô tả một **cấu trúc chính quy** ở mức khẩu hiệu: một tập ký hiệu mô hình đã phân bậc, một mô hình hiện thực hóa chúng thành phân bố, và một định lý tái dựng biến phân bố được mô hình hóa thành phân bố thực sự.
- Kể tên hai phương trình cột mốc được lý thuyết làm chặt: phương trình Kardar–Parisi–Zhang, và động lực $$\Phi^4_3$$.
- Phân biệt **ergodicity của Navier–Stokes ngẫu nhiên hai chiều** Hairer–Mattingly với câu hỏi Thiên niên kỷ còn mở về chính quy tất định ba chiều.

**Kiến thức nền.** Chuyển động Brown và tích phân Itô ở mức khẩu hiệu; phương trình nhiệt như toán tử làm trơn; ý rằng một phân bố không nhất thiết là hàm. Không cần nền White Noise hay đại số Hopf trước đó.

**Liên kết seminar.** LO1 / LO4 (chương trình giải tích khó; phương trình vật lý hình thức ↔ phép tính renormalize). Ghép với [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) cho một văn hóa PDE khác từ ngẫu nhiên sang tất định, và với bài toán Navier–Stokes ở Chương 1 chỉ để **tách** ergodicity 2D ngẫu nhiên khỏi phát biểu Thiên niên kỷ.

---

## 1. Vì sao phép tính PDE thông thường dừng lại

Một phương trình nhiệt ngẫu nhiên tuyến tính

$$
\partial_t u=\Delta u+\xi
$$

có thể được giải bằng chập với nhân nhiệt ngay cả khi $$\xi$$ là nhiễu trắng không-thời gian, một phân bố ngẫu nhiên không phải hàm. Nghiệm $$u$$ thường Hölder theo không-thời gian, nhưng với số mũ thấp. Ngay khi phương trình trở nên phi tuyến—KPZ,

$$
\partial_t h=\partial_{xx}h+(\partial_x h)^2+\xi,
$$

hoặc phương trình động lực $$\Phi^4_3$$ trên torus ba chiều—người ta phải nhân những đối tượng mà độ chính quy cộng lại thành số âm. Trong ngôn ngữ phân bố, tích ấy không được định nghĩa. Nhà vật lý trừ vô cùng (renormalization) và nhận dự đoán hữu hạn; nhà toán học cần một không gian trong đó những phép trừ ấy là định lý.

**Khẩu hiệu.** Khó khăn không phải “PDE có tính ngẫu nhiên.” Khó khăn là **nhân những đối tượng không phải hàm**.

---

## 2. Lịch sử ý tưởng: Lyons, rồi Hairer

Lý thuyết **rough path** của Terry Lyons (thập niên 1990) giải một analogue một tham số. Một phương trình vi phân thường bị dẫn bởi đường không trơn $$X$$ không thể được diễn giải chỉ từ $$X$$ nếu $$X$$ thô như chuyển động Brown; người ta còn phải quy định các tích phân lặp, một “nâng” của $$X$$. Một khi nâng tồn tại, các đường được kiểm soát có tích phân vững và một định lý liên tục: các nâng gần nhau cho nghiệm gần nhau. Rough paths được kiểm soát của Gubinelli và phép tính paracontrolled liên quan (Gubinelli–Imkeller–Perkowski) sau đó xử lý một số SPDE bằng sổ sách tương tự.

Các **cấu trúc chính quy** của Hairer (Invent. Math., 2014) mở rộng ý tưởng từ các đường chỉ số hóa theo thời gian sang các phân bố chỉ số hóa theo không-thời gian. Người ta xây một đại số trừu tượng đã phân bậc gồm các ký hiệu (cây trang trí mã hóa tích phân lặp đối với nhiễu), một **mô hình** hiện thực hóa mỗi ký hiệu thành một phân bố cụ thể, và khái niệm **phân bố được mô hình hóa**—một hàm trông, tại mỗi điểm, như tổ hợp tuyến tính hữu hạn của những ký hiệu ấy, với hệ số biến thiên đủ chính quy. Một định lý tái dựng sinh ra một phân bố thực sự. Renormalization trở thành sự đổi mô hình có hệ thống, trừ các hằng số phân kỳ (hoặc, trong công trình đại số sau với Bruned, Hairer và Zambotti, tổ chức những hằng số ấy bằng coproduct đại số Hopf).

Trích dẫn 2014 nêu bật sự tạo ra ấy. Các bài Hairer trước—nổi tiếng nhất là nghiệm phương trình KPZ năm 2013 (Ann. of Math.)—đã cho thấy một phương trình đã renormalize có thể được gán một nghĩa duy nhất; cấu trúc chính quy biến phương pháp thành một cỗ máy có thể mang đi.

---

## 3. Một cấu trúc chính quy sắp xếp lại điều gì

Xét dạng khẩu hiệu của chương trình:

> Viết nghiệm địa phương như một jet hữu hạn trong một cơ sở xây từ nhiễu; giải bài toán điểm bất động cho các hệ số jet; tái dựng; renormalize để điểm bất động vẫn hữu hạn khi cutoff tử ngoại được gỡ.

Điều này sắp xếp lại danh sách các phương trình **đặt chỉnh** như đối tượng continuum. Trước cấu trúc chính quy, nhiều SPDE kỳ dị hoặc chỉ được diễn giải sau khi làm trơn thêm, hoặc được xử lý bằng mẹo gắn với từng mô hình. Sau đó, một lớp lớn—gồm KPZ, mô hình Anderson parabolic ở chiều thấp, và $$\Phi^4_3$$—nằm dưới một mái nhà giải tích–đại số.

**$$\Phi^4_3$$** là lượng tử hóa ngẫu nhiên của độ đo Euclid $$\varphi^4$$ ba chiều: một phương trình phản ứng–khuếch tán với hạng tử bậc ba và nhiễu trắng không-thời gian. Làm cho động lực đặt chỉnh cung cấp một xây dựng động lực của một độ đo mà lý thuyết trường kiến tạo đã nghiên cứu bằng phương tiện khác. Đó **không** phải xây dựng một trường vô hướng tương tác bốn chiều không tầm thường; hãy so sánh các định lý triviality bốn chiều trong chân dung [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase/).

---

## 4. Hairer–Mattingly: ergodicity, không phải bài toán Thiên niên kỷ

Một cộng tác khác, sớm hơn, đáng được một khung sạch để các tường thuật phổ thông không trộn nó với bài toán Navier–Stokes của Viện Clay. Hairer và Mattingly (Ann. of Math., 2006) chứng minh tính duy nhất của độ đo bất biến cho **phương trình Navier–Stokes không nén hai chiều với lực ngẫu nhiên thoái hóa**: nhiễu chỉ được bơm vào hữu hạn mode Fourier, vậy mà hypoellipticity và cấu trúc Lyapunov truyền tính ngẫu nhiên xuyên hệ, cho ergodicity.

Định lý ấy nói về **tính duy nhất thống kê cho chất lưu 2D ngẫu nhiên**. Bài toán Thiên niên kỷ hỏi liệu nghiệm Navier–Stokes 3D **tất định** có còn trơn mọi thời gian, hay một chuẩn tới hạn có thể nổ. Trích dẫn Fields của Hairer nói về SPDE và cấu trúc chính quy. Đừng viết rằng ông “đã giải Navier–Stokes.”

---

## 5. Gán công lao trung thực

Cấu trúc chính quy nằm trong một mạng:

| Phòng thí nghiệm | Công lao cần giữ trong tầm nhìn |
|------------------|--------------------------------|
| Rough paths | Lyons; sau đó Friz–Victoir, Gubinelli |
| Phép tính paracontrolled | Gubinelli–Imkeller–Perkowski (một đường song song cho một số phương trình) |
| KPZ như vật lý | Kardar, Parisi, Zhang; Bertini–Giacomin; Quastel và nhiều người khác về lớp phổ dụng KPZ |
| Renormalization đại số | Bruned–Hairer–Zambotti và công trình tiếp theo |
| NSE 2D ngẫu nhiên | Hairer–Mattingly; Flandoli, Da Prato–Zabczyk cho bối cảnh SPDE rộng hơn |

**Đừng viết** “Hairer phát minh PDE ngẫu nhiên.” Da Prato, Zabczyk, Walsh và những người khác đã có lý thuyết tuyến tính và nửa tuyến tính. Hairer biến một lớp phương trình kỳ dị **dưới tới hạn** thành một lý thuyết.

---

## 6. Vì sao là Huy chương Fields

Ba lý do đan vào nhau:

1. **Độ khó.** Định nghĩa các tích như $$(\partial_x h)^2$$ khi $$\partial_x h$$ là phân bố đòi hỏi một phép tính địa phương mới, không phải lựa chọn khéo một không gian hàm bên trong thang cổ điển.
2. **Tính trung tâm.** Một khi máy tồn tại, một danh sách phương trình nổi tiếng về vật lý trở thành toán chứ không còn chuỗi hình thức.
3. **Khẩu hiệu trong sáng với phương pháp sâu.** “Khai triển, tái dựng, renormalize” là câu một học viên cao học nhớ được; các ước lượng giải tích và renormalization đại số là cả một thập niên làm việc.

Trong khóa này, Hairer ngồi cạnh các câu chuyện Fields khác tạo ra **ngôn ngữ**—không gian perfectoid, SLE, cấu trúc chính quy—chứ không kết một giả thuyết số duy nhất.

---

## Nhầm lẫn thường gặp

| Khẳng định | Chữa lại |
|------------|----------|
| “Hairer đã giải Navier–Stokes.” | Ông không giải bài toán Thiên niên kỷ 3D tất định. Hairer–Mattingly là ergodicity ngẫu nhiên 2D. |
| “Cấu trúc chính quy thay phép tính Itô.” | Lý thuyết Itô hữu hạn chiều vẫn là đường cơ sở; cấu trúc chính quy xử lý tích không-thời gian kỳ dị. |
| “KPZ không được định nghĩa cho đến 2014.” | Bài KPZ của Hairer là 2013; cấu trúc chính quy (2014) tổng quát hóa phương pháp. Nghiệm Cole–Hopf tồn tại ở một chiều dưới các hạn chế. |
| “$$\Phi^4_3$$ giống triviality 4D.” | $$\Phi^4_3$$ là lý thuyết động lực/kiến tạo 3D; triviality Euclid $$\varphi^4$$ 4D là định lý khác. |
| “Rough paths đã giải mọi SPDE.” | Rough paths xử lý dẫn động thô theo thời gian; tích kỳ dị không-thời gian cần một cỗ máy lớn hơn. |

---

## Bài tập

1. Bằng lời của bạn: vì sao tích của hai phân bố không luôn được định nghĩa? Đưa một khẩu hiệu số mũ Hölder.
2. Một **nâng** rough path thêm gì vào đường $$X$$, và vì sao chuyển động Brown có thể cần một nâng?
3. Viết phương trình KPZ trong một dòng và đánh dấu hạng tử không được định nghĩa cổ điển.
4. Phân biệt “SPDE đặt chỉnh” với “bài toán Thiên niên kỷ NSE tất định” trong một đoạn ngắn.
5. **Luyện độ chính xác.** Tìm một câu phổ thông nói Hairer “thuần hóa mọi phương trình ồn.” Viết lại thành hai câu chính xác.
6. **Kéo giãn seminar.** So sánh cấu trúc chính quy với [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase/) về $$\varphi^4$$: một bên xây động lực 3D; một bên chứng minh giới hạn scale 4D là Gaussian. Các khẩu hiệu khớp nhau thế nào mà không mâu thuẫn?

---

## Nguồn video và đọc thêm

1. **Trích dẫn IMU** — trích dẫn ngắn Fields Medallists 2014: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014/fields-medallists-2014-awardees-brief-citations).
2. **Định hướng** — chân dung Quanta: [In Noisy Equations, One Who Heard Music](https://www.quantamagazine.org/in-noisy-equations-one-who-heard-music-20140812/).
3. **Meta** — trang Huy chương Fields 2014 của IMU: [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014).

**Nhắc trạng thái:** Một lý thuyết SPDE kỳ dị—**không** phải nghiệm Navier–Stokes 3D tất định.

---

## Tài liệu tham khảo

1. Trích dẫn Huy chương Fields 2014 của IMU — Martin Hairer (mathunion.org).
2. **M. Hairer** — A theory of regularity structures (Invent. Math., 2014); Solving the KPZ equation (Ann. of Math., 2013).
3. **T. Lyons** — lý thuyết rough path (thập niên 1990); các tổng quan của Friz–Hairer.
4. **M. Hairer và J. C. Mattingly** — Ergodicity của phương trình Navier–Stokes 2D với lực ngẫu nhiên thoái hóa (Ann. of Math., 2006).
5. Láng giềng khóa học: [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase/) cho $$\varphi^4$$ ở một chiều khác; Navier–Stokes Chương 1 cho phát biểu Thiên niên kỷ mà người ta **không** được trộn.

---

## Hướng đi tiếp

- Đọc các mục đầu bài cấu trúc chính quy của Hairer và liệt kê các đối tượng: mô hình, phân bố được mô hình hóa, tái dựng.
- So sánh Cole–Hopf cho KPZ một chiều với xây dựng cấu trúc chính quy: mỗi phương pháp thấy gì?
- Tùy chọn seminar A3: một trang về phép tính paracontrolled đối lập cấu trúc chính quy—mà không tuyên bố bên nào lỗi thời.
