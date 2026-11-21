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

Sau bài tùy chọn này, bạn kể được ít nhất ba trường hợp mà một bài toán ở Chương 1 (còn mở, hoặc đã thành định lý) trở thành nền tảng hoặc động lực nghiên cứu trong khoa học máy tính và khoa học dữ liệu từ khoảng năm 2022. Đồng thời, bạn không nhầm một bộ giải dùng trong thực tế, một mô hình thay thế bằng mạng nơ-ron, hay một hệ thống giải hình học đạt mức huy chương với việc giải quyết câu hỏi toán học ban đầu.

## Kiến thức cần có

Các bài bắt buộc của chương, đặc biệt là [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Bốn màu]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/), và bài [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/). Trang này không nhắc lại các phát biểu đó.

## Mở đầu

Một bài toán của Viện Clay có thể vẫn chưa được giải, trong khi ngành công nghiệp vẫn viết và triển khai phần mềm *dựa trên những ý tưởng gần với nó*. Các bộ giải SAT xử lý những bài toán NP-đầy đủ cụ thể mà không chứng minh $$\mathbf{P}\neq\mathbf{NP}$$. Các toán tử học được (neural operator) dự báo trường vận tốc của chất lỏng mà không chứng minh nghiệm trơn của phương trình Navier–Stokes tồn tại. Một hệ thống giải hình học có thể viết lời giải bài thi olympic mà không giải được bài toán Kakeya. Vì vậy, điều bài này muốn rèn là cách diễn giải cho đúng. Các công trình gần đây trong khoa học máy tính và khoa học dữ liệu là thật, nhưng chúng không phải là lời giải "đi đường tắt" cho các bài toán lớn.

## Các khái niệm chính

Một bài toán quyết định NP-đầy đủ hỏi xem có tồn tại một chứng chỉ mà bộ kiểm tra xác nhận được trong thời gian đa thức theo kích thước đầu vào $$n$$ hay không. Câu hỏi về trường hợp xấu nhất vẫn chưa có lời giải. Trong thực tế, người ta hỏi một câu khác: với *công thức cụ thể này*, thuật toán tìm kiếm có học mệnh đề xung đột (CDCL) có cho kết quả kịp thời hạn không? Tương tự, một toán tử nơ-ron cố gắng xấp xỉ một ánh xạ nghiệm

$$
\mathcal{G}:u_0\mapsto u(\,\cdot\,,T)
$$

giữa các không gian hàm, chứ không chứng minh rằng $$u$$ vẫn trơn với mọi dữ kiện ban đầu $$u_0$$ trơn và có phân kỳ bằng không.

## Bốn ví dụ gần đây

### 1. Các cuộc thi SAT, "họ hàng" công nghiệp của P vs NP

Trong các kỳ SAT Competition từ 2022 đến 2024, các bộ giải CDCL vẫn đứng đầu trên những bộ bài kiểm tra công nghiệp và nhân tạo rất lớn. Một bộ giải chạy xong một bài **không** có nghĩa bài đó thuộc lớp độ phức tạp $$\mathbf{P}$$, và một họ công thức khó giải **không** chứng minh $$\mathbf{P}\neq\mathbf{NP}$$. Điều các cuộc thi cho thấy, về mặt ứng dụng, là cách nhìn NP qua *chứng chỉ* đã trở thành công cụ thực tế: trình biên dịch, kiểm chứng phần cứng và lập kế hoạch đều chuyển bài toán về dạng CNF, và tìm kiếm có học mệnh đề xung đột là cách tiếp cận mặc định. Hãy dùng bài P vs NP của chương này cho các định nghĩa, và dùng kết quả của các cuộc thi cho các dữ kiện kỹ thuật.

### 2. Toán tử nơ-ron làm mô hình thay thế cho Navier–Stokes

Kovachki, Li, Liu, Azizzadenesheli, Bhattacharya, Stuart và Anandkumar (2023) mô tả toán tử nơ-ron như các ánh xạ giữa những không gian hàm vô hạn chiều, và thử nghiệm trên phương trình Burgers, dòng chảy Darcy và Navier–Stokes. Toán tử nơ-ron Fourier học được một mô hình thay thế $$\widehat{\mathcal{G}}$$, tính nhanh hơn các bộ giải cổ điển nhiều bậc độ lớn trên cùng loại lưới. Còn câu hỏi Thiên niên kỷ là về sự tồn tại và độ trơn của nghiệm phương trình trên không gian liên tục. Sai số kiểm tra nhỏ của $$\widehat{\mathcal{G}}$$ chỉ là một quan sát thực nghiệm về một tập dữ liệu và một kiến trúc mạng. Hãy giữ hai điều này tách biệt.

### 3. AlphaGeometry: tính toán áp dụng cho hình học khó

Trinh, Wu, Le, He và Luong (2024) giới thiệu AlphaGeometry, một hệ thống chứng minh kết hợp mạng nơ-ron với suy luận ký hiệu, được huấn luyện trên một lượng lớn định lý sinh tự động. Trên bộ 30 bài hình học olympic, hệ thống giải được 25 bài, gần bằng thành tích trung bình của người đạt huy chương vàng IMO trên bộ bài đó. Đây là một kết quả khoa học máy tính về tìm kiếm, dữ liệu sinh tự động và một bộ máy suy diễn ký hiệu. Nó không phải là chứng minh cho Kakeya, và cũng không thay thế được lý thuyết về bài toán hạn chế được bàn trong chương này và Chương 2. Nhưng nó *là* bằng chứng rằng "hình học khó" có thể được biến thành một không gian tìm kiếm mà máy kiểm tra được.

### 4. Tìm kiếm vét cạn quanh bài toán Collatz

Barina (2021) công bố một phép kiểm tra trên GPU cho thấy ánh xạ Collatz đi vào chu trình tầm thường với mọi giá trị ban đầu đến cỡ $$2^{68}$$. Các bài kỹ thuật sau đó mở rộng phép tìm kiếm này. Nhưng một đoạn đầu hữu hạn, dù dài đến đâu, vẫn chỉ là một đoạn đầu hữu hạn. Định lý "hầu hết" của Tao và phát biểu còn mở cho "mọi $$n$$" vẫn là đối tượng của toán học. Đóng góp của khoa học máy tính là một phép tính đã được kiểm tra, đồng thời nhắc ta rằng tính toán không thể tự kết thúc câu hỏi.

## Diễn giải và nhận định

Trong mỗi trường hợp, bài toán lớn cung cấp một *khuôn mẫu* (chứng chỉ, độ trơn trên không gian liên tục, dựng hình, phép lặp), còn hệ thống được triển khai thì hoạt động trong một *giới hạn tài nguyên* cụ thể. Coi kết quả trong giới hạn đó như một định lý là lỗi điển hình của nhiều bài viết khoa học trong thập niên 2020.

## Giới hạn và hướng mở rộng

Bài này không biến RH, BSD hay giả thuyết số nguyên tố sinh đôi thành sản phẩm mật mã; những câu chuyện đó thuộc về số hạng sai số và bài lý thuyết số ở Chương 3. Bài cũng không đi sâu vào độ phức tạp của SAT hơn những gì đã nói trong bài P vs NP.

## Bài tập

1. Một nhà cung cấp tuyên bố: "bộ giải SAT của chúng tôi cho thấy P = NP trên mạch (netlist) của khách hàng." Hãy viết lại tuyên bố này cho khớp với các định nghĩa trong bài P vs NP.
2. Một công ty khởi nghiệp về khí hậu quảng cáo rằng toán tử nơ-ron của họ đã "giải Navier–Stokes." Bạn cần hai thông tin nào (phân phối dữ liệu huấn luyện; một chứng nhận về độ trơn) trước khi chấp nhận một phát biểu yếu hơn?
3. AlphaGeometry giải được 25 trên 30 bài hình học olympic. Vì sao điều đó không mâu thuẫn với việc Kakeya vẫn còn mở?
4. Nếu một phép tìm kiếm Collatz đi tới $$2^{80}$$, câu nào trong bài Collatz vẫn đúng y như hôm nay?

## Tài liệu tham khảo

- Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., & Anandkumar, A. (2023). Neural operator: Learning maps between function spaces with applications to PDEs. *JMLR*, 24(89), 1–97. [jmlr.org/papers/v24/21-1524.html](https://jmlr.org/papers/v24/21-1524.html).
- Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482. [doi:10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5).
- Barina, D. (2021). Convergence verification of the Collatz problem. *Journal of Supercomputing*, 77, 2681–2688. [doi:10.1007/s11227-020-03368-x](https://doi.org/10.1007/s11227-020-03368-x).
- [Chuỗi SAT Competition](https://satcompetition.github.io/) (các kỳ 2022–2024).
- Khóa học: [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/), [Navier–Stokes]({{ site.baseurl }}/contents/vi/chapter01/01_05_Navier_Stokes/), [Collatz]({{ site.baseurl }}/contents/vi/chapter01/01_07_Collatz_Conjecture/).

## Video tham khảo

- **Xem trước:** [Donald Knuth: Talk on SAT Solving @ JKU Linz (Recorded with Google Hangouts)](https://www.youtube.com/watch?v=QFMERqvfzlc) — Martina Seidl, tiếng Anh. Donald Knuth nói chuyện về các bộ giải SAT; nên xem trước khi đọc bài.
- [Fourier Neural Operator (FNO) (Physics Informed Machine Learning)](https://www.youtube.com/watch?v=W8PybqAk6Ik) — Steve Brunton, tiếng Anh. Giới thiệu toán tử nơ-ron Fourier; nên xem sau khi đã nắm ý chính của bài.
- [The AI that solved IMO Geometry Problems | Guest video by @Aleph0](https://www.youtube.com/watch?v=4NlrfOl0l8U) — 3Blue1Brown, tiếng Anh. Xem thêm sau hai video trên; giải thích cách AlphaGeometry giải các bài hình học IMO.
