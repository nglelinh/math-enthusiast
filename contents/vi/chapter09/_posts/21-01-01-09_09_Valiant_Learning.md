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

Khi một đứa trẻ nhìn thấy vài chục bức ảnh về con mèo rồi tự nhận ra một con mèo hoàn toàn mới ngoài công viên, ta gọi đó là "học". Nhưng trong suốt nửa đầu thế kỷ XX, trí tuệ nhân tạo thiếu một định nghĩa toán học rõ ràng cho câu hỏi: **thế nào là một khái niệm "học được" một cách hiệu quả bằng máy tính?** Năm 1984, **Leslie G. Valiant** đã đặt viên gạch nền móng bằng mô hình **PAC** (*Probably Approximately Correct* — đúng xấp xỉ với xác suất cao), biến việc "học từ dữ liệu" thành một bài toán độ phức tạp tính toán chặt chẽ.

Năm **2010**, Valiant nhận **Giải A.M. Turing** cho những đóng góp đa dạng hiếm thấy:

> “for transformative contributions to the theory of computation, including the theory of probably approximately correct (PAC) learning, the complexity of enumeration and of algebraic computation, and the theory of parallel and distributed computing.”  
> — [ACM Turing Award](https://amturing.acm.org/)

(Tạm dịch: "vì những đóng góp mang tính thay đổi cho lý thuyết tính toán, gồm lý thuyết học PAC, độ phức tạp của bài toán đếm và của tính toán đại số, và lý thuyết tính toán song song và phân tán.")

Không chỉ đặt khung cho học máy, chính Valiant cũng khai sinh lớp **#P** (độ khó của bài toán *đếm* số nghiệm) và chứng minh hàm **permanent** — người anh em song sinh của định thức chỉ khác đúng dấu cộng/trừ — lại khó ở cấp độ #P-đầy đủ! Bài này đi qua ba trụ cột ấy và nối sang [lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/) cùng [toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/).

---

## Mục tiêu học tập

Sau bài học, bạn có thể: phát biểu định nghĩa **học được theo PAC** cho một lớp khái niệm $$\mathcal{C}$$: tồn tại một thuật toán chạy trong thời gian đa thức (theo $$n,1/\varepsilon,1/\delta$$ như thường lệ), nhận các mẫu độc lập cùng phân phối (i.i.d.) từ $$\mathcal{D}$$ và, với xác suất $$\ge 1-\delta$$, trả về một giả thuyết $$h$$ sao cho $$R(h)\le\varepsilon$$ trong trường hợp khả thực; giải thích vai trò của **$$\varepsilon$$ (độ xấp xỉ)** và **$$\delta$$ (độ tin cậy)**, ứng với hai chữ "approximately" và "probably"; nêu **chiều VC** (hoặc một đại lượng đo độ phức tạp của lớp) như một cận cho số mẫu cần thiết; nêu ý tưởng của lớp **#P** và vì sao bài toán đếm khác bài toán quyết định; mô tả sự tương phản giữa permanent và định thức như một biểu tượng của độ khó trong tính toán đại số; bác bỏ các nhận định sai "PAC đã chứng minh deep learning hoạt động" và "#P-đầy đủ nghĩa là trong thực tế không đếm được bất kỳ trường hợp nào".

**Kiến thức cần có.** Xác suất cơ bản; thời gian đa thức; khái niệm lớp giả thuyết. Nên đọc kèm các bài [Độ phức tạp tính toán]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/) và [Lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

---

## Bản đồ kiến thức nền: Lý thuyết học tính toán (PAC) và Độ phức tạp bài toán đếm (#P) là gì, nghiên cứu những gì?

Hai đóng góp nổi tiếng nhất của Valiant nằm ở hai mảng tưởng như xa nhau nhưng cùng xoay quanh một câu hỏi: *đâu là ranh giới của tính toán hiệu quả?*

1. **Lý thuyết học tính toán (Computational Learning Theory — COLT):** Kết hợp xác suất thống kê với lý thuyết độ phức tạp. Để thấy trực giác của mô hình **PAC**, hãy hình dung bài toán tìm một **khoảng bí mật** $$[a, b]$$ trên trục số (ví dụ khoảng nhiệt độ lý tưởng cho một phản ứng hóa học). Bạn được xem $$m$$ điểm mẫu ngẫu nhiên đã gán nhãn "Tốt" hoặc "Xấu". Thuật toán đơn giản nhất là lấy khoảng nhỏ nhất $$[\hat a, \hat b]$$ bao gọn tất cả các điểm "Tốt". Vì mẫu là ngẫu nhiên, ta không thể đòi hỏi sai số bằng $$0$$ tuyệt đối — nhỡ hai đầu mút rơi vào vùng chưa có mẫu? Nên ta chỉ yêu cầu: với xác suất ít nhất $$1-\delta$$ (*Probably*, ví dụ $$99\%$$), tổng xác suất rơi vào vùng sai lệch không vượt quá $$\varepsilon$$ (*Approximately*, ví dụ $$1\%$$). Chỉ với $$m \ge \frac{2}{\varepsilon}\ln(2/\delta)$$ mẫu, thuật toán học được khoảng bí mật trong thời gian tuyến tính!
2. **Độ phức tạp bài toán đếm (#P) và Tính toán đại số:** Lớp NP hỏi *"Có tồn tại cách ghép cặp hoàn hảo giữa $$n$$ kỹ sư và $$n$$ dự án không?"* — bài toán này dễ, giải được trong thời gian đa thức (lớp P). Nhưng lớp **#P** hỏi *"Có **bao nhiêu** cách ghép cặp hoàn hảo như vậy?"*. Valiant chứng minh con số đó chính là **permanent** của ma trận kề $$0$$-$$1$$, và bài toán đếm này là **#P-đầy đủ** — khó hơn cả toàn bộ tầng lớp NP theo định lý Toda! Chỉ một thay đổi nhỏ — bỏ dấu $$\operatorname{sgn}(\sigma)$$ khỏi công thức định thức — đã biến một phép tính đại số tuyến tính năm nhất ($$\det$$) thành một bức tường tổ hợp khổng lồ ($$\mathrm{per}$$).

---

## 1. Học như một bài toán về độ phức tạp

### Câu hỏi Valiant đặt lại

Cho một lớp khái niệm $$\mathcal{C}$$ trên miền $$X=\{0,1\}^n$$ (hoặc $$\mathbb{R}^n$$), và một phân phối $$\mathcal{D}$$ chưa biết trên $$X$$. Một khái niệm đích $$c\in\mathcal{C}$$ dùng để gán nhãn. Người học nhận các mẫu $$(x,c(x))$$ độc lập theo $$\mathcal{D}$$. Mục tiêu là trả về $$h$$ sao cho **rủi ro**

$$
R(h)=\mathbb{P}_{x\sim\mathcal{D}}\big(h(x)\neq c(x)\big)
$$

nhỏ, với **xác suất cao theo mẫu**, trong **thời gian hiệu quả**.

Mô hình PAC định nghĩa chính xác "nhỏ" bằng $$\varepsilon$$, "xác suất cao" bằng $$1-\delta$$, "hiệu quả" bằng đa thức theo $$n,1/\varepsilon,1/\delta$$ (và theo kích thước biểu diễn của khái niệm; chi tiết xem sách). Đây không phải là một thuật toán, mà là **đặc tả bài toán** cho cả lớp $$\mathcal{C}$$.

### "Probably" và "Approximately"

- **Approximately (xấp xỉ):** không đòi $$h=c$$ tại mọi điểm; cho phép sai trên một tập có độ đo $$\le\varepsilon$$ theo $$\mathcal{D}$$.  
- **Probably (với xác suất cao):** thuật toán có thể gặp xui với một bộ mẫu hiếm gặp; xác suất thất bại $$\le\delta$$.

Hai tham số này tách riêng hai nguồn bất định: sự ngẫu nhiên của mẫu và việc nới lỏng mục tiêu. Thống kê cổ điển đã có khoảng tin cậy; Valiant bổ sung **ràng buộc về tính toán** và xem **lớp khái niệm cụ thể** là đối tượng nghiên cứu của độ phức tạp.

### Khả thực và bất khả tri

Mô hình PAC cổ điển thường giả sử **khả thực** (realizable): $$c\in\mathcal{C}$$. **PAC bất khả tri** (agnostic) nhắm đến giả thuyết tốt nhất trong lớp: đo rủi ro vượt so với $$\inf_{h\in\mathcal{H}} R(h)$$. Học máy trong thực tế gần với trường hợp bất khả tri hơn; các định lý về số mẫu và độ khó thay đổi tùy theo từng trường hợp. Xem bài [Lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

---

## 2. Số mẫu, chiều VC, và "học được" nghĩa là gì

### Hội tụ đều (dạng tổng quát)

Nếu lớp $$\mathcal{H}$$ không quá phức tạp thì rủi ro thực nghiệm

$$
\hat R_S(h)=\frac{1}{m}\sum_{i=1}^m \mathbf{1}[h(x_i)\neq y_i]
$$

gần với $$R(h)$$ một cách đều theo $$h$$ khi $$m$$ lớn. Khi đó phương pháp cực tiểu rủi ro thực nghiệm (ERM, chọn $$h$$ làm $$\hat R_S$$ nhỏ nhất) cho phép học PAC về mặt thống kê, **với điều kiện** ERM tính được.

**Chiều VC** $$\mathrm{VCdim}(\mathcal{H})$$ đo khả năng tách mọi cách gán nhãn (shatter) của lớp (ví dụ: đường thẳng trên mặt phẳng 2D tách được mọi cách gán nhãn của 3 điểm không thẳng hàng nhưng không thể tách nổi 4 điểm đặt thành hình vuông với hai cặp đối diện cùng màu, nên chiều VC của nửa mặt phẳng 2D bằng đúng $$3$$); ta có cận số mẫu dạng

$$
m = O\Big(\frac{1}{\varepsilon}\big(\mathrm{VCdim}(\mathcal{H})\log(1/\varepsilon)+\log(1/\delta)\big)\Big)
$$

(dạng phác thảo cho trường hợp khả thực). Hằng số cụ thể không quan trọng bằng việc **tách hai điểm nghẽn**: (1) có đủ mẫu về mặt thống kê; (2) tìm được giả thuyết một cách hiệu quả.

### Học về mặt tính toán và học về mặt thống kê

Valiant nhấn mạnh điểm (2). Một lớp có thể có chiều VC hữu hạn nhưng **bài toán ERM lại NP-khó**. Khi đó "học được về mặt thống kê" không đồng nghĩa với "học được theo PAC trong thời gian đa thức". Có những kết quả về độ khó không phụ thuộc cách biểu diễn: với các giả thiết mật mã, một số lớp tự nhiên không thể học PAC một cách hiệu quả. Đây là điểm cần tỉnh táo khi ai đó nói "chiều VC nhỏ thì mạng sâu an toàn": cận số mẫu có thể rất lỏng, và khả năng tối ưu bằng thuật toán lại là một chuyện hoàn toàn khác.

### Ví dụ về các lớp

- **Nửa không gian** (halfspaces) trong số chiều cố định: nền tảng của perceptron và các bộ phân tách tuyến tính.  
- **Hội các mệnh đề** với độ dài bị chặn: liên quan đến bài toán học DNF, một chương trình nghiên cứu dài, một phần vẫn còn mở ở dạng đầy đủ.  
- **Mạch nông / mạng nơ-ron**: biểu diễn càng phong phú thì cả mặt thống kê lẫn mặt tối ưu đều khó hơn; PAC cổ điển chưa "giải thích xong" deep learning.

---

## 3. #P: bài toán đếm cũng có độ phức tạp

### Từ quyết định sang đếm

Lớp **NP** hỏi: có *tồn tại* lời chứng (witness) không? Lớp **#P** hỏi: có *bao nhiêu* lời chứng? Ví dụ: số cách gán giá trị thỏa mãn một công thức Boolean (#SAT). Hiển nhiên #SAT "ít nhất khó bằng" SAT: nếu đếm được thì biết có nghiệm hay không. Valiant chỉ ra một hệ thống các bài toán **#P-đầy đủ**: những bài toán đếm khó "đại diện" cho cả lớp.

Hệ quả là nhiều bài toán "thống kê tổ hợp" (đếm cặp ghép, đếm số cách tô màu, hàm phân hoạch trong vật lý thống kê) đều khó về mặt đếm, ngay cả khi phiên bản quyết định nằm trong P. Ví dụ tiêu biểu nhất là **permanent**.

### Permanent và định thức

Với ma trận $$A=(a_{ij})$$,

$$
\mathrm{per}(A)=\sum_{\sigma\in S_n}\prod_{i=1}^n a_{i,\sigma(i)},
$$

có cùng dạng tổng theo các hoán vị như $$\det$$ nhưng **không** có dấu đan xen (ví dụ với ma trận $$2\times 2$$ là $$\begin{pmatrix}a&b\\c&d\end{pmatrix}$$, ta có $$\det = ad - bc$$ còn $$\mathrm{per} = ad + bc$$). Định thức tính được trong thời gian đa thức (phép khử Gauss nhờ tính bất biến dưới phép cộng hàng); permanent của ma trận 0-1 là #P-đầy đủ (Valiant). Đây là một trong những tương phản đẹp nhất của khoa học máy tính lý thuyết: hai đa thức "gần giống nhau", một cái dễ và một cái khó về độ phức tạp.

Trong vật lý và lấy mẫu: các kết quả về xấp xỉ permanent, thuật toán xấp xỉ ngẫu nhiên thời gian đa thức (FPRAS) cho một số lớp ma trận, và độ khó của bài toán xấp xỉ làm bức tranh chi tiết hơn, đồng thời thúc đẩy các thuật toán ngẫu nhiên và xích Markov.

---

## 4. Độ phức tạp đại số và tính toán song song

Lời trao giải còn nhắc đến *tính toán đại số* và *tính toán song song, phân tán*. Valiant đóng góp các mô hình tính permanent và định thức, phép quy dẫn đại số, và cách nhìn về độ phức tạp mạch và độ phức tạp đại số, gần với câu hỏi "VP và VNP" (phiên bản đại số của P và NP, hiện vẫn còn mở). Không cần nhớ mọi định nghĩa để nắm ý chính của bài:

> **Cùng một sự nghiệp có thể vừa định nghĩa thế nào là học hiệu quả, *vừa* chứng minh bài toán đếm và bài toán đại số là khó.**

Học và độ khó không đối lập nhau: chúng là hai mặt của câu hỏi "cái gì tính được với tài nguyên hợp lý".

Các thuật toán song song và lối tư duy kiểu đồng bộ theo khối (bulk-synchronous), một phần trong cách Valiant mô hình hóa tính toán song song, nhấn mạnh rằng độ phức tạp còn bao gồm **độ trễ, băng thông và đồng bộ hóa**, không chỉ thời gian chạy tuần tự tiệm cận. Bài [Các chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/) sẽ quay lại mối liên hệ giữa hệ thống và thuật toán.

---

## 5. PAC và học máy hiện đại

### Những điều PAC giải thích tốt

- Tách riêng **số mẫu**, **độ xấp xỉ**, **độ tin cậy** và **lớp giả thuyết**.  
- Cung cấp ngôn ngữ chung cho thống kê và khoa học máy tính.  
- Các kết quả về độ khó: đừng mong có thuật toán đa thức cho mọi lớp có biểu diễn phong phú.

### Những điều PAC cổ điển *không* tự động giải thích

- **Mạng có quá nhiều tham số** khớp hoàn toàn dữ liệu huấn luyện mà vẫn tổng quát hóa tốt (quá khớp lành tính, hiện tượng double descent); xem bài [Lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).  
- **Thiên kiến quy nạp** (inductive bias) của SGD và của kiến trúc mạng (CNN, transformer) không nằm trong khái niệm "$$\mathcal{H}$$ là một tập hợp" thuần túy.  
- Dữ liệu **không độc lập cùng phân phối**, phân phối bị dịch chuyển, quan hệ nhân quả: cần đến Pearl, học trực tuyến, thống kê vững.

PAC là **nền móng**, không phải lý thuyết giải thích mọi thứ. Giải Turing 2010 ghi nhận đúng việc đặt nền móng đó; sau này nhiều lý thuyết khác (boosting, lề, độ phức tạp Rademacher, PAC-Bayes, lý thuyết học sâu) được xây tiếp trên nền móng này.

### Boosting, một di sản

Thuật toán AdaBoost và lý thuyết học yếu gắn với câu hỏi "từ học yếu có thể có học mạnh không" trong khung độ phức tạp mẫu. Valiant không phải là tác giả duy nhất của boosting, nhưng ngôn ngữ "học được trong thời gian đa thức" đã cho các định lý boosting *một chỗ đứng*. Ý tưởng kết hợp các bộ học yếu, mỗi bộ chỉ tốt hơn đoán ngẫu nhiên một chút, thành một bộ học có độ chính xác cao vẫn được dùng trong các phương pháp tổ hợp và gradient boosting ngày nay.

---

## 6. Mô hình neuroidal và "học trong não" (phác thảo)

Valiant còn viết về mô hình tính toán lấy cảm hứng sinh học (mạng neuroidal): các ràng buộc cục bộ, số lượng nơ-ron, thời gian học so với khả năng nhận thức. Đây không phải deep learning chạy trên GPU của thập niên 2020, mà là **câu hỏi về độ phức tạp của nhận thức**: cần bao nhiêu tài nguyên để học các quan hệ, gắn biến, suy luận đơn giản. Nên đọc phần này như một cầu nối giữa triết học và toán học, không phải hướng dẫn dùng PyTorch. Nó gặp bài [Toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) ở tầng "mô hình tính toán của trí thông minh", khác với tầng "giảm hàm mất mát trên ImageNet".

---

## 7. Hiểu lầm thường gặp

| Nhận định | Sửa lại |
|----------|--------|
| "PAC nghĩa là luôn đúng trên tập kiểm tra." | Chỉ đảm bảo với xác suất $$1-\delta$$ và sai số $$\varepsilon$$ theo $$\mathcal{D}$$; không phải sai số bằng 0. |
| "Chiều VC hữu hạn thì học được trong thời gian đa thức." | Thống kê khác với việc tính được ERM. |
| "#P-đầy đủ nghĩa là không bao giờ đếm được." | Đây là độ khó tiệm cận trong trường hợp xấu nhất; các trường hợp nhỏ hoặc có cấu trúc vẫn đếm hoặc xấp xỉ được. |
| "Permanent khó vì công thức dài." | Nó khó vì phép quy dẫn #P; độ dài công thức không phải lý do về độ phức tạp. |
| "Deep learning đã thay thế PAC." | PAC vẫn là ngôn ngữ để đặc tả bài toán; deep learning bổ sung thiên kiến thuật toán và quy mô. |
| "Valiant chỉ làm học máy." | Lời trao giải còn gồm #P, tính toán đại số và tính toán song song. |

**Không nên nói.** "Đã có PAC nên vấn đề tổng quát hóa của mạng sâu đã xong." Các cận cổ điển có thể vô nghĩa trong trường hợp này; hiện tượng mới cần lý thuyết mới, đúng với tinh thần của Valiant: *đặt định nghĩa rồi chứng minh*.

---

## 8. Bài thực hành: đọc một định lý PAC

Danh sách câu hỏi khi đọc một định lý dạng "$$\mathcal{C}$$ học được hiệu quả theo PAC":

1. Miền là gì và khái niệm được biểu diễn thế nào (kích thước $$n$$)?  
2. Trường hợp khả thực hay bất khả tri?  
3. Người học được cung cấp gì: mẫu có nhãn độc lập cùng phân phối? Được phép hỏi nhãn của điểm tùy chọn (membership queries)?  
4. Thời gian và số mẫu phụ thuộc đa thức vào $$1/\varepsilon,1/\delta$$ như thế nào?  
5. Các kết quả *phủ định* dựa trên giả thiết mật mã hay độ phức tạp nào?  
6. Giả thuyết trả về có nằm trong $$\mathcal{C}$$ không (học đúng lớp, proper), hay điều kiện này được bỏ (học ngoài lớp, improper)?

Học ngoài lớp, tức là trả về $$h$$ không thuộc $$\mathcal{C}$$, đôi khi dễ hơn học đúng lớp; đây là chi tiết quan trọng khi đọc bài báo.

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Video dùng để **định hướng và làm quen với không khí nghiên cứu**, không thay thế chứng minh. Chi tiết: `research/video-research/valiant-learning/`.

**Ý chính rút ra từ bộ tư liệu**

- Valiant, Giải Turing 2010: học PAC, xem việc học như một bài toán về độ phức tạp.

**Thứ tự xem gợi ý**


**Trang chính thức và tài liệu**

- Trang Giải Turing của Valiant: https://amturing.acm.org/award_winners/valiant_2612174.cfm  
- Bộ ba Deep Learning, Giải Turing 2018: https://amturing.acm.org/award_winners/hinton_4791679.cfm  

Danh sách URL đầy đủ: `research/video-research/valiant-learning/references.md`.

## Tài liệu tham khảo


### Bộ tư liệu nghiên cứu video (mọi URL)

Danh sách đầy đủ: `research/video-research/valiant-learning/references.md`.

1. Valiant Turing page — https://amturing.acm.org/award_winners/valiant_2612174.cfm  
2. Wikipedia — Leslie Valiant — https://en.wikipedia.org/wiki/Leslie_Valiant  
3. Wikipedia — Probably approximately correct learning — https://en.wikipedia.org/wiki/Probably_approximately_correct_learning  
4. Wikipedia — Computational learning theory — https://en.wikipedia.org/wiki/Computational_learning_theory  
5. Valiant PAC paper culture (CACM / JACM lineage) — https://dl.acm.org/doi/10.1145/1968.1972  
6. Deep Learning Trio Turing 2018 — https://amturing.acm.org/award_winners/hinton_4791679.cfm  
7. Wikipedia — VC dimension (related theory) — https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_dimension  
8. ACM awards page Valiant — https://awards.acm.org/award-recipients/valiant_2612174  
9. Thư mục bộ tư liệu: `research/video-research/valiant-learning/`.

1. ACM Turing Award — Leslie Valiant (2010).  
2. Valiant — "A theory of the learnable" (*Communications of the ACM*; bài báo đặt nền cho PAC).  
3. Kearns & Vazirani — *An Introduction to Computational Learning Theory*.  
4. Arora & Barak — các chương về độ phức tạp bài toán đếm và permanent.  
5. Trong khóa học: [Lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/); [Toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/); [Độ phức tạp tính toán]({{ site.baseurl }}/contents/vi/chapter06/06_07_Complexity_Theory/); [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/).

---

## Hướng đi tiếp

- Thống kê nhiều chiều và hiện tượng tập trung độ đo: [Talagrand / Abel]({{ site.baseurl }}/contents/vi/chapter08/08_09_Talagrand_Probability/) và [Hình học nhiều chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/).  
- Deep learning, thực tiễn và lý thuyết: [Bengio–Hinton–LeCun]({{ site.baseurl }}/contents/vi/chapter09/09_12_Deep_Learning_Trio/).  
- Nhân quả, vượt ra ngoài giả thiết độc lập cùng phân phối: [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/).  
- Thực hành: học một khoảng trên $$\mathbb{R}$$ bằng ERM; vẽ sai số huấn luyện và kiểm tra theo $$m$$.  
- Đọc thêm: bài giới thiệu PAC của Valiant năm 1984 → Kearns–Vazirani chương 1–3 → một bài tổng quan về học DNF.  
- Bài tiếp theo: [Hopcroft–Tarjan]({{ site.baseurl }}/contents/vi/chapter09/09_10_Hopcroft_Tarjan/).

## Video tham khảo

- **Xem trước:** [Machine learning: Lecture 12b: PAC learning introduction](https://www.youtube.com/watch?v=XAwUQLYr5ZE) — UofU Data Science, tiếng Anh. Bài giảng nhập môn về định nghĩa học PAC; nên xem trước khi đọc bài.
- [The Computational Universe - Leslie Valiant](https://www.youtube.com/watch?v=KHPe7o6jjIU) — Institute for Advanced Study, tiếng Anh. Valiant trình bày cách nhìn của ông về vũ trụ tính toán; nên xem sau khi đã nắm ý chính của bài.
- [Prof. Leslie Valiant (Harvard) : What Needs to be Added to Machine Learning?](https://www.youtube.com/watch?v=nAMKHfqW2cw) — Computational Complexity, tiếng Anh. Xem thêm sau hai video trên, về những gì học máy hiện nay còn thiếu theo Valiant.
