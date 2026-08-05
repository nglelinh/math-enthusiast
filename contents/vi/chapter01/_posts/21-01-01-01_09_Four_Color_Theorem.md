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
> **1. Bạn đang ở đây:** Ch.1 Định lý Bốn Màu — lý thuyết + văn hóa chứng minh  
> **2. Tiếp theo:** [Studio tô màu Ch.7]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/) — dual, Heawood, viết  
> *Thời gian gợi ý:* ~2 giờ bài → ~1–2 giờ studio.

**Định lý Bốn Màu (4CT)** khẳng định mọi bản đồ phẳng có thể tô bằng tối đa **bốn** màu sao cho các miền chung biên độ dài dương nhận màu khác nhau. Tương đương: mọi **đồ thị phẳng** hữu hạn đều 4-tô màu được đỉnh.

Khác [giả thuyết Riemann]({{ site.baseurl }}/contents/vi/chapter01/01_02_Riemann_Hypothesis/) hay [Kakeya chiều cao]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/), 4CT **đã được giải**—nhưng cách giải định hình tranh luận thế nào là một chứng minh. Appel–Haken (1976) đưa lập luận đầy đủ với phân tích case được máy kiểm; các đơn giản hóa sau (Robertson–Sanders–Seymour–Thomas và người khác) vẫn dựa kiểm tra máy quy mô lớn. Formalization (ví dụ Coq của Gonthier) làm dịu lo ngại tái lập.

Bài này là điểm vào văn hóa **chứng minh hỗ trợ máy tính** trong khóa học: không phải Monte Carlo, mà checklist tổ hợp hữu hạn do con người thiết kế.

**Lộ trình:** folklore tô bản đồ → đồ thị dual → định lý năm màu → phản ví dụ tối thiểu → discharging / reducibility → hỗ trợ máy → triết lý chứng minh → mặt cao Heawood.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu 4CT bằng ngôn ngữ bản đồ và ngôn ngữ đồ thị (số màu tô đỉnh $$\chi(G)\le 4$$ cho $$G$$ phẳng hữu hạn).
- Giải thích phép chuyển **dual graph**: miền ↔ đỉnh, biên chung ↔ cạnh.
- Phác thảo vì sao **năm** màu dễ hơn bốn (Heawood / quy nạp + bậc $$\le 5$$ + Kempe chain).
- Mô tả **tập không tránh được** (unavoidable set) và cấu hình **reducible** ở mức khẩu hiệu.
- Thảo luận chứng minh hỗ trợ máy tính như vấn đề triết học *và* thực hành (surveyable proof, formal verification).
- Đối chiếu mặt phẳng với công thức **Heawood** trên mặt giống $$g\ge 1$$.
- Liên kết [studio tô màu Ch.7]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/).

**Tiên quyết.** Đồ thị như đỉnh/cạnh; hình dung vẽ phẳng không cắt. Không cần lý thuyết đồ thị nâng cao.

**Liên kết seminar.** LO1 + thảo luận “chứng minh là gì?”. Ghép: Kakeya (văn hóa bài mở giải tích); [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/) (độ cứng tính toán—khác hỗ trợ máy trong chứng minh); studio map colors.

---

## 1. Câu hỏi người vẽ bản đồ

Từ giữa thế kỷ 19 (Guthrie, De Morgan, Cayley, …), người ta hỏi: bao nhiêu màu đủ để tô bản đồ chính trị sao cho các quốc gia láng giềng khác màu?

- **Hai màu** thất bại ngay khi xuất hiện “bánh xe” lẻ các miền kề nhau theo cách phù hợp.  
- **Ba màu** thất bại với một số bản đồ phẳng (ví dụ cấu hình miền bị bao bởi vòng lẻ các láng giềng kề nhau thích hợp).  
- **Bốn màu** được phỏng đoán là đủ.  
- **Năm màu** được chứng minh đủ bằng lập luận cổ điển (định lý năm màu của Heawood; đơn giản hơn bốn).

Câu hỏi nghe như thủ công bản đồ; hình thức hóa đồ thị biến nó thành định lý cấu trúc về đồ thị thưa nhúng được trên mặt phẳng.

![Miền kề]({{ site.baseurl }}/img/chapter_img/fourcolor_map_k4.svg)

*Hình. Phác thảo các miền kề nhau—động lực cần nhiều màu.*

---

## 2. Từ bản đồ tới đồ thị phẳng

Gắn mỗi miền một **đỉnh**; vẽ **cạnh** khi hai miền chung biên độ dài dương (không chỉ chạm tại một điểm). Kết quả là **đồ thị phẳng** (vẽ không cắt, dưới giả thiết bản đồ ôn hòa).

Tô miền ⇔ tô đỉnh sao cho hai đỉnh kề khác màu.

![Dual]({{ site.baseurl }}/img/chapter_img/fourcolor_graph_dual.svg)

*Hình. Đồ thị dual: đỉnh = miền; cạnh = biên chung.*

**Dạng đồ thị của 4CT.** Mọi đồ thị phẳng hữu hạn $$G$$ thỏa $$\chi(G)\le 4$$, với $$\chi$$ là số màu tô đỉnh tối thiểu.

Các phát biểu tương đương dùng công thức Euler $$v-e+f=2$$ cho đồ thị phẳng liên thông và chặn bậc trung bình: đồ thị phẳng đơn giản thưa—$$e\le 3v-6$$ khi $$v\ge 3$$. Từ đó suy tồn tại đỉnh bậc $$\le 5$$, viên gạch của quy nạp năm màu.

**Ghi chú mô hình.** 4CT chuẩn giả định miền “hợp lý” (biên độ dài dương; thường hiểu miền liên thông). Quốc gia **không liên thông** (nhiều mảnh) đổi bài toán hoàn toàn—có thể cần nhiều màu hơn theo quy tắc khác.

---

## 3. Vì sao năm màu dễ hơn bốn

**Định lý năm màu** có chứng minh cổ điển ngắn:

1. Mọi đồ thị phẳng (đơn giản, đủ lớn) có đỉnh bậc $$\le 5$$ (từ Euler / $$e\le 3v-6$$).  
2. Gỡ đỉnh đó; quy nạp tô phần còn lại bằng 5 màu.  
3. Nếu các láng giềng của đỉnh bị gỡ không dùng hết 5 màu, mở rộng dễ; nếu không, dùng lập luận **chuỗi Kempe** (đổi màu trên thành phần liên thông hai màu) hoạt động với 5 màu.

Kempe tin đã có chứng minh bốn màu (1879); Heawood chỉ ra lỗi (1890) và cứu được năm màu. Khoảng cách giữa 5 và 4 ẩn cả thế kỷ làm việc: lỗi Kempe cho bốn màu không phải chi tiết nhỏ dễ vá bằng cùng ý.

Khẩu hiệu sư phạm: **năm màu = quy nạp + Euler + Kempe ổn định**; **bốn màu = cấu trúc sâu + case khổng lồ**.

---

## 4. Phản ví dụ tối thiểu và chiến lược Appel–Haken

Giả sử $$G$$ là **đồ thị phẳng tối thiểu không 4-tô màu được** (phản ví dụ nhỏ nhất). Khi đó, sau các rút gọn chuẩn:

- $$G$$ mang cấu trúc gần tam giác phân (maximal planar sau reduction);  
- mọi đỉnh có bậc ít nhất 5;  
- một số cấu hình địa phương bị **cấm** nếu chúng **reducible**: cấu hình $$C$$ reducible nếu mọi cách tô của $$G-C$$ (sau có thể đổi màu) mở rộng được thành tô của $$G$$—vậy $$C$$ không thể xuất hiện trong phản ví dụ tối thiểu.

Nếu chỉ ra một **tập không tránh được** $$\mathcal{U}$$ các cấu hình—mọi phản ví dụ tối thiểu *phải* chứa một $$C\in\mathcal{U}$$—và chứng minh mỗi $$C\in\mathcal{U}$$ reducible, ta được mâu thuẫn. Không còn phản ví dụ.

![Pipeline]({{ site.baseurl }}/img/chapter_img/fourcolor_proof_pipeline.svg)

*Hình. Tập không tránh được + kiểm reducibility ⇒ không có phản ví dụ tối thiểu.*

**Appel–Haken** xây tập không tránh được lớn và kiểm reducibility bằng chương trình máy tùy chỉnh (cộng lao động tay đáng kể). Các chứng minh sau giảm danh sách cấu hình và làm rõ logic (**Robertson, Sanders, Seymour, Thomas**, khoảng 1997), vẫn với kiểm máy. **Formal proof assistants** (Coq, …) đã xác minh phiên bản lập luận, trả lời một phần lo ngại “bug chương trình 1976.”

**Discharging** (xả điện) là kỹ thuật tổ hợp gán “điện tích” cho đỉnh/mặt rồi phân phối lại theo quy tắc địa phương để chứng minh mọi đồ thị trong lớp phải chứa một cấu hình trong $$\mathcal{U}$$. Đây là phần “con người thiết kế”; máy không đoán định lý—máy **kiểm case** trong khung đã thiết kế.

---

## 5. Tinh giản, vẫn kiểm bằng máy

Công trình sau cải thiện vệ sinh chứng minh mà không trở lại chứng minh tay ngắn. **Robertson, Sanders, Seymour và Thomas (1997)** cho lập luận đơn giản hơn với tập không tránh được nhỏ hơn nhiều và cấu trúc logic rõ hơn, vẫn dựa trên kiểm reducibility bằng máy. Các trình bày và kiểm độc lập khác theo sau. Formalization trong proof assistant (đặc biệt phát triển Coq của **Gonthier** cho 4CT) trả lời lo ngại khác: không chỉ “chương trình có chạy?” mà “mỗi case đã được formal hóa đúng và kernel tin cậy kiểm?”

Trạng thái cộng đồng đã ổn: **4CT là định lý**. Phần còn sôi là phương pháp—thiết kế discharging, thu nhỏ danh sách case, formal hóa lập luận tổ hợp—không phải câu hỏi bốn màu có đủ cho bản đồ phẳng hay không.

---

## 6. “Hỗ trợ máy tính” nghĩa là gì ở đây

Quan trọng là tách khỏi Monte Carlo hay “máy đoán định lý.”

Trong truyền thống Appel–Haken / RSST:

- một **checklist tổ hợp hữu hạn** xuất phát từ phương pháp discharging do **người** thiết kế;  
- mỗi case là bài toán mở rộng tô màu / reducibility đồ thị hữu hạn;  
- máy liệt kê và kiểm các case quá nhiều để tính tay tin cậy;  
- logic tổng thể (vì sao danh sách không tránh được; vì sao reducibility cho mâu thuẫn) là lập luận toán học của người.

Câu hỏi triết học vẫn phổ biến trong seminar:

- Chứng minh có **bắt buộc** surveyable bởi một tâm trí người trong thời gian hợp lý không?  
- Nếu proof assistant xác minh formalization, có khôi phục dạng surveyability ở mức kernel và văn bản formal không?  
- Ta hài lòng với *sự tồn tại* của kiểm hữu hạn, hay vẫn tìm lý do khái niệm ngắn khiến 4CT “hiển nhiên” nhìn lại?

Các nhà toán học trả lời khác nhau. Về mặt toán, 4CT được chấp nhận đã chứng minh. Về mặt khái niệm, nó là cột mốc **công nghệ chứng minh**—tiền thân của formal verification và case analysis lớn ở lĩnh vực khác. So với [P vs NP]({{ site.baseurl }}/contents/vi/chapter01/01_03_P_vs_NP/): ở đó máy tính là *đối tượng* của câu hỏi; ở 4CT máy tính là *công cụ kiểm* trong chứng minh hữu hạn.

---

## 7. Vượt mặt phẳng: định lý tô màu Heawood

Mặt phẳng đặc biệt. Trên mặt giống $$g\ge 1$$, có thể cần nhiều màu hơn. **Số Heawood**

$$
H(g)=\left\lfloor\frac{7+\sqrt{1+48g}}{2}\right\rfloor
$$

cho (trong câu chuyện cổ điển hoàn chỉnh) số chromatic tối đa cho đồ thị nhúng được trên mặt đó. Với **xuyến** ($$g=1$$), bảy màu là chặt: một số bản đồ torus cần bảy, và bảy luôn đủ. Trường hợp $$g=0$$ cắm vào công thức cho 4, nhưng lịch sử Heawood cho mặt phẳng là 5; bốn sắc nét đòi hỏi 4CT đầy đủ.

![Heawood]({{ site.baseurl }}/img/chapter_img/fourcolor_heawood.svg)

*Hình. Nhu cầu màu tăng theo giống mặt.*

Tương phản sư phạm: **tính phẳng** là ràng buộc hình học mạnh kéo chặn màu xuống bốn, trong khi một “quai” (torus) nhảy chặn chặt lên bảy. Studio Ch.7 khuyến khích chơi dual, bản đồ nhỏ ép ba/bốn màu, và công thức Heawood trên mặt đồ chơi.

**Vùng không liên thông.** Nếu một “quốc gia” có nhiều thành phần liên thông phải cùng màu, bài toán đổi: có thể dựng bản đồ cần tùy ý nhiều màu. 4CT chuẩn giả định vùng liên thông (hoặc xử lý thành phần cẩn thận). Luôn nêu mô hình khi tô màu.

---

## 8. Vì sao 4CT quan trọng với toán học

Ngoài việc đóng một conjecture nổi tiếng, 4CT:

- thúc đẩy **phương pháp discharging** và tư duy cấu trúc về đồ thị phẳng;  
- buộc cộng đồng articulating chuẩn mực cho **toán học kiểm bằng máy**;  
- cung cấp phòng thí nghiệm trăm năm cho recoloring, reducibility, và tập không tránh được;  
- vẫn là tương phản sư phạm hoàn hảo với bài **mở** giải tích và số học (RH, Kakeya chiều cao, Collatz).

Nó cũng nằm gần graph minors, giả thuyết Hadwiger (vẫn mở), và câu hỏi rộng hơn về cấu trúc và số chromatic.

---

## Từ video: “hỗ trợ máy tính” thực sự nghĩa là gì

Numberphile, Quanta, essay Notices của Gonthier và trang Thomas FC cố định khẩu hiệu LO1:

1. Chứng minh **không** phải “thử nhiều bản đồ rồi hy vọng.” Đó là lập luận **discharging / unavoidable set** cổ điển, đưa case phẳng vô hạn về danh sách cấu hình **hữu hạn**.  
2. Máy kiểm **reducibility** (và sổ sách tổ hợp liên quan)—Appel–Haken (1976), tinh gọn RSST (~633 cấu hình).  
3. **Formalization Coq của Gonthier (2005)** kiểm toàn bộ phát triển toán (theo RSST), tin cậy tập trung vào kernel assistant.  
4. **Năm màu** không cần máy; **Heawood** cho giống cao (torus tới bảy).

**Tình trạng (2026):** **đã chứng minh**. Giải được ≠ tầm thường. Đối chiếu các bài mở trong chương này.

---

## Nhầm lẫn phổ biến

| Khẳng định | Sửa |
|------------|-----|
| “Đôi khi bốn màu không đủ cho bản đồ phẳng.” | Sai—4CT nói bốn luôn đủ (biên độ dài dương, mô hình chuẩn). |
| “Máy kiểm bản đồ ngẫu nhiên.” | Sai—kiểm reducibility hữu hạn trong chứng minh thiết kế. |
| “Định lý năm màu cũng cần máy.” | Sai—có chứng minh cổ điển ngắn. |
| “4CT quyết định tô màu mọi mặt.” | Sai—giống cao dùng số Heawood. |
| “Mọi bản đồ bốn quốc gia cần bốn màu.” | Sai—chỉ khi mọi cặp chung biên; nhiều bản đồ bốn miền cần ít hơn. |
| “Formalization không cần vì 1976 đã xong.” | Formalization tăng tin cậy tái lập; không phủ nhận lịch sử Appel–Haken. |

---

## Bài tập

1. Vẽ một bản đồ phẳng **cần ba màu**; lập luận hai màu thất bại.  
2. Chuyển bản đồ đó sang dual và tô 3 màu các đỉnh.  
3. Từ $$e\le 3v-6$$ suy mọi đồ thị phẳng đơn giản $$v\ge 3$$ có đỉnh bậc $$\le 5$$.  
4. Phác thảo quy nạp năm màu trong bốn gạch đầu dòng.  
5. Bằng lời của bạn: unavoidable vs reducible.  
6. Literacy lịch sử: đọc tường thuật ngắn Appel–Haken; liệt kê một phê bình và một đáp (ví dụ formalization).  
7. Thử prompt studio [tô màu Ch.7]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/) với công thức torus.  
8. So văn hóa chứng minh: 4CT vs preprint Ricci flow của Perelman (xác minh cộng đồng không cùng kiểu nổ case).

---

## Nguồn video (gói math-video-researcher)

Xếp hạng: `research/video-research/Four_Color_Theorem/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile, *The Four Color Map Theorem*: [YouTube](https://www.youtube.com/watch?v=NgbK43jB4rQ).  
2. **Cốt lõi phổ thông** — Quanta, *Map Coloring Puzzle…*: [YouTube](https://www.youtube.com/watch?v=h7kqlYUV1l8) · [bài](https://www.quantamagazine.org/only-computers-can-solve-this-map-coloring-problem-from-the-1800s-20230329/).  
3. **Văn hóa** — Numberphile extra: [YouTube](https://www.youtube.com/watch?v=laMkuPrad3s); Conway (Simons): [YouTube](https://www.youtube.com/watch?v=fPVXBurxfU8).  
4. **Formalization** — Gonthier Notices: [PDF](https://www.ams.org/notices/200811/tx081101382p.pdf).  
5. **Cổng RSST** — Thomas: [fourcolor.html](https://thomas.math.gatech.edu/FC/fourcolor.html).

**Sau video:** 4CT **đã chứng minh**. Hỗ trợ máy ≠ tìm ngẫu nhiên; formalization ≠ “chỉ bây giờ mới đúng.”

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/Four_Color_Theorem/transcripts/` · trạng thái: `research/video-research/Four_Color_Theorem/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/Four_Color_Theorem_NgbK43jB4rQ_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu tham khảo

Thư mục URL: `research/video-research/Four_Color_Theorem/references.md`.

1. Appel & Haken (1976/77).  
2. RSST; [Thomas FC](https://thomas.math.gatech.edu/FC/fourcolor.html).  
3. Gonthier — [Formal Proof—The Four-Color Theorem](https://www.ams.org/notices/200811/tx081101382p.pdf).  
4. Heawood; Wikipedia — [Four color theorem](https://en.wikipedia.org/wiki/Four_color_theorem).  
5. Numberphile: https://www.youtube.com/watch?v=NgbK43jB4rQ · extra: https://www.youtube.com/watch?v=laMkuPrad3s  
6. Quanta: https://www.youtube.com/watch?v=h7kqlYUV1l8 · [bài 2023](https://www.quantamagazine.org/only-computers-can-solve-this-map-coloring-problem-from-the-1800s-20230329/)  
7. Conway: https://www.youtube.com/watch?v=fPVXBurxfU8  
8. Illinois museum: https://distributedmuseum.illinois.edu/exhibit/four-color-theorem/  
9. [Explore map colors]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/); [Kakeya]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/). Gói: `research/video-research/Four_Color_Theorem/`.

---

## Hướng đi tiếp

**Tiếp lộ trình B**

1. Xong: Ch.1 Bốn màu (trang này).  
2. **Tiếp →** [Studio tô màu Ch.7]({{ site.baseurl }}/contents/vi/chapter07/07_07_Explore_Map_Colors/).  

- Essay về chuẩn mực computer-assisted proof.  
- Nâng cao: Hadwiger (vẫn mở).  
- Đối chiếu [Kakeya]({{ site.baseurl }}/contents/vi/chapter01/01_08_Kakeya_Conjecture/).
