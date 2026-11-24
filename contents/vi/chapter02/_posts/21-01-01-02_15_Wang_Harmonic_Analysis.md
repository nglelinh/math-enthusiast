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

**Mạch bài học:** Bản đồ kiến thức nền (tính tay độ đo 0 vs chiều fractal trên tập Cantor, đếm ống $$\delta$$ trong 3D và bó sóng Fourier) → Bài toán chiếc kim & Tập Besicovitch → Giả thuyết Kakeya & hình ảnh sợi mì 3D → Khung giải thích chậm 4 bước về chứng minh Wang–Zahl (2025) → Các công trình khác trong lời trích dẫn IMU & ghi chú từ video chính.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Tự tính tay độ đo bằng $$0$$ nhưng chiều fractal $$\frac{\ln 2}{\ln 3} \approx 0{,}631$$ của tập Cantor để hiểu vì sao **thể tích bằng 0** không ép **chiều Hausdorff** nhỏ hơn 3.
- Phát biểu bài toán chiếc kim của Kakeya, cách dựng tập Besicovitch độ đo 0, và **giả thuyết tập Kakeya** trong $$\mathbb{R}^n$$ (đã giải cho $$n = 2, 3$$, còn mở cho $$n \ge 4$$).
- Tự ước lượng thể tích của họ $$\delta^{-2}$$ **ống $$\delta$$** trong $$\mathbb{R}^3$$ và hiểu mạch 4 bước phân tích đa thang (dính, hạt, phẳng, tự cải thiện) của **Wang–Zahl (2025)**.
- Giải thích cầu nối từ hình học ống $$\delta$$ sang **bó sóng**, bài toán hạn chế Fourier và phương trình sóng.
- Tóm tắt các đóng góp của Wang **ngoài** Kakeya (làm trơn địa phương cùng Guth–Zhang; Falconer cùng Guth–Iosevich–Ou; Furstenberg cùng Ren).

**Kiến thức cần có.** Không gian Euclid 2D/3D, thể tích hình trụ, logarit cơ bản và khái niệm biến đổi Fourier.

---

## Bản đồ kiến thức nền: Giải tích điều hòa và Lý thuyết độ đo hình học là gì?

### 1. Lý thuyết độ đo hình học: Độ đo bằng 0 nhưng số chiều vẫn lớn! (Tính tay trên tập Cantor)
Làm sao một tập hợp có thể tích bằng $$0$$ mà vẫn có số chiều đầy đủ? Hãy tự tính tay trên ví dụ fractal nổi tiếng nhất — **tập Cantor $$C \subset [0, 1]$$** (mỗi bước chia mỗi đoạn thành 3 phần bằng nhau rồi bỏ phần giữa):
- **Tổng chiều dài (độ đo Lebesgue):** Sau $$k$$ bước còn $$2^k$$ đoạn, mỗi đoạn dài $$3^{-k}$$ → tổng chiều dài $$(2/3)^k \xrightarrow{k\to\infty} \mathbf{0}$$!
- **Chiều Minkowski / Hausdorff (đếm hộp):** Muốn phủ tập Cantor bằng các đoạn nhỏ cạnh $$r = 3^{-k}$$, ta cần đúng $$N(r) = 2^k$$ đoạn. Viết $$N(r) = (1/r)^d = 3^{kd}$$, giải ra:

$$
3^{kd} = 2^k \;\Longrightarrow\; d = \frac{\ln 2}{\ln 3} \approx \mathbf{0{,}631} > 0!
$$

Độ đo Lebesgue đo "khối lượng" ở đúng số chiều nguyên, còn **chiều Hausdorff / Minkowski** đo *tốc độ tăng số hộp cần phủ khi thu nhỏ kích thước hộp*. Tập Kakeya trong $$\mathbb{R}^3$$ cũng vậy: thể tích bằng $$0$$, nhưng mọi tập Kakeya đều có số chiều bằng đúng **$$3$$**!

### 2. Đếm ống $$\delta$$ trong không gian 3 chiều (Tính tay thể tích!)
Thay mỗi đoạn thẳng dài 1 bằng một **ống $$\delta$$** (hình trụ dài $$1$$, bán kính $$\delta \ll 1$$):
- Thể tích một ống $$\delta$$ là $$\operatorname{Vol}(T_i) = \pi \delta^2 \cdot 1 \approx \delta^2$$.
- Mặt cầu đơn vị các hướng $$S^2$$ có diện tích $$4\pi$$; chia thành các hướng rời nhau cách nhau góc $$\delta$$ cho khoảng **$$N \approx \delta^{-2}$$ ống**.
- Nếu các ống không chồng lên nhau: tổng thể tích là $$N \cdot \delta^2 \approx \delta^{-2} \cdot \delta^2 = \mathbf{1}$$.
- **Câu hỏi Kakeya 3 chiều ở thang $$\delta$$:** Nếu ta cố sắp xếp $$\delta^{-2}$$ ống này chồng lên nhau khít nhất có thể, thể tích hợp $$\bigl\lvert \bigcup_i T_i \bigr\rvert$$ có thể bị nén nhỏ xuống $$\delta^\alpha$$ không? Định lý Wang–Zahl khẳng định: **Không!** Với mọi $$\varepsilon > 0$$, $$\bigl\lvert \bigcup_i T_i \bigr\rvert \ge c_\varepsilon \delta^\varepsilon$$ (gần như đạt thể tích cực đại $$1$$!).

### 3. Giải tích điều hòa: Tại sao sóng và biến đổi Fourier lại quan tâm đến ống $$\delta$$?
Khi giải phương trình sóng hoặc nghiên cứu bài toán **hạn chế Fourier** (lấy các sóng có tần số nằm trên mặt cầu hay mặt nón trong không gian tần số), sóng tổng hợp được phân rã thành các **bó sóng** (*wave packets*) — mỗi bó sóng là một "đốm năng lượng" có hình dạng đúng là một **ống $$\delta$$** chạy theo một hướng xác định! Nếu các ống $$\delta$$ có thể tụ cụm chồng khít vào một tập có số chiều nhỏ hơn 3, các bó sóng có thể giao thoa tăng cường dữ dội tạo ra đỉnh năng lượng bất thường. Vì vậy Kakeya là viên đá tảng của cả giải tích điều hòa!

---

## 1. Bài toán chiếc kim, Tập Besicovitch và Chiều fractal

Năm 1917, **Sōichi Kakeya** hỏi diện tích nhỏ nhất để xoay liên tục một chiếc kim dài 1 quay $$180^\circ$$ trên mặt phẳng (hình tròn mất $$\pi/4 \approx 0{,}785$$; hình deltoid mất $$\pi/8 \approx 0{,}393$$). **Abram Besicovitch** (1919–1928) gây chấn động khi chứng minh tồn tại **tập Besicovitch / tập Kakeya** (chứa đoạn thẳng dài 1 theo *mọi* hướng) có **độ đo Lebesgue bằng 0** bằng cách cắt tam giác thành nhiều mảnh mỏng rồi trượt chồng lên nhau lặp đi lặp lại (cây Perron / rèm sáo).

![Đoạn đơn vị theo nhiều hướng]({{ site.baseurl }}/img/chapter_img/kakeya_needle_directions.svg)

*Hình. Tập Kakeya phải chứa một đoạn dài 1 theo mọi hướng, nhưng bản thân tập đó không nhất thiết trông "đầy đặn".*

![Cắt và trượt tam giác]({{ site.baseurl }}/img/chapter_img/besicovitch_triangle_overlap.svg)

*Hình. Minh họa kinh điển: cắt một tam giác thành nhiều phần, trượt các phần để chúng chồng lên nhau nhiều hơn, rồi lặp lại.*

![Venetian blind]({{ site.baseurl }}/img/chapter_img/venetian_blinds_kakeya.svg)

*Hình. Sơ đồ kiểu rèm sáo (chỉ minh họa ý tưởng, không phải cách dựng đầy đủ).*

Năm 1971, **Roy Davies** chứng minh trên mặt phẳng 2 chiều: dù diện tích bằng $$0$$, mọi tập Kakeya đều có **chiều Hausdorff bằng 2** ($$\lvert E\rvert = 0$$ nhưng $$\dim_H(E) = 2$$).

![Measure và dimension]({{ site.baseurl }}/img/chapter_img/measure_vs_dimension.svg)

*Hình. Độ đo và số chiều là hai cách đo "kích thước" khác nhau.*

| Số chiều không gian | Tình trạng Giả thuyết Kakeya ($$\dim_H(K) = \dim_M(K) = n$$) |
|------------------|------------|
| $$n=1$$ | Hiển nhiên |
| $$n=2$$ | Đã chứng minh (Davies, 1971) |
| $$n=3$$ | Đã chứng minh (**Wang–Zahl**, 2025) |
| $$n\ge 4$$ | Còn mở (mới có các chặn dưới một phần) |

---

## 2. Khung giải thích: Wang và Zahl giải Giả thuyết Kakeya 3 chiều bằng 4 bước như thế nào? (nên đọc chậm)

Tại sao từ 2 chiều (Davies 1971) lên 3 chiều lại mất hơn nửa thế kỷ? Trên mặt phẳng, hai đường thẳng không song song *bắt buộc cắt nhau tại đúng một điểm*, nên chỉ cần bất đẳng thức Cauchy–Schwarz đơn giản là xong. Trong không gian 3 chiều, hàng triệu "sợi mì spaghetti" (ống $$\delta$$) có thể **chéo nhau không cắt**, bó chặt trong những tấm mỏng, hoặc xếp lên mặt cong hyperboloid một tầng (**regulus**)! Hãy đọc chậm 4 bước đột phá của **Hong Wang và Joshua Zahl** ([arXiv:2502.17655](https://arxiv.org/abs/2502.17655), 127 trang):

![δ-tube chồng lấp]({{ site.baseurl }}/img/chapter_img/kakeya_delta_tubes.svg)

*Hình. Nhiều ống $$\delta$$; những vùng các ống chồng lên nhau nhiều là nơi hình học trở nên phức tạp.*

#### Bước 1: Chuyển từ tập Kakeya sang ước lượng thể tích cho họ tập lồi tổng quát
Thay vì chỉ nhìn các ống $$\delta$$ cứng nhắc, Wang và Zahl phát biểu một định lý mạnh và linh hoạt hơn về **thể tích hợp của các tập lồi** trong $$\mathbb{R}^3$$: nếu một họ ống $$\delta$$ thỏa điều kiện **không tập trung bất thường** (không có quá nhiều ống bị nhét vào chung một tập lồi $$V$$ nào đó), thì hợp của chúng phải có thể tích gần lớn nhất có thể ($$\ge c_\varepsilon \delta^\varepsilon$$).

#### Bước 2: Phân tích cấu trúc đa thang — Dính (*sticky*), Hạt (*grainy*), Phẳng (*plany*)
Theo chương trình của Katz–Łaba–Tao (1999), nếu giả sử phản chứng có một họ ống $$\delta$$ có thể tích quá nhỏ (tức chồng lấp cực mạnh), thì khi phóng to ở các thang trung gian $$1 \to \rho \to \delta$$, các ống đó **không thể xếp hỗn loạn** mà buộc phải rơi vào những cấu trúc hình học cực kỳ đặc biệt: hoặc **dính** (các ống mảnh bó thành từng ống dày hơn ở thang $$\rho$$ — trường hợp Wang–Zahl đã giải riêng năm 2022 trên *JAMS* 2026, [arXiv:2210.09581](https://arxiv.org/abs/2210.09581)), hoặc tụ thành các "hạt" dẹt (*grainy* / *plany*).

#### Bước 3: Kỹ thuật tự cải thiện và Quy nạp đa thang
Đột phá quyết định của bài báo 2025 là nối khít mọi trường hợp (từ dính đến không dính) vào một cỗ máy **quy nạp theo thang**: nếu ở thang này các ống chồng lấp xấu (thể tích nhỏ), cấu trúc ẩn ép chúng phải tạo thành những cụm hình học mà khi nhìn ở thang lớn hơn (hoặc chiếu sang hướng khác), số ống trong một tập lồi $$V$$ bị vượt ngưỡng — dẫn đến **tự cải thiện** cận dưới thể tích!

$$
\text{Thể tích nhỏ ở thang } \delta
\;\Longrightarrow\;
\text{Cấu trúc dính / hạt / phẳng}
\;\Longrightarrow\;
\text{Tự cải thiện ở thang trung gian } \rho
\;\Longrightarrow\;
\text{Mâu thuẫn nếu } \dim < 3.
$$

#### Bước 4: Đóng trọn Giả thuyết Kakeya 3 chiều
<div class="textbook-theorem" markdown="1">
**Định lý (Wang–Zahl, 2025).**  
Mọi tập Kakeya $$K\subset\mathbb{R}^3$$ thỏa $$\dim_H(K) = \dim_M(K) = 3$$.
</div>

![Dòng thời gian]({{ site.baseurl }}/img/chapter_img/kakeya_history_timeline.svg)

*Hình. Một số mốc từ Kakeya (1917) đến Huy chương Fields của Wang (2026).*

---

## 3. Cầu nối Giải tích điều hòa và các công trình khác trong lời trích dẫn IMU

![Từ Kakeya đến harmonic analysis]({{ site.baseurl }}/img/chapter_img/kakeya_to_harmonic_analysis.svg)

*Hình. Chuỗi khái niệm từ hình học các ống đến giải tích Fourier và PDE.*

Lời trích dẫn Huy chương Fields 2026 của Hong Wang rộng hơn nhiều so với chỉ một bài báo Kakeya:

| Chủ đề | Cộng sự (chọn lọc) | Đóng góp chính |
|--------|--------------------------|----------------|
| **Làm trơn địa phương** (sóng trên mặt phẳng) | Larry Guth, Ruixiang Zhang | Dùng kỹ thuật đa thang và tách (*decoupling*) giải giả thuyết làm trơn địa phương trên mặt phẳng |
| **Tập khoảng cách Falconer** | Guth, Alex Iosevich, Yumeng Ou | Đột phá lớn liên hệ chiều Hausdorff với tập các khoảng cách |
| **Tập Furstenberg** (mặt phẳng) | Kevin Ren | Giải trọn giả thuyết Furstenberg trên mặt phẳng ([arXiv:2308.08819](https://arxiv.org/abs/2308.08819)): số chiều $$\ge \min\bigl(s+t,\frac{3s+t}{2},s+1\bigr)$$ |
| **Bài toán hạn chế Fourier** | nhiều cộng sự | Các tiến bộ sâu sắc cho chuỗi giả thuyết hạn chế |
| **Kakeya ba chiều** | Joshua Zahl | Trường hợp tập dính (JAMS 2026) và số chiều đầy đủ bằng 3 (arXiv:2502.17655) |

**Tiểu sử ngắn:** Hong Wang sinh tại Quế Lâm (Trung Quốc), học tại Đại học Bắc Kinh và École Polytechnique, làm tiến sĩ tại MIT dưới sự hướng dẫn của **Larry Guth**, sau đó công tác tại IAS, UCLA, rồi NYU Courant và IHES. Bà là **người phụ nữ thứ ba** nhận Huy chương Fields.

---

## Nhầm lẫn thường gặp

| Khẳng định | Kết luận | Sửa lại |
|------------|----------|---------|
| "Một mình Wang giải bài toán Kakeya ba chiều." | **Sai** | Đây là công trình chung với Joshua Zahl. |
| "Tập Kakeya ba chiều phải có thể tích dương." | **Sai** | Vẫn có tập độ đo bằng 0; định lý nói về **số chiều** bằng 3. |
| "Giải Fields chỉ vì bài toán Kakeya." | **Sai** | IMU còn nêu làm trơn địa phương, bài toán hạn chế, Falconer, Furstenberg. |
| "Chuyển động của chiếc kim chính là tập Besicovitch." | **Sai** | Một bên là **chuyển động liên tục**, một bên là **tập cố định** chứa mọi hướng. |
| "Bài toán Kakeya đã giải xong ở mọi số chiều." | **Sai** | Trường hợp $$n\ge 4$$ vẫn còn mở. |

---

## Ghi chú từ các video chính

*Phần này được viết lại từ phụ đề của các video trong bộ tài liệu (Quanta về Kakeya; Mathologer; video về chiều Hausdorff; video tiếng Việt). Nó không thay thế bài báo Wang–Zahl trên arXiv hay lời trích dẫn của IMU. Bản ghi lời: `research/video-research/Wang_Harmonic_Analysis/transcripts/`.*

- **C1. Chuyển động của chiếc kim và tập Kakeya:** "Xoay chiếc kim $$180^\circ$$" là bài toán chuyển động liên tục; giả thuyết tập Kakeya hiện đại nói về tập cố định chứa đoạn dài 1 theo mọi hướng.
- **C2. Độ đo bằng 0 và Chiều Hausdorff:** Độ đo bằng 0 **không** kéo theo số chiều bằng 0; số chiều đầy đủ **không** kéo theo độ đo Lebesgue dương.
- **C3. Video tiếng Việt & Tài liệu hỗ trợ:** Dùng để làm quen trực quan; luôn đối chiếu tên tác giả và mốc năm với arXiv và PDF của IMU trước khi trích dẫn. Xem `TRANSCRIPT_STATUS.md` và các tệp `*_knowledge_units.json`.

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
