---
layout: post
title: "Giả thuyết Kakeya"
chapter: '01'
order: 8
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
---

> **Lộ trình học A — Kakeya (3 bước)**  
> **1. Bạn đang ở đây:** Ch.1 bản đồ bài toán  
> **2. Tiếp theo:** [Bài Wang Ch.2 (Fields 2026)]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/) — lý thuyết đầy đủ  
> **3. Sau đó:** [Studio Kakeya Ch.7]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/) — vẽ / code / viết  
> *Thời gian gợi ý:* ~45 phút bản đồ → ~2–3 giờ bài giảng → ~1–2 giờ studio.

**Giả thuyết tập Kakeya** hỏi một tập trong $$\mathbb{R}^n$$ phải “lớn” thế nào nếu chứa đoạn đơn vị theo mọi hướng. Các tập kiểu này có thể có **độ đo Lebesgue bằng 0** (Besicovitch), nhưng được phỏng đoán có **chiều Hausdorff** đầy đủ $$n$$. Ở chiều 3, giả thuyết đã được **Hong Wang** và **Joshua Zahl** (2025) chứng minh; Wang nhận **Fields Medal 2026** một phần nhờ công trình này và harmonic analysis liên quan.

Đây là **bản đồ bài toán Chương 1**. Bài giảng đầy đủ: bước 2 của lộ trình trên.

Nếu $$K\subset\mathbb{R}^n$$ chứa đoạn đơn vị mọi hướng, có bắt buộc $$\dim_H(K)=\dim_M(K)=n$$? Chứng minh hiện đại thay đoạn bằng **δ-tube** mỏng và ước lượng hợp khi hướng thay đổi: chồng lấp cực đoan buộc cấu trúc đa thang. Davies (1971): chiều 2. Wang–Zahl (2025): chiều 3. $$n\ge 4$$ còn mở. Fields 2026 cho Wang.

---

## Mục tiêu học tập

- Định nghĩa tập Kakeya (Besicovitch).
- Tách measure zero và dimension $$n$$.
- Phát biểu giả thuyết và bảng trạng thái.
- Mô tả δ-tube ở mức khẩu hiệu.
- Gán công **Wang–Zahl**; liên kết Ch.2 và Ch.7.
- Không nhầm chuyển động kim với tập tĩnh.

**Liên kết seminar.** LO1. Cặp: Twin primes; Four Color; Exploration Kakeya.

---

## 1. Từ kim quay tới tập hướng

Kakeya (1917): miền nhỏ thế nào để đảo kim dài 1.

**Cải tiến trước “nghịch lý”.**  
- Giữ cố định tâm kim: quét đĩa bán kính $$1/2$$, diện tích $$\pi/4$$.  
- Vừa quay vừa trượt: **deltoid** đã giảm còn $$\pi/8$$.

![Đĩa vs deltoid]({{ site.baseurl }}/img/chapter_img/kakeya_deltoid_besicovitch_pmt.jpg)

*Hình. Hai cách quay kim: cố định tâm vs quay–trượt (deltoid $$\pi/8$$). Chân dung Besicovitch (nguồn: video Pham Manh Tuyen).*

**Abram Besicovitch** chứng minh có thể đưa diện tích về **tùy ý nhỏ / measure zero**. Hình dung xây dựng: **cây Perron** — chia tam giác, trượt chồng lấn các “quạt” hướng; giới hạn diện tích → 0 nhưng mọi hướng vẫn còn.

![Cây Perron cut-and-slide]({{ site.baseurl }}/img/chapter_img/kakeya_perron_tree_pmt.jpg)

*Hình. Bước chồng lấn kiểu Perron tree (nguồn video).*

**Tập Kakeya** hiện đại: chứa đoạn đơn vị **mọi** hướng (không bắt buộc là chuyển động liên tục của một kim).

![Hướng]({{ site.baseurl }}/img/chapter_img/kakeya_needle_directions.svg)

*Hình. Mọi hướng xuất hiện; tập chứa không nhất thiết đặc.*

![Sao các hướng Kakeya]({{ site.baseurl }}/img/chapter_img/kakeya_set_directions_pmt.jpg)

*Hình. Nhiều đoạn đơn vị theo hướng khác nhau trong một vùng (nguồn video).*

Phân biệt **chuyển động kim** vs **tập Besicovitch tĩnh**.

### Chuyển động liên tục: “squeegee” (Mathologer)

Câu chuyện trực quan (đoạn đơn vị = **squeegee** độ dày 0):

1. **Chuyển song song (warmup):** giữa hai vị trí song song, trượt dọc đường (diện tích 0) rồi quét với đỉnh rất xa — diện tích quét $$<\varepsilon$$ tùy ý (không thể = 0).  
2. **Vùng cổ điển cho quay 180°:** đĩa $$\pi/4\approx 0{,}785$$; tam giác đều chiều cao 1 $$\approx 0{,}577$$; **deltoid** còn nhỏ hơn.  
3. **Cây Perron:** cắt tam giác thành nhiều mảnh mỏng, chồng lấn → cây diện tích tùy ý nhỏ.  
4. **Magic transfer + ba cây:** khi kẹt trong cây, dùng chuyển song song giữa các cạnh gần song song; một cây ~$$60^\circ$$; **ba cây** = quay **180°** liên tục — hình **cá Kakeya**. Nhánh mịn hơn + hành lang chuyển dài hơn ⇒ diện tích quét $$<\varepsilon$$.  
5. **Giới hạn:** dãy cây → tập **measure zero** vẫn chứa đoạn đơn vị mọi hướng → đối tượng Besicovitch tĩnh; giả thuyết chiều hiện đại (Ch.2 Wang–Zahl, $$n=3$$).

![Chuyển song song]({{ site.baseurl }}/img/chapter_img/kakeya_squeegee_parallel_transfer_mathologer.jpg)

*Hình. Warmup chuyển song song: hai hình quạt nối vị trí xanh lá / xanh dương (Mathologer).*

![Đĩa, tam giác, deltoid]({{ site.baseurl }}/img/chapter_img/kakeya_disk_triangle_deltoid_mathologer.jpg)

*Hình. Vùng chuyển động liên tục: đĩa / tam giác / deltoid (Mathologer).*

![Cây Perron]({{ site.baseurl }}/img/chapter_img/kakeya_perron_tree_mathologer.jpg)

*Hình. Chồng lấn thành cây Perron (Mathologer).*

![Magic transfer]({{ site.baseurl }}/img/chapter_img/kakeya_magic_transfer_mathologer.jpg)

*Hình. Chuyển song song trên cây — [t≈10:32](https://www.youtube.com/watch?v=IM-n9c-ARHU&t=632s).*

![Cá Kakeya 180°]({{ site.baseurl }}/img/chapter_img/kakeya_fish_180_mathologer.jpg)

*Hình. Ba cây thành “cá Kakeya” cho 180° (Mathologer).*

---

## 2. Measure zero có thể; dimension đầy đủ vẫn có thể bị buộc

Besicovitch: measure zero trên mặt phẳng. **Điểm và đường** đều có diện tích 0 nhưng không “cùng cỡ”.

**Chiều Minkowski (đếm hộp):** $$N(\varepsilon)\asymp\varepsilon^{-d}$$ khi $$\varepsilon\to 0$$ (đoạn $$d=1$$, vuông $$d=2$$; fractal có thể không nguyên). **Chiều Hausdorff:** phủ bằng mảnh kích thước khác nhau, tinh tế hơn. Giả thuyết Kakeya đòi **chiều đầy đủ** của không gian nền.

![Minkowski vs Hausdorff]({{ site.baseurl }}/img/chapter_img/kakeya_minkowski_vs_hausdorff_pmt.jpg)

*Hình. Lưới đồng đều (Minkowski) vs mảnh phủ linh hoạt (Hausdorff) — nguồn video Pham Manh Tuyen.*

![Measure vs dimension]({{ site.baseurl }}/img/chapter_img/measure_vs_dimension.svg)

### Chiều Hausdorff cẩn thận hơn (hàm gauge)

Thang formal ngắn (tái dựng từ [CHALK — What is Hausdorff Dimension?](https://www.youtube.com/watch?v=LJcWhcM4okQ); deep-link [`&t=19s`](https://www.youtube.com/watch?v=LJcWhcM4okQ&t=19s)):

**1. Trực giác scale.** Phóng to $$\times 2$$: đoạn → $$2=2^1$$ bản sao (dim $$1$$); hình vuông đầy → $$4=2^2$$ (dim $$2$$); Sierpiński → $$3$$ bản sao ⇒ dim $$=\log_2 3$$.

![Scaling]({{ site.baseurl }}/img/chapter_img/hausdorff_scaling_intuition_chalk.jpg)

*Hình. Ví dụ scale trên bảng (CHALK).*

**2. Đo “sai”.** Vuông đo bằng **độ dài** ($$s=1$$): $$\infty$$; bằng **diện tích** ($$s=2$$): hữu hạn dương; bằng **thể tích** ($$s=3$$): $$0$$. Dimension = tham số tới hạn khi “độ đo” nhảy $$\infty\to 0$$.

![Đo sai trên vuông]({{ site.baseurl }}/img/chapter_img/hausdorff_wrong_measure_square_chalk.jpg)

*Hình. Length / area / volume trên một hình vuông (CHALK).*

**3. Hàm gauge.** $$\varphi\colon[0,\infty)\to[0,\infty)$$, $$\varphi(0)=0$$, không giảm, dương trên $$(0,\infty)$$, liên tục tại $$0$$. Độ dài ~ $$\varphi(t)=t$$; diện tích ~ $$t^2$$.

![Gauge]({{ site.baseurl }}/img/chapter_img/hausdorff_gauge_function_def_chalk.jpg)

*Hình. Định nghĩa gauge (CHALK).*

**4. Độ đo Hausdorff.** Phủ $$\delta$$: diam $$\le\delta$$. Đặt

$$
\mathcal{H}^\delta_\varphi(A)=\inf\Bigl\{\sum_i \varphi\bigl(\mathrm{diam}(C_i)\bigr): \{C_i\}\ \text{phủ }\delta\text{ của }A\Bigr\},
\quad
\mathcal{H}_\varphi(A)=\lim_{\delta\to 0}\mathcal{H}^\delta_\varphi(A).
$$

Với $$\varphi(t)=t^s$$ ta có độ đo Hausdorff $$s$$-chiều $$\mathcal{H}^s$$.

![Outer measure]({{ site.baseurl }}/img/chapter_img/hausdorff_outer_measure_def_chalk.jpg)

*Hình. $$\mathcal{H}^\delta_\varphi$$ (CHALK).*

**5. $$s$$ tới hạn = dimension.**

$$
\dim_H(A)=\inf\{s\ge 0:\ \mathcal{H}^s(A)=0\}=\sup\{s\ge 0:\ \mathcal{H}^s(A)=\infty\}.
$$

![Critical s]({{ site.baseurl }}/img/chapter_img/hausdorff_dimension_critical_s_chalk.jpg)

*Hình. Nhảy $$\infty\to 0$$ tại $$s=\dim_H$$ (CHALK).*

**Liên kết Kakeya.** Tập Besicovitch có thể measure 0 nhưng $$\dim_H$$ lớn; giả thuyết đòi $$\dim_H=\dim_M=n$$. Davies (1971): mọi tập Kakeya phẳng có $$\dim_H=2$$ dù measure 0.

### Ước lượng $$\dim_H$$: chặn trên và Mass Distribution Principle

Tính trực tiếp $$\mathcal{H}^s$$ khó; thực tế **ước lượng**. Video kèm: [CHALK — Estimating Hausdorff Dimension](https://www.youtube.com/watch?v=FQXbRGmAbUY) (~9,4 phút).

**Chặn trên (đếm phủ).** Nếu $$A$$ phủ được bằng $$N_k$$ tập diam $$\le\delta_k$$, $$\delta_k\to 0$$, thì

$$
\dim_H(A)\ \le\ \liminf_{k\to\infty}\frac{\log N_k}{-\log \delta_k}.
$$

Phác thảo: $$\mathcal{H}^{\delta_k}_s(A)\le N_k\delta_k^s$$; nếu $$s$$ lớn hơn liminf thì $$N_k\delta_k^s\to 0$$ ⇒ $$\mathcal{H}^s=0$$.

![Chặn trên]({{ site.baseurl }}/img/chapter_img/hausdorff_upper_bound_cover_chalk.jpg)

*Hình. Chặn trên bằng số mảnh phủ (CHALK).*

**Chặn dưới (Mass Distribution Principle).** $$\mu$$ trên $$A$$, $$0<\mu(A)<\infty$$, và $$\mu(U)\le C(\mathrm{diam}\,U)^s$$ cho mọi $$U$$ đủ nhỏ. Khi đó $$\mathcal{H}^s(A)\ge\mu(A)/C>0$$ ⇒ $$\dim_H(A)\ge s$$.

![MDP phát biểu]({{ site.baseurl }}/img/chapter_img/hausdorff_mdp_statement_chalk.jpg)

*Hình. Giả thiết MDP (CHALK).*

![MDP chứng minh]({{ site.baseurl }}/img/chapter_img/hausdorff_mdp_proof_chalk.jpg)

*Hình. Kết luận MDP (CHALK).*

**Trong lý thuyết Kakeya.** Chặn trên $$\dim\le n$$ dễ (không gian nền). Việc khó là **chặn dưới** (Wolff, Bourgain, sticky, Wang–Zahl dim $$=3$$). MDP / Frostman là công cụ chuẩn.

---

## 3. Giả thuyết

**Giả thuyết.** Mọi tập Kakeya trong $$\mathbb{R}^n$$ có $$\dim_H=\dim_M=n$$.

| $$n$$ | Trạng thái |
|-------|------------|
| 1 | Tầm thường |
| 2 | Davies 1971 |
| 3 | **Wang–Zahl 2025** |
| $$\ge 4$$ | Mở |

Nguồn: [arXiv:2502.17655](https://arxiv.org/abs/2502.17655). Không khẳng định thể tích dương.

![Wang–Zahl 2025]({{ site.baseurl }}/img/chapter_img/kakeya_wang_zahl_2025_pmt.jpg)

*Hình. Thẻ video: $$\dim_H=\dim_M=3$$ trong $$\mathbb{R}^3$$ (nguồn video; nguồn sơ cấp là arXiv).*

---

## 4. Vì sao 3D khó: δ-tube

![δ-tube]({{ site.baseurl }}/img/chapter_img/kakeya_delta_tubes.svg)

Sticky Kakeya (JAMS 2026) là bước đệm quan trọng.

---

## 5. Vì sao harmonic analysis quan tâm

Restriction, local smoothing, Falconer, Furstenberg—trích dẫn IMU Fields 2026 của Wang.

![Tới HA]({{ site.baseurl }}/img/chapter_img/kakeya_to_harmonic_analysis.svg)

### “Tháp” các giả thuyết (bản đồ phổ thông)

Video [Quanta Magazine](https://www.youtube.com/watch?v=5J3tYU_-IZI) (phỏng vấn Tao, Hickman, Wang, Zahl) đặt Kakeya làm **đáy tháp**:

1. **Giả thuyết Kakeya** (hình học hướng / tube).  
2. **Fourier restriction** — Fourier trên mặt cong.  
3. **Bochner–Riesz** — “làm mịn” biên tín hiệu.  
4. **Local smoothing** — lan truyền sóng (PDE).

Nếu Kakeya sai, nhiều tầng trên sụp; nếu đúng, phương pháp có thể **leo tháp**. Kết quả Wang–Zahl 3D được gọi là đột phá HA thế hệ (≈ 20 năm).

**Bản lề lịch sử (Fefferman):** Charles Fefferman (thập niên 1970) nối hình học Kakeya với Fourier — Kakeya không còn chỉ là “trò kim”.

![Restriction]({{ site.baseurl }}/img/chapter_img/kakeya_tower_restriction_quanta.jpg)

*Hình. Tầng restriction (Quanta).*

![Bochner–Riesz]({{ site.baseurl }}/img/chapter_img/kakeya_tower_bochner_riesz_quanta.jpg)

*Hình. Tầng Bochner–Riesz (Quanta).*

![Local smoothing]({{ site.baseurl }}/img/chapter_img/kakeya_tower_local_smoothing_quanta.jpg)

*Hình. Local smoothing / sóng (Quanta).*

### Ý tưởng chứng minh 2025 (mức khẩu hiệu)

- Tube 3D “miss” nhiều hơn rectangle 2D.  
- **Sticky Kakeya** (2022) là bước đệm.  
- **Graininess** (Guth…): nén cực đoan sinh “grain”.  
- **Induction on scales** nâng chặn dưới dim dần đến 3 (kiểm soát “mất mát” kiểu Chinese whispers).  
- $$n\ge 4$$ vẫn mở.

![Grains]({{ site.baseurl }}/img/chapter_img/kakeya_grains_induction_quanta.jpg)

*Hình. Cấu trúc grain / đa thang (Quanta).*

---

## 6. Bản đồ khóa học

| Vị trí | Vai trò |
|--------|---------|
| Ch.1 (trang này) | Bản đồ bài toán |
| Ch.2 Wang | Bài giảng đầy đủ |
| Ch.7 Exploration | Thử nghiệm “nhỏ thế nào?” |

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| Phải có thể tích dương | Sai — dimension mới là giả thuyết |
| Wang một mình | Sai — Zahl đồng tác giả |
| Xong mọi chiều | Sai — $$n\ge 4$$ mở |

---

## Bài tập

1. Định nghĩa tập Kakeya một câu.  
2. Davies tương thích Besicovitch thế nào?  
3. Vì sao dùng tube thay đoạn?  
4. Viết bảng trạng thái từ trí nhớ.  
5. Lấy khẩu hiệu self-improvement từ bài Wang Ch.2.  
6. Đọc abstract arXiv:2502.17655.  
7. Thử Ch.7 exploration 30 phút.

---

## Video phổ thông (nguồn)

Dùng cho **trực giác**; định lý chuẩn ở Ch.2 Wang + arXiv.

### ★ Câu chuyện 2025 (tiếng Anh — Quanta) — nên xem trước

- **Nguồn:** [A Once-in-a-Century Proof: The Kakeya Conjecture — Quanta](https://www.youtube.com/watch?v=5J3tYU_-IZI) (~15 phút; 2026-08-03).  
  Kim → Besicovitch → Davies → Fefferman/Fourier → tháp restriction / Bochner–Riesz / local smoothing → sticky + grains → Wang–Zahl 3D.  
  Bài viết: [Quanta 2025-03-14](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/).  
  *Lưu ý:* một số đồ họa Hausdorff trên video có errata; định nghĩa formal dùng CHALK.

### A. Hausdorff formal (tiếng Anh — CHALK, phần 1)

- **Nguồn:** [What is Hausdorff Dimension? — CHALK](https://www.youtube.com/watch?v=LJcWhcM4okQ) (~13,3 phút; 2026-08-03).  
  Scale → đo sai → gauge → $$\mathcal{H}^\delta_\varphi$$ → $$\mathcal{H}^s$$ → $$s=\dim_H$$.  
  Deep-link **[t≈0:19](https://www.youtube.com/watch?v=LJcWhcM4okQ&t=19s)**. Khớp mục “Chiều Hausdorff cẩn thận hơn”.

### A′. Ước lượng Hausdorff (tiếng Anh — CHALK, phần 2)

- **Nguồn:** [Methods for Estimating Hausdorff Dimension / MDP — CHALK](https://www.youtube.com/watch?v=FQXbRGmAbUY) (~9,4 phút; 2026-08-03).  
  Chặn trên bằng $$N_k,\delta_k$$; **Mass Distribution Principle** cho chặn dưới. Khớp mục “Ước lượng $$\dim_H$$”.

### B. Xây dựng chuyển động liên tục (tiếng Anh — Mathologer)

- **Nguồn:** [The Kakeya needle problem (squeegee) — Mathologer](https://www.youtube.com/watch?v=IM-n9c-ARHU) (~16,8 phút; 2026-08-03).  
  Tốt nhất cho **kim quay liên tục**: chuyển song song → đĩa/tam giác/deltoid → cây Perron → cá ba cây → giới hạn measure zero.  
  Deep-link **[t≈10:32](https://www.youtube.com/watch?v=IM-n9c-ARHU&t=632s)** — magic transfer trên cây.  
  Mô tả video trỏ survey của Terry Tao (đầu sâu GMT / harmonic analysis).

### C. Giải thích hình học tiếng Việt (Minkowski/Hausdorff)

- **Nguồn:** [Giả Thuyết Kakeya… | Pham Manh Tuyen](https://www.youtube.com/watch?v=XUkfpgFakMQ) (~15 phút; 2026-08-03).  
  Mốc: Fields 2026; đĩa/deltoid; Perron; định nghĩa tập; đếm hộp → Hausdorff; Davies + 3D; Wang–Zahl + $$n\ge 4$$ mở.

### D. Video ngắn (lịch sử chặn dưới, VI)

- **Nguồn:** [Phỏng Đoán Kakeya… | TOÁN PRO](https://www.youtube.com/watch?v=pxVMKoZsVc8) (~8,7 phút; 2026-08-03).  
  Bắt đầu **t=3:38** (`&t=218s`) — Besicovitch; rồi Wolff/Bourgain → sticky → 2025.

![Diện tích tiến về 0]({{ site.baseurl }}/img/chapter_img/kakeya_area_to_zero_toanpro.jpg)

*Hình. $$A\to 0$$ vẫn giữ mọi hướng (TOÁN PRO).*

![Besicovitch giải diện tích 2D]({{ site.baseurl }}/img/chapter_img/kakeya_besicovitch_solved_toanpro.jpg)

*Hình. Checkpoint Besicovitch (TOÁN PRO, ~t=3:38).*

![Bourgain và cuộc đua chặn dưới]({{ site.baseurl }}/img/chapter_img/kakeya_bourgain_toanpro.jpg)

*Hình. Thẻ Bourgain (TOÁN PRO).*

**Lưu ý (cả hai video).** Phụ đề tự động hay sai tên/năm (Kakja, 1977 thay 1917, Hous Dof, Minsky, Josu, Furier…). Dùng tên chuẩn: **Kakeya (1917)**, **Besicovitch**, **Hausdorff**, **Minkowski**, **Davies**, **Wolff**, **Bourgain**, **Joshua Zahl**, **Hong Wang**, **Fourier**.

---

## Nguồn video (gói math-video-researcher)

Phần video phổ thông ở trên đã xếp hạng định hướng. Gói chuẩn (mọi URL, bảng trạng thái Mode B, lộ trình học): `research/video-research/Kakeya_Conjecture/`.

**Nhắc trạng thái (2026):** giả thuyết *tập* Kakeya 3D **đã chứng minh** (Wang–Zahl 2025); chiều $$n\ge 4$$ và dạng maximal function mạnh hơn phần lớn **mở**. Video cho trực giác và văn hóa—không thay Ch.2 / arXiv.

---



### Transcript & frames (extract flagship)

Transcript caption và unit theo thời gian: `research/video-research/Kakeya_Conjecture/transcripts/` · trạng thái: `research/video-research/Kakeya_Conjecture/TRANSCRIPT_STATUS.md` · danh sách master: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Caption tải tự động (yt-dlp)—dùng để điều hướng, **không** thay nội dung bài.


![Frame mẫu video flagship]({{ site.baseurl }}/img/video_research/flagships/kakeya_quanta_frame01.jpg)

*Hình. Frame mẫu từ video flagship chính (xem pack cho timestamp).*

## Tài liệu tham khảo

Thư mục URL: `research/video-research/Kakeya_Conjecture/references.md`.

### Bài báo và blog

1. Wang–Zahl — [arXiv:2502.17655](https://arxiv.org/abs/2502.17655); sticky [arXiv:2210.09581](https://arxiv.org/abs/2210.09581).  
2. Tao — [blog 3D Kakeya](https://terrytao.wordpress.com/2025/02/25/the-three-dimensional-kakeya-conjecture-after-wang-and-zahl/); [ghi chú stickiness 2014](https://terrytao.wordpress.com/2014/05/07/stickiness-graininess-planiness-and-a-sum-product-approach-to-the-kakeya-problem/).  
3. Davies 1971; IMU Fields 2026 Wang.  

### Video và tin

4. Quanta video: https://www.youtube.com/watch?v=5J3tYU_-IZI · [bài](https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/)  
5. Mathologer: https://www.youtube.com/watch?v=IM-n9c-ARHU  
6. CHALK Hausdorff: https://www.youtube.com/watch?v=LJcWhcM4okQ · MDP: https://www.youtube.com/watch?v=FQXbRGmAbUY  
7. VI: https://www.youtube.com/watch?v=XUkfpgFakMQ · https://www.youtube.com/watch?v=pxVMKoZsVc8  
8. IAS Ideas: https://www.ias.edu/ideas/three-dimensional-breakthrough  
9. Wikipedia — [Kakeya set](https://en.wikipedia.org/wiki/Kakeya_set)  

### Khóa học

10. [Wang Ch.2]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/); [Explore Kakeya]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/). Gói: `research/video-research/Kakeya_Conjecture/`.

---

## Hướng đi tiếp

**Tiếp lộ trình A**

1. Xong: bản đồ Ch.1 (trang này).  
2. **Tiếp →** [Wang Ch.2]({{ site.baseurl }}/contents/vi/chapter02/02_15_Wang_Harmonic_Analysis/).  
3. **Rồi →** [Studio Kakeya Ch.7]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/).  

Tùy chọn: [CHALK Hausdorff](https://www.youtube.com/watch?v=LJcWhcM4okQ&t=19s) + [CHALK MDP](https://www.youtube.com/watch?v=FQXbRGmAbUY); [Mathologer squeegee](https://www.youtube.com/watch?v=IM-n9c-ARHU&t=632s); [Pham Manh Tuyen](https://www.youtube.com/watch?v=XUkfpgFakMQ) hoặc [TOÁN PRO](https://www.youtube.com/watch?v=pxVMKoZsVc8).  
- So văn hóa với [lộ trình Bốn màu B]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/).
