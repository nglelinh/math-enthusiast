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

Bài này không yêu cầu giải phương trình Yang–Mills. Mục đích là để bạn hiểu chuỗi khái niệm **liên thông → vận chuyển song song → holonomy** qua một ví dụ cụ thể, kể cả ý chính của hiệu ứng Aharonov–Bohm: **$$F=0$$ tại mọi điểm trên đường đi vẫn không bảo đảm pha thu được sau một vòng là tầm thường**.

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

## 1. Thiết lập

Ta xem $$S^1$$ là đoạn $$\theta\in[0,2\pi]$$ với hai đầu được dán lại. Xét liên thông hằng:

$$
A=a\,d\theta,\qquad a\in\mathbb{R}.
$$

Trên mặt phẳng bỏ đi gốc tọa độ $$\mathbb{R}^2\setminus\{0\}$$, mô hình chuẩn là

$$
A=a\,d\theta
$$

viết trong tọa độ cực (không xác định tại gốc), và ta có

$$
\oint_{S^1}A=2\pi a.
$$

Dù $$F=dA=0$$ tại mọi điểm của mặt phẳng bỏ gốc, định lý Stokes vẫn cho thấy tích phân vòng bằng **thông lượng tập trung tại gốc**, hiểu theo nghĩa phân bố. Phần này cần cẩn thận, xem bài [phân bố]({{ site.baseurl }}/contents/vi/chapter03/03_12_Distributions_Dirac/).

---

## 2. Nhiệm vụ

### Nhiệm vụ A: Pha sau một vòng (30 phút)

Với hạt có điện tích $$q$$, tính hệ số holonomy

$$
U=\exp\!\Big(iq\oint_{S^1}A\Big)=\exp(iq\cdot 2\pi a)
$$

cho $$a=0,\;1/2,\;1$$ (có thể lấy $$q=1$$). Ghi rõ trường hợp nào $$U=1$$ và trường hợp nào $$U=-1$$.

**Viết:** với giá trị thông lượng nào thì holonomy là tầm thường?

### Nhiệm vụ B: Phép biến đổi gauge (20 phút)

Trên mặt phẳng bỏ gốc, xét $$A'=A+d\lambda$$ với $$\lambda$$ là hàm trơn, đơn trị. Chứng minh $$\oint A'=\oint A$$.

Thảo luận (định tính): điều gì thay đổi nếu $$\lambda$$ tăng thêm $$2\pi$$ sau khi đi hết một vòng (hàm góc đa trị, còn gọi là phép biến đổi gauge lớn)?

### Nhiệm vụ C: Ý chính của hiệu ứng Aharonov–Bohm (20 phút)

Viết không quá 120 chữ: vì sao vân giao thoa lại phụ thuộc vào thông lượng ở vùng mà hạt không hề đi qua, trong khi dọc đường đi thì $$B=0$$?

### Nhiệm vụ D: Thêm dòng vào từ điển (15 phút)

Thêm bốn dòng vào bảng vật lý ↔ toán: $$A$$, $$F$$, holonomy, phép biến đổi gauge. Mỗi dòng ghi rõ trạng thái.

### Nhiệm vụ E: Nhật ký

Ghi lại một lỗi bạn suýt mắc (ví dụ "$$F=0$$ ở mọi nơi nên $$A=0$$").

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

Thay $$U(1)$$ bằng một liên thông ma trận $$SU(2)$$ hằng dọc theo vòng tròn. Nếu $$A$$ hằng trong một gauge cố định, mũ có sắp thứ tự đường đi trở thành mũ ma trận thông thường. Tính $$\mathcal{P}\exp\oint A$$ khi $$A$$ là một phần tử sinh dạng đường chéo đơn giản.

---

## Xem thêm

- [Lý thuyết gauge như hình học]({{ site.baseurl }}/contents/vi/chapter06/06_19_Gauge_Geometry_YM/)  
- [Thực hành: từ điển vật lý ↔ toán]({{ site.baseurl }}/contents/vi/chapter07/07_11_Explore_Physics_Math_Dictionary/)  
- [Nhóm Lie]({{ site.baseurl }}/contents/vi/chapter03/03_11_Lie_Groups_Particle_Physics/)  
