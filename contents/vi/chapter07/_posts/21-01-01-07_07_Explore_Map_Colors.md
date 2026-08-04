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

> **Lộ trình B — Bốn màu (bước 2/2)**  
> **1.** [Định lý bốn màu Ch.1]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/)  
> **2. Bạn đang ở đây:** Studio tô bản đồ Ch.7  
> *Tiên quyết:* dual graph + phác năm màu từ Ch.1.

Bốn màu đủ cho mọi bản đồ phẳng—**Appel–Haken (1976)** và các đơn giản hóa sau, gồm phân tích trường hợp có máy kiểm. Câu đó giấu cả thế kỷ gần-chứng-minh, lỗi Kempe, **định lý năm màu** sạch, và lý thuyết đồ thị trên mặt qua **số Heawood**. Studio thực hành: vẽ map, dựng dual, thất bại 3 màu, tính cận giống, viết đoạn cẩn về “chứng minh” khi máy kiểm case.

Bạn không chạy lại computer search bốn màu. Bạn **luyện định nghĩa** làm định lý có nghĩa và khám phá khi mặt/quy tắc đổi thì điều gì đổi. Cùng kỷ luật studio khác: đóng băng quy tắc trước khi vẽ; nhãn định lý / lịch sử gần đúng / construction / phản tư.

---

## Mục tiêu học tập

Sau studio bạn cần:

- Chuyển map thành **dual graph**; tô map = tô đỉnh đồ thị.
- Chỉ ra map/đồ thị phẳng cần 4 màu và vì sao 3 thất bại.
- Phác **định lý năm màu** qua Euler và đỉnh bậc $$\le 5$$.
- Tính $$H(g)=\bigl\lfloor(7+\sqrt{1+48g})/2\bigr\rfloor$$ cho giống nhỏ và diễn giải.
- Giải thích **quốc gia không liên thông** (empire/mutilated maps) có thể đòi tùy ý nhiều màu.
- Đoạn tách: chứng năm màu sơ cấp, chứng bốn màu hỗ trợ máy, định lý màu trên mặt.

**Tiên quyết.** Đồ thị phẳng, Euler $$v-e+f=2$$, quy nạp cơ bản.

---

## 1. Toán nền

### 1.1 Map, dual, chromatic number

**Bản đồ** (cho bốn màu) là phân hoạch mặt phẳng (hoặc cầu) thành hữu hạn vùng liên thông (“nước”). Hai nước kề nếu chung biên độ dài dương (chạm tại một điểm không tính). **Tô màu** gán màu sao cho nước kề khác màu.

Dựng **dual graph** $$G$$: một đỉnh mỗi nước; một cạnh khi nước chung biên. Tô map ≡ **tô đỉnh** của $$G$$. Với dual map đúng, $$G$$ phẳng (và thường không cầu dưới giả thiết êm). **Số màu** $$\chi(G)$$ là số màu tối thiểu.

**Định lý bốn màu (4CT):** mọi đồ thị phẳng 4-tô được; tương đương, mọi map phẳng 4-tô được.

### 1.2 Vì sao năm màu dễ hơn

Từ Euler cho đồ thị phẳng liên thông đơn, cùng handshaking mặt $$2e\ge 3f$$ (mỗi mặt ≥3 cạnh, mỗi cạnh chạm ≤2 mặt), suy $$e\le 3v-6$$ với $$v\ge 3$$. Do đó bậc trung bình $$2e/v<6$$, nên tồn tại đỉnh $$v$$ với $$\deg(v)\le 5$$. **Định lý năm màu** quy nạp theo $$v$$: bỏ đỉnh bậc thấp, năm-tô phần còn lại, và nếu láng giềng của đỉnh đã xóa dùng đủ năm màu thì thử xích Kempe để giải phóng một màu. Lập luận hoàn toàn người đọc được và là chuẩn mọi khóa đồ thị.

Nỗ lực Kempe 1879 cho **bốn** màu có lỗ (Heawood 1890 phơi). Lỗ tinh—đúng kiểu đáng đọc chậm một lần trong Ch.1. Đạo đức studio: ý quy nạp đẹp có thể *gần* đúng mà vẫn gãy ở một case tô lại. Đó là vì sao phân tích case có máy sau này vào câu chuyện bốn màu mà không vào năm màu.

### 1.3 Appel–Haken làm gì

Chứng minh 4CT giảm bài về tập hữu hạn (nhưng lớn) **cấu hình unavoidable** và **reducible**: mỗi cái không thể xuất hiện trong phản ví dụ tối thiểu. Unavoidability nghĩa mọi phản ví dụ tối thiểu phải chứa một cấu hình (thường chứng bằng discharging: gán charge từ Euler và phân phối lại đến khi buộc cấu hình). Reducibility nghĩa tô phần còn lại có thể mở rộng vào trong sau hữu hạn kiểm tô lại. Kiểm reducibility dùng máy liệt kê case. Công trình sau (Robertson, Sanders, Seymour, Thomas, …) đơn giản hóa tập unavoidable và recheck bằng chương trình độc lập; formalization tăng tin cậy. Dù vậy chứng minh khác năm màu về độ dài và phương pháp: sinh viên nội hóa năm màu trong một buổi chiều, trong khi bốn màu là case analysis quy mô nghiên cứu ngay cả sau đơn giản hóa.

**Câu log:** “hỗ trợ máy” có phải “không phải chứng minh”? Viết chuẩn của bạn trước và sau khi đọc thảo luận Ch.1. Vị trí giữa nhiều nhà toán học giữ: chứng minh là đối tượng xã hội cộng đồng kiểm được về nguyên tắc; máy là checker hợp lệ khi chương trình và đặc tả tự audit được.

### 1.4 Mặt và Heawood

Trên mặt giống $$g\ge 1$$, Euler đổi (đặc số Euler $$\chi=2-2g$$ cho mặt đóng định hướng), và cận bậc trung bình yếu đi vì bất đẳng thức cạnh–đỉnh phụ thuộc $$\chi$$. **Số Heawood**

$$
H(g)=\left\lfloor\frac{7+\sqrt{1+48g}}{2}\right\rfloor
$$

cho cận trên số màu map trên mặt định hướng giống $$g$$ (với $$g=0$$ công thức cho 4, nhưng lập luận Heawood cổ điển cho cầu/mặt phẳng **không** là chứng 4CT đầy đủ—lịch sử quan trọng). **Xuyến** ($$g=1$$): $$H(1)=7$$ và 7 sắc—tồn tại map xuyến cần 7 màu. Tính $$H(g)$$ tay cho giống nhỏ là kiểm fluency bắt buộc ở thí nghiệm C.

Đồ thị đầy đủ $$K_n$$ nhúng trên mặt giống đủ cao; **Ringel–Youngs** giải conjecture Heawood cho $$g\ge 1$$, xác định chromatic number mỗi mặt định hướng. Tương phản với mặt phẳng vừa kỹ thuật vừa văn hóa: khi giống dương, embedding extremal $$K_n$$ thường ghim số màu sắc sạch hơn “bốn” phẳng.

### 1.5 Đổi quy tắc phá bốn

Nếu nước được **không liên thông** (hai mảnh cùng empire phải cùng màu), có thể buộc tùy ý nhiều màu ngay trên mặt phẳng—đồng nhất mảnh cẩn thận để dual mã hóa ràng buộc đa thành phần. Ý construction chuẩn: lấy nhiều cặp vùng phải cùng màu và sắp kề sao “siêu-đỉnh” tạo clique lớn trong đồ thị xung đột. Nếu biên chạm hoang dã, hoặc map vô hạn, phát biểu đổi. Luôn đóng băng quy tắc trong đề xuất: nước liên thông? biên cung dương? map hữu hạn? cầu hay mặt phẳng?

### 1.6 Ngoài map (chân trời)

Tô đồ thị vượt xa bản đồ. **Brooks:** đồ thị liên thông không đầy đủ và không chu trình lẻ thỏa $$\chi(G)\le\Delta(G)$$. **Đa thức màu** đếm tô $$k$$-màu đúng như đa thức theo $$k$$. **Hadwiger** conjecture: chromatic number cao buộc minor đầy đủ lớn. Stretch tùy chọn nếu dual đã fluent; không bắt buộc cho checkpoint.

---

## 2. Conjecture / chứng minh / thí nghiệm

| Nhãn | Ví dụ |
|------|-------|
| **Định lý** | 4CT; năm màu; Heawood $$g\ge 1$$ (Ringel–Youngs) |
| **Gần đúng lịch sử** | Lập luận Kempe bốn màu có lỗ |
| **Construction** | Map bạn cần 4 màu; dual |
| **Phản tư** | Chuẩn chứng minh hỗ trợ máy |

**Tiêu chí:**

1. Artifact: map phẳng cần 4 màu + dual.  
2. Thất bại 3 màu tường minh (đỉnh/nước nào chặn).  
3. $$H(0),H(1),H(2)$$ tính tay.  
4. Phác năm màu bằng **văn xuôi** ≤12 câu (không bullet khô).  
5. Đoạn empire hoặc chuẩn chứng minh máy.

---

## 3. Chuẩn log

**Ngày · Ý định · Hành động · Kết quả · Nhãn · Diễn giải · Tiếp.**

Chụp/scan hình. Generator map ngẫu nhiên: ghi tham số. AI vẽ: disclose; vẫn tự kiểm kề cho ví dụ 4-critical.

---

## 4. Thí nghiệm

Làm ≥2 (khuyến nghị A).

### A — Map phẳng (25–45′)

Phát minh hoặc tìm map cần bốn màu. Ví dụ nhỏ cổ điển gồm cấu hình dual chứa minor $$K_4$$ theo cách thiết yếu, hoặc bốn vùng mỗi vùng gặp ba vùng kia dọc cung biên. Dựng dual cẩn: đỉnh = nước, cạnh chỉ cho cung chung (không chạm điểm). Thử 3 màu có hệ thống—backtracking dual nhỏ—và ghi obstruction (đỉnh nào có ba láng giềng ba màu chặn màu thứ tư dưới palette ba).

**Tiêu chí:** map + dual + obstruction viết + một câu vì sao chạm góc không tạo cạnh.

### B — Câu chuyện năm màu (20–35′)

Từ $$e\le 3v-6$$, chứng tồn tại đỉnh bậc $$\le 5$$. Phác quy nạp năm màu văn xuôi liền: base, bước quy nạp, và làm gì khi năm láng giềng dùng năm màu. Chỗ nào gãy cho bốn màu (slogan lỗi xích Kempe)? Nếu có thời gian, phác *một* xích Kempe hai màu hoán vị dọc đường nối hai láng giềng—rồi ghi hai cặp màu khác nhau có thể can thiệp, đúng vùng nguy hiểm lịch sử.

**Tiêu chí:** bổ đề bậc + outline quy nạp + một câu lỗ bốn màu + Kempe tùy chọn.

### C — Xuyến và giống (20–40′)

Tính $$H(g)$$ cho $$g=0,1,2,3$$. Với $$g=1$$, tìm ảnh map 7 màu trên xuyến (trích dẫn URL/sách). Giải thích vì sao “4” phẳng khó hơn “7” xuyến về lịch sử.

**Tiêu chí:** bảng giá trị + ảnh trích dẫn + ghi chú lịch sử.

### D — Empire không liên thông (20–30′)

Thiết kế/vẽ lại construction buộc ≥5 màu dưới quy tắc empire, hoặc tra construction chuẩn và vẽ lại. Thảo luận dual đổi thế nào (đồng nhất đỉnh?).

**Tiêu chí:** hình + tuyên bố quy tắc + lập luận cận dưới màu.

### E — Tiểu luận văn hóa chứng minh (25–40′)

Sau Ch.1 Appel–Haken, viết 5–8 câu: Chứng minh là gì? Người có phải duyệt mọi case? Recheck độc lập và formalization đổi độ tin thế nào?

**Tiêu chí:** essay với chuẩn cá nhân rõ (không rant).

---

## 5. Nhầm lẫn thường gặp

1. Luôn cần đủ 4 — nhiều map chỉ 2–3; 4 là worst case map phẳng.  
2. Năm màu cần máy — không; bốn mới là computer-assisted.  
3. Heawood ⇒ 4CT — với $$g=0$$ công thức cho 4, nhưng kỹ thuật Heawood cổ điển không chốt case phẳng như Ringel–Youngs chốt giống dương.  
4. Chạm góc buộc khác màu — quy tắc chuẩn cần cung biên.  
5. Mọi đồ thị là dual map — dual map phẳng có cấu trúc; đồ thị bất kỳ có thể không phẳng ($$\chi$$ có thể lớn tùy ý).

---

## 6. Bài tập

1. Từ $$v-e+f=2$$ và $$2e\ge 3f$$ (mặt ≥3 cạnh) suy $$e\le 3v-6$$.  
2. Tồn tại đỉnh bậc $$\le 5$$.  
3. $$K_5$$ không phẳng (lập luận chuẩn) **không** một mình chứng minh 4CT.  
4. Tính $$H(1)$$, $$H(2)$$ cẩn floor.  
5. Đề xuất ≤150 từ: mục artifact, quy tắc đóng băng, tiêu chí.

---

## 7. Rubric

| ☐ | Map + dual |
| ☐ | Obstruction 3 màu |
| ☐ | Heawood $$g=0,1$$ (+2) |
| ☐ | Phác năm màu văn xuôi |
| ☐ | Empire hoặc chuẩn chứng minh máy |
| ☐ | Nối Ch.1 |
| ☐ | Log ≥3 |

---


## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh. Chi tiết: `research/video-research/explore-map-colors/`.

**Khẩu hiệu từ gói nghiên cứu**

- **4CT:** bản đồ phẳng 4 màu (Appel–Haken 1976).
- Định lý 5 màu có chứng minh tay ngắn; 4 màu cần máy/case.
- Studio: đồ thị dual, Kempe; tranh luận “chứng minh là gì.”

**Thứ tự xem gợi ý**

1. **ORIENTATION** — Numberphile — Four Color Map Theorem: [https://www.youtube.com/watch?v=NgbK43jB4rQ](https://www.youtube.com/watch?v=NgbK43jB4rQ).  
2. **INTUITION** — Numberphile — Four Color Theorem extra footage: [https://www.youtube.com/watch?v=laMkuPrad3s](https://www.youtube.com/watch?v=laMkuPrad3s).  

**Cổng chính thức / tài liệu**


Danh mục URL đầy đủ: `research/video-research/explore-map-colors/references.md`.

## 8. Tài liệu


### Gói nghiên cứu video (mọi URL)

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

1. [Ch.1 bốn màu]({{ site.baseurl }}/contents/vi/chapter01/01_09_Four_Color_Theorem/).  
2. Wilson, *Four Colors Suffice* (lịch sử).  
3. Giáo trình đồ thị: Euler, năm màu, Heawood.  
4. Đối chiếu: [Kakeya]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/) (văn hóa mở phân tích vs chứng minh máy).

---

## Hướng đi tiếp

**Lộ trình B hoàn thành** khi rubric đầy và lưu dual artifact.

Hướng nâng nếu dual đã fluent: **Hadwiger**; **list coloring** (Thomassen 5-choosability cho đồ thị phẳng là viên ngọc); **Grötzsch** (đồ thị phẳng không tam giác 3-tô được)—vậy “cần bao nhiêu màu” phụ thuộc giả thiết thêm. Complexity thêm nghĩa khác: quyết định 3-tô được của đồ thị phẳng NP-khó tổng quát, không mâu thuẫn 4CT (4CT khẳng định cận trên đều bằng bốn, không thuật toán hiệu quả cho ba).

**Gợi ý tổng hợp một trang.** Tương phản (i) năm màu như quy nạp người; (ii) bốn màu như reducibility hữu hạn + máy kiểm; (iii) Heawood/Ringel–Youngs như câu chuyện mặt nơi số sắc đôi khi dễ chốt hơn bốn phẳng. Kết bằng chuẩn cá nhân “chứng minh là gì”.

### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/explore-map-colors/transcripts/` · trạng thái: `research/video-research/explore-map-colors/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/explore-map-colors_NgbK43jB4rQ_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

