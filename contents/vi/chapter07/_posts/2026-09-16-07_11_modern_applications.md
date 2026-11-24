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

Tháng 11 năm 2022, David Smith — một kỹ thuật viên in ấn đã nghỉ hưu ở Yorkshire (Anh) thích mày mò ghép hình trên máy tính — gửi email cho nhà toán học Craig Kaplan với một đa giác 13 cạnh kỳ dị trông giống chiếc mũ phớt. Không ai ngờ rằng mảnh ghép ấy lại là "viên đá Einstein" (từ tiếng Đức *ein Stein* — một viên đá) mà giới hình học tìm kiếm suốt 60 năm: một hình duy nhất có thể lát kín vô tận mặt phẳng mà **không bao giờ lặp lại tuần hoàn**. Ngay sau đó, chỉ trong hai năm 2023–2024, một hệ thống AI kết hợp suy luận ký hiệu mang tên **AlphaGeometry** giải được 25/30 bài hình học thi Olympic Toán quốc tế (IMO), còn các cụm card đồ họa GPU tiếp tục đẩy giới hạn kiểm chứng giả thuyết Collatz vượt qua ngưỡng khổng lồ $$2^{68} \approx 2.95 \times 10^{20}$$.

Đứng trước những công cụ mạnh mẽ đến choáng ngợp ấy, người làm toán hôm nay rất dễ rơi vào một ảo giác nguy hiểm: *liệu máy tính đã có thể làm thay cuốn sổ ghi chép nghiên cứu của chúng ta?* Câu trả lời là **không**. Trái lại, máy tính càng mạnh thì kỷ luật của người cầm bút càng phải sắc bén: biết đặt giả thuyết rõ ràng trước khi bấm nút chạy, ghi chép trung thực phạm vi tính toán, và tuyệt đối không bao giờ đánh tráo một phép tính hữu hạn đã chạy xong thành một chứng minh toán học cho tới vô cùng.

## Mục tiêu học tập

Sau bài đọc thêm này, bạn sẽ:

- Hiểu cách vận dụng ba nhóm công cụ tính toán nổi bật giai đoạn 2022–2026 trong phòng thí nghiệm toán học: bộ giải SAT cho bài toán lát mặt phẳng, hệ thống thần kinh–ký hiệu (như AlphaGeometry) cho chứng minh hình học, và tìm kiếm GPU quy mô lớn cho giả thuyết Collatz.
- Biết cách tích hợp kết quả tính toán vào cuốn nhật ký nghiên cứu mà vẫn giữ chuẩn mực khoa học: tách bạch rạch ròi giữa *phép kiểm tra hữu hạn*, *chứng chỉ UNSAT*, và *định lý toán học*.
- Nhận diện giới hạn bản chất của từng công cụ để không đưa ra những kết luận vượt quá phạm vi chứng minh.

## Bản đồ kiến thức nền: Chứng minh hình thức, SAT và Toán học có máy tính hỗ trợ là gì, nghiên cứu những gì?

Khi sinh viên đại học dùng Python hay MATLAB, ta thường nghĩ máy tính chỉ giúp "tính xấp xỉ cho nhanh". Nhưng trong toán học hiện đại, máy tính còn tham gia trực tiếp vào **logic và chứng minh** thông qua ba nhánh giao thoa với Khoa học máy tính:

1. **Bài toán thỏa mãn Boolean (SAT) và Chứng chỉ UNSAT:** Một bộ giải SAT nhận vào hàng nghìn đến hàng triệu mệnh đề logic dạng *VÀ / HOẶC / PHỦ ĐỊNH* (CNF) rồi tìm cách gán Đúng/Sai thỏa mãn tất cả. Điều kỳ diệu là nếu bộ giải trả về **UNSAT (không thỏa được)**, các bộ giải hiện đại (như CaDiCaL, Kissat) có thể xuất ra một tệp **chứng chỉ (proof certificate)** mà một chương trình kiểm chứng độc lập, cực kỳ nhỏ gọn có thể kiểm tra lại từng bước logic! Nhờ đó, một tìm kiếm hữu hạn có thể trở thành một phần chứng minh chặt chẽ (như bài toán bộ ba Pythagoras Boolean hay tính số Heesch của viên lát).
2. **Trí tuệ nhân tạo thần kinh–ký hiệu (Neuro-Symbolic AI):** Mô hình ngôn ngữ lớn (LLM) rất giỏi trực giác đoán nước đi (chẳng hạn nên vẽ thêm điểm phụ hay đường tròn ngoại tiếp nào trong hình học), nhưng lại hay "ảo giác" khi suy luận dài. Hệ thống như **AlphaGeometry** giải quyết điểm yếu đó bằng cách ghép đôi: mạng nơ-ron chỉ đóng vai trò *gợi ý dựng hình phụ*, còn toàn bộ chuỗi suy diễn logic do một **bộ suy luận ký hiệu tất định** kiểm soát — đảm bảo mọi bước chứng minh sinh ra đều hợp lệ 100%.
3. **Tính toán kiểm chứng quy mô lớn (Large-Scale Verification):** Dùng GPU hoặc mạng lưới phân tán để quét qua hàng tỉ tỉ trường hợp (như kiểm tra Collatz đến $$2^{68}$$ hay kiểm tra không điểm của hàm zeta Riemann). Phương pháp này cực mạnh để **tìm phản ví dụ** (chỉ cần 1 phản ví dụ là bác bỏ được giả thuyết!), nhưng tự nó **không bao giờ** chứng minh được một mệnh đề đúng cho mọi số tự nhiên.

## Kiến thức cần có

Bài tổng quan của phần thực hành và ít nhất một trong các bài: [lặp / Collatz]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/), [lát mặt phẳng / tô màu bản đồ]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/), [Kakeya]({{ site.baseurl }}/contents/vi/chapter07/07_02_Explore_Kakeya/), hoặc [xếp cầu]({{ site.baseurl }}/contents/vi/chapter07/07_03_Explore_Sphere_Packing/).

## Phát triển khái niệm: Hữu hạn và Vô hạn trong nhật ký studio

Một bộ giải SAT cho biết một bài toán được mã hóa hữu hạn là thỏa được hay không thỏa được. Một hệ thống hình học trả về một chứng minh viết bằng ngôn ngữ hình học hình thức. Một chương trình kiểm tra Collatz cho kết quả "mọi $$n\le N$$ đều về 1". Điểm chung của chúng là: mỗi kết quả đều là một dữ kiện về một miền *hữu hạn* hoặc trong một hệ tiên đề *cố định*. Trong khi đó, các câu hỏi lớn của Chương 7 — như tập Kakeya có thể nhỏ đến đâu, hay mọi $$n \in \mathbb{N}$$ có về 1 không — đều chạm tới vô hạn trường hợp. Cách làm đúng là ghi kết quả máy tính vào nhật ký như một dòng dữ liệu có trích dẫn rõ ràng, rồi viết ngay bên cạnh câu hỏi vô hạn vẫn đang còn mở.

## Ba công cụ

### 1. Bộ giải SAT và viên lát "chiếc mũ"

Smith, Myers, Kaplan và Goodman-Strauss (2023/2024) đã dùng tìm kiếm bằng máy tính, trong đó có tính **số Heesch** (số vòng bao tối đa mà một viên lát có thể ghép quanh nó mà không bị kẹt) bằng bộ giải SAT, trong quá trình phát hiện và chứng minh tính không tuần hoàn của viên lát đơn "chiếc mũ" (hat).

Với phần thực hành về tô màu bản đồ và lát mặt phẳng, bài học rút ra không phải là "tải viên lát về là xong". Bài học là cách **mã hóa bài toán thành câu hỏi SAT**: ví dụ, với một bản đồ gồm 50 vùng, ta tạo $$50 \times 3 = 150$$ biến Boolean $$x_{v,c}$$ ("vùng $$v$$ được tô màu $$c$$"), thêm các mệnh đề ràng buộc "mỗi vùng có ít nhất 1 màu" và "hai vùng kề nhau không cùng màu", rồi hỏi bộ giải xem có tô được bằng 3 màu không. Nếu bộ giải trả về **UNSAT**, bạn có ngay một bằng chứng vững chắc rằng 3 màu là bất khả thi cho bản đồ đó, từ đó điều chỉnh giả thuyết hoặc tìm cấu trúc cản trở (như $$K_4$$). Trang web công khai của Kaplan về viên lát "chiếc mũ" là một hình mẫu tuyệt đẹp về cách chia sẻ mã nguồn và hình vẽ song hành với chứng minh toán học.

### 2. AlphaGeometry là công cụ hỗ trợ, không phải lời phán quyết

Trinh và cộng sự (2024) cho thấy một mô hình ngôn ngữ được huấn luyện trên 100 triệu chứng minh hình học tổng hợp, kết hợp với một bộ suy luận ký hiệu, có thể tạo ra lời giải hình học Olympic mà con người đọc hiểu và kiểm chứng được từng dòng.

Trong bài thực hành về Kakeya hoặc không gian bốn chiều, bạn hoàn toàn có thể dùng công cụ kiểu này để kiểm tra hoặc chứng minh một bổ đề hình học Euclid sơ cấp (chẳng hạn tính diện tích phần giao của hai tam giác trượt trong cây Perron). Nhưng cuốn nhật ký nghiên cứu vẫn bắt buộc ghi rõ hai điều: (1) bạn đã đặt giả định gì khi dịch bài toán sang ngôn ngữ hình thức, và (2) kết quả đó *không* nói được gì (ví dụ, một bổ đề hữu hạn về tam giác không tự động cho ra cận dưới số chiều Hausdorff cho tập Kakeya liên tục).

### 3. Kiểm tra Collatz là thí nghiệm có giới hạn

Barina (2021) và các đợt tìm kiếm bằng GPU sau đó đã kiểm tra giả thuyết Collatz cho mọi số nguyên dương lên tới $$N = 2^{68} \approx 2.95 \times 10^{20}$$ (và tiếp tục tăng thêm nhờ các tối ưu hóa sàng đồng dư). Để hình dung quy mô này: nếu kiểm tra mỗi số mất 1 nano-giây trên một lõi CPU đơn lẻ, phải mất gần 10.000 năm mới xong; nhờ gom theo lớp đồng dư và chạy song song trên GPU, nhóm nghiên cứu rút xuống còn tính bằng tháng.

Tuy nhiên, bài thực hành về phép lặp ở Chương 7 đã nhấn mạnh một nguyên tắc không thể thỏa hiệp: không bao giờ được viết *"đã kiểm tra đến $$2^{68}$$"* rồi suy ra *"vậy giả thuyết đúng với mọi $$n$$"*. Trong lịch sử lý thuyết số từng có những giả thuyết (như giả thuyết Pólya hay bất đẳng thức $$\pi(x) < \operatorname{li}(x)$$) đúng liên tục tới hàng trăm triệu, thậm chí $$10^{316}$$, rồi bất ngờ sai ở số lớn hơn! Hãy ghi cận GPU thành một dòng riêng trong bảng, ghi định lý của Terence Tao (2019) về "hầu hết" các số thành một dòng khác, và giữ nguyên khẳng định cho *mọi số nguyên dương* ở trạng thái **còn mở**.

## Nhận xét

Máy tính rất giỏi điền số liệu vào bảng và kiểm tra hàng tỉ trường hợp không biết mệt mỏi, nhưng nó không tự biết phân biệt khi nào một bảng số liệu mới chỉ là gợi ý, còn khi nào đã trở thành định lý. Trong xưởng thực hành toán học, giá trị lớn nhất của bạn nằm ở sự sắc sảo và trung thực trong cuốn nhật ký, chứ không phải ở việc ai có dàn GPU kiểm tra được $$N$$ lớn nhất.

## Giới hạn và hướng mở rộng

Bạn có thể áp dụng cùng kỷ luật "máy tính là kính hiển vi, không phải thẩm phán" cho các bài về mật độ xếp cầu, đồ thị khoảng cách giữa các số nguyên tố, và thí nghiệm ngẫu nhiên – trật tự. Riêng với từ điển đối ngẫu và từ điển vật lý–toán, hãy nhớ rằng nếu dùng mô hình ngôn ngữ để điền sẵn bảng thì đó mới chỉ là một **bản nháp thô** cần kiểm chứng từng dòng trạng thái, chưa thể gọi là từ điển nghiên cứu của chính bạn.

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
