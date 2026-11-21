---
layout: post
title: "Karen Uhlenbeck: Phân tích Hình học và Gauge Theory (Abel 2019)"
chapter: '08'
order: 4
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

**Karen Keskulla Uhlenbeck** nhận **Giải Abel 2019**

> “for her pioneering achievements in geometric partial differential equations, gauge theory and integrable systems, and for the fundamental impact of her work on analysis, geometry and mathematical physics.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2019)

Bà là **nữ** laureate đầu tiên của giải Abel. Bài này giải thích vì sao lý thuyết gauge cần giải tích nặng; ở mức ý tưởng, tính compact, hiện tượng “bong bóng” (bubbling) và các kỳ dị khử được có nghĩa là gì; và một đời làm hạ tầng cho PDE hình học có thể định hình tôpô và vật lý toán như thế nào. Tài liệu: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Sau bài này, bạn có thể giải thích các đối tượng gauge (liên thông, độ cong, phân thớ) ở mức khẩu hiệu; mô tả vì sao **tính compact, bubbling và kỳ dị khử được** quan trọng với PDE hình học; đặt Uhlenbeck vào vị trí hạ tầng giải tích cho tôpô gauge (Donaldson và các thế hệ sau); nối văn hóa của giải tích hình học với mặt cực tiểu và các dòng hình học; và phân biệt “cảm hứng từ vật lý” với “định lý toán học về không gian moduli”.

**Kiến thức nền.** Giải tích nhiều biến; ý niệm về đa tạp và mặt. Đại số tuyến tính giúp hiểu “liên thông gần như là cách lấy đạo hàm trường vector”. Không cần đã học lý thuyết gauge. Liên kết: [mặt cực tiểu]({{ site.baseurl }}/contents/vi/chapter04/04_09_Minimal_Surfaces/), [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

---

## 1. Lý thuyết gauge như hình học

Trong vật lý, trường gauge mô tả các lực: điện từ là gauge abel; tương tác yếu và mạnh liên quan đến **Yang–Mills** không abel. Trong toán học, ta có một **phân thớ** chính hoặc phân thớ vector trên đa tạp $$M$$. Một **liên thông** $$A$$ là quy tắc lấy đạo hàm các tiết diện, nó vận chuyển bậc tự do “nội tại” dọc theo các đường trong $$M$$. **Độ cong** $$F_A$$ đo việc các đạo hàm riêng hỗn hợp không giao hoán với nhau; công thức địa phương có dạng

$$
F_A = dA + A\wedge A
$$

trong ngôn ngữ các dạng vi phân có giá trị trong đại số Lie.

**Phiếm hàm Yang–Mills** là năng lượng của độ cong,

$$
\mathrm{YM}(A) = \int_M \lvert F_A\rvert^2\, d\mathrm{vol},
$$

và các điểm tới hạn của nó là các **liên thông Yang–Mills**. Instanton và những nghiệm đặc biệt liên quan, ở chiều 4, trở thành trung tâm của tôpô.

Để lấy được tôpô từ **không gian moduli** của các liên thông (Donaldson và những người khác), cần có các định lý giải tích: sự tồn tại, tính compact, tính chính quy, kiểm soát kỳ dị. Lớp kết quả đó thuộc giải tích hình học. Nếu thiếu nó, hình thức luận của vật lý hay tôpô đại số không thể trở thành định lý về các 4-đa tạp trơn. Điều nên nhớ trong seminar: citation của Abel nói “fundamental impact”, nghĩa là đây là giải ghi nhận hạ tầng, không chỉ một bổ đề đẹp.

---

## 2. Vì sao giải tích là nút thắt

Không gian vô hạn chiều của các liên thông, lấy thương theo gauge, không compact theo tô-pô ngây thơ. Một dãy các liên thông có năng lượng Yang–Mills bị chặn có thể:

- hội tụ trơn trên một vùng lớn;  
- **tập trung năng lượng** tại một điểm (hoặc một tập có chiều thấp hơn);  
- tạo “bong bóng” (bubble): một nghiệm không tầm thường trên mô hình $$S^4$$ hay $$\mathbb{R}^4$$ sau khi đổi tỉ lệ.

Nếu không kiểm soát được hiện tượng đó thì không gian moduli không dùng được: không đếm được, không compact hóa được, không nối được các lớp đặc trưng với giao điểm. Tôpô cần các ước lượng.

Cùng một họ triết lý với bubbling của ánh xạ điều hòa, kỳ dị của các dòng hình học, và tính compact tập trung trong PDE biến phân; chúng là anh em chứ không phải bản sao của nhau. Ước lượng trước, phân loại sau: đó là khẩu hiệu văn hóa của giải tích hình học.

---

## 3. Những đột phá giải tích gắn với Uhlenbeck

### Tính compact của Uhlenbeck

Một dãy liên thông Yang–Mills với năng lượng bị chặn, sau khi chọn gauge, có một dãy con hội tụ trơn ngoài hữu hạn điểm (trong thiết lập tới hạn ở chiều 4), trong khi năng lượng có thể tập trung tại các điểm đó. Việc compact hóa bao gồm cả “cây bong bóng”. Đây là nền tảng của không gian moduli trong tôpô gauge.

### Kỳ dị khử được và tính chính quy epsilon

**Chính quy epsilon:** nếu năng lượng trong một quả cầu đủ nhỏ thì liên thông là chính quy (sau khi chọn gauge) với ước lượng định lượng. Do đó kỳ dị không thể tùy tiện; năng lượng nhỏ cấm những hành vi hoang dại. **Kỳ dị khử được:** một kỳ dị cô lập có thể được lấp lại nếu năng lượng bị chặn. Đó là niềm tin giải tích rằng một “lỗ” không bí ẩn vô điều kiện.

### Mẫu hình ngoài Yang–Mills

Các kỹ thuật này lan sang ánh xạ điều hòa, Yang–Mills–Higgs và các PDE hình học khác. Văn hóa **tập trung năng lượng, phóng đại tại điểm kỳ dị và phân loại các bong bóng** đã trở thành ngôn ngữ chuẩn ở bậc cao học.

### Hệ khả tích và giải tích hình học rộng hơn

Citation của Abel còn nêu các hệ khả tích và tác động rộng lên giải tích, hình học, vật lý toán. Sự nghiệp của Uhlenbeck là cả một danh mục khiến PDE hình học trở thành xa lộ nối toán thuần túy với hình học lấy cảm hứng từ vật lý, chứ không chỉ một bổ đề.

---

## 4. Tập trung năng lượng: bản đồ sâu hơn

Nhiều PDE hình học cực tiểu hóa hay tìm điểm tới hạn của một năng lượng (năng lượng Dirichlet cho ánh xạ, Yang–Mills cho liên thông). Khi năng lượng tập trung lại, có thể hình thành **bong bóng**: nghiệm có năng lượng hữu hạn trên không gian mô hình. Kiểm soát được bong bóng là trái tim của việc compact hóa không gian moduli.

Các ước lượng kiểu Uhlenbeck cho ngưỡng định lượng: dưới một mức năng lượng nhất định, sự tập trung không thể giấu một bong bóng; còn trên ngưỡng thì phải kể bong bóng một cách tường minh. Bức tranh này mang tính hình học, không chỉ là giải tích hàm: “điểm ở vô cùng” của không gian moduli có ý nghĩa hình học.

So sánh (cẩn thận) với kỳ dị của Navier–Stokes hay của dòng Ricci: phương trình khác nhau, nhưng **triết lý phân tích theo thang**, tức phóng to nơi mật độ năng lượng hay độ cong bùng nổ, có sự tương đồng.

---

## 5. Vì sao đáng một giải Abel

Một phép tính khéo léo không tạo nên một lĩnh vực. Uhlenbeck làm cho PDE hình học vô hạn chiều trở nên **dùng được** cho tôpô và vật lý. Các thế hệ sau xây dựng Donaldson–Thomas, Seiberg–Witten (một động cơ gauge khác, giải tích êm hơn), và các dòng hình học trên cảnh quan được ổn định nhờ tính compact và tính chính quy của trường phái này.

Giải Abel 2019 là giải **ghi nhận hạ tầng** đúng nghĩa: cụm “fundamental impact” là điểm chính. Việc bà là nữ laureate đầu tiên có ý nghĩa lịch sử; toán học đứng vững trên giá trị giải tích độc lập với cột mốc đó, và cột mốc ấy vẫn quan trọng đối với văn hóa của ngành. Đừng rút gọn citation thành “giải của sự đa dạng” hay thành “chỉ là vật lý hạt”.

---

## 6. Cố định gauge, moduli và “không gian nghiệm”

Liên thông chỉ được xác định modulo **phép biến đổi gauge**: đổi tầm thường hóa địa phương làm $$A$$ được viết lại mà không đổi nội dung hình học hay vật lý. Đối tượng thật sự thường là **không gian moduli**

$$
\mathcal{M} = \{\text{Yang–Mills connections}\}/\text{gauge}.
$$

Thương vô hạn chiều này nguy hiểm về mặt giải tích: phải chọn đại diện cẩn thận (gauge Coulomb và các họ hàng), rồi các ước lượng elliptic khôi phục sự kiểm soát cục bộ. Các định lý cố định gauge và tính compact kiểu Uhlenbeck chính là công cụ biến thương hình thức thành thứ mà nhà hình học compact hóa và sử dụng được.

Ở chiều 4, các liên thông phản tự đối ngẫu (instanton) tạo ra không gian moduli mà chiều và tôpô của nó mã hóa cấu trúc trơn trên các 4-đa tạp. Ứng dụng mang tính cách mạng của Donaldson dựa trên nền giải tích ấy. Seiberg–Witten sau này đưa vào một động cơ khác, nhưng điểm lịch sử vẫn là: **nếu không có tính compact và các kỳ dị khử được thì chương trình moduli không khởi động được**.

---

## 7. Vị trí trong khóa học

- [Mặt cực tiểu]({{ site.baseurl }}/contents/vi/chapter04/04_09_Minimal_Surfaces/): năng lượng, tính chính quy, các kết luận hình học rút ra từ PDE.  
- [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/): nơi trường gauge quay lại với tư cách vật lý.  
- [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/): PDE hình học chinh phục tôpô bằng một con đường khác (dòng Ricci có phẫu thuật).  
- Lý thuyết gauge và tôpô của các 4-đa tạp là câu chuyện song song “PDE → tôpô”, đối với “PDE → hình học hóa” của dòng Ricci.

Một so sánh hữu ích cho seminar: dòng Ricci biến dạng *metric*; Yang–Mills nghiên cứu *liên thông* tới hạn. Cả hai đều là chương trình PDE hình học lấy tôpô từ giải tích. Phương trình, phép đổi tỉ lệ và mô hình kỳ dị khác nhau, nhưng bài học văn hóa giống nhau: **ước lượng trước, phân loại sau**.

---

## 8. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “Gauge chỉ là vật lý hạt.” | Trong toán thuần túy: hình học của liên thông và không gian moduli, với ứng dụng cho tôpô. |
| “Compact nghĩa là mọi dãy đều hội tụ.” | Hội tụ của một dãy con sau khi chọn gauge, thường ngoài một tập kỳ dị, có thể kèm bong bóng. |
| “Uhlenbeck chứng minh định lý Donaldson.” | Donaldson dùng không gian moduli gauge cho tôpô; phân tích kiểu Uhlenbeck là hạ tầng. |
| “Kỳ dị khử được nghĩa là không có gì xấu.” | Có thể gỡ kỳ dị *dưới giả thiết* (năng lượng bị chặn). |
| “Giải Abel 2019 chỉ là giải của sự đa dạng.” | Citation nói về toán học của PDE hình học và gauge; cột mốc lịch sử chỉ là sự kiện thêm vào. |

---

## Bài tập

1. Liên thông và độ cong: mỗi khái niệm một câu (không công thức cũng được).  
2. “Bubbling” là gì đối với PDE hình học tới hạn năng lượng? Hai câu.  
3. Vì sao tôpô cần giải tích trong lý thuyết gauge? Không quá 150 từ.  
4. **Không quá 250 từ:** so sánh giải ghi nhận hạ tầng (phân tích của Uhlenbeck) với bản anh hùng ca về một định lý (ví dụ một bài toán Millennium).  
5. Nêu ba từ chung giữa PDE hình học và mặt cực tiểu; và một từ đặc trưng hơn cho gauge (liên thông, độ cong, cố định gauge).  
6. Lướt qua tài liệu về Abel 2019 trên [abelprize.no](https://abelprize.no/); liệt kê ba từ khóa định lý mới đối với bạn.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2019: Uhlenbeck, PDE hình học, gauge, bubbling và kỳ dị.
- Nữ laureate đầu tiên; hạ tầng giải tích cho tôpô gauge.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: bài giảng Abel của Uhlenbeck về Phép tính biến phân: [https://www.youtube.com/watch?v=1WepO8tFGto](https://www.youtube.com/watch?v=1WepO8tFGto).  
2. **Cốt lõi**: Bryant, về bong bóng và kỳ dị (nói về công trình của Uhlenbeck): [https://www.youtube.com/watch?v=EZNpi8H6q1Q](https://www.youtube.com/watch?v=EZNpi8H6q1Q).  
3. **Định hướng**: phỏng vấn Uhlenbeck của giải Abel: [https://www.youtube.com/watch?v=0fOaetX4eHM](https://www.youtube.com/watch?v=0fOaetX4eHM).  
4. **Định hướng**: phỏng vấn trực tiếp Uhlenbeck: [https://www.youtube.com/watch?v=mmWdPPwSi64](https://www.youtube.com/watch?v=mmWdPPwSi64).  
5. **Lịch sử**: buổi công bố giải Abel 2019: [https://www.youtube.com/watch?v=arrl_nM0T4s](https://www.youtube.com/watch?v=arrl_nM0T4s).  

**Cổng chính thức và tài liệu**

- Abel 2019 Uhlenbeck: https://abelprize.no/abel-prize-laureates/2019  

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/uhlenbeck-gauge_1WepO8tFGto_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu

### Danh mục nguồn

1. Abel 2019 Uhlenbeck — https://abelprize.no/abel-prize-laureates/2019  
2. Uhlenbeck Abel lecture — Calculus of Variations — https://www.youtube.com/watch?v=1WepO8tFGto  
3. Bryant — Bubbles & singularities (on Uhlenbeck) — https://www.youtube.com/watch?v=EZNpi8H6q1Q  
4. Abel Prize Interview Uhlenbeck — https://www.youtube.com/watch?v=0fOaetX4eHM  
5. Live interview Uhlenbeck — https://www.youtube.com/watch?v=mmWdPPwSi64  
6. Abel announcement 2019 — https://www.youtube.com/watch?v=arrl_nM0T4s  
7. Quanta — Uhlenbeck Abel — https://www.quantamagazine.org/karen-uhlenbeck-uniter-of-geometry-and-analysis-wins-abel-prize-20190319/  
8. Celebratio Mathematica — Uhlenbeck — https://celebratio.org/Uhlenbeck_K/cover/472/  
9. AMS Notices survey (Donaldson on Uhlenbeck PDF) — https://www.ams.org/journals/notices/201903/rnoti-p303.pdf  
10. Wikipedia — Karen Uhlenbeck — https://en.wikipedia.org/wiki/Karen_Uhlenbeck  

1. [Abel 2019](https://abelprize.no/abel-prize-laureates/2019).  
2. Bài khảo sát về giải tích của Yang–Mills và tính compact của Uhlenbeck.  
3. Nhập môn tôpô gauge (Donaldson–Kronheimer, …) để lấy ngữ cảnh, không phải là điều kiện tiên quyết đầy đủ.  
4. Liên kết trong khóa: mặt cực tiểu; vật lý toán; Perelman.

---

## Hướng đi tiếp

- So sánh ngôn ngữ về bubbling với kỳ dị của Navier–Stokes (phương trình khác, triết lý thang đo tương tự).  
- Trong seminar: phê bình những bài phổ thông chỉ gán gauge cho vật lý hạt.  
- Ghi lại một thách thức giải tích còn mở trong PDE hình học mà bạn quan tâm (gauge ở chiều cao hơn, mô hình kỳ dị, …).  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp theo: [Furstenberg & Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/).

## Video tham khảo

- **Xem trước** — [Karen Uhlenbeck: Some Thoughts on the Calculus of Variations](https://www.youtube.com/watch?v=1WepO8tFGto) — The Abel Prize, tiếng Anh. Xem trước để nghe chính Uhlenbeck nói về phép tính biến phân, nền tảng cho phần còn lại của bài.
- [Robert Bryant: Limits, Bubbles, and Singularities: The fundamental ideas of Karen Uhlenbeck](https://www.youtube.com/watch?v=EZNpi8H6q1Q) — The Abel Prize, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để thấy giới hạn, bong bóng và kỳ dị được giải thích có hệ thống.
- [Karen Uhlenbeck - The Abel Prize interview 2019](https://www.youtube.com/watch?v=0fOaetX4eHM) — The Abel Prize, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, qua cuộc phỏng vấn về con đường làm toán của bà.
