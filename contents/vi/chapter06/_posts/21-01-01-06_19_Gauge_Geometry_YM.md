---
layout: post
title: "Lý thuyết gauge như hình học"
chapter: '06'
order: 19
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
lesson_type: bridge_flagship
---

Trong điện từ học cổ điển, các nhà vật lý sớm nhận ra một "sự dư thừa kỳ lạ": cùng một điện trường và từ trường vật lý đo được, nhưng thế vectơ $$A$$ lại không duy nhất — bạn có thể cộng thêm gradient của một hàm tùy ý ($$A \mapsto A + d\lambda$$) mà cường độ trường $$F = dA$$ vẫn y nguyên. Thoạt nhìn, người ta tưởng đó chỉ là chuyện tiện lợi về ký hiệu toán học. Nhưng năm 1954, Dương Chấn Ninh (Chen-Ning Yang) và Robert Mills đặt một câu hỏi táo bạo: điều gì xảy ra nếu ta mở rộng sự tự do đổi hệ quy chiếu nội tại ấy từ nhóm đường tròn giao hoán $$U(1)$$ sang các nhóm quay không giao hoán như $$SU(2)$$ hay $$SU(3)$$? Hai mươi năm sau, cộng đồng toán học và vật lý sửng sốt nhận ra hai bên đang nói về cùng một đối tượng: **trường gauge chính là một liên thông (connection) trên phân thớ chính, còn cường độ trường chính là độ cong (curvature) của liên thông đó.**

Đây là **bài cầu nối chính** của nhánh Vật lý–Toán: một cơ chế hình học duy nhất làm khung xương cho Mô hình chuẩn của vật lý hạt, cho giải tích hình học cổ điển (Uhlenbeck, Donaldson), và cho bài toán Thiên niên kỷ còn mở [khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/). Nên đọc sau bài [nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/) và đọc song song với bài [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## Bản đồ kiến thức nền: Hình học vi phân, Phân thớ chính và Lý thuyết trường chuẩn nghiên cứu những gì?

Với hành trang giải tích nhiều biến và ma trận đại học, bạn có thể nắm trọn ba trụ cột của **hình học trường chuẩn (gauge geometry)** qua ẩn dụ tỉ giá hối đoái và vận chuyển song song:

### 1. Phân thớ chính (Principal Bundle) — "hệ quy chiếu nội tại ở từng điểm"
Hãy tưởng tượng mỗi điểm $$x$$ trên bản đồ không–thời gian $$M$$ có một "đồng tiền nội tệ" hay một "hệ trục quay nội tại" riêng, được mô tả bởi một nhóm Lie $$G$$ (chẳng hạn $$U(1)$$ là vòng tròn pha, $$SU(2)$$ là nhóm quay spin/isospin, $$SU(3)$$ là đối xứng màu). Toàn bộ các bản sao của $$G$$ dính mượt mà lên từng điểm của $$M$$ tạo thành một **phân thớ chính**. Điểm tinh tế của tô pô là ở cấp toàn cục, phân thớ có thể bị "xoắn" (giống dải Möbius khác hình trụ) nên không phải lúc nào cũng chọn được một hệ quy chiếu chung cho cả không gian.

### 2. Liên thông (Connection) và Độ cong (Curvature)
Nếu muốn so sánh trạng thái tại điểm $$x$$ với điểm lân cận $$y$$, bạn cần một quy tắc "quy đổi" dọc theo từng bước đi vô cùng nhỏ — đó chính là **liên thông $$A$$** (thế gauge, giống bảng tỉ giá giữa hai thành phố kề nhau). Nếu bạn đi một vòng kín (Hà Nội → Tokyo → New York → Hà Nội) và đổi tiền liên tục dọc đường mà lúc quay về số tiền bị lệch so với ban đầu, độ lệch trên mỗi đơn vị diện tích vòng kín chính là **độ cong $$F$$** (cường độ trường)! Trên mặt cầu Trái Đất, cầm một cây giáo đi từ Bắc Cực xuống Xích Đạo, rẽ ngang $$90^\circ$$ rồi quay lại Bắc Cực mà luôn giữ giáo song song với chính nó, cây giáo sẽ xoay mất $$90^\circ$$ — đó chính là holonomy đo độ cong.

### 3. Lý thuyết Yang–Mills cổ điển vs. lượng tử
- **Phía hình học cổ điển (toán thuần túy đã chín muồi):** Tìm các liên thông $$A$$ cực tiểu hóa năng lượng độ cong $$\int \operatorname{tr}(F\wedge\star F)$$, giải phương trình đạo hàm riêng phi tuyến, khảo sát không gian nghiệm (moduli) để phân biệt các đa tạp 4 chiều (Uhlenbeck, Donaldson).
- **Phía vật lý lượng tử (Mô hình chuẩn & bài toán Clay):** Lượng tử hóa toàn bộ không gian các liên thông. Trong vật lý hạt, đây là bộ công cụ dự đoán chuẩn xác nhất lịch sử; nhưng chứng minh chặt chẽ sự tồn tại và khe khối lượng ở 4 chiều vẫn là bài toán Thiên niên kỷ còn mở.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích **sự dư thừa gauge** trong điện từ học: với $$A\mapsto A+d\lambda$$ thì $$F=dA$$ không đổi.
- Viết công thức độ cong không giao hoán $$F=dA+A\wedge A$$ và giải thích vì sao số hạng thêm vào là quan trọng.
- Nêu ý chính **liên thông ↔ vận chuyển song song; độ cong ↔ holonomy phụ thuộc vào đường đi**.
- Liên hệ các lực trong Mô hình chuẩn với các **nhóm gauge** $$U(1),SU(2),SU(3)$$ ở mức tổng quan.
- Phân biệt **hình học gauge cổ điển** (phương trình đạo hàm riêng, không gian moduli, tô pô) với **Yang–Mills lượng tử** (bài toán Clay về sự tồn tại và khe khối lượng).
- Kể được toán học thuần túy đã tiếp nhận lý thuyết gauge như thế nào: định lý compact của Uhlenbeck, bất biến Donaldson, lý thuyết chỉ số.
- Tập nói chính xác: "lý thuyết gauge" không tự động là một Lý thuyết của vạn vật đã hoàn chỉnh.

**Kiến thức nền.** Giải tích nhiều biến; ma trận; nên đọc trước bài [nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/). Bài [hình học không–thời gian]({{ site.baseurl }}/contents/vi/chapter03/03_10_Geometry_Spacetime_GR/) giúp có trực giác về độ cong.

---

## 1. Maxwell: ví dụ mẫu trường hợp giao hoán

Với hệ đơn vị và cách viết không–thời gian thích hợp, cường độ trường điện từ là một 2-dạng $$F$$ (chứa cả điện trường $$\mathbf{E}$$ và từ trường $$\mathbf{B}$$) dựng từ thế là một 1-dạng $$A$$:

$$
F = dA.
$$

Phép biến đổi gauge $$A'=A+d\lambda$$ giữ nguyên $$F$$ vì đạo hàm ngoài thỏa mãn $$d\circ d=0$$ (chính là đồng nhất thức quen thuộc $$\nabla \times (\nabla \lambda) = 0$$ trong giải tích vectơ 3 chiều). Phương trình Maxwell thuần nhất $$dF=0$$ tự động thỏa mãn khi $$F=dA$$ (trên miền có tô pô tầm thường). Để ghép với vật chất mang điện (một hàm sóng phức $$\psi(x)$$), ta cần đạo hàm hiệp biến

$$
D = d - iqA
$$

sao cho khi ta xoay pha của hàm sóng tùy ý tại từng điểm, $$\psi(x) \mapsto e^{iq\lambda(x)}\psi(x)$$, số hạng thừa sinh ra từ đạo hàm của $$\lambda(x)$$ được chính phép dịch $$A \mapsto A + d\lambda$$ triệt tiêu hoàn hảo. Đây là cách hình học giải thích nguồn gốc của "ghép tối thiểu" (minimal coupling).

**Cơ chế chính.** Việc đòi hỏi vật lý bất biến dưới phép quay pha $$U(1)$$ cục bộ của trường mang điện **buộc** phải có một liên thông bù $$A$$; trong lý thuyết lượng tử, photon chính là lượng tử của trường liên thông đó.

---

## 2. Yang–Mills: độ cong không giao hoán

Với một nhóm Lie compact $$G$$ (như $$SU(2)$$ hay $$SU(3)$$) và một liên thông $$A$$ nhận giá trị trong đại số Lie (có thể nghĩ cụ thể là các ma trận phản Hermite), công thức độ cong mang thêm một số hạng phi tuyến:

$$
F = dA + A\wedge A.
$$

Khi $$G=U(1)$$, các thành phần của $$A$$ là số thực/phức giao hoán với nhau nên số hạng $$A \wedge A$$ triệt tiêu và ta trở lại lý thuyết Maxwell tuyến tính — hai tia sáng đi xuyên qua nhau không tự tương tác. Ngược lại, với $$SU(2)$$ hay $$SU(3)$$, các ma trận trong $$A$$ **không giao hoán**, nên $$A \wedge A$$ khác không và làm cho phương trình trường trở thành **phi tuyến**: hạt truyền lực gluon bản thân nó cũng mang điện tích màu và **tự tương tác với chính nó**.

### Khung giải thích: vì sao thế gauge hằng số vẫn sinh ra trường khác không? (nên đọc chậm)

Trong điện từ học giao hoán $$U(1)$$, nếu thế vectơ $$\mathbf{A}$$ là hằng số khắp không gian thì mọi đạo hàm đều bằng $$0$$, suy ra cường độ trường $$\mathbf{B} = \nabla \times \mathbf{A} = 0$$. Nhưng trong lý thuyết **Yang–Mills $$SU(2)$$**, điều kỳ diệu xảy ra ngay cả khi thế gauge không hề thay đổi theo tọa độ! Hãy tự tay kiểm tra bằng ma trận $$2 \times 2$$:

1. **Chọn hai thành phần liên thông hằng số** nằm trong đại số Lie $$\mathfrak{su}(2)$$ (các ma trận $$2\times 2$$ phản Hermite có vết bằng 0):
   $$
   A_x = \frac{i}{2}\sigma_1 = \begin{pmatrix} 0 & i/2 \\ i/2 & 0 \end{pmatrix}, \qquad A_y = \frac{i}{2}\sigma_2 = \begin{pmatrix} 0 & 1/2 \\ -1/2 & 0 \end{pmatrix}.
   $$
2. **Tính phần đạo hàm:** Vì $$A_x$$ và $$A_y$$ là ma trận hằng số, ta có $$\partial_x A_y = 0$$ và $$\partial_y A_x = 0$$.
3. **Tính phần giao hoán tử $$[A_x, A_y] = A_x A_y - A_y A_x$$:**
   $$
   A_x A_y = \begin{pmatrix} 0 & i/2 \\ i/2 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1/2 \\ -1/2 & 0 \end{pmatrix} = \begin{pmatrix} -i/4 & 0 \\ 0 & i/4 \end{pmatrix},
   $$
   $$
   A_y A_x = \begin{pmatrix} 0 & 1/2 \\ -1/2 & 0 \end{pmatrix}\begin{pmatrix} 0 & i/2 \\ i/2 & 0 \end{pmatrix} = \begin{pmatrix} i/4 & 0 \\ 0 & -i/4 \end{pmatrix}.
   $$
4. **Đọc ra độ cong $$F_{xy}$$:**
   $$
   F_{xy} = \partial_x A_y - \partial_y A_x + [A_x, A_y] = \begin{pmatrix} -i/2 & 0 \\ 0 & i/2 \end{pmatrix} = -\frac{i}{2}\sigma_3 \neq 0!
   $$

Chỉ bằng 3 dòng nhân ma trận $$2\times 2$$, bạn vừa thấy tận mắt lý do số hạng $$A \wedge A$$ thay đổi toàn bộ vật lý: hai phép vận chuyển song song theo hướng $$x$$ rồi $$y$$ không khớp với đi theo $$y$$ rồi $$x$$, tạo ra độ cong ngay từ sự tự tương tác của bản thân trường gauge!

Tác dụng Yang–Mills

$$
S[A]\propto \int \operatorname{tr}(F\wedge\star F)
$$

là một phiếm hàm năng lượng cổ điển (tổng quát hóa trực tiếp của tích phân $$\int (|\mathbf{E}|^2 + |\mathbf{B}|^2)$$ trong điện từ học), có các điểm tới hạn là các liên thông Yang–Mills. Ở bốn chiều, các liên thông tự đối ngẫu (instanton) làm cực tiểu tác dụng trong từng lớp tô pô, ứng với các số Chern.

---

## 3. Ngôn ngữ phân thớ (từ điển hình học)

| Thuật ngữ vật lý | Thuật ngữ hình học |
|-----------|-------------|
| Thế gauge $$A$$ | Liên thông trên phân thớ chính $$G$$ |
| Cường độ trường $$F$$ | Độ cong của liên thông |
| Phép biến đổi gauge | Đổi cách tầm thường hóa cục bộ / tự đẳng cấu thẳng đứng |
| Trường vật chất | Lát cắt của phân thớ vectơ liên kết (ứng với một biểu diễn của $$G$$) |
| Vận chuyển song song | Mũ sắp thứ tự theo đường đi của $$A$$ |
| Vòng Wilson | Holonomy quanh một đường cong kín |

**Độ cong như holonomy.** Vận chuyển một "hệ khung" nội tại quanh một vòng rất nhỏ diện tích $$\Delta S$$ cho một phần tử nhóm dạng $$1 + F\,\Delta S + \cdots$$. Độ cong khác không nghĩa là vận chuyển song song phụ thuộc vào đường đi. Hãy so sánh với độ cong thủy triều trong thuyết tương đối rộng (ở đó là phân thớ tiếp xúc và liên thông metric), khác với phân thớ gauge nội tại.

**Phân thớ** giúp xử lý chặt chẽ các vấn đề toàn cục: đơn cực từ Dirac (không thể viết một thế $$A$$ trơn duy nhất trên cả mặt cầu $$S^2$$ mà phải vá từ hai mảnh Bắc bán cầu và Nam bán cầu qua một phép biến đổi gauge ở Xích Đạo), số instanton, hay việc "không chọn được một gauge toàn cục" là chuyện tô pô thật sự, không chỉ là bất tiện về tọa độ.

---

## 4. Từ hình học đến Mô hình chuẩn (tổng quan)

| Nhóm gauge thành phần | Lực (nói gọn) | Biểu diễn của vật chất (ý chính) |
|---------------|---------|------------------------------|
| $$SU(3)_c$$ | Tương tác mạnh / QCD | Quark, bộ ba màu |
| $$SU(2)_L$$ | Isospin yếu | Bộ đôi thuận tay trái |
| $$U(1)_Y$$ | Siêu tích yếu | Gán giá trị $$Y$$; trộn lại để cho điện từ |

Câu chuyện lượng tử đầy đủ còn cần tái chuẩn hóa, phá vỡ đối xứng tự phát (cơ chế Higgs), và biểu diễn chiral của fermion. Nhưng **khung xương hình học** vẫn giữ nguyên một nguyên tắc thống nhất: mỗi lực cơ bản ↔ một liên thông cho nhóm $$G$$, cùng với các biểu diễn được chỉ định cho các hạt vật chất.

---

## 5. Instanton và tô pô (vì sao số Chern xuất hiện trong vật lý)

Trên một đa tạp 4 chiều định hướng, đóng (hoặc trên $$\mathbb{R}^4$$ với điều kiện suy giảm thích hợp), tích phân

$$
k = \frac{1}{8\pi^2}\int \operatorname{tr}(F\wedge F)
$$

là một bất biến tô pô nhận giá trị nguyên (số Chern thứ hai, hay số instanton, tùy quy ước chuẩn hóa). Nó giống như công thức Gauss–Bonnet quen thuộc trên mặt 2 chiều ($$\frac{1}{2\pi}\int K\,dA = 2 - 2g$$): dù bạn bóp méo hình học cục bộ ra sao, tổng độ cong vẫn khóa cứng ở một số nguyên tô pô! Một liên thông tự đối ngẫu với $$k\neq 0$$ là một **instanton**: một nghiệm có tác dụng hữu hạn, không thể biến dạng liên tục về liên thông tầm thường ($$F=0$$) trong lớp tô pô của nó.

**Về vật lý.** Instanton mô tả hiệu ứng đường hầm lượng tử giữa các chân không khác nhau, tạo nên cấu trúc chân không $$\theta$$, và tham gia vào các quy tắc chọn liên quan đến dị thường. **Về toán học.** Cũng số nguyên đó đánh dấu các thành phần liên thông của không gian moduli và là nền tảng cho các phép dựng kiểu Donaldson.

Bạn không cần học đầy đủ lý thuyết Chern–Weil, chỉ cần nắm bài học cốt lõi: **một phiếm hàm năng lượng trên các liên thông "nhìn thấy" được tô pô**, vì vậy giải tích và tô pô đại số phải làm việc cùng nhau.

---

## 6. Độ cong gauge và độ cong metric (so sánh với thuyết tương đối rộng)

| | Thuyết tương đối rộng | Lý thuyết gauge Yang–Mills |
|--|---------------------|----------------------------|
| Phân thớ | Phân thớ tiếp xúc / phân thớ khung của không–thời gian | Phân thớ chính $$G$$ nội tại |
| Liên thông | Levi-Civita (xác định từ metric) | Trường gauge $$A$$ (là biến động lực) |
| Độ cong | Riemann / Ricci | $$F=dA+A\wedge A$$ |
| Tác dụng | Einstein–Hilbert | $$\int\operatorname{tr}(F\wedge\star F)$$ |
| "Vật chất" | Tensor năng lượng–xung lượng $$T_{\mu\nu}$$ | Lát cắt của phân thớ liên kết |
| Đối xứng cục bộ | Vi phôi (tinh tế hơn) | Phép biến đổi gauge $$g(x)\in G$$ |

Cả hai đều nói "tương tác ↔ hình học", nhưng hình học hóa trên **những phân thớ khác nhau**. Việc thống nhất hai lý thuyết (và lượng tử hóa hấp dẫn) vẫn là vấn đề mở, không phải bài tập đã giải xong. Xem bài [hình học không–thời gian]({{ site.baseurl }}/contents/vi/chapter03/03_10_Geometry_Spacetime_GR/).

---

## 7. Giải tích cổ điển: những gì toán học thuần túy đã nắm được

**Định lý compact của Uhlenbeck.** Một dãy liên thông có năng lượng Yang–Mills bị chặn chỉ có thể bùng nổ theo cách được kiểm soát; năng lượng có thể tập trung tại hữu hạn điểm thành các "bọt" (instanton) mang lượng năng lượng rời rạc ([Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)).

**Lý thuyết Donaldson.** Không gian moduli các liên thông phản tự đối ngẫu cho ta các bất biến của đa tạp trơn 4 chiều: tô pô được viết lại bằng phương trình đạo hàm riêng của lý thuyết gauge. Sau đó, phương trình Seiberg–Witten làm đơn giản nhiều phần của bức tranh này. Đây là câu chuyện "vật lý viết lại tô pô" tiêu biểu nhất cuối thế kỷ 20, và được trình bày kỹ hơn trong bài tổng quan về Donaldson–Seiberg–Witten.

**Lý thuyết chỉ số.** Toán tử Dirac ghép với một liên thông có chỉ số giải tích bằng chỉ số tô pô ([Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/)); vật lý dùng điều này để hiểu các mode không chiral và dị thường.

Đây là **các định lý về đối tượng hình học cổ điển hoặc bán cổ điển**, chưa phải là định lý về sự tồn tại của lý thuyết lượng tử mà bài toán Clay yêu cầu.

---

## 8. Yang–Mills lượng tử và các vấn đề mở

Lượng tử hóa bức tranh hình học nghĩa là định nghĩa một lý thuyết trường lượng tử liên tục có giới hạn cổ điển gắn với tác dụng Yang–Mills. Phương pháp nhiễu loạn và mạng lưới cực kỳ hữu ích; nhưng việc dựng lý thuyết Yang–Mills thuần túy 4 chiều một cách kiến thiết, kèm khe khối lượng, vẫn là một [bài toán Thiên niên kỷ]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/).

**Phân biệt các tầng.**

| Tầng | Trạng thái |
|-----|------------|
| Hình học Yang–Mills cổ điển | Một lĩnh vực toán học đã trưởng thành |
| Yang–Mills lượng tử nhiễu loạn | Bộ công cụ chuẩn của vật lý; có định lý về tính tái chuẩn hóa được |
| Yang–Mills trên mạng lưới | Chính quy hóa được định nghĩa tốt; giới hạn liên tục còn tinh tế |
| Yang–Mills 4 chiều kiến thiết, kèm khe khối lượng | Bài toán Clay còn mở |

---

## 9. Các phép đối ngẫu và những phát triển hiện đại

Đối ngẫu điện–từ, đối ngẫu S của Yang–Mills siêu đối xứng, và cầu nối Langlands hình học xem xét **cả một họ lý thuyết** liên hệ với nhau qua các phép đối ngẫu, thay vì một Lagrangian duy nhất ([Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/)). Đối xứng gương và AdS/CFT mở rộng cuộc đối thoại "hình học từ trường, trường từ hình học". Luôn ghi rõ: đâu là định lý, đâu là chương trình dựa trên giả thuyết.

---

## 10. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Lý thuyết gauge là Lý thuyết của vạn vật." | Thổi phồng | Đó là khung cho các lực đã biết (cộng với các chương trình nghiên cứu); hấp dẫn và việc lượng tử hóa vẫn còn mở. |
| "Công thức $$F=dA+A^2$$ đẹp nên lý thuyết lượng tử đã chặt chẽ." | Sai | Đẹp không có nghĩa là đã dựng được theo nghĩa kiến thiết. |
| "Holonomy chỉ là cách nói của toán học cho từ trường." | Thiếu | Holonomy là dữ liệu của vận chuyển song song; $$B$$ là thành phần của độ cong trong một gauge cụ thể. |
| "Bất biến Donaldson là kết quả thực nghiệm của vật lý hạt." | Nhầm loại | Đó là bất biến của tô pô trơn, lấy cảm hứng từ không gian moduli Yang–Mills. |

---

## 11. Ví dụ nhỏ: pha thu được sau một vòng (trường hợp giao hoán)

Giả sử $$A$$ là một liên thông $$U(1)$$ trên mặt phẳng bỏ gốc tọa độ $$\mathbb{R}^2 \setminus \{0\}$$ (ví dụ bên ngoài một ống dây từ mảnh đặt tại gốc tọa độ), với $$\int_{S^1}A=2\pi\alpha$$. Vận chuyển song song pha của một hạt điện tích $$q$$ quanh đường tròn đơn vị nhân hàm sóng với thừa số pha $$e^{iq\oint A} = e^{2\pi i q\alpha}$$. Dù độ cong $$F=0$$ tại mọi điểm hạt đi qua (từ trường bằng không ngoài ống dây), holonomy vẫn khác $$1$$ nếu $$q\alpha \notin \mathbb{Z}$$ và làm dịch chuyển vân giao thoa đo được! Đó là ý chính của hiệu ứng **Aharonov–Bohm**: thế gauge và tô pô của miền (lỗ thủng ở gốc tọa độ) có tác động vật lý thực sự ngay cả ở nơi $$F$$ triệt tiêu cục bộ.

Với holonomy không giao hoán, thừa số pha vô hướng được thay bằng một ma trận trong $$G$$; mũ sắp thứ tự theo đường đi không giao hoán phản ánh chính cấu trúc $$A\wedge A$$.

---

## Tài liệu tham khảo

1. Baez & Muniain, *Gauge Fields, Knots and Gravity* (Trường gauge, nút và hấp dẫn).  
2. Nakahara, *Geometry, Topology and Physics* (Hình học, tô pô và vật lý).  
3. David Tong, bài giảng về lý thuyết gauge.  
4. Viện Clay, bài phát biểu bài toán của Jaffe & Witten.  
5. Trong khóa học: [Bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/), [Nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/), [Không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/), [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/).  
