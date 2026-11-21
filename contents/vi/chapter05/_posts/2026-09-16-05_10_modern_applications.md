---
layout: post
title: "Ứng dụng hiện đại: Ý tưởng chứng minh trong tính toán"
chapter: '05'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter05
lesson_type: optional
---

## Mục tiêu học tập

Sau bài tùy chọn này, bạn có thể mô tả ba hệ thống tính toán trong giai đoạn 2022–2026 đưa thói quen của chương 5 (biến một khẳng định thành thứ máy tính kiểm tra được) vào Lean và vào các phương pháp tìm kiếm kết hợp mạng nơ-ron với suy diễn ký hiệu. Bạn cũng cần thấy rằng điều này vẫn nằm trong khuôn khổ của Gödel: một lõi kiểm chứng (kernel) đáng tin cậy không cho ta một lý thuyết đầy đủ về mọi chân lý số học.

## Kiến thức cần có

Các bài chứng minh trước đó, đặc biệt là [Euclid và vô hạn số nguyên tố]({{ site.baseurl }}/contents/vi/chapter05/05_02_Euclid_Infinite_Primes/), [Gödel]({{ site.baseurl }}/contents/vi/chapter05/05_04_Godel_Incompleteness/), [bốn màu]({{ site.baseurl }}/contents/vi/chapter05/05_07_Four_Color_Proof/) và [Fermat]({{ site.baseurl }}/contents/vi/chapter05/05_08_Fermat_Last_Theorem/). Trang này không kể lại các lập luận đó.

## Mở đầu

Một chứng minh là một ý tưởng đã được viết thành lập luận. Các trợ lý chứng minh tương tác biến lập luận đó thành chương trình. Vài năm gần đây, ý này đã thành những tiêu đề cụ thể: Liquid Tensor Experiment hoàn thành trong Lean năm 2022; AlphaGeometry viết được chứng minh cho các bài hình học olympic năm 2024; AlphaProof, được huấn luyện bằng học tăng cường trong Lean, đạt *số điểm* ở mức huy chương bạc tại IMO 2024 (với nhiều ngày tính toán, và đề bài do con người hình thức hóa trước). Điều cần giữ từ chương 5 là phải nhìn thấy rõ *từng bước*: dựng, tìm kiếm, và để kernel kiểm tra, chứ không dùng những lời hô hào kiểu "AI giải toán".

## Phát triển khái niệm

Một trợ lý chứng minh kiểm tra rằng một hạng tử thuộc về một kiểu nào đó. Nếu $$T$$ là một phát biểu hình thức thì một chứng minh trong Lean là một phần tử của kiểu $$T$$, xét tương đối theo kernel, các tiên đề và các thư viện mà bạn tin tưởng. Định lý bất toàn của Gödel nói rằng mọi lý thuyết nhất quán, có tiên đề cho được hiệu quả, và đủ phong phú để làm số học đều để lại một số câu số học không quyết định được. Hai sự thật này cùng tồn tại. Bạn có thể kiểm chứng *định lý này* ngay hôm nay mà vẫn không có một thủ tục quyết định cho mọi định lý.

## Ba ví dụ

### 1. Liquid Tensor Experiment (2022)

Ngày 14 tháng 7 năm 2022, cộng đồng Lean, do Johan Commelin dẫn đầu và với phần toán học do Scholze đưa ra, thông báo đã hoàn thành Liquid Tensor Experiment: kiểm chứng hình thức một định lý đầy thách thức về các không gian vector "lỏng" (sự triệt tiêu của một số nhóm $$\mathrm{Ext}$$). Bài học cho khoa học máy tính giống với việc hình thức hóa định lý bốn màu và giả thuyết Kepler: một lập luận hiện đại có thể "nói chuyện" được với kernel, nhưng chỉ sau khi đầu tư nhiều năm vào thư viện (phạm trù abel, đối đồng điều). *Ý tưởng* của định lý vẫn là của Scholze và Clausen; *sản phẩm* là một kho mã.

### 2. AlphaGeometry (2024)

Trinh và cộng sự (2024) kết hợp một mô hình ngôn ngữ được huấn luyện trên các định lý hình học tổng hợp với một máy suy diễn ký hiệu. Hệ thống này viết ra các chứng minh mà con người đọc được, và giải 25 trên 30 bài hình học olympic trong bộ thử nghiệm của nhóm tác giả. Đây là tìm kiếm kết hợp với ngôn ngữ thân thiện với bộ kiểm tra, gần với tinh thần của một "nước đi Euclid" được tổ chức tốt hơn là một bài luận của mô hình ngôn ngữ. Nó không thay thế bài học của chứng minh bằng máy trong định lý bốn màu về việc *điều gì được tính* là chứng minh; nó chỉ thêm một bộ sinh ra chứng minh mà con người vẫn đọc được.

### 3. AlphaProof và IMO 2024

Thông báo ngày 25 tháng 7 năm 2024 của DeepMind, sau đó được mở rộng trong một bài trên *Nature* năm 2025, mô tả AlphaProof là một tác nhân theo kiểu AlphaZero tìm chứng minh trong Lean, dùng học tăng cường ngay lúc chạy với các bài khó. Cùng với AlphaGeometry 2, hệ thống giải được bốn trên sáu bài của IMO 2024, đạt 28 trên 42 điểm, *tương đương huy chương bạc theo bảng điểm*. Có hai chú thích quan trọng: đề bài được chuyên gia hình thức hóa trước, và thời gian tính toán vượt xa thời gian thi. Cách đọc đúng theo tinh thần chương 5 là: kernel vẫn là nơi quyết định điều gì là chứng minh; điều mới là cách các ứng viên chứng minh được đề xuất.

## Diễn giải và nhận định

Một dấu kiểm xanh của Lean là sự bảo đảm tương đối so với một đặc tả, đúng như tinh thần về kiểm chứng ở chương 9. Nó không chứng minh rằng bài toán gốc (không hình thức) đã được hình thức hóa đúng, và cũng không phải lối thoát khỏi bất toàn. *Số điểm* ngang huy chương bạc của AlphaProof không phải là huy chương bạc được trao cho một thí sinh theo luật của IMO.

## Giới hạn và hướng mở rộng

Bài này không hình thức hóa FLT hay giả thuyết Poincaré. Nó cũng không khẳng định các bài tổ hợp nay đã dễ với các tác nhân dùng Lean (các bài tổ hợp của IMO 2024 không được hệ thống giải).

## Bài tập

1. Theo phong cách bài Euclid, hãy gọi tên các *bước đi* trong LTE: điều gì được đưa về việc kernel kiểm tra, và điều gì phải xây dựng trước?
2. Vì sao "một chứng minh hình học mà người đọc được" là một loại bảo đảm khác với "kernel Lean chấp nhận một hạng tử"?
3. Liệt kê ba điểm khiến việc đánh giá AlphaProof tại IMO 2024 khác với kỳ thi dành cho con người, chỉ dùng các dữ kiện trong ghi chú của DeepMind hoặc bài báo năm 2025.
4. Phát biểu định lý bất toàn của Gödel trong một câu mà vẫn đúng sau AlphaProof.

## Tài liệu tham khảo

- Cộng đồng Lean. (2022). Completion of the Liquid Tensor Experiment. [leanprover-community.github.io/blog/posts/lte-final](https://leanprover-community.github.io/blog/posts/lte-final/).
- Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482. [doi:10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5).
- Google DeepMind. (2024). AI achieves silver-medal standard solving International Mathematical Olympiad problems. [Blog, 25 July 2024](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/).
- Hubert, T., et al. (2025). Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature*. [doi:10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y).

## Video tham khảo

- **Xem trước** — [Proving theorems with computers - Kevin Buzzard](https://www.youtube.com/watch?v=KccjCojGVO4) — Stony Brook Mathematics, tiếng Anh. Video định hướng cho mục tiêu của bài: dùng máy tính để kiểm chứng chứng minh.
- [The AI that solved IMO Geometry Problems | Guest video by @Aleph0](https://www.youtube.com/watch?v=4NlrfOl0l8U) — 3Blue1Brown, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ; nói về AlphaGeometry.
- [Improving on AlphaProof: IMO 2024 Problem 2 in Lean 4](https://www.youtube.com/watch?v=5IARsdn78xE) — David Renshaw, tiếng Anh. Một bản hình thức hóa bằng Lean 4 cho bài IMO 2024, theo tinh thần của AlphaProof. Nên dùng cạnh chủ đề kiểm chứng của bài, vì đây không phải bài nói chính thức của DeepMind.
