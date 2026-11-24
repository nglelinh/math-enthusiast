---
layout: post
title: "Vận chuyển Tối ưu"
chapter: '06'
order: 9
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Năm 1781, kỹ sư quân sự kiêm nhà toán học người Pháp Gaspard Monge đứng trước một bài toán rất trần tục: cần san một đống đất lớn sang lấp những hố công sự gần đó sao cho tổng công gánh đất là nhỏ nhất. Hơn một thế kỷ rưỡi sau, nhà toán học Liên Xô Leonid Kantorovich gặp lại đúng bài toán ấy khi tối ưu hóa mạng lưới vận tải nguyên liệu giữa các nhà máy — và lời giải quy hoạch tuyến tính của ông đã mang về giải Nobel Kinh tế năm 1975.

Ít ai ngờ rằng câu hỏi "chuyển cát lấp hố" tưởng chừng cổ xưa ấy ngày nay lại trở thành một trong những ngôn ngữ trung tâm của toán học hiện đại và trí tuệ nhân tạo. Khi thay "đống cát" bằng **phân phối xác suất**, bài toán của Monge–Kantorovich biến thành công cụ tuyệt vời để đo khoảng cách giữa hai đám mây dữ liệu, biến hình mượt mà giữa hai bức ảnh, mô tả phương trình nhiệt như một dòng chảy tối ưu, và thiết kế các mô hình sinh. **Vận chuyển tối ưu (Optimal Transport — OT)** nằm đúng ngã tư nơi giải tích, xác suất, tối ưu lồi và khoa học dữ liệu bắt tay nhau.

Bài này trình bày hành trình từ bài toán Monge, bản nới lỏng của Kantorovich, khoảng cách Wasserstein, đối ngẫu Kantorovich–Rubinstein, đến thuật toán Sinkhorn và các ứng dụng hiện đại — luôn giữ thói quen phân biệt rạch ròi đâu là định lý, đâu là xấp xỉ số và đâu là lời thổi phồng kiểu “Wasserstein GAN đã giải xong mô hình sinh”.

---

## Bản đồ kiến thức nền: Vận chuyển tối ưu là gì và nghiên cứu những gì?

Nếu bạn đã quen với xác suất và tối ưu hóa bậc đại học, có lẽ bạn từng dùng phân kỳ KL (Kullback–Leibler) hay sai số bình phương để so sánh hai phân phối xác suất. Nhưng các thước đo truyền thống chỉ so sánh chiều cao của hai đồ thị *tại cùng một tọa độ*, nên chúng hoàn toàn mù trước hình học không gian: hai ngọn đồi giống hệt nhau nằm cách nhau 1 cm hay 100 km đều cho cùng một giá trị KL bằng vô cùng nếu chúng không chồng lên nhau!

**Lý thuyết Vận chuyển Tối ưu** (Optimal Transport) khắc phục điểm mù đó bằng cách hỏi: *"Tốn ít nhất bao nhiêu công sức để đẩy khối lượng của phân phối $$\mu$$ thành hình dạng của phân phối $$\nu$$?"* Ngành này đứng trên **bốn trụ cột**:

1. **Bài toán Monge và bản nới lỏng Kantorovich:** Từ ánh xạ đẩy từng điểm $$T(x)$$ (đôi khi không tồn tại vì không cho phép chia nhỏ khối lượng) đến kế hoạch ghép nối (*coupling*) $$\pi(x,y)$$ — biến một bài toán phi tuyến cực khó thành quy hoạch tuyến tính lồi.
2. **Khoảng cách Wasserstein ($$W_p$$) và hình học không gian độ đo:** Biến tập hợp tất cả các phân phối xác suất thành một không gian hình học thực thụ, nơi ta có thể lấy trung bình hình học của hai phân phối (Wasserstein barycenter) và định nghĩa các đường trắc địa biến hình mượt mà.
3. **Đối ngẫu Kantorovich–Rubinstein:** Thay vì tìm kế hoạch vận chuyển (góc nhìn nhà vận tải), ta tìm bảng giá mua–bán tại từng địa điểm sao cho chênh lệch giá không vượt quá chi phí chở hàng (góc nhìn nhà kinh tế).
4. **OT tính toán (Computational OT — Sinkhorn):** Thêm điều chuẩn entropy để biến bài toán quy hoạch tuyến tính nặng nề thành phép nhân–chia ma trận siêu nhanh chạy mượt trên GPU.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Phát biểu bài toán Monge: tìm ánh xạ $$T$$ đẩy $$\mu$$ thành $$\nu$$ với chi phí nhỏ nhất; và vì sao ánh xạ như vậy có thể không tồn tại.
- Viết công thức **Kantorovich** trên các coupling $$\pi$$ có biên cố định.
- Định nghĩa khoảng cách **Wasserstein** $$W_p$$ và diễn giải việc $$W_1$$ nhạy với hình học.
- Nêu đối ngẫu Kantorovich–Rubinstein cho $$W_1$$ (hàm Lipschitz).
- Mô tả điều chuẩn entropy dẫn đến Sinkhorn: được gì và mất gì so với OT chính xác.
- Nhận xét những tuyên bố trong ML dùng “Wasserstein” như từ thời thượng mà không nêu hàm chi phí hay cách ước lượng.

**Kiến thức nền.** Phân phối như một độ đo (tích phân của hàm thử); tối ưu cơ bản; khoảng cách Euclid. Biết giải tích lồi thì thuận lợi, nhưng không đòi hỏi đầy đủ.

---

### Video ngắn: Trên đường thẳng, sắp theo thứ tự là tối ưu

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/optimal-transport-1d_vi.mp4"></video>
</div>

Sáu đống cát phải lấp sáu cái hố với chi phí = $$(\text{quãng đường})^2$$. Mỗi lần hai đường cắt nhau, đổi chỗ hai hố làm tổng chi phí giảm; khi không còn đường cắt nhau, phép ghép theo thứ tự và rẻ nhất trong cả 720 phép ghép.


### Tự tay thử: Ghép đống cát với hố

<div class="mex-explainer" data-mex="ot" data-lang="vi"></div>


## 1. Bài toán Monge

Cho $$\mu,\nu$$ trên không gian $$X$$ (có thể nghĩ là $$\mathbb{R}^d$$) và hàm chi phí $$c(x,y)$$, hãy tìm ánh xạ $$T$$ thỏa $$T_\#\mu=\nu$$ sao cho cực tiểu

$$
\int c\bigl(x,T(x)\bigr)\,d\mu(x).
$$

Mỗi “hạt” ở $$x$$ đi đến đúng một chỗ $$T(x)$$. Ánh xạ như vậy có thể không tồn tại: hãy tưởng tượng một kho hàng duy nhất ở vị trí $$0$$ chứa 1 tấn cát ($$\mu = \delta_0$$), còn đích đến là hai hố ở $$-1$$ và $$+1$$, mỗi hố cần 0.5 tấn ($$\nu = \frac{1}{2}\delta_{-1} + \frac{1}{2}\delta_1$$). Vì một hàm số $$T$$ chỉ có thể gửi điểm $$0$$ tới *một* giá trị duy nhất $$T(0)$$, bài toán Monge vô nghiệm! Ngay cả khi tồn tại, việc mô tả $$T$$ cũng không tầm thường. Với $$c=\|x-y\|^2$$ trên $$\mathbb{R}^d$$, dưới điều kiện chính quy ($$\mu$$ có mật độ liên tục), định lý Brenier liên hệ ánh xạ tối ưu với gradient của một thế lồi: $$T=\nabla\phi$$.

---

## 2. Nới lỏng Kantorovich: coupling

Ta cho phép **tách khối lượng** bằng một phân phối đồng thời $$\pi$$ trên $$X\times X$$ có hai biên là $$\mu,\nu$$:

$$
\inf_{\pi\in\Pi(\mu,\nu)}\int c(x,y)\,d\pi(x,y),
$$

với $$\Pi(\mu,\nu)$$ là tập các coupling. Quay lại ví dụ kho hàng ở $$0$$ và hai hố ở $$\pm 1$$: kế hoạch Kantorovich đơn giản chia đôi khối lượng, đặt $$\pi(0, -1) = 0.5$$ và $$\pi(0, 1) = 0.5$$. Đây là một bài toán quy hoạch tuyến tính vô hạn chiều. Kế hoạch tối ưu là $$\pi$$; khi $$\pi$$ tập trung trên đồ thị của một ánh xạ thì ta quay về bài toán Monge.

Dạng này mở ra đối ngẫu lồi và một lý thuyết tồn tại đã chín muồi; nó là điểm xuất phát mặc định của OT hiện đại.

---


<div class="interactive-demo" markdown="1">
<div data-demo="ot-explainer" data-preset="threeBars" data-lang="vi"></div>
</div>
<script src="{{ '/public/js/explainers/ot-explainer.js' | relative_url }}"></script>

## 3. Khoảng cách Wasserstein

Với $$p\ge 1$$ và các độ đo có moment bậc $$p$$ hữu hạn:

$$
W_p(\mu,\nu)=\Bigl(\inf_{\pi\in\Pi(\mu,\nu)}\int\|x-y\|^p\,d\pi\Bigr)^{1/p}
$$

(trên $$\mathbb{R}^d$$ với chi phí Euclid; trên không gian metric khác thì dùng $$d(x,y)^p$$). $$W_p$$ metric hóa sự hội tụ yếu cộng với hội tụ moment (với điều kiện phù hợp), và phản ánh hình học trung thực hơn khoảng cách biến thiên toàn phần (TV) hay phân kỳ KL khi các giá của hai phân phối lệch nhau.

Hãy so sánh trực tiếp hai phân phối điểm $$\delta_0$$ và $$\delta_\theta$$ (với $$\theta > 0$$):
- Phân kỳ KL giữa chúng bằng $$+\infty$$ với mọi $$\theta \neq 0$$, rồi đột ngột rơi về $$0$$ đúng lúc $$\theta = 0$$ — gradient gần như vô ích!
- Khoảng cách biến thiên toàn phần bằng $$1$$ với mọi $$\theta \neq 0$$, cũng phẳng lỳ không cho biết phải đẩy $$\theta$$ về hướng nào.
- Trong khi đó, $$W_1(\delta_0, \delta_\theta) = \lvert\theta\rvert$$ — giảm tuyến tính và mượt mà đúng bằng khoảng cách hình học khi $$\theta \to 0$$.

**Hình học của không gian các độ đo.** Không gian các độ đo có moment bậc hai hữu hạn với khoảng cách $$W_2$$ có cấu trúc rất giàu (giải tích Otto, tính lồi trắc địa của một số phiếm hàm). Đây là biên giới giữa giải tích và PDE (dòng nhiệt là dòng gradient của entropy trong không gian Wasserstein).

---

## 4. Đối ngẫu (mặt hữu dụng)

Với $$c=\|x-y\|$$, ta có công thức Kantorovich–Rubinstein:

$$
W_1(\mu,\nu)=\sup_{\|f\|_{\mathrm{Lip}}\le 1}\Bigl(\int f\,d\mu-\int f\,d\nu\Bigr).
$$

$$W_1$$ chính là đối ngẫu qua các hàm Lipschitz với hằng số không quá 1. Trực giác kinh tế của công thức này rất dễ nhớ: thay vì tự chở cát từ $$x$$ sang $$y$$ với chi phí $$\|x-y\|$$, bạn thuê một công ty trung gian mua cát tại $$x$$ với giá $$f(x)$$ và bán lại tại $$y$$ với giá $$f(y)$$. Để không ai tự chở rẻ hơn, công ty phải đặt bảng giá sao cho $$f(x) - f(y) \le \|x-y\|$$ (chính là điều kiện 1-Lipschitz!). Lợi nhuận tối đa mà công ty có thể thu về đúng bằng chi phí vận chuyển tối ưu $$W_1(\mu,\nu)$$.

Đối ngẫu này là cơ sở cho các chặn thống kê, cho cách diễn giải tối ưu bền vững, và cho một số công thức của mô hình sinh (critic Lipschitz, **về mặt lý thuyết**; trong thực hành, ràng buộc chỉ được xấp xỉ).

Với chi phí tổng quát hơn, ta có các thế $$c$$-lõm và cấu trúc độ lệch bù (complementary slackness), tức tính $$c$$-đơn điệu theo chu trình của giá của kế hoạch tối ưu.

---

## 5. Tính toán: từ LP đến Sinkhorn

Với độ đo rời rạc gồm $$n$$ điểm, OT chính xác là một bài toán LP với $$n^2$$ biến: giải được, nhưng đắt khi $$n$$ lớn. **Điều chuẩn entropy** thêm số hạng $$\varepsilon\mathrm{KL}(\pi\|\mu\otimes\nu)$$ (hoặc tương tự), cho một bài toán lồi chặt giải được bằng **Sinkhorn–Knopp**, tức là co giãn hàng và cột của ma trận. Khi $$\varepsilon\to 0$$ ta tiến về OT; với $$\varepsilon>0$$ kế hoạch bị làm mờ và đại lượng thu được đổi tính chất (phân kỳ Sinkhorn cần khử lệch trong một số cách dùng thống kê).

Còn có những đường khác: thuật toán đấu giá, network simplex, đa thang, Wasserstein cắt lát (chiếu xuống 1D rồi lấy trung bình), và công thức động Benamou–Brenier theo kiểu cơ học chất lỏng bằng PDE.

**Cần đọc cho kỹ.** “Dùng Wasserstein” có thể là OT chính xác, OT entropy, cắt lát, mini-batch có thiên lệch, hoặc một hình phạt đối ngẫu lỏng, và các cách này **không thể thay thế cho nhau** về mặt thống kê.

---

## 6. Ứng dụng

| Lĩnh vực | Vai trò của OT |
|----------|----------------|
| Thống kê | Metric giữa các phân phối; ước lượng bền vững |
| Thị giác / đồ họa | Chuyển màu, nội suy hình, đăng ký ảnh |
| Kinh tế | Ghép cặp, phân công (nguồn gốc lịch sử) |
| ML sinh | Khớp phân phối; heuristic đối ngẫu của WGAN; mô hình quỹ đạo |
| Sinh học | So sánh phân bố biểu hiện; suy luận quỹ đạo (cần thận trọng) |
| PDE / vật lý | Dòng gradient; phương trình tập hợp–khuếch tán |

**Thổi phồng.** WGAN phổ biến hóa đối ngẫu Lipschitz; việc huấn luyện ổn định là chuyện thực nghiệm, phụ thuộc kiến trúc, chứ không phải hệ quả thuần túy của Kantorovich–Rubinstein. Ước lượng theo mini-batch ở số chiều cao có thể bị thiên lệch nặng.

---

## 7. Số chiều cao và độ phức tạp mẫu

Để ước lượng $$W_p$$ liên tục ở số chiều cao từ mẫu, ở một số chế độ ta có thể cần cỡ mẫu tăng mũ theo số chiều, một biểu hiện của lời nguyền số chiều. Cấu trúc (chiều nội tại, độ trơn) và việc đổi sang một phân kỳ khác làm đổi tốc độ. Đây là thống kê toán học đang hoạt động: không phải lý do để bỏ OT, nhưng là lý do để tránh những khẳng định ngây thơ.

---

## 8. Các hướng tiên phong

1. Tốc độ thống kê của OT và của Sinkhorn đã khử lệch.  
2. OT trên đồ thị, mạng và các không gian không Euclid.  
3. Đa biên (multi-marginal) và barycenter Wasserstein.  
4. Vận chuyển không cân bằng, và vận chuyển nhân quả (có tạo và hủy khối lượng).  
5. Dòng gradient trên không gian đo có metric và mối liên hệ với lấy mẫu.  
6. OT có cấu trúc ở quy mô lớn cho mô hình sinh, với đánh giá trung thực.

### Ví dụ rời rạc $$2\times 2$$

Khối lượng $$a=(0.5,0.5)$$ tại $$x_1,x_2$$ và $$b=(0.5,0.5)$$ tại $$y_1,y_2$$: coupling là một ma trận $$2\times 2$$ không âm với tổng hàng và tổng cột đúng bằng các khối lượng đã cho. Chi phí là $$\sum\pi_{ij}c_{ij}$$. Nếu $$c_{11},c_{22}$$ rẻ còn hai ô chéo kia đắt thì kế hoạch tối ưu ưu tiên đường chéo; nếu hình học đảo ngược thì kế hoạch cũng đảo theo. LP tìm ra nghiệm tối ưu; với bài nhỏ, ta có thể liệt kê đa diện một chiều của các coupling.

OT entropy làm mục tiêu mượt hơn (thường có nghiệm duy nhất); Sinkhorn co giãn hàng và cột. Quan sát phép lặp hội tụ trên bài $$3\times 3$$ đáng giá hơn cả nghìn slide.

### Vì sao hình học của các độ đo quan trọng đối với việc học

Với mô hình sinh, ta muốn đẩy tới $$G_\#\eta$$ gần với độ đo dữ liệu $$\mu$$. Mỗi phân kỳ cho một hình học khác (ưu tiên một mode hay phủ toàn bộ khối lượng), một độ nhạy khác với điểm ngoại lai, và độ phức tạp mẫu khác. Wasserstein tính phí cho việc chuyển khối lượng qua không gian, nên nó phản ánh việc “phân phối gần nhau” tốt hơn KL khi giá lệch nhau, **với điều kiện** metric nền có ý nghĩa và bộ ước lượng không bị thiên lệch phá hỏng.

### Hoạt động nhóm

Tìm một bài báo ML có chữ “Wasserstein”. Kiểm tra theo danh sách: chi phí $$c$$ là gì? rời rạc hay liên tục? bộ giải là chính xác, Sinkhorn, cắt lát hay mini-batch? có khử lệch không? Viết một đoạn: khẳng định hình học nào *thực sự* được công thức bảo vệ, khẳng định nào chỉ là quảng cáo.

---

## Những nhầm lẫn thường gặp

| Tuyên bố | Chỉnh lại |
|----------|-----------|
| “Wasserstein chính là EMD.” | Gần đúng với $$W_1$$ rời rạc; họ $$W_p$$ rộng hơn. |
| “OT luôn cho một ánh xạ $$T$$.” | Kế hoạch có thể tách khối lượng. |
| “Sinkhorn là OT chính xác.” | Điều chuẩn làm lệch mục tiêu. |
| “WGAN huấn luyện đúng $$W_1$$.” | Ràng buộc Lipschitz chỉ được xấp xỉ. |
| “KL và $$W_p$$ đo sự không khớp như nhau.” | Tô-pô và độ nhạy khác nhau. |
| “OT tự giải được bài toán thích nghi miền.” | Là công cụ hữu ích; thành công mang tính thực nghiệm và phụ thuộc giả thiết. |

---

## Tóm tắt từ phần nghiên cứu video

Phần này dùng cho buổi seminar; hãy đối chiếu với nguồn gốc và không coi là bản chép lời.

### Hiện trạng

**Lý thuyết đã chín muồi, ứng dụng đang bùng nổ.** Lý thuyết Monge–Kantorovich là cổ điển; Sinkhorn (OT entropy) và các dòng gradient là những động cơ tính toán hiện đại.

### Phát biểu cốt lõi

Bài toán Kantorovich: $$\inf_{\pi\in\Pi(\mu,\nu)}\int c\,d\pi$$. Khoảng cách Wasserstein-$$p$$ metric hóa hội tụ yếu (trên các không gian phù hợp). Brenier: dưới các điều kiện nhất định, ánh xạ tối ưu là gradient của một thế lồi.

### Định nghĩa cần nhớ

- **Coupling.** Phân phối đồng thời $$\pi$$ có các biên là $$\mu,\nu$$.
- **Sinkhorn.** Điều chuẩn entropy của OT, giải bằng co giãn ma trận.

### Cần phân biệt rõ

- Cho rằng OT luôn cho một ánh xạ Monge tất định, kể cả trong các bối cảnh rời rạc có khối lượng bằng nhau hoặc không cân bằng mà không có giả thiết.
- Bỏ qua việc độ phức tạp mẫu của W_p thực nghiệm tăng vọt khi số chiều cao.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh hay bài báo gốc khi cần khẳng định điều quan trọng.

**Thứ tự gợi ý**

1. **Cốt lõi**: Villani, Optimal Transport Theory (Imperial College): [https://www.youtube.com/watch?v=6DZjBcDfPHs](https://www.youtube.com/watch?v=6DZjBcDfPHs).  
2. **Nền tảng**: Fields Institute, Optimal Transportation Lecture 01: [https://www.youtube.com/watch?v=TAnoqeYfO1Y](https://www.youtube.com/watch?v=TAnoqeYfO1Y).  
3. **Định hướng**: Simons, Crash Course on Optimal Transport: [https://www.youtube.com/watch?v=GMC7uOPAa_Y](https://www.youtube.com/watch?v=GMC7uOPAa_Y).  
4. **Tính toán**: UniHeidelberg, Sinkhorn iterations (discrete OT): [https://www.youtube.com/watch?v=BfOjrQAhG4M](https://www.youtube.com/watch?v=BfOjrQAhG4M).  

**Lưu ý về hiện trạng:** lý thuyết đã chín muồi và ứng dụng đang bùng nổ. Lý thuyết Monge–Kantorovich là cổ điển; Sinkhorn và các dòng gradient là những động cơ tính toán hiện đại.

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/optimal-transport_6DZjBcDfPHs_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu tham khảo

1. Villani — Topics / Old and New.
2. Peyré & Cuturi — *Computational Optimal Transport*.
3. Santambrogio — OT for applied mathematicians.
4. Nền tảng: Monge; Kantorovich; Brenier.
5. [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

---

### Video (lộ trình gợi ý)

- Villani, Optimal Transport Theory (Imperial College) (cốt lõi): https://www.youtube.com/watch?v=6DZjBcDfPHs
- Fields Institute, Optimal Transportation Lecture 01 (nền tảng): https://www.youtube.com/watch?v=TAnoqeYfO1Y
- Simons, Crash Course on Optimal Transport (định hướng): https://www.youtube.com/watch?v=GMC7uOPAa_Y
- UniHeidelberg, Sinkhorn iterations (discrete OT) (tính toán): https://www.youtube.com/watch?v=BfOjrQAhG4M

### Bài báo và web

- Wikipedia — Transportation theory (mathematics): https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)
- Wikipedia — Wasserstein metric: https://en.wikipedia.org/wiki/Wasserstein_metric
- Peyré & Cuturi — Computational OT (arXiv survey): https://arxiv.org/abs/1803.00567
- Carmin.tv OT intro lectures: https://www.carmin.tv/en/video/introduction-to-optimal-transport-theory-lecture-2
- Wikipedia — Earth mover's distance: https://en.wikipedia.org/wiki/Earth_mover%27s_distance


## Hướng đi tiếp

- [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/); [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).
- [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) cho việc học phân phối.
- Thực hành: giải OT rời rạc $$2\times 2$$ hoặc $$3\times 3$$ bằng tay; rồi chạy Sinkhorn với cùng hàm chi phí.
- Đọc: Peyré–Cuturi về tính toán, rồi trực giác của Villani, rồi phần tóm tắt một bài báo về tốc độ thống kê.
- Luôn ghi lại: *chi phí, các biên, chính xác hay có điều chuẩn, bộ ước lượng*.

## Video tham khảo

- **Xem trước** — [New Frontiers in Mathematics: Professor Cédric Villani, “Optimal Transport Theory”](https://www.youtube.com/watch?v=6DZjBcDfPHs) — Imperial College London, tiếng Anh. Xem trước để nghe Villani giới thiệu bài toán Monge và vì sao ánh xạ vận chuyển có thể không tồn tại.
- [Lecture 01 | Optimal Transportation, Geometry and Dynamics](https://www.youtube.com/watch?v=TAnoqeYfO1Y) — Fields Institute, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để theo dõi phần mở đầu của một khóa học về OT.
- [Crash Course on Optimal Transport](https://www.youtube.com/watch?v=GMC7uOPAa_Y) — Simons Institute for the Theory of Computing, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, ở dạng bài giảng ngắn tập trung vào các công thức chính.
