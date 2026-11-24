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

**Mạch bài học:** Bản đồ kiến thức nền (hình học vi phân, liên thông–độ cong–holonomy & vai trò của tô pô lỗ thủng) → Thiết lập 1-dạng $$A = a\,d\theta$$ trên $$\mathbb{R}^2\setminus\{0\}$$ → Khung giải thích chậm: tự tay giải phương trình vận chuyển song song và kiểm tra biến đổi gauge lớn → Nhiệm vụ tính holonomy & nhật ký.

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

Khi nghe cụm từ "lý thuyết gauge" hay "holonomy", nhiều người tốt nghiệp đại học dễ thấy choáng ngợp vì thuật ngữ nghe trừu tượng. Nhưng trực giác cốt lõi đứng sau nó dựa trên ba viên gạch cực kỳ gần gũi:

### 1. Vận chuyển song song và Holonomy trong Hình học vi phân

Hãy tưởng tượng bạn đứng ở Bắc Cực của Trái Đất, cầm một mũi tên chỉ thẳng xuống xích đạo dọc theo kinh tuyến $$0^\circ$$. Bạn đi thẳng xuống xích đạo, rẽ trái đi một phần tư vòng xích đạo ($$90^\circ$$), rồi đi ngược lên lại Bắc Cực — trong suốt chuyến đi, bạn luôn giữ mũi tên "song song với chính nó" (không hề tự xoay cổ tay). Khi về tới Bắc Cực, bạn sẽ ngỡ ngàng thấy mũi tên của mình đã **xoay đi đúng $$90^\circ$$** so với ban đầu! Góc xoay tích lũy được sau khi đi hết một vòng kín đó gọi là **holonomy**, và nguyên nhân của nó là độ cong của mặt cầu bên trong vòng đi.

### 2. Lý thuyết Gauge: liên thông $$A$$ và độ cong $$F$$ cho pha lượng tử

**Lý thuyết Gauge (Gauge Theory)** áp dụng chính ý tưởng đó cho **pha lượng tử** của hạt cơ bản: thay vì mũi tên tiếp tuyến trên mặt cầu, ta gắn một "mặt đồng hồ pha" $$U(1)$$ (đường tròn đơn vị trong $$\mathbb{C}$$) tại mỗi điểm của không gian:
- **Liên thông (connection) $$A$$:** quy tắc cho biết mặt đồng hồ pha phải xoay thêm bao nhiêu khi hạt dịch chuyển một đoạn vô cùng nhỏ (trong điện từ học, chính là *thế vectơ từ* $$\mathbf{A}$$).
- **Độ cong (curvature) $$F = dA$$:** đo tốc độ xoay pha quanh một vòng vuông nhỏ xíu tại chỗ (trong điện từ học, chính là *từ trường* $$\mathbf{B} = \nabla \times \mathbf{A}$$).

### 3. Vai trò của Tô pô "lỗ thủng" (Đối đồng điều de Rham)

Nếu không gian không có lỗ thủng (như toàn bộ $$\mathbb{R}^2$$), định lý Poincaré bảo đảm mọi 1-dạng đóng ($$dA = 0$$) đều là vi phân toàn phần ($$A = d\lambda$$) nên tích phân vòng luôn bằng 0. Nhưng khi không gian bị khoét một **lỗ thủng** ($$\mathbb{R}^2 \setminus \{0\}$$ nơi đặt ống dây solenoid), một liên thông có thể hoàn toàn "phẳng" ở mọi điểm bên ngoài ($$F = 0$$) mà vẫn có tích phân vòng **khác 0**! Giống như bề mặt bên của một chiếc nón lá: trải phẳng ra mặt bàn được (độ cong bằng 0 ở mọi điểm ngoài đỉnh), nhưng đi một vòng quanh đỉnh nhọn vẫn bị hụt góc!

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

Nếu $$a \neq 0$$, điều này chứng tỏ $$A$$ *không thể* viết dưới dạng vi phân toàn phần $$d\lambda$$ của bất kỳ hàm đơn trị trơn $$\lambda(x,y)$$ nào trên toàn bộ $$\mathbb{R}^2\setminus\{0\}$$. Về mặt vật lý, định lý Stokes cho thấy tích phân vòng $$2\pi a$$ chính bằng **từ thông $$\Phi$$ tập trung tại gốc** (bên trong ống dây solenoid), hiểu theo nghĩa phân bố Dirac. Phần này cần cẩn thận, xem bài [phân bố]({{ site.baseurl }}/contents/vi/chapter03/03_12_Distributions_Dirac/).

---

### Khung giải thích: Cầm tay giải phương trình vận chuyển song song và kiểm tra biến đổi gauge (nên đọc chậm)

Để thấy công thức holonomy $$U = \exp(iq \oint A)$$ không hề "rơi từ trên trời xuống" mà xuất phát trực tiếp từ phương trình vi phân năm nhất đại học, hãy tự tính từng bước:

1. **Phương trình vận chuyển song song trên $$S^1$$:** Một hàm sóng phức $$\psi(\theta)$$ được gọi là *vận chuyển song song* theo liên thông $$A = a\,d\theta$$ (với điện tích $$q$$) nếu đạo hàm hiệp biến của nó bằng 0:
   $$
   \left(\frac{d}{d\theta} - i q a\right)\psi(\theta) = 0 \iff \frac{d\psi}{d\theta} = i q a\,\psi(\theta).
   $$
2. **Giải nghiệm tường minh với điều kiện đầu $$\psi(0) = 1$$:** Phương trình vi phân cấp 1 đơn giản này có nghiệm duy nhất:
   $$
   \psi(\theta) = e^{i q a \theta}.
   $$
3. **Đi hết một vòng ($$\theta = 2\pi$$) và thay số với $$q = 1$$:**
   - Khi $$a = 0$$: $$\psi(2\pi) = e^{0} = 1$$ (không lệch pha).
   - Khi $$a = 1/2$$: $$\psi(2\pi) = e^{i\pi} = \mathbf{-1}$$! Hạt quay lại đúng điểm xuất phát nhưng pha lượng tử đã **đảo dấu hoàn toàn** — hai chùm giao thoa vòng hai phía ống dây bị đảo từ cộng hưởng (vân sáng) thành triệt tiêu (vân tối)!
   - Khi $$a = 1$$: $$\psi(2\pi) = e^{2\pi i} = \mathbf{+1}$$! Dù từ thông $$\Phi = 2\pi$$ khác 0, sự xoay pha đúng một vòng trọn vẹn khiến vân giao thoa khớp lại như cũ (đây chính là hiện tượng **lượng tử hóa từ thông**!).
4. **Kiểm tra phép biến đổi gauge lớn:** Nếu ta đổi pha theo hàm đơn trị $$g(\theta) = e^{i k \theta}$$ (với $$k \in \mathbb{Z}$$), liên thông mới dịch chuyển một lượng nguyên: $$A' = A + \frac{1}{q} k\,d\theta \implies a' = a + \frac{k}{q}$$. Tính lại holonomy mới:
   $$
   U' = e^{i q \cdot 2\pi (a + k/q)} = e^{i q \cdot 2\pi a} \cdot \underbrace{e^{2\pi i k}}_{=\,1} = U!
   $$
   Hệ số thế $$a$$ thay đổi, nhưng **holonomy $$U$$ hoàn toàn bất biến** — đó là lý do chỉ $$U$$ (chứ không phải riêng $$A$$) mới là đại lượng đo được trong phòng thí nghiệm!

---

## 2. Nhiệm vụ

### Nhiệm vụ A: Pha sau một vòng (30 phút)

Với hạt có điện tích $$q$$, tính hệ số holonomy

$$
U=\exp\!\Big(iq\oint_{S^1}A\Big)=\exp(iq\cdot 2\pi a)
$$

cho $$a=0,\;1/2,\;1$$ (lấy $$q=1$$). Ghi rõ trường hợp nào $$U=1$$ và trường hợp nào $$U=-1$$.

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
