---
layout: post
title: "Định lý Bốn Màu (Ý tưởng Chứng minh)"
chapter: '05'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter05
---

**Định lý Bốn Màu** khẳng định rằng mọi bản đồ phẳng đều có thể tô bằng nhiều nhất bốn màu sao cho các vùng kề nhau có màu khác nhau. Phát biểu này xuất hiện từ thế kỷ XIX và mãi đến năm 1976 mới được **Kenneth Appel** và **Wolfgang Haken** chứng minh. Đây là định lý lớn đầu tiên mà chứng minh **cần đến máy tính một cách thiết yếu**. Phần đóng góp của con người không mất đi, nhưng được tổ chức lại. Bài này trình bày **ý tưởng chứng minh**: đưa một họ vô hạn các bản đồ về một danh sách kiểm tra hữu hạn các cấu hình; chỉ ra rằng mọi phản ví dụ tối thiểu đều phải chứa một cấu hình trong một "tập không tránh được"; và mỗi cấu hình đó "rút gọn được", nên không thể xuất hiện trong phản ví dụ tối thiểu.

Hệ quả triết học vẫn còn nguyên giá trị: thế nào là chứng minh khi không ai đọc hết mọi trường hợp? Các chứng minh hình thức hóa về sau trong các trình hỗ trợ chứng minh trả lời một phần bằng cách kiểm tra lập luận hữu hạn đó trong một lõi logic đáng tin cậy.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Phát biểu Định lý Bốn Màu ở dạng bản đồ và dạng đồ thị (tô màu đỉnh của đồ thị phẳng, qua đồ thị đối ngẫu).
- Giải thích chiến lược chứng minh: phản ví dụ tối thiểu, tập không tránh được, cấu hình rút gọn được, và phương pháp discharging (phân phối lại điện tích).
- Mô tả sự phân công giữa phần sáng tạo của con người và phần liệt kê của máy.
- Phân biệt bốn màu (đúng) với "ba màu đủ cho mọi đồ thị phẳng" (sai) và năm màu (định lý cổ điển, dễ chứng minh hơn).
- Thảo luận ngắn gọn, công bằng về việc chứng minh có máy tính đã thay đổi gì trong tri thức toán học.
- Tránh nhầm lẫn với bản đồ trên các mặt khác và với việc tô màu bằng thuật toán trong thực tế.

**Kiến thức cần có.** Hiểu không hình thức về đồ thị phẳng, và biết phân tích trường hợp hữu hạn là gì. Không cần chạy lại chương trình năm 1976.

---

## 1. Phát biểu và đồ thị đối ngẫu

**Định lý Bốn Màu.** Các "nước" trên mọi bản đồ chính trị vẽ trên mặt phẳng (hoặc mặt cầu) có thể được tô bằng bốn màu sao cho hai nước kề nhau có màu khác nhau. Ở đây mỗi nước là một miền liên thông, và "kề nhau" nghĩa là có chung một đoạn biên có độ dài dương (không chỉ chung một điểm).

Theo ngôn ngữ đồ thị: đặt một đỉnh trong mỗi nước và nối hai đỉnh bằng một cạnh nếu hai nước chung biên. Ta được một **đồ thị phẳng**, và định lý trở thành: mọi đồ thị phẳng đều **tô được bằng 4 màu**. Các chi tiết kỹ thuật (cạnh bội, tính liên thông của nước, nghĩa chính xác của "kề") có thể xử lý ổn thỏa; phát biểu ở mức ý tưởng không thay đổi.

Năm màu thì đủ theo định lý cổ điển của Heawood (xuất phát từ hướng của Kempe). Ba màu **không** đủ cho mọi đồ thị phẳng. Vậy bốn là con số chính xác cho mặt phẳng.

---

## 2. Vì sao tấn công trực tiếp thì khó

Có vô hạn bản đồ phẳng. Một chứng minh hoặc phải tìm ra lý do cấu trúc cho thấy bốn màu luôn đủ, hoặc phải đưa bức tranh vô hạn này về một tập **hữu hạn** các tình huống bao quát mọi khả năng.

Chứng minh của Appel–Haken (và các chứng minh sau đó) đi theo hướng thứ hai, nối tiếp những nỗ lực của Kempe ở thế kỷ XIX. Chứng minh Kempe công bố có lỗi; chính lỗi đó cho thế hệ sau thấy những phép rút gọn nào mong manh. Chứng minh thành công đã sửa và mở rộng đáng kể kỹ thuật cấu hình và discharging.

---

## 3. Phản ví dụ tối thiểu

Giả sử (để đi đến mâu thuẫn) có một đồ thị phẳng không tô được bằng 4 màu. Trong các phản ví dụ, chọn cái **tối thiểu**, thường là cái có ít đỉnh nhất. Phản ví dụ tối thiểu có một tính chất hữu ích: bản thân nó không tô được, nhưng mọi đồ thị phẳng nhỏ hơn nó *đều* tô được bằng 4 màu. Do đó, nếu ta chỉ ra một mảnh cục bộ có thể co lại hoặc tô lại bằng cách dùng màu của đồ thị nhỏ hơn, thì mảnh đó không thể xuất hiện trong phản ví dụ tối thiểu.

Đó là logic của **tính rút gọn được**: một cấu hình là rút gọn được nếu sự có mặt của nó cho phép dựng một cách tô 4 màu toàn cục từ cách tô 4 màu của đồ thị nhỏ hơn, mâu thuẫn với tính tối thiểu của phản ví dụ chứa nó.

---

## 4. Tập không tránh được

**Tập không tránh được** các cấu hình là một danh sách $$\mathcal{U}=\{C_1,\ldots,C_N\}$$ sao cho **mọi** phản ví dụ tối thiểu đều phải chứa ít nhất một $$C_i$$.

Nếu mọi cấu hình trong tập không tránh được đều rút gọn được thì không tồn tại phản ví dụ tối thiểu: nó sẽ phải chứa một cấu hình rút gọn được, điều mà phản ví dụ tối thiểu không thể có. Mâu thuẫn này chứng minh định lý.

Toàn bộ chiến lược gói gọn trong hai khẳng định hữu hạn:

1. **Không tránh được:** mọi ứng viên cho phản ví dụ tối thiểu đều chứa một $$C_i\in\mathcal{U}$$.
2. **Rút gọn được:** mỗi $$C_i$$ đều rút gọn được.

Khẳng định 2, với danh sách dài, là nơi máy tính phát huy: mỗi cấu hình đòi hỏi kiểm tra rất nhiều cách mở rộng cách tô màu. Khẳng định 1 thường được chứng minh bằng **phương pháp discharging**, tức là sổ sách về bậc của đỉnh và cấu trúc của các mặt. Phương pháp này cho thấy một đồ thị "quá thưa" là không thể, và rằng "ở đâu đó phải có một mẫu cục bộ dày thuộc danh sách".

---

## 5. Discharging (cỗ máy do con người thiết kế)

Discharging là một lập luận phân phối lại cục bộ, hữu hạn. Ta gán "điện tích" cho đỉnh và mặt (cổ điển là dựa vào công thức Euler

$$
V-E+F=2
$$

cho đồ thị phẳng liên thông) sao cho tổng điện tích là một hằng số dương đã biết. Sau đó phân phối lại điện tích theo các quy tắc cục bộ. Sau khi phân phối, điện tích ở mọi vị trí chỉ không âm nếu có xuất hiện một cấu hình dày nào đó; nếu không, sẽ có chỗ mang điện tích âm, điều này không thể xảy ra. Vậy một cấu hình trong danh sách được thiết kế là không tránh được.

Thiết kế các quy tắc discharging và danh sách cấu hình là công việc tổ hợp thủ công rất sâu. Việc kiểm tra các quy tắc có chạy đúng và mỗi cấu hình có rút gọn được hay không dẫn đến một khối lượng trường hợp lớn mà máy kiểm tra được: gần hai nghìn cấu hình trong chứng minh của Appel–Haken (1.936 cấu hình), danh sách gọn hơn nhiều (633 cấu hình) trong chứng minh của Robertson–Sanders–Seymour–Thomas (1997), và cuối cùng là một chứng minh hình thức trong Coq (Gonthier và cộng sự).

---

## 6. Ý tưởng chứng minh trong một trang

1. Viết lại bài toán tô màu bản đồ thành bài toán tô 4 màu các đỉnh của đồ thị phẳng.
2. Giả sử có phản ví dụ tối thiểu $$G$$.
3. Đưa ra một tập không tránh được hữu hạn $$\mathcal{U}$$ (bằng discharging và công thức Euler).
4. Chứng minh mỗi cấu hình trong $$\mathcal{U}$$ rút gọn được (phân tích trường hợp, có máy hỗ trợ).
5. Kết luận không có phản ví dụ tối thiểu, tức mọi đồ thị phẳng đều tô được bằng 4 màu.

Con người thiết kế $$\mathcal{U}$$ và các quy tắc discharging; máy (hoặc trình hỗ trợ chứng minh) kiểm tra hàng loạt trường hợp cục bộ.

---

## 7. Chứng minh có máy tính và việc kiểm chứng về sau

Thông báo của Appel–Haken năm 1976 buộc giới toán học tranh luận: một chứng minh gồm hàng loạt trường hợp mà không ai đọc nổi thì có phải là chứng minh không? Dần dần cộng đồng chấp nhận chứng minh có máy tính khi:

- thuật toán được đặc tả rõ ràng;
- phép tính về nguyên tắc có thể tái lập;
- có kiểm tra độc lập và các đơn giản hóa tích lũy dần.

Chứng minh năm 1997 giảm bớt tập cấu hình và làm rõ cấu trúc. Chứng minh hình thức trong Coq của Georges Gonthier mã hóa lập luận để một trình hỗ trợ chứng minh kiểm từng bước dựa trên một lõi logic nhỏ. Điều đó không biến định lý thành "chỉ là chuyện của máy tính"; nó làm cho lập luận hữu hạn **được kiểm toán chặt chẽ**.

Bài học về phương pháp: *ý tưởng chứng minh có thể bao gồm việc thiết kế một bài kiểm tra hữu hạn.*

---

## 8. Định lý *không* nói gì

- Nó không khẳng định mọi bản đồ trên mọi mặt đều tô được bằng 4 màu; số màu cần thiết thay đổi theo giống của mặt (công thức Heawood cho giống cao hơn).
- Nó không cho một thuật toán thực tế nhanh nhất cho mọi trường hợp.
- Nó không nói mọi bản đồ *cần* bốn màu; chỉ nói bốn màu luôn đủ, còn ba màu thì không phải lúc nào cũng đủ.
- Nó không đồng nhất với **Định lý Năm Màu**, vốn có một chứng minh cổ điển ngắn.

---

## Nhầm lẫn thường gặp

1. "Máy kiểm tra ngẫu nhiên các bản đồ." Không: máy kiểm tra tính rút gọn được về mặt toán học cho các cấu hình trong một danh sách hữu hạn.
2. "Con người không chứng minh gì cả." Con người thiết kế phần discharging, tập không tránh được và các cấu hình rút gọn được.
3. "Bốn màu cho đồ thị phẳng nghĩa là bốn màu cho mọi đồ thị." Hoàn toàn sai; đồ thị không phẳng có thể cần nhiều màu tùy ý.
4. "Hai nước chạm nhau tại một điểm thì phải khác màu." Phát biểu chuẩn dùng đoạn biên, không tính trường hợp chạm tại một điểm.
5. "Ý tưởng chứng minh nghĩa là bỏ qua danh sách kiểm tra hữu hạn." Danh sách đó *chính là* xương sống; "ý tưởng" nghĩa là hiểu vì sao danh sách đó hoạt động.

---

## Bài tập

1. Giải thích đồ thị đối ngẫu: vì sao bài toán tô màu bản đồ trở thành bài toán tô màu đỉnh của đồ thị phẳng.
2. Chỉ ra rằng $$K_4$$ là đồ thị phẳng và cần 4 màu; vì sao điều đó cho thấy con số bốn là chính xác.
3. Vì sao phản ví dụ tối thiểu lại hữu ích? Trả lời trong năm câu.
4. Tự định nghĩa tập không tránh được và cấu hình rút gọn được.
5. Tra cứu (bên ngoài) số cấu hình của Appel–Haken và của Robertson cùng cộng sự; ghi lại các con số và một câu giải thích vì sao việc rút ngắn danh sách quan trọng.
6. **Thảo luận triết học (không quá 250 từ).** Khi nào bạn chấp nhận một chứng minh có máy tính? Nêu một tiêu chí.
7. **Viết tự luận (không quá 350 từ).** Giải thích ý tưởng chứng minh bốn màu cho một bạn học, không liệt kê hết các cấu hình.

---

## Kiến thức rút ra từ phần tìm hiểu video

Tóm tắt dùng khi thảo luận (đối chiếu với nguồn viết; **không bịa nội dung transcript**). Gói: `research/video-research/four-color-proof/analysis.md`.

### Tình trạng

**Đã được chứng minh** (Appel–Haken, 1976; sau đó được đơn giản hóa và kiểm chứng bởi Robertson cùng cộng sự, và bằng các bản hình thức hóa có máy kiểm tra). Cuộc tranh luận triết học về chứng minh có máy tính tách biệt với tình trạng của định lý.

### Phát biểu cốt lõi

Mọi đồ thị phẳng đều tô được bằng 4 màu (tương đương, mọi bản đồ trên mặt phẳng hoặc mặt cầu đều tô được bằng 4 màu sao cho các vùng kề nhau khác màu). Cấu trúc chứng minh: một tập không tránh được gồm các cấu hình rút gọn được, cùng với discharging.

### Các định nghĩa cần nắm chắc

- **Đồ thị phẳng.** Đồ thị có thể vẽ trên mặt phẳng mà không có cạnh nào cắt nhau.
- **Cấu hình rút gọn được.** Một mẫu cục bộ không thể xuất hiện trong phản ví dụ tối thiểu.

### Những hiểu lầm cần tránh

- Nghĩ rằng *mọi* bản đồ đều cần 4 màu (nhiều bản đồ cần ít hơn; 4 là cận trên cho trường hợp xấu nhất).
- Đánh đồng "có máy tính hỗ trợ" với "chưa được kiểm chứng" sau khi đã có các kiểm tra hiện đại.


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và làm quen với cách nghiên cứu**, không thay cho chứng minh hay bài báo gốc khi cần khẳng định quan trọng. Chi tiết xếp hạng: `research/video-research/four-color-proof/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile — Four Color Map Theorem (James Grime): [https://www.youtube.com/watch?v=NgbK43jB4rQ](https://www.youtube.com/watch?v=NgbK43jB4rQ).  
2. **Cốt lõi** — Quanta — Math's Map Coloring Problem / first computer-assisted proof: [https://www.youtube.com/watch?v=h7kqlYUV1l8](https://www.youtube.com/watch?v=h7kqlYUV1l8).  
3. **Làm rõ khái niệm** — Up and Atom — Four Color Theorem: What Counts as a Proof?: [https://www.youtube.com/watch?v=42-ws3bkrKM](https://www.youtube.com/watch?v=42-ws3bkrKM).  
4. **Phụ** — Numberphile2 — Four Color extra footage: [https://www.youtube.com/watch?v=laMkuPrad3s](https://www.youtube.com/watch?v=laMkuPrad3s).  

**Nhắc tình trạng:** **Đã được chứng minh** (Appel–Haken, 1976; sau đó được đơn giản hóa và kiểm chứng bởi Robertson cùng cộng sự, và bằng các bản hình thức hóa có máy kiểm tra). Cuộc tranh luận triết học về chứng minh có máy tính tách biệt với tình trạng của định lý.

---


### Transcript và khung hình (trích theo lô)

Transcript caption và unit theo thời gian: `research/video-research/four-color-proof/transcripts/` · trạng thái: `research/video-research/four-color-proof/TRANSCRIPT_STATUS.md` · danh sách master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/four-color-proof_NgbK43jB4rQ_thumb.jpg)

*Hình. Khung hình mẫu từ video chính của gói (xem gói nghiên cứu để biết mốc thời gian).*

## Tài liệu

1. Appel & Haken (1977). Every planar map is four colorable.
2. Robertson, Sanders, Seymour, Thomas (1997). The four-colour theorem.
3. Gonthier — chứng minh hình thức (Coq) của Định lý Bốn Màu.
4. Lịch sử nỗ lực của Kempe và định lý năm màu của Heawood.
5. Trong khóa học: [Euler–Königsberg]({{ site.baseurl }}/contents/vi/chapter05/05_05_Euler_Konigsberg/).

---


Danh mục URL đầy đủ: `research/video-research/four-color-proof/references.md`.

### Video (lộ trình gợi ý)

- Numberphile — Four Color Map Theorem (James Grime) (ORIENTATION): https://www.youtube.com/watch?v=NgbK43jB4rQ
- Quanta — Math's Map Coloring Problem / first computer-assisted proof (CORE): https://www.youtube.com/watch?v=h7kqlYUV1l8
- Up and Atom — Four Color Theorem: What Counts as a Proof? (HYGIENE): https://www.youtube.com/watch?v=42-ws3bkrKM
- Numberphile2 — Four Color extra footage (SECONDARY): https://www.youtube.com/watch?v=laMkuPrad3s

### Bài báo và web (từ gói nghiên cứu)

- Wikipedia — Four color theorem: https://en.wikipedia.org/wiki/Four_color_theorem
- Appel & Haken historical account (survey pages): https://en.wikipedia.org/wiki/Kenneth_Appel
- Robertson, Sanders, Seymour, Thomas — new proof survey (1997 era): https://en.wikipedia.org/wiki/Four_color_theorem#Simplification_and_verification
- Numberphile page: https://www.numberphile.com/videos/the-four-color-map-theorem
- Quanta Magazine related articles (map coloring / computer proofs): https://www.quantamagazine.org/

### Khóa học

- Gói: `research/video-research/four-color-proof/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- Đọc một cách triển khai discharging với tập không tránh được đồ chơi nhỏ.
- Tìm hiểu số màu trên mặt xuyến (torus) và các mặt khác.
- Thử xem trình hỗ trợ chứng minh mã hóa việc phân nhánh trường hợp hữu hạn như thế nào.
- Ghi lại một câu hỏi chính xác mà bạn vẫn còn thắc mắc.

## Video tham khảo

- **Xem trước** — [The Four Color Map Theorem - Numberphile](https://www.youtube.com/watch?v=NgbK43jB4rQ) — Numberphile, tiếng Anh. Video định hướng cho mục tiêu của bài: phát biểu Định lý Bốn Màu ở dạng bản đồ và dạng đồ thị.
- [The Map Coloring Puzzle That Changed Mathematics](https://www.youtube.com/watch?v=h7kqlYUV1l8) — Quanta Magazine, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ.
- [The Four Color Theorem - What Counts as a Proof?](https://www.youtube.com/watch?v=42-ws3bkrKM) — Up and Atom, tiếng Anh. Góc nhìn bổ sung sau hai video đầu.
