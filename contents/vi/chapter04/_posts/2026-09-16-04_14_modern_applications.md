---
layout: post
title: "Ứng dụng hiện đại: Vẻ đẹp đi vào sản phẩm"
chapter: '04'
order: 14
owner: Nguyen Le Linh
lang: vi
categories:
- chapter04
lesson_type: optional
---

## Mục tiêu học tập

Sau bài tùy chọn này, bạn nối được ba đối tượng “đẹp” đã có trong chương—trật tự không tuần hoàn, sinh động lực, và hiện tượng nảy sinh—với các hiện vật khoa học máy tính 2022–2026, mà không biến trang thành hub thứ hai của [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/) và không kể lại sáu trụ Big Think của Tao.

## Kiến thức cần có

Chuỗi vẻ đẹp bắt buộc, đặc biệt [lát gạch]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/), [hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/) / động lực, và [hiện tượng nảy sinh]({{ site.baseurl }}/contents/vi/chapter04/04_12_Emergence/). Hub Tao vẫn là bản đồ; trang này là cửa bên vào ứng dụng gần đây.

## Mở đầu

Chương 4 được viết như giấy phép thưởng thức các cú sốc: vô hạn có kích thước; một họ gạch có thể buộc không tuần hoàn; một dòng chảy tất định có thể trông như ngẫu nhiên; một đám đông có thể làm điều không cá thể nào làm. Những cú sốc ấy nay có kho mã. Viên hat 2023 được tìm với tính toán mang vị SAT. Mô hình sinh dựa trên score là hệ động lực được huấn luyện ở quy mô công nghiệp. “Năng lực nảy sinh” của mô hình ngôn ngữ thành slogan 2022 và cuộc tranh đo lường 2023. Không điều nào viết lại sáu trụ.

## Phát triển khái niệm

Một monotile không tuần hoàn là một prototile đơn cho phép lát mặt phẳng nhưng không cho lát tuần hoàn. Mô hình sinh khuếch tán học cách đảo quá trình thêm nhiễu $$x_0\mapsto x_t$$, thường bằng cách ước lượng score $$\nabla_x \log p_t(x)$$. Hiện tượng nảy sinh, theo cách dùng của Wei et al. (2022), là năng lực vắng ở quy mô nhỏ và có ở quy mô lớn trên một metric đã chọn. Schaeffer, Miranda và Koyejo (2023) đáp rằng một số nhảy có vẻ đột ngột là hiện tượng của metric gián đoạn. Vẻ đẹp trở nên ứng dụng khi các định nghĩa ấy chạm phần mềm.

## Ba chỗ đáp bổ sung

### 1. Viên hat và lát gạch có trợ giúp SAT

Smith, Myers, Kaplan và Goodman-Strauss (2023/2024) trưng ra “hat,” một polykite lát mặt phẳng không tuần hoàn, cùng một continuum các đa giác liên quan và một lập luận tổ hợp có máy tính hỗ trợ. Máy SAT trước đó của Kaplan cho số Heesch nằm trên đường phát hiện. Đây là bài lát gạch Chương 4 bất ngờ thành cụ thể, và đây là câu chuyện CS: tìm kiếm vét cạn và mã hóa SAT như dụng cụ nghiên cứu, không như trụ Tao mới.

### 2. Khuếch tán như động lực được huấn luyện

Karras, Aittala, Aila và Laine (2022) tách các lựa chọn thiết kế của bộ sinh dựa trên score—tiền điều kiện, lịch nhiễu, bộ lấy mẫu—và đạt số FID mạnh với vài chục lần đánh giá mạng. Đối tượng là một hệ động lực ngẫu nhiên mà trường vector được học. Đó là thói quen hỗn độn/động lực của chương này, nay là mô hình ảnh sản xuất (và, sau đó, một mảnh của tầng lắp ráp AlphaFold 3). Nó không thay studio ánh xạ logistic.

### 3. Hiện tượng nảy sinh, kèm cảnh báo metric

Wei et al. (2022) liệt kê các nhiệm vụ trên đó mô hình ngôn ngữ lớn có vẻ nhảy từ gần ngẫu nhiên tới độ chính xác dùng được. Schaeffer et al. (2023) cho thấy đổi sang metric mượt hơn có thể biến nhiều vách đá ấy thành dốc. Bài hiện tượng nảy sinh Chương 4 đã cảnh báo hành vi tập thể cần một định nghĩa. Cặp 2022–2023 là cùng cảnh báo ấy mặc áo học máy: hãy gọi tên metric trước khi gọi tên chuyển pha.

## Diễn giải và nhận định

Một lát hat trên hình nền laptop không phải phân loại mọi monotile không tuần hoàn. Một FID đẹp không phải chứng minh SDE ngược là quá trình sinh dữ liệu. Một vách độ chính xác gián đoạn không tự động là luật tự nhiên mới. Hãy giữ định nghĩa đẹp và hiện vật đang chuyển trong hai tay tách nhau.

## Giới hạn và hướng mở rộng

Trang này không liệt lại số, đại số, hình học, xác suất, giải tích và động lực. Nếu muốn ngữ pháp ấy, quay về [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/). Fractal, hình bất khả, và mặt cực tiểu để lại cho các bài riêng.

## Bài tập

1. Vì sao một mã hóa SAT giúp *trước khi* hat được biết là lát được, và vì sao điều đó vẫn không thay chứng minh không tuần hoàn?
2. Trong bộ lấy mẫu EDM, đối tượng nào gần trường vector của bài hỗn độn nhất?
3. Lấy một nhiệm vụ chấm bằng exact-match accuracy. Theo Schaeffer et al., đề xuất một metric mượt hơn và nói “hiện tượng nảy sinh” sẽ trông thế nào trên nó.
4. Viết một câu có thể xuất hiện trên trang này và một câu chỉ thuộc hub Tao.

## Tài liệu tham khảo

- Smith, D., Myers, J. S., Kaplan, C. S., & Goodman-Strauss, C. (2024). An aperiodic monotile. *Combinatorial Theory*, 4(1). [arXiv:2303.10798](https://arxiv.org/abs/2303.10798).
- Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. *NeurIPS*. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364).
- Wei, J., et al. (2022). Emergent abilities of large language models. *TMLR*. [arXiv:2206.07682](https://arxiv.org/abs/2206.07682).
- Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *NeurIPS*. [arXiv:2304.15004](https://arxiv.org/abs/2304.15004).
- Trang hat của Kaplan: [cs.uwaterloo.ca/~csk/hat](https://cs.uwaterloo.ca/~csk/hat/).
