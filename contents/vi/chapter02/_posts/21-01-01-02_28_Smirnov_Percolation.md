---
layout: post
title: "Percolation và mô hình Ising phẳng của Smirnov (Huy chương Fields 2010)"
chapter: '02'
order: 28
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy trải một bàn cờ tổ ong khổng lồ gồm hàng triệu ô lục giác, rồi với mỗi ô bạn tung một đồng xu công bằng: ngửa tô **vàng**, sấp tô **xanh**. Bây giờ lùi ra thật xa đến khi từng ô lục giác nhỏ li ti hòa vào nhau thành một bức tranh liên tục, và hỏi: xác suất có một con đường toàn ô vàng nối từ cạnh trái sang cạnh phải phụ thuộc vào điều gì? Vật lý thống kê dự đoán một phép màu: ở đúng ngưỡng tới hạn $$p_c = 1/2$$, bức tranh ngẫu nhiên đó **quên sạch** hình dáng lục giác ban đầu và trở nên **bất biến bảo giác** — nếu bạn uốn cong khung tranh bằng bất kỳ ánh xạ giải tích phức nào bảo toàn góc, xác suất nối xuyên vẫn giữ nguyên không đổi!

Suốt nhiều thập niên, dự đoán đẹp như mơ ấy chưa có nổi một chứng minh toán học cho bất kỳ mô hình lưới nào. Năm 2001, bằng một bài báo ngắn gọn đến sững sờ chỉ dài **6 trang**, **Stanislav Smirnov** chứng minh trọn vẹn công thức Cardy và tính bất biến bảo giác cho mô hình thấm đỉnh trên lưới tam giác — rồi phát minh ra **fermion chỉnh hình rời rạc** để chinh phục **mô hình Ising phẳng**. Năm 2010, ông nhận **Huy chương Fields**:

> “For the proof of conformal invariance of percolation and the planar Ising model in statistical physics.”  
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

*Tạm dịch: vì chứng minh tính bất biến bảo giác của mô hình thấm (percolation) và mô hình Ising phẳng trong vật lý thống kê.*

Cần đọc lời trao giải thật tỉnh táo: IMU nêu chính xác **hai mô hình trên lưới**, không nói mọi mô hình phẳng tới hạn đều đã thành định lý (ngay cả mô hình thấm cạnh trên lưới vuông đến nay vẫn còn mở!). Công trình của Smirnov ghép khít với ngôn ngữ đường cong liên tục **SLE** của Oded Schramm và [Wendelin Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) (Fields 2006), và mở đường cho các định lý chuyển pha chiều cao của học trò ông là [Hugo Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/) (Fields 2022).

**Mạch bài học:** Kiến thức cần nhớ (ánh xạ bảo giác, thấm đỉnh vs. thấm cạnh, giải tích phức rời rạc) → Ví dụ làm từng bước: đối xứng vàng–xanh trên lưới tổ ong nhỏ và công thức Cardy–Carleson trên tam giác đều → Giải thích: 4 bước từ đẳng thức đổi màu đến Cauchy–Riemann rời rạc, SLE$$_6$$ và fermion Ising → Những gì vẫn còn mở (thấm cạnh lưới vuông, đường đi tự tránh).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt **mô hình thấm đỉnh** (*site percolation*) với **mô hình thấm cạnh** (*bond percolation*), và giải thích vì sao chỉ tại điểm tới hạn $$p_c$$ mới xuất hiện giới hạn thang đo không tầm thường.
- Tự tay tính xác suất nối xuyên trên tam giác đều cạnh $$1$$ theo **công thức Cardy–Carleson** và thấy ý nghĩa của đối xứng bậc ba trên lưới tổ ong/tam giác.
- Giải thích vì sao định lý năm 2001 của Smirnov áp dụng chặt chẽ cho **mô hình thấm đỉnh tới hạn trên lưới tam giác**, còn **thấm cạnh trên lưới vuông** vẫn còn mở.
- Phân công chính xác: **Schramm** định nghĩa SLE, **Lawler–Schramm–Werner** xây dựng lý thuyết giải tích SLE, còn **Smirnov** chứng minh hội tụ bất biến bảo giác cho các mô hình lưới rời rạc.
- Mô tả ý chính của **fermion chỉnh hình rời rạc** cho **mô hình Ising phẳng** (Smirnov; Chelkak–Smirnov trên đồ thị đẳng bán kính) và thấy vì sao kết quả Ising lại "phổ quát" hơn kết quả thấm năm 2001.

**Kiến thức nền.** Hàm chỉnh hình và ánh xạ bảo giác giữa các miền phẳng ở mức giáo trình giải tích phức nhập môn; biến ngẫu nhiên Bernoulli và ý tưởng giới hạn thang đo (bước lưới $$\delta\to 0$$); sự khác nhau giữa mô hình rời rạc và quá trình liên tục. Không cần học trước về SLE.

**Liên kết với các bài khác.** Bài này cho thấy một dự đoán vật lý trở thành định lý gắn với một lưới cụ thể, và mối nối giữa mô hình rời rạc với hình học bảo giác liên tục. Đọc cùng [Werner / SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) để hiểu ngôn ngữ đường cong, và [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/) cho các kết quả sắc nét về chuyển pha.

---

## Kiến thức cần nhớ: Bất biến bảo giác và Giải tích phức rời rạc nghiên cứu gì?

### 1. Ánh xạ bảo giác (Conformal Map) — phép biến hình giữ nguyên góc
Một hàm chỉnh hình $$f: \Omega_1 \to \Omega_2$$ có $$f'(z) \neq 0$$ là **ánh xạ bảo giác**: cục bộ nó chỉ phóng to/thu nhỏ và xoay, không làm méo góc. Nhờ định lý ánh xạ Riemann, mọi miền đơn liên (hình vuông, hình tròn, tam giác, quả đậu...) đều biến đổi bảo giác được sang nhau. Một mô hình xác suất tới hạn có **tính bất biến bảo giác** nghĩa là nếu giải được nó trên một miền chuẩn (như tam giác đều), ta tự động biết ngay đáp số cho *mọi* hình dạng miền khác!

### 2. Thấm đỉnh trên lưới tam giác vs. Thấm cạnh trên lưới vuông
- **Thấm đỉnh trên lưới tam giác $$\mathbb{T}$$** (tô màu vàng/xanh từng ô lục giác của lưới tổ ong đối ngẫu): mỗi ô độc lập có xác suất $$p$$ tô vàng, $$1-p$$ tô xanh. Điểm tới hạn chính xác là $$p_c = 1/2$$.
- **Thấm cạnh trên lưới vuông $$\mathbb{Z}^2$$:** mỗi cạnh mở/đóng độc lập với xác suất $$p$$ (cũng có $$p_c = 1/2$$). Dù trực giác vật lý tin rằng cả hai lưới có cùng giới hạn bảo giác (**tính phổ quát**), toán học hiện nay mới chứng minh được cho lưới tam giác.

### 3. Giải tích phức rời rạc (Discrete Complex Analysis)
Muốn chứng minh một hàm xác suất $$F_\delta$$ trên lưới mịn cỡ $$\delta$$ hội tụ về một hàm chỉnh hình khi $$\delta \to 0$$, ta tìm một đẳng thức tổ hợp ngay trên lưới sao cho $$F_\delta$$ thỏa **phương trình Cauchy–Riemann rời rạc** (tổng tích phân đường vòng quanh mỗi ô nhỏ bằng $$0$$). Khi $$\delta \to 0$$, mọi giới hạn theo dãy con đều thỏa Cauchy–Riemann liên tục và bị khóa duy nhất bởi điều kiện biên!

---

## 1. Ví dụ làm từng bước: đối xứng vàng–xanh trên lưới tổ ong và công thức Cardy–Carleson

### Ví dụ 1: Tại sao $$p_c = 1/2$$ trên bàn cờ tổ ong đối xứng (trò chơi Hex)?
Xét một bàn cờ hình thoi gồm $$N \times N$$ ô lục giác (chính là trò chơi **Hex** nổi tiếng do Piet Hein và John Nash phát minh). Tô ngẫu nhiên mỗi ô màu vàng hoặc xanh với xác suất $$p = 1/2$$:
- Một định lý tôpô sơ cấp (tương đương định lý điểm bất động Brouwer!) khẳng định trò chơi Hex **không bao giờ hòa**: hoặc có một dải ô vàng nối cạnh trái với cạnh phải, hoặc có một dải ô xanh nối cạnh trên với cạnh dưới — *đúng một trong hai sự kiện xảy ra*!
- Khi $$p = 1/2$$, xác suất hai màu hoàn toàn đối xứng, nên:
  $$
  \mathbb{P}_{1/2}(\text{vàng nối trái–phải}) = \mathbb{P}_{1/2}(\text{xanh nối trên–dưới}) = \frac{1}{2} \quad \text{với MỌI kích thước } N!
  $$
Ngay cả khi $$N = 10^9$$ (bước lưới $$\delta \to 0$$), xác suất nối xuyên vẫn ghim chặt ở đúng $$1/2$$, không tụt về $$0$$ cũng không nhảy lên $$1$$! Đó là dấu hiệu rõ rệt nhất của **điểm tới hạn** $$p_c = 1/2$$.

### Ví dụ 2: Công thức Cardy–Carleson trên tam giác đều cạnh bằng $$1$$
Năm 1992, bằng lý thuyết trường bảo giác (CFT), **John Cardy** đoán ra công thức hàm siêu bội phức tạp cho xác suất nối xuyên của một hình chữ nhật bảo giác $$(\Omega; A, B, C, D)$$. **Lennart Carleson** nhận ra nếu ánh xạ bảo giác miền $$\Omega$$ thành **tam giác đều $$ABC$$ cạnh bằng $$1$$**, đặt điểm $$D$$ trên cạnh $$AC$$ cách $$C$$ một đoạn $$x \in [0, 1]$$, thì công thức của Cardy sụp gọn thành tuyến tính tuyệt đối:

$$
\mathbb{P}(\text{có đường vàng nối cạnh } AB \text{ với đoạn } CD) = x!
$$

Thử cắm số cụ thể:
- Nếu $$D$$ nằm ở $$1/4$$ cạnh $$AC$$ ($$x = 0.25$$): xác suất giới hạn đúng bằng **$$25\%$$**.
- Nếu $$D$$ là trung điểm cạnh $$AC$$ ($$x = 0.5$$): xác suất giới hạn đúng bằng **$$50\%$$**.
- Nếu $$D$$ nằm ở $$3/4$$ cạnh $$AC$$ ($$x = 0.75$$): xác suất giới hạn đúng bằng **$$75\%$$**.

---

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/smirnov-cardy-percolation_vi.mp4"></video>
</div>

Video dài khoảng 44 giây (có thuyết minh tiếng Việt): đối xứng vàng–xanh trên lưới tổ ong ($p_c=1/2$) và chứng minh 6 trang cho công thức Cardy–Carleson trên tam giác đều.

## 2. Giải thích: Smirnov chứng minh bất biến bảo giác cho Thấm và Ising như thế nào?

Bức tranh chứng minh của Smirnov cho cả hai mô hình (thấm năm 2001 và Ising năm 2010) cùng đi theo một kiến trúc 4 bước thanh lịch:

#### Bước 1: Chọn đại lượng quan sát rời rạc $$H_A, H_B, H_C$$ và phép đổi màu kỳ diệu (Thấm, 2001)
Trong bài báo 6 trang trên *Comptes Rendus* (2001; bản dài [arXiv:0909.4499](https://arxiv.org/abs/0909.4499)), Smirnov xét miền $$\Omega$$ trên lưới tam giác $$\mathbb{T}$$ có 3 cung biên $$AB, BC, CA$$. Với mỗi điểm $$z \in \Omega$$, gọi $$H_A(z)$$ là xác suất có đường vàng tách $$z$$ và cung $$BC$$ khỏi đỉnh $$A$$ (tương tự cho $$H_B, H_C$$).
Khi dịch chuyển $$z$$ qua một cạnh của ô lục giác, hiệu $$H_A(z') - H_A(z)$$ đúng bằng xác suất của một sự kiện "ba nhánh" (hai nhánh vàng và một nhánh xanh chạm vào cạnh đó). Nhờ **đẳng thức đổi màu** (*color-switching trick* — đảo màu một nhánh từ vàng sang xanh tại điểm rẽ mà không thay đổi xác suất ở $$p = 1/2$$, tận dụng chặt chẽ góc đối xứng $$120^\circ$$ của ô lục giác!), Smirnov chứng minh đạo hàm rời rạc của $$H_A, H_B, H_C$$ dọc theo ba hướng lệch nhau $$120^\circ$$ khớp nhau chính xác!

#### Bước 2: Qua giới hạn $$\delta \to 0$$ thu được hàm chỉnh hình và Công thức Cardy
Tổ hợp phức $$F_\delta(z) = H_A(z) + \tau H_B(z) + \tau^2 H_C(z)$$ (với $$\tau = e^{2\pi i/3}$$) thỏa **phương trình Cauchy–Riemann rời rạc**! Khi $$\delta \to 0$$, tính tiền compact (từ ước lượng Russo–Seymour–Welsh) đảm bảo $$F_\delta$$ hội tụ về một **hàm chỉnh hình** $$F$$ thỏa điều kiện biên ánh xạ $$\Omega$$ lên đúng **tam giác đều** — lập tức chứng minh **công thức Cardy–Carleson** và **tính bất biến bảo giác**!

#### Bước 3: Nối vào ngôn ngữ SLE của Schramm–Lawler–Werner
Một năm trước đó, **Oded Schramm (2000)** định nghĩa **tiến hóa Schramm–Loewner** $$\mathrm{SLE}_\kappa$$ và chứng minh nó là giới hạn bất biến bảo giác duy nhất khả dĩ cho đường biên tới hạn. Sau định lý Cardy của Smirnov (2001), chính Smirnov và **Camia–Newman** chứng minh đường thám hiểm giữa vùng vàng và vùng xanh hội tụ về **$$\mathrm{SLE}_6$$**! (Lý thuyết giải tích SLE và hình học Brown là Huy chương Fields 2006 của [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), không phải của Smirnov.)

| Đóng góp | Của ai, nói ngắn gọn |
|----------|---------------------|
| Đưa ra SLE | Schramm (2000) |
| Lý thuyết giải tích của SLE; biên ngoài của chuyển động Brown; các số mũ | Lawler–Schramm–Werner |
| Công thức Cardy và tính bất biến bảo giác cho mô hình thấm đỉnh trên lưới tam giác | Smirnov (2001) |
| Đại lượng quan sát được / đường biên của mô hình Ising phẳng | Smirnov; về sau Chelkak–Smirnov và các cộng sự |

#### Bước 4: Fermion chỉnh hình rời rạc cho Mô hình Ising phẳng (2010–2012)
Cho **mô hình Ising phẳng** tại nhiệt độ tới hạn $$\beta_c$$ (khác với lời giải năng lượng tự do năm 1944 của Onsager), **Smirnov** (*Ann. of Math.* 172, 2010) đưa ra **đại lượng fermion chỉnh hình rời rạc**: tổng có trọng số trên các đường biên spin kết thúc tại một cạnh, nhân thêm pha phức $$e^{-i\cdot\frac{1}{2}\text{góc quấn}}$$ (hệ số $$1/2$$ là chữ ký của fermion). Tại đúng $$\beta_c$$, đại lượng này thỏa tính *s-chỉnh hình rời rạc* với bài toán biên Riemann–Hilbert, hội tụ về hàm chỉnh hình bất biến bảo giác!
Cùng **Dmitry Chelkak** (*Invent. Math.* 189, 2012; [arXiv:0910.2045](https://arxiv.org/abs/0910.2045)), Smirnov mở rộng chứng minh ra **toàn bộ họ đồ thị đẳng bán kính (isoradial)** — chứng minh **tính phổ quát** cho Ising 2D trên vô số dạng lưới! Các bài tiếp theo cùng Duminil-Copin, Hongler, Kemppainen chứng minh đường biên spin Ising hội tụ về **$$\mathrm{SLE}_3$$**.

Tóm tắt cỗ máy giải tích phức rời rạc của Smirnov:

$$
\text{Mô hình lưới tới hạn}
\;\xrightarrow{\text{Đổi màu / Fermion}}\;
\text{Cauchy–Riemann rời rạc}
\;\xrightarrow{\delta \to 0}\;
\text{Hàm chỉnh hình bất biến bảo giác}
\;\longrightarrow\;
\mathrm{SLE}_6 \text{ \& } \mathrm{SLE}_3.
$$

---

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/smirnov-ising-fermion-sle_vi.mp4"></video>
</div>

Video dài khoảng 38 giây (có thuyết minh tiếng Việt): nối giới hạn thang đo tới $\mathrm{SLE}_6$, fermion chỉnh hình rời rạc cho mô hình Ising phẳng và các bài toán còn mở trên lưới vuông.

## 3. Những gì vẫn còn mở và vì sao được Fields 2010

- **Mô hình thấm cạnh tới hạn trên lưới vuông $$\mathbb{Z}^2$$** (và tính phổ quát cho mô hình thấm trên mọi lưới phẳng) vẫn chưa có chứng minh bất biến bảo giác — vì đẳng thức đổi màu năm 2001 phụ thuộc thiết yếu vào đối xứng bậc ba của lưới tam giác $$\mathbb{T}$$.
- **Bước đi tự tránh (Self-Avoiding Walk)** trong mặt phẳng, dự đoán hội tụ về $$\mathrm{SLE}_{8/3}$$, vẫn là giả thuyết mở nổi tiếng.
- Các công trình sau này của [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/) (Fields 2022) bổ sung tính bất biến quay cho mô hình FK 2D và tính liên tục/tầm thường ở chiều 3–4.

**Vì sao là Huy chương Fields 2010:** Smirnov không chỉ chứng minh một công thức đẹp; ông khai sinh phương pháp **giải tích phức rời rạc** biến các tiên đoán sâu nhất của vật lý thống kê 2D thành định lý chặt chẽ và nối liền các mô hình lưới rời rạc vào ngôi nhà SLE của Schramm–Lawler–Werner. (Cùng nhận Huy chương Fields 2010 là Lindenstrauss, Ngô Bảo Châu và [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/).)

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Smirnov chứng minh tính bất biến bảo giác của mô hình thấm trên mọi lưới." | Định lý năm 2001 dành cho **mô hình thấm đỉnh tới hạn trên lưới tam giác**. Mô hình thấm cạnh trên lưới vuông là trường hợp còn lại nổi tiếng. |
| "Cardy đã chứng minh công thức nối xuyên." | Cardy suy ra công thức bằng CFT, chưa chặt chẽ; Smirnov chứng minh nó cho mô hình thấm đỉnh trên lưới tam giác. |
| "SLE do Werner (hoặc Smirnov) phát minh." | SLE do **Schramm** đưa ra (2000). Huy chương của Werner là cho việc phát triển SLE và hình học Brown hai chiều, chủ yếu cùng Lawler và Schramm. |
| "Huy chương 2010 chỉ nói về mô hình thấm." | Lời trao giải của IMU nêu mô hình thấm **và** mô hình Ising phẳng. |
| "Lời giải Onsager chính là tính bất biến bảo giác của mô hình Ising." | Onsager tính năng lượng tự do hai chiều (1944). Tính bất biến bảo giác của đại lượng quan sát được và đường biên là một phát biểu hình học đến sau. |
| "Có SLE thì mọi mô hình hai chiều đã xong." | SLE chỉ là ứng viên cho phân phối giới hạn. Chứng minh một mô hình lưới hội tụ về SLE với một $$\kappa$$ cụ thể là một định lý riêng, thường vẫn còn mở. |

---

## Liên kết

- IMU Fields Medals 2010 (chỉ mục được yêu cầu): [mathunion.org/…/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- Trang Smirnov IMU / ICM 2010 (bản lưu hoạt động): [Fields Medal – Stanislav Smirnov](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-stanislav-smirnov.html)
- Chỉ mục Fields Medal IMU: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Wikipedia: [Stanislav Smirnov](https://en.wikipedia.org/wiki/Stanislav_Smirnov)
- arXiv: [0909.4499](https://arxiv.org/abs/0909.4499) (Smirnov, percolation tới hạn); [0910.2045](https://arxiv.org/abs/0910.2045) (Chelkak–Smirnov, Ising); tìm [Smirnov percolation Cardy](https://arxiv.org/search/?query=Smirnov+percolation+Cardy&searchtype=all)
- Khóa học: [Werner / SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/), [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/)

---

## Tài liệu tham khảo

1. International Mathematical Union, citation Fields Medals 2010 cho Stanislav Smirnov (tài liệu IMU / ICM Hyderabad 2010).
2. **S. Smirnov**, “Critical percolation in the plane: conformal invariance, Cardy’s formula, scaling limits,” *C. R. Acad. Sci. Paris Sér. I Math.* 333 (2001), 239–244; bản dài arXiv:0909.4499.
3. **J. L. Cardy**, “Critical percolation in finite geometries,” *J. Phys. A* 25 (1992), L201–L206.
4. **O. Schramm**, “Scaling limits of loop-erased random walks and uniform spanning trees,” *Israel J. Math.* 118 (2000), 221–288.
5. **D. Chelkak and S. Smirnov**, “Universality in the 2D Ising model and conformal invariance of fermionic observables,” *Invent. Math.* 189 (2012), 515–580, arXiv:0910.2045.
6. **S. Smirnov**, “Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model,” *Ann. of Math.* 172 (2010), 1441–1473.
7. Wikipedia, [Stanislav Smirnov](https://en.wikipedia.org/wiki/Stanislav_Smirnov); chân dung khóa học [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) và [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/).

---

## Hướng đi tiếp

- Đọc một bài tổng quan về lập luận đổi màu trước khi đọc bài trên *Comptes Rendus*. Sau khi đọc [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), viết nửa trang về trình tự: tiên đề của SLE → công thức Cardy → chứng minh hội tụ về $$\mathrm{SLE}_6$$.
- Bài tập thêm: viết một trang "những gì còn mở về mô hình thấm hai chiều", **không** khẳng định tính phổ quát là định lý.

## Video tham khảo

- **Xem trước**: [Stanislav Smirnov - 2d Percolation Revisited](https://www.youtube.com/watch?v=6QOnfvWqVoo) (MIT Department of Mathematics, tiếng Anh). Smirnov nhìn lại mô hình thấm hai chiều. Nên xem trước để làm quen với mô hình thấm đỉnh, thấm cạnh và câu hỏi nối xuyên.
- [Stanislav Smirnov, Percolation crossings and complex analysis](https://www.youtube.com/watch?v=6hCSSCV7lvQ) (Clay Mathematics Institute, tiếng Anh). Bài giảng về xác suất nối xuyên và vai trò của giải tích phức, đúng nội dung mục 1 và 2.
- [Stanislav Smirnov - Percolation revisited](https://www.youtube.com/watch?v=ZNpbvrhfWPA) (Department of Mathematics - Northwestern University, tiếng Anh). Một bài giảng khác cùng chủ đề. Dùng để ôn lại sau khi đọc xong bài.
