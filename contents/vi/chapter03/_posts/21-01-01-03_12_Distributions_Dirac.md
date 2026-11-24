---
layout: post
title: "Phân bố: Làm cho Dirac trung thực"
chapter: '03'
order: 12
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
---

Năm 1930, khi viết cuốn sách kinh điển về cơ học lượng tử, nhà vật lý Paul Dirac thản nhiên giới thiệu một "hàm số" kỳ quái ký hiệu là $$\delta(x)$$: nó bằng $$0$$ ở mọi điểm khác $$0$$, vọt lên $$+\infty$$ ngay tại $$x=0$$, thế nhưng diện tích nằm dưới chiếc gai nhọn vô hạn ấy lại bằng đúng $$1$$!

Các nhà toán học giải tích cổ điển lập tức phản đối kịch liệt: theo lý thuyết tích phân Lebesgue chặt chẽ, một hàm số bằng $$0$$ khắp nơi trừ đúng một điểm *bắt buộc* phải có tích phân bằng $$0$$, tuyệt đối không thể bằng $$1$$! Thế nhưng trớ trêu thay, "hàm bất hợp lệ" của Dirac lại hoạt động mượt mà đến kinh ngạc — không chỉ trong cơ học lượng tử mà còn trong toàn bộ kỹ thuật điện, xử lý tín hiệu và điện từ học.

Hai mươi năm sau, nhà toán học Pháp Laurent Schwartz đã giành Huy chương Fields (1950) khi chứng minh rằng Dirac không hề phá vỡ toán học — ông chỉ vô tình mở cánh cửa bước vào một thế giới rộng lớn hơn hàm số thông thường: **Lý thuyết phân bố (hay hàm suy rộng)**. Trong thế giới mới ấy, mọi hàm khả tích địa phương đều có đạo hàm đến vô hạn cấp, xung Dirac $$\delta$$ trở thành một đối tượng hoàn toàn hợp pháp, và biến đổi Fourier được giải phóng khỏi những điều kiện hội tụ chật hẹp.

Đây là bài mở đầu cho mạch Cầu nối về chủ đề "kiểm soát cái vô hạn": **vật lý cần gì, toán học cung cấp gì, và đâu là ranh giới an toàn khi tính toán**. Nên đọc kèm [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), [Hilbert / cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), và [bài tổng quan về vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích vì sao $$\delta$$ không phải là một phần tử của $$L^1_{\mathrm{loc}}$$, nhưng vẫn "tác động" được lên các hàm thử trơn.
- Định nghĩa **phân bố** là một phiếm hàm tuyến tính liên tục trên không gian hàm thử (ký hiệu: $$T(\varphi)=\langle T,\varphi\rangle$$).
- Lấy đạo hàm theo nghĩa phân bố: $$\langle T',\varphi\rangle=-\langle T,\varphi'\rangle$$.
- Phát biểu ý chính về biến đổi Fourier của phân bố tăng chậm và giải thích vì sao nó quan trọng với PDE và với các lập luận gần đúng trong lý thuyết trường lượng tử.
- Phân biệt các đẳng thức Dirac hình thức (cần thêm giả thiết) với các đẳng thức phân bố chặt chẽ.
- Hiểu vai trò của phân bố như lớp nền chặt chẽ cho các ký hiệu liên tục trong cơ học lượng tử và lý thuyết trường.

**Kiến thức nền.** Giải tích một biến; tích phân từng phần. Biết giải tích nhiều biến sẽ có ích. Không cần lý thuyết độ đo để theo dõi bài này.

---

## Bản đồ kiến thức nền: Lý thuyết phân bố (Hàm suy rộng) là gì và nghiên cứu những gì?

Trong giải tích cổ điển, ta định nghĩa một hàm số $$f$$ bằng cách chỉ rõ **giá trị của nó tại từng điểm riêng lẻ** $$x \mapsto f(x)$$. Cách nhìn này gặp bế tắc ngay lập tức với những đối tượng vật lý cực kỳ tự nhiên: một cú gõ búa tức thời (lực xung), một hạt electron coi như điện tích điểm, hay một công tắc bật tắt đột ngột (bước nhảy không có đạo hàm tại $$t=0$$).

Ý tưởng thiên tài của **lý thuyết phân bố (distribution theory)** là **đảo ngược cách định nghĩa** giống hệt cách các thiết bị đo vật lý thực tế hoạt động:
- Một chiếc nhiệt kế thật không bao giờ đo được nhiệt độ tại *một điểm toán học có thể tích bằng 0*; nó luôn đo **trung bình có trọng số** trên một vùng nhỏ trơn tru quanh đầu cảm biến: $$\int f(x)\,\varphi(x)\,dx$$.
- Thay vì hỏi *"đối tượng $$T$$ có giá trị bao nhiêu tại điểm $$x$$?"*, ta định nghĩa $$T$$ hoàn toàn thông qua **kết quả đo $$\langle T, \varphi \rangle$$ khi cho nó tương tác với mọi "cảm biến siêu trơn" (hàm thử $$\varphi$$)**.

Nhờ cú xoay góc nhìn đối ngẫu này, toàn bộ giải tích được nới rộng mà không mất đi một chút chặt chẽ nào: những đối tượng "nhọn vô hạn" hay "gãy khúc" giờ đều được cộng, lấy đạo hàm vô hạn lần và biến đổi Fourier một cách hoàn toàn hợp pháp.

---

## 1. Nhu cầu từ vật lý và kỹ thuật

Lực xung khi vợt tennis đập vào bóng, mật độ điện tích của một hạt điểm, **hàm Green**, hay "trạng thái riêng của vị trí" trong cơ học lượng tử đều vượt khỏi phạm vi hàm số cổ điển.

**Ví dụ trực quan trong kỹ thuật âm thanh (Đáp ứng xung).** Làm sao một kỹ sư âm thanh đo được đặc tính vang dội của một nhà hát lớn để giả lập nó trong phần mềm? Họ nổ một quả bóng bay (một tiếng nổ cực ngắn xấp xỉ xung Dirac $$\delta(t)$$) rồi ghi âm lại tiếng vọng — đó chính là **đáp ứng xung** $$h(t)$$ (hay hàm Green của hệ). Vì mọi bản nhạc $$u(t)$$ đều có thể xem là tổng của vô số xung $$\delta$$ dịch chuyển nối tiếp nhau, âm thanh phát ra trong nhà hát chỉ đơn giản là phép **tích chập** $$u * h$$! Tương tự trong PDE, nếu tìm được hàm Green $$G$$ thỏa mãn $$-\Delta G = \delta$$, ta giải được phương trình Poisson $$-\Delta u = f$$ cho *mọi* nguồn $$f$$ chỉ bằng tích chập $$u = G * f$$.

Ký hiệu Dirac giúp viết gọn những điều đó một cách thần kỳ. Cái giá phải trả là câu "$$\delta$$ là một hàm số" bị sai về mặt logic cổ điển. Cách giải quyết của toán học là **nâng cấp khái niệm đối tượng**, chứ không cố ép $$\delta$$ vào $$L^1$$.

---

## 2. Hàm thử và phân bố

Cố định một tập mở $$\Omega\subset\mathbb{R}^n$$. **Không gian hàm thử** $$\mathcal{D}(\Omega)=C_c^\infty(\Omega)$$ gồm tất cả các hàm trơn vô hạn lần và bằng $$0$$ ở bên ngoài một tập đóng bị chặn (giá compact) — bạn có thể xem mỗi $$\varphi\in\mathcal{D}(\Omega)$$ như một "cảm biến đo đạc cực kỳ êm dịu" tắt hẳn ở xa.

Một **phân bố** $$T\in\mathcal{D}'(\Omega)$$ là một phiếm hàm tuyến tính liên tục $$T:\mathcal{D}(\Omega)\to\mathbb{C}$$.

- **Mọi hàm số thông thường đều là phân bố:** với bất kỳ hàm khả tích địa phương $$f\in L^1_{\mathrm{loc}}(\Omega)$$, ta gắn nó với phiếm hàm:
$$
\langle f,\varphi\rangle = \int_\Omega f(x)\,\varphi(x)\,dx.
$$
- **Phân bố Dirac tại điểm $$a\in\Omega$$:** thay vì cố viết một công thức tích phân bất khả thi, ta định nghĩa trực tiếp tác động của nó lên cảm biến $$\varphi$$ là **đọc đúng giá trị của $$\varphi$$ tại điểm $$a$$**:
$$
\langle \delta_a,\varphi\rangle = \varphi(a).
$$

**Trực giác giới hạn bằng hình chuông Gauss.** Xét họ hàm chuông chuẩn $$g_\varepsilon(x) = \frac{1}{\sqrt{2\pi}\,\varepsilon}e^{-x^2/(2\varepsilon^2)}$$. Với mọi $$\varepsilon > 0$$, $$g_\varepsilon$$ là hàm trơn bình thường có diện tích luôn bằng $$1$$. Khi $$\varepsilon \to 0^+$$, chuông co hẹp lại và nhọn vút lên tại $$0$$; giới hạn điểm của nó không ra hàm cổ điển nào, nhưng giới hạn *tác động lên mọi hàm thử* lại hội tụ đẹp tuyệt đối: $$\lim_{\varepsilon\to 0^+} \int g_\varepsilon(x)\varphi(x)\,dx = \varphi(0) = \langle \delta_0, \varphi\rangle$$!

---

## 3. Đạo hàm luôn tồn tại

Làm sao lấy đạo hàm một hàm bị đứt gãy hay một xung $$\delta$$? Bí quyết lấy thẳng từ **tích phân từng phần** ở giải tích năm nhất! Với hai hàm trơn $$f$$ và $$\varphi$$ (biết $$\varphi$$ bằng 0 ở xa vô cực nên số hạng biên triệt tiêu), ta luôn có:

$$
\int f'(x)\,\varphi(x)\,dx = -\int f(x)\,\varphi'(x)\,dx.
$$

Laurent Schwartz biến đẳng thức đó thành **định nghĩa đạo hàm phân bố** cho mọi $$T \in \mathcal{D}'$$:

$$
\langle \partial_i T,\varphi\rangle = -\langle T,\partial_i \varphi\rangle.
$$

**Ví dụ chứng minh siêu gọn: đạo hàm của bước nhảy Heaviside chính là xung Dirac!** Xét hàm bậc thang $$H(x) = 0$$ khi $$x < 0$$ và $$H(x) = 1$$ khi $$x \ge 0$$ (không có đạo hàm cổ điển tại $$x=0$$). Áp dụng định nghĩa phân bố cho mọi hàm thử $$\varphi \in C_c^\infty(\mathbb{R})$$:

$$
\langle H', \varphi \rangle = -\langle H, \varphi' \rangle = -\int_0^{+\infty} \varphi'(x)\,dx = -\bigl[\varphi(+\infty) - \varphi(0)\bigr] = \varphi(0) = \langle \delta_0, \varphi \rangle.
$$

Vậy $$H' = \delta_0$$ một cách **chặt chẽ 100%**! Hệ quả chấn động: mọi phân bố đều khả vi vô hạn lần theo nghĩa yếu, và khái niệm **nghiệm yếu (weak solution)** của PDE — vốn là nền tảng cho phương pháp phần tử hữu hạn (FEM) lẫn bài toán Thiên niên kỷ [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/) — chính là nghiệm hiểu trong $$\mathcal{D}'$$.

**Chuỗi lập luận ngắn.** Nguồn điểm và bước nhảy trở nên hoàn toàn hợp lệ khi ta đẩy gánh nặng lấy đạo hàm sang **hàm thử siêu trơn $$\varphi$$**, thay vì cố lấy đạo hàm trực tiếp lên đối tượng kỳ dị.

---

## 4. Phép nhân, tập sóng trước và vùng nguy hiểm

Dù lý thuyết phân bố cực kỳ mạnh, nó vẫn có một giới hạn quan trọng cần nhớ để không tính sai:
- **An toàn:** cộng hai phân bố, lấy đạo hàm cấp bất kỳ, tích chập với hàm trơn, hoặc **nhân một phân bố với một hàm trơn** (ví dụ $$f(x)\delta_0 = f(0)\delta_0$$).
- **Vùng nguy hiểm:** **nhân hai phân bố kỳ dị với nhau** nói chung không xác định được (ví dụ $$\delta(x)^2$$ vô nghĩa trong $$\mathcal{D}'$$!).

Giải tích vi địa phương (khái niệm **tập sóng trước — wavefront set** của Lars Hörmander) cho biết chính xác điều kiện hình học khi nào tích hai phân bố có nghĩa. Đây chính là rào cản toán học sâu xa mà kỹ thuật **tái chuẩn hóa (renormalization)** trong lý thuyết trường lượng tử phải vượt qua khi nhân các trường lượng tử tại cùng một điểm không–thời gian.

**Quy tắc khi thảo luận.** Toán tử tuyến tính với hệ số trơn: hoàn toàn an toàn trong khuôn khổ phân bố. Phép toán phi tuyến và tích tại điểm của các đối tượng kỳ dị: bắt buộc phải có thêm cấu trúc giải tích.

---

## 5. Phân bố tăng chậm và biến đổi Fourier

Trong giải tích cổ điển, biến đổi Fourier đòi hỏi hàm phải khả tích ($$f \in L^1$$) — nên thậm chí một hàm hằng $$f(x)=1$$ hay sóng sin $$\cos(x)$$ thuần túy cũng không có biến đổi Fourier cổ điển!

Giải pháp của Schwartz là chọn không gian hàm thử rộng hơn một chút gọi là **không gian Schwartz $$\mathcal{S}$$** (các hàm trơn giảm nhanh hơn mọi lũy thừa khi $$\lvert x\rvert \to \infty$$, như hàm Gauss $$e^{-x^2}$$). Biến đổi Fourier biến $$\mathcal{S}$$ thành chính $$\mathcal{S}$$. Không gian đối ngẫu $$\mathcal{S}'$$ gồm các **phân bố tăng chậm (tempered distributions)** — bao trùm cả đa thức, sóng sin/cosin lẫn xung $$\delta$$!

Bằng định nghĩa đối ngẫu $$\langle \widehat{T}, \varphi \rangle = \langle T, \widehat{\varphi} \rangle$$, ta thu ngay đẳng thức kinh điển của kỹ thuật tín hiệu:

$$
\widehat{\delta_0}(\xi) = 1 \qquad \text{và} \qquad \widehat{1}(\xi) = \delta_0(\xi).
$$

Ý nghĩa vật lý tuyệt đẹp: một tiếng nổ siêu ngắn $$\delta(t)$$ chứa **đều tất cả mọi tần số** với biên độ bằng $$1$$; ngược lại một tín hiệu hằng bất biến theo thời gian chỉ tập trung toàn bộ năng lượng tại đúng tần số $$0$$! ([Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/)).

---

## 6. Ký hiệu trong cơ học lượng tử và lý thuyết trường

Trong sách vật lý lượng tử, ket vị trí $$\lvert x\rangle$$ và đẳng thức trực giao liên tục $$\langle x\vert x'\rangle=\delta(x-x')$$ thực chất là các đối tượng nằm ngoài không gian Hilbert $$L^2$$ (không thể chuẩn hóa tích phân bình phương bằng 1). Cách đặt nền móng chặt chẽ là dùng định lý phổ (độ đo giá trị phép chiếu) hoặc **không gian Hilbert được trang bị (rigged Hilbert space)** kẹp giữa ba tầng: $$\mathcal{S}\subset L^2\subset\mathcal{S}'$$ ([Hilbert / cơ học lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/)).

Trong lý thuyết trường lượng tử, các trường lượng tử tự bản thân chúng cũng là các **phân bố có giá trị toán tử** (tiên đề Wightman). Khó khăn lớn nhất về mặt toán học luôn nằm ở khâu nhân các phân bố đó lại với nhau (tái chuẩn hóa); xem thêm [tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/) và [nhóm tái chuẩn hóa]({{ site.baseurl }}/contents/vi/chapter06/06_22_Renormalization_Group/).

---

## 7. Phân biệt chính xác và cường điệu

| Khẳng định | Đánh giá | Sửa lại |
|------------|------|-----|
| "$$\delta$$ là hàm bằng vô cùng tại 0." | Chỉ là cách nói gần đúng | $$\delta$$ là một phân bố, không phải hàm số cổ điển. |
| "Lý thuyết phân bố làm cho mọi tính toán hình thức của vật lý trở nên chặt chẽ." | Sai | Phép nhân và các phép toán phi tuyến có thể không xác định. |
| "Nghiệm yếu là nghiệm giả." | Gây hiểu nhầm | Đó là nghiệm theo một nghĩa đối ngẫu chính xác; tính duy nhất và độ trơn là những câu hỏi riêng. |
| "Kỹ sư dùng $$\delta$$ là thiếu toán học." | Không công bằng | Phép tính với xung được biện minh bằng lý thuyết phân bố (hoặc biến đổi Laplace) với các giả thiết được nêu rõ. |

---

## Tài liệu tham khảo

1. Strichartz — *A Guide to Distribution Theory and Fourier Transforms*.  
2. Khóa học: [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/), [Hilbert / QM]({{ site.baseurl }}/contents/vi/chapter06/06_18_Hilbert_Spectral_QM/), [Tích phân đường]({{ site.baseurl }}/contents/vi/chapter06/06_20_Path_Integrals_Math_Status/), [Vật lý toán]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/).  
