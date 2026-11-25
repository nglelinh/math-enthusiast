---
layout: post
title: "Viazovska và Bài toán Xếp cầu (Huy chương Fields 2022)"
chapter: '02'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Nếu bạn đi qua một sạp bán cam, bạn sẽ thấy người bán luôn xếp cam theo từng lớp lục giác chồng so le lên nhau. Năm 1611, Johannes Kepler phỏng đoán rằng đó là cách xếp quả cầu đặc nhất có thể trong không gian 3 chiều — nhưng phải mất gần bốn thế kỷ (tới năm 1998), Thomas Hales mới chứng minh được điều ấy nhờ hàng trăm trang lập luận kết hợp với hàng nghìn giờ tính toán trên máy tính. Thế nên khi các nhà toán học hỏi tiếp: *"Vậy trong không gian 4 chiều, 8 chiều, hay 24 chiều thì xếp cầu thế nào là khít nhất?"*, ai cũng nghĩ bài toán sẽ còn khó gấp bội.

Rồi vào một ngày tháng 3 năm 2016, **Maryna Viazovska** đăng lên arXiv một bài báo chỉ dài hơn 20 trang, tinh tế đến mức khiến cả cộng đồng toán học sững sờ: không cần siêu máy tính kiểm tra hàng nghìn trường hợp, bà chứng minh trọn vẹn rằng lưới đối xứng **$$E_8$$** cho mật độ xếp cầu tối ưu tuyệt đối trong **8 chiều**! Chỉ một tuần sau, cùng bốn cộng sự (Cohn, Kumar, Miller, Radchenko), bà áp dụng cùng ý tưởng đó để giải luôn bài toán trong **24 chiều** với **lưới Leech**. Thành tựu rực rỡ này mang về cho Viazovska **Huy chương Fields 2022**, đưa bà trở thành **người phụ nữ thứ hai** trong lịch sử đoạt giải (sau Maryam Mirzakhani năm 2014).

Điều kỳ diệu nhất của câu chuyện nằm ở cú chuyển ngôn ngữ: thay vì xếp thử vô số quả cầu trong không gian 8 chiều, Viazovska đã dùng **dạng modular** — một công cụ tưởng chỉ sống trong lý thuyết số — để thiết kế một **"hàm kỳ diệu"** trong giải tích Fourier, tự động loại bỏ mọi đối thủ xếp cầu khác chỉ bằng một bất đẳng thức!

**Mạch bài học:** Kiến thức cần nhớ (tính tay mật độ 2D và đếm đủ 240 vectơ của $$E_8$$, công thức tổng Poisson, dạng modular) → Các chiều đã biết & từ đạn đại bác đến mã 5G → Giải thích 4 bước: chặn Cohn–Elkies và cách Viazovska thiết kế "hàm kỳ diệu" → Lưới Leech 24D & tính tối ưu phổ quát.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa mật độ xếp cầu và tự tính tay được mật độ trong 2 chiều (ô vuông $$78{,}5\%$$ vs lục giác $$90{,}7\%$$) cũng như số hôn $$240$$ và mật độ $$\pi^4/384$$ của lưới $$E_8$$ trong 8 chiều.
- Tự kiểm tra được 4 dòng chứng minh chặn trên **Cohn–Elkies** từ công thức tổng Poisson.
- Hiểu mạch 4 bước Viazovska dùng **dạng modular** và biến đổi Laplace để xây dựng **hàm kỳ diệu** có không điểm kép đúng tại $$\sqrt{2}, \sqrt{4}, \sqrt{6}, \dots$$
- Phân biệt định lý cho $$E_8$$ (Viazovska một mình) và định lý cho lưới Leech (công trình chung CKMRV).
- Kể lại sơ lược cầu nối từ chồng đạn đại bác của Kepler đến mã sửa lỗi nhiều chiều mà không đánh đồng với nội dung lời trích dẫn giải Fields.

**Kiến thức cần có.** Thể tích hình tròn/quả cầu, lưới trong $$\mathbb{R}^n$, và khái niệm biến đổi Fourier. Mọi phép tính chính đều được viết tường minh ngay bên dưới.

---

## Kiến thức cần nhớ: Hình học rời rạc, Lưới $$E_8$$ và Giải tích Fourier

### 1. Xếp cầu và Mật độ — Tính tay từ 2 chiều lên 8 chiều!
Xếp các quả cầu đồng nhất bán kính $$r$$ không chồng lên nhau trong $$\mathbb{R}^n$$. Với một **lưới** $$\Lambda$$, mỗi ô cơ sở có thể tích $$\operatorname{Vol}(\mathbb{R}^n/\Lambda)$$ chứa đúng một quả cầu, nên mật độ là $$\delta = \frac{\operatorname{Vol}(B_r)}{\operatorname{Vol}(\mathbb{R}^n/\Lambda)}$$.

- **Trong 2 chiều (đĩa tròn):**
  - *Lưới ô vuông* $$\mathbb{Z}^2$$: khoảng cách ngắn nhất bằng $$1 \implies r = 1/2$$, diện tích ô vuông $$= 1$. Mật độ: $$\delta_{\text{vuông}} = \pi (1/2)^2 = \frac{\pi}{4} \approx \mathbf{78{,}54\%}$$.
  - *Lưới lục giác (tổ ong)*: các tâm là đỉnh tam giác đều cạnh $$1 \implies r = 1/2$$, ô cơ sở là hình thoi diện tích $$\frac{\sqrt{3}}{2}$$. Mật độ: $$\delta_{\text{lục giác}} = \frac{\pi / 4}{\sqrt{3}/2} = \frac{\pi}{2\sqrt{3}} \approx \mathbf{90{,}69\%}$$ (tối ưu trong 2 chiều!).
- **Trong 8 chiều — Tự tay đếm 240 hàng xóm và tính mật độ của lưới $$E_8$$:**
  Lưới $$E_8 \subset \mathbb{R}^8$$ được định nghĩa cực kỳ gọn: gồm mọi điểm $$(x_1, \dots, x_8) \in \mathbb{R}^8$$ có tọa độ **hoặc đều nguyên, hoặc đều bán nguyên** (dạng $$k + \frac{1}{2}$$), sao cho **tổng 8 tọa độ là số chẵn**!
  - Bình phương độ dài ngắn nhất khác 0 là $$\|x\|^2 = 2$$ (tức độ dài $$\sqrt{2}$$). Hãy tự đếm xem có bao nhiêu vectơ như thế:
    1. *Tọa độ nguyên:* chọn 2 vị trí mang $$\pm 1$$, 6 vị trí còn lại bằng $$0$$ (tổng luôn chẵn) → $$\binom{8}{2} \times 2^2 = 28 \times 4 = \mathbf{112}$$ vectơ.
    2. *Tọa độ bán nguyên:* cả 8 tọa độ là $$\pm \frac{1}{2}$$ (bình phương tổng đúng bằng $$8 \times \frac{1}{4} = 2$$!), và tổng là số chẵn khi số dấu trừ là chẵn → $$2^8 / 2 = \mathbf{128}$$ vectơ.
    - **Tổng cộng:** $$112 + 128 = \mathbf{240}$$ vectơ ngắn nhất! Nghĩa là mỗi quả cầu trong $$E_8$$ chạm khít đồng thời **240** quả cầu hàng xóm!
  - Khoảng cách ngắn nhất là $$\sqrt{2} \implies$$ bán kính mỗi cầu $$r = \frac{\sqrt{2}}{2}$$. Vì $$E_8$$ có thể tích ô cơ sở đúng bằng $$1$$ và thể tích quả cầu 8D bán kính $$r$$ là $$\frac{\pi^4}{4!} r^8$$, ta tính ngay mật độ:

$$
\delta_{E_8} \;=\; \frac{\pi^4}{24} \left(\frac{\sqrt{2}}{2}\right)^8 \;=\; \frac{\pi^4}{24 \cdot 16} \;=\; \frac{\pi^4}{384} \;\approx\; \mathbf{25{,}37\%}.
$$

### 2. Giải tích Fourier và Công thức tổng Poisson
Biến đổi Fourier $$\hat{f}(\xi) = \int_{\mathbb{R}^n} f(x) e^{-2\pi i x \cdot \xi}\,dx$$ phân tích hàm $$f$$ theo tần số. **Công thức tổng Poisson** nối tổng của $$f$$ trên lưới $$\Lambda$$ với tổng của $$\hat{f}$$ trên lưới đối ngẫu $$\Lambda^*$$:

$$
\sum_{x \in \Lambda} f(x) \;=\; \frac{1}{\operatorname{Vol}(\mathbb{R}^n/\Lambda)} \sum_{\xi \in \Lambda^*} \hat{f}(\xi).
$$

### 3. Dạng modular (Modular Forms) — Vũ khí bất ngờ từ lý thuyết số
Dạng modular là những hàm giải tích sống trên nửa mặt phẳng phức trên $$\mathbb{H}$$, thỏa mãn những phương trình đối xứng cực mạnh dưới phép biến đổi $$\tau \mapsto \tau + 1$$ và $$\tau \mapsto -1/\tau$$ (như chuỗi Eisenstein $$E_4(\tau), E_6(\tau)$$ và hàm $$\Delta(\tau)$$). Vì bị khóa bởi quá nhiều đối xứng, không gian các dạng modular rất nhỏ và cứng — biến chúng thành "xưởng đúc" lý tưởng để tạo ra hàm Fourier có không điểm chính xác tại các khoảng cách của lưới $$E_8$$!

---

## 1. Đã biết gì về các chiều thấp và bài toán xếp cầu?

![Xếp lục giác]({{ site.baseurl }}/img/chapter_img/viazovska_packing_2d.svg)

*Hình. Cách xếp lục giác trên mặt phẳng, cách xếp tối ưu cổ điển trong 2 chiều.*

| Số chiều | Tình trạng |
|-------|------------|
| $$n=1$$ | Hiển nhiên (các đoạn thẳng nối khít trên đường thẳng, mật độ $$100\%$$) |
| $$n=2$$ | Lưới lục giác ($$\pi/\sqrt{12} \approx 90{,}7\%$$), kết quả cổ điển (Thue, Fejes Tóth) |
| $$n=3$$ | FCC / HCP ($$\pi/\sqrt{18} \approx 74{,}05\%$$): giả thuyết Kepler, Hales (cùng kiểm chứng hình thức) |
| $$n=8$$ | $$E_8$$ ($$\pi^4/384 \approx 25{,}37\%$$): **Viazovska (2016)** |
| $$n=24$$ | Leech ($$\pi^{12}/12! \approx 0{,}193\%$$): **Cohn–Kumar–Miller–Radchenko–Viazovska** |
| $$n$$ tổng quát | Phần lớn còn mở (kể cả chiều 4, 5, 6, 7!); đã có các chặn tiệm cận |

### Từ đạn đại bác đến chuỗi bit (theo lời kể của Tao)

Trong [cuộc trò chuyện với Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) cho loạt *Six Math Essentials*, Terence Tao kể về bài toán xếp cầu như một ví dụ tiêu biểu cho chặng đường từ sự tò mò thuần túy đến công nghệ hiện đại. Từ câu hỏi chất đạn đại bác trên tàu thủy của Kepler đến chứng minh có máy tính hỗ trợ của Hales năm 1998, các nhà toán học hỏi tiếp về xếp cầu trong không gian nhiều chiều và trong không gian *rời rạc* gồm các chuỗi bit.

Khi điện thoại gửi tín hiệu số, mỗi thông điệp là một chuỗi bit. Ta muốn các tín hiệu hợp lệ nằm cách đủ xa nhau trong khối lập phương nhiều chiều để nhiễu không làm nhầm lẫn tín hiệu — đó chính là bài toán xếp cầu rời rạc (**mã sửa lỗi**), quyết định giới hạn lý thuyết cho số bit mỗi giây qua một dải tần vô tuyến. Tuy nhiên cần tách bạch: công trình được giải Fields của Viazovska là xếp cầu trong không gian Euclid **liên tục** 8 và 24 chiều, không phải thiết kế mạng 5G. Xem thêm: [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/); bài thực hành: [Khám phá xếp cầu]({{ site.baseurl }}/contents/vi/chapter07/07_03_Explore_Sphere_Packing/).

---

### Video ngắn: Xếp đĩa tròn trong mặt phẳng

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/disc-packing-2d_vi.mp4"></video>
</div>

Trong mặt phẳng, lưới ô vuông phủ khoảng 78,5 phần trăm còn cách xếp tổ ong phủ khoảng 90,7 phần trăm, là mật độ tối ưu trong hai chiều.

---

## 2. Lưới $$E_8$$ và Lưới Leech $$\Lambda_{24}$$

![E8 và Leech]({{ site.baseurl }}/img/chapter_img/viazovska_e8_leech.svg)

*Hình. Hai lưới đặc biệt mà Viazovska và các cộng sự đã chứng minh là tối ưu.*

- **Lưới $$E_8 \subset \mathbb{R}^8$$:** lưới unimodular chẵn duy nhất trong 8 chiều, tự đối ngẫu ($$E_8^* = E_8$$), có 240 vectơ ngắn nhất độ dài $$\sqrt{2}$$ và nhóm đối xứng gần 700 triệu phần tử.
- **Lưới Leech $$\Lambda_{24} \subset \mathbb{R}^{24}$$:** lưới unimodular chẵn duy nhất trong 24 chiều *không có vectơ độ dài $$\sqrt{2}$$*; các vectơ ngắn nhất có độ dài $$2$$ và có tới **196.560** vectơ như thế!

**Lưu ý.** Tối ưu trong lớp các lưới **không** tự động là tối ưu toàn cục (một cấu hình không tuần hoàn có thể xếp khít hơn mọi lưới). Định lý Viazovska / CKMRV loại trừ *mọi* cấu hình, kể cả không tuần hoàn!

---

## 3. Giải thích: Dạng modular đã "khóa chết" bài toán xếp cầu 8 chiều như thế nào?

Tại sao một chứng minh dài chỉ hơn 20 trang lại loại trừ được *vô hạn* mọi cách xếp cầu có thể trong 8 chiều? Hãy đọc chậm 4 bước cực kỳ trong sáng dưới đây:

![Ý tưởng Cohn–Elkies]({{ site.baseurl }}/img/chapter_img/viazovska_cohn_elkies.svg)

*Hình. Các điều kiện về dấu trên $$f$$ và $$\hat f$$ cho ta một chặn trên cho bài toán xếp cầu.*

#### Bước 1: Chứng minh 4 dòng cho Chặn Cohn–Elkies (2003)
Giả sử ta tìm được một hàm xuyên tâm (chỉ phụ thuộc bán kính $$\|x\|$$) thuộc lớp Schwartz $$f: \mathbb{R}^n \to \mathbb{R}$$ thỏa mãn đúng 3 điều kiện:
1. $$f(0) = \hat{f}(0) = 1$$;
2. $$f(x) \le 0$$ với mọi $$\|x\| \ge r$$;
3. $$\hat{f}(\xi) \ge 0$$ với mọi $$\xi \in \mathbb{R}^n$$.

Lấy một lưới xếp cầu bất kỳ $$\Lambda$$ có khoảng cách ngắn nhất $$\ge r$$ (bán kính quả cầu $$r/2$$). Áp dụng **Công thức tổng Poisson** ngay lập tức cho ta:

$$
1 \;=\; f(0) \;\ge\; \underbrace{f(0) + \sum_{x \in \Lambda \setminus \{0\}} f(x)}_{\text{vì } f(x) \le 0 \text{ khi } \|x\| \ge r} \;=\; \frac{1}{\operatorname{Vol}(\mathbb{R}^n/\Lambda)} \underbrace{\left(\hat{f}(0) + \sum_{\xi \in \Lambda^* \setminus \{0\}} \hat{f}(\xi)\right)}_{\ge\, \hat{f}(0)\, =\, 1 \text{ vì } \hat{f} \ge 0} \;\ge\; \frac{1}{\operatorname{Vol}(\mathbb{R}^n/\Lambda)}.
$$

Suy ra $$\operatorname{Vol}(\mathbb{R}^n/\Lambda) \ge 1$$ — nghĩa là mật độ của **mọi** cách xếp (kể cả không phải lưới, dùng phép lấy trung bình!) đều bị chặn trên bởi $$\operatorname{Vol}(B_{r/2})$$!

#### Bước 2: Yêu cầu cực ngặt của "Hàm kỳ diệu" (*Magic Function*)
Để chặn trên này **khớp tuyệt đối** với mật độ của $$E_8$$ (nơi $$r = \sqrt{2}$$ và $$\operatorname{Vol}(\mathbb{R}^8/E_8) = 1$$), cả hai dấu $$\ge$$ ở Bước 1 phải đồng thời trở thành **dấu bằng**! Điều đó ép buộc:
- $$f(x) = 0$$ tại mọi điểm khác 0 của $$E_8$$ (tức tại mọi bán kính $$\sqrt{2}, \sqrt{4}, \sqrt{6}, \sqrt{8}, \dots$$), và vì $$f(x) \le 0$$ với $$\|x\| \ge \sqrt{2}$$, chúng phải là **không điểm kép** (đồ thị chỉ chạm trục hoành chứ không cắt qua) tại $$\sqrt{4}, \sqrt{6}, \dots$$!
- $$\hat{f}(\xi) = 0$$ cũng phải có **không điểm kép** tại đúng các bán kính $$\sqrt{2}, \sqrt{4}, \sqrt{6}, \dots$$ (vì $$E_8^* = E_8$$)!

Hơn 10 năm trời, máy tính xác nhận chặn Cohn–Elkies khớp mật độ $$E_8$$ tới 30 chữ số thập phân, nhưng không ai viết ra được công thức của hàm kỳ diệu $$f$$.

#### Bước 3: Cú xoay chuyển của Viazovska — Tách trị riêng Fourier $$\pm 1$$ và dùng Dạng modular
Viazovska tách $$f = \frac{1}{2}(a + b)$$, trong đó $$a$$ là **hàm riêng $$+1$$** ($$\hat{a} = +a$$) và $$b$$ là **hàm riêng $$-1$$** ($$\hat{b} = -b$$). Nhờ hệ số $$\sin^2\bigl(\frac{\pi}{2}\|x\|^2\bigr)$$ tự động sinh ra không điểm kép tại mọi $$\sqrt{2k}$$ ($$k \ge 1$$), bà đặt dạng thử bằng **biến đổi Laplace** trên nửa mặt phẳng trên:

$$
a(x) \;=\; \sin^2\!\left(\frac{\pi \|x\|^2}{2}\right) \int_0^\infty \phi(it)\, e^{-\pi \|x\|^2 t}\, dt.
$$

Điều kỳ diệu xảy ra: điều kiện $$\hat{a} = +a$$ và $$\hat{b} = -b$$ biến đổi chính xác thành **phương trình biến đổi modular** cho hàm $$\phi(\tau)$$! Và vì không gian các dạng gần modular (sinh bởi $$E_2, E_4, E_6$$ và $$\Delta$$) có số chiều cực nhỏ, Viazovska viết ra **công thức tường minh duy nhất** cho $$\phi(\tau)$$ và kiểm tra chặt chẽ các điều kiện dấu bằng giải tích thuần túy!

#### Bước 4: Định lý tối ưu cho 8D, 24D và Tính tối ưu phổ quát
<div class="textbook-theorem" markdown="1">
**Định lý (Viazovska, 2016/2017; và CKMRV cho 24 chiều).**  
Lưới $$E_8$$ đạt mật độ xếp cầu lớn nhất trong **mọi** cách xếp trong $$\mathbb{R}^8$$; lưới Leech $$\Lambda_{24}$$ đạt mật độ lớn nhất trong **mọi** cách xếp trong $$\mathbb{R}^{24}$$.
</div>

Sau đó, nhóm CKMRV còn đẩy kỹ thuật này lên đỉnh cao mới: chứng minh **tính tối ưu phổ quát** (*universal optimality*) — $$E_8$$ và lưới Leech cực tiểu hóa năng lượng của hệ điểm dưới *mọi* hàm thế tương tác hoàn toàn đơn điệu, đồng thời sinh ra **công thức nội suy Fourier** (Radchenko–Viazovska).

Tóm tắt mạch chứng minh:

$$
\text{Xếp cầu trong } \mathbb{R}^8
\;\xrightarrow{\text{Poisson + Cohn–Elkies}}\;
\text{Hàm kỳ diệu } f, \hat{f}
\;\xrightarrow{\text{Biến đổi Laplace}}\;
\text{Dạng modular } (E_2, E_4, E_6, \Delta)
\;\Longrightarrow\;
E_8 \text{ tối ưu tuyệt đối}.
$$

---

## 4. Ghi nhận công lao và điều nghịch lý

- **Chiều 8:** Maryna Viazovska (một mình — bài báo mốc năm 2016, *Annals of Mathematics* 2017).
- **Chiều 24:** công trình hợp tác **Cohn–Kumar–Miller–Radchenko–Viazovska** (CKMRV).
- Bà là **người phụ nữ thứ hai** nhận Huy chương Fields (2022).

**Nghịch lý đáng nhớ:** Quy luật "số chiều càng cao càng khó" bị phá vỡ ngoạn mục ở chiều 8 và 24 — ta vẫn chưa giải nổi chiều 4 hay chiều 5, nhưng lại có chứng minh giải tích tuyệt đối ngắn gọn cho chiều 8 và 24 nhờ tính đối xứng ngoại lệ của $$E_8$$ và Leech! (Lưu ý: **số hôn** — số quả cầu chạm 1 quả cầu, bằng 240 ở 8D và 196.560 ở 24D — có liên hệ nhưng *khác* với mật độ xếp cầu toàn không gian.)

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|---------|
| "Bài toán xếp cầu đã giải xong cho mọi số chiều." | **Sai** | Chỉ biết lời giải tối ưu chính xác ở chiều 1, 2, 3, 8 và 24. |
| "Tính tối ưu của $$E_8$$ chỉ là một con số gần đúng." | **Sai** | Đó là một định lý giải tích chính xác tuyệt đối. |
| "Một mình Viazovska chứng minh cho lưới Leech." | **Sai** | Trường hợp 24 chiều là công trình hợp tác CKMRV. |
| "Tối ưu trong lớp lưới thì tự động tối ưu toàn cục." | **Sai** | Nói chung cấu hình không phải lưới có thể tốt hơn; định lý loại trừ điều đó trong 8 và 24 chiều. |
| "Chỉ là chuyện hệ nghiệm, không có giải tích." | **Sai** | Giải tích Fourier và dạng modular là công cụ quyết định. |

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Chi tiết: `research/video-research/Viazovska_Sphere_Packing/`.

**Thứ tự xem gợi ý**

1. Bài viết năm 2016 của Quanta về xếp cầu: [link](https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/).  
2. Bài giảng Einstein của Viazovska: [YouTube](https://www.youtube.com/watch?v=fH6KNlUJux0).  
3. Hội thảo Breakthrough: [YouTube](https://www.youtube.com/watch?v=VCZeVsTb7DU).  
4. arXiv:1603.04246.

**Nhắc lại:** lời giải tối ưu đã biết cho các chiều 1, 2, 3, 8, 24, không phải mọi số chiều.

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Viazovska_Sphere_Packing/transcripts/` · trạng thái: `research/video-research/Viazovska_Sphere_Packing/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Viazovska_Sphere_Packing_fH6KNlUJux0_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Viazovska_Sphere_Packing/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=fH6KNlUJux0  
2. https://www.youtube.com/watch?v=VCZeVsTb7DU  
3. https://www.youtube.com/watch?v=qr6ZbYancMY  
4. https://arxiv.org/abs/1603.04246  
5. https://arxiv.org/pdf/1603.04246  
6. https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/laudatio-mv.pdf  
7. https://www.quantamagazine.org/sphere-packing-solved-in-higher-dimensions-20160330/  
8. https://en.wikipedia.org/wiki/Sphere_packing  
9. https://en.wikipedia.org/wiki/Maryna_Viazovska  
10. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022  
11. https://www.math.inc/sphere-packing  
12. https://en.wikipedia.org/wiki/E8_lattice  
13. https://en.wikipedia.org/wiki/Leech_lattice  
14. https://www.youtube.com/watch?v=OOMx2BHHWtE  

### Bộ tư liệu nghiên cứu

14. Bộ tư liệu của khóa học: `research/video-research/Viazovska_Sphere_Packing/`.

1. **M. Viazovska** (2017), *Annals of Mathematics* — 8 chiều.  
2. **Cohn–Kumar–Miller–Radchenko–Viazovska**, *Annals* — 24 chiều.  
3. **Cohn & Elkies** — chặn bằng quy hoạch tuyến tính.  
4. Các bài tổng quan / Quanta — trực giác phổ thông.  
5. IMU, Huy chương Fields 2022 — Viazovska.  
6. Conway–Sloane — kiến thức cổ điển về lưới.

---

## Hướng đi tiếp

- Tìm hiểu tính tối ưu phổ quát và bài toán cực tiểu năng lượng.  
- Học nhập môn về dạng modular dành cho người làm giải tích.  
- So sánh với Maynard và Green–Tao: cấu trúc đặc biệt kết hợp giải tích mạnh.  
- Ghi lại một câu hỏi cụ thể bạn vẫn còn thắc mắc, ví dụ "vì sao dạng modular tạo ra đúng các không điểm của $$f$$?"  
- Đọc song song bài [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) về một nữ chủ nhân khác của giải Fields, và bài [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) về cấu trúc trong không gian thưa / rời rạc.

## Video tham khảo

- **Xem trước:** [Einstein Lectures: Maryna Viazovska - The sphere packing problem](https://www.youtube.com/watch?v=fH6KNlUJux0) — Universität Bern, tiếng Anh. Viazovska giới thiệu bài toán xếp cầu cho khán giả rộng; nên xem trước khi đọc bài.
- [Maryna Viazovska: 2018 Breakthrough Prize Symposium](https://www.youtube.com/watch?v=VCZeVsTb7DU) — Breakthrough, tiếng Anh. Bài nói của Viazovska tại hội thảo Breakthrough; nên xem sau khi đã nắm ý chính của bài.
- [What is...sphere packing?](https://www.youtube.com/watch?v=qr6ZbYancMY) — VisualMath, tiếng Anh. Xem thêm sau hai video trên; giới thiệu ngắn về khái niệm xếp cầu.
