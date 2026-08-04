---
layout: post
title: "Tối ưu → Vận hành & AI"
chapter: '03'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
lesson_type: required
---

Hãng bay xếp lịch phi hành đoàn. Bệnh viện gán giường. Trung tâm dữ liệu đặt workload. Mạng nơ-ron chỉnh hàng triệu trọng số. Dưới trang phục khác nhau, cùng một câu hỏi: **chọn biến quyết định để mục tiêu nhỏ (hoặc lớn) nhất, dưới ràng buộc.**

**Lộ trình:** phát biểu bài toán → lồi → gradient & phương pháp bậc nhất → ràng buộc & Lagrange/KKT → LP/IP → dual → cảnh quan không lồi của ML → nhầm lẫn.

Bài này là bản đồ cơ chế từ tối ưu toán học tới vận trù học và huấn luyện AI—không phải cả khóa thuật toán, nhưng đủ để hiểu solver và SGD.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Viết $$\min_{x\in\mathcal{X}} f(x)$$ và nhận diện mục tiêu, biến, ràng buộc trong bài lời văn.
- Giải thích vì sao **lồi** khiến cực tiểu địa phương là toàn cục.
- Mô tả gradient descent và vai trò bước nhảy; nối với huấn luyện ML.
- Nêu LP và IP mô hình gì trong vận hành.
- Giải thích **duality** mức khẩu hiệu (giá bóng / chứng nhận tối ưu).
- Tránh “gradient descent luôn tìm min toàn cục” và “lồi = luôn dễ trong thực tế.”

**Kiến thức nền.** Gradient. Hữu ích: [đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/), [xác suất/rủi ro]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/).

---

## 1. Khuôn mẫu phổ quát

$$
\min_x f(x)\quad\text{s.t.}\quad x\in\mathcal{X}.
$$

$$f$$ là **mục tiêu**; $$\mathcal{X}$$ mã hóa **ràng buộc**. Kỹ năng mô hình hóa là nửa lĩnh vực: dịch “xếp lịch y tá theo luật lao động” thành biến và bất đẳng thức.

**Khẩu hiệu.** *Công nghệ “tối ưu” khi phát biểu quyết định như mục tiêu dưới ràng buộc và áp thuật toán có bảo đảm hoặc thực nghiệm mạnh.*

---

## 2. Tính lồi: cảnh quan đáng tin

Tập lồi: đoạn nối hai điểm nằm trong tập. Hàm lồi:

$$
f(tx+(1-t)y)\le tf(x)+(1-t)f(y).
$$

Với $$f$$ khả vi: $$f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle$$. Mọi cực tiểu địa phương trên tập lồi là toàn cục. LP, bình phương tối thiểu, nhiều SVM, barrier log sống ở đây. Gradient Lipschitz khống chế cỡ bước.

---

## 3. Gradient và phương pháp bậc nhất

$$
x_{k+1}=x_k-\eta_k\nabla f(x_k).
$$

Hướng âm gradient là hướng giảm dốc nhất cục bộ; cỡ bước $$\eta_k$$ quá lớn thì nhảy qua thung lũng, quá nhỏ thì chậm. Momentum, Nesterov, Adam sửa cập nhật bằng lịch sử gradient—vẫn họ bậc nhất, nhưng “bộ nhớ” làm quỹ đạo mượt hoặc thích nghi theo tọa độ.

**SGD:** khi $$f=\frac1n\sum_i f_i$$, ước lượng gradient bằng một hạng hoặc mini-batch—bắt buộc ở quy mô web; nhiễu có thể giúp thoát vùng xấu sắc và, theo một số quan điểm, đóng vai trò chính quy ẩn.

**Cơ chế AI.**  
*Huấn luyện mạng là tối ưu phi tuyến quy mô lớn của rủi ro thực nghiệm; backprop cung gradient; họ SGD cập nhật tham số.*

Liên hệ [xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/): loss trên tập train là rủi ro thực nghiệm; cái ta thực sự muốn nhỏ là rủi ro kỳ vọng—tối ưu chỉ là nửa câu chuyện.

---

## 4. Ràng buộc: chiếu, barrier, Lagrange

Ràng buộc cứng $$x\in\mathcal{X}$$ được xử lý bằng:

- **Chiếu:** bước gradient rồi chiếu lên $$\mathcal{X}$$ (projected gradient).  
- **Penalty / augmented Lagrangian:** làm mềm ràng buộc thành phần mục tiêu.  
- **Interior-point / barrier:** ở trong miền khả thi nghiêm ngặt trong khi đẩy tham số barrier về 0 (động cơ LP/QP hiện đại).  
- **Active-set:** đoán bất đẳng thức nào đang “chặt.”

Với ràng buộc đẳng thức $$g(x)=0$$, **nhân tử Lagrange** $$\lambda$$ tạo Lagrangian $$L(x,\lambda)=f(x)+\langle\lambda,g(x)\rangle$$. Tính dừng $$\nabla_x L=0$$ cộng khả thi là điều kiện cần dưới chính quy. Bất đẳng thức mang điều kiện **KKT**: dừng, khả thi primal/dual, bù lỏng.

Bạn không cần thuộc từng dòng KKT để dùng CVXPY—nhưng “multiplier như **giá bóng**” là trực giác vận hành: nới ràng buộc tài nguyên một đơn vị thì giá trị tối ưu cải thiện bao nhiêu?

---

## 5. Quy hoạch tuyến tính: ngựa thồ OR

$$
\min_x\, c^\top x \quad\text{s.t.}\quad Ax\le b,\quad x\ge 0
$$

(hoặc dạng đẳng thức). Miền khả thi là đa diện; tối ưu tại đỉnh (nếu tồn tại). **Simplex** đi đỉnh; **interior-point** cắt qua nội miền với lý thuyết worst-case đa thức (và thực hành xuất sắc).

**Ứng dụng.** Pha trộn, vận tải, luồng mạng như LP, kế hoạch sản xuất, thư giãn của bài khó hơn. Lịch bay và chuỗi cung ứng dùng chồng LP/MIP hằng ngày.

**Luồng mạng** từ [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/) là LP đặc biệt với cấu trúc totally unimodular—nghiệm nguyên không cần ép nguyên tường minh. Đó là ví dụ kinh điển: *cấu trúc* biến bài rời rạc thành LP “tự nhiên nguyên.”

---

## 6. Quy hoạch nguyên: quyết định rời rạc

Khi biến phải nguyên (hoặc binary), ta có **IP/MIP**:

$$
\min c^\top x \quad\text{s.t.}\quad Ax\le b,\quad x\in\mathbb{Z}^n.
$$

Mô hình quyết định có/không: mở kho hay không; gán kíp hay không. IP tổng quát NP-khó; thực tiễn dùng branch-and-bound, cutting plane, heuristic, phát biểu chặt. **Thư giãn LP** (bỏ nguyên) cho chặn và dẫn đường tìm kiếm.

**Cơ chế.** *OR thành công nhờ mô hình cấu trúc rời rạc đủ chặt để solver MIP công nghiệp khép gap; worst-case cứng không cấm thắng trên instance có cấu trúc.*

Nghệ thuật mô hình hóa—biến phụ, bất đẳng thức cắt, linearization—thường quan trọng hơn “gọi solver” một lần ngây thơ.

---

## 7. Duality: chứng nhận và giá

Mọi LP có **dual**. Duality yếu: mọi dual khả thi chặn primal. Duality mạnh (dưới khả thi/bị chặn): giá trị tối ưu trùng. Nghiệm dual tối ưu **chứng nhận** tối ưu primal—không cần chỉ tin lời solver.

Kinh tế: biến dual là **giá bóng** tài nguyên. Thuật toán: phương pháp primal-dual duy trì cả hai phía. Trong tối ưu lồi rộng hơn, dual Fenchel và Lagrange tổ chức cả họ thuật toán. Với luồng, max-flow min-cut là dual trong áo tổ hợp.

---

## 8. Không lồi và deep learning

Mất mát mạng nơ-ron thường **không lồi**: nhiều điểm tới hạn, cảnh quan giàu yên ngựa, thoái hóa do đối xứng. Lý thuyết không còn bảo đảm min toàn cục từ tìm kiếm cục bộ. Thực nghiệm, mô hình overparameterized huấn luyện bằng SGD thường đạt nghiệm *tổng quát hóa*—hiện tượng vẫn nghiên cứu sôi ([Lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/), [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/)).

Công cụ không lồi hữu ích: khởi tạo ngẫu nhiên + SGD có lịch; heuristic bậc hai (Gauss–Newton, K-FAC) với chi phí; curriculum, lớp chuẩn hóa, residual—kiến trúc như preconditioning tối ưu; phương pháp toàn cục (branch-and-bound, multistart) khi chiều nhỏ.

**Trung thực.** “Train bằng Adam” không phải chứng minh tối ưu; là quy trình kỹ thuật giảm rủi ro thực nghiệm kèm kiểm validation.

---

## 9. Tối ưu xuyên công nghệ chương 3

| Lĩnh vực | Phát biểu điển hình |
|----------|---------------------|
| Thiết kế kỹ thuật | Tối ưu ràng buộc PDE; hình dạng/topology |
| Điều khiển | LQR, MPC như QP lặp |
| Vận hành | LP/MIP lịch & định tuyến |
| Thống kê | MLE, ERM, hồi quy chính quy |
| ML | ERM không lồi qua SGD |
| Tín hiệu | Basis pursuit, compressed sensing (proxy lồi) |
| Transport | [Optimal transport Ch.6]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) |

Thống nhất triết lý và thực hành: **viết mục tiêu, tôn trọng ràng buộc, biết lớp cảnh quan, chọn thuật toán mở mắt.**

---

### Khẩu hiệu tối ưu (từ nghiên cứu video)

Ghép [3B1B gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) với sách miễn phí Boyd [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).

- **Lồi:** cực tiểu địa phương = toàn cục — lý do solver chứng nhận được.
- **Bậc nhất:** chỉ dùng gradient; mở rộng chiều cao, đổi lại điều kiện số.
- **Đối ngẫu:** biến đối ngẫu định giá ràng buộc; strong duality cần điều kiện ràng buộc.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “GD luôn tìm min toàn cục.” | Chỉ dưới điều kiện (vd lồi). |
| “Bài lồi luôn tầm thường.” | Cao chiều, không trơn, ràng buộc vẫn thách thức. |
| “LP và tối ưu ML không liên quan.” | Cùng cực tiểu mục tiêu; thuật toán & bảo đảm khác. |
| “Biến dual là rác solver.” | Giá bóng và chứng nhận tối ưu. |
| “IP không giải được vì NP-khó.” | Instance công nghiệp có cấu trúc được giải hàng ngày. |
| “Train loss nhỏ hơn ⇒ mô hình tốt hơn.” | Tổng quát hóa là về rủi ro, không chỉ loss thực nghiệm. |

---

## Bài tập

1. Nhà máy A,B: lợi nhuận và giới hạn tài nguyên—viết LP ký hiệu.  
2. $$x^4$$ lồi trên $$\mathbb{R}$$? $$-x^2$$?  
3. $$f(x,y)=x^2+10y^2$$: một bước gradient từ $$(1,1)$$, $$\eta=0.05$$.  
4. “Khớp đường thẳng bằng bình phương tối thiểu” như bài tối ưu; có lồi không?  
5. Hai câu: dual khả thi mua gì cho primal cực tiểu?  
6. “Chọn nhiều nhất hai trong ba kho” bằng biến binary.  
7. Nâng cao: vì sao softmax CE + mô hình tuyến tính lồi theo trọng, còn deep net nói chung không.

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/optimization-operations-ai/`.

**Thứ tự xem gợi ý**

1. **CORE** — 3Blue1Brown — Gradient descent, how neural networks learn: [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w).
2. **FOUNDATION** — Stanford / Boyd — Convex Optimization lectures (EE364): [https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h](https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h).
3. **FOUNDATION** — Boyd & Vandenberghe — Convex Optimization book (free PDF): [https://web.stanford.edu/~boyd/cvxbook/](https://web.stanford.edu/~boyd/cvxbook/).
4. **FOUNDATION** — MIT 6.255J / optimization OCW culture: [https://ocw.mit.edu/search/?q=optimization](https://ocw.mit.edu/search/?q=optimization).
5. **ORIENTATION** — StatQuest — Gradient Descent: [https://www.youtube.com/watch?v=sDv4f4s2SB8](https://www.youtube.com/watch?v=sDv4f4s2SB8).
6. **ORIENTATION** — 3Blue1Brown — Essence of calculus (derivatives for optimization): [https://www.youtube.com/watch?v=WUvTyaaNkzM](https://www.youtube.com/watch?v=WUvTyaaNkzM).

Danh mục URL đầy đủ: `research/video-research/optimization-operations-ai/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/optimization-operations-ai/transcripts/` · trạng thái: `research/video-research/optimization-operations-ai/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/optimization-operations-ai_IHZwWFHWa-w_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/optimization-operations-ai/references.md`.

### Video (lộ trình chính)

1. 3Blue1Brown — Gradient descent, how neural networks learn — https://www.youtube.com/watch?v=IHZwWFHWa-w
2. Stanford / Boyd — Convex Optimization lectures (EE364) — https://www.youtube.com/playlist?list=PLoROMvodv4rMJqxxviPa4AmDClvcbHi6h
3. Boyd & Vandenberghe — Convex Optimization book (free PDF) — https://web.stanford.edu/~boyd/cvxbook/
4. MIT 6.255J / optimization OCW culture — https://ocw.mit.edu/search/?q=optimization
5. StatQuest — Gradient Descent — https://www.youtube.com/watch?v=sDv4f4s2SB8
6. 3Blue1Brown — Essence of calculus (derivatives for optimization) — https://www.youtube.com/watch?v=WUvTyaaNkzM
7. Linear programming simplex culture (popular explainers) — https://en.wikipedia.org/wiki/Simplex_algorithm
8. Duality / Lagrange multipliers visual lectures — https://en.wikipedia.org/wiki/Lagrange_multiplier

### Video (tìm thêm / phụ)

9. Nocedal & Wright numerical optimization culture talks — https://web.stanford.edu/~boyd/cvxbook/

### Bài báo, sách, OCW và web

10. Boyd & Vandenberghe — Convex Optimization (PDF): https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf
11. Nesterov — Introductory Lectures on Convex Optimization: https://link.springer.com/book/10.1007/978-1-4419-8853-9
12. Wikipedia — Convex optimization: https://en.wikipedia.org/wiki/Convex_optimization
13. Wikipedia — Linear programming: https://en.wikipedia.org/wiki/Linear_programming
14. Wikipedia — Lagrange multiplier: https://en.wikipedia.org/wiki/Lagrange_multiplier
15. Wikipedia — Stochastic gradient descent: https://en.wikipedia.org/wiki/Stochastic_gradient_descent

### Trong khóa

16. Khóa: [Đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/), [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/), [Đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), [Optimal Transport]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/). Gói: `research/video-research/optimization-operations-ai/`.

## Hướng đi tiếp

- [Fourier → Xử lý tín hiệu]({{ site.baseurl }}/contents/vi/chapter03/03_08_Fourier_Signal_Processing/).  
- [Toán của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/).  
- Viết lại cơ chế cốt lõi một đoạn; ghi một câu hỏi còn mở.
