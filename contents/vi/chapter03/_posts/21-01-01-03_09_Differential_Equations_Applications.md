---
layout: post
title: "Phương trình Vi phân → Ứng dụng"
chapter: '03'
order: 9
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
lesson_type: required
---

Một nhà dịch tễ học muốn biết liệu đợt dịch cúm mùa này sẽ đạt đỉnh sau ba tuần nữa hay sẽ sớm lắng xuống nếu đóng cửa trường học. Một chuyên gia khí tượng muốn dự báo đường đi của cơn bão nhiệt đới trong 72 giờ tới. Một kỹ sư điện tử muốn chắc chắn mạch nguồn sẽ không tự rung rồi cháy tụ khi bật công tắc. Không ai trong số họ có quả cầu pha lê — nhưng cả ba đều làm chung một việc: **viết xuống quy luật cho biết trạng thái hiện tại quyết định tốc độ thay đổi trong khoảnh khắc tiếp theo như thế nào**.

Chính dòng quy luật đó là một **phương trình vi phân**. Nếu giải tích là bảng chữ cái, thì phương trình vi phân là những câu văn hoàn chỉnh mô tả cách cả vũ trụ vận động theo thời gian và không gian.

Bài học này nối tiếp bài [Giải tích → Vật lý & Kỹ thuật]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/) bằng một tấm bản đồ mạch lạc về các **họ phương trình**, khái niệm **bài toán đặt chỉnh** (khi nào ta có thể tin vào dự báo), và lý do vì sao tính toán số mới là con đường chủ lực trong công nghiệp. Về một câu hỏi lý thuyết hóc búa nhất vẫn còn bỏ ngỏ, xem [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).

**Lộ trình:** bản đồ ngành phương trình vi phân → ba thành phần của một mô hình → danh mục ODE → danh mục PDE → bài toán đặt chỉnh Hadamard → cấu trúc tuyến tính và các mode → phi tuyến và hỗn loạn → phương pháp số → điều khiển, bài toán ngược và bản sao số → nhầm lẫn thường gặp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhìn qua là phân biệt được ODE với PDE, hệ ôtônôm (không phụ thuộc tường minh vào thời gian) với hệ không ôtônôm.
- Nhận ra các phương trình chuẩn: hệ ODE tuyến tính, phương trình nhiệt, sóng, Laplace, truyền tải (transport), phản ứng – khuếch tán.
- Phát biểu ba điều kiện **đặt chỉnh** của Hadamard (tồn tại, duy nhất, phụ thuộc liên tục vào dữ liệu) và giải thích vì sao kỹ sư cần chúng.
- Giải thích ý tưởng các mode riêng (hay mode Fourier) cho bài toán tuyến tính hệ số hằng.
- Mô tả sai phân hữu hạn, phần tử hữu hạn và các phương pháp bước thời gian như cách làm trong công nghiệp khi không có nghiệm tường minh.
- Tránh hai nhầm lẫn: "viết được phương trình là có một nghiệm đẹp và duy nhất" và "tính số chỉ là bấm nút Solve".

**Kiến thức nền.** Đạo hàm và bài [giải tích làm hạ tầng]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/). Sẽ có ích nếu biết [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/) và [đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/).

---

## Bản đồ kiến thức nền: Lý thuyết phương trình vi phân là gì và nghiên cứu những gì?

Khi giải một phương trình đại số như $$x^2 - 5x + 6 = 0$$, đáp án là vài con số cụ thể. Khi giải một **phương trình vi phân (differential equation)**, ẩn số là **cả một hàm số** $$x(t)$$ hoặc một trường $$u(x,y,z,t)$$ mô tả toàn bộ lịch sử tiến hóa của hệ thống.

Ở đại học, nhiều sinh viên tưởng học phương trình vi phân là thuộc hàng tá mẹo giải tích phân để ra công thức đẹp. Trên thực tế, 99% phương trình vi phân xuất hiện trong khoa học kỹ thuật **không hề có nghiệm công thức đóng**. Vì vậy, ngành phương trình vi phân hiện đại nghiên cứu bốn câu hỏi sâu sắc hơn nhiều:

1. **Tính đặt chỉnh (Well-posedness):** phương trình có nghiệm không, nghiệm có duy nhất không, và nếu số đo ban đầu sai lệch $$0{,}1\%$$ thì kết quả dự báo có bị phá hỏng không?
2. **Phân tích định tính & Hệ động lực:** không cần giải tường minh, ta vẫn có thể biết quỹ đạo sẽ hội tụ về trạng thái cân bằng ổn định, dao động tuần hoàn mãi mãi, hay rơi vào hỗn loạn (chaos).
3. **Phân loại cấu trúc (ODE và PDE elliptic / parabolic / hyperbolic):** nhận diện bản chất vật lý đằng sau phương trình — nó làm mịn thông tin, truyền sóng đi xa, hay mô tả cân bằng tĩnh?
4. **Giải tích số (Numerical Analysis):** thiết kế thuật toán rời rạc hóa chạy ổn định trên máy tính mà không bị sai số tích lũy làm "nổ" nghiệm.

---

## 1. Ba thành phần của một mô hình

Một mô hình phương trình vi phân hoàn chỉnh luôn có đủ ba mảnh ghép: (1) **biến trạng thái** (dân số, nhiệt độ, vận tốc), (2) **quy luật tốc độ thay đổi** (bản thân phương trình vi phân), và (3) **điều kiện bổ sung** để chốt ra đúng một quỹ đạo vật lý — gồm **bài toán giá trị ban đầu (IVP)** (cho trạng thái lúc $$t=0$$) và/hoặc **bài toán biên (BVP)** (cho nhiệt độ, lực kéo ở vỏ ngoài của miền không gian).

**Ý chính.** *Dự đoán tương lai là bài toán xuôi (giải phương trình vi phân); còn thiết kế kỹ thuật thường là bài toán ngược: tìm tham số vật liệu hoặc tín hiệu điều khiển sao cho nghiệm đi đúng quỹ đạo mong muốn.*

---

## 2. Danh mục ODE: trạng thái hữu hạn chiều

Dạng tổng quát là $$\dot{x}=f(x,t)$$ với $$x\in\mathbb{R}^d$$ (nếu $$f$$ không chứa $$t$$ tường minh thì gọi là hệ **ôtônôm**, nghĩa là quy luật tự nhiên không đổi theo thời gian).

- **Hệ tuyến tính $$\dot{x}=Ax+Bu(t)$$:** trái tim của lý thuyết điều khiển cổ điển; tính ổn định quyết định hoàn toàn bởi dấu phần thực các giá trị riêng của $$A$$.
- **Các hệ phi tuyến kinh điển:** phương trình tăng trưởng giới hạn logistic, con lắc lớn, hệ thú săn mồi – con mồi Lotka–Volterra, và **mô hình dịch bệnh SIR**:
$$
\dot{S} = -\beta S I,\qquad \dot{I} = \beta S I - \gamma I,\qquad \dot{R} = \gamma I,
$$
trong đó $$S, I, R$$ là số người cảm nhiễm, đang nhiễm và đã hồi phục. Chỉ nhìn phương trình thứ hai ta đã thấy ngay khái niệm nổi tiếng **hệ số lây nhiễm cơ bản** $$R_0 = \frac{\beta S_0}{\gamma}$$: nếu $$R_0 > 1$$ thì $$\dot{I} > 0$$ (dịch bùng phát), nếu $$R_0 < 1$$ thì $$\dot{I} < 0$$ (dịch tự tắt)!

**Định lý Picard–Lindelöf và cảnh báo "nổ nghiệm".** Nếu $$f$$ đủ trơn (Lipschitz theo $$x$$), nghiệm chắc chắn tồn tại và duy nhất trong một khoảng thời gian ngắn. Nhưng đừng tưởng nghiệm luôn sống mãi! Xét phương trình vô hại $$\dot{x}=x^2$$ với $$x(0)=1$$: nghiệm chính xác là $$x(t)=\frac{1}{1-t}$$, **bùng nổ ra vô cực ngay tại thời điểm hữu hạn $$t=1$$** dù phương trình không có điểm kỳ dị nào!

---

## 3. Danh mục PDE: các trường theo không gian và thời gian

| Phương trình | Dạng (sơ lược) | Hiện tượng |
|--------------|--------------|------------|
| Truyền tải | $$\partial_t u+v\cdot\nabla u=0$$ | Đối lưu |
| Nhiệt | $$\partial_t u=\kappa\Delta u$$ | Làm trơn, truyền nhiệt |
| Sóng | $$\partial_{tt}u=c^2\Delta u$$ | Lan truyền với tốc độ hữu hạn |
| Laplace/Poisson | $$\Delta u=0$$ / $$f$$ | Thế cân bằng |
| Phản ứng – khuếch tán | $$\partial_t u=D\Delta u+R(u)$$ | Hình thành hoa văn, hóa học, sinh thái |
| Navier–Stokes | Phương trình động lượng + điều kiện không nén | Chất lỏng ([Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/)) |

**Ba tính cách hoàn toàn khác nhau của PDE:**
- **Elliptic (Laplace/Poisson):** mô tả trạng thái cân bằng tĩnh (như mặt trống căng trên khung). Thay đổi một điểm ở biên lập tức ảnh hưởng toàn bộ miền bên trong.
- **Parabolic (Nhiệt/Khuếch tán):** có chiều mũi tên thời gian một chiều — làm mịn mọi góc nhọn gần như tức thì (như giọt mực loang trong cốc nước).
- **Hyperbolic (Sóng/Truyền tải):** truyền tín hiệu đi với tốc độ hữu hạn $$c$$ và giữ nguyên các mặt gián đoạn (như tiếng nổ siêu thanh tạo sóng xung kích).

Nhận nhầm loại phương trình không chỉ làm sai trực giác vật lý mà còn dẫn tới chọn sai hoàn toàn thuật toán số.

---

## 4. Bài toán đặt chỉnh theo Hadamard

Nhà toán học Jacques Hadamard đặt ra ba tiêu chuẩn vàng cho một bài toán **đặt chỉnh (well-posed)**: (1) **tồn tại** nghiệm, (2) nghiệm **duy nhất**, và (3) nghiệm **phụ thuộc liên tục** vào dữ liệu đầu vào.

**Ví dụ trực quan về bài toán KHÔNG đặt chỉnh.** Phương trình nhiệt chạy *xuôi* theo thời gian rất đặt chỉnh. Nhưng hãy thử chạy ngược nó để hỏi: *"Biết nhiệt độ thanh sắt lúc này, hãy tính xem 10 giây trước ai đã châm lửa vào đâu?"* Vì khuếch tán đã xóa sạch mọi dao động tần số cao theo hệ số $$e^{-\kappa n^2 t}$$, chạy ngược thời gian sẽ nhân ngược với $$e^{+\kappa n^2 t}$$: chỉ một sai số đo nhiệt kế nhỏ tí $$0{,}01^\circ\mathrm{C}$$ cũng phình to thành hàng triệu độ ở quá khứ!

Bài toán không đặt chỉnh xuất hiện đầy rẫy trong thực tế (chụp cắt lớp CT, khử nhòe ảnh, tìm mỏ dầu từ sóng địa chấn) — và cách duy nhất để giải chúng là thêm **chính quy hóa (regularization)** từ [tối ưu hóa]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/).

**Liên hệ Thiên niên kỷ.** **Bài toán Navier–Stokes** hỏi xem nghiệm của phương trình chất lỏng 3D có luôn tồn tại trơn tru trên mọi thời gian mà không bị "nổ" thành điểm kỳ dị hay không. Dù câu hỏi đặt chỉnh chặt chẽ này vẫn chưa có lời giải, các phần mềm CFD vẫn thiết kế được máy bay nhờ mô hình hóa dòng rối, kiểm chứng thí nghiệm trong hầm gió và hệ số an toàn kỹ thuật.

---

## 5. Cấu trúc tuyến tính: nguyên lý chồng chất và các mode

Với phương trình tuyến tính thuần nhất, nếu $$u_1$$ và $$u_2$$ là nghiệm thì mọi tổ hợp $$c_1 u_1 + c_2 u_2$$ cũng là nghiệm (**nguyên lý chồng chất**). Nhờ đó ta có thể bẻ một bài toán phức tạp thành tổng của những **mode riêng** đơn giản: ODE hệ số hằng tách thành các hàm mũ $$e^{\lambda t}$$, còn PDE trên miền đơn giản tách bằng **phương pháp tách biến** thành chuỗi hàm riêng (chuỗi Fourier, hàm điều hòa cầu).

**Ý chính.** *Phép biến đổi [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/) chéo hóa nhiều toán tử PDE tuyến tính hệ số hằng; mỗi mode tần số tiến hóa hoàn toàn độc lập theo một ODE vô hướng.*

Trong cơ khí kết cấu, tìm tần số cộng hưởng nguy hiểm của một cây cầu hay cánh tua-bin chính là giải bài toán trị riêng tổng quát $$K\phi=\omega^2 M\phi$$ sau khi rời rạc hóa bằng phần tử hữu hạn.

---

## 6. Phi tuyến: vì sao hiếm khi có nghiệm tường minh

Khi phương trình trở nên phi tuyến, nguyên lý chồng chất biến mất — tổng hai nghiệm không còn là nghiệm nữa, và những hiện tượng kỳ thú bậc nhất của tự nhiên lập tức xuất hiện: **rẽ nhánh** (thay đổi nhẹ một tham số làm hành vi hệ đổi đột ngột), **chu trình giới hạn** (nhịp tim tự duy trì ổn định), **hoa văn Turing** (vằn ngựa vằn từ phương trình phản ứng – khuếch tán), **sóng xung kích** (tắc đường cao tốc hay sóng nổ máy bay), và **hỗn loạn tất định (chaos)**.

**Ví dụ về hỗn loạn (Hệ Lorenz và giới hạn dự báo thời tiết).** Năm 1963, Edward Lorenz rút gọn mô hình đối lưu khí quyển xuống chỉ còn **3 ODE phi tuyến** hoàn toàn tất định. Ấy vậy mà chỉ cần làm tròn điều kiện ban đầu ở chữ số thập phân thứ 6 ($$0{,}506127$$ thành $$0{,}506$$), hai quỹ đạo chỉ sau vài ngày đã tách nhau ra hoàn toàn khác biệt! Đó là lý do toán học sâu xa khiến dự báo thời tiết chi tiết từng giờ gặp trần giới hạn khoảng 2 tuần, bất kể siêu máy tính có mạnh gấp bao nhiêu lần.

---

## 7. Phương pháp số: con đường chính trong công nghiệp

Vì phần lớn phương trình thực tế không giải được bằng bút giấy, giải tích số là cánh tay nối dài của ngành:

- **Bước thời gian cho ODE:** Euler hiện (đơn giản nhưng dễ mất ổn định), Runge–Kutta bậc 4 (RK4 — công cụ đa năng kinh điển), và **phương pháp ẩn** cho các **hệ cứng (stiff)**.
- **Rời rạc hóa không gian cho PDE:** sai phân hữu hạn, thể tích hữu hạn, phần tử hữu hạn (FEM), phương pháp phổ — tất cả đưa về hệ đại số tuyến tính cỡ lớn ([Đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/)).
- **Điều kiện ổn định CFL (Courant–Friedrichs–Lewy):** với phương trình sóng truyền tốc độ $$c$$ trên lưới không gian $$\Delta x$$ và bước thời gian $$\Delta t$$, sơ đồ hiện bắt buộc thỏa $$\frac{c\,\Delta t}{\Delta x} \le 1$$. Trực giác cực kỳ tự nhiên: *trong một nhịp đồng hồ $$\Delta t$$, sóng vật lý không được phép chạy vọt qua quá một ô lưới $$\Delta x$$*, nếu không thuật toán số sẽ "không kịp nhìn thấy" sóng và nghiệm lập tức nổ tung!

### Ví dụ cầm tay chỉ việc: Vì sao Euler hiện bị "nổ" còn Euler ẩn lại sống sót?

Xét phương trình phân rã cực đơn giản $$\dot{y} = -10y$$ với $$y(0) = 1$$ (nghiệm đúng là $$y(t) = e^{-10t}$$, luôn dương và giảm êm về $$0$$). Hãy thử mô phỏng bằng máy tính với bước thời gian $$\Delta t = 0{,}25$$:

1. **Phương pháp Euler hiện** ($$y_{n+1} = y_n + \Delta t(-10y_n) = (1 - 10\Delta t)y_n = -1{,}5\,y_n$$):
$$
y_0 = 1 \;\to\; y_1 = -1{,}5 \;\to\; y_2 = +2{,}25 \;\to\; y_3 = -3{,}375 \;\to\; y_4 = +5{,}0625 \;\to\; \pm\infty!
$$
Dù nghiệm thật giảm êm về $$0$$, chỉ vì bước $$\Delta t = 0{,}25$$ vượt ngưỡng ổn định ($$\Delta t \le 0{,}2$$), lời giải số dao động trái dấu và **nổ tung ra vô cực**!
2. **Phương pháp Euler ẩn** (dùng độ dốc tại điểm mới $$y_{n+1} = y_n + \Delta t(-10y_{n+1}) \implies y_{n+1} = \frac{y_n}{1 + 10\Delta t} = \frac{y_n}{3{,}5}$$):
$$
y_0 = 1 \;\to\; y_1 \approx 0{,}286 \;\to\; y_2 \approx 0{,}082 \;\to\; y_3 \approx 0{,}023 \;\to\; 0.
$$
Dù dùng đúng bước $$\Delta t = 0{,}25$$ lớn như nhau, Euler ẩn vẫn **ổn định tuyệt đối**, giữ nguyên tính dương và tắt về 0! Đó là lý do mọi phần mềm mô phỏng mạch điện và hóa học (các hệ cứng có thang thời gian chênh nhau $$10^6$$ lần) đều bắt buộc dùng bộ giải ẩn.

### Khung giải thích: Tại sao một mô phỏng PDE trên siêu máy tính vẫn có thể sai? (nên đọc chậm)

1. **Sai tầng mô hình & loại phương trình:** chọn sai định luật vật lý hoặc nhầm điều kiện biên thì lời giải có hội tụ mượt đến mấy vẫn mô tả một thế giới không có thật.
2. **Bỏ qua tính đặt chỉnh Hadamard:** với bài toán ngược không đặt chỉnh (như chạy ngược phương trình nhiệt), lưới càng mịn thì nhiễu đo đạc càng bị khuếch đại khủng khiếp nếu không có chính quy hóa.
3. **Vi phạm điều kiện ổn định số (CFL / hệ cứng):** bước thời gian $$\Delta t$$ quá lớn so với tốc độ sóng hoặc độ cứng của hệ sẽ làm sai số làm tròn bùng nổ theo hàm mũ như ví dụ Euler hiện ở trên.
4. **Đánh đồng Kiểm chứng (Verification) với Thẩm định (Validation):** kiểm chứng chỉ xác nhận *"code giải đúng phương trình đã viết"*; còn thẩm định mới xác nhận *"phương trình đó khớp với thí nghiệm ngoài đời thật"*.

**Kiểm tra nhanh.** Một bức ảnh mô phỏng CFD nhiều màu sắc chỉ đáng tin khi đã qua đủ cả hai cửa: **kiểm chứng hội tụ lưới** (toán học số) và **thẩm định bằng số liệu đo thực tế** (vật lý).

---

## 8. Điều khiển, bài toán ngược, bản sao số

- **Điều khiển tự động:** không chỉ đứng nhìn hệ tiến hóa, kỹ sư chèn thêm đầu vào $$u(t)$$ (lực đẩy tên lửa, dòng điện mô-tơ) để ép quỹ đạo $$x(t)$$ bám sát mục tiêu (PID, LQR, điều khiển dự báo MPC).
- **Bài toán ngược (Inverse problems):** từ vài cảm biến đặt bên ngoài, suy ngược lại tham số ẩn bên trong (như tìm vị trí vết nứt ngầm trong bê tông).
- **Bản sao số (Digital twin):** kết hợp mô hình phương trình vi phân với luồng dữ liệu cảm biến thời gian thực (đồng hóa dữ liệu) để theo dõi sức khỏe công trình và tối ưu bảo trì.

---

## 9. Vị trí trong Chương 3

| Mạch nội dung | Vai trò của phương trình vi phân |
|-----|--------------|
| Giải tích | Tốc độ thay đổi và tích lũy trở thành phương trình |
| Đại số tuyến tính | Toán tử rời rạc; các mode; hệ $$Ax=b$$ |
| Xác suất | Phương trình vi phân ngẫu nhiên (SDE); đồng hóa dữ liệu có nhiễu |
| Tối ưu | Thiết kế với ràng buộc là PDE; điều khiển dự báo (MPC) |
| Fourier | Chéo hóa PDE tuyến tính hệ số hằng |
| Đồ thị | Rời rạc hóa không gian; động lực học trên mạng |

Chủ đề xuyên suốt của chương: **một đối tượng toán học (phương trình cho các hàm số) trở thành hạ tầng công nghiệp khi ta hiểu đủ sâu cả ba mặt — tính đặt chỉnh, cấu trúc vật lý và phương pháp số — để đưa vào sản phẩm.**

---

### Tóm tắt về mô hình phương trình vi phân (từ phần tìm hiểu video)

Lộ trình bậc đại học: [Strang & Moler Learn DE](https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/) và [3B1B DE intro](https://www.youtube.com/watch?v=p_di4Zn4wz4).

- **Ba thành phần của mô hình:** biến trạng thái + quy luật tốc độ thay đổi → phương trình + dữ liệu ban đầu hoặc dữ liệu biên.
- **Hadamard:** tồn tại, duy nhất, phụ thuộc liên tục; cần cả ba để kết quả đáng tin cậy về mặt kỹ thuật.
- Hầu hết lời giải trong công nghiệp là lời giải số; phân tích toán học vẫn quyết định tính ổn định, xử lý phương trình cứng, và tính hợp lệ của kết quả.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Viết được phương trình vi phân là có nghiệm duy nhất trên toàn thời gian." | Cần định lý tồn tại; nghiệm có thể nổ hoặc không duy nhất. |
| "Mô phỏng CFD chứng tỏ bài toán Navier–Stokes đã giải xong." | Tính toán số cộng mô hình không phải là lời giải bài toán Thiên niên kỷ. |
| "Phương trình cứng là phương trình khó dùng." | "Cứng" là một tính chất kỹ thuật: hệ có các thang thời gian chênh lệch rất lớn. |
| "Lưới càng mịn càng tốt." | Cần sơ đồ số ổn định và hội tụ; sai mô hình vẫn còn nguyên. |
| "Điều kiện ban đầu và điều kiện biên chỉ để trang trí." | Chúng quyết định nghiệm; điều kiện biên sai là vật lý sai. |

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/differential-equations-applications/`.

**Thứ tự xem gợi ý**

1. **FOUNDATION** — MIT RES.18-009 — Learn Differential Equations (Strang & Moler): [https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/](https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/).
2. **FOUNDATION** — MIT Learn DE YouTube playlist: [https://www.youtube.com/playlist?list=PLUl4u3cNGP63oTpyxCMLKt_JmB0WtSZfG](https://www.youtube.com/playlist?list=PLUl4u3cNGP63oTpyxCMLKt_JmB0WtSZfG).
3. **FOUNDATION** — MIT 18.03 Differential Equations video lectures (Mattuck): [https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/).
4. **INTUITION** — 3Blue1Brown — Differential equations series hub: [https://www.3blue1brown.com/topics/differential-equations](https://www.3blue1brown.com/topics/differential-equations).
5. **ORIENTATION** — 3Blue1Brown — Differential equations, a visual introduction: [https://www.youtube.com/watch?v=p_di4Zn4wz4](https://www.youtube.com/watch?v=p_di4Zn4wz4).
6. **CORE** — Strang — First-order equations (2.087 sample): [https://www.youtube.com/watch?v=4X0SGGrXDiI](https://www.youtube.com/watch?v=4X0SGGrXDiI).

Danh mục URL đầy đủ: `research/video-research/differential-equations-applications/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/differential-equations-applications/transcripts/` · trạng thái: `research/video-research/differential-equations-applications/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/differential-equations-applications_p_di4Zn4wz4_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/differential-equations-applications/references.md`.

### Video (lộ trình chính)

1. MIT RES.18-009 — Learn Differential Equations (Strang & Moler) — https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/
2. MIT Learn DE YouTube playlist — https://www.youtube.com/playlist?list=PLUl4u3cNGP63oTpyxCMLKt_JmB0WtSZfG
3. MIT 18.03 Differential Equations video lectures (Mattuck) — https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/
4. 3Blue1Brown — Differential equations series hub — https://www.3blue1brown.com/topics/differential-equations
5. 3Blue1Brown — Differential equations, a visual introduction — https://www.youtube.com/watch?v=p_di4Zn4wz4
6. Strang — First-order equations (2.087 sample) — https://www.youtube.com/watch?v=4X0SGGrXDiI
7. Numerical ODE solvers culture (Runge–Kutta explainers) — https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods
8. Heat equation derivations (popular PDE intros) — https://en.wikipedia.org/wiki/Heat_equation

### Video (tìm thêm / phụ)

9. Strogatz Nonlinear Dynamics lectures / book culture — https://www.youtube.com/watch?v=PVo1mHnU7WU

### Bài báo, sách, OCW và web

10. Hairer, Nørsett, Wanner — Solving Ordinary Differential Equations: https://link.springer.com/book/10.1007/978-3-540-78862-1
11. Wikipedia — Ordinary differential equation: https://en.wikipedia.org/wiki/Ordinary_differential_equation
12. Wikipedia — Partial differential equation: https://en.wikipedia.org/wiki/Partial_differential_equation
13. Wikipedia — Well-posed problem: https://en.wikipedia.org/wiki/Well-posed_problem
14. MIT OCW 18.03: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/
15. Strang — Differential Equations and Linear Algebra resources: https://math.mit.edu/~gs/dela/

### Trong khóa

16. Khóa: [Giải tích]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/), [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/). Gói: `research/video-research/differential-equations-applications/`.

## Hướng đi tiếp

- Đọc lại bài [Giải tích]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/) (phần phần tử hữu hạn và biến phân).  
- Một bài toán còn mở: [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).  
- [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/).  
- Tự viết lại ý chính của bài trong một đoạn văn, và ghi ra một câu hỏi bạn vẫn còn thắc mắc.


## Mô hình, đo đạc và giới hạn của dự báo

Trong ứng dụng, phương trình vi phân hiếm khi "đúng tuyệt đối". Chúng là **mô hình**, kèm theo các giả thiết về ma sát, về tuyến tính hóa, về việc bỏ qua độ trễ, hay về việc xấp xỉ một hệ rời rạc bằng một mô hình liên tục. Khi thảo luận, nên luôn tách ba tầng:

1. **Phương trình lý tưởng** (sự tồn tại và duy nhất nghiệm trong một không gian hàm thích hợp).
2. **Mô hình kỹ thuật** (hệ số đo được, nhiễu, điều kiện biên thực tế).
3. **Thuật toán số** (bước thời gian, tính ổn định, sai số cắt cụt).

Khi đọc tin "AI dự báo thời tiết bằng PDE hay bằng neural operator", hãy hỏi: đang xấp xỉ toán tử nào, trên lưới nào, và sai số được đo theo chuẩn nào? Câu trả lời thuộc về phương trình vi phân ứng dụng không kém gì thuộc về AI và tối ưu.

## Bài thực hành ngắn

Chọn một hệ một chiều (dao động có cản, hoặc mô hình logistic có khai thác). Viết ra (i) phương trình, (ii) một giả thiết đã bị bỏ qua, (iii) một đại lượng quan sát được, (iv) một câu phân biệt: điều gì vẫn là định lý toán học thuần túy, và điều gì là kết quả mô phỏng.


## Video tham khảo

- **Xem trước**: [Differential equations, a tourist's guide | DE1](https://www.youtube.com/watch?v=p_di4Zn4wz4) (3Blue1Brown, tiếng Anh). Giới thiệu trực quan phương trình vi phân qua con lắc và không gian pha. Nên xem trước khi đọc §1 và §2.
- [2. First-Order Equations](https://www.youtube.com/watch?v=4X0SGGrXDiI) (MIT OpenCourseWare, tiếng Anh). Bài giảng về phương trình vi phân bậc nhất trong loạt bài của Gilbert Strang. Hợp với §2.
- [Logistic Map Explained (Strogatz Ch. 10): Period-Doubling Route to Chaos | Part 1](https://www.youtube.com/watch?v=PVo1mHnU7WU) (Dr. Shane Ross, tiếng Anh). Ánh xạ logistic và con đường nhân đôi chu kỳ dẫn đến hỗn loạn. Lưu ý đây là hệ rời rạc (ánh xạ lặp), không phải ODE; dùng làm góc nhìn bổ sung cho §6.
