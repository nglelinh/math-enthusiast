---
layout: post
title: "Giả thuyết Kakeya"
chapter: '01'
order: 8
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
---

> **Lộ trình học A — Kakeya (3 bước)**  
> **1. Bạn đang ở đây:** Chương 1, tổng quan về bài toán  
> **2. Tiếp theo:** [Bài về Hong Wang, Chương 2 (Fields 2026)]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/): lý thuyết đầy đủ  
> **3. Sau đó:** [Bài thực hành Kakeya, Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/): vẽ, lập trình, viết  
> *Thời gian gợi ý:* khoảng 45 phút cho bài tổng quan, 2–3 giờ cho bài giảng, 1–2 giờ cho bài thực hành.

Hãy tưởng tượng bạn đặt một **cây kim mảnh dài đúng 1 đơn vị** lên mặt bàn. Bạn muốn xoay đầu kim quay đủ một vòng theo **mọi hướng** (từ $$0^\circ$$ đến $$180^\circ$$), nhưng mặt bàn lại chật chội nên bạn muốn phần diện tích bị cây kim quét qua phải **nhỏ nhất có thể**. Câu trả lời đầu tiên nảy ra trong đầu hầu như ai cũng giống nhau: cứ giữ tâm kim đứng yên rồi xoay tròn thành hình đĩa diện tích $$\pi/4 \approx 0{,}785$$ là xong! Nhưng nếu bạn chịu khó vừa xoay vừa trượt khéo léo như kiểu lùi xe vào bãi hẹp (hình deltoid ba mũi nhọn), diện tích lập tức giảm xuống chỉ còn một nửa ($$\pi/8 \approx 0{,}393$$). Năm **1917**, nhà toán học Nhật Bản **Sōichi Kakeya** đặt câu hỏi đó một cách nghiêm túc: *diện tích nhỏ nhất ấy rốt cuộc là bao nhiêu?*

Chỉ vài năm sau, **Abram Besicovitch** tung ra một câu trả lời làm đảo lộn mọi trực giác hình học thông thường: diện tích đó có thể **nhỏ tùy ý** — thậm chí tiến về **bằng không** (độ đo Lebesgue bằng 0)! Một tập hợp "gần như chẳng chiếm chút diện tích nào" trên mặt phẳng mà vẫn giấu kín bên trong một đoạn thẳng dài 1 đơn vị theo *tất cả mọi hướng*!

Nghịch lý kỳ dị ấy đã khai sinh ra một câu hỏi còn sâu hơn gấp bội: nếu thể tích không đủ tinh để đo kích thước của những tập "mỏng tang" như vậy, hãy dùng thước đo sắc bén hơn là **chiều Hausdorff** và **chiều Minkowski**. **Giả thuyết tập Kakeya** dự đoán rằng dù thể tích có thể bằng 0, một tập chứa đoạn thẳng đơn vị theo mọi hướng trong $$\mathbb{R}^n$$ vẫn buộc phải "đủ dày" về mặt chiều hình học: $$\dim_H=\dim_M=n$$. Suốt nhiều thập niên, những tên tuổi lớn như **Wolff**, **Bourgain**, **Terence Tao** chỉ đạt được các chặn dưới từng phần. Cho đến đầu năm **2025**, **Hong Wang** và **Joshua Zahl** đã gây chấn động toàn cầu khi chứng minh trọn vẹn giả thuyết trong **không gian 3 chiều** — một cột mốc được ca ngợi là đột phá lớn bậc nhất của giải tích điều hòa trong hai thập kỷ, và là một phần quan trọng trong các công trình giúp Wang nhận **Huy chương Fields 2026** (cùng các đóng góp về bài toán hạn chế, làm trơn cục bộ, bài toán Falconer, Furstenberg; xem trích dẫn của IMU và [bài về Wang ở Chương 2]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/)).

Đây là **bài tổng quan về bài toán ở Chương 1**: câu chuyện cây kim → nghịch lý độ đo bằng không → giả thuyết về số chiều → tình trạng cho 2, 3 và $$\ge 4$$ chiều → vì sao giải tích điều hòa quan tâm. Bài giảng đầy đủ (ống bán kính $$\delta$$, lập luận tự cải thiện, các công trình được giải Fields ghi nhận) là bước 2 của lộ trình trên.

**Phát biểu ngắn gọn.** Nếu $$K\subset\mathbb{R}^n$$ chứa đoạn thẳng đơn vị theo mọi hướng, có nhất thiết $$\dim_H(K)=\dim_M(K)=n$$ không? Davies (1971): đúng trong 2 chiều. Wang–Zahl (2025): đúng trong 3 chiều. Với $$n\ge 4$$, bài toán còn **mở**.

**Một phân biệt cần nắm sớm.** *Chuyển động liên tục của cây kim* (xoay một đoạn thẳng bên trong một miền) và *tập Besicovitch tĩnh* (chứa đoạn thẳng theo mọi hướng, không cần là các vị trí liên tiếp của một cây kim) là hai đối tượng có liên quan nhưng **không** giống nhau. Cả hai cùng xoay quanh ý "độ dày theo hướng"; chi tiết ở mục 1.

---

## Mục tiêu học tập

- Định nghĩa tập Kakeya (tập Besicovitch) trong $$\mathbb{R}^n$$.
- Phân biệt **độ đo bằng không** với **số chiều bằng $$n$$** (chiều Minkowski, chiều Hausdorff).
- Phát biểu giả thuyết và bảng tình trạng (2, 3, từ 4 chiều trở lên).
- Mô tả ý tưởng **ống bán kính $$\delta$$** ($$\delta$$-tube) ở mức tóm tắt.
- Ghi nhận đúng rằng đây là công trình chung của **Wang và Zahl**; liên hệ với bài ở Chương 2 và bài thực hành ở Chương 7.
- Không nhầm **chuyển động liên tục của cây kim** với tập Besicovitch tĩnh.

**Kiến thức cần có.** Không gian Euclid, diện tích và thể tích, ý niệm sơ lược về số chiều fractal. Đọc kèm bài về Wang ở Chương 2 để có trình bày đầy đủ.

**Kết nối trong khóa học.** Bạn có thể đọc song song bài này với số nguyên tố sinh đôi (cấu trúc trong tập thưa), định lý bốn màu (đã giải so với còn mở) và bài thực hành khám phá tập Kakeya nhỏ nhất ở Chương 7.

---

## Bản đồ kiến thức nền: Lý thuyết độ đo hình học và Giải tích điều hòa là gì?

Tại sao một câu đố tưởng như giải trí về việc "xoay cây kim" lại nằm ở trung tâm của toán học hiện đại và gắn liền với Huy chương Fields 2026? Câu trả lời nằm ở giao điểm của hai ngành toán học cực kỳ quyền lực:

- **Lý thuyết độ đo hình học (Geometric Measure Theory):** Trong giải tích đại học, bạn đo kích thước bằng độ dài, diện tích, thể tích (độ đo Lebesgue). Nhưng với những tập cực kỳ phức tạp như tập Cantor, đường bờ biển fractal, hay tập Besicovitch (diện tích 0 nhưng chứa đủ mọi hướng), độ đo Lebesgue bị "mù" — nó trả về 0 cho tất cả! Lý thuyết độ đo hình học chế tạo ra kính hiển vi đa thang đo (như **chiều Hausdorff** và **độ đo Hausdorff**) để phân loại và đo đạc các vật thể gồ ghề, kỳ dị, hoặc mặt cực tiểu (như màng xà phòng).
- **Giải tích điều hòa (Harmonic Analysis):** Nếu bạn từng học chuỗi Fourier hay biến đổi Fourier ở đại học (phân tích một tín hiệu âm thanh 1D thành tổng các sóng sin–cos theo tần số), thì giải tích điều hòa hiện đại mở rộng tư tưởng đó lên **không gian nhiều chiều** $$\mathbb{R}^n$$. Khi phân tích một sóng ánh sáng hay sóng âm lan truyền trong không gian 3 chiều thành các "gói sóng" (wave packets) cục bộ, mỗi gói sóng về mặt hình học lại trông hệt như một **chiếc ống mỏng ($$\delta$$-tube)** chạy theo một hướng nhất định!
- **Mối liên hệ bất ngờ:** Nếu các gói sóng theo nhiều hướng khác nhau có thể chồng khít lên nhau quá nhiều trong một thể tích bé xíu (tức là tập Kakeya có số chiều nhỏ hơn $$n$$), thì các sóng sẽ giao thoa cộng hưởng quá mạnh, làm sụp đổ hàng loạt ước lượng cơ bản cho biến đổi Fourier và phương trình sóng! Ngược lại, hiểu được hình học của các ống Kakeya chính là chìa khóa cho **xử lý tín hiệu đa chiều, chụp cộng hưởng từ (MRI), truyền sóng và nén dữ liệu**.

---

### Video ngắn: Kim quay trong một deltoid

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/kakeya-deltoid-needle_vi.mp4"></video>
</div>

Một kim dài 1 có thể quay 180° bên trong một deltoid (đường ba mũi nhọn) có diện tích $$\pi/8 \approx 0.39$$, bằng một nửa $$\pi/4 \approx 0.79$$ của đĩa quét ra khi quay kim quanh tâm. Sau này Besicovitch chứng minh diện tích có thể nhỏ tùy ý.


### Tự tay thử: Quay chiếc kim trong deltoid

<div class="mex-explainer" data-mex="kakeya" data-lang="vi"></div>


## 1. Từ cây kim xoay đến tập chứa mọi hướng

**Kakeya (khoảng 1917):** trong mặt phẳng, một miền có thể nhỏ đến đâu mà vẫn cho phép xoay ngược chiều (hoặc chứa) một đoạn thẳng đơn vị theo mọi hướng? Đây là cách phát biểu chính xác câu hỏi về "cây bút chì / cây kim" ở đầu bài.

**Các cải tiến trước khi có "nghịch lý".**  
- Giữ cố định tâm cây kim: kim quét một hình tròn bán kính $$1/2$$, diện tích $$\pi/4$$.  
- Vừa xoay vừa trượt: hình **deltoid** giảm diện tích xuống còn $$\pi/8$$.

![Đĩa vs deltoid]({{ site.baseurl }}/img/chapter_img/kakeya_deltoid_besicovitch_pmt.jpg)

*Hình. Hai cách xoay cây kim: cố định tâm, và vừa xoay vừa trượt (deltoid, diện tích $$\pi/8$$). Chân dung Besicovitch (nguồn: video của Pham Manh Tuyen).*

**Abram Besicovitch** chứng minh rằng có thể làm diện tích **nhỏ tùy ý / bằng không**. Hình dung cách xây dựng qua **cây Perron**: chia tam giác thành nhiều phần, trượt các "hình quạt" chồng lên nhau; khi lặp lại, diện tích tiến về 0 nhưng mọi hướng vẫn còn.

![Cây Perron cut-and-slide]({{ site.baseurl }}/img/chapter_img/kakeya_perron_tree_pmt.jpg)

*Hình. Bước chồng lấn kiểu cây Perron (nguồn: video).*

Theo cách hiểu hiện đại, **tập Kakeya** (còn gọi là **tập Besicovitch**) trong $$\mathbb{R}^n$$ là bất kỳ tập nào chứa một đoạn thẳng đơn vị theo **mọi** hướng. Các đoạn thẳng này **không** cần là những vị trí liên tiếp của một chuyển động liên tục: chỉ cần với mỗi hướng, có *một* đoạn thẳng đơn vị theo hướng đó nằm trong tập.

![Hướng]({{ site.baseurl }}/img/chapter_img/kakeya_needle_directions.svg)

*Hình. Mọi hướng đều xuất hiện, nhưng tập không nhất thiết phải đặc.*

![Sao các hướng Kakeya]({{ site.baseurl }}/img/chapter_img/kakeya_set_directions_pmt.jpg)

*Hình. Nhiều đoạn thẳng đơn vị theo các hướng khác nhau trong một vùng (nguồn: video).*

**Phân biệt (quan trọng).**  
- **Chuyển động của cây kim:** xoay liên tục một đoạn thẳng (tập kim Kakeya).  
- **Tập Besicovitch:** một tập tĩnh chứa mọi hướng cùng lúc.  

Cả hai cùng xoay quanh một chủ đề: độ dày theo hướng.

### Chuyển động liên tục: cây gạt nước (Mathologer)

Câu chuyện trực quan (đoạn thẳng đơn vị được xem như một **cây gạt nước** có độ dày 0):

1. **Dịch chuyển song song (khởi động):** để đi giữa hai vị trí song song, trượt dọc theo đường thẳng (diện tích 0) rồi quét qua một đỉnh ở rất xa; diện tích quét được có thể $$<\varepsilon$$ tùy ý (nhưng không thể bằng 0).  
2. **Các miền cổ điển cho phép xoay 180°:** hình tròn $$\pi/4\approx 0{,}785$$; tam giác đều chiều cao 1, khoảng $$\approx 0{,}577$$; **deltoid** còn nhỏ hơn.  
3. **Cây Perron:** cắt tam giác thành nhiều mảnh mỏng rồi chồng lấn để được một cây có diện tích nhỏ tùy ý.  
4. **Dịch chuyển trên cây và ghép ba cây:** khi bị kẹt trong cây, dùng phép dịch chuyển song song giữa các cạnh gần song song; mỗi cây cho khoảng $$60^\circ$$; ghép **ba cây** sẽ xoay liên tục được **180°**, tạo thành hình **cá Kakeya**. Nhánh càng mịn và hành lang dịch chuyển càng dài thì diện tích quét càng $$<\varepsilon$$.  
5. **Qua giới hạn:** dãy các cây cho một tập **có độ đo bằng không** vẫn chứa đoạn thẳng đơn vị theo mọi hướng, tức là một tập Besicovitch tĩnh; từ đây dẫn đến giả thuyết hiện đại về số chiều (Chương 2, Wang–Zahl, $$n=3$$).

![Chuyển song song]({{ site.baseurl }}/img/chapter_img/kakeya_squeegee_parallel_transfer_mathologer.jpg)

*Hình. Bước khởi động bằng dịch chuyển song song: hai hình quạt nối vị trí xanh lá và vị trí xanh dương (Mathologer).*

![Đĩa, tam giác, deltoid]({{ site.baseurl }}/img/chapter_img/kakeya_disk_triangle_deltoid_mathologer.jpg)

*Hình. Các miền cho chuyển động liên tục: hình tròn, tam giác, deltoid (Mathologer).*

![Cây Perron]({{ site.baseurl }}/img/chapter_img/kakeya_perron_tree_mathologer.jpg)

*Hình. Chồng lấn để tạo cây Perron (Mathologer).*

![Magic transfer]({{ site.baseurl }}/img/chapter_img/kakeya_magic_transfer_mathologer.jpg)

*Hình. Dịch chuyển song song trên cây — [t≈10:32](https://www.youtube.com/watch?v=IM-n9c-ARHU&t=632s).*

![Cá Kakeya 180°]({{ site.baseurl }}/img/chapter_img/kakeya_fish_180_mathologer.jpg)

*Hình. Ghép ba cây thành "cá Kakeya" để xoay 180° (Mathologer).*

---

## 2. Độ đo có thể bằng không, nhưng số chiều vẫn có thể bị buộc phải đầy đủ

Besicovitch: trên mặt phẳng, tập có thể có độ đo bằng không. Nhưng **điểm và đường thẳng** đều có diện tích 0 mà rõ ràng không "cùng cỡ".

**Chiều Minkowski (đếm hộp):** $$N(\varepsilon)\asymp\varepsilon^{-d}$$ khi $$\varepsilon\to 0$$ (đoạn thẳng có $$d=1$$, hình vuông có $$d=2$$; fractal có thể có số chiều không nguyên). **Chiều Hausdorff:** phủ bằng các mảnh có kích thước khác nhau, tinh tế hơn. Giả thuyết Kakeya đòi hỏi tập phải có **số chiều đầy đủ** của không gian chứa nó.

![Minkowski vs Hausdorff]({{ site.baseurl }}/img/chapter_img/kakeya_minkowski_vs_hausdorff_pmt.jpg)

*Hình. Lưới đều (Minkowski) so với các mảnh phủ linh hoạt (Hausdorff); nguồn: video của Pham Manh Tuyen.*

![Measure vs dimension]({{ site.baseurl }}/img/chapter_img/measure_vs_dimension.svg)

### "Số chiều" nghĩa là gì (trước khi nói đến Hausdorff)

**Số chiều** cho biết có bao nhiêu **hướng độc lập** để di chuyển trong một không gian.

- Trên một tờ giấy phẳng (**2 chiều**): ngang và dọc, tức hai hướng độc lập.  
- Trong một căn phòng (**3 chiều**): thêm hướng lên xuống, tức ba chiều.

Mỗi chiều ứng với một hướng độc lập. Trong bài toán Kakeya, số chiều của không gian quyết định độ phức tạp: **2 chiều** đã có điều bất ngờ của Besicovitch (diện tích gần bằng 0); **3 chiều** mở ra cả một loạt ý tưởng về ống và nhiều thang đo, dẫn đến chứng minh sâu sắc của **Wang–Zahl (2025)**.

**Từ đồ vật quen thuộc đến fractal.**

- Sợi dây: đi dọc theo một đường là chạm hết mọi điểm, đó là trực giác về **1 chiều**.  
- Tờ giấy: cần hai hướng (ngang, dọc), tức **2 chiều**.  
- Khối lập phương: thêm hướng lên xuống, tức **3 chiều**.  

Nhưng đường bờ biển hay đường cong bông tuyết nhìn từ xa có thể giống 1 chiều; càng phóng to càng thấy ngoằn ngoèo ở mọi thang đo. **Chiều Hausdorff** mô tả hiện tượng đó bằng cách cho phép số chiều **không nhất thiết là số nguyên**. Ví dụ kinh điển: đường cong **Koch** có chiều Hausdorff khoảng $$1{,}26$$, phức tạp hơn đường thẳng nhưng chưa lấp đầy mặt phẳng.

**Kakeya 3 chiều trong một câu.** Một tập Kakeya trong $$\mathbb{R}^3$$ **có thể** có **thể tích bằng 0**, nhưng giả thuyết (nay là định lý Wang–Zahl) nói rằng chiều Hausdorff của nó vẫn phải bằng **3**. Nói cách khác: không thể "làm mỏng" tập đó để nó chỉ phức tạp như một mặt hay một đường; theo nghĩa Hausdorff, nó vẫn **phức tạp đủ 3 chiều**, dù độ đo Lebesgue có thể bằng 0.

### Phủ bằng các quả cầu nhỏ: ý chính của "số chiều không nguyên"

Thay vì chỉ hỏi "vật này có mấy chiều?", ta hỏi:

> Cần bao nhiêu quả cầu nhỏ bán kính $$r$$ để phủ kín tập khi $$r\to 0$$?

Bảng tỉ lệ (theo kiểu Minkowski, đếm hộp):

| Vật | Thang đo $$r$$ | Số mảnh cần (cỡ) |
|-----|-------------|------------------|
| Đoạn thẳng dài 1 | đoạn dài $$r$$ | $$\sim 1/r = 1/r^{1}$$ |
| Hình vuông cạnh 1 | ô cạnh $$r$$ | $$\sim 1/r^{2}$$ |
| Hình lập phương cạnh 1 | khối cạnh $$r$$ | $$\sim 1/r^{3}$$ |

Nếu tập cần khoảng $$1/r^{d}$$ quả cầu bán kính $$r$$ thì $$d$$ là số chiều. Điều thú vị là $$d$$ **không** nhất thiết là số nguyên; nó có thể là $$1{,}26$$ hay $$2{,}58$$.

**Độ đo Hausdorff** làm ý này chặt chẽ hơn (định nghĩa chính xác từng bước ở mục sau). Đại ý: cộng đường kính (hoặc bán kính) của các mảnh phủ, nâng lên lũy thừa $$s$$, lấy giới hạn khi các mảnh nhỏ dần, rồi tìm **giá trị tới hạn của $$s$$**:

- nếu $$s$$ quá nhỏ, "nội dung $$s$$ chiều" thường **bằng vô cùng**;  
- nếu $$s$$ quá lớn, tổng **tiến về 0**.  

Điểm chuyển tiếp đó là **chiều Hausdorff**. Với Kakeya, ta không chỉ hỏi "tập có lớn (về thể tích) không?" mà hỏi "**ở mọi thang đo**, nó phức tạp đến mức nào?". Đó là lý do kết quả số chiều bằng 3 của Wang–Zahl sâu sắc và đáng chú ý.

### Ví dụ fractal: đường cong Koch (khởi động)

**Đường cong Koch** là fractal kinh điển trong lớp học. Bắt đầu từ một đoạn thẳng đơn vị. Ở mỗi bước, chia mỗi đoạn thành ba phần bằng nhau, bỏ phần giữa và thay bằng hai cạnh còn lại của một tam giác đều. Sau bước 1 có **4** đoạn dài $$1/3$$; sau bước 2 có **16** đoạn dài $$1/9$$; sau bước 3 có **64** đoạn dài $$1/27$$; …

Với một tập tự đồng dạng gồm $$N$$ bản sao thu nhỏ theo tỉ lệ $$r$$, số chiều đồng dạng là nghiệm của

$$
N = \Bigl(\frac{1}{r}\Bigr)^{d} \qquad\text{tức}\qquad d = \frac{\log N}{\log(1/r)}.
$$

Với đường cong Koch, $$N=4$$, $$r=1/3$$, nên

$$
d = \frac{\log 4}{\log 3} \approx 1{,}26186.
$$

Nói đơn giản: gồ ghề hơn đường thẳng, nhưng chưa lấp kín mặt phẳng. **Tập Kakeya** thường không có tính tự đồng dạng gọn gàng như vậy, nên phải dùng định nghĩa phủ Hausdorff tổng quát chứ không chỉ công thức logarit. Đây là một lý do khiến Kakeya khó và sâu hơn nhiều so với việc tính số chiều của các fractal cổ điển.

### Chiều Hausdorff, định nghĩa cẩn thận hơn (hàm thước đo)

Các bước chính thức ngắn gọn (dựng lại theo video [CHALK — What is Hausdorff Dimension?](https://www.youtube.com/watch?v=LJcWhcM4okQ); mốc thời gian [`&t=19s`](https://www.youtube.com/watch?v=LJcWhcM4okQ&t=19s)):

**1. Trực giác về phép co giãn.** Phóng to $$\times 2$$: đoạn thẳng thành $$2=2^1$$ bản sao (số chiều $$1$$); hình vuông đặc thành $$4=2^2$$ bản sao (số chiều $$2$$); tam giác Sierpiński thành $$3$$ bản sao, nên số chiều $$=\log_2 3$$. (Cùng ý với bảng phủ và công thức Koch ở trên, nay được trình bày cụ thể hơn.)

![Scaling]({{ site.baseurl }}/img/chapter_img/hausdorff_scaling_intuition_chalk.jpg)

*Hình. Ví dụ về phép co giãn trên bảng (CHALK).*

**2. Đo bằng "thước sai".** Đo hình vuông bằng **độ dài** ($$s=1$$) cho $$\infty$$; bằng **diện tích** ($$s=2$$) cho một số dương hữu hạn; bằng **thể tích** ($$s=3$$) cho $$0$$. Số chiều là giá trị tới hạn của tham số, nơi "độ đo" nhảy $$\infty\to 0$$.

![Đo sai trên vuông]({{ site.baseurl }}/img/chapter_img/hausdorff_wrong_measure_square_chalk.jpg)

*Hình. Đo một hình vuông bằng độ dài, diện tích, thể tích (CHALK).*

**3. Hàm thước đo (gauge function).** $$\varphi\colon[0,\infty)\to[0,\infty)$$, $$\varphi(0)=0$$, không giảm, dương trên $$(0,\infty)$$, liên tục tại $$0$$. Độ dài ứng với $$\varphi(t)=t$$; diện tích ứng với $$t^2$$.

![Gauge]({{ site.baseurl }}/img/chapter_img/hausdorff_gauge_function_def_chalk.jpg)

*Hình. Định nghĩa hàm thước đo (CHALK).*

**4. Độ đo Hausdorff.** Một phủ $$\delta$$ là một phủ bằng các tập có đường kính $$\le\delta$$. Đặt

$$
\mathcal{H}^\delta_\varphi(A)=\inf\Bigl\{\sum_i \varphi\bigl(\mathrm{diam}(C_i)\bigr): \{C_i\}\ \text{phủ }\delta\text{ của }A\Bigr\},
\quad
\mathcal{H}_\varphi(A)=\lim_{\delta\to 0}\mathcal{H}^\delta_\varphi(A).
$$

Với $$\varphi(t)=t^s$$ ta được độ đo Hausdorff $$s$$ chiều $$\mathcal{H}^s$$.

![Outer measure]({{ site.baseurl }}/img/chapter_img/hausdorff_outer_measure_def_chalk.jpg)

*Hình. $$\mathcal{H}^\delta_\varphi$$ (CHALK).*

**5. Giá trị tới hạn của $$s$$ chính là số chiều.**

$$
\dim_H(A)=\inf\{s\ge 0:\ \mathcal{H}^s(A)=0\}=\sup\{s\ge 0:\ \mathcal{H}^s(A)=\infty\}.
$$

![Critical s]({{ site.baseurl }}/img/chapter_img/hausdorff_dimension_critical_s_chalk.jpg)

*Hình. Bước nhảy $$\infty\to 0$$ tại $$s=\dim_H$$ (CHALK).*

**Liên hệ với Kakeya.** Tập Besicovitch có thể có độ đo 0 nhưng $$\dim_H$$ lớn; giả thuyết đòi $$\dim_H=\dim_M=n$$. Davies (1971): mọi tập Kakeya trong mặt phẳng đều có $$\dim_H=2$$, dù độ đo bằng 0.

### Ước lượng $$\dim_H$$: chặn trên và nguyên lý phân bố khối lượng

Tính trực tiếp $$\mathcal{H}^s$$ rất khó; trong thực tế người ta **ước lượng**. Video kèm theo: [CHALK — Estimating Hausdorff Dimension](https://www.youtube.com/watch?v=FQXbRGmAbUY) (khoảng 9,4 phút).

**Chặn trên (đếm số mảnh phủ).** Nếu $$A$$ được phủ bởi $$N_k$$ tập có đường kính $$\le\delta_k$$, với $$\delta_k\to 0$$, thì

$$
\dim_H(A)\ \le\ \liminf_{k\to\infty}\frac{\log N_k}{-\log \delta_k}.
$$

Phác thảo: $$\mathcal{H}^{\delta_k}_s(A)\le N_k\delta_k^s$$; nếu $$s$$ lớn hơn giới hạn dưới trên thì $$N_k\delta_k^s\to 0$$, suy ra $$\mathcal{H}^s=0$$.

![Chặn trên]({{ site.baseurl }}/img/chapter_img/hausdorff_upper_bound_cover_chalk.jpg)

*Hình. Chặn trên bằng số mảnh phủ (CHALK).*

**Chặn dưới (nguyên lý phân bố khối lượng, Mass Distribution Principle).** Giả sử có độ đo $$\mu$$ trên $$A$$ với $$0<\mu(A)<\infty$$, và $$\mu(U)\le C(\mathrm{diam}\,U)^s$$ với mọi $$U$$ đủ nhỏ. Khi đó $$\mathcal{H}^s(A)\ge\mu(A)/C>0$$, suy ra $$\dim_H(A)\ge s$$.

![MDP phát biểu]({{ site.baseurl }}/img/chapter_img/hausdorff_mdp_statement_chalk.jpg)

*Hình. Giả thiết của nguyên lý phân bố khối lượng (CHALK).*

![MDP chứng minh]({{ site.baseurl }}/img/chapter_img/hausdorff_mdp_proof_chalk.jpg)

*Hình. Kết luận của nguyên lý phân bố khối lượng (CHALK).*

**Trong lý thuyết Kakeya.** Chặn trên $$\dim\le n$$ là dễ (do không gian chứa tập). Phần khó là **chặn dưới** (Wolff, Bourgain, trường hợp "dính", Wang–Zahl với số chiều $$=3$$). Nguyên lý phân bố khối lượng và bổ đề Frostman là công cụ chuẩn.

---

## 3. Giả thuyết

**Giả thuyết (tập Kakeya).** Mọi tập Kakeya $$K\subset\mathbb{R}^n$$ đều thỏa mãn $$\dim_H(K)=\dim_M(K)=n$$.

| $$n$$ | Tình trạng |
|-------|------------|
| 1 | Hiển nhiên (tập chứa một đoạn thẳng đơn vị đã có 1 chiều) |
| 2 | Đã chứng minh (Davies, 1971) |
| 3 | Đã chứng minh (**Wang–Zahl**, 2025) |
| $$\ge 4$$ | Còn mở (đã có một số chặn dưới) |

<div class="textbook-theorem" markdown="1">
**Định lý (Wang–Zahl, 2025).** Mọi tập Kakeya trong $$\mathbb{R}^3$$ đều có chiều Hausdorff và chiều Minkowski bằng 3.  
Nguồn: [arXiv:2502.17655](https://arxiv.org/abs/2502.17655) (*Volume estimates for unions of convex sets…*).
</div>

Các tác giả **không** khẳng định thể tích dương. Độ đo bằng không vẫn tương thích với số chiều bằng 3; đó là ý chính mà cả bài muốn truyền đạt.

![Wang–Zahl 2025]({{ site.baseurl }}/img/chapter_img/kakeya_wang_zahl_2025_pmt.jpg)

*Hình. Khung hình từ video phổ thông: $$\dim_H(K)=\dim_M(K)=3$$ trong $$\mathbb{R}^3$$ (nguồn: Pham Manh Tuyen; nguồn gốc là bài trên arXiv).*

---

## 4. Vì sao 3 chiều khó: các ống bán kính $$\delta$$

**Vì sao các nhà giải tích lại "thổi phồng" đoạn thẳng thành ống?**
Một đoạn thẳng toán học có độ dày bằng 0 nên rất khó áp dụng các công cụ tích phân và thể tích. Để đưa bài toán về phạm vi giải tích, người ta làm "phình" mỗi đoạn thẳng đơn vị thành một **ống trụ ($$\delta$$-tube)** dài 1 và bán kính $$\delta$$ rất nhỏ.

Hãy thử làm một phép đếm trực giác ngay trong không gian 3 chiều $$\mathbb{R}^3$$:
- Một ống có thể tích cỡ $$\pi \delta^2 \cdot 1 \sim \delta^2$$.
- Trên mặt cầu đơn vị 2 chiều biểu diễn các hướng trong $$\mathbb{R}^3$$, ta có thể chọn khoảng $$\delta^{-2}$$ hướng phân biệt (cách nhau ít nhất một góc $$\delta$$).
- Nếu $$\delta^{-2}$$ chiếc ống ấy **hầu như không chồng lên nhau**, tổng thể tích của chúng sẽ cỡ $$\delta^{-2} \cdot \delta^2 = 1$$ (tương ứng chiều Minkowski bằng 3)!

![δ-tube]({{ site.baseurl }}/img/chapter_img/kakeya_delta_tubes.svg)

*Hình. Các ống chồng lên nhau nhiều là khó khăn chính về mặt giải tích.*

Bài toán Kakeya 3 chiều quy về việc chứng minh: dù bạn có khéo léo sắp đặt đến đâu, hợp của $$\delta^{-2}$$ chiếc ống theo các hướng khác nhau ấy cũng **không thể** bị nén chặt thành một thể tích nhỏ cỡ $$\delta^{\alpha}$$ với $$\alpha > 0$$ (nó chỉ có thể co nhẹ cỡ $$(\log(1/\delta))^{-c}$$ hay nhỏ hơn bất kỳ lũy thừa $$\delta^\varepsilon$$ nào).

Các ống chỉ có thể chồng lên nhau **rất nhiều** khi chúng buộc phải mang một **cấu trúc hình học đặc biệt** (ví dụ tụ lại thành từng cụm gần như phẳng hoặc "dính" vào nhau ở nhiều thang đo); các lập luận nhiều thang đo biến chính cấu trúc ép buộc đó thành chặn thể tích tốt hơn (**tự cải thiện**, *self-improvement*). Bài báo của Wang–Zahl dài khoảng **127 trang** về phần hình học tinh vi này, hoàn toàn không phải một mẹo ngắn.

**Kakeya "dính"** (*sticky Kakeya*; Wang–Zahl, *J. Amer. Math. Soc.* 2026; công trình trung gian năm 2022) là một trường hợp có cấu trúc quan trọng: các ống "dính" với nhau theo cách kiểm soát được ở nhiều thang đo. Đây là bước đệm quyết định trước khi chứng minh số chiều đầy đủ trong 3 chiều.

**Tóm tắt.** Đoạn thẳng → ống mỏng → chặn thể tích của hợp → cấu trúc nhiều thang đo → số chiều. Ở mỗi mũi tên, chứng minh có thể thất bại nếu không kiểm soát được những cách chồng lấn "bất thường".

---

## 5. Vì sao giải tích điều hòa quan tâm

Kakeya không phải một câu đố hình học đứng riêng. Cách các ống theo nhiều hướng sắp xếp với nhau chi phối:

- **bài toán hạn chế Fourier** (Fourier restriction) và các gói sóng;  
- **làm trơn cục bộ** (local smoothing) cho phương trình sóng;  
- các bài toán về khoảng cách và bài toán kiểu Furstenberg trong lý thuyết độ đo hình học.

Trích dẫn giải Fields của Wang nêu rõ phương pháp tách (decoupling) và nhiều thang đo cho làm trơn cục bộ trong mặt phẳng, bài toán hạn chế, Falconer, Furstenberg và Kakeya 3 chiều ([PDF của IMU](https://www.mathunion.org/fileadmin/documents/2026-07/Hong_Wang_Citations.pdf)).

![Tới HA]({{ site.baseurl }}/img/chapter_img/kakeya_to_harmonic_analysis.svg)

*Hình. Từ hình học của các ống đến các chủ đề Fourier và phương trình đạo hàm riêng.*

### "Tháp" các giả thuyết (theo cách trình bày phổ thông)

Video của [Quanta Magazine](https://www.youtube.com/watch?v=5J3tYU_-IZI) (phỏng vấn **Tao**, **Hickman**, **Wang**, **Zahl**) đặt Kakeya ở **đáy tháp** của giải tích điều hòa hiện đại:

1. **Giả thuyết Kakeya** (hình học của các hướng và các ống).  
2. **Bài toán hạn chế Fourier**: biến đổi Fourier trên mặt cong (ví dụ mặt cầu) hoạt động thế nào.  
3. **Bochner–Riesz**: "làm mịn" phần biên của tín hiệu bằng phương pháp Fourier.  
4. **Làm trơn cục bộ**: kiểm soát định lượng sự **lan truyền của sóng** (phương trình đạo hàm riêng).

Nếu Kakeya sai ở một số chiều nào đó, nhiều tầng phía trên sẽ sụp theo. Nếu các phương pháp cho Kakeya hiệu quả, chúng có thể giúp **leo lên các tầng trên**. Vì vậy định lý Wang–Zahl trong 3 chiều không chỉ là một kết quả hình học lý thú: nó thường được mô tả là đột phá lớn nhất của giải tích điều hòa trong khoảng hai thập niên.

**Bước ngoặt lịch sử (Fefferman).** Vào thập niên 1970, **Charles Fefferman** đưa hình học kiểu Kakeya vào trung tâm của giải tích, qua mối liên hệ với biến đổi Fourier nhiều chiều (bài toán nhân đĩa — ball multiplier). Đó là cây cầu sớm giữa "tập kim" và biến đổi Fourier.

![Restriction]({{ site.baseurl }}/img/chapter_img/kakeya_tower_restriction_quanta.jpg)

*Hình. Tầng bài toán hạn chế (Quanta).*

![Bochner–Riesz]({{ site.baseurl }}/img/chapter_img/kakeya_tower_bochner_riesz_quanta.jpg)

*Hình. Tầng Bochner–Riesz (Quanta).*

![Local smoothing]({{ site.baseurl }}/img/chapter_img/kakeya_tower_local_smoothing_quanta.jpg)

*Hình. Làm trơn cục bộ và sóng (Quanta).*

### Ý tưởng của chứng minh năm 2025 (tóm tắt)

- Các ống trong 3 chiều "tránh" nhau nhiều hơn các hình chữ nhật trong 2 chiều.  
- **Kakeya "dính"** (2022) là bước đệm.  
- **Cấu trúc hạt** (graininess; Guth…): khi bị nén cực mạnh, các ống tạo thành những "hạt".  
- **Quy nạp theo thang đo** nâng dần chặn dưới của số chiều lên đến 3 (phải kiểm soát sự "thất thoát" tích lũy qua nhiều bước, giống trò chơi truyền tin).  
- Trường hợp $$n\ge 4$$ vẫn còn mở.

![Grains]({{ site.baseurl }}/img/chapter_img/kakeya_grains_induction_quanta.jpg)

*Hình. Cấu trúc hạt và nhiều thang đo (Quanta).*

---

## 6. Vị trí trong khóa học

| Vị trí | Vai trò |
|--------|---------|
| **Chương 1 (trang này)** | Tổng quan về bài toán: phát biểu, tình trạng, vì sao khó, các liên hệ |
| **Chương 2, bài về Wang** | Bài giảng đầy đủ: lịch sử, các ống, phác thảo chiến lược chứng minh, các công trình, bài tập |
| **Chương 7, khám phá Kakeya** | Đề bài thực hành: vẽ, lập trình, định nghĩa lại thế nào là "nhỏ" |
| **Chương 2, bài tổng quan (tổ hợp)** | Các bài toán họ hàng về hình học liên thuộc |

Thứ tự đọc gợi ý: bài tổng quan này → bài chính về Wang → bài thực hành.

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|-----|
| "Tập Kakeya phải có thể tích dương." | Sai | Độ đo vẫn có thể bằng không; giả thuyết nói về **số chiều**. |
| "Một mình Wang giải Kakeya 3 chiều." | Sai | Đây là công trình chung với **Joshua Zahl**. |
| "Giả thuyết đã được giải cho mọi số chiều." | Sai | $$n\ge 4$$ vẫn còn **mở**. |
| "Chuyển động liên tục của cây kim chính là tập Besicovitch." | Sai | Hai khái niệm liên quan nhưng **không** giống nhau. |
| "Wang được giải Fields chỉ nhờ Kakeya." | Sai | IMU còn nêu làm trơn cục bộ, bài toán hạn chế, Falconer, Furstenberg. |

---

## Bài tập

1. Định nghĩa tập Kakeya trong $$\mathbb{R}^n$$ bằng một câu.  
2. Kết quả của Davies phù hợp thế nào với việc tập Besicovitch có độ đo bằng không?  
3. Viết $$\dim_H(A)$$ dưới dạng inf/sup theo $$\mathcal{H}^s$$; giải thích bước nhảy "$$\infty\to 0$$" với hình vuông đặc.  
4. Phát biểu chặn trên bằng số mảnh phủ và nguyên lý phân bố khối lượng (mỗi cái một câu).  
5. Phác thảo lý do vì sao trong giải tích người ta dùng ống thay cho đoạn thẳng.  
6. Kể ba tầng của "tháp" giải tích điều hòa phía trên Kakeya (bài toán hạn chế, Bochner–Riesz, làm trơn cục bộ).  
7. Viết lại bảng tình trạng cho $$n=1,2,3,\ge 4$$ mà không nhìn bài.  
8. Mở bài về Wang ở Chương 2 và trích câu tóm tắt về lập luận tự cải thiện.  
9. Đọc hiểu: đọc phần tóm tắt của arXiv:2502.17655; diễn đạt lại ước lượng thể tích bằng lời.  
10. Khám phá: thử đề bài "tập Kakeya nhỏ nhất" ở Chương 7 trong 30 phút; ghi lại một điều làm bạn bất ngờ.

---

## Video phổ thông (nguồn)

Dùng để có **trực giác**; định lý chính xác xem bài về Wang ở Chương 2 và bài trên arXiv.

### ★ Câu chuyện năm 2025 (tiếng Anh, Quanta): nên xem trước

- **Nguồn:** [A Once-in-a-Century Proof: The Kakeya Conjecture — Quanta](https://www.youtube.com/watch?v=5J3tYU_-IZI) (khoảng 15 phút; 2026-08-03).  
  Cây kim → Besicovitch → Davies → Fefferman và Fourier → tháp bài toán hạn chế / Bochner–Riesz / làm trơn cục bộ → trường hợp "dính" và cấu trúc hạt → Wang–Zahl 3 chiều.  
  Bài viết: [Quanta 2025-03-14](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/).  
  *Lưu ý:* một số hình minh họa về chiều Hausdorff trong video có lỗi đã được đính chính; định nghĩa chính xác hãy dùng video của CHALK.

### A. Chiều Hausdorff, định nghĩa chính xác (tiếng Anh, CHALK, phần 1)

- **Nguồn:** [What is Hausdorff Dimension? — CHALK](https://www.youtube.com/watch?v=LJcWhcM4okQ) (khoảng 13,3 phút; 2026-08-03).  
  Phép co giãn → đo bằng "thước sai" → hàm thước đo → $$\mathcal{H}^\delta_\varphi$$ → $$\mathcal{H}^s$$ → $$s=\dim_H$$.  
  Mốc thời gian **[t≈0:19](https://www.youtube.com/watch?v=LJcWhcM4okQ&t=19s)**. Tương ứng với mục "Chiều Hausdorff, định nghĩa cẩn thận hơn".

### A′. Ước lượng chiều Hausdorff (tiếng Anh, CHALK, phần 2)

- **Nguồn:** [Methods for Estimating Hausdorff Dimension / MDP — CHALK](https://www.youtube.com/watch?v=FQXbRGmAbUY) (khoảng 9,4 phút; 2026-08-03).  
  Chặn trên bằng $$N_k,\delta_k$$; **nguyên lý phân bố khối lượng** cho chặn dưới. Tương ứng với mục "Ước lượng $$\dim_H$$".

### B. Xây dựng chuyển động liên tục (tiếng Anh, Mathologer)

- **Nguồn:** [The Kakeya needle problem (squeegee) — Mathologer](https://www.youtube.com/watch?v=IM-n9c-ARHU) (khoảng 16,8 phút; 2026-08-03).  
  Video tốt nhất về **xoay cây kim liên tục**: dịch chuyển song song → hình tròn, tam giác, deltoid → cây Perron → cá ghép từ ba cây → giới hạn có độ đo bằng không.  
  Mốc thời gian **[t≈10:32](https://www.youtube.com/watch?v=IM-n9c-ARHU&t=632s)**: dịch chuyển song song trên cây.  
  Phần mô tả của video dẫn đến bài tổng quan của Terry Tao (để đọc sâu về lý thuyết độ đo hình học và giải tích điều hòa).

### C. Giải thích hình học bằng tiếng Việt (Minkowski, Hausdorff)

- **Nguồn:** [Giả Thuyết Kakeya… | Pham Manh Tuyen](https://www.youtube.com/watch?v=XUkfpgFakMQ) (khoảng 15 phút; 2026-08-03).  
  Các mốc: Fields 2026; hình tròn và deltoid; cây Perron; định nghĩa tập; đếm hộp → Hausdorff; Davies và trường hợp 3 chiều; Wang–Zahl và trường hợp $$n\ge 4$$ còn mở.

### D. Video ngắn (lịch sử các chặn dưới, tiếng Việt)

- **Nguồn:** [Phỏng Đoán Kakeya… | TOÁN PRO](https://www.youtube.com/watch?v=pxVMKoZsVc8) (khoảng 8,7 phút; 2026-08-03).  
  Bắt đầu từ **t=3:38** (`&t=218s`): Besicovitch; sau đó Wolff và Bourgain → trường hợp "dính" → 2025.

![Diện tích tiến về 0]({{ site.baseurl }}/img/chapter_img/kakeya_area_to_zero_toanpro.jpg)

*Hình. Diện tích $$A\to 0$$ mà vẫn giữ mọi hướng (TOÁN PRO).*

![Besicovitch giải diện tích 2D]({{ site.baseurl }}/img/chapter_img/kakeya_besicovitch_solved_toanpro.jpg)

*Hình. Mốc Besicovitch (TOÁN PRO, khoảng t=3:38).*

![Bourgain và cuộc đua chặn dưới]({{ site.baseurl }}/img/chapter_img/kakeya_bourgain_toanpro.jpg)

*Hình. Bourgain (TOÁN PRO).*

**Lưu ý (cả hai video).** Phụ đề tự động hay viết sai tên và năm (Kakja, 1977 thay vì 1917, Hous Dof, Minsky, Josu, Furier…). Hãy dùng tên chuẩn: **Kakeya (1917)**, **Besicovitch**, **Hausdorff**, **Minkowski**, **Davies**, **Wolff**, **Bourgain**, **Joshua Zahl**, **Hong Wang**, **Fourier**.

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Các video phổ thông ở trên đã được xếp theo thứ tự nên xem. Bộ tư liệu đầy đủ (mọi URL, bảng tình trạng, lộ trình học): `research/video-research/Kakeya_Conjecture/`.

**Nhắc lại tình trạng (2026):** giả thuyết *tập* Kakeya trong 3 chiều **đã được chứng minh** (Wang–Zahl 2025); với $$n\ge 4$$ và với dạng hàm cực đại mạnh hơn, phần lớn vẫn **còn mở**. Video giúp có trực giác và hiểu bối cảnh, không thay thế bài ở Chương 2 hay bài trên arXiv.

---



### Phụ đề và khung hình (trích từ video chính)

Phụ đề và các đoạn theo thời gian: `research/video-research/Kakeya_Conjecture/transcripts/` · trạng thái: `research/video-research/Kakeya_Conjecture/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Phụ đề được tải tự động (yt-dlp), chỉ dùng để tra cứu, **không** thay thế nội dung bài.


![Frame mẫu video flagship]({{ site.baseurl }}/img/video_research/flagships/kakeya_quanta_frame01.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo

Danh sách URL: `research/video-research/Kakeya_Conjecture/references.md`.

### Bài báo và blog

1. Wang–Zahl — [arXiv:2502.17655](https://arxiv.org/abs/2502.17655); trường hợp "dính" [arXiv:2210.09581](https://arxiv.org/abs/2210.09581).  
2. Tao — [blog về Kakeya 3 chiều](https://terrytao.wordpress.com/2025/02/25/the-three-dimensional-kakeya-conjecture-after-wang-and-zahl/); [ghi chú năm 2014 về tính "dính"](https://terrytao.wordpress.com/2014/05/07/stickiness-graininess-planiness-and-a-sum-product-approach-to-the-kakeya-problem/).  
3. Davies 1971; trích dẫn giải Fields 2026 của IMU cho Wang.  

### Video và tin tức

4. Video của Quanta: https://www.youtube.com/watch?v=5J3tYU_-IZI · [bài viết](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/)  
5. Mathologer: https://www.youtube.com/watch?v=IM-n9c-ARHU  
6. CHALK Hausdorff: https://www.youtube.com/watch?v=LJcWhcM4okQ · MDP: https://www.youtube.com/watch?v=FQXbRGmAbUY  
7. VI: https://www.youtube.com/watch?v=XUkfpgFakMQ · https://www.youtube.com/watch?v=pxVMKoZsVc8  
8. IAS Ideas: https://www.ias.edu/ideas/three-dimensional-breakthrough  
9. Wikipedia — [Kakeya set](https://en.wikipedia.org/wiki/Kakeya_set)  

### Trong khóa học

10. [Bài về Wang, Chương 2]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/); [Khám phá Kakeya]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/). Bộ tư liệu: `research/video-research/Kakeya_Conjecture/`.

---

## Hướng đi tiếp

**Tiếp tục lộ trình A**

1. Đã xong: bài tổng quan ở Chương 1 (trang này).  
2. **Tiếp theo →** [Bài về Wang, Chương 2]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/).  
3. **Sau đó →** [Bài thực hành Kakeya, Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/).  

Không bắt buộc: [CHALK về chiều Hausdorff](https://www.youtube.com/watch?v=LJcWhcM4okQ&t=19s) và [CHALK về nguyên lý phân bố khối lượng](https://www.youtube.com/watch?v=FQXbRGmAbUY); [Mathologer, cây gạt nước](https://www.youtube.com/watch?v=IM-n9c-ARHU&t=632s); [Pham Manh Tuyen](https://www.youtube.com/watch?v=XUkfpgFakMQ) hoặc [TOÁN PRO](https://www.youtube.com/watch?v=pxVMKoZsVc8).  
- So sánh với [lộ trình B về định lý Bốn màu]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/).

## Video tham khảo

- **Xem trước:** [The Kakeya needle problem (the squeegee approach)](https://www.youtube.com/watch?v=IM-n9c-ARHU) — Mathologer, tiếng Anh. Trình bày cách xoay cây kim trong miền có diện tích nhỏ tùy ý (cây Perron, ghép ba cây); nên xem trước khi đọc bài.
- [What is Hausdorff Dimension? Intuition, Gauge Functions, and Hausdorff Measures](https://www.youtube.com/watch?v=LJcWhcM4okQ) — CHALK, tiếng Anh. Định nghĩa chiều Hausdorff qua hàm thước đo và độ đo Hausdorff; nên xem sau khi đã nắm ý chính của bài.
- [Methods for Estimating Hausdorff Dimension: Bounds and The Mass Distribution Principle](https://www.youtube.com/watch?v=FQXbRGmAbUY) — CHALK, tiếng Anh. Xem thêm sau hai video trên; cách chặn trên và chặn dưới chiều Hausdorff.
