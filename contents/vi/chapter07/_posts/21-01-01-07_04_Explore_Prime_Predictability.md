---
layout: post
title: "Số nguyên tố có dự đoán được không?"
chapter: '07'
order: 4
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
---

> **Bài liên quan trong khóa học**  
> [Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) · [Số nguyên tố sinh đôi]({{ site.baseurl }}/contents/vi/chapter01/01_06_Twin_Prime_Conjecture/) · [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) · [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/)

Nếu bạn bước dọc theo trục số nguyên dương và gõ một tiếng chuông mỗi khi gặp một số nguyên tố — $$2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37\dots$$ — âm thanh bạn nghe thấy sẽ vô cùng khó đoán. Có lúc hai tiếng chuông vang lên sát nhau chỉ cách 2 đơn vị (như $$101$$ và $$103$$), có lúc bạn phải bước qua hàng chục, thậm chí hàng triệu hợp số im ắng mới nghe thấy tiếng tiếp theo. Nhìn gần, các số nguyên tố hành xử bất kham chẳng khác nào trò tung đồng xu.

Nhưng hãy lùi thật xa ra và nhìn toàn cảnh: sự hỗn loạn bỗng nhường chỗ cho một đường cong mượt mà đến kinh ngạc. **Định lý số nguyên tố** mô tả chính xác mật độ của chúng; **giả thuyết Riemann** nhắm tới độ chính xác gần như tuyệt đối của sai số; **định lý khoảng cách bị chặn** (Zhang, Maynard) khẳng định chúng không bao giờ thôi đứng sát nhau; còn **định lý Green–Tao** chứng minh bên trong dãy số tưởng chừng ngẫu hứng ấy ẩn chứa những cấp số cộng đều tăm tắp dài tùy ý. Câu hỏi *"Số nguyên tố có dự đoán được không?"* vì thế không có câu trả lời Có hay Không đơn giản. Trong bài thực hành này, bạn sẽ tự tay **chạy thí nghiệm trên số nguyên tố**, xây dựng một **bảng phân tầng hiện tượng**, và rèn thói quen tỉnh táo nhất của người làm số học: không bao giờ đánh đồng một đồ thị khớp đẹp đến $$10^8$$ với một định lý đúng cho tới vô cùng.

---

## Mục tiêu học tập

Sau bài thực hành, bạn có thể:

- Phát biểu định lý số nguyên tố: $$\pi(x)\sim x/\log x$$; tính $$\pi(x)$$ với $$x$$ vừa phải.
- Vẽ đồ thị hoặc lập bảng khoảng cách $$g_n=p_{n+1}-p_n$$; mô tả khoảng cách điển hình và những khoảng cách lớn hiếm gặp.
- Phân biệt trong một bảng: định lý số nguyên tố, giả thuyết Riemann, giả thuyết số nguyên tố sinh đôi, định lý khoảng cách bị chặn (Zhang/Maynard), định lý Green–Tao.
- Thiết kế thí nghiệm có phạm vi và tiêu chí rõ ràng; ghi nhãn để không nhầm quan sát với chứng minh.
- Giải thích vì sao kiểm tra đến một số $$X$$ lớn chỉ là bằng chứng trên một đoạn, không phải chứng minh cho mọi số.
- Đưa ra ít nhất một giả thuyết bằng số **có thể bác bỏ** và cố gắng bác bỏ nó.

**Kiến thức cần có.** Tính chia hết, ý tưởng cơ bản của phương pháp sàng, logarit, viết chương trình ngắn hoặc dùng phần mềm tính toán.

---

## Bản đồ kiến thức nền: Lý thuyết số giải tích là gì và nghiên cứu những gì?

Khi nghe tới số nguyên tố, nhiều người nghĩ ngay tới đại số rời rạc hay phép chia hết ở bậc phổ thông. Vậy tại sao những đột phá lớn nhất về số nguyên tố lại gắn với tích phân, biến số phức và sóng? Câu trả lời nằm ở **Lý thuyết số giải tích (Analytic Number Theory)** — ngành toán dùng công cụ liên tục (giải tích phức, chuỗi, biến đổi Fourier, xác suất) để trả lời những câu hỏi rời rạc về số nguyên.

Bức tranh lớn của ngành này xoay quanh ba trụ cột mà bạn sẽ chạm tới trong bài thực hành:

1. **Từ rời rạc sang liên tục qua hàm Zeta:** Leonard Euler phát hiện đẳng thức kỳ diệu nối mọi số nguyên dương với mọi số nguyên tố: $$\zeta(s) = \sum_{n=1}^{\infty} n^{-s} = \prod_{p} (1 - p^{-s})^{-1}$$. Sau đó Bernhard Riemann mở rộng $$s$$ sang mặt phẳng phức và chứng minh rằng dao động của hàm đếm số nguyên tố $$\pi(x)$$ được "mã hóa" hoàn toàn bởi vị trí các không điểm của $$\zeta(s)$$ — giống như một bản nhạc (phân bố số nguyên tố) được ghép từ các tần số cơ bản (các không điểm của hàm zeta).
2. **Phương pháp sàng (Sieve Theory):** Bắt nguồn từ sàng Eratosthenes cổ đại, các phương pháp sàng hiện đại (như sàng Selberg hay sàng nhiều chiều của Maynard–Tao) tìm cách ước lượng số lượng phần tử còn sót lại sau khi loại bỏ các bội số, từ đó chứng minh tồn tại vô hạn cặp số nguyên tố cách nhau không quá $$246$$ đơn vị.
3. **Tổ hợp cộng tính và mô hình xác suất:** Khi hỏi về các mẫu hình cộng tính (như bộ ba số nguyên tố cách đều $$3, 5, 7$$ hay bộ 5 số $$5, 11, 17, 23, 29$$), các nhà toán học dùng mô hình xác suất (mô hình Cramér: coi mỗi số $$n$$ có "xác suất" là số nguyên tố cỡ $$1/\log n$$) để dự đoán, rồi dùng giải tích Fourier và lý thuyết cấu trúc để chứng minh.

Một con số cụ thể để bạn cảm nhận sức mạnh của xấp xỉ: dưới $$x = 1.000.000$$, có chính xác $$\pi(10^6) = 78.498$$ số nguyên tố. Công thức sơ cấp $$x/\log x$$ dự đoán khoảng $$72.382$$ (lệch khoảng $$7.8\%$$), nhưng tích phân logarit $$\operatorname{li}(10^6)$$ cho ra $$78.627{,}5$$ — sai lệch chỉ **130 số** trên một triệu!

---

## 1. Kiến thức toán nền

### 1.1 Đếm số nguyên tố

Gọi $$p_n$$ là số nguyên tố thứ $$n$$ và $$\pi(x)=\#\{p\le x\}$$. **Định lý số nguyên tố** khẳng định

$$
\pi(x)\sim\frac{x}{\log x}\qquad(x\to\infty),
$$

tương đương với $$p_n\sim n\log n$$. Một xấp xỉ cổ điển chính xác hơn là tích phân logarit $$\operatorname{li}(x) = \int_2^x \frac{dt}{\log t}$$. Trên thực nghiệm, với những giá trị $$x$$ ta tính được, $$\pi(x)$$ khá gần các xấp xỉ này. Nhưng "khá gần" là một phát biểu định lượng về sai số, và đó chính là nội dung của giả thuyết Riemann.

### 1.2 Khoảng cách và số nguyên tố sinh đôi

Khoảng cách sau $$p_n$$ là $$g_n=p_{n+1}-p_n$$. Theo lập luận gần đúng, khoảng cách điển hình có độ lớn cỡ $$\log p_n$$, nhưng vẫn có những khoảng cách rất lớn. Dùng giai thừa có thể tạo ra khoảng cách lớn tùy ý:

$$
(n+1)!+2,\;(n+1)!+3,\;\ldots,\;(n+1)!+(n+1)
$$

là $$n$$ hợp số liên tiếp (vì số hạng thứ $$k$$ chia hết cho $$k+1$$). Chẳng hạn với $$n=4$$, ta có $$5!+2 = 122, 123, 124, 125$$ lần lượt chia hết cho $$2, 3, 4, 5$$ — dù thực tế trên trục số, khoảng trống 4 hợp số liên tiếp đã xuất hiện sớm hơn nhiều (ngay sau $$23$$ là $$24, 25, 26, 27, 28$$). Vậy khẳng định "khoảng cách luôn bị chặn" là sai, trong khi "khoảng cách *thường* có độ lớn cỡ $$\log p$$" vẫn có thể đúng theo nghĩa trung bình.

**Số nguyên tố sinh đôi** là cặp $$(p,p+2)$$ mà cả hai đều là số nguyên tố (như $$(3,5), (11,13), (29,31)$$). Giả thuyết cho rằng có vô số cặp như vậy. Lập luận gần đúng của **Hardy–Littlewood** dự đoán

$$
\#\{p\le X: p+2\text{ nguyên tố}\}\sim 2C_2\int_2^X\frac{dt}{(\log t)^2},
$$

với hằng số số nguyên tố sinh đôi $$C_2\approx 0.66016$$. Số liệu thực tế khớp với dự đoán này từ rất lâu, dù vẫn chưa có chứng minh.

### 1.3 Khoảng cách bị chặn và Maynard

**Zhang (2013):** $$\liminf(p_{n+1}-p_n)<\infty$$, cụ thể là với một cận số ban đầu là $$70.000.000$$, dựa trên phương pháp GPY và các công cụ kiểu Bombieri–Vinogradov. **Maynard**, và độc lập là Tao, đã đơn giản hóa và làm mạnh phương pháp bằng sàng nhiều chiều; dự án Polymath8 và các công trình sau đó hạ cận này xuống còn **246** (không cần giả thuyết bổ sung). Định lý khoảng cách bị chặn nói rằng *thỉnh thoảng* có các số nguyên tố đứng gần nhau; nó chưa suy ra được giả thuyết số nguyên tố sinh đôi (khoảng cách bằng 2).

### 1.4 Định lý Green–Tao

**Định lý Green–Tao:** tập các số nguyên tố chứa những cấp số cộng có độ dài hữu hạn tùy ý. Với mọi $$k$$, tồn tại $$a,d$$ sao cho

$$
a,\;a+d,\;\ldots,\;a+(k-1)d
$$

đều là số nguyên tố. Ví dụ, với $$k=5$$ ta có ngay $$5, 11, 17, 23, 29$$ (công sai $$d=6$$); với $$k=6$$ ta có $$7, 37, 67, 97, 127, 157$$ (công sai $$d=30$$ — bạn có nhận ra vì sao $$d$$ luôn chia hết cho $$2\cdot 3\cdot 5 = 30$$ không?). Chứng minh là một cột mốc của tổ hợp cộng tính và lý thuyết ergodic/cấu trúc, không dùng phương pháp sàng sơ cấp. Tìm cấp số cộng dài 4–5 bằng tay hoặc bằng máy là một bài khám phá tốt; chứng minh cho mọi $$k$$ không phải là nhiệm vụ của bài thực hành.

### 1.5 Giả thuyết Riemann dưới dạng sai số

Giả thuyết Riemann thường được phát biểu qua các không điểm của hàm $$\zeta(s)$$, nhưng trong bài này ta dùng cách nhìn về **sai số khi đếm số nguyên tố**:

$$
\pi(x)=\operatorname{li}(x)+O\bigl(x^{1/2}\log x\bigr)
$$

(dạng chuẩn, nếu giả thuyết Riemann đúng). Nói theo ngôn ngữ xác suất, sai số cỡ $$\sqrt{x}$$ chính là mức dao động đặc trưng của một **bước đi ngẫu nhiên** (giống độ lệch chuẩn khi tung đồng xu $$x$$ lần). Không cần giả thuyết Riemann, ta vẫn có những cận sai số yếu hơn. Mối liên hệ giữa miền không có không điểm và phân bố số nguyên tố thuộc về lý thuyết số giải tích sâu; bài giả thuyết Riemann ở Chương 1 là bài đọc kỹ đi kèm.

### 1.6 Dự đoán có nhiều tầng

| Tầng | Câu hỏi | Tình trạng |
|------|---------|---------------------|
| Mật độ | Có bao nhiêu $$p\le x$$? | Định lý số nguyên tố đã chứng minh |
| Sai số | Xấp xỉ tốt đến đâu? | Giả thuyết Riemann còn mở; có các cận từng phần |
| Cặp gần nhau | Có vô số cặp sinh đôi? | Còn mở; có nhiều dữ liệu |
| Thỉnh thoảng gần nhau | Khoảng cách bị chặn vô số lần? | Đã chứng minh (Zhang/Maynard) |
| Mẫu hình | Cấp số cộng độ dài $$k$$? | Green–Tao: đúng với mọi $$k$$ |
| Khoảng cách lớn nhất | Gần $$x$$ thì lớn cỡ nào? | Có các cận; quy luật chính xác còn mở |

---

## 2. Giả thuyết, chứng minh và thí nghiệm

| Nhãn | Ví dụ |
|------|-------|
| **Định lý** | Định lý số nguyên tố; Green–Tao; liminf của khoảng cách hữu hạn |
| **Giả thuyết** | Số nguyên tố sinh đôi; giả thuyết Riemann; nhiều giả thuyết Hardy–Littlewood về bộ số |
| **Quan sát** | "Trong phạm vi $$X=10^6$$, số cặp sinh đôi là …" |
| **Lập luận gần đúng** | Mô hình Cramér; tích phân Hardy–Littlewood |

**Không viết:** "Đã kiểm tra đến $$10^8$$ nên có vô số cặp sinh đôi."  
**Nên viết:** "Đến $$10^8$$, số cặp sinh đôi lệch so với tích phân Hardy–Littlewood khoảng __%."

**Tiêu chí:**

1. Đồ thị hoặc bảng khoảng cách cho ít nhất 200 số nguyên tố (nhiều hơn nếu được).  
2. Ít nhất một cấp số cộng gồm từ 4 số nguyên tố trở lên, ghi rõ $$d$$.  
3. Bảng các hiện tượng có ít nhất 5 dòng.  
4. Một giả thuyết bằng số có thể bác bỏ đã được kiểm tra, ghi rõ đúng hay sai.  
5. Một đoạn về sự khác nhau giữa kiểm tra bằng máy tính và chứng minh (giống bài giả thuyết Riemann).

---

## 3. Cách ghi nhật ký

**Ngày · Mục đích · Việc đã làm · Kết quả · Nhãn · Diễn giải · Bước tiếp theo.**

Ghi rõ phần mềm (SymPy, Sage, sàng tự viết), cách kiểm tra tính nguyên tố và phạm vi $$X$$ chính xác. Nếu dùng phép thử xác suất Miller–Rabin cho số lớn, hãy nói rõ; trong phạm vi của bạn, nên ưu tiên phép kiểm tra tất định.

---

## 4. Các thí nghiệm

Làm ít nhất 2 trong các thí nghiệm A–F.

### A — Đồ thị khoảng cách (30–60 phút)

Sinh $$N$$ số nguyên tố đầu tiên (bắt đầu với $$N=200$$, sau đó $$10^4$$ nếu được). Vẽ $$g_n$$ theo $$p_n$$ hoặc theo $$n$$. Đánh dấu các khoảng cách kỷ lục.

**Giả thuyết trước khi vẽ:** "Khoảng cách tăng đều như $$\log p$$."  
Sau khi vẽ: mô tả các đỉnh nhọn và độ lớn điển hình.

**Tiêu chí:** hình vẽ + chú thích 5 câu, phân biệt hành vi trung bình và các giá trị cực đoan.

### B — Đếm cặp sinh đôi và so với dự đoán (45–90 phút)

Với $$X=10^3,10^4,10^5$$ (lớn hơn nếu được), đếm số cặp sinh đôi với $$p\le X$$ và $$p+2$$ nguyên tố. So sánh với

$$
2C_2\int_2^X\frac{dt}{(\log t)^2}
$$

với $$C_2\approx 0.66016$$. Có thể tính tích phân gần đúng bằng phương pháp hình chữ nhật nếu ghi rõ.

**Tiêu chí:** bảng số liệu thực tế so với dự đoán; phần trăm sai lệch; khẳng định rõ rằng điều này *không* chứng minh có vô số cặp.

### C — Tìm cấp số cộng (30–60 phút)

Tìm các cấp số cộng gồm 4–5 số nguyên tố với $$d$$ nhỏ. Ghi lại ví dụ. Tùy chọn: đánh giá xem tìm kiếm trực tiếp cấp số cộng độ dài 6 khó đến mức nào.

**Tiêu chí:** ít nhất một cấp số cộng độ dài 4 dạng $$a+kd$$; ghi rõ phạm vi tìm kiếm.

### D — Bảng tổng hợp các hiện tượng (20–30 phút)

| Hiện tượng | Đã biết? | Loại công cụ | Có thí nghiệm trong bài? |
|------------|----------|------------|---------------------|
| Định lý số nguyên tố | | | |
| Giả thuyết Riemann | | | |
| Vô số cặp sinh đôi | | | |
| Khoảng cách bị chặn | | | |
| Green–Tao | | | |
| Khoảng cách lớn | | | |

**Tiêu chí:** không dòng nào nhầm "đã chứng minh" với "đã kiểm tra bằng số".

### E — Lệch theo lớp đồng dư (mở rộng)

Với các số nguyên tố $$\le X$$, so sánh số lượng trong các lớp đồng dư theo môđun 3, 4 hoặc 10 (chữ số tận cùng 1, 3, 7, 9). Nếu đã đọc tài liệu, hãy thảo luận về độ lệch Chebyshev, phân biệt rõ định lý và quan sát.

**Tiêu chí:** bảng đếm + lưu ý rằng với $$X$$ nhỏ rất dễ thấy quy luật giả.

### F — Tìm hiểu các kỷ lục

Tra nguồn tin cậy: các cặp sinh đôi và khoảng cách đã được lập bảng đến đâu; trích dẫn. Viết ba câu về sự khác nhau giữa dữ liệu và chứng minh.

**Tiêu chí:** có trích dẫn + có suy nghĩ riêng.

---

## 5. Hiểu lầm thường gặp

1. "Số nguyên tố ngẫu nhiên nên không có định lý nào." Mô hình ngẫu nhiên chỉ là lập luận gần đúng; định lý số nguyên tố và định lý Green–Tao là định lý thật.  
2. "Khoảng cách bị chặn suy ra giả thuyết sinh đôi." Khoảng cách ≤246 (hoặc cận bạn trích dẫn) không phải là khoảng cách bằng 2.  
3. "Green–Tao nghĩa là số nguyên tố tuần hoàn." Định lý chỉ nói có cấp số cộng độ dài hữu hạn tùy ý; một tập có mật độ 0 vẫn có thể có cấu trúc cộng tính phong phú.  
4. "Giả thuyết Riemann chỉ nói về mật độ." Định lý số nguyên tố nói về mật độ; giả thuyết Riemann nói về sai số và các không điểm.  
5. "Cấp số cộng dài mâu thuẫn với tính ngẫu nhiên." Cấu trúc và tính giả ngẫu nhiên có thể cùng tồn tại; xem bài thực hành [ngẫu nhiên và trật tự]({{ site.baseurl }}/contents/vi/chapter07/07_05_Explore_Randomness_Order/).

---

## 6. Bài tập

1. Chứng minh có khoảng cách lớn tùy ý (dùng giai thừa).  
2. Chứng minh không có bộ ba $$(p,p+2,p+4)$$ đều nguyên tố ngoài $$(3,5,7)$$. Vì sao xét môđun 3 là đủ?  
3. Tính $$\pi(100)$$, $$\pi(1000)$$ và so sánh với $$x/\log x$$.  
4. Tìm một cấp số cộng độ dài 4 và kiểm tra từng số hạng.  
5. Viết đề xuất 150 từ: bạn chọn tầng dự đoán nào, phạm vi và tiêu chí ra sao.

---

## 7. Danh sách kiểm tra theo tiêu chí chấm

| ☐ | Đồ thị/bảng khoảng cách (ít nhất 200 số nguyên tố) |
| ☐ | Bảng tình trạng các hiện tượng |
| ☐ | Cấp số cộng độ dài ít nhất 4 |
| ☐ | Đoạn về kiểm tra và chứng minh |
| ☐ | Nhật ký ít nhất 3 mục có nhãn |
| ☐ | Một giả thuyết bằng số đã kiểm tra (đúng/sai) |

---


## Nguồn video (bộ tư liệu nghiên cứu video)

Video dùng để **định hướng và làm quen với cách làm nghiên cứu**, không thay thế chứng minh. Chi tiết: `research/video-research/explore-prime-predictability/`.

**Những điểm chính từ bộ tư liệu**

- **Định lý số nguyên tố:** π(x) ~ x/log x.
- **Giả thuyết Riemann** cho biết sai số thông qua các không điểm của ζ; vẫn còn mở (2026).
- Số nguyên tố sinh đôi và khoảng cách bị chặn: Zhang, Maynard, Polymath; giả thuyết số nguyên tố sinh đôi vẫn còn mở.
- **Green–Tao:** có cấp số cộng các số nguyên tố dài tùy ý.
- Trong bài thực hành: vẽ đồ thị khoảng cách; không nhầm kiểm tra với chứng minh.

**Thứ tự xem gợi ý**

1. **Định hướng** — Quanta — Riemann Hypothesis Explained: [https://www.youtube.com/watch?v=zlm1aajH6gY](https://www.youtube.com/watch?v=zlm1aajH6gY).  
2. **Trực giác** — Numberphile — số nguyên tố sinh đôi và khoảng cách: [https://www.youtube.com/watch?v=QKHKD8bRAro](https://www.youtube.com/watch?v=QKHKD8bRAro).  
3. **Cốt lõi** — Wikipedia — định lý Green–Tao: [https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem](https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem).  

**Tài liệu gốc**

- Green–Tao, bài báo gốc trên arXiv: https://arxiv.org/abs/math/0404188  
- Maynard, khoảng cách nhỏ giữa các số nguyên tố: https://arxiv.org/abs/1311.4600  

Danh sách URL đầy đủ: `research/video-research/explore-prime-predictability/references.md`.

## 8. Tài liệu


### Bộ tư liệu video (mọi URL)

Danh mục đầy đủ: `research/video-research/explore-prime-predictability/references.md`.

1. Quanta — Riemann Hypothesis Explained — https://www.youtube.com/watch?v=zlm1aajH6gY  
2. Numberphile — Twin primes / prime gaps (search Numberphile primes) — https://www.youtube.com/watch?v=QKHKD8bRAro  
3. Numberphile — Twin Prime Conjecture (Maynard) — https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem  
4. Green–Tao arXiv classic — https://arxiv.org/abs/math/0404188  
5. Maynard small gaps between primes — https://arxiv.org/abs/1311.4600  
6. Quanta RH article hub — https://www.quantamagazine.org/tag/riemann-hypothesis/  
7. Wikipedia — Prime number theorem — https://en.wikipedia.org/wiki/Prime_number_theorem  
8. Wikipedia — Twin prime — https://en.wikipedia.org/wiki/Twin_prime  
9. Wikipedia — Green–Tao theorem — https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem  
10. Clay Math — Riemann Hypothesis — https://www.claymath.org/millennium/riemann-hypothesis/  
11. Thư mục gói: `research/video-research/explore-prime-predictability/`.

1. Các bài về giả thuyết Riemann, số nguyên tố sinh đôi, Green–Tao, Maynard (liên kết ở trên).  
2. Lập luận Hardy–Littlewood (ở mức tổng quan).  
3. Các bài viết phổ biến của Soundararajan hoặc Granville về số nguyên tố và khoảng cách (bản bạn tìm được).  
4. Bài thực hành [ngẫu nhiên và trật tự]({{ site.baseurl }}/contents/vi/chapter07/07_05_Explore_Randomness_Order/).

---

## Hướng đi tiếp

Nếu bạn quan tâm đến các không điểm hơn là khoảng cách, hãy chuyển thí nghiệm sang tổng riêng của hàm Möbius, hoặc so sánh $$\pi(x)$$ với $$\operatorname{li}(x)$$ (cẩn thận với độ chính xác của thư viện). Nếu quan tâm đến cấu trúc cộng tính, hãy tìm hiểu sâu hơn về định lý Green–Tao và tìm các cấp số cộng nhỏ với ràng buộc đồng dư. Hãy đọc [giả thuyết Riemann ở Chương 1]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) khi sai số trở thành vấn đề chính.

**Gợi ý viết bản tổng hợp một trang.** (i) tầng dự đoán bạn chọn; (ii) đồ thị khoảng cách cho thấy gì về hành vi điển hình và cực đoan; (iii) bảng tình trạng không nhầm kiểm tra với chứng minh; (iv) một giả thuyết bằng số đúng hay sai; (v) câu hỏi mở cho tuần sau.

### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/explore-prime-predictability/transcripts/` · trạng thái: `research/video-research/explore-prime-predictability/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/explore-prime-predictability_zlm1aajH6gY_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*


## Video tham khảo

- **Xem trước:** [The Riemann Hypothesis, Explained](https://www.youtube.com/watch?v=zlm1aajH6gY) — Quanta Magazine, tiếng Anh. Giải thích giả thuyết Riemann; nên xem trước khi đọc bài.
- [Twin Prime Conjecture - Numberphile](https://www.youtube.com/watch?v=QKHKD8bRAro) — Numberphile, tiếng Anh. Giả thuyết số nguyên tố sinh đôi; nên xem sau khi đã nắm ý chính của bài.
