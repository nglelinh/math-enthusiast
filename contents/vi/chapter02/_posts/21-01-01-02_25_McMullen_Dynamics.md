---
layout: post
title: "Động lực chỉnh hình và hình học Teichmüller của McMullen (Huy chương Fields 1998)"
chapter: '02'
order: 25
owner: Nguyen Le Linh
lang: vi
categories:
- chapter02
---

Ai từng phóng to đường viền của **tập Mandelbrot** đều khó quên cảm giác choáng ngợp: ẩn sâu bên trong những sợi ren fractal vô tận lại hiện ra vô số bản sao tí hon của chính tập Mandelbrot ban đầu! Thoạt nhìn, thế giới của phép lặp hàm phức $$z \mapsto z^2 + c$$ trên mặt phẳng và thế giới của **hình học không gian ba chiều cong âm** (những đa tạp hyperbolic 3D trong chương trình hình học hóa của William Thurston) chẳng có chút liên hệ nào. Ấy vậy mà vào thập niên 1980–1990, từ điển Sullivan cùng những định lý sắc như dao của **Curtis T. McMullen** đã hé lộ sự thật bất ngờ: hai thế giới đó được vận hành bởi *cùng một động cơ* — **tái chuẩn hóa** và **tính cứng của hệ động lực bảo giác**.

Tại ICM Berlin năm 1998, **Curtis T. McMullen** nhận **Huy chương Fields** với lời trao giải chính thức:

> For his contributions to the theory of holomorphic dynamics and geometrization of three-manifolds, including proofs of Bers’ conjecture on the density of cusp points in the boundary of the Teichmüller space, and Kra’s theta-function conjecture.

*Tạm dịch: vì những đóng góp cho lý thuyết động lực học chỉnh hình và hình học hóa đa tạp ba chiều, trong đó có chứng minh giả thuyết Bers về tính trù mật của các điểm cusp trên biên không gian Teichmüller, và giả thuyết hàm theta của Kra.*

Bài học này dẫn bạn từ những ví dụ lặp hàm bậc hai cầm tay đến **không gian Teichmüller**, **biên Bers**, toán tử chuỗi Poincaré của **Kra**, và cầu nối sang **đa tạp hyperbolic ba chiều phân thớ trên đường tròn**. Cần phân định rõ ngay từ đầu: McMullen đóng góp các công cụ sắc bén *bên trong* chương trình hình học hóa của Thurston, chứ **không** phải người hoàn tất toàn bộ giả thuyết hình học hóa hay giả thuyết Poincaré — kỳ tích đó thuộc về [Grigori Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

**Mạch bài học:** Kiến thức cần nhớ (động lực chỉnh hình, không gian Teichmüller, từ điển Sullivan) → Ví dụ làm từng bước: lặp $$z^2 + c$$ tại $$c = 0, -2, -1$$ và hình ảnh bóp thắt vòng eo mặt giống $$g=2$$ thành cusp → Giả thuyết Bers & Giả thuyết hàm theta của Kra → Giải thích: tái chuẩn hóa nối tập Mandelbrot với đa tạp 3 chiều phân thớ trên đường tròn → Liên hệ tới Mirzakhani và Perelman.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Nhắc lại lời trao giải chính thức năm 1998 và nêu tên hai giả thuyết lớn được chứng minh (tính trù mật của điểm cusp theo Bers; giả thuyết hàm theta $$\|\Theta\| < 1$$ của Kra).
- Tự tay phân tích tập Fatou và tập Julia cho các trường hợp cơ sở $$z^2, z^2 - 2, z^2 - 1$$ và giải thích trực giác của **tái chuẩn hóa** (*quadratic-like maps*).
- Giải thích **không gian Teichmüller** $$\mathcal{T}(S)$$, phép nhúng Bers, và hình ảnh một **cusp cực đại** trên biên Bers khi các đường cong đóng bị bóp thắt lại.
- Trình bày tiêu chuẩn **khả trung bình** (*amenability*) của McMullen cho phép phủ mặt Riemann và cách nó kéo theo giả thuyết Kra.
- Phân biệt rõ đóng góp của McMullen trong **chương trình hình học hóa của Thurston** với chứng minh đầy đủ giả thuyết hình học hóa của Perelman, đồng thời nối dòng truyền thừa sang [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

**Kiến thức nền.** Hàm chỉnh hình trên $$\mathbb{C}$$ và mặt cầu Riemann $$\widehat{\mathbb{C}}$$; khái niệm mặt Riemann compact giống $$g\ge 2$$ với mêtric hyperbolic; quen với việc lặp một ánh xạ nhiều lần. Không cần học trước nhóm Klein (Kleinian groups).

**Liên kết với các bài khác.** Bài này minh họa một chương trình nghiên cứu tổ chức lại cả hình học lẫn động lực học. Các bài hình học liên quan: [Mirzakhani / moduli]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/). Những tên tuổi chính của động lực học phức: Fatou, Julia, Sullivan, Douady–Hubbard, Thurston, Yoccoz.

---

## Kiến thức cần nhớ: Động lực chỉnh hình, Không gian Teichmüller và Từ điển Sullivan là gì?

### 1. Động lực học chỉnh hình (Holomorphic Dynamics) nghiên cứu gì?
Cho một hàm hữu tỷ $$f: \widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$$ (đơn giản nhất là $$f_c(z) = z^2 + c$$). Lặp $$z \mapsto f(z) \mapsto f^{\circ 2}(z) \mapsto \cdots$$ chia mặt cầu Riemann thành hai tập bất biến:
- **Tập Fatou** (vùng ổn định): quanh mỗi điểm, các quỹ đạo lân cận có cùng số phận.
- **Tập Julia $$J(f)$$** (vùng hỗn loạn): ranh giới fractal mong manh nơi hai điểm sát nhau lập tức tách xa.
Còn trên mặt phẳng tham số $$c \in \mathbb{C}$$, **tập Mandelbrot** gồm mọi giá trị $$c$$ mà quỹ đạo của điểm tới hạn $$0$$ bị chặn (tương đương với $$J(f_c)$$ liên thông).

### 2. Không gian Teichmüller $$\mathcal{T}(S)$$
Cho mặt cong đóng định hướng $$S$$ có giống $$g \ge 2$$ (như bánh vòng $$g$$ lỗ). **Không gian Teichmüller** $$\mathcal{T}(S)$$ tham số hóa tất cả các cấu trúc hyperbolic (hay cấu trúc mặt Riemann) có đánh dấu trên $$S$$ — là một không gian mượt có chiều thực đúng bằng $$6g - 6$$. Khi quên nhãn đánh dấu đi (lấy thương theo nhóm lớp ánh xạ), ta thu được **không gian moduli** $$\mathcal{M}_g$$ trong [bài Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/).

### 3. Từ điển Sullivan — sự song hành kỳ lạ giữa 2D và 3D
Một **nhóm Klein** (nhóm con rời rạc các phép biến đổi Möbius trong $$\mathrm{PSL}(2,\mathbb{C})$$) vừa tác động bảo giác lên mặt cầu Riemann ở vô cực (chia mặt cầu thành miền ổn định và **tập giới hạn** fractal giống hệt Fatou/Julia), vừa là nhóm đẳng cự của **không gian hyperbolic 3 chiều** $$\mathbb{H}^3$$ nằm bên trong! **Dennis Sullivan** phát hiện từ điển song song giữa phép lặp hàm phức và hình học đa tạp hyperbolic 3 chiều — và McMullen là bậc thầy biến từ điển đó thành những định lý cứng cáp.

---

## 1. Ví dụ làm từng bước: lặp $$f_c(z) = z^2 + c$$ và hình ảnh bóp thắt tạo cusp

### Ví dụ 1: Ba giá trị $$c$$ giúp thấy ngay Tập Julia và Tập Mandelbrot
Hãy thử tự tính quỹ đạo lặp của $$f_c(z) = z^2 + c$$ với ba giá trị $$c$$ rất đơn giản:
1. **$$c = 0$$ ($$f_0(z) = z^2$$):**
   - Nếu $$\vert z \vert < 1$$: $$z^2, z^4, z^8 \to 0$$ (hút về gốc $$0$$).
   - Nếu $$\vert z \vert > 1$$: $$z^2, z^4, z^8 \to \infty$$ (thoát ra vô cực).
   - **Tập Julia** chính là đường tròn đơn vị $$\vert z \vert = 1$$ — ranh giới trơn giữa hai số phận!
2. **$$c = -2$$ ($$f_{-2}(z) = z^2 - 2$$):** Đặt $$z = 2\cos\theta$$, ta có ngay $$f_{-2}(2\cos\theta) = 4\cos^2\theta - 2 = 2\cos(2\theta)$$! Quỹ đạo của $$0$$ là $$0 \mapsto -2 \mapsto 2 \mapsto 2 \mapsto \cdots$$ (bị chặn, nên $$-2$$ nằm ở mũi nhọn tận cùng của tập Mandelbrot), còn **Tập Julia** sụp gọn thành đúng đoạn thẳng $$[-2, 2]$$!
3. **$$c = -1$$ ($$f_{-1}(z) = z^2 - 1$$):** Quỹ đạo của $$0$$ là $$0 \mapsto -1 \mapsto 0 \mapsto -1 \mapsto \cdots$$ (chu kỳ hút siêu ổn định độ dài 2). Tập Julia biến thành hình fractal nổi tiếng mang tên **vương cung thánh đường (basilica)** — có vô số đĩa con chạm nhau!

Bây giờ hãy hình dung phép **tái chuẩn hóa**: nếu ta chọn $$c$$ nằm trong một "tập Mandelbrot con" gắn vào chu kỳ độ dài $$p$$, thì khi thu hẹp ánh xạ lặp $$f_c^{\circ p}$$ vào một đĩa nhỏ quanh $$0$$, nó hành xử y hệt một đa thức bậc hai mới (Douady–Hubbard gọi là **ánh xạ dạng bậc hai** — *quadratic-like*). Nếu quá trình phóng to và thu hẹp đó lặp được **vô hạn lần**, ta có một đa thức *tái chuẩn hóa vô hạn lần* — đúng vùng khó nhất mà **Yoccoz** (Fields 1994, xử lý trường hợp hữu hạn lần) chưa chạm tới được và McMullen đã chinh phục trong chuyên khảo năm 1994!

### Ví dụ 2: Bóp thắt chiếc bánh vòng 2 lỗ ($$g = 2$$) thành một điểm cusp trên biên Bers
Hãy cầm một mặt đóng giống $$g = 2$$ (chiếc bánh vòng 2 lỗ). Ta có thể cắt nó thành **2 "chiếc quần" ba ống** bằng đúng $$3g - 3 = 3$$ vòng eo rời nhau (gọi là 3 đường cong đóng đơn). Không gian Teichmüller $$\mathcal{T}(S)$$ có $$6g - 6 = 6$$ thông số thực (độ dài và góc xoắn của 3 vòng eo đó).
- Khi các độ dài vòng eo đều dương, ta nằm **bên trong** miền bị chặn của **phép nhúng Bers**.
- Khi ta siết chặt một vòng eo cho độ dài tiến về $$0$$, phần mặt quanh vòng eo bị kéo thành hai cái phễu nhọn vô tận (**cusp**), đẩy ta ra **biên Bers** $$\partial\mathcal{T}(S)$$.
- Khi siết chặt đồng thời cả $$3$$ vòng eo cực đại, ta được một **cusp cực đại**!

**Giả thuyết Bers (1970)** hỏi liệu những điểm cusp cực đại bị bóp thắt hoàn toàn đó có nằm **trù mật** khắp toàn bộ biên Bers hay không. Trong bài báo *"Cusps are dense"* (*Ann. of Math.* 133, 1991), **McMullen chứng minh câu trả lời là CÓ!** Trên mép của không gian các mặt hyperbolic, sự suy biến không hề hiếm — nó nằm sát rạt mọi điểm biên!

---

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/mcmullen-mandelbrot-renorm_vi.mp4"></video>
</div>

Video dài khoảng 44 giây (có thuyết minh tiếng Việt): lặp $f_c(z)=z^2+c$ tại $c=0, -2, -1$, cơ chế tái chuẩn hóa sinh bản sao Mandelbrot tí hon và Từ điển Sullivan 2D–3D.

## 2. Giả thuyết hàm theta của Kra: tiêu chuẩn khả trung bình sắc bén

Xét một phép phủ các mặt Riemann hyperbolic $$Y \to X$$ (ví dụ phủ phổ dụng $$\mathbb{D} \to X = \mathbb{D}/\Gamma$$). Nó cảm sinh phép nhúng $$\mathcal{T}(X) \hookrightarrow \mathcal{T}(Y)$$, và theo ngôn ngữ đối ngẫu, sinh ra **toán tử chuỗi Poincaré** $$\Theta$$ (lấy trung bình vi phân bậc hai chỉnh hình trên $$\mathbb{D}$$ theo nhóm $$\Gamma$$). Ta luôn có $$\|\Theta\| \le 1$$; **giả thuyết hàm theta của Irwin Kra** khẳng định $$\|\Theta\| < 1$$ (co chặt!) đối với mọi mặt kiểu hữu hạn.

Năm 1989 (*Invent. Math.* 97), **McMullen** chứng minh một tiêu chuẩn tôpô–đại số hoàn hảo cho mọi phép phủ $$Y \to X$$:

$$
\|\Theta\| = 1 \quad \Longleftrightarrow \quad \text{phép phủ } Y \to X \text{ là khả trung bình (amenable)}.
$$

Vì nhóm cơ bản của mặt hyperbolic kiểu hữu hạn chứa nhóm tự do nên *không* khả trung bình, bất đẳng thức chặt $$\|\Theta\| < 1$$ lập tức suy ra! Và một phép **co chặt** trên không gian Teichmüller chính là chiếc chìa khóa điểm bất động mở cửa vào hình học hóa đa tạp 3 chiều!

---

## 3. Giải thích: Tái chuẩn hóa nối Động lực học phức với Đa tạp 3 chiều như thế nào?

Tại sao hai chuyên khảo kinh điển của McMullen — *Complex Dynamics and Renormalization* (1994) và *Renormalization and 3-Manifolds Which Fiber over the Circle* (1996) — lại là hai mặt của cùng một đồng xu? Hãy đi chậm qua 4 bước song song:

#### Bước 1: Định lý điểm bất động trên không gian tham số
- *Phía động lực học phức:* Phép tái chuẩn hóa $$\mathcal{R}$$ biến một ánh xạ dạng bậc hai thành một ánh xạ dạng bậc hai mới ở thang nhỏ hơn. Ta cần chứng minh dãy tái chuẩn hóa hội tụ về một **điểm bất động duy nhất** (tính cứng).
- *Phía đa tạp 3 chiều:* Lấy một mặt $$S$$ nhân với $$[0,1]$$ rồi dán hai đáy bằng một phép xoắn giả Anosov $$\psi: S \to S$$ để tạo thành **đa tạp 3 chiều phân thớ trên đường tròn**. Muốn đặt mêtric hyperbolic lên nó, Thurston cần tìm **điểm bất động** của toán tử dán biên (*skinning map*) tác động trên không gian Teichmüller $$\mathcal{T}(S)$$.

#### Bước 2: Dùng biến dạng tựa bảo giác để đo "độ mềm dẻo"
Muốn chứng minh hai đối tượng trùng nhau (tính cứng) hay toán tử là co chặt, ta giả sử tồn tại một biến dạng tựa bảo giác không tầm thường (phân bố hình elip vô cùng nhỏ trên mặt cầu Riemann) và kiểm tra nó phản ứng thế nào dưới phép lặp hoặc dưới phép phủ.

#### Bước 3: Định lý co chặt (Kra) và tính không uốn được (Inflexibility)
Nhờ tiêu chuẩn khả trung bình (chứng minh $$\|\Theta\| < 1$$ cho giả thuyết Kra) và định lý **không uốn được định lượng** cho các đa tạp hyperbolic mở (bổ sung cho định lý cứng Mostow), McMullen chứng minh rằng khi lùi sâu vào trong các "tháp tái chuẩn hóa" (hoặc các phủ vô hạn của đa tạp 3 chiều), mọi biến dạng tựa bảo giác đều bị **bóp co theo cấp số nhân** về $$0$$!

#### Bước 4: Ranh giới rạch ròi giữa McMullen và Perelman
Hệ quả là McMullen vừa chứng minh tính cứng cho lớp lớn các đa thức tái chuẩn hóa vô hạn lần trong tập Mandelbrot, vừa dựng nên một chứng minh hoàn toàn mới, thống nhất cho **định lý hyperbolic hóa của Thurston trên đa tạp 3 chiều phân thớ trên đường tròn**!
Nhưng cần nói thật chính xác: McMullen làm việc *bên trong* chương trình hình học hóa của Thurston bằng động lực học bảo giác; còn người **hoàn tất toàn bộ giả thuyết hình học hóa và giả thuyết Poincaré** cho mọi đa tạp 3 chiều bằng dòng Ricci có phẫu thuật là [Grigori Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

Tóm tắt cầu nối McMullen:

$$
\text{Từ điển Sullivan}
\;\longrightarrow\;
\text{Bers (cusp trù mật) + Kra (}\|\Theta\| < 1\text{)}
\;\longrightarrow\;
\text{Tính cứng tái chuẩn hóa (2D phức }\leftrightarrow\text{ 3D phân thớ)}.
$$

---

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/mcmullen-bers-kra-cusp_vi.mp4"></video>
</div>

Video dài khoảng 50 giây (có thuyết minh tiếng Việt): bóp thắt mặt giống $g=2$ thành điểm cusp trù mật trên biên Bers và tiêu chuẩn khả trung bình cho giả thuyết hàm theta Kra.

## 4. Dòng truyền thừa và vì sao là Huy chương Fields

Cùng cách nhìn hình học–động lực học trên không gian Teichmüller và mặt hyperbolic đó sau này được tiếp nối rực rỡ qua thế hệ học trò của McMullen tại Harvard — nổi bật nhất là **Maryam Mirzakhani** (xem [bài Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/)).

**Vì sao là Huy chương Fields 1998:**
1. Giải quyết hai giả thuyết mang tên tuổi tồn tại lâu năm (**Bers** về biên Teichmüller và **Kra** về chuẩn toán tử chuỗi Poincaré $$\|\Theta\| < 1$$).
2. Biến từ điển tái chuẩn hóa của Sullivan thành một cỗ máy chứng minh thực sự chạy thông suốt giữa động lực học chỉnh hình và đa tạp hyperbolic ba chiều.
3. Gắn kết ba lĩnh vực lớn (động lực học phức, lý thuyết Teichmüller, tôpô 3 chiều) bằng cùng một cơ chế về tính compact và tính cứng bảo giác.

Cùng nhận Huy chương Fields năm 1998 tại Berlin là **Richard Borcherds**, **Timothy Gowers** và **Maxim Kontsevich**.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| "McMullen đã chứng minh hình học hóa / Poincaré." | Hình học hóa đầy đủ là của Perelman. McMullen đóng góp trong chương trình Thurston (hyperbolic hóa đa tạp phân thớ / tái chuẩn hóa). |
| "Cusp trù mật nghĩa là mọi mặt Riemann đều có cusp." | Định lý nói về *biên Bers* của không gian Teichmüller, không nói về một mặt trơn điển hình ở bên trong. |
| "Không gian Teichmüller là không gian moduli." | Không gian Teichmüller giữ thông tin đánh dấu; không gian moduli là thương theo nhóm lớp ánh xạ. |
| "Tập Julia = tập Mandelbrot." | Tập Julia nằm trên mặt phẳng động lực của một ánh xạ; tập Mandelbrot nằm trên mặt phẳng tham số của cả một họ. |
| "Tái chuẩn hóa chỉ là phóng to một bức tranh." | Đó là phép dựng một ánh xạ mới từ ánh xạ dạng bậc hai, kèm một lý thuyết về tính cứng. |
| "Huy chương chỉ vì Bers + Kra." | Đó là hai mục được nêu tên; lời trao giải còn nhắc tới động lực học chỉnh hình và hình học hóa đa tạp ba chiều. |
| "McMullen đã phân loại mọi ánh xạ hữu tỷ." | Không. Công trình nói về tính cứng, tính trù mật và tái chuẩn hóa, không phải liệt kê các lớp liên hợp. |

---

## Liên kết

- Trang Huy chương Fields của IMU: [https://www.mathunion.org/imu-awards/fields-medal](https://www.mathunion.org/imu-awards/fields-medal)
- Huy chương Fields 1998: [https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998](https://www.mathunion.org/imu-awards/fields-medal/fields-medals-1998)
- Wikipedia, Curtis T. McMullen: [https://en.wikipedia.org/wiki/Curtis_T._McMullen](https://en.wikipedia.org/wiki/Curtis_T._McMullen)
- Trang Harvard của McMullen: [https://people.math.harvard.edu/~ctm/](https://people.math.harvard.edu/~ctm/)
- Khóa học: [Mirzakhani / moduli]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman / Poincaré]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/)
- Tìm arXiv, McMullen dynamics: [https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all](https://arxiv.org/search/?query=McMullen+Teichmuller+dynamics&searchtype=all)

---

## Tài liệu tham khảo

1. Citation chính thức Fields Medal 1998 cho C. T. McMullen (IMU / ICM Berlin); xem thêm diễn từ của Yuri Manin với tư cách chủ tịch ủy ban.
2. **S. Smale**, “The work of Curtis T. McMullen,” *Doc. Math.*, Extra Vol. ICM 1998.
3. **C. T. McMullen**, “Cusps are dense,” *Ann. of Math.* **133** (1991).
4. **C. T. McMullen**, “Amenability, Poincaré series and quasiconformal maps,” *Invent. Math.* **97** (1989) (giả thuyết theta của Kra).
5. **C. T. McMullen**, *Complex Dynamics and Renormalization*, Ann. of Math. Studies **135**, Princeton, 1994.
6. **C. T. McMullen**, *Renormalization and 3-Manifolds Which Fiber over the Circle*, Ann. of Math. Studies **142**, Princeton, 1996.
7. Nền: Douady–Hubbard về ánh xạ quadratic-like và tập Mandelbrot; Sullivan về phân thớ mặt Riemann và từ điển với nhóm Kleinian; Thurston về hình học hóa (các trường hợp Haken / phân thớ).
8. Khóa học: [Mirzakhani]({{ site.baseurl }}/contents/vi/chapter02/02_05_Mirzakhani_Moduli/), [Perelman]({{ site.baseurl }}/contents/vi/chapter02/02_03_Perelman_Poincare/).

---

## Hướng đi tiếp

- Đọc bài giới thiệu ngắn của Smale tại ICM trước khi đọc hai cuốn sách năm 1994 và 1996.
- So sánh biên Bers với biên của tập Mandelbrot: cả hai được dự đoán là có cấu trúc phân lá (Thurston; Douady–Hubbard). Kết quả trù mật cusp của McMullen ủng hộ một phía của sự tương tự này.
- Bài tập thêm: lập một "từ điển" một trang gồm ba cặp khái niệm song song (ánh xạ hữu tỷ / nhóm Klein; tập Julia / tập giới hạn; tái chuẩn hóa / hyperbolic hóa đa tạp phân thớ), nhưng không khẳng định rằng từ điển này là một tương đương chặt chẽ.

## Video tham khảo

- **Xem trước**: [Curtis McMullen: Manifolds, topology and dynamics](https://www.youtube.com/watch?v=g0fQDrV-UuE) (The Abel Prize, tiếng Anh). McMullen nói về đa tạp, tôpô và động lực học ở mức đại chúng. Phù hợp để làm quen với các chủ đề trước khi đọc bài.
- [Planes in number theory, geometry and dynamics: C. McMullen](https://www.youtube.com/watch?v=hlDDHnk5aRU) (Fields Institute, tiếng Anh). Bài giảng về vai trò của các mặt phẳng trong lý thuyết số, hình học và động lực học. Thuộc giai đoạn sau giải Fields, nên xem sau khi đã đọc xong bài.
- [Dynamics on K3 Surfaces - Curtis McMullen](https://www.youtube.com/watch?v=gWTi1xvGMb8) (Stony Brook Mathematics, tiếng Anh). Bài giảng về động lực học trên mặt K3, một hướng nghiên cứu khác của McMullen. Dùng làm góc nhìn bổ sung, không thuộc lời trao giải 1998.
