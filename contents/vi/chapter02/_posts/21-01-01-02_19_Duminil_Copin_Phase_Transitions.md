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

Hãy nghĩ về một thanh nam châm sắt quen thuộc. Khi bạn nung nóng nó dần lên, từ tính yếu đi từng chút một; rồi đúng tại một ngưỡng nhiệt độ chính xác (nhiệt độ Curie, khoảng $$770^\circ\text{C}$$), từ tính biến mất hoàn toàn. Hoặc hình dung dòng nước thấm qua một tảng đá xốp: chỉ cần mật độ khe hở vượt qua một ngưỡng mỏng như sợi tóc, nước bỗng tìm được đường chảy xuyên suốt cả tảng đá. Những bước ngoặt đột ngột ở quy mô vĩ mô xuất hiện từ vô số tương tác vi mô ngẫu nhiên như vậy được gọi là **chuyển pha** (*phase transitions*).

Trong suốt nhiều thập niên, toán học về chuyển pha mắc kẹt trong một nghịch lý kỳ lạ: ở **chiều hai** (mặt phẳng), ta có cả lời giải chính xác của Onsager lẫn bộ máy bất biến bảo giác rực rỡ của [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) và [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/); ở **chiều rất cao** ($$d \ge 5$$), các đường tương tác hiếm khi va vào nhau nên xấp xỉ trường trung bình hoạt động trơn tru. Nhưng đúng hai số chiều mà thế giới vật lý thực sự sống trong đó — **chiều ba** (không gian của nam châm và chất lỏng) và **chiều bốn** (không-thời gian của lý thuyết trường lượng tử) — lại là vùng tối đầy những câu hỏi mở từ thập niên 1970–1980.

Năm 2022, **Hugo Duminil-Copin** nhận **Huy chương Fields** nhờ "giải quyết những bài toán tồn tại lâu trong lý thuyết xác suất về **chuyển pha** trong vật lý thống kê, đặc biệt ở chiều **ba** và **bốn**." Cùng các cộng sự, ông chứng minh **tính liên tục** và **tính sắc** của chuyển pha cho mô hình kiểu Ising ba chiều; cùng **Michael Aizenman**, ông chứng minh mô hình Ising bốn chiều tuân theo **trường trung bình** và lý thuyết trường lượng tử vô hướng Euclid bốn chiều là **tầm thường** (*trivial*); và ở chiều hai, ông cùng cộng sự hoàn thiện bức tranh chuyển pha liên tục/gián đoạn của mô hình cụm ngẫu nhiên **Fortuin–Kasteleyn (FK)**, chứng minh tính phổ quát trên đồ thị đẳng bán kính và **tính bất biến dưới phép quay** ở thang lớn. Dù là học trò tiến sĩ của Smirnov, huy chương năm 2022 không phải sự lặp lại của định lý bất biến bảo giác năm 2010 — và bài học này cũng sẽ chỉ rõ rằng tính bất biến bảo giác của mô hình Ising ba chiều hiện vẫn còn mở.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu lời trích dẫn ngắn của IMU năm 2022 và giải thích ba trụ cột trong lời trích dẫn dài: tính liên tục và tính sắc cho mô hình kiểu Ising ba chiều; hành vi trường trung bình và tính tầm thường ở chiều bốn (cùng Aizenman); phân loại liên tục/gián đoạn, tính phổ quát và tính bất biến dưới phép quay cho mô hình FK hai chiều.
- Định nghĩa trực quan bốn khái niệm cốt lõi: **chuyển pha**, **điểm tới hạn**, chuyển pha **liên tục** so với **gián đoạn** của tham số trật tự, và **tính sắc** (suy giảm hàm mũ dưới ngưỡng tới hạn; có thấm trên ngưỡng tới hạn).
- Giải thích vì sao chiều **ba** lại cực kỳ khó dù chiều hai đã giải chính xác được, và vì sao chiều **bốn** là ngưỡng tới hạn trên của trường vô hướng.
- Ghi nhận đúng tính cộng tác của từng kết quả lớn (**Aizenman–Duminil-Copin**, **Aizenman–Duminil-Copin–Sidoravicius**, **Duminil-Copin–Raoufi–Tassion**, và nhóm nghiên cứu mô hình FK hai chiều).
- Phân biệt rõ **tính bất biến dưới phép quay ở thang lớn** (một bước ở chiều hai hướng tới bất biến bảo giác) với **tính bất biến bảo giác đầy đủ**, và tránh nhầm lẫn với các giả thuyết về lý thuyết trường bảo giác (CFT) cho mô hình Ising ba chiều.

**Kiến thức cần có.** Mô hình thấm Bernoulli độc lập ở mức hình dung (mỗi cạnh mở với xác suất $$p$$); ý tưởng về thành phần liên thông vô hạn; hàm Hamilton và độ đo Gibbs cho mô hình Ising với nghịch đảo nhiệt độ $$\beta$$. Không cần biết trước SLE hay lý thuyết trường lượng tử kiến thiết.

**Liên hệ với khóa học.** Cùng được trao giải năm 2022: [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/). Các bài liên quan về xác suất và vật lý trong chương này: [Smirnov và mô hình thấm]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/), [Werner và SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/). Một hướng khác của vật lý thống kê, về động học: [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/).

---

## Bản đồ kiến thức nền: Lý thuyết thấm và chuyển pha thống kê nghiên cứu gì?

Để đọc các định lý của Duminil-Copin mà không bị ngợp bởi thuật ngữ vật lý, ta chỉ cần nắm ba mô hình lưới đơn giản đến mức có thể vẽ trên giấy kẻ ô vuông.

**1. Mô hình thấm (Percolation) — trò chơi mở cạnh ngẫu nhiên.**
Hãy lấy lưới vuông vô hạn $$\mathbb{Z}^d$$ (như bàn cờ vô tận ở chiều $$d=2$$ hoặc khung giàn giáo không gian ở chiều $$d=3$$). Với mỗi cạnh nối hai đỉnh kề nhau, ta tung một đồng xu thiên lệch: cạnh đó "mở" (cho nước chảy qua) với xác suất $$p \in [0,1]$$ và "đóng" với xác suất $$1-p$$, độc lập giữa các cạnh. Câu hỏi trung tâm: *có tồn tại một cụm liên thông vô hạn các cạnh mở đi ra tận vô cực hay không?*
Theo định luật không-một Kolmogorov, xác suất xuất hiện cụm vô hạn chỉ có thể bằng $$0$$ hoặc $$1$$. Tồn tại một ngưỡng sắc nét $$p_c \in (0,1)$$ gọi là **xác suất tới hạn**: khi $$p < p_c$$ mọi cụm đều hữu hạn; khi $$p > p_c$$ chắc chắn có một cụm vô hạn xuyên khắp không gian.

**2. Mô hình Ising — xã hội của các mũi tên từ tính.**
Thay vì mở/đóng cạnh, ta đặt tại mỗi đỉnh $$x \in \mathbb{Z}^d$$ một **spin** $$\sigma_x \in \{+1, -1\}$$ (như một nam châm tí hon chỉ lên hoặc chỉ xuống). Hai hàng xóm chỉ cùng chiều sẽ có năng lượng thấp (ổn định), còn chỉ ngược chiều sẽ tốn năng lượng. Ở nghịch đảo nhiệt độ $$\beta = 1/(k_B T)$$, xác suất xuất hiện một cấu hình $$\sigma$$ tỷ lệ với trọng số Boltzmann $$e^{-\beta H(\sigma)}$$, trong đó hàm năng lượng là

$$
H(\sigma) = -\sum_{\langle x,y\rangle} \sigma_x \sigma_y.
$$

- Khi nhiệt độ cao ($$\beta$$ nhỏ): nhiễu nhiệt áp đảo, các spin lật ngẫu nhiên độc lập, tổng độ từ hóa trung bình (gọi là **tham số trật tự** $$M(\beta)$$) bằng $$0$$.
- Khi nhiệt độ thấp ($$\beta > \beta_c$$): các spin đồng thuận thành một "đám đông" vĩ mô, tạo ra **độ từ hóa tự phát** $$M(\beta) > 0$$ ngay cả khi không có từ trường ngoài.

**3. Mô hình cụm ngẫu nhiên Fortuin–Kasteleyn (FK) — cây cầu thống nhất.**
Trong thập niên 1970, Fortuin và Kasteleyn phát hiện một cách ghép tuyệt đẹp: ta có thể nhìn mô hình Ising (và tổng quát hơn là mô hình Potts với $$q$$ trạng thái màu) như một **mô hình thấm có phụ thuộc**. Thay vì chỉ nhân $$p$$ cho mỗi cạnh mở và $$1-p$$ cho mỗi cạnh đóng, mỗi cấu hình cạnh $$\omega$$ còn được thưởng thêm một hệ số $$q^{k(\omega)}$$, trong đó $$k(\omega)$$ là số thành phần liên thông (cụm). Khi $$q = 1$$ ta thu lại đúng mô hình thấm Bernoulli độc lập; khi $$q = 2$$ ta thu lại đúng mô hình Ising! Nhờ biểu diễn FK (và một biểu diễn hình học song hành gọi là **dòng ngẫu nhiên** — *random currents*), bài toán về độ từ hóa và tương quan spin được dịch thẳng thành bài toán hình học về xác suất nối thông giữa các điểm trên lưới.

---

## 1. Từ bài toán cổ điển đến ý tưởng đột phá: chiều 2 giải được, chiều 3 và 4 mắc kẹt

**Rudolf Peierls** (1936) là người đầu tiên chứng minh bằng một lập luận đếm đường biên cực kỳ duyên dáng rằng mô hình Ising thực sự có chuyển pha ở mọi số chiều $$d \ge 2$$. Rồi năm 1944, **Lars Onsager** tạo ra một kỳ tích đại số: ông giải chính xác năng lượng tự do của mô hình Ising hai chiều trên lưới vuông, chứng minh rằng chuyển pha tại $$\beta_c$$ là **liên tục** (độ từ hóa giảm êm về $$0$$ chứ không tụt hẫng) và tính ra chính xác các số mũ tới hạn.

Nhưng ngay khi bước lên **chiều ba**, mọi phép tính đại số chính xác kiểu Onsager đều sụp đổ vì không gian ba chiều không còn tính phẳng để dùng các biến đổi đối ngẫu hay ma trận truyền đơn giản. Đến thập niên 1980, ai cũng biết mô hình Ising 3D có một điểm tới hạn $$\beta_c$$, nhưng hai câu hỏi cơ bản về *bản chất* của chuyển pha đó vẫn bỏ ngỏ:
1. Tại đúng ngưỡng $$\beta = \beta_c$$, độ từ hóa tự phát $$M(\beta_c)$$ có thật sự bằng $$0$$ không (**tính liên tục**), hay nó nhảy đột ngột từ $$0$$ lên một giá trị dương (như nước sôi nhảy mật độ từ lỏng sang hơi)?
2. Với *mọi* $$\beta < \beta_c$$, tương quan giữa hai spin cách nhau khoảng cách $$r$$ có giảm nhanh theo hàm mũ $$e^{-c(\beta) r}$$ không (**tính sắc**), hay tồn tại một vùng "lưng chừng" mà tương quan giảm chậm theo lũy thừa?

Lên đến **chiều bốn**, câu chuyện chuyển sang một câu hỏi sâu sắc của vật lý hạt cơ bản. Theo trực giác hình học, chuyển động Brown trong không gian $$d$$ chiều có chiều Hausdorff bằng $$2$$. Vì $$2 + 2 = 4$$, hai đường ngẫu nhiên độc lập trong $$\mathbb{R}^d$$ sẽ thường xuyên cắt nhau khi $$d \le 3$$, hiếm khi cắt nhau khi $$d \ge 5$$, và **vừa đúng ngưỡng chạm** ở $$d = 4$$! Trong vật lý lý thuyết, điều này dẫn đến dự đoán từ thập niên 1970: khi ta thu nhỏ bước lưới của mô hình Ising 4D (hoặc lý thuyết trường $$\varphi^4$$ trên lưới 4D) về $$0$$ tại điểm tới hạn để xây dựng một **lý thuyết trường lượng tử vô hướng Euclid bốn chiều**, tương tác giữa các hạt sẽ biến mất hoàn toàn ở giới hạn liên tục — giới hạn đó chỉ là một **trường tự do Gauss** (**tính tầm thường**, *triviality*). Aizenman và Fröhlich đã chứng minh được điều này cho $$d \ge 5$$ từ đầu thập niên 1980, nhưng đúng số chiều biên $$d = 4$$ — số chiều của không-thời gian vật lý — vẫn kháng cự suốt 40 năm.

Ở **chiều hai**, sau khi [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) chứng minh tính bất biến bảo giác cho mô hình thấm trên lưới tam giác và mô hình Ising 2D, còn [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) cùng Lawler và Schramm xây dựng **SLE** để mô tả đường biên tới hạn, một chương trình lớn vẫn dang dở: xử lý mô hình thấm FK *phụ thuộc* cho mọi $$q \ge 1$$, trên các đồ thị tổng quát hơn lưới vuông, và chứng minh các tính đối xứng hình học còn thiếu (như bất biến quay) làm bệ phóng tiến tới tính bất biến bảo giác đầy đủ.

---

## 2. Ý chính: hiểu bản chất của chuyển pha, không chỉ sự tồn tại

**Ý chính.** Một định lý hiện đại trong lý thuyết chuyển pha không dừng lại ở câu "$$p_c$$ tồn tại". Nó trả lời chính xác hệ *tiến đến* $$p_c$$ như thế nào: tham số trật tự tiến về $$0$$ êm ái hay nhảy cóc; tương quan tắt nhanh theo hàm mũ hay lê thê theo lũy thừa; các số mũ tới hạn có rơi về trường trung bình hay không; và khi nhìn từ rất xa, các cụm ngẫu nhiên có "quên" được hướng ngang-dọc của lưới ô vuông để trở nên bất biến dưới mọi phép quay hay không.

Để nắm trọn lời trích dẫn của IMU năm 2022, ta cần phân biệt rõ ba khái niệm then chốt:

**1. Tính liên tục (Continuity).** Nghĩa là tham số trật tự tiến về $$0$$ liên tục khi tiến tới điểm tới hạn: $$M(\beta_c) = 0$$ (với mô hình Ising) hoặc xác suất gốc tọa độ thuộc cụm vô hạn bằng $$0$$ tại $$p_c$$ (với mô hình FK). Ví dụ trực quan: nước sôi ở áp suất thường là chuyển pha **gián đoạn** (mật độ nhảy vọt giữa lỏng và hơi), còn nam châm sắt mất từ tính tại nhiệt độ Curie là chuyển pha **liên tục** (độ từ hóa giảm trơn về $$0$$). Chứng minh $$M(\beta_c) = 0$$ cho mô hình Ising 3D là bài toán mở từ thập niên 1980.

**2. Tính sắc (Sharpness).** Nghĩa là ranh giới giữa hai pha mỏng tuyệt đối, không có "vùng xám": với mọi $$\beta < \beta_c$$ (dù sát $$\beta_c$$ đến đâu), xác suất hai điểm cách nhau khoảng cách $$r$$ tương quan với nhau giảm theo hàm mũ $$e^{-c r}$$ và độ cảm (susceptibility) hữu hạn; còn với mọi $$\beta > \beta_c$$, trật tự tầm xa lập tức xuất hiện. Ý tưởng đột phá của **Duminil-Copin, Raoufi và Tassion** là mượn một công cụ từ khoa học máy tính lý thuyết — **bất đẳng thức OSSS** về thuật toán quyết định ngẫu nhiên (O'Donnell–Saks–Schramm–Servedio) — để chứng minh rằng muốn kiểm tra xem có đường thấm xuyên qua một hộp lớn hay không, mọi thuật toán đều phải "hỏi" rất nhiều cạnh, từ đó suy ra đạo hàm theo tham số phải bùng nổ và chuyển pha bắt buộc phải sắc!

**3. Trường trung bình và tính tầm thường (Mean-field & Triviality) ở chiều bốn.** Trong biểu diễn dòng ngẫu nhiên, độ lệch khỏi hành vi Gauss được đo bằng xác suất hai dòng ngẫu nhiên độc lập giao nhau. Ở chiều $$d = 4$$ — đúng chiều tới hạn biên nơi xác suất giao nhau chỉ tắt chậm cỡ $$1/\ln L$$ thay vì lũy thừa — **Aizenman và Duminil-Copin** (2021) thiết lập các ước lượng đa thang đo tinh vi để chứng minh xác suất giao nhau đó thực sự tiến về $$0$$ ở giới hạn liên tục. Hệ quả là mọi hàm tương quan bậc cao phân rã theo quy tắc Wick của trường Gauss: lý thuyết $$\varphi^4$$ Euclid bốn chiều là **tầm thường**, không tồn tại giới hạn liên tục có tương tác phi tầm thường.

---

## 3. Các định lý và các cộng sự

**Chiều 3 (mô hình kiểu Ising).** Hai định lý về tính liên tục và tính sắc đưa mô hình Ising ba chiều từ chỗ "biết có chuyển pha" sang chỗ "xác nhận chính xác bức tranh vật lý về chuyển pha loại hai". Đây là những công trình cộng tác rõ ràng:
- **Tính liên tục** của độ từ hóa cho mô hình Ising ba chiều ($$M(\beta_c) = 0$$) là công trình chung của **Michael Aizenman, Hugo Duminil-Copin và Vladas Sidoravicius** (2015), sử dụng biểu diễn **dòng ngẫu nhiên** (*random currents*) để quy tính liên tục về việc không tồn tại cụm vô hạn trong hệ hai dòng ngẫu nhiên độc lập.
- **Tính sắc** cho một lớp rộng các mô hình phụ thuộc (bao gồm mô hình FK và các mô hình kiểu Ising nhiều chiều) gắn với **Duminil-Copin, Raoufi và Tassion** (2019) nhờ phương pháp thuật toán quyết định OSSS; riêng với mô hình Ising láng giềng gần nhất, tính sắc trước đó đã được Aizenman, Barsky và Fernández chứng minh năm 1987.

**Chiều 4 (cùng Aizenman).** Bài báo *Marginal triviality of the scaling limits of critical 4D Ising and $$\varphi^4$$ models* (*Annals of Mathematics*, 2021) của **Aizenman và Duminil-Copin** giải quyết trọn vẹn giả thuyết có từ thập niên 1970 về tính tầm thường của lý thuyết trường lượng tử vô hướng Euclid bốn chiều và hành vi trường trung bình tại điểm tới hạn. Đây là thành quả **chung** của hai tác giả, không phải công trình đơn lẻ.

**Chiều 2 (mô hình FK / cụm ngẫu nhiên).** Trên mặt phẳng, Duminil-Copin cùng các cộng sự đã biến toàn bộ bức tranh cổ điển của Baxter thành định lý chặt chẽ cho **mọi** $$q \ge 1$$:
- **Phân loại chuyển pha:** Chuyển pha là **liên tục** khi $$1 \le q \le 4$$ và **gián đoạn** khi $$q > 4$$ (cùng Sidoravicius, Tassion, rồi cùng Gagnebin, Harel, Manolescu, Tassion). Hãy hình dung: khi $$q$$ nhỏ (như thấm độc lập $$q=1$$ hay Ising $$q=2$$), hệ chuyển pha êm ái; nhưng khi số màu $$q > 4$$, sự "ưa tụ cụm" của yếu tố $$q^{k(\omega)}$$ trở nên quá mạnh khiến hệ nhảy vọt đột ngột tại điểm tới hạn.
- **Tính phổ quát trên đồ thị đẳng bán kính (isoradial):** Hành vi tới hạn không phụ thuộc vào hình dạng cụ thể của lưới phẳng miễn là lưới thuộc lớp đẳng bán kính.
- **Tính bất biến dưới phép quay ở thang lớn** (cùng Kozlowski, Krachun, Manolescu, Oulamara): khi phóng xa một cấu hình FK tới hạn trên lưới vuông (vốn chỉ có đối xứng quay $$90^\circ$$), thống kê ở thang lớn trở nên bất biến dưới **mọi góc quay**! Theo lời IMU, đây là "một bước quan trọng hướng tới việc chứng minh tính bất biến bảo giác ở thang lớn của chúng", nhưng **chưa** phải chứng minh đầy đủ tính bất biến bảo giác cho mọi $$q \in [1,4]$$ và hoàn toàn **không** nói về mô hình Ising ba chiều.

**Một kết quả hai chiều sớm hơn.** Năm 2012, cùng người hướng dẫn **Stanislav Smirnov**, Duminil-Copin chứng minh hằng số liên thông của đường đi tự tránh trên lưới tổ ong đúng bằng $$\sqrt{2+\sqrt{2}}$$ — xác nhận dự đoán nổi tiếng năm 1982 của nhà vật lý Nienhuis bằng một chứng minh đẹp như thơ dùng đại lượng chỉnh hình rời rạc. Đây là dấu ấn đầu sự nghiệp của ông, đứng bên cạnh trọng tâm chiều 3 và chiều 4 của lời trích dẫn năm 2022.

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

Duminil-Copin sinh năm 1985 tại Pháp, học tại ENS và Paris-Sud, làm luận án ở Geneva dưới sự hướng dẫn của Smirnov (2011), và giữ vị trí giáo sư tại Đại học Geneva cùng IHÉS. Chi tiết tiểu sử chỉ là bối cảnh, nhưng bảng cộng sự ở trên là điều rất cần nắm chính xác.

**Đừng khẳng định:** đã chứng minh tính bất biến bảo giác đầy đủ cho mô hình Ising ba chiều; đã phân loại mọi mô hình trên lưới; đã giải xong lý thuyết trường lượng tử kiến thiết ở chiều ba; hay SLE được phát minh lại năm 2022.

---

## 5. Vì sao ông nhận Huy chương Fields

Cơ học thống kê trên lưới nổi tiếng là mảnh đất giàu dự đoán vật lý nhưng khan hiếm định lý chặt chẽ ở đúng những số chiều của tự nhiên. Chiều hai có phép màu của tính phẳng (Onsager, CFT, SLE, Smirnov). Chiều cao có trường trung bình và khai triển lace. Chính **chiều ba và chiều bốn** là khoảng trống khó nhằn nhất mà IMU nhấn mạnh. Bằng cách kết hợp các biểu diễn hình học–xác suất (dòng ngẫu nhiên, cụm ngẫu nhiên FK), công cụ ngưỡng sắc từ khoa học máy tính (bất đẳng thức OSSS), và phân tích đa thang đo thay vì tìm kiếm những công thức giải chính xác dạng đóng, Duminil-Copin và các cộng sự đã mở toang cánh cửa vào vùng tối đó.

Trong mạch khóa học, Duminil-Copin là hình mẫu về việc **đưa sức mạnh của xác suất hình học sang những số chiều mới**: ông tiếp nối ngôn ngữ của Aizenman, Smirnov và Werner, rồi rèn thêm những công cụ tổng quát hơn để giải quyết các bài toán tồn đọng hàng thập niên ở chiều ba và chiều bốn.

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

## Bài tập

1. Diễn đạt bằng lời của bạn: **chuyển pha** trong mô hình thấm là gì, và **tính sắc** cho thêm thông tin gì ngoài việc $$p_c$$ tồn tại?
2. Ở mức ý tưởng, vì sao chiều 2 "giải chính xác được" còn chiều 3 thì không? (So sánh lời giải của Onsager với việc chưa có lời giải dạng đóng cho mô hình Ising ba chiều.)
3. Phát biểu kết quả về tính tầm thường ở chiều bốn trong một câu, và nêu tên **cả hai** tác giả.
4. Liên tục hay gián đoạn: vẽ phác đồ thị $$M(\beta)$$ có bước nhảy và không có bước nhảy. Hình nào ứng với mô hình FK hai chiều khi $$q>4$$?
5. **Luyện độ chính xác.** Một bài báo đặt tiêu đề: "Nhà toán học chứng minh nam châm ba chiều có tính bảo giác". Viết lại thành hai câu phù hợp với khóa học này.
6. So sánh [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) và Duminil-Copin bằng một bảng bốn dòng: số chiều, mô hình, điều đã chứng minh, điều còn lại.
7. Vì sao **tính bất biến dưới phép quay** là một bước cần thiết để đi tới tính bất biến bảo giác, nhưng chưa đủ? Viết một đoạn.
8. **Seminar mở rộng.** IMU nhắc đến "các trường hợp không khả tích ở chiều 2". Chữ "khả tích" ở đây là một lời cảnh báo nói về điều gì (công thức chính xác chỉ có khi $$q$$ đặc biệt hoặc lưới đặc biệt), và vì sao một chứng minh không cần đến những công thức đó lại có giá trị hơn?

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
