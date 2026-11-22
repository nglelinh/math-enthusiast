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

Ở Königsberg thế kỷ XVIII (nay là Kaliningrad), bảy cây cầu nối hai hòn đảo và hai bờ sông Pregel. Người dân đặt ra một câu hỏi giải trí, và từ đó sinh ra một nhánh toán học nghiêm túc: *có đường đi qua thành phố sao cho mỗi cây cầu được đi qua đúng một lần không?* **Leonhard Euler** chứng minh rằng không có đường đi như vậy, và qua đó góp phần khai sinh **lý thuyết đồ thị**. Hình dạng của dòng sông hầu như không quan trọng; điều quan trọng là các khối đất nối với nhau như thế nào. Bài này trình bày **ý tưởng chứng minh**: lập mô hình, quy về bậc, rồi đọc ra điều cản trở.

Bài học này vượt xa một thành phố. Mỗi khi một bài toán thực chất chỉ nói về việc cái gì nối với cái gì và việc đi qua chúng (mạng máy tính, mạch điện, định tuyến), ta có thể làm theo cách của Königsberg: bỏ phần hình học thừa, giữ lại bộ khung tổ hợp, rồi lập luận bằng tính chẵn lẻ.

---

## Mục tiêu học tập

Sau bài này, bạn có thể:

- Mô hình một hệ thống cầu (hoặc đường) thành đa đồ thị, với đỉnh là các vùng đất và cạnh là các lối đi giữa chúng.
- Định nghĩa đường Euler và chu trình Euler, và nêu tiêu chuẩn về bậc.
- Áp dụng vào bốn đỉnh bậc lẻ của Königsberg và kết luận không thể có đường đi như vậy.
- Giải thích vì sao đây là một chứng minh bằng mô hình hóa: trừu tượng hóa là bước toán học đầu tiên.
- Dựng một ví dụ nhỏ *có* đường Euler và so với Königsberg.
- Nối ý tưởng này với cách suy luận về mạng hiện đại.

**Kiến thức cần có.** Biết vẽ sơ đồ, tính chẵn lẻ của số nguyên, và khái niệm đường đi là dãy các cạnh kề nhau. Không cần học lý thuyết đồ thị trước.

---

## 1. Câu đố lịch sử

Bố cục Königsberg có thể phác thành bốn vùng đất với bảy cây cầu. Các bản đồ lịch sử đặt tên khác nhau, nhưng dữ liệu tổ hợp thì không đổi: **bốn vùng đất, bảy cây cầu, và bốn đỉnh bậc lẻ** trong mô hình tự nhiên.

Câu đố này không hỏi về quãng đường ngắn nhất. Đó là một câu hỏi thuần túy về sự tồn tại: **có thể đi qua mỗi cây cầu đúng một lần không?** Bài báo năm 1736 của Euler thường được xem là văn bản đặt nền móng cho lý thuyết đồ thị, và cũng cho khía cạnh tổ hợp của tôpô: những tính chất vẫn giữ nguyên khi ta bỏ qua hình dạng.

---

## 2. Ý tưởng lập mô hình

Thay mỗi khối đất bằng một **đỉnh**. Thay mỗi cây cầu bằng một **cạnh** nối các đỉnh tương ứng. Nhiều cầu giữa cùng một cặp vùng đất trở thành **cạnh bội**. Thành phố trở thành một **đa đồ thị** $$G=(V,E)$$.

Một đường đi qua mỗi cầu đúng một lần trở thành đường đi dùng mỗi cạnh đúng một lần, gọi là **đường Euler**. Nếu điểm xuất phát và điểm kết thúc trùng nhau thì đó là **chu trình Euler**.

![Cầu Königsberg]({{ site.baseurl }}/img/chapter_img/konigsberg_bridges.svg)

*Hình. Sơ đồ: khối đất là đỉnh, cây cầu là cạnh. (Nếu không thấy ảnh, hãy tự vẽ bốn chấm và bảy đoạn nối theo sơ đồ Königsberg chuẩn.)*

**Mô hình bỏ đi những gì.** Khoảng cách, góc, độ rộng của cầu, cách vẽ lên mặt phẳng.
**Mô hình giữ lại những gì.** Quan hệ liên thuộc: vùng đất nào có cầu nào, và bao nhiêu cầu.

Bước bỏ bớt và giữ lại này chính là phần toán học của bài toán. Người nào cố giải Königsberg bằng cách vẽ bản đồ thành phố ngày càng chi tiết là đang làm việc ở sai cấp độ.

---

### Video ngắn: bảy cây cầu như một đồ thị

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/konigsberg-bridges_vi.mp4"></video>
</div>

Biến vùng đất thành điểm và cây cầu thành cạnh, rồi đếm bậc của mỗi điểm. Bốn điểm bậc lẻ loại trừ khả năng có đường đi qua mỗi cầu đúng một lần.


### Tự tay thử: đi qua các cây cầu

<div class="mex-explainer" data-mex="konigsberg" data-lang="vi"></div>


## 3. Bậc và cản trở về tính chẵn lẻ

**Bậc** $$\deg(v)$$ là số đầu mút của các cạnh tại $$v$$ (cạnh bội được đếm nhiều lần).

### Điều kiện cần, xét tại từng đỉnh

Hãy hình dung ta đi trong đồ thị và dùng mỗi cạnh đúng một lần. Mỗi lần đi qua một đỉnh, ta vào bằng một cạnh và ra bằng cạnh khác, nên dùng hết **hai** đầu mút. Xét toàn đồ thị:

- Trong **chu trình Euler**, mọi đỉnh phải có **bậc chẵn**.
- Trong **đường Euler** không đóng, có đúng **hai** đỉnh bậc lẻ, là điểm đầu và điểm cuối. Mọi đỉnh khác đều có bậc chẵn.

Các điều kiện này không chỉ cần mà với đồ thị liên thông còn là đủ (định lý cổ điển). Với Königsberg, chỉ cần tính bậc là đã loại bỏ hy vọng.

### Bậc ở Königsberg

Trong mô hình chuẩn của bảy cây cầu, cả bốn đỉnh đều có bậc lẻ (ba đỉnh bậc 3 và một đỉnh bậc 5). Một đồ thị liên thông có nhiều hơn hai đỉnh bậc lẻ thì không thể có đường Euler. Vậy không có đường đi nào qua mỗi cầu đúng một lần.

Có thể nhớ theo Euler: *đếm số đỉnh bậc lẻ; nếu nhiều hơn hai thì dừng.*

---

## 4. Ý tưởng chứng minh, nói gọn

1. **Lập mô hình** đất và cầu thành một đa đồ thị.
2. **Dịch** yêu cầu "đi qua mỗi cầu một lần" thành việc tồn tại đường Euler.
3. **Suy ra** ràng buộc về tính chẵn lẻ của bậc từ việc ghép cặp lượt vào và lượt ra.
4. **Tính** bậc của các đỉnh ở Königsberg và thấy có bốn đỉnh bậc lẻ.
5. **Kết luận** là không thể.

Không cần hình học tọa độ, không cần chuyển động liên tục. Đây là chứng minh tổ hợp: một đại lượng bất biến chặn mọi đường đi cùng một lúc.

---

## 5. Đối chiếu với các ví dụ

### Đồ thị đi được

Chu trình hình vuông có bốn đỉnh, bốn cạnh, mọi đỉnh bậc 2, nên có chu trình Euler.
Thêm một đường chéo thì hai đỉnh có bậc 3; khi đó có đường Euler đi từ đỉnh lẻ này sang đỉnh lẻ kia, nhưng không có chu trình Euler.

### Đồ thị hỏng như Königsberg

Mọi đồ thị liên thông có bốn đỉnh bậc lẻ đều không thỏa tiêu chuẩn của đường Euler. Ta không cần thử từng đường đi; bất biến này đã cấm tất cả. Đó là sức mạnh của một chứng minh bất khả thi.

### Bổ đề bắt tay

$$
\sum_{v\in V}\deg(v)=2\lvert E\rvert.
$$

Số đỉnh bậc lẻ luôn là số chẵn. Bốn đỉnh bậc lẻ không mâu thuẫn với bổ đề, và vẫn không có đường Euler phủ mọi cạnh.

---

## 6. Điều kiện đủ, nói ngắn gọn

<div class="textbook-theorem" markdown="1">
**Định lý (cổ điển, ở mức ý tưởng).** Cho $$G$$ là một đa đồ thị liên thông. Khi đó:

- có chu trình Euler khi và chỉ khi mọi đỉnh có bậc chẵn;
- có đường Euler khi và chỉ khi có đúng không hoặc hai đỉnh bậc lẻ.
</div>

**Ý tưởng cho điều kiện đủ.** Bắt đầu từ một đỉnh bậc lẻ nếu có, đi theo các cạnh chưa dùng cho đến khi không đi tiếp được; chứng minh rằng ta dừng đúng ở chỗ cần dừng; nếu còn cạnh chưa đi, ghép thêm các chu trình vào (thuật toán Hierholzer). Điều cần nhớ: điều kiện về bậc mới là cốt lõi.

---

## 7. Vì sao quan trọng

- **Khai sinh lý thuyết đồ thị.** Một bài toán về mạng lưới trở thành định lý về đỉnh và cạnh.
- **Khía cạnh tổ hợp của tôpô.** Tính chất không đổi khi biến dạng liên tục bờ sông.
- **Thuật toán.** Đường Euler xuất hiện trong lắp ráp bộ gen, định tuyến, và bài toán vẽ một nét không nhấc bút.
- **Cách làm toán.** Chứng minh bất khả thi bằng bất biến (tính chẵn lẻ của bậc) là một mẫu hình: tìm một đại lượng mà mọi đối tượng thành công đều phải có, rồi chỉ ra trường hợp đang xét không có nó.

---

## 8. Ngoài những cây cầu: bài toán người đưa thư Trung Hoa

Nếu mọi đỉnh có bậc chẵn, chu trình Euler là một lộ trình đưa thư hoàn hảo. Nếu có đỉnh bậc lẻ, **bài toán người đưa thư Trung Hoa** hỏi đường đi khép kín ngắn nhất phủ mọi cạnh ít nhất một lần. Bài toán này tương đương với việc thêm các cạnh lặp lại với tổng chi phí nhỏ nhất để ghép cặp các đỉnh bậc lẻ, rồi chạy chu trình Euler. Königsberg là trường hợp cấm đi lặp và chỉ hỏi về sự tồn tại. Một kết quả phủ định cổ điển như vậy đã mở đường cho cả lý thuyết tối ưu hóa.

---

## Nhầm lẫn thường gặp

1. "Euler chứng minh không thể thăm hết mọi khối đất." Sai mục tiêu: bài toán yêu cầu phủ **cầu (cạnh)**, không phải đỉnh. Đường Hamilton là chuyện khác hẳn.
2. "Vẽ bản đồ kỹ hơn có thể tìm ra đường đi." Cản trở này không đổi khi vẽ lại.
3. "Có đỉnh bậc lẻ nghĩa là đồ thị không liên thông." Không phải.
4. "Bốn đỉnh bậc lẻ mâu thuẫn với bổ đề bắt tay." Không; bốn là số chẵn.
5. "Ý tưởng chứng minh nghĩa là bỏ qua định nghĩa đường đi." Vẫn cần định nghĩa rõ; chỉ bỏ phần hình học đo đạc.

---

## Bài tập

1. Vẽ đa đồ thị Königsberg, ghi bậc từng đỉnh, và viết chứng minh không thể đi qua mỗi cầu một lần trong ba câu.
2. Tự dựng một đa đồ thị liên thông có đúng hai đỉnh bậc lẻ và chỉ ra một đường Euler.
3. Chứng minh số đỉnh bậc lẻ luôn chẵn từ $$\sum\deg=2\lvert E\rvert$$.
4. Có đồ thị nào có đúng một đỉnh bậc lẻ không? Vì sao?
5. Phân biệt đường Euler với đường Hamilton; cho một đồ thị nhỏ có đường này mà không có đường kia.
6. **Mô hình hóa.** Chuyển sơ đồ các hành lang của một tòa nhà thành đồ thị sao cho "đi qua mỗi hành lang đúng một lần" trở thành câu hỏi về đường Euler.
7. **Viết tự luận (không quá 300 từ).** Giải thích cho một du khách vì sao không có lộ trình đi qua mỗi cầu một lần, không dùng từ "định lý".

---

## Kiến thức rút ra từ phần tìm hiểu video

Tóm tắt dùng khi thảo luận (đối chiếu với nguồn viết; **không bịa nội dung transcript**). Gói: `research/video-research/euler-konigsberg/analysis.md`.

### Tình trạng

**Đã được chứng minh** (Euler, 1736, điều kiện cần; tính đủ của tiêu chuẩn Euler được hoàn thành về sau, bởi Hierholzer). Đây là định lý khai sinh lý thuyết đồ thị.

### Phát biểu cốt lõi

Một đồ thị liên thông có chu trình Euler khi và chỉ khi mọi đỉnh có bậc chẵn; có đường Euler khi và chỉ khi có đúng 0 hoặc 2 đỉnh bậc lẻ. Đa đồ thị Königsberg có bốn đỉnh bậc lẻ, nên không thể.

### Các định nghĩa cần nắm chắc

- **Bậc.** Số đầu mút cạnh tại một đỉnh (khuyên được tính 2).
- **Chu trình / đường Euler.** Đường đi đóng / mở dùng mỗi cạnh đúng một lần.

### Những hiểu lầm cần tránh

- Nghĩ rằng đáp án phụ thuộc vào độ dài cầu hay hình học (chỉ quan hệ liên thuộc mới quan trọng).
- Lẫn đường Hamilton (qua mỗi đỉnh một lần) với đường Euler (qua mỗi cạnh một lần).


---

## Nguồn video (gói math-video-researcher)

Dùng video để **định hướng và làm quen với cách nghiên cứu**, không thay cho chứng minh hay bài báo gốc khi cần khẳng định quan trọng. Chi tiết xếp hạng: `research/video-research/euler-konigsberg/`.

**Thứ tự gợi ý**

1. **Định hướng** — Numberphile — Seven Bridges of Königsberg (Cliff Stoll): [https://www.youtube.com/watch?v=W18FDEA1jRQ](https://www.youtube.com/watch?v=W18FDEA1jRQ).  
2. **Định hướng** — TED-Ed — How the Königsberg bridge problem changed mathematics: [https://www.youtube.com/watch?v=nZwSo4vfw6c](https://www.youtube.com/watch?v=nZwSo4vfw6c).  
3. **Nền tảng** — Sarada Herke — Graph Theory: Seven Bridges of Konigsberg: [https://www.youtube.com/watch?v=eIb1cz06UwI](https://www.youtube.com/watch?v=eIb1cz06UwI).  
4. **Cốt lõi** — Dr. Trefor Bazett — Euler Paths & 7 Bridges: [https://www.youtube.com/watch?v=dSK5jTEe-AM](https://www.youtube.com/watch?v=dSK5jTEe-AM).  

**Nhắc tình trạng:** **Đã được chứng minh** (Euler, 1736, điều kiện cần; tính đủ được hoàn thành về sau, bởi Hierholzer). Đây là định lý khai sinh lý thuyết đồ thị.

---


### Transcript và khung hình (trích theo lô)

Transcript caption và unit theo thời gian: `research/video-research/euler-konigsberg/transcripts/` · trạng thái: `research/video-research/euler-konigsberg/TRANSCRIPT_STATUS.md` · danh sách master: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/euler-konigsberg_W18FDEA1jRQ_thumb.jpg)

*Hình. Khung hình mẫu từ video chính của gói (xem gói nghiên cứu để biết mốc thời gian).*

## Tài liệu

1. Euler (1736), bài báo về các cây cầu ở Königsberg.
2. Sách nhập môn lý thuyết đồ thị: mục về đường Euler.
3. Các bài lịch sử về đồ thị và tôpô thuở đầu.
4. Trong khóa học: [Bốn màu]({{ site.baseurl }}/contents/vi/chapter05/05_07_Four_Color_Proof/) (đồ thị phẳng).

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

- Đọc thuật toán Hierholzer và cài đặt trên một đa đồ thị nhỏ.
- Tìm hiểu bài toán người đưa thư Trung Hoa như phần nối tiếp về tối ưu hóa.
- So sánh đường đi qua mọi cạnh với đường đi qua mọi đỉnh (Hamilton) để thấy độ phức tạp tăng vọt.
- Ghi lại một câu hỏi chính xác mà bạn vẫn còn thắc mắc.


## Từ cầu Königsberg đến bất biến của đồ thị

Euler không "vẽ bản đồ đẹp hơn", ông **đổi ngôn ngữ** sang đỉnh, cạnh và bậc. Điều kiện cho chu trình Euler (đồ thị liên thông, mọi bậc chẵn) là một mẫu mực của chứng minh tổ hợp: một bất biến địa phương (bậc) kiểm soát khả năng toàn cục (có chu trình).

## Cầu nối hiện đại

Cùng thói quen "mô hình hóa bằng đồ thị" nằm sau [mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), định lý bốn màu, và bài thực hành tô màu bản đồ. Khác biệt: Königsberg hỏi về sự tồn tại của một đường đi, còn bốn màu là ràng buộc về màu của các miền.

## Bài thực hành

Vẽ một đồ thị 6 đỉnh có đúng hai đỉnh bậc lẻ; chỉ ra đường Euler mở (nếu có) hoặc giải thích vì sao không có chu trình Euler đóng. Viết một đoạn: vì sao "đi hết các cầu" là bài toán đồ thị chứ không phải bài toán hình học đo đạc của dòng sông.


## Video tham khảo

- **Xem trước** — [The Seven Bridges of Königsberg - Numberphile](https://www.youtube.com/watch?v=W18FDEA1jRQ) — Numberphile, tiếng Anh. Video định hướng cho mục tiêu của bài: mô hình hệ thống cầu thành đa đồ thị.
- [How the Königsberg bridge problem changed mathematics - Dan Van der Vieren](https://www.youtube.com/watch?v=nZwSo4vfw6c) — TED-Ed, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ.
- [Graph Theory: 01. Seven Bridges of Konigsberg](https://www.youtube.com/watch?v=eIb1cz06UwI) — Sarada Herke, tiếng Anh. Góc nhìn bổ sung sau hai video đầu.
