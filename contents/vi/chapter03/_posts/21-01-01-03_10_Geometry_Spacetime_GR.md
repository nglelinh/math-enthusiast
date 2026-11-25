---
layout: post
title: "Từ hình học không–thời gian đến hấp dẫn"
chapter: '03'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
---

Ngay lúc này, ở độ cao hơn 20.000 km phía trên đầu bạn, hàng chục vệ tinh GPS đang bay quanh Trái Đất với vận tốc khoảng 14.000 km/giờ. Mỗi vệ tinh mang theo một đồng hồ nguyên tử siêu chính xác để phát tín hiệu định vị xuống điện thoại của bạn. Một sự thật ít người ngờ tới: nếu các kỹ sư không lập trình **phương trình không–thời gian cong của Einstein** vào hệ thống GPS, đồng hồ trên vệ tinh sẽ chạy nhanh hơn đồng hồ dưới mặt đất khoảng 38 micro-giây mỗi ngày — và chỉ sau 24 giờ, bản đồ trên điện thoại bạn sẽ định vị **sai lệch tới hơn 11 kilômét**!

Trước năm 1915, Isaac Newton xem hấp dẫn là một "lực kéo vô hình" truyền tức thời xuyên qua không gian phẳng tuyệt đối. **Thuyết tương đối rộng (GR)** của Albert Einstein đã đảo lộn hoàn toàn bức tranh đó bằng một cú nhảy hình học táo bạo: không có "sợi dây vô hình" nào kéo Trái Đất quanh Mặt Trời cả. Vật chất và năng lượng làm **cong chính tấm vải không–thời gian**, còn hành tinh, quả táo rơi hay tia sáng chỉ đơn giản đang đi theo con đường "thẳng nhất có thể" (**đường trắc địa**) trong hình học cong ấy.

Bài học này vẽ một tấm bản đồ trực giác ở bậc đại học cho cơ chế kỳ diệu đó: từ không–thời gian phẳng Minkowski, nguyên lý tương đương, metric và độ cong, đến phương trình Einstein và các kiểm chứng quan sát. Bài cũng chuẩn bị trực giác hình học sẽ được dùng lại trong [lý thuyết gauge]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/): **vật lý là các trường sống trên một nền hình học**, và độ cong chính là biểu hiện của tương tác.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu ý chính của **nguyên lý tương đương** và giải thích vì sao nó dẫn đến việc thay lực hấp dẫn bằng hình học của chuyển động rơi tự do.
- Giải thích metric $$g_{\mu\nu}$$ chứa những thông tin gì (khoảng cách, góc, cấu trúc nhân quả; ở mức ý tưởng).
- Phân biệt **thuyết tương đối hẹp** (không–thời gian Minkowski phẳng) và **thuyết tương đối rộng** (không–thời gian cong và thay đổi theo vật chất).
- Viết phương trình Einstein dạng sơ lược $$\mathrm{Ric}-\tfrac12 Rg=8\pi T$$ và nói mỗi vế biểu diễn điều gì.
- Trình bày **chuỗi lập luận ngắn** từ hình học đến một dự đoán (ánh sáng bị lệch, giãn thời gian do hấp dẫn) mà không cần tính toán tensor đầy đủ.
- Tránh các cách nói sai: "mọi thứ đều tương đối", "GR chỉ là chuyện viễn tưởng về lỗ đen", "không gian cong nghĩa là một bề mặt nằm trong không gian lớn hơn mà ta luôn nhìn thấy được".

**Kiến thức nền.** Giải tích nhiều biến; đại số tuyến tính (tích vô hướng). Tùy chọn: [Giải tích → Vật lý]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/).

---

## Kiến thức cần nhớ: Hình học vi phân và hình học Riemann là gì, nghiên cứu những gì?

Ở phổ thông, hình học Euclid diễn ra trên mặt giấy phẳng: tổng ba góc tam giác luôn bằng $$180^\circ$$ và hai đường thẳng song song không bao giờ cắt nhau. Nhưng mặt Trái Đất là hình cầu — nếu hai máy bay cùng xuất phát từ Xích Đạo bay thẳng về hướng Bắc (ban đầu song song nhau), chúng vẫn sẽ đâm sầm vào nhau tại Bắc Cực, và tổng ba góc một tam giác lớn trên địa cầu luôn **lớn hơn $$180^\circ$$**!

Vào thế kỷ XIX, Carl Friedrich Gauss và học trò Bernhard Riemann đã xây dựng **hình học vi phân (differential geometry)** và **hình học Riemann** để nghiên cứu những không gian cong tổng quát ở mọi số chiều thông qua ba ý tưởng cốt lõi:

1. **Đa tạp (Manifold):** một không gian mà nếu phóng to cực sát quanh bất kỳ điểm nào thì trông nó phẳng như $$\mathbb{R}^n$$ (giống mặt Trái Đất nhìn từ sân nhà bạn), nhưng ghép toàn cục lại thì có thể cong và khép kín.
2. **Tensor Metric $$g_{\mu\nu}$$:** một "cây thước đo cục bộ" đặt tại mỗi điểm, cho phép tính độ dài cung đường, góc giữa hai hướng và diện tích mà không cần hệ tọa độ vuông góc toàn cục.
3. **Độ cong nội tại (Intrinsic Curvature):** định lý tuyệt vời của Gauss (*Theorema Egregium*) chứng minh rằng một chú kiến sống trên mặt cầu hoàn toàn có thể **tự đo được độ cong của vũ trụ mình** (bằng cách đo tổng ba góc tam giác hoặc chu vi hình tròn so với $$2\pi r$$) mà **không hề cần bước ra không gian 3 chiều bên ngoài để nhìn vào**.

Khi Einstein đi tìm ngôn ngữ toán học cho thuyết tương đối rộng vào đầu thập niên 1910, toàn bộ bộ máy hình học Riemann đã nằm sẵn trên giá sách — chỉ cần đổi một dấu trừ cho chiều thời gian (hình học Lorentz)!

---

## 1. Thuyết tương đối hẹp là hình học phẳng

**Không–thời gian Minkowski** là $$\mathbb{R}^4$$ trang bị một "tích vô hướng" có dấu hỗn hợp (quy ước dấu có thể khác nhau giữa các giáo trình):

$$
ds^2 = -c^2\,dt^2 + dx^2 + dy^2 + dz^2.
$$

Chính dấu trừ trước $$c^2\,dt^2$$ tạo ra toàn bộ vật lý kỳ diệu của thuyết tương đối hẹp:
- Với tia sáng di chuyển với tốc độ $$c$$, ta có $$ds^2 = 0$$ (**nón ánh sáng** chia quá khứ – tương lai nhân quả khỏi những sự kiện không thể tác động tới nhau).
- Phép biến đổi Lorentz chính là các phép "quay hyperbolic" bảo toàn khoảng $$ds^2$$.

Ở đây **chưa có hấp dẫn**: không–thời gian Minkowski giống như một sân khấu cứng, phẳng và cố định vĩnh viễn.

**Hiểu đúng.** "Tương đối" không có nghĩa là "mọi thứ đều tùy quan điểm". Ngược lại, nó khẳng định các định luật vật lý và những đại lượng hình học bất biến (tốc độ ánh sáng $$c$$, khoảng $$ds^2$$, cấu trúc nhân quả) là **tuyệt đối giống nhau** dưới nhóm đối xứng Lorentz.

---

## 2. Từ nguyên lý tương đương đến không–thời gian cong

Năm 1907, Einstein có cái ông gọi là "ý nghĩ hạnh phúc nhất đời mình": nếu một người rơi tự do trong thang máy đứt cáp, anh ta sẽ không cảm thấy trọng lượng của chính mình — quả táo buông tay ra sẽ lơ lửng ngay trước mặt anh ta hệt như đang trôi ngoài vũ trụ không trọng lực!

Từ **nguyên lý tương đương** đó, Einstein rút ra bước ngoặt: *tại một vùng đủ nhỏ, ta không thể phân biệt rơi tự do trong trường hấp dẫn với việc trôi lơ lửng trong không gian phẳng.* Vậy thì dấu vết thật sự, không thể xóa nhòa của hấp dẫn nằm ở đâu?

**Trực giác về lực thủy triều = Độ cong.** Hãy thả hai quả táo cách nhau 1 mét rơi tự do về phía Trái Đất. Vì cả hai đều hướng về **tâm Trái Đất**, quỹ đạo của chúng không song song mãi mà sẽ **xích lại gần nhau dần** (tương tự hai người đi thẳng từ Xích Đạo về Bắc Cực!). Hiện tượng các quỹ đạo rơi tự do lân cận tự kéo sát vào nhau hoặc tách xa nhau đó gọi là **lực thủy triều** — và trong ngôn ngữ hình học, đó chính là định nghĩa của **độ cong không–thời gian**!

---

## 3. Metric, đường trắc địa, độ cong (các định nghĩa cơ bản)

**Metric Lorentz** $$g_{\mu\nu}(x)$$ gán cho mỗi sự kiện $$x$$ một ma trận đối xứng $$4\times 4$$ với dấu $$(-,+,+,+)$$, đóng vai trò bộ thước đo độ dài và thời gian tại điểm đó. Thời gian riêng (thời gian đo bằng đồng hồ đeo tay của một phi hành gia) dọc theo đường thế giới $$\gamma$$ là:

$$
\tau = \int \sqrt{-g(\dot\gamma,\dot\gamma)}\,dt
$$

(sai khác hằng số $$c$$ và cách tham số hóa). **Đường trắc địa (geodesic)** là đường làm cực trị thời gian riêng (tương đương: đường "không bẻ lái", thỏa mãn phương trình trắc địa với các ký hiệu Christoffel tính từ $$g$$ và đạo hàm $$\partial g$$).

**Các tensor độ cong** (tensor Riemann $$R^\rho{}_{\sigma\mu\nu}$$, tensor Ricci $$R_{\mu\nu}$$, độ cong vô hướng $$R$$) đo mức độ không giao hoán khi dời song song một vectơ quanh một vòng khép kín và mức độ thể tích của một đám mây hạt rơi tự do bị co bóp. Không cần thuộc lòng công thức chỉ số; chỉ cần khắc cốt câu tổng kết nổi tiếng của nhà vật lý John Wheeler:

> **Vật chất cho không–thời gian biết phải cong như thế nào; không–thời gian cong cho vật chất biết phải chuyển động như thế nào.**

### Giải thích: Từ nguyên lý tương đương đến quỹ đạo hành tinh và GPS

1. **Nguyên lý tương đương xóa bỏ "lực hấp dẫn" cục bộ:** trong một khung rơi tự do đủ nhỏ, mọi vật chuyển động thẳng đều như trong không–thời gian phẳng Minkowski.
2. **Lực thủy triều buộc không–thời gian phải cong toàn cục:** khi ghép nhiều khung rơi tự do ở các vị trí khác nhau quanh Trái Đất lại, chúng không thể khớp thành một mặt phẳng duy nhất → ta cần một **metric cong** $$g_{\mu\nu}(x)$$.
3. **Phương trình Einstein xác định metric từ vật chất:** mật độ năng lượng – xung lượng $$T_{\mu\nu}$$ quyết định độ cong thông qua hệ PDE $$G_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}$$ (ví dụ nghiệm cầu Schwarzschild quanh Trái Đất).
4. **Đọc trực tiếp tiên đoán vật lý từ metric:** đường đi của hành tinh và tia sáng là đường trắc địa của $$g_{\mu\nu}$$, còn nhịp chạy của đồng hồ GPS đọc thẳng từ thành phần $$g_{00}$$ của metric!

**Kiểm tra nhanh.** "Không–thời gian cong" không có nghĩa là Trái Đất nằm trên một tấm bạt cao su võng xuống một chiều không gian bí ẩn nào khác; độ cong là tính chất **nội tại** mã hóa ngay trong thước đo $$g_{\mu\nu}$$.

---

## 4. Phương trình Einstein là một phương trình trường

Dạng gọn của **phương trình trường Einstein**:

$$
G_{\mu\nu} := R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu},
$$

trong đó $$G_{\mu\nu}$$ là tensor Einstein xây dựng hoàn toàn từ metric và các đạo hàm bậc hai của nó, còn $$T_{\mu\nu}$$ là **tensor năng lượng – xung lượng** mô tả mật độ khối lượng, năng lượng, áp suất và dòng động lượng của vật chất.

| Vế | Ý nghĩa |
|----|---------|
| Trái ($$G_{\mu\nu}$$) | Hoàn toàn là **hình học** (độ cong không–thời gian) |
| Phải ($$T_{\mu\nu}$$) | **Vật chất & năng lượng** (nguồn gây cong) |

Vì hệ số $$\frac{8\pi G}{c^4} \approx 2 \times 10^{-43}\text{ s}^2/(\text{kg}\cdot\text{m})$$ vô cùng nhỏ, không–thời gian thực chất **cực kỳ cứng**: phải cần khối lượng cỡ cả một ngôi sao mới bẻ cong nó đáng kể! Trong chân không ($$T_{\mu\nu}=0$$), phương trình rút về $$R_{\mu\nu}=0$$ — các nghiệm nổi tiếng như lỗ đen **Schwarzschild** (không quay) và **Kerr** (đang quay) đều nằm ở đây.

**Dưới góc nhìn PDE.** Khai triển ra thành phần, phương trình Einstein là một hệ gồm 10 phương trình đạo hàm riêng phi tuyến bậc hai cho ẩn số là 10 thành phần của metric $$g_{\mu\nu}(x)$$. Tính đặt chỉnh của bài toán giá trị ban đầu (Cauchy), tính ổn định phi tuyến của lỗ đen Kerr và giả thuyết kiểm duyệt vũ trụ là những mũi nhọn rực rỡ của giải tích hình học hiện đại.

---

## 5. Từ hình học đến quan sát, mỗi hiện tượng một bước

### Ví dụ làm từng bước: Tự tính độ lệch đồng hồ GPS trực tiếp từ Metric Schwarzschild

Nghiệm chân không đối xứng cầu của phương trình Einstein bên ngoài Trái Đất (khối lượng $$M_\oplus \approx 6\times 10^{24}\text{ kg}$$) là **metric Schwarzschild**:

$$
ds^2 = -\left(1 - \frac{r_s}{r}\right)c^2\,dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1}dr^2 + r^2\bigl(d\theta^2 + \sin^2\theta\,d\phi^2\bigr),
$$

trong đó $$r_s = \frac{2GM}{c^2}$$ là bán kính Schwarzschild. Hãy tính tay đúng ba bước:

1. **Tính bán kính Schwarzschild của Trái Đất:**
$$
r_s = \frac{2 \times (6{,}67\times 10^{-11}) \times (6\times 10^{24})}{(3\times 10^8)^2} \approx 0{,}0089\text{ m} \approx 9\text{ mm}
$$
(nếu ép toàn bộ Trái Đất nhỏ bằng một viên bi đường kính 1,8 cm, nó sẽ trở thành lỗ đen!).
2. **Đọc nhịp đồng hồ tại độ cao $$r$$:** với đồng hồ đứng yên ($$dr=d\theta=d\phi=0$$), thành phần thời gian của metric cho:
$$
d\tau = \sqrt{1 - \frac{r_s}{r}}\,dt \approx \left(1 - \frac{r_s}{2r}\right)dt.
$$
3. **So sánh mặt đất với vệ tinh GPS:**
   - Tại mặt đất ($$r_\oplus \approx 6{.}371\text{ km}$$): $$\frac{r_s}{2r_\oplus} \approx \frac{0{,}0089}{1{,}274\times 10^7} \approx 7{,}0 \times 10^{-10}$$.
   - Tại quỹ đạo GPS ($$r_{\text{GPS}} \approx 26{.}571\text{ km}$$): $$\frac{r_s}{2r_{\text{GPS}}} \approx \frac{0{,}0089}{5{,}314\times 10^7} \approx 1{,}7 \times 10^{-10}$$.
   - Chênh lệch nhịp đồng hồ do độ cong hấp dẫn là $$(7{,}0 - 1{,}7)\times 10^{-10} = 5{,}3\times 10^{-10}$$. Nhân với $$86{.}400\text{ giây/ngày}$$ ta thu ngay:
$$
\Delta t_{\text{GR}} \approx 5{,}3\times 10^{-10} \times 86{.}400 \approx +45{,}8\text{ }\mu\text{s/ngày}!
$$
Trừ đi hiệu ứng chạy chậm $$-7\text{ }\mu\text{s/ngày}$$ do tốc độ bay ~14.000 km/h của thuyết tương đối hẹp, đồng hồ GPS chạy nhanh hơn mặt đất **$$+38\text{ }\mu\text{s/ngày}$$**. Nhân với tốc độ ánh sáng $$c \approx 300\text{ m}/\mu\text{s}$$, nếu không hiệu chỉnh GR, bản đồ sẽ trôi **$$38 \times 300 \approx 11{,}4\text{ km}$$ mỗi ngày**!

- **Ánh sáng bị lệch & Thấu kính hấp dẫn:** tia sáng đi theo đường trắc địa không ($$ds^2=0$$) nên tự uốn cong khi lướt qua gần Mặt Trời hay một cụm thiên hà — được Eddington xác nhận năm 1919 và nay trở thành "kính thiên văn tự nhiên" giúp kính James Webb quan sát các thiên hà sơ khai.
- **Sóng hấp dẫn:** những gợn sóng nhỏ của chính metric $$g_{\mu\nu}$$ lan truyền với tốc độ ánh sáng $$c$$. Năm 2015, đài quan sát LIGO lần đầu đo được sóng hấp dẫn từ hai lỗ đen sáp nhập cách Trái Đất 1,3 tỷ năm ánh sáng, với độ co giãn cực nhỏ cỡ $$10^{-21}$$ (tương đương đo sự thay đổi chiều dài nhỏ hơn 1/1.000 đường kính một hạt proton trên cánh tay laser dài 4 km!).
- **Vũ trụ học:** áp dụng phương trình Einstein cho vũ trụ đồng nhất và đẳng hướng (metric FLRW), toàn bộ hệ PDE rút gọn thành các ODE Friedmann mô tả sự giãn nở của vũ trụ từ Big Bang.

Mỗi hiện tượng trên đều là một **cơ chế định lượng** đi thẳng từ hình học đến con số đo đạc được, không phải phép ví von văn chương.

---

## 6. Toán học nhận lại được gì

| Chủ đề toán học | Liên hệ với GR |
|-------------|-------------|
| Hình học Riemann và hình học Lorentz | Metric, độ cong, đường trắc địa |
| Giải tích toàn cục và cấu trúc nhân quả | Miền phụ thuộc, các định lý kỳ dị Penrose–Hawking |
| PDE hyperbolic phi tuyến | Tính đặt chỉnh địa phương của phương trình tiến hóa Einstein |
| Tôpô vi phân | Tôpô của chân trời sự kiện, định lý khối lượng dương |
| Giải tích hình học | Tính ổn định của nghiệm Kerr, sóng phi tuyến trên nền lỗ đen |

GR vừa là một **ứng dụng của hình học làm thay đổi tận gốc vật lý**, vừa **nuôi dưỡng những chương trình nghiên cứu toán học thuần túy** đồ sộ (như chứng minh Định lý Khối lượng Dương của Schoen–Yau và Witten). Đây chính là tương tác hai chiều tuyệt đẹp mà Chương 3 nhấn mạnh.

---

## 7. Phân biệt chính xác và cường điệu

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "Einstein chứng minh mọi thứ đều tương đối." | Gây hiểu nhầm | Vẫn có những cấu trúc tuyệt đối (quan hệ nhân quả, tốc độ $$c$$, các đại lượng vô hướng của độ cong). |
| "Không gian cong giống một quả bóng nhìn từ bên ngoài." | Chỉ là hình ảnh ví von | Độ cong của không–thời gian là tính chất nội tại, không cần không gian bên ngoài. |
| "Lỗ đen phá vỡ vật lý." | Nói quá | Lỗ đen là nghiệm, là vùng trong GR (còn các câu hỏi lượng tử ở chân trời sự kiện là một hướng nghiên cứu riêng). |
| "GR và cơ học lượng tử đã được thống nhất." | Sai | Đã có lý thuyết bán cổ điển (trường lượng tử trên nền không–thời gian cong); lý thuyết hấp dẫn lượng tử đầy đủ vẫn còn mở. |
| "GPS chạy được nên phương trình Einstein đã được hiểu hết với tư cách PDE." | Nhầm phạm trù | Công nghệ dùng các hiệu chỉnh của GR; lý thuyết toàn cục của GR vẫn còn các bài toán mở. |

---

## Tài liệu tham khảo

1. Hartle — *Gravity*.  
2. Carroll — *Spacetime and Geometry*.  
3. Khóa học: [Giải tích → Vật lý]({{ site.baseurl }}/contents/vi/chapter03/03_02_Calculus_Physics_Engineering/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/).  
