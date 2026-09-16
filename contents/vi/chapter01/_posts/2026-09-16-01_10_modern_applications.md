---
layout: post
title: "Ứng dụng hiện đại: Bài toán lớn gặp khoa học máy tính"
chapter: '01'
order: 10
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
lesson_type: optional
---

## Mục tiêu học tập

Sau bài tùy chọn này, bạn gọi được tên ba nơi một bài toán Chương 1—còn mở, hoặc đã là định lý—đã trở thành hạ tầng hoặc động cơ nghiên cứu trong khoa học máy tính và khoa học dữ liệu từ khoảng 2022, mà không nhầm một bộ giải thực dụng, một surrogate nơ-ron, hay một máy hình học mức huy chương với việc giải quyết câu hỏi toán học gốc.

## Kiến thức cần có

Các bài bắt buộc của chương, đặc biệt [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Bốn màu]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/), và studio [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/). Trang này không viết lại các phát biểu ấy.

## Mở đầu

Một bài toán Clay có thể ngồi chưa giải trong khi công nghiệp vẫn chuyển mã *sống cạnh nó*. Bộ giải SAT tấn công các thể hiện NP-đầy đủ mà không chứng minh $$\mathbf{P}\neq\mathbf{NP}$$. Toán tử học được dự báo trường chất lỏng mà không chứng minh nghiệm Navier–Stokes trơn tồn tại. Một máy hình học có thể viết chứng minh olympic mà không khép Kakeya. Căng thẳng của bài này vì thế là vệ sinh diễn giải. Công trình CS/DS gần đây là thật; chúng không phải lời giải lén của các bài toán lớn.

## Phát triển khái niệm

Một bài toán quyết định NP-đầy đủ hỏi liệu có chứng chỉ mà bộ kiểm tra xác nhận được trong thời gian đa thức theo kích thước vào $$n$$. Lý thuyết trường hợp xấu vẫn chờ. Thực hành hỏi câu khác: trên *công thức này*, tìm kiếm học mệnh đề xung đột (CDCL) có kịp trước hạn không? Cùng kiểu ấy, một neural operator cố xấp xỉ một ánh xạ nghiệm

$$
\mathcal{G}:u_0\mapsto u(\,\cdot\,,T)
$$

giữa các không gian hàm, chứ không chứng nhận rằng $$u$$ giữ trơn với mọi $$u_0$$ trơn không phân kỳ.

## Bốn chỗ đáp gần đây

### 1. Các kỳ SAT như họ hàng công nghiệp của P vs NP

Các kỳ SAT Competition suốt 2022–2024 vẫn trao ngôi cho các máy CDCL trên benchmark công nghiệp và nhân tạo khổng lồ. Một bộ giải chạy xong **không** đặt thể hiện ấy vào $$\mathbf{P}$$ như một lớp độ phức tạp, và một họ công thức kháng cự **không** chứng minh $$\mathbf{P}\neq\mathbf{NP}$$. Điều nó chứng minh, về mặt vận hành, là góc nhìn *chứng chỉ* của NP đã là sản phẩm: trình biên dịch, kiểm chứng phần cứng, và lập kế hoạch xuất CNF, còn tìm kiếm học mệnh đề xung đột là đòn tấn công mặc định. Dùng bài P vs NP của chương này cho định nghĩa; dùng nhật ký cuộc thi cho sự thật kỹ thuật.

### 2. Neural operator như surrogate cho Navier–Stokes

Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart và Anandkumar (2023) viết neural operator như ánh xạ giữa không gian hàm vô hạn chiều và thử trên Burgers, dòng Darcy, và Navier–Stokes. Fourier neural operator học một surrogate $$\widehat{\mathcal{G}}$$ có thể đánh giá nhanh hơn bộ giải cổ điển nhiều bậc trên lưới tương tự. Câu hỏi Thiên niên kỷ là tồn tại và độ trơn của phương trình liên tục. Sai số kiểm tra nhỏ của $$\widehat{\mathcal{G}}$$ là một regularity thực nghiệm về một tập dữ liệu và một kiến trúc. Hãy giữ hai nhãn ấy tách nhau.

### 3. AlphaGeometry như đòn tính toán trên hình học khó

Trinh, Wu, Le, He và Luong (2024) giới thiệu AlphaGeometry, một bộ chứng minh neuro-symbolic được huấn luyện trên định lý tổng hợp quy mô lớn. Trên bộ 30 bài hình học olympic, nó giải 25, tiến gần thành tích trung bình của huy chương vàng IMO trên lát cắt ấy. Đây là kết quả CS về tìm kiếm, dữ liệu tổng hợp, và một máy suy diễn tượng trưng. Nó không phải chứng minh Kakeya, cũng không thay văn hóa restriction theory trong chương này và Chương 2. Nó *là* bằng chứng rằng “hình học khó” có thể biến thành không gian tìm kiếm máy kiểm được.

### 4. Tìm kiếm vét cạn bên cạnh Collatz

Barina (2021) báo một kiểm chứng quy mô GPU rằng ánh xạ Collatz đạt chu trình tầm thường với mọi giá trị xuất phát tới một cận cỡ $$2^{68}$$. Các bài kỹ thuật sau mở rộng tìm kiếm ấy. Một đoạn đầu hữu hạn, dù lớn, vẫn là một đoạn đầu hữu hạn. Định lý almost-all của Tao và phát biểu mở “mọi $$n$$” vẫn là đối tượng toán học. Đóng góp CS là một tính toán đã kiểm và một lời nhắc về điều tính toán không thể kết thúc.

## Diễn giải và nhận định

Trong mỗi trường hợp, bài toán lớn cung cấp một *hình dạng*—chứng chỉ, chính quy liên tục, dựng hình, iteration—còn hệ thống triển khai cung cấp một *ngân sách*. Đọc ngân sách như định lý là lỗi đặc trưng của viết khoa học những năm 2020.

## Giới hạn và hướng mở rộng

Bài này không biến RH, BSD, hay sinh đôi nguyên tố thành sản phẩm mật mã; những câu chuyện ấy thuộc số hạng sai và bài lý thuyết số Chương 3. Nó cũng không hình thức hóa độ phức tạp SAT vượt slogan đã có trong bài P vs NP.

## Bài tập

1. Một nhà cung cấp nói “bộ giải SAT của chúng tôi cho thấy P = NP trên netlist khách hàng.” Hãy viết lại tuyên bố cho khớp định nghĩa trong bài P vs NP.
2. Một start-up khí hậu quảng cáo neural operator như đã “giải Navier–Stokes.” Bạn sẽ đòi hai đại lượng nào (phân phối huấn luyện; một chứng chỉ độ trơn) trước khi chấp nhận một câu yếu hơn?
3. AlphaGeometry giải 25 trên 30 bài hình học olympic. Vì sao điều đó tương thích với Kakeya vẫn mở?
4. Nếu một tìm kiếm Collatz tới $$2^{80}$$, câu nào trong bài Collatz vẫn đúng y như hôm nay?

## Tài liệu tham khảo

- Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., & Anandkumar, A. (2023). Neural operator: Learning maps between function spaces with applications to PDEs. *JMLR*, 24(89), 1–97. [jmlr.org/papers/v24/21-1524.html](https://jmlr.org/papers/v24/21-1524.html).
- Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482. [doi:10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5).
- Barina, D. (2021). Convergence verification of the Collatz problem. *Journal of Supercomputing*, 77, 2681–2688. [doi:10.1007/s11227-020-03368-x](https://doi.org/10.1007/s11227-020-03368-x).
- [Chuỗi SAT Competition](https://satcompetition.github.io/) (các kỳ 2022–2024).
- Khóa học: [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/).
