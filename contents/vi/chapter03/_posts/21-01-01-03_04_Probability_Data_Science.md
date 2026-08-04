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

Mô hình 99% trên tập huấn luyện vẫn có thể hỏng khi lên production. Thăm dò nghìn người có thể dự đoán bầu cử—hoặc bẽ mặt tác giả. Bộ lọc spam không lỗi hôm qua có thể trượt chiến dịch mai. **Xác suất** là ngôn ngữ biến những thất bại đó thành đối tượng định nghĩa, đo và đôi khi chặn trên được.

**Lộ trình:** ngẫu nhiên như mô hình → kỳ vọng & phương sai → LLN & CLT → suy diễn → rủi ro trong ML → cảnh báo nhân quả → nhầm lẫn.

Bài này không phải cả khóa xác suất. Đây là bản đồ **vì sao xác suất trở thành hệ điều hành của khoa học dữ liệu**.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phân biệt dữ liệu như con số cố định với dữ liệu như hiện thực của biến ngẫu nhiên.
- Nêu **luật số lớn (LLN)** và **định lý giới hạn trung tâm (CLT)** mức khẩu hiệu–công thức và chúng biện minh gì trong thực tiễn.
- Giải thích ước lượng, khoảng tin cậy và kiểm định như *suy diễn dưới bất định*, không phải chứng chỉ chân lý.
- Định nghĩa **rủi ro** như mất mát kỳ vọng và nối ERM với “loss trên tập train.”
- Nêu vì sao tương quan không phải nhân quả và vì sao dịch phân phối phá validation ngây thơ.
- Tránh “xác suất chỉ để đánh bạc” và “big data xóa hết bất định.”

**Kiến thức nền.** Trung bình, đếm. Hữu ích: [đại số tuyến tính]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/).

---

## 1. Bước mô hình hóa: dữ liệu ngẫu nhiên

Trong tính toán thuần, mảng số chỉ là mảng. Trong khoa học dữ liệu, ta thường xem $$X_1,\ldots,X_n$$ là **biến ngẫu nhiên**—có thể khác đi nếu thế giới lặp lại (hoặc rút từ một quá trình sinh dữ liệu).

Phân phối gán trọng số/mật độ cho kết quả. Bernoulli($$p$$); mật độ chuẩn

$$
f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\Bigl(-\frac{(x-\mu)^2}{2\sigma^2}\Bigr).
$$

**Cơ chế.**  
*Xác suất biến “điều đã xảy ra” thành “quá trình nào có thể sinh ra nó—và điều gì xảy ra tiếp.”*

---

## 2. Kỳ vọng, phương sai, đại số trung bình

$$\mathbb{E}[X]$$ là trung bình có trọng số xác suất. $$\mathrm{Var}(X)=\mathbb{E}[(X-\mathbb{E}X)^2]$$ đo phân tán. Tuyến tính của kỳ vọng

$$
\mathbb{E}[aX+bY]=a\mathbb{E}X+b\mathbb{E}Y
$$

giữ ngay cả khi phụ thuộc—công cụ mạnh cho lấy mẫu và thuật toán ngẫu nhiên. Phương sai thân thiện hơn khi độc lập: trung bình hóa làm giảm nhiễu.

A/B test, CTR, latency đều là ước lượng trung bình mẫu dưới nhiễu.

---

## 3. Luật số lớn: vì sao trung bình ổn định

**LLN (không chính thức).** Với i.i.d. kỳ vọng hữu hạn $$\mu$$,

$$
\bar{X}_n=\frac1n\sum_{i=1}^n X_i \to \mu
$$

(khi $$n\to\infty$$, theo các định lý chuẩn).

**Nuôi gì.** Thăm dò, Monte Carlo, nhiễu SGD trung bình hóa, tần suất thực nghiệm tiến tới xác suất thật—**khi** giả thiết i.i.d./ergodic xấp xỉ đúng.

**Không phải.** Không nói mẫu nhỏ đã “đủ”; không sửa bias dụng cụ; không giữ nguyên khi thế giới trôi (nonstationary).

---

## 4. CLT: vì sao chuông xuất hiện

**CLT (không chính thức).** Với i.i.d. phương sai $$\sigma^2$$ hữu hạn,

$$
\sqrt{n}\,\frac{\bar{X}_n-\mu}{\sigma}\ \xrightarrow{d}\ N(0,1).
$$

**Cơ chế.**  
*Tổng nhiều hiệu ứng nhỏ độc lập xấp xỉ Gaussian; do đó trung bình mẫu có phân phối lấy mẫu xấp xỉ chuẩn, cho phép sai số chuẩn cổ điển.*

Đó là lý do thống kê nhập môn ám ảnh $$z$$-score và sai số chuẩn $$\sigma/\sqrt{n}$$: CLT cung xấp xỉ phổ quát cho *phân phối của trung bình*, không cho phân phối của một quan sát đơn (có thể lệch, rời rạc, đuôi nặng).

**Cảnh báo.** Đuôi nặng, phụ thuộc, $$n$$ nhỏ phá cổ tích. Khoa học dữ liệu hiện đại thường dùng bootstrap và bất đẳng thức tập trung (Hoeffding, Bernstein, …) như họ hàng sắc hơn hoặc linh hoạt hơn.

---

## 5. Suy diễn: từ mẫu đến phát biểu

**Ước lượng điểm** cho một đoán $$\hat\theta$$ (trung bình mẫu cho $$\mu$$, MLE cho tham số mô hình). **Ước lượng khoảng** cho tập giá trị hợp lý với diễn giải tần suất được hiệu chỉnh dưới mô hình (khoảng tin cậy)—hoặc phát biểu độ tin cậy hậu nghiệm trong ngôn ngữ Bayes.

**Kiểm định giả thuyết** hình thức hóa “hiệu ứng này có phân biệt được với nhiễu dưới null không?” **$$p$$-value không phải** “xác suất null đúng”—chúng là xác suất đuôi của thống kê kiểm định dưới null. Đọc sai chúng là dịch văn hóa lan rộng.

**Likelihood.** Cho mô hình tham số $$p(x\mid\theta)$$, likelihood $$L(\theta)=\prod_i p(x_i\mid\theta)$$ chấm điểm mức $$\theta$$ giải thích mẫu. MLE và hậu nghiệm Bayes $$p(\theta\mid data)\propto L(\theta)p(\theta)$$ là hai triết lý suy diễn lớn chia cùng ngữ pháp xác suất.

**Cơ chế công nghệ.** Hệ gợi ý, mô hình tín dụng, điểm rủi ro y tế, nền tảng A/B đều chạy pipeline: họ mô hình → khớp mẫu → quy tắc quyết định có ý thức bất định.

---

## 6. Rủi ro học máy: mất mát kỳ vọng

Trong lý thuyết học thống kê, quy tắc dự đoán $$f$$ được chấm bằng **rủi ro**

$$
R(f)=\mathbb{E}\bigl[\ell(f(X),Y)\bigr],
$$

mất mát kỳ vọng trên một rút $$(X,Y)$$ ngẫu nhiên từ phân phối dữ liệu thật. Bạn không tính được $$R(f)$$ trực tiếp; chỉ thấy mẫu và **rủi ro thực nghiệm**

$$
\hat{R}_n(f)=\frac1n\sum_{i=1}^n \ell(f(X_i),Y_i).
$$

**ERM** (cực tiểu hóa rủi ro thực nghiệm) chọn $$f$$ trong lớp $$\mathcal{F}$$ để cực tiểu $$\hat{R}_n$$. Lý thuyết tổng quát hóa hỏi khi nào $$\hat{R}_n\approx R$$ đều trên $$\mathcal{F}$$—chiều VC, độ phức tạp Rademacher, ổn định, PAC-Bayes, và các câu chuyện double descent hiện đại đều sống ở đây.

Huấn luyện nơ-ron bằng SGD là tối ưu ngẫu nhiên xấp xỉ của rủi ro thực nghiệm; xác suất giải thích *nhiễu gradient* và *khe train–test*. Xem [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/) và [Lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

**Cơ chế.**  
*“Accuracy trên một dataset” là mẫu; “hiệu năng ngoài đời” là rủi ro. Xác suất là cầu—và nhãn cảnh báo.*

---

## 7. Phụ thuộc, Bayes, quyết định dưới bất định

Dữ liệu thật hiếm khi là đồng xu i.i.d. gọn:

- **Chuỗi thời gian** và dữ liệu không gian: phụ thuộc; biến thể CLT tồn tại nhưng công thức SE ngây thơ hỏng.  
- **Mô hình Bayes / phân cấp:** partial pooling; kiểm tra dự đoán hậu nghiệm.  
- **Lý thuyết quyết định:** chọn hành động cực tiểu chi phí kỳ vọng, không chỉ ước lượng tham số.  
- **Hiệu chỉnh (calibration):** xác suất dự đoán nên khớp tần suất thực nghiệm nếu hệ đáng tin.

Quy tắc Bayes

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
$$

là đại số cập nhật niềm tin. Bộ lọc spam, nguyên mẫu chẩn đoán y, nhiều hệ xếp hạng mang tinh thần Bayes—kể cả khi triển khai là mạng nơ-ron xuất logit.

---

## 8. Nhân quả, dịch phân phối, đạo đức bất định

**Tương quan ≠ nhân quả.** Liên hệ quan sát giữa kem và đuối nước không nghĩa kem gây đuối nước; nhiệt độ gây nhiễu cả hai. Suy diễn nhân quả (kết quả tiềm năng, DAG, biến công cụ) là xác suất với “phẫu thuật” can thiệp—không đi sâu ở đây, nhưng là vệ sinh trí tuệ bắt buộc cho tuyên bố khoa học dữ liệu.

**Distribution shift.** Nếu dữ liệu production $$P_{\mathrm{test}}$$ khác huấn luyện $$P_{\mathrm{train}}$$, bảo đảm rủi ro chuyển kém. Đó là chẩn đoán xác suất của một kiểu hỏng rất thực tiễn.

**Đạo đức.** Truyền thông bất định quan trọng: mô hình quá tự tin gây hại. Ràng buộc công bằng, cơ chế dữ liệu thiếu, thiên lệch chọn mẫu là bài toán đạo đức–kỹ thuật mang hình dạng xác suất.

---

## 9. Tập trung hữu hạn mẫu

Ngoài CLT cổ điển, bất đẳng thức kiểu Hoeffding cho bảo đảm hữu hạn $$n$$ tường minh: với biến i.i.d. bị chặn, trung bình tập trung mũ quanh kỳ vọng. Các công cụ này chống lưng lý thuyết học, thuật toán ngẫu nhiên, và tính công suất nền tảng A/B.

Văn hóa từ “$$n=30$$ nên chuẩn” sang “nêu giả thiết + tập trung/bootstrap/SE vững” là dấu hiệu data scientist cẩn thận. “Nhiều dữ liệu hơn” không tự xóa bias, shift, phụ thuộc hay cấu trúc adversarial.

---

### Khẩu hiệu xác suất (từ nghiên cứu video)

Xem [3B1B Bayes](https://www.youtube.com/watch?v=HZGCoVF3YvM) và [Veritasium — The Bayesian trap](https://www.youtube.com/watch?v=R13BD8qKeTg) trước phần suy diễn.

- **Vệ sinh Bayes:** luôn viết base rate; odds hậu nghiệm = odds tiên nghiệm × tỉ số likelihood.
- **LLN vs CLT:** LLN nói trung bình ổn định; CLT nói *dao động* (chuẩn hóa) trông Gaussian.
- **Rủi ro ML** là kỳ vọng; lỗi huấn luyện là một quỹ đạo mẫu của kỳ vọng đó.

## Nhầm lẫn thường gặp

| Khẳng định | Sửa |
|------------|-----|
| “Xác suất chỉ cho sòng bạc.” | Là toán bất định của khoa học và ML. |
| “LLN ⇒ mẫu nhỏ đã chính xác.” | LLN tiệm cận; tốc độ và phương sai quan trọng. |
| “$$p$$-value = $$P(\mathrm{null}\mid data)$$.” | Không—đó là hậu nghiệm. |
| “Train loss = rủi ro thật.” | Train là thực nghiệm; rủi ro là kỳ vọng. |
| “CLT nói dữ liệu chuẩn.” | CLT nói về phân phối *của trung bình*. |

---

## Bài tập

1. Xúc xắc công bằng: $$\mathbb{E}[X]$$, $$\mathrm{Var}(X)$$.  
2. Ba câu: vì sao trung bình thăm dò ổn định khi $$n$$ tăng—và một giả thiết có thể hỏng.  
3. $$\sigma=2$$: SE trung bình đổi thế nào từ $$n=100$$ sang $$400$$?  
4. Viết $$R(f)$$, $$\hat{R}_n(f)$$; một câu vì sao cực tiểu cái sau không tự động tối ưu cái trước.  
5. Sửa một câu báo chí sai về $$p$$-value.  
6. Ví dụ train và deploy khác phân phối.  
7. Nâng cao: Hoeffding và sự phụ thuộc mũ vào $$n$$.

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
- Viết lại cơ chế cốt lõi một đoạn; ghi một câu hỏi còn mở.
