---
layout: post
title: "Đại số toán tử từ lý thuyết lượng tử"
chapter: '06'
order: 24
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Trong cơ học lượng tử cho một hạt hay một vài qubit, mọi thứ gói gọn đẹp đẽ trong một không gian Hilbert duy nhất $$\mathcal{H}$$: định lý Stone–von Neumann thậm chí còn bảo đảm rằng với hữu hạn bậc tự do, mọi cách biểu diễn hệ thức giao hoán chuẩn đều tương đương nhau — chỉ cần chọn một không gian Hilbert là xong. Nhưng khi ta bước sang một **mảnh tinh thể vô hạn chứa $$10^{23}$$ spin** hay một **trường lượng tử** trải khắp không–thời gian, định lý duy nhất đó sụp đổ! Có vô số không gian Hilbert *không tương đương nhau* ứng với các pha vật chất khác nhau (như pha sắt từ hướng lên so với hướng xuống, hay hai nhiệt độ khác nhau). Trước tình thế ấy, John von Neumann, Francis Murray, Israel Gelfand và Mark Naimark đề xuất một cuộc đảo ngược tư duy: **đừng bắt đầu từ không gian trạng thái — hãy bắt đầu từ đại số các đại lượng đo được (đại số toán tử)**, còn không gian Hilbert chỉ xuất hiện sau như một *biểu diễn* phụ thuộc vào trạng thái vật lý bạn đang đứng trong đó.

Đây là một **bài tổng quan** trong nhánh Cầu nối Vật lý–Toán: đủ cấu trúc để bạn đọc tiếp các tài liệu sâu hơn, nhưng không phải giáo trình giải tích hàm. Mục tiêu là nắm cơ chế chính và học cách nói chính xác, tránh thổi phồng. Nên đọc kèm bài [không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/) và bài [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## Bản đồ kiến thức nền: Lý thuyết đại số toán tử là gì và nghiên cứu những gì?

Ở đại học, bạn đã quen với tập $$M_n(\mathbb{C})$$ các ma trận vuông $$n \times n$$: ta cộng được, nhân được (không giao hoán), lấy chuyển vị liên hợp $$A \mapsto A^*$$, và đo kích thước bằng chuẩn toán tử $$\|A\|$$. **Lý thuyết đại số toán tử** (operator algebras) chính là sự mở rộng của giải tích ma trận sang vô hạn chiều — nơi ta nghiên cứu *cấu trúc đại số* và *tô pô* của những tập hợp toán tử tuyến tính bị chặn tác động lên không gian Hilbert.

Ngành này xoay quanh hai họ đối tượng lớn có "độ mịn" khác nhau:

- **C*-đại số (C-star algebra):** Được xem là "tô pô học không giao hoán". Khi giao hoán, một C*-đại số luôn có dạng $$C_0(X)$$ — tập các hàm liên tục trên một không gian tô pô $$X$$. Khi không giao hoán, nó là ngôn ngữ trừu tượng chuẩn để mô tả tập hợp các đại lượng quan sát lượng tử mà chưa cần cố định trước một không gian Hilbert cụ thể.
- **Đại số von Neumann (hay W*-đại số):** Được xem là "lý thuyết độ đo không giao hoán". Khi giao hoán, nó có dạng $$L^\infty(X, \mu)$$ — tập các hàm đo được bị chặn. Điểm khác biệt sống còn là đại số von Neumann chứa rất nhiều **phép chiếu trực giao** (tương ứng với các câu hỏi "có/không" trong phép đo lượng tử), và có một bảng phân loại kỳ diệu (kiểu I, II, III) làm lộ ra những hiện tượng vô hạn chiều chưa từng tồn tại ở ma trận hữu hạn — chẳng hạn "chiều liên tục" (kiểu II) hay đại số không có dấu vết hữu hạn nào (kiểu III, vốn là kiểu đại số xuất hiện trong mọi vùng không–thời gian của lý thuyết trường lượng tử!).

Hiểu được cặp đôi **C*-đại số (tô pô không giao hoán)** và **đại số von Neumann (độ đo không giao hoán)** cùng chiếc cầu nối **phép dựng GNS**, bạn đã nắm được bản đồ cốt lõi của toàn ngành.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao **các đại lượng quan sát được tạo thành một đại số** (có phép cộng, phép nhân, phép liên hợp), chứ không chỉ là "một danh sách ma trận".
- Phân biệt ở mức ý tưởng **C*-đại số** (đầy đủ theo chuẩn, thỏa $$\|a^*a\|=\|a\|^2$$) với **đại số von Neumann** (đóng theo tô pô toán tử yếu).
- Phát biểu ý chính của **phép dựng GNS**: từ một trạng thái dựng ra một biểu diễn trên không gian Hilbert.
- Nêu một động lực từ vật lý: hệ có vô hạn bậc tự do, quy tắc siêu chọn, hoặc tính địa phương trong lý thuyết trường lượng tử đại số.
- Tránh cách hiểu sai: "đại số toán tử chỉ là đại số tuyến tính viết cầu kỳ cho cùng các qubit hữu hạn".

**Kiến thức nền.** Bài [không gian Hilbert và phổ trong cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/); số phức và ma trận liên hợp.

---

## 1. Từ ma trận đến đại lượng quan sát trừu tượng

Trên $$\mathbb{C}^n$$, các đại lượng quan sát được là các ma trận Hermite ($$A = A^*$$). Tập các ma trận Hermite là một không gian vectơ thực, đóng với phép lấy đa thức của từng ma trận, nhưng chú ý rằng tích $$AB$$ của hai ma trận Hermite nói chung không còn Hermite nếu $$AB \neq BA$$ — nên muốn có phép nhân đầy đủ, ta làm việc trong toàn bộ đại số phức $$M_n(\mathbb{C})$$ chứa chúng. Ở dạng trừu tượng, khái niệm **\*-đại số có đơn vị** gói gọn đúng các phép toán đó: cộng, nhân, phần tử đơn vị, và phép đối hợp $$a\mapsto a^*$$ (những phần tử tự liên hợp $$a = a^*$$ chính là các đại lượng quan sát).

**Ý chính về mặt vật lý.** Những gì phòng thí nghiệm đo được và kết hợp được với nhau mới là thực thể cơ bản; không gian Hilbert chỉ là một **biểu diễn** của đại số đó, chứ không phải là đối tượng duy nhất định trước cho mọi pha vật lý.

---

## 2. C*-đại số (kiểm soát bằng chuẩn)

Một **C*-đại số** là một *-đại số Banach (tức đầy đủ theo một chuẩn $$\|\cdot\|$$) thỏa mãn đúng một đẳng thức vàng gọi là **đồng nhất thức C***:

$$
\|a^*a\| = \|a\|^2.
$$

Đẳng thức trông ngắn ngủi này lại có sức mạnh phi thường: nó khóa chặt *chuẩn giải tích* vào *cấu trúc đại số* (nếu một *-đại số có chuẩn C* thì chuẩn đó là **duy nhất**!). Nhờ nó, ta có phép tính hàm liên tục với các phần tử chuẩn tắc, công thức bán kính phổ, và một lý thuyết biểu diễn cực kỳ phong phú.

Hai ví dụ nền tảng luôn đáng nhớ:
1. **Không giao hoán:** $$B(\mathcal{H})$$ — đại số tất cả toán tử tuyến tính bị chặn trên một không gian Hilbert $$\mathcal{H}$$ (ví dụ hữu hạn chiều chính là $$M_n(\mathbb{C})$$).
2. **Giao hoán:** $$C_0(X)$$ — đại số các hàm liên tục triệt tiêu ở vô cực trên một không gian Hausdorff compact địa phương $$X$$, với chuẩn cực đại $$\|f\| = \sup_{x\in X}|f(x)|$$ và phép đối hợp là liên hợp phức $$f^*(x) = \overline{f(x)}$$. **Định lý Gelfand–Naimark** khẳng định *mọi* C*-đại số giao hoán đều có dạng này!

**Cầu nối sang hình học.** Hình học không giao hoán bắt đầu khi ta coi một C*-đại số không giao hoán như "đại số hàm trên một không gian lượng tử" (xem [bài tổng quan về NCG]({{ site.baseurl }}/contents/vi/chapter06/06_25_Noncommutative_Geometry_Map/)).

---

## 3. Đại số von Neumann (đóng theo tô pô yếu)

Một **đại số von Neumann** là một *-đại số các toán tử bị chặn trên không gian Hilbert $$\mathcal{H}$$, đóng theo tô pô toán tử yếu. Định lý giao hoán tử kép nổi tiếng của von Neumann chỉ ra rằng điều kiện tô pô này tương đương hoàn toàn với điều kiện đại số thuần túy $$M'' = M$$ (với $$M'$$ là tập mọi toán tử giao hoán với tất cả phần tử của $$M$$).

Các khối xây dựng cơ bản nhất của đại số von Neumann là các **nhân tử (factor)** — những đại số có tâm tầm thường ($$M \cap M' = \mathbb{C}\cdot I$$). Murray và von Neumann khởi đầu, rồi Alain Connes (Huy chương Fields 1982) hoàn thiện bảng phân loại kinh điển các nhân tử thành ba kiểu:
- **Kiểu I:** Bao gồm $$M_n(\mathbb{C})$$ và $$B(\mathcal{H})$$ — đây là thế giới cơ học lượng tử thông thường, nơi tồn tại các phép chiếu tối tiểu (tương ứng với trạng thái thuần cô lập).
- **Kiểu II:** Không còn phép chiếu tối tiểu nào (mọi không gian con đều có thể chia nhỏ mãi!), nhưng vẫn tồn tại một hàm vết (trace) cho phép gán "số chiều liên tục" nhận mọi giá trị thực trong $$[0,1]$$ hoặc $$[0,\infty]$$. Kiểu này xuất hiện tự nhiên khi lấy giới hạn chuỗi spin vô hạn ở nhiệt độ vô cùng, và gắn sâu sắc với lý thuyết nút (đa thức Jones ra đời từ chính chỉ số của đại số con kiểu $$\mathrm{II}_1$$!).
- **Kiểu III:** Không có cả phép chiếu tối tiểu lẫn vết hữu hạn! Nhờ lý thuyết modular **Tomita–Takesaki**, Connes phân loại sâu hơn kiểu III và phát hiện chính thời gian nhiệt động học (trạng thái KMS) sinh ra dòng tự đẳng cấu nội tại của đại số. Đây chính là kiểu đại số xuất hiện trong các vùng hữu hạn của lý thuyết trường lượng tử và gần đây còn trở lại nóng hổi trong vật lý hố đen lượng tử.

---

## 4. Trạng thái, phép dựng GNS, siêu chọn

Nếu ta không có sẵn không gian Hilbert, làm sao định nghĩa "trạng thái lượng tử"? Ta chỉ cần một **trạng thái** trên C*-đại số $$\mathcal{A}$$: một phiếm hàm tuyến tính $$\omega: \mathcal{A} \to \mathbb{C}$$ dương ($$\omega(a^*a) \ge 0$$) và chuẩn hóa ($$\omega(1) = 1$$) — bạn có thể hiểu $$\omega(a)$$ đơn giản là **giá trị kỳ vọng** đo được của đại lượng $$a$$!

**Phép dựng GNS (Gelfand–Naimark–Segal)** cho một kết quả tuyệt đẹp: từ bất kỳ trạng thái $$\omega$$ nào trên $$\mathcal{A}$$, ta có thể dựng ngược ra một bộ ba $$(\mathcal{H}_\omega, \pi_\omega, \Omega)$$ gồm một không gian Hilbert, một biểu diễn của $$\mathcal{A}$$, và một vectơ đơn vị cyclic $$\Omega$$ sao cho

$$
\omega(a) = \langle \pi_\omega(a)\Omega, \Omega \rangle.
$$

Hãy xem một ví dụ trực quan: xét một chuỗi vô hạn các spin $$1/2$$ nằm dọc trục số nguyên $$\mathbb{Z}$$. Trạng thái $$\omega_\uparrow$$ (tất cả spin đều chỉ lên) và trạng thái $$\omega_\downarrow$$ (tất cả spin đều chỉ xuống) cùng xác định trên chung một C*-đại số các phép đo cục bộ. Nhưng khi dùng phép dựng GNS, hai không gian Hilbert $$\mathcal{H}_{\omega_\uparrow}$$ và $$\mathcal{H}_{\omega_\downarrow}$$ lại **không tương đương unita** — không có thao tác hữu hạn nào lật được cùng lúc vô hạn spin từ lên sang xuống! Trong ngôn ngữ vật lý, các biểu diễn không tương đương như vậy tách thế giới thành các **khu vực siêu chọn** (superselection sector), giải thích cả hiện tượng phá vỡ đối xứng tự phát lẫn sự bảo toàn tuyệt đối của điện tích.

---

## 5. Lý thuyết trường lượng tử đại số (ý chính)

**Lưới Haag–Kastler** (Algebraic QFT) gán cho mỗi vùng mở bị chặn $$\mathcal{O}$$ trong không–thời gian Minkowski một đại số von Neumann $$\mathcal{A}(\mathcal{O})$$ gồm các đại lượng có thể đo đạc bên trong vùng $$\mathcal{O}$$, thỏa ba tiên đề vật lý cốt lõi:
1. *Đẳng điệu:* vùng lớn hơn chứa đại số lớn hơn ($$\mathcal{O}_1 \subset \mathcal{O}_2 \Rightarrow \mathcal{A}(\mathcal{O}_1) \subset \mathcal{A}(\mathcal{O}_2)$$).
2. *Tính địa phương (nhân quả Einstein):* hai đại lượng đo ở hai vùng cách nhau kiểu không gian (ánh sáng không kịp truyền tới nhau) thì phải **giao hoán** ($$[\mathcal{A}(\mathcal{O}_1), \mathcal{A}(\mathcal{O}_2)] = 0$$).
3. *Tính hiệp biến Poincaré:* đối xứng không–thời gian tác động nhất quán lên lưới đại số.

Hạt, tán xạ và trường được dựng lại từ chính cấu trúc của lưới này. Về trạng thái hiện nay: đây là một khung tiên đề toán học rất mạnh và sắc bén, nhưng việc xây dựng tường minh một lưới thỏa mọi tiên đề cho lý thuyết có tương tác ở 4 chiều vẫn là thách thức cực khó — cùng họ bài toán mở với lý thuyết trường lượng tử kiến thiết ([bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/), [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/)).

---

## 6. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Mọi lý thuyết lượng tử chỉ là ma trận." | Thiếu | Hệ vô hạn cần đến đại số và biểu diễn. |
| "von Neumann đã giải xong lý thuyết trường lượng tử." | Nói quá | Lý thuyết cấu trúc rất sâu, nhưng việc dựng các lý thuyết cụ thể vẫn còn mở. |
| "Có C*-đại số là xong hình học không giao hoán." | Sai | C*-đại số chỉ là một trụ cột; bộ ba phổ còn đi xa hơn. |

---

## Bài tập

1. **Đại số.** Vì sao tập các ma trận Hermite *không* đóng với phép nhân $$AB$$?  
2. **C*-đại số.** Điều kiện $$\|a^*a\|=\|a\|^2$$ cho ta trực giác gì?  
3. **GNS.** Viết một câu: từ trạng thái đến biểu diễn.  
4. **Nói chính xác.** Viết lại câu: "Đại số toán tử là triết học, không phải toán học dùng trong vật lý."  
5. **Cầu nối.** "Đại số các đại lượng quan sát địa phương" khác "một không gian Hilbert toàn cục cho cả vũ trụ" như thế nào?

---

## Tài liệu tham khảo

1. Bratteli & Robinson, *Operator Algebras and Quantum Statistical Mechanics* (Đại số toán tử và cơ học thống kê lượng tử).  
2. Haag, *Local Quantum Physics* (Vật lý lượng tử địa phương).  
3. Trong khóa học: [Không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [Hình học không giao hoán]({{ site.baseurl }}/contents/vi/chapter06/06_25_Noncommutative_Geometry_Map/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).  
