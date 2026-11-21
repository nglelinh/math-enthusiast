---
layout: post
title: "Giải tích → Vật lý & Kỹ thuật"
chapter: '03'
order: 2
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
---

Một cây cầu đứng vững không phải vì ai đó "áp công thức". Nó đứng vững vì **tốc độ biến thiên cục bộ** của ứng suất và chuyển vị phải thỏa mãn các định luật cân bằng. Sau đó các phương trình này được tích phân, bằng giải tích hoặc bằng phương pháp số, để ra một thiết kế chịu được tải trọng, gió và hiện tượng mỏi. Theo nghĩa đó, giải tích là một phần hạ tầng.

**Lộ trình:** tốc độ và tích lũy → định lý cơ bản → định luật Newton dưới dạng phương trình vi phân thường → thêm biến không gian (phương trình đạo hàm riêng) → tư duy biến phân → phương pháp phần tử hữu hạn → các ngành kỹ thuật → những nhầm lẫn thường gặp.

Đây không phải bài học đạo hàm cho người mới bắt đầu. Bài này giải thích **vì sao giải tích trở thành ngôn ngữ chính của vật lý cổ điển và phần lớn ngành kỹ thuật**, và những ý tưởng cụ thể nào giúp việc mô phỏng, điều khiển và thiết kế trở nên khả thi.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích đạo hàm và tích phân là hai phép toán ngược nhau, được nối với nhau bởi định lý cơ bản của giải tích.
- Viết định luật hai Newton dưới dạng phương trình vi phân, và hiểu lực, khối lượng, gia tốc trong cách viết đó.
- Phân biệt phương trình vi phân thường (ODE) và phương trình đạo hàm riêng (PDE); nêu các ví dụ chuẩn (phương trình nhiệt, phương trình sóng, phương trình Laplace).
- Mô tả ngắn gọn cách **phương pháp phần tử hữu hạn (FEM)** biến một định luật cân bằng liên tục thành một bài toán đại số tuyến tính cỡ lớn.
- Kể tên ba ngành kỹ thuật dùng giải tích thường xuyên và nói rõ trong mỗi ngành, *đại lượng nào* được lấy đạo hàm hay tích phân.
- Tránh hai nhầm lẫn: "giải tích chỉ là công thức ở phổ thông" và "phần mềm đã thay thế toán học".

**Kiến thức nền.** Trực giác giải tích ở phổ thông (độ dốc, diện tích). Biết về hàm nhiều biến sẽ có ích cho phần PDE.

**Liên kết.** [Phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/), [Navier–Stokes (Ch.1)]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), và bài Fourier trong chương này.

---

## 1. Hai ý tưởng, một bộ máy

**Đạo hàm** trả lời câu hỏi: tại *thời điểm này*, một đại lượng đang thay đổi nhanh đến mức nào? Vận tốc là đạo hàm của vị trí; cường độ dòng điện là tốc độ thay đổi của điện tích; chi phí biên là đạo hàm của tổng chi phí.

**Tích phân** trả lời câu hỏi: trên cả một khoảng, các thay đổi cộng dồn lại thành bao nhiêu? Quãng đường là tích phân của tốc độ; công là tích phân của lực dọc theo đường đi; tổng nhiệt lượng là tích phân của mật độ nhiệt trên vật thể.

**Định lý cơ bản của giải tích** nối hai ý tưởng này: với các giả thiết phù hợp, lấy đạo hàm và lấy tích phân là hai phép toán ngược nhau. Vật lý được xây dựng dựa trên mối nối đó:

$$
\int_a^b f(x)\,dx = F(b)-F(a)\quad\text{khi }F'=f.
$$

Tóm lại: **giải tích là ngôn ngữ toán học của sự thay đổi liên tục.**

---

## 2. Từ hình học đến động lực học

Về lịch sử, giải tích ra đời từ các bài toán hình học (tiếp tuyến, diện tích) rồi trở thành công cụ của **động lực học**. Newton và Leibniz không chỉ nghĩ ra vài mẹo tính toán; họ tạo ra một ngôn ngữ để mô tả sự thay đổi liên tục.

**Định luật hai Newton** trong một chiều,

$$
m \frac{d^2 x}{dt^2} = F\bigl(x,\tfrac{dx}{dt},t\bigr),
$$

đã là một phương trình vi phân: ẩn số là một *hàm số* $$x(t)$$. Toàn bộ cơ học cổ điển được viết bằng những phương trình như vậy.

**Tóm tắt trong một câu.**  
*Các định luật vật lý thường cho biết tốc độ thay đổi của trạng thái phụ thuộc vào chính trạng thái đó; giải phương trình vi phân cho phép dự đoán tương lai từ điều kiện ban đầu.*

---

## 3. ODE và PDE: khi có thêm biến không gian

**ODE** chỉ có đạo hàm theo một biến độc lập (thường là thời gian). Hệ khối lượng – lò xo – giảm chấn được mô tả bởi một ODE.

**PDE** có nhiều biến độc lập, thường là không gian và thời gian. Phương trình nhiệt

$$
\partial_t u = \kappa \Delta u
$$

nói rằng nhiệt độ thay đổi tỉ lệ với toán tử Laplace của nó, tức là nhiệt có xu hướng san đều ra xung quanh. Phương trình sóng $$\partial_{tt}u=c^2\Delta u$$ truyền nhiễu động đi với tốc độ hữu hạn $$c$$. Phương trình Laplace $$\Delta u=0$$ mô tả trạng thái cân bằng.

**Vì sao ngành công nghệ quan tâm.** ODE là mô hình chính cho mạch điện với các phần tử tập trung, cơ học vật rắn và nhiều vòng điều khiển. PDE là mô hình chính cho các trường liên tục: nhiệt, ứng suất, điện từ (phương trình Maxwell), chất lỏng (Navier–Stokes). "Mô phỏng" trong công nghiệp thường gồm ba bước: rời rạc hóa PDE, giải một hệ phương trình đại số lớn, rồi hiển thị kết quả. Tất cả vẫn là giải tích kết hợp với giải tích số.

---

## 4. Định luật bảo toàn, thông lượng và mô hình môi trường liên tục

Nhiều mô hình vật lý cho môi trường liên tục được xây dựng theo cùng một khuôn:

1. Chọn một đại lượng (khối lượng, năng lượng, động lượng, điện tích).  
2. Viết **định luật cân bằng**: tốc độ thay đổi của đại lượng trong một miền bằng thông lượng đi qua biên cộng với nguồn bên trong.  
3. Chuyển dạng tích phân thành PDE nhờ **định lý phân kỳ** (định lý Green, Stokes, Gauss cùng một họ; xem [Vật lý toán / Stokes→Maxwell]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/)).  
4. Đóng hệ phương trình bằng một **định luật cấu thành** (định luật Fourier: thông lượng nhiệt $$\propto -\nabla u$$; định luật Hooke: quan hệ ứng suất – biến dạng; định luật Ohm; …).

Với nhiệt: định luật Fourier cộng với cân bằng năng lượng cho ta phương trình nhiệt. Toán học ở đây không phải để trang trí: định lý phân kỳ chính là lý do việc "cân đối sổ sách" dạng tích phân biến thành một PDE.

**Tóm tắt.** *Định luật bảo toàn cộng với định luật cấu thành cho ra PDE; hình dạng miền và điều kiện biên chọn ra nghiệm có ý nghĩa vật lý.*

---

## 5. Gradient, divergence và curl (công cụ của giải tích vectơ)

Các mô hình môi trường liên tục được viết bằng ngôn ngữ **trường**. **Trường vô hướng** gán một số cho mỗi điểm (nhiệt độ, độ cao). **Trường vectơ** gán một vectơ cho mỗi điểm (gió, vận tốc). Có ba toán tử xây dựng từ ký hiệu nabla $$\nabla$$ xuất hiện ở khắp nơi trong vật lý và kỹ thuật.

### Trường vô hướng và trường vectơ

| Đối tượng | Ý nghĩa | Ví dụ |
|-----------|---------|--------|
| Vô hướng | Chỉ có độ lớn | Nhiệt độ $$30^\circ\mathrm{C}$$ |
| Vectơ | Có độ lớn và hướng | Gió 10 đơn vị về hướng đông |
| Trường vô hướng | Một số tại mỗi điểm | Bản đồ nhiệt độ $$T(x,y)$$ |
| Trường vectơ | Một vectơ tại mỗi điểm | Bản đồ gió $$\mathbf{v}(x,y)$$ |

![Trường vector]({{ site.baseurl }}/img/chapter_img/veccalc_vector_field_example_bs.jpg)

*Hình. Trường vectơ $$\mathbf{v}(x,y)=(2x,y)$$ (nguồn: Brain Station Advanced).*

### Gradient: hướng dốc lên nhanh nhất

$$
\nabla f = \Bigl(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\ldots\Bigr).
$$

**Trực giác.** $$\nabla f$$ chỉ theo hướng mà $$f$$ **tăng nhanh nhất** (hướng đẩy quả bóng lên dốc). Quả bóng tự lăn theo hướng $$-\nabla f$$ (xuống dốc; đây cũng là ý tưởng của thuật toán gradient descent).  
**Ví dụ.** Với $$f=x^2+y^2$$, tại điểm $$(1,2)$$ ta có $$\nabla f=(2,4)$$.

![Gradient lên dốc]({{ site.baseurl }}/img/chapter_img/veccalc_gradient_uphill_bs.jpg)

*Hình. Gradient của $$f=x^2+y^2$$ (cùng nguồn).*

### Divergence: nguồn, điểm hút và dòng không nén

$$
\nabla\cdot\mathbf{v} = \frac{\partial v_1}{\partial x}+\frac{\partial v_2}{\partial y}+\frac{\partial v_3}{\partial z}
$$

là một **số vô hướng**. Hãy hình dung một ô vuông nhỏ đặt trong dòng chảy:

| Dấu của $$\nabla\cdot\mathbf{v}$$ | Ý nghĩa |
|------------------------------|---------|
| $$>0$$ | Chảy ra nhiều hơn chảy vào → mật độ giảm (nguồn) |
| $$<0$$ | Chảy vào nhiều hơn chảy ra → mật độ tăng (điểm hút) |
| $$=0$$ | Vào bằng ra (dòng quay, hoặc dòng đều) |

**Ví dụ.** $$\mathbf{v}=(x,y)$$ có divergence $$=2$$; $$\mathbf{v}=(-x,-y)$$ có divergence $$=-2$$; trường quay $$\mathbf{v}=(-y,x)$$ hoặc trường hằng có divergence $$=0$$.

![Nguồn]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_source_bs.jpg)

*Hình. Trường hướng ra ngoài: divergence dương (cùng nguồn video).*

![Sink]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_sink_bs.jpg)

*Hình. Trường hướng vào trong: divergence âm (cùng nguồn).*

![Dòng đều]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_uniform_bs.jpg)

*Hình. Dòng đều: $$\nabla\cdot\mathbf{v}=0$$ (cùng nguồn).*

Trong điện từ học, điện tích dương đóng vai trò **nguồn** của điện trường $$\mathbf{E}$$. Cùng với định lý phân kỳ, đây là bước biến định luật cân bằng dạng tích phân thành PDE (§4).

### Curl: độ xoáy cục bộ (thử bằng bánh xe cánh quạt)

Curl là **tích có hướng** $$\nabla\times\mathbf{v}$$, kết quả là một vectơ. Đặt một bánh xe cánh quạt nhỏ vào dòng chảy: nếu dòng làm bánh xe quay thì curl khác 0; nếu dòng chỉ đẩy bánh xe trôi đi mà không quay thì curl bằng 0.

![Curl]({{ site.baseurl }}/img/chapter_img/veccalc_curl_paddle_bs.jpg)

*Hình. Trường quay và trực giác bánh xe cánh quạt (cùng nguồn).*

### Bảng tóm tắt

| Toán tử | Kết quả | Ý nghĩa vật lý |
|---------|--------|------------------|
| $$\nabla f$$ | vectơ | Hướng tăng nhanh nhất của trường vô hướng (lực sinh từ thế năng; định luật Fourier dùng $$-\nabla T$$) |
| $$\nabla\cdot\mathbf{v}$$ | vô hướng | Cường độ nguồn hoặc điểm hút (phương trình liên tục, định luật Gauss) |
| $$\nabla\times\mathbf{v}$$ | vectơ | Độ xoáy cục bộ (xoáy trong chất lỏng; cấu trúc của phương trình Maxwell) |

---

## 6. Nguyên lý biến phân

Nhiều bài toán cân bằng có dạng **biến phân**: cấu hình vật lý là cấu hình làm cực tiểu (hoặc làm dừng) một năng lượng hay một tác dụng (action). Theo nguyên lý Dirichlet, trong số các hàm có giá trị biên cho trước, hàm làm cực tiểu

$$
E[u]=\frac12\int_\Omega\lvert\nabla u\rvert^2\,dx
$$

là nghiệm của phương trình Laplace (với giả thiết phù hợp). Đó là hàm "phẳng nhất" khớp với giá trị biên. Đàn hồi tuyến tính, mặt cực tiểu và nhiều phương pháp phần tử hữu hạn đều dựa trên ý tưởng này: xấp xỉ năng lượng trên một không gian hữu hạn chiều rồi tìm cực tiểu. Chuỗi bước là: phép tính biến phân → ma trận thưa → bộ giải.

**Tóm tắt.** *Trạng thái cân bằng là điểm dừng của năng lượng; FEM xấp xỉ không gian hàm rồi tìm cực tiểu (hoặc giải dạng yếu tương đương).*

---

## 7. Phần tử hữu hạn: giải tích ở quy mô công nghiệp

Quy trình cơ bản:

1. Chia miền thành các phần tử (tam giác, tứ diện, …).  
2. Tìm nghiệm trong không gian các hàm đa thức từng mảnh (liên tục hoặc gián đoạn, tùy họ phương pháp).  
3. Yêu cầu nghiệm thỏa mãn **dạng yếu** (dạng tích phân hay dạng biến phân) của PDE.  
4. Lắp ráp hệ $$KU=F$$ (hoặc hệ phi tuyến, hệ phụ thuộc thời gian) rồi giải.

**Dạng yếu trong một câu.** Nhân PDE với một hàm thử, lấy tích phân từng phần để chuyển bớt đạo hàm sang hàm thử. Bước này làm cho xấp xỉ tuyến tính từng mảnh trở nên hợp lệ, vì ta chỉ đòi hỏi phương trình đúng theo nghĩa tích phân, không cần đúng tại từng điểm.

**Tóm tắt.** *FEM không bỏ đi toán học liên tục. Nó chiếu bài toán giải tích vô hạn chiều xuống một bài toán đại số tuyến tính nhiều chiều mà máy tính giải được.*

Các phương pháp cùng họ: sai phân hữu hạn (lưới đều, dễ hình dung), thể tích hữu hạn (bảo toàn ở mức rời rạc, phổ biến trong CFD), phương pháp phổ (chuỗi Fourier, hàm riêng).

---

## 8. Các ngành kỹ thuật dùng giải tích

| Ngành | Giải tích dùng để làm gì |
|----------|------------------|
| Cơ khí | Ứng suất, dao động, đàn hồi, tiếp xúc |
| Điện | ODE cho mạch điện; PDE Maxwell, tĩnh điện |
| Xây dựng | Dầm, đường truyền tải trọng, FEM cho công trình |
| Hàng không | Động lực học bay; CFD (liên hệ [NS]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/)) |
| Nhiệt – hóa | Truyền nhiệt và truyền khối; phản ứng – khuếch tán |
| Điều khiển | Tuyến tính hóa; tính ổn định; biến đổi Laplace |

**Điều khiển:** tuyến tính hóa $$\dot{x}=f(x,u)$$ quanh một điểm làm việc ta được $$\dot{\xi}=A\xi+B\mu$$. Các giá trị riêng của $$A$$ và tính điều khiển được quyết định liệu một bộ điều khiển phản hồi có làm hệ ổn định được hay không. Đó là đại số tuyến tính cộng với ODE, và vẫn là giải tích.

---

## 9. Mô hình liên tục và "bản sao số" (digital twin)

Kỹ thuật hiện đại kết hợp cảm biến, mô hình và tối ưu hóa thành một vòng lặp: mô hình ODE/PDE → ước lượng trạng thái từ số liệu đo → tối ưu đầu vào hoặc lên kế hoạch bảo trì dự đoán. **Bản sao số** của một tua-bin hay một cây cầu thường là một mô hình giải tích (hoặc một mô hình thay thế gần đúng) được hiệu chỉnh bằng dữ liệu. Nó không phải một thứ phép màu tách rời khỏi PDE.

Giới hạn: dòng rối, tiếp xúc, vết nứt, dòng nhiều pha và các hiện tượng nhiều thang đo gây khó cho cả phân tích lý thuyết lẫn tính toán số. **Tính đặt chỉnh** (tồn tại, duy nhất, phụ thuộc liên tục vào dữ liệu) là một tính chất toán học có hệ quả kỹ thuật thật: với một bài toán không đặt chỉnh, chia lưới mịn hơn không giải quyết được vấn đề.

---

## 10. Vì sao vẫn cần hiểu, khi phần mềm "tự giải"

1. Sai số do **mô hình** thường lớn hơn sai số do rời rạc hóa.  
2. **Điều kiện biên** thể hiện lựa chọn vật lý của bạn; phần mềm không chọn thay bạn.  
3. **Đưa về dạng không thứ nguyên** giúp lộ ra các số hạng quan trọng (số Reynolds, số Fourier, …).  
4. Tính ổn định và tính "cứng" (stiff) khi tích phân theo thời gian là các khái niệm giải tích (chọn bước thời gian, phương pháp ẩn hay hiện).  
5. Muốn kiểm chứng và thẩm định kết quả, bạn phải biết bài toán liên tục *đáng lẽ* cho kết quả thế nào trước khi tin vào màu sắc trên màn hình.

Chuỗi tổng quát: **cân bằng vật lý → phương trình vi phân → phân tích lý thuyết và tính toán số → quyết định thiết kế.**

---

### Tóm tắt giải tích vectơ (từ phần tìm hiểu video)

Video trực quan chính: [Brain Station — Gradient, Divergence and Curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) (khoảng 15 phút).

- **Gradient:** $$\nabla f$$ là vectơ gồm các đạo hàm riêng; nó chỉ hướng **lên dốc** (tăng nhanh nhất). Muốn xuống dốc thì dùng $$-\nabla f$$.
- **Divergence:** $$\nabla\cdot\mathbf{v}$$ là một *số vô hướng*. Dương nghĩa là có nguồn, âm nghĩa là có điểm hút, bằng không nghĩa là thể tích được bảo toàn (chất lỏng vẫn có thể chuyển động).
- **Curl:** $$\nabla\times\mathbf{v}$$ đo độ xoáy cục bộ (thử bằng một bánh xe cánh quạt nhỏ).
- Xem thêm [Essence of calculus — 3Blue1Brown](https://www.youtube.com/watch?v=WUvTyaaNkzM) để nắm định lý cơ bản trước khi học các toán tử vectơ.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Giải tích chỉ để đi thi." | Giải tích là ngôn ngữ mô tả sự thay đổi liên tục trong vật lý và kỹ thuật. |
| "Phần mềm hội tụ thì mô hình đúng." | Hội tụ là chuyện tính toán số; sai mô hình hay sai điều kiện biên vẫn còn nguyên. |
| "ODE và PDE khó như nhau." | PDE là bài toán vô hạn chiều theo không gian; cả lý thuyết lẫn phương pháp số đều khác hẳn. |
| "FEM thay thế giải tích." | FEM *chính là* phép tính biến phân được rời rạc hóa, cộng với đại số tuyến tính. |
| "Lưới càng mịn càng giải quyết được mọi thứ." | Lưới mịn chỉ giảm sai số rời rạc; nó không sửa được một mô hình vật lý sai. |
| "Gradient chỉ hướng xuống dốc." | $$\nabla f$$ chỉ hướng **lên dốc**; $$-\nabla f$$ mới là hướng xuống dốc. |
| "Divergence bằng 0 nghĩa là chất lỏng đứng yên." | Divergence bằng 0 nghĩa là không có nguồn hay điểm hút ròng; chất lỏng vẫn có thể chảy (quay, hoặc chảy đều). |

---

## Bài tập

1. Với $$s(t)=\frac12 gt^2$$, tính vận tốc và gia tốc, rồi giải thích ý nghĩa.  
2. Viết ba câu giải thích vì sao "tốc độ thay đổi tức thời" và "sự tích lũy" phải gắn liền với nhau.  
3. Phân loại ODE hay PDE: mạch RC; sự truyền nhiệt trên một thanh kim loại; quỹ đạo của một hành tinh.  
4. Viết một câu nối định luật Fourier với phương trình nhiệt.  
5. **Giải tích vectơ.** Với $$f=x^2+y^2$$, tính $$\nabla f$$ tại $$(1,2)$$. Với $$\mathbf{v}=(x,y)$$ và $$\mathbf{w}=(-y,x)$$, tính divergence và giải thích ý nghĩa của dấu.  
6. Vì sao dạng yếu cho phép dùng xấp xỉ tuyến tính từng mảnh?  
7. Chọn một thiết bị bạn hay dùng; nêu một đại lượng được lấy đạo hàm hoặc tích phân trong mô hình thiết kế của nó.  
8. Nâng cao: viết dạng yếu của $$-u''=f$$ trên $$(0,1)$$ với $$u(0)=u(1)=0$$.

---

## Video phổ thông

- **Nguồn:** [Best Explanation of Gradient, Divergence and Curl — Brain Station Advanced](https://www.youtube.com/watch?v=m_Psx7CdvDk) (khoảng 15 phút; 2026-08-03).  
  Trình tự: trường vô hướng và trường vectơ → gradient chỉ hướng lên dốc → divergence với nguồn và điểm hút → curl với bánh xe cánh quạt.

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/calculus-physics-engineering/`.

**Thứ tự xem gợi ý**

1. **ORIENTATION** — 3Blue1Brown — Essence of calculus (series / ch.1 derivative): [https://www.youtube.com/watch?v=WUvTyaaNkzM](https://www.youtube.com/watch?v=WUvTyaaNkzM).
2. **ORIENTATION** — 3Blue1Brown — Essence of calculus playlist hub: [https://www.3blue1brown.com/topics/calculus](https://www.3blue1brown.com/topics/calculus).
3. **CORE** — Brain Station Advanced — Gradient, Divergence and Curl: [https://www.youtube.com/watch?v=m_Psx7CdvDk](https://www.youtube.com/watch?v=m_Psx7CdvDk).
4. **FOUNDATION** — Khan Academy / 3B1B style multivariable (divergence theorem culture): [https://www.youtube.com/watch?v=rB83DpBJQsE](https://www.youtube.com/watch?v=rB83DpBJQsE).
5. **FOUNDATION** — MIT OCW 18.02 Multivariable Calculus (course page): [https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/](https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/).
6. **FOUNDATION** — MIT OCW 18.03 Differential Equations (video lectures): [https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/).

Danh mục URL đầy đủ: `research/video-research/calculus-physics-engineering/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/calculus-physics-engineering/transcripts/` · trạng thái: `research/video-research/calculus-physics-engineering/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/calculus-physics-engineering_WUvTyaaNkzM_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/calculus-physics-engineering/references.md`.

### Video (lộ trình chính)

1. 3Blue1Brown — Essence of calculus (series / ch.1 derivative) — https://www.youtube.com/watch?v=WUvTyaaNkzM
2. 3Blue1Brown — Essence of calculus playlist hub — https://www.3blue1brown.com/topics/calculus
3. Brain Station Advanced — Gradient, Divergence and Curl — https://www.youtube.com/watch?v=m_Psx7CdvDk
4. Khan Academy / 3B1B style multivariable (divergence theorem culture) — https://www.youtube.com/watch?v=rB83DpBJQsE
5. MIT OCW 18.02 Multivariable Calculus (course page) — https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/
6. MIT OCW 18.03 Differential Equations (video lectures) — https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/
7. Gilbert Strang & Cleve Moler — Learn Differential Equations (overview) — https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/
8. 3Blue1Brown — Divergence and curl playlist (multivariable) — https://www.3blue1brown.com/topics/multivariable-calculus

### Video (tìm thêm / phụ)

9. Numberphile / related continuum modeling culture (optional) — https://www.youtube.com/user/numberphile

### Bài báo, sách, OCW và web

10. Evans — Partial Differential Equations (AMS Graduate Studies): https://bookstore.ams.org/gsm-19-r
11. Wikipedia — Fundamental theorem of calculus: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
12. Wikipedia — Finite element method: https://en.wikipedia.org/wiki/Finite_element_method
13. MIT OCW 18.02: https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/
14. MIT OCW 18.03: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/

### Trong khóa

15. Khóa học: [Tổng quan]({{ site.baseurl }}/contents/vi/chapter03/03_00_Tong_quan/), [PTVP]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/). Gói: `research/video-research/calculus-physics-engineering/`.

## Hướng đi tiếp

- Bài tiếp theo: [Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/), [PTVP]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).  
- Bài toán thuần túy liên quan: [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).  
- Tùy chọn: xem [video về gradient, divergence, curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) rồi đọc lại §5.  
- Tự viết lại ý chính của bài trong một đoạn văn, và ghi ra một câu hỏi bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước**: [Best Explanation of Gradient, Divergence and Curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) (Brain Station Advanced, tiếng Anh). Giải thích trực quan ba toán tử gradient, divergence và curl bằng hình ảnh trường vectơ. Nên xem trước khi đọc §5.
- [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) (3Blue1Brown, tiếng Anh). Tập mở đầu của loạt bài về bản chất của giải tích: đạo hàm, tích phân và định lý cơ bản. Hợp với §1 và §2.
- [Divergence and curl: The language of Maxwell's equations, fluid flow, and more](https://www.youtube.com/watch?v=rB83DpBJQsE) (3Blue1Brown, tiếng Anh). Giải thích divergence và curl qua dòng chất lỏng và phương trình Maxwell. Xem sau khi đã nắm §4 và §5.
