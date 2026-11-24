---
layout: post
title: "Chứng minh các giả thuyết Weil của Deligne (Huy chương Fields 1978)"
chapter: '02'
order: 18
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử một thí nghiệm tưởng tượng tưởng chừng chỉ dành cho máy tính bỏ túi: cho một phương trình đa thức với hệ số nguyên, chẳng hạn $$y^2 = x^3 + x + 1$$, và ta ngồi đếm xem nó có bao nhiêu nghiệm trên các trường hữu hạn $$\mathbb{F}_5, \mathbb{F}_{25}, \mathbb{F}_{125}, \ldots$$. Thoạt nhìn, đó chỉ là một dãy số nguyên rời rạc, khô khan và chẳng hề có chút bóng dáng nào của hình học liên tục. Ấy vậy mà năm 1949, **André Weil** đã nhìn thấy bên dưới những con số đếm điểm ấy một cấu trúc đẹp đến rợn người: dãy số nghiệm đó hành xử hệt như thể đa tạp đại số trên trường hữu hạn đang sở hữu những "lỗ hổng tôpô" giống mặt cầu hay hình xuyến trên $$\mathbb{C}$$, và hàm sinh của nó tuân theo một phiên bản hoàn chỉnh của giả thuyết Riemann.

Phải mất đúng một phần tư thế kỷ, qua ba chặng tiếp sức lịch sử, tầm nhìn ấy mới trở thành định lý. **Bernard Dwork** (1960) chứng minh tính hữu tỷ của hàm zeta bằng giải tích $$p$$-adic. **Alexander Grothendieck**, **Michael Artin** và cộng đồng **SGA** xây dựng cả một tòa lâu đài mới mang tên **đối đồng điều étale** để biến bài toán đếm điểm thành công thức vết và suy ra phương trình hàm. Nhưng phần sâu và cứng rắn nhất — **tương tự giả thuyết Riemann**, tức chặn chính xác cho môđun của các trị riêng phép Frobenius — vẫn kháng cự mọi nỗ lực. Năm 1974, khi mới 29 tuổi, **Pierre Deligne** công bố *La conjecture de Weil: I*, đi vòng qua các giả thuyết chuẩn còn bỏ ngỏ của người thầy Grothendieck để hoàn tất mảnh ghép cuối cùng, rồi mở rộng thành bộ máy lý thuyết bó trong *Weil II* (1980).

Bước ngoặt đó mang về cho ông **Huy chương Fields 1978**, với ghi nhận của IMU rằng lời giải các giả thuyết Weil *"đã góp phần lớn vào việc thống nhất hình học đại số và lý thuyết số đại số."* Cần tách bạch ngay từ đầu: Huy chương Fields 1978 không có nghĩa một mình Deligne xây dựng đối đồng điều étale, càng không có nghĩa **các giả thuyết chuẩn** hay **giả thuyết Hodge** đã được giải. Còn **Giải Abel 2013** sau này là sự tôn vinh cho cả sự nghiệp đồ sộ của ông, tách biệt hoàn toàn với huy chương năm 1978.

**Mạch bài học:** Bản đồ kiến thức nền (hình học đại số, đối đồng điều étale, phép Frobenius) → Ví dụ cầm tay đếm điểm trên $$\mathbb{F}_5$$ và $$\mathbb{F}_{25}$$ → Các giả thuyết Weil và ba chặng lịch sử → Khung giải thích chậm: từ đếm điểm đến tính thuần khiết của trị riêng Frobenius → *Weil II* và chặn Ramanujan–Petersson → Ghi nhận công lao & ranh giới với giả thuyết Riemann cổ điển.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu ý chính của các giả thuyết Weil: hàm zeta của một đa tạp xạ ảnh trơn trên trường hữu hạn là **hữu tỷ**, thỏa **phương trình hàm**, và có các không điểm, cực điểm nằm trên những đường thẳng đứng xác định (**tương tự giả thuyết Riemann**).
- Tự tay đếm điểm và kiểm tra hàm zeta $$Z(X, T)$$ trên đường thẳng xạ ảnh $$\mathbb{P}^1$$ và đường cong elliptic trên $$\mathbb{F}_5$$.
- Ghi nhận đúng công lao từng chặng: **Dwork** (tính hữu tỷ), **đối đồng điều étale của Grothendieck–Artin** (công thức vết và phương trình hàm), và **Deligne** (tính thuần khiết của trị riêng Frobenius; *Weil I* và *Weil II*).
- Giải thích vì sao đối đồng điều étale là *công cụ biến phép đếm thành vết*, còn ước lượng của Deligne là *chiếc khóa phổ còn thiếu*.
- Phát biểu cẩn thận rằng chặn **Ramanujan–Petersson** cho dạng modular chỉnh hình trọng số $$\ge 2$$ suy ra từ các giả thuyết Weil cho đa tạp chiều cao hơn (đa tạp Kuga–Sato), không phải chỉ từ một đường cong modular đơn lẻ.
- Bác bỏ các hiểu lầm phổ biến: Deligne **không** chứng minh giả thuyết Riemann cổ điển, **không** chứng minh các giả thuyết chuẩn, và **không** chứng minh giả thuyết Hodge.

**Kiến thức cần có.** Trường hữu hạn $$\mathbb{F}_q$$; ý tưởng về đa tạp xạ ảnh và việc đếm điểm hữu tỷ; tích Euler và giả thuyết Riemann cổ điển như *mô hình* cho một phát biểu về không điểm. Không bắt buộc biết lược đồ hay phạm trù dẫn xuất; chỉ cần nghĩ đến "một lý thuyết đối đồng điều có công thức vết Lefschetz".

**Liên hệ với khóa học.** Giả thuyết Riemann cổ điển, vẫn còn mở: [giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/). Các bài liên quan về hình học số học: [BSD]({{ site.baseurl }}/contents/vi/chapter01/01_04_Birch_Swinnerton_Dyer/) (hàm $$L$$ của đường cong trên $$\mathbb{Q}$$), [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/), [Scholze và đối đồng điều $$p$$-adic]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/). Về giải thưởng cho cả sự nghiệp: [Giải Abel là gì?]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/).

---

## Bản đồ kiến thức nền: Hình học đại số, Đối đồng điều étale và Phép Frobenius là gì?

Trước khi đi vào hàm zeta của Weil và chứng minh của Deligne, hãy dựng một bản đồ trực giác cho ba khái niệm trụ cột đứng sau bài học.

### 1. Hình học đại số trên trường hữu hạn nghiên cứu những câu hỏi nào?
Trong giải tích, ta quen nghiên cứu các hình cong trên số thực $$\mathbb{R}$$ hay số phức $$\mathbb{C}$$ (như đường tròn $$x^2 + y^2 = 1$$) bằng đạo hàm và giới hạn. **Hình học đại số** nghiên cứu tập nghiệm của các hệ phương trình đa thức — gọi là **đa tạp đại số** — nhưng trên *mọi* hệ số, đặc biệt là **trường hữu hạn** $$\mathbb{F}_q$$ (với $$q = p^r$$, chẳng hạn $$\mathbb{F}_5 = \{0, 1, 2, 3, 4\}$$ với phép toán modulo 5).

Ngành **hình học số học** (giao điểm của hình học đại số và lý thuyết số) xoay quanh ba câu hỏi lớn:
- **Đếm điểm:** Một đa tạp $$X$$ có bao nhiêu điểm $$N_m = \#X(\mathbb{F}_{q^m})$$ khi ta mở rộng trường lên $$\mathbb{F}_q, \mathbb{F}_{q^2}, \mathbb{F}_{q^3}, \ldots$$?
- **Cấu trúc ẩn:** Dãy số nguyên $$N_1, N_2, N_3, \ldots$$ có bị ràng buộc bởi một quy luật hình học (số chiều, số "lỗ" giống $$g$$) như trên $$\mathbb{C}$$ không?
- **Ước lượng sai số:** Độ lệch giữa $$N_m$$ và giá trị xấp xỉ sơ cấp (như $$q^m + 1$$ với đường cong) lớn nhất là bao nhiêu?

### 2. Đối đồng điều (Cohomology) và công thức vết Lefschetz
Trong tôpô đại số trên $$\mathbb{C}$$, ta gắn cho mỗi không gian $$X$$ một dãy không gian vector hữu hạn chiều $$H^0(X), H^1(X), \ldots, H^{2n}(X)$$. Số chiều $$b_i = \dim H^i(X)$$ gọi là **số Betti**, đếm số "lỗ hổng $$i$$ chiều":
- Mặt cầu $$S^2$$ (tức đường thẳng xạ ảnh $$\mathbb{P}^1(\mathbb{C})$$): $$b_0 = 1, b_1 = 0, b_2 = 1$$.
- Hình xuyến $$T^2$$ (tức đường cong elliptic $$E(\mathbb{C})$$): $$b_0 = 1, b_1 = 2, b_2 = 1$$.

Điều kỳ diệu là mọi ánh xạ liên tục $$f: X \to X$$ cảm sinh một ma trận $$f^*$$ trên từng $$H^i(X)$$, và **công thức vết Lefschetz** tính số điểm bất động của $$f$$ bằng tổng đan dấu các vết:

$$
\#\{x \in X : f(x) = x\} = \sum_{i=0}^{2n} (-1)^i \operatorname{Tr}\bigl(f^* \;\big\vert\; H^i(X)\bigr).
$$

### 3. Phép Frobenius và Đối đồng điều étale
Trên trường hữu hạn $$\mathbb{F}_q$$, ta có sẵn một ánh xạ tự nhiên cực đẹp là **phép Frobenius** $$\mathrm{Frob}_q: (x_1, \ldots, x_k) \mapsto (x_1^q, \ldots, x_k^q)$$. Theo định lý nhỏ Fermat tổng quát, $$a^q = a \iff a \in \mathbb{F}_q$$, nên một điểm trong bao đóng đại số $$X(\overline{\mathbb{F}}_q)$$ nằm trong $$X(\mathbb{F}_{q^m})$$ **khi và chỉ khi** nó là điểm bất động của $$\mathrm{Frob}_q^m$$!

Vấn đề duy nhất: trên trường hữu hạn không có khái niệm "lân cận nhỏ" kiểu giải tích, còn tôpô Zariski cổ điển lại quá thô để sinh ra các số Betti đúng. **Grothendieck và Michael Artin** đã vượt qua rào cản đó bằng cách thay "tập mở con" bằng các **phủ étale** (phiên bản đại số của phép vi phôi địa phương), xây dựng nên **đối đồng điều étale** $$H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}}, \mathbb{Q}_\ell)$$ (với số nguyên tố phụ trợ $$\ell \neq p$$). Nó khôi phục đúng số Betti cổ điển, sở hữu công thức vết Lefschetz và đối ngẫu Poincaré, biến phép đếm điểm số học thành bài toán đại số tuyến tính về trị riêng của ma trận Frobenius.

---

## 1. Ví dụ cầm tay chỉ việc: đếm điểm trên $$\mathbb{F}_5$$ và thấy tận mắt hàm zeta

Trước khi phát biểu các giả thuyết Weil ở dạng tổng quát, hãy tự tay tính trên **hai ví dụ cụ thể** để thấy mọi ký hiệu trở nên sống động.

### Ví dụ 1: Đường thẳng xạ ảnh $$\mathbb{P}^1$$ trên $$\mathbb{F}_q$$
Trên $$\mathbb{F}_{q^m}$$, $$\mathbb{P}^1$$ gồm đúng $$q^m$$ điểm hữu hạn cộng thêm $$1$$ điểm ở vô cực: $$N_m = q^m + 1$$. Thay vào định nghĩa hàm sinh zeta:

$$
Z(\mathbb{P}^1, T) = \exp\Bigl(\sum_{m\ge 1} (q^m + 1)\frac{T^m}{m}\Bigr).
$$

Dùng khai triển chuỗi Taylor quen thuộc $$-\ln(1 - u) = \sum_{m \ge 1} \frac{u^m}{m}$$, ta tính ngay:

$$
\sum_{m\ge 1} (q^m + 1)\frac{T^m}{m} = -\ln(1 - qT) - \ln(1 - T) \;\Longrightarrow\; Z(\mathbb{P}^1, T) = \frac{1}{(1 - T)(1 - qT)}.
$$

Một chuỗi lũy thừa vô hạn bỗng thu gọn thành một **phân thức hữu tỷ** cực kỳ sạch sẽ! Hai nhân tử ở mẫu là $$P_0(T) = 1 - T$$ (ứng với trị riêng $$1 = q^{0/2}$$ trên $$H^0$$) và $$P_2(T) = 1 - qT$$ (ứng với trị riêng $$q = q^{2/2}$$ trên $$H^2$$).

### Ví dụ 2: Đường cong elliptic $$E: y^2 = x^3 + x + 1$$ trên $$\mathbb{F}_5$$
Hãy lập bảng thử toàn bộ $$x \in \mathbb{F}_5 = \{0, 1, 2, 3, 4\}$$ và tìm số nghiệm $$y \in \mathbb{F}_5$$ (nhớ các số chính phương modulo $$5$$ là $$0^2=0,\; 1^2=4^2=1,\; 2^2=3^2=4$$):

| $$x \in \mathbb{F}_5$$ | $$x^3 + x + 1 \pmod 5$$ | Nghiệm $$y \in \mathbb{F}_5$$ | Số điểm hữu hạn |
|---|---|---|---|
| $$0$$ | $$1$$ | $$y = 1, 4$$ | $$2$$ |
| $$1$$ | $$3$$ | Vô nghiệm | $$0$$ |
| $$2$$ | $$8 + 2 + 1 = 11 \equiv 1$$ | $$y = 1, 4$$ | $$2$$ |
| $$3$$ | $$27 + 3 + 1 = 31 \equiv 1$$ | $$y = 1, 4$$ | $$2$$ |
| $$4$$ | $$64 + 4 + 1 = 69 \equiv 4$$ | $$y = 2, 3$$ | $$2$$ |

Cộng thêm $$1$$ điểm ở vô cực $$\mathcal{O}$$, ta đếm được đúng:

$$
N_1 = \#E(\mathbb{F}_5) = 2 + 0 + 2 + 2 + 2 + 1 = 9.
$$

Hãy kiểm tra **chặn Hasse**: độ lệch so với $$q + 1 = 6$$ là $$a_5 = (5 + 1) - 9 = -3$$, thỏa $$\vert -3 \vert = 3 \le 2\sqrt{5} \approx 4.47$$!
Tuyệt vời hơn nữa: theo công thức Weil cho đường cong elliptic, đa thức tử số là $$P_1(T) = 1 - a_5 T + 5T^2 = 1 + 3T + 5T^2$$, nên hàm zeta của $$E$$ có dạng:

$$
Z(E, T) = \frac{1 + 3T + 5T^2}{(1 - T)(1 - 5T)}.
$$

Phân tích $$1 + 3T + 5T^2 = (1 - \alpha T)(1 - \bar{\alpha} T)$$, ta giải phương trình $$\alpha^2 + 3\alpha + 5 = 0$$ ra cặp số phức liên hợp:

$$
\alpha, \bar{\alpha} = \frac{-3 \pm i\sqrt{11}}{2}, \qquad \vert \alpha \vert = \sqrt{\frac{9 + 11}{4}} = \sqrt{5} = 5^{1/2}!
$$

Và chỉ từ con số $$N_1 = 9$$ vừa đếm bằng tay trên $$\mathbb{F}_5$$, ta **lập tức dự đoán chính xác** số điểm trên $$\mathbb{F}_{25}$$ mà không cần thử 25 giá trị của $$x$$:

$$
N_2 = 1 + 5^2 - (\alpha^2 + \bar{\alpha}^2) = 26 - \bigl((\alpha+\bar{\alpha})^2 - 2\alpha\bar{\alpha}\bigr) = 26 - (9 - 10) = 27!
$$

Đó chính là phép màu của các giả thuyết Weil: đếm điểm trên $$\mathbb{F}_q$$ mở ra một đa thức đặc trưng với hai trị riêng phức nằm **chính xác trên đường tròn bán kính $$\sqrt{q}$$**!

---

## 2. Các giả thuyết Weil (1949) và ba chặng lịch sử

Tổng quát hóa định lý Hasse cho đường cong elliptic và chứng minh của chính mình cho đường cong có giống $$g$$ bất kỳ (với $$\vert N_1 - (q+1)\vert \le 2g\sqrt{q}$$) cùng đa tạp abel, **André Weil** (1949) phát biểu bộ bốn giả thuyết cho mọi đa tạp xạ ảnh trơn $$X$$ chiều $$n$$ trên $$\mathbb{F}_q$$ qua hàm sinh:

$$
Z(X,T)=\exp\Bigl(\sum_{m\ge 1}N_m\frac{T^m}{m}\Bigr),\qquad T=q^{-s}.
$$

1. **Tính hữu tỷ:** $$Z(X,T)$$ là một hàm hữu tỷ theo $$T$$, phân tích thành

$$
Z(X,T)=\frac{P_1(T)P_3(T)\cdots P_{2n-1}(T)}{P_0(T)P_2(T)\cdots P_{2n}(T)},
$$

với $$P_i(T) \in \mathbb{Z}[T]$$, $$P_0(T) = 1 - T$$ và $$P_{2n}(T) = 1 - q^n T$$.
2. **Phương trình hàm:** $$Z(X, 1/(q^n T)) = \pm q^{n\chi/2} T^\chi Z(X, T)$$ (với $$\chi$$ là đặc trưng Euler–Poincaré).
3. **Tương tự giả thuyết Riemann (tính thuần khiết):** Nếu viết $$P_i(T) = \prod_{j=1}^{b_i}(1 - \alpha_{i,j} T)$$, thì mọi trị riêng nghịch đảo $$\alpha_{i,j}$$ đều có môđun phức đúng bằng $$q^{i/2}$$. Đặt $$T = q^{-s}$$, điều này có nghĩa mọi không điểm và cực điểm của $$Z(X, q^{-s})$$ đều nằm gọn trên các đường thẳng đứng $$\mathrm{Re}(s) = i/2$$.
4. **Liên hệ số Betti:** Nếu $$X$$ là phép rút gọn theo modulo $$p$$ của một đa tạp xạ ảnh trơn trên $$\mathbb{C}$$, thì $$\deg P_i = b_i$$ (số Betti thứ $$i$$ của đa tạp phức đó).

**Cuộc chạy tiếp sức ba chặng:**
- **Bernard Dwork (1960):** Gây bất ngờ lớn khi chứng minh **tính hữu tỷ** bằng giải tích $$p$$-adic, hoàn toàn không cần xây dựng đối đồng điều.
- **Grothendieck, Michael Artin và trường phái SGA (thập niên 1960):** Xây dựng **đối đồng điều étale** $$\ell$$-adic, chứng minh công thức vết Lefschetz và đối ngẫu Poincaré, qua đó hoàn tất tính hữu tỷ, phương trình hàm và liên hệ số Betti. Grothendieck kỳ vọng suy ra mảnh ghép cuối cùng (tính thuần khiết) từ **các giả thuyết chuẩn** về chu trình đại số — nhưng các giả thuyết chuẩn đến nay vẫn còn mở!
- **Pierre Deligne (*Weil I*, 1974):** Đi một con đường hoàn toàn bất ngờ, vòng qua các giả thuyết chuẩn để chứng minh trọn vẹn **tính thuần khiết** $$|\alpha_{i,j}| = q^{i/2}$$!

---

## 3. Chứng minh của Deligne: từ đếm điểm đến tính thuần khiết của trị riêng Frobenius

### Khung giải thích: làm sao Deligne khóa chặt môđun của trị riêng Frobenius mà không cần giả thuyết chuẩn? (nên đọc chậm)

Nếu đối đồng điều étale đã biến hàm zeta thành phân thức của các đa thức đặc trưng $$P_i(T) = \det\bigl(1 - T\,\mathrm{Frob} \mid H^i_{\mathrm{\acute{e}t}}(X_{\overline{k}}, \mathbb{Q}_\ell)\bigr)$$, tại sao việc chứng minh $$\vert \alpha_{i,j}\vert = q^{i/2}$$ lại khó đến mức cản bước cả trường phái Grothendieck suốt một thập kỷ? Dưới đây là 4 bước đột phá trong chứng minh *Weil I* (1974) của Deligne:

#### Bước 1: Dùng đối ngẫu Poincaré để rút gọn đẳng thức thành một bất đẳng thức duy nhất
Theo đối ngẫu Poincaré trong đối đồng điều étale, nếu $$\alpha$$ là một trị riêng của Frobenius trên $$H^i$$ thì $$q^n / \alpha$$ là một trị riêng trên $$H^{2n-i}$$ (như trong ví dụ $$\mathbb{P}^1$$: cặp $$1$$ và $$q$$; trong ví dụ đường cong elliptic: cặp $$\alpha$$ và $$5/\alpha = \bar{\alpha}$$). Do đó, nếu ta chứng minh được một chặn trên tổng quát $$\vert \alpha \vert \le q^{i/2}$$ cho **mọi** bậc $$i$$ và mọi đa tạp trơn, thì áp dụng chặn đó cho $$q^n/\alpha$$ trên $$H^{2n-i}$$ lập tức cho $$q^n/\vert\alpha\vert \le q^{(2n-i)/2} \iff \vert\alpha\vert \ge q^{i/2}$$, khóa chặt đẳng thức $$\vert\alpha\vert = q^{i/2}$$!

#### Bước 2: Cắt lát đa tạp bằng chùm Lefschetz (Lefschetz pencil)
Để chứng minh quy nạp theo số chiều $$n$$, Deligne cắt đa tạp $$X$$ chiều $$n$$ bằng một họ 1-tham số các siêu phẳng (tạo thành **chùm Lefschetz**): hầu hết các lát cắt là đa tạp trơn chiều $$n-1$$, chỉ trừ hữu hạn lát cắt có điểm kỳ dị nút đơn giản. Khi lát cắt chạy vòng quanh các điểm kỳ dị trên đường thẳng cơ sở $$\mathbb{P}^1$$, các nhóm đối đồng điều $$H^{n-1}$$ biến đổi theo một nhóm đối xứng gọi là **nhóm đơn đạo** (*monodromy group*). Nhờ định lý Kazhdan–Margulis, Deligne biết nhóm đơn đạo này *rất lớn* (nhóm symplectic toàn phần) — đó là đòn bẩy hình học cực mạnh!

#### Bước 3: Thủ thuật Rankin (lũy thừa tenxơ bậc chẵn $$2k$$) để khử triệt tiêu dấu
Làm sao chứng minh không có trị riêng nào "vượt rào" $$\vert\alpha\vert > q^{i/2}$$? Nếu chỉ cộng các trị riêng lại, số dương và số âm (hay số phức) có thể triệt tiêu lẫn nhau khiến ta không thấy trị riêng lớn. Deligne dùng **thủ thuật Rankin** từ lý thuyết số giải tích: ông nâng hệ địa phương lên **lũy thừa tenxơ bậc chẵn $$2k$$**. Khi lấy lũy thừa $$2k$$, mọi hệ số địa phương đều biến thành **số thực không âm**, không còn sự triệt tiêu dấu nữa! Nếu tồn tại một trị riêng vượt rào $$\vert\alpha\vert > q^{i/2}$$, thì khi $$k \to \infty$$, đóng góp $$\alpha^{2k}$$ sẽ tạo ra một cực điểm vượt quá miền hội tụ cho phép bởi kích thước khổng lồ của nhóm đơn đạo ở Bước 2 — một mâu thuẫn tuyệt đối! Lấy căn bậc $$2k$$ hai vế và cho $$k \to \infty$$, mọi hằng số phụ biến mất, còn lại đúng chặn sắc $$\vert\alpha\vert \le q^{i/2}$$.

#### Bước 4: Mở rộng từ đa tạp sang lý thuyết bó (*Weil II*, 1980)
Sáu năm sau, trong *La conjecture de Weil: II*, Deligne tổng quát hóa toàn bộ bức tranh từ bó hằng trên đa tạp xạ ảnh trơn sang **các bó $$\ell$$-adic kiến thiết hỗn hợp** trên lược đồ tùy ý trên $$\mathbb{F}_q$$. Ông chứng minh phép lấy ảnh trực tiếp có giá compact $$Rf_!$$ bảo toàn bất đẳng thức trọng số (nếu bó đầu vào có trọng số $$\le w$$ thì $$R^i f_!$$ có trọng số $$\le w + i$$). Nhờ *Weil II*, việc ước lượng các tổng mũ phức tạp trong lý thuyết số giải tích biến thành bài toán tính trọng số của bó!

Tóm tắt chuỗi đột phá của Deligne:

$$
\text{Đếm điểm } N_m
\;\longleftrightarrow\;
\text{Vết Frobenius (Grothendieck)}
\;\longleftrightarrow\;
\text{Chùm Lefschetz + Đơn đạo}
\;\longleftrightarrow\;
\text{Lũy thừa } 2k \text{ (Rankin)} \implies \vert\alpha\vert = q^{i/2}.
$$

Báo cáo của Nicholas Katz tại ICM Helsinki (1978) vẫn là tài liệu chuẩn về kiến trúc chứng minh vào thời điểm trao huy chương.

---

## 4. Weil II, chặn Ramanujan–Petersson, và những gì vẫn còn mở

**Những gì được khai thông.** Nhờ *Weil I* và *Weil II*, hàng loạt ước lượng sâu trong lý thuyết số giải tích (tổng mũ nhiều biến, tổng Kloosterman tổng quát, nhóm đơn đạo) trở thành các định lý hình học về trọng số. Đặc biệt nổi tiếng là lời giải cho **giả thuyết Ramanujan–Petersson**.

**Ramanujan–Petersson, nói cho cẩn thận.** Xét hàm $$\tau(n)$$ nổi tiếng của Ramanujan — hệ số khai triển của dạng modular biệt thức $$\Delta(q) = q \prod_{m\ge 1}(1 - q^m)^{24} = \sum_{n\ge 1} \tau(n) q^n$$ (trọng số $$k = 12$$). Giả thuyết Ramanujan (1916) khẳng định rằng với mọi số nguyên tố $$p$$:

$$
\vert\tau(p)\vert \le 2p^{11/2}.
$$

Đây chính là tương tự giả thuyết Riemann cho một đối tượng hình học (motive) **trọng số $$11$$**. Trước đó năm 1969 (theo gợi ý của Serre), Deligne đã gắn cho mỗi dạng cusp chỉnh hình trọng số $$k \ge 2$$ một biểu diễn Galois $$\ell$$-adic và quy chặn Ramanujan–Petersson về các giả thuyết Weil cho một đa tạp **chiều cao hơn** — cụ thể là **đa tạp Kuga–Sato** (xây bằng cách lấy tích thớ $$(k-2)$$ lần của đường cong elliptic phổ dụng trên đường cong modular, nên với $$\Delta$$ trọng số $$12$$ ta làm việc trên đa tạp chiều $$11$$!). Vì vậy, *Weil I* (1974) lập tức kéo theo $$\vert\tau(p)\vert \le 2p^{11/2}$$! (Trường hợp trọng số $$1$$ là câu chuyện riêng của **Deligne–Serre**; còn chặn cổ điển cho tổng Kloosterman một biến chỉ ở chiều $$1$$ nên đã suy ra từ định lý Weil cho đường cong từ trước năm 1974.)

**Những gì chưa được chứng minh.** **Các giả thuyết chuẩn** của Grothendieck vẫn còn mở (trừ định lý Lefschetz mạnh trong đặc số dương mà Deligne suy ra ngược lại từ *Weil II*). **Giả thuyết Hodge** vẫn còn mở. Deligne xây dựng **cấu trúc Hodge hỗn hợp** (mang trực giác trọng số sang hình học phức) và định nghĩa **chu trình Hodge tuyệt đối** như những công cụ mạnh mẽ, không phải chứng minh giả thuyết Hodge.

---

## 5. Ghi nhận công lao một cách trung thực

| Người đóng góp | Vai trò |
|----------------|---------|
| Weil (1949; trước đó cho đường cong) | Đặt giả thuyết; chứng minh cho đường cong và đa tạp abel |
| Hasse | Đường cong elliptic trên trường hữu hạn |
| Dwork (1960) | Tính hữu tỷ, bằng phương pháp $$p$$-adic |
| Grothendieck, M. Artin, SGA | Đối đồng điều étale; công thức vết; phương trình hàm |
| Serre | Các ý tưởng sớm về đối đồng điều và dạng modular; sau này Deligne–Serre |
| Deligne, Weil I (1974) | Tương tự giả thuyết Riemann / tính thuần khiết của trị riêng Frobenius |
| Deligne, Weil II (1980) | Trọng số cho bó; dạng làm việc của lý thuyết |
| Các nhà toán học sau đó | Bó perverse (BBD: Beilinson–Bernstein–Deligne, cùng Gabber) và các ứng dụng |

Deligne sinh năm 1944 tại Bỉ, làm luận án dưới sự hướng dẫn của Grothendieck, làm việc tại IHÉS trong những năm nhận Huy chương Fields, trước khi chuyển sang Institute for Advanced Study (Princeton). **Giải Abel 2013**, trao *"vì những đóng góp nền tảng cho hình học đại số và ảnh hưởng sâu rộng của chúng đến lý thuyết số, lý thuyết biểu diễn và các lĩnh vực liên quan"*, là giải cho *cả sự nghiệp* (bao gồm lý thuyết Hodge hỗn hợp, biểu diễn Deligne–Lusztig, không gian moduli đường cong cùng Mumford...). Hãy luôn tách riêng hai giải thưởng này.

---

## 6. Vì sao ông nhận Huy chương Fields, và vì sao câu chuyện này vẫn quan trọng

Các giả thuyết Weil đã định hướng cả một thế hệ toán học thế kỷ XX: chúng buộc giới hình học đại số dựng nên đối đồng điều étale, rồi đòi hỏi một ước lượng phổ sâu sắc mà bản thân lý thuyết đó không tự động trao cho. Việc hoàn tất các giả thuyết đã nối liền hai cách nhìn về cùng một dãy số nguyên $$N_m$$ — đếm nghiệm số học và phổ trị riêng trên đối đồng điều — đồng thời trao cho lý thuyết dạng tự đẳng cấu và lý thuyết số giải tích một vũ khí sắc bén.

[Giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) cổ điển cho hàm $$\zeta(s)$$ trên $$\mathbb{Q}$$ vẫn còn mở. Điều đó không hề làm giảm tầm vóc của câu chuyện Weil; trái lại, nó cho thấy vì sao giới toán học vẫn tìm kiếm một "đối đồng điều" và một "phép Frobenius" cho $$\mathrm{Spec}(\mathbb{Z})$$. Đừng bao giờ nói "Deligne đã chứng minh giả thuyết Riemann"; hãy nói chính xác: ông đã chứng minh **tương tự giả thuyết Riemann cho hàm zeta của đa tạp đại số trên trường hữu hạn**.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Deligne phát minh ra đối đồng điều étale." | Grothendieck, Artin và SGA xây dựng lý thuyết đó. |
| "Dwork chứng minh các giả thuyết Weil." | Dwork chứng minh **tính hữu tỷ**. Tính thuần khiết là của Deligne. |
| "Deligne chứng minh các giả thuyết chuẩn / giả thuyết Hodge." | Cả hai vẫn còn mở (ở dạng tổng quát). |
| "Deligne chứng minh giả thuyết Riemann cổ điển." | Ông chứng minh **phiên bản tương tự** cho đa tạp trên $$\mathbb{F}_q$$. |
| "Ramanujan suy ra từ giả thuyết Weil cho một đường cong modular." | Trọng số $$\ge 2$$ cần hình học chiều cao hơn (Kuga–Sato); trọng số 1 là kết quả của Deligne–Serre. |
| "Giải Abel 2013 và Huy chương Fields 1978 là cùng một sự ghi nhận." | Giải Abel là giải cho cả sự nghiệp, trao sau này; Huy chương Fields năm 1978 ghi nhận công trình về giả thuyết Weil. |

---

## Nguồn video và đọc thêm

Bài này không có bộ tài liệu video riêng của khóa học.

1. Huy chương Fields 1978 của IMU (lời trích dẫn cho Deligne): [mathunion.org](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1978).
2. Bách khoa: [Pierre Deligne](https://en.wikipedia.org/wiki/Pierre_Deligne); [Weil conjectures](https://en.wikipedia.org/wiki/Weil_conjectures).
3. Giải Abel 2013 (giải cho cả sự nghiệp, khác Huy chương Fields): [abelprize.no/abel-prize-laureates/2013](https://abelprize.no/abel-prize-laureates/2013).
4. Thông cáo của IAS (Abel 2013): [Pierre Deligne Awarded 2013 Abel Prize](https://www.ias.edu/press-releases/pierre-deligne-awarded-2013-abel-prize).
5. Tìm trên arXiv: [Deligne Weil](https://arxiv.org/search/?query=Deligne+Weil&searchtype=all).
6. Trong khóa học: [RH]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/); [Tổng quan về Giải Abel]({{ site.baseurl }}/contents/vi/chapter08/08_02_Giai_Abel_la_gi/).

**Ghi nhớ:** Đây là tương tự giả thuyết Riemann của Weil trên trường hữu hạn, **không** phải giả thuyết Riemann cổ điển, **không** phải giả thuyết Hodge, **không** phải các giả thuyết chuẩn.

---

## Tài liệu tham khảo

1. International Mathematical Union, Huy chương Fields 1978: Pierre Deligne (văn bản in lại từ sách lịch sử các đại hội của Albers–Alexanderson–Reid năm 1986, đăng trên trang IMU).
2. **A. Weil**, *Numbers of solutions of equations in finite fields*, *Bull. Amer. Math. Soc.* (1949).
3. **B. Dwork**, *On the rationality of the zeta function of an algebraic variety*, *Amer. J. Math.* (1960).
4. **P. Deligne**, *La conjecture de Weil: I*, *Publ. Math. IHÉS* 43 (1974); *La conjecture de Weil: II*, *Publ. Math. IHÉS* 52 (1980).
5. **N. Katz**, *The work of Pierre Deligne*, kỷ yếu ICM Helsinki 1978 (bài tổng quan vào thời điểm trao huy chương).
6. Nền tảng SGA và đối đồng điều étale: Grothendieck–Artin; một giáo trình hiện đại (ví dụ bài giảng của Milne) để tham khảo, không bắt buộc đọc.
7. Lời trích dẫn Giải Abel 2013 cho Pierre Deligne (abelprize.no).
8. Trong khóa học: [RH]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/), [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/), [Langlands]({{ site.baseurl }}/contents/vi/chapter02/02_02_Langlands_Program/).

---

## Hướng đi tiếp

- Tự tính $$Z(\mathbb{P}^n,T)$$. Đây là các giả thuyết Weil trong trường hợp không cần đối đồng điều, và giúp bạn quen với ký hiệu.
- Đọc một bài giảng (một buổi) về công thức vết Lefschetz trong đối đồng điều étale trước khi đọc Weil I.
- Bài seminar A3 (tùy chọn): viết một trang về "những gì còn mở sau Deligne" (các giả thuyết chuẩn, giả thuyết Hodge, motive, giả thuyết Riemann cổ điển), tách rõ Huy chương Fields 1978 với Giải Abel 2013.
- Nếu bạn quan tâm đến dạng modular, hãy theo Ramanujan–Petersson đến các bài báo của Deligne, rồi đến Deligne–Serre cho trọng số một, và luôn ghi rõ số chiều của đa tạp được dùng.

## Video tham khảo

- **Xem trước** — [Timothy Gowers: The Weil conjectures explained](https://www.youtube.com/watch?v=PHkYqPX3Je4) — The Abel Prize, tiếng Anh. Timothy Gowers giải thích các giả thuyết Weil cho khán giả rộng, nhân dịp Giải Abel 2013. Nên xem trước khi đọc bài.
- [The Weil Conjectures, from Abel to Deligne - Sophie Morel](https://www.youtube.com/watch?v=iDgtP6ZpR70) — Institute for Advanced Study, tiếng Anh. Sophie Morel kể lại lịch sử các giả thuyết Weil từ Abel đến Deligne, tương ứng với mục 1–2. Nên xem sau khi đọc bài.
- [The Weil conjectures - Lothar Goettsche - 2016](https://www.youtube.com/watch?v=kiQwnXT7j7g) — ICTP Mathematics, tiếng Anh. Bài giảng có tính kỹ thuật hơn về các giả thuyết Weil. Dành cho người muốn đi sâu.
