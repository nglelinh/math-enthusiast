---
layout: post
title: "Lý thuyết Độ phức tạp"
chapter: '06'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter06
---

Hãy nghĩ về một bảng Sudoku cỡ lớn $$100\times 100$$. Nếu ai đó đưa cho bạn một bảng đã điền kín số, bạn chỉ mất vài phút để kiểm tra xem mỗi hàng, mỗi cột và mỗi ô vuông con có đủ các số từ 1 đến 100 không. Nhưng nếu người ta đưa bạn một bảng trống với vài chục gợi ý và bảo "giải đi", thời gian tìm ra lời giải có thể phình to đến mức vượt cả tuổi của vũ trụ. Liệu sự chênh lệch giữa **kiểm tra một lời giải** và **tự tìm ra lời giải** có phải là một quy luật bất biến của tự nhiên, hay chỉ vì ta chưa đủ thông minh để tìm ra đường tắt?

Có những bài toán khó vì ta kém may mắn chọn nhầm thuật toán. Nhưng có những bài toán dường như khó vì **mọi thuật toán có thể tồn tại** đều buộc phải trả giá theo hàm mũ. **Lý thuyết độ phức tạp tính toán** không nghiên cứu một thuật toán cụ thể, mà nghiên cứu *bản thân bài toán*: phân loại chúng theo tài nguyên tối thiểu cần thiết (thời gian, bộ nhớ, tính ngẫu nhiên, tương tác, cổng lượng tử) và nối chúng lại bằng các phép quy dẫn. Đó là toán học của **độ khó nội tại** — nền tảng của mật mã hiện đại, thiết kế thuật toán, và là chiếc thước đo tỉnh táo để soi những tuyên bố “thần kỳ” về AI hay máy tính lượng tử.

Bài này phác họa bản đồ các lớp độ phức tạp và ý tưởng cốt lõi: **P**, **NP**, NP-đầy đủ, tính ngẫu nhiên, chứng minh tương tác, các rào cản chứng minh và độ phức tạp lượng tử. Mục tiêu là giúp bạn đọc vững vàng ở vùng biên, chứ không thay cho giáo trình chuyên sâu như Garey–Johnson.

---

## Bản đồ kiến thức nền: Lý thuyết độ phức tạp là gì và nghiên cứu những gì?

Nếu khoa học máy tính ứng dụng hỏi *"làm sao viết chương trình chạy nhanh hơn?"*, thì **Lý thuyết Độ phức tạp Tính toán** (Computational Complexity Theory) hỏi câu hỏi ngược lại — và khó hơn nhiều: *"làm sao chứng minh rằng KHÔNG CÓ chương trình nào trên đời chạy nhanh hơn một ngưỡng nhất định?"*

Ngành này xoay quanh **bốn trụ cột tư duy**:

1. **Phân loại theo tài nguyên (Complexity Classes):** Gom các bài toán vào những "vùng đất" như **P** (giải nhanh), **NP** (kiểm chứng nhanh), **PSPACE** (tốn ít bộ nhớ), **BPP** (dùng tung xúc xắc ngẫu nhiên), **BQP** (dùng máy lượng tử).
2. **Phép quy dẫn và tính đầy đủ (Reductions & Completeness):** Vì chứng minh trực tiếp một bài toán là "không thể giải nhanh" quá khó, các nhà khoa học xây dựng một mạng lưới quy đổi: chứng minh rằng nếu bạn giải nhanh được bài toán $$B$$, bạn lập tức giải nhanh được cả nghìn bài toán khác. Đỉnh cao của tư duy này là lớp **NP-đầy đủ** — những bài toán "khó ngang nhau" và khó nhất trong NP.
3. **Các rào cản siêu toán học (Barriers):** Tại sao câu hỏi $$\mathbf{P} \stackrel{?}{=} \mathbf{NP}$$ đã đứng vững hơn nửa thế kỷ với giải thưởng 1 triệu USD? Lý thuyết độ phức tạp thậm chí còn chứng minh được *những giới hạn của chính các kỹ thuật chứng minh* (relativization, natural proofs, algebrization).
4. **Độ khó như một tài nguyên (Hardness as a Resource):** Độ khó không chỉ là tin xấu! Trong mật mã học và khử ngẫu nhiên, độ khó tính toán lại chính là *nguyên liệu quý* để khóa bí mật và tạo ra tính giả ngẫu nhiên.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Định nghĩa bài toán quyết định và các lớp **P**, **NP** (thời gian đa thức; có chứng cứ kiểm tra được trong thời gian đa thức).
- Giải thích phép quy dẫn thời gian đa thức và **NP-đầy đủ** nghĩa là gì (và không có nghĩa là gì).
- Phát biểu **P vs NP** như một câu hỏi toán học còn mở, không phải khẩu hiệu về năng suất.
- Mô tả tính ngẫu nhiên (BPP), tương tác (IP) và tính toán lượng tử (BQP) mở rộng mô hình tính toán như thế nào.
- Nối hàm một chiều và độ khó trung bình với mật mã, mà không tuyên bố những tách biệt giữa các lớp mà chưa ai chứng minh.
- Nhận ra các nhầm lẫn phổ biến (“NP nghĩa là không đa thức”, “máy lượng tử giải được bài toán NP-đầy đủ”).

**Kiến thức nền.** Thời gian chạy $$n,n\log n,n^2,2^n$$; toán rời rạc cơ bản. Biết máy Turing hình thức thì tốt, nhưng không bắt buộc cho mục tiêu đọc hiểu ở đây.

---

## 1. Bài toán, thể hiện và tài nguyên

Bài toán quyết định là một ngôn ngữ $$L\subseteq\{0,1\}^*$$: với đầu vào $$x$$, thuật toán chấp nhận nếu $$x\in L$$. Độ phức tạp nhóm các ngôn ngữ theo chi phí của thuật toán tốt nhất trong một mô hình (máy Turing tất định, họ mạch, mạch lượng tử, …). Thời gian $$T(n)$$ là hàm của độ dài đầu vào $$n=|x|$$.

**P** là lớp các bài toán quyết định giải được tất định trong thời gian đa thức, nghĩa là tồn tại $$c$$ và một máy chạy trong $$O(n^c)$$. Thời gian đa thức là một thước đo thô nhưng bền cho khái niệm “hiệu quả”, giữ nguyên giữa các mô hình hợp lý (luận đề Cobham–Edmonds, không phải một định lý phổ quát). Hãy cảm nhận khoảng cách giữa đa thức và hàm mũ: với $$n = 60$$, một thuật toán $$O(n^2)$$ chỉ cần $$3{,}600$$ bước (chưa tới một phần triệu giây), trong khi thuật toán $$O(2^n)$$ đòi $$2^{60} \approx 10^{18}$$ bước (hàng chục năm trên một CPU đơn lẻ).

Bài toán tìm kiếm và tối ưu gắn với phiên bản quyết định của chúng (ví dụ “đồ thị có clique cỡ $$k$$ không?”). Thuật toán xấp xỉ và độ khó của việc xấp xỉ cho ta bức tranh tinh hơn khi nghiệm chính xác là quá khó.

---

## 2. NP và việc kiểm chứng

**NP** là lớp các bài toán có **chứng cứ** (witness) ngắn mà ta kiểm tra được tất định trong thời gian đa thức. Chính xác hơn: $$x\in L$$ khi và chỉ khi tồn tại $$w$$ với $$|w|\le\operatorname{poly}(|x|)$$ sao cho bộ kiểm tra $$V(x,w)$$ chấp nhận trong thời gian đa thức.

Ví dụ cụ thể với bài toán **3-SAT**: cho một công thức logic như

$$
(x_1 \lor \neg x_2 \lor x_3) \land (\neg x_1 \lor x_2 \lor x_4) \land \cdots
$$

gồm hàng trăm biến và hàng nghìn mệnh đề. Tìm ra một bộ giá trị Đúng/Sai cho các biến sao cho toàn bộ công thức đúng có vẻ như mò kim đáy bể trong $$2^n$$ khả năng. Nhưng nếu ai đó đưa cho bạn một bộ gán cụ thể (chứng cứ $$w$$), bạn chỉ cần thay từng biến vào rồi kiểm tra từng mệnh đề — mất thời gian tuyến tính!

**Lưu ý quan trọng:** NP *không* có nghĩa là “non-polynomial” như cách hiểu thông thường trong tiếng Anh (chữ viết tắt đúng là *Nondeterministic Polynomial time*). Mọi ngôn ngữ trong P đều nằm trong NP (chỉ cần bỏ qua chứng cứ và tự giải). Câu hỏi $$\mathbf{P}=\mathbf{NP}?$$ vẫn còn mở.

---

## 3. Phép quy dẫn và NP-đầy đủ

$$A$$ quy dẫn Karp về $$B$$ nếu có hàm $$f$$ tính được trong thời gian đa thức sao cho $$x\in A\Leftrightarrow f(x)\in B$$. Nếu $$B\in\mathbf{P}$$ và $$A$$ quy dẫn về $$B$$ thì $$A\in\mathbf{P}$$. Độ khó lan **lên** theo chiều quy dẫn.

**Cook–Levin:** SAT là **NP-đầy đủ**, nghĩa là nó thuộc NP và mọi ngôn ngữ trong NP đều quy dẫn về nó. Hàng nghìn bài toán tự nhiên là NP-đầy đủ (tô màu đồ thị, chu trình Hamilton, phiên bản quyết định của quy hoạch nguyên, …). Đây là lý thuyết về độ khó **có điều kiện**: nếu một bài toán NP-đầy đủ thuộc P thì $$\mathbf{P}=\mathbf{NP}$$. Nói một cách hình ảnh, toàn bộ hàng nghìn bài toán NP-đầy đủ được buộc chặt vào nhau bằng dây leo núi: chỉ cần *một* bài rơi xuống lớp P, cả dây chuyền sẽ kéo nhau rơi theo.

**Cần hiểu đúng.** NP-đầy đủ nghĩa là khó nhất trong NP theo phép quy dẫn thời gian đa thức. Nó không có nghĩa là “không giải được”, không có nghĩa là “mọi thể hiện thực tế đều bất khả”, và độ khó trong trường hợp xấu nhất không phải là độ khó trung bình. Các thể hiện có cấu trúc có thể dễ; heuristic có thể chạy tốt; trường hợp trung bình có thể khác.

---

### Khung giải thích: tự tay kiểm chứng 3-SAT và quy dẫn sang Tập độc lập (nên đọc chậm)

Câu nói *"mọi bài toán trong NP đều quy dẫn được về bài toán khác bằng các mảnh ghép (gadget)"* nghe rất trừu tượng. Hãy tự tay dựng một phép quy dẫn thật từ bài toán logic **3-SAT** sang bài toán đồ thị **Tập độc lập** (*Independent Set* — tìm $$k$$ đỉnh đôi một không có cạnh nối).

Xét công thức 3-SAT gồm 3 biến và $$k = 2$$ mệnh đề:

$$
\varphi = \underbrace{(x_1 \lor \neg x_2 \lor x_3)}_{C_1} \;\land\; \underbrace{(\neg x_1 \lor x_2 \lor \neg x_3)}_{C_2}.
$$

1. **Kiểm chứng nhanh (bản chất của lớp NP):** Nếu ai đó đưa cho bạn chứng cứ $$w = (x_1=1,\, x_2=1,\, x_3=0)$$, bạn thay thẳng vào từng mệnh đề:
   - $$C_1 = (1 \lor 0 \lor 0) = 1$$ (Đúng),
   - $$C_2 = (0 \lor 1 \lor 1) = 1$$ (Đúng).
   Toàn bộ phép kiểm tra chỉ mất vài phép đọc — đó là lý do 3-SAT thuộc **NP**.

2. **Dựng đồ thị quy dẫn $$G = f(\varphi)$$ (gồm 6 đỉnh):**
   - **Mỗi mệnh đề thành một tam giác 3 đỉnh:** Mệnh đề $$C_1$$ tạo tam giác có 3 đỉnh gắn nhãn $$(x_1^{(1)},\, \neg x_2^{(1)},\, x_3^{(1)})$$; mệnh đề $$C_2$$ tạo tam giác $$(\neg x_1^{(2)},\, x_2^{(2)},\, \neg x_3^{(2)})$$. Vì 3 đỉnh trong cùng tam giác nối kín với nhau, bất kỳ tập độc lập nào cũng chọn được **tối đa 1 đỉnh** từ mỗi tam giác.
   - **Nối cạnh giữa mọi cặp mâu thuẫn:** Nối $$x_1^{(1)}$$ với $$\neg x_1^{(2)}$$, nối $$\neg x_2^{(1)}$$ với $$x_2^{(2)}$$, và nối $$x_3^{(1)}$$ với $$\neg x_3^{(2)}$$. Cạnh này cấm ta chọn đồng thời một biến vừa Đúng vừa Sai!

3. **Kiểm tra sự tương đương hai chiều bằng tay:**
   - **Chiều thuận:** Từ nghiệm $$(1, 1, 0)$$, chọn một chữ Đúng trong mỗi mệnh đề: đỉnh $$x_1^{(1)}$$ ở tam giác 1 và đỉnh $$x_2^{(2)}$$ ở tam giác 2. Kiểm tra trên đồ thị: giữa $$x_1^{(1)}$$ và $$x_2^{(2)}$$ **không có cạnh nối**, nên $$\{x_1^{(1)},\, x_2^{(2)}\}$$ là tập độc lập kích thước $$k = 2$$!
   - **Chiều ngược:** Nếu đồ thị có tập độc lập cỡ $$2$$, nó buộc phải lấy đúng 1 đỉnh ở tam giác 1 và 1 đỉnh ở tam giác 2, và hai đỉnh đó không được mâu thuẫn nhau (vì không có cạnh nối). Gán hai chữ được chọn bằng Đúng (các biến chưa dùng gán tùy ý), cả hai mệnh đề lập tức Đúng!

Phép biến đổi từ $$\varphi$$ sang đồ thị $$G$$ chỉ tốn thời gian tuyến tính theo số mệnh đề. Vì vậy, nếu ngày mai có ai tìm ra thuật toán chạy nhanh (thời gian đa thức) cho bài toán Tập độc lập trên đồ thị, ta lập tức giải nhanh được 3-SAT — và kéo theo toàn bộ lớp NP sụp đổ về P.

## 4. Một số lớp tiêu biểu

| Lớp / ý | Trực giác |
|---------|-----------|
| **PSPACE** | Bộ nhớ đa thức (thời gian có thể là hàm mũ) |
| **EXPTIME** | Thời gian hàm mũ |
| **BPP** | Ngẫu nhiên, thời gian đa thức, lỗi bị chặn |
| **IP** | Chứng minh tương tác; $$\mathbf{IP}=\mathbf{PSPACE}$$ (định lý nổi tiếng) |
| **#P** | Đếm nghiệm (số phép gán thỏa mãn, …) |
| **PH** | Phân cấp đa thức (các lượng từ xen kẽ) |
| **BQP** | Lượng tử, thời gian đa thức, lỗi bị chặn |

Nhiều quan hệ tách giữa các lớp vẫn còn mở. Relativization, natural proofs và algebrization là các **rào cản**, giải thích vì sao một số kỹ thuật chứng minh không thể tách P khỏi NP. Đây là phần “siêu toán” của lý thuyết độ phức tạp: hiểu *vì sao câu hỏi này khó*.

---

## 5. Tính ngẫu nhiên và khử ngẫu nhiên

Các thuật toán ngẫu nhiên (kiểm tra đồng nhất thức đa thức, kiểm tra số nguyên tố Miller–Rabin trong lịch sử) nằm trong BPP. Về khử ngẫu nhiên: nếu giả thiết có những chặn dưới đủ mạnh cho mạch, thì tính ngẫu nhiên có lẽ không làm tăng nhiều sức mạnh của thời gian đa thức ($$\mathbf{P}=\mathbf{BPP}$$ trong một số thế giới được giả định). Bộ sinh giả ngẫu nhiên nối độ khó với tính ngẫu nhiên, và là cầu nối sang mật mã.

---

## 6. Độ khó trung bình và mật mã

Mật mã cần những bài toán khó **trung bình** trên một phân phối mà ta lấy mẫu được hiệu quả, chứ không chỉ khó ở một vài trường hợp xấu nhất. Hàm một chiều, bộ sinh giả ngẫu nhiên và các giả thiết của mật mã khóa công khai hình thức hóa điều đó. Có những kết quả sâu nối độ khó trong trường hợp xấu nhất của lattice với độ khó trung bình kiểu LWE; những phép quy dẫn như vậy rất hiếm. Lý thuyết độ phức tạp cung cấp ngôn ngữ; phân tích mật mã và an ninh cụ thể cung cấp các con số.

**Độ phức tạp mịn** (SETH, độ khó của 3SUM, độ khó của APSP) nghiên cứu số mũ đa thức chính xác và các chặn dưới có điều kiện cho những bài toán *nằm trong* P, nên liên quan đến kỹ thuật thuật toán hằng ngày. Một thuật toán chạy dưới bậc ba (chẳng hạn bậc hai) cho bài toán đường đi ngắn nhất giữa mọi cặp đỉnh trên đồ thị dày sẽ bác bỏ một giả thuyết phổ biến của độ phức tạp mịn; đó là một loại “độ khó” khác với NP-đầy đủ, nhắm vào chế độ đa thức.

### Xấp xỉ và bài toán có điều kiện hứa (promise problem)

Khi việc tối ưu chính xác là NP-khó, ta hỏi về nghiệm xấp xỉ trong hệ số $$\rho$$. Định lý PCP và hệ thống các kết quả về độ khó của việc xấp xỉ giải thích vì sao một số tỉ lệ xấp xỉ là không thể đạt được nếu $$\mathbf{P}\neq\mathbf{NP}$$. Bài toán có điều kiện hứa (đáp án có hoặc không, cách nhau bởi một khoảng trống) xuất hiện trong kiểm thử tính chất và trong độ phức tạp lượng tử. Những phân biệt này quan trọng khi ai đó tuyên bố AI “giải” một bài toán tổ hợp khó: thường đó là nghiệm xấp xỉ, hoặc giới hạn trong một họ thể hiện hẹp, hoặc là thuật toán thời gian mũ chạy trên $$n$$ nhỏ.

---

## 7. Độ phức tạp lượng tử

**BQP** gồm các bài toán giải hiệu quả trên máy lượng tử với lỗi bị chặn. Phân tích thừa số thuộc BQP (Shor); người ta không biết nó có thuộc P hay không; và không tin rằng nó là NP-đầy đủ. Không ai biết máy lượng tử giải bài toán NP-đầy đủ trong thời gian đa thức; Grover tăng tốc bậc hai cho tìm kiếm không cấu trúc nhưng vẫn để lại độ tăng theo hàm mũ trên không gian $$2^n$$ (từ $$2^n$$ xuống $$2^{n/2}$$ vẫn là hàm mũ).

Xem [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [Mật mã biên giới]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).

---

## 8. Độ phức tạp, AI và lời thổi phồng

Học máy thường giải **bằng heuristic** các thể hiện của bài toán khó (tối ưu không lồi, kiểm chứng, tìm kiếm tổ hợp). Thành công trên các bộ benchmark không làm sụp đổ P vs NP. Ngược lại, việc một cách mã hóa nào đó là NP-đầy đủ cũng không chứng minh rằng nhiệm vụ ngoài đời là vô vọng, vì cách mã hóa bài toán có ảnh hưởng.

Độ phức tạp mạch và độ phức tạp chứng minh nối với câu hỏi mạng nông hay các chứng minh ngắn biểu diễn được những gì. Đó là một giao diện đang hoạt động chứ không phải khẩu hiệu.

### Hình dung về phép quy dẫn

Để chứng minh $$B$$ là NP-khó, ta dựng $$f$$ chạy trong thời gian đa thức sao cho $$\varphi$$ thỏa mãn được khi và chỉ khi $$f(\varphi)$$ là thể hiện “có” của $$B$$. Phép quy dẫn từ SAT sang bài toán 3-tô màu dùng các gadget cục bộ: biến bị ép nhận một trong hai “màu chân lý”, và mệnh đề tô được khi có ít nhất một literal đúng. Chi tiết khá rối, nhưng bài học tổng quát thì gọn:

> **Độ khó lan theo phép quy dẫn thời gian đa thức; còn tính dễ thì lan theo chiều ngược lại.**

Nếu có một thuật toán thời gian đa thức thật sự cho một bài toán NP-đầy đủ thì toàn bộ **NP** sụp về **P**. Một tuyên bố “giải hiệu quả bài toán NP-đầy đủ” cần được kiểm tra kỹ như một tuyên bố về mật mã: có thể đó là thể hiện đặc biệt, heuristic, mã hóa sai hoặc một sự kiện lịch sử.

### Những điều độ phức tạp *không* nói

Lý thuyết này mang tính tiệm cận và phụ thuộc vào mô hình. Nó không cho ta các hằng số trên máy tính xách tay, hay ngưỡng của một bộ giải MIP công nghiệp với 200 biến. Nó *cho biết* hy vọng nào cần một đột phá về khái niệm (SAT thời gian đa thức) và hy vọng nào chỉ cần kỹ thuật (heuristic, trường hợp trung bình, xấp xỉ, độ phức tạp tham số hóa / FPT). Một số bài toán NP-khó là khả giải với tham số cố định theo tham số $$k$$ (độ rộng cây, kích thước nghiệm, …), một lối thoát có định lý cho thực hành.

### Hoạt động nhóm

Chọn một tít báo kiểu “AI giải bài toán NP-khó”. Phân tích: (1) đó là phiên bản quyết định hay tối ưu? (2) kích thước $$n$$ bao nhiêu? (3) xấp xỉ, heuristic hay chính xác? (4) có phải một họ thể hiện đặc biệt không? Viết kết luận một đoạn: *không làm sụp P vs NP vì…* hoặc *cần kiểm tra lại nguồn vì…*.

---

## Những nhầm lẫn thường gặp

| Tuyên bố | Chỉnh lại |
|----------|-----------|
| “NP nghĩa là không đa thức.” | NP là không tất định thời gian đa thức, tức là kiểm chứng được trong thời gian đa thức. |
| “P vs NP là chuyện làm việc có đáng hay không.” | Sai phạm trù; đây là câu hỏi tiệm cận về thuật toán. |
| “NP-đầy đủ thì không giải được.” | Hằng ngày vẫn giải được ở cỡ vừa; độ khó chỉ là trong trường hợp xấu nhất và có điều kiện. |
| “Máy lượng tử giải được bài toán NP-đầy đủ.” | Chưa có thuật toán thời gian đa thức nào được biết. |
| “P=NP thì mật mã chết hoàn toàn.” | Quá thô; mật mã khóa công khai bị ảnh hưởng mạnh, còn mật mã đối xứng và các bối cảnh an toàn thông tin lý thuyết thì khác. |
| “Mạng nơ-ron giải đúng 99% câu đố nên P=NP.” | Hiệu năng thực nghiệm không phải thủ tục quyết định tổng quát. |

---

## Tóm tắt từ phần nghiên cứu video

Phần này dùng cho buổi seminar; hãy đối chiếu với nguồn gốc và không coi là bản chép lời.

### Hiện trạng

**P vs NP vẫn còn mở** (tính đến năm 2026). Lý thuyết NP-đầy đủ đã chín muồi; các chặn dưới cho mạch và khử ngẫu nhiên là những biên giới lớn.

### Phát biểu cốt lõi

Cook–Levin: SAT là NP-đầy đủ. Hàng nghìn bài toán tự nhiên là NP-đầy đủ thông qua phép quy dẫn thời gian đa thức. Câu hỏi P=NP? còn mở; đa số chuyên gia phỏng đoán P≠NP.

### Định nghĩa cần nhớ

- **P / NP.** P: quyết định được trong thời gian đa thức. NP: kiểm chứng được trong thời gian đa thức khi cho trước chứng cứ.
- **Phép quy dẫn.** Ánh xạ nhiều–một thời gian đa thức, giữ nguyên đáp án có/không.

### Cần phân biệt rõ

- Nghĩ rằng NP nghĩa là “không đa thức” (thực ra là không tất định đa thức, tức kiểm chứng được).
- Tuyên bố AI giải bài toán NP-đầy đủ “một cách tổng quát” trong thời gian đa thức.

---

## Nguồn video

Hãy dùng video để **định hướng và làm quen với văn hóa nghiên cứu**, đừng dùng thay cho chứng minh hay bài báo gốc khi cần khẳng định điều quan trọng.

**Thứ tự gợi ý**

1. **Cốt lõi**: Michael Sipser, Beyond Computation: P vs NP (Harvard): [https://www.youtube.com/watch?v=msp2y_Y5MLE](https://www.youtube.com/watch?v=msp2y_Y5MLE).  
2. **Nền tảng**: MIT OCW, Sipser, bài giảng về NP-đầy đủ: [https://www.youtube.com/watch?v=iZPzBHGDsWI](https://www.youtube.com/watch?v=iZPzBHGDsWI).  
3. **Định hướng**: Quanta, Biggest Puzzle in CS: P vs NP: [https://www.youtube.com/watch?v=pQsdygaYcE4](https://www.youtube.com/watch?v=pQsdygaYcE4).  

**Lưu ý về hiện trạng:** P vs NP vẫn còn mở (tính đến năm 2026). Lý thuyết NP-đầy đủ đã chín muồi; các chặn dưới cho mạch và khử ngẫu nhiên là những biên giới lớn.

---

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/complexity-theory_msp2y_Y5MLE_thumb.jpg)

*Hình. Khung hình mẫu từ video chính.*

## Tài liệu tham khảo

1. Arora & Barak — *Computational Complexity: A Modern Approach*.
2. Sipser — *Introduction to the Theory of Computation*.
3. Cook; Levin; Karp — lịch sử của NP-đầy đủ.
4. Ghi chú về các rào cản (relativization, natural proofs); Wigderson — *Mathematics and Computation*.
5. [Mật mã biên giới]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/), [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/), [ML theory]({{ site.baseurl }}/contents/vi/chapter06/06_10_ML_Theory/).

---

### Video (lộ trình gợi ý)

- Michael Sipser, Beyond Computation: P vs NP (Harvard) (cốt lõi): https://www.youtube.com/watch?v=msp2y_Y5MLE
- MIT OCW, Sipser, bài giảng về NP-đầy đủ (nền tảng): https://www.youtube.com/watch?v=iZPzBHGDsWI
- Quanta, Biggest Puzzle in CS: P vs NP (định hướng): https://www.youtube.com/watch?v=pQsdygaYcE4

### Bài báo và web

- Wikipedia — P versus NP: https://en.wikipedia.org/wiki/P_versus_NP
- Clay Math — P vs NP: https://www.claymath.org/millennium-problems/p-vs-np-problem
- Wikipedia — NP-completeness: https://en.wikipedia.org/wiki/NP-completeness
- MIT OCW 18.404J Theory of Computation: https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/
- Wikipedia — Complexity class: https://en.wikipedia.org/wiki/Complexity_class
- Wikipedia — Cook–Levin theorem: https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem

## Hướng đi tiếp

- Ứng dụng của độ khó: [Mật mã biên giới]({{ site.baseurl }}/contents/vi/chapter06/06_06_Future_Cryptography/).
- Các lớp lượng tử: [Thông tin lượng tử]({{ site.baseurl }}/contents/vi/chapter06/06_03_Quantum_Information/).
- Thực hành: giải SAT bằng vét cạn với $$n\le 20$$ và so với heuristic; vẽ biểu đồ thời gian chạy theo kích thước.
- Đọc: phần về NP của Sipser, mỗi ngày một sơ đồ quy dẫn, rồi đọc thử một chương của Arora–Barak.
- Nhớ phân biệt các quan hệ bao hàm: cái nào là định lý, cái nào là giả thuyết.

## Video tham khảo

- **Xem trước** — [Beyond Computation: The P vs NP Problem - Michael Sipser](https://www.youtube.com/watch?v=msp2y_Y5MLE) — PoincareDuality, tiếng Anh. Xem trước để nắm khái niệm bài toán quyết định, lớp P và NP.
- [15. NP-Completeness](https://www.youtube.com/watch?v=iZPzBHGDsWI) — MIT OpenCourseWare, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ, để theo dõi phép quy dẫn và NP-đầy đủ một cách chặt chẽ.
- [P vs NP Explained: Computer Science's Biggest Puzzle](https://www.youtube.com/watch?v=pQsdygaYcE4) — Quanta Magazine, tiếng Anh. Góc nhìn bổ sung sau hai video đầu, giải thích bài toán dưới dạng dễ tiếp cận.
