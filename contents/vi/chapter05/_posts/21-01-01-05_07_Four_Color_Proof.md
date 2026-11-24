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

**Mạch bài học:** Bản đồ kiến thức nền (đồ thị phẳng, đối ngẫu, công thức Euler, chứng minh hình thức) → Phát biểu và bẫy trực giác $$K_4/K_5$$ → Phản ví dụ tối thiểu và tập không tránh được → Khung giải thích chậm: tự tay chứng minh $$\sum(6-\deg(v))=12$$, kiểm tra trên tứ diện/bát diện và chuỗi Kempe 5 màu → Discharging và kiểm chứng trong Coq.

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

## Bản đồ kiến thức nền: Đồ thị phẳng, Sắc số và Chứng minh có máy tính hỗ trợ là gì?

Để người tốt nghiệp đại học nắm ngay bức tranh toàn cảnh trước khi bước vào kỹ thuật *discharging*, hãy xem ba trụ cột đứng sau Định lý Bốn Màu:

### 1. Đồ thị phẳng (Planar Graph), Đối ngẫu và Công thức Euler
Một đồ thị gọi là **phẳng** nếu vẽ được nó trên mặt giấy mà không có hai cạnh nào cắt chéo nhau. Mỗi bản đồ chính trị đều biến thành một đồ thị phẳng bằng phép **đối ngẫu (duality)**: đặt một đỉnh vào thủ đô mỗi nước và vẽ một cạnh nối hai nước có chung một đoạn biên giới. Khi đó, "tô màu bản đồ" trở thành "tô màu đỉnh đồ thị sao cho hai đỉnh kề nhau khác màu". Trái tim của mọi đồ thị phẳng liên thông là **công thức Euler**:

$$
V - E + F = 2,
$$

trong đó $$V$$ là số đỉnh, $$E$$ là số cạnh và $$F$$ là số miền (kể cả miền vô hạn bên ngoài). Chỉ từ một dòng đẳng thức này, ta suy ra mọi đồ thị phẳng đơn đều có ít nhất một đỉnh bậc $$\le 5$$.

### 2. Sắc số (Chromatic Number $$\chi(G)$$) và Lý thuyết rút gọn cấu hình
**Sắc số** $$\chi(G)$$ là số màu ít nhất cần để tô hợp lệ các đỉnh của đồ thị $$G$$. Ngoài toán thuần túy, tô màu đồ thị là mô hình chuẩn cho bài toán **phân bổ thanh ghi trong trình biên dịch (compiler register allocation)**, **xếp lịch thi không trùng môn**, và **phân bổ tần số trạm phát sóng di động** sao cho các trạm gần nhau không nhiễu sóng. Định lý Bốn Màu khẳng định mọi đồ thị phẳng có $$\chi(G) \le 4$$.

### 3. Chứng minh có máy tính hỗ trợ vs. Chứng minh hình thức (Coq)
Năm 1976, Appel–Haken viết chương trình kiểm tra 1.936 cấu hình, mở ra cuộc tranh luận triết học lớn: *nếu mã nguồn có bug thì sao?* Đến năm 2005, Georges Gonthier hình thức hóa trọn vẹn chứng minh trong trợ lý chứng minh **Coq**, nơi một lõi logic (*kernel*) nhỏ bé kiểm toán từng bước suy diễn từ tiên đề — đưa chứng minh Bốn Màu đạt chuẩn chặt chẽ bậc nhất.

---

## 1. Phát biểu, đồ thị đối ngẫu — và bẫy trực giác đời thường

### Từ câu đố bản đồ đến bẫy của Kempe

Hãy thử tự tay vẽ một bản đồ cần nhiều màu nhất có thể trên tờ giấy. Bạn đặt 3 nước đôi một tiếp giáp nhau (dễ, cần 3 màu). Bạn bao bọc chúng bằng nước thứ 4 chạm cả 3 nước kia (tạo thành đồ thị đầy đủ $$K_4$$ — cần đúng 4 màu). Bây giờ hãy thử thêm nước thứ 5 sao cho nó chạm *cả 4* nước cũ mà không nhảy qua biên giới hay đục hầm xuyên giấy: bạn sẽ bị nhốt ngay lập tức, vì đồ thị đầy đủ $$K_5$$ **không thể vẽ phẳng** trên tờ giấy!

Điều này sinh ra một trực giác rất hấp dẫn nhưng lại **sai**: nhiều người nghĩ *"không có 5 nước đôi một chạm nhau thì chắc chắn 4 màu là đủ"*. Thực tế, trong lý thuyết đồ thị tồn tại những đồ thị thậm chí không có hình tam giác ($$K_3$$) nào mà vẫn cần 4, 5 hay 100 màu! Bản đồ phẳng phức tạp hơn thế nhiều: các ràng buộc màu lan truyền dây chuyền từ đầu này sang đầu kia của bản đồ. Chính vì những chuỗi lan truyền màu (*chuỗi Kempe*) có thể đan chéo và vô hiệu hóa lẫn nhau nên chứng minh nổi tiếng năm 1879 của Kempe đã sụp đổ ở bước tưởng như hiển nhiên nhất.

### Phát biểu chuẩn

**Định lý Bốn Màu.** Các "nước" trên mọi bản đồ chính trị vẽ trên mặt phẳng (hoặc mặt cầu) có thể được tô bằng bốn màu sao cho hai nước kề nhau có màu khác nhau. Ở đây mỗi nước là một miền liên thông, và "kề nhau" nghĩa là có chung một đoạn biên có độ dài dương (không chỉ chung một điểm).

Theo ngôn ngữ đồ thị: mọi đồ thị phẳng đều **tô được bằng 4 màu**. Năm màu thì đủ theo định lý cổ điển của Heawood (1890). Ba màu **không** đủ (vì $$K_4$$ là đồ thị phẳng nhưng cần 4 màu). Vậy bốn là con số chính xác cho mặt phẳng.

---

## 2. Vì sao tấn công trực tiếp thì khó

Có vô hạn bản đồ phẳng. Một chứng minh hoặc phải tìm ra lý do cấu trúc cho thấy bốn màu luôn đủ, hoặc phải đưa bức tranh vô hạn này về một tập **hữu hạn** các tình huống bao quát mọi khả năng.

Chứng minh của Appel–Haken (và các chứng minh sau đó) đi theo hướng thứ hai, nối tiếp những nỗ lực của Kempe ở thế kỷ XIX. Chứng minh Kempe công bố có lỗi; chính lỗi đó cho thế hệ sau thấy những phép rút gọn nào mong manh. Chứng minh thành công đã sửa và mở rộng đáng kể kỹ thuật cấu hình và discharging.

---

## 3. Phản ví dụ tối thiểu và Tập không tránh được

Giả sử (để đi đến mâu thuẫn) có một đồ thị phẳng không tô được bằng 4 màu. Trong các phản ví dụ, chọn cái **tối thiểu** $$G$$ (ít đỉnh nhất): bản thân $$G$$ không tô được bằng 4 màu, nhưng mọi đồ thị phẳng nhỏ hơn nó *đều* tô được bằng 4 màu.

- **Cấu hình rút gọn được:** Một mảnh cục bộ không thể xuất hiện trong phản ví dụ tối thiểu $$G$$, vì sự có mặt của nó cho phép ta dựng cách tô 4 màu cho $$G$$ từ cách tô 4 màu của đồ thị nhỏ hơn.
- **Tập không tránh được:** Một danh sách hữu hạn $$\mathcal{U} = \{C_1, \ldots, C_N\}$$ sao cho **mọi** phản ví dụ tối thiểu bắt buộc phải chứa ít nhất một $$C_i \in \mathcal{U}$$.

Nếu chứng minh được **mọi** cấu hình trong tập không tránh được $$\mathcal{U}$$ đều rút gọn được, thì không thể có phản ví dụ tối thiểu nào tồn tại — định lý được chứng minh!

---

## 4. Khung giải thích: tự tay suy ra phương trình "điện tích" và chạy thử chuỗi Kempe (nên đọc chậm)

Để không thấy *discharging* hay *chuỗi Kempe* như những thuật ngữ trừu tượng, hãy cầm bút kiểm tra từng bước trên các khối hình cụ thể:

### Bước 1: Tự tay chứng minh đẳng thức "kế toán điện tích" $$\sum (6 - \deg(v)) = 12$$
Xét một đồ thị phẳng đã **tam giác hóa** (thêm cạnh đến khi mọi miền, kể cả miền ngoài, đều là tam giác — việc thêm cạnh chỉ làm bài toán tô màu khó hơn, nên nếu đồ thị tam giác hóa tô được 4 màu thì đồ thị gốc cũng tô được).
1. Vì mỗi mặt tam giác có $$3$$ cạnh và mỗi cạnh nằm giữa đúng $$2$$ mặt, ta có $$3F = 2E \implies F = \frac{2}{3}E$$.
2. Thay $$F = \frac{2}{3}E$$ vào công thức Euler $$V - E + F = 2$$:
   $$
   V - E + \frac{2}{3}E = 2 \;\implies\; V - \frac{1}{3}E = 2 \;\implies\; 6V - 2E = 12.
   $$
3. Dùng Bổ đề bắt tay $$2E = \sum_{v \in V} \deg(v)$$, ta thu được ngay lập tức:
   $$
   \sum_{v \in V} \bigl(6 - \deg(v)\bigr) = 12.
   $$

**Kiểm tra bằng tay trên hai khối đa diện quen thuộc:**

| Đồ thị phẳng tam giác hóa | $$V$$ | $$E$$ | $$F$$ | Kiểm tra $$V - E + F$$ | Bậc mỗi đỉnh | Tổng điện tích $$\sum (6 - \deg(v))$$ |
|---------------------------|-------|-------|-------|------------------------|--------------|---------------------------------------|
| **Tứ diện ($$K_4$$)** | $$4$$ | $$6$$ | $$4$$ | $$4 - 6 + 4 = 2$$ | Mọi đỉnh bậc $$3$$ | $$4 \times (6 - 3) = \mathbf{12}$$ |
| **Bát diện đều** | $$6$$ | $$12$$ | $$8$$ | $$6 - 12 + 8 = 2$$ | Mọi đỉnh bậc $$4$$ | $$6 \times (6 - 4) = \mathbf{12}$$ |
| **Nhị thập diện đều** | $$12$$ | $$30$$ | $$20$$ | $$12 - 30 + 20 = 2$$ | Mọi đỉnh bậc $$5$$ | $$12 \times (6 - 5) = \mathbf{12}$$ |

Vì tổng điện tích luôn bằng **$$+12 > 0$$**, nên **chắc chắn phải có ít nhất một đỉnh bậc $$\le 5$$** (nếu mọi đỉnh đều có bậc $$\ge 6$$ thì tổng sẽ $$\le 0$$, mâu thuẫn!).

### Bước 2: Thử rút gọn đỉnh bậc $$\le 3$$ và chuỗi Kempe cho Định lý Năm Màu
- **Đỉnh bậc $$\le 3$$ (cho 4 màu):** Nếu $$G$$ có đỉnh $$v$$ bậc $$\le 3$$, xóa tạm $$v$$ để được $$G - v$$ (tô được bằng 4 màu). Lắp $$v$$ lại: $$3$$ láng giềng của $$v$$ dùng tối đa $$3$$ màu, nên chắc chắn còn trống ít nhất $$1$$ màu cho $$v$$! Vậy đỉnh bậc $$\le 3$$ rút gọn được ngay.
- **Đỉnh bậc $$5$$ (chứng minh Năm Màu bằng tay):** Giả sử có 5 màu (Đỏ, Xanh dương, Xanh lá, Vàng, Tím) và đỉnh $$v$$ có 5 láng giềng xếp vòng tròn theo chiều kim đồng hồ $$v_1$$ (Đỏ), $$v_2$$ (Xanh dương), $$v_3$$ (Xanh lá), $$v_4$$ (Vàng), $$v_5$$ (Tím).
  - Xét tất cả các đỉnh chỉ mang màu **Đỏ hoặc Xanh lá** nối thành mạng liên thông bắt đầu từ $$v_1$$ (gọi là **chuỗi Kempe Đỏ–Xanh lá**).
  - *Trường hợp A:* Chuỗi này **không chạm tới $$v_3$$**. Ta chỉ việc đảo toàn bộ màu Đỏ $$\leftrightarrow$$ Xanh lá trên chuỗi đó: $$v_1$$ chuyển thành Xanh lá, các láng giềng còn lại giữ nguyên → màu Đỏ trống ra cho $$v$$!
  - *Trường hợp B:* Chuỗi này **nối liền $$v_1$$ với $$v_3$$**. Vì đồ thị phẳng, chuỗi Đỏ–Xanh lá cộng với đường $$v_1 - v - v_3$$ tạo thành một **bức tường khép kín** nhốt $$v_2$$ (Xanh dương) ở bên trong và $$v_4$$ (Vàng) ở bên ngoài! Do đó chuỗi Kempe **Xanh dương–Vàng** xuất phát từ $$v_2$$ **không thể nào vượt tường sang tới $$v_4$$** — ta đảo Xanh dương $$\leftrightarrow$$ Vàng quanh $$v_2$$ để giải phóng màu Xanh dương cho $$v$$!

### Bước 3: Vì sao mẹo đó gãy khi chỉ có 4 màu — và Discharging ra đời
Khi chỉ có 4 màu, 5 láng giềng của $$v$$ phải lặp lại ít nhất một cặp màu (chẳng hạn $$v_1, v_3$$ cùng màu Đỏ, còn $$v_2, v_4, v_5$$ mang 3 màu kia). Nếu ta cần thực hiện *hai* phép đổi chuỗi Kempe đồng thời, chuỗi thứ nhất có thể làm hỏng cấu trúc chặn của chuỗi thứ hai (chính là lỗ hổng 11 năm của Kempe!). Vì đỉnh bậc $$5$$ đơn lẻ không tự rút gọn được cho 4 màu, Appel và Haken phải dùng **discharging** (chia bớt điện tích $$+1$$ của đỉnh bậc $$5$$ sang các đỉnh bậc $$\ge 7$$ đang âm, giữ tổng bằng $$+12$$) để ép đồ thị phải chứa một trong **1.936 cụm cấu hình lớn hơn** (như hai đỉnh bậc 5 kề nhau kèm vòng bao quanh), rồi dùng máy tính chứng minh từng cụm đều rút gọn được!

---

## 5. Discharging (cỗ máy do con người thiết kế)

Thiết kế các quy tắc discharging và danh sách cấu hình là công việc tổ hợp thủ công rất sâu. Việc kiểm tra các quy tắc có chạy đúng và mỗi cấu hình có rút gọn được hay không dẫn đến một khối lượng trường hợp lớn mà máy kiểm tra được: **1.936 cấu hình** trong chứng minh của Appel–Haken (1976), danh sách gọn hơn nhiều (**633 cấu hình**) trong chứng minh của Robertson–Sanders–Seymour–Thomas (1997), và cuối cùng là một chứng minh hình thức hoàn chỉnh trong **Coq** (Georges Gonthier và cộng sự, 2005).

---

## 6. Ý tưởng chứng minh trong một trang

1. Viết lại bài toán tô màu bản đồ thành bài toán tô 4 màu các đỉnh của đồ thị phẳng.
2. Giả sử có phản ví dụ tối thiểu $$G$$.
3. Đưa ra một tập không tránh được hữu hạn $$\mathcal{U}$$ (bằng discharging và công thức Euler $$\sum(6-\deg(v)) = 12$$).
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
