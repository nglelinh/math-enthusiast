---
layout: post
title: "Chuyển pha của Duminil-Copin (Huy chương Fields 2022)"
chapter: '02'
order: 19
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy nghĩ về một thanh nam châm sắt quen thuộc. Khi bạn nung nóng nó dần lên, từ tính yếu đi từng chút một; rồi đúng tại một ngưỡng nhiệt độ sắc như lưỡi dao (nhiệt độ Curie, khoảng $$770^\circ\text{C}$$), từ tính biến mất hoàn toàn. Hoặc hình dung nước thấm qua một tảng đá xốp: chỉ cần mật độ khe hở vượt qua một ngưỡng nhỏ, nước bỗng tìm được đường chảy xuyên suốt cả tảng đá. Những bước ngoặt đột ngột ở thang vĩ mô sinh ra từ vô số tương tác vi mô ngẫu nhiên như vậy gọi là **chuyển pha** (*phase transitions*).

Trong suốt nhiều thập niên, toán học về chuyển pha mắc kẹt trong một nghịch lý kỳ lạ: ở **chiều hai**, ta có lời giải chính xác của Onsager cùng bộ máy bất biến bảo giác rực rỡ của [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) và [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/); ở **chiều cao** ($$d \ge 5$$), các đường tương tác hiếm khi va vào nhau nên lý thuyết trường trung bình hoạt động trơn tru. Nhưng đúng hai số chiều mà tự nhiên thực sự sống trong đó — **chiều ba** (không gian của nam châm và chất lỏng) và **chiều bốn** (không-thời gian của lý thuyết trường lượng tử) — lại là vùng tối đầy những câu hỏi mở từ thập niên 1970–1980.

Năm 2022, **Hugo Duminil-Copin** nhận **Huy chương Fields** nhờ *"giải quyết những bài toán tồn tại lâu trong lý thuyết xác suất về **chuyển pha** trong vật lý thống kê, đặc biệt ở chiều **ba** và **bốn**."* Cùng các cộng sự, ông chứng minh **tính liên tục** và **tính sắc** của chuyển pha cho các mô hình kiểu Ising ba chiều; cùng **Michael Aizenman**, ông chứng minh mô hình Ising bốn chiều tuân theo **trường trung bình** và lý thuyết trường lượng tử vô hướng Euclid bốn chiều là **tầm thường** (*trivial*); và ở chiều hai, ông cùng cộng sự phân loại hoàn chỉnh chuyển pha liên tục/gián đoạn của mô hình cụm ngẫu nhiên **Fortuin–Kasteleyn (FK)**, chứng minh tính phổ quát trên đồ thị đẳng bán kính và **tính bất biến dưới phép quay** ở thang lớn. Dù là học trò tiến sĩ của Smirnov, huy chương năm 2022 không phải sự lặp lại của định lý năm 2010 — và tính bất biến bảo giác của mô hình Ising ba chiều hiện vẫn còn mở.

**Mạch bài học:** Bản đồ kiến thức nền (mô hình thấm, Ising và cụm ngẫu nhiên FK) → Ví dụ cầm tay trên lưới thấm 2D nhỏ và mô hình Ising $$2\times 2$$ → Khung giải thích chậm: tính liên tục, tính sắc (OSSS) ở chiều 3 và tính tầm thường ở chiều 4 → Các định lý và cộng sự ở chiều 2, 3, 4 → Ranh giới với Smirnov (2010) và Werner (2006).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu lời trích dẫn ngắn của IMU năm 2022 và giải thích ba trụ cột của lời trích dẫn dài: tính liên tục và tính sắc ở chiều 3; trường trung bình và tính tầm thường ở chiều 4 (cùng Aizenman); phân loại liên tục/gián đoạn, tính phổ quát và tính bất biến quay cho mô hình FK chiều 2.
- Tự tay tính xác suất nối xuyên trên một lưới thấm nhỏ và năng lượng Ising $$2\times 2$$ để thấy trực giác của điểm tới hạn $$p_c$$ và tham số trật tự $$M(\beta)$$.
- Định nghĩa rõ **chuyển pha**, **điểm tới hạn**, chuyển pha **liên tục** so với **gián đoạn**, và **tính sắc**.
- Giải thích vì sao chiều **ba** khó hơn chiều hai và vì sao chiều **bốn** là ngưỡng tới hạn trên ($$2 + 2 = 4$$) của trường vô hướng.
- Ghi nhận đúng tính cộng tác của từng kết quả lớn (**Aizenman–Duminil-Copin**, **Aizenman–Duminil-Copin–Sidoravicius**, **Duminil-Copin–Raoufi–Tassion**, nhóm FK hai chiều).
- Phân biệt rõ **tính bất biến dưới phép quay ở thang lớn** với **tính bất biến bảo giác đầy đủ**, và không gán lý thuyết trường bảo giác (CFT) 3D cho huy chương năm 2022.

**Kiến thức cần có.** Mô hình thấm Bernoulli độc lập ở mức hình dung (mỗi cạnh mở với xác suất $$p$$); ý tưởng về thành phần liên thông vô hạn; hàm Hamilton và độ đo Gibbs cho mô hình Ising với nghịch đảo nhiệt độ $$\beta$$. Không cần biết trước SLE hay lý thuyết trường lượng tử kiến thiết.

**Liên hệ với khóa học.** Cùng được trao giải năm 2022: [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/). Các bài liên quan về xác suất và vật lý trong chương này: [Smirnov và mô hình thấm]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/), [Werner và SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/). Một hướng khác của vật lý thống kê, về động học: [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/).

---

## Bản đồ kiến thức nền: Vật lý thống kê trên lưới và lý thuyết chuyển pha nghiên cứu gì?

Vật lý thống kê xác suất đặt một câu hỏi trung tâm: *khi ta có vô hạn hạt tương tác cục bộ theo quy luật ngẫu nhiên đơn giản, làm sao lại xuất hiện những thay đổi đột ngột ở quy mô toàn cục?* Ba mô hình kinh điển dưới đây là ngôn ngữ chung của toàn ngành.

### 1. Mô hình thấm (Percolation)
Lấy lưới vuông vô hạn $$\mathbb{Z}^d$$. Mỗi cạnh nối hai đỉnh kề nhau được mở ngẫu nhiên độc lập với xác suất $$p \in [0,1]$$ và đóng với xác suất $$1-p$$. Câu hỏi cốt lõi: *có tồn tại một cụm liên thông vô hạn đi ra tận vô cực hay không?* Theo định luật không-một Kolmogorov, tồn tại một **xác suất tới hạn** $$p_c \in (0,1)$$ sao cho khi $$p < p_c$$ mọi cụm đều hữu hạn (xác suất có cụm vô hạn bằng $$0$$), còn khi $$p > p_c$$ chắc chắn xuất hiện cụm vô hạn (xác suất bằng $$1$$).

### 2. Mô hình Ising
Tại mỗi đỉnh $$x \in \mathbb{Z}^d$$ đặt một mũi tên spin $$\sigma_x \in \{+1, -1\}$$. Xác suất xuất hiện cấu hình $$\sigma$$ tỷ lệ với trọng số Boltzmann $$e^{-\beta H(\sigma)}$$, trong đó $$\beta = 1/(k_B T)$$ là nghịch đảo nhiệt độ và hàm năng lượng là:

$$
H(\sigma) = -\sum_{\langle x,y\rangle} \sigma_x \sigma_y.
$$

Hai hàng xóm chỉ cùng chiều làm năng lượng giảm $$-1$$ (ổn định hơn). Khi nhiệt độ cao ($$\beta$$ nhỏ), nhiễu nhiệt thắng thế khiến độ từ hóa tự phát $$M(\beta) = 0$$; khi nhiệt độ thấp ($$\beta > \beta_c$$), các spin đồng thuận tạo ra độ từ hóa vĩ mô $$M(\beta) > 0$$.

### 3. Mô hình cụm ngẫu nhiên Fortuin–Kasteleyn (FK)
Fortuin và Kasteleyn (thập niên 1970) thống nhất cả mô hình thấm lẫn mô hình Ising/Potts thành một họ chung có hai tham số $$(p, q)$$: xác suất của một cấu hình cạnh mở $$\omega$$ tỷ lệ với

$$
p^{\#(\text{cạnh mở})}(1-p)^{\#(\text{cạnh đóng})} \, q^{k(\omega)},
$$

với $$k(\omega)$$ là số thành phần liên thông (cụm). Khi $$q = 1$$ ta thu lại đúng mô hình thấm Bernoulli độc lập; khi $$q = 2$$ ta thu lại đúng mô hình Ising (thông qua phép tô màu ngẫu nhiên mỗi cụm bằng $$+1$$ hoặc $$-1$$)!

---

## 1. Ví dụ cầm tay chỉ việc: lưới thấm 2D nhỏ và hiệu ứng "bậc thang" khi phóng lớn lưới

Hãy tự tay tính trên một **mạng cầu nối 2D nhỏ nhất có thể** — hình chữ nhật gồm 2 đường song song (trên và dưới), mỗi đường có 2 cạnh nối tiếp, cộng thêm 1 cạnh cầu nối ở giữa (tổng cộng 5 cạnh, hay đơn giản hơn trước hết hãy xét khối 4 cạnh nối song song–nối tiếp: 2 nhánh song song, mỗi nhánh gồm 2 cạnh nối tiếp).

**Bước A — Tính chính xác đa thức nối xuyên cho khối 4 cạnh:**
Để nước chảy từ bờ trái sang bờ phải trên một nhánh 2 cạnh nối tiếp, cả 2 cạnh phải mở, xác suất là $$p^2$$. Để chảy qua ít nhất một trong 2 nhánh song song, xác suất là:

$$
f(p) = 1 - (1 - p^2)^2 = 2p^2 - p^4.
$$

Thử cắm số vào hàm $$f(p)$$ và lặp phép "phóng lớn thang đo" (thay mỗi cạnh bằng cả một khối 4 cạnh, tức lặp $$p \mapsto f(p) \mapsto f(f(p)) \mapsto \cdots$$):
- Xuất phát từ $$p = 0.5$$: $$f(0.5) = 0.4375 \to f(0.4375) = 0.346 \to 0.225 \to 0.099 \to \cdots \to 0$$!
- Xuất phát từ $$p = 0.7$$: $$f(0.7) = 0.7399 \to f(0.7399) = 0.795 \to 0.865 \to 0.937 \to \cdots \to 1$$!
- Điểm bất động duy nhất nằm giữa $$0$$ và $$1$$ là nghiệm của $$2p^2 - p^4 = p \implies p_c = \frac{\sqrt{5}-1}{2} \approx 0.618$$!

Chỉ từ một khối 4 cạnh, bạn đã nhìn thấy tận mắt **bản chất của chuyển pha và tính sắc**: chỉ cần nhích $$p$$ thấp hơn $$p_c$$ một sợi tóc, khi phóng lớn lưới ($$L \to \infty$$) xác suất nối xuyên sụp nhanh về $$0$$ theo hàm mũ; nhích cao hơn $$p_c$$ một sợi tóc, nó vọt thẳng lên $$1$$! (Trên lưới vuông $$\mathbb{Z}^2$$ thực sự, định lý Kesten (1980) chứng minh đúng $$p_c = 1/2$$.)

**Bước B — Thử mô hình Ising trên lưới vuông $$2\times 2$$ (4 đỉnh, 4 cạnh):**
Có $$2^4 = 16$$ cấu hình spin.
- 2 cấu hình đồng nhất hoàn toàn (tất cả $$+1$$ hoặc tất cả $$-1$$): có 4 cặp cùng chiều, năng lượng $$H = -4$$, trọng số $$e^{4\beta}$$.
- 2 cấu hình bàn cờ xen kẽ: có 4 cặp ngược chiều, năng lượng $$H = +4$$, trọng số $$e^{-4\beta}$$.
- 12 cấu hình còn lại: có $$H = 0$$, trọng số $$1$$.

Khi nhiệt độ cao ($$\beta = 0.1$$), tỷ số giữa trạng thái đồng nhất và trạng thái hỗn loạn chỉ là $$e^{0.4} \approx 1.49$$ — các cấu hình hỗn loạn áp đảo. Khi hạ nhiệt độ ($$\beta = 2$$), trọng số trạng thái đồng nhất vọt lên $$e^8 \approx 2981$$ — hai cấu hình đồng nhất chiếm trọn xác suất! Khi số đỉnh $$N \to \infty$$, cuộc kéo co giữa năng lượng (ưa đồng thuận) và entropy (ưa hỗn loạn) tạo ra chuyển pha sắc nét tại $$\beta_c$$.

---

## 2. Từ bài toán cổ điển đến nút thắt ở chiều 3 và chiều 4

**Rudolf Peierls (1936)** chứng minh chuyển pha tồn tại cho mô hình Ising ở mọi chiều $$d \ge 2$$. Năm 1944, **Lars Onsager** giải chính xác năng lượng tự do của mô hình Ising 2D, chứng minh chuyển pha ở đó là **liên tục**. Nhưng sang **chiều ba**, mọi công thức đại số dạng đóng đều sụp đổ. Đến thập niên 1980, hai câu hỏi cốt lõi cho mô hình Ising 3D vẫn mở:
1. Tại đúng $$\beta_c$$, độ từ hóa tự phát $$M(\beta_c)$$ có thực sự bằng $$0$$ (**tính liên tục**), hay nhảy cóc?
2. Với mọi $$\beta < \beta_c$$, tương quan có tắt theo hàm mũ (**tính sắc**)?

Còn ở **chiều bốn**, bài toán chạm thẳng vào lý thuyết trường lượng tử. Hãy nhớ trực giác hình học đơn giản: chuyển động Brown (và biểu diễn dòng ngẫu nhiên của Ising) có chiều Hausdorff bằng $$2$$. Vì $$2 + 2 = 4$$, hai đường ngẫu nhiên độc lập trong $$\mathbb{R}^d$$:
- Cắt nhau rất nhiều ở $$d = 2, 3$$ (tạo tương tác mạnh, không phải trường trung bình);
- Hầu như không bao giờ cắt nhau ở $$d \ge 5$$ (Aizenman và Fröhlich đã chứng minh tính tầm thường từ đầu thập niên 1980);
- **Vừa đúng ngưỡng tới hạn biên ở $$d = 4$$!** Chính xác suất giao nhau tắt cực chậm cỡ $$1/\ln L$$ tại $$d = 4$$ đã chặn đứng mọi chứng minh suốt 40 năm.

---

## 3. Khung giải thích: làm sao chứng minh chuyển pha ở chiều 3 và chiều 4 không cần công thức chính xác? (nên đọc chậm)

Khi không có lời giải dạng đóng như Onsager ở chiều 2, Duminil-Copin và các cộng sự đã dùng một chuỗi công cụ xác suất – hình học đầy bất ngờ:

#### Bước 1: Dùng "bất đẳng thức thuật toán OSSS" từ khoa học máy tính để chứng minh Tính sắc
Xét sự kiện $$A$$ = "có đường thấm từ tâm ra biên hộp cỡ $$n$$". Để chứng minh chuyển pha là **sắc** (tức ngay dưới $$p_c$$ xác suất nối thông đã tắt theo hàm mũ), ta cần chứng minh đạo hàm $$\frac{d}{dp}\mathbb{P}_p(A)$$ lớn khi xác suất chưa gần $$0$$ hoặc $$1$$. **Duminil-Copin, Raoufi và Tassion** đã áp dụng **bất đẳng thức OSSS** (của các nhà khoa học máy tính O'Donnell–Saks–Schramm–Servedio): bất kỳ thuật toán ngẫu nhiên nào quyết định sự kiện $$A$$ bằng cách lần lượt kiểm tra từng cạnh đều phải có ít nhất một cạnh có "ảnh hưởng" lớn. Bằng cách chọn một thuật toán thăm dò thông minh (tiết lộ từng lớp cụm từ biên), họ chứng minh rằng nếu xác suất nối thông không tắt nhanh thì đạo hàm theo $$p$$ phải bùng nổ, đẩy ngay hệ vượt qua $$p_c$$! Một định lý từ khoa học máy tính lý thuyết bỗng giải quyết trọn vẹn bài toán tính sắc cho cả họ rộng mô hình thấm phụ thuộc và Ising!

#### Bước 2: Dùng "biểu diễn dòng ngẫu nhiên" để chứng minh Tính liên tục ở chiều 3
**Aizenman, Duminil-Copin và Sidoravicius (2015)** sử dụng biểu diễn **dòng ngẫu nhiên** (*random currents*): viết tương quan giữa hai spin $$\langle \sigma_x \sigma_y \rangle$$ thành xác suất hai điểm $$x, y$$ được nối với nhau trong một đồ thị ngẫu nhiên có bậc chẵn. Định lý chuyển mạch (*switching lemma*) biến câu hỏi "$$M(\beta_c) = 0$$?" thành câu hỏi hình học: *trong hệ gồm hai dòng ngẫu nhiên độc lập tại $$\beta_c$$, có tồn tại cụm vô hạn hay không?* Nhờ phân tích hàm tương quan trên mặt phản xạ và tính đơn điệu, họ chứng minh không thể có cụm vô hạn tại $$\beta_c$$, suy ra $$M(\beta_c) = 0$$ — **chuyển pha của mô hình Ising 3D là liên tục!**

#### Bước 3: Phân tích đa thang đo cho xác suất giao của hai dòng ngẫu nhiên ở chiều 4
Trong bài báo kiệt tác năm 2021 (*Annals of Mathematics*), **Aizenman và Duminil-Copin** chứng minh rằng ở đúng chiều biên $$d = 4$$, bất đẳng thức tương quan (đặc biệt là bất đẳng thức Ursell $$U_4$$ đo độ lệch khỏi phân bố Gauss) được kiểm soát hoàn toàn bởi xác suất hai dòng ngẫu nhiên độc lập giao nhau. Bằng một lập luận đa thang đo tinh vi cho thấy xác suất giao nhau bị chặn bởi $$C / (\ln L)^c \to 0$$ khi $$L \to \infty$$, họ chứng minh **mọi hàm tương quan bậc cao ở giới hạn liên tục đều phân rã theo quy tắc Wick của trường Gauss**: mô hình Ising 4D tuân theo **trường trung bình**, và lý thuyết trường lượng tử vô hướng $$\varphi^4$$ Euclid 4D là **tầm thường** (*trivial*)!

#### Bước 4: Ở chiều 2, phân loại mô hình FK và tiến tới bất biến quay
Với mô hình cụm ngẫu nhiên FK hai chiều, Duminil-Copin cùng Tassion, Manolescu, Kozlowski, Krachun, Oulamara và các cộng sự chứng minh ranh giới chuyển pha hoàn hảo: **liên tục khi $$1 \le q \le 4$$**, **gián đoạn khi $$q > 4$$**; đồng thời chứng minh **tính phổ quát** trên đồ thị đẳng bán kính và **tính bất biến dưới phép quay** ở thang lớn (khi nhìn từ xa, cấu hình tới hạn trên lưới vuông quên mất hướng ngang–dọc $$90^\circ$$) — bước đệm trực tiếp hướng tới tính bất biến bảo giác đầy đủ.

Tóm tắt mạch đột phá:

$$
\text{Mô hình lưới } (\text{Ising / FK})
\;\longleftrightarrow\;
\text{Biểu diễn hình học (dòng ngẫu nhiên, cụm FK)}
\;\longleftrightarrow\;
\text{OSSS + Đa thang đo}
\;\Longrightarrow\;
\text{Sắc \& Liên tục (3D) + Tầm thường (4D)}.
$$

---

## 4. Ghi nhận công lao và những gì huy chương không khẳng định

| Kết quả (tóm tắt) | Tác giả |
|---------------------|----------|
| Tính liên tục của độ từ hóa cho mô hình Ising ba chiều | Aizenman–Duminil-Copin–Sidoravicius và phương pháp dòng ngẫu nhiên |
| Tính sắc cho mô hình kiểu Ising và mô hình thấm | Duminil-Copin–Raoufi–Tassion (cùng các kết quả về tính sắc trước đó) |
| Trường trung bình cho mô hình Ising bốn chiều và tính tầm thường của $$\varphi^4$$ | Aizenman–Duminil-Copin (2021) |
| Liên tục/gián đoạn của mô hình FK theo $$q$$; tính phổ quát trên đồ thị đẳng bán kính | Duminil-Copin cùng Tassion, Manolescu và những người khác |
| Bất biến dưới phép quay ở thang lớn cho mô hình FK phẳng tại điểm tới hạn | Duminil-Copin cùng Kozlowski, Krachun, Manolescu, Oulamara, … |
| Bất biến bảo giác cho mô hình thấm và mô hình Ising hai chiều | **Smirnov (Fields 2010)**, xem [bài đó]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) |
| SLE như ngôn ngữ cho giới hạn tỷ lệ | **Schramm; Lawler–Schramm–Werner; Werner (Fields 2006)**, xem [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) |

(Một dấu ấn sớm khác của Duminil-Copin cùng người hướng dẫn **Stanislav Smirnov** năm 2012 là chứng minh hằng số liên thông của đường đi tự tránh trên lưới tổ ong đúng bằng $$\sqrt{2+\sqrt{2}}$$ — công trình đầu sự nghiệp đẹp mắt, đứng bên cạnh trọng tâm chiều 3 và chiều 4 của huy chương 2022.)

Duminil-Copin sinh năm 1985 tại Pháp, học tại ENS và Paris-Sud, làm luận án ở Geneva dưới sự hướng dẫn của Smirnov (2011), và là giáo sư tại Đại học Geneva cùng IHÉS.

**Đừng khẳng định:** đã chứng minh tính bất biến bảo giác đầy đủ cho mô hình Ising ba chiều; đã phân loại mọi mô hình trên lưới; đã giải xong lý thuyết trường lượng tử kiến thiết ở chiều ba; hay SLE được phát minh lại năm 2022.

---

## 5. Vì sao ông nhận Huy chương Fields

Cơ học thống kê trên lưới nổi tiếng giàu dự đoán vật lý nhưng khan hiếm định lý chặt chẽ ở đúng những số chiều của thế giới thực. Chiều hai có Onsager, CFT, SLE và Smirnov; chiều cao có trường trung bình và khai triển lace. Chính **chiều ba và chiều bốn** là khoảng trống lớn nhất mà IMU nhấn mạnh. Bằng cách kết hợp biểu diễn dòng ngẫu nhiên, cụm FK, bất đẳng thức thuật toán OSSS và phân tích đa thang đo thay vì tìm lời giải đóng, Duminil-Copin và các cộng sự đã mở toang cánh cửa vào các số chiều vật lý đó.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Ông chứng minh tính bất biến bảo giác của mô hình Ising ba chiều." | Vấn đề này vẫn còn mở. Công trình hai chiều của ông là tính bất biến dưới phép quay, một *bước hướng tới* bất biến bảo giác cho các mô hình FK. |
| "Ông chứng minh tính bất biến bảo giác hai chiều (định lý Smirnov)." | Đó là kết quả của Smirnov (2010). Duminil-Copin mở rộng chương trình FK hai chiều và chuyển sang chiều ba, bốn. |
| "Tính tầm thường nghĩa là mô hình Ising bốn chiều không có gì thú vị." | Nó nghĩa là *giới hạn tỷ lệ liên tục* là một trường Gauss, một phát biểu sâu về lý thuyết trường lượng tử. |
| "Tính sắc cũng là tính liên tục." | Tính sắc nói về sự suy giảm theo hàm mũ ngoài điểm tới hạn; tính liên tục nói về tham số trật tự tại $$\beta_c$$. |
| "Huy chương 2022 là cho một chứng minh ba chiều của riêng ông." | Văn bản của IMU nói "cùng các cộng sự"; kết quả bốn chiều là cùng Aizenman. |
| "Chuyển pha nghĩa là có $$p_c$$." | Sự tồn tại thường đã được biết; huy chương nói về *bản chất* của chuyển pha. |

---

## Nguồn video và đọc thêm

Bài này không có bộ tài liệu video riêng của khóa học.

1. Huy chương Fields 2022 của IMU (trích dẫn ngắn): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022).
2. Lời trích dẫn dài của IMU (PDF): [IMU_Fields22_Duminil-Copin_citation.pdf](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/IMU_Fields22_Duminil-Copin_citation.pdf).
3. Bách khoa: [Hugo Duminil-Copin](https://en.wikipedia.org/wiki/Hugo_Duminil-Copin).
4. Bài giới thiệu của Quanta (2022): [Hugo Duminil-Copin Wins the Fields Medal](https://www.quantamagazine.org/hugo-duminil-copin-wins-the-fields-medal-20220705/).
5. Tìm trên arXiv: [Duminil-Copin Ising](https://arxiv.org/search/?query=Duminil-Copin+Ising&searchtype=all); bản tiền ấn phẩm về bất biến dưới phép quay [arXiv:2012.11672](https://arxiv.org/abs/2012.11672).
6. Các bài liên quan trong chương này: [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/), [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/).

**Ghi nhớ:** Tính liên tục, tính sắc ở chiều ba và tính tầm thường ở chiều bốn, cùng các cộng sự. **Không** phải tính bất biến bảo giác ở chiều ba.

---

## Tài liệu tham khảo

1. International Mathematical Union, Huy chương Fields 2022: Hugo Duminil-Copin, lời trích dẫn ngắn và dài (mathunion.org).
2. **M. Aizenman, H. Duminil-Copin**, *Marginal triviality of the scaling limits of critical 4D Ising and $$\varphi^4$$ models*, *Ann. of Math.* 194 (2021).
3. Các công trình của Duminil-Copin cùng **Aizenman, Sidoravicius, Raoufi, Tassion, Manolescu** và những người khác về tính liên tục, tính sắc và mô hình FK trên mặt phẳng (xem lời trích dẫn của IMU để biết cách nhóm các kết quả).
4. **H. Duminil-Copin, S. Smirnov**, hằng số liên thông của lưới tổ ong, *Ann. of Math.* 175 (2012). Đây là công trình thời kỳ đầu, không thuộc phần ba chiều và bốn chiều của lời trích dẫn.
5. Tài liệu nền: lời giải mô hình Ising hai chiều của Onsager; sách về mô hình cụm ngẫu nhiên của Grimmett; các bài tổng quan về tính tầm thường trong lý thuyết trường kiến thiết (Aizenman, Fröhlich, …) để tham khảo.
6. Trong khóa học: [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/), [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/).

---

## Hướng đi tiếp

- Học biểu diễn FK cho đến khi giải thích được vì sao mô hình Potts tương ứng với một mô hình thấm có phụ thuộc.
- Đọc một tài liệu giải thích về dòng ngẫu nhiên trước khi đọc bài báo về tính liên tục ở chiều ba.
- Bài seminar A3 (tùy chọn): viết một trang về *các câu hỏi về bất biến bảo giác còn mở* (bất biến bảo giác đầy đủ cho mô hình FK hai chiều; CFT cho mô hình Ising ba chiều, về mặt vật lý và về mặt toán học), không gán các định lý đó cho huy chương năm 2022.
- Nếu bạn thích tổ hợp chính xác, hãy bắt đầu từ hằng số liên thông của lưới tổ ong (cùng Smirnov), rồi chuyển sang các kết quả ba chiều và bốn chiều trong lời trích dẫn của IMU để thấy rõ trọng tâm của huy chương.

## Video tham khảo

- **Xem trước** — [Fields Medal: Hugo Duminil-Copin](https://www.youtube.com/watch?v=5dXulZVstbY) — Simons Foundation, tiếng Anh. Video giới thiệu ngắn về Duminil-Copin và các công trình về chuyển pha được trao giải. Nên xem trước khi đọc bài.
- [Hugo DUMINIL-COPIN - Critical phenomena through the lens of the Ising model](https://www.youtube.com/watch?v=jNOffVsULVM) — Institut Fourier, tiếng Anh. Bài giảng của Duminil-Copin về hiện tượng tới hạn qua mô hình Ising, liên quan đến mục 1–3. Nên xem sau khi đọc bài.
- [Lecture: Duminil-Copin | September 29](https://www.youtube.com/watch?v=s3KgdQXjsy8) — Heidelberg Laureate Forum, tiếng Anh. Bài giảng tại Heidelberg Laureate Forum, bổ sung thêm góc nhìn về chuyển pha. Dành cho người muốn tìm hiểu thêm.
