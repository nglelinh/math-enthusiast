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

Trong cơ học cổ điển, một viên bi ném lên không trung đi theo đúng một đường parabol duy nhất — đường làm cho đại lượng gọi là *tác dụng* $$S[q]$$ đạt cực trị. Nhưng khi Richard Feynman suy nghĩ lại về thí nghiệm hai khe ở cuối thập niên 1940, ông đẩy trực giác ấy đi đến tận cùng: nếu ta mở ba khe, bốn khe, rồi đục thủng cả bức màn chắn thành vô số khe, và đặt vô số bức màn nối tiếp nhau giữa điểm xuất phát và đích đến, thì một hạt lượng tử đi từ $$(q_i, t_i)$$ đến $$(q_f, t_f)$$ **không chọn một quỹ đạo duy nhất — nó đi qua mọi quỹ đạo có thể cùng một lúc**! Mỗi đường đi $$q(\cdot)$$ đóng góp một mũi tên quay (số phức có môđun 1) là $$\exp(\tfrac{i}{\hbar}S[q])$$ và biên độ tổng là "tổng trên mọi lịch sử":

$$
\langle q_f,t_f|q_i,t_i\rangle \;\sim\; \int \mathcal{D}q\; \exp\!\Big(\frac{i}{\hbar}S[q]\Big).
$$

Ý tưởng **tích phân đường (path integral)** này có sức gợi cảm phi thường: khi $$\hbar$$ nhỏ, các đường đi xa quỹ đạo cổ điển có pha quay cuồng và tự triệt tiêu lẫn nhau, chỉ còn các đường sát quỹ đạo cổ điển cộng hưởng cùng pha; còn hiện tượng giao thoa giữa các đường mang toàn bộ nội dung lượng tử. Thế nhưng dưới con mắt giải tích toán học, ký hiệu $$\mathcal{D}q$$ lại ẩn chứa một sự thật gai góc: nói chung **không tồn tại độ đo Lebesgue trên không gian vô hạn chiều các đường đi** với những tính chất mà nhà vật lý ngầm giả định. Bài này tách rạch ròi ba lớp — **ý tưởng**, **phần đã làm chặt chẽ được**, và **phần vẫn còn là lập luận trực quan** — để bạn đọc vững tay khi đi qua nhánh Cầu nối. Kiến thức nền: [không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/); bài liên quan: [phân bố]({{ site.baseurl }}/contents/vi/chapter03/03_12_Distributions_Dirac/).

---

## Bản đồ kiến thức nền: Tích phân hàm, Độ đo vô hạn chiều và Giải tích tiệm cận nghiên cứu những gì?

Khi "biến lấy tích phân" không còn là một điểm $$x \in \mathbb{R}^n$$ mà là **cả một đường cong liên tục** $$q: [0,T] \to \mathbb{R}^d$$, ta bước vào ba mảng toán học giao thoa với nhau:

### 1. Lý thuyết độ đo vô hạn chiều và Độ đo Wiener
Trong $$\mathbb{R}^n$$, khối lập phương cạnh $$2$$ có thể tích $$2^n \to \infty$$ khi $$n\to\infty$$, còn khối lập phương cạnh $$1/2$$ có thể tích $$(1/2)^n \to 0$$ — nên **không tồn tại độ đo thể tích đều (Lebesgue) trên không gian vô hạn chiều**. Giải pháp của Norbert Wiener (1923) là gộp luôn thừa số Gauss động năng $$e^{-\frac{1}{2}\int \dot{q}^2 dt}$$ vào trong độ đo để tạo thành **độ đo xác suất Wiener** trên không gian các đường liên tục — đây là nền tảng chặt chẽ của chuyển động Brown, tài chính định lượng (Black–Scholes) và công thức Feynman–Kac cho cơ học lượng tử trong thời gian ảo.

### 2. Phương pháp pha dừng và Giải tích tiệm cận
Với tích phân dao động $$\int e^{iS(x)/\hbar} a(x)\,dx$$ khi $$\hbar \to 0$$, giải tích tiệm cận chứng minh rằng đóng góp áp đảo chỉ đến từ lân cận các **điểm dừng** $$S'(x_0) = 0$$ (và các điểm yên ngựa trong thời gian ảo). Trong vật lý, điều này giải thích trực tiếp cách cơ học cổ điển (nguyên lý tác dụng cực tiểu) hiện ra từ cơ học lượng tử.

### 3. Xấp xỉ lưới (Trotter) và Lý thuyết trường kiến thiết
Để biến ký hiệu hình thức $$\mathcal{D}q$$ thành phép tính có nghĩa, các nhà toán học cắt thời gian (hoặc cả không–thời gian) thành $$N$$ lát rời rạc để lấy tích phân $$N$$ biến thông thường, rồi nghiên cứu giới hạn $$N \to \infty$$ (công thức tích Trotter trong cơ học lượng tử; lý thuyết trường trên mạng lưới và lý thuyết trường kiến thiết ở 2D/3D/4D).

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

Paul Dirac (thập niên 1930) nhận thấy biên độ chuyển trạng thái trong khoảng thời gian vô cùng ngắn $$\varepsilon$$ tỉ lệ với $$\exp\!\big(\tfrac{i}{\hbar}\varepsilon L(q, \dot{q})\big)$$, trong đó $$L$$ là hàm Lagrange cổ điển. Richard Feynman (1948) biến nhận xét ngắn ngủi đó thành một cách trình bày hoàn chỉnh của cơ học lượng tử: chia khoảng thời gian $$[t_i, t_f]$$ thành $$N$$ đoạn nhỏ $$\varepsilon = (t_f - t_i)/N$$, chèn phép lấy tích phân theo mọi vị trí trung gian $$q_1, q_2, \dots, q_{N-1}$$ (nối thành một đường gấp khúc), rồi cho $$N \to \infty$$. Khi cả hai phía đều được định nghĩa tốt, cách nhìn này dẫn lại đúng phương trình Schrödinger.

### Khung giải thích: cắt lát thời gian và lấy tổng mọi đường đi bằng tay (nên đọc chậm)

Để cảm nhận tận tay tích phân đường không hề là "ảo thuật", hãy tự tính biên độ chuyển động của một hạt tự do (khối lượng $$m=1, \hbar=1$$) trong thời gian ảo (Euclid) đi từ $$q_0 = 0$$ tại $$\tau = 0$$ đến $$q_2 = x$$ tại $$\tau = 2\varepsilon$$, chỉ với **1 điểm trung gian** $$q_1 \in \mathbb{R}$$ (tức mọi đường gấp khúc 2 đoạn nối $$0 \to q_1 \to x$$):

1. **Viết tác dụng Euclid của đường gấp khúc:** Vận tốc trên đoạn đầu là $$\frac{q_1 - 0}{\varepsilon}$$, trên đoạn sau là $$\frac{x - q_1}{\varepsilon}$$, nên tổng tác dụng $$S_E = \frac{1}{2}\sum v^2 \varepsilon$$ là:
   $$
   S_E(q_1) = \frac{q_1^2}{2\varepsilon} + \frac{(x - q_1)^2}{2\varepsilon}.
   $$
2. **Hoàn thiện bình phương theo biến trung gian $$q_1$$:**
   $$
   q_1^2 + (x - q_1)^2 = 2q_1^2 - 2xq_1 + x^2 = 2\Bigl(q_1 - \frac{x}{2}\Bigr)^2 + \frac{x^2}{2}.
   $$
   Chú ý điểm cực tiểu của tác dụng xảy ra đúng tại $$q_1^* = \frac{x}{2}$$ — trung điểm nằm trên đường thẳng cổ điển nối $$0$$ với $$x$$!
3. **Lấy tích phân trên mọi vị trí trung gian $$q_1 \in (-\infty, \infty)$$** (nhớ công thức Gauss $$\int_{-\infty}^{\infty} e^{-u^2/\varepsilon}\,du = \sqrt{\pi\varepsilon}$$):
   $$
   K(0 \to x;\, 2\varepsilon) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi\varepsilon}}e^{-\frac{q_1^2}{2\varepsilon}} \cdot \frac{1}{\sqrt{2\pi\varepsilon}}e^{-\frac{(x-q_1)^2}{2\varepsilon}}\,dq_1 = \frac{1}{2\pi\varepsilon}\,e^{-\frac{x^2}{4\varepsilon}} \int_{-\infty}^{\infty} e^{-\frac{(q_1 - x/2)^2}{\varepsilon}}\,dq_1 = \frac{1}{\sqrt{4\pi\varepsilon}}\,e^{-\frac{x^2}{4\varepsilon}}.
   $$
4. **Kiểm tra kết quả:** Công thức $$\frac{1}{\sqrt{2\pi T}}e^{-x^2/(2T)}$$ với $$T = 2\varepsilon$$ chính xác là **nhân nhiệt** (nghiệm cơ bản của phương trình khuếch tán $$\partial_T u = \frac{1}{2}\partial_x^2 u$$, hay chuyển động Brown chuẩn)! Lặp lại $$N$$ bước rồi cho $$N \to \infty$$, mọi đường gấp khúc hội tụ thành độ đo Wiener hoàn toàn chặt chẽ.

**Cơ chế chính.** Sự tiến hóa lượng tử được ghép lại từ **biên độ của toàn bộ quỹ đạo**, mỗi quỹ đạo có trọng số pha $$e^{iS/\hbar}$$ (hoặc $$e^{-S_E/\hbar}$$ trong thời gian ảo), chứ không chỉ từ phương trình vi phân cục bộ cho hàm sóng.

---

## 2. Thử trước trong trường hợp hữu hạn chiều

Để cảm nhận nguyên lý **pha dừng (stationary phase)** mà không vướng vô hạn chiều, hãy xét tích phân dao động thông thường trên $$\mathbb{R}^n$$:

$$
I(\hbar)=\int_{\mathbb{R}^n} e^{iS(x)/\hbar}\,a(x)\,dx.
$$

Hãy tưởng tượng $$n=1$$ và $$S(x) = x^2$$. Khi $$\hbar$$ rất nhỏ, ở xa gốc $$x=0$$ thì $$S(x)/\hbar$$ tăng cực nhanh, nên $$\cos(x^2/\hbar)$$ và $$\sin(x^2/\hbar)$$ dao động dương–âm liên tục trong khoảng cực hẹp và **triệt tiêu lẫn nhau**. Chỉ ở ngay quanh điểm tới hạn $$S'(x_0) = 0$$ (tức $$x_0 = 0$$), pha mới biến đổi chậm lại đủ để các đóng góp cộng dồn lên nhau, cho giá trị xấp xỉ tỉ lệ với $$\sqrt{\hbar}\,e^{iS(x_0)/\hbar}$$.

Trong tích phân đường, điều tương tự xảy ra khi thay biến $$x$$ bằng cả một đường đi $$q(\cdot)$$: điểm tới hạn $$\delta S[q] = 0$$ chính là phương trình Euler–Lagrange của cơ học cổ điển! Khi $$\hbar \to 0$$, mọi đường đi ngoằn ngoèo đều tự triệt tiêu vì lệch pha, chỉ để lại một dải hẹp quanh quỹ đạo cổ điển.

---

## 3. Độ đo gặp vấn đề ở đâu?

Không gian các đường đi $$C([0,T],\mathbb{R}^d)$$ là vô hạn chiều. Trên đó không có độ đo Lebesgue bất biến tịnh tiến nào hành xử giống thể tích trong không gian hữu hạn chiều. Vì vậy ký hiệu hình thức $$\mathcal{D}q$$ phải được hiểu là **giới hạn của các tích phân hữu hạn chiều**, hoặc **một độ đo kiểu Gauss gắn với một dạng toàn phương khác**, hoặc một quy trình kiến thiết khác, chứ không phải "độ đo Lebesgue trên các đường".

Với **thời gian thực**, khó khăn còn nặng hơn một bậc: hàm dưới dấu tích phân $$e^{iS/\hbar}$$ có môđun bằng $$1$$ ở khắp nơi và dao động liên tục, nên không có tính hội tụ tuyệt đối (định lý Cameron năm 1960 chứng minh rằng ngay cả dạng phức $$e^{\frac{i}{2}\int \dot{q}^2 dt}\,\mathcal{D}q$$ cũng **không** tạo thành một độ đo phức có biến phân hữu hạn!). **Phép quay Wick** $$t\to -i\tau$$ (khi biện minh được bằng thác triển giải tích) đổi thừa số dao động $$e^{iS/\hbar}$$ thành thừa số suy giảm dương thực $$e^{-S_E/\hbar}$$, đưa tích phân đường sang không gian **Euclid** — nơi nó có cấu trúc giống hệt hàm phân hoạch $$\sum e^{-\beta E}$$ của cơ học thống kê.

---

## 4. Những trường hợp đã chặt chẽ

| Bối cảnh | Đối tượng toán học | Trạng thái |
|----------|----------------|----------------------|
| Chuyển động Brown | **Độ đo Wiener** trên các đường liên tục | Hoàn toàn chặt chẽ |
| Cơ học lượng tử với thời gian ảo | Công thức Feynman–Kac | Định lý, dưới các giả thiết về thế $$V$$ |
| Lý thuyết trường lượng tử trên mạng lưới hữu hạn | Tích phân nhiều biến thông thường | Định nghĩa tốt; bước khó là lấy giới hạn liên tục |
| Lý thuyết trường lượng tử nhiễu loạn | Chuỗi hình thức các giản đồ Feynman | Rất mạnh; nhưng không phải định nghĩa phi nhiễu loạn |
| Dựng Yang–Mills 4 chiều | Độ đo liên tục và khe khối lượng | [Bài toán Clay còn mở]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/) |

Để thấy độ chặt chẽ hoạt động ra sao trong thực tế, hãy nhìn vào hai trụ cột đầu bảng:
- **Công thức tích Trotter** viết $$e^{-it(T+V)/\hbar} = \lim_{N\to\infty}\bigl(e^{-i\frac{t}{N}T/\hbar}e^{-i\frac{t}{N}V/\hbar}\bigr)^N$$ — mỗi bước nhỏ tách riêng phần động năng $$T$$ và thế năng $$V$$, biện minh chặt chẽ cho việc cắt lát thời gian của cơ học lượng tử với thế năng đủ tốt.
- **Công thức Feynman–Kac** biểu diễn nghiệm của phương trình nhiệt có thế năng $$\partial_\tau u = \frac{1}{2}\Delta u - V(x)u$$ trực tiếp như kỳ vọng $$\mathbb{E}_x\bigl[e^{-\int_0^\tau V(B_s)\,ds} u_0(B_\tau)\bigr]$$ lấy theo chuyển động Brown $$B_s$$ — hoàn toàn chuẩn mực theo lý thuyết xác suất hiện đại!

---

## 5. Instanton, hiệu ứng đường hầm, tô pô

Trong không–thời gian Euclid, ngoài đường đi cực tiểu tầm thường (đứng yên ở đáy thế năng), tác dụng $$S_E$$ còn có thể có các điểm yên ngựa không tầm thường — kể cả **instanton** — đóng góp những hiệu ứng nhỏ cỡ $$e^{-S_E/\hbar}$$. Ví dụ trực quan nhất là hạt lượng tử trong giếng thế đôi hình chữ W: cổ điển thì hạt ở đáy trái không thể tự vượt qua đỉnh đồi sang đáy phải; nhưng trong thời gian ảo, đỉnh đồi bị lật ngược thành thung lũng nên tồn tại một đường đi cổ điển (instanton) nối đáy trái sang đáy phải với tác dụng hữu hạn $$S_0$$, cho ra xác suất xuyên hầm tỉ lệ với $$e^{-S_0/\hbar}$$.

Các hiệu ứng dạng $$e^{-c/\hbar}$$ có mọi đạo hàm theo $$\hbar$$ tại $$0$$ đều bằng $$0$$, nên **không bao giờ thấy được ở bất kỳ bậc hữu hạn nào của lý thuyết nhiễu loạn** ([instanton và dị thường]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/), [lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)). Ở đây, tích phân đường là **ngôn ngữ để ghi chép** khai triển quanh các điểm yên ngựa; còn chính các điểm yên ngựa thì được cung cấp bởi giải tích hình học của các nghiệm cổ điển.

---

## 6. Lý thuyết trường lượng tử: điểm mạnh và khoảng trống

Trong lý thuyết trường lượng tử, tích phân đường hình thức tính các hàm tương quan bằng tích phân trên mọi cấu hình trường $$\phi(x)$$ với trọng số $$e^{iS[\phi]/\hbar}$$. Khai triển quanh trường tự do cho ta các quy tắc Feynman (đường truyền propagator ứng với nghịch đảo của toán tử vi phân, đỉnh tương tác ứng với hệ số phi tuyến).

**Điểm mạnh.** Thống nhất cách xử lý đối xứng (đặc biệt là đối xứng Lorentz và đối xứng gauge), sinh ra kỹ thuật giản đồ Feynman cực kỳ hiệu quả, nối trực tiếp với lý thuyết trường thống kê qua phiên bản Euclid, và gợi ý ra lý thuyết trường lượng tử tô pô (TQFT) cùng các phép đối ngẫu.

**Khoảng trống.** Việc dựng chặt chẽ một lý thuyết liên tục có tương tác ở 4 chiều, phù hợp với Mô hình chuẩn, vẫn là một bài toán chưa giải xong, dù các dự đoán vật lý (như mômen từ dị thường của electron, khớp thực nghiệm tới hơn 10 chữ số thập phân!) thành công rực rỡ trong phạm vi hiệu lực của chúng.

---

## 7. Nói chính xác, tránh thổi phồng

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Tích phân đường chặt chẽ như tích phân Riemann cho mọi hệ." | Sai | Độ đo vô hạn chiều chính là vấn đề. |
| "Tích phân đường khớp thực nghiệm QED, vậy độ đo đã được chứng minh." | Nhầm loại | Thành công thực nghiệm không phải là chứng minh sự tồn tại theo nghĩa kiến thiết. |
| "Độ đo Wiener chính là tích phân đường Feynman." | Thiếu | Độ đo Wiener gắn với thời gian ảo và quá trình khuếch tán. |
| "Tích phân đường thay thế không gian Hilbert." | Gây hiểu nhầm | Hai cách thường tương đương khi cả hai được định nghĩa; không gian Hilbert vẫn giữ vai trò trung tâm. |

---

## Tài liệu tham khảo

1. Feynman & Hibbs, *Quantum Mechanics and Path Integrals* (Cơ học lượng tử và tích phân đường).  
2. Simon, *Functional Integration and Quantum Physics* (Tích phân hàm và vật lý lượng tử).  
3. Trong khóa học: [Không gian Hilbert và cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [Instanton]({{ site.baseurl }}/contents/vi/chapter06/06_21_Instantons_Anomalies/), [Nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/), [Bài toán khe khối lượng Yang–Mills]({{ site.baseurl }}/contents/vi/chapter01/01_10_Yang_Mills_Mass_Gap/).  
