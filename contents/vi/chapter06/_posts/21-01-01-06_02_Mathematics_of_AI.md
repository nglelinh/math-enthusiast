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

Bạn gõ một câu hỏi bất kỳ vào khung trò chuyện, và chưa đầy một giây sau, một mô hình ngôn ngữ lớn trả về câu trả lời mạch lạc. Đằng sau khoảnh khắc tưởng chừng nhẹ tênh đó là một cỗ máy toán học khổng lồ đang vận hành: từng chữ được biến thành vector hàng nghìn chiều, đi qua hàng chục lớp ma trận với hàng tỷ tham số, và toàn bộ "trí nhớ" của mô hình được khắc vào các con số ấy thông qua một cuộc leo dốc ngược khổng lồ trên mặt mất mát không ai vẽ nổi.

Điều trớ trêu thú vị của trí tuệ nhân tạo hiện đại là **kỹ thuật đang chạy nhanh hơn lý thuyết**. Giống như anh em nhà Wright đã cho máy bay cất cánh trước khi con người giải quyết trọn vẹn khí động lực học phi tuyến, học sâu (deep learning) đang hoạt động cực kỳ ấn tượng trong khi nhiều câu hỏi toán học cốt lõi — vì sao nó học được, vì sao nó không học vẹt dù thừa mứa tham số — vẫn đang bỏ ngỏ. Hệ thống AI ngày nay vừa là một sản phẩm kỹ thuật, vừa là một **đối tượng toán học** đầy bí ẩn.

Bài này không giả vờ rằng lĩnh vực đã "đóng sổ". Thay vào đó, ta sẽ mở nắp ca-pô để nhìn thấy bản đồ toán học nằm dưới học sâu, đồng thời rèn kỹ năng **đọc ở vùng biên**: biết tách bạch đâu là định lý, đâu là quy luật thực nghiệm, đâu là kinh nghiệm gần đúng (*heuristic*) và đâu chỉ là lời quảng cáo.

---

## Kiến thức cần nhớ: Toán học của AI là gì và nghiên cứu những gì?

Nếu bạn từng học đại số tuyến tính, giải tích nhiều biến và xác suất thống kê ở đại học, bạn đã nắm trong tay đúng ba viên gạch nền của toán học AI. Ngành **Toán học của AI** (Mathematics of AI / Mathematical Foundations of Deep Learning) không phải một nhánh toán tách biệt, mà là nơi bốn câu hỏi lớn giao nhau:

1. **Biểu diễn (Representation — Đại số tuyến tính & Lý thuyết xấp xỉ):** Làm thế nào biểu diễn ảnh, âm thanh, văn bản thành vector trong $$\mathbb{R}^d$$, và một mạng nơ-ron nhiều lớp có thể biểu diễn được những hàm số phức tạp đến mức nào?
2. **Tối ưu hóa (Optimization — Giải tích & Hệ động lực):** Hàm mất mát của mạng sâu có hàng tỷ biến và vô số thung lũng lồi lõm (không lồi). Tại sao một thuật toán tưởng chừng đơn giản như trượt theo độ dốc ngẫu nhiên (SGD) lại không bị mắc kẹt ở những điểm cực tiểu vô dụng?
3. **Tổng quát hóa (Generalization — Xác suất & Thống kê chiều cao):** Một mô hình có nhiều tham số hơn cả số mẫu dữ liệu vẫn dự đoán tốt trên dữ liệu chưa từng thấy. Quy luật xác suất và hình học nào đang âm thầm ngăn nó "học thuộc lòng"?
4. **Độ tin cậy và cấu trúc (Reliability & Structure — Hình học, Thông tin, Nhân quả):** Điều gì làm nên biên quyết định mong manh trước nhiễu đối kháng, và mô hình học được mối liên hệ nhân quả hay chỉ là tương quan thống kê?

Nói một cách hình ảnh: đại số tuyến tính là **ngôn ngữ** để viết ra mô hình, giải tích và tối ưu là **động cơ** giúp mô hình học, còn xác suất và hình học chiều cao là **kính hiển vi** giúp ta hiểu vì sao mô hình hoạt động được ngoài thế giới thật.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Mô tả mạng nơ-ron cơ bản như một chuỗi ghép các ánh xạ tuyến tính và phi tuyến, và viết được một lớp $$x\mapsto\sigma(Wx+b)$$.
- Giải thích huấn luyện là việc cực tiểu hóa hàm mất mát bằng phương pháp số; gradient và backpropagation chính là quy tắc chuỗi được tổ chức lại cho gọn.
- Phân biệt **rủi ro thực nghiệm** (mức khớp trên tập huấn luyện) với **rủi ro thật** (kỳ vọng trên dữ liệu mới).
- Kể ít nhất bốn lĩnh vực toán học đứng sau ML, mỗi lĩnh vực kèm một câu nói nó tham gia *như thế nào*.
- Nêu ba **câu hỏi toán còn mở** về học sâu (không phải tính năng sản phẩm).
- Nhận xét một tuyên bố phổ thông về AI theo tiêu chí chính xác hay thổi phồng.
- Hiểu các lưu ý của Tao trong buổi nói chuyện Big Think: các “mode” khoa học kế tiếp nhau, ẩn dụ trực thăng và đi bộ, **chiều sâu** của con người so với **chiều rộng** của mô hình, và vấn đề **tiêu hóa chứng minh**. Chúng chỉ là lời bàn, không phải định lý.

**Kiến thức nền.** Vector và ma trận; đạo hàm như tốc độ biến thiên cục bộ; ngôn ngữ xác suất cơ bản.

---

## 1. Dữ liệu sống trong không gian nhiều chiều

Một ảnh xám cỡ $$28\times 28$$ là một vector trong $$\mathbb{R}^{784}$$. Một khung hình video màu, một embedding của token, hay một hồ sơ biểu hiện gen cũng là vector, trong những không gian còn nhiều chiều hơn. Bộ dữ liệu là một đám mây điểm, còn một batch là một ma trận. **Đại số tuyến tính** vì thế là ngôn ngữ tự nhiên ở đây: cơ sở, phép chiếu, giá trị suy biến, cấu trúc hạng thấp, ánh xạ tuyến tính.

**Một ví dụ cụ thể.** Phân tích thành phần chính (PCA) và phân tích giá trị suy biến (SVD) tìm những hướng có phương sai lớn nhất, để nén dữ liệu hoặc khử nhiễu bằng cách chiếu lên không gian con chính. Nếu $$X$$ là ma trận dữ liệu thì các vector suy biến phải đứng đầu của phiên bản đã được trừ trung bình chính là các hướng chính. Chẳng hạn, với tập ảnh chữ số viết tay trong $$\mathbb{R}^{784}$$, chỉ cần giữ lại khoảng 30–50 hướng chính đầu tiên là bạn đã tái tạo lại hình dáng chữ số rất rõ nét — bởi dữ liệu thật không trải đều khắp $$\mathbb{R}^{784}$$, mà thường nằm bám gần một "tờ giấy cong" (đa tạp) có số chiều nội tại thấp hơn nhiều.

Nhiều chiều không đơn giản là “thêm vài tọa độ”. Hiện tượng tập trung của độ đo, tập điển hình và hình học của mặt cầu nhiều chiều làm thay đổi trực giác về khoảng cách và góc: phần lớn thể tích của quả cầu nhiều chiều nằm trong một lớp vỏ mỏng gần bề mặt và gần xích đạo, còn hai vector ngẫu nhiên độc lập trong $$\mathbb{R}^{1000}$$ gần như vuông góc nhau với xác suất rất cao. Những điều này giúp giải thích vì sao các mô hình quá tham số vẫn chạy được và vì sao phương pháp láng giềng gần nhất “ngây thơ” dễ sai. (Bài [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/) trong chương này đi sâu hơn.)

---

## 2. Mô hình: hàm được ghép từ những mảnh đơn giản

Một lớp kết nối đầy đủ là một ánh xạ tuyến tính, rồi đến một hàm phi tuyến áp dụng theo từng tọa độ:

$$
x \mapsto \sigma(Wx + b),
$$

trong đó $$W$$ là ma trận trọng số, $$b$$ là bias, $$\sigma$$ là hàm kích hoạt (ReLU, GELU, sigmoid, …). Hãy hình dung bằng hình học: phép biến đổi tuyến tính $$Wx + b$$ chỉ có thể xoay, kéo giãn và dịch chuyển không gian. Chính hàm phi tuyến — chẳng hạn $$\mathrm{ReLU}(z) = \max(0, z)$$ — mới là nhát **gấp không gian** dọc theo các siêu phẳng. Ghép 10 lớp như vậy giống như gấp một tờ giấy liên tiếp 10 lần: từ vài nhát gấp đơn giản, số vùng tuyến tính tăng theo hàm mũ, cho phép mạng uốn nắn ranh giới phân loại cực kỳ phức tạp.

Mạng sâu **ghép** nhiều lớp như vậy với nhiều kiến trúc chuyên biệt. Mạng tích chập (CNN) dùng lại các bộ lọc tuyến tính cục bộ có tính bất biến tịnh tiến — rất khớp với cấu trúc ảnh. Mạng residual viết mỗi lớp thành $$x \mapsto x + f_\theta(x)$$, giúp tín hiệu và gradient đi thẳng qua hàng trăm lớp mà không bị suy hao. Transformer dùng **attention**: một ánh xạ có cấu trúc gồm query, key, value, dạng song tuyến tính, với trọng số chuẩn hóa bằng softmax. Nhờ đó mỗi token được trộn thành một tổ hợp tuyến tính của các token khác, với hệ số phụ thuộc vào chính ngữ cảnh của dữ liệu đầu vào.

**Xấp xỉ phổ quát (định lý và thực hành).** Với giả thiết nhẹ, một mạng nông đủ rộng có thể xấp xỉ một lớp rất rộng các hàm liên tục trên tập compact (định lý xấp xỉ phổ quát cổ điển). Đây là kết quả về **biểu diễn**: nó nói rằng *tồn tại* tham số để xấp xỉ hàm mục tiêu, **chứ không** nói gradient descent tìm ra các tham số đó một cách hiệu quả. Độ sâu làm thay đổi *hiệu quả* biểu diễn và inductive bias. Còn lý thuyết giải thích *vì sao mạng sâu thường thắng mạng rộng trong thực hành* thì tinh tế hơn và vẫn đang được phát triển: lý thuyết xấp xỉ, giải tích điều hòa của phép ghép hàm và quy luật mở rộng quy mô (scaling) thực nghiệm đều góp một phần.

![Pipeline toán dưới ML]({{ site.baseurl }}/img/chapter_img/ai_math_pipeline.svg)

*Hình. Chồng khái niệm từ hình học dữ liệu tới lý thuyết mở (nếu asset có trong khóa).*

---

## 3. Học như một bài toán tối ưu

Huấn luyện là chọn tham số $$\theta$$ để giảm **mất mát** $$L(\theta)$$, đại lượng đo lỗi dự đoán trên dữ liệu (thường cộng thêm một số hạng điều chuẩn hoặc ràng buộc từ kiến trúc). Mẫu chuẩn là cực tiểu hóa rủi ro thực nghiệm:

$$
\hat\theta \in \arg\min_\theta \frac{1}{n}\sum_{i=1}^n \ell\bigl(f_\theta(x_i), y_i\bigr),
$$

với $$\ell$$ là mất mát tại từng điểm (bình phương, cross-entropy, …) và $$f_\theta$$ là mô hình.

**Gradient descent** và các biến thể ngẫu nhiên của nó đẩy tham số ngược hướng với gradient ước lượng được:

$$
\theta_{t+1} = \theta_t - \eta \widehat{\nabla L}(\theta_t).
$$

Backpropagation là quy tắc chuỗi được tổ chức theo đồ thị tính toán. Nhờ tự động vi phân, ta có gradient chính xác của hàm hợp theo từng trọng số (chỉ sai khác do làm tròn số thực). Nếu phải tính đạo hàm số bằng cách nhích từng trọng số một trong 1 tỷ tham số, ta sẽ mất 1 tỷ lượt chạy tiến; backpropagation tái sử dụng các giá trị trung gian để tính trọn bộ 1 tỷ đạo hàm riêng chỉ với chi phí xấp xỉ một lượt chạy tiến và một lượt chạy ngược.

![Cảnh quan mất mát (phác)]({{ site.baseurl }}/img/chapter_img/ai_loss_landscape.svg)

*Hình. Cảnh quan không lồi: nhiều chậu; thực hành vẫn tìm được chậu hữu ích.*

**Toán học đặt ra câu hỏi gì?** Khi nào phương pháp hội tụ? Bước học, momentum và các phương pháp thích nghi (Adam và họ hàng) hoạt động ra sao? Kích thước batch và nhiễu đóng vai trò gì? Trong học sâu, cảnh quan mất mát không lồi và rất lớn, nên các bảo đảm cổ điển cho bài toán **lồi** hiếm khi áp dụng trực tiếp. Một trực giác hữu ích từ hình học chiều cao: ở không gian hàng triệu chiều, một điểm dừng có gradient bằng không gần như luôn là **điểm yên ngựa** (lõm theo vài hướng, lồi theo các hướng khác) hơn là cực tiểu cục bộ tệ — vì để là cực tiểu cục bộ, mọi trong số hàng triệu hướng đều phải uốn lên cùng lúc! Nhiễu từ mini-batch giúp SGD trượt khỏi các điểm yên ngựa ấy và tìm thấy những "chậu" phẳng, rộng.

Giải thích chặt chẽ khoảng cách giữa lý thuyết lồi cổ điển và thành công thực nghiệm của SGD là một **chương trình nghiên cứu** thực sự chứ không phải khẩu hiệu. Giới hạn thời gian liên tục (gradient flow), chế độ mean-field/NTK và hình học của cảnh quan (điểm yên ngựa, các “chậu”, implicit bias) là những chỗ giải tích, xác suất và thực hành đang gặp nhau.

---

### Giải thích: chạy tay một bước lan truyền tiến và backpropagation

Nhiều người thấy backpropagation giống như một "hộp đen" trong PyTorch. Thực chất, nó chỉ là quy tắc đạo hàm hàm hợp (chain rule) trên từng con số cụ thể. Hãy tự kiểm tra toàn bộ vòng lặp học trên một mạng 2 lớp tí hon với **đầu vào** $$x = egin{pmatrix}1\-2\end{pmatrix}$$, **nhãn thật** $$y = 4$$, và hàm kích hoạt $$\mathrm{ReLU}(z) = \max(0, z)$$.

Cho trọng số ban đầu:

$$
W_1 = egin{pmatrix} 1 & -1 \ 2 & 1 \end{pmatrix}, \qquad
b_1 = egin{pmatrix} 0 \ 1 \end{pmatrix}, \qquad
w_2 = egin{pmatrix} 1 & -1 \end{pmatrix}, \qquad
b_2 = 0.
$$

1. **Lan truyền tiến (Forward pass):**
   - Lớp ẩn trước kích hoạt: $$z_1 = W_1 x + b_1 = egin{pmatrix}1(1) + (-1)(-2) + 0 \ 2(1) + 1(-2) + 1\end{pmatrix} = egin{pmatrix}3 \ 1\end{pmatrix}$$.
   - Sau ReLU (vì cả 3 và 1 đều dương nên giữ nguyên): $$h = \mathrm{ReLU}(z_1) = egin{pmatrix}3 \ 1\end{pmatrix}$$.
   - Dự đoán đầu ra: $$\hat y = w_2 h + b_2 = 1(3) + (-1)(1) + 0 = 2$$.
   - Hàm mất mát bình phương: $$\ell = rac{1}{2}(\hat y - y)^2 = rac{1}{2}(2 - 4)^2 = 2$$.

2. **Lan truyền ngược (Backpropagation — đi từ phải sang trái):**
   - Đạo hàm theo đầu ra: $$rac{\partial \ell}{\partial \hat y} = \hat y - y = 2 - 4 = -2$$.
   - Đạo hàm theo lớp cuối $$w_2$$: $$rac{\partial \ell}{\partial w_2} = rac{\partial \ell}{\partial \hat y}\, h^	op = (-2)egin{pmatrix}3 & 1\end{pmatrix} = egin{pmatrix}-6 & -2\end{pmatrix}$$.
   - Truyền tín hiệu lỗi về lớp ẩn $$h$$: $$rac{\partial \ell}{\partial h} = w_2^	op rac{\partial \ell}{\partial \hat y} = egin{pmatrix}1 \ -1\end{pmatrix}(-2) = egin{pmatrix}-2 \ 2\end{pmatrix}$$.
   - Qua đạo hàm ReLU (vì $$z_{1,1}=3>0$$ và $$z_{1,2}=1>0$$ nên đạo hàm đều bằng $$1$$): $$rac{\partial \ell}{\partial z_1} = egin{pmatrix}-2 \ 2\end{pmatrix}$$.
   - Đạo hàm theo ma trận $$W_1$$:
     $$rac{\partial \ell}{\partial W_1} = rac{\partial \ell}{\partial z_1}\, x^	op = egin{pmatrix}-2 \ 2\end{pmatrix}egin{pmatrix}1 & -2\end{pmatrix} = egin{pmatrix}-2 & 4 \ 2 & -4\end{pmatrix}.$$

3. **Một bước cập nhật Gradient Descent (chỉ cập nhật $$w_2$$ với bước học $$\eta = 0.1$$ để dễ kiểm tra):**
   - Trọng số mới: $$w_2^{	ext{mới}} = w_2 - 0.1egin{pmatrix}-6 & -2\end{pmatrix} = egin{pmatrix}1.6 & -0.8\end{pmatrix}$$.
   - Dự đoán mới: $$\hat y^{	ext{mới}} = 1.6(3) + (-0.8)(1) = 4.0$$ — **mất mát sụp từ $$2$$ xuống đúng $$0$$ chỉ sau một bước!**

Nhìn vào phép tính trên, bạn thấy ngay: backpropagation không hề có phép màu nào, nó chỉ lưu sẵn $$h$$ và $$z_1$$ từ lượt tiến để tránh tính đi tính lại đạo hàm khi mạng có hàng tỷ tham số.

## 4. Xác suất, thống kê và khả năng tổng quát hóa

Dữ liệu là mẫu lấy từ một phân phối $$\mathcal{D}$$ chưa biết. **Rủi ro thật** là kỳ vọng của mất mát trên mẫu mới; **rủi ro thực nghiệm** là mất mát trung bình trên tập huấn luyện:

> Mất mát huấn luyện thấp không tự động có nghĩa là rủi ro thật thấp.

Lý thuyết học thống kê cổ điển chặn khoảng cách tổng quát hóa bằng độ phức tạp của lớp hàm (VC, Rademacher): theo bức tranh cổ điển, nếu mô hình quá phức tạp, nó sẽ khớp cả nhiễu và dự đoán kém trên dữ liệu mới (đường cong chữ U giữa bias và variance). Thế nhưng mạng hiện đại thì **quá tham số** — một mạng có hàng triệu trọng số có thể học thuộc lòng cả tập ảnh bị tráo nhãn ngẫu nhiên — nhưng khi huấn luyện trên nhãn thật, nó vẫn thường tổng quát hóa rất tốt.

Hiện tượng **double descent** (giảm kép) cho thấy câu chuyện chữ U quen thuộc mới chỉ là nửa đầu của bức tranh: khi số tham số vượt xa ngưỡng nội suy (nơi lỗi huấn luyện chạm 0), lỗi kiểm tra lại *tiếp tục giảm xuống* lần thứ hai. Lý do trực giác là khi có vô số hàm đi qua mọi điểm huấn luyện, thuật toán tối ưu có đủ không gian để chọn ra **hàm trơn nhất, đơn giản nhất** trong số đó thay vì phải gồng mình uốn éo sát ngưỡng vừa đủ. Đây là vùng mà nhiều lời giải thích phổ thông không đủ dùng.

Xác suất còn xuất hiện trong gradient ngẫu nhiên, quan điểm Bayes và PAC-Bayes, hiệu chuẩn xác suất, và các mô hình sinh (likelihood, các phân kỳ, score matching, và mối liên hệ với vận chuyển tối ưu).

---

## 5. Các mảng toán khác (một bản đồ, không phải bách khoa)

| Lĩnh vực | Vai trò |
|----------|---------|
| Lý thuyết thông tin | Cross-entropy, nén, ước lượng dung lượng mô hình |
| Hệ động lực | Quỹ đạo huấn luyện; giới hạn thời gian liên tục |
| Giải tích điều hòa / xấp xỉ | Những hàm nào biểu diễn được hiệu quả |
| Lý thuyết trò chơi | Huấn luyện đối kháng; GAN như một trạng thái cân bằng lý tưởng hóa |
| Suy diễn nhân quả | Vượt khỏi giả thiết i.i.d.; chính sách và độ bền vững |
| Logic / phương pháp hình thức | Đặc tả và kiểm chứng (còn non so với quy mô hệ thống) |
| Vận chuyển tối ưu | Khoảng cách giữa các phân phối; mô hình sinh và thích nghi miền |
| Hình học nhiều chiều | Hiện tượng tập trung, chiếu ngẫu nhiên, hình học của embedding |

Bạn không cần thành thạo tất cả. Điều cần thấy là AI **sử dụng** nhiều lĩnh vực chứ không thay thế được chúng. Đại số tuyến tính và giải tích là công cụ dùng hằng ngày; xác suất và tối ưu giải thích quá trình huấn luyện; hình học và thống kê giải thích khả năng tổng quát hóa.

---

## 6. Những điều còn mở

1. Vì sao mạng quá tham số tổng quát hóa tốt trên dữ liệu có cấu trúc.
2. **Implicit bias** của bộ tối ưu: trong vô số nghiệm có mất mát huấn luyện bằng không, SGD chọn nghiệm nào?
3. Học đặc trưng so với chế độ kernel/NTK “lười”.
4. Độ bền vững và tấn công đối kháng: hình học của biên quyết định.
5. Scaling laws: các đường khớp thực nghiệm khá chắc, nhưng lý thuyết suy ra chúng mới có từng phần.
6. Hành vi của foundation model: in-context learning, “emergence”. Cần tách phần đo lường, phần định nghĩa còn mơ hồ và phần quảng cáo.

**Quy luật thực nghiệm khác với định lý, và cả hai đều khác với lời quảng cáo sản phẩm.**

### Các “mode” khoa học, trực thăng và đi bộ, và vấn đề tiêu hóa chứng minh (theo Tao)

Trong [buổi nói chuyện Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) nhân dịp ra mắt *Six Math Essentials*, Terence Tao mô tả khoa học như một chuỗi các mode: trước hết là lý thuyết và thí nghiệm, rồi đến mô phỏng, rồi dữ liệu lớn, và bây giờ là sự hỗ trợ tự động. Mỗi mode có thể chạy nhanh hơn mode trước. Nhưng nhanh hơn chưa chắc là khoa học *tiến bộ*, theo nghĩa là con người vẫn hiểu, vẫn giảng dạy được và vẫn muốn có những kết quả đó.

Ẩn dụ đi bộ của ông nói về cách dạy chứ không phải lệnh cấm dùng công cụ. Khi đi bộ, bạn nghe thấy một thác nước, đi lạc một đoạn, thấy một thác khác ở xa mà người đi sau có thể tới được. Còn trực thăng thì có thể thả bạn đúng chỗ thác ban đầu rồi bay về. Bạn có một tấm ảnh nhưng không có bản đồ. Khi chỉ nhắm đến mục tiêu đã định, ta dễ bỏ qua những ngõ rẽ bên đường, mà chính những kết nối bất ngờ đó mới tạo ra lý thuyết.

Về các mô hình ngôn ngữ lớn, ông cố ý không lãng mạn hóa. Chúng là những “cỗ máy” thống kê được huấn luyện ở quy mô khổng lồ, và bổ sung cho **chiều sâu** của con người nhờ có **chiều rộng**. Đưa cho chúng một nghìn bài toán có độ khó lẫn lộn, chúng có thể giải được một phần, trong khi không chuyên gia nào kịp nhớ ra rằng bài đó khớp với một bài báo năm 1970 ít người biết. Nhưng đưa cho chúng bài mà chưa phương pháp chuẩn nào giải được, thì theo ông, chúng vẫn chỉ đang đoán. Việc của nghề toán là ghép chiều rộng ấy với những bài toán sâu và chậm mà con người vẫn chủ động chọn.

Cũng trong buổi nói chuyện đó, ông cho rằng một chứng minh có vòng đời: được sinh ra, được kiểm tra, được viết lại để người đọc thấy chỗ khó nằm ở đâu, được công nhận là thú vị, rồi được đưa vào giáo trình. Điều ông lo là khâu sinh ra và khâu kiểm tra đang tăng tốc, còn khâu tiêu hóa thì không. Cộng đồng sẽ phải đối mặt với **tình trạng không tiêu hóa nổi chứng minh**: có quá nhiều lời giải trông đúng đến mức không phân loại xuể, và có nguy cơ tối ưu nhầm bảng điểm của khoa học. Ông vẫn bênh vực nghiên cứu xuất phát từ sự tò mò, và bênh vực việc truyền thông phải cho thấy *quá trình*, không chỉ tiện ích. Không điều nào ở đây là lời quảng bá sản phẩm cho khóa học; chúng chỉ là một khung để đọc cho tỉnh táo. Trang tổng hợp: [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/).

---

## 7. Thổi phồng và cách nói chính xác

| Tuyên bố thổi phồng | Cách diễn đạt chính xác hơn |
|---------------------|------------------------------|
| “Mạng nơ-ron hoạt động như não.” | Chỉ là một ẩn dụ thô; kiến trúc và quy tắc học khác nhau rất nhiều. |
| “AI đã giải xong bài toán trí tuệ.” | Hiệu năng trên một nhiệm vụ hẹp không phải là trí tuệ tổng quát. |
| “Giờ chỉ cần tăng quy mô, hết cần toán.” | Quy mô quan trọng, nhưng lý thuyết về tổng quát hóa và độ bền vững chưa xong. |
| “Loss giảm nghĩa là đã hiểu.” | Chỉ số huấn luyện không đồng nghĩa với hiểu khái niệm, năng lực nhân quả hay độ an toàn. |
| “Attention *is* all you need, như một lý thuyết khoa học đầy đủ.” | Transformer là một lớp kiến trúc thành công; khẩu hiệu đó **không** phải định lý đầy đủ về nhận thức. |

Khi đọc một bài báo về AI, hãy hỏi bốn câu: **đối tượng toán học là gì? Điều gì đã được chứng minh? Điều gì đã được đo? Điều gì mới chỉ là phỏng đoán?**

---

## 8. Chuỗi cơ chế tối thiểu

**Dữ liệu dạng vector** → **mô hình** $$f_\theta$$ → **mất mát** → **ước lượng gradient** → **cập nhật tham số** → **bộ dự đoán được triển khai**, rồi được đánh giá bằng rủi ro trên tập hold-out.

Mỗi mũi tên là một chỗ toán học có thể hỏng: đặc trưng kém, loss sai, gradient nổ hoặc biến mất, phân phối dữ liệu bị lệch, chỉ số đánh giá chọn sai.

### Ví dụ ngắn: lọc thư rác

Mỗi email được biến thành một vector $$x\in\mathbb{R}^d$$. Dùng hồi quy logistic:

$$
\mathbb{P}(Y=1\mid x)=\sigma(w^\top x+b),\qquad
\sigma(z)=\frac{1}{1+e^{-z}},
$$

với mất mát cross-entropy; gradient descent cập nhật $$(w,b)$$ trên từng mini-batch. Đủ mọi thành phần đã xuất hiện: tích vô hướng, hàm liên kết phi tuyến, mất mát xác suất, tối ưu ngẫu nhiên, đánh giá trên tập hold-out. Nếu thay ánh xạ tuyến tính bằng mạng sâu, bộ khung toán vẫn **y nguyên**, chỉ có lớp giả thuyết và cảnh quan tối ưu là phình to ra.

### Đánh giá bằng con số

Độ chính xác trên tập kiểm tra là một **ước lượng thực nghiệm**, không phải một chặn kiểu PAC. Độ hiệu chuẩn, hiệu năng trên các nhóm con, độ bền vững khi phân phối dịch chuyển và rủi ro bị tấn công đối kháng đều là những mục tiêu toán học khác. Văn hóa bảng xếp hạng tối ưu hóa thứ được đo; lý thuyết nhắc ta nhớ thứ *không* được đo. Khi báo chí nói “ngang tầm con người”, hãy hỏi: trên phân phối nào, theo chỉ số nào, và đã kiểm soát việc dữ liệu đánh giá lọt vào dữ liệu huấn luyện chưa?

---

## Những nhầm lẫn thường gặp

| Tuyên bố | Đánh giá | Chỉnh lại |
|----------|----------|-----------|
| “AI chỉ là thống kê.” | Thiếu | Còn có tối ưu, đại số tuyến tính, lý thuyết xấp xỉ. |
| “Gradient descent luôn tìm được cực tiểu toàn cục.” | Sai nói chung | Bài toán không lồi; trên thực tế chỉ tìm được điểm dùng tốt. |
| “Thêm tham số thì luôn overfit.” | Quan niệm dân gian | Chế độ quá tham số tinh tế hơn nhiều. |
| “Xấp xỉ phổ quát giải thích thành công của học sâu.” | Thổi phồng | Tồn tại không có nghĩa là tìm được hiệu quả. |
| “Scaling law là định lý.” | Thường không | Là đường khớp thực nghiệm; lý thuyết mới có từng phần. |
| “Phải có lý thuyết xong thì kỹ thuật mới chính đáng.” | Sai về lịch sử | Máy bay đã bay trước khi người ta kiểm soát được đầy đủ phương trình Navier–Stokes; lý thuyết vẫn giúp giảm rủi ro và định hướng thiết kế. |

---

## Tóm tắt từ phần nghiên cứu video

Phần này dùng cho buổi seminar; hãy đối chiếu với nguồn gốc và không coi là bản chép lời.

### Hiện trạng

**Đây là một lĩnh vực nghiên cứu đang hoạt động.** Thực hành kỹ thuật cốt lõi đã chín muồi, nhưng hiểu biết toán học về học sâu (tổng quát hóa, cảnh quan tối ưu, học đặc trưng) vẫn **mới có từng phần** tính đến năm 2026.

### Phát biểu cốt lõi

Xấp xỉ phổ quát cổ điển là định lý về *biểu diễn*, không phải định lý về huấn luyện. Huấn luyện là cực tiểu hóa rủi ro thực nghiệm bằng SGD trên hàm $$L(\theta)$$ không lồi. Việc tổng quát hóa của mạng quá tham số **chưa** được lý thuyết VC cổ điển giải quyết.

### Định nghĩa cần nhớ

- **Ánh xạ một lớp.** $$x\mapsto \sigma(Wx+b)$$ với hàm phi tuyến $$\sigma$$.
- **Rủi ro thực nghiệm.** $$\frac1n\sum_i \ell(f_\theta(x_i),y_i)$$, so với rủi ro thật $$\mathbb{E}\ell$$.

### Cần phân biệt rõ

- Xấp xỉ phổ quát **không** có nghĩa là bộ tối ưu sẽ tìm được hàm xấp xỉ đó.
- Một bản demo sản phẩm **không** phải là một định lý toán học.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh hay bài báo gốc khi cần khẳng định điều quan trọng.

**Thứ tự gợi ý**

1. **Định hướng**: 3Blue1Brown, But what is a neural network?: [https://www.youtube.com/watch?v=aircAruvnKk](https://www.youtube.com/watch?v=aircAruvnKk).  
2. **Cốt lõi**: 3Blue1Brown, Gradient descent, how neural networks learn: [https://www.youtube.com/watch?v=IHZwWFHWa-w](https://www.youtube.com/watch?v=IHZwWFHWa-w).  
3. **Cốt lõi**: 3Blue1Brown, What is backpropagation really doing?: [https://www.youtube.com/watch?v=Ilg3gGewQ5U](https://www.youtube.com/watch?v=Ilg3gGewQ5U).  
4. **Nền tảng**: 3Blue1Brown, Backpropagation calculus: [https://www.youtube.com/watch?v=tIeHLnjs5U8](https://www.youtube.com/watch?v=tIeHLnjs5U8).  
5. **Tổng hợp**: danh sách phát Neural Networks của 3Blue1Brown: [https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi).  

**Lưu ý về hiện trạng:** đây là lĩnh vực nghiên cứu đang hoạt động. Thực hành kỹ thuật cốt lõi đã chín muồi; hiểu biết toán học về học sâu (tổng quát hóa, cảnh quan tối ưu, học đặc trưng) vẫn còn từng phần tính đến năm 2026.

---

### Ảnh khung hình

Chú thích tự động của video được tải về chỉ để điều hướng, **không** thay thế nội dung bài.

![Frame mẫu video flagship]({{ site.baseurl }}/img/video_research/flagships/ai_3b1b_nn_frame01.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu tham khảo

1. Goodfellow, Bengio, Courville — *Deep Learning*.
2. Các bài khảo sát gần đây về khả năng tổng quát hóa của mạng sâu.
3. Lý thuyết học cổ điển: Vapnik; Rademacher.
4. NTK và mean-field: chế độ “lười” so với học đặc trưng.
5. Liên kết: [Đại số tuyến tính → AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/), [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/), [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/).

---

### Video (lộ trình gợi ý)

- 3Blue1Brown, But what is a neural network? (định hướng): https://www.youtube.com/watch?v=aircAruvnKk
- 3Blue1Brown, Gradient descent, how neural networks learn (cốt lõi): https://www.youtube.com/watch?v=IHZwWFHWa-w
- 3Blue1Brown, What is backpropagation really doing? (cốt lõi): https://www.youtube.com/watch?v=Ilg3gGewQ5U
- 3Blue1Brown, Backpropagation calculus (nền tảng): https://www.youtube.com/watch?v=tIeHLnjs5U8
- Danh sách phát Neural Networks của 3Blue1Brown (tổng hợp): https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi

### Bài báo và web

- Goodfellow, Bengio, Courville — Deep Learning (trang sách): https://www.deeplearningbook.org/
- Wikipedia — Universal approximation theorem: https://en.wikipedia.org/wiki/Universal_approximation_theorem
- Double descent (Belkin và cộng sự, 2019): https://arxiv.org/abs/1812.11118
- Trang của 3Blue1Brown: https://www.3blue1brown.com/
- Wikipedia — Deep learning: https://en.wikipedia.org/wiki/Deep_learning

### Khóa học

- Gói: `research/video-research/mathematics-of-ai/` (đặc biệt `references.md`, `learning_path.md`).
- Terence Tao — Big Think OOMx2BHHWtE (mode khoa học, trực thăng/đi bộ, khó tiêu chứng minh): https://www.youtube.com/watch?v=OOMx2BHHWtE
- Hub khóa học: [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/).
- Terence Tao — Big Think OOMx2BHHWtE (các mode khoa học, trực thăng và đi bộ, tiêu hóa chứng minh): https://www.youtube.com/watch?v=OOMx2BHHWtE

## Hướng đi tiếp

- [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/); [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).
- [Hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/); [Vận chuyển tối ưu]({{ site.baseurl }}/contents/vi/chapter06/06_09_Optimal_Transport/).
- Thực hành: huấn luyện một mô hình nhỏ; ghi lại kết quả train và test; đối chiếu với Mục 4.
- Giữ một bảng ghi các tuyên bố: *định lý / chặn / quy luật thực nghiệm / quảng cáo*.

## Video tham khảo

- **Xem trước** — [But what is a neural network? | Deep learning chapter 1](https://www.youtube.com/watch?v=aircAruvnKk) — 3Blue1Brown, tiếng Anh. Xem trước để nắm hình dung ban đầu về mạng nơ-ron như chuỗi các lớp tuyến tính xen phi tuyến.
- [Gradient descent, how neural networks learn | Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w) — 3Blue1Brown, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để hiểu mạng học bằng cách nào.
- [One of the world's greatest mathematicians explains 6 essential concepts of math | Terence Tao](https://www.youtube.com/watch?v=OOMx2BHHWtE) — Big Think, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, về cách một nhà toán học nhìn khoa học và vai trò của AI.
