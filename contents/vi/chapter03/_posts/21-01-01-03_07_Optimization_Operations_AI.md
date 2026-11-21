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

Hãng hàng không xếp lịch cho tổ bay. Bệnh viện phân giường cho bệnh nhân. Trung tâm dữ liệu phân bổ công việc cho máy chủ. Mạng nơ-ron điều chỉnh hàng triệu trọng số. Bề ngoài khác nhau, nhưng tất cả đều là một câu hỏi: **chọn các biến quyết định sao cho mục tiêu nhỏ nhất (hoặc lớn nhất), trong khi thỏa mãn các ràng buộc.**

**Lộ trình:** phát biểu bài toán → tính lồi → gradient và các phương pháp bậc nhất → ràng buộc, nhân tử Lagrange và điều kiện KKT → quy hoạch tuyến tính và quy hoạch nguyên → đối ngẫu → bề mặt không lồi trong học máy → nhầm lẫn thường gặp.

Bài này nối tối ưu hóa toán học với vận trù học và việc huấn luyện AI. Đây không phải cả một khóa học về thuật toán, nhưng đủ để bạn hiểu các bộ giải (solver) và thuật toán SGD làm gì.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Viết bài toán dưới dạng $$\min_{x\in\mathcal{X}} f(x)$$ và nhận ra mục tiêu, biến, ràng buộc trong một bài toán có lời văn.
- Giải thích vì sao **tính lồi** làm cho mọi cực tiểu địa phương đều là cực tiểu toàn cục.
- Mô tả phương pháp gradient descent và vai trò của bước nhảy; nối nó với việc huấn luyện mô hình học máy.
- Nêu quy hoạch tuyến tính (LP) và quy hoạch nguyên (IP) mô hình hóa những gì trong vận hành.
- Giải thích ý tưởng **đối ngẫu** (giá bóng, chứng nhận tối ưu).
- Tránh hai nhầm lẫn: "gradient descent luôn tìm được cực tiểu toàn cục" và "bài toán lồi thì trong thực tế luôn dễ".

**Kiến thức nền.** Gradient. Sẽ có ích nếu biết [đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/) và [xác suất, rủi ro]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/).

---

## 1. Khuôn mẫu chung

$$
\min_x f(x)\quad\text{s.t.}\quad x\in\mathcal{X}.
$$

$$f$$ là **hàm mục tiêu**; $$\mathcal{X}$$ biểu diễn các **ràng buộc**. Kỹ năng mô hình hóa chiếm một nửa lĩnh vực: phải dịch được yêu cầu như "xếp lịch y tá đúng luật lao động" thành các biến và bất đẳng thức.

**Ý chính.** *Một công nghệ được "tối ưu" khi quyết định được phát biểu thành một mục tiêu kèm ràng buộc, rồi giải bằng thuật toán có bảo đảm lý thuyết hoặc hiệu quả thực nghiệm tốt.*

---

## 2. Tính lồi: bề mặt đáng tin cậy

Một tập là lồi nếu đoạn thẳng nối hai điểm bất kỳ của nó nằm trọn trong tập. Một hàm là lồi nếu:

$$
f(tx+(1-t)y)\le tf(x)+(1-t)f(y).
$$

Với $$f$$ khả vi, điều này tương đương với $$f(y)\ge f(x)+\langle\nabla f(x),y-x\rangle$$. Khi cực tiểu một hàm lồi trên một tập lồi, mọi cực tiểu địa phương đều là cực tiểu toàn cục. Quy hoạch tuyến tính, bình phương tối thiểu, nhiều dạng SVM và phương pháp hàm chắn logarit đều thuộc loại này. Nếu gradient liên tục Lipschitz thì ta có thể chọn được độ lớn bước nhảy phù hợp.

---

## 3. Gradient và các phương pháp bậc nhất

$$
x_{k+1}=x_k-\eta_k\nabla f(x_k).
$$

Hướng ngược với gradient là hướng giảm nhanh nhất tại chỗ. Nếu bước nhảy $$\eta_k$$ quá lớn, thuật toán nhảy vọt qua thung lũng; nếu quá nhỏ, nó chạy rất chậm. Momentum, Nesterov, Adam điều chỉnh bước cập nhật dựa trên lịch sử các gradient. Chúng vẫn là phương pháp bậc nhất, nhưng phần "bộ nhớ" giúp quỹ đạo mượt hơn hoặc tự thích nghi theo từng tọa độ.

**SGD (gradient ngẫu nhiên):** khi $$f=\frac1n\sum_i f_i$$, ta ước lượng gradient bằng một số hạng hoặc một lô nhỏ (mini-batch). Điều này là bắt buộc khi dữ liệu có quy mô hàng triệu, hàng tỷ mẫu. Nhiễu có thể giúp thuật toán thoát khỏi những vùng cực tiểu nhọn kém chất lượng, và theo một số quan điểm, đóng vai trò như một dạng chính quy hóa ngầm.

**Trong AI.**  
*Huấn luyện mạng nơ-ron là tối ưu phi tuyến quy mô lớn cho rủi ro thực nghiệm; lan truyền ngược cung cấp gradient; các thuật toán họ SGD cập nhật tham số.*

Liên hệ với [xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/): hàm mất mát trên tập huấn luyện là rủi ro thực nghiệm, còn cái ta thật sự muốn nhỏ là rủi ro kỳ vọng. Tối ưu hóa mới chỉ là một nửa câu chuyện.

---

## 4. Ràng buộc: phép chiếu, hàm chắn, nhân tử Lagrange

Ràng buộc cứng $$x\in\mathcal{X}$$ được xử lý bằng các cách:

- **Phép chiếu:** thực hiện một bước gradient rồi chiếu điểm thu được lên $$\mathcal{X}$$ (projected gradient).  
- **Hàm phạt và Lagrange tăng cường:** biến ràng buộc thành một phần của hàm mục tiêu.  
- **Điểm trong và hàm chắn (interior-point, barrier):** luôn ở bên trong miền chấp nhận được, trong khi đưa tham số của hàm chắn dần về 0 (đây là lõi của các bộ giải LP/QP hiện đại).  
- **Tập hoạt động (active-set):** đoán xem những bất đẳng thức nào đang "chặt" (xảy ra dấu bằng).

Với ràng buộc đẳng thức $$g(x)=0$$, **nhân tử Lagrange** $$\lambda$$ cho hàm Lagrange $$L(x,\lambda)=f(x)+\langle\lambda,g(x)\rangle$$. Điều kiện dừng $$\nabla_x L=0$$ cùng với tính chấp nhận được là điều kiện cần, với các giả thiết chính quy. Khi có ràng buộc bất đẳng thức, ta có **điều kiện KKT**: điều kiện dừng, chấp nhận được cho bài toán gốc và bài toán đối ngẫu, và điều kiện bù.

Bạn không cần thuộc lòng từng điều kiện KKT để dùng CVXPY. Nhưng trực giác "nhân tử là **giá bóng**" rất hữu ích trong vận hành: nếu nới một ràng buộc tài nguyên thêm một đơn vị, giá trị tối ưu được cải thiện bao nhiêu?

---

## 5. Quy hoạch tuyến tính: công cụ chủ lực của vận trù học

$$
\min_x\, c^\top x \quad\text{s.t.}\quad Ax\le b,\quad x\ge 0
$$

(hoặc dạng đẳng thức). Miền chấp nhận được là một đa diện; nếu có nghiệm tối ưu thì có một nghiệm tối ưu nằm tại một đỉnh. **Phương pháp đơn hình** đi từ đỉnh này sang đỉnh khác; **phương pháp điểm trong** đi xuyên qua phần trong của miền, có bảo đảm thời gian đa thức trong trường hợp xấu nhất (và chạy rất tốt trong thực tế).

**Ứng dụng.** Bài toán pha trộn, vận tải, luồng mạng viết dưới dạng LP, kế hoạch sản xuất, và nới lỏng của các bài toán khó hơn. Lịch bay và chuỗi cung ứng dùng các tầng LP/MIP hằng ngày.

**Luồng mạng** trong bài [đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/) là một LP đặc biệt có ma trận unimodular hoàn toàn (totally unimodular), nên có nghiệm nguyên mà không cần ép điều kiện nguyên. Đây là ví dụ kinh điển: *cấu trúc* biến một bài toán rời rạc thành một LP "tự nhiên cho nghiệm nguyên".

---

## 6. Quy hoạch nguyên: các quyết định rời rạc

Khi biến phải là số nguyên (hoặc chỉ nhận giá trị 0/1), ta có **quy hoạch nguyên (IP) hay quy hoạch nguyên hỗn hợp (MIP)**:

$$
\min c^\top x \quad\text{s.t.}\quad Ax\le b,\quad x\in\mathbb{Z}^n.
$$

Loại bài toán này mô hình hóa các quyết định có/không: có mở kho hàng hay không; có phân công tổ bay này hay không. Quy hoạch nguyên tổng quát là NP-khó; trong thực tế người ta dùng nhánh cận (branch-and-bound), mặt phẳng cắt, heuristic và các cách phát biểu chặt. **Nới lỏng LP** (bỏ điều kiện nguyên) cho một cận và định hướng cho việc tìm kiếm.

**Ý chính.** *Vận trù học thành công nhờ mô hình hóa cấu trúc rời rạc đủ chặt để các bộ giải MIP công nghiệp thu hẹp được khoảng cách giữa cận trên và cận dưới; độ khó trong trường hợp xấu nhất không ngăn ta giải tốt các trường hợp có cấu trúc.*

Kỹ năng mô hình hóa (thêm biến phụ, thêm bất đẳng thức cắt, tuyến tính hóa) thường quan trọng hơn việc chỉ đơn giản "gọi bộ giải" một lần.

---

## 7. Đối ngẫu: chứng nhận và giá cả

Mọi bài toán LP đều có một **bài toán đối ngẫu**. Đối ngẫu yếu: mọi nghiệm chấp nhận được của bài đối ngẫu cho một cận của bài toán gốc. Đối ngẫu mạnh (khi bài toán chấp nhận được và bị chặn): hai giá trị tối ưu bằng nhau. Một nghiệm tối ưu của bài đối ngẫu **chứng nhận** rằng nghiệm của bài gốc là tối ưu, nên ta không phải chỉ tin vào lời bộ giải.

Về kinh tế, các biến đối ngẫu là **giá bóng** của tài nguyên. Về thuật toán, các phương pháp gốc – đối ngẫu duy trì đồng thời cả hai phía. Trong tối ưu lồi tổng quát hơn, đối ngẫu Fenchel và đối ngẫu Lagrange là khung tổ chức cho cả một họ thuật toán. Với bài toán luồng, định lý luồng cực đại – lát cắt cực tiểu chính là đối ngẫu dưới dạng tổ hợp.

---

## 8. Bài toán không lồi và học sâu

Hàm mất mát của mạng nơ-ron thường **không lồi**: có nhiều điểm tới hạn, nhiều điểm yên ngựa, và có những hướng suy biến do tính đối xứng. Lý thuyết không còn bảo đảm rằng tìm kiếm cục bộ sẽ cho cực tiểu toàn cục. Trên thực nghiệm, các mô hình có số tham số vượt xa số dữ liệu (overparameterized), khi huấn luyện bằng SGD, thường đạt được nghiệm *tổng quát hóa tốt*. Đây vẫn là một hiện tượng đang được nghiên cứu sôi nổi ([Lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/), [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/)).

Các công cụ hữu ích cho bài toán không lồi: khởi tạo ngẫu nhiên cộng SGD với lịch học phù hợp; các phương pháp gần bậc hai (Gauss–Newton, K-FAC) với chi phí tính toán cao hơn; học theo giáo trình (curriculum), các lớp chuẩn hóa, kết nối residual (có thể xem kiến trúc như một cách tiền điều kiện cho bài toán tối ưu); và các phương pháp toàn cục (nhánh cận, khởi động nhiều lần) khi số chiều nhỏ.

**Nói thật.** "Huấn luyện bằng Adam" không phải là một chứng minh tối ưu. Đó là một quy trình kỹ thuật để giảm rủi ro thực nghiệm, đi kèm việc kiểm tra trên tập validation.

---

## 9. Tối ưu hóa trong các công nghệ của chương 3

| Lĩnh vực | Bài toán điển hình |
|----------|---------------------|
| Thiết kế kỹ thuật | Tối ưu có ràng buộc là PDE; tối ưu hình dạng và tôpô |
| Điều khiển | LQR, điều khiển dự báo (MPC) như các bài QP giải lặp |
| Vận hành | LP/MIP cho lập lịch và định tuyến |
| Thống kê | MLE, ERM, hồi quy có chính quy hóa |
| Học máy | ERM không lồi giải bằng SGD |
| Xử lý tín hiệu | Basis pursuit, cảm biến nén (thay bài toán khó bằng bài toán lồi) |
| Vận chuyển | [Vận chuyển tối ưu Ch.6]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/) |

Điểm chung về cả tư duy lẫn thực hành: **viết rõ mục tiêu, tôn trọng ràng buộc, biết bề mặt bài toán thuộc loại nào, và chọn thuật toán một cách có hiểu biết.**

---

### Tóm tắt về tối ưu (từ phần tìm hiểu video)

Xem [3B1B gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) cùng với cuốn sách miễn phí của Boyd [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).

- **Tính lồi:** cực tiểu địa phương cũng là cực tiểu toàn cục; đó là lý do bộ giải có thể chứng nhận kết quả.
- **Phương pháp bậc nhất:** chỉ dùng gradient; chạy được với số chiều rất lớn, đổi lại phụ thuộc nhiều vào tính điều kiện của bài toán.
- **Đối ngẫu:** biến đối ngẫu cho biết "giá" của các ràng buộc; đối ngẫu mạnh cần thêm điều kiện về ràng buộc.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Gradient descent luôn tìm được cực tiểu toàn cục." | Chỉ đúng với điều kiện nhất định (ví dụ bài toán lồi). |
| "Bài toán lồi lúc nào cũng tầm thường." | Nhiều chiều, không trơn, nhiều ràng buộc vẫn là thách thức. |
| "LP và tối ưu trong học máy không liên quan gì nhau." | Cùng là cực tiểu hóa một mục tiêu; khác nhau ở thuật toán và bảo đảm. |
| "Biến đối ngẫu chỉ là thứ thừa của bộ giải." | Đó là giá bóng và chứng nhận tối ưu. |
| "Quy hoạch nguyên không giải được vì NP-khó." | Các bài toán công nghiệp có cấu trúc được giải hằng ngày. |
| "Mất mát huấn luyện nhỏ hơn thì mô hình tốt hơn." | Khả năng tổng quát hóa phụ thuộc vào rủi ro, không chỉ vào mất mát thực nghiệm. |

---

## Bài tập

1. Một nhà máy sản xuất hai sản phẩm A, B với lợi nhuận và giới hạn tài nguyên cho trước. Viết bài toán LP bằng ký hiệu.  
2. Hàm $$x^4$$ có lồi trên $$\mathbb{R}$$ không? Còn $$-x^2$$?  
3. Với $$f(x,y)=x^2+10y^2$$, thực hiện một bước gradient từ $$(1,1)$$ với $$\eta=0.05$$.  
4. Viết bài toán "khớp đường thẳng bằng bình phương tối thiểu" thành một bài toán tối ưu. Bài toán có lồi không?  
5. Viết hai câu: một nghiệm chấp nhận được của bài đối ngẫu cho ta biết gì về bài toán cực tiểu gốc?  
6. Biểu diễn điều kiện "chọn nhiều nhất hai trong ba kho hàng" bằng biến nhị phân.  
7. Nâng cao: vì sao entropy chéo với softmax trên một mô hình tuyến tính là hàm lồi theo trọng số, còn với mạng sâu nói chung thì không?

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
- Tự viết lại ý chính của bài trong một đoạn văn, và ghi ra một câu hỏi bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước**: [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w) (3Blue1Brown, tiếng Anh). Hàm mất mát và cách mạng nơ-ron học bằng gradient descent, minh họa bằng hình ảnh. Nên xem trước khi đọc §3.
- [Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8) (StatQuest with Josh Starmer, tiếng Anh). Tính từng bước gradient descent trên một ví dụ hồi quy đơn giản. Hợp để luyện bài tập 3 và 4.
- [The essence of calculus](https://www.youtube.com/watch?v=WUvTyaaNkzM) (3Blue1Brown, tiếng Anh). Ôn lại đạo hàm, nền tảng của gradient. Dành cho ai muốn củng cố kiến thức giải tích.
