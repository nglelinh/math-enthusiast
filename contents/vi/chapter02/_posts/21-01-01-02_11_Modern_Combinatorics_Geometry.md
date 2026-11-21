---
layout: post
title: "June Huh và Tổ hợp–Hình học Hiện đại (Huy chương Fields 2022)"
chapter: '02'
order: 15
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Bài khảo sát này làm hai việc. Thứ nhất, đây là **bản đồ phương pháp**: nó cho thấy các ý tưởng rời rạc (đồ thị, quan hệ liên thuộc, tính mở rộng, đa thức) gặp gỡ hình học, giải tích và lý thuyết số như thế nào. Thứ hai, đây là nơi Chương 2 giới thiệu **June Huh** và **Huy chương Fields 2022**. Lời trao giải ghi nhận việc ông đưa ngôn ngữ của lý thuyết Hodge vào tổ hợp: tính lõm loga cho matroid, giả thuyết Dowling–Wilson, giả thuyết Heron–Rota–Welsh, đa thức Lorentz, giả thuyết Mason dạng mạnh. Tuy vậy, bài không biến cả một lĩnh vực rộng thành tiểu sử của một người.

Nếu các bài về Maynard, Green–Tao, Viazovska, Wang giống những đỉnh núi riêng lẻ, thì tổ hợp và hình học hiện đại là **dãy núi nối chúng lại**. Công trình của Huh là một đỉnh đại số–hình học trên cùng dãy núi đó: matroid ra đời từ các tiên đề rời rạc về tính độc lập, rồi bất ngờ lại có một "bộ cấu trúc Hodge". Bạn không cần học hết mọi định lý. Điều cần là nhận ra *cùng một họ câu hỏi*: các cấu hình rời rạc tương tác với không gian liên tục như thế nào, và một chứng minh thuộc về "thế giới" nào (tổ hợp, Fourier, đa thức, phổ, tính dương).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Kể ra **năm cầu nối** giữa tổ hợp và hình học/giải tích: tổ hợp cộng tính; hình học liên thuộc; tính mở rộng và phổ; phương pháp đa thức; bổ đề chính quy và mật độ.
- Đặt tổ hợp cộng tính bên cạnh [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) và phương pháp sàng của [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/) mà không lẫn lộn công cụ.
- Thấy hình học liên thuộc có họ hàng với bài toán hạn chế (restriction) và [Kakeya–Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/).
- Giải thích ý **cấu trúc và ngẫu nhiên** (structure versus randomness) trong tổ hợp cộng tính.
- Dùng trang này như **mục lục** dẫn sang chương Khám phá và các bài Fields liên quan.
- Đặt **June Huh** (Fields 2022) lên bản đồ: tính dương kiểu Hodge cho matroid, cùng với Adiprasito, Katz và các cộng sự trong lý thuyết đa thức Lorentz.
- Đưa ra một ví dụ "phát biểu tổ hợp, chứng minh hình học" và một ví dụ theo chiều ngược lại.

**Kiến thức cần có.** Đồ thị cơ bản; tập hợp và phép đếm; trực giác về không gian Euclid; Fourier ở mức "tần số".

**Liên hệ với khóa học.** Bài này phục vụ mục tiêu về bề rộng của toán học hiện đại. Đây là bài *tổng hợp*, không đi sâu vào một định lý.

---

## 1. Câu hỏi chung: rời rạc gặp liên tục

Nhiều bài toán trông có vẻ "rời rạc":

- Tập $$A\subset\mathbb{Z}$$ hoặc $$A\subset\mathbb{F}_p$$ có bao nhiêu cấp số cộng?
- $$n$$ điểm và $$m$$ đường thẳng trên mặt phẳng tạo ra bao nhiêu **liên thuộc** (incidence), tức là cặp (điểm, đường) mà điểm nằm trên đường?
- Một đồ thị thưa có thể có **tính mở rộng** (expander) mạnh đến mức nào?
- Giao của các siêu mặt đại số có bao nhiêu điểm?

Nhưng các chứng minh hiện đại thường mượn:

- các bất đẳng thức giải tích và Fourier;
- hình học đại số trên $$\mathbb{R}$$ hoặc trên trường hữu hạn;
- lý thuyết ergodic và giới hạn của đồ thị;
- tối ưu lồi, quy hoạch nửa xác định (trong một số nhánh của khoa học máy tính lý thuyết).

Theo chiều ngược lại, hình học và giải tích "thuần túy" ngày càng dùng các ví dụ cực trị tổ hợp để kiểm tra độ sắc của kết quả: các họ ống Kakeya, cấu hình điểm–đường cực đại, lưới xếp cầu.

**Ý chính của khóa học.** *Ở biên giới nghiên cứu ngày nay, các lĩnh vực hiếm khi tách biệt; bộ công cụ luôn đến từ nhiều ngành.*

---

## 2. Tổ hợp cộng tính: cấu trúc hay ngẫu nhiên?

**Tổ hợp cộng tính** nghiên cứu các tập hợp đối với phép cộng (đôi khi cả phép nhân): tập tổng

$$
A+A=\{a+a':a,a'\in A\},
$$

cấp số cộng, tiến trình số học tổng quát, nhóm xấp xỉ, và các định lý kiểu Freiman–Ruzsa mô tả những tập "có cấu trúc cộng tính".

### 2.1. Mật độ và định lý Szemerédi

Nếu $$A\subset\{1,\ldots,N\}$$ có mật độ dương, **định lý Szemerédi** bảo đảm $$A$$ chứa cấp số cộng dài tùy ý. Đây là một định lý tổ hợp sâu, có nhiều cách chứng minh (tổ hợp, ergodic, Fourier, bổ đề chính quy cho siêu đồ thị…).

### 2.2. Mật độ bằng 0 vẫn có cấu trúc: Green–Tao

Tập số nguyên tố có mật độ 0 nhưng vẫn chứa cấp số cộng với mọi độ dài ([Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/)), nhờ **nguyên lý chuyển** (transference) và một hàm trội giả ngẫu nhiên. Bài học về phương pháp: *một định lý về mật độ có thể được "chuyển" sang một tập thưa, nếu tập thưa đó trông đủ ngẫu nhiên.*

### 2.3. Cấu trúc và ngẫu nhiên

Nhiều chứng minh tách một tập hoặc một hàm thành:

- phần **có cấu trúc** (tần số lớn, tương quan với tiến trình số học, gần với nhóm số học);
- phần **giả ngẫu nhiên** (hệ số Fourier nhỏ, chuẩn Gowers nhỏ…).

Phần có cấu trúc được xử lý bằng phân loại; phần ngẫu nhiên được ước lượng bằng bất đẳng thức. Đây là một triết lý chung, không chỉ là một bổ đề.

### 2.4. Bên cạnh Maynard

[Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/) cũng nghiên cứu các cấu hình số nguyên tố, nhưng công cụ là **phương pháp sàng** trên các dạng tuyến tính, không phải định lý Szemerédi tương đối. Cùng là số nguyên tố, nhưng công cụ khác nhau. Bản đồ tổ hợp–số học cần cả hai.

---

## 3. Hình học liên thuộc: điểm, đường thẳng, ống

**Câu hỏi mẫu.** Cho $$P$$ là một tập điểm và $$L$$ là một tập đường thẳng trong $$\mathbb{R}^2$$. Số liên thuộc

$$
I(P,L)=\#\{(p,\ell):p\in P,\;p\in\ell\}
$$

lớn nhất bằng bao nhiêu, tính theo $$|P|$$ và $$|L|$$?

**Định lý Szemerédi–Trotter** (và các biến thể) cho một chặn sắc dạng

$$
I(P,L)\lesssim |P|^{2/3}|L|^{2/3}+|P|+|L|
$$

(sai khác một hằng số). Ý nghĩa: không thể có chuyện mọi điểm đều nằm trên rất nhiều đường thẳng trong khi các đường thẳng vẫn "độc lập" theo nghĩa cực trị.

### 3.1. Phân hoạch đa thức và Guth–Katz

Trong những thập niên gần đây, **phương pháp phân hoạch đa thức** (polynomial partitioning) cho phép chia không gian thành các ô bằng tập không điểm của một đa thức, rồi kiểm soát số liên thuộc trong từng ô và trên mặt đại số. **Guth–Katz** giải bài toán khoảng cách của Erdős trên mặt phẳng bằng công cụ kiểu này; đây là ví dụ tiêu biểu cho việc "hình học đại số giúp giải bài toán tổ hợp".

### 3.2. Họ hàng với Kakeya và bài toán hạn chế

Việc đếm ống, tấm mỏng và liên thuộc trong không gian nhiều chiều gắn chặt với bài toán **Kakeya** và bài toán **hạn chế** (restriction) trong giải tích điều hòa: xem [Wang / Kakeya]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/). Trực giác chung: *không thể nén quá nhiều hướng khác nhau vào một tập nhỏ*, dù ta diễn đạt bằng độ đo, bằng Fourier hay bằng cách đếm ống rời rạc.

**Bài học khi chuyển ngôn ngữ.** Cùng một hình học về "hướng và tập mỏng", một bên là giả thuyết về độ đo, một bên là bất đẳng thức đếm.

---

## 4. Tính mở rộng: đồ thị thưa nhưng liên thông mạnh, và phổ

Một đồ thị **mở rộng** (expander) có nhiều đỉnh, bậc bị chặn (hoặc thưa), nhưng có hằng số Cheeger hoặc khe phổ tốt: mọi tập đỉnh không quá lớn đều có biên tương đối lớn. Trực giác: *không có chỗ thắt cổ chai*, nên thông tin và đường đi lan truyền nhanh.

### 4.1. Khe phổ như một bất biến hình học

Ma trận kề hoặc ma trận Laplace chuẩn hóa có các giá trị riêng; khoảng cách từ giá trị riêng tầm thường đến giá trị riêng kế tiếp đo tính mở rộng. Đây là **hình học phổ** của đồ thị, cầu nối giữa tổ hợp, lý thuyết nhóm và giải tích trên không gian rời rạc.

### 4.2. Đồ thị mở rộng nhiều chiều

Ta có thể mở rộng khái niệm lên phức đơn hình: tính mở rộng không chỉ xét trên đồ thị (1 chiều) mà cả trên các mặt, các khối… **Các phức mở rộng nhiều chiều** (high-dimensional expanders) xuất hiện trong khoa học máy tính lý thuyết (PCP, lấy mẫu, mã hóa) và trong toán thuần túy (tôpô, lý thuyết nhóm). Ý chính: *thưa nhưng vẫn liên thông mạnh theo nghĩa đối đồng điều hoặc phổ*.

### 4.3. Vì sao xếp vào "hình học"

Đồ thị mở rộng là phiên bản rời rạc của ý "cong âm" hay "trộn nhanh". Nhiều cách xây dựng dùng nhóm số học và đồ thị Cayley; đây lại là một cầu nối giữa số học và tổ hợp.

---

## 5. Phương pháp đại số: dùng đa thức để chứng minh kết quả tổ hợp

### 5.1. Định lý không điểm tổ hợp

**Alon** (và các biến thể): nếu đa thức $$f$$ có hệ số thích hợp, thì $$f$$ không thể triệt tiêu trên toàn bộ tích $$A_1\times\cdots\times A_n$$ khi các $$|A_i|$$ đủ lớn so với bậc. Hệ quả: tồn tại một điểm trong lưới tổ hợp tại đó đa thức khác 0, và điều này được dùng để chứng minh sự tồn tại của các cấu hình.

### 5.2. Phương pháp đa thức (Dvir; Guth–Katz; …)

**Dvir** chứng minh bài toán Kakeya trên trường hữu hạn với ý tưởng: nếu một tập Kakeya quá nhỏ thì có một đa thức bậc thấp triệt tiêu trên nó, và điều đó mâu thuẫn với việc tập chứa đường thẳng theo mọi hướng. **Guth–Katz** và các công trình về liên thuộc dùng đa thức trên $$\mathbb{R}$$ cùng với phân hoạch. Thông điệp:

> Hình học đại số trên một trường (hữu hạn hoặc $$\mathbb{R}$$) có thể chứng minh những phát biểu **thuần túy về đếm**.

Đây là một "cầu nối bất ngờ" đúng tinh thần Chương 2: công cụ tưởng thuộc về lĩnh vực này lại giải bài toán của lĩnh vực khác.

### 5.3. June Huh: lý thuyết Hodge khi không có đa tạp (Fields 2022)

**June Huh** nhận **Huy chương Fields 2022** vì đã đưa các ý tưởng của lý thuyết **Hodge** vào tổ hợp: giả thuyết **Dowling–Wilson** cho dàn hình học, giả thuyết **Heron–Rota–Welsh** cho matroid, lý thuyết **đa thức Lorentz**, và giả thuyết **Mason dạng mạnh**. Đây không phải là một mẹo đếm khéo. Đây là việc chuyển *ngôn ngữ của tính dương* (định lý Lefschetz khó, quan hệ Hodge–Riemann, dãy lõm loga) từ đối đồng điều của đa tạp đại số sang những đối tượng không nhất thiết đến từ hình học.

Một **matroid** ghi lại các tiên đề về tính độc lập (ý tưởng của độc lập tuyến tính, nhưng bỏ đi không gian vectơ cụ thể). Từ lâu, người ta đã dự đoán các bất biến số của matroid, nhất là các hệ số của đa thức đặc trưng, có tính **lõm loga** (log-concave), như thể chúng là các số giao của một lớp Kähler. **Adiprasito–Huh–Katz** chứng minh giả thuyết Heron–Rota–Welsh bằng cách xây dựng một "bộ cấu trúc Hodge" tổ hợp trên vành Chow của matroid. Các công trình sau đó (Huh cùng Brändén và những người khác) phát triển **đa thức Lorentz** thành một công cụ giải tích để chứng minh tính lõm loga mà không phải lúc nào cũng cần dựng một đa tạp trước.

**Định lý đã thay đổi điều gì.** Nhà tổ hợp không còn phải xem tính lõm loga của các hệ số đặc trưng như một điều kỳ diệu cần xử lý riêng từng trường hợp. Ý tưởng sau trở nên có cơ sở: *nếu một đối tượng có "bóng dáng Hodge", thì những bất đẳng thức trông giống hình học có thể trở thành định lý*. Các kết quả này **không** phân loại mọi matroid, không chứng minh giả thuyết Hodge, và không thay thế các phần khác của bài tổng hợp này. Công lao thuộc về nhiều người: Adiprasito, Katz, Brändén, cùng truyền thống Rota–Welsh–Stanley–Mason, đều được nhắc cùng với Huh.

### 5.4. Xếp cầu như một bài toán cực trị hình học–giải tích

[Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/) giải bài toán xếp cầu tối ưu bằng Fourier và dạng modular. Đây không phải tổ hợp thuần túy, nhưng thuộc cùng họ **bài toán cực trị hình học**. Bản đồ tổ hợp–hình học nên có một mục "xếp cầu, cực tiểu năng lượng" bên cạnh liên thuộc.

---

## 6. Bổ đề chính quy, giới hạn đồ thị và "thế giới dày đặc"

**Bổ đề chính quy Szemerédi** và lý thuyết **giới hạn đồ thị** (Lovász và cộng sự) cho phép tách một đồ thị dày đặc thành các khối gần như ngẫu nhiên. Đây là nền tảng cho nhiều định lý cực trị hiện đại. Cái giá phải trả là các chặn dạng tháp lũy thừa, nhắc ta rằng một định lý về sự tồn tại cấu trúc có thể không cho thuật toán hiệu quả.

Với người học về dữ liệu và mạng: bổ đề chính quy là tổ tiên về mặt tư duy của bài toán *phát hiện cộng đồng* và *mô hình khối ngẫu nhiên*, dù chi tiết toán học khác xa quy trình thực hành.

---

## 7. Bản đồ nối các bài Fields trong chương

| Chủ đề | Bài liên quan trong khóa |
|------------|---------------------------|
| Cấp số cộng / mật độ / nguyên lý chuyển | [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) |
| Sàng / khoảng cách giữa các số nguyên tố | [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/) |
| Liên thuộc / ống / Kakeya | [Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/) |
| Xếp cầu / bài toán cực trị Fourier | [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/) |
| Hodge / matroid / lõm loga | **June Huh (Fields 2022)** — mục 5.3 ở trên |
| Động lực học trên không gian moduli | [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) (họ hàng về "hình học đo được") |
| Phương trình đạo hàm riêng / động học | [Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (thống kê từ tương tác của nhiều thành phần; chỉ là so sánh, không đồng nhất) |

**Vì sao bài khảo sát nằm ở cuối Chương 2.** Khi kể về các giải Fields, ta dễ thấy chúng như những đỉnh núi cô lập. Bài tổng hợp này nhắc rằng nhiều đỉnh có chung **sườn núi phương pháp**: Fourier, bài toán cực trị, giả ngẫu nhiên, đa thức, phổ.

---

## 8. Đọc tiếp thế nào để không bị ngợp

1. Chọn **một** từ khóa: tổ hợp cộng tính (additive combinatorics) *hoặc* liên thuộc *hoặc* đồ thị mở rộng *hoặc* phương pháp đa thức.  
2. Tìm một bài tổng quan hoặc ghi chú bài giảng dài khoảng 5–20 trang (các chương của Tao–Vu; bài tổng quan của Hoory–Linial–Wigderson; ghi chú của Guth về phương pháp đa thức).  
3. Viết lại **một** định lý bằng lời của bạn, kèm một câu về "công cụ chính".  
4. Chỉ sau đó mới đọc bài báo nghiên cứu.

Đừng học song song cả năm nhánh trong một tuần.

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|-----|
| "Tổ hợp chỉ là đếm, không chứng minh bằng giải tích." | Sai | Fourier, quy hoạch nửa xác định, ergodic là xương sống của tổ hợp hiện đại. |
| "Green–Tao và Maynard là một." | Sai | Cùng nói về số nguyên tố, nhưng khác câu hỏi và khác công cụ. |
| "Liên thuộc chỉ là bài toán Olympic về điểm và đường thẳng." | Sai | Đó là nền tảng cho bài toán Kakeya rời rạc, bài toán hạn chế, lý thuyết độ đo hình học. |
| "Đồ thị mở rộng chỉ thuộc khoa học máy tính." | Sai | Có các cách xây dựng bằng số học và ứng dụng sâu trong toán thuần túy. |
| "Phương pháp đa thức giải được mọi thứ." | Sai | Mạnh trên các trường hoặc khi có cấu trúc đại số; không phải chiếc búa vạn năng. |
| "Bài tổng hợp này là danh sách định lý cần thuộc." | Sai | Đây là bản đồ định hướng việc đọc. |
| "Huh đã phân loại mọi matroid." | Sai | Ông (cùng cộng sự) chứng minh các phát biểu về tính dương kiểu Hodge; phân loại không phải là nội dung được trao giải. |

---

## Bài tập

1. Nêu **một** phát biểu tổ hợp có chứng minh hình học hoặc đại số (ví dụ Dvir hoặc Guth–Katz, nói sơ lược).
2. Nêu **một** phát biểu hình học hoặc giải tích có bước tổ hợp hoặc bước cực trị rời rạc (ví dụ các ống Kakeya, hoặc chặn cho bài toán xếp cầu).
3. "Cấu trúc và ngẫu nhiên" trong tổ hợp cộng tính nghĩa là gì? Viết không quá 150 từ.
4. Liên thuộc giống "chồng ống" ở điểm nào? Viết một đoạn liên hệ với Kakeya, không dùng công thức.
5. Chọn một từ khóa trong {liên thuộc, đồ thị mở rộng, phương pháp đa thức, cơ sở cộng tính}; tìm một bài tổng quan nhập môn và tóm tắt trong 5 câu.
6. Lập bảng 3 hàng: Green–Tao / Maynard / Szemerédi–Trotter, với các cột câu hỏi và công cụ chính.
7. **Thảo luận.** Đề xuất một bài tập nhỏ cho chương Khám phá (thử nghiệm điểm–đường thẳng hoặc đồ thị ngẫu nhiên) gắn với một ý trong bài này.

---


## Nguồn video (bộ tư liệu nghiên cứu video)

Chi tiết: `research/video-research/Modern_Combinatorics_Geometry/`.

**Thứ tự xem gợi ý**

1. **Định hướng** — Numberphile *g-conjecture* (June Huh): [YouTube](https://www.youtube.com/watch?v=4445Mbw8pYg).  
2. **Về giải thưởng** — Simons / IMU về giải Fields của Huh: [Simons](https://www.youtube.com/watch?v=yO8lQWb6TZ4) · [IMU](https://www.youtube.com/watch?v=ritFtfoRYmY).  
3. **Chân dung** — Quanta: [link](https://www.quantamagazine.org/june-huh-high-school-dropout-wins-the-fields-medal-20220705/).

**Nhắc lại:** Huh đưa ý tưởng của lý thuyết Hodge vào tổ hợp (matroid, tính lõm loga), chứ không chỉ "đếm".

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Modern_Combinatorics_Geometry/transcripts/` · trạng thái: `research/video-research/Modern_Combinatorics_Geometry/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Modern_Combinatorics_Geometry_4445Mbw8pYg_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Modern_Combinatorics_Geometry/references.md`.

### Danh sách URL đầy đủ

1. https://www.simonsfoundation.org/2022/07/05/fields-medal-video-june-huh/  
2. https://arxiv.org/search/?query=Huh+matroid+Hodge&searchtype=all  
3. https://www.quantamagazine.org/june-huh-high-school-dropout-wins-the-fields-medal-20220705/  
4. https://www.ias.edu/scholars/june-huh  
5. https://en.wikipedia.org/wiki/June_Huh  
6. https://web.math.princeton.edu/~huh/  
7. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2022  
8. https://www.youtube.com/watch?v=4445Mbw8pYg  
9. https://www.youtube.com/watch?v=cFKGX3vAs_Q  
10. https://www.youtube.com/watch?v=yO8lQWb6TZ4  
11. https://www.youtube.com/watch?v=ritFtfoRYmY  
12. https://arxiv.org/search/?query=Adiprasito+Huh+Katz&searchtype=all  
13. https://www.numberphile.com/videos/category/June+Huh  

### Bộ tư liệu nghiên cứu

14. Bộ tư liệu của khóa học: `research/video-research/Modern_Combinatorics_Geometry/`.

1. T. Tao, V. Vu — *Additive Combinatorics*.
2. Các bài tổng quan về hình học liên thuộc và phương pháp đa thức (ghi chú của Guth; các bài tổng quan sau Guth–Katz).
3. S. Hoory, N. Linial, A. Wigderson — bài tổng quan về đồ thị mở rộng.
4. N. Alon — định lý không điểm tổ hợp (bài gốc và các bài giới thiệu).
5. Liên kết trong khóa học: [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/), [Maynard]({{ site.baseurl }}/contents/vi/chapter02/02_09_Maynard_Primes/), [Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/), [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/).
6. [Tổng quan Chương 2]({{ site.baseurl }}/contents/vi/chapter02/).

---

## Hướng đi tiếp

- Chuyển sang chương **Khám phá** với các thử nghiệm hình học rời rạc: bài toán liên thuộc nhỏ, đồ thị ngẫu nhiên, mô phỏng đồ thị mở rộng.
- Ghi lại 3 câu hỏi mà bài này gợi ra vào danh sách đọc của bạn; chọn đúng một câu để tìm hiểu sâu trong 2 tuần.
- Nếu theo hướng số học: đọc thêm chương về Freiman–Ruzsa sau Green–Tao.
- Nếu theo hướng giải tích: đọc lần lượt liên thuộc → Kakeya rời rạc → bài toán hạn chế, song song với bài Wang.

## Video tham khảo

- **Xem trước:** [g-conjecture - Numberphile](https://www.youtube.com/watch?v=4445Mbw8pYg) — Numberphile, tiếng Anh. June Huh giới thiệu giả thuyết g, một ví dụ về bài toán đếm có lời giải mang màu sắc hình học; nên xem trước khi đọc bài.
- [Fields Medal: June Huh](https://www.youtube.com/watch?v=yO8lQWb6TZ4) — Simons Foundation, tiếng Anh. Phim ngắn về Huh và giải Fields; nên xem sau khi đã nắm ý chính của bài.
- [Fields Medals 2022 June Huh](https://www.youtube.com/watch?v=ritFtfoRYmY) — International Mathematical Union, tiếng Anh. Xem thêm sau hai video trên; video giới thiệu chính thức của IMU về công trình của Huh.
