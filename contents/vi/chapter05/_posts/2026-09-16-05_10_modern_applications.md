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

Tháng 12 năm 2020, nhà toán học đoạt Huy chương Fields **Peter Scholze** đăng một bài viết đầy thẳng thắn lên blog: ông vừa cùng Dustin Clausen xây dựng một định lý nền tảng mới trong toán học ngưng tụ (*condensed mathematics*), với hàng chục trang đại số đồng điều tinh vi đến mức chính ông cũng không chắc 100% rằng không có một lỗi nhỏ nào ẩn nấp đâu đó. Scholze đặt ra một lời thách thức công khai — **Liquid Tensor Experiment**: *liệu một máy tính có thể kiểm chứng trọn vẹn một định lý toán học nghiên cứu mũi nhọn đương đại hay không?*

Mười tám tháng sau, cộng đồng trợ lý chứng minh **Lean** trả lời bằng một dấu kiểm xanh tuyệt đối. Và chỉ hai năm sau đó (2024), những hệ thống AI kết hợp học sâu với suy diễn ký hiệu như **AlphaGeometry** và **AlphaProof** bắt đầu tự tìm ra lời giải cho các bài toán Olympic Toán học Quốc tế (IMO) rồi gửi trực tiếp cho Lean kiểm duyệt. Câu chuyện từ Euclid, Cantor, Gödel đến Định lý Bốn Màu đang bước sang một chương mới: nơi chứng minh không chỉ nằm trên bảng đen hay giấy in, mà trở thành **mã chương trình được kiểm toán ở cấp độ tiên đề**.

**Mạch bài học:** Kiến thức cần nhớ (chứng minh hình thức & Curry–Howard, lý thuyết phạm trù, nguyên lý de Bruijn) → Giải thích: đọc một chứng minh thật trong Lean 4 và kiểm tra một phạm trù cụ thể bằng tay → Ba cột mốc 2022–2026 (Liquid Tensor Experiment, AlphaGeometry, AlphaProof) → Đối chiếu với giới hạn của Định lý Gödel.

---

## Mục tiêu học tập

Sau bài tùy chọn này, bạn có thể mô tả ba hệ thống tính toán trong giai đoạn 2022–2026 đưa thói quen của chương 5 (biến một khẳng định thành thứ máy tính kiểm tra được) vào Lean và vào các phương pháp tìm kiếm kết hợp mạng nơ-ron với suy diễn ký hiệu. Bạn cũng cần thấy rằng điều này vẫn nằm trong khuôn khổ của Gödel: một lõi kiểm chứng (kernel) đáng tin cậy không cho ta một lý thuyết đầy đủ về mọi chân lý số học.

---

## Kiến thức cần nhớ: Chứng minh hình thức, Lý thuyết kiểu và Lý thuyết phạm trù là gì?

Khi đọc các tin tức về Lean, Liquid Tensor Experiment hay AlphaProof, người tốt nghiệp đại học thường gặp ba thuật ngữ nghe rất "hàn lâm". Dưới đây là trực giác rõ ràng cho cả ba trụ cột:

### 1. Chứng minh hình thức (Formal Proof) & Lý thuyết kiểu (Curry–Howard)
Trong lập trình thông thường, một hàm nhận đầu vào kiểu `Int` và trả về kiểu `Bool`, và trình biên dịch kiểm tra kiểu dữ liệu để bắt lỗi. Nhờ **Tương ứng Curry–Howard**, các trợ lý chứng minh như **Lean** hay **Coq** biến toán học thành lập trình kiểu phụ thuộc (*dependent type theory*):
- Mỗi **mệnh đề toán học $$T$$** là một **kiểu dữ liệu (Type)**.
- Một **chứng minh** của $$T$$ chính là một **chương trình / phần tử (Term)** có đúng kiểu $$T$$!
Nếu bạn viết một lập luận có lỗ hổng nhỏ nhất, chương trình đơn giản là **không biên dịch được**.

### 2. Lý thuyết phạm trù (Category Theory) — ngôn ngữ của các cấu trúc và mũi tên
Nếu đại số đại học nghiên cứu từng cấu trúc riêng lẻ (nhóm, vành, không gian vector), thì **lý thuyết phạm trù** đứng cao hơn một tầng để nghiên cứu **các cấu trúc và những mũi tên (cấu xạ — morphisms)** nối giữa chúng. Một phạm trù gồm: (a) các *đối tượng*, (b) các *mũi tên* giữa chúng, (c) phép *hợp thành* mũi tên có tính kết hợp, và (d) mũi tên *đồng nhất* tại mỗi đối tượng. Các cầu nối bảo toàn cấu trúc giữa hai phạm trù gọi là **hàm tử (functor)** (ví dụ: ánh xạ gán mỗi không gian tôpô với nhóm cơ bản $$\pi_1$$ của nó chính là một hàm tử từ Tôpô sang Đại số!). Chính ngôn ngữ phạm trù (phạm trù Abel, nhóm đối đồng điều $$\mathrm{Ext}$$) là hạ tầng mà Liquid Tensor Experiment phải xây trong Lean.

### 3. Nghịch lý "người gác cổng của người gác cổng" và Nguyên lý de Bruijn
Trong đời thường, khi AI viết ra một bài chứng minh dài 5 trang, ta rơi vào nghịch lý: *"AI hay ảo giác, vậy ai kiểm tra AI? Nếu dùng AI thứ hai kiểm tra thì ai kiểm tra AI thứ hai?"* Các trợ lý chứng minh dập tắt vòng lặp vô hạn đó bằng **nguyên lý de Bruijn**: tách hẳn **bộ tìm kiếm** (con người hoặc mạng nơ-ron khổng lồ hàng tỷ tham số, được phép thử sai thoải mái) khỏi **lõi kiểm chứng (kernel)** cực nhỏ chỉ vài nghìn dòng mã thuần túy. Con người chỉ cần kiểm toán đúng lõi nhỏ ấy — nếu kernel gật đầu, chứng minh chắc chắn hợp lệ từ tiên đề!

---

## Kiến thức cần có

Các bài chứng minh trước đó, đặc biệt là [Euclid và vô hạn số nguyên tố]({{ site.baseurl }}/contents/vi/chapter05/05_02_Euclid_Infinite_Primes/), [Gödel]({{ site.baseurl }}/contents/vi/chapter05/05_04_Godel_Incompleteness/), [bốn màu]({{ site.baseurl }}/contents/vi/chapter05/05_07_Four_Color_Proof/) và [Fermat]({{ site.baseurl }}/contents/vi/chapter05/05_08_Fermat_Last_Theorem/). Trang này không kể lại các lập luận đó.

---

## Giải thích: tự tay đọc một chứng minh thật trong Lean 4 và kiểm tra một phạm trù

Để cảm nhận rõ "biến chứng minh thành chương trình" thực tế trông như thế nào, hãy đọc chậm hai ví dụ cầm tay dưới đây:

### Ví dụ cầm tay 1: Một chứng minh thật trong Lean 4 (Tương ứng Curry–Howard)
Xét định lý logic cơ bản (luật *Modus Ponens*): *"Nếu $$P$$ đúng, và $$P \implies Q$$ đúng, thì $$Q$$ đúng."* Trong ngôn ngữ Lean 4, ta viết nguyên văn như một hàm lập trình:

```lean
theorem modus_ponens (P Q : Prop) (hp : P) (hpq : P → Q) : Q :=
  hpq hp
```

Hãy đọc từng mảnh như một lập trình viên:
- `P Q : Prop` khai báo hai mệnh đề (hai kiểu dữ liệu).
- `hp : P` là giả thiết — một "bằng chứng" (phần tử) thuộc kiểu `P`.
- `hpq : P → Q` là giả thiết thứ hai — một **hàm** nhận bằng chứng của `P` và trả về bằng chứng của `Q`.
- Kết luận `: Q` yêu cầu ta nộp ra một phần tử thuộc kiểu `Q`.
- Thân chứng minh `hpq hp` đơn giản là **gọi hàm `hpq` lên đầu vào `hp`**! Kernel của Lean kiểm tra kiểu: `hp` có kiểu `P`, `hpq` có kiểu `P → Q`, suy ra `hpq hp` có đúng kiểu `Q` → **dấu kiểm xanh!**

Tương tự, với bài toán số học *"nếu $$n$$ chẵn thì $$n^2$$ chẵn"*: giả sử ta có bằng chứng $$n = 2k$$, ta chỉ việc cung cấp nhân chứng mới $$m = 2k^2$$ và để kernel kiểm tra đẳng thức đại số $$(2k)^2 = 2(2k^2)$$. Mọi định lý khổng lồ như Liquid Tensor Experiment đều được xây chồng từ hàng nghìn khối gạch nhỏ chặt chẽ y hệt như vậy.

### Ví dụ cầm tay 2: Kiểm tra trực tiếp các tiên đề của một Phạm trù (Category)
Xét một phạm trù quen thuộc nhất với sinh viên đại học — phạm trù **$$\mathbf{Set}$$**:
- **Đối tượng:** các tập hợp (ví dụ $$A = \{1, 2\},\ B = \{x, y\},\ C = \{\text{Đỏ}, \text{Xanh}\}$$)
- **Mũi tên (cấu xạ):** các hàm số $$f: A \to B$$ và $$g: B \to C$$.
- **Kiểm tra bằng tay hai tiên đề phạm trù:**
  1. *Mũi tên đồng nhất:* Với mỗi tập $$A$$, hàm $$\mathrm{id}_A(a) = a$$ thỏa $$f \circ \mathrm{id}_A = f$$ và $$\mathrm{id}_B \circ f = f$$.
  2. *Tính kết hợp:* Với $$f: A \to B$$, $$g: B \to C$$, $$h: C \to D$$, tại mọi $$a \in A$$ ta luôn có $$\bigl((h \circ g) \circ f\bigr)(a) = h\bigl(g(f(a))\bigr) = \bigl(h \circ (g \circ f)\bigr)(a)$$.

Khi thay tập hợp bằng **không gian vector** và hàm bằng **ánh xạ tuyến tính (ma trận)**, ta có phạm trù **$$\mathbf{Vect}$$**. Phép gán một ma trận vuông $$M$$ với định thức $$\det(M)$$ biến phép nhân ma trận thành phép nhân số ($$\det(AB) = \det(A)\det(B)$$, $$\det(I) = 1$$) — đó chính là một **hàm tử** bảo toàn cấu trúc!

---

## Phát triển khái niệm: Lean, AI và giới hạn của Gödel

Một trợ lý chứng minh kiểm tra rằng một hạng tử thuộc về một kiểu nào đó. Nếu $$T$$ là một phát biểu hình thức thì một chứng minh trong Lean là một phần tử của kiểu $$T$$, xét tương đối theo kernel, các tiên đề và các thư viện mà bạn tin tưởng.

**Vì sao điều này không mâu thuẫn với Định lý bất toàn Gödel?** Định lý bất toàn của Gödel nói rằng mọi lý thuyết nhất quán, có tiên đề cho được hiệu quả, và đủ phong phú để làm số học đều để lại một số câu số học không quyết định được — và không tồn tại thuật toán vạn năng tự động trả lời đúng/sai cho *mọi* bài toán toán học. Hai sự thật này hoàn toàn cùng tồn tại:

| Điều Lean & AlphaProof **LÀM ĐƯỢC** | Điều Định lý Gödel vẫn **GIỚI HẠN** |
|-------------------------------------|-------------------------------------|
| Kiểm tra chắc chắn *một chứng minh cụ thể* khi đã dựng được hạng tử hợp lệ. | Không có thuật toán đảm bảo tìm ra chứng minh (hoặc phản chứng) cho *mọi* mệnh đề số học. |
| Phối hợp AI tìm kiếm với kernel để giảm tối đa sai sót của con người. | Bản thân hệ tiên đề của Lean không thể tự chứng minh tính nhất quán tuyệt đối của chính mình từ bên trong. |

Bạn hoàn toàn có thể kiểm chứng chắc chắn *định lý này* ngay hôm nay mà vẫn không có một thủ tục quyết định vạn năng cho mọi định lý.

---

## Ba ví dụ cột mốc (2022–2026)

### 1. Liquid Tensor Experiment (2022)

Ngày 14 tháng 7 năm 2022, cộng đồng Lean, do Johan Commelin dẫn đầu và với phần toán học do Scholze đưa ra, thông báo đã hoàn thành Liquid Tensor Experiment: kiểm chứng hình thức một định lý đầy thách thức về các không gian vector "lỏng" (sự triệt tiêu của một số nhóm $$\mathrm{Ext}$$).

Để "giải thích" được phát biểu của Scholze cho máy tính, nhóm dự án không thể nhảy thẳng vào định lý chính. Họ phải dành nhiều tháng xây dựng hàng chục nghìn dòng thư viện nền trong `mathlib` về **lý thuyết phạm trù** (phạm trù Abel, phức dây chuyền, đối đồng điều) và dùng một "bản đồ phụ thuộc" (*blueprint*) chia bài toán khổng lồ thành hàng trăm bổ đề nhỏ để hàng chục nhà toán học trên thế giới cùng đóng góp song song. Bài học giống với việc hình thức hóa định lý bốn màu và giả thuyết Kepler: một lập luận nghiên cứu mũi nhọn có thể "nói chuyện" được với kernel, nhưng chỉ sau khi đầu tư bài bản vào hạ tầng thư viện. *Ý tưởng* của định lý vẫn là của Scholze và Clausen; *sản phẩm* là một kho mã kiểm chứng được.

### 2. AlphaGeometry (2024)

Trinh và cộng sự (2024) kết hợp một mô hình ngôn ngữ được huấn luyện trên hàng trăm triệu định lý hình học tổng hợp với một máy suy diễn ký hiệu. Hệ thống này viết ra các chứng minh mà con người đọc được, và giải **25 trên 30** bài hình học olympic trong bộ thử nghiệm của nhóm tác giả.

Trong hình học phẳng Olympic, máy suy diễn ký hiệu rất giỏi cộng góc hay tìm tam giác đồng dạng, nhưng thường bị "tắc" khi bài toán đòi hỏi phải **vẽ thêm một đường phụ hoặc điểm phụ** (chẳng hạn lấy trung điểm $$M$$ hay dựng đường tròn ngoại tiếp phụ). AlphaGeometry giao đúng phần "trực giác gợi ý điểm phụ" cho mô hình ngôn ngữ, còn phần kiểm tra và suy luận chặt chẽ giao cho động cơ ký hiệu. Đây là tìm kiếm kết hợp với ngôn ngữ thân thiện với bộ kiểm tra, gần với tinh thần của một "nước đi Euclid" được tổ chức tốt hơn là một bài luận của mô hình ngôn ngữ. Nó không thay thế bài học của chứng minh bằng máy trong định lý bốn màu về việc *điều gì được tính* là chứng minh; nó chỉ thêm một bộ sinh ra chứng minh mà con người vẫn đọc được.

### 3. AlphaProof và IMO 2024

Thông báo ngày 25 tháng 7 năm 2024 của DeepMind, sau đó được mở rộng trong một bài trên *Nature* năm 2025, mô tả AlphaProof là một tác nhân theo kiểu AlphaZero tìm chứng minh trong Lean, dùng học tăng cường ngay lúc chạy (*test-time reinforcement learning*) với các bài khó: khi gặp một bài toán hóc búa, nó tự sinh hàng triệu biến thể dễ hơn xung quanh bài toán đó để tự luyện tập cho đến khi tìm ra lối đi.

Cùng với AlphaGeometry 2, hệ thống giải được **4 trên 6** bài của IMO 2024 (kể cả bài số 6 cực khó về lý thuyết số/hàm số), đạt **28 trên 42 điểm**, *tương đương huy chương bạc theo bảng điểm*. Có hai chú thích quan trọng: đề bài được chuyên gia hình thức hóa sang ngôn ngữ Lean trước, và thời gian tính toán (lên tới vài ngày) vượt xa thời gian thi 9 giờ của thí sinh. Cách đọc đúng theo tinh thần chương 5 là: **kernel vẫn là trọng tài duy nhất quyết định điều gì là chứng minh**; điều mới là cách các ứng viên chứng minh được đề xuất.

---

## Diễn giải và nhận định

Một dấu kiểm xanh của Lean là sự bảo đảm tương đối so với một đặc tả, đúng như tinh thần về kiểm chứng ở chương 9. Nó không chứng minh rằng bài toán gốc (viết bằng tiếng Anh hay tiếng Việt) đã được dịch sang phát biểu hình thức đúng ý tác giả — lỗi dịch đặc tả vẫn là trách nhiệm của con người — và cũng không phải lối thoát khỏi định lý bất toàn Gödel. *Số điểm* ngang huy chương bạc của AlphaProof không phải là huy chương bạc được trao cho một thí sinh theo luật của IMO.

## Giới hạn và hướng mở rộng

Bài này không hình thức hóa FLT hay giả thuyết Poincaré (dù một dự án cộng đồng lớn do Kevin Buzzard khởi xướng đang tiến hành hình thức hóa Định lý lớn Fermat trong Lean!). Nó cũng không khẳng định các bài tổ hợp nay đã dễ với các tác nhân dùng Lean (cả hai bài tổ hợp của IMO 2024 đều không được hệ thống giải).

## Tài liệu tham khảo

- Cộng đồng Lean. (2022). Completion of the Liquid Tensor Experiment. [leanprover-community.github.io/blog/posts/lte-final](https://leanprover-community.github.io/blog/posts/lte-final/).
- Trinh, T. H., Wu, Y., Le, Q. V., He, H., & Luong, T. (2024). Solving olympiad geometry without human demonstrations. *Nature*, 625, 476–482. [doi:10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5).
- Google DeepMind. (2024). AI achieves silver-medal standard solving International Mathematical Olympiad problems. [Blog, 25 July 2024](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/).
- Hubert, T., et al. (2025). Olympiad-level formal mathematical reasoning with reinforcement learning. *Nature*. [doi:10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y).

## Video tham khảo

- **Xem trước** — [Proving theorems with computers - Kevin Buzzard](https://www.youtube.com/watch?v=KccjCojGVO4) — Stony Brook Mathematics, tiếng Anh. Video định hướng cho mục tiêu của bài: dùng máy tính để kiểm chứng chứng minh.
- [The AI that solved IMO Geometry Problems | Guest video by @Aleph0](https://www.youtube.com/watch?v=4NlrfOl0l8U) — 3Blue1Brown, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ; nói về AlphaGeometry.
- [Improving on AlphaProof: IMO 2024 Problem 2 in Lean 4](https://www.youtube.com/watch?v=5IARsdn78xE) — David Renshaw, tiếng Anh. Một bản hình thức hóa bằng Lean 4 cho bài IMO 2024, theo tinh thần của AlphaProof. Nên dùng cạnh chủ đề kiểm chứng của bài, vì đây không phải bài nói chính thức của DeepMind.
