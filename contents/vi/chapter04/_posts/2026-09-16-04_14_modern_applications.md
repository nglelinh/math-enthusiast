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

Khi bước vào Chương 4, ta từng hỏi: *những ý tưởng nào đẹp và lạ đến mức các nhà toán học vẫn nghiên cứu chúng dù chẳng cần ứng dụng ngay?* Thật bất ngờ, chỉ trong giai đoạn 2022–2026, ba ý tưởng từng có vẻ "bay bổng" nhất của chương — phép lát không tuần hoàn, hệ động lực phi tuyến, và hiện tượng nảy sinh — đã đồng loạt bước ra khỏi bảng đen để xuất hiện trực tiếp trong công trình giải thưởng, phần mềm tạo ảnh AI và những tranh luận sôi nổi nhất về mô hình ngôn ngữ lớn.

## Mục tiêu học tập

Sau bài tùy chọn này, bạn liên hệ được ba chủ đề "đẹp" đã gặp trong chương (trật tự không tuần hoàn, mô hình sinh dựa trên động lực học, và hiện tượng nảy sinh) với các thành tựu khoa học máy tính giai đoạn 2022–2026. Bài này không lặp lại bài tổng quan [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/) và không kể lại sáu trụ cột trong bài nói Big Think của Tao.

## Kiến thức cần có

Các bài bắt buộc về vẻ đẹp toán học, đặc biệt là [lát gạch]({{ site.baseurl }}/contents/vi/chapter04/04_10_Tilings/), [hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/) và động lực học, và [hiện tượng nảy sinh]({{ site.baseurl }}/contents/vi/chapter04/04_12_Emergence/). Bài tổng quan về Tao vẫn là bản đồ chính; bài này là một lối rẽ sang các ứng dụng gần đây.

## Kiến thức cần nhớ: Vẻ đẹp toán học đi vào phần mềm hiện đại như thế nào?

Với người đã qua bậc đại học, khoảng cách giữa một định lý thuần túy và một sản phẩm công nghệ không nằm ở phép màu, mà nằm ở **khâu mô hình hóa, thuật toán hóa và đo đạc** — nơi ba nhánh toán học hiện đại gặp khoa học máy tính:
- **Hình học rời rạc $$\to$$ Bộ giải SAT (Combinatorial Optimization):** Khi không gian cấu hình quá lớn để vẽ tay, các ràng buộc khớp cạnh của bài toán lát gạch được dịch thành công thức logic mệnh đề (Boolean satisfiability) để máy tính rà soát hàng triệu ứng viên — nhưng chứng minh toàn cục vẫn cần tư duy toán học chặt chẽ.
- **Hệ động lực & Phương trình vi phân $$\to$$ Mô hình sinh (Generative AI):** Thay vì mô phỏng hành tinh hay thời tiết, các mô hình khuếch tán (diffusion) huấn luyện mạng nơ-ron học chính *trường vectơ score* kéo một đám mây nhiễu ngẫu nhiên trôi ngược về bức ảnh sắc nét hoặc cấu trúc protein 3D (như trong AlphaFold 3).
- **Cơ học thống kê $$\to$$ Đánh giá mô hình ngôn ngữ lớn (AI Evaluation):** Mượn từ vựng "hiện tượng nảy sinh" và "chuyển pha" vào AI là rất gợi mở, nhưng toán học nhắc ta phải kiểm tra xem "bước nhảy đột ngột" đó là bản chất của hệ hay chỉ là ảo giác do thước đo không liên tục gây ra.

## Mở đầu

Chương 4 mời bạn thưởng thức những cú sốc: vô hạn cũng có kích thước; một bộ gạch có thể buộc cách lát phải không tuần hoàn; một hệ tất định có thể trông như ngẫu nhiên; một đám đông có thể làm điều mà không cá thể nào làm được. Ngày nay những cú sốc ấy đã có mặt trong mã nguồn. Viên gạch "hat" năm 2023 được tìm ra với sự hỗ trợ của tính toán kiểu SAT. Mô hình sinh dựa trên score là một hệ động lực được huấn luyện ở quy mô công nghiệp. "Năng lực nảy sinh" của mô hình ngôn ngữ trở thành khẩu hiệu năm 2022 và thành một cuộc tranh luận về cách đo năm 2023. Không điều nào trong số đó thay đổi sáu trụ cột.

## Phát triển khái niệm

Một viên gạch đơn không tuần hoàn (aperiodic monotile) là một hình duy nhất lát kín được mặt phẳng nhưng không lát tuần hoàn được. Mô hình khuếch tán (diffusion) học cách đảo ngược quá trình thêm nhiễu $$x_0\mapsto x_t$$, thường bằng cách ước lượng score $$\nabla_x \log p_t(x)$$. Hiện tượng nảy sinh, theo cách dùng của Wei và cộng sự (2022), là một năng lực không có ở mô hình nhỏ nhưng xuất hiện ở mô hình lớn, đo bằng một thước đo đã chọn. Schaeffer, Miranda và Koyejo (2023) phản biện rằng một số bước nhảy trông có vẻ đột ngột thực ra là do thước đo không liên tục. Vẻ đẹp trở thành ứng dụng khi những định nghĩa này được đưa vào phần mềm.

## Ba ví dụ bổ sung

### 1. Viên gạch hat và lát gạch có SAT hỗ trợ

Smith, Myers, Kaplan và Goodman-Strauss (2023/2024) giới thiệu "hat", một hình ghép từ 8 hình cánh diều (polykite) lát mặt phẳng chỉ theo cách không tuần hoàn, cùng với một họ liên tục các đa giác liên quan và một lập luận tổ hợp có máy tính hỗ trợ. Trước khi viên hat xuất hiện, Craig Kaplan đã xây dựng phần mềm dùng bộ giải SAT để tính **số Heesch** (số vòng tròn đồng tâm tối đa có thể xếp bao quanh một mảnh trước khi bị kẹt) nhằm săn tìm những đa giác có hành vi lát bất thường. Khi David Smith phát hiện viên hat, chính công cụ SAT và kiểm tra vét cạn cục bộ giúp nhóm nhanh chóng xác nhận các ràng buộc ghép cạnh và xây dựng chứng minh phân tầng siêu mảnh. Đây là lúc bài lát gạch của Chương 4 bỗng trở nên cụ thể, và cũng là một câu chuyện khoa học máy tính: tìm kiếm vét cạn và mã hóa SAT được dùng như công cụ nghiên cứu, chứ không phải một trụ cột mới của Tao.

### 2. Khuếch tán như một hệ động lực được huấn luyện

Hãy hình dung quá trình "phá hủy" một bức ảnh đẹp $$x_0$$: ở mỗi bước nhỏ, bạn rắc thêm một chút nhiễu Gauss cho đến khi bức ảnh biến thành nhiễu tuyết trắng $$x_T$$ hoàn toàn vô nghĩa. Mô hình khuếch tán làm điều ngược lại: nó huấn luyện một mạng nơ-ron học **hàm score** $$\nabla_x \log p_t(x)$$ — về mặt hình học, đó là một *trường vectơ* chỉ về phía những bức ảnh có xác suất "trông như thật" cao hơn. Khi tạo ảnh mới, ta lấy một điểm nhiễu ngẫu nhiên rồi giải ngược phương trình vi phân theo trường vectơ đó.

**Ví dụ tính toán làm từng bước — hàm score 1 chiều kéo điểm nhiễu về dữ liệu thật:**
Giả sử "tập dữ liệu thật" của ta chỉ gồm đúng hai điểm $$x = -1$$ và $$x = +1$$. Sau khi thêm nhiễu Gauss phương sai $$\sigma^2 = 1$$, mật độ xác suất là hỗn hợp hai đường cong hình chuông:
$$p(x) = \frac{1}{2\sqrt{2\pi}}\left(e^{-(x-1)^2/2} + e^{-(x+1)^2/2}\right).$$
Lấy đạo hàm của $$\log p(x)$$ (chính là hàm score!), ta rút gọn được công thức cực đẹp:

$$
s(x) = \frac{d}{dx}\log p(x) = \tanh(x) - x.
$$

Thử thay ba điểm $$x$$ cụ thể để xem trường vectơ $$s(x)$$ đẩy điểm đi đâu:
- Tại $$x = +2{,}0$$: $$s(2{,}0) = \tanh(2) - 2 \approx 0{,}964 - 2 = \mathbf{-1{,}036}$$ (đẩy mạnh sang trái về gần điểm dữ liệu $$+1$$!).
- Tại $$x = +0{,}5$$: $$s(0{,}5) = \tanh(0{,}5) - 0{,}5 \approx 0{,}462 - 0{,}5 = \mathbf{-0{,}038}$$ (gần như cân bằng, nhưng khi giảm nhiễu $$\sigma \to 0$$ nó kéo dứt khoát về $$+1$$!).
- Tại $$x = -2{,}0$$: $$s(-2{,}0) \approx \mathbf{+1{,}036}$$ (đẩy mạnh sang phải về điểm dữ liệu $$-1$$!).

Mạng nơ-ron tạo ảnh hiện đại làm đúng công việc đó, chỉ thay trục 1 chiều bằng không gian ảnh hàng trăm nghìn chiều! Karras, Aittala, Aila và Laine (2022) tách riêng các lựa chọn thiết kế của mô hình sinh dựa trên score (tiền điều kiện, lịch nhiễu, bộ lấy mẫu ODE bậc cao) và đạt chỉ số FID rất tốt chỉ với vài chục lần gọi mạng nơ-ron thay vì hàng nghìn bước như trước. Đối tượng ở đây là một phương trình vi phân (tất định hoặc ngẫu nhiên) có trường vectơ được học. Đó chính là cách nghĩ về hỗn độn và động lực học của chương này, nay trở thành mô hình tạo ảnh trong sản phẩm thật (và sau đó là một phần của mô-đun dựng cấu trúc phân tử trong AlphaFold 3).

### 3. Hiện tượng nảy sinh, kèm cảnh báo về thước đo

Wei và cộng sự (2022) liệt kê những nhiệm vụ mà mô hình ngôn ngữ lớn dường như nhảy vọt từ mức gần đoán mò lên độ chính xác dùng được khi quy mô tham số vượt ngưỡng. Schaeffer và cộng sự (2023) phản biện bằng một quan sát toán học cực kỳ sắc bén: nhiều "vách đá" đó thực ra là sản phẩm của **thước đo khắc nghiệt kiểu được ăn cả, ngã về không** (exact-match).

**Ví dụ tính toán làm từng bước — ảo giác vách đá từ hàm lũy thừa $$p^4$$:**
Giả sử mô hình làm bài toán cộng số có 4 chữ số, và xác suất đoán đúng từng chữ số độc lập $$p$$ tăng rất đều đặn theo kích thước mô hình. Nếu ta chấm theo kiểu *đúng cả 4 chữ số mới được 1 điểm*, điểm exact-match là $$p^4$$:

| Xác suất đúng từng chữ số $$p$$ | Điểm mượt (trung bình chữ số) | Điểm exact-match $$p^4$$ |
|---:|---:|---:|
| $$0{,}50$$ | $$50\%$$ | $$6{,}25\%$$ |
| $$0{,}70$$ | $$70\%$$ | $$24{,}01\%$$ |
| $$0{,}85$$ | $$85\%$$ | $$52{,}20\%$$ |
| $$0{,}95$$ | $$95\%$$ | **$$81{,}45\%$$** |

Độ chính xác từng chữ số tăng đều đặn, không có "chuyển pha" thần kỳ nào cả, nhưng qua hàm lũy thừa $$p^4$$ (hay nặng hơn là $$p^{10}$$), đồ thị bỗng xuất hiện một vách đá dựng đứng! Khi đổi sang thước đo mượt hơn (như xác suất log hoặc tỷ lệ đúng từng token), nhiều "vách đá" lập tức trở thành con dốc thoai thoải. Bài hiện tượng nảy sinh ở Chương 4 đã cảnh báo rằng hành vi tập thể cần một định nghĩa rõ ràng. Cặp bài báo 2022–2023 là cùng lời cảnh báo đó trong bối cảnh học máy: hãy nêu rõ thước đo trước khi nói đến chuyển pha.

### Giải thích: từ định lý đẹp đến sản phẩm AI — 4 câu hỏi kiểm định

Khi đọc báo công nghệ ca ngợi một đột phá AI hay thuật toán mới gắn với toán học đẹp, hãy đi chậm qua 4 bước kiểm định:

1. **Xác định đối tượng toán học lõi:** Sản phẩm đang vận hành trên mô hình nào? (Gạch hat: bài toán thỏa mãn ràng buộc SAT; Diffusion: phương trình vi phân ODE/SDE với trường score $$\nabla_x \log p_t(x)$$; LLM: hàm mất mát xác suất trên chuỗi token.)
2. **Tách công cụ tính toán khỏi chứng minh:** Bộ giải SAT tìm ra ứng viên và kiểm tra hàng triệu trường hợp cục bộ, nhưng chỉ chứng minh toán học mới kết luận được cho mặt phẳng vô hạn.
3. **Kiểm tra thước đo trước khi kết luận "chuyển pha":** Một bước nhảy trên đồ thị có còn tồn tại nếu đổi từ thước đo phi tuyến sắc nét (như $$p^k$$ hoặc exact-match) sang thước đo trơn (cross-entropy / Brier score) không?
4. **Phân biệt mô hình hiệu dụng với bản chất vật lý:** Một mô hình khuếch tán sinh ảnh đẹp không chứng minh thế giới thực được sinh bởi quá trình khuếch tán ngược — nó chỉ chứng tỏ ngôn ngữ hệ động lực cực kỳ hiệu quả để xấp xỉ phân phối dữ liệu phức tạp.

**Kiểm tra nhanh.** Vì sao ví dụ $$p^4$$ ở trên lại quan trọng khi đọc các biểu đồ về AI? Vì nó cho thấy một cải thiện hoàn toàn tuyến tính ở tầng dưới có thể biến thành một "vách đá nảy sinh" giả tạo chỉ do cách ta định nghĩa điểm số ở tầng trên.

## Diễn giải và nhận định

Một hình lát gạch hat làm hình nền máy tính không phải là bảng phân loại mọi viên gạch đơn không tuần hoàn. Một chỉ số FID đẹp không chứng minh rằng phương trình vi phân ngẫu nhiên ngược là quá trình thật sự sinh ra dữ liệu. Một vách đá trên đồ thị độ chính xác với thước đo không liên tục không tự động là một quy luật tự nhiên mới. Hãy tách bạch định nghĩa toán học đẹp và sản phẩm đang được triển khai.

## Giới hạn và hướng mở rộng

Bài này không nhắc lại số học, đại số, hình học, xác suất, giải tích và động lực học. Nếu cần phần nền tảng đó, hãy quay lại [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/). Fractal, hình bất khả và mặt tối thiểu được dành cho các bài riêng.

## Tài liệu tham khảo

- Smith, D., Myers, J. S., Kaplan, C. S., & Goodman-Strauss, C. (2024). An aperiodic monotile. *Combinatorial Theory*, 4(1). [arXiv:2303.10798](https://arxiv.org/abs/2303.10798).
- Karras, T., Aittala, M., Aila, T., & Laine, S. (2022). Elucidating the design space of diffusion-based generative models. *NeurIPS*. [arXiv:2206.00364](https://arxiv.org/abs/2206.00364).
- Wei, J., et al. (2022). Emergent abilities of large language models. *TMLR*. [arXiv:2206.07682](https://arxiv.org/abs/2206.07682).
- Schaeffer, R., Miranda, B., & Koyejo, S. (2023). Are emergent abilities of large language models a mirage? *NeurIPS*. [arXiv:2304.15004](https://arxiv.org/abs/2304.15004).
- Trang về hat của Kaplan: [cs.uwaterloo.ca/~csk/hat](https://cs.uwaterloo.ca/~csk/hat/).

## Video tham khảo

- **Xem trước**: [Discovery of the Aperiodic Monotile - Numberphile](https://www.youtube.com/watch?v=_ZS3Oqg1AX0) (Numberphile, tiếng Anh). Câu chuyện phát hiện viên gạch hat. Nên xem trước khi đọc ví dụ 1.
- [But how do AI images and videos actually work? | Guest video by Welch Labs](https://www.youtube.com/watch?v=iv-5mZ_9CPY) (3Blue1Brown, tiếng Anh). Giải thích trực quan cách mô hình khuếch tán tạo ảnh và video. Xem cùng ví dụ 2.
- [Inventing Game of Life (John Conway) - Numberphile](https://www.youtube.com/watch?v=R9Plq-D1gEk) (Numberphile, tiếng Anh). John Conway kể về Game of Life, ví dụ kinh điển của hiện tượng nảy sinh. Góc nhìn bổ sung cho ví dụ 3.
