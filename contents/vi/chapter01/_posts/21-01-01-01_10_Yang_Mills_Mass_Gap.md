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

Hãy thử nhìn xuống bàn tay của chính mình. Phần lớn trọng lượng cơ thể bạn đến từ các hạt proton và neutron trong hạt nhân nguyên tử. Thế nhưng một sự thật gây kinh ngạc của vật lý hiện đại là: tổng khối lượng của các hạt quark bên trong một proton chỉ chiếm chưa tới **1%** khối lượng của nó! Hơn **99% khối lượng vật chất quanh ta** thực ra đến từ năng lượng liên kết cuồn cuộn của các hạt **gluon** — những hạt truyền lực hạt nhân mạnh mà ngay trên trang giấy phương trình cổ điển, chúng lại có **khối lượng bằng không**, giống hệt photon của ánh sáng!

Một nghịch lý sâu sắc hiện ra ngay lập tức: photon không có khối lượng nên lực điện từ vươn xa vô tận — ta thấy được ánh sáng từ những thiên hà cách hàng tỷ năm ánh sáng. Trong khi đó, gluon cổ điển cũng không có khối lượng, nhưng lực hạt nhân mạnh lại tắt ngấm ngay ở rìa hạt nhân nguyên tử (khoảng $$10^{-15}$$ mét), và các kích thích lượng tử nhẹ nhất của trường gluon lại mang một **khối lượng dương ngặt**, tách biệt khỏi chân không bởi một khoảng trống năng lượng gọi là **khe khối lượng (mass gap)**!

Trong số các Bài toán Thiên niên kỷ của Viện Clay, nếu [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) đến từ dòng chảy của chất lỏng, thì **Bài toán tồn tại Yang–Mills và khe khối lượng** đến thẳng từ trái tim của vật lý hạt cơ bản. Các nhà vật lý dùng lý thuyết Yang–Mills hằng ngày — đó là bộ khung của Mô hình Chuẩn (tương tác điện từ, tương tác yếu và sắc động lực học lượng tử QCD), và các siêu máy tính mô phỏng trên lưới đều thấy rõ hiện tượng giam hãm quark lẫn khe khối lượng. Nhưng Viện Clay đòi hỏi **toán học ở mức định lý**: xây dựng chặt chẽ lý thuyết Yang–Mills lượng tử trên không–thời gian liên tục 4 chiều (không dựa vào xấp xỉ nhiễu loạn), và chứng minh phổ năng lượng của nó có một khe dương phía trên chân không.

Bài này giúp bạn nắm vững phát biểu chính xác của bài toán, cảm nhận vẻ đẹp hình học của trường Yang–Mills cổ điển, hiểu "tồn tại" và "khe khối lượng" nghĩa là gì theo ngôn ngữ toán học, và phân định rõ ranh giới giữa thành công thực nghiệm của vật lý với thách thức toán học vẫn còn mở.

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

**Kết nối trong khóa học.** Bài toán mở cùng tinh thần về môi trường liên tục là [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/). Để đi sâu hơn về nền tảng hình học, xem [Trường chuẩn dưới góc nhìn hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/) và bài về người nhận Giải Abel [Karen Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/).

---

## Bản đồ kiến thức nền: Lý thuyết trường chuẩn, Hình học vi phân và Lý thuyết trường lượng tử là gì?

Cụm từ *Yang–Mills* nghe rất "vật lý cao siêu", nhưng cốt lõi toán học của nó lại nối thẳng với **đại số tuyến tính (ma trận và trị riêng)** cùng **giải tích** bạn đã học ở đại học:

- **Đối xứng chuẩn (Gauge Symmetry) và Nhóm Lie:** Hãy tưởng tượng bạn đang đo độ cao các ngọn núi; dù bạn chọn mực nước biển hay mặt đất làm mốc $$0$$ thì chênh lệch độ cao vẫn không đổi. Trong vật lý lượng tử, các hạt mang những "tọa độ nội tại" có thể xoay bằng các ma trận thuộc một **nhóm đối xứng liên tục** (gọi là **nhóm Lie**, như nhóm xoay vòng tròn $$U(1)$$ cho điện từ, hay nhóm ma trận unita $$SU(2), SU(3)$$ cho lực hạt nhân). **Đối xứng chuẩn địa phương** cho phép bạn chọn *hệ quy chiếu nội tại khác nhau tại mỗi điểm $$x$$ trong không–thời gian*! Để so sánh trạng thái hạt ở hai điểm lân cận khi hệ quy chiếu đang xoay đổi, hình học vi phân buộc phải đưa vào một trường hiệu chỉnh gọi là **liên thông (connection)** $$A$$ — và kỳ diệu thay, trường hiệu chỉnh hình học đó *chính là trường lực vật lý* (photon hay gluon)!
- **Giao hoán vs. Không giao hoán:** Với điện từ học (nhóm $$U(1)$$), các phép xoay chỉ là số phức $$e^{i\theta}$$ giao hoán với nhau ($$ab = ba$$), nên các hạt photon không tự tương tác với nhau và phương trình Maxwell là tuyến tính. Năm 1954, Chen-Ning Yang và Robert Mills mạnh dạn thay $$U(1)$$ bằng nhóm ma trận **không giao hoán** (như $$SU(2)$$, nơi $$AB \neq BA$$). Chính tính không giao hoán này làm xuất hiện số hạng phi tuyến $$A \wedge A$$: các hạt gluon tự mang "điện tích màu" và kéo dính lấy nhau — nguồn gốc của cả lực hạt nhân mạnh lẫn độ khó khổng lồ về mặt toán học!
- **Lý thuyết trường lượng tử (QFT) và "Phổ năng lượng":** Trong đại số tuyến tính, một ma trận đối xứng (Hermitian) có tập các **trị riêng**. Trong cơ học lượng tử, năng lượng của hệ được biểu diễn bởi một toán tử vô hạn chiều gọi là **Hamiltonian** $$H$$, và các trị riêng của $$H$$ chính là những mức năng lượng (hay khối lượng theo $$E=mc^2$$) mà các hạt có thể mang! Chân không có mức năng lượng thấp nhất bằng $$0$$. **Khe khối lượng $$\Delta > 0$$** theo đúng ngôn ngữ đại số tuyến tính chỉ đơn giản là: **không tồn tại bất kỳ trị riêng nào của $$H$$ nằm trong khoảng mở $$(0, \Delta)$$!**

---

## 1. Lý thuyết Yang–Mills cổ điển trong một trang

Cố định một nhóm Lie compact $$G$$ (ví dụ $$SU(2)$$, $$SU(3)$$) với đại số Lie $$\mathfrak{g}$$ (tập các ma trận "vận tốc xoay" gắn với $$G$$). Một **trường chuẩn** là một liên thông $$A$$: về mặt địa phương, đó là một dạng vi phân bậc 1 nhận giá trị ma trận trong $$\mathfrak{g}$$ trên không–thời gian. **Độ cong** (cường độ trường, tổng quát hóa điện trường $$\vec{E}$$ và từ trường $$\vec{B}$$) là

$$
F = dA + A\wedge A.
$$

**Vì sao số hạng $$A\wedge A$$ làm thay đổi tất cả?**
Với nhóm giao hoán $$G=U(1)$$, các thành phần của $$A$$ là số thực thông thường nên tích giao hoán tử $$[A_\mu, A_\nu] = A_\mu A_\nu - A_\nu A_\mu = 0$$; số hạng bậc hai $$A\wedge A$$ biến mất và ta quay về đúng phương trình Maxwell tuyến tính $$F=dA$$. Ngược lại, với nhóm ma trận $$SU(2)$$ hay $$SU(3)$$, hai ma trận không giao hoán nên $$[A_\mu, A_\nu] \neq 0$$! Số hạng $$A\wedge A$$ sống dậy, biến phương trình trường thành **phương trình đạo hàm riêng phi tuyến** cực kỳ phức tạp — tương tự như cách số hạng đối lưu $$(u\cdot\nabla)u$$ biến phương trình chất lưu thành Navier–Stokes phi tuyến!

**Tác dụng Yang–Mills** cổ điển trong bốn chiều tỉ lệ với

$$
S[A] = \int \operatorname{tr}(F\wedge \star F).
$$

Các điểm tới hạn của $$S$$ thỏa mãn phương trình Yang–Mills, một dạng tổng quát phi tuyến của phương trình Maxwell. **Instanton** là các nghiệm có tác dụng hữu hạn trên những đa tạp 4 chiều thích hợp; tôpô (số Chern) đã nối giải tích PDE với lý thuyết các lớp đặc trưng và dẫn tới những đột phá vĩ đại trong hình học 4 chiều (Donaldson, Uhlenbeck).

**Ý chính hình học:** Tính dư thừa chuẩn địa phương (biến đổi $$A$$ bởi $$g(x)\in G$$ mà không làm thay đổi nội dung vật lý) buộc ta phải dùng ngôn ngữ hình học của **phân thớ chính và liên thông**. Đó là lý do vật lý hạt và hình học vi phân chia sẻ chung một bộ từ vựng.

---

## 2. Từ trường cổ điển đến lý thuyết lượng tử

**Lượng tử hóa** lý thuyết Yang–Mills nghĩa là chuyển từ các trường cổ điển xác định sang một **lý thuyết trường lượng tử**: xây dựng một không gian Hilbert các trạng thái với toán tử Hamilton $$H$$, hoặc (theo cách nhìn tích phân đường Feynman trong không gian Euclid 4 chiều) định nghĩa một **độ đo xác suất** có dạng hình thức

$$
d\mu(A) \propto e^{-S[A]}\,\mathcal{D}A
$$

trên không gian vô hạn chiều các cấu hình trường $$A$$, sao cho mọi hàm tương quan đều tồn tại khi lấy giới hạn liên tục.

**Lý thuyết nhiễu loạn** khai triển quanh trường tự do (coi tương tác rất nhỏ) và sắp xếp các hiệu chỉnh bằng giản đồ Feynman. Với lý thuyết chuẩn không giao hoán, các trường ma Faddeev–Popov, đối xứng BRST và phép tái chuẩn hóa giúp khai triển hoạt động xuất sắc ở năng lượng rất cao (nơi lực mạnh yếu đi nhờ tính *tự do tiệm cận*). Thành công thực nghiệm lẫy lừng của Mô hình Chuẩn chủ yếu nằm ở chế độ nhiễu loạn này, kết hợp với tính toán mô phỏng trên lưới (Lattice QCD) ở năng lượng thấp.

**Lý thuyết trường lượng tử kiến thiết / tiên đề** đòi hỏi điều khó hơn gấp bội: xây dựng một đối tượng toán học hoàn chỉnh trên **không–thời gian liên tục 4 chiều** (không cần giả sử hằng số tương tác nhỏ), thỏa mãn đầy đủ hệ tiên đề chặt chẽ (Wightman hoặc Osterwalder–Schrader) và có tương tác thực sự. Người ta đã làm được điều này cho nhiều mô hình trong không–thời gian 2 chiều và 3 chiều; nhưng với lý thuyết Yang–Mills thuần không giao hoán trong **4 chiều**, bản thân việc chứng minh độ đo $$d\mu(A)$$ tồn tại chặt chẽ đã là nửa đầu của bài toán triệu đô!

---

## 3. Khe khối lượng là gì

Trong một lý thuyết lượng tử có toán tử Hamilton $$H\geq 0$$ và năng lượng chân không được chuẩn hóa bằng $$0$$, **khe khối lượng (mass gap)** nghĩa là tồn tại một hằng số dương ngặt $$\Delta>0$$ sao cho phổ của $$H$$ không chứa bất kỳ giá trị nào trong khoảng $$(0, \Delta)$$ — mọi trạng thái kích thích đều có năng lượng ít nhất là $$\Delta$$.

Phát biểu tương đương theo ngôn ngữ Euclid cực kỳ trực quan: các hàm tương quan liên thông giữa hai điểm cách nhau khoảng cách $$r = \vert x - y \vert$$ phải **suy giảm theo hàm mũ**:

$$
\langle \mathcal{O}(x)\,\mathcal{O}(y) \rangle_{\mathrm{conn}} \sim e^{-\Delta\,\vert x-y \vert} \qquad (\vert x-y \vert \to \infty).
$$

**Ý nghĩa vật lý:** Hãy so sánh hai tốc độ suy giảm:
- Trong điện từ học (không có khe khối lượng, $$\Delta = 0$$), tương quan giảm chậm theo quy luật lũy thừa $$1/r$$ — đó là lý do lực Coulomb và ánh sáng truyền đi tầm xa vô tận.
- Khi có khe khối lượng $$\Delta > 0$$, thừa số $$e^{-\Delta r}$$ dập tắt tương tác cực nhanh ở khoảng cách lớn hơn $$1/\Delta$$! Trong lý thuyết Yang–Mills thuần, điều đó có nghĩa các gluon không xuất hiện tự do như hạt không khối lượng, mà tự kết thành những trạng thái liên kết có khối lượng gọi là **glueball** (với khối lượng nhẹ nhất $$\ge \Delta$$). Hiện tượng giam hãm quark trong QCD đầy đủ còn phức tạp hơn; bài toán Clay về khe khối lượng cho trường chuẩn thuần là phần toán học "tinh khiết" nằm ngay lõi của hiện tượng này.

**Tình trạng (2026):** **còn mở**, là một trong sáu Bài toán Thiên niên kỷ chưa được giải của Viện Clay. Tính toán trên lưới và thực nghiệm QCD cho bằng chứng áp đảo rằng lý thuyết có khe khối lượng, nhưng bằng chứng số không thể thay thế một định lý tồn tại trên không gian liên tục.

---

## 4. Các kết quả toán học từng phần

| Bối cảnh | Những gì đã biết (tóm tắt) |
|--------|----------------------------|
| Yang–Mills cổ điển | Giải tích hình học sâu sắc: định lý compact của Uhlenbeck, không gian moduli của instanton, Donaldson. Đây là phương trình đạo hàm riêng và hình học **cổ điển**, không phải phát biểu lượng tử của bài toán Clay. |
| Số chiều thấp | Có kết quả kiến thiết cho nhiều mô hình chuẩn và mô hình liên quan khi $$d<4$$ (ví dụ Yang–Mills 2 chiều giải được gần như tường minh). |
| Yang–Mills trên lưới | Lý thuyết chuẩn trên lưới của Wilson được định nghĩa hoàn toàn chặt chẽ khi bước lưới $$a > 0$$ hữu hạn (và thậm chí chứng minh được có khe khối lượng khi tương tác rất mạnh); bước cực khó là cho $$a \to 0$$ để lấy giới hạn liên tục mà vẫn giữ nguyên được khe khối lượng! |
| Nhiễu loạn trong 4 chiều | Tính tái chuẩn hóa được của Yang–Mills (’t Hooft, Veltman) và tự do tiệm cận (Gross, Politzer, Wilczek) là thành tựu Nobel lớn, nhưng chỉ là chuỗi hình thức, chưa phải sự tồn tại kiến thiết không nhiễu loạn. |
| Tôpô và lý thuyết trường lượng tử | Định lý chỉ số, dị thường, instanton được xử lý chặt chẽ trong nhiều bối cảnh khi các toán tử đã được định nghĩa; nhưng tự chúng không xây dựng được độ đo đầy đủ của lý thuyết có tương tác. |

---

## 5. Vì sao khó

1. **Vô hạn bậc tự do.** Khác với cơ học lượng tử một hạt (tọa độ $$x \in \mathbb{R}^3$$), một trường gán một ma trận cho *mọi điểm* trong không gian — tức vô hạn chiều.  
2. **Tính phi tuyến và các quỹ đạo chuẩn.** Một cấu hình vật lý không phải một hàm $$A$$ riêng lẻ mà là cả một lớp tương đương dưới vô hạn phép biến đổi chuẩn địa phương.  
3. **Phân kỳ tử ngoại (UV divergence).** Khi cho bước lưới $$a \to 0$$, các dao động lượng tử ở bước sóng cực ngắn làm nhiều đại lượng phân kỳ ra vô cùng, đòi hỏi kỹ thuật tái chuẩn hóa nhiều thang đo cực kỳ tinh vi.  
4. **Vật lý không nhiễu loạn.** Khe khối lượng $$\Delta$$ tỉ lệ với $$e^{-c/g^2}$$ (với $$g$$ là hằng số ghép) — hàm này có mọi đạo hàm tại $$g=0$$ đều bằng 0! Điều đó giải thích vì sao **chuỗi Taylor nhiễu loạn (giản đồ Feynman) hoàn toàn mù trước khe khối lượng**, dù bạn có tính đến bậc một triệu đi nữa!  
5. **Bốn chiều là trường hợp tới hạn.** Phép đếm số mũ và hành vi của nhóm tái chuẩn hóa đặt không–thời gian 4 chiều nằm đúng trên "lưỡi dao" ranh giới — khó hơn hẳn 2 chiều và 3 chiều.

Nhiều công cụ sâu sắc đã phát triển xung quanh bài toán: lý thuyết chuẩn trên lưới, lý thuyết trường kiến thiết, nhóm tái chuẩn hóa, và giải tích hình học của trường chuẩn, dù chúng mới chinh phục được các bài toán *lân cận* chứ chưa giải trọn bài toán Clay.

---

## 6. Phát biểu chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Yang–Mills chưa giải được nên Mô hình chuẩn sai." | Sai | Mô hình chuẩn là lý thuyết vật lý được thực nghiệm ủng hộ mạnh mẽ; bài toán Clay hỏi về việc xây dựng và chứng minh toán học. |
| "Lattice QCD đã giải bài toán Clay." | Nói quá | Tính toán trên lưới là bằng chứng và khung làm việc mạnh; nhưng giải thưởng dành cho định lý về lý thuyết liên tục kèm khe khối lượng. |
| "Tự do tiệm cận nghĩa là lý thuyết đã hoàn toàn chặt chẽ." | Chưa đủ | Tự do tiệm cận là một yếu tố quan trọng ở năng lượng cao, nhưng chưa phải là một xây dựng kiến thiết đầy đủ ở mọi thang đo. |
| "Khe khối lượng chính là cơ chế Higgs." | Nhầm khái niệm | Cơ chế Higgs cho khối lượng của các hạt $$W/Z$$ và quark; khe khối lượng của Yang–Mills thuần đến từ động lực học phi tuyến của chính trường chuẩn khi không có vật chất (một cơ chế hoàn toàn khác). |
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
4. **Phản biện thông tin.** Tìm một câu viết phổ thông về chuyện "Yang–Mills chưa được giải" và viết lại sao cho không phủ nhận vật lý thực nghiệm.  
5. **So sánh.** Viết một đoạn: bài toán khe khối lượng Yang–Mills giống và khác bài toán Navier–Stokes thế nào, xét như hai Bài toán Thiên niên kỷ.  
6. **Liên hệ.** Liệt kê ba đối tượng toán học xuất hiện cả trong hình học trường chuẩn cổ điển lẫn trong bài toán lượng tử.

---

## Tài liệu tham khảo

1. Viện Toán học Clay — mô tả chính thức bài toán Yang–Mills và khe khối lượng (Jaffe–Witten).  
2. Yang & Mills (1954).  
3. Trong khóa học: [Trường chuẩn dưới góc nhìn hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Uhlenbeck]({{ site.baseurl }}/contents/vi/chapter08/08_04_Uhlenbeck_Gauge/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).  
