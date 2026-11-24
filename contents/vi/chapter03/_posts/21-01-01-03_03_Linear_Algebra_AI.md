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

Khi bạn gõ một câu hỏi vào một mô hình ngôn ngữ lớn và nhận lại câu trả lời trôi chảy sau một giây, bên trong hàng nghìn con chip GPU đang nóng lên kia thực chất đang diễn ra chuyện gì? Máy tính không "hiểu tiếng Việt" hay "suy nghĩ bằng hình ảnh" theo cách con người tưởng tượng. Thứ duy nhất nó thực hiện hàng nghìn tỷ lần mỗi giây là **nhân các bảng số khổng lồ với nhau**, cộng thêm một số dịch, bẻ cong nhẹ bằng một hàm phi tuyến đơn giản, rồi lặp đi lặp lại.

Từ hệ thống gợi ý phim trên Netflix, nhận diện khuôn mặt trên điện thoại cho đến các mô hình Transformer hàng trăm tỷ tham số, tất cả đều nói chung một thứ ngôn ngữ cổ điển đã có từ thế kỷ XIX: **vectơ, ma trận và ánh xạ tuyến tính**.

Bài học này không dừng ở câu khẩu hiệu "AI dùng nhiều toán". Chúng ta sẽ đi thẳng vào từng bánh răng để thấy rõ *chính xác phép toán đại số tuyến tính nào* đứng sau việc biểu diễn dữ liệu, nén thông tin, huấn luyện và suy luận của trí tuệ nhân tạo hiện đại.

**Lộ trình:** bản đồ ngành đại số tuyến tính → dữ liệu nhìn như hình học → lớp tuyến tính và vai trò của phi tuyến → độ sâu và biểu diễn → SVD/PCA → gradient trên không gian tham số → tích chập và attention → góc nhìn phổ → những giới hạn và nhầm lẫn thường gặp.

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

## Bản đồ kiến thức nền: Đại số tuyến tính là gì và nghiên cứu những gì?

Ở năm nhất đại học, nhiều sinh viên học đại số tuyến tính như một môn "tính định thức và giải hệ phương trình bằng khử Gauss" rồi quên sạch sau kỳ thi. Thực chất, **đại số tuyến tính (linear algebra)** là ngành toán học nghiên cứu **hình học của các không gian nhiều chiều** và **các phép biến đổi giữ nguyên cấu trúc đường thẳng** (ánh xạ tuyến tính).

Ngành này xoay quanh bốn trụ cột lớn gắn chặt với thực tế:

1. **Không gian vectơ & Hệ tọa độ:** biến mọi đối tượng phức tạp (ảnh, âm thanh, câu văn, hồ sơ người dùng) thành một điểm trong không gian $$\mathbb{R}^d$$ để có thể cộng, nhân tỉ lệ và đo khoảng cách.
2. **Ma trận như một phép biến đổi hình học:** thay vì xem ma trận $$W$$ là một bảng số tĩnh, hãy xem nó là một cỗ máy *xoay, kéo giãn, chiếu hoặc gập* cả không gian dữ liệu sang một không gian mới nơi dữ liệu dễ phân tách hơn.
3. **Tích vô hướng & Trực giao:** cung cấp khái niệm *góc* và *độ giống nhau* trong không gian hàng nghìn chiều — nền tảng của tìm kiếm ngữ nghĩa (vector search), cơ chế attention và phép chiếu bình phương tối thiểu.
4. **Phân tích ma trận (Giá trị riêng, SVD):** tìm ra những "trục xương sống" quan trọng nhất của một phép biến đổi hoặc một bảng dữ liệu khổng lồ, cho phép nén dữ liệu, khử nhiễu và chẩn đoán sự ổn định của hệ thống.

Nói ngắn gọn: **máy tính chỉ giỏi cộng và nhân song song trên mảng số.** Đại số tuyến tính là cây cầu biến thế giới hỗn độn của ảnh, chữ và hành vi thành những phép biến đổi hình học mà GPU có thể chạy với tốc độ ánh sáng.

---

## 1. Nhìn dữ liệu như hình học

Một ảnh xám nhỏ kích thước $$28\times 28$$ điểm ảnh thực chất là một vectơ trong $$\mathbb{R}^{784}$$. Biểu diễn nhúng (embedding) của một câu văn trong mô hình ngôn ngữ là một vectơ trong $$\mathbb{R}^{1536}$$ hay $$\mathbb{R}^{4096}$$. Cả một lô gồm $$n$$ mẫu, mỗi mẫu có $$d$$ đặc trưng, xếp thành một ma trận $$X\in\mathbb{R}^{n\times d}$$. Khi mọi thứ trở thành điểm trong không gian, khoảng cách, góc, hình chiếu và siêu phẳng lập tức trở thành ngôn ngữ tự nhiên để phân loại và tìm kiếm.

Tích vô hướng $$\langle u,v\rangle=u^\top v$$ và độ tương đồng cosine $$\cos\theta = \frac{u^\top v}{\|u\|\,\|v\|}$$ đo mức độ "cùng hướng" của hai vectơ.

**Ví dụ số trực quan.** Giả sử ta biểu diễn gu xem phim bằng 3 trục `[hành động, tình cảm, khoa học viễn tưởng]`:
- Người dùng A: $$u = (5, 1, 4)$$
- Phim 1: $$v_1 = (4, 0, 5)$$ → $$u^\top v_1 = 20 + 0 + 20 = 40$$, $$\cos\theta \approx 0{,}97$$ (gần như trùng hướng → gợi ý ngay!).
- Phim 2: $$v_2 = (0, 5, 1)$$ → $$u^\top v_2 = 0 + 5 + 4 = 9$$, $$\cos\theta \approx 0{,}27$$ (gần như vuông góc → không hợp gu).

Ánh xạ $$x\mapsto Ax$$ có thể xoay, co giãn, làm trượt hoặc chiếu cả đám mây dữ liệu để các nhóm giống nhau xích lại gần nhau hơn.

**Ý chính.**  
*Học máy biến dữ liệu thô thành vectơ, rồi học một chuỗi biến đổi hình học sao cho bài toán phân loại hay dự đoán trở nên dễ giải chỉ bằng một lát cắt phẳng.*

---

## 2. Lớp tuyến tính: viên gạch affine

Viên gạch cơ bản nhất của mọi mạng nơ-ron có dạng:

$$
x \mapsto \sigma(Wx + b),
$$

trong đó $$W$$ là ma trận trọng số, $$b$$ là vectơ hệ số dịch (bias), còn $$\sigma$$ là hàm phi tuyến áp lên từng tọa độ (phổ biến nhất là $$\mathrm{ReLU}(z)=\max(0,z)$$ hoặc GELU).

**Vì sao bắt buộc phải có $$\sigma$$?** Nếu bỏ $$\sigma$$ đi, bạn có xếp chồng 100 lớp lên nhau thì toàn bộ mạng vẫn sụp đổ thành **một lớp duy nhất**:

$$
W_2(W_1 x+b_1)+b_2=(W_2W_1)x+(W_2b_1+b_2).
$$

**Trực giác hình học.** Phép biến đổi affine $$Wx+b$$ chỉ có thể xoay, kéo giãn và tịnh tiến không gian — một đường thẳng vẫn mãi là đường thẳng, nên bạn không bao giờ tách nổi hai cụm dữ liệu lồng vào nhau (như hai vòng tròn đồng tâm). Khi chèn hàm $$\mathrm{ReLU}$$ vào giữa, không gian bị **gấp lại** dọc theo các siêu phẳng (tất cả phần âm bị ép về 0). Xếp nhiều lớp nối tiếp giống như nghệ thuật gấp giấy Origami: gấp không gian nhiều lần rồi cắt một nhát thẳng duy nhất ở lớp cuối, bạn có thể tách được những hình dạng phức tạp tùy ý!

Về mặt phần cứng, quá trình suy luận chỉ là chuỗi phép nhân ma trận xen kẽ các phép phi tuyến cực rẻ, khớp hoàn hảo với kiến trúc song song của GPU và TPU. Vì vậy, "cuộc chạy đua chip AI" về bản chất chính là cuộc chạy đua phần cứng cho phép nhân ma trận.

### Khung giải thích: Vì sao nhân ma trận + ReLU lại tạo ra khả năng phân loại phức tạp? (nên đọc chậm)

1. **Nhúng dữ liệu vào không gian vectơ:** ảnh, âm thanh hay câu chữ được chuyển thành các điểm $$x \in \mathbb{R}^d$$; lúc đầu hai lớp dữ liệu (ví dụ ảnh mèo và ảnh chó) xoắn chặt vào nhau nên không có mặt phẳng nào cắt tách chúng ra được.
2. **Biến đổi affine + gấp không gian từng lớp:** mỗi lớp $$h^{(\ell+1)} = \mathrm{ReLU}(W^{(\ell)}h^{(\ell)}+b^{(\ell)})$$ xoay, kéo giãn rồi gấp nhẹ không gian dữ liệu. Qua $$L$$ lớp, số mảnh gấp tuyến tính tăng theo cấp số mũ theo độ sâu $$L$$.
3. **Tách phẳng ở lớp cuối cùng:** mục tiêu của toàn bộ các lớp ẩn chỉ là *gỡ rối* đám mây dữ liệu sao cho đến lớp cuối cùng, mèo nằm hẳn một bên và chó nằm hẳn bên kia của một siêu phẳng $$w^\top h + b = 0$$.
4. **Cập nhật ma trận bằng đạo hàm:** sai số dự đoán được truyền ngược về từng phần tử của ma trận $$W^{(\ell)}$$ nhờ quy tắc dây chuyền để tinh chỉnh góc xoay và nếp gấp tốt hơn sau mỗi lô dữ liệu.

**Kiểm tra nhanh.** Một mạng sâu không "học luật bằng chữ"; nó đang học một **chuỗi phép biến dạng hình học** trong không gian nhiều chiều sao cho dữ liệu trở nên tách tuyến tính được ở đầu ra.

---

## 3. Độ sâu và biểu diễn

Trong các mạng thị giác máy tính, các lớp đầu thường học cách phản ứng với cạnh, góc và kết cấu bề mặt; các lớp giữa ghép cạnh thành bộ phận (mắt, bánh xe); các lớp sau ghép bộ phận thành cả vật thể. Đây là hệ quả tự nhiên của việc biến đổi không gian qua nhiều tầng, không có gì huyền bí. Về mặt đại số, mỗi lớp viết lại biểu diễn của lớp trước:

$$
h^{(\ell+1)}=\sigma\bigl(W^{(\ell)}h^{(\ell)}+b^{(\ell)}\bigr).
$$

Với bài toán phân loại, lớp cuối cùng thường là tuyến tính rồi qua softmax: điểm số (logit) cho các lớp là $$Wh+b$$, và softmax biến các điểm số này thành một vectơ xác suất dương có tổng bằng 1. Phần tạo ra ranh giới phân tách vẫn là đại số tuyến tính; xác suất chỉ là cách đọc kết quả dễ hiểu cho con người.

**Định lý xấp xỉ phổ quát** nói rằng một mạng nông (chỉ một tầng ẩn) nhưng đủ rộng có thể xấp xỉ mọi hàm liên tục trên một tập đóng bị chặn. Vậy tại sao thực tế người ta vẫn xây mạng sâu hàng chục, hàng trăm tầng? Vì mạng sâu khai thác được **cấu trúc phân cấp** của thế giới thật (pixel → cạnh → bộ phận → vật thể) nên thường cần ít tham số hơn theo cấp số mũ so với mạng nông để đạt cùng độ chính xác. Bản thân đại số tuyến tính không tự chọn kiến trúc; nó là bộ máy *thực thi* thiên hướng quy nạp (inductive bias) mà con người thiết kế.

---

## 4. SVD, PCA và cấu trúc hạng thấp

Mọi ma trận thực $$A\in\mathbb{R}^{m\times n}$$ — dù hình chữ nhật và méo mó đến đâu — đều có **phân tích giá trị kỳ dị (SVD)**:

$$
A=U\Sigma V^\top,
$$

trong đó $$U,V$$ là các ma trận trực giao (chỉ xoay không gian mà không làm biến dạng độ dài) và $$\Sigma$$ là ma trận đường chéo chứa các giá trị kỳ dị không âm $$\sigma_1 \ge \sigma_2 \ge \dots \ge 0$$. Bạn có thể đọc SVD như một câu chuyện hình học ba bước: *xoay* bằng $$V^\top$$ → *kéo giãn dọc các trục* theo $$\sigma_i$$ → *xoay tiếp* bằng $$U$$.

Nếu chỉ giữ lại $$k$$ giá trị kỳ dị lớn nhất và bỏ phần đuôi nhỏ, ta thu được xấp xỉ hạng $$k$$ tốt nhất có thể theo chuẩn Frobenius (và chuẩn phổ) — đó là **định lý Eckart–Young**.

**Ví dụ số về sức mạnh nén của SVD.** Một bức ảnh xám độ phân giải $$1000 \times 1000$$ cần lưu $$1{.}000{.}000$$ con số. Nếu ta dùng SVD và chỉ giữ lại $$k=50$$ thành phần kỳ dị lớn nhất, ta chỉ cần lưu $$50$$ cột của $$U$$, $$50$$ cột của $$V$$ và $$50$$ giá trị $$\sigma_i$$ — tổng cộng $$50 \times (1000 + 1000 + 1) = 100{.}050$$ con số, **giảm dung lượng tới 90%** mà mắt thường gần như không thấy khác biệt!

**PCA (phân tích thành phần chính)** chính là ứng dụng của SVD vào bảng dữ liệu đã trừ trung bình: tìm các hướng trực giao mà dữ liệu biến thiên mạnh nhất. Trong hệ gợi ý phim (như bài toán Netflix Prize), ma trận đánh giá người dùng – phim khổng lồ được xấp xỉ bằng tích hạng thấp $$UV^\top$$ (mỗi người dùng và mỗi phim chỉ cần một vectơ 20–50 "sở thích ẩn"). Ngay cả kỹ thuật tinh chỉnh LLM hiện đại như **LoRA** cũng dựa trực tiếp vào ý tưởng cập nhật trọng số bằng ma trận hạng thấp $$\Delta W = AB$$ để tiết kiệm bộ nhớ GPU!

**Ý chính.**  
*Dữ liệu nhiều chiều ngoài đời thật hiếm khi lấp đầy cả không gian; nó thường nằm sát một cấu trúc ít chiều, và SVD/PCA tìm ra đúng các trục xương sống đó.*

---

## 5. Gradient: giải tích trên không gian tham số

Huấn luyện một mô hình AI là bài toán tìm bộ tham số $$\theta$$ (toàn bộ các ma trận trọng số $$W$$ và vectơ $$b$$) sao cho hàm mất mát $$L(\theta)$$ nhỏ nhất trên dữ liệu. Mỗi bước cập nhật có dạng:

$$
\theta \leftarrow \theta - \eta \nabla_\theta L(\theta).
$$

Vì $$L$$ là hàm hợp của các phép nhân ma trận và các hàm phi tuyến đơn giản, **quy tắc dây chuyền (chain rule)** cho phép tính đạo hàm ngược từ lớp cuối về lớp đầu — đó chính là **lan truyền ngược (backpropagation)**.

**Ví dụ cầm tay chỉ việc 1 (Lan truyền ngược trên mạng 2 lớp).** Giả sử mạng có dạng $$y = w_2 \cdot \mathrm{ReLU}(w_1 x)$$ với đầu vào $$x=2$$, nhãn đúng $$y^*=10$$, trọng số khởi tạo $$w_1=1, w_2=3$$, và sai số $$L = \frac{1}{2}(y - y^*)^2$$:
- **Lượt đi xuôi (forward):** $$h = \mathrm{ReLU}(1\cdot 2)=2$$, dự đoán $$y = 3\cdot 2 = 6$$, mất mát $$L = \frac{1}{2}(6-10)^2 = 8$$.
- **Lượt đi ngược (backward):** $$\frac{\partial L}{\partial y} = y - y^* = -4$$. Theo quy tắc dây chuyền:
  - $$\frac{\partial L}{\partial w_2} = \frac{\partial L}{\partial y}\cdot h = (-4)\cdot 2 = -8$$.
  - $$\frac{\partial L}{\partial w_1} = \frac{\partial L}{\partial y}\cdot w_2 \cdot x = (-4)\cdot 3 \cdot 2 = -24$$.
- Với tốc độ học $$\eta=0{,}1$$, ta đẩy $$w_2 \leftarrow 3 - 0{,}1(-8)=3{,}8$$ và $$w_1 \leftarrow 1 - 0{,}1(-24)=3{,}4$$ — cả hai trọng số đều tăng lên để kéo dự đoán tiến sát về $$10$$!

Không có phép toán nào mới ngoài giải tích nhiều biến và nhân ma trận. Nhưng *đồ thị tính toán* có hàng tỷ nút, nên các công cụ tự động lấy đạo hàm (auto-diff như PyTorch, JAX) mới trở thành xương sống kỹ thuật. Các lỗi quen thuộc khi huấn luyện (gradient triệt tiêu, gradient bùng nổ, tràn số khi dùng độ chính xác FP16/BF16) thực chất đều là bài toán số điều kiện và thang đo trong đại số tuyến tính số.

**Ý chính.**  
*Học là tối ưu một hàm số thực trên không gian tham số khổng lồ; gradient là xấp xỉ tuyến tính cục bộ chỉ đường xuống dốc.*

Xem [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/) (khi nào phương pháp gradient hội tụ, chọn bước nhảy) và [Xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/) (rủi ro kỳ vọng so với mẫu hữu hạn).

---

## 6. Ánh xạ có cấu trúc: tích chập và attention

Nếu nối đầy đủ mọi điểm ảnh của một bức ảnh HD với lớp tiếp theo, ma trận $$W$$ sẽ phình to đến hàng nghìn tỷ tham số và lập tức quá khớp. Vì thế các kiến trúc AI hiện đại dùng những **ma trận tuyến tính có cấu trúc đặc biệt**:

**Tích chập (convolution)** dùng cho ảnh và âm thanh là một ánh xạ tuyến tính dùng **bộ lọc cục bộ dùng chung**: cùng một nhân (kernel) nhỏ $$3\times 3$$ trượt qua mọi vị trí của ảnh. Viết dưới dạng ma trận khổng lồ, nó là một ma trận rất thưa có cấu trúc Toeplitz theo khối (các đường chéo lặp lại giống hệt nhau). Nhờ đó số tham số giảm hàng triệu lần, và mô hình tự động có tính đẳng biến với phép tịnh tiến: một con mèo ở góc trái hay góc phải đều được nhận diện bằng cùng một bộ lọc.

**Self-attention** (trái tim của kiến trúc Transformer đứng sau ChatGPT, Gemini) trộn thông tin giữa các từ (token) trong câu theo công thức:

$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\Bigl(\frac{QK^\top}{\sqrt{d}}\Bigr)V,
$$

trong đó $$Q=XW_Q, K=XW_K, V=XW_V$$ là ba phép chiếu tuyến tính của chuỗi đầu vào.

### Ví dụ cầm tay chỉ việc 2: Tự tay tính một phép Self-Attention với ma trận $$2\times 2$$

Giả sử câu chỉ có 2 từ (2 hàng) với số chiều $$d = 2$$, và sau khi chiếu tuyến tính ta thu được ba ma trận:

$$
Q = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad
K = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}, \qquad
V = \begin{pmatrix} 10 & 0 \\ 0 & 20 \end{pmatrix}.
$$

1. **Tính ma trận điểm ăn khớp $$QK^\top$$:**
$$
QK^\top = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.
$$
2. **Chia cho $$\sqrt{d} = \sqrt{2} \approx 1{,}414$$** (giữ phương sai ổn định để softmax không bị bão hòa):
$$
\frac{QK^\top}{\sqrt{2}} \approx \begin{pmatrix} 0{,}71 & 0{,}71 \\ 0 & 0{,}71 \end{pmatrix}.
$$
3. **Áp $$\mathrm{softmax}$$ lên từng hàng** (dùng $$e^{0{,}71}\approx 2{,}03,\ e^0 = 1$$):
   - Hàng 1: $$\left(\frac{2{,}03}{2{,}03+2{,}03},\ \frac{2{,}03}{2{,}03+2{,}03}\right) = (0{,}50,\ 0{,}50)$$.
   - Hàng 2: $$\left(\frac{1}{1+2{,}03},\ \frac{2{,}03}{1+2{,}03}\right) \approx (0{,}33,\ 0{,}67)$$.
4. **Nhân ma trận trọng số với $$V$$ để trộn thông tin:**
$$
\mathrm{Attention}(Q,K,V) \approx \begin{pmatrix} 0{,}50 & 0{,}50 \\ 0{,}33 & 0{,}67 \end{pmatrix}\begin{pmatrix} 10 & 0 \\ 0 & 20 \end{pmatrix} = \begin{pmatrix} 5{,}0 & 10{,}0 \\ 3{,}3 & 13{,}4 \end{pmatrix}.
$$

Nhìn kết quả ta thấy ngay cơ chế: token 1 chia đều sự chú ý 50%–50% cho cả hai từ, còn token 2 chú ý 67% vào nội dung của chính nó và chỉ lấy 33% từ token 1. Toàn bộ đột phá Transformer vẫn chỉ là **ba phép chiếu tuyến tính, hai phép nhân ma trận và một hàm softmax**.

**Cấu trúc thưa và đồ thị.** Mạng nơ-ron đồ thị (GNN) thay ma trận $$W$$ dày đặc bằng việc truyền thông điệp dọc theo các cạnh của đồ thị (tương đương nhân với ma trận kề chuẩn hóa). Đó là cầu nối trực tiếp sang [lý thuyết đồ thị]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/).

---

## 7. Góc nhìn phổ: ổn định, mode, kernel

Giá trị riêng và vectơ riêng xuất hiện ngay lập tức mỗi khi một phép biến đổi được lặp lại nhiều lần hoặc khi ta phân tích độ cong:

- **Mạng residual và mạng hồi quy (RNN):** lặp lại phép nhân ma trận $$t$$ lần cho ra lũy thừa $$A^t$$. Nếu giá trị riêng lớn nhất (bán kính phổ) lớn hơn 1, tín hiệu nổ tung theo hàm mũ; nếu nhỏ hơn 1, tín hiệu tắt lịm về 0.
- **Ma trận Laplace của đồ thị:** các vectơ riêng ứng với giá trị riêng nhỏ nhất cho thấy cách chia mạng lưới thành các cộng đồng tự nhiên (phân cụm phổ).
- **Phương pháp kernel (SVM, Gaussian Process):** ma trận Gram $$K_{ij}=k(x_i,x_j)$$ nửa xác định dương cho phép tính tích vô hướng trong không gian đặc trưng vô hạn chiều mà không cần viết tọa độ ra tường minh.
- **Ma trận hiệp phương sai:** các vectơ riêng chỉ các trục chính của đám mây dữ liệu, còn giá trị riêng cho biết độ rộng của đám mây dọc theo từng trục.

Bạn không cần thuộc hết lý thuyết phổ mới viết được mã PyTorch. Nhưng khi quá trình huấn luyện bỗng dưng ra `NaN`, khi biểu diễn bị sụp đổ về một điểm (representation collapse), hay khi mạng đồ thị làm mờ hết khác biệt giữa các nút (oversmoothing), trực giác về phổ chính là ống nghe của bác sĩ để chẩn đoán đúng bệnh.

---

## 8. Những gì đại số tuyến tính không giải quyết hết

Đại số tuyến tính là điều kiện cần, nhưng chưa đủ để tạo nên một hệ thống AI đáng tin cậy:

1. **Thống kê và xác suất:** khả năng tổng quát hóa sang dữ liệu mới, hiệu chỉnh độ tin cậy, phân biệt tương quan và nhân quả.  
2. **Tối ưu hóa:** chọn thuật toán (SGD, Adam), lịch tốc độ học, hiểu thiên hướng ngầm giúp mô hình không bị quá khớp.  
3. **Phần cứng và hệ thống:** cách bố trí bộ nhớ đệm GPU, lượng tử hóa (quantization), huấn luyện phân tán trên hàng nghìn máy.  
4. **Dữ liệu và mục tiêu:** chất lượng nhãn, hàm phần thưởng, phản hồi và giá trị của con người; không phép nhân ma trận nào tự sinh ra mục đích đúng đắn.  
5. **Các hiện tượng phi tuyến:** động lực huấn luyện hỗn loạn, các năng lực đột sinh ở quy mô lớn, và lỗ hổng trước ví dụ đối kháng (adversarial examples).

[Toán của AI (Ch.6)]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) quay lại các giới hạn lý thuyết. Ở đây ta khẳng định một điều hẹp nhưng chắc chắn: **nền tảng tính toán của học máy hiện đại là đại số tuyến tính, được gắn kết bởi các phép phi tuyến.**

---

## 9. Bức tranh tối giản từ đầu đến cuối

1. Mã hóa đầu vào (ảnh, văn bản, âm thanh) thành vectơ.  
2. Áp chuỗi ánh xạ affine học được xen kẽ hàm phi tuyến (hoặc các biến thể có cấu trúc: tích chập, attention, truyền thông tin trên đồ thị).  
3. Đọc kết quả dự đoán bằng một lớp tuyến tính cuối cùng.  
4. Tính hàm mất mát; lan truyền ngược để lấy gradient; cập nhật tham số.  
5. Tùy chọn: nén, tinh chỉnh hoặc phân tích biểu diễn bằng SVD/PCA và xấp xỉ hạng thấp.

Mọi "sản phẩm AI" dùng mạng nơ-ron để phân loại, xếp hạng, tạo biểu diễn nhúng hay sinh nội dung đều chạy một biến thể của vòng lặp năm bước này. Toán học thuần túy về không gian vectơ, đối ngẫu và định lý phổ ra đời trước chip silicon hơn một thế kỷ; ngành công nghiệp ngày nay đang khai thác chính những ý tưởng đó ở quy mô khổng lồ.

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
