---
layout: post
title: "Bài toán tồn tại Yang–Mills và khe khối lượng"
chapter: '01'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
---

Trong các Bài toán Thiên niên kỷ của Viện Clay, có một bài đến từ cơ học chất lỏng ([Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/)) và một bài đến từ lý thuyết lượng tử của trường chuẩn (gauge) không giao hoán: chứng minh rằng lý thuyết Yang–Mills lượng tử tồn tại trong bốn chiều và có **khe khối lượng** (mass gap), tức là có một chặn dưới dương ngặt cho khối lượng của các hạt trong phổ, tách biệt chúng khỏi trạng thái chân không.

Các nhà vật lý dùng lý thuyết Yang–Mills hằng ngày: đó là bộ khung của Mô hình chuẩn về các hạt cơ bản (cùng với các cấu trúc bổ sung cho tương tác điện từ, tương tác yếu và sắc động lực học lượng tử QCD). Các mô phỏng trên lưới và thực nghiệm cho thấy rất rõ hiện tượng giam hãm (confinement) và khe khối lượng trong các lý thuyết chuẩn thuần kiểu QCD. Nhưng bài toán Clay đòi hỏi **toán học ở mức định lý**: xây dựng lý thuyết lượng tử không dựa vào khai triển nhiễu loạn, và chứng minh rằng phổ của toán tử Hamilton (hoặc ma trận chuyển) có một khe phía trên mức năng lượng không.

Bài này phát biểu bài toán một cách cẩn thận, phác thảo phần hình học cổ điển của lý thuyết Yang–Mills, giải thích ý nghĩa của "tồn tại" và "khe khối lượng" theo ngôn ngữ toán học, tóm tắt những gì đã biết trong các số chiều thấp và trên lưới, và lập một bảng giúp đánh giá thận trọng các khẳng định phổ thông (**mục tiêu 1**, **mục tiêu 6**).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu bài toán Clay về **sự tồn tại của lý thuyết Yang–Mills và khe khối lượng** một cách chính xác (không phải "QCD chưa được giải trong phòng thí nghiệm").
- Giải thích ngắn gọn **trường Yang–Mills cổ điển** là gì (liên thông, độ cong, tác dụng) và vì sao nhóm chuẩn **không giao hoán** làm lý thuyết khác với lý thuyết Maxwell.
- Phân biệt **thành công của lý thuyết trường lượng tử nhiễu loạn**, **bằng chứng từ tính toán trên lưới** và **định lý tồn tại theo hướng kiến thiết**.
- Nói được khe khối lượng có nghĩa gì đối với phổ, và vì sao nó liên quan đến lực tầm ngắn và các glueball có khối lượng trong lý thuyết chuẩn thuần.
- Đặt bài toán vào bản đồ khóa học, cạnh bài [trường chuẩn dưới góc nhìn hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/) và [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).
- Chỉ ra điểm sai trong ít nhất một khẳng định quá đà (ví dụ "Mô hình chuẩn đã hoàn toàn chặt chẽ về mặt toán học").

**Kiến thức cần có.** Đại số tuyến tính (ma trận, trị riêng) và một chút về phương trình đạo hàm riêng hoặc phiếm hàm năng lượng. Không cần lý thuyết trường lượng tử ở mức cao học; mục tiêu là hiểu chính xác phát biểu của bài toán mở.

**Liên hệ với khóa học.** **Mục tiêu 1**, **mục tiêu 6**. Bài toán mở cùng loại về môi trường liên tục: Navier–Stokes. Liên hệ sâu hơn: trường chuẩn dưới góc nhìn hình học. Giải Abel: [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/).

---

## 1. Lý thuyết Yang–Mills cổ điển trong một trang

Cố định một nhóm Lie compact $$G$$ (ví dụ $$SU(2)$$, $$SU(3)$$) với đại số Lie $$\mathfrak{g}$$. Một **trường chuẩn** là một liên thông $$A$$: về mặt địa phương, đó là một dạng vi phân bậc 1 nhận giá trị trong $$\mathfrak{g}$$ trên không–thời gian. **Độ cong** (cường độ trường) là

$$
F = dA + A\wedge A
$$

(với nhóm giao hoán $$G=U(1)$$, số hạng bậc hai bằng không và ta trở lại lý thuyết Maxwell $$F=dA$$). **Tác dụng Yang–Mills** cổ điển trong bốn chiều tỉ lệ với

$$
S[A] = \int \operatorname{tr}(F\wedge \star F).
$$

Các điểm tới hạn của $$S$$ thỏa mãn phương trình Yang–Mills, một dạng tổng quát phi tuyến của phương trình Maxwell. **Instanton** là các nghiệm có tác dụng hữu hạn trên những đa tạp 4 chiều thích hợp; tô pô (số Chern) đã nối giải tích với lý thuyết các lớp đặc trưng.

**Ý chính (mục tiêu 4).** Tính dư thừa chuẩn địa phương (biến đổi $$A$$ bởi $$g(x)\in G$$ mà không làm thay đổi nội dung vật lý) buộc ta phải dùng ngôn ngữ hình học của **phân thớ chính và liên thông**. Đó là lý do vật lý hạt và hình học vi phân dùng chung một bộ từ vựng.

---

## 2. Từ trường cổ điển đến lý thuyết lượng tử

**Lượng tử hóa** lý thuyết Yang–Mills nghĩa là biến lý thuyết trường cổ điển thành một lý thuyết trường lượng tử: có các hàm tương quan, có không gian Hilbert các trạng thái (theo ngôn ngữ Hamilton), hoặc có một độ đo Euclid trên không gian cấu hình trường mà giới hạn liên tục tồn tại.

**Lý thuyết nhiễu loạn** khai triển quanh trường tự do và sắp xếp các hiệu chỉnh bằng giản đồ Feynman. Với lý thuyết chuẩn không giao hoán, các trường ma Faddeev–Popov, đối xứng BRST và phép tái chuẩn hóa giúp khai triển hoạt động được ở từng bậc. Thành công thực nghiệm của Mô hình chuẩn chủ yếu nằm ở chế độ nhiễu loạn và lý thuyết trường hiệu dụng, cùng với tính toán trên lưới (không nhiễu loạn) cho tương tác mạnh.

**Lý thuyết trường lượng tử kiến thiết / tiên đề** đòi hỏi nhiều hơn: một lý thuyết trên không gian liên tục được định nghĩa chặt chẽ về mặt toán học, thỏa mãn các tiên đề (Wightman, Osterwalder–Schrader) và có tương tác không tầm thường. Những xây dựng như vậy đã có cho nhiều mô hình trong không–thời gian ít chiều; nhưng việc xây dựng đầy đủ lý thuyết Yang–Mills thuần không giao hoán trong 4 chiều với các tính chất mong đợi vẫn còn mở. Đây là nửa đầu của bài toán Clay.

---

## 3. Khe khối lượng là gì

Trong một lý thuyết lượng tử có toán tử Hamilton $$H\geq 0$$ và năng lượng chân không được chuẩn hóa bằng $$0$$, **khe khối lượng** nghĩa là tồn tại $$\Delta>0$$ sao cho mọi trạng thái kích thích (hoặc mép của phổ liên tục) đều có năng lượng ít nhất là $$\Delta$$. Phát biểu tương đương theo ngôn ngữ Euclid: các hàm tương quan liên thông của các trường địa phương giảm theo hàm mũ, với tốc độ liên quan đến $$\Delta$$.

**Ý nghĩa vật lý.** Có khe khối lượng thì độ dài tương quan hữu hạn: các bậc tự do của trường chuẩn thuần không sinh ra gluon không khối lượng giống như photon trong điện động lực học lượng tử QED. Trong lý thuyết Yang–Mills thuần, kích thích nhẹ nhất được dự đoán là một **glueball có khối lượng**. Hiện tượng giam hãm quark trong QCD đầy đủ còn phức tạp hơn; bài toán Clay về khe khối lượng cho trường chuẩn thuần là một phần toán học "sạch" trong cùng vùng khái niệm đó.

**Tình trạng (2026):** **còn mở**, là một Bài toán Thiên niên kỷ của Clay. Tính toán trên lưới và QCD vật lý cho bằng chứng mạnh rằng lý thuyết có khe, nhưng bằng chứng không phải là một định lý về sự tồn tại trên không gian liên tục kèm theo khe khối lượng như Clay yêu cầu.

---

## 4. Các kết quả toán học từng phần

| Bối cảnh | Những gì đã biết (tóm tắt) |
|--------|----------------------------|
| Yang–Mills cổ điển | Giải tích hình học sâu sắc: định lý compact của Uhlenbeck, không gian moduli của instanton, Donaldson. Đây là phương trình đạo hàm riêng và hình học **cổ điển**, không phải phát biểu lượng tử của bài toán Clay. |
| Số chiều thấp | Có kết quả kiến thiết cho nhiều mô hình chuẩn và mô hình liên quan khi $$d<4$$. |
| Yang–Mills trên lưới | Lý thuyết chuẩn trên lưới của Wilson được định nghĩa tốt khi bước lưới hữu hạn; chuyển qua giới hạn liên tục và chứng minh có khe là bước giải tích khó. |
| Nhiễu loạn trong 4 chiều | Tính tái chuẩn hóa được của Yang–Mills là thành tựu lớn của thập niên 1970, nhưng vẫn chưa phải là sự tồn tại theo hướng kiến thiết, không nhiễu loạn. |
| Tô pô và lý thuyết trường lượng tử | Định lý chỉ số, dị thường, instanton được xử lý chặt chẽ trong nhiều bối cảnh khi các toán tử đã được định nghĩa; nhưng tự chúng không xây dựng được độ đo đầy đủ của lý thuyết có tương tác. |

---

## 5. Vì sao khó (mục tiêu 1)

1. **Vô hạn bậc tự do.** Trường gán dữ liệu cho mọi điểm trong không gian.  
2. **Tính phi tuyến và các quỹ đạo chuẩn.** Một cấu hình vật lý là cả một quỹ đạo dưới các phép biến đổi chuẩn.  
3. **Phân kỳ tử ngoại.** Muốn qua giới hạn liên tục cần tái chuẩn hóa.  
4. **Vật lý không nhiễu loạn.** Khe khối lượng và hiện tượng giam hãm không suy ra được đơn giản từ giản đồ Feynman ở bậc hữu hạn.  
5. **Bốn chiều là trường hợp tới hạn.** Phép đếm số mũ và hành vi của nhóm tái chuẩn hóa khiến 4 chiều nằm đúng ở "ranh giới".

Nhiều công cụ đã phát triển xung quanh bài toán: lý thuyết chuẩn trên lưới, lý thuyết trường kiến thiết, nhóm tái chuẩn hóa, và phần lớn giải tích hình học của trường chuẩn, dù chúng mới giải được các bài toán *lân cận* chứ chưa giải trọn bài toán Clay.

---

## 6. Phát biểu chính xác, tránh thổi phồng (mục tiêu 6)

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Yang–Mills chưa giải được nên Mô hình chuẩn sai." | Sai | Mô hình chuẩn là lý thuyết vật lý được thực nghiệm ủng hộ mạnh mẽ; bài toán Clay hỏi về việc xây dựng và chứng minh toán học. |
| "Lattice QCD đã giải bài toán Clay." | Nói quá | Tính toán trên lưới là bằng chứng và khung làm việc mạnh; nhưng giải thưởng dành cho định lý về lý thuyết liên tục kèm khe khối lượng. |
| "Tự do tiệm cận nghĩa là lý thuyết đã hoàn toàn chặt chẽ." | Chưa đủ | Tự do tiệm cận là một yếu tố quan trọng, nhưng chưa phải là một xây dựng kiến thiết đầy đủ. |
| "Khe khối lượng chính là cơ chế Higgs." | Nhầm khái niệm | Cơ chế Higgs cho khối lượng của các hạt $$W/Z$$; khe khối lượng của Yang–Mills thuần đến từ động lực học của trường chuẩn khi không có vật chất (một cơ chế khác). |
| "Instanton chứng minh được khe khối lượng." | Nói quá | Instanton giúp hiểu cấu trúc chân không, nhưng tự chúng không giải được bài toán Clay. |

---

## 7. Vị trí trong Math Enthusiast

- **Chương 1:** các bài toán mở và cách nhìn nhận chúng.  
- **Chương 3:** [nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/).  
- **Chương 6:** [Trường chuẩn dưới góc nhìn hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/); [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).  
- **Chương 8:** Uhlenbeck và Atiyah–Singer.

---

## Bài tập

1. **Luyện phát biểu (không quá 120 từ).** Viết lại bài toán Clay về Yang–Mills cho một người bạn biết lý thuyết Maxwell nhưng chưa học lý thuyết trường lượng tử.  
2. **Giao hoán và không giao hoán.** Vì sao $$A\wedge A$$ bằng không với $$U(1)$$ nhưng không bằng không với $$SU(2)$$?  
3. **Tóm tắt về khe khối lượng.** Trong không quá 60 từ: liên hệ giữa sự giảm theo hàm mũ của hàm tương quan và khe trong phổ.  
4. **Mục tiêu 6.** Tìm một câu viết phổ thông về chuyện "Yang–Mills chưa được giải" và viết lại sao cho không phủ nhận vật lý thực nghiệm.  
5. **So sánh.** Viết một đoạn: bài toán khe khối lượng Yang–Mills giống và khác bài toán Navier–Stokes thế nào, xét như hai Bài toán Thiên niên kỷ.  
6. **Liên hệ.** Liệt kê ba đối tượng toán học xuất hiện cả trong hình học trường chuẩn cổ điển lẫn trong bài toán lượng tử.

---

## Tài liệu tham khảo

1. Viện Toán học Clay — mô tả chính thức bài toán Yang–Mills và khe khối lượng (Jaffe–Witten).  
2. Yang & Mills (1954).  
3. Trong khóa học: [Trường chuẩn dưới góc nhìn hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).  
