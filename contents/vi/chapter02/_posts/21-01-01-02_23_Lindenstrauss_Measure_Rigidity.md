---
layout: post
title: "Độ cứng độ đo của Lindenstrauss (Huy chương Fields 2010)"
chapter: '02'
order: 23
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Hãy thử một trò chơi đơn giản trên vòng tròn $$[0, 1)$$: mỗi bước bạn nhân vị trí hiện tại với $$2$$ rồi lấy phần thập phân ($$x \mapsto 2x \bmod 1$$). Hệ động lực này hỗn loạn đến mức có **vô số** cách phân bố xác suất bất biến — từ phân bố đều đến vô vàn phân bố fractal kỳ dị sống trên tập Cantor. Nhưng điều gì sẽ xảy ra nếu bạn bắt một phân bố xác suất phải bất biến *đồng thời* dưới cả phép nhân $$2$$ lẫn phép nhân $$3$$? Hillel Furstenberg phát hiện ra hiện tượng kỳ lạ gọi là **độ cứng độ đo** (*measure rigidity*): chỉ cần thêm một đối xứng giao hoán độc lập thứ hai, gần như toàn bộ thế giới fractal kỳ dị sụp đổ, chỉ còn lại những phân bố có nguồn gốc đại số gọn gàng!

Đáng kinh ngạc hơn nữa: câu hỏi tưởng chừng thuần túy về động lực học hỗn loạn đó lại nắm giữ chìa khóa mở hai pháo đài lớn của **lý thuyết số** và **vật lý lượng tử** — xấp xỉ đồng thời hai số vô tỷ (giả thuyết Littlewood) và phân bố năng lượng của sóng lượng tử trên mặt cong âm (tính ergodic lượng tử duy nhất). Năm 2010, **Elon Lindenstrauss** nhận **Huy chương Fields**:

> “for his results on measure rigidity in ergodic theory, and their applications to number theory.”
> — [IMU, Fields Medals 2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)

*Tạm dịch: vì các kết quả về độ cứng độ đo trong lý thuyết ergodic và những ứng dụng của chúng vào lý thuyết số.*

Huy chương tôn vinh các định lý phân loại độ đo bất biến cho **tác động chéo hóa được có hạng cao** trên không gian thuần nhất, cùng hai ứng dụng vang dội: chứng minh tập các ngoại lệ của **giả thuyết Littlewood** có **chiều Hausdorff bằng không** (cùng Manfred Einsiedler và Anatole Katok), và chứng minh **tính ergodic lượng tử duy nhất số học (QUE)** cho dạng Hecke–Maass trên các mặt hyperbolic số học compact. Bài học này đặt công trình của Lindenstrauss vào dòng chảy Furstenberg–Margulis–Ratner–Katok–Einsiedler–Host–Kra, đồng thời giữ ranh giới trung thực: giả thuyết Littlewood đầy đủ và QUE cho mặt hyperbolic không số học vẫn còn mở.

**Mạch bài học:** Kiến thức cần nhớ (lý thuyết ergodic, không gian thuần nhất các lưới, độ cứng độ đo) → Ví dụ làm từng bước: $$\times 2$$ vs $$\times 3$$ trên vòng tròn và bài toán Littlewood dưới lăng kính lưới $$3\times 3$$ → Lũy đơn (Ratner) vs. Chéo hạng cao (EKL) → Giải thích: 4 bước nối động lực học thuần nhất sang Littlewood và QUE số học → Ghi nhận công lao & phân biệt với Giải Abel 2020.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Định nghĩa **độ cứng độ đo** và tự minh họa qua ví dụ cụ thể $$\times 2 \bmod 1$$ (vô số độ đo bất biến) so với $$\times 2, \times 3$$ (ép độ đo phải đại số).
- Phân biệt rành mạch độ cứng cho dòng **lũy đơn** (định lý Ratner, phân loại hoàn toàn) với tác động **chéo hạng cao** (Einsiedler–Katok–Lindenstrauss, cần giả thiết entropy dương).
- Phát biểu **giả thuyết Littlewood** và kết luận chính xác của EKL (tập ngoại lệ có **chiều Hausdorff bằng không**), đồng thời giải thích cách dịch Littlewood thành quỹ đạo trên $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$.
- Phát biểu **QUE số học** trên mặt hyperbolic số học compact (Lindenstrauss, 2006), ghi công Rudnick–Sarnak cho giả thuyết và Soundararajan (2010) cho mặt modular không compact.
- Ghi công đúng cho Furstenberg, Margulis, Ratner, Katok, Einsiedler, Host–Kra, Bourgain và Holowinsky–Soundararajan, và phân biệt Huy chương Fields 2010 với Giải Abel 2020 trong [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/).

**Kiến thức nền.** Tác động nhóm; khái niệm độ đo bất biến và tính ergodic; hình học hyperbolic trên nửa mặt phẳng trên ở mức hình dung ($$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$). Không gian thuần nhất $$\Gamma\backslash G$$ có thể hiểu đơn giản là "một lưới (lattice) tác động lên một nhóm Lie", chưa cần lý thuyết đầy đủ.

**Liên kết với các bài khác.** [Furstenberg & Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/) trình bày quan điểm được giải Abel 2020 ghi nhận: động lực học là công cụ cho lý thuyết số. [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) là một ví dụ khác về việc đưa phương pháp ergodic vào số học. [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/) cho thấy động lực học thuần nhất trong một chân dung Fields về sau.

---

## Kiến thức cần nhớ: Lý thuyết ergodic, Động lực học thuần nhất và Độ cứng độ đo là gì?

### 1. Lý thuyết ergodic nghiên cứu những câu hỏi nào?
Lý thuyết ergodic nghiên cứu hành vi thống kê dài hạn của một hệ động lực bảo toàn độ đo $$(X, \mu, H)$$. Một độ đo xác suất $$\mu$$ gọi là **bất biến** nếu tác động của nhóm $$H$$ không làm thay đổi phân bố $$\mu$$, và gọi là **ergodic** nếu không thể tách $$X$$ thành hai mảnh bất biến độc lập đều có độ đo dương. Câu hỏi truyền thống là: *trung bình thời gian dọc theo quỹ đạo có hội tụ về trung bình không gian không?* Còn **độ cứng độ đo** hỏi sâu hơn một tầng: *tất cả những độ đo xác suất bất biến ergodic nào có thể tồn tại ngay từ đầu?*

### 2. Không gian thuần nhất $$\Gamma \backslash G$$ — nơi lý thuyết số biến thành chuyển động hình học
Xét tập tất cả các lưới có thể tích đơn vị trong $$\mathbb{R}^d$$. Mọi lưới như vậy có dạng $$g\mathbb{Z}^d$$ với $$g \in \mathrm{SL}_d(\mathbb{R})$$, và hai ma trận cho cùng một lưới khi sai khác bởi phép đổi cơ sở nguyên $$\gamma \in \mathrm{SL}_d(\mathbb{Z})$$. Vậy không gian các lưới chính là **không gian thuần nhất** $$\mathrm{SL}_d(\mathbb{R})/\mathrm{SL}_d(\mathbb{Z})$$. Một bài toán xấp xỉ Diophantine (như tìm số nguyên $$n$$ để $$n\alpha$$ rất gần số nguyên) dịch thẳng thành câu hỏi hình học: *khi kéo giãn lưới bởi ma trận chéo, lưới đó có chứa vector nguyên cực ngắn không — tức quỹ đạo có đi sâu ra vùng đỉnh nhọn (cusp) hay bị nhốt trong tập compact?*

### 3. Hai loại tác động: Lũy đơn (Unipotent) và Chéo hạng cao (Higher-rank Diagonal)
- **Dòng lũy đơn** (như ma trận trượt $$\begin{pmatrix}1 & t \\ 0 & 1\end{pmatrix}$$): quỹ đạo tách nhau chậm theo tốc độ **đa thức**. **Marina Ratner** (thập niên 1990) chứng minh mọi độ đo bất biến ergodic đều là độ đo đại số (không cần điều kiện phụ!). Trước đó **Margulis** dùng dòng lũy đơn để giải giả thuyết Oppenheim.
- **Tác động chéo hạng cao** (như nhóm ma trận chéo dương 2 tham số $$\mathrm{diag}(e^s, e^t, e^{-s-t})$$ trên $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$): quỹ đạo tách nhanh theo **hàm mũ**, sinh ra vô số tập fractal kỳ dị nên không có định lý không điều kiện như Ratner. Nhưng nếu áp thêm điều kiện **entropy dương** (loại bỏ các độ đo fractal suy biến bậc 0), Furstenberg và Margulis dự đoán độ đo vẫn bắt buộc phải đại số!

| Hướng nghiên cứu | Tác động điển hình | Phân loại | Ứng dụng số học |
|---------|-------------------|-----------|------------------|
| Ratner / Margulis, lũy đơn | Nhóm một tham số lũy đơn | Đầy đủ, đại số | Oppenheim và nhiều kết quả khác |
| Chéo, hạng cao | Xuyến tách, $$\times 2\times 3$$ | Từng phần; cần giả thiết entropy | Xấp xỉ Diophantine kiểu Littlewood |

---

## 1. Ví dụ làm từng bước: $$\times 2$$ vs. $$\times 3$$ trên vòng tròn và ma trận $$3\times 3$$ của Littlewood

### Ví dụ 1: Tại sao một phép biến đổi thì "mềm", còn hai phép giao hoán lại "cứng"?
Xét ánh xạ $$T_2(x) = 2x \bmod 1$$ trên vòng tròn $$[0, 1)$$.
- Thử lấy điểm $$x = \frac{1}{3}$$: $$T_2(1/3) = \frac{2}{3}$$, rồi $$T_2(2/3) = \frac{4}{3} \equiv \frac{1}{3} \pmod 1$$. Ta có ngay một độ đo bất biến ergodic tập trung trên 2 điểm: $$\mu = \frac{1}{2}\delta_{1/3} + \frac{1}{2}\delta_{2/3}$$.
- Viết $$x$$ ở hệ nhị phân $$0.b_1 b_2 b_3\ldots$$, phép $$T_2$$ chỉ là **dịch trái một chữ số**. Nếu bạn chọn các bit $$b_k \in \{0, 1\}$$ độc lập với xác suất $$P(b_k = 1) = 0.7$$ (đồng xu lệch), phân bố thu được là một **độ đo fractal kỳ dị** hoàn toàn bất biến dưới $$T_2$$! Có vô số độ đo như vậy.
- Bây giờ thử áp thêm phép $$T_3(x) = 3x \bmod 1$$: điểm $$1/3$$ bị kéo thẳng về $$0$$ (phá vỡ quỹ đạo tuần hoàn trên), còn cấu trúc bit nhị phân của đồng xu lệch $$0.7$$ bị xé nát hoàn toàn dưới phép nhân $$3$$! **Định lý Rudolph (1990)** chứng minh: nếu một độ đo xác suất trên vòng tròn bất biến dưới *cả* $$T_2$$ lẫn $$T_3$$ và có **entropy dương**, thì nó *bắt buộc* phải là độ đo Lebesgue đều trên $$[0, 1)$$!

### Ví dụ 2: Dịch giả thuyết Littlewood sang quỹ đạo ma trận $$3\times 3$$
**Giả thuyết Littlewood (1930)** hỏi liệu với mọi cặp số thực $$(\alpha, \beta)$$, ta có:

$$
\liminf_{n\to\infty}\, n\,\|n\alpha\|\,\|n\beta\| = 0,
$$

trong đó $$\|y\|$$ là khoảng cách từ $$y$$ tới số nguyên gần nhất. Hãy thử gài $$(\alpha, \beta)$$ vào ma trận $$3\times 3$$:

$$
u_{\alpha,\beta} = \begin{pmatrix} 1 & \alpha & \beta \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \in \mathrm{SL}_3(\mathbb{R}),
\qquad
a(s,t) = \begin{pmatrix} e^{-s-t} & 0 & 0 \\ 0 & e^s & 0 \\ 0 & 0 & e^t \end{pmatrix}.
$$

Lấy một vector nguyên $$(m, p, n)^T \in \mathbb{Z}^3$$ rồi nhân với $$a(s,t)\,u_{\alpha,\beta}$$:

$$
a(s,t)\,u_{\alpha,\beta}\begin{pmatrix} -p \\ n_1 \\ n_2 \end{pmatrix}
\;\text{— cụ thể hơn, xét ma trận chuyển vị tác động lên } (n, -p, -q)^T\text{:}
$$

Tích ba tọa độ của vector $$v = \bigl(e^{-(s+t)} n,\; e^s(n\alpha - p),\; e^t(n\beta - q)\bigr)$$ **hoàn toàn không phụ thuộc vào $$s, t$$** và đúng bằng:

$$
\bigl\vert e^{-(s+t)} n \bigr\vert \cdot \bigl\vert e^s(n\alpha - p) \bigr\vert \cdot \bigl\vert e^t(n\beta - q) \bigr\vert = \vert n \vert \cdot \vert n\alpha - p \vert \cdot \vert n\beta - q \vert!
$$

Hãy nhìn điều kỳ diệu vừa hiện ra: nếu cặp $$(\alpha, \beta)$$ là một **phản ví dụ** của Littlewood (tức $$n\|n\alpha\|\|n\beta\| \ge c > 0$$ với mọi $$n \ge 1$$), thì mọi vector nguyên khác không trong lưới $$a(s,t)u_{\alpha,\beta}\mathbb{Z}^3$$ đều có độ dài bị chặn dưới bởi $$c^{1/3} > 0$$ với *mọi* $$s, t \ge 0$$! Theo tiêu chuẩn compact Mahler, điều đó có nghĩa là **toàn bộ quỹ đạo chéo của lưới bị nhốt mãi trong một tập compact**, không bao giờ thoát ra vô cực!

---

## 2. Giải thích: từ Độ cứng độ đo đến Littlewood và QUE số học

Làm sao một định lý phân loại độ đo trên không gian thuần nhất lại bẻ khóa đồng thời cả bài toán xấp xỉ Diophantine (Littlewood) lẫn hỗn loạn lượng tử (QUE)? Hãy theo dõi mạch lập luận 4 bước:

#### Bước 1: Định lý phân loại độ đo EKL (Einsiedler–Katok–Lindenstrauss, *Annals*, 2006)
Trên $$\mathrm{SL}_3(\mathbb{R})/\mathrm{SL}_3(\mathbb{Z})$$ (hạng $$2$$), EKL nghiên cứu các độ đo xác suất $$\mu$$ bất biến và ergodic dưới toàn bộ xuyến chéo $$A = \{a(s,t)\}$$. Bằng kỹ thuật **lá Lyapunov thô** (*coarse Lyapunov foliations*) và phân rã entropy theo từng hướng giãn/co của xuyến, họ chứng minh: nếu $$\mu$$ có **entropy dương** đối với ít nhất một phần tử của $$A$$, thì $$\mu$$ bắt buộc phải là **độ đo đại số** (độ đo Haar trên một quỹ đạo đóng của nhóm con trung gian — và trong trường hợp quỹ đạo bị chặn thì không có độ đo đại số nào tập trung quanh các ngoại lệ bị nhốt!).

#### Bước 2: Suy ra tập ngoại lệ của giả thuyết Littlewood có chiều Hausdorff bằng 0
Giả sử tập các cặp phản ví dụ $$(\alpha, \beta)$$ vi phạm giả thuyết Littlewood có chiều Hausdorff dương $$> 0$$. Khi đó, bằng định lý Frostman và cách xây dựng độ đo giới hạn dọc theo các quỹ đạo bị nhốt trong tập compact, ta tạo ra được một độ đo bất biến dưới $$A$$ trên tập compact đó có **entropy dương**! Điều này mâu thuẫn trực tiếp với định lý phân loại ở Bước 1! Vậy **tập ngoại lệ của Littlewood bắt buộc có chiều Hausdorff bằng $$0$$!** (Vì tập chiều Hausdorff $$0$$ vẫn có thể khác rỗng, nên giả thuyết Littlewood đầy đủ vẫn còn mở.)

#### Bước 3: Nâng bài toán sóng lượng tử (QUE) lên dòng trắc địa trên không gian pha
Trên mặt hyperbolic $$M = \Gamma\backslash\mathbb{H}$$, một dạng Maass là hàm riêng $$-\Delta\phi = \lambda\phi$$ với phân bố khối lượng $$\mu_\phi = \vert\phi\vert^2 d\mathrm{vol}$$. Giả thuyết **QUE** của **Rudnick–Sarnak (1994)** khẳng định mọi dãy hàm riêng năng lượng cao đều hội tụ về phân bố đều (không có "vết sẹo lượng tử" tập trung trên một đường trắc địa đóng).
Bằng phép **nâng vi địa phương** (*microlocal lift*), mọi giới hạn yếu $$\mu$$ của $$\mu_\phi$$ được nâng lên thành một độ đo bất biến dưới **dòng trắc địa** (tác động chéo hạng 1!) trên không gian phân thớ tiếp xúc đơn vị $$\Gamma\backslash\mathrm{SL}_2(\mathbb{R})$$.

#### Bước 4: Biến hạng 1 thành "hạng cao" nhờ toán tử Hecke (Lindenstrauss, *Annals*, 2006)
Dòng trắc địa chỉ có hạng 1 nên tự nó không đủ độ cứng. Ý tưởng thiên tài của **Lindenstrauss** cho mặt hyperbolic **số học** là tận dụng việc $$\phi$$ còn là hàm riêng chung của vô hạn **toán tử Hecke** (dạng Hecke–Maass): các toán tử Hecke cung cấp thêm tính hồi quy theo các hướng $$p$$-adic / adelic (đóng vai trò như chiều chéo thứ hai!), đồng thời công trình trước đó của **Bourgain–Lindenstrauss** đảm bảo giới hạn lượng tử luôn có **entropy dương**! Ghép hai mảnh đó vào bộ máy độ cứng độ đo, Lindenstrauss chứng minh giới hạn lượng tử duy nhất trên mọi mặt hyperbolic số học **compact** chính là độ đo thể tích chuẩn hóa — hoàn tất **QUE số học trường hợp compact**!

(Với mặt modular **không compact** $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$, phương pháp của Lindenstrauss cho giới hạn có dạng $$c \cdot d\mathrm{vol}$$ với $$c \in [0, 1]$$; đến năm 2010, **Kannan Soundararajan** chứng minh $$c = 1$$ — không có khối lượng thoát ra đỉnh nhọn — hoàn tất QUE số học trên mặt modular. Còn QUE cho dạng cusp Hecke **chỉnh hình** là định lý độc lập của **Holowinsky–Soundararajan** (2010) bằng lý thuyết số giải tích; và QUE cho mặt hyperbolic *không số học* vẫn còn mở.)

Tóm tắt cầu nối của Lindenstrauss:

$$
\text{Số học (Littlewood / Hecke–Maass)}
\;\longleftrightarrow\;
\text{Quỹ đạo trên } \Gamma\backslash G
\;\xrightarrow{\text{Hạng cao + Entropy } > 0}\;
\text{Độ đo đại số duy nhất}.
$$

---

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/lindenstrauss-measure-rigidity_vi.mp4"></video>
</div>

Video dài khoảng 44 giây (có thuyết minh tiếng Việt): tính cứng độ đo (measure rigidity) cho tác động chéo bậc cao và giả thuyết Littlewood.

## 3. Những người liên quan và vị trí trong lịch sử

| Tên | Vai trò trong câu chuyện |
|-----|------------------------------|
| Furstenberg | Bài toán $$\times 2,\times 3$$ và ý tưởng rằng các ánh xạ giao hoán bổ sung làm độ đo trở nên cứng; hồi quy bội |
| Margulis | Siêu cứng (superrigidity), tính số học (arithmeticity), dòng lũy đơn, giả thuyết Oppenheim; giả thuyết về độ cứng cho tác động chéo |
| Ratner | Phân loại cho dòng lũy đơn, trường hợp đã hoàn tất, đối xứng với bài toán chéo |
| Katok | Entropy, độ cứng, và cộng tác trong EKL |
| Einsiedler | EKL và các công trình động lực học thuần nhất sau này với Lindenstrauss và những người khác |
| Host–Kra | Cấu trúc của trung bình bội / nhân tử nil, thuộc hướng độ cứng ergodic rộng hơn |
| Rudnick–Sarnak | Giả thuyết QUE |
| Soundararajan | Không thoát khối lượng trên $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$; QUE chỉnh hình cùng Holowinsky |
| Bourgain | Entropy của giới hạn lượng tử (cùng Lindenstrauss) |

Elon Lindenstrauss (sinh 1970) bảo vệ tiến sĩ năm 1999 tại Đại học Hebrew dưới sự hướng dẫn của Benjamin Weiss, là nghiên cứu viên dài hạn Viện Clay (2003–2005), giảng dạy tại Princeton và Đại học Hebrew, và từ 2024 là giáo sư thường trực tại IAS. Ông là người Israel đầu tiên nhận Huy chương Fields.

**Vì sao là Huy chương Fields:** Văn bản IMU 2010 tôn vinh một **phương pháp mới đầy uy lực**: kết hợp entropy dương, bất biến hạng cao (hoặc đối xứng Hecke/adelic) và động lực học thuần nhất để chinh phục những câu hỏi cốt lõi của lý thuyết số — nối tiếp trực tiếp tinh thần Giải Abel 2020 trong [Chương 8]({{ site.baseurl }}/contents/vi/chapter08/).

---

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/lindenstrauss-arithmetic-que_vi.mp4"></video>
</div>

Video dài khoảng 47 giây (có thuyết minh tiếng Việt): cực hạn duy nhất lượng tử số học (Arithmetic QUE) trên mặt hyperbolic và phân bố đều hàm riêng Laplace.

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "Giả thuyết Littlewood đã được chứng minh." | EKL: tập ngoại lệ có chiều Hausdorff bằng không. Phát biểu đầy đủ vẫn còn mở. |
| "QUE đã được chứng minh cho mọi mặt hyperbolic." | Chỉ cho dạng Hecke–Maass số học, trường hợp compact (Lindenstrauss); mặt modular thì cần thêm Soundararajan; QUE tổng quát vẫn mở. |
| "Lindenstrauss chứng minh QUE chỉnh hình." | Đó là Holowinsky–Soundararajan, bằng phương pháp khác. |
| "Độ cứng độ đo chính là định lý Ratner." | Ratner là phần lũy đơn; tác động chéo hạng cao là phần khác, mới giải được từng phần. |
| "Entropy dương chỉ là giả thiết phụ nhỏ." | Chính giả thiết này loại bỏ các độ đo bất biến kỳ quặc nhất. |
| "Fields 2010 giống Abel 2020." | Abel 2020 vinh danh cả sự nghiệp dùng động lực học của Furstenberg và Margulis; Lindenstrauss là một bước phát triển sau, ở tầm Fields. |

---

## Liên kết

- IMU Fields Medals 2010: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-2010)
- Lời tán dương IMU ICM 2010 (Lindenstrauss): [https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-elon-lindenstrauss.html](https://www.mathunion.org/fileadmin/IMU/ICM2010/offline/www.icm2010.in/prize-winners-2010/fields-medal-elon-lindenstrauss.html)
- Wikipedia — Elon Lindenstrauss: [https://en.wikipedia.org/wiki/Elon_Lindenstrauss](https://en.wikipedia.org/wiki/Elon_Lindenstrauss)
- Thông báo IAS (faculty 2024): [https://www.ias.edu/news/three-world-leading-mathematicians-join-ias-faculty](https://www.ias.edu/news/three-world-leading-mathematicians-join-ias-faculty)
- Soundararajan, QUE cho mặt modular (arXiv:0901.4060): [https://arxiv.org/abs/0901.4060](https://arxiv.org/abs/0901.4060)
- Tìm arXiv — Einsiedler Katok Lindenstrauss Littlewood: [https://arxiv.org/search/?query=Einsiedler+Katok+Lindenstrauss+Littlewood&searchtype=all](https://arxiv.org/search/?query=Einsiedler+Katok+Lindenstrauss+Littlewood&searchtype=all)
- Survey AMS Notices các Fields 2010: [https://www.ams.org/notices/201103/rtx110300453p.pdf](https://www.ams.org/notices/201103/rtx110300453p.pdf)

---

## Tài liệu tham khảo

1. Citation IMU Fields Medal 2010 — Elon Lindenstrauss.
2. M. Einsiedler, A. Katok và E. Lindenstrauss, “Invariant measures and the set of exceptions to Littlewood’s conjecture,” *Ann. of Math.* 164 (2006).
3. E. Lindenstrauss, “Invariant measures and arithmetic quantum unique ergodicity,” *Ann. of Math.* 163 (2006).
4. Z. Rudnick và P. Sarnak, “The behaviour of eigenstates of arithmetic hyperbolic manifolds,” *Comm. Math. Phys.* 161 (1994) — giả thuyết QUE.
5. K. Soundararajan, “Quantum unique ergodicity for $$\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$$,” *Ann. of Math.* 172 (2010).
6. R. Holowinsky và K. Soundararajan, “Mass equidistribution for Hecke eigenforms,” *Ann. of Math.* 172 (2010) — QUE chỉnh hình, phương pháp khác.
7. M. Ratner, phân loại độ đo và quỹ đạo cho dòng unipotent; H. Furstenberg, $$\times 2,\times 3$$ và disjointness; G. Margulis, dòng unipotent và Oppenheim.
8. B. Host và B. Kra, định lý cấu trúc cho trung bình ergodic bội (nhân tử nil).
9. Khóa học: [Furstenberg & Margulis]({{ site.baseurl }}/contents/vi/chapter08/08_05_Furstenberg_Margulis/), [Tổng quan Chương 8]({{ site.baseurl }}/contents/vi/chapter08/), [Venkatesh]({{ site.baseurl }}/contents/vi/chapter02/02_07_Venkatesh_Number_Theory/).

---

## Hướng đi tiếp

- Đọc một bài giảng ngắn về định lý Ratner trước khi đọc EKL, để thấy rõ phân loại cho trường hợp chéo còn thiếu những gì, thay vì coi hai bên như nhau.
- Bài tập thêm: viết một trang tóm tắt "Littlewood sau EKL", liệt kê những gì một chứng minh đầy đủ còn cần, nhưng không tự bịa ra chứng minh.

## Video tham khảo

- **Xem trước**: [Conferências Magnas: Elon Lindenstrauss - Homogeneous dynamics and diagonalizable actions (2013)](https://www.youtube.com/watch?v=e9Gj1yohLCw) (Instituto de Matemática Pura e Aplicada, tiếng Anh). Bài giảng lớn tại IMPA của chính Lindenstrauss về động lực học thuần nhất và tác động chéo hóa được, đúng chủ đề của mục 1 và 2.
- [Elon Lindenstrauss - An effective proof of the Oppenheim Conjecture](https://www.youtube.com/watch?v=_hOglF2XvQ8) (International Centre for Theoretical Sciences, tiếng Anh). Bài giảng về một chứng minh có đánh giá định lượng cho giả thuyết Oppenheim, thuộc phía lũy đơn của câu chuyện. Nên xem sau khi đã đọc mục 2.
