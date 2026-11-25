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

Vào những buổi chiều Chủ nhật thế kỷ XVIII ở thành phố Königsberg bên dòng sông Pregel (nay là Kaliningrad), người dân có một thú tiêu khiển quen thuộc: vừa tản bộ vừa đánh cược xem có ai tìm ra được lộ trình **đi qua cả bảy cây cầu của thành phố, mỗi cây cầu đúng một lần** hay không. Nhiều người đã đi mòn gót giày, vẽ chi chít bản đồ, thử hết đường này sang ngõ nọ nhưng lần nào cũng bị kẹt ở cây cầu cuối cùng — hoặc buộc phải quay lại một cây cầu đã đi qua.

Khi câu đố ấy được gửi đến **Leonhard Euler** ở St. Petersburg, ban đầu ông nghĩ đây chỉ là một trò tiêu khiển tầm thường không dính dáng gì đến toán học. Nhưng rồi Euler chợt nhận ra: ta chẳng cần đặt chân tới Königsberg, cũng chẳng cần biết cây cầu nào dài bao nhiêu mét hay dòng sông uốn lượn ra sao. Bằng cách **vứt bỏ toàn bộ hình học đo đạc** để chỉ giữ lại các chấm và đoạn nối, Euler không chỉ chứng minh câu đố là bất khả thi vào năm 1736, mà còn khai sinh ra cả một ngành toán học hoàn toàn mới: **lý thuyết đồ thị**.

**Mạch bài học:** Kiến thức cần nhớ (lý thuyết đồ thị, ma trận kề, bất biến và tôpô sơ khai) → Câu đố lịch sử & trò vẽ một nét → Lập mô hình đa đồ thị → Bậc đỉnh và bổ đề bắt tay → Giải thích: tự tay tính ma trận kề $$4\times 4$$ của Königsberg, thêm 1 cây cầu và lắp ráp DNA bằng đồ thị de Bruijn → Điều kiện đủ và bài toán người đưa thư Trung Hoa.

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

## Kiến thức cần nhớ: Lý thuyết đồ thị, Ma trận kề và Tôpô sơ khai là gì?

Trước năm 1736, nhắc tới hình học là người ta nghĩ ngay đến độ dài, góc đo, diện tích và tọa độ của Euclid hay Descartes. Bài báo của Euler mở ra ba trụ cột tư duy mà mọi sinh viên đại học về khoa học, kỹ thuật hay kinh tế đều sẽ gặp lại:

### 1. Lý thuyết đồ thị (Graph Theory) là gì và nghiên cứu những gì?
Đó là ngành toán nghiên cứu thuần túy về **mối quan hệ kết nối**. Một đồ thị $$G = (V, E)$$ chỉ gồm tập các đối tượng (**đỉnh** $$V$$) và tập các kết nối giữa chúng (**cạnh** $$E$$). Sơ đồ tàu điện ngầm, mạng xã hội, mạch in điện tử hay mạng lưới cung ứng đều là đồ thị: việc bạn kéo dài một tuyến đường hay xoay bản đồ đi $$90^\circ$$ không làm thay đổi bản chất kết nối. Ngành này nghiên cứu các bài toán cốt lõi như đường đi ngắn nhất (Dijkstra), luồng cực đại trên mạng, tô màu đồ thị (lập lịch), và tồn tại đường Euler / chu trình Hamilton.

### 2. Bất biến tổ hợp và đại số hóa đồ thị (Ma trận kề)
Muốn chứng minh một nhiệm vụ là *bất khả thi* (như đi qua bảy cây cầu không lặp), ta không thể thử từng đường đi vì số lượng đường tăng theo giai thừa. Thay vào đó, ta tìm một **bất biến** — một đại lượng bắt buộc phải đúng cho mọi lời giải thành công (ở đây là tính chẵn lẻ của bậc đỉnh). Hơn nữa, trong đại số tuyến tính và khoa học máy tính, mọi đồ thị đều viết gọn thành một **ma trận kề** $$A$$ (ô $$A_{ij}$$ ghi số cạnh nối đỉnh $$i$$ với đỉnh $$j$$), biến các bài toán mạng thành phép nhân ma trận và giá trị riêng (như thuật toán PageRank của Google!).

### 3. Tôpô học sơ khai (*Geometria Situs*)
Euler gọi phương pháp của mình là *"hình học của vị trí"* — tiền thân trực tiếp của **tôpô học**, ngành nghiên cứu những tính chất không đổi khi ta co giãn, uốn cong không gian mà không cắt rách. Bảy cây cầu Königsberg là bước khởi đầu cho chuỗi tư duy dẫn thẳng tới Định lý Bốn màu và Giả thuyết Poincaré ở cuối chương này.

---

## 1. Câu đố lịch sử — và trò chơi vẽ một nét đời thường

Trước khi nhìn vào bản đồ Königsberg, hãy nghĩ đến một câu đố quen thuộc thời tiểu học: **vẽ hình chiếc phong bì (hoặc ngôi nhà có hai đường chéo chữ X bên trong) bằng một nét liền không nhấc bút, không tô đè nét nào**. Nếu bạn từng thử, hẳn bạn nhận ra một "nghịch lý" kỳ lạ: nếu xuất phát từ đỉnh mái nhà thì loay hoay mãi không xong, nhưng chỉ cần đặt bút ở một trong hai góc đáy của bức tường thì lại vẽ trơn tru trong một lần!

Tại sao điểm xuất phát lại quan trọng đến thế? Vì mỗi khi ngòi bút đi *ngang qua* một giao điểm trung gian, nó phải tốn **một nét đi vào** và **một nét đi ra** — tức là các nét tại mọi giao điểm trung gian luôn bị tiêu thụ thành từng cặp (số chẵn). Chỉ có hai điểm duy nhất được phép có số nét lẻ: điểm đặt bút ban đầu và điểm nhấc bút cuối cùng. Ở hình chiếc phong bì, hai góc đáy có đúng $$3$$ nét (số lẻ), các điểm còn lại đều chẵn — nên bạn *bắt buộc* phải bắt đầu ở một góc đáy và kết thúc ở góc đáy kia.

Bố cục Königsberg cũng chính là bài toán vẽ một nét ở quy mô thành phố: bốn vùng đất (hai bờ sông và hai hòn đảo) nối với nhau bằng bảy cây cầu. Bài báo năm 1736 của Euler thường được xem là văn bản đặt nền móng cho lý thuyết đồ thị, và cũng cho khía cạnh tổ hợp của tôpô: những tính chất vẫn giữ nguyên khi ta bỏ qua hình dạng.

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

Hãy hình dung ta đi trong đồ thị và dùng mỗi cạnh đúng một lần. Mỗi lần đi qua một đỉnh trung gian, ta vào bằng một cạnh và ra bằng cạnh khác, nên dùng hết **hai** đầu mút. Xét toàn đồ thị:

- Trong **chu trình Euler**, mọi đỉnh phải có **bậc chẵn**.
- Trong **đường Euler** không đóng, có đúng **hai** đỉnh bậc lẻ, là điểm đầu và điểm cuối. Mọi đỉnh khác đều có bậc chẵn.

### Bậc ở Königsberg

Trong mô hình chuẩn của bảy cây cầu, cả bốn đỉnh đều có bậc lẻ (ba đỉnh bậc $$3$$ và một đỉnh bậc $$5$$). Một đồ thị liên thông có nhiều hơn hai đỉnh bậc lẻ thì không thể có đường Euler. Vậy không có đường đi nào qua mỗi cầu đúng một lần.

Có thể nhớ theo Euler: *đếm số đỉnh bậc lẻ; nếu nhiều hơn hai thì dừng.*

---

## 4. Giải thích: tự tay kiểm tra ma trận kề Königsberg, "xây thêm 1 cầu" và lắp ráp DNA

Để cảm nhận sức mạnh của việc đại số hóa đồ thị, hãy tự tay tính ba ví dụ cụ thể dưới đây:

### Ví dụ cầm tay 1: Ma trận kề $$4 \times 4$$ của Königsberg
Đánh nhãn 4 vùng đất: $$A$$ (đảo Kneiphof ở giữa), $$B$$ (bờ Bắc), $$C$$ (bờ Nam), $$D$$ (đảo phía Đông). Ta ghi số cây cầu nối từng cặp vùng đất vào ma trận kề đối xứng $$M$$:

$$
M \;=\;
\begin{pmatrix}
0 & 2 & 2 & 1 \\
2 & 0 & 0 & 1 \\
2 & 0 & 0 & 1 \\
1 & 1 & 1 & 0
\end{pmatrix}
\begin{array}{l}
\leftarrow \text{Hàng } A:\ 0+2+2+1 = \mathbf{5}\ (\text{lẻ}) \\
\leftarrow \text{Hàng } B:\ 2+0+0+1 = \mathbf{3}\ (\text{lẻ}) \\
\leftarrow \text{Hàng } C:\ 2+0+0+1 = \mathbf{3}\ (\text{lẻ}) \\
\leftarrow \text{Hàng } D:\ 1+1+1+0 = \mathbf{3}\ (\text{lẻ})
\end{array}
$$

Cộng tổng cả 4 hàng: $$5 + 3 + 3 + 3 = 14 = 2 \times 7$$ (khớp chuẩn **Bổ đề bắt tay** $$\sum \deg(v) = 2\lvert E\rvert$$!). Vì có tới **4 đỉnh bậc lẻ**, không tồn tại đường Euler.

### Ví dụ cầm tay 2: Nếu thành phố xây thêm ĐÚNG 1 cây cầu nối Bờ Bắc $$B$$ và Bờ Nam $$C$$ thì sao?
Ta chỉ việc cộng $$+1$$ vào ô $$(B, C)$$ và $$(C, B)$$ trong ma trận $$M$$. Lập tức:
- $$\deg(A) = 5$$ (lẻ),
- $$\deg(B) = 3 + 1 = 4$$ (chẵn!),
- $$\deg(C) = 3 + 1 = 4$$ (chẵn!),
- $$\deg(D) = 3$$ (lẻ).

Số đỉnh bậc lẻ rút xuống còn **đúng 2 đỉnh** ($$A$$ và $$D$$). Theo định lý Euler, nay *chắc chắn* tồn tại một đường Euler mở đi qua đủ cả 8 cây cầu, bắt đầu ở $$A$$ và kết thúc ở $$D$$! Hãy kiểm tra trực tiếp một hành trình 8 cầu hợp lệ:

$$
A \xrightarrow{\text{cầu } 1} B \xrightarrow{\text{cầu } 2} A \xrightarrow{\text{cầu } 3} C \xrightarrow{\text{cầu } 4} A \xrightarrow{\text{cầu } 5} D \xrightarrow{\text{cầu } 6} B \xrightarrow{\text{cầu mới}} C \xrightarrow{\text{cầu } 7} D.
$$

Đếm lại bằng tay: đi qua đúng 8 cạnh không trùng cạnh nào! (Trong Thế chiến II, hai cây cầu thực tế bị phá hủy khiến số đỉnh bậc lẻ ở Kaliningrad hiện đại cũng giảm xuống còn $$2$$, nên ngày nay du khách thực sự đi được một đường Euler mở.)

### Ví dụ cầm tay 3: Lắp ráp bộ gen DNA bằng đồ thị de Bruijn
Trong tin sinh học hiện đại, máy giải trình tự chỉ đọc được các mảnh DNA ngắn bị cắt vụn, ví dụ ta thu được 4 mảnh độ dài 3 (gọi là 3-mer) không rõ thứ tự: `TGC`, `AAT`, `GCT`, `ATG`. Làm sao ghép lại thành chuỗi DNA gốc?
- **Bước 1:** Xem mỗi mảnh 3-mer như một **cạnh có hướng** nối 2 ký tự đầu với 2 ký tự cuối:
  `AAT` ($$AA \to AT$$), `ATG` ($$AT \to TG$$), `TGC` ($$TG \to GC$$), `GCT` ($$GC \to CT$$).
- **Bước 2:** Kiểm tra bậc vào / bậc ra của các đỉnh 2-mer: `AA` có (vào 0, ra 1), `CT` có (vào 1, ra 0), mọi đỉnh trung gian `AT, TG, GC` đều có (vào 1, ra 1).
- **Bước 3:** Đi theo **đường Euler có hướng** duy nhất từ `AA` đến `CT`:
  $$AA \to AT \to TG \to GC \to CT \implies \text{chuỗi DNA gốc: } \mathbf{AATGCT}.$$

Cả một ngành tin sinh học giải mã hàng tỷ cặp bazơ ngày nay chạy trực tiếp trên phát minh năm 1736 của Euler!

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
- **Thuật toán hiện đại.** Đường Euler xuất hiện trong lắp ráp bộ gen (đồ thị de Bruijn), định tuyến xe quét rác, in mạch PCB và bài toán vẽ một nét không nhấc bút.
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

Cùng thói quen "mô hình hóa bằng đồ thị" nằm sau [mạng]({{ site.baseurl }}/contents/vi/chapter03/03_06_Graph_Theory_Networks/), định lý bốn màu, và bài toán tô màu bản đồ. Khác biệt: Königsberg hỏi về sự tồn tại của một đường đi, còn bốn màu là ràng buộc về màu của các miền.

## Video tham khảo

- **Xem trước** — [The Seven Bridges of Königsberg - Numberphile](https://www.youtube.com/watch?v=W18FDEA1jRQ) — Numberphile, tiếng Anh. Video định hướng cho mục tiêu của bài: mô hình hệ thống cầu thành đa đồ thị.
- [How the Königsberg bridge problem changed mathematics - Dan Van der Vieren](https://www.youtube.com/watch?v=nZwSo4vfw6c) — TED-Ed, tiếng Anh. Xem lượt thứ hai, khi ý chính đã rõ.
- [Graph Theory: 01. Seven Bridges of Konigsberg](https://www.youtube.com/watch?v=eIb1cz06UwI) — Sarada Herke, tiếng Anh. Góc nhìn bổ sung sau hai video đầu.
