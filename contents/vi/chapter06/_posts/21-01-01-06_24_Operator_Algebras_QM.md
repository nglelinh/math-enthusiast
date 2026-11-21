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

Cơ học lượng tử hữu hạn chiều có thể diễn đạt hoàn toàn bằng ma trận. Nhưng với các hệ vô hạn, như trường lượng tử, giới hạn nhiệt động học, hay chuỗi spin vô hạn, ta phải đổi ngôn ngữ: dùng **đại số toán tử**, thay vì một không gian Hilbert cố định chứa "mọi bậc tự do cùng lúc". Đại số von Neumann, C*-đại số và lý thuyết trường lượng tử đại số ra đời từ chính nhu cầu đó.

Đây là một **bài tổng quan** trong nhánh Cầu nối Vật lý–Toán: đủ cấu trúc để bạn đọc tiếp, nhưng không phải là giáo trình giải tích hàm. Mục tiêu là nắm cơ chế chính và học cách nói chính xác, tránh thổi phồng. Nên đọc kèm bài [không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/) và bài [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

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

Trên $$\mathbb{C}^n$$, các đại lượng quan sát được là các ma trận Hermite. Chúng tạo thành một không gian vectơ thực, đóng với phép lấy đa thức (của từng ma trận), còn tích $$AB$$ nói chung không giao hoán. Ở dạng trừu tượng, khái niệm *-đại số có đơn vị gói gọn các phép toán này: cộng, nhân, phần tử đơn vị, và phép đối hợp $$a\mapsto a^*$$.

**Ý chính về mặt vật lý.** Những gì đo được và kết hợp được với nhau mới là cơ bản; không gian Hilbert có thể chỉ là một **biểu diễn** của đại số đó, chứ không phải là đối tượng duy nhất.

---

## 2. C*-đại số (kiểm soát bằng chuẩn)

Một **C*-đại số** là một *-đại số Banach thỏa $$\|a^*a\|=\|a\|^2$$. Điều kiện này cho ta phép tính hàm liên tục với các phần tử chuẩn tắc, công thức bán kính phổ, và một lý thuyết biểu diễn phong phú. Ví dụ: $$B(\mathcal{H})$$, và $$C(X)$$ trong trường hợp giao hoán (đối ngẫu Gelfand: C*-đại số giao hoán ↔ không gian Hausdorff compact địa phương).

**Cầu nối sang hình học.** Hình học không giao hoán bắt đầu khi ta coi một C*-đại số không giao hoán như "đại số hàm trên một không gian lượng tử" (xem [bài tổng quan về NCG]({{ site.baseurl }}/contents/vi/chapter06/06_25_Noncommutative_Geometry_Map/)).

---

## 3. Đại số von Neumann (đóng theo tô pô yếu)

Một **đại số von Neumann** là một *-đại số các toán tử bị chặn trên không gian Hilbert, đóng theo tô pô toán tử yếu (tương đương với điều kiện $$M''=M$$). Các nhân tử (factor, tức đại số có tâm chỉ gồm các vô hướng) được phân loại thành kiểu I, II, III. Phân loại này do Murray và von Neumann khởi đầu, sau đó Connes phát triển tiếp. Nó gắn với thống kê lượng tử và lý thuyết modular (Tomita–Takesaki), và là nền tảng cho lý thuyết trường lượng tử đại số cũng như cơ học thống kê của hệ vô hạn.

**Kiểu I** bao gồm $$B(\mathcal{H})$$ (cơ học lượng tử thông thường). **Kiểu II và III** xuất hiện tự nhiên khi lấy tích tensor vô hạn và trong các đại số địa phương của trường lượng tử.

---

## 4. Trạng thái, phép dựng GNS, siêu chọn

Một **trạng thái** trên C*-đại số là một phiếm hàm tuyến tính dương, chuẩn hóa $$\omega$$. **Phép dựng GNS** xây dựng một không gian Hilbert $$\mathcal{H}_\omega$$, một biểu diễn $$\pi_\omega$$, và một vectơ cyclic sao cho $$\omega(a)=\langle\pi_\omega(a)\Omega,\Omega\rangle$$.

Các trạng thái khác nhau có thể cho các biểu diễn không tương đương. Trong ngôn ngữ vật lý, đó là các **khu vực siêu chọn** (superselection sector).

---

## 5. Lý thuyết trường lượng tử đại số (ý chính)

Lưới Haag–Kastler gán cho mỗi vùng không–thời gian một đại số các đại lượng quan sát địa phương, thỏa các tính chất: bao hàm (vùng lớn hơn thì đại số lớn hơn), tính địa phương (các đại lượng ở hai vùng cách nhau kiểu không gian thì giao hoán), và tính hiệp biến. Hạt và trường được dựng lại từ lưới này. Về trạng thái: đây là một khung toán học mạnh, nhưng việc dựng một lý thuyết có tương tác ở 4 chiều với đầy đủ nội dung vật lý vẫn rất khó, cùng loại vấn đề mở với lý thuyết trường lượng tử kiến thiết ([bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/), [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/)).

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
