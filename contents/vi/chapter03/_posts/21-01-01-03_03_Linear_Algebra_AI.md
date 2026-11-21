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

Bên trong GPU, mạng nơ-ron không "suy nghĩ bằng chữ". Nó nhân ma trận, cộng thêm hệ số dịch (bias), áp một hàm phi tuyến đơn giản, rồi lặp lại. Hệ gợi ý, phân loại ảnh, mô hình ngôn ngữ hay biểu đồ PCA đều dùng chung một ngôn ngữ: **vectơ, ma trận, ánh xạ tuyến tính**, kèm thêm một chút phi tuyến.

**Lộ trình:** dữ liệu nhìn như hình học → lớp tuyến tính → độ sâu và phi tuyến → SVD/PCA → gradient theo tham số → tích chập và attention → những điều đại số tuyến tính *không* giải thích được → nhầm lẫn thường gặp.

Bài này chỉ ra **chuỗi các bước** đi từ đại số tuyến tính trừu tượng đến các mô hình đang chạy thực tế. Mục đích không phải lặp lại câu "AI dùng toán", mà là chỉ rõ *phép toán nào* đứng sau việc huấn luyện và suy luận.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Xem mỗi mẫu dữ liệu là một vectơ và cả tập dữ liệu là một ma trận; đo độ giống nhau bằng tích vô hướng và chuẩn.
- Giải thích lớp $$x\mapsto Wx+b$$, và vì sao xếp chồng các ánh xạ tuyến tính mà không có phi tuyến thì chỉ thu được một ánh xạ affine.
- Nêu được SVD/PCA cho ta biết điều gì (các hướng chính, nén dữ liệu, cấu trúc hạng thấp).
- Nối việc huấn luyện với giải tích nhiều biến: hàm mất mát, gradient, quy tắc dây chuyền (lan truyền ngược).
- Mô tả tích chập (convolution) và attention như những phép toán tuyến tính (hoặc song tuyến) có cấu trúc.
- Tránh ba nhầm lẫn: "AI là phép màu", "AI chỉ là thống kê", "mạng càng sâu càng thông minh".

**Kiến thức nền.** Phép nhân ma trận, đạo hàm cơ bản. Sẽ có ích nếu biết giá trị riêng như một hệ số co giãn.

**Liên kết.** [Toán của AI (Ch.6)]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/), [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/).

---

## 1. Nhìn dữ liệu như hình học

Một ảnh xám kích thước $$28\times 28$$ là một vectơ trong $$\mathbb{R}^{784}$$. Biểu diễn nhúng (embedding) của một câu văn là một vectơ. Một lô gồm $$n$$ mẫu, mỗi mẫu có $$d$$ đặc trưng, là một ma trận $$X\in\mathbb{R}^{n\times d}$$. Khi đó khoảng cách, góc, hình chiếu và không gian con trở thành ngôn ngữ tự nhiên để nói về dữ liệu.

Tích vô hướng $$\langle u,v\rangle=u^\top v$$ đo mức độ cùng hướng của hai vectơ. Độ tương đồng cosine được dùng trong tìm kiếm và trong các biểu diễn nhúng. Ánh xạ $$x\mapsto Ax$$ có thể xoay, co giãn, làm trượt hoặc chiếu dữ liệu.

**Ý chính.**  
*Học máy biến dữ liệu thô thành vectơ, rồi học một ánh xạ sao cho bài toán trở nên dễ giải về mặt hình học.*

---

## 2. Lớp tuyến tính: viên gạch affine

$$
x \mapsto \sigma(Wx + b),
$$

trong đó $$W$$ là ma trận trọng số, $$b$$ là hệ số dịch, $$\sigma$$ là hàm phi tuyến áp lên từng tọa độ (ReLU, GELU, …).

**Nếu không có** $$\sigma$$, các lớp xếp chồng gộp lại thành một:

$$
W_2(W_1 x+b_1)+b_2=(W_2W_1)x+(W_2b_1+b_2).
$$

**Khi có** $$\sigma$$, độ sâu tạo ra các đặc trưng theo nhiều tầng. Suy luận là một chuỗi phép nhân ma trận xen kẽ các phép phi tuyến rẻ, rất hợp với GPU và TPU. Vì vậy, "bùng nổ phần cứng AI" một phần chính là bùng nổ phần cứng cho đại số tuyến tính.

---

## 3. Độ sâu và biểu diễn

Trong các mạng thị giác, các lớp đầu thường phản ứng với cạnh và kết cấu bề mặt; các lớp sau phản ứng với bộ phận và vật thể. Đây là quan sát thực nghiệm, không có gì huyền bí. Về mặt đại số, mỗi lớp biểu diễn lại kết quả của lớp trước:

$$
h^{(\ell+1)}=\sigma\bigl(W^{(\ell)}h^{(\ell)}+b^{(\ell)}\bigr).
$$

Với bài toán phân loại, lớp cuối thường là tuyến tính (hoặc tuyến tính rồi softmax): điểm số cho các lớp là $$Wh+b$$, và softmax biến các điểm số này thành một vectơ xác suất. Phần tạo ra điểm số là đại số tuyến tính; xác suất chỉ là cách đọc kết quả.

**Định lý xấp xỉ phổ quát** nói rằng một mạng nông nhưng đủ rộng có thể xấp xỉ mọi hàm liên tục trên một tập compact. Trên thực tế, mạng sâu thường có thiên hướng quy nạp (inductive bias) phù hợp hơn và cần ít tham số hơn để đạt cùng độ chính xác. Bản thân đại số tuyến tính không chọn kiến trúc; nó chỉ *thực hiện* kiến trúc bạn đã chọn. Câu hỏi "nên dùng mạng nông và rộng hay sâu và hẹp?" là câu hỏi về thiên hướng quy nạp và về tối ưu, không chỉ về khả năng xấp xỉ trên lý thuyết.

---

## 4. SVD, PCA và cấu trúc hạng thấp

Mọi ma trận thực $$A\in\mathbb{R}^{m\times n}$$ đều có **phân tích giá trị kỳ dị (SVD)**

$$
A=U\Sigma V^\top,
$$

trong đó $$U,V$$ là các ma trận trực giao và các giá trị kỳ dị không âm nằm trên đường chéo của $$\Sigma$$. Bỏ đi các giá trị kỳ dị nhỏ cho ta xấp xỉ hạng thấp tốt nhất theo chuẩn Frobenius (và theo chuẩn phổ). Đây là **định lý Eckart–Young**.

**PCA (phân tích thành phần chính)** là phiên bản dành cho dữ liệu: trừ đi giá trị trung bình, rồi tìm các hướng có phương sai lớn nhất bằng SVD hoặc bằng ma trận hiệp phương sai. Nén dữ liệu, khử nhiễu và trực quan hóa khám phá đều dựa trên một ý: *giữ lại các hướng mà dữ liệu biến thiên nhiều nhất, bỏ đi các hướng gần như không biến thiên.*

**Ý chính.**  
*Dữ liệu nhiều chiều thường nằm gần một cấu trúc ít chiều; SVD/PCA tìm ra các trục đó bằng cách giải một bài toán tối ưu có nghiệm cho bởi phổ.*

Trong hệ gợi ý, ma trận người dùng – sản phẩm được xấp xỉ bằng $$UV^\top$$; lọc cộng tác thực chất là đại số tuyến tính. Biểu diễn nhúng của từ và các mô hình chủ đề cũng lặp lại ý tưởng phân tích hạng thấp này. Khi ma trận thưa và rất lớn, người ta dùng các thuật toán SVD ngẫu nhiên hoặc lặp thay cho phân tích đầy đủ, nhưng ý tưởng vẫn vậy: "những chiều quan trọng là những chiều ứng với giá trị kỳ dị lớn".

---

## 5. Gradient: giải tích trên không gian tham số

Huấn luyện là chọn tham số $$\theta$$ (toàn bộ trọng số và hệ số dịch) để cực tiểu hóa hàm mất mát $$L(\theta)$$ lấy trung bình trên dữ liệu, ví dụ entropy chéo (cross-entropy) cho phân loại hay sai số bình phương cho hồi quy. Một bước gradient có dạng:

$$
\theta \leftarrow \theta - \eta \nabla_\theta L(\theta).
$$

Vì $$L$$ là hợp của các phép nhân ma trận và các hàm phi tuyến sơ cấp, **quy tắc dây chuyền** cho phép tính $$\nabla_\theta L$$ qua từng lớp. Đó chính là **lan truyền ngược (backpropagation)**. Không có toán học nào mới ngoài giải tích nhiều biến. Nhưng *đồ thị tính toán* rất lớn, nên các công cụ tự động lấy đạo hàm (auto-diff) đóng vai trò quan trọng.

**Trong thực tế.** Một lô nhỏ (mini-batch) dữ liệu đầu vào là một ma trận; lớp tuyến tính là một phép nhân ma trận (hoặc phép GEMM theo lô). Công cụ auto-diff ghi lại cách mỗi tensor phụ thuộc vào tham số, để một lượt tính ngược cho ra mọi đạo hàm riêng cần thiết. Các vấn đề ổn định số (gradient triệt tiêu hoặc bùng nổ, tính toán với độ chính xác hỗn hợp) vẫn là chuyện đại số tuyến tính và số dấu phẩy động: số điều kiện và thang đo, không có gì bí ẩn.

**Ý chính.**  
*Học là tối ưu một hàm số thực trên một không gian tham số rất nhiều chiều; gradient là phần tuyến tính cục bộ của hàm số đó.*

Xem [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/) (khi nào phương pháp gradient hội tụ, chọn bước nhảy) và [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/) (rủi ro kỳ vọng so với mẫu hữu hạn).

---

## 6. Ánh xạ có cấu trúc: tích chập và attention

Không phải ma trận nào cũng dày đặc và không có cấu trúc.

**Tích chập** (dùng cho ảnh, âm thanh) là một ánh xạ tuyến tính dùng **bộ lọc cục bộ chung**: cùng một nhân (kernel) nhỏ được áp lên mọi vị trí. Viết dưới dạng ma trận, nó có cấu trúc Toeplitz hoặc circulant theo khối. Số tham số ít, và tính đẳng biến với phép tịnh tiến có sẵn trong cấu trúc.

**Self-attention** (trong transformer) trộn các token theo công thức

$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\Bigl(\frac{QK^\top}{\sqrt{d}}\Bigr)V,
$$

trong đó $$Q,K,V$$ là các phép chiếu tuyến tính của đầu vào. Tích $$QK^\top$$ là song tuyến theo dữ liệu; softmax tạo ra các trọng số trộn; nhân với $$V$$ là thêm một tổ hợp tuyến tính nữa. Cơ chế này vẫn chỉ là đại số tuyến tính cộng một phép chuẩn hóa phi tuyến, và nó cho phép mô hình hóa chuỗi ở quy mô lớn mà không cần cấu trúc hồi quy (recurrence) cổ điển.

**Cấu trúc thưa và đồ thị.** Mạng nơ-ron đồ thị (GNN) thay ma trận $$W$$ dày đặc bằng việc truyền thông tin dọc theo các cạnh. Đó là một ánh xạ tuyến tính tôn trọng cấu trúc của mạng, và là cầu nối sang [lý thuyết đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/).

---

## 7. Góc nhìn phổ: ổn định, mode, kernel

Giá trị riêng và vectơ riêng xuất hiện khi động lực học hoặc dạng toàn phương đóng vai trò quan trọng:

- Mạng residual (khi tuyến tính hóa) và mạng hồi quy: lũy thừa $$A^t$$ và bán kính phổ.
- Ma trận Laplace của đồ thị: độ trơn của tín hiệu trên mạng; phân cụm phổ.
- Phương pháp kernel: ma trận Gram $$K_{ij}=k(x_i,x_j)$$; học trong không gian đặc trưng mà không cần viết các đặc trưng ra tường minh.
- Hiệp phương sai của phân phối Gauss: các trục chính của ellipsoid bất định.

Bạn không cần học hết lý thuyết phổ mới dùng được PyTorch. Nhưng khi huấn luyện bị phân kỳ, biểu diễn bị suy biến, hay một mạng đồ thị làm trơn quá mức (oversmoothing), trực giác về phổ là ngôn ngữ để tìm lỗi.

---

## 8. Những gì đại số tuyến tính không giải quyết hết

Đại số tuyến tính là cần, nhưng chưa đủ:

1. **Thống kê và xác suất:** khả năng tổng quát hóa, hiệu chỉnh độ tin cậy, các kết luận nhân quả.  
2. **Tối ưu:** thuật toán, tốc độ học, thiên hướng ngầm của SGD.  
3. **Phần cứng và hệ thống:** cách bố trí bộ nhớ, lượng tử hóa, huấn luyện phân tán.  
4. **Dữ liệu và mục tiêu:** nhãn, phần thưởng, phản hồi của con người; không phép nhân ma trận nào tự "nghĩ ra" giá trị.  
5. **Các hiện tượng phi tuyến:** động lực huấn luyện hỗn loạn, các hành vi đột sinh, ví dụ đối kháng (adversarial).

[Toán của AI (Ch.6)]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) quay lại các giới hạn lý thuyết. Ở đây ta chỉ khẳng định một điều hẹp nhưng chắc chắn: **nền tảng tính toán của học máy hiện đại là đại số tuyến tính, được gắn kết bởi các phép phi tuyến.**

---

## 9. Bức tranh tối giản từ đầu đến cuối

1. Mã hóa đầu vào thành vectơ.  
2. Áp các ánh xạ affine học được cộng phi tuyến (và các biến thể có cấu trúc: tích chập, attention, truyền thông tin trên đồ thị).  
3. Đọc kết quả dự đoán bằng một lớp tuyến tính cuối cùng.  
4. Tính hàm mất mát; lan truyền ngược; cập nhật tham số.  
5. Tùy chọn: nén hoặc phân tích biểu diễn bằng SVD/PCA.

Mọi "sản phẩm AI" dùng mạng nơ-ron để phân loại, xếp hạng, tạo biểu diễn nhúng hay sinh nội dung đều chạy một biến thể của vòng lặp này. Toán học thuần túy về không gian vectơ, đối ngẫu và định lý phổ ra đời trước chip silicon rất lâu; ngành công nghiệp đang dùng những ý tưởng đó ở quy mô khổng lồ.

---

### Đại số tuyến tính làm nền cho học máy (từ phần tìm hiểu video)

Trình tự xem: 3Blue1Brown [mạng nơ-ron](https://www.youtube.com/watch?v=aircAruvnKk) → [gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) → [lan truyền ngược](https://www.youtube.com/watch?v=Ilg3gGewQ5U); thêm bài giảng của Strang [18.06 bài 1](https://www.youtube.com/watch?v=J7DzL2_Na80).

- Một mạng sâu không có phi tuyến vẫn chỉ là một ánh xạ affine $$x\mapsto Wx+b$$.
- Huấn luyện là gradient descent (ngẫu nhiên) trên hàm mất mát; lan truyền ngược giúp tính gradient hiệu quả.
- SVD/PCA là phương pháp tuyến tính cơ sở để nén và khử nhiễu, trước khi dùng đến biểu diễn phi tuyến.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Mạng nơ-ron chỉ là hồi quy tuyến tính." | Mạng có phi tuyến; độ sâu có ý nghĩa chính là nhờ phi tuyến. |
| "PCA là toàn bộ học không giám sát." | PCA là phương pháp tuyến tính cơ sở; các biểu diễn hiện đại là phi tuyến. |
| "Lan truyền ngược là toán học mới." | Đó là quy tắc dây chuyền, tức chế độ đạo hàm ngược (reverse-mode AD), được áp dụng có hệ thống. |
| "Attention không phải đại số tuyến tính." | Phần lõi là tích ma trận cộng softmax. |
| "Biết nhân ma trận là đã hiểu mô hình." | Tính được không có nghĩa là hiểu được ý nghĩa. |

---

## Bài tập

1. Cho $$W=\begin{pmatrix}1&2\\0&1\end{pmatrix}$$, $$x=\begin{pmatrix}1\\1\end{pmatrix}$$: tính $$Wx$$. Phép biến đổi này có tác dụng hình học gì?  
2. Chứng minh hợp của các ánh xạ affine vẫn là ánh xạ affine. Vì sao cần phi tuyến giữa các lớp?  
3. Viết hai câu giải thích vì sao thành phần chính đầu tiên giữ lại được nhiều phương sai nhất.  
4. Với $$L(\theta)=(\theta-3)^2$$ và $$\eta=0.1$$, thực hiện hai bước gradient bắt đầu từ $$0$$.  
5. Viết một câu nối việc GPU nhân ma trận với quá trình suy luận của mạng nơ-ron.  
6. Phép tích chập $$3\times 3$$ có phải là một ánh xạ tuyến tính thưa có cấu trúc không?  
7. Nâng cao: chỉ ra mối liên hệ giữa các vectơ kỳ dị phải của $$X$$ và các vectơ riêng của $$X^\top X$$.

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
- Tự viết lại ý chính của bài trong một đoạn văn, và ghi ra một câu hỏi bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước**: [But what is a neural network? | Deep learning chapter 1](https://www.youtube.com/watch?v=aircAruvnKk) (3Blue1Brown, tiếng Anh). Giới thiệu mạng nơ-ron qua bài toán nhận dạng chữ số viết tay, với các lớp là phép nhân ma trận cộng hệ số dịch. Nên xem trước khi đọc §1 đến §3.
- [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w) (3Blue1Brown, tiếng Anh). Giải thích hàm mất mát và cách mạng học bằng gradient descent. Hợp với §5.
- [Backpropagation, intuitively | Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U) (3Blue1Brown, tiếng Anh). Giải thích trực quan thuật toán lan truyền ngược. Xem sau khi đã đọc §5.
