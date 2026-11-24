---
layout: post
title: "Ngô Bảo Châu và Bổ đề Cơ bản (Huy chương Fields 2010)"
chapter: '02'
order: 4
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Mùa đông năm 1967, một nhà toán học trẻ người Canada tên là Robert Langlands ngồi viết một bức thư tay dài 17 trang gửi cho André Weil. Ở đầu thư, ông khiêm tốn nhắn: *"Nếu ông sẵn lòng đọc nó như một tập hợp những suy đoán thuần túy, tôi sẽ vô cùng cảm kích; còn nếu không, chắc hẳn ông có sẵn một cái sọt rác ngay trong tầm tay."* André Weil đã không vứt bức thư ấy vào sọt rác. Nó trở thành bản tuyên ngôn của **chương trình Langlands** — mạng lưới giả thuyết đồ sộ đến mức giới toán học gọi là *"Lý thuyết Đại Thống nhất của toán học"*. Langlands tin rằng hai thế giới tưởng chừng không có chung tiếng nói — thế giới rời rạc của **lý thuyết số** (nghiệm phương trình đa thức, số nguyên tố, đối xứng Galois) và thế giới liên tục của **giải tích điều hòa** (sóng, phổ, dạng tự đẳng cấu) — thực ra đang kể cùng một câu chuyện bằng hai ngôn ngữ khác nhau.

Thế nhưng, trong suốt gần ba thập kỷ, rất nhiều định lý quan trọng bậc nhất của chương trình ấy đều phải treo một dấu ngoặc đầy day dứt ở dòng đầu tiên: *"Giả sử Bổ đề Cơ bản là đúng..."* Chỉ một đẳng thức tích phân địa phương, ban đầu bị tưởng là một bước kiểm tra kỹ thuật phụ nên mới mang cái tên khiêm nhường là **"Bổ đề Cơ bản"** (*Fundamental Lemma*), lại trở thành tảng đá chắn ngang toàn bộ xa lộ. Mọi nỗ lực tính trực tiếp tích phân ấy đều bế tắc ngay khi cỡ ma trận vượt quá 3 hay 4.

Mãi đến cuối thập niên 2000, **Ngô Bảo Châu** (khi đó làm việc tại Université Paris-Sud) đã chọn một lối đi hoàn toàn khác: thay vì cố gắng tính một tích phân $$p$$-adic rối rắm, ông dịch toàn bộ đẳng thức giải tích đó sang ngôn ngữ của **hình học đại số**, biến những con số bí ẩn thành hình dạng của một họ không gian hình học gọi là **phân thớ Hitchin**. Bước ngoặt ấy đã chứng minh trọn vẹn Bổ đề Cơ bản, tháo gỡ nút thắt gần 30 năm và mang về cho ông **Huy chương Fields 2010**. Cần phân biệt rạch ròi ngay từ đầu: Ngô Bảo Châu không "sáng lập" chương trình Langlands, và chứng minh của ông cũng không khép lại toàn bộ chương trình; nhưng nó đã gỡ bỏ chữ *"giả sử"* khỏi hàng loạt định lý trụ cột của toán học hiện đại.

**Mạch bài học:** Bản đồ kiến thức nền (hình học đại số, số $$p$$-adic, giải tích trên nhóm) → Tầm nhìn Langlands qua ví dụ số nhỏ → Công thức vết và bài toán nội soi bằng ma trận $$2\times 2$$ → Bổ đề Cơ bản → Khung giải thích chậm: từ tích phân đến phân thớ Hitchin và vết Frobenius → Laumon–Ngô đến Ngô (2010) → Hệ quả & phân biệt Langlands số học với Langlands hình học.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Đặt Bổ đề Cơ bản vào chương trình Langlands và vào bộ máy công thức vết Arthur–Selberg.
- Giải thích trực giác vì sao hai ma trận đồng dạng trên $$\mathbb{C}$$ nhưng không đồng dạng trên $$\mathbb{R}$$ (hoặc $$\mathbb{Q}_p$$) lại sinh ra **lý thuyết nội soi** (endoscopy).
- Hiểu được bước chuyển ngôn ngữ cốt lõi: vì sao **đếm điểm trên trường hữu hạn** và **hình học phân thớ Hitchin** có thể chứng minh một đẳng thức tích phân $$p$$-adic.
- Phân biệt kết quả của **Laumon–Ngô (2004)** (cho nhóm unita) với định lý tổng quát của **Ngô (2010)** (cho đại số Lie tổng quát).
- Phân biệt rõ **Langlands số học** với **Langlands hình học**, và tránh nhầm lẫn giữa **Giải Abel 2018** của Robert Langlands với **Huy chương Fields 2010** của Ngô Bảo Châu.

**Kiến thức cần có.** Ma trận, vết (trace), định thức, đa thức đặc trưng từ đại số tuyến tính đại học; đồng dư modulo $$p$$ cơ bản. Không cần biết trước về hình học đại số, số $$p$$-adic hay dạng tự đẳng cấu — tất cả đều được giới thiệu bằng ví dụ cụ thể ngay bên dưới.

---

## Bản đồ kiến thức nền: Hình học đại số, Số $$p$$-adic và Giải tích trên nhóm là gì?

Trước khi bước vào câu chuyện của Langlands và Ngô Bảo Châu, hãy dừng lại ít phút để làm quen với ba lĩnh vực xuất hiện xuyên suốt bài học. Nếu bạn có nền tảng đại học về giải tích và đại số tuyến tính, cả ba đều có điểm xuất phát rất gần gũi:

### 1. Hình học đại số (Algebraic Geometry) là gì và nghiên cứu những gì?

Ở phổ thông và năm nhất đại học, bạn đã quen với việc mô tả hình dạng bằng phương trình đa thức: $$x^2 + y^2 = 1$$ là đường tròn, $$y = x^2$$ là parabol, $$x^2 + y^2 - z^2 = 1$$ là mặt hyperboloid một tầng. **Hình học đại số** mở rộng ý tưởng đó lên mọi hệ phương trình đa thức nhiều ẩn, trong không gian nhiều chiều, và quan trọng nhất: **trên mọi hệ số** — không chỉ số thực $$\mathbb{R}$$ hay số phức $$\mathbb{C}$$, mà cả **trường hữu hạn** $$\mathbb{F}_p = \{0, 1, \dots, p-1\}$$ (nơi phép cộng, trừ, nhân, chia thực hiện theo modulo số nguyên tố $$p$$).

Ngành hình học đại số tập trung vào bốn câu hỏi lớn:
- **Phân loại hình dạng (Đa tạp đại số):** Tập nghiệm của hệ đa thức có mấy thành phần? Có bao nhiêu "lỗ" (giống $$g$$)? Có thể đưa mọi hình dạng phức tạp về vài khối gạch cơ bản không (chương trình mô hình tối thiểu)?
- **Điểm kỳ dị (Singularities):** Chỗ nào trên hình dạng bị nhọn, tự cắt nhau hay bóp méo (như đỉnh hình nón $$x^2 + y^2 = z^2$$ tại gốc tọa độ)? Làm sao "gỡ rối" (giải kỳ dị) chúng?
- **Không gian tham số (Moduli spaces):** Khi ta thay đổi hệ số của phương trình, bản thân *tập hợp tất cả các hình dạng* lại tạo thành một không gian hình học mới — phân thớ Hitchin trong chứng minh của Ngô là một thành viên nổi tiếng của họ này.
- **Hình học số học (Arithmetic Geometry):** Phương trình đa thức có bao nhiêu nghiệm nguyên, nghiệm hữu tỷ, hay nghiệm trên trường hữu hạn $$\mathbb{F}_p$$? Một phép màu của thế kỷ XX (Weil, Grothendieck, Deligne) cho thấy: để đếm số nghiệm trên $$\mathbb{F}_p$$, ta không cần ngồi đếm từng nghiệm một — ta có thể đọc nó từ **đối đồng điều** (những bất biến đại số đo số chiều và số lỗ của hình dạng).

Ngoài toán thuần túy, hình học đại số còn là nền tảng của **mật mã đường cong elliptic (ECC)** bảo vệ giao dịch ngân hàng và HTTPS, **mã sửa lỗi hình học đại số** trong truyền thông vệ tinh, và bài toán **động học ngược của cánh tay robot** (vốn là giải hệ phương trình đa thức nhiều biến).

### 2. Số $$p$$-adic là gì — tại sao cần một cách đo "khoảng cách" mới?

Trong giải tích thông thường, hai số $$1$$ và $$2$$ gần nhau hơn $$1$$ và $$26$$ vì $$\vert 2 - 1 \vert = 1 < \vert 26 - 1 \vert = 25$$. Nhưng với một nhà lý thuyết số đang nghiên cứu tính chia hết cho số nguyên tố $$p = 5$$, điều ngược lại mới thú vị: $$26 - 1 = 25 = 5^2$$ chia hết cho lũy thừa cao của $$5$$!

Nếu ta định nghĩa một "thước đo $$5$$-adic" mới: một số càng chia hết cho lũy thừa cao $$5^k$$ thì nó càng **nhỏ**, cụ thể $$\vert 5^k \cdot m \vert_5 = 5^{-k}$$ (với $$m$$ không chia hết cho $$5$$), thì:

$$
\vert 2 - 1 \vert_5 = 1, \qquad \vert 26 - 1 \vert_5 = \vert 25 \vert_5 = \frac{1}{25} = 0.04, \qquad \vert 626 - 1 \vert_5 = \vert 5^4 \vert_5 = \frac{1}{625} = 0.0016.
$$

Khi "điền đầy" các lỗ hổng của số hữu tỷ $$\mathbb{Q}$$ theo thước đo thông thường, ta được trục số thực $$\mathbb{R}$$. Khi điền đầy $$\mathbb{Q}$$ theo thước đo $$p$$-adic, ta được **trường số $$p$$-adic** $$\mathbb{Q}_p$$ — một thế giới giải tích hoàn toàn mới nơi ta vẫn tính được đạo hàm và tích phân, nhưng hình học mang cấu trúc phân nhánh dạng cây! Gom $$\mathbb{R}$$ và tất cả các $$\mathbb{Q}_p$$ (với mọi số nguyên tố $$p = 2, 3, 5, 7, \dots$$) vào chung một mái nhà, ta có **vành adele** $$\mathbb{A}$$.

### 3. Giải tích điều hòa trên nhóm ma trận (Dạng tự đẳng cấu)

Trong đại học, bạn học **chuỗi Fourier**: mọi hàm tuần hoàn trên đường tròn $$S^1$$ đều phân tích được thành tổng các "sóng cơ bản" $$e^{2\pi i n x}$$. **Giải tích điều hòa hiện đại** làm đúng việc đó, nhưng thay đường tròn đơn giản bằng các **nhóm ma trận** giàu đối xứng (gọi là *nhóm rút gọn được*, như $$\mathrm{GL}_n$$ gồm ma trận khả nghịch $$n\times n$$, $$\mathrm{SL}_n$$ có định thức 1, hay nhóm unita $$U(n)$$) với hệ số trên $$\mathbb{R}$$ và $$\mathbb{Q}_p$$. Những "sóng cơ bản" bất biến dưới các phép đối xứng số học trên các nhóm đó chính là **dạng tự đẳng cấu** (*automorphic forms*).

---

## 1. Chương trình Langlands trong một trang — bắt đầu từ một ví dụ nhỏ

Trong những năm 1960–1970, **Robert Langlands** đề xuất một mạng lưới giả thuyết rộng lớn nối hai thế giới:

- **Phía giải tích:** các **dạng tự đẳng cấu / biểu diễn tự đẳng cấu** của nhóm rút gọn được $$G(\mathbb{A})$$;
- **Phía số học:** các **biểu diễn Galois** (mã hóa tính đối xứng của nghiệm các phương trình đa thức);

thông qua các hệ **hàm $$L$$** tương thích với nhau.

![Cầu Langlands]({{ site.baseurl }}/img/chapter_img/ngo_langlands_bridge.svg)

*Hình. Sơ đồ tương ứng Langlands, với hàm $$L$$ làm cầu nối.*

### Hai ví dụ cầm tay chỉ việc để thấy "phép màu" Langlands

1. **Bậc 1 ($$\mathrm{GL}_1$$ — Luật tương hỗ bậc hai):** Hãy xét phương trình đa thức đơn giản $$x^2 + 1 = 0$$ và thử giải nó theo modulo từng số nguyên tố lẻ $$p$$:
   - Với $$p = 3$$: $$0^2+1=1,\ 1^2+1=2,\ 2^2+1=5\equiv 2 \pmod 3$$ → **vô nghiệm**.
   - Với $$p = 5$$: $$2^2 + 1 = 5 \equiv 0 \pmod 5$$ → **có nghiệm** ($$x = 2, 3$$).
   - Với $$p = 7$$: thử $$0..6$$ đều không ra $$0 \pmod 7$$ → **vô nghiệm**.
   - Với $$p = 13$$: $$5^2 + 1 = 26 \equiv 0 \pmod{13}$$ → **có nghiệm** ($$x = 5, 8$$).

   Lập bảng dài ra, ta thấy một quy luật kỳ lạ: $$x^2 + 1 \equiv 0 \pmod p$$ có nghiệm khi và chỉ khi $$p \equiv 1 \pmod 4$$! Nói theo ngôn ngữ Langlands: một câu hỏi thuần túy **số học** ("phương trình có nghiệm modulo $$p$$ không?") được điều khiển hoàn toàn bởi một hàm **tuần hoàn** cực kỳ đơn giản theo modulo 4 ($$+1$$ nếu $$p\equiv 1\pmod 4$$, $$-1$$ nếu $$p\equiv 3\pmod 4$$).

2. **Bậc 2 ($$\mathrm{GL}_2$$ — Đường cong elliptic và dạng modular):** Xét phương trình bậc ba $$E:\ y^2 + y = x^3 - x^2$$. Với mỗi số nguyên tố $$p$$, gọi $$N_p$$ là số cặp $$(x, y) \in \mathbb{F}_p^2$$ thỏa mãn phương trình và đặt độ lệch $$a_p = p - N_p$$. Nếu bạn ngồi lập bảng tính $$a_p$$ cho $$p = 2, 3, 5, 7, 11, \dots$$, bạn nhận được dãy số $$-2, -1, 1, -2, 1, \dots$$ tưởng chừng hỗn loạn. Thế nhưng nếu bạn bung một hàm giải tích thuần túy (một **dạng modular** bậc 2):

   $$
   f(q) = q \prod_{n=1}^{\infty} (1 - q^n)^2 (1 - q^{11n})^2 = q - 2q^2 - q^3 + 2q^4 + q^5 + 2q^6 - 2q^7 - 2q^9 - 2q^{10} + q^{11} + \cdots
   $$

   hãy nhìn hệ số đứng trước $$q^p$$: tại $$q^2$$ là $$-2$$, tại $$q^3$$ là $$-1$$, tại $$q^5$$ là $$+1$$, tại $$q^7$$ là $$-2$$, tại $$q^{11}$$ là $$+1$$ — **trùng khít từng con số một** với $$a_p$$ của đường cong elliptic!! (Đây chính là nội dung Định lý Modular mà Andrew Wiles và cộng sự chứng minh để giải Định lý lớn Fermat.)

Langlands dự đoán rằng sự trùng khớp kỳ diệu này không chỉ là may mắn ở bậc 1 hay bậc 2: với **mọi** phương trình đa thức nhiều ẩn và **mọi** nhóm ma trận $$G$$, luôn tồn tại một cuốn từ điển nối thế giới số học với thế giới sóng tự đẳng cấu.

Một hình ảnh dễ nhớ cho toàn bộ bài học: **Langlands** vẽ bản đồ các xa lộ nối số học và giải tích; **lý thuyết nội soi** là quy tắc chuyển làn giữa các nhóm ma trận khác nhau; còn **Bổ đề Cơ bản** là chiếc cầu vượt còn thiếu — chừng nào chưa xây xong chiếc cầu này, hàng loạt tuyến xa lộ chỉ được mở "có điều kiện".

---

### Video ngắn 1: Ngô Bảo Châu & Bổ đề Cơ bản (Tổng quan)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/langlands-fundamental-lemma_vi.mp4"></video>
</div>

Video dài khoảng 1 phút 51 giây (có thuyết minh tiếng Việt giọng Algenib): chương trình Langlands nối giải tích tự đẳng cấu với biểu diễn Galois, nút thắt nội soi trong công thức vết Arthur–Selberg, và hướng chuyển ngôn ngữ sang hình học đại số.

## 2. Công thức vết Arthur–Selberg và bài toán nội soi (qua ví dụ ma trận $$2\times 2$$)

Làm sao chứng minh hai thế giới (hoặc hai nhóm ma trận $$G$$ và $$H$$) có chung các "sóng tự đẳng cấu" khi ta không thể liệt kê hết tất cả chúng? Các nhà toán học dùng một ý tưởng bắt nguồn ngay từ đại số tuyến tính năm nhất: **tính vết (trace) của một ma trận theo hai cách**.

Với một ma trận $$M$$ cỡ $$n\times n$$, vết $$\operatorname{tr}(M)$$ bằng:
- **Cách 1 (Phía hình học):** tổng các phần tử nằm trên đường chéo chính $$\sum M_{ii}$$;
- **Cách 2 (Phía phổ):** tổng tất cả các giá trị riêng $$\sum \lambda_k$$.

**Công thức vết Arthur–Selberg** nâng đẳng thức đơn giản ấy lên không gian vô hạn chiều của các dạng tự đẳng cấu trên nhóm $$G$$:

$$
\underbrace{\sum_{\pi} m(\pi)\,\operatorname{tr}\pi(f)}_{\text{Phía phổ (dạng tự đẳng cấu)}}
\;=\;
\underbrace{\sum_{\gamma} \operatorname{vol}(G_\gamma)\, O_\gamma(f)}_{\text{Phía hình học (tích phân quỹ đạo)}}.
$$

Ở vế phải, **tích phân quỹ đạo** $$O_\gamma(f)$$ là giá trị trung bình của hàm thử $$f$$ lấy trên toàn bộ **lớp liên hợp** $$\{g^{-1}\gamma g : g \in G\}$$ của phần tử $$\gamma$$ (trong đại số tuyến tính, đó chính là tập hợp mọi ma trận đồng dạng với $$\gamma$$).

![Nút thắt công thức vết]({{ site.baseurl }}/img/chapter_img/ngo_trace_formula_bottleneck.svg)

*Hình. Nếu chưa có đẳng thức giữa các tích phân quỹ đạo, phép chuyển nội soi vẫn phải kèm điều kiện.*

### Tại sao lại xuất hiện "lý thuyết nội soi" (Endoscopy)? Hãy xem một ví dụ $$2\times 2$$!

Trong nhóm $$\mathrm{GL}_2(\mathbb{R})$$, hai ma trận có cùng đa thức đặc trưng (với hai nghiệm phân biệt) thì luôn đồng dạng với nhau. Nhưng khi chuyển sang nhóm nhỏ hơn một chút là $$\mathrm{SL}_2(\mathbb{R})$$ (các ma trận $$2\times 2$$ thực có định thức bằng 1), một hiện tượng tinh tế bất ngờ xảy ra! Hãy xét hai ma trận quay $$90^\circ$$ ngược chiều nhau:

$$
\gamma_1 = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad \gamma_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}.
$$

Cả hai đều có định thức $$1$$, vết $$0$$, và cùng đa thức đặc trưng $$\lambda^2 + 1 = 0$$ (cùng cặp giá trị riêng $$\pm i$$). Nếu cho phép dùng ma trận đổi cơ sở phức trong $$\mathrm{SL}_2(\mathbb{C})$$, ta dễ dàng biến $$\gamma_1$$ thành $$\gamma_2$$ — giới toán học gọi chúng là **liên hợp ổn định** (*stably conjugate*).

Thế nhưng, nếu chỉ được dùng ma trận đổi cơ sở **thực** $$g \in \mathrm{SL}_2(\mathbb{R})$$, bạn có thể thử giải phương trình $$g\gamma_1 = \gamma_2 g$$ với $$g = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$: ta lập tức thu được $$a = -d$$ và $$b = c$$, suy ra

$$
\det(g) = ad - bc = -(a^2 + b^2) \le 0!
$$

Không bao giờ có thể đạt $$\det(g) = +1$$! Như vậy, một lớp liên hợp ổn định duy nhất trên $$\mathbb{C}$$ đã **bị tách làm hai lớp liên hợp rời nhau** trên $$\mathbb{R}$$ (tương tự, trên trường $$p$$-adic $$\mathbb{Q}_p$$, một lớp liên hợp ổn định cũng bị tách thành nhiều mảnh rời nhau).

Khi ta cộng các tích phân quỹ đạo trên tất cả các mảnh cùng lớp liên hợp ổn định (gọi là **tích phân ổn định** $$SO_\gamma(f) = O_{\gamma_1}(f) + O_{\gamma_2}(f)$$), mọi thứ rất đẹp. Nhưng phần **hiệu** $$O_{\gamma_1}(f) - O_{\gamma_2}(f)$$ (tổng có trọng số dấu, gọi là **tích phân $$\kappa$$-quỹ đạo**) lại giống như một "nhiễu giao thoa".

Phát hiện thiên tài của Langlands và Shelstad là: phần nhiễu giao thoa $$O_{\gamma_1}(f) - O_{\gamma_2}(f)$$ trên nhóm lớn $$G$$ không hề vô nghĩa — nó **bằng đúng một tích phân ổn định trên một nhóm nhỏ hơn $$H$$** (trong ví dụ $$\mathrm{SL}_2$$ ở trên, $$H$$ chính là nhóm quay đường tròn $$\mathrm{SO}(2)$$), gọi là **nhóm nội soi** (*endoscopic group*, nghĩa đen của *endoscopy* là "soi vào bên trong" để thấy cấu trúc ẩn của $$G$$).

### Nút thắt địa phương – toàn cục

Để so sánh phía phổ (toàn cục) của $$G$$ và $$H$$ qua công thức vết, ta buộc phải chứng minh rằng tại **hầu hết mọi số nguyên tố $$p$$**, tích phân $$\kappa$$-quỹ đạo của hàm chuẩn (hàm đơn vị của đại số Hecke) trên $$G(\mathbb{Q}_p)$$ bằng đúng tích phân ổn định tương ứng trên $$H(\mathbb{Q}_p)$$, nhân thêm một hệ số chuẩn hóa $$\Delta(\gamma_H, \gamma)$$ (gọi là **hệ số chuyển**, *transfer factor*):

$$
O_\gamma^{\kappa}(\mathbf{1}_{G(\mathbb{Z}_p)}) \;=\; \Delta(\gamma_H, \gamma)\, SO_{\gamma_H}(\mathbf{1}_{H(\mathbb{Z}_p)}).
$$

Đẳng thức này chính là **Bổ đề Cơ bản**. Cái tên "bổ đề" mang tính lịch sử (ban đầu Langlands và Shelstad hy vọng có thể chứng minh nó bằng vài trang tính toán $$p$$-adic), nhưng thực tế khi số chiều tăng lên, các tích phân $$p$$-adic trở nên phức tạp đến mức không thể tính bằng tay. Một đẳng thức **địa phương** tại từng số nguyên tố $$p$$ đã khóa chặt các định lý **toàn cục** của cả chương trình Langlands trong gần 30 năm.

---

## 3. Cuộc chạy tiếp sức 30 năm: từ tính tay đến bước ngoặt hình học

Bổ đề Cơ bản không phải là câu chuyện của một người đơn độc từ vạch xuất phát; nó là một cuộc chạy tiếp sức kéo dài hơn ba thập kỷ:

- **Thập niên 1980 (Xây dựng khung):** Robert Langlands và Diana Shelstad định nghĩa chính xác **hệ số chuyển** $$\Delta(\gamma_H, \gamma)$$ và phát biểu đầy đủ Bổ đề Cơ bản; Robert Kottwitz chỉ ra cách gắn tích phân quỹ đạo với việc đếm điểm trên các đa tạp đại số.
- **Thập niên 1990 (Những trường hợp riêng & Cầu nối đặc số):** Thomas Hales chứng minh cho nhóm $$\mathrm{Sp}_4$$ bằng tính toán trực tiếp cực kỳ công phu; quan trọng nhất, **Jean-Loup Waldspurger** chứng minh một định lý chuyển đổi tuyệt đẹp: nếu Bổ đề Cơ bản đúng cho **đại số Lie** trên **trường hàm đặc số $$p$$** (như $$\mathbb{F}_q((t))$$ — nơi có đầy đủ công cụ hình học đại số!), thì nó tự động kéo theo trường hợp đặc số 0 ($$\mathbb{Q}_p$$) và trường hợp nhóm!
- **Laumon–Ngô (2004):** Gérard Laumon và Ngô Bảo Châu chứng minh Bổ đề Cơ bản cho **nhóm unita** $$U(n)$$ bằng cách đưa **phân thớ Hitchin** vào cuộc. Đây là bước đột phá chứng tỏ "lối đi hình học" không chỉ đẹp về lý thuyết mà thực sự giải được bài toán cho mọi số chiều $$n$$.
- **Ngô Bảo Châu (2008 / xuất bản IHÉS 2010):** Trong công trình *Le lemme fondamental pour les algèbres de Lie*, Ngô Bảo Châu hoàn thiện và mở rộng toàn bộ bộ máy hình học — đặc biệt là chứng minh **Định lý về giá (Support Theorem)** tổng quát — để giải quyết trọn vẹn Bổ đề Cơ bản cho mọi đại số Lie rút gọn được.

---

## 4. Hình học xuất hiện: Phân thớ Hitchin và vết Frobenius

### Khung giải thích: vì sao hình học lại "biết" giá trị của một tích phân? (nên đọc chậm)

Người đọc mới thường thắc mắc: *vế trái là một tích phân trên trường $$p$$-adic, làm sao hình học đại số lại chứng minh được hai tích phân bằng nhau mà không cần tính giá trị cụ thể của chúng?* Dưới đây là chuỗi lập luận 4 bước nối hai thế giới, kèm ví dụ trực quan ở từng bước:

![Hình học bước vào]({{ site.baseurl }}/img/chapter_img/ngo_geometry_hitchin.svg)

*Hình. Từ tích phân quỹ đạo $$p$$-adic đến các thớ hình học, rồi quay về Bổ đề Cơ bản.*

#### Bước 1: Biến tích phân thành đếm số điểm trên trường hữu hạn $$\mathbb{F}_q$$
Nhờ định lý chuyển của Waldspurger, ta thay số $$p$$-adic $$\mathbb{Q}_p$$ bằng trường chuỗi lũy thừa hình thức $$\mathbb{F}_q((t))$$ trên trường hữu hạn $$\mathbb{F}_q$$. Khi đó, tích phân quỹ đạo $$O_\gamma(\mathbf{1})$$ (tổng các phần tử thỏa điều kiện liên hợp) biến thành **số điểm hữu tỷ trên $$\mathbb{F}_q$$** của một không gian hình học đại số gọi là **thớ Springer affine** (affine Springer fiber).

#### Bước 2: Biến đếm điểm thành vết của phép Frobenius (Grothendieck–Lefschetz)
Trên trường hữu hạn $$\mathbb{F}_q$$, phép nâng lên lũy thừa $$q$$ (gọi là **phép biến đổi Frobenius**: $$x \mapsto x^q$$) giữ nguyên mọi điểm của $$\mathbb{F}_q$$ (theo định lý nhỏ Fermat, $$x^q = x$$ với mọi $$x \in \mathbb{F}_q$$). **Công thức vết Grothendieck–Lefschetz** khẳng định số điểm của đa tạp $$X$$ trên $$\mathbb{F}_q$$ bằng tổng đan dấu vết của phép Frobenius tác động lên các nhóm **đối đồng điều $$\ell$$-adic** $$H^i(X, \mathbb{Q}_\ell)$$:

$$
\#X(\mathbb{F}_q) \;=\; \sum_{i \ge 0} (-1)^i \operatorname{Tr}\bigl(\mathrm{Frob}_q \;\big\vert\; H^i(X, \mathbb{Q}_\ell)\bigr).
$$

**Ví dụ nhỏ để cầm nắm ngay:**
- Với đường thẳng xạ ảnh $$\mathbb{P}^1$$ (mặt cầu Riemann phiên bản trên $$\mathbb{F}_p$$): ta có $$p$$ điểm hữu hạn $$\{0, 1, \dots, p-1\}$$ cộng thêm $$1$$ điểm ở vô cùng, tổng cộng $$p + 1$$ điểm. Đối đồng điều của mặt cầu chỉ khác 0 ở bậc $$0$$ (vết $$= 1$$) và bậc $$2$$ (vết $$= p$$), cho đúng $$1 + p$$!
- Với đường cong elliptic $$E$$ (hình xuyến có 1 lỗ): đối đồng điều bậc $$1$$ có số chiều $$2$$, và vết Frobenius trên $$H^1$$ chính là số $$a_p$$ ta đã gặp ở Mục 1, cho số điểm $$\#E(\mathbb{F}_p) = 1 - a_p + p$$!

Nhờ công thức này, muốn chứng minh hai tích phân quỹ đạo (của $$G$$ và $$H$$) bằng nhau, ta chỉ cần chứng minh hai không gian hình học tương ứng có **cùng "gói đối đồng điều"** (tương thích với tác động của Frobenius)!

#### Bước 3: Tại sao một thớ lẻ là chưa đủ — và phân thớ Hitchin là gì?
Khổ nỗi, một **thớ Springer affine** đứng đơn độc có vô hạn chiều và đầy rẫy **điểm kỳ dị** xấu xí, nên không thể trực tiếp tính đối đồng điều của nó. Đây là lúc **phân thớ Hitchin** xuất hiện như một cú xoay chuyển cục diện.

Để hình dung **ánh xạ Hitchin** chỉ bằng đại số tuyến tính năm nhất, hãy xét tập hợp tất cả các ma trận $$2\times 2$$ có vết bằng $$0$$:

$$
A = \begin{pmatrix} a & b \\ c & -a \end{pmatrix}.
$$

Ta gắn mỗi ma trận $$A$$ với định thức của nó: $$h(A) = -\det(A) = a^2 + bc \in \mathbb{C}$$.
- Đáy tham số là trục số $$t = a^2 + bc$$.
- Với mỗi giá trị $$t$$ ở đáy, tập hợp tất cả các ma trận $$A$$ có cùng $$a^2 + bc = t$$ tạo thành một **thớ** (fiber) nằm phía trên $$t$$:
  - Khi $$t \neq 0$$ (vùng **trơn**): phương trình $$a^2 + bc = t$$ mô tả một mặt cong **trơn nhẵn** và đều đặn.
  - Khi $$t = 0$$ (điểm **kỳ dị**): phương trình $$a^2 + bc = 0$$ sụp thành một **hình nón có đỉnh nhọn** tại $$(0, 0, 0)$$.

**Phân thớ Hitchin** của Ngô Bảo Châu là phiên bản toàn cục của ánh xạ "ma trận $$\mapsto$$ đa thức đặc trưng" này, nhưng thực hiện cho các phân thớ Higgs trên cả một đường cong đại số $$C$$. Thay vì nhìn vào một thớ Springer affine kỳ dị đứng trơ trọi (ứng với một tích phân quỹ đạo cố định), Ngô nhúng nó vào **cả một họ liên tục** các thớ nằm trên đáy Hitchin $$\mathcal{A}$$ — nơi hầu hết các thớ nằm ở vùng mở trơn đều là các không gian đẹp đẽ (đa tạp abel / mặt xuyến nhiều chiều) rất dễ tính toán!

#### Bước 4: Định lý về giá (Support Theorem) — chìa khóa quyết định
Một câu hỏi sống còn lập tức nảy ra: *khi ta đi từ vùng trơn tiến vào các điểm kỳ dị ở đáy, liệu có sinh ra thêm những thành phần đối đồng điều "ẩn" chỉ sống bám trên tập kỳ dị mà vùng trơn không nhìn thấy không?*

Bằng cách khai thác cấu trúc đối xứng sâu sắc của phân thớ Hitchin (tác động của nhóm đối xứng trên các thớ) kết hợp với định lý phân tách của Beilinson–Bernstein–Deligne–Gabber, Ngô Bảo Châu chứng minh **Định lý về giá**: *không có bất kỳ thành phần đối đồng điều ẩn nào nằm lọt ra ngoài vùng trơn!* Mọi mảnh đối đồng điều trên toàn bộ phân thớ — kể cả tại những thớ kỳ dị nhất — đều được **xác định hoàn toàn bởi hành vi trên tập mở trơn**. Mà trên tập mở trơn, việc so sánh gói đối đồng điều giữa nhóm $$G$$ và nhóm nội soi $$H$$ lại trở nên trong sáng và trực tiếp. Từ đó, đẳng thức vết Frobenius — và kéo theo toàn bộ **Bổ đề Cơ bản** — lập tức được chứng minh!

Tóm tắt chuỗi chuyển ngôn ngữ vĩ đại:

$$
\text{tích phân quỹ đạo } p\text{-adic}
\;\longleftrightarrow\;
\text{đếm điểm / vết Frobenius}
\;\longleftrightarrow\;
\text{đối đồng điều phân thớ Hitchin}
\;\longleftrightarrow\;
\text{Định lý về giá (Ngô)}.
$$

---

### Video ngắn 2: Phân thớ Hitchin & Đếm điểm trên trường hữu hạn

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/langlands-hitchin-geometry_vi.mp4"></video>
</div>

Video dài khoảng 1 phút 13 giây (có thuyết minh tiếng Việt giọng Algenib): cách biến tích phân quỹ đạo p-adic thành đếm điểm qua vết Frobenius, vai trò của định lý về giá trên phân thớ Hitchin, và bước nhảy từ Laumon–Ngô (2004) sang Ngô (2010).

## 5. Hệ quả sau khi có Bổ đề Cơ bản

Chứng minh của Ngô Bảo Châu không chỉ đóng lại một bài toán cũ; nó giống như việc rút chốt một con đập đã chặn dòng chảy suốt 30 năm. Ngay sau năm 2010, hàng loạt công trình "có điều kiện" lập tức trở thành định lý vô điều kiện:

- **Ổn định hóa công thức vết Arthur–Selberg:** Hoàn thiện cỗ máy so sánh phổ giữa các nhóm rút gọn được.
- **Chương trình phân loại nội soi của James Arthur:** Phân loại hoàn chỉnh các biểu diễn tự đẳng cấu cho các nhóm cổ điển (nhóm trực giao, nhóm symplectic) bằng cách quy về nhóm tuyến tính tổng quát $$\mathrm{GL}_n$$ — một bước tiến khổng lồ cho **tính hàm tử (functoriality)** Langlands.
- **Mở ra nhánh nghiên cứu mới:** Cách dùng phân thớ Hitchin và định lý về giá để chứng minh các đẳng thức giải tích đã trở thành một trường phái riêng (chương trình "Beyond Endoscopy" và hình học của các không gian moduli Higgs).

---

## 6. Huy chương Fields 2010 và bối cảnh lịch sử

- **Trao giải:** Đại hội Toán học Thế giới (ICM) tại Hyderabad, Ấn Độ (tháng 8/2010), khi Ngô Bảo Châu đang công tác tại **Université Paris-Sud** (và Viện Nghiên cứu Cao cấp IAS, Princeton).
- **Quá trình tiếp theo:** Sau năm 2010, ông giảng dạy tại Đại học Chicago, đồng thời giữ vai trò Giám đốc khoa học của Viện Nghiên cứu Cao cấp về Toán (VIASM) tại Việt Nam, góp phần xây dựng cộng đồng nghiên cứu toán học trong nước.
- **Giải thưởng liên quan:** **Robert Langlands** nhận **Giải Abel 2018** cho toàn bộ tầm nhìn và chương trình nối lý thuyết biểu diễn với lý thuyết số. Ghi nhận công lao cho rạch ròi: Langlands đề xuất tầm nhìn; Langlands–Shelstad, Kottwitz, Waldspurger, Hales đặt nền móng lý thuyết nội soi và cầu nối đặc số; Laumon–Ngô (2004) mở khóa lối đi hình học; Ngô (2010) hoàn tất Bổ đề Cơ bản tổng quát; cả cộng đồng gỡ điều kiện cho hàng loạt định lý lớn.

---

## 7. Vị trí trong bản đồ Chương 2 và nhìn lại điều nghịch lý

Chủ đề xuyên suốt của Chương 2 là toán học hiện đại tầm giải Fields nhìn như những **cây cầu nối giữa các lĩnh vực tưởng chừng tách biệt**:

| Cầu nối | Công trình tiêu biểu |
|---------|----------------------|
| Giải tích PDE ↔ Tô pô 3 chiều | [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/) |
| Tổ hợp cộng tính ↔ Số nguyên tố | [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) |
| **Hình học đại số ↔ Giải tích tự đẳng cấu** | **Ngô Bảo Châu** |
| Hệ động lực ↔ Không gian moduli | [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/) |
| Hình học $$p$$-adic ↔ Số học | [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/) |
| Giải tích điều hòa đa thang đo ↔ Hình học | [Wang]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/) |

**Nghịch lý đáng nhớ:** Một đẳng thức tích phân **địa phương** (tại từng số nguyên tố $$p$$) đã chặn đứng các định lý **toàn cục** của cả một chương trình đại thống nhất. Và lời giải cho bài toán **giải tích** ấy lại không đến từ việc tính tích phân khéo hơn, mà đến từ **hình học đại số** — nhìn toàn bộ họ các không gian hình học cùng lúc để ép cái kỳ dị phải nghe theo cái trơn.

---

## 8. Langlands số học và Langlands hình học: phân biệt cho rõ

*Tổng hợp từ các bài giảng tổng quan (theo phong cách Edward Frenkel và bộ tư liệu Langlands). Bài chuyên sâu: [Langlands hình học và đối ngẫu S]({{ site.baseurl }}/contents/vi/chapter06/06_15_Geometric_Langlands_SDuality/).*

### Hai chương trình song song, cùng ý tưởng về nhóm đối ngẫu

| Tiêu chí | **Langlands số học** (chủ đề của bài này) | **Langlands hình học** |
|----------|-------------------------------------------|------------------------|
| Không gian nền | Trường số ($$\mathbb{Q}$$) / vành adele $$\mathbb{A}$$ | Đường cong đại số $$C$$ (thường trên $$\mathbb{C}$$) |
| Đối tượng "tự đẳng cấu" | Biểu diễn tự đẳng cấu của $$G(\mathbb{A})$$ | Bó / $$D$$-môđun trên không gian $$\mathrm{Bun}_G(C)$$ |
| Đối tượng "Galois / phổ" | Biểu diễn Galois / motive | Hệ địa phương (local systems) cho nhóm đối ngẫu $$G^\vee$$ |
| Nhóm đối ngẫu | $$G^\vee$$ | $$G^\vee$$ |
| Vai trò Bổ đề của Ngô | Công cụ cốt lõi cho **nội soi / công thức vết** | Không phải cùng một định lý (dù chia sẻ hình học Hitchin) |

**Cầu nối với vật lý lý thuyết:** Năm 2007, Anton Kapustin và Edward Witten diễn giải Langlands hình học như biểu hiện toán học của **đối ngẫu S** (đối ngẫu điện–từ) trong lý thuyết trường siêu Yang–Mills $$\mathcal{N}=4$$ trong 4 chiều, với đối xứng gương của không gian Hitchin đóng vai trò cốt lõi. Đây là một bộ từ điển và nguồn cảm hứng nghiên cứu tuyệt vời (xem thêm [bài về Witten]({{ site.baseurl }}/contents/vi/chapter06/06_17_Witten_Physics_Math/)), nhưng bản thân trực giác vật lý không thay thế cho chứng minh toán học chặt chẽ.

**Một câu tóm tắt chuẩn xác khi thảo luận:** *"Ngô Bảo Châu chứng minh Bổ đề Cơ bản để mở khóa phép so sánh nội soi trong công thức vết; chương trình Langlands số học nói chung vẫn là một mạng lưới giả thuyết đang phát triển; còn Langlands hình học là một chương trình song song ở ngôn ngữ phạm trù có chung nhóm đối ngẫu $$G^\vee$$."*

---

### Video ngắn 3: Langlands Số học vs Hình học & 4 Hiểu lầm cần tránh

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/langlands-arithmetic-vs-geometric_vi.mp4"></video>
</div>

Video dài khoảng 1 phút 8 giây (có thuyết minh tiếng Việt giọng Algenib): phân biệt Langlands số học với Langlands hình học, cầu nối đối ngẫu S của Kapustin–Witten, và 4 hiểu lầm phổ biến về Huy chương Fields 2010.

## Hiểu lầm thường gặp

| Khẳng định | Đúng/sai | Sửa lại |
|------------|----------|---------|
| "Ngô Bảo Châu sáng lập chương trình Langlands." | **Sai** | Robert Langlands đề ra chương trình (từ 1967); Ngô chứng minh Bổ đề Cơ bản — một nút thắt trung tâm trong chương trình đó. |
| "Bổ đề Cơ bản chỉ là một chi tiết kỹ thuật nhỏ." | **Sai** | Chữ "bổ đề" mang tính lịch sử; thực tế nó cản trở hàng loạt định lý lớn trong gần 30 năm. |
| "Chứng minh chỉ là biến đổi các tích phân $$p$$-adic." | **Sai** | Hình học đại số (phân thớ Hitchin, đối đồng điều và định lý về giá) mới là công cụ quyết định. |
| "Laumon–Ngô năm 2004 đã giải xong trường hợp tổng quát." | **Sai** | Năm 2004 giải cho họ nhóm unita; trường hợp tổng quát cho đại số Lie hoàn tất trong công trình riêng của Ngô (xuất bản 2010). |
| "Langlands đoạt giải Fields nhờ chương trình này." | **Sai** | Langlands nhận **Giải Abel 2018**; Ngô Bảo Châu nhận **Huy chương Fields 2010**. |
| "Ngô đã chứng minh xong toàn bộ Langlands / Langlands hình học." | **Sai** | Bổ đề Cơ bản phục vụ lý thuyết nội soi trong Langlands số học; toàn bộ chương trình vẫn còn nhiều giả thuyết mở. |
| "Langlands số học và Langlands hình học là cùng một định lý." | **Sai** | Cùng chia sẻ ý tưởng về nhóm đối ngẫu $$G^\vee$$, nhưng đối tượng và bối cảnh hoàn toàn khác nhau. |

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Video và tài liệu gốc dùng để **định hướng và làm quen với không khí nghiên cứu**. Chi tiết: `research/video-research/Langlands_Program/`.

**Thứ tự xem gợi ý**

1. **Định hướng** — Quanta, *The Biggest Project in Modern Mathematics*: [YouTube](https://www.youtube.com/watch?v=_bJeKUosqoY).  
2. **Bối cảnh** — Numberphile, *The Langlands Program* (Frenkel): [YouTube](https://www.youtube.com/watch?v=4dyytPboqvE).  
3. **Nghiên cứu** — Ngô B. C., tích phân quỹ đạo (IHÉS, phần 1/3): [YouTube](https://www.youtube.com/watch?v=74aq5gIDrFQ).  
4. **Không bắt buộc** — bài giảng Abel của Frenkel: [YouTube](https://www.youtube.com/watch?v=b8e_HMEwKIY); Wiles (Oxford): [YouTube](https://www.youtube.com/watch?v=ZFOPxZtlkig).

**Nhắc lại:** Bổ đề Cơ bản **đã được chứng minh**. Chương trình Langlands nói chung vẫn **còn mở**. Đừng nhầm "Ngô đã giải xong Langlands".

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Langlands_Program/transcripts/` · trạng thái: `research/video-research/Langlands_Program/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Langlands_Program_74aq5gIDrFQ_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo


Danh sách URL đầy đủ (mọi đường dẫn tìm được khi nghiên cứu video): `research/video-research/Langlands_Program/references.md`.

### Danh sách URL đầy đủ

1. https://www.youtube.com/watch?v=74aq5gIDrFQ  
2. https://www.youtube.com/watch?v=4dyytPboqvE  
3. https://arxiv.org/abs/0801.0446  
4. https://arxiv.org/pdf/0801.0446  
5. https://arxiv.org/abs/1103.4066  
6. https://www.claymath.org/library/cw/arthur/pdf/icm-ngo.pdf  
7. https://math.uchicago.edu/~ngo/survey.pdf  
8. https://www.ias.edu/ideas/2010/fundamental-lemma  
9. https://en.wikipedia.org/wiki/Fundamental_lemma_(Langlands_program)  
10. https://en.wikipedia.org/wiki/Langlands_program  
11. https://en.wikipedia.org/wiki/Ng%C3%B4_B%E1%BA%A3o_Ch%C3%A2u  
12. https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010  
13. https://www.youtube.com/watch?v=_bJeKUosqoY  
14. https://www.youtube.com/watch?v=b8e_HMEwKIY  
15. https://www.youtube.com/watch?v=ZFOPxZtlkig  
16. https://www.numberphile.com/videos/the-langlands-program  

### Bộ tư liệu nghiên cứu

17. Bộ tư liệu của khóa học: `research/video-research/Langlands_Program/`.

1. Tư liệu của **IMU về Huy chương Fields 2010** cho Ngô Bảo Châu.  
2. **B. C. Ngô** (2010). *Le lemme fondamental pour les algèbres de Lie*. *Publ. Math. IHÉS*.  
3. **G. Laumon & B. C. Ngô** — công trình về Bổ đề Cơ bản cho nhóm unita (giai đoạn 2004).  
4. Các bài tổng quan về lý thuyết nội soi / Bổ đề Cơ bản (Arthur; Bourbaki / ICM).  
5. Kiến thức nền: sách nhập môn về dạng tự đẳng cấu của Knapp / Bump; nâng cao: các tập về phân loại nội soi của Arthur.  
6. Các bài giới thiệu phổ thông / của các viện: chỉ dùng cho tiểu sử, không thay thế các bài tổng quan kỹ thuật.

*Ghi chú.* Khung lịch sử theo các tài liệu chuẩn của IMU / bài ca ngợi tại lễ trao giải, và theo bài báo của Ngô trên IHÉS. Các hình trong bài là sơ đồ minh họa ý tưởng.

---

## Hướng đi tiếp

- Nghe một bài giảng tổng quan khoảng một giờ về lý thuyết nội soi dành cho người ngoài ngành.  
- Xem lại tính modular của đường cong elliptic như một cột mốc khác của chương trình Langlands, với cách chứng minh hoàn toàn khác.  
- Nếu muốn đi xa hơn: tìm hiểu hệ số chuyển Langlands–Shelstad, "hệ số từ điển" đi kèm với bổ đề.  
- Đọc song song bài [Scholze]({{ site.baseurl }}/contents/vi/chapter02/02_06_Scholze_Perfectoid/) để so sánh hai cách hình học đi vào số học.

## Video tham khảo

- **Xem trước:** [The Biggest Project in Modern Mathematics](https://www.youtube.com/watch?v=_bJeKUosqoY) — Quanta Magazine, tiếng Anh. Giới thiệu tổng quan chương trình Langlands; nên xem trước khi đọc bài.
- [The Langlands Program - Numberphile](https://www.youtube.com/watch?v=4dyytPboqvE) — Numberphile, tiếng Anh. Edward Frenkel giải thích ý tưởng của chương trình Langlands; nên xem sau khi đã nắm ý chính của bài.
- [Bao Chau Ngo - 1/3 Orbital integrals, moduli spaces and invariant theory](https://www.youtube.com/watch?v=74aq5gIDrFQ) — Institut des Hautes Etudes Scientifiques (IHES), tiếng Anh. Xem thêm sau hai video trên; bài giảng của chính Ngô Bảo Châu về tích phân quỹ đạo và không gian moduli.
