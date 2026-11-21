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

Một mô hình ngôn ngữ lớn trả lời câu hỏi trong chưa đầy một giây. Phía sau là các vector hàng nghìn chiều, những ma trận có hàng tỷ tham số, một mặt mất mát không thể vẽ ra, và quá trình huấn luyện thực chất là bài toán **tối ưu dưới sự bất định**. Hệ thống AI hiện đại vừa là sản phẩm kỹ thuật vừa là một **đối tượng toán học**. Bài này vẽ bản đồ phần toán nằm dưới học sâu, cùng các câu hỏi còn mở, và không giả vờ rằng lĩnh vực này đã “đóng sổ”.

Kỹ năng cần luyện là **biết đọc ở vùng biên**: phân biệt đâu là định lý, đâu là quy luật rút ra từ thực nghiệm, đâu là heuristic và đâu chỉ là quảng cáo. Quy mô và kỹ thuật dĩ nhiên quan trọng, nhưng đại số tuyến tính, xác suất, tối ưu và hình học chiều cao cũng quan trọng không kém.

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

**Một ví dụ cụ thể.** Phân tích thành phần chính (PCA) và phân tích giá trị suy biến (SVD) tìm những hướng có phương sai lớn nhất, để nén dữ liệu hoặc khử nhiễu bằng cách chiếu lên không gian con chính. Nếu $$X$$ là ma trận dữ liệu thì các vector suy biến phải đứng đầu của phiên bản đã được trừ trung bình chính là các hướng chính.

Nhiều chiều không đơn giản là “thêm vài tọa độ”. Hiện tượng tập trung của độ đo, tập điển hình và hình học của mặt cầu nhiều chiều làm thay đổi trực giác về khoảng cách và góc: phần lớn thể tích của quả cầu nhiều chiều nằm trong một lớp vỏ mỏng gần xích đạo, và hai vector ngẫu nhiên gần như vuông góc nhau với xác suất rất cao. Những điều này giúp giải thích vì sao các mô hình quá tham số vẫn chạy được và vì sao phương pháp láng giềng gần nhất “ngây thơ” dễ sai. (Bài hình học nhiều chiều trong chương này đi sâu hơn.)

---

## 2. Mô hình: hàm được ghép từ những mảnh đơn giản

Một lớp kết nối đầy đủ là một ánh xạ tuyến tính, rồi đến một hàm phi tuyến áp dụng theo từng tọa độ:

$$
x \mapsto \sigma(Wx + b),
$$

trong đó $$W$$ là ma trận trọng số, $$b$$ là bias, $$\sigma$$ là hàm kích hoạt (ReLU, GELU, sigmoid, …). Mạng sâu **ghép** nhiều lớp như vậy. Mạng tích chập (CNN) dùng lại các bộ lọc tuyến tính cục bộ có tính bất biến tịnh tiến. Mạng residual viết mỗi lớp thành $$x \mapsto x + f_\theta(x)$$. Transformer dùng **attention**: một ánh xạ có cấu trúc gồm query, key, value, dạng song tuyến tính, với trọng số chuẩn hóa bằng softmax. Nhờ đó mỗi token được trộn thành một tổ hợp tuyến tính của các token khác, với hệ số phụ thuộc vào dữ liệu.

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

Backpropagation là quy tắc chuỗi được tổ chức theo đồ thị tính toán. Nhờ tự động vi phân, ta có gradient chính xác của hàm hợp theo từng trọng số (chỉ sai khác do làm tròn số thực).

![Cảnh quan mất mát (phác)]({{ site.baseurl }}/img/chapter_img/ai_loss_landscape.svg)

*Hình. Cảnh quan không lồi: nhiều chậu; thực hành vẫn tìm được chậu hữu ích.*

**Toán học đặt ra câu hỏi gì?** Khi nào phương pháp hội tụ? Bước học, momentum và các phương pháp thích nghi (Adam và họ hàng) hoạt động ra sao? Kích thước batch và nhiễu đóng vai trò gì? Trong học sâu, cảnh quan mất mát không lồi và rất lớn, nên các bảo đảm cổ điển cho bài toán **lồi** hiếm khi áp dụng trực tiếp. Tuy vậy, các phương pháp kiểu SGD trong thực nghiệm thường vẫn tìm được tham số **dùng tốt**. Giải thích khoảng cách này là một **chương trình nghiên cứu** thực sự chứ không phải khẩu hiệu. Giới hạn thời gian liên tục (gradient flow), chế độ mean-field/NTK và hình học của cảnh quan (điểm yên ngựa, các “chậu”, implicit bias) là những chỗ giải tích, xác suất và thực hành đang gặp nhau.

---

## 4. Xác suất, thống kê và khả năng tổng quát hóa

Dữ liệu là mẫu lấy từ một phân phối $$\mathcal{D}$$ chưa biết. **Rủi ro thật** là kỳ vọng của mất mát trên mẫu mới; **rủi ro thực nghiệm** là mất mát trung bình trên tập huấn luyện:

> Mất mát huấn luyện thấp không tự động có nghĩa là rủi ro thật thấp.

Lý thuyết học thống kê cổ điển chặn khoảng cách tổng quát hóa bằng độ phức tạp của lớp hàm (VC, Rademacher). Mạng hiện đại thì **quá tham số**, có thể khớp cả nhãn nhiễu, nhưng vẫn thường tổng quát hóa tốt trên dữ liệu có cấu trúc. **Double descent** cho thấy câu chuyện quen thuộc về đường cong chữ U giữa bias và variance là quá đơn giản. Đây là vùng mà nhiều lời giải thích phổ thông không đủ dùng.

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

## Bài tập

1. Nhân một ma trận $$2\times 2$$ với một vector bằng tay, và hiểu nó như một lớp tuyến tính không có bias.
2. Định nghĩa rủi ro thực nghiệm và rủi ro thật; viết một câu giải thích vì sao chúng lệch nhau.
3. (Tối đa 250 từ) Mô tả chuỗi dữ liệu → mô hình → loss → cập nhật → triển khai, và nêu một lỗi toán học có thể xảy ra ở mỗi bước.
4. Viết ba câu: đại số tuyến tính, xác suất và tối ưu xuất hiện như thế nào khi huấn luyện một bộ phân loại.
5. Tìm một tin tức về AI và viết lại thành hai câu, tách phần đo được khỏi phần suy đoán.
6. Chọn một mục trong Mục 6; viết một câu hỏi thực nghiệm và một câu hỏi toán học liên quan.
7. Đọc phần tóm tắt của một bài báo về double descent hoặc NTK; liệt kê ba thuật ngữ cần tra cứu.

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
