---
layout: post
title: "Giả thuyết Số nguyên tố sinh đôi"
chapter: '01'
order: 6
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
lesson_type: required
---

Hãy thử bước dọc theo trục số nguyên dương càng lúc càng xa. Khi bạn tiến tới những con số hàng trăm chữ số, các số nguyên tố trở nên thưa thớt đến cô quạnh — trung bình phải đi qua vài trăm số mới gặp lại một số nguyên tố mới. Ấy vậy mà kỳ lạ thay, thỉnh thoảng hai số nguyên tố vẫn xuất hiện sát rạt bên nhau, chỉ cách nhau đúng một số chẵn ở giữa: $$(3,5)$$, $$(5,7)$$, $$(11,13)$$, $$(17,19)$$, $$(29,31)$$, $$(101,103)$$, và thậm chí ở tận những con số khổng lồ có gần 400.000 chữ số! Những cặp đứng cạnh nhau như thế được gọi là **số nguyên tố sinh đôi**, và **Giả thuyết số nguyên tố sinh đôi** đặt một câu hỏi tưởng như trẻ con: *liệu những cặp bạn đồng hành ấy có xuất hiện mãi mãi đến vô cùng không?*

Dù không nằm trong danh sách triệu đô của Viện Clay, đây là một trong những câu hỏi mở nổi tiếng và quyến rũ nhất của lý thuyết số. Mùa xuân năm 2013, cả thế giới toán học chấn động khi Yitang Zhang — một giảng viên ít tên tuổi khi ấy ở Đại học New Hampshire — bất ngờ gửi một bài báo phá vỡ bức tường tồn tại hàng thế kỷ: ông chứng minh được rằng tồn tại một khoảng cách chẵn *hữu hạn* (dưới 70 triệu) xuất hiện vô hạn lần giữa hai số nguyên tố liên tiếp. Chỉ trong vòng một năm sau đó, James Maynard, Terence Tao và dự án cộng tác mở Polymath đã kéo kỷ lục ấy rơi thẳng từ 70 triệu xuống còn **246**!

Thế nhưng bước nhảy cuối cùng — từ **246** xuống đúng **2** — vẫn đang chắn trước mặt nhân loại như một vách đá dựng đứng. Bài này sẽ giúp bạn phát biểu giả thuyết thật chuẩn xác, tự tay tính hệ số Hardy–Littlewood và kiểm tra bộ chấp nhận được, hiểu vì sao phương pháp sàng hiện đại bị kẹt ở "rào cản chẵn lẻ", và phân biệt rạch ròi giữa "khoảng cách bị chặn" đã được chứng minh với "sinh đôi" vẫn còn mở.

**Mạch bài học:** Bản đồ kiến thức nền → phát biểu → ví dụ tính tay hằng số Hardy–Littlewood → rào cản chẵn lẻ của sàng → ví dụ bộ chấp nhận được & khung giải thích chậm Zhang–Maynard–Polymath → những gì còn mở & hiểu lầm thường gặp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu giả thuyết số nguyên tố sinh đôi và đưa ra ví dụ về các cặp sinh đôi.
- So sánh **có vô hạn số nguyên tố** (Euclid, đã biết) với **có vô hạn cặp sinh đôi** (còn mở).
- Giải thích **khoảng cách bị chặn**: tồn tại $$H$$ sao cho $$p_{n+1}-p_n\le H$$ với vô hạn chỉ số $$n$$.
- Kể về **Zhang (2013)** và **Maynard** (cùng các cải tiến của Polymath); cận không điều kiện thường được nêu trong khóa học là **$$H=246$$**.
- Giải thích vì sao khoảng cách 2 vẫn nằm ngoài khả năng của các phương pháp sàng hiện nay (vấn đề chẵn lẻ, ở mức ý tưởng).
- Liên hệ cấu trúc chi tiết của số nguyên tố với bài [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) và bài [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/).
- Tránh lỗi phổ biến như "Zhang đã chứng minh giả thuyết sinh đôi".

**Kiến thức cần có.** Số nguyên tố; đồng dư cơ bản. Biết rằng mật độ của số nguyên tố gần $$x$$ vào khoảng $$1/\log x$$ sẽ giúp hiểu lập luận gần đúng.

**Kết nối trong khóa học.** Bạn nên đọc kèm [Maynard / Giải Fields]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/), [Euclid và vô hạn số nguyên tố]({{ site.baseurl }}/contents/vi/chapter05/05_02_Euclid_Infinite_Primes/) và [Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/).

---

## Bản đồ kiến thức nền: Lý thuyết sàng và Lý thuyết số cộng tính là gì?

Vì sao những câu hỏi trông cực kỳ đơn giản như số nguyên tố sinh đôi ($$p$$ và $$p+2$$) hay giả thuyết Goldbach (mọi số chẵn $$>2$$ là tổng hai số nguyên tố) lại khó hơn nhiều so với Định lý số nguyên tố? Hãy nhìn vào ba trụ cột đứng sau bài học:

### 1. Cuộc xung đột Phép nhân vs. Phép cộng
Số nguyên tố được định nghĩa hoàn toàn bằng **phép nhân** (không chia hết cho số nào ngoài 1 và chính nó). Nhưng cặp sinh đôi $$(p, p+2)$$ lại nối hai số nguyên tố bằng **phép cộng** ($$+2$$)! Khi bạn cộng 2 vào một số nguyên tố $$p$$, cấu trúc thừa số nguyên tố của $$p+2$$ bị xáo trộn hoàn toàn — đó là lý do mọi chứng minh thuần túy phép nhân kiểu Euclid đều bó tay.

### 2. Lý thuyết sàng (Sieve Theory)
Bạn từng học *Sàng Eratosthenes* thời tiểu học: viết các số từ $$2$$ đến $$N$$, gạch bỏ bội của 2, rồi bội của 3, bội của 5... những số còn sót lại là số nguyên tố. **Lý thuyết sàng hiện đại** biến trò gạch số đó thành một cỗ máy giải tích tinh vi: thay vì gạch từng số bằng tay, ta gán các **trọng số mượt mà** (như sàng Selberg hay sàng đa chiều Maynard) và dùng nguyên lý bù trừ để *ước lượng* có ít nhất bao nhiêu số nguyên tố (hoặc số có rất ít ước nguyên tố) lọt qua lưới lọc.

### 3. Phân bố trong cấp số cộng & Lý thuyết số cộng tính
Muốn sàng hoạt động chính xác, ta cần biết số nguyên tố phân bố đều đến đâu trong các lớp chia dư $$a \pmod q$$ (ví dụ các số chia 4 dư 1 so với chia 4 dư 3). Công cụ mạnh nhất không cần giả thiết chưa chứng minh là **Định lý Bombieri–Vinogradov** (mức phân bố trung bình $$\theta = 1/2$$), còn mơ ước mạnh hơn là **Giả thuyết Elliott–Halberstam** ($$\theta = 1$$).

**Ứng dụng thực tiễn:** Lý thuyết sàng là xương sống trực tiếp của các thuật toán phân tích thừa số nguyên tố nhanh nhất hiện nay (như *Sàng trường số* — Number Field Sieve), quyết định độ dài khóa an toàn của mật mã RSA trên toàn cầu.

---

## 1. Phát biểu

**Giả thuyết số nguyên tố sinh đôi.** Có vô hạn số nguyên tố $$p$$ sao cho $$p+2$$ cũng là số nguyên tố.

Nói cách khác: phương trình $$p'-p=2$$ có vô hạn nghiệm trong tập số nguyên tố.

Giả thuyết tổng quát hơn của **Polignac** dự đoán rằng mọi khoảng cách chẵn cố định $$2k$$ đều xuất hiện vô hạn lần giữa các cặp số nguyên tố. Sinh đôi là trường hợp $$k=1$$, khoảng cách chẵn nhỏ nhất có thể (hai số nguyên tố lẻ luôn cách nhau một số chẵn; khoảng cách lẻ chỉ xuất hiện duy nhất ở cặp $$(2,3)$$ vì 2 là số nguyên tố chẵn duy nhất).

**Euclid đã biết có vô hạn số nguyên tố**; chứng minh cổ điển xét $$N=p_1\cdots p_k+1$$ để buộc phải có một số nguyên tố mới không nằm trong danh sách hữu hạn ban đầu. Lập luận đó **không** tạo ra được cặp cách nhau 2. Có vô hạn "điểm" trên trục số không hề tự động kéo theo có vô hạn "cặp điểm sát nhau" — chẳng hạn tập các lũy thừa của 2 ($$2, 4, 8, 16, \ldots$$) có vô hạn phần tử nhưng khoảng cách giữa chúng lớn dần ra vô cùng!

---

### Video ngắn: Đếm cặp sinh đôi so với heuristic

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/twin-primes-count_vi.mp4"></video>
</div>

Lưới đánh dấu 8 cặp số nguyên tố sinh đôi dưới 100. Biểu đồ so số cặp sinh đôi thật tới $$x$$ (các chấm) với dự đoán Hardy–Littlewood (đường cong): 8169 so với khoảng 8248 tại $$x = 10^6$$. Khớp tốt là bằng chứng, chưa phải chứng minh.


### Tự tay thử: Tự đếm cặp số nguyên tố sinh đôi

<div class="mex-explainer" data-mex="twins" data-lang="vi"></div>


## 2. Lập luận gần đúng: vì sao người ta tin

### Ví dụ cầm tay chỉ việc 1: Tự tính hệ số Hardy–Littlewood từ xác suất đồng dư

Theo Định lý số nguyên tố, quanh mốc $$n$$, xác suất "ngẫu nhiên" để một số là nguyên tố vào khoảng $$1/\log n$$. Nếu $$n$$ và $$n+2$$ hoàn toàn độc lập với nhau như hai lần tung xúc xắc, xác suất để *cả hai* cùng nguyên tố sẽ là $$1/(\log n)^2$$. Nhưng chúng **tương quan mạnh** theo từng số nguyên tố nhỏ $$p$$ — hãy tự tay tính tỷ số (xác suất thật) / (xác suất độc lập) cho $$p = 2, 3, 5$$:

- **Tại $$p = 2$$:**
  - Nếu độc lập: xác suất $$n$$ không chia hết cho 2 là $$1/2$$, của $$n+2$$ cũng là $$1/2 \implies$$ tích $$= \frac{1}{2}\cdot\frac{1}{2} = \frac{1}{4}$$.
  - Thực tế: cứ hễ $$n$$ lẻ là $$n+2$$ *tự động* lẻ theo! Nên xác suất thật là $$\frac{1}{2}$$.
  - **Hệ số hiệu chỉnh tại $$p=2$$:** $$\frac{1/2}{1/4} = 2$$ (tăng gấp đôi!).
- **Tại $$p = 3$$:**
  - Nếu độc lập: $$\frac{2}{3} \cdot \frac{2}{3} = \frac{4}{9}$$.
  - Thực tế: trong 3 lớp dư $$\{0, 1, 2\} \pmod 3$$, nếu $$n \equiv 0$$ thì $$3 \mid n$$; nếu $$n \equiv 1$$ thì $$3 \mid (n+2)$$; chỉ duy nhất $$n \equiv 2 \pmod 3$$ thoát được (xác suất $$\frac{1}{3}$$).
  - **Hệ số hiệu chỉnh tại $$p=3$$:** $$\frac{1/3}{4/9} = \frac{3}{4} = 0{,}75$$.
- **Tại $$p = 5$$:**
  - Nếu độc lập: $$\frac{4}{5} \cdot \frac{4}{5} = \frac{16}{25}$$.
  - Thực tế: loại 2 lớp dư $$n \equiv 0$$ và $$n \equiv 3 \pmod 5$$, còn lại 3 lớp (xác suất $$\frac{3}{5}$$).
  - **Hệ số hiệu chỉnh tại $$p=5$$:** $$\frac{3/5}{16/25} = \frac{15}{16} = 0{,}9375$$.
- **Tổng quát với mọi số nguyên tố lẻ $$p$$:** Hệ số là $$\frac{p(p-2)}{(p-1)^2}$$.

Nhân thử mới chỉ 3 số đầu: $$2 \times \frac{3}{4} \times \frac{15}{16} \approx 1{,}406$$; nhân hết mọi số nguyên tố $$p$$ ta hội tụ về **hằng số số nguyên tố sinh đôi**:

$$
2C_2 = 2\prod_{p\ge 3}\frac{p(p-2)}{(p-1)^2} \approx 1{,}32032.
$$

Từ đó Hardy và Littlewood dự đoán số cặp sinh đôi không vượt quá $$x$$ là:

$$
\pi_2(x) \sim 2C_2 \int_2^x \frac{dt}{(\log t)^2}.
$$

**Kiểm chứng số thực tế:**
- Dưới $$100$$: có đúng 8 cặp thật là $$(3,5), (5,7), (11,13), (17,19), (29,31), (41,43), (59,61), (71,73)$$.
- Dưới $$10^6$$ (một triệu): có đúng **8.169** cặp thật, trong khi công thức tích phân cho **$$\approx 8.248$$** — sai số dưới 1%!

Vì chuỗi $$\sum_n \frac{1}{(\log n)^2}$$ **phân kỳ** ra vô cùng, mô hình dự đoán có vô hạn cặp sinh đôi. Lập luận gần đúng **không phải chứng minh**, nhưng nó khẳng định không có trở ngại đồng dư ẩn nào ngăn các cặp sinh đôi tiếp tục xuất hiện.

---

## 3. Vì sao phương pháp sàng khó bắt được đúng hai số nguyên tố

Phương pháp **sàng** rất giỏi tìm các **số gần nguyên tố** (số có rất ít thừa số nguyên tố, gọi là số $$P_r$$ nếu có tối đa $$r$$ thừa số). Nhưng khi cố ép sàng phân biệt *đúng* số nguyên tố (1 thừa số) với tích hai số nguyên tố (2 thừa số), ta đụng phải một bức tường nổi tiếng mang tên **vấn đề chẵn lẻ (parity problem)** do Atle Selberg phát hiện vào cuối thập niên 1940.

**Trực giác của vấn đề chẵn lẻ:** Một bộ sàng chỉ dùng thông tin "chia hết cho các số nguyên tố nhỏ" giống như một chiếc cân chỉ đo được tổng trọng lượng mà không phân biệt được chẵn hay lẻ số quả cân bên trong. Nói cụ thể hơn, bằng các công cụ sàng cổ điển, ta rất khó tách bạch tập các số có *số lẻ* thừa số nguyên tố (như số nguyên tố $$p$$, hay $$p_1 p_2 p_3$$) với tập các số có *số chẵn* thừa số nguyên tố (như tích hai số nguyên tố $$q_1 q_2$$).

Vì vậy, đỉnh cao mà sàng cổ điển chạm tới được là **định lý Chen (1966/1973)**: có vô hạn số nguyên tố $$p$$ sao cho $$p+2$$ là số nguyên tố *hoặc* tích của đúng hai số nguyên tố (ví dụ $$7 + 2 = 9 = 3 \times 3$$, hay $$13 + 2 = 15 = 3 \times 5$$). Kết quả này sát nút giả thuyết sinh đôi một cách đáng kinh ngạc, nhưng vẫn chưa gỡ bỏ được khả năng tích hai số nguyên tố!

Điều cần nhớ: **gần nguyên tố không phải là nguyên tố**; khoảng cách giữa "1 hoặc 2 thừa số" và "đúng 1 thừa số" có thể đòi hỏi cả một kỷ nguyên công cụ mới.

---

## 4. Khoảng cách bị chặn: Zhang, Maynard, Polymath

Nếu không thể chứng minh ngay $$p_{n+1} - p_n = 2$$ xảy ra vô hạn lần, các nhà toán học đặt câu hỏi lùi lại một bước nhưng vẫn vô cùng táo bạo: *có tồn tại một con số hữu hạn $$H$$ nào đó — dù là một triệu hay một tỷ — sao cho $$p_{n+1} - p_n \le H$$ xảy ra vô hạn lần không?*

### Ví dụ cầm tay chỉ việc 2: Kiểm tra "bộ chấp nhận được" bằng đồng dư nhỏ

Thay vì chỉ nhìn đúng 2 vị trí $$(n, n+2)$$, hãy nhìn một "chùm" $$k$$ vị trí $$\{n+h_1, n+h_2, \ldots, n+h_k\}$$. Bộ độ dịch $$\mathcal{H} = \{h_1, \ldots, h_k\}$$ gọi là **chấp nhận được (admissible)** nếu với *mọi* số nguyên tố $$p$$, các giá trị $$h_i \pmod p$$ **không phủ kín** tất cả $$p$$ lớp dư $$\{0, 1, \ldots, p-1\}$$. Hãy kiểm tra bằng tay hai bộ có $$k = 3$$:

1. **Thử bộ $$\{0, 2, 4\}$$ (tức $$\{n, n+2, n+4\}$$):**
   - Modulo $$2$$: $$\{0, 0, 0\}$$ → bỏ trống lớp dư $$1$$ (ổn).
   - Modulo $$3$$: $$\{0, 2, 1\}$$ → **phủ kín cả 3 lớp dư $$\{0, 1, 2\}$$!** Nghĩa là với *mọi* $$n$$, chắc chắn có 1 trong 3 số $$n, n+2, n+4$$ chia hết cho 3! Nên ngoài $$(3, 5, 7)$$, không bao giờ có bộ ba nguyên tố nào dạng này → **KHÔNG chấp nhận được**.
2. **Thử bộ $$\{0, 2, 6\}$$ (tức $$\{n, n+2, n+6\}$$):**
   - Modulo $$2$$: $$\{0, 0, 0\}$$ → bỏ trống dư $$1$$ (ổn).
   - Modulo $$3$$: $$\{0, 2, 0\}$$ → bỏ trống dư $$1$$ (ổn! Chỉ cần chọn $$n \equiv 2 \pmod 3$$ là thoát chia hết cho 3).
   - Với mọi $$p \ge 5$$: chỉ có 3 phần tử nên không bao giờ phủ kín nổi $$p \ge 5$$ lớp dư!
   - Kết luận: **CHẤP NHẬN ĐƯỢC!** Thử ngay với $$n \equiv 5 \pmod 6$$: $$n=5 \to (5,7,11)$$; $$n=11 \to (11,13,17)$$; $$n=17 \to (17,19,23)$$; $$n=101 \to (101,103,107)$$.

### Khung giải thích: Làm sao Zhang và Maynard "lách" qua rào cản chẵn lẻ để đạt $$H = 246$$? (nên đọc chậm)

Nếu phương pháp sàng bị khóa bởi rào cản chẵn lẻ, tại sao Zhang (2013) và Maynard (2013) vẫn chứng minh được có vô hạn cặp số nguyên tố cách nhau $$\le 246$$? Hãy theo dõi 4 bước sau:

#### Bước 1: Hạ yêu cầu từ "cả 2 số đều nguyên tố" xuống "ít nhất 2 trong $$k$$ số là nguyên tố"
Với một cặp $$(n, n+2)$$, rào cản chẵn lẻ ngăn ta chứng minh cả 2 cùng nguyên tố. Nhưng Goldston–Pintz–Yıldırım (GPY, 2005) nhận ra một mẹo thiên tài: nếu xét một **bộ chấp nhận được gồm $$k$$ số** $$\{n+h_1, \ldots, n+h_k\}$$ và ta gán trọng số không âm $$w(n) \ge 0$$ rồi chứng minh trung bình có trọng số của số lượng số nguyên tố trong chùm **lớn hơn 1**, tức:
$$
\sum_{n \sim X} w(n) \left( \sum_{i=1}^{k} \mathbf{1}_{\text{nguyên tố}}(n+h_i) - 1 \right) > 0,
$$
thì bắt buộc phải tồn tại vô hạn $$n$$ sao cho chùm đó chứa **ít nhất 2 số nguyên tố**! Và hai số nguyên tố ấy chắc chắn cách nhau không quá đường kính $$H = h_k - h_1$$ của chùm!

#### Bước 2: Bước đột phá của Yitang Zhang (2013)
Trọng số một chiều của GPY dừng lại ngay sát ngưỡng — nó chỉ thiếu đúng một chút xíu thông tin phân bố số nguyên tố trong cấp số cộng vượt qua mức $$\theta = 1/2$$ của Định lý Bombieri–Vinogradov. Năm 2013, **Yitang Zhang** chứng minh được một phiên bản mức phân bố $$\theta = \frac{1}{2} + \frac{1}{1168}$$ cho các môđun "trơn", đủ để tổng trọng số vượt ngưỡng $$1$$ khi chọn $$k = 3{,}5 \times 10^6$$ số → thu được:
$$
\liminf_{n\to\infty}(p_{n+1}-p_n) < 70{,}000{,}000.
$$

#### Bước 3: Cuộc cách mạng trọng số nhiều chiều của Maynard & Tao (2013)
Chỉ vài tháng sau, **James Maynard** (và độc lập là **Terence Tao**) nhận ra không cần phá ngưỡng Bombieri–Vinogradov cực khó của Zhang: chỉ cần thay trọng số 1 biến của GPY bằng **trọng số sàng nhiều chiều** (mỗi phần tử $$n+h_i$$ trong chùm có biến trọng số riêng) là tổng vượt ngưỡng $$1$$ ngay lập tức với $$k$$ rất nhỏ — thậm chí vượt qua mọi ngưỡng $$m$$ để chứng minh có vô hạn cụm gồm $$3, 4, 100$$ số nguyên tố trong khoảng bị chặn!

#### Bước 4: Tối ưu Polymath8b xuống $$H = 246$$ — và bức tường tại $$H = 2$$
Dự án cộng tác mở **Polymath8b** tối ưu hóa hàm trọng số của Maynard và tìm ra bộ chấp nhận được hẹp nhất gồm $$k = 50$$ vị trí có đường kính đúng **$$H = 246$$**, chốt kỷ lục không điều kiện hiện nay:
$$
\liminf_{n\to\infty}(p_{n+1}-p_n)\le 246.
$$
Ngay cả nếu giả sử Giả thuyết Elliott–Halberstam, phương pháp Maynard–Polymath kéo $$k$$ xuống còn 3 vị trí ($$H = 6$$), nhưng muốn kéo xuống $$k = 2$$ (tức $$H = 2$$, sinh đôi thật sự) thì trung bình có trọng số vẫn bị chặn cứng không vượt nổi 1 do chính **rào cản chẵn lẻ**!

Các công trình của Maynard về khoảng cách nhỏ, khoảng cách lớn và phương pháp sàng là một phần lý do ông nhận **Huy chương Fields năm 2022**. Xem bài [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/).

---

## 5. Những gì còn mở?

| Phát biểu | Tình trạng |
|-----------|------------|
| Có vô hạn số nguyên tố | **Đã chứng minh** (Euclid, …) |
| Có vô hạn cặp sinh đôi (khoảng cách = 2) | **Còn mở** |
| Có một khoảng cách chẵn bị chặn xuất hiện vô hạn lần | **Đã chứng minh** (Zhang / Maynard / Polymath) |
| $$\liminf(p_{n+1}-p_n)\le 246$$ | **Đã chứng minh** (cận tham chiếu) |
| Khoảng cách = 2 xuất hiện vô hạn lần | **Còn mở** |
| Định lý Chen ($$p+2$$ là số nguyên tố hoặc tích hai số nguyên tố) | **Đã chứng minh** |
| Công thức tiệm cận Hardy–Littlewood cho số cặp sinh đôi | **Còn mở** (giả thuyết) |
| Giả thuyết Polignac cho mọi $$2k$$ | **Còn mở** (sinh đôi là trường hợp $$k=1$$) |

**Khoảng cách bị chặn** cho thấy số nguyên tố tạo thành các cụm gần nhau vô hạn lần. **Giả thuyết sinh đôi** đòi hỏi cụm chặt nhất có thể. Từ 246 xuống 2 trông có vẻ nhỏ nếu chỉ nhìn con số, nhưng là cả một vực sâu về phương pháp. Đừng gộp hai dòng này khi thảo luận hay khi viết bài A3.

---

## 6. Toán học xung quanh bài toán (các công cụ chính)

- **Lý thuyết sàng:** sàng Selberg, sàng tổ hợp, GPY, trọng số Maynard.  
- **Số nguyên tố trong cấp số cộng:** định lý Bombieri–Vinogradov (về trung bình, mạnh ngang GRH); giả thuyết Elliott–Halberstam (phân bố mạnh hơn).  
- **Bộ chấp nhận được** và bài toán tối ưu đường kính (bộ $$k$$ phần tử có thể hẹp đến đâu mà vẫn chấp nhận được?).  
- **Lý thuyết số tính toán:** tìm các cặp sinh đôi lớn; so sánh lập luận gần đúng với dữ liệu.

Không cần thành thạo các công cụ này mới phát biểu đúng được giả thuyết, nhưng biết tên chúng giúp tránh ảo tưởng rằng "chỉ cần thử chia đến $$N$$ lớn".

Có thể làm toán "xung quanh" giả thuyết sinh đôi cả đời (sàng, phân bố, các cấu trúc) mà vẫn chưa chạm tới khoảng cách 2. Đó là đặc điểm bình thường của một bài toán mở lớn. RH ([Chương 1]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/)) kiểm soát sai số khi đếm số nguyên tố; giả thuyết sinh đôi hỏi về cấu trúc các cặp ở một khoảng cách cố định. Công cụ khác nhau, nhưng cùng một câu hỏi lớn: số nguyên tố được sắp xếp như thế nào.

---

## 7. Polignac, các bộ số nguyên tố, và bài thực hành với dữ liệu

**Giả thuyết de Polignac:** mọi số chẵn dương $$2k$$ đều xuất hiện vô hạn lần dưới dạng hiệu của hai số nguyên tố. Sinh đôi là trường hợp $$k=1$$. Các định lý về khoảng cách bị chặn cho thấy *ít nhất một* hiệu chẵn trong một tập chấp nhận được hữu hạn xuất hiện vô hạn lần, nhưng chưa xác định được hiệu đó bằng 2.

**Bộ số nguyên tố.** Tổng quát hơn: xét bộ $$n+h_1,\ldots,n+h_m$$ đồng thời là số nguyên tố, với các độ dịch $$h_i$$ chấp nhận được (không phủ hết mọi lớp thặng dư modulo một số nguyên tố nhỏ nào). Hardy–Littlewood dự đoán công thức tiệm cận cho số bộ như vậy. Định lý Green–Tao (có cấp số cộng dài tùy ý gồm toàn số nguyên tố) là một thành công rực rỡ khác, dựa nhiều vào tổ hợp cộng tính hơn là sàng thuần túy, nhưng cùng thuộc chủ đề "số nguyên tố chứa nhiều cấu trúc phong phú".

**Gợi ý khám phá dữ liệu (không bắt buộc):** đếm số cặp sinh đôi đến $$N$$ và so sánh với

$$
c\int_2^N\frac{dx}{(\log x)^2}
$$

(với hằng số số nguyên tố sinh đôi, hoặc chỉ so tỷ lệ thô). Mục tiêu là **rèn cách nhìn đúng về bằng chứng**, không phải "chứng minh bằng đồ thị". Tinh thần phân biệt kiểm tra và chứng minh này giống bài [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/).

---

## Hiểu lầm thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Zhang đã chứng minh giả thuyết sinh đôi." | Ông chứng minh có *một* khoảng cách bị chặn, không phải khoảng cách 2. |
| "Khoảng cách bị chặn cũng là sinh đôi." | Bị chặn nghĩa là $$\le H$$; sinh đôi cần $$H=2$$. |
| "Bảng số chỉ có hữu hạn cặp sinh đôi nên giả thuyết sai." | Bảng số luôn hữu hạn; giả thuyết nói về vô hạn. |
| "Lập luận của Euclid dễ dàng mở rộng cho sinh đôi." | $$N=P+1$$ không buộc có cặp cách nhau 2. |
| "Maynard đã giảm xuống 2." | Cận không điều kiện tham chiếu là khoảng 246; khoảng cách 2 vẫn còn mở. |
| "Định lý Chen chính là giả thuyết sinh đôi." | Định lý Chen cho phép $$p+2$$ là tích của hai số nguyên tố. |

---

## Từ các video: chuỗi sự kiện 2013–2014 tóm tắt

Các video của Numberphile (Zhang, Maynard), bài giảng của Maynard và bài viết của Quanta năm 2013 cho ta câu chuyện sau:

1. **GPY** dựng một khung sàng *sẽ* cho khoảng cách bị chặn nếu số nguyên tố phân bố trong cấp số cộng tốt hơn một chút so với định lý Bombieri–Vinogradov.  
2. **Zhang (2013)** chứng minh một mức phân bố yếu hơn nhưng đủ mạnh để có $$\liminf(p_{n+1}-p_n)\le 70{,}000{,}000$$ (sau đó Polymath tối ưu thêm).  
3. **Maynard (và Tao, độc lập)** cải tiến trọng số sàng nhiều chiều; cận giảm mạnh; Polymath đưa cận không điều kiện về **$$H=246$$**.  
4. **Vẫn còn mở:** khoảng cách $$2$$ (sinh đôi) và **rào cản chẵn lẻ**.

**Tình trạng (2026):** giả thuyết sinh đôi **còn mở**; khoảng cách bị chặn **đã được chứng minh**.

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Đánh giá: `research/video-research/Twin_Prime_Conjecture/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile, *Gaps between Primes*: [YouTube](https://www.youtube.com/watch?v=vkMXdShDdtY).  
2. **Cốt lõi (phổ thông)** — Numberphile, *Twin Prime Conjecture* (Maynard): [YouTube](https://www.youtube.com/watch?v=QKHKD8bRAro).  
3. **Bài giảng nghiên cứu** — Maynard, *Small Gaps Between Primes*: [YouTube](https://www.youtube.com/watch?v=E-W47F9upkU).  
4. **Bài viết** — Quanta (2013): [bài](https://www.quantamagazine.org/mathematicians-team-up-on-twin-primes-conjecture-20131119/).  
5. **Bài báo** — Maynard [arXiv:1311.4600](https://arxiv.org/abs/1311.4600).

**Sau khi xem:** khoảng cách bị chặn **đã được chứng minh**; giả thuyết sinh đôi ($$H=2$$) **còn mở**. Đừng viết "Zhang chứng minh giả thuyết sinh đôi".

---


### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/Twin_Prime_Conjecture/transcripts/` · trạng thái: `research/video-research/Twin_Prime_Conjecture/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Twin_Prime_Conjecture_vkMXdShDdtY_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu

Danh sách URL: `research/video-research/Twin_Prime_Conjecture/references.md`.

1. Zhang — bài về khoảng cách bị chặn (*Annals*, 2014).  
2. Maynard — [arXiv:1311.4600](https://arxiv.org/abs/1311.4600) · [bài tổng quan arXiv:1910.13450](https://arxiv.org/abs/1910.13450).  
3. Polymath8: http://bit.ly/polymath8  
4. Hardy–Littlewood; Wikipedia — [Twin prime](https://en.wikipedia.org/wiki/Twin_prime).  
5. Numberphile Zhang: https://www.youtube.com/watch?v=vkMXdShDdtY  
6. Numberphile Maynard: https://www.youtube.com/watch?v=QKHKD8bRAro  
7. Maynard colloquium: https://www.youtube.com/watch?v=E-W47F9upkU  
8. Quanta 2013: https://www.quantamagazine.org/mathematicians-team-up-on-twin-primes-conjecture-20131119/  
9. [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/), [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/), [Euclid]({{ site.baseurl }}/contents/vi/chapter05/05_02_Euclid_Infinite_Primes/). Bộ tư liệu: `research/video-research/Twin_Prime_Conjecture/`.

---

## Hướng đi tiếp

Có thể chọn làm đề tài cho bài **A3**. Bài thực hành: đếm số cặp sinh đôi đến $$N$$ và so sánh với lập luận gần đúng. Khi đọc bài Maynard, chú ý rằng Giải Fields ghi nhận *phương pháp*, không chỉ con số $$H$$. Bảng ở mục 5 là phần cốt lõi: hãy chỉ đúng những ô còn mở.

## Video tham khảo

- **Xem trước:** [Gaps between Primes - Numberphile](https://www.youtube.com/watch?v=vkMXdShDdtY) — Numberphile, tiếng Anh. Giới thiệu kết quả của Zhang về khoảng cách giữa các số nguyên tố; nên xem trước khi đọc bài.
- [Twin Prime Conjecture - Numberphile](https://www.youtube.com/watch?v=QKHKD8bRAro) — Numberphile, tiếng Anh. Maynard giải thích giả thuyết sinh đôi và các tiến bộ gần đây; nên xem sau khi đã nắm ý chính của bài.
- [Small Gaps Between Primes - James Maynard](https://www.youtube.com/watch?v=E-W47F9upkU) — princetonmathematics, tiếng Anh. Xem thêm sau hai video trên; bài giảng nghiên cứu có nhiều chi tiết kỹ thuật hơn.
