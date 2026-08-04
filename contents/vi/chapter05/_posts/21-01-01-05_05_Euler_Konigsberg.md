---
layout: post
title: "Euler và Bảy Cầu Königsberg"
chapter: '05'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter05
---

Ở Königsberg thế kỷ XVIII (nay là Kaliningrad), bảy cây cầu nối hai đảo và hai bờ sông Pregel. Người dân hỏi một câu giải trí sinh ra hậu duệ toán học nghiêm túc: *Có đường đi qua thành phố sao cho mỗi cầu đúng một lần không?* **Leonhard Euler** chứng minh không tồn tại—và nhờ đó góp phần khai sinh **lý thuyết đồ thị**. Hình học dòng sông gần như không quan trọng; quan trọng là các khối đất nối nhau thế nào. Bài này phát triển **ý tưởng chứng minh**: mô hình hóa, quy về bậc, đọc ra cản trở.

Đạo đức đi xa hơn một thành phố. Mỗi khi bài toán thật sự về liên thuộc và duyệt—mạng, mạch, định tuyến—động tác Königsberg sẵn sàng: bỏ hình học thừa, giữ skeleton tổ hợp, suy luận về parity.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Mô hình hệ cầu (hoặc đường) thành đa đồ thị với đỉnh là vùng, cạnh là lối băng.
- Định nghĩa đường Euler và chu trình Euler; nêu tiêu chuẩn bậc cổ điển.
- Áp dụng cho bốn đỉnh bậc lẻ của Königsberg và kết luận bất khả.
- Giải thích vì sao đây là chứng minh bằng mô hình hóa: trừu tượng hóa là hành vi toán học đầu tiên.
- Dựng ví dụ nhỏ *có* tour Euler và đối chiếu với Königsberg.
- Nối ý tưởng với suy luận mạng hiện đại ở mức khẩu hiệu.

**Tiên quyết.** Vẽ sơ đồ; parity số nguyên; ý tưởng đường đi như dãy cạnh kề. Không cần khóa lý thuyết đồ thị trước.

---

## 1. Câu đố lịch sử

Bố cục Königsberg có thể phác thành bốn vùng đất với bảy cầu. Bản đồ lịch sử gán nhãn khác nhau; dữ liệu tổ hợp ổn định: **bốn vùng, bảy cầu, và bốn đỉnh bậc lẻ** trong mô hình tự nhiên.

Thách thức giải trí không phải cực tiểu khoảng cách. Đó là câu hỏi tồn tại thuần về **duyệt mỗi cầu một lần**. Memoir 1736 của Euler thường được trích như văn kiện sáng lập lý thuyết đồ thị và mặt tổ hợp của tôpô: tính chất bảo toàn khi bỏ qua hình dạng.

---

## 2. Ý tưởng mô hình hóa

Thay mỗi khối đất bằng một **đỉnh**. Thay mỗi cầu bằng một **cạnh** nối các đỉnh tương ứng. Nhiều cầu giữa cùng một cặp trở thành **đa cạnh**. Thành phố thành **đa đồ thị** $$G=(V,E)$$.

Đường đi qua mỗi cầu đúng một lần thành đường đi dùng mỗi cạnh đúng một lần: **đường Euler** (Eulerian path/trail). Nếu xuất phát và kết thúc cùng đỉnh: **chu trình Euler**.

![Cầu Königsberg]({{ site.baseurl }}/img/chapter_img/konigsberg_bridges.svg)

*Hình. Sơ đồ: đất là đỉnh, cầu là cạnh. (Nếu thiếu ảnh cục bộ, vẽ bốn chấm và bảy nối theo sơ đồ Königsberg chuẩn.)*

**Mô hình bỏ gì.** Khoảng cách, góc, độ rộng cầu, nhúng phẳng ngoài liên thông.  
**Mô hình giữ gì.** Liên thuộc: vùng nào gặp cầu nào, bao nhiêu lần.

Bước bỏ-và-giữ *chính là* toán học. Ai cố giải Königsberg bằng bản đồ thành phố ngày càng chi tiết đang làm việc ở category sai.

---

## 3. Bậc và cản trở parity

**Bậc** $$\deg(v)$$ là số đầu mút cạnh tại $$v$$ (đếm bội).

### Điều kiện cần địa phương

Hình dung đi trong đồ thị dùng mỗi cạnh một lần. Mỗi lần vào đỉnh bằng một cạnh và ra bằng cạnh khác, tiêu thụ **hai** đầu mút. Toàn cục:

- Trong **chu trình Euler**, mọi đỉnh phải **bậc chẵn**.  
- Trong **đường Euler** không đóng, đúng **hai** đỉnh có thể bậc lẻ—điểm đầu và điểm cuối. Mọi đỉnh khác bậc chẵn.

Các điều kiện không chỉ cần mà, với đồ thị liên thông, về cơ bản đủ (định lý cổ điển). Với Königsberg, **chỉ cần tính** đã giết hy vọng.

### Bậc ở Königsberg

Trong mô hình chuẩn bảy cầu, cả bốn đỉnh đều bậc lẻ (thường ba đỉnh bậc 3 và một bậc 5, hoặc bộ bậc lẻ tương đương—quan trọng là **bốn bậc lẻ**). Đồ thị liên thông không thể có đường Euler nếu có hơn hai đỉnh bậc lẻ. Vậy không có đường đi qua mỗi cầu đúng một lần.

Khẩu hiệu Euler: *đếm đỉnh lẻ; nếu hơn hai, dừng.*

---

## 4. Ý tưởng chứng minh, nén

1. **Mô hình** đất và cầu thành đa đồ thị.  
2. **Dịch** yêu cầu du lịch thành tồn tại đường Euler.  
3. **Suy** ràng buộc parity bậc từ ghép vào/ra.  
4. **Tính** bậc Königsberg; thấy bốn bậc lẻ.  
5. **Kết luận** bất khả.

Không hình học tọa độ, không chuyển động liên tục. Chứng minh tổ hợp: bất biến chặn mọi đường đi cùng lúc.

---

## 5. Đối chiếu ví dụ

### Đồ thị chạy được

Chu trình vuông: bốn đỉnh, bốn cạnh, mọi bậc 2—có chu trình Euler.  
Thêm một đường chéo: hai đỉnh bậc 3; có đường Euler từ đỉnh lẻ này sang đỉnh lẻ kia, không có chu trình Euler.

### Đồ thị hỏng như Königsberg

Mọi đồ thị liên thông bốn đỉnh bậc lẻ thất bại tiêu chuẩn đường. Không cần duyệt mọi walk; bất biến cấm tất cả—đó là sức mạnh chứng chỉ bất khả.

### Bổ đề bắt tay

$$
\sum_{v\in V}\deg(v)=2\lvert E\rvert.
$$

Số đỉnh bậc lẻ luôn chẵn. Bốn đỉnh lẻ hợp lệ với bổ đề—và vẫn không Euler cho trail phủ mọi cạnh.

---

## 6. Tính đủ, ngắn gọn

**Định lý (cổ điển, ý tưởng).** Cho $$G$$ đa đồ thị liên thông. Thì:

- có chu trình Euler khi và chỉ khi mọi bậc chẵn;  
- có đường Euler khi và chỉ khi đúng không hoặc hai đỉnh bậc lẻ.

**Ý tưởng tính đủ.** Bắt đầu tại đỉnh lẻ nếu có; đi cạnh chưa dùng đến khi kẹt; chứng minh dừng đúng chỗ; nếu còn cạnh, ghép thêm chu trình (Hierholzer). Seminar giữ: điều kiện bậc là trái tim thật.

---

## 7. Vì sao quan trọng

- **Khai sinh lý thuyết đồ thị.** Bài toán mạng thành định lý về đỉnh và cạnh.  
- **Mặt tổ hợp của tôpô.** Tính chất độc lập biến dạng liên tục bờ sông.  
- **Thuật toán.** Tour Euler xuất hiện trong slogan lắp ráp genome, định tuyến, máy vẽ không nhấc bút.  
- **Văn hóa chứng minh.** Bất khả qua bất biến (parity bậc) là mẫu: tìm đại lượng mọi đối tượng thành công phải có; chỉ ra thể hiện thiếu nó.

---

## 8. Ngoài cầu: Chinese Postman

Nếu mọi bậc chẵn, chu trình Euler là tour bưu chính hoàn hảo. Nếu có bậc lẻ, **bài toán người đưa thư Trung Hoa** hỏi walk đóng ngắn nhất phủ mọi cạnh ít nhất một lần—tương đương thêm cạnh trùng chi phí tối thiểu để ghép đỉnh lẻ, rồi chạy chu trình Euler. Königsberg là trường hợp cấm trùng và hỏi tồn tại. Phủ định cổ điển gieo lý thuyết tối ưu dương.

---

## Nhầm lẫn thường gặp

1. “Euler chứng minh không thăm được mọi khối đất.” — Sai mục tiêu: phủ **cầu (cạnh)**, không phải đỉnh. Đường Hamilton khác hẳn.  
2. “Vẽ bản đồ cẩn hơn có thể ra đường.” — Cản trở bất biến dưới vẽ lại.  
3. “Bậc lẻ nghĩa là không liên thông.” — Không.  
4. “Bốn đỉnh lẻ mâu thuẫn bổ đề bắt tay.” — Không; bốn là chẵn.  
5. “Ý tưởng chứng minh = bỏ định nghĩa walk.” — Vẫn cần định nghĩa rõ; chỉ bỏ hình học metric.

---

## Bài tập

1. Vẽ đa đồ thị Königsberg, ghi bậc, viết chứng minh bất khả ba câu.  
2. Bịa đa đồ thị liên thông đúng hai đỉnh bậc lẻ và chỉ ra đường Euler.  
3. Chứng minh số đỉnh bậc lẻ luôn chẵn từ $$\sum\deg=2\lvert E\rvert$$.  
4. Có đồ thị đúng một đỉnh bậc lẻ không? Vì sao?  
5. Phân biệt đường Euler vs đường Hamilton; cho đồ thị nhỏ có cái này không cái kia.  
6. **Mô hình hóa.** Dịch mặt bằng hành lang thành đồ thị sao cho “đi mỗi hành lang một lần” thành câu hỏi Euler.  
7. **Narrative (≤300 từ).** Giải thích cho khách du lịch vì sao không có tour cầu—không dùng từ “định lý.”

---


---

## Kiến thức trích từ nghiên cứu video

Tóm tắt cho seminar (đối chiếu nguồn viết; **không bịa transcript**). Gói: `research/video-research/euler-konigsberg/analysis.md`.

### Trạng thái

**Proved** (Euler 1736 necessity; full sufficiency of Eulerian criteria completed later, Hierholzer). Founding theorem of graph theory.

### Phát biểu / slogan cốt lõi

A connected graph has an Eulerian circuit iff every vertex has even degree; an Eulerian trail iff exactly 0 or 2 odd-degree vertices. Königsberg multigraph has four odd vertices → impossible.

### Định nghĩa cần cố định

- **Degree.** Number of edge ends at a vertex (loops contribute 2).
- **Eulerian circuit / trail.** Closed / open walk using each edge exactly once.

### Vệ sinh khái niệm

- Thinking the answer depends on bridge lengths or geometry (only incidence matters).
- Mixing Hamiltonian (vertices once) with Eulerian (edges once).


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và văn hóa nghiên cứu**, không thay chứng minh/bài báo gốc khi tuyên bố mang tính then chốt. Chi tiết xếp hạng: `research/video-research/euler-konigsberg/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile — Seven Bridges of Königsberg (Cliff Stoll): [https://www.youtube.com/watch?v=W18FDEA1jRQ](https://www.youtube.com/watch?v=W18FDEA1jRQ).  
2. **Định hướng** — TED-Ed — How the Königsberg bridge problem changed mathematics: [https://www.youtube.com/watch?v=nZwSo4vfw6c](https://www.youtube.com/watch?v=nZwSo4vfw6c).  
3. **Nền tảng** — Sarada Herke — Graph Theory: Seven Bridges of Konigsberg: [https://www.youtube.com/watch?v=eIb1cz06UwI](https://www.youtube.com/watch?v=eIb1cz06UwI).  
4. **Cốt lõi** — Dr. Trefor Bazett — Euler Paths & 7 Bridges: [https://www.youtube.com/watch?v=dSK5jTEe-AM](https://www.youtube.com/watch?v=dSK5jTEe-AM).  

**Nhắc trạng thái:** **Proved** (Euler 1736 necessity; full sufficiency of Eulerian criteria completed later, Hierholzer). Founding theorem of graph theory.

---


### Transcript & frames (batch extract)

Transcript caption và unit theo thời gian: `research/video-research/euler-konigsberg/transcripts/` · trạng thái: `research/video-research/euler-konigsberg/TRANSCRIPT_STATUS.md` · master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/euler-konigsberg_W18FDEA1jRQ_thumb.jpg)

*Hình. Frame mẫu từ video chính của gói (xem pack cho timestamp).*

## Tài liệu

1. Euler (1736), memoir về cầu Königsberg.  
2. Sách nhập môn lý thuyết đồ thị: mục đường Euler.  
3. Bài sử về đồ thị và tôpô sơ khai.  
4. Khóa học: [Bốn màu]({{ site.baseurl }}/contents/vi/chapter05/05_07_Four_Color_Proof/) (đồ thị phẳng).

---


Danh mục URL đầy đủ: `research/video-research/euler-konigsberg/references.md`.

### Video (lộ trình gợi ý)

- Numberphile — Seven Bridges of Königsberg (Cliff Stoll) (ORIENTATION): https://www.youtube.com/watch?v=W18FDEA1jRQ
- TED-Ed — How the Königsberg bridge problem changed mathematics (ORIENTATION): https://www.youtube.com/watch?v=nZwSo4vfw6c
- Sarada Herke — Graph Theory: Seven Bridges of Konigsberg (FOUNDATION): https://www.youtube.com/watch?v=eIb1cz06UwI
- Dr. Trefor Bazett — Euler Paths & 7 Bridges (CORE): https://www.youtube.com/watch?v=dSK5jTEe-AM

### Bài báo và web (từ gói nghiên cứu)

- Wikipedia — Seven Bridges of Königsberg: https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg
- MathWorld — Königsberg Bridge Problem: https://mathworld.wolfram.com/KoenigsbergBridgeProblem.html
- Euler 1736 paper (historical translations / surveys): https://en.wikipedia.org/wiki/Leonhard_Euler
- Mathigon course — Bridges of Königsberg: https://mathigon.org/course/graph-theory/bridges
- Numberphile page: https://www.numberphile.com/videos/the-seven-bridges-of-knigsberg

### Khóa học

- Gói: `research/video-research/euler-konigsberg/` (đặc biệt `references.md`, `learning_path.md`).

## Hướng đi tiếp

- Đọc thuật toán Hierholzer và cài trên đa đồ thị nhỏ.  
- Khám phá Chinese Postman như phần tiếp tối ưu.  
- Tương phản tour cạnh với tour đỉnh (Hamilton) để cảm nhận nhảy độ phức tạp.  
- Ghi một câu hỏi chính xác bạn vẫn còn.


## Từ cầu Königsberg đến bất biến đồ thị

Euler không “vẽ bản đồ đẹp hơn”—ông **đổi ngôn ngữ**: đỉnh, cạnh, bậc. Điều kiện chu trình Euler (đồ thị liên thông, mọi bậc chẵn) là mẫu mực của chứng minh tổ hợp: bất biến địa phương (bậc) kiểm soát khả năng toàn cục (chu trình).

## Cầu nối hiện đại

Cùng thói quen “mô hình hóa bằng đồ thị” nuôi [mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), định lý bốn màu, và studio tô màu bản đồ. Khác biệt: Königsberg là tồn tại đường đi; four color là ràng buộc màu mặt.

## Studio

Vẽ một đồ thị 6 đỉnh có đúng hai đỉnh bậc lẻ; chỉ ra đường Euler mở (nếu có) hoặc giải thích vì sao không có chu trình Euler đóng. Viết một đoạn: vì sao “đi hết cầu” là bài toán đồ thị chứ không phải hình học metric của sông.

