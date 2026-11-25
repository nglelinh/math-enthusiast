---
layout: post
title: "Giả thuyết Collatz"
chapter: '01'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
lesson_type: required
---

Hãy chơi một trò chơi số học chỉ gồm đúng hai dòng luật: chọn một số nguyên dương bất kỳ; nếu là số chẵn thì chia đôi, nếu là số lẻ thì nhân ba rồi cộng một. Cứ lặp đi lặp lại mãi.

Thử với số $$6$$: $$6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$$ — êm ả rơi về số 1 sau 8 bước. Bây giờ thử số $$27$$ xem sao! Thay vì đi xuống ngay, số $$27$$ nhỏ bé bỗng vọt lên $$82 \to 41 \to 124 \to \cdots$$, leo điên cuồng lên tận đỉnh **9.232** như một hạt mưa đá bị cuốn lên xuống trong đám mây giông, rồi mới chịu rơi dần về số 1 sau đúng **111 bước**! Câu hỏi mang tên **Giả thuyết Collatz** (hay bài toán $$3x+1$$) chỉ hỏi một điều duy nhất: *có phải mọi số nguyên dương, không trừ một số nào, cuối cùng đều rơi vào vòng lặp $$4 \to 2 \to 1$$ hay không?*

Nghe như một bài tập lớp 3, nhưng nó là chiếc bẫy khét tiếng nhất của toán học hiện đại. Người ta kể rằng nhà toán học huyền thoại Paul Erdős từng lắc đầu cảnh báo: *"Toán học có lẽ vẫn chưa sẵn sàng cho những bài toán như thế này"*; còn Jeffrey Lagarias thì ví nó như một căn bệnh dễ lây trong giới nghiên cứu vì ai cũng tưởng mình sắp giải được.

Trong khóa Math Enthusiast, Collatz đóng hai vai trò thú vị: ở trang Chương 1 này, nó là **ví dụ mẫu kinh điển về một bài toán mở sơ cấp**, giúp bạn phân biệt sắc nét giữa bằng chứng tính toán và chứng minh toán học; còn ở [bài thực hành Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/), nó là sân chơi mặc định cho bài **A5**, nơi bạn làm thí nghiệm số học có phương pháp (chứ không phải đi "chứng minh Collatz trong hồ sơ học tập").

**Mạch bài học:** Kiến thức cần nhớ → quy tắc & ví dụ tính tay quỹ đạo $$N=7, 9$$ → thời gian dừng → kiểm tra so với chứng minh → phép tính kỳ vọng lực hút $$3/4$$ & chu trình âm $$-5$$ → ánh xạ Syracuse → khung giải thích chậm định lý Tao (2019) → vì sao khó & hiểu lầm thường gặp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu ánh xạ Collatz $$T$$ và giả thuyết rằng mọi số nguyên dương đều rơi vào chu trình $$4\to 2\to 1$$.
- Tính quỹ đạo và **thời gian dừng toàn phần** (total stopping time) cho các số ban đầu nhỏ; mô tả kiểu dao động "lên xuống" điển hình.
- Giải thích vì sao việc máy tính kiểm tra đến những số cực lớn chỉ là **bằng chứng**, không phải chứng minh.
- Kể một loại kết quả từng phần: lập luận xác suất gần đúng; mật độ của tập các số về được 1; các ràng buộc về chu trình; bài tổng quan của Lagarias để bắt đầu đọc.
- Phát biểu ngắn gọn **định lý "hầu hết" của Tao (2019)** và giải thích vì sao nó **không** phải chứng minh đầy đủ giả thuyết Collatz.
- Phân biệt ánh xạ chuẩn $$T$$ với dạng **rút gọn / Syracuse** khi so sánh các nguồn tài liệu.
- Dùng Collatz làm đề tài **A5** mà không tuyên bố đã giải được; phân biệt trang Chương 1 (giải thích) với bài thực hành Chương 7 (thí nghiệm).
- Tránh các lỗi phổ biến như "đã kiểm tra đến $$10^{20}$$ nên đúng", "Tao đã giải Collatz", "dãy số là ngẫu nhiên", hay tin đồn trên mạng về việc bác bỏ giả thuyết.

**Kiến thức cần có.** Số nguyên và tính chẵn lẻ. Không cần giải tích; chỉ cần quen với việc lặp lại một phép toán và đọc đồ thị là đủ cho bài thực hành.

**Kết nối trong khóa học.** Bài này đi liền với [Bài thực hành về phép lặp Collatz]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/), đối chiếu bài học "kiểm tra không phải chứng minh" với [Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/), và so sánh về độ sơ cấp lẫn độ sâu với [Số nguyên tố sinh đôi]({{ site.baseurl }}/contents/vi/chapter01/01_06_Twin_Prime_Conjecture/).

---

## Kiến thức cần nhớ: Hệ động lực rời rạc, Lý thuyết Ergodic và Số học $$p$$-adic là gì?

Collatz phát biểu bằng số học tiểu học, nhưng muốn hiểu những kết quả nghiên cứu sâu nhất về nó, bạn cần nhìn thấy ba trụ cột toán học đứng phía sau:

### 1. Hệ động lực rời rạc (Discrete Dynamical Systems)
Ở đại học, bạn từng gặp các dãy truy hồi tuyến tính (như dãy Fibonacci) hay xích Markov. **Hệ động lực rời rạc** tổng quát hóa ý tưởng đó: cho một tập trạng thái $$X$$ và một ánh xạ $$f: X \to X$$, ta lặp $$x_{k+1} = f(x_k)$$ và hỏi về **số phận dài hạn** của quỹ đạo: nó hội tụ về điểm bất động, rơi vào chu trình tuần hoàn, chạy ra vô cùng, hay hỗn loạn nhạy cảm với điều kiện đầu?

### 2. Lý thuyết Ergodic & Hai kiểu "mật độ" xác suất
Khi không thể theo dõi *từng* quỹ đạo riêng lẻ, các nhà toán học chuyển sang hỏi về hành vi của **"hầu hết mọi quỹ đạo"**. Để đo tỷ lệ của một tập con $$A \subset \mathbb{N}$$, có hai thước đo phổ biến:
- **Mật độ tự nhiên:** $$\lim_{X\to\infty} \frac{\#(A \cap [1,X])}{X}$$ (đếm đều mọi số từ 1 đến $$X$$).
- **Mật độ logarit:** $$\lim_{X\to\infty} \frac{1}{\log X}\sum_{n \in A,\, n \le X} \frac{1}{n}$$ (gán trọng số $$1/n$$ — thước đo mà Terence Tao đã dùng năm 2019!).

### 3. Sự xung đột cơ số 2 và cơ số 3 (Số học $$2$$-adic / $$3$$-adic)
Phép chia $$n/2$$ cực kỳ "hiền" trong hệ nhị phân (chỉ dịch bỏ một số 0 ở cuối), còn phép $$3n+1$$ lại gắn với cấu trúc chia dư theo lũy thừa của $$3$$ (vành $$\mathbb{Z}/3^k\mathbb{Z}$$). Sự pha trộn giữa cấu trúc nhị phân và tam phân phá hủy hầu hết các bất biến đại số thông thường — đây cũng là nguồn gốc các ứng dụng của hệ động lực rời rạc trong **bộ sinh số giả ngẫu nhiên, lý thuyết hỗn độn (chaos) và bài toán dừng (halting problem)** trong khoa học máy tính.

---

## 1. Quy tắc

Với số nguyên dương $$n$$, đặt

$$
T(n) =
\begin{cases}
n/2 & \text{nếu } n \text{ chẵn},\\
3n+1 & \text{nếu } n \text{ lẻ}.
\end{cases}
$$

Lặp lại: $$n,\; T(n),\; T(T(n)),\; \ldots$$

**Ví dụ.** $$6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1 \to 4 \to \cdots$$

**Giả thuyết Collatz.** Mọi số nguyên dương sau một số bước đều đi vào chu trình $$4 \to 2 \to 1$$.

Có những phát biểu tương đương nói về việc đi đến số 1, hoặc về việc chu trình duy nhất trong các số dương là chu trình tầm thường (tùy theo dùng ánh xạ $$3n+1$$ đầy đủ hay ánh xạ rút gọn, trong đó các bước chia 2 được gộp lại).

**Nhiều tên gọi, một bài toán.** Bài toán $$3x+1$$, Syracuse, Ulam, Kakutani, Thwaites, Hasse thường đều chỉ cùng một câu chuyện cổ điển về số dương; nhưng luôn cần kiểm tra chính xác ánh xạ được dùng.

**Ký hiệu trong nghiên cứu.** $$\operatorname{Col}_{\min}(N)=\inf_{k\ge 0}T^{k}(N)$$; giả thuyết nói rằng $$\operatorname{Col}_{\min}(N)=1$$ với mọi $$N$$ dương (theo cách viết trong bài giảng của Tao).

**Thời gian dừng.** *Thời gian dừng toàn phần* của $$n$$ thường được hiểu là số bước cho đến khi chạm 1 (hoặc vào chu trình tầm thường); hãy cố định định nghĩa chính xác một lần trong báo cáo A5 của bạn. *Thời gian dừng* đôi khi lại chỉ số bước cho đến khi có một giá trị nhỏ hơn $$n$$. Hãy dùng thuật ngữ nhất quán trong toàn bộ hồ sơ học tập.

**Số ban đầu 27.** Quỹ đạo của 27 nổi tiếng vì leo lên tận 9.232 rồi mới về 1 sau 111 bước (theo ánh xạ $$T$$). Trong khi đó, hai người hàng xóm ngay cạnh nó là $$26$$ (10 bước) và $$28$$ (18 bước) lại rơi về 1 cực nhanh! Hiện tượng "số nhỏ mà đi cực xa, hàng xóm sát nhau mà số phận khác hẳn" là trực quan đầu tiên khiến ta thấy bài toán không hề đơn giản.

---

### Video ngắn: Quỹ đạo Collatz của số 97 leo lên 9232 rồi mới rơi về 1 sau 118 bước

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/collatz-orbit-97_vi.mp4"></video>
</div>

Hãy theo dõi quỹ đạo Collatz của số 97: nó leo lên 9232 rồi mới rơi về 1 sau 118 bước. Sự đi xuống cuối cùng không nhất thiết đơn điệu, và chưa ai chứng minh được điều đó đúng với mọi số bắt đầu.


### Tự tay thử: Theo dõi quỹ đạo Collatz bất kỳ

<div class="mex-explainer" data-mex="collatz" data-lang="vi"></div>


## 2. Quỹ đạo, thời gian dừng và thời gian dừng toàn phần

Cố định số ban đầu $$n$$. **Quỹ đạo** là dãy vô hạn $$n, T(n), T^2(n),\ldots$$. Phần lớn nghiên cứu về Collatz là để hiểu các quỹ đạo: chúng leo cao đến đâu, đi lòng vòng bao lâu, có vào chu trình khác không, có tiến ra vô cùng không.

Hai đại lượng cổ điển dùng để ghi chép:

- **Thời gian dừng (stopping time)** của $$n$$: bước đầu tiên $$k$$ mà $$T^k(n) < n$$ (đo xem mất bao lâu dãy mới "chịu thấp hơn" điểm xuất phát).
- **Thời gian dừng toàn phần (total stopping time)** của $$n$$: bước đầu tiên chạm $$1$$.

### Ví dụ làm từng bước 1: Tính chi tiết quỹ đạo và hai thời gian dừng cho $$n = 7$$ và $$n = 9$$

- **Với $$n = 7$$:**
  $$
  7 \xrightarrow{1} 22 \xrightarrow{2} 11 \xrightarrow{3} 34 \xrightarrow{4} 17 \xrightarrow{5} 52 \xrightarrow{6} 26 \xrightarrow{7} 13 \xrightarrow{8} 40 \xrightarrow{9} 20 \xrightarrow{10} 10 \xrightarrow{11} \mathbf{5} \xrightarrow{12} 16 \xrightarrow{13} 8 \xrightarrow{14} 4 \xrightarrow{15} 2 \xrightarrow{16} \mathbf{1}.
  $$
  - Đỉnh cao nhất đạt được: **52**.
  - **Thời gian dừng** = **11** (tại bước 11 chạm $$5 < 7$$ lần đầu tiên).
  - **Thời gian dừng toàn phần** = **16** (tại bước 16 chạm $$1$$).
- **Với $$n = 9$$:**
  $$
  9 \xrightarrow{1} 28 \xrightarrow{2} 14 \xrightarrow{3} \mathbf{7} \to \cdots \xrightarrow{19} \mathbf{1}.
  $$
  - **Thời gian dừng** chỉ bằng **3** (chạm $$7 < 9$$ ngay ở bước thứ 3!), nhưng sau đó nó lại nhập vào đúng quỹ đạo của 7 nên **thời gian dừng toàn phần** = $$3 + 16 = \mathbf{19}$$!

**Vì sao cách gọi tên quan trọng.** "Sau một số bước sẽ chạm 1" là một khẳng định định tính. Thời gian dừng biến nó thành **dữ liệu định lượng** mà bạn có thể vẽ, so sánh, đặt giả thuyết. Trong bài thực hành Chương 7, một hướng khám phá tốt hầu như luôn bắt đầu từ một đại lượng đo được (độ cao lớn nhất, thời gian dừng toàn phần, lớp đồng dư của các số lẻ, …), chứ không chỉ nhìn vào danh sách số thô.

---

## 3. Vì sao người ta quan tâm

**Dễ tiếp cận.** Ai biết chia cho 2 và nhân với 3 đều có thể tạo dữ liệu: dễ bắt đầu nhưng không có giới hạn trên, rất phù hợp cho thảo luận nhóm.

**Sâu mà không cần thuật ngữ.** Khác với BSD hay giải tích điều hòa, Collatz không cần một học kỳ kiến thức nền mới *phát biểu* được. Nhưng các kết quả từng phần tốt nhất lại dùng lý thuyết ergodic, xác suất và tổ hợp số học. Cái khó ở đây không nằm ở ngôn ngữ khó hiểu, mà ở chỗ một hệ động lực sơ cấp trên tập số nguyên lại **chống lại** mọi cố gắng chứng minh.

**Đặc điểm của bài toán mở.** Độ phức tạp của phát biểu và độ khó của lời giải **không** nhất thiết đi cùng nhau. Một công thức truy hồi một dòng có thể tồn tại qua nhiều thế hệ kỹ thuật. Hãy so sánh với ngôn ngữ trừu tượng của bài [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/).

**Toán học thực nghiệm.** Thống kê theo lớp đồng dư, cây ngược, kỷ lục độ cao, biểu đồ tần suất thời gian dừng đều là đối tượng toán học chính đáng khi giả thuyết đầy đủ còn mở. Bài toán này đánh giá cao việc ghi nhật ký cẩn thận và báo cáo trung thực kết quả âm, không kém gì một đồ thị đẹp.

**Rèn cách nhìn đúng về bằng chứng.** Bài học giống như việc kiểm tra các không điểm của hàm zeta trên đường tới hạn trong bài [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/).

Collatz là "bài toán cửa ngõ": dễ bước vào, khó đi ra. Khóa học cố ý đặt nó cạnh các bài toán Thiên niên kỷ để bạn thấy được sự đa dạng của các phát biểu.

---

## 4. Kiểm tra không phải là chứng minh

Giả thuyết đã được kiểm tra với mọi số ban đầu đến một giới hạn **cực lớn**. Các dự án tính toán đã vượt qua $$2^{68}$$, $$2^{70}$$, $$2^{71}$$ và các mốc liên quan (tức hơn $$2{,}3 \times 10^{21}$$); con số này thay đổi theo thời gian, nên khi viết bài A3 hoặc A5, hãy trích dẫn một bài tổng quan hoặc một bài kiểm tra mới nhất (ví dụ các công trình của Barina và những người tiếp theo) thay vì nhớ một con số cố định.

Trong phạm vi đã kiểm tra, chưa tìm thấy phản ví dụ nào.

Tuy vậy:

- Phản ví dụ *có thể* nằm ngoài phạm vi đã kiểm tra.
- Một quỹ đạo tiến ra vô cùng, hoặc một **chu trình khác** với $$4\to 2\to 1$$, sẽ bác bỏ giả thuyết.
- Kiểm tra **hữu hạn** số ban đầu không bao giờ chứng minh được một phát biểu về **vô hạn** số.

**Cùng tinh thần** với việc kiểm tra nhiều không điểm của hàm zeta trên đường tới hạn trong [bài Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/): **bằng chứng mạnh, nhưng chưa phải định lý.**

Trong bài A5, bạn được khuyến khích kiểm tra và vẽ đồ thị, nhưng câu kết luận phải phân biệt "trong mẫu của tôi" với "với mọi số nguyên dương".

Câu nói đúng khi thảo luận: *Collatz đã được kiểm tra đến một giới hạn hữu hạn rất lớn; phát biểu cho mọi số vẫn còn mở.* Giống như với các tính toán về RH: **bằng chứng mạnh, không phải chứng minh.**

---

## 5. Lập luận gần đúng: vì sao kỳ vọng dãy đi xuống

### Ví dụ làm từng bước 2: Chứng minh trực giác lực hút $$3/4$$ và thử đổi sang số âm!

1. **Tính kỳ vọng lực hút đi xuống:** Xuất phát từ một số lẻ $$N$$ lớn, giá trị $$3N+1$$ luôn là số chẵn nên chia hết cho $$2^1$$ (xác suất $$1$$); nếu các bit nhị phân hành xử như tung đồng xu ngẫu nhiên thì nó chia hết cho $$2^2 = 4$$ với xác suất $$1/2$$, cho $$2^3 = 8$$ với xác suất $$1/4$$, v.v. Do đó, số lần chia đôi trung bình ngay sau một bước lẻ là tổng chuỗi hình học:
   $$
   \mathbb{E}[a(N)] = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots = 2.
   $$
   Nghĩa là trung bình sau một bước lẻ kèm toàn bộ các lần chia đôi theo sau, số $$N$$ bị nhân với hệ số:
   $$
   \frac{3}{2^2} = \frac{3}{4} = 0{,}75 < 1!
   $$
   Theo thang logarit, kỳ vọng độ thay đổi của $$\log N$$ sau mỗi chu kỳ lẻ là $$\log(3/4) \approx -0{,}2877 < 0$$ — một "lực hút đi xuống" rất rõ rệt!
2. **Cảnh báo: lực hút trung bình không cấm được chu trình khác!** Hãy thử áp dụng *chính xác cùng quy tắc $$T$$* cho **số nguyên âm** $$n = -5$$:
   $$
   -5 \to 3(-5)+1 = -14 \to -7 \to 3(-7)+1 = -20 \to -10 \to \mathbf{-5}!
   $$
   Ta rơi ngay vào một chu trình độ dài 5 hoàn toàn khác với $$-1 \to -2 \to -1$$ (và còn có cả chu trình độ dài 18 xuất phát từ $$-17$$!). Phép thử nhỏ này chứng tỏ lực hút trung bình $$3/4 < 1$$ chỉ là gợi ý xác suất, hoàn toàn **không đủ** để tự động loại trừ các chu trình ẩn!

**Những lưu ý quan trọng.**

- Ánh xạ là **tất định**. Gọi các thống kê là "ngẫu nhiên" là **một lựa chọn mô hình**, không phải vì $$T$$ tung đồng xu.
- Lập luận về "hầu hết" **không** tự động kiểm soát **mọi** số nguyên. Một tập ngoại lệ siêu thưa thớt vẫn có thể thoát khỏi lực hút trung bình và làm giả thuyết sai.
- Các dạng ánh xạ rút gọn (gộp các bước chia 2) làm thay đổi hằng số trong lập luận gần đúng, nhưng **không** thay thế được một chứng minh thật sự.

Một hằng số tới hạn thường xuất hiện trong lý thuyết mật độ:

$$
\frac{\log 3}{\log 4}\approx 0{,}7925.
$$

Nó xuất hiện trong định lý "hầu hết" kiểu Korec (với hầu hết $$N$$, quỹ đạo xuống dưới lũy thừa $$N^\theta$$ khi $$\theta$$ lớn hơn ngưỡng này) và trong lập luận cân bằng giữa phép nhân $$3$$ với phép chia cho lũy thừa của $$2$$ về trung bình.

---

## 6. Ánh xạ rút gọn và ánh xạ Syracuse

Các video phổ thông thường dùng ánh xạ $$T$$ đầy đủ. Các bài giảng nghiên cứu (Tao, bài tổng quan của Lagarias, Chamberland) hay chuyển sang một ánh xạ trên các số **lẻ**, để mỗi bước có đúng **một** phép nhân với $$3$$.

Định nghĩa **ánh xạ Syracuse** trên các số nguyên dương lẻ:

$$
\operatorname{Syr}(N)=\frac{3N+1}{2^{a(N)}},
$$

trong đó $$2^{a(N)}$$ là lũy thừa lớn nhất của $$2$$ chia hết $$3N+1$$ (kết quả lại là số lẻ). Lặp $$\operatorname{Syr}$$ là theo dõi riêng các "trạm dừng số lẻ" trong quỹ đạo Collatz sau khi đã nén gọn toàn bộ các bước chia 2 liên tiếp.

**Kiểm tra lại trên $$N = 7$$:**
- $$3(7)+1 = 22 = 2^1 \cdot 11 \implies \operatorname{Syr}(7) = 11$$ (số mũ $$a=1$$).
- $$3(11)+1 = 34 = 2^1 \cdot 17 \implies \operatorname{Syr}(11) = 17$$ ($$a=1$$).
- $$3(17)+1 = 52 = 2^2 \cdot 13 \implies \operatorname{Syr}(17) = 13$$ ($$a=2$$).
- $$3(13)+1 = 40 = 2^3 \cdot 5 \implies \operatorname{Syr}(13) = 5$$ ($$a=3$$).
- $$3(5)+1 = 16 = 2^4 \cdot 1 \implies \operatorname{Syr}(5) = 1$$ ($$a=4$$).

Quỹ đạo đầy đủ theo $$T$$ mất tới 16 bước mới chạm 1, nhưng qua ống kính Syracuse chỉ còn đúng 5 bước gọn gàng: $$7 \to 11 \to 17 \to 13 \to 5 \to 1$$!

**Vì sao nghiên cứu ưa dùng dạng này.** Các thống kê theo modulo lũy thừa của $$3$$ gọn hơn hẳn; và mô hình xác suất cho số mũ $$a(N)$$ (phân phối hình học có kỳ vọng $$2$$) trở thành trung tâm của các chứng minh "hầu hết" hiện đại. **Lưu ý khi thảo luận:** quỹ đạo theo $$T$$ và theo $$\operatorname{Syr}$$ có số bước khác nhau; chỉ so sánh các nguồn sau khi đã thống nhất quy ước.

---

## 7. Các kết quả từng phần (không đầy đủ)

### 7.1 Các kết quả về mật độ / "hầu hết" (tóm tắt)

| Tác giả | Nội dung chính | Loại mật độ |
|------|-----------|-------------|
| Krasikov–Lagarias | Nhiều $$N\le x$$ đã được biết có $$\operatorname{Col}_{\min}(N)=1$$ | đếm đến $$x$$ |
| Terras | Hầu hết $$N$$ đều xuống dưới $$N$$ | mật độ tự nhiên |
| Allouche / Korec | Hầu hết $$N$$: $$\operatorname{Col}_{\min}(N)<N^\theta$$ ($$\theta$$ có thể gần đến $$\log 3/\log 4$$) | mật độ tự nhiên |
| **Tao (2019)** | Hầu hết $$N$$: $$\operatorname{Col}_{\min}(N)<f(N)$$ với **mọi** hàm $$f\to\infty$$, dù tăng chậm đến đâu | **mật độ logarit** |

**Định lý Tao (blog/arXiv).** Với mọi hàm $$f\to\infty$$,

$$
\operatorname{Col}_{\min}(N)<f(N)
$$

với hầu hết $$N$$ theo mật độ logarit. Ví dụ minh họa: hầu hết quỹ đạo có giá trị nhỏ nhất bé hơn $$\log\log\log\log N$$ — nói nôm na là "hầu hết mọi quỹ đạo Collatz đều đạt tới các giá trị gần như bị chặn".

**Định lý này không phải là:** mọi $$N$$ đều về 1; một kết quả chỉ dựa trên kiểm tra; một kết quả về mật độ tự nhiên; hay "Tao đã giải xong Collatz".

Nguồn chuẩn: [arXiv:1909.03562](https://arxiv.org/abs/1909.03562), [blog Tao](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/); bài phổ thông: [Quanta](https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/).

### 7.2 Giải thích: Ý tưởng phía sau định lý "hầu hết" của Tao (2019)

Làm thế nào Terence Tao tiến gần đến Collatz hơn bất kỳ ai trong nhiều thập kỷ mà không bị mắc kẹt ở ngưỡng $$N^{0{,}7925}$$ cũ của Korec? Hãy đi chậm qua 4 bước:

#### Bước 1: Rút gọn về ánh xạ Syracuse và theo dõi modulo $$3^n$$
Tao chuyển hẳn sang ánh xạ Syracuse trên các số lẻ. Chìa khóa kỹ thuật là nếu bạn biết phân phối của một số ngẫu nhiên theo modulo $$3^n$$, bạn có thể theo dõi biến đổi của phân phối đó sau nhiều bước lặp Syracuse liên tiếp.

#### Bước 2: Dùng mật độ logarit thay vì mật độ tự nhiên
Với mật độ tự nhiên (đếm đều mọi số), việc "nhân 3 chia $$2^a$$" làm biến dạng xác suất rất khó kiểm soát. Khi chuyển sang **mật độ logarit** (gán trọng số tỉ lệ với $$1/N$$), phép nhân với hằng số $$3/2^a$$ giữ nguyên tính bất biến tỉ lệ theo thang $$\log N$$ — biến bài toán lặp phức tạp thành một quá trình truyền phân phối đẹp mắt!

#### Bước 3: Biến đổi Fourier trên $$\mathbb{Z}/3^n\mathbb{Z}$$ và "tính bất thường 3-adic"
Bằng phân tích Fourier rời rạc (hàm đặc trưng) trên vành $$\mathbb{Z}/3^n\mathbb{Z}$$ kết hợp quá trình đổi mới (renewal process), Tao chứng minh phân phối của quỹ đạo ổn định dần và chịu lực kéo đi xuống một cách đồng đều: gần như mọi quỹ đạo đều tụt xuống dưới một hàm tăng chậm tùy ý $$f(N)$$ (như $$\log\log\log N$$).

#### Bước 4: Ranh giới cuối cùng còn bỏ ngỏ
Dù $$f(N)$$ có tăng chậm đến đâu, định lý Tao vẫn **chưa** hạ được $$f(N)$$ xuống hằng số $$1$$, và vẫn cho phép tồn tại một tập ngoại lệ có mật độ logarit bằng $$0$$ (ví dụ các lũy thừa hay một dãy số siêu thưa vẫn có mật độ 0 nhưng chứa vô hạn phần tử!). Vì vậy Collatz vẫn là bài toán mở.

### 7.3 Chu trình, các dạng tổng quát, tính toán

- **Chu trình:** trong các số dương, chỉ biết chu trình $$4\to 2\to 1$$ (và nếu có một chu trình dương khác thì độ dài của nó đã được chứng minh phải cực kỳ lớn — hàng trăm triệu bước!); với số âm hoặc ánh xạ khác thì có nhiều chu trình khác (như $$-5 \to -14 \to -7 \to -20 \to -10 \to -5$$ ta vừa thử ở trên).  
- **Dạng tổng quát $$mx+1$$:** John Conway (1972) chứng minh một họ ánh xạ tổng quát kiểu Collatz có thể mô phỏng máy tính phổ quát, dẫn tới tính không quyết định được (undecidability); điều đó **không** có nghĩa là "Collatz cổ điển đã được chứng minh là không quyết định được" (xem video của Easy Theory trong tư liệu).  
- **Kiểm tra bằng máy tính:** cắt tỉa cây, lọc theo đồng dư; đây là các kỹ thuật tính toán.  
- **Bài tổng quan của Lagarias** ([arXiv:2111.02635](https://arxiv.org/abs/2111.02635)): điểm bắt đầu để đọc tài liệu.

Các kết quả "từng phần" về Collatz mang tính *cấu trúc và mật độ*, không phải một công thức đóng cho thời gian dừng.

---

## 8. Vì sao khó, nói bằng lời

Ánh xạ trộn lẫn hai cấu trúc số học "không đội trời chung": **phép nhân với 3 cộng 1** (cấu trúc cơ số 3 kết hợp phép cộng) và **phép chia cho 2** (cấu trúc cơ số 2). Phép cộng $$+1$$ phá hủy hoàn toàn biểu diễn thừa số nguyên tố của số trước đó, làm mất đi các bất biến đại số đơn giản. Không có hàm năng lượng (hàm Lyapunov) hiển nhiên nào giảm đều sau *mọi* bước với *mọi* $$n$$. Các kỹ thuật giải tích cho hệ động lực trơn không dễ áp dụng cho hệ lai trên tập số nguyên này.

Nói cách khác: mỗi bước đều đơn giản, nhưng **bức tranh tổng thể** của vô hạn quỹ đạo thì không. Đó là khoảng cách giữa "một quy tắc trẻ em cũng hiểu" và "một định lý".

So với [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): ở đó cái khó nằm ở lớp bài toán và giới hạn của thuật toán; còn ở Collatz, cái khó là một ánh xạ cụ thể chống lại mọi chứng minh dù có thể kiểm tra từng điểm. Hai kiểu khó khác nhau, nhưng đều dạy ta sự khiêm tốn.

---

## 9. Vai trò trong khóa học: trang bài toán và bài thực hành

| Trang này (Chương 1) | Bài thực hành ([Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/)) |
|------------------|---------------|
| Phát biểu, bối cảnh, tình trạng | Thí nghiệm, nhật ký, hồ sơ học tập |
| Giải thích bản chất bài toán mở | Tự sáng tạo, khám phá bằng dữ liệu |
| Không bắt buộc viết mã | Khuyến khích viết mã, vẽ đồ thị |
| Không giải giả thuyết | Không giải giả thuyết, nhưng có quy trình kiểm tra các giả thuyết nhỏ |

**Đừng** coi A5 là "chứng minh Collatz". Hãy coi A5 là một cuộc khám phá với giả thuyết *có thể bác bỏ*, ví dụ "thời gian dừng trung bình trên $$[1,N]$$ tăng như …", rồi kiểm tra bằng dữ liệu. Một giả thuyết nhỏ bị bác bỏ vẫn là khoa học tốt; còn tuyên bố đã giải Collatz thì không.

---

## 10. Các biến thể của ánh xạ và cạm bẫy về định nghĩa

Tài liệu dùng một vài biến thể (xem thêm mục 6 về ánh xạ Syracuse):

- Ánh xạ đầy đủ $$T$$ như trên.
- Ánh xạ "rút gọn" gộp mọi phép chia 2 sau $$3n+1$$; ánh xạ **Syracuse** trên các số lẻ.
- Đôi khi xét trên tập số nguyên (kể cả số âm) hoặc trên các vành khác; khi đó chu trình có thể khác.

Khi so sánh đồ thị với bạn bè hay với một bài báo, trước hết hãy thống nhất **cùng một định nghĩa bước**. Đây là lỗi kỹ thuật nhỏ nhưng thường làm lệch số bước.

---

## Hiểu lầm thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Đã kiểm tra đến $$10^{20}$$ nên giả thuyết đúng." | Đó chỉ là bằng chứng trong phạm vi đã kiểm tra. |
| "Dãy số là ngẫu nhiên." | Dãy hoàn toàn tất định; chỉ có thống kê trông lộn xộn. |
| "$$3n+1$$ luôn làm số tăng lên." | Kết hợp với các phép chia 2, quỹ đạo thường đi xuống; hãy phát biểu lập luận gần đúng cho chính xác. |
| "Đã có bản bác bỏ bằng Lean trên mạng." | Một tuyên bố bất thường cần được cộng đồng kiểm tra; giả thuyết vẫn mở trong toán học chính thống (cẩn thận với lỗi hình thức hóa hoặc trò đùa). |
| "A5 nghĩa là chứng minh Collatz." | A5 là khám phá có phương pháp, không phải giải một bài toán cỡ Thiên niên kỷ. |
| "Phát biểu dễ nên không có toán học xung quanh." | Có các kết quả về mật độ, chu trình, lập luận gần đúng, kiểm tra bằng máy; hãy đọc Lagarias. |
| "Tao đã giải Collatz / hầu hết cũng là mọi." | Tao (2019) chứng minh kết quả "hầu hết quỹ đạo gần bị chặn" (theo mật độ logarit), **không** phải giả thuyết đầy đủ. |
| "Collatz đã được chứng minh là không quyết định được." | Chỉ một số dạng **tổng quát** liên quan đến tính không quyết định được; Collatz cổ điển vẫn mở. Đừng suy diễn quá mức từ các video phổ thông. |

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Video dùng để **định hướng và làm quen với không khí nghiên cứu**, không thay thế chứng minh (hiện chưa có chứng minh). Đánh giá chi tiết: `research/video-research/collatz/`.

**Thứ tự xem gợi ý**

1. **Định hướng** — Veritasium, *The Simplest Math Problem No One Can Solve – Collatz*: [YouTube](https://www.youtube.com/watch?v=094y1Z2wpJg).  
2. **Bối cảnh** — Numberphile, *UNCRACKABLE?* (Eisenbud): [YouTube](https://www.youtube.com/watch?v=5mFpVDpKX70).  
3. **Tổng quan** — Chamberland, *The 3x+1 Problem: Status and Recent Work* (Phần 1): [YouTube](https://www.youtube.com/watch?v=t1I9uHF9X5Y).  
4. **Bài giảng nghiên cứu** — Tao, *The Notorious Collatz conjecture*: [mathtube](https://mathtube.org/lecture/video/notorious-collatz-conjecture) · [YouTube](https://www.youtube.com/watch?v=X2p5eMWyaFs) · [slides](https://terrytao.files.wordpress.com/2020/02/collatz.pdf).  
5. **Hướng mới (không bắt buộc)** — Tao tại IAS, *Almost all Collatz Orbits…*: [YouTube](https://www.youtube.com/watch?v=k-dtx8s2ehM) · [arXiv:1909.03562](https://arxiv.org/abs/1909.03562).  
6. **Nói cho đúng (không bắt buộc)** — Easy Theory nhận xét về cách diễn đạt trong video Veritasium: [YouTube](https://www.youtube.com/watch?v=Lr6qc_9M0Ks).

**Nhắc lại:** kết quả của Tao (2019) là định lý "hầu hết quỹ đạo gần bị chặn" (theo mật độ logarit), **không** giải quyết toàn bộ giả thuyết. Tình trạng năm 2026: vẫn **còn mở**.

Phụ đề (chỉ dùng để tra cứu, **không** thay thế nội dung bài) và khung hình mẫu trong bộ tư liệu:

- `research/video-research/collatz/transcripts/` · `TRANSCRIPT_STATUS.md`

![Bảng quỹ đạo Collatz (frame Numberphile)]({{ site.baseurl }}/img/video_research/collatz/5mFpVDpKX70_frame01.jpg)

*Hình. Khung hình mẫu từ video *UNCRACKABLE?* của Numberphile (khoảng phút thứ 1), dùng để minh họa.*

![Mẫu tô màu Collatz]({{ site.baseurl }}/img/video_research/collatz/LqKpkdRRLZw_frame01.jpg)

*Hình. Khung hình từ video *Collatz in Color*; đây là minh họa hình ảnh, không phải chứng minh.*

---

## Tài liệu

Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/collatz/references.md`.

### Bài báo và blog của tác giả

1. Lagarias — *The 3x+1 Problem: An Overview*: [arXiv:2111.02635](https://arxiv.org/abs/2111.02635) · [PDF](https://arxiv.org/pdf/2111.02635).  
2. Lagarias — bài tổng quan cổ điển: [SFU](http://www.cecm.sfu.ca/organics/papers/lagarias/); bản PDF về *các dạng tổng quát*: [Williams](https://web.williams.edu/Mathematics/sjmiller/public_html/372Fa15/addcomments/Lagarias_3x+1AndItsGeneralizations.pdf).  
3. Tao — *Almost all Collatz orbits…*: [arXiv:1909.03562](https://arxiv.org/abs/1909.03562) · [PDF](https://arxiv.org/pdf/1909.03562) · [blog](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/).  
4. Tao — blog Collatz 2011: https://terrytao.wordpress.com/2011/08/25/the-collatz-conjecture-littlewood-offord-theory-and-powers-of-2-and-3/  
5. Chamberland — survey 2003 PDF: http://www.math.grinnell.edu/~chamberl/papers/3x_survey_eng.pdf  
6. Các công trình kiểm tra bằng máy tính (Barina và cộng sự …); hãy kiểm tra năm xuất bản để biết giới hạn hiện tại.

### Video chính

7. Veritasium: https://www.youtube.com/watch?v=094y1Z2wpJg  
8. Numberphile UNCRACKABLE: https://www.youtube.com/watch?v=5mFpVDpKX70 · trang: https://www.numberphile.com/videos/uncrackable-the-collatz-conjecture  
9. Chamberland Part 1: https://www.youtube.com/watch?v=t1I9uHF9X5Y  
10. Tao *Notorious Collatz*: https://mathtube.org/lecture/video/notorious-collatz-conjecture · YouTube: https://www.youtube.com/watch?v=X2p5eMWyaFs · slides: https://terrytao.files.wordpress.com/2020/02/collatz.pdf · listing: https://www.rism.it/rism-channel/2021/riemann-prize-week/the-notorious-collatz-conjecture-terence-tao  
11. Tao IAS almost-all: https://www.youtube.com/watch?v=k-dtx8s2ehM  
12. Easy Theory (đính chính wording): https://www.youtube.com/watch?v=Lr6qc_9M0Ks  

### Video bổ sung

13. Tipping Point Math: https://www.youtube.com/watch?v=m4CjXk_b8zo  
14. Numberphile Collatz in Color: https://www.youtube.com/watch?v=LqKpkdRRLZw · extra: https://www.youtube.com/watch?v=O2_h3z1YgEU · realtime: https://youtu.be/wH141HLD57o  
15. Lex Clips — Tao Collatz: https://www.youtube.com/watch?v=vT4VJyXWHlo  

### Trang web và tin tức

16. Wikipedia: https://en.wikipedia.org/wiki/Collatz_conjecture  
17. Quanta 2019: https://www.quantamagazine.org/mathematician-proves-huge-result-on-dangerous-problem-20191211/  
18. Chamberland hub: https://chamberland.math.grinnell.edu/3x.html  
19. Basel news: https://dmi.unibas.ch/en/news/details/lecture-in-basel-terence-tao-and-the-notorious-collatz-conjecture/  
20. Stanford event: https://mathematics.stanford.edu/events/kiddie-colloquium/almost-almost-collatz  
21. Pitt note: https://www.mathematics.pitt.edu/content/note-collatz-conjecture  
22. Study.com (độ tin cậy thấp với các khẳng định về nghiên cứu): https://study.com/academy/lesson/history-of-the-collatz-conjecture.html  

### Trong khóa học

23. [Bài thực hành Collatz]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/); [Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/). Bộ tư liệu: `research/video-research/collatz/` (đặc biệt là `references.md`).

---

## Hướng đi tiếp

**Đề tài mặc định cho A5.** Đọc bài thực hành ở Chương 7, chọn một giả thuyết nhỏ, ghi nhật ký thí nghiệm, và giữ rõ ranh giới giữa "trong mẫu" và "với mọi $$n$$". Nếu muốn một hệ động lực trơn hơn, có thể chọn ánh xạ logistic (giới thiệu nhẹ về hỗn độn) thay cho bài thực hành này. Quay lại trang này khi cần cách diễn đạt chuẩn cho phần "tình trạng của bài toán mở" trong hồ sơ học tập.

## Video tham khảo

- **Xem trước:** [The Simplest Math Problem No One Can Solve - Collatz Conjecture](https://www.youtube.com/watch?v=094y1Z2wpJg) — Veritasium, tiếng Anh. Giới thiệu quy tắc, các quỹ đạo và lịch sử bài toán; nên xem trước khi đọc bài.
- [UNCRACKABLE? The Collatz Conjecture - Numberphile](https://www.youtube.com/watch?v=5mFpVDpKX70) — Numberphile, tiếng Anh. David Eisenbud giải thích vì sao bài toán khó; nên xem sau khi đã nắm ý chính của bài.
- [The 3x+1 Problem: Status and Recent Work Part 1](https://www.youtube.com/watch?v=t1I9uHF9X5Y) — Experimental mathematics, tiếng Anh. Xem thêm sau hai video trên; bài giảng tổng quan về tình trạng nghiên cứu.
