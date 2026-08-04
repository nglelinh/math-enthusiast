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

**Định lý Bốn Màu** khẳng định mọi bản đồ phẳng có thể tô bằng nhiều nhất bốn màu sao cho các vùng kề nhau khác màu. Phát biểu từ thế kỷ XIX và chỉ được chứng minh năm 1976 bởi **Kenneth Appel** và **Wolfgang Haken**, đây là định lý lớn đầu tiên mà chứng minh **dùng máy tính một cách thiết yếu**. Đóng góp con người không bị xóa; nó được tổ chức lại. Bài này phát triển **ý tưởng chứng minh**: quy họ vô hạn bản đồ về checklist hữu hạn cấu hình, chỉ ra mọi phản ví dụ tối thiểu phải chứa một cấu hình trong “tập không tránh được,” và mỗi cấu hình đó “rút gọn được” nên không thể xuất hiện trong phản ví dụ tối thiểu.

Dư chấn triết học vẫn quan trọng: Chứng minh là gì khi không ai đọc hết mọi trường hợp? Các formal verification sau này trong proof assistant trả lời một phần bằng cách kiểm tra lập luận hữu hạn trong kernel tin cậy.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu Định lý Bốn Màu dạng bản đồ và dạng đồ thị (tô màu đỉnh đồ thị phẳng, dual cẩn thận).
- Giải thích chiến lược: phản ví dụ tối thiểu, tập không tránh được, cấu hình rút gọn được, discharging.
- Mô tả phân công giữa insight con người và liệt kê máy.
- Phân biệt bốn màu (đúng) với “ba màu cho mọi đồ thị phẳng” (sai) và năm màu (định lý cổ điển dễ hơn).
- Thảo luận ngắn, công bằng về chứng minh có máy tính đã đổi gì với tri thức toán.
- Tránh nhầm về bản đồ trên mặt khác và tô màu thuật toán thực tế.

**Tiên quyết.** Ý tưởng không hình thức về đồ thị phẳng; phân tích trường hợp hữu hạn là gì. Không cần chạy code 1976.

---

## 1. Phát biểu và dual

**Định lý Bốn Màu.** Các “nước” trên mọi bản đồ chính trị vẽ trên mặt phẳng (hoặc mặt cầu), mỗi nước liên thông và kề nghĩa là chia sẻ biên độ dài dương (không chỉ một điểm), có thể tô bằng bốn màu sao cho nước kề khác màu.

Về đồ thị: đặt đỉnh trong mỗi nước và cạnh giữa các nước chia biên. Kết quả là **đồ thị phẳng**, và định lý trở thành: mọi đồ thị phẳng **4-tô màu được**. Vệ sinh kỹ thuật xử lý đa cạnh, liên thông nước, nghĩa chính xác của kề; phát biểu mức ý tưởng ổn định.

Năm màu đủ theo định lý cổ điển Heawood (và dòng Kempe). Ba màu **không** đủ cho mọi đồ thị phẳng. Vậy bốn là số phổ quát sắc nét cho mặt phẳng.

---

## 2. Vì sao tấn công trực tiếp khó

Có vô hạn bản đồ phẳng. Chứng minh phải hoặc tìm lý do cấu trúc bốn màu luôn đủ, hoặc quy phong cảnh vô hạn về tập **hữu hạn** tình huống bao quát mọi khả năng.

Chứng minh Appel–Haken (và hậu duệ) đi đường thứ hai, trong truyền thống nỗ lực thế kỷ XIX của Kempe. Chứng minh công bố của Kempe có lỗ; lỗ dạy thế hệ sau phép rút gọn nào mong manh. Chứng minh thành công sửa và mở rộng lớn công nghệ cấu hình-và-discharging.

---

## 3. Phản ví dụ tối thiểu

Giả sử, để dẫn mâu thuẫn, một số đồ thị phẳng không 4-tô màu được. Trong các phản ví dụ, chọn cái **tối thiểu**—thường tối thiểu số đỉnh. Phản ví dụ tối thiểu có tính chất hữu ích: khó tô, nhưng mọi đồ thị phẳng nhỏ hơn *đều* 4-tô màu được. Do đó nếu chỉ ra một mảnh cục bộ có thể co hoặc tô lại dùng màu từ đồ thị nhỏ hơn, mảnh đó không thể xuất hiện trong phản ví dụ tối thiểu.

Đó là logic của **tính rút gọn được**: cấu hình rút gọn được nếu sự hiện diện cho phép dựng 4-tô màu toàn cục từ 4-tô màu đồ thị nhỏ hơn, mâu thuẫn tính tối thiểu của phản ví dụ chứa nó.

---

## 4. Tập không tránh được

**Tập không tránh được** các cấu hình là danh sách $$\mathcal{U}=\{C_1,\ldots,C_N\}$$ sao cho **mọi** phản ví dụ tối thiểu phải chứa ít nhất một $$C_i$$.

Nếu mọi cấu hình trong tập không tránh được đều rút gọn được, thì không tồn tại phản ví dụ tối thiểu: nó sẽ phải chứa cấu hình rút gọn được—điều phản ví dụ tối thiểu không thể. Mâu thuẫn chứng minh định lý.

Toàn bộ chiến lược gọn thành hai khẳng định hữu hạn:

1. **Không tránh được:** mọi ứng viên phản ví dụ tối thiểu chứa một $$C_i\in\mathcal{U}$$.  
2. **Rút gọn được:** mỗi $$C_i$$ rút gọn được.

Khẳng định 2, với danh sách lớn, là nơi máy tỏa sáng: mỗi cấu hình đòi kiểm nhiều mở rộng tô màu. Khẳng định 1 thường chứng minh bằng **phương pháp discharging**—sổ sách trên bậc đỉnh và cấu trúc mặt, chỉ ra đồ thị “quá thưa” bất khả và “mọi người phải mang mẫu cục bộ dày từ danh sách.”

---

## 5. Discharging (động cơ thiết kế bởi người)

Discharging là lập luận phân phối lại cục bộ hữu hạn. Gán “điện tích” cho đỉnh và mặt—cổ điển liên quan công thức Euler

$$
V-E+F=2
$$

cho đồ thị phẳng liên thông—sao cho tổng điện tích là hằng dương đã biết. Rồi phân phối lại theo quy tắc cục bộ. Sau phân phối, mọi vị trí điện tích không âm chỉ nếu xuất hiện cấu hình dày nhất định; nếu không, một chỗ giữ điện âm—bất khả. Do đó một cấu hình trong danh sách thiết kế là không tránh được.

Thiết kế quy tắc discharging và danh sách cấu hình là thủ công tổ hợp sâu. Kiểm tra quy tắc chạy và mỗi cấu hình rút gọn được trở thành, lịch sử, núi trường hợp máy kiểm được—hàng trăm cấu hình ở Appel–Haken, danh sách đơn giản hơn ở Robertson–Sanders–Seymour–Thomas (1997), và cuối cùng chứng minh hình thức trong Coq (Gonthier và cộng sự).

---

## 6. Ý tưởng chứng minh, một trang

1. Viết lại tô màu bản đồ thành 4-tô màu đỉnh đồ thị phẳng.  
2. Giả sử phản ví dụ tối thiểu $$G$$.  
3. Trình bày tập không tránh được hữu hạn $$\mathcal{U}$$ (discharging + Euler).  
4. Chứng minh mỗi cấu hình trong $$\mathcal{U}$$ rút gọn được (phân tích trường hợp; có máy).  
5. Kết luận không có phản ví dụ tối thiểu; mọi đồ thị phẳng 4-tô màu được.

Insight người thiết kế $$\mathcal{U}$$ và discharging; máy (hoặc proof assistant) kiểm nổ trường hợp cục bộ.

---

## 7. Chứng minh có máy và verification sau

Thông báo Appel–Haken 1976 buộc tranh luận: case bash không đọc được có phải chứng minh? Dần dần cộng đồng chấp nhận chứng minh có máy khi:

- thuật toán được đặc tả rõ;  
- tính toán tái lập được về nguyên tắc;  
- kiểm tra độc lập và đơn giản hóa tích lũy.

Chứng minh 1997 giảm tập cấu hình và làm rõ cấu trúc. Chứng minh hình thức Coq của Georges Gonthier mã hóa lập luận để proof assistant kiểm mọi bước so với kernel logic nhỏ. Điều đó không làm định lý “chỉ về máy tính”; nó làm lập luận hữu hạn **kiểm toán được chặt**.

Đạo đức phương pháp cho khóa học: *ý tưởng chứng minh có thể gồm thiết kế một nhiệm vụ verification hữu hạn.*

---

## 8. Định lý *không* nói gì

- Không khẳng định mọi bản đồ trên mọi mặt đều 4-tô màu; giống thay đổi câu chuyện sắc (công thức Heawood cho giống cao hơn).  
- Không cho thuật toán thực tế nhanh nhất cho mọi instance.  
- Không nói mọi bản đồ *cần* bốn màu—chỉ bốn luôn đủ và ba không luôn đủ.  
- Không đồng nhất **Định lý Năm Màu**, có chứng minh cổ điển ngắn.

---

## Nhầm lẫn thường gặp

1. “Máy ngẫu nhiên kiểm bản đồ.” — Không: kiểm trường hợp rút gọn toán học cho cấu hình trong danh sách hữu hạn.  
2. “Người không chứng minh gì.” — Người thiết kế discharging, không tránh được, rút gọn được.  
3. “Bốn màu cho đồ thị phẳng nghĩa là bốn cho mọi đồ thị.” — Sai hoàn toàn; đồ thị không phẳng có thể cần tùy ý nhiều màu.  
4. “Nước chạm tại một điểm phải khác màu.” — Phát biểu chuẩn dùng đoạn biên, không chạm điểm.  
5. “Ý tưởng chứng minh = bỏ checklist hữu hạn.” — Checklist *là* xương sống; “ý tưởng” nghĩa là hiểu vì sao checklist chạy.

---

## Bài tập

1. Giải thích dual: vì sao tô màu bản đồ thành tô màu đỉnh đồ thị phẳng.  
2. Chỉ ra $$K_4$$ phẳng và cần 4 màu; vì sao điều đó liên quan sắc nét.  
3. Vì sao phản ví dụ tối thiểu giúp? Năm câu.  
4. Tự định nghĩa tập không tránh được và cấu hình rút gọn được.  
5. Tra (bên ngoài) số cấu hình Appel–Haken vs Robertson et al.; ghi số và một câu vì sao giảm danh sách quan trọng.  
6. **Triết (≤250 từ).** Khi nào chứng minh có máy chấp nhận được với bạn? Nêu một tiêu chí.  
7. **Narrative (≤350 từ).** Giải thích ý tưởng bốn màu cho bạn học—không liệt kê hết cấu hình.

---


---

## Kiến thức trích từ nghiên cứu video

Tóm tắt cho seminar (đối chiếu nguồn viết; **không bịa transcript**). Gói: `research/video-research/four-color-proof/analysis.md`.

### Trạng thái

**Proved** (Appel–Haken 1976; simplified/verified later, Robertson et al., computer-checked formalizations). Philosophical debate about computer proofs is separate from theorem status.

### Phát biểu / slogan cốt lõi

Every planar graph is 4-colorable (equivalently, every map on the plane/sphere can be colored with 4 colors so adjacent regions differ). Proof architecture: unavoidable set of reducible configurations + discharging.

### Định nghĩa cần cố định

- **Planar graph.** Graph drawable in the plane without edge crossings.
- **Reducible configuration.** Local pattern that cannot appear in a minimal counterexample.

### Vệ sinh khái niệm

- Thinking 4 colors are needed for *every* map (many need fewer; 4 is worst-case bound).
- Conflating 'computer-assisted' with 'unverified' after modern checks.


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh/bài báo gốc khi tuyên bố mang tính then chốt. Chi tiết xếp hạng: `research/video-research/four-color-proof/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile — Four Color Map Theorem (James Grime): [https://www.youtube.com/watch?v=NgbK43jB4rQ](https://www.youtube.com/watch?v=NgbK43jB4rQ).  
2. **Cốt lõi** — Quanta — Math's Map Coloring Problem / first computer-assisted proof: [https://www.youtube.com/watch?v=h7kqlYUV1l8](https://www.youtube.com/watch?v=h7kqlYUV1l8).  
3. **Vệ sinh khái niệm** — Up and Atom — Four Color Theorem: What Counts as a Proof?: [https://www.youtube.com/watch?v=42-ws3bkrKM](https://www.youtube.com/watch?v=42-ws3bkrKM).  
4. **Phụ** — Numberphile2 — Four Color extra footage: [https://www.youtube.com/watch?v=laMkuPrad3s](https://www.youtube.com/watch?v=laMkuPrad3s).  

**Nhắc trạng thái:** **Proved** (Appel–Haken 1976; simplified/verified later, Robertson et al., computer-checked formalizations). Philosophical debate about computer proofs is separate from theorem status.

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/four-color-proof/transcripts/` · trạng thái: `research/video-research/four-color-proof/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/four-color-proof_NgbK43jB4rQ_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

1. Appel & Haken (1977). Every planar map is four colorable.  
2. Robertson, Sanders, Seymour, Thomas (1997). The four-colour theorem.  
3. Gonthier — formal proof (Coq) của Định lý Bốn Màu.  
4. Sử về nỗ lực Kempe và định lý năm màu Heawood.  
5. Khóa học: [Euler–Königsberg]({{ site.baseurl }}/contents/vi/chapter05/05_05_Euler_Konigsberg/).

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

- Đọc triển khai discharging với tập không tránh được đồ chơi nhỏ.  
- Khám phá số sắc trên torus và mặt khác.  
- Thử cách proof assistant mã hóa phân nhánh trường hợp hữu hạn.  
- Ghi một câu hỏi chính xác bạn vẫn còn.
