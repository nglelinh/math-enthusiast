---
layout: post
title: "Ứng dụng hiện đại: Chủ đề Turing, 2022–2026"
chapter: '09'
order: 15
owner: Nguyen Le Linh
lang: vi
categories:
- chapter09
lesson_type: optional
---

Nếu một nhà khoa học máy tính từ năm 2018 — đúng năm bộ ba học sâu nhận Giải Turing — bước vào phòng thí nghiệm năm 2025, họ sẽ bất ngờ trước ba cảnh tượng diễn ra song song. Ở phòng thứ nhất, các kỹ sư không còn đua nhau bơm kích thước mô hình ngôn ngữ lớn nhất có thể, mà tính toán cực kỳ chi li cách chia một ngân sách phép tính (FLOPs) cố định giữa số tham số và lượng dữ liệu theo **quy luật Chinchilla**. Ở phòng thứ hai, một tác nhân học tăng cường mang tên **AlphaProof** ngồi viết chứng minh toán học cho đề thi Olympic Toán Quốc tế (IMO) bằng ngôn ngữ hình thức **Lean** — và từng dòng suy luận đều bị hạt nhân logic kiểm duyệt gắt gao không thể "ảo giác". Ở phòng thứ ba, kiến trúc **Transformer** không chỉ dự đoán từ tiếp theo mà còn đang học cách ước lượng kết quả *phản thực* cho bệnh nhân theo từng ngày điều trị, đưa tinh thần nhân quả của Pearl vào chuỗi thời gian sâu!

Bài đọc thêm này đóng vai trò một **bản cập nhật giai đoạn 2022–2026** bổ sung trực tiếp vào tấm bản đồ ở bài [Chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/): không lặp lại các chủ đề về quyền riêng tư vi phân, mã sửa lỗi hay lượng tử, mà soi kính lúp vào chính ba điểm giao cắt mới mẻ ấy giữa tối ưu hóa, kiểm chứng hình thức và suy luận nhân quả.

## Mục tiêu học tập

Sau bài tùy chọn này, bạn có thể:

- Thêm ba ví dụ cụ thể giai đoạn 2022–2026 vào bản đồ vùng biên Toán–CS: huấn luyện tối ưu theo ngân sách tính toán (Chinchilla), tác nhân giải toán Olympic dùng trợ lý chứng minh Lean (AlphaProof), và mô hình chuỗi nhân quả (Causal Transformer).
- Phân biệt rõ đâu là *quy luật thực nghiệm*, đâu là *kiểm chứng hình thức bằng kernel*, và đâu là *kiến trúc xấp xỉ nguyên lý nhân quả*.
- Nối cả ba bước tiến hiện đại này về các nền tảng của Chương 9 (Valiant, bộ ba học sâu, Pearl và văn hóa kiểm chứng).

## Kiến thức cần nhớ: Quy luật mở rộng quy mô, Chứng minh hình thức bằng AI và Học máy nhân quả là gì, nghiên cứu những gì?

Ba cập nhật trong bài đại diện cho ba câu hỏi toán–tin sắc bén nhất của giai đoạn 2022–2026:

1. **Tối ưu hóa dưới ràng buộc ngân sách tính toán (Compute-Optimal Scaling):** Huấn luyện một mô hình ngôn ngữ có $$N$$ tham số trên $$D$$ token tốn xấp xỉ $$C \approx 6ND$$ phép tính dấu phẩy động (FLOPs). Thay vì tối ưu không ràng buộc, Hoffmann và cộng sự (2022) giải bài toán tối ưu có ràng buộc: *với ngân sách $$C$$ cố định, chọn cặp $$(N, D)$$ nào để hàm mất mát đạt cực tiểu?* Kết quả thực nghiệm cho thấy $$N$$ và $$D$$ cần tăng theo tỉ lệ cân bằng (khoảng **20 token cho mỗi tham số** — do đó mô hình Chinchilla 70 tỉ tham số huấn luyện trên 1.4 nghìn tỉ token đánh bại hoàn toàn mô hình Gopher 280 tỉ tham số nhưng thiếu dữ liệu!).
2. **Học tăng cường trong môi trường chứng minh hình thức (Formal Mathematical Reasoning):** Điểm yếu cố hữu của LLM khi làm toán bằng tiếng tự nhiên là khó kiểm soát bước suy luận sai. Khi chuyển sang ngôn ngữ trợ lý chứng minh như **Lean 4**, mỗi bước chứng minh (tactic) là một nước đi trong trò chơi logic, và **kernel** (hạt nhân kiểm chứng nhỏ gọn) trả về tín hiệu Đúng/Sai tuyệt đối chính xác. Học tăng cường (như AlphaProof) tận dụng chính tín hiệu không-ảo-giác này để tìm kiếm chứng minh ở tầm huy chương bạc IMO 2024.
3. **Học máy nhân quả trên dữ liệu chuỗi thời gian (Sequential Causal Inference):** Trong y khoa (như hồ sơ ICU theo từng giờ), liều thuốc $$A_t$$ tại giờ $$t$$ phụ thuộc vào chỉ số bệnh nhân $$X_t$$ và các liều trước đó — tạo nên mạng lưới biến nhiễu phụ thuộc thời gian (*time-varying confounding*). **Causal Transformer** kết hợp cơ chế tự chú ý với hàm mất mát đối kháng để học biểu diễn ẩn trung hòa biến nhiễu, giúp ước lượng câu hỏi phản thực *"nếu đổi phác đồ điều trị từ giờ thứ 3 thì diễn biến bệnh nhân sẽ ra sao?"*.

## Kiến thức cần có

Bài [Chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/), cùng các bài về giải thưởng làm điểm xuất phát: [bộ ba học sâu]({{ site.baseurl }}/contents/vi/chapter09/09_12_Deep_Learning_Trio/), [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/), [Valiant]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/).

## Phát triển khái niệm

Hoffmann và cộng sự (2022) coi số phép tính (FLOPs) là một ngân sách cần chia giữa số tham số $$N$$ và số token $$D$$. AlphaProof coi việc tìm các bước chứng minh (tactic) trong Lean như một môi trường học tăng cường, trong đó phần thưởng là việc kernel của Lean chấp nhận chứng minh. Một Causal Transformer coi quỹ đạo $$(X_t,A_t,Y_t)$$ như một chuỗi và cố ước lượng kết quả phản thực nếu thực hiện một chuỗi hành động khác. Đây chính là ý của Pearl, “can thiệp $$\neq$$ điều kiện hóa”, nay được đưa vào một kiến trúc mạng.

### Ví dụ làm từng bước: Chia ngân sách FLOPs theo Chinchilla và ma trận che nhân quả 3×3

Hãy tự tay thực hiện hai phép tính ngắn để thấy các thuật ngữ hiện đại 2022–2026 bám chặt vào đại số và tối ưu hóa sơ cấp như thế nào:

**Phần A — Chia một ngân sách GPU cố định $$C = 6 \times 10^{23}$$ FLOPs.** Với công thức gần đúng $$C \approx 6ND$$, ngân sách cố định tương đương ràng buộc tích $$N \cdot D = 10^{23}$$. Hãy so sánh hai chiến lược phân bổ trên cùng một hóa đơn tiền điện GPU:
- **Chiến lược A (kiểu Gopher — bơm to mô hình):** Chọn $$N_A = 280 \times 10^9$$ tham số (280 tỉ). Khi đó lượng dữ liệu tối đa còn lại chỉ là $$D_A = \dfrac{10^{23}}{2{,}8 \times 10^{11}} \approx \mathbf{357 \times 10^9}$$ token — tức chỉ khoảng $$1{,}28$$ token cho mỗi tham số (mô hình "đói dữ liệu" nghiêm trọng!).
- **Chiến lược B (kiểu Chinchilla — giữ tỉ lệ vàng $$D \approx 20N$$):** Thế $$D = 20N$$ vào $$N \cdot D = 10^{23}$$:

$$
20 N_B^2 = 10^{23} \implies N_B = \sqrt{5 \times 10^{21}} \approx \mathbf{70{,}7 \times 10^9\text{ tham số}} \quad (\approx 70\text{B}),
$$

$$
D_B = 20 N_B \approx \mathbf{1{,}41 \times 10^{12}\text{ token}} \quad (\approx 1{,}4\text{T token}).
$$

Cùng đúng một ngân sách huấn luyện $$C$$, Chiến lược B vừa đạt hàm mất mát thấp hơn rõ rệt, vừa có kích thước nhỏ hơn **4 lần** nên chi phí chạy suy luận (inference) cho người dùng cuối cũng rẻ hơn 4 lần!

**Phần B — Ma trận che nhân quả (Causal Attention Mask) trên hồ sơ 3 ngày điều trị.** Giả sử một Causal Transformer theo dõi bệnh nhân qua 3 ngày $$t = 1, 2, 3$$, với ma trận điểm chú ý thô $$S$$ (hàng $$i$$ chú ý tới cột $$j$$). Để mô hình tại ngày $$t=2$$ **tuyệt đối không nhìn trộm** chỉ số hay kết quả của ngày tương lai $$t=3$$, ta cộng thêm ma trận mặt nạ tam giác dưới $$M$$ (ô phía trên đường chéo bằng $$-\infty$$) trước khi tính softmax theo từng hàng:

$$
S = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 5 \\ 1 & 1 & 1 \end{pmatrix}, \qquad M = \begin{pmatrix} 0 & -\infty & -\infty \\ 0 & 0 & -\infty \\ 0 & 0 & 0 \end{pmatrix} \implies S + M = \begin{pmatrix} 1 & -\infty & -\infty \\ 0 & 0 & -\infty \\ 1 & 1 & 1 \end{pmatrix}.
$$

Tính bằng tay hàng thứ 2 (ngày $$t=2$$) qua hàm $$\mathrm{softmax}(v)_j = \dfrac{e^{v_j}}{\sum_k e^{v_k}}$$: vì $$e^{-\infty} = 0$$ và $$e^0 = 1$$, ta thu được vector trọng số chú ý:

$$
\mathrm{softmax}(0,\; 0,\; -\infty) = \left(\frac{1}{1+1+0},\; \frac{1}{1+1+0},\; \frac{0}{2}\right) = \mathbf{(0{,}5,\; 0{,}5,\; 0)}.
$$

Dù điểm thô của tương lai $$S_{2,3} = 5$$ lớn áp đảo, mặt nạ nhân quả đã triệt tiêu hoàn toàn luồng thông tin ngược thời gian xuống đúng **0** — phần còn lại (triệt tiêu biến nhiễu từ quá khứ $$t=1, 2$$) được xử lý tiếp bởi hàm mất mát đối kháng để xấp xỉ phép can thiệp $$do(A_t)$$ của Pearl.

### Giải thích: Vì sao giai đoạn 2022–2026 nối thẳng về di sản Giải Turing

Ba câu chuyện trên không phải ba mốt công nghệ rời rạc, mà là ba nhịp nối dài trực tiếp các ý tưởng nền tảng của Chương 9:

1. **Bước 1 — Tối ưu hóa dưới ràng buộc tài nguyên (di sản Knuth & Bộ ba học sâu):** Quy luật Chinchilla nhắc lại bài học muôn thuở của khoa học máy tính: mọi phép tính đều có ngân sách. Thay vì hỏi *"mạng lớn vô hạn thì sao?"*, kỹ thuật hiện đại giải bài toán cực trị có ràng buộc trên đường đồng mức $$6ND = C$$.
2. **Bước 2 — Tách bạch *sáng tạo tìm kiếm* và *kiểm chứng tuyệt đối* (di sản Cook–Karp & Kiểm chứng hình thức):** Trong NP, tìm chứng cứ khó nhưng kiểm chứng lại dễ. AlphaProof khai thác đúng sự bất đối xứng này: mạng nơ-ron được tự do đề xuất các nước đi táo bạo (có thể sai), còn hạt nhân Lean đóng vai người kiểm chứng hoàn hảo không bao giờ bị đánh lừa.
3. **Bước 3 — Đưa cấu trúc nhân quả vào mạng sâu (di sản Pearl & Bengio):** Dự đoán tốt chuỗi quan sát không đủ để bác sĩ đổi phác đồ. Causal Transformer cho thấy cách ghép kiến trúc học sâu (bộ ba 2018) với yêu cầu loại bỏ confounding (Pearl 2011).
4. **Bước 4 — Giữ tỉnh táo giữa thực nghiệm và định lý:** Chinchilla là đường khớp thực nghiệm (phụ thuộc kiến trúc và chất lượng dữ liệu); AlphaProof vẫn cần người dịch đề sang Lean; Causal Transformer vẫn cần giả định không có biến nhiễu ẩn. Biết rõ giới hạn của mỗi bước tiến mới là dấu hiệu của người hiểu sâu.

**Kiểm tra nhanh.** Nếu ngân sách tính toán tăng gấp **100 lần** ($$C' = 100C$$), theo quy luật Chinchilla $$N \propto \sqrt{C}$$ và $$D \propto \sqrt{C}$$, số tham số tối ưu $$N$$ và số token tối ưu $$D$$ mỗi thứ tăng bao nhiêu lần? Cả hai đều tăng đúng **$$\sqrt{100} = 10$$ lần** (vì $$10 \times 10 = 100$$).

## Ba cập nhật (không phải một bản khảo sát thứ hai)

### 1. Huấn luyện tối ưu theo ngân sách tính toán và chủ đề tối ưu

Quy luật Chinchilla (tăng số token cùng với số tham số) đã thay đổi cách các phòng thí nghiệm chi tiền. Nó không thay thế định nghĩa PAC của Valiant hay câu chuyện lan truyền ngược của bộ ba học sâu. Nó là kết quả dễ thấy nhất của năm 2022 liên quan đến chủ đề tối ưu: một câu trả lời thực nghiệm cho câu hỏi “nên đầu tư vào đâu?” khi mỗi lần huấn luyện tốn cả một kho GPU. Hãy gọi đó là một quy luật thực nghiệm, rồi quay lại các bài về AI và lý thuyết học máy để tìm các định lý.

### 2. AlphaProof và chủ đề kiểm chứng

Kết quả đánh giá ở IMO 2024 (mức tương đương huy chương bạc, giải 4/6 bài kết hợp cùng AlphaGeometry 2) và bài báo trên *Nature* năm 2025 (Hubert và cộng sự) cho thấy một tác nhân có thể đề xuất chứng minh bằng Lean và được kernel chấm. Đây là khẩu hiệu của kiểm chứng hình thức được đưa vào thực tế: kiểm thử chỉ có thể không tìm thấy lỗi, còn kernel thì chấp nhận một chứng minh cụ thể. Các lưu ý ở Chương 5 vẫn đúng (chuyên gia vẫn phải hình thức hóa phát biểu, vẫn cần thêm tính toán, và bài tổ hợp vẫn chưa giải được). Điều Chương 9 muốn nhấn mạnh là cách nhìn theo *hệ thống*: một kernel đáng tin cộng với một bộ đề xuất học được là một kiến trúc mới ở biên giới toán–tin, chứ không phải một lời trích dẫn giải Turing.

### 3. Causal Transformer và Pearl

Melnychuk, Frauen và Feuerriegel (2022) giới thiệu Causal Transformer để ước lượng kết quả phản thực trên dữ liệu theo thời gian (ví dụ dữ liệu điều trị kiểu MIMIC). Hàm mất mát đối kháng được dùng để biểu diễn *không* dự đoán được phương pháp điều trị hiện tại; đó là một phiên bản học sâu của việc chặn đường back-door. Điều này không làm do-calculus lỗi thời. Nó cho thấy các đối tượng của Pearl trông ra sao khi biến đồng hành là một chuỗi.

## Diễn giải và nhận định

Bài chủ đề hiện đại đã nhắc rằng áp lực triển khai tạo ra các định nghĩa. Chinchilla tạo ra một định nghĩa thực dụng về “đủ dữ liệu”. AlphaProof tạo ra một định nghĩa thực dụng về “đủ hình thức để chấm điểm”. Causal Transformer tạo ra một định nghĩa theo kiến trúc về “biểu diễn cân bằng”. Không định nghĩa nào trong số đó thay thế được DP, mã cực (polar code) hay thuật toán Shor.

## Giới hạn và hướng mở rộng

Đừng bỏ qua bản khảo sát mà chỉ đọc bài này. Quyền riêng tư, lý thuyết mã và tính toán lượng tử không hề dừng lại từ năm 2021; chúng không được nhắc ở đây vì bản khảo sát đã đề cập, và vì FIPS 203 đã được nói đến ở Chương 3 và 6.

## Tài liệu tham khảo

- Hoffmann, J., et al. (2022). Training compute-optimal large language models. *NeurIPS*. [arXiv:2203.15556](https://arxiv.org/abs/2203.15556).
- Google DeepMind. (2024). AI achieves silver-medal standard solving IMO problems. [blog](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/).
- Hubert, T., et al. (2025). Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature*. [doi:10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y).
- Melnychuk, V., Frauen, D., & Feuerriegel, S. (2022). Causal Transformer for estimating counterfactual outcomes. *ICML*. [arXiv:2204.07258](https://arxiv.org/abs/2204.07258).
- Bài khảo sát: [Chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/).

## Video tham khảo

- **Xem trước** — [Chinchilla Explained: Compute-Optimal Massive Language Models](https://www.youtube.com/watch?v=PZXN7jm9IC0) — Edan Meyer, tiếng Anh. Giúp nắm sự đánh đổi giữa số tham số và số token trong huấn luyện tối ưu theo ngân sách tính toán (Chinchilla). Đây là video giải thích bài báo về scaling, không phải bài giảng của chính các tác giả.
- [Improving on AlphaProof: IMO 2024 Problem 2 in Lean 4](https://www.youtube.com/watch?v=5IARsdn78xE) — David Renshaw, tiếng Anh. Một bản hình thức hóa bằng Lean 4 cho bài IMO 2024, theo tinh thần AlphaProof. Dùng cùng với phần về kiểm chứng; đây không phải bài nói chính thức của DeepMind.
- [Keynote: Judea Pearl - The New Science of Cause and Effect](https://www.youtube.com/watch?v=ZaPV1OSEpHw) — PyData, tiếng Anh. Bài nói của Pearl về khoa học mới về nhân quả, liên quan đến phần về Causal Transformer.
