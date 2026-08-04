---
layout: post
title: "Đại số tuyến tính → AI & Học máy"
chapter: '03'
order: 3
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
lesson_type: required
---

Mạng nơ-ron không “suy nghĩ bằng chữ” trong GPU. Nó nhân ma trận, cộng bias, áp phi tuyến đơn giản, rồi lặp lại. Hệ gợi ý, phân loại ảnh, mô hình ngôn ngữ và bảng điều khiển PCA đều nói cùng tiếng mẹ đẻ: **vector, ma trận, ánh xạ tuyến tính**—với gia vị phi tuyến.

**Lộ trình:** dữ liệu như hình học → lớp tuyến tính → độ sâu và phi tuyến → SVD/PCA → gradient theo tham số → tích chập & attention → điều đại số tuyến tính *không* giải thích hết → nhầm lẫn.

Bài này vẽ **chuỗi cơ chế** từ đại số tuyến tính trừu tượng đến mô hình triển khai—không khẩu hiệu “AI dùng toán,” mà *phép toán nào* nuôi huấn luyện và suy luận.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Đọc ví dụ như vector và tập dữ liệu như ma trận; đo tương tự bằng tích trong và chuẩn.
- Giải thích lớp $$x\mapsto Wx+b$$ và vì sao xếp ánh xạ tuyến tính không có phi tuyến sẽ sụp về một ánh xạ affine.
- Nêu SVD/PCA cho biết gì (hướng chính, nén, hạng thấp).
- Nối huấn luyện với giải tích nhiều biến: hàm mất mát, gradient, quy tắc chuỗi (backprop).
- Mô tả convolution và attention như phép tuyến tính (hoặc song tuyến) có cấu trúc.
- Tránh “AI là ma thuật,” “AI chỉ là thống kê,” “sâu hơn luôn thông minh hơn.”

**Kiến thức nền.** Nhân ma trận, đạo hàm cơ bản. Hữu ích: giá trị riêng như hệ số giãn.

**Liên kết.** [Toán của AI (Ch.6)]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/), [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/).

---

## 1. Dữ liệu như hình học

Ảnh xám $$28\times 28$$ là vector trong $$\mathbb{R}^{784}$$. Embedding câu là vector. Lô $$n$$ mẫu với $$d$$ đặc trưng là ma trận $$X\in\mathbb{R}^{n\times d}$$. Khoảng cách, góc, hình chiếu, không gian con trở thành ngôn ngữ tự nhiên.

Tích trong $$\langle u,v\rangle=u^\top v$$ đo sự thẳng hàng. Cosine similarity dùng trong truy hồi và embedding. Ánh xạ $$x\mapsto Ax$$ xoay, giãn, cắt, chiếu.

**Khẩu hiệu cơ chế.**  
*Học máy biến đầu vào thô thành vector, rồi học ánh xạ làm cho tác vụ trở nên dễ về mặt hình học.*

---

## 2. Lớp tuyến tính: nguyên tử affine

$$
x \mapsto \sigma(Wx + b),
$$

với $$W$$ ma trận trọng số, $$b$$ bias, $$\sigma$$ phi tuyến theo tọa độ (ReLU, GELU, …).

**Không** có $$\sigma$$, xếp lớp sụp:

$$
W_2(W_1 x+b_1)+b_2=(W_2W_1)x+(W_2b_1+b_2).
$$

**Có** $$\sigma$$, độ sâu tạo đặc trưng phân cấp. Suy luận là chuỗi nhân ma trận + phi tuyến rẻ—khớp GPU/TPU. “Bùng nổ phần cứng AI” một phần là bùng nổ phần cứng đại số tuyến tính.

---

## 3. Độ sâu và biểu diễn

Các lớp sớm trong thị giác phản ứng cạnh/kết cấu; lớp sau phản ứng bộ phận/đối tượng—thực nghiệm, không ma thuật. Đại số học, mỗi lớp nhúng lại biểu diễn trước:

$$
h^{(\ell+1)}=\sigma\bigl(W^{(\ell)}h^{(\ell)}+b^{(\ell)}\bigr).
$$

Lớp cuối thường tuyến tính (hoặc softmax-tuyến tính) cho phân loại: điểm số $$Wh+b$$ trên các lớp; softmax biến điểm thành vector xác suất—đại số tuyến tính sinh điểm, xác suất chỉ là lớp vỏ đọc kết quả.

**Định lý xấp xỉ phổ dụng** nói mạng nông rộng có thể xấp xỉ hàm liên tục trên tập compact; độ sâu thường mang *inductive bias* và hiệu quả tham số tốt hơn cho cùng độ chính xác. Đại số tuyến tính một mình không chọn kiến trúc; nó *thực thi* kiến trúc bạn đã chọn. Câu hỏi “nông rộng hay sâu hẹp?” là câu hỏi về thiên kiến quy nạp và tối ưu, không chỉ về khả năng xấp xỉ trừu tượng.

---

## 4. SVD, PCA và cấu trúc hạng thấp

Mọi ma trận thực $$A\in\mathbb{R}^{m\times n}$$ có **SVD**

$$
A=U\Sigma V^\top,
$$

với $$U,V$$ trực giao và các giá trị singular không âm trên đường chéo $$\Sigma$$. Cắt các giá trị singular nhỏ cho xấp xỉ hạng thấp tốt nhất theo chuẩn Frobenius (và chuẩn phổ)—định lý **Eckart–Young**.

**PCA** là anh em dữ liệu: căn giữa ma trận dữ liệu, lấy hướng phương sai lớn qua SVD hoặc ma trận hiệp phương sai. Nén, khử nhiễu, trực quan hóa khám phá đều cưỡi sự thật này: *giữ hướng dữ liệu biến thiên nhiều nhất; bỏ hướng gần như null.*

**Cơ chế.**  
*Dữ liệu cao chiều thường nằm gần cấu trúc thấp chiều; SVD/PCA tìm các trục đó như bài tối ưu có lời giải phổ.*

Hệ gợi ý: ma trận user–item xấp xỉ $$UV^\top$$—lọc cộng tác như đại số tuyến tính. Embedding từ và topic model lặp lại ý phân tích hạng thấp. Khi ma trận thưa và rất lớn, các thuật toán SVD ngẫu nhiên/iterative thay cho phân rã đầy đủ; tư duy vẫn là “chiều quan trọng là chiều singular lớn.”

---

## 5. Gradient: giải tích trên không gian tham số

Huấn luyện chọn tham số $$\theta$$ (mọi trọng số và bias) để cực tiểu hóa mất mát $$L(\theta)$$ trung bình trên dữ liệu—ví dụ cross-entropy cho phân loại hay sai số bình phương cho hồi quy. Bước gradient:

$$
\theta \leftarrow \theta - \eta \nabla_\theta L(\theta).
$$

Vì $$L$$ là hợp của nhân ma trận và phi tuyến sơ cấp, **quy tắc chuỗi** tính $$\nabla_\theta L$$ từng lớp: **backpropagation**. Không phải toán mới ngoài giải tích nhiều biến—nhưng *đồ thị* tính toán khổng lồ nên engine auto-diff quan trọng.

**Hình dạng thực tiễn.** Mini-batch đầu vào là ma trận; lớp tuyến tính là nhân ma trận (hoặc GEMM theo lô). Auto-diff theo dõi mỗi tensor phụ thuộc tham số thế nào để một lượt ngược cho mọi đạo hàm riêng cần thiết. Ổn định số (gradient biến mất/bùng nổ, mixed precision) vẫn là đại số tuyến tính cộng văn hóa dấu chấm động—số điều kiện và scale, không huyền bí.

**Cơ chế.**  
*Học là tối ưu một vô hướng trên không gian tham số cao chiều; gradient là đại số tuyến tính cục bộ của vô hướng đó.*

Xem [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/) (khi gradient hội tụ, bước nhảy) và [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/) (rủi ro kỳ vọng so với mẫu hữu hạn).

---

## 6. Ánh xạ có cấu trúc: convolution và attention

Không phải mọi ma trận đều dày và vô cấu trúc.

**Convolution** (ảnh, âm thanh) là ánh xạ tuyến tính với **bộ lọc cục bộ chia sẻ**: cùng một kernel nhỏ áp mọi vị trí. Ngôn ngữ ma trận: cấu trúc Toeplitz/circulant theo khối. Ít tham số; đẳng biến tịnh tiến được “xây sẵn.”

**Self-attention** (transformer) trộn token bằng

$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\Bigl(\frac{QK^\top}{\sqrt{d}}\Bigr)V,
$$

với $$Q,K,V$$ là hình chiếu tuyến tính của đầu vào. Tích $$QK^\top$$ song tuyến theo dữ liệu; softmax sinh trọng số trộn; nhân $$V$$ là tổ hợp tuyến tính khác. Cơ chế vẫn đại số tuyến tính + phi tuyến chuẩn hóa—mô hình chuỗi quy mô lớn không cần recurrence cổ điển.

**Cấu trúc thưa và đồ thị.** Mạng nơ-ron đồ thị (GNN) thay $$W$$ dày bằng truyền tin theo cạnh—ánh xạ tuyến tính tôn trọng tôpô mạng, cầu nối [lý thuyết đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/).

---

## 7. Góc nhìn phổ: ổn định, mode, kernel

Giá trị riêng và vector riêng xuất hiện khi động lực hoặc dạng toàn phương quan trọng:

- Mạng residual/tuyến tính hóa và mạng hồi quy: lũy thừa $$A^t$$ và bán kính phổ.
- Laplacian đồ thị: độ trơn tín hiệu trên mạng; spectral clustering.
- Kernel methods: ma trận Gram $$K_{ij}=k(x_i,x_j)$$; học trong không gian đặc trưng mà không viết tường minh đặc trưng.
- Hiệp phương sai Gaussian: trục chính của ellipsoid bất định.

Bạn không cần khóa phổ đầy đủ để dùng PyTorch—nhưng khi huấn luyện phân kỳ, biểu diễn sụp, hay bộ làm mượt đồ thị “oversmooth,” trực giác phổ là ngôn ngữ gỡ lỗi.

---

## 8. Điều đại số tuyến tính không kết thúc

Đại số tuyến tính là cần, chưa đủ:

1. **Thống kê / xác suất** — tổng quát hóa, hiệu chỉnh, tuyên bố nhân quả.  
2. **Tối ưu** — thuật toán, learning rate, thiên kiến ẩn của SGD.  
3. **Phần cứng và hệ thống** — bố trí bộ nhớ, lượng tử hóa, huấn luyện phân tán.  
4. **Dữ liệu và mục tiêu** — nhãn, phần thưởng, phản hồi con người; không có phép nhân ma trận nào “bịa” giá trị.  
5. **Hiện tượng phi tuyến** — động lực huấn luyện hỗn loạn, hành vi trỗi, ví dụ adversarial.

[Toán của AI (Ch.6)]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) quay lại biên lý thuyết. Ở đây khẳng định hẹp và chắc: **nền tính toán của ML hiện đại là đại số tuyến tính với keo phi tuyến.**

---

## 9. Ảnh end-to-end tối thiểu

1. Mã hóa đầu vào thành vector.  
2. Ánh xạ affine học được + phi tuyến (và biến thể có cấu trúc: conv, attention, message passing).  
3. Đọc dự đoán bằng lớp tuyến tính cuối.  
4. Đo mất mát; backprop; cập nhật.  
5. Tùy chọn: nén/phân tích biểu diễn bằng SVD/PCA.

Mọi “sản phẩm AI” phân loại, xếp hạng, embedding hay sinh qua mạng nơ-ron đều thực thi một biến thể của vòng lặp này. Toán thuần của không gian vector, đối ngẫu và định lý phổ già hơn silicon; ngành công nghiệp là người tiêu thụ khổng lồ các ý tưởng ấy ở quy mô.

---

### Đại số tuyến tính như nền ML (từ nghiên cứu video)

Lộ trình: 3Blue1Brown [mạng nơ-ron](https://www.youtube.com/watch?v=aircAruvnKk) → [gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) → [backprop](https://www.youtube.com/watch?v=Ilg3gGewQ5U); thêm Strang [18.06 bài 1](https://www.youtube.com/watch?v=J7DzL2_Na80).

- Mạng sâu không phi tuyến vẫn chỉ là một ánh xạ affine $$x\mapsto Wx+b$$.
- Huấn luyện là gradient descent (ngẫu nhiên) trên hàm mất mát; backprop tính gradient hiệu quả.
- SVD/PCA là baseline tuyến tính cho nén/khử nhiễu trước học biểu diễn phi tuyến.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “Mạng nơ-ron chỉ là hồi quy tuyến tính.” | Có phi tuyến; độ sâu quan trọng nhờ chúng. |
| “PCA là toàn bộ học không giám sát.” | PCA là baseline tuyến tính; biểu diễn hiện đại phi tuyến. |
| “Backprop là toán mới.” | Quy tắc chuỗi / reverse-mode AD có hệ thống. |
| “Attention không phải đại số tuyến tính.” | Lõi là tích ma trận + softmax. |
| “Nhân ma trận được là đã hiểu.” | Tính toán ≠ ngữ nghĩa. |

---

## Bài tập

1. $$W=\begin{pmatrix}1&2\\0&1\end{pmatrix}$$, $$x=\begin{pmatrix}1\\1\end{pmatrix}$$: tính $$Wx$$; hiệu ứng hình học?  
2. Chứng minh hợp ánh xạ affine vẫn affine; vì sao cần phi tuyến giữa lớp?  
3. Hai câu: vì sao thành phần chính hàng đầu cực đại phương sai bắt được?  
4. $$L(\theta)=(\theta-3)^2$$, $$\eta=0.1$$, hai bước gradient từ $$0$$.  
5. Một câu nối GPU nhân ma trận với suy luận nơ-ron.  
6. Convolution $$3\times 3$$ có phải ánh xạ tuyến tính thưa có cấu trúc?  
7. Nâng cao: liên hệ vector singular phải của $$X$$ với vector riêng của $$X^\top X$$.

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/linear-algebra-ai/`.

**Thứ tự xem gợi ý**

1. **ORIENTATION** — 3Blue1Brown — But what is a neural network?: [https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk).
2. **CORE** — 3Blue1Brown — Gradient descent, how neural networks learn: [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w).
3. **CORE** — 3Blue1Brown — What is backpropagation really doing?: [https://www.youtube.com/watch?v=Ilg3gGewQ5U](https://www.youtube.com/watch?v=Ilg3gGewQ5U).
4. **FOUNDATION** — 3Blue1Brown — Essence of linear algebra (playlist): [https://www.3blue1brown.com/topics/linear-algebra](https://www.3blue1brown.com/topics/linear-algebra).
5. **FOUNDATION** — 3Blue1Brown — Essence of linear algebra ch.1 (vectors): [https://www.youtube.com/watch?v=fNk_zzaMoSs](https://www.youtube.com/watch?v=fNk_zzaMoSs).
6. **FOUNDATION** — MIT OCW 18.06 Strang — Geometry of linear equations: [https://www.youtube.com/watch?v=J7DzL2_Na80](https://www.youtube.com/watch?v=J7DzL2_Na80).

Danh mục URL đầy đủ: `research/video-research/linear-algebra-ai/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/linear-algebra-ai/transcripts/` · trạng thái: `research/video-research/linear-algebra-ai/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/linear-algebra-ai_aircAruvnKk_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/linear-algebra-ai/references.md`.

### Video (lộ trình chính)

1. 3Blue1Brown — But what is a neural network? — https://www.youtube.com/watch?v=aircAruvnKk
2. 3Blue1Brown — Gradient descent, how neural networks learn — https://www.youtube.com/watch?v=IHZwWFHWa-w
3. 3Blue1Brown — What is backpropagation really doing? — https://www.youtube.com/watch?v=Ilg3gGewQ5U
4. 3Blue1Brown — Essence of linear algebra (playlist) — https://www.3blue1brown.com/topics/linear-algebra
5. 3Blue1Brown — Essence of linear algebra ch.1 (vectors) — https://www.youtube.com/watch?v=fNk_zzaMoSs
6. MIT OCW 18.06 Strang — Geometry of linear equations — https://www.youtube.com/watch?v=J7DzL2_Na80
7. MIT OCW 18.06 playlist (Strang) — https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8
8. MIT OCW 18.06 course page — https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
9. 3Blue1Brown neural networks playlist — https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi

### Video (tìm thêm / phụ)

10. Stanford CS229 / related ML theory lectures (optional survey) — https://www.youtube.com/@stanfordonline

### Bài báo, sách, OCW và web

11. Vaswani et al. — Attention Is All You Need (2017): https://arxiv.org/abs/1706.03762
12. Goodfellow, Bengio, Courville — Deep Learning (book site): https://www.deeplearningbook.org/
13. Strang — Linear Algebra and Learning from Data (MIT): https://math.mit.edu/~gs/learningfromdata/
14. Wikipedia — Singular value decomposition: https://en.wikipedia.org/wiki/Singular_value_decomposition
15. 3Blue1Brown linear algebra topic hub: https://www.3blue1brown.com/topics/linear-algebra

### Trong khóa

16. Khóa: [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/), [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/), [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/). Gói: `research/video-research/linear-algebra-ai/`.

## Hướng đi tiếp

- [Xác suất → Khoa học dữ liệu]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/).  
- [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/).  
- Viết lại cơ chế cốt lõi một đoạn; ghi một câu hỏi còn mở.
