---
layout: post
title: "Vận chuyển tối ưu và tính chính quy của Figalli (Huy chương Fields 2018)"
chapter: '02'
order: 20
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Năm 1781, kỹ sư quân sự Pháp **Gaspard Monge** đứng trước một câu hỏi trần tục trên công trường: làm thế nào để xúc một đống đất lớn và đổ đầy một hố công sự gần đó sao cho tổng công vận chuyển là nhỏ nhất? Hơn hai thế kỷ sau, bài toán xúc đất ấy đã lớn lên thành một trong những ngôn ngữ thống nhất mạnh mẽ nhất của toán học hiện đại — **lý thuyết vận chuyển tối ưu** (*optimal transport*, OT) — kết nối từ hình dạng tinh thể, chuyển động của các front khí quyển, đến hình học không gian cong và học máy.

Thế nhưng giữa việc biết "tồn tại một phương án vận chuyển rẻ nhất" và việc thực sự *dùng* được ánh xạ vận chuyển đó trong phương trình đạo hàm riêng lại có một vực thẳm: liệu ánh xạ vận chuyển có **trơn** không, hay nó xé rách đống cát thành từng mảng gãy khúc? Năm 2018, **Alessio Figalli** nhận **Huy chương Fields**

> “for contributions to the theory of optimal transport and its applications in partial differential equations, metric geometry and probability.”
> — [IMU, Fields Medals 2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)

*Tạm dịch:* Cho các đóng góp vào lý thuyết vận chuyển tối ưu và các ứng dụng của nó trong phương trình đạo hàm riêng, hình học metric và xác suất.

Hãy đặt ngay một cột mốc trung thực: **Figalli không phát minh ra vận chuyển tối ưu.** Monge đặt bài toán, Kantorovich nới lỏng nó bằng quy hoạch tuyến tính, Brenier nối nó với hàm lồi, Caffarelli dựng nền móng đầu tiên cho lý thuyết chính quy, còn Ambrosio và Villani biến nó thành ngôn ngữ chung. Đóng góp mang tầm Fields của Figalli (đặc biệt cùng **Guido De Philippis**) nằm ở lõi giải tích khó nhất: chứng minh **tính chính quy Sobolev $$W^{2,1}$$**, **tính chính quy từng phần** (kiểm soát tập kỳ dị khi bỏ giả thiết lồi và điều kiện MTW), và **tính ổn định định lượng** — biến lý thuyết chính quy thành hạ tầng vững chắc cho bất đẳng thức hình học, khí tượng học và xác suất. Bài học này tiếp nối phần giới thiệu Monge–Kantorovich trong [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), đồng thời tách bạch huy chương 2018 của Figalli với huy chương 2010 của người thầy Villani trong [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/).

**Mạch bài học:** Bản đồ kiến thức nền (Monge–Kantorovich, Brenier, Monge–Ampère) → Ví dụ cầm tay chuyển 2 đống cát & thí nghiệm "xé rách đĩa tròn" → Khung giải thích chậm: từ Caffarelli đến $$W^{2,1}$$ và tính chính quy từng phần của De Philippis–Figalli → Ba ứng dụng lớn (tinh thể Wulff, khí quyển bán địa chuyển, ma trận ngẫu nhiên) → Phân biệt Figalli 2018 với Villani 2010.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Đặt lời trích dẫn năm 2018 cho Figalli vào lịch sử dài của vận chuyển tối ưu (Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani) mà không quy cả lĩnh vực về một người.
- Tự tay giải bài toán vận chuyển tối ưu rời rạc 2 đống cát và hiểu trực giác "đường xé" khi miền đích không lồi.
- Phát biểu định lý Brenier: với chi phí bình phương khoảng cách, ánh xạ tối ưu là gradient của một hàm thế lồi, thỏa phương trình **Monge–Ampère**.
- Trình bày ba bước nhảy của Figalli và De Philippis: chính quy Sobolev $$W^{2,1}$$, chính quy từng phần (trơn ngoài tập đóng độ đo không), và tính ổn định định lượng.
- Giải thích vì sao tính chính quy của ánh xạ là cầu nối sống còn cho bất đẳng thức đẳng chu không đẳng hướng (hình Wulff) và phương trình bán địa chuyển trong khí tượng học.
- Phân biệt rõ **Figalli 2018 (OT và ứng dụng)** với **Villani 2010 (tắt dần Landau / phương trình Boltzmann)**.

**Kiến thức cần có.** Bài toán Monge và Kantorovich cùng khái niệm đẩy tiến độ đo (push-forward) $$T_\#\mu=\nu$$, như trong bài OT ở Chương 6; hàm lồi và ma trận Hessian; biết rằng một PDE elliptic phi tuyến hoàn toàn (fully nonlinear) có thể có lý thuyết chính quy. Không cần học trước về phương trình Monge–Ampère.

**Liên hệ với khóa học.** Đọc cùng bài [Caffarelli: biên tự do và Monge–Ampère]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) để thấy truyền thống nghiên cứu tính chính quy (được trao Giải Abel) mà Figalli kế thừa. Bài [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) chỉ là *một* câu chuyện Fields khác về PDE (giới hạn động học, không phải ánh xạ vận chuyển).

---

## Bản đồ kiến thức nền: Vận chuyển tối ưu và Phương trình Monge–Ampère nghiên cứu gì?

### 1. Bài toán Monge (1781) và sự nới lỏng của Kantorovich (1942)
Cho phân bố khối lượng nguồn $$\mu$$ (ví dụ đất cần xúc), phân bố đích $$\nu$$ (hố cần lấp) và hàm chi phí $$c(x,y)$$ để chuyển 1 đơn vị khối lượng từ $$x$$ sang $$y$$.
- **Monge** tìm một **ánh xạ** $$T$$ sao cho toàn bộ khối lượng ở $$x$$ đi trọn sang $$y = T(x)$$ (ký hiệu đẩy tiến độ đo $$T_\#\mu = \nu$$) với tổng chi phí $$\int c(x, T(x))\,d\mu(x)$$ nhỏ nhất.
- **Kantorovich** cho phép *chia nhỏ* khối lượng ở $$x$$ gửi đến nhiều đích khác nhau qua một **kế hoạch vận chuyển** (phép ghép) $$\pi(x,y)$$. Bài toán lập tức trở thành quy hoạch tuyến tính trên tập lồi compact, nên nghiệm tối ưu luôn tồn tại.

### 2. Định lý Brenier (1987–1991) và phương trình Monge–Ampère
Khi chi phí là bình phương khoảng cách $$c(x,y) = \|x - y\|^2$$ và $$\mu = f\,dx, \nu = g\,dy$$ là hai mật độ liên tục, **Yann Brenier** chứng minh nghiệm tối ưu luôn là một ánh xạ Monge duy nhất có dạng gradient của một **hàm lồi** $$\phi$$:

$$
T(x) = \nabla\phi(x).
$$

Theo công thức đổi biến tích phân bội, bảo toàn khối lượng $$\int_A f(x)\,dx = \int_{T(A)} g(y)\,dy$$ dẫn thẳng tới **phương trình Monge–Ampère**:

$$
f(x) = g\bigl(\nabla\phi(x)\bigr)\,\det D^2\phi(x).
$$

Đây là một PDE elliptic **phi tuyến hoàn toàn**: ẩn hàm nằm trong *định thức* của ma trận đạo hàm cấp hai $$D^2\phi$$ (tích các trị riêng của Hessian).

### 3. Lý thuyết chính quy (Regularity Theory) đặt câu hỏi gì?
Một hàm lồi $$\phi$$ luôn khả vi hầu khắp nơi, nhưng đạo hàm $$T = \nabla\phi$$ của nó có thể có bước nhảy hoặc nếp gấp. Lý thuyết chính quy hỏi: *nếu mật độ $$f, g$$ trơn mượt, thì ánh xạ $$T = \nabla\phi$$ có trơn mượt không? Nếu buộc phải có điểm gãy (tập kỳ dị), tập đó nhỏ đến mức nào?*

---

## 1. Ví dụ cầm tay chỉ việc: bài toán chuyển 2 đống cát và thí nghiệm "xé rách đĩa tròn"

### Ví dụ 1 (Rời rạc 1D): Chuyển 2 đống cát — tại sao ánh xạ tối ưu luôn "đơn điệu" (gradient hàm lồi)?
Giả sử trên trục số ta có **2 đống cát** nặng bằng nhau (mỗi đống 1 tấn) đặt tại $$x_1 = 0$$ và $$x_2 = 1$$, cần chuyển sang **2 hố** đặt tại $$y_1 = 0$$ và $$y_2 = 3$$, với chi phí bình phương khoảng cách $$c(x,y) = (x - y)^2$$. Có hai phương án ánh xạ:
- **Phương án 1 (không cắt chéo):** chuyển $$0 \to 0$$ và $$1 \to 3$$. Tổng chi phí:
  $$
  C_1 = (0 - 0)^2 + (1 - 3)^2 = 0 + 4 = 4.
  $$
- **Phương án 2 (cắt chéo nhau):** chuyển $$0 \to 3$$ và $$1 \to 0$$. Tổng chi phí:
  $$
  C_2 = (0 - 3)^2 + (1 - 0)^2 = 9 + 1 = 10 > 4!
  $$

Nhìn ngay ra quy luật: muốn tổng bình phương khoảng cách nhỏ nhất, các tia vận chuyển **không bao giờ cắt chéo nhau** — điểm bên trái ($$x_1 < x_2$$) phải đi sang đích bên trái ($$T(x_1) \le T(x_2)$$). Mà trong giải tích 1 chiều, một hàm đơn điệu tăng $$T$$ chính là **đạo hàm của một hàm lồi** $$\phi$$ ($$T = \phi'$$)! Ở chiều $$n$$, điều kiện "không cắt chéo" tổng quát hóa đúng thành định lý Brenier $$T = \nabla\phi$$ với $$\phi$$ lồi!

### Ví dụ 2 (Hình học 2D): Xé rách một đĩa tròn — vì sao tính lồi của miền đích quyết định tính trơn?
Bây giờ hãy hình dung trong mặt phẳng $$\mathbb{R}^2$$:
- Nguồn $$\mu$$ là một **đĩa tròn** đồng nhất tâm gốc tọa độ $$B(0, 1)$$ (mật độ trơn, miền lồi).
- Đích $$\nu$$ là **hai nửa đĩa tròn tách rời nhau**: nửa đĩa trái dịch sang trái một đoạn (tâm $$(-2, 0)$$) và nửa đĩa phải dịch sang phải một đoạn (tâm $$(+2, 0)$$). Miền đích này **không lồi**!

Để tối thiểu hóa tổng công, ánh xạ tối ưu $$T = \nabla\phi$$ buộc phải **cắt đôi đĩa tròn nguồn dọc theo đường kính thẳng đứng $$x_1 = 0$$**: mọi hạt cát có $$x_1 < 0$$ bay sang nửa đĩa trái ($$T(x) = x - (2,0)$$), còn mọi hạt cát có $$x_1 > 0$$ bay sang nửa đĩa phải ($$T(x) = x + (2,0)$$). Hàm thế lồi tương ứng là $$\phi(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2) + 2\vert x_1 \vert$$ — **có nếp gấp sắc dọc trục $$x_1 = 0$$**! Hai hạt cát ban đầu sát rạt hai bên đường kính bị xé cách xa nhau tới 4 đơn vị!

Thí nghiệm đơn giản ấy hé lộ toàn bộ bài toán của Caffarelli và Figalli:
- **Caffarelli (đầu thập niên 1990)** chứng minh: nếu miền đích **lồi** và các mật độ bị chặn dương trơn, sẽ không bao giờ có vết xé nào — $$\phi$$ trơn $$C^\infty$$ bên trong miền!
- **Figalli & De Philippis** đặt câu hỏi thực tế hơn: khi miền đích **không lồi** (như hai nửa đĩa trên), hoặc khi chi phí không còn là $$\|x-y\|^2$$, ta không thể tránh được "vết xé" (tập kỳ dị $$\Sigma$$). Nhưng liệu tập kỳ dị $$\Sigma$$ đó có *luôn* mỏng như đường kính $$x_1 = 0$$ (có diện tích/độ đo bằng $$0$$) hay nó có thể phình thành một đám mây fractal có diện tích dương?

---

## 2. Khung giải thích: từ Caffarelli đến $$W^{2,1}$$ và tính chính quy từng phần của De Philippis–Figalli (nên đọc chậm)

Figalli học tiến sĩ với **Luigi Ambrosio** (Pisa) và **Cédric Villani** (ENS Lyon), bảo vệ năm 2007 và công tác tại ETH Zürich từ 2016. Những đột phá mang tầm Fields của ông cùng **Guido De Philippis** (và Kim, Loeper...) giải mã bài toán Monge–Ampère qua 4 bước mạch lạc:

#### Bước 1: Vấn đề ẩn của phương trình Monge–Ampère — định thức suy biến
Trong phương trình Laplace $$\Delta\phi = \lambda_1 + \lambda_2 = 1$$, hai trị riêng của Hessian bị kìm giữ cùng nhau. Nhưng trong phương trình Monge–Ampère $$\det D^2\phi = \lambda_1 \lambda_2 = 1$$, một trị riêng có thể thu nhỏ về $$\varepsilon$$ trong khi trị riêng kia phình ra $$1/\varepsilon$$! Về hình học, các mặt mức của $$\phi$$ bị kéo dẹt thành những hình elip siêu dài (mất tính tròn đều). Chính sự suy biến này ngăn cản lý thuyết Calderón–Zygmund cổ điển áp dụng trực tiếp.

#### Bước 2: Đột phá Sobolev $$W^{2,1}$$ (De Philippis–Figalli, *Inventiones*, 2013)
Với nghiệm Alexandrov lồi của $$\det D^2\phi = f$$ ($$0 < c \le f \le C$$), ban đầu người ta chỉ biết ma trận Hessian $$D^2\phi$$ là một độ đo Radon (có thể chứa phần kỳ dị kiểu hàm delta). Bằng cách kết hợp **tính bất biến afin** của phương trình Monge–Ampère (dùng phép biến đổi tuyến tính để kéo tròn lại từng lát cắt bị dẹt) với các ước lượng độ đo hình học sắc bén, De Philippis và Figalli chứng minh phần kỳ dị không tồn tại: $$D^2\phi$$ là một hàm khả tích địa phương thực sự ($$\phi \in W^{2,1}_{\mathrm{loc}}$$, thậm chí $$D^2\phi \in L\log^k L$$)! Đây là ngưỡng sống còn giúp lấy đạo hàm $$T = \nabla\phi$$ theo nghĩa hàm thông thường và cho tính ổn định mạnh cấp hai.

#### Bước 3: Tính chính quy từng phần — kiểm soát tập kỳ dị (De Philippis–Figalli, *IHÉS*, 2015)
Khi bỏ điều kiện miền đích lồi và bỏ cả điều kiện cấu trúc Ma–Trudinger–Wang (MTW) cho chi phí tổng quát $$c(x,y)$$ (hoặc $$c = d^2/2$$ trên đa tạp Riemann bất kỳ), ánh xạ tối ưu chắc chắn có điểm kỳ dị. Trong *Partial regularity for optimal transport maps* (2015), De Philippis và Figalli chứng minh rằng ánh xạ tối ưu giữa hai mật độ trơn **luôn trơn $$C^\infty$$ bên ngoài một tập kỳ dị đóng $$\Sigma$$ có độ đo bằng không**! Nói cách khác, ánh xạ vận chuyển tối ưu là một phép vi phôi trơn trên một tập mở chiếm trọn 100% thể tích, chỉ trừ một tập "đường xé" mỏng có thể tích bằng $$0$$.

#### Bước 4: Biến tính chính quy thành tính ổn định định lượng
Một khi ánh xạ vận chuyển tối ưu được kiểm soát tốt về đạo hàm và tập kỳ dị, nó trở thành một "thước đo hình học": nếu một hình thể gần đạt cực tiểu cho một bất đẳng thức (như chu vi), ta dùng ánh xạ vận chuyển đẩy nó về hình chuẩn tối ưu; độ lệch về phiếm hàm biến thành độ lệch của $$D^2\phi$$ khỏi ma trận đơn vị, từ đó khóa chặt khoảng cách hình học thực sự giữa hai hình!

Tóm tắt hành trình giải tích của Figalli:

$$
\text{Vận chuyển } T = \nabla\phi
\;\longleftrightarrow\;
\det D^2\phi = f/g(\nabla\phi)
\;\longleftrightarrow\;
W^{2,1} \text{ \& Trơn ngoài } \Sigma\ (|\Sigma|=0)
\;\Longrightarrow\;
\text{Ổn định hình học \& PDE khí quyển}.
$$

*(Lưu ý: các công trình nổi tiếng sau này của Figalli cùng Serra và Ros-Oton về bài toán vật cản và bài toán Stefan thuộc nhánh biên tự do lân cận, bổ sung cho sự nghiệp ông chứ không phải nội dung chính của lời trích dẫn năm 2018.)*

---

## 3. Ba ứng dụng lớn: bất đẳng thức tinh thể, khí quyển và xác suất

1. **Bất đẳng thức đẳng chu không đẳng hướng định lượng (Hình Wulff).** Trong vật lý chất rắn, năng lượng bề mặt tinh thể phụ thuộc vào hướng mặt phẳng, nên hình cân bằng cực tiểu hóa chu vi không đẳng hướng là **hình Wulff** chứ không phải hình cầu. **Figalli–Maggi–Pratelli** (*Inventiones*, 2010) dùng ánh xạ Brenier để chứng minh dạng định lượng sắc: nếu chu vi không đẳng hướng của tập $$E$$ chỉ vượt chu vi hình Wulff một lượng nhỏ $$\delta$$, thì thể tích phần sai khác giữa $$E$$ và một phép tịnh tiến của hình Wulff bị chặn bởi $$C\sqrt{\delta}$$ (số mũ $$1/2$$ tối ưu).
2. **Phương trình bán địa chuyển (Semigeostrophic) trong khí tượng học.** Hệ bán địa chuyển mô tả sự hình thành các front thời tiết quy mô lớn. Trong tọa độ địa chuyển (Cullen–Purser; Benamou–Brenier), hàm thế áp suất là hàm lồi mà gradient của nó là ánh xạ vận chuyển tối ưu giữa không gian vật lý và không gian địa chuyển. Nhờ định lý chính quy $$W^{2,1}$$ mới cho Monge–Ampère, **Ambrosio–Colombo–De Philippis–Figalli** chứng minh sự tồn tại nghiệm yếu Euler toàn cục trên xuyến 2D và miền lồi 3D — ở đây $$W^{2,1}$$ chính là điều kiện để trường vận tốc vật lý xác định được!
3. **Bất đẳng thức hàm và xác suất.** Cùng **Eric Carlen**, Figalli chứng minh tính ổn định định lượng cho bất đẳng thức Gagliardo–Nirenberg và log-HLS (mô hình tụ tập sinh học Keller–Segel). Cùng **Alice Guionnet**, ông dùng ánh xạ vận chuyển xấp xỉ để chứng minh tính phổ quát trong mô hình nhiều ma trận ngẫu nhiên.

---

## 4. Hai Huy chương Fields, hai trọng tâm khác nhau

Vì Figalli là học trò của Villani, hai huy chương rất hay bị gộp chung. Bảng dưới phân tách rạch ròi:

| Huy chương | Trọng tâm của lời trích dẫn | Ngôn ngữ chung | Kết quả riêng |
|------------|-------------------|---------------|------------------|
| Villani, 2010 | Tắt dần Landau phi tuyến; hội tụ về cân bằng cho phương trình Boltzmann | Entropy, bất đẳng thức, OT như bộ công cụ mà Villani cũng phát triển | Các định lý về hồi phục trong phương trình động học |
| Figalli, 2018 | Lý thuyết OT và ứng dụng vào PDE, hình học metric, xác suất | Monge–Ampère, ánh xạ, tính ổn định | Tính chính quy và tính ổn định của phép vận chuyển, cùng các hệ quả hình học |

Đọc thêm bài [Villani / Landau–Boltzmann]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/) để thấy rõ mảng phương trình động học của năm 2010.

---

## 5. Vì sao ông nhận Huy chương Fields

Có ba lý do rõ ràng, không cần gọi vận chuyển tối ưu là "lý thuyết của riêng Figalli":
1. **Độ khó giải tích ở biên giới.** Chứng minh $$W^{2,1}$$ và tính chính quy từng phần cho PDE phi tuyến hoàn toàn Monge–Ampère nằm ngay sát giới hạn của giải tích lồi và lý thuyết độ đo hình học.
2. **Hạ tầng cho nhiều ngành khác.** Ngay khi biết ánh xạ thuộc $$W^{2,1}$$ hoặc trơn ngoài tập độ đo không, hàng loạt bài toán ở hình học tinh thể, khí tượng học và ma trận ngẫu nhiên được khai thông.
3. **Hoàn thiện bức tranh sau Caffarelli.** Caffarelli giải mã trường hợp lý tưởng (Euclid, miền lồi, chi phí bình phương); Figalli–De Philippis cho thấy chính xác điều gì còn đúng khi rời khỏi thế giới lý tưởng đó.

---

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Figalli phát minh ra vận chuyển tối ưu." | Monge, Kantorovich, Brenier, Caffarelli, Ambrosio, Villani và những người khác xây dựng lĩnh vực này; huy chương của Figalli là cho tính chính quy và các ứng dụng. |
| "Fields 2018 giống Fields 2010 của Villani." | Villani 2010 là về tắt dần Landau và phương trình Boltzmann; Figalli 2018 là về OT và các ứng dụng của nó. |
| "Ánh xạ Brenier luôn trơn." | Hàm thế lồi cho ánh xạ xác định hầu khắp nơi; tính trơn phụ thuộc vào mật độ, tính lồi, hàm chi phí, và thường chỉ đúng bên ngoài một tập kỳ dị. |
| "Lý thuyết của Caffarelli đã lỗi thời." | Đó là nền tảng; các công trình sau hỏi điều gì còn đúng khi bỏ các giả thiết hình học của ông. |
| "Chính quy từng phần nghĩa là ánh xạ thuộc $$C^\infty$$ ở mọi nơi." | Nghĩa là trơn bên ngoài một tập đóng có độ đo không; tập kỳ dị có thể khác rỗng. |
| "Tính chính quy trong OT chỉ có giá trị thẩm mỹ." | Tính đặt đúng của mô hình SG và bất đẳng thức đẳng chu định lượng đều dùng các ước lượng này làm giả thiết. |

---

## Liên kết

- IMU Fields Medals 2018: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2018)
- Wikipedia, Alessio Figalli: [https://en.wikipedia.org/wiki/Alessio_Figalli](https://en.wikipedia.org/wiki/Alessio_Figalli)
- Trang ETH (về tính chính quy của ánh xạ tối ưu): [https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps](https://people.math.ethz.ch/~afigalli/Regularity-of-optimal-maps)
- Bài giới thiệu của Quanta (2018): [https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/](https://www.quantamagazine.org/a-traveler-who-finds-stability-in-the-natural-world-20180801/)
- Tìm trên arXiv, Figalli Monge–Ampère: [https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all](https://arxiv.org/search/?query=Figalli+Monge-Ampere&searchtype=all)
- De Philippis–Figalli, tính chính quy $$W^{2,1}$$ (arXiv:1111.7207): [https://arxiv.org/abs/1111.7207](https://arxiv.org/abs/1111.7207)
- De Philippis–Figalli, tính chính quy từng phần (arXiv:1209.5640): [https://arxiv.org/abs/1209.5640](https://arxiv.org/abs/1209.5640)

---

## Tài liệu tham khảo

1. Lời trích dẫn Huy chương Fields 2018 của IMU cho Alessio Figalli.
2. Y. Brenier, “Polar factorization and monotone rearrangement of vector-valued functions,” *Comm. Pure Appl. Math.* 44 (1991).
3. L. A. Caffarelli, các bài báo về tính chính quy của phương trình Monge–Ampère và ánh xạ OT (đầu thập niên 1990); lời trích dẫn Giải Abel 2023.
4. G. De Philippis và A. Figalli, “$$W^{2,1}$$ regularity for solutions of the Monge–Ampère equation,” *Invent. Math.* 192 (2013); “Partial regularity for optimal transport maps,” *Publ. Math. IHÉS* 121 (2015); survey trong *Bull. Amer. Math. Soc.* 51 (2014).
5. A. Figalli, F. Maggi và A. Pratelli, “A mass transportation approach to quantitative isoperimetric inequalities,” *Invent. Math.* 182 (2010).
6. L. Ambrosio, M. Colombo, G. De Philippis và A. Figalli, các kết quả về tính đặt đúng của nghiệm Euler cho phương trình bán địa chuyển (trường hợp hai chiều tuần hoàn và ba chiều lồi).
7. A. Figalli, *The Monge–Ampère Equation and Its Applications*, EMS (2017).
8. C. Villani, *Topics in Optimal Transportation*; *Optimal Transport: Old and New*. Đây là tài liệu nền, không phải nội dung của huy chương năm 2010.
9. Trong khóa học: [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/), [Villani]({{ site.baseurl }}/contents/vi/chapter02/02_29_Villani_Landau_Boltzmann/).

---

## Hướng đi tiếp

- Đọc ước lượng bên trong của Caffarelli song song với kết quả chính quy từng phần của De Philippis–Figalli: những giả thiết hình học nào chuyển từ "phải giả sử" sang "không cần cho tính trơn hầu khắp nơi"?
- So sánh OT tính toán (thuật toán Sinkhorn, Chương 6) với lý thuyết giải tích: tính toán số dùng phép chính quy hóa, còn lý thuyết chính quy giải thích khi nào ánh xạ chưa chính quy hóa đã gần như trơn.

## Video tham khảo

- **Xem trước** — [Alessio Figalli (2018 Fields Medal) explains Optimal Transport](https://www.youtube.com/watch?v=jyL6ZECM7oM) — Tom Rocks Maths, tiếng Anh. Figalli tự giải thích vận chuyển tối ưu cho khán giả rộng. Nên xem trước khi đọc bài.
- [Alessio Figalli at GYSS 2022 – Recent Developments in Optimal Transport Theory](https://www.youtube.com/watch?v=pu_WHpRDmKE) — National Research Foundation Singapore, tiếng Anh. Bài giảng về các phát triển gần đây của lý thuyết vận chuyển tối ưu, liên quan đến mục 4–5. Nên xem sau khi đọc bài.
