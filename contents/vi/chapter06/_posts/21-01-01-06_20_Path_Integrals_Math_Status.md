---
layout: post
title: "Tích phân đường: Ý tưởng, sức mạnh và địa vị toán học"
chapter: '06'
order: 20
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

**Tích phân đường (path integral)** của Richard Feynman viết lại biên độ lượng tử như một "tổng trên mọi lịch sử có thể": nói đại khái,

$$
\langle q_f,t_f|q_i,t_i\rangle \;\sim\; \int \mathcal{D}q\; \exp\!\Big(\frac{i}{\hbar}S[q]\Big),
$$

trong đó $$S[q]$$ là tác dụng cổ điển của đường đi từ $$(q_i,t_i)$$ đến $$(q_f,t_f)$$. Đây là một ý tưởng vật lý xuất sắc: khi $$\hbar$$ nhỏ, đường đi cổ điển chiếm ưu thế nhờ nguyên lý pha dừng; hiện tượng giao thoa giữa các đường mang nội dung lượng tử. Ý tưởng này tổ chức lý thuyết nhiễu loạn, phép tính instanton, và phần lớn cách giảng dạy lý thuyết trường lượng tử.

Về mặt toán học, đối tượng $$\mathcal{D}q$$ rất tinh tế: nói chung **không tồn tại độ đo Lebesgue trên không gian vô hạn chiều các đường đi** với những tính chất mà nhà vật lý ngầm giả định. Bài này tách riêng ba phần: **ý tưởng**, **phần đã làm chặt chẽ được**, và **phần vẫn còn là lập luận trực quan**, để bạn đọc hiểu đúng các bài trong nhánh Cầu nối. Kiến thức nền: [không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/); bài liên quan: [phân bố]({{ site.baseurl }}/contents/vi/chapter03/03_12_Distributions_Dirac/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu ý chính của tích phân đường và quan hệ của nó với tác dụng cổ điển $$S$$.
- Giải thích trực giác pha dừng khi $$\hbar\to 0$$, nối tích phân đường với cơ học cổ điển.
- Phân biệt **tích phân Feynman theo thời gian thực**, **tích phân theo thời gian ảo (Euclid)**, và **độ đo Wiener**.
- Nêu ít nhất 2 trường hợp đã chặt chẽ (công thức Trotter dẫn về phương trình Schrödinger; độ đo Wiener cho chuyển động Brown và thời gian ảo).
- Đặt tích phân đường vào bối cảnh lý thuyết trường lượng tử: phiếm hàm sinh, giản đồ Feynman, và việc dựng lý thuyết ở 4 chiều vẫn còn mở ([bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/)).
- Phản biện khẳng định phổ biến "tích phân đường đã là toán học chặt chẽ cho mọi lý thuyết trường lượng tử".

---

## 1. Từ nhận xét của Dirac đến Feynman

Dirac (thập niên 1930) nhận thấy hàm truyền trong khoảng thời gian ngắn có liên hệ với $$\exp(iS/\hbar)$$. Feynman (1948) biến nhận xét này thành một cách trình bày có hệ thống của cơ học lượng tử, tương đương (dưới các điều kiện thích hợp) với phương trình Schrödinger: chia nhỏ thời gian, lấy tích phân theo các vị trí trung gian, rồi cho bước thời gian tiến về 0.

**Cơ chế chính.** Sự tiến hóa lượng tử được ghép lại từ **biên độ của toàn bộ quỹ đạo**, mỗi quỹ đạo có trọng số pha $$e^{iS/\hbar}$$, chứ không chỉ từ phương trình vi phân cho hàm sóng. Tuy vậy, hai cách nhìn cho cùng kết quả khi cả hai đều được định nghĩa tốt.

---

## 2. Thử trước trong trường hợp hữu hạn chiều

Tích phân dao động thông thường

$$
I(\hbar)=\int_{\mathbb{R}^n} e^{iS(x)/\hbar}\,a(x)\,dx
$$

thuộc giải tích cổ điển. Nguyên lý pha dừng nói rằng khi $$\hbar\to 0$$, số hạng chính trong khai triển tiệm cận đến từ các điểm tới hạn của $$S$$, tức là các "đường cổ điển". Tích phân đường cố gắng lặp lại câu chuyện này khi thay $$x$$ bằng một đường đi $$q(\cdot)$$ và cho $$n\to\infty$$.

---

## 3. Độ đo gặp vấn đề ở đâu?

Không gian các đường đi $$C([0,T],\mathbb{R}^d)$$ là vô hạn chiều. Trên đó không có độ đo Lebesgue bất biến tịnh tiến nào hành xử giống thể tích trong không gian hữu hạn chiều. Vì vậy ký hiệu hình thức $$\mathcal{D}q$$ phải được hiểu là **giới hạn của các tích phân hữu hạn chiều**, hoặc **một độ đo kiểu Gauss gắn với một dạng toàn phương khác**, hoặc một quy trình kiến thiết khác, chứ không phải "độ đo Lebesgue trên các đường".

Với **thời gian thực**, hàm dưới dấu tích phân dao động ($$e^{iS/\hbar}$$), nên khó xử lý hơn nhiều so với hàm dương. **Phép quay Wick** $$t\to -i\tau$$ (khi biện minh được) đưa nhiều bài toán về tích phân **Euclid** với thừa số suy giảm $$e^{-S_E/\hbar}$$, gần với cơ học thống kê hơn.

---

## 4. Những trường hợp đã chặt chẽ

| Bối cảnh | Đối tượng toán học | Trạng thái |
|----------|----------------|----------------------|
| Chuyển động Brown | **Độ đo Wiener** trên các đường liên tục | Hoàn toàn chặt chẽ |
| Cơ học lượng tử với thời gian ảo | Công thức Feynman–Kac | Định lý, dưới các giả thiết về thế $$V$$ |
| Lý thuyết trường lượng tử trên mạng lưới hữu hạn | Tích phân nhiều biến thông thường | Định nghĩa tốt; bước khó là lấy giới hạn liên tục |
| Lý thuyết trường lượng tử nhiễu loạn | Chuỗi hình thức các giản đồ Feynman | Rất mạnh; nhưng không phải định nghĩa phi nhiễu loạn |
| Dựng Yang–Mills 4 chiều | Độ đo liên tục và khe khối lượng | [Bài toán Clay còn mở]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/) |

**Công thức tích Trotter** và các định lý về toán tử liên quan biện minh được một số giới hạn liên tục cho cơ học lượng tử với thế năng đủ tốt.

---

## 5. Instanton, hiệu ứng đường hầm, tô pô

Trong không–thời gian Euclid, các điểm yên ngựa không tầm thường của $$S_E$$, kể cả **instanton**, đóng góp những hiệu ứng nhỏ cỡ $$e^{-S_E/\hbar}$$. Các hiệu ứng này không thấy được ở bất kỳ bậc hữu hạn nào của lý thuyết nhiễu loạn ([instanton và dị thường]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/), [lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)).

Ở đây, tích phân đường là **ngôn ngữ để ghi chép** khai triển quanh các điểm yên ngựa; còn chính các điểm yên ngựa thì được cung cấp bởi giải tích hình học của các nghiệm cổ điển.

---

## 6. Lý thuyết trường lượng tử: điểm mạnh và khoảng trống

Trong lý thuyết trường lượng tử, tích phân đường hình thức tính các hàm tương quan bằng tích phân trên mọi cấu hình trường với trọng số $$e^{iS[\phi]/\hbar}$$. Khai triển quanh trường tự do cho ta các quy tắc Feynman.

**Điểm mạnh.** Thống nhất cách xử lý đối xứng, sinh ra kỹ thuật giản đồ, nối với lý thuyết trường thống kê qua phiên bản Euclid, gợi ý TQFT và các phép đối ngẫu.

**Khoảng trống.** Việc dựng chặt chẽ một lý thuyết liên tục có tương tác ở 4 chiều, phù hợp với Mô hình chuẩn, vẫn là một bài toán chưa giải xong, dù các dự đoán vật lý thành công rực rỡ trong phạm vi hiệu lực của chúng.

---

## 7. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Tích phân đường chặt chẽ như tích phân Riemann cho mọi hệ." | Sai | Độ đo vô hạn chiều chính là vấn đề. |
| "Tích phân đường khớp thực nghiệm QED, vậy độ đo đã được chứng minh." | Nhầm loại | Thành công thực nghiệm không phải là chứng minh sự tồn tại theo nghĩa kiến thiết. |
| "Độ đo Wiener chính là tích phân đường Feynman." | Thiếu | Độ đo Wiener gắn với thời gian ảo và quá trình khuếch tán. |
| "Tích phân đường thay thế không gian Hilbert." | Gây hiểu nhầm | Hai cách thường tương đương khi cả hai được định nghĩa; không gian Hilbert vẫn giữ vai trò trung tâm. |

---

## Bài tập

1. **Ý chính.** Giải thích tích phân đường trong không quá 60 chữ cho một người bạn chỉ biết phương trình Schrödinger.  
2. **Pha dừng.** Vì sao đường cổ điển chiếm ưu thế khi $$\hbar\to 0$$?  
3. **Euclid và thời gian thực.** Viết một đoạn giải thích vì sao phép quay Wick giúp ích cho giải tích.  
4. **Nói chính xác.** Phản biện câu: "Nhà toán học không chấp nhận tích phân đường vì họ ghét vật lý."  
5. **Cầu nối.** Viết một đoạn cẩn thận nối điểm yên ngựa của tích phân đường với tô pô của instanton.

---

## Tài liệu tham khảo

1. Feynman & Hibbs, *Quantum Mechanics and Path Integrals* (Cơ học lượng tử và tích phân đường).  
2. Simon, *Functional Integration and Quantum Physics* (Tích phân hàm và vật lý lượng tử).  
3. Trong khóa học: [Không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [Instanton]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/), [Nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/), [Bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/).  
