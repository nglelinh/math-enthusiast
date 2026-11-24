---
layout: post
title: "Studio: Gauge vòng tròn đồ chơi và trực giác Aharonov–Bohm"
chapter: '07'
order: 12
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
---

> **Lộ trình: Hình học gauge (thực hành)**  
> **1.** [Lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)  
> **2.** Không bắt buộc: [Phân bố]({{ site.baseurl }}/contents/vi/chapter03/03_12_Distributions_Dirac/) (để dùng thông lượng và định lý Stokes cho cẩn thận)  
> **3. Bạn đang ở đây:** tính **holonomy** trong một mô hình đơn giản trên đường tròn  
> *Thời gian:* khoảng 60–120 phút; chỉ cần giải tích và số phức.

Hãy hình dung một thí nghiệm giao thoa điện tử kỳ lạ mà Yakir Aharonov và David Bohm đề xuất năm 1959: ta đặt một ống dây điện (solenoid) cực dài, được che chắn hoàn hảo sao cho toàn bộ từ trường $$B$$ bị giam chặt bên trong ống; còn bên ngoài ống — nơi hai chùm điện tử bay vòng qua hai phía trái và phải — từ trường $$B$$ bằng đúng **0 tại mọi điểm**. Theo điện từ học cổ điển, một hạt mang điện chưa từng chạm vào từ trường thì lực Lorentz tác dụng lên nó bằng 0, nên hình ảnh vân giao thoa trên màn chắn không thể nào thay đổi.

Vậy mà thực nghiệm lại cho thấy **vân giao thoa dịch chuyển rõ rệt** mỗi khi ta vặn dòng điện bên trong ống dây! Chẳng lẽ hạt điện tử "cảm nhận từ xa" được từ trường ở nơi nó không hề đi qua? Bí ẩn tưởng như siêu nhiên đó thực ra lại có một lời giải hình học vô cùng trong sáng. Trong bài thực hành này, bạn sẽ không cần đụng tới phương trình Yang–Mills phức tạp. Chỉ bằng một mô hình "đồ chơi" trên đường tròn $$S^1$$ cùng giải tích số phức cơ bản, bạn sẽ tự tay tính chuỗi khái niệm **liên thông → vận chuyển song song → holonomy**, và tận mắt thấy vì sao **độ cong $$F=0$$ tại mọi điểm dọc đường đi vẫn không ngăn được pha lượng tử bị xoay sau một vòng khép kín**.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Xem một liên thông $$U(1)$$ trên đường tròn như một 1-dạng $$A=a(\theta)\,d\theta$$ (hoặc $$A=a\,d\theta$$ với $$a$$ hằng).
- Tính pha $$e^{iq\oint A}$$ mà một hạt mang điện thu được khi đi hết một vòng $$S^1$$.
- Giải thích vì sao thông lượng qua một miền có thể bằng tích phân đường của $$A$$ (định lý Stokes), ngay cả khi đường đi tránh hoàn toàn vùng có từ trường $$B$$.
- Phân biệt phần là **định lý giải tích** với phần là **diễn giải vật lý**.
- Ghi lại một cách hiểu sai thường gặp, kiểu "thế chỉ là gauge thuần túy nên không có ý nghĩa vật lý".

**Kiến thức nền.** Tích phân đường; số phức $$e^{i\phi}$$; mục holonomy trường hợp giao hoán trong bài [Lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/).

---

## Bản đồ kiến thức nền: Hình học vi phân và Lý thuyết Gauge là gì, nghiên cứu những gì?

Khi nghe cụm từ "lý thuyết gauge" hay "holonomy", nhiều người tốt nghiệp đại học dễ thấy choáng ngợp vì thuật ngữ nghe trừu tượng. Nhưng trực giác cốt lõi của **Hình học vi phân (Differential Geometry)** đứng sau nó lại cực kỳ gần gũi:

Hãy tưởng tượng bạn đứng ở Bắc Cực của Trái Đất, cầm một mũi tên chỉ thẳng xuống xích đạo dọc theo kinh tuyến $$0^\circ$$. Bạn đi thẳng xuống xích đạo, rẽ trái đi một phần tư vòng xích đạo ($$90^\circ$$), rồi đi ngược lên lại Bắc Cực — trong suốt chuyến đi, bạn luôn giữ mũi tên "song song với chính nó" (không hề tự xoay cổ tay). Khi về tới Bắc Cực, bạn sẽ ngỡ ngàng thấy mũi tên của mình đã **xoay đi đúng $$90^\circ$$** so với ban đầu! Góc xoay tích lũy được sau khi đi hết một vòng kín đó gọi là **holonomy**, và nguyên nhân của nó là độ cong của mặt cầu bên trong vòng đi.

**Lý thuyết Gauge (Gauge Theory)** lấy chính ý tưởng hình học đó áp dụng cho **pha lượng tử** của hạt cơ bản (thay vì mũi tên tiếp tuyến trên mặt cầu, ta gắn một "mặt đồng hồ pha" $$U(1)$$ — tức đường tròn đơn vị trong $$\mathbb{C}$$ — tại mỗi điểm của không gian):
- **Liên thông (connection) $$A$$:** chính là quy tắc cho biết mặt đồng hồ pha phải xoay thêm bao nhiêu khi hạt dịch chuyển một đoạn vô cùng nhỏ. Trong điện từ học, đó chính là *thế vectơ từ* $$\mathbf{A}$$.
- **Độ cong (curvature) $$F = dA$$:** đo tốc độ xoay pha quanh một vòng vuông nhỏ xíu tại chỗ. Trong điện từ học, đó chính là *từ trường* $$\mathbf{B} = \nabla \times \mathbf{A}$$.
- **Tô pô tạo ra điều kỳ diệu:** Nếu không gian có một "lỗ thủng" (như mặt phẳng khoét đi gốc tọa độ $$\mathbb{R}^2 \setminus \{0\}$$ nơi đặt ống dây), một trường có thể hoàn toàn "phẳng" ở mọi điểm bên ngoài ($$F = 0$$), nhưng một vòng kín ôm quanh lỗ thủng vẫn tích lũy được góc xoay **holonomy** khác tầm thường! Giống như bạn đi quanh một hình nón nhọn: bề mặt bên của hình nón hoàn toàn phẳng (trải ra mặt bàn được), nhưng đi một vòng quanh đỉnh nhọn vẫn bị hụt góc!

---

## 1. Thiết lập

Ta xem $$S^1$$ là đoạn $$\theta\in[0,2\pi]$$ với hai đầu được dán lại. Xét liên thông hằng:

$$
A=a\,d\theta,\qquad a\in\mathbb{R}.
$$

Trong tọa độ Descartes $$(x,y)$$ trên mặt phẳng bỏ đi gốc tọa độ $$\mathbb{R}^2\setminus\{0\}$$, 1-dạng $$d\theta$$ viết tường minh là

$$
d\theta = \frac{-y\,dx + x\,dy}{x^2 + y^2},
$$

hoàn toàn trơn và xác định ở mọi nơi trừ gốc $$(0,0)$$. Ta dễ dàng kiểm tra bằng đạo hàm riêng rằng $$\frac{\partial}{\partial x}\!\left(\frac{x}{x^2+y^2}\right) - \frac{\partial}{\partial y}\!\left(\frac{-y}{x^2+y^2}\right) = 0$$ tại mọi $$(x,y) \neq (0,0)$$, nghĩa là độ cong $$F = dA = 0$$ ở khắp mọi điểm trên $$\mathbb{R}^2 \setminus \{0\}$$.

Ấy thế nhưng tích phân vòng quanh đường tròn đơn vị lại **khác 0**:

$$
\oint_{S^1}A = \int_0^{2\pi} a\,d\theta = 2\pi a.
$$

Nếu $$a \neq 0$$, điều này chứng tỏ $$A$$ *không thể* viết dưới dạng vi phân toàn phần $$d\lambda$$ của bất kỳ hàm đơn trị trơn $$\lambda(x,y)$$ nào trên toàn bộ $$\mathbb{R}^2\setminus\{0\}$$ (vì nếu viết được thì tích phân vòng đã phải bằng 0!). Về mặt vật lý, định lý Stokes cho thấy tích phân vòng $$2\pi a$$ chính bằng **từ thông $$\Phi$$ tập trung tại gốc** (bên trong ống dây solenoid), hiểu theo nghĩa phân bố Dirac. Phần này cần cẩn thận, xem bài [phân bố]({{ site.baseurl }}/contents/vi/chapter03/03_12_Distributions_Dirac/).

---

## 2. Nhiệm vụ

### Nhiệm vụ A: Pha sau một vòng (30 phút)

Với hạt có điện tích $$q$$, tính hệ số holonomy

$$
U=\exp\!\Big(iq\oint_{S^1}A\Big)=\exp(iq\cdot 2\pi a)
$$

cho $$a=0,\;1/2,\;1$$ (lấy $$q=1$$). Ghi rõ trường hợp nào $$U=1$$ và trường hợp nào $$U=-1$$.

**Gợi ý kiểm tra nhanh:** Với $$q=1$$ và $$a=1/2$$, ta có $$\oint A = \pi$$, nên $$U = e^{i\pi} = -1$$ — pha bị đảo ngược hoàn toàn (tương đương biến vân sáng giao thoa thành vân tối!). Nhưng với $$a=1$$, $$\oint A = 2\pi$$ nên $$U = e^{2\pi i} = 1$$ — dù từ thông khác 0, sự dịch pha đúng một vòng tròn lại làm vân giao thoa trở về vị trí cũ!

**Viết:** với giá trị thông lượng $$\Phi = 2\pi a$$ nào thì holonomy là tầm thường ($$U=1$$)?

### Nhiệm vụ B: Phép biến đổi gauge (20 phút)

Trên mặt phẳng bỏ gốc, xét $$A'=A+d\lambda$$ với $$\lambda$$ là hàm trơn, đơn trị. Chứng minh $$\oint_{S^1} A'=\oint_{S^1} A$$ (do $$\oint_{S^1} d\lambda = \lambda(2\pi) - \lambda(0) = 0$$), từ đó suy ra hệ số holonomy $$U$$ là **bất biến gauge** (tức là đại lượng có thể đo được bằng thực nghiệm!).

Thảo luận (định tính): điều gì thay đổi nếu $$\lambda(\theta) = k\theta$$ tăng thêm $$2\pi k$$ ($$k \in \mathbb{Z}$$) sau khi đi hết một vòng (hàm góc đa trị, nhưng $$g(\theta) = e^{i\lambda(\theta)}$$ vẫn đơn trị — còn gọi là **phép biến đổi gauge lớn**)?

### Nhiệm vụ C: Ý chính của hiệu ứng Aharonov–Bohm (20 phút)

Viết không quá 120 chữ: vì sao vân giao thoa lại phụ thuộc vào thông lượng ở vùng mà hạt không hề đi qua, trong khi dọc đường đi thì $$B=0$$? (Gợi ý: hai đường đi vòng qua hai bên ống dây hợp lại thành một vòng kín bao quanh lỗ thủng, nên hiệu pha giữa hai nhánh chính bằng tích phân vòng $$\oint A$$.)

### Nhiệm vụ D: Thêm dòng vào từ điển (15 phút)

Thêm bốn dòng vào bảng vật lý ↔ toán: $$A$$, $$F$$, holonomy, phép biến đổi gauge. Mỗi dòng ghi rõ trạng thái.

### Nhiệm vụ E: Nhật ký

Ghi lại một lỗi bạn suýt mắc (ví dụ "$$F=0$$ ở mọi nơi nên $$A=0$$" hoặc nhầm lẫn giữa biến đổi gauge nhỏ và biến đổi gauge lớn).

---

## 3. Tiêu chí đạt

| Tiêu chí | Đạt |
|----------|-----|
| Tính toán | $$U$$ đúng với cả ba giá trị $$a$$ |
| Định lý Stokes | Giải thích cẩn thận mối liên hệ giữa thông lượng và tích phân vòng |
| Hiệu ứng AB | Trình bày rõ ràng, không khẳng định có truyền tín hiệu nhanh hơn ánh sáng |
| Nhật ký | Có ít nhất một cách hiểu sai được ghi lại |

---

## 4. Mở rộng (không bắt buộc)

Thay $$U(1)$$ bằng một liên thông ma trận $$SU(2)$$ hằng dọc theo vòng tròn (ví dụ $$A = i a \sigma_3\, d\theta$$ với $$\sigma_3 = \operatorname{diag}(1,-1)$$). Nếu $$A$$ hằng trong một gauge cố định, mũ có sắp thứ tự đường đi trở thành mũ ma trận thông thường. Tính $$\mathcal{P}\exp\oint A$$ khi $$A$$ là một phần tử sinh dạng đường chéo đơn giản và kiểm tra xem ma trận kết quả có thuộc $$SU(2)$$ không.

---

## Xem thêm

- [Lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)  
- [Thực hành: từ điển vật lý ↔ toán]({{ site.baseurl }}/contents/vi/chapter07/07_11_Explore_Physics_Math_Dictionary/)  
- [Nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/)  
