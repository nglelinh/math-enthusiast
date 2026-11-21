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

Lý thuyết điện từ của Maxwell chứa một điều bí mật về hình học: thế vectơ $$A$$ không được xác định duy nhất bởi vật lý, vì $$A$$ và $$A+d\lambda$$ cho cùng một cường độ trường $$F=dA$$. Sự dư thừa đó gọi là **đối xứng gauge**. Năm 1954, Yang và Mills mở rộng ý tưởng này từ nhóm đường tròn $$U(1)$$ sang các nhóm không giao hoán như $$SU(2)$$, $$SU(3)$$. Hình học vi phân hiện đại nhận ra khuôn mẫu chung: **trường gauge là một liên thông trên phân thớ chính; cường độ trường là độ cong của liên thông đó.**

Đây là **bài cầu nối chính** của nhánh Vật lý–Toán: một cơ chế làm nền cho Mô hình chuẩn, cho giải tích hình học cổ điển (Uhlenbeck, Donaldson), và cho bài toán còn mở [khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/). Nên đọc sau bài [nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/) và đọc song song với bài [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

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

Với hệ đơn vị và cách viết không–thời gian thích hợp, cường độ trường điện từ là một 2-dạng $$F$$ dựng từ thế là một 1-dạng $$A$$:

$$
F = dA.
$$

Phép biến đổi gauge $$A'=A+d\lambda$$ giữ nguyên $$F$$ vì $$d\circ d=0$$. Phương trình Maxwell thuần nhất $$dF=0$$ tự động thỏa mãn khi $$F=dA$$ (trên miền có tô pô tầm thường). Để ghép với vật chất mang điện, ta cần đạo hàm hiệp biến

$$
D = d - iqA
$$

sao cho phép quay pha cục bộ của hàm sóng phức được $$A$$ bù lại. Đây là cách hình học giải thích nguồn gốc của "ghép tối thiểu" (minimal coupling).

**Cơ chế chính.** Việc được tự do quay pha $$U(1)$$ cục bộ của trường mang điện **buộc** phải có một liên thông bù $$A$$; trong lý thuyết lượng tử, photon là lượng tử của trường đó.

---

## 2. Yang–Mills: độ cong không giao hoán

Với một nhóm Lie compact $$G$$ và một liên thông $$A$$ nhận giá trị trong đại số Lie,

$$
F = dA + A\wedge A.
$$

Khi $$G=U(1)$$, móc Lie triệt tiêu và ta trở lại lý thuyết Maxwell. Với $$SU(2)$$ hay $$SU(3)$$, số hạng bậc hai làm cho phương trình trường trở thành **phi tuyến**: gluon mang màu và tự tương tác với nhau.

Tác dụng Yang–Mills

$$
S[A]\propto \int \operatorname{tr}(F\wedge\star F)
$$

là một phiếm hàm năng lượng cổ điển, có các điểm tới hạn là các liên thông Yang–Mills. Ở bốn chiều, các liên thông tự đối ngẫu (instanton) làm cực tiểu tác dụng trong từng lớp tô pô, ứng với các số Chern.

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

**Độ cong như holonomy.** Vận chuyển một "hệ khung" nội tại quanh một vòng rất nhỏ cho một phần tử nhóm dạng $$1+F+\cdots$$. Độ cong khác không nghĩa là vận chuyển song song phụ thuộc vào đường đi. Hãy so sánh với độ cong thủy triều trong thuyết tương đối rộng (ở đó là phân thớ tiếp xúc và liên thông metric), khác với phân thớ gauge nội tại.

**Phân thớ** giúp xử lý chặt chẽ các vấn đề toàn cục: đơn cực từ, số instanton, việc "không chọn được một gauge toàn cục" là chuyện tô pô, không chỉ là bất tiện về tọa độ.

---

## 4. Từ hình học đến Mô hình chuẩn (tổng quan)

| Nhóm gauge thành phần | Lực (nói gọn) | Biểu diễn của vật chất (ý chính) |
|---------------|---------|------------------------------|
| $$SU(3)_c$$ | Tương tác mạnh / QCD | Quark, bộ ba màu |
| $$SU(2)_L$$ | Isospin yếu | Bộ đôi thuận tay trái |
| $$U(1)_Y$$ | Siêu tích yếu | Gán giá trị $$Y$$; trộn lại để cho điện từ |

Câu chuyện lượng tử đầy đủ còn cần tái chuẩn hóa, phá vỡ đối xứng tự phát (cơ chế Higgs), và biểu diễn chiral của fermion. Nhưng **khung xương hình học** vẫn là: mỗi lực ↔ một liên thông cho nhóm $$G$$, cùng với các biểu diễn được chỉ định.

---

## 5. Instanton và tô pô (vì sao số Chern xuất hiện trong vật lý)

Trên một đa tạp 4 chiều định hướng, đóng (hoặc trên $$\mathbb{R}^4$$ với điều kiện suy giảm thích hợp), tích phân

$$
k = \frac{1}{8\pi^2}\int \operatorname{tr}(F\wedge F)
$$

là một bất biến tô pô nhận giá trị nguyên (số Chern thứ hai, hay số instanton, tùy quy ước chuẩn hóa). Một liên thông tự đối ngẫu với $$k\neq 0$$ là một **instanton**: một nghiệm có tác dụng hữu hạn, không thể biến dạng liên tục về liên thông tầm thường trong lớp tô pô của nó.

**Về vật lý.** Instanton mô tả hiệu ứng đường hầm giữa các chân không, tạo nên cấu trúc chân không $$\theta$$, và tham gia vào các quy tắc chọn liên quan đến dị thường. **Về toán học.** Cũng số nguyên đó đánh dấu các thành phần liên thông của không gian moduli và là nền tảng cho các phép dựng kiểu Donaldson.

Bạn không cần học đầy đủ lý thuyết Chern–Weil, chỉ cần nắm bài học: **một phiếm hàm năng lượng trên các liên thông "nhìn thấy" được tô pô**, vì vậy giải tích và tô pô đại số phải làm việc cùng nhau.

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

**Định lý compact của Uhlenbeck.** Một dãy liên thông có năng lượng Yang–Mills bị chặn chỉ có thể bùng nổ theo cách được kiểm soát; các "bọt" (instanton) có thể tập trung tại một điểm ([Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/)).

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

Giả sử $$A$$ là một liên thông $$U(1)$$ trên mặt phẳng bỏ gốc tọa độ, với $$\int_{S^1}A=2\pi\alpha$$. Vận chuyển song song pha của một hạt điện tích $$q$$ quanh đường tròn đơn vị nhân hàm sóng với $$e^{iq\oint A}$$. Dù $$F=0$$ trên mặt phẳng bỏ gốc, holonomy vẫn có thể không tầm thường. Đó là ý chính của hiệu ứng **Aharonov–Bohm**: thế và tô pô có thể quan trọng ngay cả ở nơi $$F$$ triệt tiêu cục bộ.

Với holonomy không giao hoán, pha được thay bằng một ma trận trong $$G$$; mũ sắp thứ tự theo đường đi không giao hoán phản ánh cấu trúc $$A\wedge A$$.

---

## Bài tập

1. **Phép biến đổi gauge.** Chứng minh $$F=dA$$ không đổi khi $$A\mapsto A+d\lambda$$.  
2. **Số hạng không giao hoán.** Vì sao $$A\wedge A$$ triệt tiêu khi $$A$$ là vô hướng (giao hoán) nhưng không triệt tiêu khi $$A$$ là ma trận?  
3. **Từ điển.** Ghép cặp: liên thông, độ cong, holonomy, phân thớ liên kết ↔ $$A$$, $$F$$, vòng Wilson, trường vật chất.  
4. **Mô hình chuẩn.** Nhóm gauge thành phần nào gắn với màu?  
5. **Các tầng.** Trong không quá 100 chữ, phân biệt giải tích Yang–Mills cổ điển với bài toán lượng tử của Clay.  
6. **Nói chính xác.** Viết lại câu: "Toán học vẫn chưa hiểu lý thuyết gauge nên vật lý hạt đứng trên một nền móng lung lay."  
7. **Cầu nối.** Viết một đoạn nối bài này với định lý Atiyah–Singer hoặc với kết quả của Uhlenbeck.

---

## Tài liệu tham khảo

1. Baez & Muniain, *Gauge Fields, Knots and Gravity* (Trường gauge, nút và hấp dẫn).  
2. Nakahara, *Geometry, Topology and Physics* (Hình học, tô pô và vật lý).  
3. David Tong, bài giảng về lý thuyết gauge.  
4. Viện Clay, bài phát biểu bài toán của Jaffe & Witten.  
5. Trong khóa học: [Bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/), [Nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/), [Không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/), [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Atiyah–Singer]({{ site.baseurl }}/contents/vi/chapter08/08_11_Atiyah_Singer_Index/).  
