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

**Hugo Duminil-Copin** nhận **Huy chương Fields 2022**. Theo lời trích dẫn ngắn của IMU, giải thưởng dành cho việc "giải quyết những bài toán tồn tại lâu trong lý thuyết xác suất về **chuyển pha** trong vật lý thống kê, đặc biệt ở chiều **ba** và **bốn**." Lời trích dẫn dài chi tiết hơn, và bài này đi theo lời trích dẫn dài. Cùng các cộng sự, ông chứng minh **tính liên tục** và **tính sắc** của chuyển pha cho các mô hình kiểu Ising trong không gian ba chiều, những câu hỏi còn mở từ thập niên 1980. Ở chiều bốn, cùng **Michael Aizenman**, ông chứng minh mô hình Ising có **hành vi tới hạn kiểu trường trung bình**, và chứng minh **tính tầm thường** (triviality) của lý thuyết trường lượng tử vô hướng Euclid bốn chiều, một giả thuyết lâu đời của vật lý. Ở chiều hai, với mô hình thấm phụ thuộc **Fortuin–Kasteleyn (FK)**, ông và các cộng sự xác định chuyển pha là liên tục hay gián đoạn ứng với từng giá trị tham số, chứng minh tính phổ quát trên các đồ thị đẳng bán kính (isoradial), và chứng minh **tính bất biến dưới phép quay** ở thang lớn, một bước hướng tới tính bất biến bảo giác.

Bài này dành cho người đã biết mô hình Ising (các spin trên một lưới) hoặc mô hình thấm (percolation, các cạnh mở hoặc đóng), và muốn hiểu cấu trúc của một công trình xác suất ở tầm Fields. Bài **không** nói rằng Duminil-Copin chứng minh tính bất biến bảo giác của mô hình Ising ba chiều; vấn đề đó vẫn còn mở. Bài cũng phân biệt công trình của ông với các định lý về bất biến bảo giác hai chiều của [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) (Fields 2010) và chương trình SLE của [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/). Đó là các công trình liên quan, nhưng là những định lý khác nhau. Smirnov là người hướng dẫn tiến sĩ của Duminil-Copin; huy chương năm 2022 là bước tiếp theo, không phải sự lặp lại.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu lời trích dẫn ngắn của IMU năm 2022 và giải thích ba phần của lời trích dẫn dài: tính liên tục và tính sắc cho mô hình kiểu Ising ba chiều; trường trung bình và tính tầm thường ở chiều bốn (cùng Aizenman); chuyển pha liên tục hay gián đoạn của mô hình FK hai chiều, tính phổ quát, và tính bất biến dưới phép quay.
- Định nghĩa ở mức ý tưởng: **chuyển pha**, **điểm tới hạn**, chuyển pha **liên tục** và **gián đoạn** của một tham số trật tự, và **tính sắc** (suy giảm theo hàm mũ dưới điểm tới hạn; có thấm trên điểm tới hạn).
- Giải thích vì sao chiều **ba** khó đối với mô hình Ising ngay cả khi chiều hai đã có lời giải chính xác, và vì sao chiều **bốn** là ngưỡng của trường trung bình cho trường vô hướng.
- Ghi nhận định lý về tính tầm thường ở chiều bốn là công trình chung của **Aizenman–Duminil-Copin**, và các kết quả ở chiều ba, chiều hai là của **những nhóm cộng sự cụ thể**, không phải của một tác giả.
- Phân biệt **tính bất biến dưới phép quay ở thang lớn** (một bước ở chiều hai hướng tới bất biến bảo giác) với **tính bất biến bảo giác đầy đủ**, và với mọi khẳng định về lý thuyết trường bảo giác (CFT) cho mô hình Ising ba chiều.
- Luyện **LO6**: câu "ông đã giải xong vật lý thống kê" là nói quá.

**Kiến thức cần có.** Mô hình thấm Bernoulli độc lập ở mức hình dung (mỗi cạnh mở với xác suất $$p$$); ý tưởng về thành phần liên thông vô hạn; hàm Hamilton và độ đo Gibbs cho mô hình Ising với nghịch đảo nhiệt độ $$\beta$$. Không cần biết trước SLE hay lý thuyết trường lượng tử kiến thiết.

**Liên hệ với khóa học.** Cùng được trao giải năm 2022: [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/). Các bài liên quan về xác suất và vật lý trong chương này: [Smirnov và mô hình thấm]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/), [Werner và SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/). Một hướng khác của vật lý thống kê, về động học: [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/).

---

## 1. Lịch sử: chuyển pha giải được chính xác ở chiều hai, khó ở chiều ba

**Chuyển pha** là sự thay đổi đột ngột trong hành vi ở thang lớn của một hệ khi một tham số thay đổi (nhiệt độ, mật độ, hay trọng số của cạnh). **Mô hình Ising** trên $$\mathbb{Z}^d$$ gán cho mỗi đỉnh một spin $$\sigma_x=\pm 1$$, và gán cho mỗi cấu hình trọng số $$e^{-\beta H}$$ với $$H=-\sum_{\langle x,y\rangle}\sigma_x\sigma_y$$. Ở nhiệt độ cao ($$\beta$$ nhỏ), tương quan giữa các spin giảm nhanh và **độ từ hóa tự phát** bằng 0. Ở nhiệt độ thấp, điều kiện biên dương có thể tạo ra một độ từ hóa $$M(\beta)$$ khác không. **Onsager** giải chính xác mô hình Ising hai chiều (1944) và cho thấy chuyển pha ở đó là liên tục. **Peierls** đã chứng minh trước đó rằng chuyển pha tồn tại khi số chiều từ hai trở lên. Mô hình thấm (mở mỗi cạnh một cách độc lập với xác suất $$p$$) cũng có một **xác suất tới hạn** $$p_c$$ rõ ràng: khi $$p>p_c$$ có một cụm vô hạn.

Đến thập niên 1980, *sự tồn tại* của chuyển pha cho mô hình Ising láng giềng gần nhất ở chiều $$d\ge 2$$ đã là kết quả cổ điển. Nhưng một số câu hỏi về *loại* chuyển pha vẫn còn mở ở chiều ba. $$M(\beta)$$ có tiến về $$0$$ khi $$\beta\downarrow\beta_c$$ không (chuyển pha liên tục)? Tương quan có giảm theo hàm mũ với mọi $$\beta<\beta_c$$, đồng thời bức tranh phía trên điểm tới hạn có khớp không (**tính sắc**)? Lập luận trường trung bình và phương pháp khai triển lace (lace expansion) trả lời được ở chiều *cao*, nhưng chiều ba nằm ngoài tầm của các phương pháp đó. Chiều bốn, chiều tới hạn trên của lý thuyết vô hướng $$\varphi^4$$, là một khó khăn khác. Các nhà vật lý dự đoán rằng giới hạn tỷ lệ của mô hình Ising / $$\varphi^4$$ bốn chiều tại điểm tới hạn là một **trường tự do Gauss**, tức là không có lý thuyết trường lượng tử vô hướng liên tục có tương tác trong không gian Euclid bốn chiều. Nhưng chưa có chứng minh toán học đầy đủ.

Các mô hình **phụ thuộc** hai chiều, đặc biệt là biểu diễn **cụm ngẫu nhiên (FK)** của mô hình Potts và mô hình Ising, đặt ra loại câu hỏi thứ ba. Với tham số FK $$q$$, khi nào chuyển pha là liên tục và khi nào tham số trật tự có bước nhảy? Sau khi [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) chứng minh tính bất biến bảo giác cho mô hình thấm đỉnh trên lưới tam giác và cho mô hình Ising hai chiều, vẫn còn một chương trình nghiên cứu: xử lý mô hình thấm FK *phụ thuộc* cho mọi $$q$$, trên nhiều loại đồ thị hơn lưới vuông, và chứng minh các tính đối xứng còn thiếu (phép quay, rồi bất biến bảo giác đầy đủ) để nối các mô hình trên lưới với lý thuyết trường bảo giác hai chiều. [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) cùng Lawler và Schramm đã chỉ ra rằng **SLE** mô tả giới hạn tỷ lệ một khi đã biết tính bất biến bảo giác. Các công trình hai chiều của Duminil-Copin nằm trong chương trình đó, không thay thế kết quả của Smirnov hay SLE.

---

## 2. Ý chính: hiểu bản chất của chuyển pha, không chỉ sự tồn tại

**Ý chính.** Một định lý hiện đại trong lĩnh vực này không chỉ nói "$$p_c$$ tồn tại". Nó nói hệ *tiến đến* $$p_c$$ như thế nào: liên tục hay có bước nhảy; tương quan giảm theo hàm mũ hay theo lũy thừa; số mũ tới hạn là số mũ trường trung bình hay không; hệ có bất biến dưới phép quay ở thang lớn, hay chỉ có các đối xứng của lưới.

Có ba khái niệm trong lời trích dẫn của IMU cần định nghĩa.

**Tính liên tục** của chuyển pha nghĩa là tham số trật tự (độ từ hóa với mô hình Ising, xác suất thấm với mô hình FK) tiến về giá trị tại điểm tới hạn mà không có bước nhảy. Với mô hình Ising ba chiều, đó là phát biểu $$M(\beta_c)=0$$ (tại điểm tới hạn không còn độ từ hóa dư). Theo lời trích dẫn, câu hỏi này còn mở từ thập niên 1980.

**Tính sắc** nghĩa là toàn bộ vùng dưới tới hạn đều có hành vi tốt: xác suất liên thông giảm theo hàm mũ theo khoảng cách, và độ cảm (susceptibility) hữu hạn, với mọi $$\beta<\beta_c$$ hoặc $$p<p_c$$, chứ không chỉ khi $$\beta$$ còn xa điểm tới hạn. Duminil-Copin, Raoufi và Tassion phát triển một phương pháp dựa trên thuật toán ngẫu nhiên (bất đẳng thức OSSS) để chứng minh tính sắc cho một lớp rộng các mô hình, kể cả các mô hình kiểu Ising ba chiều.

**Trường trung bình và tính tầm thường** ở chiều bốn nghĩa là các số mũ tới hạn bằng các số mũ Gauss (trường trung bình), và giới hạn tỷ lệ của trường trên lưới là một trường Gauss. Theo ngôn ngữ vật lý, lý thuyết $$\varphi^4$$ Euclid bốn chiều là **tầm thường**: nó không cho một giới hạn liên tục có tương tác thật sự. Bài báo của **Aizenman–Duminil-Copin** (2021) là kết quả mà lời trích dẫn nhắc đến.

---

## 3. Các định lý và các cộng sự

**Chiều 3 (mô hình kiểu Ising).** Tính liên tục của độ từ hóa tự phát và tính sắc của chuyển pha đưa mô hình Ising ba chiều từ chỗ "biết có chuyển pha" đến chỗ "chuyển pha đúng là loại mà mọi người dự đoán nhưng chưa chứng minh được". Đây là kết quả cộng tác. Tính liên tục của độ từ hóa cho mô hình Ising ba chiều là công trình của **Aizenman, Duminil-Copin và Sidoravicius** (dùng biểu diễn dòng ngẫu nhiên). Tính sắc gắn với **Duminil-Copin, Raoufi và Tassion**, những người đưa ra một chứng minh mới áp dụng được cho nhiều mô hình; riêng với mô hình Ising, tính sắc đã được Aizenman, Barsky và Fernández chứng minh năm 1987. Mọi cách nói chỉ nêu một tên đều không đúng.

**Chiều 4 (cùng Aizenman).** Hành vi tới hạn kiểu trường trung bình của mô hình Ising và tính tầm thường của lý thuyết trường lượng tử vô hướng Euclid bốn chiều giải quyết một giả thuyết có từ thập niên 1970 trong lý thuyết trường kiến thiết và vật lý toán (trước đó đã có các kết quả một phần ở chiều *cao hơn* và cho các mô hình khác). Đây là kết quả **chung** của Aizenman và Duminil-Copin.

**Chiều 2 (mô hình FK / cụm ngẫu nhiên).** Với mô hình cụm ngẫu nhiên trên mặt phẳng, Duminil-Copin và các cộng sự xác định chuyển pha là liên tục hay gián đoạn với **mọi** $$q\ge 1$$: liên tục khi $$q\le 4$$, gián đoạn khi $$q>4$$. Kết quả này biến bức tranh cổ điển của Baxter và những người khác thành định lý cho các mô hình lưới chuẩn. **Tính phổ quát** trên đồ thị **đẳng bán kính** nói rằng hành vi tới hạn không phụ thuộc vào cách nhúng đẳng bán kính cụ thể. **Tính bất biến dưới phép quay** ở thang lớn (Duminil-Copin, Kozlowski, Krachun, Manolescu, Oulamara và các công trình liên quan), theo lời IMU, là "một bước quan trọng hướng tới việc chứng minh tính bất biến bảo giác ở thang lớn của chúng". Đó sẽ là thành phần còn thiếu để nối chặt chẽ với lý thuyết trường bảo giác hai chiều. Kết quả này **không** phải là chứng minh đầy đủ tính bất biến bảo giác cho mọi mô hình FK đó, và **không** nói gì về mô hình Ising ba chiều.

**Một kết quả hai chiều sớm hơn.** Cùng Smirnov, Duminil-Copin chứng minh hằng số liên thông của lưới tổ ong bằng $$\sqrt{2+\sqrt{2}}$$ (cho đường đi tự tránh). Đây là công trình thời kỳ đầu của ông, không phải trọng tâm ba chiều và bốn chiều của lời trích dẫn năm 2022.

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

Duminil-Copin sinh năm 1985 tại Pháp, học tại ENS và Paris-Sud, làm luận án ở Geneva dưới sự hướng dẫn của Smirnov (2011), và giữ vị trí tại Đại học Geneva và IHÉS. Chi tiết tiểu sử có thể bỏ qua, nhưng bảng cộng sự thì cần nắm.

**Đừng khẳng định:** đã chứng minh tính bất biến bảo giác đầy đủ cho mô hình Ising ba chiều; đã phân loại mọi mô hình trên lưới; đã giải lý thuyết trường lượng tử kiến thiết ở chiều ba; hay SLE được phát minh lại năm 2022.

---

## 5. Vì sao ông nhận Huy chương Fields

Cơ học thống kê trên lưới có nhiều dự đoán đẹp nhưng ít định lý ở những số chiều mà hiện tượng vật lý thật sự xảy ra. Chiều hai có Onsager, lý thuyết trường bảo giác, SLE và Smirnov. Chiều cao có trường trung bình và khai triển lace. Chiều ba và bốn là khoảng trống mà IMU nêu ra. Việc chứng minh tính liên tục và tính sắc ở chiều ba, cùng tính tầm thường ở chiều bốn, cho thấy cách mới để có định lý ở "số chiều có ý nghĩa vật lý": dùng các biểu diễn xác suất (dòng ngẫu nhiên, độ đo cụm ngẫu nhiên), công cụ về ngưỡng sắc từ khoa học máy tính, và các bất đẳng thức tương quan cổ điển, thay vì tìm một lời giải chính xác dạng đóng.

Trong khóa học, Duminil-Copin là ví dụ về việc **dùng ngôn ngữ có sẵn cho những số chiều mới**. Ông dùng các công cụ của Smirnov, Werner và Aizenman; huy chương ghi nhận việc ông dùng các công cụ đó để chứng minh những phát biểu ở chiều ba và bốn vốn được biết là còn mở trong nhiều thập niên.

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
