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

Sau bài tùy chọn này, bạn mô tả được ba hệ thống tính toán 2022–2026 đưa nghề Chương 5—biến một tuyên bố thành thứ máy kiểm được—vào Lean và tìm kiếm neuro-symbolic, đồng thời vẫn tôn trọng Gödel: một kernel đã kiểm chứng không cho một lý thuyết đầy đủ về mọi chân lý số học.

## Kiến thức cần có

Các bài chứng minh, đặc biệt [Euclid / vô hạn nguyên tố]({{ site.baseurl }}/contents/vi/chapter05/05_02_Euclid_Infinite_Primes/), [Gödel]({{ site.baseurl }}/contents/vi/chapter05/05_04_Godel_Incompleteness/), [bốn màu]({{ site.baseurl }}/contents/vi/chapter05/05_07_Four_Color_Proof/), và [Fermat]({{ site.baseurl }}/contents/vi/chapter05/05_08_Fermat_Last_Theorem/). Trang này không kể lại các lập luận ấy.

## Mở đầu

Một chứng minh là một ý tưởng đã thành lập luận. Bộ chứng minh tương tác làm lập luận thành chương trình. Vài năm vừa rồi biến slogan ấy thành tiêu đề: Liquid Tensor Experiment xong trong Lean năm 2022; AlphaGeometry viết chứng minh hình học olympic năm 2024; AlphaProof, huấn luyện bằng học tăng cường trong Lean, đạt *điểm* mức huy chương bạc tại IMO 2024 (với tính toán nhiều ngày và việc hình thức hóa đề do người làm). Kỹ năng Chương 5 là giữ *nước cờ* nhìn thấy được: dựng, tìm kiếm, kiểm kernel—không ngôn ngữ tiệc tùng về “AI giải toán.”

## Phát triển khái niệm

Một trợ lý chứng minh kiểm rằng một hạng tử cư trú trong một kiểu. Nếu $$T$$ là một phát biểu hình thức, một chứng minh Lean là một cư dân của $$T$$, tương đối với kernel, các tiên đề, và các thư viện bạn tin. Định lý bất toàn Gödel nói rằng mọi lý thuyết nhất quán, tiên đề hóa hiệu quả, đủ giàu cho số học đều để lại một số câu số học chưa quyết. Hai sự thật ấy sống cùng nhau. Bạn có thể kiểm chứng *định lý này* hôm nay và vẫn không sở hữu một thủ tục quyết định cho mọi định lý.

## Ba chỗ đáp

### 1. Liquid Tensor Experiment (2022)

Ngày 14 tháng 7 năm 2022, cộng đồng Lean, do Johan Commelin dẫn với đầu vào toán học từ Scholze, công bố hoàn thành Liquid Tensor Experiment: kiểm chứng hình thức định lý thách thức chính về không gian vector lỏng (sự triệt tiêu của một số nhóm $$\mathrm{Ext}$$). Bài học CS khớp các hình thức hóa bốn màu và Kepler: một lập luận hiện đại có thể nói chuyện với một kernel, nhưng chỉ sau đầu tư quy mô năm vào thư viện (phạm trù abelian, đối đồng điều). *Ý tưởng* của định lý vẫn là của Scholze–Clausen; *hiện vật* là một kho mã.

### 2. AlphaGeometry (2024)

Trinh et al. (2024) ghép một mô hình ngôn ngữ huấn luyện trên định lý hình học tổng hợp với một máy suy diễn tượng trưng. Hệ thống phát ra chứng minh người đọc được và giải 25 trên 30 bài hình học olympic trong bộ chuẩn của họ. Đây là tìm kiếm cộng ngôn ngữ thân thiện với bộ kiểm, gần tinh thần một nước cờ Euclid được tổ chức tốt hơn là một bài luận mô hình ngôn ngữ. Nó không thay bài học chứng minh máy của bốn màu về *cái gì được tính* là chứng minh; nó thêm một bộ sinh mà người vẫn đọc được.

### 3. AlphaProof và IMO 2024

Thông báo 25 tháng 7 năm 2024 của DeepMind, sau đó mở rộng trong một bài *Nature* 2025, mô tả AlphaProof như một tác nhân kiểu AlphaZero tìm chứng minh Lean, dùng RL lúc kiểm trên bài khó. Cùng AlphaGeometry 2, nó giải bốn trên sáu bài IMO 2024 với 28 trên 42 điểm—*tương đương huy chương bạc trên bảng điểm*, với các chú thích quan trọng rằng đề được chuyên gia hình thức hóa và tính toán chạy xa vượt thời gian thi. Cách đọc Chương 5 thật chính xác: kernel vẫn quyết điều gì là chứng minh; cái mới là cách ứng viên được đề xuất.

## Diễn giải và nhận định

Một dấu kiểm Lean xanh là bảo đảm tương đối với một đặc tả, như slogan kiểm chứng của Chương 9 cũng nói. Nó không phải chứng minh rằng bài toán không hình thức được hình thức hóa không trượt, và không phải lối thoát khỏi bất toàn. *Điểm* huy chương bạc của AlphaProof không phải huy chương bạc trao cho một thí sinh theo luật IMO.

## Giới hạn và hướng mở rộng

Bài này không hình thức hóa FLT hay Poincaré. Nó không tuyên bố bài tổ hợp nay đã dễ với tác nhân Lean (các mục tổ hợp IMO 2024 hệ thống không giải được).

## Bài tập

1. Theo phong cách bài Euclid, gọi tên *nước cờ* trong LTE: cái gì đang được đưa về kiểm kernel, và cái gì phải được xây trước?
2. Vì sao “chứng minh hình học người đọc được” là bảo đảm khác với “kernel Lean chấp nhận một hạng tử”?
3. Liệt kê ba cách đánh giá AlphaProof tại IMO 2024 khác kỳ thi người, chỉ dùng sự thật từ ghi chú DeepMind hoặc bài 2025.
4. Phát biểu bất toàn Gödel trong một câu vẫn đúng sau AlphaProof.

## Tài liệu tham khảo

- Cộng đồng Lean. (2022). Completion of the Liquid Tensor Experiment. [leanprover-community.github.io/blog/posts/lte-final](https://leanprover-community.github.io/blog/posts/lte-final/).
- Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482. [doi:10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5).
- Google DeepMind. (2024). AI achieves silver-medal standard solving International Mathematical Olympiad problems. [Blog, 25 July 2024](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/).
- Hubert, T., et al. (2025). Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature*. [doi:10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y).
