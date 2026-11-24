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

Hãy trải một bàn cờ tổ ong khổng lồ gồm hàng triệu ô lục giác, rồi với mỗi ô bạn tung một đồng xu công bằng: ngửa thì tô **vàng**, sấp thì tô **xanh**. Bây giờ bạn lùi ra thật xa cho đến khi từng ô lục giác nhỏ li ti hòa vào nhau như một bức tranh điểm ảnh, và tự hỏi: xác suất để có một con đường liên tục toàn ô màu vàng nối từ cạnh trái sang cạnh phải của một hình vẽ bất kỳ phụ thuộc vào điều gì? Các nhà vật lý thống kê dự đoán một phép màu kinh ngạc: ở đúng ngưỡng tới hạn $$p = 1/2$$, bức tranh ngẫu nhiên đó **quên sạch** hình dáng lục giác ban đầu và trở nên **bất biến bảo giác** — nếu bạn uốn cong khung tranh bằng bất kỳ ánh xạ bảo toàn góc nào (như ánh xạ giải tích phức), xác suất nối xuyên vẫn giữ nguyên không đổi!

Dự đoán ấy đẹp như mơ, nhưng suốt nhiều thập niên không ai biết cách chứng minh cho dù chỉ một mô hình lưới cụ thể. Năm 2001, bằng một bài báo ngắn gọn đến mức sững sờ chỉ dài **6 trang**, **Stanislav Smirnov** đã chứng minh công thức Cardy và tính bất biến bảo giác cho mô hình thấm đỉnh trên lưới tam giác — rồi tiếp tục phát minh ra **fermion chỉnh hình rời rạc** để chinh phục **mô hình Ising phẳng**. Năm 2010, ông nhận **Huy chương Fields**:

> “For the proof of conformal invariance of percolation and the planar Ising model in statistical physics.”  
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

*Tạm dịch: vì chứng minh tính bất biến bảo giác của mô hình thấm (percolation) và mô hình Ising phẳng trong vật lý thống kê.*

Cần đọc lời trao giải với con mắt thật tinh tường: IMU nêu chính xác **hai mô hình trên lưới**, không nói mọi mô hình phẳng tới hạn đều đã thành định lý (ngay cả mô hình thấm cạnh trên lưới vuông đến nay vẫn còn mở!). Công trình của Smirnov ghép khít với ngôn ngữ đường cong liên tục **SLE** của Oded Schramm và [Wendelin Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) (Fields 2006), và mở đường cho các định lý chuyển pha ở chiều cao của học trò ông là [Hugo Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/) (Fields 2022).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt rõ **mô hình thấm đỉnh** (*site percolation*) với **mô hình thấm cạnh** (*bond percolation*), và giải thích vì sao chỉ tại điểm tới hạn $$p_c$$ mới xuất hiện giới hạn thang đo không tầm thường.
- Mô tả trực quan **công thức Cardy** (và dạng tam giác đều cực gọn của Carleson) về xác suất nối xuyên, và biết định lý năm 2001 của Smirnov chứng minh nó cho **mô hình thấm đỉnh tới hạn trên lưới tam giác**.
- Giải thích vì sao đối xứng bậc ba của lưới tam giác đóng vai trò sống còn trong chứng minh năm 2001, và vì sao **mô hình thấm cạnh trên lưới vuông** vẫn còn mở về tính bất biến bảo giác.
- Phân định rành mạch vai trò: **Schramm** định nghĩa SLE, **Lawler–Schramm–Werner** xây dựng lý thuyết giải tích của SLE, còn **Smirnov** chứng minh các mô hình lưới rời rạc hội tụ về giới hạn bất biến bảo giác.
- Giải thích ý chính của **fermion chỉnh hình rời rạc** trong chứng minh tính bất biến bảo giác và tính phổ quát của **mô hình Ising phẳng** (Smirnov; Chelkak–Smirnov trên đồ thị đẳng bán kính).
- Tránh những tuyên bố quá mức như "Smirnov đã giải xong vật lý thống kê hai chiều" hay nhầm định lý bất biến bảo giác với lời giải Onsager (1944).

**Kiến thức nền.** Hàm chỉnh hình và ánh xạ bảo giác giữa các miền phẳng ở mức giáo trình giải tích phức nhập môn; biến ngẫu nhiên Bernoulli và ý tưởng giới hạn thang đo (bước lưới $$\delta\to 0$$); sự khác nhau giữa mô hình rời rạc và quá trình liên tục. Không cần học trước về SLE.

**Liên kết với các bài khác.** Bài này cho thấy một dự đoán vật lý trở thành định lý gắn với một lưới cụ thể, và mối nối giữa mô hình rời rạc với hình học bảo giác liên tục. Đọc cùng [Werner / SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) để hiểu ngôn ngữ đường cong, và [Duminil-Copin]({{ site.baseurl }}/contents/vi/chapter02/02_19_Duminil_Copin_Phase_Transitions/) cho các kết quả sắc nét về chuyển pha.

---

## Bản đồ kiến thức nền: Tính bất biến bảo giác và giải tích phức rời rạc là gì?

Tại sao giải tích phức — ngành toán học về những hàm trơn mượt nhất — lại đột ngột trở thành vũ khí tối thượng để nghiên cứu các trò chơi tung đồng xu rời rạc trên lưới?

**1. Ánh xạ bảo giác (Conformal map) — phép biến dạng giữ nguyên góc.**
Trong giải tích phức, một hàm chỉnh hình $$f: \Omega_1 \to \Omega_2$$ có đạo hàm $$f'(z) \neq 0$$ là một **ánh xạ bảo giác**: ở thang rất nhỏ quanh mỗi điểm, nó chỉ phóng to/thu nhỏ và xoay chứ **không làm méo góc** giữa hai đường cong cắt nhau. Theo định lý ánh xạ Riemann, bất kỳ miền đơn liên nào (như hình vuông, hình tròn, hình tam giác, hay hình quả đậu) đều có thể biến đổi bảo giác sang đĩa đơn vị! Nếu một mô hình vật lý tới hạn trên mặt phẳng có **tính bất biến bảo giác**, điều đó có nghĩa là ta chỉ cần giải bài toán trên một hình cực đơn giản (như tam giác đều), rồi dùng ánh xạ bảo giác để tự động suy ra đáp số cho *mọi* hình dạng miền khác!

**2. Thấm đỉnh (Site) và Thấm cạnh (Bond) — hai biến thể của cùng một trò chơi.**
- **Thấm đỉnh trên lưới tam giác $$\mathbb{T}$$** (tương đương tô màu các ô lục giác của lưới tổ ong đối ngẫu): mỗi ô lục giác được tô vàng với xác suất $$p$$ hoặc xanh với xác suất $$1-p$$. Điểm tới hạn chính xác là $$p_c = 1/2$$: tại đúng $$p = 1/2$$, có sự đối xứng hoàn hảo giữa hai màu (hoặc có đường vàng nối trái–phải, hoặc có đường xanh chắn trên–dưới, không bao giờ xảy ra cả hai!).
- **Thấm cạnh trên lưới vuông $$\mathbb{Z}^2$$:** ta mở/đóng từng cạnh nối hai đỉnh vuông với xác suất $$p$$ (cũng có $$p_c = 1/2$$). Trực giác vật lý tin rằng ở giới hạn bước lưới $$\delta \to 0$$, cả hai lưới đều cho *cùng một* giới hạn bảo giác (**tính phổ quát**), nhưng toán học hiện tại mới chứng minh được cho lưới tam giác!

**3. Chiến lược "đại lượng chỉnh hình rời rạc" (Discrete holomorphic observable).**
Làm thế nào để chứng minh một xác suất trên lưới hội tụ về một hàm chỉnh hình (hoặc điều hòa) khi bước lưới $$\delta \to 0$$? Ý tưởng thiên tài của Smirnov là xây dựng ngay trên lưới rời rạc một hàm $$F_\delta$$ (đo xác suất nối xuyên hoặc tương quan spin) sao cho nó thỏa mãn **phương trình Cauchy–Riemann rời rạc** (tổng các giá trị xung quanh mỗi ô nhỏ bằng $$0$$)! Khi cho $$\delta \to 0$$, hàm giới hạn tự động thỏa phương trình Cauchy–Riemann liên tục — tức là một **hàm chỉnh hình** xác định duy nhất bởi điều kiện biên!

---

## 1. Từ bài toán cổ điển đến ý tưởng đột phá: công thức Cardy và dự đoán CFT

Khi tô màu ngẫu nhiên một hình chữ nhật lớn với xác suất $$p$$:
- Nếu $$p < p_c$$, mọi cụm mở đều nhỏ xíu, xác suất có đường nối xuyên từ trái sang phải tiến nhanh về $$0$$ khi lưới mịn dần ($$\delta \to 0$$).
- Nếu $$p > p_c$$, có cụm khổng lồ phủ khắp nơi, xác suất nối xuyên tiến về $$1$$.
- Chỉ tại đúng **điểm tới hạn** $$p = p_c$$, xác suất nối xuyên giữ giá trị không tầm thường nằm strictly trong $$(0,1)$$!

Năm 1992, bằng các công cụ vật lý (chưa chặt chẽ về toán học) của **lý thuyết trường bảo giác (CFT)**, nhà vật lý **John Cardy** đưa ra một công thức tường minh (dùng hàm siêu bội) cho xác suất nối xuyên trong giới hạn của bất kỳ miền đơn liên $$\Omega$$ nào có 4 điểm đánh dấu $$A, B, C, D$$ trên biên (gọi là một "hình chữ nhật bảo giác"). Không lâu sau, **Lennart Carleson** phát hiện một điều kỳ diệu: nếu dùng ánh xạ bảo giác để biến miền $$(\Omega; A, B, C, D)$$ thành một **tam giác đều** $$ABC$$ có cạnh bằng $$1$$, với điểm $$D$$ nằm trên cạnh $$AC$$ cách $$C$$ một đoạn $$x \in [0, 1]$$, thì công thức siêu bội rắc rối của Cardy bỗng sụp gọn thành một biểu thức đơn giản đến khó tin:

$$
\mathbb{P}(\text{có đường mở nối cung } AB \text{ với cung } CD) = x!
$$

Xác suất nối xuyên đơn giản chỉ bằng **tỷ lệ độ dài đoạn $$CD$$**! Thử nghiệm mô phỏng máy tính của Langlands–Pouliot–Saint-Aubin khớp hoàn hảo với công thức này. Nhưng suốt một thập kỷ, việc *chứng minh toán học* rằng giới hạn đó tồn tại và bằng đúng $$x$$ vẫn là bức tường không ai vượt qua được.

---

## 2. Đột phá năm 2001: mô hình thấm đỉnh trên lưới tam giác

Năm 2001, trên *Comptes Rendus de l'Académie des Sciences* (bản mở rộng là [arXiv:0909.4499](https://arxiv.org/abs/0909.4499)), **Stanislav Smirnov** tung ra một chứng minh đẹp như một bản giao hưởng ngắn. Xét mô hình thấm đỉnh tới hạn ($$p = 1/2$$) trên lưới tam giác $$\mathbb{T}$$ (tô màu vàng/xanh các ô lục giác) trong một miền $$\Omega$$ có ba cung biên $$AB, BC, CA$$. Với mỗi điểm $$z$$ bên trong miền, Smirnov xét ba hàm xác suất:
- $$H_A(z)$$: xác suất tồn tại đường vàng tách điểm $$z$$ và cung $$BC$$ khỏi đỉnh $$A$$;
- Tương tự cho $$H_B(z)$$ và $$H_C(z)$$.

Nhờ phép **đổi màu khéo léo** (*color-switching trick*) — một phép song ánh tổ hợp dựa trực tiếp vào hình học đối xứng bậc ba (góc $$120^\circ$$) của các ô lục giác — Smirnov chứng minh rằng sai phân của $$H_A, H_B, H_C$$ dọc theo các cạnh của lưới lục giác thỏa mãn đúng một hệ phương trình **Cauchy–Riemann rời rạc**! Khi cho bước lưới $$\delta \to 0$$, tổ hợp tuyến tính phức $$H_A + \tau H_B + \tau^2 H_C$$ (với $$\tau = e^{2\pi i/3}$$) hội tụ về ánh xạ bảo giác đưa $$\Omega$$ thành tam giác đều — và ngay tại biên $$AC$$, giá trị của $$H_C(D)$$ rơi ra chính xác bằng tọa độ tuyến tính $$x$$ trong **công thức Cardy–Carleson**!

**Điểm cần nhấn mạnh để không nói sai:** Đẳng thức đổi màu của Smirnov tận dụng chặt chẽ đối xứng bậc ba của lưới tam giác $$\mathbb{T}$$. Vì thế định lý 2001 chỉ chứng minh cho **mô hình thấm đỉnh tới hạn trên lưới tam giác**. Trường hợp nổi tiếng còn lại — **mô hình thấm cạnh tới hạn trên lưới vuông $$\mathbb{Z}^2$$** — đến tận ngày nay vẫn là một bài toán mở lớn về tính bất biến bảo giác!

---

## 3. Từ xác suất nối xuyên tới đường cong: SLE là ngôn ngữ của giới hạn

Xác suất nối xuyên là một con số bất biến bảo giác; còn bức tranh hình học sống động hơn nhiều là **đường thám hiểm** (*exploration path*) — đường biên zíc-zắc chạy len lỏi giữa cụm ô màu vàng bên trái và cụm ô màu xanh bên phải.

Chỉ một năm trước bài báo của Smirnov, **Oded Schramm** (2000) đã đặt ra họ quá trình ngẫu nhiên **tiến hóa Schramm–Loewner** $$\mathrm{SLE}_\kappa$$ (điều khiển bởi chuyển động Brown với phương sai $$\kappa$$), và chứng minh: nếu giới hạn thang đo của đường thám hiểm tồn tại, bất biến bảo giác và có tính chất Markov miền, thì nó *bắt buộc* phải là $$\mathrm{SLE}_\kappa$$ với một tham số $$\kappa$$ nào đó (với mô hình thấm là $$\kappa = 6$$). Tiếp đó, **Lawler–Schramm–Werner** xây dựng toàn bộ lý thuyết giải tích của SLE (nội dung Huy chương Fields 2006 của [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/)).

Ngay khi Smirnov chứng minh được công thức Cardy (2001), mảnh ghép còn thiếu lập tức khớp vào nhau: chính Smirnov (và chi tiết hóa bởi **Camia–Newman**) chứng minh rằng đường thám hiểm của mô hình thấm đỉnh trên lưới tam giác thực sự hội tụ theo phân phối về **$$\mathrm{SLE}_6$$** — và nhờ đó, toàn bộ các số mũ tới hạn nổi tiếng của mô hình thấm 2D (như chiều Hausdorff của biên cụm bằng $$7/4$$, xác suất đường đi xuyên không cắt nhau) lần đầu tiên trở thành định lý toán học chặt chẽ!

| Đóng góp | Của ai, nói ngắn gọn |
|----------|---------------------|
| Đưa ra SLE | Schramm (2000) |
| Lý thuyết giải tích của SLE; biên ngoài của chuyển động Brown; các số mũ | Lawler–Schramm–Werner |
| Công thức Cardy và tính bất biến bảo giác cho mô hình thấm đỉnh trên lưới tam giác | Smirnov (2001) |
| Đại lượng quan sát được / đường biên của mô hình Ising phẳng | Smirnov; về sau Chelkak–Smirnov và các cộng sự |

---

## 4. Mô hình Ising phẳng và fermion chỉnh hình rời rạc

Thành tựu lớn thứ hai trong lời trao giải năm 2010 của Smirnov là **mô hình Ising phẳng** (các spin $$\sigma_x = \pm 1$$ đặt trên đỉnh đồ thị phẳng, tương tác với hàng xóm ở đúng nhiệt độ tới hạn $$\beta_c$$). Dù **Lars Onsager** (1944) đã tính chính xác năng lượng tự do của mô hình Ising 2D trên lưới vuông, việc chứng minh **toàn bộ hình học tới hạn** (hàm tương quan spin và đường biên giữa cụm spin $$+1$$ và $$-1$$) có giới hạn bất biến bảo giác lại là một thách thức ở tầm mức hoàn toàn khác.

Năm 2010 (*Annals of Mathematics*), **Smirnov** đưa ra **đại lượng quan sát fermion chỉnh hình rời rạc** (*discrete holomorphic fermionic observable*) cho mô hình Ising và mô hình cụm ngẫu nhiên FK $$q = 2$$: ông gán cho mỗi cạnh trên lưới một số phức tính bằng tổng có trọng số trên tất cả các cấu hình đường biên kết thúc tại cạnh đó, nhân với một pha phức $$e^{-i \cdot \frac{1}{2} \text{góc quấn}}$$ (hệ số $$1/2$$ mang bản chất spinor/fermion!). Nhờ phép triệt tiêu cục bộ kỳ diệu tại đúng nhiệt độ tới hạn, đại lượng fermion này thỏa phương trình **Cauchy–Riemann rời rạc (tính s-chỉnh hình)** với điều kiện biên kiểu Riemann–Hilbert — và khi bước lưới $$\delta \to 0$$, nó hội tụ về một hàm chỉnh hình bất biến bảo giác tường minh!

Bước tiến ngoạn mục hơn nữa diễn ra trong công trình chung **Dmitry Chelkak và Stanislav Smirnov** (*Inventiones Mathematicae*, 2012; [arXiv:0910.2045](https://arxiv.org/abs/0910.2045)): họ chứng minh đại lượng fermion chỉnh hình hoạt động không chỉ trên lưới vuông mà trên **toàn bộ lớp đồ thị đẳng bán kính (isoradial)** — tức là **tính phổ quát** (*universality*) và bất biến bảo giác cho mô hình Ising 2D trên vô số dạng lưới khác nhau! Tiếp theo đó, Chelkak, Duminil-Copin, Hongler, Kemppainen và Smirnov chứng minh các đường biên spin của mô hình Ising 2D hội tụ về **$$\mathrm{SLE}_3$$** (và đường biên FK hội tụ về $$\mathrm{SLE}_{16/3}$$).

Như vậy, có một điểm đối lập rất thú vị: với mô hình **Ising 2D**, lý thuyết fermion chỉnh hình đã chứng minh được tính phổ quát trên cả họ đồ thị đẳng bán kính rộng lớn; trong khi với **mô hình thấm**, định lý bất biến bảo giác vẫn chỉ mới khóa chặt được trên lưới tam giác!

---

## 5. Cách xây dựng chứng minh, và vì sao được Fields

Cả hai đột phá của Smirnov đều vận hành theo một sơ đồ giải tích phức rời rạc cực kỳ sáng sủa:
1. Thiết kế một đại lượng rời rạc $$F_\delta$$ trên lưới mã hóa đúng sự kiện xác suất cần tìm (nối xuyên hoặc đường biên spin);
2. Khai thác một đẳng thức tổ hợp tinh tế của lưới tại đúng điểm tới hạn (đổi màu trên lưới tam giác; tính khả tích fermion của Ising) để chứng minh $$F_\delta$$ thỏa **hệ Cauchy–Riemann rời rạc**;
3. Dùng tính tiền compact để trích dãy con hội tụ khi $$\delta \to 0$$, rồi dùng tính duy nhất nghiệm của bài toán biên liên tục (Dirichlet hoặc Riemann–Hilbert) để khẳng định giới hạn là duy nhất và **bất biến bảo giác**.

Huy chương Fields 2010 không phải phần thưởng cho việc "đoán đúng công thức Cardy". Nó tôn vinh việc Smirnov đã biến các tiên đoán sâu sắc nhất của vật lý thống kê hai chiều thành định lý chặt chẽ, khai sinh phương pháp **giải tích phức rời rạc** làm thay đổi bộ mặt cơ học thống kê, và tạo ra cầu nối thực sự để gắn $$\mathrm{SLE}_6$$ và $$\mathrm{SLE}_3$$ với các mô hình lưới cụ thể. (Cùng nhận Huy chương Fields năm 2010 là Elon Lindenstrauss, Ngô Bảo Châu và [Cédric Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/).)

---

## 6. Những gì vẫn còn mở

Sau hai thập kỷ, nhiều bài toán lớn ngay sát cạnh định lý của Smirnov vẫn đang chờ lời giải:
- **Mô hình thấm cạnh tới hạn trên lưới vuông $$\mathbb{Z}^2$$** (và tính phổ quát cho mô hình thấm trên mọi lưới phẳng) vẫn chưa có chứng minh bất biến bảo giác.
- **Đường đi tự tránh (Self-Avoiding Walk)** trong mặt phẳng, dự đoán có giới hạn thang đo là $$\mathrm{SLE}_{8/3}$$, vẫn là một giả thuyết mở nổi tiếng (dù Duminil-Copin và Smirnov đã tính chính xác hằng số liên thông trên lưới tổ ong năm 2012).
- Các mô hình cụm ngẫu nhiên FK với $$q \in (1, 4)$$ nói chung (ngoài $$q = 2$$) mới đạt đến tính bất biến quay (Duminil-Copin và cộng sự), chưa đạt tính bất biến bảo giác đầy đủ.

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
