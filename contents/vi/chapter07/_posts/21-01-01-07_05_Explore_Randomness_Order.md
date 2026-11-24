---
layout: post
title: "Ngẫu nhiên có tạo ra trật tự không?"
chapter: '07'
order: 5
owner: Nguyen Le Linh
lang: vi
categories:
- chapter07
---

> **Liên kết**  
> [Green–Tao]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/) · [Thực hành: số nguyên tố]({{ site.baseurl }}/contents/vi/chapter07/07_04_Explore_Prime_Predictability/) · [Hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/)

Hãy thử tưởng tượng bạn rải ngẫu nhiên các hạt đậu lên một tờ giấy kẻ ô, hoặc tung một đồng xu công bằng để quyết định giữ hay bỏ từng số nguyên từ $$1$$ đến $$1000$$. Trực giác thường ngày mách bảo rằng ngẫu nhiên là kẻ thù của trật tự: tung đồng xu làm sao có thể tạo ra một hàng thẳng tắp hay một mô hình đều đặn? Ấy thế nhưng, năm 1947, Paul Erdős đã làm giới toán học sững sờ khi dùng chính hành động "tô màu ngẫu nhiên bằng tung đồng xu" để chứng minh sự tồn tại của những đồ thị có cấu trúc tinh vi mà không ai xây dựng nổi bằng tay suốt nhiều thập kỷ.

Toán học hiện đại còn đi xa hơn thế: giữa hai thái cực "trật tự tuyệt đối" và "hỗn loạn hoàn toàn" tồn tại một vùng đất cực kỳ thú vị mang tên **giả ngẫu nhiên (pseudorandomness)** — những đối tượng hoàn toàn tất định như tập số nguyên tố, nhưng lại vượt qua hàng loạt phép kiểm định thống kê giống hệt như thể chúng được tung đồng xu mà ra. Trong bài thực hành này, bạn sẽ bước vào phòng thí nghiệm mô phỏng để tự tay đo lường ranh giới giữa hai thái cực ấy: khi nào sự ngẫu nhiên phá hủy cấu trúc, khi nào mật độ buộc trật tự phải xuất hiện, và vì sao một câu khẩu hiệu như *"ngẫu nhiên tạo ra trật tự"* chỉ có ý nghĩa khi bạn chỉ rõ thang đo và phép kiểm định đi kèm.

---

## Mục tiêu học tập

Sau bài này, bạn cần:

- Nêu được ví dụ ngẫu nhiên **phá vỡ** cấu trúc và ví dụ xác suất giúp **chứng minh** sự tồn tại (hoặc tìm ra đối tượng đặc biệt).
- Phát biểu ý chính của định lý Roth (tập đủ dày chứa cấp số cộng 3 số hạng, gọi tắt là 3-AP) và so sánh với tập thưa ngẫu nhiên.
- Mô phỏng: lấy tập con ngẫu nhiên của $$\{1,\ldots,N\}$$ và đếm số 3-AP.
- Hiểu giả ngẫu nhiên là: không phân biệt được với ngẫu nhiên bằng một số phép kiểm định thống kê; lấy số nguyên tố làm ví dụ.
- Trong nhật ký, tách rõ đâu là định lý, đâu là lập luận trực quan, đâu là hiện tượng do mô phỏng sinh ra.
- Viết một đoạn liên hệ thí nghiệm với ý tưởng của Green–Tao mà không cho rằng mình đã chứng minh định lý Green–Tao.

**Kiến thức cần có.** Xác suất cơ bản (kỳ vọng, tính độc lập ở mức hiểu ý), đồng dư, đếm.

---

## Bản đồ kiến thức nền: Tổ hợp cộng tính và Phương pháp xác suất là gì, nghiên cứu những gì?

Người tốt nghiệp đại học thường học xác suất như một công cụ thống kê để phân tích dữ liệu ồn ào, và học tổ hợp như nghệ thuật đếm chỉnh hợp, tổ hợp. Nhưng trong toán học hiện đại, sự kết hợp giữa chúng đã khai sinh ra hai lĩnh vực cực kỳ sống động đứng sau bài học này:

1. **Phương pháp xác suất (The Probabilistic Method):** Do Paul Erdős khởi xướng, đây là nghệ thuật *dùng xác suất để chứng minh những định lý hoàn toàn tất định*. Thay vì vất vả vẽ ra một cấu hình thỏa mãn tính chất $$P$$, ta tạo ra một không gian các cấu hình ngẫu nhiên và tính kỳ vọng số "lỗi" (số chỗ vi phạm tính chất $$P$$). Nếu kỳ vọng số lỗi nhỏ hơn $$1$$, thì chắc chắn phải tồn tại ít nhất một cấu hình có **0 lỗi** — dù ta chưa cần biết mặt mũi nó ra sao! Cách tư duy này ngày nay là xương sống của khoa học máy tính lý thuyết, lý thuyết đồ thị ngẫu nhiên và thiết kế thuật toán.
2. **Tổ hợp cộng tính (Additive Combinatorics):** Ngành này nghiên cứu mối quan hệ giữa *kích thước* của một tập số nguyên và *cấu trúc cộng* của nó (ví dụ: tổng $$A+A$$ lớn cỡ nào? Tập $$A$$ có bắt buộc chứa cấp số cộng $$a, a+d, a+2d$$ không?). Định lý **Ramsey**, **Roth** và **Szemerédi** đều mang cùng một triết lý sâu sắc: *"Hỗn loạn hoàn toàn là bất khả thi."* Chỉ cần một hệ thống đủ lớn hoặc một tập con đủ dày, những mẫu hình trật tự (như cấp số cộng hay đồ thị con đơn sắc) buộc phải hiện ra.

Một ví dụ bằng số giúp bạn cảm nhận ngay sự phân đôi này: trong tập $$\{1, \dots, 100\}$$, có chính xác $$2450$$ bộ ba tạo thành cấp số cộng 3 số hạng (3-AP). Nếu bạn giữ lại ngẫu nhiên mỗi số với xác suất $$p = 0.2$$ (chỉ khoảng 20 số), kỳ vọng số 3-AP còn sót lại vẫn là $$2450 \times 0.2^3 \approx 19.6$$ bộ! Ngược lại, nếu bạn cố tình chọn 20 số *có cấu trúc* như các lũy thừa $$1, 2, 4, 8\dots$$ hoặc các số chỉ viết bằng chữ số $$0, 1$$ trong hệ cơ số 3, số 3-AP bằng đúng **0**. Như vậy, trên cùng một kích thước, tập ngẫu nhiên lại *giàu* cấp số cộng hơn nhiều tập có cấu trúc đặc biệt!

---

## 1. Kiến thức toán nền

### 1.1 "Trật tự" nghĩa là gì?

Trong bài này, **trật tự** là sự xuất hiện của một mẫu nhận ra được, chẳng hạn:

- cấp số cộng (AP) $$a,a+d,a+2d$$;  
- một nhóm đỉnh nối nhau đầy đủ (clique) mà mọi cạnh cùng màu khi tô màu các cạnh;  
- một cấu hình hình học (tam giác, các điểm cách nhau một đơn vị);  
- một mô tả có thể nén ngắn (độ phức tạp Kolmogorov thấp), ý này chỉ để tham khảo thêm.

**Ngẫu nhiên** ở đây nghĩa là lấy mẫu từ một phân phối đơn giản, ví dụ mỗi số nguyên được giữ lại một cách độc lập với xác suất $$p$$.

### 1.2 Ngẫu nhiên phá vỡ một số cấu trúc

Xét tập $$A\subset\{1,\ldots,N\}$$, trong đó mỗi số $$n$$ được giữ lại độc lập với xác suất $$p$$. Kỳ vọng số 3-AP xấp xỉ bằng số cặp $$(a,d)$$ có thể chọn nhân với $$p^3$$. Nếu $$p$$ rất nhỏ, ví dụ $$p=N^{-0.9}$$, kỳ vọng này có độ lớn cỡ $$N^2 \cdot (N^{-0.9})^3 = N^{-0.7} \ll 1$$. Khi đó, với xác suất cao, $$A$$ **không chứa cấp số cộng nào** (hoặc gần như không). Tập càng thưa và càng ngẫu nhiên thì cấu trúc cộng càng biến mất.

Tương tự, đồ thị ngẫu nhiên $$G(n,1/2)$$ hầu chắc chắn không có tập độc lập lớn (lớn hơn khoảng $$2 \log_2 n$$ đỉnh), nhưng lại hầu chắc chắn chứa mọi đồ thị con nhỏ cố định. Như vậy ngẫu nhiên vừa loại bỏ một số mẫu, vừa buộc một số mẫu khác phải xuất hiện.

### 1.3 Phương pháp xác suất chứng minh sự tồn tại

**Phương pháp xác suất của Erdős:** để chứng minh có tồn tại một đối tượng có tính chất $$P$$, ta định nghĩa một đối tượng ngẫu nhiên và chứng minh $$\Pr[P]>0$$. Cách này có thể không chỉ ra cụ thể đối tượng đó. Lập luận chỉ dùng lý thuyết độ đo đơn giản, thường trên không gian xác suất hữu hạn: nếu tất cả các sự kiện xấu đều tránh được trên một tập có xác suất dương, thì trong không gian mẫu có ít nhất một kết quả tốt.

Ví dụ kinh điển về chặn dưới số Ramsey $$R(k,k)$$: tô ngẫu nhiên mỗi cạnh của đồ thị đầy đủ $$K_n$$ bằng đỏ hoặc xanh với xác suất $$1/2$$. Xác suất một nhóm $$k$$ đỉnh cố định cùng màu là $$2 \cdot 2^{-\binom{k}{2}}$$. Do đó kỳ vọng số clique $$K_k$$ đơn sắc là $$\binom{n}{k} 2^{1-\binom{k}{2}}$$. Chẳng hạn với $$k=4$$ và $$n=8$$, ta có $$\binom{8}{4} 2^{1-6} = 70 / 32 > 1$$ nên chưa kết luận được; nhưng với $$n=6$$, $$\binom{6}{4} / 32 = 15/32 < 1$$, lập tức chứng minh tồn tại cách tô $$K_6$$ không có $$K_4$$ đơn sắc nào mà không cần vẽ một nét nào! Một ví dụ kinh điển khác: tồn tại đồ thị vừa có chu trình ngắn nhất dài tùy ý (girth lớn) vừa có sắc số lớn, được chứng minh bằng phương pháp xác suất từ rất lâu trước khi có cách dựng tường minh. Một ví dụ gần lý thuyết số: tồn tại tập không chứa tổng (sum-free) lớn trong $$\{1,\ldots,N\}$$ (lấy các số lẻ, hoặc một biến thể ngẫu nhiên).

Ở đây, ngẫu nhiên không phải là sự lộn xộn. Nó là **một công cụ chứng minh**. Thí nghiệm D giúp bạn thấy rõ điều này: tính kỳ vọng bằng tay, suy ra sự tồn tại, rồi với $$n$$ nhỏ thì tìm vét cạn để thấy đối tượng cụ thể.

### 1.4 Định lý cấu trúc: mật độ buộc phải có trật tự

**Định lý Roth:** với mọi $$\delta>0$$, nếu $$N$$ đủ lớn (phụ thuộc $$\delta$$) thì mọi tập con của $$\{1,\ldots,N\}$$ có mật độ ≥$$\delta>0$$ đều chứa một 3-AP. Chính mật độ, chứ không phải tính ngẫu nhiên, buộc phải có cấu trúc cộng. **Định lý Szemerédi** mở rộng kết quả này cho $$k$$-AP với mọi $$k$$ cố định. Câu hỏi định lượng "mật độ nhỏ đến mức nào thì vẫn buộc có 3-AP" vẫn đang được nghiên cứu sôi nổi (Bloom–Sisask, Kelley–Meka 2023 và nhiều người khác). Trong bài này, bạn chỉ cần ý định tính và cảm nhận về thang đo qua mô phỏng.

**Định lý Green–Tao** đưa ý tưởng này sang số nguyên tố. Dù số nguyên tố có mật độ bằng 0, chúng vẫn đủ dày *bên trong một hàm trội giả ngẫu nhiên* (pseudorandom majorant) để có các cấu hình kiểu Szemerédi. Ý tưởng sâu xa là sự phân đôi giữa cấu trúc và giả ngẫu nhiên: một tập hoặc có tính gần tuần hoàn (có cấu trúc), hoặc trông ngẫu nhiên khi đo bằng các chuẩn Gowers (giả ngẫu nhiên). Trong cả hai trường hợp đều có cấp số cộng, nhưng theo những cơ chế khác nhau.

Một cách hình dung hữu ích là **nguyên lý chuyển** (transference): nếu một tập thưa trông giống một tập dày *khi đo bằng một trọng số chọn cẩn thận*, thì các cấu hình đã biết trong tập dày cũng chuyển sang được tập thưa. Hàm trội của Green–Tao đóng vai trò đó đối với số nguyên tố. Bạn không cần dựng hàm trội này. Bạn **mô phỏng** các trường hợp dày và thưa, rồi tự diễn đạt lại sự phân đôi bằng lời của mình. Nhờ vậy, khi chương 2 nhắc đến "giả ngẫu nhiên", bạn đã có trải nghiệm cụ thể.

**Đếm chính xác số 3-AP.** Số cặp $$(a,d)$$ với $$d\ge 1$$ và $$a+2d\le N$$ bằng

$$
\sum_{d=1}^{\lfloor(N-1)/2\rfloor}(N-2d)=\Theta(N^2).
$$

Cụ thể, tổng này bằng $$\frac{N(N-2)}{4}$$ nếu $$N$$ chẵn và $$\frac{(N-1)^2}{4}$$ nếu $$N$$ lẻ (ví dụ $$N=100$$ cho đúng $$2450$$). Vậy trong mô hình Bernoulli, kỳ vọng số cấp số cộng là $$\Theta(p^3 N^2)$$. Chỉ một ước lượng tiệm cận này đã đủ để thiết kế thí nghiệm A và B hợp lý: bạn biết ngay ngưỡng $$p \approx (4/N^2)^{1/3}$$ nơi kỳ vọng bắt đầu rơi xuống dưới 1 khi giảm dần $$p$$.

### 1.5 Giả ngẫu nhiên: vùng ở giữa

Một dãy hoặc một tập được gọi là **giả ngẫu nhiên** (đối với một họ phép kiểm định) nếu nó vượt qua những phép kiểm định mà đối tượng thật sự ngẫu nhiên vượt qua với xác suất cao: phân bố đều trong các cấp số cộng, tương quan nhỏ, độ lệch Fourier gần 0, v.v. Hàm Liouville $$\lambda(n)=(-1)^{\Omega(n)}$$ được giả thuyết là hành xử như ngẫu nhiên đối với nhiều loại trung bình (giả thuyết Chowla); một số kết quả bộ phận mới được chứng minh gần đây. Số nguyên tố không khớp với mô hình dãy bit độc lập cùng phân phối một cách thô sơ (mọi số nguyên tố sau 2 đều lẻ, và trừ hữu hạn số, không rơi vào lớp $$0\bmod q$$), nhưng lại khớp với các thống kê tinh hơn sau khi đã tính đến các ràng buộc địa phương đó.

**Nguyên tắc ghi nhật ký.** Luôn nói rõ tên phép kiểm định. Nói "ngẫu nhiên" mà không nêu phép kiểm định thì chỉ là cách nói cho hay.

### 1.6 Entropy, nhiễu và khôi phục tín hiệu (mở rộng, không bắt buộc)

Trong lý thuyết mã và thống kê, nhiễu là thứ cần chống lại, nhưng mã ngẫu nhiên lại đạt được dung lượng kênh. Trong học máy, nhiễu của gradient ngẫu nhiên có thể giúp thuật toán thoát khỏi điểm yên ngựa. Chỉ nhắc đến những ý này nếu bạn muốn có đoạn về ứng dụng; phần toán chính vẫn là tổ hợp cộng tính.

---

## 2. Giả thuyết, chứng minh và thí nghiệm

| Nhãn | Ví dụ |
|------|-------|
| **Định lý** | Roth; Szemerédi; Green–Tao; các kết quả tồn tại bằng phương pháp xác suất |
| **Giả thuyết** | Số nguyên tố sinh đôi; Chowla; nhiều giả thuyết về độ lệch Fourier |
| **Mô phỏng** | "50 lần thử, $$N=200$$, $$p=0.2$$, số AP trung bình là …" |
| **Khẩu hiệu** | "Ngẫu nhiên tạo ra trật tự": mỗi lần dùng phải giải thích rõ |

**Tiêu chí:**

1. Một mô phỏng đếm 3-AP, có ghi tham số và kết quả.  
2. Một ví dụ ngẫu nhiên phá vỡ cấu trúc và một ví dụ chứng minh tồn tại bằng xác suất.  
3. Nửa trang về ý tưởng của Green–Tao (cấu trúc và giả ngẫu nhiên).  
4. Nhãn rõ ràng trong nhật ký; không viết kiểu "nhìn đồ thị là thấy Green–Tao hiển nhiên".  
5. Một chỗ hiểu sai ban đầu đã được sửa.

---

## 3. Cách ghi nhật ký

**Ngày · Dự định · Việc đã làm · Tham số $$(N,p,T)$$ · Kết quả · Nhãn · Giải thích · Bước tiếp theo.**

Ghi lại hạt giống (seed) của bộ sinh số ngẫu nhiên. Cố định định nghĩa 3-AP ngay từ đầu ($$d>0$$, ba số hạng phân biệt).

---

## 4. Thí nghiệm

Làm ít nhất 2 trong các thí nghiệm A–E.

### A. Tập dày ngẫu nhiên và 3-AP (40–80 phút)

Với $$N\in\{50,100,200\}$$ và $$p\in\{0.1,0.3,0.5\}$$, lấy mẫu Bernoulli, đếm số 3-AP, lặp lại $$T\ge 20$$ lần, ghi giá trị trung bình và lớn nhất. Đếm cẩn thận: duyệt $$d\ge 1$$ và $$a$$ sao cho $$a+2d\le N$$, kiểm tra cả ba số hạng đều thuộc tập. Với $$N$$ lớn, dùng bảng băm (hash set).

**Giả thuyết:** "Số AP trung bình xấp xỉ $$p^3 N^2$$." Hãy kiểm tra bậc độ lớn, đừng chỉ nhìn một ô trong bảng.

**Tiêu chí:** có bảng số liệu, so sánh với giá trị kỳ vọng ước lượng, và nếu được thì vẽ đồ thị số AP trung bình theo $$p$$ (với $$N$$ cố định).

### B. Trường hợp tập thưa (30–60 phút)

Cố định $$N=500$$. Giảm $$p$$ cho đến khi trung vị số AP qua các lần thử bằng 0. So sánh với ngưỡng ước lượng khi kỳ vọng nhỏ hơn 1.

**Tiêu chí:** ước lượng được giá trị $$p$$ tới hạn, và nói trung thực về sai số do số mẫu hữu hạn.

### C. Tập có cấu trúc (20–40 phút)

Dựng một tập không chứa cấp số cộng mà bạn định nghĩa được (ví dụ cấp số nhân, hoặc các số chỉ dùng chữ số 0 và 1 trong hệ cơ số 3; các cách dựng của Behrend hay Salem–Spencer là nâng cao; với $$N$$ nhỏ, một tập lớn không chứa AP đơn giản cũng được). So sánh số AP với một tập ngẫu nhiên có cùng số phần tử.

**Tiêu chí:** hai tập cùng kích thước, khác cấu trúc, số AP khác nhau, có số liệu cụ thể.

### D. Ví dụ về phương pháp xác suất (25–40 phút)

Làm lại chứng minh chặn dưới số Ramsey trong sách giáo khoa, hoặc chứng minh tồn tại giải đấu vòng tròn (tournament) không có bộ ba bắc cầu, *với kích thước nhỏ* để còn kiểm tra vét cạn được. Viết cả lập luận dùng kỳ vọng và ghi chú về kết quả vét cạn.

**Tiêu chí:** có phác thảo chứng minh tồn tại và kiểm tra tính toán cho $$n$$ nhỏ.

### E. Đọc hiểu Green–Tao (20–30 phút)

Đọc đoạn về cấu trúc và ngẫu nhiên ở chương 2 (hoặc một bài phổ biến khoa học mà bạn trích dẫn). Viết lại sự phân đôi trong không quá 8 câu. Kể tên hai phép kiểm định dùng để gọi một tập là giả ngẫu nhiên.

**Tiêu chí:** tự viết lại, không chép; nêu tên được hai phép kiểm định.

---

## 5. Những hiểu lầm thường gặp

1. "Tập ngẫu nhiên không bao giờ có mẫu." Sai: tập ngẫu nhiên đủ dày có rất nhiều AP với xác suất cao.  
2. "Chứng minh bằng xác suất là không đầy đủ." Sai: chứng minh tồn tại qua $$\Pr>0$$ là hoàn toàn chặt chẽ, chỉ là có thể không cho thuật toán tìm ra đối tượng.  
3. "Green–Tao coi số nguyên tố là các biến độc lập cùng phân phối." Sai: chứng minh dùng hàm trội giả ngẫu nhiên và lý thuyết cấu trúc.  
4. "Định lý Szemerédi cần đến ngẫu nhiên." Sai: định lý cần mật độ; chứng minh có thể dùng lý thuyết ergodic hoặc giải tích Fourier.  
5. "Mô phỏng là định lý." Sai: mô phỏng giúp đặt giả thuyết và minh họa.

---

## 7. Bảng tự đánh giá

| ☐ | Bảng mô phỏng có ghi tham số |
| ☐ | Hai ví dụ: phá vỡ cấu trúc và chứng minh tồn tại |
| ☐ | Đoạn văn về ý tưởng Green–Tao |
| ☐ | Nhật ký ít nhất 3 mục có nhãn |
| ☐ | Một chỗ hiểu sai đã sửa |
| ☐ | Một câu hỏi mở |

---


## Nguồn video (gói nghiên cứu video)

Video dùng để **định hướng và hiểu thêm về văn hóa nghiên cứu**, không thay cho chứng minh. Chi tiết: `research/video-research/explore-randomness-order/`.

**Ý chính rút ra từ gói nghiên cứu**

- Một tập xác định vẫn có thể trông "ngẫu nhiên"; mật độ buộc phải có cấp số cộng (Roth, Szemerédi, Green–Tao).
- Phương pháp xác suất: chứng minh tồn tại thông qua kỳ vọng.
- Bài thực hành: phân biệt mô phỏng với chứng minh; luôn gắn nhãn.

**Thứ tự xem gợi ý**

1. **Định hướng:** Quanta, P vs NP (cấu trúc và tìm kiếm; văn hóa của lý thuyết độ phức tạp): [https://www.youtube.com/watch?v=pQsdygaYcE4](https://www.youtube.com/watch?v=pQsdygaYcE4).  

**Trang chính thức / tài liệu**

- Green–Tao (structure in primes): https://arxiv.org/abs/math/0404188  
- Tao blog / notes on Szemerédi (expository entry): https://terrytao.wordpress.com/tag/szemeredi-theorem/  

Danh mục URL đầy đủ: `research/video-research/explore-randomness-order/references.md`.

## 8. Tài liệu


### Gói nghiên cứu video (tất cả URL)

Danh mục đầy đủ: `research/video-research/explore-randomness-order/references.md`.

1. Quanta — P vs NP (structure vs search; complexity culture) — https://www.youtube.com/watch?v=pQsdygaYcE4  
2. Green–Tao (structure in primes) — https://arxiv.org/abs/math/0404188  
3. Tao blog / notes on Szemerédi (expository entry) — https://terrytao.wordpress.com/tag/szemeredi-theorem/  
4. Wikipedia — Probabilistic method — https://en.wikipedia.org/wiki/Probabilistic_method  
5. Wikipedia — Szemerédi's theorem — https://en.wikipedia.org/wiki/Szemer%C3%A9di%27s_theorem  
6. Wikipedia — Roth's theorem — https://en.wikipedia.org/wiki/Roth%27s_theorem  
7. Wikipedia — Pseudorandomness — https://en.wikipedia.org/wiki/Pseudorandomness  
8. Alon–Spencer book info (probabilistic method) — https://en.wikipedia.org/wiki/The_Probabilistic_Method  
9. Quanta — patterns in primes / structure — https://www.quantamagazine.org/tag/number-theory/  
10. Thư mục gói: `research/video-research/explore-randomness-order/`.

1. [Green–Tao, chương 2]({{ site.baseurl }}/contents/vi/chapter02/02_04_Green_Tao/); [thực hành: số nguyên tố]({{ site.baseurl }}/contents/vi/chapter07/07_04_Explore_Prime_Predictability/); [hỗn độn]({{ site.baseurl }}/contents/vi/chapter04/04_05_Chaos/).  
2. Alon–Spencer, *The Probabilistic Method* (Phương pháp xác suất).  
3. Các bài viết phổ biến về định lý Roth và Szemerédi (blog của Tao nếu truy cập được).  
4. Bài thực hành [Collatz và phép lặp]({{ site.baseurl }}/contents/vi/chapter07/07_09_Explore_Iteration/), về những quy tắc tất định nhưng cho kết quả trông "lộn xộn".

---

## Hướng đi tiếp

Nếu thích mô phỏng, hãy viết chương trình đo độ lệch Fourier của hàm chỉ thị một tập con của $$\mathbb{Z}/N\mathbb{Z}$$, rồi so sánh tập có cấu trúc với tập ngẫu nhiên. Tập có cấu trúc (cấp số cộng dài, tập Bohr) có độ lệch lớn ở một tần số nào đó; tập ngẫu nhiên có độ lệch nhỏ với xác suất cao. Nếu thích phần suy nghĩ, hãy viết một bài luận dài hơn về định nghĩa "trật tự" trong tổ hợp và trong hệ động lực, liên hệ sự phụ thuộc nhạy vào điều kiện ban đầu ở bài hỗn độn với việc quỹ đạo Collatz trông bất quy tắc về mặt thống kê. Nếu thích thí nghiệm D, hãy đẩy chặn Ramsey thêm vài bước và ghi lại lúc nào lập luận kỳ vọng cho kết quả vượt xa khả năng vét cạn.

**Gợi ý bài tổng hợp một trang (nên làm).** Viết thành văn liền mạch: (i) khi nào ngẫu nhiên phá vỡ cấu trúc cộng trong dữ liệu của bạn; (ii) khi nào mật độ buộc phải có cấu trúc, theo định lý mà bạn trích dẫn; (iii) giả ngẫu nhiên nằm ở đâu giữa hai thái cực đó; (iv) mô phỏng *không thể* cho biết điều gì về số nguyên tố.

### Bản ghi lời và khung hình (trích tự động)

Bản ghi lời thoại và các đoạn theo thời gian: `research/video-research/explore-randomness-order/transcripts/` · trạng thái: `research/video-research/explore-randomness-order/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Khung hình mẫu từ video]({{ site.baseurl }}/img/video_research/nonflagships/explore-randomness-order_pQsdygaYcE4_thumb.jpg)

*Hình. Khung hình mẫu từ video chính của gói (xem gói nghiên cứu để biết mốc thời gian).*


## Video tham khảo

- **Xem trước:** [Terence Tao: Structure and Randomness in the Prime Numbers, UCLA](https://www.youtube.com/watch?v=PtsrAw1LR3E) (UCLA, tiếng Anh). Tao giải thích sự đan xen giữa cấu trúc và ngẫu nhiên trong số nguyên tố, đúng ý tưởng nền của định lý Green–Tao. Nên xem trước khi làm thí nghiệm.
- [Chaos: The Science of the Butterfly Effect](https://www.youtube.com/watch?v=fDek6cYijxI) (Veritasium, tiếng Anh). Giới thiệu hiệu ứng cánh bướm và hệ hỗn độn: quy tắc tất định vẫn sinh ra hành vi trông như ngẫu nhiên. Xem sau, khi đã nắm ý chính của bài.
