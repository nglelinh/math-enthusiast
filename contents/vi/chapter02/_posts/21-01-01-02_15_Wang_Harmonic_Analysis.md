---
layout: post
title: "Hong Wang: Giải tích Điều hòa và Lý thuyết Độ đo Hình học (Huy chương Fields 2026)"
chapter: '02'
order: 14
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

> **Lộ trình học A — Kakeya (bước 2/3)**  
> **1. Bài trước:** [Bản đồ Kakeya, Chương 1]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/)  
> **2. Bạn đang ở đây:** Bài về Hong Wang, Chương 2 (lý thuyết đầy đủ)  
> **3. Bài tiếp:** [Studio Kakeya, Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/)  
> *Nếu đây là lần đầu bạn gặp bài toán Kakeya, nên đọc bài ở Chương 1 trước.*

Câu chuyện bắt đầu năm 1917 từ một câu đố tưởng như để giải trí trong giờ trà: cần diện tích nhỏ nhất là bao nhiêu trên mặt bàn để xoay ngược đầu một chiếc kim dài 1 đơn vị? Chẳng ai ngờ câu đố chiếc kim của Sōichi Kakeya lại dẫn đến một kết quả phản trực giác đến kinh ngạc (có thể xoay chiếc kim trong diện tích nhỏ tùy ý, thậm chí có tập chứa đoạn thẳng dài 1 theo *mọi* hướng mà diện tích bằng đúng 0!), và rồi biến thành một trong những nút thắt trung tâm suốt cả thế kỷ của **giải tích điều hòa** và **lý thuyết sóng**.

Đầu năm 2025, **Hong Wang** (NYU Courant; giáo sư thường trực tại IHES) cùng **Joshua Zahl** đã gây chấn động giới toán học khi công bố chứng minh dài 127 trang giải trọn **giả thuyết tập Kakeya trong không gian ba chiều**. Không chỉ dừng ở Kakeya, suốt nhiều năm trước đó, Hong Wang đã liên tiếp tạo ra những đột phá lớn về bài toán làm trơn địa phương cho phương trình sóng, tập khoảng cách Falconer, tập Furstenberg và bài toán hạn chế Fourier. Thành tựu toàn diện ấy đã mang về cho bà **Huy chương Fields 2026** tại ICM Philadelphia — đưa Hong Wang trở thành **người phụ nữ thứ ba** trong lịch sử nhận giải thưởng danh giá này (sau Maryam Mirzakhani năm 2014 và Maryna Viazovska năm 2022).

**Trích dẫn ngắn của IMU:**

> For her work in harmonic analysis and geometric measure theory, including applications of multiscale and decoupling techniques to the local smoothing conjecture for the planar wave equation, and major advances in Fourier restriction, Falconer distance sets, Furstenberg sets in the plane, and the Kakeya problem in three dimensions.  
> — [IMU, Fields Medal 2026](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf)

*Tạm dịch:* Cho các công trình về giải tích điều hòa và lý thuyết độ đo hình học, gồm việc áp dụng kỹ thuật đa thang và kỹ thuật tách (decoupling) vào giả thuyết làm trơn địa phương cho phương trình sóng trên mặt phẳng, cùng những tiến bộ lớn về bài toán hạn chế Fourier, tập khoảng cách Falconer, tập Furstenberg trên mặt phẳng và bài toán Kakeya ba chiều.

Hành trình của bài học này đi qua bảy chặng:

**Bài toán chiếc kim → Tập Besicovitch → độ đo và số chiều → ống $$\delta$$ → định lý Wang–Zahl → giải tích điều hòa → các công trình được nêu trong lời trích dẫn.**

Mục tiêu không phải là trình bày lại chứng minh dài 127 trang, mà là hiểu **bài toán hỏi gì**, **vì sao nó khó suốt một thế kỷ**, và **những lĩnh vực toán học nào liên quan**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu bài toán chiếc kim của Kakeya và cách Besicovitch xây dựng một tập có độ đo bằng 0 trên mặt phẳng.
- Giải thích vì sao **độ đo Lebesgue bằng 0** không kéo theo **chiều Hausdorff (hay Minkowski)** nhỏ hơn số chiều của không gian.
- Phát biểu **giả thuyết tập Kakeya** trong $$\mathbb{R}^n$$ và nêu các kết quả đã biết cho $$n=2$$ và $$n=3$$.
- Mô tả hình ảnh các **ống $$\delta$$** và giải thích vì sao sự chồng lấp mạnh giữa các ống mới là khó khăn thật sự.
- Đặt kết quả **Wang–Zahl (2025)** và **Huy chương Fields của Wang (2026)** vào bối cảnh lịch sử dài hơn.
- Tóm tắt, kèm tên các cộng sự, những đóng góp của Wang **ngoài** bài toán Kakeya (làm trơn địa phương, Falconer, Furstenberg, bài toán hạn chế).
- Tránh các nhầm lẫn thường gặp (chuyển động của chiếc kim và tập Besicovitch; công lao chung; thể tích và số chiều).

**Kiến thức cần có.** Không gian Euclid, trực giác về diện tích và thể tích, ý tưởng fractal có số chiều không nguyên. Biến đổi Fourier chỉ cần ở mức khái niệm.

---

## Bản đồ kiến thức nền: Giải tích điều hòa và Lý thuyết độ đo hình học là gì?

Vì sao câu đố xoay một chiếc kim lại trở thành bài toán trung tâm của các nhà giải tích nghiên cứu sóng và biến đổi Fourier? Hãy nhìn vào hai ngành toán học giao nhau trong công trình của Hong Wang:

- **Lý thuyết độ đo hình học (Geometric Measure Theory) nghiên cứu gì?** Trong hình học sơ cấp, ta đo kích thước bằng chiều dài, diện tích hay thể tích (độ đo Lebesgue). Nhưng với các tập **fractal** tinh vi, thể tích có thể bằng $$0$$ dù tập vẫn rất "dày"! Ví dụ kinh điển: **tập Cantor** trên đoạn $$[0, 1]$$ (liên tục bỏ phần ba ở giữa) có tổng chiều dài bằng $$0$$, nhưng khi phủ bằng các đoạn nhỏ cỡ $$3^{-k}$$ ta cần tới $$2^k$$ đoạn, nên **chiều Hausdorff** của nó là $$\log 2 / \log 3 \approx 0{,}631$$. Lý thuyết độ đo hình học nghiên cứu chính những tập mảnh dẻ như thế: độ lớn fractal, hình chiếu, tập khoảng cách giữa các điểm (*Falconer*), và cách các đoạn thẳng hay ống mảnh chồng lấp nhau (*Kakeya*, *Furstenberg*).
- **Giải tích điều hòa (Harmonic Analysis) nghiên cứu gì?** Nghiên cứu cách phân tích hàm số và nghiệm của phương trình sóng thành tổng các sóng cơ bản (phân tích Fourier). Trong không gian nhiều chiều, khi bạn chồng rất nhiều sóng truyền theo mọi hướng khác nhau, mỗi sóng cục bộ hóa theo một hướng sẽ tập trung năng lượng trong một **ống mảnh** (gọi là *bó sóng*, wave packet). Nếu các ống mảnh theo mọi hướng có thể nén chồng khít lên nhau vào một tập cực nhỏ, thì các sóng có thể giao thoa tăng cường dữ dội tại một điểm kỳ dị!
- **Vì sao Kakeya là viên đá tảng?** Chuyển bài toán từ hình học đoạn thẳng sang các **ống $$\delta$$** (bán kính $$\delta$$, dài 1) biến bài toán Kakeya thành thước đo chuẩn cho mức độ tập trung cực đại của các bó sóng. Hiểu được sự chồng lấp đa thang của các ống $$\delta$$ chính là chìa khóa cho cả chuỗi giả thuyết lớn của giải tích điều hòa: từ bài toán hạn chế Fourier đến tính làm trơn địa phương của phương trình sóng!

---

## 1. Bài toán chiếc kim: phát biểu đơn giản, kết quả bất ngờ

Năm 1917, **Sōichi Kakeya** hỏi (đại ý): một chiếc kim dài 1 cần được **xoay liên tục** trong một miền phẳng sao cho cuối cùng đầu và đuôi đổi chỗ cho nhau (quay $$180^\circ$$). Miền đó phải có diện tích nhỏ nhất là bao nhiêu?

Theo trực giác, chiếc kim dài 1 phải quét qua một vùng "đáng kể". Xoay quanh trung điểm thì cần một hình tròn bán kính $$1/2$$ (diện tích $$\pi/4 \approx 0{,}785$$). Dùng kỹ thuật quay ba điểm kiểu đỗ xe, ta hạ diện tích xuống một hình **deltoid** (diện tích $$\pi/8 \approx 0{,}393$$). Dù vậy, người ta vẫn đinh ninh rằng diện tích phải có **một chặn dưới dương**.

Besicovitch chứng minh một điều mạnh hơn nhiều so với việc "diện tích có thể nhỏ hơn một chút".

![Đoạn đơn vị theo nhiều hướng]({{ site.baseurl }}/img/chapter_img/kakeya_needle_directions.svg)

*Hình. Tập Kakeya phải chứa một đoạn dài 1 theo mọi hướng, nhưng bản thân tập đó không nhất thiết trông "đầy đặn".*

---

## 2. Tập Besicovitch: chứa mọi hướng nhưng có độ đo bằng 0

Một **tập Kakeya** (còn gọi là **tập Besicovitch**) trong $$\mathbb{R}^n$$ là tập chứa một đoạn thẳng dài 1 theo **mọi** hướng.

**Abram Besicovitch** (khoảng 1919–1928) chứng minh rằng trên mặt phẳng tồn tại những tập như vậy có **độ đo Lebesgue bằng 0**. Nói cách khác, với mọi $$\varepsilon>0$$ ta có thể dựng một tập có diện tích nhỏ hơn $$\varepsilon$$ mà vẫn chứa đoạn dài 1 theo mọi hướng; qua một phép lấy giới hạn thích hợp, ta được một tập có độ đo đúng bằng 0.

Về lịch sử, Besicovitch ban đầu nghiên cứu vấn đề này vì một câu hỏi về **tích phân lặp** trong lý thuyết tích phân Riemann. Cách dựng của ông sau đó cũng giải luôn bài toán chiếc kim của Kakeya: kết hợp với một kỹ thuật của Pál (tịnh tiến chiếc kim dọc theo đường thẳng mất diện tích nhỏ tùy ý), ta có thể xoay chiếc kim trong một miền có diện tích nhỏ tùy ý. Vì vậy, tên gọi **tập Besicovitch** là hoàn toàn hợp lý.

### Làm sao diện tích có thể bằng 0?

Độ dài của mỗi đoạn luôn là $$1$$. Cái ta có thể làm là **dùng lại cùng một phần mặt phẳng cho rất nhiều hướng**, rồi lấy giới hạn của các lân cận ngày càng mỏng để được một tập kiểu fractal.

![Cắt và trượt tam giác]({{ site.baseurl }}/img/chapter_img/besicovitch_triangle_overlap.svg)

*Hình. Minh họa kinh điển: cắt một tam giác thành nhiều phần, trượt các phần để chúng chồng lên nhau nhiều hơn, rồi lặp lại.*

Một hình ảnh hay dùng khi giảng dạy là **rèm sáo lặp lại** (cây Perron): cắt một tam giác lớn thành nhiều tam giác mảnh có chung đỉnh, rồi trượt chúng chồng lấn lên nhau dọc theo đáy. Mỗi mảnh vẫn giữ nguyên tập hợp hướng của nó, nhưng tổng diện tích hợp lại giảm đi đáng kể sau mỗi lần cắt–trượt!

![Venetian blind]({{ site.baseurl }}/img/chapter_img/venetian_blinds_kakeya.svg)

*Hình. Sơ đồ kiểu rèm sáo (chỉ minh họa ý tưởng, không phải cách dựng đầy đủ).*

**Ý chính.** Một hình chữ nhật dài 1, rộng $$\delta$$ có diện tích cỡ $$\delta$$. Khi $$\delta\to 0$$ diện tích này tiến về 0, nhưng số hướng cần chứa là **vô hạn**. Cái khéo của Besicovitch là **dùng lại không gian** một cách có hệ thống.

### Davies (1971): số chiều vẫn bằng 2

Độ đo bằng 0 **không** có nghĩa là tập đó "một chiều". **Roy Davies** chứng minh rằng mọi tập Kakeya trên mặt phẳng đều có **chiều Hausdorff bằng 2**:

$$
\lvert E\rvert = 0 \quad\text{có thể, nhưng}\quad \dim_H(E) = 2.
$$

Đây là điều bất ngờ đầu tiên: tập này **không có diện tích, nhưng có số chiều đầy đủ**.

---

## 3. Số chiều không chỉ là 1, 2, 3

Hình học thông thường chỉ dùng số chiều nguyên. Với fractal, số chiều có thể là các giá trị ở giữa ($$1.5$$, $$2.7$$, …).

**Chiều Minkowski (chiều đếm hộp)** dễ hình dung: phủ tập bằng các hộp cạnh $$r$$ và xem số hộp cần dùng tăng theo lũy thừa nào của $$1/r$$ khi $$r\to 0$$ (nếu cần khoảng $$r^{-d}$$ hộp thì chiều Minkowski bằng $$d$$).

**Chiều Hausdorff** được định nghĩa tinh tế hơn bằng lý thuyết độ đo (cho phép dùng các quả cầu có kích thước *khác nhau* để phủ tập). Với nhiều tập "đủ đẹp", hai khái niệm này trùng nhau. Bài toán Kakeya nghiên cứu cả hai.

> **Thể tích bằng 0 không buộc số chiều phải nhỏ hơn 3.**  
> Một tập trong $$\mathbb{R}^3$$ có thể có độ đo Lebesgue bằng 0 mà vẫn có chiều Minkowski bằng 3.

![Measure và dimension]({{ site.baseurl }}/img/chapter_img/measure_vs_dimension.svg)

*Hình. Độ đo và số chiều là hai cách đo "kích thước" khác nhau.*

---

## 4. Giả thuyết tập Kakeya nói gì?

**Giả thuyết (tập Kakeya trong $$\mathbb{R}^n$$).**  
Mọi tập Kakeya $$K\subset\mathbb{R}^n$$ có chiều Hausdorff và chiều Minkowski bằng $$n$$:

$$
\dim_H(K) = \dim_M(K) = n.
$$

| Số chiều không gian | Tình trạng |
|------------------|------------|
| $$n=1$$ | Hiển nhiên |
| $$n=2$$ | Đã chứng minh (Davies, 1971) |
| $$n=3$$ | Đã chứng minh (**Wang–Zahl**, 2025) |
| $$n\ge 4$$ | Còn mở (mới có các chặn dưới một phần) |

Từ cách dựng của Besicovitch, ta biết ở mọi số chiều đều có tập Kakeya **độ đo bằng 0**. Giả thuyết nói rằng dù vậy, các tập này không thể "mỏng" quá theo nghĩa số chiều fractal.

---

## 5. Vì sao trường hợp 3 chiều khó? Các ống $$\delta$$

Thay mỗi đoạn thẳng dài 1 bằng một **ống** mảnh dài khoảng 1, bán kính $$\delta$$ (gọi là ống $$\delta$$, $$\delta$$-tube). Khi nhìn ở thang $$\delta$$, một tập Kakeya trong $$\mathbb{R}^3$$ giống như một họ gồm khoảng $$N \approx \delta^{-2}$$ ống, mỗi ống theo một hướng riêng biệt trên mặt cầu đơn vị $$S^2$$.

![δ-tube chồng lấp]({{ site.baseurl }}/img/chapter_img/kakeya_delta_tubes.svg)

*Hình. Nhiều ống $$\delta$$; những vùng các ống chồng lên nhau nhiều là nơi hình học trở nên phức tạp.*

Nếu các ống gần như không chồng lên nhau, vì mỗi ống có thể tích cỡ $$\delta^2$$, thể tích của hợp trong $$\mathbb{R}^3$$ vào cỡ $$N\cdot \delta^{2} \approx 1$$. Trường hợp khó là khi các ống **chồng lên nhau rất nhiều**:

$$
\bigl\lvert \bigcup_i T_i\bigr\rvert \;\ll\; \sum_i \lvert T_i\rvert.
$$

> **Hợp của rất nhiều ống theo nhiều hướng có thể nhỏ đến mức nào?**

### Hình dung bằng sợi mì

Hãy tưởng tượng hàng triệu sợi mì spaghetti rất mảnh, mỗi sợi theo một hướng, cần được nhét vào một vùng nhỏ nhất có thể.

- **Nếu để tản ra**, chúng chiếm nhiều không gian và số chiều rõ ràng là lớn.  
- **Nếu bó chặt**, chúng tạo thành những bó dày. Nhưng sự tập trung cực mạnh như vậy không thể tùy ý: các sợi phải gần song song, tập trung quanh một đường hay một mặt phẳng, hoặc tạo thành cấu hình kiểu **regulus** (họ đường thẳng chéo nhau cùng nằm trên một mặt cong hyperboloid một tầng — giống khung chiếc tháp làm mát hay giỏ mây đan chéo!).

Ý tưởng trong phân tích của Wang–Zahl: **khi các ống chồng lên nhau quá nhiều, chúng buộc phải có cấu trúc hình học**, và cấu trúc đó có thể khai thác ở một thang khác.

### Tính "hạt" ở nhiều thang

Ở thang thô, tập có thể trông như một khối đặc. Phóng to lên, ta thấy các ống mảnh. Phóng to thêm nữa lại thấy các cấu trúc "hạt" (*grain*) mới. Bài toán vì thế có bản chất đa thang:

$$
1 \;\to\; \delta \;\to\; \delta^{2} \;\to\; \cdots
$$

Trong không gian ba chiều, các ống có thể cắt chéo nhau, gần song song, tập trung theo đường hoặc mặt, hoặc tạo thành cấu hình regulus. Các phương pháp cho mặt phẳng (nơi hai đường thẳng không song song *bắt buộc* cắt nhau tại đúng một điểm) không mở rộng được lên ba chiều. Các bản tóm tắt của chuyên gia (ví dụ của Larry Guth) nhấn mạnh rằng chứng minh dài vì phải theo dõi đồng thời cấu trúc ở vô số thang lồng nhau.

---

## 6. Wang và Zahl thực sự chứng minh điều gì?

<div class="textbook-theorem" markdown="1">
**Định lý (Wang–Zahl, 2025).**  
Mọi tập Kakeya $$K\subset\mathbb{R}^3$$ thỏa

$$
\dim_H(K) = \dim_M(K) = 3.
$$
</div>

Nguồn chính: *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions* ([arXiv:2502.17655](https://arxiv.org/abs/2502.17655); 127 trang). Phần tóm tắt nêu rõ kết quả kỹ thuật: với một họ ống $$\delta$$ trong $$\mathbb{R}^3$$ thỏa điều kiện **không tập trung bất thường** (không có quá nhiều ống nằm gọn trong cùng một tập lồi $$V$$), hợp của chúng có **thể tích gần lớn nhất có thể** (tức $$\ge c_\varepsilon \delta^\varepsilon$$). Kết luận số chiều bằng 3 cho tập Kakeya được suy ra từ ước lượng này.

Định lý **không** nói tập Kakeya ba chiều phải có thể tích dương; tập có độ đo bằng 0 kiểu Besicovitch vẫn tồn tại. Nội dung định lý là:

> Tập Kakeya có thể có **thể tích bằng 0**, nhưng không thể có số chiều fractal nhỏ hơn 3.

### Phác thảo chiến lược (không phải chứng minh)

1. Đưa bài toán Kakeya về ước lượng cho họ các ống mảnh.  
2. Phân tích các giao điểm và sự tụ cụm của các ống.  
3. Nếu các ống chồng lên nhau rất nhiều, chứng minh chúng phải có **cấu trúc hình học** (tính "dính", tính "hạt", tính "phẳng", là các chủ đề trong chương trình của Katz–Tao).  
4. Dùng cấu trúc đó để chứng minh cấu hình phải **giãn ra** ở một thang khác (**tự cải thiện**).  
5. Lập luận **quy nạp theo thang** (nối các ước lượng cho họ ống thành ước lượng tổng quát cho hợp của các tập lồi).  
6. Kết luận số chiều không thể nhỏ hơn 3.

**Ý tưởng tự cải thiện.**

$$
\text{cấu hình xấu ở một thang}
\;\Longrightarrow\;
\text{cấu trúc ẩn}
\;\Longrightarrow\;
\text{cấu hình tốt hơn ở thang khác}.
$$

Công trình trước đó của Wang–Zahl về tập Kakeya **dính** (*sticky*) là một bước chuẩn bị quan trọng. Tập dính có tính tự đồng dạng gần đúng ở nhiều thang và đã xuất hiện trong công trình của Katz–Łaba–Tao (1999). Wang–Zahl chứng minh giả thuyết Kakeya cho tập dính trong không gian ba chiều ([arXiv:2210.09581](https://arxiv.org/abs/2210.09581); *J. Amer. Math. Soc.* **39** (2026), 515–585).

**Ghi nhận công lao.** Đây là **công trình chung** của hai tác giả. Kết quả này là đỉnh cao của cả một thế kỷ nghiên cứu, dựa trên công trình của nhiều người đi trước.

![Dòng thời gian]({{ site.baseurl }}/img/chapter_img/kakeya_history_timeline.svg)

*Hình. Một số mốc từ Kakeya (1917) đến Huy chương Fields của Wang (2026).*

---

## 7. Vì sao giải tích điều hòa quan tâm đến bài toán này?

Bài toán Kakeya nằm ở chỗ giao nhau của:

- **lý thuyết độ đo hình học**,
- **giải tích điều hòa** (bài toán hạn chế Fourier, hàm cực đại, tích phân dao động),
- **phương trình đạo hàm riêng** (tính làm trơn địa phương của phương trình sóng, sự tập trung của nghiệm).

**Biến đổi Fourier** cho tương ứng hàm $$f(x)$$ với phổ tần số $$\hat f(\xi)$$ của nó. Khi nghiên cứu các sóng có cùng bước sóng nhưng theo nhiều hướng, hay khi hạn chế biến đổi Fourier lên một mặt cong, năng lượng thường chia thành các **bó sóng** (*wave packet*) nằm trên những ống dài và mảnh. Cách các ống này chồng lên nhau quyết định năng lượng có thể **tập trung** lại hay buộc phải **lan ra**.

![Từ Kakeya đến harmonic analysis]({{ site.baseurl }}/img/chapter_img/kakeya_to_harmonic_analysis.svg)

*Hình. Chuỗi khái niệm từ hình học các ống đến giải tích Fourier và PDE.*

Một loạt giả thuyết liên quan (bài toán hạn chế, Bochner–Riesz, làm trơn địa phương ở dạng mạnh hơn hoặc ở chiều cao hơn) vẫn phụ thuộc vào hình học kiểu Kakeya. Lời giải cho trường hợp ba chiều làm thay đổi bức tranh chung, nhưng chưa kết thúc câu chuyện.

---

## 8. Ngoài Kakeya: các công trình trong lời trích dẫn dài của IMU

Lời trích dẫn của huy chương cố ý rộng hơn một định lý. Bảng tóm tắt:

| Chủ đề | Cộng sự (chọn lọc) | Đóng góp chính |
|--------|--------------------------|----------------|
| **Làm trơn địa phương** (sóng trên mặt phẳng) | Larry Guth, Ruixiang Zhang | Dùng kỹ thuật đa thang và kỹ thuật tách để giải giả thuyết làm trơn địa phương trên mặt phẳng (theo lời trích dẫn dài của IMU) |
| **Tập khoảng cách Falconer** | Guth, Alex Iosevich, Yumeng Ou | Kết quả lớn liên hệ chiều Hausdorff với tập các khoảng cách |
| **Tập Furstenberg** (mặt phẳng) | Kevin Ren | Giải giả thuyết Furstenberg trên mặt phẳng ([arXiv:2308.08819](https://arxiv.org/abs/2308.08819)): tập $$(s,t)$$-Furstenberg có số chiều ít nhất $$\min\bigl(s+t,\frac{3s+t}{2},s+1\bigr)$$ |
| **Bài toán hạn chế Fourier** | nhiều cộng sự | Các tiến bộ về cấu trúc, đóng góp cho chuỗi giả thuyết hạn chế |
| **Kakeya ba chiều** | Joshua Zahl | Trường hợp tập dính (JAMS 2026) và số chiều đầy đủ bằng 3 (arXiv:2502.17655) |

**Vì sao.** Cách các hướng sắp xếp theo kiểu fractal quyết định năng lượng và độ đo có thể tập trung đến mức nào.  
**Bằng cách nào.** Phân tích đa thang, kỹ thuật tách (*decoupling*), hình học liên thuộc và hình học các ống.  
**Kết quả.** Một loạt định lý sắc; Kakeya ba chiều là kết quả được công chúng biết đến nhiều nhất.

### Tiểu sử ngắn

Hong Wang sinh tại Quế Lâm (Trung Quốc), học tại Đại học Bắc Kinh và École Polytechnique, làm tiến sĩ ở MIT dưới sự hướng dẫn của **Larry Guth**, sau đó làm việc tại IAS, UCLA, rồi NYU Courant và IHES. Trước **Huy chương Fields tại ICM 2026 (Philadelphia)**, bà đã nhận nhiều giải thưởng như Salem, Ostrowski, Clay Research Award, New Horizons.

### Nói cho chính xác

- Giả thuyết Kakeya ba chiều là **công trình chung** với **Joshua Zahl**.  
- Huy chương Fields ghi nhận **toàn bộ các công trình**. Kakeya ba chiều là phần nổi tiếng nhất, không phải toàn bộ lời trích dẫn.  
- Bà là **người phụ nữ thứ ba** nhận Huy chương Fields.  
- **Bài toán Kakeya ở chiều cao hơn** ($$n\ge 4$$) và nhiều giả thuyết sắc trong giải tích vẫn còn mở (tính đến năm 2026).

---

## 9. Nhắc lại điều bất ngờ nhất

$$
\operatorname{Vol}(K)=0
\quad\text{có thể,}\quad
\dim(K)=3
\quad\text{là bắt buộc trong }\mathbb{R}^3.
$$

Không thể đặt các đoạn thẳng dài 1 theo mọi hướng trong không gian ba chiều vào một tập fractal có số chiều nhỏ hơn 3. Đó là nội dung của giả thuyết tập Kakeya ba chiều, nay là định lý Wang–Zahl.

---

## Nhầm lẫn thường gặp

| Khẳng định | Kết luận | Sửa lại |
|------------|----------|-----|
| "Một mình Wang giải bài toán Kakeya ba chiều." | **Sai** | Đây là công trình chung với Joshua Zahl. |
| "Tập Kakeya ba chiều phải có thể tích dương." | **Sai** | Vẫn có tập độ đo bằng 0; định lý nói về **số chiều**. |
| "Giải Fields chỉ vì bài toán Kakeya." | **Sai** | IMU còn nêu làm trơn địa phương, bài toán hạn chế, Falconer, Furstenberg. |
| "Chuyển động của chiếc kim chính là tập Besicovitch." | **Sai** | Hai khái niệm liên quan nhưng khác nhau: một bên là **chuyển động**, một bên là **tập cố định** chứa mọi hướng. |
| "Bài toán Kakeya đã giải xong ở mọi số chiều." | **Sai** | Trường hợp $$n\ge 4$$ vẫn còn mở. |

---

## Ghi chú từ các video chính

*Phần này được viết lại từ phụ đề của các video trong bộ tài liệu (Quanta về Kakeya; Mathologer; video về chiều Hausdorff; video tiếng Việt). Nó không thay thế bài báo Wang–Zahl trên arXiv hay lời trích dẫn của IMU. Bản ghi lời: `research/video-research/Wang_Harmonic_Analysis/transcripts/`.*

### C1. Chuyển động của chiếc kim và tập Kakeya

Câu chuyện "xoay chiếc kim 180° trong một vùng có diện tích nhỏ" là về **chuyển động liên tục**. Giả thuyết tập Kakeya hiện đại là về **một tập cố định** chứa đoạn dài 1 theo mọi hướng. Cả hai đều nói đến "mọi hướng" nhưng **định nghĩa khác nhau**, nên cần xác định rõ đối tượng trước khi so sánh các định lý.

### C2. Độ đo bằng 0 vẫn chứa đủ mọi hướng

Các kết quả của Besicovitch và Davies (dùng hình chữ nhật hay ống mảnh) cho thấy chứa "mọi hướng" không buộc diện tích phải dương trên mặt phẳng. Vì vậy giả thuyết ở chiều cao hơn được phát biểu bằng **số chiều** (Hausdorff, Minkowski), chứ không phải "phải có thể tích dương".

### C3. Chiều Hausdorff (kiến thức bổ trợ)

Độ đo Hausdorff, định nghĩa qua một hàm cỡ (*gauge function*), đo "độ lớn" của một tập khi thể tích của nó bằng 0. Một tập có thể có độ đo bằng 0 nhưng $$\dim_H$$ vẫn bằng số chiều của không gian. Cần nhớ rạch ròi: độ đo bằng 0 **không** kéo theo số chiều bằng 0; số chiều đầy đủ **không** kéo theo độ đo Lebesgue dương.

### C4. Kakeya ba chiều và Wang–Zahl (theo Quanta và các nguồn phổ thông)

Giả thuyết ba chiều (dạng phổ thông) nói rằng mọi tập Kakeya trong $$\mathbb{R}^3$$ có số chiều đầy đủ bằng 3. Wang và Zahl đã chứng minh điều này; các bài tường thuật nhấn mạnh việc phân tích ống $$\delta$$ ở nhiều thang và các cấu hình dính. Khi trình bày, cần lưu ý:

| Nên nói | Không nên nói |
|----------|-----------|
| **Wang và Zahl** | "Một mình Wang" |
| Kết quả về **số chiều** trong không gian ba chiều | "Mọi tập Kakeya đều có thể tích dương" |
| Trường hợp $$n\ge 4$$ vẫn còn mở | "Bài toán Kakeya đã xong hoàn toàn" |
| Lời trích dẫn của IMU rộng hơn bài toán Kakeya | "Giải Fields chỉ vì Kakeya" |

### C5. Video tiếng Việt

Dùng để làm quen với chủ đề. Phụ đề tự động hoặc chỗ ghi sai tên, sai năm là dịp tốt để rèn thói quen kiểm chứng: luôn đối chiếu với arXiv và IMU trước khi trích dẫn.

### C6. Tài liệu hỗ trợ

Xem `TRANSCRIPT_STATUS.md` và các tệp `*_knowledge_units.json`. Khi làm bài có chấm điểm, hãy dùng ký hiệu và thuật ngữ của bài học (ống $$\delta$$, chiều Hausdorff, tập dính), đừng chép nguyên phụ đề.

---

## Thách thức và mở rộng

1. Phân biệt **chuyển động liên tục của chiếc kim** với **tập Besicovitch cố định**.  
2. Có thể chặn dưới $$\lvert\bigcup T_i\rvert$$ như thế nào theo $$\delta$$ và số hướng?  
3. Vì sao trường hợp **tập dính** có thể là "đối thủ" tự nhiên của giả thuyết?  
4. Phát biểu lại bài toán Kakeya như một bài toán chặn mức độ tập trung của các bó sóng.  
5. Nêu hai khó khăn hình học xuất hiện ở chiều 4 mà ở chiều 3 nhẹ hơn.

---

## Nguồn video và tài liệu đọc

Chi tiết: `research/video-research/Wang_Harmonic_Analysis/`.

**Thứ tự xem gợi ý**

1. Quanta về Kakeya: [YouTube](https://www.youtube.com/watch?v=5J3tYU_-IZI).  
2. CHALK về chiều Hausdorff: [YouTube](https://www.youtube.com/watch?v=LJcWhcM4okQ) · MDP: [YouTube](https://www.youtube.com/watch?v=FQXbRGmAbUY).  
3. Mathologer về bài toán chiếc kim: [YouTube](https://www.youtube.com/watch?v=IM-n9c-ARHU).  
4. Tiếng Việt: [Pham Manh Tuyen](https://www.youtube.com/watch?v=XUkfpgFakMQ) · [TOÁN PRO](https://www.youtube.com/watch?v=pxVMKoZsVc8).  
5. arXiv:2502.17655 · PDF lời trích dẫn của IMU cho Wang.

**Ghi nhớ:** Bài toán Kakeya ba chiều **đã được chứng minh**; ở chiều cao hơn vẫn **còn mở**.

---


### Bản ghi lời và khung hình (video chính)

Phụ đề và các đơn vị kiến thức theo mốc thời gian: `research/video-research/Wang_Harmonic_Analysis/transcripts/` · trạng thái: `research/video-research/Wang_Harmonic_Analysis/TRANSCRIPT_STATUS.md` · danh sách chung: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Phụ đề được tải tự động (bằng yt-dlp), chỉ dùng để tra cứu, **không** thay thế nội dung bài.


![Frame mẫu video flagship]({{ site.baseurl }}/img/video_research/flagships/kakeya_mathologer_frame01.jpg)

*Hình. Một khung hình mẫu từ video chính (xem bộ tài liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh mục URL đầy đủ (gồm mọi link dùng khi tìm video): `research/video-research/Wang_Harmonic_Analysis/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=5J3tYU_-IZI  
2. https://www.youtube.com/watch?v=LJcWhcM4okQ  
3. https://www.youtube.com/watch?v=FQXbRGmAbUY  
4. https://www.youtube.com/watch?v=IM-n9c-ARHU  
5. https://www.youtube.com/watch?v=XUkfpgFakMQ  
6. https://www.youtube.com/watch?v=pxVMKoZsVc8  
7. https://arxiv.org/abs/2502.17655  
8. https://arxiv.org/abs/2210.09581  
9. https://arxiv.org/abs/2308.08819  
10. https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf  
11. https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/  
12. https://www.math.ubc.ca/~ilaba/kakeya.html  
13. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2026  
14. https://en.wikipedia.org/wiki/Kakeya_set  
15. https://en.wikipedia.org/wiki/Restriction_problem  

### Gói nghiên cứu

16. Gói khóa học: `research/video-research/Wang_Harmonic_Analysis/`.

1. **H. Wang & J. Zahl** (2025). *Volume estimates… Kakeya… three dimensions*. [arXiv:2502.17655](https://arxiv.org/abs/2502.17655).  
2. **H. Wang & J. Zahl** (2026). Sticky Kakeya sets…. *J. Amer. Math. Soc.*, *39*, 515–585. [arXiv:2210.09581](https://arxiv.org/abs/2210.09581).  
3. **K. Ren & H. Wang** (2023). *Furstenberg sets estimate in the plane*. [arXiv:2308.08819](https://arxiv.org/abs/2308.08819).  
4. **R. O. Davies** (1971). Some remarks on the Kakeya problem. *Proc. Cambridge Philos. Soc.*, *69*.  
5. **IMU** (2026). *Fields Medal 2026 — Hong Wang* (short & long citations). [PDF](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf).  
6. **I. Łaba**. [The Kakeya problem…](https://www.math.ubc.ca/~ilaba/kakeya.html).  
7. **T. Tao** (2014). Blog *Stickiness, graininess, planiness…*.  
8. **L. Guth**. Outline / survey chứng minh Wang–Zahl.  
9. **Quanta Magazine** (2025, 2026) — Kakeya và Fields của Wang.  
10. Thông cáo **NYU / IHES / CNRS** về Fields 2026.  
11. Liên kết trong khóa học: **Bài toán lớn — Kakeya** và **Khám phá — tập Kakeya nhỏ nhất**.  
12. **Video phổ thông ★ (Quanta, tiếng Anh):** [Once-in-a-Century Proof: Kakeya](https://www.youtube.com/watch?v=5J3tYU_-IZI) (khoảng 15 phút). Nói về chuỗi giả thuyết hạn chế / Bochner–Riesz / làm trơn địa phương, về tập dính và tính "hạt", có phỏng vấn Tao, Wang và Zahl. [Bài Quanta](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/). Truy cập 2026-08-03.  
13. **Video phổ thông A (CHALK, tiếng Anh):** [What is Hausdorff Dimension?](https://www.youtube.com/watch?v=LJcWhcM4okQ) (khoảng 13 phút). Giải thích hàm cỡ, $$\mathcal{H}^s$$ và $$s=\dim_H$$; nên bắt đầu từ `&t=19s`. Truy cập 2026-08-03.  
14. **Video phổ thông A′ (CHALK, tiếng Anh):** [Estimating Hausdorff / MDP](https://www.youtube.com/watch?v=FQXbRGmAbUY) (khoảng 9 phút). Chặn trên bằng phép phủ và nguyên lý phân bố khối lượng (Mass Distribution Principle). Truy cập 2026-08-03.  
15. **Video phổ thông B (Mathologer, tiếng Anh):** [Kakeya needle — squeegee](https://www.youtube.com/watch?v=IM-n9c-ARHU) (khoảng 17 phút). Về chuyển động liên tục của chiếc kim: phép tịnh tiến song song, deltoid, cây Perron; nên bắt đầu từ `&t=632s`. Truy cập 2026-08-03.  
16. **Video phổ thông C (Pham Manh Tuyen):** [Giả Thuyết Kakeya…](https://www.youtube.com/watch?v=XUkfpgFakMQ) (khoảng 15 phút). Đi từ deltoid và cây Perron đến chiều Minkowski/Hausdorff, rồi phác thảo kết quả Wang–Zahl. Truy cập 2026-08-03.  
17. **Video phổ thông D (TOÁN PRO):** [Phỏng Đoán Kakeya…](https://www.youtube.com/watch?v=pxVMKoZsVc8). Kể lại quá trình cải thiện các chặn dưới. Truy cập 2026-08-03. Nếu phụ đề ghi sai tên hoặc năm, hãy sửa theo bài này.

*Ghi chú.* Các khẳng định về định lý Kakeya (2025–2026) và lời trích dẫn giải Fields đã được đối chiếu với phần tóm tắt trên arXiv và PDF chính thức của IMU. Video phổ thông và các bài của Quanta chỉ dùng làm bối cảnh, không dùng cho chi tiết kỹ thuật.

---

## Hướng đi tiếp

**Tiếp tục lộ trình A**

1. [Bản đồ Chương 1]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/) (ôn lại bảng tình trạng).  
2. Đã xong: bài về Wang (trang này).  
3. **Bài tiếp →** [Studio Kakeya, Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/).  

- Cách nghĩ nên giữ: các ống $$\delta$$ như một bài toán về sự tụ cụm ở nhiều thang.  
- Các câu hỏi còn mở: bài toán Kakeya ở chiều cao hơn; bài toán hạn chế và làm trơn địa phương (tính đến năm 2026).

## Video tham khảo

- **Xem trước** — [A Once-in-a-Century Proof: The Kakeya Conjecture](https://www.youtube.com/watch?v=5J3tYU_-IZI) — Quanta Magazine, tiếng Anh. Video phổ thông về bài toán Kakeya và chứng minh Wang–Zahl, có phỏng vấn các tác giả. Nên xem trước khi đọc bài.
- [What is Hausdorff Dimension? Intuition, Gauge Functions, and Hausdorff Measures](https://www.youtube.com/watch?v=LJcWhcM4okQ) — CHALK, tiếng Anh. Giải thích chiều Hausdorff và độ đo Hausdorff, hỗ trợ cho mục 2–3. Nên xem khi đọc đến phần số chiều.
- [Methods for Estimating Hausdorff Dimension: Bounds and The Mass Distribution Principle](https://www.youtube.com/watch?v=FQXbRGmAbUY) — CHALK, tiếng Anh. Các cách ước lượng chiều Hausdorff (chặn trên bằng phép phủ, chặn dưới bằng nguyên lý phân bố khối lượng). Dành cho người muốn hiểu kỹ hơn phần kỹ thuật.
