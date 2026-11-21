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

Một mô hình đạt độ chính xác 99% trên tập huấn luyện vẫn có thể thất bại khi đưa vào sử dụng thật. Một cuộc thăm dò nghìn người có thể dự đoán đúng kết quả bầu cử, hoặc sai đến mức người làm phải xấu hổ. Một bộ lọc thư rác hôm qua không lọt thư nào vẫn có thể bỏ sót đợt thư rác ngày mai. **Xác suất** là ngôn ngữ giúp ta định nghĩa những thất bại đó, đo chúng, và đôi khi chặn trên được chúng.

**Lộ trình:** xem sự ngẫu nhiên như một mô hình → kỳ vọng và phương sai → luật số lớn và định lý giới hạn trung tâm → suy diễn thống kê → rủi ro trong học máy → lưu ý về nhân quả → nhầm lẫn thường gặp.

Đây không phải cả một khóa học xác suất. Bài này giải thích **vì sao xác suất trở thành nền tảng của khoa học dữ liệu**.

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

## 1. Bước mô hình hóa: xem dữ liệu là ngẫu nhiên

Khi chỉ tính toán, một dãy số chỉ là một dãy số. Trong khoa học dữ liệu, ta thường xem $$X_1,\ldots,X_n$$ là các **biến ngẫu nhiên**: nếu thế giới lặp lại, hoặc nếu ta rút mẫu lại từ cùng một quá trình sinh dữ liệu, các giá trị này có thể khác đi.

Một phân phối gán xác suất hoặc mật độ cho các kết quả có thể xảy ra. Ví dụ phân phối Bernoulli($$p$$), hay phân phối chuẩn với mật độ

$$
f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\Bigl(-\frac{(x-\mu)^2}{2\sigma^2}\Bigr).
$$

**Ý chính.**  
*Xác suất chuyển câu hỏi "điều gì đã xảy ra" thành "quá trình nào có thể sinh ra điều đó, và tiếp theo sẽ xảy ra gì".*

---

## 2. Kỳ vọng, phương sai và tính toán với trung bình

$$\mathbb{E}[X]$$ là trung bình có trọng số theo xác suất. $$\mathrm{Var}(X)=\mathbb{E}[(X-\mathbb{E}X)^2]$$ đo độ phân tán. Kỳ vọng có tính tuyến tính

$$
\mathbb{E}[aX+bY]=a\mathbb{E}X+b\mathbb{E}Y
$$

và tính chất này đúng cả khi các biến phụ thuộc nhau. Đây là công cụ mạnh cho việc lấy mẫu và cho các thuật toán ngẫu nhiên. Phương sai dễ tính hơn khi các biến độc lập: lấy trung bình nhiều quan sát độc lập giúp giảm nhiễu.

Thử nghiệm A/B, tỉ lệ nhấp chuột (CTR), độ trễ hệ thống đều là những bài toán ước lượng trung bình mẫu khi có nhiễu.

---

## 3. Luật số lớn: vì sao trung bình ổn định

**LLN (phát biểu không chính thức).** Với các biến độc lập cùng phân phối (i.i.d.) có kỳ vọng hữu hạn $$\mu$$,

$$
\bar{X}_n=\frac1n\sum_{i=1}^n X_i \to \mu
$$

(khi $$n\to\infty$$, theo nghĩa của các định lý chuẩn).

**Ứng dụng.** Thăm dò dư luận, phương pháp Monte Carlo, việc nhiễu của SGD bị triệt tiêu khi lấy trung bình, tần suất thực nghiệm tiến dần tới xác suất thật. Tất cả chỉ đúng **khi** giả thiết i.i.d. (hoặc ergodic) gần đúng với thực tế.

**Những gì LLN không nói.** LLN không nói một mẫu nhỏ là "đủ". Nó không sửa được sai lệch hệ thống của dụng cụ đo. Và nó không còn áp dụng nguyên vẹn khi thế giới thay đổi theo thời gian (dữ liệu không dừng).

---

### Video ngắn: Tổng xúc xắc thành hình chuông

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/clt-dice-bell_vi.mp4"></video>
</div>

Phân phối chính xác của tổng $$n$$ xúc xắc đều, co giãn về cùng độ rộng, với $$n = 1, 2, 3, 5, 10, 30$$. Một xúc xắc thì đều; tổng của nhiều xúc xắc bám sát đường chuông chuẩn.


### Tự tay thử: Cộng xúc xắc và xem đường chuông

<div class="mex-explainer" data-mex="clt" data-lang="vi"></div>


## 4. CLT: vì sao xuất hiện hình chuông

**CLT (phát biểu không chính thức).** Với các biến i.i.d. có phương sai $$\sigma^2$$ hữu hạn,

$$
\sqrt{n}\,\frac{\bar{X}_n-\mu}{\sigma}\ \xrightarrow{d}\ N(0,1).
$$

**Ý chính.**  
*Tổng của nhiều tác động nhỏ, độc lập có phân phối xấp xỉ chuẩn (Gauss). Vì vậy trung bình mẫu có phân phối mẫu xấp xỉ chuẩn, và ta dùng được công thức sai số chuẩn cổ điển.*

Đó là lý do thống kê nhập môn dùng nhiều đến điểm $$z$$ và sai số chuẩn $$\sigma/\sqrt{n}$$. CLT cho một xấp xỉ dùng được rất rộng rãi cho *phân phối của trung bình mẫu*, chứ không cho phân phối của từng quan sát riêng lẻ (vốn có thể lệch, rời rạc, hay có đuôi nặng).

**Lưu ý.** Khi phân phối có đuôi nặng, khi các quan sát phụ thuộc nhau, hoặc khi $$n$$ nhỏ, xấp xỉ này có thể sai. Khoa học dữ liệu hiện đại thường dùng thêm bootstrap và các bất đẳng thức tập trung (Hoeffding, Bernstein, …) như những công cụ chặt chẽ hơn hoặc linh hoạt hơn.

---

## 5. Suy diễn: từ mẫu đến kết luận

**Ước lượng điểm** cho một giá trị dự đoán $$\hat\theta$$ (trung bình mẫu để ước lượng $$\mu$$, ước lượng hợp lý cực đại (MLE) cho tham số của mô hình). **Ước lượng khoảng** cho một tập các giá trị hợp lý, với cách hiểu theo tần suất dựa trên mô hình (khoảng tin cậy), hoặc một phát biểu về độ tin hậu nghiệm theo ngôn ngữ Bayes.

**Kiểm định giả thuyết** đặt câu hỏi một cách chính xác: "nếu giả thuyết không (null) đúng, hiệu ứng này có phân biệt được với nhiễu không?" **Giá trị $$p$$ không phải** là "xác suất giả thuyết không đúng". Nó là xác suất phần đuôi của thống kê kiểm định khi giả thuyết không đúng. Hiểu sai giá trị $$p$$ là một lỗi rất phổ biến.

**Hàm hợp lý.** Với một mô hình tham số $$p(x\mid\theta)$$, hàm hợp lý $$L(\theta)=\prod_i p(x_i\mid\theta)$$ đo mức độ $$\theta$$ giải thích được mẫu. MLE và phân phối hậu nghiệm Bayes $$p(\theta\mid data)\propto L(\theta)p(\theta)$$ là hai trường phái suy diễn lớn, dùng chung ngôn ngữ xác suất.

**Trong công nghệ.** Hệ gợi ý, mô hình chấm điểm tín dụng, điểm rủi ro y tế, nền tảng thử nghiệm A/B đều chạy theo cùng một quy trình: chọn họ mô hình → khớp mô hình với mẫu → đưa ra quy tắc quyết định có tính đến bất định.

---

## 6. Rủi ro trong học máy: mất mát kỳ vọng

Trong lý thuyết học thống kê, một quy tắc dự đoán $$f$$ được đánh giá bằng **rủi ro**

$$
R(f)=\mathbb{E}\bigl[\ell(f(X),Y)\bigr],
$$

tức là mất mát kỳ vọng trên một cặp $$(X,Y)$$ rút ngẫu nhiên từ phân phối dữ liệu thật. Bạn không tính trực tiếp được $$R(f)$$; bạn chỉ có mẫu và **rủi ro thực nghiệm**

$$
\hat{R}_n(f)=\frac1n\sum_{i=1}^n \ell(f(X_i),Y_i).
$$

**ERM** (cực tiểu hóa rủi ro thực nghiệm) chọn $$f$$ trong lớp hàm $$\mathcal{F}$$ sao cho $$\hat{R}_n$$ nhỏ nhất. Lý thuyết tổng quát hóa hỏi khi nào $$\hat{R}_n\approx R$$ đều trên toàn bộ $$\mathcal{F}$$. Chiều VC, độ phức tạp Rademacher, tính ổn định, PAC-Bayes và các nghiên cứu hiện đại về hiện tượng "double descent" đều thuộc về câu hỏi này.

Huấn luyện mạng nơ-ron bằng SGD là một cách tối ưu ngẫu nhiên, gần đúng, cho rủi ro thực nghiệm. Xác suất giải thích *nhiễu của gradient* và *khoảng cách giữa kết quả trên tập huấn luyện và tập kiểm tra*. Xem [Tối ưu]({{ site.baseurl }}/contents/vi/chapter03/03_07_Optimization_Operations_AI/) và [Lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

**Ý chính.**  
*"Độ chính xác trên một tập dữ liệu" là một mẫu; "hiệu quả ngoài đời thật" là rủi ro. Xác suất là cầu nối giữa hai thứ đó, và cũng là lời cảnh báo.*

---

## 7. Sự phụ thuộc, Bayes, và ra quyết định khi có bất định

Dữ liệu thật hiếm khi giống những lần tung đồng xu i.i.d. gọn gàng:

- **Chuỗi thời gian** và dữ liệu không gian: các quan sát phụ thuộc nhau; vẫn có các phiên bản CLT cho trường hợp này, nhưng công thức sai số chuẩn đơn giản không còn đúng.  
- **Mô hình Bayes và mô hình phân cấp:** gộp thông tin một phần giữa các nhóm (partial pooling); kiểm tra mô hình bằng dự đoán hậu nghiệm.  
- **Lý thuyết quyết định:** chọn hành động có chi phí kỳ vọng nhỏ nhất, không chỉ dừng ở việc ước lượng tham số.  
- **Hiệu chỉnh (calibration):** nếu hệ thống đáng tin, xác suất nó dự đoán phải khớp với tần suất quan sát được.

Công thức Bayes

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
$$

cho biết cách cập nhật niềm tin khi có bằng chứng mới. Bộ lọc thư rác, các hệ chẩn đoán y khoa thử nghiệm, nhiều hệ xếp hạng đều theo tinh thần Bayes, kể cả khi phần cài đặt là một mạng nơ-ron xuất ra logit.

---

## 8. Nhân quả, dịch chuyển phân phối và trách nhiệm khi có bất định

**Tương quan không phải nhân quả.** Số kem bán ra và số vụ đuối nước cùng tăng, nhưng điều đó không có nghĩa ăn kem gây đuối nước; nhiệt độ cao ảnh hưởng đến cả hai. Suy diễn nhân quả (kết quả tiềm năng, đồ thị DAG, biến công cụ) là xác suất cộng thêm cách mô tả các "can thiệp". Bài này không đi sâu, nhưng đây là hiểu biết bắt buộc trước khi đưa ra bất kỳ kết luận nào từ dữ liệu.

**Dịch chuyển phân phối.** Nếu phân phối dữ liệu khi sử dụng thật $$P_{\mathrm{test}}$$ khác phân phối huấn luyện $$P_{\mathrm{train}}$$, các bảo đảm về rủi ro không còn chuyển sang được. Đây là cách xác suất mô tả một kiểu thất bại rất thường gặp trong thực tế.

**Trách nhiệm.** Cách truyền đạt sự bất định rất quan trọng: một mô hình quá tự tin có thể gây hại. Các ràng buộc về công bằng, cơ chế gây thiếu dữ liệu, thiên lệch chọn mẫu đều là những bài toán vừa đạo đức vừa kỹ thuật, và đều có dạng bài toán xác suất.

---

## 9. Bất đẳng thức tập trung với mẫu hữu hạn

Ngoài CLT cổ điển, các bất đẳng thức kiểu Hoeffding cho bảo đảm tường minh với $$n$$ hữu hạn: với các biến i.i.d. bị chặn, xác suất trung bình mẫu lệch xa kỳ vọng giảm theo hàm mũ. Các công cụ này là nền tảng cho lý thuyết học máy, cho các thuật toán ngẫu nhiên, và cho việc tính cỡ mẫu cần thiết trong các nền tảng thử nghiệm A/B.

Một nhà khoa học dữ liệu cẩn thận không dừng ở quy tắc "$$n=30$$ là đủ để coi như chuẩn". Họ nêu rõ giả thiết, rồi dùng bất đẳng thức tập trung, bootstrap hoặc sai số chuẩn vững. "Thêm dữ liệu" không tự xóa được sai lệch, dịch chuyển phân phối, sự phụ thuộc hay dữ liệu đối kháng.

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
| "Giá trị $$p$$ = $$P(\mathrm{null}\mid data)$$." | Sai, đại lượng đó là xác suất hậu nghiệm. |
| "Mất mát trên tập huấn luyện = rủi ro thật." | Mất mát huấn luyện là đại lượng thực nghiệm; rủi ro là kỳ vọng. |
| "CLT nói dữ liệu có phân phối chuẩn." | CLT nói về phân phối *của trung bình mẫu*. |

---

## Bài tập

1. Với một con xúc xắc cân đối, tính $$\mathbb{E}[X]$$ và $$\mathrm{Var}(X)$$.  
2. Viết ba câu giải thích vì sao kết quả trung bình của một cuộc thăm dò ổn định dần khi $$n$$ tăng, và nêu một giả thiết có thể không đúng.  
3. Với $$\sigma=2$$: sai số chuẩn của trung bình mẫu thay đổi thế nào khi $$n$$ tăng từ $$n=100$$ lên $$400$$?  
4. Viết công thức $$R(f)$$ và $$\hat{R}_n(f)$$; giải thích trong một câu vì sao cực tiểu hóa đại lượng sau không tự động tối ưu đại lượng trước.  
5. Tìm và sửa một câu báo chí hiểu sai về giá trị $$p$$.  
6. Cho một ví dụ trong đó dữ liệu huấn luyện và dữ liệu khi triển khai có phân phối khác nhau.  
7. Nâng cao: bất đẳng thức Hoeffding và sự phụ thuộc theo hàm mũ vào $$n$$.

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
