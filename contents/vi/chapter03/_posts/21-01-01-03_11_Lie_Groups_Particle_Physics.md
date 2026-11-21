---
layout: post
title: "Đối xứng, nhóm Lie và vật lý hạt"
chapter: '03'
order: 11
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
---

Nếu hình học là ngôn ngữ của không – thời gian, thì **đối xứng** là ngôn ngữ của các định luật bảo toàn và của việc phân loại hạt. Vật lý hạt thế kỷ 20 đã đặt cược vào một ý tưởng chính xác: các lực cơ bản và các nhóm hạt vật chất (multiplet) được tổ chức bởi các **nhóm liên tục**, đặc biệt là các nhóm Lie compact như $$U(1)$$, $$SU(2)$$, $$SU(3)$$, đóng vai trò **đối xứng gauge** hoặc đối xứng vị (flavor) toàn cục.

Bài này nối các ý tưởng toán học về nhóm Lie và biểu diễn với những kết quả vật lý: dòng bảo toàn Noether, quy tắc chọn lọc, và nhóm gauge của Mô hình Chuẩn

$$
G_{\mathrm{SM}} = U(1)_Y \times SU(2)_L \times SU(3)_c
$$

ở mức ý tưởng. Nên đọc kèm bài về vẻ đẹp của [Đối xứng]({{ site.baseurl }}/contents/vi/chapter04/04_04_Symmetry/) và bài về các lực [Gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa không chính thức một **nhóm Lie** (vừa là nhóm vừa là đa tạp trơn, và các phép toán nhóm là trơn).
- Giải thích vì sao vật lý quan tâm đến **biểu diễn**: các hạt nằm trong không gian biểu diễn, chứ không chỉ trong nhóm trừu tượng.
- Phát biểu ý chính của **định lý Noether**: mỗi đối xứng liên tục ứng với một dòng, một đại lượng được bảo toàn.
- Kể tên các thành phần $$U(1)$$, $$SU(2)$$, $$SU(3)$$ của Mô hình Chuẩn và lực, tích tương ứng (siêu tích, rồi điện từ sau khi trộn; spin đồng vị yếu; màu).
- Phân biệt **đối xứng toàn cục** và **đối xứng gauge** ở mức "đối xứng vật lý hay phần dư thừa trong cách mô tả", không cần đến hình thức BRST.
- Tránh các cách nói sai: "$$SU(3)$$ chỉ có nghĩa là có ba quark", "đối xứng là phương trình trông đẹp", "gauge chỉ là một pha toàn cục".

**Kiến thức nền.** Phép nhân ma trận; giá trị riêng của ma trận Hermite; số phức. [Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/).

---

## 1. Nhóm, họ liên tục và đại số Lie

**Nhóm** là một tập hợp có phép nhân kết hợp, có phần tử đơn vị và phần tử nghịch đảo; đó là cấu trúc của các phép đối xứng có thể ghép nối tiếp nhau. **Nhóm Lie** là nhóm đồng thời là một đa tạp trơn, nên các phép đối xứng tạo thành một họ liên tục: các phép quay $$SO(3)$$, các ma trận unita $$U(n)$$, các ma trận unita đặc biệt $$SU(n)$$ (định thức bằng 1).

Gần phần tử đơn vị, nhóm Lie được mô tả bởi **đại số Lie**: không gian tiếp xúc tại đơn vị, với móc Lie $$[X,Y]$$ đo mức độ không giao hoán của các phép biến đổi vô cùng bé. Với nhóm ma trận, đại số Lie gồm các ma trận đóng kín với phép lấy giao hoán tử.

**Ví dụ.** $$SU(2)$$ là nhóm các ma trận unita $$2\times 2$$ có định thức 1. Đại số Lie của nó có 3 chiều và đẳng cấu với đại số của mômen động lượng, nên spin-$$1/2$$ và lưỡng tuyến (doublet) spin đồng vị dùng chung một bộ máy toán học.

---

## 2. Biểu diễn: nơi các hạt "sống"

Một nhóm trừu tượng trở thành vật lý khi nó **tác động lên không gian trạng thái**. Một **biểu diễn** tuyến tính là một đồng cấu

$$
\rho: G \to GL(V)
$$

vào nhóm các ánh xạ tuyến tính khả nghịch trên một không gian vectơ $$V$$.

- **Biểu diễn bất khả quy** đóng vai trò "multiplet cơ bản".  
- Tích tensor cho các tổ hợp nhiều hạt, nhiều quark.  
- Đặc trưng (character) và trọng số cao nhất phân loại các biểu diễn của nhóm compact; đây là toán học thuần túy mà vật lý hạt dùng như một danh mục.

**Chuỗi lập luận ngắn.** Xác định một loại hạt thường có nghĩa là đo **các nhãn của một biểu diễn** (spin, điện tích, chỉ số màu); chính các nhãn này quyết định những kiểu tương tác mà đối xứng cho phép.

---

## 3. Định lý Noether (phát biểu ý chính)

Nếu định luật chuyển động không đổi dưới một họ biến đổi liên tục, thì có một dòng được bảo toàn. Tịnh tiến theo thời gian ứng với bảo toàn năng lượng; tịnh tiến trong không gian ứng với bảo toàn động lượng; phép quay ứng với bảo toàn mômen động lượng; đối xứng pha $$U(1)$$ toàn cục của một trường phức ứng với bảo toàn điện tích (trong lý thuyết thích hợp).

Trong lý thuyết trường, phát biểu này mang tính địa phương (phương trình liên tục $$\partial_\mu j^\mu=0$$). Định lý Noether là cầu nối từ **hình học của đối xứng** sang **việc kiểm kê các đại lượng bảo toàn**.

---

## 4. Đối xứng gauge và đối xứng toàn cục

| | Đối xứng toàn cục | Đối xứng gauge |
|--|-------------------|-----------------|
| Phép biến đổi | Cùng một phần tử nhóm cho toàn bộ không gian (cố định) | $$g(x)$$ thay đổi theo điểm không – thời gian |
| Ý nghĩa | Đối xứng vật lý của hệ | Thường là **phần dư thừa** trong cách mô tả (cả một quỹ đạo gauge ứng với một cấu hình vật lý) |
| Hệ quả | Tích được bảo toàn; cấu trúc multiplet | Lực xuất hiện như trường bù (liên thông) |

Lý thuyết Maxwell đã có đối xứng gauge $$U(1)$$: $$A_\mu\mapsto A_\mu+\partial_\mu\lambda$$. Lý thuyết Yang–Mills tổng quát hóa điều này cho nhóm $$G$$ không giao hoán. Mô hình Chuẩn kết hợp ba thành phần gauge với các biểu diễn xác định cho các fermion.

**Cơ chế Higgs (trong một câu).** Sự phá vỡ tự phát đối xứng gauge điện yếu cho các hạt $$W^\pm$$, $$Z$$ khối lượng, trong khi photon vẫn không có khối lượng; ở đây cần phân biệt đối xứng của phương trình với đối xứng của trạng thái chân không.

---

## 5. Nhóm của Mô hình Chuẩn

$$
\begin{aligned}
SU(3)_c &\quad \text{lực mạnh / màu (QCD)}\\
SU(2)_L &\quad \text{isospin yếu (fermion trái)}\\
U(1)_Y &\quad \text{hypercharge (trộn với }W^3\text{ thành EM)}
\end{aligned}
$$

Quark biến đổi theo biểu diễn tam tuyến (triplet) màu; lepton là đơn tuyến (singlet) màu; tương tác yếu đối xử khác nhau với trường tay trái và tay phải (tính chiral). Đây là dữ liệu về biểu diễn, không phải chi tiết trang trí.

Đây là **lý thuyết biểu diễn được áp dụng ở quy mô rất lớn**: một khi nhóm và các biểu diễn đã cố định, các đỉnh tương tác bị ràng buộc rất chặt.

---

## 6. Những lĩnh vực toán học được nuôi dưỡng bởi cùng ý tưởng

- Lý thuyết cấu trúc của đại số Lie nửa đơn (Cartan, Killing, sơ đồ Dynkin).  
- Vành biểu diễn, phạm trù tensor (về sau dùng cho anyon và các pha tôpô).  
- Các nhóm và đại số vô hạn chiều trong lý thuyết trường bảo giác (CFT) và hệ khả tích.  
- Đối ngẫu giữa nhóm $$G$$ và nhóm đối ngẫu $$G^\vee$$ trong chương trình Langlands và trong các đối ngẫu gauge ([Nguyên lý đối ngẫu]({{ site.baseurl }}/contents/vi/chapter06/06_12_Duality_Principle/)).

Vật lý hạt không phát minh ra lý thuyết Lie. Nhưng suốt một thế kỷ, nó đã **chọn lọc và làm nổi bật** cách đọc dữ liệu qua biểu diễn, và trả lại cho toán học những bài toán mới (dị thường, đối xứng lượng tử).

---

## 7. Phân biệt chính xác và cường điệu

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Vũ trụ là $$SU(3)$$." | Đơn giản hóa quá mức | $$SU(3)$$ chỉ là một thành phần của nhóm gauge mô tả các lực đã biết; không phải "lý thuyết của mọi thứ". |
| "Đối xứng gauge sinh ra lực." | Thô | Bất biến gauge cộng với tính địa phương dẫn đến liên thông; động lực học còn cần một tác dụng (Yang–Mills, …). |
| "Mọi đối xứng đều là nhóm Lie." | Sai | Các đối xứng rời rạc cũng quan trọng. |
| "Biểu diễn là hình vẽ đẹp về hạt." | Thiếu | Đó là tác động tuyến tính trên không gian trạng thái, cho ra các số lượng tử đo được. |

---

## Bài tập

1. **Định nghĩa.** Giải thích bằng lời sự khác nhau giữa nhóm, nhóm Lie và đại số Lie.  
2. **$$SU(2)$$.** Vì sao các ma trận unita $$2\times 2$$ có định thức 1 là "ngôi nhà" tự nhiên của spin-1/2?  
3. **Noether.** Ghép cặp: tịnh tiến thời gian, phép quay, pha toàn cục với năng lượng, mômen động lượng, điện tích.  
4. **Toàn cục và gauge.** Mô tả mỗi loại trong một câu.  
5. **Mô hình Chuẩn.** Thành phần nào chủ yếu ứng với "màu"? Thành phần nào ứng với "spin đồng vị yếu"?  
6. **Cầu nối.** Một biểu diễn của $$G$$ trở thành "trường vật chất trong một phân thớ liên kết" trong bài gauge như hình học như thế nào? (Chỉ cần trả lời ở mức ý tưởng.)

---

## Tài liệu tham khảo

1. Hall — *Lie Groups, Lie Algebras, and Representations*.  
2. Georgi — *Lie Algebras in Particle Physics*.  
3. Khóa học: [Đối xứng]({{ site.baseurl }}/contents/vi/chapter04/04_04_Symmetry/), [Gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/), [Yang–Mills mass gap]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/).  
