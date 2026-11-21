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

**Định lý Bốn Màu (4CT)** khẳng định rằng mọi bản đồ phẳng đều tô được bằng tối đa **bốn** màu sao cho hai miền có chung một đoạn biên (độ dài dương) luôn khác màu. Phát biểu tương đương: mọi **đồ thị phẳng** hữu hạn đều tô được các đỉnh bằng 4 màu.

Khác với [giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) hay [Kakeya trong nhiều chiều]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/), 4CT **đã được giải**. Nhưng cách giải lại làm thay đổi cuộc tranh luận về thế nào là một chứng minh. Appel và Haken (1976) đưa ra lập luận đầy đủ, trong đó việc xét các trường hợp được kiểm tra bằng máy tính. Các chứng minh đơn giản hơn về sau (Robertson–Sanders–Seymour–Thomas và những người khác) vẫn dựa vào kiểm tra bằng máy trên quy mô lớn. Việc hình thức hóa chứng minh (ví dụ bằng Coq, do Gonthier thực hiện) giúp giảm bớt lo ngại về khả năng kiểm tra lại.

Bài này giới thiệu về **chứng minh có máy tính hỗ trợ** trong khóa học: không phải mô phỏng Monte Carlo, mà là một danh sách hữu hạn các trường hợp tổ hợp do con người thiết kế.

**Nội dung bài:** bài toán tô bản đồ → đồ thị đối ngẫu → định lý năm màu → phản ví dụ nhỏ nhất → phương pháp phóng điện và tính khả quy → vai trò của máy tính → câu hỏi triết học về chứng minh → các mặt có giống cao hơn (Heawood).

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

**Liên hệ với khóa học.** Mục tiêu 1 và câu hỏi "chứng minh là gì?". Đọc cùng: Kakeya (một bài toán mở trong giải tích); [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) (độ khó tính toán, khác với việc máy tính hỗ trợ chứng minh); bài thực hành tô màu bản đồ.

---

## 1. Câu hỏi của người vẽ bản đồ

Từ giữa thế kỷ 19 (Guthrie, De Morgan, Cayley, …), người ta đã hỏi: cần bao nhiêu màu để tô một bản đồ hành chính sao cho các nước láng giềng có màu khác nhau?

- **Hai màu** không đủ ngay khi có một "bánh xe" gồm số lẻ miền kề nhau phù hợp.  
- **Ba màu** không đủ cho một số bản đồ phẳng (ví dụ một miền bị bao quanh bởi một vòng gồm số lẻ miền láng giềng kề nhau).  
- **Bốn màu** được dự đoán là đủ.  
- **Năm màu** đã được chứng minh là đủ bằng lập luận cổ điển (định lý năm màu của Heawood, đơn giản hơn trường hợp bốn màu).

Câu hỏi nghe như chuyện vẽ bản đồ, nhưng khi phát biểu bằng đồ thị, nó trở thành một định lý về cấu trúc của các đồ thị thưa vẽ được trên mặt phẳng.

![Miền kề]({{ site.baseurl }}/img/chapter_img/fourcolor_map_k4.svg)

*Hình. Phác thảo các miền kề nhau, cho thấy vì sao cần nhiều màu.*

---

## 2. Từ bản đồ đến đồ thị phẳng

Ứng với mỗi miền, đặt một **đỉnh**; nối hai đỉnh bằng một **cạnh** khi hai miền có chung một đoạn biên có độ dài dương (không chỉ chạm nhau tại một điểm). Ta được một **đồ thị phẳng** (vẽ được mà các cạnh không cắt nhau, với giả thiết bản đồ đủ "đẹp").

Tô màu các miền tương đương với tô màu các đỉnh sao cho hai đỉnh kề nhau khác màu.

![Dual]({{ site.baseurl }}/img/chapter_img/fourcolor_graph_dual.svg)

*Hình. Đồ thị đối ngẫu: đỉnh ứng với miền, cạnh ứng với biên chung.*

**Dạng đồ thị của 4CT.** Mọi đồ thị phẳng hữu hạn $$G$$ đều thỏa mãn $$\chi(G)\le 4$$, trong đó $$\chi$$ là số màu tối thiểu cần để tô các đỉnh.

Các phát biểu tương đương dùng công thức Euler $$v-e+f=2$$ cho đồ thị phẳng liên thông và một chặn cho bậc trung bình: đồ thị phẳng đơn thì thưa, cụ thể $$e\le 3v-6$$ khi $$v\ge 3$$. Từ đó suy ra luôn có một đỉnh bậc $$\le 5$$, đây là điểm mấu chốt của phép quy nạp trong chứng minh năm màu.

**Lưu ý về mô hình.** 4CT ở dạng chuẩn giả thiết các miền "hợp lý" (biên có độ dài dương; thường hiểu là miền liên thông). Nếu một nước **không liên thông** (gồm nhiều mảnh) thì bài toán thay đổi hẳn, và theo quy tắc khác có thể cần nhiều màu hơn.

---

## 3. Vì sao năm màu dễ hơn bốn màu

**Định lý năm màu** có một chứng minh cổ điển ngắn:

1. Mọi đồ thị phẳng (đơn, đủ lớn) đều có một đỉnh bậc $$\le 5$$ (suy từ công thức Euler, hay $$e\le 3v-6$$).  
2. Bỏ đỉnh đó đi; theo giả thiết quy nạp, tô phần còn lại bằng 5 màu.  
3. Nếu các đỉnh kề với đỉnh vừa bỏ không dùng hết 5 màu thì dễ dàng tô thêm; nếu không, dùng lập luận **chuỗi Kempe** (đổi màu trên một thành phần liên thông gồm hai màu), lập luận này hiệu quả với 5 màu.

Kempe tin rằng mình đã chứng minh được trường hợp bốn màu (1879); Heawood chỉ ra lỗi sai (1890) và giữ lại được kết quả năm màu. Khoảng cách từ 5 xuống 4 là cả một thế kỷ nghiên cứu: lỗi của Kempe không phải một chi tiết nhỏ có thể sửa bằng cùng ý tưởng.

Tóm tắt dễ nhớ: **năm màu = quy nạp + công thức Euler + chuỗi Kempe**; **bốn màu = cấu trúc sâu + số trường hợp khổng lồ**.

---

## 4. Phản ví dụ nhỏ nhất và chiến lược của Appel–Haken

Giả sử $$G$$ là **đồ thị phẳng nhỏ nhất không tô được bằng 4 màu** (phản ví dụ nhỏ nhất). Khi đó, sau các bước rút gọn chuẩn:

- $$G$$ gần như là một phép tam giác phân (đồ thị phẳng cực đại sau khi rút gọn);  
- mọi đỉnh đều có bậc ít nhất 5;  
- một số cấu hình cục bộ bị **loại trừ** nếu chúng **khả quy**: cấu hình $$C$$ là khả quy nếu mọi cách tô màu $$G-C$$ (có thể sau khi đổi màu) đều mở rộng được thành cách tô màu $$G$$; do đó $$C$$ không thể xuất hiện trong phản ví dụ nhỏ nhất.

Nếu tìm được một **tập không tránh được** $$\mathcal{U}$$ gồm các cấu hình (mọi phản ví dụ nhỏ nhất *đều phải* chứa một $$C\in\mathcal{U}$$) và chứng minh mỗi $$C\in\mathcal{U}$$ đều khả quy, ta được mâu thuẫn. Vậy không có phản ví dụ.

![Pipeline]({{ site.baseurl }}/img/chapter_img/fourcolor_proof_pipeline.svg)

*Hình. Tập không tránh được + kiểm tra tính khả quy ⇒ không có phản ví dụ nhỏ nhất.*

**Appel và Haken** xây dựng một tập không tránh được rất lớn và kiểm tra tính khả quy bằng các chương trình máy tính tự viết (cùng với nhiều công sức tính tay). Các chứng minh sau này rút gọn danh sách cấu hình và làm rõ logic (**Robertson, Sanders, Seymour, Thomas**, khoảng 1997), nhưng vẫn kiểm tra bằng máy. Các **trợ lý chứng minh hình thức** (Coq, …) đã kiểm chứng một phiên bản của lập luận, phần nào trả lời lo ngại "chương trình năm 1976 có lỗi".

**Phương pháp phóng điện** (discharging) là một kỹ thuật tổ hợp: gán "điện tích" cho các đỉnh và các mặt, rồi phân phối lại theo các quy tắc cục bộ, để chứng minh rằng mọi đồ thị trong lớp đang xét đều chứa một cấu hình thuộc $$\mathcal{U}$$. Đây là phần do con người thiết kế; máy tính không tự tìm ra định lý, mà chỉ **kiểm tra các trường hợp** trong khuôn khổ đã được thiết kế.

---

## 5. Chứng minh gọn hơn, nhưng vẫn kiểm tra bằng máy

Các công trình sau làm chứng minh chặt chẽ và rõ ràng hơn, nhưng không quay về được một chứng minh tay ngắn gọn. **Robertson, Sanders, Seymour và Thomas (1997)** đưa ra lập luận đơn giản hơn, với tập không tránh được nhỏ hơn nhiều và cấu trúc logic rõ ràng hơn, nhưng vẫn kiểm tra tính khả quy bằng máy. Sau đó còn có các trình bày và kiểm tra độc lập khác. Việc hình thức hóa trong trợ lý chứng minh (đặc biệt là công trình dùng Coq của **Gonthier** cho 4CT) trả lời một lo ngại khác: không chỉ "chương trình có chạy đúng không?" mà còn "mỗi trường hợp đã được hình thức hóa đúng chưa, và có được kiểm tra bởi một lõi (kernel) đáng tin cậy không?"

Cộng đồng toán học đã thống nhất: **4CT là một định lý**. Những gì còn được nghiên cứu là phương pháp (thiết kế quy tắc phóng điện, thu gọn danh sách trường hợp, hình thức hóa các lập luận tổ hợp), chứ không còn là câu hỏi bốn màu có đủ cho bản đồ phẳng hay không.

---

## 6. "Có máy tính hỗ trợ" ở đây nghĩa là gì

Điều quan trọng là phân biệt với mô phỏng Monte Carlo hay chuyện "máy tính tự đoán ra định lý".

Theo cách làm của Appel–Haken và RSST:

- có một **danh sách hữu hạn các trường hợp tổ hợp**, xuất phát từ phương pháp phóng điện do **con người** thiết kế;  
- mỗi trường hợp là một bài toán về việc mở rộng cách tô màu (tính khả quy) trên một đồ thị hữu hạn;  
- máy tính liệt kê và kiểm tra các trường hợp, vì có quá nhiều để kiểm tra tay một cách đáng tin cậy;  
- logic tổng thể (vì sao danh sách là không tránh được; vì sao tính khả quy dẫn đến mâu thuẫn) là lập luận toán học của con người.

Một số câu hỏi triết học vẫn hay được thảo luận:

- Một chứng minh có **nhất thiết** phải để một người đọc và kiểm tra được trong thời gian hợp lý không?  
- Nếu trợ lý chứng minh đã kiểm chứng bản hình thức hóa, liệu có thể coi chứng minh là "kiểm tra được" ở mức lõi và văn bản hình thức không?  
- Ta có thỏa mãn với *việc tồn tại* một phép kiểm tra hữu hạn, hay vẫn muốn tìm một lý do ngắn gọn về mặt khái niệm khiến 4CT trở nên "hiển nhiên" khi nhìn lại?

Các nhà toán học trả lời theo những cách khác nhau. Về mặt toán học, 4CT được chấp nhận là đã chứng minh. Về mặt khái niệm, nó là một cột mốc của **công nghệ chứng minh**, mở đường cho kiểm chứng hình thức và cho việc xét số lượng lớn trường hợp ở các lĩnh vực khác. So với [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): ở đó máy tính là *đối tượng* của câu hỏi; còn ở 4CT, máy tính là *công cụ kiểm tra* trong một chứng minh hữu hạn.

---

## 7. Ra ngoài mặt phẳng: định lý tô màu Heawood

Mặt phẳng là trường hợp đặc biệt. Trên các mặt có giống $$g\ge 1$$ có thể cần nhiều màu hơn. **Số Heawood**

$$
H(g)=\left\lfloor\frac{7+\sqrt{1+48g}}{2}\right\rfloor
$$

cho biết (theo kết quả cổ điển đã hoàn chỉnh) sắc số lớn nhất của các đồ thị vẽ được trên mặt đó. Với **mặt xuyến** ($$g=1$$), bảy màu là chặn chặt: có những bản đồ trên mặt xuyến cần bảy màu, và bảy màu luôn đủ. Thay $$g=0$$ vào công thức được 4, nhưng lập luận của Heawood cho mặt phẳng chỉ cho 5; để có đúng con số bốn, cần toàn bộ 4CT.

![Heawood]({{ site.baseurl }}/img/chapter_img/fourcolor_heawood.svg)

*Hình. Số màu cần dùng tăng theo giống của mặt.*

Điểm cần chú ý: **tính phẳng** là một ràng buộc hình học mạnh, kéo số màu xuống còn bốn, trong khi chỉ thêm một "quai" (mặt xuyến) đã đẩy chặn chặt lên bảy. Bài thực hành ở Chương 7 khuyến khích thử với đồ thị đối ngẫu, các bản đồ nhỏ buộc phải dùng ba hoặc bốn màu, và công thức Heawood trên các mặt đơn giản.

**Miền không liên thông.** Nếu một "nước" gồm nhiều mảnh rời nhau phải tô cùng một màu, bài toán sẽ khác: có thể dựng bản đồ cần nhiều màu tùy ý. 4CT dạng chuẩn giả thiết các miền liên thông (hoặc xử lý các mảnh một cách cẩn thận). Khi tô màu, luôn nói rõ mô hình đang dùng.

---

## 8. Vì sao 4CT quan trọng với toán học

Ngoài việc giải quyết một giả thuyết nổi tiếng, 4CT còn:

- thúc đẩy **phương pháp phóng điện** và cách nhìn cấu trúc về đồ thị phẳng;  
- buộc cộng đồng phải nói rõ các chuẩn mực cho **toán học có kiểm tra bằng máy**;  
- là "phòng thí nghiệm" suốt một thế kỷ cho các ý tưởng đổi màu, tính khả quy và tập không tránh được;  
- là ví dụ đối lập rất tốt với các bài toán **còn mở** trong giải tích và số học (RH, Kakeya nhiều chiều, Collatz).

Nó cũng gần với lý thuyết đồ thị con (graph minors), giả thuyết Hadwiger (vẫn còn mở), và các câu hỏi rộng hơn về cấu trúc và sắc số.

---

## Từ các video: "có máy tính hỗ trợ" thực sự nghĩa là gì

Các video của Numberphile, Quanta, bài viết của Gonthier trên Notices và trang của Thomas về định lý bốn màu cùng chốt lại các ý chính cho mục tiêu 1:

1. Chứng minh **không** phải là "thử thật nhiều bản đồ rồi hy vọng". Đó là lập luận cổ điển dùng **phóng điện và tập không tránh được**, đưa vô hạn trường hợp đồ thị phẳng về một danh sách **hữu hạn** cấu hình.  
2. Máy tính kiểm tra **tính khả quy** (và các tính toán tổ hợp liên quan): Appel–Haken (1976), bản rút gọn của RSST (khoảng 633 cấu hình).  
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

## Bài tập

1. Vẽ một bản đồ phẳng **cần ba màu**; giải thích vì sao hai màu không đủ.  
2. Chuyển bản đồ đó sang đồ thị đối ngẫu và tô các đỉnh bằng 3 màu.  
3. Từ $$e\le 3v-6$$, suy ra mọi đồ thị phẳng đơn với $$v\ge 3$$ đều có một đỉnh bậc $$\le 5$$.  
4. Phác thảo phép quy nạp trong chứng minh năm màu bằng bốn gạch đầu dòng.  
5. Giải thích bằng lời của bạn: tập không tránh được và cấu hình khả quy khác nhau thế nào.  
6. Tìm hiểu lịch sử: đọc một bài kể ngắn về công trình của Appel–Haken; nêu một lời phê bình và một câu trả lời (ví dụ việc hình thức hóa).  
7. Thử đề bài ở [bài thực hành tô màu, Chương 7]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/) với công thức cho mặt xuyến.  
8. So sánh cách cộng đồng chấp nhận chứng minh: 4CT và bản thảo về dòng Ricci của Perelman (việc kiểm chứng ở đó không phải là xét một số khổng lồ trường hợp).

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
