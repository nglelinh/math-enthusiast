---
layout: post
title: "Toán học của AI"
chapter: '06'
order: 2
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Một mô hình ngôn ngữ lớn trả lời câu hỏi trong chưa đầy một giây. Phía sau là các vector hàng nghìn chiều, ma trận tỷ tham số, mặt mất mát không vẽ nổi, và quá trình huấn luyện là **tối ưu dưới bất định**. Hệ AI hiện đại vừa là sản phẩm kỹ thuật vừa là **đối tượng toán học**. Bài flagship này vẽ bản đồ toán dưới học sâu và các câu hỏi còn mở—không giả vờ lĩnh vực đã “đóng”.

Kỹ năng cần luyện là **biết đọc biên giới**: tách định lý, quy luật thực nghiệm, heuristic và marketing. Quy mô và kỹ thuật quan trọng; đại số tuyến tính, xác suất, tối ưu và hình học cao chiều cũng vậy.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Mô tả mạng nơ-ron cơ bản như **ghép ánh xạ tuyến tính và phi tuyến**, viết một lớp $$x\mapsto\sigma(Wx+b)$$.
- Giải thích **huấn luyện** như cực tiểu hóa số học hàm mất mát; gradient và backpropagation như quy tắc chuỗi có tổ chức.
- Phân biệt **rủi ro thực nghiệm** (khớp tập huấn luyện) và **rủi ro thật** (kỳ vọng trên dữ liệu mới).
- Nêu ít nhất bốn lĩnh vực toán nuôi ML và mỗi lĩnh vực một câu *cách* tham gia.
- Liệt kê ba **câu hỏi toán mở** về học sâu (không phải tính năng sản phẩm).
- Phê một tuyên bố phổ thông theo chuẩn chính xác–hype.

**Kiến thức nền.** Vector, ma trận; đạo hàm như tốc độ biến thiên địa phương; ngôn ngữ xác suất cơ bản.

---

## 1. Dữ liệu sống trong không gian cao chiều

Ảnh xám kích thước $$28\times 28$$ là một vector trong $$\mathbb{R}^{784}$$. Một khung video màu, một embedding token, hay một profile biểu hiện gen là vector trong không gian ambient cao hơn. Tập dữ liệu là đám mây điểm; một batch là ma trận. **Đại số tuyến tính** là ngôn ngữ bản địa: cơ sở, chiếu, singular value, cấu trúc hạng thấp, ánh xạ tuyến tính.

**Cơ chế một bước.** Phân tích thành phần chính (PCA) và phân tích giá trị suy biến (SVD) tìm hướng phương sai lớn nhất để nén hoặc khử nhiễu bằng chiếu lên không gian con chính. Nếu $$X$$ là ma trận dữ liệu, các right singular vector hàng đầu của phiên bản đã center là các hướng chính.

Chiều cao không chỉ là “thêm tọa độ giống hệt.” Tập trung độ đo, tập điển hình, và hình học mặt cầu chiều cao đổi trực giác khoảng cách và góc: phần lớn khối lượng quả cầu chiều cao nằm gần xích đạo của một vỏ mỏng; vector ngẫu nhiên gần như trực giao với xác suất cao. Những sự kiện nuôi câu chuyện mô hình quá tham số và vì sao nearest-neighbor ngây thơ dễ lệch. (Xem bài hình học cao chiều trong chương này để sắc hơn.)

---

## 2. Mô hình: hàm từ mảnh đơn giản

Một lớp fully connected là ánh xạ tuyến tính rồi phi tuyến theo tọa độ:

$$
x \mapsto \sigma(Wx + b),
$$

với ma trận trọng số $$W$$, bias $$b$$, và activation $$\sigma$$ (ReLU, GELU, sigmoid, …). Mạng sâu **ghép** nhiều lớp như vậy. Mạng tích chập (CNN) tái sử dụng bộ lọc tuyến tính địa phương với cấu trúc tịnh tiến; residual viết lớp thành $$x \mapsto x + f_\theta(x)$$; transformer cài **attention** như ánh xạ có cấu trúc với query, key, value—dạng song tuyến và trọng số chuẩn hóa softmax trộn token thành tổ hợp tuyến tính phụ thuộc dữ liệu.

**Xấp xỉ phổ quát (định lý vs thực hành).** Dưới giả thiết nhẹ, mạng nông đủ rộng có thể xấp xỉ lớp hàm liên tục rộng trên tập compact (định lý universal approximation cổ điển). Đó là kết quả **biểu diễn**: nói *tồn tại* tham số xấp xỉ mục tiêu, **không** nói gradient descent tìm chúng hiệu quả. Độ sâu đổi *hiệu suất* biểu diễn và inductive bias. Lý thuyết *vì sao sâu thường thắng rộng trong thực hành* tinh tế hơn và vẫn đang phát triển—xấp xỉ, giải tích điều hòa của ghép, và scaling thực nghiệm đều góp mảnh.

![Pipeline toán dưới ML]({{ site.baseurl }}/img/chapter_img/ai_math_pipeline.svg)

*Hình. Chồng khái niệm từ hình học dữ liệu tới lý thuyết mở (nếu asset có trong khóa).*

---

## 3. Học như tối ưu

Huấn luyện chọn tham số $$\theta$$ để giảm **mất mát** $$L(\theta)$$ đo lỗi dự đoán trên dữ liệu (thường kèm regularizer hoặc ràng buộc kiến trúc). Mẫu chuẩn là cực tiểu hóa rủi ro thực nghiệm:

$$
\hat\theta \in \arg\min_\theta \frac{1}{n}\sum_{i=1}^n \ell\bigl(f_\theta(x_i), y_i\bigr),
$$

với $$\ell$$ mất mát điểm (bình phương, cross-entropy, …) và $$f_\theta$$ là mô hình.

**Gradient descent** và biến thể ngẫu nhiên đẩy tham số ngược hướng ước lượng gradient:

$$
\theta_{t+1} = \theta_t - \eta \widehat{\nabla L}(\theta_t).
$$

Backpropagation là quy tắc chuỗi có tổ chức cho đồ thị tính toán: tự động vi phân cho gradient chính xác của map ghép theo từng trọng số (trừ sai số floating-point).

![Cảnh quan mất mát (phác)]({{ site.baseurl }}/img/chapter_img/ai_loss_landscape.svg)

*Hình. Cảnh quan không lồi: nhiều chậu; thực hành vẫn tìm được chậu hữu ích.*

**Toán tối ưu hỏi gì.** Khi nào phương pháp hội tụ? Bước học, momentum, adaptive (Adam và họ hàng) hành xử ra sao? Batch size và nhiễu đóng vai trò gì? Trong học sâu, cảnh quan không lồi và khổng lồ; bảo đảm **lồi** cổ điển hiếm khi áp dụng trực tiếp—song thực nghiệm các phương pháp kiểu SGD thường tìm tham số **chạy được**. Giải thích khoảng trống đó là **chương trình nghiên cứu**, không phải khẩu hiệu. Giới hạn thời gian liên tục (gradient flow), chế độ mean-field/NTK, và hình học cảnh quan (điểm yên, chậu, implicit bias) là giao diện đang sống giữa giải tích, xác suất và thực hành.

---

## 4. Xác suất, thống kê và tổng quát hóa

Dữ liệu là mẫu từ phân phối $$\mathcal{D}$$ chưa biết. **Rủi ro thật** là kỳ vọng mất mát trên mẫu mới; **rủi ro thực nghiệm** trung bình trên tập huấn luyện:

> Mất mát huấn luyện thấp không tự động nghĩa rủi ro thật thấp.

Lý thuyết học thống kê cổ điển chặn khe hở tổng quát hóa bằng độ phức tạp lớp (VC, Rademacher). Mạng hiện đại **quá tham số**—có thể nội suy nhãn nhiễu—song vẫn thường tổng quát hóa trên dữ liệu có cấu trúc. **Double descent** thách thức folklore đường cong U bias–variance đơn giản. Đây là vùng LO6: nhiều giải thích phổ thông không đủ.

Xác suất còn vào gradient ngẫu nhiên, quan điểm Bayes/PAC-Bayes, hiệu chuẩn, và mô hình sinh (likelihood, phân kỳ, score matching, liên kết vận chuyển tối ưu).

---

## 5. Các sợi toán khác (bản đồ, không bách khoa)

| Lĩnh vực | Vai trò |
|----------|---------|
| Lý thuyết thông tin | Cross-entropy, nén, gợi ý dung lượng |
| Hệ động lực | Quỹ đạo huấn luyện; giới hạn thời gian liên tục |
| Giải tích điều hòa / xấp xỉ | Hàm nào biểu diễn hiệu quả |
| Lý thuyết trò chơi | Adversarial training; GAN như cân bằng lý tưởng hóa |
| Suy diễn nhân quả | Vượt i.i.d.; chính sách và robust |
| Logic / formal methods | Đặc tả, kiểm chứng (còn non trẻ so với quy mô) |
| Vận chuyển tối ưu | Khoảng cách giữa phân phối; sinh và domain adaptation |
| Hình học cao chiều | Tập trung, chiếu ngẫu nhiên, hình học embedding |

Bạn không cần thành thạo tất cả. Hãy thấy AI là **người tiêu dùng nhiều lĩnh vực**, không thay thế chúng. Đại số tuyến tính và giải tích là công cụ hàng ngày; xác suất và tối ưu dựng câu chuyện huấn luyện; hình học và thống kê dựng câu chuyện tổng quát hóa.

---

## 6. Điều còn mở (danh sách trung thực)

1. Tổng quát hóa mạng quá tham số trên dữ liệu có cấu trúc.
2. **Implicit bias** của bộ tối ưu: trong vô số nghiệm mất mát huấn luyện bằng không, SGD chọn cái nào?
3. Học đặc trưng vs chế độ kernel/NTK “lười”.
4. Robust và đối kháng: hình học biên quyết định.
5. Scaling laws: fit thực nghiệm mạnh; suy diễn lý thuyết còn từng phần.
6. Hành vi foundation model: in-context learning, “emergence”—tách đo lường, định nghĩa mơ hồ, marketing.

**Quy luật thực nghiệm ≠ định lý ≠ tuyên bố sản phẩm.**

---

## 7. Hype vs chính xác

| Tuyên bố thổi | Diễn đạt chính xác hơn |
|---------------|------------------------|
| “Mạng nơ-ron như não.” | Ẩn dụ thô; kiến trúc và quy tắc học khác sâu. |
| “Đã giải trí tuệ.” | Hiệu năng nhiệm vụ hẹp ≠ trí tuệ tổng quát. |
| “Chỉ còn scale, hết toán.” | Scale quan trọng; lý thuyết tổng quát hóa/robust chưa xong. |
| “Loss giảm = đã hiểu.” | Metric huấn luyện ≠ hiểu khái niệm, năng lực nhân quả, hay an toàn. |
| “Attention *is* all you need như lý thuyết khoa học đầy đủ.” | Transformer là lớp kiến trúc thành công; khẩu hiệu **không** phải định lý đầy đủ về nhận thức. |

Khi phê bài báo AI, đòi bốn câu: **đối tượng toán? đã chứng minh? đã đo? đang suy đoán?**

---

## 8. Chuỗi cơ chế tối thiểu

**Dữ liệu vector** → **mô hình** $$f_\theta$$ → **mất mát** → **ước lượng gradient** → **cập nhật tham số** → **bộ dự đoán triển khai** đánh giá trên rủi ro hold-out.

Mỗi mũi tên là chỗ toán có thể hỏng: đặc trưng xấu, loss sai, gradient nổ/biến mất, dịch phân phối, metric đánh giá sai.

### Narrative ngắn: phân loại thư rác

Mỗi email thành vector $$x\in\mathbb{R}^d$$. Hồi quy logistic:

$$
\mathbb{P}(Y=1\mid x)=\sigma(w^\top x+b),\qquad
\sigma(z)=\frac{1}{1+e^{-z}},
$$

mất mát cross-entropy; gradient descent cập nhật $$(w,b)$$ trên mini-batch. Đã xuất hiện đủ nhân vật: tích vô hướng, link phi tuyến, loss xác suất, tối ưu ngẫu nhiên, đánh giá hold-out. Thay map tuyến tính bằng mạng sâu—xương sống toán **cùng một khung**, chỉ lớp giả thuyết và cảnh quan tối ưu phình ra.

### Đánh giá có chữ

Accuracy trên test set là **ước lượng thực nghiệm**, không phải chặn PAC. Calibration, hiệu năng nhóm con, robust dưới dịch phân phối, rủi ro adversarial là mục tiêu toán khác. Văn hóa bảng xếp hạng tối ưu cái được đo; lý thuyết nhắc cái *không* được đo. Khi báo chí nói “tầm người”, hỏi: phân phối nào, metric nào, kiểm soát nhiễm đánh giá nào?

---

## Nhầm lẫn thường gặp

| Tuyên bố | Kết luận | Sửa |
|----------|----------|-----|
| “AI chỉ là thống kê.” | Thiếu | Còn tối ưu, đại số tuyến tính, xấp xỉ. |
| “GD luôn tìm cực tiểu toàn cục.” | Sai nói chung | Không lồi; thực hành tìm điểm hữu ích. |
| “Thêm tham số luôn overfit.” | Folklore | Chế độ quá tham số tinh tế hơn. |
| “Universal approximation giải thích thành công DL.” | Thổi | Tồn tại ≠ tìm được hiệu quả. |
| “Scaling law là định lý.” | Thường không | Fit thực nghiệm; lý thuyết từng phần. |
| “Lý thuyết phải xong trước khi kỹ thuật hợp pháp.” | Sai lịch sử | Bay trước khi kiểm soát Navier–Stokes đầy đủ; lý thuyết vẫn giảm rủi ro và dẫn thiết kế. |

---

## Bài tập

1. Nhân ma trận–vector $$2\times 2$$ bằng tay; hiểu như lớp tuyến tính không bias.
2. Định nghĩa rủi ro thực nghiệm và rủi ro thật; một câu vì sao chúng lệch.
3. (≤250 từ) Chuỗi data → model → loss → update → deploy; một lỗi toán ở mỗi bước.
4. Ba câu: đại số tuyến tính, xác suất, tối ưu xuất hiện thế nào khi huấn luyện phân loại.
5. Tìm một tin AI; viết lại hai câu tách đo lường / suy đoán.
6. Chọn một mục Mục 6; viết một câu hỏi thực nghiệm và một câu hỏi toán liên quan.
7. Đọc abstract về double descent hoặc NTK; liệt kê ba thuật ngữ cần tra.

---


---

## Kiến thức trích từ nghiên cứu video

Tóm tắt cho seminar (đối chiếu nguồn viết; **không bịa transcript**). Gói: `research/video-research/mathematics-of-ai/analysis.md`.

### Trạng thái

**Lĩnh vực nghiên cứu đang hoạt động.** Thực hành kỹ thuật cốt lõi đã chín; hiểu toán về học sâu (tổng quát hóa, cảnh quan tối ưu, học đặc trưng) vẫn **từng phần** tính đến 2026.

### Phát biểu / slogan cốt lõi

Xấp xỉ phổ quát cổ điển là định lý *biểu diễn*, không phải định lý huấn luyện. Huấn luyện là cực tiểu hóa rủi ro thực nghiệm bằng SGD trên $$L(\theta)$$ không lồi. Tổng quát hóa mạng quá tham số **chưa** được VC cổ điển kết thúc.

### Định nghĩa cần cố định

- **Map lớp.** $$x\mapsto \sigma(Wx+b)$$ với phi tuyến $$\sigma$$.
- **Rủi ro thực nghiệm.** $$\frac1n\sum_i \ell(f_\theta(x_i),y_i)$$ so với rủi ro thật $$\mathbb{E}\ell$$.

### Vệ sinh khái niệm

- Xấp xỉ phổ quát **không** ⇒ bộ tối ưu tìm được bộ xấp xỉ.
- Demo sản phẩm **không** đồng nhất định lý toán.


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh/bài báo gốc khi tuyên bố mang tính then chốt. Chi tiết xếp hạng: `research/video-research/mathematics-of-ai/`.

**Thứ tự gợi ý**

1. **Định hướng** — 3Blue1Brown — But what is a neural network?: [https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk).  
2. **Cốt lõi** — 3Blue1Brown — Gradient descent, how neural networks learn: [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w).  
3. **Cốt lõi** — 3Blue1Brown — What is backpropagation really doing?: [https://www.youtube.com/watch?v=Ilg3gGewQ5U](https://www.youtube.com/watch?v=Ilg3gGewQ5U).  
4. **Nền tảng** — 3Blue1Brown — Backpropagation calculus: [https://www.youtube.com/watch?v=tIeHLnjs5U8](https://www.youtube.com/watch?v=tIeHLnjs5U8).  
5. **Meta** — 3Blue1Brown Neural Networks playlist: [https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi).  

**Nhắc trạng thái:** **Active research field.** Core engineering practice is mature; mathematical understanding of deep learning (generalization, optimization landscapes, feature learning) remains partial as of 2026.

---



### Transcript & frames (extract flagship)

Transcript caption và unit theo thời gian: `research/video-research/mathematics-of-ai/transcripts/` · trạng thái: `research/video-research/mathematics-of-ai/TRANSCRIPT_STATUS.md` · danh sách master: `research/video-research/FLAGSHIP_TRANSCRIPTS.md`.

Caption tải tự động (yt-dlp)—dùng để điều hướng, **không** thay nội dung bài.


![Frame mẫu video flagship]({{ site.baseurl }}/img/video_research/flagships/ai_3b1b_nn_frame01.jpg)

*Hình. Frame mẫu từ video flagship chính (xem pack cho timestamp).*

## Tài liệu tham khảo

1. Goodfellow, Bengio, Courville — *Deep Learning*.
2. Survey gần đây về generalization của deep nets.
3. Lý thuyết học cổ điển: Vapnik; Rademacher.
4. NTK / mean-field — chế độ lazy vs feature learning.
5. Liên kết: [Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/), [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/), [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/).

---


Danh mục URL đầy đủ: `research/video-research/mathematics-of-ai/references.md`.

### Video (lộ trình gợi ý)

- 3Blue1Brown — But what is a neural network? (ORIENTATION): https://www.youtube.com/watch?v=aircAruvnKk
- 3Blue1Brown — Gradient descent, how neural networks learn (CORE): https://www.youtube.com/watch?v=IHZwWFHWa-w
- 3Blue1Brown — What is backpropagation really doing? (CORE): https://www.youtube.com/watch?v=Ilg3gGewQ5U
- 3Blue1Brown — Backpropagation calculus (FOUNDATION): https://www.youtube.com/watch?v=tIeHLnjs5U8
- 3Blue1Brown Neural Networks playlist (META): https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi

### Bài báo và web (từ gói nghiên cứu)

- Goodfellow, Bengio, Courville — Deep Learning (book site): https://www.deeplearningbook.org/
- Wikipedia — Universal approximation theorem: https://en.wikipedia.org/wiki/Universal_approximation_theorem
- Double descent literature hub (Belkin et al. 2019): https://arxiv.org/abs/1812.11118
- 3Blue1Brown site: https://www.3blue1brown.com/
- Wikipedia — Deep learning: https://en.wikipedia.org/wiki/Deep_learning

### Khóa học

- Gói: `research/video-research/mathematics-of-ai/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/); [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).
- [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/); [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/).
- Thực hành: huấn luyện mô hình nhỏ; ghi train vs test; gắn với Mục 4.
- Giữ bảng tuyên bố: *định lý / chặn / luật thực nghiệm / hype*.
