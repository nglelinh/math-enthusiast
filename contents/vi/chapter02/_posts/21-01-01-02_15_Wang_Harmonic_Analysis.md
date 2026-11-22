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

**Hong Wang** (NYU Courant; giáo sư thường trực tại IHES) được trao **Huy chương Fields 2026** tại ICM Philadelphia. Trích dẫn ngắn của IMU:

> For her work in harmonic analysis and geometric measure theory, including applications of multiscale and decoupling techniques to the local smoothing conjecture for the planar wave equation, and major advances in Fourier restriction, Falconer distance sets, Furstenberg sets in the plane, and the Kakeya problem in three dimensions.  
> — [IMU, Fields Medal 2026](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf)

*Tạm dịch:* Cho các công trình về giải tích điều hòa và lý thuyết độ đo hình học, gồm việc áp dụng kỹ thuật đa thang và kỹ thuật tách (decoupling) vào giả thuyết làm trơn địa phương cho phương trình sóng trên mặt phẳng, cùng những tiến bộ lớn về bài toán hạn chế Fourier, tập khoảng cách Falconer, tập Furstenberg trên mặt phẳng và bài toán Kakeya ba chiều.

Bà là **người phụ nữ thứ ba** nhận Huy chương Fields (sau Maryam Mirzakhani năm 2014 và Maryna Viazovska năm 2022). Kết quả được báo chí nhắc đến nhiều nhất là chứng minh **giả thuyết tập Kakeya trong không gian ba chiều**, thực hiện cùng **Joshua Zahl** (arXiv:2502.17655, 2025). Tuy vậy, huy chương ghi nhận **toàn bộ các công trình** của bà, không chỉ một bài báo.

Bài học đi theo trình tự:

**Bài toán chiếc kim → Tập Besicovitch → độ đo và số chiều → ống δ → định lý Wang–Zahl → giải tích điều hòa → các công trình được nêu trong lời trích dẫn.**

Mục tiêu không phải là trình bày lại chứng minh dài 127 trang, mà là hiểu **bài toán hỏi gì**, **vì sao nó khó suốt một thế kỷ**, và **những lĩnh vực toán học nào liên quan**.

Câu hỏi chính: một tập trong $$\mathbb{R}^n$$ có thể nhỏ đến mức nào mà vẫn chứa một đoạn thẳng dài 1 theo mọi hướng? Câu hỏi liên quan: cách các hướng sắp xếp ở nhiều thang khác nhau ảnh hưởng thế nào đến bài toán hạn chế Fourier, tập khoảng cách Falconer, tập Furstenberg và tính làm trơn địa phương của sóng?

Cách tiếp cận hiện đại chuyển hình học của các hướng thành bài toán ước lượng cho các họ **ống δ** (δ-tube) rất mảnh. Sau đó người ta phân tích cấu trúc ở nhiều thang (sự tụ cụm, tính "hạt", tính "phẳng", kỹ thuật tách) để chứng minh rằng khi các ống chồng lên nhau quá nhiều thì chúng buộc phải có một cấu trúc hình học khai thác được, chứ không thể sắp xếp tùy ý. Kết quả chính cùng Zahl là một ước lượng thể tích: nếu "không có quá nhiều ống nằm trong cùng một tập lồi $$V$$" thì hợp của các ống có thể tích gần lớn nhất có thể. Từ đó suy ra mọi tập Kakeya trong $$\mathbb{R}^3$$ có chiều Hausdorff và chiều Minkowski bằng 3. Lời trích dẫn dài của IMU còn nêu: tính làm trơn địa phương của phương trình sóng trên mặt phẳng (cùng Guth và Zhang); kết quả về bài toán Falconer (cùng Guth, Iosevich và Ou); tập Furstenberg trên mặt phẳng (cùng Ren); và các tiến bộ về bài toán hạn chế Fourier.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu bài toán chiếc kim của Kakeya và cách Besicovitch xây dựng một tập có độ đo bằng 0 trên mặt phẳng.
- Giải thích vì sao **độ đo Lebesgue bằng 0** không kéo theo **chiều Hausdorff (hay Minkowski)** nhỏ hơn số chiều của không gian.
- Phát biểu **giả thuyết tập Kakeya** trong $$\mathbb{R}^n$$ và nêu các kết quả đã biết cho $$n=2$$ và $$n=3$$.
- Mô tả hình ảnh các **ống δ** và giải thích vì sao sự chồng lấp mạnh giữa các ống mới là khó khăn thật sự.
- Đặt kết quả **Wang–Zahl (2025)** và **Huy chương Fields của Wang (2026)** vào bối cảnh lịch sử dài hơn.
- Tóm tắt, kèm tên các cộng sự, những đóng góp của Wang **ngoài** bài toán Kakeya (làm trơn địa phương, Falconer, Furstenberg, bài toán hạn chế).
- Tránh các nhầm lẫn thường gặp (chuyển động của chiếc kim và tập Besicovitch; công lao chung; thể tích và số chiều).

**Kiến thức cần có.** Không gian Euclid, trực giác về diện tích và thể tích, ý tưởng fractal có số chiều không nguyên. Biến đổi Fourier chỉ cần ở mức khái niệm.

---

## 1. Bài toán chiếc kim: phát biểu đơn giản, kết quả bất ngờ

Năm 1917, **Sōichi Kakeya** hỏi (đại ý): một chiếc kim dài 1 cần được **xoay liên tục** trong một miền phẳng sao cho cuối cùng đầu và đuôi đổi chỗ cho nhau. Miền đó phải có diện tích nhỏ nhất là bao nhiêu?

Theo trực giác, chiếc kim dài 1 phải quét qua một vùng "đáng kể". Xoay quanh trung điểm thì cần một hình tròn bán kính $$1/2$$ (diện tích $$\pi/4$$). Có những cách di chuyển khéo hơn cần ít diện tích hơn, ví dụ cổ điển là hình **deltoid**. Dù vậy, người ta vẫn nghĩ rằng diện tích phải có **một chặn dưới dương**.

Besicovitch chứng minh một điều mạnh hơn nhiều so với việc "diện tích có thể nhỏ hơn một chút".

![Đoạn đơn vị theo nhiều hướng]({{ site.baseurl }}/img/chapter_img/kakeya_needle_directions.svg)

*Hình. Tập Kakeya phải chứa một đoạn dài 1 theo mọi hướng, nhưng bản thân tập đó không nhất thiết trông "đầy đặn".*

---

## 2. Tập Besicovitch: chứa mọi hướng nhưng có độ đo bằng 0

Một **tập Kakeya** (còn gọi là **tập Besicovitch**) trong $$\mathbb{R}^n$$ là tập chứa một đoạn thẳng dài 1 theo **mọi** hướng.

**Abram Besicovitch** (khoảng 1919–1928) chứng minh rằng trên mặt phẳng tồn tại những tập như vậy có **độ đo Lebesgue bằng 0**. Nói cách khác, với mọi $$\varepsilon>0$$ ta có thể dựng một tập có diện tích nhỏ hơn $$\varepsilon$$ mà vẫn chứa đoạn dài 1 theo mọi hướng; qua một phép lấy giới hạn thích hợp, ta được một tập có độ đo đúng bằng 0.

Về lịch sử, Besicovitch ban đầu nghiên cứu vấn đề này vì một câu hỏi về **tích phân lặp** trong lý thuyết tích phân Riemann. Cách dựng của ông sau đó cũng giải luôn bài toán chiếc kim của Kakeya: kết hợp với một kỹ thuật của Pál, ta có thể xoay chiếc kim trong một miền có diện tích nhỏ tùy ý. Vì vậy, tên gọi **tập Besicovitch** là hợp lý.

### Làm sao diện tích có thể bằng 0?

Độ dài của mỗi đoạn luôn là $$1$$. Cái ta có thể làm là **dùng lại cùng một phần mặt phẳng cho rất nhiều hướng**, rồi lấy giới hạn của các lân cận ngày càng mỏng để được một tập kiểu fractal.

![Cắt và trượt tam giác]({{ site.baseurl }}/img/chapter_img/besicovitch_triangle_overlap.svg)

*Hình. Minh họa kinh điển: cắt một tam giác thành nhiều phần, trượt các phần để chúng chồng lên nhau nhiều hơn, rồi lặp lại.*

Một hình ảnh hay dùng khi giảng dạy là **rèm sáo lặp lại**: các dải mỏng gần song song được nghiêng, cắt và xếp lại sao cho vẫn giữ được mọi hướng trong khi tổng diện tích giảm mạnh.

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

**Chiều Minkowski (chiều đếm hộp)** dễ hình dung: phủ tập bằng các hộp cạnh $$r$$ và xem số hộp cần dùng tăng theo lũy thừa nào của $$1/r$$ khi $$r\to 0$$.

**Chiều Hausdorff** được định nghĩa tinh tế hơn bằng lý thuyết độ đo. Với nhiều tập "đủ đẹp", hai khái niệm này trùng nhau. Bài toán Kakeya nghiên cứu cả hai.

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

## 5. Vì sao trường hợp 3 chiều khó? Các ống δ

Thay mỗi đoạn thẳng dài 1 bằng một **ống** mảnh dài khoảng 1, bán kính $$\delta$$ (gọi là ống δ, δ-tube). Khi nhìn ở thang $$\delta$$, một tập Kakeya giống như một họ rất lớn các ống, mỗi ống theo một hướng (hoặc theo một lưới hướng rất mịn).

![δ-tube chồng lấp]({{ site.baseurl }}/img/chapter_img/kakeya_delta_tubes.svg)

*Hình. Nhiều ống δ; những vùng các ống chồng lên nhau nhiều là nơi hình học trở nên phức tạp.*

Nếu các ống gần như không chồng lên nhau, thể tích của hợp trong $$\mathbb{R}^3$$ vào cỡ $$N\cdot \delta^{2}$$. Trường hợp khó là khi các ống **chồng lên nhau rất nhiều**:

$$
\bigl\lvert \bigcup_i T_i\bigr\rvert \;\ll\; \sum_i \lvert T_i\rvert.
$$

> **Hợp của rất nhiều ống theo nhiều hướng có thể nhỏ đến mức nào?**

### Hình dung bằng sợi mì

Hãy tưởng tượng hàng triệu sợi mì spaghetti rất mảnh, mỗi sợi theo một hướng, cần được nhét vào một vùng nhỏ nhất có thể.

- **Nếu để tản ra**, chúng chiếm nhiều không gian và số chiều rõ ràng là lớn.  
- **Nếu bó chặt**, chúng tạo thành những bó dày. Nhưng sự tập trung cực mạnh như vậy không thể tùy ý: các sợi phải gần song song, tập trung quanh một đường hay một mặt, hoặc tạo thành cấu hình kiểu **regulus** (họ đường thẳng trên một mặt hyperboloid một tầng).

Ý tưởng trong phân tích của Wang–Zahl: **khi các ống chồng lên nhau quá nhiều, chúng buộc phải có cấu trúc hình học**, và cấu trúc đó có thể khai thác ở một thang khác.

### Tính "hạt" ở nhiều thang

Ở thang thô, tập có thể trông như một khối đặc. Phóng to lên, ta thấy các ống mảnh. Phóng to thêm nữa lại thấy các cấu trúc "hạt" mới. Bài toán vì thế có bản chất đa thang:

$$
1 \;\to\; \delta \;\to\; \delta^{2} \;\to\; \cdots
$$

Trong không gian ba chiều, các ống có thể cắt chéo nhau, gần song song, tập trung theo đường hoặc mặt, hoặc tạo thành cấu hình regulus. Các phương pháp cho mặt phẳng không mở rộng một cách đơn giản lên ba chiều. Các bản tóm tắt của chuyên gia (ví dụ của Larry Guth) nhấn mạnh rằng chứng minh dài vì phải theo dõi cấu trúc ở nhiều thang cùng một lúc.

---

## 6. Wang và Zahl thực sự chứng minh điều gì?

<div class="textbook-theorem" markdown="1">
**Định lý (Wang–Zahl, 2025).**  
Mọi tập Kakeya $$K\subset\mathbb{R}^3$$ thỏa

$$
\dim_H(K) = \dim_M(K) = 3.
$$
</div>

Nguồn chính: *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions* ([arXiv:2502.17655](https://arxiv.org/abs/2502.17655); 127 trang). Phần tóm tắt nêu rõ kết quả kỹ thuật: với một họ ống $$\delta$$ trong $$\mathbb{R}^3$$ mà không có quá nhiều ống nằm trong cùng một tập lồi $$V$$, hợp của chúng có **thể tích gần lớn nhất có thể**. Kết luận số chiều bằng 3 cho tập Kakeya được suy ra từ ước lượng này.

Định lý **không** nói tập Kakeya ba chiều phải có thể tích dương; tập có độ đo bằng 0 kiểu Besicovitch vẫn tồn tại. Nội dung định lý là:

> Tập Kakeya có thể có **thể tích bằng 0**, nhưng không thể có số chiều fractal nhỏ hơn 3.

### Phác thảo chiến lược (không phải chứng minh)

1. Đưa bài toán Kakeya về ước lượng cho họ các ống mảnh.  
2. Phân tích các giao điểm và sự tụ cụm của các ống.  
3. Nếu các ống chồng lên nhau rất nhiều, chứng minh chúng phải có **cấu trúc hình học** (tính "dính", tính "hạt", tính "phẳng", là các chủ đề trong chương trình của Katz–Tao).  
4. Dùng cấu trúc đó để chứng minh cấu hình phải **giãn ra** ở một thang khác (**tự cải thiện**).  
5. Lập luận **quy nạp theo thang**.  
6. Kết luận số chiều không thể nhỏ hơn 3.

**Ý tưởng tự cải thiện.**

$$
\text{cấu hình xấu ở một thang}
\;\Longrightarrow\;
\text{cấu trúc ẩn}
\;\Longrightarrow\;
\text{cấu hình tốt hơn ở thang khác}.
$$

Công trình trước đó của Wang–Zahl về tập Kakeya **dính** (sticky) là một bước chuẩn bị quan trọng. Tập dính có tính tự đồng dạng gần đúng ở nhiều thang và đã xuất hiện trong công trình của Katz–Łaba–Tao (1999). Wang–Zahl chứng minh giả thuyết Kakeya cho tập dính trong không gian ba chiều ([arXiv:2210.09581](https://arxiv.org/abs/2210.09581); *J. Amer. Math. Soc.* **39** (2026), 515–585).

**Ghi nhận công lao.** Đây là **công trình chung** của hai tác giả. Kết quả này là đỉnh cao của cả một thế kỷ nghiên cứu, dựa trên công trình của nhiều người đi trước.

![Dòng thời gian]({{ site.baseurl }}/img/chapter_img/kakeya_history_timeline.svg)

*Hình. Một số mốc từ Kakeya (1917) đến Huy chương Fields của Wang (2026).*

---

## 7. Vì sao giải tích điều hòa quan tâm đến bài toán này?

Bài toán Kakeya nằm ở chỗ giao nhau của:

- **lý thuyết độ đo hình học**,
- **giải tích điều hòa** (bài toán hạn chế Fourier, hàm cực đại, tích phân dao động),
- **phương trình đạo hàm riêng** (tính làm trơn địa phương của phương trình sóng, sự tập trung của nghiệm).

**Biến đổi Fourier** cho tương ứng hàm $$f(x)$$ với phổ tần số $$\hat f(\xi)$$ của nó. Khi nghiên cứu các sóng có cùng bước sóng nhưng theo nhiều hướng, hay khi hạn chế biến đổi Fourier lên một mặt cong, năng lượng thường chia thành các **bó sóng** (wave packet) nằm trên những ống dài và mảnh. Cách các ống này chồng lên nhau quyết định năng lượng có thể **tập trung** lại hay buộc phải **lan ra**.

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
**Bằng cách nào.** Phân tích đa thang, kỹ thuật tách, hình học liên thuộc và hình học các ống.  
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

Độ đo Hausdorff, định nghĩa qua một hàm cỡ (gauge function), đo "độ lớn" của một tập khi thể tích của nó bằng 0. Một tập có thể có độ đo bằng 0 nhưng $$\dim_H$$ vẫn bằng số chiều của không gian. **LO2:** độ đo bằng 0 **không** kéo theo số chiều bằng 0; số chiều đầy đủ **không** kéo theo độ đo Lebesgue dương.

### C4. Kakeya ba chiều và Wang–Zahl (theo Quanta và các nguồn phổ thông)

Giả thuyết ba chiều (dạng phổ thông) nói rằng mọi tập Kakeya trong $$\mathbb{R}^3$$ có số chiều đầy đủ bằng 3. Wang và Zahl đã chứng minh điều này; các bài tường thuật nhấn mạnh việc phân tích ống δ ở nhiều thang và các cấu hình dính. Khi trình bày, cần lưu ý:

| Nên nói | Không nên nói |
|----------|-----------|
| **Wang và Zahl** | "Một mình Wang" |
| Kết quả về **số chiều** trong không gian ba chiều | "Mọi tập Kakeya đều có thể tích dương" |
| Trường hợp $$n\ge 4$$ vẫn còn mở | "Bài toán Kakeya đã xong hoàn toàn" |
| Lời trích dẫn của IMU rộng hơn bài toán Kakeya | "Giải Fields chỉ vì Kakeya" |

### C5. Video tiếng Việt

Dùng để làm quen với chủ đề. Phụ đề tự động hoặc chỗ ghi sai tên, sai năm là cơ hội luyện mục tiêu **LO6**: đối chiếu với arXiv và IMU trước khi trích dẫn.

### C6. Tài liệu hỗ trợ

Xem `TRANSCRIPT_STATUS.md` và các tệp `*_knowledge_units.json`. Khi làm bài có chấm điểm, hãy dùng ký hiệu và thuật ngữ của bài học (ống δ, chiều Hausdorff, tập dính), đừng chép nguyên phụ đề.

---

## Thách thức và mở rộng

1. Phân biệt **chuyển động liên tục của chiếc kim** với **tập Besicovitch cố định**.  
2. Có thể chặn dưới $$\lvert\bigcup T_i\rvert$$ như thế nào theo $$\delta$$ và số hướng?  
3. Vì sao trường hợp **tập dính** có thể là "đối thủ" tự nhiên của giả thuyết?  
4. Phát biểu lại bài toán Kakeya như một bài toán chặn mức độ tập trung của các bó sóng.  
5. Nêu hai khó khăn hình học xuất hiện ở chiều 4 mà ở chiều 3 nhẹ hơn.

---

## Bài tập

1. **Khởi động.** Vì sao một đoạn thẳng trên mặt phẳng có diện tích 0 nhưng không phải là tập Kakeya?  
2. **Định nghĩa.** Viết định nghĩa: tập Kakeya trong $$\mathbb{R}^n$$; chiều Hausdorff (ở mức trực giác); ống δ.  
3. **Davies và Besicovitch.** Vì sao kết quả của Davies **bổ sung** chứ không mâu thuẫn với kết quả của Besicovitch?  
4. **Ước lượng thể tích.** Nếu có $$N$$ ống, mỗi ống thể tích $$c\delta^{2}$$, đôi một rời nhau, hãy ước lượng thể tích của hợp. Kết quả thay đổi thế nào nếu mọi cặp ống giao nhau với thể tích $$\approx\delta^{3}$$?  
5. **Tổng hợp.** Vẽ sơ đồ  
   `Kakeya → tubes → cấu trúc đa thang → Fourier / PDE`  
   và giải thích mỗi mũi tên bằng một câu.  
6. **Đọc bài nghiên cứu.** Mở [arXiv:2502.17655](https://arxiv.org/abs/2502.17655), chỉ đọc phần tóm tắt và phần mở đầu: chép lại phát biểu chính về thể tích và liệt kê ba hướng nghiên cứu đi trước.  
7. **Đọc lời trích dẫn.** So sánh [trích dẫn ngắn của IMU](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf) với một bài báo phổ biến khoa học. Cộng sự nào chỉ được nhắc đến trong văn bản chính thức?

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

- Cách nghĩ nên giữ: các ống δ như một bài toán về sự tụ cụm ở nhiều thang.  
- Các câu hỏi còn mở: bài toán Kakeya ở chiều cao hơn; bài toán hạn chế và làm trơn địa phương (tính đến năm 2026).

## Video tham khảo

- **Xem trước** — [A Once-in-a-Century Proof: The Kakeya Conjecture](https://www.youtube.com/watch?v=5J3tYU_-IZI) — Quanta Magazine, tiếng Anh. Video phổ thông về bài toán Kakeya và chứng minh Wang–Zahl, có phỏng vấn các tác giả. Nên xem trước khi đọc bài.
- [What is Hausdorff Dimension? Intuition, Gauge Functions, and Hausdorff Measures](https://www.youtube.com/watch?v=LJcWhcM4okQ) — CHALK, tiếng Anh. Giải thích chiều Hausdorff và độ đo Hausdorff, hỗ trợ cho mục 2–3. Nên xem khi đọc đến phần số chiều.
- [Methods for Estimating Hausdorff Dimension: Bounds and The Mass Distribution Principle](https://www.youtube.com/watch?v=FQXbRGmAbUY) — CHALK, tiếng Anh. Các cách ước lượng chiều Hausdorff (chặn trên bằng phép phủ, chặn dưới bằng nguyên lý phân bố khối lượng). Dành cho người muốn hiểu kỹ hơn phần kỹ thuật.
