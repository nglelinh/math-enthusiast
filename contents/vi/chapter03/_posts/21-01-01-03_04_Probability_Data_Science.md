---
layout: post
title: "Xác suất → Khoa học dữ liệu"
chapter: '03'
order: 4
owner: Nguyen Le Linh
lang: vi
categories:
- chapter03
lesson_type: required
---

Một đội kỹ sư phấn khởi tung ra mô hình nhận diện gian lận đạt độ chính xác 99% trên dữ liệu thử nghiệm — để rồi chỉ sau một tuần chạy thật, hệ thống khóa nhầm hàng nghìn thẻ của khách hàng vô tội. Một công ty đổi màu nút "Mua hàng" thấy doanh số tăng 8% sau hai ngày chạy thử nghiệm A/B, nhưng khi áp dụng toàn hệ thống thì doanh số lại… đứng yên. Một xét nghiệm y khoa có độ chính xác 99% trả về kết quả dương tính, vậy mà xác suất người đó thực sự mắc bệnh lại chưa tới 20%.

Chuyện gì đã xảy ra trong cả ba tình huống ấy? Thế giới ngoài kia đầy nhiễu, mẫu dữ liệu ta thu được luôn hữu hạn, và trực giác tự nhiên của con người cực kỳ dễ bị đánh lừa bởi sự ngẫu nhiên. **Xác suất** là ngôn ngữ duy nhất giúp ta gọi tên chính xác những cái bẫy đó, đo lường mức độ bất định, và đưa ra quyết định tỉnh táo dù không bao giờ có đủ 100% thông tin.

Bài học này không phải cả một giáo trình xác suất dày cộp. Nó tập trung giải thích **vì sao xác suất trở thành nền móng không thể thiếu của khoa học dữ liệu và học máy hiện đại**.

**Lộ trình:** bản đồ ngành xác suất & thống kê → xem sự ngẫu nhiên như một mô hình → kỳ vọng và phương sai → luật số lớn (LLN) và định lý giới hạn trung tâm (CLT) → suy diễn thống kê → rủi ro trong học máy → tư duy Bayes, nhân quả và dịch chuyển phân phối → bất đẳng thức tập trung → nhầm lẫn thường gặp.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt hai cách nhìn dữ liệu: như những con số cố định, và như giá trị quan sát được của các biến ngẫu nhiên.
- Phát biểu **luật số lớn (LLN)** và **định lý giới hạn trung tâm (CLT)** bằng lời và bằng công thức, và nói được chúng biện minh cho điều gì trong thực tế.
- Giải thích ước lượng, khoảng tin cậy và kiểm định giả thuyết là cách *suy luận khi có bất định*, không phải bằng chứng cho chân lý.
- Định nghĩa **rủi ro** là mất mát kỳ vọng, và nối khái niệm cực tiểu hóa rủi ro thực nghiệm (ERM) với "hàm mất mát trên tập huấn luyện".
- Giải thích vì sao tương quan không phải là nhân quả, và vì sao sự dịch chuyển phân phối làm hỏng cách kiểm định mô hình đơn giản.
- Tránh hai nhầm lẫn: "xác suất chỉ dùng cho cờ bạc" và "dữ liệu lớn xóa hết bất định".

**Kiến thức nền.** Trung bình cộng, phép đếm. Sẽ có ích nếu biết [đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/).

---

## Bản đồ kiến thức nền: Lý thuyết xác suất và thống kê toán học là gì, nghiên cứu những gì?

Nhiều người từng học xác suất qua vài bài toán rút bi trong hộp hay tung xúc xắc và tưởng ngành này chỉ xoay quanh tổ hợp. Ở bậc đại học và trong khoa học dữ liệu, **xác suất (probability)** và **thống kê (statistics)** là hai chiều ngược nhau của cùng một cây cầu:

- **Chiều xuôi — Lý thuyết xác suất:** *Biết quy luật (mô hình), dự đoán dữ liệu.* Nếu ta biết cơ chế sinh ra sự ngẫu nhiên (phân phối của biến ngẫu nhiên $$X$$), xác suất nghiên cứu xem trung bình sẽ hội tụ về đâu (Luật số lớn), dao động có hình dạng gì (Định lý giới hạn trung tâm), và rủi ro xảy ra biến cố cực đoan nhỏ đến mức nào (Bất đẳng thức tập trung).
- **Chiều ngược — Thống kê toán học & Lý thuyết học:** *Có dữ liệu nhiễu, suy ngược lại quy luật.* Trong đời thật, không ai cho ta biết trước xác suất thật $$p$$ của nút bấm hay hàm thật $$f$$ của thị trường. Thống kê cung cấp công cụ ước lượng tham số (MLE, Bayes), định lượng sai số (khoảng tin cậy), kiểm chứng giả thuyết, và bảo đảm rằng một mô hình học máy học tốt trên mẫu hữu hạn vẫn sẽ chạy tốt trên thế giới thật.

Nói ngắn gọn: **đại số tuyến tính giúp máy tính tính nhanh; xác suất và thống kê giúp ta biết liệu con số máy tính vừa tính ra có đáng tin hay không.**

---

## 1. Bước mô hình hóa: xem dữ liệu là ngẫu nhiên

Trong lập trình thông thường, một bảng số chỉ là một bảng số cố định. Trong khoa học dữ liệu, ta thực hiện một bước nhảy tư duy: xem các quan sát $$X_1,\ldots,X_n$$ là những **biến ngẫu nhiên** rút ra từ một quá trình sinh dữ liệu ẩn. Nếu ngày hôm qua lặp lại một lần nữa, tập khách hàng ghé thăm trang web sẽ hơi khác đi, và mọi con số đo được (doanh thu, tỉ lệ nhấp chuột) cũng sẽ dao động theo.

Một **phân phối xác suất** là bản mô tả toàn bộ hành vi của quá trình đó: ví dụ phân phối Bernoulli($$p$$) cho một cú nhấp chuột (có hoặc không), hay phân phối chuẩn (Gauss) cho sai số đo đạc:

$$
f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\Bigl(-\frac{(x-\mu)^2}{2\sigma^2}\Bigr).
$$

**Ý chính.**  
*Xác suất chuyển câu hỏi tĩnh "điều gì đã xảy ra trong bảng Excel này?" thành câu hỏi động "quá trình nào đã sinh ra dữ liệu này, và ngày mai điều gì có khả năng xảy ra tiếp theo?"*

---

## 2. Kỳ vọng, phương sai và tính toán với trung bình

$$\mathbb{E}[X]$$ là giá trị trung bình có trọng số theo xác suất (tâm cân bằng của phân phối). $$\mathrm{Var}(X)=\mathbb{E}[(X-\mathbb{E}X)^2]$$ đo độ phân tán quanh tâm đó.

Hai quy tắc đơn giản nhưng cực kỳ mạnh mẽ trong thực hành:

1. **Tính tuyến tính của kỳ vọng:**
$$
\mathbb{E}[aX+bY]=a\mathbb{E}X+b\mathbb{E}Y.
$$
Điều đáng kinh ngạc là công thức này **luôn đúng ngay cả khi $$X$$ và $$Y$$ phụ thuộc chằng chịt vào nhau**. Nhờ đó ta có thể tính doanh thu kỳ vọng của một giỏ hàng nhiều món hay độ phức tạp trung bình của các thuật toán ngẫu nhiên (như QuickSort) mà không cần biết phân phối đồng thời phức tạp của chúng.

2. **Phương sai của trung bình giảm theo $$1/n$$ (khi độc lập):** nếu $$X_1,\dots,X_n$$ độc lập có cùng phương sai $$\sigma^2$$, thì
$$
\mathrm{Var}(\bar{X}_n) = \frac{\sigma^2}{n}, \qquad \text{độ lệch chuẩn} = \frac{\sigma}{\sqrt{n}}.
$$
**Ví dụ số.** Nếu mỗi cảm biến nhiệt độ có sai số chuẩn $$\sigma = 2^\circ\mathrm{C}$$, lấy trung bình $$100$$ lần đo độc lập sẽ kéo sai số chuẩn xuống còn $$2/\sqrt{100} = 0{,}2^\circ\mathrm{C}$$. Muốn giảm sai số đi một nửa nữa (xuống $$0{,}1^\circ\mathrm{C}$$), bạn không cần gấp đôi dữ liệu mà phải tăng **gấp 4 lần** (lên $$400$$ lần đo). Quy luật $$\sqrt{n}$$ này giải thích vì sao thu thập dữ liệu để tăng độ chính xác càng về sau càng tốn kém!

---

## 3. Luật số lớn: vì sao trung bình ổn định

**LLN (phát biểu không chính thức).** Với các biến độc lập cùng phân phối (i.i.d.) có kỳ vọng hữu hạn $$\mu$$,

$$
\bar{X}_n=\frac1n\sum_{i=1}^n X_i \to \mu
$$

(khi $$n\to\infty$$, theo nghĩa hội tụ xác suất hoặc hầu chắc chắn).

**Vì sao LLN hữu ích đến thế?** Nó là lý do ngành bảo hiểm tồn tại (tai nạn của một cá nhân không đoán trước được, nhưng tổng chi trả trung bình của 1 triệu khách hàng lại cực kỳ ổn định), lý do phương pháp mô phỏng **Monte Carlo** tính được những tích phân hàng trăm chiều trong tài chính và vật lý, và lý do nhiễu của thuật toán SGD bị triệt tiêu dần khi đi qua nhiều lô dữ liệu.

**Những gì LLN không nói.** LLN không bảo đảm một mẫu nhỏ là "đủ". Nó không hề sửa được **sai lệch hệ thống (bias)**: nếu cái cân của bạn bị lệch sẵn $$+2\text{ kg}$$, bạn có cân 1 triệu lần rồi lấy trung bình thì kết quả vẫn hội tụ về con số sai lệch $$+2\text{ kg}$$ đó. Và LLN cũng không tự động áp dụng khi thế giới đổi thay theo thời gian (dữ liệu không dừng).

---

### Video ngắn: Tổng xúc xắc thành hình chuông

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/clt-dice-bell_vi.mp4"></video>
</div>

Phân phối chính xác của tổng $$n$$ xúc xắc đều, co giãn về cùng độ rộng, với $$n = 1, 2, 3, 5, 10, 30$$. Một xúc xắc thì đều; tổng của nhiều xúc xắc bám sát đường chuông chuẩn.


### Tự tay thử: Cộng xúc xắc và xem đường chuông

<div class="mex-explainer" data-mex="clt" data-lang="vi"></div>


## 4. CLT: vì sao xuất hiện hình chuông

Nếu LLN nói trung bình mẫu $$\bar{X}_n$$ tiến về $$\mu$$, thì **Định lý giới hạn trung tâm (CLT)** trả lời câu hỏi tinh tế hơn: *trên đường tiến về $$\mu$$, sai số $$\bar{X}_n - \mu$$ dao động theo hình dáng gì?*

**CLT (phát biểu không chính thức).** Với các biến i.i.d. có phương sai $$\sigma^2$$ hữu hạn,

$$
\sqrt{n}\,\frac{\bar{X}_n-\mu}{\sigma}\ \xrightarrow{d}\ N(0,1).
$$

**Ý chính.**  
*Dù phân phối gốc của từng quan sát méo mó, rời rạc hay phẳng lì như con xúc xắc, tổng (và trung bình) của nhiều tác động nhỏ, độc lập luôn hội tụ về hình chuông chuẩn (Gauss).*

**Ví dụ ứng dụng thực tế (thử nghiệm A/B).** Một trang web đo tỉ lệ mua hàng của giao diện mới trên $$n=1{.}000$$ lượt khách và thấy $$\hat{p} = 10\%$$ ($$0{,}10$$). Độ lệch chuẩn của mỗi lượt Bernoulli là $$\sqrt{0{,}1 \times 0{,}9} = 0{,}3$$, nên sai số chuẩn của trung bình mẫu là $$0{,}3 / \sqrt{1000} \approx 0{,}0095 \approx 1\%$$. Nhờ CLT, ta biết ngay khoảng tin cậy 95% (xấp xỉ $$\pm 2$$ lần sai số chuẩn) nằm quanh $$[8\%, 12\%]$$. Vì thế nếu giao diện cũ đạt $$9{,}5\%$$, mức tăng lên $$10\%$$ hoàn toàn có thể chỉ là nhiễu ngẫu nhiên — chưa đủ bằng chứng để kết luận giao diện mới tốt hơn!

**Lưu ý.** Khi phân phối có đuôi nặng (như phân phối tài sản hay biến động cực đoan trên thị trường tài chính), khi các quan sát phụ thuộc nhau, hoặc khi $$n$$ quá nhỏ, xấp xỉ chuẩn có thể sai lệch mạnh. Khoa học dữ liệu hiện đại thường kết hợp thêm **bootstrap** (tái lấy mẫu bằng máy tính) và các bất đẳng thức tập trung.

---

## 5. Suy diễn: từ mẫu đến kết luận

**Ước lượng điểm** cho một con số đoán tốt nhất $$\hat\theta$$ (như trung bình mẫu, hay ước lượng hợp lý cực đại MLE). **Ước lượng khoảng** đi kèm một biên độ bất định: theo trường phái tần suất là *khoảng tin cậy*, còn theo trường phái Bayes là *khoảng tin cậy hậu nghiệm (credible interval)*.

**Kiểm định giả thuyết** đặt câu hỏi kỷ luật: *"Nếu hiệu ứng thật sự bằng 0 (giả thuyết không $$H_0$$ đúng), xác suất ta tình cờ quan sát được kết quả cực đoan ít nhất bằng kết quả này là bao nhiêu?"* Con số đó chính là **giá trị $$p$$ (p-value)**.
- **Cảnh báo:** giá trị $$p$$ **không phải** là "xác suất giả thuyết không đúng". Ví dụ $$p = 0{,}04$$ chỉ nói rằng nếu không có hiệu ứng thật, thì cứ 100 lần làm thí nghiệm sẽ có khoảng 4 lần tình cờ ra kết quả "đẹp" như vậy do may rủi.

**Hàm hợp lý (Likelihood).** Với mô hình tham số $$p(x\mid\theta)$$, hàm hợp lý $$L(\theta)=\prod_i p(x_i\mid\theta)$$ đo mức độ khớp giữa tham số $$\theta$$ và dữ liệu quan sát. Tìm $$\theta$$ làm cực đại $$L(\theta)$$ chính là **MLE** (thú vị thay, cực tiểu hóa hàm mất mát cross-entropy khi huấn luyện mạng nơ-ron thực chất chính là MLE!). Còn nhân $$L(\theta)$$ với niềm tin ban đầu $$p(\theta)$$ ta được suy diễn **Bayes**: $$p(\theta\mid \text{data})\propto L(\theta)p(\theta)$$.

### Ví dụ cầm tay chỉ việc: Tự tính MLE và sửa bẫy mẫu nhỏ bằng Bayes

Giả sử bạn chạy một mẫu quảng cáo mới $$n = 10$$ lần và thu được $$k = 7$$ lượt nhấp chuột. Xác suất nhấp thật $$p$$ là bao nhiêu?

1. **Viết hàm hợp lý (Likelihood):** xác suất thấy đúng 7 lần nhấp trong 10 lần là $$L(p) = \binom{10}{7} p^7 (1-p)^3$$.
2. **Lấy logarit rồi tìm cực đại (MLE):**
$$
\ell(p) = \ln L(p) = \text{hằng số} + 7\ln p + 3\ln(1-p).
$$
Lấy đạo hàm theo $$p$$ và cho bằng $$0$$:
$$
\ell'(p) = \frac{7}{p} - \frac{3}{1-p} = 0 \implies 7(1-p) = 3p \implies 10p = 7 \implies \hat{p}_{\mathrm{MLE}} = 0{,}70.
$$
3. **Bẫy mẫu nhỏ và cứu cánh Bayes:** điều gì xảy ra nếu bạn mới chỉ hiển thị $$n=2$$ lần và tình cờ cả $$k=2$$ người đều bấm? MLE lập tức kết luận $$\hat{p}_{\mathrm{MLE}} = 2/2 = 100\%$$ — cực kỳ hoang tưởng! Nếu áp thêm một niềm tin tiên nghiệm nhẹ kiểu Bayes (phân phối $$\mathrm{Beta}(2,2)$$, tương đương giả định ban đầu có 2 nhấp giả định và 2 không nhấp giả định), ước lượng hậu nghiệm là:
$$
\hat{p}_{\mathrm{Bayes}} = \frac{k + 2}{n + 2 + 2} = \frac{2 + 2}{2 + 4} = \frac{4}{6} \approx 66{,}7\%.
$$
Khi dữ liệu còn ít, Bayes kéo ước lượng về mức thận trọng; khi dữ liệu lên tới $$n = 10{.}000$$, số $$+2$$ trở nên không đáng kể và Bayes hội tụ về đúng MLE!

### Khung giải thích: Từ một bảng dữ liệu hữu hạn đến quyết định ngoài đời thật (nên đọc chậm)

1. **Xem dữ liệu là một lần rút mẫu ngẫu nhiên:** bảng dữ liệu hôm nay không phải toàn bộ sự thật, mà chỉ là một thực hiện duy nhất của phân phối ẩn $$P(X,Y)$$.
2. **Đo độ dao động của ước lượng:** LLN bảo đảm trung bình mẫu hội tụ về giá trị thật, còn CLT và bất đẳng thức Hoeffding cho biết biên độ sai số $$\pm O(1/\sqrt{n})$$ ở cỡ mẫu hiện tại.
3. **Phân biệt rủi ro thực nghiệm và rủi ro kỳ vọng:** làm mất mát huấn luyện $$\hat{R}_n(f)$$ bằng 0 chưa chắc giúp rủi ro thật $$R(f)$$ nhỏ — ta cần tách tập kiểm tra độc lập và chặn độ phức tạp của mô hình.
4. **Kiểm tra hai giả định ngầm trước khi hành động:** phân phối lúc triển khai có bị dịch chuyển ($$P_{\mathrm{test}} \neq P_{\mathrm{train}}$$) không, và ta đang dùng tương quan để dự đoán hay đang can thiệp nhân quả?

**Kiểm tra nhanh.** Thêm 10 lần dữ liệu giúp giảm sai số ngẫu nhiên đi $$\sqrt{10} \approx 3{,}16$$ lần, nhưng **không bao giờ** tự sửa được thiên lệch chọn mẫu hay dịch chuyển phân phối.

---

## 6. Rủi ro trong học máy: mất mát kỳ vọng

Trong lý thuyết học thống kê, mục tiêu thật sự của một mô hình dự đoán $$f$$ không phải là làm đẹp điểm số trên dữ liệu quá khứ, mà là tối thiểu hóa **rủi ro kỳ vọng (true risk)** trên mọi dữ liệu tương lai rút từ phân phối thật:

$$
R(f)=\mathbb{E}\bigl[\ell(f(X),Y)\bigr].
$$

Trớ trêu thay, ta không bao giờ biết phân phối thật để tính trực tiếp $$R(f)$$. Thứ duy nhất ta có trong tay là tập huấn luyện hữu hạn và **rủi ro thực nghiệm (empirical risk)**:

$$
\hat{R}_n(f)=\frac1n\sum_{i=1}^n \ell(f(X_i),Y_i).
$$

**ERM (cực tiểu hóa rủi ro thực nghiệm)** chọn hàm $$f$$ làm nhỏ nhất $$\hat{R}_n(f)$$. Nhưng nếu lớp hàm $$\mathcal{F}$$ quá phức tạp, mô hình có thể "học vẹt" toàn bộ tập huấn luyện ($$\hat{R}_n(f)=0$$) mà vẫn đoán sai thảm hại trên dữ liệu mới ($$R(f)$$ rất lớn) — đó là hiện tượng **quá khớp (overfitting)**.

Lý thuyết tổng quát hóa (chiều VC, độ phức tạp Rademacher, PAC-Bayes, và các nghiên cứu hiện đại về "double descent") trả lời câu hỏi cốt lõi: *khi nào thì việc làm nhỏ mất mát huấn luyện đảm bảo rủi ro ngoài đời thật cũng nhỏ?* Xem thêm [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/) và [Lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

**Ý chính.**  
*"Độ chính xác trên tập huấn luyện" chỉ là một giá trị mẫu; "hiệu quả ngoài đời thật" là kỳ vọng. Xác suất là chiếc cầu nối hai thứ đó, đồng thời là còi báo động chống ảo tưởng.*

---

## 7. Sự phụ thuộc, Bayes, và ra quyết định khi có bất định

Dữ liệu ngoài đời hiếm khi sạch sẽ như những lần tung đồng xu độc lập:

- **Chuỗi thời gian** và dữ liệu không gian: giá cổ phiếu hôm nay hay nhiệt độ giờ này phụ thuộc chặt vào thời điểm trước đó; công thức sai số chuẩn $$\sigma/\sqrt{n}$$ không còn đúng nguyên trạng.  
- **Mô hình Bayes và mô hình phân cấp:** cho phép chia sẻ thông tin giữa các nhóm ít dữ liệu và nhiều dữ liệu (partial pooling).  
- **Lý thuyết quyết định:** một quyết định tối ưu phải cân nhắc *chi phí sai lầm* (bỏ sót một ca ung thư đắt giá gấp nhiều lần một lần xét nghiệm lại), không chỉ chọn nhãn có xác suất cao nhất.  
- **Hiệu chỉnh (calibration):** nếu mô hình dự báo thời tiết nói "70% có mưa", thì trong số những ngày nó nói 70%, trời phải thực sự mưa khoảng 70% số ngày đó.

**Công thức Bayes và cái bẫy tỉ lệ nền:**

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
$$

**Ví dụ số kinh điển (tại sao xét nghiệm chính xác 99% vẫn dễ báo nhầm?).** Giả sử một căn bệnh hiếm gặp có tỉ lệ mắc trong dân số là $$1\%$$ ($$P(H)=0{,}01$$). Một bộ xét nghiệm rất tốt: nếu bị bệnh thì phát hiện đúng $$99\%$$ ($$P(E\mid H)=0{,}99$$), nếu khỏe mạnh thì chỉ báo dương tính giả $$5\%$$ ($$P(E\mid \neg H)=0{,}05$$). Xét trong $$10{.}000$$ người đi kiểm tra:
- Có $$100$$ người thật sự mắc bệnh → khoảng $$99$$ người ra dương tính thật.
- Có $$9{.}900$$ người khỏe mạnh → $$5\% \times 9{.}900 = 495$$ người bị báo dương tính giả!
- Vậy nếu bạn nhận kết quả dương tính, xác suất bạn thật sự mắc bệnh chỉ là:
$$
P(H\mid E) = \frac{99}{99 + 495} = \frac{99}{594} \approx 16{,}7\%!
$$

Con số gây sốc này không phải nghịch lý mà là lời nhắc nhở sống còn của tư duy Bayes: **luôn nhân bằng chứng mới với tỉ lệ nền (base rate)** trước khi kết luận. Bộ lọc thư rác, phát hiện gian lận ngân hàng và chẩn đoán y khoa đều dựa trên chính phép tính này.

---

## 8. Nhân quả, dịch chuyển phân phối và trách nhiệm khi có bất định

**Tương quan không phải nhân quả.** Dữ liệu cho thấy số kem bán ra và số vụ đuối nước tăng giảm song hành cực chặt, nhưng cấm bán kem chẳng cứu được ai — biến ẩn "nhiệt độ mùa hè" mới là nguyên nhân chung. Suy diễn nhân quả (đồ thị nhân quả DAG, thí nghiệm ngẫu nhiên có đối chứng RCT, biến công cụ) mở rộng xác suất bằng phép toán "can thiệp" ($$\mathrm{do}(X=x)$$). Trước khi ra quyết định chính sách hay kinh doanh từ dữ liệu, phân biệt tương quan với nhân quả là kỹ năng sống còn.

**Dịch chuyển phân phối (distribution shift).** Mọi bảo đảm của học máy đều giả định dữ liệu lúc chạy thật $$P_{\mathrm{test}}$$ giống dữ liệu lúc huấn luyện $$P_{\mathrm{train}}$$. Khi hành vi người dùng thay đổi (như lúc dịch bệnh bùng phát làm đảo lộn thói quen mua sắm) hoặc kẻ tấn công đổi chiêu thức lừa đảo, $$P_{\mathrm{test}} \neq P_{\mathrm{train}}$$ và mô hình tụt dốc không phanh.

**Trách nhiệm.** Truyền đạt sự bất định trung thực quan trọng ngang bằng bản thân dự đoán: một mô hình AI "nói chắc như đinh đóng cột" khi thực chất nó đang đoán mò có thể gây hậu quả nghiêm trọng trong y tế, tín dụng hay xe tự lái.

---

## 9. Bất đẳng thức tập trung với mẫu hữu hạn

CLT chỉ nói chuyện khi $$n \to \infty$$, nhưng ngoài đời ta luôn có một cỡ mẫu $$n$$ hữu hạn. **Bất đẳng thức Hoeffding** (và họ bất đẳng thức tập trung như Bernstein, Chernoff) đưa ra cam kết toán học cứng rắn ngay với $$n$$ hữu hạn: với các biến i.i.d. nằm trong đoạn $$[0,1]$$,

$$
P\bigl(\lvert \bar{X}_n - \mu \rvert \ge \varepsilon\bigr) \le 2\exp(-2n\varepsilon^2).
$$

**Ví dụ số cụ thể.** Bạn muốn thăm dò một tỉ lệ $$p \in [0,1]$$ sao cho sai số không vượt quá $$\varepsilon = 0{,}03$$ (3%) với độ tin cậy ít nhất $$95\%$$ (xác suất sai $$\le 0{,}05$$). Thay vào vế phải: $$2e^{-2n(0{,}03)^2} \le 0{,}05 \implies n \ge \frac{\ln(40)}{2 \times 0{,}0009} \approx 2{.}050$$ mẫu — **điều tuyệt vời là con số 2.050 này hoàn toàn không phụ thuộc vào việc tổng dân số là 100 nghìn hay 100 triệu người!**

Một nhà khoa học dữ liệu chín chắn không dừng ở mẹo vặt "$$n=30$$ là đủ". Họ nêu rõ giả thiết, dùng bất đẳng thức tập trung, bootstrap hoặc sai số chuẩn vững, và luôn nhớ rằng "thêm dữ liệu" không tự xóa được sai lệch chọn mẫu hay dịch chuyển phân phối.

---

### Tóm tắt về xác suất (từ phần tìm hiểu video)

Xem [3B1B Bayes](https://www.youtube.com/watch?v=HZGCoVF3YvM) và [Veritasium — The Bayesian trap](https://www.youtube.com/watch?v=R13BD8qKeTg) trước phần suy diễn.

- **Thói quen Bayes:** luôn ghi ra tỉ lệ nền (base rate); tỉ số odds hậu nghiệm = tỉ số odds tiên nghiệm × tỉ số hợp lý.
- **LLN và CLT:** LLN nói trung bình mẫu ổn định dần; CLT nói *dao động* của nó (sau khi chuẩn hóa) có dạng phân phối chuẩn.
- **Rủi ro trong học máy** là một kỳ vọng; sai số trên tập huấn luyện chỉ là một giá trị mẫu của kỳ vọng đó.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Xác suất chỉ dùng cho sòng bạc." | Xác suất là toán học về sự bất định trong khoa học và học máy. |
| "Có LLN thì mẫu nhỏ cũng đã chính xác." | LLN là kết quả tiệm cận; tốc độ hội tụ và phương sai mới quyết định. |
| "Giá trị $$p$$ = $$P(\mathrm{null}\vert data)$$." | Sai, đại lượng đó là xác suất hậu nghiệm. |
| "Mất mát trên tập huấn luyện = rủi ro thật." | Mất mát huấn luyện là đại lượng thực nghiệm; rủi ro là kỳ vọng. |
| "CLT nói dữ liệu có phân phối chuẩn." | CLT nói về phân phối *của trung bình mẫu*. |

---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và trực giác**, không thay chứng minh hay tài liệu chuẩn. Chi tiết xếp hạng: `research/video-research/probability-data-science/`.

**Thứ tự xem gợi ý**

1. **CORE** — 3Blue1Brown — Bayes theorem (the geometry of Bayesian update): [https://www.youtube.com/watch?v=HZGCoVF3YvM](https://www.youtube.com/watch?v=HZGCoVF3YvM).
2. **FOUNDATION** — 3Blue1Brown — Binomial distributions | Probabilities of probabilities: [https://www.youtube.com/watch?v=8idr1WZ1A7Q](https://www.youtube.com/watch?v=8idr1WZ1A7Q).
3. **FOUNDATION** — Harvard Stat 110 (Blitzstein) — course / lecture portal: [https://stat110.net/](https://stat110.net/).
4. **FOUNDATION** — Harvard Stat 110 YouTube playlist: [https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo).
5. **ORIENTATION / hygiene** — Veritasium — The Bayesian trap (base rates): [https://www.youtube.com/watch?v=R13BD8qKeTg](https://www.youtube.com/watch?v=R13BD8qKeTg).
6. **ORIENTATION** — Khan Academy — Central limit theorem overview: [https://www.youtube.com/watch?v=YAlJCEDH2uY](https://www.youtube.com/watch?v=YAlJCEDH2uY).

Danh mục URL đầy đủ: `research/video-research/probability-data-science/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/probability-data-science/transcripts/` · trạng thái: `research/video-research/probability-data-science/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/probability-data-science_HZGCoVF3YvM_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

Danh mục URL đầy đủ (mọi link tìm được khi nghiên cứu video): `research/video-research/probability-data-science/references.md`.

### Video (lộ trình chính)

1. 3Blue1Brown — Bayes theorem (the geometry of Bayesian update) — https://www.youtube.com/watch?v=HZGCoVF3YvM
2. 3Blue1Brown — Binomial distributions | Probabilities of probabilities — https://www.youtube.com/watch?v=8idr1WZ1A7Q
3. Harvard Stat 110 (Blitzstein) — course / lecture portal — https://stat110.net/
4. Harvard Stat 110 YouTube playlist — https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo
5. Veritasium — The Bayesian trap (base rates) — https://www.youtube.com/watch?v=R13BD8qKeTg
6. Khan Academy — Central limit theorem overview — https://www.youtube.com/watch?v=YAlJCEDH2uY
7. StatQuest — Maximum likelihood fundamentals — https://www.youtube.com/watch?v=XepXtl9YKwc
8. MIT 6.041 Probabilistic Systems Analysis (OCW) — https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/

### Video (tìm thêm / phụ)

9. 3Blue1Brown lockdown math / related probability episodes — https://www.3blue1brown.com/

### Bài báo, sách, OCW và web

10. Wasserman — All of Statistics (Springer): https://link.springer.com/book/10.1007/978-0-387-21736-9
11. Wikipedia — Law of large numbers: https://en.wikipedia.org/wiki/Law_of_large_numbers
12. Wikipedia — Central limit theorem: https://en.wikipedia.org/wiki/Central_limit_theorem
13. Wikipedia — Concentration inequality: https://en.wikipedia.org/wiki/Concentration_inequality
14. Blitzstein & Hwang — Introduction to Probability (Stat 110): https://stat110.net/

### Trong khóa

15. Khóa: [Đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/), [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/), [Lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/). Gói: `research/video-research/probability-data-science/`.

## Hướng đi tiếp

- [Lý thuyết số → Mật mã]({{ site.baseurl }}/contents/vi/chapter03/03_05_Number_Theory_Cryptography/) hoặc [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/).  
- Tự viết lại ý chính của bài trong một đoạn văn, và ghi ra một câu hỏi bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước**: [Bayes theorem, the geometry of changing beliefs](https://www.youtube.com/watch?v=HZGCoVF3YvM) (3Blue1Brown, tiếng Anh). Giải thích công thức Bayes bằng hình học, với ví dụ về tỉ lệ nền. Nên xem trước khi đọc §5 và §7.
- [The Bayesian Trap](https://www.youtube.com/watch?v=R13BD8qKeTg) (Veritasium, tiếng Anh). Ví dụ xét nghiệm bệnh cho thấy trực giác dễ sai khi bỏ qua tỉ lệ nền, và cách suy nghĩ theo Bayes. Hợp với §7.
- [Binomial distributions | Probabilities of probabilities, part 1](https://www.youtube.com/watch?v=8idr1WZ1A7Q) (3Blue1Brown, tiếng Anh). Dùng phân phối nhị thức để so sánh các đánh giá có số lượt khác nhau. Góc nhìn bổ sung cho §1 và §5.
