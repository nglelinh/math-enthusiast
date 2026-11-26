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

Đó là một trong những câu hỏi cổ xưa và bướng bỉnh nhất của toán học. Suốt hàng thế kỷ, các nhà toán học thậm chí không chứng minh nổi rằng tồn tại *một hằng số hữu hạn nào đó* — dù là một tỉ! — sao cho có vô hạn cặp số nguyên tố cách nhau không quá hằng số ấy. Rồi mùa xuân năm 2013, bức tường ấy bất ngờ nứt toác khi Yitang Zhang đưa ra mốc 70 triệu; và chỉ vài tháng sau, một nghiên cứu sinh sau tiến sĩ trẻ tuổi tên là **James Maynard** (cùng lúc với Terence Tao) đã giới thiệu một chiếc sàng tinh gọn và mạnh mẽ đến mức kéo sập mốc ấy xuống chỉ còn vài trăm, đồng thời mở khóa hàng loạt bài toán khác về cấu trúc của số nguyên tố: khoảng cách cực lớn, số nguyên tố không chứa chữ số 7, và giả thuyết Duffin–Schaeffer trong xấp xỉ Diophantine.

Chính sự sắc bén và linh hoạt ấy đã mang về cho **James Maynard** tấm **Huy chương Fields 2022**.

**Mạch bài học:** Kiến thức cần nhớ (phương pháp sàng, kiểm tra tay chòm chấp nhận được, nguyên lý Dirichlet có trọng số) → Đột phá Zhang (2013) → Giải thích 4 bước: trọng số sàng nhiều chiều của Maynard và bài toán cực trị trên đơn hình → Khoảng cách lớn, chữ số bị hạn chế & Duffin–Schaeffer → So sánh với Green–Tao.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu định lý về khoảng cách bị chặn của Zhang–Maynard bằng ngôn ngữ $$\liminf$$ và tự kiểm tra bằng tay điều kiện **chòm chấp nhận được**.
- Giải thích vì sao **phương pháp sàng** hiện đại dùng trọng số mượt $$w_n \ge 0$$ thay cho phép đếm bù trừ cứng nhắc.
- Hiểu mạch 4 bước của **trọng số nhiều chiều Maynard**: vì sao nâng hàm trọng số từ 1 biến (GPY) lên $$k$$ biến độc lập lại cho phép bắt được $$m$$ số nguyên tố tùy ý trong một khoảng ngắn.
- Phân biệt **khoảng cách bị chặn** với **giả thuyết số nguyên tố sinh đôi** và với **định lý Green–Tao**.
- Nêu thêm các hướng nổi bật khác của Maynard: **khoảng cách lớn**, **số nguyên tố có chữ số bị hạn chế**, và **giả thuyết Duffin–Schaeffer**.

**Kiến thức cần có.** Số nguyên tố, phép chia lấy dư modulo $$p$$, sàng Eratosthenes và định lý số nguyên tố $$\pi(x) \sim x/\ln x$$.

**Liên hệ với khóa học.** Đọc cùng [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) để so sánh tổ hợp cộng tính với phương pháp sàng; [Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) chỉ đóng vai trò bối cảnh về phân bố, vì kết quả khoảng cách bị chặn cổ điển không giả sử RH.

---

## Kiến thức cần nhớ: Lý thuyết số giải tích và Phương pháp sàng (Sieve Theory)

### 1. Lý thuyết số giải tích & Phương pháp sàng nghiên cứu gì?
Vì không có công thức đóng sinh ra số nguyên tố thứ $$n$$, **lý thuyết số giải tích** dùng công cụ giải tích (tích phân, ước lượng tiệm cận, biến đổi Fourier) để nghiên cứu phân bố trung bình của số nguyên tố. Trong đó, **phương pháp sàng** (*sieve theory*) phát triển từ ý tưởng cổ điển của Eratosthenes (gạch bỏ bội của $$2, 3, 5, \dots$$).

Nhưng nếu dùng nguyên lý bù trừ (cộng–trừ từng ước nguyên tố $$\le \sqrt{N}$$) để đếm số nguyên tố còn sót lại, số hạng sai số phình lên thành $$2^{\pi(\sqrt{N})}$$ — lớn hơn cả $$N$$ và nuốt chửng số hạng chính! Các phương pháp sàng hiện đại (Brun, Selberg, GPY, Maynard) thay việc đếm cứng nhắc bằng các **trọng số mượt không âm $$w_n \ge 0$$** (thường viết dạng bình phương $$w_n = (\sum \lambda_d)^2$$ để tự động không âm!) và chấp nhận chỉ sàng các ước nhỏ hơn một ngưỡng $$R = N^{\theta/2}$$.

### 2. Chòm chấp nhận được (Admissible Tuple) — Ví dụ cầm tay tự kiểm tra
Muốn tìm nhiều số nguyên tố cùng lúc trong một chòm tuyến tính $$n + h_1, \dots, n + h_k$$, ta không thể chọn bừa độ dời $$(h_1, \dots, h_k)$$:
- **Ví dụ bị loại — Bộ $$(n, n+2, n+4)$$:** Xét theo modulo $$3$$, ba độ dời $$0, 2, 4$$ cho đủ cả ba số dư $$0, 2, 1 \pmod 3$$! Do đó với mọi $$n$$, một trong ba số bắt buộc chia hết cho $$3$$. Bộ này chỉ có đúng một lần toàn nguyên tố là $$(3, 5, 7)$$ rồi không bao giờ lặp lại nữa!
- **Ví dụ hợp lệ — Bộ $$(n, n+2, n+6)$$:**
  - Theo modulo $$2$$: độ dời $$0, 2, 6$$ đều chẵn (chỉ chiếm 1/2 số dư → tránh bội của 2 khi $$n$$ lẻ).
  - Theo modulo $$3$$: độ dời $$0, 2, 6 \equiv 0, 2, 0 \pmod 3$$ (chỉ chiếm 2/3 số dư → tránh bội của 3 khi $$n \equiv 2 \pmod 3$$, tức $$n \equiv 5 \pmod 6$$!).
  - Theo mọi $$p \ge 5$$: chỉ có 3 số hạng nên không thể phủ hết $$p$$ số dư!
  - Kết quả: $$(n, n+2, n+6)$$ là **chòm chấp nhận được** — kiểm tra ngay vài giá trị: $$(5, 7, 11)$$, $$(11, 13, 17)$$, $$(17, 19, 23)$$, $$(41, 43, 47)$$.

### 3. Bất đẳng thức Dirichlet có trọng số
Cho một chòm chấp nhận được $$k$$ phần tử $$(h_1, \dots, h_k)$$ và các trọng số không âm $$w_n \ge 0$$. Nếu ta chứng minh được:

$$
S \;=\; \sum_{N \le n < 2N} \left(\sum_{j=1}^k \mathbf{1}_{\mathbb{P}}(n + h_j) - (m - 1)\right) w_n \;>\; 0,
$$

thì **bắt buộc tồn tại ít nhất một $$n \in [N, 2N)$$** sao cho trong chòm $$n+h_1, \dots, n+h_k$$ có **ít nhất $$m$$ số nguyên tố**! (Vì nếu mọi $$n$$ đều có $$\le m - 1$$ số nguyên tố thì mọi số hạng trong tổng đều $$\le 0$$, mâu thuẫn với $$S > 0$$!) Đặt $$m = 2$$, hai số nguyên tố trong cùng chòm cách nhau không quá đường kính $$h_k - h_1$$ — lập tức cho ta **khoảng cách bị chặn**!

---


### Video ngắn 1: Khoảng cách bị chặn giữa các Số nguyên tố (70 triệu → 246)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/maynard-bounded-gaps_vi.mp4"></video>
</div>

Video dài khoảng 1 phút 9 giây (có thuyết minh tiếng Việt): hành trình từ Yitang Zhang (70 triệu) đến sàng đa chiều Maynard (600) và Polymath8b (246), cụm m số nguyên tố bất kỳ và rào cản chẵn lẻ.

## 1. Khoảng cách giữa các số nguyên tố và cột mốc Zhang (2013)

Ký hiệu $$p_n$$ là số nguyên tố thứ $$n$$ và $$g_n = p_{n+1} - p_n$$. Theo Định lý số nguyên tố, khoảng cách trung bình quanh $$x$$ là $$\ln x \to \infty$$, nhưng trung bình lớn không hề cấm việc thỉnh thoảng hai số nguyên tố đứng cực sát nhau!

Năm 2013, **Yitang Zhang** lần đầu tiên trong lịch sử chứng minh vô điều kiện:

$$
\liminf_{n\to\infty}(p_{n+1}-p_n) \;\le\; 70\,000\,000.
$$

Trước đó, Goldston–Pintz–Yıldırım (GPY, 2005) đã chứng minh khung sàng của họ nằm ngay sát mép vạch đích: chỉ cần số nguyên tố phân bố đều trong cấp số cộng với môđun vượt qua ngưỡng **$$1/2$$** (định lý Bombieri–Vinogradov cổ điển đạt đúng $$1/2$$!) là ra khoảng cách bị chặn. Zhang đã làm điều tưởng bất khả thi: vượt qua ngưỡng $$1/2$$ đối với các môđun *trơn* (không có ước nguyên tố lớn), mở tung cánh cửa bị khóa suốt hàng trăm năm.

---

## 2. Giải thích: Trọng số nhiều chiều của Maynard tạo nên bước nhảy vọt như thế nào?

Chỉ vài tháng sau Zhang, **James Maynard** (và độc lập là Terence Tao) đã khiến giới toán học sững sờ khi không cần đến phần chứng minh siêu khó về môđun trơn của Zhang mà chỉ dùng đúng **Định lý Bombieri–Vinogradov (1965)** đã có sẵn — vừa hạ chặn từ 70 triệu xuống 600 (rồi Polymath8 kéo xuống **246**), vừa chứng minh được tồn tại vô hạn khoảng ngắn chứa **$$m$$ số nguyên tố** với mọi $$m \ge 2$$! Hãy đọc chậm 4 bước cốt lõi:

#### Bước 1: Chỉ ra nút thắt 1 chiều của sàng GPY cổ điển
Trong sàng GPY (2005), trọng số $$w_n$$ có dạng bình phương phụ thuộc vào **một biến duy nhất** là tích $$d_1 d_2 \cdots d_k$$ của các ước $$d_j \mid (n + h_j)$$:

$$
w_n^{\text{GPY}} = \left(\sum_{d \mid \prod (n+h_j)} \lambda_d\right)^2.
$$

Vì chỉ nhìn thấy tích chung $$d = d_1\cdots d_k$$ chứ không phân biệt được ước thuộc về số hạng $$n+h_j$$ nào, tỉ số tối đa $$M_k$$ giữa "phần nguyên tố" và "tổng trọng số" bị **chặn cứng bởi hằng số $$4$$** dù ta chọn chòm dài $$k$$ lớn đến mấy! Do đó GPY không thể vượt ngưỡng khi mức phân bố chỉ là $$\theta = 1/2$$ (vì $$4 \times \frac{1}{2} / 2 = 1$$ — chạm đúng vạch chứ không vượt qua $$1$$!).

#### Bước 2: Giải phóng trọng số thành hàm $$k$$ biến độc lập (Sàng Maynard–Tao)
Ý tưởng thiên tài của Maynard là cho hệ số sàng phụ thuộc vào **từng ước riêng biệt** $$(d_1, \dots, d_k)$$ thông qua một hàm mượt $$k$$ biến $$F(t_1, \dots, t_k)$$ xác định trên đơn hình $$\Delta_k = \{t_i \ge 0 : \sum_{i=1}^k t_i \le 1\}$$:

$$
w_n^{\text{Maynard}} = \left(\sum_{\substack{d_i \mid (n+h_i) \\ d_1 \cdots d_k < R}} \mu(d_1)\cdots \mu(d_k)\, F\!\left(\frac{\ln d_1}{\ln R}, \dots, \frac{\ln d_k}{\ln R}\right)\right)^2.
$$

#### Bước 3: Quy bài toán số học về bài toán cực trị giải tích trên đơn hình $$k$$ chiều
Áp dụng định lý Bombieri–Vinogradov (mức phân bố $$\theta = 1/2$$), Maynard tính được tường minh tỉ số giữa tử và mẫu của bất đẳng thức Dirichlet qua hai tích phân $$k$$ chiều của hàm $$F$$! Bài toán số nguyên tố bỗng biến thành bài toán biến phân thuần túy: chọn hàm $$F$$ trên đơn hình $$\Delta_k$$ để cực đại hóa tỉ số $$M_k = \sup_F \frac{\sum_{j=1}^k J_k^{(j)}(F)}{I_k(F)}$$.

#### Bước 4: Phép màu tăng theo $$\ln k$$ — Bắt được $$m$$ số nguyên tố bất kỳ!
Maynard chọn một hàm thử cực kỳ khéo léo (dạng tích đối xứng) và chứng minh:

$$
M_k \;>\; \ln k - 2\ln\ln k - 2 \;\xrightarrow{k \to \infty}\; \infty!
$$

Thay vì bị kẹt ở $$4$$ như GPY, $$M_k$$ **tiến ra vô cực** khi $$k$$ lớn! Do đó với **mọi** số nguyên $$m \ge 2$$ (dù $$m = 2$$ hay $$m = 1000$$), chỉ cần chọn chòm chấp nhận được đủ dài $$k$$ sao cho $$\frac{\theta}{2} M_k > m - 1$$, ta lập tức có vô hạn khoảng có độ dài bị chặn chứa ít nhất $$m$$ số nguyên tố!

<div class="textbook-theorem" markdown="1">
**Định lý (Zhang 2013; Maynard 2013; Polymath8).**  
1. Tồn tại hằng số $$C = 246$$ sao cho $$\liminf_{n\to\infty}(p_{n+1}-p_n) \le 246$$.  
2. (Maynard–Tao) Với mọi $$m \ge 2$$, tồn tại hằng số $$C_m$$ sao cho $$\liminf_{n\to\infty}(p_{n+m-1} - p_n) \le C_m$$.
</div>

Tóm tắt mạch chứng minh:

$$
\text{Chòm } (n+h_1,\dots,n+h_k)
\;\xrightarrow{\text{Trọng số } k \text{ biến } F}\;
\text{Tích phân trên đơn hình } \Delta_k
\;\xrightarrow{M_k \sim \ln k \to \infty}\;
\liminf (p_{n+m-1}-p_n) \le C_m.
$$

---


### Video ngắn 2: Sàng đa chiều Maynard–Tao vượt nút thắt GPY 1 chiều

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/maynard-multidim-sieve_vi.mp4"></video>
</div>

Video dài khoảng 55 giây (có thuyết minh tiếng Việt): chòm chấp nhận được (0, 2, 6), nút thắt phân bố 1/2 của sàng GPY 1 chiều và trọng số hàm trơn k biến trên đơn hình.

## 3. Không chỉ khoảng cách nhỏ: Khoảng cách lớn, Chữ số bị hạn chế và Duffin–Schaeffer

Huy chương Fields 2022 ghi nhận hàng loạt đỉnh cao khác của Maynard:

- **Khoảng cách lớn (giải bài toán treo thưởng 10.000 USD của Erdős):** Dễ tạo ra $$m$$ hợp số liên tiếp bằng $$(m+1)! + 2, \dots, (m+1)! + (m+1)$$, nhưng tìm khoảng trống cực lớn so với $$\ln p_n$$ là bài toán cực khó. Maynard (độc lập, và cùng Ford–Green–Konyagin–Tao) đã phá vỡ kỷ lục tồn tại gần 80 năm cho $$\limsup \frac{p_{n+1} - p_n}{\ln p_n}$$.
- **Số nguyên tố có chữ số bị hạn chế:** Chứng minh có **vô hạn số nguyên tố không chứa chữ số 7** (hay bất kỳ chữ số cấm nào trong hệ thập phân)! Dù tập các số không chứa chữ số 7 cực mỏng (mật độ cỡ $$N^{0{,}954}/N \to 0$$), Maynard kết hợp phương pháp đường tròn Fourier với phương pháp sàng để chứng minh nó vẫn chứa vô hạn số nguyên tố.
- **Giả thuyết Duffin–Schaeffer (cùng Dimitris Koukoulopoulos, 2019):** Giải quyết bài toán mở gần 80 năm trong lý thuyết **xấp xỉ Diophantine** bằng công cụ đồ thị và lý thuyết số giải tích.

### Ghi nhận công lao và so sánh với Green–Tao

| | Green–Tao | Zhang–Maynard (khoảng cách bị chặn) |
|--|-----------|------------------------------|
| Câu hỏi | Cấp số cộng độ dài $$k$$ tùy ý trong tập số nguyên tố | $$p_{n+1}-p_n$$ bị chặn với vô hạn $$n$$ |
| Công cụ | Định lý Szemerédi tương đối + hàm trội + nguyên lý chuyển | Sàng đa chiều Maynard + phân bố trong cấp số cộng |
| Số nguyên tố sinh đôi | Không giải được khoảng cách = 2 | Không giải được khoảng cách = 2 (do rào cản chẵn lẻ của sàng) |

**Giới hạn cần nhớ:** Do **rào cản chẵn lẻ** (*parity barrier*) cố hữu của phương pháp sàng — chiếc sàng khó phân biệt số nguyên tố (1 thừa số nguyên tố) với tích của hai số nguyên tố lớn (2 thừa số) — việc đi từ $$246$$ xuống $$2$$ (giả thuyết số nguyên tố sinh đôi) vẫn đòi hỏi những ý tưởng hoàn toàn mới.

---


### Video ngắn 3: Vô hạn Số nguyên tố không chứa chữ số 7

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/maynard-missing-digits_vi.mp4"></video>
</div>

Video dài khoảng 1 phút 1 giây (có thuyết minh tiếng Việt): định lý Maynard (2019) về số nguyên tố thiếu chữ số trong hệ thập phân, phân tích Fourier trên chữ số và mở rộng phương pháp vòng tròn.

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|---------|
| "Khoảng cách bị chặn chính là số nguyên tố sinh đôi." | Sai | Giả thuyết sinh đôi đòi hỏi khoảng cách bằng 2 xuất hiện vô hạn lần. |
| "Một mình Maynard phát hiện ra khoảng cách bị chặn." | Sai | Zhang chứng minh đầu tiên năm 2013; Maynard (và Tao) đưa ra sàng đa chiều độc lập sau đó; Polymath8 hạ chặn xuống 246. |
| "Định lý số nguyên tố cấm khoảng cách nhỏ." | Sai | Nó kiểm soát trung bình $$\ln x$$, không cấm các cụm cục bộ. |
| "Phương pháp sàng là thuật toán liệt kê các cặp." | Sai | Đó là công cụ ước lượng trung bình để chứng minh tồn tại. |
| "Định lý Green–Tao đã bao gồm khoảng cách bị chặn." | Sai | Cấp số cộng dài cho phép công sai $$d$$ lớn tùy ý, không chặn khoảng cách liên tiếp. |
| "Giải Fields 2022 chỉ nhờ một bất đẳng thức về khoảng cách." | Sai | Giải ghi nhận cả khoảng cách lớn, chữ số bị hạn chế và giả thuyết Duffin–Schaeffer. |

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
