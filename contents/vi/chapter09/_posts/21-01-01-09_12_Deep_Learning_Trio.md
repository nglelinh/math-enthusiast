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

**Yoshua Bengio**, **Geoffrey Hinton** và **Yann LeCun** cùng nhận **Giải Turing (A.M. Turing Award) năm 2018**, với lời ghi nhận như sau:

> “for conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing.”  
> — [ACM Turing Award](https://amturing.acm.org/)

Tạm dịch: vì những đột phá về khái niệm lẫn kỹ thuật đã đưa mạng nơ-ron sâu trở thành một thành phần thiết yếu của ngành tính toán.

Giải thưởng này không dành cho một ứng dụng trò chuyện nào. Nó dành cho ba người đã theo đuổi suốt nhiều thập niên một niềm tin: biểu diễn phân tầng, lan truyền ngược gradient, phép tích chập và học không giám sát (tự mã hóa) có thể trở thành hạ tầng tính toán, miễn là dữ liệu, GPU và kỹ thuật huấn luyện theo kịp ý tưởng. Bài này tách phần cơ chế toán học (các lớp mạng, hàm mất mát, lan truyền ngược, thiên kiến quy nạp) ra khỏi sự quảng cáo sản phẩm. Bài cũng đặt ba người này bên cạnh [toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/), [lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/), [Valiant]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/) và [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/).

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- viết một lớp mạng $$x\mapsto \sigma(Wx+b)$$ và nhìn cả mạng như một phép hợp thành các ánh xạ;
- giải thích thuật toán lan truyền ngược (backpropagation) như quy tắc đạo hàm hàm hợp trên đồ thị tính toán;
- mô tả mạng nơ-ron tích chập (CNN) với phép tích chập, chia sẻ trọng số và gộp (pooling) như một thiên kiến quy nạp (inductive bias) về tính cục bộ và tính bất biến khi tịnh tiến;
- nêu những đóng góp tiêu biểu của từng người: Hinton (máy Boltzmann, mạng tin cậy sâu, dropout, câu hỏi về mạng capsule, “tri thức tối” trong chưng cất mô hình), LeCun (mạng tích chập, nhận dạng chữ viết tay, học tự giám sát gần đây), Bengio (học biểu diễn, cơ chế chú ý và mô hình chuỗi sang chuỗi, mô hình sinh);
- phân biệt thành công thực nghiệm có thể tái lập với định lý tổng quát hóa đã được chứng minh;
- phê phán những khẩu hiệu như “học sâu giải xong P vs NP” hay “học sâu thay thế khoa học”.

**Kiến thức nền.** Vector và ma trận, đạo hàm, bài toán học có giám sát ở mức cơ bản. Bài [Đại số tuyến tính cho AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/) sẽ giúp ích.

---

## 1. Ba con đường, một hướng đi

Trong những năm 1990 và 2000, mạng nơ-ron không phải là trung tâm của học máy chính thống. Máy vector hỗ trợ (SVM), boosting và mô hình đồ thị xác suất mới là những hướng được chú ý nhiều hơn. Ba người này, cùng cộng đồng quanh họ, vẫn giữ vững hướng mạng sâu: xếp nhiều lớp phi tuyến để máy tự học đặc trưng, thay vì chỉ phân loại trên những đặc trưng do con người thiết kế.

Giải Turing 2018 ghi nhận những người đã định hình cả một lĩnh vực, giống tinh thần của giải Abel dành cho Serre: họ đào tạo học trò, viết bài báo, xây hệ thống (mạng tích chập dùng được trong thực tế, văn hóa tính toán bằng GPU) và đưa vào từ vựng khái niệm “học biểu diễn” (representation learning). Hãy chú ý lời ghi nhận nói đến cả “khái niệm” lẫn “kỹ thuật”, không chỉ có định lý.

---

## 2. Mạng sâu là phép hợp thành các ánh xạ

### Một lớp mạng

$$
h^{(\ell)}=\sigma\big(W^{(\ell)} h^{(\ell-1)}+b^{(\ell)}\big),\qquad h^{(0)}=x.
$$

Hàm $$\sigma$$ là hàm phi tuyến áp dụng lên từng tọa độ (ReLU, sigmoid theo cách dùng trong lịch sử, tanh, ...). Nếu bỏ phi tuyến, nhiều lớp tuyến tính xếp chồng chỉ còn là một ánh xạ affine duy nhất. Độ sâu làm thay đổi lớp hàm mà mạng biểu diễn được một cách hiệu quả. Mạng nông cũng xấp xỉ được mọi hàm liên tục trên tập compact (định lý xấp xỉ phổ quát), nhưng mức độ hiệu quả và quá trình tối ưu thì phụ thuộc nhiều vào độ sâu và kiến trúc.

### Học là tối ưu hóa tham số

$$
\min_\theta \frac{1}{N}\sum_{i=1}^N \ell\big(f_\theta(x_i),y_i\big)+\Omega(\theta).
$$

Các thuật toán SGD và Adam cập nhật $$\theta$$ bằng gradient ước lượng trên từng lô nhỏ (mini-batch). Hàm mục tiêu **không lồi**, nên lý thuyết hội tụ lồi cổ điển không giải thích được hết, nhưng trong thực nghiệm phương pháp vẫn chạy tốt ở quy mô lớn. Khoảng trống giữa hai điều này chính là đề tài của [lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/) hiện đại. Đó không phải là lỗi “chưa dùng SGD đúng như sách giáo khoa thập niên 1980”.

### Lan truyền ngược

Đồ thị tính toán là một đồ thị có hướng. Mỗi nút có ma trận Jacobian cục bộ của riêng nó. Chế độ ngược của đạo hàm tự động (reverse-mode automatic differentiation) nhân các Jacobian này dọc theo chuỗi, đi từ hàm mất mát ngược về các tham số. Chi phí tính toán cùng bậc với một lượt tính xuôi, tức tỉ lệ với số cạnh của đồ thị. Đây là một **kỹ thuật tính đạo hàm tự động**, không phải phép màu tạo ra trí tuệ. Hinton cùng các đồng nghiệp đã phổ biến việc huấn luyện mạng nhiều lớp bằng cách này, còn phương pháp chế độ ngược có lịch sử rộng hơn nhiều, chẳng hạn trong lý thuyết điều khiển với phương pháp liên hợp (adjoint).

---

## 3. LeCun: tích chập và thiên kiến quy nạp cho thị giác

### Phép tích chập

Ảnh có hai tính chất: thông tin mang tính **cục bộ**, và nội dung gần như **không đổi khi tịnh tiến**. Vì vậy người ta cho một nhân (kernel) nhỏ trượt qua ảnh:

$$
(K*X)_{ij}=\sum_{u,v} K_{uv}\, X_{i+u,j+v},
$$

Việc dùng chung một nhân ở mọi vị trí (chia sẻ trọng số) làm số tham số giảm mạnh so với lớp kết nối đầy đủ trên các điểm ảnh. Phép gộp hoặc bước trượt (stride) làm giảm độ phân giải, còn xếp nhiều lớp chồng lên nhau thì mở rộng trường tiếp nhận (receptive field).

**LeNet**, mạng nhận dạng chữ viết tay, là minh chứng thực tế sớm cho cách làm này: tích chập, lan truyền ngược và dữ liệu thật. Cũng không nên nói “năm 2012 ImageNet phát minh ra học sâu”. Điều xảy ra năm 2012 (AlexNet, từ nhóm của Hinton) là sự kết hợp của quy mô lớn, GPU, ReLU và dropout, đủ để thuyết phục cả cộng đồng.

### Học tự giám sát và mô hình dựa trên năng lượng

LeCun nhấn mạnh việc học biểu diễn với rất ít nhãn: học đối sánh (contrastive learning), nhúng chung (joint embedding), mô hình thế giới (world models). Chương trình “máy học như động vật” này dùng ngôn ngữ của lý thuyết thông tin và của năng lượng. Cần nhớ đây là một **chương trình nghiên cứu**: một phần đã thành kỹ thuật vững chắc, một phần vẫn còn là giả thuyết.

---

## 4. Hinton: từ máy Boltzmann đến “tri thức”

### Tiền huấn luyện và mạng tin cậy sâu

Trước khi có ReLU và các cách huấn luyện dễ hơn, việc **tiền huấn luyện không giám sát theo từng lớp** (máy Boltzmann hạn chế RBM, mạng tin cậy sâu DBN) giúp mạng sâu có điểm khởi đầu tốt. Quy trình hiện đại ít dùng RBM, nhưng bài học vẫn còn: khi bài toán tối ưu khó, **cách khởi tạo và thứ tự học từ dễ đến khó** rất quan trọng.

### Dropout và chưng cất mô hình

Dropout vừa là một cách điều chuẩn, vừa có thể xem như xấp xỉ một tập hợp nhiều mô hình (ensemble). **Chưng cất mô hình** (distillation), hay “tri thức tối” (dark knowledge): nhãn mềm của một mạng lớn được dùng để dạy một mạng nhỏ, vì thông tin nằm trong cả phân bố xác suất chứ không chỉ ở lớp có xác suất cao nhất. Ý tưởng chuyển giao tri thức này sống tiếp trong nén mô hình và trong cách học thầy–trò (teacher–student).

### Hoài nghi về một số hướng đi

Hinton công khai tỏ ra nghi ngờ một số hướng, như mạng capsule hay cách “chỉ cần xếp thêm nhiều transformer”, dù cộng đồng đã chọn con đường khác. Giải Turing vinh danh những **đóng góp đã định hình lĩnh vực**, chứ không bảo đảm mọi nhận định sau năm 2018 đều đúng. Người đoạt giải không phải là nhà tiên tri.

---

## 5. Bengio: biểu diễn, chuỗi và mô hình sinh

### Học biểu diễn

Bengio hệ thống hóa và truyền bá một mục tiêu: không chỉ làm giảm hàm mất mát trên tập huấn luyện, mà còn học các **đặc trưng tách bạch và dùng lại được**. Các bài tổng quan về học biểu diễn của ông là cầu nối giữa ý tưởng lấy cảm hứng từ khoa học thần kinh và ngôn ngữ tối ưu hóa.

### Chuỗi và cơ chế chú ý

Mô hình chuỗi sang chuỗi (seq2seq) và cơ chế chú ý (attention) mở đường cho xử lý ngôn ngữ tự nhiên bằng mạng nơ-ron trước khi transformer chiếm ưu thế. Nhiều nhóm cùng đóng góp, trong đó có Bahdanau, Cho và Bengio, và có những công trình song song khác. **Mô hình sinh** (GAN và các mô hình khuếch tán, dòng chuẩn hóa ở gần đó) đưa yếu tố xác suất vào mạng nơ-ron.

### Tổng quát hóa và nhu cầu có lý thuyết

Bengio thường nối học sâu với nhân quả, với suy luận chậm có chủ đích (kiểu “Hệ thống 2”) và với bài toán dữ liệu ngoài phân bố huấn luyện (out-of-distribution). Ở tầm chương trình nghiên cứu, những hướng này gặp [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/), nhưng chưa thể nói là đã giải quyết xong.

---

## 6. Toán học còn thiếu gì sau giải Turing 2018

Dưới đây là danh sách thẳng thắn, không bi quan:

1. **Tối ưu hóa:** khi nào SGD tìm được điểm cực tiểu tốt (gần như toàn cục) trong chế độ có quá nhiều tham số (overparameterized)?  
2. **Tổng quát hóa:** các chặn kiểu VC thường quá lỏng để có ý nghĩa; cần xét thiên lệch của thuật toán và cấu trúc của dữ liệu.  
3. **Độ bền vững:** ví dụ đối nghịch (adversarial examples) và sự dịch chuyển phân bố dữ liệu.  
4. **Hiệu quả theo số mẫu:** so với việc học của sinh vật, mạng cần nhiều dữ liệu hơn rất nhiều.  
5. **Suy luận và tính hợp thành (compositionality)** bền vững, vượt ra ngoài việc khớp mẫu.  
6. **Mô hình nền tảng (foundation models):** các định luật mở rộng quy mô (scaling laws) rút ra từ thực nghiệm so với lý thuyết về sức chứa của mô hình.

[Toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/) và [hình học không gian nhiều chiều]({{ site.baseurl }}/contents/vi/chapter06/06_08_High_Dimensional_Geometry/) cung cấp công cụ, nhưng danh sách này vẫn còn mở.

### Suy giảm kép và nội suy

Mạng rất rộng có thể khớp cả nhiễu mà vẫn dự đoán tốt trên dữ liệu có cấu trúc. Quan niệm quen thuộc rằng sai số theo độ phức tạp mô hình có hình chữ U không còn đủ. Đây là một *hiện tượng* đã có mô hình đơn giản để nghiên cứu (hồi quy tuyến tính không điều chuẩn, đặc trưng ngẫu nhiên), nhưng chưa phải định lý áp dụng cho mọi transformer.

### Mạng phần dư, chuẩn hóa và kỹ thuật để mạng huấn luyện được

ResNet viết mỗi lớp dưới dạng $$x\mapsto x+f_\theta(x)$$. Nhờ đó gradient có đường đi tắt, và mạng rất sâu trở nên *huấn luyện được*. Chuẩn hóa theo lô (batch normalization) và chuẩn hóa theo lớp (layer normalization) điều chỉnh thang đo của các giá trị kích hoạt. Lịch trình tốc độ học và cách khởi tạo trọng số (He, Xavier) là một nửa thực dụng của câu chuyện “học sâu chạy được”. Nên hiểu rằng đây là việc **thiết kế một hệ động lực rời rạc** (ánh xạ lặp ổn định), chứ không đơn giản là “thêm lớp cho vui”. Phân tích theo thời gian liên tục (dòng gradient, ODE nơ-ron) là cầu nối sang [hệ động lực và tư duy kiểu phương trình đạo hàm riêng]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/). Cách này hữu ích, nhưng chưa thay thế được các thí nghiệm cắt bỏ thành phần (ablation) trong thực nghiệm.

### Cơ chế chú ý là dạng song tuyến tính kết hợp softmax

Cơ chế tự chú ý (self-attention), viết ở dạng sơ đồ, lấy ba loại vector truy vấn, khóa và giá trị (query, key, value) bằng các phép biến đổi tuyến tính từ các token, rồi tính tích vô hướng:

$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\Big(\frac{QK^\top}{\sqrt{d}}\Big)V
$$

và trộn thông tin toàn cục ngay trong một lớp. Thiên kiến quy nạp ở đây khác với CNN: không có ràng buộc cục bộ cứng trên lưới ảnh, mà được bù bằng dữ liệu và mã hóa vị trí. Transformer chiếm ưu thế trong xử lý ngôn ngữ và thị giác sau năm 2017, còn di sản seq2seq cộng cơ chế chú ý của nhóm Bengio vẫn là tiền sử về mặt khái niệm. Ý chính cần nhớ: **mọi “cuộc cách mạng kiến trúc” thực chất là chọn một lớp hàm và cách buộc chung tham số**, rồi giao việc còn lại cho SGD và dữ liệu.

---

## 7. Học sâu với độ phức tạp, mật mã và hệ thống

- Học sâu **không** làm sụp [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): một phương pháp heuristic chạy tốt trên các thể hiện cụ thể không phải là thuật toán đa thức trong trường hợp xấu nhất cho bài toán NP-đầy đủ.  
- **Quyền riêng tư và an ninh:** các cuộc tấn công đảo ngược mô hình (model inversion) và trích xuất dữ liệu liên quan đến mật mã ứng dụng, và gặp lại ở bài [Chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/).  
- **Hệ thống:** CUDA, trình biên dịch và phép all-reduce phân tán là nửa kỹ thuật trong lời ghi nhận “thành phần thiết yếu của ngành tính toán”.

Giải Turing 2018 nằm ở ranh giới giữa **toán rời rạc, xác suất và tối ưu hóa** với **hạ tầng tính toán**, đúng với tinh thần của chương 09.

---

## 8. Những nhầm lẫn thường gặp

| Tuyên bố | Chỉnh lại |
|----------|--------|
| “Lan truyền ngược nghĩa là AI đã hiểu bộ não.” | Đó là đạo hàm tự động trên đồ thị; chưa có bằng chứng rằng não dùng lan truyền ngược. |
| “CNN chỉ là nhiều bộ lọc đẹp.” | Chia sẻ trọng số cộng tính cục bộ chính là một thiên kiến quy nạp có nền tảng toán học. |
| “Có giải 2018 nghĩa là lý thuyết học sâu đã xong.” | Đột phá về kỹ thuật không đồng nghĩa với một lý thuyết đã hoàn chỉnh. |
| “Tăng quy mô giải được mọi bài toán ngoài phân bố và nhân quả.” | Quy mô lớn có giúp, nhưng không thay được việc xác định mô hình và can thiệp. |
| “PAC của Valiant đã lỗi thời.” | PAC vẫn là cách đặc tả bài toán học; học sâu bổ sung thêm kiến trúc và vấn đề tối ưu. |
| “Ba người này phát minh ra mạng nơ-ron từ thập niên 1940.” | McCulloch–Pitts, Rosenblatt, Rumelhart và các cộng sự mới là tiền sử; ba người định hình học *sâu* hiện đại. |

---

## 9. Cách đọc một bài báo về học sâu

Danh sách kiểm tra:

1. Kiến trúc: thiên kiến quy nạp là gì (tích chập, chú ý, phần dư)?  
2. Hàm mất mát và dữ liệu: học có giám sát, tự giám sát hay học tăng cường?  
3. Đối chứng (baseline) và thí nghiệm cắt bỏ (ablation): mức cải thiện đến từ đâu?  
4. Bài báo có kết quả lý thuyết hay chỉ có bảng số liệu?  
5. Tài nguyên tính toán: có thể tái lập được không?  
6. Bài báo có nêu kết quả âm tính và các trường hợp thất bại không?

Hiểu giới hạn của một kết quả quan trọng hơn việc thuộc tên mọi biến thể của Adam.

---

## Bài tập

1. Viết lượt tính xuôi cho mạng hai lớp kết nối đầy đủ với ReLU, đầu vào $$x\in\mathbb{R}^d$$.  
2. Giải thích ngắn gọn vì sao giữa các lớp tuyến tính bắt buộc phải có phi tuyến.  
3. So sánh lớp kết nối đầy đủ trên ảnh $$28\times 28$$ với lớp tích chập 3×3: số tham số khác nhau cỡ bao nhiêu (chỉ cần bậc độ lớn)?  
4. Dropout làm gì lúc huấn luyện và lúc kiểm tra (tóm tắt ngắn)?  
5. **Tối đa 250 từ:** giải Turing 2018 ghi nhận “khái niệm và kỹ thuật” (conceptual and engineering). Với mỗi từ, hãy nêu một ví dụ lấy từ bài.  
6. Liên hệ với [lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/): vì sao hàm mất mát trên tập huấn luyện bằng 0 vẫn không bảo đảm rủi ro thấp.  
7. Chọn một bản tóm tắt trên arXiv (2024–26) về “lý thuyết cho mô hình nền tảng”, rồi gắn nhãn từng phát biểu là định lý, định luật mở rộng quy mô hay suy đoán.

---


## Video và tài liệu

Các video gợi ý nằm ở phần *Video tham khảo* cuối bài. Hãy dùng video để làm quen với bối cảnh, không dùng thay cho chứng minh.

## Tài liệu tham khảo trực tuyến



1. Trang giải Turing của Hinton — https://amturing.acm.org/award_winners/hinton_4791679.cfm  
2. Trang giải Turing của LeCun — https://amturing.acm.org/award_winners/lecun_6017366.cfm  
3. Trang giải Turing của Bengio — https://amturing.acm.org/award_winners/bengio_3406375.cfm  
4. ACM 2018 Turing announcement — https://awards.acm.org/about/2018-turing  
5. Wikipedia — Deep learning — https://en.wikipedia.org/wiki/Deep_learning  
6. Wikipedia — Backpropagation — https://en.wikipedia.org/wiki/Backpropagation  
7. Wikipedia — Convolutional neural network — https://en.wikipedia.org/wiki/Convolutional_neural_network  
8. Giải Turing của Valiant (PAC, tiền thân của lý thuyết học) — https://amturing.acm.org/award_winners/valiant_2612174.cfm  
9. Bài liên quan trong khóa: chương 6, Toán của AI  

1. ACM Turing Award — Bengio, Hinton, LeCun (2018).  
2. Goodfellow, Bengio, Courville — *Deep Learning* (MIT).  
3. LeCun, Bengio, Hinton — “Deep learning” (*Nature* 2015), bài tổng quan.  
4. Các công trình lịch sử: LeNet; AlexNet; các bài về DBN, dropout và seq2seq với cơ chế chú ý.  
5. Trong khóa: [toán học của AI]({{ site.baseurl }}/contents/vi/chapter06/06_02_Mathematics_of_AI/); [lý thuyết học máy]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/); [đại số tuyến tính cho AI]({{ site.baseurl }}/contents/vi/chapter03/03_03_Linear_Algebra_AI/); [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/); [Valiant]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/).

---

## Hướng đi tiếp

- Độ cứng và tính ngẫu nhiên: [Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/).  
- Nhân quả khi dữ liệu ngoài phân bố: [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/).  
- Thực hành: huấn luyện một CNN nhỏ trên MNIST; thử bỏ tích chập, thay bằng lớp kết nối đầy đủ; so sánh số tham số và độ chính xác.  
- Đọc: bài tổng quan trên Nature 2015, rồi một chương sách của Goodfellow, rồi một bài báo về học tự giám sát.  
- Bài tiếp theo: [Wigderson]({{ site.baseurl }}/contents/vi/chapter09/09_13_Wigderson_Complexity/).

## Video tham khảo

- **Xem trước** — [ACM A.M. Turing Award 2018: Yoshua Bengio, Yan Lecun and Geoffrey Hinton](https://www.youtube.com/watch?v=HzilDIhWhrE) — Association for Computing Machinery (ACM), tiếng Anh. Xem trước để làm quen với chủ đề.
- [Geoffrey Hinton and Yann LeCun, 2018 ACM A.M. Turing Award Lecture "The Deep Learning Revolution"](https://www.youtube.com/watch?v=VsnQf7exv5I) — Association for Computing Machinery (ACM), tiếng Anh. Xem sau khi đã nắm ý chính.
- [AAAI 20 / AAAI 2020 Keynotes Turing Award Winners Event / Geoff Hinton, Yann Le Cunn, Yoshua Bengio](https://www.youtube.com/watch?v=UX8OubxsY8w) — ICML IJCAI ECAI 2018 Conference Videos, tiếng Anh. Góc nhìn bổ sung.
