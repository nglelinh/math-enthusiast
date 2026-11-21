---
layout: post
title: "Ứng dụng hiện đại: Máy tính trong studio"
chapter: '07'
order: 11
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
lesson_type: optional
---

## Mục tiêu học tập

Đây là bài đọc thêm tùy chọn cho phần thực hành. Sau bài này, bạn biết cách dùng ba công cụ tính toán xuất hiện trong giai đoạn 2022–2026: dùng bộ giải SAT để tìm phép lát, dùng hệ thống kết hợp mạng nơ-ron với suy luận ký hiệu để tìm chứng minh hình học, và kiểm tra giả thuyết Collatz đến những cận rất lớn. Quan trọng hơn, bạn biết phân biệt giữa một phép tính đã chạy xong với một kết quả đã được chứng minh.

## Kiến thức cần có

Bài tổng quan của phần thực hành và ít nhất một trong các bài: [lặp / Collatz]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/), [lát mặt phẳng / tô màu bản đồ]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/), [Kakeya]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/), hoặc [xếp cầu]({{ site.baseurl }}/contents/vi/chapter07/07_03_Explore_Sphere_Packing/).

## Mở đầu

Chương 7 là phần thực hành với sổ ghi chép, không phải bài giảng. Các hệ thống máy tính gần đây rất dễ khiến ta tin rằng chúng làm thay được việc ghi chép đó: chúng trả về một viên lát, một bản phác chứng minh, hay một cận như $$2^{68}$$. Nhưng các thói quen nghiên cứu đã có từ trước các hệ thống ấy: đặt giả thuyết, thiết kế thí nghiệm nhỏ, ghi lại thất bại, phân biệt quan sát với chứng minh. Bài này hướng dẫn cách *dùng* các công cụ mới mà vẫn giữ những thói quen đó.

## Phát triển khái niệm

Một bộ giải SAT cho biết một bài toán được mã hóa hữu hạn là thỏa được hay không thỏa được. Một hệ thống hình học trả về một chứng minh viết bằng ngôn ngữ hình học hình thức. Một chương trình kiểm tra Collatz cho kết quả "mọi $$n\le N$$ đều về 1". Mỗi kết quả là một quan sát về một đối tượng *hữu hạn*. Trong khi đó, các câu hỏi của phần thực hành, như tập Kakeya có thể nhỏ đến đâu, hay mọi $$n$$ có về 1 không, đều liên quan đến vô hạn trường hợp. Cách làm đúng là ghi kết quả hữu hạn vào nhật ký như một dữ liệu, rồi ghi ngay bên cạnh câu hỏi vẫn còn mở.

## Ba công cụ

### 1. Bộ giải SAT và viên lát "chiếc mũ"

Smith, Myers, Kaplan và Goodman-Strauss (2023/2024) đã dùng tìm kiếm bằng máy tính, trong đó có tính số Heesch bằng bộ giải SAT, trong quá trình tìm ra viên lát đơn không tuần hoàn "chiếc mũ" (hat). Với phần thực hành về tô màu bản đồ và lát mặt phẳng, bài học rút ra không phải là "tải viên lát về là xong". Bài học là: mã hóa một quy tắc ghép cạnh cục bộ, hỏi bộ giải xem có lát được một vùng bán kính $$R$$ hay không, và nếu kết quả là không thỏa được thì dùng thông tin đó để điều chỉnh giả thuyết. Trang web công khai của Kaplan về viên lát này là một ví dụ tốt về cách chia sẻ mã nguồn và hình vẽ cùng với lập luận.

### 2. AlphaGeometry là công cụ hỗ trợ, không phải lời phán quyết

Trinh và cộng sự (2024) cho thấy một mô hình ngôn ngữ được huấn luyện trên dữ liệu tổng hợp, kết hợp với một bộ suy luận ký hiệu, có thể tạo ra lời giải hình học olympic mà con người đọc hiểu được. Trong bài thực hành về Kakeya hoặc không gian bốn chiều, bạn có thể dùng công cụ này để chứng minh một bổ đề hình học Euclid. Nhưng nhật ký vẫn phải ghi rõ bạn đã giả định những gì (hình học phẳng, cách bạn chuyển bài toán thành dạng máy đọc được) và kết quả đó *không* nói gì (chẳng hạn không cho một cận nào cho bài toán Kakeya liên tục).

### 3. Kiểm tra Collatz là thí nghiệm có giới hạn

Barina (2021) và các lần kiểm tra bằng GPU sau đó đã kiểm tra giả thuyết Collatz cho mọi số đến một giá trị $$N$$ rất lớn. Bài thực hành về phép lặp ở Chương 7 đã nhấn mạnh: không được viết "đã kiểm tra đến $$N$$" thành "đúng với mọi $$n$$". Hãy ghi cận đã công bố thành một dòng trong bảng, ghi định lý của Tao về "hầu hết" các số thành một dòng khác, và giữ khẳng định cho mọi số là câu hỏi mở.

## Nhận xét

Máy tính rất giỏi điền số liệu vào bảng, nhưng không giỏi nhận ra rằng một bảng số liệu chưa phải là định lý. Nếu khóa học có chấm điểm phần thực hành, điểm dành cho sự trung thực trong nhật ký, không dành cho người kiểm tra được $$N$$ lớn nhất.

## Giới hạn và hướng mở rộng

Có thể áp dụng cùng cách làm cho các bài về mật độ xếp cầu, đồ thị khoảng cách giữa các số nguyên tố, và thí nghiệm ngẫu nhiên và trật tự. Từ điển đối ngẫu (bài thực hành cuối) vẫn là một bản đồ vẽ tay; nếu dùng mô hình ngôn ngữ để điền bảng thì đó chỉ là bản nháp, chưa phải từ điển.

## Bài tập

1. Mô tả bằng lời một câu hỏi SAT có thể giúp ích cho bài thực hành *tô màu bản đồ*, mà không coi định lý bốn màu là kết quả của bạn.
2. Lấy một chứng minh kiểu AlphaGeometry cho một bài toán đồng quy đơn giản. Hai dòng nào nên ghi vào nhật ký nghiên cứu của bạn?
3. Thêm một dòng vào bảng Collatz: $$N=2^{68}$$, phương pháp = tìm kiếm bằng GPU, trạng thái = kiểm tra hữu hạn. Viết dòng tương ứng cho "mọi số nguyên dương".
4. Vì sao kết quả "bộ giải trả về UNSAT (không thỏa được)" gần với một chứng minh hơn kết quả "hàm mất mát của mạng nơ-ron nhỏ"? Khi nào nó vẫn chưa phải là chứng minh cho phát biểu vô hạn mà bạn quan tâm?

## Tài liệu tham khảo

- Smith, D., Myers, J. S., Kaplan, C. S., & Goodman-Strauss, C. (2024). An aperiodic monotile. *Combinatorial Theory*, 4(1). [arXiv:2303.10798](https://arxiv.org/abs/2303.10798).
- Trinh, T. H., et al. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482.
- Barina, D. (2021). Convergence verification of the Collatz problem. *Journal of Supercomputing*, 77, 2681–2688.
- Kaplan, C. S. Tài liệu về viên lát "chiếc mũ": [cs.uwaterloo.ca/~csk/hat](https://cs.uwaterloo.ca/~csk/hat/).
- Bài thực hành: [Lặp]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/).

## Video tham khảo

- **Xem trước:** [Discovery of the Aperiodic Monotile - Numberphile](https://www.youtube.com/watch?v=_ZS3Oqg1AX0) — Numberphile, tiếng Anh. Câu chuyện phát hiện viên lát đơn không tuần hoàn; nên xem trước khi đọc bài.
- [The AI that solved IMO Geometry Problems | Guest video by @Aleph0](https://www.youtube.com/watch?v=4NlrfOl0l8U) — 3Blue1Brown, tiếng Anh. Giải thích cách AlphaGeometry giải bài hình học IMO; nên xem sau khi đã nắm ý chính của bài.
- [UNCRACKABLE? The Collatz Conjecture - Numberphile](https://www.youtube.com/watch?v=5mFpVDpKX70) — Numberphile, tiếng Anh. Xem thêm sau hai video trên, giới thiệu giả thuyết Collatz.
