---
layout: post
title: "Tính Vô tỷ của √2"
chapter: '05'
order: 6
owner: Nguyen Le Linh
lang: vi
categories:
- chapter05
---

Hơn hai nghìn năm trăm năm trước, trường phái Pythagore ở Hy Lạp cổ đại tôn thờ một niềm tin gần như tôn giáo: *"Vạn vật đều là số"* — nghĩa là mọi độ dài, mọi giai điệu âm nhạc và mọi tỷ lệ trong vũ trụ đều có thể diễn đạt trọn vẹn bằng **tỷ số của hai số nguyên**. Thế nhưng, ngay bên trong hình khối đơn giản nhất mà bất kỳ đứa trẻ nào cũng vẽ được — một hình vuông cạnh bằng $$1$$ — lại ẩn giấu một kẻ phá bĩnh: độ dài đường chéo $$\sqrt{2}$$.

Tương truyền rằng khi Hippasus xứ Metapontum chứng minh được $$\sqrt{2}$$ không thể viết thành tỷ số của hai số nguyên nào, phát hiện "phi lý" (*alogon*) ấy đã gây ra cuộc khủng hoảng nền tảng đầu tiên của lịch sử toán học. Đến tận hôm nay, lập luận ấy vẫn là một trong những chứng minh nhập môn đẹp nhất từng được viết ra: chỉ vài dòng số học sơ cấp dựa trên **tính chẵn lẻ** đã đủ đánh sập hoàn toàn giả thiết "$$\sqrt{2}$$ là số hữu tỷ".

**Mạch bài học:** Kiến thức cần nhớ (tháp hệ thống số, định giá $$p$$-adic, xuống thang vô hạn) → Nghịch lý cây thước chung và dãy xấp xỉ Pell → Chứng minh cổ điển bằng tính chẵn lẻ → Giải thích: tự tay kiểm tra ba cách chứng minh (đại số, định giá $$v_2$$, và xuống thang bằng hai hình vuông) → Mở rộng cho $$\sqrt{p}$$ và bài học về mở rộng hệ thống số.

---

## Mục tiêu học tập

Sau bài học, bạn có thể:

- Phát biểu và chứng minh $$\sqrt{2}$$ vô tỷ bằng cách chỉ ra mâu thuẫn "cả tử và mẫu đều chẵn" ở dạng tối giản.
- Giải thích vì sao điều kiện "tối giản" (hoặc một điều kiện tối thiểu tương đương) là thiết yếu.
- Nối chứng minh này với phương pháp xuống thang vô hạn và tính chia hết cho 2.
- Áp dụng ý tưởng cho $$\sqrt{3}$$ hoặc $$\sqrt{p}$$ với $$p$$ nguyên tố, chỉ ra chỗ nào lập luận chẵn lẻ cần được tổng quát hóa.
- Tránh lập luận sai "$$\sqrt{2}$$ vô tỷ vì phần thập phân không bao giờ kết thúc".
- Trình bày rõ ràng ý tưởng chứng minh khi thảo luận nhóm.

**Kiến thức cần có.** Số nguyên, chẵn và lẻ, phân số tối giản, và biết rằng $$p^2=2q^2$$ là dạng đại số của $$\sqrt{2}=p/q$$. Phương pháp phản chứng.

---

## Kiến thức cần nhớ: Hệ thống số, Định giá $$p$$-adic và Phương pháp xuống thang là gì?

Để người tốt nghiệp đại học thấy tầm vóc thực sự của bài toán tưởng như "sơ cấp" này, hãy đặt nó lên ba trụ cột của **Lý thuyết số** và **Đại số**:

### 1. Kiến trúc mở rộng các hệ thống số ($$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$)
Mỗi khi một phép toán tự nhiên chạm trần, toán học lại mở rộng vũ trụ số: số tự nhiên $$\mathbb{N}$$ không đủ để trừ sinh ra số nguyên $$\mathbb{Z}$$; số nguyên không đủ để chia sinh ra số hữu tỷ $$\mathbb{Q}$$; số hữu tỷ vẫn còn vô số "lỗ hổng" (như đường chéo $$\sqrt{2}$$) sinh ra số thực $$\mathbb{R}$$; và phương trình $$x^2 + 1 = 0$$ sinh ra số phức $$\mathbb{C}$$. Trong thế giới số vô tỷ, $$\sqrt{2}$$ là **số đại số** (nghiệm của đa thức $$x^2 - 2 = 0$$), khác với **số siêu việt** như $$\pi$$ hay $$e$$ (không là nghiệm của bất kỳ đa thức hệ số nguyên nào).

### 2. Lý thuyết chia hết và định giá $$p$$-adic ($$v_p$$)
Trong lý thuyết số hiện đại, thay vì chỉ nói "chẵn hay lẻ", ta đếm **số mũ cao nhất của số nguyên tố $$p$$** chia hết một số nguyên $$n$$ — gọi là **định giá $$p$$-adic** $$v_p(n)$$. Ví dụ $$v_2(12) = v_2(2^2 \cdot 3) = 2$$, $$v_2(24) = v_2(2^3 \cdot 3) = 3$$. Tính chất đẹp nhất của $$v_p$$ là $$v_p(ab) = v_p(a) + v_p(b)$$, nên $$v_p(a^2) = 2v_p(a)$$ **luôn là số chẵn**! Chỉ riêng nhận xét một dòng này lập tức đánh bại phương trình $$p^2 = 2q^2$$.

### 3. Nguyên lý sắp thứ tự tốt và Phương pháp xuống thang vô hạn
Tập số nguyên dương $$\mathbb{N}^*$$ có một "sàn cứng" ở $$1$$: **không thể có một dãy số nguyên dương giảm ngặt vô hạn** $$a_1 > a_2 > a_3 > \cdots > 0$$. Phương pháp **xuống thang vô hạn** (sau này được Pierre de Fermat hoàn thiện cho $$a^4 + b^4 = c^4$$) khai thác đúng sàn cứng này: nếu từ một nghiệm nguyên dương ta luôn dựng được một nghiệm nguyên dương *nhỏ hơn thực sự*, thì nghiệm ban đầu không thể tồn tại.

---

## 1. Từ nghịch lý "cây thước chia nhỏ mãi vẫn không vừa" đến định lý

Trong đời sống và kỹ thuật, ta luôn có cảm giác rằng chỉ cần chia nhỏ vạch thước thêm nữa — từ milimet xuống micromet rồi nanomet — thì sớm muộn gì cũng có một đơn vị siêu nhỏ đo **vừa khít** cả cạnh lẫn đường chéo của hình vuông. Hãy thử kiểm tra bằng **dãy xấp xỉ Pell** sinh bởi quy tắc $$p_{n+1} = p_n + 2q_n,\ q_{n+1} = p_n + q_n$$ (bắt đầu từ $$p_1 = 1, q_1 = 1$$):

| Bước $$n$$ | Phân số $$p_n/q_n$$ | Giá trị thập phân | $$p_n^2$$ | $$2q_n^2$$ | Sai lệch $$p_n^2 - 2q_n^2$$ |
|------------|---------------------|-------------------|-----------|------------|-----------------------------|
| $$1$$ | $$1/1$$ | $$1.00000$$ | $$1$$ | $$2$$ | $$-1$$ |
| $$2$$ | $$3/2$$ | $$1.50000$$ | $$9$$ | $$8$$ | $$+1$$ |
| $$3$$ | $$7/5$$ | $$1.40000$$ | $$49$$ | $$50$$ | $$-1$$ |
| $$4$$ | $$17/12$$ | $$1.41667$$ | $$289$$ | $$288$$ | $$+1$$ |
| $$5$$ | $$41/29$$ | $$1.41379$$ | $$1681$$ | $$1682$$ | $$-1$$ |
| $$6$$ | $$99/70$$ | $$1.41429$$ | $$9801$$ | $$9800$$ | $$+1$$ |

Thật kỳ lạ: ta có thể tiến sát $$\sqrt{2} \approx 1.41421356\ldots$$ đến bất kỳ độ chính xác nào, nhưng phương trình nguyên $$p^2 = 2q^2$$ thì **luôn luôn lệch ít nhất $$1$$ đơn vị**!

Hai độ dài được gọi là **thông ước** nếu có một đơn vị chung sao cho mỗi độ dài bằng một số nguyên lần đơn vị đó; điều này tương đương với tỷ số của chúng là số hữu tỷ. Chứng minh tính vô tỷ cho thấy không có cây thước chung nào — dù tinh vi đến cỡ nguyên tử — đo được cả cạnh và đường chéo hình vuông một số nguyên lần.

---

## 2. Định lý và cách đặt vấn đề

<div class="textbook-theorem" markdown="1">
**Định lý.** $$\sqrt{2}$$ là số vô tỷ: không tồn tại các số nguyên $$p,q$$ với $$q\neq 0$$ sao cho $$\sqrt{2}=p/q$$.
</div>

Một cách tương đương: phương trình

$$
p^2 = 2q^2
$$

không có nghiệm nguyên với $$q\neq 0$$.

---

## 3. Chứng minh cổ điển (ý tưởng cùng các bước thiết yếu)

Giả sử phản chứng rằng $$\sqrt{2}=p/q$$ với $$p,q$$ nguyên, $$q>0$$, và phân số là **tối giản**: $$\gcd(p,q)=1$$.

Khi đó $$p^2=2q^2$$. Vế phải chẵn nên $$p^2$$ chẵn. Theo một bổ đề quen thuộc, nếu $$p^2$$ chẵn thì $$p$$ chẵn, vì nếu $$p$$ lẻ thì $$p^2$$ cũng lẻ. Đặt $$p=2k$$ và thay vào:

$$
(2k)^2=2q^2 \implies 4k^2=2q^2 \implies q^2=2k^2.
$$

Vậy $$q^2$$ chẵn, nên $$q$$ chẵn. Như thế 2 chia hết cả $$p$$ lẫn $$q$$, mâu thuẫn với $$\gcd(p,q)=1$$. Do đó không có biểu diễn tối giản nào, nghĩa là $$\sqrt{2}$$ vô tỷ.

### Vì sao "bình phương chẵn thì số đó chẵn"

Nếu $$p=2m+1$$ thì $$p^2=4m^2+4m+1$$ là số lẻ. Thực chất đây là phép tính modulo 2:

$$
p\equiv 0\ \text{hoặc}\ 1\pmod{2},\qquad p^2\equiv 0\ \text{hoặc}\ 1\pmod{2}.
$$

---

### Video ngắn: Xuống thang bằng các hình vuông

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/sqrt2-irrational-squares_vi.mp4"></video>
</div>

Một hình minh họa cho phương pháp xuống thang vô hạn: nếu a bình phương bằng hai lần b bình phương, thì đặt hai hình vuông cạnh b vào trong hình vuông cạnh a, phần chồng lên nhau và các phần còn trống sẽ cho ra những hình vuông có cạnh nguyên nhỏ hơn.


## 4. Giải thích: tự tay kiểm tra ba góc nhìn — định giá $$v_2$$, xuống thang hình học và bài thử $$\sqrt{4}$$

Để không chỉ thuộc lòng ba dòng chẵn lẻ mà nhìn xuyên thấu cấu trúc sâu bên dưới, hãy cầm bút kiểm tra ba phép tính nhỏ sau:

### Góc nhìn 1: Định giá $$2$$-adic $$v_2$$ (tính bằng tay ngay trên số cụ thể)
Thử bất kỳ hai số nguyên dương nào, chẳng hạn $$p = 12 = 2^2 \cdot 3$$ và $$q = 10 = 2^1 \cdot 5$$:
- Vế trái: $$p^2 = 144 = 2^4 \cdot 9 \implies v_2(p^2) = 4$$ (**số chẵn**).
- Vế phải: $$2q^2 = 200 = 2^3 \cdot 25 \implies v_2(2q^2) = 1 + 2(1) = 3$$ (**số lẻ**).

Tổng quát, với **mọi** số nguyên dương $$p, q$$, ta luôn có $$v_2(p^2) = 2v_2(p)$$ là **số chẵn**, còn $$v_2(2q^2) = 1 + 2v_2(q)$$ là **số lẻ**. Một số nguyên không thể vừa có số mũ của $$2$$ là chẵn vừa là lẻ! Do đó $$p^2 = 2q^2$$ vô nghiệm tuyệt đối.

### Góc nhìn 2: Kiểm tra đại số chứng minh hình học bằng hai hình vuông (Tennenbaum / Apostol)
Giả sử có cặp số nguyên dương nhỏ nhất $$(a, b)$$ thỏa $$a^2 = 2b^2$$ (diện tích một hình vuông cạnh $$a$$ bằng tổng diện tích hai hình vuông cạnh $$b$$). Vì $$1 < \sqrt{2} < 2$$ nên $$b < a < 2b$$.
- Đặt hai hình vuông cạnh $$b$$ vào hai góc đối diện bên trong hình vuông cạnh $$a$$.
- Hai hình vuông cạnh $$b$$ sẽ **chồng lấn** nhau thành một hình vuông ở giữa có cạnh $$a' = 2b - a > 0$$.
- Hai góc còn trống chưa được phủ là hai hình vuông nhỏ giống hệt nhau có cạnh $$b' = a - b > 0$$.
- Vì tổng diện tích hai hình vuông $$b$$ bằng diện tích hình vuông $$a$$, nên diện tích phần chồng lấn **bắt buộc bằng** tổng diện tích hai góc trống:
  $$
  (2b - a)^2 \;=\; 2(a - b)^2.
  $$
- **Tự tay kiểm tra bằng khai triển:**
  - Vế trái: $$(2b - a)^2 = 4b^2 - 4ab + a^2$$.
  - Vế phải: $$2(a - b)^2 = 2a^2 - 4ab + 2b^2$$.
  - Rút gọn $$-4ab$$ hai vế: $$4b^2 + a^2 = 2a^2 + 2b^2 \iff 2b^2 = a^2$$ (đúng hoàn toàn!).
- Nhưng $$a' = 2b - a < a$$ và $$b' = a - b < b$$ lại là một cặp nghiệm nguyên dương **nhỏ hơn thực sự** — mâu thuẫn với tính nhỏ nhất của $$(a, b)$$!

### Góc nhìn 3: Bài kiểm tra ngược — vì sao chứng minh gãy ngay với $$\sqrt{4}$$?
Nếu ta cố áp dụng máy móc lập luận cổ điển cho $$p^2 = 4q^2$$:
- Vế phải chia hết cho $$4 \implies 4 \mid p^2$.
- Nhưng bước chuyển "$$4 \mid p^2 \Rightarrow 4 \mid p$$" **SAI!** (Ví dụ $$p = 2, q = 1$$ có $$p^2 = 4$$ chia hết cho $$4$$, nhưng $$p = 2$$ không chia hết cho $$4$$.)
- Dùng ngôn ngữ định giá $$v_2$$: $$v_2(4q^2) = 2 + 2v_2(q)$$ là **số chẵn**, khớp hoàn toàn với $$v_2(p^2) = 2v_2(p)$$ — không có mâu thuẫn nào xảy ra!

---

## 5. Cách trình bày bằng xuống thang vô hạn

Ta có thể chứng minh mà không cần nhắc đến ước chung lớn nhất. Giả sử $$p^2=2q^2$$ với $$p,q$$ nguyên dương. Khi đó $$p$$ chẵn, $$p=2k$$, và $$q^2=2k^2$$ nên $$q$$ chẵn, $$q=2\ell$$, và

$$
k^2=2\ell^2
$$

với $$k$$ là số nguyên dương và $$k<p$$. Lặp lại mãi, ta được một dãy số nguyên dương giảm vô hạn $$p > k > \cdots > 0$$, điều này không thể xảy ra. Đây là phương pháp **xuống thang vô hạn** của Fermat: từ một nghiệm ta tạo ra một nghiệm nhỏ hơn, và cứ thế mãi.

---

## 6. Ý tưởng cốt lõi *là* gì và *không phải* là gì

**Ý tưởng cốt lõi là gì:**
- Giả sử số đó hữu tỷ và viết ở dạng tối giản (hoặc chọn nghiệm nguyên dương nhỏ nhất).
- Chuyển tính chia hết từ $$p^2$$ sang $$p$$ nhờ tính nguyên tố của $$2$$ (hoặc so sánh tính chẵn lẻ của định giá $$v_2$$).
- Đi đến mâu thuẫn với tính tối giản / tối thiểu.

**Ý tưởng cốt lõi *không phải* là gì:**
- Không phải "phần thập phân của $$\sqrt{2}$$ không kết thúc nên nó vô tỷ". Nhiều số hữu tỷ có phần thập phân không kết thúc ($$1/3=0.333\ldots$$). Số vô tỷ tương đương với phần thập phân không kết thúc *và không tuần hoàn*, nhưng chứng minh tính không tuần hoàn không hề dễ hơn lập luận chẵn lẻ.  
- Không phủ nhận việc xấp xỉ: $$\sqrt{2}$$ *là* giới hạn của các số hữu tỷ; tính vô tỷ chỉ nói nó không bằng một tỷ số, chứ không nói nó không xấp xỉ được.  
- Bản thân chứng minh này không phân loại mọi số vô tỷ và cũng không chứng minh tính siêu việt ($$\sqrt{2}$$ là số đại số).

---

## 7. Mở rộng: $$\sqrt{3}$$ và $$\sqrt{p}$$

Với $$\sqrt{3}$$, giả sử $$p^2=3q^2$$ ở dạng tối giản. Khi đó $$3\mid p^2$$ kéo theo $$3\mid p$$ (vì 3 là số nguyên tố); đặt $$p=3k$$, ta được $$q^2=3k^2$$, suy ra $$3\mid q$$, mâu thuẫn. Bổ đề được dùng ở đây là phiên bản tổng quát:

**Nếu một số nguyên tố chia hết một tích (hoặc một bình phương) thì nó chia hết một thừa số (hoặc cơ số).**

Với số nguyên tố $$p$$ bất kỳ, cùng lập luận cho thấy $$\sqrt{p}$$ vô tỷ. Với $$n$$ không phải số chính phương, $$\sqrt{n}$$ vô tỷ; cách chứng minh gọn nhất hiện nay dùng định giá $$v_p$$ từ định lý phân tích thừa số nguyên tố duy nhất. Chứng minh cho $$\sqrt{2}$$ là khởi đầu của cả họ kết quả này.

---

## 8. Vì sao kết quả này quan trọng

- **Mẫu mực của sự chặt chẽ trong lý thuyết số.** Một giả thiết về số nguyên dẫn đến mâu thuẫn thông qua tính chia hết.  
- **Cửa ngõ vào đại số.** Nghiệm của đa thức, số nguyên đại số, mở rộng trường đều phát triển từ câu hỏi "số này có hữu tỷ không".  
- **Văn hóa chứng minh.** Đưa về dạng chuẩn (tối giản), bổ đề chẵn lẻ, phương pháp xuống thang là những công cụ dùng lại được nhiều lần.  
- **Ý thức lịch sử.** Sự không thông ước buộc toán học Hy Lạp phải vượt ra ngoài cách đo chỉ bằng số hữu tỷ.

Trong [cuộc trò chuyện với Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) về cuốn sách *Six Math Essentials*, Terence Tao đặt cú sốc này vào câu chuyện dài hơn về **việc mở rộng hệ thống số**. Phép đếm dẫn đến phép cộng và phép trừ; phép trừ đòi hỏi phải tạo ra số âm và số không để đẳng thức $$(A-B)+B=A$$ vẫn đúng khi $$B>A$$. Phép chia dẫn đến phân số. Rồi xuất hiện những độ dài nằm giữa mọi phân số: $$\sqrt{2}$$ không thể là một tỷ số, và từ Latin *irrational* phản ánh cảm giác "phi lý" đó. Về sau, căn bậc hai của số âm không nằm trong tập số thực, dẫn đến số phức, và số phức lại trở thành ngôn ngữ tự nhiên của điện từ học và cơ học lượng tử. Bài học ở đây không phải là "phần thập phân kéo dài mãi". Bài học là các loại số mới thường được tạo ra để các quy tắc đại số cũ tiếp tục đúng, và sau đó hóa ra lại mô tả được thế giới thực. Bài tổng hợp: [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/).

---

## Hiểu lầm thường gặp

1. "Phần thập phân không kết thúc thì vô tỷ." Sai: $$1/3$$ có phần thập phân tuần hoàn.  
2. "Điều kiện tối giản chỉ để cho đẹp." Sai: nếu không có điều kiện tối thiểu hoặc lập luận xuống thang, việc "cả hai đều chẵn" chưa phải là mâu thuẫn.  
3. "Chứng minh cho thấy $$\sqrt{2}$$ không xấp xỉ được bằng số hữu tỷ." Sai.  
4. "Việc $$p^2$$ chẵn kéo theo $$p$$ chẵn là tính chất riêng của số 2." Sai: với mọi số nguyên tố đều có kết quả tương tự.  
5. "Khi trình bày ý tưởng chứng minh thì bỏ qua bổ đề về bình phương số lẻ." Sai: bổ đề đó *chính là* mấu chốt; hãy nêu tên nó.

---

## Kiến thức rút ra từ nghiên cứu video

Tóm tắt để thảo luận (đã đối chiếu với tài liệu viết; **không bịa nội dung video**). Bộ tư liệu: `research/video-research/irrationality-sqrt2/analysis.md`.

### Tình trạng

**Đã được chứng minh** (truyền thống Pythagore / Euclid). Có nhiều chứng minh độc lập (chẵn lẻ, xuống thang, phân tích thừa số duy nhất, chứng minh hình học của Apostol).

### Phát biểu cốt lõi

$$\sqrt{2}$$ là số vô tỷ: nếu $$a/b$$ là phân số tối giản với $$a^2=2b^2$$ thì $$a$$ và $$b$$ đều chẵn, mâu thuẫn.

### Các định nghĩa cần nắm chắc

- **Số hữu tỷ.** $$x=a/b$$ với $$a,b\in\mathbb{Z}$$, $$b\neq 0$$.
- **Xuống thang vô hạn (ý tưởng).** Từ một nghiệm nguyên dương tạo ra một nghiệm nhỏ hơn thực sự; điều này không thể lặp mãi.

### Những nhầm lẫn khái niệm cần tránh

- Nghĩ rằng chứng minh chỉ đúng cho √2, không áp dụng được cho các số nguyên tố (chẳng hạn $$p\equiv 3\pmod 4$$) khi điều chỉnh lập luận chẵn lẻ.
- Nhầm tính vô tỷ với tính siêu việt.


---

## Nguồn video (bộ tư liệu nghiên cứu video)

Video dùng để **định hướng và làm quen với không khí nghiên cứu**, không thay thế chứng minh hay bài báo gốc với những khẳng định then chốt. Đánh giá chi tiết: `research/video-research/irrationality-sqrt2/`.

**Thứ tự gợi ý**

1. **Định hướng** — D!NG — A Proof That The Square Root of Two Is Irrational: [https://www.youtube.com/watch?v=LmpLlcNjPj0](https://www.youtube.com/watch?v=LmpLlcNjPj0).  
2. **Cốt lõi** — Wrath of Math — Most Beautiful Proof √2 irrational (chứng minh hình học của Apostol): [https://www.youtube.com/watch?v=NegYPgMAua4](https://www.youtube.com/watch?v=NegYPgMAua4).  
3. **Tổng quan** — Tipping Point Math — 5 Best Proofs √2 irrational: [https://www.youtube.com/watch?v=zEXcsZo4hOQ](https://www.youtube.com/watch?v=zEXcsZo4hOQ).  
4. **Nền tảng** — Khan Academy — Proof √2 is irrational: [https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:irrational-numbers/x2f8bb11595b61c86:proofs-concerning-irrational-numbers/v/proof-that-square-root-of-2-is-irrational](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:irrational-numbers/x2f8bb11595b61c86:proofs-concerning-irrational-numbers/v/proof-that-square-root-of-2-is-irrational).  

**Nhắc lại tình trạng:** **Đã được chứng minh** (truyền thống Pythagore / Euclid). Có nhiều chứng minh độc lập (chẵn lẻ, xuống thang, phân tích thừa số duy nhất, chứng minh hình học của Apostol).

---


### Phụ đề và khung hình (trích xuất hàng loạt)

Phụ đề và các đoạn theo thời gian: `research/video-research/irrationality-sqrt2/transcripts/` · trạng thái: `research/video-research/irrationality-sqrt2/TRANSCRIPT_STATUS.md` · tổng hợp: `research/video-research/NONFLAGSHIP_TRANSCRIPTS.md`.

![Frame mẫu video]({{ site.baseurl }}/img/video_research/nonflagships/irrationality-sqrt2_NegYPgMAua4_thumb.jpg)

*Hình. Khung hình mẫu từ video chính (xem bộ tư liệu để biết mốc thời gian).*

## Tài liệu

1. Truyền thống Hy Lạp về các đại lượng không thông ước (tài liệu lịch sử).  
2. Sách nhập môn về chứng minh: chương về phản chứng và số nguyên.  
3. Hardy & Wright — *An Introduction to the Theory of Numbers*.  
4. Trong khóa học: [Euclid và vô hạn số nguyên tố]({{ site.baseurl }}/contents/vi/chapter05/05_02_Euclid_Infinite_Primes/); [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/) cho cách nhìn của Tao về hệ thống số.
5. Terence Tao — Big Think OOMx2BHHWtE: https://www.youtube.com/watch?v=OOMx2BHHWtE

---


Danh sách URL đầy đủ: `research/video-research/irrationality-sqrt2/references.md`.

### Video (thứ tự gợi ý)

- D!NG — A Proof That The Square Root of Two Is Irrational (Định hướng): https://www.youtube.com/watch?v=LmpLlcNjPj0
- Wrath of Math — Most Beautiful Proof √2 irrational (Apostol geometric) (Cốt lõi): https://www.youtube.com/watch?v=NegYPgMAua4
- Tipping Point Math — 5 Best Proofs √2 irrational (Tổng quan): https://www.youtube.com/watch?v=zEXcsZo4hOQ
- Khan Academy — Proof √2 is irrational (Nền tảng): https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:irrational-numbers/x2f8bb11595b61c86:proofs-concerning-irrational-numbers/v/proof-that-square-root-of-2-is-irrational

### Bài báo và trang web (từ bộ tư liệu)

- Wikipedia — Square root of 2 / proofs of irrationality: https://en.wikipedia.org/wiki/Square_root_of_2
- Apostol, AMM 2000 geometric proof (reference): https://www.jstor.org/stable/2589021
- Homeschoolmath writeup of classical proof: https://www.homeschoolmath.net/teaching/proof_square_root_2_irrational.php
- Wikipedia — Proof that √2 is irrational: https://en.wikipedia.org/wiki/Square_root_of_2#Proofs_of_irrationality
- MathWorld — Irrational Number: https://mathworld.wolfram.com/IrrationalNumber.html

### Trong khóa học

- Bộ tư liệu: `research/video-research/irrationality-sqrt2/` (đặc biệt là `references.md`, `learning_path.md`).

## Hướng đi tiếp

- Tổng quát cho $$\sqrt{n}$$ với $$n$$ không phải số chính phương.  
- Liên phân số của $$\sqrt{2}$$, mặt xây dựng của tính vô tỷ (cho các xấp xỉ hữu tỷ tốt nhất).  
- So sánh với chứng minh tính vô tỷ của $$e$$ và $$\pi$$ (khó hơn, cần công cụ khác).  
- Ghi lại chính xác một câu hỏi bạn vẫn còn thắc mắc.


## Khuôn mẫu chứng minh phản chứng cổ điển

Giả sử $$\sqrt{2}=p/q$$ tối giản; suy ra $$p$$ và $$q$$ đều chẵn, mâu thuẫn. Khuôn mẫu này dạy ta: (1) làm việc trong $$\mathbb{Z}$$, (2) dùng tính chẵn lẻ hoặc định giá, (3) điều kiện tối giản là giả thiết then chốt. Mở rộng: $$\sqrt{d}$$ với $$d$$ không có ước chính phương; về sau sẽ liên hệ với mở rộng trường.

## Vì sao một bài "dễ" vẫn nằm trong chương các chứng minh nổi tiếng

Lý do không nằm ở kỹ thuật, mà ở chỗ nó **thay đổi quan niệm về số** của người Hy Lạp: đường chéo không còn là tỷ số của hai số nguyên. Khi thảo luận, nên nhấn mạnh bước ngoặt về khái niệm này, chứ không chỉ ba dòng biến đổi đại số.

## Video tham khảo

- **Xem trước:** [The Most Beautiful Proof sqrt(2) is Irrational](https://www.youtube.com/watch?v=NegYPgMAua4) — Wrath of Math, tiếng Anh. Chứng minh hình học ngắn gọn cho tính vô tỷ của √2; nên xem trước khi đọc bài.
- [The 5 Best Proofs that the Square Root of 2 is Irrational](https://www.youtube.com/watch?v=zEXcsZo4hOQ) — Tipping Point Math, tiếng Anh. Năm cách chứng minh khác nhau; nên xem sau khi đã nắm ý chính của bài.
