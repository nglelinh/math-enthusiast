---
layout: post
title: "Cần bao nhiêu màu để tô bản đồ?"
chapter: '07'
order: 7
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
---

> **Lộ trình B: Bốn màu (bước 2/2)**  
> **1.** [Định lý bốn màu, chương 1]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/)  
> **2. Bạn đang ở đây:** bài thực hành tô màu bản đồ, chương 7  
> *Kiến thức cần có:* đồ thị đối ngẫu và phác thảo chứng minh định lý năm màu ở chương 1.

Tháng 10 năm 1852, chàng sinh viên trẻ Francis Guthrie ngồi tô màu bản đồ các hạt của nước Anh và bỗng nảy ra một câu hỏi tưởng chừng ngây thơ: *Liệu có phải mọi bản đồ phẳng — bất kể rắc rối, ngoằn ngoèo đến đâu — đều chỉ cần tối đa bốn màu để không có hai vùng giáp biên nào trùng màu?* Câu hỏi ấy truyền từ cậu em Frederick tới giáo sư Augustus De Morgan, rồi trở thành cơn ám ảnh kéo dài suốt **124 năm**. Năm 1879, luật sư kiêm nhà toán học Alfred Kempe công bố lời giải và cả thế giới đã reo mừng suốt 11 năm — cho đến khi Percy Heawood vạch ra một lỗ hổng cực kỳ tinh vi trong lập luận đổi màu của ông.

Phải đến năm 1976, Kenneth Appel và Wolfgang Haken mới chốt hạ **Định lý bốn màu**, nhưng lại theo một cách chưa từng có tiền lệ: họ dùng máy tính kiểm tra hàng nghìn cấu hình, làm bùng nổ cuộc tranh luận triết học kéo dài hàng thập kỷ về việc *"thế nào mới được gọi là một chứng minh?"*. Trong bài thực hành này, bạn sẽ không chạy lại chương trình kiểm tra hàng nghìn trường hợp ấy. Thay vào đó, bạn sẽ **tự vẽ bản đồ, biến nó thành đồ thị đối ngẫu**, tận tay trải nghiệm vì sao 3 màu thất bại, tự tay giải chứng minh 5 màu gọn đẹp, bước sang mặt bánh rán (mặt xuyến) nơi cần tới 7 màu, và tự trả lời cho riêng mình câu hỏi về ranh giới của chứng minh toán học trong kỷ nguyên máy tính.

---

## Mục tiêu học tập

Sau bài này, bạn cần:

- Chuyển một bản đồ thành **đồ thị đối ngẫu**; tô màu bản đồ tương đương với tô màu các đỉnh của đồ thị.
- Chỉ ra một bản đồ (hay đồ thị phẳng) cần đúng 4 màu và giải thích vì sao 3 màu không đủ.
- Phác thảo chứng minh **định lý năm màu** dựa vào công thức Euler và sự tồn tại đỉnh bậc $$\le 5$$.
- Tính $$H(g)=\bigl\lfloor(7+\sqrt{1+48g})/2\bigr\rfloor$$ cho các giống nhỏ và giải thích ý nghĩa.
- Giải thích vì sao nếu cho phép **một nước gồm nhiều mảnh rời nhau** (bài toán "đế quốc") thì có thể cần nhiều màu tùy ý.
- Viết một đoạn phân biệt: chứng minh năm màu sơ cấp, chứng minh bốn màu có máy tính hỗ trợ, và định lý tô màu trên các mặt.

**Kiến thức cần có.** Đồ thị phẳng, công thức Euler $$v-e+f=2$$, quy nạp cơ bản.

---

## Bản đồ kiến thức nền: Lý thuyết đồ thị và Tô pô bề mặt là gì, nghiên cứu những gì?

Đằng sau trò chơi tô màu bản đồ là hai ngành toán học nền tảng cực kỳ quen thuộc với sinh viên đại học ngành toán và khoa học máy tính:

1. **Lý thuyết đồ thị (Graph Theory):** Ngành này tước bỏ mọi chi tiết hình học không cần thiết (độ dài đường biên, hình dáng ngoằn ngoèo của các quốc gia) và chỉ giữ lại duy nhất **quan hệ kết nối**: mỗi nước trở thành một *đỉnh*, hai nước chung đường biên nối với nhau bằng một *cạnh*. Khi đã chuyển sang **đồ thị đối ngẫu**, bài toán tô màu bản đồ biến thành bài toán tìm **sắc số** $$\chi(G)$$ — số màu ít nhất để tô các đỉnh sao cho hai đỉnh kề nhau luôn khác màu. Không chỉ dùng để tô bản đồ, tô màu đồ thị là mô hình trực tiếp cho bài toán **xếp lịch thi** (hai môn có chung sinh viên không thể thi cùng ca), **cấp phát thanh ghi trong trình biên dịch** (hai biến sống cùng lúc không thể dùng chung thanh ghi CPU), và **phân bổ tần số trạm phát sóng di động** để tránh nhiễu.
2. **Tô pô bề mặt (Surface Topology):** Tại sao trên mặt phẳng (hoặc mặt cầu) chỉ cần 4 màu, nhưng nếu vẽ bản đồ lên bề mặt một chiếc bánh rán (mặt xuyến — torus) thì có thể cần tới **7 màu**? Tô pô học nghiên cứu những bất biến không đổi khi ta co giãn, uốn cong bề mặt mà không xé rách. Bất biến quyết định ở đây là **giống (genus)** $$g$$ — số "lỗ thủng" của bề mặt — liên hệ trực tiếp với **đặc trưng Euler** $$\chi = v - e + f = 2 - 2g$$. Với mặt cầu ($$g=0$$), $$\chi = 2$$ nên mọi đồ thị phẳng đều đủ "thưa" ($$e \le 3v-6$$) để tồn tại đỉnh bậc $$\le 5$$. Nhưng trên mặt xuyến ($$g=1$$), $$\chi = 0$$ khiến đồ thị dày hơn ($$e \le 3v$$), cho phép vẽ trọn đồ thị đầy đủ $$K_7$$ (7 nước đôi một giáp nhau) mà không có cạnh nào cắt nhau!

Ví dụ nhỏ để thấy trực giác ngay lập tức: hãy tưởng tượng một vòng tròn gồm 3 nước $$A, B, C$$ ôm quanh một nước $$D$$ ở giữa — đó chính là đồ thị đầy đủ $$K_4$$. Ba nước ngoài tạo thành một tam giác nên đã ngốn hết 3 màu (đỏ, xanh, vàng); nước $$D$$ ở tâm chạm cả ba nên buộc phải dùng màu thứ tư! Vậy $$\chi \ge 4$$ ngay cả trên bản đồ chỉ có 4 vùng.

---

## 1. Kiến thức toán nền

### 1.1 Bản đồ, đồ thị đối ngẫu, sắc số

Một **bản đồ** (theo nghĩa của bài toán bốn màu) là một cách chia mặt phẳng (hoặc mặt cầu) thành hữu hạn vùng liên thông, gọi là các "nước". Hai nước kề nhau nếu chúng có chung một đoạn biên có độ dài dương (chỉ chạm nhau tại một điểm như ngã tư biên giới thì không tính — nếu tính, một chiếc bánh pizza cắt thành 100 miếng gặp nhau ở tâm sẽ cần tới 100 màu!). Một cách **tô màu** là gán màu cho các nước sao cho hai nước kề nhau luôn khác màu.

Ta dựng **đồ thị đối ngẫu** $$G$$: mỗi nước là một đỉnh; hai đỉnh nối với nhau khi hai nước có chung biên. Tô màu bản đồ chính là **tô màu đỉnh** của $$G$$. Với bản đồ hợp lệ, $$G$$ là đồ thị phẳng (và là đồ thị đơn dưới các giả thiết thông thường). **Sắc số** $$\chi(G)$$ là số màu ít nhất cần dùng.

**Định lý bốn màu (4CT):** mọi đồ thị phẳng đều tô được bằng 4 màu; tương đương, mọi bản đồ phẳng đều tô được bằng 4 màu.

### 1.2 Vì sao năm màu dễ hơn

Với đồ thị phẳng đơn, liên thông, từ công thức Euler kết hợp với bất đẳng thức $$2e\ge 3f$$ (mỗi mặt có ít nhất 3 cạnh, mỗi cạnh giáp nhiều nhất 2 mặt), ta suy ra $$e\le 3v-6$$ khi $$v\ge 3$$. Do đó bậc trung bình $$2e/v<6$$, nên luôn có ít nhất một đỉnh $$v$$ với $$\deg(v)\le 5$$. **Định lý năm màu** được chứng minh bằng quy nạp theo số đỉnh $$v$$: bỏ một đỉnh bậc thấp, tô phần còn lại bằng năm màu, và nếu 5 đỉnh kề với đỉnh đã bỏ dùng đủ cả năm màu (giả sử theo chiều kim đồng hồ là Đỏ–Xanh–Vàng–Lục–Tím) thì dùng **xích Kempe** (ví dụ xét thành phần liên thông gồm các đỉnh Đỏ–Vàng): nếu đỉnh Đỏ và đỉnh Vàng không nối nhau bởi đường đi Đỏ–Vàng, ta đổi màu Đỏ↔Vàng trên nhánh chứa đỉnh Đỏ để giải phóng màu Đỏ; còn nếu chúng có nối nhau, đường đi đó tạo thành một vòng kín tách rời đỉnh Xanh khỏi đỉnh Lục nhờ tính phẳng, nên ta chắc chắn đổi được màu Xanh↔Lục để giải phóng màu Xanh! Lập luận này hoàn toàn đọc hiểu được bằng tay và có mặt trong mọi giáo trình lý thuyết đồ thị.

Năm 1879, Kempe đưa ra một chứng minh cho **bốn** màu bằng cách dùng *hai* xích Kempe cùng lúc, nhưng có lỗ hổng (Heawood chỉ ra năm 1890): hai xích Kempe có thể đan xen và phá hỏng lẫn nhau khi thực hiện đổi màu đồng thời. Lỗ hổng này rất tinh vi, đáng để đọc chậm một lần ở chương 1. Bài học ở đây là: một ý tưởng quy nạp đẹp có thể *gần* đúng nhưng vẫn sai ở một trường hợp tô lại màu. Đó là lý do việc phân tích trường hợp bằng máy tính sau này xuất hiện trong câu chuyện bốn màu chứ không cần cho năm màu.

### 1.3 Appel và Haken đã làm gì

Chứng minh 4CT đưa bài toán về một tập hữu hạn (nhưng rất lớn) các **cấu hình không tránh được** (unavoidable) và **khử được** (reducible): không cấu hình nào trong số đó có thể xuất hiện trong một phản ví dụ nhỏ nhất. Không tránh được nghĩa là mọi phản ví dụ nhỏ nhất đều phải chứa ít nhất một cấu hình trong tập (thường chứng minh bằng phương pháp phóng điện, discharging: gán "điện tích" dựa trên công thức Euler rồi phân phối lại cho đến khi buộc phải có một cấu hình). Khử được nghĩa là mọi cách tô phần bên ngoài đều có thể mở rộng vào bên trong sau hữu hạn bước tô lại. Việc kiểm tra tính khử được dùng máy tính liệt kê các trường hợp (ban đầu là gần 1.936, sau giảm còn 1.476 cấu hình). Các công trình sau đó (Robertson, Sanders, Seymour, Thomas năm 1997 rút xuống 633 cấu hình) đơn giản hóa tập cấu hình và kiểm tra lại bằng chương trình độc lập; việc hình thức hóa chứng minh trên máy (Georges Gonthier bằng Coq năm 2005) càng tăng độ tin cậy. Dù vậy, chứng minh này vẫn khác hẳn chứng minh năm màu về độ dài và phương pháp: sinh viên có thể hiểu chứng minh năm màu trong một buổi chiều, còn chứng minh bốn màu vẫn là một phân tích trường hợp ở quy mô nghiên cứu, kể cả sau khi đã đơn giản hóa.

**Câu hỏi cho nhật ký:** "có máy tính hỗ trợ" có nghĩa là "không phải chứng minh" không? Viết quan điểm của bạn trước và sau khi đọc phần thảo luận ở chương 1. Nhiều nhà toán học giữ quan điểm trung dung: chứng minh là thứ mà cộng đồng có thể kiểm tra được về nguyên tắc; máy tính là công cụ kiểm tra hợp lệ khi chương trình và đặc tả của nó có thể được kiểm tra lại.

### 1.4 Các mặt và số Heawood

Trên mặt có giống $$g\ge 1$$, công thức Euler thay đổi (đặc trưng Euler $$\chi=2-2g$$ với mặt đóng định hướng được), và chặn trên cho bậc trung bình yếu đi vì bất đẳng thức giữa số cạnh và số đỉnh phụ thuộc vào $$\chi$$. **Số Heawood**

$$
H(g)=\left\lfloor\frac{7+\sqrt{1+48g}}{2}\right\rfloor
$$

là chặn trên cho số màu cần để tô bản đồ trên mặt định hướng được có giống $$g$$. Hãy thử thay vài số nhỏ để thấy quy luật:
- Mặt cầu / mặt phẳng ($$g=0$$): $$H(0) = \lfloor (7+1)/2 \rfloor = 4$$ — nhưng lập luận cổ điển của Heawood cho mặt cầu **không** chứng minh được 4CT; điểm này rất quan trọng về mặt lịch sử.
- **Mặt xuyến** ($$g=1$$, một lỗ): $$H(1) = \lfloor (7+\sqrt{49})/2 \rfloor = 7$$, và chặn này là đúng, tức là có bản đồ trên mặt xuyến cần đủ 7 màu.
- Mặt hai lỗ ($$g=2$$): $$H(2) = \lfloor (7+\sqrt{97})/2 \rfloor = \lfloor (7+9.848\dots)/2 \rfloor = 8$$.

Đồ thị đầy đủ $$K_n$$ nhúng được vào các mặt có giống đủ lớn. **Ringel và Youngs** (1968) đã chứng minh giả thuyết Heawood cho mọi $$g\ge 1$$, tức là xác định chính xác sắc số của mọi mặt định hướng được. Sự khác biệt so với mặt phẳng vừa mang tính kỹ thuật vừa thú vị về lịch sử: khi giống dương, cách nhúng $$K_n$$ tối ưu xác định số màu một cách gọn gàng hơn nhiều so với con số "bốn" trên mặt phẳng.

### 1.5 Đổi quy tắc thì con số bốn không còn đúng

Nếu một nước được phép gồm **nhiều mảnh rời nhau** (các mảnh của cùng một "đế quốc" — chẳng hạn lục địa chính và thuộc địa hải ngoại — phải cùng màu), thì có thể buộc phải dùng nhiều màu tùy ý ngay trên mặt phẳng. Khi đó đồ thị đối ngẫu phải gộp các mảnh lại để thể hiện ràng buộc nhiều thành phần. Ý tưởng dựng chuẩn: lấy nhiều nhóm vùng bắt buộc cùng màu và sắp xếp chúng kề nhau sao cho các "siêu đỉnh" tạo thành một clique lớn trong đồ thị xung đột (ví dụ: nếu mỗi đế quốc có tối đa $$m$$ mảnh rời nhau, chặn màu tăng vọt lên tới $$6m$$ khi $$m \ge 2$$!). Nếu biên giới có hình dạng quá bất thường, hoặc bản đồ có vô hạn nước, phát biểu cũng thay đổi. Vì vậy luôn cố định quy tắc trong đề xuất: các nước có liên thông không? biên chung có độ dài dương không? bản đồ có hữu hạn không? trên mặt cầu hay mặt phẳng?

### 1.6 Ngoài bản đồ (mở rộng)

Tô màu đồ thị có phạm vi rộng hơn nhiều so với bản đồ. **Định lý Brooks:** đồ thị liên thông không phải đồ thị đầy đủ và không phải chu trình lẻ thì $$\chi(G)\le\Delta(G)$$. **Đa thức sắc độ** đếm số cách tô đúng bằng $$k$$ màu, và đó là một đa thức theo $$k$$. **Giả thuyết Hadwiger:** sắc số lớn buộc đồ thị phải chứa một đồ thị đầy đủ lớn làm minor. Đây là phần mở rộng tùy chọn khi bạn đã thành thạo đồ thị đối ngẫu, không bắt buộc để đạt yêu cầu.

---

### Video ngắn: Vì sao 3 màu không đủ (K₄) và số Heawood theo giống mặt

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/four-color-kempe_vi.mp4"></video>
</div>

Video dài khoảng 1 phút 51 giây (có thuyết minh tiếng Việt): chuyển bản đồ sang đồ thị đối ngẫu, vì sao K₄ buộc dùng 4 màu, chặn Euler e ≤ 3v − 6, hai trường hợp xích Kempe trong định lý năm màu, bẫy lịch sử 1879 và số Heawood H(g) trên mặt phẳng (4) và mặt xuyến (7).


<div class="interactive-demo" markdown="1">
<div data-demo="fourcolor-explainer" data-preset="k4" data-lang="vi"></div>
</div>
<script src="{{ '/public/js/explainers/fourcolor-explainer.js' | relative_url }}"></script>

## 2. Giả thuyết, chứng minh và thí nghiệm

| Nhãn | Ví dụ |
|------|-------|
| **Định lý** | 4CT; năm màu; Heawood với $$g\ge 1$$ (Ringel–Youngs) |
| **Lịch sử (suýt đúng)** | Lập luận bốn màu của Kempe có lỗ hổng |
| **Cách dựng** | Bản đồ bạn vẽ cần 4 màu; đồ thị đối ngẫu |
| **Suy ngẫm** | Tiêu chuẩn cho chứng minh có máy tính hỗ trợ |

**Tiêu chí:**

1. Sản phẩm: một bản đồ phẳng cần 4 màu kèm đồ thị đối ngẫu.  
2. Chỉ rõ vì sao 3 màu thất bại (đỉnh hay nước nào gây cản trở).  
3. Tính tay $$H(0),H(1),H(2)$$.  
4. Phác thảo chứng minh năm màu bằng **văn xuôi**, không quá 12 câu (không gạch đầu dòng khô khan).  
5. Một đoạn về bài toán đế quốc hoặc về tiêu chuẩn chứng minh bằng máy.

---

## 3. Cách ghi nhật ký

**Ngày · Dự định · Việc đã làm · Kết quả · Nhãn · Giải thích · Bước tiếp theo.**

Chụp hoặc scan hình vẽ. Nếu dùng chương trình sinh bản đồ ngẫu nhiên, ghi lại tham số. Nếu dùng AI để vẽ, hãy ghi rõ; bạn vẫn phải tự kiểm tra quan hệ kề cho ví dụ cần đúng 4 màu.

---

## 4. Thí nghiệm

Làm ít nhất 2 thí nghiệm (nên có A).

### A. Bản đồ phẳng (25–45 phút)

Tự nghĩ ra hoặc tìm một bản đồ cần bốn màu. Ví dụ nhỏ kinh điển: đồ thị đối ngẫu chứa $$K_4$$ (làm minor) một cách thiết yếu, hoặc bốn vùng mà mỗi vùng đều giáp ba vùng còn lại dọc theo một đoạn biên. Dựng đồ thị đối ngẫu cẩn thận: đỉnh là nước, cạnh chỉ nối khi có đoạn biên chung (không tính chạm tại một điểm). Thử tô 3 màu một cách có hệ thống (quay lui trên đồ thị đối ngẫu nhỏ) và ghi lại chỗ cản trở (đỉnh nào có ba đỉnh kề mang đủ ba màu, nên không còn màu cho nó khi chỉ có ba màu).

**Tiêu chí:** bản đồ, đồ thị đối ngẫu, giải thích chỗ cản trở, và một câu giải thích vì sao chạm góc không tạo thành cạnh.

### B. Chứng minh năm màu (20–35 phút)

Từ $$e\le 3v-6$$, chứng minh có đỉnh bậc $$\le 5$$. Phác thảo phép quy nạp năm màu bằng văn xuôi liền mạch: bước cơ sở, bước quy nạp, và cách xử lý khi năm đỉnh kề dùng đủ năm màu. Lập luận này hỏng ở đâu nếu chỉ có bốn màu (ý chính của lỗi xích Kempe)? Nếu còn thời gian, phác thảo *một* xích Kempe: đổi chỗ hai màu dọc theo một đường nối hai đỉnh kề, rồi ghi lại việc hai cặp màu khác nhau có thể cản trở lẫn nhau. Đây chính là chỗ nguy hiểm trong lịch sử.

**Tiêu chí:** bổ đề về bậc, dàn ý quy nạp, một câu về lỗ hổng trong trường hợp bốn màu, và (tùy chọn) xích Kempe.

### C. Mặt xuyến và giống (20–40 phút)

Tính $$H(g)$$ với $$g=0,1,2,3$$. Với $$g=1$$, tìm một hình bản đồ 7 màu trên mặt xuyến (ghi nguồn URL hoặc sách). Giải thích vì sao về mặt lịch sử, con số "4" trên mặt phẳng lại khó hơn con số "7" trên mặt xuyến.

**Tiêu chí:** bảng giá trị, hình có trích nguồn, ghi chú lịch sử.

### D. Đế quốc không liên thông (20–30 phút)

Thiết kế hoặc vẽ lại một cách dựng buộc phải dùng ít nhất 5 màu theo quy tắc đế quốc, hoặc tra cứu cách dựng chuẩn rồi vẽ lại. Thảo luận đồ thị đối ngẫu thay đổi thế nào (có gộp đỉnh không?).

**Tiêu chí:** hình vẽ, phát biểu quy tắc, lập luận chặn dưới số màu.

### E. Bài luận về văn hóa chứng minh (25–40 phút)

Sau khi đọc phần về Appel–Haken ở chương 1, viết 5–8 câu: Chứng minh là gì? Con người có cần tự kiểm tra mọi trường hợp không? Việc kiểm tra lại độc lập và hình thức hóa làm thay đổi độ tin cậy như thế nào?

**Tiêu chí:** bài luận nêu rõ quan điểm cá nhân (không viết kiểu than phiền).

---

## 5. Những hiểu lầm thường gặp

1. "Luôn cần đủ 4 màu." Sai: nhiều bản đồ chỉ cần 2–3 màu; 4 là trường hợp xấu nhất của bản đồ phẳng.  
2. "Định lý năm màu cần máy tính." Sai: chỉ chứng minh bốn màu mới cần máy tính hỗ trợ.  
3. "Công thức Heawood suy ra 4CT." Sai: với $$g=0$$ công thức cho 4, nhưng kỹ thuật cổ điển của Heawood không giải quyết được trường hợp mặt phẳng, khác với việc Ringel–Youngs giải quyết các giống dương.  
4. "Chạm góc thì phải khác màu." Sai: quy tắc chuẩn đòi hỏi có đoạn biên chung.  
5. "Mọi đồ thị đều là đồ thị đối ngẫu của một bản đồ." Sai: đồ thị đối ngẫu của bản đồ phẳng có cấu trúc riêng; đồ thị tùy ý có thể không phẳng ($$\chi$$ có thể lớn tùy ý).

---

## 7. Bảng tự đánh giá

| ☐ | Bản đồ và đồ thị đối ngẫu |
| ☐ | Chỗ cản trở khi dùng 3 màu |
| ☐ | Heawood với $$g=0,1$$ (và 2) |
| ☐ | Phác thảo năm màu bằng văn xuôi |
| ☐ | Bài toán đế quốc hoặc tiêu chuẩn chứng minh bằng máy |
| ☐ | Liên hệ với chương 1 |
| ☐ | Nhật ký ít nhất 3 mục |

---


## Nguồn video (gói nghiên cứu video)

Video dùng để **định hướng và hiểu thêm về văn hóa nghiên cứu**, không thay cho chứng minh. Chi tiết: `research/video-research/explore-map-colors/`.

**Ý chính rút ra từ gói nghiên cứu**

- **4CT:** mọi bản đồ phẳng tô được bằng 4 màu (Appel–Haken 1976).
- Định lý 5 màu có chứng minh tay ngắn gọn; định lý 4 màu cần máy tính kiểm tra các trường hợp.
- Bài thực hành: đồ thị đối ngẫu, xích Kempe; thảo luận "thế nào là chứng minh".

**Thứ tự xem gợi ý**

1. **Định hướng:** Numberphile, Four Color Map Theorem (định lý bốn màu): [https://www.youtube.com/watch?v=NgbK43jB4rQ](https://www.youtube.com/watch?v=NgbK43jB4rQ).  
2. **Trực giác:** Numberphile, Four Color Theorem extra footage (phần quay thêm): [https://www.youtube.com/watch?v=laMkuPrad3s](https://www.youtube.com/watch?v=laMkuPrad3s).  

**Trang chính thức / tài liệu**


Danh mục URL đầy đủ: `research/video-research/explore-map-colors/references.md`.

## 8. Tài liệu


### Gói nghiên cứu video (tất cả URL)

Danh mục đầy đủ: `research/video-research/explore-map-colors/references.md`.

1. Numberphile — Four Color Map Theorem — https://www.youtube.com/watch?v=NgbK43jB4rQ  
2. Numberphile — Four Color Theorem extra footage — https://www.youtube.com/watch?v=laMkuPrad3s  
3. Wikipedia — Four color theorem — https://en.wikipedia.org/wiki/Four_color_theorem  
4. Illinois Distributed Museum — 4CT — https://distributedmuseum.illinois.edu/exhibit/four-color-theorem/  
5. Appel–Haken BAMS announcement (Euclid) — https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-82/issue-5/Every-planar-map-is-four-colorable/bams/1183538218.full  
6. Celebratio — Haken four-color solution — https://celebratio.org/Haken_W/article/794/  
7. Gonthier formal proof discussion (MathOverflow thread) — https://mathoverflow.net/questions/44673/human-checkable-proof-of-the-four-color-theorem  
8. Wikipedia — Five color theorem — https://en.wikipedia.org/wiki/Five_color_theorem  
9. Wikipedia — Graph coloring — https://en.wikipedia.org/wiki/Graph_coloring  
10. Thư mục gói: `research/video-research/explore-map-colors/`.

1. [Định lý bốn màu, chương 1]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/).  
2. Wilson, *Four Colors Suffice* (Bốn màu là đủ; sách lịch sử).  
3. Giáo trình lý thuyết đồ thị: công thức Euler, năm màu, Heawood.  
4. Để đối chiếu: [Kakeya]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/) (một bài toán giải tích còn mở, khác với chứng minh bằng máy).

---

## Hướng đi tiếp

**Hoàn thành lộ trình B** khi bạn đã đánh dấu đủ bảng tự đánh giá và lưu lại đồ thị đối ngẫu đã vẽ.

Hướng nâng cao khi đã thành thạo đồ thị đối ngẫu: **giả thuyết Hadwiger**; **tô màu theo danh sách** (định lý của Thomassen rằng đồ thị phẳng tô được theo danh sách 5 màu là một kết quả rất đẹp); **định lý Grötzsch** (đồ thị phẳng không có tam giác tô được bằng 3 màu). Như vậy, câu hỏi "cần bao nhiêu màu" phụ thuộc vào các giả thiết thêm. Độ phức tạp tính toán cho thêm một góc nhìn: bài toán quyết định một đồ thị phẳng có tô được bằng 3 màu hay không là NP-đầy đủ. Điều này không mâu thuẫn với 4CT, vì 4CT chỉ khẳng định chặn trên bốn màu cho mọi đồ thị phẳng, không cho thuật toán hiệu quả để kiểm tra ba màu.

**Gợi ý bài tổng hợp một trang.** So sánh (i) chứng minh năm màu như một phép quy nạp con người làm được; (ii) chứng minh bốn màu như tập cấu hình khử được hữu hạn cộng với kiểm tra bằng máy; (iii) Heawood và Ringel–Youngs, câu chuyện trên các mặt mà ở đó sắc số đôi khi dễ xác định hơn con số bốn trên mặt phẳng. Kết thúc bằng quan điểm cá nhân về "thế nào là chứng minh".

### Bản ghi lời và khung hình (trích tự động)

Bản ghi lời thoại và các đoạn theo thời gian: `research/video-research/explore-map-colors/transcripts/` · trạng thái: `research/video-research/explore-map-colors/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Khung hình mẫu từ video]({{ site.baseurl }}/img/video_research/nonflagships/explore-map-colors_NgbK43jB4rQ_thumb.jpg)

*Hình. Khung hình mẫu từ video chính của gói (xem gói nghiên cứu để biết mốc thời gian).*


## Video tham khảo

- **Xem trước:** [The Four Color Map Theorem - Numberphile](https://www.youtube.com/watch?v=NgbK43jB4rQ) (Numberphile, tiếng Anh). Giới thiệu định lý bốn màu và cách chuyển bản đồ thành đồ thị. Nên xem trước khi làm thí nghiệm A.
- [The Map Coloring Puzzle That Changed Mathematics](https://www.youtube.com/watch?v=h7kqlYUV1l8) (Quanta Magazine, tiếng Anh). Kể lại lịch sử bài toán bốn màu và chứng minh có máy tính hỗ trợ. Xem sau khi đã nắm ý chính.
- [John Conway - Four Color Theorem and Computer Proofs](https://www.youtube.com/watch?v=fPVXBurxfU8) (Simons Foundation, tiếng Anh). Conway bàn về định lý bốn màu và chứng minh bằng máy tính. Hữu ích cho bài luận ở thí nghiệm E.
