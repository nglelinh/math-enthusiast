---
layout: post
title: "Giải tích → Vật lý & Kỹ thuật"
chapter: '03'
order: 2
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
---

Một cây cầu không đứng vững vì ai đó “dùng công thức.” Nó đứng vững vì **tốc độ biến thiên cục bộ** của ứng suất và chuyển vị bị ràng buộc bởi các định luật cân bằng, rồi được tích phân—giải tích hoặc số—thành một thiết kế chịu tải, gió và mỏi. Đường ống đó là giải tích như hạ tầng.

**Lộ trình:** tốc độ và tích lũy → định lý cơ bản → định luật Newton như ODE → không gian bước vào (PDE) → tư duy biến phân → phần tử hữu hạn → các lĩnh vực kỹ thuật → nhầm lẫn thường gặp.

Bài này không phải khóa đạo hàm lần đầu. Đây là bản đồ **vì sao giải tích trở thành tiếng mẹ đẻ của vật lý cổ điển và phần lớn kỹ thuật**, và ý tưởng chính xác nào làm cho mô phỏng, điều khiển và thiết kế khả thi.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Giải thích đạo hàm và tích phân như hai phép toán đôi, nối bởi định lý cơ bản của giải tích.
- Viết định luật hai Newton như phương trình vi phân và diễn giải lực, khối lượng, gia tốc trong ngôn ngữ đó.
- Phân biệt ODE và PDE; nêu ví dụ chuẩn (nhiệt, sóng, Laplace).
- Mô tả, mức khẩu hiệu, cách **phương pháp phần tử hữu hạn (FEM)** biến luật cân bằng liên tục thành bài toán đại số tuyến tính lớn.
- Kể ba lĩnh vực kỹ thuật “nói” giải tích trôi chảy và *cái gì* đang được đạo hàm/tích phân.
- Tránh nhầm: “giải tích chỉ là công thức phổ thông” và “phần mềm thay thế toán.”

**Kiến thức nền.** Trực giác giải tích phổ thông (độ dốc, diện tích). Hàm nhiều biến hữu ích cho PDE.

**Liên kết.** [Phương trình vi phân]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/), [Navier–Stokes (Ch.1)]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), Fourier trong chương này.

---

## 1. Hai ý tưởng, một động cơ

**Đạo hàm** trả lời: cái gì đang đổi *ngay lúc này* nhanh ra sao? Vận tốc là đạo hàm vị trí; dòng điện có thể là tốc độ đổi điện tích; chi phí biên là đạo hàm tổng chi phí.

**Tích phân** trả lời: sự đổi tích lũy thế nào trên một khoảng? Quãng đường là tích phân tốc độ; công là tích phân lực theo đường; nhiệt tổng là tích phân mật độ trên vật thể.

**Định lý cơ bản của giải tích** là bản lề: dưới giả thiết phù hợp, đạo hàm và tích phân là nghịch đảo nhau. Vật lý được viết trên bản lề đó:

$$
\int_a^b f(x)\,dx = F(b)-F(a)\quad\text{khi }F'=f.
$$

Khẩu hiệu khóa học: **giải tích là đại số của sự biến thiên liên tục.**

---

## 2. Từ hình học đến động lực học

Lịch sử: giải tích sinh từ hình học (tiếp tuyến, diện tích) và trở thành công cụ **động lực học**. Newton và Leibniz không chỉ “phát minh mẹo thi”; họ phát minh ngôn ngữ cho sự đổi liên tục.

**Định luật hai Newton** một chiều,

$$
m \frac{d^2 x}{dt^2} = F\bigl(x,\tfrac{dx}{dt},t\bigr),
$$

đã là phương trình vi phân: ẩn số là *hàm* $$x(t)$$. Cơ học cổ điển là vũ trụ các phương trình như vậy.

**Cơ chế một câu.**  
*Các định luật vật lý thường nói tốc độ đổi của trạng thái phụ thuộc chính trạng thái; giải phương trình vi phân dự đoán tương lai từ dữ liệu ban đầu.*

---

## 3. ODE và PDE: khi không gian bước vào

**ODE** đạo hàm theo một biến độc lập (thường là thời gian). Hệ khối–lò xo–giảm chấn là ODE.

**PDE** có nhiều biến độc lập—không gian và thời gian. Phương trình nhiệt

$$
\partial_t u = \kappa \Delta u
$$

nói nhiệt độ đổi tỉ lệ với Laplacian (làm mượt cục bộ). Phương trình sóng $$\partial_{tt}u=c^2\Delta u$$ truyền nhiễu với tốc độ hữu hạn $$c$$. Laplace $$\Delta u=0$$ mô tả thế cân bằng.

**Vì sao công nghệ quan tâm.** Mô hình ODE thống trị mạch tập trung, cơ học vật rắn, nhiều vòng điều khiển. PDE thống trị trường liên tục: nhiệt, ứng suất, điện từ (Maxwell), chất lỏng (Navier–Stokes). “Mô phỏng” công nghiệp thường là: rời rạc hóa PDE, giải hệ đại số lớn, trực quan hóa—vẫn là giải tích cộng phân tích số.

---

## 4. Bảo toàn, thông lượng, mẫu continuum

Nhiều vật lý continuum theo một khuôn:

1. Chọn đại lượng (khối lượng, năng lượng, động lượng, điện tích).  
2. Viết **luật cân bằng**: tốc độ đổi trong miền = thông lượng qua biên + nguồn.  
3. Đưa dạng tích phân thành PDE nhờ **định lý divergence** (Green/Stokes/Gauss là họ hàng—xem [Vật lý toán / Stokes→Maxwell]({{ site.baseurl }}/contents/vi/chapter06/06_11_Mathematical_Physics/)).  
4. Đóng hệ bằng **luật cấu thành** (Fourier: thông lượng nhiệt $$\propto -\nabla u$$; Hooke: ứng suất–biến dạng; Ohm; …).

Với nhiệt: luật Fourier + cân bằng năng lượng → phương trình nhiệt. Toán không trang trí: định lý divergence là lý do “kế toán” tích phân thành PDE.

**Cơ chế.** *Bảo toàn + đáp ứng cấu thành → PDE; hình học miền và điều kiện biên chọn nghiệm vật lý.*

---

## 5. Gradient, divergence và curl (bộ công cụ vector calculus)

Mô hình continuum nói bằng **trường**: **trường vô hướng** gán một số cho mỗi điểm (nhiệt độ, cao độ), **trường vector** gán một vector (gió, vận tốc). Ba toán tử từ ký hiệu del $$\nabla$$ xuất hiện khắp vật lý–kỹ thuật.

### Trường vô hướng / vector

| Đối tượng | Ý nghĩa | Ví dụ |
|-----------|---------|--------|
| Vô hướng | Chỉ độ lớn | Nhiệt $$30^\circ\mathrm{C}$$ |
| Vector | Độ lớn + hướng | Gió 10 đơn vị về đông |
| Trường vô hướng | Số tại mỗi điểm | Bản đồ nhiệt $$T(x,y)$$ |
| Trường vector | Vector tại mỗi điểm | Bản đồ gió $$\mathbf{v}(x,y)$$ |

![Trường vector]({{ site.baseurl }}/img/chapter_img/veccalc_vector_field_example_bs.jpg)

*Hình. Trường $$\mathbf{v}(x,y)=(2x,y)$$ (nguồn: Brain Station Advanced).*

### Gradient: dốc nhất lên dốc

$$
\nabla f = \Bigl(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\ldots\Bigr).
$$

**Trực giác.** $$\nabla f$$ chỉ hướng **tăng nhanh nhất** của $$f$$ (đẩy bóng lên dốc). Bóng lăn tự nhiên theo $$-\nabla f$$ (xuống dốc / gradient descent).  
**Ví dụ.** $$f=x^2+y^2$$, tại $$(1,2)$$ có $$\nabla f=(2,4)$$.

![Gradient lên dốc]({{ site.baseurl }}/img/chapter_img/veccalc_gradient_uphill_bs.jpg)

*Hình. Gradient của $$f=x^2+y^2$$ (cùng nguồn).*

### Divergence: nguồn, hố hút, dòng không nén

$$
\nabla\cdot\mathbf{v} = \frac{\partial v_1}{\partial x}+\frac{\partial v_2}{\partial y}+\frac{\partial v_3}{\partial z}
$$

là **vô hướng**. Hình dung ô vuông nhỏ trong dòng chảy:

| Dấu $$\nabla\cdot\mathbf{v}$$ | Ý nghĩa |
|------------------------------|---------|
| $$>0$$ | Ra nhiều hơn vào → mật độ giảm (nguồn) |
| $$<0$$ | Vào nhiều hơn ra → mật độ tăng (hố hút) |
| $$=0$$ | Vào = ra (quay, hoặc dòng đều) |

**Ví dụ.** $$\mathbf{v}=(x,y)$$ → div $$=2$$; $$\mathbf{v}=(-x,-y)$$ → div $$=-2$$; quay $$\mathbf{v}=(-y,x)$$ hoặc trường hằng → div $$=0$$.

![Nguồn]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_source_bs.jpg)

*Hình. Trường hướng ra ngoài: divergence dương (cùng nguồn video).*

![Sink]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_sink_bs.jpg)

*Hình. Trường hướng vào trong: divergence âm (cùng nguồn).*

![Dòng đều]({{ site.baseurl }}/img/chapter_img/veccalc_divergence_uniform_bs.jpg)

*Hình. Dòng đều: $$\nabla\cdot\mathbf{v}=0$$ (cùng nguồn).*

Trong điện từ, điện tích dương như **nguồn** của $$\mathbf{E}$$. Cùng định lý divergence, đây là bước biến cân bằng tích phân thành PDE (§4).

### Curl: xoay cục bộ (bánh đạp)

Curl là **tích có hướng** $$\nabla\times\mathbf{v}$$ (vector). Đặt bánh đạp nhỏ trong dòng: nếu dòng làm bánh quay, curl ≠ 0; nếu chỉ tịnh tiến, curl = 0.

![Curl]({{ site.baseurl }}/img/chapter_img/veccalc_curl_paddle_bs.jpg)

*Hình. Trường quay và trực giác bánh đạp (cùng nguồn).*

### Bảng tóm

| Toán tử | Đầu ra | Khẩu hiệu vật lý |
|---------|--------|------------------|
| $$\nabla f$$ | vector | Đổi dốc nhất của vô hướng (lực từ thế; Fourier dùng $$-\nabla T$$) |
| $$\nabla\cdot\mathbf{v}$$ | vô hướng | Cường độ nguồn/hố hút (phương trình liên tục, Gauss) |
| $$\nabla\times\mathbf{v}$$ | vector | Xoay cục bộ (vorticity; cấu trúc Maxwell) |

---

## 6. Nguyên lý biến phân

Nhiều bài cân bằng là **biến phân**: cấu hình vật lý làm cực tiểu (hoặc dừng) một năng lượng / action. Nguyên lý Dirichlet: trong các hàm có biên cố định, hàm cực tiểu

$$
E[u]=\frac12\int_\Omega\lvert\nabla u\rvert^2\,dx
$$

giải Laplace (dưới giả thiết phù hợp)—hàm “phẳng nhất” khớp biên. Đàn hồi tuyến tính, mặt cực tiểu, và nhiều FEM sống trong thế giới này: xấp xỉ năng lượng trên không gian hữu hạn chiều rồi tối thiểu hóa—giải tích biến phân → ma trận thưa → bộ giải.

**Cơ chế.** *Cân bằng = điểm dừng của năng lượng; FEM xấp xỉ không gian hàm rồi tối thiểu (hoặc giải dạng yếu tương đương).*

---

## 7. Phần tử hữu hạn: giải tích công nghiệp hóa

Quy trình skeleton:

1. Chia miền thành phần tử (tam giác, tứ diện, …).  
2. Hạn chế ẩn số trên không gian đa thức từng mảnh (liên tục hoặc discontinuous theo họ phương pháp).  
3. Ép **dạng yếu** (tích phân / biến phân) của PDE.  
4. Lắp hệ $$KU=F$$ (hoặc phi tuyến / phụ thuộc thời gian) và giải.

**Dạng yếu một dòng.** Nhân PDE với hàm thử, tích phân từng phần, chuyển đạo hàm sang hàm thử—bước làm cho xấp xỉ tuyến tính từng mảnh hợp lệ (yếu hơn điểm từng điểm).

**Cơ chế.** *FEM không bỏ toán liên tục; nó chiếu bài giải tích vô hạn chiều xuống đại số tuyến tính cao chiều mà máy tính tấn công được.*

Họ hàng: sai phân hữu hạn (lưới đều, trực quan), thể tích hữu hạn (bảo toàn rời rạc—CFD), phổ (chuỗi Fourier / hàm riêng).

---

## 8. Các lĩnh vực kỹ thuật nói “giải tích”

| Lĩnh vực | Giải tích làm gì |
|----------|------------------|
| Cơ khí | Ứng suất, dao động, đàn hồi, tiếp xúc |
| Điện | ODE mạch; PDE Maxwell / tĩnh điện |
| Xây dựng | Dầm, đường tải, FEM công trình |
| Hàng không | Động lực bay; CFD (liên kết [NS]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/)) |
| Nhiệt–hóa | Truyền nhiệt/khối; phản ứng–khuếch tán |
| Điều khiển | Tuyến tính hóa; ổn định; biến đổi Laplace |

**Điều khiển:** tuyến tính hóa $$\dot{x}=f(x,u)$$ quanh điểm làm việc cho $$\dot{\xi}=A\xi+B\mu$$. Giá trị riêng của $$A$$ và tính điều khiển được quyết định phản hồi có ổn định được hệ hay không—đại số tuyến tính + ODE, vẫn là giải tích.

---

## 9. Mô hình liên tục và “digital twin”

Kỹ thuật hiện đại ghép cảm biến, mô hình và tối ưu theo vòng: mô hình ODE/PDE → ước lượng trạng thái từ đo → tối ưu đầu vào / bảo trì dự đoán. **Digital twin** của turbine hay cầu thường là giải tích (hoặc surrogate) hiệu chỉnh bằng dữ liệu—không phải ma thuật riêng biệt với PDE.

Giới hạn: rối loạn, tiếp xúc, nứt, đa pha, đa thang làm căng cả phân tích lẫn số trị. **Well-posedness** (tồn tại, duy nhất, phụ thuộc liên tục) là tính chất toán có hệ quả kỹ thuật: bài ill-posed không “cứ mesh mịn hơn là xong.”

---

## 10. Vì sao vẫn cần hiểu khi phần mềm “tự giải”

1. Sai **mô hình** thường lớn hơn sai rời rạc hóa.  
2. **Điều kiện biên** mã hóa vật lý bạn chọn—phần mềm không chọn hộ triết lý.  
3. **Không thứ nguyên hóa** lộ hạng tử quan trọng (Reynolds, Fourier, …).  
4. Ổn định / cứng của tích phân thời gian là khái niệm giải tích (bước thời gian, implicit/explicit).  
5. Xác minh–xác thực đòi hỏi biết bài liên tục *nên* làm gì trước khi tin màu sắc trên màn hình.

Chuỗi cơ chế: **cân bằng vật lý → phương trình vi phân → phân tích/số trị → quyết định thiết kế.**

---

### Khẩu hiệu giải tích vector (từ nghiên cứu video)

Video trực quan chính: [Brain Station — Gradient, Divergence and Curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) (~15 phút).

- **Gradient:** $$\nabla f$$ là vector các đạo hàm riêng; hướng **lên dốc** (tăng nhanh nhất). Xuống dốc dùng $$-\nabla f$$.
- **Divergence:** $$\nabla\cdot\mathbf{v}$$ là *vô hướng*. Dương ≈ nguồn, âm ≈ hố, không ≈ bảo toàn thể tích (vẫn có thể chuyển động).
- **Curl:** $$\nabla\times\mathbf{v}$$ đo quay cục bộ (thử bánh lái nhỏ).
- Kết hợp [Essence of calculus — 3Blue1Brown](https://www.youtube.com/watch?v=WUvTyaaNkzM) cho định lý cơ bản trước các toán tử vector.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “Giải tích chỉ để thi.” | Là ngôn ngữ biến thiên liên tục của vật lý–kỹ thuật. |
| “Phần mềm hội tụ ⇒ mô hình đúng.” | Hội tụ là số trị; sai mô hình/BC vẫn còn. |
| “ODE và PDE khó như nhau.” | PDE vô hạn chiều theo không gian; lý thuyết và số khác hẳn. |
| “FEM thay giải tích.” | FEM *là* giải tích biến phân rời rạc + đại số tuyến tính. |
| “Lưới mịn hơn luôn cứu mọi thứ.” | Giảm sai rời rạc; không sửa mô hình vật lý sai. |
| “Gradient chỉ xuống dốc.” | $$\nabla f$$ chỉ **lên dốc**; $$-\nabla f$$ mới là xuống dốc. |
| “Div = 0 nghĩa là chất lỏng đứng yên.” | Div = 0 nghĩa là không nguồn/hố hút ròng; dòng vẫn có thể chảy (quay, dòng đều). |

---

## Bài tập

1. Với $$s(t)=\frac12 gt^2$$, tính vận tốc và gia tốc; diễn giải.  
2. Ba câu: vì sao “tốc độ cục bộ” và “tích lũy” phải liên kết.  
3. Phân loại ODE/PDE: mạch RC; nhiệt trên thanh; quỹ đạo hành tinh.  
4. Một câu nối luật Fourier với phương trình nhiệt.  
5. **Vector calculus.** Với $$f=x^2+y^2$$ tính $$\nabla f$$ tại $$(1,2)$$. Với $$\mathbf{v}=(x,y)$$ và $$\mathbf{w}=(-y,x)$$ tính divergence; diễn giải dấu.  
6. Vì sao dạng yếu cho phép xấp xỉ tuyến tính từng mảnh?  
7. Chọn một thiết bị bạn dùng; nêu một đại lượng được đạo hàm/tích phân trong mô hình thiết kế.  
8. Nâng cao: dạng yếu của $$-u''=f$$ trên $$(0,1)$$, $$u(0)=u(1)=0$$.

---

## Video phổ thông

- **Nguồn:** [Best Explanation of Gradient, Divergence and Curl — Brain Station Advanced](https://www.youtube.com/watch?v=m_Psx7CdvDk) (~15 phút; 2026-08-03).  
  Trường vô hướng/vector → gradient lên dốc → divergence nguồn/hố hút → curl bánh đạp.

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/calculus-physics-engineering/`.

**Thứ tự xem gợi ý**

1. **ORIENTATION** — 3Blue1Brown — Essence of calculus (series / ch.1 derivative): [https://www.youtube.com/watch?v=WUvTyaaNkzM](https://www.youtube.com/watch?v=WUvTyaaNkzM).
2. **ORIENTATION** — 3Blue1Brown — Essence of calculus playlist hub: [https://www.3blue1brown.com/topics/calculus](https://www.3blue1brown.com/topics/calculus).
3. **CORE** — Brain Station Advanced — Gradient, Divergence and Curl: [https://www.youtube.com/watch?v=m_Psx7CdvDk](https://www.youtube.com/watch?v=m_Psx7CdvDk).
4. **FOUNDATION** — Khan Academy / 3B1B style multivariable (divergence theorem culture): [https://www.youtube.com/watch?v=rB83DpBJQsE](https://www.youtube.com/watch?v=rB83DpBJQsE).
5. **FOUNDATION** — MIT OCW 18.02 Multivariable Calculus (course page): [https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/](https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/).
6. **FOUNDATION** — MIT OCW 18.03 Differential Equations (video lectures): [https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/](https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/).

Danh mục URL đầy đủ: `research/video-research/calculus-physics-engineering/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/calculus-physics-engineering/transcripts/` · trạng thái: `research/video-research/calculus-physics-engineering/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/calculus-physics-engineering_WUvTyaaNkzM_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/calculus-physics-engineering/references.md`.

### Video (lộ trình chính)

1. 3Blue1Brown — Essence of calculus (series / ch.1 derivative) — https://www.youtube.com/watch?v=WUvTyaaNkzM
2. 3Blue1Brown — Essence of calculus playlist hub — https://www.3blue1brown.com/topics/calculus
3. Brain Station Advanced — Gradient, Divergence and Curl — https://www.youtube.com/watch?v=m_Psx7CdvDk
4. Khan Academy / 3B1B style multivariable (divergence theorem culture) — https://www.youtube.com/watch?v=rB83DpBJQsE
5. MIT OCW 18.02 Multivariable Calculus (course page) — https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/
6. MIT OCW 18.03 Differential Equations (video lectures) — https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/video_galleries/video-lectures/
7. Gilbert Strang & Cleve Moler — Learn Differential Equations (overview) — https://ocw.mit.edu/courses/res-18-009-learn-differential-equations-up-close-with-gilbert-strang-and-cleve-moler-fall-2015/
8. 3Blue1Brown — Divergence and curl playlist (multivariable) — https://www.3blue1brown.com/topics/multivariable-calculus

### Video (tìm thêm / phụ)

9. Numberphile / related continuum modeling culture (optional) — https://www.youtube.com/user/numberphile

### Bài báo, sách, OCW và web

10. Evans — Partial Differential Equations (AMS Graduate Studies): https://bookstore.ams.org/gsm-19-r
11. Wikipedia — Fundamental theorem of calculus: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
12. Wikipedia — Finite element method: https://en.wikipedia.org/wiki/Finite_element_method
13. MIT OCW 18.02: https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/
14. MIT OCW 18.03: https://ocw.mit.edu/courses/18-03-differential-equations-spring-2010/

### Trong khóa

15. Khóa học: [Tổng quan]({{ site.baseurl }}/contents/vi/chapter03/03_00_Tong_quan/), [PTVP]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Fourier]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/). Gói: `research/video-research/calculus-physics-engineering/`.

## Hướng đi tiếp

- Tiếp: [Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/), [PTVP]({{ site.baseurl }}/contents/vi/chapter03/03_09_Differential_Equations_Applications/).  
- Bài thuần túy liên quan: [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/).  
- Tùy chọn: xem [video grad/div/curl](https://www.youtube.com/watch?v=m_Psx7CdvDk) rồi đọc lại §5.  
- Viết lại cơ chế cốt lõi một đoạn; ghi một câu hỏi còn mở.
