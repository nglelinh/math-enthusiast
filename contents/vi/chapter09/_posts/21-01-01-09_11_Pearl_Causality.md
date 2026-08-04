---
layout: post
title: "Pearl và Toán học Nhân quả (Turing 2011)"
chapter: '09'
order: 11
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**Judea Pearl** nhận **A.M. Turing Award 2011**

> “for fundamental contributions to artificial intelligence through the development of a calculus for probabilistic and causal reasoning.”  
> — [ACM Turing Award](https://amturing.acm.org/)

Thống kê cổ điển giỏi mô tả **liên kết** dưới phân phối quan sát. Pearl đặt câu hỏi cứng hơn: **nếu can thiệp**, hệ đổi thế nào? **Nếu ngược lại quá khứ**, điều gì đã xảy ra? Ông đưa **đồ thị**, **do-calculus**, và **nấc thang nhân quả** vào AI và khoa học dữ liệu, biến “correlation ≠ causation” từ khẩu hiệu thành **đại số suy diễn**. Bài này dựng toán–logic của nhân quả cho Math Enthusiast: Bayesian networks, $$do(x)$$, confounding, counterfactual—và ranh giới khi data + graph giả định không đủ. Cầu: [xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/), [toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

---

## Mục tiêu học tập

Sau bài, bạn có thể phân biệt ba nấc **association / intervention / counterfactual**; đọc **Bayesian network** như factorization $$p(x_1,\ldots,x_n)=\prod_i p(x_i\mid \mathrm{pa}(i))$$ trên DAG; giải thích **confounder** và vì sao hồi quy quan sát có thể lệch tác động nhân quả; phát biểu ý toán tử $$do(X=x)$$ và khác conditioning $$p(y\mid x)$$; nêu **backdoor** ở mức khẩu hiệu (chặn mọi đường back-door từ $$X$$ sang $$Y$$ không tạo đường mới); mô tả counterfactual như lớp suy diễn cần mô hình cấu trúc; phê slogan “big data thay nhân quả” và “DAG = sự thật thế giới”.

**Kiến thức nền.** Xác suất có điều kiện; độc lập; đồ thị có hướng cơ bản. Không cần measure theory.

---

## 1. Ba nấc thang nhân quả

Pearl phổ biến hình ảnh **ladder of causation**:

1. **Association (thấy):** $$p(y\mid x)$$ — cho $$X=x$$ quan sát, $$Y$$ ra sao?  
2. **Intervention (làm):** $$p(y\mid do(x))$$ — nếu *ép* $$X=x$$, $$Y$$ ra sao?  
3. **Counterfactual (tưởng):** $$p(y_x\mid x',y')$$ — đã thấy $$(x',y')$$, *nếu* $$X$$ là $$x$$ thì $$Y$$?

Học máy chuẩn (ERM, supervised) sống chủ yếu nấc 1 dưới i.i.d. Chính sách, y học, kinh tế, fairness cần nấc 2–3. Turing 2011 vinh danh việc cho nấc 2–3 **cú pháp và tiên đề**, không chỉ narrative.

### Ví dụ mở đầu: kem và cháy nắng

Bán kem tương quan cháy nắng. Conditioning: biết bán kem cao có thể dự đoán cháy nắng (cùng mùa). Intervention: *ép* mở thêm cửa hàng kem mùa đông không tạo UV. Counterfactual: “nếu hôm đó không có xe kem, liệu tôi có cháy nắng?” cần mô hình cơ chế (mặt trời, hành vi…).

---

## 2. Bayesian networks: xác suất có xương đồ thị

### Factorization

Cho DAG $$G$$ trên biến $$X_1,\ldots,X_n$$, **Bayesian network** gán

$$
p(x_1,\ldots,x_n)=\prod_{i=1}^n p\big(x_i\mid x_{\mathrm{pa}(i)}\big),
$$

với $$\mathrm{pa}(i)$$ cha của $$i$$. Độc lập có điều kiện đọc từ **d-separation** trên đồ thị. Suy diễn (exact/approximate) trên mạng là chương trình thuật toán—Pearl đóng góp **belief propagation** / message passing trên trees và văn hóa graphical models.

### Vì sao đồ thị quan trọng hơn “chỉ joint table”

Joint trên $$n$$ biến nhị phân có $$2^n-1$$ bậc tự do; mạng thưa hóa bằng local conditionals. Đây vừa nén, vừa **giả định mô hình** có thể sai. LO6: BN không miễn nhiễm misspecification; nó làm giả định *nhìn thấy được*.

Graphical models còn nuôi CRF, topic models, và một phần suy diễn trong AI cổ điển trước sóng deep learning. [Toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) đặt chúng cạnh net: biểu diễn khác, câu hỏi suy diễn khác.

---

## 3. Can thiệp và $$do$$-operator

### Cắt cạnh vào $$X$$

$$do(X=x)$$ nghĩa là **can thiệp**: xóa phương trình/cạnh xác định $$X$$ từ cha, gán $$X=x$$, giữ các cơ chế khác. Phân phối can thiệp $$p(y\mid do(x))$$ *không* đồng nhất $$p(y\mid x)$$ khi có confounding.

### Confounding

Biến $$Z$$ ảnh hưởng cả $$X$$ và $$Y$$ tạo **đường back-door**. Ví dụ: điều trị $$X$$, outcome $$Y$$, mức độ bệnh nền $$Z$$ ảnh hưởng cả hai. Bệnh nhân nặng vừa hay được trị vừa outcome xấu—hồi quy thô có thể đảo dấu tác động.

**Adjustment** (đơn giản): nếu $$Z$$ thỏa tiêu chí back-door,

$$
p(y\mid do(x))=\sum_z p(y\mid x,z)\,p(z)
$$

(dạng rời rạc). Khác $$p(y\mid x)=\sum_z p(y\mid x,z)p(z\mid x)$$—trọng số $$p(z)$$ vs $$p(z\mid x)$$ là toàn bộ câu chuyện.

### do-calculus

Pearl cho **ba quy tắc** viết lại biểu thức $$do$$ thành xác suất quan sát dưới giả định đồ thị, khi có thể. Đây là **đại số suy diễn**: không phải mọi $$p(y\mid do(x))$$ đều identify từ data quan sát; do-calculus + tiêu chí đồ thị nói *khi nào* identify được và *công thức nào*.

Identification theory (cũng với instrumental variables, front-door, …) là toán logic–xác suất, không phải “chạy regression mạnh hơn”.

---

## 4. Structural Causal Models (SCM)

### Phương trình cơ chế

Mỗi biến $$X_i:=f_i(\mathrm{Pa}_i,U_i)$$ với nhiễu ngoại sinh $$U_i$$. Joint quan sát sinh từ nhiễu và cơ chế. Can thiệp thay $$f_X$$ bằng hằng. Counterfactual: cố định nhiễu (thế giới đã thực hiện), đổi cơ chế, đọc lại $$Y$$.

Ba nấc tương ứng sức mạnh giả định:

| Nấc | Cần |
|-----|-----|
| Association | Mẫu từ joint |
| Intervention | Graph / giả định cơ chế đủ để identify |
| Counterfactual | SCM chi tiết hơn (đôi khi unit-level) |

### Potential outcomes

Ngôn ngữ Neyman–Rubin $$Y(1),Y(0)$$ song song. Pearl nhấn biểu diễn đồ thị và thuật toán suy diễn; thống kê nhân quả nhấn thiết kế thí nghiệm, matching, IPW. Khóa học không “chọn phe”: cần biết **cùng câu hỏi**, hai dialect.

---

## 5. Nhân quả và học máy

### Khi i.i.d. dự đoán đủ

Gợi ý phim, nhận diện ảnh trong phân phối train—nấc 1 thường đủ nếu deployment ≈ train.

### Khi chính sách đổi phân phối

Giá, điều trị, ranking thay đổi hành vi ⇒ shift. Mô hình chỉ fit $$p(y\mid x)$$ có thể gãy khi $$p(x)$$ hoặc cơ chế đổi. **Invariant predictors**, causal representation learning, off-policy evaluation là chương trình nghiên cứu—một phần lấy cảm hứng trực tiếp từ SCM.

### Fairness và giải thích

“Nếu đổi thuộc tính nhạy cảm, outcome có đổi không?” mang hình counterfactual. Formal hóa khó: graph nào? nhiễu nào? Turing-era Pearl không kết thúc tranh luận đạo đức; ông cho **ngôn ngữ** để tranh luận không chỉ slogan.

### Deep learning + causality

Net xấp xỉ hàm; causality hỏi *hàm nào là cơ chế* và *thí nghiệm giả định nào hợp lệ*. Kết hợp (causal discovery + representation) còn non trẻ so với supervised scale. Xem [Deep Learning Trio]({{ site.baseurl }}/contents/vi/chapter09/09_12_Deep_Learning_Trio/) để không nhầm “scale” với “identify”.

---

## 6. Causal discovery: khi graph chưa cho sẵn

Nhiều ứng dụng *không* biết DAG. Thuật toán discovery (PC, FCI, score-based, …) dùng độc lập có điều kiện và giả định (causal sufficiency, faithfulness) để khôi phục lớp Markov tương đương. Giới hạn:

- **Markov equivalence:** nhiều DAG cùng độc lập—không phân biệt bằng observational data đơn thuần.  
- **Latent confounding** phá sufficiency.  
- **Finite sample** error độc lập tests.

LO6: paper “we learned the causal graph from data” cần checklist giả định, equivalence class, và validation can thiệp nếu có.

---

## 7. Nhầm lẫn thường gặp

| Tuyên bố | Chỉnh |
|----------|--------|
| “$$p(y\mid x)=p(y\mid do(x))$$ luôn.” | Chỉ dưới giả định (không confounding, …). |
| “Big data xóa nhu cầu nhân quả.” | Thêm mẫu không xóa bias cấu trúc confounding. |
| “DAG là sự thật ontology.” | Mô hình; có thể sai; hữu ích khi tường minh. |
| “Counterfactual = prediction tương lai.” | Ngược lại thế giới; khác forecast. |
| “Pearl phủ nhận RCT.” | RCT là gold standard can thiệp; lý thuyết nói thêm *quan sát* khi nào đủ. |
| “Bayesian network = Bayesian inference luôn.” | “Bayesian” ở đây là factorization xác suất; prior/posterior là chuyện khác. |
| “Correlation never useful.” | Nấc 1 hữu ích cho dự đoán; đừng *diễn giải* như can thiệp. |

---

## 8. Miniatura toán: back-door một dòng

Giả sử $$Z$$ chặn mọi đường back-door từ $$X$$ sang $$Y$$ và không có descendant “xấu” của $$X$$ trong $$Z$$ (điều kiện chuẩn). Khi đó average causal effect rời rạc:

$$
\mathbb{E}[Y\mid do(x)]=\sum_z \mathbb{E}[Y\mid x,z]\,p(z).
$$

So sánh với $$\sum_z \mathbb{E}[Y\mid x,z]\,p(z\mid x)$$. Nếu $$Z$$ liên quan $$X$$, hai trọng số khác nhau—**cùng regression nội bộ**, **khác average**. Đây là chỗ seminar có thể tính số trên bảng 2×2×2 nhỏ.

---

## 9. Front-door, instrument, và giới hạn identify

Không phải mọi graph cho phép back-door. **Front-door** dùng trung gian $$M$$ trên đường nhân quả $$X\to M\to Y$$ khi back-door bị block bởi latent. **Instrumental variables** (kinh tế lượng) ép exogenous shock vào $$X$$. Cả hai nhắc: identification là **định lý về model class**, không phải nút “causal=True” trong thư viện.

Khi không identify được từ quan sát, trung thực khoa học là nói *partial identification* (bounds) hoặc thiết kế thí nghiệm. Pearl không xóa RCT; ông mở rộng ngôn ngữ khi RCT đắt hoặc bất khả đạo đức. [Valiant PAC]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/) hỏi học trong i.i.d.; Pearl hỏi *đổi cơ chế*—hai bài toán, đừng gộp.

### Transportability

Đôi khi ta có RCT ở quần thể A và quan sát ở B. **Transport** công thức nhân quả qua domain shift dưới giả định đồ thị selection—chương trình hiện đại gần OOD ML. Lại một chỗ checklist LO6: giả định selection có test được không?

---

## Bài tập

1. Viết một ví dụ đời thường ba nấc association / intervention / counterfactual.  
2. Cho joint factorization theo chain $$X\to Y\to Z$$; viết $$p(x,y,z)$$.  
3. Giải thích một đoạn vì sao $$p(y\mid x)$$ khác $$p(y\mid do(x))$$ khi có confounder $$Z\to X$$, $$Z\to Y$$.  
4. Phát biểu back-door criterion mức khẩu hiệu; áp vào ví dụ điều trị–bệnh nền–outcome.  
5. **≤200 từ:** Vì sao equivalence class cản “học duy nhất một DAG” từ quan sát.  
6. Nối [xác suất–data]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/): một câu độc lập có điều kiện vs d-separation.  
7. **Seminar:** Chọn headline “AI finds what causes Y”. Checklist LO6: nấc thang? graph assumed? RCT? only observational?

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/pearl-causality/`.

**Khẩu hiệu từ gói nghiên cứu**

- Pearl Turing 2011: nhân quả, Bayesian nets, do-calculus.

**Thứ tự xem gợi ý**

1. **ORIENTATION** — YouTube search: Pearl causality Turing: [https://www.youtube.com/watch?v=iNm4nFBFmvo](https://www.youtube.com/watch?v=iNm4nFBFmvo).  

**Cổng chính thức / tài liệu**

- Pearl Turing page: https://amturing.acm.org/award_winners/pearl_2658896.cfm  

Danh mục URL đầy đủ: `research/video-research/pearl-causality/references.md`.


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/pearl-causality/transcripts/` · trạng thái: `research/video-research/pearl-causality/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/pearl-causality_iNm4nFBFmvo_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu tham khảo


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/pearl-causality/references.md`.

1. Pearl Turing page — https://amturing.acm.org/award_winners/pearl_2658896.cfm  
2. Wikipedia — Judea Pearl — https://en.wikipedia.org/wiki/Judea_Pearl  
3. Wikipedia — Causal model — https://en.wikipedia.org/wiki/Causal_model  
4. Wikipedia — Bayesian network — https://en.wikipedia.org/wiki/Bayesian_network  
5. Wikipedia — Do-calculus — https://en.wikipedia.org/wiki/Do_calculus  
6. Book of Why (popular entry) — https://en.wikipedia.org/wiki/The_Book_of_Why  
7. UCLA Cognitive Systems Lab (Pearl) — http://bayes.cs.ucla.edu/jp_home.html  
8. YouTube search: Pearl causality Turing — https://www.youtube.com/watch?v=iNm4nFBFmvo  
9. Thư mục gói: `research/video-research/pearl-causality/`.

1. ACM Turing Award — Judea Pearl (2011).  
2. Pearl — *Causality* (Cambridge); *The Book of Why* (phổ thông có xương).  
3. Pearl, Glymour, Jewell — *Causal Inference in Statistics: A Primer*.  
4. Peters, Janzing, Schölkopf — *Elements of Causal Inference* (MIT).  
5. Khóa: [xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/); [toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/); [Valiant/PAC]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/); [DL Trio]({{ site.baseurl }}/contents/vi/chapter09/09_12_Deep_Learning_Trio/).

---

## Hướng đi tiếp

- Supervised i.i.d. foundations: [Valiant]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).  
- Biểu diễn sâu: [Bengio–Hinton–LeCun]({{ site.baseurl }}/contents/vi/chapter09/09_12_Deep_Learning_Trio/).  
- Thực hành: bảng contingency nhỏ; so $$p(y\mid x)$$ vs adjustment formula.  
- Đọc: *Book of Why* chọn chương → Primer do-calculus → một paper causal ML.  
- Tiếp: [Deep Learning Trio]({{ site.baseurl }}/contents/vi/chapter09/09_12_Deep_Learning_Trio/).
