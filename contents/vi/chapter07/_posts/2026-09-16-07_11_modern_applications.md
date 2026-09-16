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

Sau bài bạn đồng hành studio tùy chọn này, bạn mượn được ba dụng cụ tính toán 2022–2026—lát gạch có trợ giúp SAT, tìm kiếm hình học neuro-symbolic, và kiểm Collatz cận lớn—mà không để một tính toán đã xong đóng giả một nhật ký khám phá đã xong.

## Kiến thức cần có

Tổng quan studio và ít nhất một trong [lặp / Collatz]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/), [lát gạch / màu bản đồ]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/), [Kakeya]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/), hoặc [xếp cầu]({{ site.baseurl }}/contents/vi/chapter07/07_03_Explore_Sphere_Packing/).

## Mở đầu

Chương 7 là sổ tay, không phải giảng đường. Các hệ thống CS gần đây là những sổ tay cực kỳ cám dỗ: chúng trả về một viên gạch, một phác chứng minh, hoặc một cận $$2^{68}$$. Thói quen studio già hơn các hệ thống ấy. Đặt giả thuyết, thiết kế thí nghiệm nhỏ, ghi một thất bại, tách quan sát khỏi chứng minh. Trang này cho thấy cách *dùng* dụng cụ mới bên trong thói quen ấy.

## Phát triển khái niệm

Một bộ giải SAT trả về thỏa được hoặc không thỏa được cho một mã hóa hữu hạn. Một máy hình học trả về một chứng minh trong ngôn ngữ hình học hình thức. Một bộ kiểm Collatz trả về “mọi $$n\le N$$ đã tới 1.” Mỗi đầu ra là một quan sát về một đối tượng *hữu hạn*. Các lời nhắc mở của studio—một tập Kakeya có thể nhỏ đến đâu? mọi $$n$$ có tới 1 không?—vẫn vô hạn. Nước cờ hữu ích là viết đối tượng hữu hạn vào nhật ký như dữ liệu, rồi viết câu vẫn mở bên cạnh.

## Ba dụng cụ

### 1. SAT và viên hat, như studio lát gạch

Smith, Myers, Kaplan và Goodman-Strauss (2023/2024) dùng tìm kiếm tính toán (kể cả cận Heesch dựa trên SAT) trên đường tới monotile hat. Với studio màu bản đồ và lát gạch, bài học chuyển được không phải “tải một viên hat rồi dừng.” Đó là: mã hóa một quy tắc khớp cục bộ, hỏi bộ giải một mảng bán kính $$R$$, và để tính không thỏa được *thông tin hóa* một giả thuyết. Trang hat công khai của Kaplan là mẫu chia sẻ mã và hình cùng lập luận.

### 2. AlphaGeometry như sổ hình học, không phải tiên tri

Trinh et al. (2024) cho thấy một mô hình ngôn ngữ dữ liệu tổng hợp cộng một máy tượng trưng có thể phát ra chứng minh olympic đọc được. Trong studio Kakeya hoặc chiều bốn, bạn có thể dùng dụng cụ ấy để đuổi một bổ đề Euclid. Bạn vẫn nợ nhật ký một câu về điều đã giả định (hình học phẳng, một bản dịch bài toán) và điều chưa giả định (một cận Kakeya liên tục).

### 3. Tìm kiếm Collatz như thí nghiệm có cận

Barina (2021) và các kiểm GPU sau đẩy kiểm chứng Collatz vét cạn tới $$N$$ khổng lồ. Studio lặp Chương 7 đã cấm viết “đã kiểm tới $$N$$” thành “đúng với mọi $$n$$.” Hãy dùng cận đã công bố như một hàng trong bảng; dùng định lý almost-all của Tao như một hàng khác; giữ tuyên bố phổ quát mở.

## Diễn giải và nhận định

Máy tính xuất sắc trong việc lấp bảng. Chúng trung bình trong việc nhận ra bảng không phải định lý. Điểm studio, nếu khóa học được dạy, là cho sự trung thực của nhật ký, không cho $$N$$ lớn nhất.

## Giới hạn và hướng mở rộng

Số học xếp cầu, đồ thị khoảng nguyên tố, và phòng thí nghiệm ngẫu nhiên-đối-trật tự có thể dùng cùng mẫu. Từ điển đối ngẫu (studio cuối) vẫn là bản đồ vẽ tay; một mô hình ngôn ngữ lấp bảng là bản nháp, không phải từ điển.

## Bài tập

1. Mã hóa, bằng lời, một câu hỏi SAT sẽ giúp studio *màu bản đồ* mà không tuyên bố bốn màu là kết quả của bạn.
2. Lấy một chứng minh kiểu AlphaGeometry cho một đồng quy đơn giản. Hai dòng nào thuộc nhật ký khám phá của bạn?
3. Thêm một hàng vào bảng Collatz: $$N=2^{68}$$, phương pháp = tìm kiếm GPU, trạng thái = kiểm hữu hạn. Viết hàng kề cho “mọi số nguyên dương.”
4. Vì sao “bộ giải trả về UNSAT” gần chứng minh hơn “mất mát mạng nơ-ron nhỏ”—và khi nào nó vẫn chưa phải chứng minh của phát biểu vô hạn bạn quan tâm?

## Tài liệu tham khảo

- Smith, D., Myers, J. S., Kaplan, C. S., & Goodman-Strauss, C. (2024). An aperiodic monotile. *Combinatorial Theory*, 4(1). [arXiv:2303.10798](https://arxiv.org/abs/2303.10798).
- Trinh, T. H., et al. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482.
- Barina, D. (2021). Convergence verification of the Collatz problem. *Journal of Supercomputing*, 77, 2681–2688.
- Kaplan, C. S. Tài nguyên hat: [cs.uwaterloo.ca/~csk/hat](https://cs.uwaterloo.ca/~csk/hat/).
- Studio: [Lặp]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/).
