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

Số $$\sqrt{2}$$ không phải là tỷ số của hai số nguyên. Phát hiện này thuộc về truyền thống Pythagore và thường được kể như một cuộc khủng hoảng của niềm tin rằng mọi độ dài đều thông ước với nhau. Đến nay nó vẫn là một trong những chứng minh nhập môn hay nhất trong giáo dục toán học. Lập luận rất ngắn nhưng **ý tưởng** sâu: giả sử có một biểu diễn tối giản, chỉ ra rằng tử và mẫu cùng chia hết cho 2, và như vậy mâu thuẫn với tính tối giản. Tính chẵn lẻ là chìa khóa để bác bỏ giả thiết "$$\sqrt{2}$$ hữu tỷ".

Bài này trình bày kỹ ý tưởng đó, so sánh với các cách trình bày tương đương (xuống thang vô hạn, phân tích thừa số nguyên tố đơn giản), và đặt kết quả cạnh các chứng minh tính vô tỷ khác. Mục tiêu là bạn có được một khung chứng minh có thể giảng trên bảng trong mười phút, và đủ vững để trả lời câu hỏi trong một giờ.

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

## 1. Thông ước và cách nhìn hình học

Hai độ dài được gọi là **thông ước** nếu có một đơn vị chung sao cho mỗi độ dài bằng một số nguyên lần đơn vị đó; điều này tương đương với tỷ số của chúng là số hữu tỷ. Đường chéo của hình vuông cạnh 1 dài $$\sqrt{2}$$. Nếu $$\sqrt{2}$$ hữu tỷ thì cạnh và đường chéo thông ước. Chứng minh tính vô tỷ cho thấy điều ngược lại: không có cây thước chung nào đo được cả hai một số nguyên lần.

Toán học Hy Lạp không dùng khái niệm số thực như ngày nay; phát hiện này thường được diễn đạt bằng các đại lượng không thông ước. Cách viết hiện đại dùng số nguyên và bình phương vì đó là cách trình bày đại số gọn nhất của cùng ý tưởng.

---

## 2. Định lý và cách đặt vấn đề

**Định lý.** $$\sqrt{2}$$ là số vô tỷ: không tồn tại các số nguyên $$p,q$$ với $$q\neq 0$$ sao cho $$\sqrt{2}=p/q$$.

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

Vậy $$q^2$$ chẵn, nên $$q$$ chẵn. Như thế 2 chia hết cả $$p$$ lẫn $$q$$, mâu thuẫn với $$\gcd(p,q)=1$$.

Do đó không có biểu diễn tối giản nào, nghĩa là $$\sqrt{2}$$ vô tỷ.

### Vì sao "bình phương chẵn thì số đó chẵn"

Nếu $$p=2m+1$$ thì

$$
p^2=4m^2+4m+1
$$

là số lẻ. Vậy $$p^2$$ chẵn chỉ khi $$p$$ chẵn. Thực chất đây là phép tính modulo 2:

$$
p\equiv 0\ \text{hoặc}\ 1\pmod{2},\qquad p^2\equiv 0\ \text{hoặc}\ 1\pmod{2}.
$$

---

## 4. Ý tưởng cốt lõi *là* gì

- **Giả sử số đó hữu tỷ** và viết ở dạng chuẩn (tối giản).  
- **Chuyển tính chia hết** từ $$p^2$$ sang $$p$$ nhờ lập luận modulo.  
- **Lặp lại** cho $$q$$ sau khi thay vào.  
- **Đi đến mâu thuẫn** với dạng chuẩn (có ước chung 2).

Điều quyết định không phải là phần thập phân mà là **tính chia hết**.

---

### Video ngắn: Xuống thang bằng các hình vuông

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/sqrt2-irrational-squares_vi.mp4"></video>
</div>

Một hình minh họa cho phương pháp xuống thang vô hạn: nếu a bình phương bằng hai lần b bình phương, thì đặt hai hình vuông cạnh b vào trong hình vuông cạnh a, phần chồng lên nhau và các phần còn trống sẽ cho ra những hình vuông có cạnh nguyên nhỏ hơn.


## 5. Cách trình bày bằng xuống thang vô hạn

Ta có thể chứng minh mà không cần nhắc đến ước chung lớn nhất. Giả sử $$p^2=2q^2$$ với $$p,q$$ nguyên dương. Khi đó $$p$$ chẵn, $$p=2k$$, và $$q^2=2k^2$$ nên $$q$$ chẵn, $$q=2\ell$$, và

$$
k^2=2\ell^2
$$

với $$k$$ là số nguyên dương và $$k<p$$. Lặp lại mãi, ta được một dãy số nguyên dương giảm vô hạn, điều này không thể xảy ra.

Đây là phương pháp **xuống thang vô hạn** của Fermat: từ một nghiệm ta tạo ra một nghiệm nhỏ hơn, và cứ thế mãi. Lập luận bằng phân số tối giản và lập luận xuống thang là hai cách trình bày của cùng một mâu thuẫn.

---

## 6. Ý tưởng cốt lõi *không phải* là gì

- Không phải "phần thập phân của $$\sqrt{2}$$ không kết thúc nên nó vô tỷ". Nhiều số hữu tỷ có phần thập phân không kết thúc ($$1/3=0.333\ldots$$). Số vô tỷ tương đương với phần thập phân không kết thúc *và không tuần hoàn*, nhưng chứng minh tính không tuần hoàn không hề dễ hơn lập luận chẵn lẻ.  
- Không phủ nhận việc xấp xỉ: $$\sqrt{2}$$ *là* giới hạn của các số hữu tỷ; tính vô tỷ chỉ nói nó không bằng một tỷ số, chứ không nói nó không xấp xỉ được.  
- Bản thân chứng minh này không phân loại mọi số vô tỷ và cũng không chứng minh tính siêu việt ($$\sqrt{2}$$ là số đại số).

---

## 7. Mở rộng: $$\sqrt{3}$$ và $$\sqrt{p}$$

Với $$\sqrt{3}$$, giả sử $$p^2=3q^2$$ ở dạng tối giản. Khi đó $$3\mid p^2$$ kéo theo $$3\mid p$$ (vì 3 là số nguyên tố); đặt $$p=3k$$, ta được $$q^2=3k^2$$, suy ra $$3\mid q$$, mâu thuẫn. Bổ đề được dùng ở đây là phiên bản tổng quát:

**Nếu một số nguyên tố chia hết một tích (hoặc một bình phương) thì nó chia hết một thừa số (hoặc cơ số).**

Với số nguyên tố $$p$$ bất kỳ, cùng lập luận cho thấy $$\sqrt{p}$$ vô tỷ. Với $$n$$ không phải số chính phương, $$\sqrt{n}$$ vô tỷ; cách chứng minh gọn nhất hiện nay dùng định lý phân tích thừa số nguyên tố duy nhất. Chứng minh cho $$\sqrt{2}$$ là khởi đầu của cả họ kết quả này.

---

## 8. Vì sao kết quả này quan trọng

- **Mẫu mực của sự chặt chẽ trong lý thuyết số.** Một giả thiết về số nguyên dẫn đến mâu thuẫn thông qua tính chia hết.  
- **Cửa ngõ vào đại số.** Nghiệm của đa thức, số nguyên đại số, mở rộng trường đều phát triển từ câu hỏi "số này có hữu tỷ không".  
- **Văn hóa chứng minh.** Đưa về dạng chuẩn (tối giản), bổ đề chẵn lẻ, phương pháp xuống thang là những công cụ dùng lại được nhiều lần.  
- **Ý thức lịch sử.** Sự không thông ước buộc toán học Hy Lạp phải vượt ra ngoài cách đo chỉ bằng số hữu tỷ.

Trong [cuộc trò chuyện với Big Think](https://www.youtube.com/watch?v=OOMx2BHHWtE) về cuốn sách sắp ra mắt *Six Math Essentials*, Terence Tao đặt cú sốc này vào câu chuyện dài hơn về **việc mở rộng hệ thống số**. Phép đếm dẫn đến phép cộng và phép trừ; phép trừ đòi hỏi phải tạo ra số âm và số không để đẳng thức $$(A-B)+B=A$$ vẫn đúng khi $$B>A$$. Phép chia dẫn đến phân số. Rồi xuất hiện những độ dài nằm giữa mọi phân số: $$\sqrt{2}$$ không thể là một tỷ số, và từ Latin *irrational* phản ánh cảm giác "phi lý" đó. Về sau, căn bậc hai của số âm không nằm trong tập số thực, dẫn đến số phức, và số phức lại trở thành ngôn ngữ tự nhiên của điện từ học và cơ học lượng tử. Bài học ở đây không phải là "phần thập phân kéo dài mãi". Bài học là các loại số mới thường được tạo ra để các quy tắc đại số cũ tiếp tục đúng, và sau đó hóa ra lại mô tả được thế giới thực. Bài tổng hợp: [Sáu Điều Cốt Yếu]({{ site.baseurl }}/contents/vi/chapter04/04_01_Six_Math_Essentials/).

---

## 9. Phác thảo chứng minh thứ hai (dùng phân tích thừa số nguyên tố)

Giả sử $$p^2=2q^2$$. Phân tích $$p$$ và $$q$$ thành tích các số nguyên tố. Số mũ của 2 ở vế trái là số chẵn (vì là một bình phương); ở vế phải là 1 cộng một số chẵn (thừa số 2 cộng với số mũ chẵn trong $$q^2$$), tức là số lẻ. Mâu thuẫn. Viết bằng định giá $$v_2$$: $$v_2(p^2)$$ chẵn nhưng $$v_2(2q^2)=1+v_2(q^2)$$ lẻ. Tính chẵn lẻ của định giá là cách viết hiện đại của lập luận chẵn lẻ cổ điển.

---

## Hiểu lầm thường gặp

1. "Phần thập phân không kết thúc thì vô tỷ." Sai: $$1/3$$ có phần thập phân tuần hoàn.  
2. "Điều kiện tối giản chỉ để cho đẹp." Sai: nếu không có điều kiện tối thiểu hoặc lập luận xuống thang, việc "cả hai đều chẵn" chưa phải là mâu thuẫn.  
3. "Chứng minh cho thấy $$\sqrt{2}$$ không xấp xỉ được bằng số hữu tỷ." Sai.  
4. "Việc $$p^2$$ chẵn kéo theo $$p$$ chẵn là tính chất riêng của số 2." Sai: với mọi số nguyên tố đều có kết quả tương tự.  
5. "Khi trình bày ý tưởng chứng minh thì bỏ qua bổ đề về bình phương số lẻ." Sai: bổ đề đó *chính là* mấu chốt; hãy nêu tên nó.

---

## Bài tập

1. Viết đầy đủ chứng minh cổ điển cho tính vô tỷ của $$\sqrt{2}$$, kể cả bổ đề về bình phương số lẻ.  
2. Chứng minh $$\sqrt{3}$$ vô tỷ theo cùng cách.  
3. Nếu thử chứng minh $$\sqrt{4}$$ vô tỷ thì lập luận sai ở đâu? (Số này *hữu tỷ*.)  
4. Viết lại chứng minh cho $$\sqrt{2}$$ chỉ bằng phương pháp xuống thang, không dùng ước chung lớn nhất.  
5. Dùng phân tích thừa số nguyên tố, giải thích mâu thuẫn về định giá với $$p^2=2q^2$$.  
6. Đúng hay sai: nếu $$x^2$$ chia hết cho 4 thì $$x$$ chia hết cho 4? Chứng minh hoặc đưa phản ví dụ; so sánh với trường hợp chia hết cho 2.  
7. **Viết giải thích (không quá 300 từ).** Giải thích cho một học sinh đã biết chẵn/lẻ nhưng chưa biết khái niệm "vô tỷ".  
8. Không bắt buộc: chứng minh $$\sqrt[3]{2}$$ vô tỷ bằng một lập luận chia hết tương tự.

---


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

## Bài thực hành

Chứng minh $$\sqrt{3}$$ vô tỷ theo cùng khuôn mẫu; chỉ ra bước nào không còn đúng nếu thay bằng $$\sqrt{4}$$. Viết một câu nối kết quả này với tính trù mật của số hữu tỷ và số vô tỷ trên $$\mathbb{R}$$.


## Video tham khảo

- **Xem trước:** [The Most Beautiful Proof sqrt(2) is Irrational](https://www.youtube.com/watch?v=NegYPgMAua4) — Wrath of Math, tiếng Anh. Chứng minh hình học ngắn gọn cho tính vô tỷ của √2; nên xem trước khi đọc bài.
- [The 5 Best Proofs that the Square Root of 2 is Irrational](https://www.youtube.com/watch?v=zEXcsZo4hOQ) — Tipping Point Math, tiếng Anh. Năm cách chứng minh khác nhau; nên xem sau khi đã nắm ý chính của bài.
