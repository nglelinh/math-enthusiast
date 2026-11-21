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

## Mục tiêu học tập

Sau bài tùy chọn này, bạn có thể thêm ba ví dụ cụ thể giai đoạn 2022–2026 vào bản đồ ở bài [Chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/): huấn luyện tối ưu theo ngân sách tính toán, tác nhân giải toán olympic dùng Lean, và mô hình chuỗi nhân quả. Bài này không viết lại những điều đã nói ở bài đó về quyền riêng tư vi phân, lý thuyết mã hay thuật toán lượng tử.

## Kiến thức cần có

Bài [Chủ đề hiện đại]({{ site.baseurl }}/contents/vi/chapter09/09_14_Modern_Themes/), cùng các bài về giải thưởng làm điểm xuất phát: [bộ ba học sâu]({{ site.baseurl }}/contents/vi/chapter09/09_12_Deep_Learning_Trio/), [Pearl]({{ site.baseurl }}/contents/vi/chapter09/09_11_Pearl_Causality/), [Valiant]({{ site.baseurl }}/contents/vi/chapter09/09_09_Valiant_Learning/).

## Mở đầu

Bài chủ đề hiện đại giống một chiếc la bàn: quyền riêng tư, tối ưu và lý thuyết học máy, mã hóa, tính toán lượng tử, kiểm chứng hình thức. Bài này là một *báo cáo cập nhật* giai đoạn 2022–2026 về ba hướng đã có thêm kết quả mới. Các quy luật về quy mô (scaling) đã trở thành cách phân bổ tài nguyên trong thực tế. Kiểm chứng hình thức gặp học tăng cường trong Lean. Đồ thị nhân quả gặp transformer trên dữ liệu theo thời gian. Các bài về giải thưởng vẫn là lối vào; đây là những căn phòng mở ra phía sau.

## Phát triển khái niệm

Hoffmann và cộng sự (2022) coi số phép tính (FLOPs) là một ngân sách cần chia giữa số tham số $$N$$ và số token $$D$$. AlphaProof coi việc tìm các bước chứng minh (tactic) trong Lean như một môi trường học tăng cường, trong đó phần thưởng là việc kernel của Lean chấp nhận chứng minh. Một Causal Transformer coi quỹ đạo $$(X_t,A_t,Y_t)$$ như một chuỗi và cố ước lượng kết quả phản thực nếu thực hiện một chuỗi hành động khác. Đây chính là ý của Pearl, “can thiệp $$\neq$$ điều kiện hóa”, nay được đưa vào một kiến trúc mạng.

## Ba cập nhật (không phải một bản khảo sát thứ hai)

### 1. Huấn luyện tối ưu theo ngân sách tính toán và chủ đề tối ưu

Quy luật Chinchilla (tăng số token cùng với số tham số) đã thay đổi cách các phòng thí nghiệm chi tiền. Nó không thay thế định nghĩa PAC của Valiant hay câu chuyện lan truyền ngược của bộ ba học sâu. Nó là kết quả dễ thấy nhất của năm 2022 liên quan đến chủ đề tối ưu: một câu trả lời thực nghiệm cho câu hỏi “nên đầu tư vào đâu?” khi mỗi lần huấn luyện tốn cả một kho GPU. Hãy gọi đó là một quy luật thực nghiệm, rồi quay lại các bài về AI và lý thuyết học máy để tìm các định lý.

### 2. AlphaProof và chủ đề kiểm chứng

Kết quả đánh giá ở IMO 2024 (mức tương đương huy chương bạc) và bài báo trên *Nature* năm 2025 (Hubert và cộng sự) cho thấy một tác nhân có thể đề xuất chứng minh bằng Lean và được kernel chấm. Đây là khẩu hiệu của kiểm chứng hình thức được đưa vào thực tế: kiểm thử chỉ có thể không tìm thấy lỗi, còn kernel thì chấp nhận một chứng minh cụ thể. Các lưu ý ở Chương 5 vẫn đúng (chuyên gia vẫn phải hình thức hóa phát biểu, vẫn cần thêm tính toán, và bài tổ hợp vẫn chưa giải được). Điều Chương 9 muốn nhấn mạnh là cách nhìn theo *hệ thống*: một kernel đáng tin cộng với một bộ đề xuất học được là một kiến trúc mới ở biên giới toán–tin, chứ không phải một lời trích dẫn giải Turing.

### 3. Causal Transformer và Pearl

Melnychuk, Frauen và Feuerriegel (2022) giới thiệu Causal Transformer để ước lượng kết quả phản thực trên dữ liệu theo thời gian (ví dụ dữ liệu điều trị kiểu MIMIC). Hàm mất mát đối kháng được dùng để biểu diễn *không* dự đoán được phương pháp điều trị hiện tại; đó là một phiên bản học sâu của việc chặn đường back-door. Điều này không làm do-calculus lỗi thời. Nó cho thấy các đối tượng của Pearl trông ra sao khi biến đồng hành là một chuỗi.

## Diễn giải và nhận định

Bài chủ đề hiện đại đã nhắc rằng áp lực triển khai tạo ra các định nghĩa. Chinchilla tạo ra một định nghĩa thực dụng về “đủ dữ liệu”. AlphaProof tạo ra một định nghĩa thực dụng về “đủ hình thức để chấm điểm”. Causal Transformer tạo ra một định nghĩa theo kiến trúc về “biểu diễn cân bằng”. Không định nghĩa nào trong số đó thay thế được DP, mã cực (polar code) hay thuật toán Shor.

## Giới hạn và hướng mở rộng

Đừng bỏ qua bản khảo sát mà chỉ đọc bài này. Quyền riêng tư, lý thuyết mã và tính toán lượng tử không hề dừng lại từ năm 2021; chúng không được nhắc ở đây vì bản khảo sát đã đề cập, và vì FIPS 203 đã được nói đến ở Chương 3 và 6.

## Bài tập

1. Thêm hàng thứ sáu vào bảng “đi ngược khóa học” của bài chủ đề hiện đại cho *huấn luyện tối ưu theo ngân sách tính toán*. Hàng đó dẫn đến chương nào?
2. Vì sao “kernel chấp nhận” gần với kiểm chứng kiểu Hoare hơn là kiểm thử đơn vị, và vì sao nó vẫn phụ thuộc vào đặc tả?
3. Trong Causal Transformer, hàm mất mát đối kháng đang cố mô phỏng đối tượng nào của Pearl?
4. Một slide viết “ý tưởng của giải Turing đạt đỉnh năm 2018 với học sâu”. Dựa vào bài này, hãy nêu hai đối tượng toán–tin sau năm 2018 không chỉ là mạng lớn hơn.

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
