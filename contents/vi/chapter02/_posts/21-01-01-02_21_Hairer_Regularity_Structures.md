---
layout: post
title: "Cấu trúc chính quy của Hairer (Huy chương Fields 2014)"
chapter: '02'
order: 21
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy quan sát ranh giới cháy lan nhấp nhô trên một tờ giấy, hay bề mặt gồ ghề của một đám tuyết rơi dày. Các nhà vật lý rất thích viết xuống những phương trình đạo hàm riêng có thêm một số hạng "nhiễu trắng" đại diện cho vô số va chạm ngẫu nhiên li ti. Trên bảng phấn, những phương trình ấy trông cực kỳ gọn gàng; nhưng trong mắt nhà toán học giải tích, chúng là một **cơn ác mộng lôgic**: nghiệm của phương trình gồ ghề đến mức ngay cả việc bình phương đạo hàm hay lấy lập phương của nghiệm cũng trở thành "nhân hai đại lượng vô hạn với nhau" — một phép toán hoàn toàn vô nghĩa!

Suốt nhiều thập niên, những phương trình kinh điển như **KPZ** hay **$$\Phi^4_3$$ động lực** nằm trong tình trạng lơ lửng: ai cũng tin chúng mô tả đúng tự nhiên, nhưng không ai biết cách *định nghĩa* nghiệm của chúng. Năm 2014, **Martin Hairer** nhận **Huy chương Fields**

> “for his outstanding contributions to the theory of stochastic partial differential equations, and in particular for the creation of a theory of regularity structures for such equations.”
> — [IMU, Fields Medals 2014](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014)

*Tạm dịch: vì những đóng góp xuất sắc cho lý thuyết phương trình đạo hàm riêng ngẫu nhiên, đặc biệt là việc xây dựng lý thuyết cấu trúc chính quy cho các phương trình này.*

Huy chương này trao cho một **ngôn ngữ mới**. Bằng cách mở rộng khai triển Taylor cổ điển — bổ sung vào danh sách đa thức $$1, x, x^2, \ldots$$ các "đơn thức trừu tượng" dựng từ chính nhiễu trắng — lý thuyết **cấu trúc chính quy** (*regularity structures*) của Hairer cho phép ta nhân các phân phối gồ ghề trong một không gian đại số, thực hiện **tái chuẩn hóa** chặt chẽ, rồi "tái dựng" thành nghiệm thật. Bài học này cũng đặt công trình của Hairer cạnh **đường thô** (*rough paths*) của Lyons và **phân phối paracontrol** của Gubinelli–Imkeller–Perkowski, đồng thời khẳng định rõ: đây không phải lời giải bài toán Navier–Stokes 3D của Viện Clay, và bằng tiến sĩ vật lý của Hairer chỉ là chi tiết tiểu sử.

**Mạch bài học:** Bản đồ kiến thức nền (phân phối, nhiễu trắng, SPDE kỳ dị) → Ví dụ cầm tay chỉ việc: vì sao $$\delta_0^2$$ bùng nổ và bảng đếm bậc chính quy của KPZ, $$\Phi^4_3$$ → Khung giải thích chậm: 4 bước từ khai triển Taylor mở rộng đến tái dựng, tái chuẩn hóa và điểm bất động → Đường thô (Lyons) & Phân phối paracontrol (GIP) → Phạm vi định lý và những điều không khẳng định.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Tự tính ví dụ đỉnh hộp $$\delta_\varepsilon^2$$ và bảng đếm bậc chính quy để giải thích chính xác vì sao số hạng $$(\partial_x h)^2$$ trong KPZ và $$\Phi^3$$ trong $$\Phi^4_3$$ là bất hợp pháp theo nghĩa cổ điển.
- Mô tả **cấu trúc chính quy** $$(\mathcal{A}, T, G)$$ như một khai triển Taylor mở rộng chứa thêm các đơn thức hình cây xây từ nhiễu trắng.
- Phát biểu rõ chuỗi 3 bước cốt lõi của Hairer: **định lý tái dựng**, **tái chuẩn hóa mô hình**, và **điểm bất động Banach**.
- Ghi công đúng cho **đường thô của Terry Lyons** (tiền đề) và **phân phối paracontrol của Gubinelli–Imkeller–Perkowski** (bộ công cụ song song độc lập).
- Xác định đúng phạm vi: lớp **SPDE parabolic dưới tới hạn**, không phải mọi SPDE và không phải bài toán Clay về Navier–Stokes 3D tất định.

**Kiến thức nền.** Phương trình nhiệt và khái niệm phương trình đạo hàm riêng; chuyển động Brown là đường liên tục nhưng không khả vi tại bất kỳ điểm nào; phân phối là phiếm hàm tuyến tính liên tục trên các hàm thử. Về tích phân ngẫu nhiên, chỉ cần hiểu "nhiễu trắng là đạo hàm của chuyển động Brown". Không cần học trước lý thuyết đường thô.

**Liên kết với các bài khác.** Đặt câu chuyện này lên bản đồ [vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/). Bài đó đã nêu SPDE của Hairer như một bài toán về tính đặt đúng (well-posedness). So sánh với [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/) (giới hạn động học tất định) và với [Caffarelli]({{ site.baseurl }}/contents/vi/chapter08/08_08_Caffarelli_PDE/) (tính chính quy của PDE phi tuyến *không* có nhiễu trắng không-thời gian).

---

## Bản đồ kiến thức nền: Phân phối, Nhiễu trắng và SPDE kỳ dị nghiên cứu gì?

### 1. Phân phối (Distributions) — lấy đạo hàm thoải mái, nhưng mất phép nhân
Trong giải tích đại học, hàm bậc thang (nhảy từ $$0$$ lên $$1$$ tại $$x = 0$$) không có đạo hàm cổ điển. **Lý thuyết phân phối** của Laurent Schwartz định nghĩa hàm suy rộng qua tích phân với hàm thử trơn $$\varphi$$: $$\langle u, \varphi \rangle = \int u(x)\varphi(x)\,dx$$. Nhờ tích phân từng phần, mọi phân phối đều khả vi vô hạn lần (đạo hàm của hàm bậc thang là hàm delta Dirac $$\delta_0$$). Cái giá phải trả: **ta không thể nhân hai phân phối thô với nhau**.

### 2. Chuyển động Brown và nhiễu trắng không-thời gian
**Chuyển động Brown** $$B_t$$ liên tục nhưng cực kỳ gồ ghề: $$\vert B_{t+h} - B_t \vert \sim \vert h \vert^{1/2}$$, tức chỉ đạt bậc Hölder $$1/2-$$ (chính xác là $$1/2 - \kappa$$ với mọi $$\kappa > 0$$). Đạo hàm theo nghĩa phân phối của nó là **nhiễu trắng** $$\xi$$ — một phân phối có độ chính quy **âm**. Với phương trình nhiệt $$\partial_t - \Delta$$, thời gian $$t$$ đếm gấp đôi không gian $$x$$ (vì $$t \sim x^2$$), nên tổng số chiều parabolic của không-thời gian $$d$$ chiều không gian là $$d + 2$$, và độ chính quy của nhiễu trắng không-thời gian rơi xuống tận:

$$
\mathrm{reg}(\xi) = -\frac{d+2}{2}-.
$$

### 3. SPDE kỳ dị đặt câu hỏi gì?
Giải tích Itô cổ điển (thập niên 1940) giải được phương trình vi phân ngẫu nhiên thường (1 chiều thời gian) nhờ tách quá khứ khỏi tương lai. Với **SPDE phi tuyến** trên không-thời gian, khi nghiệm thô đến mức số hạng phi tuyến là tích của các phân phối có tổng bậc chính quy $$\le 0$$, phương trình trở nên **kỳ dị**: ta phải tìm một quy trình **tái chuẩn hóa** (làm trơn nhiễu thành $$\xi^\varepsilon$$, trừ đi các hằng số phân kỳ rồi cho $$\varepsilon \to 0$$) để định nghĩa nghiệm một cách nội tại và duy nhất.

---

## 1. Ví dụ cầm tay chỉ việc: tại sao $$\delta_0^2$$ bùng nổ và bảng đếm bậc của KPZ, $$\Phi^4_3$$

### Ví dụ 1: Tại sao không thể bình phương hàm delta $$\delta_0$$?
Hãy xấp xỉ hàm delta Dirac $$\delta_0$$ bằng một cột hình chữ nhật rộng $$\varepsilon$$ và cao $$1/\varepsilon$$ quanh gốc $$0$$:

$$
\delta_\varepsilon(x) = \frac{1}{\varepsilon}\,\mathbf{1}_{[-\varepsilon/2,\, \varepsilon/2]}(x).
$$

Diện tích dưới cột bằng $$\varepsilon \cdot \frac{1}{\varepsilon} = 1$$ (nên $$\delta_\varepsilon \to \delta_0$$ khi $$\varepsilon \to 0$$). Bây giờ thử **bình phương** nó: cột mới vẫn rộng $$\varepsilon$$ nhưng cao tới $$1/\varepsilon^2$$, nên diện tích dưới nó là:

$$
\int_{\mathbb{R}} \delta_\varepsilon(x)^2\,dx = \varepsilon \cdot \frac{1}{\varepsilon^2} = \frac{1}{\varepsilon} \xrightarrow{\varepsilon \to 0} +\infty!
$$

Phép bình phương bùng nổ ra vô cực (và thậm chí phụ thuộc vào dáng của hàm xấp xỉ)! Quy tắc vàng của giải tích điều hòa khẳng định: tích $$u \cdot v$$ chỉ xác định chính tắc khi **tổng độ chính quy $$\mathrm{reg}(u) + \mathrm{reg}(v) > 0$$**.

### Ví dụ 2: Bảng đếm bậc chính quy cho hai "con quái vật" KPZ và $$\Phi^4_3$$
Toán tử nhiệt $$(\partial_t - \Delta)^{-1}$$ luôn **cộng thêm $$+2$$** vào độ chính quy, còn đạo hàm không gian $$\partial_x$$ **trừ đi $$-1$$**. Hãy cộng trừ trực tiếp trên bảng:

| Phương trình | Số chiều không gian $$d$$ | Bậc của nhiễu $$\xi$$ | Bậc của nghiệm (sau cộng $$+2$$) | Số hạng phi tuyến & tổng bậc |
|---|---|---|---|---|
| Nhiệt ngẫu nhiên $$\partial_t u = \Delta u + \xi$$ | $$d = 1$$ | $$-3/2-$$ | $$u \sim +1/2-$$ | Không có (tuyến tính, đặt đúng!) |
| **KPZ**: $$\partial_t h = \partial_x^2 h + (\partial_x h)^2 + \xi$$ | $$d = 1$$ | $$-3/2-$$ | $$h \sim +1/2- \implies \partial_x h \sim -1/2-$$ | $$(\partial_x h)^2$$: $$(-1/2-) + (-1/2-) = \mathbf{-1- < 0}$$ (Vỡ!) |
| **$$\Phi^4_3$$ động lực**: $$\partial_t\Phi = \Delta\Phi - \Phi^3 + \xi$$ | $$d = 3$$ | $$-5/2-$$ | $$\Phi \sim -1/2-$$ (đã là phân phối!) | $$\Phi^3$$: $$3 \times (-1/2-) = \mathbf{-3/2- < 0}$$ (Vỡ!) |

Nhìn vào bảng, ta thấy ngay con số **$$-1-$$** và **$$-3/2-$$** giải thích rành mạch vì sao cả KPZ lẫn $$\Phi^4_3$$ đều không thể định nghĩa theo cách cổ điển — và vì sao khi làm trơn nhiễu thành $$\xi^\varepsilon$$, số hạng $$(\partial_x h^\varepsilon)^2$$ lệch đi một hằng số cỡ $$C_\varepsilon \sim 1/\varepsilon$$ (cần trừ đi $$C_\varepsilon$$ để thu được giới hạn hữu hạn)!

---

## 2. Khung giải thích: Cấu trúc chính quy thuần hóa vô hạn như thế nào? (nên đọc chậm)

Martin Hairer (sinh 1975 tại Geneva, tiến sĩ vật lý năm 2001 dưới sự hướng dẫn của Jean-Pierre Eckmann) trước đó đã nổi tiếng với định lý ergodic cho Navier–Stokes ngẫu nhiên 2D (cùng Jonathan Mattingly, *Annals*, 2006) và lấy cảm hứng sâu sắc từ **lý thuyết đường thô** (*rough paths*) của **Terry Lyons**. Sau bài giải KPZ năm 2013 (*Annals*), ông công bố bộ máy tổng quát *A theory of regularity structures* (*Inventiones*, 2014; arXiv:1303.5113) hoạt động qua 4 bước:

#### Bước 1: Mở rộng đa thức Taylor bằng các "đơn thức hình cây" dựng từ nhiễu
Hàm trơn $$f \in C^\gamma$$ gần điểm $$x$$ được xấp xỉ bởi đa thức Taylor $$f(y) \approx f(x)\cdot 1 + f'(x)(y-x) + \cdots$$. Nghiệm của SPDE kỳ dị *không* trông giống đa thức ở thang nhỏ — nó trông giống các tích phân lặp của nhiễu trắng!
Hairer định nghĩa một **cấu trúc chính quy** $$(\mathcal{A}, T, G)$$ bằng cách ném thêm vào danh sách đơn thức $$1, X_i, X_i X_j, \ldots$$ một danh sách hữu hạn các **ký hiệu hình cây** (chẳng hạn ký hiệu $$\Xi$$ cho nhiễu $$\xi$$ bậc $$-5/2-$$, ký hiệu $$\mathcal{I}(\Xi)$$ cho nghiệm tuyến tính bậc $$-1/2-$$, ký hiệu $$\mathcal{I}(\Xi)^2$$ bậc $$-1-$$, $$\mathcal{I}(\Xi)^3$$ bậc $$-3/2-$$...):
- $$\mathcal{A} \subset \mathbb{R}$$: tập các bậc thuần nhất (cho phép cả bậc âm);
- $$T = \bigoplus_{\alpha \in \mathcal{A}} T_\alpha$$: không gian vector phân bậc sinh bởi đa thức và các cây nhiễu;
- $$G$$: nhóm cấu trúc chuyển tâm khai triển từ điểm $$y$$ sang điểm $$x$$ (tổng quát hóa công thức nhị thức Newton).

Trong không gian đại số $$T$$, **phép nhân hai ký hiệu chỉ đơn giản là ghép hai cây lại với nhau** — hoàn toàn hợp lệ về mặt đại số!

#### Bước 2: Mô hình $$(\Pi, \Gamma)$$ và Định lý Tái dựng (Cầu nối đại số $$\to$$ giải tích)
Một **mô hình** $$(\Pi, \Gamma)$$ gán cho mỗi ký hiệu cây $$\tau \in T$$ tại tâm $$x$$ một phân phối thật $$\Pi_x \tau$$ có độ lớn cỡ $$\lambda^{\vert\tau\vert}$$ ở thang $$\lambda$$. Một **phân phối được mô hình hóa** $$f(x) \in T$$ là bộ hệ số Taylor mở rộng biến thiên mượt theo phép chuyển tâm $$\Gamma_{xy}$$.
**Định lý Tái dựng (Reconstruction Theorem):** Nếu $$f$$ có độ chính quy dương $$\gamma > 0$$, tồn tại **duy nhất** một phân phối thật $$\mathcal{R}f \in \mathcal{S}'$$ sao cho gần mọi điểm $$x$$, $$\mathcal{R}f$$ khớp với mô hình địa phương $$\Pi_x f(x)$$ tới sai số $$\lambda^\gamma$$.

#### Bước 3: Tái chuẩn hóa mô hình (Tách riêng phần xác suất)
Khi làm trơn nhiễu thành $$\xi^\varepsilon$$, các phân phối $$\Pi^\varepsilon_x \tau$$ ứng với cây phi tuyến (như $$\mathcal{I}(\Xi)^2$$) sẽ phân kỳ khi $$\varepsilon \to 0$$. Nhờ điều kiện **dưới tới hạn** (*subcritical* — ở thang nhỏ, số hạng phi tuyến yếu hơn phần tuyến tính), chỉ có **hữu hạn** cây có bậc âm gây phân kỳ! Tác động của một nhóm tái chuẩn hóa (gắn với đại số Hopf của cây) trừ đi đúng hữu hạn hằng số phân kỳ địa phương (như $$-C_\varepsilon \Phi$$ trong $$\Phi^4_3$$), giúp mô hình đã tái chuẩn hóa $$(\hat{\Pi}^\varepsilon, \hat{\Gamma}^\varepsilon)$$ **hội tụ xác suất** về một mô hình giới hạn $$(\hat{\Pi}, \hat{\Gamma})$$. Đáng kinh ngạc là bước xác suất nặng nề này chỉ cần làm *một lần duy nhất* cho hữu hạn cây cơ sở!

#### Bước 4: Điểm bất động Banach hoàn toàn tất định
Khi đã cầm trên tay mô hình giới hạn $$(\hat{\Pi}, \hat{\Gamma})$$, toàn bộ phần còn lại trở nên **tất định 100%**: trên không gian Banach các phân phối được mô hình hóa, SPDE kỳ dị biến thành một ánh xạ co trên khoảng thời gian ngắn, giải ra điểm bất động duy nhất $$f$$ (giống phép lặp Picard cho ODE). Áp dụng toán tử tái dựng $$\mathcal{R}$$, ta thu được $$\mathcal{R}f$$ — định nghĩa nội tại và duy nhất cho nghiệm của SPDE kỳ dị!

Tóm tắt cỗ máy Hairer:

$$
\text{SPDE kỳ dị}
\;\xrightarrow{\text{cây nhiễu}}\;
\text{Đại số } (\mathcal{A}, T, G)
\;\xrightarrow{\text{tái chuẩn hóa}}\;
\text{Mô hình } (\hat{\Pi}, \hat{\Gamma})
\;\xrightarrow{\text{Picard + } \mathcal{R}}\;
\text{Nghiệm thật } \mathcal{R}f.
$$

---

## 3. Phân phối paracontrol và Đường thô: những người anh em song hành

Cần ghi công đầy đủ cho hai trụ cột song hành với cấu trúc chính quy:
- **Đường thô (Rough Paths) của Terry Lyons:** Tiên phong chứng minh rằng ODE bị lái bởi tín hiệu gồ ghề vẫn giải được theo từng đường mẫu nếu cấp thêm các tích phân lặp của tín hiệu. Cấu trúc chính quy là sự mở rộng tư tưởng đó lên nhiều chiều của PDE.
- **Phân phối paracontrol (Paracontrolled Distributions) của Massimiliano Gubinelli, Peter Imkeller và Nicolas Perkowski** (*Forum of Mathematics, Pi*, 2015; arXiv:1210.2684): Phát triển độc lập cùng thời điểm theo tinh thần **giải tích Fourier** và tích *paraproduct* của Bony, xử lý gọn gàng các phương trình như KPZ và $$\Phi^4_3$$. Đây là một bộ công cụ độc lập song song, không phải hệ quả của cấu trúc chính quy.

---

## 4. Những điều huy chương không khẳng định và vì sao lý thuyết này quan trọng

- **Không phải mọi SPDE:** Lý thuyết áp dụng cho lớp **parabolic dưới tới hạn**. Các phương trình tới hạn (như $$\Phi^4_4$$), trên tới hạn hay nhiều bài toán hyperbolic vẫn nằm ngoài phạm vi.
- **Không phải bài toán Clay về Navier–Stokes:** Kết quả Hairer–Mattingly (2006) là về tính ergodic của Navier–Stokes *ngẫu nhiên 2D*, không liên quan đến bài toán Thiên niên kỷ 3D tất định.
- **Không phải vì bằng tiến sĩ vật lý:** Tiểu sử vật lý giúp ông nhạy bén với tái chuẩn hóa, nhưng Huy chương Fields 2014 (và sau này Giải Breakthrough 2021) tôn vinh một ngôn ngữ toán học chặt chẽ đã biến các phép tính hình thức của vật lý thành định lý.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Mọi SPDE nay đều đặt đúng (well-posed)." | Chỉ một lớp lớn SPDE kỳ dị *parabolic dưới tới hạn*; đây không phải lý thuyết tồn tại cho mọi phương trình. |
| "Hairer giải Navier–Stokes." | Ông không giải bài toán Clay 3D tất định. Tính ergodic cho trường hợp 2D ngẫu nhiên là một định lý khác. |
| "Phân phối paracontrol là một phần của cấu trúc chính quy." | Gubinelli–Imkeller–Perkowski xây dựng một bộ công cụ độc lập, có liên quan. |
| "Nhiễu trắng là hàm, cứ nhân bình thường." | Nhiễu trắng là phân phối; muốn nhân phải có lý thuyết. |
| "Tái dựng chỉ là định lý Taylor." | Nó *mở rộng* Taylor: khai triển chứa các ký hiệu nhiễu, và kết quả là một phân phối. |
| "Fields được trao vì bằng tiến sĩ vật lý." | Đó là tiểu sử; lời trao giải nói về lý thuyết SPDE và cấu trúc chính quy. |

---

## Liên kết

- IMU Fields Medals 2014: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2014)
- Citation ngắn IMU (Hairer): [https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014/fields-medallists-2014-awardees-brief-citations](https://www.mathunion.org/imu-awards/fields-medal/fields-medal-2014/fields-medallists-2014-awardees-brief-citations)
- Ghi chú IMU, “The Work of Martin Hairer” (PDF): [https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_hairer.pdf](https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_hairer.pdf)
- Wikipedia — Martin Hairer: [https://en.wikipedia.org/wiki/Martin_Hairer](https://en.wikipedia.org/wiki/Martin_Hairer)
- Wikipedia — Regularity structure: [https://en.wikipedia.org/wiki/Regularity_structure](https://en.wikipedia.org/wiki/Regularity_structure)
- Hồ sơ Quanta (2014): [https://www.quantamagazine.org/in-noisy-equations-one-who-heard-music-20140812/](https://www.quantamagazine.org/in-noisy-equations-one-who-heard-music-20140812/)
- Hairer, cấu trúc chính quy (arXiv:1303.5113): [https://arxiv.org/abs/1303.5113](https://arxiv.org/abs/1303.5113)
- Gubinelli–Imkeller–Perkowski (arXiv:1210.2684): [https://arxiv.org/abs/1210.2684](https://arxiv.org/abs/1210.2684)
- Tìm arXiv — Hairer KPZ: [https://arxiv.org/search/?query=Hairer+KPZ&searchtype=all](https://arxiv.org/search/?query=Hairer+KPZ&searchtype=all)

---

## Tài liệu tham khảo

1. Citation IMU Fields Medal 2014 — Martin Hairer.
2. M. Hairer, “Solving the KPZ equation,” *Ann. of Math.* 178 (2013).
3. M. Hairer, “A theory of regularity structures,” *Invent. Math.* 198 (2014).
4. M. Gubinelli, P. Imkeller và N. Perkowski, “Paracontrolled distributions and singular PDEs,” *Forum Math. Pi* 3 (2015).
5. T. Lyons, lý thuyết rough path (tiền bối cho SDE theo đường đi).
6. M. Hairer và J. Mattingly, “Ergodicity of the 2D Navier–Stokes equations with degenerate stochastic forcing,” *Ann. of Math.* 164 (2006) — 2D ngẫu nhiên, không phải Clay 3D.
7. Khóa học: [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/), [Deng PDE]({{ site.baseurl }}/contents/vi/chapter02/02_12_Deng_PDE/).

## Hướng đi tiếp

- So sánh phép biến đổi Cole–Hopf cho KPZ với cách xây dựng bằng cấu trúc chính quy. Cách thứ nhất dựa vào một phép đổi biến đặc biệt; cách thứ hai áp dụng được cho cả những phương trình không có mẹo đó.
- Câu hỏi thảo luận: tái chuẩn hóa ở đây giống và khác tái chuẩn hóa trong lý thuyết trường lượng tử kiến thiết ở những điểm nào?

## Video tham khảo

- **Xem trước**: [Martin Hairer Colloquium Talk: Taming Infinities](https://www.youtube.com/watch?v=nBbx0wEgUXY) (Sydney Mathematical Research Institute - SMRI, tiếng Anh). Bài nói đại chúng của chính Hairer về việc "thuần hóa các đại lượng vô hạn". Nên xem trước để nắm vì sao tích các phân phối gây khó và tái chuẩn hóa làm gì.
- [Martin Hairer Mini-course 1: Introduction to Regularity Structures](https://www.youtube.com/watch?v=c0HlcVA1SoI) (Sydney Mathematical Research Institute - SMRI, tiếng Anh). Buổi đầu của một khóa ngắn giới thiệu cấu trúc chính quy. Nên xem sau khi đã đọc xong mục 3 và 4.
- [Martin Hairer: Fine properties of random fields: from fluids to QTF](https://www.youtube.com/watch?v=VnmfSICGDo4) (Centre International de Rencontres Mathématiques, tiếng Anh). Bài giảng về tính chất tinh tế của trường ngẫu nhiên, từ chất lỏng đến lý thuyết trường lượng tử. Dùng làm góc nhìn bổ sung sau hai video đầu.
