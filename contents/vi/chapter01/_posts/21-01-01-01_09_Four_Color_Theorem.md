---
layout: post
title: "Định lý Bốn Màu"
chapter: '01'
order: 9
owner: Nguyen Le Linh
lang: vi
categories:
- chapter01
---

> **Lộ trình học B — Bốn màu (2 bước)**  
> **1. Bạn đang ở đây:** Chương 1, Định lý Bốn Màu: lý thuyết và cách người ta chấp nhận chứng minh  
> **2. Tiếp theo:** [Bài thực hành tô màu, Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/): đồ thị đối ngẫu, Heawood, bài viết  
> *Thời gian gợi ý:* khoảng 2 giờ cho bài này, 1–2 giờ cho bài thực hành.

Tháng 10 năm 1852, chàng sinh viên vừa tốt nghiệp Francis Guthrie ngồi tô màu tấm bản đồ các hạt của nước Anh sao cho không có hai hạt chung biên giới nào trùng màu. Càng tô, anh càng ngạc nhiên nhận ra mình chưa bao giờ cần quá **bốn cây bút màu**. Anh mang thắc mắc ấy hỏi người em trai, người em hỏi nhà toán học Augustus De Morgan, và câu hỏi nhỏ tưởng như trò tiêu khiển của người vẽ bản đồ nhanh chóng lan khắp giới toán học châu Âu — khởi đầu cho một cuộc rượt đuổi kéo dài đúng **124 năm**.

Lịch sử của **Định lý Bốn Màu (4CT)** đầy những cú ngoặt kịch tính: năm 1879, luật sư kiêm nhà toán học nghiệp dư Alfred Kempe công bố một "chứng minh" được cả thế giới tán thưởng suốt 11 năm trời, cho đến khi Percy Heawood chỉ ra một lỗ hổng ẩn sâu mà không ai vá nổi bằng ý tưởng cũ (chỉ cứu lại được Định lý Năm Màu). Mãi đến năm **1976**, Kenneth Appel và Wolfgang Haken mới chinh phục được con số bốn — nhưng bằng một cách chưa từng có trong lịch sử: họ phải chạy hơn **1.200 giờ trên siêu máy tính IBM** để kiểm tra hàng nghìn cấu hình tổ hợp!

Khác với [giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) hay [Kakeya trong nhiều chiều]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/), 4CT **đã được giải**. Nhưng chính cách giải ấy đã làm bùng nổ một cuộc tranh luận triết học lớn về bản chất của chứng minh toán học: *liệu một định lý mà không một con người nào có thể tự tay kiểm tra hết mọi bước trên giấy có thực sự là một chứng minh?* Các bản rút gọn sau đó (Robertson–Sanders–Seymour–Thomas, 1997) và bản hình thức hóa hoàn toàn bằng trợ lý chứng minh **Coq** của Georges Gonthier (2005) đã khép lại nghi ngờ về lỗi lập trình, đồng thời mở ra kỷ nguyên mới của chứng minh có máy tính hỗ trợ.

**Mạch bài học:** Kiến thức cần nhớ → bài toán tô bản đồ & đồ thị đối ngẫu (ví dụ $$K_4, K_5, K_7$$) → định lý năm màu & chuỗi Kempe → ví dụ kế toán phóng điện trên khối 20 mặt đều & khung giải thích 4 bước của chứng minh 4CT → kiểm chứng hình thức Coq → định lý Heawood.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu 4CT bằng ngôn ngữ bản đồ và ngôn ngữ đồ thị (sắc số $$\chi(G)\le 4$$ với mọi đồ thị phẳng hữu hạn $$G$$).
- Giải thích cách chuyển sang **đồ thị đối ngẫu**: miền ứng với đỉnh, biên chung ứng với cạnh.
- Phác thảo vì sao **năm** màu dễ hơn bốn màu (Heawood: quy nạp, đỉnh bậc $$\le 5$$, chuỗi Kempe).
- Mô tả ngắn gọn **tập không tránh được** (unavoidable set) và cấu hình **khả quy** (reducible).
- Thảo luận chứng minh có máy tính hỗ trợ như một vấn đề vừa triết học *vừa* thực hành (chứng minh con người đọc kiểm được, kiểm chứng hình thức).
- So sánh mặt phẳng với công thức **Heawood** cho các mặt có giống $$g\ge 1$$.
- Liên hệ với [bài thực hành tô màu ở Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/).

**Kiến thức cần có.** Đồ thị gồm đỉnh và cạnh; hình dung được cách vẽ trên mặt phẳng mà các cạnh không cắt nhau. Không cần lý thuyết đồ thị nâng cao.

**Kết nối trong khóa học.** Bài này đặt câu hỏi sâu sắc "chứng minh là gì?" khi đặt cạnh Kakeya (một bài toán giải tích), [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) (độ khó tính toán, khác với việc máy tính hỗ trợ chứng minh) và [bài thực hành tô màu bản đồ]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/).

---

## Kiến thức cần nhớ: Lý thuyết đồ thị, Tôpô bề mặt và Kiểm chứng hình thức là gì?

Đằng sau câu hỏi tô bản đồ có ba trụ cột toán học và tin học cực kỳ hữu dụng mà bất kỳ người học đại học nào cũng nên biết:

### 1. Lý thuyết đồ thị & Đồ thị phẳng (Graph Theory)
Thay vì quan tâm một quốc gia có hình thù méo mó hay diện tích bao nhiêu km², lý thuyết đồ thị lược bỏ hết chi tiết thừa và chỉ giữ lại **đỉnh** (đối tượng) và **cạnh** (mối quan hệ kề nhau). **Đồ thị phẳng** (*planar graph*) là đồ thị có thể vẽ lên mặt giấy sao cho không có hai cạnh nào cắt nhau. Công cụ nền tảng nhất của đồ thị phẳng là **công thức Euler** $$v - e + f = 2$$ (số đỉnh trừ số cạnh cộng số mặt luôn bằng 2).

### 2. Tôpô bề mặt & Giống $$g$$ (Surface Topology)
Hình dạng không gian vẽ bản đồ quyết định số màu tối đa! Trên mặt có $$g$$ "lỗ thủng" (gọi là **giống** $$g$$), công thức Euler tổng quát trở thành $$v - e + f = 2 - 2g$$. Mặt phẳng và mặt cầu ($$g = 0$$) khác hẳn mặt xuyến hình bánh donut ($$g = 1$$) — trên mặt bánh donut, ta có thể vẽ 7 quốc gia mà nước nào cũng tiếp giáp với cả 6 nước còn lại!

### 3. Kiểm chứng hình thức & Trợ lý chứng minh (Formal Verification)
Các trợ lý chứng minh như **Coq** hay **Lean** cho phép viết một định lý và toàn bộ chứng minh của nó thành mã logic chặt chẽ; một chương trình lõi nhỏ gọn (*kernel*) sẽ kiểm tra máy móc từng bước suy luận về tận các tiên đề cơ bản để bảo đảm không sót bất kỳ lỗ hổng nào.

**Ứng dụng thực tiễn:** Bài toán tô màu đồ thị xuất hiện hằng ngày trong **cấp phát thanh ghi (register allocation)** của trình biên dịch (mỗi biến là một đỉnh, hai biến sống cùng lúc được nối cạnh, mỗi màu là một thanh ghi CPU), **phân bổ tần số trạm phát sóng di động** (hai trạm gần nhau không được trùng tần số), và **xếp lịch thi đại học** (hai môn có chung sinh viên không được thi cùng giờ).

---

## 1. Câu hỏi của người vẽ bản đồ

Từ giữa thế kỷ 19 (Guthrie, De Morgan, Cayley, …), người ta đã hỏi: cần bao nhiêu màu để tô một bản đồ hành chính sao cho các nước láng giềng có chung đường biên luôn có màu khác nhau?

- **Hai màu** không đủ ngay khi có một vòng lẻ miền kề nhau (ví dụ 3 miền đôi một tiếp giáp).  
- **Ba màu** không đủ cho nhiều bản đồ phẳng đơn giản (ví dụ một nước ở giữa bị bao quanh bởi một vòng 3 nước hoặc 5 nước láng giềng kề nhau: 3 nước xung quanh đã tốn 3 màu nên nước ở giữa buộc phải dùng màu thứ 4!).  
- **Bốn màu** được dự đoán là luôn đủ.  
- **Năm màu** đã được chứng minh là đủ bằng lập luận cổ điển ngắn gọn (định lý năm màu của Heawood).

Câu hỏi nghe như chuyện vẽ bản đồ, nhưng khi phát biểu bằng đồ thị, nó trở thành một định lý sâu sắc về cấu trúc của các đồ thị thưa vẽ được trên mặt phẳng.

![Miền kề]({{ site.baseurl }}/img/chapter_img/fourcolor_map_k4.svg)

*Hình. Phác thảo các miền kề nhau, cho thấy vì sao cần nhiều màu.*

---

## 2. Từ bản đồ đến đồ thị phẳng

Ứng với mỗi miền, đặt một **đỉnh**; nối hai đỉnh bằng một **cạnh** khi hai miền có chung một đoạn biên có độ dài dương (không tính trường hợp chỉ chạm nhau tại đúng một góc nhọn như bốn bang Four Corners ở Mỹ). Ta thu được một **đồ thị phẳng** (vẽ được mà các cạnh không cắt nhau, với giả thiết bản đồ đủ "đẹp").

Tô màu các miền tương đương hoàn toàn với tô màu các đỉnh sao cho hai đỉnh nối bởi một cạnh luôn khác màu.

![Dual]({{ site.baseurl }}/img/chapter_img/fourcolor_graph_dual.svg)

*Hình. Đồ thị đối ngẫu: đỉnh ứng với miền, cạnh ứng với biên chung.*

**Dạng đồ thị của 4CT.** Mọi đồ thị phẳng hữu hạn $$G$$ đều thỏa mãn $$\chi(G)\le 4$$, trong đó **sắc số** $$\chi(G)$$ là số màu tối thiểu cần để tô hợp lệ các đỉnh.

### Ví dụ làm từng bước 1: Từ công thức Euler đến giới hạn cạnh trên mặt phẳng ($$K_4, K_5$$) và mặt xuyến ($$K_7$$)

Với đồ thị phẳng đơn liên thông có $$v \ge 3$$ đỉnh, mỗi mặt (kể cả mặt vô hạn bên ngoài) được bao bởi ít nhất 3 cạnh, và mỗi cạnh làm biên cho tối đa 2 mặt, nên $$3f \le 2e \implies f \le \frac{2}{3}e$$. Thay vào công thức Euler $$v - e + f = 2$$:

$$
2 = v - e + f \le v - e + \frac{2}{3}e = v - \frac{1}{3}e \quad\Longrightarrow\quad e \le 3v - 6.
$$

Hãy kiểm tra ngay trên 3 đồ thị đầy đủ (mọi cặp đỉnh đều nối nhau):
1. **$$K_4$$ trên mặt phẳng:** $$v = 4,\, e = \binom{4}{2} = 6$$. Kiểm tra: $$6 \le 3(4) - 6 = 6$$ (vừa khít!). Ta vẽ được $$K_4$$ phẳng và cần đúng 4 màu.
2. **$$K_5$$ trên mặt phẳng:** $$v = 5,\, e = \binom{5}{2} = 10$$. Kiểm tra: $$10 > 3(5) - 6 = 9$$ → **bất khả thi!** Do đó không bao giờ có 5 nước trên mặt phẳng mà nước nào cũng tiếp giáp cả 4 nước kia.
3. **$$K_7$$ trên mặt xuyến ($$g = 1$$):** Công thức Euler đổi thành $$v - e + f = 2 - 2(1) = 0 \implies e \le 3v$$! Thử với $$K_7$$ ($$v = 7,\, e = \binom{7}{2} = 21$$): $$21 \le 3(7) = 21$$ — vừa khít! Thực sự vẽ được $$K_7$$ không cắt cạnh trên bánh donut, nên mặt xuyến cần tới 7 màu!

Ngoài ra, trên mặt phẳng, vì tổng bậc bằng $$2e$$ nên **bậc trung bình** là $$\frac{2e}{v} \le 6 - \frac{12}{v} < 6$$! Một dãy số có trung bình nhỏ hơn 6 thì **chắc chắn có ít nhất một đỉnh bậc $$\le 5$$**. Kết quả nhỏ bé này chính là viên gạch khởi đầu cho cả chứng minh năm màu lẫn bốn màu.

**Lưu ý về mô hình.** 4CT ở dạng chuẩn giả thiết các miền là liên thông (mỗi nước là một mảnh liền). Nếu một nước **không liên thông** (gồm nhiều mảnh rời nhau phải tô cùng màu) thì bài toán thay đổi hẳn và có thể cần nhiều màu tùy ý.

---

## 3. Vì sao năm màu dễ hơn bốn màu

**Định lý năm màu** có một chứng minh cổ điển chỉ dài chưa tới một trang giấy (quy nạp theo số đỉnh $$v$$):

1. Mọi đồ thị phẳng đơn đều có một đỉnh $$u$$ bậc $$\le 5$$ (nhờ $$e\le 3v-6$$ ở trên).  
2. Xóa đỉnh $$u$$ đi; theo giả thiết quy nạp, phần còn lại $$G-u$$ tô được bằng 5 màu.  
3. Nếu các hàng xóm của $$u$$ dùng chưa hết 5 màu, ta chỉ việc lấy màu còn dư tô cho $$u$$ là xong!  
4. Trường hợp khó duy nhất: $$u$$ có đúng 5 hàng xóm $$v_1, v_2, v_3, v_4, v_5$$ (xếp theo vòng tròn quanh $$u$$) mang đủ 5 màu khác nhau, giả sử lần lượt là Đỏ, Vàng, Xanh dương, Lục, Tím. Lúc này ta dùng mẹo **chuỗi Kempe**: xét tất cả các đỉnh chỉ mang màu Đỏ hoặc Xanh dương liên thông với $$v_1$$ (Đỏ).
   - Nếu chuỗi Đỏ–Xanh dương này *không* chạm tới $$v_3$$ (Xanh dương), ta cứ đảo màu Đỏ $$\leftrightarrow$$ Xanh dương trên toàn bộ thành phần liên thông đó: $$v_1$$ biến thành Xanh dương, giải phóng màu Đỏ cho $$u$$!
   - Nếu chuỗi Đỏ–Xanh dương *có* nối từ $$v_1$$ tới $$v_3$$, thì vì đồ thị là **phẳng**, sợi dây Đỏ–Xanh dương cùng với $$u$$ tạo thành một bức tường khép kín nhốt $$v_2$$ (Vàng) bên trong và $$v_4$$ (Lục) bên ngoài! Do đó chuỗi Vàng–Lục xuất phát từ $$v_2$$ *không bao giờ* chạm được tới $$v_4$$ — ta đảo màu Vàng $$\leftrightarrow$$ Lục quanh $$v_2$$ là giải phóng ngay màu Vàng cho $$u$$!

**Chỗ kẹt khi hạ xuống 4 màu:** Kempe (1879) thử áp dụng đúng mẹo đảo hai chuỗi Kempe khi $$u$$ có 5 hàng xóm mang 4 màu (ví dụ một màu lặp lại hai lần). Suốt 11 năm không ai nhận ra lỗi, cho đến năm 1890 Heawood vẽ ra một đồ thị phản ví dụ cho thấy khi đảo *đồng thời* hai chuỗi Kempe trong trường hợp 4 màu, hai chuỗi đó có thể cắt chéo và phá hỏng màu của nhau! Khoảng cách từ 5 xuống 4 hóa ra sâu tới cả một thế kỷ nghiên cứu.

Tóm tắt dễ nhớ: **năm màu = quy nạp + công thức Euler + chuỗi Kempe**; **bốn màu = cấu trúc sâu + hàng trăm cấu hình cục bộ**.

---

## 4. Phản ví dụ nhỏ nhất và chiến lược của Appel–Haken

### Ví dụ làm từng bước 2: Thử phép kế toán "phóng điện" (Discharging) trên khối 20 mặt đều

Với mọi đồ thị phẳng tam giác phân (mọi mặt đều là tam giác, $$3f = 2e$$), thay $$f = \frac{2}{3}e$$ vào $$v - e + f = 2$$ ta có $$6v - 2e = 12$$. Vì $$2e = \sum_{v} \deg(v)$$, ta thu được đẳng thức kế toán vàng:

$$
\sum_{v} \bigl(6 - \deg(v)\bigr) = 12.
$$

Hãy kiểm tra ngay trên **khối 20 mặt đều (Icosahedron)**: có $$v = 12$$ đỉnh, $$e = 30$$ cạnh, $$f = 20$$ mặt tam giác, và mọi đỉnh đều có bậc $$\deg(v) = 5$$.
- Kiểm tra công thức Euler: $$12 - 30 + 20 = 2$$ ✓.
- Gán cho mỗi đỉnh "điện tích" ban đầu $$q(v) = 6 - \deg(v)$$: mỗi đỉnh bậc 5 nhận $$+1$$, tổng điện tích toàn đồ thị là $$12 \times (+1) = \mathbf{+12}$$!

Bây giờ hãy tưởng tượng một phản ví dụ nhỏ nhất $$G$$ có hàng triệu đỉnh (bậc tối thiểu 5): đỉnh bậc 5 có điện tích $$+1$$ ("người giàu"), đỉnh bậc 6 hòa vốn ($$0$$), đỉnh bậc 7, 8, ... có điện tích $$-1, -2, \ldots$$ ("người nợ"). Khi ta áp dụng các quy tắc **chuyển điện tích cục bộ** từ đỉnh bậc 5 sang các hàng xóm bậc $$\ge 7$$, tổng điện tích toàn đồ thị **bảo toàn và vẫn bằng đúng $$+12 > 0$$**! Do đó *bắt buộc phải tồn tại ít nhất một đỉnh có điện tích cuối cùng dương* — và để điều đó xảy ra, lân cận của đỉnh ấy phải rơi vào một trong các cấu hình của danh sách hữu hạn $$\mathcal{U}$$!

### Giải thích: Chuỗi logic 4 bước của chứng minh Định lý Bốn Màu

Nhiều người tưởng máy tính "thử tô vài tỷ bản đồ rồi kết luận 4CT đúng". Thực tế chứng minh 4CT là một lập luận phản chứng chặt chẽ gồm đúng 4 bước:

#### Bước 1: Giả sử tồn tại một "phản ví dụ nhỏ nhất" $$G$$
Giả sử có đồ thị phẳng không tô được bằng 4 màu, chọn đồ thị $$G$$ có **số đỉnh ít nhất**. Khi đó *mọi* đồ thị phẳng nhỏ hơn $$G$$ đều tô được bằng 4 màu, và ta dễ dàng rút gọn để $$G$$ là đồ thị tam giác phân có mọi đỉnh bậc $$\ge 5$$.

#### Bước 2: Dùng phương pháp phóng điện tìm "tập không tránh được" $$\mathcal{U}$$ (con người thiết kế)
Bằng quy tắc chuyển điện tích như ví dụ trên, con người chứng minh bằng tay rằng *mọi* đồ thị phẳng tam giác phân bậc tối thiểu 5 đều **bắt buộc** chứa ít nhất một cấu hình cục bộ nằm trong một danh sách hữu hạn $$\mathcal{U}$$ (Appel–Haken 1976: khoảng 1.500–1.900 cấu hình; RSST 1997 rút gọn xuống đúng **633 cấu hình**).

#### Bước 3: Dùng máy tính chứng minh mọi cấu hình trong $$\mathcal{U}$$ đều "khả quy"
Một cấu hình $$C$$ là **khả quy (reducible)** nếu mọi cách tô 4 màu cho phần ngoài $$G - C$$ đều kéo dài được (có thể sau khi đảo chuỗi Kempe) thành cách tô 4 màu cho cả $$G$$ — đồng nghĩa $$C$$ **không thể** xuất hiện trong phản ví dụ nhỏ nhất $$G$$! Vì mỗi cấu hình có vòng biên từ 10 đến 14 đỉnh với hàng chục nghìn cách tô vòng biên, máy tính chạy thuật toán kiểm tra *cạn kiệt 100%* toàn bộ 633 cấu hình để xác nhận tất cả đều khả quy.

#### Bước 4: Mâu thuẫn khép lại chứng minh (và khóa chặt bằng Coq)
Phản ví dụ nhỏ nhất $$G$$ vừa *phải chứa* một $$C \in \mathcal{U}$$ (Bước 2), lại vừa *không được phép chứa* bất kỳ $$C \in \mathcal{U}$$ nào (Bước 3) → **mâu thuẫn!** Vậy không có phản ví dụ nào tồn tại. Năm 2005, Georges Gonthier hình thức hóa toàn bộ 4 bước này trong trợ lý chứng minh **Coq**, loại bỏ hoàn toàn nguy cơ lỗi lập trình.

![Pipeline]({{ site.baseurl }}/img/chapter_img/fourcolor_proof_pipeline.svg)

*Hình. Tập không tránh được + kiểm tra tính khả quy ⇒ không có phản ví dụ nhỏ nhất.*

---

## 5. Chứng minh gọn hơn, nhưng vẫn kiểm tra bằng máy

Các công trình sau làm chứng minh chặt chẽ và sáng sủa hơn rất nhiều, nhưng vẫn chưa ai tìm được một chứng minh tay ngắn gọn không cần máy tính. **Robertson, Sanders, Seymour và Thomas (RSST, 1997)** thu gọn tập không tránh được xuống chỉ còn **633 cấu hình** với 32 quy tắc phóng điện trong sáng hơn hẳn, nhưng vẫn dùng máy tính kiểm tra tính khả quy.

Bước ngoặt về độ tin cậy đến vào năm **2005**, khi **Georges Gonthier** (Microsoft Research) hình thức hóa *toàn bộ* chứng minh RSST trong trợ lý chứng minh **Coq**. Nhờ đó, câu hỏi "lỡ chương trình năm 1976 có lỗi code ẩn thì sao?" đã được giải tỏa: toàn bộ suy luận từ tiên đề lý thuyết đồ thị đến 633 cấu hình đều được kiểm tra máy móc bởi lõi (kernel) nhỏ gọn, đáng tin cậy của Coq.

Cộng đồng toán học đã thống nhất: **4CT là một định lý đã được chứng minh hoàn chỉnh**.

---

## 6. "Có máy tính hỗ trợ" ở đây nghĩa là gì

Điều quan trọng là phân biệt rõ với mô phỏng Monte Carlo hay chuyện "máy tính thử vài triệu bản đồ ngẫu nhiên rồi kết luận".

Theo cách làm của Appel–Haken và RSST:

- có một **danh sách hữu hạn các trường hợp tổ hợp**, xuất phát từ phương pháp phóng điện do **con người** thiết kế;  
- mỗi trường hợp là một bài toán chính xác về việc mở rộng cách tô màu (tính khả quy) trên một đồ thị hữu hạn;  
- máy tính liệt kê và kiểm tra cạn kiệt mọi khả năng của từng cấu hình, vì số trường hợp quá lớn để con người kiểm tay không sai sót;  
- logic tổng thể (vì sao danh sách là không tránh được; vì sao tính khả quy dẫn đến mâu thuẫn) là lập luận toán học thuần túy của con người.

Một số câu hỏi triết học vẫn thường được thảo luận:

- Một chứng minh có **nhất thiết** phải để một người đọc và kiểm tra được hết bằng mắt trong thời gian hợp lý không?  
- Nếu trợ lý chứng minh như Coq đã kiểm chứng bản hình thức hóa, liệu độ tin cậy có thậm chí còn cao hơn một bài báo 300 trang chỉ do vài người phản biện đọc tay?  
- Ta có thỏa mãn với *việc biết chắc chắn định lý đúng*, hay vẫn khao khát tìm một lý do khái niệm ngắn gọn giải thích "tại sao lại là số 4"?

Về mặt toán học, 4CT được chấp nhận hoàn toàn. Về mặt lịch sử, nó là cột mốc mở đường cho kỷ nguyên **kiểm chứng hình thức** (như dự án kiểm chứng giả thuyết Kepler bằng HOL Light/Isabelle hay cộng đồng Lean hiện nay). So với [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): ở đó máy tính là *đối tượng* của câu hỏi; còn ở 4CT, máy tính là *công cụ kiểm tra* trong một chứng minh hữu hạn.

---

## 7. Ra ngoài mặt phẳng: định lý tô màu Heawood

Mặt phẳng (và mặt cầu, giống $$g=0$$) hóa ra lại là trường hợp *khó nhất*! Trên các mặt có giống $$g\ge 1$$ (có $$g$$ lỗ thủng), **số Heawood**

$$
H(g)=\left\lfloor\frac{7+\sqrt{1+48g}}{2}\right\rfloor
$$

cho biết chính xác (theo định lý Ringel–Youngs hoàn tất năm 1968) sắc số lớn nhất của mọi đồ thị vẽ được trên mặt đó:
- Với **mặt xuyến** (hình bánh donut, $$g=1$$): $$H(1) = \lfloor (7 + \sqrt{49})/2 \rfloor = 7$$. Bảy màu là chặn chặt: có bản đồ trên mặt xuyến gồm 7 vùng mà vùng nào cũng kề với cả 6 vùng còn lại, và 7 màu luôn đủ!
- Với mặt có hai lỗ thủng ($$g=2$$): $$H(2) = \lfloor (7 + \sqrt{97})/2 \rfloor = 8$$ màu.

Trớ trêu thay, thay $$g=0$$ vào công thức Heawood cũng ra đúng số 4, nhưng chứng minh của Ringel–Youngs cho mọi $$g \ge 1$$ lại hoàn thành *trước* 4CT tận 8 năm, còn trường hợp $$g=0$$ trên mặt phẳng lại đòi hỏi toàn bộ bộ máy khổng lồ của 4CT!

![Heawood]({{ site.baseurl }}/img/chapter_img/fourcolor_heawood.svg)

*Hình. Số màu cần dùng tăng theo giống của mặt.*

Điểm cần chú ý: **tính phẳng** là một ràng buộc hình học mạnh, kéo số màu xuống còn bốn, trong khi chỉ thêm một "quai" (mặt xuyến) đã đẩy chặn chặt lên bảy. Bài thực hành ở Chương 7 khuyến khích thử với đồ thị đối ngẫu, các bản đồ nhỏ buộc phải dùng ba hoặc bốn màu, và công thức Heawood trên các mặt đơn giản.

**Miền không liên thông.** Nếu một "nước" gồm nhiều mảnh rời nhau phải tô cùng một màu, bài toán sẽ khác: có thể dựng bản đồ cần nhiều màu tùy ý. 4CT dạng chuẩn giả thiết các miền liên thông (hoặc xử lý các mảnh một cách cẩn thận). Khi tô màu, luôn nói rõ mô hình đang dùng.

---

## 8. Vì sao 4CT quan trọng với toán học

Ngoài việc giải quyết một giả thuyết nổi tiếng hơn một thế kỷ, 4CT còn:

- thúc đẩy **phương pháp phóng điện** và cách nhìn cấu trúc sâu sắc về đồ thị phẳng;  
- buộc cộng đồng phải xác lập các chuẩn mực cho **toán học có kiểm tra bằng máy** và kiểm chứng hình thức;  
- là "phòng thí nghiệm" suốt một thế kỷ cho các ý tưởng đổi màu, tính khả quy và tập không tránh được;  
- là ví dụ đối lập rất hay với các bài toán **còn mở** trong giải tích và số học (RH, Kakeya nhiều chiều, Collatz).

Nó cũng nối trực tiếp với lý thuyết đồ thị con (graph minors), giả thuyết Hadwiger (vẫn còn mở), và các câu hỏi rộng hơn về cấu trúc và sắc số.

---

## Từ các video: "có máy tính hỗ trợ" thực sự nghĩa là gì

Các video của Numberphile, Quanta, bài viết của Gonthier trên Notices và trang của Thomas về định lý bốn màu cùng chốt lại bốn ý chính:

1. Chứng minh **không** phải là "thử thật nhiều bản đồ rồi hy vọng". Đó là lập luận cổ điển dùng **phóng điện và tập không tránh được**, đưa vô hạn trường hợp đồ thị phẳng về một danh sách **hữu hạn** cấu hình.  
2. Máy tính kiểm tra **tính khả quy** (và các tính toán tổ hợp liên quan): Appel–Haken (1976), bản rút gọn của RSST (633 cấu hình).  
3. **Bản hình thức hóa bằng Coq của Gonthier (2005)** kiểm tra toàn bộ phần toán học (theo RSST); khi đó, độ tin cậy chỉ còn phụ thuộc vào lõi của trợ lý chứng minh.  
4. Định lý **năm màu** không cần máy tính; công thức **Heawood** áp dụng cho các mặt giống cao (mặt xuyến cần đến bảy màu).

**Tình trạng (2026):** **đã được chứng minh**. Đã giải được không có nghĩa là tầm thường. Hãy so sánh với các bài toán mở trong chương này.

---

## Hiểu lầm thường gặp

| Khẳng định | Sửa lại |
|------------|-----|
| "Đôi khi bốn màu không đủ cho bản đồ phẳng." | Sai. 4CT nói bốn màu luôn đủ (với biên có độ dài dương, theo mô hình chuẩn). |
| "Máy tính kiểm tra các bản đồ ngẫu nhiên." | Sai. Máy kiểm tra tính khả quy của một số hữu hạn cấu hình, trong một chứng minh đã được thiết kế. |
| "Định lý năm màu cũng cần máy tính." | Sai. Nó có chứng minh cổ điển ngắn. |
| "4CT giải quyết bài toán tô màu trên mọi mặt." | Sai. Với các mặt giống cao, dùng số Heawood. |
| "Mọi bản đồ gồm bốn nước đều cần bốn màu." | Sai. Chỉ khi mọi cặp nước đều có chung biên; nhiều bản đồ bốn miền cần ít màu hơn. |
| "Không cần hình thức hóa vì năm 1976 đã giải xong." | Hình thức hóa giúp tăng độ tin cậy và khả năng kiểm tra lại; nó không phủ nhận công trình của Appel–Haken. |

---

## Nguồn video (bộ tư liệu nghiên cứu video)

Đánh giá chi tiết: `research/video-research/Four_Color_Theorem/`.

**Thứ tự xem gợi ý**

1. **Định hướng** — Numberphile, *The Four Color Map Theorem*: [YouTube](https://www.youtube.com/watch?v=NgbK43jB4rQ).  
2. **Nội dung chính (phổ thông)** — Quanta, *Map Coloring Puzzle…*: [YouTube](https://www.youtube.com/watch?v=h7kqlYUV1l8) · [bài viết](https://www.quantamagazine.org/only-computers-can-solve-this-map-coloring-problem-from-the-1800s-20230329/).  
3. **Bối cảnh** — video bổ sung của Numberphile: [YouTube](https://www.youtube.com/watch?v=laMkuPrad3s); Conway (Simons): [YouTube](https://www.youtube.com/watch?v=fPVXBurxfU8).  
4. **Hình thức hóa** — bài của Gonthier trên Notices: [PDF](https://www.ams.org/notices/200811/tx081101382p.pdf).  
5. **Trang về chứng minh RSST** — Thomas: [fourcolor.html](https://thomas.math.gatech.edu/FC/fourcolor.html).

**Sau khi xem video:** 4CT **đã được chứng minh**. Máy tính hỗ trợ không có nghĩa là tìm kiếm ngẫu nhiên; hình thức hóa không có nghĩa là "đến giờ mới đúng".

---


### Phụ đề và khung hình

Phụ đề và các đoạn theo thời gian: `research/video-research/Four_Color_Theorem/transcripts/` · trạng thái: `research/video-research/Four_Color_Theorem/TRANSCRIPT_STATUS.md` · danh sách tổng: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Four_Color_Theorem_NgbK43jB4rQ_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu tham khảo

Danh sách URL: `research/video-research/Four_Color_Theorem/references.md`.

1. Appel & Haken (1976/77).  
2. RSST; [Thomas FC](https://thomas.math.gatech.edu/FC/fourcolor.html).  
3. Gonthier — [Formal Proof—The Four-Color Theorem](https://www.ams.org/notices/200811/tx081101382p.pdf).  
4. Heawood; Wikipedia — [Four color theorem](https://en.wikipedia.org/wiki/Four_color_theorem).  
5. Numberphile: https://www.youtube.com/watch?v=NgbK43jB4rQ · extra: https://www.youtube.com/watch?v=laMkuPrad3s  
6. Quanta: https://www.youtube.com/watch?v=h7kqlYUV1l8 · [bài 2023](https://www.quantamagazine.org/only-computers-can-solve-this-map-coloring-problem-from-the-1800s-20230329/)  
7. Conway: https://www.youtube.com/watch?v=fPVXBurxfU8  
8. Illinois museum: https://distributedmuseum.illinois.edu/exhibit/four-color-theorem/  
9. [Khám phá tô màu bản đồ]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/); [Kakeya]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/). Bộ tư liệu: `research/video-research/Four_Color_Theorem/`.

---

## Hướng đi tiếp

**Tiếp tục lộ trình B**

1. Đã xong: Bốn màu, Chương 1 (trang này).  
2. **Tiếp theo →** [Bài thực hành tô màu, Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/).  

- Viết một bài luận về chuẩn mực cho chứng minh có máy tính hỗ trợ.  
- Nâng cao: giả thuyết Hadwiger (vẫn còn mở).  
- So sánh với [Kakeya]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/).

## Video tham khảo

- **Xem trước:** [The Four Color Map Theorem - Numberphile](https://www.youtube.com/watch?v=NgbK43jB4rQ) — Numberphile, tiếng Anh. Giới thiệu bài toán tô bản đồ và câu chuyện chứng minh; nên xem trước khi đọc bài.
- [The Map Coloring Puzzle That Changed Mathematics](https://www.youtube.com/watch?v=h7kqlYUV1l8) — Quanta Magazine, tiếng Anh. Lịch sử bài toán và vai trò của máy tính trong chứng minh; nên xem sau khi đã nắm ý chính của bài.
- [John Conway - Four Color Theorem and Computer Proofs](https://www.youtube.com/watch?v=fPVXBurxfU8) — Simons Foundation, tiếng Anh. Xem thêm sau hai video trên; Conway bàn về định lý bốn màu và chứng minh bằng máy tính.
