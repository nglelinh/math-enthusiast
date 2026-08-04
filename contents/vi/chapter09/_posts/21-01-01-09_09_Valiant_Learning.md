---
layout: post
title: "Valiant và Lý thuyết Học Tính toán (Turing 2010)"
chapter: '09'
order: 9
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
---

**Leslie G. Valiant** nhận **A.M. Turing Award 2010**

> “for transformative contributions to the theory of computation, including the theory of probably approximately correct (PAC) learning, the complexity of enumeration and of algebraic computation, and the theory of parallel and distributed computing.”  
> — [ACM Turing Award](https://amturing.acm.org/)

Trước Valiant, “học máy” có thể nghe như kỹ thuật thống kê hoặc mô phỏng nơ-ron. Sau **PAC**—*Probably Approximately Correct*—học trở thành **bài toán tính toán** với định nghĩa đúng/sai: bao nhiêu mẫu, lớp khái niệm nào, thời gian poly nào, và độ tin cậy/xấp xỉ nào. Cùng sự nghiệp, Valiant đặt **#P** (đếm nghiệm) cạnh NP, và nối permanent với hardness đại số. Bài này dựng ba trụ đó cho khóa Math Enthusiast, với trọng tâm PAC và cầu sang [lý thuyết ML]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/) cùng [toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/).

---

## Mục tiêu học tập

Sau bài, bạn có thể phát biểu định nghĩa **PAC learnability** cho lớp khái niệm $$\mathcal{C}$$: tồn tại thuật toán poly-time (trong $$n,1/\varepsilon,1/\delta$$ theo chuẩn) lấy mẫu i.i.d. từ $$\mathcal{D}$$ và, với xác suất $$\ge 1-\delta$$, xuất hypothesis $$h$$ sao cho $$R(h)\le\varepsilon$$ trong mô hình realizable; giải thích vai trò **$$\varepsilon$$ (xấp xỉ)** và **$$\delta$$ (độ tin cậy)**—hai “probably / approximately”; nêu **VC-dimension** (hoặc proxy độ phức tạp lớp) như chặn số mẫu; định nghĩa ý **#P** và vì sao đếm khác quyết định; mô tả permanent vs determinant như biểu tượng hardness đại số; phê nhầm “PAC = deep learning đã chứng minh” và “#P-complete ⇒ không đếm được thực tế mọi instance”.

**Kiến thức nền.** Xác suất cơ bản; poly-time; khái niệm hypothesis class. [Độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/) và [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/) là bạn đồng hành.

---

## 1. Học như bài toán complexity

### Câu hỏi Valiant đặt lại

Cho lớp khái niệm $$\mathcal{C}$$ trên miền $$X=\{0,1\}^n$$ (hoặc $$\mathbb{R}^n$$), và phân phối $$\mathcal{D}$$ chưa biết trên $$X$$. Concept đích $$c\in\mathcal{C}$$ gán nhãn. Người học nhận mẫu $$(x,c(x))$$ i.i.d. theo $$\mathcal{D}$$. Mục tiêu: xuất $$h$$ sao cho **rủi ro**

$$
R(h)=\mathbb{P}_{x\sim\mathcal{D}}\big(h(x)\neq c(x)\big)
$$

nhỏ, với **xác suất cao trên mẫu**, trong **thời gian hiệu quả**.

PAC formal hóa “nhỏ” bằng $$\varepsilon$$, “xác suất cao” bằng $$1-\delta$$, “hiệu quả” bằng poly trong $$n,1/\varepsilon,1/\delta$$ (và kích thước biểu diễn concept—chi tiết sách). Đây không phải một thuật toán; đây là **đặc tả bài toán** cho cả lớp $$\mathcal{C}$$.

### Probably và Approximately

- **Approximately:** không đòi $$h=c$$ điểmwise; cho phép sai trên measure $$\le\varepsilon$$ theo $$\mathcal{D}$$.  
- **Probably:** thuật toán có thể xui trên mẫu hiếm; xác suất thất bại $$\le\delta$$.

Hai tham số tách hai nguồn bất định: nhiễu mẫu và nới lỏng mục tiêu. Thống kê cổ điển biết khoảng tin cậy; Valiant thêm **ràng buộc tính toán** và **lớp khái niệm tường minh** như object complexity.

### Realizable vs agnostic

PAC cổ điển thường **realizable**: $$c\in\mathcal{C}$$. **Agnostic PAC** nhắm best-in-class: excess risk so với $$\inf_{h\in\mathcal{H}} R(h)$$. Thực hành ML gần agnostic hơn; định lý mẫu và hardness tinh chỉnh theo từng chế độ. Xem [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

---

## 2. Số mẫu, VC, và “học được” nghĩa gì

### Hội tụ đều (hình dạng)

Nếu lớp $$\mathcal{H}$$ không quá phức tạp, rủi ro thực nghiệm

$$
\hat R_S(h)=\frac{1}{m}\sum_{i=1}^m \mathbf{1}[h(x_i)\neq y_i]
$$

gần $$R(h)$$ đều theo $$h$$ khi $$m$$ lớn. Khi đó ERM (chọn $$h$$ giảm $$\hat R_S$$) PAC-học được trong chế độ thống kê—**nếu** ERM tính được.

**VC-dimension** $$\mathrm{VCdim}(\mathcal{H})$$ đo khả năng shatter; chặn mẫu kiểu

$$
m = O\Big(\frac{1}{\varepsilon}\big(\mathrm{VCdim}(\mathcal{H})\log(1/\varepsilon)+\log(1/\delta)\big)\Big)
$$

(dạng schematic realizable). Chi tiết hằng số không quan trọng bằng **tách hai nút thắt**: (1) đủ mẫu thống kê; (2) tối ưu hóa/truy vấn hypothesis hiệu quả.

### Học tính toán vs học thống kê

Valiant nhấn (2). Lớp có thể có VC hữu hạn nhưng **ERM NP-khó**. Khi đó “học được thống kê” ≠ “PAC poly-time”. Có kết quả representation-independent hardness: dưới giả thiết crypto, một số lớp tự nhiên không PAC-học hiệu quả. Đây là điểm LO6 khi ai đó nói “VC nhỏ ⇒ deep net an toàn”: chặn mẫu có thể lỏng, và thuật toán mới là chuyện khác.

### Ví dụ lớp

- **Nửa không gian tuyến tính** (halfspaces) ở chiều cố định: nền tảng perceptron / linear separators.  
- **Hội/clauses** với độ dài bị chặn: liên quan DNF learning—một chương trình dài hơi, một phần còn mở ở dạng đầy đủ.  
- **Mạch nông / net**: biểu diễn giàu ⇒ thống kê và tối ưu đều khó hơn; PAC cổ điển không “giải thích xong” deep learning.

---

## 3. #P: đếm cũng là complexity

### Từ quyết định sang đếm

**NP** hỏi *tồn tại* witness? **#P** hỏi *bao nhiêu* witness? Ví dụ: số gán thỏa của công thức Boolean (#SAT). Rõ ràng #SAT “ít nhất khó bằng” SAT: nếu đếm được thì biết tồn tại hay không. Valiant chỉ ra hệ thống **#P-complete**: đếm khó “đại diện” cho cả lớp đếm.

Hệ quả văn hóa: nhiều bài “thống kê tổ hợp” (đếm matching, đếm tô màu, partition function vật lý thống kê) mang hardness đếm, ngay cả khi phiên bản quyết định nằm trong P. **Permanent** là ngôi sao.

### Permanent vs determinant

Với ma trận $$A=(a_{ij})$$,

$$
\mathrm{per}(A)=\sum_{\sigma\in S_n}\prod_{i=1}^n a_{i,\sigma(i)},
$$

cùng hình dạng tổng theo hoán vị như $$\det$$ nhưng **không** dấu xen kẽ. Determinant tính poly-time (Gaussian elimination); permanent của ma trận 0-1 là #P-complete (Valiant). Đây là một trong những tương phản đẹp nhất TCS: hai đa thức “gần giống”, một dễ một cứng theo complexity.

Vật lý và sampling: xấp xỉ permanent, FPRAS cho một số lớp, và hardness of approximation tinh chỉnh bức tranh—nuôi thuật toán ngẫu nhiên và Markov chains.

---

## 4. Độ phức tạp đại số và cầu song song

Citation còn *algebraic computation* và *parallel/distributed*. Valiant đóng góp mô hình tính permanent/determinant, reduction đại số, và tầm nhìn circuit/algebraic complexity—họ hàng câu hỏi “VP vs VNP” (analogue đại số của P vs NP, còn mở). Không cần thuộc mọi định nghĩa để nắm khẩu hiệu khóa học:

> **Cùng một sự nghiệp có thể định nghĩa học hiệu quả *và* chứng minh đếm/đại số cứng.**

Học và hardness không đối nghịch: chúng là hai mặt của “cái gì tính được bằng tài nguyên hợp lý”.

Parallel algorithms và Bulk-Synchronous-ish thinking (văn hóa Valiant về mô hình song song) nhấn: complexity còn là **độ trễ, bandwidth, đồng bộ**—không chỉ asymptotic serial time. Bài [chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/) sẽ chạm systems–algorithms lại.

---

## 5. PAC gặp thực hành ML hiện đại

### Điều PAC giải thích tốt

- Tách **mẫu**, **xấp xỉ**, **tin cậy**, **lớp**.  
- Ngôn ngữ chung cho statistics + CS.  
- Hardness results: đừng kỳ vọng poly-time cho mọi lớp biểu diễn giàu.

### Điều PAC cổ điển *không* tự động giải thích

- **Overparameterized nets** nội suy vẫn tổng quát hóa (benign overfitting, double descent)—xem [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).  
- **Inductive bias** của SGD và kiến trúc (CNN, transformer) không nằm trong “$$\mathcal{H}$$ set-theoretic” thuần.  
- Dữ liệu **không i.i.d.**, dịch phân phối, nhân quả—cần Pearl, online learning, robust statistics.

PAC là **nền móng**, không phải thuyết vạn vật. Turing 2010 vinh danh đúng việc đặt móng: sau đó cả thành phố (boosting, margin, Rademacher, PAC-Bayes, deep theory) xây tiếp.

### Boosting như di sản văn hóa

Adaboost và theory of weak learning gắn câu chuyện “weak ⇒ strong” trong khung sample complexity. Valiant không phải tác giả duy nhất của boosting, nhưng ngôn ngữ learnability poly-time làm các định lý boosting *có chỗ đứng*. Weak learner với advantage nhỏ, kết hợp thành accuracy cao—hình ảnh vẫn sống trong ensemble và gradient boosting thực hành.

---

## 6. Neuroidal model và “học trong não” (phác)

Valiant còn viết về mô hình tính–sinh học (neuroidal nets): ràng buộc địa phương, số nơ-ron, thời gian học so với năng lực nhận thức. Đây không phải deep learning GPU 2020s; đây là **câu hỏi complexity của nhận thức**: bao nhiêu tài nguyên để học quan hệ, bind biến, suy luận thô. Đọc như cầu triết–toán, không như recipe PyTorch. Gặp [toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) ở tầng “mô hình tính của thông minh”, khác tầng “train loss ImageNet”.

---

## 7. Nhầm lẫn thường gặp

| Tuyên bố | Chỉnh |
|----------|--------|
| “PAC = luôn đúng trên test set.” | $$1-\delta$$ và sai số $$\varepsilon$$ theo $$\mathcal{D}$$; không phải zero error. |
| “VC hữu hạn ⇒ học poly-time.” | Thống kê ≠ tính toán ERM. |
| “#P-complete ⇒ không bao giờ đếm được.” | Hardness asymptotic worst-case; instance nhỏ/cấu trúc vẫn đếm/xấp xỉ. |
| “Permanent khó vì công thức dài.” | Khó theo reduction #P; độ dài công thức không phải lý do complexity. |
| “Deep learning đã thay thế PAC.” | PAC vẫn là ngôn ngữ đặc tả; DL thêm bias thuật toán và scale. |
| “Valiant chỉ học máy.” | #P, đại số, song song cùng citation. |

**Không nên tuyên bố.** “Đã có PAC nên generalization deep net xong.” Chặn cổ điển có thể rỗng; hiện tượng mới cần lý thuyết mới—đúng tinh thần Valiant: *đặt định nghĩa rồi chứng minh*.

---

## 8. Studio: đọc một định lý PAC

Checklist một định lý “$$\mathcal{C}$$ is efficiently PAC-learnable”:

1. Miền và cách biểu diễn concept (size $$n$$)?  
2. Realizable hay agnostic?  
3. Oracle mẫu: i.i.d. labeled? membership queries?  
4. Phụ thuộc poly vào $$1/\varepsilon,1/\delta$$ ra sao?  
5. Giả thiết crypto/complexity nào cho *negative* results?  
6. Hypothesis class output có nằm trong $$\mathcal{C}$$ (proper) hay proper-ness bị bỏ (improper learning)?

Improper learning—xuất $$h$$ ngoài $$\mathcal{C}$$—đôi khi dễ hơn proper; đây là tinh chỉnh quan trọng khi đọc paper.

---

## Bài tập

1. Viết định nghĩa PAC realizable bằng ký hiệu $$m(\varepsilon,\delta)$$ và $$R(h)$$.  
2. Giải thích một đoạn: tăng $$\varepsilon$$ ảnh hưởng gì đến số mẫu kỳ vọng; tăng $$\delta$$ thì sao?  
3. Đếm số monom bậc $$\le k$$ trên $$n$$ biến (order-of-magnitude). Liên hệ “lớp giàu ⇒ mẫu/thời gian”.  
4. Permanent $$2\times 2$$ tính tay; so với det.  
5. **≤200 từ:** Vì sao #SAT khó “hơn” SAT theo tinh thần complexity (không cần proof đầy đủ)?  
6. Nối [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/): một câu Rademacher/VC bổ sung PAC thế nào.  
7. **Seminar:** Chọn lớp (intervals trên $$\mathbb{R}$$, rectangles, halfspaces). Phác shatter / VC; thảo luận ERM có “dễ” không.

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/valiant-learning/`.

**Khẩu hiệu từ gói nghiên cứu**

- Valiant Turing 2010: PAC learning — học như bài toán độ phức tạp.

**Thứ tự xem gợi ý**


**Cổng chính thức / tài liệu**

- Valiant Turing page: https://amturing.acm.org/award_winners/valiant_2612174.cfm  
- Deep Learning Trio Turing 2018: https://amturing.acm.org/award_winners/hinton_4791679.cfm  

Danh mục URL đầy đủ: `research/video-research/valiant-learning/references.md`.

## Tài liệu tham khảo


### Gói nghiên cứu video (mọi URL)

Danh mục đầy đủ: `research/video-research/valiant-learning/references.md`.

1. Valiant Turing page — https://amturing.acm.org/award_winners/valiant_2612174.cfm  
2. Wikipedia — Leslie Valiant — https://en.wikipedia.org/wiki/Leslie_Valiant  
3. Wikipedia — Probably approximately correct learning — https://en.wikipedia.org/wiki/Probably_approximately_correct_learning  
4. Wikipedia — Computational learning theory — https://en.wikipedia.org/wiki/Computational_learning_theory  
5. Valiant PAC paper culture (CACM / JACM lineage) — https://dl.acm.org/doi/10.1145/1968.1972  
6. Deep Learning Trio Turing 2018 — https://amturing.acm.org/award_winners/hinton_4791679.cfm  
7. Wikipedia — VC dimension (related theory) — https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension  
8. ACM awards page Valiant — https://awards.acm.org/award-recipients/valiant_2612174  
9. Thư mục gói: `research/video-research/valiant-learning/`.

1. ACM Turing Award — Leslie Valiant (2010).  
2. Valiant — “A theory of the learnable” (*CACM* / *Comm. ACM* lineage; paper nền PAC).  
3. Kearns & Vazirani — *An Introduction to Computational Learning Theory*.  
4. Arora & Barak — chapters counting complexity / permanent.  
5. Khóa: [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/); [toán AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/); [độ phức tạp]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/); [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/).

---

## Hướng đi tiếp

- Thống kê chiều cao và concentration: [Talagrand / Abel]({{ site.baseurl }}/contents/vi/chapter08/08_09_Talagrand_Probability/) và [hình học cao chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/).  
- Deep learning thực tiễn–lý thuyết: [Bengio–Hinton–LeCun]({{ site.baseurl }}/contents/vi/chapter09/09_12_Deep_Learning_Trio/).  
- Nhân quả vượt i.i.d.: [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/).  
- Thực hành: học interval trên $$\mathbb{R}$$ bằng ERM; vẽ train/test vs $$m$$.  
- Đọc: Valiant 1984/PAC intro → Kearns–Vazirani ch.1–3 → một survey DNF learning.  
- Tiếp: [Hopcroft–Tarjan]({{ site.baseurl }}/contents/vi/chapter09/09_10_Hopcroft_Tarjan/).
