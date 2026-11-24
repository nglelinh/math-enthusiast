---
layout: post
title: "Lượng tử hóa, đường cong và nút của Kontsevich (Huy chương Fields 1998)"
chapter: '02'
order: 22
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Đầu thập niên 1990, vật lý lý thuyết liên tiếp ném sang giới toán học những lời tiên đoán gây choáng váng: từ hấp dẫn lượng tử hai chiều, Edward Witten dự đoán các số giao hình học trên không gian moduli đường cong phải tuân theo phương trình sóng nước nông KdV; từ lý thuyết trường lượng tử Chern–Simons, các nhà vật lý gợi ý những tích phân đường tưởng chừng vô nghĩa lại mã hóa toàn bộ bất biến của các nút thắt trong $$\mathbb{R}^3$$; và từ cơ học lượng tử, một câu hỏi mở suốt 20 năm vẫn đứng vững: liệu *mọi* không gian pha Poisson cổ điển đều có thể lượng tử hóa biến dạng được hay không?

**Maxim Kontsevich** bước vào đúng ngã ba giông bão ấy với một thứ vũ khí thống nhất đến kỳ lạ: **tổng có trọng số trên các đồ thị**, trong đó mỗi trọng số là một tích phân trên không gian cấu hình. Ông lần lượt biến cả ba bài toán đó thành định lý toán học chặt chẽ, và nhận **Huy chương Fields 1998**:

> “For his contributions to algebraic geometry, topology, and mathematical physics, including the proof of Witten's conjecture of intersection numbers in moduli spaces of stable curves, construction of the universal Vassiliev invariant of knots, and formal quantization of Poisson manifolds.”
> — Citation IMU, ICM 1998 (như được ghi trong hồ sơ [Fields Medal](https://www.mathunion.org/imu-awards/fields-medal) và các nguồn tiểu sử chuẩn)

*Tạm dịch: vì những đóng góp cho hình học đại số, tôpô và vật lý toán, trong đó có chứng minh giả thuyết Witten về số giao trên không gian moduli các đường cong ổn định, xây dựng bất biến Vassiliev phổ dụng của nút, và lượng tử hóa hình thức các đa tạp Poisson.*

Vì Kontsevich (sinh năm 1964, giáo sư thường trực tại IHÉS) sau này còn nổi tiếng với hàng loạt chương trình lớn như **đối xứng gương đồng điều** (HMS), tích phân motivic hay hiện tượng vượt tường (*wall-crossing*), người đọc ngày nay rất dễ nhầm danh sách. Bài học này bám sát đúng **ba cột mốc của lời trao giải năm 1998**, đồng thời đặt đối xứng gương đồng điều đúng chỗ: một tầm nhìn lớn từ ICM 1994, không phải kết quả thứ ba của giải Fields 1998.

**Mạch bài học:** Bản đồ kiến thức nền (đa tạp Poisson, không gian moduli $$\overline{\mathcal{M}}_{g,n}$$, bất biến nút Vassiliev) → Ví dụ cầm tay chỉ việc: tính tích sao Moyal cho $$q \star p$$ và $$q^2 \star p^2$$ → Giả thuyết Witten & Tích phân Kontsevich → Khung giải thích chậm: Định lý hình thức (Formality) và công thức đồ thị cho lượng tử hóa biến dạng → Đối xứng gương đồng điều (1994) & phân biệt với giải năm 1998.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhớ lời trao giải năm 1998 gồm **ba** kết quả chính thức (giả thuyết Witten, bất biến Vassiliev phổ dụng, lượng tử hóa hình thức đa tạp Poisson) và không thay kết quả thứ ba bằng đối xứng gương đồng điều.
- Tự tay tính tích sao Moyal bậc $$\hbar^1, \hbar^2$$ trên mặt phẳng pha $$(q,p)$$ để cảm nhận tận mắt lượng tử hóa biến dạng làm gì.
- Phát biểu ý chính của giả thuyết Witten (hàm sinh số giao lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ là hàm tau của hệ KdV) và cách Kontsevich chứng minh bằng đồ thị ruy-băng và tích phân ma trận Airy.
- Mô tả tích phân Kontsevich như **bất biến kiểu hữu hạn phổ dụng**, đồng thời ghi công Vassiliev và Bar-Natan.
- Giải thích vì sao đa tạp Poisson khó hơn đa tạp symplectic (không có tọa độ Darboux), và cách **Định lý hình thức (Formality)** cùng công thức đồ thị trên nửa mặt phẳng trên giải quyết trọn vẹn bài toán.
- Đặt các công trình này lên bản đồ [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/) mà không đánh đồng trực giác vật lý với chứng minh toán học.

**Kiến thức nền.** Khái niệm không gian moduli của đường cong; móc Poisson trên $$\mathbb{R}^{2n}$$ hoặc trên đa tạp symplectic; đa thức Jones như một ví dụ về bất biến nút ngoài nhóm cơ bản. Biết giải tích phức và một giáo trình nhập môn hình học đại số sẽ có ích. Lý thuyết trường lượng tử thì không bắt buộc.

**Liên kết với các bài khác.** Bài [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/) trình bày chương trình HMS, nên đọc *sau* và tách biệt với giải năm 1998. Bài [Pardon / symplectic]({{ site.baseurl }}/contents/vi/chapter02/02_13_Pardon_Symplectic/) nói về phía phạm trù Fukaya, nơi HMS được sử dụng.

---

## Bản đồ kiến thức nền: Lượng tử hóa biến dạng, Không gian moduli và Lý thuyết nút nghiên cứu gì?

### 1. Lượng tử hóa biến dạng (Deformation Quantization) là gì?
Trong cơ học cổ điển, các đại lượng vật lý là hàm trơn $$f(q,p), g(q,p)$$ trên **không gian pha** với phép nhân giao hoán thông thường $$fg = gf$$ và một **móc Poisson** phản đối xứng $$\{f, g\}$$ thỏa đồng nhất thức Jacobi và quy tắc Leibniz (không gian trang bị móc như vậy gọi là **đa tạp Poisson**). Sang cơ học lượng tử, vị trí và động lượng không giao hoán nữa: $$[\hat{q}, \hat{p}] = i\hbar$$. **Lượng tử hóa biến dạng** đặt câu hỏi đại số: *liệu có thể biến dạng phép nhân giao hoán $$fg$$ thành một **tích sao** $$f \star g = fg + \hbar B_1(f,g) + \hbar^2 B_2(f,g) + \cdots$$ vẫn có tính **kết hợp**, sao cho $$f\star g - g\star f = i\hbar\{f,g\} + O(\hbar^2)$$ hay không?*

### 2. Không gian moduli $$\overline{\mathcal{M}}_{g,n}$$ và lý thuyết giao
Tập hợp tất cả các mặt Riemann (đường cong đại số phức) giống $$g$$ có $$n$$ điểm đánh dấu tạo thành **không gian moduli** $$\mathcal{M}_{g,n}$$, và khi bổ sung các mặt suy biến có điểm nút ta được không gian compact $$\overline{\mathcal{M}}_{g,n}$$ (compact hóa Deligne–Mumford, chiều phức $$3g - 3 + n$$). Lý thuyết giao hỏi: *nếu lấy tích phân các lớp đặc trưng tự nhiên (lớp $$\psi_i$$) trên $$\overline{\mathcal{M}}_{g,n}$$, những con số hữu tỷ thu được tuân theo quy luật gì?*

### 3. Bất biến nút kiểu hữu hạn (Vassiliev)
Một **nút** là vòng dây khép kín trong $$\mathbb{R}^3$$. **Vassiliev** phân loại các bất biến nút bằng cách lấy sai phân mỗi khi cho hai sợi dây xuyên qua nhau (đổi chỗ bắt chéo): bất biến nào triệt tiêu sau $$m+1$$ lần đổi chỗ gọi là **bất biến kiểu hữu hạn bậc $$\le m$$**. Câu hỏi cốt lõi: *có tồn tại một bất biến "mẹ" duy nhất sinh ra tất cả các bất biến kiểu hữu hạn không?*

---

## 1. Ví dụ cầm tay chỉ việc: tự tính tích sao Moyal và số giao trên $$\overline{\mathcal{M}}_{g,n}$$

### Ví dụ 1: Tích sao Moyal trên mặt phẳng pha $$\mathbb{R}^2$$ với tọa độ $$(q, p)$$
Trên $$\mathbb{R}^2$$ với móc Poisson chuẩn $$\{f, g\} = \frac{\partial f}{\partial q}\frac{\partial g}{\partial p} - \frac{\partial f}{\partial p}\frac{\partial g}{\partial q}$$ (đặc biệt $$\{q, p\} = 1$$), **tích sao Moyal** được viết gọn bằng toán tử vi phân:

$$
(f \star g)(q,p) = fg + \frac{i\hbar}{2}\Bigl(f_q g_p - f_p g_q\Bigr) + \frac{1}{2!}\left(\frac{i\hbar}{2}\right)^2\Bigl(f_{qq}g_{pp} - 2f_{qp}g_{qp} + f_{pp}g_{qq}\Bigr) + \cdots
$$

Hãy tự tay thay hai cặp hàm cực đơn giản vào công thức:
1. **Với $$f = q$$ và $$g = p$$:** chỉ có đạo hàm bậc 1 khác không ($$f_q = 1, g_p = 1$$), nên:
   $$
   q \star p = qp + \frac{i\hbar}{2}, \qquad p \star q = pq - \frac{i\hbar}{2} \;\Longrightarrow\; q \star p - p \star q = i\hbar = i\hbar\{q, p\}!
   $$
2. **Với $$f = q^2$$ và $$g = p^2$$:** ta có $$f_q = 2q, f_{qq} = 2$$ và $$g_p = 2p, g_{pp} = 2$$, nên số hạng bậc $$\hbar^2$$ cũng xuất hiện:
   $$
   q^2 \star p^2 = q^2 p^2 + \frac{i\hbar}{2}(4qp) + \frac{(i\hbar)^2}{8}(2\cdot 2) = q^2 p^2 + 2i\hbar qp - \frac{\hbar^2}{2}.
   $$
   Bạn có thể tự kiểm tra ngay bằng đại số sơ cấp: $$(q \star q) \star p = q \star (q \star p) = q^2 p + i\hbar q$$ — **tính kết hợp được bảo toàn hoàn hảo!**

Công thức Moyal hoạt động dễ dàng như thế chỉ vì các hệ số của móc Poisson $$\pi$$ là **hằng số** (đạo hàm của $$\pi$$ bằng $$0$$)! Ngay khi sang một **đa tạp Poisson tổng quát** nơi $$\pi(x)$$ biến thiên theo tọa độ $$x$$ (chẳng hạn $$\{x, y\} = x y$$ hay cấu trúc Lie–Poisson $$\{x_i, x_j\} = \sum c_{ij}^k x_k$$), công thức Moyal gãy ngay ở bậc $$\hbar^2$$ vì tính kết hợp bị phá vỡ bởi các đạo hàm của $$\pi$$!

### Ví dụ 2: Hai số giao đầu tiên của giả thuyết Witten
Các số giao tautological trên $$\overline{\mathcal{M}}_{g,n}$$ được định nghĩa là $$\langle\tau_{d_1}\cdots\tau_{d_n}\rangle_g = \int_{\overline{\mathcal{M}}_{g,n}} \psi_1^{d_1}\cdots\psi_n^{d_n}$$ (khác $$0$$ chỉ khi $$\sum d_i = 3g - 3 + n$$):
- Với $$g = 0, n = 3$$: chiều phức là $$3(0) - 3 + 3 = 0$$, không gian $$\overline{\mathcal{M}}_{0,3}$$ chỉ là một điểm duy nhất, nên $$\langle\tau_0^3\rangle_0 = 1$$.
- Với $$g = 1, n = 1$$: chiều phức là $$3(1) - 3 + 1 = 1$$, và phép tính hình học cho $$\langle\tau_1\rangle_1 = \frac{1}{24}$$ (hệ số $$1/24$$ xuất hiện vì đường cong elliptic có nhóm tự đẳng cấu cấp $$2$$ và liên hệ với dạng modular!).

**Giả thuyết Witten** dự đoán hàm sinh $$F(t_0, t_1, \ldots)$$ của toàn bộ vô hạn các số giao này thỏa hệ phương trình **KdV** — chỉ từ hai phương trình dây và giãn (ràng buộc Virasoro) cùng điều kiện ban đầu $$\langle\tau_0^3\rangle_0 = 1$$, ta tính đệ quy ra *tất cả* các số giao ở mọi giống $$g$$!

---

## 2. Hai trụ cột đầu tiên của Fields 1998: Giả thuyết Witten và Tích phân Kontsevich

**1. Chứng minh giả thuyết Witten (1992).** Trong bài báo *Intersection theory on the moduli space of curves and the matrix Airy function* (*Comm. Math. Phys.* 147), Kontsevich dùng định lý **vi phân Strebel** để cắt mỗi mặt Riemann có điểm đánh dấu thành một **đồ thị ruy-băng** (*ribbon graph* — đồ thị có thứ tự cạnh quanh mỗi đỉnh). Phép chia ô bằng đồ thị ruy-băng biến tích phân hình học của các lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ thành một **tổng trên tất cả các đồ thị ruy-băng bậc 3** — mà theo quy tắc khai triển Feynman, tổng này chính là khai triển tiệm cận của **tích phân ma trận Airy** trên không gian ma trận Hermite $$N\times N$$! Vì tích phân ma trận Airy đã được biết là hàm tau của hệ KdV, giả thuyết Witten được chứng minh trọn vẹn!

**2. Bất biến Vassiliev phổ dụng — Tích phân Kontsevich (1993).** **Vassiliev** đưa ra lọc kiểu hữu hạn, còn **Bar-Natan** hệ thống hóa phần tổ hợp gồm **sơ đồ dây** (*chord diagrams*) và **hệ trọng số** (như từ đại số Lie $$\mathfrak{sl}_2$$ sinh ra đa thức Jones). Kontsevich xây dựng công cụ giải tích **phổ dụng** biến *mọi* hệ trọng số thành một bất biến nút thật: nhúng nút $$K$$ vào $$\mathbb{C} \times \mathbb{R}$$ và lấy **tích phân lặp** của dạng vi phân logarit $$\frac{dz_j - dz'_j}{z_j - z'_j}$$ trên không gian cấu hình các điểm cắt nút tại các độ cao $$t_1 < \cdots < t_m$$. Ở bậc $$m = 1$$, nó thu về đúng **tích phân số móc nối Gauss** cổ điển; ở mọi bậc, nó là hiện thực toán học chặt chẽ của chuỗi nhiễu loạn Chern–Simons mà Witten từng gợi ý. Mọi bất biến kiểu hữu hạn (kể cả đa thức Jones, HOMFLY-PT) đều thu được từ tích phân Kontsevich!

---

## 3. Khung giải thích: Định lý hình thức (Formality) và lượng tử hóa mọi đa tạp Poisson (nên đọc chậm)

Tại sao bài toán lượng tử hóa biến dạng cho đa tạp **Poisson tổng quát** lại đứng vững suốt 20 năm sau khi De Wilde–Lecomte (1983) và Fedosov (1994) đã giải xong cho đa tạp symplectic? Dưới đây là 4 bước đột phá của Kontsevich (bản thảo 1997, arXiv:q-alg/9709040; *Lett. Math. Phys.* 2003):

#### Bước 1: Vì sao cách ghép địa phương của đa tạp symplectic thất bại?
Trên đa tạp symplectic, định lý Darboux đảm bảo quanh mọi điểm đều có tọa độ đưa $$\pi$$ về dạng hằng, nên ta có thể đặt tích Moyal lên từng mảnh nhỏ rồi dán lại bằng liên thông Fedosov. Nhưng trên đa tạp Poisson tổng quát (ví dụ $$\{x, y\} = x^2 + y^2$$), hạng của $$\pi$$ tụt về $$0$$ tại gốc tọa độ — **không hề tồn tại tọa độ Darboux**! Muốn có tích sao, ta phải tìm một công thức **tự nhiên theo mọi $$\pi$$ biến thiên**.

#### Bước 2: Nâng bài toán lên hai đại số Lie vi phân phân bậc (DGLA)
Kontsevich nhìn cả hai phía — "cấu trúc Poisson" và "tích sao kết hợp" — như nghiệm của **phương trình Maurer–Cartan** $$d\gamma + \frac{1}{2}[\gamma, \gamma] = 0$$ trong hai đại số Lie vi phân phân bậc:
- **Phía hình học ($$T_{\mathrm{poly}}$$):** các trường đa vector với móc Schouten–Nijenhuis và vi phân $$d = 0$$. Nghiệm Maurer–Cartan chính là các cấu trúc Poisson $$[\pi, \pi] = 0$$.
- **Phía đại số ($$D_{\mathrm{poly}}$$):** phức đối xích Hochschild các toán tử đa vi phân trên $$C^\infty(M)$$. Nghiệm Maurer–Cartan chính là các **tích sao kết hợp**!

Theo định lý Hochschild–Kostant–Rosenberg (HKR), đối đồng điều của $$D_{\mathrm{poly}}$$ đẳng cấu với $$T_{\mathrm{poly}}$$, nhưng ánh xạ HKR thông thường lại *không* bảo toàn móc Lie!

#### Bước 3: Định lý hình thức (Formality Theorem)
Kontsevich chứng minh rằng tuy ánh xạ HKR tuyến tính không bảo toàn móc Lie, ta có thể bổ sung các số hạng phi tuyến bậc cao $$U_1, U_2, U_3, \ldots$$ để dựng một **tựa đẳng cấu $$L_\infty$$** từ $$T_{\mathrm{poly}}$$ sang $$D_{\mathrm{poly}}$$! Hệ quả tức thì: mọi phần tử Maurer–Cartan bên phía hình học (mọi cấu trúc Poisson $$\pi$$) tự động được đẩy sang một phần tử Maurer–Cartan bên phía đại số (một **tích sao kết hợp**), và lớp tương đương của tích sao tương ứng **1–1** với lớp tương đương của các cấu trúc Poisson hình thức!

#### Bước 4: Công thức đồ thị tường minh trên nửa mặt phẳng trên Poincaré
Điều khiến cả giới toán học sững sờ là Kontsevich viết ra **công thức đóng tường minh** cho từng số hạng $$\hbar^n B_n(f,g)$$ trên $$\mathbb{R}^d$$:

$$
f \star g = fg + \sum_{n=1}^{\infty} \frac{\hbar^n}{n!} \sum_{\Gamma \in G_n} w_\Gamma \, B_{\Gamma, \pi}(f, g).
$$

Mỗi đồ thị có hướng $$\Gamma$$ có $$n$$ đỉnh nội (đặt $$\pi$$) và $$2$$ đỉnh biên (đặt $$f, g$$), sinh ra một toán tử song vi phân $$B_{\Gamma,\pi}(f,g)$$. Còn con số trọng số $$w_\Gamma$$ là một tích phân hoàn toàn tường minh của các góc cực hyperbolic trên không gian cấu hình $$n$$ điểm nằm trong **nửa mặt phẳng trên** $$\mathbb{H}$$! Chính định lý Stokes trên biên không gian cấu hình chứng minh các trọng số $$w_\Gamma$$ thỏa đúng điều kiện kết hợp ở mọi bậc $$\hbar^n$$!

Tóm tắt sợi chỉ đỏ xuyên suốt cả ba kết quả Fields 1998:

$$
\text{Đồ thị ruy-băng} \leftrightarrow \text{Witten–KdV}, \qquad
\text{Sơ đồ dây} \leftrightarrow \text{Vassiliev phổ dụng}, \qquad
\text{Đồ thị trên } \mathbb{H} \leftrightarrow \text{Tích sao Poisson}.
$$

*(Lưu ý chữ **"hình thức"**: kết quả làm việc trên chuỗi lũy thừa hình thức $$\mathbb{R}[\![\hbar]\!]$$, không khẳng định chuỗi hội tụ theo giá trị số thực của $$\hbar$$ hay xây dựng cơ học lượng tử trên không gian Hilbert cho mọi đa tạp Poisson.)*

---

## 4. Các chương trình liên quan nhưng không phải kết quả thứ ba năm 1998

- **Đối xứng gương đồng điều (HMS):** Trong báo cáo ICM 1994 (Zürich; arXiv:alg-geom/9411018), Kontsevich đề xuất diễn giải đối xứng gương thành tương đương giữa phạm trù dẫn xuất các bó kết hợp trên $$X$$ (mô hình B) và phạm trù Fukaya của đa tạp gương $$Y$$ (mô hình A). Nhiều trường hợp lớn đã trở thành định lý nhờ Seidel, Sheridan, Abouzaid và nhiều tác giả khác, nhưng đây là một chương trình mở dài hơi (xem [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/)), **không** phải kết quả thứ ba của giải Fields 1998.
- **Tích phân motivic:** Kontsevich phác thảo năm 1995 tại Orsay; **Denef–Loeser** phát triển thành lý thuyết đầy đủ — một công trình liên quan đến sau.
- **Ánh xạ ổn định (Gromov–Witten):** Compact hóa không gian ánh xạ từ đường cong là đóng góp nền tảng khác của Kontsevich (Taubes có nhắc tại ICM 1998), nhưng không phải một mục tách riêng trong lời trao giải chính thức.

---

## 5. Vì sao là Huy chương Fields

Huy chương năm 1998 tôn vinh những bộ **từ điển đồ thị–tích phân** biến trực giác vật lý thành định lý toán học chặt chẽ ở cả ba lĩnh vực lớn: hình học đại số (giả thuyết Witten), tôpô (bất biến nút phổ dụng), và đại số–vật lý toán (lượng tử hóa đa tạp Poisson). Trong Chương 2, Kontsevich là minh chứng rõ nét nhất cho thấy vật lý toán có thể trực tiếp sinh ra cấu trúc đại số và chứng minh hoàn chỉnh.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Kontsevich giải đối xứng gương." | Ông đề xuất HMS năm 1994; đó là một chương trình, với nhiều trường hợp đã được nhiều tác giả chứng minh. |
| "Fields 1998 = đối xứng gương đồng điều." | Kết quả thứ ba chính thức là lượng tử hóa hình thức các đa tạp Poisson. |
| "Giả thuyết Witten phân loại mọi đường cong." | Nó mô tả các số giao của lớp $$\psi$$ trên $$\overline{\mathcal{M}}_{g,n}$$ thông qua hệ KdV. |
| "Tích phân Kontsevich là đa thức Jones." | Nó là bất biến kiểu hữu hạn phổ dụng; đa thức Jones là một trong nhiều bất biến rút ra được từ nó. |
| "Lượng tử hóa hình thức là cơ học lượng tử trên không gian Hilbert." | Đó là một biến dạng kết hợp trên $$\mathbb{R}[\![\hbar]\!]$$; sự hội tụ là vấn đề riêng. |
| "Tích phân motivic là kết quả được Fields 1998." | Đó là công trình liên quan, đến sau (bài giảng của Kontsevich; Denef–Loeser). |

---

## Liên kết

- Trang IMU Fields Medal: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Wikipedia — Maxim Kontsevich: [https://en.wikipedia.org/wiki/Maxim_Kontsevich](https://en.wikipedia.org/wiki/Maxim_Kontsevich)
- Kontsevich, lượng tử hóa biến dạng (arXiv:q-alg/9709040): [https://arxiv.org/abs/q-alg/9709040](https://arxiv.org/abs/q-alg/9709040)
- Kontsevich, đại số đồng điều của đối xứng gương (arXiv:alg-geom/9411018): [https://arxiv.org/abs/alg-geom/9411018](https://arxiv.org/abs/alg-geom/9411018)
- AMS Notices, “The Mathematical Work of the 1998 Fields Medalists”: [https://www.ams.org/notices/199901/fields.pdf](https://www.ams.org/notices/199901/fields.pdf)
- Tìm arXiv — Kontsevich Witten moduli: [https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all](https://arxiv.org/search/?query=Kontsevich+Witten+moduli&searchtype=all)

---

## Tài liệu tham khảo

1. Citation IMU Fields Medal 1998 — Maxim Kontsevich (khai mạc ICM Berlin; xem thêm Taubes, “The work of Maxim Kontsevich,” ICM 1998).
2. M. Kontsevich, “Intersection theory on the moduli space of curves and the matrix Airy function,” *Comm. Math. Phys.* 147 (1992).
3. E. Witten, hấp dẫn hai chiều và lý thuyết giao trên không gian moduli (giả thuyết).
4. M. Kontsevich, “Deformation quantization of Poisson manifolds,” *Lett. Math. Phys.* 66 (2003); bản thảo q-alg/9709040.
5. V. Vassiliev, bất biến nút kiểu hữu hạn; D. Bar-Natan, hệ trọng và phức sơ đồ.
6. M. Kontsevich, “Homological algebra of mirror symmetry,” *Proc. ICM Zürich 1994* — chương trình liên quan, không phải gạch thứ ba 1998.
7. J. Denef và F. Loeser, các bài về tích phân motivic (sau bài giảng Orsay của Kontsevich).
8. Khóa học: [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Đối xứng gương]({{ site.baseurl }}/contents/vi/chapter06/06_13_Mirror_Symmetry/).

---

## Hướng đi tiếp

- Đọc một bài giảng hiện đại về các lớp tautological trên $$\overline{\mathcal{M}}_{g,n}$$ để thấy định lý Witten–Kontsevich *không* tính được những gì.
- Nếu học tiếp sang HMS, hãy ghi chép thành hai cột: "đề xuất năm 1994" và "định lý do các tác giả sau chứng minh".

## Video tham khảo

- **Xem trước**: [HLF Laureate Portraits: Maxim Kontsevich](https://www.youtube.com/watch?v=1CXvSRQVoZY) (Heidelberg Laureate Forum, tiếng Anh). Video chân dung ngắn, Kontsevich kể về con đường và cách làm toán của mình. Phù hợp để làm quen trước khi đọc bài.
- [Maxim Kontsevich | On the History of quantum cohomology and homological mirror symmetry](https://www.youtube.com/watch?v=Ml2x5NnEQ1I) (Harvard CMSA, tiếng Anh). Kontsevich kể lại lịch sử đối đồng điều lượng tử và đối xứng gương đồng điều. Nên xem sau khi đọc mục 5, để phân biệt rõ đề xuất HMS năm 1994 với ba kết quả của giải năm 1998.
