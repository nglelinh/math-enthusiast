---
layout: post
title: "Từ hình học không–thời gian đến hấp dẫn"
chapter: '03'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
---

Newton xem hấp dẫn là một lực tác dụng xuyên qua một không gian tuyệt đối, với một thời gian chung cho mọi nơi. **Thuyết tương đối rộng (GR)** của Einstein thay bức tranh đó bằng một cơ chế hình học: vật chất và năng lượng làm cong không – thời gian, và một vật rơi tự do chuyển động theo đường trắc địa (geodesic) của một metric. Khái niệm "lực hấp dẫn" được hiểu lại bằng hình học.

Bài này là bản đồ ở bậc đại học cho cơ chế đó, không phải một giáo trình GR. Bạn sẽ gặp metric, ý tưởng về độ cong, phương trình Einstein như một phương trình đạo hàm riêng nối hình học với tensor năng lượng – xung lượng, và một bảng phân biệt đâu là định lý, đâu là vật lý chuẩn, đâu là hình ảnh ví von phổ biến. Bài cũng chuẩn bị trực giác hình học sẽ được dùng lại trong [lý thuyết gauge]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/): **vật lý là các trường trên một nền hình học**, và độ cong mô tả tương tác.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu ý chính của **nguyên lý tương đương** và giải thích vì sao nó dẫn đến việc thay lực hấp dẫn bằng hình học của chuyển động rơi tự do.
- Giải thích metric $$g_{\mu\nu}$$ chứa những thông tin gì (khoảng cách, góc, cấu trúc nhân quả; ở mức ý tưởng).
- Phân biệt **thuyết tương đối hẹp** (không – thời gian Minkowski phẳng) và **thuyết tương đối rộng** (không – thời gian cong và thay đổi theo vật chất).
- Viết phương trình Einstein dạng sơ lược $$\mathrm{Ric}-\tfrac12 Rg=8\pi T$$ và nói mỗi vế biểu diễn điều gì.
- Trình bày **chuỗi lập luận ngắn** từ hình học đến một dự đoán (ánh sáng bị lệch, giãn thời gian do hấp dẫn) mà không cần tính toán tensor đầy đủ.
- Tránh các cách nói sai: "mọi thứ đều tương đối", "GR chỉ là chuyện viễn tưởng về lỗ đen", "không gian cong nghĩa là một bề mặt nằm trong không gian lớn hơn mà ta luôn nhìn thấy được".

**Kiến thức nền.** Giải tích nhiều biến; đại số tuyến tính (tích vô hướng). Tùy chọn: [Giải tích → Vật lý]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/).

---

## 1. Thuyết tương đối hẹp là hình học phẳng

**Không – thời gian Minkowski** là $$\mathbb{R}^4$$ với một tích vô hướng không xác định dấu (quy ước về dấu có thể khác nhau giữa các sách)

$$
ds^2 = -c^2\,dt^2 + dx^2 + dy^2 + dz^2.
$$

Khoảng không – thời gian, nón ánh sáng và việc tốc độ ánh sáng không đổi đều là các khái niệm hình học. Phép biến đổi Lorentz là phép đẳng cự tuyến tính của metric này. Ở đây **chưa có hấp dẫn**: không – thời gian chỉ là một sân khấu cố định.

**Hiểu đúng.** "Tương đối" có nghĩa là các định luật **có cùng dạng dưới một nhóm đối xứng xác định**, cùng với cách định nghĩa thời gian và độ dài bằng phép đo. Nó không có nghĩa là "muốn hiểu sao cũng được".

---

## 2. Từ nguyên lý tương đương đến không – thời gian cong

Phát biểu đơn giản: trong một phòng thí nghiệm nhỏ đang rơi tự do, không thể phân biệt hấp dẫn tại chỗ với trạng thái không có hấp dẫn (trừ hiệu ứng thủy triều). Einstein biến điều này thành nguyên lý xây dựng lý thuyết: **hấp dẫn không phải là một trường lực trên một sân khấu cứng; chính sân khấu có hình học, và vật rơi tự do đi theo hình học đó.**

Lực thủy triều, tức là gia tốc tương đối giữa các quỹ đạo rơi tự do gần nhau, trở thành **độ cong**. Nếu có thể "làm thẳng" mọi quỹ đạo rơi tự do cùng lúc ở khắp nơi, thì độ cong bằng không và ta quay về thuyết tương đối hẹp.

---

## 3. Metric, đường trắc địa, độ cong (các định nghĩa cơ bản)

**Metric Lorentz** $$g$$ gán cho mỗi sự kiện một tích vô hướng trên các vectơ tiếp xúc, với dấu $$(-,+,+,+)$$ (hoặc ngược lại). Thời gian riêng dọc theo một đường thế giới kiểu thời gian $$\gamma$$ về cơ bản là

$$
\tau = \int \sqrt{-g(\dot\gamma,\dot\gamma)}\,dt
$$

(sai khác hằng số và cách tham số hóa). **Đường trắc địa** là đường làm cực trị thời gian riêng (tương đương: thỏa mãn phương trình trắc địa với các ký hiệu Christoffel tính từ $$g$$ và $$\partial g$$).

**Các tensor độ cong** (Riemann, Ricci, độ cong vô hướng $$R$$) đo mức độ không giao hoán của đạo hàm hiệp biến bậc hai, và mức độ một chùm đường trắc địa bị méo về thể tích. Không cần tính từng thành phần; chỉ cần nhớ ý chính:

> **Vật chất cho không – thời gian biết phải cong như thế nào; không – thời gian cong cho vật chất biết phải chuyển động như thế nào.**

---

## 4. Phương trình Einstein là một phương trình trường

Dạng sơ lược:

$$
G_{\mu\nu} := R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu},
$$

trong đó $$G_{\mu\nu}$$ là tensor Einstein, được xây dựng từ độ cong của metric, và $$T_{\mu\nu}$$ là **tensor năng lượng – xung lượng** của vật chất và các trường không phải hấp dẫn.

| Vế | Ý nghĩa |
|----|---------|
| Trái | Hoàn toàn là hình học |
| Phải | Năng lượng, động lượng, áp suất, ứng suất của vật chất |

Trong chân không ($$T=0$$), ta nghiên cứu các metric có tensor Ricci bằng không; nghiệm lỗ đen Schwarzschild và Kerr thuộc loại này.

**Là một PDE.** Phương trình Einstein là một hệ phương trình đạo hàm riêng phi tuyến cho metric. Tính đặt chỉnh của bài toán Cauchy, tính ổn định của lỗ đen, giả thuyết kiểm duyệt vũ trụ là các chương trình nghiên cứu toán học về GR; một số đã có tiến bộ lớn gần đây, một số vẫn còn mở.

---

## 5. Từ hình học đến quan sát, mỗi hiện tượng một bước

**Giãn thời gian do hấp dẫn.** Đồng hồ nằm sâu trong giếng thế hấp dẫn chạy chậm hơn so với người quan sát ở xa (hệ thống GPS phải hiệu chỉnh hiệu ứng này, cùng với hiệu ứng của thuyết tương đối hẹp).

**Ánh sáng bị lệch, thấu kính hấp dẫn.** Đường trắc địa của ánh sáng (đường trắc địa không) bị uốn cong khi đi gần một khối lượng lớn.

**Sóng hấp dẫn.** Những nhiễu động nhỏ (tuyến tính hóa) của metric lan truyền với tốc độ $$c$$; LIGO/Virgo đo độ biến dạng (strain) do các vụ sáp nhập ở rất xa gây ra.

**Vũ trụ học.** Với metric đồng nhất và đẳng hướng (FLRW), phương trình Einstein rút gọn thành các ODE cho hệ số tỉ lệ $$a(t)$$.

Mỗi mục trên là một **cơ chế** đi từ hình học đến một đại lượng quan sát được, không phải một danh sách từ khóa.

---

## 6. Toán học nhận lại được gì

| Chủ đề toán học | Liên hệ với GR |
|-------------|-------------|
| Hình học Riemann và hình học Lorentz | Metric, độ cong, đường trắc địa |
| Giải tích toàn cục và cấu trúc nhân quả | Miền phụ thuộc, các định lý kỳ dị Penrose–Hawking |
| PDE hyperbolic phi tuyến | Tính đặt chỉnh địa phương của phương trình tiến hóa Einstein |
| Tôpô vi phân | Tôpô của chân trời sự kiện, định lý khối lượng dương |
| Giải tích hình học | Tính ổn định của nghiệm Kerr, sóng phi tuyến trên nền lỗ đen |

GR vừa là một **ứng dụng của hình học làm thay đổi vật lý**, vừa **sinh ra những chương trình nghiên cứu toán học thuần túy**. Đây chính là vai trò hai chiều mà Chương 3 muốn nhấn mạnh.

---

## 7. Phân biệt chính xác và cường điệu

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Einstein chứng minh mọi thứ đều tương đối." | Gây hiểu nhầm | Vẫn có những cấu trúc tuyệt đối (quan hệ nhân quả, tốc độ $$c$$, các đại lượng vô hướng của độ cong). |
| "Không gian cong giống một quả bóng nhìn từ bên ngoài." | Chỉ là hình ảnh ví von | Độ cong của không – thời gian là tính chất nội tại, không cần không gian bên ngoài. |
| "Lỗ đen phá vỡ vật lý." | Nói quá | Lỗ đen là nghiệm, là vùng trong GR (còn các câu hỏi lượng tử ở chân trời sự kiện là một hướng nghiên cứu riêng). |
| "GR và cơ học lượng tử đã được thống nhất." | Sai | Đã có lý thuyết bán cổ điển (trường lượng tử trên nền không – thời gian cong); lý thuyết hấp dẫn lượng tử đầy đủ vẫn còn mở. |
| "GPS chạy được nên phương trình Einstein đã được hiểu hết với tư cách PDE." | Nhầm phạm trù | Công nghệ dùng các hiệu chỉnh của GR; lý thuyết toàn cục của GR vẫn còn các bài toán mở. |

---

## Bài tập

1. **So sánh.** Viết không quá 100 từ so sánh lực hấp dẫn của Newton với chuyển động rơi tự do theo hình học của Einstein.  
2. **Ý nghĩa của metric.** $$ds^2$$ cho ta biết điều gì mà việc xét riêng "ba khoảng cách và một thời gian" không cho?  
3. **Phương trình Einstein.** Trong $$G_{\mu\nu}=8\pi T_{\mu\nu}$$ (bỏ qua hằng số), mỗi ký hiệu thuộc về hình học hay vật chất?  
4. **Cơ chế.** Giải thích việc hiệu chỉnh thời gian trong GPS như một hiệu ứng của GR, không quá 80 từ.  
5. **Cầu nối.** Viết một đoạn: "độ cong của liên thông" trong lý thuyết gauge giống và khác "độ cong của metric" trong GR như thế nào?  
6. **Sửa câu sai.** Sửa câu: "Thuyết tương đối nói rằng không có sự thật, chỉ có quan điểm."

---

## Tài liệu tham khảo

1. Hartle — *Gravity*.  
2. Carroll — *Spacetime and Geometry*.  
3. Khóa học: [Giải tích → Vật lý]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/).  
