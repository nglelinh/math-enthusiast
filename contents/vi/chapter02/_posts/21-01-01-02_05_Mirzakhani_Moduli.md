---
layout: post
title: "Mirzakhani và Không gian Mô-đun (Huy chương Fields 2014)"
chapter: '02'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy hình dung một chiếc bàn bi-a hình đa giác kỳ lạ, và bạn đánh một viên bi lăn mãi không dừng. Quỹ đạo của viên bi sẽ lặp lại một vòng kín, hay dần dần tô kín toàn bộ mặt bàn? Nghe tưởng như một câu đố giải trí, nhưng bài toán bi-a trong đa giác lại dẫn thẳng vào một trong những vùng đất trừu tượng và đẹp đẽ nhất của toán học hiện đại: hình học của **các mặt cong** và **không gian chứa mọi hình dạng có thể có của chúng** — gọi là *không gian mô-đun*.

Năm 2014, **Maryam Mirzakhani** trở thành **người phụ nữ đầu tiên** trong lịch sử nhận **Huy chương Fields**, nhờ những đóng góp mang tính đột phá cho **động lực học và hình học** của **mặt Riemann** và **không gian mô-đun** của chúng. Thay vì coi không gian mô-đun như một khái niệm trừu tượng chỉ để định nghĩa, công trình của bà đã biến "vũ trụ của mọi hình dạng" thành một đối tượng vừa **tính toán được** (đo được thể tích, đếm được số đường cong khép kín) vừa **nghiên cứu được bằng hệ động lực** (theo dõi các dòng chuyển động và tính hỗn loạn đều khắp), bắc một cây cầu rực rỡ giữa hình học hyperbolic, lý thuyết Teichmüller và hệ động lực.

**Mạch bài học:** Bản đồ kiến thức nền (hình học hyperbolic, không gian mô-đun qua ví dụ mặt xuyến & chiếc quần, lý thuyết ergodic) → Tọa độ Fenchel–Nielsen $$6g-6$$ → Đếm đường trắc địa đóng đơn → Khung giải thích chậm 4 bước: thể tích Weil–Petersson & công thức đệ quy Mirzakhani → Dòng động đất, bi-a đa giác & Định lý Cây đũa thần.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa trực quan **mặt Riemann** giống $$g\ge 2$$, **metric hyperbolic**, **không gian Teichmüller** và **không gian mô-đun**.
- Tự kiểm tra bằng tay vì sao không gian mô-đun mặt xuyến ứng với $$\mathbb{H}/\mathrm{SL}_2(\mathbb{Z})$$ và vì sao mặt giống $$g$$ có đúng $$6g - 6$$ tham số Fenchel–Nielsen.
- Phát biểu bài toán đếm **đường trắc địa đóng đơn** và tốc độ tăng tiệm cận bậc $$6g-6$$ của Mirzakhani.
- Hiểu mạch suy luận nối **thể tích Weil–Petersson** (như $$V_{1,1}(L) = \frac{1}{24}(L^2 + 4\pi^2)$$) với bài toán đếm đường cong.
- Phác thảo ý tưởng **dòng động đất**, **mặt phẳng dịch chuyển** (bi-a đa giác) và **Định lý Cây đũa thần** cùng Alex Eskin.
- Ghi nhận chính xác rằng Mirzakhani là **người phụ nữ đầu tiên đoạt Huy chương Fields** (2014) cho cả một sự nghiệp nghiên cứu sâu rộng.

**Kiến thức cần có.** Mặt giống $$g$$ (mặt cầu, mặt xuyến, …); khái niệm đường trắc địa; tích phân và số phức cơ bản. Không cần biết trước lý thuyết Teichmüller.

**Liên hệ trong khóa học.** Các bài liên quan: [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/), [vô hạn / hình dạng]({{ site.baseurl }}/contents/vi/chapter04/04_02_Infinity/), [Furstenberg–Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/).

---

## Bản đồ kiến thức nền: Hình học hyperbolic, Không gian mô-đun và Lý thuyết ergodic là gì?

### 1. Hình học hyperbolic (Hyperbolic Geometry) nghiên cứu gì?
Trong hình học phẳng Euclid, tổng ba góc tam giác bằng $$180^\circ$$ (độ cong $$0$$). Trên mặt cầu, tam giác phồng ra nên tổng ba góc $$> 180^\circ$$ (độ cong $$+1$$). **Hình học hyperbolic** là thế giới thứ ba: mọi điểm đều uốn cong như yên ngựa (độ cong âm hằng $$-1$$), tổng ba góc tam giác luôn $$< 180^\circ$$, và diện tích tam giác tỉ lệ thuận với phần thiếu góc: $$\text{Diện tích} = \pi - (\alpha + \beta + \gamma)$$! Mô hình quen thuộc nhất là **nửa mặt phẳng trên** $$\mathbb{H} = \{x + iy : y > 0\}$$ với thước đo độ dài $$ds = \frac{\sqrt{dx^2 + dy^2}}{y}$$, nơi các đường thẳng nhất (**đường trắc địa**) là các tia thẳng đứng và các nửa đường tròn vuông góc với trục thực.

Điều kỳ diệu của **Định lý đơn trị hóa** là: mọi bề mặt đóng có từ **2 lỗ trở lên** (giống $$g \ge 2$$) đều mang tự nhiên một metric hyperbolic!

### 2. Không gian mô-đun (Moduli Space) là gì? (Hai ví dụ cầm tay)
Một **không gian mô-đun** là không gian mà **mỗi điểm của nó là một hình dạng hình học hoàn chỉnh**!

- **Ví dụ 1 — Không gian mọi hình chữ nhật diện tích 1:** Mọi hình chữ nhật diện tích $$1$$ chỉ khác nhau ở tỉ lệ dài/rộng $$r \ge 1$$. Vậy "không gian mô-đun" của chúng chính là tia số $$[1, \infty)$$.
- **Ví dụ 2 — Không gian mô-đun các mặt xuyến ($$g = 1$$):** Lấy một hình bình hành trên mặt phẳng phức $$\mathbb{C}$$ sinh bởi hai vectơ $$1$$ và $$\tau$$ (với $$\operatorname{Im}\tau > 0$$), rồi dán các cạnh đối diện lại — ta được một **mặt xuyến**! Khi nào hai tham số $$\tau$$ và $$\tau'$$ cho ra *cùng một hình dạng mặt xuyến*? Chính xác khi chúng sinh ra cùng một lưới (sai khác phép quay–co giãn), tức $$\tau' = \frac{a\tau + b}{c\tau + d}$$ với ma trận $$\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathrm{SL}_2(\mathbb{Z})$$! Chẳng hạn $$\tau = i$$ (hình vuông) và $$\tau' = i + 1$$ (hình bình hành nghiêng $$45^\circ$$) đều sinh ra đúng lưới vuông $$\mathbb{Z}[i]$$ nên là **cùng một điểm** trong không gian mô-đun $$\mathcal{M}_1 = \mathbb{H}/\mathrm{SL}_2(\mathbb{Z})$$!

### 3. Lý thuyết ergodic và lý do chuyển ngôn ngữ
Lý thuyết ergodic nghiên cứu tính hỗn loạn đều khắp của hệ động lực (trung bình theo thời gian bằng trung bình theo không gian). Thay vì đứng trên *một* mặt hyperbolic $$X$$ cố định để đếm thủ công từng đường trắc địa ngoằn ngoèo, Mirzakhani bước ra ngoài, đặt $$X$$ làm một điểm trong **không gian mô-đun $$\mathcal{M}_g$$**, rồi dùng **tích phân thể tích** và **dòng động lực** trên $$\mathcal{M}_g$$ để giải bài toán đếm!

---

## 1. Mặt Riemann, đường trắc địa đơn và tọa độ $$6g - 6$$

Một **mặt Riemann đóng** giống $$g$$ có đặc trưng Euler $$\chi = 2 - 2g$$. Với $$g \ge 2$$, $$\chi < 0$$ nên mặt mang metric hyperbolic độ cong $$-1$$. **Đường trắc địa đóng đơn** là vòng khép kín ngắn nhất địa phương và **không tự cắt** — hãy hình dung một sợi dây chun căng ôm chặt lấy một cái eo trên chiếc bánh vòng nhiều lỗ.

**Không gian Teichmüller** $$\mathcal{T}_g$$ tham số hóa các mặt hyperbolic *được đánh dấu* (nhớ rõ nhãn của từng đường cong). **Không gian mô-đun** $$\mathcal{M}_g = \mathcal{T}_g / \mathrm{Mod}_g$$ là thương theo **nhóm lớp ánh xạ** $$\mathrm{Mod}_g$$ (bỏ đi nhãn đánh dấu, chỉ giữ lại hình dạng thuần túy).

### Tự kiểm tra bằng tay: Vì sao $$\dim_{\mathbb{R}} \mathcal{T}_g = 6g - 6$$?
Hãy cắt chiếc bánh vòng $$g$$ lỗ dọc theo các đường tròn rời nhau thành những mảnh cơ bản nhất không thể cắt tiếp được: mỗi mảnh là một **"chiếc quần"** (*pair of pants* — mặt cầu khoét 3 lỗ có đặc trưng Euler $$\chi = 2 - 3 = -1$$).
- Vì đặc trưng Euler cộng được khi dán dọc đường tròn ($$\chi(S^1) = 0$$), mặt giống $$g$$ (có $$\chi = 2 - 2g$$) tách thành đúng **$$2g - 2$$ chiếc quần**.
- Mỗi chiếc quần có 3 ống biên, nên tổng số ống biên là $$3(2g - 2) = 6g - 6$$. Vì cứ 2 ống dán vào nhau tạo thành 1 đường cắt, ta có đúng **$$3g - 3$$ đường cắt**.
- Hình học hyperbolic của mỗi chiếc quần được xác định duy nhất bởi độ dài 3 đường biên. Vậy $$3g - 3$$ đường cắt cho **$$3g - 3$$ tham số độ dài** $$(\ell_1, \dots, \ell_{3g-3})$$. Khi dán hai ống lại, tại mỗi đường dán ta được quyền *xoay lệch* một góc tùy ý — thêm **$$3g - 3$$ tham số góc xoắn** $$(\theta_1, \dots, \theta_{3g-3})$$.

Tổng cộng: $$(3g - 3) + (3g - 3) = \mathbf{6g - 6}$$ tham số thực (**tọa độ Fenchel–Nielsen**)! Thử với mặt 2 lỗ ($$g = 2$$): ta cắt theo **3 đường tròn** thành **2 chiếc quần**, được đúng $$3 + 3 = 6$$ tọa độ!

![Moduli như không gian hình dạng]({{ site.baseurl }}/img/chapter_img/mirzakhani_moduli_shapes.svg)

*Hình (minh họa ý tưởng). Mỗi điểm của không gian mô-đun là một lớp hình dạng của mặt; một đường cong trong không gian mô-đun là một quá trình biến dạng hình dạng.*

---

## 2. Đếm các đường trắc địa đóng đơn

Cố định một mặt hyperbolic $$X$$ có giống $$g\ge 2$$. Gọi $$N_X(L)$$ là số đường trắc địa đóng **đơn** có độ dài $$\le L$$. Nếu cho phép đường cong tự cắt, số đường tăng theo hàm mũ cực nhanh $$e^L / L$$ (định lý đường trắc địa nguyên tố, tương tự định lý số nguyên tố). Nhưng điều kiện *đơn* (không tự cắt) khiến đường cong cực kỳ "cứng", làm số lượng tăng theo hàm đa thức:

$$
N_X(L) \;\sim\; c_X\, L^{6g-6} \qquad (L \to \infty).
$$

Số mũ $$6g-6$$ khớp tuyệt đối với số chiều thực của không gian mô-đun (bậc $$6$$ với mặt 2 lỗ, bậc $$12$$ với mặt 3 lỗ!). Hơn thế nữa, Mirzakhani tính được cả **tỉ lệ chính xác** giữa các kiểu tô pô: chẳng hạn trên mặt 2 lỗ, tỉ lệ giữa đường trắc địa đơn *cắt mặt thành hai mảnh rời* so với đường *không tách mặt* là một con số hữu tỷ đẹp tuyệt đối — đúng bằng **$$1/48$$** (suy trực tiếp từ tỉ số thể tích không gian mô-đun)!

---

## 3. Khung giải thích: Vì sao đếm đường cong trên MỘT mặt lại đưa về thể tích trên KHÔNG GIAN MỌI MẶT? (nên đọc chậm)

Làm thế nào Mirzakhani vừa tính được thể tích không gian mô-đun, vừa suy ra công thức đếm $$N_X(L) \sim c_X L^{6g-6}$$? Hãy theo dõi mạch 4 bước sau:

#### Bước 1: Dạng thể tích tự nhiên Weil–Petersson
Trong tọa độ Fenchel–Nielsen $$(\ell_i, \theta_i)$$, định lý Wolpert cho biết dạng symplectic **Weil–Petersson** có công thức gọn gàng đến khó tin:

$$
\omega_{\mathrm{WP}} = \sum_{i=1}^{3g-3} d\ell_i \wedge d\theta_i.
$$

Lấy lũy thừa ngoài của $$\omega_{\mathrm{WP}}$$ cho ta một phần tử thể tích tự nhiên trên không gian mô-đun $$\mathcal{M}_{g,n}(L_1, \dots, L_n)$$ (các mặt giống $$g$$ có $$n$$ biên độ dài $$L_1, \dots, L_n$$), với tổng thể tích ký hiệu là $$V_{g,n}(L_1, \dots, L_n)$$.

#### Bước 2: Đồng nhất thức McShane tổng quát và Công thức đệ quy Mirzakhani
Để tính $$V_{g,n}(L_1, \dots, L_n)$$, Mirzakhani chọn một đường biên $$L_1$$, bắn các tia trắc địa vuông góc từ $$L_1$$ vào bên trong mặt và xem tia nào tự cắt trước. Điều đó tách biên $$L_1$$ thành một tổng các khoảng xác suất ứng với các "chiếc quần" chứa $$L_1$$ — cho ra **đồng nhất thức McShane tổng quát**. Lấy tích phân đồng nhất thức này trên toàn bộ không gian mô-đun biến phép cắt một chiếc quần thành **công thức đệ quy** tính $$V_{g,n}$$ từ các mặt đơn giản hơn (giảm $$g$$ hoặc $$n$$)!

**Ví dụ cầm tay để tự kiểm tra:** Với mặt xuyến khoét 1 lỗ ($$g = 1, n = 1$$) có biên dài $$L$$, công thức đệ quy Mirzakhani cho ra đa thức bậc hai tuyệt đẹp:

$$
V_{1,1}(L) = \frac{1}{24}\bigl(L^2 + 4\pi^2\bigr).
$$

Thử cho $$L \to 0$$ (lỗ biên co về một đỉnh nhọn cusp): ta thu được $$V_{1,1}(0) = \frac{\pi^2}{6}$$, trùng khít với thể tích cổ điển của không gian mô-đun mặt xuyến! Tổng quát hơn, Mirzakhani chứng minh mọi $$V_{g,n}(L_1, \dots, L_n)$$ đều là **đa thức theo $$L_1^2, \dots, L_n^2$$** — và các hệ số bậc cao nhất của đa thức đó chính là các số giao trên không gian mô-đun (từ đó bà cho một chứng minh hình học mới cực ngắn cho **giả thuyết Witten–Kontsevich** trong vật lý hấp dẫn lượng tử 2D!).

#### Bước 3: Chuyển đổi "đếm trên một mặt" thành "tích phân trên không gian mô-đun"
Cố định một kiểu tô pô đường cong $$\gamma$$. Trên mỗi mặt $$X \in \mathcal{M}_g$$, hàm $$s_\gamma(X) = \#\{\text{ảnh của } \gamma \text{ có độ dài} \le L\}$$ rất khó tính trực tiếp. Nhưng nếu lấy **tích phân** hàm đó trên toàn bộ $$\mathcal{M}_g$$, ta có thể đổi thứ tự tích phân (giống mở phủ không gian thương): thay vì cố định mặt rồi cộng theo mọi đường cong, ta **cắt mặt dọc theo đường cong độ dài $$\ell \le L$$** rồi lấy tích phân thể tích $$V_{g', n'}(\ell, \ell)$$ của phần mặt còn lại theo $$\ell$$ từ $$0$$ đến $$L$$! Vì $$V_{g', n'}$$ là đa thức bậc $$6g - 8$$ theo $$\ell$$ (cộng thêm yếu tố góc xoắn $$\ell$$ khi dán lại), tích phân $$\int_0^L \ell \cdot \ell^{6g-8}\, d\ell$$ lập tức cho ra đúng bậc **$$L^{6g-6}$$**!

#### Bước 4: Dùng tính ergodic của dòng động đất để quay về đúng mặt $$X$$ ban đầu
Bước 3 cho ta giá trị *trung bình* trên toàn không gian mô-đun $$\mathcal{M}_g$$. Để chứng minh rằng công thức đó đúng cho **từng mặt $$X$$ cố định**, Mirzakhani sử dụng tính **ergodic** của dòng động đất (*earthquake flow*) trên không gian các lá phân đo được: khi $$L \to \infty$$, quỹ đạo các đường cong dài trên $$X$$ phân bố đều đặn khắp không gian mô-đun nên kết quả trên từng mặt $$X$$ khớp đúng với tích phân thể tích!

Tóm tắt mạch chứng minh:

$$
\text{Cắt thành quần}
\;\xrightarrow{\text{Đệ quy}}\;
\text{Đa thức thể tích } V_{g,n}(L)
\;\xrightarrow{\text{Đổi tích phân}}\;
\text{Trung bình } \sim L^{6g-6}
\;\xrightarrow{\text{Ergodic}}\;
N_X(L) \sim c_X L^{6g-6}.
$$

---

## 4. Dòng động đất, Bi-a đa giác và Định lý "Cây đũa thần"

Một **phép động đất** (Thurston) biến dạng mặt hyperbolic bằng cách cắt mặt dọc theo một họ đường cong (lá phân đo được), trượt hai mép lệch nhau như đường đứt gãy địa chất rồi dán lại. **Dòng động đất** biến phép trượt đó thành một hệ động lực trên không gian mô-đun, và Mirzakhani chứng minh nó mang tính **ergodic** (quỹ đạo điển hình trải đều khắp không gian theo độ đo).

Song song với đó, hãy quay lại **bàn bi-a đa giác** ở đầu bài: mỗi khi viên bi chạm vào một cạnh bàn, thay vì cho viên bi bật lại, ta *lật phản chiếu* cả chiếc bàn qua cạnh đó để viên bi đi thẳng tắp! Dán các bản sao đối xứng ấy lại (ví dụ với bàn bi-a hình tam giác đều hay hình chữ nhật), ta thu được một **mặt phẳng dịch chuyển** (*translation surface*). Nhóm ma trận $$\mathrm{SL}_2(\mathbb{R})$$ tác động tự nhiên lên không gian các mặt phẳng dịch chuyển (kéo giãn một chiều, nén chiều kia).

Trong kiệt tác mệnh danh là **"Định lý Cây đũa thần"** (*Magic Wand Theorem*, 2013), **Alex Eskin và Maryam Mirzakhani** (cùng Amir Mohammadi) đã chứng minh rằng mọi bao đóng quỹ đạo và độ đo bất biến của tác động $$\mathrm{SL}_2(\mathbb{R})$$ đều cực kỳ đẹp và "cứng" (luôn là các đa tạp con affine) — hoàn toàn tương tự định lý Ratner kinh điển trên không gian thuần nhất, dù không gian mô-đun phức tạp hơn rất nhiều!

---

## 5. Vì sao công trình này quan trọng và bối cảnh con người

- Làm cho không gian mô-đun **vừa tính toán được vừa nghiên cứu được bằng hệ động lực**, bắc cây cầu **hệ động lực ↔ không gian mô-đun** trong Chương 2.
- **Maryam Mirzakhani** là **người phụ nữ đầu tiên** nhận Huy chương Fields (2014). Maryna Viazovska là người thứ hai (2022); xem bài [Viazovska]({{ site.baseurl }}/contents/vi/chapter02/02_08_Viazovska_Sphere_Packing/).
- Nhiều định lý lớn là công trình hợp tác (đặc biệt với **Alex Eskin** trong phần động lực học); luôn kiểm tra đồng tác giả khi trích dẫn.
- Mirzakhani mất năm 2017; ảnh hưởng của bà vẫn tiếp tục lan tỏa mạnh mẽ qua hàng loạt thế hệ nghiên cứu về mặt Riemann và động lực Teichmüller.

---

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|---------|
| "Không gian mô-đun chính là bản thân mặt." | **Sai** | Đó là không gian chứa tất cả các mặt (mỗi mặt là một điểm). |
| "Bà chỉ đếm đường trắc địa." | **Sai** | Thể tích Weil–Petersson, dòng động đất và Định lý Cây đũa thần cùng Eskin cũng là trung tâm. |
| "Không gian Teichmüller chính là không gian mô-đun." | **Sai** | Không gian Teichmüller có đánh dấu; không gian mô-đun là thương $$\mathcal{T}_g/\mathrm{Mod}_g$$. |
| "Tính ergodic nghĩa là mọi quỹ đạo đều tuần hoàn." | **Sai** | Đó là phát biểu về độ đo: trung bình thời gian bằng trung bình không gian. |
| "Mọi kết quả đều do một mình bà làm." | **Sai** | Nhiều định lý lớn là công trình hợp tác (như Eskin–Mirzakhani). |

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Chi tiết: `research/video-research/Mirzakhani_Moduli/`.

**Thứ tự xem gợi ý**

1. Video về Mirzakhani của Quanta/Simons: [YouTube](https://www.youtube.com/watch?v=qNuh4uta8oQ).  
2. Bài viết của Quanta: [link](https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/).  
3. Trang bài giảng Morse tại IAS: [link](https://www.ias.edu/ideas/dynamics-moduli-spaces-curves-i).  
4. Bài "cây đũa thần" (magic wand): [arXiv:1302.3320](https://arxiv.org/abs/1302.3320).

**Nhắc lại:** phần toán về không gian mô-đun và hệ động lực là lý do bài này có trong chương trình; tiểu sử của bà quan trọng về mặt văn hóa.

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Mirzakhani_Moduli/transcripts/` · trạng thái: `research/video-research/Mirzakhani_Moduli/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Mirzakhani_Moduli_qNuh4uta8oQ_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Mirzakhani_Moduli/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=qNuh4uta8oQ  
2. https://www.ias.edu/ideas/dynamics-moduli-spaces-curves-i  
3. https://arxiv.org/abs/1302.3320  
4. https://arxiv.org/abs/1305.3015  
5. https://www.quantamagazine.org/maryam-mirzakhani-is-first-woman-fields-medalist-20140812/  
6. https://en.wikipedia.org/wiki/Maryam_Mirzakhani  
7. https://celebratio.org/Mirzakhani_M/article/1087/  
8. https://terrytao.wordpress.com/tag/maryam-mirzakhani/  
9. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014  
10. https://arxiv.org/search/?query=Mirzakhani+Weil-Petersson&searchtype=all  
11. https://news.stanford.edu/stories/2014/08/surfaces-mirzakhani-081214  

### Bộ tư liệu nghiên cứu

12. Bộ tư liệu của khóa học: `research/video-research/Mirzakhani_Moduli/`.

1. IMU, Huy chương Fields 2014 — Maryam Mirzakhani (lời trích dẫn và bài ca ngợi).  
2. Luận án và các bài báo về thể tích Weil–Petersson / đếm đường trắc địa.  
3. Eskin–Mirzakhani — dòng động đất và các hệ động lực liên quan.  
4. Các bài tổng quan về động lực Teichmüller / không gian mô-đun của đường cong (nhiều tác giả).  
5. Nhập môn: hình học hyperbolic của mặt; tọa độ Fenchel–Nielsen; nhóm lớp ánh xạ (mức sơ lược).

---

## Hướng đi tiếp

- Tìm hiểu mặt phẳng dịch chuyển và bi-a trong đa giác như một chủ đề anh em.  
- So sánh với các câu chuyện khác trong khóa học về "hệ động lực gặp hình học".  
- Đọc một bản trình bày về thể tích Weil–Petersson trước khi đọc bài báo gốc.  
- Ghi lại một câu hỏi cụ thể, ví dụ "độ đo nào khiến dòng động đất là ergodic?"  
- Đọc song song bài [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/) để so sánh hai truyền thống nghiên cứu hệ động lực.

## Video tham khảo

- **Xem trước:** [Maryam Mirzakhani: A Tenacious Explorer of Abstract Surfaces](https://www.youtube.com/watch?v=qNuh4uta8oQ) — Quanta Magazine, tiếng Anh. Chân dung Mirzakhani và các mặt trừu tượng bà nghiên cứu; nên xem trước khi đọc bài.
- [Dynamics on the Moduli Spaces of Curves, I - Maryam Mirzakhani](https://www.youtube.com/watch?v=8Az_W2wv4Zo) — Institute for Advanced Study, tiếng Anh. Bài giảng của chính Mirzakhani về động lực trên không gian mô-đun của đường cong; nên xem sau khi đã nắm ý chính của bài.
- [Maryam Mirzakhani, Dynamics Moduli Spaces of Curves I](https://www.youtube.com/watch?v=tprlQMClSYQ) — Harvard Mathematics Department, tiếng Anh. Xem thêm sau hai video trên; một bài giảng khác của bà về cùng chủ đề.
