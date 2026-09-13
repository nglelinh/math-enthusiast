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

**Hugo Duminil-Copin** nhận **Huy chương Fields 2022** vì, theo citation ngắn của IMU, “giải những bài toán tồn tại lâu trong lý thuyết xác suất về **chuyển pha** trong vật lý thống kê, đặc biệt ở chiều **ba** và **bốn**.” Citation dài chính xác hơn, và bài này theo nó. Cùng cộng sự, ông thiết lập **tính liên tục** và **độ sắc** của chuyển pha cho các mô hình kiểu Ising ở chiều ba—các câu hỏi mở từ thập niên 1980. Ở chiều bốn, cùng **Michael Aizenman**, ông chứng minh **hành vi tới hạn trường trung bình** của mô hình Ising và **tính tầm thường** (triviality) của lý thuyết trường lượng tử vô hướng Euclid bốn chiều, một giả thuyết vật lý cũ. Ở chiều hai, với percolation **Fortuin–Kasteleyn (FK)** phụ thuộc, ông và cộng sự xác định tính liên tục hay gián đoạn với mọi giá trị tham số, chứng minh tính phổ quát trên đồ thị đẳng bán kính (isoradial), và thiết lập **bất biến quay** ở thang lớn như một bước tới bất biến conformal.

Bài này dành cho người đã thấy mô hình Ising như các spin trên lattice, hoặc percolation như cạnh mở và đóng, và muốn nắm kiến trúc một bài xác suất tầm Fields. Bài **không** khẳng định Duminil-Copin chứng minh bất biến conformal của mô hình Ising ba chiều. Điều đó vẫn mở. Bài cũng phân biệt công trình của ông với các định lý bất biến conformal chiều hai năm 2010 của [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) và chương trình SLE của [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/)—các chân dung kề, không cùng định lý. Người hướng dẫn tiến sĩ của Duminil-Copin là Smirnov; huy chương 2022 là chương tiếp, không phải bản in lại.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu citation ngắn IMU 2022 và diễn giải ba khối của citation dài: tính liên tục/độ sắc Ising-type 3D; trường trung bình / triviality 4D với Aizenman; liên tục-gián đoạn FK 2D, tính phổ quát, phép quay.
- Định nghĩa, mức khẩu hiệu, một **chuyển pha**, **điểm tới hạn**, **liên tục versus gián đoạn** của một tham số thứ tự, và **độ sắc** (suy giảm mũ dưới tới hạn; percolation trên tới hạn).
- Giải thích vì sao chiều **ba** khó với mô hình Ising ngay cả sau các lời giải đúng chiều hai, và vì sao chiều **bốn** là ngưỡng trường trung bình cho trường vô hướng.
- Gán định lý triviality 4D chung cho **Aizenman–Duminil-Copin**, và gán kết quả 3D cùng 2D cho **các nhóm cộng sự có tên** chứ không cho một tác giả đơn.
- Phân biệt **bất biến quay ở thang lớn** (một bước 2D tới bất biến conformal) với **bất biến conformal đầy đủ**, và với mọi tuyên bố về CFT Ising 3D.
- Luyện **LO6**: “ông giải xong vật lý thống kê” là hype.

**Kiến thức nền.** Percolation Bernoulli độc lập như tranh biếm họa (cạnh mở với xác suất $$p$$); ý tưởng thành phần liên thông vô hạn; Hamiltonian và độ đo Gibbs cho mô hình Ising ở nghịch nhiệt $$\beta$$. Không cần SLE hay QFT kiến tạo trước.

**Liên kết seminar.** Cùng lớp 2022: [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/). Họ hàng xác suất-và-vật lý (các chân dung tương lai trong chương này): [Smirnov / percolation]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/), [Werner / SLE]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/). Vật lý thống kê động học khác loại: [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/).

---

## 1. Lịch sử chuyển pha, đúng ở chiều hai và bướng ở chiều ba

Một **chuyển pha** là một thay đổi sắc trong hành vi thang lớn của hệ khi một tham số đổi—nhiệt độ, mật độ, hoặc trọng số cạnh. **Mô hình Ising** trên $$\mathbb{Z}^d$$ gán spin $$\sigma_x=\pm 1$$ cho các đỉnh và gán trọng cho cấu hình bằng $$e^{-\beta H}$$ với $$H=-\sum_{\langle x,y\rangle}\sigma_x\sigma_y$$. Ở nhiệt độ cao ($$\beta$$ nhỏ) tương quan suy giảm và **từ hóa tự phát** triệt tiêu; ở nhiệt độ thấp, điều kiện biên cộng có thể buộc một từ hóa $$M(\beta)$$ khác không. **Onsager** giải đúng mô hình Ising hai chiều (1944) và trưng ra một chuyển pha liên tục. **Peierls** đã chỉ ra rằng chuyển pha tồn tại từ chiều hai trở lên. Percolation—mở cạnh độc lập với xác suất $$p$$—có **xác suất tới hạn** $$p_c$$ sắc tương tự, với một chùm vô hạn khi $$p>p_c$$.

Sang thập niên 1980, *sự tồn tại* của chuyển pha cho Ising láng giềng gần ở chiều $$d\ge 2$$ đã cổ điển, nhưng vài câu hỏi “chuyển pha loại gì?” vẫn mở ở chiều ba. Có phải $$M(\beta)$$ tiến về $$0$$ khi $$\beta\downarrow\beta_c$$ (tính liên tục của chuyển pha)? Có phải tương quan nhỏ theo hàm mũ với mọi $$\beta<\beta_c$$, kèm bức tranh siêu tới hạn khớp (**độ sắc**)? Heuristic trường trung bình và lace expansion cho câu trả lời ở chiều *cao*; chiều ba nằm dưới các phương pháp đó. Chiều bốn, chiều tới hạn trên của lý thuyết vô hướng $$\varphi^4$$, là một sự lúng túng khác: nhà vật lý kỳ vọng giới hạn tỷ lệ của Ising / $$\varphi^4$$ 4D tới hạn là một **trường tự do Gauss**—không có QFT vô hướng continuum tương tác ở bốn chiều Euclid—nhưng một chứng minh toán học đầy đủ còn thiếu.

Các mô hình **phụ thuộc** hai chiều, đáng kể là biểu diễn **random-cluster (FK)** của Potts và Ising, đặt ra một họ câu hỏi thứ ba. Với tham số FK $$q$$, khi nào chuyển pha liên tục và khi nào tham số thứ tự nhảy? Sau khi [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) chứng minh bất biến conformal cho percolation đỉnh trên lattice tam giác và cho mô hình Ising 2D, một chương trình còn lại: xử lý percolation FK *phụ thuộc* với mọi $$q$$, trên nhiều đồ thị hơn lattice vuông, và sản sinh các đối xứng còn thiếu (phép quay, rồi bất biến conformal đầy đủ) nối các mô hình lattice với lý thuyết trường conformal 2D. [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) và Lawler–Schramm–Werner đã chỉ ra **SLE** mô tả giới hạn tỷ lệ một khi biết bất biến conformal. Công trình 2D của Duminil-Copin sống trong đường ống đó; nó không thay thế Smirnov hay SLE.

---

## 2. Khẩu hiệu: đọc chuyển pha, không chỉ sự tồn tại của nó

**Khẩu hiệu.** Một định lý hiện đại trong môn này không chỉ nói “$$p_c$$ tồn tại.” Nó nói hệ *tiến tới* $$p_c$$ thế nào: liên tục hay có bước nhảy; với suy giảm mũ hay với luật lũy thừa; với số mũ trường trung bình hay với số mũ không cổ điển; với bất biến quay ở thang lớn hay chỉ với đối xứng lattice.

Ba từ trong citation IMU đáng được định nghĩa.

**Tính liên tục** của chuyển pha nghĩa là tham số thứ tự—từ hóa với Ising, xác suất percolation với FK—tiến tới giá trị tới hạn không nhảy. Với Ising 3D, đó là phát biểu $$M(\beta_c)=0$$ (không còn từ hóa dư tại tới hạn), mở từ thập niên 1980 theo dạng citation nêu.

**Độ sắc** nghĩa là chế độ dưới tới hạn *đồng đều* dưới tới hạn: liên thông suy giảm theo hàm mũ theo khoảng cách, và susceptibility hữu hạn, với mọi $$\beta<\beta_c$$ hoặc $$p<p_c$$, không chỉ với $$\beta$$ xa dưới tới hạn. Duminil-Copin, Raoufi và Tassion phát triển các phương pháp thuật toán ngẫu nhiên / OSSS chứng minh độ sắc cho một lớp rộng các mô hình, kể cả các bối cảnh kiểu Ising 3D.

**Trường trung bình / triviality** ở chiều bốn nghĩa là các số mũ tới hạn khớp các số mũ Gauss (trường trung bình) và giới hạn tỷ lệ của trường lattice là Gauss. Ngôn ngữ vật lý: lý thuyết $$\varphi^4$$ Euclid bốn chiều là **tầm thường**—nó không cho một giới hạn continuum tương tác khác tầm thường thuộc kiểu này. **Aizenman–Duminil-Copin** (2021) là bài mà citation chỉ tới.

---

## 3. Các định lý sắp xếp lại điều gì, với cộng sự được nêu tên

**Chiều 3 (kiểu Ising).** Tính liên tục của từ hóa tự phát và độ sắc của chuyển pha đưa Ising 3D từ “một chuyển pha tồn tại” sang “chuyển pha thuộc loại mọi người đã kỳ vọng nhưng không chứng minh được.” Công lao là cộng tác. Tính liên tục của từ hóa cho mô hình Ising 3D gắn với công trình của **Aizenman, Duminil-Copin và Sidoravicius** (biểu diễn dòng ngẫu nhiên). Độ sắc gắn với **Duminil-Copin, Raoufi và Tassion**. Coi mọi khẩu hiệu một tên là sai.

**Chiều 4 (với Aizenman).** Hành vi tới hạn trường trung bình của Ising và triviality của QFT vô hướng Euclid 4D khép một giả thuyết sống trong lý thuyết trường kiến tạo và vật lý toán từ thập niên 1970 (với các kết quả bộ phận sớm hơn ở chiều *cao* và cho các mô hình khác). Gán khối này **chung** cho Aizenman và Duminil-Copin.

**Chiều 2 (FK / random-cluster).** Với mô hình random-cluster phẳng, Duminil-Copin và cộng sự chứng minh chuyển pha liên tục hoặc gián đoạn với **mọi** $$q>0$$: liên tục khi $$q\le 4$$, gián đoạn khi $$q>4$$, hoàn tất một bức tranh cổ điển của Baxter và những người khác ở mức định lý cho các mô hình lattice chuẩn. **Tính phổ quát** trên đồ thị **isoradial** nói rằng hành vi tới hạn không phụ thuộc phép nhúng isoradial cụ thể. **Bất biến quay** ở thang lớn (Duminil-Copin, Kozlowski, Krachun, Manolescu, Oulamara, và các công trình liên quan) là, theo lời IMU, “một bước quan trọng hướng tới thiết lập bất biến conformal thang lớn của chúng,” vốn sẽ là thành phần còn thiếu cho một liên kết chặt với CFT 2D. Đó **không** phải chứng minh đầy đủ bất biến conformal cho mọi mô hình FK này, và **không** phải phát biểu về Ising ba chiều.

**Mốc 2D sớm hơn, để định vị.** Cùng Smirnov, Duminil-Copin chứng minh hằng số liên thông của lattice tổ ong bằng $$\sqrt{2+\sqrt{2}}$$ (đường đi tự tránh). Đó là phần hình thành của ông, không phải trọng tâm 3D/4D của citation 2022.

---

## 4. Gán công lao trung thực và huy chương không phải gì

| Kết quả (khẩu hiệu) | Công lao |
|---------------------|----------|
| Tính liên tục từ hóa Ising 3D | Aizenman–Duminil-Copin–Sidoravicius và trường phái dòng ngẫu nhiên |
| Độ sắc cho mô hình kiểu Ising / percolation | Duminil-Copin–Raoufi–Tassion (và văn liệu độ sắc trước đó) |
| Ising trường trung bình 4D và triviality $$\varphi^4$$ | Aizenman–Duminil-Copin (2021) |
| Liên tục/gián đoạn FK với mọi $$q$$; phổ quát isoradial | Duminil-Copin với Tassion, Manolescu, và những người khác |
| Bất biến quay thang lớn trong mô hình FK phẳng tới hạn | Duminil-Copin với Kozlowski, Krachun, Manolescu, Oulamara, … |
| Bất biến conformal percolation / Ising 2D | **Smirnov (Fields 2010)** — xem [bài đó]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) |
| SLE như ngôn ngữ giới hạn tỷ lệ | **Schramm; Lawler–Schramm–Werner; Werner (Fields 2006)** — xem [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/) |

Duminil-Copin sinh năm 1985 tại Pháp, học tại ENS và Paris-Sud, viết luận án ở Geneva dưới Smirnov (2011), và giữ vị trí tại Đại học Geneva cùng IHÉS. Màu tiểu sử là tùy chọn; bảng cộng sự thì không.

**Đừng khẳng định:** bất biến conformal đầy đủ của Ising 3D; phân loại mọi mô hình lattice; lời giải QFT kiến tạo ở chiều ba; rằng SLE được phát minh lại năm 2022.

---

## 5. Vì sao Huy chương Fields

Cơ học thống kê lattice đầy những tiên đoán đẹp và ít định lý ở những chiều nơi vật lý thật sự xảy ra. Chiều hai có Onsager, lý thuyết trường conformal, SLE, và Smirnov. Chiều cao có trường trung bình và lace expansion. Chiều ba và bốn là khoảng trống IMU nêu. Khép tính liên tục và độ sắc ở 3D, cùng triviality ở 4D, đã đổi diện mạo một định lý “chiều thực tế về mặt vật lý”: các biểu diễn xác suất (dòng ngẫu nhiên, độ đo random-cluster), công cụ ngưỡng sắc từ khoa học máy tính, và các bất đẳng thức tương quan cổ điển, chứ không phải một lời giải đúng dạng đóng.

Trong khóa học này, Duminil-Copin là chân dung **ngôn ngữ thừa kế, chiều mới**. Ông viết bằng từ vựng của Smirnov, Werner và Aizenman; huy chương dành cho việc khiến từ vựng đó chứng minh các phát biểu 3D và 4D đã được quảng cáo là mở suốt nhiều thập niên.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Ông chứng minh bất biến conformal của Ising 3D.” | Vẫn mở. Công trình 2D là bất biến quay như *bước tới* bất biến conformal của các mô hình FK. |
| “Ông chứng minh bất biến conformal 2D (định lý Smirnov).” | Smirnov (2010) là chân dung bất biến conformal; Duminil-Copin mở rộng chương trình FK 2D và chuyển sang 3D/4D. |
| “Triviality nghĩa là mô hình Ising 4D nhàm chán.” | Nghĩa là *giới hạn tỷ lệ continuum* là Gauss, một phát biểu sâu về QFT. |
| “Độ sắc cũng là tính liên tục.” | Độ sắc nói về suy giảm mũ ngoài tới hạn; tính liên tục nói về tham số thứ tự tại $$\beta_c$$. |
| “Huy chương 2022 là chứng minh 3D đơn.” | Văn bản IMU nói “cùng cộng sự”; 4D là với Aizenman. |
| “Chuyển pha = tồn tại $$p_c$$.” | Sự tồn tại thường đã biết; huy chương nói về *bản chất* của chuyển pha. |

---

## Bài tập

1. Bằng lời của bạn: **chuyển pha** với percolation là gì, và **độ sắc** thêm thông tin gì ngoài sự tồn tại của $$p_c$$?
2. Vì sao chiều 2 “giải được đúng” theo cách chiều 3 thì không, mức khẩu hiệu? (Onsager versus không có Ising 3D dạng đóng.)
3. Phát biểu kết quả triviality 4D trong một câu, và nêu **cả hai** tác giả.
4. Liên tục versus gián đoạn: vẽ một tranh biếm họa $$M(\beta)$$ có bước nhảy và không có bước nhảy. Tranh nào là FK 2D khi $$q>4$$?
5. **Luyện độ chính xác.** Một tiêu đề: “Nhà toán học chứng minh nam châm 3D là conformal.” Viết lại thành hai câu cho khóa học này.
6. So [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/) và Duminil-Copin trong bảng bốn dòng: chiều, mô hình, điều đã chứng minh, điều còn lại.
7. Vì sao **bất biến quay** lại là bước cần thiết hướng tới bất biến conformal, nhưng chưa đủ? Một đoạn.
8. **Seminar mở rộng.** IMU nhắc “các trường hợp không khả tích ở chiều 2.” “Khả tích” nghĩa là gì như một lời cảnh báo (công thức đúng chỉ tồn tại với $$q$$ đặc biệt hoặc lattice đặc biệt), và vì sao một chứng minh tránh những công thức đó lại quý hơn?

---

## Nguồn video và đọc thêm

Bài này không kèm gói nghiên cứu video của khóa học.

1. IMU Fields Medals 2022 (citation ngắn): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022).
2. Citation dài IMU (PDF): [IMU_Fields22_Duminil-Copin_citation.pdf](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2022/IMU_Fields22_Duminil-Copin_citation.pdf).
3. Bách khoa: [Hugo Duminil-Copin](https://en.wikipedia.org/wiki/Hugo_Duminil-Copin).
4. Profile Quanta (2022): [Hugo Duminil-Copin Wins the Fields Medal](https://www.quantamagazine.org/hugo-duminil-copin-wins-the-fields-medal-20220705/).
5. Tìm arXiv: [Duminil-Copin Ising](https://arxiv.org/search/?query=Duminil-Copin+Ising&searchtype=all); preprint bất biến quay [arXiv:2012.11672](https://arxiv.org/abs/2012.11672).
6. Các bài liên quan trong chương này: [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/), [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/).

**Nhắc:** Tính liên tục/độ sắc 3D và triviality 4D với cộng sự—**không** phải bất biến conformal 3D.

---

## Tài liệu tham khảo

1. International Mathematical Union, Fields Medal 2022 — Hugo Duminil-Copin, citation ngắn và dài (mathunion.org).
2. **M. Aizenman, H. Duminil-Copin**, *Marginal triviality of the scaling limits of critical 4D Ising and $$\varphi^4$$ models*, *Ann. of Math.* 194 (2021).
3. Các công trình của Duminil-Copin với **Aizenman, Sidoravicius, Raoufi, Tassion, Manolescu**, và những người khác về tính liên tục, độ sắc, và mô hình FK phẳng (xem citation IMU để nhóm).
4. **H. Duminil-Copin, S. Smirnov**, hằng số liên thông lattice tổ ong, *Ann. of Math.* 175 (2012)—hình thành, không phải citation 3D/4D.
5. Nền: lời giải Ising 2D của Onsager; sách random-cluster của Grimmett; các survey triviality kiến tạo (Aizenman, Fröhlich, …) như con trỏ.
6. Khóa học: [Smirnov]({{ site.baseurl }}/contents/vi/chapter02/02_28_Smirnov_Percolation/), [Werner]({{ site.baseurl }}/contents/vi/chapter02/02_30_Werner_SLE/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/).

---

## Hướng đi tiếp

- Học biểu diễn FK cho đến khi nói được vì sao mô hình Potts là mô hình percolation có phụ thuộc.
- Đọc một tài liệu giải thích dòng ngẫu nhiên trước khi thử bài tính liên tục 3D.
- Tùy chọn seminar A3: bản một trang về *các câu hỏi conformal còn mở*—bất biến conformal FK 2D đầy đủ; CFT Ising 3D như vật lý versus toán—không trao những định lý đó cho 2022.
- Nếu thích tổ hợp đúng hơn, bắt đầu từ hằng số liên thông tổ ong (với Smirnov) rồi nhảy sang danh sách 3D/4D của IMU để trọng tâm huy chương vẫn lộ.
