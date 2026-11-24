---
layout: post
title: "Studio khám phá: Lặp và ánh xạ Collatz"
chapter: '07'
order: 9
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
---

Hãy chọn một số nguyên dương bất kỳ. Nếu nó chẵn, hãy chia đôi; nếu nó lẻ, hãy nhân 3 rồi cộng 1. Lặp lại đúng hai dòng quy tắc học sinh tiểu học ấy mãi mãi. Thử với số $$6$$: $$6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$$ — chỉ mất 8 bước là rơi gọn về $$1$$. Nhưng hãy thử với số $$27$$: thay vì giảm ngay, nó nhảy vọt như tàu lượn siêu tốc lên tới tận **9.232** và mất **111 bước** mới chịu đáp xuống $$1$$! Gần một thế kỷ qua, hàng loạt bộ óc lớn đã thử sức và Paul Erdős từng thốt lên: *"Toán học vẫn chưa sẵn sàng cho những bài toán kiểu này."*

Chào mừng bạn đến với **bài thực hành chính** của Chương 7. Nhiệm vụ của bạn **không phải** là chứng minh giả thuyết Collatz. Thay vào đó, bạn sẽ bước vào xưởng thực nghiệm với một câu hỏi mở lớn: *Điều gì xảy ra khi ta lặp đi lặp lại một quy tắc tất định đơn giản?* Bạn sẽ **thiết kế thí nghiệm**, **viết nhật ký nghiên cứu có ngày tháng**, và **báo cáo trung thực** tất cả những gì mình khám phá được — kể cả những giả thuyết bị bác bỏ, những lần tràn số hay lỗi mã nguồn, và những ranh giới mà máy tính mạnh nhất cũng không thể vượt qua.

**Bài liên quan.** [Collatz (Chương 1)]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/) · [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/) · [Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) (kiểm tra bằng máy tính khác với chứng minh).

---

## Mục tiêu học tập

- Phát biểu chính xác quy tắc **Collatz ($$3n+1$$)** và giả thuyết Collatz.
- Định nghĩa và tính **thời gian dừng toàn phần** (hoặc một biến thể được ghi rõ: số bước để về 1, số bước để xuống dưới giá trị ban đầu, v.v.).
- Thiết kế ít nhất 2 thí nghiệm với các tham số cố định từ trước (phạm vi của $$n$$, đại lượng thống kê, loại đồ thị).
- Ghi **nhật ký có ngày tháng** gồm giả thuyết, kết quả, điều bất ngờ, và nhãn phân loại (định lý / giả thuyết / quan sát / lập luận gần đúng).
- Viết một báo cáo ngắn, phân biệt rõ **định lý**, **giả thuyết**, **quan sát bằng số** và **phỏng đoán**.
- Giải thích vì sao kiểm tra bằng máy tính đến những số rất lớn vẫn không phải là chứng minh (Collatz và giả thuyết Riemann giống nhau ở điểm này).
- Áp dụng cùng phương pháp cho một đề thực hành khác của Chương 7 nếu đổi đề (cần giảng viên đồng ý).

**Kiến thức cần có.** Số nguyên, phép chia lấy dư, viết chương trình ngắn hoặc dùng phần mềm tính toán, vẽ đồ thị.

---

## Bản đồ kiến thức nền: Hệ động lực rời rạc và Lý thuyết số thực nghiệm là gì, nghiên cứu những gì?

Tại sao một phép toán chỉ dùng phép nhân 3, cộng 1 và chia 2 lại thách thức cả nền toán học hiện đại? Bởi vì nó nằm đúng giao điểm khó nhằn nhất giữa hai lĩnh vực:

1. **Hệ động lực rời rạc (Discrete Dynamical Systems):** Ngành này nghiên cứu quỹ đạo $$x, f(x), f(f(x)), \dots$$ khi áp dụng lặp đi lặp lại một hàm $$f$$. Các câu hỏi trung tâm luôn là: *Quỹ đạo có tiến ra vô cùng không? Có bị hút vào một điểm cố định hay chu trình tuần hoàn không? Và hai điểm xuất phát rất gần nhau (như $$26$$ và $$27$$) có tách xa nhau hỗn loạn không?* Khi $$f$$ tác động lên số thực (như ánh xạ logistic $$x \mapsto rx(1-x)$$ hay phương pháp Newton), ta có giải tích và đạo hàm để nghiên cứu. Nhưng khi $$f$$ tác động lên **số nguyên** như ánh xạ Collatz, ta bước vào lãnh địa của **động lực số học (arithmetic dynamics)** — nơi không có đạo hàm liên tục thông thường!
2. **Xung đột giữa cấu trúc cộng và cấu trúc nhân:** Phép chia $$n/2$$ hoàn toàn tôn trọng phân tích thừa số nguyên tố (nó chỉ xóa đi chữ số `0` ở cuối biểu diễn nhị phân). Ngược lại, phép $$3n+1$$ lại cộng thêm $$1$$ — hành động tưởng nhỏ bé này **xáo trộn toàn bộ cấu trúc nhân** của số $$n$$ theo cách cực kỳ khó lần theo. Chính sự giằng co giữa phép cộng và phép nhân là lý do nhiều bài toán số học kinh điển (như giả thuyết Goldbach, giả thuyết abc, và Collatz) vẫn còn bỏ ngỏ.

Một phép tính nhẩm trực giác cho thấy vì sao các quỹ đạo *có vẻ* sẽ giảm: xuất phát từ một số lẻ $$n$$, ta biến nó thành $$3n+1$$ (chắc chắn chẵn). Nếu giả sử số chẵn này "ngẫu nhiên" chia hết cho $$2$$ đúng $$k$$ lần (với xác suất $$2^{-k}$$), thì trung bình ta chia cho $$2$$ đúng $$2$$ lần (tức chia cho $$4$$). Sau một chu kỳ lẻ→lẻ, số mới có kích thước cỡ $$\frac{3}{4}n < n$$ — mỗi bước giảm khoảng $$25\%$$ theo trung bình hình học! Thế nhưng đó mới chỉ là **lập luận gần đúng**: chưa ai loại trừ được khả năng tồn tại một số nguyên khổng lồ nào đó "né" được quy luật trung bình để chạy mãi ra vô cùng hoặc rơi vào một chu trình kín khác $$4 \to 2 \to 1$$.

---

## 1. Kiến thức toán nền

### 1.1 Ánh xạ Collatz

Với số nguyên dương $$n$$:

$$
T(n)=
\begin{cases}
n/2 & \text{nếu }n\text{ chẵn},\\
3n+1 & \text{nếu }n\text{ lẻ}.
\end{cases}
$$

(Một số tài liệu gộp hai bước thành $$(3n+1)/2$$ khi $$n$$ lẻ. Hãy **chọn một quy ước** trong đề xuất và giữ nguyên, không trộn lẫn hai cách đếm bước.)

Lặp lại: $$n,T(n),T(T(n)),\ldots$$. **Giả thuyết Collatz** nói rằng với mọi $$n$$ dương, dãy này sẽ đến 1 (tức là rơi vào chu trình $$4\to 2\to 1\to 4\to\cdots$$).

![Quy tắc Collatz]({{ site.baseurl }}/img/chapter_img/collatz_tree.svg)

*Hình. Một bước của ánh xạ; giả thuyết nói về mọi quỹ đạo.*

### 1.2 Thời gian dừng

- **Thời gian dừng toàn phần** $$\sigma_\infty(n)$$: số lần áp dụng $$T$$ để đến 1. Ví dụ: với $$n=6$$, quỹ đạo là $$6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$$ nên $$\sigma_\infty(6) = 8$$.  
- **Thời gian dừng** $$\sigma(n)$$: số bước để đến một giá trị **nhỏ hơn hẳn** $$n$$. Với $$n=6$$, chỉ sau 1 bước ta đã được $$3 < 6$$ nên $$\sigma(6) = 1$$; nhưng với $$n=7$$ ($$7 \to 22 \to 11 \to 34 \to 17 \to 52 \to 26 \to 13 \to 40 \to 20 \to 10 \to 5 < 7$$), ta có $$\sigma(7) = 11$$ và $$\sigma_\infty(7) = 16$$.  
- **Giá trị cực đại của quỹ đạo:** giá trị lớn nhất mà quỹ đạo đạt được trước khi về 1 (với $$n=7$$ là $$52$$; với $$n=27$$ vọt lên $$9232$$!).

Hãy ghi rõ định nghĩa bạn dùng trong mã nguồn và trong nhật ký.

### 1.3 Vì sao bài toán khó

Ánh xạ này vừa làm số nhỏ đi (chia 2) vừa làm số lớn lên ($$3n+1$$). Một lập luận gần đúng về trung bình cho thấy quỹ đạo thường giảm dần, nhưng lập luận gần đúng không phải là chứng minh. Quy tắc hoàn toàn tất định, vậy mà số liệu thời gian dừng vẫn rất thất thường. Đã có một số kết quả từng phần (về mật độ các số rơi xuống dưới chính nó, về kiểm tra đến những cận rất lớn). Khi dùng các kết quả này, hãy **trích dẫn nguồn**, không tự bịa.

**Những điểm cần nắm khi viết hồ sơ (rút ra từ tư liệu video và nghiên cứu).**

- **$$\operatorname{Col}_{\min}(N)$$** là giá trị nhỏ nhất trên quỹ đạo xuất phát từ $$N$$. Giả thuyết Collatz đầy đủ nói rằng giá trị này $$=1$$ với mọi $$N$$ dương (**còn mở**).  
- **Tao (2019):** với hầu hết $$N$$ (theo mật độ logarit), $$\operatorname{Col}_{\min}(N)<f(N)$$ với mọi hàm $$f\to\infty$$. Đây là **định lý về "hầu hết" các số**, không phải lời giải giả thuyết Collatz. Nếu nhắc đến, hãy trích [arXiv:1909.03562](https://arxiv.org/abs/1909.03562).  
- **Ánh xạ Syracuse / ánh xạ tăng tốc** làm thay đổi cách đếm bước: trong đề xuất, hãy ghi rõ bạn dùng $$T$$ hay ánh xạ chỉ trên số lẻ.  
- Hằng số $$\log 3/\log 4\approx 0.7925$$ (kết quả của Korec) là phần đọc thêm tùy chọn.

Chi tiết: bài Collatz ở Chương 1, mục 4–5, và `research/video-research/collatz/analysis.md`.

### 1.4 Cây ngược

Mọi số $$m$$ đều có tiền ảnh $$2m$$; ngoài ra $$(m-1)/3$$ cũng có thể là tiền ảnh nếu $$m \equiv 4 \pmod 6$$ (để $$(m-1)/3$$ là số nguyên dương lẻ). Cây gồm các số chảy về 1 là một đối tượng thí nghiệm phong phú: có thể khảo sát số lượng nút ở mỗi độ sâu $$k$$, hay các quy luật theo đồng dư.

### 1.5 Các phép lặp khác ngoài Collatz

Ví dụ: ánh xạ logistic $$x\mapsto rx(1-x)$$; phương pháp Newton; phương pháp Babylon tính căn bậc hai… Nếu đổi đề, hãy **giữ nguyên cấu trúc hồ sơ**. Collatz được chọn làm đề mặc định vì dễ lập trình và thật sự còn là bài toán mở.

### 1.6 Kiểm tra bằng máy tính và chứng minh

Giả thuyết Collatz đã được kiểm tra cho mọi số đến một cận rất lớn (hãy trích nguồn tin cậy, vì cận này thay đổi theo thời gian, chẳng hạn vượt mốc $$2^{68} \approx 2.95 \times 10^{20}$$). Bài học giống với giả thuyết Riemann: việc kiểm tra rất nhiều không điểm nằm trên đường tới hạn làm ta tin hơn, nhưng không giải quyết được bài toán. **Không thể kiểm tra hết vô hạn trường hợp bằng một tìm kiếm hữu hạn.**

---

## 2. Cấu trúc hồ sơ thực hành

| Mốc | Tuần (theo lịch học) | Sản phẩm |
|-----|-----------------|----------|
| Đề xuất | W11 | Câu hỏi, định nghĩa, phương pháp, công cụ, tiêu chí (1–2 trang) |
| Nhật ký | W13 | Các mục có ngày tháng; thí nghiệm; các hướng bế tắc |
| Báo cáo cuối | W15 | Khoảng 6–10 trang: kết quả + giới hạn + câu hỏi tiếp theo |

**Về AI.** Được dùng AI hỗ trợ viết mã nếu khai báo rõ; nhưng **nhật ký thí nghiệm và phần diễn giải** phải do bạn tự viết.

---

## 3. Giả thuyết, chứng minh và thí nghiệm

| Nhãn | Ví dụ |
|------|-------|
| **Định lý** | Lũy thừa của 2 về 1 sau $$\log_2 n$$ lần chia đôi |
| **Giả thuyết** | Giả thuyết Collatz đầy đủ |
| **Kiểm tra bằng máy tính** | Đã kiểm tra mọi $$n\le N$$ (có trích dẫn) |
| **Quan sát** | "Thời gian dừng trung bình với $$n\le 10^4$$ là …" |
| **Lập luận gần đúng** | Mô hình nhân trung bình |

**Tiêu chí thành công (có thể điều chỉnh, nhưng phải cụ thể):**

1. Đề xuất được duyệt, với định nghĩa cố định trước khi viết mã lớn.  
2. Ít nhất 2 thí nghiệm ở mục 5 có hình hoặc bảng.  
3. Nhật ký có ít nhất 8 mục, trong đó ít nhất 2 lần thất bại.  
4. Báo cáo nói rõ điều gì **chưa** được chứng minh.  
5. Một giả thuyết bằng số được kết luận: đúng / sai / chưa kết luận được.  
6. Một đoạn về sự khác nhau giữa kiểm tra bằng máy tính và chứng minh, có trích dẫn cận đã kiểm tra.

Những việc không phải mục tiêu: "chứng minh Collatz", "tìm phản ví dụ nổi tiếng mà không có phương pháp".

---

## 4. Cách ghi nhật ký nghiên cứu

**Ngày · Mục đích · Việc đã làm · Kết quả · Nhãn · Diễn giải · Bước tiếp theo.**

Thất bại cũng được tính. Một lỗi lệch một đơn vị (off-by-one) là một sự kiện cần ghi lại, không sửa âm thầm. Ghi rõ ngôn ngữ lập trình, vấn đề tràn số (số nguyên lớn của Python hay kiểu số có độ dài cố định), và hạt giống ngẫu nhiên nếu có lấy mẫu.

---

## 5. Các thí nghiệm

Làm **ít nhất hai** trong các thí nghiệm A–G; sinh viên làm bài chính cho seminar nên làm ba.

### Thí nghiệm A — Tính quỹ đạo bằng tay (20–40 phút)

Tính quỹ đạo của $$n=1,2,\ldots,20$$ bằng tay hoặc bằng một chương trình nhỏ. Ghi lại số bước để về 1.

**Giả thuyết đặt ra trước khi tính:** "Số lẻ luôn cần nhiều bước hơn số chẵn kề nó." Sau đó kiểm tra.

**Tiêu chí thành công:** bảng đầy đủ + kết luận về giả thuyết (đúng / sai / chưa kết luận được).

### Thí nghiệm B — Đồ thị thời gian dừng (45–120 phút)

Với $$n=1$$ đến $$N$$ (bắt đầu với $$N=200$$, sau đó $$10^4$$ hoặc $$10^5$$), vẽ thời gian dừng toàn phần theo $$n$$. Đánh dấu các giá trị kỷ lục.

![Phác stopping time]({{ site.baseurl }}/img/chapter_img/collatz_stopping_time.svg)

*Hình. Phác họa cho thấy thời gian dừng rất không đều. Hãy vẽ đồ thị thật và đưa vào nhật ký.*

**Tiêu chí thành công:** đồ thị + 5 giá trị $$n$$ có thời gian dừng kỷ lục trong phạm vi + chú thích phân biệt quan sát với "quy luật".

### Thí nghiệm C — Quy luật theo đồng dư (40–90 phút)

Chia các số theo $$n\bmod 8$$ hoặc $$n\bmod 16$$. So sánh thời gian dừng trung bình và giá trị cực đại trung bình giữa các lớp.

**Lưu ý:** tương quan không phải là quy luật; với môđun nhỏ rất dễ bị đánh lừa; kiểm tra quá nhiều môđun sẽ dẫn đến sai lệch do kiểm định bội (multiple testing).

**Tiêu chí thành công:** bảng trung bình theo số dư + một đoạn diễn giải thận trọng.

### Thí nghiệm D — Cây ngược (mở rộng, 60–120 phút)

Liệt kê mọi số về 1 sau đúng $$k$$ bước, với $$k\le K$$ (chọn $$K$$ vừa sức máy tính). Vẽ số lượng theo $$k$$. Những lớp đồng dư nào chiếm ưu thế ở các tầng đầu?

**Tiêu chí thành công:** mô tả thuật toán + bảng đếm + một điều bất ngờ.

### Thí nghiệm E — Tìm hiểu kết quả kiểm tra bằng máy tính (30–45 phút)

Tìm nguồn tin cậy cho biết giả thuyết Collatz đã được kiểm tra đến đâu. Trích dẫn nguồn. Viết ba câu về sự khác nhau giữa kiểm tra và chứng minh, liên hệ với bài giả thuyết Riemann.

**Tiêu chí thành công:** có trích dẫn + có suy nghĩ riêng (không chỉ dựa vào blog không rõ nguồn).

### Thí nghiệm F — Mô hình xác suất đơn giản (45–90 phút)

Xây dựng một mô hình xác suất thô: số lẻ được biến thành $$3n+1$$ rồi chia 2 cho đến khi lại lẻ; ước lượng kỳ vọng của độ thay đổi logarit sau mỗi chu kỳ. So sánh bậc độ lớn với giá trị trung bình thực nghiệm.

**Tiêu chí thành công:** dẫn xuất mô hình + so sánh với thực nghiệm + ghi rõ "đây không phải chứng minh".

### Thí nghiệm G — Một phép lặp khác (nếu đổi đề)

Ánh xạ logistic với $$r=4$$: vẽ biểu đồ tần suất các giá trị lặp; minh họa sự phụ thuộc nhạy vào điều kiện đầu. Hoặc phương pháp Newton cho $$z^2-1$$ trên số phức (các miền hút), chỉ khi giảng viên đồng ý. Dùng lại cấu trúc đề xuất / nhật ký / báo cáo.

**Tiêu chí thành công:** hồ sơ đạt chất lượng như với đề Collatz.

---

## 6. Mẫu đề xuất

1. **Câu hỏi.** Ví dụ: thời gian dừng tăng như thế nào khi $$n\le N$$? Lớp đồng dư nào có quỹ đạo dài hơn?  
2. **Định nghĩa.** $$T$$, thời gian dừng, ánh xạ Syracuse rút gọn (nếu dùng).  
3. **Phương pháp.** Ngôn ngữ lập trình, phạm vi, loại đồ thị, phần cứng.  
4. **Tiêu chí.** Không đặt mục tiêu "chứng minh Collatz"; ví dụ: vẽ đồ thị với $$N=10^5$$; đưa ra hai giả thuyết bằng số; bác bỏ một phỏng đoán ngây thơ.  
5. **Rủi ro.** Tràn số; lỗi lệch một đơn vị; sai lệch thống kê; "p-hacking" khi thử nhiều môđun; dùng mã do AI viết mà không hiểu.  
6. **Khai báo việc dùng AI.**

Nộp đề xuất trước khi viết mã lớn, để tránh việc nhìn đồ thị rồi mới đặt câu hỏi cho khớp.

---

## 7. Dàn ý báo cáo

1. Giới thiệu: phát biểu giả thuyết Collatz; nói rõ điều gì không được chứng minh.  
2. Định nghĩa và phương pháp.  
3. Các thí nghiệm: thiết kế, kết quả, hình vẽ.  
4. Các giả thuyết bằng số đúng hay sai theo *phép kiểm tra của bạn*.  
5. Giới hạn (phạm vi, sai lệch, lỗi).  
6. Liên hệ với các chủ đề khác của khóa học.  
7. Tài liệu tham khảo + khai báo việc dùng AI.

**Tiêu chí chấm chính:** câu hỏi rõ ràng, nhật ký chất lượng, tính toán nhỏ nhưng đúng, trung thực về giới hạn. Không ai chờ đợi một "định lý Collatz mới".

---

## 8. Hiểu lầm thường gặp

1. "Đã kiểm tra đến $$10^{18}$$ nên Collatz đúng." Đó chỉ là bằng chứng trên một đoạn hữu hạn, không phải cho mọi $$n$$.  
2. "Quy tắc này ngẫu nhiên." Quy tắc hoàn toàn tất định; chỉ có số liệu về quỹ đạo là trông thất thường.  
3. "$$3n+1$$ làm số tăng mãi." Kết hợp với các bước chia 2, trung bình số thường giảm (theo lập luận gần đúng).  
4. "Đã biết có chu trình khác 4–2–1 với số dương." Đừng khẳng định điều này khi không có trích dẫn.  
5. "Khám phá thì không cần chặt chẽ." Bài thực hành đòi hỏi chặt chẽ hơn một bài tập tính toán.  
6. "Có định nghĩa thời gian dừng chuẩn quốc tế." Không có; định nghĩa khác nhau dẫn đến những bất đồng không có thật.  
7. "Tao đã giải xong Collatz." Kết quả của Tao năm 2019 là về "hầu hết" các số và quỹ đạo "gần như bị chặn" (theo mật độ logarit), không phải giả thuyết đầy đủ (xem Chương 1, mục 5).

---

## 9. Bài tập khởi động (làm trước khi viết đề xuất)

1. Viết quỹ đạo đầy đủ của $$27$$; đếm số bước theo quy ước $$T$$ của bạn.  
2. Chứng minh mọi lũy thừa của 2 đều về 1 và tính đúng số bước.  
3. Chứng minh không có bộ ba $$(p,p+2,p+4)$$ đều là số nguyên tố ngoài $$(3,5,7)$$, và giải thích vì sao bài này **không** liên quan đến Collatz (công cụ của bài thực hành về số nguyên tố là khác).  
4. Viết giả mã cho `stopping_time(n)` kèm cách xử lý khi chạy quá lâu hoặc tràn số.  
5. Đưa ra một giả thuyết về thời gian dừng có thể kiểm tra là sai.  
6. Phác thảo mục 1–2 của đề xuất, không quá 200 từ.

---

## 10. Danh sách kiểm tra theo tiêu chí chấm

| ☐ | Đề xuất + định nghĩa cố định + tiêu chí |
| ☐ | Ít nhất 2 thí nghiệm có hình/bảng |
| ☐ | Nhật ký ít nhất 8 mục, ít nhất 2 lần thất bại |
| ☐ | Phân biệt kiểm tra và chứng minh, có trích dẫn |
| ☐ | Báo cáo có gắn nhãn định lý / giả thuyết / quan sát |
| ☐ | Khai báo việc dùng AI |
| ☐ | Câu hỏi mở cho bước tiếp theo |

---

## 11. Tài liệu và liên kết

Danh sách URL đầy đủ: `research/video-research/collatz/references.md`. **Không** coi video phổ biến kiến thức là chứng minh.

1. Lagarias overview: https://arxiv.org/abs/2111.02635 · PDF https://arxiv.org/pdf/2111.02635 · SFU http://www.cecm.sfu.ca/organics/papers/lagarias/  
2. Tao almost-all: https://arxiv.org/abs/1909.03562 · PDF https://arxiv.org/pdf/1909.03562 · blog https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/  
3. Tao 2011: https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/  
4. Video chính: https://www.youtube.com/watch?v=094y1Z2wpJg · https://www.youtube.com/watch?v=5mFpVDpKX70 · https://www.youtube.com/watch?v=t1I9uHF9X5Y · https://mathtube.org/lecture/video/notorious-collatz-conjecture · https://www.youtube.com/watch?v=X2p5eMWyaFs · https://terrytao.files.wordpress.com/2020/02/collatz.pdf · https://www.youtube.com/watch?v=k-dtx8s2ehM · https://www.youtube.com/watch?v=Lr6qc_9M0Ks  
5. Video phụ: https://www.youtube.com/watch?v=m4CjXk_b8zo · https://www.youtube.com/watch?v=LqKpkdRRLZw · https://www.youtube.com/watch?v=O2_h3z1YgEU · https://youtu.be/wH141HLD57o · https://www.youtube.com/watch?v=vT4VJyXWHlo · https://www.numberphile.com/videos/uncrackable-the-collatz-conjecture  
6. Web: https://en.wikipedia.org/wiki/Collatz_conjecture · https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/ · https://chamberland.math.grinnell.edu/3x.html · https://dmi.unibas.ch/en/news/details/lecture-in-basel-terence-tao-and-the-notorious-collatz-conjecture/ · https://mathematics.stanford.edu/events/kiddie-colloquium/almost-almost-collatz · https://www.mathematics.pitt.edu/content/note-collatz-conjecture · http://www.math.grinnell.edu/~chamberl/papers/3x_survey_eng.pdf · https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa15/addcomments/Lagarias_3x+1AndItsGeneralizations.pdf · https://www.rism.it/rism-channel/2021/riemann-prize-week/the-notorious-collatz-conjecture-terence-tao  
7. [Collatz (Chương 1)]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/), [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/), [Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/). Bộ tư liệu: `research/video-research/collatz/`.  
8. Các bài thực hành khác: dùng lại cấu trúc hồ sơ này.

---

## Bước tiếp theo

Các buổi seminar tuần W11–W13 xoay quanh bài thực hành này. Hãy mang đồ thị đến lớp; phần góp ý sẽ tập trung vào phương pháp, không phải khoe kết quả. Nếu bạn thấy mình bị cuốn vào Collatz quá mức, hãy đặt điểm dừng rõ ràng và viết về giới hạn của tính toán như một **nội dung** của dự án, không coi đó là thất bại cá nhân.

## Nguồn video (bộ tư liệu nghiên cứu video)

Video dùng để **định hướng và làm quen với cách làm nghiên cứu**, không thay thế chứng minh. Chi tiết: `research/video-research/collatz/`.

**Những điểm chính từ bộ tư liệu**

- Bộ tư liệu về Collatz: `research/video-research/collatz/`.
- Kết quả "hầu hết" của Tao năm 2019 không phải lời giải giả thuyết Collatz (bài toán vẫn **còn mở** tính đến 2026).

**Thứ tự xem gợi ý**

1. **Định hướng** — Veritasium — Collatz: [https://www.youtube.com/watch?v=094y1Z2wpJg](https://www.youtube.com/watch?v=094y1Z2wpJg).  
2. **Trực giác** — Numberphile — UNCRACKABLE Collatz: [https://www.youtube.com/watch?v=5mFpVDpKX70](https://www.youtube.com/watch?v=5mFpVDpKX70).  
3. **Nền tảng** — Chamberland, tình hình bài toán 3x+1, phần 1: [https://www.youtube.com/watch?v=t1I9uHF9X5Y](https://www.youtube.com/watch?v=t1I9uHF9X5Y).  
4. **Cốt lõi** — Tao, "The Notorious Collatz Conjecture" (mathtube): [https://mathtube.org/lecture/video/notorious-collatz-conjecture](https://mathtube.org/lecture/video/notorious-collatz-conjecture).  
5. **Cốt lõi** — Tao, "The Notorious Collatz Conjecture" (YouTube): [https://www.youtube.com/watch?v=X2p5eMWyaFs](https://www.youtube.com/watch?v=X2p5eMWyaFs).  
6. **Mới nhất** — Tao tại IAS về kết quả "hầu hết" cho Collatz: [https://www.youtube.com/watch?v=k-dtx8s2ehM](https://www.youtube.com/watch?v=k-dtx8s2ehM).  

**Tài liệu gốc**

- Tao, arXiv:1909.03562: https://arxiv.org/abs/1909.03562  
- Lagarias, bài tổng quan arXiv:2111.02635: https://arxiv.org/abs/2111.02635  

Danh sách URL đầy đủ: `research/video-research/collatz/references.md`.

### Phụ đề và khung hình (bài chính)

Phụ đề và các đoạn theo thời gian cho bộ tư liệu Collatz: `research/video-research/collatz/transcripts/` · trạng thái: `research/video-research/collatz/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

**Khung hình mẫu** (định hướng cho bài thực hành):

![Frame mẫu video Collatz]({{ site.baseurl }}/img/video_research/collatz/5mFpVDpKX70_frame01.jpg)

*Hình. Khung hình mẫu từ video định hướng chính về Collatz (xem bộ tư liệu để biết mốc thời gian).*

### Bộ tư liệu video (mọi URL)

Danh mục đầy đủ: `research/video-research/collatz/references.md`.

1. Veritasium — Collatz — https://www.youtube.com/watch?v=094y1Z2wpJg  
2. Numberphile — UNCRACKABLE Collatz — https://www.youtube.com/watch?v=5mFpVDpKX70  
3. Chamberland 3x+1 status Part 1 — https://www.youtube.com/watch?v=t1I9uHF9X5Y  
4. Tao Notorious Collatz (mathtube) — https://mathtube.org/lecture/video/notorious-collatz-conjecture  
5. Tao Notorious Collatz (YouTube) — https://www.youtube.com/watch?v=X2p5eMWyaFs  
6. Tao IAS almost-all Collatz — https://www.youtube.com/watch?v=k-dtx8s2ehM  
7. Tao arXiv:1909.03562 — https://arxiv.org/abs/1909.03562  
8. Lagarias overview arXiv:2111.02635 — https://arxiv.org/abs/2111.02635  
9. Full bibliography (pack) — research/video-research/collatz/references.md  
10. Quanta Tao Collatz — https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/  
11. Thư mục gói: `research/video-research/collatz/`.

### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/explore-iteration/transcripts/` · trạng thái: `research/video-research/explore-iteration/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/explore-iteration_094y1Z2wpJg_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*


## Video tham khảo

- **Xem trước:** [The Simplest Math Problem No One Can Solve - Collatz Conjecture](https://www.youtube.com/watch?v=094y1Z2wpJg) — Veritasium, tiếng Anh. Giới thiệu giả thuyết Collatz; nên xem trước khi đọc bài.
- [UNCRACKABLE? The Collatz Conjecture - Numberphile](https://www.youtube.com/watch?v=5mFpVDpKX70) — Numberphile, tiếng Anh. Nên xem sau khi đã nắm ý chính của bài.
- [The 3x+1 Problem: Status and Recent Work Part 1](https://www.youtube.com/watch?v=t1I9uHF9X5Y) — Experimental mathematics, tiếng Anh. Xem thêm sau hai video trên: tình hình nghiên cứu bài toán 3x+1.
