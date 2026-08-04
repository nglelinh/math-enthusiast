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
> **1. Trước:** [Bản đồ Kakeya Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/)  
> **2. Bạn đang ở đây:** Bài Wang Ch.2 (lý thuyết đầy đủ)  
> **3. Tiếp:** [Studio Kakeya Ch.7]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/)  
> *Nên làm Ch.1 trước nếu lần đầu gặp Kakeya.*

**Hong Wang** (NYU Courant; giáo sư thường trực tại IHES) được trao **Huy chương Fields 2026** tại ICM Philadelphia. Trích dẫn ngắn của IMU:

> For her work in harmonic analysis and geometric measure theory, including applications of multiscale and decoupling techniques to the local smoothing conjecture for the planar wave equation, and major advances in Fourier restriction, Falconer distance sets, Furstenberg sets in the plane, and the Kakeya problem in three dimensions.  
> — [IMU, Fields Medal 2026](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf)

Bà là **người phụ nữ thứ ba** nhận Fields Medal (sau Maryam Mirzakhani 2014 và Maryna Viazovska 2022). Thành tựu hình học được nhắc nhiều nhất trên truyền thông là **giả thuyết tập Kakeya ba chiều**, chứng minh cùng **Joshua Zahl** (arXiv:2502.17655, 2025). Tuy nhiên, huy chương ghi nhận **cả khối công trình**, không chỉ một bài báo.

Lộ trình bài học:

**Bài toán kim → Tập Besicovitch → measure vs dimension → δ-tube → Wang–Zahl → Giải tích điều hòa → Danh mục Fields.**

Mục tiêu không phải tái tạo chứng minh 127 trang, mà hiểu **bài toán hỏi gì**, **vì sao kháng cự cả thế kỷ**, và **toán học nào nằm bên dưới**.

Tập trong $$\mathbb{R}^n$$ có thể nhỏ đến mức nào mà vẫn chứa đoạn đơn vị theo mọi hướng? Đồng thời: cấu hình hướng đa thang đo kiểm soát Fourier restriction, tập khoảng cách Falconer, tập Furstenberg và local smoothing cho sóng như thế nào?

Cách tiếp cận hiện đại diễn lại hình học hướng như ước lượng họ **δ-tube** mỏng, dùng phân tích cấu trúc đa thang (clustering, graininess, planiness, decoupling) để chồng lấp cực đoan buộc phải sinh ra hình học khai thác được, chứ không phải hỗn loạn thuần túy. Với Zahl: ước lượng thể tích hợp ống dưới giả thuyết “không quá nhiều ống nằm trong cùng một tập lồi $$V$$” kéo theo mọi tập Kakeya trong $$\mathbb{R}^3$$ có chiều Hausdorff và Minkowski bằng 3. Rộng hơn (trích dẫn dài IMU): local smoothing phương trình sóng phẳng với Guth–Zhang; kết quả Falconer với Guth–Iosevich–Ou; tập Furstenberg trên mặt phẳng với Ren; cùng các tiến bộ restriction. Huy chương Fields 2026.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu bài toán kim của Kakeya và construction measure zero của Besicovitch trên mặt phẳng.
- Giải thích vì sao **độ đo Lebesgue bằng 0** không buộc **chiều Hausdorff (hay Minkowski)** nhỏ hơn chiều không gian.
- Phát biểu **giả thuyết tập Kakeya** trong $$\mathbb{R}^n$$ và nêu kết quả đã biết với $$n=2$$, $$n=3$$.
- Mô tả hình ảnh **δ-tube** và vì sao chồng lấp mạnh mới là khó khăn thực sự.
- Đặt **Wang–Zahl (2025)** và **Fields Medal của Wang (2026)** vào dòng lịch sử dài hơn.
- Tóm tắt, có tên cộng tác viên, các đóng góp của Wang **ngoài** Kakeya (local smoothing, Falconer, Furstenberg, restriction).
- Tránh nhầm lẫn phổ biến (chuyển động kim vs tập Besicovitch; công lao chung; volume vs dimension).

**Kiến thức nền.** Không gian Euclid, trực giác diện tích/thể tích, fractal có chiều không nguyên. Fourier chỉ ở mức khái niệm.

---

## 1. Bài toán chiếc kim: nghe đơn giản nhưng cực kỳ quái

Năm 1917, **Sōichi Kakeya** hỏi (đại ý): diện tích nhỏ nhất của miền phẳng trong đó kim dài 1 có thể được **đảo chiều liên tục**—quay qua mọi hướng cho đến khi đầu–đuôi đảo ngược—là bao nhiêu?

Trực giác: kim dài 1 phải quét vùng “đáng kể”. Quay quanh trung điểm tạo đĩa bán kính $$1/2$$ (diện tích $$\pi/4$$). Chuyển động khéo hơn cải thiện đĩa; **deltoid** là ví dụ cổ điển. Dù vậy, người ta vẫn kỳ vọng **chặn dưới dương**.

Besicovitch cho thấy điều mạnh hơn nhiều so với “diện tích có thể nhỏ hơn một chút”.

![Đoạn đơn vị theo nhiều hướng]({{ site.baseurl }}/img/chapter_img/kakeya_needle_directions.svg)

*Hình. Tập Kakeya phải chứa đoạn dài 1 theo mọi hướng—tập chứa không nhất thiết trông “đầy”.*

---

## 2. Tập Besicovitch: mọi hướng, độ đo không

Một **tập Kakeya** (còn gọi **tập Besicovitch**) trong $$\mathbb{R}^n$$ là tập chứa đoạn thẳng đơn vị theo **mọi** hướng.

**Abram Besicovitch** (khoảng 1919–1928) chứng minh trên mặt phẳng tồn tại các tập như vậy với **độ đo Lebesgue bằng 0**. Tương đương: với mọi $$\varepsilon>0$$ có thể xây tập diện tích nhỏ hơn $$\varepsilon$$ vẫn chứa đoạn đơn vị mọi hướng; lấy giới hạn thích hợp được measure đúng bằng 0.

Về lịch sử, động lực ban đầu của Besicovitch liên quan **tích phân lặp** trong lý thuyết Riemann; construction sau đó cũng giải bài toán Kakeya (cùng các needle set diện tích dương tùy ý nhỏ và các phép quy về kiểu Pál). Gọi là **tập Besicovitch** là hợp lý về mặt lịch sử.

### Làm sao diện tích có thể bằng 0?

Độ dài đoạn cố định bằng $$1$$. Điều có thể làm là **tái sử dụng cực mạnh cùng các điểm** cho nhiều hướng, rồi chuyển sang giới hạn fractal của các lân cận ngày càng mỏng.

![Cắt và trượt tam giác]({{ site.baseurl }}/img/chapter_img/besicovitch_triangle_overlap.svg)

*Hình. Minh họa kinh điển: cắt tam giác đều, trượt nửa để tăng chồng lấp, lặp lại.*

Hình ảnh sư phạm hiện đại: **Venetian blind lặp**—các dải mỏng gần song song được nghiêng, cắt, xếp lại để giữ thông tin hướng trong khi tổng diện tích sụp đổ.

![Venetian blind]({{ site.baseurl }}/img/chapter_img/venetian_blinds_kakeya.svg)

*Hình. Sơ đồ Venetian-blind (không phải construction đầy đủ theo nghĩa đen).*

**Insight then chốt.** Diện tích hình chữ nhật dài 1, rộng $$\delta$$ cỡ $$\delta$$. Khi $$\delta\to 0$$ diện tích triệt tiêu—nhưng số hướng là **vô hạn**. Nghệ thuật của Besicovitch là **tái sử dụng không gian** có hệ thống.

### Davies (1971): dimension vẫn bằng 2

Measure zero **không** có nghĩa tập “một chiều”. **Roy Davies** chứng minh mọi tập Kakeya trên mặt phẳng có **chiều Hausdorff bằng 2**:

$$
\lvert E\rvert = 0 \quad\text{có thể, nhưng}\quad \dim_H(E) = 2.
$$

Nghịch lý lớn đầu tiên: **trống về diện tích, đầy về dimension**.

---

## 3. Dimension không chỉ có 1, 2, 3

Hình học thông thường gán chiều nguyên. Fractal cho phép giá trị trung gian ($$1.5$$, $$2.7$$, …).

**Chiều Minkowski (đếm hộp)** dễ hình dung: phủ bằng hộp cạnh $$r$$ và đọc số mũ co giãn của số hộp khi $$r\to 0$$.

**Chiều Hausdorff** tinh tế hơn theo lý thuyết độ đo. Với nhiều tập “đủ đẹp” hai khái niệm trùng nhau; Kakeya nghiên cứu cả hai.

> **Thể tích bằng 0 không buộc dimension nhỏ hơn 3.**  
> Một tập trong $$\mathbb{R}^3$$ có thể có độ đo Lebesgue 0 mà vẫn có chiều Minkowski bằng 3.

![Measure và dimension]({{ site.baseurl }}/img/chapter_img/measure_vs_dimension.svg)

*Hình. Hai khái niệm “kích thước” khác nhau.*

---

## 4. Giả thuyết tập Kakeya nói gì?

**Giả thuyết (tập Kakeya trong $$\mathbb{R}^n$$).**  
Mọi tập Kakeya $$K\subset\mathbb{R}^n$$ có chiều Hausdorff và Minkowski bằng $$n$$:

$$
\dim_H(K) = \dim_M(K) = n.
$$

| Chiều không gian | Tình trạng |
|------------------|------------|
| $$n=1$$ | Tầm thường |
| $$n=2$$ | Đã chứng minh (Davies, 1971) |
| $$n=3$$ | Đã chứng minh (**Wang–Zahl**, 2025) |
| $$n\ge 4$$ | Còn mở (có chặn dưới từng phần) |

Besicovitch đã biết tập Kakeya **measure zero** tồn tại ở chiều cao. Giả thuyết nói chúng vẫn không thể “mỏng” quá theo nghĩa fractal.

---

## 5. Vì sao 3D khó? Xuất hiện δ-tube

Thay mỗi đoạn đơn vị bằng **ống** mỏng dài khoảng 1, bán kính $$\delta$$ (δ-**tube**). Tập Kakeya ở thang $$\delta$$ trông như họ khổng lồ các ống, mỗi ống một hướng (hoặc lưới mịn các hướng).

![δ-tube chồng lấp]({{ site.baseurl }}/img/chapter_img/kakeya_delta_tubes.svg)

*Hình. Nhiều δ-tube; vùng chồng lấp mạnh là nơi hình học trở nên tinh vi.*

Nếu ống hầu như không chồng, thể tích hợp trong $$\mathbb{R}^3$$ cỡ $$N\cdot \delta^{2}$$. Ác mộng là **chồng lấp khổng lồ**:

$$
\bigl\lvert \bigcup_i T_i\bigr\rvert \;\ll\; \sum_i \lvert T_i\rvert.
$$

> **Hợp của rất nhiều ống đa hướng có thể nhỏ đến mức nào?**

### Trực giác spaghetti

Hàng triệu sợi spaghetti cực mảnh, mỗi sợi một hướng, bị nhét vào vùng nhỏ nhất có thể.

- **Phân tán.** Chiếm không gian lớn; dimension “rõ ràng” lớn.  
- **Bó chặt.** Tạo bó dày. Tập trung cực đoan không phải hỗn loạn thuần: họ gần song song, tập trung quanh đường/mặt, cấu hình kiểu **regulus**.

Phân tích kiểu Wang–Zahl: **chồng lấp cực đoan buộc cấu trúc hình học** khai thác được ở thang khác.

### “Graininess” đa thang đo

Ở thang thô có thể trông như khối đặc; zoom vào thấy ống mỏng; zoom tiếp lộ cấu trúc hạt mới. Bài toán bản chất đa thang:

$$
1 \;\to\; \delta \;\to\; \delta^{2} \;\to\; \cdots
$$

Trong 3D, ống có thể giao chéo, gần song song, tập trung theo đường/mặt, tạo cấu hình regulus. Phương pháp 2D không “tensor” lên một cách đơn giản. Các outline chuyên gia (ví dụ của Larry Guth) nhấn mạnh chứng minh dài vì phải theo dõi cấu trúc qua nhiều thang đo cùng lúc.

---

## 6. Wang và Zahl thực sự chứng minh điều gì?

**Định lý (Wang–Zahl, 2025).**  
Mọi tập Kakeya $$K\subset\mathbb{R}^3$$ thỏa

$$
\dim_H(K) = \dim_M(K) = 3.
$$

Nguồn chính: *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions* ([arXiv:2502.17655](https://arxiv.org/abs/2502.17655); 127 trang). Abstract nêu động cơ kỹ thuật rõ ràng: với họ $$\delta$$-tube trong $$\mathbb{R}^3$$ sao cho không quá nhiều ống nằm trong cùng một tập lồi $$V$$, hợp có **thể tích gần cực đại**; dimension 3 cho tập Kakeya suy ra từ đó.

Họ **không** khẳng định tập Kakeya 3D có thể tích dương—measure zero kiểu Besicovitch vẫn có thể. Định lý sâu hơn:

> Có thể **thể tích bằng 0**, nhưng không thể chứa mọi hướng trong fractal chiều thực sự nhỏ hơn 3.

### Chiến lược phác thảo (không phải chứng minh)

1. Đưa Kakeya về ước lượng họ ống mỏng.  
2. Phân tích giao và clustering.  
3. Nếu chồng lấp cực mạnh, chứng minh phải có **cấu trúc hình học** (stickiness, graininess, planiness—chủ đề trong chương trình Katz–Tao).  
4. Khai thác cấu trúc để buộc cấu hình **nở ra** ở thang khác (**self-improvement**).  
5. Chạy **quy nạp theo thang đo**.  
6. Kết luận dimension không thể ở dưới 3.

**Khẩu hiệu self-improvement.**

$$
\text{cấu hình xấu ở một thang}
\;\Longrightarrow\;
\text{cấu trúc ẩn}
\;\Longrightarrow\;
\text{cấu hình tốt hơn ở thang khác}.
$$

Công trình trước của Wang–Zahl về tập Kakeya **sticky** là bước đệm quan trọng. Tập sticky mang tính tự đồng dạng gần đúng đa thang và đã đóng vai trò trong Katz–Łaba–Tao (1999). Wang–Zahl chứng minh giả thuyết sticky Kakeya ở ba chiều ([arXiv:2210.09581](https://arxiv.org/abs/2210.09581); *J. Amer. Math. Soc.* **39** (2026), 515–585).

**Ghi nhận công lao.** Đây là **công trình chung**. Kết quả là đỉnh của cả thế kỷ nghiên cứu—không phải chứng minh xuất hiện từ khoảng không.

![Dòng thời gian]({{ site.baseurl }}/img/chapter_img/kakeya_history_timeline.svg)

*Hình. Các mốc chọn lọc từ Kakeya (1917) đến Fields của Wang (2026).*

---

## 7. Vì sao giải tích điều hòa quan tâm?

Kakeya nằm ở giao của:

- **lý thuyết độ đo hình học**,
- **giải tích điều hòa** (Fourier restriction, hàm cực đại, tích phân dao động),
- **PDE** (local smoothing cho phương trình sóng, tập trung nghiệm).

**Biến đổi Fourier** ghép $$f(x)$$ với chân dung tần số $$\hat f(\xi)$$. Khi nghiên cứu sóng cùng bước sóng nhưng nhiều hướng—hoặc restriction Fourier lên mặt cong—năng lượng thường tổ chức thành **wave packet** sống trên ống dài mỏng. Cách ống chồng lấp quyết định năng lượng có thể **tập trung** hay buộc phải **lan tỏa**.

![Từ Kakeya đến harmonic analysis]({{ site.baseurl }}/img/chapter_img/kakeya_to_harmonic_analysis.svg)

*Hình. Chuỗi khái niệm từ hình học ống đến Fourier và PDE.*

Các “tháp giả thuyết” liên quan (restriction, Bochner–Riesz, local smoothing ở dạng sắc hơn / chiều cao) vẫn phụ thuộc hình học kiểu Kakeya. Giải Kakeya 3D làm thay đổi cảnh quan; không kết thúc câu chuyện.

---

## 8. Ngoài Kakeya: danh mục Fields (trích dẫn dài IMU)

Trích dẫn huy chương cố ý rộng hơn một định lý. Bản đồ nghiên cứu gọn:

| Chủ đề | Cộng tác viên (chọn lọc) | Đóng góp chính |
|--------|--------------------------|----------------|
| **Local smoothing** (sóng phẳng) | Larry Guth, Ruixiang Zhang | Multiscale + decoupling; giải local smoothing conjecture trên mặt phẳng (trích dẫn dài IMU) |
| **Tập khoảng cách Falconer** | Guth, Alex Iosevich, Yumeng Ou | Kết quả lớn nối chiều Hausdorff với phân bố khoảng cách |
| **Tập Furstenberg** (mặt phẳng) | Kevin Ren | Giải giả thuyết Furstenberg 2D ([arXiv:2308.08819](https://arxiv.org/abs/2308.08819)): tập $$(s,t)$$-Furstenberg có chiều ít nhất $$\min\bigl(s+t,\frac{3s+t}{2},s+1\bigr)$$ |
| **Fourier restriction** | nhiều cộng tác | Tiến bộ cấu trúc nuôi “tháp” restriction |
| **Kakeya 3D** | Joshua Zahl | Trường hợp sticky (JAMS 2026) và full dimension 3 (arXiv:2502.17655) |

**WHY.** Cấu hình fractal hướng kiểm soát cách năng lượng và measure có thể tập trung.  
**HOW.** Phân tích đa thang, decoupling, hình học incidence/ống.  
**WHAT.** Chuỗi định lý sắc; Kakeya 3D là lá cờ công chúng nổi nhất.

### Lộ trình (tiểu sử ngắn)

Sinh tại Quế Lâm (Guilin); học Đại học Bắc Kinh và École Polytechnique; tiến sĩ MIT dưới hướng dẫn **Larry Guth**; IAS, UCLA, rồi NYU Courant và IHES. Chuỗi giải thưởng (Salem, Ostrowski, Clay Research Award, New Horizons, …) trước **Fields Medal tại ICM 2026 (Philadelphia)**.

### Cách nói cho chính xác

- Giả thuyết Kakeya 3D là **công trình chung** với **Joshua Zahl**.  
- Fields Medal ghi nhận **cả khối công trình**; Kakeya 3D là mảnh nổi tiếng nhất, không phải toàn bộ trích dẫn.  
- Bà là **người phụ nữ thứ ba** nhận Fields.  
- **Kakeya chiều cao** ($$n\ge 4$$) và nhiều giả thuyết giải tích sắc vẫn mở tính đến 2026.

---

## 9. Nghịch lý sâu nhất, nói lại một lần

$$
\operatorname{Vol}(K)=0
\quad\text{có thể,}\quad
\dim(K)=3
\quad\text{là bắt buộc trong }\mathbb{R}^3.
$$

Bạn không thể nhét các đoạn đơn vị theo mọi hướng 3D vào fractal thực sự chiều thấp hơn 3. Đó là nội dung giả thuyết tập Kakeya 3D—và định lý Wang–Zahl.

---

## Nhầm lẫn phổ biến (fact-check)

| Khẳng định | Kết luận | Sửa |
|------------|----------|-----|
| “Wang một mình giải Kakeya 3D.” | **Sai** | Chung với Joshua Zahl. |
| “Tập Kakeya 3D phải có thể tích dương.” | **Sai** | Measure zero vẫn có thể; định lý nói về **dimension**. |
| “Fields chỉ vì Kakeya.” | **Sai** | IMU còn nêu local smoothing, restriction, Falconer, Furstenberg. |
| “Chuyển động kim = tập Besicovitch.” | **Sai** | Liên quan nhưng khác: **chuyển động** vs **tập tĩnh** chứa mọi hướng. |
| “Kakeya xong mọi chiều.” | **Sai** | $$n\ge 4$$ còn mở. |

---

## Thách thức và mở rộng

1. Phân biệt **chuyển động kim liên tục** và **tập Besicovitch tĩnh**.  
2. Chặn dưới nào cho $$\lvert\bigcup T_i\rvert$$ theo $$\delta$$ và số hướng?  
3. Vì sao trường hợp **sticky** có thể là “kẻ thù” tự nhiên của giả thuyết?  
4. Diễn đạt lại Kakeya như chặn tập trung wave packet.  
5. Nêu hai khó khăn hình học nặng hơn ở chiều 4.

---

## Bài tập

1. **Khởi động.** Vì sao đoạn thẳng trên mặt phẳng có diện tích 0 nhưng không phải tập Kakeya?  
2. **Định nghĩa.** Viết: tập Kakeya trong $$\mathbb{R}^n$$; chiều Hausdorff (mức trực giác); δ-tube.  
3. **Davies và Besicovitch.** Vì sao Davies là **tinh chỉnh** chứ không mâu thuẫn Besicovitch?  
4. **Heuristic thể tích.** Nếu $$N$$ ống thể tích $$c\delta^{2}$$ đôi một rời nhau, ước lượng hợp. Đổi gì nếu mọi cặp giao với thể tích $$\approx\delta^{3}$$?  
5. **Tổng hợp.** Vẽ  
   `Kakeya → tubes → cấu trúc đa thang → Fourier / PDE`  
   và chú thích mỗi mũi tên bằng một câu.  
6. **Đọc nghiên cứu.** Mở [arXiv:2502.17655](https://arxiv.org/abs/2502.17655); chỉ abstract + introduction: trích phát biểu thể tích chính và liệt kê ba hướng tiền bối.  
7. **Đọc trích dẫn.** So [trích dẫn ngắn IMU](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf) với một bài popular science; cộng tác viên nào chỉ xuất hiện ở văn bản chính thức?

---


## Nguồn video (gói math-video-researcher)

Chi tiết: `research/video-research/Wang_Harmonic_Analysis/`.

**Thứ tự xem gợi ý**

1. Quanta Kakeya: [YouTube](https://www.youtube.com/watch?v=5J3tYU_-IZI).  
2. CHALK Hausdorff: [YouTube](https://www.youtube.com/watch?v=LJcWhcM4okQ) · MDP: [YouTube](https://www.youtube.com/watch?v=FQXbRGmAbUY).  
3. Mathologer needle: [YouTube](https://www.youtube.com/watch?v=IM-n9c-ARHU).  
4. VI: [Pham Manh Tuyen](https://www.youtube.com/watch?v=XUkfpgFakMQ) · [TOÁN PRO](https://www.youtube.com/watch?v=pxVMKoZsVc8).  
5. arXiv:2502.17655 · IMU Wang PDF.

**Nhắc:** Kakeya 3D **đã chứng minh**; chiều cao hơn vẫn **mở**.

---



### Transcript & frames (extract flagship)

Transcript caption và unit theo thời gian: `research/video-research/Wang_Harmonic_Analysis/transcripts/` · trạng thái: `research/video-research/Wang_Harmonic_Analysis/TRANSCRIPT_STATUS.md` · danh sách master: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Caption tải tự động (yt-dlp)—dùng để điều hướng, **không** thay nội dung bài.


![Frame mẫu video flagship]({{ site.baseurl }}/img/video_research/flagships/kakeya_mathologer_frame01.jpg)

*Hình. Frame mẫu từ video flagship chính (xem pack cho timestamp).*

## Tài liệu tham khảo


Danh mục URL đầy đủ (mọi link khi nghiên cứu video): `research/video-research/Wang_Harmonic_Analysis/references.md`.

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
12. **Video phổ thông ★ (Quanta, EN):** [Once-in-a-Century Proof: Kakeya](https://www.youtube.com/watch?v=5J3tYU_-IZI) (~15 phút) — tháp restriction / Bochner–Riesz / local smoothing; sticky/grains; phỏng vấn Tao–Wang–Zahl. [Bài Quanta](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/). 2026-08-03.  
13. **Video phổ thông A (CHALK, EN):** [What is Hausdorff Dimension?](https://www.youtube.com/watch?v=LJcWhcM4okQ) (~13 phút) — gauge, $$\mathcal{H}^s$$, $$s=\dim_H$$; deep-link `&t=19s`. 2026-08-03.  
14. **Video phổ thông A′ (CHALK, EN):** [Estimating Hausdorff / MDP](https://www.youtube.com/watch?v=FQXbRGmAbUY) (~9 phút) — chặn trên phủ + Mass Distribution Principle. 2026-08-03.  
15. **Video phổ thông B (Mathologer, EN):** [Kakeya needle — squeegee](https://www.youtube.com/watch?v=IM-n9c-ARHU) (~17 phút) — chuyển động liên tục: parallel transfer, deltoid, cây Perron, cá ba cây; deep-link `&t=632s`. 2026-08-03.  
16. **Video phổ thông C (Pham Manh Tuyen):** [Giả Thuyết Kakeya…](https://www.youtube.com/watch?v=XUkfpgFakMQ) (~15 phút) — deltoid/Perron → Minkowski/Hausdorff → Wang–Zahl sketch. 2026-08-03.  
17. **Video phổ thông D (TOÁN PRO):** [Phỏng Đoán Kakeya…](https://www.youtube.com/watch?v=pxVMKoZsVc8) — đường đua chặn dưới. 2026-08-03. Sửa tên/năm sai từ phụ đề theo bài này.

*Ghi chú nghiên cứu.* Các khẳng định về định lý Kakeya 2025–2026 và trích dẫn Fields được đối chiếu abstract arXiv và PDF chính thức của IMU. Video phổ thông / Quanta chỉ cho bối cảnh không kỹ thuật.

---

## Hướng đi tiếp

**Tiếp lộ trình A**

1. [Bản đồ Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/) (ôn bảng trạng thái).  
2. Xong: bài Wang (trang này).  
3. **Tiếp →** [Studio Kakeya Ch.7]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/).  

- Mô hình tư duy: δ-tube như clustering đa thang.  
- Mục tiêu mở: Kakeya chiều cao; restriction / local smoothing (tính đến 2026).
