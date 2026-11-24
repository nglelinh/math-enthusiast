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

Năm 1852 tại London, chàng sinh viên trẻ **Francis Guthrie** ngồi tô màu bản đồ các hạt của nước Anh sao cho không hai hạt nào chung biên giới bị trùng màu. Một câu hỏi đơn giản đến mức đứa trẻ mười tuổi cũng hiểu chợt lóe lên: *liệu bốn màu có luôn luôn đủ cho **mọi** bản đồ phẳng vẽ được hay không?*

Chẳng ai ngờ câu đố màu sắc ấy lại hành hạ giới toán học suốt **124 năm**. Năm 1879, luật sư kiêm nhà toán học Alfred Kempe công bố một lời giải thanh lịch và cả thế giới reo mừng — cho đến 11 năm sau, Percy Heawood phát hiện một lỗ hổng tinh vi giấu kín trong lập luận đổi màu chuỗi của Kempe (lập luận đó đủ chứng minh **Năm màu**, nhưng không đủ cho Bốn màu!). Phải đến năm 1976, **Kenneth Appel** và **Wolfgang Haken** mới khép lại bài toán bằng cách nhờ máy tính kiểm tra hàng nghìn cấu hình — tạo ra định lý lớn đầu tiên trong lịch sử mà chứng minh **cần đến máy tính một cách thiết yếu**.

Bài này trình bày **ý tưởng chứng minh** phía sau cuộc cách mạng đó: đưa một vũ trụ vô hạn các bản đồ về một danh sách kiểm tra hữu hạn các cấu hình; dùng phương pháp *discharging* để chứng minh mọi phản ví dụ tối thiểu đều chứa một cấu hình trong "tập không tránh được"; và chỉ ra mọi cấu hình ấy đều "rút gọn được". Hệ quả triết học vẫn còn nóng hổi đến tận hôm nay: *điều gì được gọi là chứng minh khi không một con người nào có thể tự mắt đọc hết từng trường hợp?*

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

## Bản đồ kiến thức nền: Lý thuyết đồ thị phẳng, đối ngẫu và chứng minh có máy tính hỗ trợ là gì?

Để người tốt nghiệp đại học nắm ngay bức tranh toàn cảnh trước khi đi vào kỹ thuật *discharging*, đây là bốn khái niệm trụ cột đứng sau Định lý Bốn Màu:

- **Đồ thị phẳng (Planar Graph) & Đồ thị đối ngẫu (Dual Graph):** Một đồ thị gọi là *phẳng* nếu ta vẽ được nó trên mặt giấy mà không có hai cạnh nào cắt chéo nhau. Mỗi bản đồ chính trị đều biến thành một đồ thị phẳng bằng cách đặt một **đỉnh** vào thủ đô mỗi nước và vẽ một **cạnh** nối hai nước chung đường biên. Nhờ phép đối ngẫu này, bài toán "tô màu các miền bản đồ" tương đương tuyệt đối với bài toán "tô màu các đỉnh sao cho hai đỉnh nối cạnh khác màu".
- **Công thức Euler cho đồ thị phẳng ($$V - E + F = 2$$):** Với mọi đồ thị phẳng liên thông có $$V$$ đỉnh, $$E$$ cạnh và $$F$$ miền (kể cả miền vô hạn bên ngoài), hiệu $$V - E + F$$ luôn bằng $$2$$. Một hệ quả thần kỳ của công thức này là: **mọi đồ thị phẳng đơn đều có ít nhất một đỉnh bậc $$\le 5$$** (tức là trên mọi bản đồ phẳng, luôn tồn tại ít nhất một quốc gia có nhiều nhất $$5$$ nước láng giềng!). Chính định lý nhỏ này làm động cơ cho cả chứng minh Năm màu lẫn chiến lược Bốn màu.
- **Sắc số (Chromatic Number $$\chi(G)$$):** Số màu tối thiểu cần để tô hợp lệ các đỉnh của $$G$$. Định lý Bốn Màu nói gọn: mọi đồ thị phẳng đều có $$\chi(G) \le 4$$. (Lưu ý: đồ thị không phẳng có thể cần tùy ý nhiều màu; ví dụ đồ thị đầy đủ $$K_n$$ cần đúng $$n$$ màu.)
- **Chứng minh có máy tính hỗ trợ vs. Chứng minh hình thức (Formal Proof):** Năm 1976, Appel–Haken viết chương trình máy tính kiểm tra 1.936 cấu hình, nhưng người đọc phải tin rằng mã nguồn không có lỗi lập trình. Đến năm 2005, Georges Gonthier hình thức hóa toàn bộ chứng minh trong trợ lý chứng minh **Coq**, nơi một lõi logic (*kernel*) cực nhỏ kiểm tra từng bước suy diễn từ tiên đề — biến nỗi lo "lỗi phần mềm" thành sự kiểm toán chặt chẽ bậc nhất.

---

## 1. Phát biểu, đồ thị đối ngẫu — và bẫy trực giác đời thường

### Từ câu đố bản đồ đến bẫy của Kempe

Hãy thử tự tay vẽ một bản đồ cần nhiều màu nhất có thể trên tờ giấy. Bạn đặt 3 nước đôi một tiếp giáp nhau (dễ, cần 3 màu). Bạn bao bọc chúng bằng nước thứ 4 chạm cả 3 nước kia (tạo thành đồ thị đầy đủ $$K_4$$ — cần đúng 4 màu). Bây giờ hãy thử thêm nước thứ 5 sao cho nó chạm *cả 4* nước cũ mà không nhảy qua biên giới hay đục hầm xuyên giấy: bạn sẽ bị nhốt ngay lập tức, vì đồ thị đầy đủ $$K_5$$ **không thể vẽ phẳng** trên tờ giấy!

Điều này sinh ra một trực giác rất hấp dẫn nhưng lại **sai**: nhiều người nghĩ *"không có 5 nước đôi một chạm nhau thì chắc chắn 4 màu là đủ"*. Thực tế, trong lý thuyết đồ thị tồn tại những đồ thị thậm chí không có hình tam giác ($$K_3$$) nào mà vẫn cần 4, 5 hay 100 màu! Bản đồ phẳng phức tạp hơn thế nhiều: các ràng buộc màu lan truyền dây chuyền từ đầu này sang đầu kia của bản đồ. Chính vì những chuỗi lan truyền màu (*chuỗi Kempe*) có thể đan chéo và vô hiệu hóa lẫn nhau nên chứng minh nổi tiếng năm 1879 của Kempe đã sụp đổ ở bước tưởng như hiển nhiên nhất.

### Phát biểu chuẩn

**Định lý Bốn Màu.** Các "nước" trên mọi bản đồ chính trị vẽ trên mặt phẳng (hoặc mặt cầu) có thể được tô bằng bốn màu sao cho hai nước kề nhau có màu khác nhau. Ở đây mỗi nước là một miền liên thông, và "kề nhau" nghĩa là có chung một đoạn biên có độ dài dương (không chỉ chung một điểm, như bốn bang tại điểm Four Corners của Mỹ).

Theo ngôn ngữ đồ thị: đặt một đỉnh trong mỗi nước và nối hai đỉnh bằng một cạnh nếu hai nước chung biên. Ta được một **đồ thị phẳng**, và định lý trở thành: mọi đồ thị phẳng đều **tô được bằng 4 màu**. Các chi tiết kỹ thuật (cạnh bội, tính liên thông của nước, nghĩa chính xác của "kề") có thể xử lý ổn thỏa; phát biểu ở mức ý tưởng không thay đổi.

Năm màu thì đủ theo định lý cổ điển của Heawood (xuất phát từ hướng của Kempe). Ba màu **không** đủ cho mọi đồ thị phẳng (vì $$K_4$$ là đồ thị phẳng nhưng cần 4 màu). Vậy bốn là con số chính xác cho mặt phẳng.

---

## 2. Vì sao tấn công trực tiếp thì khó

Có vô hạn bản đồ phẳng. Một chứng minh hoặc phải tìm ra lý do cấu trúc cho thấy bốn màu luôn đủ, hoặc phải đưa bức tranh vô hạn này về một tập **hữu hạn** các tình huống bao quát mọi khả năng.

Chứng minh của Appel–Haken (và các chứng minh sau đó) đi theo hướng thứ hai, nối tiếp những nỗ lực của Kempe ở thế kỷ XIX. Chứng minh Kempe công bố có lỗi; chính lỗi đó cho thế hệ sau thấy những phép rút gọn nào mong manh. Chứng minh thành công đã sửa và mở rộng đáng kể kỹ thuật cấu hình và discharging.

---

## 3. Phản ví dụ tối thiểu

Giả sử (để đi đến mâu thuẫn) có một đồ thị phẳng không tô được bằng 4 màu. Trong các phản ví dụ, chọn cái **tối thiểu**, thường là cái có ít đỉnh nhất. Phản ví dụ tối thiểu có một tính chất hữu ích: bản thân nó không tô được, nhưng mọi đồ thị phẳng nhỏ hơn nó *đều* tô được bằng 4 màu. Do đó, nếu ta chỉ ra một mảnh cục bộ có thể co lại hoặc tô lại bằng cách dùng màu của đồ thị nhỏ hơn, thì mảnh đó không thể xuất hiện trong phản ví dụ tối thiểu.

**Ví dụ nhỏ về tính rút gọn được:** Trong phản ví dụ tối thiểu $$G$$, không thể có đỉnh $$v$$ nào bậc $$\le 3$$. Vì sao? Nếu có đỉnh $$v$$ chỉ có nhiều nhất $$3$$ láng giềng, ta xóa tạm $$v$$ đi để được đồ thị $$G - v$$ nhỏ hơn; theo tính tối thiểu, $$G - v$$ tô được bằng 4 màu; bây giờ lắp $$v$$ trở lại, $$3$$ láng giềng của nó dùng nhiều nhất $$3$$ màu nên vẫn còn thừa ít nhất $$1$$ màu trống cho $$v$$ — suy ra $$G$$ tô được bằng 4 màu, mâu thuẫn! Như vậy cấu hình "đỉnh bậc $$\le 3$$" là **rút gọn được**. Tương tự, kỹ thuật đổi màu chuỗi Kempe dễ dàng loại luôn đỉnh bậc $$4$$. Mọi rắc rối dồn hết vào đỉnh bậc $$5$$ và các cụm xung quanh nó.

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

Discharging là một lập luận phân phối lại cục bộ, hữu hạn — bạn có thể hình dung nó như một **bài toán kế toán ngân sách**.

Từ công thức Euler $$V - E + F = 2$$ cho đồ thị phẳng đã tam giác hóa, ta dễ dàng biến đổi thành đẳng thức:

$$
\sum_{v \in V} (6 - \deg(v)) = 12 > 0.
$$

Hãy gán cho mỗi đỉnh $$v$$ một "số tiền" (hay **điện tích**) ban đầu bằng $$6 - \deg(v)$$. Khi đó:
- Đỉnh bậc $$5$$ có điện tích dương $$+1$$ (giàu).
- Đỉnh bậc $$6$$ có điện tích $$0$$ (hòa vốn).
- Đỉnh bậc $$7, 8, \ldots$$ có điện tích âm $$-1, -2, \ldots$$ (nợ).
- Nhưng **tổng điện tích toàn đồ thị luôn dương bằng $$+12$$**!

Tiếp theo, ta thiết kế các quy tắc chuyển điện tích cục bộ (ví dụ: các đỉnh bậc $$5$$ "chia bớt" một phần điện tích dương sang cho các láng giềng bậc lớn đang âm). Vì tổng điện tích toàn đồ thị được bảo toàn bằng $$+12 > 0$$, nên sau khi chia xong **chắc chắn vẫn phải còn ít nhất một đỉnh mang điện tích dương**. Bằng cách thiết kế luật chia khéo léo, ta chứng minh rằng bất kỳ đỉnh nào còn điện tích dương sau khi chia đều buộc phải nằm trong một cụm cục bộ thuộc danh sách $$\mathcal{U}$$!

Thiết kế các quy tắc discharging và danh sách cấu hình là công việc tổ hợp thủ công rất sâu. Việc kiểm tra các quy tắc có chạy đúng và mỗi cấu hình có rút gọn được hay không dẫn đến một khối lượng trường hợp lớn mà máy kiểm tra được: **1.936 cấu hình** trong chứng minh của Appel–Haken (1976), danh sách gọn hơn nhiều (**633 cấu hình**) trong chứng minh của Robertson–Sanders–Seymour–Thomas (1997), và cuối cùng là một chứng minh hình thức hoàn chỉnh trong **Coq** (Georges Gonthier và cộng sự, 2005).

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

- Nó không khẳng định mọi bản đồ trên mọi mặt đều tô được bằng 4 màu; số màu cần thiết thay đổi theo giống của mặt (công thức Heawood cho giống cao hơn — ví dụ trên bề mặt chiếc bánh donut/hình xuyến, có những bản đồ cần tới **7 màu**!).
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
