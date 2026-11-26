---
layout: post
title: "Nghiệm nhớt của Lions và PDE phi tuyến (Huy chương Fields 1994)"
chapter: '02'
order: 24
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử giải một phương trình vi phân cấp một trông đơn giản như bài tập năm nhất đại học: $$\vert u'(x) \vert = 1$$ trên đoạn $$[-1, 1]$$, với điều kiện biên $$u(-1) = u(1) = 0$$. Mọi sinh viên đều vẽ ra ngay cái lều tam giác $$u_1(x) = 1 - \vert x \vert$$ — nhưng cái lều đó **có đỉnh nhọn tại $$x = 0$$ nên không khả vi**! Tệ hơn nữa, nếu cho phép hàm có góc nhọn (chỉ cần thỏa phương trình hầu khắp nơi), ta có thể vẽ ra cái lều úp ngược $$u_2(x) = \vert x \vert - 1$$, hay thậm chí **vô số đường răng cưa** nhấp nhô đều có độ dốc $$\pm 1$$ hầu khắp nơi và cùng bằng $$0$$ ở hai đầu mút! Vậy đâu là quy tắc toán học chính xác để chọn ra duy nhất một "nghiệm đúng"?

Câu hỏi tưởng chừng nhỏ bé đó đã châm ngòi cho một cuộc cách mạng trong giải tích phi tuyến cuối thế kỷ XX. Năm 1994 tại ICM Zürich, **Pierre-Louis Lions** nhận **Huy chương Fields** — như S. R. S. Varadhan trình bày trong diễn văn ICM, không phải cho một giả thuyết đơn lẻ mà cho cả một **chương trình nghiên cứu** trải rộng từ xác suất đến phương trình đạo hàm riêng phi tuyến, luôn nảy sinh từ bài toán ứng dụng. Trụ cột nổi tiếng nhất của chương trình đó là lý thuyết **nghiệm nhớt** (*viscosity solutions*) — do **Crandall–Lions** khởi xướng (1983), được **Evans**, **Ishii**, **Souganidis** mở rộng sang phương trình cấp hai phi tuyến hoàn toàn, và kết tinh trong bài *User's Guide* kinh điển của **Crandall–Ishii–Lions** (1992). Bên cạnh đó là hai trụ cột độc lập khác: lý thuyết **DiPerna–Lions** (phương trình Boltzmann và vận chuyển) và **nguyên lý tập trung–compact**. Bài học này cũng tách rõ hai ranh giới: Lions **không** giải bài toán Clay về Navier–Stokes không nén 3D, và **trò chơi trường trung bình** (Lasry–Lions, 2006) là ảnh hưởng rực rỡ *về sau*, không thuộc lời trao giải năm 1994.

**Mạch bài học:** Kiến thức cần nhớ (PDE phi tuyến hoàn toàn vs. nghiệm phân phối) → Ví dụ làm từng bước: giải phương trình eikonal $$\vert u'(x)\vert = 1$$ bằng phép thử chạm đồ thị và giới hạn độ nhớt $$-\varepsilon u''$$ → Giải thích: 4 bước từ định nghĩa hàm thử đến nguyên lý so sánh và tính ổn định → Hai trụ cột khác (DiPerna–Lions và tập trung–compact) → Những điều huy chương 1994 không khẳng định.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhìn nhận Huy chương Fields 1994 của Lions như một **chương trình nghiên cứu rộng lớn** (xác suất, PDE phi tuyến, ứng dụng) chứ không phải một định lý đơn lẻ.
- Tự tay áp dụng định nghĩa hàm thử chạm đồ thị lên phương trình $$\vert u'(x) \vert - 1 = 0$$ để loại bỏ cái lều úp ngược và chọn ra duy nhất nghiệm nhớt $$u_1(x) = 1 - \vert x \vert$$.
- Giải thích vì sao phương trình Hamilton–Jacobi và PDE phi tuyến hoàn toàn không dùng được tích phân từng phần (nghiệm phân phối), nên phải xây dựng nghiệm yếu trên nền **nguyên lý cực đại**.
- Mô tả vai trò trung tâm của **nguyên lý so sánh** và ghi công đầy đủ cho **Crandall**, **Ishii**, **Evans**, **Souganidis**.
- Phân biệt hai trụ cột song hành: **DiPerna–Lions** (nghiệm tái chuẩn hóa Boltzmann / vận chuyển) và **nguyên lý tập trung–compact**.
- Tách **trò chơi trường trung bình** (Lasry–Lions, 2006) khỏi lời trao giải 1994 và bác bỏ nhầm lẫn rằng Lions giải Navier–Stokes 3D không nén.

**Kiến thức nền.** Giải tích nhiều biến; phương trình đạo hàm riêng cấp một như phương trình Hamilton–Jacobi $$u_t + H(x,\nabla u)=0$$; nguyên lý cực đại cổ điển cho hàm điều hòa hoặc cho phương trình elliptic tuyến tính đều. Điều khiển tối ưu và lý thuyết động học giúp hiểu động cơ, nhưng không bắt buộc phải học trước.

**Liên kết với các bài khác.** Bài này minh họa hai ý của chương: một chương trình nghiên cứu có thể thay đổi cả ngôn ngữ của một lĩnh vực, và cần trích dẫn đúng lời trao giải. Các bài giải tích liên quan: [Yu Deng / PDE động học]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (phương trình Boltzmann ở giai đoạn sau), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) (tính chính quy cho phương trình phi tuyến hoàn toàn, có *dùng* nghiệm nhớt), và [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) (để tách riêng bài toán Thiên niên kỷ).

---

## Kiến thức cần nhớ: PDE phi tuyến hoàn toàn và "nghiệm yếu không dùng tích phân từng phần" là gì?

### 1. Vì sao tích phân từng phần bị vô hiệu hóa?
Với PDE tuyến tính như phương trình Laplace $$-\Delta u = f$$, khi $$u$$ không khả vi cấp hai, ta nhân với hàm thử trơn $$\varphi$$ rồi tích phân từng phần để đá đạo hàm sang $$\varphi$$: $$\int \nabla u \cdot \nabla\varphi = \int f\varphi$$. Nhưng với **phương trình Hamilton–Jacobi** $$u_t + H(x, \nabla u) = 0$$ (trong điều khiển tối ưu, quang hình học) hay **PDE cấp hai phi tuyến hoàn toàn** $$F(x, u, \nabla u, D^2 u) = 0$$ (như phương trình Hamilton–Jacobi–Bellman hay Monge–Ampère $$\det D^2 u = f$$), đạo hàm của $$u$$ nằm lọt bên trong hàm phi tuyến — **tích phân từng phần hoàn toàn bất lực!**

### 2. Ý tưởng thay thế: chuyển đạo hàm sang hàm thử bằng "điểm cực đại"
Giả sử $$u$$ là hàm trơn $$C^2$$ và một hàm thử trơn $$\varphi$$ chạm vào đồ thị $$u$$ từ **phía trên** tại $$x_0$$ (tức $$u - \varphi$$ đạt cực đại địa phương tại $$x_0$$). Theo giải tích cơ bản, tại $$x_0$$ ta có $$\nabla u(x_0) = \nabla\varphi(x_0)$$ và $$D^2 u(x_0) \le D^2\varphi(x_0)$$. Nếu $$F$$ có tính elliptic (giảm theo biến ma trận $$D^2 u$$), thì đẳng thức $$F(x_0, u, \nabla u, D^2 u) = 0$$ kéo theo bất đẳng thức $$F(x_0, u(x_0), \nabla\varphi(x_0), D^2\varphi(x_0)) \le 0$$. Điểm thiên tài: **bất đẳng thức này chỉ chứa đạo hàm của hàm thử trơn $$\varphi$$, nên dùng được cho mọi hàm $$u$$ chỉ liên tục có đầy góc nhọn!**

---

## 1. Ví dụ làm từng bước: giải phương trình eikonal $$\vert u'(x) \vert - 1 = 0$$ trên $$[-1, 1]$$

Hãy xét phương trình $$F(u') = \vert u'(x) \vert - 1 = 0$$ trên $$[-1, 1]$$ với $$u(-1) = u(1) = 0$$. Ta có hai ứng cử viên liên tục rõ ràng đều thỏa phương trình ở mọi $$x \neq 0$$:
- **Cái lều ngửa lên:** $$u_1(x) = 1 - \vert x \vert$$ (đỉnh nhọn tại $$x = 0$$).
- **Cái lều úp ngược:** $$u_2(x) = \vert x \vert - 1$$ (đáy nhọn tại $$x = 0$$).

Hãy dùng định nghĩa **nghiệm nhớt** của Crandall–Lions kiểm tra từng ứng cử viên ngay tại điểm không khả vi $$x_0 = 0$$:
1. **Kiểm tra $$u_1(x) = 1 - \vert x \vert$$ tại $$x_0 = 0$$:**
   - *Điều kiện nghiệm dưới* (hàm thử trơn $$\varphi$$ chạm $$u_1$$ từ **phía trên** tại $$0$$): vì đồ thị $$\varphi$$ nằm trên cái lều có hai mái dốc $$+1$$ (bên trái) và $$-1$$ (bên phải), tiếp tuyến của $$\varphi$$ tại đỉnh $$0$$ bắt buộc có độ dốc nằm trong $$[-1, 1]$$, tức $$\vert \varphi'(0) \vert \le 1 \implies \vert \varphi'(0) \vert - 1 \le 0$$. **Đạt!**
   - *Điều kiện nghiệm trên* (hàm thử trơn $$\varphi$$ chạm $$u_1$$ từ **phía dưới** tại $$0$$): bạn không thể nhét bất kỳ đường cong trơn nào nằm dưới hai mái chụm nhọn lên trên mà chạm được đỉnh $$0$$! Vì *không tồn tại* hàm thử nào như vậy, điều kiện nghiệm trên tự động đúng. **Đạt!**
   - Kết luận: **$$u_1(x) = 1 - \vert x \vert$$ là một nghiệm nhớt!**

2. **Kiểm tra $$u_2(x) = \vert x \vert - 1$$ tại $$x_0 = 0$$:**
   - *Điều kiện nghiệm trên* (hàm thử trơn $$\varphi$$ chạm $$u_2$$ từ **phía dưới** tại $$0$$): hãy chọn ngay hàm hằng cực đơn giản $$\varphi(x) \equiv -1$$! Nó chạm đáy chữ V của $$u_2$$ từ phía dưới tại $$x_0 = 0$$ và có đạo hàm $$\varphi'(0) = 0$$. Thay vào phương trình:
     $$
     \vert \varphi'(0) \vert - 1 = 0 - 1 = -1 < 0 \quad (\text{vi phạm điều kiện nghiệm trên } \ge 0!).
     $$
   - Kết luận: **$$u_2(x) = \vert x \vert - 1$$ bị loại ngay lập tức!** (Mọi đường răng cưa có "đáy chữ V" đều bị loại y hệt như vậy!)

3. **Kiểm tra bằng giới hạn "độ nhớt tiến về 0":** Nếu ta thêm số hạng làm trơn $$-\varepsilon u''$$ thành phương trình cấp hai $$-\varepsilon u_\varepsilon''(x) + \vert u_\varepsilon'(x) \vert = 1$$ ($$u_\varepsilon(\pm 1) = 0$$), ta giải được nghiệm trơn tường minh là một đường cong tròn đầu tại $$x = 0$$:
   $$
   u_\varepsilon(x) = 1 - \vert x \vert - \varepsilon \ln\left(\frac{1 + e^{-2\vert x \vert/\varepsilon}}{1 + e^{-2/\varepsilon}}\right) \xrightarrow{\varepsilon \to 0^+} 1 - \vert x \vert = u_1(x)!
   $$
   Chính phép lấy giới hạn $$\varepsilon \to 0^+$$ làm tròn đỉnh nhọn này là nguồn gốc lịch sử của cái tên **"nghiệm nhớt"** (*viscosity solution*)!

---

## 2. Giải thích: Cỗ máy nghiệm nhớt vận hành ra sao cho PDE cấp hai?

Sau bài báo nền tảng cho phương trình cấp một của **Crandall–Lions (1983)** và các mở rộng của **Evans**, **Ishii**, **Souganidis**, toàn bộ lý thuyết cho phương trình cấp hai phi tuyến hoàn toàn $$F(x, u, \nabla u, D^2 u) = 0$$ được hệ thống hóa trong bài *User's Guide* nổi tiếng của **Crandall–Ishii–Lions** (*Bull. Amer. Math. Soc.* 1992; [arXiv:math/9207212](https://arxiv.org/abs/math/9207212)) qua 4 bước:

#### Bước 1: Định nghĩa bằng hàm thử chạm đồ thị (hoặc bằng "jet" cấp hai)
Một hàm liên tục $$u$$ là **nghiệm dưới nhớt** nếu mọi hàm thử trơn $$\varphi$$ chạm $$u$$ từ trên tại $$x_0$$ đều thỏa $$F(x_0, u(x_0), \nabla\varphi(x_0), D^2\varphi(x_0)) \le 0$$; là **nghiệm trên nhớt** nếu mọi hàm thử trơn chạm từ dưới thỏa $$\ge 0$$; và là **nghiệm nhớt** nếu thỏa cả hai. Định nghĩa tương thích tuyệt đối với nghiệm cổ điển $$C^2$$.

#### Bước 2: Nguyên lý so sánh (Comparison Principle) — trái tim của tính duy nhất
Nếu $$u$$ là nghiệm dưới nhớt và $$v$$ là nghiệm trên nhớt của cùng phương trình elliptic trên miền $$\Omega$$ với $$u \le v$$ trên biên $$\partial\Omega$$, thì $$u \le v$$ khắp trong $$\Omega$$. Hệ quả tức thì: **hai nghiệm nhớt có cùng điều kiện biên bắt buộc phải trùng nhau!**
Để chứng minh khi $$u, v$$ không khả vi, ta dùng tuyệt kỹ **nhân đôi biến** (*doubling of variables*): tối đa hóa $$u(x) - v(y) - \frac{1}{2\varepsilon}\vert x - y \vert^2$$ để ép $$x, y$$ sát nhau, rồi dùng **bổ đề Ishii (định lý tổng)** tạo ra cặp ma trận Hessian xấp xỉ tại điểm cực đại $$(x_\varepsilon, y_\varepsilon)$$ dẫn tới mâu thuẫn với tính elliptic của $$F$$.

#### Bước 3: Phương pháp Perron — từ so sánh suy ra ngay tồn tại nghiệm
Một khi đã có nguyên lý so sánh, phương pháp Perron cổ điển (lấy cận trên đúng của mọi nghiệm dưới nhớt nằm dưới một nghiệm trên) tự động tạo ra một nghiệm nhớt toàn cục — chứng minh trọn vẹn cả **tồn tại lẫn duy nhất**!

#### Bước 4: Tính ổn định kỳ diệu dưới hội tụ đều
Khác hẳn nghiệm cổ điển (đòi hỏi đạo hàm hội tụ), giới hạn hội tụ đều của bất kỳ dãy nghiệm nhớt nào vẫn **tự động là nghiệm nhớt**! Nhờ đó, giới hạn độ nhớt $$\varepsilon \to 0$$, giới hạn của các lược đồ sai phân số đơn điệu, hay hàm giá trị của bài toán điều khiển tối ưu đều lập tức được xác nhận trùng với nghiệm nhớt duy nhất.

Tóm tắt bản chất cuộc cách mạng Crandall–Ishii–Lions:

$$
\text{PDE phi tuyến hoàn toàn}
\;\xrightarrow{\text{hàm thử chạm}}\;
\text{Nghiệm nhớt}
\;\xrightarrow{\text{nhân đôi biến + Ishii}}\;
\text{So sánh + Ổn định} \implies \text{Tồn tại \& Duy nhất}.
$$

---

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/lions-viscosity-solutions_vi.mp4"></video>
</div>

Video dài khoảng 53 giây (có thuyết minh tiếng Việt): nghiệm nhớt (viscosity solutions) cho phương trình Hamilton–Jacobi–Bellman và nguyên lý so sánh.

## 3. Hai trụ cột lớn khác trong chương trình của Lions (1994)

1. **Lý thuyết DiPerna–Lions (1989) cho phương trình Boltzmann và phương trình vận chuyển.** Cùng **Ronald J. DiPerna**, Lions đưa ra khái niệm **nghiệm tái chuẩn hóa** (*renormalized solutions*) cho phương trình Boltzmann — tác động bằng hàm phi tuyến kiểu $$\ln(1+f)$$ kết hợp bổ đề compact trung bình vận tốc để chứng minh tồn tại toàn cục và ổn định yếu cho dữ kiện lớn (*Ann. of Math.* 1989). Song hành là lý thuyết **phương trình vận chuyển** với trường vận tốc thuộc lớp Sobolev $$W^{1,1}$$ (dù không đủ Lipschitz cho quỹ đạo cổ điển duy nhất, dòng Lagrange vẫn xác định hầu khắp nơi — sau này Ambrosio mở rộng sang BV). Đặt cạnh [bài về Yu Deng]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/): DiPerna–Lions xử lý tính đặt đúng của *chính* phương trình Boltzmann, còn Deng–Hani–Ma suy dẫn phương trình Boltzmann từ hệ hạt cầu cứng.
2. **Nguyên lý tập trung–compact (Concentration-Compactness, 1984–1985).** Khi cực tiểu hóa năng lượng trên không gian không compact $$\mathbb{R}^n$$ (như tìm hàm cực trị bất đẳng thức Sobolev hay bài toán kiểu Yamabe), một dãy cực tiểu hóa chỉ có thể mất tính compact theo đúng 3 cách: **tan biến** (trải loãng về 0), **tách đôi** (xé thành hai cục trôi xa nhau), hoặc **tập trung** (compact sau phép tịnh tiến/co giãn). Lions phân loại triệt để ba kịch bản này và đưa ra điều kiện năng lượng dưới cộng tính chặt để loại trừ kịch bản tách đôi, khôi phục tính tồn tại cực tiểu.

---

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/lions-boltzmann-mfg_vi.mp4"></video>
</div>

Video dài khoảng 45 giây (có thuyết minh tiếng Việt): nghiệm DiPerna–Lions cho phương trình Boltzmann và trò chơi trường trung bình (Mean Field Games).

## 4. Những điều huy chương 1994 không khẳng định và vì sao là Huy chương Fields

- **Không phải bài toán Clay về Navier–Stokes:** Các kết quả tồn tại nghiệm yếu của Lions là cho hệ Navier–Stokes **nén được**, không phải [bài toán Thiên niên kỷ]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) về tính chính quy toàn cục của Navier–Stokes **không nén 3D**.
- **Không phải trò chơi trường trung bình (Mean Field Games):** Cùng **Jean-Michel Lasry**, Lions sáng lập lý thuyết trò chơi trường trung bình năm **2006** (hệ ghép Hamilton–Jacobi–Bellman và Fokker–Planck). Đây là nhánh ảnh hưởng khổng lồ về sau, nhưng ra đời hơn một thập kỷ *sau* năm 1994.
- **Không phải công trình của một cá nhân đơn lẻ:** Nghiệm nhớt là thành quả cộng tác của Crandall, Lions, Evans, Ishii, Souganidis và cả một cộng đồng rộng lớn.

**Vì sao là Huy chương Fields:** Như Varadhan tổng kết tại ICM 1994, Lions không chỉ tạo ra một ngôn ngữ mới (nghiệm nhớt) làm biến đổi điều khiển tối ưu, lan truyền mặt sóng và hình học phi tuyến hoàn toàn, mà còn kiến tạo thêm hai cỗ máy độc lập cỡ lớn (DiPerna–Lions và tập trung–compact) — chứng minh rằng các bài toán xuất phát từ ứng dụng thực tế chính là nguồn sinh ra giải tích thuần túy sâu sắc nhất.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Nghiệm nhớt là nghiệm cổ điển $$C^2$$ có thêm độ nhớt." | Đó là nghiệm *yếu*, định nghĩa bằng bất đẳng thức với hàm thử; nghiệm $$C^2$$ chỉ là trường hợp đặc biệt. |
| "'Nhớt' là độ nhớt vật lý của chất lưu." | Tên gọi nhắc tới các *xấp xỉ* có độ nhớt tiến về 0; định nghĩa không liên quan tới chất lưu nào. |
| "Lions đã giải Navier–Stokes." | Không. Kết quả tồn tại cho trường hợp nén được không phải bài toán chính quy không nén của Viện Clay. |
| "Huy chương 1994 là nhờ trò chơi trường trung bình." | Trò chơi trường trung bình của Lasry–Lions xuất hiện giữa thập niên 2000; chỉ là ảnh hưởng về sau. |
| "Nghiệm phân phối là đủ cho phương trình phi tuyến hoàn toàn." | Khi $$F$$ phi tuyến theo $$D^2 u$$, tích phân từng phần không dùng được; nguyên lý so sánh mới là công cụ đúng. |
| "Một mình Lions phát minh nghiệm nhớt." | Crandall–Lions; sau đó Evans, Ishii, Souganidis và nhiều người khác. |
| "DiPerna–Lions suy ra phương trình Boltzmann từ hệ hạt." | Họ cho một lý thuyết đặt đúng cho phương trình động học; suy dẫn từ hệ hạt là câu chuyện khác (về sau). |

---

## Liên kết

- Trang Huy chương Fields của IMU: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Huy chương Fields 1994: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1994)
- Wikipedia, Pierre-Louis Lions: [https://en.wikipedia.org/wiki/Pierre-Louis_Lions](https://en.wikipedia.org/wiki/Pierre-Louis_Lions)
- Wikipedia, viscosity solution: [https://en.wikipedia.org/wiki/Viscosity_solution](https://en.wikipedia.org/wiki/Viscosity_solution)
- User’s guide Crandall–Ishii–Lions trên arXiv: [https://arxiv.org/abs/math/9207212](https://arxiv.org/abs/math/9207212)
- Tiểu sử ghế Collège de France: [https://www.college-de-france.fr/en/chair/pierre-louis-lions-partial-differential-equations-and-applications-statutory-chair/biography](https://www.college-de-france.fr/en/chair/pierre-louis-lions-partial-differential-equations-and-applications-statutory-chair/biography)
- Tìm arXiv, Lions viscosity: [https://arxiv.org/search/?query=Lions+viscosity+solutions&searchtype=all](https://arxiv.org/search/?query=Lions+viscosity+solutions&searchtype=all)

---

## Tài liệu tham khảo

1. S. R. S. Varadhan, bài giảng về công trình P.-L. Lions, *Proceedings of the ICM*, Zürich, 1994 (tài liệu ICM chuẩn được IMU 1994 trích).
2. **M. G. Crandall và P.-L. Lions**, “Viscosity solutions of Hamilton–Jacobi equations,” *Trans. Amer. Math. Soc.* **277** (1983).
3. **M. G. Crandall, L. C. Evans và P.-L. Lions**, “Some properties of viscosity solutions of Hamilton–Jacobi equations,” *Trans. Amer. Math. Soc.* **282** (1984).
4. **M. G. Crandall, H. Ishii và P.-L. Lions**, “User’s guide to viscosity solutions of second order partial differential equations,” *Bull. Amer. Math. Soc.* **27** (1992); [arXiv:math/9207212](https://arxiv.org/abs/math/9207212).
5. **R. J. DiPerna và P.-L. Lions**, “On the Cauchy problem for Boltzmann equations: global existence and weak stability,” *Ann. of Math.* **130** (1989).
6. **P.-L. Lions**, các bài concentration-compactness, *Ann. Inst. H. Poincaré Anal. Non Linéaire* (1984) và *Rev. Mat. Iberoamericana* (1985).
7. **J.-M. Lasry và P.-L. Lions**, ghi chú / *C. R. Math.* về mean field games (2006)—ảnh hưởng sau, không phải citation 1994.
8. Ngữ cảnh khóa học: [Deng / phương trình động học]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/), [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).

---

## Hướng đi tiếp

- Đọc bài hướng dẫn của Crandall–Ishii–Lions như một giáo trình: học nguyên lý so sánh trước, ví dụ sau.
- So sánh giới hạn độ nhớt tiến về 0 với nghiệm entropy của luật bảo toàn vô hướng (một lý thuyết nghiệm yếu gần gũi, nhưng định nghĩa khác).
- Nếu quan tâm tới ứng dụng, hãy xem trò chơi trường trung bình như một lĩnh vực *sử dụng* nghiệm nhớt, ra đời sau huy chương.
- Bài tập thêm: viết một trang "nghiệm nhớt không phải là gì" (không phải lời giải Navier–Stokes, không phải nội dung lời trao giải về trò chơi trường trung bình, không phải độ nhớt của chất lưu).

## Video tham khảo

- **Xem trước**: [The Essentials of Viscosity Solutions in R^n II](https://www.youtube.com/watch?v=I_fsCAW3xrM) (USF GradMath, tiếng Anh). Bài giảng nhập môn về nghiệm nhớt trong R^n, đúng đối tượng giải tích của bài này. Nên xem trước khi nghe các bài giảng của chính Lions.
- [Pierre-Louis Lions: Complete" Analysis of the Master Equation: an Example](https://www.youtube.com/watch?v=k0G_fwTVqHA) (Centre de recherches mathématiques - CRM, tiếng Anh). Bài giảng của Lions về "phương trình chủ" (master equation) trong trò chơi trường trung bình. Đây là chủ đề về sau, giúp thấy nghiệm nhớt được dùng tiếp ra sao, nhưng không thuộc lời trao giải 1994.
- [Charlemagne Distingushed Lecture Series 2012 with Prof. Dr. Pierre-Louis Lions](https://www.youtube.com/watch?v=spkaGZPTt9Q) (IRTG 2379 MIP, tiếng Anh). Bài giảng đại chúng của Lions trong chuỗi Charlemagne năm 2012. Xem để có thêm góc nhìn về cách ông chọn bài toán từ ứng dụng.
