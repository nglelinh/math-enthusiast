---
layout: post
title: "Bengio, Hinton, LeCun: Nền tảng Deep Learning (Turing 2018)"
chapter: '09'
order: 12
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**Yoshua Bengio**, **Geoffrey Hinton**, và **Yann LeCun** nhận chung **A.M. Turing Award 2018**

> “for conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing.”  
> — [ACM Turing Award](https://amturing.acm.org/)

Giải không trao cho “một app chat”. Nó trao cho **vài thập niên** khăng khăng rằng biểu diễn phân cấp, lan truyền gradient, tích chập, và học không giám sát/tự mã hóa *có thể* trở thành hạ tầng tính toán—khi dữ liệu, GPU, và kỹ thuật huấn luyện đuổi kịp ý tưởng. Bài này tách **cơ chế toán** (lớp, loss, backprop, inductive bias) khỏi hype sản phẩm; đặt trio cạnh [toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/), [Valiant]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/), và [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/).

---

## Mục tiêu học tập

Sau bài, bạn có thể viết một lớp $$x\mapsto \sigma(Wx+b)$$ và mạng như **hợp thành**; giải thích **backpropagation** như quy tắc chuỗi trên đồ thị tính toán; mô tả **CNN** (tích chập, weight sharing, pooling) như inductive bias dịch chuyển/cục bộ; nêu đóng góp văn hóa **Hinton** (Boltzmann/DBN, dropout, capsule-era questions, “dark knowledge”), **LeCun** (conv nets, optical character, self-supervised hiện đại), **Bengio** (representation learning, attention/seq2seq văn hóa Montreal, generative models); phân biệt **thành công thực nghiệm có tái lập** với **định lý tổng quát hóa đã khép**; phê slogan “deep learning giải P vs NP / thay khoa học”.

**Kiến thức nền.** Vector–ma trận; đạo hàm; loss supervised cơ bản. [Đại số tuyến tính–AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/) hữu ích.

---

## 1. Ba sự nghiệp, một thông điệp

Thập niên 1990–2000, mạng nơ-ron không phải trung tâm ML mainstream (SVM, boosting, graphical models chiếm spotlight). Trio—và cộng đồng quanh họ—giữ chương trình **deep architectures**: nhiều lớp phi tuyến để học đặc trưng, không chỉ classify trên feature tay.

Turing 2018 là giải **định hình lĩnh vực** (họ hàng tinh thần Abel “shaping fields”): mentor, paper, hệ thống (ConvNet thực dụng, GPU culture), và từ vựng *representation learning*. Đọc citation: *conceptual and engineering*—cả hai, không chỉ theorem.

---

## 2. Mạng sâu như hợp thành ánh xạ

### Lớp

$$
h^{(\ell)}=\sigma\big(W^{(\ell)} h^{(\ell-1)}+b^{(\ell)}\big),\qquad h^{(0)}=x.
$$

$$\sigma$$ phi tuyến theo tọa độ (ReLU, sigmoid lịch sử, tanh…). Không phi tuyến, chồng lớp tuyến tính sụp một affine. **Độ sâu** đổi lớp hàm biểu diễn hiệu quả—universal approximation nông tồn tại trên compact, nhưng *efficiency* và *optimization path* phụ thuộc sâu và architecture.

### Học = tối ưu tham số

$$
\min_\theta \frac{1}{N}\sum_{i=1}^N \ell\big(f_\theta(x_i),y_i\big)+\Omega(\theta).
$$

SGD / Adam cập nhật $$\theta$$ bằng gradient ước lượng mini-batch. Cảnh quan **không lồi**; lý thuyết hội tụ lồi cổ điển không cover hết—song thực nghiệm scale. Khoảng trống đó là [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/) hiện đại, không phải lỗi “thiếu áp dụng SGD đúng sách 1980”.

### Backprop

Đồ thị tính toán hướng: mỗi nút local Jacobian; reverse-mode AD nhân chuỗi từ loss về tham số—chi phí cùng order forward pass theo số cạnh. Đây là **kỹ thuật đạo hàm tự động**, không phải ma thuật sinh trí tuệ. Hinton và cộng đồng popularize training multi-layer; reverse-mode có lịch sử rộng hơn CS (control, adjoint).

---

## 3. LeCun: tích chập và inductive bias thị giác

### Tích chập

Ảnh có **cục bộ** và **gần tịnh tiến bất biến**. Kernel nhỏ trượt:

$$
(K*X)_{ij}=\sum_{u,v} K_{uv}\, X_{i+u,j+v},
$$

weight sharing giảm tham số so fully connected trên pixel. Pooling / stride giảm phân giải; stack lớp tăng receptive field.

**LeNet** (nhận chữ viết tay) là chứng minh văn hóa sớm: conv + backprop + data thật. Không phải “ImageNet 2012 invent deep learning”; 2012 (AlexNet, Hinton lab) là **scale + GPU + ReLU/dropout** làm community tin.

### Self-supervised và energy-based (văn hóa)

LeCun nhấn học biểu diễn ít nhãn: contrastive, joint embedding, world models—chương trình “machines learn like animals” mang hình lý thuyết thông tin và energy. Math Enthusiast ghi: đây là **agenda**, một phần đã engineering mạnh, một phần còn giả thuyết.

---

## 4. Hinton: từ Boltzmann đến “knowledge”

### Pretraining và DBN

Trước ReLU-era dễ train, **layerwise unsupervised pretraining** (RBM, deep belief nets) giúp deep net khởi động. Dù pipeline hiện đại ít RBM, bài học còn: **khởi tạo và curriculum** quan trọng khi tối ưu khó.

### Dropout, distillation

Dropout như regularizer / xấp xỉ ensemble. **Distillation** (“dark knowledge”): soft labels của net lớn dạy net nhỏ—thông tin không chỉ argmax. Ý tưởng knowledge transfer sống trong compression và teacher–student.

### Attention tới giới hạn

Hinton công khai hoài nghi một số hướng (capsule, “stack more transformers only”)—dù community chọn path khác. Turing vinh danh **đóng góp đã định hình**, không phải mọi bet sau 2018 đều đúng. LO6: laureate ≠ oracle tương lai.

---

## 5. Bengio: representation, sequence, generate

### Representation learning

Bengio formalize và truyền bá: mục tiêu không chỉ minimize train loss mà học **features disentangled / reusable**. Papers survey representation learning là cầu ngôn ngữ giữa neuroscience-inspired và optimization.

### Sequence và attention (hệ sinh thái)

Seq2seq, attention (cộng đồng rộng gồm Bahdanau–Cho–Bengio và song song khác) mở nlp neural trước transformer thống trị. **Generative models** (NADE, GAN-era participation, flow/diffusion neighbors) mở xác suất hóa net.

### Generalization và theory appetite

Bengio hay nối bridge sang causality, System 2-ish reasoning, out-of-distribution—gặp [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/) ở tầm agenda, chưa phải “đã giải”.

---

## 6. Toán còn thiếu gì sau Turing 2018

Danh sách trung thực (không bi quan):

1. **Optimization:** khi nào SGD tìm global-ish useful minimizer trong overparam regime?  
2. **Generalization:** chặn VC-style rỗng; cần bias thuật toán + data structure.  
3. **Robustness:** adversarial examples; shift.  
4. **Sample efficiency** so sinh học.  
5. **Suy luận / compositionality** bền ngoài pattern matching.  
6. **Foundation models:** scaling laws thực nghiệm vs lý thuyết capacity.

[Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) và [high-d geometry]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/) cung cấp dụng cụ; không đóng danh sách.

### Double descent và interpolation

Net rộng có thể fit nhiễu và vẫn predict tốt trên data có cấu trúc. Folklore U-shape capacity không đủ. Đây là *hiện tượng* có mô hình proxy (linear regression ridgeless, random features)—chưa phải định lý cho mọi transformer.

### Residual, normalization, và “trainability engineering”

ResNet viết lớp như $$x\mapsto x+f_\theta(x)$$: gradient có đường tắt, chiều sâu lớn trở nên *huấn luyện được*. Batch/layer normalization chỉnh scale activation; learning-rate schedule và init (He/Xavier văn hóa) là một nửa thực dụng của “deep learning works”. Math Enthusiast nên tách: đây là **thiết kế hệ động lực rời rạc** (iteration map ổn định), không chỉ “thêm layer cho vui”. Phân tích continuous-time (gradient flow, neural ODE) là cầu [hệ động lực / PDE-ish thinking]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/)—hữu ích, chưa thay thế ablation thực nghiệm.

### Attention như song tuyến + softmax

Self-attention (dạng schematic) lấy query/key/value tuyến tính từ token, chấm

$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\Big(\frac{QK^\top}{\sqrt{d}}\Big)V
$$

và trộn thông tin toàn cục trong một lớp. Inductive bias khác CNN: không locality cứng trên lưới ảnh, bù bằng data và positional encoding. Transformer thống trị NLP/vision pipelines sau 2017; di sản seq2seq+attention của hệ sinh thái Bengio vẫn là tiền sử khái niệm. Điểm khóa học: **mọi “architecture revolution” là chọn class hàm + parameter tying**, rồi giao cho SGD và data.

---

## 7. Deep learning và complexity / crypto / systems

- **Không** sụp [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): heuristic trên instance ≠ thuật toán worst-case poly cho NP-đầy đủ.  
- **Privacy / security:** model inversion, data extraction—gặp mật mã ứng dụng và [modern themes]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/).  
- **Systems:** CUDA, compilers, distributed all-reduce là nửa engineering của citation “critical component of computing”.

Turing 2018 ngồi ranh giới **toán rời rạc–xác suất–tối ưu** và **hạ tầng tính toán**—đúng tinh thần chương 09.

---

## 8. Nhầm lẫn thường gặp

| Tuyên bố | Chỉnh |
|----------|--------|
| “Backprop = AI đã hiểu não.” | AD trên graph; não không proven backprop. |
| “CNN chỉ là nhiều filter đẹp.” | Weight sharing + locality = inductive bias toán. |
| “2018 ⇒ lý thuyết DL xong.” | Engineering breakthrough ≠ closed theory. |
| “Scale giải mọi OOD/causal.” | Scale giúp; không thay identify/can thiệp. |
| “Valiant PAC obsolete.” | PAC vẫn đặc tả học; DL thêm architecture/optimization. |
| “Ba người invent neural nets 1940s.” | McCulloch–Pitts, Rosenblatt, Rumelhart et al. là tiền sử; trio định hình *deep* hiện đại. |

---

## 9. Đọc paper DL như Math Enthusiast

Checklist:

1. Kiến trúc: inductive bias gì (conv, attn, residual)?  
2. Loss + data: supervised / self-sup / RL?  
3. Baseline và ablation: gain từ đâu?  
4. Claim lý thuyết hay chỉ table?  
5. Compute: có tái lập được không?  
6. Negative results / failure modes có báo không?

Biết đọc biên giới quan trọng hơn thuộc tên mọi biến thể Adam.

---

## Bài tập

1. Viết forward 2 lớp fully connected + ReLU cho $$x\in\mathbb{R}^d$$.  
2. Giải thích một đoạn vì sao phi tuyến bắt buộc giữa các lớp tuyến tính.  
3. So fully connected trên ảnh $$28\times 28$$ với conv 3×3: tham số scale thế nào (order-of-magnitude)?  
4. Dropout làm gì lúc train vs test (mức khẩu hiệu)?  
5. **≤250 từ:** Turing 2018 vinh danh “conceptual and engineering”—cho mỗi từ một ví dụ từ bài.  
6. Nối [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/): vì sao train loss 0 không bảo đảm risk thấp.  
7. **Seminar:** Chọn abstract arXiv 2024–26 “foundation model theory”; gắn nhãn định lý / scaling law / speculation.

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/deep-learning-trio/`.

**Khẩu hiệu từ gói nghiên cứu**

- Turing 2018: Bengio–Hinton–LeCun — deep learning foundations.

**Thứ tự xem gợi ý**


**Cổng chính thức / tài liệu**

- Hinton Turing: https://amturing.acm.org/award_winners/hinton_4791679.cfm  
- LeCun Turing: https://amturing.acm.org/award_winners/lecun_6017366.cfm  
- Bengio Turing: https://amturing.acm.org/award_winners/bengio_3406375.cfm  
- Valiant PAC (learning theory ancestor): https://amturing.acm.org/award_winners/valiant_2612174.cfm  

Danh mục URL đầy đủ: `research/video-research/deep-learning-trio/references.md`.

## Tài liệu tham khảo


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/deep-learning-trio/references.md`.

1. Hinton Turing — https://amturing.acm.org/award_winners/hinton_4791679.cfm  
2. LeCun Turing — https://amturing.acm.org/award_winners/lecun_6017366.cfm  
3. Bengio Turing — https://amturing.acm.org/award_winners/bengio_3406375.cfm  
4. ACM 2018 Turing announcement — https://awards.acm.org/about/2018-turing  
5. Wikipedia — Deep learning — https://en.wikipedia.org/wiki/Deep_learning  
6. Wikipedia — Backpropagation — https://en.wikipedia.org/wiki/Backpropagation  
7. Wikipedia — Convolutional neural network — https://en.wikipedia.org/wiki/Convolutional_neural_network  
8. Valiant PAC (learning theory ancestor) — https://amturing.acm.org/award_winners/valiant_2612174.cfm  
9. Course cross: Ch.6 Math of AI — contents/en/chapter06/  
10. Thư mục gói: `research/video-research/deep-learning-trio/`.

1. ACM Turing Award — Bengio, Hinton, LeCun (2018).  
2. Goodfellow, Bengio, Courville — *Deep Learning* (MIT).  
3. LeCun, Bengio, Hinton — “Deep learning” (*Nature* 2015) survey.  
4. Historical: LeNet; AlexNet; papers DBN/dropout/attention seq2seq.  
5. Khóa: [toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/); [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/); [linear algebra AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/); [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/); [Valiant]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/).

---

## Hướng đi tiếp

- Hardness & randomness: [Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/).  
- Nhân quả OOD: [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/).  
- Thực hành: train CNN nhỏ MNIST; ablation bỏ conv → FC; quan sát param và accuracy.  
- Đọc: Nature 2015 survey → một chapter Goodfellow → một paper self-supervised.  
- Tiếp: [Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/).
