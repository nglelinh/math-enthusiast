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

**James Maynard** nhận **Huy chương Fields 2022** nhờ những đóng góp cho lý thuyết số giải tích, dẫn đến những tiến bộ lớn trong việc hiểu cấu trúc của các số nguyên tố và trong xấp xỉ Diophantine. Nếu Green–Tao hỏi về *cấp số cộng dài tùy ý trong tập số nguyên tố*, thì câu chuyện của Maynard hỏi *khoảng cách giữa hai số nguyên tố liên tiếp có thể nhỏ đến mức nào, với vô hạn lần*, và rộng hơn: những cấu hình tuyến tính nào xuất hiện vô hạn lần, khoảng cách có thể lớn đến đâu, và có số nguyên tố nào mà các chữ số bị hạn chế hay không. Đối tượng vẫn là số nguyên tố, nhưng công cụ là **phương pháp sàng** và **trọng số nhiều chiều**, chứ không phải nguyên lý chuyển của tổ hợp cộng tính.

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

## 1. Khoảng cách giữa các số nguyên tố: nhỏ, lớn và các "cấu hình"

Ký hiệu $$p_n$$ là số nguyên tố thứ $$n$$. **Khoảng cách liên tiếp** là

$$
g_n = p_{n+1}-p_n.
$$

Định lý số nguyên tố cho thấy khoảng cách "điển hình" ở gần $$x$$ có cỡ $$\log x$$: trung bình của $$g_n$$ tăng không bị chặn. Nhưng điều đó không ngăn được việc **thỉnh thoảng** có khoảng cách rất nhỏ, cũng không ngăn được việc **thỉnh thoảng** có khoảng cách rất lớn so với $$\log x$$.

Ba câu hỏi cổ điển:

1. **Nhỏ, với vô hạn lần.** Có hằng số $$C$$ sao cho $$g_n\le C$$ với vô hạn $$n$$ không? Đó là bài toán **khoảng cách bị chặn** (bounded gaps).
2. **Số nguyên tố sinh đôi.** Có vô hạn $$n$$ với $$g_n=2$$ không? Câu này mạnh hơn nhiều so với "chỉ cần bị chặn bởi *một hằng số nào đó*".
3. **Lớn.** $$g_n$$ có thể lớn đến mức nào so với $$\log p_n$$?

Ngoài ra, với một bộ độ dời cố định $$h_1<\cdots<h_k$$, có vô hạn $$n$$ sao cho $$n+h_1,\ldots,n+h_k$$ đều là số nguyên tố (hoặc gần nguyên tố theo nghĩa của phương pháp sàng) không? Số nguyên tố sinh đôi ứng với $$k=2$$, $$h_2-h_1=2$$. Khoảng cách bị chặn liên quan đến việc một hiệu $$h_j-h_i$$ nào đó xuất hiện vô hạn lần như khoảng cách giữa hai số nguyên tố.

**Một trực giác sai cần tránh.** "Số nguyên tố thưa dần" không có nghĩa là "khoảng cách liên tiếp luôn lớn". Thưa dần là một phát biểu về *trung bình*; các cụm số nguyên tố gần nhau vẫn có thể xuất hiện vô hạn lần.

---

## 2. Zhang năm 2013: liminf hữu hạn trở thành định lý

Năm 2013, **Yitang Zhang** chứng minh

$$
\liminf_{n\to\infty}(p_{n+1}-p_n) < \infty,
$$

với chặn tường minh ban đầu vào khoảng $$70$$ triệu:

$$
\liminf_{n\to\infty}(p_{n+1}-p_n) \le 70\,000\,000.
$$

Đó là lần đầu tiên có một định lý khẳng định: *có vô hạn cặp số nguyên tố cách nhau không quá một hằng số cố định*. Không cần giả thuyết Riemann. Không cần giả thuyết Elliott–Halberstam đầy đủ. Zhang dùng một dạng kết quả về phân bố của số nguyên tố trong cấp số cộng, với điều kiện trên môđun, kết hợp với khung sàng Goldston–Pintz–Yıldırım (GPY).

**Một bước ngoặt.** Từ lâu người ta đã biết: *nếu* có một giả thuyết phân bố đủ mạnh thì phương pháp GPY cho khoảng cách bị chặn. Zhang chỉ ra rằng *một phần* kết quả phân bố *đã chứng minh được* cũng đủ để đưa phương pháp sàng vượt qua ngưỡng.

Sau Zhang, dự án **Polymath** (một dự án hợp tác công khai, với Tao và nhiều người khác) nhanh chóng hạ chặn số xuống. Con số "246" (và các biến thể có điều kiện) trở thành một mốc dễ nhớ: một chặn hữu hạn tường minh, nhưng vẫn còn xa con số 2.

---

## 3. Maynard: khung sàng linh hoạt và trọng số nhiều chiều

**James Maynard**, gần như cùng lúc và theo một hướng độc lập, phát triển một biến thể **linh hoạt hơn** của phương pháp sàng, cũng cho khoảng cách bị chặn, và về nhiều mặt còn mở rộng khả năng phát hiện các chòm số nguyên tố.

### 3.1. Ý tưởng GPY

Để "bắt" được nhiều số nguyên tố trong bộ $$n+h_1,\ldots,n+h_k$$, người ta không chỉ đếm bằng hàm chỉ thị của số nguyên tố. Thay vào đó, ta xây dựng các **trọng số không âm** $$w_n$$ sao cho tổng trọng số lớn trên miền $$n\sim N$$, nhưng nếu quá nhiều số $$n+h_j$$ là hợp số (chia hết cho số nguyên tố nhỏ) thì trọng số bị **sàng** cho nhỏ đi.

Nếu sau khi sàng, số trung bình các số "gần nguyên tố" trong một chòm vẫn vượt quá một ngưỡng, thì không thể mọi chòm đều chứa nhiều nhất một số nguyên tố; do đó phải có chòm chứa *ít nhất hai* số nguyên tố. Hai số nguyên tố trong một chòm có độ dời bị chặn cho ta một khoảng cách bị chặn.

### 3.2. Trọng số nhiều chiều

Maynard tối ưu hóa trọng số trên **nhiều dạng tuyến tính cùng lúc**, với một cấu trúc nhiều chiều gắn với các thành phần của chòm. So với GPY cổ điển, khung này cho phép phát hiện các cấu hình với giả thiết phân bố yếu hơn trong một số trường hợp, dễ điều chỉnh theo từng bài toán, và mở đường cho các kết quả mạnh hơn về việc có nhiều số nguyên tố trong một khoảng ngắn.

<div class="textbook-theorem" markdown="1">
**Định lý (tóm tắt; Zhang–Maynard và cộng đồng).** Tồn tại một hằng số tuyệt đối $$C$$ (hiện nay có thể lấy khá nhỏ nhờ tối ưu bằng số) sao cho

$$
\liminf_{n\to\infty}(p_{n+1}-p_n)\le C.
$$
</div>

### 3.3. Ghi nhận công lao đúng

| Vai trò | Nội dung |
|---------|----------|
| Zhang (2013) | Lần đầu chứng minh khoảng cách bị chặn mà không cần giả thiết, với chặn tường minh |
| Maynard | Khung sàng độc lập, linh hoạt; nhiều mở rộng |
| Tao / Polymath / nhiều tác giả | Hạ chặn số, các cải tiến và biến thể |
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

**Khoảng cách lớn.** Từ lâu người ta đã chứng minh các kết quả dạng

$$
\limsup_{n\to\infty}\frac{p_{n+1}-p_n}{\log p_n}=\infty
$$

và các chặn mạnh hơn (Ford–Green–Konyagin–Maynard–Tao và những người đi trước). Ý tưởng thô: dùng giai thừa hoặc một hệ thặng dư để tạo ra một dãy dài các hợp số, rồi tinh chỉnh để khoảng trống đó xuất hiện gần một số nguyên tố lớn. Maynard đóng góp bằng các kỹ thuật sàng và tổ hợp trên hệ thặng dư tinh tế hơn nhiều so với cách dùng $$m!$$ đơn giản. "Thỉnh thoảng rất gần" và "thỉnh thoảng rất xa" không mâu thuẫn: đó là hai chế độ khác nhau của $$g_n$$.

**Chữ số bị hạn chế.** Có vô hạn số nguyên tố trong các tập mà chữ số bị hạn chế (các định lý của Maynard). Một tập "mỏng" khi viết trong hệ thập phân vẫn có thể đủ dày theo nghĩa của phương pháp sàng để chứa vô hạn số nguyên tố; đây là ví dụ cho thấy tầm với của các phương pháp sàng hiện đại, vượt ra ngoài các khoảng số nguyên liên tiếp.

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

**Giới hạn.** Giả thuyết số nguyên tố sinh đôi vẫn còn mở. Chặn số có thể còn được cải thiện, nhưng để đi từ vài trăm xuống 2 có thể cần những ý tưởng mới về bản chất. Kết quả này không giải giả thuyết Riemann.

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
