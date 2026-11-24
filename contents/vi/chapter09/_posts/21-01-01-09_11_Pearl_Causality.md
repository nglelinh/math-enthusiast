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

Hãy thử đối mặt với một nghịch lý từng khiến cả giới y khoa và thống kê đau đầu (**Nghịch lý Simpson**): một bệnh viện tổng hợp dữ liệu điều trị sỏi thận và thấy Phương pháp A có tỉ lệ khỏi bệnh cao hơn Phương pháp B ở **cả** nhóm bệnh nhân sỏi nhỏ lẫn nhóm bệnh nhân sỏi lớn. Thế nhưng khi gộp chung toàn bộ hồ sơ lại, Phương pháp B lại bất ngờ có tỉ lệ khỏi cao hơn Phương pháp A! Nếu chỉ nhìn vào bảng số liệu thống kê thuần túy, bạn nên chọn phương pháp nào? Câu trả lời hóa ra *không nằm trong bảng dữ liệu* — nó phụ thuộc vào **câu chuyện nhân quả** đằng sau dữ liệu (bác sĩ có xu hướng chỉ định phương pháp mạnh hơn cho ca bệnh nặng hơn).

Suốt một thế kỷ, thống kê cổ điển gần như cấm kỵ chữ "nguyên nhân" và chỉ lặp lại câu thần chú *"tương quan không phải nhân quả"*. **Judea Pearl** (Giải A.M. Turing **2011**) đã phá vỡ sự im lặng ấy bằng cách trao cho quan hệ nhân quả một **ngôn ngữ toán học đầy đủ** gồm đồ thị nhân quả (DAG), toán tử can thiệp $$do(x)$$ và phép tính **do-calculus**:

> “for fundamental contributions to artificial intelligence through the development of a calculus for probabilistic and causal reasoning.”  
> — [ACM Turing Award](https://amturing.acm.org/)

Bài này dẫn bạn qua cấu trúc toán–logic của nhân quả: mạng Bayes, nấc thang ba tầng (quan sát – can thiệp – phản thực), biến nhiễu (confounder) và những giới hạn không thể vượt qua bằng dữ liệu lớn đơn thuần. Liên kết: [xác suất]({{ site.baseurl }}/contents/vi/chapter03/03_04_Probability_Data_Science/), [toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

---

## Mục tiêu học tập

Sau bài, bạn có thể phân biệt ba nấc **association / intervention / counterfactual**; đọc **Bayesian network** như factorization $$p(x_1,\ldots,x_n)=\prod_i p(x_i\mid \mathrm{pa}(i))$$ trên DAG; giải thích **confounder** và vì sao hồi quy quan sát có thể lệch tác động nhân quả; phát biểu ý toán tử $$do(X=x)$$ và khác conditioning $$p(y\mid x)$$; nêu **backdoor** ở mức khẩu hiệu (chặn mọi đường back-door từ $$X$$ sang $$Y$$ không tạo đường mới); mô tả counterfactual như lớp suy diễn cần mô hình cấu trúc; phê slogan “big data thay nhân quả” và “DAG = sự thật thế giới”.

**Kiến thức nền.** Xác suất có điều kiện; độc lập; đồ thị có hướng cơ bản. Không cần measure theory.

---

## Bản đồ kiến thức nền: Toán học nhân quả và Mô hình đồ thị xác suất là gì, nghiên cứu những gì?

Người tốt nghiệp đại học ngành khoa học dữ liệu hay học máy thường rất thành thạo việc ước lượng xác suất có điều kiện $$p(y \mid x)$$ — ví dụ *"biết khách hàng vừa mua bỉm, xác suất họ mua bia là bao nhiêu?"*. Nhưng ngay khi bạn bước sang câu hỏi ra quyết định — *"nếu ta chủ động giảm giá thuốc $$X$$ thì tỉ lệ khỏi bệnh $$Y$$ thay đổi thế nào?"* — xác suất quan sát $$p(y \mid x)$$ không còn đủ nữa, bởi vì **nhìn thấy $$X=x$$** (quan sát thụ động) khác hoàn toàn với **ép $$X=x$$** (can thiệp chủ động)!

Đó là sân khấu của **Toán học nhân quả (Causal Inference)** và **Mô hình đồ thị xác suất (Probabilistic Graphical Models)**, đứng trên ba trụ cột:
1. **Đồ thị có hướng không chu trình (DAG) như bản đồ cơ chế:** Thay vì coi mọi biến bình đẳng trong một bảng dữ liệu phẳng, ta vẽ mũi tên $$A \to B$$ để biểu thị $$A$$ là nguyên nhân trực tiếp của $$B$$. Đồ thị đó cho phép phân tích phân phối đồng thời thành tích các xác suất địa phương và đọc ngay quan hệ độc lập có điều kiện bằng tiêu chuẩn **d-separation**.
2. **Toán tử $$do(x)$$ và Phép tính do-calculus:** Khi can thiệp $$do(X=x)$$, ta thực hiện một ca "phẫu thuật đồ thị": **cắt đứt mọi mũi tên đi vào $$X$$** (vì giờ đây chính ta quyết định giá trị của $$X$$ chứ không phải biến nhiễu nào khác) và tính phân phối mới của $$Y$$. Phép tính **do-calculus** của Pearl cung cấp đúng 3 quy tắc đại số để trả lời câu hỏi: *liệu có thể tính được tác động can thiệp $$p(y \mid do(x))$$ chỉ từ dữ liệu quan sát mà không cần làm thí nghiệm ngẫu nhiên (RCT) tốn kém hay không?*
3. **Mô hình nhân quả cấu trúc (SCM) và Phản thực (Counterfactual):** Ở tầng sâu nhất, mỗi biến được mô tả bằng một phương trình cơ chế $$X_i := f_i(\mathrm{Pa}_i, U_i)$$ với nhiễu nền $$U_i$$. Nhờ giữ nguyên giá trị nhiễu $$U_i$$ của một cá nhân đã quan sát rồi thay phương trình của $$X$$, ta mới định nghĩa được câu hỏi *"giá như bệnh nhân này đã không dùng thuốc đó thì kết quả ra sao?"* — nền tảng của y học cá thể hóa và đánh giá công bằng thuật toán (algorithmic fairness).

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

Joint trên $$n$$ biến nhị phân có $$2^n-1$$ bậc tự do; mạng thưa hóa bằng local conditionals. Đây vừa nén, vừa **giả định mô hình** có thể sai. Lưu ý: BN không miễn nhiễm với việc mô hình bị sai; nó làm giả định *nhìn thấy được*.

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

### Ví dụ cầm tay chỉ việc: Giải phẫu Nghịch lý Simpson bằng số liệu 700 bệnh nhân

Hãy tự tay kiểm tra chính bộ số liệu điều trị sỏi thận kinh điển (Charig và cộng sự, 1986) trên **700 bệnh nhân**, chia đều 350 ca dùng **Phương pháp A** (phẫu thuật mở) và 350 ca dùng **Phương pháp B** (tán sỏi qua da). Biến nhiễu $$Z$$ là **kích thước sỏi** ($$Z=0$$: sỏi nhỏ, $$Z=1$$: sỏi lớn), ảnh hưởng đến cả quyết định chọn phương pháp $$X$$ của bác sĩ lẫn khả năng khỏi bệnh $$Y$$ (đồ thị $$Z \to X$$, $$Z \to Y$$, $$X \to Y$$):

| Phân nhóm theo kích thước sỏi ($$Z$$) | Phương pháp A ($$X=A$$) | Phương pháp B ($$X=B$$) | Phương pháp thắng trong nhóm |
|---|---|---|---|
| Sỏi nhỏ ($$Z=0$$, tổng $$357$$ ca) | $$81 / 87 = 93{,}1\%$$ | $$234 / 270 = 86{,}7\%$$ | **A hơn** ($$+6{,}4\%$$) |
| Sỏi lớn ($$Z=1$$, tổng $$343$$ ca) | $$192 / 263 = 73{,}0\%$$ | $$55 / 80 = 68{,}8\%$$ | **A hơn** ($$+4{,}2\%$$) |
| **Gộp thô (quan sát $$p(Y=1 \vert X)$$)** | **$$273 / 350 = 78{,}0\%$$** | **$$289 / 350 = 82{,}6\%$$** | **B lại hơn** ($$+4{,}6\%$$)! |

Vì sao phép gộp thô lại đảo chiều? Nhìn vào mẫu số: bác sĩ chỉ định Phương pháp A cho tới $$263/350 = 75{,}1\%$$ ca **sỏi lớn** (vốn khó chữa), trong khi Phương pháp B nhận tới $$270/350 = 77{,}1\%$$ ca **sỏi nhỏ** (vốn dễ chữa)!

Bây giờ, ta áp dụng **công thức điều chỉnh back-door** của Pearl để tính xác suất khỏi bệnh nếu *chủ động áp dụng* một phương pháp cho toàn bộ dân số. Tỉ lệ dân số thật theo kích thước sỏi là:

$$
p(Z=0) = \frac{87 + 270}{700} = \frac{357}{700} = 51{,}0\%, \qquad p(Z=1) = \frac{263 + 80}{700} = \frac{343}{700} = 49{,}0\%.
$$

Ta thế đúng trọng số dân số $$p(Z)$$ (thay vì trọng số bị lệch $$p(Z \mid X)$$) vào công thức can thiệp:

$$
p(Y=1 \mid do(X=A)) = 0{,}51 \times 0{,}931 + 0{,}49 \times 0{,}730 \approx 0{,}4748 + 0{,}3577 = \mathbf{83{,}25\%},
$$

$$
p(Y=1 \mid do(X=B)) = 0{,}51 \times 0{,}867 + 0{,}49 \times 0{,}688 \approx 0{,}4422 + 0{,}3371 = \mathbf{77{,}93\%}.
$$

Cú đảo chiều biến mất ngay lập tức: **Phương pháp A thực sự hiệu quả hơn Phương pháp B tới $$+5{,}32$$ điểm phần trăm** ($$83{,}25\%$$ so với $$77{,}93\%$$)!

### Khung giải thích: Vì sao can thiệp là "phẫu thuật đồ thị" (nên đọc chậm)

Để không bao giờ lẫn lộn giữa xác suất có điều kiện và tác động nhân quả, hãy đi chậm qua mạch 4 bước sau:

1. **Bước 1 — Phân biệt *quan sát* và *can thiệp*:** Khi bạn tính $$p(Y=1 \mid X=A)$$, bạn đang chọn lọc nhóm bệnh nhân *tự nhiên được bác sĩ cho dùng A*. Biết $$X=A$$ vừa cho biết họ dùng A, vừa "rò rỉ" thông tin ngược lên mũi tên $$Z \to X$$ rằng họ nhiều khả năng bị sỏi lớn ($$75{,}1\%$$).
2. **Bước 2 — Cắt đứt mũi tên đi vào $$X$$:** Khi bạn thực hiện $$do(X=A)$$ (gán cứng phương pháp A cho bệnh nhân bất kỳ), mũi tên $$Z \to X$$ bị **xóa khỏi đồ thị**. Giờ đây kích thước sỏi $$Z$$ không còn quyết định phương pháp điều trị nữa, nên phân phối của $$Z$$ quay về đúng phân phối tự nhiên $$p(Z) = (51\%, 49\%)$$.
3. **Bước 3 — Giữ nguyên các cơ chế còn lại:** Cơ chế sinh học $$p(Y=1 \mid X, Z)$$ (mũi tên $$X \to Y$$ và $$Z \to Y$$) không đổi sau ca phẫu thuật đồ thị. Do đó bạn chỉ cần lấy trung bình có trọng số các xác suất tầng theo $$p(Z)$$ — chính là công thức back-door.
4. **Bước 4 — Cảnh giác khi đổi câu chuyện nhân quả:** Giả sử $$Z$$ *không phải* là kích thước sỏi đo trước điều trị, mà là **huyết áp đo sau khi uống thuốc** (một biến trung gian $$X \to Z \to Y$$). Khi đó *không có* đường back-door từ $$Z$$ vào $$X$$ — nếu bạn vẫn đem $$Z$$ đi điều chỉnh, bạn sẽ **chặn mất chính tác động của thuốc**! Cùng một bảng số liệu 700 dòng, hai đồ thị khác nhau cho ra hai quyết định y khoa trái ngược nhau.

**Kiểm tra nhanh.** Nếu trong ví dụ 700 bệnh nhân trên, tỉ lệ sỏi nhỏ trong toàn thành phố tăng lên $$p(Z=0)=80\%$$ và sỏi lớn giảm còn $$p(Z=1)=20\%$$, hãy nhẩm lại $$p(Y=1 \mid do(X=A))$$: $$0{,}8 \times 93{,}1\% + 0{,}2 \times 73{,}0\% = 74{,}48\% + 14{,}60\% = 89{,}08\%$$. Bạn thấy đấy: tác động can thiệp phụ thuộc trực tiếp vào phân phối quần thể $$p(Z)$$, trong khi hiệu quả từng tầng $$p(Y\mid X,Z)$$ vẫn giữ nguyên.

### do-calculus

Pearl cho **ba quy tắc** viết lại biểu thức $$do$$ thành xác suất quan sát dưới giả định đồ thị, khi có thể. Đây là **đại số suy diễn**: không phải mọi $$p(y\mid do(x))$$ đều identify từ data quan sát; do-calculus + tiêu chí đồ thị nói *khi nào* identify được và *công thức nào*.

Identification theory (cũng với instrumental variables, front-door, …) là toán logic–xác suất, không phải “chạy regression mạnh hơn”.

---

## 4. Structural Causal Models (SCM)

### Phương trình cơ chế

Mỗi biến $$X_i:=f_i(\mathrm{Pa}_i,U_i)$$ với nhiễu ngoại sinh $$U_i$$. Joint quan sát sinh từ nhiễu và cơ chế. Can thiệp thay $$f_X$$ bằng hằng. Counterfactual: cố định nhiễu (thế giới đã thực hiện), đổi cơ chế, đọc lại $$Y$$.

Ví dụ phản thực trong 2 dòng: giả sử mô hình tuyến tính $$Y := 2X + U_Y$$ (với $$X$$ là số giờ học thêm, $$Y$$ là điểm thi, $$U_Y$$ là nền tảng sẵn có của thí sinh). Ta quan sát một bạn học $$X'=1$$ giờ và đạt $$Y'=7$$ điểm. Bước **suy ngược (abduction)** cố định $$U_Y = 7 - 2(1) = 5$$. Bước **hành động & dự đoán** thay $$X=3$$ vào phương trình giữ nguyên $$U_Y=5$$ để trả lời câu hỏi phản thực: *"Nếu chính bạn ấy đã học 3 giờ thì điểm sẽ là $$Y_{X=3} = 2(3) + 5 = 11$$."*

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

“Nếu đổi thuộc tính nhạy cảm, outcome có đổi không?” mang hình counterfactual. Formal hóa khó: graph nào? nhiễu nào? Công trình của Pearl không kết thúc tranh luận đạo đức; ông cho **ngôn ngữ** để tranh luận không chỉ slogan.

### Deep learning + causality

Net xấp xỉ hàm; causality hỏi *hàm nào là cơ chế* và *thí nghiệm giả định nào hợp lệ*. Kết hợp (causal discovery + representation) còn non trẻ so với supervised scale. Xem [Deep Learning Trio]({{ site.baseurl }}/contents/vi/chapter09/09_12_Deep_Learning_Trio/) để không nhầm “scale” với “identify”.

---

## 6. Causal discovery: khi graph chưa cho sẵn

Nhiều ứng dụng *không* biết DAG. Thuật toán discovery (PC, FCI, score-based, …) dùng độc lập có điều kiện và giả định (causal sufficiency, faithfulness) để khôi phục lớp Markov tương đương. Giới hạn:

- **Markov equivalence:** nhiều DAG cùng độc lập—không phân biệt bằng observational data đơn thuần.  
- **Latent confounding** phá sufficiency.  
- **Finite sample** error độc lập tests.

Lưu ý: bài báo kiểu “we learned the causal graph from data” cần checklist giả định, equivalence class, và validation can thiệp nếu có.

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

## 8. Ví dụ toán nhỏ: back-door trong một dòng

Giả sử $$Z$$ chặn mọi đường back-door từ $$X$$ sang $$Y$$ và không có descendant “xấu” của $$X$$ trong $$Z$$ (điều kiện chuẩn). Khi đó average causal effect rời rạc:

$$
\mathbb{E}[Y\mid do(x)]=\sum_z \mathbb{E}[Y\mid x,z]\,p(z).
$$

So sánh với $$\sum_z \mathbb{E}[Y\mid x,z]\,p(z\mid x)$$. Nếu $$Z$$ liên quan $$X$$, hai trọng số khác nhau—**cùng regression nội bộ**, **khác average** — đúng như bảng 700 bệnh nhân ta vừa tự tay tính ở Mục 3.

---

## 9. Front-door, instrument, và giới hạn identify

Không phải mọi graph cho phép back-door. **Front-door** dùng trung gian $$M$$ trên đường nhân quả $$X\to M\to Y$$ khi giữa $$X$$ và $$Y$$ có confounder ẩn nên không thể điều chỉnh theo back-door. **Instrumental variables** (kinh tế lượng) ép exogenous shock vào $$X$$. Cả hai nhắc: identification là **định lý về model class**, không phải nút “causal=True” trong thư viện.

Khi không identify được từ quan sát, trung thực khoa học là nói *partial identification* (bounds) hoặc thiết kế thí nghiệm. Pearl không xóa RCT; ông mở rộng ngôn ngữ khi RCT đắt hoặc bất khả đạo đức. [Valiant PAC]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/) hỏi học trong i.i.d.; Pearl hỏi *đổi cơ chế*—hai bài toán, đừng gộp.

### Transportability

Đôi khi ta có RCT ở quần thể A và quan sát ở B. **Transport** công thức nhân quả qua domain shift dưới giả định đồ thị selection—chương trình hiện đại gần OOD ML. Cũng cần hỏi: giả định về selection có kiểm tra được không?

---

## Video và tài liệu

Video gợi ý, dùng để làm quen với bối cảnh chứ không thay cho chứng minh: [https://www.youtube.com/watch?v=iNm4nFBFmvo](https://www.youtube.com/watch?v=iNm4nFBFmvo).

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/pearl-causality_iNm4nFBFmvo_thumb.jpg)

*Hình. Khung hình mẫu từ video đầu tiên.*

## Tài liệu tham khảo trực tuyến

1. Trang giải Turing của Pearl — https://amturing.acm.org/award_winners/pearl_2658896.cfm  
2. Wikipedia — Judea Pearl — https://en.wikipedia.org/wiki/Judea_Pearl  
3. Wikipedia — Causal model — https://en.wikipedia.org/wiki/Causal_model  
4. Wikipedia — Bayesian network — https://en.wikipedia.org/wiki/Bayesian_network  
5. Wikipedia — Do-calculus — https://en.wikipedia.org/wiki/Do_calculus  
6. *The Book of Why* (mục từ phổ thông) — https://en.wikipedia.org/wiki/The_Book_of_Why  
7. Phòng thí nghiệm Cognitive Systems ở UCLA (Pearl) — http://bayes.cs.ucla.edu/jp_home.html  
8. Video về nhân quả của Pearl — https://www.youtube.com/watch?v=iNm4nFBFmvo  

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

## Video tham khảo

- **Xem trước** — [Judea Pearl, 2012 ACM A.M. Turing Award Lecture "The Mechanization of Causal Inference"](https://www.youtube.com/watch?v=iNm4nFBFmvo) — Association for Computing Machinery (ACM), tiếng Anh. Xem trước để làm quen với chủ đề.
