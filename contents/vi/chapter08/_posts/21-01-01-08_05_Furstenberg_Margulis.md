---
layout: post
title: "Furstenberg & Margulis: Động lực, Ergodic, Rigidity (Abel 2020)"
chapter: '08'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter08
lesson_type: required
---

**Giải Abel 2020** được trao chung cho **Hillel Furstenberg** (Đại học Hebrew Jerusalem) và **Gregory Margulis** (Yale)

> “for pioneering the use of methods from probability and dynamics in group theory, number theory and combinatorics.”  
> — [Citation của ủy ban Abel](https://abelprize.no/abel-prize-laureates/2020)

Bài này giải thích citation đó nói gì: **lý thuyết ergodic** và **động lực thuần nhất** đã trở thành động cơ cho số học và tổ hợp như thế nào; hiện tượng tái hồi nhiều lần theo kiểu Furstenberg cho ta biết gì về cấu trúc của các tập lớn; **tính siêu cứng (superrigidity)** và **tính số học (arithmeticity)** kiểu Margulis cho ta biết gì về các nhóm rời rạc; và vì sao việc ghép hai sự nghiệp trong cùng một năm của giải Abel gửi đi một thông điệp văn hóa. Tài liệu: [abelprize.no](https://abelprize.no/).

---

## Mục tiêu học tập

Định nghĩa lý thuyết ergodic như việc lấy trung bình theo quỹ đạo với một độ đo bất biến; nêu một chủ đề của Furstenberg (tái hồi nhiều lần / cấu trúc của các tập số nguyên có mật độ dương); nêu một chủ đề của Margulis (siêu cứng / tính số học / động lực thuần nhất); giải thích động lực học như một **công cụ** cho số học và tổ hợp, chứ không chỉ là chuyện hỗn độn; và nối cách nhìn này với [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) mà không khẳng định hai phương pháp giống hệt nhau.

**Kiến thức nền.** Nhóm tác động lên không gian; xác suất cơ bản (trung bình, độ đo); tập con của các số nguyên.

---

## 1. Một cuộc cách mạng chung

Lý thuyết số cổ điển thường đếm và ước lượng: điểm nguyên của lưới, số nguyên tố trong cấp số cộng, giá trị của dạng toàn phương. Furstenberg và Margulis chỉ ra rằng nhiều bài toán trở nên trong suốt, hoặc ít nhất tiếp cận được theo cách mới, khi viết lại thành **bài toán về quỹ đạo** của một nhóm tác động lên một không gian, trong đó một **độ đo bất biến** kiểm soát hành vi tiệm cận.

Thông điệp chung vừa mang tính kỹ thuật vừa mang tính văn hóa:

> Xác suất và động lực học là **toán thuần túy cốt lõi**, không chỉ là phụ lục ứng dụng.

Thông điệp đó nay đã thấm vào lý thuyết số giải tích, lý thuyết nhóm hình học và một phần của tổ hợp. Giải Abel 2020 vinh danh những người đi đầu trong cuộc di cư ấy.

---

## 2. Lý thuyết ergodic trong một trang

Một **hệ động lực** bảo toàn độ đo gồm: không gian $$X$$, một độ đo xác suất $$\mu$$, một phép biến đổi $$T:X\to X$$ (hoặc một nhóm các phép biến đổi) bảo toàn $$\mu$$. **Quỹ đạo** của $$x$$ là:

$$
\{ x,\, Tx,\, T^2x,\, T^3x,\, \dots \}.
$$

**Định lý ergodic** nối trung bình theo thời gian dọc quỹ đạo với trung bình trong không gian theo $$\mu$$. Nếu hệ là ergodic (không phân rã được), thì “hầu hết các quỹ đạo đều đi khắp không gian” theo nghĩa trung bình:

$$
\lim_{N\to\infty}\frac{1}{N}\sum_{k=0}^{N-1} f(T^k x) = \int_X f\, d\mu
$$

với $$f$$ khả tích, đúng với hầu hết $$x$$ theo $$\mu$$.

Vì sao lý thuyết số quan tâm đến điều này? Nhiều cấu hình số học có thể mã hóa thành việc quỹ đạo ghé thăm một vùng nào đó; các định lý tái hồi buộc những mẫu hình tổ hợp phải xuất hiện.

---

## 3. Furstenberg: tái hồi, cấu trúc và biên

### Tái hồi nhiều lần và cấu trúc kiểu Szemerédi

Định lý Szemerédi: mọi tập con của các số nguyên có mật độ trên dương đều chứa các cấp số cộng dài hữu hạn tùy ý. Furstenberg đã đưa ra một chứng minh ergodic bằng cách dịch mật độ và cấp số cộng thành **tái hồi nhiều lần**: với một hệ bảo toàn độ đo và một tập $$A$$ có độ đo dương, tồn tại một thời điểm quay lại $$n$$ sao cho

$$
\mu\big(A \cap T^{-n}A \cap T^{-2n}A \cap \cdots \cap T^{-(k-1)n}A\big) > 0
$$

dưới giả thiết thích hợp. Điều này bắt được một cấp số cộng $$k$$ số hạng bằng ngôn ngữ động lực.

Ý tưởng sâu xa: **sự tái hồi của quỹ đạo mã hóa các cấu hình tổ hợp**. Định lý cấu trúc của hệ động lực trở thành định lý cấu trúc của các tập số nguyên lớn.

### Ứng dụng số học và biên

Furstenberg phát triển lý thuyết cấu trúc và các ứng dụng nối hệ động lực với lý thuyết số và tổ hợp. Lý thuyết biên của bước đi ngẫu nhiên và của các tác động nhóm là một chủ đề lớn khác của ông.

Phong cách chung: biến một câu hỏi rời rạc khó thành một câu hỏi liên tục có độ đo, rồi thu hoạch tính cứng hoặc tính tái hồi.

---

## 4. Margulis: tính cứng, tính số học, động lực thuần nhất

### Siêu cứng

Định lý **siêu cứng** (Margulis và các kết quả liên quan): các đồng cấu từ một lattice hạng cao vào một nhóm đại số bị ràng buộc rất chặt, về bản chất có nguồn gốc đại số. Trực giác: hình học hạng cao buộc các ánh xạ phải mang tính đại số, không thể hoang dại.

### Tính số học

Các kết quả về **tính số học**: một số nhóm con rời rạc của nhóm Lie nửa đơn bắt buộc phải xuất phát từ các nhóm đại số trên trường số. Hình học rời rạc bị buộc phải mang tính số học.

### Động lực thuần nhất

**Không gian thuần nhất** là thương $$G/\Gamma$$ của một nhóm Lie $$G$$ cho một nhóm con rời rạc $$\Gamma$$. Các dòng trên không gian đó, đặc biệt là dòng unipotent, có bao đóng quỹ đạo rất cứng (lý thuyết Ratner nằm gần đó). Các ý tưởng kiểu Margulis khai thác tính cứng này để ràng buộc các tập số học: giá trị của các dạng, bao đóng quỹ đạo, phân bố đều.

Câu chuyện nổi tiếng ở gần đó là **giả thuyết Oppenheim** về giá trị của các dạng toàn phương không xác định, được tiếp cận bằng động lực (chứng minh của Margulis). Khẩu hiệu: xấp xỉ Diophantine và giá trị của dạng trở thành các câu hỏi về bao đóng quỹ đạo.

### Expander và giao diện giữa toán thuần túy và khoa học máy tính

Margulis cũng dựng ra các **đồ thị expander** tường minh bằng phương pháp nhóm: đồ thị thưa nhưng giãn rất mạnh, trung tâm của khoa học máy tính, lý thuyết mã và toán thuần túy. Giải Abel 2020 chạm đến vùng giáp ranh giữa toán thuần túy và khoa học máy tính, mà giải Abel 2021 (Lovász–Wigderson) sẽ vinh danh từ góc nhìn rời rạc và khoa học máy tính lý thuyết.

---

## 5. Khẩu hiệu của động lực thuần nhất (bản đồ sâu hơn)

Các dòng unipotent trên không gian thuần nhất thường có bao đóng quỹ đạo **cứng**: bao đóng tự nó là thuần nhất, không hỗn độn kiểu fractal. Tính cứng đó là món quà cho lý thuyết số. Thay vì ước lượng sai số bằng tay cho từng bài, đôi khi ta chỉ cần nhận ra hệ động lực mà bao đóng quỹ đạo của nó phân loại các khả năng số học.

Furstenberg và Margulis không dùng cùng một cỗ máy. Furstenberg nghiêng về cấu trúc và tái hồi trong các hệ bảo toàn độ đo trừu tượng (thu được kết quả tổ hợp). Margulis nghiêng về nhóm đại số, lattice và không gian thuần nhất (thu được kết quả số học và hình học). Giải Abel ghép hai người vì cả hai đều làm cho **động lực học trở thành một ngôn ngữ của toán thuần túy**.

---

## 6. Vì sao Abel ghép hai người

Phong cách khác nhau, thông điệp như nhau. Sau Furstenberg và Margulis, nhà lý thuyết số nói rằng độ đo bất biến là chuyện bình thường; nhà tổ hợp trích dẫn các chứng minh ergodic; nhà hình học nhóm rời rạc sống trong động lực thuần nhất. Xác suất không còn “chỉ là ứng dụng”; động lực học không còn “chỉ là những hình ảnh hỗn độn”.

So với [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/): các cấp số cộng trong số nguyên tố dùng ý tưởng của tổ hợp cộng tính và văn hóa gần với ergodic, trong câu chuyện Fields ở chương 02. Giải Abel 2020 nói về những người đi tiên phong đã đưa cuộc di cư đó lên thành quy mô lớn.

---

## 7. Những nhầm lẫn

| Khẳng định | Chỉnh lại |
|------------|-----------|
| “Ergodic chỉ là vật lý hay thống kê.” | Đó là lý thuyết toán thuần túy về hệ bảo toàn độ đo, có ứng dụng số học. |
| “Furstenberg chứng minh Szemerédi trước.” | Chứng minh tổ hợp của Szemerédi có trước; Furstenberg đưa ra chứng minh ergodic mang tính nền tảng. |
| “Tính cứng nghĩa là không có gì chuyển động.” | Các ánh xạ và quỹ đạo bị ràng buộc mạnh, thường là theo kiểu đại số, chứ không tùy ý. |
| “Expander chỉ dành cho khoa học máy tính.” | Chúng cũng là trung tâm của toán thuần túy (nhóm, hình học, phổ của đồ thị). |
| “Động lực học giải quyết xong lý thuyết số.” | Là bộ công cụ mạnh cho *một số* bài toán; nhiều bài còn nằm ngoài tầm với. |

---

## Bài tập

1. Tìm một ẩn dụ đời thường cho trung bình theo quỹ đạo.  
2. Vì sao mật độ dương của một tập số nguyên có thể liên quan đến tái hồi? Không quá 120 từ.  
3. So với [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/): một điểm giống và một điểm khác.  
4. **Không quá 200 từ:** “tính cứng” gợi lên điều gì trong thế giới của Margulis?  
5. Nêu một tác động của Margulis ở gần khoa học máy tính (expander) và một tác động số học.  
6. Đọc tài liệu về Abel 2020 trên [abelprize.no](https://abelprize.no/); trích ra ba danh từ chỉ đối tượng toán học.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh.

**Những ý chính từ phần nghiên cứu**

- Abel 2020: động lực và xác suất → số học và tổ hợp.
- Tái hồi của Furstenberg; siêu cứng, expander và giả thuyết Oppenheim của Margulis.

**Thứ tự xem gợi ý**

1. **Cốt lõi**: các bài giảng Abel 2020 của Furstenberg và Margulis: [https://www.youtube.com/watch?v=2i5UJwKN7os](https://www.youtube.com/watch?v=2i5UJwKN7os).  
2. **Lịch sử**: phỏng vấn Furstenberg của giải Abel: [https://www.youtube.com/watch?v=01IdfSRYawE](https://www.youtube.com/watch?v=01IdfSRYawE).  
3. **Lịch sử**: phỏng vấn Margulis của giải Abel: [https://www.youtube.com/watch?v=FInTu9-MHHU](https://www.youtube.com/watch?v=FInTu9-MHHU).  
4. **Định hướng**: phần trình bày phổ thông về công trình 2020 (đoạn của Bellos): [https://www.youtube.com/watch?v=Fqdl_jyw8OE](https://www.youtube.com/watch?v=Fqdl_jyw8OE).  
5. **Liên quan**: Margulis nói về entropy Kolmogorov–Sinai (tuần Abel trước đó): [https://www.youtube.com/watch?v=cuYO5NQieRA](https://www.youtube.com/watch?v=cuYO5NQieRA).  

**Cổng chính thức và tài liệu**

- Abel 2020 Furstenberg & Margulis: https://abelprize.no/abel-prize-laureates/2020  

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/furstenberg-margulis_2i5UJwKN7os_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu

### Danh mục nguồn

1. Abel 2020 Furstenberg & Margulis — https://abelprize.no/abel-prize-laureates/2020  
2. Abel lectures 2020 Furstenberg & Margulis — https://www.youtube.com/watch?v=2i5UJwKN7os  
3. Abel interview Furstenberg — https://www.youtube.com/watch?v=01IdfSRYawE  
4. Abel interview Margulis — https://www.youtube.com/watch?v=FInTu9-MHHU  
5. Popular presentation of 2020 work (Bellos clip) — https://www.youtube.com/watch?v=Fqdl_jyw8OE  
6. Margulis on Kolmogorov–Sinai entropy (earlier Abel week) — https://www.youtube.com/watch?v=cuYO5NQieRA  
7. NYT Abel 2020 — https://www.nytimes.com/2020/03/18/science/abel-prize-mathematics.html  
8. Nature Abel 2020 — https://www.nature.com/articles/d41586-020-00799-7  
9. Wikipedia — Hillel Furstenberg — https://en.wikipedia.org/wiki/Hillel_Furstenberg  
10. Wikipedia — Grigory Margulis — https://en.wikipedia.org/wiki/Grigory_Margulis  

1. [Abel 2020](https://abelprize.no/abel-prize-laureates/2020).  
2. Bài trình bày về động lực thuần nhất; bài khảo sát về tái hồi nhiều lần của Furstenberg.  
3. Szemerédi: văn liệu tổ hợp và văn liệu ergodic chạy song song.  
4. Trong khóa: Green–Tao; sau đó là Lovász–Wigderson.

---

## Hướng đi tiếp

- Cây cầu tổ hợp cộng tính không cần toàn bộ ergodic: “động lực học phát hiện các mẫu hình”.  
- Đọc một bài phổ thông về Oppenheim qua động lực học.  
- So tính cứng ở đây với tính cứng của Sullivan (không có miền lang thang).  
- So với [Fields]({{ site.baseurl }}/contents/vi/chapter02/02_00_Tong_quan/).  
- Tiếp theo: [Lovász & Wigderson]({{ site.baseurl }}/contents/vi/chapter08/08_06_Lovasz_Wigderson/).

## Xác suất và đối xứng trên không gian thuần nhất

Furstenberg–Margulis (Abel 2020) tôn vinh sự giao thoa giữa **lý thuyết ergodic, nhóm Lie và các ứng dụng số học và hình học**. Khẩu hiệu cho seminar: biến một câu hỏi số học hay hình học thành động lực học của một tác động nhóm, rồi khai thác các bất biến và độ đo.

## Đừng đồng nhất “ngẫu nhiên” với “không có cấu trúc”

Lý thuyết ergodic nói về trung bình theo thời gian hoặc theo không gian của các hệ động lực, thường là những cấu trúc rất cứng. Đó không phải là chuyện “toán học trở nên mơ hồ”.

## Studio

Viết 200 từ phân biệt: (a) dãy ngẫu nhiên theo nghĩa thuật toán, (b) quỹ đạo ergodic, (c) định lý mật độ kiểu Szemerédi (nếu đã học Green–Tao). Nêu một chỗ dễ nhầm thuật ngữ giữa ba thế giới đó.

## Video tham khảo

- **Xem trước** — [The Abel lectures: Hillel Furstenberg and Gregory Margulis](https://www.youtube.com/watch?v=2i5UJwKN7os) — The Abel Prize, tiếng Anh. Xem trước để nghe chính hai laureate trình bày công trình của mình.
- [Hillel Furstenberg - The Abel Prize interview 2020](https://www.youtube.com/watch?v=01IdfSRYawE) — The Abel Prize, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để nghe Furstenberg kể về con đường làm toán.
- [Gregory Margulis - The Abel Prize interview 2020](https://www.youtube.com/watch?v=FInTu9-MHHU) — The Abel Prize, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, qua cuộc phỏng vấn Margulis.
