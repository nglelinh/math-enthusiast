---
layout: post
title: "Công trình của Maynard về Số nguyên tố (Huy chương Fields 2022)"
chapter: '02'
order: 9
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Dãy số nguyên tố càng đi xa càng thưa dần — ở vùng gần $$10^{100}$$, trung bình phải đi qua hàng trăm số tự nhiên mới gặp lại một số nguyên tố. Thế nhưng thỉnh thoảng, hai số nguyên tố vẫn đứng sát rạt cạnh nhau, chỉ cách nhau đúng $$2$$ đơn vị: $$(3, 5)$$, $$(11, 13)$$, $$(29, 31)$$, $$(101, 103)$$, và thậm chí ở tận vùng hàng trăm nghìn chữ số! Liệu những cặp "số nguyên tố sinh đôi" như thế có xuất hiện mãi mãi không?

Đó là một trong những câu hỏi cổ xưa và bướng bỉnh nhất của toán học. Suốt hàng thế kỷ, các nhà toán học thậm chí không chứng minh nổi rằng tồn tại *một hằng số hữu hạn nào đó* — dù là một tỉ! — sao cho có vô hạn cặp số nguyên tố cách nhau không quá hằng số ấy. Rồi mùa xuân năm 2013, bức tường ấy bất ngờ nứt toác khi Yitang Zhang đưa ra mốc 70 triệu; và chỉ vài tháng sau, một nghiên cứu sinh sau tiến sĩ trẻ tuổi tên là **James Maynard** (cùng lúc với Terence Tao) đã giới thiệu một chiếc sàng tinh gọn và mạnh mẽ đến mức kéo sập mốc ấy xuống chỉ còn vài trăm, đồng thời mở khóa hàng loạt bài toán khác về cấu trúc của số nguyên tố: khoảng cách cực lớn, số nguyên tố không chứa chữ số 7, hay xấp xỉ Diophantine.

Chính sự linh hoạt và chiều sâu ấy đã mang về cho **James Maynard** tấm **Huy chương Fields 2022**. Nếu Green–Tao tìm kiếm những *cấp số cộng dài tùy ý* bằng tổ hợp cộng tính, thì Maynard lại đi theo con đường cổ điển nhưng được làm mới ngoạn mục của **lý thuyết số giải tích** và **phương pháp sàng nhiều chiều**.

Bài này dành cho người đã biết sơ lược định lý số nguyên tố, và muốn hiểu *vì sao* kết quả về khoảng cách bị chặn là một đột phá, *vì sao* nó vẫn yếu hơn giả thuyết số nguyên tố sinh đôi, và Maynard đứng *ở đâu* trong cộng đồng Zhang–Tao–Polymath.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu định lý về khoảng cách bị chặn của Zhang–Maynard bằng ngôn ngữ $$\liminf$$, và nói được ý nghĩa của một chặn tường minh.
- Giải thích vì sao **phương pháp sàng** là công cụ tự nhiên để tìm số nguyên tố trong các dạng tuyến tính $$n+h_1,\ldots,n+h_k$$.
- Phân biệt **khoảng cách bị chặn** với **giả thuyết số nguyên tố sinh đôi** và với **định lý Green–Tao**.
- Mô tả sơ lược ý tưởng **trọng số nhiều chiều** (từ GPY đến Maynard).
- Nêu thêm hai hướng khác trong các công trình của Maynard: **khoảng cách lớn** và **số nguyên tố có chữ số bị hạn chế**.
- Ghi nhận công lao đúng: Zhang năm 2013; Maynard độc lập; cộng đồng hạ dần chặn số; Huy chương Fields 2022 cho cả một loạt công trình.

**Kiến thức cần có.** Số nguyên tố; định lý số nguyên tố $$\pi(x)\sim x/\log x$$; sàng Eratosthenes; khoảng cách $$p_{n+1}-p_n$$.

**Liên hệ với khóa học.** Đọc cùng [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) để so sánh tổ hợp cộng tính với phương pháp sàng; [Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) chỉ đóng vai trò bối cảnh về phân bố, vì kết quả khoảng cách bị chặn cổ điển không giả sử RH.

---

## Bản đồ kiến thức nền: Lý thuyết số giải tích và Phương pháp sàng (Sieve Theory)

Để hiểu "chiếc sàng" của Maynard khác gì với cách tìm số nguyên tố ở trường phổ thông, hãy nhìn vào bản chất của lĩnh vực này:

- **Lý thuyết số giải tích (Analytic Number Theory) nghiên cứu gì?** Dùng các công cụ của giải tích (tích phân, ước lượng tiệm cận, chuỗi vô hạn, hàm phức) để trả lời các câu hỏi về số nguyên — nhất là sự phân bố của số nguyên tố. Vì ta không có "công thức đóng" sinh ra số nguyên tố thứ $$n$$, nhà toán học nghiên cứu chúng qua các **trung bình** và **xấp xỉ thống kê**.
- **Phương pháp sàng (Sieve Theory) là gì?** Mọi người đều biết *sàng Eratosthenes*: muốn tìm số nguyên tố, ta gạch bỏ bội của 2, rồi bội của 3, rồi bội của 5... Nhưng nếu thử đếm chính xác còn lại bao nhiêu số bằng nguyên lý bù trừ (cộng–trừ theo từng ước), số lượng số hạng sai số phình lên nhanh theo hàm mũ và phá hỏng mọi ước lượng! **Phương pháp sàng hiện đại** (từ Brun, Selberg đến GPY và Maynard) giải quyết điều đó bằng cách thay phép đếm cứng nhắc ($$0$$ hoặc $$1$$) bằng các **trọng số mượt** $$w_n \ge 0$$: gán điểm cao cho những số *ít khả năng chia hết cho các số nguyên tố nhỏ*, rồi chứng minh tổng số điểm ấy đủ lớn để đảm bảo có số nguyên tố thật sự lọt qua sàng.
- **Ví dụ nhỏ về "chòm chấp nhận được" (admissible tuple):** Muốn tìm nhiều số nguyên tố nằm sát nhau dạng $$n + h_1, \dots, n + h_k$$, ta không thể chọn bừa độ dời! Ví dụ bộ 3 số $$(n, n+2, n+4)$$ luôn có **ít nhất một số chia hết cho 3** (vì $$0, 2, 4$$ phủ kín mọi số dư modulo 3), nên bộ này chỉ có đúng một lần toàn nguyên tố là $$(3, 5, 7)$$ rồi hết! Trái lại, bộ $$(n, n+2, n+6)$$ tránh được modulo 2 (chỉ toàn số lẻ nếu $$n$$ lẻ) và tránh được modulo 3 (bỏ trống số dư $$1 \pmod 3$$ khi $$n \equiv 5 \pmod 6$$), nên nó **chấp nhận được** — ví dụ $$(5, 7, 11)$$, $$(11, 13, 17)$$, $$(17, 19, 23)$$. Chiếc sàng của Maynard tìm kiếm ít nhất hai (hoặc thậm chí $$m$$) số nguyên tố nằm trong một chòm chấp nhận được đủ lớn!

---

## 1. Khoảng cách giữa các số nguyên tố: nhỏ, lớn và các "cấu hình"

Ký hiệu $$p_n$$ là số nguyên tố thứ $$n$$. **Khoảng cách liên tiếp** là

$$
g_n = p_{n+1}-p_n.
$$

Định lý số nguyên tố cho thấy khoảng cách "điển hình" ở gần $$x$$ có cỡ $$\log x$$: trung bình của $$g_n$$ tăng không bị chặn. Nhưng điều đó không ngăn được việc **thỉnh thoảng** có khoảng cách rất nhỏ, cũng không ngăn được việc **thỉnh thoảng** có khoảng cách rất lớn so với $$\log x$$.

Ba câu hỏi cổ điển:

1. **Nhỏ, với vô hạn lần.** Có hằng số $$C$$ sao cho $$g_n\le C$$ với vô hạn $$n$$ không? Đó là bài toán **khoảng cách bị chặn** (*bounded gaps*).
2. **Số nguyên tố sinh đôi.** Có vô hạn $$n$$ với $$g_n=2$$ không? Câu này mạnh hơn nhiều so với "chỉ cần bị chặn bởi *một hằng số nào đó*".
3. **Lớn.** $$g_n$$ có thể lớn đến mức nào so với $$\log p_n$$?

Ngoài ra, với một bộ độ dời cố định chấp nhận được $$h_1<\cdots<h_k$$, có vô hạn $$n$$ sao cho $$n+h_1,\ldots,n+h_k$$ đều là số nguyên tố (giả thuyết chòm nguyên tố Hardy–Littlewood) hoặc chứa ít nhất $$m$$ số nguyên tố không? Số nguyên tố sinh đôi ứng với $$k=2$$, $$h_2-h_1=2$$. Khoảng cách bị chặn liên quan đến việc một hiệu $$h_j-h_i$$ nào đó xuất hiện vô hạn lần như khoảng cách giữa hai số nguyên tố.

**Một trực giác sai cần tránh.** "Số nguyên tố thưa dần" không có nghĩa là "khoảng cách liên tiếp luôn lớn". Thưa dần là một phát biểu về *trung bình*; các cụm số nguyên tố gần nhau vẫn có thể xuất hiện vô hạn lần.

---

## 2. Zhang năm 2013: liminf hữu hạn trở thành định lý

Năm 2013, **Yitang Zhang** — lúc đó là một giảng viên ít tên tuổi tại Đại học New Hampshire — gây chấn động toàn thế giới khi chứng minh

$$
\liminf_{n\to\infty}(p_{n+1}-p_n) < \infty,
$$

với chặn tường minh ban đầu là $$70$$ triệu:

$$
\liminf_{n\to\infty}(p_{n+1}-p_n) \le 70\,000\,000.
$$

Đó là lần đầu tiên có một định lý khẳng định: *có vô hạn cặp số nguyên tố cách nhau không quá một hằng số cố định*. Không cần giả thuyết Riemann. Không cần giả thuyết Elliott–Halberstam đầy đủ. Zhang dùng một dạng kết quả tinh vi về phân bố của số nguyên tố trong cấp số cộng (đánh bại ngưỡng Bombieri–Vinogradov $$1/2$$ đối với các môđun trơn), kết hợp với khung sàng Goldston–Pintz–Yıldırım (GPY).

**Một bước ngoặt.** Từ lâu người ta đã biết: *nếu* có một giả thuyết phân bố đủ mạnh thì phương pháp GPY cho khoảng cách bị chặn. Zhang chỉ ra rằng *một phần* kết quả phân bố *đã chứng minh được* cũng đủ để đưa phương pháp sàng vượt qua ngưỡng.

Sau Zhang, dự án **Polymath8** (một dự án hợp tác công khai trực tuyến, với Tao và nhiều nhà toán học khác) nhanh chóng hạ chặn số xuống từ 70 triệu xuống vài nghìn, rồi sau đột phá của Maynard xuống còn **246** (một chặn hữu hạn tường minh vô điều kiện, dù vẫn còn xa con số 2).

---

## 3. Maynard: khung sàng linh hoạt và trọng số nhiều chiều

**James Maynard**, gần như cùng lúc (và độc lập với Tao), phát triển một biến thể **đơn giản hơn nhưng mạnh hơn hẳn** của phương pháp sàng: không cần dùng đến kết quả cực khó của Zhang về môđun trơn, mà chỉ cần định lý cổ điển Bombieri–Vinogradov từ thập niên 1960 vẫn thu được khoảng cách bị chặn (ban đầu là $$600$$)!

### 3.1. Ý tưởng GPY

Để "bắt" được nhiều số nguyên tố trong bộ $$n+h_1,\ldots,n+h_k$$, người ta không chỉ đếm bằng hàm chỉ thị của số nguyên tố. Thay vào đó, ta xây dựng các **trọng số không âm** $$w_n$$ sao cho tổng trọng số lớn trên miền $$n\sim N$$, nhưng nếu quá nhiều số $$n+h_j$$ là hợp số (chia hết cho số nguyên tố nhỏ) thì trọng số bị **sàng** cho nhỏ đi.

Nếu sau khi sàng, tỉ số giữa "tổng có trọng số của số nguyên tố trong chòm" và "tổng trọng số" vượt quá $$1$$:

$$
\frac{\sum_{n} \left(\sum_{j=1}^k \mathbf{1}_{\mathbb{P}}(n+h_j)\right) w_n}{\sum_n w_n} > 1,
$$

thì theo nguyên lý Dirichlet (trung bình lớn hơn 1), phải tồn tại vô hạn $$n$$ mà trong chòm $$n+h_1, \dots, n+h_k$$ có **ít nhất hai** số nguyên tố! Hai số nguyên tố nằm cùng một chòm có đường kính $$h_k - h_1$$ lập tức cho ta khoảng cách bị chặn $$\le h_k - h_1$$.

### 3.2. Trọng số nhiều chiều

Trong GPY cổ điển, trọng số $$w_n$$ chỉ phụ thuộc vào **một biến duy nhất** là tích $$d_1 d_2 \cdots d_k$$ của các ước của từng số hạng $$n + h_j$$. Điểm thiên tài của Maynard là nhận ra sự ràng buộc 1 chiều đó quá chật chội: ông cho trọng số phụ thuộc vào **một hàm mượt $$k$$ biến độc lập** $$F(t_1, \dots, t_k)$$ theo từng ước $$d_1, \dots, d_k$$ riêng biệt! Nhờ không gian tự do nhiều chiều đó, bài toán cực đại hóa tỉ số ở trên trở thành một bài toán biến phân cổ điển trên đơn hình $$k$$ chiều — và bất ngờ là giá trị tối ưu tăng theo cỡ $$\log k$$ khi $$k \to \infty$$! Điều này không chỉ cho khoảng cách bị chặn giữa **2** số nguyên tố, mà chứng minh rằng với mọi số nguyên $$m \ge 2$$ (ví dụ $$m = 100$$), có vô hạn khoảng có độ dài bị chặn chứa ít nhất $$m$$ số nguyên tố!

<div class="textbook-theorem" markdown="1">
**Định lý (tóm tắt; Zhang–Maynard và cộng đồng).** Tồn tại một hằng số tuyệt đối $$C$$ (hiện nay có thể lấy $$C = 246$$ nhờ tối ưu bằng số) sao cho

$$
\liminf_{n\to\infty}(p_{n+1}-p_n)\le C.
$$
</div>

### 3.3. Ghi nhận công lao đúng

| Vai trò | Nội dung |
|---------|----------|
| Zhang (2013) | Lần đầu chứng minh khoảng cách bị chặn mà không cần giả thiết, với chặn tường minh |
| Maynard | Khung sàng trọng số nhiều chiều độc lập, linh hoạt; nhiều mở rộng ($$m$$ số nguyên tố trong khoảng ngắn) |
| Tao / Polymath / nhiều tác giả | Hạ chặn số xuống 246, các cải tiến và biến thể |
| Fields 2022 | Nhiều công trình: khoảng cách nhỏ, khoảng cách lớn, chữ số bị hạn chế, xấp xỉ Diophantine… |

Đừng viết "một mình Maynard phát hiện ra khoảng cách bị chặn".

---

## 4. Phương pháp sàng "phát hiện" điều gì?

**Sàng Eratosthenes** loại bỏ các hợp số. **Các phương pháp sàng hiện đại** (Selberg, Brun, GPY, Maynard…) thường không liệt kê mọi số nguyên tố; chúng **ước lượng** số lượng số nguyên tố (hoặc gần nguyên tố) trong một họ, bằng cách cân bằng giữa phần còn lại sau khi loại các số chia hết cho số nguyên tố nhỏ và sai số trong phân bố theo cấp số cộng.

Hãy hình dung $$k$$ "ô" $$n+h_j$$. Ta muốn biết có bao nhiêu lần *ít nhất hai ô* cùng là số nguyên tố. Ta gán trọng số "thưởng" khi các ô có vẻ không chia hết cho số nguyên tố nhỏ nào, rồi chứng minh rằng phần thưởng trung bình quá lớn so với giả định "mỗi chòm có nhiều nhất một số nguyên tố". Đó là một **phép phản chứng định lượng**, không phải thuật toán tìm cặp số nguyên tố.

Phương pháp sàng cho ta **sự tồn tại của vô hạn** đối tượng theo nghĩa trung bình; hiếm khi cho một công thức sinh ra các cặp. Khoảng cách bị chặn là một định lý về cấu trúc, không phải một cách sinh ra các cặp $$p$$ và $$p+C$$.

---

## 5. Khoảng cách lớn và số nguyên tố có chữ số bị hạn chế

Các công trình được giải Fields của Maynard không dừng ở khoảng cách nhỏ.

**Khoảng cách lớn.** Từ lâu người ta đã biết có những khoảng trống rất dài không chứa số nguyên tố nào — ví dụ đơn giản nhất là dãy $$(m+1)! + 2, (m+1)! + 3, \dots, (m+1)! + (m+1)$$ gồm $$m$$ hợp số liên tiếp. Nhưng so với độ lớn của $$p_n$$, khoảng trống đó vẫn nhỏ. Câu hỏi khó của Erdős (có treo thưởng 10.000 USD!) là tìm chặn dưới sắc hơn cho

$$
\limsup_{n\to\infty}\frac{p_{n+1}-p_n}{\log p_n}=\infty.
$$

Maynard (độc lập, và sau đó cùng Ford–Green–Konyagin–Tao) đã phá vỡ kỷ lục tồn tại gần 80 năm và giải trọn bài toán treo thưởng của Erdős bằng các kỹ thuật sàng và phủ hệ thặng dư tinh tế. "Thỉnh thoảng rất gần" và "thỉnh thoảng rất xa" không mâu thuẫn: đó là hai mặt cực trị của cùng một dãy $$g_n$$.

**Chữ số bị hạn chế.** Có vô hạn số nguyên tố mà trong cách viết thập phân **không hề chứa chữ số 7** (hay bất kỳ chữ số cấm nào cho trước)! Tập các số nguyên không chứa chữ số 7 cực kỳ mỏng (trong đoạn tới $$10^k$$ chỉ có $$9^k$$ số, tức mật độ cỡ $$N^{0{,}954}/N \to 0$$). Bằng cách kết hợp giải tích Fourier (phương pháp đường tròn) với phương pháp sàng, Maynard chứng minh tập mỏng ấy vẫn chứa vô hạn số nguyên tố.

Ngoài ra, cùng với **Dimitris Koukoulopoulos**, Maynard còn chứng minh **giả thuyết Duffin–Schaeffer** (1941) — một bài toán nền tảng tồn tại gần 80 năm trong lý thuyết **xấp xỉ Diophantine** (hỏi khi nào hầu hết số thực đều xấp xỉ tốt được bằng phân số rút gọn $$a/q$$ với sai số cho trước).

---

## 6. So sánh với Green–Tao

| | Green–Tao | Zhang–Maynard (khoảng cách bị chặn) |
|--|-----------|------------------------------|
| Câu hỏi | Cấp số cộng độ dài $$k$$ tùy ý trong tập số nguyên tố | $$p_{n+1}-p_n$$ bị chặn với vô hạn $$n$$ |
| Công cụ | Định lý Szemerédi tương đối + hàm trội + nguyên lý chuyển | Sàng GPY/Maynard + phân bố trong cấp số cộng |
| Số nguyên tố sinh đôi | Không giải được khoảng cách = 2 | Không giải được khoảng cách = 2; chỉ có khoảng cách ≤ $$C$$ |

Cả hai đều cho thấy số nguyên tố có cấu trúc. Một bên là cấu trúc cộng tính trải dài; một bên là các cụm cục bộ. Xem [bài Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/).

---

## 7. Vì sao quan trọng (và giới hạn)

**Tầm quan trọng.** Biến một câu hỏi dễ phát biểu về số nguyên tố thành định lý có chặn tường minh; biến phương pháp sàng thành công cụ có thể lắp ghép và dùng lại; bổ sung cho Green–Tao bằng một công cụ khác; gắn lý thuyết số giải tích với mô hình hợp tác Polymath.

**Giới hạn.** Giả thuyết số nguyên tố sinh đôi vẫn còn mở. Do "rào cản chẵn lẻ" (*parity barrier*) cố hữu của phương pháp sàng — chiếc sàng khó phân biệt số nguyên tố (1 thừa số) với tích của hai số nguyên tố lớn (2 thừa số) — việc đi từ $$246$$ xuống $$2$$ đòi hỏi những ý tưởng mới về bản chất. Kết quả này cũng không giải giả thuyết Riemann.

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|-----|
| "Khoảng cách bị chặn chính là số nguyên tố sinh đôi." | Sai | Giả thuyết sinh đôi đòi hỏi khoảng cách bằng 2 xuất hiện vô hạn lần. |
| "Một mình Maynard phát hiện ra khoảng cách bị chặn." | Sai | Zhang năm 2013; Maynard độc lập; sau đó là cả cộng đồng. |
| "Định lý số nguyên tố cấm khoảng cách nhỏ." | Sai | Nó kiểm soát trung bình, không cấm các cụm cục bộ. |
| "Phương pháp sàng là thuật toán liệt kê các cặp." | Sai | Đó là công cụ ước lượng để chứng minh tồn tại, không phải cách sinh ra các cặp. |
| "Định lý Green–Tao đã bao gồm khoảng cách bị chặn." | Sai | Cấp số cộng dài không tự cho khoảng cách liên tiếp bị chặn bởi một hằng số nhỏ. |
| "Giải Fields 2022 chỉ nhờ một bất đẳng thức về khoảng cách." | Sai | Giải ghi nhận nhiều công trình, rộng hơn một định lý về khoảng cách. |

---

## Bài tập

1. Viết phát biểu dạng $$\liminf$$ cho khoảng cách giữa các số nguyên tố liên tiếp, và giải thích vì sao liminf hữu hạn mạnh hơn "có một lần khoảng cách nhỏ".
2. Vì sao khoảng cách ≤ 246 yếu hơn giả thuyết sinh đôi? Viết một câu đúng và một câu phóng đại sai.
3. Phương pháp sàng "phát hiện" điều gì? Viết không quá 120 từ, không dùng ký hiệu; rồi viết một đoạn có dùng chòm $$n+h_j$$.
4. Lập bảng so sánh Green–Tao (cấp số cộng) với Maynard (khoảng cách): câu hỏi, công cụ, liên hệ với số nguyên tố sinh đôi.
5. Đọc lướt một bài tổng quan về khoảng cách bị chặn; liệt kê ba người có đóng góp ngoài Zhang và Maynard.
6. **Đọc tài liệu nghiên cứu.** Viết một phát biểu về khoảng cách lớn (dạng limsup) và giải thích vì sao nó không mâu thuẫn với khoảng cách bị chặn.
7. **Thảo luận.** Trong 3 phút: nếu giả thuyết Elliott–Halberstam đầy đủ được chứng minh, kết quả khoảng cách bị chặn sẽ được cải thiện thế nào (nói sơ lược)?

---


## Nguồn video (bộ tư liệu nghiên cứu video)

Chi tiết: `research/video-research/Maynard_Primes/`.

**Thứ tự xem gợi ý**

1. **Định hướng** — Numberphile *Twin Prime Conjecture* (Maynard): [YouTube](https://www.youtube.com/watch?v=QKHKD8bRAro).  
2. **Lịch sử** — Numberphile *Gaps between Primes*: [YouTube](https://www.youtube.com/watch?v=vkMXdShDdtY).  
3. **Cốt lõi** — Maynard, *Patterns in prime numbers*: [YouTube](https://www.youtube.com/watch?v=ey_57qWhGEM).  
4. **Về giải thưởng** — video của Simons về Maynard nhận giải Fields: [link](https://www.simonsfoundation.org/2022/07/05/fields-medal-video-james-maynard/).

**Nhắc lại:** khoảng cách bị chặn **đã được chứng minh**; giả thuyết số nguyên tố sinh đôi vẫn **còn mở**.

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Maynard_Primes/transcripts/` · trạng thái: `research/video-research/Maynard_Primes/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Maynard_Primes_QKHKD8bRAro_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Maynard_Primes/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=QKHKD8bRAro  
2. https://www.youtube.com/watch?v=vkMXdShDdtY  
3. https://www.youtube.com/watch?v=D4_sNKoO-RA  
4. https://www.youtube.com/watch?v=ey_57qWhGEM  
5. https://www.simonsfoundation.org/2022/07/05/fields-medal-video-james-maynard/  
6. https://arxiv.org/abs/1311.4600  
7. https://arxiv.org/pdf/1311.4600  
8. https://arxiv.org/abs/1412.5029  
9. https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/laudatio-jm.pdf  
10. https://www.quantamagazine.org/number-theorist-james-maynard-wins-the-fields-medal-20220705/  
11. https://www.numberphile.com/videos/twin-prime-conjecture  
12. https://en.wikipedia.org/wiki/Twin_prime  
13. https://en.wikipedia.org/wiki/James_Maynard_(mathematician)  
14. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022  
15. https://www.youtube.com/watch?v=eupAXdWPvX8  

### Bộ tư liệu nghiên cứu

16. Bộ tư liệu của khóa học: `research/video-research/Maynard_Primes/`.

1. IMU, Huy chương Fields 2022 — James Maynard.
2. Y. Zhang, *Bounded gaps between primes* (2013).
3. J. Maynard — khoảng cách nhỏ, trọng số nhiều chiều; khoảng cách lớn; số nguyên tố có chữ số bị hạn chế.
4. Goldston–Pintz–Yıldırım — khung GPY.
5. Polymath8; blog và các bài tổng hợp của T. Tao.
6. Bài tổng quan nhập môn về phương pháp sàng (Selberg; các phương pháp sàng hiện đại).
7. Trong khóa học: [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/), [Tổng quan Chương 2]({{ site.baseurl }}/contents/vi/chapter02/).

---

## Hướng đi tiếp

- Đọc phần giới thiệu về **sàng Selberg** và các trọng số dạng bình phương trước khi học GPY/Maynard.
- Tìm hiểu **Polymath** như một mô hình hợp tác trong lý thuyết số giải tích.
- So sánh ý "cấu trúc và ngẫu nhiên" với bài [Tổ hợp và Hình học Hiện đại]({{ site.baseurl }}/contents/vi/chapter02/02_11_Modern_Combinatorics_Geometry/).
- Xấp xỉ Diophantine trong các công trình của Maynard: hãy tìm một bài tổng quan riêng, đừng gộp nhầm vào một định lý về khoảng cách.

## Video tham khảo

- **Xem trước:** [Twin Prime Conjecture - Numberphile](https://www.youtube.com/watch?v=QKHKD8bRAro) — Numberphile, tiếng Anh. Maynard giải thích giả thuyết số nguyên tố sinh đôi và khoảng cách bị chặn; nên xem trước khi đọc bài.
- [Gaps between Primes - Numberphile](https://www.youtube.com/watch?v=vkMXdShDdtY) — Numberphile, tiếng Anh. Lịch sử bài toán khoảng cách giữa các số nguyên tố; nên xem sau khi đã nắm ý chính của bài.
- [James Maynard - Patterns in prime numbers](https://www.youtube.com/watch?v=ey_57qWhGEM) — G-Research, tiếng Anh. Xem thêm sau hai video trên; bài giảng của Maynard về các cấu hình trong tập số nguyên tố.
