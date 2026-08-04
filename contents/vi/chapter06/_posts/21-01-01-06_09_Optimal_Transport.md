---
layout: post
title: "Vận chuyển Tối ưu"
chapter: '06'
order: 9
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Làm sao chuyển một đống cát thành hình đống khác với chi phí tối thiểu? Câu hỏi mang tiếng cổ đó là gốc **vận chuyển tối ưu (OT)**—nay là ngôn ngữ trung tâm để so phân phối xác suất, biến dạng hình, và xây mô hình sinh. Từ Monge (1781) qua thư giãn tuyến tính Kantorovich đến regularization entropy và hình học tính toán, OT nằm giao điểm giải tích, xác suất, tối ưu và khoa học dữ liệu.

Bài phát triển công thức Monge và Kantorovich, khoảng cách Wasserstein, dual cơ bản, ý tính toán (Sinkhorn), và ứng dụng—gắn nhãn định lý, heuristic số, và hype “Wasserstein GAN giải generative modeling”.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu bài Monge: map $$T$$ đẩy $$\mu$$ thành $$\nu$$ tối thiểu chi phí; vì sao map có thể không tồn tại.
- Viết công thức **Kantorovich** trên coupling $$\pi$$ cố định biên.
- Định nghĩa khoảng cách **Wasserstein** $$W_p$$ và diễn giải $$W_1$$ nhạy hình học.
- Nêu dual Kantorovich–Rubinstein cho $$W_1$$ (Lipschitz).
- Mô tả regularization entropy → Sinkhorn: được/mất gì so với OT exact.
- Phê claim ML dùng “Wasserstein” như buzzword không nêu cost/ước lượng (**LO6**).

**Kiến thức nền.** Phân phối như độ đo (tích phân hàm test); tối ưu cơ bản; khoảng cách Euclid. Giải tích lồi giúp nhưng không đòi đủ.

---

## 1. Bài Monge

Cho $$\mu,\nu$$ trên không gian $$X$$ (nghĩ $$\mathbb{R}^d$$) và cost $$c(x,y)$$, tìm map $$T$$ với $$T_\#\mu=\nu$$ tối thiểu

$$
\int c\bigl(x,T(x)\bigr)\,d\mu(x).
$$

Mỗi “hạt” ở $$x$$ đi một chỗ $$T(x)$$. Map có thể không tồn tại (tách khối lượng từ một nguyên tử ra hai). Kể cả khi tồn tại, đặc trưng hóa không tầm thường. Với $$c=\|x-y\|^2$$ trên $$\mathbb{R}^d$$, dưới điều kiện chính quy, định lý Brenier liên hệ map tối ưu với gradient thế lồi: $$T=\nabla\phi$$.

---

## 2. Thư giãn Kantorovich: coupling

Cho phép **tách khối lượng** qua joint $$\pi$$ trên $$X\times X$$ biên $$\mu,\nu$$:

$$
\inf_{\pi\in\Pi(\mu,\nu)}\int c(x,y)\,d\pi(x,y),
$$

với $$\Pi(\mu,\nu)$$ tập coupling. Đây là LP vô hạn chiều. Kế hoạch tối ưu $$\pi$$; khi $$\pi$$ tập trung trên đồ thị map thì về Monge.

Form này mở dual lồi và lý thuyết tồn tại trưởng thành—điểm xuất phát mặc định của OT hiện đại.

---

## 3. Khoảng cách Wasserstein

Với $$p\ge 1$$ và moment $$p$$ hữu hạn:

$$
W_p(\mu,\nu)=\Bigl(\inf_{\pi\in\Pi(\mu,\nu)}\int\|x-y\|^p\,d\pi\Bigr)^{1/p}
$$

(trên $$\mathbb{R}^d$$ với cost Euclid; metric space khác dùng $$d(x,y)^p$$). $$W_p$$ metrize hội tụ yếu + moment (điều kiện phù hợp)—trung thành hình học hơn TV/KL khi support lệch. Dịch bump nhỏ qua không gian tốn cỡ khoảng cách trong $$W_1$$; KL có thể vô hạn nếu support không khớp.

**Hình học không gian độ đo.** Không gian độ đo moment hai hữu hạn với $$W_2$$ giàu cấu trúc (Otto calculus, geodesic convexity của một số phiếm hàm)—biên giới giải tích–PDE (heat flow như gradient flow entropy trong không gian Wasserstein).

---

## 4. Dual (mặt hữu dụng)

Với $$c=\|x-y\|$$, Kantorovich–Rubinstein:

$$
W_1(\mu,\nu)=\sup_{\|f\|_{\mathrm{Lip}}\le 1}\Bigl(\int f\,d\mu-\int f\,d\nu\Bigr).
$$

$$W_1$$ là dual của hàm Lipschitz hằng ≤ 1. Dual nuôi chặn thống kê, diễn giải tối ưu robust, và một số công thức generative (critic Lipschitz—**trên lý thuyết**; thực hành xấp xỉ ràng buộc).

Cost tổng quát hơn có thế $$c$$-concave và cấu trúc complementary slackness ($$c$$-cyclical monotonicity của support plan tối ưu).

---

## 5. Tính toán: LP → Sinkhorn

Độ đo rời rạc $$n$$ điểm: OT exact là LP $$n^2$$ biến—giải được nhưng đắt khi $$n$$ lớn. **Regularization entropy** thêm $$\varepsilon\mathrm{KL}(\pi\|\mu\otimes\nu)$$ (hoặc tương tự) → bài lồi chặt giải bằng **Sinkhorn–Knopp** scale ma trận. $$\varepsilon\to 0$$ tiến OT; $$\varepsilon>0$$ làm mờ plan và đổi phân kỳ (Sinkhorn divergence cần debias trong một số dùng thống kê).

Đường khác: auction, network simplex, multiscale, sliced Wasserstein (chiếu 1D rồi trung bình), công thức động Benamou–Brenier kiểu cơ học chất lỏng PDE.

**Biết đọc.** “Dùng Wasserstein” có thể nghĩa OT exact, entropic, sliced, mini-batch bias, hoặc dual penalty lỏng—**không hoán đổi** thống kê.

---

## 6. Ứng dụng

| Lĩnh vực | Vai trò OT |
|----------|------------|
| Thống kê | Metric phân phối; ước lượng robust |
| Thị giác / đồ họa | Chuyển màu, nội suy hình, đăng ký |
| Kinh tế | Matching, assignment (gốc lịch sử) |
| ML sinh | Khớp phân phối; heuristic dual WGAN; mô hình quỹ đạo |
| Sinh học | So phân bố biểu hiện; suy diễn quỹ đạo (cẩn thận) |
| PDE / vật lý | Gradient flow; phương trình aggregation–diffusion |

**Hype.** WGAN phổ biến hóa dual Lipschitz; ổn định huấn luyện là thực nghiệm, phụ thuộc kiến trúc—không hệ quả thuần Kantorovich–Rubinstein. Ước lượng mini-batch cao chiều có thể bias nặng.

---

## 7. Cao chiều và sample complexity

Ước lượng $$W_p$$ liên tục cao chiều từ mẫu có thể cần kích thước mẫu mũ theo chiều ở một số chế độ—một mặt curse. Cấu trúc (chiều nội tại, trơn) và phân kỳ khác đổi tốc độ. Đây là thống kê toán đang hoạt động—không lý do bỏ OT, nhưng lý do tránh claim ngây thơ.

---

## 8. Tiên phong

1. Tốc độ thống kê OT và Sinkhorn debiased.  
2. OT trên đồ thị, mạng, không gian non-Euclid.  
3. Multi-marginal và barycenter Wasserstein.  
4. Transport không cân bằng / nhân quả (tạo/hủy khối lượng).  
5. Gradient flow trên metric measure space và liên kết sampling.  
6. OT có cấu trúc quy mô lớn cho mô hình sinh với đánh giá trung thực.

### Ví dụ rời rạc $$2\times 2$$

Khối lượng $$a=(0.5,0.5)$$ tại $$x_1,x_2$$ và $$b=(0.5,0.5)$$ tại $$y_1,y_2$$: coupling là ma trận $$2\times 2$$ không âm đúng tổng hàng/cột. Cost $$\sum\pi_{ij}c_{ij}$$. Nếu $$c_{11},c_{22}$$ rẻ còn chéo đắt, plan tối ưu thích đường chéo; hình học đảo thì plan đảo. LP tìm tối ưu; instance nhỏ liệt kê polytope một chiều của coupling.

Entropic OT làm mượt mục tiêu (thường duy nhất); Sinkhorn scale hàng/cột. Nhìn $$3\times 3$$ hội tụ đáng hơn ngàn slide.

### Vì sao hình học độ đo quan trọng cho học

Mô hình sinh: làm pushforward $$G_\#\eta$$ gần độ đo dữ liệu $$\mu$$. Phân kỳ khác = hình học khác (mode-seeking vs mass-covering), độ nhạy outlier, sample complexity. Wasserstein tính phí chuyển khối lượng qua không gian—khớp “phân phối gần” hơn KL khi support lệch, **khi** metric nền có nghĩa và estimator không bị bias phá.

### Studio seminar

Tìm một paper ML viết “Wasserstein”. Checklist LO6: cost $$c$$ nào? rời rạc hay liên tục? solver exact / Sinkhorn / sliced / mini-batch? Có debias? Viết một đoạn: claim hình học nào *thật sự* được bảo vệ bởi công thức, claim nào chỉ marketing.

---

## Nhầm lẫn thường gặp

| Tuyên bố | Sửa |
|----------|-----|
| “Wasserstein = EMD.” | Gần đúng với $$W_1$$ rời rạc; họ $$W_p$$ rộng hơn. |
| “OT luôn cho map $$T$$.” | Plan có thể tách khối lượng. |
| “Sinkhorn = OT exact.” | Regularization làm lệch mục tiêu. |
| “WGAN huấn luyện đúng $$W_1$$.” | Ràng buộc Lipschitz xấp xỉ. |
| “KL và $$W_p$$ cùng mismatch.” | Topology và độ nhạy khác. |
| “OT tự giải domain adaptation.” | Toolkit hữu ích; thành công thực nghiệm, giả thiết-phụ thuộc. |

---

## Bài tập

1. Tính $$W_p(\delta_a,\delta_b)$$.
2. Vì sao $$\delta_0\to\frac12\delta_{-1}+\frac12\delta_1$$ không có map cổ điển không tách.
3. Viết $$\Pi(\mu,\nu)$$ cho hai độ đo hai điểm.
4. Dual: vì sao $$W_1$$ lớn nếu kỳ vọng lệch trên $$\mathbb{R}$$?
5. Một lợi tính toán và một giá thống kê/toán của entropic OT.
6. Tìm paper “Wasserstein”: cost, rời rạc/liên tục, solver exact/xấp xỉ.
7. Đọc phát biểu Brenier; cost nào?

---


---

## Kiến thức trích từ nghiên cứu video

Tóm tắt cho seminar (đối chiếu nguồn viết; **không bịa transcript**). Gói: `research/video-research/optimal-transport/analysis.md`.

### Trạng thái

**Mature theory, booming applications.** Monge–Kantorovich theory classical; Sinkhorn/entropic OT and gradient flows are modern computational engines.

### Phát biểu / slogan cốt lõi

Kantorovich problem: $$\inf_{\pi\in\Pi(\mu,\nu)}\int c\\,d\pi$$. Wasserstein-$$p$$ metrizes weak convergence (on suitable spaces). Brenier: under conditions, optimal maps are gradients of convex potentials.

### Định nghĩa cần cố định

- **Coupling.** Joint $$\pi$$ with marginals $$\mu,\nu$$.
- **Sinkhorn.** Entropic regularization of OT solved by matrix scaling.

### Vệ sinh khái niệm

- Thinking OT always yields a deterministic Monge map in discrete equal-mass unbalanced settings without hypotheses.
- Ignoring sample complexity blow-up of empirical W_p in high dimension.


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh/bài báo gốc khi tuyên bố mang tính then chốt. Chi tiết xếp hạng: `research/video-research/optimal-transport/`.

**Thứ tự gợi ý**

1. **Cốt lõi** — Villani — Optimal Transport Theory (Imperial College): [https://www.youtube.com/watch?v=6DZjBcDfPHs](https://www.youtube.com/watch?v=6DZjBcDfPHs).  
2. **Nền tảng** — Fields Institute — Optimal Transportation Lecture 01: [https://www.youtube.com/watch?v=TAnoqeYfO1Y](https://www.youtube.com/watch?v=TAnoqeYfO1Y).  
3. **Định hướng** — Simons — Crash Course on Optimal Transport: [https://www.youtube.com/watch?v=GMC7uOPAa_Y](https://www.youtube.com/watch?v=GMC7uOPAa_Y).  
4. **Tính toán** — UniHeidelberg — Sinkhorn iterations (discrete OT): [https://www.youtube.com/watch?v=BfOjrQAhG4M](https://www.youtube.com/watch?v=BfOjrQAhG4M).  

**Nhắc trạng thái:** **Mature theory, booming applications.** Monge–Kantorovich theory classical; Sinkhorn/entropic OT and gradient flows are modern computational engines.

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/optimal-transport/transcripts/` · trạng thái: `research/video-research/optimal-transport/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/optimal-transport_6DZjBcDfPHs_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu tham khảo

1. Villani — Topics / Old and New.
2. Peyré & Cuturi — *Computational Optimal Transport*.
3. Santambrogio — OT for applied mathematicians.
4. Nền: Monge; Kantorovich; Brenier.
5. [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

---


Danh mục URL đầy đủ: `research/video-research/optimal-transport/references.md`.

### Video (lộ trình gợi ý)

- Villani — Optimal Transport Theory (Imperial College) (CORE): https://www.youtube.com/watch?v=6DZjBcDfPHs
- Fields Institute — Optimal Transportation Lecture 01 (FOUNDATION): https://www.youtube.com/watch?v=TAnoqeYfO1Y
- Simons — Crash Course on Optimal Transport (ORIENTATION): https://www.youtube.com/watch?v=GMC7uOPAa_Y
- UniHeidelberg — Sinkhorn iterations (discrete OT) (COMPUTATION): https://www.youtube.com/watch?v=BfOjrQAhG4M

### Bài báo và web (từ gói nghiên cứu)

- Wikipedia — Transportation theory (mathematics): https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)
- Wikipedia — Wasserstein metric: https://en.wikipedia.org/wiki/Wasserstein_metric
- Peyré & Cuturi — Computational OT (arXiv survey): https://arxiv.org/abs/1803.00567
- Carmin.tv OT intro lectures: https://www.carmin.tv/en/video/introduction-to-optimal-transport-theory-lecture-2
- Wikipedia — Earth mover's distance: https://en.wikipedia.org/wiki/Earth_mover%27s_distance

### Khóa học

- Gói: `research/video-research/optimal-transport/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/); [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).
- [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) cho học phân phối.
- Thực hành: OT rời rạc $$2\times 2$$ hoặc $$3\times 3$$ bằng tay; rồi Sinkhorn cùng cost.
- Đọc: Peyré–Cuturi tính toán → intuition Villani → abstract một paper tốc độ thống kê.
- Luôn ghi: *cost, biên, exact vs regularized, estimator*.
